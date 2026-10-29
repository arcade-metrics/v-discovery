---
id: rtm.brief
titulo: Brief do domínio tempo real e multiplayer
tipo: relatorio
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: tempo real e multiplayer

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Sistemas de tempo real e multiplayer: fundamentos de comunicação em tempo real; propriedades de rede (latência, jitter, perda, ordenação); protocolos de transporte e de aplicação (TCP, UDP, WebSocket, WebRTC, WebTransport, QUIC); arquiteturas (servidor autoritativo, relay, peer-to-peer, lockstep determinístico, orientada a eventos); sincronização de estado (snapshot interpolation, state synchronization, replicação); predição e reconciliação (client-side prediction, server reconciliation, lag compensation); colaboração em tempo real sem jogo rápido (salas, presença, CRDT, OT); frameworks (Nakama, Colyseus e alternativas); confiabilidade e segurança (reconexão, tolerância a falhas, autenticação, anti-cheat); testes de desempenho e simulação de rede.

Ampliação em relação ao brief original: além de jogos de ação, cobrir explicitamente jogos por turnos, colaboração e presença, que têm requisitos distintos e literatura própria (CRDT/OT, lockstep).

Fora do escopo: engines gráficas, física local, infraestrutura de nuvem genérica.

## Estrutura

- `realtime/`: fundamentos de tempo real e comunicação.
- `networking/`: latência, jitter, perda, ordenação, relógios.
- `protocols/`: TCP, UDP, WebSocket, WebRTC, WebTransport, QUIC.
- `architectures/`: autoritativo, relay, P2P, lockstep, orientado a eventos.
- `synchronization/`: snapshot interpolation, state synchronization, dead reckoning, CRDT e OT.
- `prediction-reconciliation/`: predição, reconciliação, lag compensation.
- `multiplayer/`: salas, partidas, matchmaking, presença.
- `frameworks/`: Nakama, Colyseus, alternativas.
- `reliability-security/`: reconexão, tolerância a falhas, autenticação, cheating.
- `performance-testing/`: métricas, carga, emulação de rede.
- `case-studies/`: estudos de caso técnicos documentados.
- `standards/`: índice de RFCs e especificações do domínio.

## Fontes prioritárias

1. Glenn Fiedler, Gaffer on Games: networked physics, snapshot interpolation, state synchronization, reliability over UDP.
2. Gabriel Gambetta, Fast-Paced Multiplayer (4 partes).
3. IETF: RFC 6455 (WebSocket), RFC 768 (UDP), RFC 9293 (TCP), RFC 9000 (QUIC), RFCs do WebRTC (8825 a 8835), RFC 3393 (jitter como IPDV); W3C WebRTC 1.0 e WebTransport.
4. Documentação oficial de Nakama (Heroic Labs) e Colyseus.
5. Literatura: Bernier, 2001, latency compensating methods (Valve); Bettner e Terrano, 2001, Age of Empires; Lamport, 1978, relógios lógicos; Shapiro et al., 2011, CRDT; Ellis e Gibbs, 1989, OT; Claypool e Claypool, 2006, latência e ações do jogador; Yan e Randell, 2005, taxonomia de cheating; livros Glazer e Madhav, Multiplayer Game Programming, e Steed e Oliveira, Networked Graphics.
6. Palestras técnicas de referência (GDC) com material público.

## Perguntas abertas

- Quais limiares de latência têm evidência empírica por gênero de interação (ação, turnos, colaboração)?
- Em que condições WebTransport substitui WebSocket em navegadores, e qual o estado de suporte?
- Como comparar Nakama e Colyseus em critérios verificáveis (modelo de autoridade, escala, reconexão)?
- Que métricas de qualidade de experiência existem para tempo real fora de jogos de ação?
