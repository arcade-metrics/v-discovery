# Inventário do que já existe

Cruzamento entre as referências do [briefing](padroes-README.md) e o trabalho já feito no repositório, em 2026-11-05. Regra: **cada fato tem um dono**. Transcrição de fonte normativa mora em `base/`, exceto a BNCC, cuja fonte única é o repositório vuoo-base, release v1.1 (https://github.com/arcade-metrics/v-base), com ids `bncc-2018/<CODIGO>` e `bncc-computacao-2022/<CODIGO>`; análise conceitual de padrão mora em `conhecimento/` e é citada pelo id.

## 1. Transcrições de fonte

Em `base/camada-brasil/<pasta>/`.

| Pasta | Fonte | Domínios |
|---|---|---|
| [camada-brasil/cmdeb/](camada-brasil/cmdeb/README.md) | CMDEB, Anexo da Portaria MEC 832/2025 (MEC Gestão Presente) | D1, D3, D7 |
| [fora-da-fase-1/brasil/bncc-dados/](fora-da-fase-1/brasil/bncc-dados/README.md) | Repositório bncc-dev/bncc-dados: arquitetura de dado normativo verificado | D8 |
| [brasil/bncc-pacotes/](fora-da-fase-1/brasil/bncc-pacotes/README.md) | Repositório bncc-dev/bncc-pacotes: distribuição (npm, PyPI, MCP) | D8 |

## 2. Já analisado em `conhecimento/` (citar, não reescrever)

| Referência do briefing | Documento existente |
|---|---|
| Educacenso / Censo Escolar | `conhecimento/interoperabilidade/brazil/educacenso.md` (iop.br.educacenso) |
| LGPD | `iop.br.lgpd`; `conhecimento/privacidade-seguranca-e-governanca/legal-framework/lgpd-children.md` (psg.legal.lgpd-children); ECA digital em psg.legal.eca-and-digital-eca |
| BNCC (como grafo) | `conhecimento/grafo-conhecimento-educacional/curriculum/bncc.md` (kg.curr.bncc) |
| AEE, PNEEPEI, LBI, Libras, eMAG/NBR 17225 | `conhecimento/acessibilidade-educacao-especial-e-dua/brazil/` (acs.br.*) |
| Ed-Fi, CEDS, OneRoster, SIF | `conhecimento/interoperabilidade/rostering/` (iop.ros.*), comparação em iop.ros.comparison |
| CASE, CTDL, ESCO | `conhecimento/interoperabilidade/competencies/` (iop.comp.*) e `grafo-conhecimento-educacional/vocabularies/` (kg.voc.*) |
| LTI, Common Cartridge, SCORM | `conhecimento/interoperabilidade/tool-integration/` (iop.tool.*) |
| Caliper, xAPI, cmi5 | `conhecimento/interoperabilidade/learning-records/` (iop.lr.*) |
| QTI | iop.asmt.qti |
| CLR, Open Badges, Verifiable Credentials | `conhecimento/interoperabilidade/credentials/` (iop.cred.*) |
| IEEE LOM, Dublin Core, LRMI/schema.org | iop.md.*, kg.voc.* |
| RDF, RDFS, OWL, SKOS, JSON-LD, SHACL, SPARQL, PROV-O | `conhecimento/grafo-conhecimento-educacional/standards/` (kg.std.*) |
| WCAG, WAI-ARIA, AccessForAll/ISO 24751, EN 301 549 | `conhecimento/acessibilidade-educacao-especial-e-dua/standards/` (acs.std.*) |
| CAST UDL | `conhecimento/acessibilidade-educacao-especial-e-dua/udl/` (acs.udl.*) |
| CIF/ICF, FHIR | iop.health.cif, iop.health.fhir |
| FERPA, COPPA, GDPR-K | psg.legal.gdpr-k-and-coppa (FERPA: verificar cobertura) |
| Papéis escolares, RBAC/ABAC | psg.access.school-roles, psg.access.rbac-and-abac |
| Identidade, mapeamento, proveniência | iop.fund.identidade-e-contexto, iop.fund.mapeamento-e-proveniencia, kg.eng.versioning-and-provenance |
| Modelo conceitual em camadas | kg.mod.conceptual-model, kg.mod.layer-separation |
| Catálogo geral de versões | iop.catalogo (`conhecimento/interoperabilidade/catalogo-padroes.md`) |

## 3. Lacunas (sem nada no repositório)

| Jurisdição | Referências sem documento |
|---|---|
| Brasil | LDB (organização), DCNs, EducaDados, SAEB, SINAES, identificadores INEP, leiaute do Censo campo a campo, currículos estaduais |
| Estados Unidos | Edu-API, CCSS, NGSS |
| União Europeia | ELM, EQF, DigComp, DigCompEdu, LifeComp, GreenComp, Europass, ECTS, interoperabilidade do ensino superior |
| Reino Unido | CBDS, DfE Data Standards, School Census, quatro currículos, UK GDPR |
| China | JY/T 0633–0635-2022, Smart Education Platform, GB/T, PIPL, Data Security Law |
| Internacional | ISCED 2011, ISCED-F 2013, ISO 21001, ISO 29993 |
