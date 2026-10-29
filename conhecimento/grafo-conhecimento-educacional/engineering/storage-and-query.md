---
id: kg.eng.storage-and-query
titulo: Armazenamento e consulta
tipo: comparacao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [jena2026tdb2, rdf4j2026about, neo4j2026graphconcepts, gqlstandards2024, opencypher2026, w3c2013sparql11overview, w3c2013sparql11query, hogan2021knowledgegraphs]
relacoes:
  - { tipo: implementado-por, alvo: kg.std.sparql }
  - { tipo: depende-de, alvo: kg.found.rdf-vs-property-graphs }
  - { tipo: complementa, alvo: kg.mod.layer-separation }
  - { tipo: relacionado-a, alvo: kg.found.reasoning }
  - { tipo: relacionado-a, alvo: kg.eng.quality }
termos: [triplestore, graph database, TDB2, Fuseki, RDF4J, Memory Store, Native Store, ElasticsearchStore, Neo4j, Cypher, GQL, transação, inferência em banco]
---

# Armazenamento e consulta

## Definição e terminologia

Um **triplestore** armazena triplas RDF e responde consultas SPARQL. Um **banco de grafo de propriedades** armazena nós e relações com rótulos e propriedades, e responde consultas em Cypher ou GQL.

Este documento registra o que as fontes de fornecedor verificadas afirmam, sem comparar desempenho — nenhum benchmark foi consultado.

## Fundamentos e funcionamento

### Apache Jena

"TDB2 is a component of Apache Jena for RDF storage and query. It supports the full range of Jena APIs. TDB2 can be used as a high performance RDF store on a single machine. TDB2 can be used with Apache Jena Fuseki." TDB1 é "the previous generation native storage system for Jena" [F: jena2026tdb2].

Diferenças declaradas de TDB2 em relação a TDB1 [F: jena2026tdb2]:

- "No size limits on transactions: bulk uploads into a live Fuseki can be 100's of millions of triples."
- "Models and Graphs can be passed across transactions."
- "Transactional only (there is currently no 'autocommit' mode)."
- "Better transaction control."
- "No queue of delayed updates" e "no backlog problems."
- "'Writer pays' — readers don't."
- "Datatypes of numerics preserved; xsd:doubles supported."

E a advertência: "TDB2 is not compatible with TDB1" [F: jena2026tdb2].

[I] O ponto "writer pays" importa num grafo educacional: leituras são a carga dominante (consultas de currículo, diagnóstico), escritas acontecem em lotes de curadoria. O modelo favorece esse perfil.

### Eclipse RDF4J

"Eclipse RDF4J is an open source modular Java framework for working with RDF data. This includes parsing, storing, inferencing and querying of/over such data. It offers an easy-to-use API that can be connected to all leading RDF storage solutions" [F: rdf4j2026about].

"RDF4J fully supports the SPARQL 1.1 query and update language for expressive querying and offers transparent access to remote RDF repositories using the exact same API as for local access." Suporta "all mainstream RDF file formats, including RDF/XML, Turtle, N-Triples, N-Quads, JSON-LD, TriG and TriX" [F: rdf4j2026about].

O núcleo "provides a set of vendor-neutral APIs for highly scalable storage, reasoning, and retrieval of RDF and OWL"; bancos de terceiros implementam essas APIs [F: rdf4j2026about].

Bancos próprios [F: rdf4j2026about]:

| Banco | Descrição |
|---|---|
| Memory Store | "a transactional RDF database using main memory with optional persistent sync to disk. It is fast with excellent performance for small datasets. It scales with amount of RAM available." |
| Native Store | "a transactional RDF database using direct disk IO for persistence. It is a more scalable solution than the memory store, with a smaller memory footprint, and also offers better consistency and durability. It is currently aimed at medium-sized datasets in the order of 100 million triples." |
| ElasticsearchStore | "an experimental RDF database that uses Elasticsearch for storage", útil "if you are already using Elasticsearch for other things"; "a good usecase is if you need reference data or an ontology for your application. The built-in read cache makes it a good choice for data that updates infrequently." |

[I] A descrição do ElasticsearchStore — dados de referência ou ontologia, atualizados com pouca frequência, com cache de leitura — descreve exatamente a camada 1 de kg.mod.layer-separation. É experimental, segundo o próprio fornecedor.

A ordem de grandeza declarada para o Native Store, cerca de 100 milhões de triplas, é referência útil: um grafo curricular fica ordens de magnitude abaixo disso; uma camada de observações pode ficar acima.

### Neo4j e grafos de propriedades

"Neo4j uses a property graph database model." O modelo consiste em: nós que descrevem entidades, com zero ou mais rótulos que os classificam; relações que descrevem conexão entre nó de origem e nó de destino, sempre com uma direção e exatamente um tipo; e propriedades, pares chave-valor, em nós e relações [F: neo4j2026graphconcepts].

A linguagem é Cypher, cuja especificação aberta openCypher "evolves towards ISO/IEC 39075 GQL", e cujo propósito hoje é "to pave the road to GQL for openCypher implementers" [F: opencypher2026]. O padrão ISO/IEC 39075:2024 foi anunciado como publicado em 17/04/2024 [F: gqlstandards2024].

### Camada de consulta padronizada

SPARQL 1.1 não é só linguagem: o conjunto de onze Recommendations inclui o Protocol, o Graph Store HTTP Protocol, Service Description, Federated Query e formatos de resultado em JSON, CSV, TSV e XML [F: w3c2013sparql11overview, status e §1].

[I] Isso tem consequência prática de arquitetura: a camada de acesso de uma aplicação conversa com um endpoint HTTP padronizado, e trocar de triplestore não exige reescrevê-la. Nenhum equivalente padronizado foi verificado do lado dos grafos de propriedades.

## Requisitos e pressupostos

- Escolha prévia do modelo de grafo (kg.found.rdf-vs-property-graphs).
- Dimensionamento por camada: as três camadas de kg.mod.layer-separation têm perfis de volume e escrita muito diferentes e não precisam compartilhar tecnologia.
- Clareza sobre onde a inferência acontece: no banco, em tempo de consulta ou materializada em lote (kg.found.reasoning). RDF4J declara inferência entre suas funções [F: rdf4j2026about]; o suporte exato por perfil não foi verificado.

## Alternativas e comparações

| Critério | Jena TDB2 | RDF4J | Neo4j |
|---|---|---|---|
| Modelo | RDF [F: jena2026tdb2] | RDF [F: rdf4j2026about] | grafo de propriedades [F: neo4j2026graphconcepts] |
| Consulta | SPARQL | SPARQL 1.1 completo, consulta e atualização [F: rdf4j2026about] | Cypher, convergindo para GQL [F: opencypher2026] |
| Transações | "transactional only", sem autocommit [F: jena2026tdb2] | Memory e Native são transacionais [F: rdf4j2026about] | não verificado |
| Escala declarada | "100's of millions of triples" em carga em massa [F: jena2026tdb2] | Native Store: "in the order of 100 million triples" [F: rdf4j2026about] | não verificado |
| Acesso remoto | via Fuseki [F: jena2026tdb2] | "transparent access to remote RDF repositories using the exact same API" [F: rdf4j2026about] | protocolo próprio |
| Inferência | ver Jena Inference API, não consultada | declarada no núcleo [F: rdf4j2026about] | por consulta de caminho |
| Formatos | não verificado | RDF/XML, Turtle, N-Triples, N-Quads, JSON-LD, TriG, TriX [F: rdf4j2026about] | não aplicável |

**Nenhuma comparação de desempenho é feita aqui**: nenhum benchmark independente foi consultado, e as afirmações de escala são de fornecedor.

### Sugestão por camada

[I] Recomendação deste documento, derivada dos perfis descritos e não de medição:

| Camada | Perfil | Tecnologia indicada |
|---|---|---|
| Grafo conceitual | pequeno, lido muito, escrito em lote | triplestore RDF; cabe em memória |
| Modelo do aluno | alunos × conceitos, escrita contínua | chave-valor ou grafo, conforme o volume |
| Dados observados | muito grande, append-only, analítico | armazenamento colunar ou de eventos, fora do grafo |

## Exemplo técnico independente de domínio

```
# arquitetura por camada, com a ligação por IRI de conceito

  [triplestore RDF]          [armazenamento de estado]     [armazenamento de eventos]
   grafo conceitual     <--ref--  modelo do aluno    <--derivado--  observações
   SPARQL endpoint                  IRI de conceito              IRI de item/conceito
         ▲                                 ▲                            ▲
         └────────── aplicação: junta as três pelo identificador ───────┘
```

[I] A consequência de kg.mod.layer-separation para infraestrutura é esta: três armazenamentos, uma chave. A chave é o IRI do conceito, e por isso sua estabilidade é requisito de arquitetura, não de estilo.

## Relações com outros conceitos

Implementa kg.std.sparql. Depende de kg.found.rdf-vs-property-graphs (a escolha anterior). Complementa kg.mod.layer-separation (o dimensionamento por camada). Relaciona-se com kg.found.reasoning (onde a inferência roda) e kg.eng.quality.

## Lacunas e questões abertas

- **Nenhum benchmark foi consultado.** Todas as afirmações de escala e desempenho são de fornecedor e não foram verificadas de forma independente.
- Triplestores relevantes não foram examinados: GraphDB, Virtuoso, Oxigraph, Amazon Neptune, Stardog, Blazegraph.
- A documentação do Neo4j foi consultada apenas na página de conceitos de grafo [F: neo4j2026graphconcepts]; transações, escala e operação não foram verificadas.
- O suporte a regimes de entailment de SPARQL por implementação não foi levantado.
- Versões dos produtos não foram registradas: as páginas consultadas não trazem número de versão visível, o que torna estas afirmações datáveis apenas pela data de consulta.
- Suporte a RDF 1.2 (triple terms) por nenhuma das implementações foi verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| jena2026tdb2 | fornecedor | 2026-10-29 |
| rdf4j2026about | fornecedor | 2026-10-29 |
| neo4j2026graphconcepts | fornecedor | 2026-10-29 |
| gqlstandards2024 | tecnico | 2026-10-29 |
| opencypher2026 | fornecedor | 2026-10-29 |
| w3c2013sparql11overview | normativo | 2026-10-29 |
| w3c2013sparql11query | normativo | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
