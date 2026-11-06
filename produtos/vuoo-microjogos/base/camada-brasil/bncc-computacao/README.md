# BNCC Computação (complemento de 2022) em tabelas

> **Fonte:** *Computação na Educação Básica: Complemento à BNCC*. Arquivo `BNCCComputaoCompletodiagramado.pdf` (nesta pasta), criado em 13/04/2022 (Serif Affinity Publisher; autor nos metadados: Christian Brackmann), 75 páginas PDF, SHA-256 `60aab0b192acf867bc582dc06678cd8f3bc597e8f1b65256fc7bf04190bb793d`. Complemento à BNCC aprovado pelo Parecer CNE/CEB nº 2/2022. Transcrição em 2026-11-05. Página impressa = página PDF − 4.

## Para que serve

É o conteúdo normativo do complemento de Computação à BNCC **transformado em tabela, linha a linha**, sem interpretação, no mesmo método de [../bncc/](../bncc/README.md). Cada registro traz o código oficial, o texto como impresso, a posição no quadro (eixo, objeto de conhecimento, competência) e a página. Ao contrário da BNCC de 2017, este documento traz também, na página da direita de cada quadro, a **explicação da habilidade** e **exemplos de atividades** (plugadas e desplugadas). Esses textos foram transcritos por inteiro: são a parte mais útil para desenhar atividades.

Cobre as três etapas: Educação Infantil, Ensino Fundamental e Ensino Médio.

## Conteúdo

| Arquivo | O que tem | Registros |
|---|---|---|
| [01-premissas-e-competencias.md](01-premissas-e-competencias.md) | Premissas da EI, competências do EF e do EM | 4 + 7 + 7 |
| [10-educacao-infantil.md](10-educacao-infantil.md) | Objetivos por eixo, com os exemplos | 11 |
| [20-ensino-fundamental-anos-iniciais.md](20-ensino-fundamental-anos-iniciais.md) | Habilidades do 1º ao 5º ano e o quadro "por etapa" (`EF15CO`), com explicação e exemplos | 50 |
| [21-ensino-fundamental-anos-finais.md](21-ensino-fundamental-anos-finais.md) | Habilidades do 6º ao 9º ano e o quadro "por etapa" (`EF69CO`), com objeto em dois níveis, enunciado geral, explicação e exemplos | 54 |
| [30-ensino-medio.md](30-ensino-medio.md) | Habilidades por competência específica, com explicação e exemplos | 26 |
| [90-indice-codigos.md](90-indice-codigos.md) | Os 141 registros em uma tabela: código, etapa, eixo ou competência, quadro, página | 141 |
| [98-decisoes.md](98-decisoes.md) | Decisões de transcrição e peculiaridades do documento mantidas como impressas | |
| [99-verificacao.md](99-verificacao.md) | Completude, comparação com uma linhagem independente, erros corrigidos, como reproduzir | |
| [_pipeline/](_pipeline/) | Scripts: extração, geração dos `.md`, comparação, conferência visual | |

## Como ler as tabelas

- **Uma linha por habilidade ou objetivo**, na ordem em que aparecem nos quadros. O título `##` é o quadro como impresso (ex.: "COMPUTAÇÃO - 1º ANO", "COMPUTAÇÃO / POR ETAPA - 1º ao 5º ANO").
- **Colunas do EF, anos iniciais:** eixo | objeto de conhecimento | código | habilidade | página.
- **Colunas do EF, anos finais:** eixo | objeto de conhecimento | objeto (2º nível) | enunciado geral (sem código) | código | habilidade | página. Os nomes das duas colunas do meio são nossos (decisão 3).
- **EM:** um grupo por competência específica, com o texto impresso no quadro; o número é o da lista da PDF 65.
- **Explicação e exemplos** vêm depois das tabelas, numa seção `### <código>` por habilidade, com a página da direita. Quebras de linha marcadas com `<br>`. Quando uma habilidade tem duas linhas de explicação e exemplos, elas aparecem como "(1 de 2)" e "(2 de 2)" (decisão 2).
- **Página:** impressa e PDF, ex.: "12 (PDF 16)".

## Garantias

- 141 de 141 ocorrências de código do PDF estão nas tabelas, sem faltas nem sobras.
- Códigos, páginas, eixos, anos, objetos e competências comparados registro a registro com uma linhagem independente (bncc-dados, `dados-2026.08`): concordam em tudo, salvo três pontos explicados em [99-verificacao.md](99-verificacao.md), cada um conferido na imagem da página.
- A extração é reproduzível: o script gera de novo exatamente o mesmo resultado.

## Limites

- Quebras de linha dentro da explicação e dos exemplos são reconstruídas por regra; em casos raros duas frases ficam na mesma linha (decisão 7). O texto não muda.
- Os endereços web dos exemplos foram transcritos, não acessados (decisão 10).
- Este arquivo é a versão diagramada; a paginação coincide com a do anexo usado pelo bncc-dados, mas não foi comparado com o arquivo do portal do MEC (decisão 12, **[A CONFIRMAR]**).
- Os textos de abertura das etapas, a capa e o sumário não foram transcritos (decisão 11).
