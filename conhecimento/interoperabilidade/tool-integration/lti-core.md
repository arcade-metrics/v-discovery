---
id: iop.tool.lti-core
titulo: LTI 1.3 (Learning Tools Interoperability Core)
tipo: protocolo
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2019lti13, edtech2026lti]
relacoes:
  - { tipo: complementa, alvo: iop.tool.lti-advantage }
  - { tipo: depende-de, alvo: iop.fund.identidade-e-contexto }
  - { tipo: alternativa-a, alvo: iop.lr.cmi5 }
  - { tipo: relacionado-a, alvo: iop.tool.common-cartridge }
termos: [plataforma, ferramenta, launch, OIDC, id_token, claim, deployment_id, resource_link, target_link_uri]
---

# LTI 1.3 (Core)

## Definição e terminologia

LTI é o padrão do 1EdTech para integrar uma ferramenta externa (*tool*) a uma plataforma de aprendizagem (*platform*, tipicamente o LMS): o usuário clica em um link dentro do LMS e é levado à ferramenta, autenticado e com contexto.

Versão consultada: **Learning Tools Interoperability Core Specification 1.3, IMS Final Release, Spec Version 1.3, Document Version 3, emitida em 16 de abril de 2019** [F: imsglobal2019lti13]. A página do padrão descreve o LTI 1.3 como a versão corrente, que "addresses education security requirements" [F: edtech2026lti].

## Problema que resolve

Sem LTI, cada par LMS–ferramenta exige integração própria: autenticação, repasse de identidade, contexto de turma e retorno de nota. LTI transforma isso em um contrato n-para-n [I].

## Fundamentos e funcionamento

**Fluxo de lançamento.** O usuário clica em um LTI Link e a plataforma o lança na ferramenta por um HTML form post que carrega o payload da mensagem [F: imsglobal2019lti13, §3.1.5]. Plataformas atuam como OpenID Providers; as mensagens LTI são OpenID tokens, entregues pelo fluxo *third-party initiated login* do OpenID Connect [F: imsglobal2019lti13, §3.4]. Parâmetros opcionais de login: `lti_message_hint`, `lti_deployment_id` e `client_id` [F: imsglobal2019lti13, §4.1]. Mensagens plataforma→ferramenta são OpenID Tokens; ferramenta→plataforma são JWTs [F: imsglobal2019lti13, §4.2]. A plataforma converte o payload JSON em JWT — cada propriedade de topo vira um claim — e o envia por form post no parâmetro `JWT` ou `id_token` [F: imsglobal2019lti13, §4.4].

**Claims de um Resource Link Launch (§5.3)** [F: imsglobal2019lti13]:

| Claim | Regra |
|---|---|
| `message_type` | `LtiResourceLinkRequest` (§5.3.1) |
| `version` | `1.3.0` (§5.3.2) |
| `deployment_id` | sensível a maiúsculas, até 255 caracteres ASCII (§5.3.3) |
| `target_link_uri` | deve coincidir com o valor da requisição de login OIDC; a ferramenta deve usar este claim, e não o valor inicial, para o redirecionamento final (§5.3.4) |
| `resource_link` | `id` estável, único dentro do `deployment_id`, até 255 caracteres ASCII (§5.3.5) |
| `sub` | obrigatório, salvo lançamento anônimo (§5.3.6) |
| `roles` | array que pode ser vazio; se não vazio, deve conter ao menos um papel dos vocabulários definidos (§5.3.7, §A.2) |
| `context` | opcional; se presente, `id` é obrigatório — §5.2 recomenda incluir contexto (§5.4.1) |

**Segurança.** HTTPS com TLS é exigido para mensagens e serviços e para todas as URLs contidas neles [F: imsglobal2019lti13, §3.5]. Todos os serviços da plataforma devem ser protegidos por access token; as ferramentas obtêm tokens pelo perfil JWT de autenticação de cliente OAuth 2.0, e `iss` e `sub` do client assertion devem ser ambos o `client_id` da ferramenta [F: imsglobal2019lti13, §6.2]. Incluir `deployment_id` nas requisições de token é SHOULD [F: imsglobal2019lti13, §6.2.1]. A ferramenta deve identificar o usuário apenas pelo identificador único, não por outros atributos [F: imsglobal2019lti13, §3.3]. Receptores devem ignorar claims que não compreendem [F: imsglobal2019lti13, §3.5, §4.3].

**Serviços relacionados.** O documento cita Basic Outcomes (LTI-BO-11) e Assignment and Grade Services (LTI-AGS-20) no Apêndice D, e Deep Linking 2.0 (LTI-DL-20) na §5 [F: imsglobal2019lti13].

## Requisitos e pressupostos

- Registro prévio entre plataforma e ferramenta: `client_id`, URLs de login e redirect, e chaves públicas (JWKS).
- Relógios sincronizados o suficiente para validação de `exp`/`iat` dos JWTs [I].
- Um `deployment_id` por instalação da ferramenta na plataforma; o mesmo `client_id` pode ter vários deployments [I].

## Vantagens e limitações

Vantagens [I]: adoção ampla entre LMS; separa autenticação (OIDC) de autorização de serviço (OAuth 2 client credentials); o conjunto de claims cobre identidade, contexto e papéis sem acoplar ao modelo de dados do LMS.

Limitações [I]:
- O vocabulário de papéis é do padrão, não da instituição; mapear papéis locais para os de LTI é trabalho semântico que o padrão não faz.
- `deployment_id` até 255 caracteres e `resource_link.id` estável impõem disciplina ao LMS que nem toda instalação cumpre.
- A especificação Core não cobre notas, listas de participantes nem seleção de conteúdo; isso exige LTI Advantage (`iop.tool.lti-advantage`).

## Alternativas e comparações

Para *lançar conteúdo rastreável* em vez de *ferramenta*, cmi5 (`iop.lr.cmi5`) ocupa papel equivalente. Para *empacotar e transportar* links de ferramenta junto com conteúdo, Common Cartridge (`iop.tool.common-cartridge`).

## Métricas e métodos de avaliação

Suíte de certificação do LTI Advantage e ferramenta de diagnóstico em `build.1edtech.org` (acesso com login); existe também uma suíte legada, e a página sugere requisitos de LTI Advantage para RFPs institucionais [F: edtech2026lti].

## Exemplo técnico independente de domínio

```
1. Plataforma -> Ferramenta (GET/POST /login):
     iss, login_hint, target_link_uri, lti_message_hint, client_id, lti_deployment_id
2. Ferramenta -> Plataforma (/authorize):
     scope=openid, response_type=id_token, response_mode=form_post, nonce, state, redirect_uri
3. Plataforma -> Ferramenta (form POST em redirect_uri):
     id_token = JWT { message_type, version, deployment_id, target_link_uri,
                      resource_link{id}, sub, roles[], context{id} }
4. Ferramenta valida assinatura pelo JWKS da plataforma e redireciona para target_link_uri
```

## Relações com outros conceitos

Complementado por `iop.tool.lti-advantage`, que acrescenta os serviços. Depende das decisões de `iop.fund.identidade-e-contexto`.

## Lacunas e questões abertas

- Requisitos de algoritmo de assinatura (RS256), rotação de chaves, `nonce` e `state` não apareceram no trecho lido da especificação (a página excede o limite de leitura); permanecem não verificados em fonte primária.
- Estado de depreciação de LTI 1.1 e LTI 2.0: não documentado nas páginas consultadas.
- Vocabulário completo de papéis (§A.2) não lido.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2019lti13 | normativo | 2026-10-29 |
| edtech2026lti | fornecedor | 2026-10-29 |
