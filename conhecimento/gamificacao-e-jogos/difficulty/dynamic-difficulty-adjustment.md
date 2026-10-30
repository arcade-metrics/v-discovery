---
id: gam.diff.dynamic-difficulty-adjustment
titulo: Ajuste dinâmico de dificuldade (DDA)
tipo: tecnica
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [hunicke2004hamlet, hunicke2005case, zohaib2018dda, andrade2006balancing, missura2009player, constant2019confidence, denisova2019deceptive, vitekova2026dda, paraschos2023game, baldwin2013framework]
relacoes:
  - { tipo: depende-de, alvo: gam.diff.challenge-and-zpd }
  - { tipo: depende-de, alvo: gam.motiv.flow }
  - { tipo: complementa, alvo: adp.adapt.sequencing-policies }
  - { tipo: complementa, alvo: gam.instr.telemetry-as-evidence }
  - { tipo: relacionado-a, alvo: acs.adapt.algorithmic-adaptation-and-autonomy }
  - { tipo: relacionado-a, alvo: acs.adapt.adapting-games-and-activities }
  - { tipo: relacionado-a, alvo: rtm.mp.matchmaking }
  - { tipo: relacionado-a, alvo: lae.psy.reliability-and-validity }
  - { tipo: avaliado-por, alvo: lae.ind.engagement-indicators }
termos: [dynamic difficulty adjustment, dynamic game balancing, challenge function, flailing, ajuste reativo, ajuste proativo, rubber band AI, dynamic scripting, challenge-sensitive action selection, multiplayer DDA, DDA explícito, DDA oculto, superconfiança, exploração do DDA]
---

# Ajuste dinâmico de dificuldade (DDA)

## Definição e terminologia

Ajuste dinâmico de dificuldade (*dynamic difficulty adjustment*, DDA) é a modificação automática, em tempo real, de características, comportamentos e cenários de um jogo conforme a habilidade do jogador, para que ele não se entedie quando o jogo é fácil demais nem se frustre quando é difícil demais [F: zohaib2018dda, resumo]. Sinônimos na literatura: *dynamic game balancing* [F: andrade2006balancing] e, no jargão de projeto, *rubber band AI*, em que os oponentes são "puxados" na direção do desempenho do jogador [F: missura2009player, §3]. Em jogos competitivos com vários humanos, a variante *multiplayer DDA* existe como linha própria [F: baldwin2013framework, metadados].

O que não é: não é a escolha estática de nível (fácil, médio, difícil) feita uma vez pelo jogador [F: zohaib2018dda, resumo]; não é o sequenciamento de itens de conteúdo por um modelo de aluno, que fica em `adp.adapt.sequencing-policies`; não é o pareamento de jogadores de habilidade parecida, que fica em `rtm.mp.matchmaking`. A diferença entre dificuldade do jogo e dificuldade do conteúdo, e o alvo de desafio, ficam em `gam.diff.challenge-and-zpd`.

## Problema que resolve

Hunicke e Chapman resumem: jogos são "boring when they are too easy and frustrating when they are too hard", e a dificuldade costuma ser estática diante do desempenho individual [F: hunicke2004hamlet, resumo]. Níveis pré-definidos falham diante da diversidade de jogadores e da velocidade diferente com que cada um aprende, além de não acompanharem regressões, por exemplo após um tempo sem jogar [F: andrade2006balancing, introdução]. Poucos níveis tornam fácil escolher mas improvável acertar; muitos níveis tornam a escolha difícil, e ir e voltar entre o jogo e as configurações interrompe o fluxo [F: missura2009player, §1 e §3].

## Fundamentos e funcionamento

### O laço: medir, decidir, agir

Toda abordagem precisa medir, explícita ou implicitamente, a dificuldade enfrentada, por uma heurística chamada *challenge function*: taxa de acertos, peças ganhas e perdidas, pontos de vida, tempo para completar a tarefa ou qualquer métrica da pontuação [F: andrade2006balancing, §2; zohaib2018dda, §3]. Andrade et al. fixam três requisitos: identificar depressa o nível inicial do jogador, acompanhar de perto evoluções e regressões e manter o comportamento do jogo crível, porque o jogador não deve perceber que o computador joga "with a virtual hand tied behind its back" [F: andrade2006balancing, §2].

### Hamlet: estoque, oferta e demanda

O sistema Hamlet, embutido num motor de tiro em primeira pessoa, modela vida e munição como estoque e usa teoria de estoques para prever falta (*shortfall*): quando o dano acumulado provavelmente supera a vida disponível, o jogador está "flailing" e o sistema intervém [F: hunicke2004hamlet, Assessment]. As ações são reativas (mudar precisão e dano de inimigos já em cena) ou proativas (mudar inimigos que ainda vão surgir); as reativas são mais diretas mas arriscam fazer o jogo parecer "schizophrenic", e as proativas preservam a suspensão de descrença mas são mais difíceis de avaliar e podem gerar uma espiral de correções [F: hunicke2004hamlet, Actions]. Cada intervenção tem custo, ponderado por local, progresso, número de mortes e intervenções anteriores, porque intervir sempre do mesmo jeito torna o jogo trivial [F: hunicke2004hamlet, Cost]. Duas políticas ilustram o alvo: "Comfort Zone" mantém o jogador em torno de 50% de vida; "Discomfort Zone", para experientes, o mantém lutando a partir de 15 a 20% [F: hunicke2004hamlet, Policies].

### Competência e desempenho do oponente

A abordagem *challenge-sensitive* de Andrade et al. separa competência (o agente aprende, por aprendizagem por reforço, a jogar o melhor possível) de desempenho (age só tão bem quanto necessário): se o jogo está difícil demais, escolhe a segunda melhor ação, a terceira, e assim por diante, até igualar o jogador [F: andrade2006balancing, §3].

### Modelos de jogador aprendidos fora de linha

Missura e Gärtner agrupam traços de partidas de testadores (que ajustavam a dificuldade à mão) em tipos de jogador, e um classificador prevê o tipo a partir dos primeiros 30 segundos de jogo; em 17 participantes, ajuste dinâmico com previsão de tipo superou as alternativas [F: missura2009player, §5 e §7]. O objetivo declarado é um ajuste que "does not bother the actual players" [F: missura2009player, §1].

## Algoritmos e modelos relevantes

A revisão de Zohaib classifica as abordagens desde 2009 em métodos probabilísticos, perceptrons e aprendizagem de preferência, *dynamic scripting*, Hamlet, aprendizagem por reforço, UCT com redes neurais, sistemas auto-organizáveis e modelagem afetiva por EEG [F: zohaib2018dda, Tabela 2 e §3]. Exemplos que a revisão relata: no *dynamic scripting*, das três variantes para jogo equilibrado, "high-fitness penalizing" não teve sucesso e as outras duas funcionaram [F: zohaib2018dda, §3.3]; num jogo de reabilitação, aprendizagem por reforço multiperiódica superou métodos multiobjetivo em satisfação e em habilidade motora [F: zohaib2018dda, §3.5]; com fNIRS, ajustar a carga de uma tarefa de simulação reduziu erros em 35% sobre a linha de base [F: zohaib2018dda, §3.8]. O autor declara que a amostra de abordagens "is neither complete nor exhaustive" [F: zohaib2018dda, §5]. Para jogos sérios, uma revisão de 75 artigos dos últimos cinco anos encontrou reabilitação e educação entre os usos mais comuns, de regras (lógica fuzzy) a modelos de jogador e aprendizagem de máquina, sem avaliação formal de risco de viés [F: vitekova2026dda, resumo]. Outra revisão de adaptação de dificuldade e personalização existe e não foi lida [F: paraschos2023game, metadados].

## Requisitos e pressupostos

- Uma variável observável que se relacione com o desafio sentido; a *challenge function* é heurística e precisa ser validada para o jogo [F: andrade2006balancing, §4].
- Parâmetros de jogo que mudam a dificuldade de forma previsível; o controle de estoque de Hamlet só serve a gêneros em que essa manipulação existe, e não a jogos de tabuleiro em que os lados têm os mesmos recursos [F: andrade2006balancing, §2].
- Clareza sobre o que está sendo ajustado: o desafio da mecânica ou a dificuldade da habilidade-alvo (ver `gam.diff.challenge-and-zpd`) [I].

## Vantagens e limitações

**Vantagens.** Num jogo de luta, o agente adaptativo teve a menor variância de desempenho entre jogadores de perfis diferentes e foi o preferido por 3 de 4 jogadores [F: andrade2006balancing, resultados]; o tamanho da amostra impede generalizar [I]. Num estudo com 120 participantes, um cronômetro adaptativo aumentou a imersão (efeito da adaptação F(1,114) = 22,37, p < 0,001, ηp² = 0,164) [F: denisova2019deceptive, §6.2.1].

**Riscos documentados.**

- *Percepção de manipulação.* A literatura de projeto supõe que o jogador se sente enganado; Andrade et al. e Zohaib tratam a adaptação imperceptível como requisito [F: andrade2006balancing, §2; zohaib2018dda, §1]. A evidência contraria parte do temor: informar que o jogo se adapta aumentou a imersão independentemente de a adaptação existir (F(2,114) = 5,08, p = 0,008, ηp² = 0,082), sem interação entre informação e adaptação [F: denisova2019deceptive, §6.2.1]. A revisão do mesmo artigo registra que, em jogos multijogador, a ajuda adaptativa a um jogador pode ser vista como vantagem injusta (os autores atribuem a Hunicke 2005 a identificação da injustiça percebida como problema central do balanceamento multijogador; esse texto existe [F: hunicke2005case, metadados] mas não foi lido), e que escalar a dificuldade com o progresso pode tirar a sensação de conquista [F: denisova2019deceptive, §3].
- *Perda de controle e autonomia.* O DDA tira controle do projetista e o passa ao código [F: hunicke2004hamlet, Prior Work]; do lado do jogador, a escolha entre adaptação feita pelo sistema e controlada pela pessoa é tema de `acs.adapt.algorithmic-adaptation-and-autonomy`. Constant e Levieux relatam um estudo em que o DDA baseado nas escolhas do jogador melhorou mais a sensação de controle que o baseado no desempenho [F: constant2019confidence, §2, citando Ang e Mitchell 2017].
- *Superconfiança.* Com dificuldade mantida perto de 50% de sucesso, jogadores superestimaram mais suas chances do que com dificuldade aleatória: no jogo motor, para 78% de chance objetiva de falha, a falha percebida foi 72% na condição aleatória e 37% na equilibrada [F: constant2019confidence, §5]. Os autores tratam isso como desejável; para uma atividade que também ensina autoavaliação, é um efeito colateral a medir [I].
- *Exploração.* Cinco participantes aprenderam a perder de propósito com aposta baixa para receber um desafio mais fácil e então apostar alto [F: constant2019confidence, §5]; o *rubber band* "often suffers from disbalance and exploitability" [F: missura2009player, §3].
- *Contaminação da medida.* Sob adaptação, a pontuação deixa de medir só o jogador: com cronômetro adaptativo as pontuações foram maiores e menos dispersas (F(1,114) = 11,63, p = 0,001, ηp² = 0,090), e o que se disse ao jogador também mudou a pontuação (F(2,114) = 5,66, p = 0,004, ηp² = 0,08) [F: denisova2019deceptive, §6.2.2]. Um controlador que persegue taxa de acerto fixa tende a tornar a taxa de acerto pouco informativa sobre habilidade; a informação passa para o nível de dificuldade alcançado, que precisa ser registrado e modelado (ver `lae.psy.reliability-and-validity`) [I].

## Alternativas e comparações

| Opção | Quem decide | Risco principal | Evidência lida |
|---|---|---|---|
| Níveis estáticos | jogador, uma vez | descompasso com evolução | [F: andrade2006balancing, §1] |
| DDA oculto | sistema | percepção de manipulação, exploração | [F: missura2009player; constant2019confidence] |
| DDA declarado | sistema, com aviso | expectativa altera a experiência | [F: denisova2019deceptive] |
| DDA por escolha do jogador | jogador, durante o jogo | escolhas abaixo da habilidade | [F: constant2019confidence, §2] |
| Pareamento entre humanos | sistema de matchmaking | ver `rtm.mp.matchmaking` | [I] |

## Métricas e métodos de avaliação

Andrade et al. combinam três fontes: registros (eficiência do agente, diferença de pontos de vida), questionários de satisfação e entrevistas, e separam uma fase de aprendizagem, encerrada por um ponto de controle, da fase de comparação [F: andrade2006balancing, §4]. Constant e Levieux estimam a dificuldade objetiva por regressão logística de efeitos mistos (parâmetro de dificuldade e tempo como efeitos fixos, intercepto aleatório por jogador) e a percebida por apostas antes de cada jogada [F: constant2019confidence, §4]. A imersão foi medida pelo *Immersive Experience Questionnaire* [F: denisova2019deceptive, §6.1.2]. Indicadores de engajamento ficam em `lae.ind.engagement-indicators`; em atividade educacional, o desfecho de aprendizagem precisa ser medido fora do laço adaptativo [I].

## Exemplo técnico independente de domínio

```
estado: nivel_jogo em [0,1], passo = 0.1, alvo = 0.5
a cada rodada:
    registrar(evento, nivel_jogo, resultado)          # o nível vai junto da evidência
    nivel_jogo += passo if resultado == sucesso else -passo
    nivel_jogo  = limitar(nivel_jogo, 0, 1)
    se alternancia_suspeita(ultimas_rodadas):         # perder de propósito para colher fácil
        congelar_ajuste(k rodadas)
relatorio: habilidade estimada por logit(sucesso) ~ nivel_jogo + tempo + (1|jogador)
```

A regra de passo fixo é a usada por Constant e Levieux [F: constant2019confidence, §4]; o registro do nível com a evidência e o congelamento contra exploração são recomendação deste documento [I].

## Relações com outros conceitos

Depende do modelo de desafio e da separação jogo/conteúdo (`gam.diff.challenge-and-zpd`) e do construto de flow (`gam.motiv.flow`). Complementa o sequenciamento de conteúdo (`adp.adapt.sequencing-policies`) e a telemetria como evidência (`gam.instr.telemetry-as-evidence`). Relaciona-se com autonomia diante da adaptação (`acs.adapt.algorithmic-adaptation-and-autonomy`), adaptação de jogos para acessibilidade (`acs.adapt.adapting-games-and-activities`), matchmaking (`rtm.mp.matchmaking`) e validade de medida (`lae.psy.reliability-and-validity`).

## Lacunas e questões abertas

- Os estudos lidos têm amostras pequenas (4 em Andrade et al., 17 em Missura e Gärtner) ou condições não aleatorizadas no mesmo período (Constant e Levieux aplicaram as condições em sessões com um mês de intervalo) [F: andrade2006balancing; missura2009player; constant2019confidence, §4].
- Não foi lido estudo que meça efeito do DDA sobre aprendizagem com grupo controle; a revisão de jogos sérios diz que a evidência sugere ganhos, com métricas limitadas [F: vitekova2026dda, resumo].
- O texto de Hunicke 2005 e o de DDA multijogador de Baldwin et al. não foram abertos [F: hunicke2005case, metadados; baldwin2013framework, metadados].
- Efeito do DDA, declarado ou oculto, em crianças e em populações neurodivergentes (ver `gam.evid.special-education-and-neurodivergence`) [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hunicke2004hamlet | academico | 2026-10-30 |
| hunicke2005case | academico (metadados) | 2026-10-30 |
| zohaib2018dda | academico | 2026-10-30 |
| andrade2006balancing | academico | 2026-10-30 |
| missura2009player | academico | 2026-10-30 |
| constant2019confidence | academico | 2026-10-30 |
| denisova2019deceptive | academico | 2026-10-30 |
| vitekova2026dda | academico (resumo) | 2026-10-30 |
| paraschos2023game | academico (metadados) | 2026-10-30 |
| baldwin2013framework | academico (metadados) | 2026-10-30 |
