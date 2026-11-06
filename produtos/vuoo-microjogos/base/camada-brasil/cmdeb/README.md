# CMDEB: Conjunto Mínimo de Dados da Educação Básica

> **Fonte:** Portaria MEC nº 832, de 16/12/2025, Anexo. MEC Normas <https://mecnormas.mec.gov.br/pesquisa/detalhar/8017> (texto também no DOU de 17/12/2025). Coletado em 2026-11-04.

## Para que serve

Mineração do modelo de informação que o MEC exige das redes de ensino no **MEC Gestão Presente**: quais dados (variáveis, tipos, formatos, domínios de código, obrigatoriedade) descrevem estudante, matrícula, turma, componente curricular, frequência, desempenho, profissionais e escolas. Serve de referência para modelagem de dados e interoperabilidade de produtos que lidam com dados de alunos: campos esperados, códigos oficiais, o que é obrigatório e o que é opcional.

Este material é **transcrição estruturada da fonte**, sem interpretação. Análise e decisões de produto ficam fora desta pasta.

## Conteúdo

| Arquivo | O que tem |
|---|---|
| [00-norma.md](00-norma.md) | Metadados da portaria, arts. 13 e 14 resumidos (finalidade, tipos de dado, conteúdo mínimo, transmissão) |
| [01-metodo.md](01-metodo.md) | Como ler as tabelas: ocorrência, categorias, observações sobre a fonte |
| [02-indice-variaveis.md](02-indice-variaveis.md) | As 156 variáveis em uma tabela, com bloco, ocorrência, tipo e categoria |
| [10-estudante.md](10-estudante.md) | Bloco 1: Registro do Estudante (29 variáveis) |
| [20-trajetoria.md](20-trajetoria.md) | Bloco 2: matrícula, turma, componente curricular, frequência (componente e turma), avaliação (63) |
| [30-profissionais.md](30-profissionais.md) | Bloco 3: profissionais, formação, vínculos (47) |
| [40-instituicoes.md](40-instituicoes.md) | Bloco 4: instituições de ensino (17) |

Total: 156 variáveis (82 Registro, 55 Complementar, 17 Referência, 2 Situacional).

## Como foi obtido

A página do MEC Normas é um app web sem o texto no HTML. O conteúdo veio da API que a própria página consome (`/pesquisa/api/atos/8017`), que devolve o ato em JSON; as tabelas do Anexo foram convertidas para Markdown por script, e a contagem (156 linhas de dado) foi conferida contra a fonte. Nenhum arquivo para download foi baixado.

## Limites

- O art. 4º da Portaria 234/2025 (objetivos da finalidade) e os demais artigos dela **não** estão nesta portaria; ficam como pendência se forem necessários.
- O Anexo pode ser atualizado por ato do Ministro (art. 14 § 4º); conferir vigência antes de usar.
