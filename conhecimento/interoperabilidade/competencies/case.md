---
id: iop.comp.case
titulo: CASE (Competencies and Academic Standards Exchange)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2017case, ims2017case10, onedtech2025case, credengine2026ctdl, w3c2009skos, krathwohl2002revision]
relacoes:
  - { tipo: complementa, alvo: iop.md.lrmi-schema-org }
  - { tipo: alternativa-a, alvo: iop.comp.ctdl }
  - { tipo: complementa, alvo: iop.asmt.qti }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: complementa, alvo: kg.curr.competency-frameworks }
  - { tipo: complementa, alvo: kg.curr.prerequisites }
  - { tipo: relacionado-a, alvo: kg.std.skos }
  - { tipo: relacionado-a, alvo: kg.curr.bncc }
  - { tipo: relacionado-a, alvo: kg.curr.cognitive-taxonomies }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [CASE, competência, padrão curricular, framework, alinhamento, identificador referenciável, CFDocument, CFItem, CFAssociation, CFAssociationTypeEnum, isChildOf, isPeerOf, isPartOf, exactMatchOf, precedes, isRelatedTo, replacedBy, exemplar, hasSkillLevel, GUID, frameworkType, extensions, targetType]
---

# CASE (Competencies and Academic Standards Exchange)

## Definição e terminologia

CASE é o serviço do 1EdTech (antigo IMS Global) para publicar e trocar competências e padrões curriculares em formato legível por máquina.

"The 1EdTech Competencies and Academic Standards Exchange (CASE) v1.1 standard facilitates the exchange of information about academic learning standards, competencies, and skills between different educational applications and tools, for the specific needs of K-12, Higher Education, and the Workforce. CASE can also transmit information about rubrics, performance task criteria, and associations across frameworks, so frameworks and items can be related and aligned" [F: onedtech2025case, resumo].

A motivação declarada: "The goal for CASE is to replace the current ways of documenting a learning standard and competency, typically a PDF or HTML document, by a method that is both human and machine-readable. These digital versions are called CASE Frameworks." Os dados têm identificadores globalmente únicos (GUIDs) que permitem etiquetar recursos de aprendizagem e associar padrões acadêmicos, competências e habilidades a outros frameworks CASE, a credenciais digitais e a órgãos normativos externos [F: onedtech2025case, §1].

As aplicações envolvidas na troca incluem tipicamente LMSs, repositórios de objetos de aprendizagem, SISs, ferramentas de avaliação, gestão curricular, credenciamento digital e plataformas de contratação [F: onedtech2025case, resumo].

## Status normativo

- **CASE v1.1**: Final Release, Document Version 1, emitida em 24/01/2025 [F: onedtech2025case]. "This document is released for public adoption and implementation of the CASE Service 1.1 specification" [F: onedtech2025case, §1.1].
- **CASE v1.0**: IMS Final Release, emitida em 7 de julho de 2017 [F: imsglobal2017case]; o Information Model é o documento que define as entidades e o vocabulário de associações [F: ims2017case10].
- O conjunto documental inclui um Information Model e um binding REST/JSON, publicados como documentos separados [F: imsglobal2017case].

## Problema que resolve

Padrões curriculares e competências são tipicamente publicados como PDF ou HTML, feitos para leitura humana. CASE substitui isso por definições legíveis por máquina "both syntactically and semantically", permitindo que sistemas troquem e administrem esses dados, apoiando alinhamentos comuns e fornecendo identificadores únicos referenciáveis para uso em certificados e históricos [F: imsglobal2017case].

Esse é o ponto de articulação de todo o domínio de interoperabilidade [I]: sem identificador estável de competência, o alinhamento de um recurso (`teaches`), de um item de avaliação e de um resultado de aluno não pode ser expresso de forma verificável, só como texto repetido em cada sistema.

## Fundamentos e funcionamento

### Padrão de uso

Derivado do problema declarado [I]: a autoridade curricular publica o framework uma vez, com identificadores; todos os demais sistemas referenciam esses identificadores em vez de copiar o texto do padrão. Mudanças no currículo passam a ser versionadas na origem.

### Entidades

[I] Três entidades sustentam o modelo:

- **CFDocument**: o framework (um currículo, um conjunto de padrões).
- **CFItem**: o item dentro do framework (uma competência, uma habilidade, um descritor).
- **CFAssociation**: a relação tipada entre itens, ou entre documentos.

### Vocabulário de associações

O `CFAssociationTypeEnum` é "the permitted set of values for the type of association between CFItems or between CFDocuments" [F: ims2017case10, §7.3.1]. O conjunto enumerado é `{ isChildOf | isPeerOf | isPartOf | exactMatchOf | precedes | isRelatedTo | replacedBy | exemplar | hasSkillLevel }` [F: ims2017case10, §5].

Definições normativas [F: ims2017case10, tabela 7.3.1]:

| Termo | Definição |
|---|---|
| `isChildOf` | "To represent the structural relationship in a taxonomy between parent and child. The source/origin is a child of the target/destination." |
| `isPartOf` | "The origin of the association is included either physically or logically in the item at the destination of the association. This classifies an item as being logically or semantically contained as a subset of the destination." |
| `isPeerOf` | "The source/origin is a peer of of the target/destination." |
| `precedes` | "The origin of the association comes before the destination of the association in time or order." |
| `isRelatedTo` | "The origin of the association is related to the destination in some way that is not better described by another association type." |
| `exactMatchOf` | "Equivalent to. Used to connect derived CFItem to CFItem in original source CFDocument." |
| `exemplar` | "The target/destination node is an example of best practice for the definition of the source/origin." |
| `replacedBy` | "The origin of the association has been supplanted by, displaced by, or superseded by the destination of the association." |
| `hasSkillLevel` | "The destination of this association is understood to define a given skill level i.e. Reading Lexile 100, Depth Knowledge 2, or Cognitive Level (Blooms Taxonomy) etc." |

[I] Dois pontos merecem destaque para quem está modelando um grafo educacional:

1. **`precedes` é o mais próximo de pré-requisito que o CASE oferece**, e sua definição é deliberadamente fraca: "comes before ... in time or order". Não afirma dependência cognitiva. Ver `kg.curr.prerequisites`.
2. **`hasSkillLevel` liga um item a um nível cognitivo**, com a taxonomia de Bloom citada como exemplo na própria definição [F: ims2017case10, tabela 7.3.1]. Ver `kg.curr.cognitive-taxonomies` e [F: krathwohl2002revision, metadados].

### Mudanças de 1.0 para 1.1

Entre as alterações registradas [F: onedtech2025case, §1.12 e seções de revisão]:

- `CFDocument.frameworkType`, campo opcional que permite ao criador indicar o tipo de framework, "for example course codes".
- `CFDocument.caseVersion`: "The CASE version for the CFDocument. Currently, the only expected value is 1.1 since this field does not exist for CASE 1.0."
- `CFItem.subject` e `CFItem.subjectURI`.
- `CFAssociation.notes`, `CFAssociation.originNodeURI.targetType` e `CFAssociation.destinationNodeURI.targetType`.
- **Associações para fora do CASE**: "CFAssociations now allow the originNodeURI and destinationNodeURI to point to non-CASE frameworks. This is a large change since it changes how CASE consumers process associations since it can no longer be assumed the target is a CASE object. To help guide implementors the field targetType was added to these association pointers."
- **Extensões**: CASE 1.0 proibia explicitamente "proprietary data elements"; em CASE 1.1, `CFItem`, `CFDocument`, `CFAssociation` e outras entidades podem incluir um campo `extensions` com subcampos fora da especificação. Um sistema consumidor "can simply ignore the entire extensions field". Aninhar dados próprios em `extensions` evita colisão de nomes com campos futuros; a boa prática recomendada é camelCase, por consistência com os campos oficiais [F: onedtech2025case].

[I] A mudança de associações para alvos não-CASE é a mais relevante para um grafo educacional: é o que permite que um framework CASE aponte para um conceito de um grafo próprio, ou para ESCO, sem exigir que tudo seja CASE.

## Requisitos e pressupostos

- Existe uma autoridade que publica o framework e mantém os identificadores estáveis ao longo das revisões curriculares [I].
- Os consumidores referenciam por identificador, e não por título ou código impresso [I].
- GUIDs por entidade [F: onedtech2025case, §1].
- Para uso em grafo RDF, um mapeamento de CASE para RDF. A especificação descreve entidades JSON e um serviço REST; nenhum contexto JSON-LD oficial foi verificado.
- Atenção ao processar associações em CASE 1.1: não se pode mais assumir que o alvo é objeto CASE; o campo `targetType` existe para isso [F: onedtech2025case].

## Vantagens e limitações

Vantagens: é o padrão específico para troca de frameworks de competência, com vocabulário de associação fechado e definido; resolve a camada semântica de currículo com um identificador referenciável, desenhado para ser citado por credenciais e históricos [F: imsglobal2017case]; permite associações entre frameworks (alinhamento); tem conformidade certificável, com seção dedicada na especificação [F: onedtech2025case, §1.3].

Limitações [I]:
- `precedes` não distingue ordem de apresentação de dependência cognitiva; `isChildOf` e `isPartOf` se sobrepõem na prática; o vocabulário fechado não cobre força ou confiança de uma associação (isso cai em `extensions`).
- CASE é um modelo de serviço REST com JSON, não um vocabulário RDF; a ponte para o grafo é trabalho a fazer.
- Exige um publicador institucional. Onde o currículo não é publicado em CASE, caso do Brasil, não verificado, a adoção significa publicar o currículo você mesmo, assumindo papel de autoridade que não se tem.
- Não resolve equivalência entre frameworks diferentes por si; para isso, é preciso declarar correspondências (`exactMatchOf` dentro do padrão, ou ver `iop.fund.mapeamento-e-proveniencia`).

## Alternativas e comparações

| Necessidade | CASE | CTDL-ASN | SKOS puro |
|---|---|---|---|
| Publicar framework curricular | sim | sim [F: credengine2026ctdl] | parcial |
| Serviço REST definido | sim | registro próprio | não |
| Foco | educação básica e currículo | credenciais e mercado de trabalho | genérico |
| Ecossistema | 1EdTech | Credential Engine | web semântica |

| Necessidade | Opção |
|---|---|
| Trocar frameworks de competência entre sistemas | CASE [F: onedtech2025case] |
| Representar a mesma hierarquia como grafo RDF | SKOS [F: w3c2009skos] |
| Classificação europeia de competências pronta | ESCO; ver `iop.comp.esco` |
| Credenciais e competências ligadas a trabalho | CTDL; ver `iop.comp.ctdl` |

Mapeamento aproximado CASE → SKOS, proposto por este documento [I]:

| CASE | SKOS |
|---|---|
| `CFDocument` | `skos:ConceptScheme` |
| `CFItem` | `skos:Concept` com `skos:inScheme` |
| `isChildOf` | `skos:broader` (direção invertida: o filho aponta para o pai em ambos) |
| `exactMatchOf` | `skos:exactMatch` |
| `isRelatedTo` | `skos:related` |
| `precedes` | sem equivalente; propriedade própria |
| `hasSkillLevel` | sem equivalente; propriedade própria |
| `isPartOf` | sem equivalente direto; `skos:broader` perde a distinção |

A comparação ampla entre vocabulários educacionais, por camada de cobertura, está em `kg.voc.comparison`.

## Exemplo técnico independente de domínio

```turtle
# framework CASE representado como esquema SKOS, com propriedades próprias
# para o que SKOS não cobre
ex:fw/curriculo-x  a skos:ConceptScheme ;
    skos:prefLabel "Framework X"@pt ;
    ex:caseFrameworkType "course codes" .

ex:item/9b21 a skos:Concept ;
    skos:inScheme  ex:fw/curriculo-x ;
    skos:notation  "X.5.07" ;
    skos:prefLabel "Resolver problemas com frações equivalentes"@pt ;
    skos:broader   ex:item/9b00 ;                      # era isChildOf
    ex:precede     ex:item/9b22 ;                      # era precedes
    ex:nivelCognitivo ex:bloom/aplicar ;               # era hasSkillLevel
    skos:exactMatch <https://outro.example/case/item/abc> .   # era exactMatchOf
```

[I] A tradução perde `isPartOf` e `exemplar`, que não têm equivalente SKOS. Se essas distinções importarem, precisam de propriedades próprias, e é por isso que o mapeamento acima é proposta deste documento, não equivalência afirmada pela especificação.

## Relações com outros conceitos

Complementa `iop.md.lrmi-schema-org` (fornece os identificadores que vão em `teaches`/`assesses`) e `iop.asmt.qti` (alinhamento de itens). Alternativa a `iop.comp.ctdl` conforme o domínio de uso. Depende de `iop.sem.vocabularios-e-skos`. No domínio do grafo: complementa `kg.curr.competency-frameworks` e `kg.curr.prerequisites`; relaciona-se com `kg.std.skos` (a tradução para grafo), `kg.curr.bncc` (um currículo candidato a ser publicado como framework CASE) e `kg.curr.cognitive-taxonomies` (`hasSkillLevel`).

## Lacunas e questões abertas

- O modelo de informação completo de CASE 1.1 (lista de campos por entidade) não foi acessado: a URL `/spec/case/v1p1/info/` retornou 404. As definições de associação citadas vêm do Information Model de CASE 1.0 [F: ims2017case10], que CASE 1.1 estende; a seção de mudanças não registra alteração no `CFAssociationTypeEnum`, mas isso não foi confirmado contra o modelo de 1.1. As classes `CFRubric` e `CFConcept`, citadas na literatura secundária, não foram verificadas.
- Nenhum contexto JSON-LD oficial para CASE foi localizado.
- Não foi verificado se existe versão posterior a 1.1.
- Não foi verificado se a BNCC ou currículos estaduais estão publicados como framework CASE por alguma iniciativa; é a questão central para uso no Brasil.
- A semântica de `precedes` é fraca demais para servir de pré-requisito pedagógico sem qualificação adicional; como qualificá-la dentro do padrão (via `extensions`?) fica em aberto.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2017case | normativo | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
| credengine2026ctdl | fornecedor | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| krathwohl2002revision | academico | 2026-10-29 |
