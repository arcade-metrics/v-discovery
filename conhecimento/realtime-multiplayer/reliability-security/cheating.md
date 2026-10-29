---
id: rtm.sec.cheating
titulo: Cheating em sistemas multiplayer: taxonomia e mitigação
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [yan2005classification, webb2007cheating, heroiclabs2026multiplayer, cwe1385, rfc8446]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: complementa, alvo: rtm.sync.interest-management }
  - { tipo: complementa, alvo: rtm.sec.authentication }
  - { tipo: complementa, alvo: rtm.sec.transport-security }
  - { tipo: complementa, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.mp.turn-based }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [cheating, fairness, misplaced trust, wallhack, map hack, bot, look-ahead cheat, suppress-correct cheat, lag switch, autoridade do servidor, validação de entradas, detecção estatística]
---

# Cheating em sistemas multiplayer: taxonomia e mitigação

## Definição e terminologia

Yan e Randell (2005) adotam a definição: "Any behaviour that a player uses to gain an advantage over his peer players or achieve a target in an online game is cheating if, according to the game rules or at the discretion of the game operator [...], the advantage or the target is one that he is not supposed to have achieved" [F: yan2005classification, §1]. A tese central do artigo é que, embora o cheating decorra em grande parte de falhas de segurança, "the four traditional aspects of security — confidentiality, integrity, availability and authenticity — are insufficient to explain it. Instead, fairness becomes a vital additional aspect" [F: yan2005classification, abstract].

O conceito vale além de jogos: numa sessão colaborativa ou por turnos, "cheating" é qualquer manipulação do protocolo ou do cliente que dê a um participante vantagem ou informação indevida [I]. Este documento usa a taxonomia de jogos por ser a literatura mais madura.

## Problema que resolve

Um cliente é, por definição, código que roda na máquina do adversário. Tudo que o cliente sabe, o usuário pode ler; tudo que o cliente decide, o usuário pode alterar; tudo que o cliente envia, o usuário pode forjar. Projetar para isso é a diferença entre um sistema que resiste a trapaça e um que depende da boa vontade dos participantes.

## Fundamentos e funcionamento

### A taxonomia de Yan e Randell (2005)

O artigo revisa uma lista anterior de onze formas e apresenta "a revised list, which classifies cheats into 15 categories" [F: yan2005classification, §3.1], rotuladas de A a O, e as organiza numa taxonomia tridimensional: "the underlying vulnerability (what is exploited?), consequence (what type of failure can be achieved?) and the cheating principal (who is cheating?)" [F: yan2005classification, abstract]. As categorias mais relevantes para sistemas de tempo real, com a descrição dos autores:

| Categoria (Yan & Randell) | Descrição no artigo | Leitura em tempo real [I] |
|---|---|---|
| A. Exploiting Misplaced Trust | "tampering with game code, configuration data, or both, on the client side"; exemplo do "map hack" que revela áreas não exploradas em RTS [F: yan2005classification, §3.1] | cliente modificado; qualquer lógica confiada ao cliente |
| E. Exploiting Machine Intelligence | programas que "can compete with human players" em lugar deles [F: yan2005classification, §3.1] | bots e aimbots |
| F. Modifying Client Infrastructure | modificar "device drivers in his operating system", como "a graphics driver to make a wall transparent [...] the so-called 'wall hack'" [F: yan2005classification, §3.1] | information exposure: o cliente recebe mais do que deveria mostrar |
| G. Denying Service to Peer Players | atrasar respostas do oponente "by flooding his network connection" [F: yan2005classification, §3.1] | DoS seletivo; lag switch aplicado ao outro |
| H. Timing Cheating | "a cheating player can delay his own move until he knows all the opponents' moves" (look-ahead cheat) e o "suppress-correct cheat", que dropa mensagens "at the 'right' time" [F: yan2005classification, §3.1] | lag switch próprio; exploração de lag compensation e de lockstep |
| C. Abusing the Game Procedure | "escaping: a cheater disconnects himself from the game system when he is going to lose" [F: yan2005classification, §3.1] | abandono estratégico; interação com janela de graça de reconexão |
| B. Collusion | troca ilícita de informação entre jogadores que deveriam ser adversários [F: yan2005classification, §3.1] | fora do alcance técnico do protocolo |
| I, J, K. Passwords, Lack of Secrecy, Lack of Authentication | credenciais comprometidas; tráfego ou dados legíveis; ausência de autenticação mútua (ex.: servidor falso) [F: yan2005classification, §3.1] | ver `rtm.sec.authentication` e `rtm.sec.transport-security` |
| L. Bug or Loophole | explorar defeito do jogo [F: yan2005classification, §3.1] | validação de entradas e invariantes |
| M. Compromising Game Servers | adulterar programas ou dados no servidor [F: yan2005classification, §3.1] | segurança de infraestrutura, fora de escopo |

Webb e Soh (2007) publicaram uma revisão de cheating em jogos em rede (DIMEA 2007, DOI 10.1145/1306813.1306839), cujos metadados foram verificados; o conteúdo do artigo não pôde ser aberto nesta sessão (não verificado) e não é citado quanto a categorias.

### Mapeamento para a pilha de tempo real

A documentação do Nakama expõe a dicotomia de arquitetura que determina quase tudo: em modo relayed, o servidor "has no insight into what the data being sent is and no oversight into whether the data is correct"; em modo autoritativo, "all exchanges of gameplay data are validated and broadcast by the server" [F: heroiclabs2026multiplayer]. [I] Relay e P2P (ver `rtm.arch.relay-server`, `rtm.arch.peer-to-peer`) deixam as categorias A, E, F e H quase sem defesa técnica; o servidor autoritativo (ver `rtm.arch.authoritative-server`) é a pré-condição de todas as mitigações abaixo.

### Mitigações e o que cada uma cobre

1. **Autoridade no servidor.** O servidor simula e decide; o cliente envia intenções (entradas), não resultados. Cobre A e L para tudo que o servidor valida. Custo: latência percebida, mitigada por predição (ver `rtm.pred.client-side-prediction`), que por sua vez reabre a questão de reconciliação.
2. **Validação de entradas.** Cada entrada é checada contra o que é fisicamente ou regimentalmente possível: taxa máxima de comandos, velocidade máxima, alcance, cooldowns, turno do jogador. Cobre A e L; é a implementação concreta de "validated [...] by the server" [F: heroiclabs2026multiplayer]. [I] Também faz parte do tratamento de entrada não confiável que o CWE-1385 recomenda: "Treat all input as untrusted" [F: cwe1385].
3. **Interest management.** O servidor só envia a cada cliente o que ele pode ver (ver `rtm.sync.interest-management`). É a única defesa estrutural contra F (wallhack) e contra o map hack de A: não se pode revelar o que não chegou ao cliente [I]. Limite: o que precisa chegar para predição e interpolação suaves (por exemplo, um adversário prestes a aparecer) já é informação exposta.
4. **Detecção estatística.** Para E (bots, aimbots) e para H (timing), a mitigação é probabilística: distribuição de tempos de reação, precisão fora do envelope humano, padrões de perda de pacote correlacionados com situações vantajosas [I]. Produz falsos positivos e exige processo de revisão; não é prevenção.
5. **Tratamento do timing.** Para o look-ahead em lockstep (ver `rtm.arch.deterministic-lockstep`), o servidor ou o protocolo pode exigir compromisso antes da revelação (commit-reveal) [H]. Para lag compensation (ver `rtm.pred.lag-compensation`), limitar o quanto o servidor "volta no tempo" em favor de um cliente reduz o ganho do lag switch, ao custo de prejudicar clientes com latência alta legítima [I].
6. **Autenticação e transporte cifrado.** Cobrem I, J, K (ver `rtm.sec.authentication`, `rtm.sec.transport-security`). O TLS "is designed to prevent eavesdropping, tampering, and message forgery" entre endpoints [F: rfc8446, abstract], o que elimina a adulteração *no caminho*, não no cliente.
7. **Integridade do cliente (anti-cheat local).** Verificação de assinatura, detecção de injeção, kernel drivers. Trata A e F onde o servidor não alcança; é uma corrida armamentista e depende de plataforma. Sem fonte primária verificada nesta sessão; registrado como [H].

### Limites

- Nada que roda no cliente é confiável; defesas no cliente elevam o custo, não eliminam o ataque [I].
- Information exposure tem piso: dados necessários para renderizar são, por definição, expostos. Interest management reduz o excedente, não o necessário.
- Collusion (B) e social engineering (O) são extraprotocolo [F: yan2005classification, §3.1].
- Detecção estatística é posterior ao dano e exige evidência; sistemas de reputação e revisão humana completam o quadro [I].
- Yan e Randell observam que um caso real "may be complex and involves multiple cheating forms", citando um caso de collusion que abusa do procedimento e explora um loophole ao mesmo tempo [F: yan2005classification, §3.1]; defesas isoladas falham contra combinações.

## Requisitos e pressupostos

- Arquitetura autoritativa (ou, em lockstep, determinismo com verificação cruzada de hashes de estado).
- Modelo explícito de "o que cada cliente pode ver e fazer" por sala e por momento.
- Telemetria de comandos por cliente para detecção posterior (ver `rtm.perf.metrics`).

## Vantagens e limitações

Tratar cheating como requisito de fairness, e não só de segurança clássica, muda o que se mede: além de confidencialidade e integridade, importam simetria de informação e de tempo entre participantes [F: yan2005classification, abstract] [I]. A limitação estrutural é que toda mitigação forte custa latência (autoridade, validação) ou largura de banda (interest management mais fino) ou falsos positivos (detecção).

## Alternativas e comparações

| Arquitetura | Cliente modificado (A) | Wallhack (F) | Timing (H) | Bots (E) |
|---|---|---|---|---|
| P2P sem autoridade | sem defesa | sem defesa | sem defesa | detecção |
| Relay | sem defesa [F: heroiclabs2026multiplayer] | sem defesa | sem defesa | detecção |
| Autoritativo | validação | interest management | limites de compensação | detecção |
| Lockstep determinístico | hash cruzado detecta divergência | sem defesa (todos têm tudo) | look-ahead vulnerável | detecção |

[I] Tabela sintetiza as seções anteriores; "sem defesa" significa sem defesa estrutural no protocolo.

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`: taxa de entradas rejeitadas por validação por cliente; distribuição de intervalos entre comandos; correlação entre perda de pacotes do cliente e eventos vantajosos; bytes enviados ao cliente que ele não renderizou (medida do excedente de informação). Testes: cliente de carga com entradas inválidas (ver `rtm.perf.load-testing`), emulação de lag switch (ver `rtm.perf.network-emulation`).

## Exemplo técnico independente de domínio

```text
# Validação de entrada no servidor autoritativo
on_input(conn, input):
    p = player_of(conn)                         # identidade da conexão, nunca do payload
    if now - p.last_input_at < MIN_INTERVAL: reject("rate") ; p.strikes += 1 ; return
    if not p.is_turn and game.is_turn_based: reject("turn") ; return
    if distance(p.pos, input.target) > p.max_reach(dt): reject("reach") ; return
    if input.seq <= p.last_seq: return          # duplicata, ver rtm.rel.delivery-semantics
    apply(p, input) ; p.last_seq = input.seq ; p.last_input_at = now
    telemetry.record(p.id, input, accepted = true)

# Interest management como defesa: so' envia o que o cliente pode ver
for c in clients: send(c, filter(world, visible_from(c)))
```

## Relações com outros conceitos

Depende de `rtm.arch.authoritative-server`. Complementa `rtm.sync.interest-management` (information exposure), `rtm.sec.authentication` e `rtm.sec.transport-security` (categorias I, J, K) e `rtm.pred.lag-compensation` (timing). Relaciona-se a `rtm.arch.peer-to-peer` e `rtm.arch.deterministic-lockstep` (superfícies de ataque distintas) e a `rtm.mp.turn-based` (look-ahead, escaping). Avaliado por `rtm.perf.metrics`.

## Lacunas e questões abertas

- Webb e Soh (2007): só metadados verificados (crossref); conteúdo não acessível nesta sessão. A versão de periódico de 2008 dos mesmos autores também não foi lida.
- Não foi localizada fonte primária verificável sobre anti-cheat de cliente (drivers, atestação) nem sobre eficácia medida de detecção estatística; ambos ficam como [H].
- Commit-reveal contra look-ahead em lockstep: sem fonte verificada nesta sessão.
- Falta literatura específica sobre "cheating" em colaboração sem jogo (edição concorrente, presença falsa); a transposição é interpretação.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| yan2005classification | academico | 2026-10-29 |
| webb2007cheating | academico (metadados apenas) | 2026-10-29 |
| heroiclabs2026multiplayer | fornecedor | 2026-10-29 |
| cwe1385 | tecnico | 2026-10-29 |
| rfc8446 | normativo | 2026-10-29 |
