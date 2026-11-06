# Crosswalk — padrão internacional → entidade provisória do Core

Alvos de `_convencoes.md` §4. Tipo de equivalência: exata, aproximada, parcial, mais ampla, mais restrita, inexistente. "Papel" diz o que o padrão fornece ao Core: **classificação** (código de valor), **formato** (forma de serialização/identificação), **modelo** (estrutura de entidade), **requisito** (exigência a satisfazer). Todo o mapeamento é **proposta** [I].

## 1. Classificações educacionais

| Conceito do padrão | Alvo Core | Equivalência | Papel | Observação |
|---|---|---|---|---|
| ISCED 2011 education programme | C.PRG | aproximada | classificação | ISCED classifica programa; C.PRG também representa série/ano, que ISCED não tem |
| ISCED level (1º dígito) | C.PRG.iscedLevel → C.VOC | exata (como código) | classificação | `scheme = isced-2011-p` |
| ISCED-P 3 dígitos | C.PRG + C.VOC | exata | classificação | atribuído ao segmento (QI-02) |
| ISCED-A (escolaridade obtida) | C.CRD / C.RES | parcial | classificação | resultado, não programa (RU KS4) |
| Programme orientation (G/V) | atributo de C.PRG | exata | classificação | |
| Theoretical starting age / duration | atributos de C.PRG | exata | classificação | base do ordinal neutro (QI-01) |
| Compulsory education age span | atributo de jurisdiction (C.ORG raiz do adaptador) | parcial | classificação | sem alvo claro: candidato a "JurisdictionProfile" [I] |
| Mapeamento nacional (planilha UIS) | C.CAS + C.PRV | aproximada | modelo | associação programa-nacional → ISCED com fonte e ano |
| ISCED-F field | C.PRG.fieldOfEducation → C.VOC | exata (como código) | classificação | só profissional/técnico |
| ISCED-F field | C.SUB | **inexistente** | — | não usar (QI-06) |

## 2. Gestão e qualidade

| Conceito do padrão | Alvo Core | Equivalência | Papel | Observação |
|---|---|---|---|---|
| ISO 21001 educational organization | C.ORG | mais ampla | requisito | inclui provedores não escolares |
| ISO 21001 learner / other beneficiary | C.LRN / C.GRD | aproximada | requisito | |
| ISO 21001 interested parties (Anexo C) | C.PER + papéis | parcial | requisito | |
| ISO 21001 learner with special needs (5.1.3, 7.2.2, 8.1.3) | C.SUP, C.PLN | parcial | requisito | |
| ISO 21001 8.5.2 identification and traceability | C.IDN, C.PRV | aproximada | requisito | |
| ISO 21001 8.5.5 protection and transparency of learners' data | C.CNS | parcial | requisito | |
| ISO 21001 7.5 documented information | C.PRV | parcial | requisito | |
| ISO 21001 9.1.2 satisfaction of learners, beneficiaries, staff | — | **inexistente** | requisito | candidato C.FBK (QI-09) |
| ISO 21001 Anexo A early childhood | C.PRG (ISCED 0) | parcial | requisito | |
| ISO 29993 learning service | C.OFR | mais ampla | requisito | educação não formal |

## 3. Formatos de base

| Padrão | Alvo Core | Papel | Regra proposta |
|---|---|---|---|
| RFC 3339 date-time | todos os instantes (C.EVT, C.PRV, C.ENR) | formato | UTC + offset |
| RFC 9557 | C.SCH | formato | hora local + fuso IANA quando importa |
| ISO 8601 full-date | C.PER.birthDate, C.SES, C.ENR vigência | formato | `YYYY-MM-DD` |
| ISO 8601 duration | C.ACT duração estimada, C.SUP tempo estendido | formato | `PT…` |
| BCP 47 | C.PER (idiomas), C.ACT (idioma do conteúdo), C.VOC (rótulos multilíngues) | formato | etiqueta completa |
| ISO 3166-1/-2 | C.ORG.jurisdiction, C.CFW.jurisdiction | classificação | `BR`, `BR-SP` |
| UUID v7 (RFC 9562) | chave de toda entidade | formato | interna |
| URI HTTP persistente | C.VOC, C.CFW, C.CMP, C.ACT publicados | formato | nunca para C.PER/C.LRN |
| — (identificador externo) | C.IDN | modelo | `{scheme, value, issuer, validFrom, validTo}` |
| JSON Schema 2020-12 | contrato de cada entidade | formato | `$id` versionado |
| OpenAPI 3.1 | API do Core e adaptadores | formato | |
| JSON-LD 1.1 `@context` | exposição semântica de todas as entidades públicas | formato | contexto versionado |
| SKOS (Concept, ConceptScheme, *Match) | C.VOC, C.CAS | modelo | tipos de equivalência ↔ SKOS (QI-16) |
| PROV-O (Entity, Activity, Agent) | C.PRV | modelo | |
| SHACL | validação de grafo publicado | formato | |

## 4. Competências, recursos, credenciais

| Conceito do padrão | Alvo Core | Equivalência | Papel | Observação |
|---|---|---|---|---|
| IEEE 1484.20.3 competency definition | C.CMP | aproximada [NV] | modelo | texto não verificado |
| IEEE 1484.20.2 (prática para definir competências) | C.CMP (redação) | — | requisito | orientação editorial |
| IEEE 2881 Learning Resource | C.ACT | aproximada [NV] | modelo | |
| IEEE 2881 Learning Event | C.SCH / C.EVT | parcial [NV] | modelo | 2881 "evento" = instância presencial/virtual de recurso; C.EVT do Core é telemetria — não confundir [I] |
| IEEE LOM / ISO/IEC 19788 learning object/resource | C.ACT | aproximada | modelo | legado |
| VC 2.0 VerifiableCredential | C.CRD (exportação) | aproximada | formato | |
| OB 3.0 Achievement / AchievementCredential | C.CRD + C.CMP | aproximada | modelo | |

## 5. Acessibilidade e inclusão

| Conceito do padrão | Alvo Core | Equivalência | Papel | Observação |
|---|---|---|---|---|
| WCAG 2.2 conformance level (A/AA/AAA) | atributo de C.ACT | exata (como código) | classificação | |
| WCAG success criterion | C.VOC (`scheme = wcag-2.2`) | exata | classificação | para declarar exceções |
| UDL 3.0 principle / guideline / consideration | C.VOC (`scheme = cast-udl-3.0`), associado a C.ACT | exata (como código) | classificação | anotação de desenho |
| ISO/IEC 24751-2 personal needs and preferences | — | **inexistente** | modelo | candidato C.PRF (QI-19); hoje cairia em C.SUP, que é mais ampla |
| ISO/IEC 24751-3 digital resource description | atributos de C.ACT | parcial | modelo | |
| CIF component/code | C.SUP + C.VOC (`scheme = who-icf`) | parcial | classificação | opcional |
