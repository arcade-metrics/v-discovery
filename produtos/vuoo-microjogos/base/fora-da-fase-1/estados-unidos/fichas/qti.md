# Ficha: QTI — Question and Test Interoperability

> Análise em conhecimento/interoperabilidade/assessment/qti.md (`iop.asmt.qti`).

```yaml
id: us.qti
name: Question and Test Interoperability
acronym: QTI
jurisdiction: internacional (1EdTech)
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário
domain: [D5, D7]   # D7 via perfil AccessForAll PNP v3
official_url: https://www.1edtech.org/standards/qti
repository_url: unknown
version: 3.0 (Final Release, Document 1.0)
publication_date: 2022-05-01
last_updated: unknown
legal_status: voluntário
mandatory_scope: nenhum federal; exigência em contratos de avaliação estadual não verificada
education_levels: K-12, ensino superior
geographic_scope: internacional
language: inglês
license: unknown
technical_formats: XML, Content Packaging
api_available: parcial (empacotamento; resultados)
data_model_available: sim
ontology_available: not_found
schemas_available: sim (XSD)
implementation_examples: ver conhecimento
related_standards: [CASE, AfA PNP v3, Content Packaging 1.2, IEEE LOM, OneRoster ARP]
entities: [AssessmentTest, TestPart, Section, AssessmentItem, ResponseDeclaration, OutcomeDeclaration, AssessmentResult]
relationships: teste ⊃ partes ⊃ seções ⊃ itens; item alinhado a CFItem
vocabularies: interações, tipos de resposta; PNP para necessidades de acesso
core_relevance: alta para C.ASM/C.ITM/C.RES; PNP é referência para C.SUP sem diagnóstico
regional_adapter_relevance: baixa-média
limitations: ver conhecimento
open_questions: []
sources: [conhecimento: imsglobal2022qti30]
access_date: 2026-11-05
research_status: apontado (sem nova pesquisa)
```

## O que falta para o crosswalk

- O perfil AccessForAll PNPv3 incluído no QTI 3.0 (`conhecimento/`, §2.4) é o mecanismo americano/internacional para declarar **necessidades e preferências de acesso** sem diagnóstico; mapeia para C.SUP com equivalência aproximada [I]. Já analisado em `acs.std.*` (AccessForAll/ISO 24751).
- Os nomes de entidades da linha `entities` são os do QTI conhecidos pelo autor; apenas AssessmentItem/AssessmentTest constam explicitamente do documento de `conhecimento/` [I].
