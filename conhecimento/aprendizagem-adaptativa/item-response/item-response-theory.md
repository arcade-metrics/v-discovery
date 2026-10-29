---
id: adp.irt.item-response-theory
titulo: Item response theory (IRT)
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nguyen2014irt, rizopoulos2006ltm, magis2012catr, pelanek2016elo, papousek2014adaptive, gervet2020deepkt, rasch1960probabilistic, lord1980applications, baker2001irtbasics]
relacoes:
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: adp.irt.elo-rating }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.kt.logistic-models }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
termos: [item characteristic curve, difficulty, discrimination, guessing, unidimensionality, local independence, Rasch model, 1PL, 2PL, 3PL, computerized adaptive testing, item bank, information function, differential item functioning]
---

# Item response theory (IRT)

## Definição e terminologia

Teoria de resposta ao item (IRT) é a família de modelos de variável latente que liga respostas dicotômicas ou politômicas a um traço latente unidimensional (habilidade), com aplicação principal em testagem educacional [F: rizopoulos2006ltm]. A curva que dá a probabilidade de acerto em função da habilidade é a *item characteristic curve* (ICC). A forma geral para item dicotômico i e habilidade z é P(x_i = 1 | z) = c_i + (1 − c_i)·g(a_i(z − b_i)), onde b_i é a dificuldade, a_i a discriminação (inclinação da ICC), c_i o parâmetro de acerto ao acaso (guessing) e g a função logística ou probit [F: rizopoulos2006ltm]. Nomes alternativos: *latent trait theory*; o modelo de Rasch é também chamado 1PL, com uma sutileza — estritamente, Rasch fixa todas as discriminações em 1, enquanto o 1PL as exige apenas iguais entre si [F: magis2012catr]. As origens canônicas são Rasch (1960) e Lord (1980), aqui citadas apenas por metadados (cópias abertas não localizadas). O que não é: IRT não modela mudança de conhecimento ao longo da prática; é um modelo de medição de estado (ver seção sobre knowledge tracing).

## Problema que resolve

Na teoria clássica de testes (CTT), o escore observado depende dos itens aplicados (itens fáceis produzem escores maiores) e as propriedades dos itens mudam com a amostra, exigindo reestimar confiabilidade a cada população [F: nguyen2014irt]. A IRT, quando seus pressupostos valem, separa pessoa e item: as estimativas de traço são comparáveis entre conjuntos de itens diferentes (invariância de habilidade) e os parâmetros de item permanecem estáveis entre amostras (invariância de item) [F: nguyen2014irt]. Essa separação é o que viabiliza bancos de itens calibrados e testes adaptativos.

## Fundamentos e funcionamento

### Os modelos 1PL/Rasch, 2PL e 3PL

- **1PL/Rasch**: c_i = 0 e a_i = 1; só a dificuldade varia entre itens: P(correto) = 1/(1 + e^−(θ−b)) [F: rizopoulos2006ltm] [F: papousek2014adaptive]. A dificuldade b é o nível de traço em que a probabilidade de acerto é 50% [F: nguyen2014irt]. A parcimônia permite amostras menores, mas as propriedades de comparabilidade só valem se o modelo ajustar [F: nguyen2014irt].
- **2PL**: c_i = 0 e a_i livre por item; a discriminação é a inclinação da ICC no ponto b e mede quão bem o item separa níveis baixos e altos do traço [F: nguyen2014irt] [F: rizopoulos2006ltm].
- **3PL (Birnbaum)**: estima também c_i, a assíntota inferior — probabilidade de acerto ao acaso por examinandos de habilidade muito baixa; adequado a testes de conhecimento com múltipla escolha, e c > 0,35 é tradicionalmente considerado inaceitável [F: nguyen2014irt] [F: rizopoulos2006ltm].
- **4PL (Barton e Lord)**: acrescenta assíntota superior d_i < 1 (desatenção), usada em CAT para mitigar o efeito de erros no início do teste sobre examinandos de alta habilidade [F: magis2012catr].

Logit e probit são intercambiáveis na prática via a constante de escala 1,702 [F: rizopoulos2006ltm]. Para itens politômicos existem o Graded Response Model, o Partial Credit e o Rating Scale [F: rizopoulos2006ltm], não detalhados aqui.

### Pressupostos

1. **Unidimensionalidade**: os itens medem um único traço; verifica-se por análise fatorial — solução de um fator, ou primeiro fator dominante com pelo menos 20% da variância [F: nguyen2014irt].
2. **Independência local**: dado o traço, as respostas aos itens são independentes; é o que decompõe a verossimilhança em produto de termos por item [F: rizopoulos2006ltm]. Diagnósticos: correlações residuais e estatísticas de dependência local; discriminações muito altas (acima de ~4) são sinal de violação [F: nguyen2014irt].
3. **Monotonicidade**: a probabilidade de acerto cresce com o traço [F: nguyen2014irt].
4. **Invariância de parâmetros entre grupos**, verificada por análise de *differential item functioning* (DIF) com itens-âncora [F: nguyen2014irt].

### Estimação

Três grandes métodos de máxima verossimilhança: condicional (CML), conjunta (JMLE) e marginal (MML), além de abordagens bayesianas [F: rizopoulos2006ltm]. A JMLE é o procedimento iterativo padrão para o modelo de Rasch, mas é lenta para dados grandes e inadequada para atualização online [F: papousek2014adaptive]. A MML assume que os respondentes são amostra aleatória de uma população com distribuição de habilidade F(z), integra a habilidade para fora da verossimilhança e maximiza a verossimilhança marginal — na prática com quadratura de Gauss-Hermite [F: rizopoulos2006ltm]. A precisão da medição na IRT é descrita pela função de informação do item e do teste, que varia ao longo da escala do traço, em contraste com o coeficiente único de confiabilidade da CTT [F: nguyen2014irt].

## IRT estática versus modelagem dinâmica de aprendizagem

Os modelos básicos de IRT assumem habilidade constante: foram desenvolvidos para testagem, em que não se espera mudança de habilidade durante o teste [F: pelanek2016elo]. Knowledge tracing e sistemas de rating modelam exatamente o que a IRT assume fixo — a mudança do conhecimento com a prática [F: pelanek2016elo]. Em prática adaptativa, o objetivo primário é melhorar a habilidade; a estimativa é meio, não fim, então as garantias estatísticas da IRT pesam menos que modelar aprendizagem, esquecimento e motivação [F: papousek2014adaptive]. [I] Os dois mundos se encontram nos modelos logísticos de KT: o Best-LR de Gervet et al., melhor regressão logística em um benchmark de nove conjuntos, é descrito pelos autores como PFA com contagens reescalonadas "aumentada com parâmetros de habilidade do aluno e dificuldade da questão da IRT" [F: gervet2020deepkt]; e o AKT regulariza embeddings de questão com o modelo de Rasch (ver `adp.kt.deep-kt-successors`). A estimação online dos parâmetros de Rasch sem recalibração é o papel do Elo (ver `adp.irt.elo-rating`).

## Uso em testes adaptativos (CAT)

Em computerized adaptive testing os itens são escolhidos um a um, de forma ótima dado o que já se observou: o processo exige um banco de itens previamente calibrado por um modelo IRT, seleciona o próximo item pelo critério de informação (o mais comum é máxima informação de Fisher no ponto da estimativa corrente; a regra de Urry — item com dificuldade mais próxima da habilidade estimada — é equivalente à MFI sob o 1PL), reestima a habilidade após cada resposta (ML, Bayes modal, EAP ou verossimilhança ponderada) e para por um de três critérios: comprimento fixo, precisão alvo da estimativa ou classificação do examinando [F: magis2012catr]. Vantagens sobre teste fixo: testes mais curtos para a mesma precisão, menor risco de fraude (sequências diferentes por pessoa) e estimativa imediata; desvantagens: exige recursos computacionais e um banco de itens grande e bem calibrado, o que encarece a administração [F: magis2012catr]. Questões operacionais relevantes: exposição de itens e balanceamento de conteúdo [F: magis2012catr]. Do ponto de vista pedagógico, o alvo de informação máxima implica taxa de acerto perto de 50%, que é baixa para prática e afeta motivação — sistemas de prática adaptativa miram taxas maiores, como 75% [F: papousek2014adaptive].

## Vantagens e limitações

Vantagens: invariância de pessoa e item quando o modelo ajusta; precisão descrita por nível de traço; base formal para CAT e para equiparação de testes [F: nguyen2014irt] [F: magis2012catr]. Limitações: pressupostos fortes (unidimensionalidade, independência local) que precisam ser testados [F: nguyen2014irt]; habilidade constante, inadequada para modelar aprendizagem em curso [F: pelanek2016elo]; calibração exige amostras não triviais e procedimentos iterativos difíceis de usar online [F: papousek2014adaptive] [F: pelanek2016elo]; recuperação ruim de habilidade quando há erros iniciais em CAT, mitigável com 4PL [F: magis2012catr].

## Alternativas e comparações

| Aspecto | IRT (1–3PL) | Elo rating | BKT / KT |
|---|---|---|---|
| Habilidade | constante [F: pelanek2016elo] | muda a cada resposta [F: pelanek2016elo] | muda (aprendizagem) [F: papousek2014adaptive] |
| Estimação | JMLE/MML iterativa, offline [F: rizopoulos2006ltm] | atualização heurística online [F: pelanek2016elo] | EM / busca exaustiva [F: papousek2014adaptive] |
| Garantias estatísticas | sim, modelos bem calibrados [F: pelanek2016elo] | não [F: pelanek2016elo] | parciais [I] |
| Uso típico | testagem, CAT [F: magis2012catr] | prática adaptativa, baixo risco [F: pelanek2016elo] | tutores, mastery learning [F: gervet2020deepkt] |

## Exemplo técnico independente de domínio

Laço de um CAT dicotômico sobre banco calibrado (síntese das etapas descritas em [F: magis2012catr]):

```
cat(banco_calibrado, criterio_parada):
    respostas = []
    theta = estimativa_inicial()            # ex.: 0, ou regra inicial do banco
    enquanto nao criterio_parada(theta, erro_padrao, |respostas|):
        item = argmax_{i em banco nao usados} informacao_fisher(i, theta)
        r = administrar(item)               # 0 ou 1
        respostas.append((item, r))
        theta = reestimar(respostas)        # ML, Bayes modal, EAP ou WLE
    retornar theta, erro_padrao(theta)
```

Critérios de parada típicos: número fixo de itens, erro padrão abaixo de limiar, ou decisão de classificação [F: magis2012catr].

## Relações com outros conceitos

É um dos fundamentos dos modelos de aluno (`adp.lm.learner-model`). O Elo (`adp.irt.elo-rating`) é a mesma forma funcional do Rasch com estimação online. Os modelos logísticos de KT (`adp.kt.logistic-models`) estendem a forma logística com contagens de prática; o BKT (`adp.kt.bayesian-knowledge-tracing`) é a alternativa markoviana. A seleção de itens do CAT é um caso particular das políticas de `adp.adapt.sequencing-policies`. Calibração e qualidade preditiva são avaliadas pelos métodos de `adp.eval.predictive-metrics`.

## Lacunas e questões abertas

- Rasch (1960) e Lord (1980) entraram apenas como [metadados]: nenhuma cópia aberta foi localizada hoje; metadados verificados em catálogos.
- Baker, *The Basics of Item Response Theory* (2001): registro ERIC verificado e PDF baixado, mas a digitalização não tem camada de texto; o conteúdo não foi lido e nada é citado dele.
- A página aberta do artigo de Thompson e Weiss (PARE 2011) sobre desenvolvimento de CAT estava bloqueada por proteção anti-bot; não citada.
- Detalhes da MML (algoritmo EM de Bock e Aitkin) ficaram na referência indireta de Rizopoulos a Baker e Kim (2004); fonte primária aberta não verificada.
- Modelos politômicos e IRT multidimensional não foram cobertos; relevantes para rubricas e crédito parcial.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nguyen2014irt | academico | 2026-10-29 |
| rizopoulos2006ltm | academico | 2026-10-29 |
| magis2012catr | academico | 2026-10-29 |
| pelanek2016elo | academico | 2026-10-29 |
| papousek2014adaptive | academico | 2026-10-29 |
| gervet2020deepkt | academico | 2026-10-29 |
| rasch1960probabilistic | academico [metadados] | 2026-10-29 |
| lord1980applications | academico [metadados] | 2026-10-29 |
| baker2001irtbasics | academico [metadados] | 2026-10-29 |
