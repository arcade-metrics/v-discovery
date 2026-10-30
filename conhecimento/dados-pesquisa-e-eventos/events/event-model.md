---
id: dat.ev.event-model
titulo: Modelo de evento (envelope, identidade, tipo, versão e contexto)
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [cncf2026cloudevents, cncf2026cloudeventsseq, cncf2026cloudeventsdt, otel2026logsdatamodel, otel2026semconvevents, adl2016xapidata, microsoft2026eventsourcing, young2017versioning, serranolaguna2017applying]
relacoes:
  - { tipo: complementa, alvo: dat.ev.event-sourcing }
  - { tipo: complementa, alvo: dat.ev.event-to-xapi-mapping }
  - { tipo: complementa, alvo: dat.ev.instrumentation-and-opentelemetry }
  - { tipo: complementa, alvo: dat.ev.game-telemetry }
  - { tipo: complementa, alvo: dat.qual.schema-validation-and-evolution }
  - { tipo: complementa, alvo: dat.qual.clocks-and-ordering }
  - { tipo: complementa, alvo: dat.qual.loss-and-deduplication }
  - { tipo: relacionado-a, alvo: dat.qual.granularity-and-constructs }
  - { tipo: relacionado-a, alvo: iop.fund.dados-vs-protocolo }
  - { tipo: relacionado-a, alvo: rtm.net.clock-synchronization }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: complementa, alvo: lae.dq.provenance-and-lineage }
termos: [evento, ocorrência, envelope, atributos de contexto, payload, tipo de evento, versão de esquema, dataschema, fonte, sequência, timestamp de ocorrência, timestamp de observação, fonte de relógio, evento de interação]
---

# Modelo de evento

## Definição e terminologia

A especificação CloudEvents distingue **ocorrência**, "the capture of a statement of fact during the operation of a software system", de **evento**, "a data record expressing an occurrence and its context"; o evento traz dois tipos de informação, os dados da ocorrência (*event data*, o payload) e metadados de contexto, e uma mesma ocorrência pode gerar mais de um evento [F: cncf2026cloudevents, §Notations and Terminology]. Neste documento, **envelope** é o conjunto de atributos de contexto que podem ser lidos sem desserializar o payload, como a especificação descreve: "designed such that they can be serialized independent of the event data" [F: cncf2026cloudevents, §Context Attributes]. **Evento de interação** é o evento cuja ocorrência é uma ação do aprendiz sobre um elemento de uma atividade (toque, escolha, resposta, abandono) [I].

O que o modelo de evento não é: não é o protocolo de transporte (HTTP, fila, WebSocket), que a CloudEvents trata em *bindings* separados; não é o vocabulário de domínio (que verbos e tipos existem), que fica em perfis ou convenções semânticas; e não é o armazenamento, que pode ser log append-only (`dat.ev.event-sourcing`) ou tabela analítica [I].

## Problema que resolve

Produtores descrevem eventos de formas diferentes, o que obriga consumidores a reaprender cada formato e impede ferramentas genéricas de roteamento e rastreio [F: cncf2026cloudevents, §Overview]. Em pesquisa há um problema adicional: o evento precisa servir de **evidência** meses depois, quando o software, o conteúdo e a configuração já mudaram. Sem versão de esquema, versão de conteúdo e configuração ativa registradas no próprio evento, a reinterpretação depende de memória institucional [I]. Young descreve o caso extremo: uma série de leituras "27, 27, 27, 80.6, 80.6" de um termostato não permite saber se a temperatura subiu ou se a unidade mudou de Celsius para Fahrenheit, e "semantic meaning cannot change between versions of software" [F: young2017versioning, General Versioning Concerns].

## Fundamentos e funcionamento

### O envelope mínimo de referência (CloudEvents 1.0.2)

A CloudEvents exige quatro atributos e define quatro opcionais [F: cncf2026cloudevents, §REQUIRED Attributes, §OPTIONAL Attributes]:

| Atributo | Obrigatório | Semântica normativa |
|---|---|---|
| `id` | sim | "`source` + `id`" deve ser único por evento distinto; reenvio por erro de rede pode repetir o `id`, e consumidores podem tratar `source`+`id` iguais como duplicata |
| `source` | sim | URI-reference do contexto em que a ocorrência aconteceu; URI absoluta recomendada |
| `specversion` | sim | versão da especificação (`1.0`) |
| `type` | sim | tipo da ocorrência, definido pelo produtor, deve ter prefixo DNS reverso |
| `datacontenttype` | não | tipo de mídia do payload (RFC 2046) |
| `dataschema` | não | URI do esquema do payload; mudanças incompatíveis devem gerar URI diferente |
| `subject` | não | sujeito do evento no contexto da `source`, para filtragem sem ler o payload |
| `time` | não | instante da ocorrência (RFC 3339); se não determinável, todos os produtores da mesma `source` devem usar o mesmo algoritmo |

Nomes de atributo são ASCII minúsculo e dígitos, recomendados até 20 caracteres; extensões seguem as mesmas regras e "have no defined meaning in this specification" [F: cncf2026cloudevents, §Attribute Naming Convention, §Extension Context Attributes]. A extensão `sequence` acrescenta a posição do evento na sequência de uma `source`, string ordenável lexicograficamente, recomendada monotônica e contígua; com `sequencetype=Integer` começa em 1 e cresce de 1 em 1 [F: cncf2026cloudeventsseq]. A extensão de rastreio distribuído carrega `traceparent` e `tracestate` do W3C Trace Context [F: cncf2026cloudeventsdt].

### Dois relógios, não um

O modelo de logs do OpenTelemetry separa `Timestamp`, "time when the event occurred measured by the origin clock", de `ObservedTimestamp`, o instante em que o sistema de coleta observou o evento, ambos em nanossegundos desde a época UNIX [F: otel2026logsdatamodel, §Field: Timestamp, §Field: ObservedTimestamp]. O xAPI faz a mesma distinção entre `timestamp` (quando a experiência ocorreu) e `stored` (quando o LRS gravou), e a norma admite que "there can be delays" entre os dois [F: adl2016xapidata, §2.4.7, §2.4.8]. Nenhum dos dois padrões registra **qual relógio** produziu o carimbo nem seu desvio estimado; para evidência, isso precisa ir para uma extensão [I] (ver `dat.qual.clocks-and-ordering`).

### Versão de esquema e versão de tipo

A documentação da Microsoft lista estratégias de evolução: desserialização tolerante, "include a version identifier in each event, either as metadata in the event envelope or as part of the event type name", *upcasting* na leitura e, como último recurso, migração no lugar, que "undermines the audit trail" [F: microsoft2026eventsourcing, Problems and considerations]. Young descreve as duas famílias: versionamento por tipo (`Evento_v1`, `Evento_v2`, sempre aditivo) e esquema fraco, em que o JSON é mapeado ao tipo com regras simples (campo presente nos dois → valor do JSON; só no JSON → ignorado; só no tipo → valor padrão) [F: young2017versioning, Basic Type Based Versioning; Weak Schema].

## Requisitos e pressupostos

- Identificador estável por produtor e contador ou relógio monotônico local, para que `source`+`id`+`sequence` permitam deduplicar e ordenar sem confiar no relógio de parede [I].
- Registro de esquemas acessível por URI, para que `dataschema` resolva anos depois [I].
- Política de minimização: a CloudEvents determina que "sensitive information SHOULD NOT be carried or represented in context attributes", porque intermediários podem inspecionar e registrar esses atributos [F: cncf2026cloudevents, §Privacy and Security].

## Vantagens e limitações

Vantagens [I]: envelope separado do payload permite roteamento, deduplicação e auditoria sem conhecer o domínio; versão explícita torna a reinterpretação mecânica; dois carimbos de tempo expõem atraso de entrega.

Limitações: a CloudEvents não define semântica de domínio nem de tempo além de "quando a ocorrência aconteceu" [F: cncf2026cloudevents, §time]; eventos devem ser compactos, já que intermediários só são obrigados a encaminhar até 64 KByte [F: cncf2026cloudevents, §Size Limits]; e um envelope genérico não diz nada sobre o que o pesquisador precisa para interpretar o evento como medida [I].

## Alternativas e comparações

| Modelo | Identidade | Tempo | Versão de esquema | Domínio |
|---|---|---|---|---|
| CloudEvents 1.0.2 | `source`+`id` | `time` (opcional) | `dataschema`, ou no `type` | nenhum |
| OTel EventRecord | sem id obrigatório | `Timestamp` + `ObservedTimestamp` | Schema URL do recurso | `EventName` + atributos |
| xAPI statement | `id` UUID | `timestamp` + `stored` | `version` da especificação; conteúdo em `context.revision` | actor-verb-object |
| Evento de interação (Serrano-Laguna et al.) | não define | `timestamp` | não define | ação, alvo, valor |

Fontes da tabela: [F: cncf2026cloudevents], [F: otel2026logsdatamodel], [F: otel2026semconvevents], [F: adl2016xapidata], [F: serranolaguna2017applying, §3]. O xAPI é um caso especial de modelo de evento com semântica de aprendizagem embutida; os demais são envelopes genéricos [I].

## Exemplo técnico independente de domínio

Envelope proposto para um evento de interação em atividade lúdica, como síntese deste documento [I]; campos `x*` são extensões no sentido CloudEvents:

```
specversion   "1.0"
id            "e-000193"                  # único por source
source        "urn:produtor:<instalacao>/<dispositivo-pseudonimo>"
type          "org.exemplo.atividade.resposta.v3"
dataschema    "https://exemplo.org/esquemas/resposta/3.1.0"
subject       "<sessao-id>"
time          "2026-10-30T13:04:11.120Z"  # relógio de parede do dispositivo
sequence      "193"  sequencetype "Integer"   # por sessão
xmonotonicns  "8812340000"                # offset monotônico desde início da sessão
xclocksource  "device-wall;ntp-offset=-38ms;sync=2026-10-30T12:58Z"
xcontentver   "atividade-17@2.4.0"        # versão do conteúdo
xconfighash   "sha256:9f2c..."            # configuração ativa (dificuldade, acessibilidade)
traceparent   "00-<trace-id>-<span-id>-01"
data          { ator: "<pseudonimo>", alvo: "item-17", acao: "selecionou",
                valor: "B", correto: false, latencia_ms: 1840, tentativa: 2 }
```

## Relações com outros conceitos

Base de `dat.ev.event-to-xapi-mapping` (o envelope precisa conter tudo que o statement exige) e de `dat.ev.event-sourcing` (o evento é a unidade do log). `dat.ev.instrumentation-and-opentelemetry` trata os carimbos e o contexto de rastreio; `dat.qual.schema-validation-and-evolution`, `dat.qual.clocks-and-ordering` e `dat.qual.loss-and-deduplication` aprofundam versão, tempo e duplicatas. A separação entre modelo e transporte retoma `iop.fund.dados-vs-protocolo`; a minimização segue `psg.access.minimization-and-privacy-by-design`; a proveniência do evento como dado de pesquisa liga-se a `lae.dq.provenance-and-lineage`.

## Lacunas e questões abertas

- Nenhuma das especificações lidas padroniza a declaração da fonte de relógio e do desvio estimado; os nomes `xclocksource` e `xmonotonicns` acima são ilustrativos.
- Falta verificar se registros de esquema (JSON Schema, Avro) oferecem URI estável adequada a `dataschema` por prazos de pesquisa (ver `dat.qual.schema-validation-and-evolution`).
- Não foi encontrada orientação normativa sobre como representar "configuração ativa" de forma compacta e reprodutível; hash de configuração exige que o documento de configuração seja arquivado à parte.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| cncf2026cloudevents | normativo | 2026-10-30 |
| cncf2026cloudeventsseq | normativo | 2026-10-30 |
| cncf2026cloudeventsdt | normativo | 2026-10-30 |
| otel2026logsdatamodel | normativo | 2026-10-30 |
| otel2026semconvevents | normativo (Development) | 2026-10-30 |
| adl2016xapidata | normativo | 2026-10-30 |
| microsoft2026eventsourcing | fornecedor | 2026-10-30 |
| young2017versioning | tecnico | 2026-10-30 |
| serranolaguna2017applying | academico | 2026-10-30 |
