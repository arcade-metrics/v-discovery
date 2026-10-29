---
id: rtm.net.ordering-and-reliability
titulo: Ordenação e confiabilidade (total, parcial, por canal; confiabilidade seletiva; bloqueio de cabeça de fila)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc9293, rfc768, rfc8085, rfc9000, rfc9114, rfc9221, rfc8831, rfc3758, rfc7496, rfc8260, rfc4737, mdn2026datachannel, oasis2019mqtt, fiedler2008udp, fiedler2008reliability, fiedler2014lockstep, lamport1978time]
relacoes:
  - { tipo: complementa, alvo: rtm.net.packet-loss }
  - { tipo: complementa, alvo: rtm.net.logical-clocks }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: implementado-por, alvo: rtm.proto.tcp }
  - { tipo: implementado-por, alvo: rtm.proto.udp }
  - { tipo: implementado-por, alvo: rtm.proto.quic }
  - { tipo: implementado-por, alvo: rtm.proto.webrtc }
  - { tipo: implementado-por, alvo: rtm.proto.webtransport }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
termos: [ordenação total, ordenação parcial, ordenação por canal, confiabilidade seletiva, head-of-line blocking, reliable ordered, reliable unordered, unreliable, ack bitfield, PR-SCTP, número de sequência]
---

# Ordenação e confiabilidade

## Definição e terminologia

Dois eixos independentes descrevem o serviço que um canal oferece [I]:

- **Confiabilidade**: a mensagem chega com certeza (retransmissão até ack), chega com esforço limitado (retransmissões ou tempo de vida limitados) ou chega se der (sem retransmissão).
- **Ordenação**: a mensagem é entregue na ordem de envio em relação a todas as outras (**total**, por fluxo), apenas em relação às do mesmo canal/stream (**por canal**), apenas respeitando causalidade (**parcial**, ver `rtm.net.logical-clocks`) ou em qualquer ordem.

TCP oferece "a reliable, in-order, byte-stream service" sobre um único fluxo [F: rfc9293, §2.2]. UDP não garante entrega nem proteção contra duplicatas [F: rfc768]; o RFC 8085 obriga aplicações que precisam de ordem a restaurá-la por conta própria [F: rfc8085, §3.3]. Fiedler nomeia as três combinações usuais em jogos ao descrever o que TCP dá (confiável e ordenado) e o que ele constrói sobre UDP (acks sem reenvio, ordem decidida pela aplicação) [F: fiedler2008reliability]; os canais de dados WebRTC expõem exatamente esses eixos: "reliable or unreliable message transmission" e "in-order or out-of-order message delivery" por mensagem [F: rfc8831, §6.4]. Na API do navegador, `ordered` (padrão `true`), `maxRetransmits` e `maxPacketLifeTime` (mutuamente exclusivos) configuram cada canal [F: mdn2026datachannel].

**Bloqueio de cabeça de fila** (*head-of-line blocking*, HOL): dados já recebidos não podem ser entregues porque um dado anterior na ordem ainda falta [I]. Fiedler descreve em TCP: dados novos "get put in a queue, and you cannot access it until that lost packet has been retransmitted" [F: fiedler2008udp]. O RFC 9114 explica que em HTTP/2 sobre TCP "a lost or reordered packet causes all active transactions to experience a stall" e que em QUIC "one stream that is blocked or suffers packet loss does not prevent progress on other streams" [F: rfc9114, §1.1, §2]; o RFC 9000 lista "avoidance of head-of-line blocking across multiple streams" como benefício [F: rfc9000, §13]. O RFC 8260 descreve a variante no emissor SCTP: mensagens grandes causam "a form of sender-side head-of-line blocking", resolvida pelo intercalamento de mensagens (chunk I-DATA) [F: rfc8260, §1.1].

## Problema que resolve

Escolher o par (confiabilidade, ordenação) por tipo de mensagem evita pagar latência por garantias que a mensagem não precisa. Fiedler: jogos enviam 10 a 30 pacotes por segundo e "only the most recent data is useful", então esperar retransmissão de estado antigo é desperdício [F: fiedler2008reliability].

## Fundamentos e funcionamento

### Ordenação total em um fluxo (TCP)

Cada octeto tem número de sequência; o ack de `X` indica que todos os octetos até `X − 1` chegaram [F: rfc9293, §3.4]. A entrega em ordem implica que um segmento perdido retém os seguintes até a retransmissão, cujo temporizador segue o RFC 6298 [F: rfc9293, §3.8.1; fiedler2008udp]. Reordenação na rede (causada por caminhos paralelos, balanceamento, retransmissão de camada 2, filas) pode disparar retransmissão espúria: 3-reordering faz um emissor NewReno retransmitir [F: rfc4737, §1.1, §5.4].

### Ordenação por canal (QUIC, SCTP, WebRTC)

QUIC oferece streams como "a lightweight, ordered byte-stream abstraction" e "does not provide any means of ensuring ordering between bytes on different streams" [F: rfc9000, §2]. SCTP com RFC 8260 permite escalonadores por stream: FCFS, round-robin, round-robin por pacote (uma perda afeta um só stream), prioridade, capacidade justa e WFQ (obrigatório para WebRTC) [F: rfc8260, §3]. [I] Ordenação por canal é o meio-termo: preserva ordem onde importa (chat, comandos de um mesmo objeto) e isola perdas entre canais.

### Confiabilidade seletiva (parcial)

PR-SCTP define serviço "partially reliable" em que o usuário especifica, por mensagem, "the rules governing how persistent" a transmissão deve ser; a política **timed reliability** abandona a mensagem quando expira o tempo de vida, e o chunk FORWARD TSN avança o ponto de ack cumulativo para liberar mensagens presas em filas de reordenação [F: rfc3758, §1.2, §3.2, §3.6, §4.1]. O RFC 7496 acrescenta a política de **retransmissões limitadas** (com limite 0 "behaves similarly to UDP") e a de **prioridade** [F: rfc7496, §3.1-3.2]. O RFC 8831 exige ambas e nota que "Limiting the number of retransmissions to zero, combined with unordered delivery, provides a UDP-like service" [F: rfc8831, §6.1].

### Sem confiabilidade, com feedback

QUIC DATAGRAM: sem retransmissão, mas confirmado e sob controle de congestionamento; a aplicação pode ser notificada de ack ou perda suspeita [F: rfc9221, §5.2]. Fiedler implementa o mesmo sobre UDP: cabeçalho com `sequence`, `ack` e `ack_bits` (32 bits), acks redundantes, perda inferida após 1 s, e "we leave it up to the application to compose a new packet containing the data that was lost" [F: fiedler2008reliability]. Para entradas em lockstep, a redundância substitui a retransmissão: todas as entradas não confirmadas vão em cada pacote [F: fiedler2014lockstep].

### Ordenação total entre processos

Quando várias fontes geram eventos, ordem por canal não basta para decidir "quem agiu primeiro". Lamport mostra que relógios lógicos dão uma ordem total `⇒` que estende a ordem causal `→`, desempatando por "any arbitrary total ordering < of the processes", e que essa ordem total "can be very useful in implementing a distributed system" [F: lamport1978time, §Ordering the Events Totally]. Ver `rtm.net.logical-clocks`.

## Algoritmos e modelos relevantes

- Comparação de sequência com wraparound: 16 bits bastam se a comparação tratar "0, 1, 2" como mais novos que 65535; a 30 pps, 16 bits dão a volta em cerca de meia hora, 32 bits em mais de quatro anos e meio [F: fiedler2008reliability].
- Ack bitfield: `ack` + 32 bits confirmam até 33 pacotes por cabeçalho [F: fiedler2008reliability].
- Detecção de perda por limiar de pacotes (3) e de tempo (9/8 RTT) em QUIC [F: rfc9002, §6.1].
- Nível de QoS por mensagem em pub/sub: "At most once", "At least once", "Exactly once" [F: oasis2019mqtt, Abstract].

## Requisitos e pressupostos

- Ordenação por canal exige que a aplicação particione mensagens em canais sem dependências cruzadas [I].
- Confiabilidade seletiva exige que a aplicação saiba a validade temporal de cada mensagem (tempo de vida ou número de tentativas) [F: rfc3758, §1.2].
- Qualquer esquema sobre UDP deve ser robusto a duplicatas por até 2 minutos (MSL) [F: rfc8085, §3.3]; Fiedler recomenda ids de mensagem para descartar duplicatas ao reenviar dados [F: fiedler2008reliability].

## Vantagens e limitações

| Serviço | Latência sob perda | HOL | Caso de uso [I] |
|---|---|---|---|
| reliable ordered (TCP, stream QUIC) | ≥ RTT por perda [F: fiedler2008udp] | sim, dentro do fluxo | chat, transações, estado inicial |
| reliable unordered (SCTP unordered, app sobre UDP) | ≥ RTT só para a mensagem perdida | não | eventos independentes (pickup, placar) |
| partially reliable (PR-SCTP) | limitada pelo tempo de vida [F: rfc3758] | configurável | posições com validade curta |
| unreliable (UDP, DATAGRAM, maxRetransmits=0) | nenhuma | não | estado substituível, entradas redundantes |

## Alternativas e comparações

Fiedler argumenta contra misturar TCP e UDP no mesmo protocolo de jogo, pois TCP "tends to induce packet loss in UDP packets", e recomenda construir confiabilidade seletiva sobre UDP [F: fiedler2008udp]. Em navegadores, a alternativa é escolher o transporte que exponha os eixos: WebRTC data channels ou WebTransport (`rtm.proto.webrtc`, `rtm.proto.webtransport`).

## Métricas e métodos de avaliação

Taxa de reordenação (`Type-P-Reordered`) [F: rfc4737, §3.3]; atraso de entrega à aplicação versus atraso de chegada (mede o HOL) [I]; taxa de mensagens abandonadas em PR-SCTP [F: rfc3758, §3.4].

## Exemplo técnico independente de domínio

Cabeçalho e lógica de confiabilidade seletiva sobre datagramas, no estilo de Fiedler:

```
cabecalho: { seq: u16, ack: u16, ack_bits: u32, canal: u8 }

ao receber(h):
    marcar_recebido(h.seq)                      # para compor ack/ack_bits de saída
    for i in 0..32: if h.ack_bits & (1<<i): confirmar(h.ack - 1 - i)
    confirmar(h.ack)
    switch canal:
        ORDENADO_CONFIAVEL:   enfileirar; entregar enquanto proximo_esperado presente
        CONFIAVEL_SEM_ORDEM:  entregar agora; registrar id para descartar duplicata
        NAO_CONFIAVEL:        if seq mais nova que ultima_vista: entregar; else descartar

a cada tick de envio:
    pacote = ultimo_estado()                     # dados não confiáveis: sempre o mais novo
    for m in mensagens_confiaveis_sem_ack(tempo > limite): pacote += m   # novo seq, mesmo id
    enviar(pacote)
```

"mais nova" usa comparação com wraparound [F: fiedler2008reliability].

## Relações com outros conceitos

Complementa `rtm.net.packet-loss` (a perda é o que a confiabilidade recupera) e `rtm.net.logical-clocks` (ordem parcial causal e ordem total entre processos); depende de `rtm.net.latency` (custo de cada retransmissão); é implementada por `rtm.proto.tcp`, `rtm.proto.udp`, `rtm.proto.quic`, `rtm.proto.webrtc`, `rtm.proto.webtransport`; relaciona-se a `rtm.rel.delivery-semantics` (semântica exposta à aplicação) e a `rtm.sync.crdt` (estruturas que dispensam ordenação total).

## Lacunas e questões abertas

- Nenhuma fonte normativa define o vocabulário "reliable ordered / reliable unordered / unreliable" como tal; ele é prática de engenharia (Fiedler, APIs WebRTC).
- Falta comparação medida de HOL entre WebSocket (TCP), WebTransport (QUIC) e WebRTC sob a mesma perda; ver `rtm.proto.comparison`.
- A relação entre ordenação por canal e ordenação causal entre canais não é coberta pelas RFCs; é tema de `rtm.net.logical-clocks`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc9293 | normativo | 2026-10-29 |
| rfc768 | normativo | 2026-10-29 |
| rfc8085 | normativo (BCP) | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| rfc9114 | normativo | 2026-10-29 |
| rfc9221 | normativo | 2026-10-29 |
| rfc8831 | normativo | 2026-10-29 |
| rfc3758 | normativo | 2026-10-29 |
| rfc7496 | normativo | 2026-10-29 |
| rfc8260 | normativo | 2026-10-29 |
| rfc4737 | normativo | 2026-10-29 |
| rfc9002 | normativo | 2026-10-29 |
| mdn2026datachannel | fornecedor | 2026-10-29 |
| oasis2019mqtt | normativo | 2026-10-29 |
| fiedler2008udp | tecnico | 2026-10-29 |
| fiedler2008reliability | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| lamport1978time | academico | 2026-10-29 |
