# Decisões de transcrição

> **Fonte:** *Base Nacional Comum Curricular* (EI e EF), MEC, versão homologada de 20/12/2017, `BNCC_20dez_site.pdf` (472 páginas PDF). Decisões tomadas na transcrição de 2026-11-04, cada uma conferida na página impressa (imagem renderizada) quando a camada de texto do PDF não bastava.

Regra geral: **o que a página imprime é o que a tabela traz**, inclusive erros do próprio documento. Nada é corrigido para ficar "certo"; o que é estranho fica registrado aqui.

## 1. EF09GE01 impresso sem o parêntese de abertura

Na PDF 393 (p. 391), o código aparece como `EF09GE01)`, sem o `(`. É o único caso no documento.

**Decisão:** reconhecer o código assim mesmo. A tabela traz `EF09GE01`.

## 2. Dois códigos impressos duas vezes, com textos diferentes

| Código | 1ª ocorrência | 2ª ocorrência |
|---|---|---|
| EF05LP25 | PDF 129: "Planejar e produzir, com certa autonomia, verbetes de dicionário…" (Produção de textos / Escrita autônoma) | PDF 133: "Representar cenas de textos dramáticos…" (Oralidade / Performances orais) |
| EF04LP27 | PDF 133: "Recitar cordel e cantar repentes e emboladas…" (Oralidade / Performances orais) | PDF 135: "Identificar, em textos dramáticos, marcadores das falas…" (Análise linguística/semiótica / Forma de composição de textos dramáticos) |

**Decisão:** manter as quatro linhas, cada uma na sua posição no quadro, marcadas com ⚠ em [21-lingua-portuguesa.md](21-lingua-portuguesa.md). O documento tem, portanto, 1.304 habilidades impressas e 1.302 códigos distintos no EF. Quem usar o código como chave precisa tratar esses dois casos.

## 3. π perdido na camada de texto (EF07MA33)

A camada de texto da PDF 309 traz "o número como a razão"; a página impressa mostra "o número **π** como a razão".

**Decisão:** prevalece a página impressa. A correção está no mapa `CORRECOES_VISUAIS` do extrator, com a página conferida.

## 4. Hífen no fim da linha

O documento é diagramado com hifenização: um hífen no fim da linha pode ser quebra silábica ("com-/preendendo") ou hífen da palavra ("gráfico-/espacial"). Para decidir, o extrator consulta o próprio documento: se a palavra aparece em outro trecho, no meio de linha, com hífen, o hífen fica; se aparece sem hífen, sai.

Dois casos não tinham evidência no documento e foram conferidos na imagem, ambos com hífen real:

| Palavra | Onde |
|---|---|
| gráfico-espacial | EF69LP48, PDF 159 |
| pós-escrita | Unidade temática de Língua Inglesa, 8º ano, PDF 256 |

Quando a quebra acontece numa palavra composta, o documento repete o hífen no início da linha seguinte ("reelaborando-/-as"). O extrator junta essas partes com um único hífen.

## 5. Barra no fim da linha

Quando a linha termina em `/` ("tema/" + "assunto"), as partes são unidas **sem espaço**: "tema/assunto". É a forma que o documento usa quando a mesma expressão cabe numa linha só.

Exceção: quando a página imprime a barra seguida de espaço **no meio da linha**, o espaço é mantido. É o caso de "Análise linguística/ semiótica" nos quadros de 8º e 9º anos de Língua Portuguesa; nos demais quadros, o documento imprime "Análise linguística/semiótica".

## 6. Sobrescritos, ligaduras e caracteres de controle

| Caso | O que a camada de texto traz | O que a tabela traz |
|---|---|---|
| Sobrescrito numérico | `cm3`, `ax2` | `cm³`, `ax²` (como impresso) |
| Ligaduras tipográficas | `ﬁ`, `ﬂ` | `fi`, `fl` |
| Caractere de controle do InDesign depois de "•" (História) | `•\x07Domínios` | `• Domínios` |
| Separador de linha Unicode | ` ` | espaço |

## 7. Peculiaridades do documento mantidas como impressas

Conferidas na página impressa:

| Código | O que o documento imprime | Página |
|---|---|---|
| EF05LP10 | "anedotas, piadas e cartuns,," (vírgula dupla) | PDF 121 |
| EF89LP19 | termina em "frente às propostas", **sem ponto final** | PDF 183 |
| EF69LP35 | "enciclopédia digital colaborativa , infográfico" (espaço antes da vírgula) | PDF 153 |
| EF01LP09 e EF01LP13 | o mesmo texto nos dois códigos: "Comparar palavras, identificando semelhanças e diferenças entre sons de sílabas iniciais, mediais e finais." | PDF 101 |
| Arte 1º ao 5º ano | objetos "Contexto e práticas" (Música) e "Matrizes estéticas culturais" | PDF 202 |

## 8. Estrutura das tabelas: o que vem da geometria da página

- **Linha do quadro (EF):** definida pelos fios horizontais da coluna "Objetos de conhecimento" (página da esquerda). Fios que aparecem só na página da direita subdividem a coluna de habilidades dentro de uma mesma célula de objetos.
- **Página dupla (EF):** os quadros ocupam duas páginas. Unidades temáticas (ou práticas) e objetos ficam na página da esquerda, e as habilidades na da direita, alinhadas pela altura.
- **Vários objetos numa célula:** separados quando o documento abre parágrafo (espaço maior que o entrelinha, ou item com "•"). Linhas que continuam a frase (começam em minúscula ou seguem uma linha terminada em `/` ou `-`) ficam no mesmo objeto.
- **Faixas:** "CAMPO …" e "TODOS OS CAMPOS DE ATUAÇÃO" em Língua Portuguesa, "EIXO …" em Língua Inglesa. Cada habilidade recebe a faixa mais próxima acima dela; o texto descritivo impresso na faixa vai como citação.
- **Nota de célula:** a célula "Oralidade" de LP 6º ao 9º ano traz a nota "*Considerar todas as habilidades dos eixos leitura e produção…". Ela é registrada como nota (em itálico) e não como parte do nome da prática.
- **Linha do quadro (EI):** objetivos impressos na mesma altura, nas três colunas de grupo etário, recebem o mesmo número de linha. É a relação "mesmo aspecto do campo" que o documento mostra lado a lado.

## 9. Capítulo "Estrutura da BNCC" fica fora do índice

As PDF 25 a 36 reproduzem, como exemplo de leitura dos quadros, 7 códigos (EI01TS01, EI02TS01, EI03TS01, EF01CI02, EF01CI03, EF01CI04, EF06HI14). Eles entram nas tabelas só pela ocorrência nos quadros normativos.

## 10. O que não foi transcrito em tabela

A prosa dos capítulos (apresentação, introdução, textos de área e de componente, descrição dos campos de experiências, textos de transição) não é tabela. Ficaram fora, por decisão de escopo. Ficaram dentro todas as listas e todos os quadros oficiais.
