---
id: rtm.proto.comparison
titulo: Comparação de protocolos de transporte para tempo real
tipo: comparacao
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc9293, rfc768, rfc8085, rfc6455, rfc8441, rfc9220, rfc8831, rfc8832, rfc8835, rfc9260, rfc9000, rfc9001, rfc9221, rfc9114, rfc9113, rfc6202, whatwg2026html, whatwg2026websockets, w3c2025webrtc, w3c2026webtransport, frindell2026webtransport, caniuse2026websockets, caniuse2026rtcpeerconnection, caniuse2026webtransport, caniuse2026eventsource, mdn2026webtransport]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.proto.tcp }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.proto.webrtc }
  - { tipo: relacionado-a, alvo: rtm.proto.webtransport }
  - { tipo: relacionado-a, alvo: rtm.proto.quic }
  - { tipo: relacionado-a, alvo: rtm.proto.http-streaming }
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.perf.qoe-thresholds }
termos: [head-of-line blocking, reliability, ordering, NAT traversal, browser availability]
---

# Comparação de protocolos de transporte para tempo real

## Definição e terminologia

Este documento compara seis opções de transporte usadas em sistemas de tempo real e multiplayer: TCP, UDP, WebSocket, WebRTC data channel, WebTransport e Server-Sent Events (SSE). Cada linha da tabela remete ao documento do protocolo, onde as afirmações estão citadas em detalhe. Critérios: confiabilidade, ordenação, head-of-line (HOL) blocking, disponibilidade em navegador, NAT traversal, segurança obrigatória, latência típica (qualitativa) e maturidade normativa.

Convenção para as colunas qualitativas [I]: "latência típica" descreve o atraso adicional imposto pelo transporte em relação ao RTT da rede, não um número; "maturidade" descreve o status normativo em 2026-10-29.

## Fundamentos e funcionamento

### Tabela principal

| Critério | TCP | UDP | WebSocket | WebRTC data channel | WebTransport | SSE |
|---|---|---|---|---|---|---|
| Confiabilidade | total [F: rfc9293, §2.2] | nenhuma [F: rfc768] | total (herda TCP) [F: rfc6455, §1.7] | configurável por canal: reliable, limited retransmissions, timed [F: rfc8832, §5.1] | streams confiáveis + datagrams não confiáveis [F: rfc9000, §2; rfc9221, §5.2] | total (herda TCP) [I] |
| Ordenação | total [F: rfc9293, §2.2] | nenhuma [F: rfc768] | total [I] | configurável por canal (ordered/unordered) [F: rfc8832, §5.1] | ordenada dentro de cada stream; nenhuma entre streams ou datagramas [F: rfc9000, §2, §2.2] | total [I] |
| HOL blocking | sim, no fluxo inteiro [I; rfc9113, §1] | não | sim (um canal TCP); via H2/H3 o HOL fica no TCP ou no stream [F: rfc8441; rfc9220] [I] | não entre canais (streams SCTP) [F: rfc9260, §1.5.2]; sim dentro de canal ordenado [I] | não entre streams [F: rfc9114, §2]; sim dentro de um stream [I] | sim (TCP) [I] |
| Navegador | não diretamente (só via HTTP, WebSocket) [I] | não diretamente (só via WebRTC, WebTransport) [I] | sim; 97,49% [F: caniuse2026websockets; whatwg2026websockets] | sim; 97,26% [F: caniuse2026rtcpeerconnection; w3c2025webrtc] | sim; 91,64%; Baseline 2026 Newly available; Safari 26.4+ [F: caniuse2026webtransport; mdn2026webtransport] | sim; 97,28% [F: caniuse2026eventsource; whatwg2026html, §9.2] |
| NAT | cliente-servidor sem problema; P2P requer técnicas fora de escopo [I] | hole punching com ICE/STUN/TURN [F: rfc8445; rfc8489; rfc8656] | cliente-servidor sobre TCP [I] | ICE obrigatório; TURN obrigatório, inclusive sobre TCP/TLS [F: rfc8835, §3.4] | cliente-servidor sobre UDP/QUIC; fallback HTTP/2 [F: frindell2026webtransport] | cliente-servidor [I] |
| Segurança obrigatória | não (TLS opcional) [I] | não (DTLS opcional) [I] | não no protocolo; `wss` recomendado [F: rfc6455, §3] [I] | sim: DTLS obrigatório, chaves inacessíveis ao script [F: rfc8827, §6.5; rfc8831, §5] | sim: QUIC exige TLS 1.3 e a API só aceita `https` [F: rfc9001, §4.2; w3c2026webtransport] | não no protocolo; HTTPS recomendado [I] |
| Latência típica (qualitativa) | handshake 1 RTT; retransmissão e RTO >= 1 s em perda [F: rfc9293, §3.5; rfc6298, §2.4] | mínima; sem handshake nem retransmissão [I] | TCP + handshake HTTP; em regime estável igual a TCP [I] | ICE + DTLS + SCTP para estabelecer; em regime, próxima de UDP para canais unreliable [I] | 1 RTT ou 0-RTT; datagramas próximos de UDP; PTO em vez de RTO [F: rfc9000, §7; rfc9002, §6.2] [I] | long polling até três trânsitos; SSE igual a TCP após conexão [F: rfc6202, §2.2] [I] |
| Maturidade | Internet Standard, STD 7 [F: rfc9293] | Internet Standard, STD 6 [F: rfc768] | Proposed Standard (RFC 6455) + Living Standard [F: rfc6455; whatwg2026websockets] | Proposed Standard (RFCs 8831, 8832) + W3C Recommendation [F: rfc8831; w3c2025webrtc] | Internet-Drafts em WG Last Call + W3C Candidate Recommendation [F: frindell2026webtransport; w3c2026webtransport] | Living Standard (HTML §9.2) + RFC 6202 Informational [F: whatwg2026html; rfc6202] |

### Tabela de capacidades secundárias

| Critério | TCP | UDP | WebSocket | WebRTC DC | WebTransport | SSE |
|---|---|---|---|---|---|---|
| Fronteiras de mensagem | não [F: rfc9293, §3.9.1.2] | sim | sim (frames) [F: rfc6455, §5.2] | sim (mensagens SCTP) [F: rfc9260, §1.1] | streams: não; datagrams: sim [F: rfc9221] | sim (eventos) [F: whatwg2026html, §9.2] |
| Multiplexação nativa | não | n/a | não [F: rfc6455, §9.2] | sim (até 65535 streams) [F: rfc8831, §6.2] | sim (streams QUIC) [F: rfc9000, §2] | não |
| Direção | bidirecional | bidirecional | bidirecional | bidirecional | bidirecional | servidor-para-cliente [F: whatwg2026html, §9.2] |
| Topologia | qualquer | qualquer | cliente-servidor | P2P ou servidor | cliente-servidor | cliente-servidor |
| Binário | sim | sim | sim [F: rfc6455, §5.2] | sim [F: rfc8831, §8] | sim | não (texto UTF-8) [F: whatwg2026html, §9.2] |
| Controle de congestionamento | obrigatório [F: rfc9293, §3.8.2] | responsabilidade da aplicação [F: rfc8085, §3.1] | herdado do TCP | por associação SCTP [F: rfc8831, §5] | por conexão QUIC, compartilhado com datagramas [F: rfc9221, §5.4] | herdado do TCP |
| Migração de rede | não | n/a | não | ICE restart (não verificado aqui) [H] | migração QUIC iniciada pelo cliente [F: rfc9000, §9] | não |
| Reconexão na plataforma | não | n/a | não (aplicação) [I] | não (aplicação) [I] | não (aplicação) [I] | sim, com Last-Event-ID [F: whatwg2026html, §9.2] |

## Algoritmos e modelos relevantes

Modelo de decisão proposto pelo autor [I], a validar com rtm.perf.qoe-thresholds:

1. Precisa de P2P em navegador? WebRTC data channel é a única opção.
2. Precisa de entrega não confiável em navegador, cliente-servidor? WebTransport, com fallback a WebSocket para a parcela sem suporte.
3. Toda mensagem deve chegar e ordem importa (turnos, chat, colaboração)? WebSocket; SSE se só o servidor emite.
4. Fora do navegador, ação rápida? UDP com confiabilidade seletiva, ou QUIC com datagramas.
5. Fora do navegador, sem exigência de latência baixa? TCP.

## Requisitos e pressupostos

- Os percentuais de uso do caniuse são globais e mudam continuamente; foram lidos em 2026-10-29 [F: caniuse2026websockets; caniuse2026rtcpeerconnection; caniuse2026webtransport; caniuse2026eventsource].
- "Latência típica" é qualitativa; medições pertencem a rtm.perf.metrics e rtm.perf.network-emulation.

## Vantagens e limitações

Síntese [I]:
- TCP e derivados (WebSocket, SSE) ganham em simplicidade e maturidade; perdem em HOL blocking e retransmissão de dados obsoletos.
- UDP e derivados (WebRTC DC, WebTransport datagrams, QUIC) ganham em controle de entrega; perdem em complexidade ou maturidade.
- WebRTC é o mais completo e o mais complexo; WebTransport é o mais simples entre os não confiáveis, mas o menos maduro normativamente.

## Alternativas e comparações

Comparações por arquitetura (servidor autoritativo, relay, P2P, lockstep) estão em rtm.arch.comparison; por semântica de entrega (at-most-once, at-least-once, exactly-once na camada de aplicação), em rtm.rel.delivery-semantics.

## Exemplo técnico independente de domínio

Mapeamento de tipos de mensagem para canais, aplicável a qualquer protocolo com múltiplos canais [I]:

```
mensagem            confiável?  ordenada?  canal sugerido
----------------------------------------------------------
join/leave/chat     sim         sim        stream confiável (WS, QUIC stream, DC reliable)
input por tick      não         não        datagram / DC unordered maxRetransmits=0
snapshot de estado  não         não        datagram / DC unordered maxPacketLifeTime=~1 tick
evento irreversível sim         não        DC reliable unordered / stream dedicado
```

## Relações com outros conceitos

Este documento relaciona rtm.proto.tcp, rtm.proto.udp, rtm.proto.websocket, rtm.proto.webrtc, rtm.proto.webtransport, rtm.proto.quic e rtm.proto.http-streaming. As normas estão indexadas em rtm.std.index. Decisões de arquitetura em rtm.arch.comparison; limiares de experiência em rtm.perf.qoe-thresholds.

## Lacunas e questões abertas

- Não há medição comparativa de latência verificada; a coluna é qualitativa.
- ICE restart para migração de rede em WebRTC não foi verificado nas fontes desta sessão.
- O status do WebTransport pode mudar em meses; revisar a coluna de maturidade.
- Falta uma coluna de custo operacional (TURN, servidores HTTP/3), que depende de fontes de fornecedores.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc9293 | normativo | 2026-10-29 |
| rfc768 | normativo | 2026-10-29 |
| rfc8085 | normativo (BCP) | 2026-10-29 |
| rfc6298 | normativo | 2026-10-29 |
| rfc6455 | normativo | 2026-10-29 |
| rfc8441 | normativo | 2026-10-29 |
| rfc9220 | normativo | 2026-10-29 |
| rfc8445 | normativo | 2026-10-29 |
| rfc8489 | normativo | 2026-10-29 |
| rfc8656 | normativo | 2026-10-29 |
| rfc8827 | normativo | 2026-10-29 |
| rfc8831 | normativo | 2026-10-29 |
| rfc8832 | normativo | 2026-10-29 |
| rfc8835 | normativo | 2026-10-29 |
| rfc9260 | normativo | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| rfc9001 | normativo | 2026-10-29 |
| rfc9002 | normativo | 2026-10-29 |
| rfc9221 | normativo | 2026-10-29 |
| rfc9114 | normativo | 2026-10-29 |
| rfc9113 | normativo | 2026-10-29 |
| rfc6202 | normativo (Informational) | 2026-10-29 |
| whatwg2026html | normativo | 2026-10-29 |
| whatwg2026websockets | normativo | 2026-10-29 |
| w3c2025webrtc | normativo | 2026-10-29 |
| w3c2026webtransport | normativo (CR) | 2026-10-29 |
| frindell2026webtransport | normativo (Internet-Draft) | 2026-10-29 |
| caniuse2026websockets | secundario | 2026-10-29 |
| caniuse2026rtcpeerconnection | secundario | 2026-10-29 |
| caniuse2026webtransport | secundario | 2026-10-29 |
| caniuse2026eventsource | secundario | 2026-10-29 |
| mdn2026webtransport | fornecedor | 2026-10-29 |
