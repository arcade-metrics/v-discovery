# Ficha: Idioma — BCP 47 e ISO 639

```yaml
id: int.language-tags
name: BCP 47 Tags for Identifying Languages (RFC 5646) e Matching of Language Tags (RFC 4647); ISO 639 Code for individual languages and language groups
acronym: BCP 47 / ISO 639
jurisdiction: internacional (IETF; ISO)
issuing_organization: IETF (BCP 47); IANA (Language Subtag Registry); ISO/TC 37 e ISO 639 Maintenance Agency
reference_type: padrão da Internet (BCP) + norma técnica
domain: [D3, D7, D8]
official_url: https://www.rfc-editor.org/info/bcp47 ; https://www.iana.org/assignments/language-subtag-registry ; https://www.iso.org/standard/74575.html
repository_url: registro IANA (texto)
version: BCP 47 = RFC 5646 (set. 2009) + RFC 4647 (set. 2006) [N32]; ISO 639:2023 (2ª ed., 2023-11-08), que consolidou e substituiu ISO 639-1, -2, -3, -4 e -5 [N30, secundária]
publication_date: ver version
last_updated: registro IANA atualizado continuamente
legal_status: voluntário
mandatory_scope: nenhum
education_levels: não se aplica
geographic_scope: global
language: en
license: RFC e registro IANA livres; ISO 639 paga (listas de códigos públicas pela agência de manutenção)
technical_formats: texto (registro)
api_available: não
data_model_available: gramática ABNF de etiquetas (RFC 5646)
ontology_available: not_found
schemas_available: não
implementation_examples: HTML `lang`, JSON-LD `@language`, CLDR
related_standards: [int.iso-3166 (subtag de região), ISO 15924 (subtag de escrita)]
entities: [etiqueta de idioma, subtag (idioma, escrita, região, variante)]
relationships: etiqueta = idioma[-escrita][-região][-variante]
vocabularies: Language Subtag Registry (IANA)
core_relevance: alta — idioma de conteúdo, de interface e de comunicação com família; línguas de sinais como idioma de instrução
regional_adapter_relevance: média
limitations: ISO 639:2023 reorganizou a série em "sets"; documentos antigos citam 639-1/-2/-3 — usar BCP 47 isola o Core dessa mudança
open_questions: [QI-11]
sources: [N30, N32]
access_date: 2026-11-05
research_status: status verificado (BCP 47 em fonte oficial; ISO 639:2023 em fonte secundária)
```

## O que o Core adota (proposta)

- Todo campo de idioma é **etiqueta BCP 47**, não código ISO 639 solto: `pt-BR`, `en-US`, `en-GB`, `de-DE`, `pt-PT`, `zh-Hans-CN`.
- Línguas de sinais são idiomas com subtag própria (ex.: Libras `bzs`, ASL `ase`, BSL `bfi`, língua de sinais chinesa `csl`) [I: conferir cada subtag no registro IANA]. Isso permite registrar "idioma de instrução = Libras" em C.PER/C.SUP e "conteúdo disponível em Libras" em C.ACT sem lista paralela.
- Casamento de preferência (aluno pede `pt`, conteúdo existe em `pt-BR`) segue RFC 4647 (*lookup*).
