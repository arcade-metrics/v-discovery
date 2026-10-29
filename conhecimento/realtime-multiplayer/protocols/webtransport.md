---
id: rtm.proto.webtransport
titulo: WebTransport
tipo: protocolo
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [frindell2026webtransport, kinnear2026overview, frindell2026http2, w3c2026webtransport, rfc9000, rfc9114, rfc9221, rfc9297, rfc9002, mdn2026webtransport, caniuse2026webtransport]
relacoes:
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: depende-de, alvo: rtm.proto.quic }
  - { tipo: depende-de, alvo: rtm.proto.udp }
  - { tipo: alternativa-a, alvo: rtm.proto.websocket }
  - { tipo: alternativa-a, alvo: rtm.proto.webrtc }
  - { tipo: complementa, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
termos: [WebTransport, datagram, unidirectional stream, bidirectional stream, sendOrder, Baseline]
---

# WebTransport

## Definição e terminologia

WebTransport é um framework cliente-servidor para navegadores, com streams confiáveis e datagramas não confiáveis, sobre HTTP/3 (QUIC) e, como fallback, HTTP/2. A especificação tem duas partes: no IETF, o grupo WEBTRANS mantém "The WebTransport Protocol Framework" (draft-ietf-webtrans-overview-13), "WebTransport over HTTP/3" (draft-ietf-webtrans-http3-16) e "WebTransport over HTTP/2" (draft-ietf-webtrans-http2-15); no W3C, a API "WebTransport" é Candidate Recommendation Snapshot de 30 de julho de 2026 [F: kinnear2026overview; frindell2026webtransport; frindell2026http2; w3c2026webtransport].

**Status em 2026-10-29.** Os três drafts do IETF estão em estado "In WG Last Call" com IESG state "I-D Exists", intended status Proposed Standard, última versão de 6 de julho de 2026, expirando em 7 de janeiro de 2027; nenhum foi publicado como RFC [F: frindell2026webtransport; kinnear2026overview; frindell2026http2]. A API W3C é Candidate Recommendation, não Recommendation [F: w3c2026webtransport]. A própria API observa que os drafts subjacentes ainda estão em andamento e que a API pode mudar [F: w3c2026webtransport].

Termos:
- **datagram**: mensagem não confiável, não ordenada, que cabe em um pacote QUIC [F: rfc9221, §5].
- **unidirectional / bidirectional stream**: fluxos confiáveis e ordenados, independentes entre si [F: rfc9000, §2].
- **sendOrder**: prioridade de envio entre streams e datagramas [F: w3c2026webtransport, §6.11].

O que não é: não é P2P (só cliente-servidor), não substitui WebRTC para mídia e não é "UDP bruto" (há criptografia e controle de congestionamento obrigatórios) [I].

## Problema que resolve

Dá ao navegador o que até então só WebRTC data channels ofereciam, mas em topologia cliente-servidor e sem ICE/SDP: entrega não confiável (datagramas) e múltiplos streams sem head-of-line blocking entre si, com a segurança e o handshake rápido de QUIC [I]. O overview do IETF descreve o objetivo: permitir que clientes "security-restricted" (navegadores) se comuniquem com um servidor por um transporte seguro e multiplexado, com protocolos considerados seguros de expor a aplicações não confiáveis [F: kinnear2026overview].

## Fundamentos e funcionamento

**Base QUIC.** Streams são criados por qualquer endpoint, podem enviar dados intercalados com outros streams e podem ser cancelados; "QUIC does not provide any means of ensuring ordering between bytes on different streams" [F: rfc9000, §2]. HTTP/3 coloca cada requisição em seu próprio stream, de modo que um stream bloqueado ou com perda não interrompe os outros [F: rfc9114, §2].

**Datagramas.** A RFC 9221 define os frames DATAGRAM (0x30, 0x31): não retransmitidos, mas ack-eliciting; protegidos por chaves 0-RTT ou 1-RTT; sujeitos ao controlador de congestionamento da conexão; sem controle de fluxo; devem caber em um único pacote QUIC; casos de uso citados: áudio e vídeo em tempo real, jogos, túneis [F: rfc9221, §2, §3, §5, §5.2, §5.3, §5.4]. A RFC 9297 associa datagramas a uma requisição HTTP/3 pelo Quarter Stream ID e define `SETTINGS_H3_DATAGRAM` (0x33) e o Capsule Protocol para HTTP/1.1 e HTTP/2, onde não há entrega não confiável [F: rfc9297, §2.1, §2.1.1, §3]. WebTransport sobre HTTP/2 confirma: seus datagramas não são de fato não confiáveis, pois HTTP/2 retransmite [F: frindell2026http2, §5.1].

**API W3C.** `new WebTransport(url, options)` aceita apenas URLs `https` sem fragmento; `ready` resolve quando a sessão é estabelecida; `closed` quando termina; `draining` sinaliza encerramento gracioso solicitado pelo servidor [F: w3c2026webtransport]. `datagrams` expõe `readable`, `createWritable`, `maxDatagramSize`, `incomingMaxAge`, `outgoingMaxAge` e limites de buffer [F: w3c2026webtransport, §6.14]. `createBidirectionalStream()`, `createUnidirectionalStream()`, `incomingBidirectionalStreams`, `incomingUnidirectionalStreams` [F: w3c2026webtransport]. `sendOrder` (padrão 0) faz bytes de streams com valor maior serem enviados antes; `sendGroup` cria espaços de prioridade com partilha igual de banda [F: w3c2026webtransport, §6.11, §8]. Opções: `serverCertificateHashes`, `allowPooling`, `requireUnreliable`, `congestionControl` ("default", "throughput", "low-latency"; "low-latency" é feature at risk), `protocols` (subprotocolo), `headers` [F: w3c2026webtransport, §6.9]. `getStats()` expõe `smoothedRtt`, `rttVariation`, `minRtt`, `bytesLost`, `packetsLost`, `estimatedSendRate`, e para datagramas `lostOutgoing` (conforme RFC 9002 §6.1), `expiredOutgoing`, `expiredIncoming`, `droppedIncoming` [F: w3c2026webtransport, §6.13, §6.14]. `WebTransportCloseInfo` tem `closeCode` e `reason` [F: w3c2026webtransport, §6.10].

**Suporte de navegadores (2026-10-29).** O MDN marca a interface como "Baseline 2026 - Newly available", com a nota "Since March 2026, this feature works across the latest devices and browser versions" [F: mdn2026webtransport]. O caniuse registra 91,64% de uso global suportado: Chrome 97+ (91-94 desativado por padrão), Edge 98+, Firefox 114+, Safari 26.4+, Safari iOS 26.4+, Opera 83+, Samsung Internet 18+ [F: caniuse2026webtransport]. A tabela de compatibilidade detalhada do MDN não pôde ser extraída nesta sessão (ver Lacunas).

## Requisitos e pressupostos

- Servidor HTTP/3 com suporte a WebTransport; caminho UDP aberto até o servidor; a RFC 9000 exige datagramas de pelo menos 1200 bytes [F: rfc9000, §14].
- Fallback para HTTP/2 quando UDP é bloqueado, aceitando perda das garantias de não confiabilidade [F: frindell2026http2].
- Certificado válido ou `serverCertificateHashes` [F: w3c2026webtransport].
- A aplicação lida com datagramas que excedem `maxDatagramSize` e com expiração por `outgoingMaxAge` [F: rfc9221, §5; w3c2026webtransport, §6.14] [I].

## Vantagens e limitações

Vantagens [I]:
- Datagramas não confiáveis e streams independentes em cliente-servidor, sem ICE, SDP ou sinalização externa.
- Handshake QUIC/TLS 1.3 em 1 RTT, com 0-RTT possível [F: rfc9000, §7].
- Migração de conexão QUIC pode manter a sessão em troca de rede, iniciada pelo cliente [F: rfc9000, §9].
- Estatísticas de transporte expostas à aplicação [F: w3c2026webtransport, §6.13].

Limitações:
- Especificações não finalizadas em 2026-10-29 (drafts em WG Last Call; W3C em CR) [F: frindell2026webtransport; w3c2026webtransport].
- Só cliente-servidor [F: kinnear2026overview] [I].
- Suporte em Safari só a partir de 26.4 [F: caniuse2026webtransport]; a parcela sem suporte exige fallback a WebSocket [I].
- Datagramas limitados a um pacote QUIC, tipicamente cerca de 1200 bytes de payload [F: rfc9221, §5; rfc9000, §14] [I].
- Congestionamento compartilhado entre streams e datagramas da mesma conexão [F: rfc9221, §5.4].

## Alternativas e comparações

| Critério | WebTransport | WebSocket | WebRTC data channel |
|---|---|---|---|
| Não confiável | datagrams [F: rfc9221] | não | sim [F: rfc8832] |
| Multiplex sem HOL | streams QUIC [F: rfc9114, §2] | não (um canal TCP) | streams SCTP [F: rfc9260, §1.5.2] |
| Topologia | cliente-servidor | cliente-servidor | P2P ou servidor |
| Status da spec | drafts + CR [F: frindell2026webtransport; w3c2026webtransport] | RFC + Living Standard | RFCs + Recommendation |
| Uso global (caniuse) | 91,64% [F: caniuse2026webtransport] | 97,49% [F: caniuse2026websockets] | 97,26% [F: caniuse2026rtcpeerconnection] |

Ver rtm.proto.comparison.

## Exemplo técnico independente de domínio

```
wt = new WebTransport("https://game.example/session", {congestionControl:"low-latency"})
await wt.ready

// canal confiável de controle (um stream bidirecional)
ctl = await wt.createBidirectionalStream()
ctlWriter = ctl.writable.getWriter(); ctlWriter.write(encode({type:"join", room}))

// estado por datagrama, não confiável
dgWriter = wt.datagrams.createWritable({sendOrder: 10})   // prioridade acima de 0
every tick: dgWriter.write(encode({seq, input}))

// recepção
for await (const dg of wt.datagrams.readable) apply(decode(dg))

// fallback
if (!("WebTransport" in self) || failed(wt)) useWebSocket()
```

## Relações com outros conceitos

WebTransport depende de rtm.proto.quic e, por consequência, de rtm.proto.udp; é especificado pelos drafts e RFCs listados em rtm.std.index. É alternativa a rtm.proto.websocket e rtm.proto.webrtc em navegador. Complementa rtm.arch.authoritative-server como transporte cliente-servidor com datagramas. Semânticas de entrega em rtm.rel.delivery-semantics; reconexão e migração em rtm.rel.reconnection.

## Lacunas e questões abertas

- A tabela de compatibilidade do MDN não foi renderizada no texto recuperado; versões vêm do caniuse, que ainda rotula a API W3C como "Working Draft" embora a página do W3C consultada seja Candidate Recommendation [F: caniuse2026webtransport; w3c2026webtransport].
- O status pode mudar: drafts em WG Last Call em julho de 2026; verificar publicação como RFC.
- Não há dado empírico aqui sobre a diferença de latência entre datagramas WebTransport e WebRTC data channels; pertence a rtm.perf.metrics.
- Suporte a WebTransport sobre HTTP/2 nos navegadores não foi verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| frindell2026webtransport | normativo (Internet-Draft) | 2026-10-29 |
| kinnear2026overview | normativo (Internet-Draft) | 2026-10-29 |
| frindell2026http2 | normativo (Internet-Draft) | 2026-10-29 |
| w3c2026webtransport | normativo (Candidate Recommendation) | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| rfc9114 | normativo | 2026-10-29 |
| rfc9221 | normativo | 2026-10-29 |
| rfc9297 | normativo | 2026-10-29 |
| rfc9002 | normativo | 2026-10-29 |
| rfc9260 | normativo | 2026-10-29 |
| rfc8832 | normativo | 2026-10-29 |
| mdn2026webtransport | fornecedor | 2026-10-29 |
| caniuse2026webtransport | secundario | 2026-10-29 |
| caniuse2026websockets | secundario | 2026-10-29 |
| caniuse2026rtcpeerconnection | secundario | 2026-10-29 |
