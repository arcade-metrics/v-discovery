# Ficha: LTI 1.3 / LTI Advantage

> Análises em conhecimento/interoperabilidade/tool-integration/lti-core.md (`iop.tool.lti-core`) e lti-advantage.md (`iop.tool.lti-advantage`).

```yaml
id: us.lti
name: Learning Tools Interoperability
acronym: LTI
jurisdiction: internacional (1EdTech)
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário (protocolo)
domain: [D6, D8]   # D1 indireto (context, NRPS)
official_url: https://www.1edtech.org/standards/lti
repository_url: unknown
version: LTI Core 1.3 (Document 3, 2019-04-16); Advantage: NRPS 2.0, AGS 2.0, Deep Linking 2.0
publication_date: 2019-04-16
last_updated: unknown
legal_status: voluntário
mandatory_scope: nenhum
education_levels: K-12, ensino superior
geographic_scope: internacional
language: inglês
license: unknown
technical_formats: OIDC, JWT, OAuth 2, JSON
api_available: sim
data_model_available: parcial (claims)
ontology_available: not_found
schemas_available: unknown
implementation_examples: ver conhecimento
related_standards: [OneRoster, Caliper, Common Cartridge]
entities: [Platform, Tool, Deployment, Context, ResourceLink, User (sub), Membership (NRPS), LineItem/Score/Result (AGS)]
relationships: launch = user × context × resource_link com roles[]
vocabularies: papéis LIS (§A.2, não lido), tipos de contexto
core_relevance: média — define o contrato de lançamento do VUOO como Tool em LMS americanos; C.IDN (sub por plataforma)
regional_adapter_relevance: média (canal de distribuição, não de dados oficiais)
limitations: ver conhecimento
open_questions: []
sources: [conhecimento]
access_date: 2026-11-05
research_status: apontado (sem nova pesquisa)
```

## O que falta para o crosswalk

- O `sub` do LTI é identificador da pessoa **por plataforma**; o Core precisa tratá-lo como C.IDN com `scheme` = emissor da plataforma, nunca como chave global [I].
- `context` (geralmente a section/class) mapeia para C.OFR; quando o LMS usa context para grupos ad hoc, para C.GRP (kind flexível) [I].
