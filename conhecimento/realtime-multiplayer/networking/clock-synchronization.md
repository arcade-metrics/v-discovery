---
id: rtm.net.clock-synchronization
titulo: Sincronização de relógios (NTP, PTP, estimativa de offset por RTT, tempo do servidor como referência)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc5905, rfc2330, rfc7679, rfc2681, rfc8877, ieee2019ptp, cristian1989probabilistic, lamport1978time, kulkarni2014logical, w3c2026hrtime, fiedler2014lockstep, fiedler2015state, gambetta2014entity]
relacoes:
  - { tipo: complementa, alvo: rtm.net.logical-clocks }
  - { tipo: complementa, alvo: rtm.net.latency }
  - { tipo: depende-de, alvo: rtm.net.jitter }
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: relacionado-a, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
termos: [offset, skew, drift, sincronização de relógio, NTP, PTP, stratum, server time, relógio monotônico, wall clock, timestamp]
---

# Sincronização de relógios

## Definição e terminologia

O RFC 2330 define os termos [F: rfc2330, §10.1]: **offset** é a diferença entre a leitura do relógio e o tempo verdadeiro (UTC); **skew** é a diferença de frequência (taxa de variação do offset); **drift** é a variação do skew; **resolução** é o menor incremento do relógio; dois relógios estão **sincronizados** quando seu offset relativo é zero. O RFC 2330 ilustra que um skew de 0,01% soma cerca de 60 ms de erro em 10 minutos [F: rfc2330, §10.1].

**Sincronizar** é estimar e corrigir offset (e skew) de um relógio em relação a uma referência. Dois padrões:

- **NTP v4** (RFC 5905, Standards Track, obsoleta RFCs 1305 e 4330): "widely used to synchronize computer clocks in the Internet"; servidores primários têm *stratum* 1 e cada nível abaixo soma um, até o máximo 16 (não sincronizado); porta UDP 123 [F: rfc5905, Abstract, §3, §9.1, Figura 6].
- **PTP** (IEEE 1588-2019, ativo, substitui a edição de 2008): "precise synchronization of clocks in packet-based networked systems", com precisão "in the sub-microsecond range" e, em rede bem projetada, "sub-nanosecond time transfer accuracy" [F: ieee2019ptp]. Apenas a página do padrão foi consultada; o texto normativo não foi aberto.

Em aplicações distribuídas interativas, a referência prática é o **tempo do servidor** (*server time*): cada cliente mantém uma estimativa `t_servidor ≈ t_local + offset` e carimba eventos nessa base [I].

## Problema que resolve

Relógios de cristal divergem: Lamport assume taxa com erro `|dC/dt − 1| < κ` e cita κ ≤ 10^-6 "for typical crystal controlled clocks" [F: lamport1978time, §Physical Clocks]. Sem sincronização, não se pode medir atraso unidirecional (todo erro de sincronização "adds directly to the measurement error" [F: rfc7679, §3.7.1]), nem alinhar buffers de interpolação ou de playout ao tempo do emissor, nem comparar carimbos de tempo entre máquinas [I].

## Fundamentos e funcionamento

### Troca de quatro carimbos (NTP)

O protocolo on-wire usa quatro carimbos: `T1` (envio do cliente), `T2` (recepção no servidor), `T3` (envio do servidor), `T4` (recepção no cliente). O RFC define

```
offset θ = ½ · [(T2 − T1) + (T3 − T4)]
delay  δ = (T4 − T1) − (T3 − T2)
```

e fixa valores negativos de atraso na precisão do sistema [F: rfc5905, §8]. [I] A fórmula do offset assume que ida e volta têm o mesmo atraso; se a assimetria for `a` (ida − volta), o erro do offset é `a/2`. O RFC 2681 lembra que RTT mede "two distinct paths together" e o RFC 7679 que mesmo rotas simétricas têm enfileiramento assimétrico [F: rfc2681, §1.1; rfc7679, §1.1].

### Filtragem e disciplina

O RFC 5905 descreve: um **clock filter** que funciona "as an 8-stage shift register" com amostras ordenadas por atraso crescente; algoritmos de **seleção** (detecção bizantina de "falsetickers"), **agrupamento** e **combinação** ("statistically averaging the surviving truechimers"); e uma **disciplina** que combina PLL e FLL, "a PLL usually works better when network jitter dominates, while an FLL works better when oscillator wander dominates" [F: rfc5905, §5, §10, §11.3]. Intervalos de consulta vão de MINPOLL 6 (64 s) a MAXPOLL 17 (36,4 h) [F: rfc5905, §7.3]. Precisão esperada: "within a few tens of milliseconds" na Internet e "within a few hundred microseconds" em LANs rápidas [F: rfc5905, §1].

O RFC 2330 adverte que usar NTP para calibrar medições dos mesmos caminhos que o NTP atravessa "would be unsound", e que a busca por precisão do NTP pode custar skew e drift de curto prazo; prefere relógios com GPS [F: rfc2330, §10.1].

### Sincronização probabilística

Cristian (1989) propôs ler o relógio remoto por ida e volta e aceitar a leitura só quando o RTT é curto, limitando o erro; apenas o registro bibliográfico foi verificado [F: cristian1989probabilistic]. [I] O princípio "amostra de menor RTT é a melhor" é o mesmo do clock filter do NTP e da prática em jogos descrita abaixo.

### Relógio cliente-servidor em sistemas interativos

A prática em jogos é uma versão simplificada do NTP [I]: o cliente envia `T1`, o servidor responde com `T2 ≈ T3`, o cliente calcula `offset` e `rtt` por amostra, coleta várias amostras, descarta as de maior RTT (ou fora de uma faixa estatística) e adota a mediana ou média das restantes; depois corrige lentamente para não causar saltos. Fiedler nota que um buffer de playout real precisa "handling clock drift and adjusting playback speed" [F: fiedler2014lockstep], e que em sincronização de estado os pacotes são liberados "at the correct time" por número de sequência [F: fiedler2015state]. A técnica de Simpson (2002), frequentemente citada para isso, **não foi verificada** (página fora do ar).

Com o tempo do servidor como referência, o cliente pode: carimbar entradas com `t_servidor_estimado`; renderizar entidades remotas em `t_servidor_estimado − atraso_interp` (ver `rtm.pred.entity-interpolation` [F: gambetta2014entity]); e o servidor pode reconstruir o instante em que o cliente viu o mundo para compensação de latência (`rtm.pred.lag-compensation`) [I].

### Relógio monotônico vs. wall clock

O padrão W3C High Resolution Time distingue o relógio monotônico ("never decreases, so it can't be changed by system clock adjustments"), apropriado para medir intervalos, do wall clock, que pode retroceder; a resolução padrão é 100 µs, ou 5 µs em contextos isolados [F: w3c2026hrtime]. [I] Offsets devem ser aplicados sobre o relógio monotônico; o wall clock só serve para exibir.

### Formatos de carimbo

O RFC 8877 recomenda o formato NTP de 64 bits (32 bits de segundos desde 1900 + 32 bits de fração, ~233 ps, volta em 2036) e o PTP truncado de 64 bits (segundos desde 1970 em TAI + nanossegundos, volta em 2106) [F: rfc8877, §4.2.1, §4.3].

## Algoritmos e modelos relevantes

- NTP on-wire + filtro + seleção + disciplina [F: rfc5905].
- PTP com carimbos de hardware [F: ieee2019ptp].
- Lamport: sob PC1 (taxa) e PC2 (offset < ε), com mensagens a cada τ segundos e atraso imprevisível < ξ em um grafo de diâmetro d, obtém-se `ε ≈ d(2κτ + ξ)` [F: lamport1978time, Theorem].
- Hybrid Logical Clocks: mantêm o componente lógico "always close to the NTP clock", cabem no formato de 64 bits do NTP e toleram "NTP kinks and uncertainties" [F: kulkarni2014logical]. Ver `rtm.net.logical-clocks`.

## Requisitos e pressupostos

Simetria aproximada de atraso (ou conhecimento da assimetria); estabilidade do oscilador entre amostras; relógio monotônico disponível. Para atraso unidirecional, o RFC 7679 exige sincronização "very closely" e soma à incerteza as resoluções de ambos os relógios [F: rfc7679, §3.5, §3.7.1].

## Vantagens e limitações

| Método | Precisão típica | Requisitos | Limitação |
|---|---|---|---|
| NTP | dezenas de ms (Internet), centenas de µs (LAN) [F: rfc5905, §1] | UDP 123, servidores | assimetria de rota não detectável [I] |
| PTP | sub-µs [F: ieee2019ptp] | hardware de carimbo, rede controlada | não aplicável fim a fim na Internet pública [I] |
| offset por RTT na aplicação | da ordem do jitter residual [I] | nada além do protocolo | mesma hipótese de simetria; precisa refiltrar |

## Alternativas e comparações

Alternativa a sincronizar relógios físicos: não sincronizar e usar ordem causal (`rtm.net.logical-clocks`) ou numerar ticks do servidor como "tempo" (todo evento é carimbado com o tick em que o servidor o processou) [I]. Fiedler indexa o jitter buffer por número de sequência de quadro, que é um relógio de ticks [F: fiedler2015state].

## Métricas e métodos de avaliação

Offset estimado e seu desvio; RTT das amostras aceitas; frequência de correções e magnitude dos saltos; erro de sincronização reportado como componente da incerteza de atraso unidirecional [F: rfc7679, §3.7.1].

## Exemplo técnico independente de domínio

```
amostras = []
repetir N vezes (ex.: 8), com intervalo:
    T1 = mono(); enviar(PING, T1)
    ao receber(PONG, T1, T2, T3): T4 = mono()
        rtt    = (T4 - T1) - (T3 - T2)
        offset = ((T2 - T1) + (T3 - T4)) / 2          # [F: rfc5905 §8]
        amostras.append((rtt, offset))
ordenar amostras por rtt; manter a metade de menor rtt     # princípio do clock filter [F: rfc5905 §10]
offset_est = mediana(offset das mantidas)
server_time(t) = t + offset_est
# correção contínua: offset_aplicado += clamp(offset_est - offset_aplicado, -k, +k) por tick
```

[I] `k` pequeno evita saltos visíveis; se a diferença for grande (reconexão), reinicializar.

## Relações com outros conceitos

Complementa `rtm.net.logical-clocks` (tempo físico vs. causal) e `rtm.net.latency` (RTT é o insumo); depende de `rtm.net.jitter` (o erro do offset é limitado pela variação de atraso); é especificada pelas normas em `rtm.std.index`; é usada por `rtm.pred.lag-compensation`, `rtm.pred.entity-interpolation`, `rtm.arch.deterministic-lockstep` e `rtm.arch.authoritative-server`.

## Lacunas e questões abertas

- Fontes específicas de jogos sobre sincronização (Simpson 2002; wiki de rede do Source; Bernier 2001) não puderam ser abertas; o procedimento na seção "Relógio cliente-servidor" é síntese do autor a partir do NTP.
- O texto do IEEE 1588 e o artigo de Cristian não foram abertos (apenas página do padrão e registro Crossref).
- Não foi encontrada medição publicada da precisão de offset obtida por aplicações sobre WebSocket/WebRTC em navegadores.
- Tratamento de skew (não só offset) em sessões longas carece de fonte específica do domínio.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc5905 | normativo | 2026-10-29 |
| rfc2330 | normativo (informativo) | 2026-10-29 |
| rfc7679 | normativo | 2026-10-29 |
| rfc2681 | normativo | 2026-10-29 |
| rfc8877 | normativo (informativo) | 2026-10-29 |
| ieee2019ptp | normativo (página do padrão) | 2026-10-29 |
| cristian1989probabilistic | academico (registro Crossref) | 2026-10-29 |
| lamport1978time | academico | 2026-10-29 |
| kulkarni2014logical | academico | 2026-10-29 |
| w3c2026hrtime | normativo | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| fiedler2015state | tecnico | 2026-10-29 |
| gambetta2014entity | tecnico | 2026-10-29 |
