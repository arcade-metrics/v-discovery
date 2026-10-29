---
id: rtm.arch.event-driven
titulo: Arquitetura orientada a eventos para tempo real
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [fowler2005eventsourcing, fowler2017eventdriven, microsoft2026eventsourcing, microsoft2026pubsub, microsoft2025cqrs, kleppmann2015insideout, lamport1978clocks, shapiro2011crdt, heroiclabs2026multiplayer, heroiclabs2026authoritative, colyseus2026room, gambetta2014clientserver]
relacoes:
  - { tipo: alternativa-a, alvo: rtm.arch.authoritative-server }
  - { tipo: alternativa-a, alvo: rtm.arch.relay-server }
  - { tipo: alternativa-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: alternativa-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: depende-de, alvo: rtm.net.logical-clocks }
  - { tipo: depende-de, alvo: rtm.rel.delivery-semantics }
  - { tipo: complementa, alvo: rtm.sync.crdt }
  - { tipo: complementa, alvo: rtm.sync.operational-transformation }
  - { tipo: complementa, alvo: rtm.rt.communication-patterns }
  - { tipo: complementa, alvo: rtm.mp.turn-based }
  - { tipo: complementa, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
termos: [event-driven architecture, event sourcing, event store, publish-subscribe, broker, topic, command, event, CQRS, materialized view, projection, rehydration, snapshot (event sourcing), compensating event, eventual consistency, idempotency, happened-before]
---

# Arquitetura orientada a eventos para tempo real

## Definição e terminologia

Família de arquiteturas em que a comunicação e, frequentemente, o estado são organizados em torno de **eventos**: registros imutáveis de algo que aconteceu. Fowler identifica quatro padrões distintos sob o rótulo "event-driven": *event notification*, *event-carried state transfer*, *event sourcing* e *CQRS* [F: fowler2017eventdriven]. Para tempo real e multiplayer, interessam sobretudo dois mecanismos:

- **Publish-subscribe (pub/sub)**: "Broadcast events asynchronously to multiple interested consumers through an intermediary, without coupling the senders to the receivers" [F: microsoft2026pubsub]. O intermediário é um *broker* ou *event bus*; o fornecedor distingue mensagem e evento: "A *message* is a packet of data. An *event* is a message that notifies other components about a change or an action that occurs" [F: microsoft2026pubsub].
- **Event sourcing**: "Capture all changes to an application state as a sequence of events" [F: fowler2005eventsourcing]; o *event store* append-only "serves as the system of record" e o estado atual é derivado por replay, processo que a documentação da Microsoft chama de *rehydration* [F: microsoft2026eventsourcing].

Vocabulário associado: **command** (intenção de mudança, pode ser rejeitada) versus **event** (fato ocorrido) versus **state** (projeção derivada). No CQRS, "Commands update data. Queries retrieve data", e comandos devem representar tarefas de negócio ("Book hotel room" em vez de "Set ReservationStatus to Reserved") [F: microsoft2025cqrs]. Fowler alerta para o evento que é "a passive-aggressive command", isto é, uma notificação que na verdade exige ação do receptor [F: fowler2017eventdriven].

O que não é: não é uma simulação contínua em ticks com estado autoritativo transmitido (rtm.arch.authoritative-server); não garante ordem total nem latência mínima por construção (ver limitações) [I].

## Problema que resolve

- **Desacoplamento** entre quem produz e quem consome mudanças: adicionar ou remover um consumidor não exige alterar o remetente [F: microsoft2026pubsub].
- **Histórico e auditoria**: "The event log provides a strong audit capability" e permite recriar estados históricos ou explorar cenários alternativos [F: fowler2017eventdriven]; Fowler lista *complete rebuild*, *temporal query* e *event replay* como capacidades [F: fowler2005eventsourcing].
- **Contenção de escrita**: escritas append-only evitam o bloqueio por linha do modelo CRUD [F: microsoft2026eventsourcing].
- **Colaboração**: a Microsoft indica CQRS para "collaborative environments" em que vários usuários modificam os mesmos dados, porque comandos granulares reduzem conflitos de merge [F: microsoft2025cqrs].

[I] Em sistemas de tempo real, o padrão se aplica melhor a interações discretas (turnos, edição colaborativa, presença, chat, placares) do que a simulação contínua de ação, em que o custo do broker e a consistência eventual pesam contra.

## Fundamentos e funcionamento

Fluxo de referência, combinando pub/sub, event sourcing e CQRS [I, a partir de microsoft2026eventsourcing e microsoft2025cqrs]:

```
cliente ──command──▶ command handler ──rehydrate(stream)──▶ regras
                           │ emite event(s)
                           ▼
                      broker/topic ──▶ handler 1: append no event store (system of record)
                                   ──▶ handler 2: atualiza projeção (read model)
                                   ──▶ handler 3: notifica clientes inscritos (push)
cliente ◀──event/state notification── assinatura no topic
```

Pontos documentados:

- **Imutabilidade e compensação.** "you should never update the event data"; a única forma de desfazer é um *compensating event* [F: microsoft2026eventsourcing].
- **Projeções e snapshots.** Como reler todo o stream é caro, mantêm-se *materialized views*; snapshots a cada N eventos permitem reidratar a partir do último snapshot; "Snapshots are an optimization, not a replacement for the eventstream" [F: microsoft2026eventsourcing]. Fowler descreve o mesmo com snapshot noturno em memória e reaplicação após falha [F: fowler2005eventsourcing].
- **Separação leitura/escrita.** Kleppmann formula o princípio: "Databases are global, shared, mutable state"; propõe tratar escritas como fatos imutáveis num log e servir leituras por views derivadas, "A materialized view is just a cached subset of the log"; "This separation of reads and writes is really the key idea here" [F: kleppmann2015insideout]. Segundo o autor, o log "squeezes the non-determinism" da concorrência para fora do caminho de escrita [F: kleppmann2015insideout].
- **Entrega e ordem.** Em pub/sub, "The order in which subscribers receive messages isn't guaranteed"; brokers oferecem *at-most-once*, *at-least-once* ou *exactly-once*, com custos distintos; sem deduplicação, os consumidores devem ser idempotentes [F: microsoft2026pubsub]. Em event sourcing a entrega é tipicamente *at least once*, exigindo handlers idempotentes [F: microsoft2026eventsourcing].
- **Efeitos externos no replay.** Fowler recomenda encapsular integrações em *gateways* que suprimem envios em modo replay, e que "the domain logic should never care about the context of the running of the events" [F: fowler2005eventsourcing].

### Ordem e relógios lógicos

Com vários produtores, a ordem física de chegada não reflete a causalidade. Lamport define a relação *happened before* como uma ordem parcial sobre eventos e dá um algoritmo de relógios lógicos (regras IR1 e IR2) que satisfaz a *Clock Condition* e permite estender a ordem parcial a uma ordem total, usada para construir um *State Machine* replicado [F: lamport1978clocks]. A Microsoft recomenda anotar cada evento com timestamp ou identificador incremental e rejeitar duplicatas de (entidade, id) no event store [F: microsoft2026eventsourcing]. Detalhes em rtm.net.logical-clocks.

### Relação com CRDT e OT

[I] Quando não há um ponto único de serialização (edição offline, multi-região), o log por si não resolve conflitos; entram tipos de dados replicados. Shapiro et al. (2011) definem os *Conflict-free Replicated Data Types* [F: shapiro2011crdt, metadados verificados; conteúdo não acessado nesta sessão]. Operações de CRDT baseados em operação são, na prática, eventos comutativos que podem trafegar por pub/sub; a reconciliação deixa de depender de ordem total. Ver rtm.sync.crdt e rtm.sync.operational-transformation.

### Em frameworks de multiplayer

Os frameworks do domínio expõem primitivas compatíveis com este estilo sem adotá-lo integralmente [I]: Nakama descreve o jogo por turnos ativo como modo autoritativo com *tick rate* baixa, "The expected tick-rate is quite low as the rate of messages sent and received is low" [F: heroiclabs2026multiplayer]; Colyseus trata mensagens nomeadas com um handler por tipo ("You can only define a single handler per message type") e expõe hooks de ciclo de vida da sala [F: colyseus2026room]. [I] Um *room* com handlers por tipo de mensagem e difusão a inscritos é um pub/sub de escopo restrito; acrescentar um log append-only por sala converte-o em event sourcing.

## Algoritmos e modelos relevantes

- Relógios lógicos de Lamport e ordenação total por desempate [F: lamport1978clocks].
- Controle de concorrência otimista no event store: rejeitar append se o stream mudou desde a leitura, então recarregar e repetir [F: microsoft2026eventsourcing].
- Idempotent consumer: rastrear último número de sequência processado por consumidor [F: microsoft2026eventsourcing].
- Snapshot a cada N eventos [F: microsoft2026eventsourcing].
- Versionamento de eventos: deserialização tolerante, versão no envelope, *upcasting* [F: microsoft2026eventsourcing].
- Topics e filtragem por conteúdo para que cada assinante receba só o subconjunto relevante [F: microsoft2026pubsub].

## Requisitos e pressupostos

- Tolerância a **consistência eventual**: "The system is only eventually consistent when it creates materialized views" [F: microsoft2026eventsourcing]; a Microsoft lista como inadequado quando "Systems require consistency and real-time updates to the views of the data" [F: microsoft2026eventsourcing].
- Eventos projetados com **intenção** ("two seats were reserved" em vez de "remaining seats changed to 42") [F: microsoft2026eventsourcing].
- Handlers idempotentes e ordenação explícita por identificador [F: microsoft2026eventsourcing; microsoft2026pubsub].
- Estratégia de evolução de esquema, pois "We have to figure out how to deal with changes in the schema of events over time" [F: fowler2017eventdriven].
- Dados pessoais fora do stream ou *crypto-shredding*, dado o conflito com direito ao esquecimento [F: microsoft2026eventsourcing].

## Vantagens e limitações

Vantagens: baixo acoplamento, "pretty simple to set up" no caso de notificação [F: fowler2017eventdriven]; auditoria e replay [F: fowler2005eventsourcing]; isolamento de falhas, pois "A subscriber failure doesn't affect the publisher or other subscribers" e o broker retém mensagens [F: microsoft2026pubsub]; escalabilidade independente de leitura e escrita [F: microsoft2025cqrs]; testes *given-when-then* sem infraestrutura [F: microsoft2026eventsourcing].

Limitações: a Microsoft classifica event sourcing como "a complex pattern that introduces significant trade-offs" e caro para migrar [F: microsoft2026eventsourcing]; pub/sub é inadequado quando "An application requires near real-time interaction with consumers. The pub/sub model introduces latency through the broker" e quando a ordem é obrigatória [F: microsoft2026pubsub]; o fluxo lógico "is not explicit in any program text" e fica difícil de depurar [F: fowler2017eventdriven]; CQRS é visto por colegas de Fowler como "often misused" [F: fowler2017eventdriven].

## Alternativas e comparações

| Critério | Orientada a eventos | Servidor autoritativo (ticks) |
|---|---|---|
| Unidade de comunicação | evento/comando discreto | entrada por tick e estado |
| Fonte de verdade | event store [F: microsoft2026eventsourcing] | memória do servidor [F: heroiclabs2026authoritative] |
| Consistência | eventual [F: microsoft2026eventsourcing] | forte no servidor, por tick [I] |
| Latência | broker no caminho [F: microsoft2026pubsub] | RTT ao servidor [F: gambetta2014clientserver] |
| Adequação | turnos, colaboração, presença [I] | ação contínua [F: heroiclabs2026multiplayer] |

Tabela completa em rtm.arch.comparison.

## Métricas e métodos de avaliação

- Latência de ponta a ponta produtor→broker→consumidor e *lag* das projeções em relação ao event store [I, a partir de microsoft2026eventsourcing].
- Backlog por assinante (mensagens não confirmadas) e uso de *flow control* [F: microsoft2026pubsub].
- Taxa de duplicatas e de rejeições por concorrência otimista [F: microsoft2026eventsourcing].
- Tamanho de stream por entidade e custo de reidratação com e sem snapshot [F: microsoft2026eventsourcing].

## Exemplo técnico independente de domínio

```
# servidor de sessão com log de eventos e difusão
stream[sessao] = []                      # append-only
clock = 0                                # relógio lógico do servidor

ao_receber_command(sessao, cliente, cmd, cmd_id):
  se cmd_id ja_processado(sessao): return            # idempotência
  estado = projetar(stream[sessao])                  # ou snapshot + delta
  eventos = decidir(estado, cmd)                     # pode rejeitar
  para e em eventos:
    clock += 1; e.seq = clock; e.causa = cmd_id
    append(stream[sessao], e)                        # concorrência otimista
    publicar(topic(sessao), e)                       # assinantes: clientes, projeções
  registrar(cmd_id)

# cliente
ao_receber_evento(e):
  se e.seq != esperado: pedir_replay(desde = esperado)
  estado_local = aplicar(estado_local, e)
```

## Relações com outros conceitos

Alternativa às arquiteturas de simulação (autoritativo, relay, P2P, lockstep). Depende de rtm.net.logical-clocks (ordem causal) e de rtm.rel.delivery-semantics (at-least-once, idempotência). Complementa rtm.sync.crdt e rtm.sync.operational-transformation (reconciliação sem ordem total), rtm.rt.communication-patterns (pub/sub como padrão de comunicação), rtm.mp.turn-based e rtm.mp.presence (casos de uso naturais). Relaciona-se com rtm.proto.websocket (canal usual de push para clientes) e rtm.rel.reconnection (replay desde o último evento conhecido).

## Lacunas e questões abertas

- O capítulo de Kleppmann em *Designing Data-Intensive Applications* não foi acessado; a página do livro (dataintensive.net) informa apenas título e autor. Usou-se a transcrição pública da palestra "Turning the database inside-out" [F: kleppmann2015insideout].
- O texto completo de Shapiro et al. (2011) não foi aberto (página da editora redireciona para autenticação; espelhos HAL/LIP6 bloqueados ou indisponíveis); apenas metadados foram verificados via Semantic Scholar. Definições de CvRDT/CmRDT ficam para rtm.sync.crdt.
- Não há, nas fontes abertas, medição de latência adicionada por brokers em cenários interativos; os fornecedores afirmam qualitativamente que o broker introduz latência [F: microsoft2026pubsub].
- Falta fonte que descreva event sourcing aplicado a sessões de jogo por turnos com números (tamanho de stream, custo de replay); registrar em estudo de caso quando verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fowler2005eventsourcing | tecnico | 2026-10-29 |
| fowler2017eventdriven | tecnico | 2026-10-29 |
| microsoft2026eventsourcing | fornecedor | 2026-10-29 |
| microsoft2026pubsub | fornecedor | 2026-10-29 |
| microsoft2025cqrs | fornecedor | 2026-10-29 |
| kleppmann2015insideout | tecnico | 2026-10-29 |
| lamport1978clocks | academico | 2026-10-29 |
| shapiro2011crdt | academico | 2026-10-29 |
| heroiclabs2026multiplayer | fornecedor | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| gambetta2014clientserver | tecnico | 2026-10-29 |
