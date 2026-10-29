---
id: rtm.net.packet-loss
titulo: Perda de pacotes (causas, perda em rajada, Gilbert-Elliott, efeitos em TCP e UDP, retransmissão, FEC e redundância)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc7680, rfc3611, rfc2330, rfc8085, rfc768, rfc9293, rfc6298, rfc9002, rfc9221, rfc2198, rfc6363, rfc4737, gilbert1960capacity, elliott1963estimates, hasslinger2008gilbert, wikipedia2026burst, fiedler2008udp, fiedler2008reliability, fiedler2014lockstep, fiedler2014snapshot, fiedler2016fragmentation]
relacoes:
  - { tipo: complementa, alvo: rtm.net.latency }
  - { tipo: complementa, alvo: rtm.net.jitter }
  - { tipo: complementa, alvo: rtm.net.ordering-and-reliability }
  - { tipo: relacionado-a, alvo: rtm.proto.tcp }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.proto.quic }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: avaliado-por, alvo: rtm.perf.network-emulation }
termos: [perda de pacotes, loss ratio, perda em rajada, Gilbert-Elliott, retransmissão, FEC, redundância, Tmax, RTO, fragmentação]
---

# Perda de pacotes

## Definição e terminologia

O RFC 7680 define `Type-P-One-way-Packet-Loss` como valor binário: 0 se o pacote foi recebido, 1 se o destino não o recebeu dentro do tempo de espera `Tmax` [F: rfc7680, §2.3-2.4]. A RFC conta como perdido um pacote corrompido ("If the packet arrives but is corrupted, then it is counted as lost") e um pacote cuja remontagem de fragmentos falha; cópias duplicadas não corrompidas contam como recebido [F: rfc7680, §2.5]. A estatística `Type-P-One-way-Packet-Loss-Ratio` é a média dos valores, isto é, a razão entre perdas e total [F: rfc7680, §4.1]. O RFC 7680 é Internet Standard (STD 82) e obsoleta o RFC 2680 [F: rfc7680].

**Perda em rajada** (*burst loss*): sequência de perdas próximas. O RFC 3611 define *burst* via o parâmetro `Gmin` (recomendado 16): a mais longa sequência que começa e termina em pacote perdido ou descartado e não contém `Gmin` ou mais pacotes consecutivos recebidos; *gap* é o período entre rajadas; derivam-se *burst density*, *gap density*, *burst duration* e *gap duration* [F: rfc3611, §4.7.2].

**Reordenação não é perda**: o RFC 4737 afirma que "losses alone do not cause subsequent packets to be declared reordered" e que protocolos devem lidar com ambas [F: rfc4737, §1, §6].

## Problema que resolve

Caracterizar a perda (taxa, distribuição temporal, correlação) determina qual estratégia de recuperação é viável dentro do orçamento de latência: retransmitir custa pelo menos um RTT; FEC e redundância custam banda; ignorar custa qualidade [I].

## Fundamentos e funcionamento

### Causas

O RFC 7680 conta como perda qualquer não chegada dentro de `Tmax`, o que inclui descarte por fila cheia, corrupção e falha de remontagem [F: rfc7680, §2.5-2.6]. Haßlinger e Hohlfeld listam corrupção por erros de bit, reduções temporárias de capacidade em enlaces sem fio e descarte em roteadores "in phases of overload" [F: hasslinger2008gilbert, §1]. Fragmentação agrava: Fiedler mostra que, se qualquer fragmento se perde, o pacote inteiro se perde, e com 1% de perda por fragmento a probabilidade sobe para ≈2% com 2 fragmentos, ≈9,5% com 10 e ≈63,4% com 100 (`1 − 0,99^n`) [F: fiedler2016fragmentation]. O RFC 8085 recomenda não exceder o MTU do caminho e, sem descoberta de PMTU, usar 1280 bytes em IPv6 e o menor entre 576 bytes e o MTU do primeiro salto em IPv4 [F: rfc8085, §3.2]. Fiedler relata perda típica de 1 a 5% em UDP na Internet [F: fiedler2008udp].

### Modelo de Gilbert-Elliott

Gilbert (1960) propôs um canal com memória como cadeia de Markov de dois estados; Elliott (1963) estendeu o modelo para estimar taxas de erro de códigos [F: gilbert1960capacity; elliott1963estimates; apenas os registros bibliográficos foram abertos]. Na formulação de Haßlinger e Hohlfeld, o modelo gera erros como eventos independentes com taxa `1 − k` no estado bom (G) e `1 − h` no estado ruim (B), transições `p = P(B | G)` e `r = P(G | B)`, e os tempos de permanência são geométricos com médias `(1 − p)/p` e `(1 − r)/r`; "we interpret an event as the arrival of a packet and an error as a packet loss" [F: hasslinger2008gilbert, §3]. Gilbert tratou o caso especial de estado bom sem erros (`k = 1`) [F: hasslinger2008gilbert, §3; wikipedia2026burst]. Os autores ajustaram o modelo a traços de um roteador de acesso de 2,5 Gb/s e concluem que "simple Markov models are appropriate to capture the observed loss pattern" [F: hasslinger2008gilbert, Abstract, §2].

```
        p
   G ------> B        G: perde com prob. 1-k (Gilbert: k = 1)
   ^         |        B: perde com prob. 1-h
   +---------+        P(B) estacionária = p/(p+r)
        r             comprimento médio de rajada em B = 1/r   [I, derivado]
```

### Efeito em TCP

TCP "provides a reliable, in-order, byte-stream service", detecta perda por números de sequência e corrige por retransmissão [F: rfc9293, §2.2, §3.8]. O temporizador de retransmissão é `RTO = SRTT + max(G, 4·RTTVAR)`, com mínimo recomendado de 1 s e duplicação a cada expiração [F: rfc6298, §2.4, §5.5]. Reordenação também dispara retransmissão: para `n = 3`, "a NewReno TCP sender would retransmit 1 packet in response to an instance of 3-reordering" [F: rfc4737, §5.4]. Fiedler descreve a consequência para dados sensíveis ao tempo: detectar a perda leva pelo menos um RTT, "commonly it takes 2*RTT", mais uma viagem para a retransmissão; com ping de 125 ms, cerca de 1/5 s de espera no melhor caso; dados novos ficam enfileirados atrás do pacote perdido [F: fiedler2008udp]. Em lockstep sobre TCP a 100 ms e 1% de perda ele observou travadas "every few seconds" [F: fiedler2014lockstep].

### Efeito em UDP

UDP não garante entrega nem proteção contra duplicatas [F: rfc768]. O RFC 8085 exige que aplicações que precisam de confiabilidade a implementem ou usem TCP/SCTP, que restaurem ordenação por conta própria, que sejam robustas a duplicatas dentro do MSL de 2 minutos, e recomenda, para quem envia cópias redundantes (por exemplo três), espaçá-las por vários RTTs [F: rfc8085, §3.3, §3.1.6]. QUIC também não retransmite pacotes inteiros: "the information that might be carried in frames is sent again in new frames as needed" [F: rfc9000, §13.3], e os DATAGRAM frames "are not retransmitted upon loss detection" embora sejam confirmados e sujeitos ao controle de congestionamento [F: rfc9221, §5.2, §5.4].

## Algoritmos e modelos relevantes

### Retransmissão seletiva na aplicação

Fiedler propõe sequência + ack + bitfield de 32 acks anteriores por pacote, acks redundantes ("you would have to lose 100% of packets for more than a second to stop an ack getting through"), perda inferida após 1 s sem ack, e **nunca reenviar o mesmo pacote**: a aplicação compõe um pacote novo com os dados que ainda importam [F: fiedler2008reliability]. QUIC declara perda por limiar de pacotes (`kPacketThreshold = 3`) ou de tempo (`9/8` do RTT) [F: rfc9002, §6.1].

### Redundância

Envio repetido de entradas até o ack: em lockstep, cada pacote carrega todas as entradas ainda não confirmadas; com RTT de 30 a 250 ms isso dá 2 a 15 quadros por pacote, e o pior caso (2 s) são 120 entradas de 6 bits, "only 90 bytes of input" [F: fiedler2014lockstep]. O RFC 2198 formaliza o mesmo princípio para áudio: cada pacote carrega cópias (em geral de menor qualidade) de dados anteriores, de modo que a perda "may be reconstructed at the receiver from the redundant data"; funciona quando "the average number of consecutively lost packets is small", e redundância excessiva "will increase network congestion, and hence packet loss" [F: rfc2198, §1, §3, §6].

### FEC

O RFC 6363 define o arcabouço: pacotes-fonte, pacotes de reparo gerados por um esquema FEC, aplicável onde "real-time, scalability, or other constraints prohibit the use of higher-layer feedback"; a banda de reparo não deve exceder a dos dados originais; o receptor pode precisar bufferizar até os reparos chegarem, e o atraso de decodificação pode tornar os dados inúteis para tempo real [F: rfc6363, §1, §2, §4.1, §8.1-8.2, §10.2].

### Ignorar

Para estado que é substituído pelo próximo, a melhor estratégia é não recuperar: Fiedler mostra que snapshots perdidos são pulados pelo buffer de interpolação, ao custo de atraso suficiente para dois pacotes consecutivos perdidos [F: fiedler2014snapshot].

## Requisitos e pressupostos

- Retransmissão requer feedback e pelo menos um RTT de folga no orçamento [F: fiedler2008udp].
- Redundância e FEC pressupõem rajadas curtas em relação à janela de redundância [F: rfc2198, §1].
- Qualquer estratégia precisa de controle de congestionamento: aplicações UDP "SHOULD control the rate" e, enviando mais que alguns datagramas por RTT, implementar TFRC ou equivalente [F: rfc8085, §3.1, §3.1.2].

## Vantagens e limitações

| Estratégia | Custo em latência | Custo em banda | Rajadas longas |
|---|---|---|---|
| retransmissão | ≥ 1 RTT (TCP: até 2 RTT + ida) [F: fiedler2008udp] | baixo | tolera, com atraso crescente |
| redundância de entradas | nenhum extra | proporcional ao RTT [F: fiedler2014lockstep] | tolera até o timeout |
| FEC em bloco | espera do bloco [F: rfc6363, §4.1] | ≤ 100% dos dados [F: rfc6363, §8.2] | falha se a rajada exceder a capacidade do código [I] |
| ignorar + buffer | k·intervalo [F: fiedler2014snapshot] | nenhum | perda visível além de k pacotes |

## Alternativas e comparações

Ver `rtm.net.ordering-and-reliability` para a combinação de perda com ordenação (confiável ordenado, confiável não ordenado, não confiável) e `rtm.rel.delivery-semantics` para a semântica exposta à aplicação.

## Métricas e métodos de avaliação

Loss ratio [F: rfc7680, §4.1]; densidade e duração de rajadas e gaps, taxa de descarte [F: rfc3611, §4.7]; parâmetros `p`, `r`, `k`, `h` ajustados a traços [F: hasslinger2008gilbert]. Emulação com Gilbert-Elliott é o método usual em `rtm.perf.network-emulation` [I].

## Exemplo técnico independente de domínio

Emulador de perda em rajada (Gilbert simplificado, `k = 1`):

```
estado = G
para cada pacote:
    if estado == G: perder = False; if rand() < p: estado = B
    else:           perder = rand() < (1 - h); if rand() < r: estado = G
```

Com `p = 0,01`, `r = 0,5`, `h = 0`: perda média `P(B) = p/(p+r) ≈ 2%`, rajadas de 2 pacotes em média [I, derivado da formulação de hasslinger2008gilbert].

## Relações com outros conceitos

Complementa `rtm.net.latency` e `rtm.net.jitter` (pacote tardio = perdido para a aplicação) e `rtm.net.ordering-and-reliability`; relaciona-se aos transportes `rtm.proto.tcp`, `rtm.proto.udp`, `rtm.proto.quic`; às técnicas que convivem com perda, `rtm.arch.deterministic-lockstep` e `rtm.sync.snapshot-interpolation`; à semântica `rtm.rel.delivery-semantics`; e é reproduzida em `rtm.perf.network-emulation`.

## Lacunas e questões abertas

- Os textos de Gilbert (1960) e Elliott (1963) não foram abertos (acesso bloqueado em três editoras); somente os registros Crossref. A descrição do modelo vem de Haßlinger e Hohlfeld (2008) e de fonte secundária.
- O RFC 2198 e o RFC 6363 cobrem mídia; não foi localizada fonte normativa sobre FEC aplicada a estado de jogo.
- Não há dados verificados sobre distribuição de rajadas em redes móveis atuais; o traço de Haßlinger e Hohlfeld é de acesso ADSL em 2008.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc7680 | normativo | 2026-10-29 |
| rfc3611 | normativo | 2026-10-29 |
| rfc2330 | normativo (informativo) | 2026-10-29 |
| rfc8085 | normativo (BCP) | 2026-10-29 |
| rfc768 | normativo | 2026-10-29 |
| rfc9293 | normativo | 2026-10-29 |
| rfc6298 | normativo | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| rfc9002 | normativo | 2026-10-29 |
| rfc9221 | normativo | 2026-10-29 |
| rfc2198 | normativo | 2026-10-29 |
| rfc6363 | normativo | 2026-10-29 |
| rfc4737 | normativo | 2026-10-29 |
| gilbert1960capacity | academico (registro Crossref) | 2026-10-29 |
| elliott1963estimates | academico (registro Crossref) | 2026-10-29 |
| hasslinger2008gilbert | academico | 2026-10-29 |
| wikipedia2026burst | secundario | 2026-10-29 |
| fiedler2008udp | tecnico | 2026-10-29 |
| fiedler2008reliability | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2016fragmentation | tecnico | 2026-10-29 |
