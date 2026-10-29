---
id: lae.found.analytics-cycle
titulo: O ciclo de learning analytics
tipo: framework
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [clow2012cycle, campbelldeblois2007academic, chatti2014challenges, shum2012policybrief]
relacoes:
  - { tipo: relacionado-a, alvo: lae.found.la-vs-edm }
  - { tipo: complementa, alvo: iop.lr.caliper }
  - { tipo: relacionado-a, alvo: adp.lm.open-learner-model }
termos: [ciclo de learning analytics, closing the loop, dashboard, reference model, what-who-why-how, micro-level, meso-level, macro-level, stakeholders]
---

# O ciclo de learning analytics

## Definição e terminologia

O "ciclo de learning analytics" é o modelo de processo que descreve como dados brutos sobre aprendizes são transformados em ação sobre o ambiente de aprendizagem, fechando um laço de retroalimentação entre captura de dados, análise e intervenção [F: clow2012cycle, conforme descrito por fontes secundárias sobre o artigo — ver Lacunas]. Não é um algoritmo nem uma técnica de modelagem: é um modelo de referência de alto nível, análogo a um ciclo de vida de processo, usado para situar onde cada técnica específica (predição, clusterização, estimativa de conhecimento latente etc.) se encaixa no fluxo entre dado e decisão [I].

Dois modelos de referência concorrem pela formulação canônica do ciclo:

- O modelo de cinco estágios de **Campbell, DeBlois e Oblinger** (2007), formulado no contexto de academic analytics institucional: **Capture** (captura de dados a partir de sistemas administrativos e acadêmicos), **Report** (geração de relatórios), **Predict** (modelagem preditiva), **Act** (ação sobre a predição, por exemplo uma intervenção de aconselhamento) e **Refine** (refinamento do modelo com base em novos dados) [F: clow2012cycle, que atribui esse modelo de cinco estágios a Campbell e Oblinger 2007 — a formulação exata com esses cinco termos não foi localizada no texto integral do artigo de 2007 consultado nesta sessão; ver Lacunas]. O artigo de Campbell, DeBlois e Oblinger de fato descreve repetidamente um ciclo de captura de dados institucionais, construção de modelos preditivos, geração de "inteligência acionável" e refinamento contínuo do modelo à medida que novos dados chegam, por exemplo nos casos de uso de admissão da Baylor University e de retenção da University of Alabama, ainda que sem rotular os cinco passos com esses nomes exatos [F: campbelldeblois2007academic].
- O **ciclo de learning analytics** proposto por **Doug Clow** (2012), que revisita o modelo de cinco estágios e o reformula como um laço fechado de quatro elementos: **Learners** (aprendizes, que geram dados ao interagir com o ambiente), **Data** (os dados gerados), **Metrics** (métricas, analytics ou visualizações derivadas dos dados) e **Interventions** (intervenções que realimentam o comportamento dos aprendizes, fechando o ciclo) [F: clow2012cycle]. Clow ancora esse ciclo em teoria pedagógica — em particular no ciclo de aprendizagem experiencial de Kolb e na reflexão-em-ação de Schön — argumentando que dados sem ação (ou ação sem retroalimentação) não constituem learning analytics efetiva: o ciclo só "fecha" quando a intervenção de fato chega ao aprendiz e gera nova experiência a ser capturada [F: clow2012cycle].

O que o ciclo não é: não é uma descrição de arquitetura técnica (pipeline de ETL, armazém de dados, API), tratada em outro domínio (`dados-pesquisa-e-eventos`); e não é, por si, um modelo de aprendiz ou de conhecimento do estudante — esses são um dos insumos possíveis da etapa de métricas/análise, aprofundados em `aprendizagem-adaptativa`.

## Problema que resolve

Instituições, cursos e produtos educacionais acumulam dados de interação sem que isso produza, por si só, melhoria de aprendizagem. O ciclo formaliza a exigência de que a análise esteja acoplada a uma ação que efetivamente chegue ao aprendiz ou ao educador — "fechar o loop" — e que o resultado dessa ação retroalimente o próximo ciclo de captura e análise [F: clow2012cycle]. Sem essa retroalimentação explícita, dashboards e relatórios tendem a ficar isolados da prática pedagógica, problema que Clow aponta como razão para reformular o modelo mais administrativo de Campbell e Oblinger em termos pedagógicos [F: clow2012cycle].

## Fundamentos e funcionamento

### As quatro dimensões do modelo de referência de Chatti et al.

Um segundo eixo organizador complementar ao ciclo temporal é o modelo de referência de quatro dimensões proposto por Chatti, Dyckhoff, Schroeder e Thüs (2012) e revisado por Chatti et al. (2014), que pergunta, para qualquer iniciativa de LA: **o quê** (que dados e ambientes alimentam a análise), **quem** (quais interessados são alvo da análise), **por quê** (quais objetivos motivam a análise) e **como** (quais métodos a realizam) [F: chatti2014challenges]. As quatro dimensões, detalhadas:

- **O quê (dados, ambientes e contexto)**: as fontes de dados dividem-se entre sistemas educacionais centralizados — sobretudo learning management systems (LMS), que acumulam logs de leitura, escrita, acesso a materiais, envio de tarefas e realização de provas, frequentemente com ferramentas simples de relatório embutidas — e ambientes de aprendizagem distribuídos, como personal learning environments (PLEs) e MOOCs, que agregam dados de fontes formais e informais em formatos heterogêneos [F: chatti2014challenges].
- **Quem (interessados/stakeholders)**: estudantes, professores, tutores (humanos ou inteligentes), instituições educacionais (administradores e tomadores de decisão), pesquisadores e projetistas de sistema, cada um com perspectivas, objetivos e expectativas distintas em relação ao exercício de analytics [F: chatti2014challenges].
- **Por quê (objetivos)**: monitoramento e análise (acompanhar atividades e gerar relatórios para apoiar decisão de professores e instituições), predição e intervenção (estimar conhecimento e desempenho futuro para habilitar ação proativa), tutoria e mentoria, avaliação e feedback, adaptação, personalização e recomendação, e consciência e reflexão (apoiar auto avaliação de aprendizes e professores) [F: chatti2014challenges].
- **Como (métodos)**: estatística descritiva, visualização de informação, mineração de dados (classificação/predição, clusterização, regras de associação) e análise de redes sociais são as quatro famílias de método mais citadas na literatura de LA [F: chatti2014challenges].

### Níveis de análise: micro, meso e macro

Buckingham Shum, em policy brief de 2012 para o Instituto de Tecnologias da Informação em Educação da UNESCO (IITE), propõe uma tipologia de três níveis que se tornou referência para situar em que escala uma iniciativa de LA opera [F: shum2012policybrief]:

- **Micro-nível**: analytics que sustentam o rastreamento e a interpretação de dados em nível de processo para aprendizes individuais (e, por extensão, pequenos grupos). É o dado mais granular e mais pessoal — podendo revelar atividade clique a clique, geolocalização, empréstimos de biblioteca e redes interpessoais — e de maior interesse para o próprio aprendiz e para quem responde por seu sucesso [F: shum2012policybrief].
- **Meso-nível**: analytics que operam no nível da instituição individual, em geral apropriando ferramentas e práticas de business intelligence (BI) corporativo para integrar silos de dados, otimizar fluxos de trabalho, gerar dashboards institucionais e prever evasão de "clientes" (estudantes) [F: shum2012policybrief]. É o nível em que academic analytics, no sentido de Campbell e Oblinger, normalmente opera [F: shum2012policybrief].
- **Macro-nível**: analytics que viabilizam comparação e integração entre instituições — por exemplo, pesquisas de maturidade institucional ou acesso estadual/nacional a dados de avaliação padronizada ao longo da vida escolar do estudante — tendendo a se tornar cada vez mais próximas de tempo real à medida que incorporam dados de granularidade mais fina dos níveis meso e micro [F: shum2012policybrief].

Buckingham Shum destaca que esses três níveis estão convergindo: fusões e parcerias entre fornecedores de BI corporativo e plataformas de aprendizagem social estão integrando capacidade de analytics empresarial com o rastreamento de atividade de usuário em nível micro, e a agregação de históricos de interação de milhares de aprendizes entre coortes, períodos, instituições e países cria analytics de nível meso e macro com granularidade de processo sem precedentes — o que, por sua vez, pode melhorar a confiança estatística de modelos preditivos no nível micro [F: shum2012policybrief].

### O laço de retroalimentação

Reunindo o modelo de referência com os níveis de análise, o fluxo típico descrito na literatura segue: **captura** de traços de interação do aprendiz (nível micro) ou de dados agregados de curso/instituição (meso/macro) → **agregação e pré-processamento** desses dados em um formato analisável → **análise/modelagem**, usando os métodos descritos na dimensão "como" (estatística, visualização, mineração de dados, análise de redes) → **visualização e relato** dos resultados em forma compreensível para o interessado-alvo → **intervenção/ação** executada por um humano (professor, tutor, o próprio aprendiz) ou por um sistema automatizado → **retroalimentação**, em que o efeito da intervenção se torna, ele próprio, novo dado a ser capturado no ciclo seguinte [I, síntese que integra clow2012cycle, chatti2014challenges e shum2012policybrief]. A etapa de intervenção é o ponto em que o ciclo mais frequentemente se rompe na prática: Clow a identifica como o elo historicamente mais negligenciado, e por isso central ao seu argumento de "fechar o loop" [F: clow2012cycle].

## Requisitos e pressupostos

- Existência de uma fonte de dados de interação suficientemente granular para a pergunta de analytics em questão — um sistema que não registra eventos relevantes não pode alimentar o ciclo nesse nível [I].
- Um destinatário humano ou automatizado capaz de agir sobre a métrica ou predição gerada; sem essa capacidade de ação, o ciclo não fecha e a análise permanece descritiva [F: clow2012cycle].
- Clareza sobre qual das quatro dimensões do modelo de Chatti et al. está sendo usada para que a pergunta de pesquisa ou de produto faça sentido — por exemplo, confundir o "quem" (interessado) com o "por quê" (objetivo) tende a produzir indicadores que não servem a ninguém [I, generalização a partir de chatti2014challenges].
- Compatibilidade entre o nível de análise (micro, meso, macro) e a decisão que se pretende apoiar: um indicador de nível micro sobre um aprendiz individual não substitui, nem é substituído por, uma comparação de nível macro entre instituições [F: shum2012policybrief].

## Vantagens e limitações

A formulação em ciclo tem a vantagem de expor onde, na prática, uma iniciativa de LA costuma falhar — tipicamente na etapa de intervenção, não na de captura ou análise de dados [F: clow2012cycle]. Como limitação, o próprio Clow nota que otimizar para a métrica errada (uma proxy de aprendizagem, e não a aprendizagem em si) é um risco sistemático do modelo, o que o leva a insistir que a avaliação (assessment) deve ser o ponto de ancoragem do que é otimizado [F: clow2012cycle, conforme descrito em material de apresentação do autor — ver Lacunas]. O modelo de quatro dimensões de Chatti et al., por sua vez, é descritivo e taxonômico: ajuda a mapear a literatura e identificar lacunas de pesquisa, mas não prescreve, por si, qual combinação de dimensões produz impacto em aprendizagem [I].

## Alternativas e comparações

| Modelo | Unidade de análise | Ênfase | Fonte |
|---|---|---|---|
| Capture–Report–Predict–Act–Refine (Campbell & Oblinger) | Ciclo institucional de academic analytics | Decisão administrativa (matrícula, retenção, captação de recursos) | [F: clow2012cycle] atribuindo a [F: campbelldeblois2007academic] |
| Ciclo de learning analytics (Clow) | Laço aprendiz–dado–métrica–intervenção | Fechamento do loop pedagógico, ancorado em teoria da aprendizagem | [F: clow2012cycle] |
| Modelo de referência de quatro dimensões (Chatti et al.) | O quê / quem / por quê / como | Mapeamento taxonômico de qualquer iniciativa de LA, independente de escala | [F: chatti2014challenges] |
| Micro/meso/macro (Buckingham Shum) | Escala institucional da análise | Situar uma iniciativa entre aprendiz individual, instituição e sistema multi-institucional | [F: shum2012policybrief] |

Os quatro modelos não competem entre si: o ciclo de Clow descreve o fluxo temporal de uma iniciativa; o modelo de Chatti et al. descreve suas dimensões constitutivas; e a tipologia de Buckingham Shum descreve sua escala. Uma mesma iniciativa de LA pode ser descrita simultaneamente pelos três [I].

## Métricas e métodos de avaliação

A avaliação de uma iniciativa de LA, no próprio ciclo, ocorre na etapa de retroalimentação: o critério mínimo, segundo Clow, é se a intervenção de fato chegou ao aprendiz e gerou mudança observável [F: clow2012cycle]. Chatti et al. relatam, a partir de Dyckhoff et al., que a avaliação de ferramentas de LA deveria cobrir três objetivos — informar explicitamente o desenho da ferramenta, provocar uma reação comportamental do professor e provocar uma reação comportamental do estudante — mas que a literatura até então revisada reportava poucas publicações medindo de fato a reação comportamental de professores e estudantes [F: chatti2014challenges]. Métricas específicas de qualidade preditiva (A'/AUC, kappa, precisão, revocação) pertencem à camada de modelagem de cada técnica, não ao ciclo em si, e são tratadas junto às técnicas individuais noutros documentos do domínio e de `aprendizagem-adaptativa`.

## Exemplo técnico independente de domínio

```
estado: captura(evento_interação) -> buffer_bruto
loop a cada janela_de_agregação:
    dados_agregados = pre_processar(buffer_bruto)         # limpeza, junção, anonimização
    metricas = analisar(dados_agregados, metodo)          # estatística | mineração de dados | SNA | visualização
    para cada interessado in {aprendiz, professor, instituição, pesquisador}:
        relato = adaptar_para(metricas, interessado.objetivo)  # quem / por quê
        se relato.aciona_intervencao:
            intervencao = decidir_acao(relato)             # humana ou automatizada
            aplicar(intervencao, aprendiz_ou_turma)
            registrar(intervencao) -> buffer_bruto          # fecha o loop: a ação vira novo dado
    senão:
        registrar("ciclo sem intervenção — loop não fechado")  # falha típica apontada por Clow
```

## Relações com outros conceitos

Complementa `lae.found.la-vs-edm`, que descreve as duas tradições de pesquisa cujos métodos alimentam a etapa de "análise/modelagem" deste ciclo. Relaciona-se com `adp.lm.open-learner-model`, na medida em que um open learner model é uma forma específica de "visualização e relato" da etapa de métricas voltada diretamente ao aprendiz (nível micro). Complementa `iop.lr.caliper`, especificação de eventos de aprendizagem que formaliza tecnicamente a etapa de captura do ciclo — este documento não aprofunda formatos de evento, que ficam em `interoperabilidade`.

## Lacunas e questões abertas

- O artigo integral de Clow (2012), "The Learning Analytics Cycle: Closing the loop effectively" (LAK '12, DOI 10.1145/2330601.2330636), não pôde ser acessado nesta sessão: o repositório Open Research Online da Open University (via core.ac.uk) bloqueou o acesso automatizado (erro 403 / desafio Cloudflare). O conteúdo deste documento sobre o ciclo de quatro elementos (Learners, Data, Metrics, Interventions) e sua ancoragem em Kolb e Schön foi reconstruído a partir das notas de apresentação do próprio autor publicadas em slide deck (SlideShare) e de citações em fontes acadêmicas secundárias (um artigo da ASEE e o capítulo de Chatti et al. 2014); a formulação exata dos quatro elementos no texto do artigo não foi conferida palavra por palavra.
- O modelo de cinco estágios "Capture, Report, Predict, Act, Refine" é consistentemente atribuído a Campbell e Oblinger (2007) por Clow (segundo as fontes secundárias acima), mas essa rotulação exata não foi encontrada no texto integral do artigo "Academic Analytics: A New Tool for a New Era" (Campbell, DeBlois e Oblinger, EDUCAUSE Review 42(4), 2007) consultado nesta sessão — é possível que a formulação exata venha de um white paper companheiro (referência interna "PUB6101" da EDUCAUSE) não localizado em versão acessível. Registrado como "não verificado" na forma exata.
- Greller e Drachsler (2012), "Translating Learning into Numbers: A Generic Framework for Learning Analytics" (Educational Technology & Society), propõem um framework de seis dimensões (competências, restrições, métodos, objetivos — distinguindo reflexão de predição —, dados e interessados) frequentemente citado ao lado do modelo de Chatti et al.; não foi possível obter o texto integral nesta sessão (apenas resumos de terceiros), por isso o framework não foi incluído no corpo do documento e a chave bibliográfica correspondente não foi registrada em `fontes`. Fica como lacuna para expansão futura.
- Pardo e Siemens (2014) e Slade e Prinsloo (2013) propõem princípios éticos específicos para LA (transparência, controle do estudante sobre os dados, segurança e responsabilização, no primeiro caso; seis princípios incluindo LA como prática moral e o estudante como agente, no segundo), citados por Chatti et al. (2014); por não terem sido consultados em texto integral nesta sessão, são apenas mencionados aqui como referência para aprofundamento e não entraram no corpo do texto nem no frontmatter de fontes. Questões de consentimento e privacidade em sentido estrito, incluindo LGPD, ficam fora do escopo deste domínio por definição do brief (`lae.brief`) e devem ser aprofundadas em `privacidade-seguranca-e-governanca` ou em `dados-pesquisa-e-eventos`.
- Não foi possível confirmar, com fonte primária, se a tipologia micro/meso/macro de Buckingham Shum (2012) foi adotada formalmente por SoLAR ou pela literatura de LAK como terminologia padrão, ou se permanece uma proposta entre outras; o texto a apresenta como a formulação mais citada, com base no próprio documento primário consultado, mas sem levantamento sistemático de adoção posterior.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| clow2012cycle | academico (texto integral não acessado; via slides do autor e citações secundárias) | 2026-10-29 |
| campbelldeblois2007academic | academico | 2026-10-29 |
| chatti2014challenges | academico | 2026-10-29 |
| shum2012policybrief | normativo (policy brief UNESCO/IITE) | 2026-10-29 |
