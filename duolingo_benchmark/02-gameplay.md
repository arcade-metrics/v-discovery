---
titulo: Gameplay do Duolingo: lição, exercícios, caminho, adaptação, feedback
capitulo: 02
atualizado_em: 2026-10-29
marcas: "[V] fonte primária · [S] fonte secundária · [I] inferência"
---

# 02 · Gameplay

## 1. Loop da lição

**O que é.** Sequência de 2 a 18 exercícios (**tipicamente ~15**), 2 a 5 minutos, formatos alternados [S/V]. Começa fácil (reconhecer) e vai ficando difícil (montar com banco de palavras, depois digitar); oficialmente só isso é confirmado; ordem detalhada (1–3 reconhecimento, 4–7 word bank, 8–11 digitação, 12–14 misto, 15 fácil para terminar em sucesso) é análise de terceiros [S]. Exercícios de escuta começam **com texto junto do áudio** e o texto vai sumindo conforme o nível sobe [V]. Dentro de uma habilidade: nível inicial = codificação de vocabulário/gramática; nível 2 = reconhecimento; nível 3 = fala; níveis seguintes = recuperação (retrieval) [V, 2021].

**Anatomia de uma tela de exercício** [I/S]: barra de progresso arredondada no topo (verde; enche a cada item e ainda avança um pouco após erro, "nunca se sente travado"); "X" para sair à esquerda; corações/energia à direita; enunciado em uma linha ("Tap what you hear"); personagem em Rive ao lado de balão de fala; área de resposta (tiles brancos com borda cinza e "aba" inferior, imagens, teclado, microfone); botão CHECK verde 3D, cinza até haver resposta; links discretos "CAN'T LISTEN NOW" / "CAN'T SPEAK NOW".

**Feedback por item.**
- **Acerto** [S/I]: painel sobe do rodapé em verde-claro com ícone de check e elogio variável ("Nice!", "Great!", "Awesome!", "Excellent!"), chime ascendente "saltitante", haptic, botão CONTINUE verde; o personagem tem animação própria de acerto; a cada 5/10 acertos seguidos, overlay escuro "5 in a row!" / "10 in a row!" com o Duo (`02-gameplay-combo-*`).
- **Erro** [S/I]: painel vermelho-claro ("not scary red") com "X", "Correct solution:" e a resposta correta **em texto**, tom descendente descrito como "desanimador o bastante para você querer acertar a próxima, mas não tão duro a ponto de gerar ansiedade", botão GOT IT/CONTINUE em vermelho; custa 1 coração (antes) ou energia (2025); em pares, só o par errado pisca. O item (ou equivalente) **volta no fim da lição** ("Let's correct the exercises you missed!") e vai para a fila *Mistakes* do Practice Hub [V].
- **Explain My Answer** [V]: botão após qualquer resposta. Acerto: a razão curta. Erro: forma correta ao lado da incorreta + regra breve + exemplos contrastantes, calibrado para a L1 do aluno. Grátis desde 1/1/2026 em ES, FR, DE, JA, PT, IT, KO.
- **Adventures e Video Call** usam outro modelo: sem faixa vermelha; o personagem redireciona ("Oh, did you mean…?") ou o feedback vem **depois** da chamada [V].
- Toggles do usuário [V]: Sound effects, Haptic feedback, Animations, Motivational messages, Listening exercises, Friends Quests, Friend Streaks (`02-gameplay-preferencias-*`).

**Fim de lição** [S/V]: fanfarra, personagem/Duo comemorando, cartões **XP total / precisão / tempo** em cores distintas, botão CLAIM XP; "Perfect lesson!" para 0 erros; depois telas encadeadas: ofensiva, missões diárias, liga, baú, conquista; sair no meio dispara modal "você perderá o XP" com Duo preocupado. Em 2025, novas animações de fim de lição e o personagem **Eddy** substituiu o rótulo "exercício difícil" [V]. Experimento: rotular "this is a hard exercise" fez alunos passarem mais tempo, voltarem no dia seguinte e aceitarem mais exercícios difíceis ("raises the floor and the ceiling"); um **card de level-up** explicando o ganho de proficiência também aumentou retorno [V].

**Por que funciona.** Ciclo curto de esforço → feedback imediato → progresso visível; variedade de formato a cada 10–20 s ("surpresa e deleite" como requisito [S]); barra de progresso como "efeito de progresso dotado" [I]; clareza visual como requisito de aprendizagem: "um visual pouco claro leva o aprendiz a errar ou se perder, e nossa falha vira a falha do aprendiz" [V].

**Números.** "O número de lições concluídas foi o preditor mais forte de ganho de aprendizagem" (estudo citado pela empresa) [V]. ~20% das lições iniciadas não são terminadas (dado usado para justificar atualização do modelo em streaming) [V].

**Risco na educação especial.** Feedback de erro **textual** e rápido em momento de frustração; vermelho + som descendente como sinais aversivos; cascata de telas pós-lição desregula; arrastar e digitar exigem precisão motora; "repetir o erro no fim" pode fazer a lição "não acabar nunca" para quem erra muito [I].

**Adaptações.** Feedback multimodal e não textual (voz + animação + ícone); erro em cor neutra; uma tela final; alvos ≥ 48–64 px, tocar em vez de arrastar como alternativa, sem limite de tempo por item; teto de itens extras [I].

Imagens: `02-gameplay-feedback-*`, `02-gameplay-combo-*`, `02-gameplay-revisao-de-erros-fim-da-licao.png`, `02-gameplay-fim-de-licao-*`, `02-gameplay-modal-*`, `02-gameplay-explain-my-answer-*`, `02-gameplay-exercicio-dificil-*`, `02-gameplay-card-subiu-de-nivel-level-up.png`, `02-gameplay-preferencias-*`.

Fontes: https://blog.duolingo.com/duolingo-101-how-to-learn-a-language-on-duolingo · https://blog.duolingo.com/duolingo-difficult-exercises · https://blog.duolingo.com/explain-my-answer-now-free · https://blog.duolingo.com/product-highlights/ · https://blog.duolingo.com/shape-language-duolingos-art-style/ · https://screensdesign.com/apps/duolingo-language-lessons/ · pesquisa/2026-10-29-gameplay.md §2 e §4

---

## 2. Catálogo de tipos de exercício

Não há lista oficial; os rótulos abaixo são os de tela em capturas do blog [V] ou de terceiros [S]. Para cada tipo: interação, exigência motora, tempo, tratamento do erro. Imagem de referência quando há.

| Tipo (rótulo) | Interação / input | Tempo | Erro | Imagem |
|---|---|---|---|---|
| **Translate the word / this sentence** [V] | Tocar tiles do banco de palavras ou digitar; botão alterna word bank ↔ teclado; arrastar para reordenar tiles (2024+) | sem | faixa vermelha; volta no fim; −1 energia | `02-gameplay-exercicio-traduza-a-palavra-imagem-peixe.png`, `…-dificil-traduzir-digitando.png` |
| **Tap what you hear** [V] | Tocar alto-falante; montar frase com tiles; botão tartaruga (lento, com pausas); replay ilimitado | sem | idem | `…-toque-o-que-ouve-word-bank.png`, `…-toque-o-que-ouve-lily-frances.jpg` |
| **Type what you hear / Repeat what you hear** [V] | Digitar; botão "Reveal" mostra o texto | sem | idem | `…-acessibilidade-reveal-mostrar-texto.png` |
| **What do you hear?** (4 opções) [V] | Toque em 1 de 4 tiles | sem | idem | `…-o-que-ouve-coreano-4-opcoes.jpg`, `…-escuta-grade-2x2-check.png` |
| **Listen for the missing word** [V] | Escolher entre opções de áudio | sem | idem | `…-ouca-a-palavra-faltante.jpg` |
| **Type the missing word** [V] | Digitar uma palavra na lacuna | sem | idem | `…-digite-a-palavra-faltante.jpg` |
| **Complete the translation** [S] | Lacuna + teclado | sem | idem | `…-complete-a-traducao-teclado.png` |
| **Select the correct translation / Mark the correct meaning** [S] | Múltipla escolha | sem | idem | `…-selecione-a-traducao-correta.png` |
| **Speak the correct response / Repeat after Lily** [V] | Tocar microfone, falar; reconhecimento de fala; "CAN'T SPEAK NOW" pula a fala da lição | timeout curto de gravação [I] | microfone desativável; não trava após tentativas [S] | `…-fale-a-resposta-correta.png`, `…-repita-depois-de-lily.png` |
| **Listen and respond** [V] | Ouvir (botão SLOW) e tocar uma resposta em áudio | sem | idem | `…-ouca-e-responda-lento.png` |
| **Tap the matching pairs** [V] | Tocar duas colunas (palavra↔tradução ou áudio↔texto) | sem na lição; **com tempo** no Match Madness | par errado treme em vermelho, sem coração [S] | `…-pares-audio-texto-claro.jpg`, `…-pares-erro-par-vermelho.png` |
| **Select the related image** [V] | Tocar 1 de 2–4 imagens | sem | idem | `…-duoradio-selecione-a-imagem-lucy.png` |
| **Complete the dialogue / chat** [S] | Múltipla escolha em balão | sem | idem | — |
| **What sound does this make?** [V] | Tocar sílaba/caractere (JA, KO) | sem | idem | `…-que-som-faz-japones.png` |
| **Build the character** [V] | **Arrastar** partes do caractere (Hangul) | sem | idem | `…-monte-o-caractere-arrastar.png` |
| **Draw the missing stroke** [V] | **Traçar** com o dedo seguindo guia azul | sem | tolerância; re-tentativa [I] | `…-trace-o-traco-faltante.png` |
| **Story** [V] | Diálogo narrado com perguntas intercaladas (toque, arrastar, múltipla escolha) | sem | erros não custam corações [S] | `…-story-historia-bea-una-cita.png`, `…-story-dialogo-eddy-oliver-escuro.png` |
| **DuoRadio** [V] | Episódio de rádio com personagem; exercícios: pares áudio↔tradução, ✓/✗, "Select 3 words you hear", imagem; sem transcrição; "Do this later" | sem | não documentado | `…-duoradio-*` (6) |
| **Adventures** [V] | Mini-mundo 2D: andar, tocar objetos, escolher falas; 30 XP; só EN→FR e ES→EN no lançamento (set/2024) | sem | **não marcado como erro**: personagem redireciona com cara de confuso | `…-aventuras-*`, `…-caminho-com-no-de-aventura.png` |
| **Video Call** (Max) [V] | Fala livre com Lily (IA); pausa "pensando"; "repeat"/"slow down"; 1 a 3 min; transcrição e feedback depois | sem | sem correção durante; "não penalizado se for compreendido" | `…-video-call-*` (6) |
| **Roleplay** (Max) [V] | Chat escrito por cenário | sem | feedback ao final | `…-roleplay-lily-cafe.png` |
| **Side Quest** [V] | 3 lições **cronometradas** por personagem; 1 estrela cada | **com tempo** | um erro = sem estrela | `…-side-quest-estrelas-cronometrado.jpg` |
| **Match Madness** [V/S] | Pares o mais rápido possível; 9 níveis; 20→60 XP; seg–sex na aba de ligas | **com tempo** (~1:45/nível) | penalidade de tempo | `…-match-madness-ends-in-1-day.png` |
| **Lightning Round** [S] | 2 min, 3 níveis mistos; até 40 XP | **com tempo** | tempo acaba = fim | — |
| **XP Ramp Up** [S] | 3 níveis × 3 rodadas, tempo decrescente (2:30 → 1:30) | **com tempo** | idem | — |
| **Rapid Review** [S] | Lição normal cronometrada, 3 checkpoints, até 60 XP | **com tempo** | idem | — |

Nota: desafios cronometrados custam 100 gemas por tentativa para usuário grátis (ilimitados no Super) [S]. Match Madness não gasta energia por erro [S].

**Risco na educação especial.** Os modos cronometrados são os de maior risco (tempo, erro = perda de estrela). Arrastar (Build the character) e traçar exigem precisão motora; digitar exige ortografia. Os formatos de **toque em alvo grande** (imagem, 4 opções, pares) e os de **manipulação direta** (Math, Adventures) são os mais aproveitáveis [I].

Fontes: pesquisa/2026-10-29-gameplay.md §1 · https://blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-listening-skills/ · https://blog.duolingo.com/duoradio-listening-practice · https://blog.duolingo.com/adventures · https://blog.duolingo.com/video-call · https://blog.duolingo.com/ways-to-practice-in-duolingo

---

## 3. Caminho (path) e estrutura do curso

**O que é.** Desde **1/11/2022** a árvore de habilidades (em que o usuário escolhia o que fazer) foi trocada por um **caminho linear único** [V]. Hierarquia: Curso → **Seção** (alinhada ao CEFR) → **Unidade** (objetivo comunicativo, guia, personagem) → **Nível** (nó; "um nó = um crown level da árvore antiga") → **Lição** [V/S]. Em volta: baús, Stories, DuoRadio, Adventures, prática personalizada, "Daily Refresh", troféu de revisão da unidade, nós **Legendary** (replay mais difícil, sem dicas; nó dourado; 40 XP) [V/S]. "Jump here?": quiz adaptativo curto para pular uma unidade; falhar = começar do início [S]. Mini-unidades com ícones (estrela, livro, câmera, fone) [V].

**Como o caminho decide o próximo item.** A **posição** no mapa é fixa, "pensada para misturar conceitos" com base em repetição espaçada; o que varia por pessoa é o **conteúdo** de cada lição (Birdbrain, §4) [V]. Em Math (2025) e Music o usuário pode escolher unidade [V]. No curso de xadrez, seções por faixa de Elo com "JUMP HERE" (`02-gameplay-xadrez-secoes-jump-here.png`).

**Anatomia visual** [S/I]: barra superior com bandeira do curso, chama da ofensiva, gemas, corações/energia; banner da unidade em cor sólida da seção; **nós circulares em zigue-zague** (ativo = cor da unidade com anel de progresso e popup "Lesson 2 of 7, +35 XP"; concluído = dourado/coroa; bloqueado = cinza); divisores com o nome da unidade; nav inferior com 5–6 ícones.

**Justificativa oficial.** Simplificar, guiar o iniciante, aumentar engajamento e conversão, dar motivo para inativos voltarem [V]. Estudo interno: quem usou o caminho teve **melhores notas de leitura e escuta** que quem usou a árvore [V/S] (`04-evidencias-eficacia-arvore-vs-caminho.png`).

**Críticas.** Forte reação de usuários antigos pela **perda de autonomia** [V/S]; usuária com TDAH: escolher a lição "ajudava a manter minha atenção" [S].

**Por que funciona.** Elimina paralisia de escolha; sempre há um próximo passo óbvio; progresso legível espacialmente; mini-marcos próximos [I/S].

**Risco na educação especial.** Linearidade e próximo passo óbvio ajudam quem precisa de previsibilidade e quem tem alta carga de decisão; mas **trava** quem empaca num nó (ex.: habilidade de leitura) e tira do educador a capacidade de direcionar [I].

**Adaptações.** Mapa visual com próximo passo destacado, mas o **educador atribui e reordena**; **rotas alternativas** da mesma habilidade em modalidades diferentes (auditiva, visual, motora); nenhum bloqueio duro por desempenho [I].

Imagens: `02-gameplay-caminho-*` (30), `02-gameplay-home-antes-depois-*`, `02-gameplay-xadrez-*`.

Fontes: https://blog.duolingo.com/new-duolingo-home-screen-design · https://blog.duolingo.com/intermediate-mini-units · https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655 · https://duolingo.deconstructoroffun.com/mechanics/lesson-path · pesquisa/2026-10-29-gameplay.md §2

---

## 4. Adaptação de dificuldade e revisão espaçada

**Half-Life Regression (HLR)** [V]: Settles & Meeder (ACL 2016); modelo treinável que estima a "meia-vida" de cada palavra na memória; reduziu o erro de previsão em >45% e teve ~metade do erro do sistema Leitner; aumentou a retenção diária em A/B; código e dataset (~13 M pares usuário-palavra) abertos.

**Birdbrain v1 (mar/2020)** [V]: regressão logística inspirada em **Item Response Theory**: P(acerto) = f(habilidade do aluno − dificuldade do exercício); dificuldade = soma das dificuldades das features (tipo, palavras); atualização por um passo de SGD após cada exercício ("generalização do Elo"); rodou em shadow mode; em out/2020 personalizava >20% das lições; A/B: mais engajamento e avanço mais rápido para material difícil (sem effect sizes publicados).

**Birdbrain v2 (mai/2022)** [V]: **LSTM** que comprime o histórico do aluno num vetor de 40 dimensões; atualiza em **minutos**; captura perfis irregulares; dados em streaming durante a lição; escala: >50 M ativos, ~1 bilhão de exercícios/dia.

**Session Generator** [V]: monta a lição de um pool grande de candidatos usando a P(acerto), mantendo o aluno "na zona em que continua engajado mas aprendendo no limite", e inclui revisão de erros recentes. **Taxa de acerto alvo não é publicada**; ~80% é inferência de terceiros [S]. Se o aluno vai bem, o algoritmo puxa exercícios "um pouco mais difíceis, do próximo nível", muitas vezes sem o aluno notar [V].

**Geração de conteúdo por LLM (jun/2023)** [V]: Learning Designer define tema/gramática/vocabulário/tipo; prompt com língua, nível CEFR e tema; LLM gera 10 candidatos; designer escolhe ~3 e edita; especialistas humanos têm a palavra final; o Birdbrain continua só **selecionando**.

**Por que funciona.** Espaçamento e prática de recuperação (dois dos achados mais robustos da ciência cognitiva) + dificuldade desejável calibrada para manter a taxa de acerto alta [V/I].

**Risco na educação especial.** É o componente de **maior valor pedagógico e menor risco** [I]. Atenção: um modelo treinado na população "média" calibra mal para perfis atípicos (irregularidade entre domínios, dificuldade fonológica específica) [I].

**Adaptações.** Taxa de acerto alvo alta (≥80%) ainda mais importante para quem tem histórico de fracasso; o educador vê e ajusta o nível; o painel mostra **por que** um item está voltando [I].

Imagens: `02-gameplay-birdbrain-*` (5), `02-gameplay-hlr-*` (3).

Fontes: https://preview.aclanthology.org/fix_video/P16-1174.pdf · https://blog.duolingo.com/how-we-learn-how-you-learn · https://blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain · https://spectrum.ieee.org/duolingo · https://blog.duolingo.com/large-language-model-duolingo-lessons · https://research.duolingo.com/ · pesquisa/2026-10-29-gameplay.md §3

---

## 5. Onboarding e nivelamento

**O que é.** Valor antes do cadastro: escolher idioma e motivo, meta diária (Casual 5 min → Intense 20), fazer a primeira lição antes de criar conta [S]. 2025: "7 perguntas rápidas" (de onde conheceu, quanto sabe, por quê), "Where would you like to start?" (do zero ou "Find my level"), tela "COURSE BUILDING… 3 million people learning Korean", pedido de notificação com o Duo ("I'll remind you to practice so it becomes a habit!") [S/V]. Nivelamento adaptativo sem "teste formal" visível; a versão de 2019 tinha "Take a test to jump ahead! ~5 minutes" [S]. Compromisso: trocar "continuar" por "me comprometo com a minha meta" aumentou retenção; meta de ofensiva (7/14/30 dias) no onboarding [V/S]. A primeira semana é a fase mais frágil [V].

**Risco na educação especial.** Onboarding com texto, escolhas abstratas e "teste" não serve para crianças pequenas; ser classificado no "nível 1" é visível [I].

**Adaptações.** Contas criadas pelo educador (como os cartões de login sem e-mail do Duolingo for Schools); onboarding com zero texto, personagem com voz, um jogo fácil com sucesso garantido; nivelamento **invisível e gentil**; cadência definida pelo educador [I].

Imagens: `02-gameplay-onboarding-*` (15).

Fontes: https://goodux.appcues.com/blog/duolingo-user-onboarding · https://screensdesign.com/apps/duolingo-language-lessons/ · https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks

---

## 6. Produtos para crianças e escolas

**Duolingo ABC** (alfabetização, 3 a 8 anos) [S]: 700+ lições / 127 unidades da pré-escola ao 2º ano, alinhadas ao Common Core e ao National Reading Panel; atividades por toque, arrastar, ouvir e falar: traçar letras e formas, estourar bolhas, parear letra↔objeto, desembaralhar letras, palavra↔imagem, dizer sons em voz alta (reconhecimento de fala), histórias com **destaque palavra a palavra**; "pouca ou nenhuma instrução explícita; a criança aprende por tentativa e erro"; cada jogo precisa ser concluído para liberar o próximo. **Sem anúncios, sem compras, offline.** Relato de +28% em alfabetização após 9 semanas (EDC) não verificado [S]. **Lacuna:** não há documentação de corações, timer, ligas nem de como o erro é sinalizado; requer teste de mão.

**Duolingo Math** [V/S]: elementar (3º ano → início do fundamental II) e "brain training"; **manipuláveis desenhados em código** (blocos contáveis, pizza de frações, líquido animado, grade de área/perímetro, arrastar cédulas, construir quadriláteros); dificuldade numérica sobe por faixa (soma até 10 → 100 → 500) com o visual escalando junto; alterna formatos para não ficar repetitivo; "evita ser chato ao avisar o erro"; ML repete o mesmo problema até a criança resolver; filosofia "implicit learning: you learn by doing"; desde 2025 o usuário escolhe a unidade; ofensiva e XP compartilhados com idiomas.

**Duolingo Music** [V/S]: ritmo, notas, teclado virtual, leitura de partitura, treino de ouvido; "centenas de lições curtas"; revisores: vira "jogo de ritmo simples"; erro corrigido no momento pedindo para repetir.

**Duolingo for Schools** [V, guia oficial]: professor cria turmas; alunos entram por link, código ou **contas criadas pelo professor sem e-mail** (roster de usuário/senha); **XP Assignment** com meta e prazo (a tela estima o tempo); dashboard com XP, lições, tempo, **activity log em tempo real**, relatório por aluno; quatro configurações de privacidade que o professor liga/desliga: Fórum, Eventos, **Friend requests e Leagues**, Conteúdo maduro; leaderboard de turma opcional. **Não há** controle do professor sobre corações/energia, timers ou dificuldade [I, por ausência]. Para menores de 13 no app consumidor, ligas e social são desativados [S].

**Lição para uma plataforma de educação especial.** Quando desenha para crianças pequenas, o Duolingo **remove** anúncios, compras, competição e economia e mantém loop + feedback + personagem + progresso. Narração com destaque palavra a palavra, traçado e manipulação direta são padrões diretamente aproveitáveis, desde que haja alternativas motoras. O painel do professor (e não a tela do aluno) é o lugar do dado de desempenho [I].

Imagens: `02-gameplay-math-*` (9), `02-gameplay-product-highlights-*`.

Fontes: https://www.commonsensemedia.org/app-reviews/duolingo-abc-learn-to-read · https://blog.duolingo.com/developing-math · https://blog.duolingo.com/new-subjects/ · https://www.the74million.org/article/duolingo-the-language-learning-app-giant-wants-to-teach-kids-math/ · https://schools-cdn.duolingo.com/documents/214566024b2e7c04285dd733ab8eab2d.pdf · pesquisa/2026-10-29-gameplay.md §5

---

## 7. Acessibilidade: o que existe, o que falta, o que os usuários dizem

**Existe** [V/S]: replay ilimitado de áudio; botão tartaruga (lento, com pausas entre palavras); "Can't listen now" (pula a escuta da lição) e "Can't speak now"; "Reveal" (mostra o texto em repeat-what-you-hear); "Do this later" no DuoRadio; toggle global "Listening exercises"; toggles de efeitos sonoros, haptics, animações, mensagens motivacionais; word bank ↔ teclado; microfone desativável; modo escuro (2020).

**Não existe / não localizado** [I, por ausência]: ajuste de fonte (Dynamic Type), alto contraste próprio, remoção de timers, opção "sem vermelho", modo dislexia, `prefers-reduced-motion`, declaração pública de acessibilidade/WCAG, paleta dark oficial. Na web, "animations" e "motivational messages" ficam só no localStorage e se religam sozinhos [S].

**Leitores de tela** [S]: "usável", mas botões sem rótulo, foco salta para "Next" após Check (precisa voltar para ler o feedback), tela de resultados lida como "números sem contexto", anúncios sem saída. Auditoria brasileira com WAVE: falta de texto alternativo e contraste inadequado em componentes interativos [S].

**Críticas de usuários neurodivergentes e com deficiência** [S]: "inacessível para autistas" (animações piscantes, sons súbitos, ordem rígida, pressão de ofensiva, perder corações por erro, expectativa de desempenho rápido, anúncios barulhentos); TDAH: perda da escolha de lição; surda: Practice Hub "forçando frases de escuta"; dislexia: "palavras e ortografia difíceis, querem mais customização"; texto pequeno e contraste baixo; cascata de 5 telas de recompensa "tediosa". **Lacuna:** nenhuma crítica documentada sobre timers e arrastar por usuários com deficiência motora.

**Contraste da paleta** (cap. 03 §7): CTAs primários (branco sobre verde 2,09:1, sobre azul 2,44, sobre vermelho 3,30) **falham AA**; o feedback combina cor com ícone, posição e som [I].

Imagens: `02-gameplay-acessibilidade-*` (5), `02-gameplay-preferencias-*` (3).

Fontes: https://blog.duolingo.com/learning-with-hearing-aids/ · https://applevis.com/comment/150456 · https://inviocean.com/learn/language-sounds-the-blind-experience-with-duolingo/ · https://www.thetribune.ca/?p=6500458 · https://sol.sbc.org.br/index.php/erigo/article/download/39529/39301 · pesquisa/2026-10-29-gameplay.md §6

---

## 8. Análises de game design do loop

- **Hook Model** (análises de terceiros) [S]: Trigger (push, culpa) → Action (lição 3–5 min) → Reward variável (XP, ofensiva, liga, baú) → Investment (ofensiva, posição na liga, amigos).
- **Tríade** [S]: core loop (lição → XP) / metagame (caminho, ligas) / perfil (ofensiva, avatar).
- **Octalysis** [S]: ofensiva como Core Drive 8 (loss avoidance).
- **Deconstructor of Fun** [S]: Meta / Fun / Lock-in (cap. 00 §2); "Lesson Path": por que lições curtas parecem progresso (caminho linear, mini-marcos próximos, mix variado).
- Nenhuma GDC talk ou artigo do Game Developer dedicado ao core loop foi localizado (lacuna).

Fontes: https://blakecrosley.com/guides/design/duolingo · https://yukaichou.com/gamification-analysis/brawl-stars-duolingo-collab-octalysis/ · https://www.deconstructoroffun.com/blog/2025/4/14/duolingo-how-the-15b-app-uses-gaming-principles-to-supercharge-dau-growth
