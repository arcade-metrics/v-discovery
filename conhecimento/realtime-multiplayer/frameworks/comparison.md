---
id: rtm.fw.comparison
titulo: Comparação de frameworks de multiplayer e tempo real
tipo: comparacao
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nakama2026github, nakama2026github-api, nakama2026github-api-release, nakama2026license, nakama2026docs-architecture, nakama2026docs-authoritative, nakama2026docs-relayed, nakama2026docs-matchmaker, nakama2026docs-status, nakama2026docs-session, nakama2026docs-storage, nakama2026docs-runtime, nakama2026docs-benchmarks, heroiclabs2026enterprise, heroiclabs2026cloud, colyseus2026github, colyseus2026github-api, colyseus2026github-api-releases, colyseus2026license, colyseus2026docs-intro, colyseus2026docs-state, colyseus2026docs-schema, colyseus2026docs-matchmaker, colyseus2026docs-queue, colyseus2026docs-presence, colyseus2026docs-reconnection, colyseus2026docs-relay, colyseus2026docs-transport, colyseus2026docs-scalability, colyseus2026docs-auth, colyseus2026docs-cloud, colyseus2026docs-faq, photon2026fusion-intro, photon2026fusion-topologies, photon2026fusion-pricing, photon2026realtime-intro, unity2026ngo-manual, unity2026ngo-authority, unity2026ngo-distributed, unity2026ngo-license, unity2026ngo-github-api, unity2026transport, unity2026mps-sdk, unity2026ugs-pricing, socketio2026docs, socketio2026docs-multiple-nodes, socketio2026github-api, socketio2026github-api-release, ably2026platform, ably2026connect, ably2026pricing]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.fw.nakama }
  - { tipo: relacionado-a, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.fw.alternatives }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.arch.relay-server }
  - { tipo: relacionado-a, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.sync.state-replication }
  - { tipo: relacionado-a, alvo: rtm.mp.matchmaking }
  - { tipo: relacionado-a, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.perf.load-testing }
termos: [sincronização automática de estado, sincronização manual de estado, serviço gerenciado, maturidade de projeto]
---

# Comparação de frameworks de multiplayer e tempo real

## Definição e terminologia

Esta comparação coloca lado a lado Nakama (`rtm.fw.nakama`), Colyseus (`rtm.fw.colyseus`) e quatro alternativas representativas de categorias distintas de `rtm.fw.alternatives`: Photon Fusion (netcode de engine proprietário com nuvem), Unity Netcode for GameObjects (netcode de engine de código aberto), Socket.IO (biblioteca de transporte e pub/sub) e Ably (pub/sub gerenciado). A escolha das quatro pretende cobrir uma de cada categoria, não ranquear produtos [I].

Convenções das tabelas [I]:

- **Sincronização de estado**: *automática via schema* quando o framework serializa e difunde o estado declarado; *manual* quando o desenvolvedor serializa e envia mensagens; *replicação por atributos* quando a engine replica campos marcados.
- **Modelo de autoridade**: *autoritativo* (servidor ou host decide), *relay* (servidor repassa sem validar), *distribuída* (clientes donos de objetos), *nenhum* (a biblioteca não define).
- **Maturidade**: ano de criação do repositório no GitHub e data do último push ou release na consulta de 2026-10-29. Isso mede atividade, não qualidade [I].

Todas as células com fato trazem marca `[F]`; onde a documentação não cobre o item, consta "não documentado" ou "não verificado".

## Fundamentos e funcionamento

### Tabela 1: licença, linguagem, autoridade, transporte, sincronização

| Critério | Nakama | Colyseus | Photon Fusion | Unity NGO | Socket.IO | Ably |
|---|---|---|---|---|---|---|
| Licença / modelo | Apache-2.0; licenças comerciais para Enterprise [F: nakama2026license; heroiclabs2026enterprise] | MIT [F: colyseus2026license] | Proprietário, planos por CCU; 20 CCU dev e 100 CCU Launch grátis, 500 CCU a US$ 125/mês [F: photon2026fusion-pricing] | MIT [F: unity2026ngo-license] | MIT [F: socketio2026github-api] | Serviço proprietário; Free com 6 M msgs/mês e 200 conexões; Standard US$ 29/mês [F: ably2026pricing] |
| Linguagem do servidor | Go; extensões em Go, Lua, TypeScript/JavaScript (ES5) [F: nakama2026github-api; nakama2026docs-runtime] | Node.js/TypeScript (ou Bun) [F: colyseus2026github-api; colyseus2026docs-intro] | C# em Unity (servidor dedicado é build headless Unity) [F: photon2026fusion-topologies] | C# em Unity 6.0+ [F: unity2026ngo-manual] | JavaScript/Node.js [F: socketio2026docs] | Não aplicável (SaaS); SDKs multiplataforma [F: ably2026platform] |
| Modelo de autoridade | Relay e autoritativo (match handler) [F: nakama2026docs-relayed; nakama2026docs-authoritative] | Autoritativo; relay via `RelayRoom` [F: colyseus2026github; colyseus2026docs-relay] | Autoritativo (Dedicated Server, Client Host) e distribuído (Shared Authority) [F: photon2026fusion-topologies] | Autoritativo (server/host) e distribuído (distributed authority) [F: unity2026ngo-authority; unity2026ngo-distributed] | Nenhum embutido [F: socketio2026docs] [I] | Nenhum; pub/sub com LiveObjects para estado convergente [F: ably2026platform] |
| Transporte | WebSocket e rUDP, payload protobuf ou JSON; gRPC/HTTP para requisições [F: nakama2026docs-architecture] | WebSocket padrão (`ws`); uWebSockets.js, WebTransport, Bun [F: colyseus2026docs-transport] | UDP com NAT punch-through e relay (Client Host); dedicado com IP público [F: photon2026fusion-topologies]; camada Photon Realtime oferece UDP confiável, TCP e WebSocket [F: photon2026realtime-intro] | Unity Transport sobre UDP ou WebSocket; WebGL só WebSocket [F: unity2026transport] | HTTP long-polling, WebSocket, WebTransport com fallback [F: socketio2026docs] | "Typically WebSockets", multiplexado [F: ably2026connect] |
| Sincronização de estado | Manual: estado em memória do match, broadcast explícito [F: nakama2026docs-authoritative] | Automática via Schema com patches delta binários a cada 50 ms (padrão) [F: colyseus2026docs-state] | Replicação por atributos (networked properties, RPCs), compressão e área de interesse [F: photon2026fusion-intro] | Replicação por NetworkVariables e RPCs [F: unity2026ngo-distributed; unity2026ngo-authority] | Manual (eventos) [F: socketio2026docs] | Manual (mensagens) ou LiveObjects [F: ably2026platform] |

### Tabela 2: matchmaking, presença, reconexão, persistência, escala, gerenciado, maturidade

| Critério | Nakama | Colyseus | Photon Fusion | Unity NGO | Socket.IO | Ably |
|---|---|---|---|---|---|---|
| Matchmaking | Matchmaker em lote (intervalo 15 s padrão), tickets com query, parties, hook para criar match [F: nakama2026docs-matchmaker] | `joinOrCreate`/`filterBy`/`sortBy` por sala e `QueueRoom` por rank [F: colyseus2026docs-matchmaker; colyseus2026docs-queue] | Via Photon Realtime: lobbies, random join com filtros, SQL Lobby, tickets [F: photon2026realtime-intro] | Não embutido; Unity Matchmaker e Lobby via Multiplayer Services SDK [F: unity2026mps-sdk] | Não há [I] | Não há [I] |
| Presença | Status social por conexão com follow; presenças de match [F: nakama2026docs-status; nakama2026docs-relayed] | Não há presença de usuário embutida; `Presence` é pub/sub interno entre processos [F: colyseus2026docs-presence] [I] | Não documentado nas páginas abertas | Não documentado nas páginas abertas | Não há; rooms permitem construí-la [I] | Spaces (estado de participantes) e Chat (online status) [F: ably2026platform] |
| Reconexão | Evento de leave distingue desconexão; handler pode reservar lugar; tickets do matchmaker não sobrevivem [F: nakama2026docs-authoritative; nakama2026docs-matchmaker]; refresh de sessão automático em parte dos SDKs [F: nakama2026docs-session] | `allowReconnection` com token; retentativa automática no SDK (15 tentativas, backoff até 5 s) [F: colyseus2026docs-reconnection] | Não documentado nas páginas abertas | Não documentado nas páginas abertas | Reconexão automática com atraso crescente e buffer de pacotes [F: socketio2026docs] | Estado preservado por 2 min após unload; heartbeat 15 s [F: ably2026connect] |
| Persistência embutida | Storage JSON com versões, leaderboards, chat persistente, contas [F: nakama2026docs-storage; nakama2026github] | Só usuários/autenticação via `@colyseus/database`; estado de sala em memória [F: colyseus2026docs-auth] [I] | Não; Photon Server "does not include a persistence layer" [F: photon2026server-intro] | Não [I] | Não [I] | Histórico de mensagens não verificado; LiveObjects persistido em canais [F: ably2026platform] |
| Escala horizontal | Um nó no OSS; cluster (CRDT e gossip) é recurso Enterprise [F: nakama2026docs-architecture] | Um processo por núcleo, Redis obrigatório, cada sala em um processo, proxy NGINX/Traefik [F: colyseus2026docs-scalability] | Photon Cloud (escala do fornecedor); servidor dedicado hospedado pelo cliente [F: photon2026fusion-topologies] | Depende do hosting escolhido [I] | Sticky sessions e adapter (Redis etc.) [F: socketio2026docs-multiple-nodes] | Gerenciada pelo fornecedor [F: ably2026platform] |
| Serviço gerenciado | Heroic Cloud (GCP/AWS, inclui Enterprise, preço por capacidade alocada) [F: heroiclabs2026cloud] | Colyseus Cloud (NGINX e PM2, cobrança mensal antecipada) [F: colyseus2026docs-cloud] | Photon Cloud (Public, Premium, Enterprise) [F: photon2026fusion-pricing] | Unity Multiplayer Services (Relay, Lobby, Matchmaker, Distributed Authority); Multiplay repassado ao Rocket Science em 2026-03-31 [F: unity2026mps-sdk; unity2026ugs-pricing; unity2026multiplay-eos] | Não há oficial [I] | Só gerenciado [F: ably2026platform] |
| Maturidade | Repositório 2017-01; v3.41.0 em 2026-09-18; push 2026-10-29; 13.608 estrelas [F: nakama2026github-api; nakama2026github-api-release] | Repositório 2015-11; colyseus@0.18.10 em 2026-10-22; push 2026-10-26; 7.490 estrelas [F: colyseus2026github-api; colyseus2026github-api-releases] | Fusion 2 (release notes 2.1); código fechado, sem GitHub público verificado [F: photon2026fusion-intro] | Repositório 2018-01; versão 3.1.0; push 2026-10-28; 2.332 estrelas [F: unity2026ngo-github-api; unity2026ngo-manual] | Repositório 2010-03; 4.8.4 em 2026-09-25; push 2026-09-29; 63.228 estrelas [F: socketio2026github-api; socketio2026github-api-release] | SaaS; sem repositório de servidor público [I] |

## Requisitos e pressupostos

- Nakama e Colyseus exigem hospedar o servidor (ou pagar a nuvem do fornecedor); Nakama precisa de banco PostgreSQL wire-compatible, Colyseus precisa de Redis para mais de um processo [F: nakama2026github; colyseus2026docs-scalability].
- Photon Fusion e NGO pressupõem Unity como ambiente de desenvolvimento e de servidor [F: photon2026fusion-topologies; unity2026ngo-manual].
- Socket.IO e Ably pressupõem que a lógica de jogo e o modelo de autoridade serão construídos pela aplicação [I].

## Vantagens e limitações

Síntese do que as fontes documentam, sem juízo de valor [I]:

- **Nakama** concentra serviços (contas, storage, chat, leaderboards, parties) e dois modelos de autoridade, ao custo de sincronização manual e de clustering restrito ao Enterprise [F: nakama2026github; nakama2026docs-authoritative; nakama2026docs-architecture].
- **Colyseus** automatiza a sincronização e a reconexão em uma base pequena (MIT, Node.js), mas não traz serviços de backend além de autenticação e está em versão 0.x com guias de migração a cada minor [F: colyseus2026docs-state; colyseus2026docs-reconnection; colyseus2026docs-intro].
- **Photon Fusion** oferece predição, lag compensation e três topologias na engine, com modelo comercial por CCU e servidores dedicados não hospedados pela Photon [F: photon2026fusion-intro; photon2026fusion-topologies; photon2026fusion-pricing].
- **Unity NGO** é MIT e integrado à engine, com autoridade distribuída dependente de serviço pago acima do free tier e sem matchmaking próprio [F: unity2026ngo-license; unity2026ngo-distributed; unity2026ugs-pricing].
- **Socket.IO** cobre transporte com fallback, reconexão e rooms, mas nada de jogo; escala exige sticky sessions e adapter [F: socketio2026docs; socketio2026docs-multiple-nodes].
- **Ably** entrega pub/sub, presença de participantes e estado convergente como serviço, com SLA contratual só no plano Enterprise [F: ably2026platform; ably2026pricing].

## Alternativas e comparações

### Critérios de escolha

Perguntas que as fontes permitem responder de forma verificável [I]:

1. **Quem valida o estado?** Se o servidor precisa validar (ver `rtm.arch.authoritative-server`), Nakama (match handler), Colyseus (Room), Fusion Dedicated Server e NGO server authority atendem; relay puro (Nakama relayed, Colyseus RelayRoom, Photon Realtime) e pub/sub não validam [F: nakama2026docs-relayed; colyseus2026docs-relay; photon2026realtime-intro].
2. **Quem serializa o estado?** Colyseus, Fusion e NGO serializam campos declarados; Nakama, Socket.IO e Ably exigem serialização própria [F: colyseus2026docs-schema; photon2026fusion-intro; nakama2026docs-authoritative].
3. **A engine é Unity?** Fusion e NGO só existem dentro do Unity; os demais são agnósticos de cliente [F: photon2026fusion-intro; unity2026ngo-manual].
4. **Precisa de serviços de backend além da partida?** Só Nakama documenta storage, leaderboards, chat e parties embutidos [F: nakama2026github].
5. **Qual o orçamento de operação?** Licenças MIT/Apache exigem hospedar e escalar (Redis, PostgreSQL, proxies); Photon e Ably cobram por CCU ou mensagens; Nakama Enterprise e Heroic Cloud não publicam preços [F: photon2026fusion-pricing; ably2026pricing; heroiclabs2026enterprise].
6. **Reconexão é requisito?** Colyseus e Socket.IO documentam reconexão automática do cliente; Nakama expõe primitivas no servidor; Fusion e NGO não cobrem o tema nas páginas abertas [F: colyseus2026docs-reconnection; socketio2026docs; nakama2026docs-authoritative].
7. **Navegador é alvo?** WebSocket está em todos; Colyseus e Socket.IO oferecem WebTransport; Fusion e NGO em WebGL dependem de WebSocket ou relay [F: colyseus2026docs-transport; socketio2026docs; unity2026transport].

## Métricas e métodos de avaliação

Nenhum dos seis publica benchmark comparável entre si [I]. Nakama publica números do fornecedor (20.277 CCU num nó de 1 CPU/3 GB; carga de match autoritativo a 10 ticks/s), sem data nem versão [F: nakama2026docs-benchmarks]. Colyseus publica apenas estimativa de 1.000 a 2.000 conexões por 1 vCPU/1 GB em jogos simples e recomenda testar com `@colyseus/loadtest` [F: colyseus2026docs-faq]. Fusion, NGO, Socket.IO e Ably não trazem números de capacidade nas páginas consultadas. Uma comparação justa exigiria o mesmo cenário (tick, payload, jogadores por sala) medido por terceiros, conforme `rtm.perf.load-testing` [I].

## Exemplo técnico independente de domínio

Mapeamento do mesmo requisito ("sala de 4 jogadores com estado validado no servidor e reentrada após queda") nos dois frameworks de servidor [I]:

```
Nakama                                   Colyseus
------                                   --------
match handler registrado por nome        classe Room definida em defineServer
match_join_attempt: checar lotação       maxClients = 4 (trava automática)
match_loop a N ticks/s:                  setTimestep / setFixedTimestep:
  aplicar mensagens enfileiradas           onMessage por tipo
  broadcast(op, serializar(estado))        patches automáticos a cada patchRate
match_leave(presenca.desconectou=true):  onDrop -> allowReconnection(client, s)
  manter entrada do jogador no estado      marcar jogador como desconectado
rejoin: cliente guarda match_id e        rejoin: cliente guarda reconnectionToken
  chama join de novo; handler decide       e chama client.reconnect(token)
```

## Relações com outros conceitos

A comparação apoia-se em `rtm.fw.nakama`, `rtm.fw.colyseus` e `rtm.fw.alternatives`; os critérios de autoridade remetem a `rtm.arch.comparison`, `rtm.arch.authoritative-server` e `rtm.arch.relay-server`; transporte a `rtm.proto.websocket` e `rtm.proto.udp`; sincronização a `rtm.sync.state-replication`; matchmaking, presença e reconexão a `rtm.mp.matchmaking`, `rtm.mp.presence` e `rtm.rel.reconnection`; avaliação de capacidade a `rtm.perf.load-testing`.

## Lacunas e questões abertas

- Presença e reconexão em Fusion e NGO: não localizadas nas páginas abertas; podem existir em páginas de manual não consultadas.
- Preços de Nakama Enterprise, Heroic Cloud e Colyseus Cloud (planos de computação) não publicados ou não abertos.
- Histórico de mensagens e garantias de entrega de Ably não verificados em página própria.
- Nenhum benchmark independente foi localizado; os números existentes são do fornecedor.
- Ano do primeiro release estável: para Nakama e Colyseus usou-se a data de criação do repositório como proxy; não verifiquei a data de 1.0 (Nakama) ou de 0.1 (Colyseus).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nakama2026github, nakama2026docs-architecture, nakama2026docs-authoritative, nakama2026docs-relayed, nakama2026docs-matchmaker, nakama2026docs-status, nakama2026docs-session, nakama2026docs-storage, nakama2026docs-runtime, nakama2026docs-benchmarks | fornecedor | 2026-10-29 |
| nakama2026github-api, nakama2026github-api-release, nakama2026license | tecnico | 2026-10-29 |
| heroiclabs2026enterprise, heroiclabs2026cloud | fornecedor (marketing) | 2026-10-29 |
| colyseus2026github, colyseus2026docs-intro, colyseus2026docs-state, colyseus2026docs-schema, colyseus2026docs-matchmaker, colyseus2026docs-queue, colyseus2026docs-presence, colyseus2026docs-reconnection, colyseus2026docs-relay, colyseus2026docs-transport, colyseus2026docs-scalability, colyseus2026docs-auth, colyseus2026docs-cloud, colyseus2026docs-faq | fornecedor | 2026-10-29 |
| colyseus2026github-api, colyseus2026github-api-releases, colyseus2026license | tecnico | 2026-10-29 |
| photon2026fusion-intro, photon2026fusion-topologies, photon2026fusion-pricing, photon2026realtime-intro, photon2026server-intro | fornecedor | 2026-10-29 |
| unity2026ngo-manual, unity2026ngo-authority, unity2026ngo-distributed, unity2026transport, unity2026mps-sdk, unity2026ugs-pricing, unity2026multiplay-eos | fornecedor | 2026-10-29 |
| unity2026ngo-license, unity2026ngo-github-api | tecnico | 2026-10-29 |
| socketio2026docs, socketio2026docs-multiple-nodes | fornecedor | 2026-10-29 |
| socketio2026github-api, socketio2026github-api-release | tecnico | 2026-10-29 |
| ably2026platform, ably2026connect, ably2026pricing | fornecedor | 2026-10-29 |
