# Europass e European Digital Credentials for Learning (EDC)

```yaml
id: eu-edc-europass
name: Europass / European Digital Credentials for Learning
acronym: EDC (antes EDCI, European Digital Credentials Infrastructure)
jurisdiction: União Europeia / EEE
issuing_organization: Comissão Europeia (DG EMPL)
reference_type: framework de política (Europass) + infraestrutura e formato de credencial (EDC)
domain: [D3, D5, D8]
official_url: https://europass.europa.eu/en/stakeholders/european-digital-credentials
repository_url: not_found (ferramentas open source citadas pela página, URL não registrada)
version: unknown (formato segue ELM v3.3)
publication_date: unknown
last_updated: unknown
legal_status: Europass instituído por decisão do Parlamento e do Conselho (página linka CELEX:32018D0646); EDC é serviço/formato, não obrigação
mandatory_scope: voluntário para emissores; selo eletrônico eIDAS obrigatório para que a credencial seja EDC
education_levels: todos
geographic_scope: UE/EEE e países Europass
language: multilíngue
license: unknown
technical_formats: [JSON-LD conforme ELM, W3C VC, exportação PDF]
api_available: unknown
data_model_available: sim (ELM, ver eu-elm)
ontology_available: sim (ELM)
schemas_available: sim (perfil EDC em SHACL e JSON Schema)
implementation_examples: sim (repositório ELM, pasta Credentials/)
related_standards: [eu-elm, W3C VC, eIDAS, ESCO, DigComp, CEFR, EQF]
entities: EuropeanDigitalCredential, EuropeanDigitalPresentation, Claims ELM
relationships: credencial contém claims; emissor sela; titular guarda em carteira (ex.: "My Library" da conta Europass)
vocabularies: listas controladas Europass (credential type, verification status etc.)
core_relevance: média: C.CRD deve exportar para EDC
regional_adapter_relevance: alta para exportação no adaptador UE
limitations: não cobre educação básica de forma específica; dependência de selo qualificado eIDAS
open_questions: relação EDC × EUDI Wallet não verificada
sources: [S-UE-01, S-UE-06]
access_date: 2026-11-05
research_status: parcial (página institucional)
```

## Análise

Segundo a Europass, EDC são credenciais de aprendizagem "originalmente digitais" (diplomas, microcredenciais, certificados de participação), descritas pelo ELM, alinhadas ao W3C VC, que **devem** levar selo eletrônico eIDAS emitido por prestador de confiança; a verificação automática ocorre a cada visualização; podem referenciar ESCO, DigComp e CEFR; o titular as guarda numa carteira (ex.: "My Library") e compartilha por link ou PDF [S-UE-06]. Ferramentas: EDC Issuer e Viewer prontos e versões open source para integração [S-UE-06].

O modelo de VC já está analisado em `conhecimento/interoperabilidade/credentials/verifiable-credentials.md` (`iop.cred.verifiable-credentials`); esta ficha acrescenta só o perfil europeu.

**Para o Core [I]:** C.CRD precisa de (a) referência à especificação (C.CMP/qualificação), (b) emissor como C.ORG com identificador legal, (c) prova/selo fora do conteúdo, (d) apresentação seletiva. O EDC mostra que a credencial europeia é "claims ELM dentro de VC", logo o Core não precisa de um modelo próprio de prova, só de um exportador.
