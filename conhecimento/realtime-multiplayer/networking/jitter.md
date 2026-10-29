---
id: rtm.net.jitter
titulo: Jitter (variação de atraso, IPDV, PDV, jitter buffer e atraso de interpolação)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc3393, rfc5481, rfc3550, rfc3611, rfc7679, fiedler2014snapshot, fiedler2015state, fiedler2014lockstep, fiedler2018vr, gambetta2014entity]
relacoes:
  - { tipo: complementa, alvo: rtm.net.latency }
  - { tipo: complementa, alvo: rtm.net.packet-loss }
  - { tipo: depende-de, alvo: rtm.net.clock-synchronization }
  - { tipo: relacionado-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
  - { tipo: avaliado-por, alvo: rtm.perf.network-emulation }
termos: [jitter, IPDV, PDV, variação de atraso, jitter buffer, playout delay, atraso de interpolação, interarrival jitter]
---

# Jitter

## Definição e terminologia

**Jitter** é o nome coloquial para a **variação do atraso** entre pacotes de um mesmo fluxo. O RFC 3393 evita o termo ("we will avoid the term 'jitter' whenever possible") porque ele tem dois sentidos: variação de um sinal em relação a um relógio e variação de uma métrica em relação a uma referência, como média ou mínimo [F: rfc3393, §1.1]. As definições normativas:

- **IPDV** (*IP Packet Delay Variation*): "the difference between the one-way-delay of the selected packets", `ddT = dTk − dTi` para um par de pacotes escolhido por uma **função de seleção** [F: rfc3393, §1.2, §2.4-2.5]. O RFC 5481 escreve a forma usual com pacotes consecutivos: `IPDV(i) = D(i) − D(i−1)` [F: rfc5481, §4.1].
- **PDV** (*Packet Delay Variation*): `PDV(i) = D(i) − D(min)`, atraso relativo ao pacote de menor atraso do intervalo, sempre ≥ 0; o nome vem da Recomendação ITU-T Y.1540 [F: rfc5481, §4.2].
- **Interarrival jitter** do RTP: estimativa da "statistical variance of the RTP data packet interarrival time", definida como desvio médio suavizado de `D(i,j) = (Rj − Ri) − (Sj − Si)` com `J(i) = J(i−1) + (|D(i−1,i)| − J(i−1))/16`; o ganho 1/16 "gives a good noise reduction ratio while maintaining a reasonable rate of convergence" [F: rfc3550, §6.4.1].

O RFC 3393 é Standards Track; o RFC 5481 é informativo e se apresenta como declaração de aplicabilidade das duas formas [F: rfc3393; rfc5481, §1].

**Jitter buffer** (ou *de-jitter buffer*, *playout buffer*): fila no receptor que atrasa a entrega para que os pacotes possam ser consumidos em ritmo regular. O RFC 3611 reporta seus parâmetros: `JB nominal` (atraso para pacotes pontuais), `JB maximum` e `JB abs max`, e um campo que indica se o buffer é adaptativo ou fixo [F: rfc3611, §4.7.6-4.7.7].

## Problema que resolve

Pacotes enviados em intervalos regulares chegam em intervalos irregulares. Um consumidor em ritmo fixo (decodificador de áudio, simulação em tick, interpolador de posições) precisa de uma reserva de tempo para não ficar sem dados; o tamanho dessa reserva é o custo em latência que o jitter impõe [I]. Fiedler descreve o sintoma sem buffer: objetos empilhados "drift out of phase in time and pop" [F: fiedler2015state].

## Fundamentos e funcionamento

### IPDV versus PDV

O RFC 5481 compara as duas formas: IPDV pode ser positivo ou negativo, PDV é ≥ 0; a distribuição de PDV não muda se a ordem dos pacotes mudar, a de IPDV muda; PDV é menos afetado por perda (no caso de perda alternada, IPDV não produz resultado) [F: rfc5481, §4.4, §6.1]. Para dimensionar buffer, o RFC favorece PDV: o atraso mínimo serve como ponto de alinhamento e "the PDV range or 99.9th percentile relates closely to the required buffer size", enquanto IPDV "has no reliable relationship to de-jitter buffer size" [F: rfc5481, §7.1.2, §7.3].

### Relação com perda

O RFC 3393 observa que pacotes perdidos impedem estatísticas simples como a média, exigindo estatísticas condicionais que descartam pares com perda [F: rfc3393, §4.1]. O RFC 3611 define *discard rate*: fração de pacotes descartados pelo jitter buffer por chegada tardia ou precoce, underrun ou overflow [F: rfc3611, §4.7.1]. [I] Um pacote que chega depois do seu instante de reprodução é, para a aplicação, equivalente a um pacote perdido; jitter e perda se convertem um no outro pelo tamanho do buffer.

### Jitter buffer em simulações

Fiedler aplica a mesma ideia a estado de jogo: pacotes "bunch up" entre quadros, então o receptor os guarda em um jitter buffer indexado pelo número de sequência e os libera no instante correto; para sincronização de estado, sugere "4-5 frames @ 60HZ" de atraso [F: fiedler2015state]. Para lockstep determinístico, o buffer de *playout delay* guarda o tempo local da primeira entrada e libera cada quadro nesse tempo mais 100 ms; "the cost of increasing the buffer size is additional latency" [F: fiedler2014lockstep]. Em realidade virtual, usou "100ms delay to received packets" para suavizar a entrega de estado dos avatares [F: fiedler2018vr].

### Jitter e atraso de interpolação

Na interpolação de snapshots, o buffer absorve jitter **e** perda. Fiedler relata que, com 2 a 5% de perda, o melhor atraso é 3× o intervalo de envio (300 ms a 10 pacotes/s) para sobreviver a dois pacotes consecutivos perdidos, e adicionou mais tempo para jitter, totalizando 350 ms; o jitter observado era de "one or two frames @ 60fps"; a 30 pps o atraso cai para cerca de 150 ms e a 60 pps para cerca de 85 ms [F: fiedler2014snapshot]. Gambetta mostra o mesmo mecanismo com um intervalo de atualização (100 ms a 10 atualizações/s) como atraso de exibição [F: gambetta2014entity]. [I] Logo: `atraso_interp ≈ k·intervalo_envio + margem_jitter`, com `k` escolhido pela tolerância a perdas consecutivas.

## Algoritmos e modelos relevantes

- Estimador RTP com filtro exponencial 1/16 [F: rfc3550, §6.4.1]; o RFC 3393 descreve a mesma estimativa como "jitter estimate" com valores absolutos de IPDV [F: rfc3393, §4.5].
- Estatísticas IPPM para IPDV: percentis (o 50º é a mediana), percentil inverso, pico a pico (máximo menos mínimo em subintervalos) [F: rfc3393, §4.3-4.6].
- Buffer adaptativo: o RFC 3611 reconhece buffers adaptativos reportando `JB abs max` como o maior atraso que podem atingir [F: rfc3611, §4.7.7]; o algoritmo de adaptação em si não é normalizado nas fontes consultadas [I].

## Requisitos e pressupostos

IPDV e PDV são definidos sobre atrasos unidirecionais, que requerem relógios sincronizados ou, ao menos, com deriva conhecida [F: rfc7679, §3.5]. [I] Uma diferença de atrasos cancela o *offset* constante entre os relógios, mas não a deriva (*skew*), que aparece como tendência na série de IPDV. O estimador RTP usa carimbos de tempo da origem e do receptor sem exigir sincronização de offset [F: rfc3550, §6.4.1].

## Vantagens e limitações

| Métrica | Vantagem | Limitação |
|---|---|---|
| IPDV | sensível à ordem e à sequência; útil para diagnosticar enfileiramento | não se relaciona de forma confiável ao tamanho de buffer; sofre com perda [F: rfc5481, §6.1, §7.3] |
| PDV | relação direta com buffer; robusta à perda; composição espacial possível | depende de estimar o mínimo no intervalo [F: rfc5481, §6.4, §7.1.2] |
| interarrival jitter (RTP) | computável no receptor sem relógio sincronizado | é uma média suavizada, não um percentil [F: rfc3550, §6.4.1] |

## Alternativas e comparações

Alternativas ao buffer para lidar com jitter em simulações [I]: extrapolação (Fiedler relata redução de 350 ms para 150 ms, mas com imprecisão em corpos rígidos [F: fiedler2014snapshot]); aumentar a taxa de envio (reduz o intervalo e portanto o atraso de interpolação, ao custo de banda, ver `rtm.net.bandwidth`); e aceitar *pops* visuais com suavização posterior [F: fiedler2015state].

## Métricas e métodos de avaliação

IPDV e PDV com percentis (99,9º para buffer) [F: rfc5481, §7.1.2]; interarrival jitter RTCP [F: rfc3550]; taxa de descarte e parâmetros de buffer RTCP XR [F: rfc3611]. Em laboratório, Fiedler usa jitter simulado de ±2 quadros a 60 fps combinado com 5% de perda [F: fiedler2014snapshot]; ver `rtm.perf.network-emulation`.

## Exemplo técnico independente de domínio

Jitter buffer por número de sequência, no estilo descrito por Fiedler:

```
ATRASO = 100 ms                       # ou k * intervalo_envio + margem
ao receber pacote(seq, t_chegada):
    if base_t is None: base_t = t_chegada; base_seq = seq
    buffer[seq] = pacote
a cada tick de consumo (agora):
    seq_alvo = base_seq + floor((agora - base_t - ATRASO) / intervalo_envio)
    if seq_alvo in buffer: consumir(buffer.pop(seq_alvo))
    else: registrar("underrun")        # perda ou jitter > ATRASO
```

Dimensionamento com PDV: `ATRASO ≈ percentil_99.9(PDV) + margem` [F: rfc5481, §7.1.2]. [I] Para interpolação, somar ainda `k·intervalo_envio` para cobrir perdas consecutivas.

## Relações com outros conceitos

Complementa `rtm.net.latency` (o buffer converte jitter em latência fixa) e `rtm.net.packet-loss` (pacotes tardios são descartados); depende de `rtm.net.clock-synchronization` para IPDV/PDV; é o fundamento do atraso em `rtm.sync.snapshot-interpolation` e `rtm.pred.entity-interpolation` e do *playout delay* em `rtm.arch.deterministic-lockstep`; é avaliado em `rtm.perf.metrics` e reproduzido em `rtm.perf.network-emulation`.

## Lacunas e questões abertas

- Nenhuma fonte normativa consultada especifica um algoritmo de buffer adaptativo; há apenas campos de relatório (RFC 3611).
- A relação `atraso_interp ≈ k·intervalo + margem` é síntese do autor a partir de relatos técnicos; faltam medições publicadas por taxa de envio e perfil de jitter.
- Os valores de Fiedler (350 ms a 10 pps etc.) vêm de um experimento específico com física de corpos rígidos; não generalizar sem medir.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc3393 | normativo | 2026-10-29 |
| rfc5481 | normativo (informativo) | 2026-10-29 |
| rfc3550 | normativo | 2026-10-29 |
| rfc3611 | normativo | 2026-10-29 |
| rfc7679 | normativo | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2015state | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| fiedler2018vr | tecnico | 2026-10-29 |
| gambetta2014entity | tecnico | 2026-10-29 |
