# European Learning Model (ELM)

```yaml
id: eu-elm
name: European Learning Model (originalmente "Europass Learning Model")
acronym: ELM
jurisdiction: União Europeia / EEE (uso voluntário; infraestrutura Europass)
issuing_organization: Comissão Europeia, DG EMPL, Unidade EMPL.B.2 (Skills Agenda)
reference_type: modelo de dados semântico (ontologia OWL + perfis de aplicação SHACL)
domain: [D2, D3, D4, D5, D8; D1 só marginal]
official_url: https://europa.eu/europass/elm-browser/index.html
repository_url: https://github.com/european-commission-empl/European-Learning-Model (ARQUIVADO; última versão marcada 3.1, 2023-06-08)
version: "3.3 (vigente segundo a Europass, notícia de 2025-08-11); repositório GitHub congelado em 3.1; ontologia ELM.ttl com dc:modified 2023-06-05"
publication_date: "v1.0 2020-10-27; v3.0 2023-04-03; v3.1 2023-06-08 (tags GitHub)"
last_updated: "v3.3 em 2025 (data exata not_found); distribuição JSON Schema snb-model 20250514-0 no portal EU Vocabularies"
legal_status: padrão técnico da Comissão; não é ato normativo. O uso é exigido para emitir European Digital Credentials (EDC) e publicar no QDR.
mandatory_scope: obrigatório só para quem emite EDC/publica no QDR; não há obrigação para escolas de educação básica
education_levels: todos (formal, não formal, informal); orientado a qualificações, ensino superior, EFP e microcredenciais
geographic_scope: UE/EEE e países Europass
language: 29 línguas no ELM Browser; vocabulários controlados multilíngues
license: EUPL-1.2 (repositório GitHub)
technical_formats: [RDF/Turtle, RDF/XML, OWL, SHACL, JSON-LD (contexto edc-ap-context.jsonld), JSON Schema (perfil EDC), XSD (perfis QDR, legado)]
api_available: não há API do modelo; ferramentas EDC (Issuer, Viewer) e QDR têm interfaces próprias (not_found detalhe)
data_model_available: sim
ontology_available: sim (http://data.europa.eu/snb/model/elm)
schemas_available: sim (SHACL por perfil: EDC, LOQ, AMS, PID; JSON Schema EDC; XSD QDR legado)
implementation_examples: sim (pasta Credentials/ com exemplos JSON-LD ELM v3 e XML ELM v2)
related_standards: [W3C VC Data Model, ELMO/EMREX, ESCO, EQF, ISCED-F 2013, DigComp, CEFR, eIDAS, Core Person/Location Vocabularies, ADMS, FOAF, W3C ORG/RegOrg]
entities: ver análise
relationships: ver análise
vocabularies: 37 listas controladas na coleção Europass do EU Vocabularies (ver terminologia.md)
core_relevance: alta para D2/D3/D5 (separação especificação × instância, resultado de aprendizagem, credencial verificável); baixa para D1
regional_adapter_relevance: alvo de exportação de conquistas/credenciais de um adaptador UE
limitations: não modela turma, matrícula, calendário, horário, oferta de componente; repositório GitHub arquivado (fonte vigente migrou para ELM Browser/EU Vocabularies)
open_questions: diferenças campo a campo entre 3.1 (GitHub) e 3.3 (EU Vocabularies) não verificadas
sources: [S-UE-01, S-UE-02, S-UE-03, S-UE-04, S-UE-05]
access_date: 2026-11-05
research_status: verificado (ontologia 3.1 inspecionada); 3.3 só por notícia oficial
```

## Análise técnica (§6.3)

**Origem e estado.** O README do repositório oficial abre com "This repository is archived and no longer updated" e remete ao ELM Browser (documentação) e ao dataset `snb-model` do EU Vocabularies (artefatos técnicos) [S-UE-01]. A API do GitHub confirma `archived: true`, licença EUPL-1.2 e tags 1.0, 3.0 e 3.1 [S-UE-01]. A Europass declara a versão 3.3 (2025): suporte a documentos de mobilidade Europass em EDC, propriedade nova para ordenar itens de conteúdo da credencial, montenegrino nas listas controladas e uma estratégia de versionamento com endereço estável por versão no Publications Office [S-UE-03]. O que segue foi lido na ontologia `rdf/ontology/ELM.ttl` (v3.1).

**Âmbito declarado.** Modelo "for Interoperability of Learning Opportunities, Qualifications, Accreditation and Credentials in Europe", com o objetivo de descrever "certificates of attendance, examination results, degrees and diplomas, diploma supplements, professional certifications, employer recommendations" [S-UE-01]. É **extensão do W3C Verifiable Credentials** em JSON-LD e está "fully mapped" ao ELMO/EMREX [S-UE-01].

### Classes (47 `owl:Class` em ELM.ttl v3.1)

Padrão central: **par Especificação × Instância (Claim)**. A especificação descreve o que se oferece ou se exige; o Claim registra o que aconteceu com uma pessoa, e liga-se à especificação por `specifiedBy`.

| Instância (subclasse de `elm:Claim`) | Especificação | Definição oficial (rdfs:comment, resumida) |
|---|---|---|
| `LearningAchievement` | `LearningAchievementSpecification` (subclasse: `Qualification`) | "A recognised and/or awarded set of learning outcomes of an individual" |
| `LearningActivity` | `LearningActivitySpecification` | "Any process which leads to the acquisition of knowledge, skills or responsibility and autonomy" |
| `LearningAssessment` | `LearningAssessmentSpecification` | resultado de processo que estabelece em que medida o aprendiz atingiu conhecimentos/habilidades contra critérios |
| `LearningEntitlement` | `LearningEntitlementSpecification` | direito (exercer profissão, acessar oportunidade) resultante da aprendizagem |

Demais classes: `LearningOpportunity` ("An opportunity to realise a given set of learning outcomes via a learning activity and/or assessment"), `LearningOutcome` (enunciado em termos de conhecimento, habilidades, responsabilidade e autonomia), `Qualification` ("A specification of an assessment and validation process which is obtained when a competent authority determines..."), `AwardingProcess`, `AwardingBody`, `AwardingOpportunity`, `Accreditation`, `CreditPoint`, `GradingScheme`, `ResultDistribution`, `ResultCategory`, `ShortenedGrading`, `Evidence`, `EuropeanDigitalCredential` (subclasse de `cred:VerifiableCredential`), `EuropeanDigitalPresentation`, `VerificationCheck`, `Agent`, `Person` (subclasse de `Agent` e `cpv:Person`), `Organisation` (subclasse de `Agent` e `rov:RegisteredOrganization`), `Group` (subclasse de `foaf:Group`, "collection of Agents"), `Identifier`, `LegalIdentifier`, `Address`, `ContactPoint`, `Phone`, `Mailbox`, `Grant`, `PriceDetail`, `Amount`, `Note`, `MediaObject`, `WebResource`, `DisplayDetail`/`DisplayParameter`/`IndividualDisplay`, `QualificationReference`, `Specification`, `ShaclValidator2017` [S-UE-02].

### Propriedades relevantes para o Core

| Propriedade | Domínio → Alcance | Nota para o Core |
|---|---|---|
| `specifiedBy` | Claim → Specification | separa "o que é" de "o que aconteceu"; perfis restringem pares |
| `awardedBy` | Claim → AwardingProcess | quem concedeu, onde, quando (proveniência da conquista) |
| `learningOutcome` | LearningAchievementSpecification → LearningOutcome | resultado esperado ligado à especificação |
| `relatedESCOSkill`, `relatedSkill` | LearningOutcome → skos:Concept | alinhamento a taxonomias externas por SKOS |
| `EQFLevel`, `NQFLevel` | Qualification → skos:Concept | nível como conceito de vocabulário, não inteiro |
| `ISCEDFCode` | LearningAchievementSpecification → skos:Concept | área ISCED-F 2013 |
| `educationLevel`, `learningSetting`, `mode`, `targetGroup`, `learningSchedule` | → skos:Concept | tudo codificado por listas controladas |
| `creditPoint` | Specification → CreditPoint (sistema + valor) | crédito com `framework` (ex.: ECTS) |
| `grade` | LearningAssessment → xsd:string | nota textual; escala em `gradingScheme` |
| `hasPart` / `isPartOf` | mesma classe | composição recursiva (programa → módulo) |
| `entryRequirement`, `influencedBy`/`influences`, `provenBy`/`proves`, `specialisationOf`/`generalisationOf` | entre Claims/Specs | requisito de entrada, influência, cadeia de evidência e especialização; **não há** propriedade `prerequisite` explícita na v3.1 |
| `directedBy` | Activity → Agent | organização ou departamento que conduziu a atividade |
| `groupMemberOf` | Person → Group | única forma de agrupamento de pessoas |
| `nationalId` | Person → LegalIdentifier | identificador nacional com `spatialCode` |
| `learningSchedule` | LearningOpportunity → skos:Concept | descrição textual/codificada de agenda, não horário estruturado |

**Identificadores.** `Identifier` genérico com `schemeId`, `schemeName`, `schemeVersion`; `LegalIdentifier` com `spatialCode` (país) para pessoas e organizações; identificadores eIDAS, fiscal e IVA para organizações [S-UE-02]. É o mesmo padrão "identificador + esquema" previsto em C.IDN.

**Cardinalidades e validação.** Restritas nos perfis SHACL, não na ontologia (que deixa domínios abertos, "restricted on application profile level"). O perfil `EDC-generic-full.ttl` tem 37 `sh:NodeShape` e referencia vocabulários em `http://data.europa.eu/snb/{eqf,isced-f,learning-setting,credential,claim-type,evidence-type,verification,...}/` [S-UE-04].

**Perfis de aplicação.** EDC (credenciais: genérico, acreditado, diploma supplement, emitido por mandato, convertido), LOQ (oportunidades e qualificações para o QDR), AMS (acreditação), PID (identidade da pessoa) [S-UE-01].

**Temporalidade/versionamento.** `startDate`/`endDate`, `awardingDate`, `issuanceDate`/`validFrom`/`expirationDate` herdados do VC; versionamento do modelo por endereço estável (v3.3) [S-UE-03]. Não há versionamento de instância (histórico de mudanças de uma qualificação) no ELM.ttl [I].

**Extensão.** Por perfis de aplicação SHACL e por vocabulários controlados (qualquer `skos:Concept` com esquema identificado) [S-UE-02]. Credenciais podem carregar `credentialProfiles` [S-UE-02].

**Autenticação/integridade.** Fora do modelo; o EDC exige selo eletrônico eIDAS (ver [eu-edc-europass](eu-edc-europass.md)).

**Organização acadêmica (pergunta do briefing).** Confirmado: o ELM **não** modela turma, matrícula, ano letivo, período, horário, sala, oferta de componente ou vínculo professor–turma. `Group` é só coleção de agentes; `LearningOpportunity` tem `learningSchedule` como conceito/texto e `location`, mas não sessões nem matrículas [S-UE-02]. [I] A educação básica europeia não tem modelo comum de gestão escolar, o que é coerente com a competência nacional (ver [eu-competencia-nacional](eu-competencia-nacional.md)).

### Lições para o Core [I]

1. **Especificação × instância** é o padrão mais reutilizável: C.CMP/C.ASM descrevem; C.RES/C.CRD/C.EVD registram ocorrências ligadas por `specifiedBy`.
2. **Níveis e áreas como `skos:Concept` de um esquema identificado** (EQF, ISCED-F), nunca inteiros soltos: reforça C.VOC.
3. **Credencial = envelope VC** sobre claims de aprendizagem; C.CRD deve poder serializar-se em VC/ELM sem perda.
4. **Ausência de D1** no ELM confirma que o modelo de organização escolar do Core não pode vir da UE; virá de Ed-Fi/OneRoster/CBDS/Educacenso.
