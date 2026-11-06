# Ficha: OneRoster 1.2

> Análise conceitual em conhecimento/interoperabilidade/rostering/oneroster.md (`iop.ros.oneroster`). Aqui: classes, enumerações, papéis por organização e regras de extensão, lidos no Information Model do Rostering Service.

```yaml
id: us.oneroster
name: OneRoster
acronym: OR
jurisdiction: internacional (origem e adoção majoritária nos EUA)
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário (especificação técnica com certificação)
domain: [D1, D5, D8]   # D5 via Gradebook; D6 indireto via Resources
official_url: https://www.1edtech.org/standards/oneroster
repository_url: https://www.imsglobal.org/spec/oneroster/v1p2/rostering/info
version: 1.2 (IMS Final Release)
publication_date: 2022-09-19 [E11]
last_updated: unknown
legal_status: voluntário
mandatory_scope: not_found como exigência normativa estadual; aparece como critério de compra (guia de procurement do 1EdTech) [E37]
education_levels: K-12 (ensino superior coberto por Edu-API)
geographic_scope: internacional
language: inglês
license: unknown (especificação pública; termos de licença não lidos)
technical_formats: REST/JSON, CSV
api_available: sim (Rostering, Gradebook, Resources)
data_model_available: sim (Information Model UML)
ontology_available: not_found
schemas_available: sim (JSON Schema/OpenAPI citados no conjunto; não inspecionados)
implementation_examples: sim (exemplos no documento)
related_standards: [LTI NRPS, Edu-API, Ed-Fi (perfil OneRoster no ODS/API), IMS LIS]
entities: [Org, AcademicSession, Course, Class, Enrollment, User, Role, UserProfile, Demographics, LineItem, Result, Category, ScoreScale, Resource]
relationships: Course→Org (1); Class→Course (1), Class→School (1), Class→terms (1..*); Enrollment = User×Class com role; Role = User×Org
vocabularies: OrgTypeEnum, SessionTypeEnum, ClassTypeEnum, RoleEnum, RoleTypeEnum, EnrolRoleEnum, BaseStatusEnum, GenderEnum
core_relevance: alta — modelo mínimo de roster, papéis por organização, sessões hierárquicas
regional_adapter_relevance: alta (formato de fato para apps de sala de aula K-12)
limitations: sem frequência, programas, avaliação externa; troca CSV em lote
open_questions: ver questoes-abertas.md Q05
sources: [E11, E12, E37]
access_date: 2026-11-05
research_status: verificado em fonte primária (Information Model, seções 3–8)
```

## Acréscimos ao documento de `conhecimento/`

**Classe base.** Toda entidade tem `sourcedId`, `status` (BaseStatusEnum: `active`, `tobedeleted`), `dateLastModified` e `metadata` [E11].

**Classes e atributos principais** [E11]:

| Classe | Atributos |
|---|---|
| Org | name, type, identifier, parent, children |
| AcademicSession | title, startDate, endDate, type, parent, children, schoolYear |
| Course | title, schoolYear, courseCode, grades, subjects, org, subjectCodes, resources |
| Class | title, classCode, classType, location, grades, subjects, course, school, terms, subjectCodes, periods, resources |
| Enrollment | user, class, school, role, primary, beginDate, endDate |
| User | userMasterIdentifier, username, userIds, enabledUser, nomes, identifier, email, sms, phone, roles, userProfiles, primaryOrg, resources… |
| Role | roleType, role, org, userProfile, beginDate, endDate |
| UserProfile | profileId, profileType, vendorId, applicationId, description, credentials |
| Demographics | birthDate, sex, campos de raça/etnia… |

**Course × Class.** Course é "programa de estudo", tipicamente com currículo comum, atribuído a uma única org; class é a atividade de ensino de um course, e cada course é ensinado por uma ou mais classes [E11].

**Papéis por organização (novidade da 1.2).** O atributo `roles` foi adicionado a User, e `role`/`orgs` removidos. "A user must have at least one role and each role is assigned in the context of a single org" [E11 §3.3].

**Enumerações** [E11 §6.3]:

| Enum | Valores | Extensível com `ext:` |
|---|---|---|
| OrgTypeEnum | department, district, local, national, school, state | sim |
| SessionTypeEnum | gradingPeriod, schoolYear, semester, term | sim |
| ClassTypeEnum | homeroom, scheduled | sim |
| RoleEnum | aide, counselor, districtAdministrator, guardian, parent, principal, proctor, relative, siteAdministrator, student, systemAdministrator, teacher | sim |
| RoleTypeEnum | primary, secondary | não |
| EnrolRoleEnum | administrator, proctor, student, teacher | não |
| GenderEnum | female, male, other, unspecified | sim |
| BaseStatusEnum | active, tobedeleted | não |

**Extensões** [E11 §8.1]: dados proprietários só no espaço `metadata` da classe Base; operações existentes não podem ser alteradas; termos proprietários de vocabulário com prefixo `ext:` (padrão `(ext:)[a-zA-Z0-9\.\-_]+`); perfis só podem restringir, nunca acrescentar.

**Segurança** (1.1, mantida como referência): OAuth 2.0 Bearer com client credentials, TLS ≥ 1.2 [E12].
