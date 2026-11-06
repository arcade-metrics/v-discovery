# Ficha: acesso ao mercado — Lista Negativa de investimento estrangeiro (2024) e política "双减" (2021)

> Duas referências curtas reunidas porque ambas determinam **quem pode operar** a VUOO na China, não como o dado é modelado.

```yaml
id: cn.acesso-ao-mercado
name: 外商投资准入特别管理措施（负面清单）（2024年版） + 关于进一步减轻义务教育阶段学生作业负担和校外培训负担的意见
acronym: Lista Negativa 2024; 双减
jurisdiction: China
issuing_organization: NDRC e MOFCOM (lista, Ordem nº 23) [C23]; Escritório Geral do Comitê Central do PCCh e do Conselho de Estado (双减) [C24]
reference_type: regulamento ministerial (lista) + documento de política central (意见)
domain: [D8]
official_url: https://www.ndrc.gov.cn/xxgk/zcfb/fzggwl/202409/P020240907514493057643.pdf ; https://www.gov.cn/zhengce/2021-07/24/content_5627132.htm
repository_url: n/a
version: lista 2024; 双减 2021
publication_date: lista 2024-09 (vigência 2024-11-01, trecho); 双减 2021-07-24 [C23, C24]
last_updated: unknown (versão posterior da lista não verificada)
legal_status: vigentes (presumido)
mandatory_scope: investimento estrangeiro; formação extracurricular para a educação obrigatória
education_levels: obrigatória (双减); todas (lista)
geographic_scope: nacional (zonas de livre comércio têm lista própria, não lida)
language: chinês
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [regras de licença ICP/telecom (não lidas)]
entities: n/a
relationships: n/a
vocabularies: n/a
core_relevance: nenhuma
regional_adapter_relevance: alta (estrutura societária e oferta)
limitations: classificação da VUOO (ferramenta escolar × serviço de formação × telecom de valor agregado) não verificada com regulador
open_questions: [QA-20, QA-21]
sources: [C23, C24]
access_date: 2026-11-05
research_status: itens relevantes verificados
```

## Regras

| Fonte | Item | Regra |
|---|---|---|
| Lista Negativa 2024 [C23] | 12 | telecom de valor agregado: capital estrangeiro **≤ 50%** (exceto comércio eletrônico, comunicação multipartite doméstica, armazenamento e reenvio, call center) |
| | 13 | proibido investimento estrangeiro em notícias on-line, **publicação em rede**, audiovisual on-line, cultura on-line (trecho da linha, não lido por inteiro) |
| | 20 | pré-escola, médio e superior: só cooperação sino-estrangeira com controle chinês |
| | 21 | **proibido investir em instituições de educação obrigatória** |
| 双减 [C24] | 13 | instituições de reforço de disciplinas (学科类): não abrem capital; **capital estrangeiro não pode controlar nem participar** (aquisição, gestão, franquia, VIE); instituições on-line passam de registro a **aprovação** |
| | 14 | **proibido oferecer cursos estrangeiros**; proibido contratar estrangeiros fora da China para ministrar formação |

## Efeito para a VUOO [I]

- A VUOO é plataforma para escolas, não escola: o item 21 não a atinge diretamente; mas se operar como serviço de internet com receita, precisa de licença de telecom de valor agregado, com teto de 50% de capital estrangeiro.
- Se a VUOO oferecer conteúdo de disciplina **diretamente a famílias** de alunos da educação obrigatória, fora da escola, pode ser enquadrada como formação on-line de disciplinas: aprovação prévia e proibição de capital estrangeiro. O modelo seguro é vender só a escolas/órgãos (B2G/B2B) por meio de parceiro local.
- "Proibido oferecer cursos estrangeiros" pesa sobre conteúdo curricular trazido de fora: o adaptador China deve operar com currículo chinês e conteúdo revisado localmente.
