# Ficha: Caliper Analytics

> Análise em conhecimento/interoperabilidade/learning-records/caliper.md (`iop.lr.caliper`): Event, Entity, Envelope, Sensor, perfis, propriedades obrigatórias. Comparação com xAPI em `iop.lr.comparison`.

```yaml
id: us.caliper
name: Caliper Analytics
acronym: Caliper
jurisdiction: internacional (1EdTech)
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário (modelo de eventos + vocabulário JSON-LD + binding)
domain: [D6, D3]
official_url: https://www.1edtech.org/standards/caliper
repository_url: https://github.com/1EdTech/caliper-spec
version: 1.2 Final
publication_date: 2020-03-27
last_updated: unknown
legal_status: voluntário
mandatory_scope: nenhum
education_levels: K-12, ensino superior
geographic_scope: internacional
language: inglês
license: unknown
technical_formats: JSON-LD
api_available: sim (envio de Envelope a endpoint)
data_model_available: sim
ontology_available: contexto JSON-LD (ver conhecimento)
schemas_available: unknown
implementation_examples: sim (no documento)
related_standards: [xAPI, LTI, OneRoster]
entities: [Event (actor, action, object, eventTime, group, membership, session, edApp), Entity (Person, Organization, CourseSection, Membership, DigitalResource, AssessmentItem…), Envelope, Sensor]
relationships: Event liga Person → ação → Entity, no contexto de group (CourseSection) e membership
vocabularies: perfis (metric profiles) e ações por perfil
core_relevance: média-alta — alvo de C.EVT; mostra que o evento carrega o contexto organizacional (group/membership)
regional_adapter_relevance: baixa (não é exigido por jurisdição)
limitations: nenhuma versão posterior a 1.2 encontrada [E38]
open_questions: Q09
sources: [E38]
access_date: 2026-11-05
research_status: apontado; versão reconfirmada por trecho
```

## O que falta para o crosswalk

- Em 2026-11-05 não foi encontrada versão 1.3; a tag `1.2-final` é a mais recente identificada [E38, trecho].
- Os nomes `group` (ex.: CourseSection), `membership` e `session` como propriedades de Event vêm do conhecimento prévio do autor sobre a spec 1.2 e **não** foram relidos nesta rodada [I]; conferir contra §2.1 da spec antes de usar no crosswalk definitivo.
