# Ficha: Plataforma Nacional de Educação Inteligente (国家智慧教育公共服务平台, smartedu.cn) e normas JY/T 0641, 0650, 0643

```yaml
id: cn.smartedu
name: 国家智慧教育公共服务平台 (National Smart Education Public Service Platform) + 智慧教育平台 系列 JY/T
acronym: smartedu.cn; JY/T 0641—2022; JY/T 0650—2022; JY/T 0643—2025
jurisdiction: China
issuing_organization: Ministério da Educação; app desenvolvido por 中央电化教育馆 (trecho) [C27]; normas: MOE [C06]
reference_type: plataforma pública (serviço) + normas técnicas setoriais recomendadas
domain: [D6, D8, D4 (indireto)]
official_url: https://www.smartedu.cn/
repository_url: not_found
version: JY/T 0641—2022; JY/T 0650—2022; JY/T 0643—2025
publication_date: 0641 e 0650: 2022-11-30; 0643: 2025-04-27 [C06]
last_updated: unknown
legal_status: plataforma: serviço público; normas: vigentes, recomendadas [C06]
mandatory_scope: JY/T 0650 é usada na "revisão técnica para entrada em operação" de recursos na plataforma (escopo SAMR) [C06]; obrigatoriedade geral not_found
education_levels: básica, profissional, superior [C04]
geographic_scope: nacional, com plataformas provinciais conectadas [C04]
language: chinês
license: unknown
technical_formats: not_found
api_available: não localizada (nenhuma documentação pública de API ou de padrão de intercâmbio)
data_model_available: não (JY/T 0641 é funcional)
ontology_available: não
schemas_available: não
implementation_examples: a própria plataforma
related_standards: [GB/T 22239-2019 (等级保护), GB/T 29765-2021 (backup), GB/T 36366-2018 (电子学档 e-portfólio), GB/T 41479-2022 (processamento de dados de rede), GB/T 35273-2020, JY/T 0644-2022]
entities: [usuário com papel, passe unificado, autorização a plataforma conectada, recurso (por disciplina, ano, edição, volume), curso, atividade de ensino síncrona/assíncrona, avaliação]
relationships: passe 1—N autorizações; recurso → disciplina/ano/edição/volume do livro didático
vocabularies: papéis (estudante, professor, pais, servidor escolar, servidor da administração, outros); tipos de documento (RIC, autorização de residência HK/Macau/Taiwan, passaporte)
core_relevance: média (identidade federada, catálogo de recursos)
regional_adapter_relevance: alta se a VUOO quiser conectar-se ao portal ou publicar recursos nele
limitations: API, protocolo de SSO e formato de recurso não localizados; JY/T 0650 e 0643 só título/escopo
open_questions: [QA-09, QA-12]
sources: [C04, C06, C27]
access_date: 2026-11-05
research_status: JY/T 0641 lida; 0650 e 0643 só metadados; plataforma sem documentação técnica pública localizada
```

## Achados

**JY/T 0641—2022 智慧教育平台 基本功能要求** (requisitos funcionais básicos) [C04]:
- Arquitetura: portal (autenticação, navegação, temas, busca, recomendação) + 4 blocos (escola básica, profissional, superior, salão de serviços) + ensino on-line.
- Bloco de escola básica: educação temática, 课程教学 (busca de livro didático por disciplina, ano, edição e volume, com sumário e recursos), tarefas, recursos de planejamento, serviço após aula, formação docente, educação familiar, experiências de reforma, livros didáticos digitais.
- Ensino on-line: ensino, aprendizagem (síncrona/assíncrona), avaliação (opcional), análise de dados e avaliação formando "电子学档" (e-portfólio), banco de recursos, interação, gestão, assistente de IA (análise de comportamento em vídeo, revisão de imagem e voz).
- Identidade: registro com nome real (documento + celular), passe unificado, autorização revogável a outras plataformas conectadas, com nome, sexo, escola, região e ID do passe (ver [../modelo-de-dados.md §8](../modelo-de-dados.md)).
- Segurança e técnica: 等级保护 (GB/T 22239-2019), backup (GB/T 29765-2021), "interface de dados baseada em protocolos de internet padrão" sem especificar qual.

**JY/T 0650—2022 智慧教育平台 数字教育资源技术要求**: escopo "revisão técnica de recursos digitais criados por órgãos e escolas para entrar em operação na plataforma" [C06]. Texto não lido.

**JY/T 0643—2025 智慧教育平台 个人信息保护通用要求**: escopo "regular o tratamento de dados pessoais dos usuários de plataformas de educação inteligente de todos os níveis"; redação inclui Huawei, Alibaba, Hikvision [C06]. Texto não lido. É a norma mais diretamente aplicável à VUOO na China e deve ser lida antes de qualquer projeto (QA-12).

**smartedu.cn**: SPA sem conteúdo acessível sem JavaScript; nenhum portal de desenvolvedor, API ou formato de intercâmbio localizado [C27]. `api_available: not_found`.

## Observações para o Core [I]

- O modelo de autorização da plataforma (o usuário autoriza a plataforma conectada a receber nome, sexo, escola, região e ID) é um consentimento por destinatário com revogação; C.CNS precisa de destinatário, conjunto de atributos e estado.
- Se a VUOO for "plataforma conectada", o adaptador precisa aceitar o passe nacional como provedor de identidade (C.IDN `scheme = smartedu-pass`), mas o protocolo é unknown.
