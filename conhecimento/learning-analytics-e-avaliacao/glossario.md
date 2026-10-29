---
id: lae.glossario
titulo: Glossário de learning analytics, mineração de dados e avaliação
tipo: glossario
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Glossário: learning analytics, mineração de dados e avaliação

Termos consolidados do domínio, selecionados dos campos `termos:` dos frontmatters. Termos em inglês quando esse é o uso consolidado na literatura. Cada entrada aponta para o documento que aprofunda.

## Fundamentos

| Termo | Definição | Documento |
|---|---|---|
| Learning Analytics (LA) | medição, coleta, análise e reporte de dados sobre alunos e seus contextos, com o propósito de entender e otimizar a aprendizagem e os ambientes em que ela ocorre | lae.found.la-vs-edm |
| Educational Data Mining (EDM) | aplicação de métodos de mineração de dados a dados educacionais para descobrir padrões, com ênfase em descoberta automatizada de modelos | lae.found.la-vs-edm |
| academic analytics | uso de analytics em nível institucional/administrativo, como vizinho histórico de LA e EDM | lae.found.la-vs-edm |
| discovery with models / relationship mining / structure discovery | famílias de técnica de EDM descritas na literatura de mineração de dados educacionais | lae.found.la-vs-edm |
| ciclo de learning analytics | modelo de processo que liga captura de dados, análise, visualização e intervenção, com retroalimentação (*closing the loop*) | lae.found.analytics-cycle |
| reference model (what-who-why-how) | framework de referência de quatro dimensões para descrever um sistema de LA | lae.found.analytics-cycle |
| micro/meso/macro-level | níveis de análise de LA — aluno individual, curso/turma, instituição | lae.found.analytics-cycle |

## Qualidade de dado

| Termo | Definição | Documento |
|---|---|---|
| proveniência (*provenance*) | registro verificável de origem e transformação de um dado até um indicador | lae.dq.provenance-and-lineage |
| data lineage | rastro documentado das transformações aplicadas a um dado ao longo de um pipeline | lae.dq.provenance-and-lineage |
| why / where provenance | tipos de proveniência: por que um dado está no resultado, e de onde especificamente ele veio | lae.dq.provenance-and-lineage |
| PROV-O | modelo de referência de proveniência do W3C, citado aqui apenas como ponto de integração futura | lae.dq.provenance-and-lineage |
| trace data | dado de interação deixado automaticamente por um aluno ao usar um sistema digital | lae.dq.bias-and-validity |
| viés de construto (*construct validity* comprometida) | quando o dado de log não mede o construto que se pretende medir | lae.dq.bias-and-validity |
| confundimento / causalidade reversa | ameaças a inferir causa a partir de correlação entre indicador e resultado | lae.dq.bias-and-validity |

## Indicadores

| Termo | Definição | Documento |
|---|---|---|
| engajamento comportamental / cognitivo / emocional | as três dimensões de engajamento do framework de Fredricks, Blumenfeld & Paris | lae.ind.engagement-indicators |
| proxy comportamental | medida indireta (ex. tempo em tela) usada como substituto de um construto não observável diretamente | lae.ind.engagement-indicators |
| early warning system (EWS) | sistema que identifica alunos em risco acadêmico a partir de indicadores, para possibilitar intervenção | lae.ind.dropout-and-risk-prediction |
| profecia autorrealizável | risco de uma predição de risco influenciar o próprio resultado que tenta prever | lae.ind.dropout-and-risk-prediction |
| learning analytics dashboard (LAD) | painel de visualização de indicadores voltado a aluno, professor ou gestor | lae.ind.dashboards-and-olm |
| data literacy / dashboard literacy | capacidade de interpretar corretamente dados e visualizações de um dashboard | lae.ind.dashboards-and-olm |
| open learner model (OLM) | modelo de aluno exposto de forma compreensível ao próprio aluno ou a outros interessados (aprofundado em aprendizagem-adaptativa) | lae.ind.dashboards-and-olm |

## Avaliação formativa e desenho curricular

| Termo | Definição | Documento |
|---|---|---|
| avaliação formativa | avaliação de um estágio intermediário, voltada a ajustar o ensino em curso | lae.asmt.formative-and-summative |
| avaliação somativa | avaliação ao final de um processo, voltada a certificar ou decidir progressão | lae.asmt.formative-and-summative |
| feed up / feed back / feed forward | as três perguntas do modelo de feedback de Hattie & Timperley (para onde vou, como estou indo, para onde ir depois) | lae.asmt.formative-and-summative |
| constructive alignment (alinhamento construtivo) | princípio de Biggs de alinhar objetivos, atividades de ensino e avaliação | lae.asmt.constructive-alignment |
| taxonomia de Bloom revisada | taxonomia de objetivos educacionais de Anderson & Krathwohl, cruzando processo cognitivo e tipo de conhecimento | lae.asmt.constructive-alignment |
| SOLO taxonomy | taxonomia de Biggs & Collis para classificar a qualidade estrutural de uma resposta | lae.asmt.constructive-alignment |

## Psicometria

| Termo | Definição | Documento |
|---|---|---|
| classical test theory (CTT) | modelo em que o escore observado é a soma do escore verdadeiro e de um erro de medição | lae.psy.classical-test-theory |
| índice de dificuldade / discriminação | estatísticas clássicas de item usadas na CTT | lae.psy.classical-test-theory |
| dependência de amostra / de teste | limitações da CTT: estatísticas de item mudam conforme a amostra ou o teste usado | lae.psy.classical-test-theory |
| confiabilidade (consistência interna, teste-reteste, formas paralelas) | grau em que um instrumento produz resultados consistentes | lae.psy.reliability-and-validity |
| alfa de Cronbach / ômega de McDonald | estatísticas usadas para estimar consistência interna, com críticas à primeira | lae.psy.reliability-and-validity |
| validade de construto, conteúdo, critério | tipos de evidência de validade de um instrumento de medição | lae.psy.reliability-and-validity |
| Differential Item Functioning (DIF) | quando um item tem comportamento estatístico diferente entre subgrupos de mesma habilidade | lae.psy.fairness-in-measurement |

## Métodos de avaliação de resultado

| Termo | Definição | Documento |
|---|---|---|
| randomized controlled trial (RCT) | desenho experimental com atribuição aleatória a tratamento ou controle | lae.evalm.experimental-design |
| desenho quase-experimental | desenho sem randomização, usado quando ela não é viável (ex. regressão descontínua, diferenças em diferenças) | lae.evalm.experimental-design |
| validade interna / externa | ameaças centrais a um desenho experimental ou quase-experimental | lae.evalm.experimental-design |
| unidade de randomização / contaminação / SUTVA | cuidados ao desenhar A/B testing em contexto educacional | lae.evalm.experimental-design |
| effect size (tamanho de efeito) | medida padronizada de magnitude, independente do tamanho da amostra | lae.evalm.effect-size-and-replication |
| meta-análise | método de agregação estatística de resultados de múltiplos estudos | lae.evalm.effect-size-and-replication |
| crise de replicação / pré-registro | dificuldade de reproduzir achados originais, e a prática de registrar hipóteses antes da coleta como mitigação | lae.evalm.effect-size-and-replication |
