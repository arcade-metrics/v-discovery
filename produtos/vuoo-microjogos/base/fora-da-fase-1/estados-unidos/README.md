# Estados Unidos — adaptador de referência

**Estado: standby (referência).** Documentado o suficiente para mostrar que um adaptador EUA cabe sem mudar o Core, sem detalhar campo a campo ([_convencoes.md §1](../../_convencoes.md)). Pesquisa de 2026-11-05; fontes em [evidencias.md](evidencias.md). Parte §3.5 do [briefing](../../padroes-README.md).

## Escopo

Padrões de dados (Ed-Fi, CEDS, OneRoster, Edu-API), currículo (CASE, CCSS, NGSS), experiência e avaliação (Caliper, QTI, LTI, Common Cartridge, CLR/Open Badges) e privacidade (FERPA, COPPA, leis estaduais). Os padrões já analisados em `conhecimento/` são **apontados**, não reescritos; as fichas deles só acrescentam entidades, chaves e vocabulários para o crosswalk.

## Índice

| Arquivo | Conteúdo |
|---|---|
| [modelo-de-dados.md](modelo-de-dados.md) | entidades, identidades e cardinalidades (Ed-Fi 6.1, OneRoster 1.2, Edu-API 1.0, CASE, CCSS, NGSS) |
| [terminologia.md](terminologia.md) | conceitos, falsos amigos, enumerações com códigos |
| [cobertura.md](cobertura.md) | matriz referência × D1–D8 |
| [crosswalk-core.md](crosswalk-core.md) | conceito americano → C.xxx com tipo de equivalência |
| [questoes-abertas.md](questoes-abertas.md) | verificações pendentes e candidatos a entidade do Core |
| [evidencias.md](evidencias.md) | fontes, versões, data de acesso |

**Fichas** (`fichas/`):

| Ficha | Tipo | Situação |
|---|---|---|
| [ed-fi](fichas/ed-fi.md) | padrão de dados | aponta `iop.ros.ed-fi` + chaves verificadas nos modelos v6.1.0 |
| [ceds](fichas/ceds.md) | vocabulário | aponta `iop.ros.ceds` + versão 14 |
| [oneroster](fichas/oneroster.md) | padrão de intercâmbio | aponta `iop.ros.oneroster` + enums e papéis |
| [edu-api](fichas/edu-api.md) | padrão de intercâmbio (ensino superior) | **nova**, completa |
| [case](fichas/case.md) | intercâmbio de competências | aponta `iop.comp.case` |
| [caliper](fichas/caliper.md) | eventos | aponta `iop.lr.caliper` |
| [qti](fichas/qti.md) | avaliação | aponta `iop.asmt.qti` |
| [clr-open-badges](fichas/clr-open-badges.md) | credenciais | aponta `iop.cred.*` |
| [lti](fichas/lti.md) | integração de ferramentas | aponta `iop.tool.lti-*` |
| [common-cartridge](fichas/common-cartridge.md) | pacote de conteúdo | aponta `iop.tool.common-cartridge` |
| [ccss](fichas/ccss.md) | framework curricular | **nova**, completa |
| [ngss](fichas/ngss.md) | framework curricular | **nova**, completa |
| [ferpa](fichas/ferpa.md) | lei federal | **nova**, completa (não havia cobertura em `conhecimento/`) |
| [coppa](fichas/coppa.md) | regulamento federal | aponta `psg.legal.gdpr-k-and-coppa` |
| [leis-estaduais](fichas/leis-estaduais.md) | variação estadual | ficha curta |

## Resumo em 10 linhas

1. Não há padrão de dados educacional obrigatório federal; a obrigação de formato vem da especificação de coleta de cada estado (ex.: Texas TEDS, baseado no Ed-Fi).
2. Ed-Fi 6.1 (Apache-2.0) é o modelo mais amplo do K-12; associações têm data inicial na própria identidade.
3. Ed-Fi trata vocabulários como dados (descriptors com namespace do governante e mapeamento entre namespaces).
4. OneRoster 1.2 é o mínimo de mercado para apps: Org, AcademicSession hierárquica, Course/Class, Enrollment, papéis por organização com vigência.
5. Edu-API 1.0 (Final) leva o mesmo desenho ao ensino superior e separa Affiliation (pessoa↔org) de Enrollment (pessoa↔oferta).
6. Os três padrões distinguem catálogo (Course), oferta num período e instância com pessoas (Section/Class); o Core provisório não distingue o catálogo.
7. CASE 1.1 é o transporte de currículo; CCSS tem identificação tripla (pontos, URI, GUID); NGSS é multidimensional e sem formato legível por máquina oficial localizado.
8. FERPA impõe ao modelo: classificação de atributos (directory information), opt-out, registro de divulgações, transferência de direitos aos 18 anos e base "school official".
9. COPPA e as leis estaduais (SOPIPA e similares) impõem finalidade, proibição de perfilamento e publicidade, retenção e exclusão por contrato.
10. Conclusão provisória: um adaptador EUA cabe no Core com quatro acréscimos genéricos (atribuição de papel com vigência, unidade de catálogo, mapeamento de códigos, classificação/registro de divulgação), nenhum específico dos EUA.

## O que um adaptador EUA exigiria

**Do adaptador (local, sem tocar no Core)** [I]:
- Importadores Ed-Fi (API REST JSON, por estado, com extensões e descritores estaduais), OneRoster 1.2 (REST e CSV) e, se houver ensino superior, Edu-API; LTI 1.3 para lançamento; CASE para padrões.
- Tabelas C.VOC: OrgType/subclasses Ed-Fi → `kind`; GradeLevel (PK, K, 1–12) → séries; SessionType; RoleEnum/ClassroomPosition/StaffClassification → papéis; Program (serviços) → C.SUP/C.ENR.
- Conversão de identidade: chaves naturais Ed-Fi (com datas) → identificador substituto + vigência; `sourcedId`, StudentUniqueId, `sub` LTI → C.IDN com `scheme`.
- Regras FERPA/COPPA/estado: categorias de directory information por organização, opt-out, transferência de direitos aos 18, consentimento escolar só para fim educacional, retenção e exclusão por contrato.

**Do Core (genérico, útil também ao Brasil)** — candidatos registrados em [questoes-abertas.md](questoes-abertas.md):
- Atribuição de papel como entidade com organização/oferta e vigência (Q19).
- Unidade de catálogo distinta de componente e de oferta (Q18).
- Mapeamento de códigos entre vocabulários (Q22) e composição tipada entre competências (Q26).
- Classificação de sensibilidade por atributo, registro de divulgação, acordo de dados e política de retenção (Q14, Q16).
- Possivelmente frequência (Q25) e rubrica (Q12).
