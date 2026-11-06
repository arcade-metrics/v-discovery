---
id: kg.std.skos
titulo: SKOS
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2009skos, w3c2009skosprimer, w3c2012owl2overview, esco2026what, dcmi2026lrmi, w3c2017shacl, mec2026bncc]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: alternativa-a, alvo: kg.std.owl2 }
  - { tipo: implementado-por, alvo: iop.comp.esco }
  - { tipo: complementa, alvo: kg.curr.competency-frameworks }
  - { tipo: relacionado-a, alvo: kg.found.reasoning }
termos: [SKOS, skos:Concept, skos:ConceptScheme, skos:prefLabel, skos:altLabel, skos:notation, skos:broader, skos:narrower, skos:related, skos:broaderTransitive, skos:semanticRelation, skos:exactMatch, skos:closeMatch, skos:inScheme, skos:topConceptOf, tesauro, taxonomia]
---

# SKOS

## Definição e terminologia

SKOS "defines a common data model for sharing and linking knowledge organization systems via the Web". A motivação declarada é que muitos sistemas de organização do conhecimento — tesauros, taxonomias, esquemas de classificação, listas de cabeçalhos de assunto — compartilham estrutura semelhante [F: w3c2009skos, resumo].

O Primer resume o escopo: SKOS "provides a model for expressing the basic structure and content of concept schemes such as thesauri, classification schemes, subject heading lists, taxonomies, folksonomies, and other similar types of controlled vocabulary" [F: w3c2009skosprimer, resumo].

O que não é: SKOS não é uma ontologia de domínio. Um `skos:Concept` é uma unidade de significado em um vocabulário, não uma classe cujos membros se instanciem. [I] Confundir os dois é o erro mais comum ao modelar currículo: "Frações equivalentes" é um conceito do vocabulário, não a classe das frações equivalentes.

## Status normativo

W3C Recommendation de 18/08/2009, editada por Alistair Miles (STFC Rutherford Appleton Laboratory / University of Oxford) e Sean Bechhofer (University of Manchester) [F: w3c2009skos]. O SKOS Primer é W3C Working Group Note da mesma data, editada por Antoine Isaac (Vrije Universiteit Amsterdam) e Ed Summers (Library of Congress), com atualização de status de 30/10/2023 que substituiu um link quebrado [F: w3c2009skosprimer].

## Fundamentos e funcionamento

### Relações semânticas

SKOS distingue duas categorias básicas de relação semântica: **hierárquica** e **associativa**. Um vínculo hierárquico indica que um conceito é de algum modo mais geral ("broader") que o outro ("narrower"); um vínculo associativo indica que os dois são inerentemente relacionados, mas nenhum é mais geral que o outro [F: w3c2009skos, §8.1].

Pontos normativos relevantes [F: w3c2009skos, §8.1, §8.3]:

- Por convenção, `skos:broader` e `skos:narrower` são usados "only to assert a direct (i.e., immediate) hierarchical link between two SKOS concepts". Para sustentar essa convenção, essas propriedades **não são declaradas transitivas**.
- `skos:broaderTransitive` e `skos:narrowerTransitive` representam vínculo direto ou indireto. Por convenção, **não são usadas para fazer asserções**: servem para inferir o fecho transitivo dos vínculos hierárquicos.
- `skos:related` afirma o vínculo associativo.
- `skos:semanticRelation`, `skos:broader`, `skos:narrower`, `skos:related`, `skos:broaderTransitive` e `skos:narrowerTransitive` são todas instâncias de `owl:ObjectProperty` (S18). O domínio e o contradomínio de `skos:semanticRelation` são `skos:Concept` (S19, S20). `skos:broaderTransitive`, `skos:narrowerTransitive` e `skos:related` são subpropriedades de `skos:semanticRelation` (S21).

### Duas decisões de projeto que importam

1. **Ciclos são consistentes.** Um ciclo na relação hierárquica "is consistent with the SKOS data model, i.e., there is no condition requiring that `skos:broaderTransitive` be irreflexive" [F: w3c2009skos, §8.6.8]. [I] Se o grafo educacional proíbe ciclo de pré-requisito, a proibição tem de vir de validação própria.
2. **Hierárquico e associativo são disjuntos.** A especificação "treats the hierarchical and associative relations as fundamentally distinct in nature. Therefore a clash between hierarchical and associative links is not consistent with the SKOS data model". A posição segue as definições usuais dos padrões de tesauro ISO 2788 e BS 8723-2 [F: w3c2009skos, §8.6.10].

### Rótulos

[I] SKOS separa rótulo preferido (`skos:prefLabel`), alternativo (`skos:altLabel`) e oculto (`skos:hiddenLabel`), além de `skos:notation` para códigos. Essa separação é o que permite que um currículo tenha código oficial, nome na norma, nome usado por professores e grafias com erro comum, tudo apontando para o mesmo conceito — sem duplicá-lo.

### Mapeamento entre esquemas

[I] SKOS oferece propriedades de mapeamento (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`) para ligar conceitos de esquemas diferentes sem igualá-los logicamente como faria `owl:sameAs` (ver kg.std.owl2). É o mecanismo adequado para alinhar BNCC a ESCO, ou um vocabulário interno a um framework CASE.

### Adoção em educação

- A ESCO, classificação multilíngue europeia de competências e ocupações, descreve 3.039 ocupações e 13.939 competências, traduzidas em 28 idiomas; a versão corrente é ESCO v1.2.1, release v6.0.0, com última atualização em 10/12/2025 [F: esco2026what]. Ver iop.comp.esco.
- Os *concept schemes* do LRMI são "pequenos conjuntos de conceitos para uso como valores com as propriedades LRMI", e "os conceitos nos vocabulários foram declarados em RDF usando o Simple Knowledge Organization System (SKOS) do W3C" [F: dcmi2026lrmi]. Ver iop.md.lrmi-schema-org.

## Requisitos e pressupostos

- Que o objeto modelado seja mesmo um vocabulário de conceitos e não uma ontologia de classes [I].
- Que a convenção de não asserir `skos:broaderTransitive` seja respeitada pelos produtores de dados [F: w3c2009skos, §8.1]; caso contrário o grafo mistura afirmado e derivado.
- Que a restrição de aciclicidade, se necessária, seja imposta externamente (ver kg.std.shacl).

## Vantagens e limitações

Vantagens: custo baixíssimo de adoção; cobre exatamente o formato de um currículo (hierarquia com códigos e rótulos); mapeamento entre esquemas sem compromisso lógico; amplamente adotado em vocabulários educacionais e de competências.

Limitações: não exprime restrição, cardinalidade nem disjunção; aceita ciclos; não distingue "parte de" de "mais específico que" — ambas viram `skos:broader` se não se acrescentar propriedade própria; e não dá suporte nativo a progressão temporal ou pré-requisito (que não é nem hierárquico nem meramente associativo). [I]

## Alternativas e comparações

| Precisa de | Camada |
|---|---|
| Hierarquia curricular com códigos e rótulos multilíngues | SKOS [F: w3c2009skos] |
| Distinguir pré-requisito de hierarquia | propriedade própria, subpropriedade de `skos:semanticRelation` ou independente [I] |
| Cardinalidade, disjunção, transitividade declarada | OWL 2 [F: w3c2012owl2overview] |
| Impedir ciclo | SHACL [F: w3c2017shacl] |

## Exemplo técnico independente de domínio

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ex:   <https://example.org/id/> .

ex:esquema/curriculo-v3 a skos:ConceptScheme ;
    skos:prefLabel "Currículo de referência, versão 3"@pt .

ex:c/8f3a a skos:Concept ;
    skos:inScheme   ex:esquema/curriculo-v3 ;
    skos:prefLabel  "Frações equivalentes"@pt ;
    skos:altLabel   "Equivalência de frações"@pt ;
    skos:notation   "C-8F3A" ;
    skos:broader    ex:c/numeros-racionais ;       # só o vínculo imediato
    skos:closeMatch <https://example.net/outro/esquema/frac-eq> .

# pré-requisito NÃO é broader nem related: propriedade própria, para não violar
# a disjunção entre hierárquico e associativo e para não poluir o fecho de broaderTransitive
ex:preRequisitoDe a owl:ObjectProperty .
ex:c/8f3a ex:preRequisitoDe ex:c/1b2c .
```

[I] Esse é o padrão que este domínio recomenda: SKOS para a espinha curricular, propriedade própria para pré-requisito. A razão é a disjunção normativa de §8.6.10: encaixar pré-requisito em `skos:related` pode gerar choque com o fecho hierárquico quando dois conceitos são ao mesmo tempo irmãos na hierarquia e ligados por pré-requisito [F: w3c2009skos, §8.6.10].

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.std.rdf. Alternativa a kg.std.owl2 quando basta hierarquia. Implementado por iop.comp.esco. Complementa kg.curr.competency-frameworks. Relaciona-se com kg.found.reasoning (fecho transitivo por convenção, não por inferência automática).

## Lacunas e questões abertas

- A errata do SKOS Reference "may include some normative corrections" [F: w3c2009skos] e não foi consultada.
- Não foi verificado se a BNCC tem publicação em SKOS; a consulta ao portal do MEC mostrou publicação em PDF e planilha [F: mec2026bncc]. Ver kg.curr.bncc.
- [H] Modelar pré-requisito como subpropriedade de `skos:semanticRelation` (e não como propriedade independente) daria domínio e contradomínio de graça, mas herdaria a semântica de relação semântica SKOS; o efeito sobre o fecho e sobre a disjunção §8.6.10 não foi verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2009skos | normativo | 2026-10-29 |
| w3c2009skosprimer | normativo | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
| dcmi2026lrmi | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
| mec2026bncc | normativo | 2026-10-29 |
