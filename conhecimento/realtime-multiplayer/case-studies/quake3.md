---
id: rtm.case.quake3
titulo: "Quake III Arena: snapshots com delta contra o último ack sobre UDP"
tipo: estudo-de-caso
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
ano_do_sistema: 1999
fontes: [sanglard2012quake3]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.sync.delta-compression }
  - { tipo: relacionado-a, alvo: rtm.sync.state-replication }
  - { tipo: relacionado-a, alvo: rtm.net.packet-loss }
  - { tipo: relacionado-a, alvo: rtm.net.ordering-and-reliability }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.net.bandwidth }
termos: [snapshot, delta compression, last acknowledged snapshot, netchan, MTU]
---

# Quake III Arena: snapshots com delta contra o último ack sobre UDP

## Contexto e gênero de interação

Quake III Arena (id Software, 1999) é um jogo de ação em primeira pessoa, multiplayer, com entrada contínua e ritmo rápido. A fonte deste caso é a revisão do código-fonte publicado pela id Software, escrita por Fabien Sanglard: "Quake 3 Source Code Review: Network Model (Part 3 of 5)", de 30 de junho de 2012 [F: sanglard2012quake3].

Nota sobre a natureza da fonte: Sanglard não é autor do sistema; a análise, porém, é feita diretamente sobre o código-fonte liberado pela id Software, com trechos de código e nomes de funções (`MSG_WriteDeltaEntity`, `Netchan_Transmit`, `netField_t`), o que a torna uma fonte técnica verificável contra o artefato primário (o código) [I]. O texto também remete a escritos de Brian Hook (id Software) sobre o modelo de rede, que não foram abertos nesta pesquisa [F: sanglard2012quake3].

## Restrições de projeto

O artigo não enumera metas formais do projeto. O que é reportado [F: sanglard2012quake3]:

- jogo de ritmo rápido em que informação não recebida na primeira transmissão já é velha demais para valer reenvio;
- transporte UDP/IP, evitando TCP/IP porque a transmissão confiável introduzia latência intolerável;
- pacotes fragmentados em pedaços de 1.400 bytes, embora um datagrama UDP possa ter até 65.507 bytes, para ficar abaixo do MTU típico de 1.500 bytes e evitar fragmentação e remontagem em roteadores.

## Arquitetura escolhida

Cliente/servidor com servidor autoritativo: os clientes enviam comandos a cada quadro e recebem atualizações do estado do jogo; o servidor mantém o "Master gamestate" autoritativo e o propaga a cada cliente, lidando com perda de pacotes UDP. Comandos do cliente viram valores `event_t` que modificam o estado ao chegar ao servidor [F: sanglard2012quake3].

A pilha de rede tem duas camadas opcionais e mutuamente exclusivas: criptografia com chave pré-compartilhada, ou compressão com chave Huffman pré-computada. O módulo NetChannel, herdado do QuakeWorld, abstrai a comunicação de baixo nível [F: sanglard2012quake3].

## Técnicas usadas

### Snapshots e histórico por cliente

Para cada cliente, o servidor guarda os últimos 32 estados enviados (snapshots) em um array circular, com wrap por máscara binária. Um estado "dummy", com todos os campos zerados, serve de baseline quando não há snapshot válido anterior [F: sanglard2012quake3].

### Delta contra o último snapshot confirmado

A cada envio, o servidor copia o Master gamestate para a próxima posição do histórico e compara com uma baseline: o último snapshot que o cliente confirmou (ack), ou o dummy se não houver confirmação válida ou se o snapshot for velho demais. Só os campos diferentes são escritos [F: sanglard2012quake3].

O artigo ilustra com um estado de quatro campos (três inteiros de posição e um de vida) [F: sanglard2012quake3]:

- quadro 1: sem snapshot válido, baseline é o dummy, envia-se tudo, que o autor estima em 132 bits (cada campo com um bit marcador seguido de 32 bits);
- quadro 2: o snapshot anterior foi confirmado, envia-se só o campo alterado, 36 bits;
- quadro 3: o snapshot mais recente não foi confirmado, o delta é calculado contra um snapshot mais antigo confirmado; a mensagem carrega tanto a alteração antiga não recebida quanto a nova.

O autor argumenta que esse único algoritmo produz atualizações parciais ou completas e reenvia automaticamente informação antiga perdida junto com a nova, sem lógica de retransmissão separada [F: sanglard2012quake3].

### Introspecção de memória em C

Como C não tem reflexão, o motor usa uma tabela `netField_t` com nome do campo, offset (calculado com macro de stringização e cast de ponteiro nulo) e tamanho em bits. `MSG_WriteDeltaEntity` percorre a tabela comparando campos por índice, offset e tamanho, sem conhecer o significado dos campos [F: sanglard2012quake3].

### Mensagens confiáveis à parte

Algumas mensagens precisam chegar (saída de jogador, troca de mapa); o NetChannel garante a entrega delas, enquanto os snapshots lidam com perda do estado regular [F: sanglard2012quake3].

## Resultados e números reportados

- 32 snapshots por cliente no histórico do servidor [F: sanglard2012quake3].
- Cerca de 8 MB de memória para manter 32 estados de 4 jogadores, segundo medição do autor da revisão [F: sanglard2012quake3].
- Fragmentação em 1.400 bytes; MTU típico de 1.500 bytes; limite de datagrama UDP de 65.507 bytes [F: sanglard2012quake3].
- Exemplo didático: 132 bits para atualização completa de quatro campos, 36 bits para delta de um campo [F: sanglard2012quake3].
- Taxas de envio do servidor (Hz) e portas não são informadas no artigo [F: sanglard2012quake3].

## Lições documentadas

O princípio declarado no artigo: em um jogo rápido, dado que não chegou na primeira tentativa já não vale o reenvio, por isso UDP e "delta contra o último confirmado" em vez de retransmissão ao estilo TCP [F: sanglard2012quake3]. A lição implícita, na leitura deste documento, é que a confiabilidade pode ser obtida pela semântica dos dados (estado mais recente) em vez de pela semântica do transporte (entrega de cada pacote) [I].

## O que é opinião e o que é fato

- Fato: estrutura do histórico, algoritmo de delta, fragmentação, tabela de campos, uso de UDP e NetChannel, conforme código revisado [F: sanglard2012quake3].
- Opinião/estimativa do autor da revisão: a contagem de bits do exemplo e a estimativa de 8 MB de memória são cálculos de Sanglard, não números publicados pela id Software [F: sanglard2012quake3] [I].
- Interpretação deste documento: o custo do esquema cresce com perda de pacotes, porque o delta contra um ack antigo embute mais campos; isso é um compromisso entre simplicidade e banda sob perda [I].

## Limites do estudo

- Trata-se de revisão de código feita 13 anos após o lançamento, não de relato de projeto dos autores originais; decisões de design são inferidas do código [I].
- O artigo cobre apenas o modelo de transmissão; predição do cliente e interpolação no Quake III não são abordadas nesta parte da série [I].
- Nada é dito sobre taxas de atualização, banda por jogador ou comportamento sob perda medida [F: sanglard2012quake3].

## Relações com outros conceitos

Instância de `rtm.arch.authoritative-server` sobre `rtm.proto.udp`. A técnica central é `rtm.sync.delta-compression` contra o último snapshot confirmado, forma de `rtm.sync.state-replication` que torna a transmissão tolerante a `rtm.net.packet-loss` sem retransmissão explícita (`rtm.rel.delivery-semantics`, `rtm.net.ordering-and-reliability`). O histórico de 32 snapshots é o lado servidor de `rtm.sync.snapshot-interpolation`. A fragmentação em 1.400 bytes relaciona-se a `rtm.net.bandwidth`.

## Lacunas e questões abertas

- Qual a taxa de snapshots padrão do servidor e como ela interage com a janela de 32 estados sob perda alta: não respondido pela fonte [H].
- Os escritos de Brian Hook citados pelo autor poderiam oferecer relato de primeira mão dos projetistas; não foram verificados nesta sessão [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| sanglard2012quake3 | tecnico (revisão de código-fonte publicado) | 2026-10-29 |
