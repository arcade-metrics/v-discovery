# SEND Code of Practice e EHC plan como dado (Inglaterra)

```yaml
id: uk-eng-send-ehcp
name: Special educational needs and disability code of practice 0 to 25 years; EHC plan; SEN no School Census e no SEN2
acronym: SEND CoP / EHCP
jurisdiction: Inglaterra
issuing_organization: DfE e Department of Health
reference_type: statutory guidance (CoP) sob Children and Families Act 2014 e SEND Regulations 2014; itens de dados CBDS
domain: [D7, D3, D1]
official_url: https://www.gov.uk/government/publications/send-code-of-practice-0-to-25
repository_url: n/a
version: "CoP de janeiro de 2015 (PDF SEND_Code_of_Practice_January_2015.pdf); dados: CBDS May 2026"
publication_date: 2015-01
last_updated: unknown
legal_status: CoP é guia estatutário (dever de considerar); EHC plan é instrumento legal (s.37 Children and Families Act 2014; reg. 12 SEND Regulations 2014)
mandatory_scope: LAs, escolas, provedores de EY, colégios FE
education_levels: 0 a 25 anos
geographic_scope: Inglaterra
language: inglês
license: unknown
technical_formats: [PDF (CoP); XLSX (CBDS)]
api_available: não
data_model_available: parcial (itens CBDS e coleta SEN2 da LA)
ontology_available: não
schemas_available: via especificações de coleta
implementation_examples: n/a
related_standards: [uk-eng-cbds, uk-eng-school-census, uk-wal-cfw-plasc-aln, uk-sco-cfe-census]
entities: SEN provision, SEN type (need), EHC plan (seções A–K), EHC needs assessment, setting
relationships: aluno tem 0..1 provisão vigente; 0..2 tipos ranqueados (censo); 0..1 EHC plan mantido por uma LA
vocabularies: CS096 SEN provision; CS071 SEN type; CS077 special school type; CS110 SEN setting; CS113 motivo de cessação; CS124 origem do pedido
core_relevance: muito alta para D7
regional_adapter_relevance: muito alta
limitations: tipos de necessidade são categorias majoritariamente diagnósticas; o plano completo não é dado estruturado nacional (só datas, cessação, setting)
open_questions: reforma do sistema SEND anunciada após 2025 não verificada
sources: [S-UK-11, S-UK-02, S-UK-04]
access_date: 2026-11-05
research_status: verificado (CoP e CBDS)
```

## Análise

**Quatro áreas amplas de necessidade** (CoP 5.32 e 6.28 ss.): communication and interaction; cognition and learning; social, emotional and mental health; sensory and/or physical needs [S-UK-11]. O CoP diz que as áreas dão "an overview of the range of needs" (6.27); a abordagem graduada tem quatro etapas: **assess, plan, do, review** [S-UK-11].

**EHC plan: seções obrigatórias** (CoP 9.62; s.37 CFA 2014; reg. 12 SEND Regulations 2014), separadamente rotuladas, formato local [S-UK-11]:

| Seção | Conteúdo |
|---|---|
| A | visões, interesses e aspirações da criança e dos pais / do jovem |
| B | necessidades educacionais especiais |
| C | necessidades de saúde relacionadas à SEN |
| D | necessidades de assistência social relacionadas à SEN |
| E | resultados (outcomes) buscados |
| F | provisão educacional especial requerida |
| G | provisão de saúde |
| H1 / H2 | provisão de assistência social (H1 sob a seção 2 do CSDPA 1970; H2 outra) |
| I | nome e tipo da escola/instituição |
| J | orçamento pessoal (Personal Budget), se houver |
| K | pareceres e informações reunidos na avaliação |

**Como dado nacional** (CBDS) [S-UK-02]:
- *Provisão* (CS096): `N` sem SEN; `K` SEN Support; `E` EHC plan; históricos `S` statement, `A` School/Early Years Action, `P` Action Plus (só em `<SENhistory>` do CTF).
- *Tipo* (CS071): SPLD, MLD, SLD, PMLD, SEMH, SLCN, HI, VI, MSI, PD, ASD, **DS** (Down Syndrome), OTH, NSA (SEN support sem avaliação especializista; não se aplica ao SEN2).
- *Ranking* N00024: 1 = principal; censo aceita até 2 tipos [S-UK-04].
- *Unidade/recurso*: membro de SEN unit (N00022) ou resourced provision (N00023).
- *Ciclo do plano* (coleta SEN2 das LAs): origem do pedido de avaliação (CS124), data de decisão de revisão anual (N00720), rascunho de plano emendado (N00796), cessação e motivo (N00715/N00716, CS113), setting quando não há UPN/UKPRN (CS110: educação domiciliar eletiva, NEET 16–25 etc.).

### Lições para o Core (D7) [I]

1. **Três camadas separadas**: (a) nível de provisão/apoio (N/K/E) é um **estado do aluno com vigência**; (b) tipo de necessidade é **classificação ranqueada** e opcional (NSA = "apoio sem avaliação de tipo"), o que permite apoiar sem rotular; (c) o plano individual (EHC) é **documento legal com seções fixas**, mantido por uma organização (LA), com ciclo de vida (pedido, avaliação, emissão, revisão anual, emenda, cessação, transferência).
2. C.SUP deve aceitar "necessidade sem categoria" e ranking; C.PLN deve ter `maintained_by` (C.ORG), seções tipadas (visões do estudante, resultados, provisão por setor: educação, saúde, social) e eventos de ciclo de vida.
3. A seção E (outcomes) liga o plano a resultados, o que aproxima C.PLN de C.CMP/C.RES.
4. Categorias diagnósticas (ex.: DS, ASD) coexistem com áreas funcionais amplas; o Core deve guardar a categoria local como C.VOC do adaptador, nunca como enum do Core, para não reduzir o estudante a diagnóstico (briefing D7).
