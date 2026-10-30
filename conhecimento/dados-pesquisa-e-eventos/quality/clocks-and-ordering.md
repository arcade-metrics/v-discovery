---
id: dat.qual.clocks-and-ordering
titulo: Relógios de dispositivo, carimbos de evento e ordenação em dados de pesquisa
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2026hrtime, mdn2026performancenow, mdn2026eventtimestamp, mdn2026requestanimationframe, ieee2024posixclock, android2026systemclock, android2026inputevent, rfc5905, lamport1978time, cncf2026cloudevents, w3c2026pointerevents3]
relacoes:
  - { tipo: depende-de, alvo: rtm.net.clock-synchronization }
  - { tipo: depende-de, alvo: rtm.net.logical-clocks }
  - { tipo: complementa, alvo: rtm.net.ordering-and-reliability }
  - { tipo: relacionado-a, alvo: rtm.net.jitter }
  - { tipo: complementa, alvo: dat.qual.granularity-and-constructs }
  - { tipo: complementa, alvo: dat.qual.loss-and-deduplication }
  - { tipo: parte-de, alvo: dat.ev.event-model }
  - { tipo: relacionado-a, alvo: dat.ev.event-sourcing }
  - { tipo: relacionado-a, alvo: lae.dq.provenance-and-lineage }
termos: [relógio monotônico, relógio de parede, time origin, carimbo duplo, âncora de sessão, número de sequência por sessão, tempo de recebimento no servidor, step de relógio, slew, sono profundo, ordem causal]
---

# Relógios de dispositivo, carimbos de evento e ordenação em dados de pesquisa

## Definição e terminologia

Este documento trata de **qual relógio carimba cada evento de pesquisa** e de **como reconstruir a ordem** dos eventos depois da coleta. A teoria de sincronização (NTP, offset por RTT) está em `rtm.net.clock-synchronization`, e a de ordem causal (happens-before, relógios de Lamport e vetoriais, HLC) em `rtm.net.logical-clocks`; aqui elas são aplicadas ao registro de dados de interação, sem repetir a teoria [I].

Três relógios aparecem em qualquer plataforma. O **relógio de parede** acompanha o calendário e "sometimes needs to be adjusted", por isso não serve para medir desempenho nem ordenar eventos; o **relógio monotônico** nunca retrocede e não é afetado por ajustes, mas só existe dentro de uma execução do agente de usuário; a **time origin** é o zero do relógio monotônico num documento (início da navegação) ou num worker (início da execução) [F: w3c2026hrtime]. No POSIX, `CLOCK_REALTIME` mede segundos desde a Epoch e pode ser ajustado, enquanto `CLOCK_MONOTONIC` "cannot be set via clock_settime()" e conta desde "an unspecified point in the past", de modo que seu valor absoluto "is meaningless"; resoluções "are implementation-defined" e consultáveis por `clock_getres()` [F: ieee2024posixclock]. No Android, `System.currentTimeMillis()` é o relógio de parede, que "may jump backwards or forwards unpredictably"; `uptimeMillis()` é monotônico mas para em sono profundo; `elapsedRealtime()` inclui o sono e é "the recommend basis for general purpose interval timing" [F: android2026systemclock].

## Problema que resolve

Um dado de pesquisa precisa de duas coisas que nenhum relógio único entrega: intervalos exatos dentro da sessão (RT, pausas, duração de tentativas) e posição absoluta no calendário (data da sessão, alinhamento com outros registros). Usar o relógio de parede para intervalos introduz saltos: o NTPv4 corrige offsets abaixo do limiar STEPT de 125 ms por ajuste gradual, mas acima dele, depois do limiar de espera WATCH de 900 s, "the clock is stepped to the correct offset" [F: rfc5905, §11.2.3, §11.3]. Usar o relógio monotônico para tudo perde a âncora no calendário e a comparabilidade entre sessões [F: w3c2026hrtime]. Sem número de sequência, eventos que chegam fora de ordem ou duplicados não podem ser reordenados com segurança (ver `dat.qual.loss-and-deduplication`) [I].

## Fundamentos e funcionamento

### O que cada plataforma carimba

No navegador, `performance.now()` e `Event.timeStamp` são medidos em milissegundos desde a time origin, no relógio monotônico [F: mdn2026performancenow; mdn2026eventtimestamp]. O carimbo de `requestAnimationFrame` é o mesmo para todas as janelas de mesma origem no mesmo agente [F: mdn2026requestanimationframe], e os eventos coalescidos de ponteiro vêm em ordem cronológica de `timeStamp` [F: w3c2026pointerevents3, §10]. `Date.now()` é relativo à Epoch Unix e "may have been impacted by system and user clock adjustments, clock skew" [F: mdn2026performancenow]. No Android, eventos de entrada carregam `getEventTime()` "in the SystemClock.uptimeMillis() time base" [F: android2026inputevent], o relógio que para em sono profundo [F: android2026systemclock].

### Armadilhas documentadas

- **Sono e suspensão.** A especificação Level 2 exige que `performance.now()` continue contando durante o sono do sistema, mas a MDN observa que "only browsers on Windows keep ticking during sleep" e aponta bugs abertos nos demais [F: mdn2026performancenow]. Um intervalo que atravessa suspensão pode ser subestimado [I].
- **Abas ocultas.** `requestAnimationFrame` é pausado em abas de fundo na maioria dos navegadores [F: mdn2026requestanimationframe]; eventos de quadro deixam de existir sem erro aparente [I].
- **Carimbos não comparáveis entre execuções.** O relógio monotônico não permite comparar eventos de execuções diferentes [F: w3c2026hrtime]; dois documentos (por exemplo, uma página e seu worker) têm time origins distintas [I].
- **Deriva como dado sensível.** Comparar `timeOrigin` com `Date.now() - performance.now()` ao longo do tempo revela a deriva do relógio, o que a especificação trata como possível vazamento de informação do usuário [F: w3c2026hrtime]. Registrar os dois relógios por evento cria esse sinal [I].
- **Precisão do NTP.** O RFC 5905 indica precisão de "a few tens of milliseconds" para clientes na Internet [F: rfc5905, §1]. O relógio de parede de dois dispositivos não ordena eventos separados por menos que isso [I].

### Carimbo duplo com âncora de sessão

A prática que decorre dessas fontes, síntese deste documento [I]:

1. Cada evento leva o carimbo monotônico local (ms desde a time origin, ou `elapsedRealtime` no Android) e um **número de sequência** estritamente crescente por sessão e por produtor.
2. A sessão leva uma **âncora**: um par (monotônico, parede em UTC no formato RFC 3339) lido no início e repetido periodicamente e após retorno de suspensão ou visibilidade. O tempo de calendário de cada evento é derivado da âncora mais próxima, não lido por evento.
3. O servidor acrescenta **tempo de recebimento** no seu próprio relógio, sincronizado por NTP, e, se houver troca de mensagens, a estimativa de offset descrita em `rtm.net.clock-synchronization`.
4. A ordem dentro de uma sessão é a do número de sequência; entre produtores (dois dispositivos na mesma atividade), a ordem confiável é só a causal, obtida com relógio lógico ou com sequenciador central, como em `rtm.net.logical-clocks` [F: lamport1978time].

A especificação CloudEvents define o atributo `time` em RFC 3339 e admite que, se o instante da ocorrência não puder ser determinado, ele seja preenchido com outro tempo, como o atual [F: cncf2026cloudevents]. Para dados de pesquisa, essa substituição precisa ser marcada, porque transforma tempo de ocorrência em tempo de envio [I].

## Requisitos e pressupostos

O relógio monotônico precisa existir e ser lido no mesmo contexto que gera o evento; a time origin precisa ser registrada por contexto quando há mais de um (página, worker) [I]. O número de sequência precisa sobreviver a recarregamentos da página dentro da mesma sessão, o que exige persistência local (ver `dat.qual.loss-and-deduplication`) [I]. A resolução observada do relógio deve ser registrada como covariável, já que depende de navegador e de isolamento de origem cruzada [F: mdn2026eventtimestamp].

## Vantagens e limitações

O carimbo duplo separa o que é medida (intervalos monotônicos) do que é contexto (calendário), e o tempo de recebimento no servidor dá uma terceira referência independente do dispositivo [I]. Limitações: a âncora herda o erro do relógio de parede no instante da leitura; sessões que atravessam suspensão podem ter intervalos errados em plataformas que param o relógio; e a ordem entre dispositivos continua parcial [I].

## Alternativas e comparações

| Estratégia de carimbo | Intervalos dentro da sessão | Calendário | Ordem entre dispositivos | Risco principal |
|---|---|---|---|---|
| Só relógio de parede por evento | sujeitos a step e ajuste [F: rfc5905, §11.3] | sim | não, erro de dezenas de ms [F: rfc5905, §1] | saltos e intervalos negativos [I] |
| Só monotônico | exatos na resolução do relógio [F: w3c2026hrtime] | não | não | perda de âncora [I] |
| Monotônico + sequência + âncora + recebimento no servidor | exatos | derivado da âncora | causal, com sequenciador ou relógio lógico | sono e abas ocultas [F: mdn2026performancenow; mdn2026requestanimationframe] |
| Tempo do servidor estimado por offset | erro do offset | sim | aproximada | assimetria de rota, ver `rtm.net.clock-synchronization` |

## Métricas e métodos de avaliação

Intervalos negativos ou nulos entre eventos consecutivos de mesma sequência (meta zero); diferença entre o tempo derivado da âncora e o tempo de recebimento no servidor, cuja distribuição mistura latência e erro de relógio; lacunas na sequência; número de reancoragens por suspensão ou visibilidade; resolução observada do carimbo [I]. A variação de atraso entre envio e recebimento é tratada em `rtm.net.jitter`.

## Exemplo técnico independente de domínio

```
ao iniciar sessao e a cada N minutos, e em visibilitychange/resume:
    ancora = {mono: monotonic_now(), parede_utc: wall_now_rfc3339(), motivo}
    emitir(evento_ancora)
ao gerar evento e:
    seq += 1; persistir(seq)
    e.env = {sessao, produtor, seq, mono: e.timeStamp_monotonico, contexto: "doc"|"worker"}
no servidor ao receber:
    e.env.recebido_utc = server_wall_now()
na analise:
    ordenar por (sessao, produtor, seq)
    intervalo(a, b) = b.mono - a.mono         # so dentro do mesmo contexto e sem ancora de resume entre eles
    calendario(e) = ancora_previa.parede_utc + (e.mono - ancora_previa.mono)
```

## Relações com outros conceitos

Depende de `rtm.net.clock-synchronization` (offset e NTP) e de `rtm.net.logical-clocks` (ordem causal); complementa `rtm.net.ordering-and-reliability`, que trata ordem no transporte. É parte do envelope definido em `dat.ev.event-model` e alimenta a reconstrução de estado em `dat.ev.event-sourcing`. Fornece os carimbos de que `dat.qual.granularity-and-constructs` precisa e a sequência que `dat.qual.loss-and-deduplication` usa para detectar lacunas. A âncora e o tempo de recebimento são metadados de linhagem no sentido de `lae.dq.provenance-and-lineage`.

## Lacunas e questões abertas

- Não foi aberta documentação equivalente para iOS (relógios de sistema e carimbo de eventos de toque); o comportamento em sono fica por verificar.
- O bug de `performance.now()` em suspensão fora do Windows foi verificado só pela nota da MDN; o estado atual de cada navegador não foi conferido.
- Não foi encontrada fonte que meça o erro típico da âncora de parede em dispositivos móveis de consumo.
- Falta avaliar se registrar deriva de relógio por sessão precisa de base legal específica, dado o risco de identificação apontado pela especificação W3C.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2026hrtime | normativo | 2026-10-30 |
| w3c2026pointerevents3 | normativo | 2026-10-30 |
| ieee2024posixclock | normativo | 2026-10-30 |
| rfc5905 | normativo | 2026-10-30 |
| cncf2026cloudevents | normativo | 2026-10-30 |
| mdn2026performancenow | fornecedor | 2026-10-30 |
| mdn2026eventtimestamp | fornecedor | 2026-10-30 |
| mdn2026requestanimationframe | fornecedor | 2026-10-30 |
| android2026systemclock | fornecedor | 2026-10-30 |
| android2026inputevent | fornecedor | 2026-10-30 |
| lamport1978time | academico | 2026-10-30 |
