# Ficha: Ed-Fi Data Standard

> Análise conceitual em conhecimento/interoperabilidade/rostering/ed-fi.md (`iop.ros.ed-fi`). Esta ficha **não repete** aquele texto; acrescenta o que falta para o crosswalk: entidades, chaves, cardinalidades, descritores e extensões, lidos nos modelos oficiais da v6.1.0.

```yaml
id: us.ed-fi
name: Ed-Fi Data Standard
acronym: Ed-Fi DS
jurisdiction: Estados Unidos (uso fora dos EUA possível por extensão)
issuing_organization: Ed-Fi Alliance, LLC
reference_type: padrão voluntário (modelo de dados + diretrizes de API normativas)
domain: [D1, D3, D5, D7, D8]   # D2/D4 parcial (LearningStandard); D6 ausente
official_url: https://docs.ed-fi.org/reference/data-exchange/data-standard/
repository_url: https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard
version: 6.1.0 (corrente); 5.x também suportada
publication_date: v6.0.0 e v5.2.0 em 23 dez (ano não exibido na página de releases); v6.1.0 em 7 mai [E10]
last_updated: página What's New atualizada em 2026-10-15 [E02]
legal_status: padrão voluntário; obrigatório apenas onde um estado o impõe para coleta (ver leis-estaduais.md)
mandatory_scope: nenhum federal; estadual em alguns estados (ex.: Texas via TEDS) [E33]
education_levels: K-12 (núcleo); ensino superior parcial (PostSecondaryInstitution, EducatorPreparationProgram)
geographic_scope: EUA
language: inglês
license: Apache-2.0 (repositório do Data Standard) [E03]
technical_formats: JSON (API REST), XML/XSD (interchanges), MetaEd, Mermaid (modelos)
api_available: sim (Ed-Fi API Guidelines normativas; ODS/API é implementação de referência)
data_model_available: sim (Unifying Data Model, declarado não normativo) [E06]
ontology_available: not_found
schemas_available: sim (pasta Schemas no repositório; conteúdo não inspecionado)
implementation_examples: sim (Samples/Sample XML; distrito fictício Grand Bend) [E01]
related_standards: [CEDS, OneRoster, SIF, CASE]
entities: ver modelo-de-dados.md §1
relationships: associações de primeira classe com data inicial na identidade
vocabularies: Descriptors com namespace (uri://ed-fi.org/...) e mapeamento entre namespaces
core_relevance: alta — melhor referência de associação com vigência, vocabulário extensível e herança de organização
regional_adapter_relevance: alta (seria o formato de troca de um adaptador EUA K-12 com SEAs)
limitations: ancorado em prestação de contas dos EUA; entidades sem "Person" unificada; mudanças incompatíveis entre majors
open_questions: ver questoes-abertas.md Q01–Q04
sources: [E01, E02, E03, E04, E05, E06, E07, E08, E10]
access_date: 2026-11-05
research_status: verificado em fonte primária (modelos v6.1.0); extensões só por trecho
```

## O que falta em `conhecimento/` e foi verificado aqui

### Domínios (modelos v6.1.0)

36 diagramas no repositório [E03], entre eles: EducationOrganization, Enrollment, SchoolCalendar, BellSchedule, TeachingAndLearning (CourseCatalog, SectionsAndPrograms), StudentAcademicRecord (Gradebook, ReportCard, StudentTranscript), Assessment (AssessmentMetaData, Standards, StudentAssessment), AssessmentRegistration, StudentAttendance, Discipline, Intervention, StudentCohort, StudentHealth, SpecialEducation, SpecialEducationDataModel, AlternativeAndSupplementalServices, Graduation, Path, Staff, Credential, EducatorPreparationProgram, PerformanceEvaluation, RecruitmentAndStaffing, Finance, Survey, StudentIdentificationAndDemographics, StudentProgramEvaluation.

### Chaves de identidade (marcadas "I" nos modelos) [E03]

| Entidade | Identidade |
|---|---|
| EducationOrganization (e subclasses) | EducationOrganizationId (inteiro); subclasses: SchoolId, LocalEducationAgencyId, StateEducationAgencyId, EducationServiceCenterId… |
| Student / Staff / Contact | StudentUniqueId / StaffUniqueId / ContactUniqueId |
| Person | PersonId + SourceSystem (descritor) |
| StudentSchoolAssociation | Student + School + **EntryDate** |
| StudentEducationOrganizationAssociation | Student + EducationOrganization |
| StudentContactAssociation | Student + Contact |
| Session | School + SchoolYear + SessionName |
| GradingPeriod | School + SchoolYear + GradingPeriod (descritor) + GradingPeriodName |
| Course | CourseCode + EducationOrganization |
| CourseOffering | LocalCourseCode + School + Session |
| Section | SectionIdentifier + CourseOffering |
| StudentSectionAssociation | Student + Section + **BeginDate** |
| StaffSectionAssociation | Staff + Section + **BeginDate** |
| StaffEducationOrganizationAssignmentAssociation | Staff + EducationOrganization + StaffClassification + **BeginDate** |
| GeneralStudentProgramAssociation | Student + EducationOrganization + Program + **BeginDate** |
| Grade | StudentSectionAssociation + GradingPeriod + GradeType |
| Assessment | AssessmentIdentifier + Namespace |
| StudentAssessment | StudentAssessmentIdentifier + Student + Assessment |
| StudentIdentificationCode | Student + EducationOrganization + StudentIdentificationSystem |

### Descritores

"Data model elements that capture a controlled enumeration value", frequentemente chamados de "code sets" [E04]. O namespace indica quem governa o valor; boa prática é URI de domínio próprio; valores `uri://ed-fi.org` "must not edit or change" [E04]. "Only descriptor values in the 'ed-fi.org' namespace are part of the standard" [E01]. Desde o DS 4.0, *descriptor mappings* registram como dado a equivalência entre valores de namespaces diferentes (local, estadual, fornecedor, federal) [E04]. O UDM não impõe integridade entre o mapeamento e os descritores referidos (trecho, [E04]).

### Extensões

Extensões são permitidas apenas nas formas listadas como suportadas no Extension Framework; a implementação de referência é o MetaEd [E07, trecho]. A lista exata de tipos suportados não foi lida (página 404 na URL tentada).

### Renomeações relevantes

Parent → Contact e StudentParentAssociation → StudentContactAssociation no DS 5.0 [E08]. No DS 6.0, demografia e diretório saem de StudentEducationOrganizationAssociation para StudentDemographic e StudentDirectory, ambos com identidade Student + EducationOrganization [E02, E03].

### Temporalidade

Associações carregam BeginDate/EntryDate na identidade; a história é preservada por linhas sucessivas, não por versão [E03]. A documentação de "effective dates" afirma suporte limitado ao conceito fora disso [E09, trecho].
