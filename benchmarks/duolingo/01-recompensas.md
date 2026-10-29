---
titulo: Sistema de recompensas do Duolingo
capitulo: 01
atualizado_em: 2026-10-29
marcas: "[V] fonte primária · [S] fonte secundária · [I] inferência"
esquema_por_mecanica: [o que é, como funciona, por que funciona, números, evidência externa, críticas, risco na educação especial, adaptações, imagens, fontes]
---

# 01 · Sistema de recompensas

Como ler: cada mecânica segue o mesmo esquema. "Números" são da empresa (variações relativas de A/B, adultos). "Risco" é curto; o cap. 05 aprofunda por perfil.

## 0. Mapa da economia

```
 ESFORÇO                 MOEDAS/CONTADORES            SINKS (onde se gasta)         PRAZO
 exercício ──► combo ──► XP ───────────► liga (semanal) ──► promoção/rebaixamento    semana
 lição ──────────────► XP, baú aleatório ─► gemas ──► congelamento, recarga, desafios dia
 lição/dia ──────────► ofensiva ──► marcos 7/30/50/100/365 ──► Society, cards         dia→ano
 missões diárias ────► baú (3 níveis) + quest points ──► insígnia mensal, suits        dia→mês
 amigos ─────────────► Friends Quest, Friend Streak ──► XP boost, gemas, "nudge"       semana
 erro ───────────────► −1 coração (antes) / −energia (2025) ──► anúncio, gemas, Super  sessão
```

Programações de reforço presentes [I, classificação]: **razão fixa** (XP por lição, limiares de missão), **intervalo fixo** (reset diário/semanal/mensal, boosts de 15 min, Happy Hour), **razão variável** (conteúdo do baú, devolução aleatória de energia por acertos seguidos), **intervalo variável** (baú diário liberado 9 a 10 h depois). As recompensas de maior peso emocional (marcos de ofensiva) seguem intervalo fixo **crescente**. A cadência de micro-reforço é de ~10 a 20 s (feedback por item) e de ~3 min (fim de lição com 3 a 5 telas encadeadas) [S/I].

Imagens: `00-visao-dof-*`, `01-recompensas-loja-ofertas-especiais-baus.png`.

---

## 1. XP (pontos de experiência)

**O que é.** Pontos ganhos por atividade. Alimentam meta diária (opcional), ligas, missões e Streak Society. Existem XP Boosts (2x por 15 a 30 min; 3x que ativa sozinho na primeira lição do dia seguinte, desde dez/2024) [V/S].

**Como funciona (valores 2024–2026).** Lição nova do caminho **35 XP**; revisão de nó concluído **5 XP**; Legendary **40 XP**; Match Madness do estágio 1 (20 XP) até 60; Ramp Up e Lightning Round até 40; Rapid Review até 60; combo até +5 por lição; histórias 14 a 28 [V para os valores de captura oficial; S para os demais]. Histórico: 10 XP/lição (2019–2021) → 20–25 (2022–2024) → 35 após o reequilíbrio de jun/2024 [S]. Bônus por janela: Early Bird (6h–12h) e Night Owl (18h–0h) com baús, relatados como retirados em 2025 [S]; Happy Hour aos sábados (+5 XP/lição por 1 h) [S].

**Por que funciona.** Moeda única e comparável que liga todos os subsistemas [I]. Boosts com janela curta criam urgência (intervalo fixo).

**Números.** O XP **distorce o comportamento**: incentivava "farmar" atividades fáceis. Dar mais XP a lições do caminho rendeu **+1,1 M minutos/dia** (ajuste parcial) e **+1,8 M** (completo) de tempo aprendendo bem [V]. Atrelar a ofensiva ao XP confundia; simplificar para "uma lição por dia" tornou a ofensiva mais eficaz [V].

**Evidência externa.** Meta-análises de gamificação: pontos, insígnias e rankings isolados têm efeito fraco ou nulo na aprendizagem; **níveis** e **narrativa** têm efeito maior (cap. 04).

**Críticas.** Premia volume, não domínio. O próprio Duolingo criou o TSLW porque "total de sessões" premiava sessões curtas e fáceis [V].

**Risco na educação especial.** O XP só tem sentido em comparação ou acumulação; números grandes e abstratos têm pouco significado para crianças pequenas; premia velocidade e pune quem processa devagar [I].

**Adaptações.** Progresso **concreto e não numérico** (um mundo que ganha objetos, um mapa que se revela), ligado a **domínio de habilidade**, não a tempo ou quantidade [I].

Imagens: `01-recompensas-xp-experimento-reequilibrio-tslw.png`, `01-recompensas-xp-formula-tslw.png`, `01-recompensas-xp-tempo-medio-por-licao-por-nivel.png`, `02-gameplay-caminho-popup-licao-start-35xp.png`, `02-gameplay-caminho-popup-review-5xp-legendary-40xp.png`.

Fontes: https://blog.duolingo.com/time-spent-learning-well/ · https://blog.duolingo.com/ways-to-practice-in-duolingo · https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks · pesquisa/2026-10-29-recompensas.md §1

---

## 2. Ofensiva (streak), congelamento, reparo, marcos

**O que é.** Contador de dias consecutivos com ao menos uma lição [V]. Antes exigia bater a meta diária; hoje basta uma lição [V].

**Como funciona.**
- **Congelamento** (Streak Freeze): protege um dia sem prática; até **2** equipados grátis, até **5** via Streak Society; ~200 gemas (A/B de 200 a 600) [V/S]. Assinantes Super ganham reposição automática pela primeira missão diária [S]. "Earn Back": com estoque zerado, poucas lições numa janela curta restauram [S].
- **Reparo**: pago em gemas ou dinheiro; evento gratuito em jun/2026 (ofensiva ≥30 dias, 3 lições seguidas) [S].
- **Aposta** (Streak Wager / Double or Nothing): 50 gemas apostadas em manter 7/14/30 dias; teste original relatou +5% retenção D14 e +600% de receita de compras [S].
- **Meta de ofensiva** (Streak Goal): no onboarding, 7/14/30 dias; tela "Streak Goal & Protection" [S]. Versões prometem gemas (30/300/700) e "5x mais chance de concluir o curso" (`01-recompensas-ofensiva-meta-compromisso-gemas-5x.png`).
- **Perfect Streak / Perfect Week**: camada de prestígio para dias sem congelamento; halo na chama e barra contínua; sem recompensa funcional; limiar varia por A/B (capturas com 3, 22 e 26 dias) [S/V].
- **Marcos**: 7, 30, 50, 100, 365 com animação; o Duo vira **fênix** porque "on fire" não era entendido em todas as culturas; versão com balões rejeitada por "baixa energia"; o timing foi tratado como tão importante quanto o visual [V]. Card compartilhável (5 a 10x mais compartilhamento orgânico; >6 M compartilhamentos diários) [S].
- **Streak Society**: nasceu como clube de 365 dias (2022); hoje em níveis a partir de 7 dias, cada um com baú; relatos: 7 dias → 3 dias de Super; 30 → ícone exclusivo; cada 100 → +3 congelamentos; 365 → contador ao lado do nome no ranking; certificado imprimível e kit físico [V para a existência; S para os níveis].
- **Notificação "salva-ofensiva"** à noite: a "primeira grande vitória" do time de retenção [V]. **BRB**: protege a ofensiva em quedas do servidor (>2 M protegidas) [S].
- **Widget**: o Duo fica progressivamente aflito até a meia-noite e relaxa depois; 25 ilustrações [V].
- **Friend Streak**: compartilhada com até 5 amigos; níveis 7/14/30/50 (Good/Great/Best/Lifelong friends); "nudge" em nome do usuário; +22% de conclusão da lição diária [V/S].

**Por que funciona (psicologia citada pela empresa).** Formação de hábito por repetição no mesmo contexto [V]; **aversão à perda** (o Duolingo admite: perder a ofensiva reduz a motivação e usuários **evitam desafios** para não arriscá-la) [V]; os primeiros dias valem mais (de 2 para 3 dias é +50%; de 200 para 201, +0,5%), por isso as telas investem no início [V]; flexibilidade (congelamento) aumenta a motivação [V].

**Números (empresa).**
| Mudança | Resultado |
|---|---|
| Separar meta diária da ofensiva | +3,3% retenção D14; +1% DAU; +10,5% aprendizes com ofensiva (+19% entre novos) [V] |
| Permitir 2 congelamentos | +0,38% DAU [V] |
| Nova animação de marco | +1,7% retenção D7 de novos [V] |
| Um ano de otimização | >50% do DAU com ofensiva de 7+ dias (era ~1/3) [V] |
| Chegar a 7 dias | 2,4x mais chance de voltar no dia seguinte; 3,6x de concluir o curso (correlação) [V] |
| "Continuar" → "Me comprometo com a meta" | Ganho "significativo" sem número [V] |
| Weekend Amulet (teste) | +4% retorno em 7 dias, −5% perda de ofensiva; DAU cai 5–10% nos fins de semana [S] |
Escala: 32 M de DAU com ofensiva ≥7 dias; 8 a 9 M com ≥1 ano (2025) [S].

**Evidência externa.** Silverman & Barasch (2023, *JCR*, 7 estudos): ofensiva intacta aumenta engajamento futuro, ofensiva **quebrada leva ao abandono** mesmo com o mesmo comportamento real; pior quando a pessoa se culpa, melhor quando há reparo; recomendam **evitar "você quebrou sua ofensiva"** [V]. Lally (UCL, hábitos): perder um dia **não afeta** a formação do hábito; o design é que faz o dia perdido parecer falha pessoal [S]. Mobbin (859 designs de ofensiva): quase todos contam dias, não aprendizagem; alavancas emocionais: esperança, completude de padrão, antropomorfismo, medo [S].

**Críticas.** Relatos de choro e "colapso" de crianças ao perder a ofensiva [S, anedótico]; caso público de restauração da ofensiva de 301 dias de um menino de 10 anos hospitalizado [S]; "ansiedade de ofensiva" quando o motivo de abrir o app passa de "quero aprender" para "tenho medo de perder" [S]. Que 2 congelamentos deem só +0,38% de DAU e que existam campanhas de recuperação sugere que a **perda** é fonte relevante de churn [I].

**Risco na educação especial: ALTO.** Pressupõe acesso diário que a criança não controla (fins de semana, faltas por terapias, falta de dispositivo); a quebra de uma sequência pode ser muito aversiva para quem tem rigidez cognitiva; vergonha para quem tem dificuldade com planejamento e tempo [I].

**Adaptações.** Contador **acumulativo que nunca zera**; "ritmo" semanal com tolerância; ofensiva **coletiva** pausada pelo calendário escolar; nunca mostrar perda nem usar "você quebrou" [I + V de Silverman & Barasch].

Imagens: `01-recompensas-ofensiva-*` (36 arquivos: marcos, fênix, calendário, Society, congelamento, Perfect Streak, meta, reparo), `01-recompensas-widget-*` (9), `01-recompensas-friend-streak-*` (6).

Fontes: https://blog.duolingo.com/improving-the-streak · https://blog.duolingo.com/duolingo-streak-research/ · https://blog.duolingo.com/how-duolingo-streak-builds-habit · https://blog.duolingo.com/streak-milestone-design-animation · https://blog.duolingo.com/streak-celebration-parties/ · https://blog.duolingo.com/friend-streak/ · https://blog.duolingo.com/widget-feature/ · https://duolingo.deconstructoroffun.com/mechanics/streaks · https://mobbin.com/blog/streaks-are-about-losing-a-study-of-859-streak-designs · Silverman & Barasch (2023) JCR 49(6) · pesquisa/2026-10-29-recompensas.md §2

---

## 3. Missões diárias, mensais, de amigos, de família

**O que é.** Três missões por dia (ex.: ganhar X XP, 90% de acerto em N lições, N combos), com baú por missão em três níveis (bronze/prata/ouro) [V/S]. **Quest points** acumulam para a insígnia mensal e para eventos de colecionáveis [S]. **Friends Quest** semanal (5 dias) pareia dois amigos ativos; desde 2025 há pareamento universal [V]. **Family Quest** para o plano família [S].

**Como funciona.** Missões e exigências são **adaptativas por usuário** [S]. Insígnia mensal: de 1.000 XP/mês (2021) para 30 missões (2022), 50 (2023), 100 para alguns (2024), "70 pontos" (2026); o Duolingo trocou XP por missões para impedir "farm" de XP no fim do mês [V/S]. Recompensa por fechar as 3 diárias aumentou em 2025 [V]. Friends Quest: XP Boost de 30 min ou 100 gemas [S]. Baú diário cuja recompensa só libera 9 a 10 h depois (intervalo variável) [S].

**Por que funciona.** Metas próximas, específicas e variadas; rotação diária traz novidade; cooperação traz compromisso social ("não quero decepcionar meu parceiro") [I].

**Números.** Quem segue amigos tem **5,6x** mais chance de concluir o curso (correlação); mais da metade do DAU segue alguém [V]. Não há número isolado para missões.

**Críticas.** Metas mensais que sobem para quem cumpre geram reclamações ("usuários frustrados com o aumento de 50 para 100") [S].

**Risco na educação especial.** Missões de **precisão** punem quem erra mais; de **velocidade** punem processamento lento; em dupla, o aluno "mais fraco" vira o motivo do fracasso do par; missões que mudam todo dia quebram previsibilidade [I]. **Positivo:** missões cooperativas de grupo são a mecânica social mais aproveitável.

**Adaptações.** Missões **do grupo inteiro**, de esforço/exploração ("experimente um jogo novo"), anunciadas com antecedência e com ícones fixos [I].

Imagens: `01-recompensas-missoes-*`, `01-recompensas-friends-quest-*`, `01-recompensas-bau-*`, `01-recompensas-colecionaveis-*`.

Fontes: https://blog.duolingo.com/friends-quests/ · https://blog.duolingo.com/product-highlights/ · https://duolingo.deconstructoroffun.com/mechanics/collectibles · pesquisa/2026-10-29-recompensas.md §4

---

## 4. Gemas, baús, loja, colecionáveis

**O que é.** Gemas: moeda (antes "lingots"). Baús: recompensa de conteúdo variável. Loja: sinks. Colecionáveis (2025–2026): eventos de ~21 dias com 6 "suits" de avatar por quest points [S].

**Como funciona.**
| Item da loja | Gemas [S] |
|---|---|
| Congelamento | 200 (A/B 200–600); captura de 2026 mostra 425 por 1 dia |
| Recarga de corações/Energy | 350–450 |
| Timer Boost | 450 |
| Desafio Lendário / cronometrado | 100 cada (grátis no Super) |
| League Repair | 2.000 |
| Double or Nothing | 50 |
Fontes de gemas: baús pós-lição, baú de missão (ex.: +6), top 3 da liga (60), Friends Quest (100), Society, convites [S]. Conquistas **não dão gemas** [V]. Pacotes em dinheiro de US$ 2,99 a 11,99 [S]. Baú redesenhado em 2025 para ser "mais delicioso" [V]; tela "COMMON — Tap for a chance to upgrade!" (`01-recompensas-bau-common-toque-para-upgrade.png`).

**Por que funciona.** Recompensa de razão variável é a mais resistente à extinção (Skinner) e é o mecanismo central das loot boxes [I]. Loop fechado: lições dropam os itens que as gemas compram [S].

**Críticas.** Monetização da frustração: cada ponto de escassez tem um "resolvedor" pago (§7).

**Risco na educação especial: MUITO ALTO.** Recompensa aleatória é especialmente potente para crianças com impulsividade e sensibilidade a recompensa imediata [I]. **Legal (Brasil):** o ECA Digital (Lei 15.211/2025, em vigor desde 17/03/2026) proíbe loot boxes em jogos voltados a crianças e adolescentes ou de acesso provável por eles; baús de conteúdo aleatório mesmo sem dinheiro real ficam em zona cinzenta [V para a lei; I para a aplicação; consultar jurídico].

**Adaptações.** **Sem moeda, sem baú aleatório, sem loja.** Recompensas determinísticas e anunciadas ("ao terminar, você ganha a peça X"); colecionáveis que **nunca se perdem** e que todos conseguem completar [I].

Fontes: https://blog.duolingo.com/achievement-badges/ · https://duolingo.deconstructoroffun.com/mechanics/leagues · https://duolingoguides.com/what-are-duolingo-gems-for/ · https://www.machadomeyer.com.br/pt/inteligencia-juridica/publicacoes-ij/direito-digital/estatuto-digital-da-crianca-e-do-adolescente-lei-n-15-211-2025-entra-em-vigor-em-17-de-marco-de-2026 · pesquisa/2026-10-29-recompensas.md §1.4–1.5

---

## 5. Corações → Energy (vidas)

**O que é.** Até 2025: 5 corações; cada erro tira um; sem corações a lição para (esperar, praticar, anúncio, gemas ou Super) [V/S]. Desde mai–jul/2025: **Energy**, barra de 25 unidades [S]; cada exercício gasta; o erro gasta mais; **acertos seguidos devolvem energia em ritmo aleatório**; revisar erros é grátis; recarga total em ~1 dia; recarga com anúncio ou gemas [V].

**Justificativa oficial [V].** "Os corações não eram a forma mais eficaz de apoiar a aprendizagem"; "errar é parte normal de aprender"; iniciantes tinham **2x** mais chance de ficar sem corações no meio da lição.

**Leitura crítica [S].** Com corações, quem não errava nunca era levado a pagar; com Energy, **até quem acerta tudo acaba sem energia**: a pressão de monetização passa a valer para todos. Abaixo-assinado "Hearts, not Energy".

**Risco na educação especial: MUITO ALTO.** Punir o erro com a interrupção da atividade é contrário ao DUA e à pedagogia do erro; quem erra mais (leitura, toque impreciso) é expulso justamente quando precisa de mais prática; uma barra que acaba desloca o controle do tempo do educador para o sistema [I]. Até o Duolingo abandonou corações por isso [V].

**Adaptações.** Errar nunca interrompe; limite de tempo é do educador, não de uma barra [I].

Imagens: `02-gameplay-modal-coracoes-cada-erro-custa-1.png`, `01-recompensas-energy-*`.

Fontes: https://blog.duolingo.com/duolingo-energy/ · https://uxdesign.cc/duolingos-small-ui-switch-that-changes-everything-fae257203633 · https://www.change.org/p/duolingo-hearts-not-energy

---

## 6. Ligas e leaderboards

**O que é.** Ranking **semanal** de ~30 pessoas por XP da semana, de qualquer curso, pareadas por ritmo e fuso [V/S]. **10 divisões** (Bronze → Diamante). Promoção de 30: Bronze 20, Prata 15, Ouro 10, Safira–Pérola 7, Obsidiana 5; rebaixamento do 24º para baixo; fecha domingo [S]. Top 10 do Diamante vão ao **Torneio Diamante** (quartas, semi, final) [V]. Entrada automática (opt-out). Notificações "você foi ultrapassado", "risco de rebaixamento" [S]. Leaderboard de amigos desde 2025 [V]. League Repair: 2.000 gemas [S]. Prêmio: 60 gemas para top 3 [S]. XP necessário não é publicado; exemplos: 1º com 1.947 XP, 11º rebaixado com 246 [S].

**Por que funciona.** Comparação com rivais **próximos em desempenho**: "a proximidade do competidor importa mais do que a proximidade da relação"; a primeira versão com amigos funcionava pior [V]. Aversão à perda (rebaixamento), meta próxima (corte de promoção), prazo [I].

**Números.** Lançar ligas: **+17%** de tempo total de aprendizagem e **3x** usuários altamente engajados (1h+/dia, 5 dias/semana) [V]. O ranking estimulou atividades fáceis; o XP foi reequilibrado [V].

**Evidência externa.** Hanus & Fox (2015): curso de 16 semanas com leaderboard e insígnias teve **menos** motivação intrínseca e notas finais menores, atribuído à comparação social desfavorável; literatura mista [S]. Malayao et al. (2026): ranking correlaciona com desempenho só para quem está no topo; posições baixas relatam queda de motivação e estresse [V]. Mais em cap. 04.

**Risco na educação especial: MUITO ALTO.** Expõe sempre os mesmos alunos na lanterna, diante dos colegas; risco de bullying; hiperfoco no ranking pode virar compulsão; "ser ultrapassado" pode ser vivido como injustiça [I].

**Adaptações.** Nenhum ranking entre alunos; progresso **coletivo** rumo a uma meta comum; comparação só consigo mesmo e só quando positiva; desempenho individual **só no painel do educador** (como o Duolingo for Schools) [I].

Imagens: `01-recompensas-liga-*` (19 arquivos: diagrama, divisões, promoção, rebaixamento, torneio, repair, prêmio).

Fontes: https://blog.duolingo.com/duolingo-leagues-leaderboards/ · https://duolingo.deconstructoroffun.com/mechanics/leagues · https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth · pesquisa/2026-10-29-recompensas.md §1.3 e §5

---

## 7. Conquistas, insígnias, recordes pessoais

**O que é.** Reformulação de dez/2023: "Personal Records" (Longest Streak, Daily Most XP, Perfect Lessons, Highest League) e "Awards"; insígnias mensais de missão; conquistas não dão gemas [V].

**Por que funciona.** Coleção, completude, identidade [I].

**Números.** Sem dado público de impacto.

**Evidência externa.** Deci, Koestner & Ryan (1999, 128 estudos): recompensas tangíveis esperadas e contingentes reduzem motivação intrínseca (d −0,28 a −0,40); feedback verbal informativo aumenta; debate aberto (Cameron & Pierce) [V].

**Risco na educação especial: moderado e aproveitável.** Conquistas cumulativas que nunca se perdem são a forma mais segura de reconhecimento; cuidado com conquistas de desempenho ("10 lições perfeitas") e de tempo ("30 dias seguidos"); coleção impossível de completar gera sofrimento [I].

**Adaptações.** Reconhecimento **informativo** ("você aprendeu a juntar sílabas com R") em vez de controlador ("ganhe 3 estrelas para desbloquear"); todas alcançáveis pelo grupo inteiro; mostrar sempre o que falta [I].

Imagens: `01-recompensas-conquistas-*`, `02-gameplay-conquista-flawless-finisher.png`.

Fontes: https://blog.duolingo.com/achievement-badges/ · Deci, Koestner & Ryan (1999) Psychological Bulletin 125(6)

---

## 8. Social: amigos, feed, cutucadas

**O que é.** Seguir amigos, Friend Streak, Friends Quest, leaderboard de amigos, presentear boosts, feed com "friend updates" ("[amigo] completou uma unidade", "avançou à semifinal") com botão SEND CONGRATS, "high five", nudge [V/S].

**Números.** 5,6x mais chance de concluir o curso para quem segue amigos (correlação); programa de indicação trouxe só +3% de novos [V].

**Risco na educação especial.** Grafo social aberto entre crianças não é aceitável (LGPD art. 14, ECA Digital); recursos baseados em "amigos" tornam visível quem não tem amigos ou não foi escolhido, o que amplifica a exclusão de crianças que já têm menos amizades recíprocas [I].

**Adaptações.** O "social" é **o grupo fechado como unidade** (criado pelo educador) e o personagem como parceiro; sem seguir, convidar ou ver o perfil de colegas [I].

Imagens: `01-recompensas-social-feed-amigo-completou-unidade.png`, `01-recompensas-liga-feed-amigo-semifinal-diamante.png`, `01-recompensas-friends-quest-*`, `01-recompensas-friend-streak-*`.

Fontes: https://blog.duolingo.com/friends-social-features/ · https://blog.duolingo.com/friend-streak/

---

## 9. Notificações, e-mail, widget

**O que é.** Lembretes diários (push e e-mail) na voz do Duo e, desde 2025, de Lily e Falstaff [V]; "salva-ofensiva" à noite; mensagens cada vez mais insistentes; depois de dias sem resposta, "parece que esses lembretes não estão funcionando, vamos parar de enviá-los" (chamada internamente de "passive aggressive reminder", uma das mais bem-sucedidas, segundo o CPO) [V/S]. Ícone do app muda de humor (sazonais: assustador, bobo, triste, glitch) [V]. Widget com o Duo por hora do dia [V].

**Como funciona (algoritmo) [V].** Banco de lembretes pré-escritos, personalizados por idioma e tamanho da ofensiva; novas mensagens testadas em grupo pequeno; seleção por **bandit** multi-armed (recompensa = lição concluída), pontuação só entre pessoas do mesmo perfil, **decaimento de novidade** pela curva do esquecimento; ~200 M de lembretes em 34 dias. A mesma mensagem vale −4,7 para um idioma e +8,7 para outro. O push é tratado como canal a "proteger": aumentar volume exigia aprovação do CEO; o exemplo do Groupon (5 e-mails/dia) é usado como alerta.

**Por que funciona.** Gatilho externo no momento certo; culpa e humor que viraram marca [V/S].

**Críticas.** "20 dias de chantagem emocional"; imagens do Duo triste "incomodam alguns usuários, especialmente crianças" [S]; CEO descreveu o tom como "entre legal e malvado" [S].

**Risco na educação especial: ALTO.** Ironia e sarcasmo são lidos **literalmente** por parte do público; "o Duo está triste por sua causa" vira culpa real [I, consistente com a literatura sobre pragmática]. Push para criança fora do contexto de uso não se justifica.

**Adaptações.** Sem push para a criança; comunicação **informativa e sem culpa** ao responsável/educador; o personagem nunca fica triste, bravo ou decepcionado com a criança, nunca "sente falta" de forma culpabilizante, nunca ameaça perda; pode ficar contente ao reencontrar sem mencionar a ausência [I].

Imagens: `01-recompensas-notificacoes-*` (7), `01-recompensas-widget-*` (9), `02-gameplay-onboarding-pedido-de-notificacao.png`, `03-estilo-copy-teste-notificacao-alemao.png`.

Fontes: https://blog.duolingo.com/oi-e-o-duo-inteligencia-artificial-por-tras-do-meme/ · https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth · https://www.universityxp.com/news/2025/7/25/we-havent-seen-you-in-a-while-duolingos-passive-aggressive-strategy-for-keeping-users-hooked · https://uxdesign.cc/20-days-of-emotional-blackmail-from-duolingo-4f566523e3c5 · KDD 2020 "A Sleeping, Recovering Bandit for Recurring Notifications"

---

## 10. Monetização: Super, Max e a fricção da economia grátis

**O que é.** **Super**: energia ilimitada, sem anúncios, Practice Hub, desafios e Legendary sem gemas, congelamento automático [V/S]. **Max**: + **Video Call** com Lily (memória entre chamadas, transcrição, feedback pós-chamada) e **Roleplay**; **Explain My Answer** saiu do Max e ficou grátis em 1/1/2026 [V]. Preços (Brasil, 2025): Super R$ 179,90/ano, Família R$ 269,90 [S]; EUA: Super ~US$ 12,99/mês, Max ~29,99 [S]. 9% dos MAU pagam (2025); 12,2 M de assinantes, 133 M MAU (T4/2025); assinaturas = 75% da receita, anúncios 9% [V/S].

**Como a fricção converte [I, apoiado em S].** Energy acaba → anúncio, 350–450 gemas ou Super; desafio cronometrado → 100 gemas ou Super; congelamento zerado → 200 gemas ou auto-freeze do Super; rebaixamento → 2.000 gemas; ofensiva perdida → reparo pago. Paywalls usam "usuários Super têm 4x mais chance de concluir o curso" [S]. Localização de copy: "Unlimited Hearts" virou "No heart loss on errors" em chinês [V].

**Risco na educação especial.** Qualquer fricção monetizável é incompatível com uso escolar; o ECA Digital veda perfilamento para publicidade a menores [V].

Imagens: `02-gameplay-max-*`, `03-estilo-copy-unlimited-hearts-ingles-vs-chines.png`, `01-recompensas-energy-opcoes-de-recarga.png`.

Fontes: https://blog.duolingo.com/duolingo-max · https://blog.duolingo.com/explain-my-answer-now-free · https://www.sec.gov/Archives/edgar/data/1562088/000156208825000098/q1fy25duolingo3-31x25share.htm · pesquisa/2026-10-29-recompensas.md §3

---

## 11. Resumo: o que cada mecânica realmente faz

| Mecânica | Alavanca psicológica | Prazo | Reforço | Monetiza? | Veredito (cap. 00 §6) |
|---|---|---|---|---|---|
| XP | acumulação, comparação | item/lição | razão fixa | não | substituir |
| Ofensiva | aversão à perda, hábito | dia | intervalo fixo crescente | sim (freeze, repair) | substituir |
| Missões | meta próxima, novidade, compromisso social | dia/semana/mês | razão fixa + baú | indireta | adaptar |
| Baú / gemas | recompensa variável, escassez | lição/dia | razão variável | sim | não usar |
| Corações / Energy | escassez, punição do erro | sessão | — | sim | não usar |
| Liga | comparação social, status, prazo | semana | — | sim (repair) | não usar |
| Conquistas | coleção, identidade | longo | razão fixa | não | adaptar |
| Social | reciprocidade, pertencimento | semana | — | não | não usar (grafo) |
| Notificações | gatilho, culpa, humor | dia | — | não | não usar (para a criança) |
