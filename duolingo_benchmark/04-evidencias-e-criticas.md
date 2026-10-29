---
titulo: Evidências e críticas
capitulo: 04
atualizado_em: 2026-10-29
marcas: "[V] fonte primária · [S] fonte secundária · [I] inferência"
---

# 04 · Evidências e críticas

Objetivo: separar o que é **dado da empresa**, o que é **evidência independente** e o que é **crítica documentada**, com a força de cada um. Serve de base para o cap. 05 e para qualquer decisão que cite "o Duolingo funciona".

## 1. Como ler os números do Duolingo

1. Quase todos vêm da própria empresa (blog, entrevistas, cartas a acionistas).
2. São **variações relativas** de testes A/B: "+3,3% de retenção D14" = 3,3% a mais que o controle, não 3,3 pontos percentuais.
3. Medem **retenção, engajamento ou tempo**, não aprendizagem. A exceção é o TSLW, que é um proxy.
4. Foram medidos com **adolescentes e adultos**. Os termos de uso exigem 13+ para conta padrão; para menores de 13, ligas e social são desativados [S]. Nenhum número foi medido com crianças nem com alunos da educação especial.
5. O produto muda o tempo todo (só a ofensiva passou por mais de 600 experimentos [V]). O que vale hoje pode não valer amanhã.
6. Correlação vs. causa: "quem chega a 7 dias de ofensiva tem 3,6x mais chance de concluir o curso" é correlação; gente mais motivada faz ofensivas longas. O próprio Mazal ressalva **viés de seleção** [V].

## 2. Dados da empresa (tabela consolidada)

| Afirmação | Valor | Tipo | Fonte |
|---|---|---|---|
| CURR é a alavanca de maior impacto em DAU | ~5x a segunda; CURR +21% em 4 anos; DAU 4,5x | simulação + resultado [V] | Lenny's |
| Ligas | +17% tempo de aprendizagem; 3x usuários altamente engajados | A/B [V] | Lenny's, blog |
| Separar meta diária da ofensiva | +3,3% retenção D14; +1% DAU; +10,5% com ofensiva | A/B [V] | blog |
| 2 congelamentos | +0,38% DAU | A/B [V] | blog |
| Animação de marco | +1,7% retenção D7 de novos | A/B [V] | blog |
| Reequilíbrio de XP | +1,1 M / +1,8 M minutos/dia de TSLW | A/B [V] | blog |
| "Hard exercise" rotulado | mais tempo, mais retorno, mais aceitação de difícil | A/B, sem número [V] | blog |
| Card de level-up | mais retorno e busca por conteúdo difícil | A/B, sem número [V] | blog |
| "Me comprometo com a meta" | ganho "significativo" | A/B, sem número [V] | Lenny's |
| Notificações: bandit | "dezenas" de pequenos ganhos; ~200 M em 34 dias | [V] | blog PT, KDD 2020 |
| Friends Quest / seguir amigos | 5,6x conclusão do curso (correlação) | [V] | carta a acionistas |
| Friend Streak | +22% conclusão da lição diária | [S] | DoF |
| Redesign das abas 2026 | engajamento subiu, aprendizagem estável | [V], sem número | blog |
| Corações → Energy | iniciantes tinham 2x mais chance de ficar sem corações | [V] | blog |
| Caminho vs. árvore | melhores notas de leitura e escuta | estudo interno [V/S] | blog |
| Pagantes | 9% dos MAU; 12,2 M assinantes; 133 M MAU (T4/2025) | [V/S] | SEC, imprensa |

Imagens: `01-recompensas-xp-experimento-reequilibrio-tslw.png`, `01-recompensas-ofensiva-experimento-retencao-grafico.png`, `00-visao-*`, `04-evidencias-eficacia-*`.

## 3. Eficácia (aprendizagem)

- Estudo em *Foreign Language Annals* (2022, n = 225): quem concluiu 5 unidades de espanhol ou francês teve leitura e escuta comparáveis a 4 semestres universitários [V]. Financiado pela empresa; críticos (CALL-EJ) apontam **viés de seleção**; só leitura e escuta [S].
- "Lições concluídas" como preditor mais forte de ganho (estudo citado pela empresa) [V].
- **TSLW** [V]: criado porque "total de sessões" premiava sessões curtas e fáceis e "tempo total" era dominado por superusuários. Fórmula: minutos no caminho + 0,5 × minutos em outras atividades. Meta: aumentar a parcela com ≥15 min/dia. **Lição:** até o Duolingo precisou corrigir uma gamificação que premiava o comportamento errado.

Fontes: https://blog.duolingo.com/results-duolingo-efficacy-studies · https://callej.org/index.php/journal/article/download/419/347/1013 · https://blog.duolingo.com/time-spent-learning-well/

## 4. Evidência independente sobre as mecânicas

### 4.1 Ofensivas
- **Silverman & Barasch (2023, *JCR* 49(6), 7 estudos)** [V]: ofensiva intacta → mais engajamento futuro; ofensiva **quebrada → abandono**, mesmo com o mesmo comportamento real; efeito mais forte com autoculpa, mais fraco quando há reparo; recomendam evitar "você quebrou sua ofensiva"; "o que conta como sequência é maleável".
- **Lally et al. (UCL)** via Mobbin [S]: perder um dia não afeta a formação do hábito.
- Surveys com usuários do Duolingo [S]: ofensiva é a fonte de motivação mais citada; recursos sociais "estressantes" para parte dos respondentes; competição gera "pressão ou ansiedade"; efeito motivacional via **competência e pertencimento; autonomia não media** (Da Nang 2026, n = 247).

### 4.2 Rankings
- **Hanus & Fox (2015, *Computers & Education*)** [S via revisões]: 16 semanas, leaderboard + insígnias → **menos** motivação intrínseca, satisfação e empoderamento, notas menores; atribuído à comparação social desfavorável; n ≈ 80; literatura mista.
- **Malayao et al. (2026, *JOTSE*)** [V]: ranking correlaciona com desempenho só para quem está no topo; posições baixas relatam queda de motivação e estresse.
- Quase-experimento (Japão, EFL) [S]: efeito negativo em emoção, atitude e desempenho de quem está embaixo; positivo no meio e no topo.

### 4.3 Recompensas extrínsecas e motivação intrínseca
- **Deci, Koestner & Ryan (1999, 128 estudos)** [V]: recompensas tangíveis esperadas e contingentes à tarefa reduzem motivação intrínseca (d −0,28 a −0,40); feedback verbal positivo e informativo aumenta. Contraponto: Cameron & Pierce. Debate aberto.

### 4.4 Gamificação em educação (meta-análises)
- **Kurnaz & Koçtürk (2025, *Psychology in the Schools*)** [V]: K-12, g = 0,65; intrínseca 0,64 vs extrínseca 0,71 (ICs sobrepostos); **fundamental I g = 0,31**, secundário 1,02; heterogeneidade alta.
- **Treve (2026, *Online Learning*)** [V]: 28 estudos; motivação g = 0,52, desempenho 0,41; **narrativa supera pontos/insígnias/ranking**.
- Meta-análise em ensino de programação (ISCTE) [S]: d = 0,4, efeito vindo de **níveis**; pontos, insígnias, avatares e rankings sem efeito significativo.

### 4.5 Jogos sérios e gamificação com alunos da educação especial
- **Schultz et al. (2025, *Frontiers in Psychiatry*)** [V]: 37 estudos / 22 jogos sérios para TDAH; mecânicas de recompensa **não foram analisadas**; maiores efeitos nos estudos com maior risco de viés.
- **López-Bouzas & del Moral-Pérez (2023, *Rev. J. Autism Dev. Disord.*)** [V]: 70 estudos com alunos autistas; maioria protótipos; ganhos em habilidades sociais e emocionais; pouca medida de eficácia.
- **Dai, Wufue & Zhang (2025, *Frontiers in Education*)** [V]: RCT n = 80, TDAH, 6–12 anos, 8 semanas: app com feedback imediato, pontos, insígnias e níveis adaptativos vs. mesmo conteúdo sem gamificação → ganhos grandes em atenção (η² 0,20–0,24) e leitura/escrita/matemática (d 0,98–1,25), mantidos em follow-up. Limites: app dos autores, não cego, QI 95–105, **componentes agrupados** (não isola a recompensa).
- **Kim (2025)** [V]: economia de fichas digital para TDAH, 4 semanas, melhora em atenção; amostra pequena.
- **TDAH e recompensa (literatura clínica)** [V]: crianças com TDAH descontam recompensas futuras mais fortemente (aversão à espera), respondem forte à recompensa **entregue** mas têm **antecipação diminuída**; recomendação clínica: reforço **imediato, frequente e consistente**. Isso apoia o loop curto com feedback imediato e **não** apoia mecânicas de antecipação longa (ofensiva de 30 dias, liga semanal, meta mensal) [I na aplicação].
- **Nenhum estudo controlado** localizado sobre o efeito de XP, liga ou ofensiva **do Duolingo** em crianças ou em usuários com TDAH/TEA; a evidência infantil é anedótica.

Fontes: pesquisa/2026-10-29-recompensas.md §5 · https://udspace.udel.edu/items/42ce576b-8e1f-429a-8541-e29e48dbcfbb · https://depts.washington.edu/techdocs/papers/deciExtrinsicRewardsAndIntrinsicMotivation99.pdf · https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1668260/full · https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1605744/full · https://link.springer.com/10.1007/s40489-023-00381-7 · https://pmc.ncbi.nlm.nih.gov/articles/PMC3268965 · https://pmc.ncbi.nlm.nih.gov/articles/PMC3059765

## 5. Críticas documentadas: síntese com força

| Crítica | Evidência | Força |
|---|---|---|
| Aversão à perda e ansiedade de ofensiva | A empresa admite que perder desmotiva e que usuários evitam desafios; Silverman & Barasch | **[V] forte** |
| A gamificação premia volume, não aprendizagem | A empresa criou o TSLW e reequilibrou o XP por isso | **[V] forte** |
| Culpa como alavanca (notificações, Duo triste, widget) | Tom "entre legal e malvado" assumido pelo CEO; "passive aggressive reminder" é uma das mais eficazes; relatos | [S] moderada |
| Monetização da frustração (corações → Energy, reparo, League Repair) | Abaixo-assinado; análises de UX; a empresa justifica pela aprendizagem | [S] moderada |
| Rankings reduzem motivação de quem perde | Hanus & Fox; Malayao; literatura mista | [V/S] moderada |
| Recompensas extrínsecas minam motivação intrínseca | Deci, Koestner & Ryan; debate aberto | [V] moderada a forte |
| Efeitos em crianças (choro, colapso, uso abaixo de 13 sem verificação) | Guias parentais; caso do menino de 10 anos; Common Sense 13+ | [S] fraca a moderada, sem estudo controlado |
| Eficácia superestimada | Estudos financiados pela empresa, viés de seleção | [S] moderada |
| Perda de autonomia (caminho linear) | Reação de usuários em 2022; relato de usuária com TDAH | [V/S] |
| Inacessível para parte dos usuários (autismo, deficiência visual, surdez, dislexia) | Relatos; auditoria WAVE; ausência de declaração WCAG | [S] moderada |
| Recompensa aleatória ≈ loot box | ECA Digital proíbe loot box para crianças no Brasil | [V lei / I aplicação] |
| Contraste dos CTAs abaixo de AA | Cálculo sobre a paleta publicada | [I] |

Fontes: https://screenwiseapp.com/guides/duolingo-and-the-streak-obsession · https://www.commonsensemedia.org/website-reviews/duolingo · https://www.ibtimes.co.uk/duolingo-restores-301-day-streak-hospitalised-boy-1813986 · https://thedecisionlab.com/es-ES/insights/consumer-insights/streak-creep-the-perils-of-too-much-gamification · https://www.thetribune.ca/?p=6500458 · https://sol.sbc.org.br/index.php/erigo/article/download/39529/39301

## 6. Contexto legal brasileiro (resumo)

- **ECA Digital (Lei 15.211/2025, em vigor desde 17/03/2026)** [V]: proíbe loot boxes em jogos voltados a crianças e adolescentes ou de acesso provável por eles (art. 20, segundo análises jurídicas); exige supervisão parental; veda perfilamento para publicidade a menores. ADI 7999 no STF contra trechos da lei. Aplicação a baús sem dinheiro real: zona cinzenta, consultar jurídico [I].
- **LGPD art. 14** [V]: tratamento de dados de crianças no melhor interesse, com consentimento específico de um dos pais; grafo social aberto entre crianças e perfilamento são problemáticos.

Fontes: https://www.machadomeyer.com.br/pt/inteligencia-juridica/publicacoes-ij/direito-digital/estatuto-digital-da-crianca-e-do-adolescente-lei-n-15-211-2025-entra-em-vigor-em-17-de-marco-de-2026 · https://confidata.com.br/blog/eca-digital-o-que-muda-empresas · https://coad.com.br/home/noticias-detalhe/139047/questionadas-regras-do-eca-digital-sobre-verificacao-de-idade-e-acesso-a-jogos-na-internet

## 7. Lacunas (o que ninguém conseguiu confirmar)

Consolidado das seções "Lacunas" das três pesquisas:
1. Lista oficial de tipos de exercício; regras atuais de Match Madness, Lightning Round, Ramp Up e Side Quest (tempo, penalidade, custo).
2. Taxa de acerto alvo do Birdbrain; limite de erros do Legendary e do "Jump here".
3. Feedback de erro no Duolingo ABC, Math infantil e Music (cor, som, retry, corações).
4. Tempo em tela das faixas de feedback e do combo; haptics por evento; durações e easing de animação; paleta sonora e autoria.
5. Tabela oficial de XP e preços em gemas; XP mínimo por divisão de liga; níveis e recompensas da Streak Society; regras da Family Quest; preço do reparo de ofensiva.
6. Declaração de acessibilidade/WCAG; ajustes nativos de fonte, contraste e timer; paleta dark oficial.
7. Duolingo for Schools: atribuições além de XP; controle do professor sobre corações/energia.
8. Críticas de usuários com deficiência motora sobre timers e arrastar.
9. Estudo controlado de qualquer mecânica do Duolingo com crianças ou com alunos da educação especial.
