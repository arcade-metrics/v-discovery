---
id: rtm.arch.comparison
titulo: Comparação das arquiteturas de tempo real e multiplayer
tipo: comparacao
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gambetta2014clientserver, gambetta2014prediction, fiedler2010networking, fiedler2014lockstep, fiedler2014networkedphysics, fiedler2015statesync, fiedler2010floatingpoint, bettner2001archers, knutsson2004p2p, rfc8445, rfc8825, heroiclabs2026multiplayer, heroiclabs2026relayed, heroiclabs2026authoritative, colyseus2026relay, colyseus2026room, unity2026topologies, unity2026clientserver, photon2026hostmigration, ggpo2019devguide, microsoft2026eventsourcing, microsoft2026pubsub, microsoft2025cqrs]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.arch.relay-server }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.arch.event-driven }
  - { tipo: complementa, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: complementa, alvo: rtm.sync.state-synchronization }
  - { tipo: complementa, alvo: rtm.sync.state-replication }
  - { tipo: complementa, alvo: rtm.sync.crdt }
  - { tipo: complementa, alvo: rtm.pred.client-side-prediction }
  - { tipo: complementa, alvo: rtm.pred.server-reconciliation }
  - { tipo: complementa, alvo: rtm.pred.lag-compensation }
  - { tipo: complementa, alvo: rtm.pred.comparison }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.fw.comparison }
  - { tipo: relacionado-a, alvo: rtm.perf.qoe-thresholds }
termos: [source of truth, cheat resistance, determinism requirement, per-session scale]
---

# Comparação das arquiteturas de tempo real e multiplayer

## Definição e terminologia

Este documento compara as cinco arquiteturas descritas em `architectures/`: servidor autoritativo (rtm.arch.authoritative-server), relay (rtm.arch.relay-server), peer-to-peer (rtm.arch.peer-to-peer), lockstep determinístico (rtm.arch.deterministic-lockstep) e orientada a eventos (rtm.arch.event-driven). Os critérios são: fonte de verdade, resistência a trapaça, custo de infraestrutura, latência percebida, requisito de determinismo, escala por sessão, complexidade de implementação e adequação a ação, turnos e colaboração.

[I] As arquiteturas não são mutuamente exclusivas em todos os eixos: lockstep é um modelo de sincronização que roda sobre P2P ou relay; "orientada a eventos" descreve organização de estado e comunicação que pode conviver com um servidor autoritativo de ticks baixos. A tabela trata cada uma na forma típica documentada pelas fontes.

## Tabela comparativa

| Critério | Servidor autoritativo | Relay | Peer-to-peer | Lockstep determinístico | Orientada a eventos |
|---|---|---|---|---|---|
| Fonte de verdade | servidor: "the one and only authority" [F: gambetta2014clientserver] | clientes; um host "will reconcile state changes between peers" [F: heroiclabs2026relayed] | cada par; coordenadores por região em overlays [F: knutsson2004p2p] | nenhuma; simulação idêntica em todos [F: fiedler2014lockstep] | event store, "system of record" [F: microsoft2026eventsourcing] |
| Resistência a trapaça | alta por desenho; "to minimize cheating" [F: unity2026clientserver] | nenhuma: "no cheat detection" [F: heroiclabs2026relayed] | baixa: distribuir estado "increases the opportunities for cheating" [F: knutsson2004p2p] | baixa quanto a informação (estado completo em todos) [I]; entradas são verificáveis [I] | depende de onde os comandos são validados; alta se o handler roda no servidor [I] |
| Custo de infraestrutura | mais alto: "often the most expensive network topology" [F: unity2026clientserver] | baixo: servidor só encaminha [F: heroiclabs2026relayed] | mínimo para simulação, mas sinalização e STUN/TURN; TURN "may be expensive" [F: rfc8445] | o do transporte (P2P ou relay) [I] | broker e event store; padrão "complex" e caro de migrar [F: microsoft2026eventsourcing] |
| Latência percebida | RTT ao servidor; 50 ms já é notado, 500 ms "unplayable" [F: gambetta2014clientserver]; mitigável por predição [F: gambetta2014prediction] | um salto cliente-relay-cliente, sem simulação [I] | caminho direto entre pares [F: rfc8825 via rtm.arch.peer-to-peer] | input delay fixo (100 ms no exemplo de Fiedler; 200 ms por turno em AoE) [F: fiedler2014lockstep; bettner2001archers]; zero com rollback [F: ggpo2019devguide] | broker no caminho; inadequado para "near real-time interaction" [F: microsoft2026pubsub] |
| Requisito de determinismo | fraco: "deterministic enough" para predição [F: gambetta2014prediction] | nenhum [I] | nenhum, salvo se usar lockstep [I] | estrito, bit a bit [F: fiedler2014lockstep] | nenhum; handlers devem ser idempotentes [F: microsoft2026eventsourcing] |
| Escala por sessão | limitada por CPU do nó: menor tick rate, mais partidas por núcleo [F: heroiclabs2026authoritative] | limitada por mensagens encaminhadas; sem limite explícito documentado [F: heroiclabs2026relayed] | full mesh O(n²) [I]; overlays por região até milhares simulados [F: knutsson2004p2p] | poucos participantes; latência do mais lento [F: fiedler2010networking] | alta em consumidores (fan-out via topics) [F: microsoft2026pubsub] |
| Complexidade | alta quando combinada com predição e reconciliação [F: fiedler2010networking] | baixa no servidor; protocolo todo no cliente [F: colyseus2026relay] | alta: ICE, eleição de host, replicação [F: rfc8445; knutsson2004p2p] | alta: determinismo "exceptionally difficult" [F: fiedler2010networking] | alta: versionamento, consistência eventual, replay [F: microsoft2026eventsourcing] |
| Ação rápida | adequada com predição; Nakama: "suitable for fast paced real-time gameplay" [F: heroiclabs2026multiplayer] | possível se trapaça irrelevante [F: heroiclabs2026relayed] | histórica (Doom, RTS) via lockstep [F: fiedler2010networking] | RTS e luta (rollback) [F: bettner2001archers; ggpo2019devguide] | inadequada [F: microsoft2026pubsub] |
| Turnos | adequada com tick baixo [F: heroiclabs2026multiplayer] | adequada (1v1, cooperativo) [F: heroiclabs2026relayed] | adequada para poucos jogadores [I] | adequada; 4-5 frames de delay imperceptíveis em tabuleiro [F: ggpo2019devguide] | muito adequada: comandos discretos, auditoria [I] |
| Colaboração | adequada como ponto de serialização [I] | adequada para presença e difusão [I] | adequada com CRDT [I] | inadequada (entrada tardia impraticável) [F: fiedler2010networking] | muito adequada; CQRS para "collaborative environments" [F: microsoft2025cqrs] |

## Discussão

### Fonte de verdade e confiança são o mesmo eixo

[I] As cinco arquiteturas se ordenam por onde fica a verdade: servidor (autoritativo, orientada a eventos com handlers no servidor), um cliente (relay com host), todos os clientes (P2P, lockstep). Quanto mais a verdade se afasta de um componente controlado pelo operador, menor a resistência a trapaça e menor o custo de infraestrutura. Nenhuma fonte consultada apresenta uma arquitetura que combine custo zero de servidor e resistência alta; o fornecedor Nakama trata a escolha entre relayed e authoritative como decisão de design sem "fator decisivo" [F: heroiclabs2026authoritative].

### Latência: onde cada arquitetura paga

- O autoritativo paga RTT ao servidor e mitiga com predição e reconciliação (rtm.pred.client-side-prediction, rtm.pred.server-reconciliation), interpolação de entidades (rtm.pred.entity-interpolation) e compensação de latência (rtm.pred.lag-compensation) [F: gambetta2014prediction; fiedler2010networking].
- O lockstep paga input delay fixo e travamentos quando entradas atrasam; Fiedler mostra que, com TCP, 100 ms e 1% de perda já produzem travamentos a cada poucos segundos, e que entradas redundantes sobre UDP sustentam 2 s de latência e 25% de perda [F: fiedler2014lockstep]. O rollback elimina o delay percebido ao custo de reexecução [F: ggpo2019devguide].
- A orientada a eventos paga o broker; o próprio fornecedor a desaconselha para interação quase em tempo real [F: microsoft2026pubsub].
- P2P e relay pagam apenas o transporte, mas P2P pode cair em TURN [F: rfc8445].

Bettner registra que, em RTS, até 250 ms não era notado e 500 ms constantes eram jogáveis, mas latência variável era pior que latência alta constante [F: bettner2001archers]; o guia do GGPO afirma que em jogos de luta 1 frame de delay já é perceptível [F: ggpo2019devguide]. [I] O limiar depende do gênero, o que remete a rtm.perf.qoe-thresholds.

### Determinismo como custo oculto

Só o lockstep exige determinismo bit a bit; Fiedler documenta que isso é "yes, if…": mesmo compilador, mesma arquitetura, FPU fixada, sem funções transcendentais, com perda de desempenho [F: fiedler2010floatingpoint]. O autoritativo com predição precisa apenas de resultado "completely predictable" dado estado e entradas, pois divergências são corrigidas pelo servidor [F: gambetta2014prediction]. A sincronização por estado de Fiedler dispensa determinismo perfeito ao custo de ser "an approximate and lossy synchronization strategy" [F: fiedler2015statesync]. [I] Esse é o eixo que mais influencia a escolha de linguagem, engine e bibliotecas.

### Banda e escala por sessão

Lockstep tem banda proporcional ao tamanho da entrada [F: fiedler2014lockstep], o que permitiu 8 jogadores e milhares de unidades em 28,8 kbps [F: bettner2001archers]. O autoritativo tem banda proporcional ao estado visível por cliente, mitigada por rtm.sync.interest-management, rtm.sync.delta-compression e priorização; Fiedler cita um orçamento de 256 kbit/s com acumulador de prioridade na sincronização por estado, contra cerca de 18 mbit/s de uma versão inicial de snapshot interpolation [F: fiedler2015statesync]. P2P em full mesh cresce quadraticamente [I]; overlays por região limitam cada jogador à sua vizinhança [F: knutsson2004p2p].

### Disponibilidade do estado

Partidas autoritativas em Nakama "do not end even if all players have left" [F: heroiclabs2026authoritative]; partidas relayed terminam quando o último sai [F: heroiclabs2026relayed]; em P2P com host migration, perde-se o que mudou desde o último snapshot [F: photon2026hostmigration]; em event sourcing, o estado é sempre reconstruível do log [F: microsoft2026eventsourcing]. [I] Para sessões longas, reconexão (rtm.rel.reconnection) e tolerância a falhas (rtm.rel.fault-tolerance), as duas pontas do espectro são autoritativo e event sourcing.

### Combinações documentadas

- Autoritativo + predição + reconciliação: Gambetta partes I e II [F: gambetta2014clientserver; gambetta2014prediction].
- Relay + host em cliente: Nakama relayed [F: heroiclabs2026relayed].
- P2P + lockstep: Doom, Age of Empires [F: fiedler2010networking; bettner2001archers].
- P2P + lockstep + rollback: GGPO [F: ggpo2019devguide].
- Event sourcing + CQRS + pub/sub: Microsoft [F: microsoft2026eventsourcing; microsoft2025cqrs].
- Autoritativo com tick baixo para turnos: Nakama [F: heroiclabs2026multiplayer].

## Métricas e métodos de avaliação

Para comparar arquiteturas em um caso concreto, as métricas mínimas são [I]: latência percebida entre entrada e efeito visível (por gênero), banda por cliente e total por sessão, custo por sessão-hora, taxa de correções (reconciliação ou rollback), taxa de desync, tempo de recuperação após queda de host ou servidor, e proporção de sessões que exigem relay de transporte (TURN). Ver rtm.perf.metrics, rtm.perf.load-testing e rtm.perf.network-emulation.

## Exemplo técnico independente de domínio

Árvore de decisão mínima [I], derivada das fontes acima:

```
trapaça importa?
├─ sim ─▶ ação rápida?
│         ├─ sim ─▶ autoritativo + predição/reconciliação/lag compensation
│         └─ não ─▶ autoritativo com tick baixo  ou  orientada a eventos
└─ não ─▶ estado grande (RTS) ou poucos jogadores com reflexo (luta)?
          ├─ sim ─▶ lockstep (P2P ou relay), rollback se luta
          └─ não ─▶ relay com host  ou  P2P com CRDT (colaboração)
```

## Relações com outros conceitos

Relaciona-se com os cinco documentos de arquitetura. Complementa as técnicas de sincronização (rtm.sync.snapshot-interpolation, rtm.sync.state-synchronization, rtm.sync.state-replication, rtm.sync.crdt) e de predição (rtm.pred.client-side-prediction, rtm.pred.server-reconciliation, rtm.pred.lag-compensation, rtm.pred.comparison), que são as ferramentas que alteram a posição de cada arquitetura nos eixos de latência e banda. Relaciona-se com rtm.sec.cheating (eixo de confiança), rtm.fw.comparison (como os frameworks expõem cada arquitetura) e rtm.perf.qoe-thresholds (limiares por gênero).

## Lacunas e questões abertas

- Não há, nas fontes abertas, comparação quantitativa controlada das cinco arquiteturas sob a mesma carga; as células da tabela combinam fontes heterogêneas (artigos técnicos, documentação de fornecedores, um artigo acadêmico de simulação).
- Bernier (2001) e a página "Source Multiplayer Networking" da Valve não foram acessadas (bloqueio anti-bot); os valores de tick e interpolação do Source ficam **não verificados** neste conjunto.
- Custos de infraestrutura são qualitativos; faltam números de custo por sessão-hora por arquitetura.
- A coluna "orientada a eventos" carece de fonte específica de jogos; baseia-se em padrões de arquitetura corporativa aplicados por interpretação.
- A adequação de P2P com CRDT para colaboração é interpretação; o texto de Shapiro et al. não foi aberto nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gambetta2014clientserver | tecnico | 2026-10-29 |
| gambetta2014prediction | tecnico | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| fiedler2014networkedphysics | tecnico | 2026-10-29 |
| fiedler2015statesync | tecnico | 2026-10-29 |
| fiedler2010floatingpoint | tecnico | 2026-10-29 |
| bettner2001archers | tecnico | 2026-10-29 |
| knutsson2004p2p | academico | 2026-10-29 |
| rfc8445 | normativo | 2026-10-29 |
| rfc8825 | normativo | 2026-10-29 |
| heroiclabs2026multiplayer | fornecedor | 2026-10-29 |
| heroiclabs2026relayed | fornecedor | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| colyseus2026relay | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| unity2026topologies | fornecedor | 2026-10-29 |
| unity2026clientserver | fornecedor | 2026-10-29 |
| photon2026hostmigration | fornecedor | 2026-10-29 |
| ggpo2019devguide | tecnico | 2026-10-29 |
| microsoft2026eventsourcing | fornecedor | 2026-10-29 |
| microsoft2026pubsub | fornecedor | 2026-10-29 |
| microsoft2025cqrs | fornecedor | 2026-10-29 |
