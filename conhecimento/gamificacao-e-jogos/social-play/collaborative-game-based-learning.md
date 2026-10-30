---
id: gam.social.collaborative-game-based-learning
titulo: Aprendizagem colaborativa mediada por jogo
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [johnson2009educational, slavin2010cooperative, padillazea2015design, tervrugte2015competition, plass2013impact, sailer2020gamification, clark2016digital, sun2023systematic, bensasson2012enforce, porayskapomsta2018blending, carneiro2024serious, stone2018online]
relacoes:
  - { tipo: alternativa-a, alvo: gam.social.cooperation-vs-competition }
  - { tipo: parte-de, alvo: gam.fund.serious-games-and-gbl }
  - { tipo: relacionado-a, alvo: gam.mech.mda-and-design-frameworks }
  - { tipo: depende-de, alvo: ped.theory.sociocultural-and-zpd }
  - { tipo: relacionado-a, alvo: gam.evid.special-education-and-neurodivergence }
  - { tipo: relacionado-a, alvo: ped.incl.evidence-based-practices-by-population }
  - { tipo: complementa, alvo: acs.adapt.adapting-games-and-activities }
  - { tipo: complementa, alvo: rtm.mp.turn-based }
  - { tipo: avaliado-por, alvo: dat.ev.game-telemetry }
  - { tipo: relacionado-a, alvo: ped.std.single-case-designs }
termos: [aprendizagem colaborativa mediada por jogo, interdependência positiva, responsabilidade individual, interação promotora, processamento de grupo, metas de grupo, colaboração imposta, jogo livre, mediação do professor, andaimagem do professor, agrupamento heterogêneo, dominância na dupla]
---

# Aprendizagem colaborativa mediada por jogo

## Definição e terminologia

Aprendizagem colaborativa mediada por jogo é o arranjo em que duas ou mais pessoas jogam juntas com meta compartilhada e a aprendizagem depende da interação entre elas, não só da interação de cada uma com o jogo [I]. Entra no mesmo campo da aprendizagem cooperativa, cuja base teórica é a interdependência social [F: johnson2009educational, resumo], e da aprendizagem colaborativa apoiada por computador (CSCL).

Termos centrais:

- **Interdependência positiva**: o sucesso de cada membro depende do sucesso dos outros. É um dos cinco pilares da aprendizagem cooperativa de Johnson e Johnson, ao lado de **responsabilidade individual**, **interação promotora face a face**, **habilidades sociais** e **processamento (autoanálise) de grupo**, na lista que Padilla-Zea et al. adotam para projetar jogos colaborativos [F: padillazea2015design, §2].
- **Metas de grupo e responsabilidade individual**: na formulação de Slavin, o grupo trabalha por uma meta ou recompensa, e o sucesso dele depende da aprendizagem individual de cada membro [F: slavin2010cooperative, resumo do capítulo].
- **Colaboração imposta** (enforced collaboration): o jogo só aceita a ação quando os parceiros agem juntos, por exemplo arrastando a mesma peça ao mesmo tempo [F: bensasson2012enforce, resumo].

O que não é: jogar na mesma sala, ou em uma partida multiplayer, sem meta compartilhada nem dependência mútua é jogo em paralelo, não aprendizagem colaborativa [I]. A infraestrutura de partida (salas, turnos, sincronização) fica em `rtm.mp.turn-based` e documentos vizinhos.

## Problema que resolve

Juntar alunos diante de um jogo não basta. Slavin descreve o problema: quando a tarefa do grupo é produzir algo, e não garantir que cada um aprenda, o aluno mais capaz não tem motivo para explicar, e a participação do menos capaz "may be seen as interference rather than help" [F: slavin2010cooperative, seção sobre metas de grupo]. O conceito organiza as decisões de projeto e de mediação que tornam o jogo conjunto uma situação de aprendizagem [I].

## Fundamentos e funcionamento

### O que a pesquisa em aprendizagem cooperativa diz sobre a estrutura

- Métodos com recompensa de grupo baseada na soma da aprendizagem individual tiveram efeito mediano de +0,32 sobre desempenho em 64 estudos de pelo menos quatro semanas; métodos informais, sem essa estrutura, +0,07 [F: slavin2010cooperative, seção sobre metas de grupo].
- Quem mais ganha num grupo cooperativo é quem dá e recebe explicações elaboradas; dar ou receber respostas sem explicação se associou negativamente ao ganho [F: slavin2010cooperative, seção sobre metas de grupo, citando Webb].
- Os métodos estruturados beneficiam alunos de todos os níveis, e alunos de alto desempenho não perdem [F: slavin2010cooperative, seção sobre metas de grupo]. Em uma avaliação do método CIRC citada no capítulo, as análises separadas para alunos da educação especial deram efeitos de +0,99 em compreensão leitora e +0,90 em vocabulário [F: slavin2010cooperative, seção CIRC]. O método é de sala de aula, não um jogo digital.
- Para Johnson e Johnson, a teoria gerou procedimentos operacionais para o papel do professor na aprendizagem cooperativa [F: johnson2009educational, resumo]. A mediação faz parte do método.

### O que a evidência em jogos diz

- Jogar em grupo não supera de modo geral o jogo individual. Clark et al. comparam com Wouters et al. (2013), para quem o jogo em grupo superava o individual, e concluem que jogos colaborativos "may not be generally more effective" que os individuais; o arranjo pior foi o individual competitivo [F: clark2016digital, Discussão].
- Em gamificação, o subgrupo só colaborativo teve poucos estudos e intervalos largos: g = 0,40 [-0,67; 1,48], k = 2, em resultados cognitivos [F: sailer2020gamification, Tabela 2].
- No experimento de Plass et al. (N = 58), a colaboração reduziu o desempenho dentro do jogo na sessão, não mudou a fluência medida fora do jogo e aumentou a intenção de voltar a jogar e de recomendar o jogo [F: plass2013impact, resumo].
- Ter Vrugte et al. montaram duplas heterogêneas com interdependência positiva, interação promotora e responsabilidade individual (teste individual). Não houve efeito geral de colaboração, mas os alunos abaixo da média ganharam mais com colaboração sem competição [F: tervrugte2015competition, §6.1, §7]. Os autores sugerem roteiros de colaboração ou perguntas para guiar a discussão em trabalhos futuros [F: tervrugte2015competition, §8].

### Mediação do professor

A revisão sistemática de Sun et al. (24 estudos empíricos, ensino fundamental anos iniciais, 2011 a março de 2022) identificou estratégias de andaimagem do professor na fase de orientação e durante o jogo, com influência correlacional na aprendizagem, e pede mais pesquisa sobre a interação professor-aluno [F: sun2023systematic, resumo]. O texto integral não foi lido; a revisão não permite estimar o efeito causal da mediação [I].

### Educação especial: o caso do autismo

- **Colaboração imposta com crianças autistas**: seis duplas de crianças de 8 a 11 anos com TEA de alto funcionamento, num quebra-cabeça em mesa tátil. No modo de colaboração imposta houve mais interação social positiva e mais brincadeira colaborativa do que no jogo livre, sem diferença em comportamentos negativos. Os autores dizem que o desafio maior desse modo, sobretudo para crianças com menos habilidade sociocomunicativa, indica a necessidade de critérios de seleção e de "mediation steps" [F: bensasson2012enforce, resumo].
- **Agente virtual com profissional presente**: no ambiente ECHOES, a criança coopera com um agente virtual inteligente e um profissional humano acompanha. O estudo, com 29 crianças com TEA e dificuldades de aprendizagem de 4 a 14 anos em escolas do Reino Unido, das quais 15 entraram na análise, encontrou aumento significativo da proporção de respostas sociais dirigidas aos profissionais humanos e nenhuma evidência de transferência no pós-teste [F: porayskapomsta2018blending, resumo]. O desenho foi intrassujeitos, sem grupo controle [F: porayskapomsta2018blending, §4]. A interação com o humano não era exigida pelo jogo e consistia em encorajamento, demonstração e prontidão para responder às iniciativas da criança [F: porayskapomsta2018blending, §2.2]. A conclusão dos autores é que tecnologia e profissional devem se reforçar, e não um substituir o outro [F: porayskapomsta2018blending, §8].
- **Revisão de jogos sérios para habilidades sociais em TEA**: nove estudos incluídos; influência positiva sobre habilidades sociais e domínios relacionados, mas evidência limitada que pede desenhos rigorosos [F: carneiro2024serious, resumo]. Os autores registram que jogos participativos e colaborativos são promissores, mas podem aumentar o isolamento [F: carneiro2024serious, Discussão].
- **Jogos multiplayer comerciais**: estudo qualitativo com três alunos com TEA jogando Minecraft descreve apoio à conversa recíproca, à escrita e ao gesto como meios de interação [F: stone2018online, resumo]. É descritivo, sem medida de efeito.

**Resposta à pergunta do brief** [I]: as fontes lidas não sustentam que o jogo colaborativo, sozinho, melhore resultados de aprendizagem em educação especial. Os resultados positivos com crianças autistas são de interação social durante o jogo, em amostras muito pequenas, com mediação humana presente ou recomendada e sem evidência de transferência. Na pesquisa em sala de aula, o efeito depende de estrutura (metas de grupo, responsabilidade individual) e de procedimentos do professor. A conclusão prudente é tratar a mediação como parte da intervenção e avaliá-la junto, e não como opcional.

## Requisitos e pressupostos

- Meta do grupo que dependa da aprendizagem de cada membro, não de um produto único [F: slavin2010cooperative, seção sobre metas de grupo].
- Mecânica que exija contribuição de todos (recursos ou papéis complementares, ação conjunta), com nível de exigência compatível com o perfil social do aluno [F: bensasson2012enforce, resumo].
- Um adulto que saiba quando entrar e quando sair da interação [F: porayskapomsta2018blending, §2.2].
- Duplas heterogêneas pressupõem que a mecânica não premie a dominância do mais forte [F: tervrugte2015competition, §8].

## Vantagens e limitações

Vantagens: mais interesse, prazer e intenção de voltar a jogar [F: plass2013impact, resumo]; oportunidade de praticar interação social em contexto estruturado [F: bensasson2012enforce, resumo]. Limitações: efeito sobre aprendizagem não superior ao do jogo individual em média [F: clark2016digital, Discussão]; queda de desempenho dentro do jogo [F: plass2013impact, resumo]; exigência social que pode excluir justamente quem mais precisa [F: bensasson2012enforce, resumo]; custo de mediação.

## Métricas e métodos de avaliação

Medir aprendizagem individualmente, fora do jogo, e interação social com codificação de vídeo ou de eventos [F: bensasson2012enforce, resumo]. Padilla-Zea et al. propõem registrar mensagens trocadas entre membros em matrizes por categoria (comunicação, colaboração, coordenação) para análise de redes sociais [F: padillazea2015design, §3.4]. Com amostras pequenas, os desenhos de caso único (`ped.std.single-case-designs`) são mais adequados do que comparações de grupo [I].

## Exemplo técnico independente de domínio

```
regra de turno colaborativo:
    peça só se move se ação(A) e ação(B) chegam dentro de janela_t
    janela_t por perfil: ampla no início, reduzida conforme sucesso
eventos para evidência:
    iniciativa(quem, para_quem), resposta(quem, latência)
    ajuda_explicada(quem), ajuda_sem_explicação(quem)
    intervenção_do_mediador(tipo, momento)   # entra na análise, não é ruído
avaliação: teste individual pós-sessão + contagem de iniciativas por sessão
```

## Relações com outros conceitos

Alternativa e par da comparação em `gam.social.cooperation-vs-competition`; caso particular de `gam.fund.serious-games-and-gbl`; base teórica de mediação em `ped.theory.sociocultural-and-zpd`; evidência por população em `gam.evid.special-education-and-neurodivergence` e `ped.incl.evidence-based-practices-by-population`; adaptação do jogo ao perfil em `acs.adapt.adapting-games-and-activities`; turnos e partida em `rtm.mp.turn-based`; eventos em `dat.ev.game-telemetry`.

## Lacunas e questões abertas

- Nenhum estudo lido compara o mesmo jogo colaborativo com e sem mediação do professor; a pergunta do brief segue sem teste direto.
- Faltam estudos com deficiência intelectual e TDAH em jogos colaborativos.
- A colaboração imposta aumenta a interação durante o jogo; não se sabe se isso transfere para fora dele [I].
- Não localizamos nesta sessão as revisões de Sadka e Antle nem de Silva et al. sobre jogos colaborativos com mediador, nem Boyd et al. (2015); não citadas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| johnson2009educational | academico (resumo) | 2026-10-30 |
| slavin2010cooperative | academico | 2026-10-30 |
| padillazea2015design | academico | 2026-10-30 |
| tervrugte2015competition | academico | 2026-10-30 |
| plass2013impact | academico (resumo) | 2026-10-30 |
| sailer2020gamification | academico | 2026-10-30 |
| clark2016digital | academico | 2026-10-30 |
| sun2023systematic | academico (resumo) | 2026-10-30 |
| bensasson2012enforce | academico (resumo) | 2026-10-30 |
| porayskapomsta2018blending | academico | 2026-10-30 |
| carneiro2024serious | academico | 2026-10-30 |
| stone2018online | academico (resumo) | 2026-10-30 |
