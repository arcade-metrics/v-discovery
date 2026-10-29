---
id: kg.std.rdf
titulo: RDF 1.1 e RDF 1.2
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2014rdf11concepts, w3c2026rdf12concepts, w3c2020jsonld11]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.found.identifiers-and-triples }
  - { tipo: complementa, alvo: kg.std.rdfs }
  - { tipo: complementa, alvo: kg.std.json-ld }
  - { tipo: relacionado-a, alvo: kg.found.context-and-reification }
termos: [RDF, abstract syntax, RDF graph, RDF dataset, named graph, default graph, IRI, blank node, literal, triple term, reifying triple, directional language-tagged string, RDF version announcement]
---

# RDF 1.1 e RDF 1.2

## Definição e terminologia

RDF é "a framework for representing information in the Web". A especificação de conceitos define uma sintaxe abstrata (um modelo de dados) que serve para ligar todas as linguagens e especificações baseadas em RDF, com duas estruturas de dados centrais: grafos RDF, conjuntos de triplas sujeito-predicado-objeto cujos elementos podem ser IRIs, blank nodes ou literais tipados; e RDF datasets, usados para organizar coleções de grafos RDF, compreendendo um grafo padrão e zero ou mais grafos nomeados [F: w3c2014rdf11concepts, resumo].

## Status normativo

| Documento | Status | Data | Versão |
|---|---|---|---|
| RDF 1.1 Concepts and Abstract Syntax | W3C Recommendation | 25/02/2014 | REC-rdf11-concepts-20140225 [F: w3c2014rdf11concepts] |
| RDF 1.2 Concepts and Abstract Data Model | W3C Candidate Recommendation Snapshot | 07/04/2026 | CR-rdf12-concepts-20260407 [F: w3c2026rdf12concepts] |
| JSON-LD 1.1 | W3C Recommendation | 16/07/2020 | REC-json-ld11-20200716 [F: w3c2020jsonld11] |

RDF 1.1 declara que "a new concept in RDF 1.1 is the notion of an RDF dataset to represent multiple graphs" [F: w3c2014rdf11concepts, status]. A página de RDF 1.2 aponta RDF 1.1 Concepts como "Latest Recommendation" [F: w3c2026rdf12concepts].

## Fundamentos e funcionamento

### Estruturas de RDF 1.1

- **Tripla**: sujeito (IRI ou blank node), predicado (IRI), objeto (IRI, literal ou blank node) [F: w3c2014rdf11concepts, §3.1].
- **Grafo**: conjunto de triplas [F: w3c2014rdf11concepts, §3].
- **Dataset**: exatamente um grafo padrão, sem nome, que pode estar vazio; zero ou mais grafos nomeados, cada um um par (IRI ou blank node, grafo RDF) [F: w3c2014rdf11concepts, §4].
- **Datatypes**: a especificação discute tipagem de dados e o tratamento de identificadores de fragmento em IRIs dentro de grafos RDF [F: w3c2014rdf11concepts, resumo], usando os tipos built-in do XML Schema [F: w3c2014rdf11concepts, §5].

### O que RDF 1.2 acrescenta

Três mudanças declaradas no resumo [F: w3c2026rdf12concepts, resumo]:

1. **Triple terms**: a possibilidade de usar uma tripla RDF como termo na posição de objeto de outra tripla. Com isso, passam a existir quatro tipos de nó no grafo: IRIs, literais, blank nodes e triple terms [F: w3c2026rdf12concepts, §3].
2. **Directional language-tagged strings**: literais com um componente de direção de base, que permite especificar a direção inicial do texto para apresentação por um agente de usuário.
3. **RDF version announcement**: um mecanismo para transmitir explicitamente qual versão de RDF um dado conjunto de dados usa, para facilitar a transição de 1.1 para 1.2.

A seção de reificação de RDF 1.2 define `rdf:reifies`, reifiers e triple annotations; ver kg.found.context-and-reification, que trata do assunto em detalhe.

## Requisitos e pressupostos

- Mundo aberto. Ver kg.found.reasoning.
- IRIs sob controle de quem publica. Ver kg.found.identifiers-and-triples.
- Escolha de serialização. RDF 1.1 define a sintaxe abstrata; as serializações concretas (Turtle, N-Triples, N-Quads, TriG, RDF/XML, JSON-LD) são documentos separados. JSON-LD 1.1 é uma serialização JSON para linked data [F: w3c2020jsonld11].

## Vantagens e limitações

Vantagens: modelo mínimo e estável desde 2014; identidade global nativa; datasets com grafos nomeados como mecanismo padrão para separar origens; base para toda a pilha (RDFS, OWL, SKOS, SHACL, SPARQL, PROV-O).

Limitações: não há anotação nativa de aresta em RDF 1.1 (resolvido parcialmente por RDF 1.2, ainda em Candidate Recommendation); verbosidade; o modelo não diz nada sobre validação — isso é SHACL (ver kg.std.shacl).

## Alternativas e comparações

Ver kg.found.rdf-vs-property-graphs para a comparação com grafos de propriedades, e kg.std.comparison para quando usar cada padrão da pilha RDF.

## Exemplo técnico independente de domínio

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/id/> .

ex:c/8f3a  a                skos:Concept ;
           skos:prefLabel   "Frações equivalentes"@pt ;
           ex:nivelEstimado "3"^^xsd:integer .
```

```trig
# dataset: grafo padrão mais um grafo nomeado
{ ex:c/8f3a a skos:Concept . }

GRAPH ex:g/curadoria-2026-10 {
  ex:c/8f3a ex:preRequisitoDe ex:c/1b2c .
}
```

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.found.identifiers-and-triples. Complementa kg.std.rdfs (o esquema mínimo sobre RDF) e kg.std.json-ld (uma serialização). Relaciona-se com kg.found.context-and-reification.

## Lacunas e questões abertas

- RDF 1.2 está em Candidate Recommendation Snapshot; a data de Recommendation não é conhecida. O relatório de implementação está referenciado na especificação [F: w3c2026rdf12concepts], mas não foi consultado.
- Não foi levantado o suporte a triple terms em triplestores e bibliotecas.
- A errata de RDF 1.1 não foi consultada; a especificação pede que seja verificada [F: w3c2014rdf11concepts].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| w3c2026rdf12concepts | normativo | 2026-10-29 |
| w3c2020jsonld11 | normativo | 2026-10-29 |
