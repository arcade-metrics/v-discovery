---
id: adp.kt.bayesian-knowledge-tracing
titulo: Bayesian Knowledge Tracing (BKT)
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [corbett1995kt, pelanek2017overview, vandesande2013bkt, beckchang2007identifiability, pavlik2009pfa, khajah2016howdeep]
relacoes:
  - { tipo: parte-de, alvo: adp.lm.learner-model }
  - { tipo: alternativa-a, alvo: adp.kt.logistic-models }
  - { tipo: alternativa-a, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: depende-de, alvo: adp.id.knowledge-components }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: avaliado-por, alvo: adp.eval.evaluation-protocols }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
  - { tipo: relacionado-a, alvo: adp.kt.comparison }
termos: [knowledge tracing, mastery learning, mastery threshold, slip, guess, hidden Markov model, identifiability, model degeneracy, overlay model]
---

# Bayesian Knowledge Tracing (BKT)

## Definição e terminologia

Knowledge tracing é o processo em que um tutor mantém, para cada unidade de conhecimento do domínio, uma estimativa da probabilidade de que o aluno a tenha aprendido, atualizada a cada oportunidade de aplicá-la [F: corbett1995kt]. No modelo original de Corbett e Anderson, as unidades são regras de produção do "ideal student model" do ACT Programming Tutor, e o modelo do aluno é um *overlay* desse modelo ideal [F: corbett1995kt]. O nome "Bayesian Knowledge Tracing" (BKT) consolidou-se depois; Pelánek o descreve como um caso especial de modelo oculto de Markov (HMM) com habilidade binária (sabe/não sabe) e transição discreta do estado não aprendido para o aprendido [F: pelanek2017overview].

O que não é: BKT não é *model tracing* — o acompanhamento passo a passo da resolução para dar feedback imediato, que no mesmo tutor usa as mesmas regras mas é um processo distinto [F: corbett1995kt]. Também não é um modelo de habilidade contínua: a família logística (`adp.kt.logistic-models`) modela a habilidade como variável contínua de crescimento gradual [F: pelanek2017overview].

van de Sande distingue duas formas que receberam o mesmo nome: a cadeia de Markov de BKT, que prediz a probabilidade média (entre alunos) de acerto a cada oportunidade, e o HMM completo, que usa o desempenho do aluno individual para atualizar a probabilidade condicional de aprendizado [F: vandesande2013bkt].

## Problema que resolve

Implementar *mastery learning* individualizado: decidir, durante a prática, quando cada componente de conhecimento foi dominado, para dar prática adicional só do que falta. No tutor, o aluno pratica exercícios de uma seção até que cada regra introduzida atinja o critério de domínio, e os exercícios remediais variam por aluno [F: corbett1995kt]. A avaliação fica continuamente integrada à prática — testes podem validar as decisões de mastery, mas não entram nelas [F: corbett1995kt].

## Fundamentos e funcionamento

### Os quatro parâmetros

O modelo assume aprendizagem em dois estados: cada regra está no estado aprendido ou não aprendido; a transição pode ocorrer antes da prática (leitura do texto) ou em cada oportunidade de aplicação; não há esquecimento; o desempenho é governado pelo estado, mas só probabilisticamente [F: corbett1995kt]. Dois parâmetros de aprendizagem e dois de desempenho, estimados empiricamente por regra [F: corbett1995kt]:

| Parâmetro | Nome | Definição |
|---|---|---|
| p(L0) | Initial Learning | probabilidade de a regra já estar aprendida antes da primeira oportunidade de aplicá-la [F: corbett1995kt] |
| p(T) | Acquisition | probabilidade de transição do estado não aprendido para o aprendido após uma oportunidade de aplicação [F: corbett1995kt] |
| p(G) | Guess | probabilidade de acertar com a regra não aprendida [F: corbett1995kt] |
| p(S) | Slip | probabilidade de errar com a regra aprendida [F: corbett1995kt] |

### Equações

Atualização do estado de conhecimento após a n-ésima oportunidade (equação 1 do artigo original) [F: corbett1995kt]:

```
p(Ln) = p(Ln-1 | evidência) + (1 − p(Ln-1 | evidência)) · p(T)
```

A posteriori `p(Ln-1 | evidência)` vem de inferência bayesiana sobre o acerto ou erro da ação; o procedimento é uma variação do de Atkinson (1972), e p(T) independe de a aplicação ter sido correta ou não [F: corbett1995kt]. O artigo original não explicita as fórmulas condicionais; elas aparecem na literatura posterior [I]. Na forma dada por Pelánek (θ = estimativa de conhecimento, c = correção da resposta) [F: pelanek2017overview]:

```
se c = 1:  θ' = θ(1−Ps) / (θ(1−Ps) + (1−θ)Pg)
se c = 0:  θ' = θPs / (θPs + (1−θ)(1−Pg))
θ := θ' + (1 − θ') Pl
```

Predição de acerto (equação 2 do artigo original) [F: corbett1995kt]:

```
p(C) = p(L)·(1 − p(S)) + (1 − p(L))·p(G)
```

### Critério de mastery

O tutor apresenta exercícios até cada regra da seção atingir probabilidade de conhecimento de 0,95, critério análogo aos sistemas de mastery learning do Personalized System of Instruction de Keller [F: corbett1995kt]. Pelánek registra o mesmo "95% de chance" como critério de parada comum em políticas de mastery, ao lado de alternativas como "k acertos seguidos" [F: pelanek2017overview].

### Ajuste de parâmetros

Os parâmetros globais (p(L0), p(T), p(S), p(G)) são tipicamente ajustados por expectation-maximization, busca exaustiva em grade ou gradiente; abordagens de ajuste por soma de quadrados dos resíduos (curve fitting) também foram usadas, inclusive no artigo original [F: pelanek2017overview] [F: vandesande2013bkt].

## Requisitos e pressupostos

- Um mapeamento de itens para componentes de conhecimento, com um modelo BKT independente por componente; o modelo básico não representa relações entre componentes [F: pelanek2017overview]. Ver `adp.id.knowledge-components`.
- Não-esquecimento: a transição aprendido → não aprendido não ocorre [F: corbett1995kt]. O pressuposto é razoável para prática em intervalos curtos [F: khajah2016howdeep]; para conhecimento declarativo com retenção de longo prazo ele é a principal limitação [I].
- Resposta binária (certo/errado) por oportunidade, com uma única regra creditada por ação — no tutor isso é garantido pela estrutura de currículo por mastery [F: corbett1995kt].
- p(T) constante no tempo [F: vandesande2013bkt].

## Identifiability e degeneração de parâmetros

Beck e Chang identificaram o "Identifiability Problem": múltiplas combinações de P(G) e P(L0) produzem exatamente a mesma taxa de erro média prevista, logo os dados agregados não determinam os parâmetros [F: vandesande2013bkt, que descreve o resultado; beckchang2007identifiability, metadados]. van de Sande explica a origem: a cadeia de Markov de BKT tem solução analítica exponencial `P(Cj) = 1 − P(S) − A·e^(−βj)` com apenas três parâmetros efetivos, onde `A = (1 − P(S) − P(G))(1 − P(L0))` — qualquer combinação de P(G) e P(L0) com o mesmo A gera o mesmo modelo agregado [F: vandesande2013bkt].

Já o HMM completo não sofre de identifiability quando há acertos e erros na sequência: os quatro parâmetros afetam o comportamento separadamente [F: vandesande2013bkt]. Mas há degeneração empírica: Baker, Corbett e Aleven definiram como "empirically degenerate" os modelos em que um acerto não aumenta a estimativa de aprendizado; a análise de pontos fixos de van de Sande mostra que o comportamento desejado exige `P(G) + P(S) < 1` e `0 < P(T) < 1 − P(S)/(1 − P(G))` [F: vandesande2013bkt]. Pavlik et al. observam, na prática, slip implausivelmente alto quando não limitado ("a problem with identifiability"), e por isso limites como slip ≤ 0,1 e guess ≤ 0,3 foram recomendados por Corbett para evitar sobreajuste [F: pavlik2009pfa]. Pelánek nota que a importância da identifiability depende do propósito: pouco relevante para política instrucional baseada só em predições, crítica para open learner models e para interpretação de parâmetros [F: pelanek2017overview].

## Validade empírica original

No estudo 1 (tutor de Lisp, 21 regras, 158 goals de programação), com os quatro parâmetros constantes entre regras, a correlação entre acurácia prevista e observada por goal foi r = 0,47 (erro médio 0,06; erro absoluto médio 0,16); permitindo parâmetros por regra, r = 0,85 (erro médio −0,01; erro absoluto 0,07) [F: corbett1995kt]. Na predição de testes externos, o modelo foi sensível a diferenças individuais quando os alunos não trabalharam até mastery: correlação real×esperada r = 0,69 no terceiro teste [F: corbett1995kt]. O modelo, porém, subestimava alunos acima da média e superestimava os abaixo, visível na correlação negativa entre erros no tutor e acurácia no teste [F: corbett1995kt].

## Variantes

- **Individualização**: Corbett e Anderson estimam quatro pesos por aluno (um por tipo de parâmetro), aplicados em forma de odds: `p_irs = p_ir·w_is / (p_ir·w_is + (1 − p_ir))`; com pesos ajustados, a predição do segundo teste tornou-se confiável (r = 0,51) [F: corbett1995kt]. Trabalhos posteriores individualizam p(L0) e p(T) (Pardos e Heffernan 2010; Yudelson et al. 2013), com risco de sobreajuste por poucos dados por aluno [F: pelanek2017overview].
- **Dificuldade de item**: KT-IDEM adiciona parâmetros por item (Pardos e Heffernan 2011) [F: pelanek2017overview].
- **Contextualização de slip e guess**: estimativas contextuais por ação (Baker, Corbett e Aleven 2008) [F: pelanek2017overview].
- **Esquecimento**: um parâmetro F = P(transição aprendido → não aprendido) sensibiliza o modelo a recência e à sequência absoluta de tentativas [F: khajah2016howdeep]; ver `adp.kt.deep-knowledge-tracing` para o papel dessa extensão na comparação com DKT.

## Exemplo técnico independente de domínio

```
para cada componente k: L[k] = pL0[k]
ao observar resposta (k, correta?):
    se correta: post = L[k]*(1-pS[k]) / (L[k]*(1-pS[k]) + (1-L[k])*pG[k])
    senão:      post = L[k]*pS[k]     / (L[k]*pS[k]     + (1-L[k])*(1-pG[k]))
    L[k] = post + (1 - post) * pT[k]
    se L[k] >= 0.95: declarar mastery de k      # critério do tutor original
predizer_acerto(k) = L[k]*(1-pS[k]) + (1-L[k])*pG[k]
```

Restrições de sanidade ao ajustar: `pG + pS < 1` e `pT < 1 − pS/(1 − pG)` [F: vandesande2013bkt].

## Relações com outros conceitos

É a técnica de referência de estimação de estado do aluno dentro de `adp.lm.learner-model`. Alternativa aos modelos logísticos (`adp.kt.logistic-models`) e ao DKT (`adp.kt.deep-knowledge-tracing`); a comparação sistemática está em `adp.kt.comparison`. Depende de uma decomposição do domínio em `adp.id.knowledge-components`. Suas predições alimentam políticas de sequenciamento e mastery (`adp.adapt.sequencing-policies`) e são avaliadas pelos protocolos e métricas de `adp.eval.predictive-metrics` e `adp.eval.evaluation-protocols`.

## Lacunas e questões abertas

- Beck e Chang 2007 não pôde ser aberto (Springer exige autenticação; nenhuma cópia aberta encontrada em buscas na sessão); o conteúdo citado vem da descrição em van de Sande 2013. O remédio proposto pelos autores (priors) não foi citado aqui por falta de fonte aberta.
- As equações condicionais de atualização não constam explicitamente do artigo de 1995 aberto nesta sessão (26 páginas verificadas); atribuímos as fórmulas a Pelánek 2017 e van de Sande 2013. Se alguma edição do artigo tiver apêndice com as fórmulas, a atribuição pode ser refinada.
- O artigo original não informa de onde vem o valor 0,95 do critério de mastery além da analogia com mastery learning; não localizamos justificativa formal do limiar [I].
- van de Sande cita evidência de que curvas de aprendizagem individuais podem seguir lei de potência, o que questionaria a forma exponencial de BKT; a questão segue aberta [F: vandesande2013bkt].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| corbett1995kt | academico | 2026-10-29 |
| pelanek2017overview | academico | 2026-10-29 |
| vandesande2013bkt | academico | 2026-10-29 |
| beckchang2007identifiability | academico (apenas metadados) | 2026-10-29 |
| pavlik2009pfa | academico | 2026-10-29 |
| khajah2016howdeep | academico | 2026-10-29 |
