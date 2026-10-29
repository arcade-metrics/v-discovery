---
id: lae.found.la-vs-edm
titulo: Learning Analytics vs. Educational Data Mining
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [siemensbaker2012towards, solaresearch2026whatisla, iedms2026about, bakerinventado2014edm, chatti2014challenges, romeroventura2007survey, romeroventura2010review, romeroventura2020updated, campbelldeblois2007academic]
relacoes:
  - { tipo: relacionado-a, alvo: lae.found.analytics-cycle }
  - { tipo: complementa, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: complementa, alvo: adp.irt.item-response-theory }
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
termos: [Learning Analytics, Educational Data Mining, academic analytics, LAK, SoLAR, International Educational Data Mining Society, discovery with models, relationship mining, structure discovery, prediction models]
---

# Learning Analytics vs. Educational Data Mining

## Definição e terminologia

Learning Analytics (LA) é definido, na formulação adotada pela Society for Learning Analytics Research (SoLAR) desde a 1ª International Conference on Learning Analytics and Knowledge (LAK11, 2011) e ainda citada como a definição mais referenciada do campo, como "a medição, coleta, análise e emissão de relatórios de dados sobre os aprendizes e seus contextos, com o propósito de compreender e otimizar a aprendizagem e os ambientes em que ela ocorre" [F: siemensbaker2012towards]. Em 2025 o comitê executivo da SoLAR formou um grupo de trabalho para revisar essa definição após 15 anos de uso, e a página atual da entidade a resume de forma mais compacta como "a coleta, análise, interpretação e comunicação de dados sobre os aprendizes e sua aprendizagem", voltada a gerar "insights teoricamente relevantes e acionáveis para potencializar a aprendizagem e o ensino" [F: solaresearch2026whatisla].

Educational Data Mining (EDM) é definido pela International Educational Data Mining Society (IEDMS) como "uma disciplina emergente, voltada para o desenvolvimento de métodos de exploração dos tipos únicos de dados oriundos de ambientes educacionais, e para o uso desses métodos a fim de compreender melhor os estudantes e os ambientes em que aprendem" [F: siemensbaker2012towards, cita a definição da IEDMS; iedms2026about]. Romero e Ventura, em sua revisão seminal da literatura entre 1995 e 2005, também ajudaram a consolidar o termo como área de pesquisa dedicada a aplicar técnicas de mineração de dados sobre dados educacionais [F: romeroventura2007survey]; a revisão de 2010 dos mesmos autores descreve a EDM como "uma área de pesquisa interdisciplinar emergente que lida com o desenvolvimento de métodos para explorar dados oriundos de contextos educacionais, usando esses métodos para entender melhor os estudantes e os ambientes em que aprendem" [F: romeroventura2010review].

O que LA e EDM não são: nenhum dos dois é sinônimo de **academic analytics**, termo cunhado por Campbell, DeBlois e Oblinger para o uso institucional de mineração de dados e modelagem preditiva voltado a decisões administrativas — matrícula, retenção, captação de recursos — mais do que à aprendizagem em si [F: campbelldeblois2007academic]. Siemens e Long tratam academic analytics como o nível institucional/departamental de análise, por oposição ao nível de sala de aula que chamam de learning analytics [I, com base na distinção relatada por fontes secundárias sobre Siemens & Long 2011 — o texto integral do artigo não pôde ser verificado nesta sessão, ver Lacunas]. Chatti et al. situam academic analytics e action analytics como campos vizinhos de LA, dos quais LA herdou conceitos e métodos, mas dos quais se diferencia por não se restringir a gestão de matrícula e previsão de sucesso acadêmico, orientando-se também a estudantes e professores com objetivos pedagógicos como reflexão, adaptação, personalização e recomendação [F: chatti2014challenges].

## Problema que resolve

Ambos os campos respondem à mesma pressão: o volume crescente de dados gerados pela interação de estudantes com sistemas educacionais (logs de LMS, tutores inteligentes, MOOCs) tornou inviável a análise manual e criou demanda por métodos sistemáticos que convertam esses dados em entendimento sobre o aprendiz e em ação sobre o ambiente de aprendizagem [F: siemensbaker2012towards]. LA e EDM compartilham o objetivo de melhorar a prática educacional a partir de abordagens intensivas em dados, incluindo como a avaliação é compreendida e como intervenções são planejadas e selecionadas [F: siemensbaker2012towards].

## Fundamentos e funcionamento

### Origens históricas

A EDM tem a trajetória mais longa. A sequência de marcos documentada por Baker e Inventado e por Siemens e Baker é: um primeiro workshop relacionado em 2000, um workshop teórico de Zaiane em 2001 sobre o potencial de métodos de EDM, o primeiro workshop a usar explicitamente o termo "educational data mining" em 2005 (em Pittsburgh, junto à AAAI), o livro "Data Mining in e-Learning" de Romero e Ventura também em 2005/2006, a 1ª International Conference on Educational Data Mining em 2008 (Montreal), o primeiro número do Journal of Educational Data Mining em 2009, o primeiro Handbook of Educational Data Mining em 2010 (Romero, Ventura, Pechenizkiy e Baker) e, por fim, a fundação da International Educational Data Mining Society (IEDMS) em julho de 2011, constituída como organização sem fins lucrativos em Massachusetts [F: bakerinventado2014edm; F: siemensbaker2012towards; F: iedms2026about]. Em 2026 a IEDMS reporta cerca de 240 membros pagantes, com participação anual na conferência EDM de magnitude semelhante [F: bakerinventado2014edm].

A comunidade de Learning Analytics nasceu depois e se organizou mais rapidamente. A série de conferências LAK foi concebida no início de 2010, com comitês diretivo e de programa globais; a 1ª International Conference on Learning Analytics and Knowledge (LAK11) ocorreu em Banff, Canadá, entre 27 de fevereiro e 1º de março de 2011, reunindo mais de 100 participantes e com atas publicadas pela ACM [F: siemensbaker2012towards]. A chamada da conferência declarava explicitamente a intenção de colocar em diálogo "os domínios técnico, pedagógico e social" para que intervenções e sistemas organizacionais atendessem às necessidades de todos os interessados [F: siemensbaker2012towards]. No verão de 2011 foi fundada a Society for Learning Analytics Research (SoLAR), com 14 membros fundadores — entre eles University of Michigan, Stanford, The Open University, Athabasca University e University of Queensland — para dar governança à conferência, apoiar padrões de pesquisa de alta qualidade e promover a adoção de LA por diferentes públicos [F: solaresearch2026whatisla via página "About SoLAR"; F: siemensbaker2012towards]. O primeiro Learning Analytics Summer Institute (LASI) ocorreu em 2012 [F: bakerinventado2014edm].

Assim, 2011 é o ano de fundação institucional de ambas as sociedades (IEDMS e SoLAR), embora a EDM já contasse com quase uma década de atividade prévia em workshops, enquanto LA emergiu de forma mais concentrada a partir da conferência fundadora [F: bakerinventado2014edm].

### Convergências

Siemens e Baker descrevem EDM e LAK (como a comunidade de learning analytics era por vezes identificada, pelo nome de sua conferência) como comunidades definidas de modo relativamente similar, que refletem a emergência de abordagens intensivas em dados na educação e compartilham o objetivo de melhorar a qualidade da análise de dados educacionais em larga escala, tanto para pesquisa básica quanto para prática [F: siemensbaker2012towards]. Baker e Inventado reforçam que muitas das mesmas pessoas frequentam as conferências EDM e LAK, com uma atitude de "competição amistosa e/ou colaboração amistosa" entre as comunidades [F: bakerinventado2014edm].

### Diferenças de ênfase

Siemens e Baker propõem cinco eixos de distinção entre as comunidades, explicitamente descritos como tendências gerais e não regras rígidas, já que pesquisadores de ambas as comunidades frequentemente adotam práticas do "lado" oposto [F: siemensbaker2012towards]:

| Eixo | EDM | LA (LAK) |
|---|---|---|
| Tipo de descoberta | Descoberta automatizada é central; julgamento humano é uma ferramenta auxiliar | Julgamento humano é central; descoberta automatizada é uma ferramenta auxiliar |
| Redução vs. holismo | Ênfase em decompor fenômenos em componentes e analisar relações entre eles (ex.: paradigma "discovery with models") | Ênfase em compreender sistemas como totalidades, em sua complexidade plena |
| Adaptação e personalização | Maior foco em adaptação automatizada (ex.: por um sistema tutor inteligente, sem humano no laço) | Maior foco em informar e capacitar instrutores e aprendizes |
| Origens | Raízes fortes em software educacional e modelagem de estudante, com comunidade significativa dedicada à predição de desempenho em cursos | Raízes mais fortes em web semântica, "currículo inteligente", predição de resultados e intervenções sistêmicas |
| Técnicas e métodos | Classificação, clusterização, modelagem bayesiana, mineração de relacionamentos, discovery with models, visualização | Análise de redes sociais, análise de sentimento, analytics de influência, análise de discurso, predição de sucesso do aprendiz, análise de conceitos, modelos de sensemaking |

[F: siemensbaker2012towards, tabela 1]

Baker e Inventado, revisitando essa comparação dois anos depois, resumem a diferença de forma mais direta: "Learning analytics tem um foco relativamente maior na interpretação humana dos dados e em visualização [...]. EDM tem um foco relativamente maior em métodos automatizados" [F: bakerinventado2014edm]. Eles também relatam uma visão alternativa apresentada por John Behrens na LAK 2012: ao contrário do que os próprios nomes sugerem, a EDM teria maior foco em aprendizagem como tema de pesquisa, enquanto learning analytics teria maior foco em aspectos da educação além da aprendizagem propriamente dita [F: bakerinventado2014edm]. Chatti et al. resumem de forma semelhante: "a EDM tem um foco mais tecnológico [...] ela visa, basicamente, ao desenvolvimento e aplicação de técnicas de mineração de dados no domínio educacional (analytics orientada a dados). A LA, por outro lado, tem um foco mais pedagógico. Ela coloca em prática diferentes métodos de analytics para estudar sua efetividade real na melhoria do ensino e da aprendizagem (analytics centrada no aprendiz)" [F: chatti2014challenges], citando a formulação de Clow de que "learning analytics está preocupada, antes de tudo e acima de tudo, com a aprendizagem" [F: chatti2014challenges, citando Clow 2013].

Na prática metodológica, os dois campos compartilham métodos de predição e de clusterização, mas EDM pesquisadores tendem a usar mais estimativa de conhecimento latente (p. ex. Bayesian Knowledge Tracing, ver `adp.kt.bayesian-knowledge-tracing`) do que classificação e regressão clássicas; descoberta de estrutura de domínio é mais enfatizada em EDM, enquanto análise de redes sociais é mais enfatizada em LA; mineração de relacionamentos é significativamente mais comum em EDM; e "discovery with models" também é mais comum em EDM, inclusive quando aparece em artigos de conferências LAK escritos por autores mais identificados com a comunidade EDM [F: bakerinventado2014edm]. Em contrapartida, análise automatizada de texto, mineração de texto e análise de discurso são áreas mais proeminentes em learning analytics do que em EDM [F: bakerinventado2014edm].

### Relação com academic analytics

Academic analytics precede ambos os campos e nasceu de iniciativas institucionais de gestão de matrícula e retenção: Campbell, DeBlois e Oblinger descrevem analytics como a prática de "unir grandes conjuntos de dados, técnicas estatísticas e modelagem preditiva" para produzir "inteligência acionável" e relatam casos de uso institucionais como previsão de inscrição na Baylor University, retenção na University of Alabama e identificação de estudantes em risco a partir de dados de sistema de gestão de cursos na Purdue University [F: campbelldeblois2007academic]. Chatti et al. observam que as iniciativas de academic analytics e action analytics se restringiram historicamente à gestão de matrícula e à predição de sucesso acadêmico, com uso de software estatístico, enquanto LA ampliou o escopo para objetivos mais alinhados ao processo de aprendizagem em si, como reflexão, adaptação, personalização e recomendação, e passou a se dirigir também a estudantes e professores, não apenas a gestores institucionais [F: chatti2014challenges].

## Alternativas e comparações

Não há alternativa a LA e EDM enquanto tradições de pesquisa — ambas coexistem e se sobrepõem parcialmente. A tabela de diferenças de ênfase na seção anterior resume a comparação mais citada da literatura [F: siemensbaker2012towards]. Romero e Ventura, em sua revisão atualizada de 2020, tratam LA e EDM como parte de uma mesma área de pesquisa mais ampla, ao lado de termos correlatos surgidos na última década — academic analytics, institutional analytics, teaching analytics, data-driven education e educational data science — sem estabelecer uma fronteira rígida entre eles [F: romeroventura2020updated].

## Aplicações típicas

Na EDM, quatro classes de método concentram a maior parte da pesquisa: modelos de predição (classificação, regressão e, como caso especial, estimativa de conhecimento latente — ver `adp.kt.bayesian-knowledge-tracing` e `adp.irt.item-response-theory`), descoberta de estrutura (clusterização, análise fatorial, descoberta de estrutura de domínio via Q-matrix), mineração de relacionamento (regras de associação, padrões sequenciais, correlação, mineração causal) e discovery with models, em que as saídas de um modelo tornam-se entrada de uma segunda análise [F: bakerinventado2014edm]. Em learning analytics, aplicações típicas incluem dashboards de acompanhamento de estudantes, sistemas de alerta precoce de evasão, ferramentas de visualização de interação em LMS, análise de redes sociais de aprendizagem colaborativa e analytics centrada no aprendiz para personalização e autorreflexão [F: chatti2014challenges].

## Relações com outros conceitos

Este documento é o ponto de entrada histórico e terminológico do domínio `learning-analytics-e-avaliacao`; o ciclo de processo pelo qual LA transforma dados em ação é tratado em `lae.found.analytics-cycle`. Técnicas de estimativa de conhecimento latente mencionadas como insumo típico de ambos os campos — Bayesian Knowledge Tracing e teoria de resposta ao item — são aprofundadas em `aprendizagem-adaptativa` (`adp.kt.bayesian-knowledge-tracing`, `adp.irt.item-response-theory`) e usadas aqui apenas como exemplo de método compartilhado, não como objeto deste domínio. O conceito de modelo de aprendiz (`adp.lm.learner-model`), para o qual tanto LA quanto EDM fornecem insumos, é tratado com profundidade em `aprendizagem-adaptativa`.

## Lacunas e questões abertas

- O artigo de Siemens e Long, "Penetrating the Fog: Analytics in Learning and Education" (EDUCAUSE Review 46(5), 2011), citado por múltiplas fontes secundárias como origem da distinção entre academic analytics (nível institucional) e learning analytics (nível de sala de aula/departamento), não pôde ser acessado integralmente nesta sessão — a página da EDUCAUSE retornou erro 403. A atribuição dessa distinção específica a Siemens e Long permanece "não verificado" em sua formulação exata; o conteúdo foi inferido a partir de resumos de terceiros, e por isso foi marcado como [I] no texto, não como [F].
- Não foi possível localizar, nas fontes consultadas nesta sessão, uma data exata de quando a IEDMS e a SoLAR formalizaram a "aliança" de comunicação e colaboração recomendada por Siemens e Baker (2012); o artigo apenas recomenda que os comitês executivos formalizem tal relação, sem confirmação de que isso tenha ocorrido.
- A citação de Clow (2013a), "Learning analytics is first and foremost concerned with learning", foi verificada apenas indiretamente, via citação de Chatti et al. (2014); o texto original de Clow não foi consultado nesta sessão.
- A revisão de Romero e Ventura de 2010 foi consultada apenas por resumo/abstract de terceiros (IEEE Xplore não fornece texto completo sem assinatura); a definição textual exata de EDM citada aqui foi parafraseada a partir desse resumo e marcada como fonte, mas não foi conferida palavra por palavra contra o PDF original.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| siemensbaker2012towards | academico | 2026-10-29 |
| solaresearch2026whatisla | secundario | 2026-10-29 |
| iedms2026about | secundario | 2026-10-29 |
| bakerinventado2014edm | academico | 2026-10-29 |
| chatti2014challenges | academico | 2026-10-29 |
| romeroventura2007survey | academico (metadados) | 2026-10-29 |
| romeroventura2010review | academico (resumo) | 2026-10-29 |
| romeroventura2020updated | academico (resumo) | 2026-10-29 |
| campbelldeblois2007academic | academico | 2026-10-29 |
