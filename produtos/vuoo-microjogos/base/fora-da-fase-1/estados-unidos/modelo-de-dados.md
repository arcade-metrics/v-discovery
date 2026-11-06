# Modelo de dados — Estados Unidos (nível standby)

Entidades principais dos padrões americanos, com identidade e cardinalidade, suficientes para o crosswalk. Não é transcrição campo a campo. Notação: **[I]** inferência; chaves marcadas como identidade ("I") nos modelos Mermaid oficiais do Ed-Fi v6.1.0 [E03]. Fontes em [evidencias.md](evidencias.md).

## 1. Ed-Fi Data Standard 6.1 (K-12, prestação de contas estadual)

### 1.1 Organização (D1)

```
EducationOrganization (EducationOrganizationId, NameOfInstitution, EducationOrganizationCategory[1..*], OperationalStatus)
  ├─ IsA StateEducationAgency (SEA)
  ├─ IsA EducationServiceCenter (ESC)        ── IsOrganizationComponentOf → SEA (0..1)
  ├─ IsA LocalEducationAgency (LEA)          ── → SEA (0..1), → ESC (0..1), → ParentLocalEducationAgency (0..1)
  ├─ IsA School                              ── → LEA (0..1); GradeLevel[1..*]; SchoolType; CharterStatus
  ├─ IsA PostSecondaryInstitution
  ├─ IsA CommunityOrganization / CommunityProvider
  ├─ IsA OrganizationDepartment              ── → EducationOrganization (0..1)
  └─ IsA EducationOrganizationNetwork        ── N:N com EducationOrganization via EducationOrganizationNetworkAssociation
FeederSchoolAssociation (School, FeederSchool, BeginDate)
Location (School, ClassroomIdentificationCode)  — sala
```
[E03 `EducationOrganization.mmd`, `TeachingAndLearning-SectionsAndPrograms.mmd`]. Herança "é mais útil quando a entidade é de uma e só uma subclasse" [E05].

### 1.2 Calendário (D1)

| Entidade | Identidade | Atributos-chave |
|---|---|---|
| SchoolYearType | SchoolYear (enumeração) | — |
| Session | School + SchoolYear + SessionName | BeginDate, EndDate, Term (descritor), TotalInstructionalDays; GradingPeriods 0..*, AcademicWeeks 0..* |
| GradingPeriod | School + SchoolYear + GradingPeriod (descritor) + GradingPeriodName | BeginDate, EndDate, PeriodSequence, TotalInstructionalDays |
| Calendar / CalendarDate | School + SchoolYear + CalendarCode / + Date | tipo de dia (descritor) [I] |
| ClassPeriod / BellSchedule | School + ClassPeriodName | horários |

Observação [I]: Session é **por escola**, sem hierarquia pai/filho; a relação Session ↔ GradingPeriod é N:N.

### 1.3 Ensino (D1/D4)

| Entidade | Identidade | Relações e atributos |
|---|---|---|
| Course | CourseCode + EducationOrganization | catálogo; CourseTitle, NumberOfParts, AcademicSubject, OfferedGradeLevel[], LearningStandard[] (N:N), créditos |
| CourseOffering | LocalCourseCode + School + Session | → Course (1, obrigatório); CurriculumUsed[] |
| Section | SectionIdentifier + CourseOffering | Location, ClassPeriod[] (N:N), Program[] (N:N), EducationalEnvironment, MediumOfInstruction, InstructionLanguage, SectionType |
| Program | EducationOrganization + ProgramName + ProgramType | programa de serviço (ex.: educação especial, Title I) — **não** é série/etapa |
| StudentCohort / Cohort | — | grupos para intervenção (não detalhado) |

### 1.4 Pessoas e vínculos (D1/D3)

| Entidade | Identidade | Notas |
|---|---|---|
| Student | StudentUniqueId | Name, BirthData; → Person (0..1) |
| Staff | StaffUniqueId | |
| Contact (antes Parent) | ContactUniqueId | renomeado no DS 5.0 [E08] |
| Person | PersonId + SourceSystem | elo opcional entre registros de papéis diferentes [E03]; o UDM evita "Person" unificada [E05] |
| StudentIdentificationCode / StaffIdentificationCode / ContactIdentificationCode | pessoa + EducationOrganization + IdentificationSystem | identificadores múltiplos atribuídos por organização |
| StudentDemographic / StudentDirectory | Student + EducationOrganization | dado pessoal **como reportado por cada organização** (DS 6.0) [E02] |
| StudentEducationOrganizationAssociation | Student + EducationOrganization | vínculo genérico com indicadores |
| StudentSchoolAssociation | Student + School + **EntryDate** | EntryGradeLevel (obrigatório), ExitWithdrawDate, ExitWithdrawType, PrimarySchool, Calendar, GraduationPlan, EnrollmentType, FullTimeEquivalency |
| StudentEducationOrganizationResponsibilityAssociation | Student + EducationOrganization + Responsibility + **BeginDate** | organização responsável (ex.: responsável pela prestação de contas) |
| StudentSectionAssociation | Student + Section + **BeginDate** | EndDate, HomeroomIndicator, AttemptStatus, RepeatIdentifier, Program[] |
| StudentContactAssociation | Student + Contact | Relation (descritor), LegalGuardian, LivesWith, PrimaryContactStatus, EmergencyContactStatus, ContactPriority, ContactRestrictions |
| GeneralStudentProgramAssociation (e especializações, ex.: StudentSpecialEducationProgramAssociation) | Student + EducationOrganization + Program + **BeginDate** | serviços e programas |
| StaffSectionAssociation | Staff + Section + **BeginDate** | ClassroomPosition (obrigatório), EndDate, PercentageContribution |
| StaffEducationOrganizationAssignmentAssociation | Staff + EducationOrganization + StaffClassification + **BeginDate** | função na organização |
| StaffEducationOrganizationEmploymentAssociation | Staff + EducationOrganization + EmploymentStatus | vínculo empregatício |
| StaffSchoolAssociation | Staff + School + ProgramAssignment | |

### 1.5 Resultados e avaliação (D5)

| Entidade | Identidade | Notas |
|---|---|---|
| Grade | StudentSectionAssociation + GradingPeriod + GradeType | LetterGradeEarned, NumericGradeEarned, LearningStandardGrade[] |
| ReportCard | Student + EducationOrganization + GradingPeriod | boletim |
| StudentAcademicRecord / CourseTranscript | Student + EducationOrganization + SchoolYear + Term / + Course + CourseAttemptResult | histórico escolar |
| CompetencyObjective / StudentCompetencyObjective | EducationOrganization + Objective + ObjectiveGradeLevel / + Student + GradingPeriod | avaliação por objetivo local |
| Assessment | AssessmentIdentifier + **Namespace** | AcademicSubject, AssessedGradeLevel[], AssessmentScore[], AssessmentPerformanceLevel[], ContentStandard, AdaptiveAssessment |
| ObjectiveAssessment, AssessmentItem | parte de Assessment | → LearningStandard |
| StudentAssessment | StudentAssessmentIdentifier + Student + Assessment | ScoreResult[], PerformanceLevel[], **Accommodation[] (descritor)**, ReasonNotTested, AdministrationEnvironment |
| LearningStandard / LearningStandardEquivalenceAssociation | LearningStandardId | padrão curricular e equivalências |

### 1.6 Outros domínios sem alvo direto no Core

Attendance (StudentSchool/Section/ProgramAttendanceEvent, SectionAttendanceTakenEvent), Discipline, StudentHealth (imunizações), Finance, Survey, Intervention, Path (PathPhase, PathMilestone, StudentPath), Credential (de educador), PerformanceEvaluation, RecruitmentAndStaffing, EducatorPreparationProgram, RestraintEvent (educação especial) [E03].

## 2. OneRoster 1.2 (roster para aplicações)

```
Org (type: national|state|local|district|school|department; parent 0..1, children 0..*)
AcademicSession (type: schoolYear|term|semester|gradingPeriod; parent 0..1, children 0..*; schoolYear; startDate; endDate)
Course (org 1; schoolYear 0..1; courseCode; grades[]; subjects[]; subjectCodes[])
Class (course 1; school 1; terms 1..*; classType: homeroom|scheduled; periods[]; location)
User (roles 1..* ; userIds[]; primaryOrg; userProfiles[])
  Role (roleType: primary|secondary; role: RoleEnum; org 1; beginDate; endDate)
Enrollment (user 1; class 1; school 1; role: student|teacher|administrator|proctor; primary; beginDate; endDate)
Demographics (1:1 com User)
Gradebook: Category, LineItem, Result, ScoreScale   (atributos não lidos nesta rodada; ex. LineItem→class, Result→lineItem+student [I])
Resources: Resource (vinculado a Course/Class/User)
Base: sourcedId, status, dateLastModified, metadata{extensions}
```
[E11]. Valores dos enums em [fichas/oneroster.md](fichas/oneroster.md).

## 3. Edu-API 1.0 (ensino superior)

```
Organization (parent/children) ── Affiliation (person, organization, role, startDate, endDate, affiliationStatus) ── Person (PersonName, IdentifierEntry[], Agents[])
AcademicSession (parent/children, sessionType)
CollectionTemplate ⊃ CourseTemplate ⊃ ComponentTemplate       (catálogo)
   │ 1 → 0..*                                                  
CollectionOffering ⊃ CourseOffering ⊃ ComponentOffering       (oferta: organization, academicSession, offeringFormat, synchronicity, roleEnablement, learningObjectiveSet)
Enrollment (person, educationOffering, role, isActive, enrollmentStatus, startDate, endDate)
```
[E13].

## 4. CASE 1.1 (currículo)

`CFDocument` (framework) 1 → 0..* `CFItem`; `CFAssociation` (originNodeURI, destinationNodeURI com `targetType`, associationType) entre itens/documentos, inclusive para fora do CASE. Detalhes em `iop.comp.case`.

## 5. Frameworks curriculares

| Framework | Níveis | Identificação |
|---|---|---|
| CCSS Matemática | framework → set → grade → domain → cluster → standard | `Math.6.EE.1` (forma oficial com prefixo CCSS) / URI / GUID [E19] |
| CCSS ELA | framework → (set: anchor) → grade → strand/domain → standard | `CCSS.ELA-Literacy.RL.2.1` |
| NGSS | série/banda → (tópico ou DCI) → PE; PE ← SEP + DCI(sub-ideia) + CCC | `HS-PS1-1`, `2-PS1-2` [E25] |

## 6. Caliper (eventos)

Event (`id` urn:uuid, `type`, `actor`, `action`, `object`, `eventTime` ISO 8601 UTC ms, `profile`) em Envelope emitido por Sensor; ver `iop.lr.caliper`.

## 7. Comparação estrutural das três camadas de "turma"

| Camada [I] | Ed-Fi | OneRoster | Edu-API | Core provisório |
|---|---|---|---|---|
| Unidade de catálogo (o que se ensina) | Course | Course | CourseTemplate | C.SUB (aproximado) — **sem entidade própria** |
| Oferta num período | CourseOffering | (implícita em Class.terms) | CourseOffering | C.OFR |
| Instância com pessoas e horário | Section | Class (scheduled) | CourseOffering / ComponentOffering | C.OFR |
| Agrupamento administrativo | (homeroom via StudentSectionAssociation.HomeroomIndicator) | Class (homeroom) | — | C.GRP kind=acadêmica |
| Grupo flexível | Cohort / StudentCohort | — | — | C.GRP kind=flexível |
