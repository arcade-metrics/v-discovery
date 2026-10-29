---
id: rtm.proto.quic
titulo: QUIC e HTTP/3
tipo: protocolo
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc9000, rfc9001, rfc9002, rfc9114, rfc9221, rfc8446, rfc9846, rfc9113, rfc8085]
relacoes:
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: depende-de, alvo: rtm.proto.udp }
  - { tipo: alternativa-a, alvo: rtm.proto.tcp }
  - { tipo: complementa, alvo: rtm.proto.webtransport }
  - { tipo: complementa, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.net.ordering-and-reliability }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.sec.transport-security }
termos: [QUIC, stream, 0-RTT, connection ID, connection migration, PTO, HTTP/3, QPACK]
---

# QUIC e HTTP/3

## Definição e terminologia

QUIC é um transporte multiplexado e seguro sobre UDP, definido na RFC 9000 (Proposed Standard, maio de 2021, J. Iyengar e M. Thomson, eds.) [F: rfc9000]. A RFC 9001 define o uso de TLS 1.3 para segurança [F: rfc9001] e a RFC 9002, detecção de perda e controle de congestionamento [F: rfc9002]. HTTP/3 (RFC 9114, Proposed Standard, junho de 2022) mapeia a semântica HTTP sobre QUIC [F: rfc9114].

Termos:
- **stream**: fluxo de bytes ordenado dentro de uma conexão; unidirecional ou bidirecional; ids de 62 bits cujos dois bits baixos codificam iniciador e direção [F: rfc9000, §2.1].
- **0-RTT**: envio de dados pelo cliente antes da resposta do servidor, usando parâmetros de uma conexão anterior [F: rfc9000, §7.4.1].
- **connection ID**: identificador que permite à conexão sobreviver a mudanças de IP e porta [F: rfc9000, §9].
- **PTO (probe timeout)**: substitui o RTO do TCP [F: rfc9002, §6.2].

O que não é: não é "TCP sobre UDP"; a semântica de confiabilidade é por stream, e a criptografia não é opcional [F: rfc9001, §4.2] [I].

## Problema que resolve

Elimina o head-of-line blocking entre fluxos independentes que HTTP/2 sobre TCP sofre ("TCP head-of-line blocking is not addressed by this protocol" [F: rfc9113, §1]), integra o handshake de transporte com o de TLS para reduzir RTTs e permite que a conexão sobreviva a troca de rede [I]. A RFC 9114 explica que em HTTP/2 sobre TCP uma perda de pacote paralisa todas as transações ativas, enquanto em HTTP/3 cada par requisição-resposta usa seu próprio stream QUIC [F: rfc9114, §1.1, §2].

## Fundamentos e funcionamento

**Streams.** Criados por qualquer endpoint, "can concurrently send data interleaved with other streams, and can be canceled"; "QUIC does not provide any means of ensuring ordering between bytes on different streams"; dentro de um stream, "Endpoints MUST be able to deliver stream data to an application as an ordered byte stream" [F: rfc9000, §2, §2.2]. Controle de fluxo por stream (MAX_STREAM_DATA) e por conexão (MAX_DATA), e limite de concorrência (MAX_STREAMS) [F: rfc9000, §4.1, §4.6].

**Handshake.** O handshake criptográfico é carregado em pacotes Initial e Handshake; "QUIC includes the encoded transport parameters in the cryptographic handshake" [F: rfc9000, §7.1, §7.4]. Há quatro níveis de chave: Initial, 0-RTT, Handshake e 1-RTT [F: rfc9001, §2.1, §4.1.3]. TLS 1.3 é o mínimo: clientes não devem oferecer versões anteriores [F: rfc9001, §4.2]. 0-RTT "depends on both client and server using protocol parameters that were negotiated from a previous connection" [F: rfc9000, §7.4.1] e os dados 0-RTT "can be replayed by an attacker" [F: rfc9001, §4.6]. A RFC 8446 (TLS 1.3) foi obsoletada pela RFC 9846 em 2026 [F: rfc9846].

**Migração.** Connection IDs permitem sobreviver a mudanças de endereço; "Clients are responsible for initiating all migrations"; endpoints "MUST NOT initiate connection migration before the handshake is confirmed"; ao detectar mudança de endereço (NAT rebinding), o endpoint "MUST perform path validation" com PATH_CHALLENGE/PATH_RESPONSE; o parâmetro `disable_active_migration` restringe migração ativa; o servidor pode indicar `preferred_address` [F: rfc9000, §8.2, §9, §9.3, §9.6]. A conexão é fechada silenciosamente ao exceder o menor `max_idle_timeout` anunciado [F: rfc9000, §10.1].

**Tamanho de datagrama.** QUIC não deve ser usado em caminhos que não suportem datagramas de 1200 bytes; pacotes Initial devem ser expandidos a pelo menos 1200 bytes [F: rfc9000, §14, §14.1].

**Perda e congestionamento (RFC 9002).** Números de pacote nunca se repetem numa conexão, o que elimina a ambiguidade de retransmissão do TCP e melhora a medição de RTT [F: rfc9002, §3, §4.2]. Perda é declarada por limiar de pacotes (3) ou de tempo (9/8 RTT) [F: rfc9002, §6.1.1, §6.1.2]. O PTO é SRTT + variância + max_ack_delay do peer; sua expiração não marca pacotes como perdidos, apenas envia sondas [F: rfc9002, §6.2, §6.2.1]. O controlador padrão é semelhante ao TCP NewReno; outros, como CUBIC, são permitidos seguindo a RFC 8085; janela inicial de 10 datagramas máximos; pacing recomendado [F: rfc9002, §7, §7.2, §7.7]. Retransmissão é de frames, não de pacotes [I].

**Datagramas não confiáveis.** A extensão da RFC 9221 (frames 0x30/0x31) oferece entrega não confiável dentro da conexão, sem retransmissão mas com ACK, sob o mesmo controle de congestionamento; ver rtm.proto.webtransport [F: rfc9221, §4, §5.2, §5.4].

**HTTP/3.** Cada requisição no seu stream bidirecional iniciado pelo cliente (streams 0, 4, 8, ...); QPACK substitui HPACK porque este assumia entrega em ordem; streams de controle com SETTINGS; ALPN "h3"; descoberta via Alt-Svc [F: rfc9114, §3.1, §4.1, §6.1, §6.2.1, §7.1]. CONNECT cria túnel num stream [F: rfc9114, §4.4]; o extended CONNECT da RFC 9220 permite WebSocket sobre HTTP/3 (ver rtm.proto.websocket).

## Requisitos e pressupostos

- UDP liberado na rede até o servidor; caso contrário, fallback a TCP [F: rfc9000, §14] [I].
- Certificado TLS; não existe QUIC sem autenticação do servidor [F: rfc9001, §4.4].
- A aplicação decide o que pode ir em 0-RTT, dado o risco de replay [F: rfc9001, §4.6].
- Implementação em user space na maioria dos ambientes, com custo de CPU maior que TCP em kernel [H].

## Vantagens e limitações

Vantagens [I]:
- Sem HOL blocking entre streams [F: rfc9114, §2].
- Handshake de 1 RTT, 0-RTT em reconexão [F: rfc9000, §7].
- Migração de conexão (Wi-Fi para celular) sem reconectar [F: rfc9000, §9].
- Detecção de perda mais precisa que TCP [F: rfc9002, §3, §4.5].
- Datagramas não confiáveis como extensão [F: rfc9221].

Limitações:
- HOL blocking persiste dentro de cada stream [F: rfc9000, §2.2] [I].
- Controle de congestionamento único por conexão, compartilhado por streams e datagramas [F: rfc9221, §5.4].
- Bloqueio de UDP em redes corporativas [I].
- Em navegador, só acessível via HTTP/3 e WebTransport; não há API QUIC bruta [I].

## Alternativas e comparações

| Critério | TCP | QUIC | SCTP (WebRTC) |
|---|---|---|---|
| Unidade | byte stream | streams de bytes + datagramas (ext.) | mensagens em streams |
| HOL entre fluxos | sim | não [F: rfc9114, §2] | não [F: rfc9260, §1.5.2] |
| Criptografia | externa | integrada TLS 1.3 [F: rfc9001] | DTLS externa [F: rfc8261] |
| Migração | não | sim [F: rfc9000, §9] | multihoming (não usado em WebRTC) [F: rfc8831, §5] |

## Exemplo técnico independente de domínio

```
cliente                                      servidor
 |-- Initial (ClientHello, transport params) ------>|
 |-- 0-RTT (dados, se sessão anterior) ----------->|
 |<-- Initial (ServerHello) + Handshake (cert...) --|
 |<-- 1-RTT (dados) -------------------------------|
 |-- Handshake (Finished) + 1-RTT (dados) --------->|   handshake confirmado

streams:
  stream 0  (bidi, cliente)  -> controle, confiável, ordenado
  stream 2  (uni, cliente)   -> upload de replay
  DATAGRAM frames            -> inputs e snapshots, não confiáveis
perda do pacote com stream 2 não atrasa o stream 0 nem os datagramas
```

Migração: o cliente muda de IP, envia pacote não-probing do novo endereço; o servidor inicia PATH_CHALLENGE; ao receber PATH_RESPONSE, continua a conexão no novo caminho [F: rfc9000, §9.3, §8.2] [I].

## Relações com outros conceitos

QUIC depende de rtm.proto.udp e é alternativa a rtm.proto.tcp. É a base de rtm.proto.webtransport e do WebSocket sobre HTTP/3 (rtm.proto.websocket). Segurança em rtm.sec.transport-security; migração e reconexão em rtm.rel.reconnection; ordenação por stream em rtm.net.ordering-and-reliability. Especificado pelas RFCs em rtm.std.index.

## Lacunas e questões abertas

- O texto da RFC 9000 recuperado não contém a frase "head-of-line"; a afirmação de ausência de HOL entre streams se apoia na RFC 9114 §1.1 e §2 e na independência de ordenação da RFC 9000 §2.
- Seção 9.2 da RFC 9001 (replay em 0-RTT) não foi lida; cita-se §4.6.
- Custo de CPU de QUIC em user space é hipótese sem fonte verificada aqui.
- Suporte de HTTP/3 em servidores e CDNs não foi verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc9000 | normativo | 2026-10-29 |
| rfc9001 | normativo | 2026-10-29 |
| rfc9002 | normativo | 2026-10-29 |
| rfc9114 | normativo | 2026-10-29 |
| rfc9221 | normativo | 2026-10-29 |
| rfc8446 | normativo (obsoleta) | 2026-10-29 |
| rfc9846 | normativo | 2026-10-29 |
| rfc9113 | normativo | 2026-10-29 |
| rfc8085 | normativo (BCP) | 2026-10-29 |
| rfc9260 | normativo | 2026-10-29 |
| rfc8261 | normativo | 2026-10-29 |
| rfc8831 | normativo | 2026-10-29 |
