---
id: dat.index
titulo: Dados de pesquisa e eventos
tipo: mapa
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Dados de pesquisa e eventos

Base de conhecimento agnóstica sobre como capturar, estruturar, governar e compartilhar dados gerados pela interação com software educacional, com foco em pesquisa. Cobre o evento como unidade de registro, a qualidade do dado no momento da coleta, a gestão de dados de pesquisa, a ética em pesquisa com crianças e os datasets públicos de referência. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo e fontes prioritárias em [`00-brief.md`](00-brief.md).

## Como navegar

Comece pelo [mapa de conceitos](mapa-conceitos.md) e pelo [glossário](glossario.md). A [matriz comparativa](matriz-comparativa.md) reúne em tabelas as comparações centrais: envelopes de evento, formas de persistência, carimbo de tempo, deduplicação, formatos de esquema, tempo de reação em laboratório e online, repositórios, planos de gestão de dados, documentação de dataset, regimes de revisão ética, consentimento e datasets de referência. O [relatório](relatorio.md) registra método, cobertura, lacunas e próximos passos desta versão.

Leitura sugerida para quem chega sem contexto:

1. `events/event-model.md`: o evento como fato imutável com envelope, identidade, tipo, versão de esquema e dois relógios. É o vocabulário do resto do domínio.
2. `events/game-telemetry.md` e `events/instrumentation-and-opentelemetry.md`: o que instrumentar numa atividade lúdica e como o OpenTelemetry resolve tempo, sessão e contexto.
3. `quality/clocks-and-ordering.md` e `quality/granularity-and-constructs.md`: qual relógio carimba cada evento e qual grão preserva tempo de reação, hesitação e trajetória.
4. `quality/loss-and-deduplication.md` e `quality/schema-validation-and-evolution.md`: como saber quanto se perdeu e como mudar o esquema sem tornar ilegíveis os eventos antigos.
5. `events/event-sourcing.md` e `events/event-to-xapi-mapping.md`: o log append-only como fonte de verdade e a projeção para xAPI sem perda.
6. `research-data/fair-principles.md`, `data-management-plans.md`, `repositories-and-versioning.md`, `data-documentation.md`: como o dado coletado vira dataset citável, com acesso controlado quando os titulares são crianças.
7. `research-ethics/cep-conep-system.md`, `consent-and-assent-in-research.md`, `research-vs-operation.md`: o que precisa passar por comitê de ética, o que o termo de consentimento e o de assentimento devem conter, e quando a operação de um serviço vira pesquisa.
8. `datasets/comparison.md`, depois `pslc-datashop.md`, `assistments.md` e `ednet.md`: o que os datasets públicos de referência oferecem e o que nenhum deles cobre.

## Pastas

| Pasta | Conteúdo | Prefixo de id |
|---|---|---|
| `events/` | modelo de evento, telemetria de jogos, event sourcing, instrumentação e OpenTelemetry, mapeamento para xAPI | `dat.ev.*` |
| `quality/` | granularidade e construtos cognitivo-motores, relógios e ordenação, perda e deduplicação, validação e evolução de esquema | `dat.qual.*` |
| `research-data/` | princípios FAIR, planos de gestão de dados, repositórios e versionamento, documentação de dataset | `dat.rd.*` |
| `research-ethics/` | sistema CEP/Conep e Sistema Nacional, consentimento e assentimento em protocolo, pesquisa versus operação | `dat.ethics.*` |
| `datasets/` | PSLC DataShop, ASSISTments, EdNet e comparação com OULAD, KDD Cup 2010, Junyi e Duolingo SLAM | `dat.ds.*` |

A lista completa de ids planejados está em [`_plano-ids.md`](_plano-ids.md).

## Convenções do domínio

- **Fronteira com `privacidade-seguranca-e-governanca`.** LGPD, consentimento como gestão de permissões de serviço, anonimização, pseudonimização, k-anonimato, privacidade diferencial e risco de reidentificação ficam lá (`psg.legal.*`, `psg.consent.*`, `psg.deid.*`). Aqui esses temas aparecem só quando o dado vira dataset de pesquisa, por relação. O consentimento e o assentimento tratados aqui são exigência de protocolo de pesquisa (`dat.ethics.consent-and-assent-in-research`); o par equivalente de serviço está em `psg.consent.parental-consent` e `psg.consent.child-assent`.
- **Fronteira com `interoperabilidade`.** A especificação xAPI está em `iop.lr.xapi`, e a comparação com Caliper e cmi5 em `iop.lr.comparison`. Aqui fica só o esquema interno e a projeção para xAPI (`dat.ev.event-to-xapi-mapping`), como o brief decidiu.
- **Fronteira com `realtime-multiplayer`.** Sincronização de relógio, relógios lógicos e semânticas de entrega estão em `rtm.net.clock-synchronization`, `rtm.net.logical-clocks` e `rtm.rel.delivery-semantics`. Os documentos de `quality/` aplicam essa teoria à coleta para pesquisa sem repeti-la.
- **Fronteira com `aprendizagem-adaptativa`.** Modelos preditivos, knowledge tracing e knowledge components ficam em `adp.*`. Os documentos de `datasets/` descrevem os dados; a comparação de modelos sobre eles está em `adp.kt.comparison`.
- **Fronteira com `learning-analytics-e-avaliacao`.** Proveniência, vieses de dado de interação e desenho experimental ficam em `lae.dq.*` e `lae.evalm.*`; aqui o assunto é o dado no momento da coleta e o seu caminho até um dataset.
- Nomes de publicadores de datasets (universidades, empresas, fundações) aparecem só como autoria do dado, nunca como recomendação de produto.
- Campos e nomes em exemplos técnicos (por exemplo `xclocksource`, `xmonotonicns`) são ilustrativos, como os próprios documentos declaram; não são padrão publicado.
