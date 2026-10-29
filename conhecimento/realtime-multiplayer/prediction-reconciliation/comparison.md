---
id: rtm.pred.comparison
titulo: Comparação das técnicas de predição, reconciliação, interpolação e lag compensation
tipo: comparacao
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gambetta2014architecture, gambetta2014prediction, gambetta2014interpolation, gambetta2014lagcomp, gambetta2014demo, bernier2001latency, valve2026source, fiedler2010networking, fiedler2014snapshot, liu2022survey, lee2015evaluation, lee2017corner]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.pred.server-reconciliation }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
  - { tipo: relacionado-a, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.sync.state-synchronization }
  - { tipo: relacionado-a, alvo: rtm.sync.dead-reckoning }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
  - { tipo: relacionado-a, alvo: rtm.sync.operational-transformation }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
  - { tipo: relacionado-a, alvo: rtm.mp.turn-based }
  - { tipo: relacionado-a, alvo: rtm.perf.qoe-thresholds }
termos: [latency compensation, prediction family, time manipulation, determinism requirement]
---

# Comparação das técnicas de predição, reconciliação, interpolação e lag compensation

## Definição e terminologia

Este documento compara as quatro técnicas da pasta `prediction-reconciliation/` entre si e com as técnicas vizinhas de `synchronization/` e `architectures/`. Usa como referência de classificação a taxonomia de Liu, Xu e Claypool (2022), que organiza mais de 80 trabalhos em "eleven base technique types, organized into four main groups": Feedback, Prediction, Time Manipulation e World Adjustment [F: liu2022survey, abstract e §4]. Nessa taxonomia:

- client-side prediction é *Prediction > Self-Prediction* [F: liu2022survey, §4.2.1];
- entity interpolation e dead reckoning são *Prediction > Other-prediction > Interpolation* e *> Extrapolation* [F: liu2022survey, §4.2.3 e §4.2.4];
- lag compensation é *Time Manipulation > Time Delay > Time Warp* [F: liu2022survey, §4.3.1.1];
- server reconciliation não é um nó da taxonomia; é o mecanismo de correção inerente à self-prediction (a taxonomia descreve que o estado do cliente "is inevitably fixed to align with the server game state") [F: liu2022survey, §4.2; I].

O termo guarda-chuva nas fontes é *latency compensation* (ou *lag compensation* em sentido amplo), o que colide com o uso estrito de "lag compensation" para o time warp do servidor; a taxonomia registra essa confusão [F: liu2022survey, §4.3.1.1]. Nesta base, "lag compensation" sem qualificador é sempre o sentido estrito (`rtm.pred.lag-compensation`).

## Problema que resolve

Cada técnica ataca uma manifestação distinta da latência em um servidor autoritativo [I, sintetizando gambetta2014architecture a gambetta2014lagcomp]:

| Manifestação | Quem sofre | Técnica |
|---|---|---|
| Atraso entre entrada e resposta própria | Jogador local | Client-side prediction |
| Recuo e avanço ao chegar estado antigo | Jogador local | Server reconciliation |
| Teletransporte dos outros a cada atualização | Observador | Entity interpolation (ou dead reckoning) |
| Tiro certo na tela que erra no servidor | Atirador | Lag compensation |

Gambetta apresenta as quatro como um conjunto que, combinado, deixa a experiência "quase indistinguível de um jogo local" [F: gambetta2014architecture]; a demo mostra o efeito de ligar cada uma separadamente [F: gambetta2014demo].

## Fundamentos e funcionamento

### Tabela comparativa

| Critério | Client-side prediction | Server reconciliation | Entity interpolation | Lag compensation |
|---|---|---|---|---|
| Onde roda | Cliente | Cliente | Cliente | Servidor |
| Sobre quais entidades | A própria [F: valve2026source] | A própria | As remotas [F: gambetta2014interpolation] | As remotas, no instante da ação [F: bernier2001latency] |
| Exibe no tempo | Presente previsto | Presente corrigido | Passado (~100 ms nos exemplos) [F: gambetta2014interpolation] | Passado reconstruído no servidor [F: gambetta2014lagcomp] |
| CPU | Simulação local extra | Re-simulação de N comandos por atualização (N ≈ fps × RTT; 5 com 50 fps e 100 ms) [F: bernier2001latency] | Busca e lerp por entidade por frame | Rebobinar e restaurar poses por ação; raycast no passado |
| Memória | Estado local | Buffer de comandos pendentes [F: gambetta2014prediction] | Histórico de amostras por entidade [F: bernier2001latency] | Histórico de poses por jogador (1 s na Valve) [F: valve2026source] |
| Banda | Comandos com seq e duração [F: bernier2001latency] | Seq confirmada em cada estado [F: gambetta2014prediction] | Nenhuma extra; Hermite exige enviar velocidade [F: fiedler2014snapshot] | Timestamp e interpolação do cliente no comando [F: bernier2001latency] |
| Complexidade | Código compartilhado cliente/servidor [F: bernier2001latency] | Idempotência de efeitos; estado só-cliente [F: bernier2001latency] | Relógio e histórico; tratamento de perda [F: valve2026source] | Estimativa de latência; limites; estado extra (agachado, vivo) [F: bernier2001latency] |
| Exige determinismo | Sim, "suficiente" (divergências corrigidas) [F: gambetta2014prediction] | Idem | Não | Não (reproduz poses gravadas, não re-simula) |
| Custo de justiça | Nenhum | Nenhum | Quem se move vê antes (*view interpolation delay*) [F: valve2026source] | "Shot around the corner" [F: gambetta2014lagcomp; F: lee2017corner] |

### Como combinam

- **Prediction sem reconciliation** produz o serrilhado de Gambetta sempre que há entradas em trânsito; na prática as duas são uma só técnica em duas metades [F: gambetta2014prediction].
- **Prediction/reconciliation sem interpolation** melhora só o jogador local; os outros continuam irregulares [F: gambetta2014demo].
- **Interpolation sem lag compensation** cria mira defasada ("you're shooting where your target was 100 ms ago") [F: gambetta2014interpolation]; lag compensation existe para corrigir exatamente essa defasagem, e por isso a fórmula da Valve inclui a interpolação do cliente [F: valve2026source].
- **Lag compensation sem interpolation** é possível, mas a Valve alerta que desligar a interpolação no cliente produz resultados indesejados, porque o servidor assume o atraso de interpolação no cálculo [F: valve2026source].
- **Interpolation vs. dead reckoning** são alternativas para a mesma função; Gambetta indica interpolação para movimento brusco e dead reckoning para entidades previsíveis [F: gambetta2014interpolation]; a Valve usa extrapolação apenas como fallback para perdas consecutivas, limitada a 0,25 s [F: valve2026source]; Fiedler limita extrapolação útil a 50 a 250 ms [F: fiedler2014snapshot]. Ver `rtm.sync.dead-reckoning`.

### Relação com as arquiteturas

| Arquitetura | Prediction/reconciliation | Interpolation | Lag compensation |
|---|---|---|---|
| Servidor autoritativo (`rtm.arch.authoritative-server`) | Aplicável; é o caso descrito por todas as fontes | Aplicável | Aplicável |
| Lockstep determinístico (`rtm.arch.deterministic-lockstep`) | Não se aplica na forma descrita: todos simulam as mesmas entradas e esperam o jogador mais lento [F: fiedler2010networking]; o rollback de jogos de luta é um parente sob *time warp* [F: liu2022survey, §4.3.1.1] | Não necessária (todos têm o estado completo) | Não se aplica |
| Relay (`rtm.arch.relay-server`) / P2P (`rtm.arch.peer-to-peer`) | Possível se um par for autoritativo; sem autoridade não há contra o que reconciliar [I] | Aplicável a qualquer fluxo de atualizações [I] | Só com um nó autoritativo [I] |
| Orientado a eventos (`rtm.arch.event-driven`) | Em geral desnecessária; ver seção seguinte [I] | Raramente | Não |

Ver `rtm.arch.comparison` e `rtm.sync.state-synchronization`.

## Requisitos e pressupostos

Resumo do que cada técnica exige, consolidando os documentos individuais:

- Todas: servidor (ou nó) autoritativo e entradas com número de sequência ou timestamp [F: gambetta2014prediction; F: gambetta2014lagcomp].
- Prediction e reconciliation: código de simulação executável no cliente e determinismo suficiente [F: gambetta2014prediction; F: bernier2001latency].
- Interpolation: taxa de atualização regular e estimativa do relógio do servidor [F: bernier2001latency].
- Lag compensation: estimativa de latência por cliente, histórico com profundidade igual ao rewind, ação instantânea [F: bernier2001latency; F: valve2026source].

## Aplicabilidade a jogos por turnos e colaboração

As fontes são explícitas sobre o escopo: Gambetta afirma que o modelo de dumb client (sem nenhuma das técnicas) funciona bem em jogos por turnos, como estratégia e pôquer, e em LAN; as técnicas existem para jogos rápidos pela internet [F: gambetta2014architecture]. Bernier enquadra lag compensation como ferramenta para jogos de ação e como decisão de design [F: bernier2001latency].

Interpretação por tipo de interação [I]:

| Tipo de interação | Prediction/reconciliation | Interpolation | Lag compensation | O que de fato importa |
|---|---|---|---|---|
| Ação em tempo real (FPS, corrida) | Necessária | Necessária | Necessária em hitscan | As quatro, combinadas |
| Turnos (`rtm.mp.turn-based`) | Desnecessária; feedback local otimista opcional (mostrar a jogada antes da confirmação) | Desnecessária | Desnecessária | Ordem, confirmação, reconexão (`rtm.rel.reconnection`) |
| Colaboração em documento (`rtm.sync.crdt`, `rtm.sync.operational-transformation`) | A ideia de "aplicar localmente e conciliar depois" existe, mas é resolvida por CRDT/OT, não por re-simulação | Desnecessária (não há movimento contínuo) | Desnecessária | Convergência e intenção do usuário |
| Presença e cursores (`rtm.mp.presence`) | Desnecessária | Útil para suavizar cursores remotos, com o mesmo raciocínio de exibir no passado | Desnecessária | Taxa de atualização e custo de banda |
| Simulação cooperativa lenta (navegação, estratégia em tempo real) | Opcional | Dead reckoning pode bastar, por previsibilidade [F: gambetta2014interpolation] | Rara | Consistência; lockstep é alternativa [F: fiedler2010networking] |

Conclusão: para turnos e colaboração, a maioria das técnicas desta pasta não é necessária; o que se transfere é o princípio de aplicar a ação local imediatamente e aceitar a autoridade do servidor ao confirmar, que Gambetta exemplifica com combate por turnos (mostrar sangue e número de dano de imediato, alterar a vida só com confirmação) [F: gambetta2014prediction; I].

## Métricas e métodos de avaliação

- Lee e Chang (2015): lag compensation e tick rate maior aumentam significativamente o desempenho em CS:GO; interpolação inconclusiva; V-Sync sem efeito [F: lee2015evaluation].
- Lee e Chang (2017): limite de rewind de 250 ms razoável para 4 m/s [F: lee2017corner].
- O survey de Liu, Xu e Claypool tabula faixas de latência testadas por estudo (por exemplo, 0 a 150 ms para o estudo com CS:GO de 2015, e até 3000 ms em estudos de extrapolação em jogos arcade), útil como mapa para `rtm.perf.qoe-thresholds` [F: liu2022survey, tabela de estudos].
- Instrumentação de fornecedor: `net_graph`, `cl_showerror`, `sv_showimpacts`, `net_fakelag` no Source [F: valve2026source].

## Exemplo técnico independente de domínio

Composição das quatro técnicas em um tick, em prosa estruturada:

```
Cliente, frame:
  1. ler entrada -> cmd{seq, dt, entrada, t_cliente, interp}
  2. enviar cmd; pendentes.adicionar(cmd)
  3. estado_proprio <- simular(estado_proprio, cmd)          # prediction
  4. para cada remota: exibir(lerp(historico, agora - interp)) # interpolation
  5. renderizar

Cliente, ao receber estado {estado, ultimo_seq}:
  6. estado_proprio <- estado; reaplicar pendentes > ultimo_seq # reconciliation
  7. historico[remotas].adicionar(estado)

Servidor, tick:
  8. para cada cmd recebido:
       se cmd tem ação instantânea:
           rebobinar remotas para t_alvo(cmd); resolver; restaurar  # lag comp.
       estado[c] <- simular(estado[c], cmd); ultimo_seq[c] <- cmd.seq
  9. gravar poses no histórico; enviar {estado, ultimo_seq[c]} a cada c
```

## Relações com outros conceitos

Depende de `rtm.arch.authoritative-server`. Relaciona-se com cada técnica desta pasta e com `rtm.sync.snapshot-interpolation`, `rtm.sync.state-synchronization` e `rtm.sync.dead-reckoning` (técnicas de sincronização que fornecem o fluxo de estado), com `rtm.sync.crdt` e `rtm.sync.operational-transformation` (o equivalente de "aplicar local e conciliar" em colaboração), com `rtm.arch.deterministic-lockstep` e `rtm.arch.comparison` (arquiteturas em que estas técnicas não se aplicam), com `rtm.mp.turn-based` e com `rtm.perf.qoe-thresholds`.

## Lacunas e questões abertas

- Os números de custo (CPU, memória, banda) nas fontes são exemplos ilustrativos (50 fps, 100 ms, 20 snapshots/s, 1 s de histórico), não medições; faltam medições publicadas comparando as técnicas sob a mesma carga [H].
- Não localizamos fonte que trate explicitamente da aplicação (ou não) destas técnicas a colaboração e presença; a tabela de aplicabilidade é interpretação a partir do escopo declarado por Gambetta e Bernier.
- As páginas da Valve foram verificadas em cópia integral de terceiros (originais com HTTP 403).
- O texto completo do survey foi lido em extração de PDF; figuras (3, 6 a 13) não foram inspecionadas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gambetta2014architecture | tecnico | 2026-10-29 |
| gambetta2014prediction | tecnico | 2026-10-29 |
| gambetta2014interpolation | tecnico | 2026-10-29 |
| gambetta2014lagcomp | tecnico | 2026-10-29 |
| gambetta2014demo | tecnico | 2026-10-29 |
| bernier2001latency | tecnico (artigo GDC 2001; original 403, verificado em cópia integral) | 2026-10-29 |
| valve2026source | fornecedor (original 403, verificado em cópia integral) | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| liu2022survey | academico | 2026-10-29 |
| lee2015evaluation | academico (abstract e metadados verificados) | 2026-10-29 |
| lee2017corner | academico (abstract e metadados verificados) | 2026-10-29 |
