# Crosswalk UE → Core provisório

Alvos: entidades C.xxx de [../_convencoes.md](../../_convencoes.md) §4. Tipos: exata, aproximada, parcial, mais ampla, mais restrita, inexistente. Todo mapeamento é **[I]** (proposta do pesquisador), fundamentado nas definições citadas em [terminologia.md](terminologia.md).

| Conceito local | Fonte | Alvo Core | Tipo | Observação |
|---|---|---|---|---|
| elm:Organisation | ELM | C.ORG | aproximada | ELM exige pessoa jurídica registrada (⊂ rov:RegisteredOrganization); C.ORG também cobre unidades sem personalidade |
| elm:Person | ELM | C.PER | exata | |
| elm:Agent | ELM | C.PER ∪ C.ORG | mais ampla | superclasse; o Core não tem "agente" genérico |
| elm:Group | ELM | C.GRP | mais ampla | coleção genérica de agentes, sem `kind`, período ou oferta |
| elm:LearningOpportunity | ELM | C.OFR | parcial | tem provedor, datas, local; não tem grupo, profissional nem horário estruturado |
| elm:learningSchedule | ELM | C.SCH | parcial | conceito/texto, não sessões |
| elm:LearningAchievementSpecification | ELM | C.CMP (ou C.PRG quando é programa) | aproximada | especificação do que se reconhece; mais próxima de "objetivo/qualificação" que de habilidade curricular |
| elm:Qualification | ELM | **sem alvo** | inexistente | candidata a entidade/subtipo (ver questões abertas) |
| elm:LearningOutcome | ELM | C.CMP | aproximada | enunciado K/S/R&A; C.CMP também cobre objeto de conhecimento |
| elm:hasPart / isPartOf | ELM | C.CAS (hierarquia) | exata | |
| elm:entryRequirement | ELM | C.CAS (pré-requisito) | aproximada | texto/nota, não necessariamente referência estruturada |
| elm:specialisationOf / generalisationOf | ELM | C.CAS | aproximada | |
| elm:relatedESCOSkill | ELM | C.CAS (alinhamento externo) | exata | |
| elm:LearningAssessmentSpecification | ELM | C.ASM | aproximada | |
| elm:LearningAssessment | ELM | C.RES | aproximada | instância com nota (string) |
| elm:GradingScheme | ELM | C.VOC (escala) | parcial | o Core não tem "escala" como entidade |
| elm:ResultDistribution | ELM | **sem alvo** | inexistente | estatística agregada da coorte; poderia ser derivada |
| elm:LearningActivity | ELM | C.ACT / C.EVT | parcial | é Claim (participação registrada), não o recurso |
| elm:LearningAchievement | ELM | C.CRD | aproximada | |
| elm:LearningEntitlement | ELM | **sem alvo** | inexistente | direito resultante (ex.: acesso a etapa seguinte) |
| elm:EuropeanDigitalCredential | ELM/EDC | C.CRD | exata (como envelope) | |
| elm:Evidence | ELM | C.EVD | aproximada | |
| elm:AwardingProcess | ELM | C.PRV | parcial | proveniência da concessão |
| elm:Accreditation | ELM | **sem alvo** | inexistente | acreditação de organização para qualificações; relevante em EFP/superior |
| elm:Identifier / LegalIdentifier | ELM | C.IDN | exata | padrão `scheme` + valor |
| elm:CreditPoint | ELM/ECTS | **sem alvo** | inexistente | atributo de C.CMP/C.PRG no Core [I] |
| EQF level | EQF | C.VOC | exata (como vocabulário) | atributo de qualificação; não equivale a C.PRG |
| NQF level | EQF | C.VOC | exata (como vocabulário) | |
| ISCED / ISCED-F | ELM, Eurydice | C.VOC (atributo de C.PRG/C.SUB) | exata | |
| ESCO skill | ESCO | C.CMP em C.CFW externo | exata | |
| DigComp (framework) | JRC | C.CFW | exata | versionar 2.2 e 3.0 separadamente |
| DigComp área / competência | JRC | C.CMP (hierárquico) | exata | |
| DigComp proficiency level | JRC | **sem alvo** | inexistente | escala de proficiência por framework |
| LifeComp / GreenComp / DigCompEdu | JRC | C.CFW + C.CMP | exata | |
| ECTS (crédito) | ECTS | sem alvo | inexistente | |
| Sistema nacional (Eurydice) | Eurydice | adaptador nacional | — | fora do Core |
| GDPR base legal / consentimento art. 8 | GDPR | C.CNS | aproximada | precisa de idade-limite por jurisdição |
| AI Act: decisão automatizada | AI Act | C.PRV + C.RES | parcial | exige registro de sistema/versão e supervisão humana |
