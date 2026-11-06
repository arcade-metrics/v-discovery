---
produto: VUOO
slug: vuoo-microjogos
etapa: guia-de-estilo
status: rascunho
atualizado_em: 2026-11-05
---

# Guia de estilo do VUOO (versão inicial)

Ponto de entrada para quem vai desenhar, ilustrar, animar, escrever ou programar qualquer tela do VUOO. Este guia **resume e organiza** o que já está decidido ou proposto em outros arquivos; o detalhe fica nas fontes, e, se houver divergência, a fonte prevalece.

Marcas como no restante de `produtos/`: `[ASSUMIDO]` valor proposto sem dado; `[A CONFIRMAR]` depende de decisão de alguém; `[PRECEDENTE]` vem do estudo anterior de linguagem (1º ao 5º ano, microjogos), copiado em `base/precedente-linguagem/`, e entra aqui como proposta, não como decisão, por causa da D-31.

---

## 0. O que este guia já fixa e o que ainda não

| Área | Estado | Fonte principal |
|---|---|---|
| Princípios | proposta consolidada | §2; `base/parametrizacao-estilo.md` §1; `base/precedente-linguagem/03-linguagem.md` §2 |
| Estilo parametrizado (eixos, níveis, presets) | **decidido** o modelo (D-27 a D-29); valores `[ASSUMIDO]` | `base/parametrizacao-estilo.md` §2 a §6 |
| Limites invioláveis | candidatos a regra de negócio | `base/parametrizacao-estilo.md` §5 |
| Personalidade e tom de voz | `[PRECEDENTE]`, a adaptar por etapa escolar | `base/precedente-linguagem/03-linguagem.md` §2 e §12 |
| Movimento e som | regras definidas; valores `[ASSUMIDO]`; ferramentas **decididas** (D-37) | `base/parametrizacao-estilo.md` §3.1, §3.3 |
| Tokens | **decidido** o formato (W3C Design Tokens, D-36); valores em aberto | §11 |
| **Paleta** | **em aberto** (D-31, A-12) | critérios em §5 |
| **Tipografia** | **em aberto** (D-31, A-12) | critérios em §6 |
| **Personagem** | **em aberto** (D-31, A-12) | requisitos em §8 |
| **Marca e logotipo** | **em aberto** (D-31, A-12) | — |
| Linguagem de formas | em exploração | [`exemplos-de-design/`](../../exemplos-de-design/) (raiz do repositório) |

Resumo: o guia já diz **como** o estilo do VUOO se comporta e **o que ele nunca faz**. Ainda não diz **como ele se parece**. Essa é a primeira frente de design (D-31).

---

## 1. O estilo VUOO em uma frase

**Um estilo desenhado contra parâmetros: moderado por padrão, seguro nos dois extremos, que cada aluno ajusta ao próprio jeito sem deixar de reconhecer o VUOO.**

Público (D-24, D-30): ensino fundamental (anos iniciais e finais) e ensino médio, cerca de 6 a 17 anos, incluindo o público da educação especial. Dois lados (D-25): o **aluno**, que joga, e o **professor e gestor**, que acompanham. Plataformas (D-33, D-34, D-36): app Flutter (Android e iOS, celular e tablet), *mobile first*, com build web; painel do adulto na web em React.

---

## 2. Princípios

1. **Desenhar contra parâmetros, não contra valores.** Uma tela é aprovada quando funciona no mínimo, no padrão e no máximo de cada eixo, não quando fica bonita num ponto só (D-27, D-29).
2. **Padrão moderado, extremos de primeira classe.** O mínimo não é uma tela quebrada e o máximo não é um "modo festa" improvisado: os dois são desenhados e testados como o padrão (D-27).
3. **Acesso vence estética.** Em qualquer conflito, o parâmetro que garante acesso prevalece.
4. **Previsível antes de surpreendente.** Regras, rotina, tempo e fim são sempre conhecidos. Controles fixos não mudam de lugar `[PRECEDENTE]`.
5. **Mostra o que o aluno fez, nunca o que faltou.** Os dias que faltam aparecem como casas **neutras** (sem cor de alerta, sem "faltam"), sem perda por ausência, sem comparação com colegas (ofensiva compassiva, que pausa e nunca zera; `02-prd.md` §6).
6. **Literal para o aluno, transparente para o adulto.** Frases concretas para quem joga; evidência e limite por trás de cada afirmação para quem ensina `[PRECEDENTE]`.
7. **Nada na tela expõe o aluno aos colegas.** Preset, ajuste ou Plano Educacional Individualizado nunca aparecem para outro aluno (D-19 `[PRECEDENTE]`; `base/parametrizacao-estilo.md` §12).
8. **O aluno vê e desfaz toda mudança.** Manual, do professor ou da IA, toda mudança é nomeada em linguagem simples e reversível com um toque.
9. **Nomes de experiência, não de diagnóstico.** "Calmo", "Leitura apoiada", "Toque fácil"; nunca "Autismo", "Dislexia" ou "TDAH".
10. **Estilo não muda o que está sendo avaliado.** Na avaliação em momentos marcados (`02-prd.md` §7), os estímulos ficam protegidos de presets e da IA; só as acomodações de acesso continuam valendo (L-07; palco de medida, D-20 `[PRECEDENTE]`).

---

## 3. Personalidade e tom de voz

### 3.1 Personalidade `[PRECEDENTE]`
**Arquétipo: o Companheiro.** O colega mais velho e paciente que senta ao lado.

| É | Não é |
|---|---|
| calmo | apático |
| caloroso | meloso, infantilizado |
| curioso | intrometido |
| constante | repetitivo a ponto de irritar |
| direto | seco, mandão |
| brincalhão no gesto | irônico na fala |

O humor padrão é **pastelão físico** (`per.humor`): compreensível sem ler entrelinhas. A personalidade é a mesma nas três estéticas; o que muda com a idade é a forma, não o caráter.

### 3.2 Regras de escrita para o aluno
Valem em qualquer etapa:

1. Uma ação pedida por frase, no presente e no afirmativo.
2. Botões dizem exatamente o que acontece. Nunca "OK" ou "Vamos lá?".
3. Elogio descreve a ação, não a pessoa.
4. O erro informa sem julgar ("Esse não." + a instrução).
5. Sem ironia, sarcasmo, ameaça, culpa ou tristeza como alavanca.
6. Toda frase é verdadeira em qualquer dia: nada de "amanhã tem mais" ou "senti sua falta".
7. Um nome por coisa, sempre o mesmo.
8. Sem itálico, sem texto justificado, sem texto sobre imagem.

**Por etapa** `[A CONFIRMAR]`:

| | Anos iniciais | Anos finais | Ensino médio |
|---|---|---|---|
| Estética (`apa.estetica`) | lúdica | jovem | sóbria |
| Tamanho da frase | até 8 palavras `[PRECEDENTE]` | `[A CONFIRMAR]` | `[A CONFIRMAR]` |
| Frases por instrução | 1 a 2 | 2 | 2 |
| Leitura automática | instruções | desligada | desligada |
| Pictograma em toda instrução | sim | opcional | opcional |

O nível de linguagem é um **eixo de acesso** independente da idade: um aluno de 15 anos que lê como um de 2º ano recebe linguagem simples com a estética da idade dele.

**Fonte única de falas** `[PRECEDENTE]`: toda fala tem um ID, um texto (`.texto`) e uma versão para voz (`.voz`), numa tabela só (modelo em `base/precedente-linguagem/06-especificacao-base.md` §4). **Número nunca é falado em feedback.**

**Mascote, evento → reação** `[PRECEDENTE]`: as reações do mascote seguem uma matriz evento → reação com prioridade quando eventos coincidem (modelo no mesmo arquivo, §5). Critério de aceite: **nenhuma reação depende de acerto ou erro.**

**Nunca dizer** (exemplos colhidos nas revisões do precedente): "Errado." · "Quase!" · "Ops!" · "Está difícil?" · "Amanhã tem mais." · "Vou sentir sua falta." · "Onde você estava?" · "Você merece!" · "12 de 20."

### 3.3 Tom para o adulto `[PRECEDENTE]`
| | Professor | Gestor |
|---|---|---|
| Quem fala | o VUOO, como colega experiente | o VUOO, como parceiro técnico |
| Mostra | o que observou, de onde veio, o limite, o que sugere | agregados sem ordenação |
| Nunca | diagnóstico, nome de condição, comparação com a turma, jargão | exposição de aluno; ranking de turma ou escola |

Glossário de uso e de termos a evitar em `base/precedente-linguagem/03-linguagem.md` §13. O lado do adulto terá guia próprio quando for desenhado (D-25).

---

## 4. Estilo parametrizado (resumo)

O detalhe completo está em `base/parametrizacao-estilo.md`. O essencial:

**Três tipos de eixo:**
- **estímulo**, do mínimo ao máximo em torno do moderado: movimento, saturação, som, densidade, personagem, celebração;
- **acesso**, que só aumenta o apoio: tamanho, contraste, tempo, tolerância de toque, leitura;
- **escolha**, sem ordem de intensidade: tema claro ou escuro, estética por idade, voz, fonte, cor de destaque.

**Escala de 5 níveis dos eixos de estímulo:** 0 Mínimo · 1 Calmo · **2 Moderado (padrão)** · 3 Expressivo · 4 Máximo.

**Famílias de parâmetros:** `mov.*` movimento · `cor.*` cor e luz · `som.*` e `hap.*` som e háptica · `tam.*` tamanho e espaço · `txt.*` texto e linguagem · `den.*` densidade visual · `tmp.*` tempo · `ent.*` entrada · `per.*` e `fb.*` personagem e feedback · `apa.*` aparência · `pre.*` previsibilidade.

**Presets:** o estudo prevê 6 bases de estímulo (Mínimo, Calmo, Moderado, Foco, Vibrante, Máximo) e 18 complementos. **Na v0.0.0: Calmo, Moderado (sempre o padrão) e Vibrante, mais 5 complementos** (`02-prd.md` §8). Tudo fica nas configurações do jogador; não há calibração no primeiro acesso. O aluno ajusta por cima e pode salvar até 3 presets próprios `[ASSUMIDO]`.

**Ordem de resolução:** limites invioláveis → travas do professor → ajustes do aluno → complementos → base → sistema operacional → padrão do produto. Entre dois complementos, em estímulo vence o **menor**; em acesso, o **mais generoso**.


---

## 5. Cor

**A paleta da marca está em aberto (D-31).** O que já está fixado são os critérios que qualquer paleta precisa cumprir.

### 5.1 Critérios
1. **Definida em OKLCH**, porque `cor.saturacao` multiplica o croma (0,15 · 0,5 · **0,8** · 1,0 · 1,15). O padrão usa 80% do croma da marca.
2. **Contraste em toda combinação** de tema (claro, escuro, sépia), saturação, visão de cor (típica, protanopia, deuteranopia, tritanopia, monocromática) e contraste: texto ≥ 4,5:1, componentes ≥ 3:1 (L-02). No padrão, texto principal ≥ 7:1.
3. **Validada por script antes de publicar.** Reaproveitar e estender `base/precedente-linguagem/ferramentas/contraste.py`, que já valida pares e distância entre tons para daltonismo.
4. **Cor nunca é o único código** (L-03): todo estado tem forma, ícone ou texto.
5. **Uma cor forte e duas claras por tela** no padrão (`cor.fortes_por_tela`).
6. **Fundo em branco quebrado** por padrão (`cor.brilho_maximo`), nunca branco puro como fundo de tela.
7. **Erro não é vermelho de alarme** (proposta, `[PRECEDENTE D-09]`).
8. **6 a 8 cores de destaque pessoal**, todas validadas, para o aluno escolher "minha cor".
9. **Rótulo de botão primário passa em AA.** O benchmark mostra que os botões do Duolingo falham até 3:1 ([`benchmarks/duolingo/03-estilo.md`](../../benchmarks/duolingo/03-estilo.md) §1); o VUOO não repete isso.

### 5.2 Papéis que a paleta precisa cobrir
Os papéis do precedente continuam úteis mesmo com cores novas. A paleta nova precisa de um token semântico para cada um:

| Papel | Exemplo de uso |
|---|---|
| fundo, superfície | fundo da tela, cartões |
| divisória, contorno | trilho de barra; borda de alvo (≥ 3:1) |
| texto, texto secundário | instrução, rótulo |
| marca / ação principal, pressionado | botão primário |
| destaque claro | área de atenção |
| recompensa | conquista, peça nova (só em áreas pequenas `[PRECEDENTE]`) |
| concluído | atividade feita |
| ajuda / pista | dica, contorno de pista |
| foco | anel de foco |
| personagem | corpo, rosto, detalhes |

**Precedente para comparar:** `base/precedente-linguagem/ferramentas/paleta.json` (azul `ceu`, âmbar `sol`, verde `folha`, lavanda; 40 pares aprovados nos modos padrão, suave e alto contraste).

---

## 6. Tipografia

**As famílias estão em aberto (D-31).** Critérios:

1. **Uma opção de alfabetização** para os anos iniciais: "a" e "g" de um andar, I, l e 1 bem diferentes (`txt.familia`).
2. **Uma opção de alta legibilidade**, sempre disponível como escolha do aluno.
3. **Uma fonte de marca** para anos finais e médio `[A CONFIRMAR]`.
4. **Licença** que permita uso comercial em app e web (OFL ou comprada), com arquivos que funcionem em Flutter e no navegador.
5. **Aguenta os eixos de acesso:** texto até 300% com reflow para uma coluna; espaçamento de letras até +0,12 em, de palavras até +0,16 em, entrelinha até 2,0 (WCAG 1.4.12).
6. **Números tabulares** para o painel do adulto.
7. **Caixa alta (letra bastão)** configurável para o 1º ano.
8. **Não adotar fonte "para dislexia" como solução.** O que tem evidência é tamanho e espaçamento.

**Padrões iniciais** (`base/parametrizacao-estilo.md` §3.4 e §3.5): espaço entre letras +0,03 em; entrelinha 1,5; linha de até 40 caracteres nos anos iniciais e 60 nos demais.

**Precedente:** Andika (alfabetização) e Atkinson Hyperlegible Next (interface), com escala de instrução 28/40 px e rótulo 20/28 px (`base/precedente-linguagem/03-linguagem.md` §6).

---

## 7. Forma e ilustração

### 7.1 Regras
- **Vetorial e plana**, poucas camadas, leve para aparelho fraco e uso offline.
- **Cores ligadas a tokens** (SVG com variáveis), para que saturação, tema, contraste e visão de cor se apliquem sem redesenhar.
- **Camadas nomeadas**, cada uma ligada a um nível de `den.ilustracao`: `fundo`, `cenario`, `decoracao`, `personagem`, `tarefa`, `foco`. No nível 0 só aparecem `tarefa` e `foco`.
- **Silhueta legível em escala de cinza** (teste obrigatório no modo monocromático).
- **Uma família de ilustração por estética** (lúdica, jovem, sóbria), com a mesma gramática de camadas.
- **Pessoas diversas** nos avatares: tons de pele, cabelos, óculos, aparelho auditivo, cadeira de rodas, abafador de ruído, sem destacar ninguém `[PRECEDENTE]`.
- **Lugares brasileiros reais** `[PRECEDENTE]`.

**Construção** `[PRECEDENTE]` (detalhe em `base/precedente-linguagem/guia-pratico-design.md` §6 e `transformar-em-vuoo.md`):

- **Formas básicas:** retângulo arredondado, círculo/oval e triângulo arredondado. Toda forma complexa é uma soma delas.
- **Sem traço de contorno:** as formas se separam pela cor.
- **Volume por tom interno, nunca por sombra:** três tons por cor (luz, base, tom interno); luz sempre do alto à esquerda. Sem sombra projetada, gradiente, textura, desfoque ou transparência.
- **Cantos arredondados, nenhuma ponta viva.** Não há vilões; nada hostil ou ameaçador.
- **Contraste sem traço:** objeto que se toca tem ao menos metade da borda com 3:1 contra o fundo e fica sobre um palco (cartão com borda de 2 px, 3 px em alto contraste).
- **Proporção:** cabeça com 1/3 da altura nos anos iniciais e 1/4 a partir dos 9 anos.
- **Objetos com rosto:** nunca falam; só as expressões do conjunto do personagem; a emoção vem da história do jogo, **nunca do acerto ou erro**; sem rosto quando a tarefa não pede.
- **Pictogramas próprios.** O ARASAAC não permite uso comercial.

### 7.2 Linguagem de formas (em exploração)
Os esboços em [`exemplos-de-design/`](../../exemplos-de-design/) (raiz do repositório) testam três famílias:

| Família | Construção | Potencial descrito | Leitura contra os princípios |
|---|---|---|---|
| **Redonda** | círculos, elipses, volumes arredondados; olhos grandes; pode dispensar contorno | personagens simpáticos, expressivos, construção simples | a mais alinhada a "suave por padrão" e a leitura fácil de expressão; boa base para a estética lúdica |
| **Blocada** | quadrados, retângulos, trapézios; proporções exageradas | personagens irreverentes, silhueta forte | serve a contraste entre personagens e à estética jovem; a irreverência fica no gesto, nunca na fala (§3.2) |
| **Afunilada** | triângulos, pontas, assimetrias | tensão visual, atitude, individualidade | útil com moderação na estética jovem e sóbria; pontas em excesso contrariam a forma arredondada recomendada para baixa carga visual |

**Proposta** `[ASSUMIDO]`: escolher **uma família dominante** para a marca e o personagem principal, e permitir as outras como **secundárias** por estética ou para diferenciar personagens. O Duolingo faz algo parecido: toda ilustração parte de três formas arredondadas, com uma quantidade controlada de formas por figura ([`benchmarks/duolingo/03-estilo.md`](../../benchmarks/duolingo/03-estilo.md) §3).

---

## 8. Personagem

**Arte, espécie e nome estão em aberto (D-31).** Qualquer proposta precisa cumprir:

1. **Expressões em conjunto fixo**: 5 no padrão (`per.expressividade`), de neutra fixa no nível 0 a exagero cartunesco no 4.
2. **Sem arte de tristeza, decepção, raiva ou medo.** Diante do erro, o personagem fica curioso; o erro tem uma única versão em todos os níveis (L-06).
3. **Leitura testada antes de fechar a arte**: o precedente propõe ≥ 80% de compreensão das expressões pelos alunos mais novos `[PRECEDENTE HIP-4]`.
4. **Personalidade estável e literal**, humor físico (§3.1).
5. **Mesmo lugar e mesmo tamanho** em todas as telas; o aluno pode escondê-lo (`per.presenca` = 0).
6. **Três versões por estética** (`apa.mascote_visual`): personagem infantil, versão jovem, só ícone.
7. **Pose estática desenhada** para o nível 0, não um quadro congelado ao acaso.
8. **Animável em Rive** com entradas de intensidade, velocidade e repouso (D-37).
9. **Sem gênero, espécie ou conotação cultural que exclua** alguém `[PRECEDENTE]`.
10. **Entra no acordo de propriedade intelectual** junto com a marca (D-18 `[PRECEDENTE]`).
11. Compatibilidade com a animatrônica do projeto do CIATec (`[IN-13]`): não é requisito do produto, que é independente do projeto desde 2026-11-05; só entra se uma decisão de produto a adotar.

**Precedente:** o VUOO Bot, robô com visor, olhos e boca de luz e asas curtas, com cinco expressões (atento, contente, curioso, pensando, sossegado) (`base/precedente-linguagem/03-linguagem.md` §4).

---

## 9. Movimento

- **Funcional, curto e previsível.** No padrão: transição de 250 ms com deslize curto; resposta com pulso único de 250 ms; deslocamento até 24 px e escala até 1,05.
- **Nada súbito, nada piscando:** no máximo 3 flashes por segundo em qualquer nível (L-01); sem parallax até o nível 2.
- **Personagem parado em repouso** nos níveis baixos; respiração leve no padrão.
- **Todo laço com mais de 5 s é pausável** (L-05).
- **`prefers-reduced-motion`** do sistema define o valor inicial como 1 ou 0.
- **Três camadas de ferramenta** (D-37): código Flutter para interface e peças simples; Rive para personagens e peças com estados; After Effects → Lottie para animações lineares.
- **Três versões entregues por animação-chave** (calma, moderada, máxima) e a pose estática do nível 0; o nível 3 pode ser interpolado.

Tabela completa por nível em `base/parametrizacao-estilo.md` §3.1.

---

## 10. Som e háptica

- **Canais com volume separado:** voz, efeitos, música e ambiente. Música e efeitos abaixam quando há fala.
- **Voz é a referência:** cerca de −16 LUFS integrados, pico ≤ −1 dBTP `[ASSUMIDO]`. No padrão, efeitos a −12 dB da voz e música só no mapa e nas transições a −24 dB (A-03).
- **Sem buzina, alarme, tique-taque ou som de erro "murcho"**, em nenhum nível; o erro não tem contorno descendente.
- **O som nunca é o único canal**: legendas ligadas para fala de personagem por padrão `[ASSUMIDO]`; indicador visual de som como opção.
- **Cada som em três variantes** (suave, padrão, brilhante), normalizado, com metadado de canal, graves e ataque.
- **Háptica leve**, só em confirmação, no padrão.

---

## 11. Layout, componentes e tokens

### 11.1 Layout
- **Mobile first a partir de 360 px**, com versão de tablet; o build web usa o mesmo código (D-34).
- **Controles fixos que nunca mudam de lugar** (L-04): Pausar em cima à esquerda, Ouvir em cima à direita, Ajustes embaixo à esquerda. As posições exatas estão em aberto (A-05); a regra de que não mudam, não.
- **Alvos de toque:** 64 px nos anos iniciais, 56 nos finais, 48 no médio `[ASSUMIDO]`; nunca abaixo de 44 px, com espaço entre alvos de 16 px (nunca abaixo de 8) (L-10).
- **Toque simples**, aceito na soltura do dedo; arrastar sempre tem a alternativa "tocar e tocar".

### 11.2 Componentes
Cada componente tem uma ficha com os estados (padrão, pressionado, foco, desabilitado, carregando, feito, erro), os **parâmetros que o afetam** e o comportamento em cada canto (mínimo, moderado, máximo, acesso extremo). Exemplo em `base/parametrizacao-estilo.md` §9.6.

### 11.3 Wireframes
Toda tela é entregue em **cinco quadros**: moderado em 360 px, mínimo, máximo, acesso extremo (texto 300%, alvo 128 px, um item por tela) e ordem de leitura linear para leitor de tela e varredura. Mais o tablet no moderado. Uma tela só é aprovada quando os cinco funcionam.

### 11.4 Tokens
- **Arquivo único no formato W3C Design Tokens**, lido pelo app Flutter e pelo painel React (D-36).
- **Cadeia:** perfil do aluno → resolvedor de presets → tokens → componentes, ilustração, animação e som. Nenhuma peça referencia valor fixo.
- **Nomes semânticos** (papel), nunca descritivos de cor.
- **Ponto de partida para espaço e raio** `[PRECEDENTE]`: espaço em base 4 (4, 8, 12, 16, 24, 32, 48, 64); raios 8, 14, 20 e pílula; anel de foco de 3 px com afastamento de 3 px.

---

## 12. Limites invioláveis

Nenhum preset, ajuste manual, trava do professor ou ação de IA ultrapassa os limites **L-01 a L-10**: flashes (L-01), contraste (L-02), cor como único código (L-03), controles fixos (L-04), laços pausáveis (L-05), erro não punitivo (L-06), estímulos de medida protegidos (L-07), teto da IA (L-08), mudança automática anunciada e reversível (L-09) e alvos mínimos (L-10). O texto exato e a base normativa de cada um estão em `base/parametrizacao-estilo.md` §5, dono único.

**Candidatos vindos do precedente** `[A CONFIRMAR]` para o público ampliado: sem ranking entre alunos; sem perda ou punição por ausência; sem contagem regressiva visível para o aluno; sem recompensa aleatória (a forma da regra está em A-11).

---

## 13. Checklist de entrega

- [ ] Nenhum valor fixo; tudo em token.
- [ ] Ilustração em camadas nomeadas, testada no nível 0.
- [ ] Silhueta legível em escala de cinza.
- [ ] Três versões das animações-chave e a pose estática.
- [ ] Nenhum flash acima de 3 por segundo (ferramenta de fotossensibilidade).
- [ ] Sons em três variantes, normalizados.
- [ ] Contraste validado por script em todas as combinações.
- [ ] Cinco quadros de wireframe aprovados.
- [ ] Textos revisados contra §3.2 e a lista "nunca dizer".
- [ ] Nenhum nome de preset ou ajuste fala de diagnóstico.

---

## 14. O que falta para a versão 1 deste guia

As lacunas estão em [`decisoes.md`](decisoes.md) §2. As que bloqueiam este guia: **A-12** (paleta, tipografia, personagem e marca), **A-13** (linguagem de formas), **A-14** (metáfora do voo), **A-15** (tom para anos finais e médio), **A-16** (pictogramas), **A-02** (padrões por etapa), **A-03** (música), **A-05** (posição dos controles) e **A-11** (recompensa aleatória).

---

## Fontes

- [`decisoes.md`](decisoes.md): decisões D-24 a D-37 e questões abertas A-nn.
- `base/parametrizacao-estilo.md`: parâmetros, presets, limites, implicações para arte.
- `base/precedente-linguagem/` (03-linguagem, 04-microjogos, 05-decisoes, 06-especificacao-base, guia-pratico-design, transformar-em-vuoo, ferramentas, pesquisa): precedente de marca, Bot, cor, tipografia, movimento, som, tom e tokens.
- [`benchmarks/duolingo/03-estilo.md`](../../benchmarks/duolingo/03-estilo.md) e [`05-riscos-educacao-especial.md`](../../benchmarks/duolingo/05-riscos-educacao-especial.md) (fora da pasta, por exceção): o que copiar e o que evitar do Duolingo.
- [`exemplos-de-design/`](../../exemplos-de-design/) (raiz do repositório): esboços de linguagem de formas (redonda, blocada, afunilada).
