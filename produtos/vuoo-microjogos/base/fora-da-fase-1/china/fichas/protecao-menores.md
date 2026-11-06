# Ficha: 未成年人网络保护条例 (2023) e 未成年人保护法 art. 72 (Proteção on-line de menores)

```yaml
id: cn.protecao-menores
name: 未成年人网络保护条例 (Regulamento de proteção de menores on-line) + 中华人民共和国未成年人保护法 (Lei de Proteção de Menores)
acronym: Decreto do Conselho de Estado nº 766; MPL
jurisdiction: China
issuing_organization: Conselho de Estado (regulamento) [C17]; Comitê Permanente da APN (lei) [C18]
reference_type: regulamento administrativo (行政法规) + lei
domain: [D8, D3, D6]
official_url: http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/202310/t20231025_1087333.html
repository_url: n/a
version: regulamento 2023; lei rev. 2020 (alterada em 2024, trecho)
publication_date: regulamento aprovado em 2023-09-20 [C17]
last_updated: unknown
legal_status: regulamento vigente desde 2024-01-01 [C17]; lei vigente
mandatory_scope: prestadores de produtos e serviços de rede, controladores de dados, fabricantes de terminais, escolas, famílias
education_levels: menores de 18 anos
geographic_scope: nacional
language: chinês
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [PIPL, CSL, 儿童个人信息网络保护规定 (CAC 2019, trecho C30)]
entities: [menor, responsável, prestador de serviço, escola]
relationships: responsável exerce direitos do menor
vocabularies: n/a
core_relevance: alta (C.CNS, C.GRD, auditoria, acesso)
regional_adapter_relevance: alta
limitations: texto completo da lei não aberto (art. 72 só por trecho)
open_questions: [QA-18]
sources: [C17, C18, C30]
access_date: 2026-11-05
research_status: regulamento verificado no site do MOE; lei por trecho
```

## Artigos relevantes do regulamento [C17]

| Art. | Regra | Efeito [I] |
|---|---|---|
| 13, 16 | escolas incluem letramento digital; regras de uso de rede e terminais na escola | contexto de uso, não obrigação da VUOO |
| 20 | plataforma com **número muito grande de menores** ou influência relevante: avaliações periódicas de impacto, **modo menor/área para menores**, sistema de conformidade com **órgão independente majoritariamente externo**, regras específicas da plataforma, relatório anual de responsabilidade social; critério de "grande número" a ser definido pela CAC | depende de escala |
| 28 | serviços de **educação on-line para menores**: produtos adequados à idade e à capacidade cognitiva | adequação por faixa etária precisa estar no modelo (C.PRG/idade) |
| 31 | serviços de publicação de informação e **mensagens instantâneas** para menores exigem **identidade real** do menor ou do responsável; sem isso, não prestar o serviço | chat e mural exigem verificação |
| 33–34 | responsável orienta o menor; controlador oferece meios fáceis de consulta, cópia, correção, complemento, **exclusão** e portabilidade a pedido do menor ou do responsável; recusa por escrito com motivo | painel do responsável |
| 35 | incidente com dados de menor: plano de resposta, **aviso à CAC** e aos menores e responsáveis | |
| 36 | **mínimo privilégio**; acesso de funcionário a dado de menor com **aprovação** e **registro** | trilha de acesso aprovada, não só log |
| 37 | **auditoria anual de conformidade** do tratamento de dados de menores, relatada à CAC | |
| 38 | informação privada publicada por menor: aviso e bloqueio | moderação |
| 43 | jogos, transmissão ao vivo, áudio/vídeo, redes sociais: **modo menor** com limites de horário, duração, função e conteúdo e ferramentas para o responsável | gamificação da VUOO pode ser lida como "jogo" (unknown) |

**Lei de Proteção de Menores, art. 72** (trecho, C18): tratamento on-line de dados de menores segue legalidade, legitimidade e necessidade; para menores de 14, consentimento dos pais ou responsável, salvo lei; correção e exclusão a pedido.

**Educação APP (C22, item 六)**: "后台实名、前台自愿" (identidade real no servidor, pseudônimo na interface); coleta de dados de menores com consentimento e autorização do responsável; proibido coletar dado sem relação com o serviço.
