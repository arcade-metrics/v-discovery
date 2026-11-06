# Ficha: JSON Schema 2020-12

> Validação e evolução compatível de esquemas de evento já analisadas em `conhecimento/dados-pesquisa-e-eventos/quality/schema-validation-and-evolution.md` (`dat.qual.schema-validation-and-evolution`). Não repetir.

```yaml
id: int.json-schema
name: JSON Schema (Core e Validation), draft 2020-12
acronym: JSON Schema 2020-12
jurisdiction: internacional
issuing_organization: JSON Schema Organization (publicado como Internet-Draft no IETF, não RFC)
reference_type: especificação aberta (não é padrão formal de organismo de normalização) [I]
domain: [D8]
official_url: https://json-schema.org/specification
repository_url: https://github.com/json-schema-org/json-schema-spec
version: 2020-12 — "The current version is 2020-12! The previous version was 2019-09." [N25]
publication_date: unknown (página não traz data)
last_updated: nenhuma versão posterior publicada até 2026-11-05 [N25]
legal_status: voluntário
mandatory_scope: nenhum
education_levels: não se aplica
geographic_scope: global
language: en
license: unknown (não verificada)
technical_formats: JSON
api_available: não se aplica
data_model_available: sim (meta-esquema)
ontology_available: não
schemas_available: meta-esquema https://json-schema.org/draft/2020-12/schema [I: URI inferida do link da página]
implementation_examples: OpenAPI 3.1+ usa dialeto baseado em 2020-12 [N26]; Open Badges 3.0 e CLR 2.0 publicam JSON Schema [ver iop.cred.*]
related_standards: [int.openapi, kg.std.shacl (validação de grafo)]
entities: [schema, vocabulário, dialeto]
relationships: $ref, $defs, $dynamicRef
vocabularies: core, applicator, validation, unevaluated, format-annotation, content, meta-data
core_relevance: alta — contrato de payload de todas as entidades
regional_adapter_relevance: alta — adaptador declara extensões por esquema
limitations: valida estrutura de documento, não grafo; `format` é anotação por padrão (não validação) [I: conferir]
open_questions: [QI-15]
sources: [N25]
access_date: 2026-11-05
research_status: status verificado
```

## O que o Core adota (proposta)

JSON Schema 2020-12 como linguagem única de contrato de payload; `$id` com URI persistente e versão no caminho; extensões de adaptador por `allOf`/`$ref` sob namespace do adaptador, com `unevaluatedProperties: false` no núcleo [I]. SHACL fica para validação de grafo publicado (não de API).
