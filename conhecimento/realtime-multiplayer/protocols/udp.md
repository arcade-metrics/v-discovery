---
id: rtm.proto.udp
titulo: UDP (User Datagram Protocol)
tipo: protocolo
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc768, rfc9868, rfc8085, rfc8445, rfc8489, rfc8656, rfc9147, rfc9000, rfc7496, rfc8831, rfc8835, frindell2026webtransport]
relacoes:
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: depende-de, alvo: rtm.net.packet-loss }
  - { tipo: depende-de, alvo: rtm.net.ordering-and-reliability }
  - { tipo: alternativa-a, alvo: rtm.proto.tcp }
  - { tipo: complementa, alvo: rtm.proto.webrtc }
  - { tipo: complementa, alvo: rtm.proto.quic }
  - { tipo: complementa, alvo: rtm.proto.webtransport }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.sec.transport-security }
termos: [UDP, datagram, NAT traversal, STUN, TURN, ICE, selective reliability, hole punching]
---

# UDP (User Datagram Protocol)

## Definição e terminologia

UDP é o protocolo de transporte sem conexão da pilha IP, definido na RFC 768 de 28 de agosto de 1980, por J. Postel, STD 6, status Internet Standard [F: rfc768]. A RFC define: "The protocol is transaction oriented, and delivery and duplicate protection are not guaranteed" [F: rfc768]. A RFC 9868 (Proposed Standard, 2025) atualiza a RFC 768 definindo opções de transporte na "surplus area" após os dados do usuário [F: rfc9868].

Termos:

- **datagram**: unidade de envio com fronteiras preservadas; cada `send` vira um pacote [I].
- **selective reliability**: confiabilidade construída pela aplicação só para as mensagens que precisam [I].
- **NAT traversal / hole punching**: técnicas para dois hosts atrás de NAT trocarem UDP diretamente, padronizadas em ICE, STUN e TURN [F: rfc8445; rfc8489; rfc8656].

O que UDP não é: não é "TCP sem confiabilidade" apenas; também não tem controle de congestionamento nem de fluxo, e isso impõe obrigações à aplicação (ver Requisitos) [F: rfc8085, §3.1] [I].

## Problema que resolve

UDP dá à aplicação acesso quase direto ao serviço de datagramas do IP, com demultiplexação por porta e um checksum opcional em IPv4 [F: rfc768]. Para tempo real, isso resolve o problema central do TCP: a aplicação decide o que retransmitir, o que descartar e em que ordem entregar, sem head-of-line blocking imposto pelo transporte [I].

## Fundamentos e funcionamento

**Cabeçalho de 8 bytes.** Source Port (opcional, zero se não usado), Destination Port, Length (mínimo 8, inclui cabeçalho) e Checksum de 16 bits em complemento de um sobre um pseudo-cabeçalho, o cabeçalho UDP e os dados; "An all zero transmitted checksum value means that the transmitter generated no checksum" [F: rfc768]. A RFC 8085 orienta a habilitar o checksum; sobre IPv6 ele é obrigatório, salvo o modo zero-checksum para túneis [F: rfc8085, §3.4, §3.4.1].

**Sem estado.** Não há handshake; o primeiro datagrama já carrega dados. Não há números de sequência, ACKs ou janelas [F: rfc768] [I].

**Tamanho de mensagem.** A RFC 8085 (BCP 145) recomenda não exceder o path MTU; sem informação de PMTU, usar 576 bytes em IPv4 e 1280 em IPv6 como MTU efetiva [F: rfc8085, §3.2]. QUIC, que roda sobre UDP, exige que o caminho suporte datagramas de pelo menos 1200 bytes [F: rfc9000, §14].

**NAT e keep-alives.** NATs devem manter estado por pelo menos 2 minutos, mas muitos middleboxes usam timeouts menores; keep-alives, quando necessários, não devem ser mais frequentes que a cada 15 segundos, com jitter aleatório [F: rfc8085, §3.5].

**NAT traversal.** ICE (RFC 8445) coleta candidatos host, server-reflexive (mapeamento público aprendido via STUN), relayed (TURN) e peer-reflexive, e testa pares com STUN Binding requests [F: rfc8445, §2.1, §5.1.1, §7.2.4]. STUN (RFC 8489) permite descobrir o endereço refletido; "is not a NAT traversal solution by itself"; portas padrão 3478 (UDP/TCP) e 5349 (TLS/DTLS); magic cookie 0x2112A442 [F: rfc8489, §1, §5, §8.1]. TURN (RFC 8656) é o relay de último recurso: "it is best to use a TURN server only when a direct communication path cannot be found"; hole punching falha quando ambos os lados estão atrás de NAT com mapeamento dependente de endereço ou de endereço e porta [F: rfc8656, §1]. Alocações TURN duram 10 minutos por padrão e são renovadas com Refresh [F: rfc8656, §3.2]. Send/Data indications acrescentam 36 bytes por pacote, motivo de existirem ChannelData com cabeçalho de 4 bytes [F: rfc8656, §3.5].

**Segurança.** UDP não oferece confidencialidade; DTLS 1.3 (RFC 9147) fornece segurança equivalente a TLS 1.3 sobre datagramas, "except for order protection and non-replayability", com epoch e sequence number explícitos por registro e janela anti-replay [F: rfc9147, §1, §4, §4.5.1].

## Algoritmos e modelos relevantes

Construir confiabilidade seletiva sobre UDP exige, no mínimo [I]:

1. Número de sequência por pacote e bitfield de ACKs (por exemplo, os 32 últimos) piggybacked em cada pacote.
2. Política por mensagem: descartar se obsoleta, reenviar até N vezes ou até expirar lifetime; essa é a taxonomia que SCTP (RFC 3758, RFC 7496) e os WebRTC data channels formalizam [F: rfc7496, §3.1].
3. Controle de congestionamento ou limitação de taxa: a RFC 8085 diz que aplicações sem transporte congestion-controlled devem limitar a taxa; aplicações de baixo volume não devem exceder em média um datagrama por RTT, e sem estimativa de RTT, um a cada 3 segundos [F: rfc8085, §3.1, §3.1.3].

## Requisitos e pressupostos

- A aplicação tolera perda, duplicação e reordenação, "for up to the 2-minute TCP MSL" [F: rfc8085, §3.3].
- A aplicação implementa controle de congestionamento ou circuit breaker [F: rfc8085, §3.1, §3.1.10].
- Para P2P, há servidor STUN e, para NATs restritivos, servidor TURN [F: rfc8656, §1].
- Em navegadores, UDP bruto não está disponível: só por WebRTC data channels (SCTP sobre DTLS sobre UDP) ou WebTransport (QUIC sobre UDP) [F: rfc8831, §5; frindell2026webtransport] [I].

## Vantagens e limitações

Vantagens [I]:
- Latência mínima: sem handshake, sem retransmissão obrigatória, sem HOL blocking.
- Fronteiras de mensagem preservadas.
- Controle total de reliability e ordering por mensagem.

Limitações:
- Nada é garantido: entrega, ordem, deduplicação [F: rfc768].
- A aplicação assume as obrigações de BCP 145 [F: rfc8085].
- Bloqueio por firewalls corporativos; a RFC 8835 exige TURN sobre TCP e TLS justamente para "UDP-blocking firewalls" [F: rfc8835, §3.4].
- Indisponível em navegadores sem WebRTC ou WebTransport [I].

## Alternativas e comparações

Ver tabela em rtm.proto.comparison. Em resumo: TCP quando tudo deve chegar em ordem; QUIC quando se quer streams independentes com criptografia integrada e, com RFC 9221, datagramas não confiáveis; WebRTC data channel para P2P em navegador [I].

## Métricas e métodos de avaliação

Perda unidirecional conforme RFC 7680 (Type-P-One-way-Packet-Loss) e variação de atraso (IPDV) conforme RFC 3393 são as métricas padronizadas; ver rtm.net.packet-loss, rtm.net.jitter e rtm.perf.metrics [I].

## Exemplo técnico independente de domínio

Cabeçalho de aplicação mínimo para confiabilidade seletiva sobre UDP (pseudocódigo):

```
struct Header {
  uint16 seq;        // sequência deste pacote
  uint16 ack;        // maior seq recebida do peer
  uint32 ack_bits;   // bit i = 1 se (ack - i - 1) foi recebido
}

on_send(payload, policy):
  pkt = Header{seq=next_seq++, ack=last_recv, ack_bits=recv_mask} + payload
  if policy == RELIABLE: pending[pkt.seq] = (pkt, retries=0, t=now)
  udp.send(pkt)

on_receive(pkt):
  update(recv_mask, pkt.seq)
  for each seq confirmed by (pkt.ack, pkt.ack_bits): pending.remove(seq)

on_tick():
  for (seq, entry) in pending:
    if now - entry.t > rto and entry.retries < MAX: resend(entry)
    elif entry.retries >= MAX: abandon(seq)   # equivalente a PR-SCTP limited retransmissions
```

Fluxo ICE simplificado: cada peer obtém candidatos (host, STUN reflexive, TURN relayed), troca-os via sinalização, envia STUN Binding em cada par; o par que responde primeiro com maior prioridade é nomeado pelo agente controlling [F: rfc8445, §2.2, §8.1.1] [I].

## Relações com outros conceitos

UDP é especificado pelas RFCs em rtm.std.index. Depende dos conceitos de perda (rtm.net.packet-loss) e de ordenação (rtm.net.ordering-and-reliability). É alternativa a rtm.proto.tcp e base de rtm.proto.quic, rtm.proto.webtransport e rtm.proto.webrtc. As semânticas de entrega que a aplicação constrói sobre ele são tratadas em rtm.rel.delivery-semantics; arquiteturas P2P que dependem de NAT traversal, em rtm.arch.peer-to-peer; DTLS, em rtm.sec.transport-security.

## Lacunas e questões abertas

- A RFC 768 não tem seções numeradas; as citações apontam ao documento inteiro.
- Não foram verificadas as estatísticas de sucesso de hole punching por tipo de NAT; isso é relevante para decidir investimento em TURN.
- O artigo de Glenn Fiedler sobre reliability over UDP (fonte prioritária do brief) não foi consultado neste documento; pertence a rtm.net.ordering-and-reliability.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc768 | normativo | 2026-10-29 |
| rfc9868 | normativo | 2026-10-29 |
| rfc8085 | normativo (BCP) | 2026-10-29 |
| rfc8445 | normativo | 2026-10-29 |
| rfc8489 | normativo | 2026-10-29 |
| rfc8656 | normativo | 2026-10-29 |
| rfc9147 | normativo | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| rfc7496 | normativo | 2026-10-29 |
| rfc8831 | normativo | 2026-10-29 |
| rfc8835 | normativo | 2026-10-29 |
| frindell2026webtransport | normativo (Internet-Draft) | 2026-10-29 |
