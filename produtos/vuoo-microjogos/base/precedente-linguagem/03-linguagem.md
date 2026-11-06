---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-microjogos
etapa: 03-linguagem
status: em revisão
atualizado_em: 2026-10-27
---

# 03 · Linguagem do VUOO

Documento de referência para quem vai desenhar, ilustrar, animar, escrever ou programar uma tela do VUOO. A página visual (`vuoo-linguagem.html`) mostra o mesmo conteúdo aplicado. Os códigos entre colchetes apontam para a origem de cada regra (ver cabeçalho de `02-gamificacao.md`).

> **Status:** proposta para o 1º ciclo de co-design (C17). Metáfora, mascote e paleta têm critério de aceite em `05-decisoes.md`. Este documento é insumo das consultorias de especificação de produto e de design instrucional do PIPE.

---

## 1. Arquitetura de marca

**Decisão:** o VUOO é uma **marca de produto autônoma**. O CIATec/USP e a FAPESP aparecem como **endosso em texto**, fora da experiência da criança (D-01).

- **Nenhum elemento da identidade VUOO deriva das marcas FAPESP, USP ou CIATec** (I1). O logotipo da FAPESP exige autorização escrita do Presidente (I3).
- **Bloco de créditos, só texto**, na tela "Sobre", no rodapé do painel do professor, no site e em impressos (I2):
  > VUOO é desenvolvido pela Wemoga Software Studio em cooperação com o CIATec – Centro de Inclusão e Acessibilidade por meio da Tecnologia (EACH/USP), com apoio da FAPESP (processo nº `[A CONFIRMAR]`). As opiniões, hipóteses e conclusões ou recomendações expressas neste material são de responsabilidade dos autores e não necessariamente refletem a visão da FAPESP.
- **Faixa de endosso:** área reservada, monocromática, para até 3 logotipos menores que o VUOO, preenchida só depois de autorização formal; funciona em positivo e negativo (I3, I4).
- **A criança nunca vê logotipo institucional.**
- **Jogos do CIATec** (D-18): continuam acessíveis gratuitamente fora do VUOO, como prevê a governança aberta do CIATec (`[IN-30]`). Se rodarem dentro do VUOO, é por decisão do comitê gestor, com o selo textual "Jogo do CIATec" e os mesmos componentes. O Bot é opcional neles.

## 2. Conceito

### A ideia
**Voar junto.** O VUOO é a trajetória de cada criança, desenhada um dia de cada vez, com um companheiro que acompanha sem julgar. O nome já é a metáfora, e o título do projeto também ("trajetórias educacionais", `[IN-32]`). A identidade se organiza em torno de **uma linha que cresce**: a linha de voo do Bot no Caminho, a fileira de penas, o traço de evolução no painel do professor.

### Princípios de marca
1. **Previsível antes de surpreendente.** Regras, rotina, tempo e fim são sempre conhecidos. A única surpresa permitida é um presente sem nada em jogo (a peça da coleção). (R18)
2. **Suave por padrão, intenso por escolha.** O padrão serve a quem tem mais sensibilidade sensorial. Quem busca estímulo aumenta a intensidade. (R1, R34, R38)
3. **Mostra o que fez, nunca o que faltou.** Nenhuma tela da criança tem nota, erro acumulado, comparação, contagem regressiva ou casa vazia. (R17, R29, S3, S6, S7)
4. **Literal para a criança, transparente para o adulto.** Frases curtas e concretas para quem joga; evidência e limite por trás de cada afirmação para quem ensina. (R23, `[IN-21]`, I10)
5. **A mesma tela e o mesmo som para todos.** Nada do que a criança vê ou do que os colegas ouvem distingue uma criança com Plano Educacional Individualizado das outras. (`[IN-04]`, HIP-5, S9)
6. **A linguagem fica fora do palco de medida.** Estímulos medidos pertencem ao protocolo do CIATec. (`[IN-17]`, C3)

### Personalidade
**Arquétipo: o Companheiro.** O colega mais velho e paciente que senta ao lado.

| É | Não é |
|---|---|
| calmo | apático |
| caloroso | meloso, infantilizado |
| curioso | intrometido |
| constante | repetitivo a ponto de irritar |
| direto | seco, mandão |
| brincalhão no gesto | irônico na fala |

---

## 3. Logotipo (direção)

- **VUOO em caixa alta**, desenho sem serifa, traço uniforme, cantos arredondados. É legível por quem está aprendendo a ler (I19).
- **O "OO" são os olhos do Bot**, dentro do visor. O nome é o rosto do produto.
- Versões: completa, reduzida (só o visor com os olhos, para o ícone do app) e monocromática.
- `[A CONFIRMAR]` Desenho final por designer de marca; aqui está a direção, e a página visual traz um estudo.

---

## 4. VUOO Bot

### Forma
Três formas básicas, como o guia de ilustração do Duolingo faz com o Duo (pesquisa `a`), compatíveis com a animatrônica em impressão 3D do **projeto do CIATec, apoiado pela Wemoga** (`[IN-13]`, C27):

1. **Casco:** oval levemente achatado, cor `casco`.
2. **Visor:** retângulo de cantos muito arredondados, cor `visor`. Na versão física, tela OLED ou matriz de LED.
3. **Asas:** duas asas curtas e arredondadas, cor `ceu`. Mexem pouco. Na versão física, dois servos.

Detalhes:
- **Olhos e boca de luz**, cor `olho`, desenhados **no visor**. A boca é uma linha curta de luz (D-03 revista). A pesquisa recomenda boca clara para a leitura da expressão (R33), e como o visor é uma tela, a boca não custa nada ao animatrônico (C19, S8).
- **Luz da antena:** ponto no topo que indica estado. É a comunicação não verbal mais simples possível (`[IN-12]`).

**Por que um robô e não um bicho:** um robô simples não tem espécie, gênero nem conotação cultural, é compatível com a fabricação e o projeto já o chama de "VUOO Bot". O "robozinho fofo" é clichê de edtech (pesquisa `c`); a diferenciação vem do visor de luz, da paleta e do comportamento. **Proposta para co-design** (D-03).

### Expressões
Cinco, sempre iguais, cada uma com palavra e pictograma quando a criança ativar os rótulos de emoção (R33). A leitura delas é a HIP-4 e deve ser testada **antes** de fechar a arte.

| Expressão | Olhos | Boca | Asas | Luz da antena | Rótulo | Quando |
|---|---|---|---|---|---|---|
| **Atento** (neutro) | dois ovais | linha reta curta | relaxadas | apagada | sem rótulo | padrão; durante o jogo; **depois de erro** |
| **Contente** | arcos para cima | curva para cima | levantam uma vez | `sol` | "Estou contente." | **só em pontos que todos alcançam**: fim do voo, peça nova, chegada no Caminho |
| **Curioso** | **olho esquerdo** maior (sempre o esquerdo) | pequeno "o" | asa esquerda levantada | `ceu` | "Estou curioso." | no convite a um jogo novo |
| **Pensando** | olham para **cima e para a direita** | linha inclinada | paradas | `lavanda`, pulso senoidal de 2 s | "Estou pensando." | **só enquanto o jogo carrega** (E2) |
| **Sossegado** | ovais com a **pálpebra superior reta**, pupila de luz visível (não fechados) | curva leve para cima | posição neutra; sobem e descem 6° em 6 s | `folha` | "Estou sossegado." | **só no Ninho** |

**O casco tem sempre traço `contorno` de 2 px**, porque `casco` sobre `papel` dá 1,05:1. Estados, durações e a matriz evento → reação estão em `06` §5, que prevalece.

**A expressão do Bot não depende de acerto nem de erro** (S8, E2). Ele nunca fica mais feliz porque a criança acertou, nem muda de expressão porque ela errou. Não existe arte de tristeza, decepção, raiva, medo ou surpresa.

### Comportamentos (proposta)
O projeto nomeia quatro comportamentos adaptativos: espelhar, provocar, celebrar, recuar (`[IN-11]`). As definições abaixo são **proposta deste estudo** (C25) e separam **o que o Bot expressa** de **o que o gêmeo decide**. Os nomes ficam no documento técnico; nunca aparecem no painel do professor (S17).

| Comportamento | O que o gêmeo decide | O que o Bot expressa | Fala-modelo | Limite |
|---|---|---|---|---|
| **Espelhar** | nada; é reação ao toque | Fora do palco, inclina 8° em **todo** toque do treino, certo ou errado. Expressão **atento**. | nenhuma | Nunca no bloco de medida. Testar se é lido como imitação zombeteira (S17). **Comum aos dois braços.** |
| **Provocar** (convidar) | introduzir um microjogo que a criança **ainda não jogou** | Mostra a prévia e espera. Expressão **curioso**. | `jogo.convite`: "Tem um jogo novo. Quer jogar?" | Sempre recusável. A dificuldade **dentro** de um jogo muda entre blocos **sem convite** (E26). **Só no braço adaptativo.** |
| **Celebrar** | nada; acontece em pontos que todos alcançam | Descreve o que a criança fez. **Contente** só no fim do voo e em marcos. | `voo.fim` | Elogia a ação, nunca a pessoa. Nunca "estou contente **com você**". **Comum aos dois braços** (E23). |
| **Recuar** | erros seguidos no treino → o jogo fica mais devagar | **Nenhuma mudança de expressão** (atento). Aviso só em texto. | `treino.devagar` | Nunca anuncia como fracasso. Nunca em voz alta (S9). Não oferece o Ninho (S10). **Só no braço adaptativo.** |

Os **limiares** de cada comportamento (quantos erros, quanto tempo de hesitação) são **parâmetros de CMS**, definidos com o CIATec e ajustados no PP3 (F3.1, C25).

### Variante "Bot não adaptativo" (braço de controle do PP3)
Mesma arte, mesma posição, mesmas falas, mesmo comportamento fora do palco, mas **sem disparos do gêmeo**: espelha e celebra igual ao braço adaptativo; não convida; não recua; a dificuldade segue uma progressão fixa por fase. Nos dois braços, o Bot fica fora do palco e imóvel durante a medida. Ocultação do Bot e ajustes do "Do meu jeito" ficam **registrados por sessão** para análise por intenção de tratar (C5).

### Regras de conduta
O Bot **nunca**:
1. fica triste, chora ou diz que vai sentir falta (I9);
2. chama a criança de volta ou manda notificação (I7);
3. compara a criança com outra (R29);
4. usa ironia, sarcasmo, piada de duplo sentido ou figura de linguagem (R23);
5. diz "errado", "quase", "de novo não". Pode dizer "Esse não", como informação neutra (S11);
6. fala, se mexe ou aponta durante um bloco de medida, nem apresenta estímulos medidos (`[IN-17]`, C8);
7. aparece de repente: entra pela lateral, devagar, em cerca de 400 ms (R8);
8. pede dado pessoal, foto ou nome completo (I11);
9. fala de saúde, diagnóstico ou "o que você tem" (`[IN-05]`);
10. fala em voz alta sobre adaptação, recuo ou pausa (S9).

O Bot **sempre**:
1. fica no mesmo lugar e no mesmo tamanho em todos os microjogos (R33);
2. pode ser escondido **pela criança**. Se o professor esconder o Bot de uma criança, ela vê isso no "Do meu jeito" ("A professora deixou assim. Você pode mudar.") (S8, S9);
3. fala com a mesma voz, no mesmo ritmo, com frases do repertório;
4. tem cada fala em texto, pictograma e, nas instruções, Libras (I17, S15).

### Vínculo
- A **peça escolhida pela criança** não precisa de aviso: o próprio gesto de escolher anuncia. **Mudanças impostas pelo sistema** (redesenho, troca de arte) são avisadas no início do voo em que acontecem, sem falar em amanhã (`bot.mudanca`) (E10).
- O nome do Bot, se a criança quiser dar um, é escolhido de uma lista (S14).
- `[A CONFIRMAR]` O que acontece com o Bot de uma criança quando ela muda de escola ou quando a escola encerra o contrato precisa de regra de despedida, sem culpa e sem "vou sentir sua falta".

### Voz
- Português brasileiro, sotaque neutro, ritmo pausado (cerca de 130 palavras por minuto), registro médio, sem agudos estridentes (I20, I25).
- **O canal de voz depende da configuração de fone do aparelho;** a tabela de `06` §3 prevalece. Sem fone, só falam em voz alta nome do jogo, instrução, aviso de dados, fim de microjogo, fim do voo e peça nova, e **nunca um número** (S9, E1).
- `[A CONFIRMAR]` TTS para falas dinâmicas e voz gravada para sons de fala pedagógicos (fonemas, sílabas), que são conteúdo (I20).
- O Bot é um robô e não tem gênero. Em português, "o Bot".

---

## 5. Cor

### Tokens
Validados por `ferramentas/contraste.py`. O resultado está em `ferramentas/resultado-contraste.txt`: 23 pares, todos AA ou AAA.

| Token | Hex | Papel |
|---|---|---|
| `papel` | `#F3F5F7` | Fundo da moldura |
| `superficie` | `#FFFFFF` | Cartões, fundo do palco em blocos de treino |
| `nevoa` | `#DDE3EA` | Divisões, trilho da barra |
| `contorno` | `#7D8A98` | Borda de componentes (3,5:1) |
| `tinta` | `#1D2833` | Texto principal (13,7:1 sobre `papel`) |
| `tinta-suave` | `#4A5866` | Texto secundário |
| `ceu` | `#2F6699` | **Cor da marca.** Ação principal, asas, linha do Caminho |
| `ceu-profundo` | `#1F4A73` | Pressionado; texto sobre `ceu-claro` |
| `ceu-claro` | `#DCE7F2` | Área de destaque |
| `sol` | `#E0A23A` | **Só recompensa**, sobre fundo escuro ou em preenchimento grande: estrelas do Céu, selo de peça |
| `sol-icone` | `#B07A1C` | Pena, estrela offline e próximo voo **sobre fundo claro** (3,4:1; o `sol` dá só 2,04:1) (E7) |
| `sol-claro` / `sol-tinta` | `#FBEED3` / `#6E4708` | Selo de peça |
| `folha` | `#3B7F57` | Concluído |
| `folha-claro` / `folha-tinta` | `#DCEEE2` / `#1F5236` | Fundo e texto de concluído |
| `lavanda` | `#A593DB` | Ajuda, pista, Ninho (texto escuro sobre ela) |
| `lavanda-claro` / `lavanda-tinta` | `#EAE6F5` / `#43357A` | Fundo e texto de ajuda |
| `casco` / `visor` / `olho` | `#F6F2EA` / `#1D2833` / `#8BE0EE` | Bot (olhos 10:1 sobre o visor) |

**Três modos, todos validados em `ferramentas/resultado-contraste.txt` (40 pares):**
- **Padrão:** a tabela acima.
- **Modo suave** (tokens `suave-*` em `paleta.json`): papel `#EEF0F2`, ceu `#4F6F8E`, ceu-profundo `#3A546D`, ceu-claro `#E2E8EE`, sol `#B89559`, sol-icone `#97814F`, sol-claro `#F3EDE2`, folha `#557A64`, folha-claro `#E3ECE6`, lavanda `#B3AACB`, lavanda-claro `#EEECF3`, olho `#A9D3DA`. Os demais tokens não mudam.
- **Alto contraste** (tokens `ac-*`): papel `#FFFFFF`, tinta `#000000`, contorno `#1D2833`, ceu `#0B3D6B`, sol-icone `#7A5200`, folha `#16502E`, lavanda-tinta `#2E2066`. Texto, bordas e botões com pelo menos 7:1, contornos de 3 px (S15, E25).

Os modos trocam valores de tokens **da moldura**. Precedência entre modos e ajustes em `06` §6. Espaço, raio, foco, movimento e estados em `06` §7.

### Regras
1. **Não existe vermelho no VUOO** (D-09). Erro não é perigo (R14). No painel, o sinal de atenção se distingue por ícone e texto, em `ceu-claro` (E19).
2. **Uma cor forte por tela.** Na moldura, é a ação principal. No palco de medida, quem decide é o protocolo.
3. **`sol` só em áreas pequenas** (R2; estudo de Grandgeorge com amostra pequena).
4. **Cor nunca sozinha** (R4, I15): todo estado tem forma ou ícone.
5. **Os tons `-claro` nunca diferenciam estados entre si.** O script mostra ΔE < 6 entre eles, para qualquer pessoa.
6. **Os quatro tons semânticos** (`ceu`, `sol`, `folha`, `lavanda`) são distinguíveis em visão típica e com protanopia e deuteranopia (ΔE ≥ 21). Com tritanopia, `ceu` × `folha` fica no limite (ΔE 10,6): mais um motivo para a regra 4.
7. **Modo suave, alto contraste, tema e variantes de teste não mudam o palco de medida** (C3).

### Proposta ao CIATec para o A/B/n
O CIATec prevê testar 5 interfaces visuais, 2 tipos de feedback e 2 sistemas de progressão (`[IN-25]`). O desenho é do CIATec (C13). Este estudo propõe três listas:

**Invariantes de segurança** (nenhuma variante pode violar):
- sem vermelho;
- sem perda nem punição por ausência;
- sem ranking entre crianças;
- sem recompensa aleatória;
- sem contagem regressiva para a criança;
- sem expressão do Bot contingente a desempenho;
- pausa, Ninho e "Agora não" sempre visíveis.

**Variáveis experimentais abertas**, com candidatos:
- **5 interfaces visuais:** combinações de saturação da moldura (de 35% a 60% em `ceu`), densidade de ilustração (nenhuma, de borda, plena nas transições) e intensidade de celebração (suave, padrão, festa). Também podem ser 5 direções visuais distintas, desde que respeitem os invariantes.
- **2 tipos de feedback no treino:** (A) só retorno de competência (o alvo reage, sem palavras); (B) retorno de competência + descrição verbal da ação pelo Bot.
- **2 sistemas de progressão:** (A) Caminho (trajetória que cresce por dia de voo); (B) Álbum (cada dia de voo adiciona uma página com uma ilustração do tema).

**Restrições de medida:** nos microjogos com bloco de medida, as variantes mudam só a moldura (C3).

---

## 6. Tipografia

| Função | Família | Por quê |
|---|---|---|
| **Letra da criança:** instruções, palavras-alvo, rótulos | **Andika** (SIL, OFL) | Desenhada para alfabetização: "a" e "g" de um andar, I/l/1 diferentes (R9, I16) |
| **Letra de interface:** painel, telas do adulto, números | **Atkinson Hyperlegible Next** (Braille Institute, OFL) | Alta diferenciação entre caracteres, bom conjunto de pesos (R9) |

**Evidência:** nenhuma das duas tem estudo com crianças comprovando ganho de leitura; OpenDyslexic não tem benefício comprovado. O que tem evidência é espaçamento e tamanho (Zorzi 2012), e é isso que as regras abaixo fixam (pesquisa `b`).

### Regras da letra da criança
- **Caixa alta (letra bastão) por padrão no 1º ano e início do 2º**, configurável pelo professor por turma ou criança (R10, EF01LP11 `[A CONFIRMAR código]`).
- **Nível de leitura e aparência por idade são configurações separadas** (S15). Uma criança de 10 anos que lê como uma de 1º ano recebe texto simples com ilustração e temas da idade dela.
- Instrução principal com no mínimo **28 px**; rótulos com no mínimo **20 px** (R11).
- Espaço entre letras **+0.03em** por padrão e **+0.12em** no modo espaçado; entrelinha por nível em `06` §7 (R12).
- No máximo **40 caracteres por linha**, **uma frase por instrução** (R12, R23).
- Sem itálico, sem justificar, sem texto sobre imagem. Escala de texto em 100%, 125% e 150%, **só na moldura** (C3).

### Escala
| Nível | Criança (Andika) | Professor (Atkinson Next) |
|---|---|---|
| Título de tela | 36 / 44 | 28 / 36, peso 700 |
| Instrução | 28 / 40 | — |
| Rótulo / corpo | 20 / 28 | 16 / 24 |
| Legenda | — | 14 / 20 |
| Dado em tabela | — | 14 / 20, números tabulares |

---

## 7. Pictogramas e ícones

- **Conjunto próprio** (D-15): o ARASAAC é CC BY-NC-SA, que proíbe uso comercial (pesquisa `b`). `[A CONFIRMAR]` Parecer jurídico.
- **Mapeamento para os símbolos do AEE** (S15): para crianças que usam comunicação alternativa, o professor pode trocar os pictogramas de "tocar", "esperar", "pausar" e "ajuda" pelos que a criança já usa. Isso vale só para a moldura e para as instruções.
- **Estilo:** forma preenchida em `tinta` com contorno de 3 px arredondado, grade 48 × 48, raio 4 px, frontal, sem perspectiva nem sombra (R25).
- **Um pictograma por conceito, sempre o mesmo.** Conjunto mínimo:
  - **ações:** tocar, esperar, não tocar, olhar, ouvir;
  - **navegação:** jogar, pausar, continuar, sair, repetir instrução, próximo, "agora não";
  - **estados:** feito, ajuda, Ninho, câmera ligada;
  - **emoções do Bot:** as 5 da tabela;
  - **tempo:** começo, meio, fim, como forma;
  - **colaboração:** sua vez, me ajuda, pronto, espera.
- O toque longo nunca é a única forma de ouvir um rótulo (R36).

---

## 8. Ilustração

- **Plana e vetorial**, poucas camadas, para aparelhos fracos e offline (I23).
- **Formas arredondadas.** Não há vilões no VUOO.
- **Paisagens brasileiras reais**: ipê, cerrado, quintal, rua de cidade do interior, rio, feira.
- **Pessoas diversas** nos avatares e no Ninho: tons de pele, cabelos, óculos, aparelho auditivo, cadeira de rodas, abafador de ruído, sem destacar ninguém.
- **Temas para 6–8 e para 9–12 anos**, com a mesma simplicidade de texto (S15).
- **No palco de medida, quem decide é o protocolo.** Fora dele, a ilustração rica fica nas transições, no Caminho, no Pouso e no Ninho (R5).
- **Avatares:** galeria grande de figuras distinguíveis à primeira vista (I26).

---

## 9. Movimento

- **Funcional, curto, previsível** (R6): transições de 200 a 300 ms, reação ao toque de 100 a 200 ms.
- **Nada súbito** (R8). O Bot entra pela lateral em 400 ms.
- **Nada piscando:** até 3 flashes por segundo, sem tremor, zoom súbito ou parallax (WCAG 2.3.1).
- **O Bot fica parado em repouso.** Pisca a cada 4 a 6 s no modo padrão; no Modo suave, não pisca (R33).
- **Todo loop com mais de 5 s tem pausa** (WCAG 2.2.2).
- **Respeita `prefers-reduced-motion`** como valor inicial (R39).
- **Rive**, com máquina de estados para o Bot (pesquisa `a`). `[A CONFIRMAR]` com a equipe de desenvolvimento.

---

## 10. Som

- **Três canais com volumes separados:** voz, efeitos, música (R7).
- **Música desligada por padrão.** Efeitos baixos por padrão.
- **Efeitos curtos e suaves**, sem buzina, alarme, tique-taque ou graves fortes (R7, R14).
- **Repertório mínimo de sons de interface:**
  - **toque:** clique de madeira suave;
  - **alvo certo tocado no treino:** uma nota de marimba, que sai do alvo (retorno de competência) e nunca do Bot;
  - **pista:** uma **nota única**, no mesmo registro da anterior, com outro timbre (kalimba), **sem contorno descendente** (S12). A validar no co-design com a pergunta "o que esse som quer dizer?";
  - **fim de microjogo:** três notas ascendentes;
  - **peça nova:** arpejo curto;
  - **Ninho:** vento muito baixo.
- No palco de medida, o som é o do protocolo.
- **O som nunca é o único canal** (I25).
- **Sons de fala pedagógicos são conteúdo** (I20).

---

## 11. Layout e componentes

### Palco de medida e moldura (C3, C6, C7, C8)
Toda tela de microjogo tem duas zonas:

| | **Palco de medida** | **Moldura** |
|---|---|---|
| O que é | Área onde aparecem os estímulos de um bloco de medida | Tudo o que está ao redor, e tudo o que acontece entre blocos |
| Quem define | **Protocolo do CIATec**, congelado a partir do PP1 (núcleo de medida) | Esta linguagem |
| Cor, contraste, tema | Do protocolo. Modo suave, alto contraste, tema e variantes A/B/n **não** se aplicam | Personalizáveis |
| Tamanho | **Em milímetros**, com calibração por DPI do aparelho. Tela mínima definida pelo CIATec | Em px, responsivo |
| Orientação | **Travada** durante o bloco | Livre |
| Tempo | Do protocolo. Barra de duração **oculta por padrão** | Barra visível no treino |
| Bot | Fora, imóvel, calado | Presente |
| Registro | Aparelho, tela, DPI, orientação, configurações ativas: tudo por sessão, como covariável | — |

**Modo aplicação × modo sala** (C6): o modo aplicação, para os estudos do PP1, PP3 e PP5, usa moldura mínima e configurações travadas. O modo sala, para a rotina, usa a moldura completa. Os dois compartilham o mesmo palco de medida.

### A tela do microjogo
Funciona de 360 px (celular) a 10" (tablet):

```
┌────────────────────────────────────────────┐
│ [⏸ Pausar]   ● ● ○  Plano de hoje   [🔊 Ouvir]│  ← moldura, fixa
├────────────────────────────────────────────┤
│                                            │
│               PALCO                        │  ← no bloco de medida: protocolo do CIATec
│                                            │
├────────────────────────────────────────────┤
│ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬░░░░░░ (só no treino)        │
│ [Bot]  TOQUE QUANDO APARECER O CÍRCULO.     │  ← moldura, fixa
└────────────────────────────────────────────┘
```

- **Pausar sempre no canto superior esquerdo; Ouvir sempre no direito** (R22, R24).
- **Alvos de interface na moldura com no mínimo 64 × 64 px** e 16 px entre eles (R35).
- **Só toque simples na moldura**, aceito na soltura do dedo (R36).

### Componentes
| Componente | Função | Regras |
|---|---|---|
| **Botão primário** | Uma ação por tela | `ceu`, rótulo `superficie`, pictograma à esquerda, altura 64 px, raio 20 px |
| **Botão par** | Duas opções de mesmo peso | Mesmo tamanho, cor e peso (I8). A opção de parar ou recusar fica **à esquerda**. Nos documentos, pares são escritos sempre na ordem visual: "Agora não / Jogar" (E15) |
| **Plano de hoje** | Agenda visual | Atual com anel `ceu`; feito com visto `folha`; jogo pulado **sai do Plano** em 200 ms, sem marca (E17) |
| **Barra de duração** | Tempo no treino | Trilho `nevoa`, preenchimento `ceu`, sem números, **sem mudar de cor**. Oculta no bloco de medida; lá, a instrução fica como **texto estático** na moldura, sem balão (E12) |
| **Balão do Bot** | Fala | Letra da criança, pictograma, botão de ouvir; nunca cobre o palco |
| **Fileira de penas** | Dias de voo | No topo do Caminho. Uma pena `sol-icone` por dia de voo; a cada 10, um galho; só cresce; sem dias da semana, casas vazias ou total (`06` §8) |
| **Selo de peça** | Peça nova | Aparece no Caminho, com escolha entre 3 peças equivalentes |
| **Caminho** | Trajetória | Linha `ceu` contínua; próximo voo em `sol`; nada bloqueado |
| **Céu da turma** | Pertencimento | Fundo `visor`, estrelas `sol`; texto só do que foi aceso; versão para projetar |
| **Aviso de dados** | Aviso e assentimento | Bot + voz + texto + pictograma + Libras; "Ouvir de novo"; "Agora não / Quero jogar" |
| **Câmera ligada** | Captura por Wemoga Eye (C16) | **Não usa a antena**, que é só emoção (E3). Pictograma de câmera + rótulo "Câmera ligada", fixo no canto inferior esquerdo da moldura enquanto a câmera estiver ligada. Fala `camera.aviso` antes de ligar `[A CONFIRMAR]` com o projeto técnico e o jurídico |
| **Do meu jeito** | Ajustes da criança | Prévia ao vivo e áudio (R39); mostra ajustes do professor |
| **Troca de criança** | Aparelho compartilhado | Turma → avatar → senha-figura (a partir do 2º ano); limpa o estado anterior (S14) |
| **Turno** (colaboração) | De quem é a vez | Avatar da vez em destaque; moldura na cor da criança da vez |
| **Barra compartilhada** (colaboração) | Objetivo da dupla | Uma barra para os dois, sem divisão por criança |
| **Pictogramas entre pares** (colaboração) | Comunicação | Conjunto fechado: sua vez, me ajuda, pronto, espera |

### Offline (C26)
- O voo funciona sem rede, com carimbo de tempo local para o tempo de reação e sincronização posterior.
- A estrela do Céu fica "a acender" (contorno pontilhado) até sincronizar.
- A peça da coleção é garantida localmente.
- **O painel nunca mostra "não teve vez" quando a sessão só não sincronizou.** Mostra "aguardando sincronização".

---

## 12. Tom de voz

### Os três públicos
| | Criança | Professor | Gestor |
|---|---|---|---|
| **Quem fala** | O Bot | O VUOO, como um colega experiente | O VUOO, como parceiro técnico |
| **Registro** | Literal, presente, até 8 palavras | Objetivo, respeitoso com o tempo | Linguagem de política pública |
| **Mostra** | O que a criança fez | O que observou, de onde veio, o limite, o que sugere | Agregados sem ordenação |
| **Nunca** | Erro, comparação, ironia, metáfora, número falado | Diagnóstico, nome de condição, comparação com a turma, jargão | Exposição de criança; ranking de turma ou escola |

### Criança: regras e falas
**A fonte única das falas, com ID, versão falada, canal e plural, é `06-especificacao-base.md` §3 e §4.** Aqui ficam só os princípios:

1. Uma ação pedida por frase, no presente e no afirmativo.
2. Até 8 palavras por frase (exceção: avisos de dados e de câmera, divididos em frases curtas).
3. Sem metáfora, ironia, gíria, expressão ou personificação de objetos.
4. Botões dizem exatamente o que acontece. Nunca "OK" ou "Vamos lá?".
5. Elogio descreve a ação, não a pessoa.
6. A pista informa sem julgar: "Esse não." + a instrução do treino.
7. Toda frase é verdadeira em qualquer dia: o sistema gera a frase a partir do estado real e nunca promete o amanhã.
8. Um nome por coisa, e nenhum nome de jogo igual a um termo do sistema (Ninho, Caminho, Pouso, Penas, Céu).
9. Números só no texto, nunca na voz.

**O que nunca dizer** (exemplos que as revisões encontraram): "Errado." · "Quase!" · "Ops!" · "Vamos mais devagar." · "Está difícil?" · "Toque quando o sinal abrir." · "Voar de novo" · "Amanhã tem mais." · "Vou sentir sua falta." · "Onde você estava?" · "Respire comigo." · "Você merece!" · "12 de 20."

---

## 13. Painel do professor (C4, C9, S4, D-17)

### O cartão individual: duas camadas
**Camada 1, a abertura:** rótulo de ação observável em linguagem de sala + evolução da criança em relação a ela mesma.

> **Ana · Esperar o sinal**
> Nas últimas 2 semanas, Ana esperou o sinal antes de tocar em 7 de cada 10 tentativas. No começo do mês, eram 4 de cada 10.

**Camada 2, o detalhe ("De onde veio"):** construto da ontologia, instrumento, sessões, faixa para a idade com incerteza, e o que o jogo mede e não mede.

> **De onde veio:** Controle inibitório · jogo Sinal Aberto · 9 partidas em modo sala, de 6 a 24/10.
> **Faixa para a idade:** dentro do esperado para 7 anos neste jogo. Confiança moderada (9 partidas).
> **O que isto mede:** esperar antes de agir, num jogo de toque. **Não mede:** comportamento em sala, atenção em geral, aprendizagem.

**Rodapé fixo em todo cartão individual:**
> Isto é uma pista de sala de aula. Não é avaliação nem diagnóstico, e não substitui a equipe da escola.

**Regras:**
- **Título = ação observável aprovada na ontologia** (rótulo de sala, ex.: "Esperar o sinal"); o **construto técnico** fica na camada 2. Nunca texto livre (C10, E19).
- **Sem comparação com a turma.** A norma, quando aparece, é a etária do instrumento, e só na camada 2 (C4, S4).
- **Nome:** primeiro nome; inicial do sobrenome só com homônimo (S18).
- Sinais de construtos motores são suprimidos quando a criança joga com perfil de parâmetros alternativo (S15).

### Sinal de atenção
Aparece só depois de um número mínimo de partidas (parâmetro com o CIATec) e sempre nesta ordem. **"Partida"** é uma jogada de um microjogo; **"voo"** é a sessão de 3 jogos (E19).

> **Ana · Esperar o sinal · sinal de atenção**
> Nas últimas 3 semanas, a forma como Ana joga o Sinal Aberto mudou: ela tem tocado antes do sinal com mais frequência.
> **Antes de tudo, vale olhar o contexto:** mudou de aparelho, de horário ou de sala? Faltou nos últimos dias?
> **Se o contexto não explica:** observe em sala se ela tem esperado a vez em outras situações.
> **Encaminhamento:** converse com a professora do AEE ou com a coordenação. Se a escola achar necessário, a rede tem {serviço local}.
> [Confirmo o que observei] [Não observei isso em sala] [Já encaminhado]
> *Faixa para a idade, de onde veio e o que isto mede: ver detalhe.*

- **Chips do cartão**, sempre com ícone e texto, em `ceu-claro` com texto `ceu-profundo`: "evolução" (seta), "estável" (traço), "sinal de atenção" (lupa), "acesso" (tablet). O sinal de atenção se distingue pelo ícone e pelo texto, não pela cor; `sol` continua só recompensa (E19).
- Estados depois dos botões em `06` §2.
- Os três botões alimentam a métrica de precisão de alertas do PP5 (`[IN-35]`). "Não observei" registra a contestação e reduz o peso do sinal (LGPD art. 20) (S4).
- **Nunca** nomeia condição, nunca usa "risco" na interface, nunca usa vermelho nem âmbar. Para os relatórios FAPESP, a correspondência é "alerta de risco (projeto) = sinal de atenção (interface)" (C4).
- **Inferência associada a condição nunca chega ao painel** (`[IN-33]`).

### Perguntas em linguagem natural (Graph RAG)
O professor pergunta, o VUOO responde com **afirmação + evidência expansível + limite** (C9, `[IN-21]`):

> **Pergunta:** "Como a Ana está no jogo de lembrar a ordem?"
> **Resposta:** Ana lembrou sequências de 3 a 4 luzes nas últimas 6 partidas de Luzes em Ordem, sem mudança grande desde setembro.
> [Ver as 6 partidas] · [O que esse jogo mede]

**Quando não há evidência:** "Não tenho partidas suficientes para responder. Ana jogou esse jogo 2 vezes."
**Quando a pergunta é diagnóstica** ("A Ana tem TDAH?"): "Não respondo sobre diagnóstico. Posso mostrar o que observei nos jogos e sugerir com quem conversar na escola."

### Predição
Sempre como **faixa com incerteza**, em linguagem simples, e sempre com o que pode mudar:
> Se o ritmo das últimas semanas continuar, Ana deve chegar ao fim de novembro **entre 7 e 9 de cada 10** tentativas esperando o sinal. Essa estimativa muda se ela jogar menos de 2 dias por semana.

### Saída para o Plano Educacional Individualizado
Modelo exportável `[A CONFIRMAR formato aceito pelas secretarias, F4.1]`: **objetivo do plano → evidência do VUOO (cartões) → observação do professor (campo livre) → próximos passos**. O VUOO preenche só a coluna de evidência; o resto é do professor.

### Controles e uso
- Interruptor **"Mostrar sugestões automáticas"** (padrão ligado) (ECA Digital art. 17 §4º V).
- **O painel nunca entra em modo projeção.** Só o Céu da turma é projetável (S3).
- Exportação individual só para o próprio professor e o AEE.
- Avisos de acesso: "3 crianças ainda não tiveram vez no aparelho esta semana." Nunca no mesmo fluxo do Céu.

### Glossário (I27, I28, I29, S17)
| Usar | Evitar |
|---|---|
| estudante, criança | aluno-problema, caso |
| estudante autista, estudante com deficiência (respeitando a preferência da criança e da família) | portador, deficiente, especial, "sofre de" |
| sem condição identificada | típico, normal |
| sinal de atenção, padrão observado, pista | diagnóstico, suspeita, "possível TDAH", risco (na interface) |
| ainda não, em desenvolvimento, consolidando | errou, fracassou, atrasado |
| dentro / abaixo / acima da faixa para a idade **neste jogo** (só na camada 2) | "abaixo" sozinho, no título, ou sem o jogo |
| habilidade (código BNCC), objetivo do Plano Educacional Individualizado | score, nota, ranking, performance |
| sugestão | "o sistema recomenda que você deve" |
| Plano Educacional Individualizado (PEI), por extenso na primeira vez em cada tela | PEI sozinho (também é o Programa Ensino Integral na SEDUC-SP) |
| acompanhamento, trajetória | monitoramento, rastreamento |
| — | gêmeo digital, engajamento, insight, gamificação, IA preditiva, espelhar, provocar |

### Gestor (I30, S20)
Agregados, sem ordenar turmas nem escolas, com supressão de células com menos de 10 estudantes:
> Na Diretoria de Ensino de Franca, as turmas de 1º a 5º ano tiveram em média 3,2 dias de voo por criança por semana em setembro. 214 estudantes com Plano Educacional Individualizado têm acompanhamento contínuo registrado. *(contagem por diretoria; não exibida por escola)*

### Família (S2)
Relatório imprimível de uma página, na voz do professor, que mostra o que a criança fez e nunca o que faltou. O aviso de privacidade diz a verdade:
> O VUOO guarda como seu filho ou sua filha joga: o que tocou, quanto tempo levou e quando pausou. A professora usa isso para planejar as aulas. Ninguém de fora da escola vê o nome da criança. {se houver câmera: a câmera registra para onde a criança olha durante alguns jogos, e não grava o rosto.} Para saber mais ou pedir a exclusão dos dados: {contato do encarregado}.

### Selo de confiança (comunicação externa)
> Sem anúncios. Sem sorteios. Sem notificações para a criança. Sem coleta além do necessário. (I31)

---

## 14. DUA × linguagem (C11)

| Princípio do DUA | O que a linguagem já faz | Lacuna declarada |
|---|---|---|
| **Múltiplos meios de engajamento** | Tema de interesse; intensidade de celebração em 3 níveis; Modo suave; Ninho; convite recusável; "Agora não"; penas e coleção sem perda | O engajamento por interesse no palco de medida depende do protocolo (C3) |
| **Múltiplos meios de representação** | Voz + texto + pictograma em toda instrução; Libras nas instruções; letra bastão configurável; escala de texto; demonstração antes de jogar; pictogramas mapeáveis aos do AEE | Leitor de tela no palco; jogos inacessíveis a crianças cegas sem alternativa declarada |
| **Múltiplos meios de ação e expressão** | Toque simples na moldura; tolerância de movimento | **Só toque.** Voz, olhar (Wemoga Eye) e acionadores não estão especificados. Cada meio alternativo, se aceito pelo CIATec, gera um **perfil de parâmetros próprio** no palco de medida, registrado como tal (C11, S15) |
| **DUA na interface do professor** (vuoo §4) | Duas camadas no cartão; perguntas em linguagem natural; glossário sem jargão | O efeito por letramento digital precisa ser testado no co-design e no PP4 |
