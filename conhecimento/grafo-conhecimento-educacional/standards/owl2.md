---
id: kg.std.owl2
titulo: OWL 2 e seus perfis
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2012owl2overview, w3c2012owl2profiles, w3c2012owl2primer, w3c2012owl2syntax, w3c2014rdfschema, noy2001ontology101]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: alternativa-a, alvo: kg.std.rdfs }
  - { tipo: alternativa-a, alvo: kg.std.skos }
  - { tipo: complementa, alvo: kg.found.ontologies }
  - { tipo: avaliado-por, alvo: kg.found.reasoning }
  - { tipo: relacionado-a, alvo: kg.eng.versioning-and-provenance }
termos: [OWL 2, OWL 2 EL, OWL 2 QL, OWL 2 RL, OWL 2 DL, Direct Semantics, RDF-Based Semantics, perfil, profile, data complexity, taxonomic complexity, combined complexity, owl:versionIRI, owl:sameAs, owl:disjointWith, TransitiveProperty]
---

# OWL 2 e seus perfis

## Definição e terminologia

"The OWL 2 Web Ontology Language, informally OWL 2, is an ontology language for the Semantic Web with formally defined meaning. OWL 2 ontologies provide classes, properties, individuals, and data values and are stored as Semantic Web documents. OWL 2 ontologies can be used along with information written in RDF, and OWL 2 ontologies themselves are primarily exchanged as RDF documents" [F: w3c2012owl2overview, resumo].

Um **perfil** OWL 2 (chamado *fragment* ou *sublanguage* em lógica computacional) é "a trimmed down version of OWL 2 that trades some expressive power for the efficiency of reasoning" [F: w3c2012owl2profiles, §1]. Cada perfil é definido como restrição sintática da especificação estrutural de OWL 2 e é mais restritivo que OWL DL [F: w3c2012owl2overview, §2.4].

OWL 2 tem duas semânticas: a **Direct Semantics** e a **RDF-Based Semantics** [F: w3c2012owl2overview, resumo]. A diferença tem consequência computacional drástica, registrada na tabela abaixo.

## Status normativo

Todos os documentos de OWL 2 consultados são W3C Recommendation de 11/12/2012, segunda edição [F: w3c2012owl2overview; w3c2012owl2profiles; w3c2012owl2primer; w3c2012owl2syntax]. O Document Overview registra que "there have been no substantive changes since the previous version" [F: w3c2012owl2overview, status] e que a compatibilidade com OWL 1 é, "to all intents and purposes, complete": toda ontologia OWL 1 permanece válida em OWL 2, com inferências idênticas em todos os casos práticos [F: w3c2012owl2overview, §3].

## Fundamentos e funcionamento

### Os três perfis

[F: w3c2012owl2overview, §2.4]:

- **OWL 2 EL** "enables polynomial time algorithms for all the standard reasoning tasks"; é adequado a aplicações com ontologias muito grandes, em que poder expressivo pode ser trocado por garantias de desempenho. Restringe os tipos de restrição de classe admitidos, mantendo quantificação existencial sobre expressão de classe ou intervalo de dados, quantificação existencial sobre indivíduo ou literal, e auto-restrição [F: w3c2012owl2profiles, §2.1].
- **OWL 2 QL** "enables conjunctive queries to be answered in LogSpace (more precisely, AC0) using standard relational database technology"; adequado a ontologias relativamente leves que organizam grande número de indivíduos, quando é útil ou necessário acessar os dados por consultas relacionais. É definido não só pelo conjunto de construtores admitidos, mas também pelos lugares em que podem ocorrer [F: w3c2012owl2profiles, §3.1].
- **OWL 2 RL** "enables the implementation of polynomial time reasoning algorithms using rule-extended database technologies operating directly on RDF triples"; adequado a ontologias leves sobre muitos indivíduos quando é útil operar diretamente sobre triplas RDF. As restrições foram desenhadas "so as to avoid the need to infer the existence of individuals not explicitly present in the knowledge base, and to avoid the need for nondeterministic reasoning" [F: w3c2012owl2profiles, §4.1].

Uma implementação baseada em regras de OWL 2 RL pode operar sobre um grafo RDF arbitrário; nesse caso o raciocínio é sempre *sound*, mas pode não ser *complete*. O teorema PR1 do documento de perfis estabelece que, em geral, quando a ontologia é consistente com a definição estrutural de OWL 2 RL, uma implementação baseada em regras que responda consultas atômicas fundamentadas é *sound* e *complete* [F: w3c2012owl2overview, §2.4].

### Complexidade

Medidas usadas: complexidade de dados (tamanho das asserções), taxonômica (tamanho dos axiomas sem asserções), de consulta e combinada [F: w3c2012owl2profiles, §5]. Resultados, para consistência de ontologia, satisfatibilidade e subsunção de expressão de classe e verificação de instância [F: w3c2012owl2profiles, tabela 10]:

| Linguagem | Taxonômica | Dados | Combinada |
|---|---|---|---|
| OWL 2, RDF-Based Semantics | indecidível | indecidível | indecidível |
| OWL 2, Direct Semantics | N2EXPTIME-complete | decidível, complexidade em aberto (NP-hard) | N2EXPTIME-complete |
| OWL 2 EL | PTIME-complete | PTIME-complete | PTIME-complete |
| OWL 2 QL | NLogSpace-complete | em AC0 | NLogSpace-complete |
| OWL 2 RL | PTIME-complete | PTIME-complete | PTIME-complete (co-NP-complete para satisfatibilidade/subsunção/instância em expressões não atômicas) |
| OWL 1 DL | NEXPTIME-complete | decidível, complexidade em aberto (NP-hard) | NEXPTIME-complete |

Para OWL 2 Direct Semantics e OWL 2 EL, os limites caem para NEXPTIME-complete e PTIME-complete respectivamente "if the property hierarchy can be translated into a polynomially-sized nondeterministic finite automaton" [F: w3c2012owl2profiles, tabela 10].

A própria especificação alerta: esses resultados "refer to the worst-case complexity of these reasoning problems and, as such, do not say that implemented algorithms necessarily run in this class on all input problems" [F: w3c2012owl2profiles, §5].

### Construtores relevantes a um grafo educacional

[I] Os que importam na prática deste domínio:

| Construtor | Uso típico aqui |
|---|---|
| `owl:TransitiveProperty` | fecho de pré-requisito e de parte-de |
| `owl:disjointWith` | separar Competência de Recurso, Evidência de Objetivo |
| `owl:inverseOf` | `preRequisitoDe` / `temPreRequisito` |
| `owl:sameAs` | igualdade de indivíduos entre fontes — com cuidado, por ser compromisso lógico forte |
| `owl:equivalentClass` | alinhar a ontologia própria a um vocabulário externo |
| cardinalidade qualificada | "toda Competência tem ao menos um Objetivo" |
| `owl:versionIRI` | versionamento de ontologia [F: w3c2012owl2syntax] |

Sobre `owl:sameAs`: [I] igualar dois indivíduos propaga todas as afirmações de um para o outro. Ao integrar currículos, é quase sempre errado — o que se quer é mapeamento, não identidade. Ver `skos:exactMatch` em kg.std.skos e `exactMatchOf` do CASE em iop.comp.case.

## Requisitos e pressupostos

- Um raciocinador que suporte o perfil escolhido, ou a aceitação de inferência parcial.
- Decisão explícita entre Direct Semantics e RDF-Based Semantics; a segunda é indecidível em todas as medidas [F: w3c2012owl2profiles, tabela 10].
- Conformidade estrutural com o perfil, se as garantias de complexidade importam: os perfis são restrições sintáticas, e sair delas invalida as garantias [F: w3c2012owl2profiles, §1].

## Vantagens e limitações

Vantagens: semântica formal; detecção de inconsistência; alinhamento declarado com vocabulários externos; perfis com garantias de complexidade conhecidas.

Limitações: custo computacional e de modelagem; curva de aprendizado alta; mundo aberto confunde quem espera validação (ver kg.std.shacl); e a expressividade convida a modelar mais do que é necessário. [I] Noy e McGuinness lembram que não há uma forma correta de modelar e que a melhor solução depende da aplicação pretendida [F: noy2001ontology101, §3].

## Alternativas e comparações

Ver kg.std.comparison. Em resumo: SKOS para hierarquias sem compromisso lógico, RDFS para esquema leve, OWL para onde a consistência formal vale o custo, SHACL para validar.

## Exemplo técnico independente de domínio

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex:  <https://example.org/voc/> .

<https://example.org/voc/> a owl:Ontology ;
    owl:versionIRI <https://example.org/voc/3.1.0> .

ex:Competencia owl:disjointWith ex:Recurso .

ex:preRequisitoDe a owl:ObjectProperty , owl:TransitiveProperty ;
    owl:inverseOf ex:temPreRequisito .

# cardinalidade qualificada: toda Competência tem ao menos um Objetivo associado
ex:Competencia rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty ex:temObjetivo ;
    owl:minQualifiedCardinality "1"^^xsd:nonNegativeInteger ;
    owl:onClass ex:ObjetivoDeAprendizagem
] .
```

[I] Esse recorte cabe em OWL 2 RL? `owl:TransitiveProperty` e `owl:disjointWith` sim; cardinalidade qualificada mínima em superclasse, não — RL restringe o uso de construtores por posição sintática [F: w3c2012owl2profiles, §4.1]. A verificação exata de conformidade exige a gramática do apêndice 6 do documento de perfis, não feita aqui.

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.std.rdf. Alternativa a kg.std.rdfs e a kg.std.skos. Complementa kg.found.ontologies. Avaliado por kg.found.reasoning. Relaciona-se com kg.eng.versioning-and-provenance (`owl:versionIRI`).

## Lacunas e questões abertas

- A conformidade de um modelo educacional concreto a OWL 2 RL ou EL não foi verificada; exige aplicar as gramáticas dos apêndices do documento de perfis [F: w3c2012owl2profiles, §6].
- Não foi levantado desempenho real de raciocinadores sobre grafos curriculares; só limites de pior caso.
- A errata de OWL 2 "may include some normative corrections" [F: w3c2012owl2overview] e não foi consultada.
- Qual perfil adotar para um grafo que mistura ontologia pequena e muitos indivíduos (o caso de evidências de aprendizagem) fica em aberto. [H] QL ou RL parecem indicados pelo próprio texto do Overview, que os associa a "relatively lightweight ontologies used to organize large numbers of individuals" [F: w3c2012owl2overview, §2.4], mas a escolha entre os dois depende do perfil de consulta.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2012owl2overview | normativo | 2026-10-29 |
| w3c2012owl2profiles | normativo | 2026-10-29 |
| w3c2012owl2primer | normativo | 2026-10-29 |
| w3c2012owl2syntax | normativo | 2026-10-29 |
| w3c2014rdfschema | normativo | 2026-10-29 |
| noy2001ontology101 | academico | 2026-10-29 |
