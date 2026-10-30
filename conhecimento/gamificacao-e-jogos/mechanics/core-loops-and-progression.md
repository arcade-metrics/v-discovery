---
id: gam.mech.core-loops-and-progression
titulo: Loops de jogo, progressão e economias internas
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [guardiola2016gameplay, czauderna2019gameplay, dormans2011simulating, adams2012game, sellers2017advanced, hunicke2004mda, mekler2017towards, sailer2017gamification, katz2014differential, zagal2013dark, gray2018dark]
relacoes:
  - { tipo: complementa, alvo: gam.mech.mda-and-design-frameworks }
  - { tipo: complementa, alvo: gam.mech.points-badges-leaderboards }
  - { tipo: relacionado-a, alvo: gam.mech.streaks-loss-aversion-and-dark-patterns }
  - { tipo: depende-de, alvo: gam.diff.challenge-and-zpd }
  - { tipo: complementa, alvo: gam.diff.dynamic-difficulty-adjustment }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
  - { tipo: relacionado-a, alvo: gam.motiv.feedback-design }
  - { tipo: relacionado-a, alvo: dat.ev.game-telemetry }
  - { tipo: avaliado-por, alvo: lae.ind.engagement-indicators }
termos: [core loop, gameplay loop, progressão, nível, barra de progresso, economia interna, recurso, fonte, dreno, conversor, feedback positivo, feedback negativo, grinding, playing by appointment]
---

# Loops de jogo, progressão e economias internas

## Definição e terminologia

- **Gameplay loop** (ou **core loop**): o ciclo curto e repetido de ações do jogador que constitui a atividade central do jogo. Guardiola propõe uma delineação formal do gameplay loop, aplicável a projeto e análise, que trata o loop como "the potentials states of the player in the game system" [F: guardiola2016gameplay, resumo]. Na prática descrita por Czauderna e Guardiola, o método lista ações do jogador "represented by verbs and minimal context" e as liga num fluxograma para formalizar "the core gameplay" [F: czauderna2019gameplay].
- **Progressão**: estrutura que ordena o acesso a conteúdo, desafio ou capacidade ao longo do tempo (níveis, árvores, caminhos, desbloqueios) [I]. Dormans distingue estruturas de emergência (regras que geram variação) de estruturas de progressão (sequências planejadas), tema de sua tese e do livro com Adams [F: adams2012game, metadados].
- **Economia interna**: segundo Dormans, apoiado em Adams e Rollings, os recursos do jogo "as well as the entities or actions that cause them to be produced, consumed and exchanged"; recursos podem ser concretos (moedas, munição) ou abstratos (habilidade, posição estratégica) [F: dormans2011simulating, "Internal Economy"].

O que não é: progressão no jogo não é progressão na aprendizagem. Um nível de jogo pode subir por tempo investido sem que o domínio do conteúdo mude [I]; o alinhamento entre as duas é o tema de `adp.adapt.sequencing-policies` e `gam.diff.challenge-and-zpd`.

## Problema que resolve

O loop define o que o jogador faz a maior parte do tempo; a progressão define por que voltar; a economia regula ritmo e equilíbrio [I]. Em jogos educacionais, a pergunta é se a ação repetida no loop é a própria prática do conteúdo ou uma atividade lateral. Czauderna e Guardiola dizem que métodos anteriores observam as ações dos aprendizes "rather superficially" e propõem a sequência curta de ações como unidade de análise para unir jogar e aprender [F: czauderna2019gameplay].

## Fundamentos e funcionamento

### Loop como unidade de projeto educacional

No estudo de caso de *Antura and the Letters*, jogo de alfabetização em árabe para crianças refugiadas, cada minijogo recebeu um gameplay loop em que as ações eram coloridas como pedagógicas ou não pedagógicas [F: czauderna2019gameplay]. O exercício revelou minijogos em que nenhuma habilidade além da pedagógica era desafiada e outros em que não foi possível separar ação lúdica de ação pedagógica (traçar a forma da letra é, ao mesmo tempo, controle motor e conteúdo) [F: czauderna2019gameplay]. Os autores relatam uma avaliação de impacto independente, com mais de 300 crianças em sessões diárias de 45 minutos por sete semanas, citada a partir de relatório de Koval-Saifi e Plass (2018) que não foi lido nesta sessão [F: czauderna2019gameplay].

### Economia interna e feedback

Os diagramas Machinations representam pools, fontes, drenos, conversores e negociadores (traders), funções econômicas que Dormans atribui a Adams e Rollings [F: dormans2011simulating, "Internal Economy"]. Um padrão recorrente é o **motor dinâmico**: "the more factories a player builds the quicker resources are produced", um laço de feedback positivo que amplia vantagens [F: dormans2011simulating, "Modeling SimWar"]. O MDA mostra o efeito desse tipo de laço sobre a experiência (o líder dispara e os demais desistem) e as correções por feedback negativo (subsídio aos atrasados, imposto aos líderes) [F: hunicke2004mda, "Dynamic Models"]. Sellers (2017) trata o projeto de jogos como projeto de sistemas [F: sellers2017advanced, metadados]; o conteúdo não foi verificado.

### Progressão visível: níveis, barras e gráficos

Experimentos que isolam elementos de progressão mostram efeitos sobre quantidade de ação, não sobre motivação intrínseca ou qualidade. Em Mekler et al. (adultos, N = 273, tarefa de rotular imagens), níveis exibidos como barra vertical de progresso aumentaram o número de rótulos em relação a só pontos (d = 0,35), sem efeito sobre qualidade, motivação intrínseca ou competência percebida [F: mekler2017towards, §4.1-4.2]. Em Sailer et al. (adultos, N = 331 após verificação de manipulação), o grupo com insígnias, placar e gráfico de desempenho relatou mais competência que o controle (ηp² = 0,020), mas o desenho não isola o gráfico dos outros dois elementos [F: sailer2017gamification, resultados].

Com crianças, o resultado pode ser o oposto. Num treino de memória de trabalho com 107 crianças de 6 a 14 anos, a versão que explicava vidas e níveis teve ganho de treino menor que a versão com todos os elementos, assim como a exibição de pontos em tempo real; os autores sugerem que esses elementos "may distract from the core cognitive training task" e reconhecem amostra pequena e intervenção curta [F: katz2014differential, resumo].

## Vantagens e limitações

Loops e economias explícitos permitem simular e balancear antes de construir [F: dormans2011simulating, resumo] e tornar visível o que o jogador repete [I]. Limitações e riscos documentados:

- **Grinding**: tarefas repetitivas para progredir; Zagal, Björk e Lewis o descrevem como padrão escuro quando serve apenas para alongar o jogo, e observam que jogadores "especially young or new ones" têm dificuldade de estimar quanto tempo o jogo exigirá [F: zagal2013dark, §4.1.1].
- **Playing by appointment**: progressão que exige jogar em horários definidos pelo jogo, com perda (o "withering") se o jogador não voltar; a "escuridão" se anula quando cumprir o horário não é necessário para progredir [F: zagal2013dark, §4.1.2].
- Gray et al. classificam como "gamification", dentro da estratégia "forced action", a situação em que partes do serviço só podem ser "earned" por uso repetido e talvez indesejado [F: gray2018dark, "Forced Action"].

Para uma atividade educacional, a implicação é que progressão deveria depender de evidência de domínio, não de tempo ou de comparecimento diário [I].

## Alternativas e comparações

| Estrutura | O que regula | Risco típico |
|---|---|---|
| Progressão por domínio | acesso ao próximo conteúdo por evidência de aprendizagem | depende de boa medida (`gam.instr.telemetry-as-evidence`) [I] |
| Progressão por volume (XP por ação) | acesso por quantidade de ação | grinding; quantidade sem qualidade [F: mekler2017towards; zagal2013dark] |
| Progressão por calendário | acesso por retorno em datas | playing by appointment [F: zagal2013dark] |
| Economia com feedback positivo | amplia vantagens | líder dispara, demais desistem [F: hunicke2004mda] |
| Economia com feedback negativo | reequilibra | reduz sensação de mérito [I] |

## Métricas e métodos de avaliação

Separar indicadores de loop (ações por sessão, tempo por ciclo) de indicadores de aprendizagem (acerto em itens novos, retenção), e não usar os primeiros como substitutos dos segundos [I]; ver `lae.ind.engagement-indicators` e `dat.ev.game-telemetry`. Para efeito de um elemento de progressão, o desenho adequado é o experimento que adiciona ou remove só esse elemento, como em Mekler et al. e Katz et al. [I].

## Exemplo técnico independente de domínio

```
loop:   apresentar_item -> responder -> feedback -> (proximo_item | revisar)
economia:
  fonte:  acerto_em_item_novo -> +1 "estrela"          # recompensa ligada ao construto
  dreno:  nenhum                                        # sem perda por ausência
progressao:
  desbloquear(unidade_k+1) se P(domínio(unidade_k)) >= 0.8   # por evidência, não por XP
  nunca: desbloquear por dias consecutivos; perder progresso por inatividade
registrar: cada desbloqueio com a evidência que o justificou
```

## Relações com outros conceitos

Complementa `gam.mech.mda-and-design-frameworks` e `gam.mech.points-badges-leaderboards`; os riscos de retorno compulsório continuam em `gam.mech.streaks-loss-aversion-and-dark-patterns`. Depende de `gam.diff.challenge-and-zpd` e complementa `gam.diff.dynamic-difficulty-adjustment`. Relaciona-se com `adp.adapt.sequencing-policies`, `gam.motiv.feedback-design` e `dat.ev.game-telemetry`.

## Lacunas e questões abertas

- Não se localizou estudo experimental sobre "core loops" como tal com aprendizes; a evidência é de elementos isolados (níveis, pontos) ou de estudos de caso.
- Sellers (2017) e Adams e Dormans (2012) só tiveram metadados verificados.
- O relatório de impacto citado por Czauderna e Guardiola não foi lido; o resultado é relatado pelos projetistas do jogo.
- Faltam estudos sobre progressão visível com crianças com deficiência intelectual ou TDAH, para quem barras e níveis podem ter outro efeito (ver `gam.evid.special-education-and-neurodivergence`).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| guardiola2016gameplay | academico [metadados] | 2026-10-30 |
| czauderna2019gameplay | academico | 2026-10-30 |
| dormans2011simulating | academico | 2026-10-30 |
| adams2012game | academico [metadados] | 2026-10-30 |
| sellers2017advanced | tecnico [metadados] | 2026-10-30 |
| hunicke2004mda | academico | 2026-10-30 |
| mekler2017towards | academico | 2026-10-30 |
| sailer2017gamification | academico | 2026-10-30 |
| katz2014differential | academico | 2026-10-30 |
| zagal2013dark | academico | 2026-10-30 |
| gray2018dark | academico | 2026-10-30 |
