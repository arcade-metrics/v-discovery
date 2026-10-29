---
id: rtm.mp.rooms-and-matches
titulo: Salas, partidas, lobbies e parties
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nakama2026authoritative, nakama2026relayed, nakama2026parties, nakama2026configuration, nakama2026projecttemplate, colyseus2026room, colyseus2026lifecycle, colyseus2026visibility, colyseus2026lobby, colyseus2026scalability, colyseus2026presence, colyseus2026transportws, ellis1989concurrency]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: depende-de, alvo: rtm.arch.relay-server }
  - { tipo: complementa, alvo: rtm.mp.session-lifecycle }
  - { tipo: complementa, alvo: rtm.mp.matchmaking }
  - { tipo: complementa, alvo: rtm.mp.presence }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.sync.interest-management }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
termos: [room, match, lobby, party, presence, seat reservation, tick rate, match label, autoDispose]
---

# Salas, partidas, lobbies e parties

## Definição e terminologia

Uma **sala** (*room*) ou **partida** (*match*) é a unidade de sessão compartilhada de um sistema multiplayer: um conjunto de participantes conectados que recebem os mesmos eventos e, em geral, compartilham um estado. Ellis e Gibbs já descreviam em 1989 a "sessão" de um sistema groupware como um grupo de participantes com interface a um contexto compartilhado, no qual os participantes "são livres para entrar e sair durante uma sessão" [F: ellis1989concurrency, §1]. A terminologia dos frameworks atuais varia:

- **Match** (Nakama): unidade de jogo em tempo real. Pode ser *relayed* (o servidor só repassa mensagens e mantém a lista de presenças) ou *authoritative* (o servidor executa lógica de jogo em um *match handler*) [F: nakama2026relayed] [F: nakama2026authoritative].
- **Room** (Colyseus): "the core building block of Colyseus"; cada instância agrupa um conjunto de clientes que compartilham estado e mensagens [F: colyseus2026room].
- **Party** (Nakama): grupo temporário para atividade social ou de jogo, que "só existe enquanto houver pelo menos um usuário nele"; a documentação distingue parties de *groups* persistentes [F: nakama2026parties].
- **Lobby**: sala de espera ou listagem de salas disponíveis. No Colyseus há um `LobbyRoom` embutido que "provides a live listing of available rooms in your game server" [F: colyseus2026lobby].
- **Presence**: a representação de um participante dentro da sala (Nakama usa `user_id`, `session_id`, `username`); no Colyseus, o termo *Presence* designa outra coisa: a API de comunicação entre processos [F: colyseus2026presence]. Ver rtm.mp.presence.

O que não é: uma sala não é a conexão de transporte (um socket pode participar de várias salas) nem o grupo social persistente (guilda, amigos), que sobrevive à sessão.

## Problema que resolve

[I] Sem uma unidade de sessão, o servidor precisaria decidir, para cada mensagem, quem deve recebê-la e sob qual estado interpretá-la. A sala delimita: (a) o conjunto de destinatários de uma difusão; (b) o estado que é autoridade para aqueles participantes; (c) o ciclo de vida (criação, junção, saída, encerramento); (d) a unidade de alocação de recursos, o que permite escalar horizontalmente distribuindo salas entre processos.

## Fundamentos e funcionamento

### Ciclo join/leave

No Nakama relayed, qualquer usuário cria um match e recebe um id único; outros entram com esse id; "matches cannot be password protected or otherwise closed"; "a match ends when all users have left" e o id não pode ser reutilizado [F: nakama2026relayed]. No Nakama authoritative, o ciclo é governado por sete funções do *match handler* (`match_init`, `match_join_attempt`, `match_join`, `match_leave`, `match_loop`, `match_terminate`, `match_signal`), chamadas apenas pelo servidor; a partida só termina quando uma função retorna estado nulo, e "continua rodando depois que todos saem", ao contrário do relayed [F: nakama2026authoritative].

No Colyseus 0.18, a sala percorre os ganchos `onAuth`, `onCreate`, `onJoin`, `onDrop`, `onReconnect`, `onLeave`, `onDispose`, na ordem "created, authenticated, joined, dropped, reconnected, left, disposed" [F: colyseus2026lifecycle]. `onCreate` é chamado "once, when the room is created by the matchmaker"; `onDispose` roda quando não restam clientes e `autoDispose` é `true` (padrão) ou quando `.disconnect()` é chamado [F: colyseus2026lifecycle].

### Capacidade e acesso

- Colyseus: `maxClients` tem padrão `Infinity` e a sala é "auto-locked when full"; `locked` bloqueia novas entradas em todos os caminhos, mas clientes em reconexão "can still return to their seats"; `private` esconde a sala das listagens e de `join()`/`joinOrCreate()`, mas `joinById()` ainda admite quem tiver o id; `unlisted` esconde das listagens mas continua elegível para `join()` [F: colyseus2026room] [F: colyseus2026visibility].
- Nakama authoritative: a aceitação de entrada é decidida em `match_join_attempt`; o template oficial rejeita com `"match full"` quando `len(presences)+joinsInProgress >= 2` e permite retorno de um usuário cuja presença está `nil` após desconexão [F: nakama2026projecttemplate].
- Nakama party: `maxSize` vai até 256 usuários e "this maximum includes the party leader"; parties abertas admitem sem aprovação e fechadas exigem aceite do líder [F: nakama2026parties].

### Estado da sala

No Nakama authoritative, cada match tem estado em memória, isolado, transformado por entrada validada a cada *tick*; o estado "não é enviado aos clientes automaticamente", a lógica deve chamar *broadcast* com op code e payload [F: nakama2026authoritative]. No relayed, o único estado mantido pelo servidor é o id da partida e a lista de presenças; o servidor "não inspeciona nem armazena" os dados retransmitidos [F: nakama2026relayed]. No Colyseus, `state` é o estado sincronizado, mutável, com `patchRate` padrão de 50 ms (20 fps) [F: colyseus2026room].

### Metadados e descoberta

Nakama usa *match labels* (string ou JSON; só JSON é consultável; limite de 2 KB; atualização recomendada no máximo uma vez por tick) para busca de partidas [F: nakama2026authoritative]. Colyseus usa `metadata`, atualizável via `setMatchmaking()`, e o `LobbyRoom`, notificado "automatically during onCreate(), onJoin(), onLeave() and onDispose()" quando o tipo de sala tem `enableRealtimeListing()`; o lobby envia `rooms` (lista completa), `+` (sala adicionada ou atualizada) e `-` (sala removida) [F: colyseus2026lobby].

### Sala como unidade de escala horizontal

A documentação do Colyseus afirma que "each Room belongs to a single Colyseus process", que aumentar o número de processos "will increase the amount of rooms that can be created", e que as salas são distribuídas "equally" entre os processos; entrar em uma sala tem duas etapas: qualquer processo reserva um assento (*seat reservation*) e o cliente conecta por WebSocket ao processo dono da sala, usando `publicAddress`. Redis é "required for scaling" (`RedisPresence` e `RedisDriver`) [F: colyseus2026scalability]. Nakama afirma que o handler e o estado de um match "live on one Nakama instance", que se torna o host daquele match; cada match "is self-contained and cannot communicate with or affect other matches" [F: nakama2026authoritative].

[I] O padrão comum é: a sala é a unidade atômica de posicionamento; estado da sala nunca é compartilhado entre processos; um diretório ou presença distribuída (Redis no Colyseus, cluster no Nakama Enterprise) mapeia id de sala para processo; o cliente é roteado ao processo correto. A consequência é que a capacidade por sala é limitada pelo processo, e o escalonamento é por número de salas, não por tamanho de uma sala.

## Requisitos e pressupostos

- Identificador de sala único e estável durante a vida da sala (Nakama: id gerado; nome opcional faz dois criadores caírem na mesma partida [F: nakama2026relayed]; Colyseus: `roomId` de 9 caracteres aleatórios, personalizável em `onCreate()` [F: colyseus2026room]).
- Detecção de desconexão por heartbeat para que o `leave` implícito aconteça (Nakama: `socket.ping_period_ms` padrão 15000 e `pong_wait_ms` padrão 25000 [F: nakama2026configuration]; Colyseus: `pingInterval` padrão 3000 ms e `pingMaxRetries` padrão 2 [F: colyseus2026transportws]).
- Em autoritativo, um laço de simulação com *tick rate* cujo trabalho cabe no intervalo; Nakama encerra o match se muitos laços atrasarem e recomenda começar com taxa baixa e subir em passos de 1 a 2 [F: nakama2026authoritative].

## Vantagens e limitações

Vantagens [I]: isolamento de falhas (uma sala com erro não afeta outras); escalonamento linear por salas; modelo mental simples para difusão e autoridade.

Limitações: uma sala muito grande não se divide entre processos (Colyseus: cada processo "has a maximum amount of players it can handle" [F: colyseus2026scalability]); partidas autoritativas ociosas consomem recursos até que a lógica as encerre (Nakama exige tratar o caso, por exemplo encerrar após N ticks vazios; `match.max_empty_sec` padrão 0, sem máximo [F: nakama2026authoritative] [F: nakama2026configuration]); no relayed, não há validação nem persistência [F: nakama2026relayed].

## Alternativas e comparações

| Modelo | Quem mantém o estado | Entrada restrita? | Sobrevive sem jogadores? | Fonte |
|---|---|---|---|---|
| Nakama relayed match | clientes (um host eleito) | não | não | [F: nakama2026relayed] |
| Nakama authoritative match | servidor (handler) | sim, via `match_join_attempt` | sim, até retornar nil | [F: nakama2026authoritative] |
| Nakama party | servidor (membros, líder, label) | sim, aberta/fechada | não | [F: nakama2026parties] |
| Colyseus Room | servidor (`state`) | sim, `lock`/`private`/`maxClients` | só com `autoDispose: false` | [F: colyseus2026room] |

[I] Partidas sem sala explícita (por exemplo, mundo contínuo com *interest management*) resolvem o problema de difusão por área, não por sessão; ver rtm.sync.interest-management.

## Exemplo técnico independente de domínio

Máquina de estados mínima de uma sala genérica, em pseudocódigo:

```
estado Sala:
  id, capacidade, membros: mapa<sessao, Participante>, fase ∈ {aberta, cheia, fechada}

ao criar(opcoes):
  capacidade := opcoes.capacidade; fase := aberta

ao tentar_entrar(sessao, credenciais):
  se fase = fechada: rejeitar("fechada")
  se |membros| ≥ capacidade e sessao ∉ reservas: rejeitar("cheia")
  se não autenticar(credenciais): rejeitar("não autorizado")
  membros[sessao] := novo Participante; notificar(todos, "entrou", sessao)
  se |membros| = capacidade: fase := cheia

ao sair(sessao, motivo):
  remover membros[sessao]; notificar(todos, "saiu", sessao, motivo)
  se fase = cheia: fase := aberta
  se membros vazio e auto_encerrar: encerrar()
```

Diagrama em texto da distribuição por processos:

```
cliente --(1) pedir assento--> qualquer processo --(2) consulta diretório--> sala S em processo P
cliente <--(3) reserva {salaId, processo P, endereço}--
cliente --(4) conectar a P e consumir reserva--> P: sala S.onJoin
```

## Relações com outros conceitos

Depende do modelo de autoridade (rtm.arch.authoritative-server, rtm.arch.relay-server). Complementa rtm.mp.session-lifecycle (fases da partida), rtm.mp.matchmaking (quem entra em qual sala) e rtm.mp.presence (quem está em qual sala). Implementado por rtm.fw.nakama e rtm.fw.colyseus. Relaciona-se com rtm.rel.reconnection (retorno ao assento) e rtm.sync.interest-management (difusão por área em vez de por sala).

## Lacunas e questões abertas

- Não foi verificado o comportamento de replicação de presenças no Nakama Enterprise além da afirmação de que é "transparente" ao handler; os limites de tamanho de match por nó não estão documentados na página consultada.
- A documentação do Colyseus não informa o tempo de expiração padrão de uma *seat reservation* na página de matchmaking.
- Falta evidência empírica pública sobre o número de salas por processo em função do tick rate e do tamanho do estado; a recomendação do Nakama de começar com tick baixo é do fornecedor, não medida.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nakama2026authoritative | fornecedor | 2026-10-29 |
| nakama2026relayed | fornecedor | 2026-10-29 |
| nakama2026parties | fornecedor | 2026-10-29 |
| nakama2026configuration | fornecedor | 2026-10-29 |
| nakama2026projecttemplate | tecnico | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| colyseus2026lifecycle | fornecedor | 2026-10-29 |
| colyseus2026visibility | fornecedor | 2026-10-29 |
| colyseus2026lobby | fornecedor | 2026-10-29 |
| colyseus2026scalability | fornecedor | 2026-10-29 |
| colyseus2026presence | fornecedor | 2026-10-29 |
| colyseus2026transportws | fornecedor | 2026-10-29 |
| ellis1989concurrency | academico | 2026-10-29 |
