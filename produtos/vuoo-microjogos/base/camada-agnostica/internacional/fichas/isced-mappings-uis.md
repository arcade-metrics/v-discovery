# Ficha: Mapeamentos ISCED 2011 do UIS

```yaml
id: int.isced-mappings
name: ISCED Mappings and Country Diagrams
acronym: —
jurisdiction: internacional (UIS), conteúdo nacional
issuing_organization: UNESCO Institute for Statistics, com respostas dos Estados-membros
reference_type: conjunto de dados de classificação (crosswalk nacional → ISCED)
domain: [D1, D8]
official_url: https://uis.unesco.org/en/isced-mappings ; https://www.uis.unesco.org/en/methods-and-tools/isced/mapping-and-diagrams
repository_url: https://download.uis.unesco.org/ISCED%20mapping/ (padrão de URL ISCED_2011_Mapping_<País>.xlsx)
version: por país; ano de referência na planilha (BR 2012/2013; US, PT, DE, UK 2020/2021; CN 2023)
publication_date: por país
last_updated: rolling basis [N03, p. 3]
legal_status: dado estatístico oficial validado pelo UIS
mandatory_scope: nenhum
education_levels: 0–8
geographic_scope: 201 países [N03, p. 4]
language: en + idioma nacional dos nomes de programa
license: unknown
technical_formats: XLSX (mapeamentos), JPG (diagramas)
api_available: not_found
data_model_available: sim, implícito nas colunas (modelo UOE)
ontology_available: não
schemas_available: não
implementation_examples: ver mapeamentos-isced.md
related_standards: [int.isced-2011]
entities: [programa nacional, qualificação]
relationships: programa → ISCED-P; qualificação → ISCED-A; programa → requisito de entrada (ISCED); programa → acesso a nível superior
vocabularies: colunas do questionário UOE (orientação, FT/PT, acesso, posição em graus)
core_relevance: alta — fonte de dados para o crosswalk de C.PRG
regional_adapter_relevance: alta — cada adaptador importa a sua planilha
limitations: granularidade de programa; anos de referência heterogêneos; dois layouts de planilha; nomes nacionais livres, sem identificador estável de programa ("Prog.2.1" é numeração interna e se repete no RU)
open_questions: [QI-01, QI-03, QI-04, QI-07]
sources: [N03, N04, N05, N06, N07, N08, N09, N10]
access_date: 2026-11-05
research_status: completo para os 6 países (níveis 0–3)
```

Colunas úteis ao Core (modelo UOE novo): programa (nome nacional e inglês), requisito mínimo de entrada, idade teórica de entrada, duração teórica, orientação, acesso direto ao nível seguinte, regime FT/PT, ISCED-P, matrículas, qualificação, ISCED-A, nível EQF (UE). O modelo antigo (Brasil) acrescenta "anos acumulados de escolaridade desde o início do ISCED 1" (col. K) [N05].
