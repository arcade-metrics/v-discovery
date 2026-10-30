---
produto: VUOO
slug: vuoo
etapa: estilo-aluno/01-parametrizacao
status: rascunho para discussão
atualizado_em: 2026-10-30
---

# Estilo adaptativo do aluno: parametrização

Documento de trabalho para discutir **como o lado do aluno se parece, se move e soa**, antes de desenhar qualquer tela. A tese é uma só: **nenhuma tela, ilustração, animação ou som é desenhada num valor fixo. Tudo é desenhado contra parâmetros**, que o aluno, o professor e, mais tarde, a IA podem mover dentro de limites.

Escrito primeiro para ser lido por um modelo de linguagem (ids estáveis, tabelas, regras numeradas), depois por pessoas. Marcas: `[ASSUMIDO]` valor proposto sem dado; `[A CONFIRMAR]` depende de decisão de alguém; `[A PESQUISAR]` depende de domínio de `conhecimento/` ainda não pesquisado; `[VUOO]` precedente do estudo `produtos/vuoo-linguagem/`, reaproveitado aqui como proposta.

---

## 0. Decisões já tomadas (pelo usuário, 30/10/2026)

A numeração continua a de `../../vuoo-linguagem/05-decisoes.md` (D-01 a D-23), para não haver dois D-01 no mesmo produto.

| Código | Decisão |
|---|---|
| **D-24** | Público-base: **ensino fundamental (anos iniciais e finais) e ensino médio**, aproximadamente 6 a 17 anos, incluindo o público da educação especial. |
| **D-25** | Dois lados: aluno (jogador) e professor/gestor. **Este documento trata só do aluno.** |
| **D-26** | Fundamentos: desenho universal, design centrado no ser humano e DUA. |
| **D-27** | O estilo é **adaptativo e parametrizado**: movimento, cor, som, tamanho e demais eixos são configuráveis. O **padrão é moderado**, mas o sistema é projetado para funcionar nos **dois extremos** (mínimo e máximo). |
| **D-28** | Há **muitos presets**, além de **personalização** pelo aluno, que pode salvar a própria combinação. |
| **D-29** | Arte, estilo, wireframes e componentes **partem da parametrização**. Numa fase posterior, os parâmetros serão **acionáveis por IA**. |
| **D-30** | O produto é o **VUOO**. Isto amplia o público das propostas (1º ao 5º ano em `[IN-06]` e na proposta do CIATec) para o fundamental inteiro e o médio. |
| **D-31** | **Identidade visual começa do zero**: paleta, tipografia, personagem e marca. As propostas de identidade de `../../vuoo-linguagem/03-linguagem.md` (cor `ceu`, Bot, Andika) ficam como precedente, não como ponto de partida. É a primeira frente de design. |
| **D-32** | O orçamento de produção das variantes (animação, som, estéticas, Libras, audiodescrição) é ajustado **depois do primeiro ciclo completo de uma atividade e dos testes**. Desenvolve-se desde já prevendo essa fase. |
| **D-33** | O VUOO é **aplicativo** (Android e iOS, smartphone e tablet), sobretudo para o aluno, e **também precisa funcionar na web**. |
| **D-34** | O cliente do aluno é feito em **Flutter** desde o início, *mobile first*. A versão web do aluno é o build web do mesmo código (D-36). |
| **D-35** | A primeira versão construída chama-se **v0.0.0**, não "protótipo". Antes dela, escreve-se uma documentação orientadora para o seu desenvolvimento. |
| **D-36** | **Aluno:** Flutter no app (Android e iOS) e o build web do mesmo código como secundário; atividades com medida só no app. **Professor e gestor:** web em React. **Tokens de estilo** em arquivo único no formato W3C Design Tokens, lido pelos dois. |
| **D-37** | **Animação em três camadas.** *Código Flutter*: interface e peças simples de jogo (escala, posição, cor, rebote), guiadas pelos tokens de movimento. *Rive*: personagens e peças interativas com estados; custo por animador, runtime MIT, arquivos exportados seguem funcionando sem assinatura. *After Effects → Lottie*: animações lineares (celebrações, conquistas, aberturas, ícones), com guia de recursos suportados para aparelhos fracos. Alternativa registrada caso o Rive seja vetado: Spine (licença única). |

Tudo o que vem abaixo é proposta para discussão, salvo o que estiver nesta tabela.

---

## 1. Princípios

1. **Desenhar contra parâmetros, não contra valores.** Uma tela é aprovada quando funciona no mínimo, no padrão e no máximo de cada eixo, não quando fica bonita num ponto só.
2. **Padrão moderado, extremos de primeira classe.** O máximo não é um "modo festa" improvisado nem o mínimo é uma tela quebrada: os dois são desenhados, ilustrados, animados e testados como o padrão.
3. **Três tipos de eixo, com lógicas diferentes** (ver §2):
   - **estímulo**: vai do mínimo ao máximo em torno do moderado (movimento, saturação, som, densidade, personagem, celebração);
   - **acesso**: parte do padrão e só aumenta o apoio (tamanho, contraste, tempo, tolerância de toque, leitura);
   - **escolha**: opções sem ordem de intensidade (tema claro ou escuro, estética por idade, voz, fonte, cor de destaque).
4. **Nomes de presets falam de experiência, não de diagnóstico.** "Calmo", "Leitura apoiada" e "Toque fácil", nunca "Autismo", "Dislexia" ou "TDAH". Quem precisa de um preset nem sempre tem um laudo, e quem tem um laudo nem sempre precisa daquele preset (`acs.found.disability-models` `[A PESQUISAR]`).
5. **Aparência por idade e nível de leitura são independentes.** Um aluno de 15 anos que lê como um de 2º ano recebe linguagem simples com estética da idade dele `[VUOO S15]`.
6. **Acesso vence estética.** Em qualquer conflito, o parâmetro que garante acesso prevalece sobre o que define estilo.
7. **O aluno vê e entende o que mudou.** Toda mudança, manual, do professor ou da IA, é visível, nomeada em linguagem simples e reversível com um toque.
8. **Estilo não muda o que está sendo avaliado.** Se uma atividade tem estímulos de medida, eles são protegidos de presets e da IA (o "palco de medida" do VUOO, `[VUOO D-20]`). A fronteira entre acomodação e modificação está em `acs.adapt.accommodation-vs-modification` `[A PESQUISAR]`.

---

## 2. Modelo de parâmetro

Cada parâmetro tem a mesma ficha. É esta ficha que o motor de estilo, os designers e a IA leem.

| Campo | Significado | Exemplo |
|---|---|---|
| `id` | Identificador estável, `eixo.nome` | `mov.amplitude` |
| `tipo_eixo` | `estimulo`, `acesso` ou `escolha` | `estimulo` |
| `tipo_valor` | `nivel` (0 a 4), `continuo`, `discreto`, `booleano`, `enum` | `nivel` |
| `valores` | Faixa ou lista | 0 a 4 |
| `padrao` | Valor inicial do produto | 2 |
| `extremo_min` / `extremo_max` | O que o parâmetro faz em cada ponta | sem deslocamento / até a tela inteira |
| `escopo` | Onde vale: `moldura`, `conteudo`, `medida` (nunca, salvo protocolo) | `moldura`, `conteudo` |
| `quem_muda` | `aluno`, `professor`, `familia`, `ia`, `sistema` | aluno, professor, ia |
| `travavel` | O professor pode fixar o valor? | sim |
| `piso_teto` | Limite que nenhum ator ultrapassa (ver §5) | ≤ 3 flashes/s |
| `base` | Norma, evidência ou precedente | WCAG 2.3.3 |

### A escala de 5 níveis dos eixos de estímulo

| Nível | Nome | Ideia |
|---|---|---|
| 0 | **Mínimo** | Só o necessário para a tarefa. Nada se move sem ação do aluno, nenhum som que não seja fala, cor só para codificar. |
| 1 | **Calmo** | Feedback presente, discreto e lento. Sem partículas, sem música. |
| 2 | **Moderado** (padrão) | Jogo reconhecível como jogo, sem súbitos, sem saturação alta, sem som alto. |
| 3 | **Expressivo** | Animação com exagero, celebração visível, música em transições, cenário vivo. |
| 4 | **Máximo** | Tudo o que o estilo permite dentro dos limites invioláveis: partículas, molas, cenário animado, fanfarra, háptica forte. |

Eixos de acesso usam degraus próprios (por exemplo, texto de 100% a 300%), sempre a partir do padrão e só para mais apoio.

---

## 3. Eixos e parâmetros

Valores numéricos são `[ASSUMIDO]` até a validação com usuários, salvo quando citam norma.

### 3.1 Movimento (`mov.*`) · estímulo

| id | 0 Mínimo | 1 Calmo | 2 Moderado | 3 Expressivo | 4 Máximo | Base |
|---|---|---|---|---|---|---|
| `mov.intensidade` (mestre) | 0 | 1 | **2** | 3 | 4 | move os demais `mov.*` juntos |
| `mov.transicao` | troca instantânea ou esmaecimento ≤ 100 ms | esmaecimento 300 ms | deslize 250 ms | deslize 250 ms com ultrapassagem leve | sequência encadeada 350 ms | `[VUOO]` 200–300 ms |
| `mov.amplitude` (deslocamento e escala máximos) | 0 px, só opacidade | ≤ 8 px, escala ≤ 1,02 | ≤ 24 px, ≤ 1,05 | ≤ 64 px, ≤ 1,15 | tela inteira, ≤ 1,3, achatar e esticar | WCAG 2.3.3 |
| `mov.curva` | linear | saída suave | saída suave | saída com recuo | mola | — |
| `mov.particulas` (por evento) | 0 | 0 | ≤ 12, só no fim da atividade | ≤ 40 | ≤ 120, confete de tela cheia sem piscar | — |
| `mov.repouso` (personagem e cenário parados) | estático | estático, piscar a cada 6–8 s | respiração leve | gestos de espera | personagem e cenário vivos | `[VUOO]` Bot parado em repouso |
| `mov.parallax` | desligado | desligado | desligado | ≤ 8 px | ≤ 24 px | risco vestibular, WCAG 2.3.3 |
| `mov.tremor_tela` | nunca | nunca | nunca | nunca | ≤ 4 px por ≤ 200 ms, **só em acerto ou celebração** | — |
| `mov.feedback_resposta` | troca de estado sem animação | contorno aparece em 150 ms | pulso único 250 ms | pulso + rebote | pulso + partículas + rebote | — |
| `mov.icones_animados` | estáticos | estáticos | animam ao receber foco | animam em laço curto | animam sempre (com pausa automática) | benchmark: ícones animados aumentaram início de lições (`benchmarks/duolingo/03-estilo.md §3`) |
| `mov.video_autoplay` | desligado | desligado | desligado | ligado sem som | ligado | WCAG 2.2.2 |

**Fora da escala (piso e teto de §5):** no máximo 3 flashes por segundo em qualquer nível (WCAG 2.3.1); todo laço com mais de 5 s tem pausa (WCAG 2.2.2); `prefers-reduced-motion` do sistema define o valor inicial como 1 ou 0.

### 3.2 Cor e luz (`cor.*`)

| id | Tipo | Valores | Padrão | Mínimo → Máximo | Base |
|---|---|---|---|---|---|
| `cor.saturacao` | estímulo | multiplicador do croma OKLCH: 0,15 · 0,5 · 0,8 · 1,0 · 1,15 | **0,8** | quase cinza (codificação por forma mantida) → acima da marca, até o limite do gamut | benchmark: verde saturado sobre branco sobrecarrega (`03-estilo.md §3`) |
| `cor.fortes_por_tela` | estímulo | 0 · 1 · 1 forte + 2 claras · 3 · livre | **1 forte + 2 claras** | nenhuma cor forte → paleta de seção livre | `[VUOO]` "uma cor forte por tela" |
| `cor.fundo` | estímulo | liso · liso · ilustração suave · ilustração plena · ilustração animada | **ilustração suave** | — | — |
| `cor.contraste` | acesso | padrão (texto ≥ 4,5:1, componentes ≥ 3:1) · reforçado (≥ 7:1 e ≥ 4,5:1) · máximo (≥ 12:1, bordas 3 px) | **padrão**, já com texto principal ≥ 7:1 `[VUOO]` | — | WCAG 1.4.3, 1.4.6, 1.4.11 |
| `cor.visao_de_cor` | acesso | típica · protanopia · deuteranopia · tritanopia · monocromática | **típica** | — | `acs.dim.visual` `[A PESQUISAR]` |
| `cor.tema` | escolha | claro · escuro · sépia | **claro** (ou o do sistema) | — | — |
| `cor.brilho_maximo` | acesso | branco puro · branco quebrado · sépia | **branco quebrado** | — | — |
| `cor.destaque_pessoal` | escolha | 6 a 8 cores validadas para o aluno chamar de "minha cor" | marca | — | identidade e pertencimento |
| `cor.sobreposicao_leitura` | escolha | desligada · tons | **desligada** | — | evidência fraca para sobreposições coloridas `[A PESQUISAR]` |

**Regras de cor (candidatas a invariante):** cor nunca é o único código (WCAG 1.4.1); toda combinação de saturação, tema e visão de cor é validada por script antes de publicar, como `produtos/vuoo-linguagem/ferramentas/contraste.py` faz para o VUOO; o tom de erro não é vermelho de alarme (`[VUOO D-09]`, proposta).

### 3.3 Som e háptica (`som.*`, `hap.*`)

Volumes em dB relativos à voz, que é a referência `[ASSUMIDO]`: voz normalizada em cerca de −16 LUFS integrados, pico real ≤ −1 dBTP.

| id | 0 Mínimo | 1 Calmo | 2 Moderado | 3 Expressivo | 4 Máximo |
|---|---|---|---|---|---|
| `som.efeitos` | desligado | −18 dB | **−12 dB** | −6 dB | −3 dB |
| `som.musica` | desligada | desligada | **só em mapa e transições, −24 dB** | também em atividades sem fala, −18 dB | contínua, −12 dB |
| `som.ambiente` | desligado | desligado | desligado | −24 dB | −18 dB |
| `som.dinamica` | ataque ≥ 30 ms, sem graves < 100 Hz | ataque ≥ 20 ms | **ataque ≥ 10 ms, compressão leve** | transientes permitidos | transientes e graves permitidos |
| `som.feedback` | nenhum | só acerto, uma nota | **acerto e erro neutro (sem contorno descendente)** | + som de sequência | + fanfarra |
| `hap.intensidade` | desligada | leve | **leve, só em confirmação** | média | forte, padrões rítmicos |

| id | Tipo | Valores | Padrão |
|---|---|---|---|
| `som.voz` | acesso | 0 a 100% | **100%** |
| `som.abaixar_sob_voz` | invariante | música e efeitos abaixam quando há fala | sempre ligado |
| `som.leitura_automatica` | acesso | desligada · instruções · tudo | **instruções** nos anos iniciais, **desligada** nos demais `[A CONFIRMAR]` |
| `som.velocidade_fala` | acesso | 0,75× a 1,5× | **1×** |
| `som.voz_escolhida` | escolha | vozes disponíveis | por idade |
| `som.pacote` | escolha | madeira e marimba (suave) · padrão · arcade | **padrão** |
| `som.mono` | acesso | ligado · desligado | desligado |
| `som.indicador_visual` | acesso | cada som tem ícone ou legenda na tela | desligado (ligado no preset "Sem som") |
| `som.legendas` | acesso | desligadas · ligadas, com tamanho e fundo ajustáveis | **ligadas** para toda fala de personagem `[ASSUMIDO]` |
| `hap.substitui_som` | acesso | vibração traduz eventos sonoros | desligado |

**Regras:** três canais com volume separado (voz, efeitos, música) e um quarto de ambiente; o som nunca é o único canal (WCAG 1.1.1, 1.2); sem buzina, alarme, tique-taque ou som de erro "murcho" em nenhum nível (`benchmarks/duolingo/03-estilo.md §6`).

### 3.4 Tamanho e espaço (`tam.*`) · acesso

| id | Degraus | Padrão | Base |
|---|---|---|---|
| `tam.texto` | 100 · 125 · 150 · 200 · 300% | **100%** (ou o do sistema) | WCAG 1.4.4 (200%), 1.4.10 (reflow em 320 px) |
| `tam.alvo_minimo` | 48 · 56 · 64 · 80 · 96 · 128 px | **64** anos iniciais, **56** anos finais, **48** médio `[ASSUMIDO]` | WCAG 2.5.5 (44 px), 2.5.8 (24 px); `[VUOO]` 64 px para criança |
| `tam.espaco_entre_alvos` | 8 · 16 · 24 · 32 px | **16** | `acs.dim.motor` `[A PESQUISAR]` |
| `tam.densidade` | compacta · padrão · arejada · um item por tela | **padrão** | — |
| `tam.largura_linha` | 30 · 40 · 60 caracteres | **40** anos iniciais, **60** demais | `[VUOO]` R12 |
| `tam.foco` | anel de 2 · 3 · 4 · 6 px | **3** | WCAG 2.4.7, 2.4.13 |
| `tam.ampliacao_conteudo` | lupa desligada · 1,5× · 2× · 3× | desligada | baixa visão |

### 3.5 Texto e linguagem (`txt.*`)

| id | Tipo | Valores | Padrão | Base |
|---|---|---|---|---|
| `txt.familia` | escolha/acesso | marca · alta legibilidade (Atkinson Hyperlegible) · alfabetização (Andika, "a" e "g" escolares) · fonte do sistema | **alfabetização** nos anos iniciais, **marca** nos demais `[A CONFIRMAR]` | `[VUOO]` §6; fontes "para dislexia" sem evidência |
| `txt.caixa` | acesso | normal · caixa alta (letra bastão) | **caixa alta** no 1º ano, configurável | `[VUOO]` R10 |
| `txt.espaco_letras` | acesso | 0 · +0,03 · +0,12 em | **+0,03 em** | WCAG 1.4.12 |
| `txt.espaco_palavras` | acesso | 0 · +0,16 em | 0 | WCAG 1.4.12 |
| `txt.entrelinha` | acesso | 1,4 · 1,5 · 1,8 · 2,0 | **1,5** | WCAG 1.4.12 |
| `txt.nivel_linguagem` | acesso | padrão · simples · leitura fácil · pictográfico com texto mínimo | **padrão** | ISO 24495-1, Inclusion Europe; `acs.dim.cognitive-accessibility` `[A PESQUISAR]` |
| `txt.frases_por_instrucao` | acesso | livre · 2 · 1 | **2** | `[VUOO]` R23 |
| `txt.destaque_leitura` | acesso | desligado · palavra a palavra sincronizado com a voz | desligado | — |
| `txt.libras` | acesso | desligada · vídeo nas instruções · vídeo em toda fala | desligada | Lei 10.436/2002, `acs.br.libras` `[A PESQUISAR]` |
| `txt.pictogramas` | acesso | só ícones de navegação · pictograma em toda instrução · pictogramas do AEE do aluno | **pictograma em toda instrução** nos anos iniciais | `acs.at.aac` `[A PESQUISAR]` |
| `txt.descricao_imagens` | acesso | texto alternativo · + audiodescrição | texto alternativo sempre | WCAG 1.1.1 |

Sem itálico, sem texto justificado, sem texto sobre imagem, em qualquer configuração.

### 3.6 Densidade e complexidade visual (`den.*`) · estímulo

| id | 0 Mínimo | 1 Calmo | 2 Moderado | 3 Expressivo | 4 Máximo |
|---|---|---|---|---|---|
| `den.elementos` | só a tarefa e os controles fixos | + um apoio (personagem ou dica) | **tarefa, apoio, progresso** | + contadores e decoração | tudo visível |
| `den.ilustracao` | nenhuma | só nas bordas | **plena nas transições, de borda nas atividades** | plena em todo lugar | plena e animada |
| `den.placar` (contadores, sequência, moedas) | oculto | oculto | **só progresso da atividade** | progresso + conquistas | tudo |
| `den.modo_foco` | ligado: o que não é a tarefa some | esmaece o resto a 40% | **desligado** | desligado | desligado |
| `den.decoracao` | nenhuma | nenhuma | discreta | rica | rica e animada |

**Fronteira:** número de alternativas, tamanho do enunciado e dificuldade são **parâmetros pedagógicos**, não de estilo. Mudar o que é medido é modificação, não acomodação (`acs.adapt.accommodation-vs-modification` `[A PESQUISAR]`), e fica com o domínio de adaptação (`adp.adapt.adaptive-learning-systems`).

### 3.7 Tempo e ritmo (`tmp.*`) · acesso

| id | Valores | Padrão | Base |
|---|---|---|---|
| `tmp.limite` | sem limite · ×10 · ×3 · ×1,5 · ×1 | **sem cronômetro visível**; jogos com tempo começam em ×1 `[A CONFIRMAR]` | WCAG 2.2.1 (ajustável até ×10) |
| `tmp.velocidade_jogo` | 50% a 150%, passos de 10% | **100%** | Game Accessibility Guidelines `[A PESQUISAR]` |
| `tmp.avanco_automatico` | desligado · após 3 s · após 6 s | **desligado** | — |
| `tmp.feedback_fica` | até o toque · 3 s · 6 s | **até o toque** | — |
| `tmp.lembrete_pausa` | desligado · 10 · 15 · 20 min | **20 min** `[ASSUMIDO]` | — |
| `tmp.contagem_regressiva_visivel` | desligada · ligada | **desligada** | `[VUOO]` invariante "sem contagem regressiva" |

### 3.8 Entrada e interação (`ent.*`) · acesso

| id | Valores | Padrão | Base |
|---|---|---|---|
| `ent.modalidade` | toque · mouse · teclado · 1 acionador · 2 acionadores · varredura · voz · olhar | detectada pelo aparelho | `acs.at.alternative-access` `[A PESQUISAR]` |
| `ent.arrastar` | arrastar · tocar e tocar | **as duas aceitas** | WCAG 2.5.7 |
| `ent.permanencia` (tempo mínimo de toque) | 0 · 300 · 600 · 1000 ms | **0** | tremor |
| `ent.ignorar_repeticao` | 0 · 300 · 800 ms | **300 ms** | toques involuntários |
| `ent.aceitar_na_soltura` | sempre | sempre | WCAG 2.5.2 |
| `ent.confirmacao` | resposta direta · tocar e confirmar | **resposta direta** | — |
| `ent.desfazer` | sempre disponível antes de confirmar | sempre | — |
| `ent.varredura_velocidade` | 0,5 a 5 s por item; automática ou passo a passo | 1,5 s, automática | — |
| `ent.gestos` | só toque simples · gestos complexos com alternativa | **só toque simples** na moldura | WCAG 2.5.1 |

### 3.9 Personagem e feedback (`per.*`, `fb.*`)

| id | 0 Mínimo | 1 Calmo | 2 Moderado | 3 Expressivo | 4 Máximo |
|---|---|---|---|---|---|
| `per.presenca` | oculto | sob demanda (botão) | **canto, presente** | presente e reage | protagonista, atravessa a tela |
| `per.expressividade` | expressão neutra fixa | 3 expressões, troca lenta | **5 expressões** | exagero cartunesco | achatar e esticar, troca rápida |
| `per.fala` | desligada (só texto) | uma frase curta | **frase curta + voz** | fala com variação | fala com variação e bordões |
| `fb.celebracao` | selo estático | selo com brilho único | **selo + animação curta** | festa | festa + tela cheia + fanfarra |
| `fb.erro` | texto informativo | + ícone | **+ personagem curioso** | + personagem curioso animado | igual ao 3: **o erro não escala** |

| id | Tipo | Valores | Padrão |
|---|---|---|---|
| `per.humor` | escolha | literal · pastelão físico · humor verbal leve | **pastelão físico** |
| `fb.tipo` | escolha | só retorno de competência (o alvo reage) · + descrição verbal | **+ descrição verbal** |

**Regras do personagem (candidatas a invariante):** nunca sarcasmo, ironia, ameaça ou tristeza como alavanca; reação ao erro é curiosidade, nunca decepção; personalidade estável e literal (`benchmarks/duolingo/03-estilo.md §4` e `§7`; `05-riscos-educacao-especial.md`).

### 3.10 Aparência e identidade (`apa.*`) · escolha

| id | Valores | Padrão |
|---|---|---|
| `apa.estetica` | lúdica (anos iniciais) · jovem (anos finais) · sóbria (médio) · neutra mínima | **pela etapa escolar**, sempre trocável pelo aluno |
| `apa.tema_interesse` | espaço, natureza, esporte, música, cidade, fantasia… `[A CONFIRMAR]` | escolhido no primeiro uso |
| `apa.avatar` | galeria diversa: tons de pele, cabelo, óculos, aparelho auditivo, cadeira de rodas, abafador de ruído | escolhido no primeiro uso |
| `apa.mascote_visual` | personagem infantil · versão jovem · só ícone | pela estética |

A estética muda forma, proporção, ilustração e vocabulário visual. **Não muda** tamanho, contraste, tempo ou nível de linguagem, que são eixos de acesso.

### 3.11 Previsibilidade e estrutura (`pre.*`) · acesso

| id | Valores | Padrão |
|---|---|---|
| `pre.agenda` (plano da sessão visível) | desligada · ligada | **ligada** nos anos iniciais |
| `pre.aviso_transicao` | desligado · anúncio 3 s antes · anúncio + confirmação | **anúncio 3 s antes** |
| `pre.novidade` | elemento novo aparece direto · com apresentação curta · só depois de aceito | **com apresentação curta** |
| `pre.posicoes_fixas` | Pausar, Ouvir e Ajustes sempre no mesmo lugar | **invariante** |
| `pre.surpresas` (eventos aleatórios de interface) | desligadas · ligadas | **desligadas** `[A CONFIRMAR]`; recompensa aleatória fica fora em qualquer caso (`gam.motiv.*` `[A PESQUISAR]`) |

---

## 4. Os extremos, descritos inteiros

Para desenhar o extremo, é preciso vê-lo como uma experiência, não como uma lista de valores. Os quatro cantos abaixo são **obrigatórios** em toda tela (ver §9).

### 4.1 Mínimo (todos os eixos de estímulo em 0)
A tela mostra só a tarefa, os três controles fixos e o texto da instrução. Fundo liso em tom de papel, uma única cor codificada (sempre com forma), nenhum personagem visível (chamável pelo botão de ajuda). Nada se move sem ação do aluno; uma resposta muda de estado instantaneamente, com contorno e ícone. Nenhum som além da fala, que só toca se pedida ou se a leitura automática estiver ligada. Fim de atividade: um selo estático e a frase "Atividade feita."

### 4.2 Moderado (padrão)
Fundo com ilustração suave nas bordas, personagem no canto com respiração leve, uma cor forte na ação principal. Transições de 250 ms com deslize curto. Acerto com pulso e uma nota; erro com contorno, ícone e personagem curioso, sem som de "erro". Música só no mapa. Fim de atividade com animação curta e até 12 partículas.

### 4.3 Máximo (todos os eixos de estímulo em 4)
Cenário vivo e animado, personagem que atravessa a tela e reage com exagero, paleta de seção saturada, música contínua, efeitos com graves, háptica rítmica, celebração de tela cheia com confete e fanfarra, sequência de acertos com rebote e tremor leve de tela. **Continua valendo:** sem flash acima de 3/s, sem ameaça, erro igual ao nível 3, Pausar e "Calma" sempre a um toque.

### 4.4 Acesso extremo (eixos de acesso no topo)
Texto a 300% com reflow para uma coluna, alvos de 128 px com 32 px entre eles, contraste máximo, um item por tela, linguagem fácil com pictogramas, leitura automática de tudo com destaque palavra a palavra, sem limite de tempo, entrada por varredura com 3 s por item. Combina com qualquer nível de estímulo.

### 4.5 Esboço da mesma tela nos quatro cantos

Tela de atividade de escolha, celular em retrato:

```
MÍNIMO                                MODERADO (padrão)
┌──────────────────────────────┐      ┌──────────────────────────────┐
│ [II]                    [◁))]│      │ [II]  ■■■□□ 3 de 5     [◁))]│
│                              │      │ ~ ~ ilustração de borda ~ ~ │
│ Qual é a metade de 8?        │      │ Qual é a metade de 8?        │
│                              │      │                              │
│  ┌──────┐  ┌──────┐          │      │  ┌──────┐  ┌──────┐          │
│  │  2   │  │  4   │          │      │  │  2   │  │  4   │          │
│  └──────┘  └──────┘          │      │  └──────┘  └──────┘          │
│  ┌──────┐  ┌──────┐          │      │  ┌──────┐  ┌──────┐          │
│  │  6   │  │  16  │          │      │  │  6   │  │  16  │   (•‿•)  │
│  └──────┘  └──────┘          │      │  └──────┘  └──────┘   persona│
│ [⚙]                          │      │ [⚙]          [ VERIFICAR ]  │
└──────────────────────────────┘      └──────────────────────────────┘
 sem progresso, sem personagem,        progresso, personagem em
 resposta direta                       repouso, ação principal colorida

MÁXIMO                                ACESSO EXTREMO (texto 300%)
┌──────────────────────────────┐      ┌──────────────────────────────┐
│ [II] ★12 🔥5 ■■■□□      [◁))]│      │ [II]                    [◁))]│
│ ✦  cenário animado  ✦  ☁  ✦ │      │                              │
│ Qual é a metade de 8?        │      │  METADE                      │
│   \(^o^)/  personagem grande │      │  DE 8?                       │
│  ┌──────┐  ┌──────┐          │      │  [🖼 pictograma]              │
│  │  2   │  │  4   │ ✦        │      │ ┌──────────────────────────┐ │
│  └──────┘  └──────┘          │      │ │           4              │ │
│  ┌──────┐  ┌──────┐   ✦      │      │ └──────────────────────────┘ │
│  │  6   │  │  16  │          │      │        ▼ próximo: 2 de 4     │
│  └──────┘  └──────┘          │      │ [◀ anterior]   [ escolher ]  │
│ [⚙]   ♪   [ VERIFICAR!! ]    │      │ [⚙]                          │
└──────────────────────────────┘      └──────────────────────────────┘
 placar completo, cenário vivo,        uma alternativa por vez, lida em
 música, celebração de tela cheia      voz alta, varredura ou toque
```

Os controles fixos (Pausar em cima à esquerda, Ouvir em cima à direita, Ajustes embaixo à esquerda) não mudam de lugar em nenhum canto. O botão Calma (§5) também é fixo e ainda não está desenhado. As posições exatas são `[A CONFIRMAR]` (A-05); a regra de que não mudam é invariante.

---

## 5. Limites invioláveis

Nenhum preset, ajuste manual, trava de professor ou ação de IA ultrapassa estes limites. São candidatos a regra de negócio (`RN-nn`) quando o produto chegar a essa etapa.

| # | Limite | Base |
|---|---|---|
| L-01 | No máximo 3 flashes por segundo; sem padrões listrados ou vermelho saturado piscando | WCAG 2.3.1 |
| L-02 | Texto ≥ 4,5:1 e componentes ≥ 3:1 em **toda** combinação de tema, saturação e visão de cor | WCAG 1.4.3, 1.4.11 |
| L-03 | Cor nunca é o único código | WCAG 1.4.1 |
| L-04 | Pausar, Ouvir, Ajustes e **Calma** sempre visíveis, na mesma posição | `[VUOO]` R22, R24 |
| L-05 | Todo laço de mais de 5 s é pausável | WCAG 2.2.2 |
| L-06 | Erro nunca é punitivo: sem som de alarme, sem tremor, sem tristeza do personagem, sem sarcasmo | benchmark §4, §6, §7 |
| L-07 | Estímulos de medida não mudam por estilo, preset ou IA | `[VUOO D-20]` |
| L-08 | A IA nunca reduz um parâmetro de acesso nem aumenta estímulo acima do teto definido pelo aluno ou pelo professor | §8 |
| L-09 | Toda mudança automática é anunciada e desfeita com um toque | §8 |
| L-10 | Alvos nunca abaixo de 44 px, espaçamento nunca abaixo de 8 px | WCAG 2.5.5 |

### O botão Calma
Um controle fixo que, com **um toque**, leva todos os eixos de estímulo a 0 imediatamente, inclusive no meio de uma atividade, sem perder o progresso. Um segundo toque volta ao que estava. É a saída de emergência que torna seguro ter o máximo disponível. O uso do botão é um sinal para a IA (§8), nunca um registro exibido como problema.

---

## 6. Presets

### 6.1 Duas camadas: uma base e vários complementos
- **Base de estímulo** (escolhe-se **uma**): define o nível dos eixos de estímulo.
- **Complementos de acesso e de escolha** (combinam-se **vários**): definem valores, pisos ou tetos de parâmetros específicos.

Assim, "Vibrante + Leitura apoiada + Toque fácil" é uma combinação válida, e o número de experiências possíveis cresce sem que cada uma precise ser desenhada à mão.

### 6.2 Bases de estímulo

| Eixo | Mínimo | Calmo | **Moderado** | Foco | Vibrante | Máximo |
|---|---|---|---|---|---|---|
| `mov.intensidade` | 0 | 1 | **2** | 1 | 3 | 4 |
| `cor.saturacao` | 0,5 | 0,5 | **0,8** | 0,8 | 1,0 | 1,15 |
| `cor.fundo` | liso | liso | **suave** | liso | pleno | animado |
| `som.efeitos` | 0 | 1 | **2** | 1 | 3 | 4 |
| `som.musica` | 0 | 0 | **2** | 0 | 3 | 4 |
| `den.elementos` | 0 | 1 | **2** | 0 | 3 | 4 |
| `den.modo_foco` | ligado | esmaece | **desligado** | ligado | desligado | desligado |
| `per.presenca` | 0 | 1 | **2** | 1 | 3 | 4 |
| `fb.celebracao` | 0 | 1 | **2** | 1 | 3 | 4 |
| `hap.intensidade` | 0 | 1 | **2** | 1 | 3 | 4 |
| Para quem tende a servir | sobrecarga sensorial intensa, crise | quem prefere pouco estímulo | ponto de partida | quem se distrai com o entorno, mas gosta de cor | quem busca estímulo | quem busca muito estímulo, recompensa forte |

"Para quem tende a servir" orienta o design e a IA. **Não aparece na tela do aluno.**

### 6.3 Complementos

| Complemento | O que fixa (valor, piso ou teto) |
|---|---|
| **Alto contraste** | `cor.contraste` = reforçado; bordas de alvo 3 px; `cor.fundo` ≤ liso |
| **Contraste máximo** | `cor.contraste` = máximo; `cor.saturacao` ≤ 0,5; `tam.foco` ≥ 4 px |
| **Cores sem confusão** (3 variantes) | `cor.visao_de_cor` = protanopia, deuteranopia ou tritanopia |
| **Monocromático** | `cor.visao_de_cor` = monocromática; codificação só por forma, padrão e texto |
| **Noturno** | `cor.tema` = escuro; `cor.brilho_maximo` = branco quebrado; `som.*` −6 dB; `hap` ≤ 1 |
| **Visão ampliada** | `tam.texto` ≥ 200%; `tam.alvo_minimo` ≥ 80; `tam.densidade` ≥ arejada; `tam.foco` ≥ 4 |
| **Leitor de tela** | ordem linear; `ent.gestos` = toque simples; `txt.descricao_imagens` = + audiodescrição; `mov` ≤ 1; nada que dependa só de posição visual |
| **Leitura apoiada** | `txt.familia` = alta legibilidade; `txt.espaco_letras` = +0,12; `txt.entrelinha` ≥ 1,8; `som.leitura_automatica` = instruções; `txt.destaque_leitura` = ligado; `tam.largura_linha` ≤ 40 |
| **Leitura fácil** | `txt.nivel_linguagem` = leitura fácil; `txt.frases_por_instrucao` = 1; `txt.pictogramas` = em toda instrução |
| **Pictogramas do AEE** | `txt.pictogramas` = do aluno; `txt.nivel_linguagem` = pictográfico |
| **Libras** | `txt.libras` = toda fala; `som.legendas` = ligadas; `per.presenca` ≥ 2 se houver personagem sinalizante `[A CONFIRMAR]` |
| **Sem som** | `som.indicador_visual` = ligado; `som.legendas` = ligadas; `hap.substitui_som` = ligado; nenhuma informação só sonora |
| **Ouvir tudo** | `som.leitura_automatica` = tudo; `txt.destaque_leitura` = ligado |
| **Toque fácil** | `tam.alvo_minimo` ≥ 80; `tam.espaco_entre_alvos` ≥ 24; `ent.permanencia` = 300; `ent.ignorar_repeticao` = 800; `ent.arrastar` = tocar e tocar; `ent.confirmacao` = tocar e confirmar |
| **Acionador e varredura** | `ent.modalidade` = varredura; `tam.densidade` ≥ arejada; `tmp.limite` = sem limite; `mov` ≤ 2 no foco da varredura |
| **Tempo livre** | `tmp.limite` = sem limite; `tmp.avanco_automatico` = desligado; `tmp.feedback_fica` = até o toque; `tmp.velocidade_jogo` ≤ 80% |
| **Previsível** | `pre.agenda` = ligada; `pre.aviso_transicao` = anúncio + confirmação; `pre.novidade` = só depois de aceito; `pre.surpresas` = desligadas |
| **Sem personagem** | `per.presenca` = 0; feedback por ícone e texto |
| **Estética jovem / sóbria / neutra** | `apa.estetica` correspondente |

São 18 complementos (20 contando as variantes de cor) sobre 6 bases. Tudo é ponto de partida: o aluno ajusta em cima.

### 6.4 Regras de combinação

1. **Invariantes (§5) vencem tudo.**
2. **Trava do professor** vence o aluno. O aluno vê o cadeado e uma frase simples ("Seu professor escolheu este tamanho").
3. **Ajuste manual do aluno** vence presets.
4. **Complemento** vence a base no parâmetro que ele toca.
5. **Entre dois complementos:** em parâmetro de **estímulo**, vence o valor **menor**; em parâmetro de **acesso** (tamanho, contraste, tempo, tolerância), vence o **mais generoso**.
6. **Combinação incompatível** (por exemplo, Leitor de tela com arrastar obrigatório) é resolvida automaticamente pela alternativa acessível, com aviso.
7. **Configurações do sistema operacional** só definem **valores iniciais**: menos movimento → base Calmo; mais contraste → Alto contraste; fonte maior → `tam.texto` correspondente; leitor de tela ativo → complemento Leitor de tela.

Ordem de resolução, de cima para baixo: invariantes → travas → ajustes do aluno → complementos → base → sistema operacional → padrão do produto.

### 6.5 Personalização: "Do meu jeito"
- Prévia ao vivo de cada ajuste, com som (`[VUOO]` R39).
- Ajuste por eixo, com uma barra de 5 posições para estímulo e degraus para acesso; detalhe por parâmetro numa camada "mais opções".
- **Salvar como meu preset**, com nome e ícone escolhidos pelo aluno; até 3 presets próprios `[ASSUMIDO]`.
- Troca rápida de preset sem sair da atividade (por exemplo, de Vibrante para Calmo depois do intervalo).
- O professor pode criar presets para a turma ou para um aluno e compartilhá-los.
- "Voltar ao padrão" sempre disponível, com confirmação.
- A própria tela de ajustes sempre aparece com acesso no nível do aluno e estímulo no máximo em 1: ninguém precisa enfrentar o máximo para conseguir sair dele.

### 6.6 Primeiro uso: calibração em forma de jogo
Quatro a seis perguntas curtas, cada uma com prévia: "Assim está bom?" para tamanho, movimento, som e cor, e a escolha de estética, tema e avatar. Duração alvo menor que 2 minutos `[ASSUMIDO]`, pulável (cai no padrão moderado ou nos valores do sistema). Refazível a qualquer momento. Mostrar 4 bases e "mais opções", não as 6 bases e 18 complementos de uma vez, para evitar fadiga de escolha.

---

## 7. Quem pode mudar o quê

| Ator | Eixos de estímulo | Eixos de acesso | Escolha | Travas |
|---|---|---|---|---|
| Aluno | sim | sim (exceto se travado) | sim | não |
| Professor | sim, por aluno ou turma | sim | sugere | sim, com motivo |
| Família | sugere `[A CONFIRMAR]` | sugere | não | não |
| Sistema operacional | valor inicial | valor inicial | tema | não |
| IA (fase posterior) | dentro do envelope (§8) | só para mais apoio, com aviso | sugere | nunca |

**Trava** precisa de motivo registrado (por exemplo, "combinado no PEI") e prazo de revisão `[ASSUMIDO]`. Travar estímulo no máximo não é permitido: travar serve para proteger, não para impor estímulo.

---

## 8. Acionamento pela IA (fase posterior)

A parametrização é o que torna a IA possível: ela não "redesenha" telas, ela **move parâmetros** dentro de um envelope. O conceito de adaptação e seus limites estão em `adp.adapt.adaptive-learning-systems` e `acs.adapt.algorithmic-adaptation-and-autonomy` `[A PESQUISAR]`.

### 8.1 Níveis de autonomia

| Nível | Comportamento | Padrão |
|---|---|---|
| 0 | Desligada | — |
| 1 | Observa e **sugere** ao aluno ("Quer deixar mais calmo?") | **padrão inicial** `[A CONFIRMAR]` |
| 2 | **Aplica temporariamente** com aviso e desfazer de um toque | só com autorização do professor |
| 3 | Aplica e **aprende a preferência**, propondo salvar como preset | só com autorização do professor e assentimento do aluno |

### 8.2 Envelope
- O aluno ou o professor definem um **teto** e um **piso** por eixo de estímulo. A IA se move só entre eles.
- Em eixos de acesso, a IA **só aumenta** o apoio (L-08).
- Uma mudança por vez, um eixo por vez, **só entre atividades**. A exceção é o botão Calma, que é do aluno.
- Nada muda durante item de avaliação (L-07).

### 8.3 Sinais candidatos e ações permitidas

| Sinal | Hipótese | Ação permitida | Nunca |
|---|---|---|---|
| Botão Calma usado | sobrecarga | sugerir base mais baixa para as próximas atividades | registrar como "crise" para o professor sem contexto |
| Saída logo após celebração | celebração excessiva | sugerir reduzir `fb.celebracao` | — |
| Toques fora do alvo repetidos | alvo pequeno, tremor | sugerir Toque fácil ou alvo maior | reduzir alvo |
| Reescutas frequentes, tempo longo na instrução | leitura difícil | sugerir Leitura apoiada ou Ouvir tudo | baixar o nível pedagógico |
| Aparelho no mudo, volume zero | ambiente sem som | sugerir Sem som | — |
| Ajustes manuais repetidos no mesmo sentido | preferência estável | propor salvar como preset | aplicar sem perguntar |
| Inatividade longa no meio da atividade | distração ou cansaço | sugerir pausa | aumentar estímulo para "prender a atenção" acima do teto |
| Horário noturno | uso noturno | sugerir Noturno | — |

**Fora por padrão:** câmera, microfone contínuo e inferência de emoção, por serem dado sensível de criança e adolescente (`psg.legal.lgpd-children`, `psg.consent.child-assent`). Se entrarem, é por decisão separada.

### 8.4 O que a IA não faz
- Não infere nem armazena diagnóstico. A configuração é **preferência**, não rótulo.
- Não usa presets como indicador de deficiência em relatórios para o professor ou o gestor.
- Não explica a mudança por perfil clínico ("como você tem TDAH…"), só pela experiência ("Você apertou Calma; quer começar a próxima atividade mais calma?").

### 8.5 Dados
O perfil de configuração pode revelar deficiência: é tratado como dado pessoal potencialmente sensível, com minimização e privacidade desde a concepção (`psg.access.minimization-and-privacy-by-design`). Guardado no aparelho por padrão e sincronizado só o necessário `[A CONFIRMAR]`. Formato portável entre sistemas: `acs.std.accessforall-iso-24751` e `acs.adapt.preference-profiles` `[A PESQUISAR]`. Em atividades com medida, a configuração ativa entra como covariável da sessão `[VUOO]`.

---

## 9. Implicações para arte, estilo, wireframes e componentes

### 9.1 A cadeia
```
perfil do aluno (JSON) → resolvedor (§6.4) → tokens → componentes, ilustração, animação, som
```
Nenhuma peça de arte referencia valor fixo de cor, duração, volume ou tamanho: referencia **token**. Os tokens seguem o formato W3C Design Tokens `[VUOO P32]`.

### 9.2 Ilustração
- Vetorial, com cores ligadas a tokens (SVG com variáveis), para que saturação, tema, contraste e visão de cor se apliquem sem redesenhar.
- **Em camadas nomeadas**, cada uma ligada a um nível de `den.ilustracao`: `fundo`, `cenario`, `decoracao`, `personagem`, `tarefa`, `foco`. No nível 0 só `tarefa` e `foco` aparecem.
- Forma arredondada, mínimo de detalhe, silhueta legível em escala de cinza (teste obrigatório no nível monocromático).
- Uma família de ilustração por estética (lúdica, jovem, sóbria), com a mesma gramática de camadas.

### 9.3 Animação
- Máquina de estados (Rive ou equivalente `[A CONFIRMAR]`) com entradas numéricas: `intensidade` (0–4), `velocidade`, `repouso` (ligado/desligado), `particulas`.
- Para cada animação-chave (acerto, fim de atividade, conquista, entrada de personagem), o animador entrega **ao menos três versões**: calma (1), moderada (2) e máxima (4). O nível 0 é uma **pose estática** desenhada, não um quadro congelado ao acaso. O nível 3 pode ser interpolado.
- Erro tem uma só versão, igual em todos os níveis (L-06).

### 9.4 Som
- Cada som em **três variantes** (suave, padrão, brilhante) e por pacote sonoro, normalizado, com metadado de canal.
- Graves e ataques rápidos marcados no metadado, para que o resolvedor os filtre nos níveis 0 e 1.

### 9.5 Wireframes
Cada tela é entregue em **cinco quadros obrigatórios**:
1. Moderado em 360 px.
2. Mínimo.
3. Máximo.
4. Acesso extremo (texto 300%, alvo 128 px, um item por tela).
5. Ordem de leitura linear para leitor de tela e varredura.

Mais o tablet no moderado. Uma tela só é aprovada quando os cinco funcionam.

### 9.6 Componentes
Cada componente tem uma ficha com: estados (padrão, pressionado, foco, desabilitado, carregando, feito, erro), **parâmetros que o afetam** e o comportamento em cada canto. Exemplo resumido:

| Componente | Parâmetros | Mínimo | Moderado | Máximo | Acesso extremo |
|---|---|---|---|---|---|
| Botão de alternativa | `tam.alvo_minimo`, `cor.*`, `mov.feedback_resposta`, `som.feedback`, `ent.*` | contorno + ícone, sem som | pulso + nota | pulso, rebote, partículas | 128 px, um por tela, lido em voz alta |
| Barra de progresso | `den.placar`, `mov.*` | oculta | trilho com preenchimento | com marcos animados | texto "2 de 4" lido |

### 9.7 Checklist de entrega de arte
- [ ] Nenhum valor fixo; tudo em token.
- [ ] Camadas nomeadas e testadas no nível 0.
- [ ] Silhueta legível em escala de cinza.
- [ ] Três versões das animações-chave e pose estática.
- [ ] Nenhum flash acima de 3/s (ferramenta de análise de fotossensibilidade).
- [ ] Sons em três variantes, normalizados.
- [ ] Contraste validado por script em todas as combinações de tema, saturação e visão de cor.
- [ ] Cinco quadros de wireframe aprovados.

---

## 10. Arquitetura do perfil (esboço, não é ADR)

Exemplo de perfil resolvido. A forma definitiva sai do primeiro ADR de `padroes/` deste produto e da pesquisa de `acs.std.accessforall-iso-24751`.

```json
{
  "versao_esquema": "0.1",
  "base": "vibrante",
  "complementos": ["leitura-apoiada", "toque-facil"],
  "ajustes_aluno": { "som.musica": 1, "cor.destaque_pessoal": "laranja" },
  "travas": [
    { "id": "tam.alvo_minimo", "valor": 96, "por": "professor", "motivo": "combinado no PEI", "revisar_em": "2027-03-01" }
  ],
  "ia": { "nivel": 1, "envelope": { "mov.intensidade": [1, 3], "som.efeitos": [0, 3] } },
  "origem_inicial": { "prefers_reduced_motion": false, "fonte_sistema": 1.0 }
}
```

O resolvedor aplica §6.4 e gera os tokens; o resultado é determinístico e pode ser recalculado offline.

---

## 11. Validação

| O quê | Como |
|---|---|
| Contraste e cor | Script automático sobre todas as combinações de tema × saturação × visão de cor × contraste, falhando a publicação se algum par violar L-02 |
| Explosão de combinações | Teste combinatório aos pares sobre bases × complementos, mais os quatro cantos de §4 em captura visual para regressão |
| Fotossensibilidade | Ferramenta de análise sobre toda animação no nível 4 |
| Uso real | Co-design e testes com alunos de cada etapa e com usuários de tecnologia assistiva (`acs.asmt.user-testing-with-at`, `acs.part.inclusive-and-participatory-design` `[A PESQUISAR]`) |
| Métricas de produto | Distribuição de bases escolhidas; uso do botão Calma; ajustes desfeitos logo depois (sinal de padrão errado); abandono por preset; tempo da calibração inicial |

Se a maioria dos alunos sai do moderado na mesma direção, o padrão está errado e deve mudar.

---

## 12. Riscos

| Risco | Mitigação |
|---|---|
| Custo de arte e de testes cresce com o número de níveis | Três versões entregues à mão por animação-chave, o resto interpolado; tokens e camadas em vez de variantes desenhadas; teste aos pares |
| Fadiga de escolha | Calibração curta; 4 bases visíveis e o resto em "mais opções"; IA no nível 1 sugere |
| Estigma ("o preset dos que têm problema") | Nomes de experiência; presets também para quem só gosta (Vibrante, Noturno, Estética jovem); nunca mostrar o preset de um aluno para outros |
| O máximo prejudica quem não sabe pedir menos | Padrão moderado; botão Calma; professor pode pôr teto |
| IA paternalista ou invasiva | Nível 1 por padrão; envelope; L-08 e L-09; sem câmera por padrão |
| Inconsistência visual entre combinações | Uma gramática por estética; tokens; os quatro cantos aprovados em toda tela |
| Configuração altera o que é medido | L-07; configuração registrada como covariável |

---

## 13. Decisões em aberto

| # | Pergunta | Quem responde |
|---|---|---|
| A-01 | ~~Nome e slug do produto~~ | resolvido: VUOO (D-30) |
| A-02 | Padrões por etapa: alvo (64/56/48), fonte, leitura automática, agenda | usuário + co-design |
| A-03 | Música no padrão moderado: só no mapa (proposta) ou desligada | usuário |
| A-04 | Quais 4 bases aparecem na calibração inicial | usuário + co-design |
| A-05 | Posição dos controles fixos e do botão Calma | design |
| A-06 | Nível de autonomia inicial da IA (proposta: 1) e quem autoriza os níveis 2 e 3 | usuário + jurídico |
| A-07 | Família pode sugerir ajustes? | usuário |
| A-08 | ~~Stack e ferramenta de animação~~ | resolvido: D-34, D-36, D-37 |
| A-09 | Haverá atividades com medida? Se sim, quem define o protocolo protegido | usuário |
| A-10 | Orçamento de produção das variantes | adiado para depois do primeiro ciclo (D-32) |
| A-11 | Recompensa aleatória e eventos-surpresa: fora por princípio ou por configuração | usuário, depois de `gam.*` |
| A-12 | Paleta, tipografia e personagem da marca | do zero (D-31); primeira frente de design |

---

## 14. Dependências da base de conhecimento

Este documento antecipa decisões que a base ainda não sustenta. Antes de transformar qualquer item em regra (`RN-nn`) ou padrão (`ADR-nn`), estes ids precisam existir:

- **Acessibilidade** (`conhecimento/acessibilidade-educacao-especial-e-dua/`, só brief): `acs.std.wcag`, `acs.std.game-accessibility-guidelines`, `acs.dim.cognitive-accessibility`, `acs.dim.visual`, `acs.dim.auditory`, `acs.dim.motor`, `acs.at.alternative-access`, `acs.at.aac`, `acs.adapt.preference-profiles`, `acs.adapt.accommodation-vs-modification`, `acs.adapt.algorithmic-adaptation-and-autonomy`, `acs.std.accessforall-iso-24751`, `acs.br.emag-and-nbr-17225`, `acs.br.libras`.
- **Gamificação** (`conhecimento/gamificacao-e-jogos/`, só brief): `gam.motiv.intrinsic-extrinsic-and-overjustification`, `gam.evid.special-education-and-neurodivergence`, `gam.mech.points-badges-leaderboards`.
- **Já pesquisados e citados aqui:** `adp.adapt.adaptive-learning-systems`, `psg.access.minimization-and-privacy-by-design`, `psg.legal.lgpd-children`, `psg.consent.child-assent`, `lms.case.duolingo`.
- **Benchmark:** `benchmarks/duolingo/03-estilo.md` (todas as seções) e `05-riscos-educacao-especial.md`.
- **Precedente:** `produtos/vuoo-linguagem/03-linguagem.md` §5–§11 e §14, `06-especificacao-base.md` §6–§7, `05-decisoes.md` D-09, D-20.
