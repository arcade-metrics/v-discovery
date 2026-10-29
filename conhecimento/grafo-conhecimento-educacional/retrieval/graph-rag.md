---
id: kg.ret.graph-rag
titulo: Graph RAG
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [edge2024graphrag, microsoft2026graphragdocs, abdelmagied2025graphrag, hogan2021knowledgegraphs]
relacoes:
  - { tipo: depende-de, alvo: kg.found.knowledge-graphs }
  - { tipo: complementa, alvo: kg.ret.text-to-query }
  - { tipo: alternativa-a, alvo: kg.ret.graph-embeddings }
  - { tipo: relacionado-a, alvo: kg.eng.construction }
  - { tipo: relacionado-a, alvo: kg.mod.layer-separation }
termos: [Graph RAG, RAG, query-focused summarization, QFS, graph index, community detection, Leiden, community summary, global sensemaking, comprehensiveness, diversity, empowerment, directness, win rate, Personal Knowledge Graph]
---

# Graph RAG

## Definição e terminologia

**GraphRAG** é "a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text" [F: edge2024graphrag, resumo].

A motivação declarada: RAG convencional "fails on global questions directed at an entire text corpus, such as 'What are the main themes in the dataset?', since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task"; métodos de QFS anteriores, por sua vez, "do not scale to the quantities of text indexed by typical RAG systems" [F: edge2024graphrag, resumo].

O que não é: Graph RAG não é consulta a um grafo curado. É a construção de um grafo *a partir de texto* para servir de índice. [I] Essa distinção é central neste domínio e é desenvolvida abaixo.

## Problema que resolve

[F: edge2024graphrag, resumo] identifica a lacuna: perguntas globais sobre um corpus inteiro. RAG por similaridade recupera trechos relevantes a uma consulta específica; não consegue responder "quais são os temas principais", porque nenhum trecho contém a resposta.

[I] Em educação, as perguntas globais são comuns: "que conceitos este material cobre", "onde o curso é mais fraco", "que lacunas existem entre dois módulos".

## Fundamentos e funcionamento

### O pipeline

A abordagem "uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities. Given a question, each community summary is used to generate a partial response, before all partial responses are again summarized in a final response to the user" [F: edge2024graphrag, resumo].

Detalhes verificados [F: edge2024graphrag]:

- **Particionamento**: "community detection (e.g., Leiden, Traag et al., 2019) is used to partition the graph index"; uma variedade de algoritmos de detecção de comunidade poderia ser usada, e os autores remetem a surveys de Fortunato (2010) e Jin et al. (2021). Na implementação usaram Leiden, com a biblioteca graspologic [F: edge2024graphrag, §5, §Apêndice].
- **Hierarquia de comunidades**: resumos são gerados por nível. Para comunidades de nível mais alto, se todos os resumos de elemento couberem no limite de tokens da janela de contexto, procede-se diretamente; caso contrário, substituem-se iterativamente resumos de subcomunidade (mais curtos) pelos resumos de elemento (mais longos) até caberem na janela [F: edge2024graphrag, §2].
- **Janela de contexto**: foi usada janela fixa de 8 mil tokens para gerar resumos de comunidade, respostas de comunidade e respostas globais; a indexação do grafo usou janela de 600 tokens [F: edge2024graphrag, §5].
- **Chunking**: o texto é dividido em pedaços de tamanho pré-especificado, o que "ensures relevant information is distributed across chunks, rather than concentrated (and potentially lost) in a single context window" [F: edge2024graphrag, §2].

### Avaliação e resultados

Dois conjuntos de dados na faixa de um milhão de tokens: transcrições de podcast (1.669 pedaços de 600 tokens com sobreposição de 100, totalizando 1 milhão de tokens) e artigos de notícia (3.197 pedaços, 1,7 milhão de tokens) [F: edge2024graphrag, §5].

Os índices resultantes: 8.564 nós e 20.691 arestas para o conjunto de podcasts; 15.754 nós e 19.520 arestas para o de notícias [F: edge2024graphrag, §5.1].

Quatro critérios de avaliação, entre eles **comprehensiveness** ("how much detail does the answer provide to cover all aspects"), diversity, empowerment e directness; os autores observam que "directness is effectively in opposition to comprehensiveness and diversity" e o usam como teste de validade [F: edge2024graphrag, §4, §5.1].

Resultados [F: edge2024graphrag, §5.1]:

| Comparação | Podcast | Notícias |
|---|---|---|
| Comprehensiveness, abordagens globais vs. RAG vetorial | 72-83% de taxa de vitória (p<.001) | 72-80% (p<.001) |
| Diversity, idem | 75-82% (p<.001) | 62-71% (p<.01) |

"Our use of directness as a validity test confirmed that vector RAG produces the most direct responses across all comparisons." Para **empowerment**, os resultados foram mistos, tanto entre abordagens globais e RAG vetorial quanto entre GraphRAG e sumarização do texto fonte [F: edge2024graphrag, §5.1].

[I] Leitura honesta dos números: a vantagem é clara e estatisticamente significativa para abrangência e diversidade de respostas a perguntas globais; não é uma melhoria geral de RAG. Para perguntas específicas, o RAG vetorial continua mais direto.

### Implementação

A Microsoft Research mantém documentação pública do GraphRAG, organizada em Indexing, Prompt Tuning, Query, Configuration e CLI [F: microsoft2026graphragdocs].

### Em educação

Abdelmagied et al. propõem um pipeline de Graph RAG para MOOCs, motivado por três problemas declarados: ausência de interação direta entre aluno e instrutor; alucinação de modelos de linguagem, que RAG endereça recuperando documentos antes de gerar; e o fato de a aplicação de RAG entre MOOCs ser limitada por material de aprendizagem não estruturado. O pipeline "leverages Educational Knowledge Graphs (EduKGs) and Personal Knowledge Graphs (PKGs) to guide learners to understand knowledge concepts" na plataforma CourseMapper [F: abdelmagied2025graphrag, resumo].

A avaliação é exploratória e pequena: três instrutores (um professor e dois assistentes) avaliaram os pipelines em três MOOCs de suas áreas — Learning Analytics, Interação Humano-Computador e Tecnologias Web — cobrindo 6 a 8 conceitos marcados como "não compreendidos" por MOOC e 30 a 40 pares pergunta-resposta cada [F: abdelmagied2025graphrag, §4.1]. Os autores afirmam que os resultados "show the potential of Graph RAG to empower learners", sem alegar efeito demonstrado [F: abdelmagied2025graphrag, resumo].

[I] Com n = 3 avaliadores, o trabalho indica viabilidade, não eficácia.

[I] Dois pontos desse trabalho importam para este domínio: (i) o grafo educacional e o grafo pessoal são estruturas distintas, o que corrobora kg.mod.layer-separation; (ii) o argumento declarado é que material não estruturado limita RAG — ou seja, o grafo curado é o que torna a recuperação possível entre cursos.

### A distinção decisiva

[I] Há dois usos de "Graph RAG" que convém não confundir:

| | Grafo construído do texto | Grafo curado consultado |
|---|---|---|
| Origem do grafo | extraído por LLM dos documentos [F: edge2024graphrag] | curadoria e padrões |
| Confiabilidade | a do extrator | a da curadoria |
| Pergunta que responde bem | global, de sensemaking | específica, estrutural |
| Papel do LLM | constrói e resume | traduz pergunta em consulta (ver kg.ret.text-to-query) |

Um grafo curricular curado não precisa de detecção de comunidade para responder "quais são os pré-requisitos de X" — isso é uma consulta SPARQL. Precisa de Graph RAG quando a pergunta é sobre o corpus de materiais, não sobre a estrutura curricular.

## Requisitos e pressupostos

- Um corpus de texto, se o grafo for construído a partir dele.
- Orçamento de LLM para a indexação, que é a etapa cara: cada documento passa por extração e cada comunidade por sumarização [F: edge2024graphrag, §2].
- Re-indexação quando o corpus muda; os resumos de comunidade são pré-gerados [F: edge2024graphrag, resumo].

## Vantagens e limitações

Vantagens: responde perguntas globais que RAG vetorial não responde, com vantagem medida em abrangência e diversidade [F: edge2024graphrag, §5.1]; a hierarquia de comunidades permite escolher o nível de granularidade; o índice é inspecionável, ao contrário de um índice vetorial.

Limitações: custo de indexação; o grafo extraído herda os erros do extrator; empowerment não melhorou de forma consistente [F: edge2024graphrag, §5.1]; perguntas específicas continuam melhor servidas por RAG vetorial [F: edge2024graphrag, §5.1]; e os resultados vêm de dois conjuntos de dados em domínios não educacionais.

## Alternativas e comparações

| Pergunta | Abordagem |
|---|---|
| "Quais são os pré-requisitos de X?" | SPARQL sobre grafo curado (kg.std.sparql) |
| "Onde este material explica frações?" | RAG vetorial |
| "Que temas este corpus de materiais cobre?" | Graph RAG [F: edge2024graphrag] |
| "Que conceitos faltam entre dois módulos?" | grafo curado + Graph RAG sobre os materiais [I] |
| "Que conceitos são parecidos com X?" | embeddings de grafo (kg.ret.graph-embeddings) |

## Métricas e métodos de avaliação

Os critérios de Edge et al.: comprehensiveness, diversity, empowerment e directness, avaliados por comparação par a par com taxa de vitória [F: edge2024graphrag, §4]. A validação adicional usou extração de alegações: "comprehensiveness: measured as the average number of claims extracted from the answers" [F: edge2024graphrag, §5].

[I] Em educação, essas métricas são insuficientes: a pergunta relevante é se a resposta ajuda o aluno a aprender, não se é abrangente. Isso pertence a adp.eval.educational-effectiveness.

## Exemplo técnico independente de domínio

```
# fluxo de indexação (conforme descrito em edge2024graphrag, §2)
documentos
  → chunking (600 tokens, sobreposição 100)
  → extração de entidades e relações por LLM
  → grafo de entidades
  → detecção de comunidade (Leiden)
  → hierarquia de comunidades
  → sumarização por comunidade, respeitando a janela de contexto

# fluxo de consulta global
pergunta
  → para cada resumo de comunidade: resposta parcial
  → sumarização das respostas parciais
  → resposta final
```

[I] O desenho híbrido que este domínio recomenda: o grafo conceitual curado responde perguntas estruturais por SPARQL; o Graph RAG indexa os materiais e liga suas comunidades aos conceitos do grafo curado por alinhamento. As duas estruturas se referenciam pelo IRI de conceito, como em kg.mod.layer-separation.

## Relações com outros conceitos

Depende de kg.found.knowledge-graphs. Complementa kg.ret.text-to-query (o outro caminho pelo qual um LLM usa o grafo). Alternativa a kg.ret.graph-embeddings. Relaciona-se com kg.eng.construction (o pipeline de indexação é um pipeline de construção) e kg.mod.layer-separation.

## Lacunas e questões abertas

- Os resultados são de dois conjuntos de dados, nenhum educacional [F: edge2024graphrag, §5].
- A avaliação educacional disponível tem três avaliadores e três cursos [F: abdelmagied2025graphrag, §4.1]: é indício de viabilidade, não evidência de eficácia.
- O custo de indexação não foi levantado em nenhuma fonte consultada em termos monetários ou de tempo.
- A documentação do GraphRAG da Microsoft foi aberta apenas na página inicial [F: microsoft2026graphragdocs]; parâmetros, versões e requisitos não foram examinados.
- [H] O desenho híbrido proposto acima (grafo curado + índice Graph RAG ligados por IRI) parece o arranjo certo, mas não foi encontrado na literatura consultada nem testado.
- Não foi investigado como evitar que o grafo extraído por LLM contradiga o grafo curado quando ambos cobrem o mesmo conceito.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| edge2024graphrag | academico | 2026-10-29 |
| microsoft2026graphragdocs | fornecedor | 2026-10-29 |
| abdelmagied2025graphrag | academico | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
