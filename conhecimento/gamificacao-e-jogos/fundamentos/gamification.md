---
id: gam.fund.gamification
titulo: Gamificação
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [deterding2011game, deterding2014game, hamari2014does, koivisto2019rise, seaborn2015gamification, landers2014developing, plass2015foundations, sailer2020gamification]
relacoes:
  - { tipo: parte-de, alvo: gam.fund.comparison }
  - { tipo: alternativa-a, alvo: gam.fund.serious-games-and-gbl }
  - { tipo: depende-de, alvo: gam.motiv.self-determination-theory }
  - { tipo: complementa, alvo: gam.mech.points-badges-leaderboards }
  - { tipo: complementa, alvo: gam.mech.mda-and-design-frameworks }
  - { tipo: relacionado-a, alvo: gam.motiv.intrinsic-extrinsic-and-overjustification }
  - { tipo: relacionado-a, alvo: gam.mech.streaks-loss-aversion-and-dark-patterns }
  - { tipo: avaliado-por, alvo: gam.evid.meta-analyses }
  - { tipo: avaliado-por, alvo: gam.evid.study-designs-and-quality }
  - { tipo: avaliado-por, alvo: lae.ind.engagement-indicators }
termos: [gamificação, elemento de design de jogo, contexto não lúdico, gamefulness, gameful design, gameful interaction, affordance motivacional, gamified learning, pointsification, ludus, paidia]
---

# Gamificação

## Definição e terminologia

A definição mais citada é a de Deterding, Dixon, Khaled e Nacke: gamificação é "the use of game design elements in non-game contexts" [F: deterding2011game, metadados; texto lido na tradução autorizada, deterding2014game, §4]. O texto original (MindTrek 2011, p. 9-15) não pôde ser aberto; o conteúdo abaixo vem da tradução francesa publicada em *Sciences du jeu* (2014), que reproduz o artigo, e de revisões que o citam com página (p. 9) [F: seaborn2015gamification, §3.2; sailer2020gamification, p. 78].

A definição tem quatro componentes, cada um com uma fronteira explícita [F: deterding2014game, §4.1 a §4.4]:

- **Jogo (game), não brincadeira (play).** Gamificação diz respeito ao jogo estruturado por regras e metas (*ludus*), não ao brincar livre e exploratório (*paidia*). Os autores propõem "gamefulness" como par de "playfulness", e distinguem a experiência (gamefulness), os artefatos que a proporcionam (gameful interaction) e a prática de projetar para obtê-la (gameful design).
- **Elementos, não jogo completo.** Um jogo sério é um jogo completo com fim não recreativo; a gamificação "n'emprunte aux jeux que quelques éléments de design". Os elementos não precisam ser exclusivos de jogos, mas devem ser "caractéristiques des jeux".
- **Design, não tecnologia.** O termo se refere a elementos de *design* de jogo, não a tecnologias de jogo (motores, controles) nem a práticas lúdicas em geral.
- **Contexto não lúdico, sem restrição de finalidade.** A definição não limita contexto, objetivo ou cenário; educação é um dos contextos possíveis.

Os autores organizam os elementos em cinco níveis de abstração: padrões de interface (insígnias, placares, níveis), padrões e mecânicas de jogo (tempo limitado, recursos limitados, turnos), princípios e heurísticas (metas claras, variedade de estilos de jogo), modelos de design de jogo (MDA, desafio-fantasia-curiosidade) e métodos de design (playtesting, design centrado no jogo) [F: deterding2014game, §4.3, tabela 1].

Definições concorrentes: Huotari e Hamari definem gamificação pelo resultado pretendido, "a process of enhancing a service with affordances for gameful experiences", sem exigir que o produto final não seja um jogo [F: seaborn2015gamification, §3.2, citando Huotari e Hamari 2012]. Hamari, Koivisto e Sarsa operam com essa linha: affordances motivacionais → resultados psicológicos → resultados comportamentais [F: hamari2014does, §2]. Koivisto e Hamari (2019) resumem: gamificação é projetar sistemas de informação "to afford similar experiences and motivations as games do, and consequently, attempting to affect user behavior" [F: koivisto2019rise, resumo]. Seaborn e Fels propõem uma síntese, "the intentional use of game elements for a gameful experience of non-game tasks and contexts" [F: seaborn2015gamification, §3.2].

O que não é: jogo sério, jogo com propósito (GWAP) ou jogo de realidade alternativa, que são jogos completos [F: seaborn2015gamification, §5.1]; nem "playificação" (funware, funology, qualidades lúdicas de Malone), da qual a gamificação seria um subconjunto orientado a estrutura e metas [F: seaborn2015gamification, §5.1].

## Problema que resolve

Atividades necessárias mas pouco atraentes (exercícios, tarefas repetitivas, uso de um serviço) sofrem com baixa adesão. A gamificação pretende aumentar motivação e engajamento e, por meio deles, mudar comportamento: "The most commonly stated objective behind using a gamified approach is to encourage behavior change" [F: seaborn2015gamification, §5.1]. Em educação, Plass, Homer e Kinzer descrevem a gamificação como uso de elementos de jogo, como sistemas de incentivo, "to motivate players to engage in a task they otherwise would not find attractive" [F: plass2015foundations, p. 259].

## Fundamentos e funcionamento

### Gamificação da aprendizagem: efeito indireto

A teoria da aprendizagem gamificada de Landers define gamificação como "the use of game attributes, as defined by the Bedwell taxonomy, outside the context of a game with the purpose of affecting learning-related behaviors or attitudes"; esses comportamentos e atitudes influenciam a aprendizagem moderando a relação entre qualidade do desenho instrucional e resultados, ou mediando-a diretamente [F: landers2014developing, resumo]. Landers contrasta isso com a abordagem de jogos sérios, em que a manipulação dos atributos de jogo "is typically intended to affect learning without this type of behavioral mediator/moderator" [F: landers2014developing, resumo]. Sailer e Homner acrescentam a consequência prática: como a gamificação não substitui a instrução, conteúdo instrucional eficaz é pré-requisito, e a teoria não diz quais mecanismos de aprendizagem os elementos acionam; para isso recorrem à teoria da autodeterminação [F: sailer2020gamification, p. 78-79].

### Processo, não produto

Sailer e Homner: a abordagem baseada em jogo implica projetar jogos completos, enquanto a gamificação altera um processo de aprendizagem existente para que seja experimentado como semelhante a jogo; "gamification is not a product in the way that a (serious) game is" [F: sailer2020gamification, p. 78]. Seaborn e Fels chegam a conclusão parecida: gamificação como uma abordagem de design, a "mentalidade do designer inspirada em jogos", mais do que uma propriedade do sistema [F: seaborn2015gamification, §5.3].

### Quais elementos se usam

Na revisão de Hamari et al., pontos, placares e insígnias foram "clearly the most commonly found variants" entre 10 categorias de affordances (também níveis, história/tema, metas claras, feedback, recompensas, progresso, desafio) [F: hamari2014does, §4.1, tabela 2]. Cinco anos depois, Koivisto e Hamari, com 819 estudos, relatam que pontos, insígnias e placares e os contextos educação, saúde e crowdsourcing "persist as the most common" [F: koivisto2019rise, resumo]. Seaborn e Fels chamam essa concentração de "pointsification" [F: seaborn2015gamification, §5.2].

## Vantagens e limitações

Vantagens [I]: custo de produção menor que o de um jogo, porque se acrescenta uma camada a uma atividade existente; independência do conteúdo; possibilidade de testar elementos isolados.

Limitações documentadas:
- **Efeito misto e dependente de contexto e usuário.** Hamari et al. (24 estudos empíricos) concluem que a gamificação "does work, but some caveats exist": a maioria dos estudos quantitativos encontrou efeitos positivos só em parte das relações testadas, e só dois tiveram todos os testes positivos [F: hamari2014does, §4.3, §5]. Koivisto e Hamari: os resultados pendem para o positivo, mas "the amount of mixed results is remarkable" [F: koivisto2019rise, resumo].
- **Fragilidade metodológica.** Amostras pequenas (cerca de N=20), instrumentos não validados, ausência de grupo controle, vários elementos testados em bloco, prazos curtos com possível efeito de novidade [F: hamari2014does, §5.1]. Seaborn e Fels: a maioria dos estudos aplicados não usou teoria nem definiu gamificação, faltou análise estatística e só um estudo (Thom et al. 2012) removeu os elementos num desenho cruzado [F: seaborn2015gamification, §5.2.2, §5.3].
- **Motivação extrínseca.** A literatura teórica converge para a teoria da autodeterminação e alerta que efeitos baseados em recompensa extrínseca podem ser temporários ou prejudiciais com o tempo [F: seaborn2015gamification, §5.1, §5.2.2]; o tema é aprofundado em `gam.motiv.intrinsic-extrinsic-and-overjustification`.
- **Crítica conceitual.** Plass et al. registram que, do ponto de vista de design de jogos, é menos desejável usar recursos de jogo para "enhance" mecânicas desinteressantes, mas que há pouca evidência sobre o impacto relativo das duas estratégias [F: plass2015foundations, p. 260].

## Métricas e métodos de avaliação

Hamari et al. separam três camadas mensuráveis: affordances implementadas (variável independente), resultados psicológicos (motivação, atitude, prazer) e resultados comportamentais (uso, participação, desempenho) [F: hamari2014does, §2, §4.2]. Em aprendizagem, Sailer e Homner usam resultados cognitivos, motivacionais e comportamentais e encontraram, em estudos de 2013 a 2017 com aprendizes de escola, ensino superior e formação profissional: cognitivos g = 0,49 (IC 95% 0,30 a 0,69; k = 19; N = 1686), motivacionais g = 0,36 (IC 0,18 a 0,54; k = 16; N = 2246), comportamentais g = 0,25 (IC 0,04 a 0,46; k = 9; N = 951); só o efeito cognitivo se manteve estável no subconjunto de alto rigor [F: sailer2020gamification, resumo e §Final Sample]. Detalhes e moderadores ficam em `gam.evid.meta-analyses`.

## Exemplo técnico independente de domínio

```
atividade_base = lista_de_exercicios(conteudo)      # instrução já existe
camada = {pontos: por_acerto, insignia: "10 seguidos", placar: semanal}
versao_gamificada = aplicar(camada, atividade_base)  # conteúdo e tarefa inalterados
avaliar:
  comparar(versao_gamificada, atividade_base)        # mesma instrução nos dois grupos
  medir(psicológico: motivação; comportamental: tentativas, retorno; cognitivo: pós-teste)
  isolar elementos (fatorial) e medir após retirada da camada
```

## Relações com outros conceitos

Alternativa a `gam.fund.serious-games-and-gbl` e comparada em `gam.fund.comparison`. Depende de `gam.motiv.self-determination-theory` como explicação dos efeitos; os elementos típicos estão em `gam.mech.points-badges-leaderboards` e os de risco em `gam.mech.streaks-loss-aversion-and-dark-patterns`; o nível "modelos de design" remete a `gam.mech.mda-and-design-frameworks`. Avaliada por `gam.evid.meta-analyses`, `gam.evid.study-designs-and-quality` e pelos indicadores de `lae.ind.engagement-indicators`.

## Lacunas e questões abertas

- O artigo original de Deterding et al. (ACM) não foi aberto; citações vêm da tradução francesa e de revisões que dão a página.
- O texto integral de Landers (2014) e de Koivisto e Hamari (2019) não foi aberto; só os resumos.
- Quantos elementos fazem um sistema gamificado virar jogo continua sem critério operacional; Deterding et al. e Seaborn e Fels reconhecem a subjetividade.
- Faltam estudos que isolem elementos e que meçam efeito após a retirada da camada; evidência com crianças pequenas e com educação especial não foi examinada aqui (ver `gam.evid.special-education-and-neurodivergence`).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| deterding2011game | academico [metadados] | 2026-10-30 |
| deterding2014game | academico (tradução do anterior, texto integral) | 2026-10-30 |
| hamari2014does | academico | 2026-10-30 |
| koivisto2019rise | academico (resumo) | 2026-10-30 |
| seaborn2015gamification | academico | 2026-10-30 |
| landers2014developing | academico (resumo) | 2026-10-30 |
| plass2015foundations | academico | 2026-10-30 |
| sailer2020gamification | academico | 2026-10-30 |
