---
id: rtm.proto.websocket
titulo: WebSocket (RFC 6455, RFC 8441, RFC 9220)
tipo: protocolo
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc6455, rfc7936, rfc8307, rfc8441, rfc9220, rfc9113, rfc9114, rfc9293, whatwg2026websockets, caniuse2026websockets]
relacoes:
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: depende-de, alvo: rtm.proto.tcp }
  - { tipo: alternativa-a, alvo: rtm.proto.webtransport }
  - { tipo: alternativa-a, alvo: rtm.proto.http-streaming }
  - { tipo: alternativa-a, alvo: rtm.proto.webrtc }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.rt.communication-patterns }
termos: [WebSocket, opening handshake, frame, opcode, masking, ping/pong, close code, subprotocol, extended CONNECT]
---

# WebSocket (RFC 6455, RFC 8441, RFC 9220)

## Definição e terminologia

WebSocket é um protocolo de mensagens bidirecional, full-duplex, sobre uma única conexão TCP, iniciado por um handshake compatível com HTTP. A RFC 6455, "The WebSocket Protocol", de dezembro de 2011 (I. Fette e A. Melnikov), tem status Proposed Standard e é atualizada pelas RFCs 7936, 8307 e 8441 [F: rfc6455]. A API de navegador é definida pelo WebSockets Standard do WHATWG (Living Standard, atualizado em 19 de outubro de 2026), antes parte do HTML e do Fetch [F: whatwg2026websockets].

Termos:

- **opening handshake**: requisição HTTP com `Upgrade: websocket` respondida com 101 [F: rfc6455, §4].
- **frame**: unidade do protocolo de enquadramento; uma mensagem pode ter vários frames [F: rfc6455, §5.2, §5.4].
- **opcode**: tipo do frame (continuation, text, binary, close, ping, pong) [F: rfc6455, §5.2].
- **masking**: XOR obrigatório dos dados cliente-para-servidor com chave de 32 bits [F: rfc6455, §5.3].
- **subprotocol**: protocolo de aplicação negociado via `Sec-WebSocket-Protocol` [F: rfc6455, §1.9, §11.3.4].

O que não é: não é UDP para navegador, não oferece multiplexação nativa de canais e não permite entrega não confiável ou não ordenada [I].

## Problema que resolve

Antes do WebSocket, comunicação servidor-para-navegador dependia de long polling ou streaming HTTP, com overhead de cabeçalhos e limites de conexão (ver rtm.proto.http-streaming). WebSocket dá um canal persistente de mensagens, com framing leve e sem a semântica requisição-resposta, reutilizando as portas 80 e 443 e a infraestrutura HTTP para o handshake [F: rfc6455, §1.7, §3] [I].

## Fundamentos e funcionamento

**Handshake (RFC 6455 §4).** O cliente envia um GET com `Upgrade: websocket`, `Connection: Upgrade`, `Sec-WebSocket-Key` (base64 aleatório), `Sec-WebSocket-Version: 13`, opcionalmente `Origin`, `Sec-WebSocket-Protocol` e `Sec-WebSocket-Extensions` [F: rfc6455, §4.1]. O servidor responde `101 Switching Protocols` com `Sec-WebSocket-Accept` = base64(SHA-1(key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11")) e, se escolher, um subprotocolo [F: rfc6455, §1.3, §4.2.2]. Esquemas `ws` (porta padrão 80) e `wss` (443) [F: rfc6455, §3].

**Framing (RFC 6455 §5.2).** Cada frame tem FIN (1 bit), RSV1-3 (reservados a extensões), opcode (4 bits), MASK (1 bit), payload length em 7, 7+16 ou 7+64 bits, masking key (32 bits, se MASK) e payload [F: rfc6455, §5.2]. Opcodes: 0x0 continuation, 0x1 text (UTF-8), 0x2 binary, 0x8 close, 0x9 ping, 0xA pong [F: rfc6455, §5.2, §5.5]. Frames de controle têm payload de no máximo 125 bytes e não podem ser fragmentados [F: rfc6455, §5.5]. Fragmentação de mensagens de dados é definida em §5.4.

**Masking.** O cliente deve mascarar todo frame enviado ao servidor; o servidor não mascara. A motivação é impedir que script controlado por atacante produza bytes que pareçam requisições HTTP e envenenem proxies intermediários; "Clients MUST choose a new masking key for each frame" [F: rfc6455, §5.1, §5.3, §10.3].

**Ping/pong.** Ping (0x9) solicita pong (0xA) com o mesmo payload; servem como keep-alive e verificação de vivacidade [F: rfc6455, §5.5.2, §5.5.3]. O WHATWG observa que ping e pong não são expostos à API do navegador [F: whatwg2026websockets].

**Fechamento.** Close frame (0x8) com código de 2 bytes e motivo opcional. Códigos definidos: 1000 normal; 1001 going away; 1002 protocol error; 1003 tipo de dado inaceitável; 1005 nenhum código presente (nunca enviado); 1006 fechamento anormal sem Close frame (nunca enviado); 1007 dado inconsistente com o tipo; 1008 violação de política; 1009 mensagem grande demais; 1010 extensão esperada não negociada; 1011 condição inesperada no servidor; 1015 falha de TLS (nunca enviado) [F: rfc6455, §7.4.1]. Faixas: 1000-2999 reservada ao protocolo, 3000-3999 para bibliotecas e frameworks (registro IANA), 4000-4999 uso privado [F: rfc6455, §7.4.2]. Da API do navegador, `close(code, reason)` aceita só 1000 ou 3000-4999 e motivo de até 123 bytes UTF-8 [F: whatwg2026websockets].

**Subprotocolos e extensões.** Subprotocolos são registrados na IANA por First Come First Served [F: rfc6455, §11.5]; a RFC 7936 esclarece os procedimentos do registro [F: rfc7936]. A RFC 6455 não define nenhuma extensão [F: rfc6455, §9.2].

**Origem.** Servidores destinados a certos sites devem verificar `Origin` e responder 403 se inaceitável; isso protege contra scripts, não contra clientes não-navegador [F: rfc6455, §10.2].

**Bootstrapping sobre HTTP/2 (RFC 8441).** Proposed Standard, setembro de 2018, atualiza a RFC 6455. Define o setting `SETTINGS_ENABLE_CONNECT_PROTOCOL` (0x8) e o "extended CONNECT" com pseudo-cabeçalho `:protocol = websocket`; `Connection`, `Upgrade`, `Sec-WebSocket-Key` e `Sec-WebSocket-Accept` não são usados; como HTTP/2 não tem 101, o servidor responde `:status = 200`; o stream HTTP/2 passa a fazer o papel da conexão TCP, com fechamento ordenado por END_STREAM e abort por RST_STREAM CANCEL [F: rfc8441, §3, §5, §5.1]. Isso permite multiplexar vários WebSockets e requisições numa só conexão TCP [I].

**Bootstrapping sobre HTTP/3 (RFC 9220).** Proposed Standard, 2022; aplica o mesmo extended CONNECT sobre HTTP/3, com `SETTINGS_ENABLE_CONNECT_PROTOCOL` (0x08) no registro de settings do HTTP/3; fechamento ordenado mapeia ao FIN do stream e abort a `H3_REQUEST_CANCELLED`; servidor que não suporta o `:protocol` "SHOULD respond" 501 [F: rfc9220, §3, §5]. Sobre HTTP/3 cada WebSocket vive em um stream QUIC, então uma perda não bloqueia outros streams, mas dentro do WebSocket a entrega continua ordenada e confiável [F: rfc9114, §2] [I].

**API WHATWG.** `new WebSocket(url, protocols)`; esquemas `ws`, `wss` e também `http`/`https` mapeados; `readyState` CONNECTING 0, OPEN 1, CLOSING 2, CLOSED 3; `send()` aceita string, Blob, ArrayBuffer e ArrayBufferView; `bufferedAmount`; `binaryType` "blob" (padrão) ou "arraybuffer"; eventos open, message, error, close; redirecionamentos não são seguidos no handshake; falha antes de estabelecer gera código 1006 [F: whatwg2026websockets].

## Requisitos e pressupostos

- Conexão TCP (ou stream HTTP/2 e HTTP/3) estável; a RFC 6455 posiciona o protocolo sobre TCP [F: rfc6455, §1.7].
- Em navegador, toda a semântica de TCP se aplica: ordenado, confiável, com HOL blocking [I].
- A aplicação implementa heartbeat próprio quando a API não expõe ping/pong [F: whatwg2026websockets] [I].

## Vantagens e limitações

Vantagens [I]: suporte universal (caniuse registra 97,49% de uso global, Chrome 16+, Firefox 11+, Safari 7+, Edge 12+ [F: caniuse2026websockets]); framing de mensagens pronto; passa por proxies HTTP e TLS; modelo mental simples.

Limitações:
- Herda do TCP ordenação estrita e HOL blocking; a RFC 9113 reconhece que "TCP head-of-line blocking is not addressed" [F: rfc9113, §1] [I].
- Sem multiplexação nativa: um WebSocket é um único canal ordenado; a RFC 6455 não define extensão de multiplex [F: rfc6455, §9.2]. Com RFC 8441/9220, a multiplexação vem do HTTP/2 ou HTTP/3, não do WebSocket [I].
- Sem entrega não confiável: dados obsoletos (estado antigo) são retransmitidos [I].
- Sem controle de Nagle pela API do navegador; o comportamento depende da implementação do user agent [H].

Quando basta [I]: jogos por turnos, cartas, quiz, chat, presença, lobby, colaboração com CRDT/OT e qualquer tempo real em que perda é inaceitável e latência de dezenas a centenas de milissegundos é tolerável.

## Alternativas e comparações

| Critério | WebSocket | WebTransport | WebRTC data channel |
|---|---|---|---|
| Transporte | TCP (ou stream H2/H3) [F: rfc6455, §1.7; rfc8441; rfc9220] | QUIC/HTTP/3 [F: frindell2026webtransport] | SCTP/DTLS/UDP [F: rfc8831, §5] |
| Não confiável | não | datagrams [F: rfc9221] | sim, por canal [F: rfc8832, §5.1] |
| Multiplex | só via H2/H3 | streams nativos | vários canais |
| Topologia | cliente-servidor | cliente-servidor | P2P ou servidor |

Ver rtm.proto.comparison.

## Exemplo técnico independente de domínio

```
C -> S:
GET /realtime HTTP/1.1
Host: example.org
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
Sec-WebSocket-Protocol: game.v1

S -> C:
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
Sec-WebSocket-Protocol: game.v1

depois, frame binário pequeno do cliente:
 FIN=1 RSV=000 opcode=0x2 MASK=1 len=5 masking-key=0x12345678 payload=XOR(data, key)
```

Heartbeat de aplicação quando ping/pong não é acessível (pseudocódigo):

```
every 15 s: ws.send({t:"hb", ts:now})
on message {t:"hb", ts}: rtt_estimate = now - ts
if no message for 45 s: ws.close(4000, "timeout"); reconnect()
```

## Relações com outros conceitos

WebSocket depende de rtm.proto.tcp e é especificado pelas RFCs em rtm.std.index. É alternativa a rtm.proto.webtransport, rtm.proto.http-streaming e rtm.proto.webrtc para transporte em navegador. É o transporte de frameworks como rtm.fw.colyseus e rtm.fw.nakama (verificar em seus documentos). Reconexão e retomada de sessão são tratadas em rtm.rel.reconnection; padrões de comunicação, em rtm.rt.communication-patterns.

## Lacunas e questões abertas

- A seção 1.5 (Design Philosophy) da RFC 6455 não foi lida no texto recuperado; a posição sobre TCP vem do sumário e de §1.7.
- Não foi verificado o estado de `WebSocketStream` (API com backpressure); o WHATWG WebSockets Standard consultado não a menciona [F: whatwg2026websockets].
- Comportamento de Nagle/buffering nos user agents não é especificado; é uma hipótese a validar por medição.
- A extensão permessage-deflate (RFC 7692) não foi verificada nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc6455 | normativo | 2026-10-29 |
| rfc7936 | normativo | 2026-10-29 |
| rfc8307 | normativo | 2026-10-29 |
| rfc8441 | normativo | 2026-10-29 |
| rfc9220 | normativo | 2026-10-29 |
| rfc9113 | normativo | 2026-10-29 |
| rfc9114 | normativo | 2026-10-29 |
| rfc8831 | normativo | 2026-10-29 |
| rfc8832 | normativo | 2026-10-29 |
| rfc9221 | normativo | 2026-10-29 |
| frindell2026webtransport | normativo (Internet-Draft) | 2026-10-29 |
| whatwg2026websockets | normativo | 2026-10-29 |
| caniuse2026websockets | secundario | 2026-10-29 |
