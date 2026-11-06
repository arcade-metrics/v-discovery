# Terminologia — Estados Unidos

Conceitos e vocabulários controlados americanos relevantes para o Core. Traduções são de trabalho [I]; a coluna "falso amigo" sinaliza termos que **não** equivalem ao homônimo brasileiro. Fontes em [evidencias.md](evidencias.md).

## 1. Conceitos

| Termo (EUA) | Definição de trabalho | Falso amigo / cuidado | Fonte |
|---|---|---|---|
| SEA (State Education Agency) | secretaria estadual de educação | não é "rede"; é o órgão regulador e coletor | E03 |
| LEA (Local Education Agency) | distrito escolar; pode ter LEA-pai (ex.: charter dentro de distrito) | aproxima-se de "rede municipal", mas é ente com orçamento próprio | E03 |
| ESC / RESA (Education Service Center) | agência regional de serviços | sem equivalente direto no Brasil (próximo de diretoria regional) | E03 |
| School | escola | — | E03 |
| District (OneRoster OrgType) | equivalente a LEA | — | E11 |
| Course | unidade de catálogo (ex.: "Algebra I") com código, créditos e séries | **não** é "curso" brasileiro (curso técnico/etapa); está entre "componente curricular" e "disciplina de uma série" | E03, E11 |
| CourseOffering | curso oferecido numa escola numa sessão | — | E03 |
| Section | instância de oferta com professor, alunos, sala e horário | **não** é "seção"; no Brasil a coisa mais próxima é "turma × componente" | E03 |
| Class (OneRoster) | instância de ensino de um Course; `homeroom` ou `scheduled` | homeroom ≈ "turma" brasileira; scheduled ≈ oferta do componente | E11 |
| Homeroom | grupo de referência administrativo | ≈ turma | E11 |
| Session / Term | período letivo da escola (semestre, trimestre) | — | E03, E11 |
| GradingPeriod | período de lançamento de notas | ≈ bimestre/trimestre de avaliação | E03, E11 |
| SchoolYear | ano letivo identificado pelo ano de término (ex.: 2026 para 2025–26) [I: convenção Ed-Fi, não relida] | o Brasil usa o ano civil | — |
| Grade level | série/ano (K, 1–12; PK) | "grade" também significa "nota" | E03 |
| Grade (entidade) | nota de um aluno numa section num grading period | — | E03 |
| Program (Ed-Fi) | programa de serviço (educação especial, Title I, ELL…) | **não** é etapa/modalidade; o alvo é C.SUP/C.ENR, não C.PRG | E03 |
| Contact (Ed-Fi; antes Parent) | pessoa de contato do aluno; LegalGuardian é atributo da associação | — | E03, E08 |
| Guardian / Parent / Relative (OneRoster RoleEnum) | papéis de família | — | E11 |
| Agent (Edu-API) | relação de representação (parent, guardian) | — | E13 |
| Affiliation (Edu-API) | vínculo pessoa↔organização com papel e vigência | ≈ "vínculo" / "lotação" | E13 |
| Enrollment | OneRoster/Edu-API: pessoa↔class/oferta; Ed-Fi usa "enrollment" para StudentSchoolAssociation | ambíguo entre padrões | E03, E11, E13 |
| Descriptor | valor controlado com namespace do governante | ≈ código de tabela auxiliar | E04 |
| IEP (Individualized Education Program) | plano educacional individualizado sob a IDEA | ≈ PEI; regime legal diferente | E02 |
| Accommodation | adaptação (ex.: em avaliação) | ≈ "recurso de acessibilidade/adaptação" | E03 |
| Education record (FERPA) | registro mantido pela instituição diretamente ligado ao aluno | — | E27 |
| Directory information (FERPA) | dado divulgável sem consentimento, salvo opt-out | sem equivalente na LGPD | E27 |
| Eligible student (FERPA) | aluno ≥ 18 anos ou no ensino superior | — | E27 |
| School official / legitimate educational interest | base de acesso sem consentimento | ≈ "execução de políticas públicas"/ "contrato" na LGPD (aproximado) [I] | E27 |
| Operator (SOPIPA) | fornecedor de serviço online K-12 | — | E30 |
| Performance expectation (NGSS) | objetivo avaliável composto de três dimensões | ≈ "habilidade" BNCC, mas multidimensional | E25 |
| Cluster (CCSS Math) | agrupamento de padrões dentro de um domínio | — | E19 |

## 2. Vocabulários controlados (com códigos)

### 2.1 OneRoster 1.2 [E11 §6.3]

| Enum | Códigos |
|---|---|
| OrgTypeEnum | `department`, `district`, `local`, `national`, `school`, `state` |
| SessionTypeEnum | `gradingPeriod`, `schoolYear`, `semester`, `term` |
| ClassTypeEnum | `homeroom`, `scheduled` |
| RoleEnum | `aide`, `counselor`, `districtAdministrator`, `guardian`, `parent`, `principal`, `proctor`, `relative`, `siteAdministrator`, `student`, `systemAdministrator`, `teacher` |
| RoleTypeEnum | `primary`, `secondary` |
| EnrolRoleEnum | `administrator`, `proctor`, `student`, `teacher` |
| GenderEnum | `female`, `male`, `other`, `unspecified` |
| BaseStatusEnum | `active`, `tobedeleted` |

Extensão: `ext:<termo>` em Org/Session/Class/Role/Gender [E11 §8.1].

### 2.2 Ed-Fi descriptors (amostra de nomes; valores não transcritos)

Namespace padrão `uri://ed-fi.org/<Descriptor>#<CodeValue>` [I: forma usual; E04 confirma o namespace `uri://ed-fi.org`]. Descritores nas entidades lidas [E03]: EducationOrganizationCategory, SchoolType, CharterStatus, GradeLevel, EntryGradeLevel, EntryType, ExitWithdrawType, Term, GradingPeriod, AcademicSubject, ClassroomPosition, StaffClassification, EmploymentStatus, Relation, Sex, Race, LimitedEnglishProficiency, EconomicDisadvantage, Disability (common), Accommodation, AssessmentCategory, ProgramType, SectionType, EducationalEnvironment, MediumOfInstruction, StudentIdentificationSystem, SourceSystem. Os arquivos XML de valores estão em https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Standard/tree/main/Descriptors [E01] (não inspecionados).

### 2.3 Edu-API (valores vistos em exemplos; listas incompletas) [E13]

`role`: member, chair · `enrollmentStatus`: onLeave (e, pela comparação com OneRoster, registered, enrolled, deferred, on hold) · `offeringType`: collection, standard · `offeringFormat`: online · `synchronicity`: hybrid · `recordStatus`: active, deleted · `agentType`: parent, guardian · `learningObjectiveSet.source`: case, unknown.

### 2.4 NGSS — disciplinas e ideias centrais [E25]

| Código | Ideia central |
|---|---|
| PS1 | Matter and Its Interactions (PS1A–PS1C) |
| PS2 | Motion and Stability: Forces and Interactions (PS2A–PS2C) |
| PS3 | Energy (PS3A–PS3D) |
| PS4 | Waves and Their Applications in Technologies for Information Transfer (PS4A–PS4C) |
| LS1 | From Molecules to Organisms: Structures and Processes (LS1A–LS1D) |
| LS2 | Ecosystems: Interactions, Energy, and Dynamics (LS2A–LS2D) |
| LS3 | Heredity: Inheritance and Variation of Traits (LS3A–LS3B) |
| LS4 | Biological Evolution: Unity and Diversity (LS4A–LS4D) |
| ESS1 | Earth's Place in the Universe (ESS1A–ESS1C) |
| ESS2 | Earth's Systems (ESS2A–ESS2E) |
| ESS3 | Earth and Human Activity (ESS3A–ESS3D) |
| ETS | Engineering, Technology, and Applications of Science (código ETS não visto no trecho lido; domínio citado em E24) |

Prefixo de série: `K`, `1`–`5`, `MS`, `HS`.

### 2.5 CCSS — códigos de domínio

Exemplos verificados: `EE` (Matemática), `RL`, `RF` (ELA) [E19]. Lista completa não transcrita.
