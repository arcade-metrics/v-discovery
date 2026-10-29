---
id: lae.evalm.effect-size-and-replication
titulo: Tamanho de efeito, meta-análise e crise de replicação na avaliação de resultado educacional
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [cohen1988statistical, hattie2009visible, simpson2017misdirection, glass1976primary, openscience2015estimating, nosek2018preregistration]
relacoes:
  - { tipo: relacionado-a, alvo: lae.evalm.experimental-design }
termos: [effect size, tamanho de efeito, Cohen's d, meta-análise, crise de replicação, pré-registro, significância estatística, poder estatístico]
---

# Tamanho de efeito, meta-análise e crise de replicação na avaliação de resultado educacional

## Definição e terminologia

Tamanho de efeito (*effect size*) é uma medida padronizada da magnitude de uma diferença ou de uma associação, independente do tamanho da amostra — ao contrário de um valor-p, que mistura magnitude do efeito com tamanho amostral [I, com base em cohen1988statistical]. A medida mais usada para comparar duas médias é o *d* de Cohen, definido como a diferença entre as médias dos dois grupos dividida por um desvio-padrão comum (*pooled*) [F: cohen1988statistical]. Para associações entre variáveis contínuas, a medida equivalente é o coeficiente de correlação *r* [F: cohen1988statistical].

O que não é: tamanho de efeito não é significância estatística. Um resultado pode ser estatisticamente significativo (p < 0,05) com um efeito trivial, se a amostra for grande o suficiente; e pode ser um efeito substantivo sem atingir significância, se a amostra for pequena [I, com base em cohen1988statistical]. Os dois números respondem perguntas diferentes: significância pergunta "esse efeito é distinguível de zero, dado o ruído amostral?"; tamanho de efeito pergunta "o quão grande é esse efeito, em uma escala comparável entre estudos?" [I].

Meta-análise é a síntese estatística dos tamanhos de efeito de múltiplos estudos sobre a mesma pergunta, produzindo uma estimativa combinada e uma medida de quanto os estudos concordam entre si [F: glass1976primary]. O termo foi cunhado por Gene Glass em 1976, em discurso de posse na American Educational Research Association, que distinguiu três níveis de análise de dados de pesquisa: análise primária (a análise original de um estudo), análise secundária (reanálise dos dados de um estudo já existente) e meta-análise (a análise estatística de um grande conjunto de resultados de análises individuais, com o propósito de integrar os achados) [F: glass1976primary].

## Problema que resolve

Um único estudo mostrando que uma intervenção educacional "funcionou" — mesmo com desenho experimental robusto (ver `lae.evalm.experimental-design`) — não diz, por si só, se o efeito é grande o suficiente para importar na prática, nem se o efeito se replicaria em outro contexto, outra amostra, outra implementação [I]. Tamanho de efeito resolve o primeiro problema (dar uma escala comparável de magnitude); meta-análise e replicação resolvem o segundo (checar se o achado é estável através de estudos e contextos diferentes) [I].

## Fundamentos e funcionamento

### Cohen's d e as faixas de referência contestadas

Cohen propôs, no livro de 1988, faixas de referência para interpretar a magnitude de *d*: pequeno (≈ 0,2), médio (≈ 0,5) e grande (≈ 0,8) [F: cohen1988statistical]. O próprio Cohen apresentou esses valores como "critérios operacionais, recomendados para uso apenas quando não há base melhor disponível" — ou seja, como convenção de último recurso, calibrada em cima de estudos típicos das ciências sociais das décadas de 1960 e 1970, não como padrão universal [F: cohen1988statistical].

Essa ressalva do próprio autor é frequentemente perdida quando as faixas de Cohen são aplicadas, sem ajuste, à educação. John Hattie, em *Visible Learning* (2009), sintetizou mais de 800 meta-análises sobre fatores associados ao desempenho escolar e propôs um "ponto de corte" (*hinge point*) de d = 0,4 como o efeito médio típico de um ano de progresso escolar, usado como referência para separar intervenções "acima da média" de intervenções "abaixo da média" de efetividade [F: hattie2009visible]. A proposta teve grande influência em política educacional e formação de professores por oferecer um "ranking" comparável de centenas de práticas pedagógicas [I].

### Críticas metodológicas à síntese de Hattie

A crítica mais sistemática e revisada por pares localizada nesta pesquisa é a de Adrian Simpson (2017), publicada no *Journal of Education Policy*. O argumento central de Simpson é que tamanhos de efeito padronizados, como o *d* de Cohen, não são diretamente comparáveis nem combináveis entre estudos a menos que presunções fortes se sustentem — sobre a equivalência dos grupos de comparação, sobre a amplitude da população amostrada e sobre o desenho do instrumento de medição — e essas presunções são seguidamente violadas na literatura educacional [F: simpson2017misdirection]. Segundo Simpson, um *d* maior não indica necessariamente maior impacto educacional real: áreas no topo de rankings como o de Hattie tendem a ser aquelas em que os pesquisadores conseguem desenhar experimentos mais sensíveis (menor variância dentro do grupo), não necessariamente aquelas com maior efeito substantivo [F: simpson2017misdirection]. A conclusão de Simpson é que políticas públicas e recursos correm o risco de ser mal direcionados quando decisões se apoiam em rankings de tamanhos de efeito combinados sem checar essas condições [F: simpson2017misdirection].

Outras críticas, levantadas em discussões públicas sobre a obra de Hattie (não confirmadas nesta sessão em fonte revisada por pares — registradas como "não verificado"), apontam: (a) erros de cálculo em conversões de tamanho de efeito para "common language effect size" atribuídos a Higgins e Simpson (2011), Topphol (2011) e Bergeron e Rivard (2017); (b) a ideia de que o hinge point de 0,4 ignoraria variação sistemática do tamanho de efeito por idade do aluno; e (c) a prática de converter *d* em "anos de progresso escolar" como uma equivalência que a métrica, por si, não sustenta. Como essas críticas não foram localizadas nesta sessão em publicação primária revisada por pares, ficam registradas como lacuna, não como fato estabelecido.

### Meta-análise como agregação de evidência

A lógica da meta-análise é tratar cada estudo individual como uma observação de um tamanho de efeito "verdadeiro" (possivelmente variável entre contextos), e combinar essas observações ponderando por precisão (tipicamente, pelo inverso da variância de cada estimativa), produzindo uma estimativa agregada e um intervalo de confiança mais estreito do que qualquer estudo isolado teria [I, com base em glass1976primary]. O valor da meta-análise está em reduzir a dependência do julgamento sobre qualquer evidência educacional a um único estudo — mas isso só é válido quando os estudos agregados são de fato comparáveis na forma apontada por Simpson: populações, desenhos e medidas suficientemente semelhantes para que combinar seus tamanhos de efeito faça sentido substantivo, não apenas aritmético [F: simpson2017misdirection].

### A crise de replicação

A chamada "crise de replicação" nas ciências sociais e comportamentais ficou amplamente documentada com o projeto *Reproducibility Project: Psychology*, publicado pela Open Science Collaboration em 2015 na revista *Science*. O projeto replicou 100 estudos experimentais e correlacionais de três periódicos de psicologia, usando amostras maiores e, quando disponíveis, os materiais originais [F: openscience2015estimating]. Os resultados: enquanto 97% dos estudos originais reportaram resultado estatisticamente significativo, apenas 36% das replicações o fizeram; o tamanho de efeito médio das replicações (r = 0,197) foi cerca de metade do tamanho de efeito médio dos estudos originais (r = 0,403) [F: openscience2015estimating]. Apenas 47% dos tamanhos de efeito originais caíram dentro do intervalo de confiança de 95% da respectiva replicação [F: openscience2015estimating]. O melhor preditor de sucesso da replicação não foram características das equipes, mas a força da evidência original — efeitos originalmente mais fortes e com valor-p mais baixo tenderam a replicar com mais frequência [F: openscience2015estimating].

Embora esse projeto tenha sido conduzido em psicologia, não em educação especificamente, sua implicação metodológica se estende à pesquisa educacional pelas práticas que compartilham: amostras moderadas, múltiplas comparações possíveis, flexibilidade analítica pós-hoc e maior publicação de resultados positivos do que de resultados nulos (viés de publicação) [I]. A implicação prática para avaliação de produto ou método educacional é direta: um único estudo mostrando ganho de aprendizagem, mesmo com desenho experimental adequado, tem uma probabilidade não desprezível de não replicar com a mesma magnitude em uma segunda tentativa independente — a inflação otimista de efeitos originais é um padrão observado, não uma exceção [I, com base em openscience2015estimating].

### Pré-registro como mitigação

Pré-registro é a prática de documentar publicamente, antes de coletar ou analisar os dados, as hipóteses, o desenho, as variáveis e o plano de análise estatística de um estudo [F: nosek2018preregistration]. Nosek, Ebersole, DeHaven e Mellor (2018) argumentam que a credibilidade da pesquisa é corroída quando achados exploratórios (descobertos ao explorar os dados após coletados) são apresentados como se fossem previsões confirmatórias — um problema agravado por viés de retrospecto (*hindsight bias*), que faz um padrão encontrado post hoc parecer, psicologicamente, como se tivesse sido previsto [F: nosek2018preregistration]. O pré-registro resolve isso ao fixar o que era previsão e o que era exploração antes de os resultados serem conhecidos, permitindo que o leitor avalie a confirmação de uma hipótese sem o risco de inflação por graus de liberdade do pesquisador (testar múltiplas variáveis, cortes ou modelos até encontrar significância) [F: nosek2018preregistration]. Uma crítica posterior ao artigo de Nosek et al., citada por eles mesmos na literatura (Ledgerwood 2018, não verificada diretamente nesta sessão), destaca que pré-registrar previsões teóricas (para permitir falseabilidade) e pré-registrar planos de análise (para controlar taxa de erro tipo I) são dois objetivos distintos que a prática às vezes confunde — registrado aqui como nuance, não como consenso fechado.

Para a avaliação de produtos e métodos educacionais, pré-registro é diretamente aplicável tanto a RCTs quanto a A/B tests (ver `lae.evalm.experimental-design`): declarar, antes de olhar os dados, qual é a métrica primária de sucesso, qual o tamanho de amostra planejado e qual a regra de parada evita o risco de, diante de um resultado nulo na métrica original, buscar outra métrica até achar uma significativa e reportá-la como se fosse a pergunta original [I].

## Algoritmos e modelos relevantes

Fórmula do *d* de Cohen para duas amostras independentes, com s_pooled o desvio-padrão combinado ponderado pelos tamanhos de amostra [F: cohen1988statistical]:

```
d = (M1 − M2) / s_pooled
```

Estrutura geral de uma meta-análise de efeitos aleatórios (forma conceitual, não a fórmula completa de estimação de variância entre estudos) [I, com base em glass1976primary]:

```
para cada estudo i: observar efeito_i e erro-padrão_i
peso_i = 1 / variancia_i          # estudos mais precisos pesam mais
efeito_combinado = soma(peso_i * efeito_i) / soma(peso_i)
heterogeneidade = checar se efeito_i variam mais do que o esperado só por ruído amostral
                   (se sim, os estudos podem não ser comparáveis o bastante para combinar — Simpson, 2017)
```

## Requisitos e pressupostos

- Comparar tamanhos de efeito entre estudos pressupõe grupos de comparação equivalentes, amplitude de população semelhante e instrumentos de medição com foco e precisão comparáveis; quando isso não se sustenta, o tamanho de efeito reflete a sensibilidade do desenho tanto quanto o fenômeno medido [F: simpson2017misdirection].
- Interpretar um *d* isolado exige contexto da área e do tipo de intervenção — Cohen já advertia contra aplicar suas faixas de forma mecânica fora do domínio em que foram calibradas [F: cohen1988statistical].
- Confiar em um único estudo como evidência de eficácia pressupõe implicitamente que o estudo replicaria; a evidência empírica da crise de replicação torna essa suposição frágil por padrão, não por exceção [F: openscience2015estimating].
- Pré-registro só mitiga inflação de achados exploratórios se o plano registrado for de fato seguido, e se desvios do plano forem declarados explicitamente na publicação [I, com base em nosek2018preregistration].

## Vantagens e limitações

| Prática | Vantagem | Limitação |
|---|---|---|
| Tamanho de efeito (d, r) | Comparável entre estudos de tamanhos de amostra diferentes; separa magnitude de significância [F: cohen1988statistical] | Faixas de referência (pequeno/médio/grande) são convenção, não lei; sensíveis ao desenho do estudo, não só ao fenômeno [F: simpson2017misdirection] |
| Meta-análise | Reduz dependência de um único estudo; aumenta precisão da estimativa combinada [I, com base em glass1976primary] | Combinar estudos heterogêneos pode produzir uma média sem significado substantivo [F: simpson2017misdirection] |
| Replicação independente | Evidência direta de estabilidade do efeito fora do contexto original [F: openscience2015estimating] | Custosa; raramente financiada ou publicada com o mesmo destaque do estudo original (viés de publicação) [I] |
| Pré-registro | Reduz inflação de achados por graus de liberdade do pesquisador [F: nosek2018preregistration] | Não impede um desenho de baixa qualidade; é garantia de transparência, não de validade [I] |

## Alternativas e comparações

A tabela acima cobre a comparação central. É importante notar que essas práticas não competem entre si — tamanho de efeito, meta-análise, replicação e pré-registro são complementares, e a ausência de qualquer uma delas enfraquece a confiança no conjunto: um tamanho de efeito grande em um único estudo não pré-registrado, sem tentativa de replicação, é a situação de menor confiança possível, mesmo com desenho experimental impecável [I].

## Métricas e métodos de avaliação

Para julgar se um corpo de evidência sobre um método ou produto educacional é confiável, a pergunta não é apenas "qual o *d* reportado?", mas: o tamanho de efeito foi calculado com grupos de comparação equivalentes? Existe mais de um estudo independente apontando na mesma direção e magnitude aproximada? O estudo foi pré-registrado, ou os resultados reportados podem ter sido selecionados entre várias análises possíveis? [I, sintetizado a partir de simpson2017misdirection, openscience2015estimating e nosek2018preregistration].

## Exemplo técnico independente de domínio

```
dado: um estudo reporta d = 0.45 para uma intervenção
perguntar:
  1. o grupo de comparação era equivalente (randomizado ou quase-experimental válido)?
     -> ver lae.evalm.experimental-design
  2. esse d é consistente com outros estudos independentes da mesma intervenção?
     -> se não houver outro estudo: tratar como evidência preliminar, não conclusiva
     -> se houver vários: considerar meta-análise, checando heterogeneidade
  3. o estudo foi pré-registrado?
     -> se não: considerar risco de inflação por graus de liberdade do pesquisador
  4. o instrumento de medição do resultado é comparável ao de estudos similares?
     -> se não: cautela ao comparar a magnitude do d com benchmarks de outras áreas
decisão: nenhuma dessas perguntas, isoladamente, invalida o achado;
         a ausência de várias delas ao mesmo tempo deveria reduzir a confiança na decisão de adotar a intervenção
```

## Relações com outros conceitos

Este documento trata da leitura estatística do efeito encontrado por um estudo; o desenho que produz esse efeito — RCT, A/B test, desenhos quase-experimentais e suas ameaças à validade — está em `lae.evalm.experimental-design`, com o qual este documento mantém relação de complementaridade: um bom desenho sem leitura criteriosa do tamanho de efeito, ou um tamanho de efeito bem interpretado a partir de um desenho fraco, são igualmente insuficientes para decisão.

## Lacunas e questões abertas

- As críticas específicas a erros de cálculo na obra de Hattie (atribuídas a Higgins e Simpson 2011, Topphol 2011, Bergeron e Rivard 2017) não foram verificadas em fonte primária nesta sessão; aparecem apenas em fontes secundárias (blogs educacionais). Registradas como "não verificado" — pesquisa futura deveria tentar acessar essas publicações diretamente.
- Não foi localizada, nesta sessão, uma meta-análise ou revisão específica sobre a taxa de replicação de estudos de eficácia de produtos educacionais digitais (em contraste com psicologia em geral ou com intervenções pedagógicas tradicionais); a extrapolação da crise de replicação de psicologia para este subcampo é uma inferência razoável, mas não uma evidência direta — registrada como lacuna.
- A crítica de Ledgerwood (2018) ao artigo de pré-registro de Nosek et al. foi mencionada apenas de forma indireta, a partir de resumo de busca, sem acesso ao texto completo; fica como pendência de verificação.
- O DOI do artigo de Glass (1976) não foi localizado nesta sessão (periódico da época pode não ter DOI retroativo atribuído); a citação se apoia em metadados consistentes de catálogo e da James Lind Library, não em acesso ao PDF original.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| cohen1988statistical | academico | 2026-10-29 |
| hattie2009visible | academico | 2026-10-29 |
| simpson2017misdirection | academico | 2026-10-29 |
| glass1976primary | academico (metadados; DOI não localizado) | 2026-10-29 |
| openscience2015estimating | academico | 2026-10-29 |
| nosek2018preregistration | academico | 2026-10-29 |
