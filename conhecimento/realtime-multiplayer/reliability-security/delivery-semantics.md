---
id: rtm.rel.delivery-semantics
titulo: Semânticas de entrega de mensagens
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [kafka2026semantics, oasis2019mqtt, rfc9147, rfc7519, fiedler2008reliability, rfc8446, colyseus2026connection]
relacoes:
  - { tipo: depende-de, alvo: rtm.net.ordering-and-reliability }
  - { tipo: depende-de, alvo: rtm.net.packet-loss }
  - { tipo: complementa, alvo: rtm.rel.reconnection }
  - { tipo: complementa, alvo: rtm.rel.fault-tolerance }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.proto.tcp }
  - { tipo: relacionado-a, alvo: rtm.arch.event-driven }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [at-most-once, at-least-once, exactly-once, idempotência, deduplicação, sequence number, ack, replay]
---

# Semânticas de entrega de mensagens

## Definição e terminologia

Semântica de entrega é a garantia que o sistema oferece sobre quantas vezes uma mensagem enviada é *processada* pelo destinatário diante de perda, reenvio e falha. A documentação do Kafka dá as três definições canônicas: "At most once — Messages may be lost but are never redelivered"; "At least once — Messages are never lost but may be redelivered"; "Exactly once — Each message is processed once and only once" [F: kafka2026semantics]. A especificação MQTT 5.0 usa os mesmos nomes para seus níveis de QoS 0, 1 e 2 [F: oasis2019mqtt, §3.3.1.2].

O ponto que a documentação do Kafka ressalta é que a questão "breaks down into two problems: the durability guarantees for publishing a message and the guarantees when consuming a message" [F: kafka2026semantics]: a garantia é uma propriedade de ponta a ponta, que envolve produtor, transporte e consumidor, não só do canal.

Termos auxiliares: **idempotência** (aplicar a mesma mensagem duas vezes produz o mesmo efeito que aplicá-la uma vez); **deduplicação** (descartar cópias já vistas, identificadas por id ou número de sequência); **sequence number** (contador monotônico por emissor que permite ordenar, detectar lacunas e deduplicar); **ack** (confirmação de recebimento).

## Problema que resolve

Em tempo real, mensagens se perdem (UDP, quedas de WebSocket) e, para compensar, são reenviadas; reenviar cria duplicatas. Uma entrada de jogador aplicada duas vezes (um disparo, um lance, uma edição) corrompe o estado; uma entrada perdida sem aviso dessincroniza o cliente. Escolher a semântica por tipo de mensagem, e implementá-la de verdade, é o que separa "parece funcionar na rede local" de "funciona com perda e reconexão".

## Fundamentos e funcionamento

### As três semânticas e o que cada uma exige

- **At-most-once** é o que se obtém sem fazer nada: enviar e esquecer. No lado consumidor, corresponde a gravar a posição *antes* de processar; no Kafka, se o consumidor "crashes after processing messages but before saving its position", o padrão oposto gera reprocessamento, logo salvar antes gera perda [F: kafka2026semantics]. Adequado a dados substituídos pela próxima mensagem: posições, snapshots, presença "digitando" [I].
- **At-least-once** exige reenvio até ack. O Kafka descreve que, antes da versão 0.11.0.0, um produtor sem resposta "had little choice but to resend the message", o que "provides at-least-once delivery semantics since the message may be written to the log again" [F: kafka2026semantics]. No MQTT, QoS 1 é "At least once delivery" com PUBACK, e o emissor "MUST set DUP to 1" ao reenviar um PUBLISH [F: oasis2019mqtt, §3.3.1.1, §3.4]. Adequado a eventos que não podem se perder, desde que o receptor tolere duplicatas.
- **Exactly-once** não é propriedade do canal; é at-least-once no transporte mais deduplicação ou idempotência no receptor. O Kafka implementa isso no produtor: "the broker assigns each producer an ID and deduplicates messages using a sequence number that is sent by the producer along with every message", e, para consumo com efeitos externos, armazena o offset "in the same place as its output" ou usa transações [F: kafka2026semantics]. O MQTT QoS 2 usa o handshake de quatro passos PUBLISH, PUBREC, PUBREL, PUBCOMP, com o mesmo Packet Identifier em todos [F: oasis2019mqtt, §2.2.1, §3.5-3.7]. A documentação do Kafka também observa o atalho comum: "In many cases messages have a primary key and so the updates are idempotent" [F: kafka2026semantics].

### Sequence numbers: ordenação, lacunas e deduplicação

O mesmo contador resolve três problemas. Fiedler descreve, para UDP, um esquema em que cada pacote carrega número de sequência, e os acks são enviados de forma redundante: cada pacote leva o último ack mais um bitfield de 32 bits cobrindo as 32 sequências anteriores, de modo que a perda de um pacote não impede que o ack chegue; pacotes sem ack em cerca de um segundo são considerados perdidos; e "we never resend a packet with a given sequence number" (reenvia-se o *conteúdo* num pacote novo) [F: fiedler2008reliability]. O autor também fundamenta por que TCP não serve para o caso: "if a packet is lost, TCP has to stop and wait for that packet to be resent", atrasando tudo que vem depois [F: fiedler2008reliability]. Ver `rtm.net.ordering-and-reliability` para o tratamento completo.

O DTLS 1.3 ilustra o mesmo padrão em outra camada: "Each DTLS record contains a sequence number to provide replay protection", com detecção de replay opcional, porque "Datagram transport neither requires nor provides reliable or in-order delivery" [F: rfc9147, §3, §4.5.1].

### Deduplicação por id

Quando as mensagens não vêm de um único fluxo sequencial (por exemplo, comandos reenviados após reconexão por caminhos diferentes), usa-se um identificador único por mensagem e uma janela de ids já vistos. A RFC 7519 define o claim `jti` do JWT com essa função: "provides a unique identifier for the JWT" e "can be used to prevent the JWT from being replayed" [F: rfc7519, §4.1.7]. O padrão é o mesmo para comandos de aplicação: id gerado pelo cliente, tabela de vistos no servidor com expiração [I].

### Reconexão e replay

Após uma queda, o cliente informa o último número de sequência recebido e o servidor reenvia o que falta a partir de um buffer de saída; o Colyseus, por exemplo, enfileira `room.send()` durante a desconexão (até `maxEnqueuedMessages`, padrão 10) e os envia ao reconectar [F: colyseus2026connection]. [I] Esse reenvio é at-least-once por natureza: se a queda ocorreu depois que o servidor processou a mensagem mas antes do ack, o cliente reenviará; o servidor precisa deduplicar pela sequência do cliente. Ver `rtm.rel.reconnection`.

### Escolha por tipo de mensagem

| Tipo de mensagem | Semântica recomendada [I] | Mecanismo |
|---|---|---|
| Estado contínuo (posição, cursor) | at-most-once | último vence; sequence para descartar atrasados |
| Entrada do jogador (disparo, lance) | exactly-once efetivo | at-least-once + dedup por (cliente, seq) |
| Evento de sala (entrou, saiu) | at-least-once | ack + reenvio; receptor idempotente |
| Transação (compra, pontuação final) | exactly-once | id único + registro durável antes do efeito |
| Chat | at-least-once | dedup por id de mensagem no cliente |

## Requisitos e pressupostos

- Deduplicação exige memória no receptor: janela por emissor (sequence) ou conjunto de ids com expiração. O tamanho da janela limita por quanto tempo uma duplicata tardia é reconhecida.
- Sequence numbers são por emissor e por fluxo; misturar fluxos num contador único quebra a detecção de lacunas [I].
- Contadores de largura fixa dão a volta; comparações precisam tratar wrap-around [F: fiedler2008reliability].
- Exactly-once com efeitos externos (banco, pagamento) exige que o registro de "já processado" seja atômico com o efeito, como a documentação do Kafka descreve para offsets e saída [F: kafka2026semantics].

## Vantagens e limitações

- At-most-once é barato e correto para dados substituíveis; aplicá-lo a comandos produz perdas silenciosas.
- At-least-once sem deduplicação é o erro mais comum: funciona até a primeira retransmissão real [I].
- Exactly-once ponta a ponta custa memória e, se envolve persistência síncrona, latência; o Kafka relata que esperar o commit "can take on the order of 10 ms" no seu contexto [F: kafka2026semantics], número ilustrativo de outra classe de sistema.
- Ordem total entre emissores diferentes não decorre de sequence numbers por emissor; exige relógio lógico ou serialização no servidor (ver `rtm.net.logical-clocks`).

## Alternativas e comparações

Transporte confiável (TCP, WebSocket) entrega at-least-once *na camada de bytes* enquanto a conexão vive, e nada após a queda; é por isso que a semântica precisa ser reconstruída na aplicação quando há reconexão [I]. Brokers (Kafka, MQTT) oferecem as três semânticas como configuração explícita e servem de referência de vocabulário, mas introduzem um salto adicional incompatível com orçamentos de latência de jogos de ação [H].

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`: taxa de duplicatas detectadas, taxa de lacunas de sequência, tempo até ack (p50/p95/p99), tamanho médio e máximo da janela de dedup, mensagens reenviadas por reconexão. Em `rtm.perf.network-emulation`, cenários de perda e duplicação (netem `loss`, `duplicate`) são os que expõem falhas de semântica.

## Exemplo técnico independente de domínio

```text
# Emissor: at-least-once com sequence e reenvio por timeout
seq = 0 ; unacked = {}
send(cmd):   seq += 1 ; msg = {seq, id: uuid(), cmd} ; unacked[seq] = msg ; transmit(msg)
on_ack(n):   remove unacked[k] for k <= n            # ack cumulativo
every 200ms: for m in unacked older than RTO: transmit(m)   # mesmo seq, mesmo id

# Receptor: deduplicação e ordenação por emissor
expected[client] = 1 ; seen_ids = lru_set(ttl = 60 s)
on_receive(client, msg):
    if msg.id in seen_ids: send_ack(client, msg.seq) ; return      # duplicata
    if msg.seq < expected[client]: send_ack(client, msg.seq) ; return
    buffer[client].insert(msg)
    while buffer[client].has(expected[client]):
        m = buffer[client].pop(expected[client])
        apply(m.cmd) ; seen_ids.add(m.id) ; expected[client] += 1
    send_ack(client, expected[client] - 1)
```

## Relações com outros conceitos

Depende de `rtm.net.ordering-and-reliability` (mecanismos de transporte) e de `rtm.net.packet-loss` (o problema de origem). Complementa `rtm.rel.reconnection` (replay após queda) e `rtm.rel.fault-tolerance` (reexecução idempotente). Relaciona-se aos transportes `rtm.proto.udp` e `rtm.proto.tcp` e à arquitetura `rtm.arch.event-driven`. Avaliado por `rtm.perf.metrics`.

## Lacunas e questões abertas

- A seção 4.3 da especificação MQTT 5.0 (fluxos de QoS) não foi lida integralmente nesta sessão; as definições citadas vêm do resumo e das seções de pacotes (3.3 a 3.7).
- Não foi localizada fonte primária que meça o custo de deduplicação por id em servidores de jogo com milhares de clientes; os limites de janela são decisão de projeto sem evidência citada.
- O livro de Kleppmann (DDIA) trata o tema em profundidade, mas não foi consultado nesta sessão; não citado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| kafka2026semantics | fornecedor | 2026-10-29 |
| oasis2019mqtt | normativo | 2026-10-29 |
| rfc9147 | normativo | 2026-10-29 |
| rfc7519 | normativo | 2026-10-29 |
| fiedler2008reliability | tecnico | 2026-10-29 |
| rfc8446 | normativo | 2026-10-29 |
| colyseus2026connection | fornecedor | 2026-10-29 |
