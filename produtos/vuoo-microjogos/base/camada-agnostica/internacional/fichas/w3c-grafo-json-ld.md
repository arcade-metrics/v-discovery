# Ficha curta: W3C RDF, RDFS, OWL 2, SKOS, JSON-LD 1.1, SHACL, PROV-O

> Análise completa em `conhecimento/grafo-conhecimento-educacional/standards/` — rdf.md (`kg.std.rdf`), rdfs.md, owl2.md, skos.md, json-ld.md, shacl.md, prov-o.md, comparação em comparison.md. Não repetir.

```yaml
id: int.w3c-semantic-stack
name: W3C RDF / RDFS / OWL 2 / SKOS / JSON-LD 1.1 / SHACL / PROV-O
acronym: —
jurisdiction: internacional (W3C)
issuing_organization: W3C
reference_type: recomendações W3C
domain: [D2, D4, D8]
official_url: https://www.w3.org/TR/json-ld11/ (e demais em conhecimento/)
repository_url: https://github.com/w3c/json-ld-syntax (JSON-LD)
version: JSON-LD 1.1, W3C Recommendation de 2020-07-16 [N27]; demais: ver conhecimento/
publication_date: ver conhecimento/
last_updated: JSON-LD 1.2 sem Working Draft publicado; carta do JSON-LD WG aprovada em jan. 2026 com FPWD previsto para o 4º tri de 2026 e conclusão no 4º tri de 2027 (rascunho de carta) [N28, trecho]
legal_status: voluntário
mandatory_scope: nenhum
education_levels: não se aplica
geographic_scope: global
language: en
license: W3C
technical_formats: Turtle, JSON-LD, RDF/XML, N-Triples
api_available: SPARQL (kg.std.sparql)
data_model_available: sim
ontology_available: sim
schemas_available: SHACL
implementation_examples: ver conhecimento/
related_standards: [int.cool-uris, int.json-schema, VC 2.0 (@context obrigatório)]
entities: ver conhecimento/
relationships: ver conhecimento/
vocabularies: SKOS (skos:Concept, broader, exactMatch, closeMatch…), PROV (Entity, Activity, Agent)
core_relevance: alta — C.VOC (SKOS), C.PRV (PROV-O), C.CAS (mapeamentos SKOS), exposição semântica (JSON-LD)
regional_adapter_relevance: média
limitations: ver conhecimento/
open_questions: [QI-16]
sources: [N27, N28]
access_date: 2026-11-05
research_status: apontado; só status do JSON-LD atualizado
```

## O que falta para o Core

- Os **tipos de equivalência** do crosswalk (`_convencoes.md` §4: exata, aproximada, parcial, mais ampla, mais restrita, inexistente) casam com SKOS: `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch`; "inexistente" é ausência de asserção [I]. Propõe-se que C.CAS serialize assim.
- Contexto JSON-LD do Core: um `@context` versionado por URI persistente; dados de API continuam JSON puro válido contra JSON Schema, e o contexto só dá semântica [I].
- Ficar em JSON-LD **1.1**; 1.2 é sobretudo errata e ainda não tem rascunho [N28, trecho].
