---
id: rtm.mp.matchmaking
titulo: Matchmaking e sistemas de rating
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nakama2026matchmaker, nakama2026configuration, nakama2026parties, colyseus2026matchmaker, colyseus2026queue, colyseus2026visibility, elo1978rating, glickman2016glicko, glickman2026site, herbrich2006trueskill, microsoft2026trueskill]
relacoes:
  - { tipo: complementa, alvo: rtm.mp.rooms-and-matches }
  - { tipo: complementa, alvo: rtm.mp.session-lifecycle }
  - { tipo: depende-de, alvo: rtm.mp.presence }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.perf.qoe-thresholds }
termos: [matchmaking, ticket, rating, Elo, Glicko, rating deviation, TrueSkill, match quality, seat reservation, queue]
---

# Matchmaking e sistemas de rating

## Definição e terminologia

**Matchmaking** é o processo de agrupar participantes que esperam em uma fila em partidas compatíveis, segundo critérios como habilidade, região ou latência, tamanho de grupo e modo de jogo. Distingue-se de dois vizinhos: a **listagem de salas** (lobby), em que o próprio usuário escolhe onde entrar, e o **rating**, que é a estimativa numérica de habilidade usada como um dos critérios.

Termos recorrentes:

- **Ticket**: pedido de matchmaking de um usuário ou grupo; no Nakama "cada ticket atua como buscador e como alvo que outros podem encontrar" [F: nakama2026matchmaker].
- **Seat reservation**: no Colyseus, toda chamada de join do SDK passa pelo matchmaker, que "answers with a seat reservation" contendo `name`, `sessionId`, `roomId` e `processId` [F: colyseus2026matchmaker].
- **Rating**: valor estimado de força de um competidor. Elo (1978) é o sistema de referência em xadrez [F: elo1978rating]; Glicko adiciona um **rating deviation (RD)**, um desvio-padrão que "mede a incerteza de um rating" [F: glickman2016glicko]; TrueSkill modela a habilidade como gaussiana com média μ e desvio σ e "tracks the uncertainty about player skills" [F: herbrich2006trueskill].

## Problema que resolve

[I] Jogadores chegam a instantes diferentes, com habilidades, regiões e tamanhos de grupo distintos. O sistema precisa decidir, em tempo limitado, uma partição em partidas que maximize qualidade (equilíbrio, latência aceitável, grupo intacto) sem fazer ninguém esperar demais. A documentação do Nakama é explícita em que "match success and duration are not guaranteed; they depend on pool size and criteria" [F: nakama2026matchmaker].

## Fundamentos e funcionamento

### Fila e critérios

No Nakama, o matchmaking é um processo em lote repetido: a cada passagem (intervalo `matchmaker.interval_sec`, padrão 15 s) os tickets são comparados e formam partidas que satisfaçam mutuamente critérios e contagens. Cada ticket traz: `properties` (pares chave-valor string ou numéricos descrevendo o remetente, por exemplo `region: "europe"`, `rank: 8`), `min_count` e `max_count` (inclusivos do remetente), opcionalmente `count_multiple`, e uma `query` sobre as propriedades dos outros (por exemplo `+properties.region:europe +properties.rank:>=5 +properties.rank:<=10`); `"*"` casa com qualquer um. O matchmaker tenta primeiro o máximo e recua até o mínimo; `matchmaker.max_intervals` (padrão 2) define quantas passagens no máximo antes de aceitar o mínimo; `max_tickets` por sessão ou party tem padrão 3 [F: nakama2026matchmaker] [F: nakama2026configuration]. Só usuários com socket aberto participam; desconectar cancela os tickets [F: nakama2026matchmaker].

O Colyseus 0.18 oferece dois caminhos. O primeiro é a seleção de sala: `joinOrCreate()` filtra candidatas pelas opções registradas em `filterBy([...])`, ordena por `sortBy({ clients: -1 })` (salas mais cheias primeiro) ou `{ clients: 1 }`, ignora salas `locked` ou `private`, e cria uma sala se nenhuma servir [F: colyseus2026matchmaker] [F: colyseus2026visibility]. O segundo é o `QueueRoom`, que "provides a matchmaking queue that groups players over time": por padrão "clients are grouped by rank and split into multiple groups if the rank difference becomes too high", `maxTeamSize` e `teamId` mantêm equipes juntas, `allowIncompleteGroups` permite iniciar incompleto, `maxWaitingCycles` (padrão 15) e `maxWaitingCyclesForPriority` (padrão 10) controlam quando um grupo incompleto é aceito ou um cliente vira prioritário e "can bypass compare" [F: colyseus2026queue].

### Grupos (parties)

No Nakama, o líder da party define os critérios e adiciona o grupo inteiro; "party members stay together in results", parties podem casar com outras parties e com usuários solo; com máximo 10, uma party de 5 pode completar com uma de 3 e dois solos; todos os membros recebem o callback de resultado [F: nakama2026matchmaker] [F: nakama2026parties].

### Resultado e entrada na partida

Nos dois frameworks, ser casado não é entrar: no Nakama o cliente recebe um evento com os pares e um token (relayed) ou id (autoritativo, criado no hook `matchmaker_matched`) e "must call the match join operation"; tokens "are short-lived" [F: nakama2026matchmaker]. No Colyseus, o cliente recebe uma `seat` reservation e usa `consumeSeatReservation` [F: colyseus2026queue].

### Trade-off tempo de espera versus qualidade

[I] Critérios estritos reduzem o conjunto de candidatos e elevam o tempo de espera; relaxá-los ao longo do tempo é o mecanismo padrão. A documentação do Nakama desaconselha reenviar o mesmo ticket e limites artificiais de tempo e recomenda submeter "multiple tickets with progressively more permissive queries" [F: nakama2026matchmaker]. O `QueueRoom` do Colyseus implementa o relaxamento com ciclos de espera e prioridade [F: colyseus2026queue]. Em TrueSkill, a qualidade de um pareamento é medida pela probabilidade de empate relativa a dois jogadores de habilidade igual, entre 0 e 1; se algum σ é grande, "the match quality criterion is significantly smaller than 1" [F: microsoft2026trueskill].

## Algoritmos e modelos relevantes

### Elo

Arpad Elo, *The Rating of Chessplayers, Past and Present*, 1978 [F: elo1978rating; registro bibliográfico verificado, texto não consultado]. Glickman descreve o Elo como "the first chess rating system that had probabilistic underpinnings", desenvolvido no início dos anos 1960, e observa que no Elo as mudanças de rating são balanceadas (um ganha x, o outro perde x), o que não vale no Glicko [F: glickman2016glicko]. Herbrich et al. apresentam o TrueSkill como "a generalisation of the Elo system used in Chess" [F: herbrich2006trueskill].

### Glicko

O autor, Mark Glickman, criou o Glicko em 1995 em resposta a uma deficiência do Elo: a confiabilidade do rating não é modelada. O sistema mantém rating r e RD. Jogadores não avaliados começam com r = 1500 e RD = 350; entre períodos, RD cresce por RD = min(√(RD²_old + c²), 350); após um período, r' e RD' são atualizados pelas fórmulas com q = ln(10)/400 = 0,0057565, g(RD) e E(s|r, r_j, RD_j) = 1/(1 + 10^(−g(RD_j)(r − r_j)/400)). Resultados de partidas sempre diminuem o RD; o tempo sem jogar sempre o aumenta. O autor recomenda períodos com "an average of 5-10 games per player" e um piso de RD "such as 30" para que ratings de jogadores ativos continuem a mudar. Intervalo de 95%: (r − 1,96 RD, r + 1,96 RD) [F: glickman2016glicko]. A página do autor lista também o Glicko-2, "an improvement on the original Glicko system", ambos em domínio público [F: glickman2026site]; o PDF do Glicko-2 não pôde ser lido nesta sessão (não verificado).

### TrueSkill

Herbrich, Minka e Graepel, NIPS 19 (conferência de 2006, volume publicado em 2007), pp. 569-576 [F: herbrich2006trueskill]. O resumo verificado afirma: sistema bayesiano, generalização do Elo, rastreia a incerteza, "explicitly models draws", lida com "any number of competing entities" e infere habilidades individuais a partir de resultados por equipe; a inferência é "approximate message passing on a factor graph representation" e o sistema roda em "a large-scale commercial online gaming service" sob o nome TrueSkill [F: herbrich2006trueskill]. As figuras do artigo comparam Elo e TrueSkill em dados de Halo 2 (modos Small Team, Free for All, Head to Head) [F: herbrich2006trueskill, figuras; o corpo do texto não pôde ser extraído, não verificado em detalhe]. A página do projeto na Microsoft Research documenta: novo jogador com μ = 25 e σ = 8,333 (valor exibido μ − 3σ = 0); habilidade de equipe é a soma das habilidades; tabela de jogos necessários por modo (por exemplo 12 em 1v1 e 91 em 2 equipes de 8), podendo ser "up to three times higher"; classificação por μ − k·σ com k = 3 "a common value" [F: microsoft2026trueskill]. A documentação do fornecedor afirma que o Elo "is not designed to work" para partidas multijogador [F: microsoft2026trueskill].

## Requisitos e pressupostos

- Presença: só jogadores conectados participam da fila (Nakama) [F: nakama2026matchmaker]; ver rtm.mp.presence.
- Medidas de latência ou região confiáveis por jogador, se usadas como critério; ver rtm.net.latency.
- Um rating só é útil se atualizado com resultados confiáveis; [I] em partidas por equipe ou com desistência, a atribuição de resultado individual é um problema aberto que o TrueSkill 2 tenta tratar com pontuações individuais [F: microsoft2026trueskill].
- Processamento em um único nó ativo com failover (Nakama) [F: nakama2026matchmaker].

## Vantagens e limitações

[I] Vantagens: partidas equilibradas aumentam retenção e evitam frustração; fila por critérios desacopla descoberta de salas da UI. Limitações: pools pequenos tornam critérios estritos inviáveis; o Nakama alerta que a lista de combinações possíveis "will, by necessity, include matches that are not possible to create" (exemplo: 3 jogadores, tamanho 2, 3 combinações, 1 realizável) [F: nakama2026matchmaker]; ratings com baixa incerteza param de mudar (Glicko) [F: glickman2016glicko].

## Alternativas e comparações

| Sistema | Estado por jogador | Equipes e N>2 | Empates | Incerteza explícita | Fonte |
|---|---|---|---|---|---|
| Elo | rating | não (por projeto) | sim, via 1/2 | não | [F: glickman2016glicko] [F: microsoft2026trueskill] |
| Glicko | rating, RD | 1v1 por par | sim (s = 1/2) | sim (RD) | [F: glickman2016glicko] |
| TrueSkill | μ, σ | sim | sim, modelado | sim (σ) | [F: herbrich2006trueskill] |

| Mecanismo de fila | Critério | Relaxamento | Fonte |
|---|---|---|---|
| Nakama matchmaker | query sobre properties, min/max, múltiplos | múltiplos tickets; max_intervals | [F: nakama2026matchmaker] |
| Colyseus joinOrCreate | filterBy/sortBy sobre metadata | criar sala nova | [F: colyseus2026matchmaker] |
| Colyseus QueueRoom | rank, teamId, compare() | ciclos de espera, prioridade | [F: colyseus2026queue] |

## Métricas e métodos de avaliação

[I] Tempo de espera (distribuição, não só média), taxa de tickets expirados, desvio de rating dentro da partida, latência máxima intrapartida, taxa de abandono precoce. Para ratings, a acurácia preditiva de resultados futuros: Glickman recomenda calibrar c "by optimizing predictive accuracy of future games" [F: glickman2016glicko]; o artigo do TrueSkill mede desvio da probabilidade de vitória em relação a 50% em função do número de jogos [F: herbrich2006trueskill, figura].

## Exemplo técnico independente de domínio

Diagrama em texto de uma fila com relaxamento progressivo:

```
t=0   ticket A {rating 1500±50, regiao R1, min 2, max 2, janela ±100}
t=0   ticket B {rating 1750±40, regiao R1, ...}
t=15  passagem 1: |1500-1750| > 100  -> sem match; A e B seguem no pool
t=15  cliente A envia ticket A' com janela ±300 (mantendo A)
t=30  passagem 2: A' aceita B (|250| <= 300) e B aceita A? só se a query de B admitir 1500
      -> com rev_precision=true, validação bidirecional; senão, unidirecional após rev_threshold
t=30  resultado {A, B} -> ambos recebem token/id; cada um chama join; A' e A são cancelados
```

Pseudocódigo da atualização Glicko para um jogador em um período (adaptado das fórmulas de [F: glickman2016glicko]):

```
q := ln(10)/400
g(RD) := 1 / sqrt(1 + 3 q² RD² / π²)
E(r, rj, RDj) := 1 / (1 + 10^(-g(RDj) (r - rj)/400))
d2 := 1 / (q² Σj g(RDj)² E_j (1 - E_j))
r' := r + q / (1/RD² + 1/d2) * Σj g(RDj) (sj - E_j)
RD' := sqrt(1 / (1/RD² + 1/d2))
```

## Relações com outros conceitos

Complementa rtm.mp.rooms-and-matches (destino do casamento) e rtm.mp.session-lifecycle (fase de formação). Depende de rtm.mp.presence (só conectados na fila) e de rtm.net.latency (critério de região). Implementado por rtm.fw.nakama e rtm.fw.colyseus. Relaciona-se com rtm.perf.qoe-thresholds (limiar de latência aceitável como critério).

## Lacunas e questões abertas

- Elo 1978: apenas o registro bibliográfico foi verificado; as fórmulas e o fator K não foram citados da obra original.
- Glicko-2 (volatilidade, constante τ): PDF não legível nesta sessão; não verificado.
- TrueSkill: o corpo do artigo (valores de β, ε, τ) não pôde ser extraído; os números vêm da página do projeto, que é fonte de fornecedor.
- Não há, nas fontes consultadas, estudo comparando políticas de relaxamento (múltiplos tickets versus ciclos de prioridade) em termos de tempo de espera e qualidade.
- Como combinar latência medida e rating em uma única função de custo é decisão de produto sem norma; fica como questão aberta.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nakama2026matchmaker | fornecedor | 2026-10-29 |
| nakama2026configuration | fornecedor | 2026-10-29 |
| nakama2026parties | fornecedor | 2026-10-29 |
| colyseus2026matchmaker | fornecedor | 2026-10-29 |
| colyseus2026queue | fornecedor | 2026-10-29 |
| colyseus2026visibility | fornecedor | 2026-10-29 |
| elo1978rating | academico | 2026-10-29 |
| glickman2016glicko | tecnico | 2026-10-29 |
| glickman2026site | tecnico | 2026-10-29 |
| herbrich2006trueskill | academico | 2026-10-29 |
| microsoft2026trueskill | fornecedor | 2026-10-29 |
