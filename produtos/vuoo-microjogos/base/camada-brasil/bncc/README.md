# BNCC 2017 (EI e EF) em tabelas

> **Histórico (06/11/2026).** Esta transcrição é da edição de 2017 e fica como referência de método. A BNCC de referência é a versão final (EI, EF e EM), no repositório **vuoo-base** (`fontes/bncc/`, https://github.com/arcade-metrics/v-base): fonte oficial `BNCC_EI_EF_110518_versaofinal_site.pdf` (versão final, EI, EF e EM) e cópia de trabalho `BNCC_reparado.pdf`.

> **Fonte:** *Base Nacional Comum Curricular: Educação é a Base*, Ministério da Educação, versão homologada para a Educação Infantil e o Ensino Fundamental. Arquivo `BNCC_20dez_site.pdf` (nesta pasta), criado em 20/12/2017 (Adobe InDesign), 472 páginas PDF, SHA-256 `7d0004aacde591d4d898cbdf950ab7ed28e875f837dab12bb88cb15567cdf180`. Transcrição em 2026-11-04. Página impressa = página PDF − 2.

## Para que serve

Este é o conteúdo normativo da BNCC de Educação Infantil e Ensino Fundamental **transformado em tabela, linha a linha**, sem interpretação. Cada registro traz o código oficial, o texto como impresso, a sua posição no quadro (unidade temática ou prática, objetos de conhecimento, campo de atuação ou eixo) e a página. Serve de base de dados curricular para produto, com rastreabilidade até a página do documento.

O texto é o do documento de **2017**. A BNCC completa de 2018 (com o Ensino Médio) mudou alguns textos e numerações da EI e do EF; as diferenças estão em [99-verificacao.md](99-verificacao.md).

## Conteúdo

| Arquivo | O que tem | Registros |
|---|---|---|
| [01-competencias-gerais.md](01-competencias-gerais.md) | As 10 competências gerais | 10 |
| [02-competencias-especificas.md](02-competencias-especificas.md) | Competências específicas de área e de componente do EF | 84 em 11 listas |
| [10-educacao-infantil.md](10-educacao-infantil.md) | Grupos etários, direitos de aprendizagem, campos de experiências, objetivos por campo (com a linha do quadro), síntese das aprendizagens | 93 objetivos, 6 direitos, 19 sínteses |
| [21-lingua-portuguesa.md](21-lingua-portuguesa.md) | Habilidades por quadro, campo de atuação, prática de linguagem e objetos | 391 |
| [22-arte.md](22-arte.md) | Habilidades por unidade temática e objetos | 61 |
| [23-educacao-fisica.md](23-educacao-fisica.md) | idem | 69 |
| [24-lingua-inglesa.md](24-lingua-inglesa.md) | idem, por eixo | 88 |
| [25-matematica.md](25-matematica.md) | idem | 247 |
| [26-ciencias.md](26-ciencias.md) | idem | 111 |
| [27-geografia.md](27-geografia.md) | idem | 123 |
| [28-historia.md](28-historia.md) | idem | 151 |
| [29-ensino-religioso.md](29-ensino-religioso.md) | idem | 63 |
| [90-indice-codigos.md](90-indice-codigos.md) | Os 1.397 registros em uma tabela: código, etapa, componente, quadro, página | 1.397 |
| [98-decisoes.md](98-decisoes.md) | Decisões de transcrição e peculiaridades do documento mantidas como impressas | |
| [99-verificacao.md](99-verificacao.md) | Completude, comparação com uma linhagem independente, erros corrigidos, como reproduzir | |
| [_pipeline/](_pipeline/) | Scripts que geram as tabelas a partir do PDF (extração, geração dos `.md`, conferência visual) | |

## Como ler as tabelas

- **Uma linha por habilidade ou objetivo**, na ordem em que aparecem nos quadros.
- **Colunas do EF:** unidade temática (ou prática de linguagem, em LP) | objetos de conhecimento | código | habilidade | página. Quando a célula do quadro tem vários objetos, eles vêm separados por `<br>`, todos ligados às habilidades daquela linha.
- **Subtítulos:** `##` é o quadro como impresso (ex.: "MATEMÁTICA – 5º ANO"); `###` é a faixa do quadro (campo de atuação em LP, eixo em LI), com o texto impresso na faixa.
- **Página:** impressa e PDF, ex.: "93 (PDF 95)".
- **⚠** marca os dois códigos que o documento imprime duas vezes com textos diferentes (EF05LP25 e EF04LP27; decisão 2).

## Garantias

- 1.397 de 1.397 ocorrências de código dos quadros estão nas tabelas, sem faltas nem sobras.
- Textos, estrutura e alinhamentos comparados registro a registro com uma linhagem independente (bncc-dados, BNCC 2018); cada diferença foi conferida na imagem da página impressa e é diferença real entre as versões.
- A extração é reproduzível: o script gera de novo exatamente as mesmas tabelas.

## Limites

- A **prosa** dos capítulos (introdução, textos de área e de componente, descrição dos campos de experiências) não foi transcrita: não é tabela.
- O documento é de **2017** e não traz o Ensino Médio. Para o texto vigente da BNCC completa (2018), consultar a versão homologada de 2018.
