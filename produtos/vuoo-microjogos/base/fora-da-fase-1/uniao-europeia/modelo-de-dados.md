# Modelo de dados: União Europeia

Só um referencial europeu tem modelo de dados formal: o **ELM** (v3.1 inspecionado; v3.3 vigente). Os frameworks do JRC têm estrutura tabular, não modelo. Dados escolares (D1) **não têm modelo europeu**: são nacionais (ver [fichas/eu-competencia-nacional.md](fichas/eu-competencia-nacional.md)). Fontes em [evidencias.md](evidencias.md).

## 1. ELM: entidades principais

```
EuropeanDigitalCredential (⊂ cred:VerifiableCredential)
  ├─ credentialSubject: Person (⊂ Agent, cpv:Person)
  │     ├─ nationalId → LegalIdentifier (spatialCode)
  │     ├─ groupMemberOf → Group (⊂ foaf:Group)
  │     └─ hasClaim → Claim
  │            ├─ LearningAchievement ─specifiedBy→ LearningAchievementSpecification ⊃ Qualification
  │            ├─ LearningActivity    ─specifiedBy→ LearningActivitySpecification
  │            ├─ LearningAssessment  ─specifiedBy→ LearningAssessmentSpecification ─gradingScheme→ GradingScheme
  │            └─ LearningEntitlement ─specifiedBy→ LearningEntitlementSpecification
  │            (todo Claim) ─awardedBy→ AwardingProcess ─awardingBody→ Organisation
  ├─ issuer: Organisation (⊂ Agent, rov:RegisteredOrganization)
  └─ evidence / verificationCheck

LearningOpportunity ─learningAchievementSpecification→ Specification
                    ─providedBy→ Organisation ; learningSchedule (skos:Concept) ; location
LearningAchievementSpecification ─learningOutcome→ LearningOutcome ─relatedESCOSkill→ skos:Concept
                                 ─creditPoint→ CreditPoint ; ISCEDFCode ; EQFLevel/NQFLevel (Qualification)
Accreditation ─accreditingAgent→ Organisation ; limitQualification / limitEQFLevel / limitField ...
```

## 2. Atributos e identificadores (seleção)

| Entidade | Identificador | Atributos relevantes | Cardinalidade |
|---|---|---|---|
| Person | URI; `nationalId` (LegalIdentifier com país) | nome (cpv), `dateOfBirth`, `placeOfBirth`, `citizenshipCountry`, `gender`, contato | definida em SHACL por perfil |
| Organisation | URI; `LegalIdentifier`, `eidasLegalIdentifier`, `vatIdentifier`, `taxIdentifier` | nome, endereço, `logo`; hierarquia via W3C ORG [I: `org:` importado] | idem |
| LearningAchievementSpecification | URI; `Identifier` (schemeId/schemeName/schemeVersion) | título, `learningOutcome` (0..n), `creditPoint`, `ISCEDFCode`, `educationLevel`, `learningSetting`, `mode`, `volumeOfLearning`, `targetGroup`, `hasPart`/`isPartOf` | idem |
| Qualification | idem | `EQFLevel`, `NQFLevel`, `isPartialQualification`, `qualificationCode` | idem |
| LearningAssessment | URI | `grade` (string), `assessedBy`, `assessmentStatus`, `resultDistribution`, `shortenedGrading` | idem |
| LearningOutcome | URI | descrição, `relatedESCOSkill`, `relatedSkill`, `reusabilityLevel`, tipo de skill | idem |
| CreditPoint | — | `framework` (skos:Concept: sistema de crédito), `point` | idem |
| AwardingProcess | — | `awardingBody`, `awardingDate`, `location` | idem |

## 3. Regras transversais

- **Validação**: SHACL por perfil (EDC, LOQ, AMS, PID). A ontologia deixa domínios e alcances abertos e diz que são "restricted on application profile level" [S-UE-02].
- **Codificação**: quase todo atributo categórico é `skos:Concept` de uma lista controlada do EU Vocabularies (URI `http://data.europa.eu/snb/<lista>/...`).
- **Temporalidade**: `startDate`/`endDate`, `awardingDate`, `issuanceDate`/`expirationDate` (VC). Sem histórico de versão por instância.
- **Serialização**: JSON-LD (contexto do perfil EDC), Turtle e RDF/XML; JSON Schema para o perfil EDC; XSD legado para o QDR.
- **Extensão**: novos perfis SHACL, novas listas controladas, `credentialProfiles`.
- **Autenticidade**: selo eIDAS no EDC (fora do modelo).

## 4. Cobertura de D1 (organização acadêmica)

| Conceito do briefing | No ELM? |
|---|---|
| organização, unidade | sim (`Organisation`; hierarquia só via `org:` importado, sem classe própria de unidade) |
| ano letivo, período | **não** (só datas no Claim/Opportunity) |
| curso/programa | parcial (`LearningAchievementSpecification`/`Qualification`, `hasPart`) |
| turma / grupo | **não** (`Group` é coleção genérica de agentes) |
| matrícula | **não** |
| oferta de componente | parcial (`LearningOpportunity` = especificação oferecida por provedor, com datas e local; sem professor nem turma) |
| horário / sessão | **não** (`learningSchedule` é conceito/texto) |
| profissional / professor | **não** como papel; `directedBy`/`assessedBy` apontam para Agent |

## 5. Frameworks de competência (estrutura comum)

| Framework | Níveis hierárquicos | Escala de proficiência | Códigos publicados | Legível por máquina |
|---|---|---|---|---|
| DigComp 3.0 | área (5) → competência (21) → resultados | 4 níveis | 1.1–5.4 | planilha + LOD (JRC); lista SKOS Europass |
| DigComp 2.2 | área (5) → competência (21) → exemplos | 8 níveis [I] | 1.1–5.4 | PDF |
| DigCompEdu | área (6) → competência (22) | sim (nomes não confirmados) | 1.1–6.5 [I] | PDF |
| LifeComp | área (3) → competência (9) → descritores | não | P1–L3 | PDF |
| GreenComp | área (4) → competência (12) | não | not_found | PDF |
| EQF | nível (8) × 3 dimensões | — | 1–8 | SKOS (snb/eqf) |
