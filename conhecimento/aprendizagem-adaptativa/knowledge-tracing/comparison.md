---
id: adp.kt.comparison
titulo: Comparação entre famílias de knowledge tracing (BKT, logísticos, DKT, sucessores profundos)
tipo: comparacao
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gervet2020when, khajah2016howdeep, xiong2016going, pelanek2017overview, pavlik2009pfa, corbett1995kt, yeung2018dktplus]
relacoes:
  - { tipo: parte-de, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.kt.logistic-models }
  - { tipo: relacionado-a, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.kt.deep-kt-successors }
  - { tipo: relacionado-a, alvo: adp.lm.open-learner-model }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: avaliado-por, alvo: adp.eval.evaluation-protocols }
termos: [dataset size, generalização, calibração, mastery decision, open learner model, ablation study]
---

# Comparação entre famílias de knowledge tracing

## Definição e terminologia

Este documento compara quatro famílias de modelos de estimação de estado do aluno a partir de sequências de respostas: processos de Markov (Bayesian Knowledge Tracing, BKT), modelos logísticos (AFM/PFA, ver `adp.kt.logistic-models`), aprendizado profundo recorrente (Deep Knowledge Tracing, DKT) e seus sucessores com mecanismos de atenção e regularização (`adp.kt.deep-kt-successors`). A comparação segue a metodologia de Gervet et al., que avaliou as três primeiras famílias (mais BKT+, a melhor variante estendida de BKT) em nove datasets reais de sistemas tutores [F: gervet2020when].

O que este documento não faz: não declara uma família "melhor" em absoluto. Pelánek argumenta que a escolha depende do contexto de uso — tipo de componente de conhecimento, dados disponíveis, propósito do modelo (predição, modelo aberto ao aluno, insight acionável) [F: pelanek2017overview].

## Problema que resolve

Orientar a escolha de família de modelo para uma aplicação concreta, evitando duas falhas comuns na literatura: comparar um modelo novo contra uma linha de base fraca (BKT clássico sem extensões, PFA sem features) [F: khajah2016howdeep] [F: gervet2020when], ou usar dados de benchmark com defeitos que inflam artificialmente um modelo sobre outro [F: xiong2016going].

## Dados exigidos por família

| Família | Exige rótulo de KC por item | Sensível a timestamps | Volume mínimo de dados | Observação |
|---|---|---|---|---|
| BKT (clássico) | sim, 1 KC por item [F: pelanek2017overview] | não | baixo (4 parâmetros por KC) [F: gervet2020when] | modelo independente por KC [F: gervet2020when] |
| BKT+ (individualização + esquecimento + descoberta de KC) | pode descobrir KCs [F: khajah2016howdeep] | parcialmente (esquecimento) [F: khajah2016howdeep] | moderado | ajuste por MCMC, ordens de magnitude mais lento [F: gervet2020when] |
| Logístico (PFA, AFM, Best-LR) | sim, aceita múltiplos KCs por item [F: pavlik2009pfa] | com features de janela (DAS3H) [F: gervet2020when] | moderado a grande | regressão logística padrão, rápida [F: pavlik2009pfa] |
| DKT | não estritamente, mas desempenho ótimo depende do modelo de KC [F: gervet2020when] | sim, ordem exata da sequência [F: gervet2020when] | grande (aprendizes por item/KC) [F: gervet2020when] | ~250 mil parâmetros com 200 unidades LSTM e 50 KCs [F: khajah2016howdeep] |
| Sucessores com atenção (ex. SAKT) | variável | sim | grande | ver `adp.kt.deep-kt-successors` para detalhes de arquitetura |

## Interpretabilidade dos parâmetros

BKT tem quatro parâmetros por KC com significado psicológico direto (probabilidade inicial, taxa de aprendizagem, slip, guess), mas sofre de identifiability na forma agregada — múltiplas combinações de guess e conhecimento inicial geram a mesma predição média [F: pelanek2017overview] (detalhe em `adp.kt.bayesian-knowledge-tracing`). Os modelos logísticos também têm parâmetros interpretáveis (facilidade do KC, ganho por sucesso/fracasso) e ajuste convexo determinístico, vantagem sobre o ajuste do BKT, que pode cair em ótimo local [F: xiong2016going]. O DKT é, nas palavras de Khajah et al., "massive neural network model with tens of thousands of parameters which are near-impossible to interpret" [F: khajah2016howdeep]; além disso, sem regularização adicional suas predições podem ser internamente inconsistentes — a estimativa de uma habilidade pode cair após um acerto na própria habilidade [F: yeung2018dktplus].

## Desempenho preditivo publicado

A comparação mais extensa e controlada é a de Gervet et al. em nove datasets (AUC, melhor hiperparâmetro por busca em grade) [F: gervet2020when]:

- Logistic regression com o melhor conjunto de features (Best-LR) lidera em 4 de 9 datasets: algebra05, bridge06, assistments09 e spanish — os de menor número de aprendizes por item/KC, ou com milhares de interações por aluno [F: gervet2020when].
- DKT lidera nos 5 restantes: assistments12, assistments17, statics, squirrel e assistments15 — datasets maiores ou com progressão fortemente sequencial pelo material [F: gervet2020when].
- "Markov process methods, like Bayesian Knowledge Tracing, lag behind other approaches" — BKT clássico não é competitivo na escala considerada; BKT+ (a extensão mais completa) chega perto do Best-LR mas é ordens de magnitude mais lento para treinar (dias, contra menos de dois minutos para regressão logística ou DKT) [F: gervet2020when].
- Em datasets pequenos (poucos aprendizes por item), DKT sobreajusta; em datasets muito grandes, DKT supera a regressão logística porque consegue modelar relações não lineares entre histórico e log-odds de acerto [F: gervet2020when].
- DKT explora melhor a ordem temporal exata quando os alunos progridem sequencialmente pelo material (assistments17, statics), mas falha em reter informação de longo prazo quando há milhares de interações por aluno (spanish, bridge06) — nesses casos a regressão logística com contagens históricas o supera [F: gervet2020when].
- Nos estudos de ablação, as features de janela temporal introduzidas no DAS3H não acrescentam poder preditivo a um modelo logístico linear, mas ajudam uma rede não linear (feedforward) — evidência de relação não linear entre histórico e log-odds em datasets sequenciais [F: gervet2020when].
- O modelo de KC desenhado por especialistas acrescenta pouco poder preditivo na maioria dos datasets (ganho ≤ 0,01 AUC em 7 de 9), exceto nos dois datasets do KDD Cup 2010 [F: gervet2020when].

Resultados anteriores e isolados, já situados pela comparação acima: Piech et al. reportaram ganho de 25% de AUC do DKT sobre BKT no ASSISTments (0,86 vs 0,67) [F: piech2015dkt, citado também em khajah2016howdeep]; Khajah et al. mostraram que boa parte desse ganho (82%, somando viés de métrica e falta de esquecimento no BKT) desaparece com um BKT estendido (BKT+FSA average ≈ DKT nos 4 datasets testados) [F: khajah2016howdeep]; Xiong et al. mostraram que, em dados do ASSISTments devidamente limpos (sem duplicação, sem scaffolding, sem repetição de sequência por KC), o DKT não supera o PFA de forma consistente (AUC 0,73-0,75 vs 0,73 no dataset 09-10(c); 0,70 vs 0,69 no dataset 2014-15), mantendo vantagem clara apenas no KDD Cup (0,79 vs 0,71) [F: xiong2016going]. Pavlik, Cen e Koedinger já haviam mostrado, antes do DKT, que o PFA supera o BKT clássico em quatro datasets de tutores reais (A′ de 0,685 a 0,723 contra 0,660 a 0,719 do BKT) [F: pavlik2009pfa].

## Custo de treino

Ordenação aproximada, do mais rápido ao mais lento, segundo Gervet et al.: regressão logística e DKT treinam em menos de dois minutos nos datasets considerados; BKT (EM ou busca em grade) é rápido por KC mas escala linearmente com o número de KCs; BKT+ (com descoberta de KC e MCMC) leva dias nos datasets grandes, a ponto de os autores não conseguirem completar o treino em alguns deles ("Too slow") [F: gervet2020when]. Khajah et al. relatam tempos de execução de minutos a dezenas de minutos para suas variantes de BKT estendido em datasets de até algumas centenas de milhares de interações [F: khajah2016howdeep].

## Utilidade pedagógica

Pelánek distingue três usos de um modelo de aluno — política instrucional automática, modelo de aluno aberto (open learner model) e insight acionável para humanos — e observa que eles pesam de modo diferente a acurácia e a interpretabilidade [F: pelanek2017overview]. Para decisões de mastery (critério "95% de probabilidade de domínio"), o requisito central é uma estimativa de probabilidade bem calibrada por componente de conhecimento, propriedade nativa do BKT e dos modelos logísticos por construção [F: corbett1995kt] [F: pelanek2017overview]. Gervet et al. mostram que mesmo os melhores modelos (Best-LR e DKT) apresentam viés sistemático de calibração fora do intervalo de maior densidade de dados em vários datasets — o que compromete o uso direto das probabilidades em políticas adaptativas ou em modelos abertos ao aluno, qualquer que seja a família [F: gervet2020when]. Para um open learner model, Pelánek observa que um comportamento intuitivo (acerto aumenta a estimativa de domínio, erro diminui) é esperado pelos usuários, mas nem todo modelo complexo garante isso — propriedade que falha no DKT sem regularização de consistência [F: pelanek2017overview] [F: yeung2018dktplus]. Para insight acionável (ex. redesenho de currículo, avaliação de dificuldade de itens), a estabilidade dos parâmetros entre reamostragens importa mais que pequenos ganhos de acurácia — um argumento a favor de BKT e modelos logísticos sobre DKT nesse uso específico [F: pelanek2017overview].

## Alternativas e comparações

Síntese das condições em que cada família se justifica, com base nas fontes acima:

| Condição | Família recomendada pelas evidências |
|---|---|
| Poucos aprendizes por item/KC, dataset pequeno a moderado | Regressão logística com boas features (Best-LR) [F: gervet2020when] |
| Milhares de interações por aluno (ex. línguas, prática massiva) | Regressão logística (contagens históricas); DKT perde desempenho por não reter longo prazo [F: gervet2020when] |
| Dataset muito grande, progressão fortemente sequencial pelo material | DKT [F: gervet2020when] |
| Necessidade de decisão de mastery transparente e auditável | BKT ou modelos logísticos (parâmetros interpretáveis, probabilidade calibrada por construção) [F: pelanek2017overview] [F: corbett1995kt] |
| Necessidade de open learner model com comportamento intuitivo garantido | BKT ou modelos logísticos; DKT exige regularização adicional (DKT+) para não contradizer a entrada observada [F: yeung2018dktplus] |
| Insight acionável sobre o domínio (redesenho de currículo, dificuldade de item) | BKT ou logísticos, pela estabilidade e interpretabilidade dos parâmetros [F: pelanek2017overview] |
| Múltiplos KCs por item, sem descoberta automática de estrutura | Modelos logísticos (compensatórios por soma) [F: pavlik2009pfa]; BKT clássico não lida nativamente com isso [F: pelanek2017overview] |
| Pesquisa de ponta em datasets muito grandes, tolerância a caixa-preta | DKT e sucessores (`adp.kt.deep-kt-successors`), com cautela de calibração [F: gervet2020when] |

## Exemplo técnico independente de domínio

```
escolher_familia(dataset, uso_pretendido):
    se uso_pretendido == "mastery_decision" ou "open_learner_model":
        preferir BKT ou logístico (probabilidade interpretável e calibrada)
    senao se uso_pretendido == "insight_acionavel":
        preferir BKT ou logístico (estabilidade de parâmetros)
    senao:  # uso_pretendido == "predicao_pura"
        se aprendizes_por_item(dataset) < limiar_pequeno:
            usar logístico (Best-LR)
        senao se interacoes_por_aluno(dataset) > limiar_muito_longo:
            usar logístico (DKT perde informação de longo prazo)
        senao:
            comparar DKT vs Best-LR por validação cruzada; relatar AUC e RMSE, não só AUC
    sempre: verificar calibração (reliability diagram) antes de uso em política adaptativa
```

## Relações com outros conceitos

Este documento sintetiza `adp.kt.bayesian-knowledge-tracing`, `adp.kt.logistic-models` e `adp.kt.deep-knowledge-tracing`, e remete a `adp.kt.deep-kt-successors` para arquiteturas mais recentes. A discussão de utilidade pedagógica se conecta a `adp.lm.open-learner-model`. Os protocolos e métricas citados (AUC, RMSE, calibração, validação cruzada por aprendiz) são detalhados em `adp.eval.predictive-metrics` e `adp.eval.evaluation-protocols`.

## Lacunas e questões abertas

- Gervet et al. não incluem BKT clássico (sem extensão) nos nove datasets por ser não competitivo na escala considerada; os números de BKT puro vêm de fontes anteriores (Piech et al., Xiong et al.), nem sempre com a mesma metodologia de validação cruzada — comparação direta deve ser lida com cautela [F: gervet2020when].
- Não encontramos comparação publicada que isole custo total de propriedade (treino + manutenção + explicabilidade para professores) de forma quantitativa; a ordenação de custo de treino acima é qualitativa.
- A relação entre calibração e decisões de mastery no mundo real (não apenas AUC/RMSE) carece de estudo controlado nas fontes revisadas; Gervet et al. apontam o problema mas não testam o impacto em uma política real [F: gervet2020when].
- Pelánek nota que a importância da interpretabilidade e da escolha de família muda com a granularidade do componente de conhecimento; não há regra quantitativa para essa fronteira, apenas heurísticas do framework KLI [F: pelanek2017overview].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gervet2020when | academico | 2026-10-29 |
| khajah2016howdeep | academico | 2026-10-29 |
| xiong2016going | academico | 2026-10-29 |
| pelanek2017overview | academico | 2026-10-29 |
| pavlik2009pfa | academico | 2026-10-29 |
| corbett1995kt | academico | 2026-10-29 |
| yeung2018dktplus | academico | 2026-10-29 |
