---
id: rtm.mp.presence
titulo: Presença (quem está online e onde)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nakama2026status, nakama2026relayed, nakama2026configuration, nakama2026parties, colyseus2026presence, colyseus2026scalability, colyseus2026transportws, colyseus2026lobby, colyseus2026reconnection, yjs2026awareness, yjs2026awarenessapi, ellis1989concurrency]
relacoes:
  - { tipo: complementa, alvo: rtm.mp.rooms-and-matches }
  - { tipo: complementa, alvo: rtm.mp.session-lifecycle }
  - { tipo: depende-de, alvo: rtm.rel.reconnection }
  - { tipo: depende-de, alvo: rtm.rt.communication-patterns }
  - { tipo: relacionado-a, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
termos: [presence, status, heartbeat, ping/pong, awareness, follow, presence event, fan-out]
---

# Presença (quem está online e onde)

## Definição e terminologia

**Presença** é a informação, mantida pelo sistema e difundida aos interessados, de quais participantes estão conectados, em que sala ou contexto estão e qual estado declaram (por exemplo "em partida", "ausente", posição do cursor). Ellis e Gibbs já apontavam que as janelas de grupo do GROVE "also indicate who is using the window" [F: ellis1989concurrency, §1].

Variações terminológicas que confundem:

- **Status** (Nakama): string livre ou JSON que um usuário publica por conexão; usuários "will not appear online to their followers" até definir um status [F: nakama2026status].
- **Presence** (Nakama): entrada de um usuário em um match, party ou canal (user_id, session_id, username), entregue em eventos de join/leave [F: nakama2026relayed].
- **Presence** (Colyseus): API de comunicação entre processos (pub/sub e chave-valor), "responsible for inter-process communication (IPC) when scaling Colyseus"; não é presença de usuário [F: colyseus2026presence].
- **Awareness** (Yjs): canal de informação efêmera "such as who is online and where their cursors are", separada do documento, "as it doesn't need to be persisted across sessions" [F: yjs2026awareness].

## Problema que resolve

[I] Clientes precisam saber quem mais está presente para renderizar listas, cursores, avatares e para decidir ações (convidar, esperar, iniciar). O servidor precisa detectar saídas implícitas (queda de rede) para liberar assentos, cancelar filas e informar os demais. Presença é, portanto, duas coisas: um detector de vida e um mecanismo de difusão.

## Fundamentos e funcionamento

### Heartbeats e timeouts

A detecção de vida se apoia em ping/pong no transporte. Nakama: `socket.ping_period_ms` padrão 15000 (deve ser menor que `pong_wait_ms`), `socket.pong_wait_ms` padrão 25000 [F: nakama2026configuration]. Colyseus: `pingInterval` padrão 3000 ms e `pingMaxRetries` padrão 2; clientes "are forcibly disconnected if they don't respond" após as tentativas [F: colyseus2026transportws]. Na camada de aplicação, o awareness do Yjs marca um cliente remoto como offline se "a client doesn't receive updates from a remote peer for 30 seconds", exigindo que cada cliente rebroadcast seu estado periodicamente; o evento `'update'` dispara "even when the awareness state does not change" justamente para servir de heartbeat [F: yjs2026awarenessapi].

[I] O intervalo de heartbeat fixa o pior caso de detecção de queda: ~25 s no Nakama padrão, ~9 s no Colyseus padrão (3 s × (2 + 1)), 30 s no awareness do Yjs. Valores menores custam tráfego e geram falsos positivos sob jitter; valores maiores atrasam a liberação de assentos. Ver rtm.net.jitter e rtm.rel.reconnection.

### Modelos de difusão

1. **Por assinatura explícita** (Nakama status): usuários "receive updates only from people they follow"; `followUsers` retorna imediatamente as presenças online dos seguidos com status visível; o follow dura só a sessão, "when the user disconnects they automatically unfollow"; atualizações chegam em `StatusPresenceEvent` com `joins` e `leaves` [F: nakama2026status].
2. **Por pertencimento a sala** (Nakama match/party): ao criar ou entrar, o cliente recebe a lista inicial; depois o servidor empurra eventos; "events are batched for efficiency, meaning any event can contain multiple joins and/or leaves" [F: nakama2026relayed]. Parties removem automaticamente quem desconecta [F: nakama2026parties].
3. **Por listagem** (Colyseus LobbyRoom): o lobby é notificado em `onCreate`, `onJoin`, `onLeave`, `onDispose` das salas com listagem ativa e envia `rooms`, `+`, `-` aos clientes [F: colyseus2026lobby]; é presença de salas, não de usuários.
4. **Por CRDT de estado** (Yjs awareness): "tiny state-based Awareness CRDT" que envia objetos JSON a todos os usuários; campos não padronizados, com convenção `cursor` e `user` [F: yjs2026awareness].

### Status por conexão

No Nakama "the status is set for each connection, and is erased when the user disconnects"; um usuário em vários dispositivos pode ter um status por dispositivo; limpar o status torna o usuário invisível e os seguidores recebem o mesmo evento de desconexão [F: nakama2026status]. [I] Isso implica que presença é por sessão, não por usuário; agregá-la por usuário (online se qualquer sessão está online) é responsabilidade da aplicação. `session.single_socket` (padrão `false`) força uma conexão por usuário, desconectando as anteriores [F: nakama2026configuration].

### Custo de difusão em grupos grandes

[I] Se cada um dos n membros de um grupo publica mudanças de presença e cada mudança é entregue aos outros n − 1, o tráfego de saída por evento é O(n) e, se todos mudam com frequência comparável, o tráfego total por unidade de tempo é O(n²). Com cursores ou posições atualizados várias vezes por segundo, isso domina o custo da sala. Mitigações documentadas ou derivadas: agrupar eventos (Nakama agrupa joins e leaves em lote [F: nakama2026relayed]); restringir destinatários por assinatura (follow) [F: nakama2026status]; limitar taxa de atualização efêmera; usar interesse espacial (rtm.sync.interest-management). [H] Para n acima de algumas centenas, a presença fina (cursores) deixa de ser viável por difusão total e exige particionamento por região do documento ou amostragem.

### Escala entre processos

No Colyseus, a presença de usuário em uma sala é local ao processo dono da sala; a coordenação entre processos usa `RedisPresence`, "required for multi-process or distributed deployments", que oferece `subscribe`/`publish`, chaves, conjuntos (`sadd`, `smembers`), hashes e listas [F: colyseus2026presence] [F: colyseus2026scalability]. [I] Presença global (por exemplo "amigos online" entre salas em processos distintos) exige esse barramento ou um serviço externo; o Nakama resolve isso no próprio servidor com o mecanismo de status/follow e, em cluster, com replicação de presenças (afirmação do fornecedor; detalhes não verificados).

## Requisitos e pressupostos

- Conexão persistente (WebSocket ou equivalente) para que o servidor possa empurrar eventos; ver rtm.proto.websocket.
- Relógio de heartbeat no servidor e no cliente, com tolerância a jitter.
- Identidade de sessão estável durante a reconexão, para que a presença não oscile (Colyseus mantém `sessionId` ao reconectar e troca `reconnectionToken` a cada conexão [F: colyseus2026reconnection]); ver rtm.rel.reconnection.

## Vantagens e limitações

[I] Vantagens: feedback social imediato; base para matchmaking (só presentes entram na fila) e para liberar recursos. Limitações: custo quadrático em grupos grandes; falsos negativos sob perda de pacotes; ambiguidade entre "saiu" e "caiu" até expirar o timeout; presença por sessão versus por usuário.

## Alternativas e comparações

| Abordagem | Quem recebe | Persistência | Custo por evento | Fonte |
|---|---|---|---|---|
| Nakama status/follow | seguidores online | só sessão | O(seguidores) | [F: nakama2026status] |
| Nakama match presence | membros da partida | só vida da partida | O(membros), em lote | [F: nakama2026relayed] |
| Colyseus LobbyRoom | clientes no lobby | não | O(clientes do lobby) | [F: colyseus2026lobby] |
| Yjs awareness | todos os pares do doc | não | O(pares), com heartbeat 30 s | [F: yjs2026awareness] [F: yjs2026awarenessapi] |

## Métricas e métodos de avaliação

[I] Tempo de detecção de queda (do último pacote ao evento de leave); taxa de falsos positivos de desconexão; bytes de presença por cliente por segundo em função de n; latência de propagação de um evento de join a todos os membros. Ver rtm.perf.metrics.

## Exemplo técnico independente de domínio

Pseudocódigo de um rastreador de presença por sala com heartbeat e difusão em lote:

```
estrutura Presenca { sessao, usuario, status, ultimo_pong }

a cada ping_period:
  para cada p em sala.presencas: enviar(p.sessao, PING)

ao receber PONG(sessao): presencas[sessao].ultimo_pong := agora

a cada verificação (ex.: ping_period):
  caidos := { p | agora - p.ultimo_pong > pong_wait }
  para cada p em caidos: marcar_saida(p, motivo = "timeout")

marcar_saida(p, motivo):
  remover presencas[p.sessao]
  enfileirar_evento(leaves += p)
  iniciar_janela_reconexao(p)        # ver rtm.rel.reconnection

ao entrar(p): presencas[p.sessao] := p; enfileirar_evento(joins += p)

a cada tick de difusão (ex.: 100 ms):
  se fila não vazia: difundir(sala, { joins, leaves }); esvaziar fila
```

Estimativa de custo para presença fina (cursores) com f atualizações por segundo por membro e payload b bytes:

```
saída do servidor por segundo ≈ n · (n − 1) · f · b
n = 10,  f = 10, b = 40  ->  ~36 KB/s
n = 100, f = 10, b = 40  ->  ~3,96 MB/s
```

## Relações com outros conceitos

Complementa rtm.mp.rooms-and-matches e rtm.mp.session-lifecycle. Depende de rtm.rel.reconnection (distinguir queda de saída) e de rtm.rt.communication-patterns (push por assinatura). Relaciona-se com rtm.proto.websocket e com rtm.sync.crdt (awareness como CRDT de estado). Implementado por rtm.fw.nakama e rtm.fw.colyseus.

## Lacunas e questões abertas

- O limite O(n²) é derivação do autor; não foi encontrada medição publicada pelos fornecedores sobre custo de presença em função de n.
- Como o Nakama replica presenças em cluster (Enterprise) não está detalhado nas páginas consultadas.
- Não há norma para semântica de status (online, ausente, ocupado); cada produto define a sua.
- O valor de 30 s do awareness do Yjs é da API; a documentação não discute o impacto de jitter nesse valor.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nakama2026status | fornecedor | 2026-10-29 |
| nakama2026relayed | fornecedor | 2026-10-29 |
| nakama2026configuration | fornecedor | 2026-10-29 |
| nakama2026parties | fornecedor | 2026-10-29 |
| colyseus2026presence | fornecedor | 2026-10-29 |
| colyseus2026scalability | fornecedor | 2026-10-29 |
| colyseus2026transportws | fornecedor | 2026-10-29 |
| colyseus2026lobby | fornecedor | 2026-10-29 |
| colyseus2026reconnection | fornecedor | 2026-10-29 |
| yjs2026awareness | fornecedor | 2026-10-29 |
| yjs2026awarenessapi | fornecedor | 2026-10-29 |
| ellis1989concurrency | academico | 2026-10-29 |
