---
id: rtm.rt.communication-patterns
titulo: Padrões de comunicação em tempo real (polling, long polling, push, pub/sub, streaming, request/response)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc6202, rfc6455, whatwg2026sse, oasis2019mqtt, grpc2026concepts, rfc9114, rfc9000, rfc9221, rfc8831, fiedler2008udp, fiedler2015state, gambetta2014client]
relacoes:
  - { tipo: complementa, alvo: rtm.rt.realtime-systems }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
  - { tipo: implementado-por, alvo: rtm.proto.websocket }
  - { tipo: implementado-por, alvo: rtm.proto.http-streaming }
  - { tipo: implementado-por, alvo: rtm.proto.webtransport }
  - { tipo: implementado-por, alvo: rtm.proto.webrtc }
  - { tipo: relacionado-a, alvo: rtm.arch.event-driven }
  - { tipo: relacionado-a, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
termos: [polling, long polling, push, publish/subscribe, streaming, request/response, server-sent events, tópico, QoS de entrega]
---

# Padrões de comunicação em tempo real

## Definição e terminologia

Padrões de comunicação descrevem **quem inicia** a troca, **quantas mensagens** fluem por iniciativa e **como o canal é mantido**. Os seis padrões tratados aqui [I]:

| Padrão | Iniciador | Cardinalidade | Canal |
|---|---|---|---|
| request/response | cliente | 1 pedido, 1 resposta | efêmero ou reutilizado |
| polling | cliente, periódico | 1:1 repetido | efêmero |
| long polling | cliente; servidor segura a resposta | 1:1 com espera | efêmero, reaberto a cada evento |
| push / streaming | servidor, após abertura pelo cliente | 1:N mensagens | persistente |
| pub/sub | produtor publica, intermediário distribui | 1:N por tópico | persistente, desacoplado |
| mensagens bidirecionais | ambos | N:M | persistente |

O RFC 6202 define **long polling** como responder a uma requisição "only when a particular event, status, or timeout has occurred" e **HTTP streaming** como manter a requisição aberta indefinidamente, nunca terminando a resposta mesmo após enviar dados [F: rfc6202, §2.1 e §3.1]. **Server-Sent Events** (SSE) é a formalização de streaming unidirecional servidor→página no padrão HTML, com tipo `text/event-stream` [F: whatwg2026sse]. O RFC 6455 define o WebSocket como protocolo independente sobre TCP, concebido para "supersede existing bidirectional communication technologies that use HTTP as a transport layer" [F: rfc6455, §1.1 e §1.7]. A especificação MQTT define **publish/subscribe** como distribuição um-para-muitos com "decoupling of applications", em que um servidor atua como "intermediary between Clients which publish Application Messages" e os entrega por **tópico** [F: oasis2019mqtt, Abstract e §1.2].

## Problema que resolve

O padrão escolhido determina o **atraso mínimo entre um evento no servidor e sua observação pelo cliente**, o **custo por mensagem** e o **número de conexões**. O RFC 6455 enumera os problemas do uso de HTTP para comunicação bidirecional: o servidor é forçado a manter várias conexões TCP por cliente, "the wire protocol has a high overhead, with each client-to-server message having an HTTP header", e o script precisa mapear respostas a requisições [F: rfc6455, §1.1].

## Fundamentos e funcionamento

### Polling e long polling

Polling periódico tem atraso médio de meio intervalo mais a ida e volta, e custo fixo por consulta mesmo sem novidades [I]. Long polling elimina o custo de consultas vazias, mas o RFC 6202 registra que "every long poll request and long poll response is a complete HTTP message", de modo que, para mensagens pequenas e raras, os cabeçalhos podem dominar o volume, e que "the maximal latency is over three network transits" (resposta, nova requisição, nova resposta) [F: rfc6202, §2.2]. O RFC recomenda limitar o número de long polls por cliente, idealmente um compartilhado entre abas, timeouts na faixa de 30 s ("generally 30 seconds is a safer value") e `Cache-Control: no-cache` [F: rfc6202, §5.1, §5.5, §5.6].

### Streaming e push

Streaming HTTP mantém a resposta aberta; o RFC 6202 alerta que intermediários que bufferizam respostas parciais quebram o padrão ("HTTP streaming will not work with such intermediaries") e que a delimitação de mensagens "needs to be performed at the application level", pois proxies podem re-fragmentar chunks [F: rfc6202, §3.2]. SSE padroniza isso: eventos separados por linha em branco, campos `data:`, `event:`, `id:` e `retry:`; o cliente reconecta automaticamente e envia o cabeçalho `Last-Event-ID` para retomar [F: whatwg2026sse]. O padrão HTML observa que proxies legados derrubam conexões ociosas e sugere comentários periódicos (cerca de 15 s) como keep-alive [F: whatwg2026sse].

### Mensagens bidirecionais

WebSocket adiciona um mecanismo de framing sobre TCP ("layers a framing mechanism on top of TCP") e usa uma única conexão para os dois sentidos [F: rfc6455, §1.5, §1.1]. Sobre QUIC, HTTP/3 usa streams independentes: "one stream that is blocked or suffers packet loss does not prevent progress on other streams" [F: rfc9114, §2]; a extensão DATAGRAM do QUIC oferece entrega sem retransmissão, útil para "audio/video streaming applications, gaming applications" [F: rfc9221, §1-2]. Canais de dados WebRTC oferecem, por mensagem, entrega confiável ou não e ordenada ou não [F: rfc8831, §6.4].

### Pub/sub e semântica de entrega

MQTT define três níveis de QoS: 0 "At most once", 1 "At least once" (pode duplicar), 2 "Exactly once" [F: oasis2019mqtt, Abstract]; e um **keep alive** em que o servidor fecha a conexão se nada chegar em 1,5 vezes o intervalo [F: oasis2019mqtt, §3.1.2.10]. [I] Esses níveis são o vocabulário padrão para a semântica de entrega (ver `rtm.rel.delivery-semantics`).

### Streaming em RPC

A documentação do gRPC define quatro tipos de chamada: unária, streaming do servidor, streaming do cliente e bidirecional, com a garantia de que "gRPC guarantees message ordering within an individual RPC call" e, no modo bidirecional, "the two streams operate independently" [F: grpc2026concepts].

## Requisitos e pressupostos

- Push e streaming pressupõem conexão persistente e infraestrutura (proxies, balanceadores) que a tolere [F: rfc6202, §3.2, §5.5].
- Pub/sub pressupõe um intermediário com estado de assinaturas; o desacoplamento vem ao custo desse componente [F: oasis2019mqtt, §1.2].
- Para jogos de ação, Fiedler argumenta que "the game only cares about the most recent data", o que favorece mensagens não confiáveis e não ordenadas em vez de qualquer padrão sobre TCP [F: fiedler2008udp].

## Vantagens e limitações

| Padrão | Vantagens | Limitações |
|---|---|---|
| polling | simples, cacheável, sem estado no servidor | atraso médio de meio intervalo; custo sem novidades [I] |
| long polling | baixo custo ocioso; atravessa proxies | >3 trânsitos de latência máxima; cabeçalhos completos [F: rfc6202, §2.2] |
| streaming/SSE | atraso de um trânsito; reconexão padronizada | unidirecional; proxies bufferizantes [F: rfc6202, §3.2; whatwg2026sse] |
| WebSocket | bidirecional, framing leve | sobre TCP: bloqueio de cabeça de fila (ver `rtm.net.ordering-and-reliability`) [F: fiedler2008udp] |
| pub/sub | desacoplamento 1:N, QoS explícita | broker como ponto de passagem; QoS 2 custa handshakes [F: oasis2019mqtt] |
| datagramas (QUIC/WebRTC) | sem retransmissão, sem ordenação forçada | aplicação precisa lidar com perda [F: rfc9221, §5.2; rfc8831] |

## Alternativas e comparações

Quando cada um se aplica [I], com base nas propriedades acima:

- **request/response** e **polling**: estado que muda raramente, consultas idempotentes, cache útil.
- **long polling**: notificações esparsas em ambientes onde só HTTP/1.1 atravessa; o RFC 6202 o trata como fallback de compatibilidade.
- **SSE/streaming**: feed unidirecional (placar, presença, notificações) com reconexão automática.
- **WebSocket / WebTransport streams**: salas, chat, jogos por turno, colaboração com ordenação por canal.
- **pub/sub**: fan-out para muitos assinantes por tópico, com ou sem broker dedicado.
- **datagramas**: estado de jogo rápido em que a última amostra substitui as anteriores [F: fiedler2008udp; fiedler2015state].

## Métricas e métodos de avaliação

Atraso evento→observação (em trânsitos de rede), bytes por mensagem incluindo cabeçalhos, conexões por cliente e por servidor, taxa de reconexões. O RFC 6202 oferece a contagem de trânsitos como métrica comparativa [F: rfc6202, §2.2, §3.2].

## Exemplo técnico independente de domínio

Atraso evento→cliente, por padrão, em trânsitos de rede (T = um trânsito unidirecional) [I]:

```
polling (intervalo P):   espera média P/2 + 2T
long polling:            T (resposta) ... depois 2T para rearmar; pior caso ~3T [F: rfc6202 §2.2]
streaming/SSE/WebSocket: T
pub/sub via broker:      T (produtor->broker) + T (broker->assinante) = 2T
```

Esqueleto de um feed SSE:

```
GET /feed            -> 200 OK, Content-Type: text/event-stream
id: 41
event: estado
data: {"v": 41, ...}
                     (linha em branco despacha o evento)
: keep-alive         (comentário a cada ~15 s)
```

Na reconexão o cliente envia `Last-Event-ID: 41` e o servidor retoma a partir do evento 42 [F: whatwg2026sse].

## Relações com outros conceitos

Complementa `rtm.rt.realtime-systems` (o padrão define o atraso mínimo alcançável); depende de `rtm.net.latency` e `rtm.net.bandwidth` (trânsitos e cabeçalhos são os custos); é implementado pelos protocolos `rtm.proto.websocket`, `rtm.proto.http-streaming`, `rtm.proto.webtransport` e `rtm.proto.webrtc`; relaciona-se a `rtm.arch.event-driven`, `rtm.mp.presence` e `rtm.rel.delivery-semantics`.

## Lacunas e questões abertas

- Não foi localizada fonte normativa que defina "push" de forma genérica; o termo é usado pelo padrão HTML para SSE.
- A comparação quantitativa de overhead por mensagem entre WebSocket, SSE e long polling não foi medida aqui; o RFC 6202 e o RFC 6455 trazem apenas argumentos qualitativos.
- O artigo de Eugster et al. (2003), "The many faces of publish/subscribe", não foi aberto (acesso bloqueado); a definição de pub/sub foi tomada da especificação MQTT.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc6202 | normativo (informativo) | 2026-10-29 |
| rfc6455 | normativo | 2026-10-29 |
| whatwg2026sse | normativo | 2026-10-29 |
| oasis2019mqtt | normativo | 2026-10-29 |
| grpc2026concepts | fornecedor | 2026-10-29 |
| rfc9114 | normativo | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| rfc9221 | normativo | 2026-10-29 |
| rfc8831 | normativo | 2026-10-29 |
| fiedler2008udp | tecnico | 2026-10-29 |
| fiedler2015state | tecnico | 2026-10-29 |
| gambetta2014client | tecnico | 2026-10-29 |
