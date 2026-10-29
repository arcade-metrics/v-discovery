---
id: rtm.mp.turn-based
titulo: Jogos por turnos, síncronos e assíncronos
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nakama2026authoritative, nakama2026projecttemplate, nakama2026configuration, nakama2026relayed, colyseus2026reconnection, colyseus2026room, ellis1989concurrency]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: complementa, alvo: rtm.mp.session-lifecycle }
  - { tipo: complementa, alvo: rtm.mp.rooms-and-matches }
  - { tipo: alternativa-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
termos: [turn-based, asynchronous multiplayer, turn timeout, forfeit, move validation, state machine, op code]
---

# Jogos por turnos, síncronos e assíncronos

## Definição e terminologia

Um jogo **por turnos** é aquele em que a ação é serializada: em cada instante, um subconjunto definido de participantes (em geral um) tem o direito de agir, e o estado só muda quando uma jogada é aceita. Distinguem-se dois regimes:

- **Síncrono**: todos os participantes estão conectados durante a partida e os turnos duram segundos ou minutos. A documentação do Nakama descreve este caso como jogadores conectados "playing a quick turn-based match" [F: nakama2026authoritative].
- **Assíncrono**: a partida dura horas ou dias; os participantes raramente estão conectados ao mesmo tempo; cada jogada é persistida e o adversário é notificado. Ellis e Gibbs chamavam o análogo em groupware de "non-real-time groupware", com sessões "days or even weeks in length" nas quais "real-time notification may not be necessary" [F: ellis1989concurrency, §1].

O que não é: lockstep determinístico (rtm.arch.deterministic-lockstep) também serializa a simulação em passos, mas todos agem a cada passo e o estado avança continuamente; não é jogo por turnos no sentido aqui usado.

## Problema que resolve

[I] Jogos de ação precisam de predição, interpolação e compensação de latência porque o estado muda continuamente e a percepção de atraso degrada a experiência. Jogos por turnos removem esse problema: a latência de uma jogada só precisa ser menor que a tolerância humana para "esperar a vez" (segundos), não que o intervalo entre quadros. Em troca, aparecem requisitos distintos: validação rigorosa de cada jogada, controle de tempo por turno, persistência do estado entre conexões e notificação de quem não está presente.

## Fundamentos e funcionamento

### Requisitos que mudam em relação a jogos de ação

| Requisito | Jogo de ação | Jogo por turnos | Observação |
|---|---|---|---|
| Predição no cliente | necessária | desnecessária | [I] a jogada espera o aceite do servidor |
| Autoridade | servidor com reconciliação | servidor simples, sequencial | [I] uma jogada por vez; sem corrida |
| Taxa de simulação | 10-60 Hz | baixa (o template do Nakama usa `tickRate = 5` [F: nakama2026projecttemplate]) | o tick só serve a temporizadores |
| Persistência da partida | opcional | obrigatória no assíncrono | [I] o estado deve sobreviver a processos |
| Reconexão | janela curta | janela longa (Colyseus sugere ~30 s para jogos rápidos e ~5 min para turnos [F: colyseus2026reconnection]) | ver rtm.rel.reconnection |
| Notificação fora de sessão | não | sim no assíncrono | [I] push, e-mail ou inbox |

### Modelagem como máquina de estados

[I] A partida é uma máquina de estados finita: `aguardando_jogadores → em_turno(j) → validando → em_turno(j') ... → encerrada(resultado)`. Cada jogada é uma transição com guarda (é a vez de j? a jogada é legal?) e efeito (novo estado, próximo jogador, prazo). O template oficial do Nakama materializa isso com campos `board`, `marks` (user_id → marca), `mark` (de quem é a vez), `deadlineRemainingTicks`, `winner`, `nextGameRemainingTicks`, `playing` e `emptyTicks` [F: nakama2026projecttemplate].

### Validação de jogada no servidor

No template do Nakama, no `MatchLoop`: se `s.mark != mark`, a jogada é rejeitada ("It is not this player's turn"); se o payload não desserializa, é rejeitada; se `msg.Position < 0 || msg.Position > 8` ou a célula já está ocupada, é rejeitada ("Client sent a position outside the board, or one that has already been played"); rejeições são enviadas "only to the offending user" com `OPCODE_REJECTED` [F: nakama2026projecttemplate]. [I] Esta é a forma mínima de autoridade: o cliente propõe, o servidor decide, e o estado novo é difundido com um op code de atualização. Ver rtm.sec.cheating para a motivação.

### Timeouts de turno e forfeit

No template: cada tick decrementa `deadlineRemainingTicks`; ao chegar a zero, `playing` vira falso, "the player who timed out forfeits" e o vencedor é a marca oposta; o prazo é de 10 s (`turnTimeFastSec`) se o label tem `Fast = 1`, senão 20 s (`turnTimeNormalSec`); entre jogos há `delayBetweenGamesSec = 5` [F: nakama2026projecttemplate]. [I] No regime assíncrono o prazo é de horas ou dias, o relógio é de parede (não ticks) e o vencimento deve ser verificado também quando o adversário consulta a partida, não só por um laço ativo.

### Encerramento e partidas vazias

O template encerra a partida ociosa quando `emptyTicks >= maxEmptySec * tickRate` (30 s × 5 = 150 ticks), registrando "closing idle match" e retornando `nil` [F: nakama2026projecttemplate]; `match.max_empty_sec` padrão 0 significa sem máximo global [F: nakama2026configuration]. [I] No assíncrono, uma partida sem conexões não deve ser encerrada; deve ser descarregada da memória e recarregada da persistência quando alguém voltar. Isso implica que o modelo "match vive em memória em um nó" (Nakama autoritativo [F: nakama2026authoritative]; Colyseus `autoDispose` padrão `true` [F: colyseus2026room]) precisa de um invólucro de carga sob demanda.

### Mensagens

Op codes distinguem o propósito de cada mensagem antes de decodificar o payload [F: nakama2026relayed]. O template usa `OPCODE_MOVE`, `OPCODE_UPDATE`, `OPCODE_DONE`, `OPCODE_START`, `OPCODE_REJECTED`, `OPCODE_OPPONENT_LEFT`, `OPCODE_INVITE_AI` [F: nakama2026projecttemplate]. [I] Para turnos, a entrega deve ser confiável e ordenada por partida; ver rtm.rel.delivery-semantics.

## Requisitos e pressupostos

- Autoridade no servidor sobre regras e estado; ver rtm.arch.authoritative-server.
- Identidade estável do jogador entre sessões (reconexão retorna ao mesmo assento: o template readmite um usuário cuja presença está `nil` [F: nakama2026projecttemplate]).
- No assíncrono: armazenamento durável do estado e do histórico de jogadas; canal de notificação fora da conexão; idempotência de jogadas reenviadas.
- Relógio de parede confiável no servidor para prazos longos; ver rtm.net.clock-synchronization.

## Vantagens e limitações

[I] Vantagens: tolerância alta a latência e jitter; validação simples e auditável; baixo custo de CPU por partida; pode rodar sobre HTTP com polling no assíncrono. Limitações: tempo de espera percebido depende do adversário; abandono exige regra de forfeit; partidas longas acumulam estado a persistir; o modelo em memória dos frameworks de tempo real precisa de adaptação para o assíncrono.

## Alternativas e comparações

| Regime | Conexão | Prazo de turno | Estado | Notificação | Fonte |
|---|---|---|---|---|---|
| Síncrono (match em memória) | persistente | 10-20 s no template | memória do nó | eventos da partida | [F: nakama2026projecttemplate] |
| Assíncrono (persistido) | intermitente | horas a dias | banco de dados | push/inbox | [I] |
| Lockstep determinístico | persistente | por passo fixo | replicado | n/a | ver rtm.arch.deterministic-lockstep |

## Métricas e métodos de avaliação

[I] Latência da jogada (envio → aceite → difusão); taxa de jogadas rejeitadas por tipo (fora de turno, ilegal, malformada); taxa de forfeit por timeout; tempo entre turnos no assíncrono; partidas abandonadas. Ver rtm.perf.metrics.

## Exemplo técnico independente de domínio

Máquina de estados de uma partida por turnos para dois jogadores, independente do jogo:

```
estados: AGUARDANDO, TURNO(j), ENCERRADA(resultado)
estado inicial: AGUARDANDO

AGUARDANDO --entrou(p) e |jogadores| = 2--> TURNO(j0); prazo := agora + T
TURNO(j) --jogada(p, m) [p = j e legal(m, estado)]--> aplicar(m); se terminal: ENCERRADA(resultado) senão TURNO(outro(j)); prazo := agora + T
TURNO(j) --jogada(p, m) [p ≠ j ou não legal(m)]--> TURNO(j); responder(p, REJEITADA)
TURNO(j) --tempo ≥ prazo--> ENCERRADA(forfeit de j)
TURNO(j) --saiu(p, motivo = desconexão)--> TURNO(j); abrir janela de reconexão(p)
TURNO(j) --janela de reconexão(p) expirou--> ENCERRADA(forfeit de p)
TURNO(j) --saiu(p, motivo = voluntário)--> ENCERRADA(forfeit de p)
ENCERRADA --persistir(resultado); notificar(ambos)--> fim
```

Variante assíncrona do tratamento de prazo (relógio de parede, verificação preguiçosa):

```
ao carregar partida(id) de armazenamento:
  se estado = TURNO(j) e agora ≥ prazo: aplicar forfeit(j); persistir; notificar
ao receber jogada(p, m, id, jogada_seq):
  se jogada_seq já aplicada: responder(OK idempotente)
  carregar partida(id); validar; aplicar; persistir; notificar(outro(p))
```

## Relações com outros conceitos

Depende de rtm.arch.authoritative-server. Complementa rtm.mp.session-lifecycle (fases, resultado, persistência) e rtm.mp.rooms-and-matches. É alternativa a rtm.pred.client-side-prediction no sentido de que dispensa predição. Relaciona-se com rtm.arch.deterministic-lockstep, rtm.rel.reconnection, rtm.rel.delivery-semantics e rtm.sec.cheating. Implementado por rtm.fw.nakama e rtm.fw.colyseus.

## Lacunas e questões abertas

- Não foi encontrada documentação oficial do Nakama ou do Colyseus dedicada ao regime assíncrono (partidas de dias); o tratamento acima é derivação do autor.
- O tutorial XOXO do Nakama só mostra o cliente; a lógica de servidor citada vem do template no GitHub (fonte técnica, não documentação).
- Falta evidência sobre tolerância humana a atraso de aceite de jogada em jogos por turnos; ver rtm.perf.qoe-thresholds.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nakama2026authoritative | fornecedor | 2026-10-29 |
| nakama2026projecttemplate | tecnico | 2026-10-29 |
| nakama2026configuration | fornecedor | 2026-10-29 |
| nakama2026relayed | fornecedor | 2026-10-29 |
| colyseus2026reconnection | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| ellis1989concurrency | academico | 2026-10-29 |
