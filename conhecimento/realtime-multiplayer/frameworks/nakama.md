---
id: rtm.fw.nakama
titulo: Nakama (Heroic Labs)
tipo: framework
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
versao_consultada: "Nakama server v3.41.0 (2026-09-18), nakama-common v1.48.0"
fontes: [nakama2026github, nakama2026github-api, nakama2026github-api-release, nakama2026release-3410, nakama2026license, nakama2026docs-architecture, nakama2026docs-multiplayer, nakama2026docs-authoritative, nakama2026docs-relayed, nakama2026docs-matchmaker, nakama2026docs-parties, nakama2026docs-status, nakama2026docs-authentication, nakama2026docs-session, nakama2026docs-sockets, nakama2026docs-storage, nakama2026docs-leaderboards, nakama2026docs-chat, nakama2026docs-clients, nakama2026docs-configuration, nakama2026docs-docker, nakama2026docs-runtime, nakama2026docs-go-runtime, nakama2026docs-ts-runtime, nakama2026docs-benchmarks, heroiclabs2026enterprise, heroiclabs2026cloud, heroiclabs2026nakama]
relacoes:
  - { tipo: depende-de, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.arch.relay-server }
  - { tipo: relacionado-a, alvo: rtm.mp.rooms-and-matches }
  - { tipo: relacionado-a, alvo: rtm.mp.matchmaking }
  - { tipo: relacionado-a, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.mp.turn-based }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.sec.authentication }
  - { tipo: alternativa-a, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.fw.comparison }
termos: [match handler, tick rate, relayed multiplayer, authoritative match, matchmaker ticket, op code, match label, party, presence, session token, refresh token]
---

# Nakama (Heroic Labs)

## Definição e terminologia

Nakama é um servidor de backend para jogos, de código aberto, que o repositório oficial descreve como "scalable open-source game backend server: multiplayer, matchmaking, leaderboards, chat, and social features for games" [F: nakama2026github]. É escrito em Go [F: nakama2026github-api], licenciado sob Apache License 2.0 [F: nakama2026license; nakama2026github-api] e mantido pela Heroic Labs. O repositório foi criado em 2017-01-13 e registrava 13.608 estrelas e último push em 2026-10-29 na data de consulta [F: nakama2026github-api].

A versão estável mais recente na data de consulta é a v3.41.0, publicada em 2026-09-18, compilada com Go 1.27.1 e que exige nakama-common v1.48.0 para módulos Go [F: nakama2026github-api-release; nakama2026release-3410]. O ritmo de lançamento observado é de uma versão minor a cada dois a três meses (v3.37.0 em fevereiro, v3.38.0 em março, v3.39.0 em maio, v3.40.0 em julho, v3.41.0 em setembro) [F: nakama2026github-api-release].

Nakama não é um motor de jogo nem uma biblioteca de netcode de engine (não faz replicação automática de objetos). É um servidor "monolítico e stateful" que expõe APIs de tempo real e de requisição a partir de vários subsistemas [F: nakama2026docs-architecture]. O que ele chama de *match* corresponde ao conceito de sala ou partida tratado em `rtm.mp.rooms-and-matches` [I].

## Problema que resolve

O projeto se propõe a fornecer, num único servidor, os serviços de backend que jogos multiplayer costumam precisar: contas e autenticação, armazenamento, grafo social e grupos, chat, multiplayer em tempo real e por turnos, leaderboards, torneios, parties, validação de compras, notificações, matchmaker, console administrativo e métricas [F: nakama2026github]. O servidor é estendido com lógica própria em Lua, TypeScript/JavaScript ou Go nativo [F: nakama2026github; nakama2026docs-runtime].

## Fundamentos e funcionamento

### Arquitetura

A documentação de arquitetura lista os componentes: autorização (JWT assinado), gerenciamento de cluster, console e métricas (Prometheus), banco de dados, interfaces externas (socket e requisição), dados em memória com busca em campos JSON (usados pelo matchmaker), gerenciamento (ciclo de vida de matches, agendamento de leaderboards e torneios, matchmaking, multiplayer autoritativo), roteamento de mensagens, presença (identificada por usuário, sessão e nó) e *streams*, mecanismo central de envio de dados ao vivo [F: nakama2026docs-architecture].

Há duas interfaces externas [F: nakama2026docs-architecture]:

- **Socket**: entrada principal para funcionalidades em tempo real (chat, multiplayer); "runs on WebSockets and rUDP", com payloads binários (Protocol Buffers) ou texto (JSON).
- **Request**: entrada para atividade não tempo real (contas etc.), sobre gRPC e HTTP.

Nas páginas de conceito e nos SDKs de cliente consultados, apenas WebSocket aparece em exemplos (`NakamaWebsocketClient`, `createWebSocket()`); o rUDP é citado só na visão de arquitetura, sem página própria aberta nesta sessão [F: nakama2026docs-sockets; nakama2026docs-architecture] [I: tratar rUDP como transporte declarado, não como opção documentada para os SDKs consultados].

### Banco de dados e instalação

O servidor "requires CockroachDB or another Postgres wire-compatible server as its database" [F: nakama2026github]. A arquitetura chama de canônico o par com CockroachDB [F: nakama2026docs-architecture], mas o guia Docker oficial usa a imagem `postgres:16.8-alpine`, a imagem `registry.heroiclabs.com/heroiclabs/nakama:3.37.0` e expõe as portas 7349, 7350 (API) e 7351 (console) [F: nakama2026docs-docker].

### Runtime do servidor

O código customizado é carregado da pasta `data/modules` (arquivos `.js`, `.so` e `.lua`); quando o mesmo RPC ou match handler é registrado em mais de um runtime, a precedência é Go, depois Lua, depois JavaScript [F: nakama2026docs-runtime]. Restrições relevantes:

- **Go**: compilado como plugin `.so`; precisa da mesma versão de Go do binário do servidor e da versão de nakama-common correspondente (3.41.0 pareia com 1.48.0); goroutines são desencorajadas; sem sandbox, erros fatais não são contidos; build de plugin não é suportado no Windows (usa-se a imagem `nakama-pluginbuilder`) [F: nakama2026docs-go-runtime].
- **TypeScript/JavaScript**: VM goja, "currently supports the JavaScript ES5 spec"; sem módulos Node (`crypto`, `fs`), sem acesso a filesystem, execução single-threaded; variáveis globais não guardam estado porque o código roda em contextos instanciados de um pool de VMs; a documentação recomenda este runtime como padrão [F: nakama2026docs-ts-runtime; nakama2026docs-runtime].

RPCs registrados ficam expostos por REST (`/v2/rpc/<id>`), socket e gRPC [F: nakama2026docs-runtime].

### Modelos de multiplayer

Nakama documenta dois modelos de partida [F: nakama2026docs-multiplayer]:

**Relayed (client-authoritative)**: o servidor encaminha mensagens entre participantes "sem inspecionar tamanho ou conteúdo", não oferece detecção de trapaça nem correção; guarda apenas o id do match e a lista de presenças; o match vive em memória até o último participante sair; não há senha ou controle de acesso (qualquer um com o id entra); um cliente eleito pelos próprios clientes atua como host [F: nakama2026docs-relayed]. Corresponde a `rtm.arch.relay-server` [I].

**Server-authoritative**: o desenvolvedor escreve um *match handler* no runtime; o servidor valida e distribui os dados; a documentação afirma não haver "cenários prontos", a lógica do jogo é do desenvolvedor [F: nakama2026docs-authoritative]. Corresponde a `rtm.arch.authoritative-server` [I]. A página descreve quatro padrões: tempo real assíncrono (tick alto), turnos ativos (tick baixo), turnos passivos (estado persistido, loop encerrado entre turnos) e baseado em sessão (Nakama orquestra instâncias headless de servidores de jogo) [F: nakama2026docs-authoritative].

O match handler tem sete funções obrigatórias, chamadas só pelo servidor: match init, join attempt, join, leave, loop, terminate e signal [F: nakama2026docs-authoritative]. Propriedades documentadas [F: nakama2026docs-authoritative]:

- Estado isolado em memória por match; mudanças não são enviadas automaticamente, é preciso `broadcast` (imediato) ou `broadcastDeferred` (fim do loop).
- *Tick rate*: número de chamadas do loop por segundo; o mínimo é 1 [F: nakama2026docs-multiplayer]; cada loop deve terminar antes do próximo; se atrasos se acumulam, o servidor encerra o match.
- Mensagens de clientes são enfileiradas e entregues em lote a cada tick; payloads devem caber em um MTU de 1.500 bytes; recomendação de no máximo uma mensagem por tick por presença; excesso pode ser descartado (mitigação: `match.input_queue_size`, padrão 128 [F: nakama2026docs-configuration]).
- *Match label*: string ou JSON, máximo 2 KB; só JSON é pesquisável; atualização em lote a cada `match.label_update_interval_ms` (padrão 1.000 ms [F: nakama2026docs-configuration]).
- Matches autoritativos não terminam quando todos saem; só terminam quando uma função de ciclo de vida retorna estado nulo; matches não se comunicam entre si (signal é exceção rara).
- Eventos de *leave* indicam se o jogador saiu ou desconectou; o handler pode reservar o lugar do desconectado.
- Migração de match durante shutdown gracioso é marcada como recurso Enterprise.

### Matchmaker

O matchmaker é um processo em lote: tickets entram num pool e a cada `matchmaker.interval_sec` (padrão 15 s) o servidor tenta formar grupos; `max_intervals` (padrão 2) define quantos intervalos esperar antes de aceitar tamanho abaixo do ideal; `max_tickets` por usuário tem padrão 3 [F: nakama2026docs-matchmaker; nakama2026docs-configuration]. Tickets têm propriedades string/numéricas, consulta com sintaxe própria (`+properties.region:...`), `minCount`/`maxCount`/`countMultiple`; só jogadores com socket aberto podem usar o matchmaker e a desconexão cancela os tickets, sem restauração ao reconectar [F: nakama2026docs-matchmaker]. Ser "matched" não coloca o jogador na partida: o cliente precisa chamar o join com o token (relayed) ou o id (autoritativo, criado por um hook *matchmaker matched*) [F: nakama2026docs-matchmaker]. Em cluster, o processamento do matchmaker roda num único nó ativo com failover [F: nakama2026docs-matchmaker]. Em Go, `RegisterMatchmakerProcessor` permite substituir o agrupamento [F: nakama2026docs-matchmaker].

### Parties, status e presença

*Parties* são grupos temporários com líder, tamanho máximo de 256 usuários, abertos ou fechados, com pedidos de entrada, mensagens com op code e matchmaking em grupo (membros "sempre mantidos juntos") [F: nakama2026docs-parties; nakama2026docs-matchmaker]. A documentação diz que parties não são destinadas à lógica central do jogo [F: nakama2026docs-parties].

*Status* é a presença social: definido por conexão, apagado na desconexão; seguidores recebem eventos de mudança como joins/leaves; *follows* duram só a sessão [F: nakama2026docs-status]. A presença dentro de um match (lista de participantes) é separada e chega como eventos em lote [F: nakama2026docs-relayed].

### Chat, storage e leaderboards

- **Chat**: canais do tipo room (público), group (membros) e direct message (ambos precisam entrar); persistente por padrão, com histórico; membros ocultos; hooks para filtrar conteúdo [F: nakama2026docs-chat].
- **Storage**: coleções e chaves com valor JSON, dono, permissões de leitura/escrita definidas a cada escrita, versão para escrita condicional (`"*"` para criar-se-não-existe), escrita em lote transacional, `StorageWriteRetry` com até 10 tentativas (Go e TypeScript) [F: nakama2026docs-storage].
- **Leaderboards**: ordem fixa na criação, operadores `set`/`best`/`incr`/`decr`, modo autoritativo (só o servidor envia scores), reset por expressão cron, registros expirados ficam listáveis; ranks só para leaderboards em cache de rank [F: nakama2026docs-leaderboards].

### Autenticação e sessão

Métodos: device ID (10 a 128 bytes alfanuméricos com hífens), email/senha (mínimo 8 caracteres), consoles (Xbox, PlayStation, Nintendo, mediante verificação), Apple, Game Center, Facebook, Facebook Instant e custom (validação própria num before hook, por exemplo Discord); link/unlink de identificadores (409 se já pertence a outra conta; 403 ao remover o último) [F: nakama2026docs-authentication]. A v3.41.0 acrescentou autenticação "provider-agnostic" com APIs `Authenticate`/`Link`/`Unlink` e hooks [F: nakama2026release-3410]. A sessão é um JWT com expiração padrão de 60 s (`session.token_expiry_sec`) e refresh token de 3.600 s; a documentação sugere token de 2 a 3 vezes a sessão média de jogo e refresh de 24 h a 30 dias; SDKs .NET/Unity, JavaScript, Java, Godot e Swift renovam automaticamente, Dart, Unreal, C++ e Defold exigem renovação manual [F: nakama2026docs-session; nakama2026docs-configuration].

### Socket, limites e reconexão

Mensagens de tempo real têm limite `socket.max_message_size_bytes` de 4 KB por padrão; acima disso o servidor fecha a conexão; RPC por HTTP aceita 256 KB (`socket.max_request_size_bytes`) [F: nakama2026docs-sockets]. Outros padrões: `ping_period_ms` 15.000, `pong_wait_ms` 25.000, `outgoing_queue_size` 16; cliente que não responde heartbeats é desconectado [F: nakama2026docs-configuration; nakama2026docs-sockets]. Se o buffer de envio de um cliente lento enche, o servidor pode desconectá-lo [F: nakama2026docs-authoritative].

Sobre reconexão a um match, as páginas consultadas documentam apenas: (a) o evento de leave distingue saída de desconexão e o handler autoritativo pode reservar o lugar; (b) tickets do matchmaker não sobrevivem à desconexão [F: nakama2026docs-authoritative; nakama2026docs-matchmaker]. Não encontrei, nas páginas abertas, um mecanismo nativo de reconexão à partida (token de reconexão); o rejoin parece ser responsabilidade do cliente e do match handler [I] (ver Lacunas).

### SDKs de cliente

Unity/.NET, Unreal, C++, Dart/Flutter, Godot 3 e 4, JavaScript, Swift, Java/Android, Defold, Cocos2d-x C++ e Cocos2d JavaScript; SDKs de console (PlayStation 4/5, Xbox, Switch) sob pedido e não abertos [F: nakama2026docs-clients].

## Requisitos e pressupostos

- Banco PostgreSQL wire-compatible (PostgreSQL ou CockroachDB) [F: nakama2026github].
- Runtime customizado em Go exige versão de Go idêntica à do binário e nakama-common pareado [F: nakama2026docs-go-runtime].
- Em multiplayer autoritativo, toda a lógica de jogo e o broadcast de estado são do desenvolvedor; não há sincronização automática de estado [F: nakama2026docs-authoritative].
- Clustering (vários nós compartilhando presença e roteamento) é funcionalidade do Nakama Enterprise, não do código aberto [F: nakama2026docs-architecture; nakama2026docs-authoritative].

## Vantagens e limitações

Vantagens documentadas [I, com base nas fontes acima]: amplitude de serviços num único servidor; três linguagens de extensão; dois modelos de autoridade no mesmo servidor; licença permissiva; cadência de lançamentos regular.

Limitações documentadas:

- Sem replicação automática de estado; o desenvolvedor serializa e difunde tudo [F: nakama2026docs-authoritative].
- JavaScript limitado a ES5 e sem ecossistema Node [F: nakama2026docs-ts-runtime].
- Escala horizontal com estado compartilhado entre nós depende do Enterprise; a edição aberta é um nó [F: nakama2026docs-architecture]. O site comercial afirma "commercial licenses are also available" sem publicar preços [F: heroiclabs2026nakama].
- Mensagem de socket de 4 KB por padrão e payload recomendado dentro de 1.500 bytes [F: nakama2026docs-sockets; nakama2026docs-authoritative].
- Relayed: sem validação, sem senha, sem persistência [F: nakama2026docs-relayed].

## Alternativas e comparações

Colyseus (`rtm.fw.colyseus`) cobre o mesmo nicho de servidor de salas com autoridade, mas com sincronização automática de estado e sem a camada de serviços sociais e de persistência. Alternativas por categoria estão em `rtm.fw.alternatives`; a tabela comparativa está em `rtm.fw.comparison`.

## Métricas e métodos de avaliação

Benchmarks publicados pelo fornecedor (Heroic Labs), sem data nem versão declaradas na página, com Tsung como gerador de carga, banco CloudSQL de 8 vCPU/30 GB, matches a 10 ticks/s com até 10 jogadores [F: nakama2026docs-benchmarks]:

| Configuração | CCU máximo conectado | Tempo médio de conexão |
|---|---|---|
| 1 nó OSS, 1 CPU / 3 GB | 20.277 | 21,14 ms |
| 2 nós Enterprise, 1 CPU / 3 GB cada | 29.550 | 23,29 ms |
| 2 nós Enterprise, 2 CPU / 6 GB cada | 35.723 | 23,91 ms |

Para a carga de match autoritativo, a taxa média de requisições foi 39,20 req/s (1 nó), 57,92 (2×1 CPU) e 103,18 (2×2 CPU), com latência média de 15,84 ms, 79,85 ms e 42,60 ms respectivamente [F: nakama2026docs-benchmarks]. A página não publica matches por nó, mensagens por segundo nem percentis de latência [F: nakama2026docs-benchmarks]. Afirmações do site comercial como "performance tests up to 2 million CCU" e "thousands of multiplayer matches on a single Nakama server" não trazem metodologia e devem ser lidas como marketing [F: heroiclabs2026nakama] [I].

## Exemplo técnico independente de domínio

Estrutura de um match handler autoritativo, em pseudocódigo próximo ao exemplo de lobby da documentação [F: nakama2026docs-authoritative] [I: adaptação]:

```
registrar_match("lobby", handler)

handler.init(ctx, params):
    estado = { presencas: {}, ticks_vazios: 0 }
    return estado, tick_rate = 1, label = "{}"

handler.join_attempt(ctx, estado, presenca, metadata):
    return estado, aceitar = true          # aqui entram regras de lotação e senha

handler.join(ctx, estado, presencas):
    para p em presencas: estado.presencas[p.session_id] = p
    return estado

handler.leave(ctx, estado, presencas):
    para p em presencas: remover estado.presencas[p.session_id]
    return estado

handler.loop(ctx, estado, mensagens):
    para m em mensagens:                    # entregues em lote por tick
        aplicar(m.op_code, m.dados, estado)
    dispatcher.broadcast(OP_ESTADO, serializar(estado))
    se vazio(estado.presencas): estado.ticks_vazios += 1
    se estado.ticks_vazios > 100: return nulo   # encerra o match
    return estado

handler.terminate(ctx, estado, segundos_graca): return estado
handler.signal(ctx, estado, dados): return estado, resposta
```

## Relações com outros conceitos

Nakama depende de WebSocket como transporte principal do socket (`rtm.proto.websocket`) e declara rUDP (`rtm.proto.udp`). Implementa os dois modelos de autoridade (`rtm.arch.authoritative-server`, `rtm.arch.relay-server`), o conceito de match/sala (`rtm.mp.rooms-and-matches`), matchmaking em lote (`rtm.mp.matchmaking`), presença em match e status social (`rtm.mp.presence`), padrões de turno ativo e passivo (`rtm.mp.turn-based`), autenticação por dispositivo, email e provedores (`rtm.sec.authentication`) e expõe primitivas para reconexão (`rtm.rel.reconnection`). É alternativa a `rtm.fw.colyseus` e é comparado em `rtm.fw.comparison`.

## Lacunas e questões abertas

- Reconexão a match: não localizei página dedicada; a documentação consultada só expõe o evento de leave com flag de desconexão e a reserva de lugar pelo handler. Verificar se há token de rejoin nos SDKs.
- rUDP: declarado na arquitetura, mas nenhuma página consultada mostra como habilitá-lo nos SDKs; não verificado em detalhe.
- Limites numéricos de storage, chat e tamanho de status não aparecem nas partes lidas das páginas (páginas truncadas a 100 mil caracteres).
- Página de Enterprise (`/enterprise/`) descreve clustering com CRDT e gossip em termos de marketing; não há documentação técnica pública aberta nesta sessão sobre topologia de cluster, nem preços.
- Data e versão dos benchmarks não são declaradas pelo fornecedor; os números podem se referir a versões antigas.
- Página de limites de multiplayer (`/concepts/multiplayer/limits/`) retornou 404.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nakama2026github | fornecedor | 2026-10-29 |
| nakama2026github-api | tecnico | 2026-10-29 |
| nakama2026github-api-release | tecnico | 2026-10-29 |
| nakama2026release-3410 | fornecedor | 2026-10-29 |
| nakama2026license | fornecedor | 2026-10-29 |
| nakama2026docs-architecture | fornecedor | 2026-10-29 |
| nakama2026docs-multiplayer | fornecedor | 2026-10-29 |
| nakama2026docs-authoritative | fornecedor | 2026-10-29 |
| nakama2026docs-relayed | fornecedor | 2026-10-29 |
| nakama2026docs-matchmaker | fornecedor | 2026-10-29 |
| nakama2026docs-parties | fornecedor | 2026-10-29 |
| nakama2026docs-status | fornecedor | 2026-10-29 |
| nakama2026docs-authentication | fornecedor | 2026-10-29 |
| nakama2026docs-session | fornecedor | 2026-10-29 |
| nakama2026docs-sockets | fornecedor | 2026-10-29 |
| nakama2026docs-storage | fornecedor | 2026-10-29 |
| nakama2026docs-leaderboards | fornecedor | 2026-10-29 |
| nakama2026docs-chat | fornecedor | 2026-10-29 |
| nakama2026docs-clients | fornecedor | 2026-10-29 |
| nakama2026docs-configuration | fornecedor | 2026-10-29 |
| nakama2026docs-docker | fornecedor | 2026-10-29 |
| nakama2026docs-runtime | fornecedor | 2026-10-29 |
| nakama2026docs-go-runtime | fornecedor | 2026-10-29 |
| nakama2026docs-ts-runtime | fornecedor | 2026-10-29 |
| nakama2026docs-benchmarks | fornecedor | 2026-10-29 |
| heroiclabs2026enterprise | fornecedor (marketing) | 2026-10-29 |
| heroiclabs2026cloud | fornecedor (marketing) | 2026-10-29 |
| heroiclabs2026nakama | fornecedor (marketing) | 2026-10-29 |
