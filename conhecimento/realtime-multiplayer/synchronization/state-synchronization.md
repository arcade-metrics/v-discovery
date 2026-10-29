---
id: rtm.sync.state-synchronization
titulo: State synchronization
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [fiedler2015statesync, fiedler2018vr, fiedler2014snapshot, fiedler2015compression, frohnmayer2000tribes]
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-replication }
  - { tipo: alternativa-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: alternativa-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: complementa, alvo: rtm.sync.delta-compression }
  - { tipo: complementa, alvo: rtm.sync.interest-management }
  - { tipo: relacionado-a, alvo: rtm.sync.dead-reckoning }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
  - { tipo: depende-de, alvo: rtm.net.jitter }
termos: [state synchronization, priority accumulator, bandwidth budget, jitter buffer, extrapolation, visual smoothing, quantization]
---

# State synchronization

## Definição e terminologia

State synchronization é a família em que a simulação roda nos dois lados e viajam tanto entradas quanto estado: o lado autoritativo envia, a cada pacote, o estado de um subconjunto dos objetos, escolhido por prioridade dentro de um orçamento de banda, e o receptor aplica esse estado à sua simulação local, que continua avançando (extrapolando) entre atualizações [F: fiedler2015statesync]. O autor a descreve como "approximate and lossy": não exige determinismo perfeito e os objetos continuam se movendo entre atualizações [F: fiedler2015statesync].

Termos associados: *priority accumulator* (acumulador de prioridade, mecanismo de escolha de quais objetos entram no pacote), *bandwidth budget* (orçamento de banda por pacote), *jitter buffer*, *visual smoothing* (suavização só na renderização) [F: fiedler2015statesync]. O modelo de rede do TRIBES usa o termo *ghost* para a cópia remota e *Most Recent State* para a categoria de entrega em que só a versão mais recente interessa [F: frohnmayer2000tribes].

O que não é: não é dead reckoning clássico, embora use extrapolação; a diferença é que aqui o receptor roda a simulação física completa como extrapolador, não uma fórmula cinemática por entidade (ver `rtm.sync.dead-reckoning`). [I]

## Problema que resolve

Snapshot interpolation entrega resultado suave mas com atraso alto (350 ms nos testes a 10 pps) e sem simulação local, o que impede o receptor de interagir fisicamente com o estado [F: fiedler2014snapshot]. State synchronization reduz o atraso a um jitter buffer de 4 a 5 frames a 60 Hz e permite simulação local, ao preço de divergência que precisa ser corrigida [F: fiedler2015statesync]. No experimento em VR, o autor adotou essa família porque o motor de física (PhysX) não é determinístico, o que descarta lockstep, e porque manter cópias preditivas com até 250 ms de latência a 90 Hz exigiria cerca de 25 passos de simulação por frame [F: fiedler2018vr].

## Fundamentos e funcionamento

### Dados por objeto

Cada `StateUpdate` traz índice, posição, orientação, velocidade linear e velocidade angular; as velocidades são obrigatórias porque a extrapolação local depende delas; uma flag `at_rest` evita enviar velocidades nulas [F: fiedler2015statesync]. O pacote leva um número de sequência (que pode servir de número de frame a 60 Hz), até 32 entradas redundantes e até 64 state updates; a simulação do autor tem 901 cubos [F: fiedler2015statesync].

### Priority accumulator

Como nem todos os objetos cabem em cada pacote, o autor usa um acumulador por objeto. A cada frame: (1) cada objeto recebe uma prioridade corrente (no exemplo, 1 000 000 para o cubo do jogador, 100 para cubos interagindo, 1 para cubos parados); (2) a prioridade é somada ao acumulador persistente; (3) os objetos são ordenados por acumulador decrescente; (4) os primeiros que cabem no pacote são enviados e têm o acumulador zerado; os que não couberam mantêm o valor [F: fiedler2015statesync]. Sem o acumulador, só os objetos de prioridade alta seriam enviados e os demais nunca seriam atualizados [F: fiedler2015statesync].

Na versão em VR, o fator de prioridade pode ser negativo para impedir envio, cubos em colisões de alta energia e cubos arremessados recebem prioridade extra, e reduzir a prioridade de cubos em repouso piorou os resultados porque eles dessincronizavam sem correção rápida [F: fiedler2018vr]. Um refinamento para objetos que param: ao entrar em repouso, o objeto recebe prioridade elevada até que o pacote com sua posição final seja confirmado, para não perder a última atualização [F: fiedler2015statesync].

O TRIBES descreve o mesmo padrão com outro vocabulário: o *Ghost manager* monta uma lista de atualização com todo objeto que tem mudança de status ou *State Mask* não nula, ordena primeiro por mudança de status e depois por prioridade do objeto (atribuída pela camada de simulação no processo de *scoping*), e escreve na ordem até encher o pacote [F: frohnmayer2000tribes].

### Orçamento de banda

O autor usa um limite de exemplo de 256 kbit/s: calcula-se o tamanho do cabeçalho e do preâmbulo e o restante vai para state updates; se um update não cabe, pula-se para o próximo; o limite pode ser ajustado em tempo real, por exemplo reduzido sob congestionamento [F: fiedler2015statesync]. No TRIBES, cada stream manager tem taxa e tamanho de pacote definidos pelo host remoto conforme sua conexão; um cliente em modem de 28.8 kbit/s poderia pedir 10 pacotes por segundo de 200 bytes, cerca de 2 KB/s [F: frohnmayer2000tribes].

### Jitter buffer e aplicação do estado

Pacotes chegam em rajadas irregulares (o autor cita 2, 0, 1, 2, 0 por frame); são segurados e entregues na ordem e no tempo corretos pelo número de sequência, com atraso sugerido de 4 a 5 frames a 60 Hz; sem isso há divergência e *pops* em pilhas de objetos [F: fiedler2015statesync]. O autor recomenda aplicar o estado diretamente na simulação ("snap the physics state hard"), sem suavização, para que a extrapolação parta de um estado físico válido [F: fiedler2015statesync].

### Quantização dos dois lados

Para que as extrapolações dos dois lados fiquem parecidas, o estado é quantizado nos dois lados antes de cada passo de simulação, como se tivesse sido transmitido [F: fiedler2015statesync]. A precisão necessária é maior que em snapshot interpolation: 4096 valores por metro para posição (contra 512) e 15 bits por componente do quaternion "smallest three" (contra 9); precisão insuficiente empurra objetos para penetração e o solver reage com *pops* [F: fiedler2015statesync]. Em VR, a resolução usada foi de 1/1000 de centímetro, e a quantização introduziu penetrações que o PhysX corrigia com saltos, mitigadas com `maxDepenetrationVelocity` de 1 m/s [F: fiedler2018vr].

### Suavização visual

A correção é escondida só na renderização: ao chegar um update, calcula-se um offset de erro de posição e orientação tal que o objeto visual não se mova; o offset decai a cada frame (fator 0,9 para posição; slerp de 0,1 em direção à identidade para orientação) [F: fiedler2015statesync]. Fatores adaptativos: erro até 25 cm usa fator 0,95 (suave); erro de 1 m ou mais usa 0,85 (rápido), com transição linear; para orientação, faixa de 0,1 a 0,5 pelo produto escalar com a identidade [F: fiedler2015statesync]. A justificativa do autor: correções grandes precisam ser rápidas para não desorientar, e jitter pequeno precisa de suavização forte [F: fiedler2015statesync].

## Requisitos e pressupostos

- Simulação executável no receptor na mesma taxa que no emissor; o autor recomenda 60 Hz nos dois lados [F: fiedler2015statesync].
- Mecanismo de confirmação de pacotes se houver codificação delta por objeto (ver `rtm.sync.delta-compression`) [F: fiedler2015statesync].
- Estado contínuo com velocidades conhecidas. [I]
- Autoridade clara por objeto; em simulação distribuída, dois números de sequência por objeto (autoridade e propriedade) resolveram conflitos no experimento em VR, com a propriedade vencendo a autoridade [F: fiedler2018vr].

## Vantagens e limitações

Vantagens: atraso menor que snapshot interpolation (4 a 5 frames contra centenas de ms) [F: fiedler2015statesync]; o receptor pode interagir com o estado; banda limitada por orçamento, não pelo número de objetos [F: fiedler2015statesync]; mesmo sem suavização nem compressão o resultado já é bom segundo o autor [F: fiedler2015statesync].

Limitações: rajadas de perda de cerca de 1/4 de segundo ainda causam *pops*, que o autor considera inevitáveis [F: fiedler2015statesync]; custo de CPU, pois forçar o estado de corpos rígidos a cada frame aumentou muito o uso do PhysX [F: fiedler2018vr]; instabilidades específicas de física (cubos deslizando por realimentação da rotação quantizada; pilhas vibrando), resolvidas com soluções caseiras como buffer circular de 16 frames para detectar repouso [F: fiedler2018vr]; a representação "smallest three" em ponto fixo mostrou-se numericamente instável para predição de rotação, e o autor recomenda não usá-la no futuro [F: fiedler2018vr]; sem servidor autoritativo, o modelo distribuído só serve para experiências cooperativas [F: fiedler2018vr].

## Alternativas e comparações

| Aspecto | Snapshot interpolation | State synchronization |
|---|---|---|
| Conteúdo do pacote | todos os objetos visíveis [F: fiedler2014snapshot] | subconjunto por prioridade [F: fiedler2015statesync] |
| Simulação no receptor | não | sim, extrapola [F: fiedler2015statesync] |
| Velocidades no pacote | só se Hermite [F: fiedler2014snapshot] | obrigatórias [F: fiedler2015statesync] |
| Atraso | 3× intervalo + jitter [F: fiedler2014snapshot] | 4 a 5 frames a 60 Hz [F: fiedler2015statesync] |
| Precisão de quantização | 512/m, 9 bits [F: fiedler2015compression] | 4096/m, 15 bits [F: fiedler2015statesync] |
| Banda citada | ~2 Mbit/s a 10 pps sem compressão [F: fiedler2014snapshot] | orçamento de 256 kbit/s [F: fiedler2015statesync] |

## Métricas e métodos de avaliação

Banda efetiva contra o orçamento; frequência de *pops* sob perda em rajada; tempo até cada objeto receber ao menos uma atualização (starvation), que o acumulador deve limitar [I]; metas qualitativas do experimento em VR: pegar e arremessar sem latência perceptível e pilhas que entram em repouso sem jitter visível [F: fiedler2018vr].

## Exemplo técnico independente de domínio

Priority accumulator com orçamento de bytes por pacote.

```
estado persistente: acum[o] = 0 para cada objeto o

montar_pacote(orcamento_bytes):
    para cada o:
        acum[o] += prioridade(o)              # ex.: 1e6 jogador, 100 ativo, 1 parado; <0 nunca envia
    ordem = objetos ordenados por acum decrescente
    pacote = cabecalho()                      # seq, ack, ack_bits, entradas redundantes
    para o em ordem:
        se acum[o] <= 0: continuar
        upd = codificar_estado(o)             # pos, rot, vel, ang_vel, at_rest
        se tamanho(pacote) + tamanho(upd) > orcamento_bytes: continuar   # tenta o próximo, menor
        pacote.anexar(upd)
        acum[o] = 0
    enviar(pacote)

receptor, a cada frame:
    p = jitter_buffer.entregar(frame_atual - atraso_frames)   # 4 a 5 frames a 60 Hz
    para upd em p.updates: aplicar_sem_suavizar(upd); offset_visual[o] = pos_visual - pos_fisica
    simular_um_passo()                                        # quantizar estado antes do passo
    para cada o: offset_visual[o] *= fator(|offset_visual[o]|); renderizar(pos_fisica + offset_visual[o])
```

## Relações com outros conceitos

Parte de `rtm.sync.state-replication`; alternativa a `rtm.sync.snapshot-interpolation` e a `rtm.arch.deterministic-lockstep`. A extrapolação local é parente de `rtm.sync.dead-reckoning`; o priority accumulator é uma forma temporal de `rtm.sync.interest-management`; a codificação delta por objeto está em `rtm.sync.delta-compression`. A predição do próprio avatar em cliente-servidor (`rtm.pred.client-side-prediction`) é um caso especial de simulação local com correção.

## Lacunas e questões abertas

- Os valores de prioridade, fatores de suavização e tamanho de jitter buffer são escolhas empíricas do autor para sua cena; não há fonte que os generalize.
- O autor pede soluções melhores para a detecção de repouso em simulação replicada [F: fiedler2018vr]; questão aberta.
- Não há comparação revisada por pares entre state synchronization e snapshot interpolation.
- O modelo TRIBES é o antecedente histórico mais próximo que verificamos; o PDF não traz data e a atribuição de ano é inferida (TRIBES publicado em dezembro de 1998 e TRIBES 2 em desenvolvimento) [F: frohnmayer2000tribes].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fiedler2015statesync | tecnico | 2026-10-29 |
| fiedler2018vr | tecnico | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2015compression | tecnico | 2026-10-29 |
| frohnmayer2000tribes | tecnico | 2026-10-29 |
