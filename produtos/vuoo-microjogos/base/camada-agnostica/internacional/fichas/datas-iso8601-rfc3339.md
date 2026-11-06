# Ficha: Datas e horas — ISO 8601, RFC 3339 e RFC 9557

> Uso em eventos já analisado em `conhecimento/dados-pesquisa-e-eventos/quality/clocks-and-ordering.md` (`dat.qual.clocks-and-ordering`) e `.../events/event-model.md` (`dat.ev.event-model`). Não repetir; aqui só a escolha de perfil para o Core.

```yaml
id: int.datetime
name: ISO 8601 Date and time — Representations for information interchange; RFC 3339 Date and Time on the Internet: Timestamps; RFC 9557 Timestamps with Additional Information
acronym: ISO 8601 / RFC 3339 / RFC 9557
jurisdiction: internacional (ISO; IETF)
issuing_organization: ISO/TC 154; IETF
reference_type: norma técnica (ISO, paga) + padrões da Internet (IETF, abertos)
domain: [D8]
official_url: https://www.iso.org/iso-8601-date-and-time-format.html ; https://www.rfc-editor.org/rfc/rfc3339 ; https://www.rfc-editor.org/info/rfc9557
repository_url: não se aplica
version: ISO 8601-1:2019 e ISO 8601-2:2019 [I: edições conhecidas, não verificadas nesta sessão; iso.org 403]; RFC 3339 (2002); RFC 9557 (2024, Proposed Standard, atualiza RFC 3339) [N31b]
publication_date: ver version
last_updated: RFC 9557 (2024)
legal_status: voluntário
mandatory_scope: nenhum
education_levels: não se aplica
geographic_scope: global
language: en
license: ISO paga; RFCs livres
technical_formats: texto
api_available: não se aplica
data_model_available: gramática ABNF (RFC 3339 §5.6)
ontology_available: xsd:date / xsd:dateTime (XML Schema) para RDF [I]
schemas_available: JSON Schema `format: date-time`, `date`, `duration` remetem à RFC 3339 [I: conferir no vocabulário de formato da 2020-12]
implementation_examples: universais
related_standards: [int.json-schema, IANA Time Zone Database]
entities: [instante, data civil, duração, intervalo, fuso]
relationships: —
vocabularies: nomes de fuso IANA (America/Sao_Paulo)
core_relevance: alta
regional_adapter_relevance: média (calendário letivo local)
limitations: RFC 3339 não guarda fuso civil, só offset; RFC 9557 resolve com sufixo entre colchetes; ISO 8601 integral é ampla demais para validação
open_questions: [QI-10]
sources: [N31, N31b]
access_date: 2026-11-05
research_status: status RFC verificado; edições ISO não verificadas
```

## O que o Core adota (proposta)

| Uso | Forma |
|---|---|
| Instante (evento, auditoria) | RFC 3339 com `Z` ou offset; persistir em UTC |
| Agenda escolar (aula às 8h locais) | data + hora local + fuso IANA; serialização RFC 9557 quando trafegar como instante |
| Data civil (nascimento, vigência de matrícula, ano letivo) | `YYYY-MM-DD`, sem hora nem fuso |
| Duração | ISO 8601 `PnDTnHnM` |
| Período | par início/fim explícito (C.SES), não string de intervalo ISO [I: facilita consulta] |
