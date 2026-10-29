---
id: rtm.arch.peer-to-peer
titulo: Peer-to-peer (P2P) sem servidor de simulação
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [fiedler2010networking, bettner2001archers, knutsson2004p2p, rfc8445, rfc8825, photon2026hostmigration, unity2026topologies, ggpo2019readme, ggpo2019devguide, heroiclabs2026relayed]
relacoes:
  - { tipo: alternativa-a, alvo: rtm.arch.authoritative-server }
  - { tipo: alternativa-a, alvo: rtm.arch.relay-server }
  - { tipo: alternativa-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: alternativa-a, alvo: rtm.arch.event-driven }
  - { tipo: depende-de, alvo: rtm.proto.webrtc }
  - { tipo: complementa, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: complementa, alvo: rtm.sync.interest-management }
  - { tipo: complementa, alvo: rtm.sync.dead-reckoning }
  - { tipo: complementa, alvo: rtm.rel.fault-tolerance }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
termos: [peer-to-peer, full mesh, host migration, NAT traversal, ICE, STUN, TURN, overlay, locality of interest, coordinator]
---

# Peer-to-peer (P2P) sem servidor de simulação

## Definição e terminologia

Arquitetura em que os participantes trocam mensagens diretamente entre si e mantêm o estado da sessão sem um servidor que simule o jogo. Fiedler descreve o caso clássico, o *peer-to-peer lockstep* de Doom, Command and Conquer, Age of Empires e StarCraft: cada máquina executa o mesmo jogo e troca comandos processados em turnos a partir de um estado inicial comum [F: fiedler2010networking]. Bettner afirma que "The Genie engine supported a peer-to-peer network topology" [F: bettner2001archers]. Knutsson et al. generalizam para mundos massivos: os jogadores formam um *overlay* em que "many of the game functions are implemented", contribuindo memória, CPU e banda para manter o estado compartilhado [F: knutsson2004p2p].

Modelos [I]:
- **Full mesh**: cada par mantém conexão com todos os outros; é o modelo do lockstep clássico e de SDKs de rollback como GGPO, cujo exemplo conecta cada jogador por `local` ou IP:porta remota [F: ggpo2019readme].
- **Host entre pares com migração**: um par é autoridade e, se sai, outro assume (ver rtm.arch.authoritative-server, "host migration") [F: photon2026hostmigration].
- **Overlay estruturado**: o mundo é particionado e cada partição tem um coordenador escolhido pela rede, como no projeto de Knutsson et al. sobre Pastry e Scribe [F: knutsson2004p2p].

O que não é: um relay não é P2P, pois há um nó fixo intermediário (rtm.arch.relay-server); um *listen server* não é P2P, pois um único nó é autoridade por desenho (rtm.arch.authoritative-server). A distinção pode ser tênue quando há host migration [I].

## Problema que resolve

- **Custo e provisionamento.** Knutsson et al. apontam que no modelo cliente-servidor "the server has to be over-provisioned to handle peak loads" e propõem um sistema que "dynamically scales up and down with the number of players", com "lower deployment cost than centralized games servers" [F: knutsson2004p2p].
- **Latência entre pares próximos.** Sem o salto pelo servidor, a latência é a do caminho direto entre os pares [I]; a RFC 8825 descreve, para WebRTC, que o caminho de mídia "goes directly between the browsers" [F: rfc8825, §3].
- **Ausência de infraestrutura.** Em LAN ou entre poucos participantes, dispensa qualquer servidor de jogo; Fiedler observa que o lockstep de Doom funcionava bem em LAN, mas pela Internet usuários de modem tinham experiência muito ruim [F: fiedler2010networking].

## Fundamentos e funcionamento

### Descoberta e NAT traversal

Pares atrás de NAT não conhecem seus endereços públicos. A RFC 8445 (ICE) define a técnica normativa para fluxos UDP: cada agente reúne candidatos de três tipos, **host** ("A transport address on a directly attached network interface"), **server-reflexive** ("A translated transport address on the public side of a NAT", obtido via STUN) e **relayed** ("A transport address allocated from a TURN server"); os pares de candidatos são testados por *connectivity checks*, "a STUN request/response transaction", em ordem de prioridade [F: rfc8445, §2]. Quando nenhum par direto funciona, o TURN "acts as a packet relay, forwarding traffic between L and R" [F: rfc8445, §2]; a norma observa que "use of TURN servers may be expensive, so some deployments may elect not to use them" [F: rfc8445, §5.1.1.2].

Em navegadores, a RFC 8825 fixa o WebRTC como conjunto de protocolos, define o *data channel* como "An abstraction that allows data to be sent between WebRTC endpoints in the form of messages" e deixa a sinalização "outside the scope of the WebRTC protocol suite" [F: rfc8825, §2.2, §3]. [I] Portanto, mesmo P2P exige um serviço de sinalização e, em geral, servidores STUN/TURN; "sem servidor" refere-se apenas à simulação.

Fluxo de estabelecimento [I, a partir de rfc8445 e rfc8825]:

```
par A ──oferta (candidatos)──▶ sinalização ──▶ par B
par A ◀──resposta (candidatos)── sinalização ◀── par B
A ⇄ B: connectivity checks STUN em cada par de candidatos (prioridade)
A ⇄ B: dados pelo primeiro par válido (direto) ou via TURN (relayed)
```

### Overlay estruturado para muitos jogadores

Knutsson et al. baseiam-se em *locality of interest*: embora o mundo seja grande, a área de interesse de um jogador é limitada, e jogadores podem ser agrupados por áreas coincidentes [F: knutsson2004p2p]. O mundo é particionado em regiões; cada região recebe um ID (hash do nome) no espaço de chaves do Pastry, e o nó vivo com ID mais próximo "serves as the coordinator for the region", resolvendo atualizações conflitantes sobre objetos compartilhados e multicastando as bem-sucedidas pelo Scribe [F: knutsson2004p2p]. A gerência de contas permanece centralizada: o projeto "centralizing the account management at the server, and only distributing game states to the peers" [F: knutsson2004p2p].

## Algoritmos e modelos relevantes

- ICE com STUN/TURN para estabelecer conectividade [F: rfc8445].
- Lockstep determinístico entre pares (rtm.arch.deterministic-lockstep) e rollback (GGPO) [F: fiedler2010networking; ggpo2019readme].
- DHT (Pastry) e multicast de aplicação (Scribe) para mapear regiões a coordenadores [F: knutsson2004p2p].
- Replicação de coordenador: o algoritmo mantém "at least one replica up under all circumstances" e replica dinamicamente ao detectar falha [F: knutsson2004p2p].
- Dead reckoning para mascarar perda ou atraso de atualizações de posição (rtm.sync.dead-reckoning), citado pelos autores como mecanismo de aplicação [F: knutsson2004p2p].

## Requisitos e pressupostos

- Confiança mútua ou mecanismos adicionais: Knutsson et al. reconhecem que "Distributing game states to the peers increases the opportunities for cheating" e deixam a prevenção como trabalho futuro [F: knutsson2004p2p].
- Conectividade: sucesso do ICE ou disponibilidade de TURN [F: rfc8445].
- Baixa frequência de falhas: o projeto de Knutsson et al. assume taxa de falha de 0,007 por minuto (de 1000 nós, 7 falham ou saem por minuto) e usa eventos do próprio jogo para detectar falhas, em vez de sondagem ativa [F: knutsson2004p2p].
- Para lockstep: todos os pares presentes antes de começar; Fiedler aponta que entrar no meio da partida é impraticável nesse modelo [F: fiedler2010networking].

## Vantagens e limitações

Vantagens:
- Sem custo de servidor de simulação; escala com o número de jogadores [F: knutsson2004p2p].
- Latência direta entre pares quando o caminho direto existe [F: rfc8825].
- Resiliência parcial: sem ponto único de simulação; no modelo distribuído da Unity, "any one client may be compromised and/or cheating without making the entire experience unplayable" [F: unity2026topologies].

Limitações:
- **Confiança**: sem autoridade, cada par pode mentir; o modelo distribuído é descrito pelo fornecedor como mais vulnerável a trapaças [F: unity2026topologies].
- **Escala por sessão em full mesh**: [I] cada par envia a n−1 pares, logo o tráfego total por tick cresce como n(n−1), ou O(n²); por isso o full mesh é usado com poucos participantes (os exemplos do GGPO vão de 2 a 4 jogadores [F: ggpo2019devguide]) e os overlays estruturados limitam cada jogador à sua região [F: knutsson2004p2p].
- **Latência do mais lento**: em lockstep, cada jogador sofre a latência do participante mais lento [F: fiedler2010networking].
- **NAT**: parte dos pares só se conecta via TURN, que tem custo [F: rfc8445, §5.1.1.2].
- **Disponibilidade do estado**: quando um par sai, "its state quickly becomes stale and the replica becomes invalid" [F: knutsson2004p2p]; em host migration, mudanças desde o último snapshot "will be lost" [F: photon2026hostmigration].
- **Concentração de carga**: no experimento de Knutsson et al., a tarefa de coordenador concentrou-se em cerca de 10% dos nós [F: knutsson2004p2p].

## Alternativas e comparações

Ver rtm.arch.comparison. Em relação ao relay: o relay remove NAT traversal e descoberta ao custo de um salto e de um serviço; em relação ao autoritativo: troca confiança e custo de servidor por confiança mútua [I].

## Métricas e métodos de avaliação

- Taxa de sucesso de conectividade direta vs. relayed (ICE) [I, a partir de rfc8445].
- Número de saltos e atraso de entrega no overlay: Knutsson et al. mediram que a maioria das mensagens unicast chega em até seis saltos, com atraso máximo de cerca de 400 ms sob atrasos de enlace simulados, e que o multicast tem cauda longa (cerca de 1% acima de 18 saltos) [F: knutsson2004p2p].
- Mensagens por segundo por nó e efeito de agregação: a agregação de atualizações reduziu a banda pela metade no experimento com 1000 jogadores e 100 regiões [F: knutsson2004p2p].
- Tempo de recuperação após falha de coordenador: "the time to transfer data to the new coordinator or replica" [F: knutsson2004p2p].

Condições do experimento: até cerca de 4000 nós virtuais em uma única JVM, atualizações de posição a cada 150 ms, média de 10 jogadores por região, 300 segundos simulados, média de 5 execuções [F: knutsson2004p2p]. [I] São resultados de simulação, não de rede real.

## Exemplo técnico independente de domínio

Pseudocódigo de um par em full mesh com host eleito e migração [I]:

```
pares = conectar_todos(lista_de_sinalizacao)        # ICE por par
host = min(pares ∪ {eu}, chave = id_estavel)

loop:
  se eu == host:
    estado = aplicar(estado, entradas_recebidas()); difundir(estado)
  senao:
    enviar(host, minhas_entradas()); estado = receber(host)
  se host caiu:
    host = min(pares_vivos ∪ {eu}, chave = id_estavel)
    se eu == host: estado = ultimo_snapshot_conhecido   # perda possível
```

## Relações com outros conceitos

Alternativa às demais arquiteturas. Depende de rtm.proto.webrtc (e, via ele, de ICE) para conectividade em navegadores. Complementa rtm.arch.deterministic-lockstep (o modelo histórico de P2P em jogos), rtm.sync.interest-management (regiões e grupos de interesse), rtm.sync.dead-reckoning e rtm.rel.fault-tolerance (replicação de coordenador). Relaciona-se com rtm.sec.cheating e rtm.net.bandwidth (crescimento O(n²)).

## Lacunas e questões abertas

- O abstract e metadados de Knutsson et al. foram verificados em cópia PDF hospedada no MIT e via Semantic Scholar (DOI 10.1109/INFCOM.2004.1354485); a página do IEEE Xplore não abriu nesta sessão.
- Não foi verificada literatura sobre detecção de trapaça em P2P (por exemplo, protocolos de *commit* de entradas com hash); fica para rtm.sec.cheating.
- Não há, nas fontes abertas, medição comparando latência P2P direta vs. via relay em redes reais.
- O comportamento do ICE em redes móveis e com NATs simétricos (frequência de uso de TURN) não foi quantificado aqui.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fiedler2010networking | tecnico | 2026-10-29 |
| bettner2001archers | tecnico | 2026-10-29 |
| knutsson2004p2p | academico | 2026-10-29 |
| rfc8445 | normativo | 2026-10-29 |
| rfc8825 | normativo | 2026-10-29 |
| photon2026hostmigration | fornecedor | 2026-10-29 |
| unity2026topologies | fornecedor | 2026-10-29 |
| ggpo2019readme | tecnico | 2026-10-29 |
| ggpo2019devguide | tecnico | 2026-10-29 |
| heroiclabs2026relayed | fornecedor | 2026-10-29 |
