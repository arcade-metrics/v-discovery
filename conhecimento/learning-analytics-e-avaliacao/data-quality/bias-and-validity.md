---
id: lae.dq.bias-and-validity
titulo: Vieses e validade em dados de interação usados para learning analytics
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ferguson2012drivers, slade2013ethical, tempelaar2020subjective, kovanovic2015timeontask, fincham2019counting, weidlich2022causal, gasevic2015notforget]
relacoes:
  - { tipo: relacionado-a, alvo: lae.found.la-vs-edm }
  - { tipo: depende-de, alvo: lae.dq.provenance-and-lineage }
termos: [trace data, viés de amostragem, viés de construto, confundimento, causalidade reversa, construct validity, self-selection bias, ética em learning analytics]
---

# Vieses e validade em dados de interação usados para learning analytics

## Definição e terminologia

Dados de interação (*trace data*, também chamados dados de rastro ou de log) são os registros deixados automaticamente por um aluno ao interagir com um sistema — cliques, tempo em tela, respostas, acessos — e são a matéria-prima mais comum de learning analytics (LA) [I]. Este documento trata de dois problemas distintos, mas frequentemente confundidos, que afetam a confiabilidade de indicadores construídos sobre esses dados [I]:

- **Viés** (amostragem não representativa, confundimento, auto-seleção): o conjunto de alunos ou de eventos observados não representa igualmente a população de interesse, ou a relação entre variáveis observadas é distorcida por uma terceira variável não observada [I].
- **Validade**, em particular validade de construto: se o que o log mede de fato corresponde ao construto psicológico ou pedagógico que se pretende medir (engajamento, esforço, aprendizagem) [I, ancorado na preocupação levantada por F: fincham2019counting].

O que não é: este documento não trata do esquema técnico do evento (formato, taxonomia de eventos), que fica em `dados-pesquisa-e-eventos`; trata do que acontece depois que o evento já existe e está sendo usado para compor um indicador ou alimentar uma decisão [I]. Também não trata de modelos preditivos individuais de aluno (knowledge tracing, IRT), que ficam em `aprendizagem-adaptativa`; aqui o recorte é a confiabilidade do dado de entrada e da inferência agregada sobre esse dado [I].

## Problema que resolve

Um indicador de LA costuma ser tratado, na prática, como um dado "objetivo" por ser derivado de log em vez de autorrelato — mas essa suposição de objetividade não elimina viés nem resolve validade [I]. Reconhecer essas limitações é necessário antes de transformar um indicador em julgamento de valor sobre um aluno, uma turma ou uma intervenção, especialmente quando esse julgamento tem consequência institucional (sinalização de risco, intervenção pedagógica, avaliação de um produto) [I]. Rebecca Ferguson, em sua revisão de 2012 sobre os direcionadores, desenvolvimentos e desafios de LA, já situava entre os desafios do campo a necessidade de lidar com a ética do uso de dados de aluno e de assegurar que a análise sirva de fato à aprendizagem, não apenas à mensuração do que é fácil de medir [F: ferguson2012drivers].

## Fundamentos e funcionamento

### Viés de amostragem: quem deixa rastro

Nem todo aluno gera dados de interação na mesma proporção ou pelas mesmas razões. Diferenças de acesso a dispositivo e conectividade produzem lacunas sistemáticas em quem aparece nos dados de log, e esse tipo de viés de representação costuma ser mais difícil de detectar do que vieses mais estudados em outras modalidades de dado, porque o log "parece" neutro por ser um registro automático de comportamento [I, com base em achados análogos documentados para dados de sensor e de informática pessoal fora do contexto educacional — ver Lacunas]. Em LA, isso significa que um indicador agregado (ex. "tempo médio de estudo da turma") pode refletir desproporcionalmente o comportamento dos alunos com melhor acesso a dispositivo e rede, subrrepresentando quem usa a plataforma de forma mais esparsa ou por canais não instrumentados [I].

### Viés de construto: o log mede o que se quer medir?

Mesmo quando o dado é bem amostrado, ele pode não medir o construto pretendido. Fincham et al. observam que "engajamento" tem sido tratado de formas variadas na literatura de LA, sem consenso sobre a própria definição do construto, o que levanta "grave preocupação quanto à validade de construto": métricas diferentes rotuladas como "engajamento" podem não medir a mesma coisa [F: fincham2019counting]. Os autores propõem e validam, com análise fatorial exploratória e confirmatória, um modelo de engajamento ancorado em teoria e descrito por métricas comuns de LA, justamente para testar se essas métricas convergem para um mesmo construto latente [F: fincham2019counting].

Um caso concreto desse problema é o tempo em tela ou "tempo na tarefa" (*time on task*) como proxy de esforço ou engajamento cognitivo. Kovanović et al. mostram que o método de estimar tempo na tarefa a partir de dados de log de LMS é raramente descrito em detalhe na literatura, e que a escolha do método de estimação, por si só, muda as conclusões de um estudo de LA, sobretudo em cursos com uso intenso do LMS [F: kovanovic2015timeontask]. Isto é: duas análises que dizem medir "tempo de estudo" podem divergir não por diferença real de comportamento dos alunos, mas por diferença no critério operacional de onde uma sessão começa e termina [F: kovanovic2015timeontask]. O problema de validade aqui é duplo — tempo em tela não é garantidamente engajamento cognitivo (problema conceitual de construto) e, mesmo como medida de tempo, sua estimação não é padronizada (problema de medição) [I].

### Confundimento: quem deixa mais rastro já era diferente antes

Alunos mais motivados ou com melhor desempenho prévio tendem a interagir mais com a plataforma independentemente de qualquer efeito causal da interação sobre o aprendizado — o que gera confundimento quando se interpreta uma correlação entre "uso da plataforma" e "desempenho" como evidência de que o uso causa o desempenho [I]. Weidlich, Gašević e Drachsler, num primer sobre inferência causal e viés em LA usando grafos acíclicos dirigidos (DAGs), descrevem três armadilhas centrais para a área: viés de confundimento, viés de controle excessivo (*overcontrol bias*) e viés de colisor (*collider bias*), mostrando como aparecem na literatura publicada de LA e propondo formas de mitigação a partir da explicitação de hipóteses causais em um DAG [F: weidlich2022causal]. Esse tipo de confundimento está ligado a um viés de auto-seleção mais amplo: quando o uso de uma ferramenta de LA ou de um recurso é opcional, o grupo que efetivamente a usa já pode ser sistematicamente diferente do grupo que não usa, tornando a comparação entre os dois grupos não uma estimativa do efeito da ferramenta, mas de quem optou por usá-la [I].

### Causalidade reversa

Uma correlação entre um sinal de log e um resultado de aprendizagem pode decorrer de causalidade reversa: não é que acessar mais recursos cause melhor desempenho, mas que já estar com melhor desempenho (ou mais próximo de dominar o conteúdo) muda o padrão de acesso — por exemplo, alunos que já entenderam o conteúdo acessam menos material de reforço, criando uma correlação negativa que poderia ser mal interpretada como "menos acesso causa pior desempenho" ou o inverso, dependendo do recorte [I]. A estrutura de DAG defendida por Weidlich, Gašević e Drachsler é precisamente uma ferramenta para explicitar a direção hipotética de causalidade antes de interpretar uma correlação observacional, tornando visível quando a direção afirmada não é a única compatível com os dados [F: weidlich2022causal].

### Trace data pode não ser mais "objetivo" do que autorrelato

Há uma suposição comum de que dados de log são mais confiáveis por não dependerem da percepção do aluno sobre si mesmo. Tempelaar, Rienties e Nguyen testaram essa suposição numa aplicação de *dispositional learning analytics*, comparando viés de estilo de resposta (tendência sistemática de uso de escalas de autorrelato, independente do conteúdo do item) entre dados subjetivos (questionários) e dados de log de processo: encontraram que o viés de estilo de resposta explica uma parcela considerável da variação nos instrumentos de autorrelato e no desempenho em curso, enquanto os dados de log de processo são, na amostra estudada, majoritariamente independentes desses padrões de viés de resposta (sobreposição de até cerca de 4% da variação explicada) [F: tempelaar2020subjective]. Os próprios autores ressalvam que isso não torna o dado de log livre de viés em qualquer sentido — apenas livre de um tipo específico de viés (estilo de resposta) ao qual o autorrelato está sujeito [F: tempelaar2020subjective]. Ou seja: trace data pode ser mais objetivo em relação a um viés específico sem ser objetivo em relação a outros (amostragem, construto, confundimento) [I].

## Requisitos e pressupostos

Para que um indicador de LA baseado em trace data sirva de base a uma decisão (institucional ou de produto), geralmente é preciso assumir, de forma explícita e testável [I]:

- que a população que gera o dado é razoavelmente representativa da população sobre a qual se quer concluir, ou que a diferença de representação foi estimada e considerada [I];
- que a métrica de log tem alguma relação de validade (ainda que indireta) com o construto nomeado, e não apenas um nome em comum com ele — como no caso de "engajamento" discutido por Fincham et al. [F: fincham2019counting];
- que a direção de causalidade assumida entre o sinal de log e o resultado de interesse foi considerada contra hipóteses alternativas (confundimento, causalidade reversa, auto-seleção), idealmente com uma estrutura causal explícita [F: weidlich2022causal];
- que o uso do dado para decisão sobre um aluno individual respeita os princípios éticos de transparência e de tratamento do aluno como agente, não apenas como objeto de mensuração, na linha proposta por Slade e Prinsloo [F: slade2013ethical].

## Vantagens e limitações

Trace data tem a vantagem de escala (captura contínua, sem o custo de aplicar instrumentos) e, para pelo menos um tipo de viés estudado (estilo de resposta em escalas), mostrou-se mais robusto que autorrelato [F: tempelaar2020subjective]. A limitação central é que essas vantagens não se estendem automaticamente a outros vieses (amostragem, construto, confundimento, causalidade reversa), e tratar o dado de log como neutro por ser "automático" é, em si, um risco metodológico [I]. Ferguson já apontava, na origem do campo, que os desafios de LA não são apenas técnicos, mas envolvem decidir o que vale a pena medir e para que fim — uma formulação que antecipa a discussão de validade de construto [F: ferguson2012drivers]. Gašević, Dawson e Siemens argumentam, na mesma linha, que LA precisa estar ancorado em teoria educacional e não apenas no que é computacionalmente conveniente de calcular a partir do log disponível [F: gasevic2015notforget].

## Alternativas e comparações

| Estratégia de mitigação | Enfrenta | Não enfrenta sozinha |
|---|---|---|
| Triangular trace data com autorrelato e avaliação externa | Viés de construto (métrica única não confiável) [I] | Viés de amostragem se o autorrelato tiver a mesma lacuna de cobertura [I] |
| Modelar explicitamente hipóteses causais em DAG antes de interpretar correlação [F: weidlich2022causal] | Confundimento, causalidade reversa, viés de colisor [F: weidlich2022causal] | Viés de amostragem e de construto, que são anteriores à etapa causal [I] |
| Desenho experimental ou quase-experimental (ver `lae` domínio, métodos de avaliação) | Direção de causalidade de forma mais direta que análise observacional [I] | Custo operacional alto; nem todo indicador de produto comporta um experimento [I] |
| Análise fatorial / validação de construto do indicador antes do uso [F: fincham2019counting] | Viés de construto | Viés de amostragem e confundimento [I] |
| Princípios éticos explícitos de uso (transparência, agência do aluno) [F: slade2013ethical] | Risco de dano a um aluno individual a partir de decisão automatizada | Não corrige o viés estatístico do dado em si; é uma camada de governança, não de método [I] |

## Métricas e métodos de avaliação

Não há uma métrica única consolidada de "quão enviesado" é um indicador de LA; os métodos usados na literatura revisada combinam: comparação de estrutura fatorial de um construto entre amostras (análise fatorial confirmatória, como em Fincham et al.) [F: fincham2019counting]; comparação de resultados de um mesmo estudo sob diferentes definições operacionais da métrica de entrada, para estimar a sensibilidade da conclusão ao método de medição (como feito para tempo na tarefa por Kovanović et al.) [F: kovanovic2015timeontask]; e explicitação de um DAG causal para identificar, antes da análise, que variáveis precisam ser controladas, quais não devem ser controladas (para não introduzir viés de colisor) e quais são confundidoras plausíveis [F: weidlich2022causal]. Tempelaar, Rienties e Nguyen usam modelagem com variável latente de estilo de resposta para estimar a fração de variância de um instrumento atribuível a esse viés, método que poderia ser adaptado para estimar vieses análogos em métricas de log [F: tempelaar2020subjective].

## Exemplo técnico independente de domínio

```
# checklist de validação antes de promover um sinal de log a "indicador"
dado sinal_bruto, construto_alvo:
    1. cobertura: a distribuição de quem gera sinal_bruto é comparável à população alvo?
       (ex.: comparar taxa de dados ausentes por subgrupo conhecido)
    2. construto: existe evidência (teórica ou de validação empírica, ex. análise fatorial)
       de que sinal_bruto se relaciona com construto_alvo e não apenas o nomeia?
    3. direção causal: desenhar o DAG hipotético entre sinal_bruto, construto_alvo e
       variáveis de confundimento plausíveis (ex. desempenho prévio, motivação) —
       a correlação observada é compatível com mais de uma direção causal?
    4. auto-seleção: o sinal_bruto só existe para quem optou por um comportamento
       (ex. usar um recurso opcional)? se sim, a comparação entre quem usa e quem não
       usa está contaminada pela própria escolha?
    5. uso em decisão sobre indivíduo: se o indicador influenciar uma decisão sobre
       um aluno específico, documentar o grau de incerteza e permitir contestação
       (princípio de transparência e agência do aluno)
se qualquer item falhar sem mitigação -> reportar indicador com ressalva explícita,
    não como fato consolidado
```

## Relações com outros conceitos

Este documento pressupõe a rastreabilidade tratada em `lae.dq.provenance-and-lineage`: sem saber de onde um dado vem e que transformação sofreu, não é sequer possível testar os vieses de amostragem ou de construto descritos aqui [I]. Relaciona-se com os fundamentos do domínio (`lae.found.la-vs-edm`) na medida em que a tensão entre medir o que é computacionalmente disponível e medir o que é pedagogicamente relevante é constitutiva da distinção entre as tradições de LA e EDM [I]. A discussão de causalidade aqui introduzida (confundimento, causalidade reversa) é aprofundada, no desenho de pesquisa, pelos métodos de avaliação experimental e quase-experimental do próprio domínio `learning-analytics-e-avaliacao` (ver `00-brief.md`, estrutura sugerida).

## Lacunas e questões abertas

- O achado de que dados de log são menos sujeitos a viés de estilo de resposta do que autorrelato vem de um único estudo aplicado (dispositional learning analytics, cursos de matemática/estatística para calouros) [F: tempelaar2020subjective]; não foi verificado se o resultado se generaliza para outros tipos de log (ex. cliques em vídeo, acesso a fórum) ou outros contextos educacionais.
- A afirmação sobre viés de amostragem por acesso a dispositivo/internet em dados de rastro educacionais especificamente (em oposição a dados de sensor/informática pessoal em geral) não foi encontrada numa fonte dedicada ao contexto de LA durante esta pesquisa; o parágrafo correspondente está marcado [I] e é uma inferência por analogia, não um fato com fonte direta em LA — fica como lacuna a localizar um estudo específico de LA sobre o tema (ex. literatura de "digital divide in learning analytics").
- Não verificado: a extensão exata da literatura posterior a 2022 sobre causalidade em LA além do primer de Weidlich, Gašević e Drachsler; é descrita aqui como uma introdução ao tema, não como cobertura exaustiva do estado da arte em inferência causal em LA.
- Slade e Prinsloo (2013) é citado quanto aos princípios éticos gerais; a literatura de ética em LA desde então (incluindo os próprios autores, em trabalhos posteriores sobre vulnerabilidade de alunos) não foi aprofundada nesta sessão e é candidata a um documento próprio do domínio, possivelmente fora de `data-quality/`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ferguson2012drivers | academico | 2026-10-29 |
| slade2013ethical | academico | 2026-10-29 |
| tempelaar2020subjective | academico | 2026-10-29 |
| kovanovic2015timeontask | academico | 2026-10-29 |
| fincham2019counting | academico | 2026-10-29 |
| weidlich2022causal | academico | 2026-10-29 |
| gasevic2015notforget | academico | 2026-10-29 |
