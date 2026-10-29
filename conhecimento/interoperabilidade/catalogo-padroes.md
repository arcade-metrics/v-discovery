---
id: iop.catalogo
titulo: Catálogo de padrões
tipo: mapa
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2023xapi, aicc2016cmi5, imsglobal2020caliper, imsglobal2019lti13, imsglobal2019ltinrps, imsglobal2019ltiags, imsglobal2019ltidl, scorm2026versions, imsglobal2011cc, imsglobal2022qti30, imsglobal2022oneroster, edfi2026datastandard, a4l2021sifspecs, nces2026ceds, standict2026lom, dcmi2020terms, dcmi2026lrmi, schemaorg2026learningresource, imsglobal2017case, credengine2026ctdl, esco2025what, w3c2025vcdm, imsglobal2026ob30, imsglobal2025clr20, w3c2009skos, who2001icf, hl72023fhir, brasil2018lgpd, iso2020ts20748, a4l2022sifna]
relacoes:
  - { tipo: complementa, alvo: iop.matriz }
  - { tipo: depende-de, alvo: iop.fund.dados-vs-protocolo }
termos: [padrão, especificação, versão, status, mantenedor]
---

# Catálogo de padrões

Um padrão por linha. "Versão de referência" é a versão consultada nesta rodada, com a data que a própria fonte declara. Status segue a nomenclatura do mantenedor. A coluna "Tipo de fonte" distingue norma de organismo de normalização (IEEE, W3C, ISO, OMS, HL7), especificação de consórcio (1EdTech, ADL, AICC, A4L, Ed-Fi), vocabulário institucional (NCES, Comissão Europeia, Credential Engine) e lei.

## Registro de experiências e eventos

| Padrão | Mantenedor | Versão de referência | Data | Status | Tipo de fonte | Documento |
|---|---|---|---|---|---|---|
| xAPI | IEEE LTSC | IEEE 9274.1.1-2023 | publicada 2023-10-06 [F: ieee2023xapi] | Active Standard [F: ieee2023xapi] | norma | iop.lr.xapi |
| cmi5 | cmi5 Working Group (AICC) | Quartz, 1st Edition | 2016-06-01 [F: aicc2016cmi5] | production release [F: aicc2016cmi5] | consórcio | iop.lr.cmi5 |
| Caliper Analytics | 1EdTech | 1.2 | 2020-03-27 [F: imsglobal2020caliper] | Final Release [F: imsglobal2020caliper] | consórcio | iop.lr.caliper |
| Learning analytics interoperability | ISO/IEC JTC 1/SC 36 | TS 20748-3:2020 | 2020 [F: iso2020ts20748] | Technical Specification | norma | — (citado em iop.fund.mapeamento-e-proveniencia) |

## Integração de ferramentas e conteúdo

| Padrão | Mantenedor | Versão de referência | Data | Status | Tipo de fonte | Documento |
|---|---|---|---|---|---|---|
| LTI Core | 1EdTech | 1.3 (doc. 3) | 2019-04-16 [F: imsglobal2019lti13] | Final Release [F: imsglobal2019lti13] | consórcio | iop.tool.lti-core |
| LTI NRPS | 1EdTech | 2.0 | 2019-04-16 [F: imsglobal2019ltinrps] | Final Release [F: imsglobal2019ltinrps] | consórcio | iop.tool.lti-advantage |
| LTI AGS | 1EdTech | 2.0 (doc. 3) | 2019-04-16 [F: imsglobal2019ltiags] | Final Release [F: imsglobal2019ltiags] | consórcio | iop.tool.lti-advantage |
| LTI Deep Linking | 1EdTech | 2.0 (doc. 2) | 2019-04-16 [F: imsglobal2019ltidl] | Final Release [F: imsglobal2019ltidl] | consórcio | iop.tool.lti-advantage |
| SCORM | ADL | 2004 4th Edition | 2009-03 [F: scorm2026versions] | estável, sem evolução ativa [I] | consórcio | iop.tool.scorm |
| Common Cartridge | 1EdTech | 1.3 (Thin CC guide 2015) | 2013-07 [F: imsglobal2011cc] | Final Specification [F: imsglobal2011cc] | consórcio | iop.tool.common-cartridge |
| QTI | 1EdTech | 3.0 (doc. 1.0) | 2022-05-01 [F: imsglobal2022qti30] | Final Release [F: imsglobal2022qti30] | consórcio | iop.asmt.qti |

## Dados escolares, matrícula e vocabulário

| Padrão | Mantenedor | Versão de referência | Data | Status | Tipo de fonte | Documento |
|---|---|---|---|---|---|---|
| OneRoster | 1EdTech | 1.2 (doc. 2) | 2022-09-19 [F: imsglobal2022oneroster] | Final Release [F: imsglobal2022oneroster] | consórcio | iop.ros.oneroster |
| Ed-Fi Data Standard | Ed-Fi Alliance | 6.0 (5.x em suporte) | 6.0 em 2025 [F: edfi2026datastandard] | em evolução [F: edfi2026datastandard] | consórcio | iop.ros.ed-fi |
| SIF | Access 4 Learning | por localidade (NA 4.3) | NA 4.3 publicada [F: a4l2022sifna] | versão corrente não verificada | consórcio | iop.ros.sif |
| CEDS | NCES | não verificada | — | adesão voluntária [F: nces2026ceds] | vocabulário institucional | iop.ros.ceds |
| Educacenso | INEP | leiaute anual | não verificada | obrigatório no Brasil [I] | sistema nacional | iop.br.educacenso |

## Metadados de recurso

| Padrão | Mantenedor | Versão de referência | Data | Status | Tipo de fonte | Documento |
|---|---|---|---|---|---|---|
| IEEE LOM | IEEE | 1484.12.1-2020 | 2020 [F: standict2026lom] | ativa, substitui 2002 [F: standict2026lom] | norma | iop.md.ieee-lom |
| DCMI Metadata Terms | DCMI | identificador 2020-01-20 | 2020-01-20 [F: dcmi2020terms] | DCMI Recommendation [F: dcmi2020terms] | consórcio | iop.md.dublin-core |
| LRMI | DCMI | não declarada na página | — [F: dcmi2026lrmi] | especificação DCMI [F: dcmi2026lrmi] | consórcio | iop.md.lrmi-schema-org |
| schema.org/LearningResource | Schema.org | v30.1 (desenvolvimento) | 2026-09-16 [F: schemaorg2026learningresource] | tipo marcado como novo [F: schemaorg2026learningresource] | consórcio | iop.md.lrmi-schema-org |

## Competências e currículo

| Padrão | Mantenedor | Versão de referência | Data | Status | Tipo de fonte | Documento |
|---|---|---|---|---|---|---|
| CASE | 1EdTech | 1.0 | 2017-07-07 [F: imsglobal2017case] | Final Release [F: imsglobal2017case] | consórcio | iop.comp.case |
| CTDL / CTDL-ASN / QData | Credential Engine | não verificada | — | "de facto standards" [F: credengine2026ctdl] | vocabulário institucional | iop.comp.ctdl |
| ESCO | Comissão Europeia (DG EMPL) | v1.2.1 (release 6.0.0) | 2025-12-10 [F: esco2025what] | classificação oficial da UE [F: esco2025what] | vocabulário institucional | iop.comp.esco |

## Credenciais

| Padrão | Mantenedor | Versão de referência | Data | Status | Tipo de fonte | Documento |
|---|---|---|---|---|---|---|
| Verifiable Credentials Data Model | W3C | 2.0 | 2025-05-15 [F: w3c2025vcdm] | W3C Recommendation [F: w3c2025vcdm] | norma | iop.cred.verifiable-credentials |
| Open Badges | 1EdTech | 3.0 (doc. 1.4.5) | 2026-06-29 [F: imsglobal2026ob30] | Final Release [F: imsglobal2026ob30] | consórcio | iop.cred.open-badges |
| Comprehensive Learner Record | 1EdTech | 2.0 (doc. 1.1) | 2025-10-14 [F: imsglobal2025clr20] | Final Release [F: imsglobal2025clr20] | consórcio | iop.cred.clr |

## Semântica, saúde e regime jurídico

| Padrão | Mantenedor | Versão de referência | Data | Status | Tipo de fonte | Documento |
|---|---|---|---|---|---|---|
| SKOS | W3C | SKOS Reference | 2009-08-18 [F: w3c2009skos] | W3C Recommendation [F: w3c2009skos] | norma | iop.sem.vocabularios-e-skos |
| CIF / ICF | OMS | ICF | endossada em 2001-05-22 [F: who2001icf] | padrão internacional [F: who2001icf] | norma | iop.health.cif |
| FHIR | HL7 | R5 (v5.0.0) | geração do doc. 2023-03-26 [F: hl72023fhir] | STU [F: hl72023fhir] | norma | iop.health.fhir |
| LGPD | Brasil | Lei 13.709/2018 | 2018-08-14 [F: brasil2018lgpd] | em vigor | lei | iop.br.lgpd |

## Observações sobre o catálogo

- Datas ausentes significam que a fonte consultada não as declara, não que não existam. Cada caso está registrado como lacuna no documento correspondente [I].
- "Versão de referência" não é necessariamente a versão mais recente: é a que foi consultada e citada nesta base. Ver `relatorio.md`.
- Para o que cada padrão especifica (dados, vocabulário, binding, protocolo, empacotamento), ver `iop.fund.dados-vs-protocolo`.
