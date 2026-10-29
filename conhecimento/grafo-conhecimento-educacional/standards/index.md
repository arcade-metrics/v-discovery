---
id: kg.std.index
titulo: Índice de normas e especificações do domínio
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2014rdf11concepts, w3c2026rdf12concepts, w3c2014rdfschema, w3c2012owl2overview, w3c2012owl2profiles, w3c2012owl2primer, w3c2012owl2syntax, w3c2009skos, w3c2009skosprimer, w3c2013sparql11query, w3c2013sparql11overview, w3c2017shacl, w3c2020jsonld11, w3c2013provo, w3c2024dcat3, ieee2020lom, ieee2020lomxml, dcmi2020terms, dcmi2026lrmi, onedtech2025case, ims2017case10, schemaorg2026learningresource, schemaorg2026releases, gqlstandards2024, opencypher2026, mec2026bncc]
relacoes:
  - { tipo: relacionado-a, alvo: kg.std.rdf }
  - { tipo: relacionado-a, alvo: kg.std.rdfs }
  - { tipo: relacionado-a, alvo: kg.std.owl2 }
  - { tipo: relacionado-a, alvo: kg.std.skos }
  - { tipo: relacionado-a, alvo: kg.std.sparql }
  - { tipo: relacionado-a, alvo: kg.std.shacl }
  - { tipo: relacionado-a, alvo: kg.std.json-ld }
  - { tipo: relacionado-a, alvo: kg.std.prov-o }
  - { tipo: relacionado-a, alvo: kg.std.comparison }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [W3C Recommendation, Candidate Recommendation Snapshot, W3C Working Group Note, IEEE Active Standard, 1EdTech Final Release, DCMI Recommendation, ISO/IEC International Standard]
---

# Índice de normas e especificações do domínio

## Definição e terminologia

Índice das especificações relevantes a grafos de conhecimento educacional, com status normativo verificado em 2026-10-29 nas páginas `w3.org/TR`, `standards.ieee.org`, `dublincore.org`, `imsglobal.org`, `schema.org` e `gqlstandards.org`. Cada entrada traz a chave BibTeX (nos fragmentos `kg-standards.bib` e `kg-vocabularies.bib`), o título, o status, a data e a URL.

Níveis de maturidade usados aqui, como aparecem nas próprias páginas:

- **W3C**: *Recommendation* (estável, endossada); *Candidate Recommendation Snapshot* (em curso); *Working Group Note* (informativa, não normativa).
- **IEEE SA**: *Active Standard*; *Superseded*; *Inactive-Withdrawn*; *Inactive-Reserved* [F: ieee2020lom].
- **1EdTech (ex-IMS Global)**: *Final Release* [F: onedtech2025case; ims2017case10].
- **DCMI**: *DCMI Recommendation* [F: dcmi2020terms].
- **ISO/IEC**: *International Standard* publicado [F: gqlstandards2024].

Legenda da coluna "Normativo": N = norma vigente; N-cr = em Candidate Recommendation, não final; I = informativa (Note) ou documento de divulgação; N-sup = norma que supersedeu outra listada.

## Fundamentos e funcionamento

### Pilha W3C de grafos

| Chave | Documento | Status | Data | Normativo | URL |
|---|---|---|---|---|---|
| w3c2014rdf11concepts | RDF 1.1 Concepts and Abstract Syntax | W3C Recommendation [F: w3c2014rdf11concepts] | 2014-02-25 | N | https://www.w3.org/TR/rdf11-concepts/ |
| w3c2026rdf12concepts | RDF 1.2 Concepts and Abstract Data Model | W3C Candidate Recommendation Snapshot [F: w3c2026rdf12concepts] | 2026-04-07 | N-cr | https://www.w3.org/TR/rdf12-concepts/ |
| w3c2014rdfschema | RDF Schema 1.1 | W3C Recommendation; atualização de status em 2023-12-01 [F: w3c2014rdfschema] | 2014-02-25 | N | https://www.w3.org/TR/rdf-schema/ |
| w3c2012owl2overview | OWL 2 Document Overview (2nd ed.) | W3C Recommendation [F: w3c2012owl2overview] | 2012-12-11 | N | https://www.w3.org/TR/owl2-overview/ |
| w3c2012owl2syntax | OWL 2 Structural Specification and Functional-Style Syntax (2nd ed.) | W3C Recommendation [F: w3c2012owl2syntax] | 2012-12-11 | N | https://www.w3.org/TR/owl2-syntax/ |
| w3c2012owl2profiles | OWL 2 Profiles (2nd ed.) | W3C Recommendation [F: w3c2012owl2profiles] | 2012-12-11 | N | https://www.w3.org/TR/owl2-profiles/ |
| w3c2012owl2primer | OWL 2 Primer (2nd ed.) | W3C Recommendation [F: w3c2012owl2primer] | 2012-12-11 | N | https://www.w3.org/TR/owl2-primer/ |
| w3c2009skos | SKOS Reference | W3C Recommendation [F: w3c2009skos] | 2009-08-18 | N | https://www.w3.org/TR/skos-reference/ |
| w3c2009skosprimer | SKOS Primer | W3C Working Group Note; atualização de status em 2023-10-30 [F: w3c2009skosprimer] | 2009-08-18 | I | https://www.w3.org/TR/skos-primer/ |
| w3c2013sparql11query | SPARQL 1.1 Query Language | W3C Recommendation [F: w3c2013sparql11query] | 2013-03-21 | N | https://www.w3.org/TR/sparql11-query/ |
| w3c2013sparql11overview | SPARQL 1.1 Overview | W3C Recommendation; aponta para as onze Recommendations do conjunto [F: w3c2013sparql11overview] | 2013-03-21 | N | https://www.w3.org/TR/sparql11-overview/ |
| w3c2017shacl | Shapes Constraint Language (SHACL) | W3C Recommendation [F: w3c2017shacl] | 2017-07-20 | N | https://www.w3.org/TR/shacl/ |
| w3c2020jsonld11 | JSON-LD 1.1 | W3C Recommendation; Recommendation anterior JSON-LD 1.0 de 2014-01-16 [F: w3c2020jsonld11] | 2020-07-16 | N | https://www.w3.org/TR/json-ld11/ |
| w3c2013provo | PROV-O: The PROV Ontology | W3C Recommendation [F: w3c2013provo] | 2013-04-30 | N | https://www.w3.org/TR/prov-o/ |
| w3c2024dcat3 | Data Catalog Vocabulary (DCAT) Version 3 | W3C Recommendation; Recommendation anterior DCAT 2 de 2020-02-04 [F: w3c2024dcat3] | 2024-08-22 | N | https://www.w3.org/TR/vocab-dcat-3/ |

O conjunto SPARQL 1.1 compreende onze W3C Recommendations publicadas na mesma data: Overview, Query Language, Update, Service Description, Federated Query, Query Results JSON Format, Query Results CSV and TSV Formats, Query Results XML Format (Second Edition), Entailment Regimes, Protocol e Graph Store HTTP Protocol [F: w3c2013sparql11overview, status]. Apenas Overview e Query Language foram abertos nesta sessão.

### Padrões educacionais

| Chave | Documento | Status | Data | Normativo | URL |
|---|---|---|---|---|---|
| ieee2020lom | IEEE 1484.12.1-2020, Standard for Learning Object Metadata | Active Standard; supersede 1484.12.1-2002; aprovação em 2020-09-24 [F: ieee2020lom] | 2020-11-16 | N-sup | https://standards.ieee.org/standard/1484_12_1-2020.html |
| ieee2020lomxml | IEEE 1484.12.3-2020, XML Schema binding para LOM | Active Standard, mesmo grupo de trabalho [F: ieee2020lomxml] | 2020 | N | https://standards.ieee.org/standard/1484_12_1-2020.html |
| dcmi2020terms | DCMI Metadata Terms | DCMI Recommendation [F: dcmi2020terms] | 2020-01-20 | N | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| dcmi2026lrmi | LRMI Terms e concept schemes | especificação DCMI mantida pelo LRMI Working Group; concept schemes declarados em RDF com SKOS [F: dcmi2026lrmi] | — | N | https://www.dublincore.org/specifications/lrmi/ |
| onedtech2025case | 1EdTech CASE Service v1.1 | Final Release [F: onedtech2025case] | 2025-01-24 | N | https://www.imsglobal.org/spec/case/v1p1 |
| ims2017case10 | IMS CASE Service Information Model v1.0 | IMS Final Release [F: ims2017case10] | 2017-07-07 | N | https://www.imsglobal.org/sites/default/files/CASE/casev1p0/information_model/caseservicev1p0_infomodelv1p0.html |
| schemaorg2026learningresource | schema.org, tipo LearningResource | vocabulário de fornecedor; release corrente 30.1 de 2026-09-16 [F: schemaorg2026releases] | 2026 | I | https://schema.org/LearningResource |
| mec2026bncc | Base Nacional Comum Curricular | documento normativo nacional, definido pela LDB (Lei 9.394/1996) [F: mec2026bncc] | — | N | http://basenacionalcomum.mec.gov.br/ |

### Grafos de propriedades

| Chave | Documento | Status | Data | Normativo | URL |
|---|---|---|---|---|---|
| gqlstandards2024 | ISO/IEC 39075:2024, Database languages — GQL | International Standard publicado, anunciado pelo comitê em 2024-04-17 [F: gqlstandards2024] | 2024 | N | https://www.gqlstandards.org/ |
| opencypher2026 | openCypher | especificação aberta de Cypher; evolui em direção a ISO/IEC 39075 GQL [F: opencypher2026] | — | I | https://opencypher.org/ |

O texto de ISO/IEC 39075:2024 não foi consultado: a página da ISO retornou HTTP 403 nesta sessão. O que se afirma vem do site do comitê de padronização e do openCypher.

## Requisitos e pressupostos

- Datas e status aqui refletem o estado das páginas em 2026-10-29. Um padrão em Candidate Recommendation pode avançar; um Active Standard do IEEE está dentro do ciclo de dez anos [F: ieee2020lom].
- Erratas: as especificações do W3C pedem que sejam verificadas e podem conter correções normativas [F: w3c2014rdf11concepts; w3c2009skos; w3c2012owl2overview; w3c2017shacl; w3c2013provo]. Nenhuma errata foi consultada nesta sessão.

## Relações com outros conceitos

Relaciona-se com todos os documentos de `standards/` e com kg.voc.comparison (os vocabulários educacionais em detalhe). A decisão de qual camada usar está em kg.std.comparison.

## Lacunas e questões abertas

- Nove das onze Recommendations de SPARQL 1.1 não foram abertas.
- Os textos integrais de IEEE 1484.12.1-2020 e de ISO/IEC 39075:2024 não são acessíveis sem compra; o que consta aqui vem das páginas públicas de catálogo.
- Não foram levantados: IMS LTI, QTI, OneRoster e Caliper, que pertencem ao domínio `interoperabilidade`, nem padrões de credenciais (Open Badges, Verifiable Credentials), que tocam este domínio pela via do CTDL.
- Nenhuma errata foi consultada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| w3c2026rdf12concepts | normativo | 2026-10-29 |
| w3c2014rdfschema | normativo | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
| w3c2012owl2profiles | normativo | 2026-10-29 |
| w3c2012owl2primer | normativo | 2026-10-29 |
| w3c2012owl2syntax | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| w3c2009skosprimer | normativo | 2026-10-29 |
| w3c2013sparql11query | normativo | 2026-10-29 |
| w3c2013sparql11overview | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
| w3c2020jsonld11 | normativo | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| w3c2024dcat3 | normativo | 2026-10-29 |
| ieee2020lom | normativo | 2026-10-29 |
| ieee2020lomxml | normativo | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
| dcmi2026lrmi | normativo | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| schemaorg2026releases | fornecedor | 2026-10-29 |
| gqlstandards2024 | tecnico | 2026-10-29 |
| opencypher2026 | fornecedor | 2026-10-29 |
| mec2026bncc | normativo | 2026-10-29 |
