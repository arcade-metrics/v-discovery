---
id: gam.motiv.self-determination-theory
titulo: Teoria da autodeterminação aplicada a jogos
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [ryan2000selfdetermination, ryan2006motivational, tyack2020selfdetermination, deterding2023objective, deci1999metaanalytic, bardach2023role]
relacoes:
  - { tipo: complementa, alvo: gam.motiv.intrinsic-extrinsic-and-overjustification }
  - { tipo: complementa, alvo: gam.motiv.flow }
  - { tipo: complementa, alvo: gam.motiv.feedback-design }
  - { tipo: relacionado-a, alvo: gam.mech.points-badges-leaderboards }
  - { tipo: relacionado-a, alvo: gam.social.cooperation-vs-competition }
  - { tipo: relacionado-a, alvo: gam.diff.challenge-and-zpd }
  - { tipo: relacionado-a, alvo: acs.part.self-determination }
  - { tipo: relacionado-a, alvo: acs.adapt.algorithmic-adaptation-and-autonomy }
  - { tipo: avaliado-por, alvo: lae.psy.reliability-and-validity }
termos: [teoria da autodeterminação, SDT, necessidades psicológicas básicas, autonomia, competência, relacionamento, cognitive evaluation theory, CET, organismic integration theory, OIT, locus de causalidade percebido, regulação externa, regulação introjetada, regulação identificada, regulação integrada, amotivação, PENS, IMI, controles intuitivos, presença]
---

# Teoria da autodeterminação aplicada a jogos

## Definição e terminologia

A teoria da autodeterminação (self-determination theory, SDT) é uma teoria da motivação humana que estuda as condições sociais que favorecem ou bloqueiam a motivação autônoma. Seu núcleo é o postulado de "three innate psychological needs--competence, autonomy, and relatedness" que, satisfeitas, levam a mais automotivação e saúde mental e, frustradas, a menos motivação e bem-estar [F: ryan2000selfdetermination, p. 68]. Aplicada a jogos, a SDT propõe que o "pull" motivacional de um jogo vem de quanto ele satisfaz essas necessidades durante a partida, e não de recompensas ou de traços do jogador [F: ryan2006motivational, resumo].

A SDT é organizada em subteorias. Duas importam aqui. A *cognitive evaluation theory* (CET) explica a variação da motivação intrínseca diante de eventos como recompensas e feedback [F: ryan2000selfdetermination, p. 70]. A *organismic integration theory* (OIT) descreve um contínuo de regulação, da amotivação à motivação intrínseca, passando pelas regulações externa, introjetada, identificada e integrada [F: ryan2000selfdetermination, p. 72-73]. Não é sinônimo de "teoria da diversão": a SDT não define o que torna um jogo divertido; ela prevê o efeito de condições do contexto sobre necessidades e motivação [I].

## Problema que resolve

Projetistas precisam saber por que um jogo é jogado de forma voluntária e quais elementos podem destruir esse engajamento quando o jogo é usado para fins educativos. A SDT oferece proposições testáveis sobre isso: o que aumenta competência percebida, o que muda o locus de causalidade percebido, e o que separa motivação autônoma de controlada [F: tyack2020selfdetermination, §Self-Determination Theory].

## Fundamentos e funcionamento

### Competência e autonomia na CET

A CET afirma que eventos que favorecem a sensação de competência durante a ação (desafio ótimo, feedback que promove eficácia, ausência de avaliações depreciativas) aumentam a motivação intrínseca, e que feedback de desempenho positivo a aumenta enquanto o negativo a reduz [F: ryan2000selfdetermination, p. 70]. Mas a competência só aumenta a motivação intrínseca "accompanied by a sense of autonomy", isto é, com locus de causalidade percebido interno [F: ryan2000selfdetermination, p. 70]. Recompensas tangíveis, ameaças, prazos, diretivas, avaliações sob pressão e metas impostas reduzem a motivação intrínseca; escolha e oportunidades de autodireção a aumentam [F: ryan2000selfdetermination, p. 70]. Os efeitos de recompensas são detalhados em `gam.motiv.intrinsic-extrinsic-and-overjustification`.

### Relacionamento

O relacionamento (relatedness) tem papel mais distal na motivação intrínseca: os autores citam estudos em que segurança de apego e suporte à autonomia da mãe predizem mais comportamento exploratório do bebê [F: ryan2000selfdetermination, p. 71]. Em jogos, ele aparece sobretudo no jogo multijogador [F: ryan2006motivational, estudo 4].

### Internalização (OIT)

A regulação introjetada é movida por culpa, ansiedade ou orgulho, "regulation by contingent self-esteem"; o envolvimento do ego é sua forma clássica [F: ryan2000selfdetermination, p. 72]. A identificada e a integrada são formas autônomas de motivação extrínseca. Para atividades educativas que não são intrinsecamente interessantes, a OIT é mais pertinente que a CET: o alvo passa a ser a internalização do valor da atividade, e não só a diversão [I].

### A aplicação a videogames: Ryan, Rigby e Przybylski (2006)

Quatro estudos aplicaram a SDT a jogos. Nos estudos 1 a 3, com 89, 50 e 58 universitários jogando 1, 2 e 4 jogos, autonomia e competência percebidas no jogo se associaram a diversão, preferência por jogar de novo e variação de bem-estar do pré ao pós-jogo [F: ryan2006motivational, resumo e §Study 1-3]. Controles intuitivos se relacionaram a competência e autonomia, e a mediação foi testada por regressões [F: ryan2006motivational, §Study 1]. O estudo 4 foi um levantamento com 730 membros de uma comunidade online de jogos multijogador (16 a 44 anos, média 22,1, 679 homens): autonomia, competência e relacionamento predisseram, cada um de forma independente, diversão e intenção de jogar no futuro [F: ryan2006motivational, resumo e §Study 4]. O instrumento criado, PENS (Player Experience of Need Satisfaction), tem subescalas de competência, autonomia, relacionamento, presença/imersão e controles intuitivos [F: tyack2020selfdetermination, §Self-Determination Theory].

## Requisitos e pressupostos

- A atividade precisa ter algum interesse intrínseco para que a CET se aplique; com atividades tediosas, o problema é de internalização (OIT) [F: deci1999metaanalytic, p. 651; ryan2000selfdetermination, p. 71].
- Autonomia em jogo pode ser afetada pelo desenho (opções, escolhas) ou pelo contexto (jogar por vontade x jogar para aprender); Tyack e Mekler recomendam declarar qual dos dois é estudado [F: tyack2020selfdetermination, §Future Directions].
- Nenhum dos quatro estudos de 2006 teve crianças; a generalização para elas é inferência [I].

## Vantagens e limitações

Vantagens: proposições explícitas e testáveis; instrumentos (PENS, IMI) usados em muitos estudos, o que facilita comparação [F: tyack2020selfdetermination, §Discussion]. Limitações documentadas:

- Na revisão de 110 artigos do CHI e CHI PLAY que citam a SDT, a maioria se engajou "in a rather shallow manner", com relatos descritivos da teoria, poucas referências às subteorias, e várias afirmações "dubious (and often uncited)" sobre como elementos de jogo se ligam a conceitos da SDT [F: tyack2020selfdetermination, §Shallow Engagement with SDT].
- A validação do PENS é limitada: os autores originais implicam validação não publicada; estudos independentes em geral apoiam a estrutura, mas não está claro se controles intuitivos e competência são fatores distintos, e itens de presença têm problemas recorrentes [F: tyack2020selfdetermination, §Self-Determination Theory].
- Os próprios autores de 2006 apontam que PENS e a medida de presença eram novos e precisavam de mais validação de construto, e que os efeitos de curto prazo sobre bem-estar foram mistos [F: ryan2006motivational, discussão final].
- Num experimento pré-registrado (n = 309) que manipulou o equilíbrio objetivo dificuldade-habilidade num jogo contra IA, o equilíbrio não afetou o comportamento de jogo; os autores concluem que a SDT e o flow estão "too underspecified to severely test" e que equilíbrio e competência importam menos para o engajamento comportamental do que se supõe [F: deterding2023objective, resumo].

## Alternativas e comparações

| Abordagem | O que explica | Ponto fraco para projeto |
|---|---|---|
| SDT (CET e OIT) | Efeito de contexto sobre necessidades e tipo de motivação | Subespecificada para prever um parâmetro de jogo [F: deterding2023objective, resumo] |
| Flow (`gam.motiv.flow`) | Estado de absorção em equilíbrio desafio-habilidade | Mede estado, não motivação de longo prazo [I] |
| Reforço e incentivo (tradição comportamental) | Frequência de comportamento sob contingência | Prevê pouco sobre o que acontece quando a contingência some [F: deci1999metaanalytic, p. 627] |
| Aprendizagem por recompensa (Murayama) | Transição de recompensa extrínseca para recompensa interna da aprendizagem | Proposta teórica recente, com testes ainda escassos [F: bardach2023role, conclusões] |

## Métricas e métodos de avaliação

PENS (necessidades no jogo), IMI (Intrinsic Motivation Inventory, motivação intrínseca e diversão) e medidas comportamentais de livre escolha. Na revisão de Tyack e Mekler, IMI e PENS apareceram cada um em 40% dos artigos [F: tyack2020selfdetermination, Tabela 1]. Recomenda-se, segundo os mesmos autores, ligar hipóteses explicitamente a proposições da SDT em vez de usá-la como justificativa a posteriori [F: tyack2020selfdetermination, §Future Directions]. Tempo de jogo livre (behavioral free choice) é o indicador clássico da CET; ver `lae.ind.engagement-indicators` e, sobre validade das escalas, `lae.psy.reliability-and-validity`.

## Exemplo técnico independente de domínio

Hipóteses testáveis para uma atividade lúdica, no formato que a revisão recomenda:

```
H1 (CET, competência): feedback informativo de progresso > feedback ausente
    -> medida: PENS-competência; tempo em livre escolha após a sessão
H2 (CET, autonomia): escolha de ordem das fases > ordem imposta
    -> medida: PENS-autonomia; IMI interesse
H3 (OIT): explicar por que a habilidade importa > não explicar
    -> medida: escala de regulação (externa, introjetada, identificada)
controle: mesmo conteúdo, mesma duração; registrar se a sessão foi voluntária ou obrigatória
```

## Relações com outros conceitos

Complementa `gam.motiv.intrinsic-extrinsic-and-overjustification` (efeitos de recompensas, que a CET prevê), `gam.motiv.flow` (competência e desafio) e `gam.motiv.feedback-design` (feedback como evento informativo ou controlador). Relaciona-se a `gam.mech.points-badges-leaderboards`, a `gam.social.cooperation-vs-competition` (relacionamento) e a `gam.diff.challenge-and-zpd` (desafio ótimo). No domínio de acessibilidade, a autodeterminação como direito e competência de pessoas com deficiência está em `acs.part.self-determination`, e o conflito entre adaptação automática e autonomia em `acs.adapt.algorithmic-adaptation-and-autonomy`.

## Lacunas e questões abertas

- Não se localizou validação do PENS com crianças nem com populações com deficiência intelectual ou TEA.
- Faltam testes que liguem um parâmetro de jogo a uma necessidade de forma causal; o experimento de Deterding e Cutting só teve o resumo lido.
- Não está claro como medir autonomia em jogo usado de forma obrigatória na escola, que muda o contexto do qual a CET depende.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ryan2000selfdetermination | academico | 2026-10-30 |
| ryan2006motivational | academico | 2026-10-30 |
| tyack2020selfdetermination | academico | 2026-10-30 |
| deterding2023objective | academico (resumo) | 2026-10-30 |
| deci1999metaanalytic | academico | 2026-10-30 |
| bardach2023role | academico (pré-print) | 2026-10-30 |
