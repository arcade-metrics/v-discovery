---
id: rtm.sync.state-replication
titulo: Replicação de estado em simulações distribuídas
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [fiedler2014intro, fiedler2014lockstep, fiedler2014snapshot, fiedler2015statesync, fiedler2015compression, fiedler2018vr, fiedler2010networking, gambetta2014clientserver, sanglard2012quake3, frohnmayer2000tribes, madhav2015multiplayer]
relacoes:
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: depende-de, alvo: rtm.net.jitter }
  - { tipo: depende-de, alvo: rtm.net.packet-loss }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: complementa, alvo: rtm.pred.client-side-prediction }
  - { tipo: complementa, alvo: rtm.pred.entity-interpolation }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
  - { tipo: relacionado-a, alvo: rtm.sync.operational-transformation }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [state replication, réplica, autoridade, deterministic lockstep, snapshot interpolation, state synchronization, ghost]
---

# Replicação de estado em simulações distribuídas

## Definição e terminologia

Replicação de estado (*state replication*) é o problema de manter N cópias (réplicas) de um estado de simulação coerentes entre si quando essas cópias vivem em máquinas diferentes, ligadas por uma rede com latência, jitter e perda de pacotes. Uma das réplicas, ou um conjunto delas, detém a autoridade sobre partes do estado; as demais são visões aproximadas que precisam convergir para a autoridade. [I]

Nomes alternativos encontrados na literatura técnica: *networked physics* (quando o estado replicado é uma simulação física) [F: fiedler2014intro], *object replication* (capítulo 5 de Madhav e Glazer) [F: madhav2015multiplayer], *ghosting* (termo do modelo de rede do TRIBES: um *ghost* é a cópia de um objeto persistida e transmitida a um host remoto) [F: frohnmayer2000tribes]. Neste domínio usamos "replicação de estado" como nome do problema e "família de sincronização" para cada estratégia de solução. [I]

O que não é: replicação de estado não é o mesmo que replicação de banco de dados nem consenso distribuído. Aqui o estado muda dezenas de vezes por segundo, a perda de uma atualização é tolerável porque a próxima a substitui, e o critério de sucesso é perceptual (o usuário não deve notar a divergência), não transacional. [I]

## Problema que resolve

Uma simulação interativa com várias pessoas precisa que cada participante veja "o mesmo mundo" com atraso pequeno o bastante para a interação parecer imediata. Gambetta descreve o ponto de partida: o servidor é "the one and only authority" sobre o estado, o cliente é um "privileged spectator", e qualquer viagem de ida e volta pela rede introduz um atraso percebido entre a ação do jogador e seu efeito; o autor usa 50 ms por sentido como cenário próximo do melhor caso e afirma que atrasos de 100, 200 e até 500 ms não são incomuns [F: gambetta2014clientserver]. Sem uma estratégia de replicação, cada ação precisaria de uma ida e volta antes de ser exibida, ou todos os participantes precisariam trocar o estado inteiro a cada frame. [I]

As restrições simultâneas são: banda finita por participante, latência que não pode ser eliminada, perda de pacotes que não pode ser evitada e, em muitos casos, simulações não determinísticas entre máquinas. A replicação de estado é o conjunto de técnicas que escolhe o que enviar, com que frequência e como o receptor preenche as lacunas entre o que recebeu e o que exibe. [I]

## Fundamentos e funcionamento

### O que viaja pela rede: entradas ou estado

A escolha fundamental é entre transmitir as entradas (*inputs*) que dirigem a simulação ou o estado resultante dela. Fiedler apresenta a série "Networked Physics" como a mesma simulação (cubos físicos controlados por um jogador) replicada de três maneiras diferentes: *deterministic lockstep*, *snapshot interpolation* e *state synchronization* [F: fiedler2014intro].

- Em **deterministic lockstep** só as entradas viajam; cada lado avança o frame n apenas depois de receber a entrada n de todos; a banda não depende do número de objetos simulados, mas exige que a simulação seja determinística bit a bit dado o mesmo estado inicial, as mesmas entradas e o mesmo passo de tempo [F: fiedler2014lockstep]. O autor relata que o determinismo só valeu na mesma máquina, com o mesmo binário e sistema operacional, e que não há garantia entre compiladores, arquiteturas ou entre builds debug e release [F: fiedler2014lockstep]. Documento próprio: `rtm.arch.deterministic-lockstep`.
- Em **snapshot interpolation** o lado autoritativo captura o estado relevante inteiro (um *snapshot*) e o envia; o receptor não simula, guarda um buffer de snapshots e interpola entre dois snapshots passados [F: fiedler2014snapshot]. Documento: `rtm.sync.snapshot-interpolation`.
- Em **state synchronization** os dois lados rodam a simulação; viajam entradas e estado, o receptor extrapola a partir do último estado recebido e aceita correções; o autor a descreve como "approximate and lossy" [F: fiedler2015statesync]. Documento: `rtm.sync.state-synchronization`.

### Autoridade

Nas três famílias existe uma fonte de verdade por objeto. Em cliente-servidor a autoridade é o servidor [F: gambetta2014clientserver]. Fiedler, no experimento de física em VR, descartou lockstep (motor de física não determinístico) e cliente-servidor com predição (sem servidor dedicado, o custo de rollback não compensava) e adotou simulação distribuída com autoridade por objeto: cada jogador assume autoridade sobre os cubos com que interage e envia o estado deles aos outros, com todos os pacotes passando pelo host, que arbitra conflitos [F: fiedler2018vr]. O autor recomenda esse modelo apenas para experiências cooperativas, porque não oferece a segurança de um servidor autoritativo [F: fiedler2018vr].

### Histórico resumido

Fiedler descreve a evolução: Doom usava lockstep peer-to-peer, que funcionava em LAN e mal na internet; Quake (1996) adotou cliente-servidor com clientes como terminais que interpolam estados recebidos; QuakeWorld acrescentou predição do próprio movimento no cliente; jogos de estratégia como Age of Empires e StarCraft usam lockstep porque o estado (milhares de unidades) é grande demais para ser trocado [F: fiedler2010networking]. Sanglard, ao revisar o código do Quake 3, resume o princípio do modelo de snapshots: informação que não chega na primeira transmissão não vale reenvio porque já estará desatualizada, por isso o motor usa UDP e não TCP [F: sanglard2012quake3].

## Requisitos e pressupostos

- Existe uma autoridade definida por objeto, mesmo que ela mude ao longo do tempo. [I]
- A rede é modelada como não confiável e desordenada; as três famílias de Fiedler são construídas sobre UDP com sequência própria, e o autor afirma explicitamente que snapshots devem usar UDP e nunca TCP [F: fiedler2014snapshot]. Ver `rtm.proto.udp` e `rtm.net.ordering-and-reliability`.
- O estado é tolerante a perda: uma atualização perdida é substituída pela seguinte. Isso vale para estado "mais recente" (posição, orientação) e não vale para eventos que precisam acontecer uma vez (entrada ou saída de jogador, troca de nível), que o Quake 3 garante por outra camada [F: sanglard2012quake3]. O TRIBES formaliza a distinção em categorias de entrega: *nonguaranteed*, *guaranteed* (ordenado), *most recent state* e *guaranteed quickest* [F: frohnmayer2000tribes]. Ver `rtm.rel.delivery-semantics`.
- A taxa de simulação e a taxa de envio podem ser diferentes; a família escolhida determina como o receptor preenche o intervalo entre atualizações (interpolação, extrapolação ou espera). [I]

## Critérios de escolha

| Critério | Deterministic lockstep | Snapshot interpolation | State synchronization |
|---|---|---|---|
| O que viaja | entradas [F: fiedler2014lockstep] | estado completo visível [F: fiedler2014snapshot] | entradas e subconjunto priorizado do estado [F: fiedler2015statesync] |
| Simulação no receptor | idêntica, determinística [F: fiedler2014lockstep] | nenhuma; só reconstrução visual [F: fiedler2014snapshot] | local, aproximada, corrigida [F: fiedler2015statesync] |
| Determinismo exigido | bit a bit [F: fiedler2014lockstep] | não | não; quantização dos dois lados reduz divergência [F: fiedler2015statesync] |
| Banda vs número de objetos | independente [F: fiedler2014lockstep] | cresce com os objetos (900 cubos a 60 pps: ~11,6 Mbit/s sem compressão) [F: fiedler2014snapshot] | limitada por orçamento fixo (exemplo de 256 kbit/s) [F: fiedler2015statesync] |
| Atraso adicionado | playout delay buffer (exemplo de 100 ms) [F: fiedler2014lockstep] | interpolation delay (350 ms a 10 pps nos vídeos do autor) [F: fiedler2014snapshot] | jitter buffer de 4 a 5 frames a 60 Hz [F: fiedler2015statesync] |
| Número de jogadores | o autor recomenda para no máximo 2 a 4 jogadores [F: fiedler2014snapshot] | sem limite estrutural; custo é banda [I] | sem limite estrutural; custo é CPU e banda [I] |
| Entrada tardia (late join) | difícil: exige capturar estado determinístico no meio da partida [F: fiedler2010networking] | trivial: próximo snapshot basta [I] | requer snapshot inicial completo [I] |

Regra de bolso derivada das recomendações do autor: lockstep quando a simulação é determinística e há poucos jogadores; snapshot interpolation quando não há determinismo ou há mais jogadores e a banda comporta o estado; state synchronization quando o receptor precisa de atraso menor ou interação física local e aceita complexidade maior [F: fiedler2014snapshot] [I]. Em jogos de ação cliente-servidor, Fiedler aponta que predição no cliente com servidor autoritativo é a solução para ação em tempo real com latência alta [F: fiedler2010networking]; ver `rtm.pred.client-side-prediction`.

## Vantagens e limitações

Vantagem comum: as três famílias desacoplam a taxa de envio da taxa de exibição e toleram perda sem retransmissão. Limitação comum: todas introduzem um atraso deliberado (buffer) para absorver jitter; o tamanho desse buffer é o parâmetro que troca suavidade por latência, e Fiedler nota, para o lockstep, que buffer pequeno gera travamentos e buffer grande aumenta a latência [F: fiedler2014lockstep]. [I]

Limitação de escala: snapshot interpolation sem compressão é proibitivo com muitos objetos; a redução vem de quantização, codificação delta e filtragem de relevância, tratadas em `rtm.sync.delta-compression` e `rtm.sync.interest-management`. [I]

## Relação com estado que não é simulação

CRDT e OT (`rtm.sync.crdt`, `rtm.sync.operational-transformation`) resolvem um problema vizinho: réplicas que recebem edições concorrentes e precisam convergir para o mesmo valor sem autoridade central e sem descartar operações. A diferença essencial é a semântica de perda: na replicação de simulação uma atualização antiga é descartável porque a seguinte a substitui; em edição colaborativa nenhuma operação pode ser perdida, e a ordem relativa importa. [I] É plausível que um sistema real combine as duas famílias: estado contínuo (posições) por snapshot ou state synchronization e estado discreto compartilhado (documento, inventário) por CRDT; não encontramos fonte que avalie essa combinação. [H]

## Métricas e métodos de avaliação

Métricas usadas pelas fontes: banda por cliente em kbit/s ou Mbit/s, medida antes e depois de cada otimização [F: fiedler2014snapshot] [F: fiedler2015compression]; atraso total entre o evento na autoridade e sua exibição na réplica [F: fiedler2014snapshot]; artefatos visuais sob perda e jitter controlados (o autor testa com 5% de perda e ±2 frames de jitter a 60 fps) [F: fiedler2014snapshot]; memória por cliente no servidor (Quake 3: 32 snapshots por cliente, cerca de 8 MB para 4 jogadores segundo a medição de Sanglard) [F: sanglard2012quake3]. Ver `rtm.perf.metrics` e `rtm.perf.network-emulation`.

## Exemplo técnico independente de domínio

Laço genérico do lado da réplica, parametrizado pela família. O corpo de `fill_gap` é o que distingue as três estratégias.

```
loop a cada frame de render (dt):
    pacotes = receber_sem_bloquear()
    para p em pacotes:
        se p.seq mais recente que ultimo_seq:        # sequência própria sobre UDP
            buffer.inserir(p)                         # ordenado por seq / tempo
            ultimo_seq = p.seq
    estado_exibido = fill_gap(buffer, agora - atraso_alvo)
    renderizar(estado_exibido)

fill_gap (lockstep):         avança a simulação determinística só se input[n] presente; senão espera
fill_gap (snapshot interp.): acha s_a, s_b com s_a.t <= t_alvo < s_b.t; interpola(s_a, s_b, t_alvo)
fill_gap (state sync):       aplica último estado recebido como condição inicial; simula localmente até agora
```

## Relações com outros conceitos

Este é o documento-raiz da família; `rtm.sync.snapshot-interpolation`, `rtm.sync.state-synchronization`, `rtm.sync.dead-reckoning`, `rtm.sync.delta-compression` e `rtm.sync.interest-management` declaram `parte-de` apontando para ele. Depende das propriedades de rede em `rtm.net.latency`, `rtm.net.jitter`, `rtm.net.packet-loss` e `rtm.net.bandwidth`. O lockstep é tratado como arquitetura em `rtm.arch.deterministic-lockstep`. Predição e reconciliação (`rtm.pred.*`) são o complemento do lado do jogador local. CRDT e OT são a família vizinha para estado não simulado.

## Lacunas e questões abertas

- A página "Introduction to Networked Physics" só nomeia as três famílias; os critérios de escolha acima foram reunidos a partir dos artigos seguintes da série e são síntese nossa. [I]
- Não verificamos o conteúdo do capítulo 5 de Madhav e Glazer além do sumário público; a correspondência entre "object replication" e as famílias de Fiedler é inferência. [I]
- Falta fonte acadêmica que compare as três famílias com métricas controladas; o material de Fiedler é opinião técnica de referência com experimentos próprios, não revisado por pares.
- Combinação de replicação de simulação com CRDT para o mesmo sistema: sem fonte. [H]

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fiedler2014intro | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2015statesync | tecnico | 2026-10-29 |
| fiedler2015compression | tecnico | 2026-10-29 |
| fiedler2018vr | tecnico | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
| gambetta2014clientserver | tecnico | 2026-10-29 |
| sanglard2012quake3 | tecnico | 2026-10-29 |
| frohnmayer2000tribes | tecnico | 2026-10-29 |
| madhav2015multiplayer | academico | 2026-10-29 (apenas sumário) |
