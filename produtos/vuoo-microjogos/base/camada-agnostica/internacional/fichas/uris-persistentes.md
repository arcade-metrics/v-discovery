# Ficha: URIs HTTP persistentes (Cool URIs)

```yaml
id: int.cool-uris
name: Cool URIs for the Semantic Web; Cool URIs don't change
acronym: —
jurisdiction: internacional (W3C)
issuing_organization: W3C Semantic Web Education and Outreach Interest Group; T. Berners-Lee (1998)
reference_type: nota de grupo de interesse (não normativa) + ensaio
domain: [D8]
official_url: https://www.w3.org/TR/cooluris/ ; https://www.w3.org/Provider/Style/URI
repository_url: não se aplica
version: Interest Group Note, 2008-12-03 [N29]
publication_date: 2008-12-03
last_updated: 2008-12-03
legal_status: recomendação de boa prática; o grupo "does not expect this document to become a W3C Recommendation" [N29]
mandatory_scope: nenhum
education_levels: não se aplica
geographic_scope: global
language: en
license: W3C document license
technical_formats: HTTP, RDF, HTML
api_available: não se aplica
data_model_available: não
ontology_available: não
schemas_available: não
implementation_examples: identificadores de vocabulários W3C; ESCO; CTDL [I]
related_standards: [kg.std.rdf, kg.std.skos, kg.std.json-ld]
entities: [recurso, documento descritor]
relationships: URI de recurso → documento (via # ou 303 See Other)
vocabularies: —
core_relevance: alta para vocabulários e currículos publicados (C.VOC, C.CFW, C.CMP); baixa para dados pessoais (nunca publicar)
regional_adapter_relevance: média (adaptador publica URIs de códigos nacionais, ex.: BNCC)
limitations: nota de 2008; não trata versionamento de conceitos
open_questions: [QI-14]
sources: [N29]
access_date: 2026-11-05
research_status: verificado
```

## Pontos da nota (§4) e escolha proposta

- **Hash URIs** (`…/vocab#termo`): bons para conjuntos pequenos e estáveis, servidos como arquivo estático; custo: baixar o arquivo inteiro [N29, 4.1].
- **303 URIs**: redirecionamento por recurso; servem grandes conjuntos; custo: ida e volta extra [N29, 4.2–4.3].
- **Negociação de conteúdo**: a mesma URI serve HTML ou RDF conforme `Accept` [N29, 2.1, 4.7].

Proposta [I]: vocabulários do Core (níveis, tipos de apoio) com hash URIs sob um domínio próprio e versionado no caminho (`/vocab/v1#…`); itens de currículo (milhares de habilidades) com URIs por item e negociação de conteúdo. O nome do domínio é decisão de produto (QI-14).
