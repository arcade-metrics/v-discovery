# Ficha: registro (备案) de aplicativos educacionais — 教技厅〔2019〕3号 e 教技函〔2019〕55号

```yaml
id: cn.apps-educacionais-2019
name: 教育移动互联网应用程序备案管理办法 (Medidas de registro de apps móveis educacionais) + 教育部等八部门关于引导规范教育移动互联网应用有序健康发展的意见 (Parecer de oito ministérios)
acronym: 教技厅〔2019〕3号; 教技函〔2019〕55号
jurisdiction: China
issuing_organization: Escritório Geral do MOE (medidas) [C21]; MOE e mais sete órgãos (parecer) [C22]
reference_type: regulamento ministerial (规范性文件) + parecer de política
domain: [D8, D6]
official_url: http://www.moe.gov.cn/srcsite/A16/s3342/201911/t20191122_409333.html
repository_url: n/a
version: 2019
publication_date: medidas 2019-11-13 [C21]; parecer 2019 (教技函〔2019〕55号; data exata unknown, publicado pela CAC em 2019-09-05) [C22]
last_updated: unknown (vigência atual não confirmada; ver QA-19)
legal_status: vigente presumido; nenhuma revogação localizada
mandatory_scope: apps "com professores, alunos e pais como usuários principais e ensino/aprendizagem como cenário principal" (art. 2) [C21]
education_levels: todos
geographic_scope: nacional ("一省备案，全国有效")
language: chinês
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: plataforma de registro http://app.eduyun.cn (国家数字教育资源公共服务体系) [C21]
related_standards: [CSL art. 21 (等级保护), ICP备案, PIPL]
entities: [prestador (提供者), usuário institucional (使用者: órgão ou escola), app]
relationships: prestador 1—N apps; escola usa só app registrado e registra o uso
vocabularies: "自研自用" (desenvolvido e usado internamente)
core_relevance: nenhuma (é obrigação de operação)
regional_adapter_relevance: alta (pré-condição de entrada)
limitations: o texto integral das medidas não foi lido além dos artigos citados
open_questions: [QA-19]
sources: [C21, C22]
access_date: 2026-11-05
research_status: aviso e artigos 2, 9, 11, 13, 14 verificados
```

## Requisitos [C21, C22]

1. **Antes** do registro de prestador: **ICP备案** e **网络安全等级保护定级备案** (art. 9). Depois do período de transição (até 2020-01-31), registro sem esses dois é cancelado (aviso, item 三).
2. Registro de prestador na província do domicílio; vale no país; subsidiárias registram pela matriz (art. 11). Verificação em 10 dias úteis (arts. 13–14); número de registro **exibido no app** (art. 14).
3. Escolas e órgãos fazem **registro de uso** e escolhem apenas apps registrados (aviso; resumo do art. 8 em trecho).
4. Lojas de apps devem tratar o registro educacional como condição importante para publicação (parecer, item 十三).
5. Dados (parecer, item 六): mecanismo de proteção em coleta, armazenamento, transmissão e uso; **"后台实名、前台自愿"**; consentimento do responsável para dados de menores; proibido coletar dado não relacionado ao serviço; apps para menores limitam tempo de uso e indicam faixa etária (item 五).
6. Integração (parecer, item 十二): "鼓励" validar os dados de instituições, professores e alunos com a base nacional e **consolidá-los na 国家教育基础数据库** (base nacional de dados educacionais básicos).

## Efeito para a VUOO [I]

- O registro exige ICP备案, que exige servidor no território e entidade local (regras de ICP não lidas; QA-20).
- O item 十二 é incentivo, não obrigação: a VUOO China pode ser pressionada a sincronizar com a base nacional, o que reforça ter o Core com importação/exportação nos formatos JY/T 0633.
