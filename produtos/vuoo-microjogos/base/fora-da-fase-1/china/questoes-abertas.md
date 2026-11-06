# Questões abertas — China

Ambiguidades, lacunas, conflitos e decisões pendentes. Pesquisa de 2026-11-05. "Candidato a entidade do Core" segue a regra de [_convencoes.md §4](../../_convencoes.md).

## 1. Referências e textos

| ID | Questão | Situação / próximo passo |
|---|---|---|
| QA-01 | **JY/T 0634-2022 e JY/T 0635-2022 não existem** no cadastro de normas setoriais da SAMR. Os temas do briefing correspondem a JY/T 0637—2022 (pessoal) e JY/T 0639—2022 (escolas de educação básica) [C06, C09]. | Corrigir o briefing (§3.3) para 0633/0637/0639. Confirmar o aviso oficial "《教育基础数据》等三项" no moe.gov.cn (só visto em lista do eol.cn). |
| QA-02 | Relação entre a série JY/T 1001–1007-2012 e as normas de 2022: nada indica substituição; ambas "现行". Relação entre GB/T 33782/35298-2017 e JY/T 1001/1002-2012 (títulos quase iguais) também unknown. | Ler prefácios da GB/T 33782 e 35298 (openstd.samr.gov.cn, leitura on-line). |
| QA-03 | Os códigos de que a JY/T 0633 depende (tipo de escola, urbano/rural, mantenedor, categoria de estudante, categoria e origem de servidor, **regra do 学校标识码**) estão na GB/T 33782—2017, não lida. | Ler GB/T 33782 §4.1, tabelas 4, 5, 24, 63, 64. |
| QA-04 | **Turma, oferta, horário e sala** não aparecem em nenhuma norma de dados lida. | Verificar JY/T 1004-2012 (普通中小学校管理信息) e GB/T 36351.2-2018. Se ausentes, o adaptador depende do sistema de gestão da escola. |
| QA-05 | **Formato oficial do 学籍号** não publicado; fonte secundária: G/L/J + 18 posições [C12]. Relação com o 个人标识码 a19 da JY/T 0633 não confirmada. | Buscar especificação técnica do sistema nacional de 学籍 ou norma da 教育部教育管理信息中心. Não implementar validação de formato sem fonte oficial. |
| QA-06 | Identificador nacional de professor (além do 个人标识码 e do nº do certificado docente) não localizado; regra do nº do 教师资格证 não vista. | Verificar sistema nacional de gestão de professores (全国教师管理信息系统) e regras do certificado. |
| QA-07 | As normas de dados não marcam quem é o **responsável legal** (pode consentir); a PIPL exige consentimento dele para menores de 14. | No adaptador, atributo próprio em C.GRD; verificar se JY/T 0643—2025 trata disso. |
| QA-08 | GB/T 36342-2018 (campus inteligente), 中小学数字校园建设规范(试行) (2018) e a situação atual do CELTS não foram lidos. | Baixa prioridade para o Core. |
| QA-09 | smartedu.cn: nenhuma API, protocolo de SSO ou formato de recurso público localizado. JY/T 0650—2022 (requisitos técnicos de recursos) não lida. | Ler JY/T 0650; procurar documentação de acesso de plataformas conectadas (接入规范). |
| QA-12 | **JY/T 0643—2025 智慧教育平台 个人信息保护通用要求** (vigente desde 2025-04-27) é a norma setorial de proteção de dados mais aplicável à VUOO e não foi lida. | Prioridade 1 antes de qualquer decisão de adaptador China. |
| QA-13 | Normas de metadados de recursos (JY/T 0607–0609-2017, 0644-2022) e de competência docente (0646-2022) só por título. | Ler 0607 (modelo) e 0608 (XML) para comparar com LOM/LRMI. |
| QA-14 | Os 16 padrões curriculares de 2022 não foram abertos: não se sabe se os itens (conteúdos, requisitos de qualidade) têm **códigos** ou só numeração de seção. Nenhuma versão legível por máquina localizada. | Abrir 2 padrões (数学, 信息科技) e verificar numeração. |
| QA-17 | Texto consolidado da Lei de Cibersegurança de 2026 não lido; a numeração dos artigos mudou (ex.: localização de CIIO citada como art. 39). | Ler texto republicado pela APN. |
| QA-18 | Lei de Proteção de Menores (alterada em 2024) só por trecho; não se sabe se a gamificação da VUOO seria "jogo on-line" para fins de modo menor (条例 art. 43). | Ler a lei e normas de modo menor da CAC. |
| QA-19 | Vigência atual das medidas de registro de apps educacionais (2019) e da plataforma app.eduyun.cn não confirmada. | Verificar avisos do MOE após 2023. |

## 2. Implantação e mercado

| ID | Questão | Situação |
|---|---|---|
| QA-16 | Limiares de transferência (CAC 2024) tornam inviável processar dados de alunos chineses fora da China em escala. Medidas de certificação de dados pessoais para exportação (2025) e o regime de "acesso remoto" como transferência não foram lidos. | Decisão de arquitetura: instância isolada no território [I]. |
| QA-20 | Regras de **ICP备案/licença ICP** e de telecom de valor agregado não lidas; exigência de servidor e entidade no território inferida, não verificada. | Ler 互联网信息服务管理办法 e regras do MIIT. |
| QA-21 | Enquadramento da VUOO: ferramenta escolar (B2B/B2G) × formação on-line de disciplinas (双减: aprovação e proibição de capital estrangeiro) × publicação em rede (proibida a capital estrangeiro, lista negativa item 13). | Parecer jurídico local antes de qualquer projeto. |
| QA-23 | Regras de **algoritmos de recomendação** (互联网信息服务算法推荐管理规定) e de **IA generativa** (生成式人工智能服务管理暂行办法) não pesquisadas; a CSL 2025 acrescentou artigo sobre IA. | Pesquisar se a VUOO usar recomendação adaptativa ou IA generativa com alunos. |
| QA-24 | Designação como infraestrutura crítica (CIIO) de plataforma educacional de grande porte: unknown. | Depende de autoridade setorial. |

## 3. Candidatos a entidade/atributo do Core

| ID | Candidato | Origem chinesa | Por que é genérico [I] |
|---|---|---|---|
| QA-10 | `AggregateIndicator` (indicador agregado por organização e período) | JY/T 0639 | Censo Escolar (Brasil) e School Census (UK) pedem o mesmo; derivado, fora do núcleo transacional |
| QA-11 | `DataClassification` (esquema, classe, nível, herança pelo máximo) por conjunto de dados | JY/T 0661, DSL art. 21 | LGPD (dado sensível), GDPR (categorias especiais), FERPA (directory information) também classificam; só o esquema muda |
| QA-15 | `ProgramStructure` (variante de estrutura de anos por implantação: "六三"/"五四") | 课程方案 2022 | Brasil (EF 1–5/6–9), EUA (K-5/6-8 × K-6/7-9) têm variações locais equivalentes |
| QA-16b | `DataResidency` + registro de transferência (base legal, receptor, volume, mecanismo) | PIPL 38–40, CAC 2024 | GDPR cap. V e LGPD art. 33 pedem o mesmo |
| QA-22 | Vínculo funcional (编制, forma de contratação, contrato) | JY/T 0633 4.8–4.10 | provavelmente extensão do adaptador, não Core; registrar só para decisão |
| QA-25 | `kind` em C.ENR (escola atual × escola de pertencimento) e em C.CNS (destinatário, atributos, revogação) | JY/T 0633 3.2/3.3; JY/T 0641 §6.1 | separação de vínculo administrativo × frequência aparece também no Brasil (matrícula × enturmação) |
