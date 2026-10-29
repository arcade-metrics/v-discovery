---
id: rtm.pred.entity-interpolation
titulo: Entity interpolation
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gambetta2014interpolation, gambetta2014demo, bernier2001latency, valve2026source, fiedler2014snapshot, liu2022survey, lee2015evaluation]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: depende-de, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: depende-de, alvo: rtm.net.jitter }
  - { tipo: alternativa-a, alvo: rtm.sync.dead-reckoning }
  - { tipo: complementa, alvo: rtm.pred.client-side-prediction }
  - { tipo: complementa, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.net.packet-loss }
  - { tipo: relacionado-a, alvo: rtm.pred.comparison }
termos: [entity interpolation, interpolation delay, lerp, other-prediction, extrapolation, position history, view interpolation delay]
---

# Entity interpolation

## Definição e terminologia

Entity interpolation é a técnica pela qual o cliente exibe as entidades que não controla (outros jogadores, objetos do servidor) com um atraso deliberado, interpolando entre duas atualizações já recebidas do servidor em vez de exibir cada atualização assim que chega [F: gambetta2014interpolation]. Gambetta resume: "The key to the solution is to show the other players in the past relative to the user's player" [F: gambetta2014interpolation].

Nomes e termos relacionados nas fontes:

- **Interpolation / lerp / view interpolation**: nomes usados pela documentação da Valve; o atraso é o "lerp" (`cl_interp`) [F: valve2026source].
- **Interpolation delay / buffer**: termo de Fiedler para o tempo que snapshots ficam guardados antes de serem exibidos [F: fiedler2014snapshot].
- **Other-prediction > Interpolation**: posição na taxonomia de Liu, Xu e Claypool, definida como "predicts past states for objects controlled by other players based on the current state and previously known states" [F: liu2022survey, §4.2.3].
- **Snapshot interpolation** (`rtm.sync.snapshot-interpolation`): o mesmo mecanismo visto do lado do protocolo de sincronização (o que o servidor envia e com que taxa). Este documento trata da decisão de exibir no passado e de suas consequências para predição e lag compensation [I].

O que não é: não é extrapolação (dead reckoning), que estima o futuro; Gambetta sublinha que a interpolação "doesn't predict future positions at all – it uses only real entity data provided by the server" [F: gambetta2014interpolation].

## Problema que resolve

O servidor autoritativo não processa cada entrada ao chegar; ele enfileira entradas e atualiza o mundo em passos fixos, no exemplo de Gambetta 10 vezes por segundo (time step de 100 ms), enviando o estado a cada passo [F: gambetta2014interpolation]. Se o cliente movesse as outras entidades só quando o pacote chega, "you'd get players who teleport short distances every 100 ms, making the game unplayable" [F: gambetta2014interpolation]. A Valve descreve o mesmo com seus números: cerca de 20 snapshots por segundo, um a cada 50 ms; sem interpolação o movimento ficaria travado [F: valve2026source].

Client-side prediction não resolve isso, porque não há como prever a entrada dos outros jogadores [F: valve2026source]; a demo de Gambetta mostra que, com predição e reconciliação ativas, os outros jogadores continuam irregulares até que a interpolação seja ligada [F: gambetta2014demo].

## Fundamentos e funcionamento

Com atualizações recebidas em t = 900 e t = 1000, o cliente exibe, entre t = 1000 e t = 1100, o movimento que ocorreu entre 900 e 1000; mostra movimento real, apenas com cerca de 100 ms de atraso [F: gambetta2014interpolation]. Cada jogador vê o mundo de forma ligeiramente diferente: o próprio personagem no presente e os outros no passado [F: gambetta2014interpolation].

### Escolha do atraso de interpolação

- Gambetta usa um atraso igual ao intervalo de atualização (100 ms para 10 Hz) [F: gambetta2014interpolation].
- A Valve usa por padrão lerp de 100 ms (`cl_interp 0.1`) com 20 snapshots/s, de modo que sempre há dois snapshots válidos para interpolar mesmo se um for perdido [F: valve2026source]. A documentação dá a fórmula "interpolation period = max( cl_interp, cl_interp_ratio / cl_updaterate )" e recomenda zerar `cl_interp` e aumentar `cl_updaterate` (até o tickrate) para reduzir o lerp [F: valve2026source].
- Bernier (2001) descreve o Half-Life: 20 atualizações/s por padrão, interpolação de 100 ms, e a opção de subir para 200 ms para tolerar uma atualização perdida ao custo de mais latência [F: bernier2001latency].
- Fiedler, para física em rede, usa a regra prática de que o buffer deve cobrir a perda de dois pacotes seguidos; com 2 a 5% de perda, "the amount of delay that works best at 2-5% packet loss is 3X the packet send rate", o que a 10 pps dá 300 ms; somando margem para jitter de 1 a 2 frames a 60 fps, o autor usou 350 ms [F: fiedler2014snapshot].

Interpretação: o atraso é uma função da taxa de envio, da perda esperada e do jitter, não uma constante; "100 ms" é um valor histórico ligado a 10 a 20 atualizações por segundo [I]. Ver `rtm.net.jitter` e `rtm.net.packet-loss`.

### Histórico de posições e intervalo irregular

Bernier descreve que o cliente guarda a sequência de (timestamp, origem, ângulos) e, a cada frame, procura o par de atualizações que envolve o tempo-alvo para interpolar entre elas [F: bernier2001latency]. O intervalo entre pacotes não é fixo: com 20 atualizações/s o mínimo é 50 ms, mas pode chegar a 61 ms ou mais sob controle de banda [F: bernier2001latency]. Teletransportes devem ser detectados (flag ou distância excessiva) para não "deslizar" o objeto [F: bernier2001latency].

### Quando faltam atualizações

A Valve descreve que, com perdas consecutivas, o cliente passa a extrapolação linear (`cl_extrapolate 1`) limitada a 0,25 s (`cl_extrapolate_amount`), porque depois disso o erro fica grande demais [F: valve2026source]. Fiedler reporta que extrapolação só funciona bem em movimento quase linear e por curtos períodos, de 50 a 250 ms [F: fiedler2014snapshot].

### Qualidade da interpolação

Gambetta nota que, se interpolação linear não bastar, o servidor pode enviar dados mais detalhados (segmentos retos ou posições amostradas a cada 10 ms) [F: gambetta2014interpolation]. Bernier aponta o artefato da "bola quicando" achatada, porque a amostragem perde os extremos [F: bernier2001latency]. Fiedler compara linear e Hermite: a 10 pps, a linear produz tremor de posição e pulsação em objetos anexados; a Hermite usa a velocidade de cada amostra e elimina os artefatos ao custo de enviar velocidade [F: fiedler2014snapshot].

## Requisitos e pressupostos

- Atualizações com timestamp ou número de tick, para posicionar cada amostra no tempo [F: bernier2001latency].
- Taxa de atualização razoavelmente regular; Bernier aponta a dependência de intervalo fixo como limitação da interpolação simples [F: bernier2001latency].
- Movimento suave o bastante para que interpolar entre duas amostras seja aceitável [F: gambetta2014interpolation].
- Tolerância do jogo ao atraso visual: aceitável em jogos onde a resposta à própria entrada (coberta pela predição) importa mais que a posição exata dos outros [I].

## Vantagens e limitações

Vantagens:

- Movimento contínuo com dados reais, sem correções bruscas [F: gambetta2014interpolation].
- Tolera perda de um snapshot sem artefato, quando o atraso cobre dois intervalos [F: valve2026source].
- Na demo de Gambetta, a irregularidade de velocidade quase desaparece com cerca de 10 atualizações por segundo [F: gambetta2014demo].

Limitações:

- O jogador mira onde o alvo estava 100 ms atrás: "you're shooting where your target was 100 ms ago!" [F: gambetta2014interpolation]. A Valve descreve que quem se move ganha uma vantagem pequena, pois vê o alvo um instante antes (*view interpolation delay*) [F: valve2026source]. Isso motiva `rtm.pred.lag-compensation`.
- Cada cliente vê uma versão levemente diferente do mundo [F: gambetta2014interpolation].
- Atraso adicional soma-se à latência de rede na percepção dos outros jogadores [I].

## Alternativas e comparações

| Técnica | Base | Exibe | Correções | Adequação (segundo as fontes) |
|---|---|---|---|---|
| Entity interpolation | Amostras reais passadas | Passado (~1 a 3 intervalos) | Nenhuma por predição | Movimento brusco e imprevisível (jogadores em shooters) [F: gambetta2014interpolation] |
| Dead reckoning / extrapolação | Última posição, velocidade, aceleração | Presente estimado | Saltos quando erra | Entidades previsíveis (carros, navios) [F: gambetta2014interpolation]; QuakeWorld limitava a 100 ms [F: bernier2001latency] |
| Exibir ao chegar | Último pacote | Presente amostrado | Nenhuma | Teletransporte a cada intervalo [F: gambetta2014interpolation] |

Ver `rtm.sync.dead-reckoning` para a extrapolação e `rtm.sync.snapshot-interpolation` para o lado do protocolo.

## Métricas e métodos de avaliação

- **Atraso efetivo de exibição** (lerp final), que a Valve expõe via `net_graph` [F: valve2026source].
- **Perda e jitter** da rede, que ditam o atraso mínimo seguro [F: fiedler2014snapshot].
- **Artefatos visuais**: tremor de posição, pulsação, achatamento de trajetórias [F: fiedler2014snapshot; F: bernier2001latency].
- **Efeito no desempenho do jogador**: Lee e Chang (2015) avaliaram interpolação, lag compensation, tick rate e V-Sync em Counter-Strike: Global Offensive; os resultados sobre a interpolação foram inconclusivos, enquanto lag compensation e tick rate maior aumentaram o desempenho [F: lee2015evaluation]. Ver `rtm.perf.qoe-thresholds`.

## Exemplo técnico independente de domínio

```
# Cliente, para cada entidade remota e
historico[e] <- lista de (t_servidor, estado)   # ordenada por t

ao receber snapshot {t_s, estados}:
    para cada (e, estado) em estados: historico[e].adicionar((t_s, estado))

a cada frame, com relogio_servidor_estimado = agora:
    t_render <- agora - atraso_interp            # ex.: 100 ms
    para cada e:
        (t0, s0), (t1, s1) <- par em historico[e] com t0 <= t_render <= t1
        if par existe:
            alpha <- (t_render - t0) / (t1 - t0)
            exibir(e, lerp(s0, s1, alpha))
        else if t_render > ultimo t1 e (t_render - t1) < limite_extrap:
            exibir(e, extrapolar(s1, t_render - t1))
        else:
            exibir(e, s1)                        # congela
        descartar amostras com t < t_render - margem
```

Linha do tempo (atualizações a cada 100 ms, atraso de 100 ms):

```
recebido:  S(900)      S(1000)      S(1100)
exibido:   ------- 900->1000 ------ 1000->1100
relógio:   1000        1100         1200
```

## Relações com outros conceitos

Depende de `rtm.sync.snapshot-interpolation` (o fluxo de snapshots que alimenta o histórico), de `rtm.arch.authoritative-server` e de `rtm.net.jitter` (que dimensiona o atraso). É alternativa a `rtm.sync.dead-reckoning` para o mesmo problema (exibir entidades remotas). Complementa `rtm.pred.client-side-prediction` (que cobre a entidade própria) e `rtm.pred.lag-compensation` (que corrige a mira defasada; a lag compensation da Valve leva em conta o lerp do cliente no cálculo). Relaciona-se com `rtm.net.packet-loss`. Síntese em `rtm.pred.comparison`.

## Lacunas e questões abertas

- Página da Valve inacessível diretamente (HTTP 403 em 2026-10-29); verificada em cópia integral de terceiros. Valor padrão de `cl_interp_ratio` não consta no texto verificado.
- A página "Interpolation" da wiki da Valve, que segundo resultado de busca chama o padrão de 100 ms de valor "da era do dial-up", não foi aberta; não verificado.
- Não há, nas fontes verificadas, estudo que relacione atraso de interpolação a QoE fora de FPS (jogos cooperativos, simulações lentas) [H].
- Interpolação de estados não espaciais (animação, flags discretas) não é tratada pelas fontes; na prática exige regras próprias [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gambetta2014interpolation | tecnico | 2026-10-29 |
| gambetta2014demo | tecnico | 2026-10-29 |
| bernier2001latency | tecnico (artigo GDC 2001; original 403, verificado em cópia integral) | 2026-10-29 |
| valve2026source | fornecedor (original 403, verificado em cópia integral) | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| liu2022survey | academico | 2026-10-29 |
| lee2015evaluation | academico (abstract e metadados verificados) | 2026-10-29 |
