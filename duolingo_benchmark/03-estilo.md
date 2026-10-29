---
titulo: Estilo do Duolingo: visual, personagens, movimento, som, tom de voz
capitulo: 03
atualizado_em: 2026-10-29
marcas: "[V] fonte primária · [S] fonte secundária · [I] inferência"
nota_de_metodo: design.duolingo.com redireciona para o blog desde 2025; paleta completa e tokens vieram de extrações de terceiros (brand-atoms, shadcn DESIGN.md). Tratar hex e regras como [S] salvo indicação.
---

# 03 · Estilo

## 1. Paleta

**Cores com nome de animal** [S, extração de design.duolingo.com]:

| Grupo | Nome | Hex | Uso |
|---|---|---|---|
| Verdes | **Feather Green** | `#58CC02` | primária, marca, ação primária, sucesso, única cor permitida para preencher o Duo |
| | Mask Green | `#89E219` | só ilustração; hover no dark |
| | Tree Frog | `#58A700` | estado pressionado / "aba" inferior do botão |
| | Turtle | `#A5ED6E` | texto/borda de destaque "correto" |
| | Sea Sponge | `#D7FFB8` | chip selecionado; painel de acerto |
| Neutros | Snow | `#FFFFFF` | fundo |
| | Polar | `#F7F7F7` | superfície |
| | Swan | `#E5E5E5` | borda, divisor |
| | Hare | `#AFAFAF` | borda de botão secundário, desabilitado |
| | Wolf | `#777777` | texto secundário |
| | **Eel** | `#4B4B4B` | texto principal (**nunca preto puro**); fundo do dark mode |
| Vermelhos | **Cardinal** | `#FF4B4B` | erro, perda de ofensiva, confirmação destrutiva; nunca em áreas grandes |
| | Fire Ant | `#EA2B2B` | |
| | Crab | `#FF7878` | |
| | Flamingo | `#FFB2B2` | painel de erro |
| Amarelos/laranjas | **Bee** | `#FFC800` | aviso, conquistas, XP |
| | Lion | `#FFB100` | |
| | **Fox** | `#FF9600` | chama da ofensiva |
| | Duck | `#FBE56D` | |
| | Canary | `#FFF5D3` | |
| Azuis | **Macaw** | `#1CB0F6` | secundária, foco de input, gemas, acento no dark |
| | Whale | `#1899D6` | |
| | **Humpback** | `#2B70C9` | |
| | Narwhal | `#1453A3` | |
| | Blue Jay | `#84D8FF` | |
| | Moon Jelly | `#7AF0F2` | |
| Roxos/rosas | Beetle | `#CE82FF` | |
| | Betta | `#9069CD` | |
| | Butterfly | `#6F4EA1` | |
| | Starfish | `#FFAADE` | |

Agrupamento oficial (trecho indexado) [V]: secundárias = Macaw, Cardinal, Bee, Fox, Humpback; neutras = Eel, Wolf, Hare, Swan, Polar, Snow. "As cores centrais vêm do mascote": Wing Overlay `#43C000`, Beak Inner `#B66E28`, Beak Lower/Feet `#F49000`, Beak Upper `#FFC200`, Beak Highlight `#FFDE00`, Tongue Pink `#FFCAFF`.

**Regras** [S]: uma única cor saturada de CTA por tela; verde só em ação primária e títulos-chave, nunca como acento genérico; dark mode inverte (fundo Eel, superfície Wolf, texto Snow/Polar/Swan). Cada seção/unidade do caminho tem sua cor de banner (verde, roxo, laranja, rosa, azul) [I/S].

**Contraste WCAG** [I, calculado]: branco sobre Feather Green **2,09:1**, sobre Macaw 2,44, sobre Cardinal 3,30, sobre Fox 2,18; Bee sobre Snow 1,55; Hare sobre Snow 2,19; Wolf sobre Snow 4,48; Eel sobre Snow 8,72; Humpback sobre Snow 4,93. Rótulos de botão são 15 px bold (abaixo do limiar de "texto grande"), então **os CTAs primários, azuis e vermelhos falham AA 4,5:1 e até 3:1**. A marca confia em tamanho, caixa alta e peso [I]. Não há modo específico para daltonismo; o feedback combina cor com ícone (✓/✗), posição e som [I].

Imagens: `03-estilo-app-store-*` (5, uma cor de fundo cada), `03-estilo-abas-direcao-*`.

Fontes: https://brand-atoms.pages.dev/dist/brands/duolingo/1.0.0/markdown/brand-guide.md · https://www.shadcn.io/design/duolingo/raw · https://design.duolingo.com/identity/color (redireciona) · pesquisa/2026-10-29-estilo.md §1 e §7

## 2. Tipografia e componentes

**Feather Bold** [V/S]: fonte própria, desenhada por Krista Radoeva (Fontsmith) no rebrand da Johnson Banks (2019); formas vêm da asa da coruja ("flick" no g, junções em ponta de asa); só display (h1 64 px/700/1.05/−1,28 px; h2 48 px); não é comercializada. **DIN Next Rounded / DIN Round Pro** (Monotype) [S]: interface e corpo: heading 32/700, 19/700; body 17/500, 15/700, 13/700; caption 13/500; label caixa alta 15/700 com tracking 0,8 px. **Só pesos 500 e 700**; display ≥ 1,5× o corpo.

**Tokens de componente** [S, extração do site]: botão primário com "aba" inferior plana de 3–4 px em Tree Frog que "afunda" ao pressionar, **sem sombra difusa** (`shadow 0 4px 0`); altura 50 px; raios 8 px (chips, inputs), 12–16 px (botões, cards), 9999 px (badges); botão secundário borda 2 px Hare; input borda 2 px Swan → Macaw em foco; divisor 1 px Swan; espaçamentos 8/10/12/16/24/32/48/96; gutter 16 px. Tiles de resposta: brancos, borda Swan, mesma aba inferior [I].

**Risco na educação especial.** Fontes arredondadas e grossas são boas para leitores iniciantes [I]; para dislexia importa mais tamanho, espaçamento e letras bem diferenciadas (b/d/p/q, I/l/1, a e g de forma escolar) do que fontes "para dislexia", cuja evidência é fraca [I]; não há ajuste de tamanho no app.

Imagens: `03-estilo-tipografia-feather-bold-vs-din-next-rounded.jpg`, `03-estilo-wordmark-feather-bold.jpg`.

Fontes: https://www.creativebloq.com/news/feather-bold · https://fontsinuse.com/uses/59497/duolingo-app · https://www.monotype.com/es/node/6287 · pesquisa/2026-10-29-estilo.md §1

## 3. Linguagem de forma (shape language) e ilustração

**Regra** [V]: toda ilustração é construída a partir de **três formas**: retângulo arredondado, círculo e triângulo arredondado. Formas pontudas são "off-brand". Princípios: **rápido de produzir** (vetor), **claro** (mínimo de detalhe, silhuetas legíveis, espaço negativo branco), **divertido** (exagero, caricatura, humor), **ângulos e animação guiam o olhar**. Quantidade de formas: um gato com 6 formas é abstrato demais, com 14 está bom, com 30 é demais (`03-estilo-shape-language-gato-6-14-30-formas.png`). O estilo evoluiu de formas pontudas e cores apagadas sobre cinza (2012–2014) para arredondadas, vivas, sobre branco; a mudança começou em **2018 no Duolingo Kids** [V]. Justificativa explícita: o visual lúdico **reduz o medo de errar** [V]. Dado: ícones de habilidade **animados** prenderam mais atenção e fizeram o usuário iniciar mais lições [V].

**Construção do Duo (2018)** [V, App Store "Behind the Design"]: "mais ou menos um cilindro com asas"; asas são semicírculos atrás do corpo; pés em pílula; geometria simples e perspectiva plana para ser previsível de qualquer ângulo; **uma postura e uma expressão canônica**; antes havia só dois estados (feliz, chorando); tempo de animação e ilustração caiu drasticamente. Evolução: wordmark 2010 → coruja com rosto feito das letras d-u-o (2011) → olhos reais e bico, 3D para o iOS 7 (2012) → versão mais fofa (2014) → atual (2018); verde porque, "reza a lenda", o cofundador odiava verde [V/S]. Estilo 2D chapado, sem contorno; linha só para separar áreas de mesma cor [V/I].

**Rebrand Johnson Banks (2018–19)** [V]: logotipo desenhado a partir das formas do mascote; Feather Bold; tom de voz, cores centrais e guia de ilustração; "everyone can Duolingo".

**Risco na educação especial.** Positivo: formas arredondadas, mínimo de detalhe, silhuetas claras e espaço branco estão alinhados a recomendações de baixa carga visual [I]. Atenção: verde vivo sobre branco e telas comemorativas saturadas com partículas e flashes podem sobrecarregar hipersensibilidade visual; vermelho e verde como único código falha para daltonismo (~8% dos meninos) [I].

**Adaptações.** Modo de baixa estimulação (menos movimento, saturação menor, respeitar `prefers-reduced-motion`); código duplo cor + forma + ícone; canais de som separados [I].

Imagens: `03-estilo-shape-language-*` (12), `03-estilo-duo-*` (20), `03-estilo-app-evolucao-2012-2014-2018.png`, `03-estilo-logo-*`.

Fontes: https://blog.duolingo.com/shape-language-duolingos-art-style/ · https://apps.apple.com/us/story/id1463847719 · https://www.designweek.co.uk/issues/2-6-january-2019/duolingo-owl-receives-makeover-as-app-becomes-more-gamified · https://www.johnsonbanks.co.uk/work/duolingo · pesquisa/2026-10-29-estilo.md §2

## 4. Personagens

**Duo** [V/S]: coruja. **No app**: comemora, encoraja, aparece em marcos (fênix), fica aflito no widget. **Fora do app** (TikTok): persona "unhinged" (persegue quem não faz lição, briga com o Google Tradutor); "wholesome unhinged" na definição da comunicação; "morte" do Duo em fev/2025 com contador global de XP para "revivê-lo". Duas camadas: coach entusiasmado no produto, perseguidor ameaçador no meme; o meme vaza para o produto pelas notificações e pela percepção das crianças ("o Duo vai me pegar") [I].

**World Characters ("Project World", 2020)** [V/S]: humanos modernos "com personalidades muito peculiares"; diversidade de idade, etnia e personalidade "para que todo aprendiz se identifique com ao menos um"; **pares de contraste** geram drama; nomes iguais em todas as línguas; emprestam do Duo: formas simples, olhos grandes, pés destacados do corpo. 10 personagens com voz e 20+ visemas cada:

| Personagem | Traço | Observação |
|---|---|---|
| Lily | adolescente, introvertida, sarcasmo autoprotetor, "deadpan", cabelo roxo | a equipe perguntou "quão deadpan ela pode ser sem prejudicar o aprendizado"; Video Call com IA |
| Zari | colegial extrovertida, nota 10 | melhor amiga (oposta) de Lily |
| Bea | ambiciosa, "bastante neurótica" | contraste com Lin |
| Lin | avó de Lucy, tranquila | voz "perpetuamente divertida" em inglês, "lânguida" em japonês |
| Lucy | neta, "passado misterioso", punk | apresenta DuoRadio |
| Junior | 8 anos, filho de Eddy | |
| Eddy | trintão, pai solteiro, fitness | comemora lições perfeitas (2025) |
| Oscar | ~40, professor de arte, bigode | |
| Vikram | ex-finanças, padeiro | |
| Falstaff | urso | único animal além do Duo; Video Call |

**Vozes** [V]: casting de meses; atores gravaram em inglês; a gravação virou "blueprint" para ES/FR/DE/JA com fonetistas; ML gera qualquer frase; **coloração emocional (raiva) foi difícil** porque o modelo foi treinado em fala neutra.

**Como reagem ao erro** [V/I]: há um estado final de reação a erro; a reação é leve (surpresa, careta "sem parecer julgadora"), nunca punitiva dentro do exercício; a culpa fica nas notificações e no marketing.

**Risco na educação especial.** Sarcasmo (Lily), ameaça como humor (Duo) e tristeza do personagem como alavanca são ambíguos e potencialmente angustiantes para quem lê literalmente [I]. **Positivo:** personalidades distintas e **estáveis** (introvertida, ansiosa, extrovertida) retratadas com afeto permitem que crianças diferentes se vejam representadas [I].

**Adaptações.** Personagem com personalidade estável, previsível, literal e calorosa; erra junto e "aprende" com a criança; reage ao erro com curiosidade; humor de pastelão físico, compreensível sem pragmática verbal [I].

Imagens: `03-estilo-personagens-*` (13), `03-estilo-zari-*` (8), `03-estilo-visemas-*` (7).

Fontes: https://blog.duolingo.com/building-character/ · https://blog.duolingo.com/character-voices/ · https://blog.duolingo.com/duolingo-female-character-origin-stories · https://blog.duolingo.com/world-character-visemes · https://npr.org/2025/02/26/nx-s1-5309785/duolingo-owl-mascot-lives · https://campaignlive.com/article/duolingo-comms-head-sam-dalsimer-leads-wholesome-unhinged-strategy/1910699 · pesquisa/2026-10-29-estilo.md §2

## 5. Movimento

**Arquitetura Rive** [V]: máquina de estados com **estados de corpo** (poses de lição) e **estados de boca** em paralelo; idle = acenos, piscar, sobrancelhas; estado final de reação a acerto/erro; pipeline TTS → tempos por fonema → mapa fonema→visema → o app dispara as bocas; a fala **pára cedo se o usuário termina antes**; escolhido sobre game engine por arquivos pequenos e handoff animador→engenheiro. Esboço da máquina: IDLE → Correct Answer → Correct Anim → Reset; Incorrect Answer → Incorrect Anim → Neutral (`03-estilo-visemas-maquina-de-estados-corpo-esboco.png`).

**Video Call com Lily** [V, Rive 2025]: 8 animações de cabeça × 8 de corpo = 64+ variações de movimento neutro; artboards aninhados; expressões disparadas por evento; inclina ao ouvir, "pondera" durante latência, aperta os olhos quando confusa; arquivo final **< 1 MB**; cargo de "creative technologist".

**Marco de ofensiva** [V]: tratado como "power-up de videogame"; fênix por ser reconhecida em todas as culturas; versão com balões rejeitada; várias passagens de rough antes de refinar "ritmo e energia". **Não há durações nem easing publicados.** Cada personagem tem animação própria de acerto; interstitials de combo; ícones animados; widget com Duo progressivamente aflito [V]. Pipeline 3D experimental (Zari, 2023) [V]. Lottie não confirmado.

**Redesign das abas (fev/2026)** [V]: quatro direções (Punchy, Soft, Modular, Flat); resultado remove contêineres em favor de espaço, cabeçalhos no mesmo nível, títulos à esquerda, conjunto mínimo de estilos; engajamento subiu sem mexer em métricas de aprendizado.

**Risco e adaptações.** Máquina de estados e arquivos leves são diretamente aproveitáveis; o que muda é o conteúdo dos estados (sem tristeza, sem aflição) e a existência de um modo com menos movimento [I].

Imagens: `03-estilo-rive-*` (5), `03-estilo-visemas-*`, `03-estilo-abas-*` (11), `01-recompensas-ofensiva-marco-fenix-*`, `03-estilo-licao-gif-translate.gif`.

Fontes: https://blog.duolingo.com/world-character-visemes/ · https://rive.app/blog/duolingo-s-ai-powered-video-call-brings-lily-to-life · https://blog.duolingo.com/streak-milestone-design-animation/ · https://blog.duolingo.com/core-tabs-redesign/ · pesquisa/2026-10-29-estilo.md §3

## 6. Som

**Não existe documentação oficial** da paleta sonora nem crédito de autoria [V, por ausência]. Relatos [S]: chime ascendente "saltitante" no acerto; tom descendente "murcho" no erro; fanfarra no fim; o som de abertura do app é igual ao de acerto; o toggle "Sound effects" também desliga as vibrações; haptics "preenchem os graves" sob o som. Vagas internas mencionam sound designers para o curso de Música [S]. Extensões de terceiros separam volume de efeitos e de frases [S].

**Risco e adaptações.** Sons súbitos e sobrepostos são queixa documentada de usuários autistas [S]; canais separados (narração, efeitos, música) com opção de desligar efeitos sem perder a narração; erro com som suave e não punitivo [I].

Fontes: pesquisa/2026-10-29-estilo.md §4 · https://out-of-scope-product.beehiiv.com/p/duolingo-has-it-venmo-has-it-even-slack-has-it-your-product-doesn-t

## 7. Tom de voz e copy

**Voz oficial** (design.duolingo.com/writing, trechos indexados) [V]: **Expressive** (palavras simples para sentimentos grandes; breve; voz ativa), **Playful** (amigável, "clever em doses rápidas"; **evitar sarcasmo, presunção e secura**), **Embracing** ("seja quem for, somos seu maior torcedor"), **Worldly**. A voz é constante; o **tom muda com o estado do leitor**: em conteúdo sensível, menos exclamações; em sucesso, celebrar. Erro: preferir "Not quite correct. Try again!" a "Incorrect." A voz do Duo é a da marca.

**Processo** [V]: tom descrito internamente como "lúdico e gentilmente passivo-agressivo"; copy localizada em ~22 línguas; ferramenta **Expurrimenter** testa 2–3 strings por hipótese. Exemplos: ES, sair da lição: "¿Quieres terminar esta sesión?" → "**¡No te rindas!** ¿De verdad quieres salir?" (menos abandonos); DE, opt-in de notificação justificado por "comprovadamente ajuda" (+8%); ZH, "Unlimited Hearts" → "No heart loss on errors". Separação entre **copy testável** (instruções, botões) e **conteúdo do curso** (`03-estilo-copy-anatomia-copy-testavel-vs-conteudo.png`).

**Microcopy real** [S/V]: feedback "Nice!", "Great!", "Awesome!", "Excellent!", "A+++++! You make this look easy", "4 speaking exercises! Speak on THAT"; notificações "Hi, it's Duo! I missed you. It has been 3 days…", "Hey. It's Lily. Did you practice Greek today? Be a lot cooler if you did…", "You're falling behind!", "These reminders don't seem to be working. We'll stop sending them for now."; Video Call com Falstaff: "Always nice to talk. Though your lack of fur is alarming".

**PT-BR** [V/S]: Brasil é o 2º mercado (50 M de usuários em 2024); "usamos o humor, que está no DNA da marca"; limites: nada ofensivo, violência, drogas, religião; memes vindos do público adotados "mantendo leve"; cargo de Brazilian Portuguese Language Manager mantém guia de estilo e glossário. Exemplo de push em PT: "Hora de praticar [idioma]!".

**Risco e adaptações.** A voz oficial já pede para evitar sarcasmo; o produto para educação especial deve ir além: linguagem **literal**, frases curtas, sem ironia, sem culpa, sem ameaça de perda; humor físico; o mesmo tom estável em todos os estados [I].

Imagens: `03-estilo-copy-*` (6), `01-recompensas-notificacoes-*`, `02-gameplay-fim-de-licao-a-mais-mais-mais.png`, `02-gameplay-fim-de-licao-4-exercicios-de-fala.png`.

Fontes: https://design.duolingo.com/writing/voice · https://blog.duolingo.com/copy-testing-experiments · https://blog.duolingo.com/oi-e-o-duo-inteligencia-artificial-por-tras-do-meme/ · https://www.meioemensagem.com.br/womentowatch/analigia-martins-o-poder-do-humor-no-marketing-do-duolingo · pesquisa/2026-10-29-estilo.md §5

## 8. Anatomia das telas principais (iOS, 2025–2026)

| Tela | Elementos | Imagens |
|---|---|---|
| Home / caminho | barra superior (bandeira, chama Fox, gemas Macaw, corações Cardinal / ∞ Super); banner da unidade na cor da seção; nós em zigue-zague; baú, troféu, personagem; nav de 5–6 ícones; light e dark | `02-gameplay-caminho-*` |
| Lição | barra de progresso, X, corações; enunciado; personagem Rive + balão; tiles/imagens/teclado/microfone; CHECK | `02-gameplay-exercicio-*` |
| Feedback | painel inferior verde-claro (check, elogio) ou vermelho-claro (X, "Correct solution") | `02-gameplay-feedback-*` |
| Fim de lição | personagem, cartões XP/precisão/tempo (Bee, Feather Green, Macaw), CLAIM XP; depois missão, baú, conquista | `02-gameplay-fim-de-licao-*` |
| Liga | cabeçalho na cor da liga, escudo, lista com avatar e XP, zonas de promoção/rebaixamento | `01-recompensas-liga-*` |
| Ofensiva | chama grande, número, semana marcada, calendário mensal, Streak Goal & Protection | `01-recompensas-ofensiva-*` |
| Missões | aba Quests com três diárias, baús por nível, medidores mensal e de colecionáveis | `01-recompensas-missoes-*` |
| Loja | cartão Super/Max, My Items, Streak Freeze, Timer Boost, ofertas | `01-recompensas-loja-*` |
| Perfil | avatar customizável, estatísticas, Friend Streaks, insígnias, gráfico semanal | `02-gameplay-perfil-*`, `03-estilo-abas-*` |
| Widget | Duo por hora do dia, contador | `01-recompensas-widget-*` |

Galeria completa de 116 telas: https://screensdesign.com/apps/duolingo-language-lessons/ · mapa de 70 telas e 115 transições: https://revyl-landing.pages.dev/atlas/duolingo/report/ · kits não oficiais no Figma Community (lista em pesquisa/2026-10-29-estilo.md §8).
