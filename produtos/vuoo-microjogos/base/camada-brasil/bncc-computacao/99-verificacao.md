# Verificação

> **Fonte verificada:** *Computação na Educação Básica: Complemento à BNCC*, `BNCCComputaoCompletodiagramado.pdf`, SHA-256 `60aab0b192acf867bc582dc06678cd8f3bc597e8f1b65256fc7bf04190bb793d`. **Linhagem independente usada só para comparação:** `computacao.json` do dataset [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados), release `dados-2026.08`, commit `9c26897`, SHA-256 `6192c381961c55ab…` (estrutura via planilhas da Secretaria de Educação de Pernambuco, texto verificado contra o anexo oficial; CC BY 4.0, bncc.dev, mantido pela Profy). Verificado em 2026-11-05.

## Como foi feito

1. **Extração determinística** (`_pipeline/extrair.py`): lê a camada de texto do PDF com a posição de cada palavra (PyMuPDF) e reconstrói os quadros pela geometria: colunas pelos fios verticais (ou pelo meio entre os cabeçalhos, onde falta fio), linhas pelos fios horizontais, e a página da direita pela altura da linha da habilidade. Não há digitação nem LLM na cadeia; as intervenções manuais são as de [98-decisoes.md](98-decisoes.md), cada uma com página conferida na imagem.
2. **Falha em vez de adivinhar:** o extrator para com erro se uma célula de habilidade não abre com código, se tem dois códigos, se um eixo é desconhecido, se uma célula da direita ultrapassa a da esquerda, se uma lista não tem o número de itens esperado ou se o número de competências do quadro do EM difere da lista.
3. **Reprodução:** duas execuções geram JSON idêntico (mesmo SHA-256).
4. **Contagens e completude** contra o próprio PDF (abaixo).
5. **Comparação com a linhagem independente** registro a registro (`_pipeline/comparar.py`). Toda diferença foi conferida na imagem da página.

## Completude

| Verificação | Resultado |
|---|---|
| Ocorrências de código entre parênteses no PDF | 141 |
| Registros nas tabelas | 141 (11 objetivos EI + 104 habilidades EF + 26 habilidades EM) |
| Códigos distintos | 141 (EF05CO11 impresso como `EF05CO011`, decisão 1) |
| Código no PDF fora das tabelas / nas tabelas fora do PDF | 0 / 0 |
| Células de habilidade sem código de abertura | 0 |
| Habilidades sem explicação ou exemplos | 0 (EI tem só exemplos, como impresso) |

Por quadro: EI 11; 1º ano 7, 2º 6, 3º 9, 4º 8, 5º 11, por etapa 1º ao 5º 9; 6º 10, 7º 11, 8º 11, 9º 10, por etapa 6º ao 9º 12; EM 26. Por eixo (EI e EF): Pensamento Computacional 49, Cultura Digital 36, Mundo Digital 30. EM por competência: 1 → 6, 2 → 2, 3 → 3, 4 → 5, 5 → 2, 6 → 4, 7 → 4.

Listas: premissas da EI 4, competências do EF 7, competências do EM 7.

## Comparação com a linhagem independente

| Item | Iguais | Diferentes | Origem das diferenças |
|---|---|---|---|
| Conjunto de códigos | 141 / 141 | 0 | |
| Página PDF | 141 / 141 | 0 | |
| Textos das aprendizagens | 139 / 141 | 2 | barra no fim da linha (abaixo) |
| Eixo | 115 / 115 | 0 | |
| Grupo etário (EI) | 11 / 11 | 0 | |
| Anos (EF) | 104 / 104 | 0 | |
| Objeto de conhecimento, anos iniciais | 50 / 50 | 0 | |
| Objeto de conhecimento, anos finais, 1º nível | 53 / 54 | 1 | "(cont.)" (decisão 5) |
| Objeto, anos finais, 2º nível | 53 / 54 | 1 | "(cont.)" (decisão 5) |
| Competência do EM (número) | 26 / 26 | 0 | |
| Competências do EF (texto) | 7 / 7 | 0 | |
| Competências do EM (texto da lista) | 7 / 7 | 0 | a linhagem usa o texto da lista; o do quadro difere em 3 (decisão 4) |

Comparação de objetos feita sem diferenciar maiúsculas. Os campos que só esta transcrição tem (explicação, exemplos, enunciado geral sem código, texto da competência como impresso no quadro, premissas da EI) não têm com o que comparar na linhagem.

### Diferenças de texto

| Código | Esta transcrição | Linhagem | Página |
|---|---|---|---|
| EF08CO05 | "armazenamento/processamento distribuídos" | "armazenamento/ processamento distribuídos" | PDF 52 |
| EF69CO09 | idem | idem | PDF 62 |

Nas duas, a barra está no fim da linha impressa (conferido na imagem); a regra daqui une sem espaço (decisão 6). É a mesma divergência de regra registrada no [../bncc/99-verificacao.md](../bncc/99-verificacao.md).

## Erros de extração encontrados e corrigidos durante o processo

| Erro | Causa | Correção |
|---|---|---|
| Quadros "por etapa" não lidos | A faixa colorida do título foi tomada como faixa de cabeçalho | Cabeçalho localizado pelo retângulo que contém os rótulos das colunas |
| `EF05CO01` contado duas vezes | `EF05CO011` casava como prefixo | Código com 2 ou 3 dígitos; mapa explícito (decisão 1) |
| Explicação e exemplos misturados em 3 habilidades | Duas linhas da direita para uma célula da esquerda | Pares em ordem (decisão 2) |
| Coluna de explicação e de exemplos sem fio entre elas (PDF 61 e 63) | O documento não desenha o fio nessas páginas | Limite pelo meio entre os cabeçalhos |
| Competência do EM sem correspondência | Texto do quadro difere da lista | Correspondência pela ordem, diferença registrada (decisão 4) |
| "responsabilidad e" | Palavra partida sem hífen em coluna estreita | Conferência visual (decisão 6) |
| Itens de lista colados na mesma linha (EI03CO04, EI03CO05) | Linha anterior rente à margem | Marcador de lista abre linha nova (decisão 7) |

## Como reproduzir

```bash
pip install pymupdf
python PRD/bncc-computacao/_pipeline/extrair.py saida.json
python PRD/bncc-computacao/_pipeline/gerar_md.py saida.json PRD/bncc-computacao
python PRD/bncc-computacao/_pipeline/comparar.py saida.json <bncc-dados>/dados/computacao-2022/computacao.json
python PRD/bncc-computacao/_pipeline/ver_pagina.py 36 "EF05CO011" cod11 40   # conferência visual de um trecho
```
