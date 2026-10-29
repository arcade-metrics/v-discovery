---
id: kg.found.rdf-vs-property-graphs
titulo: RDF e grafos de propriedades, comparação
tipo: comparacao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, w3c2014rdf11concepts, neo4j2026graphconcepts, opencypher2026, gqlstandards2024, w3c2013sparql11query, w3c2013sparql11overview, w3c2017shacl]
relacoes:
  - { tipo: parte-de, alvo: kg.found.knowledge-graphs }
  - { tipo: relacionado-a, alvo: kg.found.context-and-reification }
  - { tipo: relacionado-a, alvo: kg.eng.storage-and-query }
  - { tipo: relacionado-a, alvo: kg.std.comparison }
termos: [property graph, directed edge-labelled graph, RDF, Cypher, openCypher, GQL, SPARQL, label, nó, relação, propriedade]
---

# RDF e grafos de propriedades, comparação

## Definição e terminologia

**Grafo dirigido com arestas rotuladas** (*directed edge-labelled graph*, ou *multi-relational graph*): nós ligados por arestas rotuladas. O modelo padronizado correspondente é RDF [F: hogan2021knowledgegraphs, §2.1.1], em que uma tripla tem sujeito, predicado e objeto [F: w3c2014rdf11concepts, §3.1].

**Grafo de propriedades**: permite associar um conjunto de pares propriedade-valor e um rótulo tanto a nós quanto a arestas [F: hogan2021knowledgegraphs, §2.1.3]. O modelo do Neo4j consiste em nós que descrevem entidades, com zero ou mais rótulos que os classificam; relações que ligam um nó de origem a um de destino, sempre com uma direção e exatamente um tipo; e propriedades, pares chave-valor, em nós e relações [F: neo4j2026graphconcepts].

Esta não é uma escolha entre "semântico" e "não semântico": é uma escolha entre um modelo minimal com padronização ampla e um modelo mais flexível com ferramental de banco de dados. [I]

## Problema que resolve

A pergunta aparece no primeiro dia de projeto e costuma ser decidida por hábito de equipe. [I] A comparação abaixo existe para que seja decidida pelo que o grafo precisa fazer.

## Fundamentos e funcionamento

### A diferença central: anotar a aresta

Hogan et al. constroem a comparação exatamente sobre esse ponto. Em grafos dirigidos com arestas rotuladas "we cannot directly annotate an edge" com informação adicional; é preciso criar um nó para a relação, ou usar grafos nomeados, o que "could become cumbersome" se grafos nomeados já servem a outro propósito, como rastrear a origem dos dados [F: hogan2021knowledgegraphs, §2.1.3]. O modelo de grafo de propriedades "was thus proposed to offer additional flexibility when modelling data as a graph" [F: hogan2021knowledgegraphs, §2.1.3].

### Intertradutibilidade

"Property graphs can be translated to/from directed edge-labelled graphs without loss of information"; em resumo, "directed-edge labelled graphs offer a more minimal model, while property graphs offer a more flexible one" e, com frequência, "the choice of model will be secondary to other practical factors, such as the implementations available for different models" [F: hogan2021knowledgegraphs, §2.1.3].

[I] Isso retira o drama da decisão: ela é reversível com custo de engenharia, não de modelagem conceitual. O que não é reversível de graça é o esquema de identificadores (ver kg.found.identifiers-and-triples).

### Linguagens de consulta e padronização

- RDF: SPARQL 1.1, conjunto de onze W3C Recommendations de 21/03/2013, incluindo linguagem de consulta, atualização, protocolo, federação, regimes de entailment e formatos de resultado [F: w3c2013sparql11overview].
- Grafo de propriedades: Cypher, desenvolvido pelo Neo4j, tem especificação aberta no openCypher, que hoje "evolves towards ISO/IEC 39075 GQL — the property graph query language standard developed by ISO/IEC JTC1 SC32 WG3", e cujo propósito passou a ser "to pave the road to GQL for openCypher implementers" [F: opencypher2026]. A publicação de ISO/IEC 39075:2024 foi anunciada em 17/04/2024 [F: gqlstandards2024].

[I] Até 2024, a assimetria de padronização era um argumento forte a favor de RDF. Com GQL publicado, o argumento perde força — mas RDF mantém algo que GQL não tem: uma pilha de padrões para *esquema* (RDFS, OWL, SKOS) e *validação* (SHACL), não só para consulta.

## Alternativas e comparações

| Critério | RDF (grafo dirigido rotulado) | Grafo de propriedades |
|---|---|---|
| Unidade mínima | tripla sujeito-predicado-objeto [F: w3c2014rdf11concepts, §3.1] | nó ou relação com rótulo e propriedades [F: neo4j2026graphconcepts] |
| Anotar uma aresta | só por reificação, nó n-ário, grafo nomeado ou triple term [F: hogan2021knowledgegraphs, §3.3] | nativo, como propriedade da relação [F: neo4j2026graphconcepts] |
| Identidade global | IRI, nativo [F: w3c2014rdf11concepts, §3.1] | por convenção de propriedade |
| Esquema formal | RDFS, OWL, SKOS | sem padrão equivalente |
| Validação | SHACL [F: w3c2017shacl] | por aplicação |
| Consulta padronizada | SPARQL 1.1, W3C Recommendation 2013 [F: w3c2013sparql11overview] | GQL, ISO/IEC 39075:2024 [F: gqlstandards2024]; openCypher converge para ele [F: opencypher2026] |
| Federação entre fontes | SPARQL 1.1 Federated Query [F: w3c2013sparql11overview, §1] | não padronizada |
| Múltiplos grafos | RDF dataset com grafos nomeados [F: w3c2014rdf11concepts, §4] | por convenção |
| Inferência | OWL, RDFS, regimes de entailment [F: w3c2013sparql11overview, §1] | por consulta de caminho |
| Conversão | sem perda de informação em ambas as direções [F: hogan2021knowledgegraphs, §2.1.3] | idem |

### Critério de escolha

[I] Recomendação deste documento, não afirmação das fontes:

- Escolha RDF quando o grafo precisa **publicar** (identidade global, reuso de vocabulário de terceiros, federação), quando o **esquema é um produto** (ontologia versionada, validável) ou quando há exigência de interoperabilidade com padrões educacionais que já são RDF ou mapeáveis (ver kg.voc.comparison).
- Escolha grafo de propriedades quando o grafo é **interno**, quando quase toda aresta carrega atributos (peso, confiança, data) e quando o perfil de uso é travessia com filtros, não inferência.
- Combinações existem na prática e não são contraditórias, dada a intertradutibilidade [F: hogan2021knowledgegraphs, §2.1.3].

## Métricas e métodos de avaliação

[I] Critérios mensuráveis para decidir em um caso concreto: proporção de arestas que precisam de atributo; número de vocabulários externos a reusar; necessidade de consulta federada; profundidade típica de travessia; existência de requisito de publicação aberta (ver kg.eng.quality e os princípios FAIR).

## Exemplo técnico independente de domínio

```cypher
// grafo de propriedades: atributo na aresta, nativo
MATCH (a:Conceito)-[r:PRE_REQUISITO_DE]->(b:Conceito)
WHERE r.confianca >= 0.7
RETURN a.id, b.id, r.confianca
```

```sparql
# RDF: a mesma consulta exige que o contexto já tenha sido modelado (aqui, nó de relação)
SELECT ?a ?b ?c WHERE {
  ?rel a :RelacaoPreRequisito ; :origem ?a ; :destino ?b ; :confianca ?c .
  FILTER (?c >= 0.7)
}
```

[I] A diferença de verbosidade é real, mas é consequência da decisão de modelagem de contexto (kg.found.context-and-reification), não uma limitação intrínseca de expressividade.

## Relações com outros conceitos

Parte de kg.found.knowledge-graphs. Relaciona-se com kg.found.context-and-reification (a diferença central entre os modelos), kg.eng.storage-and-query (as implementações de cada lado) e kg.std.comparison (quando usar cada padrão da pilha RDF).

## Lacunas e questões abertas

- O texto de ISO/IEC 39075:2024 não foi consultado: a página da ISO retornou HTTP 403 nesta sessão. O que se afirma sobre GQL vem do anúncio do comitê [F: gqlstandards2024] e do openCypher [F: opencypher2026].
- Não foram levantados benchmarks comparativos de desempenho entre triplestores e bancos de grafo de propriedades em cargas educacionais.
- [H] Em grafos curriculares, a fração de arestas que precisa de anotação parece alta (alinhamentos, pré-requisitos inferidos, evidências), o que favoreceria grafo de propriedades; mas a necessidade de reusar vocabulários como CASE e ESCO puxa para RDF. Nenhuma das duas pressões foi quantificada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| neo4j2026graphconcepts | fornecedor | 2026-10-29 |
| opencypher2026 | fornecedor | 2026-10-29 |
| gqlstandards2024 | tecnico | 2026-10-29 |
| w3c2013sparql11query | normativo | 2026-10-29 |
| w3c2013sparql11overview | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
