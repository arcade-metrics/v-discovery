---
id: adp.kt.deep-knowledge-tracing
titulo: Deep Knowledge Tracing (DKT)
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [piech2015dkt, khajah2016howdeep, xiong2016going, yeung2018dktplus, gervet2020when, pelanek2017overview]
relacoes:
  - { tipo: alternativa-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: alternativa-a, alvo: adp.kt.logistic-models }
  - { tipo: relacionado-a, alvo: adp.kt.deep-kt-successors }
  - { tipo: depende-de, alvo: adp.id.knowledge-components }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: avaliado-por, alvo: adp.eval.evaluation-protocols }
  - { tipo: relacionado-a, alvo: adp.kt.comparison }
termos: [deep knowledge tracing, RNN, LSTM, one-hot encoding, AUC, recency effect, skill discovery, reconstruction problem, waviness, prediction-consistent regularization]
---

# Deep Knowledge Tracing (DKT)

## Definição e terminologia

Deep Knowledge Tracing (DKT) é a aplicação de redes neurais recorrentes (RNN), "profundas no tempo", à tarefa de knowledge tracing: dado o histórico de interações x1…xt de um aluno, prever aspectos da interação xt+1, tipicamente a probabilidade de acerto da próxima questão [F: piech2015dkt]. O estado latente de conhecimento é um vetor contínuo de alta dimensão aprendido dos dados, em vez de uma variável binária por habilidade como no BKT [F: piech2015dkt]. Os autores usam duas variantes: RNN simples (sigmoide) e LSTM [F: piech2015dkt].

O que não é: DKT não é um modelo interpretável por parâmetro — com 200 unidades ocultas LSTM e 50 habilidades, tem cerca de 250.000 parâmetros livres, contra 200 do BKT para as mesmas 50 habilidades [F: khajah2016howdeep]. Também não é, apesar da divulgação original, independente de estrutura de domínio: a representação de entrada/saída por knowledge components afeta fortemente o desempenho [F: gervet2020when].

## Problema que resolve

Capturar regularidades que os modelos estruturados por habilidade não capturam: a entrada é a sequência completa de pares (exercício, acerto) na ordem real, de modo que o modelo pode explorar ordem temporal exata, similaridade entre habilidades e variação individual, e pode operar sem anotação de conceitos por especialistas [F: piech2015dkt] [F: khajah2016howdeep].

## Fundamentos e funcionamento

### Arquitetura e entrada/saída

Equações da RNN simples [F: piech2015dkt]:

```
ht = tanh(Whx·xt + Whh·ht-1 + bh)
yt = σ(Wyh·ht + by)
```

A entrada xt é um one-hot da tupla {qt, at} (exercício × correção), logo xt ∈ {0,1}^2M para M exercícios distintos; representações separadas de qt e at pioraram o desempenho [F: piech2015dkt]. Para M grande, os autores usam vetores gaussianos aleatórios de dimensão N ≪ M, justificados por compressed sensing [F: piech2015dkt]. A saída yt tem um componente por exercício: a probabilidade prevista de acerto; a predição de at+1 é lida na entrada correspondente a qt+1 [F: piech2015dkt].

### Treinamento

O objetivo é a log-verossimilhança negativa da sequência observada (entropia cruzada binária sobre a predição do próximo passo), minimizada por gradiente estocástico em minibatches; dropout na leitura de yt; clipping de gradiente; dimensionalidade oculta 200 e minibatch 100 em todos os experimentos [F: piech2015dkt].

### Resultados originais

AUC reportada por Piech et al. [F: piech2015dkt]:

| Dataset | Marginal | BKT | BKT* (melhor da literatura) | DKT (LSTM) |
|---|---|---|---|---|
| Simulated-5 | ? | 0,54 | – | 0,75 |
| Khan Math (1,4M respostas, 69 exercícios) | 0,63 | 0,68 | – | 0,85 |
| ASSISTments 2009-2010 | 0,62 | 0,67 | 0,69 | 0,86 |

Os autores descrevem o resultado no ASSISTments como ganho de 25% de AUC sobre o melhor resultado anterior [F: piech2015dkt]. Aplicações demonstradas: escolha de sequência de exercícios via expectimax (tratando a escolha como MDP) e descoberta de estrutura: um grafo de influência entre exercícios `Jij = y(j|i) / Σk y(j|k)` recupera os clusters de conceitos latentes nos dados sintéticos [F: piech2015dkt].

## Re-análises críticas (obrigatórias para interpretar os números acima)

### Khajah, Lindsey e Mozer 2016: "How Deep is Knowledge Tracing?"

Hipotetizam quatro regularidades que o DKT explora e o BKT clássico não: efeitos de recência, sequência contextualizada de tentativas, similaridade entre habilidades e variação individual de proficiência [F: khajah2016howdeep]. Resultados principais:

- Reavaliando o BKT clássico com procedimento de AUC uniforme, obtêm 0,73 no ASSISTments (não 0,67) e 0,62 no Synthetic (não 0,54); estimam que 31,6% da diferença reportada em Piech et al. vem de procedimento de cálculo de AUC enviesado contra o BKT (AUC por habilidade e depois média, versus AUC global) [F: khajah2016howdeep].
- BKT com esquecimento (BKT+F) atinge 0,83 no ASSISTments — mais 50,6% da diferença desaparece [F: khajah2016howdeep].
- Com extensões já existentes na literatura (esquecimento, descoberta de habilidades, proficiência latente — BKT+FSA), o BKT fica em média indistinguível do DKT nos quatro datasets testados; com rótulos por exercício, BKT+S chega a 0,90 no ASSISTments [F: khajah2016howdeep].
- Conclusão dos autores: o ganho do DKT não vem de descoberta de representações ("knowledge tracing may be a domain that does not require 'depth'"), mas de flexibilidade para capturar regularidades estatísticas; o preço é a interpretabilidade [F: khajah2016howdeep].

### Xiong et al. 2016: problemas nos dados ASSISTments

Reproduzindo o DKT em TensorFlow, encontraram três problemas no benchmark ASSISTments 2009-2010 [F: xiong2016going]:

1. **Registros duplicados**: 123.778 das 525.535 linhas (23,6%) eram duplicações erradas, reconhecidas pela equipe do ASSISTments [F: xiong2016going].
2. **Problemas de scaffolding misturados aos principais** (73.466 linhas), informação que BKT e PFA excluem — vantagem indevida para o DKT [F: xiong2016going].
3. **Sequências repetidas por rótulo de habilidade**: questões multi-habilidade entravam uma vez por habilidade; nos pontos repetidos o DKT chega a AUC 0,97, inflando o resultado global [F: xiong2016going].

Com dados limpos e habilidades conjuntas (09-10 (c)) e no dataset 2014-15, o DKT não supera o PFA (AUC 0,73-0,75 vs 0,73; 0,70 vs 0,69), embora continue claramente acima do BKT; no KDD Cup 2010 o DKT mantém vantagem (0,79 vs 0,71) [F: xiong2016going].

### Yeung e Yeung 2018: inconsistência das predições

Identificam dois problemas de comportamento do DKT: falha de reconstrução da entrada (após um erro em uma habilidade, a probabilidade prevista para essa mesma habilidade pode subir, e vice-versa) e transição ondulada ("wavy") do estado previsto entre passos, indesejável porque o estado de conhecimento deveria mudar gradualmente [F: yeung2018dktplus]. Propõem regularizar a perda com três termos — erro de reconstrução r e medidas de waviness w1 (norma L1) e w2 (norma L2) — formando o DKT+ [F: yeung2018dktplus]. No ASSIST2009, o DKT+ mantém a AUC de predição do próximo passo (0,8212 → 0,8227) e melhora a AUC da interação corrente de 0,9044 para 0,9625, com w1 caindo de 0,0830 para 0,0229 [F: yeung2018dktplus]. A implicação para uso pedagógico: sem a regularização, as estimativas do DKT são pouco confiáveis como representação de conhecimento para um open learner model [I].

### Gervet et al. 2020: quando o DKT vence

Em nove datasets, o DKT lidera nos grandes ou fortemente sequenciais e perde para regressão logística nos moderados ou com milhares de interações por aluno (dificuldade de reter informação de longo prazo); a escolha de entradas/saídas (KCs vs itens) muda a AUC em até ~0,05, mostrando dependência do modelo de domínio [F: gervet2020when]. Detalhes em `adp.kt.comparison`.

## Requisitos e pressupostos

- Grandes volumes de dados: "RNNs require large amounts of training data", adequadas a educação online, não a uma turma pequena [F: piech2015dkt]; em datasets com poucos alunos por item, o DKT sobreajusta [F: gervet2020when].
- Sequências ordenadas de respostas binárias com rótulo de exercício ou habilidade; a qualidade e o formato desse rótulo afetam diretamente o resultado [F: gervet2020when] [F: xiong2016going].
- Infraestrutura de treino (GPU ajuda; treinamento é computacionalmente intensivo, embora o DKT treine em minutos em datasets grandes) [F: khajah2016howdeep] [F: gervet2020when].

## Vantagens e limitações

Vantagens: dispensa anotação de conceitos para prever (pode descobrir estrutura) [F: piech2015dkt]; captura recência, ordem temporal exata e similaridade entre habilidades [F: khajah2016howdeep] [F: gervet2020when]; aceita qualquer entrada vetorizável [F: piech2015dkt]; atinge desempenho de pico com poucas interações por aluno novo [F: gervet2020when].

Limitações: interpretabilidade quase nula dos parâmetros [F: khajah2016howdeep]; predições inconsistentes sem regularização [F: yeung2018dktplus]; sensibilidade a defeitos de dados (duplicações, sequências repetidas) [F: xiong2016going]; dificuldade com sequências muito longas [F: gervet2020when]; os ganhos originais sobre BKT foram substancialmente inflados por procedimento de avaliação e qualidade dos dados [F: khajah2016howdeep] [F: xiong2016going].

## Exemplo técnico independente de domínio

```
# M exercícios; entrada one-hot de dimensão 2M; saída de dimensão M
para cada aluno, para t = 1..T-1:
    x = onehot(q_t + a_t * M)
    h = LSTM(x, h)                      # estado latente de conhecimento
    y = sigmoid(W_out · h + b_out)      # prob. de acerto de cada exercício
    perda += entropia_cruzada(y[q_{t+1}], a_{t+1})
# regularização de consistência (DKT+): perda += λr·r + λw1·w1 + λw2·w2²
```

## Relações com outros conceitos

Alternativa a `adp.kt.bayesian-knowledge-tracing` e a `adp.kt.logistic-models`; a comparação de condições de uso está em `adp.kt.comparison`. Os sucessores com atenção e outras arquiteturas estão em `adp.kt.deep-kt-successors`. Apesar da promessa de independência de anotação, depende na prática de `adp.id.knowledge-components` para desempenho ótimo [F: gervet2020when]. Avaliado por `adp.eval.predictive-metrics` (AUC, RMSE, calibração) sob os protocolos de `adp.eval.evaluation-protocols` — as divergências de AUC entre artigos ilustram por que o protocolo importa [F: khajah2016howdeep].

## Lacunas e questões abertas

- O valor "Marginal" do Simulated-5 não é reportado na tabela original (célula "?") [F: piech2015dkt].
- A página do arXiv de Khajah et al. não nomeia o veículo de publicação; a apresentação na EDM 2016 não foi verificada em fonte aberta.
- Yeung e Yeung 2018: lido na versão arXiv v1; o veículo (Learning at Scale 2018) não foi verificado.
- Permanece sem explicação satisfatória que informação temporal exatamente o DKT explora que um modelo log-linear não consegue, e por que atinge desempenho de pico mais rápido [F: gervet2020when].
- O experimento controlado de currículo com Khan Academy anunciado por Piech et al. como trabalho em andamento não foi rastreado nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| piech2015dkt | academico | 2026-10-29 |
| khajah2016howdeep | academico | 2026-10-29 |
| xiong2016going | academico | 2026-10-29 |
| yeung2018dktplus | academico | 2026-10-29 |
| gervet2020when | academico | 2026-10-29 |
| pelanek2017overview | academico | 2026-10-29 |
