# ECTS, Erasmus Without Paper e EMREX/ELMO (ensino superior, ficha curta)

Fora do escopo direto da VUOO (educação básica). Registrado para provar que o Core acomoda crédito e mobilidade sem mudança.

## ECTS

```yaml
id: eu-ects
name: European Credit Transfer and Accumulation System
acronym: ECTS
jurisdiction: Espaço Europeu de Ensino Superior (Bolonha)
issuing_organization: Comissão Europeia / Bologna Follow-Up Group (ECTS Users' Guide 2015)
reference_type: sistema de créditos (guia; adoção por lei nacional varia)
domain: [D1, D4, D5]
official_url: https://education.ec.europa.eu/sites/default/files/document-library-docs/ects-users-guide_en.pdf
repository_url: n/a
version: ECTS Users' Guide 2015
publication_date: 2015
last_updated: unknown
legal_status: guia; correspondência 60 créditos/ano "often formalised by national legal provisions"
mandatory_scope: nacional
education_levels: ensino superior
geographic_scope: EHEA
language: multilíngue
license: unknown
technical_formats: n/a (no ELM, elm:CreditPoint com framework "Educational credit system")
api_available: n/a
data_model_available: n/a
ontology_available: lista controlada "Educational credit system"
schemas_available: n/a
implementation_examples: elm:creditPoint
related_standards: [eu-elm, eu-ewp-emrex]
entities: CreditPoint (sistema + valor)
relationships: crédito atribuído à especificação de aprendizagem
vocabularies: Educational credit system
core_relevance: baixa (educação básica não usa crédito) [I]
regional_adapter_relevance: baixa
limitations: só superior
open_questions: n/a
sources: [S-UE-18]
access_date: 2026-11-05
research_status: parcial (PDF oficial não aberto; dado de 60 créditos e 1.500–1.800 h/ano por cópia BFUG)
```

60 créditos por ano letivo em tempo integral; carga anual de 1.500 a 1.800 horas, isto é, 25 a 30 horas por crédito [S-UE-18].

## Erasmus Without Paper (EWP) e EMREX/ELMO

```yaml
id: eu-ewp-emrex
name: Erasmus Without Paper network; EMREX; ELMO
acronym: EWP / EMREX / ELMO
jurisdiction: UE (Erasmus+, European Student Card Initiative)
issuing_organization: Comissão Europeia + consórcios de projetos
reference_type: rede e APIs de intercâmbio (EWP); serviço controlado pelo estudante (EMREX); formato XML (ELMO)
domain: [D3, D8]
official_url: not_found em domínio europa.eu nesta sessão
repository_url: https://github.com/emrex-eu/elmo-schemas (citado no README do ELM)
version: unknown
publication_date: unknown
last_updated: unknown
legal_status: uso exigido em processos Erasmus+ (não verificado em ato normativo)
mandatory_scope: instituições de ensino superior em mobilidade Erasmus+ [não verificado]
education_levels: ensino superior
geographic_scope: UE
language: inglês
license: unknown
technical_formats: [XML (ELMO), APIs REST da rede EWP]
api_available: sim (EWP)
data_model_available: sim (ELMO)
ontology_available: não
schemas_available: sim (XSD ELMO)
implementation_examples: unknown
related_standards: [eu-elm (mapeado a ELMO), eu-ects]
entities: Learner, Report, LearningOpportunitySpecification/Instance (ELMO) [I]
relationships: n/a
vocabularies: n/a
core_relevance: baixa
regional_adapter_relevance: baixa
limitations: só superior
open_questions: "European Higher Education Interoperability Framework" como documento formal: not_found; os componentes concretos são EWP, EMREX, ESC
sources: [S-UE-01, S-UE-19]
access_date: 2026-11-05
research_status: ficha curta
```

O README do ELM declara o modelo "aligned with, and fully mapped to, the ELMO/EMREX Standard" [S-UE-01]. EWP é rede de troca de dados de mobilidade em tempo real entre instituições; EMREX dá ao estudante o controle do envio de seus registros em formato ELMO (relatórios de avaliação EWP 2023 e white paper 2024, fontes de projeto, não oficiais da Comissão) [S-UE-19].

**Lição [I]:** o padrão EMREX (o titular autoriza a transferência do próprio histórico) é análogo ao que C.CNS + C.CRD precisam para portabilidade de histórico escolar.
