# UK GDPR, Data Protection Act 2018, Data (Use and Access) Act 2025 e Children's Code

```yaml
id: uk-gdpr-dpa-childrens-code
name: UK GDPR; Data Protection Act 2018; Data (Use and Access) Act 2025; ICO Age Appropriate Design Code (Children's code)
acronym: UK GDPR / DPA 2018 / DUAA / AADC
jurisdiction: Reino Unido (as quatro nações)
issuing_organization: Parlamento do UK; Information Commissioner's Office (código)
reference_type: lei (UK GDPR, DPA 2018, DUAA 2025) + código de prática estatutário (AADC, s.123 DPA 2018)
domain: [D8, D7]
official_url: https://www.legislation.gov.uk/ukpga/2018/12/contents ; https://www.legislation.gov.uk/ukpga/2025/18/section/81 ; https://ico.org.uk/
repository_url: n/a
version: "DPA 2018 consolidado; DUAA 2025 com comencement principal em 2026 (SI 2026/82)"
publication_date: DPA 2018; DUAA 2025
last_updated: 2026 (comencement do DUAA; guias ICO atualizados em 2026)
legal_status: obrigatório
mandatory_scope: todo tratamento de dados pessoais no UK; AADC para serviços da sociedade da informação "likely to be accessed by children"
education_levels: todos
geographic_scope: Reino Unido
language: inglês
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [eu-gdpr]
entities: n/a
relationships: n/a
vocabularies: 15 padrões do AADC; faixas etárias 0-5, 6-9, 10-12, 13-15, 16-17
core_relevance: alta (C.CNS, privacidade por padrão, idade)
regional_adapter_relevance: alta
limitations: n/a
open_questions: texto de s.9 DPA 2018 e s.81 DUAA não lidos diretamente nesta sessão
sources: [S-UK-18, S-UK-19, S-UK-20]
access_date: 2026-11-05
research_status: apontado + atualização
```

## Análise

**Dono do fato:** `conhecimento/privacidade-seguranca-e-governanca/legal-framework/gdpr-k-and-coppa.md` (`psg.legal.gdpr-k-and-coppa`) já descreve o AADC: 15 padrões (best interests of the child, DPIA, age appropriate application, transparency, detrimental use of data, policies and community standards, default settings, data minimisation, data sharing, geolocation, parental controls, profiling, nudge techniques, connected toys and devices, online tools), abordagem de risco para age assurance e faixas etárias do anexo B [S-UK-18].

**O que esta ficha acrescenta:**

1. **Idade de consentimento digital no UK = 13 anos** (s.9 DPA 2018 adapta o art. 8 do UK GDPR) [I: conhecimento prévio; texto não lido nesta sessão].
2. **Data (Use and Access) Act 2025, s.81** ("data protection by design: children's higher protection matters"): controladores de serviços da sociedade da informação provavelmente acessados por crianças devem considerar como as crianças podem ser mais bem protegidas e apoiadas e que merecem proteção específica; em vigor por regulamento de comencement de 2026 (SI 2026/82); o ICO atualizou o guia de "data protection by design" e, em 15/05/2026, o guia de dados de crianças [S-UK-19, busca; fontes jurídicas secundárias].
3. **Dados escolares**: as coletas estatutárias têm base legal própria (ex.: s.537A Education Act 1996 na Inglaterra) [S-UK-04]; o UPN tem uso restrito ao contexto educacional [S-UK-02].
4. [I] Fora do UK GDPR, cada nação tem base legal própria para seus censos; o Core não deve assumir uma única base legal por "país".

**Para o Core [I]:** C.CNS precisa de `jurisdiction` (nação, não país), idade-limite configurável e registro de DPIA por funcionalidade; configuração "high privacy by default" (AADC padrão 7) como padrão do produto, não como opção.
