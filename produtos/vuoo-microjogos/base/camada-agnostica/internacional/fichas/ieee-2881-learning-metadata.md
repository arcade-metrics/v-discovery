# Ficha: IEEE 2881-2025 — Learning Metadata Terms (ex-P2881)

**Atualização de status:** o projeto P2881 virou norma ativa, **IEEE 2881-2025**, publicada em 2025-10-03 [N22].

```yaml
id: int.ieee-2881
name: IEEE Standard for Learning Metadata Terms
acronym: IEEE 2881 (LMT)
jurisdiction: internacional (IEEE)
issuing_organization: IEEE Computer Society, C/LT; WG LMeta - Learning Metadata [N22]
reference_type: norma técnica (modelo conceitual de metadados)
domain: [D6, D8]
official_url: https://standards.ieee.org/ieee/2881/11719/
repository_url: projeto IEEE SA Open "LMT", Apache 2.0 [N22]; URL not_found
version: 2881-2025 (Active)
publication_date: PAR 2024-09-26; aprovação 2025-05-28; publicação 2025-10-03 [N22]
last_updated: 2025-10-03
legal_status: voluntário
mandatory_scope: nenhum
education_levels: todos
geographic_scope: global
language: en
license: texto pago/assinatura [N22]
technical_formats: modelo alinhado a RDF, independente de serialização [N22]
api_available: não
data_model_available: sim (pago)
ontology_available: provável (RDF), não verificado
schemas_available: unknown
implementation_examples: not_found
related_standards: [IEEE LOM 1484.12.1 (base declarada em fonte secundária), LRMI/schema.org, Dublin Core]
entities: [Learning Resource, Learning Event] [N22]
relationships: unknown
vocabularies: unknown
core_relevance: média — a distinção oficial entre recurso e evento de aprendizagem é a mesma que o Core faz entre C.ACT e C.EVT/C.SCH
regional_adapter_relevance: baixa
limitations: texto pago; termos não verificados
open_questions: [QI-18]
sources: [N22]
access_date: 2026-11-05
research_status: só metadados oficiais
```

Escopo (página IEEE): modelo de "classes and properties that intentionally align to a Resource Description Framework (RDF) type of model"; "It centers around different types of Learning Resources and Learning Events, distinguishing between the two as both were often previously categorized as Learning Objects" [N22].

## O que o Core adota (proposta)

Manter LRMI/schema.org como serialização prática de C.ACT (ver `iop.md.lrmi-schema-org`) e registrar 2881 como alvo de alinhamento futuro. A separação recurso × evento (2881) confirma C.ACT ≠ C.EVT [I].
