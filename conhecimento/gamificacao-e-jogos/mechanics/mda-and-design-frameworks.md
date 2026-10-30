---
id: gam.mech.mda-and-design-frameworks
titulo: MDA e frameworks de projeto de jogos
tipo: framework
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [hunicke2004mda, arnab2015mapping, walk2017dde, salen2004rules, czauderna2019gameplay, guardiola2016gameplay, dormans2011simulating, sailer2017gamification]
relacoes:
  - { tipo: complementa, alvo: gam.mech.core-loops-and-progression }
  - { tipo: relacionado-a, alvo: gam.fund.serious-games-and-gbl }
  - { tipo: relacionado-a, alvo: gam.fund.gamification }
  - { tipo: complementa, alvo: gam.instr.evidence-centered-design }
  - { tipo: relacionado-a, alvo: gam.instr.telemetry-as-evidence }
  - { tipo: relacionado-a, alvo: gam.motiv.self-determination-theory }
  - { tipo: relacionado-a, alvo: dat.qual.granularity-and-constructs }
  - { tipo: relacionado-a, alvo: acs.adapt.adapting-games-and-activities }
termos: [MDA, mecânica, dinâmica, estética, sistema de feedback, LM-GM, mecânica de aprendizagem, mecânica de jogo, serious game mechanic, DDE, gameplay loop]
---

# MDA e frameworks de projeto de jogos

## Definição e terminologia

**MDA** (Mechanics, Dynamics, Aesthetics) é um framework de análise e projeto de jogos apresentado por Hunicke, LeBlanc e Zubek, "developed and taught as part of the Game Design and Tuning Workshop at the Game Developers Conference, San Jose 2001-2004" [F: hunicke2004mda, resumo]. Separa o jogo em três camadas causalmente ligadas: **mecânicas**, "the particular components of the game, at the level of data representation and algorithms"; **dinâmicas**, "the run-time behavior of the mechanics acting on player inputs and each others' outputs over time"; e **estéticas**, "the desirable emotional responses evoked in the player" [F: hunicke2004mda, "MDA"]. A tese central é que jogos são "more like artifacts than media": o conteúdo de um jogo "is its behavior" [F: hunicke2004mda, "MDA"].

**LM-GM** (Learning Mechanics-Game Mechanics) é um modelo de Arnab et al. para analisar e projetar jogos sérios mapeando, em cada situação de jogo, que mecânica de aprendizagem se realiza por meio de que mecânica de jogo [F: arnab2015mapping, resumo]. O elo entre as duas é a **serious game mechanic (SGM)**, "the design decision that concretely realises the transition of a learning practice/goal into a mechanical element of game-play" [F: arnab2015mapping, introdução].

O que não é: nenhum dos dois é uma teoria de motivação nem prediz aprendizagem. MDA não tem construto psicológico medido; suas "estéticas" são um vocabulário, não escalas [I]. Para motivação, ver `gam.motiv.self-determination-theory`.

## Problema que resolve

Jogos produzem comportamento difícil de prever: "the string of events that occur during gameplay and the outcome of those events are unknown at the time the product is finished" [F: hunicke2004mda, "MDA"]. Projetistas mexem em regras; jogadores vivem experiências. Sem um vocabulário que ligue as duas pontas, uma mudança de regra tem efeito imprevisto sobre a experiência. Em jogos educacionais o problema dobra: além de ligar regra e experiência, é preciso ligar regra e objetivo de aprendizagem. Arnab et al. partem do pressuposto de que o aspecto fundamental do projeto de jogo sério é "the translation of learning goals/practices into mechanical element of game-play" [F: arnab2015mapping, resumo].

## Fundamentos e funcionamento

### As duas perspectivas do MDA

Do lado do projetista, "the mechanics give rise to dynamic system behavior, which in turn leads to particular aesthetic experiences"; do lado do jogador, a ordem se inverte: estética define o tom, que aparece em dinâmicas observáveis e, por fim, em mecânicas operáveis [F: hunicke2004mda, "MDA as Lens"]. Os autores recomendam começar pela estética para favorecer projeto "experience-driven (as opposed to feature-driven)" [F: hunicke2004mda, "MDA"].

O artigo propõe oito estéticas: sensação, fantasia, narrativa, desafio, companheirismo (fellowship), descoberta, expressão e submissão ("game as pastime"), declarando que não há "Grand Unified Theory" que diga que combinação produz diversão [F: hunicke2004mda, "Aesthetics"].

### Modelos de dinâmica e sistemas de feedback

O instrumento analítico mais útil do MDA é tratar dinâmicas como sistemas de feedback. No exemplo do Monopoly, quem lidera acumula riqueza e pune os demais com eficácia crescente; "as the gap widens, only a few (and sometimes only one) of the players is really invested" [F: hunicke2004mda, "Dynamic Models"]. As correções propostas são mecânicas: subsídios a quem está atrás, impostos a quem está à frente, ou pressão de tempo [F: hunicke2004mda, "Mechanics"]. O ajuste fino ("tuning") é iterativo e por teste com jogadores [F: hunicke2004mda, "Tuning"]. O mesmo artigo mostra a variação de público: a versão para crianças de 3 a 7 anos privilegia exploração e descoberta "more important than challenge" [F: hunicke2004mda, "First Pass"].

Dormans formaliza essa ideia ao modelar a "economia interna" do jogo como fluxo de recursos: os diagramas Machinations "foreground the feedback structures" que, em grande parte, determinam o comportamento dinâmico do jogo [F: dormans2011simulating, "Introduction"]; ver `gam.mech.core-loops-and-progression`.

### LM-GM: do objetivo pedagógico à ação do jogador

O modelo traz listas pré-definidas de mecânicas de aprendizagem (organizadas pela taxonomia revisada de Bloom) e de mecânicas de jogo, e o analista desenha um mapa ligando LMs e GMs ao longo do fluxo de ações [F: arnab2015mapping]. Os autores advertem que o LM-GM "is not a formulaic means to design SGs" [F: arnab2015mapping].

## Vantagens e limitações

O MDA dá linguagem comum a projetistas e pesquisadores e explica efeitos em cascata de pequenas mudanças. Limitações: (a) é um texto curto de workshop, sem validação empírica [I]; (b) as oito estéticas são uma lista aberta e não operacionalizada [F: hunicke2004mda, "Aesthetics"]; (c) a literatura posterior registra críticas: o capítulo DDE (Walk, Görlich e Barrett, 2017) propõe uma revisão do MDA chamada Design, Dynamics, Experience [F: walk2017dde, metadados]; o conteúdo das críticas não foi verificado nesta sessão.

A evidência sobre o LM-GM é pequena. No primeiro teste, com 10 estudantes de engenharia (3 descartados), a análise com LM-GM melhorou as respostas dos participantes (Wilcoxon, T = 0, p = 0,031, N = 6), e os próprios autores dizem que a amostra "was too small to provide conclusive results" [F: arnab2015mapping, §4.1]. No segundo, com 26 participantes, a média SUS foi 67,3 para o LM-GM e 46,7 para o modelo comparado (GOM), embora a maioria achasse o GOM mais fácil de usar [F: arnab2015mapping, avaliação 2]. Isso mede usabilidade percebida do modelo, não qualidade dos jogos projetados com ele [I].

## Alternativas e comparações

| Framework | Unidade de análise | Liga a aprendizagem? | Evidência |
|---|---|---|---|
| MDA | camadas mecânica/dinâmica/estética | não | conceitual [F: hunicke2004mda] |
| DDE | revisão do MDA | não verificado | [F: walk2017dde, metadados] |
| LM-GM | situação de jogo, par LM-GM | sim, por Bloom | testes de usabilidade pequenos [F: arnab2015mapping] |
| Gameplay loop | sequência curta de ações do jogador | sim, na versão educacional | estudo de caso [F: czauderna2019gameplay] |
| Machinations | fluxo de recursos e feedback | não | simulação de balanceamento [F: dormans2011simulating] |

O gameplay loop (Guardiola) modela o ciclo de ações do jogador para projeto e análise [F: guardiola2016gameplay, resumo]; Czauderna e Guardiola argumentam que os métodos de projeto educacional anteriores, incluindo o LM-GM, observam as ações "rather superficially" e propõem a sequência curta de ações como unidade [F: czauderna2019gameplay]. Salen e Zimmerman (2004) são a referência acadêmica de fundamentos de projeto de jogos [F: salen2004rules, metadados]; a definição de jogo do livro, "a system in which players engage in an artificial conflict, defined by rules, that results in a quantifiable outcome", foi lida aqui como citada por Sailer et al. [F: sailer2017gamification, nota 1].

## Exemplo técnico independente de domínio

```
objetivo_aprendizagem: "associar letra ao som"
estetica_alvo: [descoberta, desafio]           # MDA, perspectiva do jogador
dinamica_desejada: "tentativa curta, erro barato, feedback imediato"
mecanicas:                                       # MDA, perspectiva do projetista
  - ouvir_som -> escolher_entre_3_letras -> feedback
mapa_lm_gm:                                      # LM-GM
  - LM: "identificar"   GM: "seleção sob escolha"   SGM: "escolha É a resposta"
  - LM: "repetir"       GM: "rodadas"               SGM: "rodada = item de prática"
checagem: cada GM sem LM correspondente é ruído ou motivação extrínseca; registrar
```

## Relações com outros conceitos

Complementa `gam.mech.core-loops-and-progression` (que detalha loops e economias) e `gam.instr.evidence-centered-design` (o LM-GM declara intenção pedagógica; o ECD exige o vínculo entre ação e evidência, também tratado em `gam.instr.telemetry-as-evidence` e `dat.qual.granularity-and-constructs`). Relaciona-se com `gam.fund.serious-games-and-gbl`, `gam.fund.gamification`, `acs.adapt.adapting-games-and-activities` e com a teoria motivacional de `gam.motiv.self-determination-theory`.

## Lacunas e questões abertas

- O texto do capítulo DDE e de Salen e Zimmerman não foi lido; as críticas ao MDA precisam ser verificadas na fonte.
- Não se localizou estudo que compare jogos projetados com e sem um desses frameworks quanto a aprendizagem.
- O evento exato e a paginação do artigo MDA não foram verificados no próprio PDF.
- Nenhum dos frameworks trata explicitamente de acessibilidade ou de crianças com deficiência; a adaptação de mecânicas fica em `acs.adapt.adapting-games-and-activities`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hunicke2004mda | academico (artigo de workshop) | 2026-10-30 |
| arnab2015mapping | academico | 2026-10-30 |
| walk2017dde | academico [metadados] | 2026-10-30 |
| salen2004rules | academico [metadados] | 2026-10-30 |
| guardiola2016gameplay | academico [metadados] | 2026-10-30 |
| czauderna2019gameplay | academico | 2026-10-30 |
| dormans2011simulating | academico | 2026-10-30 |
| sailer2017gamification | academico | 2026-10-30 |
