# Ficha: CASE — Competencies and Academic Standards Exchange

> Análise completa em conhecimento/interoperabilidade/competencies/case.md (`iop.comp.case`): entidades, `CFAssociationTypeEnum` com definições, mudanças 1.0 → 1.1, extensões, mapeamento para SKOS. Não repetir.

```yaml
id: us.case
name: Competencies and Academic Standards Exchange
acronym: CASE
jurisdiction: internacional (1EdTech); publicação dos padrões estaduais dos EUA via CASE Network
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário (modelo de informação + serviço REST/JSON)
domain: [D2, D4, D5]   # D5: CFRubric (não verificado)
official_url: https://standards.1edtech.org/case/specifications/standards/v1p1
repository_url: unknown
version: 1.1 Final [E39]
publication_date: 2025-01-24 [E39]
last_updated: unknown
legal_status: voluntário
mandatory_scope: nenhum federal; uso estadual a verificar (Q08)
education_levels: K-12, ensino superior, força de trabalho
geographic_scope: internacional
language: inglês
license: unknown
technical_formats: JSON, REST
api_available: sim
data_model_available: sim
ontology_available: not_found (sem contexto JSON-LD oficial; ver conhecimento)
schemas_available: unknown
implementation_examples: CASE Network 2 (registro de frameworks dos 50 estados, segundo anúncio datado) [E22]; Google Classroom aceita `caseDocumentId`/`caseItemId` [E23]
related_standards: [CCSS, NGSS, OneRoster (LearningStandard GUIDs), Edu-API (LearningObjectiveSet), CLR/OB (Alignment), QTI]
entities: [CFPackage, CFDocument, CFItem, CFAssociation, CFItemType, CFSubject, CFConcept, CFLicense, CFAssociationGrouping, CFRubric]   # as cinco últimas não verificadas em fonte primária
relationships: CFAssociationTypeEnum (isChildOf, isPeerOf, isPartOf, exactMatchOf, precedes, isRelatedTo, replacedBy, exemplar, hasSkillLevel)
vocabularies: CFAssociationTypeEnum; frameworkType; CFItemType
core_relevance: alta — alvo direto de C.CFW, C.CMP, C.CAS
regional_adapter_relevance: alta (formato de importação de padrões estaduais)
limitations: ver conhecimento
open_questions: Q08
sources: [E22, E23, E39]
access_date: 2026-11-05
research_status: apontado (análise em conhecimento); acréscimos verificados só por trecho
```

## O que falta para o crosswalk

- Cada CFPackage contém exatamente um CFDocument (trecho de E39 via busca).
- GUIDs CASE já são consumidos como referência externa por plataformas grandes (Google Classroom: `caseDocumentId`, `caseItemId` opcional) [E23]; para o Core, isso confirma que C.IDN precisa aceitar `scheme = case-guid` em C.CMP e C.CFW [I].
- Edu-API referencia objetivos por `learningObjectiveSet` com `source = case` [E13]: alinhamento oferta↔competência por GUID CASE é padrão emergente [I].
- Lista completa de classes de CASE 1.1 (CFRubric, CFConcept, CFSubject etc.) segue não verificada, como já registrado em `conhecimento/`.
