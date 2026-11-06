# Decisões de transcrição

> **Fonte:** *Computação na Educação Básica: Complemento à BNCC*, `BNCCComputaoCompletodiagramado.pdf` (75 páginas PDF, criado em 13/04/2022). Decisões tomadas na transcrição de 2026-11-05, cada uma conferida na página impressa (imagem renderizada) quando a camada de texto do PDF não bastava.

Regra geral, a mesma de [../bncc/98-decisoes.md](../bncc/98-decisoes.md): **o que a página imprime é o que a tabela traz**, inclusive erros do próprio documento. Nada é corrigido para ficar "certo"; o que é estranho fica registrado aqui.

## 1. EF05CO11 impresso com três dígitos

Na PDF 36 (p. 32), o código aparece como `(EF05CO011)`. A sequência do 5º ano vai de EF05CO01 a EF05CO10 antes dele, e nenhum outro código usa três dígitos.

**Decisão:** reconhecer como `EF05CO11`. O índice ([90-indice-codigos.md](90-indice-codigos.md)) mostra o código impresso ao lado. Cuidado para quem busca por expressão regular: `EF05CO01` casa como prefixo de `EF05CO011`, e uma busca ingênua acha `EF05CO01` duas vezes.

## 2. Uma habilidade, duas linhas de explicação e exemplos

Os quadros ocupam página dupla: eixo, objeto e habilidade na esquerda; explicação e exemplos na direita, alinhados pela altura. Em três habilidades, a célula da esquerda corresponde a **duas** linhas na direita:

| Código | Página da direita | Origem das duas linhas |
|---|---|---|
| EF15CO02 | PDF 39 | as mesmas de EF01CO02 e EF01CO03 |
| EF15CO05 | PDF 41 | as mesmas de EF03CO04 e EF03CO05 |
| EF07CO01 | PDF 47 | duas linhas próprias |

**Decisão:** manter as duas, em ordem, como pares "Explicação (1 de 2) / Exemplos (1 de 2)" e "(2 de 2)". Nenhuma linha da direita abrange mais de uma habilidade da esquerda (o extrator falha se isso acontecer).

## 3. Anos finais: dois níveis de objeto e uma coluna sem título

Do 6º ao 9º ano (e no quadro "por etapa" 6º ao 9º), o quadro tem cinco colunas. O cabeçalho "OBJETO DE CONHECIMENTO" cobre duas (objeto e um segundo nível, ex.: "Programação" › "Tipos de dados") e o cabeçalho "HABILIDADE" cobre outras duas: uma sem código, com um enunciado que agrupa várias habilidades, e a da habilidade com código.

**Decisão:** quatro campos, com nomes nossos porque o documento não os nomeia: *Objeto de conhecimento*, *Objeto (2º nível)*, *Enunciado geral (sem código)* e *Habilidade*. O enunciado geral é repetido em cada linha que ele cobre, como os objetos no [../bncc/](../bncc/README.md). Nos anos iniciais o quadro tem três colunas (eixo, objeto, habilidade).

## 4. Competências do Ensino Médio: o quadro e a lista não dizem o mesmo

A lista da p. 61 (PDF 65) e a coluna "Competência específica" dos quadros do EM imprimem textos diferentes em três competências:

| Nº | Lista (PDF 65) | Quadro (coluna "Competência específica") |
|---|---|---|
| 4 | "…produzindo **conteúdos e artefatos** de forma criativa, com respeito às **questões éticas e legais**…" | "…produzindo **informação e/ou artefatos** de forma criativa, com respeito às **questões legais**…" (PDF 70) |
| 5 | "…próprias da Computação **preferencialmente** de maneira colaborativa." | "…próprias da Computação de maneira colaborativa." |
| 7 | "…recorrendo aos conhecimentos da Computação e suas tecnologias frente às questões…" | "…recorrendo aos conhecimentos da Computação e suas tecnologias **para tomar decisões** frente às questões…" |

**Decisão:** as duas versões ficam como impressas: a lista em [01-premissas-e-competencias.md](01-premissas-e-competencias.md), a do quadro no título de cada grupo em [30-ensino-medio.md](30-ensino-medio.md). O número da competência de cada habilidade vem da **ordem**: a k-ésima célula distinta do quadro é a competência k da lista. As sete aparecem em ordem e as outras quatro têm texto idêntico ao da lista, então a correspondência é inequívoca.

Uma coincidência que ajuda a ler o 7: a competência 7 do **Ensino Fundamental** (PDF 15) traz "para tomar decisões", como o quadro do EM.

## 5. "(cont.)" impresso nas células

Em EF09CO05 (PDF 58), as três células de contexto terminam em "(cont.)": "Sistemas distribuídos e internet (cont.)", "Segurança cibernética (cont.)" e o enunciado geral "…e da internet. (cont.)". É o marcador do documento para uma célula que continua da página anterior.

**Decisão:** manter como impresso. Quem agrupar habilidades por objeto deve retirar o sufixo " (cont.)" antes de comparar.

## 6. Hífen e barra no fim da linha

As mesmas regras do [../bncc/98-decisoes.md](../bncc/98-decisoes.md) (decisões 4 e 5): hífen no fim da linha se decide pelo léxico do próprio documento; barra no fim da linha une sem espaço. Casos conferidos:

| Caso | Onde | Decisão |
|---|---|---|
| vice-versa | EF05CO03, PDF 33 | hífen mantido (grafia obrigatória; sem ocorrência no meio de linha) |
| inglês-espanhol | EF69CO10, PDF 63 | hífen mantido (a mesma linha traz "português-inglês") |
| on-line | EF06CO09, PDF 45 | **ambíguo**: o documento usa "online" 19 vezes e "on-line" 2 vezes no meio de linha. Mantido o hífen impresso |
| "responsabilidad" + "e" | objeto de EF09CO06 a EF09CO09, PDF 58 | a coluna estreita parte a palavra **sem hífen**; unida como "responsabilidade" |
| "armazenamento/" + "processamento" | EF08CO05 (PDF 52) e EF69CO09 (PDF 62) | barra no fim da linha: "armazenamento/processamento" |
| endereço web partido em "-" ou "/" | exemplos | une sem espaço e mantém o caractere |

## 7. Quebras de linha na explicação e nos exemplos

As células da direita têm parágrafos, listas numeradas ("1)", "(i)", "•", "-", "Passo (1)") e endereços web. O PDF não marca quebra de linha; o extrator a reconstrói por regra declarada: espaço vertical maior que 1,5 entrelinha abre parágrafo; a linha seguinte começa com marcador de lista, ou a primeira palavra dela caberia na linha anterior, é quebra real; nos demais casos a frase continua.

**Limite conhecido:** quando uma frase termina rente à margem e a seguinte não começa com marcador, a quebra se perde e as duas frases ficam na mesma linha. Caso observado: "…(e.g. dobraduras, bordado, costura). Exemplo: Executar o seguinte algoritmo" em EI03CO03 (PDF 7), que a página imprime em duas linhas. **O texto não muda, só a disposição.**

## 8. Eixos em caixa alta, normalizados

A página imprime o eixo em caixa alta e, no EF, girado 90°. A tabela traz o nome normalizado (Pensamento Computacional, Mundo Digital, Cultura Digital); o JSON guarda também a forma impressa. O extrator falha com qualquer eixo fora desses três.

## 9. Peculiaridades do documento mantidas como impressas

| O quê | Onde |
|---|---|
| EF06CO01 termina em "‘tipo de dados’", **sem ponto final** (o gêmeo EF69CO01 tem ponto e diz "tipo de dado") | PDF 42 |
| Habilidades com **texto idêntico** a outra: EF03CO03 = EF15CO04; EF05CO03 = EF15CO03; EF06CO02 a EF06CO08 = EF69CO02 a EF69CO08; EF06CO09 = EF69CO11; EF06CO10 = EF69CO12; EF08CO05 = EF69CO09; EF08CO06 = EF69CO10; EF07CO03 = EF08CO04 = EF09CO02 | 14 grupos |
| **Explicação e exemplos repetidos** entre o quadro do ano e o quadro "por etapa" (ex.: EF01CO01 e EF15CO01) | 12 pares |
| Só o grupo etário 03 (crianças pequenas) tem objetivos na EI | PDF 6 a 12 |

Quem usar o texto como chave (ex.: para achar o código a partir do enunciado) precisa tratar os textos repetidos.

## 10. Endereços web

Os exemplos citam 17 endereços (jogos, ferramentas, materiais). Ficam como impressos, **sem acesso nem verificação**: em 2026 alguns podem estar fora do ar ou ter mudado de conteúdo.

## 11. O que não foi transcrito

Capa e páginas sem camada de texto (PDF 1, 2 e 4), sumário (PDF 3), páginas separadoras (PDF 14 e 64) e os títulos de abertura de etapa. Ficaram dentro todos os quadros e as três listas numeradas (premissas da EI, competências do EF e do EM), com o parágrafo de introdução das premissas.

## 12. Identidade do documento

Metadados do PDF: título "Computação na Educação Básica - Complemento à BNCC", autor "Christian Brackmann", criado no Serif Affinity Publisher em 13/04/2022. O nome do arquivo diz "diagramado". A paginação coincide registro a registro (141 de 141) com a do anexo ao Parecer CNE/CEB nº 2/2022 que o bncc-dados usa como fonte (`anexo-ao-parecer-cneceb-no-2-2022-bncc-computacao.pdf`), o que indica que o arquivo tem a mesma diagramação. **[A CONFIRMAR]** contra o arquivo publicado pelo MEC: não foi baixado nem comparado byte a byte.
