---
id: iop.exemplos
titulo: Exemplos de mensagens e payloads
tipo: comparacao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [adl2016xapidata, imsglobal2020caliper, aicc2016cmi5, imsglobal2019lti13, imsglobal2019ltiags, imsglobal2019ltinrps, imsglobal2022oneroster, w3c2025vcdm, w3c2009skos, schemaorg2026learningresource, scorm2026technical]
relacoes:
  - { tipo: complementa, alvo: iop.matriz }
  - { tipo: relacionado-a, alvo: iop.lr.comparison }
termos: [payload, statement, envelope, claim, credencial]
---

# Exemplos de mensagens e payloads

Estruturas ilustrativas, montadas a partir dos campos descritos nas especificações citadas. **Não são exemplos copiados das especificações** e não substituem a leitura delas; servem para comparar a forma de cada padrão lado a lado [I]. Todos os identificadores são fictícios.

## 1. Mesmo fato, quatro padrões

O fato: a aluna identificada por `8f2c1e` respondeu corretamente ao item 17, em 12,4 segundos, na turma 5A.

### xAPI

Campos conforme o modelo de Statement [F: adl2016xapidata].

```json
{
  "actor":  { "objectType": "Agent",
              "account": { "homePage": "https://sis.exemplo", "name": "8f2c1e" } },
  "verb":   { "id": "https://exemplo/verbs/answered", "display": { "pt-BR": "respondeu" } },
  "object": { "id": "https://exemplo/items/17",
              "definition": { "type": "http://adlnet.gov/expapi/activities/cmi.interaction" } },
  "result": { "success": true, "duration": "PT12.4S", "score": { "scaled": 1.0 } },
  "context": { "registration": "3f0c9a71-0000-4000-8000-000000000001",
               "contextActivities": { "grouping": [ { "id": "https://exemplo/turmas/5A" } ] } },
  "timestamp": "2026-10-29T13:04:11.120Z"
}
```

### Caliper

Envelope com metadados do Sensor e evento com `id` em `urn:uuid` e `eventTime` em UTC com milissegundos [F: imsglobal2020caliper, §2.1, §4, §5].

```json
{
  "sensor": "https://app.exemplo/sensor",
  "sendTime": "2026-10-29T13:05:00.000Z",
  "dataVersion": "http://purl.imsglobal.org/ctx/caliper/v1p2",
  "data": [{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id": "urn:uuid:4f1b2c3d-0000-4000-8000-000000000002",
    "type": "AssessmentItemEvent",
    "profile": "AssessmentProfile",
    "actor":  { "id": "https://sis.exemplo/users/8f2c1e", "type": "Person" },
    "action": "Completed",
    "object": { "id": "https://exemplo/items/17", "type": "AssessmentItem" },
    "eventTime": "2026-10-29T13:04:11.120Z"
  }]
}
```

### cmi5

O mesmo evento ocorreria entre `initialized` e `terminated` e seria *cmi5 allowed*: template de contexto cmi5, verbo livre, sem o id de categoria cmi5 [F: aicc2016cmi5].

```
launched    (LMS)
initialized (AU)
  ... statements cmi5 allowed, inclusive o exemplo xAPI acima ...
passed      (AU, scaled >= masteryScore)
completed   (AU)
terminated  (AU)
```

### SCORM

Não há mensagem: o conteúdo chama a API JavaScript do LMS e grava elementos do modelo `cmi.*`, como status de conclusão, nota e tempo [F: scorm2026technical]. O registro vive no LMS, não em um repositório consultável.

## 2. Lançamento LTI 1.3

Claims obrigatórios de um Resource Link Launch [F: imsglobal2019lti13, §5.3]. O conteúdo é o payload do `id_token`, antes de virar JWT.

```json
{
  "https://purl.imsglobal.org/spec/lti/claim/message_type": "LtiResourceLinkRequest",
  "https://purl.imsglobal.org/spec/lti/claim/version": "1.3.0",
  "https://purl.imsglobal.org/spec/lti/claim/deployment_id": "D-42",
  "https://purl.imsglobal.org/spec/lti/claim/target_link_uri": "https://ferramenta.exemplo/launch",
  "https://purl.imsglobal.org/spec/lti/claim/resource_link": { "id": "rl-9913" },
  "sub": "8f2c1e",
  "https://purl.imsglobal.org/spec/lti/claim/roles": [
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner"
  ],
  "https://purl.imsglobal.org/spec/lti/claim/context": { "id": "turma-5A" }
}
```

## 3. Publicação de nota (LTI AGS)

Campos de Score visíveis na especificação [F: imsglobal2019ltiags]; media type `application/vnd.ims.lis.v1.score+json`.

```json
{
  "userId": "8f2c1e",
  "scoreGiven": 9.0,
  "scoreMaximum": 10.0,
  "activityProgress": "Completed",
  "gradingProgress": "FullyGraded",
  "timestamp": "2026-10-29T13:10:00.000Z"
}
```

## 4. Lista de participantes (LTI NRPS)

Estrutura do container de memberships [F: imsglobal2019ltinrps]; media type `application/vnd.ims.lti-nrps.v2.membershipcontainer+json`.

```json
{
  "id": "https://lms.exemplo/sections/2923/memberships",
  "context": { "id": "turma-5A", "title": "5º ano A" },
  "members": [
    { "user_id": "8f2c1e",
      "roles": [ "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner" ],
      "status": "Active" }
  ]
}
```

## 5. Rostering em lote (OneRoster CSV)

O binding CSV [F: imsglobal2022oneroster] é um conjunto de arquivos; a chave entre eles é o `sourcedId`.

```
# enrollments.csv
sourcedId,status,dateLastModified,classSourcedId,schoolSourcedId,userSourcedId,role,primary
enr-001,active,2026-10-29,cls-5A,sch-07,usr-8f2c1e,student,

# users.csv
sourcedId,status,dateLastModified,enabledUser,givenName,familyName,role,identifier
usr-8f2c1e,active,2026-10-29,true,,,student,8f2c1e
```

Nomes de coluna ilustrativos: o binding CSV não foi lido nesta rodada [I].

## 6. Credencial verificável

Estrutura mínima conforme o VCDM 2.0: `@context` cujo primeiro item é `https://www.w3.org/ns/credentials/v2`, emissor, sujeito e prova [F: w3c2025vcdm].

```json
{
  "@context": [ "https://www.w3.org/ns/credentials/v2",
                "https://purl.imsglobal.org/spec/ob/v3p0/context.json" ],
  "type": [ "VerifiableCredential", "OpenBadgeCredential" ],
  "issuer": "https://escola.exemplo/issuers/1",
  "credentialSubject": {
    "id": "did:exemplo:8f2c1e",
    "achievement": { "id": "https://escola.exemplo/achievements/leitura-fluente" }
  },
  "proof": { "type": "DataIntegrityProof" }
}
```

A URL de contexto do Open Badges é ilustrativa; não foi verificada [I].

## 7. Vocabulário e mapeamento (SKOS)

Correspondência entre dois vocabulários, declarada como dado [F: w3c2009skos].

```turtle
<https://exemplo/verbs/answered>
  a skos:Concept ;
  skos:prefLabel "respondeu"@pt-BR ;
  skos:exactMatch <https://outro.exemplo/verbs/responded> ;
  skos:closeMatch <https://terceiro.exemplo/actions/Submitted> .
```

## 8. Metadado de recurso

Propriedades do tipo LearningResource [F: schemaorg2026learningresource], com a competência expressa por identificador, não por texto.

```json
{
  "@context": "https://schema.org",
  "@type": ["VideoObject", "LearningResource"],
  "name": "Frações equivalentes",
  "learningResourceType": "video",
  "teaches": { "@type": "DefinedTerm",
               "termCode": "EF05MA03",
               "inDefinedTermSet": "https://exemplo/curriculo" }
}
```

## Lacunas

- Nenhum dos exemplos foi validado contra o esquema oficial do padrão correspondente. Validar antes de usar como referência de implementação.
- Faltam exemplos de QTI, Common Cartridge, CASE e FHIR, cujos modelos não foram lidos em detalhe nesta rodada.
