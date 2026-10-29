---
id: rtm.net.bandwidth
titulo: Largura de banda (banda vs latência, custo por tick, compressão, orçamento de bits por cliente)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [cheshire1996latency, fiedler2014snapshot, fiedler2015compression, fiedler2015state, fiedler2018vr, fiedler2016reading, fiedler2016fragmentation, fiedler2008reliability, fiedler2014lockstep, rfc8085, rfc6455, rfc6202, rfc768, riot2020valorant, claypool2006report]
relacoes:
  - { tipo: complementa, alvo: rtm.net.latency }
  - { tipo: complementa, alvo: rtm.net.packet-loss }
  - { tipo: depende-de, alvo: rtm.rt.communication-patterns }
  - { tipo: relacionado-a, alvo: rtm.sync.delta-compression }
  - { tipo: relacionado-a, alvo: rtm.sync.interest-management }
  - { tipo: relacionado-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.sync.state-synchronization }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
  - { tipo: avaliado-por, alvo: rtm.perf.load-testing }
termos: [largura de banda, taxa de envio, tick rate, orçamento de bits, bitpacking, quantização, delta encoding, priority accumulator, MTU, overhead de cabeçalho]
---

# Largura de banda

## Definição e terminologia

**Largura de banda** (ou **capacidade**) é a quantidade de dados que um enlace ou caminho transporta por unidade de tempo. Cheshire insiste na distinção com latência: "Manufacturers say 'speed' when they mean 'capacity'", e capacidade pode ser aumentada agregando enlaces, enquanto latência não [F: cheshire1996latency]. Em sistemas multiplayer, as grandezas derivadas são [I]:

- **taxa de envio** (pacotes por segundo, pps) e **tick rate** (passos de simulação por segundo), que podem diferir;
- **custo por tick**: bytes que um emissor precisa enviar por passo para um destinatário;
- **orçamento de bits por cliente**: limite superior aceito por segundo (ou por pacote) para cada conexão.

O que banda **não** é: velocidade de entrega. Cheshire exemplifica que 40 KB levam cerca de 32 ms em Ethernet de 10 Mbit/s e cerca de 5 s em ISDN de 64 kbit/s; o mesmo arquivo, latências diferentes só por serialização [F: cheshire1996latency].

## Problema que resolve

Taxas de envio altas reduzem atraso de interpolação (ver `rtm.net.jitter`) mas multiplicam o custo; estados grandes não cabem em pacotes pequenos; cabeçalhos dominam mensagens pequenas. O orçamento de banda é a restrição que obriga a escolher **o que**, **quanto** e **com que precisão** enviar [I].

## Fundamentos e funcionamento

### Custo por tick e por pacote

Fiedler calcula o pior caso de snapshots não comprimidos: 900 cubos a 225 bits cada dão cerca de 25 KB por snapshot; a 60 pps, 1.520.550 bytes/s, cerca de 11,6 Mbit/s; a 10 pps cai por um fator de 6, para cerca de 2 Mbit/s [F: fiedler2014snapshot]. Em outra contagem (901 cubos, 321 bits/cubo, 60 pps) o ponto de partida é 17,37 Mbit/s e a meta "256 kilobits per-second" [F: fiedler2015compression]. Em VR, a meta era manter cada jogador "under 256kbps, so the entire simulation could fit into 1mbps for the host", atingida para quatro jogadores [F: fiedler2018vr].

Cada pacote carrega cabeçalhos de IP e UDP: no cálculo de Fiedler um snapshot de 25 KB vira 25.342,5 bytes por pacote com cabeçalhos [F: fiedler2014snapshot]; o cabeçalho UDP tem 8 bytes [F: rfc768]. Para mensagens pequenas, o RFC 6455 aponta que em HTTP "each client-to-server message having an HTTP header" é "high overhead" [F: rfc6455, §1.1] e o RFC 6202 que em long polling cada mensagem é um HTTP completo [F: rfc6202, §2.2].

### Banda proporcional a quê?

Em lockstep só entradas trafegam: "bandwidth is proportional to the size of the input, not the number of objects in the simulation"; entradas de 6 bits a 60 por segundo, redundantes até o ack, dão 2 a 15 quadros por pacote para RTT de 30 a 250 ms, e o pior caso de 2 s são 90 bytes [F: fiedler2014lockstep]. Em sincronização de estado, a banda é proporcional ao número de objetos **enviados por pacote**, que o emissor limita [F: fiedler2015state]. [I] Escolher a arquitetura é escolher a variável de que a banda depende (jogadores, objetos ou eventos).

### Limite por pacote: MTU

Fiedler adota 1200 bytes como "conservative lower bound" de payload na IPv4 de 2016, com 1500 como MTU real de desktops e 1472 como limite típico de payload UDP antes de fragmentação; em IPv6 pacotes de até 1280 bytes passam sem fragmentação [F: fiedler2016fragmentation]. O RFC 8085 fixa os mesmos valores de fallback (1280 em IPv6; min(576, MTU do primeiro salto) em IPv4) [F: rfc8085, §3.2]. [I] O orçamento por pacote vira então `~1200 − cabeçalho_da_aplicação` bytes.

## Algoritmos e modelos relevantes

### Reduzir bits por valor

- **Bitpacking**: escrever só os bits necessários para a faixa, por exemplo 10 bits para [0, 1000] em vez de 16; texto é "much less efficient than the binary format" (uint32 máximo: 10 bytes em texto, 4 em binário) [F: fiedler2016reading].
- **Quantização**: orientação como "smallest three" em 29 bits em vez de 128; posição em 50 bits; bit "at rest" que dispensa velocidades; cubo cai de 321 para 80 bits, "approximately 1/4 of the original cost" [F: fiedler2015compression]. Em sincronização de estado a precisão precisa subir (512 → 4096 posições por metro; 9 → 15 bits por componente) para que extrapolações coincidam [F: fiedler2015state].

### Enviar menos valores

- **Delta encoding contra baseline confirmado**: o emissor codifica cada snapshot em relação a um snapshot que o receptor confirmou, "roughly RTT in the past"; cubos não alterados custam 1 bit; índices relativos custam 5,5 bits em média; deltas de posição 26,1 bits e de orientação 23,3 bits; uma cena parada cai para "around 15 kilobits per-second" [F: fiedler2015compression]. Com predição balística do baseline, cerca de 90% dos cubos em movimento custam 1 bit extra ("perfect prediction") [F: fiedler2018vr]. Ver `rtm.sync.delta-compression`.
- **Priority accumulator**: cada objeto acumula prioridade por quadro; os de maior acumulado entram no pacote até o limite de bytes, e só os enviados zeram o acumulador; exemplo de prioridades 1.000.000 (jogador), 100 (interagindo), 1 (em repouso); orçamento de 256 kbit/s ajustável em tempo de execução [F: fiedler2015state]. Ver `rtm.sync.interest-management`.

### Adaptar a taxa

Fiedler usa dois modos: 30 pps em condições boas e 10 pps em condições ruins (RTT > 250 ms), com pacotes de 256 bytes, o que dá cerca de 64 kbit/s e 20 kbit/s, e histerese com tempo de retorno dobrando até 60 s [F: fiedler2008reliability]. O RFC 8085 exige que aplicações UDP que enviam mais de alguns datagramas por RTT implementem controle de congestionamento tipo TFRC ou janela, e que as de baixo volume não enviem, em média, "more than one UDP datagram per RTT" [F: rfc8085, §3.1.2-3.1.3].

## Requisitos e pressupostos

- Delta encoding exige acks e memória de baselines por receptor [F: fiedler2015compression; fiedler2015state].
- Quantização exige que emissor e receptor quantizem igual antes de simular [F: fiedler2015state].
- Orçamento por cliente pressupõe que o pior caso agregado no servidor (clientes × orçamento) caiba no enlace de subida [I]. Claypool observa que a maioria dos jogos tem "low bitrate requirements, sending frequent but small packets" [F: claypool2006report, §1].

## Vantagens e limitações

| Técnica | Ganho | Custo |
|---|---|---|
| reduzir pps | linear (60→10 pps = 6×) [F: fiedler2014snapshot] | atraso de interpolação maior |
| quantização | ~4× por objeto [F: fiedler2015compression] | perda de precisão; pops se insuficiente [F: fiedler2015state] |
| delta encoding | "big order of magnitude win" [F: fiedler2015compression] | acks, baselines, complexidade |
| priorização | banda fixa por pacote [F: fiedler2015state] | objetos de baixa prioridade atrasam |
| lockstep (só entradas) | independe de nº de objetos [F: fiedler2014lockstep] | determinismo; latência do mais lento |

## Alternativas e comparações

Comparação entre **mais banda** e **mais latência**: Cheshire argumenta que latência não pode ser comprada [F: cheshire1996latency]; Fiedler mostra que enviar menos (10 pps) custa atraso de interpolação (350 ms) e enviar mais (60 pps) reduz para cerca de 85 ms [F: fiedler2014snapshot]. [I] A banda é, portanto, o recurso que se gasta para comprar latência de interpolação menor.

## Métricas e métodos de avaliação

Bits por segundo por cliente (entrada e saída), bytes por pacote, pps, fração de cabeçalho, taxa de objetos atendidos por tick (priorização). Em laboratório, Fiedler reporta kbit/s por cena (parada vs. em movimento) [F: fiedler2015compression]. Ver `rtm.perf.metrics` e `rtm.perf.load-testing`.

## Exemplo técnico independente de domínio

Orçamento por pacote com acumulador de prioridade:

```
ORCAMENTO_BYTES = 1200 - CABECALHO           # conservador para MTU [F: fiedler2016fragmentation]
a cada tick, para cada destinatário d:
    for obj in objetos: acc[d][obj] += prioridade(obj, d)
    candidatos = ordenar(objetos, por=acc[d], decrescente)
    pacote = novo(); usados = 0
    for obj in candidatos:
        bits = codificar_delta(obj, baseline[d][obj])   # 1 bit se inalterado
        if usados + bits <= ORCAMENTO_BYTES*8:
            pacote += bits; usados += bits; acc[d][obj] = 0
    enviar(d, pacote)
# banda por destinatário <= ORCAMENTO_BYTES * pps, independentemente do nº de objetos
```

## Relações com outros conceitos

Complementa `rtm.net.latency` (a troca banda × atraso de interpolação) e `rtm.net.packet-loss` (fragmentação multiplica perda); depende de `rtm.rt.communication-patterns` (overhead por padrão); fundamenta `rtm.sync.delta-compression`, `rtm.sync.interest-management`, `rtm.sync.snapshot-interpolation`, `rtm.sync.state-synchronization` e `rtm.arch.deterministic-lockstep`; é avaliada em `rtm.perf.metrics` e `rtm.perf.load-testing`.

## Lacunas e questões abertas

- Os números de Fiedler são de uma simulação de física com 900 cubos; não há aqui medições de banda de jogos comerciais nem de colaboração (CRDT/OT), onde o custo é por operação.
- O relato de fornecedor sobre 128 ticks/s não informa banda por cliente [F: riot2020valorant].
- Não foi localizada fonte normativa para "orçamento de bits por cliente"; é prática de engenharia.
- Compressão genérica (entropia, dicionário) aplicada a estado de jogo não foi coberta pelas fontes abertas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| cheshire1996latency | tecnico | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2015compression | tecnico | 2026-10-29 |
| fiedler2015state | tecnico | 2026-10-29 |
| fiedler2018vr | tecnico | 2026-10-29 |
| fiedler2016reading | tecnico | 2026-10-29 |
| fiedler2016fragmentation | tecnico | 2026-10-29 |
| fiedler2008reliability | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| rfc8085 | normativo (BCP) | 2026-10-29 |
| rfc6455 | normativo | 2026-10-29 |
| rfc6202 | normativo (informativo) | 2026-10-29 |
| rfc768 | normativo | 2026-10-29 |
| riot2020valorant | tecnico | 2026-10-29 |
| claypool2006report | academico | 2026-10-29 |
