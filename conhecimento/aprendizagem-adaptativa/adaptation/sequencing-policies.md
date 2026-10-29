---
id: adp.adapt.sequencing-policies
titulo: Políticas de seleção e sequenciamento de atividades
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [vanlehn2006behavior, corbett1995kt, pelanekrihak2017mastery, pelanek2016elo, doroudi2019reward, bloom1968mastery]
relacoes:
  - { tipo: parte-de, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: depende-de, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: depende-de, alvo: adp.irt.elo-rating }
  - { tipo: alternativa-a, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: avaliado-por, alvo: adp.eval.evaluation-protocols }
  - { tipo: relacionado-a, alvo: adp.kt.logistic-models }
termos: [mastery threshold, instructional sequencing, Markov decision process, POMDP, myopic policy, target success rate, aptitude-treatment interaction]
---

# Políticas de seleção e sequenciamento de atividades

## Definição e terminologia

Sequenciamento instrucional (*instructional sequencing*) é o problema de decidir, a cada momento, qual atividade (item, tarefa, unidade) apresentar a um aluno específico, dado tudo o que se infere sobre seu estado de conhecimento até ali [F: doroudi2019reward]. É o conteúdo concreto do laço externo descrito em `adp.adapt.adaptive-learning-systems`: ali se descrevem os quatro desenhos de laço externo (menu, sequência fixa, mastery learning, macroadaptação); aqui se detalham as políticas que implementam mastery learning e macroadaptação, e a forma mais geral de tratá-las como problema de decisão sequencial.

O termo cobre três famílias de política, que coexistem na literatura e muitas vezes se combinam: (1) **critério de mastery** — parar de praticar um componente quando uma estimativa de domínio cruza um limiar [F: pelanekrihak2017mastery]; (2) **seleção por dificuldade alvo** — escolher o próximo item para que a taxa de acerto esperada fique próxima de um valor alvo [F: pelanek2016elo]; (3) **sequenciamento como decisão sequencial sob incerteza** — formular a escolha de ação como um Markov Decision Process (MDP) ou Partially Observable MDP (POMDP) e buscar a política que maximiza uma função de recompensa relacionada à aprendizagem [F: doroudi2019reward]. As duas primeiras famílias podem ser vistas como casos particulares, com políticas e funções de recompensa implícitas, da terceira [F: doroudi2019reward].

O que não é: sequenciamento não é o mesmo que a estimação do estado de conhecimento em si (BKT, modelos logísticos — `adp.kt.bayesian-knowledge-tracing`, `adp.kt.logistic-models`), embora dependa dela; é a camada de decisão que consome essas estimativas [I].

## Problema que resolve

Dado um orçamento de tempo e atenção finito, qual sequência de atividades leva o aluno a aprender mais, mais rápido, ou com menos esforço desperdiçado? Atkinson, citado por Doroudi, Aleven e Brunskill, argumentou já em 1972 que uma teoria de instrução precisa de quatro ingredientes: um modelo do processo de aprendizagem, uma especificação das ações instrucionais admissíveis, uma especificação dos objetivos instrucionais e uma escala de custos e payoffs — os mesmos ingredientes que definem formalmente um MDP [F: doroudi2019reward]. Praticar aleatoriamente ou em ordem fixa desperdiça tempo em itens já dominados ou aplica itens difíceis demais antes da hora; o objetivo das políticas de sequenciamento é usar a estimativa de estado do aluno para evitar esse desperdício [I, a partir de F: doroudi2019reward].

## Fundamentos e funcionamento

### Critério de mastery (mastery threshold)

A forma mais simples de critério de mastery usa um limiar fixo T sobre uma estimativa de probabilidade de resposta correta (ou de estado "aprendido"): o sistema declara domínio quando a estimativa ultrapassa T [F: pelanekrihak2017mastery]. No tutor original de Corbett e Anderson, o critério é uma probabilidade de conhecimento (estimada por BKT) de 0,95 por regra; o próprio artigo observa a analogia com sistemas de mastery learning autoguiados baseados no Personalized System of Instruction de Keller, que a literatura já mostrava eficazes em elevar a média de desempenho [F: corbett1995kt]. Pelánek e Řihák mostram que esse valor específico não é arbitrário na prática: usando curvas de esforço-contra-resultado (*effort-score graphs*) com dados reais de um sistema de gramática checa, o ganho de desempenho satura (deixa de compensar o esforço adicional) justamente perto de um limiar de 0,95 para componentes de conhecimento difíceis, o que os autores interpretam como evidência de que 0,95 é um compromisso razoável, não apenas uma convenção herdada [F: pelanekrihak2017mastery].

Existem alternativas mais simples ao critério por limiar sobre um modelo probabilístico: "N acertos seguidos" (*N correct in a row*) e taxa de acerto média nas últimas N tentativas são usadas na prática e dispensam ajuste de um modelo completo [F: pelanekrihak2017mastery]. Pelánek e Řihák argumentam, a partir de experimentos com dados simulados e reais, que métodos simples como a média móvel exponencial (EMA) são suficientemente flexíveis e que o esforço de pesquisa deveria se concentrar mais no ajuste do limiar e na escolha dos dados usados (por exemplo, se incorporar tempo de resposta) do que na escolha do modelo de aluno em si [F: pelanekrihak2017mastery].

### Seleção por dificuldade alvo e Elo

Uma segunda família de política não declara domínio e para, mas escolhe continuamente o próximo item de modo que a dificuldade fique calibrada à habilidade do aluno. O sistema Outline Maps, descrito por Pelánek, usa uma taxa de sucesso alvo (por exemplo, 75%) e seleciona adaptativamente itens cuja dificuldade estimada, combinada com a habilidade estimada do aluno, produza essa taxa esperada [F: pelanek2016elo]. A estimativa de habilidade e de dificuldade vem de uma adaptação do sistema de rating Elo (originado no xadrez) ao contexto educacional: a probabilidade de resposta correta é modelada pela função logística da diferença entre a habilidade do aluno θ e a dificuldade do item d, `P(correto) = 1/(1 + e^-(θ-d))`, e tanto θ quanto d são atualizados a cada resposta por uma regra de atualização incremental, análoga à atualização de rating após uma partida [F: pelanek2016elo]. Pelánek mostra, com dados simulados, que essa atualização Elo produz estimativas de dificuldade próximas das obtidas por estimação de máxima verossimilhança conjunta (um método bem mais custoso computacionalmente), com a vantagem de permitir atualização incremental online — útil justamente para decidir o próximo item em tempo real — e de produzir estimativas razoáveis de habilidade já a partir de dez respostas por aluno (correlação 0,8 com o valor simulado verdadeiro) [F: pelanek2016elo]. O documento `adp.irt.elo-rating` aprofunda esse modelo; aqui o ponto é seu uso como mecanismo de seleção: escolher o item cuja dificuldade estimada está mais próxima da habilidade estimada do aluno (ou de um deslocamento que produza a taxa de sucesso alvo), o que é o análogo contínuo do critério de mastery por limiar [I, a partir de F: pelanek2016elo].

### Sequenciamento como MDP/POMDP

Formalmente, um MDP de horizonte finito especifica estados, ações admissíveis, uma função de transição e uma função de recompensa R(s,a) [F: doroudi2019reward]. Quando o estado de conhecimento do aluno não é diretamente observável — o caso comum, já que só se observa a resposta (certa/errada), não o estado latente "sabe/não sabe" — o problema correto é um POMDP [F: doroudi2019reward]. Doroudi, Aleven e Brunskill notam explicitamente que, se o critério de recompensa for ignorado, o próprio modelo BKT (`adp.kt.bayesian-knowledge-tracing`) é equivalente a um POMDP com dois estados ocultos por componente de conhecimento; BKT não costuma ser enquadrado como RL porque sua função de recompensa não é declarada explicitamente, embora o uso de BKT para mastery learning siga implicitamente alguma função de recompensa — por exemplo, recompensa 1 quando o aluno transita do estado não aprendido para o aprendido [F: doroudi2019reward]. Isso implica que políticas de mastery threshold e políticas explicitamente derivadas de RL não são categorias totalmente separadas: a primeira é um caso particular da segunda com recompensa implícita e planejamento restrito [F: doroudi2019reward].

Planejamento e aprendizagem por reforço em POMDPs gerais são intratáveis; por isso, modelos usados na prática (como BKT) são POMDPs deliberadamente muito restritos, o que viabiliza encontrar uma política ótima, e é comum usar aproximações como planejamento *míope* (*myopic planning*) — escolher a ação que maximiza a recompensa esperada apenas no próximo passo, ignorando o horizonte mais longo — em vez de planejamento de longo horizonte [F: doroudi2019reward]. Já em 1972, Atkinson usava uma política míope por esse motivo prático, e Doroudi et al. observam que, em alguns casos simples, a política míope é de fato ótima e, mesmo quando não é, costuma ficar próxima do ótimo [F: doroudi2019reward].

### A crítica da recompensa

O título do artigo de revisão de Doroudi, Aleven e Brunskill — "Where's the Reward?" — resume seu argumento central: formular sequenciamento como MDP/POMDP obriga a declarar explicitamente uma função de recompensa, e essa declaração é o passo em que a maior parte do trabalho conceitual (e o maior risco de erro) se concentra, porque proxies plausíveis de "aprendizagem" (acerto na próxima tentativa, tempo até mastery, nota em pós-teste) podem levar a políticas muito diferentes entre si [F: doroudi2019reward]. Os autores notam que até estudos clássicos de mastery learning, quando comparados a um baseline de "nenhuma remediação" em vez de a outra forma de sequenciar a remediação, não constituem evidência de que a política de mastery seja melhor que outras políticas de sequenciamento — apenas de que mastery é melhor que não fazer nada [F: doroudi2019reward]. Essa ressalva se aplica ao próprio estudo original de Corbett e Anderson, citado por Doroudi et al. exatamente como exemplo desse tipo de comparação [F: doroudi2019reward].

## Algoritmos e modelos relevantes

- **Critério de limiar fixo** sobre uma estimativa de modelo (BKT, 0,95) ou sobre estatística simples (N acertos seguidos, EMA) [F: pelanekrihak2017mastery].
- **Elo / seleção por dificuldade alvo**: atualização incremental de habilidade e dificuldade via função logística, seleção do item que aproxima a taxa de sucesso esperada de um alvo fixo [F: pelanek2016elo].
- **MDP com planejamento míope**: ajusta um modelo (transição e recompensa) aos dados e escolhe, a cada passo, a ação que maximiza o valor esperado de curto prazo [F: doroudi2019reward].
- **POMDP com estimação de parâmetros**: formulação mais geral, da qual BKT é um caso restrito; parâmetros estimados por expectation-maximization ou métodos análogos [F: doroudi2019reward].

## Requisitos e pressupostos

- Um modelo de estado do aluno já ajustado aos dados (BKT, logístico ou Elo) antes de a política poder operar sobre ele [F: pelanekrihak2017mastery] [F: pelanek2016elo].
- Para políticas de MDP/POMDP explícitas: uma função de recompensa declarada e defensável — o ponto mais frágil do enfoque, segundo a revisão [F: doroudi2019reward].
- Dados suficientes por aluno para a atualização incremental ser informativa; no caso Elo, da ordem de dez respostas por aluno para uma estimativa razoável de habilidade, segundo simulação [F: pelanek2016elo].
- Granularidade de componente de conhecimento bem definida e tratável como unidade independente — pressuposto compartilhado com BKT (`adp.kt.bayesian-knowledge-tracing`) [F: pelanekrihak2017mastery].

## Vantagens e limitações

Vantagens: políticas de mastery threshold e de dificuldade alvo são simples de implementar, atualizam-se online e não exigem resolver um POMDP geral [F: pelanekrihak2017mastery] [F: pelanek2016elo]; a formulação como MDP/POMDP generaliza essas políticas e permite, em princípio, otimizar diretamente qualquer função de recompensa declarada [F: doroudi2019reward].

Limitações: a escolha do limiar de mastery envolve uma troca entre esforço e desempenho que precisa ser calibrada por domínio e por dificuldade do componente, não há um valor universalmente correto [F: pelanekrihak2017mastery]; planejamento exato em POMDPs é intratável em geral, forçando aproximações (modelos restritos, planejamento míope) cujas garantias de otimalidade são limitadas [F: doroudi2019reward]; a maior fragilidade conceitual é a especificação da recompensa, que frequentemente fica implícita ou mal justificada [F: doroudi2019reward].

## Alternativas e comparações

| Política | O que otimiza | Precisa de função de recompensa explícita? | Granularidade da decisão |
|---|---|---|---|
| Mastery threshold | parar quando estimativa ≥ T | não (implícita) | por componente de conhecimento |
| Dificuldade alvo / Elo | taxa de sucesso esperada ≈ alvo | não (implícita) | por item, a cada resposta |
| MDP/POMDP com planejamento míope | recompensa esperada de curto prazo | sim | por ação/passo |
| MDP/POMDP com planejamento de longo horizonte | recompensa esperada acumulada | sim | por ação/passo, com antecipação |

Fonte da tabela: síntese do autor a partir de [F: pelanekrihak2017mastery], [F: pelanek2016elo] e [F: doroudi2019reward].

## Métricas e métodos de avaliação

Para critério de mastery, Pelánek e Řihák propõem **gráficos de esforço-resultado** (*effort-score graphs*): o eixo de esforço mede o número de tentativas até a decisão de mastery, o eixo de resultado mede o desempenho (real ou simulado) após essa decisão; o limiar recomendado é aquele em que a curva começa a estabilizar, ou seja, onde esforço adicional deixa de melhorar o resultado [F: pelanekrihak2017mastery]. Os autores alertam que a prática comum de avaliar modelos de aluno apenas por métricas de acurácia preditiva (RMSE, AUC — ver `adp.eval.predictive-metrics`) não mede o impacto real sobre a decisão de mastery, que é uma construção latente não diretamente observável [F: pelanekrihak2017mastery].

Para políticas de sequenciamento formuladas como MDP/POMDP, Doroudi, Aleven e Brunskill revisaram toda a pesquisa empírica que compara políticas induzidas por RL a linhas de base, usando como desfecho tipicamente desempenho em pós-teste ou tempo até mastery [F: doroudi2019reward]. Das 36 comparações qualificadas, 21 encontraram ao menos uma política induzida por RL significativamente melhor que todas as linhas de base testadas, 4 mostraram interação aptidão-tratamento favorável a alunos de baixo desempenho sem diferença geral, 4 tiveram resultado misto, 10 não encontraram diferença significativa, e 1 encontrou a linha de base melhor — ou seja, pouco mais da metade dos estudos mostrou vantagem clara do sequenciamento adaptativo sobre o fixo, e os efeitos significativos costumam ter tamanho grande (d de Cohen ≥ 0,8) [F: doroudi2019reward]. Os autores agruparam os estudos em cinco clusters por tipo de ação instrucional (aprendizagem de pares associados, aprendizagem de conceitos, conteúdo interdependente, tipos de atividade, e objetivos fora de aprendizagem) e encontraram sucesso muito desigual entre eles: o cluster de pares associados teve a maior proporção de resultados significativos, enquanto o cluster de sequenciamento de conteúdo interdependente teve a menor [F: doroudi2019reward]. A conclusão central da revisão é que RL foi mais bem-sucedido quando restringido por teorias da psicologia cognitiva e das ciências da aprendizagem, combinando abordagens dirigidas por teoria com abordagens dirigidas por dados, em vez de depender só de algoritmos de dados sem estrutura [F: doroudi2019reward].

## Exemplo técnico independente de domínio

Combinação de critério de mastery, seleção por dificuldade alvo e planejamento míope, no mesmo laço de decisão:

```
para cada componente k: L[k] = estimativa_inicial(k)        # ex.: BKT
para cada aluno: theta = habilidade_inicial                  # ex.: Elo

escolher_proxima_acao(componentes_pendentes, itens, theta, alvo_sucesso=0.75):
    # 1. remover componentes ja em mastery
    pendentes = [k for k in componentes_pendentes if L[k] < limiar_mastery]
    se pendentes vazio: retornar FIM_DA_SECAO

    # 2. entre os itens dos componentes pendentes, escolher por dificuldade alvo
    candidatos = itens cujos componentes estao em pendentes
    melhor = argmin_{i em candidatos} | P(correto | theta, dificuldade_i) - alvo_sucesso |

    # 3. (opcional) desempate por recompensa esperada de curto prazo (planejamento miope)
    se houver empate: melhor = argmax recompensa_esperada_proximo_passo(melhor_candidatos)
    retornar melhor

apos observar resposta (k, correta?):
    L[k] = atualizar_bkt(L[k], correta?)
    theta, dificuldade_i = atualizar_elo(theta, dificuldade_i, correta?)
```

O critério de mastery (`limiar_mastery`, tipicamente 0,95) e a taxa de sucesso alvo (tipicamente 0,75) são hiperparâmetros calibráveis por domínio, não constantes universais [F: pelanekrihak2017mastery] [F: pelanek2016elo].

## Relações com outros conceitos

É parte de `adp.adapt.adaptive-learning-systems`, que descreve o laço externo em termos gerais; este documento aprofunda as políticas que o laço externo executa quando o desenho é mastery learning ou macroadaptação. Depende de `adp.kt.bayesian-knowledge-tracing` e de `adp.irt.elo-rating` como fontes da estimativa de estado que as políticas consomem. É avaliado pelos protocolos de `adp.eval.predictive-metrics` (para a qualidade do modelo subjacente) e `adp.eval.evaluation-protocols` (para a validação da política em si, incluindo estudos com grupo de controle). Relaciona-se com `adp.kt.logistic-models`, outra família de modelo de estado que pode alimentar a mesma camada de decisão.

## Lacunas e questões abertas

- Não foi possível abrir o capítulo de Aleven, McLaughlin, Glenn e Koedinger (2017) sobre tecnologias de aprendizagem adaptativa (paywall), que é citado na literatura como referência central para a "Adaptivity Grid"; não citado como [F].
- A revisão de Doroudi, Aleven e Brunskill cobre estudos até dezembro de 2018 (busca por citação direta e reversa no Google Scholar); políticas de RL profundo mais recentes, mencionadas pelos próprios autores como tendência emergente, não são cobertas em detalhe por eles e não foram verificadas aqui [F: doroudi2019reward].
- Pelánek e Řihák concentram sua análise em componentes de conhecimento isolados, sem considerar relações de pré-requisito entre componentes; o problema de sequenciar múltiplos componentes interdependentes é tratado de forma independente por essa fonte [F: pelanekrihak2017mastery].
- Bloom (1968) é citado apenas por metadados (registro ERIC); a formulação original de mastery learning como pedagogia, fora do contexto computacional, não foi lida em texto completo nesta sessão [F: bloom1968mastery, metadados].
- Não localizamos, nas fontes abertas nesta sessão, uma métrica consolidada de "quanto" o sequenciamento adaptativo supera o fixo além da contagem de significância estatística de Doroudi et al.; uma metanálise com tamanhos de efeito agregados não foi encontrada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| vanlehn2006behavior | academico | 2026-10-29 |
| corbett1995kt | academico | 2026-10-29 |
| pelanekrihak2017mastery | academico | 2026-10-29 |
| pelanek2016elo | academico | 2026-10-29 |
| doroudi2019reward | academico | 2026-10-29 |
| bloom1968mastery | academico (apenas metadados) | 2026-10-29 |
