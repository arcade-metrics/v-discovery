# Ficha: COPPA — Children's Online Privacy Protection Rule

> Análise completa em conhecimento/privacidade-seguranca-e-governanca/legal-framework/gdpr-k-and-coppa.md (`psg.legal.gdpr-k-and-coppa`): 16 CFR Part 312, revisão de 2025 (90 FR 16918), consentimento pela escola (FAQ §N). Consentimento parental em `psg.consent.parental-consent`. Não repetir.

```yaml
id: us.coppa
name: Children's Online Privacy Protection Rule
acronym: COPPA
jurisdiction: Estados Unidos (federal)
issuing_organization: Federal Trade Commission (FTC)
reference_type: regulamento federal (com base em lei de 1998)
domain: [D8]
official_url: ver fontes ftc2025coppa e ftc2025coppafinalrule em conhecimento/ (URL não reacessada nesta rodada)
repository_url: n/a
version: 16 CFR Part 312, revisão final 90 FR 16918 (2025-04-22), vigência 2025-06-23, conformidade até 2026-04-22
publication_date: ver version
last_updated: 2025-04-22
legal_status: regulamento vinculante
mandatory_scope: operadores de serviços online dirigidos a menores de 13 anos ou com conhecimento efetivo de coleta deles
education_levels: K-8 na prática (idade < 13) [I]
geographic_scope: EUA
language: inglês
license: domínio público
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [FERPA, leis estaduais]
entities: [verifiable parental consent, school authorization (FAQ), written data retention policy, written information security program]
relationships: escola pode consentir como agente dos pais só para uso "for the use and benefit of the school"
vocabularies: métodos de verificação de consentimento (§312.5(b)(2))
core_relevance: alta — C.CNS precisa distinguir concedente (responsável × escola) e finalidade; política de retenção
regional_adapter_relevance: obrigatória para operar com menores de 13 nos EUA
limitations: ver conhecimento
open_questions: Q15
sources: [conhecimento: ftc2025coppa, ftc2025coppafinalrule, ftc2025coppafaq]
access_date: 2026-11-05
research_status: apontado (sem nova pesquisa)
```

## O que falta para o crosswalk

- Consentimento separado para divulgação a terceiros (revisão 2025) → C.CNS por finalidade **e** por destinatário [I].
- Retenção não indefinida + política escrita → o Core precisa de política de retenção associada a categoria de dado (candidato; ver questoes-abertas Q16).
