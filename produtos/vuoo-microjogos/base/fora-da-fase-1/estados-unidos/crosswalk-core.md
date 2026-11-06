# Crosswalk: conceitos americanos → Core provisório

Alvos: entidades C.xxx de [_convencoes.md §4](../../_convencoes.md). Tipos: **exata**, **aproximada**, **parcial**, **mais ampla** (conceito americano é mais amplo que o alvo), **mais restrita**, **inexistente**. Todas as linhas são mapeamento proposto por esta pesquisa **[I]**, fundamentado nas definições citadas em [modelo-de-dados.md](modelo-de-dados.md) e nas fichas; nenhum padrão declara equivalência com o Core.

## 1. Organização, calendário e oferta (D1)

| Conceito EUA | Padrão | Alvo | Tipo | Observação |
|---|---|---|---|---|
| EducationOrganization | Ed-Fi | C.ORG | exata | superclasse abstrata |
| SEA / LEA / ESC / School / PostSecondaryInstitution / OrganizationDepartment | Ed-Fi | C.ORG (`kind`) | mais restrita | subclasse → valor de `kind` controlado por C.VOC |
| EducationOrganizationNetwork | Ed-Fi | C.ORG + relação N:N | parcial | exige que C.ORG aceite pertencimento múltiplo, não só árvore |
| CommunityOrganization / CommunityProvider | Ed-Fi | C.ORG | aproximada | provedores externos (ex.: contraturno) |
| Org (type) | OneRoster | C.ORG | exata | `parent` único |
| Organization | Edu-API | C.ORG | exata | |
| Location | Ed-Fi | C.LOC | exata | sala por escola |
| Session | Ed-Fi | C.SES | mais restrita | por escola; sem hierarquia |
| GradingPeriod | Ed-Fi | C.SES (tipo período de avaliação) | mais restrita | N:N com Session |
| AcademicSession | OneRoster, Edu-API | C.SES | exata | hierárquica, com tipo |
| SchoolYear (enumeração) | Ed-Fi | C.SES (tipo ano letivo) | aproximada | é chave, não entidade |
| Calendar / CalendarDate | Ed-Fi | C.SES + C.SCH | parcial | dias letivos: sem alvo próprio (ver Q17) |
| ClassPeriod / BellSchedule | Ed-Fi | C.SCH | aproximada | |
| Course | Ed-Fi, OneRoster | C.SUB | aproximada | unidade de catálogo com créditos/séries; Core não distingue catálogo de componente (Q18) |
| CourseTemplate / CollectionTemplate / ComponentTemplate | Edu-API | C.SUB / C.PRG | parcial | Collection ≈ programa; Component sem alvo |
| AcademicSubject (descritor), subjectCodes | Ed-Fi, OneRoster | C.SUB via C.VOC | aproximada | área/assunto |
| CourseOffering | Ed-Fi, Edu-API | C.OFR | parcial | oferta sem pessoas |
| Section | Ed-Fi | C.OFR | aproximada | oferta com pessoas, sala, horário |
| Class `scheduled` | OneRoster | C.OFR | aproximada | |
| Class `homeroom` | OneRoster | C.GRP (`kind`=acadêmica) | aproximada | |
| Cohort / StudentCohort | Ed-Fi | C.GRP (`kind`=flexível) | aproximada | |
| GradeLevel (descritor) | Ed-Fi, OneRoster `grades` | C.PRG (série) | aproximada | K–12 vs. etapas brasileiras: tabela no adaptador |
| Program | Ed-Fi | C.SUP / C.ENR | **falso amigo de C.PRG** | programa de serviço, não etapa |
| context (LTI) | LTI | C.OFR ou C.GRP | aproximada | depende do LMS |

## 2. Pessoas, papéis e vínculos (D1/D3)

| Conceito EUA | Padrão | Alvo | Tipo | Observação |
|---|---|---|---|---|
| Student | Ed-Fi | C.PER + C.LRN | parcial | registro de papel, não pessoa |
| Staff | Ed-Fi | C.PER + C.STF | parcial | |
| Contact | Ed-Fi | C.PER + C.GRD | parcial | |
| Person (PersonId + SourceSystem) | Ed-Fi | C.PER + C.IDN | aproximada | elo de resolução de identidade |
| User | OneRoster | C.PER | aproximada | carrega papéis |
| Person | Edu-API | C.PER | exata | papéis fora da pessoa |
| Role (role, org, roleType, begin/end) | OneRoster | C.LRN / C.STF / C.GRD (papel contextual) | aproximada | **papel por organização com vigência**; Core precisa de atribuição de papel como entidade (Q19) |
| Affiliation | Edu-API | C.ENR (pessoa×org) + papel | aproximada | |
| StudentSchoolAssociation | Ed-Fi | C.ENR (pessoa×org) | aproximada | inclui série de entrada, tipo de saída |
| StudentEducationOrganizationAssociation | Ed-Fi | C.ENR (pessoa×org) | parcial | vínculo sem vigência |
| StudentEducationOrganizationResponsibilityAssociation | Ed-Fi | C.ENR + papel da organização | parcial | responsabilidade (ex.: prestação de contas) ≠ matrícula |
| StudentSectionAssociation | Ed-Fi | C.ENR (pessoa×oferta) | exata | |
| Enrollment | OneRoster, Edu-API | C.ENR (pessoa×oferta) | exata | inclui papel de staff (teacher) |
| StaffSectionAssociation | Ed-Fi | C.ENR (staff×oferta) / C.STF | aproximada | ClassroomPosition = papel |
| StaffEducationOrganizationAssignmentAssociation | Ed-Fi | C.ENR (staff×org) / C.STF | aproximada | |
| StaffEducationOrganizationEmploymentAssociation | Ed-Fi | — | inexistente | vínculo trabalhista fora do escopo |
| StudentContactAssociation | Ed-Fi | C.GRD | exata | LegalGuardian, LivesWith, prioridade, restrições |
| Agent | Edu-API | C.GRD | aproximada | |
| GeneralStudentProgramAssociation | Ed-Fi | C.ENR (pessoa×programa) | aproximada | |
| StudentSpecialEducationProgramAssociation | Ed-Fi | C.SUP + C.ENR | parcial | |
| IEP (Early Access DS 6.1) | Ed-Fi | C.PLN | aproximada | modelo não inspecionado |
| StudentDemographic / StudentDirectory | Ed-Fi | C.PER + C.PRV | parcial | dado pessoal com fonte organizacional |
| Demographics | OneRoster | C.PER | aproximada | atributos sensíveis |
| StudentIdentificationCode / userIds / IdentifierEntry / LTI `sub` | todos | C.IDN | exata | `scheme` + organização atribuidora |
| UserProfile | OneRoster | C.IDN | parcial | credenciais por aplicação; sem alvo pleno |

## 3. Currículo e competências (D2/D4)

| Conceito EUA | Padrão | Alvo | Tipo | Observação |
|---|---|---|---|---|
| CFDocument | CASE | C.CFW | exata | |
| CFItem | CASE | C.CMP | exata | |
| CFAssociation | CASE | C.CAS | exata | 9 tipos; alvo pode ser não-CASE |
| CFItemType / CFSubject / CFConcept | CASE | C.VOC | aproximada | não verificados em fonte primária |
| LearningStandard | Ed-Fi | C.CMP | aproximada | |
| LearningStandardEquivalenceAssociation | Ed-Fi | C.CAS (equivalência) | aproximada | |
| LearningObjectiveSet | Edu-API | C.CAS (oferta→competência) | parcial | Core não tem alinhamento oferta↔competência explícito |
| CCSS (framework) / NGSS | CCSS, NGSS | C.CFW | exata | |
| CCSS domain / cluster / standard | CCSS | C.CMP (`kind`) | exata | profundidade variável |
| NGSS Performance Expectation | NGSS | C.CMP | aproximada | composto de três dimensões |
| NGSS SEP / DCI / CCC | NGSS | C.CMP (outros esquemas) + C.CAS (composição) | parcial | relação de composição com papel ausente no Core |
| Clarification statement / assessment boundary | NGSS | atributo de C.CMP / C.CAS→C.ASM | parcial | |
| Connection boxes | NGSS | C.CAS | aproximada | inclusive cross-framework (→ CCSS) |
| Identificadores CCSS (pontos, URI, GUID) | CCSS | C.IDN | exata | múltiplos por item |

## 4. Avaliação e resultados (D5)

| Conceito EUA | Padrão | Alvo | Tipo | Observação |
|---|---|---|---|---|
| Assessment / ObjectiveAssessment | Ed-Fi | C.ASM | exata / parcial | ObjectiveAssessment é parte |
| AssessmentItem | Ed-Fi, QTI | C.ITM | exata | |
| StudentAssessment | Ed-Fi | C.RES (+ C.EVD) | aproximada | inclui Accommodation → C.SUP |
| AssessmentScore / PerformanceLevel | Ed-Fi | C.RES (escala) | parcial | escala sem entidade própria |
| Grade | Ed-Fi | C.RES | aproximada | nota por oferta e período |
| ReportCard / StudentAcademicRecord / CourseTranscript | Ed-Fi | C.RES / C.CRD | parcial | histórico escolar sem alvo próprio (Q20) |
| LineItem | OneRoster | C.ASM / C.ACT | aproximada | item do diário de notas |
| Result | OneRoster | C.RES | exata | |
| ScoreScale | OneRoster | C.VOC / C.RES | parcial | |
| Category (gradebook) | OneRoster | — | inexistente | ponderação de diário |
| CompetencyObjective / StudentCompetencyObjective | Ed-Fi | C.CMP / C.RES | aproximada | objetivo local avaliado |
| AchievementCredential / ClrCredential | OB, CLR | C.CRD | exata | |
| Alignment | OB, CLR | C.CAS | aproximada | |
| ResultDescription / RubricCriterionLevel | CLR | — | inexistente | rubrica (Q12) |
| QTI PNP (AccessForAll) | QTI | C.SUP | aproximada | necessidade de acesso sem diagnóstico |

## 5. Experiência e eventos (D6)

| Conceito EUA | Padrão | Alvo | Tipo |
|---|---|---|---|
| Caliper Event | Caliper | C.EVT | exata |
| Caliper Entity (DigitalResource, AssessmentItem) | Caliper | C.ACT / C.ITM | aproximada |
| Envelope / Sensor | Caliper | C.PRV | parcial |
| Resource | OneRoster | C.ACT | aproximada |
| Resource link | LTI | C.ACT | aproximada |
| Cartridge | Common Cartridge | C.ACT (pacote) + C.PRV | parcial |
| Intervention | Ed-Fi | C.ACT / C.PLN | parcial |
| Path / PathMilestone / StudentPath | Ed-Fi | — | inexistente (percurso; ver Q21) |

## 6. Governança (D8)

| Conceito EUA | Padrão | Alvo | Tipo | Observação |
|---|---|---|---|---|
| Descriptor | Ed-Fi | C.VOC | exata | namespace = governante |
| Descriptor mapping | Ed-Fi | C.VOC (mapeamento) | parcial | Core não tem entidade de mapeamento de códigos (Q22) |
| Option set / element | CEDS | C.VOC | exata | |
| `ext:` vocabulary terms / metadata.extensions | OneRoster, Edu-API | mecanismo de extensão do Core | n/a | |
| sourcedId / dateLastModified / status | OneRoster | C.IDN / C.PRV | aproximada | |
| Consent (FERPA §99.30) | FERPA | C.CNS | exata | escopo: registros, finalidade, destinatário |
| School official exception / legitimate educational interest | FERPA | C.CNS (`legal_basis`) | aproximada | |
| Directory information + opt-out | FERPA | — | inexistente | classificação por atributo + preferência da pessoa (Q14) |
| Record of disclosures (§99.32) | FERPA | C.PRV | parcial | registro de divulgação sem alvo pleno (Q14) |
| Eligible student (transferência de direitos) | FERPA | C.GRD + regra | parcial | |
| Verifiable parental consent / school authorization | COPPA | C.CNS | aproximada | concedente: responsável ou escola |
| Data retention policy | COPPA | — | inexistente | Q16 |
| Data privacy agreement (contrato) | leis estaduais | — | inexistente | Q16 |
| Escopo `core.readonly.privacy` | Edu-API | — | inexistente | sensibilidade por atributo (Q14) |

## 7. Entidades americanas sem alvo no Core provisório

Frequência/attendance (StudentSchool/Section/ProgramAttendanceEvent); disciplina (DisciplineIncident, RestraintEvent); saúde (imunização); finanças; pesquisa (Survey); vínculo empregatício e avaliação de desempenho docente; recrutamento; formação de educadores; credencial de educador; Path; categoria de diário; rubrica; registro de divulgação; directory information/opt-out; política de retenção; acordo de compartilhamento de dados; dias letivos (CalendarDate); unidade de catálogo (Course) distinta de componente; atribuição de papel com vigência como entidade.
