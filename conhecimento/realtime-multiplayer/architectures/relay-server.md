---
id: rtm.arch.relay-server
titulo: Servidor relay (relayed multiplayer)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [heroiclabs2026multiplayer, heroiclabs2026relayed, heroiclabs2026authoritative, colyseus2026relay, colyseus2026room, unity2026topologies, rfc8445, fiedler2010networking]
relacoes:
  - { tipo: alternativa-a, alvo: rtm.arch.authoritative-server }
  - { tipo: alternativa-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: alternativa-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: alternativa-a, alvo: rtm.arch.event-driven }
  - { tipo: depende-de, alvo: rtm.mp.presence }
  - { tipo: complementa, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: complementa, alvo: rtm.sync.state-replication }
  - { tipo: complementa, alvo: rtm.rel.reconnection }
  - { tipo: implementado-por, alvo: rtm.fw.nakama }
  - { tipo: implementado-por, alvo: rtm.fw.colyseus }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.proto.webrtc }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
termos: [relay server, relayed multiplayer, client-authoritative, host (cliente), opcode, TURN]
---

# Servidor relay (relayed multiplayer)

## Definição e terminologia

Arquitetura em que um servidor central recebe mensagens dos clientes de uma sessão e as repassa aos demais, sem executar a simulação nem validar o conteúdo. A autoridade sobre o estado fica nos clientes; por isso a documentação do Nakama chama o modelo de "relayed multiplayer (also known as client-authoritative)" [F: heroiclabs2026relayed]. O mesmo fornecedor resume o papel do servidor: "Nakama functions as a relay for gameplay data between clients" e "has no insight into what the data being sent is and no oversight into whether the data is correct" [F: heroiclabs2026multiplayer].

Nomes alternativos: *relay room* (Colyseus) [F: colyseus2026relay], *client-authoritative* [F: heroiclabs2026relayed]. Na documentação da Unity, a topologia *distributed authority* tem componente semelhante: um serviço central leve que guarda pouco estado e roteia tráfego, sem servidor que simule o jogo [F: unity2026topologies].

O que não é: não é um servidor autoritativo (não há validação de regras no servidor) [F: heroiclabs2026relayed]; não é P2P puro (há um nó intermediário fixo que todos alcançam, o que elimina o problema de NAT traversal entre pares) [I]. No plano de transporte, um servidor TURN também é um relay de pacotes, "forwarding traffic between L and R" [F: rfc8445, §2], mas opera abaixo da aplicação; este documento trata do relay de aplicação.

## Problema que resolve

[I] O relay resolve três problemas práticos de P2P sem assumir o custo de um servidor de simulação:

1. **Conectividade**: todos os clientes abrem conexão de saída para um endereço público; nenhum par precisa aceitar conexões entrantes.
2. **Descoberta e pertencimento**: o servidor mantém a lista de participantes. A documentação do Nakama afirma que as únicas informações de partida mantidas pelo servidor são o match ID e a lista de presences [F: heroiclabs2026relayed].
3. **Custo**: o servidor não executa lógica de jogo, logo o custo por sessão é o de encaminhar mensagens. A documentação da Unity afirma, para a topologia distribuída, que ela é mais barata "since they lack a dedicated central server" [F: unity2026topologies].

Segundo o fornecedor Nakama, o modelo é adequado para jogos "where authoritative control on the server is not important (e.g. cheating is a non-factor)", como 1v1 simples ou cooperativo [F: heroiclabs2026relayed].

## Fundamentos e funcionamento

Fluxo de mensagens [I, consolidado de heroiclabs2026relayed e colyseus2026relay]:

```
cliente A ──msg(opcode, payload)──▶ relay ──msg(A, opcode, payload)──▶ cliente B
                                          └──msg(A, opcode, payload)──▶ cliente C
cliente B ──msg(...)───────────────▶ relay ──▶ A, C
relay mantém: id da sessão, lista de presences, conexões; não interpreta payload
```

Características documentadas pelos fornecedores:

- **Encaminhamento opaco.** Nakama repassa dados "regardless of message size or content" e "without inspection"; "there is no cheat detection, error correction, or other such functionality available" [F: heroiclabs2026relayed]. A RelayRoom do Colyseus tem "Minimal backend state (no authoritative validation)" [F: colyseus2026relay].
- **Destinatários.** Em Nakama, por padrão a mensagem vai a todos os demais participantes, com opção de direcionar a um subconjunto de presences [F: heroiclabs2026relayed]. Em Colyseus, "Messages are only sent to other connected clients, never the current one" [F: colyseus2026relay].
- **Tipo de mensagem.** Nakama usa um *op code* numérico que identifica o tipo de comando; Colyseus usa mensagens nomeadas (`relay.send("fire", {...})`) [F: heroiclabs2026relayed; colyseus2026relay].
- **Ordem.** Nakama afirma que as mensagens são transmitidas "in the order received", não necessariamente na ordem de envio [F: heroiclabs2026relayed].
- **Ciclo de vida.** Em Nakama as partidas relayed existem só na memória do servidor, sem persistência, e terminam quando o último participante sai [F: heroiclabs2026relayed]; contraste com partidas autoritativas, que "do not end even if all players have left" [F: heroiclabs2026authoritative]. Em Colyseus, `autoDispose` padrão `true` descarta a sala quando o último cliente desconecta [F: colyseus2026room].
- **Acesso.** Em Nakama, "if a user has the match ID then they are able to join"; não há senha, e dois criadores com o mesmo `name` "will end up with identical match IDs" [F: heroiclabs2026relayed].

### Host entre os clientes

Como o servidor não simula, um cliente costuma assumir o papel de **host** lógico. A documentação do Nakama afirma que um cliente atua como host, escolhido pelos próprios clientes, e que ele "will reconcile state changes between peers"; sugere escolher o host de forma determinística (por exemplo, a presence com menor session ID) e recalcular quando ele sai [F: heroiclabs2026relayed]. [I] Esse arranjo é, na prática, um servidor autoritativo hospedado em um cliente, com o relay fazendo o transporte; herda as limitações do *listen server* (ver rtm.arch.authoritative-server) e exige migração de host.

Alternativa sem host: cada cliente é autoridade sobre seus próprios objetos e os demais replicam (modelo próximo da *distributed authority* da Unity) [F: unity2026topologies]; ou todos os clientes executam lockstep determinístico e o relay apenas transporta entradas (ver rtm.arch.deterministic-lockstep) [I].

## Algoritmos e modelos relevantes

- Eleição determinística de host por ordenação das presences [F: heroiclabs2026relayed].
- Replicação de estado por dono (*owner-authoritative*) com reconciliação pelo host (rtm.sync.state-replication).
- Lockstep sobre relay: o relay transporta entradas e os clientes simulam (rtm.arch.deterministic-lockstep).
- Reconexão com janela de tolerância: Colyseus limita `allowReconnectionTime` a 40 segundos ("values above 40 are clamped to 40") [F: colyseus2026relay].

## Requisitos e pressupostos

- Os clientes precisam ser confiáveis entre si, pois nenhum componente valida regras [F: heroiclabs2026relayed].
- O protocolo de aplicação (opcodes, formato, ordem, idempotência) é inteiramente definido pelo cliente; o relay não oferece correção de erros [F: heroiclabs2026relayed].
- Tamanho e frequência: Nakama recomenda manter o conteúdo dentro de um MTU de 1500 bytes e preferir menos mensagens maiores (um envio de 1000 bytes por segundo é melhor que cinco de 200 bytes) [F: heroiclabs2026relayed].
- Presença: o fornecedor recomenda registrar o listener de presence antes de criar ou entrar na partida, pois eventos de entrada e saída podem chegar em lotes e a lista inicial pode não estar completa [F: heroiclabs2026relayed]. Daí a dependência de rtm.mp.presence.
- Saídas voluntárias ou por queda precisam ser tratadas na lógica do jogo [F: heroiclabs2026relayed].

## Vantagens e limitações

Vantagens:
- Custo por sessão baixo e lógica de servidor mínima; adequado a protótipos e a casos em que a validação fica no cliente [F: colyseus2026relay].
- Elimina NAT traversal entre pares e a descoberta direta (comparar com rtm.arch.peer-to-peer) [I].
- Latência: um salto cliente→relay→cliente, sem tempo de simulação no servidor [I].

Limitações:
- Sem resistência a trapaça: o próprio fornecedor condiciona o uso a cenários em que "cheating is a non-factor" [F: heroiclabs2026relayed]. A Unity afirma que a topologia distribuída é mais vulnerável a trapaças [F: unity2026topologies].
- Sem estado durável no servidor: sem persistência da partida e sem avanço do mundo quando todos saem [F: heroiclabs2026relayed].
- Ordem e entrega são as do transporte; ordenação entre remetentes não é garantida pelo relay [F: heroiclabs2026relayed].
- Com host em cliente, a sessão depende da conexão e do hardware do host, e a troca de host perde o estado não replicado (ver host migration em rtm.arch.authoritative-server) [I].

## Alternativas e comparações

| Critério | Relay | Autoritativo | P2P |
|---|---|---|---|
| Quem simula | clientes (ou um host) | servidor | todos os pares |
| Validação no servidor | nenhuma [F: heroiclabs2026relayed] | total [F: heroiclabs2026multiplayer] | nenhuma |
| NAT traversal entre pares | não necessário | não necessário | necessário (ICE) [F: rfc8445] |
| Estado após todos saírem | perdido [F: heroiclabs2026relayed] | mantido [F: heroiclabs2026authoritative] | perdido |

Tabela completa em rtm.arch.comparison.

## Métricas e métodos de avaliação

- Mensagens por segundo por sessão e bytes por mensagem em relação ao MTU [F: heroiclabs2026relayed].
- Latência de encaminhamento (tempo entre receber e repassar) e RTT cliente-relay-cliente (rtm.perf.metrics).
- Taxa de eventos de presence por sessão e tempo até recomputar o host após saída [I].
- Taxa de reconexões bem-sucedidas dentro da janela permitida [F: colyseus2026relay].

## Exemplo técnico independente de domínio

Pseudocódigo do relay e da eleição de host nos clientes [I]:

```
# servidor relay
ao_receber(sessao, remetente, msg):
  destinos = msg.destinos ou (sessao.presences − {remetente})
  para cada d em destinos:
    enviar(d, { de: remetente, opcode: msg.opcode, payload: msg.payload })
  # nenhuma leitura de payload

# cliente
ao_mudar_presences(presences):
  host = min(presences, chave = session_id)      # determinístico
  se host == eu: assumir_autoridade()
  senao: seguir(host)
```

## Relações com outros conceitos

Alternativa às demais arquiteturas; complementa rtm.arch.deterministic-lockstep (o relay é um transporte natural para troca de entradas) e rtm.sync.state-replication (replicação por dono sobre o relay). Depende de rtm.mp.presence para pertencimento e eleição de host. Implementado por Nakama (modo *relayed*) [F: heroiclabs2026relayed] e por Colyseus (`RelayRoom`) [F: colyseus2026relay]. Relaciona-se com rtm.sec.cheating (limite de confiança) e com rtm.proto.webrtc (TURN como relay de transporte, distinto do relay de aplicação) [F: rfc8445].

## Lacunas e questões abertas

- Os fornecedores consultados não publicam limites numéricos de participantes ou de mensagens por segundo para o modo relay; Nakama afirma não haver limite explícito além de design, rede e hardware [F: heroiclabs2026relayed].
- Não foi localizada fonte acadêmica que caracterize formalmente o modelo relay como distinto de cliente-servidor e P2P; a distinção aqui é de documentação de fornecedor [I].
- Semântica de entrega (at-most-once, at-least-once) do relay em cada framework não está detalhada nas páginas consultadas; verificar em rtm.rel.delivery-semantics.
- A página de visão geral da Unity sobre *distributed authority* foi consultada, mas o serviço de relay da Unity não foi aberto; não citar seus limites.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| heroiclabs2026multiplayer | fornecedor | 2026-10-29 |
| heroiclabs2026relayed | fornecedor | 2026-10-29 |
| heroiclabs2026authoritative | fornecedor | 2026-10-29 |
| colyseus2026relay | fornecedor | 2026-10-29 |
| colyseus2026room | fornecedor | 2026-10-29 |
| unity2026topologies | fornecedor | 2026-10-29 |
| rfc8445 | normativo | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
