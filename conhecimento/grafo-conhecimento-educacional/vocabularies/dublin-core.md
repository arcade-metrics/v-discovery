---
id: kg.voc.dublin-core
titulo: Dublin Core e DCMI Metadata Terms
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [dcmi2020terms, dcmi2026lrmi, w3c2009skos, schemaorg2026learningresource, ieee2020lom]
relacoes:
  - { tipo: parte-de, alvo: kg.voc.comparison }
  - { tipo: complementa, alvo: kg.voc.ieee-lom }
  - { tipo: complementa, alvo: kg.voc.schema-org-learning-resource }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: relacionado-a, alvo: kg.std.skos }
termos: [Dublin Core, DCMI Metadata Terms, namespace /terms/, namespace /elements/1.1/, vocabulary encoding scheme, syntax encoding scheme, LRMI, concept scheme]
---

# Dublin Core e DCMI Metadata Terms

## Definição e terminologia

DCMI Metadata Terms "is an up-to-date specification of all metadata terms maintained by the Dublin Core Metadata Initiative, including properties, vocabulary encoding schemes, syntax encoding schemes, and classes" [F: dcmi2020terms].

Dois espaços de nomes coexistem: o namespace `/terms/` e o namespace legado `/elements/1.1/`, ambos documentados na especificação, que também lista esquemas de codificação de vocabulário e de sintaxe, além de classes [F: dcmi2020terms, sumário].

[I] A distinção importa: `dcterms:creator` (namespace `/terms/`) tem contradomínio definido; `dc:creator` (namespace `/elements/1.1/`) é literal livre. Misturar os dois em um grafo gera inconsistência de tipo silenciosa.

## Status normativo

DCMI Recommendation, emitida em 2020-01-20, criada pelo DCMI Usage Board. O identificador da versão é `http://dublincore.org/specifications/dublin-core/dcmi-terms/2020-01-20/` [F: dcmi2020terms].

## Fundamentos e funcionamento

### Papel em um grafo educacional

[I] Dublin Core é o núcleo mínimo de descrição de qualquer recurso: título, criador, data, idioma, assunto, tipo, formato, direitos, relação. É o vocabulário que não precisa de justificativa — se um grafo tem recursos, usa Dublin Core para o básico e vocabulário especializado para o resto.

### LRMI

O LRMI é a especificação DCMI voltada a recursos educacionais: "a collection of classes, properties and concept schemes for markup and description of educational resources", construída sobre o vocabulário extenso de Schema.org e outros padrões [F: dcmi2026lrmi].

O LRMI distingue [F: dcmi2026lrmi]:

- **LRMI Terms**: a especificação corrente dos termos LRMI em RDF.
- **Concept Schemes**: pequenos conjuntos de conceitos para uso como valores com as propriedades LRMI. Como as propriedades para as quais esses conceitos se destinam também existem como propriedades de Schema.org, "the concepts in these concept schemes can be used with a level of certainty in Web markup". Os conceitos foram declarados em RDF usando SKOS [F: dcmi2026lrmi].
- **LRMI 1.1**: a versão criada pelo projeto LRMI entre 2011 e 2014 e transferida à DCMI em 2014, retida como estava; "newer terms are to be found in the current specification of LRMI Terms in RDF" [F: dcmi2026lrmi].

[I] A consequência prática é relevante: o LRMI resolve o problema de *valores controlados* para as propriedades educacionais de schema.org. Onde schema.org admite `Text` ou `DefinedTerm` (por exemplo em `learningResourceType` e `educationalUse` [F: schemaorg2026learningresource]), o LRMI oferece os conceitos SKOS a usar como `DefinedTerm`.

A DCMI descreve sua própria abordagem de metadados como visando "pragmatic interoperability among traditional and newer technologies on the basis of knowledge graph design principles" [F: dcmi2020terms, página da DCMI, seção Metadata Basics].

## Requisitos e pressupostos

- Escolha explícita entre os namespaces `/terms/` e `/elements/1.1/`, e disciplina em não misturá-los sem necessidade [I].
- Para usar os concept schemes do LRMI como valores, um entendimento de SKOS (ver kg.std.skos) [F: dcmi2026lrmi].

## Vantagens e limitações

Vantagens: adoção universal; termos estáveis desde os anos 1990; já em RDF; o LRMI acrescenta a camada educacional com valores controlados declarados em SKOS.

Limitações: Dublin Core puro é genérico demais para descrição pedagógica; `dcterms:subject` não distingue "ensina" de "trata de"; e a relação entre LRMI Terms, LRMI 1.1 e as propriedades correspondentes de schema.org exige atenção para não duplicar afirmações. [I]

## Alternativas e comparações

| Necessidade | Vocabulário |
|---|---|
| Núcleo de descrição de recurso | DCMI Metadata Terms [F: dcmi2020terms] |
| Propriedades pedagógicas na Web aberta | schema.org LearningResource [F: schemaorg2026learningresource] |
| Valores controlados para essas propriedades | LRMI concept schemes, em SKOS [F: dcmi2026lrmi] |
| Metadados de objeto de aprendizagem em repositório | IEEE LOM [F: ieee2020lom] |

Ver kg.voc.comparison.

## Exemplo técnico independente de domínio

```turtle
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema:  <https://schema.org/> .
@prefix ex:      <https://example.org/id/> .

ex:r/4412 a schema:LearningResource ;
    dcterms:title     "Introdução a frações equivalentes"@pt ;
    dcterms:creator   ex:agente/equipe-conteudo ;
    dcterms:created   "2026-03-14"^^xsd:date ;
    dcterms:language  "pt-BR" ;
    dcterms:license   <https://creativecommons.org/licenses/by/4.0/> ;
    schema:teaches    ex:c/8f3a .
```

[I] Dublin Core para o que é descrição de recurso; schema.org para o que é relação pedagógica. A divisão evita usar `dcterms:subject` para dizer "ensina", afirmação mais forte e mais útil.

## Relações com outros conceitos

Parte de kg.voc.comparison. Complementa kg.voc.ieee-lom e kg.voc.schema-org-learning-resource. Depende de kg.std.rdf. Relaciona-se com kg.std.skos (os concept schemes do LRMI).

## Lacunas e questões abertas

- A lista completa de termos DCMI não foi examinada elemento a elemento; só o cabeçalho de status, o sumário e exemplos.
- Os LRMI Terms em RDF e os concept schemes individuais não foram abertos; a descrição vem da página da especificação [F: dcmi2026lrmi].
- A relação exata entre cada termo LRMI e a propriedade schema.org correspondente não foi mapeada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| dcmi2020terms | normativo | 2026-10-29 |
| dcmi2026lrmi | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| ieee2020lom | normativo | 2026-10-29 |
