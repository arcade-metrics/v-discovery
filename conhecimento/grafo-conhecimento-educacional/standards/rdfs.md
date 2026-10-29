---
id: kg.std.rdfs
titulo: RDF Schema 1.1
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2014rdfschema, w3c2014rdf11concepts, w3c2012owl2overview, w3c2009skos, w3c2017shacl]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: alternativa-a, alvo: kg.std.owl2 }
  - { tipo: complementa, alvo: kg.found.ontologies }
  - { tipo: relacionado-a, alvo: kg.found.reasoning }
termos: [RDFS, rdfs:Class, rdfs:subClassOf, rdfs:subPropertyOf, rdfs:domain, rdfs:range, rdfs:label, rdfs:comment, rdfs:seeAlso, rdfs:isDefinedBy, vocabulário]
---

# RDF Schema 1.1

## Definição e terminologia

RDF Schema é o vocabulário de descrição de vocabulários sobre RDF: define classes, hierarquia de classes, propriedades, hierarquia de propriedades, domínio e contradomínio, e termos de documentação.

## Status normativo

W3C Recommendation de 25/02/2014, editada por Dan Brickley e R. V. Guha (Google), com Brian McBride como editor anterior [F: w3c2014rdfschema]. A página traz uma atualização de status de 01/12/2023 registrando a correção do link "Latest published version", que passou a apontar para `http://www.w3.org/TR/rdf11-schema/`, a versão correspondente a RDF 1.1 [F: w3c2014rdfschema].

## Fundamentos e funcionamento

### Os termos centrais

| Termo | Papel |
|---|---|
| `rdfs:Class` | classe de classes |
| `rdfs:subClassOf` | subsunção entre classes |
| `rdf:Property`, `rdfs:subPropertyOf` | propriedades e hierarquia entre elas |
| `rdfs:domain` | classe dos sujeitos de uma propriedade |
| `rdfs:range` | classe ou datatype dos objetos |
| `rdfs:label`, `rdfs:comment` | documentação legível por humano |
| `rdfs:seeAlso`, `rdfs:isDefinedBy` | ligação a recursos relacionados e ao definidor |

[F: w3c2014rdfschema]

### O que RDFS infere

[I] A inferência de RDFS é pequena e barata, e é exatamente isso que a torna útil como piso: declarar `rdfs:domain` faz com que todo sujeito daquela propriedade seja tipado pela classe do domínio; declarar `rdfs:subClassOf` propaga o tipo para cima na hierarquia; `rdfs:subPropertyOf` propaga as afirmações da subpropriedade para a superpropriedade. Ver kg.found.reasoning para a comparação de níveis.

Atenção a um efeito contraintuitivo: `rdfs:domain` e `rdfs:range` **não são restrições de validação** — são afirmações de inferência. [I] Declarar `rdfs:range :Conceito` em `:preRequisitoDe` não impede que um recurso apareça como objeto; faz com que o raciocinador conclua que aquele recurso é um `:Conceito`. Para restringir de fato, usa-se SHACL (kg.std.shacl).

### Relação com OWL

Ontologias OWL 2 podem ser usadas junto com informação escrita em RDF e são trocadas primariamente como documentos RDF [F: w3c2012owl2overview, resumo]. [I] Na prática, RDFS e OWL coexistem no mesmo grafo; RDFS cobre o esqueleto (classes, propriedades, rótulos) e OWL acrescenta o que exige compromisso lógico (disjunção, cardinalidade, características de propriedade).

## Requisitos e pressupostos

- RDF como modelo subjacente [F: w3c2014rdf11concepts].
- Entendimento de que RDFS descreve, não valida.
- Rótulos multilíngues quando o grafo for usado em mais de um idioma; `rdfs:label` aceita language tags, herdadas de RDF [F: w3c2014rdf11concepts, §3.3].

## Vantagens e limitações

Vantagens: custo quase nulo; suportado por qualquer biblioteca RDF; inferência previsível; suficiente para a maior parte do que um grafo educacional precisa declarar sobre si mesmo.

Limitações: não exprime cardinalidade, disjunção, equivalência nem características de propriedade (transitividade, simetria); não valida; a inferência de domínio e contradomínio surpreende quem espera comportamento de esquema relacional. [I]

## Alternativas e comparações

| Precisa de | Camada |
|---|---|
| Classes, propriedades, rótulos, hierarquia | RDFS [F: w3c2014rdfschema] |
| Hierarquia de conceitos sem compromisso de classe | SKOS (kg.std.skos) [F: w3c2009skos] |
| Disjunção, cardinalidade, transitividade | OWL 2 (kg.std.owl2) [F: w3c2012owl2overview] |
| Garantir forma dos dados | SHACL (kg.std.shacl) [F: w3c2017shacl] |

## Exemplo técnico independente de domínio

```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex:   <https://example.org/voc/> .

ex:Conceito    a rdfs:Class ;
               rdfs:label   "Conceito"@pt , "Concept"@en ;
               rdfs:comment "Unidade de conhecimento referenciável por currículo e por recurso."@pt .

ex:Competencia a rdfs:Class ;
               rdfs:subClassOf ex:Conceito .

ex:preRequisitoDe a rdf:Property ;
               rdfs:domain ex:Conceito ;
               rdfs:range  ex:Conceito ;
               rdfs:label  "é pré-requisito de"@pt .

# efeito: dado ex:x ex:preRequisitoDe ex:y, infere-se que ex:x e ex:y são ex:Conceito.
# NÃO se infere erro caso ex:x seja declarado de outra classe; RDFS apenas acrescenta o tipo.
```

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.std.rdf. Alternativa a kg.std.owl2 quando basta esquema leve. Complementa kg.found.ontologies. Relaciona-se com kg.found.reasoning.

## Lacunas e questões abertas

- A errata de RDF Schema 1.1 não foi consultada; a especificação pede que seja verificada [F: w3c2014rdfschema].
- Não foi levantado o conjunto mínimo de termos RDFS que um grafo educacional deveria adotar como convenção interna. [H] `rdfs:label`, `rdfs:comment`, `rdfs:subClassOf` e `rdfs:isDefinedBy` parecem suficientes para o esqueleto, deixando o resto para SKOS e OWL — não verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2014rdfschema | normativo | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
