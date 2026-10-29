---
id: iop.lr.xapi
titulo: xAPI (Experience API, IEEE 9274.1.1)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2023xapi, adl2016xapiabout, adl2016xapidata, adl2021xapi20]
relacoes:
  - { tipo: alternativa-a, alvo: iop.lr.caliper }
  - { tipo: alternativa-a, alvo: iop.tool.scorm }
  - { tipo: complementa, alvo: iop.lr.cmi5 }
  - { tipo: depende-de, alvo: iop.fund.identidade-e-contexto }
  - { tipo: relacionado-a, alvo: iop.lr.comparison }
termos: [statement, LRS, actor, verb, object, IFI, registration, voiding, substatement]
---

# xAPI (Experience API)

## Definição e terminologia

xAPI é um modelo de dados em JSON e uma API REST para registrar e recuperar experiências de aprendizagem em um *Learning Record Store* (LRS). Nomes alternativos: Experience API, Tin Can API (nome do projeto original, em desuso).

A versão normalizada é a IEEE 9274.1.1-2023, "IEEE Standard for Learning Technology — JavaScript Object Notation (JSON) Data Model Format and Representational State Transfer (RESTful) Web Service for Learner Experience Data Tracking and Access", aprovada pelo board em 2023-03-30 e publicada em 2023-10-06, com status de *Active Standard*; o escopo declara ser uma versão melhorada e padronizada da especificação xAPI 1.0.3, para rastreio e acesso a dados de experiência [F: ieee2023xapi]. A mesma página registra a existência da norma internacional ISO/IEC/IEEE 39274-1-1-2025 sobre o mesmo assunto [F: ieee2023xapi].

A versão pública anterior é a 1.0.3, de 21 de setembro de 2016, dividida em três partes: Part One (About), Part Two (Data) e Part Three (Data Processing, Validation, and Security) [F: adl2016xapiabout].

O que xAPI **não** é: não é um formato de empacotamento de conteúdo (isso é SCORM/Common Cartridge), não é um vocabulário fechado de verbos, e não é um sistema de relatórios [I].

## Problema que resolve

Registrar que alguém fez alguma coisa, em qualquer lugar — dentro ou fora de um LMS, online ou offline, em simulador, jogo ou atividade física — num formato comum, com um repositório consultável [F: adl2016xapiabout] [I].

## Fundamentos e funcionamento

**Statement.** A estrutura central é a sentença "I did this": Actor (o "I"), Verb (o "did") e Object (o "this") [F: adl2016xapiabout]. Propriedades obrigatórias: `actor`, `verb`, `object`. Recomendada: `id` (UUID), que o LRS atribui se ausente. Opcionais: `result`, `context`, `timestamp` (o LRS usa o tempo de armazenamento se ausente) e `attachments`. O LRS define `stored` e define `authority` quando não fornecida ou quando não há relação de confiança forte. A propriedade `version` deve valer `1.0.0` quando definida por um Learning Record Provider, o que a norma desencoraja [F: adl2016xapidata].

**Actor.** Agent identificado por exatamente um IFI: `mbox` (IRI mailto), `mbox_sha1sum` (SHA1 hex do IRI mailto), `openid` (URI) ou `account` (`homePage` + `name`). Group pode ser anônimo (sem IFI, com `member`, e cada grupo anônimo é distinto) ou identificado (um IFI, `member` opcional) [F: adl2016xapidata].

**Verb.** `id` é um IRI obrigatório e é ele que define o significado; `display` é um language map recomendado, apenas para exibição, e não deve ser usado para inferir significado [F: adl2016xapidata].

**Object.** Por padrão é uma Activity (`id` obrigatório; `definition` opcional com `name`, `description`, `type`, `moreInfo`, propriedades de interação e `extensions`). Pode ser Agent/Group (com `objectType` explícito), StatementRef (referência a UUID de outro statement, usada para comentários e *voiding*) ou SubStatement (validado como statement, mas sem `id`, `stored`, `version` e `authority`, e sem aninhamento) [F: adl2016xapidata].

**Result.** `score` (`scaled` entre -1 e 1, recomendado; `raw`, `min`, `max`), `success`, `completion`, `response`, `duration` (ISO 8601) e `extensions` [F: adl2016xapidata].

**Context.** `registration` (UUID), `instructor`, `team`, `contextActivities` com os buckets `parent`, `grouping`, `category` e `other` (o LRS devolve como arrays), `revision` e `platform` (válidos só quando o Object é Activity), `language` (RFC 5646), `statement` e `extensions` [F: adl2016xapidata].

**Imutabilidade.** Statements são tidos como permanentes; a única forma suportada de desfazer é o *voiding* [F: adl2016xapidata].

**Mudanças na 2.0.** Segundo comunicação da ADL, a atualização acrescenta `contextAgents` e `contextGroups`, permitindo estabelecer contexto diretamente com indivíduos e equipes, padroniza timestamps em fuso universal, proíbe propriedades extras e permite que o LRS rejeite statements por intenção maliciosa ou má construção; a governança passou ao IEEE LTSC [F: adl2021xapi20]. Esta é fonte secundária do próprio mantenedor; o texto normativo da IEEE 9274.1.1-2023 é pago e não foi consultado [I].

## Requisitos e pressupostos

- Existe um LRS acessível por HTTPS com autenticação.
- Há uma decisão explícita sobre o vocabulário de verbos e os IRIs de atividade. A norma não a toma por você; sem perfil acordado, dois emissores produzem dados não agregáveis [I].
- A política de identificação do Actor foi decidida antes do primeiro statement (ver `iop.fund.identidade-e-contexto`).

## Vantagens e limitações

Vantagens [I]: cobre experiências fora do LMS; extensível por `extensions` em quase todo ponto do modelo; `SubStatement` e `StatementRef` permitem falar sobre statements; `registration` e `contextActivities` dão agregação sem acoplar à estrutura de um LMS.

Limitações:
- O significado está no IRI do verbo, e a norma não fixa lista [F: adl2016xapidata]; a interoperabilidade semântica fica delegada a perfis [I].
- Imutabilidade por design conflita com pedidos de eliminação (ver `iop.fund.privacidade-e-seguranca`) [I].
- Liberdade de modelagem produz dados heterogêneos entre fornecedores [I].
- A norma vigente é paga, o que dificulta verificação pública de detalhes da 2.0 [I].

## Alternativas e comparações

Ver `iop.lr.comparison` para a comparação com Caliper. Para conteúdo lançado por LMS com regras de sessão, o perfil cmi5 (`iop.lr.cmi5`) cobre o que o xAPI puro deixa em aberto.

## Métricas e métodos de avaliação

Conformidade de LRS historicamente se verifica com suíte de testes da ADL; não verificado o estado atual dessa suíte sob a governança IEEE [H]. Métricas úteis de qualidade de dados: proporção de statements com `registration`, número de IRIs de verbo distintos por ação semanticamente equivalente, densidade de `extensions` [I].

## Exemplo técnico independente de domínio

```json
{
  "actor":  { "objectType": "Agent",
              "account": { "homePage": "https://sis.exemplo", "name": "8f2c1e" } },
  "verb":   { "id": "http://exemplo/verbs/respondeu",
              "display": { "pt-BR": "respondeu" } },
  "object": { "id": "http://exemplo/atividades/item-17",
              "definition": { "type": "http://adlnet.gov/expapi/activities/cmi.interaction" } },
  "result": { "success": true, "duration": "PT12.4S",
              "score": { "scaled": 1.0 } },
  "context": { "registration": "0b1b...-uuid",
               "contextActivities": { "grouping": [ { "id": "http://exemplo/turmas/5A" } ] } },
  "timestamp": "2026-10-29T13:04:11.120Z"
}
```

## Relações com outros conceitos

Alternativa a `iop.lr.caliper` para registro de eventos e a `iop.tool.scorm` para rastreio de conteúdo. Complementado por `iop.lr.cmi5`, que acrescenta regras de lançamento e sessão.

## Lacunas e questões abertas

- Texto normativo da IEEE 9274.1.1-2023 não lido; diferenças exatas em relação a 1.0.3 permanecem com fonte secundária.
- Especificação de Profiles do ADL não consultada; é a peça que resolve a lacuna de vocabulário.
- Situação do LRS Test Suite sob governança IEEE: não verificada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ieee2023xapi | normativo | 2026-10-29 |
| adl2016xapiabout | normativo | 2026-10-29 |
| adl2016xapidata | normativo | 2026-10-29 |
| adl2021xapi20 | secundario | 2026-10-29 |
