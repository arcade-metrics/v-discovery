---
id: iop.fund.identidade-e-contexto
titulo: Identidade, papéis e contexto na troca de dados educacionais
tipo: conceito
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [adl2016xapidata, imsglobal2019lti13, imsglobal2019ltinrps, imsglobal2022oneroster, aicc2016cmi5, imsglobal2020caliper, brasil2018lgpd]
relacoes:
  - { tipo: depende-de, alvo: iop.fund.niveis-de-interoperabilidade }
  - { tipo: complementa, alvo: iop.fund.privacidade-e-seguranca }
  - { tipo: relacionado-a, alvo: iop.ros.oneroster }
termos: [IFI, inverse functional identifier, sourcedId, deployment_id, registration, contexto, papel, pseudonimização]
---

# Identidade, papéis e contexto

## Definição e terminologia

Trocar um evento de aprendizagem exige responder a três perguntas de identidade [I]: **quem** é o sujeito, **em que agrupamento** (turma, curso, matrícula) a ação ocorreu, e **qual instância** do sistema emitiu o dado.

Cada padrão resolve isso com um mecanismo próprio:

- **xAPI**: o Agent é identificado por exatamente um *Inverse Functional Identifier* (IFI) — `mbox`, `mbox_sha1sum`, `openid` ou `account` (par `homePage` + `name`) [F: adl2016xapidata]. Grupos podem ser anônimos (sem IFI, com lista de membros, e cada grupo anônimo é tratado como distinto) ou identificados (um IFI) [F: adl2016xapidata]. O contexto carrega `registration` (UUID da matrícula/inscrição), `instructor`, `team` e `contextActivities` com os papéis `parent`, `grouping`, `category` e `other` [F: adl2016xapidata].
- **LTI 1.3**: o usuário vem no claim `sub`, obrigatório salvo lançamento anônimo [F: imsglobal2019lti13, §5.3.6]; a instância da integração vem em `deployment_id`, sensível a maiúsculas e limitado a 255 caracteres ASCII [F: imsglobal2019lti13, §5.3.3]; o recurso vem em `resource_link.id`, estável e único dentro do `deployment_id` [F: imsglobal2019lti13, §5.3.5]. A especificação exige que a ferramenta identifique o usuário apenas pelo identificador único, não por outros atributos [F: imsglobal2019lti13, §3.3].
- **LTI NRPS 2.0**: a lista de membros traz `user_id` e `roles` como obrigatórios, e `status` `Active` ou `Inactive` (ausente significa `Active`); `Deleted` só aparece em relatórios de diferença. Atributos como nome e e-mail só são compartilhados com consentimento da plataforma [F: imsglobal2019ltinrps].
- **OneRoster**: a identidade de cada entidade é o `sourcedId`, atribuído pelo sistema de origem [F: imsglobal2022oneroster].
- **cmi5**: o `actor` vai na URL de lançamento como objeto Agent xAPI, e a especificação orienta que não contenha informação pessoal sensível; o `registration` é o UUID da inscrição no curso [F: aicc2016cmi5].

## Problema que resolve

Sem uma resposta comum, o mesmo aluno aparece como três pessoas diferentes em três sistemas, e eventos não podem ser agregados. Com a resposta errada, o identificador vira dado pessoal exposto em claro em cada evento emitido [I].

## Fundamentos e funcionamento

**Identificador opaco versus identificador natural.** `mbox` (e-mail) é natural: legível, fácil de correlacionar entre sistemas, e dado pessoal. `account` com um identificador opaco emitido pela instituição é pseudônimo: exige uma tabela de correspondência sob controle de quem é responsável pelo tratamento. O `mbox_sha1sum` é hash do e-mail, portanto reversível por dicionário quando o universo de e-mails é pequeno [I] — a norma o define apenas como "hex-encoded SHA1 hash of the mailto IRI", sem alegar irreversibilidade [F: adl2016xapidata].

**Escopo do identificador.** `deployment_id` do LTI e `sourcedId` do OneRoster são escopados ao emissor; IFIs de xAPI são globais por construção. Misturar os dois regimes é fonte comum de colisão: dois `sourcedId` iguais vindos de secretarias diferentes não são a mesma turma [I].

**Contexto como chave de agregação.** Em xAPI, `registration` é o que permite reunir eventos de uma mesma tentativa; `contextActivities.grouping` é o que permite reunir por curso. O cmi5 usa exatamente isso para delimitar a sessão [F: aicc2016cmi5]. Em Caliper, o agrupamento vem das entidades referenciadas pelo evento, que formam um grafo dirigido [F: imsglobal2020caliper, §2.2].

## Requisitos e pressupostos

- Existe uma autoridade de identificadores. Na prática, é o sistema de matrícula (SIS) [I].
- O identificador é estável no tempo: o LTI exige `resource_link.id` estável [F: imsglobal2019lti13, §5.3.5]; o mesmo vale, por analogia, para o identificador de aluno [I].
- Se o identificador é pseudônimo, a chave de reidentificação é tratada como dado pessoal e segue a base legal aplicável [F: brasil2018lgpd, art. 5, art. 6].

## Vantagens e limitações

Pseudonimização com `account` é a opção que melhor concilia agregação e minimização [I], ao custo de exigir um serviço de resolução e de quebrar a correlação espontânea com outros sistemas — que é, justamente, o objetivo.

Limitação dos IFIs: a norma xAPI exige *exatamente um* IFI por Agent [F: adl2016xapidata], o que torna a migração de esquema de identificação uma operação que reescreve o histórico ou cria um segundo sujeito [I].

## Alternativas e comparações

| Mecanismo | Escopo | Reidentificável | Onde aparece |
|---|---|---|---|
| `mbox` | global | sim, diretamente | xAPI |
| `mbox_sha1sum` | global | sim, por dicionário | xAPI |
| `account` opaco | emissor + conta | só com tabela | xAPI, cmi5 |
| `sub` (OIDC) | emissor | depende do emissor | LTI 1.3 |
| `sourcedId` | emissor | depende do emissor | OneRoster |

## Métricas e métodos de avaliação

Taxa de resolução de identidade entre dois sistemas (quantos sujeitos de A encontram par em B) e taxa de colisão. Ambas medidas sobre amostra rotulada [I].

## Exemplo técnico independente de domínio

```
Sistema de matrícula emite:   aluno#8f2c1e (opaco, estável)
LMS lança ferramenta:         sub = 8f2c1e, deployment_id = D-42
Ferramenta emite statement:   actor.account = { homePage: "https://sis.exemplo", name: "8f2c1e" }
                              context.registration = <uuid da matrícula>
                              context.contextActivities.grouping = [ turma, curso ]
```

A ferramenta nunca vê o nome do aluno; o LRS agrega por `account.name`; só o SIS resolve `8f2c1e` para uma pessoa.

## Relações com outros conceitos

Depende de `iop.fund.niveis-de-interoperabilidade` (identidade é simultaneamente questão técnica, semântica e jurídica) e complementa `iop.fund.privacidade-e-seguranca`.

## Lacunas e questões abertas

- Não foi verificado como o xAPI 2.0 (IEEE 9274.1.1-2023) alterou as regras de IFI em relação a 1.0.3; a leitura foi feita sobre o texto público de 1.0.3.
- Falta um documento sobre resolução de identidade entre OneRoster e LRS (correspondência `sourcedId` ↔ IFI).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| adl2016xapidata | normativo | 2026-10-29 |
| imsglobal2019lti13 | normativo | 2026-10-29 |
| imsglobal2019ltinrps | normativo | 2026-10-29 |
| imsglobal2022oneroster | normativo | 2026-10-29 |
| aicc2016cmi5 | normativo | 2026-10-29 |
| imsglobal2020caliper | normativo | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
