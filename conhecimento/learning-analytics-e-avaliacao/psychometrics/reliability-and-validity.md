---
id: lae.psy.reliability-and-validity
titulo: Confiabilidade e validade de instrumentos de avaliação
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [crockeralgina1986ctt, cronbach1951alpha, sijtsma2009alpha, revellezinbarg2009coefficients, messick1995validity, aera2014standards]
relacoes:
  - { tipo: depende-de, alvo: lae.psy.classical-test-theory }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: avaliado-por, alvo: lae.psy.fairness-in-measurement }
termos: [confiabilidade, consistência interna, alfa de Cronbach, ômega de McDonald, teste-reteste, formas paralelas, validade de construto, validade de conteúdo, validade de critério, validade convergente, validade discriminante, validade preditiva, Standards for Educational and Psychological Testing]
---

# Confiabilidade e validade de instrumentos de avaliação

## Definição e terminologia

Confiabilidade e validade são as duas propriedades centrais pelas quais a qualidade de um instrumento de avaliação é julgada. Confiabilidade é a consistência da medição: o grau em que o instrumento produziria o mesmo resultado em condições repetidas equivalentes, formalizada na teoria clássica dos testes (CTT, ver `lae.psy.classical-test-theory`) como a proporção da variância do escore observado atribuível ao escore verdadeiro, σ²(T)/σ²(X) [I, decorrência direta do modelo apresentado em `lae.psy.classical-test-theory`]. Validade é a propriedade de as inferências e os usos feitos a partir dos escores de um teste serem apropriados e sustentados por evidência — não uma propriedade do teste isoladamente, mas da interpretação dada aos seus resultados para um propósito específico [F: messick1995validity, que unifica os tipos tradicionais de validade (conteúdo, critério, construto) como facetas de um conceito único de validade de construto, descrito via fontes secundárias que resumem o artigo — ver Lacunas]. Essa reformulação foi incorporada pelos "Standards for Educational and Psychological Testing", publicação conjunta da American Educational Research Association (AERA), da American Psychological Association (APA) e do National Council on Measurement in Education (NCME), referência normativa da área nos Estados Unidos e amplamente citada internacionalmente [F: aera2014standards, descrito via fontes secundárias acadêmicas — texto integral não acessado nesta sessão, ver Lacunas].

O que não é: confiabilidade não é validade, e um instrumento pode ser altamente confiável — produzir resultados consistentes — sem medir o que se propõe a medir (ver seção Vantagens e limitações / distinção central) [I].

## Problema que resolve

Antes de usar um indicador de desempenho, engajamento ou aprendizagem construído a partir de um instrumento de avaliação, é preciso responder a duas perguntas distintas: o instrumento produz resultados estáveis o bastante para serem úteis (confiabilidade), e os resultados significam o que se pretende que signifiquem, para o uso pretendido (validade)? Sem essa checagem, um painel de indicadores ou um critério de aprovação pode estar amplificando ruído de medição ou usando um proxy que não corresponde ao construto de interesse — risco especialmente relevante quando os escores alimentam decisões automatizadas ou modelos preditivos de `aprendizagem-adaptativa`.

## Fundamentos e funcionamento

### Confiabilidade: tipos e estimadores

A CTT distingue formas de estimar confiabilidade conforme a fonte de erro que se quer capturar [I, decorrência do modelo de `lae.psy.classical-test-theory`]:

- **Consistência interna**: o grau em que os itens de um único teste, aplicado uma única vez, medem de forma coerente o mesmo construto. O estimador clássico é o **alfa de Cronbach**, introduzido por Cronbach em 1951 como generalização da confiabilidade por metades (split-half): alfa é matematicamente a média de todos os coeficientes de split-half possíveis para um teste, e Cronbach demonstrou que seu cálculo não exige o pressuposto de que os itens sejam unidimensionais [F: cronbach1951alpha, conteúdo descrito via fontes secundárias acadêmicas — texto completo do artigo original não acessado nesta sessão].
- **Teste-reteste**: aplica-se o mesmo instrumento duas vezes à mesma amostra, em momentos diferentes, e correlaciona-se os dois conjuntos de escores; captura estabilidade temporal, mas é sensível a efeitos de aprendizagem ou memória da primeira aplicação e ao intervalo escolhido entre as aplicações [I].
- **Formas paralelas**: aplicam-se duas versões do teste, construídas para serem equivalentes em conteúdo e dificuldade, à mesma amostra, e correlaciona-se os escores; evita o efeito de memória do teste-reteste, mas exige o trabalho adicional de construir e validar formas efetivamente equivalentes [I].

### Críticas ao alfa de Cronbach e alternativas

O uso difundido do alfa de Cronbach como medida-padrão de confiabilidade recebeu críticas metodológicas recorrentes. Sijtsma (2009) argumenta que alfa é, na prática, um limite inferior da confiabilidade — frequentemente uma subestimativa grosseira — e que não está relacionado à estrutura interna (unidimensionalidade) do teste da forma como costuma ser interpretado; segundo essa crítica, alfa é usado mais como medida de consistência interna do que como estimativa legítima de confiabilidade [F: sijtsma2009alpha, conteúdo obtido via resultado de mecanismo de busca que indexou o artigo; tentativa de acesso direto ao PDF retornou erro de limite de requisições nesta sessão — ver Lacunas]. Em resposta, Revelle e Zinbarg concordam que alfa não é apropriado para julgar se um teste mede um único conceito, mas recomendam o **ômega de McDonald** (ω) como estimador preferível ao "greatest lower bound" (glb) — um modelo de fatores que separa a variância comum (do construto) da variância específica de cada item, produzindo uma estimativa de confiabilidade menos dependente do pressuposto de tau-equivalência que o alfa assume implicitamente [F: revellezinbarg2009coefficients, conteúdo descrito via fontes secundárias]. O debate sobre qual coeficiente usar — alfa, ômega, ou o glb — permanece ativo na literatura psicométrica mais recente, sem consenso definitivo sobre um substituto universal [I].

### Validade: tipos de evidência

A tradição mais antiga distinguia três tipos de validade — de conteúdo, de critério e de construto — mas essa tripartição foi formalmente abandonada pelas edições mais recentes dos "Standards for Educational and Psychological Testing", que tratam validade como um conceito unitário sustentado por cinco fontes de evidência complementares, não por tipos concorrentes [F: aera2014standards, descrito via fontes secundárias acadêmicas]:

- **Evidência baseada no conteúdo do teste**: o quanto os itens e tarefas do instrumento representam adequadamente o domínio de conhecimento ou habilidade que se pretende avaliar — herdeira direta da antiga "validade de conteúdo", frequentemente verificada por análise de especialistas e por alinhamento teste-currículo [F: aera2014standards].
- **Evidência baseada em processos de resposta**: o quanto os processos cognitivos ou comportamentais efetivamente empregados pelos respondentes correspondem ao que o construto pretende capturar [F: aera2014standards].
- **Evidência baseada na estrutura interna**: o quanto as relações entre itens e entre dimensões do instrumento são consistentes com a estrutura teórica esperada do construto — herdeira parcial da antiga "validade de construto" [F: aera2014standards].
- **Evidência baseada em relações com outras variáveis**: inclui as noções tradicionais de **validade convergente** (o instrumento se correlaciona com outras medidas do mesmo construto ou de construtos teoricamente relacionados), **validade discriminante** (não se correlaciona indevidamente com medidas de construtos distintos) e **validade preditiva** (os escores predizem desempenho futuro em um critério relevante, herdeira da antiga "validade de critério") [F: aera2014standards].
- **Evidência baseada nas consequências da testagem**: o quanto os usos e as consequências reais da aplicação do teste — incluindo efeitos não pretendidos sobre subgrupos — são compatíveis com o uso pretendido; fonte de evidência que conecta validade a equidade de medição (ver `lae.psy.fairness-in-measurement`) [F: aera2014standards].

## Requisitos e pressupostos

- Confiabilidade pressupõe o modelo de escore verdadeiro mais erro da CTT (ver `lae.psy.classical-test-theory`), com erros não correlacionados entre aplicações ou formas comparadas [I].
- O alfa de Cronbach, especificamente, costuma ser interpretado sob o pressuposto implícito de tau-equivalência essencial entre itens (cargas iguais no fator comum); quando esse pressuposto não se sustenta, alfa tende a subestimar a confiabilidade real, o que motiva a preferência por ômega em contextos onde o pressuposto é questionável [F: sijtsma2009alpha; revellezinbarg2009coefficients].
- Qualquer afirmação de validade exige que se especifique o uso e a população pretendidos: validade não é uma propriedade fixa do instrumento, e a mesma prova pode ser válida para um uso (diagnóstico formativo em sala de aula) e inválida para outro (seleção de alto risco) sem qualquer mudança no instrumento em si [F: messick1995validity].

## Vantagens e limitações

A distinção central desta seção: **um instrumento pode ser confiável sem ser válido**. Um termômetro quebrado que sempre marca 36°C é perfeitamente consistente (confiável) mas inútil para medir febre (inválido para esse uso); de forma análoga, um teste cujos itens medem de forma consistente um traço irrelevante ao construto de interesse (por exemplo, velocidade de leitura em vez de compreensão matemática, quando o enunciado dos problemas é longo) pode exibir alfa ou ômega altos e, ainda assim, não sustentar as inferências que se pretende fazer a partir dele [I]. A recíproca é mais restritiva: um instrumento pouco confiável dificilmente é válido para qualquer uso prático, porque erro de medição aleatório atenua qualquer relação real entre o escore e o critério externo que se quer prever ou a conclusão que se quer sustentar [I] — por isso a confiabilidade costuma ser tratada como condição necessária, mas não suficiente, para a validade [I].

Limitações práticas: estimar confiabilidade por consistência interna é barato (uma única aplicação), mas não captura estabilidade temporal; teste-reteste e formas paralelas capturam estabilidade, mas custam uma segunda aplicação (e, no caso de formas paralelas, a construção e validação de uma segunda versão equivalente) [I]. Validade de conteúdo e de processos de resposta dependem de julgamento de especialistas, menos facilmente quantificável que os coeficientes de confiabilidade [I].

## Alternativas e comparações

| Estimador de confiabilidade | O que captura | Limitação principal |
|---|---|---|
| Alfa de Cronbach | consistência interna, uma aplicação [F: cronbach1951alpha] | limite inferior da confiabilidade real; pode subestimar gravemente quando tau-equivalência não se sustenta [F: sijtsma2009alpha] |
| Ômega de McDonald | consistência interna via modelo de fatores, menos dependente de tau-equivalência [F: revellezinbarg2009coefficients] | exige ajuste de modelo fatorial, mais complexo de calcular e comunicar que alfa [I] |
| Teste-reteste | estabilidade temporal [I] | confundido com efeitos de aprendizagem/memória; exige duas aplicações [I] |
| Formas paralelas | estabilidade sem efeito de memória direto [I] | exige construir e validar uma segunda forma equivalente [I] |

## Métricas e métodos de avaliação

Ver estimadores de confiabilidade acima. Para validade, não há um único número substituto para as cinco fontes de evidência dos Standards: a prática recomendada é reunir evidência de múltiplas fontes (conteúdo, estrutura interna, relações com critérios externos) em um "argumento de validade" cumulativo para o uso específico pretendido, em vez de buscar um único coeficiente de "validade geral" [F: messick1995validity, conforme síntese de fontes secundárias sobre o conceito de validade como argumento].

## Exemplo técnico independente de domínio

Cálculo de alfa de Cronbach a partir de uma matriz de respostas a k itens (pseudocódigo, fórmula padrão):

```
entrada: matriz R[pessoa][item], k itens
k = numero_de_itens(R)
var_itens = soma( variancia(R[:][j]) para cada item j )
var_total = variancia( soma(R[pessoa][:]) para cada pessoa )

alfa = (k / (k - 1)) * (1 - var_itens / var_total)
```

Nota: o mesmo cálculo não informa se o construto medido é o pretendido — essa é uma pergunta de validade, não de confiabilidade, e não é respondida por nenhuma manipulação adicional dos mesmos dados de resposta [I].

## Relações com outros conceitos

Depende do modelo de escore verdadeiro mais erro da teoria clássica dos testes (`lae.psy.classical-test-theory`), de onde vem a definição formal de confiabilidade. Relaciona-se com a teoria de resposta ao item (`adp.irt.item-response-theory`), que oferece uma noção de precisão de medição mais fina (função de informação variável por nível de traço) do que o coeficiente único de confiabilidade da CTT. A evidência de validade baseada em consequências de testagem é avaliada em profundidade por `lae.psy.fairness-in-measurement`, que trata de funcionamento diferencial de item e de vieses de medição entre subgrupos.

## Lacunas e questões aberta

- O artigo original de Cronbach (1951) e o de Sijtsma (2009) não foram acessados em texto completo nesta sessão: o primeiro por exigir autenticação em repositório acadêmico sem cópia aberta localizada, o segundo por limite de requisições (HTTP 429) no servidor que hospedava o PDF indexado. As afirmações sobre ambos vêm de descrições de terceiros que parafraseiam ou citam diretamente o conteúdo; revisão futura deveria confirmar diretamente nos textos originais.
- Os "Standards for Educational and Psychological Testing" (2014) são citados como referência normativa central da área, mas o texto integral da publicação não foi acessado nesta sessão (não há versão de acesso aberto). As cinco fontes de evidência de validade foram reconstruídas a partir de múltiplas fontes secundárias acadêmicas convergentes, mas um trecho textual direto do documento não pôde ser citado.
- Não foi aprofundada aqui a distinção entre confiabilidade "relativa" (capacidade de ordenar pessoas) e "absoluta" (precisão do escore individual), relevante para decisões de corte (pass/fail) — possível extensão futura em `assessment-design/`.
- O ômega de McDonald tem variantes (ω total, ω hierárquico) não diferenciadas aqui; aprofundamento ficaria para um documento técnico específico sobre modelagem de confiabilidade por análise fatorial, se o domínio crescer nessa direção.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| crockeralgina1986ctt | academico [metadados] | 2026-10-29 |
| cronbach1951alpha | academico [metadados; conteúdo via fontes secundárias] | 2026-10-29 |
| sijtsma2009alpha | academico [conteúdo via resultado de busca; download direto falhou] | 2026-10-29 |
| revellezinbarg2009coefficients | academico [metadados] | 2026-10-29 |
| messick1995validity | academico [metadados; conteúdo via fontes secundárias] | 2026-10-29 |
| aera2014standards | normativo [conteúdo via fontes secundárias] | 2026-10-29 |
