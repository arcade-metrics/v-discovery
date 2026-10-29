---
id: lae.index
titulo: Learning analytics, mineração de dados e avaliação
tipo: mapa
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Learning analytics, mineração de dados e avaliação

Base de conhecimento agnóstica sobre como transformar interações de alunos em indicadores confiáveis e em julgamentos de valor sobre aprendizagem. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo e fontes prioritárias em [`00-brief.md`](00-brief.md).

## Como navegar

Comece pelo [mapa de conceitos](mapa-conceitos.md) e pelo [glossário](glossario.md). A [matriz comparativa](matriz-comparativa.md) resume lado a lado as três grandes dicotomias do domínio (LA x EDM, CTT x IRT, experimental x quase-experimental). O [relatório](relatorio.md) registra cobertura, lacunas e próximos passos desta versão.

Leitura sugerida para quem chega sem contexto:

1. `foundations/la-vs-edm.md`: as duas tradições que dão nome ao domínio, e como se relacionam com academic analytics.
2. `foundations/analytics-cycle.md`: o ciclo que liga captura de dado, análise, visualização e intervenção — vocabulário usado pelo resto do domínio.
3. `data-quality/provenance-and-lineage.md` e `bias-and-validity.md`: por que um indicador pode estar tecnicamente correto e ainda assim enganar, e como rastrear sua origem.
4. `indicators/engagement-indicators.md`, `dropout-and-risk-prediction.md`, `dashboards-and-olm.md`: como um indicador vira ação — para prever risco ou para expor ao próprio aluno.
5. `assessment-design/formative-and-summative.md` e `constructive-alignment.md`: o desenho pedagógico que a avaliação deveria servir, antes de qualquer número.
6. `psychometrics/classical-test-theory.md`, `reliability-and-validity.md`, `fairness-in-measurement.md`: como saber se um instrumento de avaliação mede o que diz medir, de forma consistente e equitativa.
7. `evaluation-methods/experimental-design.md` e `effect-size-and-replication.md`: como saber se uma intervenção ou produto de fato gera resultado de aprendizagem, e por que um único estudo raramente basta.

## Pastas

| Pasta | Conteúdo | Prefixo de id |
|---|---|---|
| `foundations/` | Learning Analytics vs. Educational Data Mining, ciclo de LA, níveis de análise | `lae.found.*` |
| `data-quality/` | proveniência e linhagem, vieses e validade de dados de interação | `lae.dq.*` |
| `indicators/` | engajamento, predição de risco/evasão, dashboards e open learner model | `lae.ind.*` |
| `assessment-design/` | avaliação formativa/somativa/diagnóstica, alinhamento construtivo | `lae.asmt.*` |
| `psychometrics/` | teoria clássica dos testes, confiabilidade e validade, equidade de medição | `lae.psy.*` |
| `evaluation-methods/` | desenho experimental e quase-experimental, tamanho de efeito e replicação | `lae.evalm.*` |

A lista completa de ids planejados está em [`_plano-ids.md`](_plano-ids.md).

## Convenções do domínio

- Teoria de Resposta ao Item, Elo e knowledge tracing são tratados só como ponto de relação (`complementa`/`relacionado-a`): o conteúdo em profundidade vive em `aprendizagem-adaptativa`, para não duplicar.
- Telemetria bruta, esquemas de evento, FAIR e LGPD ficam em `dados-pesquisa-e-eventos`; aqui o assunto é a qualidade do dado já capturado, para fins de indicador e análise.
- Formatos padronizados de registro e troca (xAPI, Caliper, QTI) ficam em `interoperabilidade`; citados aqui só como ponto de integração (`complementa`).
- "Course Signals" e outros sistemas citados em `indicators/dropout-and-risk-prediction.md` são tratados como caso histórico de literatura acadêmica, nunca como produto a adotar.
- Nenhum documento trata um indicador, modelo ou instrumento como superior por padrão fora do que a fonte citada sustenta; comparações exigem fonte, de preferência independente de quem propôs o método avaliado.
