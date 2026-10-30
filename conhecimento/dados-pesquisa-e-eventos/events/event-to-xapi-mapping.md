---
id: dat.ev.event-to-xapi-mapping
titulo: Mapeamento de evento interno para xAPI sem perda
tipo: tecnica
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [adl2016xapidata, ieee2026xapibasedocs, ieee2023xapi, adl2017xapiprofiles, adl2017adlvocab, serranolaguna2017applying, otel2026logsdatamodel]
relacoes:
  - { tipo: depende-de, alvo: dat.ev.event-model }
  - { tipo: especificado-por, alvo: iop.lr.xapi }
  - { tipo: complementa, alvo: iop.lr.cmi5 }
  - { tipo: relacionado-a, alvo: iop.lr.caliper }
  - { tipo: relacionado-a, alvo: iop.lr.comparison }
  - { tipo: depende-de, alvo: iop.fund.mapeamento-e-proveniencia }
  - { tipo: complementa, alvo: dat.ev.event-sourcing }
  - { tipo: complementa, alvo: dat.ev.game-telemetry }
  - { tipo: complementa, alvo: dat.qual.schema-validation-and-evolution }
  - { tipo: complementa, alvo: dat.qual.clocks-and-ordering }
  - { tipo: complementa, alvo: kg.std.prov-o }
  - { tipo: relacionado-a, alvo: psg.deid.anonymization-and-pseudonymization }
termos: [mapeamento sem perda, projeção xAPI, statement, xAPI Profile, Statement Template, Pattern, extensão de contexto, extensão de resultado, IRI de verbo, registration, revision, platform, contextAgents, ida e volta, perda por precisão]
---

# Mapeamento de evento interno para xAPI sem perda

## Definição e terminologia

**Mapeamento sem perda** é uma função do evento interno para um statement xAPI tal que o evento original possa ser reconstruído a partir do statement (ida e volta) sem ambiguidade de valor, tempo ou significado [I]. Este documento trata do esquema interno e da projeção; a especificação xAPI em si está em `iop.lr.xapi`, e a comparação com Caliper e cmi5 em `iop.lr.comparison`.

Versões consideradas: xAPI 1.0.3 (ADL, 2016) [F: adl2016xapidata] e xAPI 2.0, normalizada como IEEE 9274.1.1-2023 [F: ieee2023xapi, metadados], cujo texto base é publicado em repositório aberto do IEEE com changelog em relação à 1.0.3 [F: ieee2026xapibasedocs]. **xAPI Profile** é o documento JSON-LD que define conceitos (verbos, tipos de atividade, extensões), **Statement Templates** e **Patterns** [F: adl2017xapiprofiles, §3.0].

## Problema que resolve

O xAPI fixa a estrutura (actor, verb, object, result, context), não o vocabulário; o significado de um verbo está no seu IRI [F: adl2016xapidata, §2.4.3]. Um emissor que projeta eventos internos sem regras explícitas produz statements válidos mas não reconstruíveis: campos caem em `extensions` sem esquema, tempos são truncados e a versão do conteúdo some [I]. A pergunta do domínio é qual esquema interno torna a projeção mecânica e reversível.

## Fundamentos e funcionamento

### Correspondência de base

Serrano-Laguna et al., em trabalho com a ADL, mapeiam o evento de interação de jogos sérios assim: `userId → actor`, `action → verb`, `target → object`, `value → result` (opcional) e `timestamp → timestamp`; quando a semântica do valor não cabe em `score`, `success`, `completion`, `response` ou `duration`, usam `result.extensions` [F: serranolaguna2017applying, §5.1, Tabela 1]. Os verbos reutilizam o vocabulário da ADL quando existe (`initialized`, `progressed`, `completed`) e criam IRIs novos só quando necessário, como `https://w3id.org/xapi/seriousgames/verbs/unlocked` [F: serranolaguna2017applying, §5.2, Tabela 2]. O vocabulário ADL é ele próprio publicado como xAPI Profile, com versão `https://w3id.org/xapi/adl/v1.0` gerada em 2017-08-21 [F: adl2017adlvocab].

### Tabela de mapeamento proposta

Síntese deste documento sobre as fontes citadas em cada linha [I]:

| Campo interno | Destino xAPI | Regra que afeta a perda |
|---|---|---|
| `source` + `id` | `id` (UUID) | statement id deve ser UUID; recomendado que o emissor o gere [F: adl2016xapidata, §2.4.1]; derivar UUID determinístico de `source`+`id` permite deduplicar [I] |
| ator pseudônimo | `actor.account{homePage,name}` | um único IFI por Agent [F: adl2016xapidata, §2.4.2] |
| `type` (ação) | `verb.id` | o IRI define o significado; `display` não [F: adl2016xapidata, §2.4.3] |
| alvo | `object.id` + `definition.type` | — |
| resultado | `result.score/success/completion/response/duration` | `duration` pode ser truncada a 0,01 s [F: adl2016xapidata, §4.6] |
| latência, tentativa, valor bruto | `result.extensions` | chaves devem ser IRIs; o LRS não valida valores [F: adl2016xapidata, §4.1] |
| `time` (ocorrência) | `timestamp` | precisão garantida só até milissegundos [F: adl2016xapidata, §4.5] |
| tempo de observação | `context.extensions` | `stored` é sempre sobrescrito pelo LRS [F: adl2016xapidata, §2.4.8] |
| `session_id` | `context.registration` | registration pode ser tentativa, sessão ou abranger várias atividades [F: adl2016xapidata, §2.4.6.1] |
| atividade-mãe, turma | `context.contextActivities.parent/grouping` | — |
| versão do conteúdo | `context.revision` | só com Object do tipo Activity; para mudança maior, novo id de atividade [F: adl2016xapidata, §2.4.6] |
| cliente e dispositivo | `context.platform` + `context.extensions` | só com Object do tipo Activity [F: adl2016xapidata, §2.4.6] |
| versão de esquema, `config_hash`, fonte de relógio, `sequence` | `context.extensions` | sem semântica para o LRS |
| perfil seguido | `contextActivities.category` com id da versão do perfil | recomendado pela especificação de perfis [F: adl2017xapiprofiles, §5.0] |
| outros agentes (mediador, par) | `context.contextAgents` (só 2.0) | substitui `instructor`/`team`, agora "Not Recommended" [F: ieee2026xapibasedocs, LRS §4.2.2.5] |

### Onde a perda acontece

1. **Tempo sub-milissegundo**: o timestamp deve preservar ao menos milissegundos e pode ser truncado além disso [F: adl2016xapidata, §4.5]; na 2.0 o LRS "may truncate or round" a 3 casas [F: ieee2026xapibasedocs, LRS]. Carimbos em nanossegundos, como os do OTel [F: otel2026logsdatamodel, §Field: Timestamp], precisam de cópia integral em extensão.
2. **Fuso local**: na 2.0 o timestamp "shall be formatted to UTC" e o LRS converte em vez de rejeitar [F: ieee2026xapibasedocs, ChangeLog]; o deslocamento local original, relevante para análise de hora do dia, se perde se não for gravado à parte [I].
3. **Duração**: precisão além de 0,01 s pode ser truncada e é ignorada em comparações [F: adl2016xapidata, §4.6] [F: ieee2026xapibasedocs, LRS].
4. **Propriedades fora do lugar**: na 2.0 o LRS deve rejeitar statements com propriedades adicionais fora dos pontos de extensão [F: ieee2026xapibasedocs, ChangeLog]; campos internos não mapeados precisam ir para `extensions`, nunca para a raiz.
5. **Imutabilidade parcial**: definições de atividade e `display` de verbo não fazem parte do statement e podem mudar depois [F: adl2016xapidata, §2.3.1]; a interpretação durável deve estar no IRI e na `revision` [I].

### Regras do perfil

Um Statement Template fixa propriedades determinantes (verbo, tipo de atividade do objeto, tipos de atividade de contexto) e regras JSONPath com `presence` `included`, `excluded` ou `recommended`; o emissor que segue o template deve incluir todas as propriedades determinantes e cumprir todas as regras [F: adl2017xapiprofiles, §8.0, §8.1]. Extensões declaradas em perfil podem apontar um JSON Schema (`schema` ou `inlineSchema`, Draft-07) e devem ser usadas só no lugar previsto: `ContextExtension` em context, `ResultExtension` em result [F: adl2017xapiprofiles, §7.2]. Patterns descrevem sequências de statements (`sequence`, `alternates`, `optional`, `oneOrMore`, `zeroOrMore`) [F: adl2017xapiprofiles, §9.0]. É pelo perfil que a validação das extensões, ausente no LRS, é recuperada [I].

## Requisitos e pressupostos

- O esquema interno é um superconjunto do statement: tudo que o xAPI exige existe no evento, e o que o xAPI não tem tem destino declarado em extensão com IRI controlado [I].
- IRIs de extensão com controlador e descrição legível no próprio IRI, como a norma recomenda [F: adl2016xapidata, §4.1].
- O log interno continua sendo a fonte de verdade; o LRS é uma projeção (ver `dat.ev.event-sourcing`) [I].

## Vantagens e limitações

Vantagens [I]: interoperabilidade com LRS e ferramentas de análise; vocabulário reaproveitável entre estudos; validação por perfil.

Limitações: a própria norma adverte que "A Statement defined entirely by its extensions becomes meaningless as no other system can make sense of it" [F: adl2016xapidata, §4.1]; extensões demais anulam o ganho de padronização, como Serrano-Laguna et al. também observam [F: serranolaguna2017applying, §3.4]; perfis de jogos educativos não cobrem medidas motoras finas [I].

## Alternativas e comparações

| Estratégia | Perda | Custo |
|---|---|---|
| Emitir só xAPI no cliente | alta (tempo, campos sem destino) | baixo |
| Log interno + projeção xAPI com extensões | baixa, controlada pelo perfil | médio |
| Log interno + projeção + evento original como attachment assinado | nula para auditoria | alto |
| Caliper em vez de xAPI | ver `iop.lr.comparison` | — |

O xAPI 1.0.3 prevê statements assinados com JWS como attachment, para "strong and durable evidence of the authenticity and integrity" [F: adl2016xapidata, §2.6].

## Métricas e métodos de avaliação

Teste de ida e volta [I]: para uma amostra de eventos, projetar para xAPI, reconstruir e comparar campo a campo; registrar a taxa de diferenças por campo. Validar statements contra o perfil com um Profile Validator, que deve verificar todas as regras de template [F: adl2017xapiprofiles, §8.0].

## Exemplo técnico independente de domínio

```
evento: {source:"urn:p/D7", id:"e-193", type:"resposta.v3", time:"…T13:04:11.120734Z",
         sessao:"S1", ator:"p-8f2c", alvo:"item-17", valor:"B", correto:false,
         latencia_ms:1840, content_ver:"2.4.0", config_hash:"sha256:9f2c…", seq:193}
statement:
  id        = uuidv5(NS, "urn:p/D7|e-193")
  actor     = {account:{homePage:"https://exemplo.org", name:"p-8f2c"}}
  verb      = {id:"http://adlnet.gov/expapi/verbs/answered"}
  object    = {id:"https://exemplo.org/itens/17"}
  result    = {success:false, response:"B",
               extensions:{"https://exemplo.org/x/latencia-ms":1840}}
  context   = {registration:"<uuid de S1>", revision:"2.4.0",
               contextActivities:{category:[{id:"<IRI da versão do perfil>"}]},
               extensions:{"https://exemplo.org/x/evento":{source:"urn:p/D7", id:"e-193",
                 schema:"resposta/3.1.0", seq:193, time_ns:"…T13:04:11.120734Z",
                 config:"sha256:9f2c…"}}}
  timestamp = "…T13:04:11.120Z"
```

## Relações com outros conceitos

Depende de `dat.ev.event-model` e de `iop.fund.mapeamento-e-proveniencia`; é especificado por `iop.lr.xapi` e complementa `iop.lr.cmi5` quando a atividade é lançada por LMS. A projeção a partir do log segue `dat.ev.event-sourcing`; o modelo de interação vem de `dat.ev.game-telemetry`. A proveniência do statement pode ser expressa em `kg.std.prov-o`; o ator pseudônimo segue `psg.deid.anonymization-and-pseudonymization`.

## Lacunas e questões abertas

- O texto pago da IEEE 9274.1.1-2023 não foi lido; usou-se o texto base aberto do grupo de trabalho no repositório do IEEE, que pode diferir da edição publicada.
- Não foi verificado se existe perfil xAPI publicado para medidas motoras ou de tempo de reação em atividades lúdicas.
- A especificação de perfis declara relevância para xAPI 1.0.x; sua aplicação a statements 2.0 (por exemplo, regras sobre `contextAgents`) não foi verificada.
- O registro xapi.vocab.pub não respondeu nesta sessão; o vocabulário ADL foi lido no repositório de perfis.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| adl2016xapidata | normativo | 2026-10-30 |
| ieee2026xapibasedocs | normativo | 2026-10-30 |
| ieee2023xapi | normativo [metadados] | 2026-10-30 |
| adl2017xapiprofiles | normativo | 2026-10-30 |
| adl2017adlvocab | normativo | 2026-10-30 |
| serranolaguna2017applying | academico (versão preprint) | 2026-10-30 |
| otel2026logsdatamodel | normativo | 2026-10-30 |
