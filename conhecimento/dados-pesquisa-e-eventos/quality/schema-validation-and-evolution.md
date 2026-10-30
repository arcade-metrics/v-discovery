---
id: dat.qual.schema-validation-and-evolution
titulo: Validação de esquema e evolução compatível de eventos
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [jsonschema2022core, jsonschema2022validation, apache2026avrospec, google2026protobufproto3, confluent2026schemaevolution, cncf2026cloudevents]
relacoes:
  - { tipo: parte-de, alvo: dat.ev.event-model }
  - { tipo: complementa, alvo: dat.rd.data-documentation }
  - { tipo: complementa, alvo: dat.rd.repositories-and-versioning }
  - { tipo: complementa, alvo: dat.ev.event-to-xapi-mapping }
  - { tipo: relacionado-a, alvo: dat.ev.event-sourcing }
  - { tipo: relacionado-a, alvo: dat.qual.granularity-and-constructs }
  - { tipo: relacionado-a, alvo: lae.dq.provenance-and-lineage }
termos: [esquema de evento, validação de esquema, dialeto, asserção, anotação, esquema do escritor, esquema do leitor, resolução de esquema, compatibilidade retroativa, compatibilidade progressiva, compatibilidade total, compatibilidade transitiva, registro de esquemas, número de campo reservado, modelo de conteúdo aberto, modelo de conteúdo fechado]
---

# Validação de esquema e evolução compatível de eventos

## Definição e terminologia

Um **esquema de evento** descreve tipos, campos e restrições de uma classe de eventos. **Validar** é verificar, na entrada, se um evento satisfaz o esquema declarado; **evoluir** é mudar o esquema sem tornar ilegíveis os eventos já gravados nem quebrar quem os produz ou consome. Num dataset de pesquisa, eventos de meses ou anos convivem no mesmo repositório, então todo evento precisa dizer com qual versão foi escrito [I].

Vocabulário de compatibilidade, como a documentação do Confluent Schema Registry o define [F: confluent2026schemaevolution]: **BACKWARD** significa que "consumers using the new schema can read data produced with the last schema" (atualizam-se primeiro os consumidores); **FORWARD**, que "data produced with a new schema can be read by consumers using the last schema" (atualizam-se primeiro os produtores); **FULL**, que as duas valem; as variantes **_TRANSITIVE** comparam com todas as versões anteriores e não só com a última; **NONE** desliga a verificação. O padrão do registro é BACKWARD, "not BACKWARD_TRANSITIVE" [F: confluent2026schemaevolution].

## Problema que resolve

Sem validação na entrada, um erro de instrumentação (campo renomeado, unidade trocada de ms para s) contamina o dataset e só aparece na análise, quando a coleta já acabou [I]. Sem regras de evolução, uma mudança legítima (novo campo de covariável de dispositivo, por exemplo) torna eventos antigos ilegíveis, ou é feita reutilizando um nome ou número de campo com outro significado, o que é pior: a Protocol Buffers adverte que reutilizar número de campo torna a decodificação ambígua e pode causar vazamento de dados pessoais e "Data corruption" [F: google2026protobufproto3]. Para pesquisa, o esquema também é documentação: é ele que diz o que cada campo significava na data da coleta (ver `dat.rd.data-documentation`) [I].

## Fundamentos e funcionamento

### JSON Schema 2020-12

O núcleo do JSON Schema 2020-12 (draft-bhutton-json-schema-01, junho de 2022, Internet-Draft informativo) usa `$schema` como identificador do dialeto e de seu meta-esquema e `$id` para dar a cada recurso de esquema um URI canônico [F: jsonschema2022core, §8.1.1, §8.2.1]. A especificação distingue **asserções**, que fazem o documento passar ou falhar, de **anotações**, informação coletada que a implementação não é obrigada a usar [F: jsonschema2022core, §7.6, §7.7]. Na especificação de validação, `format` é por padrão só anotação: tratá-lo como asserção é opcional e, quando a implementação o faz, deve vir desligado por padrão, salvo se o vocabulário Format-Assertion for declarado [F: jsonschema2022validation, §7.1, §7.2]. Consequência prática: um campo `"format": "date-time"` não rejeita carimbos malformados a menos que isso seja configurado [I]. A palavra-chave `deprecated` marca campos que aplicações "SHOULD refrain from usage" e que podem ser removidos no futuro [F: jsonschema2022validation, §9.3].

Para JSON Schema, a compatibilidade depende do **modelo de conteúdo**. O Confluent distingue política leniente, que aceita mudanças "regardless of the content model", de política estrita, em que modelos abertos (`additionalProperties: true`) permitem mais mudanças que modelos fechados (`additionalProperties: false`) [F: confluent2026schemaevolution].

### Apache Avro: esquema do escritor e do leitor

A especificação Avro 1.12.0 parte de que o esquema usado para escrever acompanha os dados, de modo que o leitor sempre consegue interpretá-los, e de que o leitor pode projetá-los num esquema diferente; a **resolução de esquema** casa os dois [F: apache2026avrospec, Schema Resolution]. Regras para registros: campos são casados por nome, em qualquer ordem; campo do escritor ausente no leitor é ignorado; campo do leitor ausente no escritor usa o valor default do leitor, e sem default "an error is signalled" [F: apache2026avrospec, Schema Resolution]. Há promoções de tipo permitidas (`int` para `long`, `float` ou `double`; `long` para `float` ou `double`; `float` para `double`; `string` e `bytes` entre si); um símbolo de enum desconhecido usa o default do enum do leitor, se houver; aliases reescrevem o esquema do escritor com nomes do leitor [F: apache2026avrospec, Schema Resolution].

### Protocol Buffers: números de campo

A regra central da Protocol Buffers (proto3) é que a identidade de um campo é seu número. Mudar o número de um campo existente "is not safe"; acrescentar campos é seguro; ao remover, o número "must not used again", e deve ir para a lista `reserved`, junto com o nome, para que as codificações JSON e TextFormat continuem a funcionar; o compilador rejeita números reservados [F: google2026protobufproto3, Updating A Message Type; Deleting Fields; Reserved Field Numbers]. Mensagens proto3 preservam campos desconhecidos na leitura e na reescrita, e `int32`, `uint32`, `int64`, `uint64` e `bool` são compatíveis entre si no fio [F: google2026protobufproto3].

### Esquema no envelope do evento

A CloudEvents oferece o atributo opcional `dataschema`, que identifica o esquema seguido por `data`, e determina que "Incompatible changes to the schema SHOULD be reflected by a different URI" [F: cncf2026cloudevents]. Junto com `type`, isso dá ao evento uma referência à definição exata usada na escrita [I]. Para Avro, o registro de esquemas cumpre papel semelhante, guardando versões numeradas e verificando o tipo de compatibilidade configurado antes de aceitar uma nova versão [F: confluent2026schemaevolution].

## Requisitos e pressupostos

- Cada evento leva tipo e versão de esquema (ou URI de `dataschema`), resolvíveis para sempre; esquemas ficam versionados junto do dataset, como em `dat.rd.repositories-and-versioning` [I].
- Escolha explícita do tipo de compatibilidade; para dados de pesquisa que serão relidos anos depois, a variante transitiva é a que garante leitura de todas as versões antigas [F: confluent2026schemaevolution; I].
- Campos novos com default (Avro) ou opcionais; nada de reutilizar nome ou número [F: apache2026avrospec; google2026protobufproto3].
- Eventos inválidos não são descartados em silêncio: vão para uma área de quarentena com o motivo, para que a perda por validação entre na conta de `dat.qual.loss-and-deduplication` [I].

## Vantagens e limitações

Validar na entrada desloca erros para perto de quem os causa e torna o significado de cada campo verificável [I]. Limitações: JSON Schema valida estrutura, não semântica (um RT em segundos passa num campo numérico); as palavras-chave de formato não são verificadas por padrão [F: jsonschema2022validation, §7.2]; e a mudança de significado sem mudança de forma (mesmo campo, nova definição operacional) não é detectada por nenhuma regra de compatibilidade, só por versionamento disciplinado e documentação [I].

## Alternativas e comparações

| Critério | JSON Schema 2020-12 | Avro 1.12.0 | Protocol Buffers (proto3) |
|---|---|---|---|
| Identidade do campo | nome | nome, com aliases [F: apache2026avrospec] | número [F: google2026protobufproto3] |
| Leitura de versão antiga | depende do modelo de conteúdo [F: confluent2026schemaevolution] | resolução escritor/leitor com defaults [F: apache2026avrospec] | campos desconhecidos preservados [F: google2026protobufproto3] |
| Remoção de campo | `deprecated` como anotação [F: jsonschema2022validation, §9.3] | seguro se o leitor tiver default ou ignorar [F: apache2026avrospec] | reservar número e nome [F: google2026protobufproto3] |
| Legível sem ferramenta | sim (JSON) | não, binário com esquema [I] | não, binário [I] |
| Situação do texto | Internet-Draft de 2022 [F: jsonschema2022core] | especificação do projeto | guia oficial do projeto |

Para dados destinados a arquivamento e reuso amplo, a legibilidade do JSON pesa a favor; para volume alto de amostras de trajetória, os formatos binários reduzem tamanho [H].

## Métricas e métodos de avaliação

Taxa de eventos rejeitados por versão de esquema e por produtor; número de versões ativas simultâneas; teste automático de compatibilidade a cada mudança (o registro de esquemas faz isso no tipo configurado) [F: confluent2026schemaevolution]; teste de releitura de uma amostra de eventos antigos com o esquema atual antes de cada publicação de dataset [I].

## Exemplo técnico independente de domínio

```
evento (envelope):
  type: org.exemplo.tentativa.respondida
  dataschema: https://exemplo.org/esquemas/tentativa/3        # versao incompativel => novo URI
  data: {estimulo_t: 18233.4, resposta_t: 18871.9, ponto_final: [412.5, 188.0], dpr: 2.625}

esquema v3 (JSON Schema 2020-12, modelo fechado):
  $schema: https://json-schema.org/draft/2020-12/schema
  $id: https://exemplo.org/esquemas/tentativa/3
  type: object
  required: [estimulo_t, resposta_t]
  properties:
    estimulo_t: {type: number, description: "ms desde timeOrigin, quadro rAF"}
    resposta_t: {type: number, description: "ms desde timeOrigin, Event.timeStamp"}
    ponto_final: {type: array, items: {type: number}, minItems: 2, maxItems: 2}
    dpr: {type: number}                       # novo na v3, opcional => leitores v2 abertos nao quebram
    rt_ms: {type: number, deprecated: true}   # derivado; mantido so para leitura de dados antigos
  additionalProperties: false
```

## Relações com outros conceitos

É parte do envelope definido em `dat.ev.event-model` e determina a fidelidade do mapeamento em `dat.ev.event-to-xapi-mapping`. Complementa `dat.rd.data-documentation` (o esquema é parte do dicionário de dados) e `dat.rd.repositories-and-versioning` (esquemas versionados com o dataset). Em `dat.ev.event-sourcing`, a releitura de eventos antigos depende das regras de evolução. Os campos exigidos por `dat.qual.granularity-and-constructs` entram aqui como contrato; a versão de esquema por evento é metadado de linhagem em `lae.dq.provenance-and-lineage`.

## Lacunas e questões abertas

- A versão 2020-12 do JSON Schema circula como Internet-Draft expirado; não foi verificado se há publicação mais recente adotada como referência estável.
- As tabelas de regras por formato do Confluent foram lidas de forma parcial; a correspondência exata entre tipo de compatibilidade e campos obrigatórios em Avro e Protobuf ficou por conferir.
- Não foi encontrada fonte que trate de mudança de definição operacional sem mudança de forma em dados comportamentais; a recomendação de versionar por significado é deste documento.
- Faltam comparações medidas de tamanho e custo de validação entre os três formatos para fluxos de amostras de ponteiro.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| jsonschema2022core | normativo (Internet-Draft) | 2026-10-30 |
| jsonschema2022validation | normativo (Internet-Draft) | 2026-10-30 |
| apache2026avrospec | fornecedor | 2026-10-30 |
| google2026protobufproto3 | fornecedor | 2026-10-30 |
| confluent2026schemaevolution | fornecedor | 2026-10-30 |
| cncf2026cloudevents | normativo | 2026-10-30 |
