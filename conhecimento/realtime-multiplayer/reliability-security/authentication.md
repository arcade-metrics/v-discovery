---
id: rtm.sec.authentication
titulo: Autenticação e autorização em sessões de tempo real
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc6455, rfc7519, rfc6749, schneider2013cswsh, owasp2020wstg, cwe1385, heroiclabs2026session, heroiclabs2026authentication, heroiclabs2026sockets, heroiclabs2026configuration, heroiclabs2026authoritative, colyseus2026auth, colyseus2026room, colyseus2026sdk]
relacoes:
  - { tipo: depende-de, alvo: rtm.proto.websocket }
  - { tipo: depende-de, alvo: rtm.sec.transport-security }
  - { tipo: complementa, alvo: rtm.rel.reconnection }
  - { tipo: complementa, alvo: rtm.mp.rooms-and-matches }
  - { tipo: complementa, alvo: rtm.sec.cheating }
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
termos: [JWT, access token, refresh token, Origin, CSWSH, autorização por sala, session token]
---

# Autenticação e autorização em sessões de tempo real

## Definição e terminologia

Autenticação é estabelecer *quem* é o cliente que abre uma conexão de tempo real; autorização é decidir *o que* esse cliente pode fazer dentro dela (entrar numa sala, enviar certo tipo de mensagem, ver certo estado). Em conexões de longa duração, ambas têm uma particularidade: a decisão tomada no instante da abertura precisa continuar válida (ou ser revalidada) por minutos ou horas, e a credencial pode expirar com a conexão ainda viva.

Termos: **JWT** (JSON Web Token), "a compact, URL-safe means of representing claims to be transferred between two parties" [F: rfc7519, abstract]; **access token**, "a string representing an authorization issued to the client" [F: rfc6749, §1.4]; **refresh token**, usado "to obtain a new access token when the current access token becomes invalid or expires" [F: rfc6749, §1.5]; **Origin**, cabeçalho do handshake WebSocket que identifica a origem do script no navegador [F: rfc6455, §4.1]; **CSWSH** (Cross-Site WebSocket Hijacking), ataque em que uma página maliciosa abre um WebSocket autenticado pelo cookie da vítima [F: schneider2013cswsh].

## Problema que resolve

Sem autenticação, qualquer cliente pode se apresentar como qualquer usuário; sem autorização por sala, um cliente autenticado pode entrar em sessões alheias ou enviar comandos de outro jogador. E, especificamente no navegador, o WebSocket tem uma armadilha: o handshake é uma requisição HTTP comum, com cookies, e os navegadores não aplicam a ele as restrições de mesma origem das requisições XHR/fetch; o servidor que confia só no cookie fica exposto a CSWSH [F: schneider2013cswsh; F: cwe1385].

## Fundamentos e funcionamento

### O que a RFC 6455 permite

A RFC é deliberadamente neutra: "This protocol doesn't prescribe any particular way that servers can authenticate clients during the WebSocket handshake. The WebSocket server can use any client authentication mechanism available to a generic HTTP server, such as cookies, HTTP authentication, or TLS authentication" [F: rfc6455, §10.5]. O handshake "MAY include any other header fields, for example, cookies", e cabeçalhos de autenticação [F: rfc6455, §4.1]. Sobre origem: servidores restritos a certos sites "SHOULD verify the Origin field is an origin they expect" e, se inaceitável, "SHOULD respond to the WebSocket handshake with a reply containing HTTP 403 Forbidden status code"; a RFC esclarece que "The intent is not to prevent non-browsers from establishing connections but rather to ensure that trusted browsers under the control of potentially malicious JavaScript cannot fake a WebSocket handshake" [F: rfc6455, §10.2].

### Onde colocar o token na abertura

Três posições, com trade-offs [I], dado que a API WebSocket dos navegadores não permite definir cabeçalhos arbitrários no handshake (fato de plataforma, não da RFC):

| Posição | Funciona no navegador | Risco | Observações |
|---|---|---|---|
| Cabeçalho `Authorization` | não (só clientes nativos) | baixo | permitido pela RFC [F: rfc6455, §4.1]; ideal para SDKs nativos |
| Query string (`?token=`) | sim | token em logs de proxy, histórico, Referer | usar token curto e de uso único, sobre wss [I] |
| Primeira mensagem após abrir | sim | janela entre abrir e autenticar; conexão anônima consome recurso | servidor deve fechar se não autenticar em N ms [I] |
| Cookie de sessão | sim, automático | CSWSH se não validar Origin [F: schneider2013cswsh] | combinar com Origin e token anti-CSRF |
| Subprotocolo (`Sec-WebSocket-Protocol`) | sim | abuso semântico do cabeçalho | técnica de contorno; não normativa [I] |

Os frameworks ilustram: o Nakama emite "a signed JSON Web Token (JWT) that your client presents with each subsequent request", validado "in memory without a database lookup on every call", e os SDKs conectam o socket passando a sessão (`socket.connect(session, appearOnline)`); o SDK Dart recebe `token: session.token` na criação do cliente de WebSocket [F: heroiclabs2026session; F: heroiclabs2026sockets]. A página de sockets não documenta onde o token vai na requisição de upgrade (não verificado). No Colyseus, a autenticação de entrada em sala passa pelo hook `onAuth(client, options, context)`, cujo retorno fica em `client.auth`; o módulo `@colyseus/auth` oferece "revocation-aware JWTs" e a orientação "Verify JWTs and reject revoked sessions in your room's `onAuth` hook"; no SDK de cliente, `client.auth.token` "is sent automatically as an `Authorization` header" nas chamadas HTTP [F: colyseus2026auth; F: colyseus2026room; F: colyseus2026sdk].

### JWT: claims que importam numa conexão longa

A RFC 7519 define `exp` como "the expiration time on or after which the JWT MUST NOT be accepted for processing", com tolerância de relógio pequena a critério do implementador; `jti` como identificador único que "can be used to prevent the JWT from being replayed"; `aud` como destinatários previstos, devendo o token ser rejeitado por quem não está listado [F: rfc7519, §4.1.3-4.1.7]. [I] Num servidor de tempo real, `aud` separa tokens de API HTTP de tokens de socket; `jti` permite revogação por lista; `exp` curto limita o dano de vazamento, mas obriga a tratar expiração *durante* a conexão.

### Expiração e renovação durante a conexão

O OAuth 2.0 define o par access token + refresh token; o refresh é usado só junto ao servidor de autorização [F: rfc6749, §1.5]. O Nakama adota o mesmo desenho: `session.token_expiry_sec` padrão 60 s ("intentionally short") e `session.refresh_token_expiry_sec` padrão 3600 s; os SDKs com auto-refresh verificam "whether the session token expires within the next five minutes" antes de cada chamada [F: heroiclabs2026session; F: heroiclabs2026configuration]. Um detalhe relevante: no Nakama, logout "does not disconnect their open socket connections"; derrubar sockets exige `sessionDisconnect` no servidor [F: heroiclabs2026session]. O Colyseus trata revogação por versão: um banimento "bumps `tokenVersion`", com "existing JWTs rejected on the next room join" [F: colyseus2026auth].

[I] Três políticas possíveis para o token que expira com o socket aberto: (a) a conexão herda a validade da abertura e só revalida ao reconectar (simples; revogação lenta); (b) o cliente envia o token renovado por mensagem e o servidor atualiza a identidade da conexão (revogação em minutos); (c) o servidor fecha a conexão ao expirar, forçando reconexão com token novo (revogação exata; custo de reconexão, ver `rtm.rel.reconnection`). A escolha depende do valor do que a sessão protege.

### Autorização por sala

Autenticar o usuário não autoriza nada em particular. Três verificações mínimas [I]: (1) ao entrar: o usuário pode entrar nesta sala (convite, matchmaking, propriedade)? O Colyseus coloca isso em `onAuth` antes de `onJoin` [F: colyseus2026room]; o Nakama expõe `match_join_attempt` no handler autoritativo [F: heroiclabs2026authoritative]. (2) por mensagem: o remetente é dono da entidade que o comando afeta? O servidor nunca aceita o "id do jogador" vindo do payload; usa a identidade da conexão. (3) por leitura: o cliente só recebe o que pode ver (ver `rtm.sync.interest-management` e `rtm.sec.cheating`).

### CSWSH

Schneider (2013) descreve o ataque: a vítima autenticada visita uma página maliciosa, que abre um WebSocket ao servidor alvo; o navegador anexa o cookie de sessão; sem checagem de Origin, o servidor aceita, e o atacante lê os dados empurrados pelo servidor e envia mensagens como a vítima, o que o autor chama de CSRF estendido a leitura e escrita [F: schneider2013cswsh]. Mitigações do autor: validar Origin no handshake e "Use session-individual random tokens (like CSRF-Tokens) on the handshake request and verify them on the server" [F: schneider2013cswsh]. A classe foi catalogada como CWE-1385, "Missing Origin Validation in WebSockets", cujas mitigações listadas incluem verificar Origin, exigir tokens CSRF aleatórios, usar wss, autenticar antes de estabelecer a conexão, limitar taxa e tamanho de payload, e tratar toda entrada como não confiável [F: cwe1385]. O guia de testes OWASP (WSTG-CLNT-10) afirma: "It is the server's responsibility to verify the Origin header in the initial WebSocket handshake", e que, como "WebSockets do not handle authentication" nem autorização, os testes usuais de caixa-preta se aplicam [F: owasp2020wstg].

## Requisitos e pressupostos

- Transporte cifrado (wss) é pré-condição; token em query string sobre ws:// é texto claro (ver `rtm.sec.transport-security`).
- Relógios razoavelmente sincronizados entre emissor e verificador de JWT, pela semântica de `exp` [F: rfc7519, §4.1.4].
- Chave de assinatura protegida e com rotação; validação de assinatura em todo nó que aceita sockets.
- Lista de origens permitidas mantida com a configuração de deploy.

## Vantagens e limitações

- JWT auto-contido permite validar sem banco por conexão [F: heroiclabs2026session], o que importa em picos de reconexão; a contrapartida é que revogação exige `jti` em lista ou versão de token [I].
- Token na query string é a opção mais compatível com navegadores e a mais exposta a vazamento por logs.
- Origin protege contra scripts em navegadores, não contra clientes nativos maliciosos, por definição da própria RFC [F: rfc6455, §10.2]; para esses, ver `rtm.sec.cheating`.

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`: tempo de handshake incluindo validação, taxa de conexões rejeitadas por origem ou token, conexões anônimas abertas sem autenticar em N ms, tempo entre revogação e desconexão efetiva. Testes: WSTG-CLNT-10 [F: owasp2020wstg].

## Exemplo técnico independente de domínio

```text
on_upgrade(request):
    if request.origin not in ALLOWED_ORIGINS: respond(403)            # rfc6455 §10.2
    token = request.header("Authorization") or request.query("token")
    if token is None: accept() ; start_timer(AUTH_DEADLINE, close_if_unauthenticated)
    else: identity = verify_jwt(token, aud = "realtime", now) or respond(401)
          accept(identity)

on_message(conn, msg):
    if conn.identity is None and msg.type != AUTH: close(conn, 4401)
    if msg.type == AUTH: conn.identity = verify_jwt(msg.token, ...) ; return
    if msg.type == REFRESH: conn.identity = verify_jwt(msg.token, ...) ; return
    if conn.identity.exp < now: close(conn, 4401)                      # politica (c)
    if not can(conn.identity, msg.room, msg.action): drop(msg) ; audit()
    apply(msg, actor = conn.identity.sub)                             # nunca msg.player_id
```

## Relações com outros conceitos

Depende de `rtm.proto.websocket` (handshake) e de `rtm.sec.transport-security` (sigilo do token). Complementa `rtm.rel.reconnection` (renovação na queda), `rtm.mp.rooms-and-matches` (autorização por sala) e `rtm.sec.cheating` (clientes nativos hostis). Especificado pelas RFCs indexadas em `rtm.std.index`. Implementado por `rtm.fw.nakama` e `rtm.fw.colyseus`.

## Lacunas e questões abertas

- Não verificado: posição do token na requisição de upgrade do socket do Nakama (query string ou outro); a documentação consultada mostra apenas a API do SDK.
- Não verificado: parâmetros `context` de `onAuth` no Colyseus (acesso a cabeçalhos ou token); a página consultada remete a outra não lida.
- Não há nas fontes consultadas comparação medida de custo entre as três políticas de expiração durante a conexão.
- A versão "latest" do WSTG redireciona; o texto citado é da v4.2.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc6455 | normativo | 2026-10-29 |
| rfc7519 | normativo | 2026-10-29 |
| rfc6749 | normativo | 2026-10-29 |
| schneider2013cswsh | tecnico | 2026-10-29 |
| owasp2020wstg | tecnico | 2026-10-29 |
| cwe1385 | tecnico | 2026-10-29 |
| heroiclabs2026session | fornecedor | 2026-10-29 |
| heroiclabs2026authentication | fornecedor | 2026-10-29 |
| heroiclabs2026sockets | fornecedor | 2026-10-29 |
| heroiclabs2026configuration | fornecedor | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| colyseus2026auth | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| colyseus2026sdk | fornecedor | 2026-10-29 |
