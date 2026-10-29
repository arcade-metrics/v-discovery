---
id: rtm.rel.reconnection
titulo: Reconexão e retomada de sessão
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc6455, rfc9000, brooker2015backoff, brooker2019timeouts, heroiclabs2026sockets, heroiclabs2026configuration, heroiclabs2026authoritative, heroiclabs2026session, colyseus2026reconnection, colyseus2026connection, colyseus2026room]
relacoes:
  - { tipo: depende-de, alvo: rtm.proto.websocket }
  - { tipo: depende-de, alvo: rtm.mp.session-lifecycle }
  - { tipo: complementa, alvo: rtm.rel.delivery-semantics }
  - { tipo: complementa, alvo: rtm.rel.fault-tolerance }
  - { tipo: complementa, alvo: rtm.sec.authentication }
  - { tipo: complementa, alvo: rtm.mp.presence }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.proto.quic }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [heartbeat, ping/pong, backoff exponencial, jitter de backoff, token de reconexão, janela de graça, replay de mensagens, connection migration]
---

# Reconexão e retomada de sessão

## Definição e terminologia

Reconexão é o conjunto de mecanismos pelos quais um cliente que perdeu a conexão de transporte com o servidor de tempo real (a) detecta a perda, (b) restabelece um canal e (c) retoma a sessão lógica (sala, partida, presença, estado) com a menor perda possível de contexto. Distingue-se de *autenticação* (quem é o cliente, ver `rtm.sec.authentication`) e de *tolerância a falhas do servidor* (o que acontece quando é o servidor que cai, ver `rtm.rel.fault-tolerance`), embora as três se combinem.

Termos usados aqui:

- **Heartbeat**: mensagem periódica cuja ausência sinaliza queda. No WebSocket, os quadros de controle Ping e Pong cumprem esse papel [F: rfc6455, §5.5.2-5.5.3].
- **Backoff exponencial com jitter**: política de espera entre tentativas de reconexão que cresce geometricamente e é aleatorizada para evitar sincronização de clientes [F: brooker2015backoff].
- **Token de reconexão**: credencial de curta duração, emitida pelo servidor, que identifica a sessão lógica a ser retomada (e não apenas o usuário). Colyseus expõe esse conceito literalmente como `room.reconnectionToken` [F: colyseus2026reconnection].
- **Janela de graça**: intervalo durante o qual o servidor preserva a vaga e o estado do cliente desconectado antes de tratá-lo como saída definitiva.
- **Replay de mensagens**: reenvio, após reconexão, das mensagens que o cliente não recebeu, identificadas por números de sequência.

## Problema que resolve

Conexões de longa duração caem por motivos fora do controle da aplicação: troca de rede em dispositivos móveis, suspensão do processo em segundo plano, timeouts de NAT e proxies, falha de um nó intermediário. Sem tratamento explícito, uma queda de poucos segundos vira, para o usuário, perda da partida ou da sessão de colaboração. O objetivo é tornar a queda um evento recuperável e, quando possível, invisível.

## Fundamentos e funcionamento

### Detecção de queda

Uma conexão TCP ociosa pode permanecer "aberta" do ponto de vista do sistema operacional por muito tempo depois que o caminho de rede deixou de funcionar; por isso, protocolos de aplicação acrescentam sinais próprios de vida [I].

A RFC 6455 define que, ao receber um quadro Ping, o endpoint "MUST send a Pong frame in response, unless it already received a Close frame", e observa que um Ping "may serve either as a keepalive or as a means to verify that the remote endpoint is still responsive" [F: rfc6455, §5.5.2]. A RFC também permite um Pong não solicitado, que funciona como "a unidirectional heartbeat" sem resposta esperada [F: rfc6455, §5.5.3]. Um detalhe prático: a API WebSocket dos navegadores não expõe Ping/Pong ao código JavaScript, de modo que aplicações web costumam implementar heartbeat em nível de mensagem [I].

No QUIC, a RFC 9000 define um *idle timeout* negociado pelo parâmetro `max_idle_timeout`, cujo valor efetivo "is computed as the minimum of the two advertised values"; quando ocioso além disso, "the connection is silently closed and its state is discarded" [F: rfc9000, §10.1]. Para testar vida, "An endpoint can send a PING or another ack-eliciting frame to test the connection for liveness" [F: rfc9000, §10.1.1].

Em frameworks, os parâmetros de heartbeat são configuração de servidor. A documentação de configuração do Nakama lista `socket.ping_period_ms` (padrão 15000 ms, intervalo entre pings ao cliente), `socket.pong_wait_ms` (padrão 25000 ms, espera pelo pong) e `socket.ping_backoff_threshold` (padrão 20 mensagens: se o cliente enviou pelo menos esse número de mensagens no período, o próximo ping é adiado) [F: heroiclabs2026configuration]. A página de sockets do Nakama afirma que "The server can also close a connection on its own when the client stops answering the heartbeat, which usually means long blocking work on the client stalled its network loop" [F: heroiclabs2026sockets]. [I] Isso significa que a latência de detecção do lado do servidor é da ordem de `ping_period + pong_wait` no pior caso, o que importa para a janela de graça.

### Política de nova tentativa

A própria RFC 6455 traz orientação para reconexão após fechamento anormal: "The first reconnect attempt SHOULD be delayed by a random amount of time", sugerindo "a value chosen randomly between 0 and 5 seconds" como atraso inicial razoável, e que tentativas subsequentes "SHOULD be delayed by increasingly longer amounts of time, using a method such as truncated binary exponential backoff" [F: rfc6455, §7.2.3]. A justificativa é evitar que todos os clientes de um servidor que caiu tentem reconectar no mesmo instante [I].

O artigo de Marc Brooker no AWS Architecture Blog (2015) simula clientes em contenção e compara backoff exponencial puro com três variantes com jitter. O autor relata que o backoff sem jitter "was the clear loser"; que, entre as variantes, *Full Jitter* fez menos trabalho total e *Decorrelated Jitter* terminou um pouco mais rápido; e conclui que backoff com jitter "should be considered a standard approach for remote clients" [F: brooker2015backoff]. As fórmulas no artigo estão em imagens sem texto alternativo; a descrição em prosa é: exponencial multiplica a espera por uma constante até um teto; Full Jitter sorteia uniformemente entre zero e o valor exponencial; Equal Jitter mantém metade fixa e sorteia a outra metade; Decorrelated Jitter faz o máximo do sorteio depender do valor anterior [F: brooker2015backoff]. O texto posterior do mesmo autor na AWS Builders' Library acrescenta: "Jitter adds some amount of randomness to the backoff to spread the retries around in time", recomenda limitar o backoff (capped exponential backoff), retentar "at a single point in the stack" e aplicar jitter também a timers e trabalho periódico [F: brooker2019timeouts].

A documentação do Colyseus mostra uma implementação concreta: a reconexão automática do SDK usa backoff exponencial com `minDelay` 100 ms, `maxDelay` 5000 ms, `maxRetries` 15 e exige `minUptime` de 5000 ms de conexão prévia para disparar; o backoff é substituível por função própria [F: colyseus2026connection].

### Retomada da sessão lógica

Reconectar o transporte não basta: a sessão lógica (sala, posição na partida, presença) precisa ser reencontrada. Há três camadas:

1. **Credencial**. O token de autenticação do usuário pode ter expirado durante a queda. No Nakama, o token de sessão é um JWT com `session.token_expiry_sec` padrão de 60 s, e um refresh token com padrão de 3600 s, renovável sem reautenticar [F: heroiclabs2026session]. Ver `rtm.sec.authentication`.
2. **Identificador da sessão lógica**. No Colyseus, `room.reconnectionToken` é "refreshed on every successful connection" e deve ser persistido pelo cliente; `client.reconnect(token)` só funciona se o servidor ainda mantém a vaga [F: colyseus2026reconnection]. No Nakama não há token de reconexão de partida documentado; o padrão documentado é rejoin pelo `matchId` via `socket.joinMatch(matchId)` [F: heroiclabs2026sockets], e o handler autoritativo recebe em `match_leave` "whether the player left the match or disconnected", com a observação "In the case of disconnects you can decide to temporarily reserve their seat" [F: heroiclabs2026authoritative].
3. **Estado perdido**. Dois modelos: enviar snapshot completo (Colyseus: "After a successful reconnection, the server sends a full state snapshot" e o SDK o reconcilia na árvore existente [F: colyseus2026reconnection]); ou reenviar apenas as mensagens perdidas, o que exige números de sequência por conexão e um buffer de saída no servidor (ver `rtm.rel.delivery-semantics`). [I] Snapshot é mais simples e robusto; replay por sequência preserva eventos transitórios (chat, efeitos) que um snapshot de estado não contém.

### Janela de graça

A janela de graça é implementada pelo servidor que, ao detectar a queda não consentida, reserva a vaga por um tempo. No Colyseus, `onDrop()` é chamado "on every non-consented disconnection" e `this.allowReconnection(client, 30)` segura a vaga por 30 s; o modo `"manual"` segura até rejeição explícita (`reconnection.reject()`); um `room.leave()` consentido usa o close code `CONSENTED` (4000) e pula `onDrop()` [F: colyseus2026reconnection]. A documentação recomenda não remover os dados do jogador em `onDrop()`, mas marcar algo como `player.connected = false`, e remover só em `onLeave()` [F: colyseus2026reconnection]. Mensagens enviadas pelo cliente durante a desconexão ficam enfileiradas ("`room.send()` calls will be queued", limite `maxEnqueuedMessages` 10) [F: colyseus2026connection].

### Mudança de rede em dispositivos móveis

Com TCP e WebSocket, uma troca de interface (Wi-Fi para celular) muda o endereço IP e invalida a conexão; a aplicação precisa reconectar do zero. O QUIC foi desenhado para o contraste: "The use of a connection ID allows connections to survive changes to endpoint addresses (IP address and port)" [F: rfc9000, §9]; "Only clients are able to migrate in this version of QUIC" [F: rfc9000, §1]; "An endpoint can migrate a connection to a new local address by sending packets containing non-probing frames" [F: rfc9000, §9.2], após validação de caminho, em que "Failure of path validation simply means that the new path is not usable for this connection" [F: rfc9000, §9.1]. A migração é proibida antes de o handshake ser confirmado [F: rfc9000, §9]. Servidores podem desabilitá-la com `disable_active_migration` [F: rfc9000, §5.2.3]. [I] Para aplicações em navegador, isso só está disponível via WebTransport (ver `rtm.proto.webtransport`); com WebSocket, a reconexão em camada de aplicação continua necessária.

## Requisitos e pressupostos

- O servidor precisa manter estado da sessão lógica por pelo menos a janela de graça; sessões sem estado no servidor não têm o que retomar.
- O cliente precisa persistir localmente a credencial e o identificador da sessão lógica (token de reconexão ou id da sala) em armazenamento que sobreviva a recarga de página ou troca de app.
- Para replay por sequência, cada mensagem servidor para cliente precisa de número monotônico por conexão lógica, e o servidor precisa de buffer limitado por cliente.
- Heartbeat agressivo custa bateria e tráfego em móveis; o intervalo é um compromisso com a latência de detecção [I].

## Vantagens e limitações

- Reconexão com janela de graça converte quedas curtas em pausas; sem ela, cada queda é uma saída.
- A janela de graça tem custo: vagas reservadas por jogadores que não voltam bloqueiam salas e exigem política de expiração (o padrão de 30 s do exemplo do Colyseus é ilustrativo, não normativo [I]).
- Replay por sequência tem custo de memória por cliente e exige limite; acima do limite, cai-se para snapshot.
- Reconexão automática pode mascarar problemas de rede e inflar métricas de "sessões ativas" se não for instrumentada (ver `rtm.perf.metrics`: tempo de reconexão, taxa de reconexões por sessão).

## Alternativas e comparações

| Abordagem | Detecção | Retomada | Mudança de rede |
|---|---|---|---|
| WebSocket + heartbeat de aplicação | Ping/Pong [F: rfc6455] ou mensagem própria | token de reconexão + snapshot ou replay | reconexão completa |
| QUIC / WebTransport | idle timeout + PING [F: rfc9000, §10.1] | migração mantém a mesma conexão [F: rfc9000, §9] | nativa, só pelo cliente |
| Colyseus (0.17+) | não documentado na página consultada | automática com backoff; `reconnectionToken`; snapshot completo [F: colyseus2026connection] | reconexão completa |
| Nakama | ping/pong configurável no servidor [F: heroiclabs2026configuration] | rejoin por `matchId`; reserva de vaga a cargo do handler [F: heroiclabs2026authoritative] | reconexão completa |

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`: tempo de detecção de queda, tempo de reconexão (do evento de fechamento até a sessão retomada), taxa de reconexões por sessão e por minuto, fração de reconexões que falham dentro da janela de graça, tamanho do buffer de replay. Em `rtm.perf.network-emulation`, cenários de queda total e de troca de rede são os que exercitam esta técnica.

## Exemplo técnico independente de domínio

```text
# Cliente: laço de reconexão com Full Jitter (descrição em prosa de brooker2015backoff)
base = 0.5 s ; cap = 30 s ; attempt = 0
loop:
    try: conn = open(url, headers={auth: token})
         send(RESUME, {session_id, last_seq_received})
         attempt = 0 ; return conn
    catch: sleep(random_uniform(0, min(cap, base * 2^attempt))) ; attempt += 1

# Servidor: tratamento de queda e retomada
on_disconnect(client, consented):
    if consented: remove(client) ; return
    client.connected = false ; reserve_seat(client, grace = 30 s)
on_resume(conn, session_id, last_seq):
    c = find_reserved(session_id) ; if none: reject("expired")
    if last_seq >= c.outbox.oldest_seq: replay(c.outbox.after(last_seq))
    else: send_full_snapshot(c)
    c.connected = true ; attach(conn, c)
```

## Relações com outros conceitos

Depende do transporte (`rtm.proto.websocket`) e do ciclo de vida de sessão (`rtm.mp.session-lifecycle`). Complementa `rtm.rel.delivery-semantics` (replay exige deduplicação e sequência), `rtm.rel.fault-tolerance` (queda do servidor é o caso simétrico) e `rtm.sec.authentication` (renovação de credencial durante a queda). Implementado por `rtm.fw.nakama` e `rtm.fw.colyseus` com modelos distintos. `rtm.proto.quic` é o contraste para mudança de rede. Avaliado por `rtm.perf.metrics`.

## Lacunas e questões abertas

- A documentação do Nakama consultada não descreve um fluxo de reconexão de partida de ponta a ponta nem o formato da URL do socket; o rejoin por `matchId` e a reserva de vaga são descritos apenas como possibilidades do handler. Não verificado: se o servidor reenvia estado perdido automaticamente em algum modo.
- A página de reconexão do Colyseus não documenta o mecanismo de heartbeat; não verificado como o SDK detecta a queda que dispara `onDrop`.
- Não há, nas fontes consultadas, evidência empírica sobre duração ideal da janela de graça por tipo de interação; os 30 s são exemplo de documentação.
- As fórmulas do artigo da AWS só estão em imagens; a descrição aqui é a prosa do artigo.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc6455 | normativo | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| brooker2015backoff | tecnico | 2026-10-29 |
| brooker2019timeouts | tecnico | 2026-10-29 |
| heroiclabs2026sockets | fornecedor | 2026-10-29 |
| heroiclabs2026configuration | fornecedor | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| heroiclabs2026session | fornecedor | 2026-10-29 |
| colyseus2026reconnection | fornecedor | 2026-10-29 |
| colyseus2026connection | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
