# PRD: padrões e fontes minerados

Pasta para **mineração de padrões** de fontes externas (normas, modelos de dados, especificações) que alimentam requisitos de produto. Cada fonte vira uma subpasta com um `README.md` que **sempre cita a fonte e diz para que serve**.

## Convenções

- Tudo em `.md`. Se uma fonte tiver arquivo para download (PDF, planilha, XML), discute-se antes de baixar.
- Cada subpasta: `README.md` (fonte, finalidade, conteúdo, como foi obtido, limites) + arquivos numerados.
- Transcrição fiel da fonte, sem interpretação; análise fica em outra camada.
- Toda página cita a fonte e a data de coleta.

## Conteúdo

Tudo está em [padroes/](../produtos/vuoo-microjogos/base/padroes-README.md), organizado por jurisdição (desde 2026-11-05). As fontes brasileiras que antes ficavam soltas aqui foram movidas para [padroes/brasil/](../produtos/vuoo-microjogos/base/camada-brasil/README-estudo-brasil.md):

| Pasta | Fonte | Para que serve |
|---|---|---|
| [padroes/brasil/cmdeb/](../produtos/vuoo-microjogos/base/camada-brasil/cmdeb/README.md) | Portaria MEC 832/2025, Anexo (CMDEB) | Dados e variáveis da educação básica exigidos pelo MEC Gestão Presente |
| [padroes/brasil/bncc-dados/](../produtos/vuoo-microjogos/base/fora-da-fase-1/brasil/bncc-dados/README.md) | Repositório bncc-dev/bncc-dados (release dados-2026.08) | Análise da arquitetura de dado normativo aberto e verificado + playbook para replicar a estratégia (piloto: CMDEB) |
| [padroes/brasil/bncc-pacotes/](../produtos/vuoo-microjogos/base/fora-da-fase-1/brasil/bncc-pacotes/README.md) | [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) | Interfaces para máquina (npm, PyPI, MCP) e aplicação ao VUOO. Inspirar, não copiar |
| [padroes/brasil/bncc-computacao/](../produtos/vuoo-microjogos/base/camada-brasil/bncc-computacao/README.md) | *Computação na Educação Básica: Complemento à BNCC* (Parecer CNE/CEB 2/2022) | Os 141 objetivos e habilidades de Computação (EI, EF, EM) transcritos linha a linha |
| [padroes/brasil/bncc/](../produtos/vuoo-microjogos/base/camada-brasil/bncc/README.md) | BNCC homologada de 20/12/2017 (EI e EF) | Quadros e listas oficiais transcritos linha a linha em tabelas, com página e verificação |
