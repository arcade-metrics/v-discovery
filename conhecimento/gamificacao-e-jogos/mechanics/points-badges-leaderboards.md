---
id: gam.mech.points-badges-leaderboards
titulo: Pontos, insígnias e placares
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [sailer2017gamification, mekler2017towards, landers2017gamification, landers2015goalsetting, hanus2015assessing, denny2013effect, brom2019gamifying, katz2014differential, zagal2013dark]
relacoes:
  - { tipo: parte-de, alvo: gam.fund.gamification }
  - { tipo: depende-de, alvo: gam.motiv.self-determination-theory }
  - { tipo: relacionado-a, alvo: gam.motiv.intrinsic-extrinsic-and-overjustification }
  - { tipo: complementa, alvo: gam.motiv.feedback-design }
  - { tipo: relacionado-a, alvo: gam.social.cooperation-vs-competition }
  - { tipo: complementa, alvo: gam.mech.core-loops-and-progression }
  - { tipo: relacionado-a, alvo: gam.mech.streaks-loss-aversion-and-dark-patterns }
  - { tipo: avaliado-por, alvo: gam.evid.meta-analyses }
  - { tipo: avaliado-por, alvo: lae.evalm.experimental-design }
termos: [pontos, insígnia, badge, placar, leaderboard, nível, gráfico de desempenho, feedback granular, feedback cumulativo, comparação social, definição de metas, quantidade x qualidade, PBL]
---

# Pontos, insígnias e placares

## Definição e terminologia

Pontos, insígnias (badges, conquistas) e placares (leaderboards), às vezes abreviados como PBL, são os elementos de jogo mais usados em gamificação [I]. Sailer et al. descrevem a função de cada um: pontos dão "granular feedback, which can be directly connected to the actions of the player"; gráficos de desempenho dão feedback sustentado; insígnias e placares "assess a series of player actions" e dão feedback cumulativo [F: sailer2017gamification, §5]. Níveis são marcos de progressão sobre uma escala de pontos e são tratados em `gam.mech.core-loops-and-progression`.

O que não é: nenhum desses elementos é, sozinho, um jogo. São camadas de registro e comparação sobre uma atividade que continua igual [I]; ver `gam.fund.gamification`.

## Problema que resolve

Os elementos são usados para aumentar participação e persistência. A hipótese teórica mais citada vem da teoria da autodeterminação: o feedback dos elementos satisfaria a necessidade de competência e, com isso, a motivação intrínseca [F: sailer2017gamification, §5; mekler2017towards, §2.1]. Uma hipótese alternativa trata o placar como **definição implícita de metas**: Landers et al. testaram se a teoria de definição de metas explica por que placares funcionam [F: landers2017gamification, metadados; landers2015goalsetting].

## Fundamentos e funcionamento

### Informacional ou controlador

Mekler et al. resumem a teoria da avaliação cognitiva: o efeito de uma recompensa extrínseca sobre a motivação intrínseca depende de ela ser percebida como informacional ou controladora; feedback positivo percebido como controlador pode reduzir autonomia e motivação intrínseca [F: mekler2017towards, §2.1]. O detalhamento teórico, incluindo a metanálise de Deci, Koestner e Ryan, fica em `gam.motiv.intrinsic-extrinsic-and-overjustification`.

### O que os experimentos mostram

**Sailer et al. (2017)**: experimento aleatorizado on-line, simulação de separação de pedidos em armazém, 419 participantes completos, média de idade 22 anos; após excluir 88 que não perceberam os elementos da sua condição, N = 331 [F: sailer2017gamification, §6.3]. Todas as condições tinham pontos. A condição com insígnias, placar e gráfico de desempenho aumentou a competência percebida (F(2,328) = 3,39, ηp² = 0,020) e o sentido de significado da tarefa (ηp² = 0,018) em relação ao controle; não afetou a liberdade de decisão [F: sailer2017gamification, §6.4]. Os três elementos foram testados em bloco, sem separar o efeito de cada um, e foi medida satisfação de necessidades, não aprendizagem [I].

**Mekler et al. (2017)**: experimento 4 x 2 on-line com 273 adultos (idade média 32,8 anos) rotulando pinturas; condições sem elementos, com pontos, com placar (fictício) e com níveis [F: mekler2017towards, §3]. Os elementos aumentaram a quantidade de rótulos (F(3,265) = 10,09, ηp² = 0,103): pontos superaram o controle (d = 0,44) e placar e níveis superaram pontos (d = 0,39 e 0,35) [F: mekler2017towards, §4.1]. Não houve efeito sobre qualidade dos rótulos (ηp² = 0,008), motivação intrínseca nem competência; quantidade e qualidade se correlacionaram negativamente [F: mekler2017towards, §4]. Conclusão dos autores: os elementos "functioned as extrinsic incentives, effective only for promoting performance quantity" [F: mekler2017towards, resumo].

**Landers, Bauer e Callan (2017)**: brainstorming com cinco condições, quatro níveis clássicos de meta (faça o seu melhor, fácil, difícil, quase impossível) e um placar sem instrução; segundo o primeiro autor, "simply presenting the leaderboard resulted in similar achievement levels to those of the difficult and impossible goals", e quem não acreditava no placar teve desempenho pior [F: landers2015goalsetting]. O artigo só teve metadados verificados [F: landers2017gamification, metadados].

**Hanus e Fox (2015)**: estudo longitudinal em sala de aula universitária com insígnias e placar [F: hanus2015assessing, metadados]. Segundo a descrição de Brom et al., a versão gamificada não melhorou notas nem esforço autorrelatado e foi "detrimental to their intrinsic motivation, satisfaction and, to some extent, sense of empowerment" [F: brom2019gamifying, "Edu-gamification Studies with Comparative Design"].

**Brom et al. (2019)**: 98 universitários estudaram por duas horas uma simulação com e sem meta de jogo, escolha, pontos, moeda virtual e elogio; não houve diferença em aprendizagem nem em motivação intrínseca; a versão gamificada foi percebida como mais fácil (ηp² = 0,10; d = 0,74 e 0,42 contra os dois controles) [F: brom2019gamifying, resumo]. A mesma revisão relata, de estudos de de-Marcos et al., que versões competitivas de um curso melhoraram a entrega de tarefas mas "hindered conceptual learning" [F: brom2019gamifying, "Edu-gamification Studies with Comparative Design"].

**Denny (2013)**: estudo de insígnias numa plataforma de questões criadas por estudantes; o resumo afirma que havia "little empirical evidence" sobre a eficácia de insígnias [F: denny2013effect, resumo]. Os resultados não foram lidos nesta sessão.

### Crianças

O único experimento com crianças lido nesta área é o de Katz et al.: 107 crianças de 6 a 14 anos em acampamentos escolares, sete versões de um treino de memória de trabalho, versões sorteadas por acampamento [F: katz2014differential, "Participants"]. O grupo que não via pontos durante o jogo melhorou mais que o grupo que via (F(1,103) = 7,937, p = 0,006, ηp² = 0,072) [F: katz2014differential, "Results"]. Os autores consideram os achados preliminares pela amostra pequena e pela duração de três dias [F: katz2014differential, resumo].

## Vantagens e limitações

Vantagens com evidência experimental: aumento de quantidade de ação [F: mekler2017towards] e de competência percebida [F: sailer2017gamification]; o placar se comporta como meta difícil [F: landers2015goalsetting]. Limitações com evidência: ausência de efeito sobre qualidade, motivação intrínseca e aprendizagem em adultos [F: mekler2017towards; brom2019gamifying], efeito negativo sobre motivação e satisfação em sala de aula (descrito por terceiros) [F: brom2019gamifying] e efeito negativo da pontuação visível sobre ganho de treino em crianças [F: katz2014differential]. Quase toda a evidência é com adultos, em sessões únicas, com tarefas sem conteúdo curricular [I].

Riscos documentados além do efeito médio: a rivalidade de placar pode ser monetizada ("pay to win"), padrão que Zagal, Björk e Lewis classificam como escuro [F: zagal2013dark, §4.2]; e quem está no fim do placar pode ser desmotivado, possibilidade discutida por Sailer et al. a partir da literatura [F: sailer2017gamification, §3].

## Alternativas e comparações

| Elemento | Construto pretendido | Achado experimental lido | Risco principal |
|---|---|---|---|
| Pontos | competência (feedback granular) | +quantidade (d = 0,44), sem efeito em motivação intrínseca [F: mekler2017towards]; pior ganho de treino em crianças [F: katz2014differential] | quantidade em vez de qualidade |
| Insígnias | competência (feedback cumulativo), metas | só em bloco com placar e gráfico [F: sailer2017gamification] | controle percebido quando obrigatórias [I] |
| Placar | comparação social, meta implícita | ≈ meta difícil [F: landers2015goalsetting]; +quantidade (d = 0,39 sobre pontos) [F: mekler2017towards] | desmotivação de quem está atrás; rivalidade monetizada [F: zagal2013dark] |
| Gráfico de desempenho | competência, autocomparação | só em bloco [F: sailer2017gamification] | não estudado isoladamente [I] |

## Métricas e métodos de avaliação

Testar um elemento por vez contra uma condição sem ele, e medir separadamente quantidade, qualidade, motivação intrínseca e aprendizagem [I]; verificar se o participante percebeu o elemento, como Sailer et al. fizeram [F: sailer2017gamification, §6.3]. Para efeitos médios agregados por elemento, ver `gam.evid.meta-analyses`; para desenho, `lae.evalm.experimental-design`.

## Exemplo técnico independente de domínio

```
pontos:   concedidos por acerto em item novo ou corrigido; nunca por volume bruto
insignia: marca de domínio ("leu 20 palavras novas sem ajuda"), opcional, nunca bloqueia conteúdo
placar:   desligado por padrão para crianças;
          se ativo: só contra o próprio histórico ou em equipe, sem posições públicas individuais
registro: condição de exibição (pontos visíveis s/n) gravada com cada evento, para análise
```

## Relações com outros conceitos

Parte de `gam.fund.gamification`; depende de `gam.motiv.self-determination-theory` e relaciona-se com `gam.motiv.intrinsic-extrinsic-and-overjustification` e `gam.social.cooperation-vs-competition`; complementa `gam.motiv.feedback-design` e `gam.mech.core-loops-and-progression`. Os riscos de retorno compulsório estão em `gam.mech.streaks-loss-aversion-and-dark-patterns`. Avaliado por `gam.evid.meta-analyses` e `lae.evalm.experimental-design`.

## Lacunas e questões abertas

- Hanus e Fox (2015), Landers et al. (2017) e Denny (2013) não tiveram o texto integral lido; os números ficam por verificar.
- Faltam experimentos com crianças, com conteúdo curricular e com duração de semanas; não se localizou nenhum com crianças com deficiência.
- Não se verificou se o efeito de quantidade persiste após a retirada dos elementos.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| sailer2017gamification | academico | 2026-10-30 |
| mekler2017towards | academico | 2026-10-30 |
| landers2017gamification | academico [metadados] | 2026-10-30 |
| landers2015goalsetting | tecnico (blog do autor) | 2026-10-30 |
| hanus2015assessing | academico [metadados] | 2026-10-30 |
| denny2013effect | academico [metadados] | 2026-10-30 |
| brom2019gamifying | academico | 2026-10-30 |
| katz2014differential | academico | 2026-10-30 |
| zagal2013dark | academico | 2026-10-30 |
