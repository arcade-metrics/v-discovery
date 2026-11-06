# National Curriculum in England

```yaml
id: uk-eng-national-curriculum
name: The national curriculum in England (framework for key stages 1 to 4)
acronym: NC
jurisdiction: Inglaterra
issuing_organization: Department for Education
reference_type: currículo nacional (statutory guidance; programmes of study)
domain: [D2, D4]
official_url: https://www.gov.uk/government/collections/national-curriculum
repository_url: n/a
version: "framework de 2014-12-02 (programmes of study de 2013/2014); revisão anunciada"
publication_date: 2014-12-02 (framework KS1–4)
last_updated: unknown
legal_status: obrigatório para escolas mantidas pela LA ("All local-authority-maintained schools in England must teach these programmes of study"); academies não cobertas pela frase da página
mandatory_scope: escolas mantidas pela LA
education_levels: key stages 1 a 4 (anos 1 a 11); EYFS é framework separado
geographic_scope: Inglaterra
language: inglês
license: unknown ([I] OGL)
technical_formats: [PDF, HTML]
api_available: not_found
data_model_available: não
ontology_available: não
schemas_available: não
implementation_examples: n/a
related_standards: [uk-eng-cbds (CS037 key stage, CS086 year group)]
entities: Key stage, Year group, Subject, Programme of study, Attainment target
relationships: key stage contém anos; disciplina tem programme of study por key stage
vocabularies: key stage (CBDS CS037), NC year group (CS086)
core_relevance: média (estrutura curricular por estágio, não por ano)
regional_adapter_relevance: alta
limitations: não legível por máquina; sem códigos oficiais de objetivos (diferente da BNCC); revisão em curso
open_questions: estrutura e formato do novo currículo (publicação prevista primavera/2027; não verificado em fonte primária)
sources: [S-UK-08, S-UK-10, S-UK-02]
access_date: 2026-11-05
research_status: parcial
```

## Análise

A coleção oficial reúne o framework KS1–4 (statutory guidance de 2014-12-02) e os programmes of study por disciplina, a maioria "Statutory guidance"; PSHE e religious education aparecem como "Guidance"; a obrigação declarada é para escolas mantidas pela autoridade local [S-UK-08].

**Estrutura** [I, por conhecimento prévio e códigos CBDS]: Early Years Foundation Stage (nursery/reception), KS1 (anos 1–2), KS2 (anos 3–6), KS3 (7–9), KS4 (10–11). O CBDS codifica key stage de turma (CS037: F, 1, 2, 3, M) e ano curricular (CS086: E1, E2, N1, N2, R, 1–14, M, X) [S-UK-02].

**Legibilidade por máquina:** not_found. Os programmes of study são texto; não há identificadores oficiais por objetivo. [I] Um adaptador teria de cunhar identificadores e registrar proveniência, como o Brasil fez fora do governo com a BNCC (`brasil/bncc-dados/`).

**Revisão curricular.** O relatório final do Curriculum and Assessment Review e a resposta do governo foram publicados em 2025-11-05 (página atualizada em 2025-12-10) [S-UK-10]. Fontes secundárias indicam currículo revisado a publicar na primavera de 2027 para ensino a partir de setembro de 2028 e avaliação estatutária de leitura no ano 8; **não verificado** na resposta oficial (PDF não aberto).

**Para o Core [I]:** C.CFW com versão e vigência (2014 → 2028); C.PRG distingue **estágio** (key stage) de **ano** (year group); o vínculo C.CMP↔C.PRG é por key stage, não por ano, o que o Core deve aceitar (alinhamento a faixa de anos).
