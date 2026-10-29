---
id: rtm.case.age-of-empires
titulo: "Age of Empires: lockstep determinístico sobre modem de 28.8"
tipo: estudo-de-caso
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
ano_do_sistema: 1997
fontes: [bettner2001archers]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.net.latency }
  - { tipo: relacionado-a, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.net.ordering-and-reliability }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.perf.qoe-thresholds }
  - { tipo: relacionado-a, alvo: rtm.perf.metrics }
termos: [deterministic lockstep, communication turn, simultaneous simulation, out-of-sync, speed control]
---

# Age of Empires: lockstep determinístico sobre modem de 28.8

## Contexto e gênero de interação

Age of Empires (Ensemble Studios, 1997) e Age of Empires II: The Age of Kings são jogos de estratégia em tempo real (RTS) em que cada jogador comanda centenas de unidades. O estudo de caso é o artigo "1500 Archers on a 28.8: Network Programming in Age of Empires and Beyond", de Paul Bettner e Mark Terrano, publicado em Game Developer / Gamasutra em 22 de março de 2001 e apresentado originalmente na Game Developers Conference de 2001 [F: bettner2001archers]. A página atual em gamedeveloper.com lista apenas Bettner como autor; o artigo original é assinado por Bettner e Terrano, ambos da Ensemble Studios [F: bettner2001archers].

O gênero importa: em um RTS, o jogador emite comandos de alto nível ("mova estas unidades para cá") com frequência baixa, e o resultado visível é a simulação de muitas entidades. Isso é o oposto de um jogo de ação em primeira pessoa, em que a entrada é contínua e a entidade crítica é uma só [I].

## Restrições de projeto

Os autores reportam as metas do projeto multiplayer [F: bettner2001archers]:

- batalhas "épicas" com muitas unidades e tipos de unidade;
- suporte a 8 jogadores;
- jogo fluido em LAN, modem e Internet;
- plataforma mínima: Pentium 90 com 16 MB de RAM e modem de 28.8 kbps;
- integrar-se ao motor existente (Genie) sem grandes reescritas;
- taxa de quadros consistente de 15 fps na configuração mínima.

O problema central que os autores descrevem: enviar estado por unidade (posição X/Y, status, ação, direção, dano) limitaria o jogo a cerca de 250 unidades em movimento, muito abaixo do que o design pedia [F: bettner2001archers]. Além disso, o tempo de simulação por turno variava bastante: renderização dependia do que o jogador olhava, e o pathfinding da IA podia variar o tempo de turno em até 200 ms [F: bettner2001archers].

## Arquitetura escolhida

Os autores chamam a solução de "simultaneous simulation" (simulação simultânea), hoje conhecida como deterministic lockstep: cada máquina executa a mesma simulação determinística e recebe os mesmos comandos de jogador no mesmo instante lógico; apenas comandos trafegam pela rede, nunca o estado dos objetos [F: bettner2001archers]. A topologia é peer-to-peer: todos trocam comandos entre si, com um host designado para calcular parâmetros de ritmo [F: bettner2001archers].

O transporte é UDP, com o próprio jogo cuidando de ordenação, detecção de perda e reenvio. Cada mensagem carrega número de turno e número de sequência; mensagens atrasadas referentes a turnos passados são descartadas. A regra de projeto declarada é "quando em dúvida, assuma que caiu": receptores pedem imediatamente mensagens faltantes, e emissores às vezes reenviam antes do pedido se o ack atrasa [F: bettner2001archers].

## Técnicas usadas

### Turnos de comunicação e agendamento com dois turnos de antecedência

Um lockstep puro faria o jogo parar a cada espera de rede, dado que a latência na Internet variava de cerca de 20 a 1.000 ms [F: bettner2001archers]. A solução: separar "turnos de comunicação" dos quadros de renderização, com turnos tipicamente de cerca de 200 ms, e marcar cada comando para execução dois turnos no futuro (um comando emitido no turno 1000 executa no turno 1002). Isso dá à rede tempo para entregar e confirmar o comando antes de ser necessário, enquanto a simulação continua [F: bettner2001archers].

### Controle de velocidade (speed control)

Cada cliente informa sua taxa de quadros sustentável e o maior ping médio que observa; os dois valores vão na mensagem "Turn Done", ocupando 2 bytes no total. O host calcula uma nova taxa de quadros e uma nova duração de turno: a duração do turno acompanha o ping de ida e volta e é dividida em tantos quadros de simulação quantos a máquina mais lenta sustenta. A duração sobe rapidamente quando a latência dispara e desce devagar, mudando poucos milissegundos por turno, para manter o jogo suave [F: bettner2001archers].

### Sincronização do gerador de números aleatórios

O gerador de números aleatórios é semeado igualmente em todas as máquinas, e cada máquina precisa fazer exatamente o mesmo número de chamadas. Aleatoriedade que não afeta a simulação (sons de terreno, por exemplo) é tratada à parte: salva-se o estado do gerador, usa-se a aleatoriedade não simulada e restaura-se o estado, re-semeando a partir do último valor [F: bettner2001archers].

### Detecção de dessincronização

Checksums cobrem mundo, objetos, pathfinding, targeting e outros subsistemas; qualquer divergência marca o jogo como "out of sync" e o interrompe. Os autores relatam que diferenças pequenas se acumulam e a causa raiz é difícil de rastrear; a depuração dependia de traces de mensagens muito grandes (cerca de 50 MB) e de dumps do mundo [F: bettner2001archers].

## Resultados e números reportados pelos autores

- Meta de 8 jogadores e 15 fps em Pentium 90 com modem 28.8 [F: bettner2001archers].
- Turno de comunicação típico de cerca de 200 ms; comandos agendados com 2 turnos de antecedência [F: bettner2001archers].
- Latência observada na Internet entre cerca de 20 e 1.000 ms [F: bettner2001archers].
- Percepção de latência de comando em RTS: até cerca de 250 ms passa despercebido; 250 a 500 ms é jogável; acima de 500 ms torna-se perceptível. Latência consistente é melhor percebida do que latência que oscila entre rápida e lenta [F: bettner2001archers].
- Comportamento dos jogadores: um comando a cada 1,5 a 2 s em média, com picos de 3 a 4 comandos por segundo em batalhas pesadas; cliques repetidos no mesmo ponto geravam picos de tráfego, e um filtro que descartava comandos repetidos no mesmo local reduziu a carga [F: bettner2001archers].
- Overhead do controle de velocidade: 2 bytes por mensagem "Turn Done" [F: bettner2001archers].
- Traces de depuração de sincronização de cerca de 50 MB [F: bettner2001archers].

O artigo não apresenta medições controladas (experimentos com variação de latência ou perda); os números acima são observações de desenvolvimento e teste reportadas pelos autores [I].

## Lições documentadas pelos autores

Os autores listam lições explícitas [F: bettner2001archers]:

1. Conhecer o usuário: medir que latência é perceptível no gênero em questão, e preferir latência consistente a latência baixa mas variável.
2. Metering (instrumentação) legível por testadores, sempre ligado, mantido até o lançamento; removê-lo cedo deixou problemas passarem.
3. Educar programadores acostumados a código single-player: há um intervalo entre emitir, receber e executar um comando; comandos devem ser validados no envio e na recepção.
4. Testar bibliotecas de terceiros (DirectPlay) de forma independente para confirmar as garantias prometidas.
5. Construir simuladores e aplicativos mínimos de estresse para isolar problemas como inundação de conexões e perda de pacotes.
6. Testar em modems reais ou simulados cedo e continuamente.

Benefícios "escondidos" que os autores reportam: como todos os clientes devem bater exatamente, alterar estado ou fluxo de um cliente tende a provocar dessincronização, o que dificulta certas trapaças (vazamentos locais de informação, como revelar o mapa, continuaram possíveis e foram corrigidos em patches); e a simulação determinística permitiu gravações de partidas (replays) que reproduzem exatamente, úteis para depuração e para a comunidade [F: bettner2001archers].

## O que é opinião dos autores e o que é fato

- Fato reportado: metas, arquitetura, mecanismos (turnos, agendamento, speed control, RNG, checksums) e os números listados acima [F: bettner2001archers].
- Opinião dos autores: que 250 ms "passa despercebido" em RTS é uma observação qualitativa de testes, não resultado de experimento controlado; que lockstep "dificulta trapaça" é uma avaliação dos autores sobre o estado de 2001 [I].
- Interpretação deste documento: o modelo funciona porque a entrada de um RTS é esparsa e de alto nível; a mesma técnica aplicada a entrada contínua exigiria turnos muito mais curtos e esbarraria na variação de latência que os autores descrevem [I].

## Limites do estudo

- Idade: o artigo descreve sistemas de 1997 a 2000, em modems de 28.8 e 56 kbps e processadores Pentium 90; os limiares de percepção podem ter mudado com hardware e expectativas atuais [I].
- Contexto: o custo do determinismo (mesma ordem de chamadas ao RNG, mesmo ponto flutuante em todas as máquinas) é mencionado como dificuldade de desenvolvimento, mas o artigo não discute determinismo entre plataformas ou compiladores diferentes, que o RTS3 planejado (3D, mais de 8 jogadores, 56k TCP/IP, NAT e firewalls) teria que enfrentar [F: bettner2001archers] [I].
- O artigo não quantifica banda consumida por jogador por segundo além das observações de frequência de comandos [I].

## Relações com outros conceitos

Este caso é o exemplo canônico de `rtm.arch.deterministic-lockstep` em topologia `rtm.arch.peer-to-peer`, sobre `rtm.proto.udp` com confiabilidade implementada na aplicação (`rtm.net.ordering-and-reliability`, `rtm.rel.delivery-semantics`). As observações de percepção de latência alimentam `rtm.perf.qoe-thresholds`; a recomendação de metering permanente alimenta `rtm.perf.metrics`; as observações sobre trapaça alimentam `rtm.sec.cheating`.

## Lacunas e questões abertas

- Os limiares de 250/500 ms para RTS são reportados sem método; falta evidência empírica controlada para o gênero [H].
- Como o modelo se comporta com mais de 8 jogadores e com jogadores em plataformas heterogêneas não é respondido pelo artigo [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| bettner2001archers | tecnico (artigo de praticantes, Game Developer / GDC 2001) | 2026-10-29 |
