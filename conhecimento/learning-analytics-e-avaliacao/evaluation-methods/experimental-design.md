---
id: lae.evalm.experimental-design
titulo: Desenho experimental e quase-experimental para avaliação de resultado educacional
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [shadishcookcampbell2002experimental, ies2022wwchandbook, thistlethwaitecampbell1960regression, cardkrueger1994minimum, kohavitangxu2020trustworthy, eef2026randomisationlevel]
relacoes:
  - { tipo: relacionado-a, alvo: lae.evalm.effect-size-and-replication }
termos: [randomized controlled trial, RCT, grupo de controle, desenho quase-experimental, regressão descontínua, diferenças em diferenças, validade interna, validade externa, A/B testing, unidade de randomização, contaminação, SUTVA]
---

# Desenho experimental e quase-experimental para avaliação de resultado educacional

## Definição e terminologia

Desenho experimental é o arranjo de um estudo em que o pesquisador atribui aleatoriamente unidades (alunos, turmas, escolas) a uma condição de tratamento (a intervenção, o produto, o método) ou a uma condição de controle, de modo que a comparação entre os grupos permita atribuir causalidade à diferença de resultado observada [I, com base em shadishcookcampbell2002experimental]. Quando essa atribuição é aleatória, o desenho é chamado de *randomized controlled trial* (RCT) ou experimento randomizado [F: shadishcookcampbell2002experimental].

Desenho quase-experimental compartilha a lógica de comparar um grupo exposto à intervenção com um grupo não exposto, mas sem atribuição aleatória — a separação entre os grupos vem de alguma outra regra (quem se inscreveu, quem já usava o produto, um ponto de corte administrativo) [F: shadishcookcampbell2002experimental]. Shadish, Cook e Campbell tratam ambos os desenhos sob o guarda-chuva de "inferência causal generalizada": o objetivo comum é estimar o efeito causal de um tratamento sobre um resultado, e a diferença está em quão bem cada desenho descarta explicações alternativas para a diferença observada [F: shadishcookcampbell2002experimental].

*A/B testing* é o nome, consolidado em produtos digitais, para um experimento controlado randomizado aplicado à comparação de duas (ou mais) variantes de um produto ou de uma experiência — é um RCT, não uma categoria metodológica à parte [I, com base em kohavitangxu2020trustworthy]. Quando aplicado a um produto educacional, a variante A e a variante B costumam ser versões de uma funcionalidade, de um roteiro instrucional ou de uma política de prática, e o resultado medido pode ser um indicador de aprendizagem (ver `learning-analytics-e-avaliacao/indicators/`) ou um proxy comportamental (conclusão, retenção, tempo em tarefa) [I].

O que não é: um desenho quase-experimental não é "um experimento mais fraco" em grau indiferenciado — é uma família de desenhos específicos, cada um com sua própria lógica de identificação do efeito (ver seção de Algoritmos e modelos relevantes), e alguns, sob certas condições, aproximam-se da validade de um RCT [F: shadishcookcampbell2002experimental]. Também não deve ser confundido com um estudo observacional sem nenhum grupo de comparação (estudo pré-pós de um único grupo), que Shadish, Cook e Campbell classificam como o desenho mais fraco da família quase-experimental justamente por não isolar a intervenção de outras mudanças concorrentes no tempo [F: shadishcookcampbell2002experimental].

## Problema que resolve

Observar que o desempenho de alunos melhorou depois de usar um produto ou método não implica que o produto ou método causou a melhora — a melhora pode vir de maturação, de outras intervenções simultâneas, de regressão à média, ou de os alunos que optaram por usar o produto já serem diferentes dos que não optaram (viés de seleção) [I, com base em shadishcookcampbell2002experimental]. Desenho experimental e quase-experimental existem para que seja possível responder, com confiança quantificável, a uma pergunta causal — "este resultado teria acontecido sem a intervenção?" — e não apenas descrever uma correlação [I].

No ciclo de um produto educacional, essa pergunta aparece tipicamente em dois momentos: quando se decide se uma intervenção pedagógica (um método, um currículo, uma prática de ensino) tem evidência de eficácia antes de ser incorporada; e quando se decide, de forma contínua, se uma mudança específica no produto (uma funcionalidade, um fluxo, um algoritmo de recomendação) melhora um resultado de interesse — esta segunda situação é o domínio do A/B testing [I].

## Fundamentos e funcionamento

### Grupos de controle e lógica da comparação

A randomização busca produzir, em expectativa, grupos de tratamento e controle equivalentes em todas as características observáveis e não observáveis relevantes antes da intervenção, de modo que qualquer diferença de resultado após a intervenção possa ser atribuída a ela [F: shadishcookcampbell2002experimental]. O grupo de controle pode receber nenhuma intervenção, uma intervenção "de costume" (business as usual) ou uma intervenção alternativa (comparação ativa) — a escolha muda a interpretação do efeito estimado: comparação contra nada estima o efeito absoluto; comparação contra uma alternativa estima o efeito incremental [I].

### Ameaças à validade interna

Validade interna é o grau de confiança de que a relação observada entre tratamento e resultado é causal, dentro do próprio estudo [F: shadishcookcampbell2002experimental]. Shadish, Cook e Campbell catalogam as principais ameaças, entre elas [F: shadishcookcampbell2002experimental]:

- **Seleção**: os grupos diferem sistematicamente antes da intervenção (central em desenhos sem randomização).
- **Maturação**: mudanças que ocorreriam de qualquer forma com o tempo (alunos amadurecem, aprendem fora da intervenção).
- **História**: eventos externos concorrentes no período do estudo afetam os grupos de forma desigual.
- **Regressão à média**: unidades selecionadas por terem desempenho extremo tendem a se aproximar da média na medição seguinte, independentemente de tratamento.
- **Atrito diferencial (mortality)**: perda de participantes diferente entre os grupos, correlacionada ao resultado.
- **Testagem e instrumentação**: o próprio ato de medir, ou mudanças no instrumento de medição entre as ondas, afeta o resultado observado.
- **Difusão ou imitação do tratamento**: o grupo de controle é exposto, ainda que parcialmente, ao tratamento (ver contaminação, abaixo).

### Ameaças à validade externa

Validade externa é o grau em que o efeito encontrado se generaliza para outras pessoas, contextos, momentos e operacionalizações da intervenção e do resultado, além dos estudados [F: shadishcookcampbell2002experimental]. Um RCT com validade interna alta (boa randomização, baixo atrito) ainda pode ter validade externa baixa se a amostra, o contexto institucional ou a forma de implementação da intervenção forem atípicos [I, com base em shadishcookcampbell2002experimental]. Os dois tipos de validade frequentemente competem por recursos de desenho: maior controle experimental (mais homogeneidade da amostra, ambiente mais controlado) tende a reduzir a variação que ameaça a validade interna, mas também reduz a diversidade de contextos para a qual o resultado generaliza [I].

### Desenhos quase-experimentais quando a randomização não é viável

Randomizar o acesso a uma intervenção educacional nem sempre é possível ou ético — por exemplo, quando a intervenção já está em uso disseminado, quando negar o acesso a um grupo levanta objeção institucional, ou quando a unidade de decisão (a escola, o sistema) já escolheu adotar ou não. Nesses casos, desenhos quase-experimentais tentam reconstruir uma comparação válida sem atribuição aleatória [I, com base em shadishcookcampbell2002experimental]:

- **Regressão descontínua (regression discontinuity, RD)**: quando a atribuição à intervenção segue uma regra de corte em uma variável contínua observável (uma nota mínima para entrar em um programa de reforço, um escore de risco para ser alocado a um acompanhamento), unidades logo acima e logo abaixo do corte são comparáveis, e a diferença de resultado no entorno do corte estima o efeito local da intervenção [F: thistlethwaitecampbell1960regression]. O desenho foi introduzido por Thistlethwaite e Campbell em 1960 justamente em um contexto educacional — o efeito de um reconhecimento por mérito atribuído por corte de nota em concurso — e e permanece, segundo os próprios autores da tradição, um desenho concentrado majoritariamente em aplicações educacionais [F: thistlethwaitecampbell1960regression].
- **Diferenças em diferenças (difference-in-differences, DiD)**: compara a mudança no resultado ao longo do tempo entre um grupo exposto à intervenção e um grupo de comparação não exposto, pressupondo que, na ausência da intervenção, as duas trajetórias teriam evoluído em paralelo ("tendências paralelas") [I, com base em cardkrueger1994minimum]. O exemplo canônico do método — fora do domínio educacional, mas estrutural para entender a lógica — é o estudo de Card e Krueger sobre o efeito do salário mínimo no emprego em restaurantes de fast-food, comparando Nova Jersey (que elevou o salário mínimo) com a Pensilvânia vizinha (que não elevou), antes e depois da mudança [F: cardkrueger1994minimum]. Uma reavaliação posterior, usando dados de folha de pagamento em vez de levantamento telefônico, chegou a uma conclusão diferente da original, o que ilustra como a qualidade da medição do resultado condiciona a robustez de uma DiD [I, com base em cardkrueger1994minimum].
- **Desenho pré-pós com grupo de comparação não equivalente**: mede o resultado antes e depois da intervenção tanto no grupo tratado quanto em um grupo de comparação escolhido por conveniência ou pareamento, sem garantia de tendências paralelas nem de equivalência inicial; é mais fraco que DiD e RD porque não tem uma fonte de identificação do efeito tão clara, mas é o desenho quase-experimental mais acessível quando não há variável de corte nem séries temporais longas [F: shadishcookcampbell2002experimental].

O *What Works Clearinghouse* (WWC) do Institute of Education Sciences dos EUA formaliza essa hierarquia em seu manual de padrões de evidência: um RCT bem implementado pode receber a classificação mais alta ("atende aos padrões sem ressalvas"), mas um desenho quase-experimental, mesmo bem conduzido, está limitado a uma classificação intermediária ("atende aos padrões com ressalvas") [F: ies2022wwchandbook]. Essa hierarquia reflete o julgamento da área de que nenhum ajuste estatístico em um quase-experimento elimina totalmente a incerteza sobre equivalência inicial dos grupos que a randomização resolve por construção [I].

### A/B testing como caso particular

Um A/B test aplicado a um produto educacional é estruturalmente um RCT: unidades são aleatoriamente designadas a variantes, e a diferença de métricas entre variantes estima o efeito causal da mudança [I, com base em kohavitangxu2020trustworthy]. Kohavi, Tang e Xu descrevem o valor desse desenho em ambientes de produto justamente pela escala com que pode ser repetido — organizações de tecnologia que operam dezenas de milhares de experimentos controlados por ano usam o método para decidir, de forma incremental e contínua, pequenas mudanças de produto [F: kohavitangxu2020trustworthy]. Isso diferencia o A/B testing de produto do RCT acadêmico clássico mais em escala e cadência do que em lógica inferencial [I].

### Unidade de randomização: aluno vs. turma

Uma decisão central de desenho em contexto educacional é a unidade de randomização — o nível em que a atribuição aleatória é feita. Randomizar no nível do aluno individual, dentro de uma mesma turma ou escola, produz mais poder estatístico para o mesmo tamanho de amostra, porque há mais unidades independentes [F: eef2026randomisationlevel]. Mas alunos de uma mesma turma interagem: conversam, compartilham material, o professor pode (intencional ou inadvertidamente) misturar práticas entre os dois grupos — o que gera **contaminação** (ou difusão do tratamento) entre tratamento e controle [F: eef2026randomisationlevel].

Formalmente, contaminação é uma violação da *Stable Unit Treatment Value Assumption* (SUTVA): a suposição, necessária para a inferência causal padrão, de que o resultado de uma unidade depende apenas da condição a que ela própria foi atribuída, não da condição atribuída a outras unidades [I, com base em eef2026randomisationlevel]. Quando alunos de turmas vizinhas trocam informação sobre a intervenção, essa suposição é violada e o efeito estimado tende a ser enviesado para baixo (porque o grupo de controle recebe parte do tratamento) [I].

Randomizar no nível da turma ou da escola (randomização em cluster) reduz o risco de contaminação, porque a unidade inteira recebe uma única condição, mas custa poder estatístico — a correlação intraclasse entre alunos de uma mesma turma faz com que cada aluno adicional contribua menos informação independente do que contribuiria sob randomização individual, exigindo amostras maiores (mais turmas) e ajuste da análise estatística pelo efeito de cluster [F: eef2026randomisationlevel]. Não existe um desenho universalmente correto: a escolha depende de quão plausível é a contaminação para aquela intervenção específica e de quanto poder estatístico o orçamento de amostra permite perder [F: eef2026randomisationlevel].

## Requisitos e pressupostos

- Para um RCT: atribuição verdadeiramente aleatória, ocultação da alocação antes do início do tratamento, e adesão (ou ao menos mensuração da não adesão) ao grupo designado [I, com base em shadishcookcampbell2002experimental].
- Para RD: a variável de corte não pode ser manipulável pelos participantes (alguém não pode se colocar estrategicamente de um lado ou outro do corte) e deve haver densidade suficiente de observações perto do corte [I, com base em thistlethwaitecampbell1960regression].
- Para DiD: a suposição de tendências paralelas — sem a intervenção, grupo tratado e grupo de comparação teriam evoluído de forma similar no período — não é testável diretamente para o período pós-tratamento, apenas sugerida por tendências pré-tratamento semelhantes [I, com base em cardkrueger1994minimum].
- Para qualquer desenho com grupo de comparação não randomizado: a ausência de viés de seleção não observável precisa ser justificada pelo contexto, não pode ser assumida por padrão [F: shadishcookcampbell2002experimental].
- SUTVA (ausência de interferência entre unidades) precisa ser plausível para a unidade de randomização escolhida; quando não é, a unidade de randomização deve subir de nível (de aluno para turma, de turma para escola) [I, com base em eef2026randomisationlevel].

## Vantagens e limitações

| Desenho | Vantagem principal | Limitação principal |
|---|---|---|
| RCT (randomização individual) | Maior poder estatístico; elimina viés de seleção observável e não observável por construção [F: shadishcookcampbell2002experimental] | Vulnerável a contaminação quando unidades interagem; nem sempre viável ou ético [I] |
| RCT (randomização em cluster) | Reduz contaminação entre unidades que interagem [F: eef2026randomisationlevel] | Exige amostra maior; análise deve ajustar correlação intraclasse [F: eef2026randomisationlevel] |
| Regressão descontínua | Boa aproximação de um experimento local perto do corte, sem precisar randomizar [F: thistlethwaitecampbell1960regression] | Efeito estimado é local (vale perto do corte, não necessariamente para toda a população); exige variável de corte contínua e não manipulável [I] |
| Diferenças em diferenças | Usa dados de antes e depois para controlar diferenças fixas entre grupos [I, com base em cardkrueger1994minimum] | Depende da suposição não testável de tendências paralelas; sensível à qualidade da medição do resultado [F: cardkrueger1994minimum] |
| Pré-pós com grupo de comparação não equivalente | Mais simples de implementar com dados já existentes [F: shadishcookcampbell2002experimental] | Maior exposição a viés de seleção e a ameaças de história e maturação diferenciais [F: shadishcookcampbell2002experimental] |

## Alternativas e comparações

A tabela acima cobre a comparação central do domínio. Vale notar que os desenhos não são mutuamente exclusivos: um RCT pode ser complementado por uma análise de regressão descontínua quando há não adesão ao protocolo de randomização (alguns alunos do grupo controle acessam a intervenção por fora do estudo), e uma DiD pode ser combinada com pareamento prévio dos grupos de comparação para reduzir a dependência da suposição de tendências paralelas [I].

## Métricas e métodos de avaliação

A métrica central para julgar o desenho em si (não o efeito encontrado) é o grau de controle das ameaças à validade interna listadas acima [F: shadishcookcampbell2002experimental]. O WWC operacionaliza esse julgamento em um protocolo de classificação (atende sem ressalvas / atende com ressalvas / não atende), aplicado estudo a estudo, considerando randomização, atrito e equivalência de linha de base [F: ies2022wwchandbook]. O tamanho do efeito encontrado por qualquer um desses desenhos é tratado em `lae.evalm.effect-size-and-replication`, que também cobre a necessidade de replicação para confiar no resultado de um único estudo.

## Exemplo técnico independente de domínio

Esboço de protocolo de decisão para escolher desenho, independente da intervenção específica:

```
dado: uma intervenção candidata e um resultado de interesse
se randomização da unidade individual é eticamente e operacionalmente viável
   e a interação entre unidades tratadas e não tratadas é improvável:
    usar RCT com randomização individual
senão se randomização é viável mas a interação entre unidades é provável:
    usar RCT com randomização em cluster (turma/escola)
    ajustar tamanho de amostra para correlação intraclasse
senão se existe uma regra de corte contínua e não manipulável que determina acesso:
    usar regressão descontínua ao redor do corte
senão se existem dados de antes/depois para um grupo tratado e um grupo de comparação plausível:
    usar diferenças em diferenças
    verificar tendências pré-tratamento paralelas antes de interpretar o resultado
senão:
    usar pré-pós com grupo de comparação não equivalente
    reportar explicitamente as ameaças à validade interna não controladas
```

## Relações com outros conceitos

Este documento trata do desenho da coleta de evidência causal; o tratamento estatístico do resultado obtido — tamanho de efeito, significância, replicação e pré-registro — está em `lae.evalm.effect-size-and-replication`, com o qual este documento tem relação de complementaridade (um desenho bem feito ainda exige uma leitura criteriosa do efeito encontrado).

## Lacunas e questões abertas

- Não foi possível acessar o texto integral de Shadish, Cook e Campbell (2002) nesta sessão; as afirmações atribuídas à obra vêm de descrições consistentes em múltiplos registros de catálogo de biblioteca e são, no mínimo, representativas do consenso sobre o conteúdo do livro, mas a citação de página específica não foi possível — registrado como lacuna.
- O protocolo exato de classificação de evidência do WWC versão 5.0 (critérios numéricos de atrito aceitável, equivalência de linha de base) não foi verificado em detalhe nesta sessão; o PDF do manual não foi lido integralmente, apenas sua página de apresentação. Fica como lacuna para aprofundamento futuro.
- Não foi encontrada, nesta sessão, uma meta-análise ou revisão sistemática específica comparando o poder estatístico de randomização por aluno vs. por turma em intervenções educacionais de learning analytics ou produtos digitais (distinto de intervenções pedagógicas tradicionais); a seção sobre unidade de randomização generaliza a partir de orientação metodológica geral (EEF) mais do que de evidência quantitativa direta — "não verificado" para o caso específico de produtos digitais.
- A relação entre A/B testing de produto e os padrões de evidência do WWC (se um A/B test de produto educacional poderia, em princípio, ser avaliado pelos mesmos critérios) não foi explorada em fonte alguma consultada; é uma questão em aberto.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| shadishcookcampbell2002experimental | academico (metadados de catálogo; texto integral não acessado) | 2026-10-29 |
| ies2022wwchandbook | normativo | 2026-10-29 |
| thistlethwaitecampbell1960regression | academico | 2026-10-29 |
| cardkrueger1994minimum | academico | 2026-10-29 |
| kohavitangxu2020trustworthy | academico | 2026-10-29 |
| eef2026randomisationlevel | secundario | 2026-10-29 |
