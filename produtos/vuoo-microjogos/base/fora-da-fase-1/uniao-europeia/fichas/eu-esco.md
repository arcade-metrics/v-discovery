# ESCO (complemento)

```yaml
id: eu-esco
name: European Skills, Competences, Qualifications and Occupations
acronym: ESCO
jurisdiction: União Europeia
issuing_organization: Comissão Europeia, DG EMPL
reference_type: classificação multilíngue / vocabulário (SKOS)
domain: [D2, D8]
official_url: https://esco.ec.europa.eu/
repository_url: ver documento existente
version: ver documento existente
publication_date: ver documento existente
last_updated: ver documento existente
legal_status: vocabulário de referência; uso exigido em serviços EURES/Europass por atos próprios (não verificado aqui)
mandatory_scope: ver documento existente
education_levels: transversal (orientado a mercado de trabalho)
geographic_scope: UE/EEE
language: multilíngue
license: ver documento existente
technical_formats: [RDF/SKOS, CSV, API]
api_available: sim (ver documento existente)
data_model_available: sim
ontology_available: sim
schemas_available: sim
implementation_examples: elm:relatedESCOSkill
related_standards: [eu-elm, EQF, ISCO-08, DigComp]
entities: Occupation, Skill/Competence, Knowledge, Qualification
relationships: ocupação ↔ habilidade essencial/opcional; habilidade ↔ conhecimento
vocabularies: ESCO skills pillar, occupations pillar
core_relevance: baixa para educação básica; útil para alinhamento de competências digitais/transversais
regional_adapter_relevance: média
limitations: orientado a ocupações; não substitui currículo escolar
open_questions: relação formal ESCO × EQF não documentada nas páginas consultadas (já registrada no doc existente)
sources: [S-UE-01, S-UE-02, S-UE-05]
access_date: 2026-11-05
research_status: apontado (análise principal em conhecimento/)
```

## Análise

**Dono do fato:** `conhecimento/interoperabilidade/competencies/esco.md` (`iop.comp.esco`; o antigo `kg.voc.esco` redireciona para ele). Não reescrito aqui.

O que falta lá e importa para o adaptador UE:

1. **Ligação ELM → ESCO**: `elm:relatedESCOSkill` (alcance `skos:Concept`) no `LearningOutcome` [S-UE-02]; é o mecanismo pelo qual um resultado de aprendizagem aponta para ESCO sem igualá-los.
2. **Listas controladas compartilhadas**: a coleção Europass do EU Vocabularies foi "developed by ESCO and the EDC team" e inclui "Skill type", "Skill reusability level", "Key competences for lifelong learning" e "Digital Competence Framework" [S-UE-05]. Ou seja, DigComp e as competências-chave de 2018 já existem como vocabulário SKOS reutilizável.
3. [I] Para o Core, ESCO entra como C.CFW externo, alinhado via C.CAS de tipo "alinhamento", nunca como equivalência.
