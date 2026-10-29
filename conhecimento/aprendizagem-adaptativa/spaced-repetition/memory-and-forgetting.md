---
id: adp.sr.memory-and-forgetting
titulo: Memória e esquecimento
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ebbinghaus1885memory, murre2015replication, wixted1991form, averell2011form, bjork1992disuse, bjork2023difficulties, wozniak1995twocomponents, wozniak2018twocomponentmodel, wozniak2018twocomponents, khajah2016deep]
relacoes:
  - { tipo: complementa, alvo: adp.sr.spacing-and-testing-effects }
  - { tipo: implementado-por, alvo: adp.sr.classical-algorithms }
  - { tipo: implementado-por, alvo: adp.sr.half-life-regression }
  - { tipo: implementado-por, alvo: adp.sr.fsrs }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
termos: [forgetting curve, savings, storage strength, retrieval strength, stability, retrievability, two-component model of memory]
---

# Memória e esquecimento

## Definição e terminologia

A *curva do esquecimento* (forgetting curve) descreve o declínio da retenção de material aprendido em função do tempo desde o estudo, com queda rápida no início e cada vez mais lenta depois [F: ebbinghaus1885memory]. A medida clássica é o *savings* (método das economias): a fração do esforço original de aprendizagem que é poupada ao reaprender o material após um intervalo [F: ebbinghaus1885memory].

Dois pares de termos descrevem o estado de um item na memória de longo prazo. Na "new theory of disuse" de Bjork e Bjork, cada item tem uma *storage strength* (quão bem aprendido e interconectado está) e uma *retrieval strength* (quão acessível está no momento, dado o contexto) [F: bjork2023difficulties]. Na tradição de repetição espaçada derivada de Wozniak/SuperMemo, o par análogo é *stability* (quanto tempo a memória dura sem revisão) e *retrievability* (probabilidade de recordação em um dado momento) [F: wozniak2018twocomponentmodel]. A própria literatura do SuperMemo reconhece os pares como contrapartes próximas, com interpretações distintas dos mecanismos [F: wozniak2018twocomponents].

O que não é: esquecimento, nos dois quadros, não é apagamento do traço. A teoria de Bjork assume que storage strength, uma vez acumulada, nunca é perdida; o que declina é a retrieval strength [F: bjork2023difficulties]. Essa é uma proposta teórica, não um achado replicado [I].

## Problema que resolve

Um modelo de aluno que estima domínio apenas a partir de acertos e erros, ignorando o tempo, superestima o conhecimento de quem não pratica há semanas. Qualquer sistema que decida *o que revisar e quando* precisa de um modelo explícito de declínio da recordação em função do tempo e do histórico de revisões [I]. Este documento reúne a base empírica (curva do esquecimento e sua replicação), o debate sobre a forma funcional e os dois modelos de dois componentes usados para fundamentar algoritmos de repetição espaçada (`adp.sr.classical-algorithms`, `adp.sr.fsrs`).

## Fundamentos e funcionamento

### A curva de Ebbinghaus

Ebbinghaus aprendeu séries de 13 sílabas sem sentido até o critério e as reaprendeu após intervalos variados, em 163 testes duplos realizados em 1879-1880 [F: ebbinghaus1885memory, §VII]. Resultados: após 1 hora, cerca de metade do trabalho original precisou ser refeito; após 24 horas, cerca de um terço foi retido (33,7%); após 6 dias, cerca de um quarto; após 31 dias, "fully one fifth" (pouco mais de 20%) [F: ebbinghaus1885memory, §VII]. Ele resumiu os próprios dados com a fórmula logarítmica `b = 100k / ((log t)^c + k)`, com k = 1,84 e c = 1,25 (t em minutos), apresentada como descrição dos seus resultados, não como lei geral [F: ebbinghaus1885memory, §29].

### Replicação moderna

Murre e Dros replicaram o experimento com um sujeito (o segundo autor, 22 anos, falante nativo de holandês), 70 listas de 104 sílabas CVC (8 séries de 13), intervalos de retenção de 20 min, 1 h, 9 h, 1, 2, 6 e 31 dias, e cerca de 70 horas de aprendizagem e reaprendizagem em 75 dias [F: murre2015replication]. A curva obtida é muito semelhante à de Ebbinghaus e à da replicação alemã de Heller et al., exceto no ponto de 31 dias, em que o savings do novo sujeito foi muito menor (0,041; 0,137 após correção pelo aumento do tempo de aprendizagem ao longo do experimento) [F: murre2015replication]. Os autores concluem ainda que a curva de Ebbinghaus "most probably shows a jump upwards starting at the 24 hour data point"; a literatura de sono preveria esse ganho, mas eles afirmam explicitamente que não se pode concluir que o aumento local se deva ao sono [F: murre2015replication]. O formato qualitativo da curva — queda acentuada seguida de queda lenta — é, portanto, achado empírico replicado; explicações mecanísticas do salto nas 24 h permanecem hipótese [H].

### Forma funcional: exponencial × potência

A forma matemática da curva é disputada há décadas. Wixted e Ebbesen relataram, comparando seis funções candidatas em experimentos de recordação de palavras, reconhecimento de faces e matching em pombos, que uma função de potência descreveu melhor o esquecimento, inclusive reanalisando a função de savings de Ebbinghaus [F: wixted1991form — apenas metadados e abstract verificados; texto completo não aberto]. Averell e Heathcote compararam funções candidatas com modelos hierárquicos bayesianos em dados de recordação com pistas de 1 min a 28 dias [F: averell2011form — apenas metadados e abstract verificados; conclusão não citada aqui]. Na análise de Murre e Dros, as funções de potência (1880) e logarítmica (1885) do próprio Ebbinghaus ajustam bem os dados dele (R² = 98,8%), mas, no conjunto das replicações, uma soma de exponenciais (equivalente ao Memory Chain Model dos autores) obteve o melhor AIC médio, com diferença de cerca de 1,5 ponto para a função de potência — abaixo do limiar de 2 usualmente considerado significativo [F: murre2015replication]. [I] A leitura prudente: nenhuma forma simples vence com folga; exponencial por item com parâmetros que mudam a cada revisão (como nos modelos de dois componentes) e potência por agregação são ambas defensáveis.

### A "new theory of disuse" (Bjork e Bjork)

A teoria, publicada em 1992 em homenagem a W. K. Estes [F: bjork1992disuse — metadados], é descrita pelos próprios autores em capítulo aberto de 2023 [F: bjork2023difficulties]. Postulados: (1) cada item tem storage strength e retrieval strength; (2) a recordação em um momento depende apenas da retrieval strength corrente; (3) a storage strength, uma vez acumulada, nunca é perdida — o que se perde com o desuso é acesso, não armazenamento; (4) há uma assimetria na interação: quanto maior a storage strength corrente, maior o ganho de retrieval strength ao reestudar ou recuperar; quanto maior a retrieval strength corrente, *menor* o ganho de storage strength — por isso esquecer (perder retrieval strength) pode ampliar o aprendizado, o "forgetting as the friend of learning"; (5) o ato de recuperar uma informação é um evento mais potente, para as duas forças, do que reestudá-la [F: bjork2023difficulties]. Todo esse conjunto é proposta teórica para explicar efeitos empíricos (espaçamento, teste), não resultado experimental direto — as forças não são observáveis separadamente [H].

### O modelo de dois componentes da tradição SuperMemo

Wozniak, Gorzelanczyk e Murakowski argumentaram, a partir de dados de espaçamento ótimo em aprendizagem de pares associados, pela existência de dois componentes independentes da memória de longo prazo, suficientes para explicar o espaçamento ótimo e o efeito de espaçamento [F: wozniak1995twocomponents]. Na formalização usada nos algoritmos SuperMemo mais recentes (SM-17): *stability* (S) é definida como o intervalo entre revisões que produz probabilidade média de recordação de 0,9; *retrievability* (R) é a probabilidade esperada de recordação, assumindo esquecimento exponencial negativo, `R = e^(-t/S)`; a stability aumenta quando a revisão ocorre antes de a retrievability chegar a zero, e o fator de aumento é maior quando a retrievability está mais baixa e menor para itens mais difíceis ou já muito estáveis [F: wozniak2018twocomponentmodel] [F: wozniak2018twocomponents]. Atenção ao estatuto das fontes: o artigo de 1995 saiu em periódico (Acta Neurobiologiae Experimentalis), mas as definições operacionais e fórmulas acima vêm do wiki supermemo.guru, literatura de praticante escrita pelo próprio autor do sistema, sem revisão por pares [F: wozniak2018twocomponentmodel]. Divergência registrada pelo próprio Wozniak: Bjork sustenta que memórias estáveis persistem mesmo com retrieval strength zero; no modelo de Wozniak, a stability torna-se indeterminada nesse ponto [F: wozniak2018twocomponents].

### Esquecimento em modelos de aluno

O Bayesian Knowledge Tracing clássico fixa em zero a probabilidade de transição do estado "sabe" para "não sabe": "In standard BKT, F = 0" — uma vez inferido que o aluno aprendeu, nem uma longa sequência de erros altera o estado [F: khajah2016deep]. Khajah, Lindsey e Mozer mostraram que permitir esquecimento (BKT+F) eleva a AUC de 0,73 para 0,83 no conjunto Assistments, respondendo pela maior parte da vantagem relatada do Deep Knowledge Tracing sobre o BKT [F: khajah2016deep]. [I] Ou seja: boa parte do "ganho" de modelos neurais sobre o BKT vem simplesmente de capturar recência/esquecimento que o BKT clássico ignora por construção. Ver `adp.kt.bayesian-knowledge-tracing` e `adp.kt.deep-knowledge-tracing`.

## Requisitos e pressupostos

- Modelos de dois componentes exigem histórico de revisões por item com carimbos de tempo; sem o "quando", só resta modelar desempenho por tentativa, como o BKT clássico [I].
- Retrievability/retrieval strength não é observável diretamente: é estimada a partir de desfechos binários (ou graduados) de tentativas de recordação, o que exige volume de dados e calibração (`adp.eval.predictive-metrics`) [I].
- A base empírica clássica usa material verbal discreto (sílabas, pares associados, fatos); a extrapolação para habilidades complexas e procedimentais é pressuposto, não dado [I].

## Vantagens e limitações

A visão de dois componentes explica com economia por que desempenho imediato engana (retrieval strength alta com storage strength baixa), por que o espaçamento ajuda e por que recuperar supera reestudar [F: bjork2023difficulties]; e fornece a base direta dos agendadores de revisão (`adp.sr.classical-algorithms`, `adp.sr.fsrs`, `adp.sr.half-life-regression`) [I]. Limitações: os componentes são latentes e as teorias são subdeterminadas pelos dados (exponencial × potência segue sem resolução decisiva [F: murre2015replication]); a evidência de replicação da curva vem de delineamentos de sujeito único [F: murre2015replication]; e as fórmulas operacionais da tradição SuperMemo não passaram por revisão por pares [F: wozniak2018twocomponentmodel] [I].

## Alternativas e comparações

Como diferentes famílias de modelo tratam o esquecimento:

| Abordagem | Representação do esquecimento | Evidência citada |
|---|---|---|
| BKT clássico | nenhuma (F = 0 por construção) | [F: khajah2016deep] |
| BKT com esquecimento (BKT+F) | transição sabe→não sabe por oportunidade | AUC 0,73→0,83 em Assistments [F: khajah2016deep] |
| Dois componentes (SuperMemo/FSRS) | R = e^(-t/S), S cresce a cada revisão bem-sucedida | praticante [F: wozniak2018twocomponentmodel]; ver `adp.sr.fsrs` |
| Regressão de meia-vida | meia-vida estimada de características do histórico | ver `adp.sr.half-life-regression` |
| Curvas agregadas (potência/log/exponencial) | função única do tempo | [F: murre2015replication] [F: wixted1991form, metadados] |

## Métricas e métodos de avaliação

Savings (percentual de esforço poupado no reaprendizado) é a medida clássica [F: ebbinghaus1885memory]; probabilidade de recordação em função do atraso é a medida moderna padrão. Comparação de formas funcionais usa critérios de informação (AIC), com a ressalva de que diferenças pequenas (<2) não decidem [F: murre2015replication]. Modelos de aluno com esquecimento são avaliados por AUC e calibração em predição de próxima resposta [F: khajah2016deep]; ver `adp.eval.predictive-metrics` e `adp.eval.evaluation-protocols`.

## Exemplo técnico independente de domínio

Esqueleto de estimador de dois componentes, seguindo a forma da literatura de praticante [F: wozniak2018twocomponentmodel]; os valores das funções `ganho_estabilidade` e `S_inicial` são o que cada algoritmo concreto (SM-x, FSRS) define e ajusta aos dados [I]:

```
estado por item: S (estabilidade, em dias), t_ultima (momento da última revisão)

retrievabilidade(item, agora):
    t = agora - item.t_ultima            # dias desde a última revisão
    retornar exp(-t / item.S)            # esquecimento exponencial dado S

ao_revisar(item, resultado, agora):
    R = retrievabilidade(item, agora)
    se resultado == sucesso:
        item.S = item.S * ganho_estabilidade(item.S, R, dificuldade)
        # ganho maior quando R está baixa; menor para S já alta  [teoria]
    senão:
        item.S = S_inicial(dificuldade)  # reaprendizagem
    item.t_ultima = agora
```

## Relações com outros conceitos

Complementa `adp.sr.spacing-and-testing-effects`, que trata dos efeitos de espaçamento e teste que estes modelos pretendem explicar e explorar. É a fundamentação teórica implementada por `adp.sr.classical-algorithms`, `adp.sr.half-life-regression` e `adp.sr.fsrs`. Relaciona-se com `adp.kt.bayesian-knowledge-tracing` (que ignora esquecimento por construção) e com `adp.lm.learner-model` (o estado de memória é uma das variáveis de um modelo de aluno).

## Lacunas e questões abertas

- Bjork e Bjork 1992 (capítulo original): não aberto — o site do laboratório Bjork na UCLA recusou conexão na sessão (ECONNREFUSED) e a cópia tentada em espelho retornou 404; entra na bibliografia só com metadados, e o conteúdo é citado pelo capítulo aberto de 2023 dos mesmos autores.
- Wixted e Ebbesen 1991: texto completo não aberto (página da editora retornou 403); metadados confirmados via Crossref; a afirmação de conteúdo aqui se limita ao abstract.
- Averell e Heathcote 2011: texto completo não aberto (repositório da Newcastle retornou 403); apenas metadados; por isso o resultado deles não é afirmado neste documento.
- Corbett e Anderson 1995 (BKT original): a cópia PDF pública localizada é digitalização sem camada de texto; a afirmação sobre ausência de esquecimento no BKT é feita via [F: khajah2016deep].
- A Tabela 3 de Murre e Dros (savings por intervalo) está publicada como imagem e não foi extraída; os valores por intervalo do sujeito moderno não são citados aqui, apenas o de 31 dias discutido no texto.
- Replicações da curva são de sujeito único; falta base multissujeito moderna com o método de savings [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ebbinghaus1885memory | academico | 2026-10-29 |
| murre2015replication | academico | 2026-10-29 |
| wixted1991form | academico (apenas metadados) | 2026-10-29 |
| averell2011form | academico (apenas metadados) | 2026-10-29 |
| bjork1992disuse | academico (apenas metadados) | 2026-10-29 |
| bjork2023difficulties | academico | 2026-10-29 |
| wozniak1995twocomponents | academico | 2026-10-29 |
| wozniak2018twocomponentmodel | tecnico (praticante) | 2026-10-29 |
| wozniak2018twocomponents | tecnico (praticante) | 2026-10-29 |
| khajah2016deep | academico | 2026-10-29 |
