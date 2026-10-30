---
id: dat.ev.instrumentation-and-opentelemetry
titulo: Instrumentação e OpenTelemetry como referência
tipo: framework
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [otel2026overview, otel2026logsdatamodel, otel2026semconvevents, otel2026semconvsession, otel2026contextpropagation, otel2026schemas, w3c2021tracecontext, cncf2026cloudeventsdt]
relacoes:
  - { tipo: depende-de, alvo: dat.ev.event-model }
  - { tipo: complementa, alvo: dat.ev.game-telemetry }
  - { tipo: complementa, alvo: dat.qual.clocks-and-ordering }
  - { tipo: complementa, alvo: dat.qual.schema-validation-and-evolution }
  - { tipo: complementa, alvo: dat.qual.loss-and-deduplication }
  - { tipo: relacionado-a, alvo: rtm.net.clock-synchronization }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: psg.audit.audit-trails }
termos: [instrumentação, OpenTelemetry, sinal, trace, span, métrica, log, LogRecord, EventRecord, EventName, Timestamp, ObservedTimestamp, resource, semantic conventions, context propagation, propagator, traceparent, tracestate, baggage, telemetry schema, schema URL]
---

# Instrumentação e OpenTelemetry

## Definição e terminologia

**Instrumentação** é o código inserido no software para emitir dados sobre sua própria execução [I]. O OpenTelemetry (OTel) organiza essa emissão em **sinais**, cada um "a specialized form of observability" (traces, métricas, logs e baggage), que compartilham um subsistema comum de **propagação de contexto** mas funcionam de forma independente [F: otel2026overview, §OpenTelemetry Client Architecture]. Cada sinal tem API, SDK, convenções semânticas e pacotes contrib [F: otel2026overview]. A versão da especificação consultada é a 1.62.0 e a das convenções semânticas, 1.44.0 (rótulos do site em 2026-10-30).

- **Span**: operação com nome, início e fim, atributos, eventos com carimbo próprio, pai e links; um **trace** é um grafo acíclico de spans [F: otel2026overview, §Spans, §Traces].
- **LogRecord / EventRecord**: um registro de log com `EventName` não vazio é um **Event**; o nome "SHOULD uniquely identify the event structure (both attributes and body)" [F: otel2026logsdatamodel, §Field: EventName].
- **Resource**: a entidade que produz a telemetria, como aplicação ou infraestrutura [F: otel2026overview, §Resources].
- **Semantic conventions**: chaves e valores padronizados para conceitos comuns [F: otel2026overview, §Semantic Conventions].

O que não é: o OTel é um framework de **observabilidade operacional**. Ele não define vocabulário de aprendizagem nem garante completude dos dados; serve aqui como referência de desenho de envelope, tempo e contexto, não como destino obrigatório dos eventos de pesquisa [I].

## Problema que resolve

Sem convenções, cada equipe nomeia atributos de um jeito, e correlacionar eventos do cliente com processamento no servidor exige casamento manual. O OTel resolve correlação (contexto propagado), nomenclatura (convenções semânticas) e evolução (telemetry schemas) [F: otel2026overview] [F: otel2026schemas, §Motivation].

## Fundamentos e funcionamento

### Quando um evento, quando um span

A convenção de eventos define eventos como "named occurrences at a meaningful point in time" e cita como exemplos interações de usuário, transições de estado e avaliações de feature flag. Operações com duração e fronteira significativa devem ser spans; propriedades da operação inteira, atributos de span [F: otel2026semconvevents, §When to define events]. Em atividade lúdica, uma tentativa de nível é candidata a span e cada resposta dentro dela a evento [I].

### Regras de evento

O nome do evento é obrigatório, não pode conter valores dinâmicos e deve ser de baixa cardinalidade [F: otel2026semconvevents, §Event name]. `Timestamp` deve ser o instante da ocorrência; convenções não podem definir `ObservedTimestamp`, que SDKs e coletores preenchem [F: otel2026semconvevents, §Timestamps]. Atributos devem ser documentados, inclusive os que "may contain sensitive information, be expensive to collect, or be especially large" [F: otel2026semconvevents, §Attributes]. A convenção de eventos está em status *Development* [F: otel2026semconvevents].

### Tempo

`Timestamp` é medido pelo relógio de origem e é opcional quando desconhecido; `ObservedTimestamp` é medido pelo relógio do coletor; para formatos com um só carimbo, recomenda-se usar `Timestamp` se presente e `ObservedTimestamp` caso contrário [F: otel2026logsdatamodel, §Field: Timestamp, §Field: ObservedTimestamp]. A diferença entre os dois é uma estimativa do atraso de entrega, mas inclui o erro do relógio do dispositivo [I] (ver `dat.qual.clocks-and-ordering`).

### Sessão

`session.id` identifica a sessão em todos os sinais; `session.start` deve ser emitido a cada nova sessão e `session.previous_id` encadeia continuações [F: otel2026semconvsession]. Ambos os atributos são *Opt-In* e *Development* [F: otel2026semconvsession].

### Propagação de contexto e W3C Trace Context

Contexto é o objeto que permite correlacionar um sinal com outro entre serviços; propagação é o mecanismo que o serializa, e o propagador padrão do OTel usa os cabeçalhos do W3C Trace Context [F: otel2026contextpropagation]. A Recomendação W3C de 23 de novembro de 2021 define `traceparent` com quatro campos: `version` (`00`), `trace-id` (16 bytes), `parent-id` (8 bytes) e `trace-flags` (8 bits, só `sampled` definido), todos em hexadecimal minúsculo; valores só com zeros são inválidos [F: w3c2021tracecontext, §3.2]. A extensão de rastreio distribuído da CloudEvents leva esse contexto para dentro do evento e, em múltiplos saltos, deve carregar o trace inicial da transmissão [F: cncf2026cloudeventsdt].

### Telemetry schemas

Esquemas de telemetria são versionados, identificados por Schema URL única por versão e declaram transformações entre versões; quando a conversão não é possível, há quebra de compatibilidade [F: otel2026schemas, §How Schemas Work]. É o mesmo problema da versão de esquema de evento de pesquisa, resolvido por URL resolvível [I].

## Requisitos e pressupostos

- Relógio do dispositivo minimamente sincronizado, ou registro do desvio, para que `Timestamp` tenha significado [I].
- Coletor que preserve todos os eventos de pesquisa: amostragem de traces é aceitável para diagnóstico, não para dados de estudo [I].
- Privacidade: o W3C determina que fornecedores "MUST NOT use traceparent and tracestate fields for any personally identifiable or otherwise sensitive information" e que geradores aleatórios não podem usar dados identificáveis como semente [F: w3c2021tracecontext, §6, §6.1].

## Vantagens e limitações

Vantagens: separação explícita entre tempo de ocorrência e de observação [F: otel2026logsdatamodel]; correlação cliente-servidor padronizada [F: w3c2021tracecontext]; mecanismo formal de evolução por Schema URL [F: otel2026schemas].

Limitações: convenções de eventos e de sessão ainda em *Development* [F: otel2026semconvevents] [F: otel2026semconvsession]; a especificação W3C reconhece que o `traceparent` permite correlacionar requisições de uma mesma transação e inferir identidade do chamador, embora classifique o risco como "theoretical rather than practical" [F: w3c2021tracecontext, §6.1]; não há semântica pedagógica [I].

## Alternativas e comparações

| Referência | Foco | Tempo | Correlação | Vocabulário |
|---|---|---|---|---|
| OpenTelemetry | observabilidade | ocorrência + observação | trace/span, sessão | técnico (HTTP, BD, sessão) |
| CloudEvents | interoperabilidade de eventos | `time` | extensão `traceparent` | nenhum |
| xAPI | registro de aprendizagem | `timestamp` + `stored` | `registration`, `contextActivities` | aberto, por perfis |

Síntese a partir de [F: otel2026logsdatamodel], [F: cncf2026cloudeventsdt] e `dat.ev.event-to-xapi-mapping` [I].

## Exemplo técnico independente de domínio

```
span "nivel.tentativa"  trace_id=T  span_id=A  start=t0  end=t5
  resource: {service.name: "cliente-atividade", service.version: "2.4.0"}
  attrs:    {session.id: S, nivel.id: "n3", tentativa: 2}
  event "atividade.resposta"  Timestamp=t2  ObservedTimestamp=t2'
        attrs {item.id: "i17", resposta: "B", correta: false, latencia_ms: 1840}
envio HTTP ao coletor com  traceparent: 00-T-A-01
```

## Relações com outros conceitos

Depende de `dat.ev.event-model` e o complementa com regras de tempo e contexto. `dat.qual.clocks-and-ordering` e `rtm.net.clock-synchronization` tratam sincronização; `dat.qual.schema-validation-and-evolution`, a evolução que o OTel resolve por Schema URL; `dat.qual.loss-and-deduplication`, a completude que a amostragem ameaça. Os limites de privacidade se alinham a `psg.access.minimization-and-privacy-by-design`; logs de execução também alimentam `psg.audit.audit-trails`.

## Lacunas e questões abertas

- Não foi verificado o estado da Trace Context Level 2 nem se ela altera `trace-flags`.
- Falta avaliar a viabilidade de usar o pipeline OTel (SDK e coletor) como transporte de eventos de pesquisa sem amostragem, com garantia de entrega.
- O OTel não tem convenção para "versão de conteúdo" ou "configuração ativa"; o uso de `service.version` cobre só o software.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| otel2026overview | normativo | 2026-10-30 |
| otel2026logsdatamodel | normativo | 2026-10-30 |
| otel2026semconvevents | normativo (Development) | 2026-10-30 |
| otel2026semconvsession | normativo (Development) | 2026-10-30 |
| otel2026contextpropagation | fornecedor | 2026-10-30 |
| otel2026schemas | normativo | 2026-10-30 |
| w3c2021tracecontext | normativo | 2026-10-30 |
| cncf2026cloudeventsdt | normativo | 2026-10-30 |
