---
id: rtm.rt.realtime-systems
titulo: Sistemas de tempo real (hard, firm, soft) e tempo real em comunicação interativa
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [liu1973scheduling, whittaker2026liu, kernel2026deadline, wikipedia2026realtime, stankovic1988misconceptions, shin1994realtime, claypool2006report, claypool2006latency, gambetta2014client, fiedler2010what, fiedler2014lockstep, riot2020valorant, rfc2681, rfc6202]
relacoes:
  - { tipo: complementa, alvo: rtm.rt.communication-patterns }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: relacionado-a, alvo: rtm.net.jitter }
  - { tipo: relacionado-a, alvo: rtm.perf.qoe-thresholds }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [tempo real, hard real-time, firm real-time, soft real-time, deadline, rate-monotonic scheduling, earliest deadline first, tick, tempo real interativo]
---

# Sistemas de tempo real (hard, firm, soft) e tempo real em comunicação interativa

## Definição e terminologia

Um sistema de **tempo real** é aquele cuja correção depende não só do resultado lógico, mas do instante em que o resultado é produzido: existe um **deadline** (prazo) associado a cada tarefa ou resposta. A classificação consolidada na literatura de sistemas embarcados distingue três classes pela consequência de perder o prazo [F: wikipedia2026realtime, que atribui a classificação a Kopetz, *Real-Time Systems*, 1997, pp. 12-14; o livro de Kopetz não foi aberto nesta sessão]:

- **hard real-time**: perder um deadline é falha total do sistema;
- **firm real-time**: perdas infrequentes são toleráveis, mas o resultado atrasado tem utilidade zero;
- **soft real-time**: a utilidade do resultado degrada progressivamente após o deadline.

O artigo seminal de Liu e Layland usa o termo "hard-real-time environment" para o cenário em que tarefas periódicas de controle precisam de "guaranteed service", isto é, prazos que devem ser cumpridos sempre [F: liu1973scheduling; whittaker2026liu]. Os artigos de Stankovic (1988) e Shin e Ramanathan (1994), frequentemente citados pelas definições de "real-time computing", tiveram apenas o registro bibliográfico verificado nesta sessão (ver Lacunas) [F: stankovic1988misconceptions; shin1994realtime].

O que **não** é tempo real: "rápido" não é sinônimo de tempo real. Um sistema pode ter latência média baixa e ainda assim não ser de tempo real se não houver limite garantido (ou ao menos estatisticamente caracterizado) para o pior caso. A distinção central é **previsibilidade** versus velocidade média [I].

Em comunicação interativa (voz, vídeo, jogos, colaboração), "tempo real" é usado num sentido diferente: não há escalonador que garanta prazos, e sim um **orçamento de atraso fim a fim** dentro do qual a interação permanece aceitável para o usuário. Esse uso corresponde, na taxonomia acima, a **soft** ou **firm** real-time [I].

## Problema que resolve

A disciplina de tempo real responde à pergunta: dado um conjunto de tarefas com períodos, tempos de execução e prazos, é possível garantir que todos os prazos sejam cumpridos, e com que algoritmo de escalonamento? Em comunicação interativa a pergunta muda: dado que a rede não garante prazo nenhum, como projetar o sistema para que a maioria das mensagens chegue dentro de um orçamento, e o que fazer com as que não chegam [I].

## Fundamentos e funcionamento

### Modelo de tarefas periódicas (sistemas embarcados)

Liu e Layland modelam tarefas periódicas independentes com período `T_i`, tempo de execução constante `C_i` e deadline igual ao fim do período; tarefas aperiódicas não são tratadas como de tempo real [F: whittaker2026liu]. A **utilização** do processador é `U = Σ C_i / T_i`.

### Classes por função de utilidade

Uma forma de unificar as três classes é descrever a utilidade do resultado como função do tempo de conclusão [I]:

```
utilidade
  ^
  |-----------+              hard:  utilidade -> falha catastrófica após d
  |           |              firm:  utilidade = 0 após d
  |           \_____         soft:  utilidade decresce após d
  +-----------d--------> tempo de conclusão
```

### Tempo real em comunicação interativa

Em jogos e colaboração, a métrica que domina é a **latência de ida e volta** entre a ação do usuário e a observação do efeito. Gambetta assume 50 ms de ida como melhor caso e cita que atrasos de 100 a 500 ms são comuns, e que "a lag of half a second isn't just noticeable, it actually makes the game unplayable" [F: gambetta2014client]. Fiedler relata que o projeto original de Quake (1996) visava latências "< 200ms", enquanto jogadores de modem viam "300+ ms" [F: fiedler2010what]. Em um título competitivo recente, o servidor roda em passo fixo de 128 ticks por segundo e a meta declarada é 35 ms de ping para 70% da base de jogadores [F: riot2020valorant].

Isso configura um sistema **soft real-time com deadlines por classe de ação**: Claypool e Claypool propõem categorizar ações por **precisão** e **deadline** e resumem limiares de latência por perspectiva: avatar em primeira pessoa, 100 ms; avatar em terceira pessoa, 500 ms; omnipresente (estratégia, simulação), 1000 ms [F: claypool2006report, Tabela 1; claypool2006latency]. Os próprios autores registram que "the exact threshold depends upon the game and to some extent the player" [F: claypool2006report, §6].

### O "tick" como período

Servidores de jogos e simuladores adotam um **tick** (passo fixo) que faz papel análogo ao período de uma tarefa de tempo real: toda a lógica de um quadro precisa caber no intervalo, senão o sistema acumula atraso. Fiedler descreve o mecanismo de "catch-up" de até 4 quadros por quadro de renderização para evitar a "spiral of death" quando as entradas chegam agrupadas [F: fiedler2014lockstep]. [I] Essa é a tradução prática de um deadline soft: perder o prazo de um tick degrada, mas não quebra, o sistema.

## Algoritmos e modelos relevantes

- **Rate-monotonic (RM)**: prioridade fixa, inversamente proporcional ao período; ótimo entre os escalonadores de prioridade fixa. O limite inferior de utilização garantida para `m` tarefas é `m(2^(1/m) − 1)`, que tende a `ln 2 ≈ 0,693` quando `m` cresce [F: whittaker2026liu; liu1973scheduling, cujo resumo diz "may be as low as 70 percent for large task sets"].
- **Earliest Deadline First (EDF, "deadline driven")**: prioridade dinâmica pelo prazo mais próximo; atinge utilização de 100% e, se existe algum escalonamento viável, existe um viável por EDF [F: whittaker2026liu].
- **Escalonamento misto**: as `k` tarefas mais frequentes em RM e as demais em EDF, motivado pelo hardware da época [F: whittaker2026liu].
- Implementação em sistema operacional de propósito geral: a classe `SCHED_DEADLINE` do kernel Linux implementa EDF com Constant Bandwidth Server, parametrizada por `runtime`, `deadline` e `period`, cita Liu e Layland como referência e usa como teste de admissão `Σ runtime/period ≤ 1` em uniprocessador quando `D_i = P_i` [F: kernel2026deadline]. A documentação do kernel afirma ainda que o controle de admissão padrão limita a banda a 95% por CPU (`950000/1000000`) [F: kernel2026deadline].

## Requisitos e pressupostos

Para garantias hard: tempos de execução de pior caso conhecidos, tarefas independentes, períodos fixos, sem bloqueios imprevisíveis [F: whittaker2026liu]. Nenhum desses pressupostos vale para a Internet pública: o atraso de rede não tem limite superior conhecido e o RFC 2681 observa que o valor mínimo do atraso indica apenas propagação e transmissão, enquanto o restante é variável [F: rfc2681, §1.1]. Daí o tempo real interativo ser necessariamente soft/firm [I].

## Vantagens e limitações

| Classe | Garantia | Custo | Onde aparece em sistemas interativos |
|---|---|---|---|
| hard | determinística | análise de pior caso, hardware dedicado | não se aplica fim a fim; pode existir localmente (áudio, controle) [I] |
| firm | resultado atrasado descartado | precisa de política de descarte | pacote de estado que chegou depois do próximo: descartado [I] |
| soft | degradação gradual | precisa de métricas de QoE | latência de entrada, interpolação, colaboração [I] |

Limitação central da transposição: a literatura de escalonamento garante prazos **dentro de um nó**; entre nós, o canal introduz atraso, variação de atraso e perda sem contrato de prazo [I].

## Alternativas e comparações

Comparação entre "tempo real" embarcado e interativo [I]:

| Aspecto | Embarcado (hard) | Comunicação interativa (soft/firm) |
|---|---|---|
| Objeto do prazo | tarefa local | mensagem fim a fim |
| Falha ao perder prazo | catastrófica | degradação perceptível |
| Ferramenta | escalonador, análise de utilização | orçamento de latência, buffers, predição |
| Métrica | cumprimento de deadlines | latência, jitter, perda, QoE |
| Referência | Liu e Layland 1973 | Claypool 2006, Gambetta, Fiedler |

## Métricas e métodos de avaliação

Para o lado embarcado: taxa de deadlines perdidos e utilização `U`. Para o lado interativo: atraso de ida e volta medido conforme RFC 2681 [F: rfc2681], limiares por classe de ação [F: claypool2006report] e métricas de QoE do domínio (ver `rtm.perf.metrics` e `rtm.perf.qoe-thresholds`).

## Exemplo técnico independente de domínio

Laço de simulação com tick fixo e tratamento soft de deadline:

```
TICK = 1/60 s
acumulador = 0
loop:
    agora = relogio_monotonico()
    acumulador += agora - anterior; anterior = agora
    passos = 0
    while acumulador >= TICK and passos < MAX_CATCHUP:   # ex.: 4
        simular(TICK); acumulador -= TICK; passos += 1
    if passos == MAX_CATCHUP:                             # deadline soft perdido
        acumulador = 0; registrar_metrica("tick_overrun")
    renderizar(interpolacao = acumulador / TICK)
```

O limite `MAX_CATCHUP` segue a recomendação de Fiedler para evitar a espiral de atraso [F: fiedler2014lockstep]. [I] Um sistema hard não poderia "zerar o acumulador"; um soft pode, ao custo de um salto perceptível.

## Relações com outros conceitos

Depende de `rtm.net.latency` (a latência é a variável que define o deadline fim a fim) e complementa `rtm.rt.communication-patterns` (o padrão de comunicação determina o atraso mínimo alcançável). Relaciona-se a `rtm.net.jitter` (variação de atraso é o que os buffers absorvem), a `rtm.arch.deterministic-lockstep` (arquitetura em que o tick vira deadline firm) e aos documentos de avaliação `rtm.perf.metrics` e `rtm.perf.qoe-thresholds`.

## Lacunas e questões abertas

- As definições hard/firm/soft foram verificadas apenas em fonte secundária (Wikipedia citando Kopetz 1997); o livro de Kopetz e os artigos de Stankovic (1988) e Shin e Ramanathan (1994) não foram abertos (acesso bloqueado); apenas registros Crossref foram conferidos. **Não verificado** no texto original.
- O PDF de Liu e Layland foi baixado, mas a extração de texto falhou (fonte com codificação não padrão); os resultados foram conferidos pelo resumo técnico de Whittaker e pelo abstract exposto na busca. Confirmar citações literais no original.
- Faltam evidências empíricas de limiares de latência para colaboração (edição conjunta, quadro branco) comparáveis às de jogos; Claypool cobre apenas gêneros de jogo.
- Em que medida a terminologia firm/soft é usada na literatura de redes para pacotes atrasados (descarte por buffer de jitter) merece levantamento próprio.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| liu1973scheduling | academico (registro Crossref; PDF baixado, texto não extraível) | 2026-10-29 |
| whittaker2026liu | secundario | 2026-10-29 |
| kernel2026deadline | fornecedor | 2026-10-29 |
| wikipedia2026realtime | secundario | 2026-10-29 |
| stankovic1988misconceptions | academico (apenas registro Crossref) | 2026-10-29 |
| shin1994realtime | academico (apenas registro Crossref) | 2026-10-29 |
| claypool2006report | academico | 2026-10-29 |
| claypool2006latency | academico (registro Crossref) | 2026-10-29 |
| gambetta2014client | tecnico | 2026-10-29 |
| fiedler2010what | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| riot2020valorant | tecnico | 2026-10-29 |
| rfc2681 | normativo | 2026-10-29 |
| rfc6202 | normativo (informativo) | 2026-10-29 |
