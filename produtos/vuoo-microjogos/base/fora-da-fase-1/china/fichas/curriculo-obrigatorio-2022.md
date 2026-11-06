# Ficha: 义务教育课程方案和课程标准（2022年版） (Plano e padrões curriculares da educação obrigatória, ed. 2022)

```yaml
id: cn.curriculo-obrigatorio-2022
name: 义务教育课程方案和课程标准（2022年版）
acronym: 课程方案 2022 + 16 课程标准
jurisdiction: China
issuing_organization: Ministério da Educação; aviso 教材〔2022〕2号 [C25]
reference_type: documento curricular oficial (plano + padrões por disciplina)
domain: [D2, D4, D1 (carga horária), D5 (学业质量)]
official_url: https://www.gov.cn/zhengce/zhengceku/2022-04/21/content_5686535.htm
repository_url: n/a
version: 2022年版
publication_date: aviso de 2022-03-25; divulgado 2022-04-21 [C25, C26 metadados]
last_updated: errata do padrão de matemática "以此为准2022年5月9日" [C25]
legal_status: vigente desde o semestre de outono de 2022 [C25]
mandatory_scope: 国家课程 obrigatório para todos os alunos ("所有学生必须按规定修习") [C26 p. 6]
education_levels: educação obrigatória, anos 1–9
geographic_scope: nacional; províncias fazem plano de implementação e currículo local
language: chinês
license: unknown
technical_formats: PDF (o plano é PDF só de imagem)
api_available: não
data_model_available: não
ontology_available: não
schemas_available: não
implementation_examples: livros didáticos e recursos da smartedu.cn organizados por disciplina/ano/edição/volume [C04]
related_standards: [普通高中课程方案 (não lido), JY/T 0663-2026 (leitura), JY/T 0646-2022]
entities: [plano, padrão de disciplina, disciplina, ano, segmento, competência nuclear, conteúdo, padrão de qualidade acadêmica]
relationships: plano 1—N disciplinas (com anos); disciplina 1—1 padrão; padrão → competências nucleares, conteúdo, qualidade
vocabularies: 3 categorias de currículo; tabela 1 de disciplinas × anos
core_relevance: alta (C.CFW/C.SUB/C.PRG/C.CMP)
regional_adapter_relevance: alta
limitations: nenhuma versão legível por máquina localizada; codificação interna dos padrões não verificada
open_questions: [QA-14, QA-15]
sources: [C25, C26, C04]
access_date: 2026-11-05
research_status: aviso e plano (pp. 2, 4–8, 11–12) verificados; os 16 padrões não lidos
```

## Estrutura verificada

- **Anexos** (17): o plano + 道德与法治, 语文, 历史, 数学, 英语, 日语, 俄语, 地理, 科学, 物理, 化学, 生物学, 信息科技, 体育与健康, 艺术, 劳动 [C25].
- **Categorias** (p. 6): 国家课程 (nacional, desenvolvida pelo MOE, obrigatória), 地方课程 (planejada pela província), 校本课程 (organizada pela escola; em regra escolhida pelo aluno).
- **Organização** (p. 6): "九年一贯设置", arranjo "六三" ou "五四".
- **Disciplinas × anos**: tabela 1 em [../terminologia.md §2.10](../terminologia.md). Regras (p. 7): inglês a partir do 3º ano (opcional antes, oral); no ginásio uma língua estrangeira (inglês, japonês, russo…); ciências 1–9 com opção de física/química/biologia separadas no ginásio; 信息科技 independente nos anos 3–8; artes por linguagens com escolha de pelo menos duas nos anos 8–9; "专题教育" integrada, sem aula própria.
- **Tempo** (p. 8): 39 semanas/ano (35 de aulas novas nos anos 1–8; 33 no 9º); 26 aulas/semana (anos 1–2), 30 (3–6), 34 (7–9); total de 9 522 aulas; 40 min no primário, 45 no ginásio.
- **Padrões** (p. 11): cada padrão define natureza, ideias, objetivos, **conteúdo** e **学业质量** (qualidade acadêmica) e implementação; giram em torno das **核心素养**; cada disciplina dedica **≥ 10% da carga** a 跨学科主题学习; padrões consideram ligação com a pré-escola e entre segmentos.

## Legibilidade por máquina

- Nenhum arquivo estruturado (JSON, CASE, RDF) ou codificação oficial de itens foi localizado (`not_found`).
- O plano é distribuído como PDF de imagens [C26]; os padrões não foram abertos.
- A smartedu.cn organiza recursos por disciplina/ano/edição/volume do livro didático, não por item de padrão [C04] [I: indica que o eixo operacional é o livro didático].

## Observações para o Core [I]

- Três camadas de emissor (nacional, provincial, escola) num mesmo currículo: C.CFW precisa de `issuer_level` e de composição de frameworks (o currículo da escola = nacional + local + escolar).
- "六三"/"五四" significa que o mesmo ano (ex.: 6º) pertence a segmentos diferentes conforme a região: C.PRG precisa de variante de estrutura por implantação, não de mapeamento fixo ano→segmento.
- 核心素养 + 学业质量 aproxima-se de competência + descritor de nível; sem a codificação, o crosswalk com BNCC só pode ser temático.
