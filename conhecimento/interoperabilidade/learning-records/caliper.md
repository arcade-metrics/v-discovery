---
id: iop.lr.caliper
titulo: Caliper Analytics
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2020caliper, adl2016discovery]
relacoes:
  - { tipo: alternativa-a, alvo: iop.lr.xapi }
  - { tipo: complementa, alvo: iop.tool.lti-core }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: relacionado-a, alvo: iop.lr.comparison }
termos: [Sensor, Envelope, Event, Entity, perfil (profile), JSON-LD, eventTime, use metrics]
---

# Caliper Analytics

## Definição e terminologia

Caliper Analytics é a especificação de eventos de aprendizagem do 1EdTech (ex-IMS Global): define um modelo de dados de eventos e entidades, uma serialização JSON-LD e uma Sensor API para emissão.

Versão consultada: **Caliper Analytics Specification, 1EdTech Final Release, Version 1.2, emitida em 27 de março de 2020**, disponibilizada para adoção pela comunidade [F: imsglobal2020caliper].

Termos [F: imsglobal2020caliper, §1.2, §2, §5]:

- **Event**: descreve `actor`, `action` e `object` ligados a um instante. Cada Event tem um UUID.
- **Entity**: tipo genérico para pessoas, grupos, recursos e demais participantes; entidades formam um grafo dirigido.
- **Envelope**: contêiner de transporte de Events e Entities, com metadados do Sensor emissor.
- **Sensor**: software, dentro da aplicação de aprendizagem, que implementa a Sensor API e envia os dados.
- **Profile**: vocabulário tipado de eventos para uma área de atividade.

## Problema que resolve

Padronizar a telemetria de aprendizagem em um vocabulário fechado por área de atividade, de modo que o consumidor saiba de antemão quais eventos e quais propriedades esperar — o oposto da abordagem aberta do xAPI [I].

## Fundamentos e funcionamento

**Propriedades de Event.** `id`, `type`, `actor`, `action`, `object` e `eventTime`. O `id` deve ser um UUID expresso como URN, na forma `urn:uuid:<UUID>`. `eventTime` usa ISO 8601 com precisão de milissegundos, em UTC. A propriedade `profile` é opcional por compatibilidade retroativa, mas Sensors SHOULD informá-la [F: imsglobal2020caliper, §2.1].

**Perfis (§3).** Annotation, Assessment, Assignable, Feedback, Forum, Grading, Media, Reading, Resource Management, Search, Session, Survey, Tool Launch, Tool Use e General [F: imsglobal2020caliper, §3].

**Serialização (§4).** JSON-LD, com contexto em `http://purl.imsglobal.org/ctx/caliper/v1p2`; a seção cobre contexto JSON-LD, identificadores, tipos e coerção de tipo, e entidades anônimas [F: imsglobal2020caliper, §4].

**Transporte (§5, §6).** A Sensor API define comportamento, envelope, payload JSON-LD e requisições HTTP; o lado do Endpoint cobre respostas HTTP, informação de configuração e limites de tamanho de string e armazenamento [F: imsglobal2020caliper, §5, §6].

**Use metrics.** O Apêndice J lista métricas de uso: AssessmentsPassed, AssessmentsSubmitted, MinutesOnTask, SkillsMastered, StandardsMastered, UnitsCompleted, UnitsPassed e WordsRead [F: imsglobal2020caliper, Apêndice J].

**Conformidade.** Tudo fora das seções não normativas é normativo; as palavras-chave seguem a RFC 2119; falhar um MUST torna a implementação não conforme. O guia de conformidade e certificação define requisitos para Sensors e pode ser mais estrito que a especificação [F: imsglobal2020caliper, §1.3, §1.4.1].

## Requisitos e pressupostos

- A aplicação emissora consegue implementar um Sensor e enviar envelopes por HTTP ao endpoint.
- O caso de uso cabe em um dos perfis existentes; fora deles, o perfil General é o recurso disponível [I].
- O consumidor processa JSON-LD, ou ao menos JSON com `@context` fixo [I].

## Vantagens e limitações

Vantagens [I]: vocabulário tipado por perfil reduz a divergência semântica entre fornecedores; JSON-LD dá caminho natural para grafos; o envelope com metadados do Sensor preserva proveniência; `urn:uuid` por evento dá idempotência e deduplicação.

Limitações [I]:
- Cobertura limitada aos perfis previstos; atividades atípicas (jogo, atividade motora, uso offline) não têm perfil próprio.
- Menos extensível que xAPI por construção — essa rigidez é o mecanismo pelo qual ganha comparabilidade.
- A versão consultada é de 2020; não foi verificado se há versão posterior.

## Alternativas e comparações

Ver `iop.lr.comparison`. Em 2016, uma revisão conjunta ADL/IMS registrou que as especificações vêm de origens diferentes e não são equivalentes, que xAPI foi construído para rastrear qualquer experiência (inclusive desempenho físico) e não só cursos web, que Caliper é a implementação do Learning Analytics Framework do IMS, e que a adoção "should not be one-or-the-other" [F: adl2016discovery].

## Métricas e métodos de avaliação

Conformidade: guia de conformidade e certificação do 1EdTech para Sensors [F: imsglobal2020caliper, §1.4.1]. Qualidade de dados: proporção de eventos com `profile` declarado; proporção de eventos fora dos perfis previstos [I].

## Exemplo técnico independente de domínio

```json
{
  "sensor": "https://app.exemplo/sensor",
  "sendTime": "2026-10-29T13:05:00.000Z",
  "dataVersion": "http://purl.imsglobal.org/ctx/caliper/v1p2",
  "data": [{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id": "urn:uuid:4f1b2c3d-0000-4000-8000-000000000001",
    "type": "AssessmentItemEvent",
    "profile": "AssessmentProfile",
    "actor":  { "id": "https://sis.exemplo/users/8f2c1e", "type": "Person" },
    "action": "Completed",
    "object": { "id": "https://app.exemplo/items/17", "type": "AssessmentItem" },
    "eventTime": "2026-10-29T13:04:11.120Z"
  }]
}
```

Exemplo ilustrativo, montado a partir da estrutura descrita na especificação; não é um exemplo copiado dela [I].

## Relações com outros conceitos

Alternativa a `iop.lr.xapi`. Complementa `iop.tool.lti-core`, já que os perfis Tool Launch e Tool Use descrevem exatamente a atividade mediada por LTI [F: imsglobal2020caliper, §3]. Depende do tratamento de vocabulários em `iop.sem.vocabularios-e-skos`.

## Lacunas e questões abertas

- Existe Caliper 1.3 ou posterior? Não verificado.
- O corpo das seções §4 a §6 e dos perfis §3.13–§3.15 não foi lido integralmente (a página excede o limite de leitura); detalhes de HTTP e de cada perfil permanecem não verificados.
- Mapeamento normativo Caliper↔xAPI: ver ISO/IEC TS 20748-3 em `iop.fund.mapeamento-e-proveniencia`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2020caliper | normativo | 2026-10-29 |
| adl2016discovery | secundario | 2026-10-29 |
