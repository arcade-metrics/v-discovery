---
id: iop.md.lrmi-schema-org
titulo: LRMI e schema.org/LearningResource
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [dcmi2026lrmi, schemaorg2026learningresource, dcmi2020terms]
relacoes:
  - { tipo: complementa, alvo: iop.md.dublin-core }
  - { tipo: alternativa-a, alvo: iop.md.ieee-lom }
  - { tipo: complementa, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: iop.md.comparison }
termos: [LearningResource, educationalAlignment, teaches, assesses, learningResourceType, AlignmentObject]
---

# LRMI e schema.org/LearningResource

## Definição e terminologia

**LRMI** (Learning Resource Metadata Initiative) é uma coleção de classes, propriedades e esquemas de conceitos para descrever recursos educacionais, mantida sob a DCMI. Foi criada pelo projeto LRMI entre 2011 e 2014 e transferida para a DCMI em 2014; a versão 1.1 foi preservada como estava em 2014. LRMI se apoia no vocabulário do schema.org: as propriedades para as quais seus esquemas de conceitos se destinam também existem como propriedades do schema.org, e os esquemas de conceitos são declarados em RDF com SKOS [F: dcmi2026lrmi].

**schema.org/LearningResource** é o tipo, na hierarquia `Thing > CreativeWork > LearningResource`, para obras com "uma orientação particular e explícita para a aprendizagem", físicas ou digitais; a documentação indica que deve ser somado a um tipo primário, como Book ou VideoObject [F: schemaorg2026learningresource].

**Propriedades específicas de LearningResource** [F: schemaorg2026learningresource]:

| Propriedade | Tipo | Significado |
|---|---|---|
| `teaches` | DefinedTerm, Text | a competência ou resultado de aprendizagem que o recurso ajuda a aprender |
| `assesses` | DefinedTerm, Text | a competência ou resultado que o recurso avalia |
| `competencyRequired` | DefinedTerm, Text, URL | conhecimento, habilidade ou atributo necessário |
| `educationalAlignment` | AlignmentObject | alinhamento a um framework educacional estabelecido |
| `educationalLevel` | DefinedTerm, Text, URL | nível de progressão |
| `educationalUse` | DefinedTerm, Text | finalidade educacional (tarefa, trabalho em grupo) |
| `learningResourceType` | DefinedTerm, Text | tipo predominante do recurso (apresentação, roteiro) |

A documentação recomenda não usar `educationalAlignment` quando uma propriedade mais simples, como `teaches` ou `assesses`, expressa a relação [F: schemaorg2026learningresource].

## Problema que resolve

Descrever recursos educacionais com vocabulário que os mecanismos de busca e a web de dados já entendem, sem exigir um repositório institucional nem um esquema XML próprio [I].

## Fundamentos e funcionamento

A combinação típica é: Dublin Core (ou as propriedades equivalentes de schema.org) para a descrição genérica, LearningResource para a camada educacional, e um identificador de competência externo (CASE, CTDL-ASN, ESCO) como valor de `teaches`/`assesses` ou alvo de `educationalAlignment` [I]. É isso que liga metadados de recurso a currículos e competências (ver `iop.comp.case`).

## Requisitos e pressupostos

- Os valores de `teaches`, `assesses` e `educationalLevel` só são interoperáveis se vierem de vocabulário controlado com identificadores; texto livre produz descrição legível e não comparável [I].

## Vantagens e limitações

Vantagens [I]: custo de adoção baixo (JSON-LD embutido na página do recurso); alcance imediato em busca; apoiado em RDF e SKOS, o que facilita a conversão para grafo.

Limitações [I]:
- Vocabulário menos detalhado que o IEEE LOM na dimensão pedagógica.
- Evolui pelo processo do schema.org: o tipo está marcado como "new" na versão de desenvolvimento consultada (V30.1, 2026-09-16), com pedido de feedback de implementação [F: schemaorg2026learningresource], o que recomenda cautela quanto à estabilidade de detalhes [I].
- A página de LRMI consultada não traz número de versão nem data da especificação corrente [F: dcmi2026lrmi], o que dificulta citar versão.

## Alternativas e comparações

Ver `iop.md.comparison`.

## Exemplo técnico independente de domínio

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

Complementa `iop.md.dublin-core` e `iop.comp.case`. Alternativa a `iop.md.ieee-lom` para descrição de recursos na web.

## Lacunas e questões abertas

- Versão, data e URI de namespace da especificação LRMI corrente não constam da página consultada; verificar na página de LRMI Terms.
- Relação formal (mapeamento declarado) entre LRMI/schema.org e IEEE LOM: não verificada.
- Uso de `educationalAlignment`/`AlignmentObject` com identificadores CASE: não verificado em fonte primária.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| dcmi2026lrmi | normativo | 2026-10-29 |
| schemaorg2026learningresource | normativo | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
