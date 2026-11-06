---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-linguagem
etapa: pesquisa / c-benchmark
status: rascunho para revisão
atualizado_em: 2026-10-27
---

# C · Benchmark de produtos educacionais e jogos infantis

**Objetivo:** mapear como produtos próximos ao VUOO resolvem loop de jogo, recompensa, mascote, visual, tom de voz e acessibilidade, para decidir o que copiar, o que adaptar e o que evitar. Os códigos `[IN-xx]` remetem a `../00-insumos.md`.

**Método e confiabilidade.** Pesquisa web (outubro/2026) em sites oficiais, lojas de aplicativos, imprensa especializada, artigos acadêmicos e organizações de defesa da infância. Três níveis de confiança aparecem no texto:
- sem marcação: afirmação com fonte listada no fim da ficha;
- **(autodeclarado)**: vem do marketing ou da loja do próprio produto, sem verificação independente;
- **(obs.)**: observação de design feita por quem escreve este relatório a partir de conhecimento prévio dos produtos (paleta, traço, tom). Não há fonte citável; vale conferir com captura de tela antes de virar decisão.

Produtos analisados (14 fichas + 1 referência institucional): Duolingo / Duolingo ABC, Khan Academy Kids, Lingokids, Endless Alphabet, Teach Your Monster to Read, Toca Boca, Prodigy Math, Matific, Kahoot!, ClassDojo, Otsimo, Proloquo2Go / Avaz (CAA), EndeavorRx, GraphoGame Brasil, Elefante Letrado e Árvore, mais a identidade do Governo de SP / SEDUC-SP.

O Instituto Ayrton Senna foi pesquisado e descartado como ficha: não foi encontrado jogo digital próprio para crianças; a atuação é em programas e materiais socioemocionais (ver fontes gerais).

---

## 1. Tabela comparativa

| Produto | Público | Loop central | Recompensa | Mascote | Falha / pressão | Monetização | Acessibilidade declarada | Relevância p/ VUOO |
|---|---|---|---|---|---|---|---|---|
| **Duolingo / ABC** | 3–8 (ABC); adultos (principal) | Lição curta em trilha linear | XP, sequência (streak), corações, baús | Duo (coruja), elenco diverso | Corações (perde ao errar); streak cria ansiedade | Freemium (principal); ABC sem anúncios nem compras | Áudio em tudo no ABC; offline | Alta: referência citada [IN-14] |
| **Khan Academy Kids** | 2–8 | Trilha de atividades curtas + biblioteca | Itens para personagens, estrelas | Kodi Bear + 4 amigos animais | Baixa pressão; sem tempo | Gratuito, sem anúncios, sem assinatura | Texto todo tocável com leitura em voz; ícones no lugar de texto; gestos do mascote | Muito alta |
| **Lingokids** | 2–8 | Catálogo de atividades, vídeos, músicas | Pouco explícito; área dos pais celebra progresso | Baby Bot (robô) + Billy, Cowy, Lisa, Elliot | Baixa | Assinatura agressiva; reclamações de cobrança | Não declarada | Média: robô-mascote próximo do VUOO Bot |
| **Endless Alphabet** | 3–6 | Arrastar letras-personagem para montar palavra; animação explica o sentido | A própria animação (recompensa intrínseca) | Monstrinhos | Sem pontuação, sem falha, sem tempo (autodeclarado) | Compra única | Não declarada | Alta: modelo "sem falha" |
| **Teach Your Monster to Read** | 3–6 | Aventura de fonética com monstro personalizado | Customizar e "ensinar" o monstro | Monstro criado pela criança | Baixa | Compra única no app (preço varia por país) | Não declarada | Alta: criança ensina o mascote |
| **Toca Boca** | 3–9 | Brincadeira livre, sem objetivo | Nenhuma; a brincadeira é a recompensa | Personagens neutros em gênero | Sem vencer/perder, sem placar | Historicamente sem IAP/anúncios (hoje freemium no Toca World) | Não declarada | Média: estética e tom, não loop |
| **Prodigy Math** | 6–14 | RPG de batalhas que exigem resolver contas | Pets, itens, níveis, baús | Avatar mago + pets | Combate | Freemium com "membership"; alvo de denúncia à FTC | Não declarada | Alta como **antiexemplo** |
| **Matific** | 4–12 (SEDUC-SP oferece) | "Episódios" de minijogos manipulativos de matemática | Baú em 3 níveis, itens de avatar, metas | Avatar | Baixa | B2B/B2G | Não declarada | Muito alta: já está na rede paulista |
| **Kahoot!** | Todas | Quiz ao vivo projetado na sala | Pontos por acerto e velocidade, pódio | Nenhum (marca) | Timer visível, ranking público | Freemium B2B | Não há como desligar o timer ao vivo | Alta como **alerta** |
| **ClassDojo** | Ensino fundamental | Professor dá/tira pontos de comportamento | Pontos +/- visíveis à turma e família | Monstrinhos-avatar | Exposição pública de nota negativa | Freemium para famílias | — | Alta como **alerta** (painel do professor) |
| **Otsimo** | Crianças com TEA e outras deficiências | Jogos curtos baseados em ABA, adaptativos | Reforço imediato | Mascote simples | Baixa | Assinatura | Sem anúncios; adaptação por progresso; relatórios para pais | Média (risco de parecer clínico [IN-05]) |
| **Proloquo2Go / Avaz** | Usuários de CAA | Prancha de comunicação por símbolos | — | — | — | Compra | Código de cores Fitzgerald; posição fixa das palavras (planejamento motor) | Alta para sistema pictográfico [IN-12] |
| **EndeavorRx** | 8–17 com TDAH (prescrição) | Pilotar e desviar + coletar alvos, 25 min/dia | Progressão de mundos | Avatar piloto | Dificuldade adaptativa em tempo real; bloqueio após 30 min | Prescrição médica | — | Alta para **adaptação**; evitar tom clínico [IN-05] |
| **GraphoGame Brasil** | 4–9 | Ouvir som → tocar letra/sílaba; 57 sequências | Estrelas, mapa de aventura | Personagens simples | Baixa; recomenda até 15 min/dia | MEC (gratuito até 2021), hoje pago | Offline; origem em pesquisa sobre dislexia | Muito alta: público e política pública |
| **Elefante Letrado** | Anos iniciais (SEDUC-SP) e 6º–7º (MG) | Ler livro digital + atividades | Pontos por minuto lido → figurinhas virtuais | Elefante | Métrica de palavras por minuto | B2G | — | Alta: está na rede paulista; alerta sobre métricas de velocidade |
| **Árvore** | Fundamental | Ler livros, ganhar pontos | Floresta virtual que cresce; para de crescer após 3 dias sem ler | Otto | Pressão de sequência (floresta "parada") | B2B/B2G | — | Média |

---

## 2. Fichas por produto

### 2.1 Duolingo e Duolingo ABC
- **Público:** Duolingo principal, jovens e adultos; **Duolingo ABC**, alfabetização em inglês para 3 a 7 anos (as fontes variam entre 3–6 e "até o 1º ano").
- **Loop:** lição curta em trilha linear; cada lição tem exercícios de poucos segundos; fim de lição com celebração.
- **Recompensa:** XP, sequência diária (streak), ligas com ranking, baús. No ABC, a criança perde parte de um "coração" ao errar e recupera ao avançar; ganha recompensas ao terminar lições. Não foi encontrada evidência de streak no ABC.
- **Mascote:** Duo, coruja verde. O guia oficial de ilustração define o sistema: **tudo é construído com três formas básicas (retângulo arredondado, círculo, triângulo arredondado), sem pontas**; Duo é expressivo, tem grande variedade de poses, os pés podem se separar do corpo na animação e centralizar as pupilas é proibido "porque fica assustador". O redesenho de 2019 levou a formas geométricas e perspectiva chapada.
- **Paleta e visual:** verde-assinatura #58CC02 ("Feather Green"), fonte própria Feather Bold (Johnson Banks, 2019). Cores saturadas, chapadas, sombras sólidas deslocadas nos botões (botões "3D" chapados) **(obs.)**.
- **Tom de voz:** brincalhão, autodepreciativo, às vezes passivo-agressivo nas notificações ("meme do Duo ameaçador") **(obs.)**.
- **Acessibilidade:** ABC sem anúncios nem compras, funciona offline, áudio em tudo **(autodeclarado)**.
- **Aprender:** (1) mascote como sistema construído por formas simples, o que é exatamente o que o VUOO Bot precisa para ser fabricável em 3D [IN-13]; (2) guia de ilustração público e regrado, que permite muitos ilustradores sem perder consistência [IN-18]; (3) lição curtíssima com fechamento claro, igual aos 60–90 s do VUOO.
- **Evitar:** ligas com ranking, culpa por streak quebrado e notificações de cobrança emocional; corações que punem o erro (contaminam a medição de padrão de erro [IN-17] e geram ansiedade [IN-28]); copiar o "verde Duolingo + botão chapado com sombra", hoje o visual mais imitado de edtech.

### 2.2 Khan Academy Kids
- **Público:** 2 a 8 anos; alinhado ao Head Start e Common Core; equipe veio da Duck Duck Moose.
- **Loop:** trilha personalizada de atividades curtas (leitura, matemática, socioemocional, criatividade) + biblioteca livre.
- **Recompensa:** itens colecionáveis e roupas para os personagens **(obs.)**; baixa ênfase em placar.
- **Mascote:** **Kodi Bear**, narradora, com mais quatro animais. O ponto mais interessante: Kodi **se comunica por gestos fundamentados em pesquisa sobre gestos e desenvolvimento da linguagem**; quando a criança tem dificuldade, leva a pata ao queixo ou aponta para a cabeça, com convites gentis.
- **Paleta e visual:** ilustração em aquarela/textura suave, tons quentes e terrosos com acentos saturados, personagens arredondados de livro ilustrado **(obs.)**.
- **Tom de voz:** caloroso, de contadora de histórias, sem ironia.
- **Acessibilidade:** interface minimiza texto e privilegia ícones e animações; **todo texto é tocável e lido em voz alta**. Não há declaração formal de acessibilidade na App Store nem avaliação de terceiros.
- **Modelo:** gratuito para sempre, sem anúncios e sem assinatura.
- **Aprender:** (1) gestos do mascote como canal pedagógico, resposta direta a "mediação sem dependência de linguagem verbal" [IN-12]; (2) "todo texto tem áudio"; (3) modelo sem anúncios como sinal de confiança para escola pública.
- **Evitar:** trilha muito longa e catálogo grande que dispersam o professor; ausência de declaração de acessibilidade (o VUOO deve publicar a sua, WCAG [IN-07]).

### 2.3 Lingokids
- **Público:** 2 a 8 anos; inglês e habilidades gerais ("Playlearning").
- **Loop:** catálogo de mais de 3 a 4 mil atividades, músicas e vídeos; inclui conteúdo licenciado (Disney, Blippi, Pocoyo).
- **Recompensa:** pouco explícita nas fontes; área dos pais para acompanhar e celebrar.
- **Mascote:** **Baby Bot**, robozinho curioso "em busca de aprender tudo", com Billy (inventor), Cowy (artista), Lisa (líder) e Elliot (panda destemido).
- **Paleta e visual:** cartoon 2D vibrante, contornos limpos, fundos de cor sólida **(obs.)**.
- **Tom:** animado, de programa infantil de TV.
- **Acessibilidade:** não declarada.
- **Críticas:** Common Sense Media diz que "pode ficar caro"; pais relatam problemas com período de teste e cobranças inesperadas.
- **Aprender:** um robô aprendiz como mascote funciona; o robô que **aprende junto** com a criança é narrativa próxima do VUOO Bot "espelhar/recuar" [IN-11].
- **Evitar:** o VUOO Bot ser "mais um robozinho fofo azul": o arquétipo já está ocupado (Baby Bot, e outros). Diferenciar pela forma e pela personalidade, não pela espécie. Evitar catálogo infinito e conteúdo de TV.

### 2.4 Endless Alphabet (Originator)
- **Público:** 3 a 6 anos.
- **Loop:** cada palavra vira um quebra-cabeça: a criança arrasta letras falantes (cada letra tem som e anima ao ser tocada) até a silhueta da palavra; depois, uma animação curta e engraçada mostra o significado.
- **Recompensa:** a animação final; não há placar.
- **Mascote:** monstrinhos coloridos.
- **Falha:** o desenvolvedor afirma que não há pontuação nem estado de falha; um agregador acrescenta "sem limite de tempo" **(autodeclarado)**.
- **Visual:** monstros de formas irregulares, cores fortes, fundos limpos, muito movimento e "squash and stretch" **(obs.)**.
- **Aprender:** recompensa **intrínseca e semântica** (a animação é o conteúdo), sem economia de pontos; tocar objeto = ouvir som (tudo responde).
- **Evitar:** excesso de animação/humor pastelão para quem tem sensibilidade sensorial; precisa de controle de movimento.

### 2.5 Teach Your Monster to Read (Usborne Foundation)
- **Público:** 3 a 6 anos; desenvolvido com a Universidade de Roehampton.
- **Loop:** a criança cria o próprio monstro e o leva numa aventura de fonética; a narrativa é "ensinar o monstro a ler".
- **Recompensa:** progresso do monstro, novos lugares e itens.
- **Modelo:** compra única sem compras internas nem anúncios (app); a fundação é sem fins lucrativos.
- **Aprender:** **efeito protégé**: a criança ensina o companheiro, em vez de ser avaliada por ele. Muito alinhado ao comportamento "espelhar" do VUOO Bot [IN-11] e ao tom não avaliativo.
- **Evitar:** customização longa antes de começar (atrito em sessões de 60–90 s).

### 2.6 Toca Boca
- **Público:** 3 a 9 anos.
- **Loop:** brincadeira aberta; o app oferece parâmetros, não objetivos. O CEO afirma que "as regras são inventadas pelas crianças e mudam a cada sessão".
- **Recompensa:** nenhuma; "sem vencer, sem perder, sem estresse, sem placar, sem regras".
- **Personagens:** deliberadamente **neutros em gênero**.
- **Visual:** traço plano, formas geométricas simples, cores pastel e saturadas misturadas, humor visual, personagens com olhos grandes e proporções estranhas **(obs.)**.
- **Modelo:** historicamente sem compras internas nem anúncios (Motionographer, 2016); hoje o Toca Boca World é freemium **(obs.)**.
- **Aprender:** neutralidade de gênero e diversidade sem estereótipo; tom de "brinquedo", não de "escola"; o design permite muitos usos do mesmo objeto.
- **Evitar:** o loop aberto não serve para medir construtos [IN-16]; usar só como referência de tom e de "momento livre" entre microjogos.

### 2.7 Prodigy Math (antiexemplo de monetização)
- **Público:** 6 a 14 anos; usado em escolas, inclusive com conta do professor.
- **Loop:** RPG de batalhas; para atacar, a criança resolve contas.
- **Recompensa:** pets, itens, níveis, baús, roupas.
- **Críticas documentadas** (Fairplay e coalizão de 22 organizações, denúncia à FTC em 2021):
  - cerca de **16 anúncios de assinatura em 19 minutos, contra 4 problemas de matemática**;
  - baú brilhante bloqueado para não assinantes, que recebem anúncio;
  - **marcadores de status**: assinantes andam em nuvens e usam distintivos, não assinantes andam na terra; amigos veem quem assina ("Wizard Watch");
  - assinantes ganham mais estrelas e níveis pelas mesmas tarefas;
  - shopping, roletas, pets, danças e chat como distrações;
  - promessa ao professor de que é "e sempre será gratuito" enquanto pressiona a criança em casa; os benefícios pagos valem também na escola, aumentando desigualdade.
- **Aprender:** o engajamento alto vem do RPG e da coleção, não da matemática. Serve para medir o risco de **"engajamento sem substância"** que a proposta do VUOO já critica no Duolingo [IN-14].
- **Evitar (regras para o VUOO):** nenhum item visível que diferencie crianças (por pagamento, por desempenho ou por perfil, reforçando [IN-04]); nenhuma moeda que compita com a tarefa; nenhum pedido para a criança "pedir aos pais"; proporção tempo de tarefa / tempo de menu alta e medida.

### 2.8 Matific
- **Público:** 4 a 12 anos; oferecido gratuitamente pela SEDUC-SP (fontes divergem entre anos iniciais e 6º–9º). Estudo acadêmico relata **duas atividades semanais obrigatórias**, usando aulas de Orientação de Estudos.
- **Loop:** "episódios", famílias de minitarefas manipulativas (arrastar, agrupar, medir), com trilha adaptativa definida por teste inicial e avaliações formativas.
- **Recompensa:** baú em três níveis para incentivar repetir e dominar; itens de avatar; metas e conquistas.
- **Painel do professor:** visão ao vivo da turma, por grupo ou aluno; atribuição de tarefas; relatórios por aluno e turma.
- **Visual:** cenários 3D-cartoon/2D limpos, manipulativos grandes, interface com pouco texto **(obs.)**.
- **Aprender:** é o **comparador mais direto do VUOO na rede paulista**: o professor já conhece esse formato de "episódio curto + painel ao vivo". Baú que premia **domínio** (repetir até acertar bem) é melhor do que baú que premia volume.
- **Evitar:** parecer "mais um Matific"; obrigatoriedade como motor de uso (o VUOO precisa de motivo intrínseco); painel que mostra só desempenho, sem leitura pedagógica acionável [IN-22]. Um revisor notou que os alunos ficavam mais focados quando o tempo de uso era limitado ao previsto, o que reforça sessões curtas.

### 2.9 Kahoot! (alerta sobre tempo e ranking)
- **Público:** todas as idades; uso coletivo projetado.
- **Loop:** pergunta na tela → resposta no aparelho → placar → pódio.
- **Recompensa:** pontos por acerto **e velocidade**, pódio, música.
- **Evidências:** estudos financiados ou divulgados pela empresa mostram baixa ansiedade em contexto de baixo risco; estudos independentes apontam que tempo e ranking geram ansiedade; **alunos quietos e tímidos de todos os níveis não ficam confortáveis com pontuação pública, e alunos da educação especial com boa percepção social ficam envergonhados com suas notas** (Montana State). No fórum de suporte, a empresa confirma que **não é possível desligar o timer** no jogo ao vivo, só aumentar o tempo.
- **Visual:** roxo forte, formas geométricas (triângulo, losango, círculo, quadrado) com cor **e** forma para cada alternativa **(obs.)**.
- **Aprender:** associar **forma + cor** a cada alternativa (não depende só de cor, bom para daltonismo e pré-leitores); energia de momento coletivo.
- **Evitar:** pontuação por velocidade (contamina tempo de reação [IN-17]); timer visível obrigatório; pódio. Se o VUOO tiver momento coletivo [IN-19], ele deve ser cooperativo (meta da turma), sem ranking individual [IN-26].

### 2.10 ClassDojo (alerta sobre o painel do professor)
- **Público:** professores, alunos e famílias do fundamental.
- **Loop:** professor dá pontos positivos e negativos de comportamento; a família vê.
- **Mascote:** monstrinhos-avatar coloridos para cada aluno.
- **Visual:** monstrinhos arredondados, verde-água e cores primárias, interface muito amigável **(obs.)**.
- **Críticas:** pesquisa da University of South Australia (Manolev) diz que reduz comportamento a números, normaliza e intensifica a vigilância e promove disciplina "arcaica", comparando-a ao crédito social chinês; relatos de **pontos anunciados em público que humilham a criança** e de placares exibidos a pais em evento escolar; a crítica behaviorista (Alfie Kohn) diz que recompensa e punição são "dois lados da mesma moeda". A maior parte é opinião ou estudo qualitativo, sem experimento controlado.
- **Aprender:** visual simpático aplicado a um painel de adulto cria adesão de professores e famílias.
- **Evitar:** qualquer número de "comportamento" ou desempenho da criança visível aos colegas; painel que vira ferramenta de vigilância. O painel do VUOO deve falar de **sinais pedagógicos e próximos passos**, não de pontuação, alinhado a [IN-04] e [IN-21].

### 2.11 Otsimo
- **Público:** crianças com TEA, síndrome de Down e outras deficiências do desenvolvimento.
- **Loop:** jogos curtos (palavras, números, cores, emoções) baseados em ABA; algoritmo adapta cada exercício ao progresso; várias mecânicas para o mesmo conteúdo.
- **Recompensa:** reforço imediato **(obs.)**.
- **Acessibilidade:** sem anúncios para evitar distração; gráficos diários, semanais e mensais para os pais; app de CAA à parte com 1.700 palavras e modelagem por vídeo.
- **Visual:** ilustração plana, fundos limpos, poucos elementos por tela **(obs.)**.
- **Aprender:** ensinar o mesmo conteúdo com mecânicas diferentes (generalização); poucos estímulos por tela.
- **Evitar:** enquadramento ABA/terapêutico e "app para autista": contradiz [IN-02], [IN-04] e [IN-05]. O VUOO deve ter a mesma clareza sensorial **para a turma toda**, sem rótulo.

### 2.12 Proloquo2Go e Avaz (CAA)
- **Público:** pessoas com comunicação complexa (CAA).
- **Princípios de design:** **código de cores Fitzgerald** (1954; verde para ações, azul para adjetivos, na variação do Avaz), adotado pela comunidade de CAA e publicado pelo ARASAAC; **posição fixa das palavras** para criar memória motora (Proloquo2Go Crescendo; Avaz com "layout e padrões motores consistentes entre níveis").
- **Aprender:** (1) se o VUOO Bot usar pictogramas [IN-12], seguir convenções de CAA já conhecidas pelas professoras de AEE (ARASAAC, Fitzgerald) em vez de inventar uma iconografia; (2) **botões e controles sempre no mesmo lugar** entre microjogos, princípio de planejamento motor útil para DCD e TEA.
- **Evitar:** importar a densidade de uma prancha de CAA; o VUOO precisa de poucos símbolos por tela.

### 2.13 EndeavorRx (Akili)
- **Público:** 8 a 17 anos com TDAH, sob prescrição; autorizado pela FDA em 2020 (inicialmente 8–12), com dados de 5 estudos e mais de 600 crianças.
- **Loop:** pilotar um veículo desviando de obstáculos enquanto coleta alvos (atenção seletiva e multitarefa) **(obs. sobre a mecânica)**.
- **Adaptação:** o algoritmo SSME **ajusta dificuldade e velocidade em tempo real** para manter a criança "nos limites de desempenho predefinidos" de cada indivíduo.
- **Dose:** cerca de 25 min/dia, 5 dias/semana, por 4 semanas; **bloqueio após 30 min diários**. Não é tratamento isolado.
- **Visual:** mundos 3D coloridos, estética de videogame comercial **(obs.)**.
- **Aprender:** (1) adaptação contínua dentro de faixa-alvo, que é exatamente o "provocar/recuar" do VUOO Bot [IN-11]; (2) limite diário explícito como característica de projeto, não falha; (3) é possível ter rigor de medida e estética de jogo ao mesmo tempo.
- **Evitar:** linguagem de prescrição, tratamento e "dose": [IN-05] proíbe parecer clínico. Traduzir para "rotina", "missão do dia".

### 2.14 GraphoGame Brasil (MEC / Tempo de Aprender)
- **Público:** 4 a 9 anos; lançado pelo MEC em nov/2020 dentro do Tempo de Aprender; adaptado pelo Instituto do Cérebro do RS (PUCRS); origem finlandesa, criado inicialmente para crianças com dislexia.
- **Loop:** ouvir um som e tocar a letra ou sílaba correspondente; 57 sequências com fases.
- **Modos:** "Estrelas", para uso escolar; "Mapa da Aventura", livre.
- **Uso recomendado:** **no máximo 15 minutos por dia**.
- **Acessibilidade e contexto:** **funciona offline** (internet só para baixar); sem anúncios.
- **Polêmica:** usado politicamente em 2022 (promessa de alfabetizar em seis meses, sem evidência apresentada); deixou de ser gratuito e hoje custa R$ 24,90 no iPad.
- **Visual:** simples, funcional, pouco autoral **(obs.)**.
- **Aprender:** offline e sessões curtas como requisitos da escola pública brasileira [IN-07]; modo escola separado do modo livre; base científica como argumento.
- **Evitar:** estética genérica e pouco cuidada (chancela científica sem cuidado visual não gera vínculo); dependência de um único governo ou programa para a marca; promessas de resultado.

### 2.15 Elefante Letrado
- **Público:** anos iniciais na SEDUC-SP; 6º e 7º ano em MG (108 mil alunos); Porto Alegre desde 2017.
- **Loop:** biblioteca digital + atividades de compreensão + leitura oral.
- **Recompensa:** **cada minuto de leitura gera pontos trocados por figurinhas virtuais** ("álbuns digitais" na rede paulista); a SEDUC-SP reporta aumento de 10% no tempo semanal de leitura (dado oficial, sem avaliação independente).
- **Painel:** professores acompanham o progresso em tempo real; relatórios de desempenho.
- **Críticas:** Le Monde Diplomatique Brasil ("Um elefante nem tão letrado"): "gamificação banalizada que premia a velocidade em detrimento da reflexão desumaniza o ato de ler"; Entretextos (2026) critica a métrica de fluência baseada em velocidade de leitura oral e a leitura mecanizada.
- **Aprender:** **álbum de figurinhas** é um mecanismo de coleção culturalmente brasileiro, que funciona na rede paulista e não depende de ranking.
- **Evitar:** premiar tempo ou velocidade (efeito contrário ao que se quer medir [IN-17]); tratar a métrica de máquina como verdade pedagógica no painel.

### 2.16 Árvore
- **Público:** ensino fundamental; mais de 11 mil escolas, maioria pública **(autodeclarado)**.
- **Loop:** ler livros, ganhar pontos.
- **Recompensa:** **a pontuação faz crescer uma floresta virtual; se a criança fica três dias sem ler, a floresta para de crescer.** Olimpíada de leitura com classificação estadual.
- **Mascote:** Otto.
- **Painel:** professor indica livros e acompanha uso em relatórios.
- **Aprender:** metáfora de **crescimento cumulativo** (algo que cresce com o uso) em vez de pontos abstratos; boa ponte com "trajetória" [IN-32].
- **Evitar:** consequência negativa por ausência (punir quem não tem aparelho ou internet em casa é questão de equidade); competição entre escolas e alunos.

### 2.17 Referência institucional: Governo de SP / SEDUC-SP
- **O que existe:** a SEDUC-SP oferece um conjunto de plataformas pela **Sala do Futuro** (2023): Tarefa SP, Khan Academy, Matific, Leia SP, Elefante Letrado, Alura, Redação Paulista, SPeak e outras. Não há manual de marca específico da SEDUC; vale o **Manual de Identidade Visual do Governo do Estado de SP** (abr/2023, revisão 05/2024), lançado com as cores da bandeira paulista (preto, branco, vermelho) e o mote "São Paulo são todos", com fotos de pessoas.
- **Implicação:** cada plataforma da Sala do Futuro mantém a própria identidade; o VUOO vai conviver lado a lado com Matific e Elefante Letrado na mesma tela de acesso. A identidade não pode parecer de governo [IN-30], mas precisa caber ao lado do selo do Governo de SP sem conflito (evitar vermelho/preto/branco como cores primárias, que lembrariam a marca estadual).
- **Fonte relacionada:** InternetLab (2026) analisa as plataformas digitais na educação pública paulista, com potencialidades e desafios (vale ler na íntegra para riscos de dados [IN-29]).

---

## 3. O "visual genérico" de edtech infantil: 4 padrões a evitar

1. **Mascote-animal-fofo + cor primária chapada.** Coruja verde, urso, elefante, panda, monstrinho colorido, robozinho azul de olhos grandes. O espaço está saturado: Duo, Kodi, Elliot, Baby Bot, os monstros do ClassDojo, Endless Alphabet e Teach Your Monster, o Elefante Letrado. Um VUOO Bot "robô fofo azul com olhos de tela" fica indistinguível. **(obs.)**
2. **"Duolingo-like": botões arredondados com sombra sólida deslocada, verde/azul/amarelo saturados, tipografia sem serifa arredondada e pesada, confete na tela de vitória.** Virou o template do mercado. Funciona, mas apaga a marca. **(obs.)**
3. **Economia de brilho: baús, moedas, gemas, estrelas douradas, roletas, raios de luz.** Comunicam "loot" e cassino. Em Prodigy viraram ferramenta de pressão comercial; em Matific e Elefante Letrado são o motor de uso. Para o VUOO, além de genérico, contaminam a medição [IN-17].
4. **Painel do professor "dashboard SaaS" com semáforo vermelho/amarelo/verde e ranking da turma.** Herda a lógica do ClassDojo e do Kahoot: pontua e expõe a criança. Professores com baixo letramento digital [IN-22] leem só a cor, e o vermelho vira rótulo [IN-04]. **(obs.)**

(Um quinto padrão menor: **cenário "escola de desenho animado"** com lápis, quadro-negro e mochila, que reforça que é tarefa e não brincadeira.)

---

## 4. Oportunidades de diferenciação para o VUOO

1. **Bot que aprende com a criança, não que a avalia.** Combinar o efeito protégé do Teach Your Monster e o Baby Bot "aprendiz" com os gestos da Kodi Bear: o VUOO Bot espelha, provoca, celebra e recua [IN-11] por **corpo, olhos e luz**, sem texto. Forma construída com 3–4 primitivas (como o sistema do Duo), o que garante animação consistente **e** impressão 3D [IN-13]. Diferenciar pela forma (algo que voa, coerente com "VUOO" e "trajetória" [IN-32]) e não pela espécie.
2. **Recompensa intrínseca e de trajetória, não economia de loot.** A animação de fim de microjogo mostra o **efeito** da ação (como Endless Alphabet), e o progresso aparece como **trajetória/rota de voo que se alonga** (crescimento cumulativo como na floresta da Árvore, mas **sem perda por ausência**). Coleção ao estilo do álbum de figurinhas brasileiro é aceitável se for igual para todos e não comprável. Nada de bônus por velocidade.
3. **Clareza sensorial universal (DUA), sem rótulo.** Poucos elementos por tela, controles em posição fixa entre jogos (lição da CAA), forma + cor em cada opção (lição do Kahoot), áudio em todo texto (Khan Kids), controle de movimento e som para todos, sem modo "especial" que identifique a criança [IN-04]. Publicar uma declaração de acessibilidade WCAG, coisa que nenhum concorrente analisado faz de forma clara.
4. **Coletivo cooperativo em vez de ranking.** Onde Kahoot e ClassDojo expõem, o VUOO pode ter "meta da turma" (a turma toda faz o Bot voar mais longe), resolvendo a tensão de [IN-19] e [IN-26].
5. **Painel do professor como conversa, não semáforo.** "O que observei → o que sugiro amanhã", com evidência recuperável [IN-21], linguagem simples [IN-22], sem nota de comportamento e sem vermelho como rótulo.
6. **Identidade brasileira, pública e calorosa.** Nenhum concorrente da rede paulista tem uma linguagem visual autoral brasileira; os brasileiros (GraphoGame, Elefante Letrado) são funcionais e pouco cuidados. Há espaço para paleta e ilustração com referências locais (cores de céu e cidade de SP, texturas de papel e guache de sala de aula) longe tanto do vermelho/preto do Governo de SP quanto do verde/azul saturado do "Duolingo-like".
7. **Offline, curto e com limite como virtude.** GraphoGame (15 min/dia) e EndeavorRx (bloqueio a 30 min) tornam o limite parte do produto. O VUOO pode comunicar "uma missão por dia, curtinha" como marca, oposto do engajamento infinito.

---

## 5. Fontes

### Duolingo / Duolingo ABC
- https://design.duolingo.com/illustration
- https://design.duolingo.com/illustration/duo
- https://design.duolingo.com/illustration/characters
- https://www.designweek.co.uk/issues/2-6-january-2019/duolingo-owl-receives-makeover-as-app-becomes-more-gamified
- https://www.creativereview.co.uk/duolingo-rebrand-johnson-banks/
- https://www.creativebloq.com/news/feather-bold
- https://madegooddesigns.com/duolingo-brand-guidelines/
- https://imaginationsoup.net/duolingo-abc-literacy-app/
- https://www.cultofmac.com/696695/duolingo-abc-teaches-kids-to-read-free/
- https://apptopia.com/google-play/app/com.duolingo.literacy/about

### Khan Academy Kids
- https://blog.khanacademy.org/supporting-english-language-acquisition-with-khan-academy-kids/
- https://learn.khanacademy.org/khan-academy-kids/
- https://apps.apple.com/us/app/khan-academy-kids/id1378467217
- https://www.familygamingdatabase.com/accessibility/Khan+Academy+Kids
- https://apkmirror.com/apk/khan-academy/khan-academy-kids/khan-academy-kids-2-0-release

### Lingokids
- https://lingokids.com/lingokids-universe-old-2023
- https://help.lingokids.com/hc/en-us/articles/205124321-What-is-Lingokids
- https://www.commonsensemedia.org/app-reviews/lingokids-play-and-learn
- https://www.commonsensemedia.org/app-reviews/lingokids-play-and-learn/user-reviews/adult

### Endless Alphabet
- https://apps.apple.com/app/id591626572
- https://mwm.ai/apps/endless-alphabet/591626572

### Teach Your Monster to Read
- https://theliteraryplatform.com/news/2014/09/teach-your-monster-to-read/
- https://apps.apple.com/us/app/teach-your-monster-to-read/id828392046

### Toca Boca
- https://motionographer.com/2016/04/27/the-design-process-behind-toca-bocas-infectious-apps/
- https://kidscreen.com/?p=59849
- https://readwriterespond.com/2018/02/toca-boca/

### Prodigy Math
- https://fairplayforkids.org/pf/prodigy/
- https://fairplayforkids.org/?p=26304
- https://www.mediapost.com/publications/article/360719/ftc-urged-to-investigate-prodigy-math-game-over-al.html
- https://en.wikipedia.org/wiki/Prodigy_Education
- https://fairplayforkids.org/wp-content/uploads/2021/10/2021-Annual-report.pdf

### Matific
- https://www.matific.com/us/en-us/home/product-features/
- https://mindsharelearning.ca/?p=13582
- https://www.teachprimary.com/tried_and_tested/view/matific

### Kahoot!
- https://scholarworks.montana.edu/server/api/core/bitstreams/6a157b0b-fc8c-49a5-a035-28976b1f8744/content
- https://par.nsf.gov/servlets/purl/10284492
- https://ejournal.upi.edu/index.php/tegar/article/download/92888/pdf
- https://support.kahoot.com/hc/en-us/community/posts/33338883797395-Disable-timer-for-live-host-Kahoot
- https://kahoot.com/blog/2025/07/17/kahoot-impact-research-academic-stress/ (fonte da própria empresa)

### ClassDojo
- https://theconversation.com/digitally-tracking-student-behaviour-in-the-classroom-encourages-compliance-not-learning-110181
- https://educationhq.com/news/classdojo-harms-teachers-behaviour-management-approach-researcher-188825/
- https://www.ellaslist.com.au/articles/this-school-app-is-controlling-and-sending-out-the-wrong-message-to-students-says-research
- https://new.principalcenter.com/what-do-you-think-of-classdojo-pbis-rewards-and-behavior-points-systems

### Otsimo
- https://apps.apple.com/us/app/id1475410615
- https://www.badcredit.org/news/otsimo-offers-game-based-special-education-apps/
- https://eastersealstech.com/2023/09/07/otsimo-aac-app
- https://ubwp.buffalo.edu/happe/2021/01/13/otsimo/

### Proloquo2Go / Avaz / CAA
- https://www.closingthegap.com/wp-content/uploads/2020/transcripts/WCT_Webinar123_Avaz2018.pdf
- https://www.assistiveware.com/support/proloquo2go/appearance/color-code-page-background
- https://aulaabierta.arasaac.org/en?p=67992

### EndeavorRx
- https://intuitionlabs.ai/software/telepsychiatry-digital-mental-health/digital-therapeutics-prescription-apps/endeavorrx
- https://psychnews.psychiatryonline.org/doi/10.1176/appi.pn.2020.8a5
- https://www.biospace.com/fda-approves-akili-s-therapeutic-video-game-for-adhd
- https://accessgudid.nlm.nih.gov/devices/00850002639018

### GraphoGame Brasil
- https://apps.apple.com/BR/app/id1540637587
- https://www.gazetadopovo.com.br/educacao/poucas-escolas-nao-tem-internet-diz-ministro-da-educacao-em-lancamento-de-app-de-alfabetizacao/
- https://www.cartacapital.com.br/?p=303339
- https://sol.sbc.org.br/index.php/sbie/article/download/26711/26530

### Elefante Letrado
- https://www.correiodamanha.com.br/nacional/sao-paulo/estado-de-sao-paulo/2026/06/amp/296225-albuns-digitais-impulsionam-leitura-na-rede-paulista.html
- https://diplomatique.org.br/o-curioso-caso-de-uma-plataforma-de-leitura-que-transforma-a-literatura-em-caixas-quadradas/
- https://ojs.uel.br/revistas/uel/index.php/entretextos/article/download/54799/54352/316192
- https://acervodigital.ufpr.br/xmlui/handle/1884/100211
- https://periodicos.feevale.br/seer/index.php/revistaconhecimentoonline/article/view/1868

### Árvore
- https://www.mobiletime.com.br/noticias/11/02/2021/arvore-plataforma-da-acesso-a-livros-digitais-para-1-milhao-de-estudantes-brasileiros/
- https://www.agazeta.com.br/educares/gamificacao-na-educacao-jogos-viram-trunfo-na-sala-de-aula-1122
- https://sol.sbc.org.br/index.php/semiedu_estendido/article/view/21066
- https://apps.apple.com/BR/app/id1094879125

### SEDUC-SP / Governo de SP
- https://abcdoabc.com.br/rede-estadual-12-plataformas-estudantes/
- https://www.bnewssaopaulo.com.br/amp/noticias/politica/sala-do-futuro-conheca-a-nova-plataforma-de-ensino-usada-nas-escolas-de-sp.html
- https://revista.internetlab.org.br/wp-content/uploads/2026/01/Plataformas-digitais-na-educacao-publica-paulista_-entre-potencialidades-e-desafios.pdf
- https://revistas.uece.br/index.php/BOCEHM/article/download/13712/12964/65278
- https://sigam.ambiente.sp.gov.br/sigam3/repositorio/559/documentos/Anexo%206%20do%20MPO%20-%20Manual%20de%20Comunicacao%20do%20Governo_05.2024.pdf
- https://publicidadelegal.gazetasp.com.br/wp-content/uploads/2023/03/pl_import_687d3b7d80669_gsp-04a060323-certificado-5.pdf
- https://semil.sp.gov.br/ambientenet/2023/05/a-semil-esta-com-uma-nova-aparencia/

### Design para TEA e neurodivergência (geral)
- https://journals-sol.sbc.org.br/index.php/rbie/article/download/7245/4201/43075
- https://sol.sbc.org.br/index.php/sbgames_estendido/article/download/45906/45667/
- https://repositorio.ipv.pt/entities/publication/95a2f6f8-3ba8-49e0-90d2-62e17639687b

### Instituto Ayrton Senna (pesquisado, sem jogo digital próprio encontrado)
- https://institutoayrtonsenna.org.br/app/uploads/2023/10/Materiais-Instituto-Ayrton-Senna.pdf
- https://institutoayrtonsenna.org.br/app/uploads/2022/11/instituto-ayrton-senna-as-competencias-socioemocionais-no-cotidiano-das-escolas.pdf

---

## 6. Limitações e próximos passos
- Paleta, traço e tom marcados como **(obs.)** precisam de captura de tela de cada app (sugestão: um painel de referência visual com 3 telas por produto).
- Nenhum concorrente publica avaliação de acessibilidade; não foi possível comparar recursos como contraste, tamanho de alvo ou leitor de tela sem testar os apps.
- A faixa de uso da Matific na SEDUC-SP diverge entre fontes; confirmar na Sala do Futuro.
- Ler na íntegra o relatório do InternetLab (2026) sobre plataformas na rede paulista, provável leitura dos mesmos gestores que vão avaliar o VUOO.
