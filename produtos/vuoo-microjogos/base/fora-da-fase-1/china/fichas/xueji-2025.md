# Ficha: 中小学生学籍管理办法 (2025) e 学籍号 (Regulamento do registro escolar de alunos do ensino primário e secundário)

```yaml
id: cn.xueji-2025
name: 中小学生学籍管理办法 (Medidas de gestão do registro escolar de alunos do primário e secundário)
acronym: 教基〔2025〕1号
jurisdiction: China
issuing_organization: Ministério da Educação [C11]
reference_type: regulamento ministerial (规范性文件)
domain: [D1, D3, D8]
official_url: not_found no moe.gov.cn nesta pesquisa; republicação oficial provincial https://edu.gd.gov.cn/zwgknew/jyfzgh/content/post_4664892.html [C11]
repository_url: n/a
version: 2025 (revoga 教基一〔2013〕7号)
publication_date: 2025-01-03 (assinatura); publicado 2025-02-07 [C11]
last_updated: 2025
legal_status: vigente desde a publicação (art. 30) [C11]
mandatory_scope: todas as escolas primárias e secundárias e órgãos educacionais
education_levels: primário, ginásio, médio (pré-escola tem regulamento próprio de 2025, não lido)
geographic_scope: nacional; regras de transferência detalhadas pelas províncias (art. 12)
language: chinês
license: n/a
technical_formats: n/a
api_available: não (sistema nacional fechado, 5 níveis de uso)
data_model_available: não (descreve processos, não campos)
ontology_available: não
schemas_available: não
implementation_examples: 国家中小学生学籍信息管理系统
related_standards: [JY/T 0633-2022, PIPL, JY/T 0661-2025]
entities: [estudante, registro escolar (学籍), escola, transferência, dossiê eletrônico]
relationships: estudante 1—1 学籍 (一人一籍); 学籍 → escola atual; transferência = evento entre escolas
vocabularies: not_found (tipos de mudança de registro definidos pelas províncias)
core_relevance: alta para C.ENR (vínculo com vigência e situação) e C.IDN
regional_adapter_relevance: alta
limitations: formato do 学籍号 não publicado; sem API
open_questions: [QA-05]
sources: [C11, C12]
access_date: 2026-11-05
research_status: artigos relevantes verificados em republicação oficial
```

## Artigos relevantes [C11]

| Art. | Regra |
|---|---|
| 5 | MOE constrói o 国家学籍系统 e o acesso móvel; órgãos e escolas respondem pela **segurança dos dados** de 学籍 |
| 6 | escola coleta os dados com documento de identidade válido e cria o dossiê em 2 meses; "em regra, não se cria dossiê em papel" |
| 8 | "学籍号由国家学籍系统按照有关规则自动生成并分配，一人一号，终身不变" |
| 10 | estrangeiros e HK/Macau/Taiwan registram com documento válido |
| 12 | "一人一籍、籍随人走"; condições de cada mudança fixadas pela província |
| 15 | transferência iniciada pela escola de destino no sistema; 10 dias úteis por instância; transferência interprovincial "一网通办"; pais consultam pelo celular |
| 19 | concluintes permanecem registrados no sistema |
| 23 | sistema centralizado, uso em 5 níveis; cada região tem a gestão e o uso dos seus dados |
| 24 | "**除法律法规有明确规定或经县级以上人民政府批准的，任何学生学籍信息不得向外提供**"; dados fornecidos devem ser desidentificados ou anonimizados; impedir que outros sistemas coletem dados de alunos irregularmente; construir a "identidade digital educacional confiável do estudante" baseada no 学籍 |
| 30 | vigência imediata; revoga o regulamento de 2013 |

**Formato do 学籍号**: não está no regulamento. Fontes secundárias (2016) descrevem prefixo **G** + número do documento (definitivo), **L** (provisório, regra semelhante ao documento) e **J** (sem documento válido) [C12, trecho]. Não verificado em fonte oficial.

## Observações para o Core [I]

- O 学籍 é o vínculo-mestre aluno↔escola com vigência e situação; mapeia para C.ENR (escola) com identificador C.IDN `scheme = cn-xueji`. A VUOO não **emite** 学籍号; só poderia **receber** o número, e o art. 24 limita até isso: a escola não pode passar dados de 学籍 a terceiros sem base legal ou aprovação.
- [I] Consequência de projeto: no adaptador China, a VUOO deve funcionar sem depender do 学籍号 (identificador próprio por instância), aceitando-o só se a escola obtiver autorização; o Core não pode exigir identificador nacional.
- A regra "no máximo 2 meses para criar o dossiê" e "10 dias úteis por transferência" são regras de processo do sistema nacional, não da VUOO.
