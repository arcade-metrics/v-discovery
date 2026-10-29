---
id: iop.fund.dados-vs-protocolo
titulo: Padrões de dados, de protocolo e de empacotamento
tipo: conceito
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2023xapi, imsglobal2020caliper, imsglobal2019lti13, imsglobal2022oneroster, dcmi2020terms, imsglobal2017case, imsglobal2011cc, adl2016xapidata, imsglobal2019ltiags, imsglobal2022qti30]
relacoes:
  - { tipo: complementa, alvo: iop.fund.niveis-de-interoperabilidade }
  - { tipo: relacionado-a, alvo: iop.catalogo }
termos: [modelo de dados, binding, protocolo, empacotamento, vocabulário controlado, perfil de aplicação]
---

# Padrões de dados, de protocolo e de empacotamento

## Definição e terminologia

Padrões educacionais costumam ser citados em lista única, como se fossem comparáveis entre si. Não são. Um padrão pode especificar [I]:

- **Modelo de dados**: quais entidades existem, que atributos têm, como se relacionam. Exemplo: o modelo de Statement do xAPI [F: adl2016xapidata].
- **Vocabulário controlado**: que valores são válidos em um campo. Exemplo: os tipos de associação do CASE [F: imsglobal2017case]; os verbos definidos pelo cmi5.
- **Binding / serialização**: como o modelo vira bytes. Exemplo: o binding XML do QTI 3.0 [F: imsglobal2022qti30, §2]; o binding CSV do OneRoster [F: imsglobal2022oneroster].
- **Protocolo de intercâmbio**: que mensagens trafegam, em que ordem, com que segurança. Exemplo: o fluxo OIDC de lançamento do LTI 1.3 [F: imsglobal2019lti13, §3.4].
- **Empacotamento**: como um conjunto de arquivos e metadados viaja como unidade. Exemplo: o manifesto do Common Cartridge [F: imsglobal2011cc].
- **Serviço / API**: endpoints concretos com contrato. Exemplo: as três subservices do LTI AGS [F: imsglobal2019ltiags].

Um mesmo documento normativo frequentemente especifica várias dessas coisas. O xAPI define modelo de dados *e* API REST contra um LRS [F: ieee2023xapi]. O Caliper define modelo de dados, serialização JSON-LD e uma Sensor API [F: imsglobal2020caliper, §2, §4, §5].

## Problema que resolve

Classificar o padrão por aquilo que ele especifica responde a duas perguntas práticas [I]:

1. **O que ainda falta decidir?** Adotar um modelo de dados não diz como transportá-lo; adotar um protocolo não diz que vocabulário usar nos campos livres.
2. **Dois padrões são concorrentes ou complementares?** Dois padrões que especificam camadas diferentes compõem (LTI transporta, Caliper descreve o evento). Dois que especificam a mesma camada competem (xAPI e Caliper para registro de eventos).

## Fundamentos e funcionamento

Classificação dos padrões deste domínio pelo que cada um especifica (coluna marcada = o padrão trata daquilo):

| Padrão | Modelo de dados | Vocabulário | Binding | Protocolo/API | Empacotamento |
|---|---|---|---|---|---|
| xAPI (IEEE 9274.1.1) | sim | parcial (verbos ficam fora da norma) | JSON | sim (LRS REST) | não |
| cmi5 | perfil do xAPI | sim (9 verbos) | JSON | lançamento + fetch de token | estrutura de curso XML |
| Caliper 1.2 | sim | sim (perfis) | JSON-LD | sim (Sensor/Endpoint) | não |
| LTI 1.3 | mensagens | papéis | JWT | sim (OIDC) | não |
| LTI Advantage | sim (line item, membership) | papéis, status | JSON | sim (REST + OAuth 2) | não |
| SCORM | sim (cmi.*) | sim | XML | API JavaScript | sim (PIF) |
| Common Cartridge | manifesto | tipos de recurso | XML | não | sim |
| QTI 3.0 | sim | sim (interações) | XML | não | perfila Content Packaging |
| OneRoster 1.2 | sim | sim | JSON e CSV | sim (REST) | não |
| Ed-Fi | sim | sim (descriptors) | JSON | sim (API Guidelines) | não |
| CEDS | sim (elementos) | sim | — | não | não |
| IEEE LOM, Dublin Core, LRMI | sim | parcial | XML/RDF/JSON-LD | não | não |
| CASE | sim | sim (tipos de associação) | JSON | sim (REST) | não |
| CTDL, ESCO | sim | sim | RDF | API (ESCO) | não |
| Open Badges 3.0, CLR 2.0 | sim | sim | JSON-LD | sim (REST + OAuth 2) | sim (baking em PNG/SVG) |
| W3C VC 2.0 | sim | não | JSON-LD | não (securing é separado) | não |
| SKOS | sim (meta-modelo) | não | RDF | não | não |

A tabela é interpretação do autor a partir das especificações citadas em cada documento deste domínio [I].

## Requisitos e pressupostos

Para que a classificação seja útil, é preciso que o documento normativo deixe claro o que é normativo e o que é informativo. O Caliper, por exemplo, declara que tudo fora das seções não normativas é normativo e segue RFC 2119 [F: imsglobal2020caliper, §1.3].

## Vantagens e limitações

Limitação: a fronteira entre "vocabulário" e "modelo de dados" é porosa. No xAPI, o verbo é um IRI e a norma não fixa a lista; o significado vem do IRI, não do rótulo exibido [F: adl2016xapidata]. Isso coloca a decisão semântica fora do padrão, o que é liberdade para quem emite e problema para quem consome [I].

## Alternativas e comparações

Ver `iop.catalogo` para a tabela completa com órgão mantenedor, versão vigente e status, e `iop.matriz` para a comparação por caso de uso.

## Relações com outros conceitos

Complementa `iop.fund.niveis-de-interoperabilidade`: esta classificação é a decomposição da camada técnica e da fronteira dela com a semântica.

## Lacunas e questões abertas

- SIF não entrou na tabela por falta de leitura da especificação de infraestrutura (ver `iop.ros.sif`).
- A coluna "vocabulário" do xAPI depende da especificação de Profiles do ADL, não consultada nesta rodada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ieee2023xapi | normativo | 2026-10-29 |
| adl2016xapidata | normativo | 2026-10-29 |
| imsglobal2020caliper | normativo | 2026-10-29 |
| imsglobal2019lti13 | normativo | 2026-10-29 |
| imsglobal2019ltiags | normativo | 2026-10-29 |
| imsglobal2022oneroster | normativo | 2026-10-29 |
| imsglobal2022qti30 | normativo | 2026-10-29 |
| imsglobal2017case | normativo | 2026-10-29 |
| imsglobal2011cc | normativo | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
