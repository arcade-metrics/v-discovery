---
id: rtm.proto.webrtc
titulo: WebRTC e data channels
tipo: protocolo
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc8825, rfc8826, rfc8827, rfc8829, rfc9429, rfc8831, rfc8832, rfc8834, rfc8835, rfc8445, rfc8863, rfc8489, rfc8656, rfc7675, rfc9260, rfc8261, rfc3758, rfc7496, rfc8260, rfc6347, rfc9147, w3c2021webrtc, w3c2025webrtc, w3c2026webrtced, mdn2026createdatachannel, mdn2026rtcdatachannel, caniuse2026rtcpeerconnection]
relacoes:
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: depende-de, alvo: rtm.proto.udp }
  - { tipo: alternativa-a, alvo: rtm.proto.websocket }
  - { tipo: alternativa-a, alvo: rtm.proto.webtransport }
  - { tipo: complementa, alvo: rtm.arch.peer-to-peer }
  - { tipo: complementa, alvo: rtm.arch.relay-server }
  - { tipo: relacionado-a, alvo: rtm.sec.transport-security }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.net.ordering-and-reliability }
termos: [WebRTC, data channel, SCTP, DTLS, ICE, STUN, TURN, DCEP, partial reliability, SFU, signaling]
---

# WebRTC e data channels

## Definição e terminologia

WebRTC é um conjunto de protocolos (IETF) e uma API JavaScript (W3C) para comunicação em tempo real entre navegadores e outros endpoints. A RFC 8825 (Proposed Standard, janeiro de 2021) é o "applicability statement" do conjunto: não define protocolo, mas lista o que uma implementação deve seguir [F: rfc8825]. A API é "WebRTC: Real-Time Communication in Browsers", W3C Recommendation; a primeira Recommendation é de 26 de janeiro de 2021 [F: w3c2021webrtc] e a versão vigente consultada é de 13 de março de 2025 [F: w3c2025webrtc].

Termos:

- **data channel**: canal de dados arbitrários sobre SCTP/DTLS/UDP, com reliability e ordering configuráveis [F: rfc8831, §6.4].
- **DCEP**: Data Channel Establishment Protocol, negociação in-band de canais [F: rfc8832].
- **ICE / STUN / TURN**: NAT traversal (ver rtm.proto.udp).
- **signaling**: troca de ofertas e respostas SDP, fora do escopo das RFCs: "outside the scope of the WebRTC protocol suite" [F: rfc8825, §3].
- **SFU**: selective forwarding unit, servidor que termina conexões WebRTC e repassa fluxos; o termo é de uso técnico, não definido nas RFCs consultadas [I].

## Problema que resolve

Para jogos e colaboração, data channels são a única forma de um navegador enviar dados não confiáveis ou não ordenados diretamente a outro peer, com NAT traversal e criptografia obrigatórias [I]. O conjunto também resolve mídia (áudio/vídeo), que não é o foco deste domínio.

## Fundamentos e funcionamento

**Documentos obrigatórios (RFC 8825).** Endpoints MUST implementar RFC 8835 (transportes), RFC 8834 (RTP), RFC 8826 e 8827 (segurança), RFC 8831 e 8832 (data channels); navegadores MUST implementar JSEP e a API W3C [F: rfc8825, §4, §5, §7, §8]. JSEP era a RFC 8829, obsoletada pela RFC 9429 (Proposed Standard, 2024) [F: rfc9429].

**Pilha de transporte (RFC 8835, RFC 8831).** ICE completo (não ICE-Lite) MUST ser suportado; TURN MUST ser suportado, inclusive sobre TCP e TLS para "UDP-blocking firewalls"; ICE-TCP (RFC 6544) MUST ser suportado [F: rfc8835, §3.4]. A troca de chaves MUST usar DTLS-SRTP; DTLS e RTP são multiplexados na mesma porta; todos os pares de candidatos compartilham uma associação DTLS [F: rfc8835, §3.5]. Para data channels: SCTP sobre DTLS sobre ICE (RFC 8261), com I-DATA (RFC 8260) e DCEP (RFC 8832) [F: rfc8835, §3.5]. A RFC 8831 descreve a pilha: SCTP sobre DTLS sobre ICE/UDP; SCTP roda em user space porque DTLS normalmente roda; multihoming não é usado; o controle de congestionamento é por associação, logo todos os canais compartilham uma janela [F: rfc8831, §1, §5]. PMTU inicial não deve exceder 1200 bytes em IPv4 e 1280 em IPv6 [F: rfc8831, §5].

**Segurança (RFC 8826, 8827).** O navegador é a base confiável; "it MUST NOT be possible for arbitrary sites to initiate calls to arbitrary locations without user consent"; ICE serve como verificação de consentimento e a frescura do consentimento segue a RFC 7675 [F: rfc8826, §3, §4.1, §4.2.1]. A RFC 7675 define checagens STUN a cada ~5 s (nunca abaixo de 4 s) e expiração do consentimento em 30 s sem resposta [F: rfc7675]. A RFC 8827 exige DTLS-SRTP em todo canal de mídia, DTLS 1.2 com TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 e P-256, preferência por forward secrecy, e proíbe que JavaScript obtenha material de chave [F: rfc8827, §6.5]. DTLS 1.2 (RFC 6347) foi obsoletada por DTLS 1.3 (RFC 9147) [F: rfc9147], mas as RFCs WebRTC consultadas referenciam a 1.2 [F: rfc8827, §6.5; rfc8835].

**SCTP (RFC 9260).** Proposed Standard, junho de 2022, obsoleta a RFC 4960. É orientado a mensagens, com múltiplos streams por associação; a entrega é sequenciada dentro de cada stream, "so a blocked stream does not hold up the others", o que evita HOL blocking entre streams [F: rfc9260, §1.1, §1.5.2]. O bit U marca mensagens não ordenadas [F: rfc9260, §3.3.1]. Handshake de quatro vias com cookie (INIT, INIT ACK, COOKIE ECHO, COOKIE ACK) [F: rfc9260, §1.5.1]. Controle de congestionamento semelhante ao TCP [F: rfc9260, §7].

**Confiabilidade parcial.** PR-SCTP (RFC 3758) acrescenta o chunk FORWARD TSN e o serviço de "timed reliability" por lifetime [F: rfc3758, §3.2, §4.1]. A RFC 7496 adiciona a "Limited Retransmissions Policy" (limite de retransmissões; 0 dá comportamento tipo UDP) e cita a pilha WebRTC como caso de uso [F: rfc7496, §3.1]. A RFC 8831 exige PR-SCTP com ambas as políticas, e diz que retransmissões zero com entrega não ordenada "gives a UDP-like service" [F: rfc8831, §6.1, §6.4]. A RFC 8260 (I-DATA, interleaving de mensagens) evita que uma mensagem grande monopolize a associação; "The interleaving of user messages is required for WebRTC data channels" e o escalonador WFQ deve ser suportado [F: rfc8260, §2, §3].

**Canais (RFC 8831, 8832).** Cada canal usa um stream SCTP de entrada e um de saída com o mesmo id; o número de streams negociado SHOULD ser 65535; cliente DTLS usa ids pares e servidor, ímpares [F: rfc8831, §6.2, §6.5; rfc8832, §4]. PPIDs: 51 string, 53 binary, 56 string vazia, 57 binary vazia; DCEP usa PPID 50 [F: rfc8831, §8; rfc8832, §8.1]. Sem interleaving, emissores SHOULD limitar mensagens a 16 KB [F: rfc8831, §6.6]. Emissores SHOULD desativar Nagle [F: rfc8831, §6.6]. DCEP: DATA_CHANNEL_OPEN (0x03) com Channel Type, Priority, Reliability Parameter, Label e Protocol; DATA_CHANNEL_ACK (0x02) [F: rfc8832, §5.1, §5.2]. Tipos: 0x00 reliable ordered; 0x80 reliable unordered; 0x01 partial reliable rexmit; 0x81 rexmit unordered; 0x02 partial reliable timed; 0x82 timed unordered; o Reliability Parameter é o número de retransmissões ou o lifetime em ms [F: rfc8832, §5.1].

**API W3C.** `createDataChannel(label, options)` com `ordered` (padrão true), `maxPacketLifeTime`, `maxRetransmits` (mutuamente exclusivos; "an attempt to do so will result in an error"), `protocol`, `negotiated` (padrão false), `id`; `readyState` connecting/open/closing/closed; `bufferedAmount` e `bufferedAmountLowThreshold`; `binaryType` inicia em "arraybuffer"; `send()` aceita string, Blob, ArrayBuffer e ArrayBufferView e lança TypeError se exceder `maxMessageSize` [F: w3c2026webrtced, §6.2]. A documentação do MDN afirma que label e protocol não podem exceder 65.535 bytes, que `id` vai de 0 a 65534 e que definir ambos os limites lança SyntaxError [F: mdn2026createdatachannel]. `RTCIceServer.urls` aceita `stun:`, `turn:` e `turns:`; implementações devem suportar pelo menos 32 entradas [F: w3c2025webrtc].

## Requisitos e pressupostos

- Canal de sinalização próprio (WebSocket, HTTP) para trocar SDP e candidatos ICE; JSEP permite trickle ICE [F: rfc8829, §3.5] [I].
- Servidores STUN e, para NATs restritivos ou firewalls, TURN; sem TURN, parte dos pares não conecta [F: rfc8656, §1; rfc8835, §3.4] [I].
- Em uso com servidor (SFU ou servidor autoritativo), o servidor precisa de uma implementação WebRTC não-navegador, que a RFC 8825 reconhece como endpoint conforme sem API JavaScript [F: rfc8825, §2.2].

## Vantagens e limitações

Vantagens [I]: única opção P2P em navegador; reliability e ordering por canal; criptografia obrigatória; suporte amplo (caniuse: 97,26% de uso global; Chrome 23+, Firefox 22+, Safari 11+, Edge 79+ [F: caniuse2026rtcpeerconnection]); MDN marca RTCDataChannel como Baseline "Widely available" desde janeiro de 2020 [F: mdn2026rtcdatachannel].

Limitações:
- Complexidade: ICE, DTLS, SCTP, SDP e sinalização externa [I].
- Congestionamento compartilhado entre todos os canais da associação [F: rfc8831, §5].
- Latência de estabelecimento: coleta de candidatos, checagens ICE, handshake DTLS e SCTP [I].
- P2P expõe IP dos pares; a RFC 8826 lista mitigação via TURN [F: rfc8826, §4.2.4].
- Em topologia P2P com N jogadores, cada cliente mantém N-1 conexões; autoridade e anti-cheat ficam mais difíceis (ver rtm.arch.peer-to-peer) [I].
- Custo de TURN quando o caminho direto falha [F: rfc8656, §1].

## Alternativas e comparações

Para cliente-servidor com dados não confiáveis em navegador, WebTransport (rtm.proto.webtransport) é mais simples; para dados confiáveis ordenados, WebSocket. Ver rtm.proto.comparison [I].

## Exemplo técnico independente de domínio

```
A                       sinalização                     B
|-- createOffer / setLocalDescription                  |
|-- offer (SDP) ---------------------------------------->|
|                                   setRemoteDescription, createAnswer
|<-- answer (SDP) ---------------------------------------|
|<-- candidatos ICE (trickle) -------------------------->|
|== checagens STUN par a par; nominação ==================|
|== handshake DTLS (um por associação) ===================|
|== SCTP INIT / INIT ACK / COOKIE ECHO / COOKIE ACK =====|
|-- DCEP DATA_CHANNEL_OPEN (stream 0, tipo 0x82, lifetime=100ms, label="state")
|<-- DCEP DATA_CHANNEL_ACK
|-- mensagens de estado, não ordenadas, descartadas após 100 ms
```

Configuração típica de canais num jogo [I]:

```
state   = pc.createDataChannel("state",  {ordered:false, maxPacketLifeTime:100})
input   = pc.createDataChannel("input",  {ordered:false, maxRetransmits:3})
control = pc.createDataChannel("control")   // reliable, ordered
```

## Relações com outros conceitos

WebRTC depende de rtm.proto.udp (ICE, STUN, TURN, DTLS) e é especificado pelas RFCs em rtm.std.index. É alternativa a rtm.proto.websocket e rtm.proto.webtransport. Complementa rtm.arch.peer-to-peer e rtm.arch.relay-server (SFU ou TURN). Segurança de transporte em rtm.sec.transport-security; semânticas de entrega em rtm.rel.delivery-semantics.

## Lacunas e questões abertas

- O texto da seção 6.2 da Recommendation de 2025 não pôde ser lido na íntegra; os detalhes da API foram confirmados no editor's draft [F: w3c2026webrtced] e no MDN. Verificar se o erro ao definir ambos os limites é TypeError ou SyntaxError na Recommendation (MDN diz SyntaxError; o editor's draft diz apenas "an error").
- A adoção de DTLS 1.3 em implementações WebRTC não foi verificada.
- Não há valor numérico de latência adicionada por TURN nas RFCs [F: rfc8656]; medir em rtm.perf.network-emulation.
- A posição do WebRTC em relação a RFC 8863 (ICE PAC) e `maxChannels` prático por navegador não foi verificada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc8825 | normativo | 2026-10-29 |
| rfc8826 | normativo | 2026-10-29 |
| rfc8827 | normativo | 2026-10-29 |
| rfc8829 | normativo (obsoleta) | 2026-10-29 |
| rfc9429 | normativo | 2026-10-29 |
| rfc8831 | normativo | 2026-10-29 |
| rfc8832 | normativo | 2026-10-29 |
| rfc8834 | normativo | 2026-10-29 |
| rfc8835 | normativo | 2026-10-29 |
| rfc8445 | normativo | 2026-10-29 |
| rfc8863 | normativo | 2026-10-29 |
| rfc8489 | normativo | 2026-10-29 |
| rfc8656 | normativo | 2026-10-29 |
| rfc7675 | normativo | 2026-10-29 |
| rfc9260 | normativo | 2026-10-29 |
| rfc8261 | normativo | 2026-10-29 |
| rfc3758 | normativo | 2026-10-29 |
| rfc7496 | normativo | 2026-10-29 |
| rfc8260 | normativo | 2026-10-29 |
| rfc6347 | normativo (obsoleta) | 2026-10-29 |
| rfc9147 | normativo | 2026-10-29 |
| w3c2021webrtc | normativo | 2026-10-29 |
| w3c2025webrtc | normativo | 2026-10-29 |
| w3c2026webrtced | normativo (editor's draft) | 2026-10-29 |
| mdn2026createdatachannel | fornecedor | 2026-10-29 |
| mdn2026rtcdatachannel | fornecedor | 2026-10-29 |
| caniuse2026rtcpeerconnection | secundario | 2026-10-29 |
