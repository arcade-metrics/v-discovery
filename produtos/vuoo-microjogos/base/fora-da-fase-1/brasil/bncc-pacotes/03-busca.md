# Busca textual

> **Fonte:** [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes), commit `e9b4985`: `DECISOES.md` D10, `packages/bncc/src/busca.ts`, `packages/bncc/src/nucleo.ts` (`indiceBusca`, `buscar`), `python/bncc/_busca.py`, `packages/bncc/test/nucleo.test.ts`, `CHANGELOG.md` (0.4.0 a 0.6.0), issues #8, #9 e #14 citadas no changelog. Analisado em 2026-11-04.
>
> Inspirar, não copiar: ver o aviso em [README.md](README.md). Descrevemos o desenho para entender as escolhas; uma busca do VUOO será desenhada para o nosso corpus e o nosso público.

## O problema que motivou o desenho

Até a 0.4.0 a busca era por substring. Medido pelo projeto: `fração` e `frações` devolviam conjuntos disjuntos; a palavra `de` casava 94% da Base; `texto` devolvia 394 registros, 254 deles só porque continham `contexto`, e sem ordem o cliente via os primeiros do arquivo. Para uma fonte anti-alucinação, "zero resultados" ou ruído confirmam ao modelo que o dado não existe.

A evolução foi em três passos, cada um uma versão:

| Versão | Mudança |
|---|---|
| 0.4.0 (issue #9) | consulta por palavras em qualquer ordem, pontuação ignorada; ainda sem ranking |
| 0.5.0 (issue #14) | ranking determinístico: radical, palavras vazias, BM25, estratos |
| 0.6.0 | ranking extraído para funções puras exportadas, para o navegador obter a mesma ordem |

## O algoritmo, passo a passo

**1. Normalização.** Decomposição Unicode e remoção de diacríticos, minúsculas, espaços únicos. Na consulta, pontuação vira espaço.

**2. Palavras vazias.** Lista fixa e curta, idêntica em TS e Python (39 palavras: artigos, preposições, contrações, pronomes possessivos, `que`, `como`, `sobre`, `entre`, `etc`). Consulta formada só por elas devolve vazio, de propósito.

**3. Radical por regras curtas** (não é um stemmer completo). Palavras de até 3 letras ficam como estão. Depois, nesta ordem, e só se sobrarem pelo menos 3 letras:

- plural: `coes→cao`, `oes→ao`, `aes→ao`, `ais→al`, `eis→el`, `ois→ol`, `is→il`, `ns→m`, `res→r`, `zes→z`, `ses→s`, `s→∅`;
- sufixo forte (se casar, para aqui): `mente→∅`, `cao→c`, `ao→∅`;
- vogal final de gênero (`a`, `o`, `e`) em palavras de 5 letras ou mais;
- derivacionais: `cionari→c`, `cional→c`, `idad→∅`, `ment→∅`.

Alvo declarado: `fracao`, `fracoes` e `fracionario` no mesmo radical, sem que `texto` case `contexto`. Colisões conhecidas e **aceitas por escrito**: `conta`/`conto`, `lida`/`lido`, `educacao`/`educacional`. A tabela palavra → radical é teste unitário nas duas linguagens.

**4. Índice com campos estruturais.** Cada aprendizagem é indexada pelo enunciado **e** pelos nomes dos seus campos estruturais (componente, área, campo de experiências, eixo, unidade temática ou prática, objetos de conhecimento), estes com peso 0,5. O projeto chama isso de "contextual retrieval de graça": como o dado já é estruturado, o contexto não precisa ser gerado.

**5. Pontuação BM25** com k1 = 1,2 e b = 0,75, IDF na forma `ln(1 + (N − df + 0,5) / (df + 0,5))`, arredondada a 3 casas e devolvida em `pontuacao`. O arredondamento existe para que diferenças de último bit entre JavaScript e Python não troquem posições.

**6. Estratos** (aplicados antes da pontuação):

| Ordem | Estrato | Condição |
|---|---|---|
| 0 | idêntico | enunciado normalizado igual à consulta |
| A | literal | casa todos os radicais **e** contém a consulta literal (só para consultas de 2+ palavras) |
| B | todos | casa todos os radicais |
| C | parcial | casa parte dos radicais, **só se 0, A e B estiverem vazios** |

Dentro de cada estrato, pontuação decrescente; empate desfeito por código em ordem lexicográfica. Resultado: ordem totalmente determinística e reproduzível.

Por que cada estrato existe:

- **Idêntico:** um enunciado mais longo que contém a consulta pode pontuar mais no BM25 (EF08GE05 contém o texto de EF08HI06). Testado: buscando cada uma das 1.721 aprendizagens pelo próprio enunciado, só 16 não vêm em primeiro, e todas têm texto idêntico ao de outro código.
- **Literal só com 2+ palavras:** com uma palavra, reintroduziria a diferença singular/plural que o radical acabou de apagar.
- **Parcial como última passada:** com casamento parcial sempre ligado, o enunciado completo de EF05CO11 passaria de 1 para 47 resultados e o de EI01ET06 para 422. O `total` deixaria de servir ao caso de uso "tenho o enunciado, qual é o código?" (lookup inverso), que motivou a issue #9. Medido em 26/09/2026.

**7. Filtros como predicado.** Etapa, componente e ano são aplicados como função `aceitar(i)` sobre o índice, sem alterar a pontuação dos demais (o IDF continua calculado sobre o corpus inteiro).

## Uma implementação, também no navegador

As interfaces com busca própria (o site e outra interface) filtravam por substring, cada uma com sua regra. Na 0.6.0 o ranking virou funções puras no subpath `@bncc/dados/busca`, sem dados e sem Node:

- `indiceBusca()` devolve a forma serializável: `{codigo, texto, k, kc}` por aprendizagem, onde `k` e `kc` são os radicais do enunciado e dos campos, separados por espaço.
- `prepararIndice(entradas)` calcula frequências, df e tamanho médio.
- `ranquear(indice, consulta, aceitar?)` devolve `{i, pontuacao}`.

A página web baixa o índice como JSON (sem os dados completos), roda `ranquear` e obtém **a mesma ordem e a mesma pontuação** de `buscar()`. Um teste nos dois pacotes prova a equivalência para todas as consultas de busca da fixture.

## Explicabilidade como regra

A descrição da tool `bncc_buscar` diz em uma frase como a ordem é calculada, que plural, gênero, acento e palavras vazias não importam, e quando entra o casamento parcial. O agente que consome sabe o que esperar e como refinar.

## O que ficou de fora, por decisão

- **Busca semântica por embeddings.** É camada inferida, precisa de modelo e de rótulo próprio. Outra decisão, se a léxica não bastar.
- **Golden set de busca com taxa de acerto medida.** Sugerido na issue #14 a partir do bncc-benchmark, mas não existe no repositório.
