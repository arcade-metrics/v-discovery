---
id: rtm.mp.session-lifecycle
titulo: Ciclo de vida da sessão multiplayer
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nakama2026authoritative, nakama2026relayed, nakama2026matchmaker, nakama2026projecttemplate, colyseus2026lifecycle, colyseus2026reconnection, colyseus2026room, colyseus2026server, colyseus2026queue]
relacoes:
  - { tipo: complementa, alvo: rtm.mp.rooms-and-matches }
  - { tipo: complementa, alvo: rtm.mp.matchmaking }
  - { tipo: complementa, alvo: rtm.mp.presence }
  - { tipo: complementa, alvo: rtm.mp.turn-based }
  - { tipo: depende-de, alvo: rtm.rel.reconnection }
  - { tipo: depende-de, alvo: rtm.rel.fault-tolerance }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.arch.relay-server }
  - { tipo: relacionado-a, alvo: rtm.sec.authentication }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
termos: [session lifecycle, ready check, host migration, graceful shutdown, consented leave, reconnection window, match result]
---

# Ciclo de vida da sessão multiplayer

## Definição e terminologia

O **ciclo de vida da sessão** é a sequência de fases pelas quais passa uma partida ou sala, do pedido de criação ao registro do resultado: criação, entrada (*join*), prontidão (*ready*), início, execução (com pausas, quedas e reconexões), término, resultado e persistência. O documento rtm.mp.rooms-and-matches trata da sala como unidade; este trata das transições no tempo.

Termos:

- **Consented leave**: saída voluntária, distinta de queda. No Colyseus, `room.leave()` fecha com código `CONSENTED` (4000); quedas não consentidas acionam `onDrop` [F: colyseus2026reconnection].
- **Reconnection window**: tempo em que o assento é mantido para o cliente caído; `allowReconnection(client, seconds | "manual")` [F: colyseus2026reconnection].
- **Host migration**: em modelos sem servidor autoritativo, a escolha de um novo cliente host quando o atual sai [F: nakama2026relayed].
- **Graceful shutdown**: encerramento ordenado do processo; no Colyseus, `gracefullyShutdown` padrão `true`, com `onLeave` recebendo `SERVER_SHUTDOWN` (4001) para todos os clientes e `onDispose` rodando para todas as salas [F: colyseus2026server] [F: colyseus2026lifecycle].

## Problema que resolve

[I] Sem fases explícitas, a lógica de jogo mistura perguntas distintas: a partida já começou? quem está pronto? a saída foi queda ou abandono? o resultado foi gravado? Uma máquina de fases torna cada transição verificável e permite que reconexão, presença e persistência se liguem a pontos definidos.

## Fundamentos e funcionamento

### Criação

Nakama relayed: qualquer usuário cria e recebe um id; um nome opcional faz criadores com o mesmo nome caírem na mesma partida [F: nakama2026relayed]. Nakama autoritativo: criação por RPC (nome do handler e parâmetros, retorna id) ou pelo hook `matchmaker_matched`, que cria a partida e devolve o id; `match_init` retorna estado inicial, tick rate e label [F: nakama2026authoritative] [F: nakama2026matchmaker]. Colyseus: `onCreate(options)` roda "once, when the room is created by the matchmaker"; `options` mescla os valores de `defineRoom()` com os do SDK, com precedência do servidor [F: colyseus2026lifecycle].

### Entrada e autenticação

Colyseus: `onAuth(client, options, context)` "is called before onJoin" e seu retorno fica em `client.auth`; `onJoin` só dispara após `onAuth` bem-sucedido [F: colyseus2026lifecycle]. Nakama autoritativo: `match_join_attempt` decide a admissão e `match_join` registra as presenças [F: nakama2026authoritative]. Ver rtm.sec.authentication.

### Prontidão e início

[I] Nenhum dos frameworks impõe uma fase "ready"; ela é convenção de aplicação. No template do Nakama, o jogo começa quando há dois presentes e `playing` vira verdadeiro; entre jogos há atraso de 5 s [F: nakama2026projecttemplate]. Um *ready check* típico exige confirmação explícita de cada participante dentro de um prazo, devolvendo os faltantes à fila. Nakama observa que jogadores casados pelo matchmaker "are not in the match until they explicitly join, so they can decline" [F: nakama2026authoritative], o que já funciona como um ready implícito.

### Execução, pausa e queda

Nakama autoritativo: `match_loop` roda a cada tick "even with no input"; `match_leave` recebe o motivo (saída ou desconexão), permitindo "hold a disconnected player's seat temporarily" [F: nakama2026authoritative]. Colyseus 0.18: `onDrop(client, code)` dispara em desconexões "without consent"; a documentação recomenda chamar `allowReconnection()` ali e marcar o jogador como desconectado no estado em vez de removê-lo; `onReconnect(client)` dispara quando o assento é retomado, com o mesmo `sessionId`, `auth`, `userData` e `view`; `onLeave` dispara na saída definitiva (consentida, timeout ou falha de reconexão) [F: colyseus2026lifecycle] [F: colyseus2026reconnection]. Se `onDrop` não for definido, `onLeave` cobre os dois casos [F: colyseus2026lifecycle]. Ao reconectar automaticamente, o servidor envia um snapshot completo que o SDK reconcilia na árvore existente [F: colyseus2026reconnection].

[I] "Pausa" é, portanto, um estado derivado: a partida está em execução, mas um ou mais assentos estão em janela de reconexão. A política (congelar o relógio, continuar com forfeit, substituir por bot) é decisão do jogo. O `QueueRoom` do Colyseus prevê preencher vagas "with bots" quando grupos incompletos são permitidos [F: colyseus2026queue].

### Host migration

No Nakama relayed, como o servidor não arbitra, "one client acts as host" para reconciliar estado e tratar mensagens ambíguas; a documentação sugere um método determinístico sem negociação: ordenar presenças por `session_id` e escolher a primeira; quando o host sai, "the remaining clients recalculate it the same way" [F: nakama2026relayed]. [I] A migração implica que o estado autoritativo esteja replicado nos clientes (ou que seja reconstruível) antes da saída do host; caso contrário, a partida se perde. Em servidor autoritativo não há host migration; há *match migration* entre nós: o `match_terminate` do Nakama recebe um período de carência e, no Enterprise, o exemplo migra jogadores para uma nova partida [F: nakama2026authoritative]. Ver rtm.arch.peer-to-peer e rtm.rel.fault-tolerance.

### Término, resultado e persistência

Nakama autoritativo: a partida termina "only when a lifecycle function returns a nil state"; `match_terminate` roda no desligamento com carência em segundos [F: nakama2026authoritative]. Relayed: termina quando todos saem; o id não é reutilizável; partidas "live in memory and can't be persisted" [F: nakama2026relayed]. Colyseus: `onDispose()` roda antes da destruição, "can be async, for example to persist data", quando não há clientes e `autoDispose` é `true` ou após `.disconnect()` [F: colyseus2026lifecycle]. [I] O ponto de persistência do resultado deve ser idempotente: um processo pode cair entre "resultado calculado" e "resultado gravado", e um `graceful shutdown` pode chamar `onDispose` em muitas salas ao mesmo tempo.

## Requisitos e pressupostos

- Identidade de sessão estável para reconexão (Colyseus: `reconnectionToken` deve ser persistido pelo cliente, por exemplo em `sessionStorage`, e muda a cada conexão [F: colyseus2026reconnection]); ver rtm.rel.reconnection.
- Presença confiável para detectar quedas; ver rtm.mp.presence.
- Armazenamento durável para resultado e, no assíncrono, para o estado; ver rtm.mp.turn-based.
- Política de encerramento de partidas vazias (Nakama exige que a lógica trate; o template usa 30 s) [F: nakama2026projecttemplate].

## Vantagens e limitações

[I] Vantagens de fases explícitas: cada gancho tem uma responsabilidade; reconexão e forfeit têm pontos de decisão claros; testes podem enumerar transições. Limitações: frameworks diferem na granularidade dos ganchos (Nakama 7 funções; Colyseus 7 ganchos mais `onUncaughtException`), e portar a máquina de fases entre eles exige mapeamento; estados derivados (pausa, ready) não são nativos.

## Alternativas e comparações

| Fase | Nakama autoritativo | Colyseus 0.18 | Fonte |
|---|---|---|---|
| criar | RPC / matchmaker_matched → match_init | onCreate | [F: nakama2026authoritative] [F: colyseus2026lifecycle] |
| autenticar e admitir | match_join_attempt | onAuth | idem |
| entrar | match_join | onJoin | idem |
| queda | match_leave(motivo) | onDrop | idem |
| retorno | match_join (presença nil readmitida) | onReconnect | [F: nakama2026projecttemplate] [F: colyseus2026reconnection] |
| saída definitiva | match_leave | onLeave | idem |
| laço | match_loop (tick) | setTimestep / setFixedTimestep | [F: colyseus2026room] |
| encerrar | retornar nil; match_terminate | onDispose; disconnect() | idem |

## Métricas e métodos de avaliação

[I] Tempo de formação (criação → início); taxa de abandono em ready check; taxa de reconexão bem-sucedida dentro da janela; partidas encerradas por host migration falha; resultados não persistidos após desligamento. Ver rtm.perf.metrics.

## Exemplo técnico independente de domínio

Máquina de fases genérica com reconexão e resultado, em pseudocódigo:

```
fases: CRIADA, FORMANDO, PRONTA, EM_CURSO, ENCERRANDO, ENCERRADA

CRIADA   --config aceita--> FORMANDO
FORMANDO --entrou(p) [autenticado e há assento]--> FORMANDO
FORMANDO --todos confirmaram ready dentro de T_ready--> PRONTA
FORMANDO --T_ready expirou--> remover não confirmados; se mínimo atendido: PRONTA senão FORMANDO
PRONTA   --iniciar--> EM_CURSO; abrir laço
EM_CURSO --caiu(p)--> EM_CURSO; assento(p) := reservado até agora + T_reconexão
EM_CURSO --voltou(p) [assento reservado]--> EM_CURSO; reenviar snapshot(p)
EM_CURSO --T_reconexão(p) expirou--> aplicar política(p) ∈ {forfeit, bot, continuar}
EM_CURSO --condição de término--> ENCERRANDO; resultado := calcular()
ENCERRANDO --persistir(resultado) idempotente; notificar--> ENCERRADA
ENCERRADA --sem conexões ou após T_pós--> liberar recursos
```

Eleição determinística de host (modelo relay), conforme a sugestão do fornecedor [F: nakama2026relayed]:

```
host := min(presencas, chave = session_id)
ao receber leave(p): se p = host: host := min(presencas restantes, chave = session_id)
```

## Relações com outros conceitos

Complementa rtm.mp.rooms-and-matches, rtm.mp.matchmaking (fase de formação), rtm.mp.presence (detecção de queda) e rtm.mp.turn-based (persistência e forfeit). Depende de rtm.rel.reconnection e rtm.rel.fault-tolerance. Relaciona-se com rtm.arch.peer-to-peer e rtm.arch.relay-server (host migration) e rtm.sec.authentication (admissão). Implementado por rtm.fw.nakama e rtm.fw.colyseus.

## Lacunas e questões abertas

- Não há, nas fontes consultadas, especificação de *ready check* nem de pausa; ambos são convenções de aplicação.
- A migração de partidas entre nós no Nakama Enterprise é mencionada por exemplo de código, sem documentação de garantias (perda de estado, duplicação).
- O comportamento do Colyseus quando um processo cai sem `graceful shutdown` (assentos reservados, salas em `devMode`) não foi verificado além da menção a `devMode` (padrão `false`) [F: colyseus2026server].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nakama2026authoritative | fornecedor | 2026-10-29 |
| nakama2026relayed | fornecedor | 2026-10-29 |
| nakama2026matchmaker | fornecedor | 2026-10-29 |
| nakama2026projecttemplate | tecnico | 2026-10-29 |
| colyseus2026lifecycle | fornecedor | 2026-10-29 |
| colyseus2026reconnection | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| colyseus2026server | fornecedor | 2026-10-29 |
| colyseus2026queue | fornecedor | 2026-10-29 |
