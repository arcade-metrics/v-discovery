---
id: rtm.index
titulo: Tempo real e multiplayer
tipo: mapa
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Tempo real e multiplayer

Base de conhecimento agnóstica sobre sistemas de tempo real e multiplayer. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo e fontes prioritárias em [`00-brief.md`](00-brief.md).

## Como navegar

Comece pelo [mapa de conceitos](mapa-conceitos.md), que mostra as dependências entre documentos, e pelo [glossário](glossario.md). O [relatório](relatorio.md) registra cobertura, lacunas e próximos passos desta versão.

Leitura sugerida para quem chega sem contexto:

1. `realtime/realtime-systems.md` e `networking/latency.md`: o que "tempo real" significa aqui e por que a latência é a restrição central.
2. `protocols/comparison.md`: que transporte está disponível em cada ambiente.
3. `architectures/comparison.md`: onde fica a fonte de verdade.
4. `synchronization/state-replication.md`: as famílias de sincronização e quando cada uma se aplica.
5. `prediction-reconciliation/comparison.md`: o que é necessário só para jogos de ação.
6. `multiplayer/`: salas, presença, matchmaking e turnos, independentes de gênero.
7. `frameworks/comparison.md` e `case-studies/README.md`: como tudo isso aparece em sistemas reais.

## Pastas

| Pasta | Conteúdo | Prefixo de id |
|---|---|---|
| `realtime/` | fundamentos de tempo real e padrões de comunicação | `rtm.rt.*` |
| `networking/` | latência, jitter, perda, ordenação, banda, relógios | `rtm.net.*` |
| `protocols/` | TCP, UDP, WebSocket, WebRTC, WebTransport, QUIC, HTTP streaming | `rtm.proto.*` |
| `standards/` | índice de RFCs e especificações | `rtm.std.*` |
| `architectures/` | autoritativo, relay, P2P, lockstep, orientado a eventos | `rtm.arch.*` |
| `synchronization/` | replicação de estado, snapshot interpolation, state sync, dead reckoning, delta, interest management, CRDT, OT | `rtm.sync.*` |
| `prediction-reconciliation/` | predição, reconciliação, interpolação de entidades, lag compensation | `rtm.pred.*` |
| `multiplayer/` | salas, matchmaking, presença, turnos, ciclo de sessão | `rtm.mp.*` |
| `frameworks/` | Nakama, Colyseus, alternativas, comparação | `rtm.fw.*` |
| `reliability-security/` | reconexão, tolerância a falhas, semântica de entrega, autenticação, cheating, segurança de transporte | `rtm.rel.*`, `rtm.sec.*` |
| `performance-testing/` | métricas, limiares de QoE, carga, emulação de rede | `rtm.perf.*` |
| `case-studies/` | sistemas documentados por quem os construiu | `rtm.case.*` |

A lista completa de ids planejados está em [`_plano-ids.md`](_plano-ids.md).

## Convenções do domínio

- Fiedler e Gambetta são opinião técnica de referência (tipo `tecnico`), não norma. RFCs são normativas. Documentação de Nakama e Colyseus é de fornecedor e depende de versão.
- Limiares numéricos de latência só aparecem com `[F]` e fonte empírica. Quando a literatura diverge, o documento registra a divergência.
- Técnicas de jogos de ação (predição, lag compensation) são marcadas como tais. Jogos por turnos e colaboração têm documentos próprios e não herdam esses requisitos.
