---
id: adp.glossario
titulo: Glossário de aprendizagem adaptativa e gêmeos digitais para aprendizagem
tipo: glossario
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Glossário: aprendizagem adaptativa e gêmeos digitais para aprendizagem

Termos consolidados do domínio, selecionados dos campos `termos:` dos frontmatters por aparecerem em mais de um documento ou serem centrais à área. Termos em inglês quando esse é o uso consolidado na literatura. Cada entrada aponta para o documento que aprofunda e cita a fonte.

## Modelos de aluno e design instrucional

| Termo | Definição | Documento |
|---|---|---|
| learner model | registro persistente, por knowledge component, do que o sistema infere sobre o conhecimento e os traços de um aluno | adp.lm.learner-model |
| overlay model | representação do progresso do aluno como sobreposição estrutural ao modelo de domínio | adp.lm.learner-model |
| inner loop / outer loop | os dois laços de decisão de um sistema tutor: por passo (feedback, dicas) e por tarefa (o que estudar a seguir) | adp.lm.learner-model, adp.adapt.adaptive-learning-systems |
| open learner model (OLM) | learner model exposto, em forma compreensível, ao próprio aluno, professor ou outros interessados | adp.lm.open-learner-model |
| negotiated learner model | OLM em que aluno e sistema buscam concordar sobre o conteúdo do modelo por meio de diálogo | adp.lm.open-learner-model |
| knowledge component (KC) | unidade cognitiva adquirida, inferível a partir do desempenho em tarefas relacionadas | adp.id.knowledge-components |
| learning event | mudança cognitiva não observável: construção ou aplicação de um knowledge component | adp.id.kli-framework |
| instructional event / assessment event | atividade observável, controlada por um instrutor, que visa produzir ou avaliar aprendizagem | adp.id.kli-framework |
| alignment hypothesis / asymmetry hypothesis | hipóteses concorrentes sobre como a complexidade da instrução deveria depender da complexidade do conhecimento-alvo | adp.id.kli-framework |
| Q-matrix | matriz item-atributo que mapeia tarefas a knowledge components, usada em diagnóstico psicométrico | adp.id.knowledge-components |
| Learning Factors Analysis (LFA) | busca combinatória automatizada (A* + regressão logística) por modelos de KC melhor ajustados a dados reais | adp.id.knowledge-components |
| closing the loop | ciclo completo de descoberta estatística de KC, interpretação, redesenho instrucional e validação experimental de ganho de aprendizagem | adp.id.knowledge-components |

## Knowledge tracing

| Termo | Definição | Documento |
|---|---|---|
| knowledge tracing | estimar, a partir do histórico de respostas, a probabilidade de um aluno dominar um componente de conhecimento | adp.kt.bayesian-knowledge-tracing |
| slip / guess | probabilidade de errar mesmo sabendo, ou acertar mesmo sem saber, usadas no BKT para tornar o desempenho observado probabilístico | adp.kt.bayesian-knowledge-tracing |
| identifiability (model degeneracy) | situação em que combinações distintas de parâmetros produzem a mesma predição agregada, tornando os parâmetros individuais não recuperáveis dos dados | adp.kt.bayesian-knowledge-tracing |
| deep knowledge tracing (DKT) | uso de redes neurais recorrentes (RNN/LSTM) para modelar o estado de conhecimento do aluno como vetor latente contínuo aprendido dos dados | adp.kt.deep-knowledge-tracing |
| prediction-consistent regularization | termos de regularização (reconstrução + "waviness") que corrigem incoerências nas predições do DKT ao longo do tempo | adp.kt.deep-knowledge-tracing |
| Additive Factors Model (AFM) | modelo logístico que soma, por componente de conhecimento, um termo de dificuldade e um termo de ganho proporcional às oportunidades de prática | adp.kt.logistic-models |
| Performance Factors Analysis (PFA) | reconfiguração do AFM sensível ao desempenho (sucessos/fracassos passados, não apenas contagem de oportunidades) | adp.kt.logistic-models |
| memory-augmented knowledge tracing | KT que usa memória externa chave-valor endereçável em vez de um único estado recorrente | adp.kt.deep-kt-successors |
| attention-based knowledge tracing | KT que pondera interações passadas por relevância via mecanismo de atenção | adp.kt.deep-kt-successors |
| label leakage (avaliação de KT) | vazamento do rótulo verdadeiro em avaliações "one-by-one" de sequências expandidas por KC, que infla artificialmente o desempenho relatado | adp.kt.deep-kt-successors |

## Teoria de resposta ao item e Elo

| Termo | Definição | Documento |
|---|---|---|
| item characteristic curve (ICC) | curva que dá a probabilidade de acerto em função da habilidade do respondente | adp.irt.item-response-theory |
| local independence | pressuposto de que respostas a itens são independentes dado o traço latente | adp.irt.item-response-theory |
| computerized adaptive testing (CAT) | teste em que cada item é selecionado dinamicamente a partir de um banco calibrado, conforme a estimativa corrente de habilidade | adp.irt.item-response-theory |
| uncertainty function (Elo) | função decrescente no número de respostas que substitui a constante K fixa, acelerando convergência inicial e estabilizando no longo prazo | adp.irt.elo-rating |
| cold start (modelagem de aluno) | problema de estimar habilidade/dificuldade com poucos dados; o Elo mitiga com poucas dezenas de respostas por aluno | adp.irt.elo-rating |

## Memória, esquecimento e repetição espaçada

| Termo | Definição | Documento |
|---|---|---|
| forgetting curve | curva que descreve o declínio da retenção de memória em função do tempo desde o estudo | adp.sr.memory-and-forgetting |
| savings (method of savings) | fração do esforço original de aprendizagem poupada ao reaprender material após um intervalo; medida clássica de Ebbinghaus | adp.sr.memory-and-forgetting |
| storage strength / retrieval strength | na New Theory of Disuse de Bjork: quão bem aprendido está um item (nunca perdido) vs. quão acessível está no momento (declina com desuso) | adp.sr.memory-and-forgetting |
| stability (S) / retrievability (R) | na tradição SuperMemo/Wozniak: intervalo que mantém 90% de recordação média (S), e probabilidade de recordação em um dado momento, R=e^(-t/S) (R) | adp.sr.memory-and-forgetting, adp.sr.fsrs |
| spacing effect | ganho de retenção quando apresentações do mesmo material são espaçadas em vez de massificadas | adp.sr.spacing-and-testing-effects |
| lag effect | comparação entre diferentes níveis de espaçamento (ISI) entre si | adp.sr.spacing-and-testing-effects |
| interstudy interval (ISI) / retention interval (RI) | intervalo entre episódios de estudo do mesmo material / intervalo entre o último estudo e o teste final, que determina o ISI ótimo | adp.sr.spacing-and-testing-effects |
| testing effect (retrieval practice) | ganho de retenção ao tentar recuperar o material da memória em vez de reestudá-lo | adp.sr.spacing-and-testing-effects |
| desirable difficulties | condições de prática (espaçamento, intercalação, teste) que dificultam o desempenho imediato mas melhoram a retenção a prazo | adp.sr.spacing-and-testing-effects |
| ease factor (EF) | multiplicador por item do SM-2 que cresce ou encolhe o intervalo conforme a nota de qualidade da resposta | adp.sr.classical-algorithms |
| half-life (meia-vida) | tempo estimado para a probabilidade de recordação de um item cair pela metade, na curva exponencial de esquecimento | adp.sr.half-life-regression |
| DSR model (difficulty, stability, retrievability) | representação de estado de memória por item usada pelo FSRS: dificuldade, estabilidade e probabilidade de recordação atual | adp.sr.fsrs |
| desired retention (retenção desejada) | parâmetro definido pelo usuário no FSRS para controlar o trade-off entre carga de revisões e probabilidade de recordação no momento da revisão | adp.sr.fsrs |
| time windows (janelas temporais de prática) | divisão do histórico de tentativas em intervalos crescentes, usada por DASH/DAS3H para modelar esquecimento por habilidade | adp.sr.comparison |

## Adaptação e sequenciamento

| Termo | Definição | Documento |
|---|---|---|
| adaptive learning | sistema que infere conhecimento, objetivos ou preferências do aluno e usa essa inferência para mudar conteúdo, sequência, feedback ou apresentação | adp.adapt.adaptive-learning-systems |
| adaptivity vs. adaptability | distinção entre adaptação dirigida pelo sistema (a partir de um modelo de usuário) e customização dirigida pelo próprio usuário | adp.adapt.adaptive-learning-systems |
| macroadaptation | desenho de laço externo que escolhe a próxima tarefa pelo recobrimento entre os componentes de conhecimento que ela exercita e os que o aluno já domina | adp.adapt.adaptive-learning-systems |
| mastery threshold | limiar sobre uma estimativa de domínio (ex.: 0,95 em BKT) usado para decidir quando parar de praticar um componente | adp.adapt.sequencing-policies |
| target success rate | taxa de acerto alvo usada para selecionar itens de dificuldade calibrada à habilidade estimada do aluno, tipicamente via Elo | adp.adapt.sequencing-policies |
| instructional sequencing as MDP/POMDP | formulação do sequenciamento como problema de decisão sequencial sob incerteza, em que a especificação da recompensa é o ponto mais frágil | adp.adapt.sequencing-policies |
| myopic policy | política que otimiza a recompensa esperada apenas do próximo passo, aproximação tratável de planejamento em POMDP | adp.adapt.sequencing-policies |

## Gêmeos digitais

| Termo | Definição | Documento |
|---|---|---|
| digital twin | construto virtual vinculado a um objeto físico específico por fluxo de dados automático e bidirecional ao longo do ciclo de vida | adp.dt.digital-twin-origins |
| digital model / digital shadow / digital twin (taxonomia de 3 níveis) | classificação pela direção do fluxo de dados: nenhum fluxo automático, fluxo unidirecional (físico→virtual), ou fluxo automático bidirecional | adp.dt.digital-twin-origins |
| Digital Twin Prototype (DTP) / Digital Twin Instance (DTI) | gêmeo do artefato genérico (como projetado) vs. gêmeo de um exemplar físico específico, vinculado a ele por toda a vida útil | adp.dt.digital-twin-origins |
| human digital twin (HDT) | réplica digital de uma pessoa física, construída a partir de dados externos, fisiológicos, comportamentais, sociais e ambientais | adp.dt.human-digital-twin |
| learning digital twin / student digital twin | termo ainda instável na literatura para réplica digital de um aluno; a maior parte do que é chamado de "digital twin em educação" refere-se a laboratórios, equipamentos ou campi, não ao aluno | adp.dt.learning-digital-twin |
| Tests of Virtuality | bateria de três testes (sensorial-visual, desempenho, refletividade) propostos por Grieves para avaliar se um sistema virtual é indistinguível do físico correspondente | adp.dt.architecture-and-validation |
| twinning / sincronização bidirecional | mecanismo de atualização contínua entre físico e virtual que distingue um digital twin de um modelo estático | adp.dt.architecture-and-validation |

## Avaliação

| Termo | Definição | Documento |
|---|---|---|
| scoring rule (própria/imprópria) | regra de pontuação que recompensa dizer a verdade sobre a distribuição prevista; MAE é imprópria, RMSE e log-likelihood são próprias | adp.eval.predictive-metrics |
| calibration (calibração) | correspondência entre probabilidade prevista e frequência observada, distinta de discriminação/ranking (AUC) | adp.eval.predictive-metrics |
| student-level cross-validation | divisão de dados em que todo o histórico de um aluno fica inteiramente em treino ou em teste, testando generalização a alunos novos | adp.eval.evaluation-protocols |
| ABROCA (Absolute Between-ROC Area) | métrica que mede a área absoluta entre curvas ROC de dois subgrupos, quantificando disparidade de acurácia sem depender de um limiar único | adp.eval.heterogeneous-populations |
| non-malleability test (teste de não-maleabilidade) | critério de Baker & Hawn para decidir que atributos do aluno (imutáveis, não escolhidos) devem ser tratados como eixo de viés algorítmico | adp.eval.heterogeneous-populations |
| effect size (Hedges's g) | diferença de médias padronizada entre grupo tratamento e controle, corrigida para viés de amostra pequena; métrica-padrão de eficácia educacional em meta-análises | adp.eval.educational-effectiveness |
