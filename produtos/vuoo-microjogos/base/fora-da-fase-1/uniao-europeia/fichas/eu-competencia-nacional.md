# Competência nacional na educação básica, Eurydice e ISCED

```yaml
id: eu-competencia-nacional
name: Divisão de competências UE × Estados-membros na educação; Eurydice / Eurypedia
acronym: Eurydice
jurisdiction: UE (descrição de 40 países em Eurypedia)
issuing_organization: Rede Eurydice (EACEA, Comissão Europeia, e unidades nacionais)
reference_type: base descritiva (não normativa) + diagramas de estruturas educacionais
domain: [D1, D4, D7]
official_url: https://eurydice.eacea.ec.europa.eu/national-education-systems
repository_url: n/a
version: "Eurypedia contínua; diagramas 'The structure of the European education systems' 2025/2026 (atualizado em 2025-09-22)"
publication_date: n/a
last_updated: 2025-09-22 (diagramas 2025/26); edição 2026/27 citada por fonte secundária, não confirmada
legal_status: informativo
mandatory_scope: nenhum
education_levels: da educação infantil ao superior
geographic_scope: 27 Estados-membros + 13 países (Eurypedia)
language: inglês + línguas nacionais
license: unknown
technical_formats: [HTML, ferramenta web interativa]
api_available: not_found
data_model_available: não
ontology_available: não
schemas_available: não
implementation_examples: n/a
related_standards: [ISCED 2011 (UNESCO), eu-eqf]
entities: sistema educacional nacional, nível ISCED, programa
relationships: programa nacional ↔ nível ISCED
vocabularies: ISCED 2011 (lista controlada "International Standard Classification of Education" na coleção Europass)
core_relevance: alta como evidência de que D1 é sempre nacional
regional_adapter_relevance: alta: o "adaptador UE" para escolas é, na prática, 27 adaptadores nacionais [I]
limitations: descritivo; não traz dados nem códigos de sistemas de gestão
open_questions: quais Estados têm padrão de dados escolar publicado (ex.: identificadores nacionais de aluno) não foi levantado
sources: [S-UE-20, S-UE-21, S-UE-22]
access_date: 2026-11-05
research_status: parcial
```

## Análise

**Base jurídica [I, a confirmar no TFUE].** Na UE, o conteúdo do ensino e a organização dos sistemas educativos são de competência dos Estados-membros; a União apoia e coordena (art. 165 TFUE). Por isso os instrumentos europeus (EQF, DigComp, ELM, Europass) são recomendações ou ferramentas voluntárias e **nenhum define dados escolares** (aluno, turma, matrícula, frequência). O texto do art. 165 não foi lido nesta sessão.

**Eurydice.** A Eurypedia descreve sistemas de 40 países (27 UE + Albânia, Bósnia e Herzegovina, Geórgia, Islândia, Liechtenstein, Moldávia, Montenegro, Noruega, Macedônia do Norte, Sérvia, Suíça, Turquia, Ucrânia), da educação infantil ao superior, numa estrutura comum de 14 capítulos; há páginas próprias para provisão separada de necessidades educacionais especiais [S-UE-20]. Os diagramas de estrutura 2025/2026 cobrem 39 sistemas em 37 países, atualizados em 2025-09-22, separados em "educação infantil até pós-secundário não terciário" e "terciário (ISCED 5–8)" [S-UE-21].

**ISCED.** Os diagramas da Eurydice usam ISCED para alinhar programas nacionais; o ELM usa ISCED-F 2013 para áreas (`elm:ISCEDFCode`) e a coleção Europass tem lista controlada ISCED [S-UE-02, S-UE-05]. A ficha da ISCED é da pasta `internacional/`.

**O que não é harmonizado:** identificadores de aluno e escola, calendário, organização de turmas, códigos de necessidades educacionais especiais, censos escolares. [I] A Agência Europeia para Necessidades Especiais e Educação Inclusiva (EASIE) coleta dados comparativos, mas por definição operacional própria; não verificado nesta sessão.

**Lição para o Core [I]:** C.PRG precisa de dois atributos separados: o rótulo local (ano/série nacional) e o nível ISCED como C.VOC externo. Nenhum adaptador europeu pode assumir um único esquema de ano escolar.
