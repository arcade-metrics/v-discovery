---
título: Guia prático de design — VUOO
produto: VUOO, microjogos para crianças (CIATec/EACH-USP, Wemoga Software Studio)
atualizado_em: 2026-10-31
status: guia vivo — usar como referência única de design; não depende de nenhum outro documento
---

# Guia prático de design — VUOO

## O que é o VUOO, em um parágrafo

O VUOO é um produto educacional para crianças do ensino fundamental (6 a 12 anos), usado na escola em tablet ou celular, individualmente ou em dupla. A criança joga **microjogos curtos** guiada por um personagem companheiro, o **Bot**. Alguns microjogos têm, dentro deles, um **bloco de medida**: uma pesquisa científica externa (protocolo do CIATec) usa esse bloco para medir funções cognitivo-motoras (atenção, memória, controle inibitório etc.) e precisa que ele siga regras rígidas de apresentação. A professora acompanha o progresso num **painel**, em linguagem simples e sem comparação entre crianças. Este guia cobre tudo que é preciso para desenhar, ilustrar, escrever ou implementar uma tela do VUOO — e só este documento.

## Resumo de uma página — o que nunca muda

- **Sem vermelho na interface.** Erro não é perigo. A única exceção é ilustrar um objeto que é vermelho na vida real (maçã, tomate), com a rampa `il-fruta` (§6).
- **Objetos, personagens e cenários seguem o estilo do Duolingo: formas simples, sem traço de contorno, volume por tom interno.** Isso não vale para a marca, o logo e o Bot (§6).
- **Sem perda, sem punição, sem ranking entre crianças, sem recompensa aleatória, sem contagem regressiva para a criança.**
- **O Bot nunca muda de expressão por causa de acerto ou erro.** Ele é neutro (expressão "atento") em ambos.
- **Pausa, Ninho ("preciso de uma pausa") e "Agora não" (recusar um convite) ficam sempre visíveis e sempre funcionam.**
- **Cor nunca é o único sinal de um estado.** Todo estado tem também forma, ícone ou texto.
- **Dentro de um bloco de medida, nada deste guia vale exceto a existência do Bot parado e calado.** Quem manda ali é o protocolo de pesquisa (ver §9).
- **Uma frase, uma ação pedida, até 8 palavras**, no presente e no afirmativo, para a criança.
- **Nunca "errado", "quase", "de novo não"**, nem comparação com outra criança, nem diagnóstico, no painel do professor.

---

## 1. Personalidade e princípios de marca

**Conceito:** *voar junto*. O VUOO é a trajetória de cada criança, desenhada um dia de cada vez, com um companheiro que acompanha sem julgar.

**Arquétipo do Bot: o Companheiro** — o colega mais velho e paciente que senta ao lado.

| É | Não é |
|---|---|
| calmo | apático |
| caloroso | meloso, infantilizado |
| curioso | intrometido |
| constante | repetitivo a ponto de irritar |
| direto | seco, mandão |
| brincalhão no gesto | irônico na fala |

**Seis princípios, válidos para qualquer tela, ilustração, texto ou som:**

1. **Previsível antes de surpreendente.** Regras, rotina, tempo e fim são sempre conhecidos de antemão. A única surpresa permitida é um presente sem nada em jogo (a peça de coleção).
2. **Suave por padrão, intenso por escolha.** O padrão serve a quem tem mais sensibilidade sensorial; quem busca estímulo aumenta a intensidade.
3. **Mostra o que a criança fez, nunca o que faltou.** Nenhuma tela da criança tem nota, erro acumulado, comparação, contagem regressiva ou casa vazia.
4. **Literal para a criança, transparente para o adulto.** Frases curtas e concretas para quem joga; evidência e limite claros para quem ensina.
5. **A mesma tela e o mesmo som para todos.** Nada do que a criança vê ou do que os colegas ouvem distingue uma criança com plano educacional individualizado das outras.
6. **A linguagem de design fica fora do bloco de medida.** Ali, quem decide é o protocolo de pesquisa (§9).

**Marca:** o VUOO é uma marca de produto autônoma. Instituições parceiras (universidade, financiador) aparecem só como crédito em texto, fora da experiência da criança — nunca como logotipo visível para ela, nunca derivando cor, forma ou nome do VUOO.

---

## 2. O Bot

### Forma

Três formas básicas:

1. **Casco** — oval levemente achatado, cor `casco`.
2. **Visor** — retângulo de cantos muito arredondados, cor `visor`. É onde moram os olhos e a boca (luz).
3. **Asas** — duas asas curtas e arredondadas, cor `ceu`. Mexem pouco.

O casco sempre tem um traço de contorno de 2 px na cor `contorno` (sem esse traço, `casco` sobre `papel` fica com contraste insuficiente para distinguir a silhueta). O Bot faz parte da marca e por isso **não segue** o estilo sem traço das ilustrações (§6).

Por que um robô: um robô simples não tem espécie, gênero nem conotação cultural. A diferenciação do Bot vem do visor de luz, da paleta e do comportamento — não de ser "fofo".

**O Bot é um robô sem gênero.** Em português, trate como "o Bot".

**Tamanhos por contexto** (referência enquanto não houver folha de modelo definitiva): moldura 52 px · Caminho (tela inicial) 48 px · tela de fim de sessão 96 px · tela de descanso (Ninho) 160 px.

### As cinco expressões

Sempre as mesmas cinco, cada uma sempre com a mesma combinação de olhos, boca, asas e luz da antena. Quando a criança ativa rótulos de emoção, cada expressão também tem uma palavra e um pictograma fixos.

| Expressão | Olhos | Boca | Asas | Luz da antena | Rótulo | Quando aparece |
|---|---|---|---|---|---|---|
| **Atento** (neutro) | dois ovais | linha reta curta | relaxadas | apagada | sem rótulo | padrão; durante o jogo; **também depois de um erro** |
| **Contente** | arcos para cima | curva para cima | sobem uma vez | `flor` | "Estou contente." | só em pontos que todas as crianças alcançam: fim de sessão, peça nova na coleção |
| **Curioso** | olho esquerdo maior (sempre o esquerdo) | pequeno "o" | asa esquerda levantada | `ceu` | "Estou curioso." | ao convidar para um jogo novo |
| **Pensando** | olham para cima e para a direita | linha inclinada | paradas | `lavanda`, pulso de 2 s | "Estou pensando." | só enquanto o jogo carrega |
| **Sossegado** | ovais, pálpebra superior reta, pupila visível (não fechados) | curva leve para cima | sobem e descem 6° em 6 s | `folha` | "Estou sossegado." | só na tela de descanso (Ninho) |

**Regra de ouro:** a expressão do Bot **nunca depende de a criança ter acertado ou errado**. Não existe arte de tristeza, decepção, raiva, medo ou surpresa — essas expressões não fazem parte do repertório.

### Estados de animação

| Estado | Expressão | Antena | Movimento | Pisca? |
|---|---|---|---|---|
| `entrando` | atento | apagada | desliza da esquerda para a posição fixa, 400 ms, suave | não |
| `atento` | atento | apagada | parado | a cada 4–6 s (nunca no Modo suave) |
| `falando` | atento | apagada | boca alterna entre a linha reta e um "o" pequeno a cada sílaba tônica | não |
| `espelhando` | atento | apagada | inclina 8° em direção ao toque, 200 ms ida e volta, em **todo** toque de treino, certo ou errado | não |
| `curioso` | curioso | `ceu` | uma asa sobe 20°, 300 ms | sim |
| `carregando` | pensando | `lavanda`, pulso de 2 s | parado | não |
| `contente` | contente | `flor` | as duas asas sobem 20° uma vez, 300 ms | não |
| `sossegado` | sossegado | `folha` | asas sobem e descem 6° a cada 6 s | não |
| `imóvel no bloco de medida` | atento | apagada | nenhum | não |
| `oculto` | — | — | não aparece; a fala fica só no balão de texto, com um pictograma pequeno do Bot | — |

**A antena é só emoção.** Quando a câmera do aparelho está ligada para captura de dados, isso **nunca** aparece na antena: é um pictograma fixo de câmera com o texto "Câmera ligada", no canto inferior esquerdo da tela, enquanto ela estiver ligada.

### De evento a reação (guia de animação/som)

| Evento na tela | Estado do Bot | Som | O que ele diz (resumo) |
|---|---|---|---|
| Início da sessão | `entrando` → `falando` → `atento` | — | avisa quantos jogos tem hoje |
| Antes de um jogo começar | `falando` | — | nome do jogo e a instrução |
| Início do bloco de medida | `imóvel` | o que o protocolo definir | nenhuma (instrução vira texto fixo na tela, sem balão) |
| Toque durante o bloco de medida | `imóvel` | o que o protocolo definir | nenhuma |
| Fim do bloco de medida | `atento` → `falando` | três notas ascendentes | "Você jogou até o fim." |
| Toque registrado no treino (certo ou errado) | `espelhando` | nota de marimba **só no alvo certo**, vinda do alvo e não do Bot | nenhuma |
| Erro no treino | `espelhando` (igual ao acerto) | nota única de kalimba | "Esse não." + repete a instrução |
| Jogo fica mais devagar (ajuste automático) | `atento`, sem mudar expressão | — | "O jogo vai ficar mais devagar." |
| Convite a um jogo novo | `curioso` | — | "Tem um jogo novo. Quer jogar?" |
| Carregando | `carregando` | — | nenhuma |
| Pausa | `atento` | — | "Pausado." |
| Entrar no Ninho (descanso) | `sossegado` | vento muito baixo | "Aqui você pode descansar." |
| Fim da sessão | `contente` | três notas ascendentes | resumo do que a criança jogou |
| Peça nova na coleção | `contente` | arpejo curto | convite a escolher a peça |

Prioridade quando dois eventos coincidem: peça nova na coleção > fim da sessão > limite diário atingido. Um evento de cada vez, com 400 ms de intervalo; uma fala termina antes da próxima começar.

### O que o Bot nunca faz

1. Fica triste, chora ou diz que vai sentir falta da criança.
2. Chama a criança de volta ou manda notificação.
3. Compara a criança com outra.
4. Usa ironia, sarcasmo, piada de duplo sentido ou figura de linguagem.
5. Diz "errado", "quase" ou "de novo não" — pode dizer "Esse não", como informação neutra.
6. Fala, se mexe ou aponta durante o bloco de medida, nem apresenta os estímulos medidos.
7. Aparece de repente: entra sempre pela lateral, devagar, em cerca de 400 ms.
8. Pede dado pessoal, foto ou nome completo.
9. Fala sobre saúde, diagnóstico ou "o que a criança tem".
10. Fala em voz alta sobre adaptação, recuo ou pausa (isso fica só em texto).

### O que o Bot sempre faz

1. Fica no mesmo lugar e no mesmo tamanho em todos os microjogos.
2. Pode ser escondido pela própria criança a qualquer momento, nos ajustes pessoais.
3. Fala com a mesma voz, no mesmo ritmo, com frases do repertório fixo (§10).
4. Tem cada fala disponível em texto, em pictograma e, nas instruções, em Libras.

### Voz do Bot

- Português brasileiro, sotaque neutro, ritmo pausado (cerca de 130 palavras por minuto), registro médio, sem agudos.
- Sem fone de ouvido conectado, só falam em voz alta: nome do jogo, instrução, aviso sobre dados, fim de microjogo, fim de sessão e peça nova — **nunca um número**. Com fone, mais falas podem soar (ver tabela de canal em §10).
- O Bot não tem gênero gramatical marcado: "o Bot".

---

## 3. Cor

Todo token abaixo já foi validado em contraste (WCAG AA ou AAA) nas combinações de uso indicadas, e as cinco cores semânticas (`ceu`, `sol`, `folha`, `lavanda`, `flor`) foram checadas para serem distinguíveis também com protanopia, deuteranopia e tritanopia. A paleta segue a família Okabe–Ito, o conjunto de cores de referência para distinção sob daltonismo.

### Paleta padrão

| Token | Hex | Uso |
|---|---|---|
| `papel` | `#F7F4EC` | Fundo das telas (branco quente, não o branco puro) |
| `superficie` | `#FFFFFF` | Cartões, fundo de áreas de jogo nos blocos de treino |
| `nevoa` | `#E6E2D8` | Divisórias, trilho de barras. **Nunca usar para delimitar um alvo de toque** |
| `contorno` | `#87878E` | Borda de componentes e de alvos de toque |
| `tinta` | `#2B2D42` | Texto principal e contornos (contraste 12,3:1 sobre `papel`) |
| `tinta-suave` | `#686975` | Texto secundário |
| `ceu` | `#0072B2` | **Cor primária da marca.** Botão de ação principal, asas do Bot, linha de trajetória, anel de foco |
| `ceu-profundo` | `#005280` | Estado pressionado; texto sobre `ceu-claro` |
| `ceu-claro` | `#D2E0E3` | Área de destaque |
| `brisa` | `#56B4E9` | **Apoio, só decorativo — nunca para texto.** Painéis e elementos de fundo; sempre com borda `contorno` ou encostado em `superficie`, porque sozinho não tem contraste suficiente para servir de alvo |
| `sol` | `#E69F00` | **Aviso gentil / "tentar de novo".** Contorno de pista no treino, banner de incentivo — nunca um sinal de erro, nunca punitivo |
| `sol-tinta` | `#674800` | Texto sobre `sol-claro`; também a cor do contorno de pista sobre `superficie` |
| `sol-claro` | `#F4E7C9` | Fundo de aviso/incentivo |
| `folha` | `#009E73` | Estado "concluído" (ícone, visto) |
| `folha-profundo` | `#007E5C` | Fundo de botão "concluído" com texto `superficie` |
| `folha-claro` | `#D2E7DA` | Fundo de "concluído" |
| `folha-tinta` | `#00573F` | Texto de "concluído" |
| `lavanda` | `#8E96D6` | Ajuda, pista geral, tela de descanso — Ninho (texto escuro sobre ela) |
| `lavanda-claro` | `#E6E7F2` | Fundo de ajuda |
| `lavanda-tinta` | `#454E80` | Texto de ajuda |
| `flor` | `#CC79A7` | **Recompensa e coleção.** Bot "contente", estrela do Céu, peça nova — nunca um estado funcional (certo/errado) |
| `flor-icone` | `#AD678E` | Ícone de recompensa sobre fundo claro (pena, próximo voo) |
| `flor-claro` | `#F1E2E2` | Fundo de selo de recompensa |
| `flor-tinta` | `#70435C` | Texto de selo de recompensa |
| `casco` | `#FBFAF6` | Corpo do Bot |
| `visor` | `#2B2D42` | Visor do Bot (fundo dos olhos) |
| `olho` | `#8BE0EE` | Olhos e boca do Bot (9:1 sobre `visor`) |
| `ceu-texto-noite` | `#B9ECF5` | Texto sobre fundo `visor` (ex.: painel de turma projetado) |

**Por que `sol` não é mais a cor de recompensa:** antes, a mesma cor acumulava dois papéis (recompensa e "tente de novo"), o que deixava os dois sinais parecidos demais. Agora `flor` é só recompensa/coleção e `sol` é só o aviso gentil de "tentar de novo" — mais fácil de distinguir, inclusive para daltonismo.

**Cor excluída de propósito:** o tom "vermelhão" (`#D55E00`, da mesma família Okabe–Ito) não entra na interface do VUOO, porque é uma variação de vermelho e a interface não usa vermelho (ver regra 1, abaixo). Se um dia for necessário um destaque adicional fora da experiência da criança, ele precisa de um tom fora do eixo do vermelho.

### Modo suave (sensibilidade sensorial)

Troca só estes tokens; os demais continuam iguais à paleta padrão:

| Token | Hex |
|---|---|
| `papel` | `#EAE8E0` |
| `ceu` | `#2D7AA4` |
| `ceu-profundo` | `#2D6582` |
| `ceu-claro` | `#C6D1D2` |
| `brisa` | `#68A7C9` |
| `sol` | `#CA992B` |
| `sol-tinta` | `#70571D` |
| `sol-claro` | `#E2D7BD` |
| `folha` | `#2D9879` |
| `folha-profundo` | `#2D8269` |
| `folha-claro` | `#C6D7CB` |
| `lavanda` | `#8E93BC` |
| `lavanda-claro` | `#D6D7DF` |
| `lavanda-tinta` | `#555C81` |
| `flor` | `#B87F9C` |
| `flor-claro` | `#DFD3D1` |
| `flor-tinta` | `#734A60` |
| `olho` | `#8CCBD4` |

No Modo suave, além da cor: efeitos sonoros a 30% do volume padrão, música desligada, o Bot não pisca, celebração "quieta" (selo estático em vez de animação de festa).

### Alto contraste

Troca só estes tokens, todos com pelo menos 7:1 de contraste sobre `papel`/`superficie` em branco puro:

| Token | Hex |
|---|---|
| `papel` | `#FFFFFF` |
| `tinta` | `#000000` |
| `contorno` | `#2B2D42` |
| `ceu` | `#005280` |
| `sol` | `#674800` |
| `folha` | `#005F45` |
| `lavanda` | `#454E80` |
| `flor` | `#70435C` |

Em alto contraste, `sol`, `folha`, `lavanda` e `flor` passam a ser usados como a própria cor de texto/ícone (como seus equivalentes `-tinta` na paleta padrão) em vez de como preenchimento — é isso que garante os 7:1. Bordas em alto contraste usam 3 px em vez dos 2 px padrão.

### Regras de cor

1. **Não existe vermelho na interface do VUOO — nem suas variações, como o vermelhão.** Erro não é perigo. Um alerta (ex.: no painel do professor) se distingue por ícone e texto, nunca por cor de alarme — usar `ceu-claro`. **Exceção única:** a ilustração de um objeto que é vermelho na vida real (maçã, tomate, morango, semáforo) usa a rampa `il-fruta` (§6). Nunca como botão, sinal, retorno de acerto ou erro, nem como emoção de personagem.
2. **Uma cor forte por tela.** Na tela da criança, é a cor da ação principal.
3. **`flor` só em áreas pequenas** (estrelas, selos, peça de coleção) — nunca como preenchimento grande. **`brisa` nunca carrega texto** — é só decorativo, sempre com borda ou espaço ao redor para não depender do próprio contraste.
4. **Cor nunca sozinha.** Todo estado (concluído, pulado, offline, aviso) também tem forma ou ícone próprio.
5. **As versões `-claro` de cada cor nunca servem para diferenciar estados entre si** — são próximas demais em luminância para isso.
6. **As cinco cores semânticas** (`ceu`, `sol`, `folha`, `lavanda`, `flor`) foram checadas para serem distinguíveis também com daltonismo comum (protanopia, deuteranopia, tritanopia). Mesmo assim, siga sempre a regra 4.
7. **Os modos (suave, alto contraste) e qualquer variação visual de teste nunca mudam a cor dentro de um bloco de medida** — ali manda o protocolo (§9).
8. **As cores desta seção são da interface.** Objetos, personagens e cenários usam a paleta de ilustração (§6). As cores semânticas nunca pintam um objeto, com uma única exceção: as bochechas de emoção de um personagem (§6).

---

## 4. Tipografia

| Função | Família | Por quê |
|---|---|---|
| Texto para a criança (instruções, palavras, rótulos) | **Andika** (SIL, fonte livre) | Desenhada para alfabetização: "a" e "g" de um andar só, e I maiúsculo / l minúsculo / 1 bem diferentes entre si |
| Texto de interface para adultos (painel, telas do professor, números) | **Atkinson Hyperlegible Next** (Braille Institute, fonte livre) | Alta diferenciação entre caracteres parecidos |

### Regras do texto para a criança

- Caixa alta (letra bastão) por padrão no 1º ano e início do 2º ano; configurável pelo professor por turma ou por criança.
- Nível de leitura e aparência adequada à idade são **duas configurações separadas** — uma criança mais velha que lê como uma criança do 1º ano recebe texto simples, mas com ilustração e temas da idade dela, não infantilizados.
- Instrução principal com no mínimo **28 px**; rótulos com no mínimo **20 px**.
- Espaçamento entre letras: `+0,03em` por padrão, `+0,12em` no modo espaçado.
- No máximo **40 caracteres por linha**, **uma frase por instrução**.
- Sem itálico, sem texto justificado, sem texto sobre imagem.
- A escala de texto (100%, 125%, 150%) só se aplica fora do bloco de medida.

### Escala de tamanhos

| Nível | Criança (Andika), tamanho/entrelinha | Adulto (Atkinson), tamanho/entrelinha |
|---|---|---|
| Título de tela | 36 / 44 | 28 / 36, peso 700 |
| Instrução | 28 / 40 | — |
| Rótulo / corpo | 20 / 28 | 16 / 24 |
| Legenda | — | 14 / 20 |
| Dado em tabela | — | 14 / 20, algarismos tabulares |

Peso: 400 no corpo do texto, 700 em títulos e botões. Entrelinha do corpo para a criança: 1,5.

---

## 5. Pictogramas e ícones

- **Conjunto próprio do VUOO**, desenhado para o produto (não usar bibliotecas de terceiros com licença que proíba uso comercial).
- **Estilo:** forma preenchida na cor `tinta`, contorno de 3 px arredondado, grade de 48 × 48 px, raio de 4 px, sempre de frente, sem perspectiva nem sombra.
- **Um pictograma por conceito, sempre o mesmo em todas as telas.** Conjunto mínimo necessário:
  - **ações:** tocar, esperar, não tocar, olhar, ouvir;
  - **navegação:** jogar, pausar, continuar, sair, repetir instrução, próximo, "agora não";
  - **estados:** feito, ajuda, descanso (Ninho), câmera ligada;
  - **emoções do Bot:** as cinco expressões de §2;
  - **tempo:** começo, meio, fim, representados como forma, nunca como número;
  - **colaboração (jogos em dupla):** sua vez, me ajuda, pronto, espera.
- Para crianças que usam comunicação alternativa, o professor pode trocar os pictogramas de "tocar", "esperar", "pausar" e "ajuda" pelos símbolos que a criança já usa — isso vale só para os pictogramas da interface, não para os do jogo em si.
- O toque longo (long-press) nunca é a única forma de ouvir a descrição de um rótulo — tem que haver sempre um botão visível de ouvir.

---

## 6. Ilustração

Vale para **objetos, personagens (exceto o Bot), pessoas, avatares e cenários**. **Não vale** para a marca, o logo, o Bot (§2) nem os pictogramas de interface (§5), que têm regras próprias. Para transformar uma forma qualquer (desenho em papel, imagem, SVG, arquivo do Illustrator) em ilustração VUOO, o passo a passo está em `transformar-em-vuoo.md`.

### Estilo: o mesmo princípio do Duolingo

- **Feita de formas básicas:** retângulo arredondado, círculo/oval e triângulo arredondado. Toda forma complexa é uma soma dessas.
- **Sem traço de contorno.** As formas se separam umas das outras pela diferença de cor, não por linha.
- **Volume por tom interno, nunca por sombra.** Cada cor tem três tons (luz, base, tom interno). A luz vem sempre do alto à esquerda: o tom interno é uma forma chapada no lado de baixo e à direita, e a luz é no máximo um brilho pequeno no alto à esquerda. Sem sombra projetada, gradiente, textura, desfoque ou transparência.
- **Cantos sempre arredondados, nenhuma ponta viva. Não há vilões no VUOO** — nenhuma ilustração hostil ou ameaçadora.
- **Vista:** frontal, lateral ou 3/4, conforme a forma de origem. O 3/4 é simplificado: no máximo dois planos visíveis, sem linhas de fuga.
- **Plana e vetorial, sem 3D.** Toda ilustração precisa poder ser animada por código (SVG, Lottie ou Rive): partes separadas e nomeadas, poucas formas e poucos nós (ver `transformar-em-vuoo.md`).

### Paleta de ilustração

Cada rampa tem três tons. Todas foram validadas em `ferramentas/paleta.json` (tokens `il-*`).

| Rampa | Luz | Base | Tom interno | Uso |
|---|---|---|---|---|
| `il-mato` | `#C4E39A` | `#8CC152` | `#5E8F32` | folhagem, grama, cerrado, legumes verdes |
| `il-ipe` | `#FFE89A` | `#F5C93A` | `#C99A1C` | ipê-amarelo, sol do cenário, milho, banana |
| `il-laranja` | `#FFC796` | `#F28A3C` | `#BF5F1C` | laranja, cenoura, abóbora |
| `il-fruta` | `#FFA79C` | `#E25545` | `#A8352B` | **só objetos vermelhos na vida real:** maçã, tomate, morango, semáforo |
| `il-ipe-roxo` | `#E6C2EE` | `#B07CC6` | `#7E4F96` | ipê-roxo, jabuticaba, uva, flores |
| `il-rio` | `#CBEAF7` | `#7FC4E6` | `#3F8DB8` | água, céu do cenário, vidro |
| `il-terra` | `#ECD3AE` | `#C49462` | `#8C5F38` | chão, madeira, cerâmica, pão |
| `il-pedra` | `#E3E0D8` | `#B3AEA3` | `#7C776D` | metal, rua, pedra, eletrodomésticos escuros |
| `il-casca` | `#FFFFFF` | `#F2EFE6` | `#D8D3C6` | objetos brancos: geladeira, prato, nuvem, papel |

**Pessoas e avatares** (sempre a mesma rampa para a mesma criança ou personagem):

| Rampa | Luz | Base | Tom interno |
|---|---|---|---|
| `il-pele-1` | `#FCE3D3` | `#F5CDB4` | `#DDA88A` |
| `il-pele-2` | `#F6D2B0` | `#E8B48A` | `#C98E66` |
| `il-pele-3` | `#E8B88E` | `#D29A6A` | `#AE7648` |
| `il-pele-4` | `#C99068` | `#A86E48` | `#84522F` |
| `il-pele-5` | `#9C6644` | `#7E4E30` | `#5E3720` |
| `il-pele-6` | `#7A4B32` | `#5C3522` | `#422416` |
| `il-cabelo-preto` | `#4A3F3A` | `#2E2622` | `#1C1614` |
| `il-cabelo-castanho` | `#8A5A3C` | `#6B4229` | `#4C2D1A` |
| `il-cabelo-loiro` | `#F2D58C` | `#DDB55E` | `#B98E3A` |
| `il-cabelo-ruivo` | `#E08A4E` | `#C2652C` | `#94481B` |
| `il-cabelo-grisalho` | `#E6E4E0` | `#BDBAB4` | `#94918A` |

**Detalhes de rosto** (olhos, boca, sobrancelha) em `tinta`, com um ponto de brilho `superficie` no olho. Sobre `il-pele-5` e `il-pele-6`, o olho ganha uma esclera oval `superficie` ao redor, porque `tinta` direto sobre essas peles não tem contraste.

**Regras da paleta de ilustração:**

1. No máximo **3 rampas por objeto** e **5 por cenário**, sem contar os detalhes de rosto.
2. Cada forma usa só os três tons da própria rampa. Não se inventa cor nova nem se mistura tom de duas rampas numa mesma forma. Para um objeto claro de uma cor (ex.: rosa, lilás), vale a **rampa clara**: base = luz, tom interno = base, brilho = `superficie`.
3. As cores semânticas da interface (§3) **nunca** pintam um objeto, com uma única exceção: as bochechas de emoção (abaixo).
4. `il-fruta` só em objetos que são vermelhos na vida real. Nunca em botão, sinal, retorno de acerto ou erro, nem em emoção.
5. Duas rampas próximas sob daltonismo (`il-mato` × `il-laranja`, `il-fruta` × `il-terra`) nunca podem ser a única diferença entre duas respostas de um jogo — vale a regra "cor nunca sozinha" (§3).

### Conjuntos por cenário

| Conjunto | Rampas | Fundo | Chão |
|---|---|---|---|
| Cerrado | mato, ipê, terra, pedra, rio | `il-rio-luz` | `il-terra` |
| Quintal | mato, terra, laranja, fruta, casca | `il-rio-luz` | `il-mato` |
| Feira | fruta, laranja, ipê, mato, ipê-roxo | `papel` | `il-terra-luz` |
| Rio | rio, mato, pedra, terra | `il-rio-luz` | `il-rio` |
| Cidade do interior | pedra, casca, ipê-roxo, terra, rio | `il-rio-luz` | `il-pedra-luz` |
| Casa (interior) | casca, pedra, terra, rio, ipê | `il-terra-luz` | `il-terra` |
| Ninho (descanso) | rio, ipê-roxo, pedra | `lavanda-claro` | `il-pedra-luz` |

Os temas de 6–8 e 9–12 anos usam os mesmos conjuntos; o que muda é o assunto e a proporção dos personagens (abaixo), não a cor.

### Contraste sem traço

Sem contorno, um objeto claro some sobre um fundo claro (`il-casca` sobre `papel` tem 1,05:1). Por isso:

- **Objeto que a criança precisa reconhecer ou tocar:** pelo menos metade da borda externa precisa ter **3:1** contra o fundo. Na prática, o tom interno fica na borda de baixo e da direita, e o fundo é escolhido do conjunto para dar contraste.
- **Objeto que é alvo de toque** fica sobre um **palco**: cartão `superficie` com raio de 20 px e borda `contorno` de 2 px (3 px em alto contraste), como qualquer alvo da interface. A ilustração dentro do palco continua sem traço. Objetos `il-casca` e `il-ipe` não têm contraste contra nenhum fundo claro; o palco deles é `il-terra-tom` (4,8:1 e 3,5:1) ou, só para `il-casca`, `il-rio-tom` (3,2:1).
- **Objeto só decorativo** (fundo de cenário): sem exigência de contraste, mas também nunca pode parecer clicável.

### Personagens e pessoas

- **Pessoas diversas** em avatares e nas telas sociais: tons de pele, cabelos, óculos, aparelho auditivo, cadeira de rodas, abafador de ruído — sem destacar nenhuma característica em particular.
- **Proporção:** cabeça com 1/3 da altura total no tema de 6–8 anos, e com 1/4 no tema de 9–12 anos.
- **Avatares:** galeria grande de figuras que se distinguem claramente entre si pela silhueta, não só pela cor.

### Personagens com emoção (objetos com rosto)

Um objeto pode ganhar rosto e emoção (ex.: uma geladeira contente). As regras:

1. **Nunca fala.** Só o Bot fala. Um objeto com rosto não tem balão, nem voz, nem frase atribuída a ele.
2. **Só as cinco emoções do Bot.** Nunca triste, bravo, com medo, decepcionado ou assustado.
3. **A emoção nunca depende de a criança ter acertado ou errado.** Ela vem da história do jogo (está sol, a casa está arrumada), não do desempenho.
4. **A emoção se lê primeiro pela forma**; a cor é só um reforço pequeno, nas bochechas.

| Emoção | Olhos | Boca | Corpo | Bochechas |
|---|---|---|---|---|
| atento | dois ovais | linha reta curta | reto, proporção original | sem bochechas |
| contente | arcos para cima | curva para cima | estica 5% na vertical | `flor` |
| curioso | olho esquerdo maior | pequeno "o" | inclina 8° | `ceu` |
| pensando | ovais olhando para cima e para a direita | linha inclinada | reto | `lavanda` |
| sossegado | ovais com pálpebra superior reta | curva leve para cima | achata 5% e alarga 5% | `folha` |

- **Olhos:** ovais em `tinta`, com altura de 8% a 12% da altura do objeto, no terço de cima da face principal.
- **Bochechas:** dois ovais pequenos, cada um com no máximo 3% da área da face, logo abaixo e por fora dos olhos.
- **Sem sobrancelhas** em objetos; elas ficam para pessoas.
- **Sem rosto quando a tarefa não pede.** Objeto comum não tem rosto; o rosto é uma escolha da história do jogo.

### Modos e bloco de medida

- **Modo suave:** cada cor das rampas perde 30% de saturação (HSL), mantendo matiz e luminosidade.
- **Alto contraste:** o palco dos alvos usa borda de 3 px `ac-contorno`; a ilustração não muda.
- **Dentro do bloco de medida, a ilustração é só a que o protocolo define.** Quando um objeto serve de "roupa" para um estímulo, forma e cor do estímulo vêm do protocolo e não passam por este estilo. Fora do bloco — nas transições, na tela inicial, no fim de sessão e no descanso — a ilustração pode ser mais rica.

---

## 7. Movimento

| Token | Valor |
|---|---|
| `dur-curta` | 150 ms |
| `dur-media` | 250 ms |
| `dur-entrada` | 400 ms |
| curva padrão | ease-out |

- **Funcional, curto, previsível:** transições de 200–300 ms, reação ao toque de 100–200 ms.
- **Nada súbito.** O Bot sempre entra pela lateral em cerca de 400 ms.
- **Nada piscando:** no máximo 3 flashes por segundo, sem tremor, zoom súbito ou efeito parallax.
- **O Bot fica parado em repouso**, piscando a cada 4–6 s no modo padrão; no Modo suave, não pisca.
- **Todo loop com mais de 5 s precisa ter uma pausa.**
- **Respeita a preferência do sistema por "menos movimento"** como valor inicial, antes de qualquer outro ajuste.

---

## 8. Som

- **Três canais com volume separado:** voz, efeitos, música.
- **Música desligada por padrão. Efeitos em volume baixo por padrão** (e mais baixo ainda no Modo suave, a 30%).
- **Efeitos curtos e suaves** — nunca buzina, alarme, tique-taque ou graves fortes.
- **Repertório mínimo:**
  - toque: clique de madeira suave;
  - alvo certo tocado no treino: uma nota de marimba, que sai do alvo e nunca do Bot;
  - pista (quando erra no treino): uma nota única, timbre de kalimba, sem contorno melódico descendente;
  - fim de um microjogo: três notas ascendentes;
  - peça nova na coleção: arpejo curto;
  - entrar no descanso (Ninho): vento muito baixo.
- **Dentro do bloco de medida, o som é o que o protocolo definir.**
- **O som nunca é o único canal de uma informação** — sempre acompanhado de texto ou pictograma.

---

## 9. Layout de tela

### Duas zonas em toda tela de microjogo

| | Área de medida | Moldura (tudo ao redor) |
|---|---|---|
| O que é | Onde aparecem os estímulos de um bloco de medida, quando o microjogo tem um | Tudo o que cerca essa área, e tudo o que acontece entre blocos |
| Quem define as regras | Um protocolo de pesquisa externo, fixo | **Este guia** |
| Cor, contraste, tema | Fixos pelo protocolo — Modo suave, alto contraste e qualquer variação visual **não** se aplicam | Personalizáveis conforme §3–§8 |
| Tamanho | Em milímetros reais, calibrado pelo aparelho | Em pixels, responsivo |
| Orientação da tela | Travada durante o bloco | Livre |
| Barra de tempo | Oculta por padrão | Visível durante blocos de treino |
| O Bot | Fora da área, imóvel, calado | Presente e ativo |

Nem todo microjogo tem bloco de medida — alguns são só de treino/jogo livre, e aí a tela inteira segue este guia.

### Estrutura da tela de um microjogo

Funciona de 360 px (celular) a telas de 10" (tablet):

```
┌────────────────────────────────────────────┐
│ [Pausar]      ● ● ○  Plano de hoje  [Ouvir] │  ← moldura, fixa
├────────────────────────────────────────────┤
│                                              │
│                    ÁREA DE JOGO              │  ← no bloco de medida: regida pelo protocolo
│                                              │
├────────────────────────────────────────────┤
│ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬░░░░░░ (só durante o treino)  │
│ [Bot]  TOQUE QUANDO APARECER O CÍRCULO.      │  ← moldura, fixa
└────────────────────────────────────────────┘
```

- **Botão de pausar sempre no canto superior esquerdo; botão de ouvir sempre no direito.**
- **Alvos de toque na moldura com no mínimo 64 × 64 px**, com pelo menos 16 px entre eles.
- **Só toque simples na moldura**, registrado no momento em que o dedo solta a tela (não no momento em que toca).

### Tokens de espaço, raio e foco

| Grupo | Valores |
|---|---|
| Espaço (base 4) | 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 px |
| Raio pequeno / médio / grande / pílula | 8 / 14 / 20 / 999 px |
| Anel de foco | `ceu`, 3 px, com 3 px de afastamento do componente |
| Alvo mínimo — criança | 64 × 64 px, com 16 px entre alvos |
| Alvo mínimo — adulto (painel) | 44 × 44 px |
| Borda de alvo de toque | `contorno`, 2 px (3 px em alto contraste). `nevoa` nunca delimita um alvo |
| Contorno de pista ("tentar de novo") | `sol-tinta`, 3 px |
| Traço do casco do Bot | `contorno`, 2 px, sempre presente |

### Estados de componente

Todo componente interativo precisa prever: **padrão**, **pressionado** (`ceu-profundo`), **em foco** (anel), **desabilitado** (`nevoa` com texto `tinta-suave`, nunca escondido), **carregando** (Bot no estado `carregando`), **concluído** (visto `folha`), **pulado** (sai da lista, sem marca de erro), **offline** (contorno pontilhado em `flor-icone`, até sincronizar).

### Biblioteca de componentes

| Componente | Função | Regras |
|---|---|---|
| **Botão primário** | Uma ação por tela | Fundo `ceu`, texto `superficie`, pictograma à esquerda, altura 64 px, raio 20 px |
| **Par de botões** | Duas opções de mesmo peso (ex.: "Agora não" / "Jogar") | Mesmo tamanho, cor e peso visual; a opção de recusar/parar fica sempre à esquerda |
| **Agenda do dia** | Lista visual dos jogos da sessão | Jogo atual com anel `ceu`; concluído com visto `folha`; jogo pulado some da lista em 200 ms, sem marca |
| **Barra de progresso do treino** | Mostra tempo restante só durante o treino | Trilho `nevoa`, preenchimento `ceu`, sem números, nunca muda de cor. Some no bloco de medida — ali a instrução vira texto fixo, sem balão |
| **Balão de fala do Bot** | Mostra o que o Bot diz | Fonte da criança, pictograma, botão de ouvir; nunca cobre a área de jogo |
| **Fileira de "penas" (sequência de dias)** | Mostra os dias em que a criança jogou | Pena em `flor-icone`, uma por dia; a cada 10, agrupa num "galho"; só cresce, nunca mostra dias faltando ou total |
| **Selo de peça nova** | Marca de coleção | Fundo `flor-claro`, texto `flor-tinta`. Aparece na tela inicial, com escolha entre peças equivalentes (nunca peça "melhor" ou "pior") |
| **Linha de trajetória** | Mostra o caminho percorrido | Linha contínua em `ceu`; o próximo trecho em `brisa` (decorativo); nada fica bloqueado |
| **Painel social da turma** | Senso de pertencimento coletivo | Fundo `visor`, elementos acesos em `flor`; mostra só o que já foi "aceso" coletivamente, nunca ranking individual |
| **Aviso sobre uso de dados** | Transparência e consentimento | Bot + voz + texto + pictograma + Libras; sempre com "ouvir de novo" e opção de recusar |
| **Indicador de câmera ligada** | Avisa captura de imagem ativa | Pictograma de câmera + texto "Câmera ligada", fixo no canto inferior esquerdo enquanto ativa; nunca usa a antena do Bot para isso |
| **Ajustes da criança** | Personalização acessível | Pré-visualização ao vivo (cor, tamanho, som); mostra também o que o professor já ajustou |
| **Troca de criança (aparelho compartilhado)** | Login simples | Turma → avatar → senha-figura (a partir do 2º ano); limpa todo o estado da criança anterior |
| **Indicador de turno (jogo em dupla)** | De quem é a vez | Avatar da vez em destaque; moldura na cor da criança da vez |
| **Barra de objetivo compartilhado (jogo em dupla)** | Progresso da dupla | Uma única barra para as duas crianças, sem divisão por criança |

### Funcionando offline

- A sessão funciona sem internet; o horário é registrado localmente e sincronizado depois.
- Um elemento ainda não sincronizado aparece com contorno pontilhado em `flor-icone` ("a acender"), nunca como erro.
- A peça de coleção ganha naquele momento é garantida mesmo sem sincronizar depois.
- O painel do professor nunca mostra "não jogou" quando na verdade só falta sincronizar — mostra "aguardando sincronização".

---

## 10. Anatomia de um microjogo

### Regra de composição: duas camadas que não se misturam

Um microjogo pode ter uma camada de **conteúdo curricular** (ex.: fonemas, números) e uma camada de **medida cognitivo-motora** (ex.: tempo de reação, memória). Elas não podem se misturar dentro do bloco de medida: se o conteúdo curricular decide a resposta certa num bloco que mede, por exemplo, controle inibitório, uma criança que erra por não saber o conteúdo passa a parecer que tem baixo controle inibitório — o que é falso e pode gerar um alerta incorreto no painel do professor.

**Por isso:**
1. **No bloco de medida, o conteúdo curricular nunca decide a resposta certa.** Ele pode aparecer só como "roupa" visual (o alvo é desenhado como um bolo, mas o que diz para tocar é a forma/cor do protocolo), ou nem aparecer.
2. **O conteúdo curricular só decide a resposta certa no bloco de treino**, que vem antes ou depois do bloco de medida, dentro do mesmo microjogo.
3. **Duração e número de tentativas do bloco de medida vêm sempre do protocolo de pesquisa**, nunca de uma decisão de design.
4. **O bloco de medida segue sempre as regras da "área de medida" do §9**: estímulos em milímetros, orientação travada, Bot fora e imóvel, barra de tempo oculta.

### As nove fases de um microjogo

| Fase | O que acontece |
|---|---|
| 1. Apresentação | Pictograma e nome falado do jogo; duração mostrada como forma, nunca como número |
| 2. Demonstração | Uma mão animada faz a ação uma vez |
| 3. Prática | Uma tentativa, com retorno de treino |
| 4. "Pronto?" | Botão "Jogar" — a própria criança decide quando começar |
| 5. **Bloco de medida** (quando existe) | Estímulos do protocolo, na área travada |
| 6. Transição | "Agora: [nome da parte de treino]." |
| 7. **Bloco de treino** | Conteúdo curricular, com pistas graduais |
| 8. "O que você fez" | Frase sobre participação (se foi bloco de medida) ou sobre ações feitas (se foi treino) — nunca sobre acerto/erro |
| 9. "Próximo" | Prévia do próximo jogo; par de botões "Agora não" / "Jogar" |

Um microjogo pode ter só o bloco de treino (sem medida), ou só o bloco de medida (sem treino).

### Modelo de ficha para um novo microjogo

```
Nome (para a criança):     substantivo concreto, até 3 palavras; não repete nenhum
                           nome de tela do sistema (ex.: não pode se chamar "Caminho")
Pictograma:                do conjunto oficial (§5)
Bloco de medida:
  O que mede:              (ex.: controle inibitório, memória de trabalho)
  Parâmetros:              estímulos, tempos, nº de tentativas — vêm do protocolo
  Conteúdo curricular?:     não, ou sim como "roupa" visual registrada
Bloco de treino:
  Conteúdo curricular:     o que ensina
  Pistas:                  sem dica → destaque → demonstração
  Tempo:                   ajustável pelo professor
Instrução (fala + texto):  1 frase, 1 ação pedida, no presente
"O que você fez":          participação (medida) ou ações feitas (treino) — nunca acertos
Câmera:                    não, ou sim com aviso + consentimento + Bot imóvel
```

### Três exemplos de arquétipo

- **Jogo individual com medida + treino** — *Sinal Aberto*: no bloco de medida, aparece um círculo cheio (tocar) ou um quadrado vazado (não tocar), sem conteúdo curricular. No bloco de treino ("figuras e sons"), a criança toca na figura que começa com o som pedido, com pista "Esse não. Toque na figura que começa com [som]." se errar.
- **Jogo colaborativo, sem medida individual** — *Ponte em Dupla*: cada criança vê metade de uma ponte; uma toca a peça e a outra confirma a forma. Os turnos são visíveis, a comunicação usa pictogramas fechados ("sua vez", "me ajuda", "pronto", "espera"), uma única barra de progresso para as duas. O Bot anuncia o resultado da dupla, nunca de uma criança isoladamente.
- **Jogo livre, sem certo e errado** — *Casa do Bot*: a criança escolhe o que a casa do Bot precisa a partir de pistas do ambiente (está sol, choveu). Cada escolha tem uma consequência visível e calma, sem avaliação.

### Acessibilidade dentro do microjogo

- **Surdez:** instruções também em Libras (vídeo curto). Num bloco de medida com estímulo sonoro, a criança surda é **dispensada com registro** — nunca medida por uma alternativa visual que geraria um dado incomparável.
- **Baixa visão:** usar o modo alto contraste da moldura (§3); no bloco de medida, pedir ao protocolo que o estímulo de "não tocar" tenha pelo menos 4,5:1 de contraste.
- **Cegueira:** cada jogo precisa declarar explicitamente se é acessível ou não, e qual é a alternativa pedagógica equivalente.
- **Deficiência motora:** perfil de parâmetros alternativo (ex.: alvo maior, uso de acionador), sempre registrado como tal.
- **Tempo:** ajustável em todo bloco de treino. Só o bloco de medida pode ter tempo fixo não ajustável.

---

## 11. Tom de voz

### Três públicos, três registros

| | Criança | Professor | Gestor escolar |
|---|---|---|---|
| Quem fala | O Bot | O VUOO, como colega experiente | O VUOO, como parceiro técnico |
| Registro | Literal, presente, até 8 palavras | Objetivo, respeitoso com o tempo | Linguagem de política pública |
| Mostra | O que a criança fez | O que foi observado, de onde veio, o limite, o que sugere | Dados agregados, sem ranking |
| Nunca | Erro, comparação, ironia, metáfora, número falado | Diagnóstico, nome de condição médica, comparação entre turmas, jargão técnico | Exposição de uma criança; ranking de turma ou escola |

### Regras para falar com a criança

1. Uma ação pedida por frase, no presente e no afirmativo.
2. No máximo 8 palavras por frase (exceção: avisos sobre dados e sobre câmera, que podem vir em várias frases curtas).
3. Sem metáfora, ironia, gíria ou personificação de objetos (ex.: dizer "a câmera vai ver", nunca "a câmera vai olhar para você").
4. Botões dizem exatamente o que vai acontecer ao tocá-los — nunca "OK" ou "Vamos lá?".
5. Elogio descreve a ação, nunca a pessoa ("Você jogou até o fim", nunca "Você é demais").
6. A pista (ajuda após erro) informa sem julgar: "Esse não." + repetir a instrução.
7. Toda frase precisa ser verdadeira em qualquer dia — nunca prometer "amanhã tem mais" ou algo que dependa do futuro.
8. Um nome por coisa; nenhum nome de jogo pode repetir um nome de tela do sistema.
9. Números só aparecem em texto, nunca são falados em voz.

**Frases que nunca devem aparecer:** "Errado." · "Quase!" · "Ops!" · "Vamos mais devagar." · "Está difícil?" · "Voar de novo" · "Amanhã tem mais." · "Vou sentir sua falta." · "Onde você estava?" · "Respire comigo." · "Você merece!" · qualquer coisa do tipo "12 de 20" dito em voz alta.

### Canal por tipo de fala

Configuração por aparelho: "com fone" ou "sem fone" (padrão: sem fone).

| Tipo de fala | Sem fone | Com fone |
|---|---|---|
| Nome do jogo e instrução | voz + texto + pictograma | voz + texto + pictograma |
| Aviso sobre dados, primeira vez no app | voz + texto + pictograma + Libras | igual |
| Fim de sessão, fim de microjogo, peça nova | voz (sem número) + texto | voz (sem número) + texto |
| Pista, recuo, pausa, pular, convite, descanso, ajustes | só texto + pictograma | voz + texto |
| Qualquer frase com número | só texto, nunca em voz | só texto, nunca em voz |

### Repertório de falas da criança (referência de implementação)

| Quando acontece | O que aparece (texto) |
|---|---|
| Início da sessão | "Oi! Hoje tem [n] jogos." |
| Antes de um jogo | "Agora: [nome do jogo]." |
| Instrução do jogo | a instrução de uma frase (ex.: "Toque quando aparecer o círculo.") |
| Transição para o treino | "Agora: [nome da parte de treino]." |
| Erro no treino | "Esse não. [instrução repetida]." |
| Jogo fica mais devagar | "O jogo vai ficar mais devagar." |
| Fim do bloco de medida | "Você jogou [nome do jogo] até o fim." |
| Fim do bloco de treino | "Você [ação feita] [quantidade]." |
| Convite a jogo novo | "Tem um jogo novo. Quer jogar?" |
| Pausa | "Pausado." |
| Pular o jogo | "Tudo bem. Agora: próximo jogo." |
| Entrar no descanso | "Aqui você pode descansar." |
| Fim da sessão | "Hoje você jogou [n] jogos." |
| Peça nova na coleção | "Uma peça nova para o Bot. Escolha uma." |
| Limite diário atingido | "Os jogos de hoje acabaram." |
| Ajuste feito pelo professor | "[A professora / O professor] deixou assim. Você pode mudar." |
| Mudança visual do Bot | "Hoje o Bot está com uma asa nova. Você pode trocar nos seus ajustes." |
| Aviso sobre uso de dados | "O VUOO guarda como você joga. A sua professora vê. Seus colegas não veem." |
| Antes de ligar a câmera | "A câmera vai ver para onde você olha. Ela não guarda seu rosto." |

### Painel do professor: estrutura de duas camadas

Cada card de uma criança tem duas camadas, nunca misturadas:

**Camada 1 — o que se vê de cara:** ação observável em linguagem de sala + evolução da própria criança em relação a ela mesma.

> **Ana · Esperar o sinal**
> Nas últimas 2 semanas, Ana esperou o sinal antes de tocar em 7 de cada 10 tentativas. No começo do mês, eram 4 de cada 10.

**Camada 2 — "de onde veio", aberta sob demanda:** o construto técnico, o instrumento, quantas sessões, a faixa esperada para a idade com o grau de confiança, e o que o jogo mede e não mede.

**Rodapé fixo em todo card:**

> Isto é uma pista de sala de aula. Não é avaliação nem diagnóstico, e não substitui a equipe da escola.

**Regras:**
- O título do card é sempre a ação observável em linguagem de sala (ex.: "Esperar o sinal"), nunca o nome técnico do construto — esse fica só na camada 2.
- **Nunca compara com a turma.** Quando há uma norma de referência, ela é por idade, vem do instrumento de medida, e aparece só na camada 2.
- Um sinal de atenção (quando o padrão de jogo muda de forma notável) sempre vem acompanhado de: o que mudar pode significar, uma pergunta sobre o contexto (mudou de aparelho? faltou aula?), e um encaminhamento sugerido — nunca a palavra "risco" nem a cor de alarme.

### Glossário do painel

| Usar | Evitar |
|---|---|
| estudante, criança | aluno-problema, caso |
| estudante autista, estudante com deficiência (respeitando a preferência da família) | portador, deficiente, especial, "sofre de" |
| sem condição identificada | típico, normal |
| sinal de atenção, padrão observado, pista | diagnóstico, suspeita, risco (como palavra de interface) |
| ainda não, em desenvolvimento, consolidando | errou, fracassou, atrasado |
| dentro / abaixo / acima da faixa esperada para a idade **neste jogo** | "abaixo" sozinho, sem dizer em que jogo |
| habilidade, objetivo do plano educacional | nota, pontuação, ranking, performance |
| sugestão | "o sistema recomenda que você deve" |
| plano educacional individualizado, por extenso na primeira vez | a sigla sozinha, sem explicar antes |
| acompanhamento, trajetória | monitoramento, rastreamento |

---

## 12. Acessibilidade — o que já está resolvido e o que ainda não

**Já coberto por este guia:**
- Várias formas de se engajar: tema de interesse, três níveis de intensidade de celebração, Modo suave, tela de descanso, convites sempre recusáveis, coleção sem perda.
- Várias formas de entender a informação: voz + texto + pictograma em toda instrução, Libras nas instruções, letra bastão configurável, escala de texto, demonstração antes de jogar.
- Uma forma de agir: toque simples, com tolerância a pequenas variações de movimento.

**Ainda em aberto (verificar antes de desenhar algo que dependa disso):**
- Apoio a leitor de tela dentro da área de jogo.
- Jogos totalmente inacessíveis a crianças cegas ainda não têm alternativa pedagógica declarada caso a caso.
- Modo de varredura para acionadores (switch access) ainda não foi decidido jogo a jogo.
- Arte final do Bot (proporções exatas, grade de luz do visor) ainda depende de um designer de marca — o que está nas §2 são diretrizes, não um manual de arte fechado.
- Paleta de ilustração (§6): validada em contraste e daltonismo, mas ainda não testada impressa nem nos tablets das escolas.
- Folha de modelo dos objetos com rosto: as proporções de §6 são diretriz; a primeira leva de arte deve ser revisada por um ilustrador antes de virar referência.
- Conjunto completo de pictogramas ainda não foi auditado juridicamente quanto a uso comercial de referências externas — desenhar o conjunto próprio do zero, não copiar de bibliotecas existentes.
