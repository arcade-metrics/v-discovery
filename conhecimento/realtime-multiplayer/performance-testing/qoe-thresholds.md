---
id: rtm.perf.qoe-thresholds
titulo: Limiares de latência e qualidade de experiência por tipo de interação
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [claypool2006latency, claypool2006tr, pantel2002delay, sheldon2003warcraft, beigbeder2004unreal, itu2017g1032, itu2020g1072, ignat2015delay]
relacoes:
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: depende-de, alvo: rtm.perf.metrics }
  - { tipo: complementa, alvo: rtm.pred.client-side-prediction }
  - { tipo: complementa, alvo: rtm.pred.lag-compensation }
  - { tipo: complementa, alvo: rtm.mp.turn-based }
  - { tipo: complementa, alvo: rtm.sync.crdt }
  - { tipo: complementa, alvo: rtm.sync.operational-transformation }
  - { tipo: relacionado-a, alvo: rtm.perf.network-emulation }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [QoE, precisão, deadline, modelo avatar, modelo onipresente, perspectiva em primeira pessoa, MOS, opinion model, fatores de influência]
---

# Limiares de latência e qualidade de experiência por tipo de interação

## Definição e terminologia

Limiar de latência é o valor acima do qual a degradação de desempenho ou de experiência do usuário deixa de ser aceitável para um dado tipo de interação. Qualidade de experiência (QoE) é a avaliação subjetiva do usuário; a Recomendação ITU-T G.1032 organiza "a list of factors which may influence the quality of experience (QoE) of cloud gaming and online gaming", agrupados em "user, system, and context factors" [F: itu2017g1032]. Um *opinion model* é um modelo que prevê QoE (tipicamente MOS) a partir de parâmetros técnicos; a ITU-T G.1072 é um desses modelos para cloud gaming [F: itu2020g1072].

Este documento reúne apenas limiares com fonte verificada, separados por tipo de interação. Todo número aqui é [F] com a fonte, as condições e, quando disponível, o n; nenhum é extrapolação.

## Problema que resolve

"Quanto de latência é aceitável?" tem resposta diferente para um tiro, uma corrida, um lance de xadrez e uma edição de texto compartilhada. Usar um número único (por exemplo, "menos de 100 ms") para todo o domínio ou superdimensiona a infraestrutura de sistemas tolerantes ou subdimensiona a de sistemas sensíveis. A literatura empírica distingue classes de interação e dá ordens de grandeza para cada uma.

## Fundamentos e funcionamento

### O modelo precisão-deadline (Claypool e Claypool, 2006)

O artigo "Latency and player actions in online games" (Communications of the ACM, vol. 49, n. 11, 2006, DOI 10.1145/1167838.1167860 [F: claypool2006latency]) e o relatório técnico correspondente (WPI TR 06-13, 2006 [F: claypool2006tr]) propõem classificar ações do jogador por "the precision required to complete the action and the deadline by which the action must be completed": "Actions with higher precision and tight deadlines are sensitive to even modest latencies, while actions with lower precision and loose deadlines are" menos sensíveis [F: claypool2006tr, §1]. Os autores distinguem dois modelos de interação: *Avatar* (o jogador age por um único personagem, em primeira ou terceira pessoa) e *Omnipresent* (o jogador "has the ability to view and influence simultaneously different" partes do mundo) [F: claypool2006tr, §3].

A síntese dos autores (Tabela 1 do relatório) é:

| Modelo / perspectiva | Gêneros de exemplo | Sensibilidade | Limiar |
|---|---|---|---|
| Avatar, primeira pessoa | FPS, corrida | alta | 100 ms [F: claypool2006tr, Tabela 1] |
| Avatar, terceira pessoa | esportes, RPG | média | 500 ms [F: claypool2006tr, Tabela 1] |
| Omnipresent | RTS, simulação | baixa | 1000 ms [F: claypool2006tr, Tabela 1] |

Os autores alertam que "the exact threshold depends upon the game and to some extent the player" e que, dentro de uma classe, ações menos precisas ou com deadline mais folgado deslocam a curva para a direita [F: claypool2006tr, §6].

As evidências que sustentam a tabela, conforme resumidas pelos próprios autores:

- **Primeira pessoa, tiro**: em Unreal Tournament 2003, com arma de alta precisão em combates de dois jogadores, "a sharp drop (about 35%) in accuracy at 100 milliseconds of latency" [F: claypool2006tr, §5]; o estudo original é Beigbeder et al. (2004, NetGames, DOI 10.1145/1016540.1016556), cujos metadados foram verificados e cujo texto não foi lido nesta sessão [F: beigbeder2004unreal].
- **Primeira pessoa, corrida**: tempo de volta com "a significantly steeper increase above 50 milliseconds and again above 150 milliseconds" [F: claypool2006tr, §5], remetendo ao estudo de Pantel e Wolf abaixo.
- **Terceira pessoa, esporte**: em Madden NFL, "no significant drop-off in performance until after 500 milliseconds of latency" [F: claypool2006tr, §5].
- **Terceira pessoa, RPG**: em EverQuest 2, de 0 a 500 ms a perda é pequena, "adding only an additional 5 seconds to about 2 minutes of combat" [F: claypool2006tr, §5].
- **Omnipresent, RTS**: em Warcraft III, construir a árvore tecnológica leva cerca de 8 minutos sem latência, e "latency values of up to 3.5 seconds increase total build time by at most 14 seconds, which is less than 1% of the total time" [F: claypool2006tr, §5]; o estudo original é Sheldon et al. (2003, NetGames, DOI 10.1145/963900.963901), metadados verificados, texto não lido [F: sheldon2003warcraft]. Em Age of Mythology, a diferença de pontuação "from no induced latency to one second of induced latency is only equivalent to about one unit" [F: claypool2006tr, §5].

### Corrida com controle direto (Pantel e Wolf, 2002)

"On the impact of delay on real-time multiplayer games" (NOSSDAV 2002, DOI 10.1145/507670.507674 [F: pantel2002delay]) testou um simulador de corrida de carros de controle remoto, visto de cima, com 12 participantes; o atraso de apresentação "was increased in steps of 50 ms each up to a maximum of 500 ms", sem que os jogadores soubessem o valor, com cinco voltas por configuração e entrevista subjetiva; a série parava quando o participante declarava a situação intolerável [F: pantel2002delay, §4]. Resultados: para o piloto experiente, "Until a delay value of about 150 ms, only a small increase in the round times can be observed, followed by an almost exponential increase above 150 ms", e ele interrompeu a 250 ms; "Below 50 ms, no significant alterations of the lap time are measurable. Hence, we believe that even for competitions, a presentation delay up to 50 ms is uncritical" [F: pantel2002delay, §4]. Na média de todos, "Starting for delay values above 50ms, the achieved round times increase strongly" [F: pantel2002delay, §4]. Para iniciantes, "higher delay values up to 200 ms seem to be acceptable for unpracticed drivers", e os participantes relataram que é possível se acostumar até cerca de 200 ms "but the driving was stated to be definitely not realistic" [F: pantel2002delay, §4]. Os autores distinguem explicitamente o desempenho objetivo (tempo de volta) da impressão subjetiva, e consideram esta última a que importa [F: pantel2002delay, §4].

### Cloud gaming (ITU-T)

A G.1072 (01/2020, com Corrigendum 1 de 10/2020) é "an opinion model that estimates how well non-expert gamers will rate the overall quality of cloud gaming services", com "impairment factor approach" que modela o efeito de parâmetros de rede IP e de codificação de vídeo sobre a qualidade de vídeo e de entrada; destina-se a planejamento de rede, assumindo "that the network may experience packet loss and latency"; tem um modo padrão que assume jogo "highly sensitive to delay and frame loss" e um modo estendido com coeficientes ajustados quando o tipo de jogo é conhecido [F: itu2020g1072]. Os coeficientes e limiares numéricos do modelo estão no corpo da Recomendação, não lido nesta sessão (não verificado). [I] O ponto metodológico útil é que o modelo trata a sensibilidade à latência como parâmetro do tipo de jogo, em linha com Claypool.

### Jogos por turnos

Não foi localizada nesta sessão fonte primária com limiares empíricos para jogos por turnos. O que a literatura verificada oferece é o extremo "Omnipresent" de Claypool (RTS tolerando segundos para ações de construção) [F: claypool2006tr]. [I] Jogos por turnos têm deadline ainda mais folgado que RTS (a ação é discreta e não há adversário se movendo durante a decisão), o que sugere limiares de segundos; mas a percepção de "o sistema respondeu ao meu clique" continua sujeita à responsividade de interface, que é outra métrica. Fica como [H] até verificação de estudo específico. Ver `rtm.mp.turn-based`.

### Colaboração em tempo real

Ignat et al. (2015), "How Do User Groups Cope with Delay in Real-Time Collaborative Note Taking" (ECSCW 2015, DOI 10.1007/978-3-319-20499-4_12): metadados verificados; o resumo automatizado disponível indica que o atraso prejudica a forma como grupos lidam com conteúdo sobreposto e errôneo no documento, atribuído a menor consciência da atividade dos colegas [F: ignat2015delay, tldr]. O texto completo e os valores de atraso testados não puderam ser abertos (não verificado); nenhum limiar numérico é citado. [I] Em colaboração, o atraso afeta coordenação (conflitos, retrabalho) mais do que desempenho individual, o que é um tipo de degradação diferente do dos jogos. Ver `rtm.sync.crdt` e `rtm.sync.operational-transformation`.

## Requisitos e pressupostos

- Os limiares acima são de latência *adicionada* em laboratório, medida entre cliente e servidor; latência de aplicação (ver `rtm.perf.metrics`) inclui mais componentes.
- Os estudos de jogos usaram métricas de desempenho (acerto, tempo de volta, tempo de construção), e, em Pantel e Wolf, também impressão subjetiva; a transferência para "satisfação" é indireta.
- Amostras pequenas: 12 participantes em Pantel e Wolf [F: pantel2002delay, §4]; os demais n não foram verificados.

## Vantagens e limitações

- O modelo precisão-deadline é transferível para fora de jogos: qualquer interação pode ser posicionada nos dois eixos [I].
- Os limiares são de 2002 a 2006, com os jogos da época; técnicas de compensação posteriores (ver `rtm.pred.lag-compensation`) deslocam o ponto em que a latência vira degradação visível, sem mudar o fenômeno [I].
- Nenhuma fonte verificada cobre colaboração ou turnos com números.

## Alternativas e comparações

| Tipo de interação | Evidência | Ordem de grandeza (fonte) |
|---|---|---|
| Ação rápida, primeira pessoa | UT2003, corrida | ~100 ms [F: claypool2006tr]; 50 ms não crítico, >150 ms degrada fortemente para experientes [F: pantel2002delay] |
| Avatar em terceira pessoa | Madden, EQ2 | ~500 ms [F: claypool2006tr] |
| Estratégia (RTS) | Warcraft III, AoM | ~1000 ms; segundos para construção [F: claypool2006tr] |
| Turnos | nenhuma verificada | [H] segundos |
| Colaboração | Ignat et al. 2015 (texto não lido) | sem número verificado |

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`. Para reproduzir os estudos: adicionar latência controlada (ver `rtm.perf.network-emulation`), medir uma métrica de desempenho da tarefa e uma de opinião; variar em degraus (Pantel e Wolf usaram 50 ms até 500 ms [F: pantel2002delay]); reportar n e condições.

## Exemplo técnico independente de domínio

```text
# Posicionar uma interacao nos eixos de Claypool e escolher o orcamento
precision = {alta, media, baixa} ; deadline = {apertado, medio, folgado}
if precision == alta and deadline == apertado: budget ~ 100 ms   # claypool2006tr
elif deadline == folgado:                       budget ~ 1000 ms  # claypool2006tr
else:                                           budget ~ 500 ms   # claypool2006tr
# Validar: experimento com latencia em degraus, metrica de tarefa + opiniao, n reportado
```

## Relações com outros conceitos

Depende de `rtm.net.latency` e de `rtm.perf.metrics`. Complementa `rtm.pred.client-side-prediction` e `rtm.pred.lag-compensation` (técnicas que deslocam os limiares), `rtm.mp.turn-based`, `rtm.sync.crdt` e `rtm.sync.operational-transformation` (interações de deadline folgado). Relaciona-se a `rtm.perf.network-emulation` (como reproduzir). Avaliado por `rtm.perf.metrics`.

## Lacunas e questões abertas

- Beigbeder et al. (2004) e Sheldon et al. (2003): só metadados verificados; os números citados vêm do resumo de Claypool e Claypool.
- ITU-T G.1072: só o sumário foi lido; coeficientes e faixas de delay do modelo não verificados.
- Ignat et al. (2015): texto completo bloqueado; sem números.
- Nenhuma fonte verificada para jogos por turnos; a pergunta aberta do brief do domínio ("limiares por gênero de interação") continua parcialmente aberta para turnos e colaboração.
- Faltam estudos recentes (pós-2015) com técnicas de compensação modernas; não buscados nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| claypool2006latency | academico (metadados) | 2026-10-29 |
| claypool2006tr | academico | 2026-10-29 |
| pantel2002delay | academico | 2026-10-29 |
| sheldon2003warcraft | academico (metadados) | 2026-10-29 |
| beigbeder2004unreal | academico (metadados) | 2026-10-29 |
| itu2017g1032 | normativo | 2026-10-29 |
| itu2020g1072 | normativo | 2026-10-29 |
| ignat2015delay | academico (metadados e resumo) | 2026-10-29 |
