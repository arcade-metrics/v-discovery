# Common Basic Data Set (CBDS), Inglaterra

```yaml
id: uk-eng-cbds
name: Common Basic Data Set
acronym: CBDS
jurisdiction: Inglaterra (alguns itens valem para Inglaterra e País de Gales, ex.: UPN)
issuing_organization: Department for Education (DfE), Data Development Team
reference_type: dicionário de dados + conjuntos de códigos (padrão técnico do governo para MIS escolares)
domain: [D1, D3, D5, D7, D8]
official_url: https://www.gov.uk/government/publications/common-basic-data-set-cbds-database
repository_url: n/a (planilha CBDS_VersionMay2026.xlsx)
version: "May 2026 (arquivo CBDS_VersionMay2026.xlsx, 776 KB)"
publication_date: 2013-10-14 (primeira publicação)
last_updated: 2026-05-11
legal_status: padrão técnico; obrigatório de fato porque as coletas estatutárias (School Census, CTF, Workforce Census) remetem a ele
mandatory_scope: fornecedores de MIS e escolas/LAs que enviam coletas ao DfE
education_levels: educação infantil (EY) a pós-16 escolar; serviços sociais da criança (CIN, SEN2)
geographic_scope: Inglaterra
language: inglês
license: unknown (gov.uk; [I] provavelmente Open Government Licence)
technical_formats: [XLSX; itens com tag XML usada nas especificações de coleta]
api_available: não
data_model_available: sim (dicionário plano de itens + módulos nas especificações)
ontology_available: não
schemas_available: indireto (cada especificação de coleta traz estrutura XML; CBDS traz tags)
implementation_examples: especificações de coleta (School Census 2026–27 v1.2, CTF 26)
related_standards: [uk-eng-school-census, uk-identificadores, SIF UK (coluna de mapeamento), ESCS/ISB]
entities: níveis (pupil, school…) e módulos; 837 itens de dados N00001…; code sets CSnnn
relationships: implícitas (níveis/módulos), não declaradas como chaves estrangeiras
vocabularies: code sets CS001…CS137+ (ex.: CS071 SEN type, CS096 SEN provision, CS086 NC year group)
core_relevance: alta para D1/D3/D7 (identificadores com dígito verificador, matrícula com dual registration, SEN como necessidade + provisão)
regional_adapter_relevance: muito alta (base do adaptador Inglaterra)
limitations: dicionário plano; relações e cardinalidades estão nas especificações de coleta, não no CBDS; coluna "Class" vazia
open_questions: licença formal; existência de versão legível por máquina além do XLSX
sources: [S-UK-01, S-UK-02]
access_date: 2026-11-05
research_status: verificado (planilha inspecionada)
```

## Análise técnica

**Estrutura da planilha** (lida em diretório temporário) [S-UK-02]: abas `Navigation`, `VersionHistory`, `Metadata`, `DataItems` (837 itens), `CodeSetRegister`, `CodeSets`, `Archived_DataItems`, `Archived_Codesets`. Colunas de `DataItems`: CBDS Identifier (`Nnnnnn`), Data Item Name, Description, Type and Format (ex.: `A(13)`, `CCYY-MM-DD`), Code set / Valid Values, Item Level Validation, XML Tag, Class, ESCS ISB Compliance, ESCS Data Model, **SIF Specification** (mapeamento para objetos SIF UK, ex.: `Learner Personal`, `LearnerSchoolEnrolment`, `LearnerSpecialNeeds`), notas de coleta, histórico, multiplicidade, RFC, datas e **uma coluna por coleta** (Autumn School Census 2025, CTF 22, SEN2 2025, EYC 2026…) marcando uso.

A página oficial descreve a organização por **níveis** (ex.: pupil, school), **módulos** (ex.: school characteristics) e **itens com code sets**; mudanças por "request for change" [S-UK-01].

**Itens de destaque** (identificador | nome | formato | code set):

| Item | Nome | Formato | Valores |
|---|---|---|---|
| N00001 | Unique Pupil Number (UPN) | A(13) | letra verificadora + 12 dígitos; temporário termina em letra |
| N00002 | Pupil's Former UPN | A(13) | |
| N00011 | ULN | 10 dígitos | dígito verificador mod 11 |
| N00017 | Pupil/child Enrolment status | A(1) | CS007 |
| N00022 / N00023 | Membro de SEN unit / resourced provision | booleano | |
| N00024 | Pupil SEN Type ranking | inteiro | 1 = principal |
| N00166 | Pupil SEN type code | A(4) | CS071 |
| N00209 | SEN Provision | A(1) | CS096 |
| N00673 | EHC Plan (indicação na admissão) | booleano | |
| N00715 / N00716 | Data / motivo de cessação do EHC plan | data / CS113 | |
| N00708 | SEN setting type | A(4) | CS110 |
| N00182 | Pupil's Actual National Curriculum Year Group | A(2) | CS086 |
| N00244 | Class Reference Name | A(30) | |
| N00267 / N00268 / N00296 | Class Type / Class Key Stage / Class Year Group | | CS036 / CS037 / CS086 |
| N00278 | Establishment URN | 6 dígitos | |
| N00279 | DfE Establishment Number | A(4) | 0000–9999 |
| N00216 | LA Number | A(3) | CS003 |
| N00530 | UKPRN | 8 dígitos | 10000000–99999999 |
| N00539 | Teacher Number (TRN) | 7 dígitos | |
| N00180 | Unique Candidate Identifier (UCI) | A(13) | |
| N00092 | Contact Relationship to pupil | A(3) | CS012 |
| N00049 | Contact Responsibility to Pupil (responsabilidade parental) | booleano | |
| N00157 / N00165 | Attendance Codes / marks por sessão | A(1) / A(999) | CS066 |

**Regras de validação** estão no próprio item: UPN com algoritmo de letra verificadora (pesos 2..13, módulo 23, tabela de letras sem I, O, S) e caracteres 2–4 = código de LA válido pós-abril de 1998 ou pseudo-LA galês; ULN com dígito verificador (soma ponderada 10..2, módulo 11, rejeita resto 0) [S-UK-02].

**Restrição de uso do identificador.** O UPN "is an identifier for use in the educational context during a child's school career only and subject to Data Protection restrictions" [S-UK-02]. Lição: C.IDN precisa de atributo de **finalidade/uso permitido**.

**Temporalidade/versionamento.** Itens têm Creation/Implementation/Changed/Cut Off Date; itens e code sets aposentados vão para abas `Archived_*`; códigos válidos só para histórico (ex.: CS096 `S`, `A`, `P` só em `<SENhistory>` do CTF) [S-UK-02].

**Operações CRUD, autenticação, API:** não se aplicam; a troca é por arquivo XML nas coletas (COLLECT) e CTF entre escolas [S-UK-03].

**Extensão:** só por RFC ao DfE.

### Lições para o Core [I]

1. **Matrícula com tipo de registro**: CS007 distingue registro único, principal e subsidiário (dual registration) e "Guest" (frequenta sem estar registrado). C.ENR precisa de `registration_kind`.
2. **SEN como dois eixos**: *provisão* (N/K/E: nenhuma, SEN Support, EHC plan) separada de *tipo de necessidade* (CS071) com **ranking** (principal/secundária). C.SUP precisa de ranking e C.PLN precisa ser referenciado pela provisão.
3. **Ano curricular ≠ idade**: N00182 é o ano em que o aluno é ensinado "regardless of their chronological age".
4. **Turma com ano e estágio próprios**: Class Year Group pode ser `M` (multisseriada); C.GRP precisa admitir múltiplos anos.
