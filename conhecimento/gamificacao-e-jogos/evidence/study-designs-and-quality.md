---
id: gam.evid.study-designs-and-quality
titulo: Desenhos de estudo e qualidade metodológica em jogos educacionais
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [mayer2019computer, wouters2013metaanalysis, clark2016digital, sailer2020gamification, cheung2016methodological, connolly2012systematic, boyle2016update, grossard2017serious, kollins2020novel, clinicaltrialsgov2016starsadhd]
relacoes:
  - { tipo: complementa, alvo: gam.evid.meta-analyses }
  - { tipo: complementa, alvo: gam.evid.special-education-and-neurodivergence }
  - { tipo: depende-de, alvo: lae.evalm.experimental-design }
  - { tipo: avaliado-por, alvo: lae.evalm.effect-size-and-replication }
  - { tipo: relacionado-a, alvo: ped.synth.meta-analysis-and-bias }
  - { tipo: relacionado-a, alvo: ped.std.single-case-designs }
  - { tipo: relacionado-a, alvo: lae.psy.reliability-and-validity }
  - { tipo: relacionado-a, alvo: lae.ind.engagement-indicators }
  - { tipo: relacionado-a, alvo: dat.ethics.research-vs-operation }
termos: [comparação de mídia, pesquisa de valor agregado, consequências cognitivas, ensaio randomizado, quase-experimento, pré e pós-teste, condição de controle ativo, viés de publicação, fail-safe N, teste de Egger, trim and fill, modelo de seleção, medida feita pelo pesquisador, transferência, escala de qualidade de Connolly]
---

# Desenhos de estudo e qualidade metodológica em jogos educacionais

## Definição e terminologia

"Desenho de estudo" é a forma como se compara quem jogou com quem não jogou, ou uma versão do jogo com outra. Mayer distingue três gêneros: **valor agregado** (versão base contra a mesma versão com um recurso a mais), **consequências cognitivas** (habilidade cognitiva geral depois de jogar um jogo comercial, contra atividade de controle) e **comparação de mídia** (conteúdo aprendido em jogo contra conteúdo em mídia convencional) [F: mayer2019computer, resumo]. Dentro de cada gênero, o desenho pode ser ensaio randomizado, quase-experimento (grupos não sorteados, muitas vezes turmas inteiras) ou só pós-teste [F: wouters2013metaanalysis, método].

O que não é: um estudo de usabilidade ou de aceitação, que mede se a pessoa gostou do jogo, não é estudo de eficácia de aprendizagem [I]. Grossard et al. encontraram exatamente esse caso em quatro jogos para autismo cujo único estudo media se os jogadores gostaram, sem medir mudança de habilidade [F: grossard2017serious, discussão].

## Problema que resolve

O efeito médio publicado depende do desenho. Saber ler o desenho evita adotar uma mecânica com base num efeito que desaparece quando o estudo é feito com rigor [I].

## Fundamentos e funcionamento

### O efeito encolhe com randomização

- Wouters et al.: a randomização atenua o efeito (z = 2,75, p = 0,003) e, nos estudos randomizados, os jogos sérios não foram mais eficazes que a instrução convencional [F: wouters2013metaanalysis, resultados]. Os autores advertem que, restringindo a estudos randomizados com pré e pós-teste, o efeito positivo "may disappear" [F: wouters2013metaanalysis, limitações].
- Clark et al., comparação de mídia: quase-experimentos g = 0,43 [0,22; 0,63], 25 estudos; experimentos randomizados g = 0,17 [0,004; 0,33], 32 estudos; diferença marginal (p = 0,051) [F: clark2016digital, Tabela 5].
- Sailer e Homner: no subconjunto de alto rigor (randomizados, ou quase-experimentos com pré e pós-teste), o efeito cognitivo se mantém (g = 0,42) mas os efeitos motivacional e comportamental deixam de ser significativos; quase-experimentos acharam efeito e experimentos não [F: sailer2020gamification, subconjunto e limitações].
- Em educação em geral, Cheung e Slavin, com 645 estudos de 12 revisões, acharam efeitos cerca de duas vezes maiores em artigos publicados, ensaios pequenos e medidas feitas pelo pesquisador, e efeitos maiores em quase-experimentos que em randomizados [F: cheung2016methodological, resumo].

### Qualidade do comparador e da descrição

Na metanálise de Clark, a qualidade da condição de comparação se associou negativamente ao efeito (b = -0,15); restringindo a comparadores de qualidade média ou melhor, o efeito de mídia caiu de 0,33 para 0,28 [F: clark2016digital, resultados]. Os autores observam que muitos estudos davam "only sparse descriptions of game or control interventions" [F: clark2016digital, discussão]. Para jogos sérios, a comparação com controle passivo (ler, assistir a slides) mede outra coisa que a comparação com prática ativa equivalente [I]; Wouters et al. separam os dois casos como moderador [F: wouters2013metaanalysis, método].

### Viés de publicação

As três metanálises testam o viés e não o encontram: Wouters por fail-safe N (3.489, acima do limiar de 395) [F: wouters2013metaanalysis, resultados]; Clark por funil, teste de Egger (p = 0,36 e 0,33) e trim and fill sem estudos imputados [F: clark2016digital, viés de publicação]; Sailer e Homner por funil, modelo de seleção e fail-safe N [F: sailer2020gamification, viés de publicação]. Os próprios Sailer e Homner lembram que a ausência de viés é "highly unlikely unless a set of preregistered reports is examined" [F: sailer2020gamification, viés de publicação]. Wouters notou que só três comparações vinham de trabalhos não publicados, o que dificulta detectar o viés [F: wouters2013metaanalysis, discussão].

### Medida do desfecho

Em 30 de 31 comparações de motivação de Wouters, a motivação foi medida por questionário depois do jogo; os autores sugerem medidas durante o jogo, comportamentais ou fisiológicas [F: wouters2013metaanalysis, discussão]. Sailer e Homner apontam a falta de instrumentos padronizados como fonte de variação de confiabilidade e validade não considerada no efeito médio [F: sailer2020gamification, limitações]. Clark et al. não acharam associação entre tipo de avaliação ou "overalignment" do teste e o efeito na comparação de mídia [F: clark2016digital, resultados].

### Revisões sistemáticas sem metanálise

Connolly et al. (2012) reuniram 129 artigos com evidência empírica sobre jogos para usuários de 14 anos ou mais; os desfechos mais frequentes foram aquisição de conhecimento e desfechos afetivos e motivacionais [F: connolly2012systematic, resumo]. A atualização de Boyle et al. selecionou 143 artigos de 2009 a 2014 com evidência de maior qualidade, com conhecimento como desfecho mais frequente em jogos para aprendizagem [F: boyle2016update, resumo]. A escala de qualidade de Connolly, usada por outras revisões, pontua tipo de estudo, método e análise, generalização (tamanho e representatividade da amostra), pertinência e confiança no resultado, de 1 a 3 cada, total máximo 15 [F: grossard2017serious, método]. Na revisão de Grossard et al., a concordância entre avaliadores foi alta no total (ICC = 0,95) mas baixa no critério de pertinência (ICC = 0,36) [F: grossard2017serious, método].

## Vantagens e limitações

| Desenho | Ganho | Risco principal |
|---|---|---|
| Comparação de mídia | Responde se vale trocar a aula pelo jogo | Confunde mídia, conteúdo, tempo e novidade [I] |
| Valor agregado | Isola uma mecânica | Pouca validade externa; poucos estudos (20 em Clark) [F: clark2016digital, Tabela 4] |
| Consequências cognitivas | Mede habilidade geral | Excluído das metanálises de Wouters por controle sem atividade [F: wouters2013metaanalysis, limitações] |
| Ensaio randomizado com controle ativo | Atribuição causal | Custo; desfecho primário pode ser estreito [I] |
| Caso único (single-case) | Viável com populações pequenas | Generalização depende de replicação [I] |

O ensaio STARS-ADHD ilustra um desenho forte com desfecho estreito: randomizado, duplo-cego, com controle digital ativo, 348 crianças; o desfecho primário era um teste computadorizado de atenção [F: kollins2020novel, resumo], e as escalas de sintomas melhoraram de forma parecida nos dois braços (ADHD-RS total: -6,2 contra -5,7) [F: clinicaltrialsgov2016starsadhd, resultados]. Detalhes em `gam.evid.special-education-and-neurodivergence`.

## Métricas e métodos de avaliação

Checklist mínimo para avaliar um estudo de jogo educacional, recomendado por este documento a partir das fontes acima [I]: atribuição (randomizada, por turma, nenhuma); comparador (passivo, ativo equivalente, versão do jogo); número de sessões; desfecho cognitivo medido fora do jogo, com instrumento independente; seguimento tardio; tamanho de amostra; descrição suficiente do jogo e do controle; registro prévio; financiamento.

## Exemplo técnico independente de domínio

```
classificar_evidencia(estudo):
  se estudo.desfecho in {gosto, usabilidade, tempo_de_uso}: retornar "aceitacao"
  se estudo.desfecho == desempenho_no_proprio_jogo: retornar "comportamento no jogo"
  nivel = "fraca"
  se estudo.controle e estudo.pre_pos: nivel = "moderada"
  se estudo.randomizado e estudo.controle_ativo e estudo.medida_independente:
      nivel = "forte"
  se nao estudo.seguimento: anotar("sem retencao")
  retornar nivel
```

## Relações com outros conceitos

Base metodológica de `gam.evid.meta-analyses` e `gam.evid.special-education-and-neurodivergence`. Depende de `lae.evalm.experimental-design`; tamanho de efeito em `lae.evalm.effect-size-and-replication`; síntese e viés em `ped.synth.meta-analysis-and-bias`; caso único em `ped.std.single-case-designs`. Engajamento medido por log, que não substitui desfecho de aprendizagem, em `lae.ind.engagement-indicators`.

## Lacunas e questões abertas

- Nenhuma metanálise lida avalia risco de viés por estudo com instrumento padronizado; usam desenho como moderador.
- Não há, nas fontes lidas, estimativa de efeito de novidade separada do efeito do jogo.
- Connolly 2012 e Boyle 2016 foram lidos só no resumo; os critérios de "maior qualidade" de Boyle não foram verificados.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| mayer2019computer | academico (resumo) | 2026-10-30 |
| wouters2013metaanalysis | academico | 2026-10-30 |
| clark2016digital | academico | 2026-10-30 |
| sailer2020gamification | academico | 2026-10-30 |
| cheung2016methodological | academico (resumo) | 2026-10-30 |
| connolly2012systematic | academico (resumo) | 2026-10-30 |
| boyle2016update | academico (resumo) | 2026-10-30 |
| grossard2017serious | academico | 2026-10-30 |
| kollins2020novel | academico (resumo) | 2026-10-30 |
| clinicaltrialsgov2016starsadhd | tecnico | 2026-10-30 |
