---
id: iop.plano-ids
titulo: Plano de identificadores do domínio
tipo: mapa
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Plano de identificadores do domínio interoperabilidade

Lista de ids da primeira versão. Relações entre documentos usam estes ids, nunca caminhos de arquivo.

Diferenças em relação à estrutura sugerida no `00-brief.md`: as áreas `metadata/`, `competencies/`, `semantics/` e `fundamentos/` foram acrescentadas, porque a especificação de pesquisa cobre modelos de dados (LOM, Dublin Core, LRMI, CASE, CEDS, ESCO, CTDL) e não só protocolos de troca. `credentials/` absorveu Verifiable Credentials. RDF e OWL ficam em `grafo-conhecimento-educacional`; aqui só entra o uso de SKOS para alinhamento de vocabulários.

| Pasta | Id | Arquivo |
|---|---|---|
| fundamentos | iop.fund.niveis-de-interoperabilidade | fundamentos/niveis-de-interoperabilidade.md |
| fundamentos | iop.fund.dados-vs-protocolo | fundamentos/dados-vs-protocolo.md |
| fundamentos | iop.fund.identidade-e-contexto | fundamentos/identidade-e-contexto.md |
| fundamentos | iop.fund.mapeamento-e-proveniencia | fundamentos/mapeamento-e-proveniencia.md |
| fundamentos | iop.fund.conformidade-e-certificacao | fundamentos/conformidade-e-certificacao.md |
| fundamentos | iop.fund.privacidade-e-seguranca | fundamentos/privacidade-e-seguranca.md |
| learning-records | iop.lr.xapi | learning-records/xapi.md |
| learning-records | iop.lr.cmi5 | learning-records/cmi5.md |
| learning-records | iop.lr.caliper | learning-records/caliper.md |
| learning-records | iop.lr.comparison | learning-records/comparison.md |
| tool-integration | iop.tool.lti-core | tool-integration/lti-core.md |
| tool-integration | iop.tool.lti-advantage | tool-integration/lti-advantage.md |
| tool-integration | iop.tool.scorm | tool-integration/scorm.md |
| tool-integration | iop.tool.common-cartridge | tool-integration/common-cartridge.md |
| assessment | iop.asmt.qti | assessment/qti.md |
| rostering | iop.ros.oneroster | rostering/oneroster.md |
| rostering | iop.ros.ed-fi | rostering/ed-fi.md |
| rostering | iop.ros.sif | rostering/sif.md |
| rostering | iop.ros.ceds | rostering/ceds.md |
| rostering | iop.ros.comparison | rostering/comparison.md |
| metadata | iop.md.ieee-lom | metadata/ieee-lom.md |
| metadata | iop.md.dublin-core | metadata/dublin-core.md |
| metadata | iop.md.lrmi-schema-org | metadata/lrmi-schema-org.md |
| metadata | iop.md.comparison | metadata/comparison.md |
| competencies | iop.comp.case | competencies/case.md |
| competencies | iop.comp.ctdl | competencies/ctdl.md |
| competencies | iop.comp.esco | competencies/esco.md |
| credentials | iop.cred.verifiable-credentials | credentials/verifiable-credentials.md |
| credentials | iop.cred.open-badges | credentials/open-badges.md |
| credentials | iop.cred.clr | credentials/clr.md |
| semantics | iop.sem.vocabularios-e-skos | semantics/vocabularios-e-skos.md |
| semantics | iop.sem.interoperabilidade-semantica | semantics/interoperabilidade-semantica.md |
| health | iop.health.cif | health/cif.md |
| health | iop.health.fhir | health/fhir.md |
| brazil | iop.br.educacenso | brazil/educacenso.md |
| brazil | iop.br.lgpd | brazil/lgpd.md |
| (raiz) | iop.index | README.md |
| (raiz) | iop.glossario | glossario.md |
| (raiz) | iop.mapa | mapa-conceitos.md |
| (raiz) | iop.catalogo | catalogo-padroes.md |
| (raiz) | iop.matriz | matriz-comparativa.md |
| (raiz) | iop.exemplos | exemplos-payloads.md |
| (raiz) | iop.relatorio | relatorio.md |
| (raiz) | iop.plano-ids | _plano-ids.md |
| (raiz) | iop.brief | 00-brief.md |

## Adiado para versões futuras

- `iop.lr.xapi-profiles`: especificação de perfis xAPI (ADL Profile Spec). Precisa de leitura da especificação própria, não coberta nesta rodada.
- `iop.tool.lti-legacy`: LTI 1.1 e LTI 2.0, estado de depreciação. Não verificado em fonte primária.
- `iop.asmt.arp`: Assessment Results Profile do OneRoster, citado em `iop.ros.oneroster` mas sem documento próprio.
- `iop.br.sistemas-estaduais`: integrações estaduais brasileiras, sem documentação pública verificada nesta rodada.
