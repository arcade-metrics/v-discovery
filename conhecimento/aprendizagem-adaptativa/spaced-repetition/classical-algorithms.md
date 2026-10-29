---
id: adp.sr.classical-algorithms
titulo: Algoritmos clássicos de repetição espaçada (Leitner e SM-2)
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [wozniak1990sm2, supermemoguru2018sm2, anki2026algofaq, anki2026deckoptions, settles2016hlr, ilidio2026hlr]
relacoes:
  - { tipo: depende-de, alvo: adp.sr.memory-and-forgetting }
  - { tipo: depende-de, alvo: adp.sr.spacing-and-testing-effects }
  - { tipo: alternativa-a, alvo: adp.sr.half-life-regression }
  - { tipo: alternativa-a, alvo: adp.sr.fsrs }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
termos: [spaced repetition, Leitner system, SM-2, ease factor, graduated-interval recall, inter-repetition interval]
---

# Algoritmos clássicos de repetição espaçada (Leitner e SM-2)

## Definição e terminologia

Algoritmos clássicos de repetição espaçada são regras de agendamento de revisões com estrutura fixa e parâmetros escolhidos à mão, anteriores ao ajuste estatístico por dados de uso. Os três mais citados são o método de Pimsleur (*graduated-interval recall*, 1967), o sistema de Leitner (caixas de flashcards, 1972) e o SM-2 do SuperMemo (Wozniak, 1987–1990). Settles e Meeder observam que a maioria dos algoritmos práticos de repetição espaçada são "funções simples com uns poucos parâmetros escolhidos à mão", o que era razoável quando os cronogramas eram geridos sem computador [F: settles2016hlr].

O que não são: não são modelos preditivos de memória. Nenhum deles estima probabilidade de recordação; eles produzem apenas o próximo intervalo de revisão a partir do desempenho observado. Modelos que estimam recordação (HLR, FSRS) são tratados em `adp.sr.half-life-regression` e `adp.sr.fsrs`.

## Problema que resolve

Dado o efeito de espaçamento e o efeito de teste (`adp.sr.spacing-and-testing-effects`), revisar no momento certo rende mais retenção por minuto de estudo do que revisar em bloco. O problema operacional é decidir *quando* reapresentar cada item com informação mínima: apenas o histórico de acertos e erros daquele item, sem dados populacionais. Os algoritmos clássicos resolvem isso com regras determinísticas baratas de computar e de entender.

## Fundamentos e funcionamento

### Pimsleur: intervalos fixos crescentes

Pimsleur (1967) propôs introduzir e testar vocabulário em intervalos que crescem exponencialmente — no cronograma original: 5 s, 25 s, 2 min, 10 min, 1 h, 5 h, 1 dia, 5 dias, 25 dias, 4 meses, 2 anos [F: settles2016hlr]. O cronograma é pré-gravado e idêntico para todos os itens e alunos; não reage a erros [F: settles2016hlr].

### Leitner: caixas com promoção e rebaixamento

No sistema de Leitner (1972), caixas correspondem a intervalos de prática (na variante descrita por Settles e Meeder: 1, 2, 4, 8 e 16 dias). Todo cartão começa na caixa de 1 dia; um acerto o promove à caixa seguinte (intervalo dobra), um erro o rebaixa a uma caixa de intervalo menor (intervalo cai pela metade na variante analisada) [F: settles2016hlr]. É parcialmente adaptativo: o intervalo responde ao desempenho, mas a regra de atualização é fixa e igual para todos os itens e alunos [F: ilidio2026hlr]. O Duolingo usou uma variante de Leitner em seu modelo de aluno original, substituída depois pelo HLR em resposta a reclamações de que os medidores de força não refletiam o que o aluno sabia [F: settles2016hlr].

### SM-2: ease factor por item

O SM-2 foi descrito por Piotr Wozniak na dissertação de mestrado *Optimization of learning* (1990) e usado no SuperMemo 1.0 a 3.0, de 13/12/1987 a 09/03/1989; o nome vem do SuperMemo 2.0 [F: wozniak1990sm2]. O site do autor o apresenta como o primeiro algoritmo de computador para calcular o cronograma ótimo de repetição espaçada — afirmação de fornecedor sobre o próprio produto [F: supermemoguru2018sm2].

Especificação publicada pela SuperMemo [F: wozniak1990sm2]:

- Intervalos entre repetições (dias): `I(1) = 1`; `I(2) = 6`; para `n > 2`, `I(n) = I(n-1) * EF`, com arredondamento para cima.
- Cada item carrega um *ease factor* `EF`, inicial 2,5, atualizado após cada repetição conforme a qualidade da resposta `q` (escala 0–5, de "blecaute total" a "resposta perfeita"): `EF' = EF + (0.1 - (5-q) * (0.08 + (5-q) * 0.02))`. Com `q = 4` o EF não muda; se o resultado cair abaixo de 1,3, é fixado em 1,3.
- Resposta com `q < 3` reinicia as repetições do item a partir de `I(1)`, sem alterar o EF.
- Itens com `q < 4` são repetidos na mesma sessão até atingirem pelo menos 4.

O EF é o único estado adaptativo: itens difíceis acumulam EF menor e intervalos que crescem mais devagar. Não há modelo de probabilidade de recordação nem uso do histórico de outros itens ou de outros alunos [I].

## Requisitos e pressupostos

- Avaliação por item a cada revisão: binária (Leitner) ou graduada 0–5 (SM-2) [F: wozniak1990sm2].
- Nenhum dado populacional, timestamp fino ou treino: os parâmetros (intervalos iniciais 1 e 6 dias, EF inicial 2,5, piso 1,3) são constantes definidas pelo autor [F: wozniak1990sm2].
- Pressuposto implícito de que dobrar ou multiplicar por EF o intervalo após cada acerto acompanha o crescimento da retenção — herdado da pesquisa de espaçamento, mas não ajustado a material ou população [I].

## Uso em software de código aberto: o caso do Anki

O Anki, software de flashcards de código aberto, é um exemplo de implementação derivada do SM-2 — citado aqui como ilustração documentada, não como recomendação. A documentação do fornecedor afirma que o algoritmo padrão é "baseado no SuperMemo 2" com modificações, entre elas: passos de aprendizagem configuráveis em vez dos intervalos fixos de 1 e 6 dias; quatro botões de resposta em vez de seis graus; atraso na revisão incorporado ao próximo intervalo; erros em aprendizagem não afetam o ease; ease nunca abaixo de 130%; teto configurável de intervalo máximo [F: anki2026algofaq]. Nas opções de baralho, o *starting ease* padrão é 2,50, com *easy bonus* 1,30 e *hard interval* 1,20 [F: anki2026deckoptions]. Desde o Anki 23.10 o usuário pode optar pelo FSRS no lugar do algoritmo SM-2 modificado (`adp.sr.fsrs`) [F: anki2026algofaq].

## Vantagens e limitações

Vantagens: custo computacional desprezível e nenhuma necessidade de dados históricos — funcionam a partir do primeiro cartão [I]; regras inteiramente inspecionáveis, fáceis de explicar ao aluno [I]; décadas de uso prático em software de flashcards [F: settles2016hlr].

Limitações:

- Parâmetros fixos, não ajustados ao material nem ao aluno; Pimsleur nem sequer reage a erros [F: settles2016hlr].
- Não estimam probabilidade de recordação; como preditores, ficam perto do acaso: na reanálise de Ilídio et al. sobre os dados do Duolingo, Leitner obteve AUC 0,5100 e MAE 0,2313, e Pimsleur AUC 0,5067 e MAE 0,4383, contra MAE 0,1153 do HLR [F: ilidio2026hlr].
- No estudo original do HLR, Leitner teve MAE 0,235 e Pimsleur 0,445, contra 0,128 do HLR — embora Leitner tenha tido a melhor AUC (0,542) entre os métodos testados [F: settles2016hlr].
- No SM-2, o EF confunde dificuldade do item com estado da memória do aluno e só muda em função da última sequência de notas; dois alunos com memórias muito diferentes recebem o mesmo cronograma inicial [I].
- A documentação do Anki afirma que o FSRS "exige menos revisões para a mesma retenção" e lida melhor com revisões atrasadas que o SM-2 modificado — afirmação de fornecedor, condizente com os benchmarks mantidos pelos autores do FSRS, mas não verificada de forma independente aqui [F: anki2026algofaq].

## Alternativas e comparações

Pimsleur e Leitner podem ser escritos como casos particulares do HLR com pesos fixos: o cronograma de Pimsleur equivale a pesos {xn: 2,4; bias: -16,5} e o Leitner da Figura 3 do artigo a {acertos: +1; erros: -1} na meia-vida log-linear [F: settles2016hlr]. A comparação completa Leitner × SM-2 × HLR × FSRS × KT com esquecimento está em `adp.sr.comparison`.

## Exemplo técnico independente de domínio

```
# SM-2, por item
estado: n = 0, EF = 2.5, I = 0

revisar(q):                       # q em 0..5
    se q >= 3:
        n += 1
        se n == 1: I = 1
        senao se n == 2: I = 6
        senao: I = teto(I * EF)
    senao:
        n = 0; I = 1              # reinicia; EF inalterado
    EF = max(1.3, EF + (0.1 - (5-q)*(0.08 + (5-q)*0.02)))
    agendar(hoje + I dias)
```

Conforme a especificação publicada pela SuperMemo [F: wozniak1990sm2].

## Relações com outros conceitos

Justificam-se pelos efeitos de espaçamento e teste (`adp.sr.spacing-and-testing-effects`) e pressupõem o esquecimento descrito em `adp.sr.memory-and-forgetting`. São alternativas de baixo custo a `adp.sr.half-life-regression` e `adp.sr.fsrs`, que os substituem quando há dados de histórico em escala. A escolha do próximo item a revisar é um caso de `adp.adapt.sequencing-policies`.

## Lacunas e questões abertas

- Não localizamos avaliação publicada e revisada por pares do SM-2 como preditor de recordação; o benchmark srs-benchmark (mantido pelos autores do FSRS) não reporta linha SM-2 nas tabelas principais da versão consultada.
- A dissertação de Wozniak (1990) e o livro de Leitner (1972) não foram abertos; Leitner e Pimsleur estão descritos aqui pela caracterização verificável em Settles e Meeder (2016) e Ilídio et al. (2026).
- As datas e a primazia histórica do SM-2 vêm de páginas do próprio fornecedor (super-memory.com, supermemo.guru); não encontramos fonte independente que as confirme.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| wozniak1990sm2 | fornecedor | 2026-10-29 |
| supermemoguru2018sm2 | fornecedor | 2026-10-29 |
| anki2026algofaq | fornecedor | 2026-10-29 |
| anki2026deckoptions | fornecedor | 2026-10-29 |
| settles2016hlr | academico | 2026-10-29 |
| ilidio2026hlr | academico | 2026-10-29 |
