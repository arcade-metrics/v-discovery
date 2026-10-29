---
id: dat.plano-ids
titulo: Plano de identificadores do domínio
tipo: mapa
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Plano de identificadores do domínio dados-pesquisa-e-eventos

Lista de ids planejados para a primeira versão, derivada da estrutura sugerida em `00-brief.md`. Relações entre documentos usam estes ids, nunca caminhos de arquivo. Prefixos de área: `ev`, `qual`, `rd`, `ethics`, `ds`.

| Pasta | Id | Arquivo | Escopo em uma linha |
|---|---|---|---|
| events | dat.ev.event-model | events/event-model.md | Evento como fato imutável: envelope, identidade, tipo, versão de esquema, contexto; modelos de referência (CloudEvents, xAPI statement como caso especial) |
| events | dat.ev.game-telemetry | events/game-telemetry.md | Telemetria de jogos: o que instrumentar, métricas de jogo, granularidade, custo de coleta (Drachen, Seif El-Nasr e Canossa) |
| events | dat.ev.event-sourcing | events/event-sourcing.md | Event sourcing e log append-only: estado como projeção de eventos, replay, CQRS, quando não usar |
| events | dat.ev.instrumentation-and-opentelemetry | events/instrumentation-and-opentelemetry.md | OpenTelemetry como referência de instrumentação: sinais (traces, métricas, logs, eventos), convenções semânticas, contexto de propagação |
| events | dat.ev.event-to-xapi-mapping | events/event-to-xapi-mapping.md | Como um esquema de evento interno se mapeia para xAPI sem perda: actor, verb, object, result, context, extensions; perfis |
| quality | dat.qual.granularity-and-constructs | quality/granularity-and-constructs.md | Granularidade mínima de evento para preservar construtos cognitivo-motores (tempo de reação, hesitação, sequência, erro): taxa de amostragem, precisão de timestamp |
| quality | dat.qual.clocks-and-ordering | quality/clocks-and-ordering.md | Relógios de dispositivo, relógio monotônico x de parede, NTP, ordenação causal e sequência por sessão |
| quality | dat.qual.loss-and-deduplication | quality/loss-and-deduplication.md | Perda, duplicação, buffer offline, entrega idempotente, reconciliação na sincronização |
| quality | dat.qual.schema-validation-and-evolution | quality/schema-validation-and-evolution.md | Validação de esquema (JSON Schema, Avro, Protobuf), evolução compatível, registro de esquemas |
| research-data | dat.rd.fair-principles | research-data/fair-principles.md | Princípios FAIR (Wilkinson et al. 2016): findable, accessible, interoperable, reusable; métricas de FAIRness; tensão com dados de menores |
| research-data | dat.rd.data-management-plans | research-data/data-management-plans.md | Plano de gestão de dados: estrutura, exigências de agências (FAPESP, outras), ciclo de vida, custos |
| research-data | dat.rd.repositories-and-versioning | research-data/repositories-and-versioning.md | Repositórios (Zenodo, Dataverse, OSF, repositórios institucionais), DOI de dataset, versionamento (DVC, git-annex), embargo e acesso controlado |
| research-data | dat.rd.data-documentation | research-data/data-documentation.md | Documentação de dataset: datasheets (Gebru et al.), dicionário de dados, codebook, DDI, README de dataset |
| research-ethics | dat.ethics.cep-conep-system | research-ethics/cep-conep-system.md | Sistema CEP/CONEP: Resoluções CNS 466/2012 e 510/2016, Plataforma Brasil, pesquisa com crianças e adolescentes, emendas, prazos |
| research-ethics | dat.ethics.consent-and-assent-in-research | research-ethics/consent-and-assent-in-research.md | TCLE e termo de assentimento em pesquisa: conteúdo mínimo, linguagem, registro; diferença para consentimento de serviço (LGPD) |
| research-ethics | dat.ethics.research-vs-operation | research-ethics/research-vs-operation.md | Separação entre base de pesquisa e base operacional; uso secundário de dado operacional; ética de experimentos A/B em educação |
| datasets | dat.ds.pslc-datashop | datasets/pslc-datashop.md | PSLC DataShop: formato de transação, KCs, exportações, termos de uso |
| datasets | dat.ds.assistments | datasets/assistments.md | ASSISTments: datasets públicos, esquema, usos na literatura, limites |
| datasets | dat.ds.ednet | datasets/ednet.md | EdNet (Riiid): escala, hierarquia KT1 a KT4, licença, limites |
| datasets | dat.ds.comparison | datasets/comparison.md | Comparação dos datasets de referência (inclui OULAD, KDD Cup 2010, Junyi, Duolingo SLAM se verificáveis): tamanho, granularidade, documentação, licença, população |
| (raiz) | dat.index | README.md | |
| (raiz) | dat.glossario | glossario.md | |
| (raiz) | dat.mapa | mapa-conceitos.md | |
| (raiz) | dat.matriz | matriz-comparativa.md | |
| (raiz) | dat.relatorio | relatorio.md | |
| (raiz) | dat.plano-ids | _plano-ids.md | |
| (raiz) | dat.brief | 00-brief.md | |
