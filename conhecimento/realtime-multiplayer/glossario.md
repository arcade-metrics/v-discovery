---
id: rtm.glossario
titulo: Glossário de tempo real e multiplayer
tipo: glossario
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Glossário: tempo real e multiplayer

Termos consolidados do domínio. Cada entrada tem definição curta e o id do documento que a aprofunda e cita a fonte. Termos em inglês quando esse é o uso consolidado na literatura. Os campos `termos:` dos frontmatters listam 436 termos distintos; este glossário seleciona os que aparecem em mais de um documento ou que são centrais à área.

## Tempo real e padrões de comunicação

| Termo | Definição | Documento |
|---|---|---|
| tempo real | sistema cuja correção depende do instante em que o resultado é produzido, não só do valor | rtm.rt.realtime-systems |
| hard / firm / soft real-time | perder o prazo é falha total / perdas raras toleráveis, resultado atrasado vale zero / utilidade degrada gradualmente | rtm.rt.realtime-systems |
| deadline | prazo associado a uma tarefa ou resposta | rtm.rt.realtime-systems |
| tick, tick rate | passo fixo da simulação e sua frequência por segundo; faz papel de período e deadline soft | rtm.rt.realtime-systems, rtm.arch.authoritative-server |
| polling | cliente consulta periodicamente; atraso médio de meio intervalo | rtm.rt.communication-patterns |
| long polling | servidor segura a resposta até haver evento ou timeout | rtm.rt.communication-patterns, rtm.proto.http-streaming |
| server-sent events | streaming unidirecional padronizado (text/event-stream, Last-Event-ID) | rtm.proto.http-streaming |
| publish/subscribe | distribuição 1:N por tópico via intermediário, desacoplando produtores e consumidores | rtm.rt.communication-patterns, rtm.arch.event-driven |

## Rede

| Termo | Definição | Documento |
|---|---|---|
| latência | tempo entre emissão e chegada de uma informação | rtm.net.latency |
| RTT | atraso de ida e volta, do primeiro bit enviado ao último bit da resposta (RFC 2681) | rtm.net.latency, rtm.perf.metrics |
| one-way delay | atraso unidirecional em wire time (RFC 7679); exige relógios sincronizados | rtm.net.latency, rtm.perf.metrics |
| atraso de propagação / serialização / enfileiramento / processamento | componentes do atraso de um pacote | rtm.net.latency |
| SRTT | RTT suavizado por média móvel exponencial | rtm.net.latency |
| jitter | variação do atraso entre pacotes de um fluxo; termo evitado pela RFC 3393 em favor de IPDV | rtm.net.jitter |
| IPDV / PDV | diferença de atraso entre pacotes consecutivos / atraso relativo ao mínimo do intervalo | rtm.net.jitter, rtm.perf.metrics |
| jitter buffer | fila que atrasa a entrega para consumo em ritmo regular; custo em latência (playout delay) | rtm.net.jitter |
| perda de pacotes, loss ratio | pacote não recebido dentro de um prazo (RFC 7680); razão perdas/total | rtm.net.packet-loss |
| perda em rajada, Gilbert-Elliott | sequência de perdas próximas; modelo de Markov de dois estados | rtm.net.packet-loss |
| retransmissão / FEC / redundância | recuperar perda por reenvio após feedback / por pacotes de reparo sem feedback / repetindo dados anteriores | rtm.net.packet-loss |
| RTO | temporizador de retransmissão do TCP, piso de 1 s (RFC 6298) | rtm.net.packet-loss, rtm.proto.tcp |
| ordenação total / por canal / parcial | entrega na ordem de envio para todo o fluxo / só dentro do canal / só respeitando causalidade | rtm.net.ordering-and-reliability |
| confiabilidade seletiva | persistência definida por mensagem (tempo de vida ou número de retransmissões) | rtm.net.ordering-and-reliability, rtm.proto.udp |
| head-of-line blocking | dados já recebidos retidos até chegar um anterior na ordem | rtm.net.ordering-and-reliability, rtm.proto.tcp |
| reliable ordered / reliable unordered / unreliable | os três serviços usuais construídos sobre datagramas | rtm.net.ordering-and-reliability |
| ack bits / ack bitfield | ack mais 32 bits confirmando redundantemente os pacotes anteriores | rtm.net.ordering-and-reliability, rtm.sync.delta-compression |
| sequence number | contador monotônico por emissor que ordena, detecta lacunas e deduplica | rtm.rel.delivery-semantics, rtm.pred.server-reconciliation |
| largura de banda, orçamento de bits | capacidade por unidade de tempo; limite de bytes por pacote ou por segundo por cliente | rtm.net.bandwidth |
| bitpacking, quantização, delta encoding | escrever só os bits necessários; reduzir precisão; codificar contra baseline confirmado | rtm.net.bandwidth, rtm.sync.delta-compression |
| MTU | tamanho máximo de pacote; 1200 bytes como payload conservador | rtm.net.bandwidth |
| offset / skew / drift | diferença do relógio / sua taxa / variação da taxa (RFC 2330) | rtm.net.clock-synchronization |
| NTP, stratum | protocolo de sincronização com quatro carimbos; nível hierárquico da fonte | rtm.net.clock-synchronization |
| server time | tempo do servidor como referência; cliente mantém tempo local mais offset | rtm.net.clock-synchronization |
| relógio monotônico vs wall clock | nunca retrocede (medir intervalos) vs ajustável (exibir) | rtm.net.clock-synchronization |
| happens-before | relação causal parcial de Lamport | rtm.net.logical-clocks |
| relógio de Lamport / relógio vetorial | contador consistente com a causalidade / vetor que a caracteriza exatamente | rtm.net.logical-clocks |
| hybrid logical clock | relógio lógico limitado a ficar próximo do tempo físico | rtm.net.logical-clocks |

## Protocolos

| Termo | Definição | Documento |
|---|---|---|
| TCP | transporte orientado a conexão com byte stream confiável e ordenado (RFC 9293) | rtm.proto.tcp |
| Nagle, TCP_NODELAY | coalescência de segmentos pequenos; opção de socket que a desativa | rtm.proto.tcp |
| UDP, datagram | transporte sem conexão nem confiabilidade (RFC 768); unidade com fronteiras preservadas | rtm.proto.udp |
| NAT traversal, STUN, TURN, ICE | técnicas para hosts atrás de NAT se alcançarem; descoberta de endereço refletido; relay de último recurso; coleta e teste de candidatos | rtm.proto.udp, rtm.arch.peer-to-peer |
| WebSocket | protocolo de mensagens bidirecional sobre TCP com handshake HTTP (RFC 6455) | rtm.proto.websocket |
| opening handshake, frame, opcode, masking | GET com Upgrade respondido com 101; unidade de enquadramento e seu tipo; XOR obrigatório cliente para servidor | rtm.proto.websocket |
| ping/pong | frames de controle de keep-alive; não expostos à API do navegador | rtm.proto.websocket, rtm.rel.reconnection |
| close code, subprotocol | código de 2 bytes no fechamento; protocolo de aplicação negociado no handshake | rtm.proto.websocket |
| extended CONNECT | WebSocket sobre HTTP/2 e HTTP/3 (RFC 8441, 9220) | rtm.proto.websocket |
| WebRTC, data channel | conjunto de protocolos IETF mais API W3C; canal de dados sobre SCTP/DTLS/UDP com confiabilidade e ordem configuráveis (RFC 8831) | rtm.proto.webrtc |
| SCTP, DTLS, PR-SCTP | transporte orientado a mensagens com multi-streaming; TLS sobre datagramas; entrega parcialmente confiável | rtm.proto.webrtc, rtm.sec.transport-security |
| signaling, SFU | troca de SDP e candidatos fora das RFCs; servidor que termina conexões WebRTC e repassa fluxos | rtm.proto.webrtc |
| WebTransport | streams e datagramas cliente-servidor sobre HTTP/3 (drafts IETF, CR W3C em 2026) | rtm.proto.webtransport |
| QUIC, 0-RTT, connection migration | transporte multiplexado sobre UDP com TLS 1.3 integrado (RFC 9000 a 9002); envio antes da resposta; conexão sobrevive a troca de IP | rtm.proto.quic |
| HTTP streaming, chunked | resposta mantida aberta com várias peças de dados | rtm.proto.http-streaming |
| Internet Standard / Proposed Standard / Recommendation / Living Standard | níveis de maturidade normativa do IETF, W3C e WHATWG | rtm.std.index |

## Arquiteturas

| Termo | Definição | Documento |
|---|---|---|
| authoritative server | servidor é a única fonte de verdade; clientes enviam entradas e recebem estado | rtm.arch.authoritative-server |
| dedicated server / listen server / host | máquina só para simulação / instância que simula e também é cliente / nó que detém a autoridade da sessão | rtm.arch.authoritative-server |
| dumb client | cliente que só envia entradas e exibe o estado recebido, sem simular | rtm.arch.authoritative-server, rtm.pred.client-side-prediction |
| relay server, relayed multiplayer, client-authoritative | servidor repassa mensagens sem simular nem validar; autoridade fica nos clientes | rtm.arch.relay-server |
| peer-to-peer, full mesh | pares trocam mensagens sem servidor de simulação; cada par conectado a todos, tráfego O(n²) | rtm.arch.peer-to-peer |
| deterministic lockstep | só entradas são trocadas; todos simulam identicamente | rtm.arch.deterministic-lockstep |
| determinismo bit a bit | mesma entrada e estado produzem resultado idêntico em todas as máquinas | rtm.arch.deterministic-lockstep |
| input delay, playout delay buffer | atraso fixo entre amostrar e executar entrada; buffer indexado por frame | rtm.arch.deterministic-lockstep |
| communication turn, speed control | turno em que comandos são coletados e agendados dois turnos à frente; ajuste dinâmico da duração do turno | rtm.arch.deterministic-lockstep, rtm.case.age-of-empires |
| desync / out of sync | divergência de estado entre participantes, detectada por checksum | rtm.arch.deterministic-lockstep |
| rollback netcode | predição de entradas remotas, execução especulativa e reexecução ao errar | rtm.arch.deterministic-lockstep |
| event-driven architecture, event sourcing, event store | estado organizado em torno de eventos imutáveis; toda mudança como log append-only | rtm.arch.event-driven |
| command vs event, CQRS, projection | intenção (pode ser rejeitada) vs fato ocorrido; separação de escrita e leitura; estado derivado do log | rtm.arch.event-driven |
| host migration | transferência da autoridade para outro nó ou par quando o atual sai | rtm.arch.authoritative-server, rtm.mp.session-lifecycle, rtm.rel.fault-tolerance |

## Sincronização de estado

| Termo | Definição | Documento |
|---|---|---|
| state replication | manter N réplicas de um estado coerentes sob latência, jitter e perda, com uma autoridade por objeto | rtm.sync.state-replication |
| ghost | cópia de um objeto do servidor replicada em um host remoto (termo do TRIBES) | rtm.sync.state-replication, rtm.case.tribes |
| snapshot | captura do estado relevante de todos os objetos visíveis em um instante | rtm.sync.snapshot-interpolation, rtm.case.quake3 |
| interpolation delay | atraso deliberado entre recepção e exibição para interpolar entre dois snapshots passados | rtm.sync.snapshot-interpolation, rtm.pred.entity-interpolation |
| hermite interpolation | interpolação que usa posição e velocidade nos pontos de amostra | rtm.sync.snapshot-interpolation |
| state synchronization | ambos os lados simulam; viajam entradas e um subconjunto priorizado do estado; o receptor extrapola e aceita correções | rtm.sync.state-synchronization |
| priority accumulator, bandwidth budget | acumulador por objeto que decide o que cabe no pacote; orçamento fixo de bytes por pacote | rtm.sync.state-synchronization, rtm.net.bandwidth |
| visual smoothing | esconder correções só na renderização por um offset de erro que decai | rtm.sync.state-synchronization |
| dead reckoning, DRM | extrapolação cinemática por entidade; o emissor só atualiza quando sua própria extrapolação excede um limiar; algoritmos padronizados em DIS | rtm.sync.dead-reckoning |
| error threshold, heartbeat (DIS), convergence smoothing | limiar que dispara atualização; atualização periódica mesmo sem violação; transição suave para a posição corrigida | rtm.sync.dead-reckoning |
| delta compression, acknowledged baseline | enviar só a diferença em relação a um estado que o receptor comprovadamente possui | rtm.sync.delta-compression |
| smallest three | codificação de quaternion com os três menores componentes mais índice do maior | rtm.sync.delta-compression |
| state mask | bitmask por objeto marcando grupos de estado alterados (TRIBES) | rtm.sync.delta-compression, rtm.case.tribes |
| interest management, area of interest | determinar o que é relevante para cada participante e enviar só isso; região que ele percebe | rtm.sync.interest-management |
| aura / nimbus | área de presença de um objeto / área de percepção; x percebe y quando nimbus(x) intersecta aura(y) | rtm.sync.interest-management |
| scoping | determinação de quais objetos existem como ghost em cada cliente, com prioridade | rtm.sync.interest-management, rtm.case.tribes |
| CRDT | tipo de dado replicado cujas réplicas podem ser atualizadas sem coordenação e convergem por construção | rtm.sync.crdt |
| strong eventual consistency | réplicas que receberam as mesmas atualizações têm o mesmo estado, sem rollback | rtm.sync.crdt |
| state-based (CvRDT) / operation-based (CmRDT) | réplicas trocam estados e aplicam merge de semilattice / propagam operações que comutam sob entrega causal | rtm.sync.crdt |
| G-Counter, PN-Counter, LWW-Register, OR-Set, RGA | contador por réplica; contador com negativos; registro por timestamp; conjunto add-wins; sequência replicada | rtm.sync.crdt |
| tombstone, delta-state CRDT, state vector | marca de removido mantida nos metadados; propagar só deltas; próximo clock esperado de cada cliente | rtm.sync.crdt |
| operational transformation | operações remotas concorrentes são transformadas contra as locais para preservar intenção e convergir | rtm.sync.operational-transformation |
| transformation function, TP1 / TP2 | função que ajusta uma operação em face de outra; propriedades para convergência com 2 e com 3 ou mais operações concorrentes | rtm.sync.operational-transformation |
| dOPT, Jupiter | algoritmo distribuído de OT de Ellis e Gibbs; sistema cliente-servidor em que cada cliente transforma só contra o servidor | rtm.sync.operational-transformation, rtm.case.jupiter |
| last-writer-wins por propriedade | conflito só entre a mesma propriedade do mesmo objeto; vence o último valor recebido pelo servidor | rtm.case.figma-multiplayer |
| fractional indexing | ordem de irmãos como fração; inserção toma o ponto médio | rtm.case.figma-multiplayer |

## Predição e reconciliação

| Termo | Definição | Documento |
|---|---|---|
| client-side prediction | o cliente aplica a própria entrada ao estado local de imediato e é corrigido se divergir | rtm.pred.client-side-prediction |
| user command, input buffer | registro de entrada enviado ao servidor; fila de comandos ainda não confirmados | rtm.pred.client-side-prediction |
| misprediction | divergência entre o estado previsto e o autoritativo; correção visível | rtm.pred.client-side-prediction, rtm.perf.metrics |
| shared simulation code | mesma lógica de movimento em cliente e servidor | rtm.pred.client-side-prediction |
| server reconciliation, rewind and replay | ao receber estado autoritativo, o cliente aceita-o, descarta entradas confirmadas e reaplica as pendentes | rtm.pred.server-reconciliation |
| last acknowledged input, correction smoothing | última entrada confirmada pelo servidor; diluir no tempo a correção residual | rtm.pred.server-reconciliation |
| entity interpolation | exibir entidades remotas com atraso deliberado, interpolando entre atualizações recebidas | rtm.pred.entity-interpolation |
| extrapolation | estimar posição futura a partir de velocidade e aceleração, por tempo limitado | rtm.pred.entity-interpolation, rtm.sync.dead-reckoning |
| position history | série temporal de poses por entidade usada para interpolar no cliente e rebobinar no servidor | rtm.pred.entity-interpolation, rtm.case.half-life |
| lag compensation, time warp | o servidor rebobina as outras entidades ao instante em que o cliente agiu, resolve a ação e restaura | rtm.pred.lag-compensation |
| command execution time, rollback limit | instante-alvo do rewind; profundidade máxima do histórico | rtm.pred.lag-compensation |
| shot around the corner | ser atingido já atrás da cobertura porque o servidor avaliou o tiro no passado | rtm.pred.lag-compensation |
| latency compensation, self-prediction, other-prediction | termo guarda-chuva da taxonomia de Liu, Xu e Claypool; prever o próprio estado; estimar o estado dos outros | rtm.pred.comparison |
| determinism requirement | grau de reprodutibilidade exigido: "suficiente" para predição, estrito para lockstep, nenhum para interpolação | rtm.pred.comparison |

## Multiplayer: salas, partidas, presença

| Termo | Definição | Documento |
|---|---|---|
| room, match | unidade de sessão compartilhada que vive em um único processo; partida, relayed ou autoritativa | rtm.mp.rooms-and-matches |
| lobby, party | sala de espera ou listagem viva; grupo temporário com líder que entra junto no matchmaker | rtm.mp.rooms-and-matches |
| seat reservation | reserva de vaga emitida pelo matchmaker e consumida pelo cliente ao conectar | rtm.mp.rooms-and-matches, rtm.fw.colyseus |
| match label, op code | metadado de partida para busca; código numérico que classifica uma mensagem antes de decodificá-la | rtm.mp.rooms-and-matches, rtm.mp.turn-based |
| matchmaking, ticket | agrupar participantes de uma fila por habilidade, região, grupo e modo; pedido de um usuário ou party | rtm.mp.matchmaking |
| rating, Elo, Glicko, rating deviation, TrueSkill | estimativa de habilidade; sistema de xadrez; sistema com incerteza explícita; desvio do rating; sistema bayesiano para equipes e empates | rtm.mp.matchmaking |
| match quality | em TrueSkill, probabilidade de empate relativa a jogadores iguais | rtm.mp.matchmaking |
| presence, status | quem está conectado, em que contexto e com que estado declarado; string ou JSON publicado por conexão | rtm.mp.presence |
| awareness | canal efêmero de presença separado do documento e não persistido (Yjs) | rtm.mp.presence |
| fan-out | difusão de um evento a n destinatários; com n emissores, custo O(n²) | rtm.mp.presence |
| turn-based, asynchronous multiplayer | ação serializada, só o jogador da vez age; partida de horas ou dias, persistida | rtm.mp.turn-based |
| turn timeout, forfeit, move validation | prazo para jogar; derrota por abandono ou timeout; verificação no servidor de turno, legalidade e formato | rtm.mp.turn-based |
| session lifecycle, ready check | criação, join, ready, início, execução, término, resultado, persistência; confirmação de cada participante antes de iniciar | rtm.mp.session-lifecycle |
| consented leave, reconnection window, graceful shutdown | saída voluntária distinta de queda; tempo em que o assento é mantido; encerramento ordenado do processo | rtm.mp.session-lifecycle |

## Frameworks

| Termo | Definição | Documento |
|---|---|---|
| match handler, match loop | funções que o servidor Nakama invoca para executar uma partida autoritativa; função chamada a cada tick | rtm.fw.nakama |
| authoritative match, relayed multiplayer (Nakama) | estado em memória no servidor, mudado só por entrada validada; servidor repassa sem validar | rtm.fw.nakama |
| session token / refresh token | JWT de curta duração renovado por refresh token | rtm.fw.nakama, rtm.sec.authentication |
| schema, patch rate | definição de estado sincronizável do Colyseus serializada em patches binários; intervalo de envio dos patches | rtm.fw.colyseus |
| state view | filtro por cliente que define quais instâncias e campos cada um recebe (Colyseus) | rtm.fw.colyseus |
| presence (Colyseus), driver | componente de pub/sub e chave-valor entre processos; armazenamento dos dados de salas do matchmaker | rtm.fw.colyseus |
| allowReconnection, reconnection token | retém o assento de um cliente caído por N segundos e permite rejoin por token | rtm.fw.colyseus, rtm.rel.reconnection |
| netcode de engine | biblioteca de replicação acoplada a um motor de jogo | rtm.fw.alternatives |
| orquestrador de servidores dedicados | sistema que coloca, escala e aloca processos de servidor de jogo | rtm.fw.alternatives |
| pub/sub gerenciado, infraestrutura de colaboração | serviço de canais e presença operado pelo fornecedor; serviço ou biblioteca para edição simultânea convergente | rtm.fw.alternatives |
| autoridade distribuída | cada cliente é dono de um subconjunto de objetos | rtm.fw.alternatives |

## Confiabilidade e segurança

| Termo | Definição | Documento |
|---|---|---|
| heartbeat | mensagem periódica cuja ausência sinaliza queda; define o pior caso de detecção | rtm.rel.reconnection, rtm.mp.presence |
| backoff exponencial com jitter | espera entre retentativas que cresce geometricamente até um teto e é aleatorizada | rtm.rel.reconnection |
| token de reconexão, janela de graça | credencial que identifica a sessão lógica a retomar; intervalo em que vaga e estado são preservados | rtm.rel.reconnection |
| checkpoint | cópia periódica do estado em memória para armazenamento durável | rtm.rel.fault-tolerance |
| PACELC | se há partição, disponibilidade vs consistência; senão, latência vs consistência | rtm.rel.fault-tolerance |
| graceful degradation, chaos engineering | reduzir funcionalidade deliberadamente sob condição adversa; experimentar com falhas reais para testar hipóteses de estabilidade | rtm.rel.fault-tolerance |
| at-most-once / at-least-once / exactly-once | pode perder mas nunca repete / nunca perde mas pode repetir / processada uma única vez | rtm.rel.delivery-semantics |
| idempotência, deduplicação | aplicar N vezes equivale a aplicar uma; descartar cópias já vistas por id ou sequência | rtm.rel.delivery-semantics |
| JWT, access token / refresh token | claims assinadas ou cifradas (RFC 7519); credencial de curta duração / credencial para obter nova | rtm.sec.authentication |
| Origin, CSWSH | cabeçalho do handshake que identifica a origem do script; sequestro de WebSocket entre sites por cookie | rtm.sec.authentication |
| autorização por sala | verificação por entrada, por mensagem e por leitura do que o cliente pode fazer | rtm.sec.authentication |
| cheating, misplaced trust | vantagem que o jogador não deveria alcançar; adulteração de código ou dados confiados ao cliente | rtm.sec.cheating |
| wallhack, look-ahead cheat, lag switch | exposição de informação; atrasar o próprio lance até conhecer os dos outros; induzir perda ou atraso para explorar compensação | rtm.sec.cheating |
| wss, DTLS, 0-RTT (segurança) | WebSocket sobre TLS; TLS para datagramas; dados no primeiro voo sem proteção contra replay | rtm.sec.transport-security |

## Desempenho e testes

| Termo | Definição | Documento |
|---|---|---|
| percentil (p50/p95/p99) | agregação por distribuição em vez de média | rtm.perf.metrics |
| quatro sinais de ouro | latência, tráfego, erros, saturação | rtm.perf.metrics |
| QoE, opinion model | qualidade de experiência avaliada subjetivamente; modelo que a prevê a partir de parâmetros técnicos | rtm.perf.qoe-thresholds |
| precisão / deadline (Claypool) | eixos para classificar a sensibilidade de ações à latência | rtm.perf.qoe-thresholds |
| modelo avatar / onipresente | interação por um único personagem / controle simultâneo de vários recursos | rtm.perf.qoe-thresholds |
| virtual user, cliente sintético / realista | cliente simulado em teste de carga; padrão fixo de mensagens vs reprodução do protocolo real | rtm.perf.load-testing |
| smoke / average-load / stress / soak / spike / breakpoint | tipos de teste de carga | rtm.perf.load-testing |
| porta efêmera, RLIMIT_NOFILE | porta local de conexões de saída; limite por processo de sockets abertos | rtm.perf.load-testing |
| emulação de rede, netem, toxic | introduzir latência, variação, perda, reordenação e limite de banda; disciplina de fila Linux; condição de falha em proxy | rtm.perf.network-emulation |
| matriz de cenários | combinações de condições de rede (boa, média, ruim, móvel, hostil) com métricas e critérios por cenário | rtm.perf.network-emulation |
