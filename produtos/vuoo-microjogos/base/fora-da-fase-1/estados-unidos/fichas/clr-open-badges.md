# Ficha: CLR 2.0 e Open Badges 3.0

> Análises em conhecimento/interoperabilidade/credentials/clr.md (`iop.cred.clr`), open-badges.md (`iop.cred.open-badges`) e verifiable-credentials.md.

```yaml
id: us.clr-open-badges
name: Comprehensive Learner Record / Open Badges
acronym: CLR / OB
jurisdiction: internacional (1EdTech)
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário (modelo de dados de credencial verificável)
domain: [D3, D5, D8]
official_url: https://www.1edtech.org/standards/comprehensive-learner-record ; https://www.1edtech.org/standards/open-badges
repository_url: unknown
version: CLR 2.0 (Final, Document 1.1, 2025-10-14); Open Badges 3.0 (Final, Document 1.4.5, 2026-06-29)
publication_date: ver version
last_updated: ver version
legal_status: voluntário
mandatory_scope: nenhum
education_levels: todos
geographic_scope: internacional
language: inglês
license: unknown
technical_formats: JSON-LD, W3C VC Data Model 2.0 (e 1.1)
api_available: sim (API de troca)
data_model_available: sim
ontology_available: contexto JSON-LD
schemas_available: sim (JSON Schema)
implementation_examples: ver conhecimento
related_standards: [W3C VC, CASE (alvos de Alignment), QTI]
entities: [Achievement, AchievementCredential, ClrCredential, Alignment, Result, ResultDescription, RubricCriterionLevel, Evidence, Profile]
relationships: credencial → achievement → alignment (CFItem); result → resultDescription (rubrica)
vocabularies: AchievementType, ResultType, ResultStatusType
core_relevance: média — alvo de C.CRD, C.RES (rubrica), C.EVD
regional_adapter_relevance: baixa
limitations: ver conhecimento
open_questions: []
sources: [conhecimento: imsglobal2025clr20, imsglobal2026ob30]
access_date: 2026-11-05
research_status: apontado (sem nova pesquisa)
```

## O que falta para o crosswalk

- `Alignment` aponta para frameworks externos (tipicamente GUID CASE) — confirma que C.CRD precisa de relação tipada para C.CMP via C.CAS [I].
- `ResultDescription` com níveis de rubrica ("approaches", "meets", "exceeds") é o único ponto do pacote EUA que modela **rubrica** explicitamente além de CASE CFRubric (não verificado); o Core provisório não tem entidade de rubrica — ver questoes-abertas Q12.
