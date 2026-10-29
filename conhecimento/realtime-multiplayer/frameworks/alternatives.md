---
id: rtm.fw.alternatives
titulo: Alternativas a Nakama e Colyseus por categoria
tipo: comparacao
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [photon2026fusion-intro, photon2026fusion-topologies, photon2026fusion-pricing, photon2026realtime-intro, photon2026realtime-pricing, photon2026quantum-intro, photon2026quantum-pricing, photon2026server-intro, unity2026ngo-manual, unity2026ngo-authority, unity2026ngo-distributed, unity2026ngo-license, unity2026ngo-github-api, unity2026transport, unity2026mps-sdk, unity2026ugs-pricing, unity2026multiplay-eos, rocketscience2026hosting, mirror2026readme, mirror2026github-api, mirror2026docs-transports, fishnet2026docs, fishnet2026docs-models, fishnet2026license, fishnet2026github-api, unreal2026networking, agones2026overview, agones2026create-gameserver, agones2026github-api, agones2026github-api-release, gamefabric2026site, gizmodo2026hathora, edgegap2026docs, edgegap2026orchestration, edgegap2026pricing, socketio2026docs, socketio2026docs-multiple-nodes, socketio2026github-api, socketio2026github-api-release, supabase2026realtime, supabase2026realtime-limits, supabase2026realtime-protocol, supabase2026realtime-github-api, ably2026platform, ably2026connect, ably2026pricing, pubnub2026docs, pubnub2026core-concepts, liveblocks2026docs, liveblocks2026how-it-works, liveblocks2026pricing, liveblocks2026license, partykit2026docs, partykit2026how-it-works, partykit2026github-api, yjs2026docs, yjs2026awareness, yjs2026y-websocket, yjs2026license, yjs2026github-api, hocuspocus2026docs, hocuspocus2026github-api]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.fw.nakama }
  - { tipo: relacionado-a, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.fw.comparison }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.arch.relay-server }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.proto.webtransport }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
  - { tipo: relacionado-a, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
termos: [netcode de engine, orquestrador de servidores dedicados, pub/sub gerenciado, infraestrutura de colaboração, autoridade distribuída, relay gerenciado]
---

# Alternativas a Nakama e Colyseus por categoria

## Definição e terminologia

Este documento reúne entradas curtas sobre produtos e projetos que resolvem partes do mesmo problema de Nakama (`rtm.fw.nakama`) e Colyseus (`rtm.fw.colyseus`), organizados em cinco categorias [I]:

- **netcode de engine**: biblioteca de replicação de objetos acoplada a um motor de jogo (Photon Fusion, Netcode for GameObjects, Mirror, FishNet, replicação do Unreal);
- **servidor de jogo / serviço de rede para jogos**: relay, salas e matchmaking como serviço (Photon Realtime, Unity Multiplayer Services, Edgegap Relay);
- **orquestrador de servidores dedicados**: coloca, escala e aloca processos de servidor (Agones, GameFabric/ex-Hathora, Edgegap, Multiplay by Rocket Science);
- **pub/sub gerenciado**: canais, presença e histórico como serviço (Ably, PubNub, Supabase Realtime) ou biblioteca (Socket.IO);
- **colaboração**: estado compartilhado para edição simultânea (Liveblocks, PartyKit, Yjs/Hocuspocus).

Cada entrada registra o que é, categoria, modelo de autoridade suportado, transporte, licença ou modelo comercial e data de consulta (2026-10-29 em todas). Afirmações de marketing são marcadas como tais. Onde uma página oficial não pôde ser aberta, consta "não verificado".

## Netcode de engine

### Photon Fusion (Exit Games)

O que é: SDK de rede para Unity, descrito na documentação como biblioteca de sincronização de estado com compressão de dados, predição do cliente, lag compensation e sistema de área de interesse; versão documentada Fusion 2 (release notes até 2.1) [F: photon2026fusion-intro]. Categoria: netcode de engine com nuvem do fornecedor [I]. Autoridade: três topologias; *Dedicated Server* (servidor headless com "full and exclusive State Authority", não hospedado pela Photon), *Client Host* (host com autoridade total, "a rogue host can cheat", NAT punch-through UDP com cerca de 1 em 10 jogadores caindo em relay) e *Shared Authority* (autoridade distribuída por objeto, Photon Room coordena transferências e guarda o estado) [F: photon2026fusion-topologies]. Transporte: a página de topologias cita UDP e relay; a página de introdução não nomeia protocolo [F: photon2026fusion-topologies; photon2026fusion-intro]. Licença/modelo: proprietário com planos por CCU; grátis para desenvolvimento (20 CCU, 60 GB/mês) e plano Launch de 100 CCU grátis para um app; 500 CCU por US$ 125/mês, 1.000 por US$ 250, 2.000 por US$ 500; Premium a US$ 0,50/CCU com mínimo de US$ 1.000/mês; planos "For Games Only" [F: photon2026fusion-pricing]. Não encontrei declaração de código aberto nas páginas consultadas [I].

### Photon Realtime e Photon Server

O que é: camada base de multiplayer com autenticação, matchmaking (lobbies, filtros, SQL Lobby, tickets) e comunicação entre clientes; não sincroniza objetos, costuma ser combinada com Fusion ou Quantum [F: photon2026realtime-intro]. Arquitetura de Name Server, Master Server e Game Server; clientes falam só com o servidor [F: photon2026realtime-intro]. Categoria: servidor de jogo / relay gerenciado [I]. Autoridade: relay; a página não define quem é autoritativo e deixa ao jogo decidir [F: photon2026realtime-intro]. Transporte: UDP confiável com escolha de sequenciamento e confiabilidade por mensagem, além de TCP e WebSockets [F: photon2026realtime-intro]. Licença/modelo: Public Cloud grátis até 20 CCU (desenvolvimento), 100 CCU por US$ 95 uma vez, 500 CCU por US$ 95/mês, 1.000 por US$ 185, 2.000 por US$ 370; Premium a US$ 0,29/CCU com mínimo de US$ 580/mês; Enterprise sob consulta [F: photon2026realtime-pricing]. Photon Server é a versão on-premises (núcleo C++ sobre UDP confiável, TCP, HTTP e WebSockets; lógica em .NET; sem camada de persistência) e "requires a valid license to run" [F: photon2026server-intro].

### Photon Quantum

O que é: framework ECS determinístico para Unity com predição e rollback, "supporting up to 128 players"; cada cliente roda a simulação localmente e troca apenas inputs; um servidor autoritativo "game-agnostic" na infraestrutura Photon sincroniza relógios e gerencia latência de input, extensível para "referee" [F: photon2026quantum-intro]. Categoria: netcode de engine (lockstep determinístico com rollback; ver `rtm.arch.deterministic-lockstep`) [I]. Transporte: construído sobre a camada Photon Realtime [F: photon2026quantum-intro]. Licença/modelo: proprietário; planos idênticos aos de Fusion (20 CCU dev, 100 CCU Launch grátis, 500/1.000/2.000 CCU por US$ 125/250/500 ao mês, Premium US$ 0,50/CCU) [F: photon2026quantum-pricing]. Versão documentada: Quantum 3, com preview 3.1 [F: photon2026quantum-intro].

### Unity Netcode for GameObjects (NGO)

O que é: biblioteca de alto nível da Unity para rede sobre GameObjects, versão documentada 3.1.0, exige Unity 6.0 ou superior; WebGL requer NGO 1.2.0+ e Unity Transport 2.0.0+ [F: unity2026ngo-manual]. Categoria: netcode de engine [I]. Autoridade: *server authority* (cliente-servidor, com host ou servidor dedicado; "a central authority helps limit cheating") e *distributed authority*, em que cada instância é dona de um subconjunto de objetos, um *session owner* cuida de cenas e late joiners, e a documentação avisa que "cheating can be easier" e que não serve a jogos competitivos com predição [F: unity2026ngo-authority; unity2026ngo-distributed]. O serviço de distributed authority é fornecido pelo pacote Multiplayer Services, com free tier de 6.000 horas de conectividade e 100 GiB/mês [F: unity2026ngo-distributed; unity2026ugs-pricing]. Transporte: Unity Transport 2.x, camada orientada a conexão sobre UDP ou WebSockets, com pipelines opcionais de confiabilidade, ordenação e fragmentação; WebGL só como cliente WebSocket [F: unity2026transport]. Licença: MIT (Copyright 2021 Unity Technologies) [F: unity2026ngo-license]; o GitHub registra o repositório criado em 2018-01-05 com 2.332 estrelas e push em 2026-10-28 [F: unity2026ngo-github-api].

### Unity Multiplayer Services (Lobby, Relay, Matchmaker, Multiplay)

O que é: o SDK Multiplayer Services unifica Lobby, Matchmaker e Relay sob uma API de *sessions* para jogos P2P e com servidor dedicado; Relay "lets players connect securely without dedicated game servers" [F: unity2026mps-sdk]. Categoria: serviço de rede para jogos (relay e matchmaking gerenciados) [I]. Autoridade: relay para jogos hospedados por cliente; o SDK não impõe modelo [I]. Modelo comercial: Relay com os primeiros 50 CCU médios mensais grátis e US$ 0,16 por CCU adicional, banda de 3 GiB/CCU até 150 GiB/mês; Lobby com 10 GiB/mês grátis por grupo regional e US$ 0,09 a 0,16/GiB excedente; preço do Matchmaker não consta na página [F: unity2026ugs-pricing]. Hospedagem de servidores (Multiplay): a Unity encerrou o suporte direto em 2026-03-31 e licenciou o software ao Rocket Science Group; Matchmaker, Relay, Lobby e Distributed Authority seguem [F: unity2026multiplay-eos]. O Rocket Science descreve Multiplay como hospedagem híbrida (bare metal e cinco nuvens) em mais de 40 regiões com alocação "em menos de um segundo" (afirmações de marketing) [F: rocketscience2026hosting]. Transporte do Relay: não verificado nesta sessão (página de conexão retornou 404).

### Mirror

O que é: biblioteca de rede para Unity, "#1 Open Source Unity Networking Library" (slogan); servidor e cliente no mesmo projeto, `NetworkBehaviour`, `[SyncVar]`, `[Command]`, `[ClientRpc]`, `[TargetRpc]`; suporta Unity 2019 a 2022 LTS e 6000.1 [F: mirror2026readme; mirror2026github-api]. Categoria: netcode de engine [I]. Autoridade: definida por componente via SyncDirection, servidor ou cliente autoritativo [F: mirror2026readme]. Transporte: KCP (UDP confiável) como padrão, Telepathy (TCP) e Simple Web Sockets embutidos; multiplexer, simulação de latência, criptografia e relays (Steam, EOS, Edgegap, Light Reflective Mirror) [F: mirror2026docs-transports; mirror2026readme]. Licença: MIT; repositório criado em 2018-07-20, 6.377 estrelas, push em 2026-10-19 [F: mirror2026github-api]. Benchmarks citados no README (400 a 800 CCU em 2022; 480 CCU em 2019 com uMMORPG) são autodeclarados e sem metodologia na página; cifras como "300–700 million players" são marketing [F: mirror2026readme] [I].

### Fish-Networking (FishNet)

O que é: solução de rede para Unity "aimed towards reliability, ease of use, efficiency, and flexibility", sem limite de CCU ou paywall; promete não quebrar APIs em versões maiores e mantém trilhas Release e Development [F: fishnet2026docs]. Categoria: netcode de engine [I]. Autoridade: "server authoritative by design"; modelos documentados: servidor dedicado, host (listen-server) e sem P2P nativo; host migration não é embutida [F: fishnet2026docs; fishnet2026docs-models]. Transporte: sistema de transports plugável; a página de modelos lista relays suportados (Unity Relay, Edgegap, Photon Realtime, EOS, Steam Datagram Relay, BlitzRelay); nomes e protocolos dos transports oficiais (Tugboat, Bayou) não verificados nesta sessão (páginas 404) [F: fishnet2026docs-models]. Licença: custom da FirstGearGames, não é licença OSI; concede uso e modificação para jogos, mas proíbe que "other networking solutions" usem ou reimplementem o software; FishNet-Pro distribuído a equipes de até 20 pessoas [F: fishnet2026license]. GitHub: criado em 2021-08-21, 2.078 estrelas, push em 2026-10-18, licença registrada como "Other" [F: fishnet2026github-api].

### Unreal Engine (replicação nativa)

O que é: o sistema de rede do Unreal usa modelo cliente-servidor em que "the server, as the host of the game, holds the one, true, authoritative game state"; atores com replicação habilitada sincronizam criação, destruição e movimento; propriedades e RPCs (Server, Client, NetMulticast) são declarados pelo desenvolvedor [F: unreal2026networking]. Modos: Standalone, Dedicated Server, Listen Server e Client; três sistemas de replicação: Generic, Replication Graph (escala de muitos atores) e Iris (mais novo, com filtragem e priorização) [F: unreal2026networking]. Categoria: netcode de engine [I]. Autoridade: servidor autoritativo; o listen server dá vantagem ao host [F: unreal2026networking]. Transporte: a página de visão geral não cobre a camada de transporte; não verificado. Licença: as páginas de EULA e FAQ da Epic retornaram 403 nesta sessão; o modelo de royalties não foi verificado em fonte primária.

## Orquestradores de servidores dedicados

### Agones

O que é: "open source platform, for deploying, hosting, scaling, and orchestrating dedicated game servers" sobre Kubernetes, com recursos `GameServer` e `Fleet`, estratégias de alocação e SDK de ciclo de vida (health check, estado, configuração) [F: agones2026overview]. Um `GameServer` cria um Pod; o exemplo usa `portPolicy: Dynamic` e protocolo UDP; o sidecar do SDK recebe `SDK.Ready()` e move o estado para `Ready` [F: agones2026create-gameserver]. Categoria: orquestrador [I]. Autoridade: agnóstico; hospeda qualquer processo de servidor dedicado (ver `rtm.arch.authoritative-server`) [I]. Transporte: o do servidor hospedado; portas UDP/TCP expostas pelo Kubernetes [F: agones2026create-gameserver]. Licença: Apache-2.0; repositório criado em 2017-12-07, 7.090 estrelas, push em 2026-10-27; release v1.61.0 em 2026-09-24 [F: agones2026github-api; agones2026github-api-release].

### Hathora (encerrado) e GameFabric (Nitrado)

O que é: Hathora era um serviço gerenciado de hospedagem de servidores de jogo; em 2026 `hathora.dev` redireciona para `gamefabric.com` [F: gamefabric2026site]. Segundo a imprensa, a Hathora foi comprada pela Fireworks AI, o suporte a jogos terminou em 2026-05-05 e a migração dos clientes foi oferecida para o GameFabric da Nitrado [F: gizmodo2026hathora] (fonte secundária; comunicado oficial da Hathora não aberto nesta sessão). GameFabric se apresenta como camada única de orquestração em bare metal, nuvem ou híbrido, "running on Agones and Kubernetes under the hood", com alocador de sessões, proteção DDoS e API REST/gRPC; tráfego de jogo UDP; a página cita 22 regiões bare metal e "mais de 75 regiões" com nuvem, números inconsistentes entre seções (marketing) [F: gamefabric2026site]. Categoria: orquestrador gerenciado [I]. Modelo comercial: bare metal, híbrido e cloud/BYOC com cobrança por segundo; preços em página separada, não verificada [F: gamefabric2026site].

### Edgegap

O que é: hospedagem e orquestração de servidores de jogo em containers numa "distributed edge network", com API para apps, versões, deployments e relays, Session Orchestration para matchmakers e server browsers, integrações com Nakama, Unity Gaming Services e PlayFab, e amostras para Mirror, FishNet, Fusion, NGO, Unreal, Godot e Colyseus [F: edgegap2026docs; edgegap2026orchestration]. Deployments podem ser por partida (escala sob demanda) ou standby regional; Private Fleets reservam capacidade 24/7 [F: edgegap2026orchestration]. Categoria: orquestrador gerenciado, com relay como produto separado [I]. Autoridade: servidores dedicados; o produto Distributed Relays é descrito como "no compute, not authoritative servers" [F: edgegap2026pricing]. Transporte: o do servidor hospedado; amostras WebGL usam transports WebSocket [F: edgegap2026docs]. Modelo comercial: free tier (1 app, até 1,5 vCPU, deployments limitados a 60 min); Edge Cloud a US$ 0,00115 por vCPU-minuto e US$ 0,10/GB de egress, "615+ locations"; Private Fleet a US$ 0,0261 por vCPU-hora ou US$ 280 a 350 por host/mês; relays grátis até 50 CCU e de US$ 8 (100 CCU) a US$ 450 (2.000 CCU) por mês; matchmaking de US$ 22 a 395 por mês [F: edgegap2026pricing].

## Pub/sub e mensageria em tempo real

### Socket.IO

O que é: biblioteca JavaScript para comunicação bidirecional baseada em eventos; "NOT a WebSocket implementation" (adiciona metadados a cada pacote, incompatível com clientes WebSocket puros) [F: socketio2026docs]. Transporte: HTTP long-polling, WebSocket ou WebTransport, com seleção automática e fallback; heartbeat; reconexão automática com atraso crescente; buffer de pacotes offline; acknowledgements; broadcasting por rooms; namespaces [F: socketio2026docs]. Escala: múltiplos nós exigem sticky sessions (ou só WebSocket/WebTransport) e um adapter (Redis, Redis Streams, MongoDB, Postgres, cluster, Google Pub/Sub, SQS, Service Bus) para broadcast entre processos [F: socketio2026docs-multiple-nodes]. Categoria: biblioteca de pub/sub e transporte, não é framework de jogo [I]. Autoridade: nenhuma; o desenvolvedor implementa o modelo [I]. Licença: MIT; repositório de 2010-03-11, 63.228 estrelas, push em 2026-09-29; release socket.io@4.8.4 em 2026-09-25 [F: socketio2026github-api; socketio2026github-api-release].

### Supabase Realtime

O que é: serviço distribuído com três recursos: Broadcast (mensagens entre clientes), Presence (estado compartilhado de usuários online) e Postgres Changes (escuta de mudanças no banco) [F: supabase2026realtime]. Transporte: WebSocket (`wss://.../realtime/v1/websocket`), canais no estilo Phoenix (`phx_join`), heartbeat obrigatório a cada 25 s; protocolo 2.0.0 com frames JSON em array e broadcast binário opcional [F: supabase2026realtime-protocol]. Limites por plano: Free 200 conexões simultâneas, 100 mensagens/s, 100 joins/s, payload 256 KB; Pro 500 conexões e 500 msg/s (10.000 conexões e 2.500 msg/s sem spend cap); Team 10.000 e 2.500; 10 chaves de presença por objeto [F: supabase2026realtime-limits]. Categoria: pub/sub gerenciado com código aberto (servidor em Elixir, Apache-2.0, criado em 2019-09-23, 7.671 estrelas, push em 2026-10-29) [F: supabase2026realtime-github-api] [I]. Autoridade: nenhuma embutida; Broadcast é relay e Postgres é a fonte de verdade quando usado [I].

### Ably

O que é: plataforma pub/sub como serviço com produtos Pub/Sub, Chat, Spaces (estado de participantes: cursores, locks, avatares), LiveObjects (estado compartilhado com resolução de conflitos), LiveSync (mudanças de banco) e AI Transport [F: ably2026platform]. Transporte: "typically WebSockets" com todos os canais multiplexados numa conexão; heartbeat de 15 s, cliente passa a `disconnected` após 25 s sem atividade; estado de conexão preservado por 2 minutos após unload para retomar sem perda [F: ably2026connect]. Garantias: a página de plataforma fala em "integrity" contra mensagens perdidas, duplicadas ou fora de ordem, sem detalhar; afirmações como "15+ datacenters", "700+ edge locations" e "no single point of failure" são marketing [F: ably2026platform] [I]. Modelo comercial: Free com 6 milhões de mensagens/mês, 200 conexões e 200 canais simultâneos, 500 msg/s; Standard US$ 29/mês, Pro US$ 399/mês mais uso (US$ 2,50 por milhão de mensagens, US$ 1 por milhão de minutos de conexão, com descontos por volume); SLA de 99,999% só no Enterprise [F: ably2026pricing]. Categoria: pub/sub gerenciado [I]. Autoridade: nenhuma; LiveObjects oferece convergência de estado (não verificado em detalhe) [I].

### PubNub

O que é: plataforma hospedada de mensagens em tempo real com pub/sub por canais (criados no primeiro uso, nome até 92 caracteres, wildcard por ponto), Presence (join/leave/timeout em canal `-pnpres`, ocupação, estado), Message Persistence com retenção configurável, Signals (até 64 bytes, não persistidos), App Context e Access Manager com tokens assinados [F: pubnub2026docs; pubnub2026core-concepts]. Ordenação: timetoken de 17 dígitos (100 ns) atribuído pelo servidor; mensagens de regiões diferentes podem chegar fora de ordem [F: pubnub2026core-concepts]. Limites: payload padrão 32 KiB (até 2 MB processáveis), 50.000 memberships por usuário, 5.000 membros por canal [F: pubnub2026core-concepts]. Transporte: SDKs e REST sobre TLS; protocolo não nomeado nas páginas consultadas [F: pubnub2026docs]. Afirmações de latência (0,5 ms de processamento na mesma região) e SLA de 99,999% são do fornecedor; a página registra que o caminho de subscribe é "at-most-once" numa conexão estável [F: pubnub2026docs]. Categoria: pub/sub gerenciado, proprietário; preços não verificados [I].

## Colaboração em tempo real

### Liveblocks

O que é: "realtime infrastructure for handling concurrent edits on shared data" para pessoas e agentes; produtos Sync (estado colaborativo), Comments e Notifications; SDKs React, JavaScript, Redux, Zustand, Yjs, ProseMirror, Lexical, CodeMirror, Node.js, Python e REST [F: liveblocks2026docs]. Uma *room* é "a stateful WebSocket server on the edge" que hospeda Presence, estado compartilhado e comentários; hospedagem apenas gerenciada, em regiões Earth (Cloudflare edge mais AWS us-east-1), US e EU (Enterprise) [F: liveblocks2026how-it-works]. Categoria: infraestrutura de colaboração gerenciada [I]. Autoridade: estado convergente de Storage e integração Yjs (`@liveblocks/yjs`); o mecanismo de resolução de conflitos não está descrito nas páginas consultadas [F: liveblocks2026how-it-works]. Transporte: WebSocket [F: liveblocks2026how-it-works]. Licença: dual, Apache-2.0 na maior parte do código e AGPL-3.0-or-later em `@liveblocks/server` e na CLI [F: liveblocks2026license]. Preços: Free com 500 salas ativas/mês e 10 conexões por sala; Pro US$ 30/mês; Team a partir de US$ 600/mês; créditos mensais mais uso [F: liveblocks2026pricing].

### PartyKit

O que é: plataforma para apps multiplayer em que cada *Party* é uma instância única por sala, apoiada por um Cloudflare Durable Object com estado em memória isolado; o mesmo `id` roteia sempre à mesma instância; handlers `onRequest`, `onConnect`, `onMessage`; clientes via HTTP ou WebSocket (biblioteca PartySocket); Y-PartyKit para Yjs [F: partykit2026how-it-works]. Categoria: colaboração / servidores stateful de borda [I]. Autoridade: servidor por sala (o Party é a autoridade) [I]. Transporte: WebSocket e HTTP [F: partykit2026how-it-works]. Licença: MIT; repositório criado em 2022-12-10, 5.742 estrelas, push em 2026-10-09 [F: partykit2026github-api]. Estado: a plataforma hospedada está sendo desligada, com deploys encerrados em 16 de outubro e desligamento em 2026-10-23; a documentação aponta migração para PartyServer e deploy na própria conta Cloudflare [F: partykit2026docs; partykit2026how-it-works].

### Yjs e Hocuspocus

O que é: Yjs é uma biblioteca CRDT de alto desempenho para apps colaborativos, com tipos compartilhados semelhantes a Map e Array; "the order in which document updates are applied doesn't matter"; agnóstica de rede, com adaptadores WebRTC, WebSocket e Hyper, bindings para ProseMirror, Tiptap, Monaco, Quill, CodeMirror e Remirror [F: yjs2026docs]. O protocolo de *awareness* compartilha presença transitória (nome, cor, cursor) como CRDT baseado em estado, não persistido, com remoção automática ao sair [F: yjs2026awareness]. `y-websocket` é um provider cliente-servidor com servidor de referência (`npx y-websocket`, porta 1234), persistência opcional em LevelDB e sem escala horizontal embutida (sugere pub/sub ou sharding; aponta y-redis) [F: yjs2026y-websocket]. Licença MIT (Kevin Jahns e RWTH Aachen); repositório de 2014-07-29, 22.992 estrelas, push em 2026-10-23 [F: yjs2026license; yjs2026github-api]. Hocuspocus é o backend WebSocket para Yjs em TypeScript, executável em Node.js, Bun, Deno e Cloudflare Workers (desde v4), com webhooks e afirmação de que "scales to millions of users with Redis" (marketing); documentado no site da Tiptap [F: hocuspocus2026docs]. Licença MIT; repositório de 2020-11-13, 2.639 estrelas, push em 2026-10-28 [F: hocuspocus2026github-api]. Categoria: colaboração (ver `rtm.sync.crdt`). Autoridade: nenhuma central; convergência por CRDT [F: yjs2026docs] [I].

## Relações com outros conceitos

As entradas de netcode de engine implementam `rtm.arch.authoritative-server` (servidor ou host) e, em Fusion Shared e NGO distributed authority, variantes de autoridade distribuída próximas de `rtm.arch.peer-to-peer`; Quantum implementa `rtm.arch.deterministic-lockstep`. Photon Realtime, Unity Relay e Edgegap Relay implementam `rtm.arch.relay-server`. Os orquestradores são infraestrutura para `rtm.arch.authoritative-server`. Os serviços pub/sub cobrem `rtm.proto.websocket` e, em Socket.IO, `rtm.proto.webtransport`, com presença (`rtm.mp.presence`) e reconexão (`rtm.rel.reconnection`) como recursos de cliente. Yjs, Liveblocks e Hocuspocus implementam `rtm.sync.crdt`.

## Lacunas e questões abertas

- Unreal Engine: EULA e FAQ (unrealengine.com) retornaram 403; modelo de royalties não verificado em fonte primária.
- FishNet: páginas de transports (Tugboat, Bayou) retornaram 404; protocolos não verificados.
- Unity Relay: página de conexão retornou 404; transporte (UDP/DTLS/WSS) não verificado.
- Hathora: comunicado oficial de aquisição não aberto; apenas imprensa (Gizmodo).
- Photon: nenhuma página aberta declara explicitamente que os SDKs são de código fechado; apenas se verificou o modelo de preços por CCU e a exigência de licença do Photon Server.
- PubNub e GameFabric: páginas de preços não abertas.
- Ably: fallbacks de transporte (XHR, SSE) e detalhes de LiveObjects não verificados.
- Liveblocks: mecanismo de resolução de conflitos do Storage não descrito na página consultada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| photon2026fusion-intro, photon2026fusion-topologies, photon2026realtime-intro, photon2026quantum-intro, photon2026server-intro | fornecedor | 2026-10-29 |
| photon2026fusion-pricing, photon2026realtime-pricing, photon2026quantum-pricing | fornecedor (preços) | 2026-10-29 |
| unity2026ngo-manual, unity2026ngo-authority, unity2026ngo-distributed, unity2026transport, unity2026mps-sdk | fornecedor | 2026-10-29 |
| unity2026ngo-license, unity2026ngo-github-api | tecnico | 2026-10-29 |
| unity2026ugs-pricing | fornecedor (preços) | 2026-10-29 |
| unity2026multiplay-eos | fornecedor (anúncio) | 2026-10-29 |
| rocketscience2026hosting, gamefabric2026site | fornecedor (marketing) | 2026-10-29 |
| mirror2026readme, mirror2026docs-transports, fishnet2026docs, fishnet2026docs-models | fornecedor | 2026-10-29 |
| mirror2026github-api, fishnet2026github-api, fishnet2026license | tecnico | 2026-10-29 |
| unreal2026networking | fornecedor | 2026-10-29 |
| agones2026overview, agones2026create-gameserver | fornecedor | 2026-10-29 |
| agones2026github-api, agones2026github-api-release | tecnico | 2026-10-29 |
| gizmodo2026hathora | secundario | 2026-10-29 |
| edgegap2026docs, edgegap2026orchestration, edgegap2026pricing | fornecedor | 2026-10-29 |
| socketio2026docs, socketio2026docs-multiple-nodes | fornecedor | 2026-10-29 |
| socketio2026github-api, socketio2026github-api-release | tecnico | 2026-10-29 |
| supabase2026realtime, supabase2026realtime-limits, supabase2026realtime-protocol | fornecedor | 2026-10-29 |
| supabase2026realtime-github-api | tecnico | 2026-10-29 |
| ably2026platform, ably2026connect, ably2026pricing | fornecedor | 2026-10-29 |
| pubnub2026docs, pubnub2026core-concepts | fornecedor | 2026-10-29 |
| liveblocks2026docs, liveblocks2026how-it-works, liveblocks2026pricing | fornecedor | 2026-10-29 |
| liveblocks2026license | tecnico | 2026-10-29 |
| partykit2026docs, partykit2026how-it-works | fornecedor | 2026-10-29 |
| partykit2026github-api | tecnico | 2026-10-29 |
| yjs2026docs, yjs2026awareness, yjs2026y-websocket, hocuspocus2026docs | fornecedor | 2026-10-29 |
| yjs2026license, yjs2026github-api, hocuspocus2026github-api | tecnico | 2026-10-29 |
