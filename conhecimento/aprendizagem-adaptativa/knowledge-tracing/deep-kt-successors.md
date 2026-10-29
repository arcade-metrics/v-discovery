---
id: adp.kt.deep-kt-successors
titulo: Sucessores do DKT baseados em memória e atenção (DKVMN, SAKT, AKT)
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [zhang2017dkvmn, pandey2019sakt, ghosh2020akt, abdelrahman2023ktsurvey, shen2024ktsurvey, liu2022pykt, gervet2020deepkt]
relacoes:
  - { tipo: alternativa-a, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: alternativa-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: alternativa-a, alvo: adp.kt.logistic-models }
  - { tipo: depende-de, alvo: adp.id.knowledge-components }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: relacionado-a, alvo: adp.kt.comparison }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: avaliado-por, alvo: adp.eval.evaluation-protocols }
termos: [memory-augmented knowledge tracing, attention-based knowledge tracing, monotonic attention, key-value memory, Rasch embedding, label leakage, AUC]
---

# Sucessores do DKT baseados em memória e atenção (DKVMN, SAKT, AKT)

## Definição e terminologia

Família de modelos de knowledge tracing profundo que substitui o estado oculto recorrente do DKT por uma memória externa endereçável (DKVMN) ou por mecanismos de atenção (SAKT, AKT). O survey de Abdelrahman, Wang e Nunes organiza os modelos profundos de KT em seis grupos: modelagem de sequência (DKT, DKT+), aumentados por memória (DKVMN, SKVMN), baseados em atenção (SAKT, AKT, SAINT, RKT), baseados em grafos (GKT, GIKT, SKT), cientes de texto (EERNN, EKT) e cientes de esquecimento (DKT+forget, HawkesKT) [F: abdelrahman2023ktsurvey]. Este documento cobre os dois grupos do meio; grafos e esquecimento ficam fora do escopo. O que não é: nenhum desses modelos é um método de avaliação estática de habilidade (ver `adp.irt.item-response-theory`); todos preveem a correção da próxima resposta a partir da sequência de interações.

## Problema que resolve

Cada sucessor ataca uma limitação declarada do DKT. O DKVMN parte de que o DKT resume todo o conhecimento do aluno em um único vetor oculto, o que dificulta rastrear o domínio de um conceito específico e apontar pontos fortes e fracos [F: zhang2017dkvmn]. O SAKT parte de que modelos recorrentes (DKT, DKVMN) comprimem a história em um estado-resumo e generalizam mal quando os dados são esparsos — poucos registros por aluno ou por item [F: pandey2019sakt]. O AKT parte de que os modelos profundos preveem bem mas são pouco interpretáveis, o que limita o uso em personalização, e propõe acoplar componentes inspirados em modelos psicométricos e cognitivos [F: ghosh2020akt].

## Fundamentos e funcionamento

### DKVMN (Zhang et al., WWW 2017)

Mantém uma matriz-chave estática, que representa conceitos latentes, e uma matriz-valor dinâmica, que guarda o nível de domínio de cada conceito. O embedding do exercício é comparado com cada slot da matriz-chave (produto interno + softmax), produzindo um peso de correlação que indica quais conceitos o exercício envolve. A leitura soma os slots de valor ponderados pelo peso e produz a probabilidade de acerto; a escrita atualiza os slots com um vetor de apagamento e um vetor de adição derivados do par (exercício, resposta) [F: zhang2017dkvmn]. Os autores relatam AUC superior ao DKT nos quatro conjuntos testados (por exemplo, 82,7 contra 80,3 em Synthetic-5 e 82,8 contra 80,2 em Statics2011), com menos parâmetros e menos sobreajuste, e mostram que atribuir cada exercício ao conceito de maior peso recupera agrupamentos de conceitos sem anotação humana [F: zhang2017dkvmn]. O próprio artigo avisa que seus números de BKT vêm de trabalhos anteriores com pré-processamento diferente e não são diretamente comparáveis [F: zhang2017dkvmn].

### SAKT (Pandey e Karypis, EDM 2019)

Primeiro modelo de KT com autoatenção [F: abdelrahman2023ktsurvey]. O exercício a prever é a query; as interações passadas (exercício, correção), com embedding posicional, são chaves e valores de uma atenção escalada com máscara causal, seguida de rede feed-forward; um único bloco de atenção basta (a ablação com 0 e 2 blocos não melhora) [F: pandey2019sakt]. Os autores relatam AUC média de 0,824 contra 0,786 do DKT (ganho médio de 4,43%), com o maior ganho no conjunto mais esparso (ASSIST2015: 0,854 contra 0,736) e empate no mais denso, além de treino cerca de 30 vezes mais rápido por época que o DKT por ser paralelizável [F: pandey2019sakt]. Esses números foram contestados por replicações independentes (ver seção de avaliação).

### AKT (Ghosh, Heffernan e Lan, KDD 2020)

Combina atenção com dois componentes interpretáveis. Primeiro, atenção monotônica: cada escore de atenção é multiplicado por exp(−θ·d(t,τ)), onde θ é uma taxa de decaimento aprendida por cabeça e d(t,τ) é uma distância temporal ciente de contexto que penaliza menos a prática antiga relacionada ao conceito atual [F: ghosh2020akt]. Segundo, embeddings regularizados pelo modelo de Rasch: o embedding da questão é x = c + μ·d, com c o embedding do conceito, d um vetor de variação e μ um escalar de dificuldade, capturando diferenças entre questões do mesmo conceito com cerca de 2CD+Q parâmetros em vez de QD [F: ghosh2020akt] (ver `adp.irt.item-response-theory`). Nos experimentos dos autores o AKT supera DKT, DKVMN e SAKT em quatro conjuntos (por exemplo, 0,7828 contra 0,7313 do DKT em ASSISTments2015), com ganho de até 6% de AUC, e — ponto notável — o DKT supera o SAKT em todos os conjuntos, contradizendo o artigo original do SAKT [F: ghosh2020akt]. Estudos de caso qualitativos sugerem que cabeças de atenção operam em escalas temporais distintas e que os μ aprendidos ordenam questões por dificuldade de forma intuitiva; os autores apresentam isso como potencial, não como benefício comprovado [F: ghosh2020akt].

## Requisitos e pressupostos

- Dados sequenciais de interação em volume suficiente; o próprio artigo do SAKT motiva a atenção pela esparsidade, mas replicações sugerem que os conjuntos educacionais típicos são pequenos demais para a autoatenção render (ver abaixo) [F: gervet2020deepkt].
- Mapeamento questão–conceito (knowledge components): os embeddings de Rasch do AKT exigem identificadores de questão, disponíveis só em parte dos conjuntos [F: ghosh2020akt]; em ASSISTments2012, a maioria das questões não tem anotação de KC, o que o survey associa a desempenho menor [F: abdelrahman2023ktsurvey]. Ver `adp.id.knowledge-components`.
- Protocolo de avaliação padronizado; sem isso os resultados não são comparáveis (ver seção seguinte).

## Métricas, benchmarks independentes e o problema do pré-processamento

A métrica dominante é AUC [F: abdelrahman2023ktsurvey]. Dois benchmarks independentes reavaliaram a família com protocolo único e chegaram a conclusões bem menos favoráveis que os artigos originais:

- Gervet et al. compararam regressão logística, BKT+, DKT e SAKT em nove conjuntos reais: o SAKT ficou abaixo do DKT em todos; em ASSISTments2015 os autores originais relataram AUC 0,85 e a replicação observou 0,73, e um número de baseline do artigo original (0,82) "não pôde ser reproduzido e parece impossível" [F: gervet2020deepkt]. A hipótese dos autores é que os conjuntos educacionais são pequenos demais para autoatenção [F: gervet2020deepkt].
- O pyKT (NeurIPS 2022 Datasets and Benchmarks) padronizou pré-processamento e avaliação de 10 modelos em 7 conjuntos e documentou duas fontes de inflação: (1) pré-processamento privado e não descrito — o AUC relatado do DKT em ASSISTments2009 varia de 0,73 a 0,821 entre artigos; (2) vazamento de rótulo na avaliação "one-by-one" de sequências expandidas por KC, em que o modelo vê respostas verdadeiras de KCs da mesma questão [F: liu2022pykt]. Com protocolo corrigido: o AKT foi o melhor em quase todos os 7 conjuntos (por exemplo, 0,7853 contra 0,7541 do DKT em AS2009); o DKVMN ficou abaixo do DKT nos 7; o SAKT ficou abaixo do DKT em 6 de 7; e os resultados originais do ATKT não foram reproduzíveis após corrigir um vazamento de rótulo futuro [F: liu2022pykt]. A conclusão textual: "a maioria das abordagens DLKT propostas recentemente não consegue vencer o DKT original" [F: liu2022pykt].
- O survey de Abdelrahman et al. reforça: a versão original do ASSISTments2009 é considerada não confiável (duplicatas inflam resultados) e resultados obtidos com versões ou pré-processamentos diferentes não devem ser comparados [F: abdelrahman2023ktsurvey].

[I] Síntese: da família, só o AKT tem ganho que sobrevive a benchmark independente, e ainda assim na ordem de 0,01–0,03 de AUC, não dos 4–6% dos artigos originais; o custo em dados, computação e opacidade deve ser pesado contra isso (ver `adp.kt.comparison` e `adp.eval.predictive-metrics`).

## Vantagens e limitações

Vantagens: DKVMN dá leitura por conceito do estado de conhecimento, que o DKT não dá [F: zhang2017dkvmn]; atenção expõe quais interações passadas pesaram na previsão, com potencial interpretativo [F: ghosh2020akt]; AKT liga dificuldade de item a um parâmetro escalar herdado da psicometria [F: ghosh2020akt]; treino paralelizável [F: pandey2019sakt].

Limitações: ganhos preditivos pequenos ou inexistentes sobre o DKT em avaliação padronizada [F: liu2022pykt] [F: gervet2020deepkt]; sensibilidade a pré-processamento e a vazamento de dados nas comparações publicadas [F: liu2022pykt]; interpretabilidade demonstrada só por estudos de caso qualitativos [F: ghosh2020akt]; nenhum dos artigos mede efeito pedagógico, apenas previsão [I].

## Alternativas e comparações

| Modelo | Mecanismo central | Resultado no artigo original | Em benchmark independente (pyKT, 7 conjuntos) |
|---|---|---|---|
| DKVMN | memória chave-valor por conceito [F: zhang2017dkvmn] | supera DKT nos 4 conjuntos [F: zhang2017dkvmn] | abaixo do DKT nos 7 [F: liu2022pykt] |
| SAKT | autoatenção, 1 bloco [F: pandey2019sakt] | +4,43% AUC médio sobre o estado da arte [F: pandey2019sakt] | abaixo do DKT em 6 de 7 [F: liu2022pykt] |
| AKT | atenção monotônica + embeddings de Rasch [F: ghosh2020akt] | até +6% AUC [F: ghosh2020akt] | melhor em quase todos os 7 [F: liu2022pykt] |
| DKT (referência) | RNN com estado único | — | competitivo; maioria dos sucessores não o vence [F: liu2022pykt] |

Alternativas fora da família profunda: regressão logística com boas features vence em conjuntos de tamanho moderado e BKT fica atrás de ambas (ver `adp.kt.logistic-models`, `adp.kt.bayesian-knowledge-tracing`) [F: gervet2020deepkt].

## Exemplo técnico independente de domínio

Esqueleto comum dos modelos atencionais de KT (notação simplificada do SAKT/AKT):

```
prever(exercicio e_t1, historico [(e_1,r_1)...(e_t,r_t)]):
    q = embed_exercicio(e_t1)                      # query
    para i em 1..t:
        k_i = embed_interacao(e_i, r_i) + pos(i)   # chave e valor
        s_i = (q . k_i) / sqrt(d)
        # so no AKT: s_i *= exp(-theta * dist_contextual(t1, i))
    w = softmax(mascara_causal(s))
    contexto = soma_i w_i * v_i
    retornar sigmoide(ffn(contexto, q))            # P(resposta correta)
```

Dimensionamentos de referência do SAKT: 1 bloco de atenção, dimensão oculta buscada em {50..200}, sequências truncadas/particionadas em 50–500 interações conforme o conjunto [F: pandey2019sakt].

## Relações com outros conceitos

Alternativas ao `adp.kt.deep-knowledge-tracing` (que estendem), ao `adp.kt.bayesian-knowledge-tracing` e aos `adp.kt.logistic-models`; a comparação sistemática entre famílias fica em `adp.kt.comparison`. O embedding de Rasch do AKT importa o modelo 1PL de `adp.irt.item-response-theory`. A avaliação depende de `adp.eval.predictive-metrics` e dos protocolos de `adp.eval.evaluation-protocols`, onde o vazamento de rótulo documentado pelo pyKT deve ser tratado em detalhe.

## Lacunas e questões abertas

- O DOI das versões de conferência (WWW 2017, KDD 2020, EDM 2019) não foi verificado; as leituras foram feitas nas versões arXiv. A página do arXiv do SAKT indica a conferência EDM sem ano explícito.
- O survey de Shen et al. (IEEE TLT 2024, arXiv 2105.15106) teve apenas o abstract aberto; dele consta a existência das bibliotecas EduData e EduKTM e uma taxonomia de três tipos de modelos fundamentais [F: shen2024ktsurvey]; o corpo não foi lido.
- SAINT, SAINT+, RKT e os modelos de grafos não foram cobertos aqui; o pyKT inclui alguns deles e o quadro geral não muda [F: liu2022pykt].
- Nenhuma fonte aberta encontrada mede impacto desses modelos em resultado de aprendizagem (não só previsão); lacuna para `adp.eval.educational-effectiveness`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| zhang2017dkvmn | academico | 2026-10-29 |
| pandey2019sakt | academico | 2026-10-29 |
| ghosh2020akt | academico | 2026-10-29 |
| abdelrahman2023ktsurvey | academico | 2026-10-29 |
| shen2024ktsurvey | academico (abstract) | 2026-10-29 |
| liu2022pykt | academico | 2026-10-29 |
| gervet2020deepkt | academico | 2026-10-29 |
