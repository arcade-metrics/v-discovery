# Questões abertas — Estados Unidos

Ambiguidades, lacunas de verificação e **candidatos a entidade do Core** (conforme [_convencoes.md §4](../../_convencoes.md)).

## 1. Verificação pendente

| # | Questão | Por que importa | Próximo passo |
|---|---|---|---|
| Q01 | Lista exata de tipos de extensão suportados pelo Ed-Fi Extension Framework (nova entidade, novo descritor, novo atributo em entidade existente, nova associação?) | define o padrão de extensão do Core por analogia | ler https://docs.ed-fi.org/reference/data-exchange/extensions-framework/ (URL alternativa deu 404) |
| Q02 | Ed-Fi v6.2.0: o README do repositório exibe 6.2.0, mas a página de releases mostra 6.1.0 como "Latest" | versão de referência | conferir tags e docs.ed-fi.org |
| Q03 | Modelo de IEP (Early Access, DS 6.1) | alvo de C.PLN e C.SUP | ler `SpecialEducationDataModel.mmd` e Data Handbook 6.1 |
| Q04 | Como a API Ed-Fi restringe acesso a atributos sensíveis (perfis, claim sets) | analogia com escopo de privacidade | ler documentação do ODS/API |
| Q05 | Atributos de LineItem/Result/ScoreScale do OneRoster Gradebook 1.2 | crosswalk de D5 | ler Gradebook Information Model |
| Q06 | Lista de domínios do CEDS 14 e serialização da CEDS Ontology | uso como camada semântica | abrir `CEDS-V14.0.0.0.xlsx` / repositório da ontologia |
| Q07 | Enumerações completas do Edu-API (RoleTypeEnum, EnrollmentStatusEnum…) e data do Final | crosswalk de papéis/estados de matrícula | ler §enumerações do documento (offset > 400 000 caracteres) |
| Q08 | Quais estados publicam seus padrões oficialmente em CASE (e se CCSS/NGSS têm framework "oficial" no CASE Network 2) | importação de currículo no adaptador | consultar CASE Network 2 |
| Q09 | Propriedades `group`, `membership`, `session` do Caliper Event (citadas de memória) | crosswalk C.EVT → C.OFR/C.ENR | reler Caliper 1.2 §2.1 |
| Q10 | Existe publicação legível por máquina oficial do NGSS? E o XML do CCSS segue qual versão do CEDS? | importação automatizada | contatar/ler WestEd e corestandards.org |
| Q11 | Autoridade do domínio thecorestandards.org (a página diz não ser afiliada à NGA/CCSSO) vs. corestandards.org | qual URI usar como C.IDN canônico | verificar corestandards.org e a NGA |
| Q13 | Contagem atual de estados que adotaram o NGSS (só fontes secundárias e datadas) | escopo do adaptador | mapa de adoção no site oficial |
| Q15 | Estado do *negotiated rulemaking* de FERPA (set/2026, fonte secundária) e da regra escolar da COPPA | regras podem mudar a base legal de fornecedores | Federal Register / reginfo.gov |
| Q23 | Texto oficial e emenda de 2024 do SOPIPA; levantamento das leis de outros estados | política de dados por estado | leginfo.legislature.ca.gov; Student Privacy Compass por estado |
| Q24 | Section 504 / ADA e IDEA como fontes de dados de inclusão (não pesquisadas) | D7 | ficha futura |

## 2. Candidatos a entidade (ou atributo) do Core

| # | Candidato | Evidência americana | Proposta [I] |
|---|---|---|---|
| Q12 | **Rubric / CriterionLevel** | CLR ResultDescription, RubricCriterionLevel; CASE CFRubric (NV) | entidade de rubrica ligada a C.ASM e C.CMP |
| Q14 | **DataClassification + DisclosureRecord** | FERPA directory information, opt-out, §99.32; Edu-API `core.readonly.privacy` | sensibilidade por atributo; preferência de opt-out por pessoa; log de divulgação com destinatário, finalidade e base legal |
| Q16 | **DataAgreement / RetentionPolicy** | COPPA retenção escrita; SOPIPA exclusão; contratos distritais | acordo por C.ORG contratante com finalidades e prazos |
| Q17 | **InstructionalCalendar (dias letivos)** | Ed-Fi Calendar/CalendarDate | pode ser C.SES + C.SCH; decidir se dia letivo é entidade |
| Q18 | **CourseDefinition (unidade de catálogo)** distinta de C.SUB | Ed-Fi Course, OneRoster Course, Edu-API CourseTemplate | três níveis: catálogo → oferta (C.OFR) → instância/seção; ou C.OFR com `level` |
| Q19 | **RoleAssignment** (pessoa × papel × organização/oferta × vigência) | OneRoster Role; Edu-API Affiliation; Ed-Fi StaffEducationOrganizationAssignmentAssociation | C.LRN/C.STF/C.GRD como atribuições, não como subtipos de pessoa |
| Q20 | **AcademicRecord / Transcript** | Ed-Fi StudentAcademicRecord, CourseTranscript, ReportCard | consolidado oficial por período |
| Q21 | **Path / Pathway** | Ed-Fi Path, PathPhase, PathMilestone | avaliar junto com percursos adaptativos de D6 |
| Q22 | **CodeMapping** (equivalência entre códigos de vocabulários) | Ed-Fi descriptor mappings | parte de C.VOC ou entidade própria |
| Q25 | **Attendance** | Ed-Fi StudentSchool/Section AttendanceEvent | provavelmente necessário também no Brasil [I] |
| Q26 | **Composição tipada entre competências** | NGSS PE = SEP + DCI + CCC | novo tipo em C.CAS (`composedOf` com papel/dimensão) |

## 3. Conflitos entre padrões

- **Data na identidade do vínculo**: Ed-Fi põe BeginDate/EntryDate na chave (história = linhas); OneRoster e Edu-API usam `sourcedId` com begin/end como atributos. O Core precisa escolher identificador substituto + vigência como atributo, e o adaptador Ed-Fi converte [I].
- **"Enrollment"** significa pessoa×escola no Ed-Fi e pessoa×class/oferta no OneRoster/Edu-API.
- **Pessoa unificada**: Edu-API e OneRoster têm Person/User único com papéis; Ed-Fi recusa Person unificada (só elo PersonId+SourceSystem).
