---
id: rtm.proto.tcp
titulo: TCP (Transmission Control Protocol)
tipo: protocolo
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc9293, rfc5681, rfc9438, rfc6298, rfc896, rfc9113, ieee2018posix]
relacoes:
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: depende-de, alvo: rtm.net.ordering-and-reliability }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: alternativa-a, alvo: rtm.proto.udp }
  - { tipo: alternativa-a, alvo: rtm.proto.quic }
  - { tipo: complementa, alvo: rtm.proto.websocket }
  - { tipo: complementa, alvo: rtm.proto.http-streaming }
  - { tipo: relacionado-a, alvo: rtm.proto.comparison }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
termos: [TCP, head-of-line blocking, Nagle algorithm, TCP_NODELAY, congestion window, RTO, byte stream]
---

# TCP (Transmission Control Protocol)

## Definição e terminologia

TCP é o protocolo de transporte orientado a conexão da pilha IP. A RFC 9293, que consolida a especificação original (RFC 793) e suas atualizações, define que "TCP provides a reliable, in-order, byte-stream service to applications" [F: rfc9293, §2.2]. A RFC 9293 é STD 7, com status Internet Standard, publicada em agosto de 2022, e obsoleta as RFCs 793, 879, 2873, 6093, 6429, 6528 e 6691 [F: rfc9293].

Termos usados neste documento:

- **byte stream**: a aplicação vê um fluxo contínuo de bytes sem fronteiras de mensagem; o bit PSH "is not a record marker and is independent of segment boundaries" [F: rfc9293, §3.9.1.2].
- **head-of-line (HOL) blocking**: bloqueio de dados já recebidos enquanto um segmento anterior perdido não é retransmitido [I].
- **Nagle algorithm**: coalescência de segmentos pequenos descrita na RFC 896 e normatizada na RFC 9293 §3.7.4.
- **TCP_NODELAY**: opção de socket que desativa Nagle; o nome vem da API de sockets POSIX, não da RFC [F: ieee2018posix].

O que TCP não é: não é um protocolo de mensagens, não oferece entrega parcial ou não ordenada e não expõe à aplicação controle sobre retransmissão [I].

## Problema que resolve

TCP resolve a entrega confiável e ordenada sobre uma rede que perde, duplica e reordena pacotes. A RFC define que perdas são detectadas por números de sequência, erros por checksum por segmento e corrigidas por retransmissão [F: rfc9293, §2.2]. O protocolo também resolve controle de fluxo (janela do receptor) e controle de congestionamento, este último obrigatório: "MUST implement the basic congestion control algorithms slow start, congestion avoidance" (MUST-19) [F: rfc9293, §3.8.2].

## Fundamentos e funcionamento

**Estabelecimento.** A conexão é aberta por three-way handshake com troca de segmentos SYN, em que cada lado confirma o número de sequência inicial do outro [F: rfc9293, §3.5]. Isso custa um RTT antes de a aplicação poder enviar dados [I].

**Cabeçalho.** Portas de origem e destino, número de sequência, número de reconhecimento, data offset, flags (CWR, ECE, URG, ACK, PSH, RST, SYN, FIN), janela, checksum, urgent pointer e opções; o checksum é obrigatório (MUST-2, MUST-3) [F: rfc9293, §3.1]. O espaço de sequência é de 32 bits, com comparação módulo 2^32, e os ACKs são cumulativos [F: rfc9293, §3.4].

**Confiabilidade.** O timer de retransmissão (RTO) "MUST be computed according to the algorithm in" RFC 6298 [F: rfc9293, §3.8.1]. A RFC 6298 define RTO = SRTT + max(G, K×RTTVAR), K = 4, RTO inicial de 1 segundo, arredondamento mínimo para 1 segundo quando o cálculo dá menos, e dobra do RTO a cada expiração (exponential backoff) [F: rfc6298, §2, §5.5]. O algoritmo de Karn proíbe amostras de RTT de segmentos retransmitidos, salvo com a opção timestamp [F: rfc6298, §3].

**Ordenação.** Segmentos são processados em ordem de SEG.SEQ; segmentos de número mais alto "SHOULD be held for later processing" (SHLD-31) e são remontados no buffer de recepção antes de serem devolvidos ao usuário [F: rfc9293, §3.10.7.4]. Daí decorre o HOL blocking: bytes posteriores a uma lacuna ficam retidos até a retransmissão chegar [I].

**Controle de congestionamento.** A RFC 5681 (Draft Standard) define slow start e congestion avoidance (§3.1), fast retransmit após três ACKs duplicados e fast recovery (§3.2); cwnd limita os dados não reconhecidos em voo e ssthresh é reduzido a max(FlightSize/2, 2×SMSS) em perda [F: rfc5681, §3.1, §3.2]. A RFC 9438 (CUBIC) atualiza a RFC 5681 e substitui o crescimento linear da janela por uma função cúbica [F: rfc9438].

**Controle de fluxo.** O receptor anuncia uma janela; "A TCP receiver SHOULD NOT shrink the window" (SHLD-14), e o emissor deve sondar janela zero (MUST-36) [F: rfc9293, §3.8.6]. ACK atrasado é recomendado (SHLD-18) com atraso "MUST be less than 0.5 seconds" (MUST-40) [F: rfc9293, §3.8.6.3].

**Nagle.** A RFC define: "If there is unacknowledged data (i.e., SND.NXT > SND.UNA), then the sending TCP endpoint buffers all user data (regardless of the PSH bit) until the outstanding data has been acknowledged or until the TCP endpoint can send a full-sized segment" [F: rfc9293, §3.7.4]. Implementações "SHOULD implement the Nagle algorithm" (SHLD-7), mas "there MUST be a way for an application to disable the Nagle algorithm on an individual connection" (MUST-17) [F: rfc9293, §3.7.4]. A motivação histórica está na RFC 896 (hoje Historic, obsoletada pela RFC 7805): o "small-packet problem", em que um byte de teclado gerava 41 bytes de pacote, cerca de 4000% de overhead [F: rfc896]. Na API de sockets POSIX, a opção `TCP_NODELAY` é definida como "Avoid coalescing of small segments" [F: ieee2018posix].

## Requisitos e pressupostos

- Caminho de rede com perda moderada; o controle de congestionamento interpreta perda como congestionamento [F: rfc5681, §3.2] [I].
- Aplicação tolera latência variável, pois retransmissão e RTO adicionam atrasos de pelo menos um RTT e, no pior caso, 1 segundo ou mais [F: rfc6298, §2.4] [I].
- Para tempo real, a aplicação precisa desativar Nagle (MUST-17) ou aceitar coalescência de pequenas mensagens [F: rfc9293, §3.7.4] [I].

## Vantagens e limitações

Vantagens [I]:
- Confiabilidade, ordenação e controle de congestionamento prontos; nenhum código de aplicação necessário.
- Atravessa NAT e firewalls de forma previsível; é o transporte de HTTP/1.1, HTTP/2 e WebSocket.
- Comportamento bem compreendido por middleboxes.

Limitações para tempo real de baixa latência:
- **HOL blocking**: um segmento perdido retém todos os bytes posteriores até a retransmissão [F: rfc9293, §3.10.7.4] [I]. A RFC 9113 (HTTP/2) reconhece explicitamente: "TCP head-of-line blocking is not addressed by this protocol" [F: rfc9113, §1].
- **RTO conservador**: piso de 1 segundo e backoff exponencial [F: rfc6298, §2.4, §5.5]; perda detectada só por timer pode custar segundos [I].
- **Nagle + delayed ACK**: Nagle retém dados até o ACK; o receptor pode atrasar o ACK até 0,5 s (MUST-40) [F: rfc9293, §3.7.4, §3.8.6.3]; a combinação atrasa pequenas mensagens frequentes, típicas de jogos [I].
- **Sem fronteiras de mensagem**: a aplicação precisa de framing próprio [F: rfc9293, §3.9.1.2] [I].
- **Handshake de 1 RTT** antes de qualquer dado [F: rfc9293, §3.5] [I].
- **Sem controle sobre retransmissão**: dados obsoletos (por exemplo, posição antiga) são retransmitidos mesmo quando já substituídos [I].

Quando TCP é adequado [I]: jogos por turnos, chat, lobby, matchmaking, transferência de assets, colaboração em documentos, e qualquer canal em que toda mensagem deve chegar e a latência de centenas de milissegundos é aceitável. O autor deste documento recomenda TCP (ou WebSocket sobre TCP) como canal de controle mesmo em jogos que usam UDP para estado.

## Alternativas e comparações

| Critério | TCP | UDP (rtm.proto.udp) | QUIC (rtm.proto.quic) |
|---|---|---|---|
| Confiabilidade | total [F: rfc9293, §2.2] | nenhuma [F: rfc768] | por stream; datagrams opcionais [F: rfc9000; rfc9221] |
| HOL blocking | sim, no fluxo inteiro [I] | não | só dentro de um stream [F: rfc9114, §2] |
| Handshake | 1 RTT [F: rfc9293, §3.5] | nenhum | 1 RTT ou 0-RTT [F: rfc9000, §7] |
| Criptografia | separada (TLS) | separada (DTLS) | integrada (TLS 1.3) [F: rfc9001] |

A comparação completa está em rtm.proto.comparison.

## Métricas e métodos de avaliação

Medir RTT suavizado (SRTT) e RTTVAR como na RFC 6298 [F: rfc6298, §2], contagem de retransmissões e tempo em zero-window. Para tempo real, o autor sugere medir a latência fim a fim de mensagens pequenas com e sem `TCP_NODELAY` sob perda emulada (ver rtm.perf.network-emulation).

## Exemplo técnico independente de domínio

Sequência de abertura e envio com Nagle desativado (pseudocódigo):

```
cliente                                servidor
  |---- SYN (seq=x) --------------------->|
  |<--- SYN,ACK (seq=y, ack=x+1) ---------|
  |---- ACK (ack=y+1) ------------------->|   conexão ESTABLISHED
  |
  setsockopt(sock, IPPROTO_TCP, TCP_NODELAY, 1)
  |
  loop a cada tick:
     msg = frame(len=2 bytes, payload)    # framing próprio, TCP não tem fronteiras
     send(sock, msg)                      # segue imediatamente, sem esperar ACK
```

Ilustração de HOL blocking: se os segmentos 1, 2 e 3 são enviados e o 1 se perde, o receptor retém 2 e 3 até receber a retransmissão de 1, mesmo que a aplicação pudesse usar 2 e 3 sozinhos [I].

## Relações com outros conceitos

TCP é especificado pelas RFCs indexadas em rtm.std.index. Depende dos conceitos de ordenação e confiabilidade (rtm.net.ordering-and-reliability) e de latência (rtm.net.latency). É alternativa a rtm.proto.udp e rtm.proto.quic, e serve de base para rtm.proto.websocket e rtm.proto.http-streaming. As semânticas de entrega que ele oferece são discutidas em rtm.rel.delivery-semantics.

## Lacunas e questões abertas

- A RFC 9293 não menciona `TCP_NODELAY` pelo nome; o nome vem do POSIX [F: ieee2018posix]. Comportamentos de "quick ACK" e de desativação de delayed ACK são específicos de sistema operacional e não foram verificados aqui.
- Não foi verificada literatura empírica sobre o impacto de HOL blocking em jogos; isso pertence a rtm.perf.qoe-thresholds.
- Algoritmos de controle de congestionamento modernos (BBR) não foram cobertos; só CUBIC tem RFC verificada [F: rfc9438].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc9293 | normativo | 2026-10-29 |
| rfc5681 | normativo | 2026-10-29 |
| rfc9438 | normativo | 2026-10-29 |
| rfc6298 | normativo | 2026-10-29 |
| rfc896 | normativo (Historic) | 2026-10-29 |
| rfc9113 | normativo | 2026-10-29 |
| ieee2018posix | normativo | 2026-10-29 |
