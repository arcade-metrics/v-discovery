# Ficha: ISCED-F 2013 — Fields of Education and Training

```yaml
id: int.isced-f-2013
name: ISCED Fields of Education and Training 2013
acronym: ISCED-F 2013
jurisdiction: internacional (UNESCO)
issuing_organization: UNESCO Institute for Statistics
reference_type: classificação estatística internacional
domain: [D1, D4]
official_url: https://unesdoc.unesco.org/ark:/48223/pf0000228085_eng (manual 2014; não aberto, 403)
repository_url: not_found
version: ISCED-F 2013; descrições detalhadas publicadas em 2015 (pf0000235049)
publication_date: 2014
last_updated: unknown; "comprehensive revision" recomendada pelo ISCED Review Panel [N02; N03, p. 6]
legal_status: voluntário; uso em coletas da UE desde 2016 [N14]
mandatory_scope: estatística
education_levels: secundário, pós-secundário e superior (campos não se aplicam à educação geral básica além de 00)
geographic_scope: global
language: en (integral); traduções parciais [N13]
license: unknown
technical_formats: PDF
api_available: not_found
data_model_available: não (lista hierárquica)
ontology_available: not_found (oficial)
schemas_available: not_found
implementation_examples: Erasmus+ (códigos de área em acordos interinstitucionais) [N12, secundária]
related_standards: [int.isced-2011, ISCED 1997 fields]
entities: [campo amplo, campo estreito, campo detalhado]
relationships: hierarquia estrita de 3 níveis
vocabularies: 11 amplos / 29 estreitos / 80 detalhados (+ códigos 0, 8, 9) — ver terminologia.md §5
core_relevance: baixa para educação básica geral; média para itinerários técnicos e formação docente
regional_adapter_relevance: baixa
limitations: não é taxonomia de componentes curriculares; Matemática escolar ≠ 0541
open_questions: [QI-06]
sources: [N12, N13, N14]
access_date: 2026-11-05
research_status: parcial — tabela de códigos de fonte secundária que reproduz o Appendix 1; PDF oficial não acessado
```

## O que o Core adota (proposta)

Atributo opcional `C.PRG.fieldOfEducation` (`scheme = isced-f-2013`) só para programas profissionais/técnicos. **Não** ligar C.SUB ao ISCED-F [I].
