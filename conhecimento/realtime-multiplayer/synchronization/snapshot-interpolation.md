---
id: rtm.sync.snapshot-interpolation
titulo: Snapshot interpolation
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [fiedler2014snapshot, fiedler2015compression, fiedler2015statesync, gambetta2014entity, sanglard2012quake3, fiedler2010networking]
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-replication }
  - { tipo: alternativa-a, alvo: rtm.sync.state-synchronization }
  - { tipo: alternativa-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: complementa, alvo: rtm.sync.delta-compression }
  - { tipo: complementa, alvo: rtm.sync.interest-management }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
  - { tipo: depende-de, alvo: rtm.proto.udp }
  - { tipo: depende-de, alvo: rtm.net.jitter }
  - { tipo: depende-de, alvo: rtm.net.packet-loss }
termos: [snapshot, interpolation delay, interpolation buffer, jitter buffer, hermite interpolation, slerp, send rate]
---

# Snapshot interpolation

## Definição e terminologia

Snapshot interpolation é a técnica em que o lado autoritativo captura periodicamente um *snapshot* (o estado relevante de todos os objetos visíveis), envia-o sem garantia de entrega, e o receptor, em vez de simular, guarda os snapshots em um buffer e exibe uma interpolação entre dois snapshots passados [F: fiedler2014snapshot]. O atraso deliberado entre a recepção e a exibição é o *interpolation delay*; o buffer que o implementa é chamado de *interpolation buffer* ou, por analogia com áudio, *jitter buffer* [F: fiedler2014snapshot].

Gambetta chama a mesma ideia, aplicada a outros jogadores em um jogo cliente-servidor, de *entity interpolation*: o cliente mostra as outras entidades "no passado" em relação ao jogador local, interpolando entre as últimas posições reais recebidas [F: gambetta2014entity]. O documento `rtm.pred.entity-interpolation` trata dessa variante do ponto de vista de predição e reconciliação; aqui o foco é a replicação do estado inteiro.

O que não é: não é extrapolação. Entity interpolation "não prevê nada", usa apenas dados reais do servidor, e por isso mostra o movimento com atraso mas sem saltos de correção [F: gambetta2014entity]. A extrapolação é tratada em `rtm.sync.dead-reckoning`.

## Problema que resolve

Quando a simulação não é determinística, ou há mais participantes do que o lockstep comporta, não dá para replicar entradas; é preciso replicar estado. Fiedler recomenda snapshot interpolation quando a simulação não é determinística ou há mais de 2 a 4 jogadores, faixa em que o lockstep determinístico ainda é recomendado [F: fiedler2014snapshot]. O problema específico que a interpolação resolve é a irregularidade de chegada: pacotes enviados a 60 por segundo chegam em rajadas, alguns frames recebem dois snapshots e outros nenhum; em LAN quase não aparece, em Wi-Fi ou internet produz *hitches* [F: fiedler2014snapshot].

## Fundamentos e funcionamento

### Lado do emissor

O emissor captura, a cada intervalo de envio, o estado de cada objeto e envia um pacote com um número de sequência de 16 bits; o receptor descarta snapshots mais antigos que o último recebido [F: fiedler2014snapshot]. No experimento do autor, o estado por cubo é uma flag `interacting`, uma posição (`vec3f`) e uma orientação (`quat4f`); na versão com interpolação Hermite, a velocidade linear também é enviada [F: fiedler2014snapshot].

Snapshots não precisam de confiabilidade: se um pacote se perde, o receptor pula para o snapshot seguinte. O autor é explícito: "This is why you should always use UDP for sending snapshots" [F: fiedler2014snapshot]. O mesmo princípio aparece no Quake 3, onde informação que não chega na primeira transmissão não vale reenvio porque já estará desatualizada [F: sanglard2012quake3].

### Lado do receptor: buffer e atraso

O receptor guarda os snapshots por um tempo antes de exibi-los e interpola posição e orientação entre dois snapshots "atrasados", trocando latência por suavidade [F: fiedler2014snapshot]. A regra prática do autor para o tamanho do atraso: cerca de 3 vezes o intervalo de envio, para tolerar perda de 2% a 5% (300 ms a 10 pacotes por segundo), mais uma folga para jitter de 1 a 2 frames a 60 fps; nos vídeos a 10 pps o atraso total foi de 350 ms [F: fiedler2014snapshot]. O autor recomenda que o buffer tenha folga para perder dois pacotes seguidos [F: fiedler2014snapshot].

Gambetta usa o mesmo raciocínio com números diferentes: servidor enviando 10 atualizações por segundo e cliente renderizando as outras entidades 100 ms no passado [F: gambetta2014entity]. A diferença (100 ms contra 350 ms) reflete premissas distintas sobre perda e jitter; Gambetta não discute perda de pacotes nesse artigo, Fiedler dimensiona para 5% de perda e ±2 frames de jitter [I].

### Taxa de envio versus taxa de simulação

A taxa de envio é independente da taxa de simulação. No experimento, a simulação roda a 60 Hz, e o autor testa envio a 60 pps (referência, com muito jitter em redes reais) e a 10 pps (taxa principal dos testes de interpolação) [F: fiedler2014snapshot]. Aumentar a taxa de envio reduz o atraso de interpolação: o autor projeta 150 ms a 30 pps e 85 ms a 60 pps, e conclui que, para reduzir o atraso, é preciso aumentar a taxa de envio e otimizar a banda [F: fiedler2014snapshot].

### Interpolação linear versus Hermite

Interpolação linear entre snapshots causa uma leve trepidação na posição por descontinuidade de primeira ordem nos pontos de amostra [F: fiedler2014snapshot]. A interpolação Hermite usa a velocidade linear de cada objeto nos pontos de amostra, passa pelos pontos inicial e final e iguala as velocidades neles, eliminando os artefatos visíveis a 10 pps sem aumentar a taxa de envio, ao custo de enviar a velocidade [F: fiedler2014snapshot]. Para orientação, trocar nlerp por slerp basta para velocidade angular constante, sem enviar velocidade angular [F: fiedler2014snapshot].

### Extrapolação como complemento

O autor testou extrapolar 200 ms para reduzir o atraso total de 350 ms para 150 ms e considerou o resultado ruim: a extrapolação não conhece colisões nem a física do jogo, os cubos atravessam o chão e depois são corrigidos; ele afirma que extrapolação funciona razoavelmente apenas para movimentos quase lineares (aviões, barcos, naves) e por períodos curtos, de 50 a 250 ms [F: fiedler2014snapshot].

## Requisitos e pressupostos

- Transporte sem retransmissão (UDP ou equivalente) e sequência própria [F: fiedler2014snapshot]. Ver `rtm.proto.udp`.
- Relógio de apresentação no receptor que avança de forma estável, independente da chegada dos pacotes; o atraso alvo deve cobrir o jitter esperado (`rtm.net.jitter`). [I]
- Banda suficiente para o estado visível: sem compressão, 900 cubos a 225 bits cada dão cerca de 25 KB por snapshot, 11,6 Mbit/s a 60 pps e cerca de 2 Mbit/s a 10 pps [F: fiedler2014snapshot]. A redução para o alvo de 256 kbit/s do autor exige quantização e codificação delta, descritas em `rtm.sync.delta-compression` [F: fiedler2015compression].
- Estado interpolável: posição, orientação e grandezas contínuas. Estado discreto (animação, eventos) precisa de tratamento à parte. [I]

## Vantagens e limitações

Vantagens: nenhuma simulação no receptor, portanto nenhum requisito de determinismo [F: fiedler2014snapshot]; tolerância natural a perda; entrada tardia trivial (o próximo snapshot é o estado completo) [I]; resultado visual suave mesmo a 10 pps com Hermite [F: fiedler2014snapshot].

Limitações: atraso de exibição maior que o das outras famílias (350 ms nos testes a 10 pps, contra 4 a 5 frames a 60 Hz no state synchronization) [F: fiedler2014snapshot] [F: fiedler2015statesync]; banda proporcional ao número de objetos visíveis [F: fiedler2014snapshot]; o receptor não pode interagir fisicamente com o estado replicado sem simulação local [I]. Gambetta nota a consequência para mira: o tiro acerta a posição de 100 ms atrás, o que motiva a compensação de lag [F: gambetta2014entity]; ver `rtm.pred.lag-compensation`.

## Alternativas e comparações

| Aspecto | Snapshot interpolation | State synchronization | Dead reckoning |
|---|---|---|---|
| Receptor simula? | não [F: fiedler2014snapshot] | sim, com correções [F: fiedler2015statesync] | extrapola a partir do último estado [F: gambetta2014entity] |
| Dados por objeto | posição, orientação (+ velocidade se Hermite) [F: fiedler2014snapshot] | posição, orientação, velocidades [F: fiedler2015statesync] | posição, velocidade, aceleração [I] |
| Atraso | 3× intervalo de envio + jitter [F: fiedler2014snapshot] | 4 a 5 frames a 60 Hz [F: fiedler2015statesync] | zero nominal, com saltos de correção [F: gambetta2014entity] |
| Melhor para | movimento imprevisível [F: gambetta2014entity] | física interativa com muitos objetos [F: fiedler2015statesync] | movimento previsível (carros, navios) [F: gambetta2014entity] |

## Métricas e métodos de avaliação

Banda em Mbit/s por taxa de envio [F: fiedler2014snapshot]; atraso total em ms; presença de artefatos sob perda e jitter emulados (5% e ±2 frames) [F: fiedler2014snapshot]. Ver `rtm.perf.network-emulation`.

## Exemplo técnico independente de domínio

Buffer de interpolação com atraso fixo. `atraso` é o interpolation delay; `snapshots` é ordenado por tempo de captura `t`.

```
receber(snapshot s):
    se s.seq <= ultimo_seq: descartar        # sequência de 16 bits, com wrap
    ultimo_seq = s.seq
    snapshots.inserir_ordenado(s)             # chave: s.t
    remover entradas com s.t < agora - 2*atraso

amostrar(agora):
    t_alvo = agora - atraso
    (a, b) = par consecutivo com a.t <= t_alvo < b.t
    se não existe b:                          # buffer esvaziou (perda ou jitter)
        retornar último estado exibido        # ou extrapolar por no máximo ~250 ms
    u = (t_alvo - a.t) / (b.t - a.t)
    para cada objeto o:
        pos = hermite(a[o].pos, a[o].vel, b[o].pos, b[o].vel, u)   # ou lerp se sem velocidade
        rot = slerp(a[o].rot, b[o].rot, u)
    retornar estado interpolado
```

Dimensionamento, seguindo a regra do autor: `atraso = 3 * intervalo_envio + folga_jitter` [F: fiedler2014snapshot].

## Relações com outros conceitos

Parte da família `rtm.sync.state-replication`. Alternativa a `rtm.sync.state-synchronization` e a `rtm.arch.deterministic-lockstep`. Torna-se viável em escala quando combinada com `rtm.sync.delta-compression` e `rtm.sync.interest-management`. A variante do lado do jogador, aplicada só a entidades remotas, está em `rtm.pred.entity-interpolation`; o atraso que ela introduz é o motivo de `rtm.pred.lag-compensation`.

## Lacunas e questões abertas

- O Quake 3 envia snapshots delta-comprimidos; Sanglard não informa a taxa de envio nem se o cliente interpola, por isso não citamos o Quake 3 como exemplo de interpolação, só de snapshots [F: sanglard2012quake3].
- O artigo de Bernier (Valve, 2001), referência histórica para entity interpolation com 100 ms, não pôde ser aberto (HTTP 403 nas cópias tentadas): não verificado.
- Gambetta não data a página; o ano 2014 segue a convenção do domínio.
- Não encontramos fonte com medição perceptual de qual atraso de interpolação é aceitável por gênero; ver `rtm.perf.qoe-thresholds`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2015compression | tecnico | 2026-10-29 |
| fiedler2015statesync | tecnico | 2026-10-29 |
| gambetta2014entity | tecnico | 2026-10-29 |
| sanglard2012quake3 | tecnico | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
