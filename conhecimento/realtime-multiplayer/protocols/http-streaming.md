---
id: rtm.proto.http-streaming
titulo: Long polling, Server-Sent Events e streaming HTTP
tipo: protocolo
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc6202, whatwg2026html, whatwg2026fetch, rfc9112, rfc9113, rfc9114, rfc6455, caniuse2026eventsource]
relacoes:
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: depende-de, alvo: rtm.proto.tcp }
  - { tipo: alternativa-a, alvo: rtm.proto.websocket }
  - { tipo: alternativa-a, alvo: rtm.proto.webtransport }
  - { tipo: complementa, alvo: rtm.arch.event-driven }
  - { tipo: relacionado-a, alvo: rtm.rt.communication-patterns }
  - { tipo: relacionado-a, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.mp.turn-based }
termos: [long polling, HTTP streaming, Server-Sent Events, EventSource, text/event-stream, Last-Event-ID, chunked transfer coding]
---

# Long polling, Server-Sent Events e streaming HTTP

## Definição e terminologia

Família de técnicas que obtêm comunicação quase em tempo real do servidor para o cliente usando apenas requisições e respostas HTTP. A RFC 6202 (Informational, abril de 2011) documenta problemas e práticas de long polling e streaming em HTTP bidirecional [F: rfc6202]. Server-Sent Events (SSE) é a padronização de streaming unidirecional no HTML Living Standard do WHATWG, seção 9.2, atualizado em 26 de outubro de 2026 [F: whatwg2026html, §9.2].

- **long polling**: o servidor segura a requisição aberta e só responde quando há evento, mudança de estado ou timeout; o cliente então reenvia [F: rfc6202, §2.1].
- **HTTP streaming**: o servidor mantém a requisição aberta indefinidamente e envia várias peças de dados na mesma resposta, sem encerrá-la [F: rfc6202, §3.1].
- **SSE / EventSource**: API de navegador que consome um stream `text/event-stream` com reconexão automática [F: whatwg2026html, §9.2].
- **chunked transfer coding**: codificação HTTP/1.1 que permite enviar conteúdo de tamanho desconhecido em pedaços delimitados por tamanho, mantendo a conexão persistente [F: rfc9112, §7.1].

O que não é: nenhuma dessas técnicas é bidirecional num único canal; o caminho cliente-para-servidor usa requisições HTTP normais [F: whatwg2026html, §9.2] [I].

## Problema que resolve

Entregar eventos do servidor ao navegador sem WebSocket, usando infraestrutura HTTP comum (proxies, CDNs, autenticação por cookie), para casos em que a frequência de eventos é baixa a moderada e a direção dominante é servidor-para-cliente [I].

## Fundamentos e funcionamento

**Long polling (RFC 6202).** Problemas listados: overhead de cabeçalhos a cada mensagem; latência máxima de mais de três trânsitos de rede, mais com retransmissão TCP; cada cliente segura uma conexão TCP e uma requisição; degradação por batching sob carga; timeouts e caching [F: rfc6202, §2.2]. Recomendações: limitar a uma requisição long poll por navegador, compartilhada entre abas; timeouts altos mas não demais, com 30 s descrito como mais seguro e até 120 s em experimentos; `Cache-Control: no-cache` [F: rfc6202, §5.1, §5.5, §5.6].

**HTTP streaming (RFC 6202).** Pode usar chunked transfer em HTTP/1.1 [F: rfc6202, §3.1]. Problemas: intermediários podem bufferizar a resposta inteira; navegadores podem forçar reconexão periódica para limitar memória; clientes não são obrigados a processar respostas parciais; o framing de mensagens deve ser feito pela aplicação, pois proxies podem re-chunkar [F: rfc6202, §3.2]. A RFC 9112 (HTTP/1.1, STD 99, Internet Standard) define chunked: cada chunk inicia com tamanho em hexadecimal, chunk de tamanho zero encerra, trailers opcionais [F: rfc9112, §7.1, §7.1.2].

**Server-Sent Events (WHATWG HTML §9.2).** `new EventSource(url, {withCredentials})`; `readyState` CONNECTING 0, OPEN 1, CLOSED 2; eventos `open`, `message`, `error`; `close()` aborta o fetch [F: whatwg2026html, §9.2]. Formato: MIME `text/event-stream`, decodificado obrigatoriamente como UTF-8; linhas terminam em CRLF, LF ou CR; linha em branco despacha o evento; campos `event`, `data`, `id`, `retry`; linhas iniciadas por dois-pontos são comentários [F: whatwg2026html, §9.2]. Reconexão: o cliente reconecta após o fechamento; resposta 204 instrui a parar; na reconexão envia o cabeçalho `Last-Event-ID` se houver id; status diferente de 200, Content-Type errado ou erro fatal de rede impedem reconexão; implementações podem aplicar backoff [F: whatwg2026html, §9.2]. O padrão observa que chunking feito por outra camada pode prejudicar a confiabilidade e que pode ser desativado para event streams; que proxies legados podem derrubar conexões ociosas, sugerindo um comentário a cada cerca de 15 segundos; e que o modo de cache é "no-store" [F: whatwg2026html, §9.2]. Sobre limites de conexões: clientes sujeitos ao limite por servidor do HTTP podem ter problemas quando várias páginas abrem event streams ao mesmo domínio; mitigações incluem domínios únicos por conexão ou um EventSource compartilhado via shared worker [F: whatwg2026html, §9.2].

**Fetch com corpo em stream.** No Fetch Standard (Living Standard, 19 de outubro de 2026), um body é "A stream (a `ReadableStream` object)", o que permite consumir respostas progressivamente sem EventSource; requisições com ReadableStream exigem preflight CORS [F: whatwg2026fetch, §2.2.4, §2.2.5].

**HTTP/2 e HTTP/3.** Sobre HTTP/2 a multiplexação de streams numa conexão TCP remove o limite de conexões por host do HTTP/1.1 e o custo de uma conexão por long poll, mas mantém o HOL blocking do TCP [F: rfc9113, §1, §5]. Sobre HTTP/3, cada resposta está num stream QUIC independente [F: rfc9114, §2].

## Requisitos e pressupostos

- Proxies e CDNs que não bufferizem respostas em streaming [F: rfc6202, §3.2].
- Eventos com tamanho e frequência moderados; a RFC 6202 não quantifica, mas a lista de problemas assume isso [I].
- Para SSE, apenas texto UTF-8; binário precisa de codificação (base64) [F: whatwg2026html, §9.2] [I].

## Vantagens e limitações

Vantagens [I]:
- Funciona com qualquer servidor HTTP; sem upgrade de protocolo.
- Reconexão e retomada por `Last-Event-ID` já na plataforma [F: whatwg2026html, §9.2].
- Suporte amplo: caniuse registra 97,28% de uso global para SSE (Chrome 6+, Firefox 6+, Safari 5+, Edge 79+) [F: caniuse2026eventsource].

Limitações:
- Unidirecional (SSE) ou com overhead de cabeçalhos por mensagem (long polling) [F: rfc6202, §2.2; whatwg2026html, §9.2].
- Herdam HOL blocking e ordenação estrita do TCP [I].
- Latência de long polling de três trânsitos no pior caso [F: rfc6202, §2.2].
- Limite de conexões por host em HTTP/1.1 [F: whatwg2026html, §9.2].

Quando bastam [I]: notificações, presença, placares, feeds de eventos, jogos por turnos com poucos eventos por minuto, dashboards. O autor recomenda SSE sobre HTTP/2 como primeira opção quando o cliente só precisa receber, e WebSocket quando precisa enviar com frequência.

## Alternativas e comparações

| Critério | Long polling | SSE | WebSocket |
|---|---|---|---|
| Direção | S->C por resposta; C->S por requisição | S->C | bidirecional |
| Overhead por mensagem | cabeçalhos HTTP completos [F: rfc6202, §2.2] | campos de texto | 2-14 bytes de frame [F: rfc6455, §5.2] |
| Reconexão | manual | automática com Last-Event-ID [F: whatwg2026html, §9.2] | manual |
| Binário | sim | não (texto) | sim |

## Exemplo técnico independente de domínio

Stream SSE enviado pelo servidor:

```
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-cache

: keep-alive
retry: 3000

id: 41
event: score
data: {"team":"A","points":3}

id: 42
data: linha 1
data: linha 2

```

Cliente:

```
es = new EventSource("/events")
es.addEventListener("score", e => apply(JSON.parse(e.data)))
es.onerror = () => { /* o user agent reconecta sozinho e envia Last-Event-ID: 42 */ }
```

Long polling (pseudocódigo do cliente):

```
loop:
  resp = GET /poll?since=cursor   (servidor segura até evento ou 30 s)
  if resp.status == 200: apply(resp.events); cursor = resp.cursor
```

## Relações com outros conceitos

Depende de rtm.proto.tcp (e de HTTP/2 e HTTP/3 em rtm.proto.quic). É alternativa a rtm.proto.websocket e rtm.proto.webtransport para notificação servidor-para-cliente. Complementa rtm.arch.event-driven. Casos de uso em rtm.mp.presence e rtm.mp.turn-based; padrões em rtm.rt.communication-patterns.

## Lacunas e questões abertas

- O HTML Living Standard não quantifica o limite de conexões por servidor; o valor depende do user agent (não verificado).
- A seção do Fetch Standard sobre `duplex: "half"` em requisições streaming não foi lida na íntegra.
- Não há evidência verificada aqui comparando latência de SSE e WebSocket sob mesma carga.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc6202 | normativo (Informational) | 2026-10-29 |
| whatwg2026html | normativo | 2026-10-29 |
| whatwg2026fetch | normativo | 2026-10-29 |
| rfc9112 | normativo | 2026-10-29 |
| rfc9113 | normativo | 2026-10-29 |
| rfc9114 | normativo | 2026-10-29 |
| rfc6455 | normativo | 2026-10-29 |
| caniuse2026eventsource | secundario | 2026-10-29 |
