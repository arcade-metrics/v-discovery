# Ficha: IEEE 1484.20.3-2022 (Shareable Competency Definitions) e IEEE 1484.20.2-2022 (Defining Competencies)

> Sem documento em `conhecimento/`. Comparar com CASE (`iop.comp.case`), CTDL (`iop.comp.ctdl`) e ESCO (`iop.comp.esco`) em `conhecimento/interoperabilidade/competencies/`.

```yaml
id: int.ieee-1484-20
name: IEEE Standard for Learning Technology — Data Model for Shareable Competency Definitions (1484.20.3-2022); IEEE Recommended Practice for Defining Competencies (1484.20.2-2022)
acronym: IEEE SCD (1484.20.3); 1484.20.2
jurisdiction: internacional (IEEE)
issuing_organization: IEEE Computer Society, C/LT Learning Technology; WG C/LT/CD Competency Data Standards [N20]
reference_type: norma técnica (1484.20.3, modelo de dados) e prática recomendada (1484.20.2)
domain: [D2, D4]
official_url: https://standards.ieee.org/ieee/1484.20.3/10749/ ; https://standards.ieee.org/ieee/1484.20.2/10743/
repository_url: projeto IEEE SA Open vinculado, licença Apache 2.0 [N20]; URL do repositório not_found
version: 1484.20.3-2022 (Active); 1484.20.2-2022 (Active)
publication_date: 1484.20.3: PAR 2021-11-09, aprovação 2022-12-03, publicação 2023-07-27 [N20]; 1484.20.2: aprovação 2022-09-21, publicação 2022-12-02 [N21, trecho]
last_updated: emenda P1484.20.3a em andamento (IEEE SA Open, documentos não normativos como perfis de aplicação, esclarecer rubricas) [N20]
legal_status: voluntário
mandatory_scope: nenhum
education_levels: todos (escola, superior, trabalho)
geographic_scope: global
language: en
license: texto pago/assinatura [N20]; artefatos open source Apache 2.0 [N20]
technical_formats: unknown (texto não acessado; projeto de 2021 sugeria RDF/JSON-LD — not_found em fonte oficial)
api_available: não (modelo de dados)
data_model_available: sim (pago)
ontology_available: unknown
schemas_available: unknown
implementation_examples: ADL (grupo de trabalho) [trecho]; não levantado
related_standards: [IEEE 1484.20.1-2007 (RCD, antecessor), CASE, CTDL, ESCO, int.ieee-2881]
entities: [competency definition; demais classes unknown]
relationships: unknown
vocabularies: unknown
core_relevance: média — candidato a modelo neutro para C.CMP; depende de acesso ao texto
regional_adapter_relevance: baixa (EUA usa CASE na prática)
limitations: texto pago; nenhuma classe verificada; escopo declarado é a definição da competência, não o currículo nem o alinhamento escolar
open_questions: [QI-17]
sources: [N20, N21]
access_date: 2026-11-05
research_status: só metadados oficiais
```

Escopo (página IEEE): "Defined in this standard are a data model for describing, referencing, and sharing competency definitions"; "It enables interoperability among learning systems that deal with competency information" [N20].

## O que o Core adota (proposta)

Não adotar como formato. Usar como **referência neutra** ao desenhar C.CMP e conferir, quando o texto estiver disponível, se o Core consegue exportar para 1484.20.3 sem perda. Para importação/exportação de currículos, CASE (EUA) e SKOS continuam sendo os alvos práticos [I].
