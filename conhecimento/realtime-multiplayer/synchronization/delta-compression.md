---
id: rtm.sync.delta-compression
titulo: Delta compression
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [sanglard2012quake3, fiedler2015compression, fiedler2015statesync, fiedler2018vr, fiedler2016reliable, frohnmayer2000tribes]
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-replication }
  - { tipo: complementa, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: complementa, alvo: rtm.sync.state-synchronization }
  - { tipo: depende-de, alvo: rtm.net.ordering-and-reliability }
  - { tipo: depende-de, alvo: rtm.proto.udp }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.rel.delivery-semantics }
termos: [delta compression, baseline, acknowledged baseline, quantization, smallest three, state mask, ack bits]
---

# Delta compression

## Definição e terminologia

Delta compression (ou *delta encoding*) é a técnica de enviar, em vez do estado completo, apenas a diferença entre o estado atual e um estado de referência (*baseline*) que o receptor comprovadamente já possui [F: sanglard2012quake3] [F: fiedler2015compression]. A referência é chamada de *acknowledged baseline* porque o emissor só pode usar como base um estado cuja recepção foi confirmada (*acked*) pelo receptor [F: fiedler2015compression]. Quando não há baseline válida, envia-se o estado completo [F: sanglard2012quake3].

Termos associados: *quantização* (reduzir a precisão de um valor para caber em menos bits), *smallest three* (codificação de quaternion que envia só os três menores componentes), *state mask* (máscara de bits que marca quais partes do estado mudaram) [F: fiedler2015compression] [F: frohnmayer2000tribes].

O que não é: não é compressão de propósito geral (Huffman, aritmética), que pode ser aplicada por cima; o Quake 3 aplica Huffman com tabela pré-computada depois da codificação delta [F: sanglard2012quake3]. E não é "enviar só o que mudou" sem baseline confirmada: sem a confirmação, uma perda deixaria o receptor com um estado inconsistente para sempre. [I]

## Problema que resolve

O estado de uma simulação muda pouco entre dois envios consecutivos; a maior parte dos objetos está parada ou se move de forma previsível. Enviar o estado completo gasta banda com informação que o receptor já tem. No experimento de Fiedler, 901 cubos a 60 Hz sem compressão custam cerca de 17,38 Mbit/s contra um alvo de 256 kbit/s [F: fiedler2015compression]; a sequência de otimizações, culminando na codificação delta e no envio só de objetos alterados, é o que fecha essa distância.

## Fundamentos e funcionamento

### O modelo do Quake 3

Sanglard descreve o servidor do Quake 3 com três elementos: o *master gamestate* (estado verdadeiro), um histórico circular dos últimos 32 snapshots enviados a cada cliente e um *dummy snapshot* com todos os campos zerados [F: sanglard2012quake3]. A cada frame do servidor: copia-se o master gamestate para o próximo slot do histórico do cliente; compara-se esse snapshot com o último que o cliente confirmou; se não há confirmação válida, compara-se com o dummy, o que gera uma atualização completa [F: sanglard2012quake3].

No exemplo do artigo, com quatro campos (X, Y, Z, vida): no frame 1, sem baseline, a mensagem completa tem cerca de 132 bits (cada campo com um bit marcador antes de 32 bits de valor); no frame 2, com o snapshot anterior confirmado e só Y alterado, a mensagem fica em cerca de 36 bits; no frame 3, se o cliente não confirmou o último snapshot, a comparação volta ao último confirmado e a mensagem reenvia as mudanças antigas junto com as novas; se o snapshot confirmado for velho demais (fora da janela de 32), volta-se ao dummy [F: sanglard2012quake3]. O mesmo algoritmo, portanto, gera atualizações parciais ou completas e repara perdas sem retransmissão explícita [F: sanglard2012quake3].

A comparação campo a campo é feita por uma tabela `netField_t` (nome, offset e número de bits) construída com a macro `NETF`, no módulo `msg.c`; o código compara campos por offset e tamanho sem saber o que compara [F: sanglard2012quake3]. Mensagens que precisam chegar (saída de jogador, troca de nível) são garantidas pela camada NetChannel, à parte dos snapshots [F: sanglard2012quake3]. O custo de memória medido por Sanglard: 32 snapshots por cliente, cerca de 8 MB para 4 jogadores [F: sanglard2012quake3]. A camada de transporte fragmenta em blocos de 1400 bytes para evitar fragmentação por roteadores com MTU de 1500 [F: sanglard2012quake3].

### A sequência de Fiedler: quantização antes do delta

Fiedler parte de 321 bits por cubo (orientação 128, velocidade 96, posição 96, flag 1) e reduz em etapas: quaternion "smallest three" com 2 bits de índice e 3×9 bits, em faixa de ±0,707107 (222 bits); velocidade quantizada em 3×11 bits com flag "at rest" (160 bits); remoção da velocidade, porque a 60 Hz a interpolação linear basta (126 bits); posição quantizada em 18+18+14 bits para ±256 m em xy e 0 a 32 m em z, com 512 valores por metro, cerca de 2 mm (80 bits) [F: fiedler2015compression]. Só então entra a codificação delta contra baseline confirmada: a diferença de posição fica em média em 26,1 bits e a de orientação em 23,3 bits [F: fiedler2015compression]. Enviando apenas cubos alterados, com índice de 10 bits ou flags conforme a quantidade, o estado estacionário (tudo parado) cai para cerca de 15 kbit/s; o índice relativo com codificação por faixas (1+3, 1+1+5, 1+1+10 bits) custa em média 5,5 bits; flags separadas de "posição alterada" e "orientação alterada" economizam cerca de 2 bits por cubo [F: fiedler2015compression]. O autor relata que codificação aritmética pode superar o *bit-packing* em cerca de 25%, segundo implementação de Fabian Giesen, e recomenda medir dados reais antes de escolher codificações (ele usou busca gulosa em script) [F: fiedler2015compression].

### Baseline por pacote ou por objeto

Em snapshot interpolation a baseline é um snapshot inteiro, porque todos os objetos viajam em todo pacote [F: fiedler2015compression]. Em state synchronization, nem todos os objetos vão em cada pacote, então a baseline é por objeto: cada update precisa indicar qual pacote serve de base, o que custa 1 bit (relativo ou absoluto) mais 16 bits de sequência; a otimização do autor coloca no cabeçalho o pacote confirmado mais recente e envia por objeto um offset de 5 bits em relação a ele, cobrindo cerca de meio segundo a 60 pps; bases mais antigas caem para codificação absoluta [F: fiedler2015statesync]. Em VR, a baseline também é por cubo, exigindo confirmação de pacotes, rastreamento dos estados enviados por pacote e um buffer circular de estados recebidos por cubo; a codificação delta usa um bit para "sem mudança", menos bits para diferenças pequenas e uma predição balística em ponto fixo que acertou cerca de 90% das vezes dentro da resolução de quantização [F: fiedler2018vr]. O autor estima o ganho da delta real em "another order of magnitude" ao custo de muita complexidade, e recomenda usá-la apenas se necessário [F: fiedler2015statesync].

### Confirmação de pacotes sobre UDP

A baseline confirmada exige saber quais pacotes chegaram. O esquema descrito por Fiedler usa, por pacote, `sequence` (16 bits), `ack` (sequência mais recente recebida do outro lado) e `ack_bits` (32 bits, em que o bit n ligado confirma o pacote `ack − n`); cada confirmação é repetida em até 32 pacotes seguintes, então a perda de um pacote raramente apaga a informação [F: fiedler2016reliable]. O autor nota que ausência de ack não prova perda (o ack pode ter se perdido), mas que isso é extremamente raro [F: fiedler2016reliable]. Ver `rtm.net.ordering-and-reliability`.

### Alternativa: máscara de estado com reenvio seletivo (TRIBES)

O TRIBES não codifica diferenças numéricas; cada objeto tem uma *State Mask* em que cada bit representa um grupo de estado (posição e velocidade, rotação, animação; objetos típicos têm mais de 20 bits), e só os grupos com bit ligado são escritos no pacote [F: frohnmayer2000tribes]. Se o pacote é notificado como perdido, os bits são religados, exceto quando um pacote posterior já levou uma versão mais nova do mesmo estado, porque só a versão mais recente é garantida [F: frohnmayer2000tribes]. É uma forma de delta por campo, com reparo por notificação em vez de por baseline. [I]

## Requisitos e pressupostos

- Canal de confirmação bidirecional sobre UDP [F: fiedler2015statesync] [F: fiedler2016reliable].
- Memória no emissor para o histórico de estados enviados por receptor (Quake 3: 32 por cliente) [F: sanglard2012quake3].
- Estado quantizado de forma idêntica nos dois lados, para que "sem mudança" seja exato em inteiros [F: fiedler2015compression]. [I]
- Um estado inicial conhecido por ambos (dummy zerado no Quake 3; flag de estado inicial em Fiedler) [F: sanglard2012quake3] [F: fiedler2015compression].

## Vantagens e limitações

Vantagem: redução de banda de uma a duas ordens de grandeza em estado estacionário (de Mbit/s para cerca de 15 kbit/s no experimento) [F: fiedler2015compression]; reparo implícito de perdas sem retransmissão [F: sanglard2012quake3].

Trade-off memória, CPU e banda: cada cliente exige um histórico de snapshots (memória) e uma comparação campo a campo por frame (CPU) para economizar banda; a janela de histórico limita quão antiga pode ser a baseline antes de cair para atualização completa (32 no Quake 3; cerca de meio segundo com offset de 5 bits em Fiedler) [F: sanglard2012quake3] [F: fiedler2015statesync]. Sob perda alta, a baseline envelhece e o ganho cai, até o limite de atualizações completas. [I] A complexidade de implementação é o custo que Fiedler mais enfatiza [F: fiedler2015statesync].

## Alternativas e comparações

| Estratégia | Baseline | Reparo de perda | Custo principal |
|---|---|---|---|
| Delta contra último snapshot confirmado (Quake 3) [F: sanglard2012quake3] | snapshot inteiro | próximo delta inclui mudanças antigas | memória por cliente |
| Delta por objeto com offset (Fiedler) [F: fiedler2015statesync] | por objeto | volta a absoluto se base velha | rastreamento por objeto |
| State mask com religamento de bits (TRIBES) [F: frohnmayer2000tribes] | nenhuma; só "mais recente" | bits reenviados se não superados | sem compressão numérica |
| Quantização sem delta [F: fiedler2015compression] | nenhuma | não necessário | banda maior em repouso |

## Métricas e métodos de avaliação

Bits médios por objeto por campo após delta (26,1 e 23,3 no experimento) [F: fiedler2015compression]; banda em estado estacionário e em movimento intenso; taxa de acerto da predição (90% em VR) [F: fiedler2018vr]; memória por cliente [F: sanglard2012quake3].

## Exemplo técnico independente de domínio

```
emissor, por receptor r:
    historico[r] = anel de N snapshots enviados, indexado por seq
    confirmado[r] = seq do último snapshot que r confirmou (ou nenhum)

enviar_snapshot(r, atual):
    base = historico[r][confirmado[r]] se confirmado[r] dentro da janela senão SNAPSHOT_ZERO
    msg = {seq: atual.seq, base_seq: base.seq}
    para cada objeto o em atual:
        se quantizar(atual[o]) == quantizar(base[o]): escrever_bit(0); continuar
        escrever_bit(1); escrever_delta(quantizar(atual[o]) - quantizar(base[o]))   # faixas pequenas em menos bits
    historico[r][atual.seq] = atual
    enviar(msg)

ao_receber_ack(r, seq): confirmado[r] = max(confirmado[r], seq)

receptor:
    base = snapshots[msg.base_seq] (ou SNAPSHOT_ZERO); novo = copia(base)
    para cada objeto: se bit == 1: novo[o] = base[o] + ler_delta()
    snapshots[msg.seq] = novo; enviar ack(msg.seq) com ack_bits dos 32 anteriores
```

## Relações com outros conceitos

Parte de `rtm.sync.state-replication`; complementa `rtm.sync.snapshot-interpolation` (baseline por snapshot) e `rtm.sync.state-synchronization` (baseline por objeto). Depende do esquema de confirmação em `rtm.net.ordering-and-reliability` e de UDP (`rtm.proto.udp`). A distinção entre estado "mais recente" e mensagens garantidas é o tema de `rtm.rel.delivery-semantics`.

## Lacunas e questões abertas

- Sanglard menciona `MSG_WriteDeltaEntity` ora em `snapshot.c`, ora em `msg.c`; o código-fonte do Quake 3 não foi aberto para conferir.
- Os totais finais em kbit/s de Fiedler após cada etapa estão em vídeos e gráficos, não no texto; só os valores citados no texto foram usados.
- Não encontramos avaliação revisada por pares comparando delta por snapshot e delta por objeto.
- O PDF do TRIBES não traz data; ano inferido.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| sanglard2012quake3 | tecnico | 2026-10-29 |
| fiedler2015compression | tecnico | 2026-10-29 |
| fiedler2015statesync | tecnico | 2026-10-29 |
| fiedler2018vr | tecnico | 2026-10-29 |
| fiedler2016reliable | tecnico | 2026-10-29 |
| frohnmayer2000tribes | tecnico | 2026-10-29 |
