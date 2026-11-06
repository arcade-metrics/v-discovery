# Ficha: 促进和规范数据跨境流动规定 (Regras para promover e regular o fluxo transfronteiriço de dados, CAC 2024)

```yaml
id: cn.transferencia-2024
name: 促进和规范数据跨境流动规定 (Provisions on Promoting and Regulating Cross-Border Data Flows)
acronym: Ordem CAC nº 16
jurisdiction: China
issuing_organization: Administração do Ciberespaço da China (国家互联网信息办公室, CAC) [C19]
reference_type: regulamento ministerial (部门规章)
domain: [D8]
official_url: https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
repository_url: n/a
version: 2024
publication_date: 2024-03-22 (aprovado 2023-11-28) [C19]
last_updated: unknown
legal_status: vigente desde a publicação; prevalece sobre as medidas de avaliação (2022) e de contrato-padrão (2023) em caso de conflito (art. 13) [C19]
mandatory_scope: todo processador que envia dados ao exterior
education_levels: todos
geographic_scope: nacional; zonas de livre comércio podem ter lista negativa própria (art. 6)
language: chinês
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [PIPL arts. 38–40, DSL art. 31, CSL art. 37, 数据出境安全评估办法 (2022), 网络数据安全管理条例]
entities: [processador, CIIO, receptor no exterior, dado importante, informação sensível]
relationships: n/a
vocabularies: limiares por número de pessoas
core_relevance: alta (residência e fluxo entre instâncias)
regional_adapter_relevance: alta
limitations: medidas de certificação de 2025 não lidas
open_questions: [QA-16]
sources: [C19]
access_date: 2026-11-05
research_status: artigos 1–3, 5–8, 11, 13 verificados
```

## Regras [C19]

| Situação (não-CIIO, acumulado desde 1º de janeiro) | Mecanismo |
|---|---|
| Dados sem informação pessoal nem dado importante, de comércio, transporte, **cooperação acadêmica** etc. (art. 3) | isento |
| Necessário para contrato do qual o indivíduo é parte (inclui "考试服务"), RH transfronteiriço, emergência (art. 5, I–III) | isento |
| < 100 mil pessoas, **sem informação sensível** (art. 5, IV) | isento |
| 100 mil–1 milhão de pessoas (não sensível) **ou < 10 mil pessoas com informação sensível** (art. 8) | contrato-padrão ou certificação |
| ≥ 1 milhão de pessoas, ou **≥ 10 mil com informação sensível**, ou qualquer **dado importante** (art. 7) | avaliação de segurança da CAC via CAC provincial |
| CIIO: qualquer informação pessoal ou dado importante (art. 7) | avaliação de segurança |

Dado importante: só precisa ser declarado como tal se assim indicado por autoridade ou publicado (art. 2).

## Efeito para a VUOO [I]

- Como dados de menores de 14 são sensíveis (PIPL art. 28), **qualquer** envio de dados de alunos do primário ao exterior, por menor que seja, cai no art. 8 (contrato-padrão ou certificação) e, a partir de 10 mil alunos/ano, no art. 7 (avaliação de segurança da CAC). Soma-se o consentimento separado dos responsáveis (PIPL art. 39) e a proibição de fornecer dados de 学籍 sem aprovação (学籍 art. 24).
- Na prática, processar dados de alunos chineses numa instância fora da China é inviável para uma operação escolar de porte; a instância China deve ser autônoma e só exportar conteúdo não pessoal (currículo, itens, recursos) e, com cautela, agregados não classificados como importantes.
