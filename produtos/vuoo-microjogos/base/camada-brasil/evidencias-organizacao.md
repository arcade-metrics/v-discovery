# Evidências: frente organização e dados (Brasil)

Registro de fontes da frente "organização e dados" (D1, D3, D8). Cada afirmação nos demais arquivos desta frente cita um identificador `[Exx]` desta tabela. Data de acesso de todas as fontes: **2026-11-05**, salvo indicação. Arquivos baixados (planilhas, PDFs, RAR) ficaram em diretório temporário fora do repositório e foram tratados como dados não confiáveis; nada foi copiado para o repo.

Convenções: **[I]** = inferência própria; `not_found` = procurado e não encontrado; "paráfrase" = a ferramenta de leitura devolveu o texto resumido, sem transcrição literal; conferir a redação antes de citar como texto legal.

## 1. Censo Escolar / Educacenso (INEP)

| Id | Fonte | URL | Versão / página / aba | Observação |
|---|---|---|---|---|
| E01 | Página "Primeira Etapa da Coleta" (Matrícula Inicial), aba Migração | https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/orientacoes/matricula-inicial/migracao | HTML | Lista leiaute 2026, tabelas auxiliares, instruções de migração |
| E02 | **Layout de Importação e Exportação da Matrícula Inicial 2026** (planilha) | https://download.inep.gov.br/educacao_basica/educacenso/migracao/2026/layout_de_importacao_e_exportacao_2026.xlsx | Versão **V5** (aba "atualizações da versão" registra v1 a V5); metadado `modified` 2026-07-01 | Abas: atualização, atualizações da versão, regras gerais, 00, 10, 20, 30, 40, 50, 60, Anexos 1 a 8. Fonte primária do modelo campo a campo |
| E03 | Layout de Identificação 2026 | https://download.inep.gov.br/educacao_basica/educacenso/migracao/2026/layout_de_identificacao_2026.xlsx | "Versão 1"; abas Regras Gerais, Campos | Arquivo de 9 campos para obter o ID INEP de alunos |
| E04 | Tabelas auxiliares do Educacenso 2026 | https://download.inep.gov.br/educacao_basica/educacenso/migracao/2026/tabelas_auxiliares_2026.rar | 22 planilhas (Etapas, AEE, Áreas do conhecimento, Municípios, Distritos, Países, Órgãos Regionais etc.) | "Tabela de Deficiência x Recurso" está com ano 2025 no nome |
| E05 | Etapas e Instruções Gerais para a Migração, 1ª etapa 2026 | https://download.inep.gov.br/educacao_basica/educacenso/migracao/2026/instrucoes_da_migracao_censo_escolar_1_etapa_2026.pdf | PDF, seções 1º a 5º passo | Fluxo exportação → identificação → importação; perfis Estado/Municipal/Escola |
| E06 | **Caderno de Conceitos e Orientações do Censo Escolar 2026** (1ª etapa) | https://download.inep.gov.br/publicacoes/institucionais/estatisticas_e_indicadores/cadernos_de_conceitos_2026.pdf | PDF interativo; páginas citadas pelo número impresso | Definições de turma, etapa, mediação, organização, AEE, identificação única, CPF |
| E07 | Página Matrícula Inicial, aba Cronograma | https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/orientacoes/matricula-inicial/cronograma | HTML | Data de referência 27/05/2026; Portaria nº 217/2026 (cronograma); Portaria MEC nº 731/2026 (preliminares) |
| E08 | Página "2ª Etapa da Coleta" (Situação do Aluno), aba Migração | https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/orientacoes/situacao-do-aluno/migracao | HTML | Em 2026-11-05 a página ainda lista os arquivos **2025** |
| E09 | Layout de Importação e Exportação 2025 – Situação do Aluno | https://download.inep.gov.br/educacao_basica/educacenso/migracao/2025/layout_de_importacao_e_exportacao_2025_situacao_do_aluno.v3.xlsx.xlsx | Título interno "Versão 2"; nome do arquivo "v3"; registros 89, 90, 91 | Códigos de situação do aluno |
| E10 | Caderno de Conceitos e Orientações da 2ª Etapa do Censo Escolar 2025 – Situação do Aluno | https://download.inep.gov.br/publicacoes/institucionais/estatisticas_e_indicadores/cadernos_de_conceitos_e_orientacoes_da_segunda_etapa_do_censo_escolar_2025_situacao_do_aluno_ed.pdf | PDF, seções 2 a 5 (p. 6 a 11) | Definições de aprovado, reprovado, transferido, deixou de frequentar etc. |
| E11 | Página de microdados do Censo Escolar | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar | HTML | Microdados 2025 publicados (`microdados_censo_escolar_2025_.zip`); conteúdo não baixado |
| E12 | Página Censo Escolar (raiz) | https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar | HTML | Link "Documentos e legislação" do briefing não existe mais (404); conteúdo hoje em "Orientações" e "Outros documentos" |

## 2. Legislação federal

| Id | Fonte | URL | Versão | Observação |
|---|---|---|---|---|
| E20 | LDB, Lei 9.394/1996, texto compilado (Planalto) | https://www.planalto.gov.br/ccivil_03/leis/l9394.htm | Compilado consultado em 2026-11-05; alteração mais recente vista: Lei 15.468/2026 (art. 26 §9-B) | Leitura por ferramenta que devolveu **paráfrase**; o download direto por curl falhou (conexão reiniciada). Artigos 4, 8–11, 16–18, 21, 23, 24, 26, 29–32, 34, 35, 37, 38, 58–61, 67 |
| E21 | Lei Complementar 220, de 31/10/2025 (Sistema Nacional de Educação) | https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp220.htm | DOU 03/11/2025 | Arts. 24 a 26 (Inde, **Inue = CPF**); art. 26 caput e inciso I com transcrição literal; demais em paráfrase |
| E22 | Decreto 6.425/2008 (censos anuais da educação), via Caderno 2026 | citado em E06, p. 2 | — | Obrigatoriedade do Censo para escolas públicas e privadas (art. 4º), conforme o Caderno; texto do decreto não lido diretamente |
| E23 | Portaria MEC 264/2007 (Dia Nacional do Censo Escolar) | https://download.inep.gov.br/educacao_basica/educacenso/legislacao_documentos/2011/portaria_n264_dia_nacional_censo_2007.pdf | citada em E07 | Data de referência = última quarta-feira de maio; PDF não lido |

## 3. MEC: EducaDados, Gestão Presente, CMDEB

| Id | Fonte | URL | Versão | Observação |
|---|---|---|---|---|
| E30 | **Portaria MEC nº 269, de 24/03/2026** (EducaDados e Plataforma Nacional de Dados da Educação) | https://mecnormas.mec.gov.br/pesquisa/detalhar/9047 (texto via `https://mecnormas.mec.gov.br/pesquisa/api/atos/9047`); DOU: https://www.in.gov.br/web/dou/-/portaria-mec-n-269-de-24-de-marco-de-2026-695460311 | DOU 26/03/2026; vigente | Texto integral lido (24 artigos) |
| E31 | Portaria MEC nº 832/2025 (CMDEB) | ver [cmdeb/00-norma.md](cmdeb/00-norma.md) | — | Já transcrita; não reescrita aqui |
| E32 | Portaria MEC nº 234, de 02/04/2025 (MEC Gestão Presente) | DOU 03/04/2025, p. 55: https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?jornal=515&pagina=55&data=03/04/2025 | — | **Texto integral não lido** (PDF do DOU exige captcha; cópia em abmes.org.br é imagem). Conteúdo conhecido via E33 e E34 |
| E33 | Notícia MEC "Portaria institui a plataforma de dados MEC Gestão Presente" | https://www.gov.br/mec/pt-br/assuntos/noticias/2025/abril/portaria-institui-a-plataforma-de-dados-mec-gestao-presente | abr/2025 | Adesão voluntária por acordo de adesão via Simec |
| E34 | Páginas MEC Gestão Presente: "Como funciona", "Sistema Gestão Presente", "Gestão Presente na Escola", "Contexto", "Legislação" | https://www.gov.br/mec/pt-br/mec-gestao-presente/como-funciona ; …/sistema-gestao-presente ; …/gestao-presente-na-escola ; …/contexto ; …/legislacao | HTML | SGP 2.0 lançado em 10/03/2026; transição (EI, EF e profissionais na nova versão; EM na antiga) |
| E35 | Cartilha de uso da API da nova versão do Sistema Gestão Presente | https://www.gov.br/mec/pt-br/mec-gestao-presente/documentos/cartilhausoapimecgestaopresente.pdf | PDF 10 p. | Token Bearer (5 min), snake_case, HTTP 422, rotas de lotes |
| E36 | **Especificação OpenAPI "API CMDEB v2"** | https://api-cmde2.gestaopresente.mec.gov.br/api/v2/openapi.json (Swagger: https://api-cmde2.gestaopresente.mec.gov.br/docs ; Redoc: …/redoc; homologação: https://api-cmde2.hmg.gestaopresente.mec.gov.br/…) | OpenAPI 3.1.0, `info.version` 2.0.0; 49 operações, 106 schemas | Pública, sem autenticação para leitura do contrato |
| E37 | FAQ MEC Gestão Presente | https://www.gov.br/mec/pt-br/acesso-a-informacao/perguntas-frequentes/mec-gestao-presente | HTML | Adesão ao SGP é pré-requisito dos demais módulos |

## 4. Estados

| Id | Fonte | URL | Versão | Observação |
|---|---|---|---|---|
| E40 | SEDUC-SP, POP.URENT1.2005 "Regularização de Registro do Aluno (R.A) em duplicidade" | https://midiasstoragesec.blob.core.windows.net/001/2026/06/pop-urent1_-2005-processo-de-regularizao-de-registro-de-aluno-em-duplicidade.pdf | publicado jun/2026 | Definição do RA; RA com dígito e UF; SED como sistema oficial |
| E41 | SP, FAQ Cadastro de Alunos (SED) | https://www.saude.sp.gov.br/resources/crh/gsdrh/supervisao-escolar/a13-2017-07-27-faq_cadastrodealunos_edicao.pdf | 2017 | Fonte antiga, hospedada em domínio da Saúde-SP (escolas técnicas); usar só como indício |

## 5. Fontes buscadas e não encontradas

| Item | Resultado |
|---|---|
| Dicionário de dados oficial do Educacenso como documento único | `not_found`: o INEP publica o leiaute (E02) e tabelas auxiliares (E04); dicionário de microdados fica dentro do ZIP (E11), não lido |
| Leiaute da Situação do Aluno 2026 | `not_found` em 2026-11-05: a página (E08) ainda lista 2025 |
| Texto integral da Portaria MEC 234/2025 | não lido (ver E32) |
| Ato que define o "Padrão Nacional de Interoperabilidade da Educação" (Portaria 269/2026, art. 9–11) | `not_found` |
| Composição do CC/EducaDados (art. 21 da Portaria 269/2026) | `not_found` |
| Manual do SGP nova versão (`MANUALGESTAOPRESENTENOVAVERSAO.pdf`) | link na página E34 retorna 404 |
