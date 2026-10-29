# Teardown do sistema de engajamento do Duolingo — insumo para a linguagem de produto do VUOO

> Pesquisa documental feita em 27/10/2026. Objetivo: entender cada mecânica de engajamento do Duolingo (e de Duolingo ABC/Math, no que for relevante para crianças), por que funciona, o que se sabe em números, e qual o risco de copiá-la para crianças de 6 a 11 anos neurodivergentes (TEA, TDAH, dislexia, DCD) numa turma inteira da rede pública de SP.

## Como ler este documento

Cada afirmação traz uma marca de confiança:

- **[V]**: verificado em fonte primária (blog oficial do Duolingo, artigo acadêmico, relação com investidores) ou em entrevista com gente do Duolingo.
- **[S]**: fonte secundária (imprensa, análise de UX, wiki de fãs, análise de terceiros). Plausível, mas não confirmado pela empresa.
- **[I]**: inferência minha ou observação de uso do produto que não verifiquei nesta pesquisa. Trate como hipótese.

Cuidados gerais:
1. Quase todos os números de impacto vêm do próprio Duolingo, são **variações relativas** de testes A/B (por exemplo, "+3,3% de retenção no D14" quer dizer 3,3% a mais que o controle, não 3,3 pontos percentuais) e medem **retenção ou engajamento, não aprendizagem**.
2. O público do Duolingo é adolescente e adulto. Os termos de uso exigem 13 anos ou mais para conta padrão [S, Common Sense Media]. **Nenhuma** das métricas abaixo foi medida com crianças de 6 a 11 anos, e menos ainda com crianças neurodivergentes.
3. O produto muda o tempo todo; o Duolingo diz ter feito mais de 600 experimentos só com a ofensiva [V]. O que vale hoje pode não valer amanhã.

---

## 0. A tese do crescimento: por que o Duolingo virou uma máquina de hábito

- **O que é:** entre ~2018 e 2022, o time de produto, liderado por Jorge Mazal (ex-CPO), montou um modelo de crescimento e descobriu que a alavanca de maior impacto em usuários ativos diários (DAU) era a **CURR (Current User Retention Rate)**: a chance de um usuário que está ativo continuar ativo amanhã. Na definição do Duolingo, "usuário atual" é quem usou o app hoje e pelo menos uma vez nos 6 dias anteriores [V].
- **Números:** na simulação, mexer na CURR teve cerca de **5x** o impacto em DAU da segunda melhor alavanca [V]. A CURR subiu **21%** em 4 anos, e o churn diário dos melhores usuários caiu **mais de 40%** [V]. O DAU cresceu **4,5x** em 4 anos [V].
- **Implicação:** quase toda a gamificação descrita abaixo (ligas, ofensiva, notificações) foi otimizada para **voltar todo dia**, e não para aprender mais em cada sessão. Mais tarde o Duolingo criou uma métrica de "aprender bem" para compensar esse viés (seção 13).
- **Risco para crianças neurodivergentes:** o VUOO é usado **na escola, mediado pelo professor**. Retenção diária fora do horário de aula não é um objetivo legítimo para uma criança de 7 anos e também não é o modelo de negócio do VUOO. Importar o objetivo "DAU/CURR" traz junto todo o arsenal de pressão. **[I]** A métrica norteadora do VUOO deve ser outra, por exemplo "microjogos concluídos com sucesso por criança e por semana" e "habilidades consolidadas".

Fontes:
- https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth
- https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks

---

## 1. Loop central da lição

### O que é
- A **lição** é uma sequência curta de exercícios de formatos variados: tocar a tradução, montar a frase com blocos de palavras, ouvir e escrever, falar, ligar pares. **[S]** O número de exercícios varia: errar um item faz ele (ou um equivalente) voltar no fim da lição (Duolingo Wiki). **[I]** Pela observação de uso, uma lição típica tem por volta de 10 a 15 exercícios e leva 2 a 5 minutos. Usuários estimam "2,5 a 3 minutos por lição" [S].
- **Feedback de cada resposta [I, observação de uso]:** a pessoa responde e aperta "Verificar". Uma faixa sobe do rodapé: **verde** com um elogio curto e um som ascendente em caso de acerto; **vermelha** com a resposta correta e um som descendente em caso de erro. O botão vira "Continuar". Contador de **combo** em acertos seguidos. A **barra de progresso** no topo enche a cada item.
- **Som [S]:** "chime saltitante" no acerto, "tom descendente e murcho" no erro, descrito como "desanimador o bastante para você querer acertar a próxima, mas não tão duro a ponto de gerar ansiedade" (newsletter Out of Scope). Não encontrei documentação oficial de sound design.
- **Personagens dentro do exercício [V]:** os 10 "World Characters" falam as frases com sincronização labial em tempo real (Rive + visemas), piscam e balançam a cabeça enquanto esperam, e têm um **estado final de reação** conforme a resposta esteja certa ou errada.
- **Revisão de erros:** no sistema Energy, revisar os erros no fim da lição **não gasta energia** [V].
- **Tela de fim de lição [I, observação]:** animação comemorativa com personagem, XP ganho, precisão (%) e tempo. Depois vêm telas encadeadas: progresso da ofensiva, missões diárias, posição na liga, às vezes um baú. Em 2025 o Duolingo anunciou "novas animações para as telas de fim de lição" e trocou o rótulo "exercício difícil" pelo personagem **Eddy**, que comemora lições perfeitas [V].

### Por que funciona
- **Ciclo curto de esforço, feedback imediato e progresso visível:** feedback imediato e frequente é especialmente eficaz para quem tem pouca tolerância à espera (veja TDAH abaixo). **[I]** A barra de progresso é um "efeito de progresso dotado": ver o quanto falta reduz a desistência.
- **Clareza visual como requisito de aprendizagem [V]:** o diretor de arte do Duolingo diz que um visual pouco claro leva o aprendiz a errar ou se perder, e que "nossa falha vira a falha do aprendiz".

### Números conhecidos
- Lições do caminho são a unidade de valor: um estudo independente citado pelo Duolingo diz que "o número de lições concluídas foi o preditor mais forte de ganho de aprendizagem" [V, citado pelo Duolingo].
- O XP por lição já foi cerca de 10 e hoje gira em torno de 25, mais bônus de combo e boosts [S, duoplanet].

### Risco para crianças neurodivergentes
- **Dislexia:** a faixa de erro mostra **texto** com a resposta correta e exige leitura rápida, num momento de frustração. **[I]** No VUOO, o feedback precisa ser **multimodal e não textual**: áudio narrado, a resposta correta demonstrada em animação, ícone.
- **TEA:** o som descendente e o vermelho são sinais aversivos e pouco previsíveis em intensidade. Para crianças com hipersensibilidade auditiva, sons altos, sobrepostos e com timbres "de erro" causam desconforto. **[I]** Sugestão: volume de efeitos separado da narração, opção de silenciar, erro sinalizado com cor neutra (âmbar ou azul, nunca vermelho) e som suave e não punitivo.
- **TDAH:** o loop curto funciona bem. Mas o **encadeamento de telas pós-lição** (XP, ofensiva, missão, liga, baú) é uma cascata de estímulos que pode desregular a criança e roubar o tempo de transição. **[I]** No VUOO: **uma** tela final, curta, com um único reforço e um único próximo passo.
- **DCD (dispraxia):** exercícios de arrastar blocos e de digitar exigem precisão motora. **[I]** Alvos grandes (≥ 48–64 px), tocar em vez de arrastar como alternativa, sem limite de tempo por item.
- **Repetir o item errado no fim** é boa pedagogia (prática de recuperação). **[I]** Mas para a criança que erra muito, a lição "não acaba nunca". Defina um teto de itens extras.

Fontes:
- https://duolingo.fandom.com/wiki/File:Basics1_Lesson.png (wiki, estrutura da lição)
- https://out-of-scope-product.beehiiv.com/p/duolingo-has-it-venmo-has-it-even-slack-has-it-your-product-doesn-t (sons)
- https://blog.duolingo.com/world-character-visemes (personagens nos exercícios)
- https://blog.duolingo.com/duolingo-energy/ (revisão de erros grátis)
- https://blog.duolingo.com/product-highlights/ (Eddy, animações de fim de lição)
- https://blog.duolingo.com/shape-language-duolingos-art-style/ (clareza visual)
- https://blog.duolingo.com/time-spent-learning-well/ (lições concluídas como preditor)
- https://newsletter.duoplanet.com/posts/has-duolingo-finally-fixed-xp (XP)

---

## 2. XP (pontos de experiência)

### O que é
- Pontos ganhos por concluir lições e práticas. Alimentam a **meta diária** (opcional), as **ligas** semanais e as **missões**. Existem **XP Boosts** (XP em dobro por alguns minutos) como recompensa, válidos em todos os cursos [V, blog].

### Por que funciona
- Moeda de esforço unificada e comparável, que liga todos os subsistemas (liga, missão, meta). **[I]**

### Números e evidências
- **O XP distorce o comportamento.** O Duolingo constatou que o XP incentivava "farmar" atividades fáceis. Ao **dar mais XP para lições do caminho** nas ligas, ganhou **+1,1 milhão de minutos/dia** com um ajuste parcial e **+1,8 milhão de minutos/dia** com o ajuste completo de "tempo aprendendo bem" [V].
- **Ligar a ofensiva ao XP confundia os usuários.** Simplificar a regra para "uma lição por dia" tornou a ofensiva mais eficaz [V, entrevista com o PM de retenção].

### Risco para crianças neurodivergentes
- **[I]** O XP só tem sentido em comparação (liga) ou acumulação (número que cresce). Para uma criança de 6 a 8 anos, números grandes e abstratos têm pouco significado, e **comparar** é o principal vetor de dano (seção 6).
- **[I]** O XP premia **volume**, não domínio. Isso estimula crianças com TDAH a escolher o caminho rápido e fácil, e pune quem é mais lento por dislexia ou DCD.
- **[I]** Alternativa para o VUOO: progresso **concreto e não numérico**, como o mundo do VUOO Bot ganhando um objeto, uma planta crescendo ou um mapa se revelando. Ligado a **domínio de habilidade**, não a tempo ou quantidade.

Fontes:
- https://blog.duolingo.com/time-spent-learning-well/
- https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks
- https://blog.duolingo.com/friends-quests/ (XP Boost)

---

## 3. Ofensiva (streak), congelamento, reparo e ansiedade

### O que é
- Contador de **dias consecutivos** com pelo menos uma lição concluída [V]. Antes era preciso bater a meta diária; hoje basta uma lição [V].
- **Congelamento (Streak Freeze):** protege a ofensiva por um dia sem prática. O limite passou para **até 2 equipados ao mesmo tempo** [V]. É comprado com gemas [S].
- **Reparo (Streak Repair):** recupera uma ofensiva perdida, pago com gemas ou dinheiro [S].
- **Evento de recuperação (junho de 2026):** por tempo limitado, quem tinha perdido uma ofensiva de 30 dias ou mais podia recuperá-la **de graça fazendo 3 lições seguidas**. Só valia para a maior ofensiva perdida, e o CPO Cem Kansu atribuiu a mudança a pedidos dos usuários [S, imprensa].
- **Aposta de ofensiva (Streak Wager / Streak Challenge):** apostar gemas que vai manter a ofensiva por 7, 14 ou 30 dias [V, blog]. Um relato secundário fala em **+5% de retenção no D14** e **+600% de receita de compras internas** no teste original da aposta com lingots [S, Econsultancy].
- **Marcos e animação:** 7 dias, 30 dias, 100 dias, 1 ano. O Duo vira uma **fênix em chamas**, porque o "on fire" não era entendido em todas as culturas. O marco foi desenhado como um "power-up de videogame" e vem com um card para compartilhar [V].
- **Ofensiva com amigos (Friend Streak):** ofensiva compartilhada com até 5 amigos [V].
- **Notificação "salva-ofensiva":** um aviso no fim da noite para quem está prestes a perder a ofensiva. Foi a "primeira grande vitória" do time de retenção [V].
- **BRB:** protege ofensivas durante quedas do servidor; já protegeu mais de 2 milhões [S].

### Por que funciona (psicologia citada pelo Duolingo)
- **Formação de hábito:** repetir um comportamento no mesmo contexto o torna automático. O Duolingo cita um estudo da APA de 1998 [V].
- **Aversão à perda:** o medo de perder uma ofensiva longa faz a pessoa praticar em dias em que pularia. **O próprio Duolingo admite o lado negativo:** perder a ofensiva pode **reduzir a motivação**, e usuários **evitam desafios** para não arriscar a ofensiva [V].
- **Os primeiros dias valem mais:** passar de 2 para 3 dias é +50%; de 200 para 201 é +0,5%. Por isso as telas investem nos primeiros dias [V].
- **Flexibilidade aumenta a motivação:** o Duolingo cita estudos da Penn e da UCLA para justificar o congelamento [V].
- **Pesquisa acadêmica independente:** Silverman & Barasch (2023, *Journal of Consumer Research*, 7 estudos) mostram que uma ofensiva **intacta** aumenta o engajamento futuro, mas uma ofensiva **quebrada** leva ao **abandono**, mesmo com o mesmo comportamento real. O efeito é **mais forte quando a pessoa culpa a si mesma** e **mais fraco quando dá para reparar**. As autoras recomendam **evitar notificações do tipo "você quebrou sua ofensiva"** e lembram que "o que conta como sequência é maleável" [V].

### Números conhecidos (todos do Duolingo, variações relativas)
| Mudança | Resultado |
|---|---|
| Separar a meta diária da ofensiva | **+3,3%** retenção D14; **+1%** DAU; **+10,5%** aprendizes com ofensiva (**+19%** entre novos) [V] |
| Permitir 2 congelamentos | **+0,38%** DAU [V] |
| Nova animação de marco | **+1,7%** retenção D7 de novos usuários [V] |
| Um ano de otimização | Pouco mais da metade do DAU com ofensiva de 7+ dias (era ~1/3); **+40%** usuários com 7+ dias [V] |
| Quem chega a 7 dias de ofensiva | **2,4x** mais chance de voltar no dia seguinte [V]; **3,6x** mais chance de concluir o curso [V, pesquisa interna] |
| Trocar o botão "continuar" por "me comprometo com a meta" | Aumento "significativo" de retenção, sem número publicado [V] |
| Ofensiva de 10 dias | Queda "substancial" de abandono, com o próprio Mazal ressalvando **viés de seleção** [V] |

Atenção: "quem tem ofensiva de 7 dias volta mais" é correlação. Gente mais motivada faz ofensivas longas.

### Críticas
- Guias para pais relatam choro e "colapsos" de crianças ao perder a ofensiva ou receber notificação da liga, e falam de "ansiedade de ofensiva" quando o motivo para abrir o app passa de "quero aprender" para "tenho medo de perder" [S, anedótico].
- Caso público: o Duolingo **restaurou a ofensiva de 301 dias de um menino de 10 anos hospitalizado**. Mostra o peso emocional que uma criança dá ao contador [S, IBTimes].
- O dado de que **2 congelamentos dão só +0,38% de DAU** e as campanhas de "recuperação" sugerem que a **perda** da ofensiva é uma fonte relevante de churn e frustração [I].

### Risco para crianças neurodivergentes: ALTO
- **A ofensiva diária pressupõe acesso diário**, mas o VUOO acontece na escola. Fins de semana, feriados, faltas (comuns em crianças com terapias e consultas), greves e falta de tablet **quebram** a ofensiva por motivos que a criança não controla. Pelo estudo de Silverman & Barasch, isso leva ao abandono. Quando a criança se culpa, o efeito piora. **[I + V]**
- **TEA:** a quebra de uma regra ou sequência pode ser vivida como um evento muito aversivo. A rigidez cognitiva transforma o contador em obsessão. **[I]**
- **TDAH:** dificuldade com a percepção do tempo e com planejamento. O contador vira fonte de **vergonha** quando falha. **[I]**
- **[I] Recomendação para o VUOO:** **não ter ofensiva diária individual.** Alternativas: (a) contagem **acumulativa que nunca zera** ("já fizemos 23 voos!"); (b) "ritmo" **semanal** com tolerância embutida; (c) **ofensiva coletiva da turma**, controlada pelo calendário escolar e pausada automaticamente em dias sem aula; (d) **nunca** mostrar perda nem usar a linguagem "você quebrou".

Fontes:
- https://blog.duolingo.com/improving-the-streak
- https://blog.duolingo.com/duolingo-streak-research/
- https://blog.duolingo.com/how-duolingo-streak-builds-habit
- https://blog.duolingo.com/streak-milestone-design-animation
- https://blog.duolingo.com/friend-streak/
- https://blog.duolingo.com/protecting-streaks-from-site-issues
- https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks
- https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth
- https://www.econsultancy.com/six-a-b-tests-used-by-duolingo-to-tap-into-habit-forming-behaviour (secundária; página bloqueou o acesso direto, dados vieram do resumo da busca)
- https://androidauthority.com/duolingo-revive-broken-streak-event-3673004/
- https://www.ibtimes.co.uk/duolingo-restores-301-day-streak-hospitalised-boy-1813986
- Silverman & Barasch (2023), JCR 49(6): https://udspace.udel.edu/items/42ce576b-8e1f-429a-8541-e29e48dbcfbb ; https://www.colorado.edu/business/news/2023/04/20/research-streaks-marketing-tech-barasch ; https://lerner.udel.edu/seeing-opportunity/lerner-professor-researches-how-streaks-motivate-us/
- https://screenwiseapp.com/guides/managing-duolingo-streaks-when-gamification-becomes-stressful (anedótica)

---

## 4. Missões diárias, mensais e de amigos

### O que é
- **Missões diárias:** **três** tarefas por dia, como ganhar X XP, fazer lições com alta precisão ou atingir N combos. Em 2025 o Duolingo **aumentou a recompensa** por completar as três [V].
- **Meta mensal / insígnia do mês:** completar N missões no mês para ganhar uma insígnia temática. Há relatos de exigências subindo de 50 para 100 missões e de um sistema de "pontos de missão" em teste [S, duoplanet].
- **Missões de amigos (Friends Quests):** toda semana, dois amigos são pareados para cumprir um desafio em conjunto em 5 dias. O pareamento só envolve amigos **ativos**, "para você não carregar a missão sozinho" [V]. Elas valem mais pontos para a meta mensal [V]. Recompensa: XP Boost de 30 minutos ou baú com 100 gemas [S, App Store]. Desde 2025 há **pareamento universal** para quem não tem amigos [V].
- **Missão em família:** versão cooperativa para assinantes do plano família [S].

### Por que funciona
- **[I]** As missões dão **metas próximas, específicas e variadas** (teoria de definição de metas) e dão "motivo" para sessões a mais. A rotação diária introduz **novidade**.
- **[I]** As missões cooperativas usam **compromisso social** e reciprocidade: "não quero decepcionar meu parceiro".

### Números conhecidos
- Quem segue amigos tem **5,6x** mais chance de concluir o curso (correlação) [V]. Mais da metade do DAU segue ao menos um amigo [V, carta aos acionistas Q2 2024]. Não encontrei números isolados do efeito das missões.

### Risco para crianças neurodivergentes
- **Positivo:** missões **cooperativas** são a mecânica mais aproveitável para o VUOO. "A turma inteira junta 200 estrelas para o VUOO Bot consertar a nave" é cooperação sem comparação. **[I]**
- **Risco:** missões que exigem **precisão** ("faça 3 lições sem erro") punem quem erra mais por dislexia ou DCD. Missões que exigem **velocidade** punem o processamento lento. **[I]** Use missões de **esforço ou exploração** ("experimente um jogo novo", "ajude o Bot 3 vezes"), nunca de desempenho.
- **Risco:** em missão de dupla, a criança "mais fraca" vira o motivo do fracasso do par. Isso pode virar exclusão social na turma. **[I]** Prefira missões **da turma inteira**, em que ninguém fica identificável como o "elo fraco".
- **TEA:** missões que mudam todo dia quebram a previsibilidade. **[I]** Antecipe as missões (ex.: "missões da semana" visíveis desde segunda-feira) com ícones fixos.

Fontes:
- https://blog.duolingo.com/friends-quests/
- https://blog.duolingo.com/friends-social-features/
- https://blog.duolingo.com/product-highlights/
- https://newsletter.duoplanet.com/posts/how-many-quests-duolingo
- https://newsletter.duoplanet.com/posts/duolingo-family-quest
- https://apps.apple.com/id/iphone/story/id1688543383
- https://duolingo.gcs-web.com/static-files/4e06bcf5-20f4-44a1-a751-6389e82f3467 (carta aos acionistas)

---

## 5. Baús, gemas, corações e Energy (economia do jogo)

### Gemas (moeda)
- Moeda interna, antes chamada "lingots". Ganha-se em missões, baús, ligas (**+60 gemas** para quem fica entre os 3 primeiros [S]) e se compra com dinheiro. Serve para comprar **congelamento e reparo de ofensiva**, **recarga de energia/corações**, apostas de ofensiva, presentear XP Boost a amigos, e "League Repair", que custa 2.000 gemas para recuperar a divisão perdida [S, Deconstructor of Fun].

### Baús
- Baús aparecem no caminho, ao completar missões e em eventos. O conteúdo é **variável** (gemas, boosts). Em 2025 a experiência de abrir baú foi redesenhada para ser "mais deliciosa" [V]. **[I]** É uma recompensa de razão variável, que é o reforço mais resistente à extinção (Skinner) e também o mecanismo central das loot boxes.

### Corações → Energy
- **Corações (até 2025):** 5 vidas. Cada erro tira um coração. Sem corações, a lição para, e é preciso esperar, praticar, ver anúncio, pagar com gemas ou assinar o Super, que dá vidas ilimitadas [V/S].
- **Energy (a partir de maio/julho de 2025, primeiro para uma parte dos usuários):** o dia começa com energia cheia; **cada exercício ou lição gasta energia**; o erro gasta mais; **sequências de acertos devolvem energia** em ritmo **aleatório**; revisar erros é grátis; a recarga total leva cerca de um dia; dá para recarregar com anúncio ou gemas; há bônus por lição perfeita, por adicionar amigo e por baús [V]. A barra tem 25 unidades contra 5 corações [S, The Verge via cópias].
- **Justificativa oficial [V]:** "os corações não eram a forma mais eficaz de apoiar a aprendizagem", "errar é parte normal de aprender" e **iniciantes tinham 2x mais chance de ficar sem corações no meio da lição**. A meta declarada é fazer mais aprendizes concluírem lições.
- **Leitura crítica [S]:** com corações, quem não errava nunca era levado a pagar. Com Energy, **até quem acerta tudo acaba sem energia**, então a pressão de monetização passa a valer para todos. Houve abaixo-assinado "Hearts, not Energy" e reclamações de usuários.

### Por que funciona
- **[I]** Escassez e tempo de espera (o modelo "energy" dos jogos mobile da Zynga e da King) convertem frustração em compra ou assinatura. Recompensas variáveis (baú, devolução aleatória de energia) sustentam a antecipação.

### Risco para crianças neurodivergentes: MUITO ALTO
- **Legal (Brasil):** o **ECA Digital (Lei 15.211/2025, em vigor desde 17/03/2026)** proíbe *loot boxes* em jogos eletrônicos voltados a crianças e adolescentes ou de acesso provável por eles (art. 20, segundo análises jurídicas). Também exige supervisão parental e veda perfilamento para publicidade a menores. Baús de conteúdo aleatório, mesmo sem dinheiro real, ficam numa zona cinzenta perigosa. **[V para a lei; I para a aplicação a baús sem pagamento: consultar o jurídico]** Há uma ADI (7999) no STF contra trechos da lei.
- **Corações e vidas:** punir o erro com a interrupção da atividade é contrário ao DUA e à pedagogia do erro construtivo. Para a criança com dislexia, que erra mais em tarefas de leitura, ou com DCD, que erra o toque, **perder vidas significa ser expulsa da atividade justamente quando precisa de mais prática**. Até o Duolingo abandonou o modelo por isso. **[V + I]**
- **Energy:** limitar o tempo de jogo por uma barra que acaba **desloca o controle do tempo de tela do professor para o sistema** e cria frustração arbitrária. **[I]**
- **Recompensa aleatória** é especialmente potente e potencialmente compulsiva em crianças com TDAH (impulsividade, sensibilidade à recompensa imediata). **[I]**
- **[I] Recomendação para o VUOO:** **sem moeda, sem vidas, sem energia, sem baú aleatório.** Recompensas **determinísticas e anunciadas** ("ao terminar, o Bot ganha a peça X"), sem economia de troca, sem anúncios, sem compras. O limite de tempo é do professor ou da escola, não de uma barra.

Fontes:
- https://blog.duolingo.com/duolingo-energy/ (oficial, 03/07/2025)
- https://uxdesign.cc/duolingos-small-ui-switch-that-changes-everything-fae257203633
- https://www.androidauthority.com/quitting-duolingo-energy-system-3599842/
- https://www.change.org/p/duolingo-hearts-not-energy
- https://duolingo.fandom.com/wiki/Energy
- https://duolingo.deconstructoroffun.com/mechanics/leagues (gemas e League Repair)
- https://blog.duolingo.com/product-highlights/ (baús 2025)
- https://www.machadomeyer.com.br/pt/inteligencia-juridica/publicacoes-ij/direito-digital/estatuto-digital-da-crianca-e-do-adolescente-lei-n-15-211-2025-entra-em-vigor-em-17-de-marco-de-2026
- https://confidata.com.br/blog/eca-digital-o-que-muda-empresas
- https://coad.com.br/home/noticias-detalhe/139047/questionadas-regras-do-eca-digital-sobre-verificacao-de-idade-e-acesso-a-jogos-na-internet

---

## 6. Ligas e leaderboards

### O que é
- Ranking **semanal** de cerca de **30 pessoas** (número de terceiros; o Duolingo não publica), ordenado por XP da semana. Os grupos juntam pessoas de **ritmo parecido** e fuso horário parecido, de qualquer curso. A liga recomeça todo domingo [V para o formato; S para os 30].
- **10 divisões:** Bronze, Prata, Ouro, Safira, Rubi, Esmeralda, Ametista, Pérola, Obsidiana, Diamante. A **promoção** é maior nas divisões baixas: no Bronze sobem 20 de 30; no Obsidiana, 5. Os últimos de cada grupo **caem** de divisão [S]. Os 10 primeiros do Diamante entram no **Torneio Diamante** (quartas, semi e final) [V].
- O usuário entra **automaticamente** (opt-out). É possível chegar ao topo da primeira liga só estudando com regularidade [V].
- Notificações de mudança de posição: "você foi ultrapassado", "risco de rebaixamento" [S].
- Desde 2025 há **leaderboard de amigos** [V].

### Por que funciona
- **Comparação social** com rivais **próximos** em desempenho. Mazal: "a proximidade do competidor importa mais do que a proximidade da relação". A primeira versão, com amigos e família, funcionava pior [V].
- **[I]** Aversão à perda (rebaixamento), efeito de meta próxima (o corte de promoção) e prazo semanal.

### Números conhecidos
- Lançar as ligas trouxe **+17% de tempo total de aprendizagem** e **triplicou** os aprendizes altamente engajados (1h+/dia, 5 dias/semana) [V].
- O próprio Duolingo descobriu que o ranking por XP estimulava **atividades fáceis** e reequilibrou o XP (seção 2) [V].

### Evidência acadêmica
- **Hanus & Fox (2015, *Computers & Education*):** curso universitário de 16 semanas, com e sem leaderboard e insígnias. O grupo gamificado teve **menos motivação intrínseca, satisfação e empoderamento** com o tempo e **notas finais menores**. Os autores atribuem o efeito à **comparação social desfavorável** para quem tinha pior desempenho. A amostra era pequena (~80) e há estudos com resultado oposto [S para os detalhes, via revisões].

### Risco para crianças neurodivergentes: MUITO ALTO
- Numa turma real, um ranking **expõe** sempre as mesmas crianças (com deficiência, com dislexia, as mais lentas) **na lanterna**, na frente dos colegas e do professor. Isso fere o princípio de inclusão do DUA e pode ferir a dignidade, com risco de bullying. **[I]**
- **TDAH:** o hiperfoco no ranking pode gerar comportamento compulsivo; perder pode gerar explosões emocionais. **[I]**
- **TEA:** a rigidez com regras de justiça faz com que ser "ultrapassado" seja vivido como injustiça. **[I]**
- **[I] Recomendação para o VUOO:** **nenhum ranking entre crianças.** Use (a) **progresso coletivo** da turma em direção a uma meta comum; (b) **comparação consigo mesmo** ("você fez mais do que na semana passada", só se for positivo); (c) dados de desempenho **só no painel do professor**, nunca na tela do aluno. O Duolingo for Schools mostra XP, tempo e tarefas no painel do professor [S], e esse é o lugar certo para o dado.

Fontes:
- https://blog.duolingo.com/duolingo-leagues-leaderboards/
- https://duolingo.deconstructoroffun.com/mechanics/leagues
- https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth
- https://blog.duolingo.com/time-spent-learning-well/
- https://blog.duolingo.com/product-highlights/
- Hanus & Fox (2015), Computers & Education 80:152–161 (citado via https://educationaltechnologyjournal.springeropen.com/articles/10.1186/s41239-017-0042-5 e https://pmc.ncbi.nlm.nih.gov/articles/PMC8916940)

---

## 7. Conquistas (achievements) e insígnias

### O que é
- Conquistas com níveis por marcos acumulados (dias de ofensiva, XP total, lições perfeitas, palavras aprendidas) e insígnias mensais de missão. **[I, observação]** Mostradas no perfil.

### Por que funciona
- **[I]** Coleção e completude, metas de longo prazo e identidade ("sou alguém que...").

### Números
- Não encontrei dados públicos de impacto.

### Risco para crianças neurodivergentes
- **Moderado e aproveitável.** Conquistas **cumulativas que nunca se perdem** são a forma mais segura de reconhecimento. **[I]**
- Cuidado com conquistas de **desempenho** ("10 lições perfeitas"), que excluem quem erra mais, e de **tempo** ("30 dias seguidos"), que exigem acesso diário. **[I]**
- **TEA:** coleções completas podem ser altamente motivadoras (interesse por sistemas e coleções), mas uma coleção **impossível de completar** gera sofrimento. **[I]** Mostre sempre o que falta e garanta que tudo seja alcançável pela turma inteira.
- **Base teórica:** a meta-análise de Deci, Koestner & Ryan (1999, 128 estudos) mostra que recompensas tangíveis **esperadas e contingentes à tarefa** reduzem a motivação intrínseca (d entre −0,28 e −0,40), enquanto o **feedback verbal positivo e informativo** aumenta. É um debate ainda aberto (Cameron & Pierce). **[V]** Para o VUOO: reconhecimento **informativo** ("você aprendeu a juntar sílabas com R!") em vez de controlador ("ganhe 3 estrelas para desbloquear").

Fontes:
- Deci, Koestner & Ryan (1999), Psychological Bulletin 125(6): https://depts.washington.edu/techdocs/papers/deciExtrinsicRewardsAndIntrinsicMotivation99.pdf
- https://www.selfdeterminationtheory.org/SDT/documents/2001_DeciKoestnerRyan.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2731358/ (contraponto, Cameron et al.)

---

## 8. Amigos e social

### O que é
- Seguir amigos, ofensiva com amigos (até 5), missões de amigos, ranking de amigos, presentear boosts, e "high five" e incentivos [V/S].

### Números
- Quem segue amigos tem **5,6x** mais chance de concluir o curso [V, correlação]. Mais da metade do DAU segue alguém [V]. O programa de indicação (um mês de Super) trouxe só **+3%** de novos usuários [V].

### Risco para crianças neurodivergentes
- Grafo social aberto entre crianças **não é aceitável**: risco de contato indevido, LGPD art. 14 e ECA Digital. **[I]**
- Crianças com TEA ou TDAH frequentemente têm **menos amizades recíprocas**. Recursos sociais baseados em "amigos" **amplificam a exclusão**, ao tornar visível quem não tem amigos ou não foi escolhido. **[I]**
- **[I] Para o VUOO:** o "social" é **a turma como unidade** (fechada, criada pelo professor) e o **VUOO Bot como parceiro**. Nada de seguir, convidar ou ver o perfil de colegas.

Fontes:
- https://blog.duolingo.com/friends-social-features/
- https://blog.duolingo.com/friend-streak/
- https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth

---

## 9. Notificações

### O que é
- Lembretes diários (push e e-mail) com a "voz" do Duo e, desde 2025, de **Lily e Falstaff** [V]. O "salva-ofensiva" chega à noite [V]. As notificações vão ficando mais insistentes, e depois de dias sem resposta vem o famoso "parece que esses lembretes não estão funcionando, vamos parar de enviá-los" [S]. **[S]** O ícone do app muda de humor (em 2025 houve ícones sazonais: "assustador, bobo, **triste**, glitch" [V]).

### Por que funciona
- **[V]** O Duolingo trata o push como um canal a "**proteger**": aumentar o volume exigia justificativa forte e aprovação do CEO. Testam horário, template, imagem, texto e idioma com A/B e um **algoritmo de bandit** (multi-armed bandit), que gerou "dezenas" de pequenos ganhos. O exemplo do Groupon (5 e-mails por dia, usuários que desistiam para sempre) é usado como alerta.
- **[S]** O CEO Luis von Ahn descreveu o tom como um equilíbrio "entre legal e malvado" (Mashable, 2017, via Daily Dot). O humor passivo-agressivo **virou meme**, o que transformou a culpa em parte da marca.

### Críticas
- Culpa como alavanca: imagens do Duo triste e mensagens de culpa "incomodam alguns usuários, especialmente crianças" [S, El País via UniversityXP]. Textos como "20 dias de chantagem emocional do Duolingo" [S].

### Risco para crianças neurodivergentes: ALTO
- Crianças de 6 a 11 anos, sobretudo com TEA, têm **dificuldade com ironia e sarcasmo**: "o Duo está triste por sua causa" é lido **literalmente** como culpa real. **[I, consistente com a literatura sobre pragmática no TEA]**
- O VUOO é usado na escola, e a criança não deveria receber push fora dela. Se houver comunicação com a família, ela vai **para o responsável**, em tom informativo e sem culpa. **[I]**
- **[I] Regra para o VUOO Bot:** o Bot **nunca** fica triste, bravo ou decepcionado **com a criança**, nunca "sente falta" de forma culpabilizante, nunca ameaça perda. Pode ficar **contente em reencontrar** ("Que bom te ver! Vamos voar?") sem mencionar a ausência.

Fontes:
- https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth
- https://www.dailydot.com/irl/duolingo-owl-memes/
- https://www.universityxp.com/news/2025/7/25/we-havent-seen-you-in-a-while-duolingos-passive-aggressive-strategy-for-keeping-users-hooked
- https://uxdesign.cc/20-days-of-emotional-blackmail-from-duolingo-4f566523e3c5
- https://blog.duolingo.com/product-highlights/

---

## 10. Trilha / caminho (path)

### O que é
- Desde **1º de novembro de 2022**, a "árvore" de habilidades, em que o usuário escolhia o que fazer, foi trocada por um **caminho linear único**. Dentro de cada unidade há lições, histórias, prática personalizada, revisão de unidade, baús e nós "lendários" (desafio opcional). As dicas viraram um "guia" por unidade, e a prática passou a ficar **embutida** no caminho em vez de exigir revisitar habilidades "rachadas" [V].
- Justificativa: simplificar, guiar o iniciante, aumentar o engajamento e a conversão em assinatura, e dar um motivo para usuários inativos voltarem [V]. Houve forte reação de usuários antigos pela **perda de autonomia** [V/S].
- O Duolingo afirma que quem usou o caminho teve **melhores notas de leitura e escuta** que quem usou a árvore (estudo interno) [V/S].
- Em Math, desde 2025, **é possível navegar e começar qualquer unidade ou tema** [V], o que reintroduz escolha.

### Por que funciona
- **[I]** Elimina a "paralisia de escolha", sempre mostra um **próximo passo óbvio** e deixa o progresso legível espacialmente (mapa).

### Risco para crianças neurodivergentes
- **Positivo:** linearidade e um próximo passo óbvio ajudam **TEA** (previsibilidade) e **TDAH** (reduz a carga de decisão). **[I]**
- **Negativo:** linearidade **trava** quem empaca num nó (ex.: dislexia numa habilidade de leitura) e tira do professor a capacidade de direcionar. **[I]**
- **[I] Para o VUOO:** um mapa visual com **próximo passo destacado**, mas com o **professor podendo atribuir e reordenar** jogos (como as "tarefas" do Duolingo for Schools), **caminhos alternativos** de mesma habilidade em modalidades diferentes (auditiva, visual, motora), e nenhum bloqueio duro por desempenho.

Fontes:
- https://blog.duolingo.com/new-duolingo-home-screen-design
- https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655
- https://investors.duolingo.com/static-files/d667f9d1-8f7f-418c-b116-e699a30a9826
- https://blog.duolingo.com/product-highlights/

---

## 11. Revisão espaçada e prática personalizada

### O que é
- **Half-Life Regression (HLR)**, de Settles & Meeder (ACL 2016): um modelo treinável que estima a "meia-vida" de cada palavra na memória do aprendiz. Reduziu o erro de previsão em **mais de 45%** contra as referências e teve cerca de metade do erro do sistema Leitner usado antes. Nos testes A/B, aumentou a **retenção diária**. Código e dados são abertos [V].
- **Birdbrain:** um sistema posterior, re-treinado toda noite, que estima a probabilidade de acerto de cada exercício para cada pessoa. O gerador de sessão usa isso para montar lições no nível certo de dificuldade [S, VentureBeat com Burr Settles].
- Lições de **prática personalizada** embutidas no caminho [V].

### Por que funciona
- Efeito de espaçamento e prática de recuperação (dois dos achados mais robustos da ciência cognitiva) somados à **dificuldade desejável calibrada** para manter a taxa de acerto alta, o que é motivador.

### Risco para crianças neurodivergentes
- **Este é o componente de maior valor pedagógico e menor risco.** **[I]**
- Atenção: um modelo treinado com a população "média" calibra mal para perfis atípicos (ex.: perfil irregular no TEA, dificuldade fonológica específica na dislexia). **[I]** O VUOO deve deixar o professor ver e ajustar o nível, e mostrar no painel **por que** um item está voltando.
- **[I]** Uma taxa de acerto alvo alta (~80% ou mais) é ainda mais importante para crianças com histórico de fracasso escolar.

Fontes:
- https://preview.aclanthology.org/fix_video/P16-1174.pdf
- https://blog.duolingo.com/how-we-learn-how-you-learn
- https://venturebeat.com/ai/how-duolingo-uses-ai-in-every-part-of-its-app

---

## 12. Onboarding e nivelamento

### O que é
- **Valor antes do cadastro:** escolher o idioma e o motivo, definir a meta diária, fazer a **primeira lição antes de criar a conta**. O cadastro é pedido depois da primeira lição ou do teste de nível, e é possível adiar até o fim do primeiro nível [S].
- **Nivelamento dentro do jogo:** o usuário avança por níveis até chegar à dificuldade adequada, sem um "teste formal" [S].
- **Compromisso:** trocar "continuar" por "me comprometo com a minha meta" aumentou a retenção [V]. A primeira semana é a fase mais frágil, e atravessá-la eleva muito a retenção de longo prazo [V].

### Risco para crianças neurodivergentes
- No VUOO, quem cria as contas é o **professor** (como os "cartões de login" sem e-mail do Duolingo for Schools [S]). **[I]** O onboarding da criança deve ser: **zero texto**, apresentação do VUOO Bot com voz, **um microjogo fácil** com sucesso garantido logo de cara, e login por imagem/QR.
- **[I]** Nivelamento **invisível e gentil**: nunca "teste", nunca "você está no nível 1". A criança com dislexia que "cai" no nível mais baixo não deveria perceber que foi classificada.
- **[I]** O "compromisso" (meta diária escolhida pela criança) não faz sentido para crianças de 6 a 8 anos. Quem define a cadência é o professor.

Fontes:
- https://goodux.appcues.com/blog/duolingo-user-onboarding
- https://uxdesign.cc/the-duolingo-diaries-an-honest-ux-review-part-1-onboarding-ed0165d44c58
- https://learn.k20center.ou.edu/tech-tool/4772
- https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks

---

## 13. O contrapeso: métrica de "aprender bem" e eficácia

- **Time Spent Learning Well (TSLW)** [V]: uma métrica-proxy de aprendizagem, porque estudos de eficácia são lentos demais para testes A/B diários. Fórmula aproximada: **minutos no caminho + 0,5 × minutos em outras atividades**. Foi criada porque "total de sessões" premiava sessões curtas e fáceis e "tempo total" era dominado por superusuários. A meta é aumentar a parcela de aprendizes com **15 minutos ou mais por dia**. Dias de pouco esforço são tolerados para evitar churn.
- **Eficácia** [V/S]: estudo publicado em *Foreign Language Annals* (2022, n = 225) mostra que quem concluiu 5 unidades de espanhol ou francês teve leitura e escuta comparáveis às de 4 semestres universitários. Mas os estudos são **financiados pela empresa**, com **viés de seleção** apontado por críticos (CALL-EJ) e só cobrem leitura e escuta.
- **Lição para o VUOO [I]:** definir **desde o início** uma métrica-norte de aprendizagem (e não de engajamento) e tratar engajamento como **meio**. O TSLW mostra que até o Duolingo precisou corrigir a gamificação que premiava o comportamento errado.

Fontes:
- https://blog.duolingo.com/time-spent-learning-well/
- https://blog.duolingo.com/results-duolingo-efficacy-studies
- https://investors.duolingo.com/news-releases/news-release-details/leading-language-research-journal-publishes-study-showing
- https://callej.org/index.php/journal/article/download/419/347/1013

---

## 14. Mascote Duo e elenco de personagens

### Duo
- Coruja verde. **No app**, comemora, encoraja e aparece em marcos (vira fênix nas ofensivas [V]). **Fora do app** (TikTok e redes), tem uma persona "**unhinged**" ("desequilibrada"): persegue usuários que não fazem lição, briga com o Google Tradutor, é fã da Dua Lipa. O time de social (Zaria Parvez) chegou a esse tom com escuta social e testes. O primeiro viral brincava com a **coruja pressionando o usuário** [V/S]. A diretoria de comunicação chama o estilo de "wholesome unhinged" [S].
- **A "morte" do Duo (fevereiro de 2025):** anúncio da morte (atropelado por um Cybertruck), ícone com olhos em X e convite para "fazer lições para revivê-lo", com contador global de XP. Ele "voltou" em 24/02. Teve dezenas de milhões de visualizações. Os números de impressões (1,7 bilhão) não são verificados [V para o fato, S para os números].
- **[I]** A personalidade tem duas camadas: no produto, um **coach entusiasmado**; no meme, um **perseguidor ameaçador**. O meme vaza para o produto pelas notificações (culpa) e pela forma como as crianças percebem o Duo ("o Duo vai me pegar").

### Elenco (World Characters)
- **10 personagens** com voz e um conjunto próprio de **mais de 20 bocas** (visemas), animados no **Rive** com máquina de estados: idle (piscar, acenar com a cabeça), fala sincronizada, reação final de acerto ou erro [V].
- As personalidades são construídas como **contrastes**: Zari, extrovertida, e Lily, introvertida, sarcástica e "deadpan"; Lin, tranquilo, e Bea, ansiosa/"neurótica" [V, blog]. Outros: Junior, Oscar, Eddy (um "pai fitness" que comemora lições perfeitas), Falstaff (urso) [V/S].
- Lily ganhou **videochamada com IA** (Duolingo Max), com expressões e lábios dirigidos por máquina de estados do Rive em tempo real [V, blog do Rive].
- **Diversidade intencional:** o blog descreve a origem das personagens femininas como forma de representar personalidades variadas [V].

### Como reagem ao erro
- **[V]** Os personagens têm um estado de reação a erro no fim do exercício. **[I, observação]** A reação é leve (expressão de surpresa ou desânimo), nunca punitiva dentro do exercício. A culpa fica concentrada nas **notificações** e no marketing.

### Risco para crianças neurodivergentes
- **TEA:** sarcasmo (Lily), ameaça como humor (Duo) e tristeza do personagem como alavanca são **ambíguos e potencialmente angustiantes**. **[I]**
- **Positivo:** personagens com **personalidades distintas e estáveis** (introvertida, ansiosa, extrovertida) permitem que crianças diferentes **se vejam representadas**. Uma personagem ansiosa ou introvertida retratada com afeto é **valiosa para crianças neurodivergentes**. **[I]**
- **[I] Para o VUOO Bot:** personalidade **estável, previsível, literal e calorosa**; erra junto e "aprende" com a criança (modelo de mentalidade de crescimento); reage ao erro com **curiosidade** ("Hmm, vamos tentar de outro jeito?"), nunca com tristeza; sem sarcasmo e sem humor de ameaça. O humor, se houver, vem do **pastelão físico** do Bot (tropeça, se enrola), que é compreensível sem pragmática verbal.

Fontes:
- https://www.marketplace.org/story/2022/01/17/the-creative-force-behind-a-viral-corporate-tiktok-account
- https://digiday.com/marketing/how-duolingo-is-using-its-unhinged-content-with-duo-the-owl-to-make-people-laugh-on-tiktok/
- https://campaignlive.com/article/duolingo-comms-head-sam-dalsimer-leads-wholesome-unhinged-strategy/1910699
- https://www.adroll.com/blog/unrolling-duolingo-how-unhinged-tiktoks-made-the-brand-a-winner
- https://npr.org/2025/02/26/nx-s1-5309785/duolingo-owl-mascot-lives
- https://blog.duolingo.com/duolingo-female-character-origin-stories
- https://blog.duolingo.com/world-character-visemes
- https://rive.app/blog/duolingo-s-ai-powered-video-call-brings-lily-to-life
- https://blog.duolingo.com/product-highlights/

---

## 15. Sistema visual

### Paleta
- **Cores oficiais** (antigo site de marca design.duolingo.com, hoje redirecionado para o blog; valores confirmados por várias cópias) [V/S]:
  - **Feather Green `#58CC02`** (cor primária e da marca)
  - **Mask Green `#89E219`**
  - **Eel `#4B4B4B`** (texto)
  - **Snow `#FFFFFF`** (fundo)
  - **Macaw `#1CB0F6`** (azul secundário)
  - **Beak Upper `#FFC200`** (paleta do Duo)
- Fontes não oficiais [S]: **Cardinal `#FF4B4B`** (erro, perda de vida), **Bee `#FFC800`** (conquistas), além de Fox (laranja) e outras com **nomes de animais**.
- **[I, observação]** Os botões são "3D", com uma borda inferior mais escura que "afunda" ao toque; os cantos são muito arredondados; o fundo é branco com muito espaço vazio.

### Tipografia
- **Feather Bold:** fonte própria, desenhada por Krista Radoeva (Fontsmith) no rebrand da **Johnson Banks em 2019**. As formas vêm da asa da coruja ("flick" no "g" minúsculo, junções como ponta de asa). Usada em títulos e momentos de marca; **não é comercializada** [V/S].
- **DIN Next Rounded (Monotype):** usada no texto de interface [S].

### Ilustração: "shape language"
- Toda ilustração é construída a partir de **3 formas básicas: retângulo arredondado, círculo e triângulo arredondado**. **Formas pontudas são "off-brand"** [V, guia de design].
- Princípios [V]: **rápido de produzir** (vetor), **claro** (o mínimo de detalhes, silhuetas legíveis, **espaço negativo branco** para não atrapalhar), **divertido** (exagero e caricatura, humor) e uso de **ângulos e animação para guiar o olhar**. O estilo evoluiu de formas pontudas e cores apagadas sobre cinza para formas **arredondadas, cores vivas sobre branco**. Essa evolução começou em **2018 no Duolingo KIDS**.
- Dado de design [V]: ícones de habilidade **animados** prenderam mais a atenção e fizeram o usuário iniciar mais lições.
- Justificativa explícita [V]: o visual lúdico **reduz o medo de errar**.

### Motion
- **Rive** com **máquinas de estado** para personagens (lip-sync em tempo real, idle, reações). Os arquivos são pequenos e multiplataforma [V]. Que **todas** as animações do app tenham migrado para o Rive é afirmação de terceiros [S].
- Animação de marco: o timing foi tratado como **tão importante quanto o visual** [V].

### Sound design
- Não há documentação oficial. Relatos descrevem um chime ascendente no acerto e um tom descendente no erro [S]. **[I]** Há também fanfarra no fim da lição e sons de baú e de ofensiva.

### Risco para crianças neurodivergentes
- **Positivo e aproveitável:** a shape language arredondada, com o mínimo de detalhe, silhuetas claras e muito espaço branco, está **alinhada** a recomendações de baixa carga visual para TEA, TDAH e dislexia. **[I]**
- **Atenção:**
  - **Verde vivo sobre branco** e telas comemorativas muito saturadas, com partículas e flashes, podem sobrecarregar crianças com hipersensibilidade visual. **[I]** O VUOO precisa de um **modo calmo** (menos movimento, respeitando `prefers-reduced-motion`, saturação menor).
  - **Vermelho e verde** como único código de erro e acerto falha para **daltonismo** (cerca de 8% dos meninos) e o vermelho carrega significado punitivo. **[I]** Combine sempre com forma e ícone.
  - **Tipografia:** fontes arredondadas e grossas são boas para leitores iniciantes. **[I]** Para dislexia, priorize uma fonte com letras **bem diferenciadas** (b/d/p/q, I/l/1), um "a" e um "g" de forma escolar, espaçamento generoso e opção de aumentar. Fontes "específicas para dislexia" têm evidência fraca. O que importa é tamanho, espaçamento e clareza das letras.
  - **Som:** volume e canais separados (narração, efeitos, música), com opção de desligar efeitos sem perder a narração. **[I]**

Fontes:
- https://design.duolingo.com/identity/color (hoje redireciona; valores via https://brandpalettes.com/duolingo-colors/ e https://open-design.ai/plugins/design-system-duolingo/)
- https://www.creativebloq.com/news/feather-bold
- https://www.designweek.co.uk/duolingo-rebrand-avoids-silicon-valley-tropes-and-reflects-companys-quirky-personality/
- https://www.monotype.com/es/node/6287
- https://fontsinuse.com/uses/59497/duolingo-app
- https://design.duolingo.com/illustration (hoje redireciona; trecho citado em resultados de busca)
- https://blog.duolingo.com/shape-language-duolingos-art-style/
- https://blog.duolingo.com/world-character-visemes
- https://blog.duolingo.com/streak-milestone-design-animation
- https://www.strv.com/blog/how-we-translated-a-children-s-educational-product-from-paper-to-pixels (afirmação de adoção ampla do Rive)

---

## 16. Duolingo ABC e Duolingo Math (produtos para crianças)

### Duolingo ABC
- Alfabetização para crianças de **3 a 8 anos**. Mais de 700 lições da pré-escola ao 2º ano, alinhadas ao Common Core e ao National Reading Panel (consciência fonêmica, fonética sistemática, fluência, compreensão). Atividades **multissensoriais** (traçar letras, arrastar), histórias **narradas com destaque palavra por palavra**, minijogos [S, App Store/SmartBrief].
- **Sem anúncios e sem compras internas** [S]. Isso remove a principal fonte de pressão da economia do app adulto.
- Eficácia: relato de **+28%** na pontuação de alfabetização após 9 semanas (EDC). **Não encontrei o estudo original**, então trate como não verificado [S].
- **[I]** Não encontrei documentação de como o ABC trata ofensivas e recompensas. A ausência de ligas, vidas e moeda no material público sugere uma gamificação **bem mais leve** que a do app principal. Vale a pena um teste de mão no app antes de qualquer decisão.
- A shape language arredondada atual **nasceu no Duolingo KIDS em 2018** [V].

### Duolingo Math
- Lançado em 2022 como app separado e depois incorporado ao app principal (com Música). Usa **minijogos**, lições curtas, unidades e ofensiva. Exercícios **manipuláveis** (ex.: mover os ponteiros de um relógio) [S]. O blog relata a dificuldade de criar visuais e exercícios que mudam com a dificuldade, porque a matemática não tem "blocos de construção" uniformes como a língua [V].
- 2025: **60 novas unidades** do 6º ao 9º ano; o usuário pode **escolher qualquer unidade ou tema**; disponível em dezenas de idiomas [V].

### Risco e lição para o VUOO
- **[I]** O próprio Duolingo, quando desenha para **crianças pequenas** (ABC), **remove** anúncios, compras, competição social e economia. É um forte sinal de que "a jogabilidade do Duolingo" que o dono do produto quer é **o loop de lição + feedback + personagem + progresso visível**, e **não** ligas, corações, gemas e culpa.
- **[I]** Narração palavra a palavra com destaque, traçado e manipulação direta (relógio) são padrões **diretamente aproveitáveis** para dislexia e DCD, desde que haja alternativas motoras.

Fontes:
- https://apps.apple.com/app/id1440502568
- https://www.smartbrief.com/original/strengthen-early-literacy-skills-with-duolingo-abc
- https://duolingoguides.com/duolingo-abc/ (o dado de 28% vem daqui; não verificado)
- https://blog.duolingo.com/developing-math
- https://blog.duolingo.com/new-subjects/
- https://techcrunch.com/?p=2431531
- https://blog.duolingo.com/product-highlights/

---

## 17. Críticas documentadas: síntese

| Crítica | Evidência | Força |
|---|---|---|
| **Aversão à perda e ansiedade de ofensiva** | O próprio Duolingo admite que perder a ofensiva desmotiva e que usuários evitam desafios; Silverman & Barasch (2023) mostram abandono após ofensiva quebrada, pior com autoculpa | **[V] forte** |
| **Culpa como alavanca (notificações, Duo triste)** | Tom "entre legal e malvado" assumido pelo CEO; relatos de usuários e imprensa | [S] moderada |
| **Monetização da frustração** (corações → Energy, gemas, reparo pago) | Críticas de UX e abaixo-assinado; o Duolingo justifica pela aprendizagem | [S] moderada |
| **A gamificação premia volume, não aprendizagem** | O próprio Duolingo criou o TSLW e reequilibrou o XP por isso | **[V] forte** |
| **Leaderboards reduzem motivação intrínseca de quem perde** | Hanus & Fox (2015); efeitos mistos na literatura | [V/S] moderada |
| **Recompensas extrínsecas minam motivação intrínseca** | Deci, Koestner & Ryan (1999), meta-análise, ainda debatida | [V] moderada a forte |
| **Efeitos em crianças** (choro, colapso, uso abaixo de 13 anos sem verificação de idade) | Common Sense Media classifica 13+; guias parentais anedóticos; caso do menino de 10 anos hospitalizado | [S] fraca a moderada, sem estudo controlado |
| **Eficácia superestimada** | Estudos financiados pela empresa, viés de seleção | [S] moderada |
| **Perda de autonomia** (caminho linear) | Reação de usuários em 2022 | [V/S] |
| **Recompensa aleatória ≈ loot box** | ECA Digital proíbe loot box para crianças no Brasil | [V lei / I aplicação] |

**TDAH e recompensas [V, literatura clínica]:** crianças com TDAH descontam recompensas futuras mais fortemente (aversão à espera), respondem forte à recompensa **entregue** mas têm **antecipação diminuída**. A recomendação clínica é reforço **imediato, frequente e consistente**. Isso apoia o loop curto com feedback imediato, mas **não** apoia mecânicas baseadas em antecipação de longo prazo (ofensiva de 30 dias, liga semanal, meta mensal), que justamente funcionam mal para esse perfil e geram falha visível. **[I na aplicação]**

Fontes:
- https://screenwiseapp.com/guides/duolingo-and-the-streak-obsession
- https://www.commonsensemedia.org/website-reviews/duolingo
- https://thedecisionlab.com/es-ES/insights/consumer-insights/streak-creep-the-perils-of-too-much-gamification
- https://desirabilitylab.com/backfill/backfill-2024-302-duolingo-streak-mechanics
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3268965 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3059765 ; https://link.springer.com/article/10.1007/s10802-011-9547-x (TDAH, recompensa e espera)
- demais fontes citadas nas seções anteriores

---

## 18. Matriz de decisão para o VUOO [I: recomendações, não dados]

| Mecânica do Duolingo | Veredito para o VUOO | Versão adaptada |
|---|---|---|
| Loop de lição curto, feedback imediato, barra de progresso | **ADOTAR** | Microjogo de 60–90 s; feedback multimodal (voz + animação + ícone); erro em cor neutra, sem vermelho; teto de itens extras |
| Fim de lição com celebração | **ADOTAR, enxuto** | Uma tela, um reforço informativo ("você aprendeu X"), um próximo passo; respeitar o modo calmo |
| Personagens animados com reação | **ADOTAR** | VUOO Bot com máquina de estados (Rive), reação ao erro = curiosidade, nunca tristeza |
| Shape language arredondada, espaço branco | **ADOTAR** | Mais um modo de baixa estimulação e código duplo (cor + forma) |
| Revisão espaçada e dificuldade adaptativa | **ADOTAR** | Taxa de acerto alvo alta; ajuste visível e editável pelo professor |
| Trilha/caminho visual | **ADAPTAR** | Mapa com próximo passo claro + professor atribui/reordena + rotas alternativas por modalidade |
| Missões | **ADAPTAR** | Missões **da turma**, de esforço/exploração, anunciadas com antecedência |
| Conquistas | **ADAPTAR** | Cumulativas, nunca perdidas, todas alcançáveis, ligadas a habilidades |
| XP numérico | **SUBSTITUIR** | Progresso concreto no mundo do Bot (objetos, mapa), sem números |
| Ofensiva diária | **SUBSTITUIR** | Contador acumulativo que nunca zera ou ritmo coletivo da turma pausado pelo calendário escolar |
| Ligas e leaderboards | **NÃO USAR** | Meta coletiva da turma; desempenho só no painel do professor |
| Corações / Energy | **NÃO USAR** | Errar nunca interrompe; o tempo de uso é controlado pelo professor |
| Gemas, baús aleatórios, loja | **NÃO USAR** | Recompensas determinísticas e anunciadas (risco jurídico pelo ECA Digital) |
| Notificações com culpa | **NÃO USAR** | Sem push para a criança; comunicação informativa para o responsável e o professor |
| Social baseado em amigos | **NÃO USAR** | Turma fechada como unidade; o Bot como parceiro |
| Humor "unhinged" / sarcasmo | **NÃO USAR** | Humor físico e literal; personalidade estável e previsível |
| Métrica TSLW (aprendizagem > engajamento) | **ADOTAR o princípio** | Métrica-norte de habilidades consolidadas, não de DAU |
