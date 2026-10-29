---
id: adp.eval.predictive-metrics
titulo: Métricas preditivas para modelos de aluno
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [pelanek2015metrics, pelanek2018details, pelanek2017umapmetrics, gervet2020when]
relacoes:
  - { tipo: avaliado-por, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: avaliado-por, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: avaliado-por, alvo: adp.kt.logistic-models }
  - { tipo: complementa, alvo: adp.eval.evaluation-protocols }
  - { tipo: depende-de, alvo: adp.eval.evaluation-protocols }
  - { tipo: relacionado-a, alvo: adp.eval.educational-effectiveness }
termos: [AUC, RMSE, log-loss, calibração, scoring rule, Brier score, reliability diagram, A' statistic]
---

# Métricas preditivas para modelos de aluno

## Definição e terminologia

Métricas preditivas quantificam o quanto as probabilidades que um modelo de aluno atribui a uma resposta futura (`p_i ∈ [0,1]`) se aproximam do resultado observado (`o_i ∈ {0,1}`), em geral a correção de uma resposta [F: pelanek2015metrics]. Na literatura de student modeling o termo "métrica" é usado de forma não técnica, como sinônimo de "qualquer função usada para comparar modelos", e não no sentido matemático de distância [F: pelanek2015metrics]. As métricas mais citadas se dividem em três famílias: compreensão probabilística do erro (MAE, RMSE, log-likelihood), compreensão qualitativa do erro via matriz de confusão (acurácia, precisão, F1, kappa), e avaliação da ordenação relativa das predições (ROC/AUC) [F: pelanek2015metrics]. O termo "scoring rule", usado em previsão meteorológica e análise de decisão, é sinônimo de métrica de desempenho preditivo; uma scoring rule é "própria" (*proper*) se o melhor valor esperado é obtido dizendo a verdade, isto é, prevendo a distribuição real [F: pelanek2015metrics]. O que esta família de métricas não é: não é uma medida de eficácia educacional nem de qualidade de decisão pedagógica — ver `adp.eval.educational-effectiveness` para essa distinção.

## Problema que resolve

Pesquisadores precisam comparar modelos de aluno (BKT, PFA, DKT e variantes) e ajustar seus parâmetros, e ambas as tarefas exigem resumir a diferença entre predições e observações em um único número [F: pelanek2015metrics]. Não existe consenso sobre qual métrica usar, e a escolha é frequentemente feita sem justificativa explícita: Pelánek cita um artigo de EDM que usa apenas AUC "por ser uma métrica popular de machine learning", sem mais argumento [F: pelanek2015metrics]. Essa ausência de critério é um problema prático porque diferenças pequenas entre modelos — muitas vezes na terceira casa decimal de RMSE — podem ou não ser importantes, e a métrica escolhida influencia essa interpretação mais do que a escolha do procedimento de ajuste de parâmetros [F: pelanek2015metrics].

## Fundamentos e funcionamento

### MAE, RMSE e log-likelihood

MAE é `(1/n) Σ|o_i − p_i|`; RMSE é a raiz de `(1/n) Σ(o_i − p_i)²`; log-likelihood é `Σ[o_i log(p_i) + (1−o_i) log(1−p_i)]` [F: pelanek2015metrics]. MAE é uma scoring rule *imprópria*: um modelo que prevê exatamente a probabilidade real de acerto pode perder, em MAE, para um modelo enviesado em direção ao resultado majoritário [F: pelanek2015metrics]. Pelánek ilustra isso com um aluno simulado que acerta com probabilidade constante 0,7: um modelo A que prevê 0,7 (o modelo correto) tem MAE pior que um modelo B que prevê 0,9, embora A seja estritamente melhor em RMSE e log-likelihood, que são scoring rules próprias [F: pelanek2015metrics]. Em um experimento com 300 combinações de modelo e conjunto de dados simulados, MAE concordou com RMSE/LL sobre qual é o melhor modelo em apenas 2 de 20 casos, enquanto RMSE e LL concordaram entre si em 17 de 20 [F: pelanek2015metrics]. A conclusão central do autor é que **MAE não deveria ser usada** para avaliação de modelos de aluno binários [F: pelanek2015metrics].

RMSE sem a raiz quadrada é chamado, em previsão meteorológica, de Brier score ou quadratic scoring rule [F: pelanek2015metrics]. Log-likelihood penaliza muito mais fortemente predições confiantes e erradas — é ilimitada, de modo que uma única predição muito confiante e errada pode dominar o valor total, por isso na prática se usa um limite artificial (por exemplo 0,01) para as probabilidades [F: pelanek2015metrics]. RMSE e LL têm forma de erro muito parecida, divergindo principalmente nesse extremo [F: pelanek2015metrics].

### AUC e suas armadilhas em knowledge tracing

A curva ROC resume o desempenho de classificação binária sobre todos os limiares possíveis; a área sob ela (AUC) equivale à probabilidade de que uma observação positiva escolhida ao acaso tenha predição maior que uma negativa escolhida ao acaso, e vale 0,5 para predições aleatórias e 1 para um modelo perfeito [F: pelanek2015metrics]. A limitação central da AUC é que ela considera apenas a **ordenação relativa** das predições: se todas as predições forem divididas por dois, a AUC permanece igual [F: pelanek2015metrics]. Isso tem três consequências documentadas especificamente para modelos de habilidade (skill models):

1. **Calibração ausente.** AUC não exige que os valores absolutos de probabilidade estejam corretos, o que é precisamente o que decisões de mastery learning precisam [F: pelanek2015metrics].
2. **Sensibilidade à heterogeneidade dos dados, não à qualidade do modelo.** Em dados homogêneos (um único skill, dificuldade estável) a AUC fica baixa (perto de 0,5) mesmo para o modelo ótimo; em dados heterogêneos (múltiplos skills ou alunos com habilidades muito diferentes) a AUC sobe mesmo para um modelo simples, porque a métrica capta sobretudo a variabilidade dos dados, não a capacidade preditiva "dentro" de cada skill [F: pelanek2017umapmetrics]. Pelánek mostra um exemplo artificial onde um modelo com "mismatch de velocidade de aprendizagem" entre dois skills obtém a mesma AUC que o modelo correto quando computada por skill, mas desempenho ruim quando computada globalmente — e o oposto ocorre com um modelo que combina um skill correto com um skill de "aprendizagem negativa" [F: pelanek2017umapmetrics].
3. **Relação fraca com usos posteriores do modelo.** Pardos e Yudelson (2013), citados por Pelánek, usaram dados simulados para comparar métricas na identificação do "momento de aprendizagem" (o passo em que o aluno aprendeu o skill) e obtiveram bons resultados com RMSE e resultados ruins com AUC [F: pelanek2015metrics]. Dhanani et al. (2014), também citados, compararam métricas quanto à capacidade de recuperar os parâmetros verdadeiros de BKT a partir de dados simulados: RMSE e LL recuperam bem os parâmetros (RMSE ligeiramente melhor), enquanto AUC leva a resultados ruins [F: pelanek2015metrics].

Com base nesse conjunto de evidências, a recomendação do autor é que, para modelos de habilidade, **AUC deveria ser usada com mais critério**, preferencialmente como métrica adicional e não única, e que RMSE ou log-likelihood são escolhas mais defensáveis para avaliação e para ajuste de parâmetros [F: pelanek2015metrics].

### Agregação: global, por skill, por aluno

Dados de modelos de aluno têm pelo menos duas dimensões — alunos e skills (ou itens) — e qualquer métrica pode ser computada de três formas: globalmente (tratando todos os pontos de dados como iguais), com média por skill (calcula-se a métrica por skill e tira-se a média), ou com média por aluno [F: pelanek2017umapmetrics]. Nenhuma dessas formas é "a correta"; a escolha depende da aplicação, mas influencia fortemente o resultado quando a distribuição de respostas por aluno ou por skill é desigual — o que é típico em sistemas reais [F: pelanek2017umapmetrics]. Pelánek demonstra com dados simulados (70% dos alunos com 5 tentativas, 30% com 60 tentativas) que o RMSE global pode apontar um modelo como melhor enquanto o RMSE médio por aluno aponta o modelo concorrente como melhor [F: pelanek2017umapmetrics]. O problema é documentado como causa real, não hipotética, de resultados inflados: Khajah, Lindsey e Mozer (2016) mostraram que o ganho de 25% em AUC reportado por Piech et al. (2015) para Deep Knowledge Tracing sobre BKT se devia em grande parte ao fato de que os dois trabalhos computaram AUC de formas diferentes — cálculo global versus cálculo por skill com média — e não a uma diferença real de capacidade preditiva [F: pelanek2018details]. Xiong et al. (2016) chegaram de forma independente a uma conclusão relacionada, atribuindo parte do ganho reportado de DKT a um problema de duplicação de registros no dataset público ASSISTments 2009-2010 (ver `adp.eval.evaluation-protocols`) [F: pelanek2018details].

Pelánek recomenda que todo relato de métrica declare explicitamente qual forma de agregação foi usada, algo que sua revisão da literatura mostra ser raro: na maioria dos artigos analisados não é possível determinar, a partir do texto, se a AUC relatada foi global ou com média por skill ou por aluno [F: pelanek2017umapmetrics].

## Requisitos e pressupostos

- A escolha de métrica deve ser guiada pelo uso pretendido do modelo: valores absolutos de probabilidade importam (mastery learning, ajuste de dificuldade) ou apenas a ordenação relativa importa (triagem, ranking)? [F: pelanek2015metrics]
- Para comparação de modelos, a métrica de avaliação final deveria idealmente coincidir com a métrica usada no ajuste de parâmetros; usar AUC só na avaliação final enquanto o ajuste otimiza RMSE ou log-likelihood implicitamente é uma inconsistência comum [F: pelanek2015metrics].
- Relatar a forma de agregação (global, por skill, por aluno) é pré-condição para que o número seja comparável entre estudos [F: pelanek2017umapmetrics].
- Valores absolutos de RMSE e AUC não são interpretáveis isoladamente como "bom" ou "ruim": dependem da taxa de erro média e da heterogeneidade dos dados, não apenas da qualidade do modelo [F: pelanek2017umapmetrics].

## Vantagens e limitações

RMSE e log-likelihood são scoring rules próprias, convertem-se naturalmente em decomposições diagnósticas (Brier score) e são comparáveis entre estudos quando a agregação é declarada [F: pelanek2015metrics]. Sua limitação é menor interpretabilidade absoluta e, no caso de log-likelihood, sensibilidade extrema a erros confiantes sem um limite artificial de probabilidade [F: pelanek2015metrics].

AUC tem a vantagem de não exigir calibração para ser calculada e de ser familiar a partir de outras áreas de machine learning, mas para modelos de habilidade essa mesma invariância a reescalonamento é uma desvantagem quando a aplicação depende de valores absolutos [F: pelanek2015metrics]. AUC também não é bem definida quando todas as respostas de um aluno (ou skill) são iguais, situação comum na agregação por aluno para alunos com poucas respostas; a prática usual é ignorar esses casos, o que o próprio Pelánek chama de "não inteiramente justo" [F: pelanek2017umapmetrics].

MAE é simples e intuitiva, mas é scoring rule imprópria e pode levar a conclusões equivocadas sobre qual modelo é melhor; a recomendação é não usá-la [F: pelanek2015metrics].

## Alternativas e comparações

| Métrica | Tipo | Própria? | Sensível a calibração | Recomendação |
|---|---|---|---|---|
| MAE | erro absoluto | não [F: pelanek2015metrics] | sim | não usar [F: pelanek2015metrics] |
| RMSE | erro quadrático | sim [F: pelanek2015metrics] | sim | preferida para modelos de habilidade [F: pelanek2015metrics] |
| Log-likelihood | baseada em verossimilhança | sim [F: pelanek2015metrics] | sim | preferida, mais sensível a erros confiantes [F: pelanek2015metrics] |
| AUC | ordenação (ROC) | não se aplica (não é scoring rule) | não (invariante a reescala) [F: pelanek2015metrics] | usar com critério, nunca isolada [F: pelanek2015metrics] |
| Acurácia/F1/kappa | matriz de confusão | depende de limiar | sim | mais apropriada para modelos de afeto/estado do que para modelos de skill [F: pelanek2015metrics] |

Gervet et al. (2020), ao comparar IRT, PFA, DAS3H, BKT+, DKT e SAKT em nove datasets reais, reportam AUC e RMSE lado a lado justamente porque "cuidamos de calibração, e essa característica [de invariância a reescala] é indesejável" na AUC [F: gervet2020when].

## Métricas e métodos de avaliação

### Calibração e por que importa para decisões de mastery

Calibração mede a diferença entre probabilidades previstas e frequências observadas; um modelo bem calibrado que prevê 0,8 de chance de acerto deve, entre os casos em que previu 0,8, observar acerto em aproximadamente 80% deles [F: gervet2020when]. A decomposição do Brier score em *reliability* (calibração), *resolution* (capacidade de distinguir casos, isto é, não prever sempre a taxa-base) e *uncertainty* (incerteza inerente dos eventos, independente do modelo) torna essa distinção operacional: um modelo pode ter reliability perfeita apenas prevendo sempre a taxa-base, mas isso tem resolution nula e é inútil na prática — um bom modelo precisa das duas propriedades [F: pelanek2015metrics]. Diagramas de confiabilidade (*reliability diagrams*), que plotam frequência prevista contra observada por faixas (bins) de predição, tornam essa diferença visível mesmo quando duas métricas agregadas (por exemplo RMSE) são quase idênticas entre dois modelos [F: pelanek2015metrics].

Calibração importa diretamente para decisões de mastery learning e para modelos de aluno abertos porque essas aplicações **usam o valor absoluto da predição como limiar de decisão** (por exemplo, declarar domínio quando `P(acerto) > 0,95`) [F: gervet2020when]. Gervet et al. relatam que, nos modelos de melhor desempenho preditivo que testaram (regressão logística com melhores features e DKT), a calibração é boa apenas no intervalo de probabilidades onde está concentrada a maior parte dos dados; fora desse intervalo há vieses sistemáticos — em um dos datasets (ASSISTments 2009), ambos os modelos superestimam alunos quando a probabilidade de acerto observada é baixa e subestimam quando é alta [F: gervet2020when]. Os autores concluem que "uma política instrucional que baseia seu comportamento adaptativo em um modelo de desempenho de aluno severamente enviesado é de valor limitado, quando não diretamente prejudicial" [F: gervet2020when], e que visualizar a calibração permite detectar — mas não necessariamente corrigir automaticamente — esses vieses sistemáticos antes que se propaguem para a política adaptativa [F: gervet2020when].

### Incerteza da estimativa de estado do aluno

As fontes abertas nesta pesquisa tratam a incerteza principalmente de forma indireta, via diagramas de confiabilidade e decomposição do Brier score, que expõem o grau de (des)calibração mas não produzem diretamente um intervalo de confiança por predição individual [F: pelanek2015metrics]. Modelos bayesianos como BKT produzem, a cada passo, uma probabilidade pontual de domínio `P(mastery)`, mas a literatura consultada não discute explicitamente a construção de intervalos de credibilidade em torno dessa estimativa nem sua comunicação a quem toma decisões (professor, política adaptativa) [H]. A ausência de uma discussão verificável e dedicada ao tema é registrada como lacuna abaixo.

## Exemplo técnico independente de domínio

Cálculo de três métricas sobre um conjunto de predições, destacando a diferença entre agregação global e por grupo (aluno ou skill):

```
entrada: lista de tuplas (grupo_id, p_predito, o_observado)

MAE_global      = media(|o - p|) sobre todas as tuplas
RMSE_global     = sqrt(media((o - p)^2)) sobre todas as tuplas
LL_global       = soma(o*log(p) + (1-o)*log(1-p)) sobre todas as tuplas, com p limitado a [eps, 1-eps]

para cada metodo in {global, por_grupo}:
    se metodo == por_grupo:
        para cada grupo g:
            RMSE_g = RMSE calculado só com as tuplas de g
        RMSE_agregado = media(RMSE_g sobre os grupos)   # cada grupo pesa igual
    senao:
        RMSE_agregado = RMSE_global                      # cada tupla pesa igual

reportar: metrica usada, metodo de agregacao, e n de tuplas/grupos
```

Diagrama de confiabilidade (esboço): dividir as predições em `k` faixas (bins) por valor de `p`; para cada faixa, plotar o valor médio de `p` (eixo x) contra a frequência observada de acerto naquela faixa (eixo y); um modelo perfeitamente calibrado cai sobre a diagonal. Um histograma auxiliar ("sharpness graph") mostra quantos casos caem em cada faixa, revelando se o modelo usa uma gama ampla de probabilidades ou se concentra as predições perto da taxa-base [F: pelanek2015metrics].

## Relações com outros conceitos

Esta técnica é a base quantitativa usada para comparar os modelos descritos em `adp.kt.bayesian-knowledge-tracing`, `adp.kt.deep-knowledge-tracing` e `adp.kt.logistic-models`. Ela depende, para ser interpretável, dos protocolos de validação tratados em `adp.eval.evaluation-protocols` (sem especificar como os dados foram divididos entre treino e teste, uma métrica preditiva não é comparável entre estudos). A distinção entre precisão preditiva e utilidade educacional do modelo é aprofundada em `adp.eval.educational-effectiveness`.

## Lacunas e questões abertas

- Não foi localizada, entre as fontes efetivamente abertas, uma discussão dedicada e verificável sobre intervalos de credibilidade ou distribuições posteriores para a estimativa de estado do aluno (por oposição à estimativa pontual); o tratamento de incerteza nesta pesquisa limitou-se a calibração agregada.
- Kulik & Fletcher (2016) e VanLehn (2011), citados por outras fontes consultadas como referências sobre a relação entre precisão preditiva e eficácia, não puderam ser abertos nesta sessão (ver nota no fragmento bibliográfico); não são citados aqui como [F].
- A literatura revisada por Pelánek é centrada em modelos de habilidade binários (correto/incorreto); extensões para desempenho contínuo (tempo de resposta, acerto parcial) são mencionadas apenas de passagem [F: pelanek2015metrics].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| pelanek2015metrics | academico | 2026-10-29 |
| pelanek2018details | academico | 2026-10-29 |
| pelanek2017umapmetrics | academico | 2026-10-29 |
| gervet2020when | academico | 2026-10-29 |
