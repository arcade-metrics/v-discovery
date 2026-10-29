---
id: rtm.arch.authoritative-server
titulo: Servidor autoritativo (authoritative server)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gambetta2014clientserver, gambetta2014prediction, fiedler2010networking, unity2026topologies, unity2026clientserver, heroiclabs2026multiplayer, heroiclabs2026authoritative, colyseus2026docs, colyseus2026room, colyseus2026state, photon2026hostmigration, knutsson2004p2p]
relacoes:
  - { tipo: alternativa-a, alvo: rtm.arch.relay-server }
  - { tipo: alternativa-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: alternativa-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: alternativa-a, alvo: rtm.arch.event-driven }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: complementa, alvo: rtm.pred.client-side-prediction }
  - { tipo: complementa, alvo: rtm.pred.server-reconciliation }
  - { tipo: complementa, alvo: rtm.pred.entity-interpolation }
  - { tipo: complementa, alvo: rtm.pred.lag-compensation }
  - { tipo: complementa, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: complementa, alvo: rtm.sync.state-synchronization }
  - { tipo: complementa, alvo: rtm.sync.interest-management }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.mp.rooms-and-matches }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
termos: [authoritative server, dedicated server, listen server, host, dumb client, tick, tick rate, match loop, host migration]
---

# Servidor autoritativo (authoritative server)

## Definição e terminologia

Arquitetura cliente-servidor em que o servidor é a única fonte de verdade sobre o estado da simulação: os clientes enviam entradas (comandos), o servidor executa a lógica e devolve o estado resultante. Gambetta formula o princípio assim: "the one and only authority regarding everything that happens in the world is the server" [F: gambetta2014clientserver]. A documentação da Unity descreve a mesma ideia como "the server has final authority on the state of the game" [F: unity2026topologies].

Nomes alternativos: *server-authoritative*, *client-server authoritative*, *authoritative multiplayer* (Nakama) [F: heroiclabs2026multiplayer]. Fiedler, descrevendo a arquitetura de Quake (1996), chama o cliente desse modelo de "dumb terminal": ele apenas envia entradas e interpola as atualizações que recebe [F: fiedler2010networking].

O que não é: não é um servidor relay, que apenas repassa mensagens sem simular (ver rtm.arch.relay-server); não é lockstep, em que todos os participantes simulam e nenhum é autoridade (ver rtm.arch.deterministic-lockstep). A autoridade do servidor é sobre o estado, não sobre a infraestrutura: o processo autoritativo pode rodar em máquina dedicada ou na máquina de um dos jogadores (ver "Variações").

## Problema que resolve

Dois problemas motivam a arquitetura [I]:

1. **Confiança.** Em jogos competitivos um jogador que trapaceia degrada a experiência dos demais. Gambetta recomenda: "Always assume the worst – that players *will* try to cheat"; por isso saúde, posição e outras variáveis de estado não devem ser controladas pelo cliente, que envia apenas intenções do tipo "quero mover uma casa para a direita" [F: gambetta2014clientserver]. Fiedler atribui a Tim Sweeney o resumo "The Server Is The Man" [F: fiedler2010networking].
2. **Consistência com entrada e saída dinâmica.** Fiedler lista como vantagens do modelo cliente-servidor, em relação ao lockstep P2P de Doom: a qualidade da partida depende só da conexão de cada jogador com o servidor, jogadores podem entrar e sair durante a partida, e a banda por jogador cai [F: fiedler2010networking].

## Fundamentos e funcionamento

Fluxo básico de mensagens [I, consolidado de gambetta2014clientserver e fiedler2010networking]:

```
cliente A ──entrada(seq=n)──▶ servidor ──estado(t)──▶ cliente A
cliente B ──entrada(seq=m)──▶ servidor ──estado(t)──▶ cliente B
                               │
                               └─ simula em ticks fixos; valida; aplica; publica
```

O servidor avança a simulação em **ticks** de duração fixa. A documentação do Nakama define a taxa como chamadas por segundo: uma *tick rate* de 10 produz 10 execuções do *match loop* por segundo, iniciadas a cada 100 ms [F: heroiclabs2026authoritative]. O loop é chamado mesmo sem entradas pendentes, para avançar o estado, validar entradas e expulsar jogadores inativos [F: heroiclabs2026authoritative]. Em Colyseus, o intervalo padrão do loop de simulação é 16,6 ms (60 fps) e o estado é enviado aos clientes a cada `patchRate` de 50 ms (cerca de 20 fps) [F: colyseus2026room].

A publicação de estado pode ser automática ou explícita, conforme o framework. Em Colyseus, "Only the server can directly mutate the state"; clientes recebem o estado completo ao entrar e, depois, apenas as propriedades alteradas a cada intervalo de patch [F: colyseus2026state]. Em Nakama, mudanças no estado da partida não são enviadas automaticamente: o código do servidor precisa chamar *broadcast* com um *opcode* [F: heroiclabs2026authoritative].

### Custo de latência

A ida e volta ao servidor é a limitação central. Gambetta observa que mesmo com 50 ms entre cliente e servidor o jogador percebe uma pausa antes de o personagem se mover; em conexões piores, 100, 200 ou 500 ms são comuns, e meio segundo "makes the game unplayable" [F: gambetta2014clientserver]. Fiedler cita Carmack sobre o Quake original: "This gives 300+ ms latencies, minimum" [F: fiedler2010networking]. A documentação da Unity descreve o custo estrutural: "all state changes must be sent from client to server, processed, and then sent back out to other clients" [F: unity2026clientserver].

### Variações

**Dedicated server vs. listen server.** A documentação da Unity distingue o *dedicated server*, em que "a dedicated machine runs only the game simulation", do *listen server*, em que uma única instância roda a simulação e também funciona como cliente jogável [F: unity2026topologies]. Segundo o mesmo fornecedor, o dedicado oferece o maior desempenho e melhores *tick rates* e é resiliente a clientes comprometidos, mas "Dedicated servers are often the most expensive network topology" [F: unity2026topologies; unity2026clientserver]; o listen server não gera custo extra, mas a instância que hospeda é "a single point of failure if the game instance hosting the server is compromised" [F: unity2026topologies].

**Host migration.** Quando o servidor autoritativo roda na máquina de um jogador (*host*), a saída dele exige escolher outro host. A documentação do Photon Fusion descreve o recurso para o modo *Host*: um novo host é escolhido, o último estado armazenado é enviado só a ele, o intervalo de *snapshot* é configurável ("30 second intervals is recommend for most"), apenas o snapshot mais recente fica na nuvem e as mudanças entre o último snapshot e a migração "will be lost" [F: photon2026hostmigration]. [I] A migração reintroduz no modelo autoritativo parte dos problemas de confiança e de disponibilidade típicos de P2P.

**Server-authoritative com predição.** O cliente aplica suas próprias entradas localmente antes de receber a confirmação e reconcilia quando chega o estado do servidor. Gambetta mantém a autoridade: um cliente adulterado pode exibir o que quiser, mas "it wouldn't affect the state of the server" [F: gambetta2014prediction]. O detalhamento está em rtm.pred.client-side-prediction e rtm.pred.server-reconciliation.

## Algoritmos e modelos relevantes

- Loop de simulação em ticks fixos com fila de entradas por cliente (pseudocódigo abaixo).
- Numeração de sequência das entradas, para o servidor informar "o último input processado" e o cliente descartar os já confirmados [F: gambetta2014prediction].
- Reaplicação (*rewind and replay*) no cliente a partir de buffer circular de estados e entradas, descrita por Fiedler para QuakeWorld [F: fiedler2010networking].
- Interpolação no cliente das atualizações recebidas (rtm.pred.entity-interpolation, rtm.sync.snapshot-interpolation).
- Compensação de latência no servidor para ações instantâneas (rtm.pred.lag-compensation).

## Requisitos e pressupostos

- Toda regra que afeta o resultado precisa executar no servidor; o cliente só pode executar cópias para fins de predição [F: gambetta2014prediction].
- O servidor precisa processar o loop dentro do tick: a documentação do Nakama afirma que, se o loop atrasa, o servidor tenta compensar, e se muitos loops atrasarem "the server will end the match" [F: heroiclabs2026authoritative].
- Orçamento de mensagens: o Nakama recomenda payloads dentro de um MTU de 1500 bytes e no máximo uma mensagem por tick por presença; mensagens excedentes podem ser descartadas com erro em log [F: heroiclabs2026authoritative]. Clientes lentos podem encher o buffer de envio e ser desconectados [F: heroiclabs2026authoritative].
- Para predição funcionar, a simulação precisa ser "determinística o bastante": dado um estado e um conjunto de entradas, o resultado deve ser previsível [F: gambetta2014prediction]. Esse requisito é mais fraco que o do lockstep (identidade bit a bit) [I].

## Vantagens e limitações

Vantagens:
- Resistência a trapaça por desenho: o fornecedor Unity associa o servidor dedicado a jogos competitivos que precisam de autoridade central "to minimize cheating and the effects of bad actors" [F: unity2026clientserver].
- Entrada e saída de jogadores durante a partida e banda por jogador menor que em P2P [F: fiedler2010networking].
- Estado persiste independentemente dos clientes: em Nakama, "authoritative matches do not end even if all players have left", o que permite o mundo avançar durante desconexões temporárias [F: heroiclabs2026authoritative].
- Ponto único para validação, persistência e observabilidade [I].

Limitações:
- Latência percebida igual ao RTT até o servidor, sem técnicas complementares [F: gambetta2014clientserver].
- Custo de hospedagem: o servidor dedicado é descrito como a topologia mais cara, com custo de hardware e manutenção [F: unity2026topologies; unity2026clientserver]. Knutsson et al. observam que, no modelo cliente-servidor, "the server has to be over-provisioned to handle peak loads" [F: knutsson2004p2p].
- Escala por sessão limitada pela CPU do nó que hospeda a partida: a documentação do Nakama recomenda a menor *tick rate* aceitável porque taxas menores permitem mais partidas simultâneas por núcleo [F: heroiclabs2026authoritative].
- Complexidade: para esconder a latência é preciso reintroduzir lógica de jogo no cliente; Fiedler cita Carmack: "I am sad to see the elegant client-as-terminal setup go away" [F: fiedler2010networking].

## Alternativas e comparações

Ver rtm.arch.comparison para a tabela completa. Em resumo [I]: relay troca validação por custo; P2P troca servidor por confiança mútua e NAT traversal; lockstep troca envio de estado por determinismo estrito; orientado a eventos troca simulação contínua por log de eventos e consistência eventual.

## Métricas e métodos de avaliação

- RTT cliente-servidor e sua distribuição (rtm.net.latency, rtm.perf.metrics).
- Duração real do tick versus orçamento (atrasos de loop) [F: heroiclabs2026authoritative].
- Mensagens por tick por presença e tamanho de payload em relação ao MTU [F: heroiclabs2026authoritative].
- Partidas simultâneas por núcleo para uma dada tick rate [F: heroiclabs2026authoritative].
- Frequência de correções de predição no cliente (ver rtm.pred.server-reconciliation).

## Exemplo técnico independente de domínio

Pseudocódigo do loop do servidor, em tick fixo [I]:

```
loop_servidor(dt_tick):
  estado = estado_inicial()
  tick = 0
  a cada dt_tick:
    entradas = fila.retirar_todas()            # (cliente_id, seq, comando)
    para cada e em entradas:
      se valida(e, estado):                    # regras executam só aqui
        estado = aplicar(estado, e)
        ultimo_seq[e.cliente_id] = e.seq
    estado = avancar_simulacao(estado, dt_tick)
    para cada c em clientes:
      enviar(c, { tick, ultimo_seq[c], visao(estado, c) })  # visão filtrada
    tick += 1
```

`visao(estado, c)` representa *interest management* (rtm.sync.interest-management); `ultimo_seq` é o que permite a reconciliação no cliente [F: gambetta2014prediction].

## Relações com outros conceitos

É alternativa às outras quatro arquiteturas do domínio. Depende de rtm.net.latency, pois o RTT define a latência mínima percebida. Complementa as técnicas de predição e reconciliação (rtm.pred.*) e as de sincronização de estado (rtm.sync.snapshot-interpolation, rtm.sync.state-synchronization, rtm.sync.interest-management), que existem para mascarar ou reduzir o custo da autoridade central. É implementado por Nakama (modo *authoritative*) [F: heroiclabs2026authoritative] e por Colyseus, que se descreve como framework para "building authoritative game servers, with real-time state synchronization" [F: colyseus2026docs]. Relaciona-se com rtm.sec.cheating (motivação), rtm.mp.rooms-and-matches (unidade de isolamento: em Nakama, "Every running match is self-contained" [F: heroiclabs2026authoritative]) e rtm.rel.reconnection.

## Lacunas e questões abertas

- Bernier (2001), "Latency Compensating Methods in Client/Server In-game Protocol Design and Optimization", e a página "Source Multiplayer Networking" da Valve não puderam ser abertas nesta sessão (bloqueio anti-bot em developer.valvesoftware.com e em espelhos); os valores de tick, interpolação e lag compensation do Source permanecem **não verificados** aqui e devem ser cobertos em rtm.pred.lag-compensation.
- Não foi encontrada fonte verificável com números de custo de hospedagem por jogador-hora; as afirmações de custo são qualitativas (fornecedores).
- Faltam dados empíricos sobre o impacto do *listen server* na latência dos demais jogadores (*host advantage*); a documentação da Unity não usa esse termo [F: unity2026clientserver].
- As versões das documentações de Nakama e Colyseus não estão indicadas nas páginas consultadas; registrar a versão quando o documento de frameworks a confirmar.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gambetta2014clientserver | tecnico | 2026-10-29 |
| gambetta2014prediction | tecnico | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
| unity2026topologies | fornecedor | 2026-10-29 |
| unity2026clientserver | fornecedor | 2026-10-29 |
| heroiclabs2026multiplayer | fornecedor | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| colyseus2026docs | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| colyseus2026state | fornecedor | 2026-10-29 |
| photon2026hostmigration | fornecedor | 2026-10-29 |
| knutsson2004p2p | academico | 2026-10-29 |
