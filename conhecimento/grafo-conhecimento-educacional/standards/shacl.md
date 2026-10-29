---
id: kg.std.shacl
titulo: SHACL
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2017shacl, w3c2013sparql11query, w3c2014rdf11concepts, hogan2021knowledgegraphs, w3c2012owl2overview]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: depende-de, alvo: kg.std.sparql }
  - { tipo: alternativa-a, alvo: kg.found.reasoning }
  - { tipo: avaliado-por, alvo: kg.eng.quality }
  - { tipo: relacionado-a, alvo: kg.std.owl2 }
termos: [SHACL, shapes graph, data graph, sh:NodeShape, sh:PropertyShape, focus node, sh:conforms, validation report, sh:ValidationResult, sh:minCount, sh:maxCount, sh:class, sh:datatype, sh:nodeKind, sh:pattern, sh:closed, SHACL-SPARQL, SHACL list, SHACL subclass]
---

# SHACL

## Definição e terminologia

SHACL é "a language for validating RDF graphs against a set of conditions". As condições são fornecidas como *shapes* e outras construções expressas na forma de um grafo RDF. Os grafos usados dessa maneira são os **shapes graphs**; os grafos validados contra eles são os **data graphs**. Como shapes graphs são usados para validar que data graphs satisfazem um conjunto de condições, "they can also be viewed as a description of the data graphs that do satisfy these conditions", descrição útil "for a variety of purposes beside validation, including user interface building, code generation and data integration" [F: w3c2017shacl, resumo].

O que não é: SHACL não é inferência. OWL sob mundo aberto não acusa dado faltante; SHACL acusa. Os dois resolvem problemas diferentes e coexistem. [I]

## Status normativo

W3C Recommendation de 20/07/2017, editada por Holger Knublauch (TopQuadrant) e Dimitris Kontokostas (University of Leipzig), publicada pelo RDF Data Shapes Working Group [F: w3c2017shacl].

A especificação distingue a linguagem núcleo das seções 5 e 6, que tratam de SHACL-SPARQL: "the features that SHACL-SPARQL has in addition to the Core language. These advanced features are SPARQL-based constraints and constraint components" [F: w3c2017shacl, §1].

## Fundamentos e funcionamento

### Terminologia herdada

SHACL reusa a terminologia de RDF 1.1 Concepts (grafo RDF, tripla, IRI, literal, blank node, nó, termo RDF, sujeito, predicado, objeto, datatype) e de SPARQL 1.1 Query Language [F: w3c2017shacl, §1.1]. Caminhos de propriedade SPARQL são definidos como em SPARQL 1.1; um termo RDF `n` tem valor `v` para um caminho `p` em um grafo `G` se houver solução da consulta `SELECT ?s ?o WHERE { ?s p' ?o }` sobre `G` ligando `?s` a `n` e `?o` a `v` [F: w3c2017shacl, §1.1].

Dois termos próprios importam na modelagem educacional [F: w3c2017shacl, §1.1]:

- **SHACL subclass / superclass**: um nó `Sub` é SHACL subclasse de `Super` se houver uma sequência de triplas com predicado `rdfs:subClassOf` ligando um ao outro.
- **SHACL type**: os tipos SHACL de um termo são seus valores de `rdf:type` mais as SHACL superclasses desses valores.

### Componentes de restrição do núcleo

[F: w3c2017shacl, §4]:

| Família | Componentes |
|---|---|
| Tipo de valor | `sh:class`, `sh:datatype`, `sh:nodeKind` |
| Cardinalidade | `sh:minCount`, `sh:maxCount` |
| Faixa de valor | `sh:minExclusive`, `sh:minInclusive`, `sh:maxExclusive`, `sh:maxInclusive` |
| Cadeia de caracteres | `sh:minLength`, `sh:maxLength`, `sh:pattern`, `sh:languageIn`, `sh:uniqueLang` |
| Par de propriedades | `sh:equals`, `sh:disjoint`, `sh:lessThan`, `sh:lessThanOrEquals` |
| Lógicos | `sh:not`, `sh:and`, `sh:or`, `sh:xone` |
| Baseados em shape | `sh:node`, `sh:property`, `sh:qualifiedValueShape` com `sh:qualifiedMinCount`/`sh:qualifiedMaxCount` |
| Outros | `sh:closed` com `sh:ignoredProperties`, `sh:hasValue`, `sh:in` |

[I] Para um grafo educacional, `sh:uniqueLang` e `sh:languageIn` cobrem a exigência de rótulo único por idioma; `sh:qualifiedMinCount` cobre "toda habilidade deve ter ao menos um item que a avalie"; `sh:closed` impede que propriedades não previstas entrem sem revisão.

### Relatório de validação

A validação produz um `sh:ValidationReport` com `sh:conforms` (booleano), `sh:result` (os resultados individuais) e `sh:shapesGraphWellFormed`. Cada `sh:ValidationResult` traz, entre outros, o nó foco (`sh:focusNode`) e o caminho (`sh:resultPath`) [F: w3c2017shacl, §3.6].

[I] O relatório é ele próprio um grafo RDF. Isso permite guardar o histórico de validações no mesmo grafo em que os dados vivem e consultar a evolução da qualidade com SPARQL. Ver kg.eng.quality.

### SHACL-SPARQL

Para o que o núcleo não cobre — por exemplo, aciclicidade de pré-requisitos — existem restrições baseadas em SPARQL e componentes de restrição próprios [F: w3c2017shacl, §1, §5, §6].

## Requisitos e pressupostos

- Um data graph e um shapes graph; o vínculo entre eles pode ser declarado com `sh:shapesGraph` [F: w3c2017shacl, §3.3].
- Um motor SHACL. O núcleo é implementável sem SPARQL; SHACL-SPARQL exige um motor SPARQL.
- Clareza sobre o que é erro de dado e o que é lacuna aceitável. [I] Sob mundo aberto, dado faltante é a regra; SHACL serve para declarar onde isso deixa de ser aceitável.

## Vantagens e limitações

Vantagens: valida sem fechar o mundo do grafo inteiro; shapes são RDF, versionáveis como o resto; o relatório é consultável; a mesma shape serve para gerar interface e documentação, como a própria especificação aponta [F: w3c2017shacl, resumo].

Limitações: o núcleo não exprime restrições estruturais globais (aciclicidade, conectividade) sem SPARQL; a especificação trata explicitamente do manejo de shapes recursivas [F: w3c2017shacl, §3.4.3], sinal de que recursão é área delicada; e validar grafos grandes a cada escrita é caro.

## Alternativas e comparações

| Objetivo | Ferramenta | Razão |
|---|---|---|
| Garantir que os dados têm a forma esperada | SHACL | validação explícita sobre mundo aberto [F: w3c2017shacl] |
| Derivar fatos novos | OWL / RDFS | inferência, não validação [F: w3c2012owl2overview] |
| Detectar contradição lógica no modelo | raciocinador OWL | consistência formal [F: w3c2012owl2overview, §2.4] |
| Medir qualidade ao longo do tempo | relatórios SHACL acumulados + métricas | ver kg.eng.quality [F: hogan2021knowledgegraphs, §7] |

Hogan et al. observam que formas de inacurácia sintática "can typically be assessed using validation tools" [F: hogan2021knowledgegraphs, §7.1.1].

## Exemplo técnico independente de domínio

```turtle
@prefix sh:   <http://www.w3.org/ns/shacl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ex:   <https://example.org/voc/> .

ex:ConceitoShape a sh:NodeShape ;
    sh:targetClass skos:Concept ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) ;

    sh:property [
        sh:path       skos:prefLabel ;
        sh:minCount   1 ;
        sh:uniqueLang true ;
        sh:languageIn ( "pt" "en" ) ;
        sh:message    "Todo conceito precisa de exatamente um rótulo preferido por idioma."@pt
    ] ;
    sh:property [
        sh:path     skos:notation ;
        sh:maxCount 1 ;
        sh:pattern  "^C-[0-9A-F]{4}$"
    ] ;
    sh:property [
        sh:path     ex:preRequisitoDe ;
        sh:class    skos:Concept ;
        sh:nodeKind sh:IRI
    ] .

# aciclicidade: fora do núcleo, exige SHACL-SPARQL
ex:SemCicloShape a sh:NodeShape ;
    sh:targetClass skos:Concept ;
    sh:sparql [
        sh:message "Conceito não pode ser pré-requisito de si mesmo, direta ou indiretamente."@pt ;
        sh:select """
            SELECT $this WHERE { $this <https://example.org/voc/preRequisitoDe>+ $this }
        """
    ] .
```

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.std.rdf e de kg.std.sparql (para SHACL-SPARQL e para a semântica de caminhos de propriedade). Alternativa a kg.found.reasoning quando o objetivo é verificar e não derivar. Avaliado por kg.eng.quality. Relaciona-se com kg.std.owl2.

## Lacunas e questões abertas

- A errata do SHACL não foi consultada; a especificação pede que seja verificada [F: w3c2017shacl].
- Não foi levantado o custo de validar grafos educacionais grandes nem a prática de validação incremental.
- [H] Um conjunto mínimo de shapes para grafos curriculares (rótulo obrigatório, código único, aciclicidade de pré-requisito, cobertura de avaliação) parece ser o mesmo em qualquer currículo e poderia ser publicado como perfil reutilizável; nenhuma fonte consultada publica um assim.
- SHACL 1.2 está em desenvolvimento no W3C segundo o editor's draft referenciado pela especificação [F: w3c2017shacl]; o status atual não foi verificado nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2017shacl | normativo | 2026-10-29 |
| w3c2013sparql11query | normativo | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
