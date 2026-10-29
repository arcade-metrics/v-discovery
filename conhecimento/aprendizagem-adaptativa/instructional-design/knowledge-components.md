---
id: adp.id.knowledge-components
titulo: Knowledge component
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [koedinger2012kli, vanlehn2006behavior, cen2005lfa, cen2006lfa, liu2017closing, tatsuoka1983rulespace, datashop2026kcmodels, datashop2026about]
relacoes:
  - { tipo: parte-de, alvo: adp.id.kli-framework }
  - { tipo: depende-de, alvo: adp.id.kli-framework }
  - { tipo: complementa, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
termos: [knowledge component, KC, Q-matrix, cognitive model, Learning Factors Analysis, LFA, Additive Factors Model, difficulty factor, DataShop, closing the loop]
---

# Knowledge component

## Definição e terminologia

Um **knowledge component (KC)** é definido pelo KLI framework como "uma unidade adquirida de função ou estrutura cognitiva que pode ser inferida a partir do desempenho em um conjunto de tarefas relacionadas" [F: koedinger2012kli]. Essas tarefas são os *Assessment Events* do framework (ver `adp.id.kli-framework`) [F: koedinger2012kli]. Os autores usam "Knowledge Component" deliberadamente como termo guarda-chuva para generalizar sobre termos diversos usados para descrever peças de cognição ou conhecimento — regra de produção, esquema, misconception, "facet" — assim como termos cotidianos como conceito, princípio, fato ou habilidade [F: koedinger2012kli]. VanLehn, de forma convergente, define um KC como "um conceito, princípio, fato, etc. do domínio da tarefa; qualquer fragmento da informação persistente e específica do domínio que deve ser usado para realizar tarefas" [F: vanlehn2006behavior], e nota que, apesar das conotações da palavra "conhecimento", um KC pode ser incorreto — uma misconception que os instrutores preferem que o estudante não aplique [F: vanlehn2006behavior].

Na literatura de modelagem cognitiva aplicada a tutores, um KC model (o conjunto de KCs de um domínio e seu mapeamento para os passos de tarefas) é frequentemente chamado, de forma alternativa, de **Q-matrix** [F: liu2017closing]. O termo tem origem na abordagem *rule space* de Tatsuoka (1983), que usa uma matriz de atributos (itens × atributos cognitivos) para diagnosticar misconceptions a partir de padrões de resposta em teoria de resposta ao item [F: tatsuoka1983rulespace, metadados]. O que um KC não é: não é o passo observável em si (o *step*, na terminologia de VanLehn), que é um evento de interface físico e observável, enquanto o KC e sua aplicação (o *learning event*) são mentais e não observáveis diretamente [F: vanlehn2006behavior].

## Problema que resolve

Um domínio de ensino não é uma lista plana de tópicos; o desempenho do estudante varia tarefa a tarefa por razões que precisam ser nomeadas e contadas para que um sistema (ou um pesquisador) possa agir sobre elas — dar um hint específico, escolher a próxima tarefa, estimar domínio. O KC resolve o problema de granularidade: decompor conhecimento em unidades que podem ser individualmente rastreadas, contadas e usadas como base de inferência sobre o que o estudante sabe [F: vanlehn2006behavior]. Sem essa decomposição comum, knowledge tracing, sequenciamento e desenho instrucional usariam vocabulários incompatíveis entre si.

## Fundamentos e funcionamento

### Escala temporal e granularidade

Muitos KCs descrevem processos mentais situados aproximadamente no nível de *unit task* das escalas temporais de ação humana de Newell: tarefas unitárias duram cerca de 10 segundos e são essencialmente os nós-folha, os menores passos na decomposição de uma tarefa de raciocínio — a aplicação de um único operador em um espaço de resolução de problemas [F: koedinger2012kli]. KCs que operam em uma dada tarefa são hierárquicos, o que coloca o problema de como focar nos componentes certos para uma dada situação de aprendizagem; a estratégia do KLI framework é focar no nível do componente em que o estudante novato comete erros, tratando níveis inferiores (já dominados pela população-alvo) como atômicos [F: koedinger2012kli]. VanLehn ilustra a ambiguidade de granularidade com o mesmo passo algébrico podendo ser modelado como um único learning event grosso ou como uma sequência de vários learning events finos, dependendo dos objetivos instrucionais do projetista: se o sistema precisa detectar e dar feedback específico sobre erro de arredondamento, precisa da análise fina; caso contrário, a análise grossa basta [F: vanlehn2006behavior].

### Taxonomia de KCs no KLI framework

O KLI framework caracteriza KCs por quatro distinções que cortam domínios [F: koedinger2012kli]:

1. **Generalidade da condição de aplicação**: constante (um único padrão único ao qual o KC se aplica, como em pares associados) ou variável (múltiplos padrões possíveis, como em categorias, regras, esquemas ou princípios) [F: koedinger2012kli].
2. **Generalidade da resposta**: constante (um valor único, como um rótulo de categoria) ou variável (depende da informação extraída da condição) [F: koedinger2012kli].
3. **Se a relação é verbal ou não-verbal**.
4. **Até que ponto o KC pode ser racionalizado** (tem uma justificativa subjacente).

Cruzando essas dimensões, a taxonomia produz rótulos comuns: condição constante + resposta constante + não-verbal = *associação*; condição constante + resposta constante + verbal = *fato*; condição variável + resposta constante + não-verbal = *categoria*; condição variável + resposta constante + verbal = *conceito*; condição variável + resposta variável + não-verbal = *produção, esquema ou habilidade*; condição variável + resposta variável + verbal sem racionale = *regra ou plano*; condição variável + resposta variável + verbal com racionale = *princípio, regra ou modelo* [F: koedinger2012kli]. Essas propriedades definem, em primeira aproximação, uma noção de complexidade: KCs com condições e respostas variáveis, operando em escala temporal mais longa, são mais complexos do que KCs constantes de escala curta [F: koedinger2012kli]. O formato condição-resposta enfatiza que saber não é só saber o quê ou saber como, mas saber quando — aprender as condições de aplicação (o "quando") pode ser mais difícil do que aprender as respostas possíveis (o "quê") [F: koedinger2012kli].

### Descoberta e refinamento de modelos cognitivos: Learning Factors Analysis

A escolha de quais KCs compõem o modelo cognitivo de um domínio tradicionalmente vinha de brainstorming e refinamento iterativo entre especialistas de conteúdo, cientistas cognitivos e programadores — modelos de "primeira tentativa" que a experiência mostra serem melhoráveis [F: cen2005lfa]. **Learning Factors Analysis (LFA)**, de Cen, Koedinger e Junker (2006), automatiza parte desse refinamento: parte de um modelo cognitivo base (um conjunto de "skills"/KCs), aplica operadores de mutação — *split* (dividir uma skill em várias, segundo um fator de dificuldade), *add* (adicionar o fator como skill nova) e *merge* (substituir skills pelo valor do fator) — e busca, com um algoritmo A* guiado por heurística, o modelo que melhor se ajusta a dados reais de interação [F: cen2005lfa].

O ajuste é avaliado por regressão logística múltipla sobre se o estudante acertou ou não um passo, tratando estudante, skill e a interação entre skill e ordem de prática (o número de vezes que aquele estudante já praticou aquela skill) como preditores [F: cen2005lfa]. A seleção entre modelos candidatos usa estatísticas de ajuste penalizado por complexidade: Log-likelihood, R², AIC (Akaike Information Criterion: -2×log-likelihood + 2×número de parâmetros) e BIC (Bayesian Information Criterion: -2×log-likelihood + número de parâmetros × número de observações) [F: cen2005lfa]. No experimento original, com um modelo base de geometria (área de figuras, 12 skills, 5431 pontos de dados de 59 estudantes), todas as heurísticas concordaram em que adicionar o fator "FigurePart" melhorava o modelo; Log-likelihood e AIC convergiram ainda em dividir a skill "circle-area" segundo o fator "Embed" (se o círculo estava isolado ou embutido em outra figura), enquanto BIC, por penalizar mais fortemente a complexidade, selecionou um modelo mais parcimonioso com menos skills [F: cen2005lfa]. Um fator de dificuldade, nessa metodologia, é uma característica oculta de um problema que o torna mais fácil ou mais difícil de resolver, tipicamente identificada por teoria e análise de tarefa [F: cen2005lfa].

Aplicado depois a 11 conjuntos de dados públicos do DataShop, cobrindo diferentes domínios e tecnologias educacionais, o processo de busca do LFA melhorou o ajuste dos modelos de KC além dos melhores modelos gerados por humanos em todos os conjuntos de dados testados [F: liu2017closing]. Um ponto central da abordagem, segundo Liu e Koedinger, é que o LFA deriva novas variáveis a partir de variáveis existentes rotuladas por humanos, por meio de operadores simples (split, merge, add) — isso preserva a interpretabilidade, ao contrário de métodos totalmente automatizados que podem produzir descobertas difíceis ou impossíveis de interpretar [F: liu2017closing].

### "Fechando o laço": da descoberta estatística ao redesenho instrucional

Liu e Koedinger (2017) ilustram o ciclo completo de uso de uma descoberta do LFA. Em um conjunto de dados de geometria, o LFA havia dividido os itens de área de círculo em dois KCs separados — cálculo direto (achar área dado o raio) e cálculo inverso (achar o raio dado a área) — sem fazer a mesma divisão para outras formas [F: liu2017closing]. Os autores interpretaram essa divisão específica do círculo como evidência de uma dificuldade oculta ligada à aplicação da raiz quadrada no cálculo inverso, testaram essa interpretação em um conjunto de dados novo (com itens de área de quadrado, que também exigem raiz quadrada no sentido inverso) e, confirmada a interpretação, redesenharam um tutor de geometria em sala de aula para reforçar prática e scaffolding nos itens que exigem aplicar a raiz quadrada [F: liu2017closing]. O grupo com o tutor redesenhado teve escores de pós-teste significativamente mais altos que o grupo de controle, mesmo controlando pelo pré-teste (β = 0,09; p = 0,027; diferença de médias de pós-teste de 0,85 contra 0,73) [F: liu2017closing]. Os autores chamam esse processo completo — desenho do sistema, implantação, análise de dados, descoberta, retornando ao desenho — de "closing the loop", e apontam que é uma das poucas demonstrações experimentais de que uma melhoria automatizada de modelo de KC leva a ganhos reais de aprendizagem [F: liu2017closing].

### DataShop como infraestrutura

O **DataShop**, mantido pelo LearnLab/Carnegie Mellon University, é descrito pela própria documentação como "um serviço de análise de dados para a comunidade de ciência da aprendizagem", oferecendo um repositório central para armazenar e proteger dados de pesquisa e um conjunto de ferramentas de análise e relatório, incluindo curvas de aprendizagem padrão, navegação interativa dos dados e exportação para software estatístico [F: datashop2026about]. Na terminologia do DataShop, um **KC model** é definido operacionalmente como "um mapeamento entre passos e knowledge components em um conjunto de dados" [F: datashop2026kcmodels]. A plataforma gera automaticamente dois modelos de referência — um modelo de KC único (todas as transações mapeadas a um KC) e um modelo de passo único (um KC por passo distinto, com passos de poucas observações deixados sem KC) — e permite importar modelos definidos por pesquisadores via planilha, com uma coluna "KC (nome_do_modelo)" por KC [F: datashop2026kcmodels]. A comparação entre modelos de KC no DataShop é feita por número de KCs, número de observações rotuladas e cinco medidas de ajuste: AIC, BIC e três valores de RMSE de validação cruzada, com ordenação padrão por BIC — por penalizar mais fortemente parâmetros extras — e critério secundário configurável [F: datashop2026kcmodels].

## Algoritmos e modelos relevantes

- **Additive Factors Model (AFM)**: uma generalização do modelo de Rasch da teoria de resposta ao item que acomoda aprendizagem ao longo do tempo, usada para avaliar modelos de KC alternativos em conjunto com os dados [F: liu2017closing]. É o modelo estatístico usado pelo DataShop para gerar as medidas de ajuste de um KC model [F: datashop2026kcmodels].
- **Learning Factors Analysis (LFA)**: busca combinatória A* sobre o espaço de modelos de KC gerados por operadores split/add/merge, avaliados por regressão logística [F: cen2005lfa; F: cen2006lfa, metadados].
- **Rule space (Tatsuoka)**: abordagem anterior, baseada em teoria de resposta ao item, para diagnosticar padrões de misconception a partir de uma matriz item-atributo [F: tatsuoka1983rulespace, metadados].

## Requisitos e pressupostos

- Dados de interação rotulados por passo (estudante, item/passo, acerto/erro) para ajustar qualquer modelo estatístico sobre KCs [F: cen2005lfa].
- Um modelo cognitivo base, geralmente gerado por especialistas, como ponto de partida para busca automatizada — o LFA refina, mas não substitui inteiramente, o julgamento humano inicial [F: cen2005lfa; F: liu2017closing].
- Interpretabilidade como objetivo declarado: Liu e Koedinger argumentam que o envolvimento humano inicial na rotulagem de variáveis (diferentemente de métodos totalmente automatizados) é o que torna os resultados do LFA acionáveis para redesenho instrucional [F: liu2017closing].

## Vantagens e limitações

Vantagens: KC é um vocabulário comum que atravessa knowledge tracing (a unidade rastreada), sequenciamento (a unidade que define o que uma tarefa "exercita") e desenho instrucional (a unidade do KLI framework) [I]; a busca automatizada do LFA reduz o trabalho manual de inspecionar curvas de aprendizagem em busca de "blips" (irregularidades) [F: cen2005lfa].

Limitações: os próprios autores do LFA, em 2005, declaram que "o significado do modelo melhor ainda precisa ser investigado" e que "não está claro se precisamos substituir o modelo base pelo modelo melhor gerado pelo sistema" — a melhoria estatística de ajuste não equivale automaticamente a um modelo cognitivamente correto ou acionável [F: cen2005lfa]. O requisito de rotulagem humana inicial do LFA foi citado na literatura como limitação por quem defende métodos puramente automatizados [F: liu2017closing]. Modelos de KC construídos por entrevistas estruturadas, protocolos think-aloud e análise racional, embora tradicionais, são demorados e sujeitos a ignorar distinções de conteúdo importantes para aprendizes novatos [F: liu2017closing].

## Alternativas e comparações

| Aspecto | Modelo cognitivo manual (especialista) | Difficulty Factors Assessment | Learning Factors Analysis |
|---|---|---|---|
| Quem decide a decomposição | especialistas de conteúdo, iterativamente [F: cen2005lfa] | pesquisador, por comparação experimental controlada de um fator por vez [F: liu2017closing] | busca automatizada (A*) sobre variantes do modelo base [F: cen2005lfa] |
| Papel dos dados | validação posterior, se houver | usados para comparar pares de problemas [F: liu2017closing] | usados diretamente como critério de busca (regressão logística) [F: cen2005lfa] |
| Esforço humano | alto, inicial e contínuo | alto, por fator testado | inicial (rotulagem de fatores candidatos), reduzido na busca [F: liu2017closing] |
| Interpretabilidade do resultado | alta por construção | alta | preservada pelo uso de operadores simples sobre variáveis rotuladas por humanos [F: liu2017closing] |

## Métricas e métodos de avaliação

Ajuste estatístico de modelos de KC: Log-likelihood, R², AIC e BIC [F: cen2005lfa]; no DataShop, adicionalmente, RMSE de validação cruzada [F: datashop2026kcmodels]. Validação educacional (não apenas estatística) de uma descoberta de KC: medição de ganho pré/pós-teste em experimento controlado após redesenho instrucional baseado na descoberta — o critério de "closing the loop" [F: liu2017closing]. Ver `adp.eval.predictive-metrics` para o tratamento geral dessas métricas no domínio.

## Exemplo técnico independente de domínio

Esqueleto do ciclo de busca de modelo de KC por operadores e avaliação estatística, simplificado a partir da descrição do LFA [F: cen2005lfa]:

```
buscar_melhor_modelo(modelo_base, dados, fatores_candidatos):
    fronteira = fila_prioridade([modelo_base])
    melhores = []
    enquanto fronteira não vazia:
        modelo = fronteira.extrair_melhor(heuristica=BIC)
        para fator em fatores_candidatos:
            para operador em [split, add, merge]:
                novo_modelo = operador(modelo, fator)
                se não é_duplicata(novo_modelo, melhores):
                    ajustar(novo_modelo, dados)           # regressao logistica
                    novo_modelo.bic = calcular_bic(novo_modelo)
                    fronteira.inserir(novo_modelo)
        melhores = manter_top_k(fronteira, k=10..20)      # limitar memoria
    retornar melhor(melhores, criterio=BIC)
```

## Relações com outros conceitos

Parte de e dependência de `adp.id.kli-framework`, que fornece a definição formal e a taxonomia de KC usada aqui. Complementa `adp.lm.learner-model`, cujo overlay é tipicamente um vetor de estimativas por KC. Relaciona-se com `adp.kt.bayesian-knowledge-tracing`, que estima probabilisticamente o domínio de cada KC ao longo do tempo, com `adp.irt.item-response-theory`, de onde vem a linhagem do Q-matrix e do AFM, e com `adp.adapt.sequencing-policies`, que decide a próxima tarefa com base na cobertura de KCs. É avaliado por `adp.eval.predictive-metrics`.

## Lacunas e questões abertas

- Cen, Koedinger e Junker (2006), a versão publicada e revisada por pares do LFA (ITS 2006), foi verificada apenas por metadados nesta pesquisa — a Springer exige autenticação; o conteúdo citado aqui vem da versão de workshop aberta de 2005, que os próprios autores descrevem como antecessora do método [F: cen2005lfa]. Não é possível garantir que detalhes tenham mudado entre as duas versões.
- Tatsuoka (1983) foi verificado apenas por metadados (Wiley exige autenticação); a equivalência entre Q-matrix e KC model foi citada via a descrição de Liu e Koedinger, não da leitura direta do artigo original de rule space [F: liu2017closing].
- Não localizamos, nesta pesquisa, documentação pública detalhada do algoritmo exato do AFM tal como implementado no DataShop (apenas sua descrição como generalização do modelo de Rasch) [F: liu2017closing]; detalhamento adicional ficaria para o documento de modelos logísticos (`adp.kt.logistic-models`).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| koedinger2012kli | academico | 2026-10-29 |
| vanlehn2006behavior | academico | 2026-10-29 |
| cen2005lfa | academico | 2026-10-29 |
| cen2006lfa | academico (apenas metadados) | 2026-10-29 |
| liu2017closing | academico | 2026-10-29 |
| tatsuoka1983rulespace | academico (apenas metadados) | 2026-10-29 |
| datashop2026kcmodels | fornecedor | 2026-10-29 |
| datashop2026about | fornecedor | 2026-10-29 |
