---
id: rtm.case.tribes
titulo: "TRIBES: streams por requisito de entrega, ghosts e notificação de pacotes"
tipo: estudo-de-caso
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
ano_do_sistema: 1998
fontes: [frohnmayer2001tribes]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.proto.udp }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.net.ordering-and-reliability }
  - { tipo: relacionado-a, alvo: rtm.net.packet-loss }
  - { tipo: relacionado-a, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.sync.state-replication }
  - { tipo: relacionado-a, alvo: rtm.sync.interest-management }
  - { tipo: relacionado-a, alvo: rtm.sync.delta-compression }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
termos: [ghost, ghost manager, event manager, move manager, state mask, scoping, most recent state, packet notification, bit packing]
---

# TRIBES: streams por requisito de entrega, ghosts e notificação de pacotes

## Contexto e gênero de interação

Starsiege: TRIBES (Dynamix, dezembro de 1998) é um jogo de ação em equipe, em primeira pessoa, com veículos e mapas grandes, jogável em LAN e Internet. A fonte é "The TRIBES Engine Networking Model, or How to Make the Internet Rock for Multi-player Games", de Mark Frohnmayer e Tim Gift (Dynamix) [F: frohnmayer2001tribes]. O texto diz que o modelo "está sendo desenvolvido para TRIBES II" e "foi implementado primeiro em Starsiege TRIBES, publicado em dezembro de '98" [F: frohnmayer2001tribes]. O PDF espelhado não traz data impressa; a atribuição corrente do artigo à GDC de 2001 não foi verificada contra registro da conferência nesta sessão [I].

## Restrições de projeto

Reportado pelos autores [F: frohnmayer2001tribes]:

- até 128 jogadores humanos ou controlados por IA em uma partida;
- desempenho na Internet dirigiu o projeto: conexões de modem de baixo custo, banda baixa, latência alta e perda intermitente;
- exemplo de configuração: cliente em modem 28.8 define 10 pacotes por segundo de 200 bytes, cerca de 2 KB/s;
- entrada amostrada a cada 32 ms; simulação avança em incrementos fixos de 32 ms ("ticks").

## Arquitetura escolhida

Cliente/servidor, com o servidor validando todos os movimentos dos jogadores. Os autores observam que só alguns gerenciadores são assimétricos e nada impede o modelo em topologias peer-to-peer ou multi-servidor [F: frohnmayer2001tribes]. Três camadas [F: frohnmayer2001tribes]:

1. Connection Layer: módulo de pacotes de plataforma (UDP) e Connection Manager, que oferece conexão virtual sem garantias de entrega, mas com notificação de status de cada pacote.
2. Stream Layer: Stream Manager mais cinco gerenciadores (Event, Ghost, Move, Datablock, String), cada um com garantia de entrega distinta.
3. Simulation Layer: avanço do tempo, escopo (scoping) e predição no cliente.

O conceito-chave é classificar todo dado por requisito de entrega [F: frohnmayer2001tribes]:

| Categoria | Semântica |
|---|---|
| Non-guaranteed | nunca retransmitido se perdido |
| Guaranteed | retransmitido e entregue na ordem de envio |
| Most Recent State | volátil; só a versão mais recente interessa |
| Guaranteed Quickest | precisa chegar o mais rápido possível |

## Técnicas usadas

### Notificação de pacotes em vez de retransmissão

O Connection Manager usa janela deslizante e acks apenas para avançar a janela e gerar eventos de notificação, com overhead médio de 3 bytes por pacote. Pacotes nunca são retransmitidos pela camada de conexão e são liberados logo após o envio; a notificação ("entregue" ou "perdido", onde "perdido" inclui chegada fora de ordem) é repassada à camada de streams em ordem de envio, e cada gerenciador decide o que fazer. Os autores afirmam que uma camada que só oferecesse "garantido" ou "não garantido" não bastaria para as quatro modalidades [F: frohnmayer2001tribes].

### Bit packing

Um bit stream próprio provê leitura e escrita de bits, inteiros de comprimento variável, floats normalizados e strings com Huffman; todo dado, inclusive cabeçalho e janela, passa por ele [F: frohnmayer2001tribes].

### Event Manager

Entrega eventos (objetos persistentes polimórficos) garantidos e não garantidos; eventos garantidos são processados em ordem. Se um pacote é notificado como perdido, os eventos nele voltam à frente da fila. Overhead normal de 3 bits por pacote e 1 bit por evento; de 7 a 14 bits adicionais por pacote se houver perda [F: frohnmayer2001tribes].

### Ghost Manager, scoping e Most Recent State

Um ghost é a cópia de um objeto do servidor em um host remoto. Só objetos em escopo (potencialmente visíveis ao cliente, determinado por banco espacial) são ghosted; objetos "ghost always" ficam sempre em escopo. Cada ghost tem um Ghost ID e uma State Mask em que cada bit representa um conjunto de estado (posição e velocidade, rotação, animação); objetos de TRIBES têm tipicamente mais de 20 flags de estado. Ao preencher um pacote, o gerenciador constrói uma lista de atualização ordenada por mudança de status e depois por prioridade, e escreve até encher. A prioridade é calculada pelo próprio objeto a partir de distância, raio projetado no frustum, velocidade relativa, estado de animação e modificadores de interesse (projéteis vindo na direção do cliente valem mais que veículos, que valem mais que itens) [F: frohnmayer2001tribes].

A garantia "Most Recent State": ao escrever um estado, a máscara enviada fica registrada no Transmission Record e é limpa; se o pacote é notificado como perdido, os bits voltam à máscara, exceto se um pacote posterior já levou o mesmo bit, caso em que a perda é ignorada. Os autores descrevem quatro possibilidades (entregue; perdido sem mudança; perdido com mudança já reenviada; perdido com mudança recente ainda não enviada) e explicam que a posição obsoleta nunca é reenviada [F: frohnmayer2001tribes]. Os autores afirmam que os objetos de simulação dependem "quase exclusivamente" desse mecanismo [F: frohnmayer2001tribes].

### Move Manager e predição do objeto controlado

Moves (translações, rotações e gatilhos, coletados a cada 32 ms) vão em todo pacote; cada move é transmitido três vezes em pacotes consecutivos. Se 3 pacotes seguidos caem, moves exclusivos deles se perdem, podendo causar "warping" momentâneo. Em Starsiege TRIBES, toda a janela de moves ia em cada pacote (100% de entrega), mas isso criava realimentação negativa: perda alargava a janela, aumentava o pacote, estourava a banda e causava mais perda; a mudança para três repetições foi feita por isso [F: frohnmayer2001tribes].

O Control Object do servidor e seu ghost recebem os mesmos moves e devem processá-los deterministicamente a partir do mesmo estado inicial; o servidor escreve o estado do Control Object em todo pacote, o que permite ao cliente predizer o próprio movimento à frente das atualizações e ao servidor validar todos os moves [F: frohnmayer2001tribes]. Ghosts não controlados (itens, projéteis) predizem por conta própria e interpolam suavemente para a posição corrigida quando chega atualização [F: frohnmayer2001tribes].

### Datablocks

Dados estáticos (atributos de tipos de veículo, por exemplo) são enviados uma vez, via eventos garantidos, normalmente na conexão ou troca de mapa; o ghost só envia o ID do datablock, com "enormes economias de banda" segundo os autores [F: frohnmayer2001tribes].

### Avanço do tempo e interpolação

Simulação em ticks de 32 ms; ghosts mantêm informação de interpolação para trás, usada para "tween" entre ticks em máquinas de taxa de quadros alta [F: frohnmayer2001tribes].

## Resultados e números reportados

- 128 jogadores por partida; modem 28.8 com 10 pacotes/s de 200 bytes (cerca de 2 KB/s); tick de 32 ms; 3 bytes de overhead por pacote na conexão; 3 bits por pacote e 1 bit por evento no Event Manager; mais de 20 flags de estado por objeto; cada move enviado 3 vezes [F: frohnmayer2001tribes].
- Não há medições de desempenho, perda tolerada ou latência percebida no artigo [I].

## Lições documentadas pelos autores

- Classificar dados por requisito de entrega e dar a cada classe um mecanismo próprio faz "uso ótimo" da banda disponível, segundo os autores [F: frohnmayer2001tribes].
- A realimentação negativa da retransmissão de moves é relatada como problema concreto de produção, corrigido em TRIBES II [F: frohnmayer2001tribes].
- Os autores listam o que o modelo não resolve: quais comportamentos ficam no servidor e quais no cliente, como organizar estados parciais, como priorizar, que compressão usar, como predizer o Control Object; e propõem melhorias não implementadas: pacotes sob demanda, processamento assíncrono por cliente, stream de áudio, banda dinâmica por cliente e estimativa automática de banda [F: frohnmayer2001tribes].

## O que é opinião e o que é fato

- Fato: estrutura das camadas, categorias, algoritmos de máscara e notificação, números listados [F: frohnmayer2001tribes].
- Opinião dos autores: que o modelo faz uso "ótimo" de banda; a afirmação não é acompanhada de medição [F: frohnmayer2001tribes] [I].
- Interpretação deste documento: a notificação de entrega sem retransmissão é a ideia que distingue TRIBES; ela permite que "mais recente" e "garantido e ordenado" coexistam no mesmo pacote sem head-of-line blocking [I].

## Limites do estudo

- Descreve TRIBES (1998) e o projeto de TRIBES II; valores como 32 ms e 28.8 refletem a época [I].
- O artigo não traz data impressa nem dados experimentais [F: frohnmayer2001tribes].
- A predição do Control Object e a escolha de prioridades são declaradas fora do escopo pelos autores [F: frohnmayer2001tribes].

## Relações com outros conceitos

Instância de `rtm.arch.authoritative-server` sobre `rtm.proto.udp` cuja contribuição central é a semântica de entrega por classe de dado (`rtm.rel.delivery-semantics`, `rtm.net.ordering-and-reliability`) com tolerância a `rtm.net.packet-loss` sem retransmissão de camada baixa. O Ghost Manager combina `rtm.sync.state-replication` com atualização parcial por máscara (`rtm.sync.delta-compression`) e scoping com prioridade (`rtm.sync.interest-management`). O Move Manager implementa `rtm.pred.client-side-prediction` do objeto controlado; o tweening entre ticks relaciona-se a `rtm.pred.entity-interpolation`. O orçamento por cliente relaciona-se a `rtm.net.bandwidth`.

## Lacunas e questões abertas

- Como a prioridade de ghosts se comporta com 128 jogadores e banda de modem não é quantificado [H].
- A estimativa automática de banda é listada como problema em aberto pelos autores [F: frohnmayer2001tribes].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| frohnmayer2001tribes | tecnico (artigo de praticantes; PDF espelhado em gamedevs.org) | 2026-10-29 |
