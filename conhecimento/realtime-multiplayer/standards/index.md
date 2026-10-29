---
id: rtm.std.index
titulo: Índice de normas e especificações do domínio
tipo: padrao
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc768, rfc9868, rfc9293, rfc896, rfc5681, rfc9438, rfc6298, rfc8085, rfc6455, rfc7936, rfc8307, rfc8441, rfc9220, rfc9112, rfc9113, rfc9114, rfc6202, rfc8825, rfc8826, rfc8827, rfc8829, rfc9429, rfc8831, rfc8832, rfc8834, rfc8835, rfc8445, rfc8863, rfc8489, rfc8656, rfc7675, rfc9260, rfc8261, rfc3758, rfc7496, rfc8260, rfc6347, rfc9147, rfc9853, rfc8446, rfc9846, rfc9000, rfc9001, rfc9002, rfc9221, rfc9297, rfc3393, rfc5905, rfc7679, rfc7680, frindell2026webtransport, kinnear2026overview, frindell2026http2, w3c2021webrtc, w3c2025webrtc, w3c2026webrtced, w3c2026webtransport, whatwg2026html, whatwg2026websockets, whatwg2026fetch, ieee2018posix]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.proto.tcp }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.proto.webrtc }
  - { tipo: relacionado-a, alvo: rtm.proto.webtransport }
  - { tipo: relacionado-a, alvo: rtm.proto.quic }
  - { tipo: relacionado-a, alvo: rtm.proto.http-streaming }
  - { tipo: relacionado-a, alvo: rtm.net.jitter }
  - { tipo: relacionado-a, alvo: rtm.net.packet-loss }
  - { tipo: relacionado-a, alvo: rtm.net.latency }
  - { tipo: relacionado-a, alvo: rtm.net.clock-synchronization }
  - { tipo: relacionado-a, alvo: rtm.sec.transport-security }
  - { tipo: relacionado-a, alvo: rtm.perf.metrics }
termos: [Internet Standard, Proposed Standard, Draft Standard, Best Current Practice, Informational, Historic, Recommendation, Candidate Recommendation, Living Standard, Internet-Draft]
---

# Índice de normas e especificações do domínio

## Definição e terminologia

Índice das RFCs do IETF e das especificações W3C, WHATWG e IEEE relevantes a tempo real e multiplayer, com status normativo verificado em 2026-10-29 nas páginas `rfc-editor.org/info/rfcNNNN`, `datatracker.ietf.org`, `w3.org/TR` e nos Living Standards do WHATWG. Cada entrada traz chave BibTeX (em `referencias/fragmentos/rtm-protocols.bib`), número, título, status, ano e URL.

Níveis de maturidade do IETF usados aqui, como aparecem nas páginas de informação do RFC Editor: **Internet Standard** (com número STD), **Draft Standard** (nível intermediário antigo), **Proposed Standard**, **Best Current Practice** (com número BCP), **Informational** e **Historic** [F: rfc9293; rfc5681; rfc6455; rfc8085; rfc6202; rfc896]. Para o W3C: **Recommendation** e **Candidate Recommendation**; para o WHATWG: **Living Standard**, sem versão, datado pela última atualização; para o IETF antes de RFC: **Internet-Draft**, com estado de grupo de trabalho.

Legenda da coluna "Normativo": N = norma vigente; N-obs = norma obsoletada por outra listada; N-atu = norma vigente atualizada por outra; I = Informational ou Historic (não normativa); D = draft (não publicada).

## Fundamentos e funcionamento

### Transporte básico: UDP e TCP

| Chave | Número | Título | Status | Ano | Normativo | URL |
|---|---|---|---|---|---|---|
| rfc768 | RFC 768 | User Datagram Protocol | Internet Standard, STD 6; atualizada por RFC 9868 [F: rfc768] | 1980 | N-atu | https://www.rfc-editor.org/info/rfc768 |
| rfc9868 | RFC 9868 | Transport Options for UDP | Proposed Standard; atualiza RFC 768 [F: rfc9868] | 2025 | N | https://www.rfc-editor.org/info/rfc9868 |
| rfc9293 | RFC 9293 | Transmission Control Protocol (TCP) | Internet Standard, STD 7; obsoleta RFC 793 e outras [F: rfc9293] | 2022 | N | https://www.rfc-editor.org/info/rfc9293 |
| rfc896 | RFC 896 | Congestion Control in IP/TCP Internetworks | Historic; obsoletada por RFC 7805 [F: rfc896] | 1984 | I | https://www.rfc-editor.org/info/rfc896 |
| rfc5681 | RFC 5681 | TCP Congestion Control | Draft Standard; atualizada por RFC 9438 [F: rfc5681] | 2009 | N-atu | https://www.rfc-editor.org/info/rfc5681 |
| rfc9438 | RFC 9438 | CUBIC for Fast and Long-Distance Networks | Proposed Standard; obsoleta RFC 8312, atualiza RFC 5681 [F: rfc9438] | 2023 | N | https://www.rfc-editor.org/info/rfc9438 |
| rfc6298 | RFC 6298 | Computing TCP's Retransmission Timer | Proposed Standard; obsoleta RFC 2988 [F: rfc6298] | 2011 | N | https://www.rfc-editor.org/info/rfc6298 |
| rfc8085 | RFC 8085 | UDP Usage Guidelines | Best Current Practice, BCP 145; atualizada por RFC 8899 [F: rfc8085] | 2017 | N-atu | https://www.rfc-editor.org/info/rfc8085 |
| ieee2018posix | IEEE Std 1003.1-2017 | The Open Group Base Specifications Issue 7, 2018 edition, `<netinet/tcp.h>` (TCP_NODELAY) [F: ieee2018posix] | norma IEEE/Open Group | 2018 | N | https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/netinet_tcp.h.html |

### HTTP e WebSocket

| Chave | Número | Título | Status | Ano | Normativo | URL |
|---|---|---|---|---|---|---|
| rfc9112 | RFC 9112 | HTTP/1.1 | Internet Standard, STD 99; atualizada por RFC 9931 [F: rfc9112] | 2022 | N-atu | https://www.rfc-editor.org/info/rfc9112 |
| rfc9113 | RFC 9113 | HTTP/2 | Proposed Standard; obsoleta RFC 7540 e 8740 [F: rfc9113] | 2022 | N | https://www.rfc-editor.org/info/rfc9113 |
| rfc9114 | RFC 9114 | HTTP/3 | Proposed Standard [F: rfc9114] | 2022 | N | https://www.rfc-editor.org/info/rfc9114 |
| rfc6202 | RFC 6202 | Known Issues and Best Practices for the Use of Long Polling and Streaming in Bidirectional HTTP | Informational [F: rfc6202] | 2011 | I | https://www.rfc-editor.org/info/rfc6202 |
| rfc6455 | RFC 6455 | The WebSocket Protocol | Proposed Standard; atualizada por RFC 7936, 8307, 8441 [F: rfc6455] | 2011 | N-atu | https://www.rfc-editor.org/info/rfc6455 |
| rfc7936 | RFC 7936 | Clarifying Registry Procedures for the WebSocket Subprotocol Name Registry | Proposed Standard; atualiza RFC 6455 [F: rfc7936] | 2016 | N | https://www.rfc-editor.org/info/rfc7936 |
| rfc8307 | RFC 8307 | Well-Known URIs for the WebSocket Protocol | Proposed Standard; atualiza RFC 6455 [F: rfc8307] | 2018 | N | https://www.rfc-editor.org/info/rfc8307 |
| rfc8441 | RFC 8441 | Bootstrapping WebSockets with HTTP/2 | Proposed Standard; atualiza RFC 6455 [F: rfc8441] | 2018 | N | https://www.rfc-editor.org/info/rfc8441 |
| rfc9220 | RFC 9220 | Bootstrapping WebSockets with HTTP/3 | Proposed Standard [F: rfc9220] | 2022 | N | https://www.rfc-editor.org/info/rfc9220 |
| whatwg2026websockets | WHATWG | WebSockets Standard | Living Standard, atualizado em 2026-10-19 [F: whatwg2026websockets] | 2026 | N | https://websockets.spec.whatwg.org/ |
| whatwg2026html | WHATWG | HTML Standard, §9.2 Server-sent events | Living Standard, atualizado em 2026-10-26 [F: whatwg2026html] | 2026 | N | https://html.spec.whatwg.org/multipage/server-sent-events.html |
| whatwg2026fetch | WHATWG | Fetch Standard | Living Standard, atualizado em 2026-10-19 [F: whatwg2026fetch] | 2026 | N | https://fetch.spec.whatwg.org/ |

### WebRTC

| Chave | Número | Título | Status | Ano | Normativo | URL |
|---|---|---|---|---|---|---|
| rfc8825 | RFC 8825 | Overview: Real-Time Protocols for Browser-Based Applications | Proposed Standard [F: rfc8825] | 2021 | N | https://www.rfc-editor.org/info/rfc8825 |
| rfc8826 | RFC 8826 | Security Considerations for WebRTC | Proposed Standard [F: rfc8826] | 2021 | N | https://www.rfc-editor.org/info/rfc8826 |
| rfc8827 | RFC 8827 | WebRTC Security Architecture | Proposed Standard [F: rfc8827] | 2021 | N | https://www.rfc-editor.org/info/rfc8827 |
| rfc8829 | RFC 8829 | JavaScript Session Establishment Protocol (JSEP) | Proposed Standard; obsoletada por RFC 9429 [F: rfc8829] | 2021 | N-obs | https://www.rfc-editor.org/info/rfc8829 |
| rfc9429 | RFC 9429 | JavaScript Session Establishment Protocol (JSEP) | Proposed Standard; obsoleta RFC 8829 [F: rfc9429] | 2024 | N | https://www.rfc-editor.org/info/rfc9429 |
| rfc8831 | RFC 8831 | WebRTC Data Channels | Proposed Standard [F: rfc8831] | 2021 | N | https://www.rfc-editor.org/info/rfc8831 |
| rfc8832 | RFC 8832 | WebRTC Data Channel Establishment Protocol | Proposed Standard [F: rfc8832] | 2021 | N | https://www.rfc-editor.org/info/rfc8832 |
| rfc8834 | RFC 8834 | Media Transport and Use of RTP in WebRTC | Proposed Standard [F: rfc8834] | 2021 | N | https://www.rfc-editor.org/info/rfc8834 |
| rfc8835 | RFC 8835 | Transports for WebRTC | Proposed Standard [F: rfc8835] | 2021 | N | https://www.rfc-editor.org/info/rfc8835 |
| rfc8445 | RFC 8445 | Interactive Connectivity Establishment (ICE) | Proposed Standard; obsoleta RFC 5245; atualizada por RFC 8863 [F: rfc8445] | 2018 | N-atu | https://www.rfc-editor.org/info/rfc8445 |
| rfc8863 | RFC 8863 | ICE Patiently Awaiting Connectivity (ICE PAC) | Proposed Standard; atualiza RFC 8445 e 8838 [F: rfc8863] | 2021 | N | https://www.rfc-editor.org/info/rfc8863 |
| rfc8489 | RFC 8489 | Session Traversal Utilities for NAT (STUN) | Proposed Standard; obsoleta RFC 5389 [F: rfc8489] | 2020 | N | https://www.rfc-editor.org/info/rfc8489 |
| rfc8656 | RFC 8656 | Traversal Using Relays around NAT (TURN) | Proposed Standard; obsoleta RFC 5766 e 6156 [F: rfc8656] | 2020 | N | https://www.rfc-editor.org/info/rfc8656 |
| rfc7675 | RFC 7675 | STUN Usage for Consent Freshness | Proposed Standard [F: rfc7675] | 2015 | N | https://www.rfc-editor.org/info/rfc7675 |
| w3c2021webrtc | W3C | WebRTC 1.0: Real-Time Communication Between Browsers | Recommendation, 2021-01-26 [F: w3c2021webrtc] | 2021 | N-atu | https://www.w3.org/TR/2021/REC-webrtc-20210126/ |
| w3c2025webrtc | W3C | WebRTC: Real-Time Communication in Browsers | Recommendation, 2025-03-13 [F: w3c2025webrtc] | 2025 | N | https://www.w3.org/TR/webrtc/ |
| w3c2026webrtced | W3C | WebRTC: Real-Time Communication in Browsers (Editor's Draft) | Editor's Draft [F: w3c2026webrtced] | 2026 | D | https://w3c.github.io/webrtc-pc/ |

### SCTP e DTLS

| Chave | Número | Título | Status | Ano | Normativo | URL |
|---|---|---|---|---|---|---|
| rfc9260 | RFC 9260 | Stream Control Transmission Protocol | Proposed Standard; obsoleta RFC 4960 e outras [F: rfc9260] | 2022 | N | https://www.rfc-editor.org/info/rfc9260 |
| rfc3758 | RFC 3758 | SCTP Partial Reliability Extension | Proposed Standard [F: rfc3758] | 2004 | N | https://www.rfc-editor.org/info/rfc3758 |
| rfc7496 | RFC 7496 | Additional Policies for the Partially Reliable SCTP Extension | Proposed Standard [F: rfc7496] | 2015 | N | https://www.rfc-editor.org/info/rfc7496 |
| rfc8260 | RFC 8260 | Stream Schedulers and User Message Interleaving for SCTP | Proposed Standard [F: rfc8260] | 2017 | N | https://www.rfc-editor.org/info/rfc8260 |
| rfc8261 | RFC 8261 | DTLS Encapsulation of SCTP Packets | Proposed Standard; atualizada por RFC 8899 e 8996 [F: rfc8261] | 2017 | N-atu | https://www.rfc-editor.org/info/rfc8261 |
| rfc6347 | RFC 6347 | Datagram Transport Layer Security Version 1.2 | Proposed Standard; obsoletada por RFC 9147 [F: rfc6347] | 2012 | N-obs | https://www.rfc-editor.org/info/rfc6347 |
| rfc9147 | RFC 9147 | The DTLS Protocol Version 1.3 | Proposed Standard; obsoleta RFC 6347; atualizada por RFC 9853 [F: rfc9147] | 2022 | N-atu | https://www.rfc-editor.org/info/rfc9147 |
| rfc9853 | RFC 9853 | Return Routability Check for DTLS 1.2 and 1.3 | Proposed Standard; atualiza RFC 9146 e 9147 [F: rfc9853] | 2026 | N | https://www.rfc-editor.org/info/rfc9853 |

### TLS, QUIC e WebTransport

| Chave | Número | Título | Status | Ano | Normativo | URL |
|---|---|---|---|---|---|---|
| rfc8446 | RFC 8446 | The TLS Protocol Version 1.3 | Proposed Standard; obsoletada por RFC 9846 [F: rfc8446] | 2018 | N-obs | https://www.rfc-editor.org/info/rfc8446 |
| rfc9846 | RFC 9846 | The TLS Protocol Version 1.3 | Proposed Standard; obsoleta RFC 8446 e outras [F: rfc9846] | 2026 | N | https://www.rfc-editor.org/info/rfc9846 |
| rfc9000 | RFC 9000 | QUIC: A UDP-Based Multiplexed and Secure Transport | Proposed Standard [F: rfc9000] | 2021 | N | https://www.rfc-editor.org/info/rfc9000 |
| rfc9001 | RFC 9001 | Using TLS to Secure QUIC | Proposed Standard [F: rfc9001] | 2021 | N | https://www.rfc-editor.org/info/rfc9001 |
| rfc9002 | RFC 9002 | QUIC Loss Detection and Congestion Control | Proposed Standard [F: rfc9002] | 2021 | N | https://www.rfc-editor.org/info/rfc9002 |
| rfc9221 | RFC 9221 | An Unreliable Datagram Extension to QUIC | Proposed Standard [F: rfc9221] | 2022 | N | https://www.rfc-editor.org/info/rfc9221 |
| rfc9297 | RFC 9297 | HTTP Datagrams and the Capsule Protocol | Proposed Standard [F: rfc9297] | 2022 | N | https://www.rfc-editor.org/info/rfc9297 |
| kinnear2026overview | draft-ietf-webtrans-overview-13 | The WebTransport Protocol Framework | Internet-Draft, In WG Last Call, intended Proposed Standard; 2026-07-06 [F: kinnear2026overview] | 2026 | D | https://datatracker.ietf.org/doc/draft-ietf-webtrans-overview/ |
| frindell2026webtransport | draft-ietf-webtrans-http3-16 | WebTransport over HTTP/3 | Internet-Draft, In WG Last Call, intended Proposed Standard; 2026-07-06 [F: frindell2026webtransport] | 2026 | D | https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/ |
| frindell2026http2 | draft-ietf-webtrans-http2-15 | WebTransport over HTTP/2 | Internet-Draft, In WG Last Call, intended Proposed Standard; 2026-07-06 [F: frindell2026http2] | 2026 | D | https://datatracker.ietf.org/doc/draft-ietf-webtrans-http2/ |
| w3c2026webtransport | W3C | WebTransport | Candidate Recommendation Snapshot, 2026-07-30 [F: w3c2026webtransport] | 2026 | N (CR) | https://www.w3.org/TR/webtransport/ |

### Métricas de rede e tempo

| Chave | Número | Título | Status | Ano | Normativo | URL |
|---|---|---|---|---|---|---|
| rfc3393 | RFC 3393 | IP Packet Delay Variation Metric for IPPM | Proposed Standard [F: rfc3393] | 2002 | N | https://www.rfc-editor.org/info/rfc3393 |
| rfc7679 | RFC 7679 | A One-Way Delay Metric for IPPM | Internet Standard, STD 81; obsoleta RFC 2679 [F: rfc7679] | 2016 | N | https://www.rfc-editor.org/info/rfc7679 |
| rfc7680 | RFC 7680 | A One-Way Loss Metric for IPPM | Internet Standard, STD 82; obsoleta RFC 2680 [F: rfc7680] | 2016 | N | https://www.rfc-editor.org/info/rfc7680 |
| rfc5905 | RFC 5905 | Network Time Protocol Version 4 | Proposed Standard; obsoleta RFC 1305 e 4330; atualizada por RFC 7822, 8573, 9109, 9748, 9769 [F: rfc5905] | 2010 | N-atu | https://www.rfc-editor.org/info/rfc5905 |

## Requisitos e pressupostos

- As páginas `/info/` do RFC Editor nem sempre exibem o mês de publicação; quando ausente, o ano vem do aviso de copyright e o mês, do texto da RFC [F: rfc9000; rfc9114].
- DOIs não foram exibidos nas páginas consultadas; o padrão `10.17487/RFCNNNN` do RFC Editor não foi verificado individualmente e não é registrado no BibTeX.

## Relações com outros conceitos

Cada protocolo em `protocols/` declara `especificado-por: rtm.std.index`. As RFCs de métricas (3393, 7679, 7680) sustentam rtm.net.jitter, rtm.net.latency, rtm.net.packet-loss e rtm.perf.metrics; a RFC 5905 sustenta rtm.net.clock-synchronization; DTLS e TLS sustentam rtm.sec.transport-security.

## Lacunas e questões abertas

- RFC 7805 (que tornou a RFC 896 Historic), RFC 8899 (DPLPMTUD), RFC 8838 (Trickle ICE), RFC 8843 (BUNDLE) e RFC 7692 (permessage-deflate) são citadas por outras RFCs mas não foram abertas nesta sessão; não verificadas.
- RFC 2330 (framework IPPM) e RFC 2679/2680 (obsoletas) não foram abertas.
- Não foram localizadas normas IEEE específicas de jogos em rede; IEEE 1278 (DIS) não foi verificada nesta sessão.
- Os drafts WebTransport podem ter sido publicados como RFC após 2026-10-29; reverificar.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| todas as chaves das tabelas acima | normativo (ou Informational/Historic/Draft, conforme a coluna Status) | 2026-10-29 |
