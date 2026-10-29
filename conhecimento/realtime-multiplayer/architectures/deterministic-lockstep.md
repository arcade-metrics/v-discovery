---
id: rtm.arch.deterministic-lockstep
titulo: Lockstep determinístico (deterministic lockstep)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [fiedler2014lockstep, fiedler2010floatingpoint, fiedler2010networking, fiedler2014networkedphysics, fiedler2015statesync, bettner2001archers, ggpo2019readme, ggpo2019devguide, orland2011cannon]
relacoes:
  - { tipo: alternativa-a, alvo: rtm.arch.authoritative-server }
  - { tipo: alternativa-a, alvo: rtm.arch.relay-server }
  - { tipo: alternativa-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: alternativa-a, alvo: rtm.arch.event-driven }
  - { tipo: alternativa-a, alvo: rtm.sync.state-synchronization }
  - { tipo: alternativa-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: depende-de, alvo: rtm.net.ordering-and-reliability }
  - { tipo: complementa, alvo: rtm.arch.peer-to-peer }
  - { tipo: complementa, alvo: rtm.arch.relay-server }
  - { tipo: complementa, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.proto.tcp }
  - { tipo: relacionado-a, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.mp.turn-based }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
termos: [deterministic lockstep, determinism, input delay, playout delay buffer, communication turn, desync, out of sync, checksum, rollback netcode, frame delay]
---

# Lockstep determinístico (deterministic lockstep)

## Definição e terminologia

Forma de sincronizar uma simulação entre computadores enviando apenas as entradas que a controlam, não o estado. Fiedler a define assim e deriva a consequência: "bandwidth is proportional to the size of the input, not the number of objects in the simulation" [F: fiedler2014lockstep]. Bettner descreve a mesma ideia em Age of Empires como *simultaneous simulations*: a meta era "run the exact same simulation on each machine" [F: bettner2001archers].

Nomes alternativos: *simultaneous simulation* [F: bettner2001archers], *peer-to-peer lockstep* [F: fiedler2010networking], *input-based synchronization* [I]. **Rollback netcode** é uma extensão: em vez de esperar as entradas remotas, o cliente as prevê, executa especulativamente e, se errar, volta e reexecuta [F: ggpo2019readme].

O que não é: não é *state synchronization*, em que "we don't just send input, we send both input and state" e a sincronia não depende de determinismo perfeito [F: fiedler2015statesync]; não exige servidor autoritativo, embora possa usar um relay ou um servidor como transporte [I].

## Problema que resolve

Banda. Bettner relata que transmitir posição, status, ação, direção e dano de cada unidade limitaria o jogo a cerca de 250 unidades em movimento, incompatível com a meta de 8 jogadores e a plataforma-alvo "16MB Pentium 90 with a 28.8 modem" [F: bettner2001archers]. Fiedler reforça: enviar estado custaria banda proporcional ao número de objetos, enquanto a entrada por frame é uma struct de seis booleanos [F: fiedler2014lockstep]. Fiedler observa que o modelo ainda é usado em RTS porque o estado é grande demais para ser transmitido [F: fiedler2010networking].

## Fundamentos e funcionamento

Todos os participantes começam do mesmo estado inicial e aplicam, no mesmo passo de simulação, o mesmo conjunto de entradas de todos [F: fiedler2010networking]. Fluxo [I, a partir de fiedler2014lockstep e bettner2001archers]:

```
par A: entrada(frame n) ──▶ todos      par B: entrada(frame n) ──▶ todos
cada par: espera ter entradas de TODOS para o frame n
          estado(n+1) = simular(estado(n), entradas(n))   # idêntico em todos
          checksum(estado) trocado periodicamente         # detecção de desync
```

### Input delay e turnos de comunicação

Para não travar esperando a rede, a entrada é agendada para execução no futuro. Em Age of Empires os turnos de comunicação duravam tipicamente 200 ms e "commands issued during turn 1000 would be scheduled for execution during turn 1002"; um mecanismo de *speed control* ajustava a duração do turno a partir da taxa de quadros e do maior ping reportado pelos clientes [F: bettner2001archers]. Fiedler usa um *playout delay buffer* com atraso fixo de 100 ms: entradas são indexadas por frame e a simulação só avança quando tem a entrada do frame n; se não chegou, espera, o que causa travamentos; ele limita a 4 frames simulados por frame de renderização para evitar a "spiral of death" [F: fiedler2014lockstep]. Aumentar o buffer reduz travamentos mas adiciona latência [F: fiedler2014lockstep].

Sobre percepção: Bettner relata que, para RTS, até 250 ms não era notado, entre 250 e 500 ms era jogável e acima de 500 ms era perceptível; latência constante era preferível à variável (500 ms fixos eram jogáveis, oscilações eram sentidas como "jerky") [F: bettner2001archers]. O guia do GGPO afirma que em jogos de luta um *frame delay* acima de 1 frame já é perceptível para jogadores intermediários, enquanto em jogos de tabuleiro ou quebra-cabeça 4 a 5 frames podem passar despercebidos [F: ggpo2019devguide].

### Transporte: TCP vs. UDP com redundância

Fiedler mostra que sobre TCP a retransmissão de um pacote perdido leva cerca de RTT×2 e a simulação trava enquanto espera; com 100 ms de latência e 1% de perda aparecem travamentos a cada poucos segundos, e com 250 ms e 5% de perda o problema piora bastante [F: fiedler2014lockstep]. A alternativa é UDP com envio redundante: cada pacote inclui todas as entradas ainda não confirmadas, o receptor responde com *ack* da mais recente, e o remetente descarta as confirmadas; com codificação por diferença, cada entrada repetida custa 1 bit e uma mudança 7 bits; pior caso de 120 entradas em cerca de 90 bytes; a demonstração funciona com 2 segundos de latência e 25% de perda [F: fiedler2014lockstep]. O autor admite que, sem perda ou com latência muito baixa, TCP pode funcionar [F: fiedler2014lockstep].

### Rollback

O GGPO descreve a motivação: técnicas tradicionais compensam o tempo de transmissão atrasando as entradas, o que deixa o jogo lento; o rollback usa predição de entradas e execução especulativa para aplicar entradas imediatamente, criando "a ilusão de uma rede de latência zero" [F: ggpo2019readme]. Cannon, em entrevista, descreve que, "Instead of inserting any internet latency between the button press and the start of the move", o atraso recai sobre o início do movimento do oponente, com animações de preenchimento [F: orland2011cannon]. O guia do desenvolvedor exige: "The game simulation must be fully deterministic", estado encapsulado e serializável, e capacidade de carregar, salvar e executar um frame sem renderizar; frames executados com predição errada são "temporarily executing the incorrect prediction frames" e são refeitos; ao atingir o "internal prediction limit", a chamada de sincronização retorna erro e o jogo não deve avançar [F: ggpo2019devguide]. Exemplo do guia: com delay de 1 frame e pacote levando 4 frames, o rollback é de cerca de 3 frames [F: ggpo2019devguide].

## Algoritmos e modelos relevantes

- Playout delay buffer e entradas indexadas por frame [F: fiedler2014lockstep].
- Turnos de comunicação com agendamento de dois turnos à frente e *speed control* adaptativo [F: bettner2001archers].
- Entradas redundantes sobre UDP com ack cumulativo [F: fiedler2014lockstep].
- Save/load de estado e reexecução (rollback) [F: ggpo2019devguide].
- Checksums de estado para detecção de desync [F: bettner2001archers; fiedler2014lockstep].

## Requisitos e pressupostos

**Determinismo bit a bit.** Fiedler exige "Exactly the same" resultado, a ponto de um checksum do estado físico ser idêntico em cada frame [F: fiedler2014lockstep]. Fontes de não determinismo documentadas:

- *Ponto flutuante.* "Differences in floating point behavior between compilers, OS's and even instruction sets" tornam quase impossível garantir determinismo entre plataformas; pode não haver determinismo entre builds de debug e release [F: fiedler2014lockstep]. Em artigo dedicado, Fiedler conclui que a resposta é "yes, if…": é possível com o mesmo compilador, mesma arquitetura e ajustes de plataforma; cita desenvolvedores que fixam o modo da FPU e o verificam a cada tick, evitam funções transcendentais e usam modo IEEE estrito com perda de desempenho [F: fiedler2010floatingpoint].
- *RNG.* Em Age of Empires os geradores eram semeados e sincronizados; para aleatoriedade fora da simulação (sons) o estado do gerador era salvo e restaurado, e todos os programadores precisavam fazer o mesmo número de chamadas dentro da simulação [F: bettner2001archers]. Fiedler obteve determinismo no ODE semeando o gerador com o número do frame [F: fiedler2014lockstep].
- *Ordem de iteração e bibliotecas.* Fiedler cita equipe que teve problemas com API de física cujo solver variava o número de iterações conforme a CPU [F: fiedler2010floatingpoint]. [I] Qualquer iteração sobre estruturas com ordem não determinística (hash maps, threads) quebra a propriedade.

**Detecção de desync.** Bettner relata checksums do mundo, objetos, pathfinding e targeting; qualquer divergência marcava "out of sync" e "the game stopped"; a depuração usava rastros de mensagens de cerca de 50 MB; pequenas diferenças se multiplicavam (um cervo levemente desalinhado afetava aldeões minutos depois) [F: bettner2001archers]. [I] Como não há autoridade, não existe recuperação natural: ou se reinicia de um snapshot acordado, ou a partida termina.

**Todos presentes.** Entrar no meio exige transferir o estado inteiro e todas as entradas desde então; Fiedler aponta que isso torna a entrada tardia impraticável e exige lobby [F: fiedler2010networking].

## Vantagens e limitações

Vantagens: banda quase constante com o número de objetos [F: fiedler2014lockstep]; estado nunca transmitido, o que suporta milhares de unidades [F: bettner2001archers]; replay e reprodução a partir do log de entradas [I]; sem servidor obrigatório [F: fiedler2010networking]; simetria (ninguém é autoridade) e, com rollback, resposta imediata à própria entrada [F: ggpo2019readme].

Limitações: determinismo "exceptionally difficult to ensure" [F: fiedler2010networking]; latência ditada pelo participante mais lento [F: fiedler2010networking]; sem entrada tardia [F: fiedler2010networking]; cada participante conhece o estado completo, o que facilita trapaças de informação (*map hack*) [I]; rollback exige save/load rápido e custo de CPU de reexecução [F: ggpo2019devguide].

## Alternativas e comparações

Fiedler organiza sua série em três abordagens: "deterministic lockstep", "snapshot interpolation" e "state synchronization" [F: fiedler2014networkedphysics]. Para a diferença de comportamento sob atraso: no lockstep a simulação para e espera a entrada; em state synchronization, continua extrapolando com a última entrada recebida [F: fiedler2015statesync]. Tabela em rtm.arch.comparison.

## Métricas e métodos de avaliação

- Travamentos (*hitches*) por minuto em função de latência, perda e tamanho do buffer [F: fiedler2014lockstep].
- Banda por pacote: 2 a 15 frames de entrada por pacote em média, pior caso cerca de 90 bytes mais cerca de 15 bytes de overhead no exemplo de Fiedler [F: fiedler2014lockstep].
- Frequência de desync (checksums divergentes) por hora de jogo [F: bettner2001archers].
- Profundidade média de rollback em frames e taxa de predições incorretas [F: ggpo2019devguide].

## Exemplo técnico independente de domínio

```
# cada participante, simulação a taxa fixa
buffer[frame] = {}                     # entradas por frame, por participante
delay = D                              # frames de input delay

a cada frame local f:
  minha = amostrar_entrada()
  buffer[f + delay][eu] = minha
  enviar_redundante(todas_entradas_nao_confirmadas())   # UDP
  se buffer[f] tem entrada de TODOS:
      estado = simular(estado, buffer[f])               # determinístico
      se f % K == 0: difundir(checksum(estado), f)
  senao:
      esperar()                                         # ou prever + rollback

ao_receber_checksum(c, f_remoto):
  se c != checksum_local[f_remoto]: declarar_desync()
```

## Relações com outros conceitos

Alternativa às outras arquiteturas e às técnicas de sincronização por estado (rtm.sync.state-synchronization, rtm.sync.snapshot-interpolation). Depende de rtm.net.ordering-and-reliability (entradas de cada frame precisam chegar, em ordem). Complementa rtm.arch.peer-to-peer e rtm.arch.relay-server, que são os transportes usuais, e rtm.pred.client-side-prediction (rollback é predição aplicada a entradas remotas). Relaciona-se com rtm.proto.udp e rtm.proto.tcp (escolha de transporte), rtm.net.bandwidth e rtm.mp.turn-based (turnos de comunicação).

## Lacunas e questões abertas

- O artigo de Bettner e Terrano está publicado em gamedeveloper.com com byline apenas de Paul Bettner e data 2001-03-22; a coautoria de Mark Terrano e a apresentação na GDC 2001 não aparecem na página e ficam **não verificadas**. O GDC Vault estava em manutenção na data da consulta.
- O artigo de Tony Cannon "Fight the Lag!" (Game Developer Magazine, 2012) não foi localizado em forma acessível; **não verificado**. A caracterização do rollback usa o README e o guia do GGPO e uma entrevista (fonte secundária).
- O guia do GGPO não informa o valor do limite interno de predição nem o número máximo de jogadores [F: ggpo2019devguide].
- Não há fonte aberta nesta sessão sobre lockstep com servidor autoritativo que valide entradas e redistribua (modelo híbrido); registrar quando verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fiedler2014lockstep | tecnico | 2026-10-29 |
| fiedler2010floatingpoint | tecnico | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
| fiedler2014networkedphysics | tecnico | 2026-10-29 |
| fiedler2015statesync | tecnico | 2026-10-29 |
| bettner2001archers | tecnico | 2026-10-29 |
| ggpo2019readme | tecnico | 2026-10-29 |
| ggpo2019devguide | tecnico | 2026-10-29 |
| orland2011cannon | secundario | 2026-10-29 |
