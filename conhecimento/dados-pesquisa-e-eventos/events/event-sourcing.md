---
id: dat.ev.event-sourcing
titulo: Event sourcing e log append-only
tipo: tecnica
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [fowler2005eventsourcing, fowler2011cqrs, microsoft2026eventsourcing, young2017versioning, kleppmann2015insideout, kleppmann2017ddia]
relacoes:
  - { tipo: depende-de, alvo: dat.ev.event-model }
  - { tipo: complementa, alvo: dat.ev.event-to-xapi-mapping }
  - { tipo: complementa, alvo: dat.qual.schema-validation-and-evolution }
  - { tipo: complementa, alvo: dat.qual.loss-and-deduplication }
  - { tipo: complementa, alvo: dat.rd.repositories-and-versioning }
  - { tipo: relacionado-a, alvo: dat.ethics.research-vs-operation }
  - { tipo: complementa, alvo: psg.audit.audit-trails }
  - { tipo: relacionado-a, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: complementa, alvo: lae.dq.provenance-and-lineage }
termos: [event sourcing, event store, eventstream, log append-only, projeção, materialized view, rehydration, replay, snapshot, CQRS, evento compensatório, upcasting, crypto-shredding, consistência eventual]
---

# Event sourcing e log append-only

## Definição e terminologia

Fowler define a ideia fundamental como "ensuring every change to the state of an application is captured in an event object, and that these event objects are themselves stored in the sequence they were applied for the same lifetime as the application state itself" [F: fowler2005eventsourcing]. A documentação da Microsoft descreve o **event store** como registro append-only que serve de "system of record", com um **eventstream** por entidade; o estado atual é obtido por **rehydration**, o replay dos eventos da entidade, e consultas usam **materialized views**, projeções somente leitura [F: microsoft2026eventsourcing, Solution].

**CQRS** (Command Query Responsibility Segregation) é a separação entre o modelo usado para atualizar e o usado para ler; Fowler atribui o padrão a Greg Young e adverte que "for most systems CQRS adds risky complexity" [F: fowler2011cqrs]. Event sourcing e CQRS são independentes, embora combinados com frequência [F: fowler2011cqrs] [F: microsoft2026eventsourcing, Solution].

O que não é: um broker de mensagens não é um event store. A Microsoft observa que brokers como Kafka "typically lack per-entity stream queries and optimistic concurrency" e servem como camada de distribuição, não como substituto [F: microsoft2026eventsourcing, Problems and considerations]. Também não é um log de depuração: o evento é a fonte de verdade, não um efeito colateral [I].

## Problema que resolve

Sistemas que guardam só o estado atual perdem o caminho até ele. Fowler lista o que o log permite: reconstrução completa, consulta temporal ("determine the application state at any point in time") e replay corrigido de eventos [F: fowler2005eventsourcing]. Para pesquisa, o ganho principal é que **novas perguntas podem ser feitas aos dados antigos**: uma métrica inventada depois da coleta é uma nova projeção sobre o mesmo log [I]. Kleppmann generaliza a ideia: o banco de dados tradicional já traduz internamente escritas imperativas em "a stream of immutable facts", e tornar esse fluxo explícito permite derivar visões materializadas a partir dele [F: kleppmann2015insideout].

## Fundamentos e funcionamento

1. Comandos são validados contra o estado reidratado e geram eventos; eventos são anexados, nunca alterados [F: microsoft2026eventsourcing, Solution].
2. Conflitos de escrita na mesma entidade usam controle de concorrência otimista: o append é rejeitado se o stream mudou desde a leitura [F: microsoft2026eventsourcing, Pattern advantages].
3. Correções são **eventos compensatórios**, "a new event that reverses or corrects the effect of a previous event"; o evento original permanece [F: microsoft2026eventsourcing, Problems and considerations].
4. Streams longos usam **snapshots** a cada N eventos; snapshots "are an optimization, not a replacement for the eventstream" [F: microsoft2026eventsourcing, Problems and considerations].
5. Entrega a consumidores é tipicamente pelo menos uma vez, então manipuladores devem ser idempotentes e rastrear o último número de sequência processado [F: microsoft2026eventsourcing, Problems and considerations].

**Consultas externas e comportamento.** Se o processamento de um evento depende de dado externo, o replay precisa do valor da época: "If I ask for an exchange rate on December 5th and replay that event on December 20th, I will need the exchange rate on Dec 5" [F: fowler2005eventsourcing, External Queries]. Young responde à pergunta sobre versionar a lógica de reidratação com "you don't": o resultado calculado na época deve estar no evento [F: young2017versioning, General Versioning Concerns]. Para dados educacionais, isso significa gravar no evento a versão do conteúdo, a configuração ativa e o resultado avaliado no momento, e não recalculá-los no replay [I].

**Por que não editar.** Young argumenta que imutabilidade elimina invalidação de cache e simplifica escala, e que "if you allow a single update" o dado deixa de ser imutável [F: young2017versioning, Why can't I update an event?].

## Requisitos e pressupostos

- Eventos desenhados por intenção, não por estado resultante: a Microsoft contrasta "two seats were reserved" com "remaining seats changed to 42", em que o segundo "only tells you the resulting state" [F: microsoft2026eventsourcing, Problems and considerations].
- Estratégia de evolução de esquema definida antes do primeiro evento (ver `dat.qual.schema-validation-and-evolution`).
- Aceitação de consistência eventual entre log e projeções [F: microsoft2026eventsourcing, Problems and considerations].

## Vantagens e limitações

| Vantagens | Limitações |
|---|---|
| trilha de auditoria nativa [F: microsoft2026eventsourcing] | consistência eventual inerente [F: microsoft2026eventsourcing] |
| novas projeções sobre dados antigos [F: fowler2005eventsourcing] | consulta ad hoc difícil sem projeção [F: microsoft2026eventsourcing] |
| correção sem apagar histórico [F: microsoft2026eventsourcing] | eventos errados persistem; exigem compensação ou upcaster [F: microsoft2026eventsourcing] |
| escrita append-only sem contenção de linha [F: microsoft2026eventsourcing] | conflito com direito de eliminação de dados pessoais [F: microsoft2026eventsourcing] |

Para dados pessoais, a Microsoft indica guardar dados pessoais fora do store e referenciá-los por identificador ou, quando não for possível, *crypto-shredding*: cifrar com chave por titular e apagar a chave [F: microsoft2026eventsourcing, Problems and considerations]. Em pesquisa com menores, a pseudonimização na origem reduz esse conflito (ver `psg.deid.anonymization-and-pseudonymization`) [I].

## Alternativas e comparações

| Abordagem | Histórico | Complexidade | Quando |
|---|---|---|---|
| CRUD com estado atual | nenhum | baixa | dados de referência, perfis [F: microsoft2026eventsourcing, When to use] |
| CRUD + tabela de auditoria | parcial (mudanças) | média | auditoria sem replay |
| Log de eventos de telemetria append-only, sem reidratar entidades | completo para eventos | média | coleta de pesquisa |
| Event sourcing completo + CQRS | completo, fonte de verdade | alta | domínio com regras e replay de estado |

A Microsoft desaconselha o padrão para protótipos, MVPs, sistemas de vida curta e equipes sem experiência em arquiteturas orientadas a eventos [F: microsoft2026eventsourcing, When to use this pattern]. Para coleta de pesquisa, a terceira linha costuma bastar: o log é imutável e versionado, mas o sistema operacional pode continuar CRUD [I].

## Exemplo técnico independente de domínio

```
anexar(stream="sessao/S1", esperado=v41, evento={tipo:"resposta.v3", seq:42, ...})
  -> conflito se versao(stream) != 41
projecao "acertos_por_item":
  para cada evento em log desde checkpoint:
     se evento.id ja processado: pular             # idempotência
     se tipo == "resposta.v2": evento = upcast_v2_v3(evento)
     se tipo == "correcao.resposta": desfazer(evento.ref); aplicar(evento)
     atualizar(tabela, evento); checkpoint = evento.seq
```

## Relações com outros conceitos

Depende de `dat.ev.event-model`; projeções para xAPI estão em `dat.ev.event-to-xapi-mapping`. Evolução de esquema e duplicatas estão em `dat.qual.schema-validation-and-evolution` e `dat.qual.loss-and-deduplication`; a semântica de entrega em `rtm.rel.delivery-semantics`. O log é trilha de auditoria (`psg.audit.audit-trails`) e insumo de linhagem (`lae.dq.provenance-and-lineage`); congelar uma fatia do log como dataset liga-se a `dat.rd.repositories-and-versioning`.

## Lacunas e questões abertas

- "Designing Data-Intensive Applications", de Kleppmann (O'Reilly, 2017) [F: kleppmann2017ddia, metadados], só teve metadados verificados; o tratamento de logs e processamento de fluxos no livro não foi lido.
- O livro de Young está marcado pela própria página como 90 % completo, com última atualização em 2017-04-09.
- Falta avaliar quanto custa crypto-shredding em logs de pesquisa de longo prazo e se ele é aceito por comitês de ética como forma de eliminação.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fowler2005eventsourcing | tecnico | 2026-10-30 |
| fowler2011cqrs | tecnico | 2026-10-30 |
| microsoft2026eventsourcing | fornecedor | 2026-10-30 |
| young2017versioning | tecnico | 2026-10-30 |
| kleppmann2015insideout | tecnico | 2026-10-30 |
| kleppmann2017ddia | academico [metadados] | 2026-10-30 |
