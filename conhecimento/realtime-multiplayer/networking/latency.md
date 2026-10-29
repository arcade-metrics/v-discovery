---
id: rtm.net.latency
titulo: Latência (RTT, atraso unidirecional, componentes, limites físicos, medição, efeito na interatividade)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc2681, rfc7679, rfc2330, rfc6298, rfc9002, cheshire1996latency, gambetta2014client, gambetta2014entity, claypool2006report, claypool2006latency, fiedler2008udp, fiedler2008reliability, fiedler2010what, riot2020valorant, fiedler2014snapshot]
relacoes:
  - { tipo: complementa, alvo: rtm.net.jitter }
  - { tipo: complementa, alvo: rtm.net.bandwidth }
  - { tipo: complementa, alvo: rtm.net.packet-loss }
  - { tipo: depende-de, alvo: rtm.net.clock-synchronization }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
  - { tipo: avaliado-por, alvo: rtm.perf.qoe-thresholds }
  - { tipo: especificado-por, alvo: rtm.std.index }
termos: [latência, RTT, atraso unidirecional, atraso de propagação, atraso de serialização, atraso de enfileiramento, atraso de processamento, wire time, SRTT, ping]
---

# Latência

## Definição e terminologia

**Latência** é o tempo entre a emissão de uma informação e sua chegada ao destino. Duas métricas normativas:

- **Atraso unidirecional** (*one-way delay*): o RFC 7679 define `Type-P-One-way-Delay` como `dT` quando a origem envia o primeiro bit no *wire time* `T` e o destino recebe o último bit em `T+dT`; é indefinido (informalmente infinito) se o pacote não chega dentro de `Tmax` [F: rfc7679, §3.4].
- **Atraso de ida e volta** (*round-trip delay*, RTT): o RFC 2681 define `Type-P-Round-trip-Delay` como o tempo do primeiro bit do pacote de teste até o último bit da resposta, enviada imediatamente pelo destino [F: rfc2681, §2.4].

*Wire time* é o instante em que o bit aparece no enlace observado, não o instante em que o host o processa; o RFC 2330 recomenda definir métricas em *wire time* para separar atraso de rede de atraso de host [F: rfc2330, §10.2].

"Ping" é o nome coloquial da medição de RTT por ICMP Echo; o RFC 2681 cita que é frequentemente possível medir ida e volta "without installing measurement-specific software" [F: rfc2681, §1.1].

O que latência **não** é: largura de banda. Cheshire argumenta que fabricantes dizem "speed" quando querem dizer "capacity", que banda pode ser comprada agregando enlaces mas "no amount of money can turn any number of them into a link with good latency" [F: cheshire1996latency].

## Problema que resolve

Entender latência resolve a pergunta "qual o atraso mínimo e típico entre uma ação e seu efeito observado?", que delimita o que uma arquitetura pode esconder e o que precisa ser compensado por predição ou interpolação [I].

## Fundamentos e funcionamento

### Componentes

Decomposição clássica do atraso de um pacote em um caminho [I], com apoio nas fontes:

| Componente | Origem | Depende de |
|---|---|---|
| propagação | velocidade do sinal no meio | distância física |
| serialização (transmissão) | colocar os bits no enlace | tamanho do pacote / taxa do enlace |
| enfileiramento | espera em filas de roteadores | carga da rede |
| processamento | roteamento, pilha de rede, aplicação | hardware e software |

O RFC 7679 afirma que o **valor mínimo** observado "suggests propagation and transmission delay" e que valores acima do mínimo indicam congestionamento no caminho [F: rfc7679, §1.1]; o RFC 2681 diz o mesmo para o RTT mínimo [F: rfc2681, §1.1].

### Limites físicos

Cheshire usa a velocidade da luz no vácuo, 300 × 10^6 m/s, e em fibra cerca de 66% disso, 200 × 10^6 m/s; para Stanford–Boston (4320 km) o atraso teórico unidirecional é 21,6 ms e o RTT 43,2 ms, contra um ping medido de cerca de 85 ms [F: cheshire1996latency]. Gambetta estima que 4000 km à velocidade da luz levam cerca de 13 ms, e assume 50 ms unidirecionais como melhor caso realista, com 100 a 500 ms comuns [F: gambetta2014client]. [I] A diferença entre o limite físico e o medido é enfileiramento, processamento e rota não geodésica.

### Serialização e o "último quilômetro"

Cheshire mostra que, num modem de 33 kbit/s, transmitir 10 caracteres leva 2,4 ms mas o total chega a 102,4 ms pela latência do dispositivo; modems típicos somavam cerca de 100 ms, "roughly 300 times worse" que Ethernet (~0,3 ms) [F: cheshire1996latency]. Claypool e Claypool registram LANs "well under 10 milliseconds" e modems discados que "can add 100s of milliseconds" [F: claypool2006report, §1].

### RTT ≠ 2 × unidirecional

O RFC 7679 justifica medir cada sentido porque, com rotas assimétricas, "round-trip measurements actually measure the performance of two distinct paths together", e mesmo em rotas simétricas o enfileiramento pode ser assimétrico [F: rfc7679, §1.1]. O RFC 2681 acrescenta que não se pode, em geral, somar dois atrasos unidirecionais para obter o RTT, pois a resposta precisa ser disparada pelo pacote de ida [F: rfc2681, §2.6].

### Latência fim a fim em sistemas interativos

A latência percebida inclui mais do que a rede. O relato técnico sobre um jogo competitivo decompõe o "peeker's advantage" em buffers de servidor (2 quadros: 0,5 de espera, 0,5 de buffer de rede, 1 para aplicar e difundir) e de cliente (3 quadros: 0,5 de espera, 1 de buffer de rede, 0,5 de GPU/swap chain) somados ao RTT de rede; com 35 ms de RTT e cliente a 60 FPS, servidor a 128 ticks reduz a vantagem em cerca de 40 ms (28%) [F: riot2020valorant]. A interpolação de entidades adiciona deliberadamente um intervalo de atualização (100 ms a 10 atualizações/s) para mostrar os outros jogadores "in the past" [F: gambetta2014entity]; Fiedler mede 350 ms de atraso de interpolação a 10 pacotes/s com perda e jitter [F: fiedler2014snapshot].

## Algoritmos e modelos relevantes

- **Estimador suavizado de RTT** (TCP): `SRTT` e `RTTVAR` com `alpha = 1/8`, `beta = 1/4`, `RTO = SRTT + max(G, 4·RTTVAR)`, RTO inicial de 1 s e mínimo recomendado de 1 s [F: rfc6298, §2]. QUIC usa `smoothed_rtt = 7/8·smoothed_rtt + 1/8·adjusted_rtt`, `rttvar = 3/4·rttvar + 1/4·|smoothed_rtt − adjusted_rtt|`, mantém `min_rtt` como menor amostra e desconta o atraso de ACK informado pelo par [F: rfc9002, §5.2-5.3].
- **Estatísticas IPPM**: percentil, mediana e mínimo sobre a amostra, com valores indefinidos tratados como infinitos [F: rfc7679, §5].
- Fiedler usa média móvel exponencial com peso 10% por pacote para o RTT da camada de aplicação [F: fiedler2008reliability].

## Requisitos e pressupostos

Medir atraso unidirecional exige relógios sincronizados: "it will be important for Src and Dst to synchronize very closely" e qualquer erro de sincronização soma diretamente ao erro de medição [F: rfc7679, §3.5, §3.7.1]. RTT dispensa isso: só o relógio da origem importa ("self-synchronization") [F: rfc2681, §2.7.1]. Ver `rtm.net.clock-synchronization`.

## Vantagens e limitações

RTT é fácil de medir e suficiente para estimar o custo de uma troca cliente-servidor; não revela assimetria nem a direção congestionada [F: rfc7679, §1.1]. Atraso unidirecional é mais informativo, mas depende de sincronização cujo erro é da mesma ordem do que se quer medir [F: rfc7679, §3.7.1].

## Alternativas e comparações

Efeito da latência por classe de ação, segundo a taxonomia precisão × deadline [F: claypool2006report, §4-6; claypool2006latency]:

| Modelo | Perspectiva | Sensibilidade | Limiar |
|---|---|---|---|
| avatar | primeira pessoa (FPS, corrida) | alta | 100 ms |
| avatar | terceira pessoa (esporte, RPG) | média | 500 ms |
| omnipresente | variável (RTS, simulação) | baixa | 1000 ms |

Os autores alertam que o limiar exato "depends upon the game and to some extent the player" [F: claypool2006report, §6]. No extremo competitivo, jogadores detectaram diferenças de cerca de 10 ms e desfechos frequentemente se decidiram em 20 a 50 ms [F: riot2020valorant].

## Métricas e métodos de avaliação

- RTT por amostra e estatísticas (mín., mediana, percentis) [F: rfc2681; rfc7679, §5].
- Atraso unidirecional com relógios sincronizados [F: rfc7679].
- Latência fim a fim "input-to-photon" decomposta em quadros de cliente e servidor [F: riot2020valorant].
- Ver `rtm.perf.metrics` e `rtm.perf.qoe-thresholds`.

## Exemplo técnico independente de domínio

Estimador de RTT na camada de aplicação, no espírito do RFC 6298:

```
ao enviar pacote seq:   t_envio[seq] = agora()
ao receber ack(seq):    amostra = agora() - t_envio[seq]
    if primeira: srtt = amostra; rttvar = amostra/2
    else:
        rttvar = (1 - 1/4)*rttvar + (1/4)*|srtt - amostra|
        srtt   = (1 - 1/8)*srtt   + (1/8)*amostra
    min_rtt = min(min_rtt, amostra)        # ~ propagação + serialização
    fila_estimada = srtt - min_rtt          # ~ enfileiramento atual
```

[I] `min_rtt` aproxima o piso físico; `srtt − min_rtt` aproxima o componente variável, útil para dimensionar buffers (ver `rtm.net.jitter`).

## Relações com outros conceitos

Complementa `rtm.net.jitter`, `rtm.net.bandwidth` e `rtm.net.packet-loss` (as quatro propriedades de rede do domínio); depende de `rtm.net.clock-synchronization` para medidas unidirecionais; é compensada por `rtm.pred.client-side-prediction`, `rtm.pred.lag-compensation` e `rtm.pred.entity-interpolation`; é avaliada em `rtm.perf.metrics` e `rtm.perf.qoe-thresholds`; as RFCs citadas estão indexadas em `rtm.std.index`.

## Lacunas e questões abertas

- Os limiares de Claypool datam de 2006 e de jogos específicos; faltam dados equivalentes para colaboração e jogos por turno.
- A decomposição de latência de entrada (input-to-photon) só foi verificada em um relato de fornecedor; não há fonte normativa.
- Não foi aberto o artigo de Bernier (2001) sobre compensação de latência (acesso bloqueado); referências a ele devem ser tratadas como não verificadas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc2681 | normativo | 2026-10-29 |
| rfc7679 | normativo | 2026-10-29 |
| rfc2330 | normativo (informativo) | 2026-10-29 |
| rfc6298 | normativo | 2026-10-29 |
| rfc9002 | normativo | 2026-10-29 |
| cheshire1996latency | tecnico | 2026-10-29 |
| gambetta2014client | tecnico | 2026-10-29 |
| gambetta2014entity | tecnico | 2026-10-29 |
| claypool2006report | academico | 2026-10-29 |
| claypool2006latency | academico (registro Crossref) | 2026-10-29 |
| fiedler2008udp | tecnico | 2026-10-29 |
| fiedler2008reliability | tecnico | 2026-10-29 |
| fiedler2010what | tecnico | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| riot2020valorant | tecnico | 2026-10-29 |
