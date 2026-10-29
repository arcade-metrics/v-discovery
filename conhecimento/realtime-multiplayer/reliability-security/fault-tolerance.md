---
id: rtm.rel.fault-tolerance
titulo: Tolerância a falhas do servidor de sessão
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brewer2012cap, abadi2012pacelc, abadi2010pacelc, principlesofchaos2019, heroiclabs2026authoritative, heroiclabs2026multiplayer, colyseus2026room, kafka2026semantics, brooker2019timeouts]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: depende-de, alvo: rtm.sync.state-replication }
  - { tipo: complementa, alvo: rtm.rel.reconnection }
  - { tipo: complementa, alvo: rtm.rel.delivery-semantics }
  - { tipo: complementa, alvo: rtm.mp.session-lifecycle }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [estado em memória, checkpoint, host migration, replicação, CAP, PACELC, graceful degradation, chaos engineering, steady state]
---

# Tolerância a falhas do servidor de sessão

## Definição e terminologia

Tolerância a falhas, aqui, é a capacidade de um sistema de tempo real continuar a prestar serviço (ou degradar de forma controlada) quando o processo ou nó que hospeda uma sessão (sala, partida, documento colaborativo) falha, fica isolado da rede ou precisa ser desligado. O foco é a *sessão com estado em memória*, que é o caso comum em servidores de jogo e de colaboração, e não a infraestrutura de nuvem genérica (fora de escopo do domínio).

Termos:

- **Estado em memória vs persistido**: estado da sessão mantido só no processo (rápido, perdido na falha) ou gravado em armazenamento durável (sobrevive, mas custa latência).
- **Checkpoint**: cópia periódica do estado em memória para armazenamento durável, a partir da qual a sessão pode ser reconstruída.
- **Host migration**: transferência do papel de "autoridade" ou "anfitrião" de uma sessão para outro nó ou par quando o atual falha.
- **Replicação**: manutenção de cópias do estado em mais de um nó, síncrona ou assíncrona.
- **Graceful degradation**: redução deliberada de funcionalidade (em vez de falha total) sob condição adversa.
- **Chaos engineering**: "the discipline of experimenting on a system in order to build confidence" na sua capacidade de suportar condições turbulentas [F: principlesofchaos2019].

## Problema que resolve

Uma sessão de tempo real é, quase sempre, um objeto com estado vivo num único processo: o tick loop, as presenças, o estado do mundo. Esse desenho dá latência mínima e simplicidade, mas cria um ponto único de falha por sessão. Quando o processo morre, todos os clientes daquela sessão caem ao mesmo tempo; quando o nó é isolado da rede, ele pode continuar a executar sem que ninguém o alcance. A pergunta de projeto é: o que se perde, por quanto tempo e para quem, e quanto se paga em latência e complexidade para perder menos.

## Fundamentos e funcionamento

### O que os frameworks assumem

A documentação do Nakama é explícita: "Nakama exposes an in-memory region for authoritative matches to use for the duration of the match to store their state" [F: heroiclabs2026authoritative]; partidas relayed "are kept in-memory and exist on the server until their last participant has left" [F: heroiclabs2026multiplayer]. Para desligamento controlado, a função `match_terminate` "runs when the server is shutting down, with a grace period", e o exemplo documentado transmite um novo id de partida para que os jogadores migrem (recurso marcado como Nakama Enterprise) [F: heroiclabs2026authoritative]. Para partidas por turnos "passivas", a documentação descreve o padrão checkpoint: "When all participants are offline, at the end of the match loop you write the match state to the database" antes de terminar a partida [F: heroiclabs2026multiplayer].

No Colyseus, a sala tem `autoDispose` padrão `true` ("Automatically dispose the room when last client disconnects") e `onDispose` no ciclo de vida [F: colyseus2026room]; a página consultada não descreve replicação de estado de sala entre processos. [I] Em ambos os frameworks, a resposta padrão a falha de processo é perda da sessão em memória; sobrevivência é responsabilidade do código de aplicação via checkpoint.

### Estratégias

1. **Aceitar a perda, reconectar rápido.** Sessões curtas e de baixo valor (uma rodada de poucos minutos) podem simplesmente terminar; o investimento vai para reconexão e matchmaking rápidos (ver `rtm.rel.reconnection`). Este é o padrão implícito dos frameworks consultados [I].
2. **Checkpoint periódico.** O estado é serializado para um armazenamento durável a cada N ticks ou a cada evento significativo (fim de turno, fim de rodada). Após falha, um novo processo carrega o último checkpoint e os clientes reconectam. Perde-se o que aconteceu desde o checkpoint. Funciona bem para turnos e colaboração, onde eventos são discretos e o custo de perder "o último lance" é tolerável se o cliente puder reenviá-lo (idempotência, ver `rtm.rel.delivery-semantics`) [I].
3. **Log de eventos + reexecução.** Em vez de (ou além de) checkpoints, registra-se cada entrada aceita num log durável; a reconstrução reexecuta o log a partir do último checkpoint. Exige simulação determinística (ver `rtm.arch.deterministic-lockstep`). A documentação do Kafka ilustra o mesmo princípio em outro contexto: o consumidor pode "read the messages, process the messages, and finally save its position", obtendo at-least-once e reprocessamento idempotente após falha [F: kafka2026semantics].
4. **Replicação ativa.** Dois ou mais nós recebem as mesmas entradas e mantêm o mesmo estado; um é primário. Custa latência (replicação síncrona) ou consistência (assíncrona), como discute PACELC abaixo. Pouco comum em servidores de jogo de ação pelo custo por tick [H].
5. **Host migration (P2P e relay).** Quando o anfitrião é um par, outro par assume. Exige que todos tenham estado suficiente para continuar e um protocolo de eleição; não encontrada documentação primária verificável nesta sessão, registrado em Lacunas.

### CAP e PACELC como vocabulário

Brewer (2012) reafirma que "any networked shared-data system can have at most two of three desirable properties" (consistência, disponibilidade, tolerância a partições), mas argumenta que "The '2 of 3' formulation was always misleading because it tended to oversimplify the tensions among properties" e que "Because partitions are rare, CAP should allow perfect C and A most of the time" [F: brewer2012cap]. Sua recomendação operacional é tratar a partição em três passos: detectar, "enter an explicit partition mode that can limit some operations" e recuperar, restaurando consistência e compensando erros [F: brewer2012cap].

Abadi (2012) sustenta que "CAP only posits limitations in the face of certain types of failures, and does not constrain any system capabilities during normal operation", e que o compromisso entre consistência e latência "arguably has been more influential" no projeto de sistemas; daí a formulação PACELC: se há partição (P), escolhe-se entre disponibilidade (A) e consistência (C); senão (E), entre latência (L) e consistência (C) [F: abadi2012pacelc]. O artigo classifica Dynamo, Cassandra e Riak como PA/EL, sistemas ACID tradicionais como PC/EC e PNUTS como PC/EL [F: abadi2012pacelc]. A formulação apareceu antes no blog do autor (2010): "To me, CAP should really be PACELC" [F: abadi2010pacelc].

[I] Para sessões de tempo real a leitura é direta: um servidor de partida com estado em memória é PA/EL por construção (prefere responder já, com o estado local, a coordenar); um documento colaborativo com CRDT (ver `rtm.sync.crdt`) é PA/EL com convergência garantida; um jogo por turnos com persistência síncrona por lance é PC/EC e paga em latência por lance. A escolha deve ser explícita e por operação, como Brewer sugere.

### Graceful degradation

Padrões de degradação controlada em tempo real [I]: reduzir tick rate ou frequência de snapshots sob sobrecarga; suspender funções não essenciais (chat, presença detalhada) antes do núcleo; marcar jogadores como "desconectados" em vez de removê-los (ver `rtm.rel.reconnection`); entrar em "modo partição" com operações limitadas, no vocabulário de Brewer [F: brewer2012cap]. Brooker acrescenta cuidados de cliente: timeouts em toda chamada remota, retentativa num único ponto da pilha e com orçamento (token bucket), porque retentativas "spend more server capacity" e podem transformar uma falha parcial em indisponibilidade [F: brooker2019timeouts].

### Chaos engineering

Os Principles of Chaos Engineering propõem definir o *steady state* como saída mensurável (vazão, taxa de erro, percentis de latência), formular hipótese de que ele se mantém no grupo experimental, introduzir eventos reais ("failing servers or severed network connections") e tentar refutar a hipótese; os princípios avançados incluem "Run experiments in production", "Automate experiments to run continuously" e "Minimize blast radius" [F: principlesofchaos2019]. [I] Para sessões de tempo real, os experimentos naturais são: matar o processo de uma sala com clientes conectados, isolar um nó da rede, injetar latência entre servidor e banco de checkpoint. Ferramentas de injeção em rede estão em `rtm.perf.network-emulation`.

## Requisitos e pressupostos

- Para checkpoint e reexecução, o estado precisa ser serializável e a simulação, idealmente, determinística.
- Clientes precisam de reconexão com retomada (ver `rtm.rel.reconnection`); tolerância do servidor sem retomada do cliente é inútil.
- Entradas precisam ser idempotentes ou deduplicáveis para que reenvio após falha não duplique efeitos (ver `rtm.rel.delivery-semantics`).
- A autoridade sobre o estado deve ser única em cada instante; replicação sem liderança clara cria estados divergentes [I].

## Vantagens e limitações

| Estratégia | Perda na falha | Custo em latência normal | Complexidade |
|---|---|---|---|
| Aceitar perda | sessão inteira | nenhum | baixa |
| Checkpoint periódico | desde o último checkpoint | baixa (assíncrono) | média |
| Log + reexecução | nada (até a última entrada durável) | por entrada, se síncrono | alta (determinismo) |
| Replicação ativa | nada ou quase | por tick/entrada | alta |

[I] As linhas refletem o eixo E-L/C de PACELC: quanto menos se perde, mais se paga em latência em operação normal.

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`: tempo de recuperação da sessão após falha (do kill ao primeiro tick servido), fração de sessões recuperadas, idade do último checkpoint no instante da falha, tamanho do checkpoint, latência adicional por tick introduzida pela persistência, e, em experimentos de caos, diferença de steady state entre grupo de controle e experimental [F: principlesofchaos2019].

## Exemplo técnico independente de domínio

```text
# Sessão autoritativa com checkpoint e reexecução de log
state = load_checkpoint(session_id) or initial_state()
log   = durable_log(session_id)
for entry in log.after(state.last_seq): state = apply(state, entry)   # reexecução

every tick:
    for input in inbox:                       # inputs validados e deduplicados
        if input.seq <= state.last_seq_for(input.client): continue
        log.append(input)                     # durável antes de aplicar (PC) ou depois (EL)
        state = apply(state, input)
    broadcast_snapshot(state)
    if tick % CHECKPOINT_EVERY == 0: save_checkpoint(state)   # assíncrono

on_partition_detected():                      # Brewer: modo partição explícito
    mode = PARTITION ; disable(operations_requiring_coordination)
```

## Relações com outros conceitos

Depende da arquitetura autoritativa (`rtm.arch.authoritative-server`) e da replicação de estado (`rtm.sync.state-replication`). Complementa `rtm.rel.reconnection` (lado do cliente), `rtm.rel.delivery-semantics` (idempotência para reexecução) e `rtm.mp.session-lifecycle`. Relaciona-se a `rtm.arch.peer-to-peer` (host migration) e `rtm.sync.crdt` (convergência sem coordenação). Implementado parcialmente por `rtm.fw.nakama` (checkpoint em turnos passivos, migração no desligamento) e `rtm.fw.colyseus` (ciclo de vida da sala). Avaliado por `rtm.perf.metrics`.

## Lacunas e questões abertas

- Host migration em P2P: não foi localizada nesta sessão fonte primária verificável (documentação de engine ou artigo com DOI); o tema fica como [H] até verificação.
- A documentação do Colyseus consultada não trata de sobrevivência de estado de sala a falha de processo; não verificado se há mecanismo oficial.
- Não há, nas fontes consultadas, medições de custo de latência por tick de checkpoint síncrono em servidores de jogo; os números precisam vir de `rtm.perf.load-testing`.
- O livro "Designing Data-Intensive Applications" (Kleppmann) é referência usual para replicação e consistência, mas seu conteúdo não foi consultado nesta sessão; não citado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brewer2012cap | academico | 2026-10-29 |
| abadi2012pacelc | academico | 2026-10-29 |
| abadi2010pacelc | tecnico | 2026-10-29 |
| principlesofchaos2019 | tecnico | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| heroiclabs2026multiplayer | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| kafka2026semantics | fornecedor | 2026-10-29 |
| brooker2019timeouts | tecnico | 2026-10-29 |
