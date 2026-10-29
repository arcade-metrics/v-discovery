---
id: adp.eval.evaluation-protocols
titulo: Protocolos de validação para modelos de aluno
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [pelanek2018details, gervet2020when, xiong2016going, pelanek2017mastery]
relacoes:
  - { tipo: depende-de, alvo: adp.eval.predictive-metrics }
  - { tipo: complementa, alvo: adp.eval.predictive-metrics }
  - { tipo: avaliado-por, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: avaliado-por, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
  - { tipo: relacionado-a, alvo: adp.eval.educational-effectiveness }
termos: [vazamento de dados, validação cruzada, student-level cross-validation, item-level cross-validation, generalização, predições estáticas, predições dinâmicas, feedback loop]
---

# Protocolos de validação para modelos de aluno

## Definição e terminologia

Um protocolo de validação é o conjunto de decisões metodológicas sobre como os dados históricos de interação são coletados, divididos em conjunto de treino e de teste, e usados para calcular uma métrica preditiva [F: pelanek2018details]. Pelánek argumenta que essas decisões "podem parecer detalhes técnicos não diretamente relacionados ao problema central da modelagem de aluno", mas que, na prática, "mesmo detalhes metodológicos aparentemente pequenos podem ter consequências significativas para a interpretação de experimentos com modelos de aluno" [F: pelanek2018details]. O termo cobre pelo menos três decisões distintas: (1) como os dados usados para treino e teste foram coletados, (2) como dividir dados em treino e teste para validação cruzada, e (3) que tipo de generalização a validação está de fato medindo (a novos alunos, a novos itens, a novas populações, a novos pontos no tempo) [F: pelanek2018details]. Protocolo de validação não é sinônimo de métrica: duas avaliações podem usar a mesma métrica (por exemplo AUC) e ainda assim não ser comparáveis, se a forma de dividir os dados for diferente — ver `adp.eval.predictive-metrics` para a distinção entre escolha de métrica e sua forma de cálculo.

## Problema que resolve

Modelos de aluno são ajustados sobre dados históricos, mas o interesse prático está em sua capacidade de generalizar — fazer predições úteis para alunos e itens que ainda não foram vistos [F: pelanek2018details]. Sem um protocolo de validação explícito, duas formas de viés passam despercebidas: vazamento de informação do futuro para o passado (usar respostas posteriores para prever respostas anteriores) e contaminação entre o conjunto de treino e o de teste pela mesma unidade (mesmo aluno, mesmo item) [F: pelanek2018details]. O caso mais citado na literatura consultada é o de Deep Knowledge Tracing: Piech et al. (2015) reportaram um ganho de 25% em AUC sobre BKT, mas análises posteriores atribuíram boa parte desse ganho a dois problemas de protocolo — computação da métrica de forma diferente da literatura anterior (ver `adp.eval.predictive-metrics`) e um problema de qualidade dos dados no dataset público usado (duplicação de registros), não a uma vantagem real do modelo [F: pelanek2018details] [F: xiong2016going].

## Fundamentos e funcionamento

### Vazamento de dados por duplicação: o caso ASSISTments 2009-2010

Xiong, Zhao, Van Inwegen e Beck (2016) reimplementaram DKT em TensorFlow para reproduzir os resultados de Piech et al. e, ao investigar o dataset público ASSISTments 2009-2010 usado no artigo original, encontraram três problemas de preparação de dados que inflavam artificialmente o desempenho de DKT [F: xiong2016going]:

1. **Registros duplicados.** O dataset continha 123.778 linhas duplicadas de um total de 525.535 (23,6%), diferindo apenas nos campos que contam o número de oportunidades de prática; os autores confirmam que isso é um erro de dados reconhecido pela própria equipe do ASSISTments, e excluem essas duplicatas de todos os experimentos subsequentes [F: xiong2016going].
2. **Mistura de problemas principais com problemas de scaffolding.** Problemas de scaffolding (andaimes pedagógicos oferecidos após erro) são tipicamente excluídos por BKT e PFA, mas o experimento original de DKT não fez essa filtragem, dando a DKT acesso a informação adicional que os modelos comparados não tinham — uma comparação, portanto, não equivalente [F: xiong2016going].
3. **Duplicação por repetição de tag de skill.** Quando um problema tem múltiplas tags de skill, o formato do dataset repete a sequência de respostas uma vez por skill associado; para um modelo sequencial como DKT, que processa a ordem exata das interações, isso insere informação redundante que infla artificialmente o desempenho — os autores mostram que, ao prever os registros repetidos (que seguem imediatamente o registro original na sequência), DKT atinge AUC de 0,97, contra 0,77 nos registros originais ("líderes") da mesma sequência [F: xiong2016going].

Após corrigir essas três questões (usando apenas problemas principais, sem duplicação, com skills múltiplos tratados como um skill conjunto), os autores concluem que "as descobertas de DKT não mantêm uma vantagem geral quando comparadas ao modelo PFA, quando aplicadas a conjuntos de dados devidamente preparados e limitados a questões principais (não de scaffolding)" [F: xiong2016going]. Esse episódio é citado por Pelánek como o exemplo paradigmático de como decisões de protocolo — não apenas de modelo — determinam a conclusão de um estudo [F: pelanek2018details].

### Divisão de dados: por aluno, por item, por tempo

Pelánek propõe terminologia baseada no termo "nível" (*level*) para descrever esquemas de divisão treino/teste, evitando o termo ambíguo "estratificado", que tem significados conflitantes na literatura de modelos de aluno [F: pelanek2018details]:

- **Student level (nível de aluno):** todos os dados de um aluno ficam inteiramente no treino ou inteiramente no teste; testa generalização para alunos novos. É o esquema mais comum em modelagem de aluno, porque na aplicação real sempre chegam alunos novos, enquanto o conjunto de itens é relativamente fixo [F: pelanek2018details].
- **Item level (nível de item):** análogo, mas dividindo por item; testa generalização para itens novos. É mais relevante quando a aplicação depende de prever o desempenho em itens ainda não vistos no treino [F: pelanek2018details].
- **Population level:** divisão por população natural de alunos (por exemplo, coortes de um mesmo curso em semestres diferentes), testando generalização entre populações [F: pelanek2018details].
- **KC level:** divisão por componente de conhecimento (knowledge component), testando generalização a novos KCs [F: pelanek2018details].

Esses esquemas não são mutuamente exclusivos; um estudo pode cruzar divisão por aluno com divisão por item simultaneamente [F: pelanek2018details].

### Aspecto temporal: predições estáticas versus dinâmicas

Além de decidir a unidade de divisão, é preciso decidir como o tempo é tratado. Divisão aleatória ignorando a ordem temporal usaria ações futuras para prever ações passadas, o que não faz sentido [F: pelanek2018details]. Dentro da validação cruzada por nível de aluno, Pelánek distingue:

- **Predições estáticas:** a predição para toda a sequência de teste de um aluno é feita de uma só vez, com base apenas nos dados de treino — o modelo não é atualizado ao longo da sequência de teste [F: pelanek2018details].
- **Predições dinâmicas:** a predição é atualizada continuamente após cada resposta observada, incorporando também os dados do conjunto de teste à medida que são revelados (respeitando sua ordem) [F: pelanek2018details].

A abordagem dinâmica corresponde mais de perto ao uso real de um modelo de aluno em um sistema de ensino, e por isso costuma ser a preferível; a abordagem estática é usada sobretudo por conveniência computacional, quando recalcular a predição após cada observação é custoso (por exemplo em métodos de cadeia de Markov Monte Carlo ou fatoração de matrizes) [F: pelanek2018details]. Pelánek observa que diferentes famílias de modelo tendem a adotar protocolos diferentes na prática — trabalhos baseados em BKT tipicamente usam validação dinâmica, enquanto trabalhos baseados em AFM (additive factor model) tipicamente usam validação estática — o que compromete a comparabilidade direta entre essas famílias quando os protocolos não são alinhados [F: pelanek2018details].

### Interação entre coleta de dados e divisão: viés de mastery learning

Pelánek identifica uma interação importante: quando os dados de treino foram coletados por um sistema que já usa mastery learning (ou seja, o sistema para de apresentar itens de um skill quando declara domínio), construir o conjunto de teste como "os últimos 20% das tentativas de cada aluno" introduz viés sistemático a favor de respostas corretas, porque qualquer critério de mastery learning é, por definição, acionado ao observar respostas corretas [F: pelanek2018details]. Pelánek e Řihák (2017), em análise experimental dedicada a critérios de mastery learning (regra de N acertos consecutivos, média móvel exponencial, critérios baseados em modelo probabilístico), mostram que a escolha da fonte de dados usada para a decisão de domínio e o ajuste do limiar de corte têm impacto maior sobre o comportamento do sistema do que a escolha da técnica de modelagem de aluno em si — reforçando que decisões de protocolo (aqui, de que dado conta como "evidência de domínio") não são secundárias em relação à escolha de modelo [F: pelanek2017mastery]. Isso é agravado por um **loop de retroalimentação**: o modelo usado pelo sistema de produção influencia quais dados são coletados, e esses mesmos dados são depois usados para avaliar modelos (inclusive o próprio modelo em produção) — uma dinâmica que, segundo Pelánek, não tem paralelo direto em outros domínios de previsão probabilística (como meteorologia), onde o modelo não influencia os dados coletados [F: pelanek2015metrics, §6.3].

### Generalização entre cursos, populações e plataformas

Gervet et al. (2020) conduziram validação cruzada aninhada de 5 folds, em nível de aluno, em nove datasets reais de diferentes sistemas (ASSISTments, KDD Cup/Cognitive Tutor, Squirrel AI, um curso de espanhol, um curso de estática de engenharia) [F: gervet2020when]. Os autores explicitam que escolheram validar apenas por aluno (não também por tempo ou por item) "para que nossos resultados fossem comparáveis à maior parte do trabalho anterior" — uma decisão de protocolo tomada por comparabilidade, não por ser a mais rigorosa [F: gervet2020when]. Eles identificam explicitamente essa escolha como limitação do próprio estudo: "a principal limitação do nosso trabalho é a ausência de validação cruzada no espaço de itens. Nossa metodologia de validação cruzada demonstra que os modelos generalizam para novos alunos, mas não nos diz quão bem os modelos generalizam para itens fora do conjunto de treino" [F: gervet2020when]. O achado central do estudo é que qual modelo generaliza melhor depende de características do dataset — regressão logística lidera em datasets de tamanho moderado ou com muitas interações por aluno, DKT lidera em datasets grandes ou onde a ordem temporal precisa importa, e métodos de processo de Markov como BKT ficam atrás de ambos em todos os nove datasets testados [F: gervet2020when]. Essa dependência do resultado em relação às propriedades do dataset é, em si, um argumento metodológico: comparações de modelo feitas em um único dataset não generalizam para "qual modelo é melhor" de forma ampla [F: gervet2020when].

## Requisitos e pressupostos

- Validação cruzada por aluno pressupõe que as propriedades dos itens e da população de alunos sejam estáveis ao longo do tempo; Pelánek cita como exceção plausível (embora não testada) domínios de conhecimento sujeitos a eventos correntes, como fatos de geografia afetados por guerra ou mudanças políticas [F: pelanek2018details].
- Avaliar generalização para itens novos exige um esquema de divisão por item (ou por KC), não apenas por aluno; a maioria dos estudos revisados usa apenas divisão por aluno, deixando a generalização a itens novos sem teste direto [F: pelanek2018details] [F: gervet2020when].
- Antes de qualquer comparação entre modelos, datasets públicos devem ser auditados quanto a duplicação de registros e inconsistência de rotulagem de skill — a ausência dessa auditoria foi a causa identificada de uma conclusão amplamente citada e posteriormente revisada na literatura de knowledge tracing [F: xiong2016going].

## Vantagens e limitações

Protocolos explícitos (nomeados e documentados) tornam resultados comparáveis entre estudos e expõem vieses de coleta; sua principal limitação é o custo: validação cruzada aninhada com seleção de hiperparâmetros, como a usada por Gervet et al., é computacionalmente cara, e os próprios autores reportam que BKT+ foi tão lento que não puderam concluir experimentos em datasets grandes dentro do protocolo adotado ("muito lento" nas tabelas de resultado) [F: gervet2020when]. Protocolos com predições dinâmicas são mais realistas, mas computacionalmente mais caros que os estáticos para certas famílias de modelo [F: pelanek2018details].

## Alternativas e comparações

| Protocolo | Testa generalização para | Risco de viés se mal aplicado | Custo computacional |
|---|---|---|---|
| Divisão aleatória (ignora estrutura) | nada de relevante prático | vazamento temporal severo [F: pelanek2018details] | baixo |
| Student-level CV, predição estática | alunos novos | viés se treino usou mastery learning e teste é "últimas tentativas" [F: pelanek2018details] | baixo-médio |
| Student-level CV, predição dinâmica | alunos novos, uso realista | menor, mas ainda sujeito a feedback loop na coleta original [F: pelanek2018details] | médio-alto |
| Item-level CV | itens novos | raramente aplicado; ausência é limitação reconhecida mesmo em estudos recentes [F: gervet2020when] | médio |
| Population/cohort-level CV | novas populações/plataformas | pressupõe que coortes sejam comparáveis entre si [F: pelanek2018details] | médio |

## Métricas e métodos de avaliação

Os protocolos aqui descritos não são, por si, métricas — são a condição de validade para que as métricas de `adp.eval.predictive-metrics` (AUC, RMSE, log-likelihood) sejam comparáveis entre estudos. Gervet et al. reportam AUC e RMSE com desvio padrão entre os 5 folds da validação cruzada, o que permite diferenciar diferença real de ruído amostral [F: gervet2020when]. Xiong et al. usam AUC e o quadrado da correlação de Pearson (r²) como métricas complementares, justificando que r² é "similar a RMSE, mas mais interpretável", embora reconheçam que "nenhum dos dois métodos é uma métrica de avaliação perfeita" [F: xiong2016going].

## Validação do modelo versus validação da política de adaptação

Um protocolo de validação, por mais rigoroso que seja, avalia a capacidade preditiva do **modelo** — não avalia se a **política de adaptação** que consome essas predições (que item mostrar a seguir, quando declarar domínio) produz bons resultados educacionais. Gervet et al. tornam essa distinção explícita: "a eficácia de sistemas tutores inteligentes é determinada principalmente por seu elo mais fraco", e argumentam que hoje esse elo mais fraco costuma ser a política instrucional e o modelo de componentes de conhecimento, não o modelo de predição de desempenho [F: gervet2020when]. Eles notam ainda que modelos com precisões preditivas semelhantes podem, quando inseridos em uma política adaptativa, produzir recomendações de item "muito diferentes" — citando Rollinson e Brunskill (2015) — e que a maioria das políticas instrucionais hoje em uso é heurística, sem justificativa teórica ou empírica direta (por exemplo, o "princípio Goldilocks" de escolher itens de dificuldade intermediária) [F: gervet2020when]. Avaliar apenas o modelo preditivo (via AUC/RMSE/calibração) não garante, portanto, que a política que o usa seja boa; essa lacuna é retomada em `adp.eval.educational-effectiveness`, que trata da relação entre precisão preditiva e resultado educacional de fato observado em estudantes.

Pelánek chega a uma formulação relacionada a partir de simulações: um modelo de aluno incorreto pode, ao guiar a própria coleta de dados via mastery learning, gerar um conjunto de dados insuficiente para demonstrar que o modelo está incorreto — isto é, o feedback loop entre modelo e coleta pode mascarar, na validação do modelo, exatamente os defeitos que mais importam para a política [F: pelanek2018details].

## Exemplo técnico independente de domínio

Esquema de validação cruzada em nível de aluno, com predição dinâmica, aplicável a qualquer modelo sequencial de aluno:

```
entrada: interacoes agrupadas por aluno, ordenadas por tempo dentro de cada aluno
k = numero de folds (ex.: 5)

dividir alunos em k grupos disjuntos (sem levar em conta itens ou tempo entre alunos)

para cada fold f de 1 a k:
    teste  = alunos do grupo f
    treino = alunos dos grupos restantes

    ajustar modelo M usando apenas interacoes de "treino"

    para cada aluno a em "teste":
        reiniciar o estado do modelo para o aluno a
        para cada interacao (item, resposta, t) de a, em ordem:
            p = M.prever(estado_atual, item)          # predicao dinamica
            registrar (p, resposta) para calculo de metrica
            estado_atual = M.atualizar(estado_atual, item, resposta)   # incorpora o dado de teste revelado

calcular metrica (ex.: RMSE) sobre todos os pares (p, resposta) registrados,
reportando tambem a agregacao usada (global, por aluno, por skill — ver adp.eval.predictive-metrics)
```

Nota de auditoria prévia, antes de qualquer execução acima: verificar duplicação de linhas, consistência entre contadores de oportunidade e presença de múltiplas tags de skill por item no dataset de origem [F: xiong2016going].

## Relações com outros conceitos

Este documento é pré-requisito para a leitura correta de qualquer número produzido por `adp.eval.predictive-metrics`: sem declarar o protocolo de divisão de dados, uma métrica preditiva não é comparável entre estudos. Protocolos de validação também são a ponte metodológica para `adp.eval.educational-effectiveness`, que trata do passo seguinte — mesmo um modelo corretamente validado pode não corresponder a uma política de adaptação eficaz. A dependência do desempenho relativo dos modelos em relação a propriedades do dataset, documentada por Gervet et al., conecta este documento a `adp.kt.comparison` e a `adp.adapt.sequencing-policies`.

## Lacunas e questões abertas

- Não foi localizada, entre as fontes abertas, uma comparação sistemática e verificável entre protocolos de validação prospectiva (modelo avaliado em produção, com dados coletados após o deploy) e validação interna offline; a distinção é mencionada na literatura consultada apenas de forma indireta, via a discussão do feedback loop entre coleta e modelo [F: pelanek2018details].
- Gervet et al. reconhecem explicitamente a ausência de validação cruzada por item em seu próprio estudo como limitação; não foi encontrada, nas fontes abertas, uma substituição mais recente que resolva essa lacuna para os mesmos datasets.
- Doroudi & Brunskill (2019), citado por buscas secundárias como trabalho relevante sobre a diferença entre acurácia de modelo e equidade de política resultante, não pôde ser aberto nesta sessão (cópia no site da autora fora do ar); não é citado aqui como [F].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| pelanek2018details | academico | 2026-10-29 |
| gervet2020when | academico | 2026-10-29 |
| xiong2016going | academico | 2026-10-29 |
| pelanek2017mastery | academico | 2026-10-29 |
