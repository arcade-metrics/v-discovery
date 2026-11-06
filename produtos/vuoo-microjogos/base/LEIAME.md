# Base

Pesquisa de padrões (camadas agnóstica e Brasil, jurisdições fora da fase 1) e os estudos de estilo, captura e linguagem que fundamentam o produto.

**Citações de fonte:** os arquivos citam a base de conhecimento (`conhecimento/…`), os insumos (`projeto/insumos.md`) e a proposta (`projeto/vuoo.md`) pelo caminho, sem copiá-los.

## Raiz

| Arquivo | O que tem |
|---|---|
| `estrutura-escolar.md` | Resumo de organização, pessoas, papéis e inclusão (porta de entrada) |
| `captura-de-interacao.md` | Toque, arrasto, sensores, normalização, eventos |
| `parametrizacao-estilo.md` | Estilo adaptativo completo |
| `relatorio-infra-vuoo.md` | Relatório da infraestrutura agnóstica, com as decisões de infraestrutura INF-01 a INF-22 |
| `padroes-README.md` | Briefing da pesquisa de padrões |
| `_convencoes.md` | Formato de entrega e vocabulário provisório do Core |
| `inventario-existente.md` | Cruzamento entre o briefing e o trabalho já feito |
| `precedente-linguagem/` | Estudo de linguagem de 27/10/2026 (os insumos IN-01 a IN-35 que ele cita estão em `projeto/insumos.md`): página visual `vuoo-linguagem.html`, brief, gamificação, linguagem, microjogos (anatomia, ficha, conceitos), decisões D-01 a D-23, especificação de falas e mascote, guia prático de design, receita de ilustração, pesquisas (neurodivergência, 16 produtos, institucional), revisões e ferramentas. Só precedente: vale o que os documentos da raiz adotaram |

## `camada-agnostica/` (fase 1)

| Arquivo | O que tem |
|---|---|
| `arquitetura-em-camadas.md` | Diagrama e decisões: Core, perfis, adaptadores, views, grafo híbrido |
| `core-v0.1.md` | 12 princípios e ~35 entidades do Core |
| `padroes-de-arquitetura.md`, `evidencias-arquitetura.md` | Pesquisa de arquitetura e fontes |
| `internacional/` | Padrões-base: ISCED, datas, idioma, UUID, JSON Schema, OpenAPI, JSON-LD, WCAG, credenciais |

## `camada-brasil/` (fase 1)

| Arquivo | O que tem |
|---|---|
| `modulo-brasil.md` | Componentes do perfil Brasil e ordem de construção |
| `README-estudo-brasil.md` | Índice do estudo Brasil |
| `modelo-de-dados*.md`, `terminologia*.md` | Organização, Censo, CMDEB, currículo, avaliação, PEI |
| `crosswalk-*.md`, `cobertura-*.md`, `evidencias-*.md`, `questoes-abertas-*.md` | Brasil × Core, fontes e questões |
| `cmdeb/` | Portaria MEC 832/2025: 156 variáveis |
| `fichas/` | 25 fichas de normas brasileiras (LDB, LBI, LGPD, ECA Digital, Port. 421…) |

## `fora-da-fase-1/`

Referência, sem uso na fase 1.

| Pasta | O que tem |
|---|---|
| `estados-unidos/`, `uniao-europeia/`, `reino-unido/`, `china/` | Perfis por jurisdição em standby |
| `brasil/bncc-dados/`, `brasil/bncc-pacotes/` | Análise do bncc.dev: só inspiração, não usar |
