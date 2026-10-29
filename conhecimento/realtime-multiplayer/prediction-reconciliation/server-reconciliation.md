---
id: rtm.pred.server-reconciliation
titulo: Server reconciliation
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gambetta2014prediction, gambetta2014demo, bernier2001latency, valve2026source, fiedler2010networking, liu2022survey, wikipedia2026csp]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: depende-de, alvo: rtm.pred.client-side-prediction }
  - { tipo: depende-de, alvo: rtm.net.ordering-and-reliability }
  - { tipo: complementa, alvo: rtm.pred.entity-interpolation }
  - { tipo: complementa, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.sync.state-synchronization }
  - { tipo: relacionado-a, alvo: rtm.pred.comparison }
termos: [server reconciliation, sequence number, last acknowledged input, replay, rewind and replay, misprediction, correction smoothing]
---

# Server reconciliation

## Definição e terminologia

Server reconciliation é o procedimento pelo qual um cliente que faz client-side prediction incorpora um estado autoritativo vindo do servidor sem desfazer o que já previu: ele aceita o estado recebido, descarta as entradas que o servidor já processou e reaplica, sobre esse estado, as entradas ainda não confirmadas [F: gambetta2014prediction]. O termo é de Gambetta; Fiedler descreve o mesmo mecanismo em QuakeWorld como "rewinds and replays" dos últimos frames do jogador local [F: fiedler2010networking]; Bernier o descreve como reexecutar a janela de comandos a partir do "último estado reconhecido" [F: bernier2001latency].

O que não é: reconciliação não é um protocolo de consenso nem resolve conflitos entre vários clientes; só concilia a visão local do jogador com a autoridade do servidor para a entidade que ele controla [I]. Também não é a mesma coisa que a correção suavizada (*smoothing*), que é um tratamento visual aplicado quando a reconciliação ainda deixa um resíduo de erro [I].

## Problema que resolve

Client-side prediction sozinha falha quando há entradas em trânsito. Gambetta demonstra com lag de 250 ms, 100 ms por casa e duas pressões seguidas da tecla: em t = 250 ms chega do servidor "x = 11", mas o cliente já previu x = 12 e, por obedecer ao servidor, recua para 11; em t = 350 ms chega "x = 12" e o personagem avança de novo. O jogador vê andar duas casas, parar, recuar uma, parar e avançar, o que o autor considera inaceitável [F: gambetta2014prediction]. A causa é que o cliente vê o mundo no presente enquanto cada atualização do servidor descreve um passado em que nem todas as entradas já enviadas haviam sido processadas [F: gambetta2014prediction].

## Fundamentos e funcionamento

Mecanismo descrito por Gambetta [F: gambetta2014prediction]:

1. O cliente atribui a cada entrada um número de sequência crescente (`#1`, `#2`, ...).
2. O cliente guarda uma cópia de cada entrada enviada.
3. Cada estado enviado pelo servidor inclui o número da última entrada processada para aquele cliente ("based on what I've seen up to your request #1, your position is x = 11").
4. Ao receber o estado, o cliente descarta as entradas com número menor ou igual ao confirmado, substitui seu estado pelo recebido e reaplica, em ordem, as entradas restantes.

No exemplo do autor: em t = 250 ms chega `{x = 11, último = #1}`; o cliente descarta #1, mantém #2, define x = 11 e reaplica #2, obtendo x = 12, sem salto. Em t = 350 ms chega `{x = 12, último = #2}`; nada resta a reaplicar [F: gambetta2014prediction].

Descrições equivalentes nas outras fontes:

- Bernier: "the last acknowledged movement from the server is used as a starting point" e "the client will most often end up running the same commands over and over again"; com 50 fps e 100 ms de RTT, a janela tem cerca de 5 comandos [F: bernier2001latency].
- Fiedler: o cliente mantém buffer circular de estados e entradas; ao chegar uma correção (atrasada pela rede), descarta os estados mais antigos que ela, aplica o estado corrigido e reexecuta as entradas guardadas até o presente, mantendo o resto do mundo fixo [F: fiedler2010networking].
- Valve: quando o snapshot chega, o cliente compara a posição real com a prevista; se houver diferença há erro de predição e o servidor tem a palavra final [F: valve2026source].

### Misprediction e correção

Se a predição estava errada por motivo real (colisão com outro jogador, dano, intervenção do servidor), a reaplicação das entradas pendentes parte do estado corrigido e o resultado difere do que estava na tela. Gambetta observa que mesmo com determinismo total e sem trapaça a predição pode não bater com o servidor quando há vários clientes, porque o servidor incorpora entradas de outros jogadores que o cliente desconhecia [F: gambetta2014prediction]. A taxonomia de Liu, Xu e Claypool descreve o mesmo custo: quando o estado do cliente é "inevitably fixed to align with the server game state", a correção é perceptível e pode incomodar [F: liu2022survey, §4.2].

### Smoothing de correção

A documentação da Valve descreve que a correção é distribuída no tempo pela variável `cl_smoothtime` (valor padrão não informado no texto) e que `cl_smooth 0` desliga a suavização [F: valve2026source]. A Wikipedia (secundária) descreve a prática geral: diferenças pequenas são interpoladas aos poucos; diferenças grandes são aplicadas de uma vez [F: wikipedia2026csp]. Nenhuma das fontes primárias dá limiares numéricos para "pequeno" e "grande"; isso fica como lacuna [I].

### Papel dos números de sequência

Os números de sequência fazem três coisas: identificam até onde o servidor processou (acknowledgement cumulativo), permitem descartar o buffer de forma monotônica e dão ao servidor um meio de detectar entradas duplicadas ou fora de ordem [I, com base em gambetta2014prediction]. Isso independe do transporte: sobre UDP o cliente pode reenviar entradas não confirmadas em cada pacote; sobre transporte confiável e ordenado a numeração continua necessária para a reconciliação, ainda que a entrega esteja garantida [I]. Ver `rtm.net.ordering-and-reliability`.

## Requisitos e pressupostos

- Tudo que `rtm.pred.client-side-prediction` exige: servidor autoritativo, código de simulação compartilhado e determinismo suficiente [F: gambetta2014prediction].
- **Reaplicação idempotente de efeitos.** Como comandos são reexecutados, efeitos colaterais (som, partículas) devem disparar só na primeira execução [F: bernier2001latency].
- **Estado de simulação separável.** O cliente precisa conseguir substituir o estado da própria entidade pelo estado do servidor e re-simular só ela, "mantendo o resto do mundo fixo" [F: fiedler2010networking]. Estado só do cliente precisa de uma janela deslizante própria [F: bernier2001latency].
- **Custo de CPU proporcional à janela.** A cada atualização do servidor o cliente re-simula até N comandos, com N aproximadamente igual a `taxa_de_frames × RTT` [F: bernier2001latency, exemplo de 5 comandos]. Com 60 fps e 300 ms de RTT isso dá cerca de 18 re-simulações por atualização recebida [I].

## Vantagens e limitações

Vantagens:

- Elimina o "serrilhado" de posição que a predição sozinha produz quando há entradas em trânsito [F: gambetta2014prediction].
- Na demo de Gambetta, ativar reconciliação junto com predição faz o movimento próprio ficar quase instantâneo mesmo com 250 ms ou 500 ms de lag; uma marca cinza mostra a última posição confirmada pelo servidor [F: gambetta2014demo].
- Mantém o servidor autoritativo: o cliente nunca "vence" o servidor, só antecipa [F: gambetta2014prediction].

Limitações:

- Só vale para a entidade do próprio jogador; os outros jogadores continuam exigindo interpolação [F: gambetta2014demo].
- Mispredições reais ainda causam salto; o smoothing mitiga, mas não elimina [F: valve2026source].
- Exige buffer e re-simulação, cujo custo cresce com RTT e taxa de frames [F: bernier2001latency].
- Casos irreversíveis (morte, consumo de item) exigem tratamento especial: Gambetta recomenda mostrar efeitos imediatos (sangue, número de dano) mas só alterar a vida quando o servidor confirmar [F: gambetta2014prediction].

## Alternativas e comparações

| Estratégia ao receber estado autoritativo | Resultado visual | Fonte |
|---|---|---|
| Aceitar estado e descartar predição (sem reconciliação) | Recuo e avanço repetidos quando há entradas em trânsito | [F: gambetta2014prediction] |
| Ignorar o servidor até divergir muito | Inconsistência acumulada; servidor deixa de ser autoridade prática | [I] |
| Reconciliação (aceitar + reaplicar pendentes) | Sem salto quando a predição estava certa; salto só em mispredição real | [F: gambetta2014prediction] |
| Reconciliação + smoothing | Mispredição diluída ao longo de `cl_smoothtime` | [F: valve2026source] |

## Métricas e métodos de avaliação

- Número de comandos pendentes por atualização (proxy de custo de CPU e de RTT) [I].
- Magnitude do erro residual após reconciliação, medida como distância entre o estado re-simulado e o que estava na tela; a Valve expõe `cl_showerror` para isso [F: valve2026source].
- Frequência de mispredições por minuto em cenários com N jogadores, já que colisões entre jogadores são a fonte típica de divergência [I, com base em fiedler2010networking].
- Emulação de latência e perda para reproduzir os cenários de Gambetta (250 ms, 500 ms) [F: gambetta2014demo]; ver `rtm.perf.network-emulation`.

## Exemplo técnico independente de domínio

```
# Cliente
ao receber estado_servidor {estado, ultimo_seq}:
    pendentes.remover_ate(ultimo_seq)          # descarta confirmados
    estado_local <- estado                     # aceita autoridade
    para cmd em pendentes (ordem crescente de seq):
        estado_local <- simular(estado_local, cmd, efeitos = desligados)
    if distancia(estado_local, estado_na_tela) > 0:
        iniciar_smoothing(estado_na_tela -> estado_local, duracao = T_smooth)

# Servidor
ao receber cmd {seq, dt, entrada} do cliente c:
    if seq <= ultimo_seq[c]: ignorar           # duplicado ou fora de ordem
    estado[c] <- simular(estado[c], cmd)
    ultimo_seq[c] <- seq
a cada tick:
    para cada cliente c: enviar {estado, ultimo_seq[c]}
```

Diagrama de sequência (lag 250 ms, duas entradas em t = 0 e t = 100):

```
t=0    C: cmd#1 -> x=11 local            ----> S
t=100  C: cmd#2 -> x=12 local            ----> S
t=250  S processa #1, envia {x=11, ult=1}
t=350  S processa #2, envia {x=12, ult=2}
t=500  C recebe {x=11, ult=1}: descarta #1, x=11, reaplica #2 -> x=12 (sem salto)
t=600  C recebe {x=12, ult=2}: descarta #2, x=12, nada a reaplicar
```

Os instantes seguem o exemplo de Gambetta, com os tempos de chegada ao cliente somando a latência de volta [I, com base em gambetta2014prediction].

## Relações com outros conceitos

Depende de `rtm.pred.client-side-prediction` (não existe sem o buffer de predição), de `rtm.arch.authoritative-server` e de `rtm.net.ordering-and-reliability` (números de sequência e acknowledgements). Complementa `rtm.pred.entity-interpolation` (que trata as outras entidades) e `rtm.pred.lag-compensation`. Relaciona-se com `rtm.sync.state-synchronization`, onde a mesma ideia de estado autoritativo mais correção aparece na sincronização de física. Síntese em `rtm.pred.comparison`.

## Lacunas e questões abertas

- Nenhuma fonte primária verificada dá limiares numéricos para distinguir correção suave de correção imediata, nem o valor padrão de `cl_smoothtime`; as páginas da Valve estavam inacessíveis (HTTP 403) e o texto foi verificado em cópia integral de terceiros.
- Interação entre reconciliação e física com estado contínuo (velocidades, contatos) não é tratada por Gambetta; Fiedler cobre isso na série sobre física em rede, não aberta nesta sessão (ver `rtm.sync.state-synchronization`).
- Reconciliação em simulações não determinísticas por construção (ponto flutuante heterogêneo, aleatoriedade) exige semear RNG e normalizar aritmética; as fontes não detalham [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gambetta2014prediction | tecnico | 2026-10-29 |
| gambetta2014demo | tecnico | 2026-10-29 |
| bernier2001latency | tecnico (artigo GDC 2001; original 403, verificado em cópia integral) | 2026-10-29 |
| valve2026source | fornecedor (original 403, verificado em cópia integral) | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
| liu2022survey | academico | 2026-10-29 |
| wikipedia2026csp | secundario | 2026-10-29 |
