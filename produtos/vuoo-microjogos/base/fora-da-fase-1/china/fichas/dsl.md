# Ficha: 中华人民共和国数据安全法 (Lei de Segurança de Dados)

```yaml
id: cn.dsl
name: 中华人民共和国数据安全法 (Data Security Law)
acronym: DSL
jurisdiction: China
issuing_organization: Comitê Permanente da APN [C14]
reference_type: lei
domain: [D8]
official_url: https://www.cac.gov.cn/2021-06/11/c_1624994566919140.htm
repository_url: n/a
version: 2021
publication_date: 2021-06-10 [C14]
last_updated: not_found
legal_status: vigente desde 2021-09-01 (art. 55) [C14]
mandatory_scope: tratamento de dados no território (art. 2); todos os dados, não só pessoais
education_levels: todos
geographic_scope: nacional (com alcance extraterritorial em casos de dano à China, não detalhado aqui)
language: chinês
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: JY/T 0661-2025 (classificação setorial da educação)
related_standards: [PIPL, CSL, 网络数据安全管理条例, GB/T 43697-2024, JY/T 0661-2025]
entities: [dado, dado importante, dado central nacional, catálogo de dados importantes]
relationships: setor → catálogo de dados importantes
vocabularies: núcleo / importante / geral
core_relevance: alta (rótulo de classificação por conjunto)
regional_adapter_relevance: alta
limitations: catálogo de dados importantes da educação não localizado publicamente (a JY/T 0661 descreve o processo)
open_questions: [QA-11]
sources: [C14, C05]
access_date: 2026-11-05
research_status: artigos relevantes verificados
```

## Artigos relevantes [C14]

| Art. | Regra |
|---|---|
| 21 | sistema de classificação e graduação de dados; catálogo de dados importantes; "dados centrais nacionais" com gestão mais rígida; cada região e setor define seu catálogo |
| 31 | saída de dados importantes: CIIO segue a CSL; demais seguem medidas da CAC |
| 36 | não fornecer dados armazenados na China a autoridades judiciais/policiais estrangeiras sem aprovação |

Efeito [I]: a educação é setor-chave (JY/T 0661, introdução: "教育作为数据安全法确定的八大重点行业领域之一") [C05]; dados agregados de muitas escolas podem virar "importantes" e ficar presos ao território, mesmo sem dado pessoal.
