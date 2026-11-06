---
título: Transformar em VUOO — receita para o agente
produto: VUOO, microjogos para crianças (CIATec/EACH-USP, Wemoga Software Studio)
atualizado_em: 2026-10-31
status: receita viva — o estilo vem de guia-pratico-design.md §6; os valores de cor vêm de ferramentas/paleta.json
---

# Transformar em VUOO — receita para o agente

Este documento é para um agente que recebe **uma forma qualquer** — desenho em papel, foto, imagem, SVG ou arquivo do Illustrator — e precisa devolver **a mesma coisa no estilo de ilustração do VUOO**, como SVG pronto para animar em código, Lottie ou Rive.

Siga as etapas na ordem. Cada etapa termina numa decisão que vai para o relatório final (§12). Quando uma regra daqui não decidir um caso, escolha a opção **mais simples**, registre a escolha no relatório e siga em frente.

**Fontes:**
- **Cores:** `ferramentas/paleta.json`, tokens que começam com `il-` (rampas de ilustração) e os tokens `tinta`, `superficie`, `flor`, `ceu`, `lavanda`, `folha`, `contorno`. Nunca digite um hex de memória; copie do JSON.
- **Estilo e regras de personagem:** `guia-pratico-design.md` §6. Se este documento e o guia divergirem, vale o guia.

---

## 0. Antes de começar: dá para transformar?

Pare e avise, sem transformar, se a entrada for:

| Entrada | O que fazer |
|---|---|
| Marca, logo, o Bot ou um pictograma de interface | Não transformar. Eles têm regras próprias (guia §1, §2, §5) e não seguem este estilo |
| Estímulo de um bloco de medida (forma ou cor que o protocolo de pesquisa define) | Não transformar. Forma e cor vêm do protocolo; avise quem pediu |
| Personagem, mascote ou marca de terceiros reconhecível | Não transformar. Avise e peça uma forma original |
| Arma ou objeto feito para ferir | Não transformar. Avise |

Siga com cuidado (transforme, mas registre) se a entrada tiver algo ameaçador que dá para suavizar: dentes, garras, fogo, bicho bravo. O VUOO não tem vilões (guia §6).

---

## 1. Ler a entrada

O resultado desta etapa é a **ficha de leitura**, preenchida antes de desenhar qualquer coisa:

```
O que é:            (ex.: geladeira de duas portas)
Tipo:               objeto | objeto com rosto | pessoa/avatar | cenário   (ver §2)
Vista da origem:    frontal | lateral | 3/4
Partes:             lista, da maior para a menor (ex.: corpo, porta de cima, porta de baixo, 2 puxadores)
Proporção:          largura:altura do conjunto (ex.: 1:1,8)
Cores reais:        por parte (ex.: corpo branco, puxadores cinza)
Alvo de toque?:     sim | não   (a criança toca nele no jogo?)
Tamanho na tela:    menor tamanho em que vai aparecer (padrão: 64 px)
Conjunto:           cenário onde vai morar (Cerrado, Quintal, Feira, Rio, Cidade, Casa, Ninho) — ver §5
Emoção pedida:      nenhuma | atento | contente | curioso | pensando | sossegado
```

Como ler cada tipo de entrada:

### Desenho em papel (foto ou digitalização)

- O que interessa é **a forma**. Ignore a textura do papel, a sombra da foto, manchas, linhas de rascunho e de construção.
- O traço de lápis ou caneta marca **a borda de uma forma**, não vira traço no resultado.
- Hachura e sombreado à mão não viram sombra. No máximo indicam onde fica o tom interno.
- Quando uma linha pode ser parte do objeto ou rascunho, escolha a leitura mais simples e registre.

### Imagem (foto real ou ilustração em outro estilo)

- Extraia a silhueta e as partes; descarte a luz e a sombra da foto. No VUOO, a luz vem sempre do alto à esquerda, qualquer que seja a luz da foto.
- Texto, número, rótulo e marca de produto são **removidos** (ex.: o logotipo da geladeira).
- Se a imagem estiver muito escura ou cortada e a forma não der para ler, pare e peça outra.

### SVG

- Abra e leia a estrutura: grupos, quantidade de paths, quantidade de nós, traços (`stroke`), gradientes, filtros, máscaras.
- Use o SVG como **referência de proporção**, não como base para editar. Um SVG de outra origem quase nunca tem as partes separadas do jeito que a animação precisa; redesenhar com formas básicas (§3) costuma ser mais rápido e sempre dá resultado mais limpo.
- Um traço que é **parte do objeto** (fio, haste, cabo) vira forma preenchida com a espessura mínima (§3). Um traço que é **só contorno** desaparece.

### Arquivo do Illustrator (via MCP)

- Liste as camadas, pranchetas e objetos antes de mexer. **Nunca altere o original:** crie uma prancheta ou camada nova chamada `VUOO` e trabalhe nela.
- Crie no documento um grupo de amostras globais chamado `VUOO ilustração`, com uma amostra por token `il-*` usado, nomeada com o token. Pinte só com essas amostras.
- Efeitos ao vivo, estilos gráficos, aparências múltiplas, símbolos e pincéis precisam ser **expandidos ou removidos** antes de exportar; nada disso sobrevive à exportação para Lottie ou Rive.
- O nome de cada camada ou grupo é o `id` que vai para o SVG (§9).
- **Nunca entregue o resultado de vetorização automática** (Rastreamento de imagem / Image Trace). Ela gera centenas de nós e não anima. Pode usar o rastreamento como guia de proporção, numa camada que será apagada.

---

## 2. Classificar

| Tipo | Prancheta | Máximo de paths | Máximo de rampas | Menor detalhe |
|---|---|---|---|---|
| Objeto | 512 × 512 | 20 | 3 | 24 unidades |
| Objeto com rosto | 512 × 512 | 30 (rosto incluído) | 3 + `tinta` + bochecha | 24 unidades |
| Pessoa ou avatar | 512 × 512 | 40 | pele + cabelo + 2 de roupa | 24 unidades |
| Cenário | 1920 × 1080 | 200 | 5 | 32 unidades |

- **Margem de 32 unidades** em toda prancheta de objeto: nada encosta na borda.
- O "menor detalhe" é a menor largura que qualquer parte pode ter. Numa prancheta de 512 exibida a 64 px, 24 unidades viram 3 px — abaixo disso, a parte some.
- No máximo **24 nós por path.**

---

## 3. Simplificar e reconstruir com formas básicas

### 3.1 Cortar partes

1. Comece pela lista de partes da ficha de leitura.
2. Retire as partes da menor para a maior, enquanto o objeto **continuar reconhecível só pela silhueta**, preenchida de uma cor só, a 64 px.
3. Pare quando a próxima remoção atrapalhar o reconhecimento ou quando estiver dentro do limite de paths (§2), o que vier primeiro.
4. Itens repetidos (botões do fogão, folhas de uma árvore, pintas do morango) viram **3 a 5** unidades, agrupadas.

### 3.2 Reconstruir

- Cada parte é **uma forma básica, ou a soma de até três**: retângulo arredondado, círculo/oval, triângulo arredondado.
- **Mantenha a proporção principal** da ficha de leitura, com até 10% de diferença.
- **Engorde o que é fino:** toda parte fina (cabo, perna, haste, fio) ganha pelo menos o "menor detalhe" de §2. Se mesmo assim não ler, remova.
- **Se a origem é quase simétrica, deixe simétrica.**
- **Cantos:** todo canto tem raio entre **15% e 25% do menor lado da forma**, com mínimo de 8 unidades. Ponta de triângulo, raio mínimo de 10% do lado. Nenhum canto vivo.
- **Grade de 8 unidades:** posições e tamanhos em múltiplos de 8 sempre que possível.

### 3.3 Vista

- Mantenha a vista da origem: frontal, lateral ou 3/4.
- **3/4 simplificado:** no máximo dois planos visíveis (frente e um lado), lados paralelos, sem linhas de fuga. O lado aparece com no máximo 1/3 da largura da frente e fica no tom interno.
- Se a origem tem perspectiva forte (vista de cima, de baixo, linhas de fuga), converta para a vista mais reconhecível do objeto (em geral, frontal) e registre.

---

## 4. Tirar o que não existe no VUOO

| Se você vê | Faça |
|---|---|
| Contorno ou linha preta em volta das formas | Remova. As formas se separam pela cor; duas partes vizinhas da mesma rampa se separam pelo tom interno |
| Sombra projetada no chão ou em outra forma | Remova. Sem substituto |
| Gradiente | Troque por base + tom interno chapados |
| Textura (madeira, tecido, casca, pelo) | Remova. No máximo um padrão de 3 a 5 formas pequenas repetidas (veios, pintas), no tom interno |
| Reflexo ou brilho complexo | Uma única forma de luz (§5) |
| Transparência (vidro, água, plástico) | Cor chapada da rampa `il-rio`, opacidade 100% |
| Ponta viva, quina | Arredonde (§3.2) |
| Texto, número, logotipo, marca de produto | Remova |
| Rosto num objeto, sem emoção pedida | Remova o rosto |
| Expressão triste, brava, assustada | Troque por "atento" e registre |
| Dentes, garras, olhar ameaçador | Arredonde e suavize até não ameaçar; dentes e garras somem |
| Vermelho num objeto que não é vermelho na vida real | Troque pela rampa mais próxima (`il-laranja` ou `il-ipe-roxo`) |
| Uma cor de interface (`ceu`, `sol`, `folha`, `lavanda`, `flor`, `brisa`) pintando o objeto | Troque pela rampa de ilustração equivalente (§5) |
| Efeito 3D, volume renderizado | Achate: base + tom interno + luz |

---

## 5. Pintar

### 5.1 Escolher a rampa de cada parte

| Cor real | Rampa |
|---|---|
| verde (folha, grama, legume) | `il-mato` |
| amarelo, dourado | `il-ipe` |
| laranja | `il-laranja` |
| vermelho — **só se for vermelho na vida real** (maçã, tomate, morango, semáforo) | `il-fruta` |
| roxo, lilás | `il-ipe-roxo` |
| rosa | `il-ipe-roxo` em rampa clara (abaixo) |
| azul, água, céu, vidro | `il-rio` |
| marrom, bege, madeira, pão | `il-terra` |
| cinza, metal, pedra | `il-pedra` |
| preto (pneu, panela) | `il-cabelo-preto` |
| branco | `il-casca` |
| pele | `il-pele-1` a `il-pele-6` — se a pessoa não estiver definida, escolha e registre |
| cabelo | `il-cabelo-*` |

- **Limite de rampas** por tipo (§2). Se passar, junte as partes de cor parecida na mesma rampa.
- Se o objeto vai para um cenário, prefira as rampas do conjunto:

| Conjunto | Rampas | Fundo | Chão |
|---|---|---|---|
| Cerrado | mato, ipê, terra, pedra, rio | `il-rio-luz` | `il-terra` |
| Quintal | mato, terra, laranja, fruta, casca | `il-rio-luz` | `il-mato` |
| Feira | fruta, laranja, ipê, mato, ipê-roxo | `papel` | `il-terra-luz` |
| Rio | rio, mato, pedra, terra | `il-rio-luz` | `il-rio` |
| Cidade do interior | pedra, casca, ipê-roxo, terra, rio | `il-rio-luz` | `il-pedra-luz` |
| Casa (interior) | casca, pedra, terra, rio, ipê | `il-terra-luz` | `il-terra` |
| Ninho (descanso) | rio, ipê-roxo, pedra | `lavanda-claro` | `il-pedra-luz` |

- **Rampa clara**, para objetos claros de uma cor só (rosa, lilás): base = `-luz`, tom interno = base, brilho = `superficie`.

### 5.2 Base, tom interno e luz

Para cada parte:

1. **Base:** a forma inteira, na cor base da rampa.
2. **Tom interno:** uma forma chapada no tom `-tom`, colada na borda **de baixo e da direita** da parte, ocupando **20% a 35% da área** dela.
   - Numa forma redonda, é um crescente. Numa forma retangular, uma faixa em L ou só na base.
   - O tom interno **acompanha a borda** da base (mesma curva), nunca é um retângulo solto por cima.
3. **Luz (opcional):** no máximo **uma** forma pequena por parte grande, no tom `-luz`, no alto à esquerda, com até **10% da área** da parte. Peças pequenas não levam luz.

A luz vem **sempre** do alto à esquerda, em todo objeto e em todo cenário.

---

## 6. Contraste sem traço

Sem contorno, a silhueta depende do fundo. Faça o teste com a função de contraste do script:

```
cd ferramentas
python3 -I -c "import sys; sys.path.insert(0, '.'); from contraste import contraste; print(round(contraste('#F2EFE6', '#F7F4EC'), 2))"
```

| Situação | Exigência | Se falhar |
|---|---|---|
| Objeto que a criança precisa reconhecer | Pelo menos metade da borda externa (somando base e tom interno que encostam no fundo) com **3:1** contra o fundo | Troque o fundo por outro do conjunto; se ainda falhar, use um palco |
| Objeto que é alvo de toque | Sempre sobre um **palco**: cartão com raio de 20 px e borda `contorno` de 2 px, fundo `superficie` | Objetos `il-casca` e `il-ipe`: palco `il-terra-tom`; `il-casca` também pode usar `il-rio-tom` |
| Objeto só decorativo | Sem exigência | — |
| Olhos e boca sobre a face | `tinta` com no mínimo 3:1 sobre a base (já validado para todas as rampas, exceto `il-pele-5` e `il-pele-6`) | Sobre `il-pele-5` e `il-pele-6`, o olho ganha esclera oval `superficie` |

O palco é um componente da interface, não da ilustração: entregue o objeto sem palco e registre no relatório "precisa de palco: sim, cor X".

---

## 7. Rosto e emoção (só quando pedido)

Um objeto só ganha rosto quando a ficha de leitura pede uma emoção. Regras do guia (§6), resumidas:

- O objeto **nunca fala**. Só o Bot fala.
- Só cinco emoções. Nunca triste, bravo, com medo ou decepcionado.
- A emoção vem da história do jogo, **nunca** de a criança acertar ou errar.

| Emoção | Olhos | Boca | Corpo | Bochechas |
|---|---|---|---|---|
| atento | dois ovais | linha reta curta | reto | sem bochechas |
| contente | arcos para cima | curva para cima | estica 5% na vertical | `flor` |
| curioso | olho esquerdo maior (sempre o esquerdo) | pequeno "o" | inclina 8° | `ceu` |
| pensando | ovais olhando para cima e para a direita | linha inclinada | reto | `lavanda` |
| sossegado | ovais com pálpebra superior reta | curva leve para cima | achata 5% e alarga 5% | `folha` |

**Medidas:**
- **Rosto:** na face principal do objeto (a porta da geladeira, a frente do pote), no terço de cima.
- **Olhos:** ovais `tinta`, com altura de 8% a 12% da altura do objeto, afastados um olho e meio entre si, com um ponto de brilho `superficie` no alto à esquerda.
- **Boca:** `tinta`, com largura de cerca de 1,5 olho, centrada abaixo dos olhos.
- **Bochechas:** dois ovais, cada um com até 3% da área da face, abaixo e por fora dos olhos. É o **único** lugar onde uma cor de interface entra numa ilustração.
- **Objetos não têm sobrancelhas.**
- **Deformação do corpo:** estica, inclina e achata não são desenhados. A animação aplica a deformação a partir do ponto de giro do `corpo` (§9); entregue o corpo na proporção original.
- **Várias emoções:** entregue **um SVG com um grupo de rosto para cada emoção pedida**, sempre incluindo o `rosto-atento`. Só o `rosto-atento` fica visível; os outros têm `display="none"`.

---

## 8. Pessoas e avatares

- **Proporção:** cabeça com 1/3 da altura total no tema de 6–8 anos, e com 1/4 no tema de 9–12 anos.
- **Rosto:** olhos `tinta` (com esclera em `il-pele-5` e `il-pele-6`), sobrancelha opcional em `tinta` ou no tom do cabelo, boca `tinta`, sem nariz ou nariz em tom interno da pele.
- **Mãos:** uma forma arredondada, sem dedos separados (no máximo o polegar).
- **Diversidade:** óculos, aparelho auditivo, cadeira de rodas, abafador de ruído, entre outros, aparecem como mais uma parte do desenho, sem destaque.
- **Emoções:** a mesma tabela de §7, com sobrancelha opcional.
- **Avatares:** cada avatar novo precisa se diferenciar dos outros **pela silhueta** (cabelo, acessório, roupa), não só pela cor.

---

## 9. Montar o SVG

### Estrutura

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <title>Geladeira</title>
  <desc>Geladeira branca de duas portas, vista frontal, contente.</desc>
  <g id="geladeira">
    <g id="corpo" data-pivo="256 480">
      <path id="corpo-base" class="il-casca" fill="#F2EFE6" d="…"/>
      <path id="corpo-tom" class="il-casca-tom" fill="#D8D3C6" d="…"/>
    </g>
    <g id="porta-cima" data-pivo="128 120">
      <path id="porta-cima-base" class="il-casca" fill="#F2EFE6" d="…"/>
      <path id="porta-cima-tom" class="il-casca-tom" fill="#D8D3C6" d="…"/>
      <path id="porta-cima-luz" class="il-casca-luz" fill="#FFFFFF" d="…"/>
    </g>
    <g id="puxador-cima">…</g>
    <g id="rosto-atento">…</g>
    <g id="rosto-contente" display="none">
      <g id="olho-esq" data-pivo="…">…</g>
      <g id="olho-dir" data-pivo="…">…</g>
      <path id="boca" class="tinta" fill="#2B2D42" d="…"/>
      <path id="bochecha-esq" class="flor" fill="#CC79A7" d="…"/>
      <path id="bochecha-dir" class="flor" fill="#CC79A7" d="…"/>
    </g>
  </g>
</svg>
```

### Regras

- **Um `<g>` raiz** com o nome do objeto e **um `<g>` por parte**. Ids em português, minúsculas, sem acento, separados por hífen (`porta-cima`, `olho-esq`). Os nomes `corpo`, `olho-esq`, `olho-dir`, `boca`, `bochecha-esq`, `bochecha-dir` e `rosto-<emocao>` são fixos.
- **Dentro de cada parte, no máximo três paths**, nesta ordem de empilhamento: `-base`, `-tom`, `-luz`.
- **Cor:** `fill` com o hex exato do `paleta.json` **e** `class` com o nome do token. O hex garante que Lottie e Rive importem certo; a classe permite trocar a cor por código (Modo suave, outro conjunto).
- **Ponto de giro:** `data-pivo="x y"` em todo grupo que pode se mexer (corpo, portas, braços, olhos, folhas). No `corpo`, o ponto fica no centro da base.
- **Ordem do arquivo = ordem de empilhamento:** de trás para a frente.
- **Coordenadas absolutas**, arredondadas para 1 casa decimal; transformações aplicadas nos paths (nenhum `transform` sobrando, exceto se for intencional para animação).

**Proibido no arquivo:** `stroke` (todo elemento sem traço), `linearGradient`, `radialGradient`, `filter`, `mask`, `clipPath`, `pattern`, `image`, `text`, `opacity` ou `fill-opacity` diferentes de 1, `<use>`, estilos em CSS embutido.

### Modo suave

Não entregue um segundo arquivo. O Modo suave é aplicado por código: cada cor `il-*` perde 30% de saturação (HSL), mantendo matiz e luminosidade. Por isso a `class` com o token é obrigatória.

---

## 10. Testes de aceite

Rode todos antes de entregar. Cada um entra no relatório com "ok" ou com o que foi feito.

1. **Silhueta:** preenchida de uma cor só, a 64 px, ainda se reconhece o que é.
2. **Tamanho:** a 64 px, nenhuma parte some ou vira borrão. Se houver ferramenta de renderização (ex.: `rsvg-convert -w 64`), gere o PNG e olhe; se não houver, confira o "menor detalhe" (§2) parte a parte.
3. **Contagem:** paths, nós por path e rampas dentro dos limites (§2).
4. **Cores:** todo `fill` é um hex do `paleta.json` com a `class` correspondente; nenhuma cor de interface fora das bochechas; `il-fruta` só em objeto vermelho na vida real.
5. **Contraste:** o teste de §6 feito contra o fundo do conjunto ou contra o palco.
6. **Proibidos:** nenhum elemento ou atributo da lista de §9.
7. **Estrutura:** todo grupo e path tem `id`; partes móveis têm `data-pivo`; com rosto, existe `rosto-atento` visível.
8. **Luz:** todo tom interno embaixo e à direita, toda luz no alto à esquerda.
9. **Cantos:** nenhum canto vivo.
10. **Tom:** nada ameaçador, nada triste, nenhum texto, nenhuma marca.

---

## 11. Exemplos

### Maçã (foto)

- **Leitura:** objeto, vista frontal, partes: corpo, cabinho, folha. Vermelho na vida real. Alvo de toque num jogo de feira.
- **Simplificar:** o reflexo da foto vira uma luz; as pintinhas e a textura somem; o cabinho fino engorda para 24 unidades.
- **Reconstruir:** o corpo é um círculo achatado com uma reentrância no alto (dois círculos somados); o cabinho é um retângulo arredondado inclinado 10°; a folha é uma gota (círculo + triângulo arredondado).
- **Pintar:** corpo `il-fruta` (permitido: é vermelha na vida real), crescente `il-fruta-tom` embaixo à direita, luz `il-fruta-luz` no alto à esquerda; cabinho `il-terra`; folha `il-mato` com tom interno. Três rampas.
- **Contraste:** `il-fruta` sobre `papel` tem 3,4:1. Como é alvo, vai sobre palco `superficie`.

### Geladeira contente (desenho em papel)

- **Leitura:** objeto com rosto, vista frontal, partes: corpo, porta de cima, porta de baixo, dois puxadores, uma faixa de ímãs desenhada no papel. Emoção pedida: contente. Conjunto: Casa.
- **Simplificar:** os ímãs (rabiscos) saem, porque não são necessários para reconhecer; o logotipo desenhado sai.
- **Reconstruir:** corpo e portas são retângulos arredondados com raio de 20% da largura; os puxadores são retângulos arredondados verticais de 24 unidades de largura.
- **Pintar:** `il-casca` no corpo e nas portas, com tom interno numa faixa à direita de cada porta; puxadores `il-pedra`. Duas rampas.
- **Rosto:** na porta de cima. Grupo `rosto-atento` (visível) e grupo `rosto-contente` (oculto, olhos em arco, boca curva, bochechas `flor`).
- **Contraste:** `il-casca` não tem contraste sobre fundo claro. Registro: "precisa de palco: sim, `il-terra-tom`" se for alvo; se for cenário, o fundo `il-terra-luz` da Casa não basta — o agente avisa que a geladeira só se lê como decoração.

### Cadeira (SVG com traço)

- **Leitura:** o SVG tem 312 paths, todos com `stroke` preto de 3 px e preenchimento branco; vista 3/4 com perspectiva.
- **Decisão:** usar só como referência de proporção e redesenhar (§1, SVG).
- **Reconstruir:** vista 3/4 simplificada: frente (encosto + assento) e um lado estreito em tom interno; quatro pernas viram duas visíveis na frente e uma atrás, cada uma com 32 unidades.
- **Pintar:** `il-terra` (madeira), veios da madeira viram três traços curtos no tom interno. Uma rampa.

### Ipê-amarelo para cenário (Illustrator)

- **Leitura:** cenário Cerrado; o arquivo tem 40 camadas, com pincéis e um gradiente no céu.
- **Illustrator:** criar a prancheta `VUOO` de 1920 × 1080, criar as amostras globais `il-*`, deixar o original intacto.
- **Simplificar:** copa = 4 círculos sobrepostos em `il-ipe` com tom interno em dois deles; tronco = dois retângulos arredondados em `il-terra`; o gradiente do céu vira o fundo chapado `il-rio-luz`; o chão vira `il-terra`; flores caídas = 5 círculos de 32 unidades.
- **Exportar:** expandir pincéis; conferir que nenhum `stroke` sobrou; ids `copa`, `tronco`, `chao`, `flores-caidas`, com `data-pivo` na base da copa (para balançar).

---

## 12. Relatório de entrega

Entregue o SVG e, junto, este relatório curto:

```
Objeto:              (nome)
Origem:              papel | imagem | SVG | Illustrator — (arquivo)
Tipo:                objeto | objeto com rosto | pessoa/avatar | cenário
Vista:               frontal | lateral | 3/4 (simplificado de: …)
Partes mantidas:     (lista)
Partes removidas:    (lista e por quê)
Rampas:              (tokens)
Conjunto:            (nome)
Emoções no arquivo:  atento [, …]
Precisa de palco:    não | sim, cor (token)
Contagem:            N paths, maior path com N nós
Testes (§10):        1 ok · 2 ok · … (ou o que foi feito)
Decisões tomadas:    (toda escolha que este documento não decidia)
Dúvidas para o time: (se houver)
```
