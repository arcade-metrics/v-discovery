# Ficha: OpenAPI Specification 3.1 / 3.2

```yaml
id: int.openapi
name: OpenAPI Specification
acronym: OAS
jurisdiction: internacional
issuing_organization: OpenAPI Initiative (Linux Foundation)
reference_type: especificação aberta
domain: [D8]
official_url: https://spec.openapis.org/oas/
repository_url: https://github.com/OAI/OpenAPI-Specification
version: publicadas v3.0.0–3.0.4, v3.1.0–3.1.2, v3.2.0 e v3.2.1 (mais recente) [N26]
publication_date: unknown (índice não traz datas de versão); iterações de esquema 3.2 datadas de 2025-09-17 a 2026-08-30 [N26]
last_updated: 2026-08-30 (esquema 3.2) [N26]
legal_status: voluntário
mandatory_scope: nenhum
education_levels: não se aplica
geographic_scope: global
language: en
license: Apache-2.0 [I: não verificado nesta sessão]
technical_formats: JSON, YAML
api_available: não se aplica (descreve APIs)
data_model_available: sim
ontology_available: não
schemas_available: sim — esquemas e dialetos publicados em spec.openapis.org [N26]
implementation_examples: OneRoster 1.2, Ed-Fi ODS/API, Edu-API publicam OpenAPI [ver estados-unidos/]
related_standards: [int.json-schema]
entities: [document, path, operation, component, security scheme]
relationships: —
vocabularies: —
core_relevance: alta — contrato das APIs do Core e dos adaptadores
regional_adapter_relevance: alta
limitations: 3.1 e 3.2 usam dialeto próprio sobre JSON Schema 2020-12 (dialetos 2024-11-10 e 2026-02-26) [N26]; ferramental para 3.2 pode estar atrás de 3.1 [I]
open_questions: [QI-15]
sources: [N26]
access_date: 2026-11-05
research_status: status verificado (sem datas de versão)
```

## O que o Core adota (proposta)

OpenAPI **3.1.x** como piso de contrato (compatível com JSON Schema 2020-12); avaliar 3.2 quando o ferramental de geração de código estiver estável (QI-15). Não usar 3.0 (dialeto de esquema divergente) [I].
