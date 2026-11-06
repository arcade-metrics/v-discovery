---
id: iop.md.lrmi-schema-org
titulo: LRMI e schema.org LearningResource
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [dcmi2026lrmi, schemaorg2026learningresource, schemaorg2026alignmentobject, schemaorg2026releases, dcmi2020terms, w3c2020jsonld11]
relacoes:
  - { tipo: complementa, alvo: iop.md.dublin-core }
  - { tipo: alternativa-a, alvo: iop.md.ieee-lom }
  - { tipo: complementa, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: iop.md.comparison }
  - { tipo: complementa, alvo: kg.std.json-ld }
  - { tipo: relacionado-a, alvo: kg.mod.conceptual-model }
  - { tipo: relacionado-a, alvo: kg.found.context-and-reification }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [LRMI, LRMI Terms, LRMI 1.1, LearningResource, AlignmentObject, teaches, assesses, competencyRequired, educationalAlignment, educationalLevel, educationalUse, learningResourceType, alignmentType, educationalFramework, targetDescription, DefinedTerm, EducationEvent]
---

# LRMI e schema.org LearningResource

## Definição e terminologia

**LRMI** (Learning Resource Metadata Initiative) é "a collection of classes, properties and concept schemes for markup and description of educational resources", mantida sob a DCMI e construída sobre o vocabulário extenso de schema.org e outros padrões [F: dcmi2026lrmi]. O LRMI distingue [F: dcmi2026lrmi]:

- **LRMI Terms**: a especificação corrente dos termos LRMI em RDF.
- **Concept Schemes**: pequenos conjuntos de conceitos para uso como valores com as propriedades LRMI, declarados em RDF usando SKOS. Como as propriedades para as quais esses conceitos se destinam também existem como propriedades de schema.org, "the concepts in these concept schemes can be used with a level of certainty in Web markup".
- **LRMI 1.1**: a versão criada pelo projeto LRMI entre 2011 e 2014 e transferida à DCMI em 2014, retida como estava; "newer terms are to be found in the current specification of LRMI Terms in RDF".

**schema.org LearningResource**: "The LearningResource type can be used to indicate CreativeWorks (whether physical or digital) that have a particular and explicit orientation towards learning, education, skill acquisition, and other educational purposes." A especificação acrescenta que "LearningResource is expected to be used as an addition to a primary type such as Book, VideoObject, Product etc." e que `EducationEvent` serve a propósito semelhante para coisas do tipo evento [F: schemaorg2026learningresource]. A hierarquia é `Thing > CreativeWork > LearningResource` [F: schemaorg2026learningresource].

O tipo está marcado como "in the 'new' area — implementation feedback and adoption from applications and websites can help improve our definitions" [F: schemaorg2026learningresource]. [I] Isso é um aviso de estabilidade: as definições podem mudar.

## Status normativo

schema.org não é norma de organismo de padronização; é um vocabulário mantido colaborativamente. A release corrente registrada na lista de releases é a **30.1, de 2026-09-16** [F: schemaorg2026releases]. A página consultada é a versão de desenvolvimento do site [F: schemaorg2026learningresource].

A página reporta uso de "10K - 100K Domains" para `LearningResource` e "1K - 10K Domains" para `AlignmentObject`, com base em agregações mensais do índice web do Google, referentes a agosto de 2026 [F: schemaorg2026learningresource; schemaorg2026alignmentobject].

A página de LRMI consultada não traz número de versão nem data da especificação corrente [F: dcmi2026lrmi].

## Problema que resolve

Descrever recursos educacionais com vocabulário que os mecanismos de busca e a web de dados já entendem, sem exigir um repositório institucional nem um esquema XML próprio [I].

## Fundamentos e funcionamento

### Propriedades de LearningResource

[F: schemaorg2026learningresource]:

| Propriedade | Tipo esperado | Definição |
|---|---|---|
| `teaches` | `DefinedTerm` ou `Text` | "The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term." |
| `assesses` | `DefinedTerm` ou `Text` | "The item being described is intended to assess the competency or learning outcome defined by the referenced term." |
| `competencyRequired` | `DefinedTerm`, `Text` ou `URL` | "Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource." |
| `educationalAlignment` | `AlignmentObject` | "An alignment to an established educational framework." Não deve ser usada quando a natureza do alinhamento pode ser descrita por propriedade simples, por exemplo para expressar que um recurso ensina ou avalia uma competência. |
| `educationalLevel` | `DefinedTerm`, `Text` ou `URL` | "The level in terms of progression through an educational or training context." Exemplos: 'beginner', 'intermediate', 'advanced', e conjuntos formais de indicadores de nível. |
| `educationalUse` | `DefinedTerm` ou `Text` | "The purpose of a work in the context of education; for example, 'assignment', 'group work'." |
| `learningResourceType` | `DefinedTerm` ou `Text` | "The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'." |

Mais as propriedades herdadas de `CreativeWork`, entre elas `about` ("The subject matter of an object", com propriedade inversa `subjectOf`) [F: schemaorg2026learningresource].

### AlignmentObject

"An intangible item that describes an alignment between a learning resource and a node in an educational framework." Hierarquia: `Thing > Intangible > AlignmentObject`. A mesma ressalva aparece: não usar onde a natureza do alinhamento pode ser descrita por propriedade simples [F: schemaorg2026alignmentobject].

Propriedades [F: schemaorg2026alignmentobject]:

| Propriedade | Tipo | Definição |
|---|---|---|
| `alignmentType` | `Text` | "A category of alignment between the learning resource and the framework node. Recommended values include: 'requires', 'textComplexity', 'readingLevel', and 'educationalSubject'." |
| `educationalFramework` | `Text` | "The framework to which the resource being described is aligned." |
| `targetDescription` | `Text` | "The description of a node in an established educational framework." |

### A distinção que importa

[I] `teaches`, `assesses` e `competencyRequired` são relações **diretas** do recurso para a competência. `educationalAlignment` é uma relação **reificada** (um `AlignmentObject` intermediário) para quando o tipo de alinhamento precisa ser qualificado. Ambas as páginas dizem explicitamente para preferir a forma simples quando ela serve [F: schemaorg2026learningresource; schemaorg2026alignmentobject]. É o mesmo trade-off tratado em `kg.found.context-and-reification`, resolvido aqui pelo vocabulário: forma simples por padrão, nó intermediário quando há contexto a registrar.

### Valores controlados

Várias propriedades aceitam `DefinedTerm`. Os concept schemes do LRMI fornecem conjuntos de conceitos SKOS para uso como valores com as propriedades LRMI, e como essas propriedades também existem como propriedades de schema.org, os conceitos podem ser usados "with a level of certainty in Web markup" [F: dcmi2026lrmi]. [I] O LRMI resolve, assim, o problema de *valores controlados* para as propriedades educacionais de schema.org.

### Combinação típica

[I] Dublin Core (ou as propriedades equivalentes de schema.org) para a descrição genérica (ver `iop.md.dublin-core`), LearningResource para a camada educacional, e um identificador de competência externo (CASE, CTDL-ASN, ESCO) como valor de `teaches`/`assesses` ou alvo de `educationalAlignment`. É isso que liga metadados de recurso a currículos e competências (ver `iop.comp.case`).

## Requisitos e pressupostos

- Serialização: JSON-LD é a forma usual de aplicar schema.org em páginas [F: w3c2020jsonld11]. Ver `kg.std.json-ld`.
- Uso como tipo adicional, não como tipo primário [F: schemaorg2026learningresource].
- Os valores de `teaches`, `assesses` e `educationalLevel` só são interoperáveis se vierem de vocabulário controlado com identificadores; texto livre produz descrição legível e não comparável [I].
- Aceitar que o vocabulário muda entre releases e que `LearningResource` está na área "new" [F: schemaorg2026learningresource].

## Vantagens e limitações

Vantagens [I]: o único vocabulário educacional consultado que oferece `teaches`, `assesses` e `competencyRequired` como propriedades diretas e nomeadas; custo de adoção baixo (JSON-LD embutido na página do recurso) e alcance imediato em busca; adoção mensurável na Web; gratuito e aberto; apoiado em RDF e SKOS, o que facilita a conversão para grafo; combina com Dublin Core e LRMI sem conflito.

Limitações [I]:
- Não é norma de organismo de padronização; evolui pelo processo do schema.org, e o tipo está na área "new", o que recomenda cautela quanto à estabilidade de detalhes.
- Tipos esperados frouxos (`Text` onde deveria haver referência); `educationalLevel` como texto livre mistura níveis informais e formais.
- Vocabulário menos detalhado que o IEEE LOM na dimensão pedagógica.
- Nenhuma validação embutida; isso é SHACL (ver `kg.std.shacl`).
- A página de LRMI não traz versão nem data, o que dificulta citar versão.

## Alternativas e comparações

Ver `iop.md.comparison` e `kg.voc.comparison`. A diferença central: LOM descreve o recurso de forma exaustiva em esquema XML; schema.org descreve a *relação pedagógica* do recurso com competências, em RDF, de forma enxuta.

## Exemplo técnico independente de domínio

Com alinhamento reificado e valores por identificador:

```json
{
  "@context": "https://schema.org",
  "@type": ["VideoObject", "LearningResource"],
  "@id": "https://example.org/id/r/4412",
  "name": "Introdução a frações equivalentes",
  "learningResourceType": "presentation",
  "educationalUse": "assignment",
  "teaches":  { "@type": "DefinedTerm", "@id": "https://example.org/id/c/8f3a" },
  "assesses": { "@type": "DefinedTerm", "@id": "https://example.org/id/c/8f3a" },
  "competencyRequired": { "@type": "DefinedTerm", "@id": "https://example.org/id/c/numeros-racionais" },
  "educationalAlignment": {
    "@type": "AlignmentObject",
    "alignmentType": "educationalSubject",
    "educationalFramework": "Base Nacional Comum Curricular",
    "targetDescription": "Resolver e elaborar problemas com frações equivalentes"
  }
}
```

[I] `teaches` e `assesses` apontando para o mesmo conceito é intencional no exemplo: o recurso ensina e avalia a mesma coisa. Em um grafo que separa recurso de instrumento (ver `kg.mod.conceptual-model`), essa coincidência deixa de ser comum.

Forma mínima, com código de habilidade curricular como `termCode`:

```json
{
  "@context": "https://schema.org",
  "@type": ["VideoObject", "LearningResource"],
  "name": "Introdução a frações equivalentes",
  "inLanguage": "pt-BR",
  "learningResourceType": "video",
  "educationalLevel": "ensino fundamental, anos iniciais",
  "teaches": { "@type": "DefinedTerm",
               "termCode": "EF05MA03",
               "inDefinedTermSet": "https://exemplo/curriculo" }
}
```

## Relações com outros conceitos

Complementa `iop.md.dublin-core` (descrição básica) e `iop.comp.case` (identificadores de competência). Alternativa a `iop.md.ieee-lom` para descrição de recursos na web. No domínio do grafo: complementa `kg.std.json-ld` (serialização); relaciona-se com `kg.mod.conceptual-model` e `kg.found.context-and-reification`.

## Lacunas e questões abertas

- Versão, data e URI de namespace da especificação LRMI corrente não constam da página consultada; verificar na página de LRMI Terms.
- Não foi levantada a lista completa dos concept schemes do LRMI que servem de valores.
- Relação formal (mapeamento declarado) entre LRMI/schema.org e IEEE LOM: não verificada.
- Uso de `educationalAlignment`/`AlignmentObject` com identificadores CASE: não verificado em fonte primária.
- Os números de adoção são do índice do Google, reportados pela própria schema.org [F: schemaorg2026learningresource]; não foram verificados de forma independente, e "10K-100K domains" é faixa larga.
- `alignmentType` recomenda valores ('requires', 'textComplexity', 'readingLevel', 'educationalSubject') mas é `Text` livre [F: schemaorg2026alignmentobject]; a prática real de uso desses valores não foi levantada.
- A estabilidade das definições na área "new" é risco declarado e não quantificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| dcmi2026lrmi | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| schemaorg2026alignmentobject | fornecedor | 2026-10-29 |
| schemaorg2026releases | fornecedor | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
| w3c2020jsonld11 | normativo | 2026-10-29 |
