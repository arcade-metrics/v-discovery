---
id: rtm.perf.load-testing
titulo: Teste de carga para WebSocket e UDP
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [k62026ws, k62026metrics, k62026testtypes, k62026finetune, artillery2026ws, artillery2026socketio, locust2026other, gatling2026ws, man7getrlimit, kernel2026ipsysctl, rfc6056, google2016sre]
relacoes:
  - { tipo: depende-de, alvo: rtm.perf.metrics }
  - { tipo: depende-de, alvo: rtm.proto.websocket }
  - { tipo: complementa, alvo: rtm.perf.network-emulation }
  - { tipo: complementa, alvo: rtm.rel.fault-tolerance }
  - { tipo: complementa, alvo: rtm.mp.rooms-and-matches }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.proto.tcp }
  - { tipo: relacionado-a, alvo: rtm.fw.comparison }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [virtual user, ramp-up, soak test, spike test, stress test, breakpoint test, cliente sintético, cliente realista, descritor de arquivo, porta efêmera, TIME_WAIT]
---

# Teste de carga para WebSocket e UDP

## Definição e terminologia

Teste de carga é a execução controlada de muitos clientes simulados contra o sistema para medir como as métricas (ver `rtm.perf.metrics`) se comportam em função do número de conexões, da taxa de mensagens e do tempo. A documentação do k6 nomeia os tipos: *smoke* ("validate that your script works and that the system performs adequately under minimal load"), *average-load* ("assess how your system performs under expected normal conditions"), *stress* ("assess how a system performs at its limits when load exceeds the expected average"), *soak* ("assess the reliability and performance of your system over extended periods"), *spike* ("validate the behavior and survival of your system in cases of sudden, short, and massive increases in activity") e *breakpoint* ("gradually increase load to identify the capacity limits of the system") [F: k62026testtypes].

Um **virtual user** (VU) é um cliente simulado; em k6, `vus` é "Current number of active virtual users" [F: k62026metrics]. Um cliente **sintético** executa um padrão fixo de mensagens; um cliente **realista** reproduz o comportamento do protocolo de aplicação (autenticação, entrada em sala, entradas na cadência do jogo, reação ao estado recebido) [I].

## Problema que resolve

Sistemas de tempo real falham de modos que testes funcionais não revelam: filas de saída que crescem com clientes lentos, ticks que estouram o orçamento quando a sala enche, garbage collection que vira jitter, limites do sistema operacional que aparecem só na milésima conexão. Teste de carga é o único modo de observar esses modos antes dos usuários, e de atribuir números a "quantas conexões por nó".

## Fundamentos e funcionamento

### Ferramentas com suporte verificado a WebSocket

| Ferramenta | Suporte | Métricas próprias | Observações da documentação |
|---|---|---|---|
| k6 (`k6/ws`) | `ws.connect(url, params, callback)` retorna Socket com `on`, `send`, `sendBinary`, `ping`, `setInterval`, `setTimeout`, `close`; eventos `open`, `message`, `binaryMessage`, `ping`, `pong`, `close`, `error` [F: k62026ws] | `ws_connecting`, `ws_session_duration`, `ws_sessions`, `ws_ping`, `ws_msgs_received`, `ws_msgs_sent`, mais `data_sent`, `data_received`, `vus`, `iterations` [F: k62026metrics] | a página indica que "A module with a better and standard API exists" (`k6/websockets`, API padrão com event loop global) e a recomenda quando possível [F: k62026ws]; `connect` "blocks the test finalization until the connection is closed" [F: k62026ws] |
| Artillery (engine `ws`) | ações `connect`, `send`, `think`, `loop`, `function`; `connect` primeiro no fluxo; cabeçalhos e subprotocolos em `config.ws` [F: artillery2026ws] | `websocket.messages_sent`, `websocket.messages_received`, `websocket.send_rate`, `websocket.receive_rate` [F: artillery2026ws] | objetos em `send` são serializados em JSON; `think` longo mantém o cliente conectado ouvindo [F: artillery2026ws] |
| Artillery (engine `socketio`) | ação `emit` com canal e payload; `response` e `acknowledge` para validar; `namespace` [F: artillery2026socketio] | as do engine | "the response data is expected within the same namespace" [F: artillery2026socketio] |
| Gatling (`ws`) | `ws(name).connect(url)`, `sendText`, `sendBytes`, `await(seconds).on(check)`, `close()` com código 1000, `wsBaseUrl` [F: gatling2026ws] | checks por mensagem | "Gatling currently only supports blocking checks that will wait until receiving expected message or timing out" [F: gatling2026ws] |
| Locust | sem cliente WebSocket nativo: "Locust only comes with built-in support for HTTP/HTTPS but it can be extended to test almost any system" disparando o evento `request` após cada chamada; exemplos XML-RPC e gRPC; `SocketIOUser` marcado "experimental and may change without notice" [F: locust2026other] | `request` com tipo, nome, tempo de resposta, tamanho, exceção [F: locust2026other] | bibliotecas precisam ser compatíveis com gevent, senão "This will block the whole Locust/Python process" [F: locust2026other] |

### UDP e protocolos próprios

Nenhuma das quatro ferramentas documenta cliente UDP para protocolos de jogo. O caminho documentado é o do Locust: encapsular a biblioteca do protocolo e emitir eventos de requisição [F: locust2026other]; o mesmo é possível em k6 via extensões, não verificado nesta sessão. [I] Na prática, para UDP próprio o gerador de carga costuma ser o próprio cliente do sistema compilado em modo *headless*, instrumentado com as métricas de `rtm.perf.metrics`; isso dá cliente realista de graça, ao custo de precisar de máquinas de carga capazes.

### Métricas a coletar

Do lado do gerador: conexões abertas, tempo de handshake, mensagens e bytes por segundo em cada sentido, RTT de ping de aplicação, erros e fechamentos por código [F: k62026metrics; F: artillery2026ws]. Do lado do servidor: tempo por tick, fila de saída por cliente, CPU, memória, descritores abertos, e os quatro sinais (latência, tráfego, erros, saturação) [F: google2016sre]. Sempre em percentis por janela, nunca média (ver `rtm.perf.metrics`).

### Metodologia

A documentação do k6 recomenda: "Stick to simple load patterns. For all test types, directions is enough: ramp-up, plateau, ramp-down", e desaconselha padrões "rollercoaster" por desperdiçarem recursos e dificultarem isolar causas [F: k62026testtypes]. Durações indicadas: smoke de segundos a minutos; average e stress de 5 a 60 minutos; soak por horas; spike por poucos minutos com carga muito alta; breakpoint até o sistema falhar, poucas vezes [F: k62026testtypes].

[I] Para tempo real, a sequência útil é:

1. **Smoke** com poucos VUs realistas para validar o script (autenticação, sala, cadência).
2. **Average-load** no número esperado de conexões por nó, por 15 a 60 minutos, para fixar a linha de base de p50/p95/p99.
3. **Soak** por horas no mesmo nível: vazamentos de memória, crescimento de filas, pausas de GC viram jitter visível só com tempo.
4. **Spike**: todos os clientes reconectando ao mesmo tempo após uma queda simulada é o pico mais realista de um sistema de tempo real; é aqui que backoff com jitter (ver `rtm.rel.reconnection`) é testado.
5. **Breakpoint**: aumentar conexões ou mensagens/s até o tempo por tick ultrapassar o orçamento; registrar o ponto e o modo de falha.

### Sintético versus realista

[I] Cliente sintético (envia N mensagens/s fixas, ignora o que recebe) mede a capacidade bruta do servidor de aceitar e distribuir; é barato e reproduzível. Cliente realista (reage ao estado, respeita turnos, entra e sai de salas, reconecta) mede o que importa para o produto, mas acopla o teste ao protocolo e exige manutenção. Usar sintético para breakpoint e regressão; realista para average, soak e spike. Em ambos, o padrão de *fan-out* (uma mensagem de entrada gera N de saída numa sala de N) é a variável dominante; testar com o tamanho real de sala.

### Limites do sistema operacional

Cada conexão consome um descritor de arquivo no gerador e no servidor. O `getrlimit(2)` define `RLIMIT_NOFILE` como "a value one greater than the maximum file descriptor number that can be opened by this process"; exceder faz `open`, `pipe` e `dup` falharem com `EMFILE`; há limite *soft* (o que o kernel aplica) e *hard* (teto que só processo privilegiado eleva) [F: man7getrlimit]. A documentação do k6 relata no exemplo Linux soft de 1024 e hard de 1048576, orienta `ulimit -n` e `/etc/security/limits.conf`, dimensiona o valor como VUs × requisições por iteração, e observa que o sintoma típico é "too many open files" [F: k62026finetune].

Conexões de saída consomem portas efêmeras por destino. A documentação do kernel Linux define `ip_local_port_range` como "the local port range that is used by TCP and UDP to choose the local port", com padrão "32768 and 60999" [F: kernel2026ipsysctl]; o k6 calcula 28.231 portas e sugere ampliar com `sysctl -w net.ipv4.ip_local_port_range="16384 65000"`, notando que a faixa vale para TCP e UDP; no macOS o padrão é 49152 a 65535 [F: k62026finetune]. A RFC 6056 recomenda que algoritmos de seleção "should use the whole range 1024-65535", contra a faixa dinâmica da IANA de 49152 a 65535 [F: rfc6056, §2.1, §3.2]. Conexões TCP fechadas ficam em TIME_WAIT "typically configured between 15 seconds and 2 minutes" antes de a porta poder ser reutilizada; o k6 prefere espalhar o alvo por várias portas ou IPs, com `tcp_tw_reuse` como último recurso [F: k62026finetune]. O backlog de `listen()` é limitado por `somaxconn`, padrão 4096 (128 antes do Linux 5.4) [F: kernel2026ipsysctl], relevante para picos de conexão no servidor [I].

[I] Consequência prática: um único gerador atinge no máximo alguns milhares de conexões simultâneas por IP de destino; testes de dezenas de milhares exigem geradores distribuídos ou múltiplos IPs e portas no servidor, e o próprio servidor precisa do mesmo ajuste de descritores.

## Requisitos e pressupostos

- Ambiente de teste isolado ou com interest management idêntico ao de produção; fan-out é o que escala.
- Geradores com rede e CPU sobrando; se o gerador satura, as medidas são do gerador. O k6 estima 1 a 5 MB de RAM por VU [F: k62026finetune].
- Relógios dos geradores e do servidor alinhados o bastante para correlacionar eventos (ver `rtm.net.clock-synchronization`).

## Vantagens e limitações

- Ferramentas de WebSocket maduras tornam barato testar frameworks como Nakama e Colyseus, que usam WebSocket (ver `rtm.fw.comparison`); UDP próprio exige gerador próprio.
- Checks bloqueantes (Gatling) e `connect` bloqueante (k6/ws) moldam o script em torno de pares requisição-resposta, que não é o padrão de tempo real (fluxo contínuo); o `k6/websockets` com event loop é mais adequado [F: k62026ws] [I].
- Teste de carga mede capacidade; não mede experiência sob rede ruim; combinar com `rtm.perf.network-emulation`.

## Alternativas e comparações

Ver tabela de ferramentas acima. Critério de escolha [I]: k6 ou Artillery para WebSocket e Socket.IO com scripts simples; Gatling onde já há investimento em JVM; Locust quando o protocolo exige biblioteca Python própria; cliente headless do próprio sistema para UDP.

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`. Critérios de aceite típicos [I]: p99 do RTT de aplicação abaixo do limiar da classe de interação (ver `rtm.perf.qoe-thresholds`) no nível average; tempo por tick p99 abaixo de 80% do orçamento; zero crescimento monotônico de memória e de fila em soak; recuperação completa após spike dentro de N segundos.

## Exemplo técnico independente de domínio

```text
# Esqueleto de cliente realista (pseudocodigo, estilo k6/websockets)
scenario: stages = [ramp 0->N em 5 min, plateau N por 30 min, ramp N->0 em 2 min]
vu():
    token = http.post(AUTH, {device_id}).token
    ws = connect(WSS_URL, headers = {Authorization: "Bearer " + token})
    ws.on(open):  ws.send(JOIN, {room = pick_room()}) ; every(2 s): ws.send(PING, {t0 = now()})
    ws.on(message, m):
        if m.type == PONG: trend_rtt.add(now() - m.t0)
        if m.type == STATE: counter_state.add(1) ; check_seq(m.seq)
        if m.type == YOUR_TURN or game.is_realtime: ws.send(INPUT, cadence(game))
    ws.on(close, code): counter_close[code].add(1)
    sleep(session_length())
thresholds: trend_rtt p(99) < BUDGET_MS ; counter_close[1006] rate < 0.01
# No servidor: hist_tick p99 < 0.8 * tick_budget ; gauge_outq max < outgoing_queue_size
```

## Relações com outros conceitos

Depende de `rtm.perf.metrics` e de `rtm.proto.websocket`. Complementa `rtm.perf.network-emulation` (rede ruim sob carga), `rtm.rel.fault-tolerance` (experimentos de falha sob carga) e `rtm.mp.rooms-and-matches` (fan-out por sala). Relaciona-se a `rtm.proto.udp`, `rtm.proto.tcp` e `rtm.fw.comparison`. Avaliado por `rtm.perf.metrics`.

## Lacunas e questões abertas

- Extensões de k6 para UDP e o módulo `k6/websockets`: só a menção na página de `k6/ws` foi lida; a página do módulo novo não foi aberta.
- Versões das ferramentas não estão explícitas nas páginas consultadas ("latest"); registrar a versão ao reproduzir.
- Não há, nas fontes consultadas, números de referência de conexões por nó para Nakama ou Colyseus; precisam ser medidos.
- Locust `SocketIOUser`: experimental segundo a própria documentação [F: locust2026other].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| k62026ws | fornecedor | 2026-10-29 |
| k62026metrics | fornecedor | 2026-10-29 |
| k62026testtypes | fornecedor | 2026-10-29 |
| k62026finetune | fornecedor | 2026-10-29 |
| artillery2026ws | fornecedor | 2026-10-29 |
| artillery2026socketio | fornecedor | 2026-10-29 |
| locust2026other | fornecedor | 2026-10-29 |
| gatling2026ws | fornecedor | 2026-10-29 |
| man7getrlimit | tecnico | 2026-10-29 |
| kernel2026ipsysctl | tecnico | 2026-10-29 |
| rfc6056 | normativo | 2026-10-29 |
| google2016sre | tecnico | 2026-10-29 |
