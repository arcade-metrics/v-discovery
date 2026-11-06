# País de Gales: Curriculum for Wales, PLASC e ALN/IDP

```yaml
id: uk-wal-cfw-plasc-aln
name: Curriculum for Wales; Pupil Level Annual School Census (PLASC); Additional Learning Needs (ALN) e Individual Development Plan (IDP)
acronym: CfW / PLASC / ALN / IDP
jurisdiction: País de Gales
issuing_organization: Welsh Government
reference_type: currículo nacional (framework em legislação + guias) + coleta anual + sistema legal de ALN
domain: [D1, D2, D4, D7]
official_url: https://hwb.gov.wales/curriculum-for-wales/ ; https://www.gov.wales/pupil-level-annual-school-census-plasc-technical-completion-notes
repository_url: n/a
version: "PLASC janeiro de 2026 (technical completion notes); ALN Code for Wales 2021"
publication_date: notas PLASC 2026-01
last_updated: unknown
legal_status: currículo em legislação (Curriculum and Assessment (Wales) Act 2021 [I: nome não confirmado na página]); ALN sob Additional Learning Needs and Education Tribunal (Wales) Act 2018; PLASC sob regulamentos de informação sobre alunos, emendados em 2026 para alinhar ao ALN
mandatory_scope: escolas mantidas
education_levels: 3–16 (currículo); PLASC: nursery, primary, middle, secondary, special
geographic_scope: País de Gales
language: inglês e galês
license: unknown
technical_formats: [PDF (notas), arquivo de coleta de MIS]
api_available: não
data_model_available: parcial (campos PLASC)
ontology_available: não
schemas_available: not_found
implementation_examples: n/a
related_standards: [uk-identificadores (UPN vale para Inglaterra e País de Gales), uk-eng-send-ehcp]
entities: Pupil, School, ALN provision, Additional need, IDP
relationships: aluno 1 situação de ALN (N/C/L); 1..n necessidades adicionais
vocabularies: Pupil ALN provision (N, C, L); Additional needs (DYSL, DYSC, DYSP, ADHD, MLD, SLD, PMLD, BESD, SLCD, HI, VI, MSI, PMED, ASD, DNA)
core_relevance: alta para D7 (quem mantém o plano)
regional_adapter_relevance: alta
limitations: Curriculum for Wales dá autonomia às escolas para desenhar o próprio currículo; não há lista nacional de objetivos codificados [I]
open_questions: estrutura de progressão (passos 1–5) e áreas não confirmadas em fonte primária nesta sessão (páginas hwb devolveram 404)
sources: [S-UK-14, S-UK-15]
access_date: 2026-11-05
research_status: parcial (PLASC verificado; currículo parcial)
```

## Curriculum for Wales

Framework nacional com requisitos em legislação e guias: introdução (quatro propósitos), áreas de aprendizagem e experiência, **statements of what matters**, **principles of progression**, **descriptions of learning**, guia de avaliação; frameworks transversais de letramento, numeracia (LNF) e competência digital (DCF) [S-UK-14]. [I, não verificado nesta sessão] Seis Areas of Learning and Experience (Expressive Arts; Health and Well-being; Humanities; Languages, Literacy and Communication; Mathematics and Numeracy; Science and Technology) e cinco **progression steps** relacionados de forma ampla às idades 5, 8, 11, 14 e 16; implantação a partir de setembro de 2022.

[I] Para o Core: progressão por **passos** não amarrados a ano; currículo de escola derivado do framework nacional (C.CFW institucional derivado de C.CFW nacional via C.CAS).

## PLASC 2026 e ALN

Dia do censo: **20 de janeiro de 2026** [S-UK-15]. O sistema ALN substituiu o SEN em quatro anos (setembro de 2021 a agosto de 2025); os itens SEN foram removidos após agosto de 2025 e os novos itens ALN são "largely a terminology change" [S-UK-15].

| Campo | Valores | Regra |
|---|---|---|
| Pupil ALN provision (1 car., obrigatório) | `N` sem ALN; `C` IDP mantido pela escola; `L` IDP mantido pela autoridade local | IDPs anteriores ao ALN Act não podem ser `C`/`L`; branco inválido |
| Additional needs (4 car., obrigatório) | DYSL, DYSC, DYSP, ADHD (SPLD); MLD; SLD; PMLD; BESD; SLCD; HI; VI; MSI; PMED; ASD; DNA (não se aplica) | uma categoria por aluno no mínimo, inclusive com IDP |

Desenvolvimentos futuros anunciados: dados individuais de crianças com ALN em outros contextos, dados de provisão e de pessoal ALN [S-UK-15].

### Lição para o Core (D7) [I]

O País de Gales torna explícito **quem mantém o plano** (escola × autoridade local) como o próprio valor do código. C.PLN precisa de `maintained_by` (C.ORG) e o adaptador deriva o código. Note também que "ADHD" aparece como subcategoria de dificuldade específica aqui, mas não como tipo próprio na Inglaterra (CS071): categorias não são equivalentes entre as nações do UK.
