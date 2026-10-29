---
id: adp.sr.half-life-regression
titulo: Half-life regression (HLR)
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [settles2016hlr, duolingo2016hlrcode, ilidio2026hlr, srsbenchmark2026]
relacoes:
  - { tipo: depende-de, alvo: adp.sr.memory-and-forgetting }
  - { tipo: alternativa-a, alvo: adp.sr.classical-algorithms }
  - { tipo: alternativa-a, alvo: adp.sr.fsrs }
  - { tipo: relacionado-a, alvo: adp.kt.logistic-models }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
termos: [half-life regression, half-life, forgetting curve, lag time, recall rate, lexeme tag, learning trace]
---

# Half-life regression (HLR)

## Definição e terminologia

Half-life regression (HLR) é um modelo treinável de repetição espaçada proposto por Settles e Meeder (Duolingo) na ACL 2016. Ele estima indiretamente a *meia-vida* (half-life) de um item na memória de longo prazo do aluno como função log-linear de um vetor de features, e prevê a probabilidade de recordação pela curva de esquecimento exponencial de Ebbinghaus [F: settles2016hlr]. "Item", no artigo, é um *lexeme tag* (lexema com anotação morfológica); cada instância de dado é uma sessão de prática aluno-palavra com taxa de recordação observada `p`, tempo decorrido `Δ` e features `x` [F: settles2016hlr].

O que não é: não é um modelo de sequência — o histórico entra apenas como contadores agregados nas features, não como série temporal; e não é um escalonador completo — o artigo o usa para ordenar itens por fraqueza prevista, não para calcular intervalos ótimos [F: settles2016hlr] [I].

## Problema que resolve

Os algoritmos clássicos (`adp.sr.classical-algorithms`) usam regras fixas; plataformas em larga escala têm milhões de traces que permitem ajustar um modelo estatístico mais rico [F: settles2016hlr]. O problema concreto do Duolingo era que os medidores de força baseados em Leitner "não refletiam adequadamente o que os alunos tinham aprendido", gerando reclamações [F: settles2016hlr]. O HLR substitui a regra fixa por um preditor de recordação ajustado aos dados, que também permite personalizar por item via pesos de features.

## Fundamentos e funcionamento

Modelo [F: settles2016hlr]:

- Curva de esquecimento: `p = 2^(-Δ/h)`, com `p` a probabilidade de recordação, `Δ` o tempo desde a última prática e `h` a meia-vida.
- Meia-vida estimada: `ĥ_Θ = 2^(Θ·x)` — a meia-vida cresce exponencialmente com cada exposição, pressuposto comum na pesquisa de espaçamento.
- Perda (por instância): `ℓ = (p − p̂_Θ)² + α(h − ĥ_Θ)² + λ‖Θ‖²`, onde `h` é aproximado algebricamente por `h = −Δ / log₂(p)`. O termo em `h` importa: sem ele, o MAE mais que dobra.
- Otimização por AdaGrad (SGD), com `λ = 0.1`, `α = 0.01`, `η = 0.001` no experimento; na prática `p̂` é limitado a [0,0001; 0,9999] e `ĥ` a [15 min; 9 meses].

Features [F: settles2016hlr]:

- *Interação*: contadores por aluno-palavra — vezes vistas `x_n`, acertos `x_⊕`, erros `x_⊖` (raiz quadrada dos contadores funcionou melhor que os valores brutos) — responsáveis pela personalização.
- *Lexeme tags*: cerca de 20 mil variáveis indicadoras esparsas, uma por lexema, capturando a dificuldade inerente de cada palavra; mais um bias.

Pimsleur e Leitner são casos particulares do HLR com pesos fixos, o que situa o modelo como generalização treinável dos algoritmos clássicos [F: settles2016hlr].

## Dados e resultados do artigo

- Avaliação histórica: 12,9 milhões de sessões aluno-palavra de duas semanas de logs do Duolingo, 90% treino / 10% teste [F: settles2016hlr]. HLR obteve MAE 0,128, contra 0,235 do Leitner, 0,445 do Pimsleur e 0,211 da regressão logística; em AUC, porém, o Leitner foi o melhor (0,542, contra 0,538 do HLR); o HLR teve a melhor correlação de meia-vida (CORh 0,201) [F: settles2016hlr]. A redução de erro "45%+" do abstract refere-se ao MAE sobre o Leitner [F: settles2016hlr].
- Pesos aprendidos são interpretáveis: pesos positivos em cognatos e palavras curtas/regulares, negativos em formas irregulares e construções como particípios — leitura de dificuldade linguística a partir do modelo [F: settles2016hlr].
- Experimento de usuário I (HLR vs. Leitner, ~1 milhão de alunos, 6 semanas): atividade geral +0,3%, lições +0,3%, prática −7,3% (significativo) — interpretado pelos autores como prática desnecessária evitada [F: settles2016hlr].
- Experimento de usuário II (HLR sem lexeme tags vs. HLR, 3,3 milhões de alunos, 2 semanas): retenção diária +12,0% em qualquer atividade, +1,7% em lições, +9,5% em prática, todos significativos; o ganho de engajamento "12%" do abstract vem deste experimento [F: settles2016hlr]. A motivação foi overfitting das features de lexema: itens com pesos muito negativos decaíam rápido demais, gerando reclamações; a variante sem lexemas (HLR -lex) foi implantada para todos [F: settles2016hlr].
- Dados e código públicos: repositório `duolingo/halflife-regression` (MIT), com ~13 milhões de traces (CSV de ~361 MB) hospedados no Harvard Dataverse (DOI 10.7910/DVN/N8XJME) e implementação em Python puro [F: duolingo2016hlrcode].

## Requisitos e pressupostos

- Volume: milhões de traces para ajustar dezenas de milhares de pesos; o termo L2 não bastou para evitar overfitting dos lexemas [F: settles2016hlr].
- `p` observado como *proporção* de acertos na sessão (vários exercícios da mesma palavra), não como resultado binário único [F: settles2016hlr].
- Forma exponencial única da curva de esquecimento e meia-vida log-linear nas features — pressupostos fortes herdados de Ebbinghaus; modelos como ACT-R e MCM usam formas de lei de potência [F: settles2016hlr].

## Vantagens e limitações

Vantagens: treinável a partir de logs reais; generaliza Pimsleur e Leitner; pesos interpretáveis; validado em produção com experimentos controlados de grande escala — algo raro na literatura de repetição espaçada [F: settles2016hlr] [I].

Limitações:

- AUC próxima do acaso: 0,538 no artigo original [F: settles2016hlr]; 0,5079 na reprodução de Ilídio et al. sobre o mesmo dataset [F: ilidio2026hlr]. Para ordenar o que praticar primeiro — o uso real do modelo — métricas de ranqueamento importam mais que MAE, argumento explícito de Ilídio et al. [F: ilidio2026hlr].
- Personalização limitada: um modelo global por curso; o aluno só entra via contadores. A extensão com efeitos aleatórios cruzados de aluno e lexema (HLR+LMM) melhora todas as métricas (AUC 0,5584; com features estendidas, 0,6030; Random Forest sobre as mesmas features, 0,6312) [F: ilidio2026hlr].
- Os resultados de engajamento são métricas de negócio do próprio Duolingo, não medidas de aprendizagem; o artigo não reporta efeito sobre retenção de conhecimento [I].
- Fora do domínio de origem: no srs-benchmark (dados de 10 mil usuários de Anki; benchmark mantido pelos autores do FSRS), o HLR aparece com log loss 0,4694, RMSE(bins) 0,1275 e AUC 0,6369 — pior que a baseline constante em log loss (0,3945) e muito atrás do FSRS-6 (0,3460 / 0,0653 / 0,7034) [F: srsbenchmark2026]. A comparação deve ser lida com cautela dupla: o benchmark é dos autores do algoritmo concorrente, e o HLR foi desenhado para taxas de recordação por sessão em dados de linguagem, não para revisões binárias de flashcards [I].

## Análises e sucessores

Linhagem documentada por Ilídio et al. [F: ilidio2026hlr]: reformulações neurais do HLR — rede feed-forward (Zaidi et al. 2020, "neural half-life regression"), GRU (Ye et al. 2022) e atenção (Ma et al. 2023) — melhoram a predição ao custo de explicabilidade; a crítica central dos autores é a dependência de um conjunto pequeno de features. A resposta deles (HLR de efeitos mistos + Random Forest + SHAP) busca ganho de desempenho mantendo explicação, com Δ (tempo desde a última exposição) como a feature mais influente [F: ilidio2026hlr].

## Métricas e métodos de avaliação

MAE, AUC e correlação de Spearman da meia-vida no artigo original e na reanálise [F: settles2016hlr] [F: ilidio2026hlr]; log loss e RMSE(bins) no srs-benchmark [F: srsbenchmark2026]. Ver `adp.eval.predictive-metrics`.

## Exemplo técnico independente de domínio

```
# predição
h_est = 2 ** dot(theta, x)          # meia-vida em dias
p_est = 2 ** (-delta / h_est)       # probabilidade de recordar

# treino (SGD sobre traces <p, delta, x>)
h_obs = -delta / log2(clamp(p))
perda = (p - p_est)**2 + alfa*(h_obs - h_est)**2 + lambda*norm2(theta)
theta -= taxa * grad(perda)         # AdaGrad no artigo
```

Conforme as equações (1)–(3) e o apêndice A.3 do artigo [F: settles2016hlr].

## Relações com outros conceitos

Formaliza a curva de esquecimento de `adp.sr.memory-and-forgetting` como preditor treinável. Alternativa aos algoritmos clássicos (`adp.sr.classical-algorithms`), que são seus casos particulares, e ao `adp.sr.fsrs`, que modela estado de memória por item em vez de meia-vida por features. Como regressão sobre contadores de acertos e erros, é parente dos modelos logísticos de knowledge tracing (`adp.kt.logistic-models`); os efeitos aleatórios de aluno e item da extensão de Ilídio et al. são análogos a habilidade e dificuldade em `adp.irt.item-response-theory` [F: ilidio2026hlr].

## Lacunas e questões abertas

- Procuramos um relatório independente intitulado "half-life regression revisited"; o que encontramos de verificável foi o artigo aberto de Ilídio et al. (2026), usado aqui. Discussões de praticantes criticando o MAE como métrica (issue no projeto Ebisu) não foram abertas e não são citadas como fonte.
- Zaidi et al. 2020, Ye et al. 2022 (GRU-HLR) e Ma et al. 2023 são citados via Ilídio et al.; não abrimos os originais.
- Não há, até onde verificamos, replicação dos experimentos de usuário fora do Duolingo.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| settles2016hlr | academico | 2026-10-29 |
| duolingo2016hlrcode | fornecedor | 2026-10-29 |
| ilidio2026hlr | academico | 2026-10-29 |
| srsbenchmark2026 | tecnico | 2026-10-29 |
