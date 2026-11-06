# Internacional — padrões transversais que sustentam o Core

Parte §4 do [briefing](../../padroes-README.md). Estado: **transversal, alimenta o Core**. Pesquisa feita em 2026-11-05. Convenções em [../_convencoes.md](../../_convencoes.md); regra "cada fato tem um dono": padrões já analisados em `conhecimento/` têm aqui só ficha curta com o caminho e o que falta para o Core.

## Escopo

Padrões sem vínculo com uma jurisdição que o Core pode adotar como classificação, formato, modelo ou requisito:
1. classificações educacionais da UNESCO (ISCED 2011, ISCED-F 2013) e os **mapeamentos oficiais do UIS** para Brasil, EUA, Portugal e Alemanha (UE), Reino Unido e China;
2. normas de gestão educacional (ISO 21001, ISO 29993);
3. padrões de base para datas, idiomas, países, identificadores, URIs e contratos;
4. competências e metadados (IEEE 1484.20.x, IEEE 2881, ISO/IEC 19788, LOM);
5. acessibilidade e credenciais (WCAG, UDL, ISO/IEC 24751, VC/OB; só status e o que o Core representa).

Fora do escopo: QTI, xAPI/Caliper, CASE/CTDL/ESCO (estão em `conhecimento/` e nas pastas regionais).

## Índice

| Arquivo | Conteúdo |
|---|---|
| [mapeamentos-isced.md](mapeamentos-isced.md) | etapa nacional → ISCED-P/A, idade teórica e duração, 6 países, com aba e linha da planilha |
| [terminologia.md](terminologia.md) | níveis e códigos ISCED-P/A, dimensões, ISCED-F 2013 completo (11/29/80), formatos canônicos de base |
| [crosswalk-core.md](crosswalk-core.md) | padrão → C.xxx, com tipo de equivalência e papel |
| [cobertura.md](cobertura.md) | matriz referência × D1–D8 |
| [questoes-abertas.md](questoes-abertas.md) | QI-01 a QI-21, incluindo 3 candidatos a entidade do Core |
| [evidencias.md](evidencias.md) | fontes N01–N33 com tipo e versão |
| `fichas/` | ver tabela abaixo |

| Ficha | Id | Tipo |
|---|---|---|
| [isced-2011](fichas/isced-2011.md) | int.isced-2011 | completa |
| [isced-f-2013](fichas/isced-f-2013.md) | int.isced-f-2013 | completa |
| [isced-mappings-uis](fichas/isced-mappings-uis.md) | int.isced-mappings | completa |
| [iso-21001](fichas/iso-21001.md) | int.iso-21001 | parcial (texto pago) |
| [iso-29993](fichas/iso-29993.md) | int.iso-29993 | só metadados |
| [datas-iso8601-rfc3339](fichas/datas-iso8601-rfc3339.md) | int.datetime | completa |
| [idioma-bcp47-iso639](fichas/idioma-bcp47-iso639.md) | int.language-tags | completa |
| [iso-3166](fichas/iso-3166.md) | int.iso-3166 | não verificada na fonte (403) |
| [uuid-rfc9562](fichas/uuid-rfc9562.md) | int.uuid | completa |
| [uris-persistentes](fichas/uris-persistentes.md) | int.cool-uris | completa |
| [json-schema-2020-12](fichas/json-schema-2020-12.md) | int.json-schema | completa |
| [openapi](fichas/openapi.md) | int.openapi | completa |
| [w3c-grafo-json-ld](fichas/w3c-grafo-json-ld.md) | int.w3c-semantic-stack | curta → `kg.std.*` |
| [ieee-1484-20-competencias](fichas/ieee-1484-20-competencias.md) | int.ieee-1484-20 | só metadados oficiais |
| [ieee-2881-learning-metadata](fichas/ieee-2881-learning-metadata.md) | int.ieee-2881 | só metadados oficiais |
| [iso-iec-19788-mlr](fichas/iso-iec-19788-mlr.md) | int.iso-iec-19788 | curta |
| [ieee-lom](fichas/ieee-lom.md) | int.ieee-lom | curta → `iop.md.ieee-lom` |
| [credenciais-vc-ob](fichas/credenciais-vc-ob.md) | int.credentials | curta → `iop.cred.*` |
| [acessibilidade-wcag-udl-afa](fichas/acessibilidade-wcag-udl-afa.md) | int.accessibility-cross | curta → `acs.std.*`, `acs.udl.*` |
| [cif-icf](fichas/cif-icf.md) | int.icf | curta → `iop.health.cif` |

## Resumo em 10 linhas

1. O ISCED 2011 é o único pivô internacional de **nível**; classifica programas, não séries, e está em revisão desde 2023 (ISCED-F será revisto de forma ampla).
2. Os mapeamentos do UIS para os seis países foram lidos célula a célula; anos de referência vão de 2012/2013 (Brasil) a 2023 (China).
3. Nos seis, primária = 100, secundário inferior = 244, superior geral = 344; o que muda é idade, duração e onde a fronteira cai (Portugal e Brasil têm etapas que cruzam ISCED 1 e 2).
4. Educação especial **não é nível** em nenhum mapeamento: aparece transversal (EUA) ou embutida nos níveis regulares (Alemanha).
5. O ISCED-F não serve para componentes curriculares da educação básica.
6. A ISO 21001 já está na **2ª edição (2025)**; é lista de requisitos (dados do aprendiz, rastreabilidade, necessidades especiais, satisfação), não modelo de dados. ISO 29993 é para educação não formal.
7. Base técnica proposta: RFC 3339/9557, BCP 47, ISO 3166, UUIDv7, URIs persistentes, JSON Schema 2020-12, OpenAPI 3.1, JSON-LD 1.1.
8. IEEE 1484.20.3-2022 e 1484.20.2-2022 estão ativos; P2881 virou **IEEE 2881-2025**; textos pagos, classes não verificadas.
9. VC 2.0 é Recommendation (2025-05-15) e Open Badges 3.0 está alinhado; WCAG 2.2 vigente, WCAG 3 ainda Working Draft (set. 2026); UDL 3.0 vigente — tudo já documentado em `conhecimento/`.
10. Três candidatos a entidade do Core: ordinal de série neutro (QI-01), Feedback/Complaint (QI-09), AccessPreference (QI-19).

## O que o Core adota de cada padrão — tabela decisória (**PROPOSTA**, não decisão)

| Padrão | Decisão proposta | Força | Onde no Core | Condição / risco |
|---|---|---|---|---|
| ISCED 2011 (ISCED-P) | adotar como **classificação de nível** de C.PRG, por segmento, com `scheme = isced-2011-p` | adotar | C.PRG, C.VOC | revisão do ISCED; manter versão no `scheme` |
| ISCED 2011 (ISCED-A) | adotar para escolaridade obtida | adotar (opcional) | C.CRD, C.RES | |
| Mapeamentos UIS | importar como dado de adaptador, com proveniência (fonte, ano de referência) | adotar | C.CAS, C.PRV | BR de 2012/2013 (QI-07) |
| ISCED-F 2013 | só para programas técnicos/profissionais; nunca para C.SUB | opcional | C.PRG | revisão ampla em curso |
| ISO 21001:2025 | usar como **lista de verificação** de registros | referência | C.SUP, C.PLN, C.CNS, C.PRV, (C.FBK) | texto pago |
| ISO 29993:2017 | não adotar agora | não adotar | — | só se houver oferta não formal |
| RFC 3339 / ISO 8601 | instantes em RFC 3339 (UTC); datas civis `YYYY-MM-DD`; durações ISO 8601 | adotar | todas | |
| RFC 9557 | hora local + fuso IANA em agendas | adotar | C.SCH | suporte de bibliotecas [I] |
| BCP 47 (sobre ISO 639) | toda referência a idioma | adotar | C.PER, C.ACT, C.VOC | conferir subtags de línguas de sinais |
| ISO 3166-1/-2 | jurisdição de organização e de currículo | adotar | C.ORG, C.CFW | abaixo de subdivisão: C.IDN do adaptador |
| UUID (RFC 9562) | v7 como chave interna; nunca exportar ID de pessoa sem pseudonimizar | adotar | todas | QI-13 |
| URIs persistentes | para vocabulários, currículos, atividades publicadas | adotar | C.VOC, C.CFW, C.CMP, C.ACT | domínio a decidir |
| JSON Schema 2020-12 | linguagem única de contrato de payload | adotar | todas | |
| OpenAPI 3.1 | contrato de API; 3.2 em avaliação | adotar | API | |
| JSON-LD 1.1 + SKOS + PROV-O | exposição semântica; vocabulários e mapeamentos em SKOS; proveniência em PROV-O | adotar | C.VOC, C.CAS, C.PRV | 1.2 sem rascunho ainda |
| SHACL | validação de grafo publicado | opcional | — | |
| IEEE 1484.20.3 | referência para desenhar C.CMP; meta de exportação sem perda | referência | C.CMP | texto pago |
| IEEE 2881-2025 | referência; LRMI/schema.org segue como serialização prática | referência | C.ACT, C.SCH | texto pago |
| ISO/IEC 19788, IEEE LOM | não adotar; importar se necessário | não adotar | C.ACT | |
| VC 2.0 / OB 3.0 | formato de **exportação** de C.CRD | adotar (fase posterior) | C.CRD | não carregar C.SUP (QI-21) |
| WCAG 2.2 AA | alvo de produto + atributo de conformidade de C.ACT | adotar | C.ACT | WCAG 3 só monitorar |
| CAST UDL 3.0 | vocabulário de anotação de desenho de atividades | adotar | C.VOC, C.ACT | não é checklist |
| ISO/IEC 24751 (AfA) | modelo para preferências de acesso e descrição de recurso | adotar (modelo) | C.PRF (novo), C.ACT | QI-19 |
| CIF | vocabulário opcional de funcionalidade | opcional | C.SUP | nunca obrigatório |

## O que não foi verificado

- Texto oficial do ISCED 2011 e do ISCED-F 2013 (UIS 404, UNESDOC 403): códigos ISCED-P/A que não aparecem em nenhum mapeamento estão marcados **[conferir]** em `terminologia.md`; a tabela ISCED-F veio de reprodução secundária do Appendix 1.
- Páginas iso.org (403): ISO 21001:2025 foi lida pela prévia pública; ISO 29993, ISO 3166, ISO 8601 e ISO 639:2023 só por catálogos secundários ou conhecimento prévio.
- Conteúdo normativo da ISO 21001, IEEE 1484.20.3, IEEE 2881 e ISO/IEC 19788 (pagos).
- Subtags BCP 47 de línguas de sinais e lista vigente de subdivisões ISO 3166-2.
- Se existe mapeamento ISCED do Brasil mais novo que 2012/2013 em outro canal do UIS.
