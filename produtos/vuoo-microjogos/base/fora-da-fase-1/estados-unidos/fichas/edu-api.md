# Ficha: Edu-API

> Sem documento em `conhecimento/` (lacuna registrada em [inventario-existente.md](../../../inventario-existente.md)). Ficha completa.

```yaml
id: us.edu-api
name: Edu-API
acronym: Edu-API
jurisdiction: internacional (1EdTech); foco em ensino superior
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário (especificação técnica: modelo de informação + binding REST/JSON)
domain: [D1, D8]   # D2/D4 indireto via LearningObjectiveSet
official_url: https://standards.1edtech.org/edu-api/specifications/standards/v1p0
repository_url: unknown
version: 1.0 (Final) [E13]
publication_date: unknown (documento Candidate Final citado em 12/03/2025 por resultado de busca; data do Final não localizada)
last_updated: unknown
legal_status: voluntário
mandatory_scope: nenhum
education_levels: ensino superior (declarado); aplicável a K-12 [I]
geographic_scope: internacional (implementações nos EUA, ex.: Oracle PeopleSoft Campus Solutions; cliente Go da SUNET, Suécia)
language: inglês
license: unknown
technical_formats: REST, JSON (obrigatório)
api_available: sim — base path /1edtech/eduapi/base/v1p0 [E13]
data_model_available: sim
ontology_available: not_found
schemas_available: unknown (não verificado)
implementation_examples: sim (exemplos JSON no documento; Oracle declara suportar todos os endpoints obrigatórios)
related_standards: [OneRoster (contraparte K-12, mesma terminologia provider/consumer), IMS LIS (antecessor "espiritual"), CASE (LearningObjectiveSet com source=case)]
entities: [Person, PersonName, Agent, Organization, AcademicSession, Education, EducationOffering, CollectionTemplate, CourseTemplate, ComponentTemplate, CollectionOffering, CourseOffering, ComponentOffering, Affiliation, Enrollment, RoleEnablement, Location, Address, IdentifierEntry, LearningObjectiveSet]
relationships: template 1 → 0..* offerings; Collection ⊃ Course ⊃ Component (em template e oferta); Organization e AcademicSession hierárquicas (parent/children); Affiliation = Person×Organization; Enrollment = Person×EducationOffering
vocabularies: RoleTypeEnum, EnrollmentStatusEnum, RegistrationStatusEnum, AffiliationStatusEnum, offeringType, offeringFormat, synchronicity, sessionType, recordStatus… (listas completas não lidas)
core_relevance: alta — separa identidade de contexto e vínculo institucional (Affiliation) de vínculo com oferta (Enrollment)
regional_adapter_relevance: média para VUOO (EF/EM); alta se houver ensino superior
limitations: lista completa de enumerações não lida; data do Final não localizada
open_questions: Q07
sources: [E13, E14]
access_date: 2026-11-05
research_status: parcial — serviços, classes e segurança verificados; enumerações vistas só em exemplos
```

## Análise técnica (§6.3)

**Serviços (REST, somente leitura no v1.0)** [E13]: EducationManagement (templates e ofertas, por sessão, aluno ou staff), AcademicSessionManagement, OrganizationManagement, PersonManagement (pessoas, staff, students, pessoas por oferta ou organização), EnrollmentManagement (por id, oferta ou sessão), AffiliationManagement. O PDF de 2024 descreve o foco da primeira versão como troca em massa de matrículas entre SIS e LMS [E14, trecho].

**Modelo** [E13]:

- *Template × Offering.* Cada template (Collection, Course, Component) é instanciado em zero ou mais ofertas do mesmo tipo. Exemplo do documento: uma CourseOffering está numa AcademicSession, é instância de um CourseTemplate, é oferecida por uma Organization e tem alunos matriculados.
- *Collection → Course → Component.* Coleções compõem cursos; cursos compõem componentes (ex.: aula teórica, laboratório), nos dois níveis.
- *Affiliation × Enrollment.* O LIS tinha "Membership" único; o Edu-API separa vínculo pessoa↔organização (Affiliation) de vínculo pessoa↔oferta (Enrollment). Papéis ficam na relação, não na Person.
- *Ciclo de vida da matrícula.* Dois sinais: `isActive` (booleano) e `enrollmentStatus` (ex.: registrado, matriculado, adiado, em espera).
- *Agents.* Relações como responsável/guardião (`agentType`: parent, guardian nos exemplos).

**Atributos vistos nos exemplos** [E13]:

| Classe | Atributos |
|---|---|
| Enrollment | sourcedId, recordLanguage, isActive, enrollmentStatus, person, role, startDate, endDate, educationOffering, offeringType, recordStatus, dateLastModified |
| Affiliation | sourcedId, person, organization, role, startDate, endDate, affiliationStatus, recordStatus, dateLastModified |
| CourseOffering | offeringType, course, parent, title, description, primaryCode, otherCodes, locations, organization, academicSession, offeringFormat, paceOfStudy, registrationStatus, startDate, endDate, teachingLanguage, max/min/enrolled/pendingNumberStudents, roleEnablement, synchronicity, learningObjectiveSet… |

Valores vistos em exemplos (não são listas completas): role `member`, `chair`; enrollmentStatus `onLeave`; offeringFormat `online`; synchronicity `hybrid`; recordStatus `active`, `deleted`; learningObjectiveSet.source `case`, `unknown`.

**Extensões** [E13]: só pelo contêiner `extensions` de cada classe, com namespace por entidade (ex.: `personExtensions`); termos de vocabulário proprietários com prefixo `ext:`; novos endpoints permitidos; extensões não são testadas na conformidade; perfis só acrescentam restrições.

**Segurança** [E13]: OAuth 2.0 client credentials obrigatório; escopos `core.readonly` e `core.readonly.privacy` (atributos governados por política de privacidade da instituição); `expires_in` recomendado 3600 s; 401 token inválido, 403 escopo insuficiente; TLS obrigatório.

**Comparação com OneRoster e Ed-Fi** [I, a partir de E11, E13, E03]:

| Aspecto | OneRoster 1.2 | Edu-API 1.0 | Ed-Fi 6.1 |
|---|---|---|---|
| Catálogo vs. oferta | Course / Class | CourseTemplate / CourseOffering (+ Component) | Course / CourseOffering / Section |
| Vínculo institucional | Role (User×Org) | Affiliation (Person×Organization) | StudentSchoolAssociation, StaffEducationOrganization*Association |
| Vínculo com oferta | Enrollment (User×Class) | Enrollment (Person×Offering) | StudentSectionAssociation, StaffSectionAssociation |
| Data na identidade do vínculo | não | não | sim (BeginDate/EntryDate) |
| Escopo de privacidade na API | não | sim (`core.readonly.privacy`) | por perfil/autorização do ODS/API (não verificado) |
