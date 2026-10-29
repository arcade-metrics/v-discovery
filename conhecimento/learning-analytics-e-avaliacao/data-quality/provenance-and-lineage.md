---
id: lae.dq.provenance-and-lineage
titulo: Proveniência e linhagem de dados em learning analytics
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [buneman2001whywhere, w3c2013provo, gardner2018replicability, haim2023openscience, gasevic2015notforget]
relacoes:
  - { tipo: relacionado-a, alvo: lae.found.la-vs-edm }
  - { tipo: depende-de, alvo: lae.dq.bias-and-validity }
termos: [proveniência, data lineage, why provenance, where provenance, reprodutibilidade, replicação, versionamento de pipeline, PROV-O]
---

# Proveniência e linhagem de dados em learning analytics

## Definição e terminologia

Proveniência de dados é o registro que explica a origem de um item de dado e o processo pelo qual ele chegou ao seu estado atual — entradas, entidades, sistemas e processos que o influenciaram [I, com base em F: buneman2001whywhere]. Na literatura de bancos de dados, Buneman, Khanna e Tan formalizaram essa noção dividindo-a em duas perguntas distintas sobre um item de saída de uma consulta: "why provenance" (que dados de origem contribuíram para a existência do item) e "where provenance" (de que localização nos dados de origem o item foi efetivamente copiado) [F: buneman2001whywhere]. Essa distinção segue relevante como vocabulário conceitual mesmo fora de bancos relacionais: perguntar "por que este indicador tem este valor" (quais eventos de origem contribuíram) é diferente de perguntar "de onde veio exatamente este número" (qual registro específico foi lido) [I].

**Linhagem de dados** (*data lineage*) é um termo mais operacional e corrente na prática de engenharia de dados: descreve o mapeamento do ciclo de vida de um dado — onde ele se originou, como se transformou ao longo de um pipeline e onde está armazenado agora [I]. Na prática as duas palavras são usadas de forma intercambiável; quando se distinguem, proveniência tende a enfatizar a origem e a confiabilidade de um registro específico, e linhagem tende a enfatizar o fluxo e as transformações de um conjunto de dados através de um sistema [I].

Aplicado a learning analytics (LA), proveniência e linhagem significam poder responder, para qualquer número que aparece num indicador, painel ou relatório: de que eventos brutos ele veio, que transformações (filtros, agregações, junções, imputação, normalização) foram aplicadas, com qual versão do código e dos parâmetros, e em que momento [I]. O que não é: proveniência não é o esquema do evento bruto em si (isso é tratado em `dados-pesquisa-e-eventos`), nem é a conformidade legal do uso do dado (LGPD, FAIR — também fora deste domínio, ver `00-brief.md`); aqui o interesse é exclusivamente a rastreabilidade do caminho do dado até o indicador analítico [I].

## Problema que resolve

Um indicador de LA (taxa de engajamento, score de risco de evasão, nota agregada de uma rubrica) costuma passar por várias etapas entre o evento bruto e o número exibido: filtragem de outliers, escolha de uma janela de tempo, definição de "sessão", agregação por aluno ou por turma, eventual imputação de dados faltantes. Sem registro dessas etapas, dois efeitos problemáticos aparecem: (1) impossibilidade de auditar por que um aluno específico recebeu um sinalizador de risco, o que é particularmente grave quando esse sinalizador influencia uma decisão institucional sobre o aluno [I]; e (2) impossibilidade de reproduzir ou replicar um resultado de pesquisa ou um relatório de produto meses depois, quando o pipeline mudou silenciosamente [I]. A literatura de educational data mining (EDM) e LA documentou esse segundo problema de forma sistemática nos últimos anos, configurando o que pode ser descrito como uma preocupação paralela à "crise de replicação" discutida em outras ciências empíricas [I].

Gardner, Yang, Baker e Brooks argumentam que, em EDM e campos correlatos, a reprodutibilidade de modelos de machine learning enfrenta barreiras experimentais, metodológicas e de dados que não se resolvem apenas compartilhando código-fonte; eles propuseram o MOOC Replication Framework (MORF), um framework de código aberto para replicação ponta a ponta que executa código em contêineres com DOIs por configuração de execução, permitindo auditar exatamente qual versão de dado e de pipeline gerou qual resultado [F: gardner2018replicability]. Haim, Shaw e Heffernan revisaram 133 artigos da conferência Learning Analytics and Knowledge (LAK) de 2023 quanto a práticas de ciência aberta e tentativa de reprodução: menos da metade adotava práticas padrão de ciência aberta, cerca de 5% atendia plenamente aos princípios definidos pelos autores, e nenhum dos artigos pôde ser reproduzido no tempo alocado (15 minutos por artigo) [F: haim2023openscience]. Esse resultado é um indício direto, na própria comunidade de LA, de que a ausência de proveniência e linhagem documentadas compromete a confiabilidade dos indicadores publicados, não só de artigos acadêmicos [I].

## Fundamentos e funcionamento

### O que versionar e documentar

Para que um indicador de LA seja rastreável, a prática de engenharia de dados sugere versionar e registrar, no mínimo [I]:

- a fonte do dado bruto (sistema de origem, esquema, data de extração);
- a versão do pipeline de transformação (código, parâmetros, bibliotecas e suas versões) que gerou o indicador a partir do bruto;
- as decisões de modelagem incorporadas na transformação (definição operacional de "sessão", limiares de outlier, método de imputação de dados faltantes, janela temporal de agregação);
- a data e o contexto de execução (quando o pipeline rodou, sobre qual recorte de dados).

Gardner et al. ilustram esse princípio na prática ao descrever a dificuldade de replicar análises em dados MOOC — privados, de formatos heterogêneos e volumosos — sem uma infraestrutura que fixe essas decisões em contêineres executáveis versionados [F: gardner2018replicability]. A mesma lógica se aplica a um pipeline de indicadores de produto: se a definição de "sessão ativa" mudar silenciosamente de uma versão do pipeline para outra, dois relatórios que usam o nome "engajamento" deixam de ser comparáveis sem que ninguém perceba [I].

### Why e where provenance aplicadas a um indicador

Usando a distinção de Buneman, Khanna e Tan [F: buneman2001whywhere]: a "where provenance" de um valor de indicador aponta para os registros de evento específicos que, somados, compõem aquele número (por exemplo, a lista de respostas corretas que compõem uma taxa de acerto); a "why provenance" aponta para o conjunto mais amplo de condições e dados que tiveram influência na existência daquele número (por exemplo, o fato de o aluno ter sido elegível para a atividade, de a atividade ter sido entregue dentro do prazo considerado, de o esquema de pontuação vigente na época ser aquele) [I]. Projetar um sistema de proveniência que responda só à primeira pergunta é mais simples, mas responde a perguntas de auditoria mais limitadas do que as que um comitê de ética ou um aluno contestando uma decisão institucional provavelmente fará [I].

### PROV-O como modelo de referência

O W3C publicou o PROV Ontology (PROV-O) como Recomendação em 30 de abril de 2013, uma codificação em OWL2 do modelo de dados PROV-DM para representar e trocar registros de proveniência entre sistemas diferentes [F: w3c2013provo]. Seu núcleo define três classes — `Entity` (uma coisa, física, digital ou conceitual, com aspectos fixos), `Activity` (algo que ocorre ao longo de um período de tempo e age sobre ou com entidades, usando, transformando ou gerando-as) e `Agent` (algo responsável por uma atividade, pela existência de uma entidade, ou pela atividade de outro agente) — e relações como `wasGeneratedBy` (liga uma entidade à atividade que a produziu), `used` (liga uma atividade a uma entidade que ela utilizou), `wasAssociatedWith` (liga uma atividade ao agente responsável), `wasDerivedFrom` (liga uma entidade a outra da qual foi derivada) e `wasAttributedTo` (liga uma entidade ao agente a quem ela é atribuída) [F: w3c2013provo]. PROV-O é extensível a domínios de aplicação específicos [F: w3c2013provo]. Para LA, esse vocabulário dá uma forma padronizada de dizer, por exemplo, que um "indicador de risco de evasão" (`Entity`) `wasGeneratedBy` uma execução de pipeline (`Activity`) que `used` um conjunto de eventos brutos (`Entity`) e `wasAssociatedWith` uma versão de código mantida por uma equipe (`Agent`) [I]. O aprofundamento de PROV-O e de sua representação em RDF/OWL, fora do escopo deste domínio, fica em `grafo-conhecimento-educacional` (ver Relações com outros conceitos).

## Requisitos e pressupostos

- Existência de um identificador estável para cada evento bruto e para cada execução de pipeline, sem os quais não há o que linkar [I].
- Separação explícita, na arquitetura de dados, entre a camada de evento bruto (imutável) e a camada de indicador derivado (recalculável), para que a proveniência aponte sempre de volta à camada bruta e não a outro derivado já transformado [I].
- Controle de versão do código do pipeline (não apenas dos dados), já que a mesma entrada processada por duas versões de pipeline pode produzir indicadores diferentes [F: gardner2018replicability].
- Vontade organizacional de investir tempo em documentação e metadados de transformação, que não geram valor analítico imediato e por isso tendem a ser cortados sob pressão de prazo — um padrão já observado na baixa adoção de práticas de ciência aberta em LA mesmo dentro da comunidade acadêmica [F: haim2023openscience].

## Vantagens e limitações

Rastrear proveniência e linhagem permite auditar decisões individuais sobre alunos, diagnosticar divergências entre relatórios que deveriam coincidir e sustentar replicação de achados de pesquisa ou de produto [I]. A limitação central é de custo: instrumentar proveniência completa (nível `why`, não só `where`) exige capturar metadados em cada etapa de transformação, o que aumenta a complexidade de engenharia e pode não compensar para indicadores de baixo risco [I]. Há também um limite epistêmico: documentar de onde um número veio não garante que o número meça o que se pretende medir — essa é uma questão de validade de construto, tratada em `lae.dq.bias-and-validity`, e proveniência não a resolve sozinha [I].

## Alternativas e comparações

| Abordagem | O que garante | O que não garante |
|---|---|---|
| Logging ad hoc (comentários em código, planilhas de decisão) | Baixo custo inicial | Não é consultável sistematicamente; se perde com rotatividade de equipe [I] |
| Metadados de linhagem em ferramenta de engenharia de dados (catálogo de dados, grafo de dependência de pipeline) | Rastreamento automático de transformações e dependências entre tabelas [I] | Tipicamente captura "where" mas não necessariamente o "why" completo de uma decisão de modelagem [I] |
| Modelo de proveniência padronizado (ex. PROV-O) | Vocabulário interoperável, extensível e consultável como grafo [F: w3c2013provo] | Exige modelagem explícita de entidades, atividades e agentes; maior esforço de adoção do que um catálogo de linhagem comum [I] |
| Framework de replicação executável (ex. MORF) | Reprodutibilidade ponta a ponta de uma análise, incluindo ambiente de execução [F: gardner2018replicability] | Desenhado para pesquisa em lote, não para rastreabilidade em tempo real de um indicador de produto [I] |

## Métricas e métodos de avaliação

Não há uma métrica única de "qualidade de proveniência"; a literatura de reprodutibilidade em EDM/LA usa como proxy a taxa de reprodução bem-sucedida de um estudo ou pipeline a partir do que foi documentado. Gardner et al. relatam a aplicação do MORF a uma replicação em escala com configurações e trilhas de execução publicamente auditáveis via DOI [F: gardner2018replicability]; Haim, Shaw e Heffernan relatam, como medida de linha de base da comunidade de LA, que nenhum dos 133 artigos revisados pôde ser reproduzido dentro de um tempo fixo por avaliador, e que a adesão a princípios de ciência aberta (disponibilização de dados, código e materiais) foi o fator limitante mais citado [F: haim2023openscience]. Para um pipeline de produto, o equivalente prático é a capacidade de, dado um indicador exibido em uma data passada, recalculá-lo exatamente a partir dos metadados registrados e obter o mesmo valor [I].

## Exemplo técnico independente de domínio

```
registro_proveniência(indicador_id, valor, timestamp):
    entidade_saida = Entity(id=indicador_id, valor=valor)
    atividade = Activity(
        id=pipeline_execucao_id,
        versao_codigo=git_commit_hash,
        parametros={janela: "7d", limiar_outlier: 3.0}
    )
    entidade_saida.wasGeneratedBy(atividade)
    para cada evento_bruto em eventos_usados:
        atividade.used(Entity(id=evento_bruto.id, fonte=evento_bruto.sistema_origem))
    atividade.wasAssociatedWith(Agent(id=equipe_responsavel))
    persistir(entidade_saida, atividade, relacoes)  # grafo de proveniência consultável
```

Uma consulta típica sobre esse grafo seria "liste todos os eventos brutos e a versão de código que geraram o indicador X do aluno Y na data Z" — equivalente a reconstruir a "why provenance" descrita por Buneman, Khanna e Tan para aquele valor específico [I, com base em F: buneman2001whywhere].

## Relações com outros conceitos

Proveniência e linhagem são pré-condição prática para a reprodutibilidade discutida também na tradição de LA/EDM e para a auditabilidade de indicadores tratados no restante do domínio `learning-analytics-e-avaliacao` (`lae.found.la-vs-edm`). Depende de, e é complementado por, o tratamento de viés e validade dos dados de origem (`lae.dq.bias-and-validity`): um pipeline com proveniência impecável ainda pode propagar um dado de entrada enviesado ou com baixa validade de construto — rastreabilidade não é sinônimo de qualidade do dado em si [I]. O aprofundamento técnico de PROV-O em RDF/OWL como padrão de representação de conhecimento (classes, propriedades, serialização) pertence a `grafo-conhecimento-educacional`; no momento da redação deste documento não foi encontrado, na base, um documento equivalente a `kg.standards.prov-o` (a pasta `grafo-conhecimento-educacional/standards/` ainda não contém esse arquivo), portanto nenhuma relação tipada foi declarada no frontmatter para esse id — ver Lacunas.

## Lacunas e questões abertas

- O id `kg.standards.prov-o` não existe ainda na base no momento desta pesquisa (checado em `grafo-conhecimento-educacional/standards/`, pasta sem esse arquivo); quando for criado, este documento deve ganhar a relação `{ tipo: complementa, alvo: kg.standards.prov-o }` no frontmatter.
- Não foi localizado, na pesquisa feita nesta sessão, um padrão de proveniência específico da comunidade de LA (equivalente a PROV-O mas desenhado para indicadores educacionais); a adoção de PROV-O em produtos de LA, se existe, não foi verificada.
- O artigo de Gašević, Dawson e Siemens aqui citado («Let's not forget: Learning analytics are about learning», TechTrends 59(1), 2015) argumenta pela necessidade de ancorar LA em teoria educacional, mas não é, estritamente, um artigo sobre proveniência técnica de dados; ele é citado aqui como pano de fundo da preocupação da comunidade com a solidez dos indicadores, não como fonte de método de linhagem — essa é uma inferência do redator do documento, registrada como [I] no texto, e deve ser revisada se uma fonte mais direta de Gašević et al. sobre proveniência for localizada depois.
- Não verificado: se existem estudos de caso publicados de implementação de proveniência estilo PROV-O num pipeline real de learning analytics (em oposição a MOOCs/MORF, que é um framework de replicação de pesquisa, não de proveniência de indicador de produto).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| buneman2001whywhere | academico | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| gardner2018replicability | academico | 2026-10-29 |
| haim2023openscience | academico | 2026-10-29 |
| gasevic2015notforget | academico | 2026-10-29 |
