---
id: rtm.fw.colyseus
titulo: Colyseus
tipo: framework
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
versao_consultada: "colyseus 0.18.10 (2026-10-22); @colyseus/sdk 0.18.8 (2026-10-26); schema 5"
fontes: [colyseus2026github, colyseus2026github-api, colyseus2026github-api-releases, colyseus2026license, colyseus2026docs-intro, colyseus2026docs-server-start, colyseus2026docs-room, colyseus2026docs-lifecycle, colyseus2026docs-reconnection, colyseus2026docs-relay, colyseus2026docs-state, colyseus2026docs-schema, colyseus2026docs-view, colyseus2026docs-matchmaker, colyseus2026docs-queue, colyseus2026docs-visibility, colyseus2026docs-presence, colyseus2026docs-driver, colyseus2026docs-transport, colyseus2026docs-ws, colyseus2026docs-scalability, colyseus2026docs-auth, colyseus2026docs-cloud, colyseus2026docs-cloud-pricing, colyseus2026docs-faq, colyseus2026docs-netcode, colyseus2026docs-loadtest, colyseus2026docs-sdk-connection]
relacoes:
  - { tipo: depende-de, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.proto.webtransport }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.arch.relay-server }
  - { tipo: relacionado-a, alvo: rtm.sync.state-replication }
  - { tipo: relacionado-a, alvo: rtm.sync.delta-compression }
  - { tipo: relacionado-a, alvo: rtm.sync.interest-management }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.mp.rooms-and-matches }
  - { tipo: relacionado-a, alvo: rtm.mp.matchmaking }
  - { tipo: relacionado-a, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.sec.authentication }
  - { tipo: alternativa-a, alvo: rtm.fw.nakama }
  - { tipo: relacionado-a, alvo: rtm.fw.comparison }
termos: [room, schema, patch rate, seat reservation, state view, presence (Colyseus), driver (Colyseus), reconnection token, allowReconnection]
---

# Colyseus

## Definição e terminologia

Colyseus é um framework de servidor multiplayer para Node.js, descrito no repositório como "Authoritative Multiplayer Framework for Node.js", construído em Node.js e TypeScript [F: colyseus2026github]. A linguagem principal registrada pelo GitHub é TypeScript, a licença é MIT (copyright 2015-2026 Endel Dreyer), o repositório foi criado em 2015-11-22 e tinha 7.490 estrelas e último push em 2026-10-26 na data de consulta [F: colyseus2026github-api; colyseus2026license].

A linha de versão atual é 0.18: `colyseus@0.18.10` foi publicada em 2026-10-22 e `@colyseus/sdk@0.18.8` em 2026-10-26 [F: colyseus2026github-api-releases]. O projeto é um monorepo cujo pacote principal `colyseus` é acompanhado por transports (`@colyseus/ws-transport`, `@colyseus/uwebsockets-transport`), presence e driver Redis, proxy Traefik, ferramentas, monitor e playground, todos versionados em 0.18.x [F: colyseus2026github-api-releases]. O sistema de estado é "schema 5" [F: colyseus2026docs-schema].

A documentação apresenta o framework como servidor autoritativo com sincronização de estado em tempo real, matchmaking e integração com engines e frontends; inclui módulos de autenticação, banco de dados, painel administrativo e ferramentas de desenvolvimento [F: colyseus2026docs-intro]. Não é um serviço de backend completo (não há leaderboards, chat ou grafo social embutidos) e não é um motor de jogo [I]. A *Room* é a unidade central e corresponde ao conceito de sala em `rtm.mp.rooms-and-matches` [I].

## Problema que resolve

O framework resolve o problema de manter um estado compartilhado autoritativo por sala e distribuí-lo aos clientes com patches binários incrementais, sem que o desenvolvedor escreva a serialização [F: colyseus2026docs-state]. Também cobre matchmaking por sala, reconexão com reserva de assento e escala horizontal por processo [F: colyseus2026docs-matchmaker; colyseus2026docs-reconnection; colyseus2026docs-scalability].

## Fundamentos e funcionamento

### Requisitos e inicialização

Exige Node.js LTS (ou Bun como alternativa); um projeto é criado com `npm create colyseus-app@latest` e escuta por padrão na porta 2567, onde também serve o Playground para testar salas sem cliente [F: colyseus2026docs-server-start].

### Room

Cada instância de `Room` guarda um grupo de clientes que compartilham estado e mensagens; o desenvolvedor estende a classe [F: colyseus2026docs-room]. Propriedades e padrões [F: colyseus2026docs-room]:

| Propriedade | Padrão | Função |
|---|---|---|
| `maxClients` | `Infinity` | lotação; a sala trava sozinha ao encher |
| `patchRate` | 50 ms (20 patches/s) | intervalo de envio de patches; `null` desliga o envio automático |
| `autoDispose` | `true` | descarta a sala quando o último cliente sai |
| `seatReservationTimeout` | 15 s | tempo para um cliente com assento reservado completar o join |
| `maxMessagesPerSecond` | `Infinity` | limite por cliente; exceder desconecta |
| `roomId` | string aleatória de 9 caracteres | pode ser customizado em `onCreate` |

Ciclo de vida, na ordem documentada "created → authenticated → joined → dropped → reconnected → left → disposed": `onCreate(options)`, `onAuth(client, options, context)` (token, headers, IP), `onJoin`, `onDrop(client, code)` (desconexão inesperada, lugar recomendado para `allowReconnection`), `onReconnect`, `onLeave(client, code)`, `onDispose`, mais `onBeforePatch`, `onUncaughtException` e `onBeforeShutdown` [F: colyseus2026docs-lifecycle]. O loop de simulação usa `setTimestep(callback, delay)` (padrão 16,6 ms) ou `setFixedTimestep` para jogos com predição; `setSimulationInterval` é o nome antigo [F: colyseus2026docs-room]. Códigos de fechamento 4000–4010 são reservados; aplicações usam 4011–4999 [F: colyseus2026docs-room].

Visibilidade: `locked` (bloqueia joins; automático ao lotar), `private` (só por `joinById`), `unlisted` (fora de listagens, mas casável por `joinOrCreate`); não há senha nativa, a receita combina `filterBy`, `unlisted` e `onAuth` [F: colyseus2026docs-visibility].

Há uma `RelayRoom` embutida que apenas repassa mensagens entre clientes, sem validação, com `players` como estado mínimo e `allowReconnectionTime` limitado a 40 s; a documentação a recomenda para protótipos e sugere escrever uma sala própria com validação quando necessário [F: colyseus2026docs-relay]. É o equivalente ao modo relay de `rtm.arch.relay-server` [I].

### Schema e sincronização de estado

O estado é definido no servidor com `schema()` (builder) ou decoradores `@type()`; só campos declarados sincronizam; apenas o servidor muta o estado e clientes pedem mudanças por mensagens [F: colyseus2026docs-schema; colyseus2026docs-state]. Um cliente novo recebe os tipos e o estado completo; depois, a cada `patchRate`, o servidor codifica só as propriedades alteradas, identificando instâncias por `refId`; o cliente aplica os patches e dispara `onAdd`, `onRemove`, `onChange` e `listen` [F: colyseus2026docs-state]. "Only the latest mutation of each property is queued" entre patches [F: colyseus2026docs-state].

Tipos: `string`, `boolean`, `number` (auto-dimensionado), inteiros com e sem sinal de 8 a 64 bits, `float32`, `float64`, `bigint64`/`biguint64`, `t.quantized()` e `t.angle()` para floats compactos; coleções `ArraySchema`, `MapSchema` (chaves string), `SetSchema` e `CollectionSchema` (só SDK JavaScript) [F: colyseus2026docs-schema]. Limites: até 63 propriedades sincronizáveis por Schema (herdadas e `.deprecated()` contam); arrays multidimensionais não são suportados; servidor e cliente precisam da mesma definição na mesma ordem; novos campos vão ao fim e campos antigos são marcados `.deprecated()`, o que importa para clientes C#, C++ e Haxe [F: colyseus2026docs-schema; colyseus2026docs-state]. Modificadores: `.view()` (visível só a quem tem StateView), `.unreliable()` (experimental, só com WebTransport), `.patchOnly()`, `.fullStateOnly()` [F: colyseus2026docs-schema].

*StateView* (introduzido em 0.16) faz filtragem por cliente (interest management): `client.view = new StateView()`, `view.add(instancia, tag)`, `view.subscribe(colecao)`; a documentação avisa que não é otimizado para grandes volumes e que cada view adiciona um passo de codificação [F: colyseus2026docs-view]. Relaciona-se a `rtm.sync.interest-management` [I].

### Matchmaking

Toda chamada de join do SDK "goes through the matchmaker" e devolve uma *seat reservation* (`name`, `sessionId`, `roomId`, `processId`) [F: colyseus2026docs-matchmaker]. Métodos: `joinOrCreate`, `join`, `joinById`, `create`, `reconnect`; salas são definidas com `defineServer({ rooms })`/`defineRoom`, com `.filterBy([...])` (opções gravadas na criação da sala filtram joins posteriores), `.sortBy({...})` e `.enableRealtimeListing()` [F: colyseus2026docs-matchmaker]. `matchMaker.controller.exposedMethods` restringe o que clientes podem chamar [F: colyseus2026docs-matchmaker]. Uma `QueueRoom` embutida agrupa jogadores por `rank` ao longo de ciclos (`maxPlayers` padrão 4, `maxWaitingCycles` padrão 15), com `compare`, times por `teamId` e grupos incompletos preenchidos por bots [F: colyseus2026docs-queue].

### Presence e Driver

Dois componentes trocáveis sustentam a escala [F: colyseus2026docs-presence; colyseus2026docs-driver]:

- **Presence**: pub/sub e chave-valor entre processos (`subscribe`, `publish`, `set`, `hset`, `incr`, listas, sets); `LocalPresence` (memória, um processo) ou `RedisPresence` (ioredis, suporta Redis Cluster).
- **Driver**: armazena os dados das salas para o matchmaker; `LocalDriver` (memória), `RedisDriver` (recomendado em produção), `MongooseDriver` ("not actively maintained"), além de opções PostgreSQL via `@colyseus/database`.

O termo "presence" em Colyseus é infraestrutura interna de coordenação, não presença de usuário como em `rtm.mp.presence`; a presença de usuário é derivada do estado da sala (coleção de players) [I].

### Escala horizontal

Cada sala vive em exatamente um processo e as conexões dos clientes vão ao processo que a criou; Redis é "hard requirement" para múltiplos processos [F: colyseus2026docs-scalability]. O join tem dois passos: reservar assento (qualquer processo, coordenado por Redis pub/sub) e conectar por WebSocket diretamente ao processo dono da sala, usando `publicAddress` por instância [F: colyseus2026docs-scalability]. A documentação recomenda PM2 em modo fork (não cluster), um processo por núcleo em portas 2567, 2568..., atrás de NGINX ou Traefik; `@colyseus/traefik` é um pacote do monorepo [F: colyseus2026docs-scalability; colyseus2026github-api-releases].

### Transporte

`WebSocketTransport` é o padrão, sobre a biblioteca `ws`, com `pingInterval` 3.000 ms, `pingMaxRetries` 2, `maxPayload` 4.096 bytes e `verifyClient` [F: colyseus2026docs-ws]. Alternativas: uWebSockets.js, WebTransport e Bun WebSockets; a página de transports não rotula nenhum como experimental, mas o modificador `.unreliable()` do schema é marcado experimental e exige WebTransport [F: colyseus2026docs-transport; colyseus2026docs-schema].

### Reconexão

Dois fluxos, ambos dependentes de o servidor reter o assento com `allowReconnection(client, segundos | "manual")` em `onDrop` [F: colyseus2026docs-reconnection]:

- **Automático** (desde 0.17): o SDK detecta a queda e tenta reconectar com backoff exponencial, mantendo o mesmo objeto `room` e seus listeners; padrões do SDK: `maxRetries` 15, `minDelay` 100 ms, `maxDelay` 5.000 ms, `minUptime` 5.000 ms, `maxEnqueuedMessages` 10; falha final emite código 4003 [F: colyseus2026docs-reconnection; colyseus2026docs-sdk-connection].
- **Manual**: `client.reconnect(reconnectionToken)` após recarregar a página; o token é renovado a cada conexão; retorna nova instância de `Room` [F: colyseus2026docs-reconnection].

`room.leave()` envia código 4000 (consentido), pula `onDrop` e não retém assento; ao reconectar, o servidor envia snapshot completo que o SDK mescla na árvore existente; a documentação sugere janelas de cerca de 30 s para jogos rápidos e 5 min para turnos [F: colyseus2026docs-reconnection].

### Autenticação

`onAuth` na sala valida JWT; `auth.middleware()` protege rotas HTTP; o módulo `@colyseus/auth` oferece email/senha, anônimo, OAuth com "200+ providers", recuperação de senha e sessões JWT com revogação; `@colyseus/database` adiciona loja de usuários e banimento via `tokenVersion` [F: colyseus2026docs-auth].

### Netcode (0.18)

A seção de netcode, nova em 0.18, oferece timestep fixo com um input por passo, predição do cliente com rollback e replay, interpolação de entidades remotas e lag compensation por rewind, com APIs `room.input()`, `Predict`, `defineInput()`, `setFixedTimestep()` e `allowRewindState()`; o desenvolvedor fornece a função de passo determinística [F: colyseus2026docs-netcode]. Relaciona-se a `rtm.pred.client-side-prediction` [I].

### Colyseus Cloud

Hospedagem gerenciada pela equipe do framework: deploy com `npx @colyseus/cloud deploy` ou integração GitHub; usa NGINX e PM2; cobrança mensal antecipada por plano de computação, com crédito proporcional ao excluir instância (exemplo da documentação: instância de US$ 100/mês excluída após 15 dias gera US$ 50 de crédito) [F: colyseus2026docs-cloud; colyseus2026docs-cloud-pricing]. "Up and ready for production in less than 15 minutes" e "premium managed hosting" são afirmações de marketing [F: colyseus2026docs-cloud] [I].

### SDKs de cliente

TypeScript/JavaScript, React, Unity, MonoGame, Godot, Defold, Construct 3, GameMaker, Cocos Creator, Haxe, Flutter, Swift, SDK nativo em C, Discord Activity e WeChat [F: colyseus2026docs-intro].

## Requisitos e pressupostos

- Node.js LTS ou Bun [F: colyseus2026docs-server-start].
- Redis para qualquer implantação com mais de um processo [F: colyseus2026docs-scalability].
- Estado modelado em Schema com as restrições de 63 campos e definição idêntica nos dois lados [F: colyseus2026docs-schema].
- Lógica de jogo em JavaScript/TypeScript, single-threaded por processo [I, decorrente de Node.js].

## Vantagens e limitações

Vantagens documentadas: sincronização automática com patches binários incrementais [F: colyseus2026docs-state]; reconexão nativa com token e retentativa automática [F: colyseus2026docs-reconnection]; licença MIT [F: colyseus2026license]; filtragem por cliente com StateView [F: colyseus2026docs-view]; cadência de releases frequente em 0.18 [F: colyseus2026github-api-releases].

Limitações documentadas:

- Versão ainda em 0.x; migrações entre 0.15, 0.16, 0.17 e 0.18 têm guias próprios, o que indica quebras entre versões [F: colyseus2026docs-intro] [I].
- Sem persistência de jogo, leaderboards ou chat embutidos; o módulo `@colyseus/database` cobre usuários e autenticação [F: colyseus2026docs-auth].
- Capacidade por processo não tem número oficial: a FAQ fala em cerca de 1.000 a 2.000 conexões para jogos simples num servidor de 1 vCPU/1 GB, estima 2 a 5 KB de memória por conexão e manda "always load test your specific use case" [F: colyseus2026docs-faq].
- StateView não é otimizado para grandes volumes [F: colyseus2026docs-view].
- Payload de entrada de 4 KB por padrão no transport `ws` [F: colyseus2026docs-ws].

## Alternativas e comparações

Nakama (`rtm.fw.nakama`) oferece match handler sem sincronização automática, mas com serviços sociais e persistência; Socket.IO e serviços pub/sub gerenciados cobrem só o transporte e a difusão; ver `rtm.fw.alternatives` e `rtm.fw.comparison`.

## Métricas e métodos de avaliação

O fornecedor não publica benchmarks de servidor; o README afirma escala de "10 to 10,000+ CCU with Redis and load balancers" sem metodologia (marketing) [F: colyseus2026github] [I]. A ferramenta `@colyseus/loadtest` simula clientes com script próprio (`--room`, `--numClients`, `--endpoint`); a documentação observa que a 20 patches/s, 500 clientes num processo decodificam 10.000 patches/s e que o gerador de carga pode virar gargalo, recomendando um processo por núcleo e máquina separada [F: colyseus2026docs-loadtest].

## Exemplo técnico independente de domínio

Estrutura de uma Room com estado sincronizado, em pseudocódigo próximo à documentação [F: colyseus2026docs-room; colyseus2026docs-schema; colyseus2026docs-lifecycle] [I: adaptação]:

```
Jogador = schema({ x: t.number(), y: t.number(), conectado: t.boolean() })
Estado  = schema({ jogadores: t.map(Jogador) })

class SalaExemplo extends Room:
    maxClients = 4
    state = new Estado()

    onCreate(options):
        onMessage("mover", (client, msg) ->
            j = state.jogadores.get(client.sessionId)
            validar(msg); j.x += msg.dx; j.y += msg.dy)   # só o servidor muta
        setTimestep(dt -> simular(state, dt))

    onAuth(client, options, ctx): return verificar_jwt(ctx.token)
    onJoin(client, options, auth): state.jogadores.set(client.sessionId, new Jogador())
    onDrop(client, code):
        state.jogadores.get(client.sessionId).conectado = false
        allowReconnection(client, 30)          # retém o assento por 30 s
    onReconnect(client): state.jogadores.get(client.sessionId).conectado = true
    onLeave(client, code): state.jogadores.delete(client.sessionId)
    onDispose(): persistir_resultado()

defineServer({ rooms: { exemplo: defineRoom(SalaExemplo).filterBy(["modo"]) } })
# cliente: room = client.joinOrCreate("exemplo", { modo: "x" }); guardar room.reconnectionToken
```

## Relações com outros conceitos

Colyseus depende de WebSocket (`rtm.proto.websocket`) e oferece WebTransport opcional (`rtm.proto.webtransport`). Implementa servidor autoritativo (`rtm.arch.authoritative-server`) e, via `RelayRoom`, relay (`rtm.arch.relay-server`). Sua sincronização é replicação de estado com patches delta (`rtm.sync.state-replication`, `rtm.sync.delta-compression`) e filtragem por cliente (`rtm.sync.interest-management`); o módulo de netcode cobre predição (`rtm.pred.client-side-prediction`). Cobre salas (`rtm.mp.rooms-and-matches`), matchmaking (`rtm.mp.matchmaking`), reconexão (`rtm.rel.reconnection`) e autenticação (`rtm.sec.authentication`). É alternativa a `rtm.fw.nakama` e comparado em `rtm.fw.comparison`.

## Lacunas e questões abertas

- Nenhum benchmark oficial; a estimativa da FAQ (1.000 a 2.000 conexões por vCPU) é orientação, não medição.
- O formato binário dos patches (bytes por tipo) está em página de otimização não aberta nesta sessão.
- Regiões disponíveis no Colyseus Cloud e planos de computação (página `/cloud/compute-plans`) não foram verificados.
- Estado de maturidade do transport WebTransport e do Bun transport não é rotulado na documentação.
- Ano do primeiro release público: o repositório foi criado em 2015; as tags mais antigas visíveis na API são 0.14.17-alpha; não verifiquei a data da versão 0.1.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| colyseus2026github | fornecedor | 2026-10-29 |
| colyseus2026github-api | tecnico | 2026-10-29 |
| colyseus2026github-api-releases | tecnico | 2026-10-29 |
| colyseus2026license | fornecedor | 2026-10-29 |
| colyseus2026docs-intro | fornecedor | 2026-10-29 |
| colyseus2026docs-server-start | fornecedor | 2026-10-29 |
| colyseus2026docs-room | fornecedor | 2026-10-29 |
| colyseus2026docs-lifecycle | fornecedor | 2026-10-29 |
| colyseus2026docs-reconnection | fornecedor | 2026-10-29 |
| colyseus2026docs-relay | fornecedor | 2026-10-29 |
| colyseus2026docs-state | fornecedor | 2026-10-29 |
| colyseus2026docs-schema | fornecedor | 2026-10-29 |
| colyseus2026docs-view | fornecedor | 2026-10-29 |
| colyseus2026docs-matchmaker | fornecedor | 2026-10-29 |
| colyseus2026docs-queue | fornecedor | 2026-10-29 |
| colyseus2026docs-visibility | fornecedor | 2026-10-29 |
| colyseus2026docs-presence | fornecedor | 2026-10-29 |
| colyseus2026docs-driver | fornecedor | 2026-10-29 |
| colyseus2026docs-transport | fornecedor | 2026-10-29 |
| colyseus2026docs-ws | fornecedor | 2026-10-29 |
| colyseus2026docs-scalability | fornecedor | 2026-10-29 |
| colyseus2026docs-auth | fornecedor | 2026-10-29 |
| colyseus2026docs-cloud | fornecedor (marketing) | 2026-10-29 |
| colyseus2026docs-cloud-pricing | fornecedor | 2026-10-29 |
| colyseus2026docs-faq | fornecedor | 2026-10-29 |
| colyseus2026docs-netcode | fornecedor | 2026-10-29 |
| colyseus2026docs-loadtest | fornecedor | 2026-10-29 |
| colyseus2026docs-sdk-connection | fornecedor | 2026-10-29 |
