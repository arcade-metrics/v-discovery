---
id: rtm.perf.metrics
titulo: Métricas de rede e de aplicação para tempo real
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc2681, rfc7679, rfc7680, rfc3393, google2016sre, k62026metrics, artillery2026ws, heroiclabs2026authoritative, heroiclabs2026configuration, colyseus2026room, colyseus2026sdk, principlesofchaos2019]
relacoes:
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: depende-de, alvo: rtm.net.jitter }
  - { tipo: depende-de, alvo: rtm.net.packet-loss }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
  - { tipo: complementa, alvo: rtm.perf.qoe-thresholds }
  - { tipo: complementa, alvo: rtm.perf.load-testing }
  - { tipo: complementa, alvo: rtm.perf.network-emulation }
  - { tipo: complementa, alvo: rtm.net.clock-synchronization }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: especificado-por, alvo: rtm.std.index }
termos: [RTT, one-way delay, IPDV, jitter, perda de pacotes, tick rate, tempo por tick, snapshot, misprediction, percentil, p99, histograma, quatro sinais de ouro]
---

# Métricas de rede e de aplicação para tempo real

## Definição e terminologia

Métricas são as grandezas mensuráveis com as quais se avalia um sistema de tempo real, divididas em duas famílias: métricas de **rede** (propriedades do caminho entre cliente e servidor, definidas de forma normativa pelo grupo IPPM do IETF) e métricas de **aplicação** (propriedades do servidor, do protocolo de aplicação e da experiência resultante, definidas por cada sistema). Este documento é o ponto de referência `avaliado-por` dos demais documentos do domínio: cada técnica aponta para cá as métricas com que deve ser avaliada.

Definições normativas:

- **Round-trip delay (RTT)**: a RFC 2681 define `Type-P-Round-trip-Delay` como o intervalo entre o envio do primeiro bit de um pacote pela origem e a recepção do último bit da resposta, "that Src received the last bit of that packet at wire-time T+dT"; se não há resposta, o valor é indefinido, "(informally, infinite)" [F: rfc2681, §2.4]. A RFC observa que "The minimum value of this metric provides an indication of the delay due only to propagation and transmission delay", e valores acima do mínimo indicam congestionamento [F: rfc2681, §1.1].
- **One-way delay**: a RFC 7679 define `Type-P-One-way-Delay` como dT tal que "Src sent the first bit of a Type-P packet to Dst at wire time T" e "Dst received the last bit of that packet at wire time T+dT"; indefinido se o pacote não chega dentro do limiar Tmax [F: rfc7679, §3.4]. A medição exige relógios sincronizados: "it will be important for Src and Dst to synchronize very closely", com GPS atingindo dezenas de microssegundos e NTP comum apenas milissegundos [F: rfc7679, §3.5].
- **One-way loss**: a RFC 7680 define `Type-P-One-way-Packet-Loss` com valor 0 (recebido) ou 1 (não recebido dentro de Tmax); o limiar Tmax trata atrasos muito grandes como perda [F: rfc7680, §2.4]. A RFC justifica medir por sentido porque caminhos de ida e volta podem diferir [F: rfc7680, §1].
- **Delay variation (jitter)**: a RFC 3393 define IPDV como "the difference between the one-way-delay of the selected packets" de um fluxo, e explica que evita o termo "jitter" "because it is used in different ways", preferindo "delay variation" [F: rfc3393, §1.1, §1.2, §2.4]. Aplica-se com ou sem relógios sincronizados, pois a diferença cancela o offset constante [F: rfc3393, abstract].

## Problema que resolve

Sem métricas definidas, discussões sobre "lag" não convergem: RTT medido pela aplicação (que inclui filas e processamento) difere do RTT de rede; "jitter" significa coisas diferentes para cada equipe; médias escondem a cauda que os usuários sentem. Definir o vocabulário, o método de cálculo e a forma de agregação é pré-requisito para limiares (ver `rtm.perf.qoe-thresholds`), testes de carga (ver `rtm.perf.load-testing`) e emulação (ver `rtm.perf.network-emulation`).

## Fundamentos e funcionamento

### Métricas de rede

| Métrica | Definição | Unidade | Como medir em aplicação [I] |
|---|---|---|---|
| RTT | RFC 2681 [F: rfc2681] | ms | ping/pong de aplicação com timestamp local; não exige sincronização |
| One-way delay | RFC 7679 [F: rfc7679] | ms | exige relógios sincronizados (ver `rtm.net.clock-synchronization`); raro em produção |
| IPDV | RFC 3393 [F: rfc3393] | ms | diferença entre atrasos de pacotes consecutivos; usar o RTT ou o intervalo de chegada como proxy |
| Perda | RFC 7680 [F: rfc7680] | fração | lacunas de número de sequência por janela de tempo |
| Reordenação | fora das RFCs lidas | fração | pacotes com sequência menor que a última entregue |
| Vazão por cliente | ver `rtm.net.bandwidth` | bytes/s | contadores de envio e recepção por conexão |

### Métricas de aplicação

| Métrica | O que mede | Fonte do conceito |
|---|---|---|
| Taxa de mensagens (enviadas/recebidas por segundo) | carga de protocolo | Artillery expõe `websocket.send_rate` e `websocket.receive_rate` [F: artillery2026ws]; k6 expõe `ws_msgs_sent`, `ws_msgs_received` [F: k62026metrics] |
| Bytes por cliente por segundo | custo de banda por sessão | k6 `data_sent`, `data_received` [F: k62026metrics] |
| Tick rate | frequência do laço de simulação | Nakama: "the desired frequency (per second) at which the server calls the match loop function" [F: heroiclabs2026authoritative]; Colyseus: timestep padrão 16.6 ms (60 fps) e `patchRate` padrão 50 ms (20 fps) [F: colyseus2026room] |
| Tempo de processamento por tick | fração do orçamento do tick consumida | Nakama: "If too many loops fall behind [...] the server will end the match" [F: heroiclabs2026authoritative] |
| Tamanho de snapshot ou patch | bytes por atualização de estado | ver `rtm.sync.snapshot-interpolation`, `rtm.sync.delta-compression` |
| Mispredictions por minuto | correções visíveis de predição | ver `rtm.pred.client-side-prediction` [I] |
| Tempo de handshake e de sessão | custo de abertura e duração | k6 `ws_connecting`, `ws_session_duration`, `ws_sessions` [F: k62026metrics] |
| Latência de ping de aplicação | RTT medido no protocolo | k6 `ws_ping`: "Duration between a ping request and its pong reception" [F: k62026metrics]; Colyseus `room.ping()` "Measure round-trip time on an existing connection" [F: colyseus2026sdk] |
| Tempo de reconexão | do fechamento à retomada | ver `rtm.rel.reconnection` [I] |
| Conexões simultâneas por nó | capacidade | k6 `vus` como carga oferecida [F: k62026metrics]; no servidor, contador de sockets abertos |
| Fila de saída por cliente | cliente lento | Nakama `socket.outgoing_queue_size` padrão 16: "If this is exceeded the client is considered too slow and will disconnect" [F: heroiclabs2026configuration] |

### Agregação: percentis, não médias

O capítulo de monitoramento do livro de SRE do Google adverte que "it's tempting to design a system based upon the mean of some quantity", mas que "the idea that most of your requests are near the mean is just hopeful thinking"; recomenda coletar "request counts bucketed by latencies (suitable for rendering a histogram), rather than actual latencies", com limites de bucket "approximately exponentially" distribuídos, e usar "your 99th percentile response time over some small window" como sinal precoce de saturação [F: google2016sre]. O mesmo texto nota que, em sistemas encadeados, "the 99th percentile of one backend can easily become the median response of your frontend" [F: google2016sre]. Os Principles of Chaos Engineering citam "latency percentiles" entre os exemplos de saída mensurável do steady state [F: principlesofchaos2019].

[I] Em tempo real a cauda é a experiência: um p50 de 40 ms com p99 de 400 ms significa que, a 20 snapshots por segundo, cada cliente vê uma correção visível a cada poucos segundos. Reportar p50, p95 e p99 por janela curta (por exemplo, 10 s) e por cliente, e nunca só a média.

### Os quatro sinais

O livro de SRE propõe "latency, traffic, errors, and saturation" como os quatro sinais a observar se só se puder observar quatro, distinguindo "the latency of successful requests and the latency of failed requests" [F: google2016sre]. [I] Tradução para tempo real: latência (RTT de aplicação, tempo por tick), tráfego (mensagens/s, bytes/s, conexões), erros (mensagens rejeitadas, desconexões não consentidas, lacunas de sequência), saturação (fração do orçamento do tick, fila de saída, descritores de arquivo).

### Como instrumentar

1. **Cliente**: ping/pong de aplicação com timestamp local a cada 1 a 5 s para RTT [I]; contadores de lacunas e duplicatas por sequência; contador de correções de predição; timestamp de cada evento de fechamento e de retomada.
2. **Servidor**: por tick, tempo de início e fim; por cliente, bytes e mensagens em cada sentido, tamanho da fila de saída, último ping; por sala, número de presenças e tamanho do último snapshot.
3. **Exportação**: histogramas com buckets exponenciais [F: google2016sre] por métrica, rotulados por versão de cliente, região e tipo de rede; nunca agregar p99 pela média de p99 de nós diferentes (percentis não se somam) [I].
4. **Ferramentas de carga**: k6 e Artillery já emitem as métricas de WebSocket listadas acima; para UDP e protocolos próprios, a aplicação precisa expor contadores equivalentes (ver `rtm.perf.load-testing`).

## Requisitos e pressupostos

- Números de sequência em todas as mensagens para medir perda, reordenação e duplicatas.
- Relógio monotônico local para RTT; relógios sincronizados só para one-way delay [F: rfc7679, §3.5].
- Cardinalidade controlada nos rótulos: métricas por cliente em memória, agregadas antes de exportar.

## Vantagens e limitações

- RTT é barato e não exige sincronização, mas combina ida e volta, que podem diferir; a RFC 2681 reconhece essa troca por facilidade de implantação [F: rfc2681, §1.1].
- IPDV com RTT como proxy mistura variação de ida e de volta; aceitável como indicador, não como medida normativa [I].
- Percentis por janela curta são ruidosos com poucos clientes; reportar o n junto.

## Alternativas e comparações

Métricas de QoE (opinião do usuário, MOS) são o complemento das métricas objetivas desta página e são tratadas em `rtm.perf.qoe-thresholds` com as Recomendações ITU-T G.1032 e G.1072.

## Exemplo técnico independente de domínio

```text
# Cliente: RTT e perda por sequence
every 2 s: send(PING, {t0 = mono_now()})
on PONG(t0): rtt = mono_now() - t0 ; hist_rtt.observe(rtt)
on MSG(seq): if seq > expected: lost += seq - expected ; expected = seq + 1
             elif seq < expected: dup_or_reorder += 1 ; else: expected += 1

# Servidor: tempo por tick e fila de saida
each tick: t = mono_now() ; simulate() ; hist_tick.observe(mono_now() - t)
           for c in clients: gauge_outq.set(c.id, len(c.outbox))
# Export: histogramas com buckets exponenciais; p50/p95/p99 por janela de 10 s
```

## Relações com outros conceitos

Depende das propriedades de rede (`rtm.net.latency`, `rtm.net.jitter`, `rtm.net.packet-loss`, `rtm.net.bandwidth`). Complementa `rtm.perf.qoe-thresholds` (o que os números significam para o usuário), `rtm.perf.load-testing` e `rtm.perf.network-emulation` (como produzi-los) e `rtm.net.clock-synchronization` (one-way delay). Relaciona-se a `rtm.pred.client-side-prediction`, `rtm.sync.snapshot-interpolation` e `rtm.rel.reconnection`, que apontam para cá como `avaliado-por`. Especificado pelas RFCs do IPPM indexadas em `rtm.std.index`.

## Lacunas e questões abertas

- Não foi lida nesta sessão a RFC de reordenação de pacotes do IPPM (RFC 4737); a métrica de reordenação acima é descrita informalmente.
- Não há, nas fontes consultadas, definição padronizada de "misprediction" nem método de contagem; é uma métrica de aplicação sem norma.
- A documentação do Colyseus consultada não descreve métricas internas do servidor (tempo por tick); só a API de ping do cliente.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc2681 | normativo | 2026-10-29 |
| rfc7679 | normativo | 2026-10-29 |
| rfc7680 | normativo | 2026-10-29 |
| rfc3393 | normativo | 2026-10-29 |
| google2016sre | tecnico | 2026-10-29 |
| k62026metrics | fornecedor | 2026-10-29 |
| artillery2026ws | fornecedor | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| heroiclabs2026configuration | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| colyseus2026sdk | fornecedor | 2026-10-29 |
| principlesofchaos2019 | tecnico | 2026-10-29 |
