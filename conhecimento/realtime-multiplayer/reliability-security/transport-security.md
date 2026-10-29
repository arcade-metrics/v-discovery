---
id: rtm.sec.transport-security
titulo: Segurança de transporte: TLS, wss, DTLS e QUIC
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [rfc8446, rfc6455, rfc9147, rfc9001, rfc9000, rfc8827, cwe1385, owasp2020wstg]
relacoes:
  - { tipo: depende-de, alvo: rtm.proto.websocket }
  - { tipo: depende-de, alvo: rtm.proto.webrtc }
  - { tipo: depende-de, alvo: rtm.proto.quic }
  - { tipo: complementa, alvo: rtm.sec.authentication }
  - { tipo: complementa, alvo: rtm.sec.cheating }
  - { tipo: complementa, alvo: rtm.proto.webtransport }
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: relacionado-a, alvo: rtm.net.latency }
termos: [TLS 1.3, wss, DTLS 1.3, DTLS-SRTP, QUIC, 0-RTT, replay, certificado, AEAD]
---

# Segurança de transporte: TLS, wss, DTLS e QUIC

## Definição e terminologia

Segurança de transporte é o conjunto de garantias que a camada de transporte cifrada oferece aos dados *em trânsito* entre dois endpoints. A RFC 8446 enumera as três que o TLS 1.3 fornece: autenticação ("The server side of the channel is always authenticated; the client side is optionally authenticated"), confidencialidade ("Data sent over the channel after establishment is only visible to the endpoints") e integridade ("Data sent over the channel after establishment cannot be modified by attackers without detection") [F: rfc8446, §1].

Para os transportes do domínio, as especificações relevantes são: TLS 1.3 (RFC 8446, agosto de 2018, que "supersedes and obsoletes previous versions of TLS, including version 1.2" [F: rfc8446, §1]); WebSocket sobre TLS, o esquema `wss` [F: rfc6455, §3]; DTLS 1.3 (RFC 9147, abril de 2022, que "obsoletes RFC 6347" [F: rfc9147, abstract]) para datagramas; e QUIC, que integra TLS 1.3 no próprio transporte (RFC 9001, maio de 2021 [F: rfc9001]).

## Problema que resolve

Em tempo real, o tráfego inclui credenciais (ver `rtm.sec.authentication`), estado de jogo que vale dinheiro ou vantagem, e conteúdo colaborativo privado. Sem cifra, qualquer nó no caminho lê e altera. Com cifra de transporte, o que resta de exposição está nos endpoints, e é importante dizer isso com clareza: TLS não resolve cheating nem autentica o usuário, só o servidor e o canal.

## Fundamentos e funcionamento

### TLS 1.3 e o que mudou

A RFC 8446 lista as diferenças em relação ao TLS 1.2: remoção de algoritmos simétricos legados, com todos os restantes sendo AEAD; adição de um modo 0-RTT "at the cost of certain security properties"; remoção de suites RSA estático e Diffie-Hellman estático, de modo que toda troca de chaves oferece sigilo futuro (forward secrecy); cifragem de todas as mensagens de handshake após o ServerHello; derivação de chaves redesenhada com HKDF [F: rfc8446, §1.2]. [I] Para tempo real importa sobretudo o handshake mais curto (1-RTT) e o 0-RTT para reconexões rápidas, com a ressalva de replay abaixo.

### wss: WebSocket sobre TLS

A RFC 6455 define os esquemas `ws` e `wss`, com portas padrão 80 e 443 [F: rfc6455, §3]; com o flag seguro, "the client MUST perform a TLS handshake over the connection" antes de enviar o handshake WebSocket [F: rfc6455, §4.1]. A seção de segurança estabelece que "Connection confidentiality and integrity is provided by running the WebSocket Protocol over TLS (wss URIs)", que "WebSocket implementations MUST support TLS and SHOULD employ it when communicating with their peers", e alerta que "some TLS cipher mechanisms don't provide connection confidentiality", devendo os clientes usar "only Strong TLS algorithms" [F: rfc6455, §10.6]. O CWE-1385 lista "Use TLS: Connect over wss" entre as mitigações de WebSocket [F: cwe1385], e o guia OWASP orienta a verificar "that the WebSocket connection is using SSL to transport sensitive information wss://" e a testar a implementação TLS [F: owasp2020wstg].

### DTLS 1.3 para UDP e WebRTC

O TLS pressupõe um fluxo confiável e ordenado; sobre datagramas isso não existe. A RFC 9147 explica que "Datagram transport neither requires nor provides reliable or in-order delivery of data" e que "the DTLS protocol does not compensate for lost or reordered data traffic" [F: rfc9147, §3]. Para que o handshake funcione, "DTLS uses a simple retransmission timer to handle packet loss", adiciona números de sequência a registros e mensagens de handshake, suporta fragmentação e reassemblagem, e "optionally supports record replay detection" [F: rfc9147, §3]; "Each DTLS record contains a sequence number to provide replay protection" [F: rfc9147, §4.5.1]. Contra amplificação e DoS, "DTLS servers SHOULD perform a cookie exchange whenever a new handshake is being performed" [F: rfc9147, §5.1]. A RFC resume as garantias como equivalentes às do TLS "with the exception of order protection / non-replayability" [F: rfc9147, abstract].

No WebRTC, a arquitetura de segurança exige: "Implementations MUST support DTLS [RFC6347] and DTLS-SRTP [RFC5763] [RFC5764] for SRTP keying", "Implementations MUST support SCTP over DTLS [RFC8261]" e "All data channels MUST be secured via DTLS" [F: rfc8827]. [I] Isto é, canais de dados WebRTC (ver `rtm.proto.webrtc`) são sempre cifrados; a versão de DTLS referenciada pela RFC 8827 (janeiro de 2021) é a 1.2, anterior à 9147.

### QUIC: TLS embutido

A RFC 9001 "describes how QUIC [...] is secured using TLS [TLS13]": QUIC "uses keys derived from a TLS handshake", as mensagens de handshake TLS viajam em frames CRYPTO, e "TLS record protection is not used by QUIC"; em vez disso, QUIC "assumes responsibility for the confidentiality and integrity protection of packets", protegendo payload com o AEAD negociado e, adicionalmente, partes do cabeçalho, "in particular the Packet Number field" [F: rfc9001, §1, §3, §4.1.3, §5, §5.3]. [I] Diferente de "WebSocket sobre TLS", não existe QUIC sem cifra; é o transporte do WebTransport (ver `rtm.proto.webtransport`) e do HTTP/3, e traz migração de conexão (ver `rtm.rel.reconnection`) já protegida pelos connection IDs [F: rfc9000, §9].

### 0-RTT e replay

Tanto TLS 1.3 quanto QUIC permitem enviar dados no primeiro voo quando há PSK de sessão anterior. A RFC 8446 avisa: "There are no guarantees of non-replay between connections" para dados 0-RTT [F: rfc8446, §2.3]. A RFC 9001 reforça que "This application data can be replayed by an attacker" e que "the lack of replay protection means that restrictions on their use are necessary" [F: rfc9001, §2.1, §5.6]. [I] Para tempo real: a primeira mensagem de uma reconexão 0-RTT não pode ser um comando com efeito (um lance, uma compra); pode ser um "resume" idempotente. Ver `rtm.rel.delivery-semantics`.

### Certificados

A autenticação do servidor no TLS depende de o cliente validar o certificado contra âncoras de confiança. Em navegadores isso é automático e inescapável; em clientes nativos (SDKs de jogo, dispositivos móveis), a validação é configurável e, se desabilitada "para testes", converte o canal em cifra sem autenticação, vulnerável a interposição [I]. A RFC 6455 lembra que, no WebSocket, TLS também pode autenticar o *cliente* ("TLS authentication") [F: rfc6455, §10.5], opção rara em consumo massivo por custo de distribuição de certificados [I].

### O que a criptografia de transporte não resolve

1. **Cheating.** Um cliente modificado cifra e assina seu tráfego forjado corretamente; o TLS protege o canal contra terceiros, não o servidor contra o cliente. Ver `rtm.sec.cheating`.
2. **Autenticação do usuário.** TLS autentica o servidor (e opcionalmente a máquina cliente); quem é o usuário é problema da aplicação (token, JWT). Ver `rtm.sec.authentication`.
3. **CSWSH.** O ataque funciona sobre wss, porque o navegador da vítima faz o handshake legitimamente; a defesa é Origin e token, não cifra [F: cwe1385].
4. **Exposição nos endpoints.** Dados decifrados no cliente são legíveis pelo usuário (wallhack); logs no servidor com tokens de query string são legíveis por quem acessa logs.
5. **Metadados.** Tamanho, frequência e temporização de pacotes continuam visíveis; em tempo real, isso pode revelar atividade (por exemplo, rajadas em combate) [H].

## Requisitos e pressupostos

- Certificados válidos e renovação automática; falha de renovação derruba todas as conexões novas.
- Suporte a TLS 1.3 nos dois lados; a RFC 6455 exige TLS, não uma versão específica [F: rfc6455, §10.6].
- Para UDP próprio (sem WebRTC nem QUIC), DTLS precisa ser integrado pela aplicação; o custo de handshake inclui o cookie exchange [F: rfc9147, §5.1].

## Vantagens e limitações

- Custo de latência: um handshake 1-RTT a mais na abertura; em reconexões, 0-RTT reduz isso com a restrição de replay. Custo de CPU por pacote com AEAD é pequeno em hardware moderno, mas não nulo em servidores que processam dezenas de milhares de pacotes por segundo [H].
- Terminação de TLS em balanceadores simplifica certificados e permite inspeção, mas deixa o trecho interno em claro, o que é decisão de modelo de ameaça [I].

## Alternativas e comparações

| Transporte | Cifra | Especificação | Replay | Observação |
|---|---|---|---|---|
| WebSocket `ws://` | nenhuma | RFC 6455 | n/a | só em rede confiável e testes |
| WebSocket `wss://` | TLS | RFC 6455 §10.6 + RFC 8446 | protegido após handshake; 0-RTT não | padrão para navegadores |
| WebRTC data channel | DTLS (SCTP sobre DTLS) | RFC 8827 | detecção opcional de registro [F: rfc9147] | obrigatório, sem opção em claro |
| QUIC / WebTransport | TLS 1.3 integrado | RFC 9001 | 0-RTT não protegido | sem modo em claro |
| UDP próprio | DTLS 1.3 ou cifra própria | RFC 9147 | opcional | cifra própria é risco; preferir DTLS [I] |

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`: tempo de handshake (TLS + WebSocket) p50/p95/p99; fração de conexões com 0-RTT aceito; erros de certificado por versão de cliente; CPU por conexão em carga (ver `rtm.perf.load-testing`). Testes: WSTG-CLNT-10 inclui verificação de wss e de fraquezas de TLS [F: owasp2020wstg].

## Exemplo técnico independente de domínio

```text
# Politica de endpoint de tempo real
listen(wss, port = 443, tls = { min_version: 1.3, certs: auto_renew })
reject_if(scheme == "ws" and env == "production")
on_0rtt_data(msg):                 # rfc8446 §2.3 / rfc9001 §5.6
    if msg.has_side_effects(): defer_until_handshake_complete(msg)
    else: handle(msg)              # ex.: RESUME idempotente
on_upgrade(req): validate_origin(req) ; authenticate(req)   # TLS nao faz isso
```

## Relações com outros conceitos

Depende dos transportes `rtm.proto.websocket`, `rtm.proto.webrtc` e `rtm.proto.quic`. Complementa `rtm.sec.authentication` (identidade do usuário), `rtm.sec.cheating` (o que a cifra não cobre) e `rtm.proto.webtransport`. Especificado pelas RFCs indexadas em `rtm.std.index`. Relaciona-se a `rtm.net.latency` pelo custo de handshake.

## Lacunas e questões abertas

- A seção 8 da RFC 8446 (mecanismos anti-replay para 0-RTT) não foi lida nesta sessão; só a ressalva da §2.3.
- Não foi consultada fonte com medição de custo de CPU de AEAD por pacote em servidores de jogo; fica como [H].
- Status de adoção de DTLS 1.3 em implementações WebRTC: não verificado.
- Nota de consistência (revisão de 2026-10-29): segundo `rtm.std.index`, a RFC 8446 foi obsoletada pela RFC 9846 (2026) e a RFC 9147 foi atualizada pela RFC 9853. O conteúdo citado aqui vem da RFC 8446; uma revisão futura deve conferir as seções correspondentes na RFC 9846.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| rfc8446 | normativo | 2026-10-29 |
| rfc6455 | normativo | 2026-10-29 |
| rfc9147 | normativo | 2026-10-29 |
| rfc9001 | normativo | 2026-10-29 |
| rfc9000 | normativo | 2026-10-29 |
| rfc8827 | normativo | 2026-10-29 |
| cwe1385 | tecnico | 2026-10-29 |
| owasp2020wstg | tecnico | 2026-10-29 |
