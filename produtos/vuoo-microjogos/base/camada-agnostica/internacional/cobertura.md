# Cobertura — Internacional

Matriz referência × domínio (briefing §5). Legenda: **C** Completa, **P** Parcial, **I** Indireta, **A** Ausente, **NV** Não verificada. Sem nota de qualidade.

D1 Organização acadêmica · D2 Modelo de aprendizagem · D3 Modelo do aprendiz · D4 Currículo · D5 Avaliação · D6 Experiência de aprendizagem · D7 Inclusão e acessibilidade · D8 Interoperabilidade e governança

| Referência | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Nota |
|---|---|---|---|---|---|---|---|---|---|
| ISCED 2011 | P | A | I | A | A | A | A | P | níveis de programa e escolaridade obtida; não desce a série nem a oferta |
| ISCED-F 2013 | I | A | A | I | A | A | A | P | campos de formação; não é currículo |
| Mapeamentos UIS | P | A | A | A | A | A | I | P | D7 indireta: educação especial aparece como transversal (EUA, DE) |
| ISO 21001:2025 | P | I | I | I | P | I | P | P | requisitos de gestão; corpo NV (pago) |
| ISO 29993:2017 | I | NV | NV | NV | NV | NV | NV | NV | só metadados |
| ISO 8601 / RFC 3339 / RFC 9557 | I | A | A | A | A | A | A | C | formato de tempo |
| BCP 47 / ISO 639 | A | A | I | A | A | I | I | C | idioma; línguas de sinais |
| ISO 3166 | I | A | A | A | A | A | A | C | país e subdivisão |
| UUID (RFC 9562) | A | A | A | A | A | A | A | C | identificador |
| Cool URIs | A | A | A | A | A | A | A | P | nota não normativa |
| JSON Schema 2020-12 | A | A | A | A | A | A | A | C | contrato de payload |
| OpenAPI 3.1/3.2 | A | A | A | A | A | A | A | C | contrato de API |
| W3C RDF/OWL/SKOS/JSON-LD/SHACL/PROV-O | A | I | A | P | A | A | A | C | ver `kg.std.*` |
| IEEE 1484.20.3 / 20.2 | A | P | A | P | NV | A | A | P | modelo de competência; texto NV |
| IEEE 2881-2025 | A | A | A | A | A | P | NV | P | recurso × evento; texto NV |
| ISO/IEC 19788 | A | A | A | A | A | P | NV | P | só metadados |
| IEEE LOM | A | A | A | A | A | P | I | P | ver `iop.md.ieee-lom` |
| VC 2.0 / Open Badges 3.0 | A | A | P | I | I | A | A | C | ver `iop.cred.*` |
| WCAG 2.2 | A | A | A | A | A | P | C | I | conteúdo/interface; ver `acs.std.wcag` |
| CAST UDL 3.0 | A | P | I | I | I | C | C | A | framework de desenho; ver `acs.udl.*` |
| ISO/IEC 24751 (AfA) | A | A | P | A | A | P | C | P | preferências e descrição de recurso; ver `acs.std.accessforall-iso-24751` |
| CIF / ICF | A | A | P | A | A | A | P | P | funcionalidade; ver `iop.health.cif` |

Lacunas de domínio que nenhum padrão internacional transversal cobre bem [I]:
- **D1 granular** (série, turma, oferta, horário): só padrões regionais (Ed-Fi, OneRoster, Educacenso, CMDEB).
- **D4 curricular neutro**: não há taxonomia internacional de componentes curriculares da educação básica; o ISCED-F não serve (QI-06).
- **D5 avaliação**: nada transversal nesta lista; QTI (`iop.asmt.qti`) é o candidato, fora do escopo desta pasta.
