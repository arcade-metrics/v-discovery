---
id: kg.std.sparql
titulo: SPARQL 1.1
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2013sparql11query, w3c2013sparql11overview, w3c2014rdf11concepts, jena2026tdb2, rdf4j2026about, w3c2017shacl]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: complementa, alvo: kg.found.reasoning }
  - { tipo: implementado-por, alvo: kg.eng.storage-and-query }
  - { tipo: relacionado-a, alvo: kg.ret.text-to-query }
termos: [SPARQL, SELECT, CONSTRUCT, ASK, DESCRIBE, property path, basic graph pattern, OPTIONAL, FILTER, NOT EXISTS, MINUS, GROUP BY, HAVING, BIND, VALUES, federated query, entailment regime, SPARQL Update, Graph Store HTTP Protocol, Service Description]
---

# SPARQL 1.1

## Definição e terminologia

"RDF is a directed, labeled graph data format for representing information in the Web. This specification defines the syntax and semantics of the SPARQL query language for RDF. SPARQL can be used to express queries across diverse data sources, whether the data is stored natively as RDF or viewed as RDF via middleware" [F: w3c2013sparql11query, resumo].

A linguagem cobre padrões de grafo obrigatórios e opcionais com conjunção e disjunção, e também "aggregation, subqueries, negation, creating values by expressions, extensible value testing, and constraining queries by source RDF graph". Os resultados podem ser conjuntos de solução ou grafos RDF [F: w3c2013sparql11query, resumo].

## Status normativo

SPARQL 1.1 é um conjunto de **onze** W3C Recommendations de 21/03/2013, produzidas pelo SPARQL Working Group [F: w3c2013sparql11overview, status]:

| Documento | Papel |
|---|---|
| SPARQL 1.1 Overview | visão geral |
| SPARQL 1.1 Query Language | linguagem de consulta |
| SPARQL 1.1 Update | linguagem de atualização de grafos RDF |
| SPARQL 1.1 Service Description | descoberta e vocabulário para descrever serviços SPARQL |
| SPARQL 1.1 Federated Query | consultas distribuídas por múltiplos endpoints |
| SPARQL 1.1 Query Results JSON Format | formato de resultado |
| SPARQL 1.1 Query Results CSV and TSV Formats | formatos de resultado |
| SPARQL Query Results XML Format (Second Edition) | formato de resultado |
| SPARQL 1.1 Entailment Regimes | semântica sob regimes como RDF Schema, OWL ou RIF |
| SPARQL 1.1 Protocol | transporte de consultas e atualizações a um serviço |
| SPARQL 1.1 Graph Store HTTP Protocol | gestão de grafos por operações HTTP comuns |

[F: w3c2013sparql11overview, §1]

[I] Vale notar o que isso significa para um projeto: SPARQL não é só uma linguagem, é também um protocolo HTTP e um formato de resposta padronizados. Trocar de triplestore não exige reescrever a camada de acesso.

## Fundamentos e funcionamento

### Formas de consulta

[I] Quatro formas, com usos distintos em um grafo educacional:

| Forma | Retorna | Uso típico |
|---|---|---|
| `SELECT` | tabela de soluções | relatórios, listas, alimentação de UI |
| `CONSTRUCT` | grafo RDF | projeção de um subgrafo; materialização de inferências em grafo nomeado |
| `ASK` | booleano | verificação de condição |
| `DESCRIBE` | grafo RDF | obter a descrição de um recurso sem conhecer seu esquema |

### Recursos que importam aqui

A especificação cobre negação, com teste de ausência e de presença de padrão [F: w3c2013sparql11query, §8]; **property paths**, com sintaxe própria e casamento de caminho de comprimento arbitrário [F: w3c2013sparql11query, §9, §9.4]; atribuição com `BIND` [F: w3c2013sparql11query, §10.1]; e agregação com `GROUP BY` e `HAVING` [F: w3c2013sparql11query, §11].

[I] Property paths são o recurso decisivo neste domínio: permitem percorrer pré-requisitos transitivamente sem raciocinador e sem materialização. Ver kg.found.reasoning.

### Federação e regimes de entailment

SPARQL 1.1 Federated Query define extensão da linguagem para executar consultas distribuídas por diferentes endpoints [F: w3c2013sparql11overview, §1]. [I] É o caminho natural para consultar um vocabulário de terceiro (ESCO, por exemplo) sem copiá-lo, ao custo de depender da disponibilidade do serviço externo.

SPARQL 1.1 Entailment Regimes define a semântica de consultas sob regimes como RDF Schema, OWL ou RIF [F: w3c2013sparql11overview, §1]. O suporte efetivo varia por implementação e não foi levantado aqui.

### Implementações

Eclipse RDF4J "fully supports the SPARQL 1.1 query and update language for expressive querying" e oferece acesso transparente a repositórios RDF remotos com a mesma API do acesso local [F: rdf4j2026about]. Apache Jena TDB2 "is a component of Apache Jena for RDF storage and query", suporta toda a gama de APIs do Jena e pode ser usado com o Apache Jena Fuseki [F: jena2026tdb2]. Ver kg.eng.storage-and-query.

## Requisitos e pressupostos

- Dados em RDF, nativamente ou por middleware [F: w3c2013sparql11query, resumo].
- Conhecimento do esquema para escrever `SELECT`; `DESCRIBE` existe exatamente para o caso contrário.
- Atenção a consultas com property path não limitado em grafos grandes. [I] Um `?x :preRequisitoDe+ ?y` sem âncora percorre o fecho inteiro.

## Vantagens e limitações

Vantagens: padronizado desde 2013, com protocolo e formatos de resposta; travessia de caminho declarativa; federação; `CONSTRUCT` permite transformar grafo em grafo, útil para materializar derivações em um grafo nomeado separado.

Limitações: sem suporte nativo a funções analíticas de grafo (centralidade, detecção de comunidade); desempenho de property paths varia muito por implementação; regimes de entailment raramente implementados por completo; curva de aprendizado para quem vem de SQL. [I]

## Alternativas e comparações

| Precisa de | Opção |
|---|---|
| Consulta sobre RDF, padronizada | SPARQL 1.1 [F: w3c2013sparql11overview] |
| Consulta sobre grafo de propriedades | GQL / openCypher; ver kg.found.rdf-vs-property-graphs |
| Validação de forma | SHACL, que define restrições baseadas em SPARQL além do núcleo [F: w3c2017shacl] |
| Análise de grafo (comunidades, centralidade) | biblioteca fora do padrão; ver kg.ret.graph-rag |

## Exemplo técnico independente de domínio

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX ex:   <https://example.org/voc/>

# 1. todos os conceitos que precedem um alvo, transitivamente
SELECT DISTINCT ?anterior ?rotulo WHERE {
  ?anterior ex:preRequisitoDe+ <https://example.org/id/c/1b2c> ;
            skos:prefLabel     ?rotulo .
  FILTER (lang(?rotulo) = "pt")
}

# 2. conceitos sem nenhum recurso que os ensine (lacuna de cobertura)
SELECT ?c WHERE {
  ?c a skos:Concept .
  FILTER NOT EXISTS { ?r ex:ensina ?c }
}

# 3. materializar o fecho em um grafo nomeado separado
CONSTRUCT { ?a ex:preRequisitoDeTransitivo ?b }
WHERE     { ?a ex:preRequisitoDe+ ?b }

# 4. contagem de habilidades por componente curricular
SELECT ?componente (COUNT(?h) AS ?n) WHERE {
  ?h a ex:Habilidade ; ex:componente ?componente .
} GROUP BY ?componente HAVING (COUNT(?h) > 10)
```

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.std.rdf. Complementa kg.found.reasoning (property path cobre o fecho sem raciocinador). Implementado por kg.eng.storage-and-query. Relaciona-se com kg.ret.text-to-query (geração de SPARQL por modelo de linguagem).

## Lacunas e questões abertas

- O suporte real a regimes de entailment e a desempenho de property paths por implementação não foi levantado.
- A errata de SPARQL 1.1 Query "may include some normative corrections" [F: w3c2013sparql11query] e não foi consultada.
- Não há, entre as fontes consultadas, um conjunto de consultas de referência para grafos educacionais que sirva de banco de testes.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2013sparql11query | normativo | 2026-10-29 |
| w3c2013sparql11overview | normativo | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| jena2026tdb2 | fornecedor | 2026-10-29 |
| rdf4j2026about | fornecedor | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
