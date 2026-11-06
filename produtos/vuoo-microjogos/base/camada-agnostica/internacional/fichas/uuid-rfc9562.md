# Ficha: UUID — RFC 9562

> Identidade de pessoas e mapeamento entre sistemas já analisados em `conhecimento/interoperabilidade/fundamentos/identidade-e-contexto.md` (`iop.fund.identidade-e-contexto`). Aqui só o formato do identificador interno.

```yaml
id: int.uuid
name: Universally Unique IDentifiers (UUIDs)
acronym: UUID (RFC 9562)
jurisdiction: internacional (IETF)
issuing_organization: IETF
reference_type: padrão da Internet (Standards Track)
domain: [D8]
official_url: https://www.rfc-editor.org/rfc/rfc9562.html
repository_url: não se aplica
version: RFC 9562
publication_date: 2024-05 [N24]
last_updated: 2024-05
legal_status: voluntário
mandatory_scope: nenhum
education_levels: não se aplica
geographic_scope: global
language: en
license: livre (IETF Trust)
technical_formats: 128 bits; texto hexadecimal 8-4-4-4-12; URN `urn:uuid:`
api_available: não se aplica
data_model_available: sim (layout de bits por versão)
ontology_available: não
schemas_available: JSON Schema `format: uuid` [I]
implementation_examples: universais
related_standards: [RFC 4122 (obsoleta por esta)]
entities: [UUID]
relationships: —
vocabularies: versões 1–8 (1 tempo gregoriano; 2 DCE; 3 nome/MD5; 4 aleatório; 5 nome/SHA-1; 6 tempo reordenado; 7 tempo Unix; 8 personalizado) [N24]
core_relevance: alta
regional_adapter_relevance: nenhuma
limitations: UUIDv7 expõe o instante de criação (ms) no próprio identificador [N24, §6]; isso é dado sobre o aluno quando o ID é de aluno [I]
open_questions: [QI-13]
sources: [N24]
access_date: 2026-11-05
research_status: verificado
```

## O que o Core adota (proposta)

- Chave interna de toda entidade: **UUIDv7** ("Implementations SHOULD utilize UUIDv7 instead of UUIDv1 and UUIDv6 if possible" [N24]); ordenação por tempo melhora localidade de índice.
- Para entidades de pessoa exportadas para fora (pesquisa, terceiros), avaliar UUIDv4 ou pseudônimo derivado, para não vazar data de cadastro (QI-13) [I].
- Identificadores externos (INEP, CPF, NCES, UPN, CASE GUID) nunca substituem a chave interna: entram em C.IDN `{scheme, value, issuer, validFrom}`.
- UUIDv5 (nome + namespace) é opção para IDs determinísticos de itens de vocabulário importados (ex.: código BNCC → UUID estável) [I].
