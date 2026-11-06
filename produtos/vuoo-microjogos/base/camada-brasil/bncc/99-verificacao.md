# Verificação

> **Fonte verificada:** *Base Nacional Comum Curricular* (EI e EF), MEC, versão homologada de 20/12/2017, `BNCC_20dez_site.pdf`, SHA-256 `7d0004aacde591d4d898cbdf950ab7ed28e875f837dab12bb88cb15567cdf180`. **Linhagem independente usada só para comparação:** dataset [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados), release `dados-2026.08` (BNCC completa homologada de 2018, extraída das planilhas do MEC; CC BY 4.0, bncc.dev, mantido pela Profy). Verificado em 2026-11-04.

## Como foi feito

1. **Extração determinística** (`_pipeline/extrair.py`): lê a camada de texto do PDF com as posições de cada linha (PyMuPDF) e reconstrói as tabelas pela geometria (colunas, fios, faixas). Não há digitação nem LLM na cadeia; as únicas intervenções manuais são as listadas em [98-decisoes.md](98-decisoes.md), cada uma com página conferida.
2. **Reprodução:** rodar o extrator de novo gera um JSON idêntico ao validado.
3. **Contagens e completude** contra o próprio PDF (abaixo).
4. **Comparação com a linhagem independente** registro a registro: texto, objetos de conhecimento, unidade temática ou prática, campo de atuação e eixo. Toda diferença foi conferida na imagem da página impressa.

## Completude

| Verificação | Resultado |
|---|---|
| Ocorrências de código nos quadros do PDF (fora do capítulo "Estrutura") | 1.397 |
| Registros nas tabelas | 1.397 (93 objetivos EI + 1.304 habilidades EF) |
| Códigos distintos | 1.395 (2 códigos impressos duas vezes, decisão 2) |
| Código no PDF fora das tabelas / nas tabelas fora do PDF | 0 / 0 |
| Linhas de habilidade sem código de abertura | 0 |

Contagens por componente (EF): Língua Portuguesa 391, Matemática 247, História 151, Geografia 123, Ciências 111, Língua Inglesa 88, Educação Física 69, Ensino Religioso 63, Arte 61.

Listas: competências gerais 10; competências específicas: Linguagens 6, Língua Portuguesa 10, Arte 9, Educação Física 10, Língua Inglesa 6, Matemática 8, Ciências da Natureza 8, Ciências Humanas 7, Geografia 7, História 7, Ensino Religioso 6. Direitos de aprendizagem 6. Síntese das aprendizagens 19 itens (conferidos na imagem das PDF 54 e 55).

## Comparação com a linhagem independente (BNCC 2018)

| Item | Iguais | Diferentes | Origem das diferenças |
|---|---|---|---|
| Textos dos objetivos da EI | 93 / 93 | 0 | |
| Alinhamento da EI (mesma linha do quadro) | 32 / 32 | 0 | |
| Competências gerais | 10 / 10 | 0 | |
| Textos das competências específicas | 84 / 84 | 0 | Em LP, História e Ensino Religioso a **numeração** difere: o documento de 2018 reordenou. A de 2017 foi conferida na imagem (PDF 87 e 437) |
| Unidade temática / prática (EF) | 1.300 / 1.300 | 0 | (sem contar os 2 códigos duplicados) |
| Campo de atuação (LP) e eixo (LI) | todos | 0 | |
| Textos das habilidades (EF) | 1.291 / 1.300 | 9 | Ver abaixo |
| Objetos de conhecimento (EF) | 1.292 / 1.300 | 8 | Ver abaixo |

Diferenças que não são nem de versão nem de leitura (separador "/ " e itens de objeto juntados) ficaram de fora da contagem. O bncc-dados guarda o espaço que a planilha põe depois de uma barra no fim da linha e às vezes junta dois objetos numa mesma string; a tabela daqui segue a página (decisões 5 e 8).

### Diferenças de texto: o que a página de 2017 imprime

Todas conferidas na imagem. A tabela traz a coluna 2017.

| Código | 2017 (este documento) | 2018 |
|---|---|---|
| EF01LP09 | "…sons de sílabas iniciais, mediais e finais." | "…sons de sílabas iniciais." |
| EF01LP13 | "…sons de sílabas iniciais, mediais e finais." | "…sons de sílabas mediais e finais." |
| EF02MA06 | "…estratégias pessoais ou convencionais." | "…estratégias pessoais." |
| EF03MA05 | "…cálculo mental e escrito para resolver…" | "…cálculo mental e escrito, inclusive os convencionais, para resolver…" |
| EF05LP10 | "cartuns,," | "cartuns," |
| EF89LP19 | sem ponto final | com ponto final |
| EF67LP28, EF69LP53 | "infanto-juvenis", "infanto-juvenil" | "infantojuvenis", "infantojuvenil" |
| EF08MA09 | "ax² = b" | "ax2 = b" (sobrescrito perdido na planilha) |

### Diferenças de objetos de conhecimento

| Código | 2017 (este documento) | 2018 |
|---|---|---|
| EF04LP06 | Morfologia | Morfologia/Morfossintaxe |
| EF15AR13 | Contexto e práticas | Contextos e práticas |
| EF15AR24 | Matrizes estéticas culturais | Matrizes estéticas e culturais |
| EF09LI12 | Produção de textos escritos, com mediação do professor/colegas | (sem a vírgula) |
| EF02MA17 | …cm³… | …cm3… |
| EF08MA09 | …ax² = b | …ax2 = b |
| EF08MA20, EF08MA21 | Volume de cilindro reto | Volume de bloco retangular |

## Erros de extração encontrados e corrigidos durante o processo

O resultado acima é o da versão final do extrator. As primeiras rodadas tinham erros, e cada um virou regra no código:

| Erro | Causa | Correção |
|---|---|---|
| 13 habilidades de Ensino Religioso ausentes | Título do quadro mais abaixo quando há título de seção na página | Localizar o cabeçalho pela coluna "OBJETOS DE CONHECIMENTO" |
| EF09GE01 ausente | Código impresso sem "(" | Parêntese de abertura opcional (decisão 1) |
| Objetos vazios em dezenas de linhas | Fios parciais da página da direita contados como linha do quadro | Só fios da coluna de objetos (decisão 8) |
| Objeto partido em dois ("…alfabético/" + "Convenções…") | Parágrafo decidido só pelo espaçamento | Continuação por "/", "-" ou minúscula |
| Prática vazia em 13 habilidades de LP | Rótulo em fonte Medium, não Bold | Qualquer fonte não regular na coluna 1 |
| Nota de rodapé dentro do nome "Oralidade" | Nota impressa em negrito, em várias linhas | Nota começa em "*" e vai até o fim da célula |
| Campo de atuação errado em ~100 habilidades | Página com duas faixas: todas recebiam a última | Faixa mais próxima acima da habilidade |
| "gráficoespacial", "pósescrita" | Hífen real tratado como quebra | Conferência visual (decisão 4) |
| "o número como" | π perdido na camada de texto | Conferência visual (decisão 3) |

## Como reproduzir

```bash
pip install pymupdf
python PRD/BNCC/_pipeline/extrair.py saida.json
python PRD/BNCC/_pipeline/gerar_md.py saida.json PRD/BNCC
python PRD/BNCC/_pipeline/ver_pagina.py 309 "EF07MA33" ma33 80   # conferência visual de um trecho
```
