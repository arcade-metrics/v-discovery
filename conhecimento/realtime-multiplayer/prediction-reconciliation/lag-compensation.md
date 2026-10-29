---
id: rtm.pred.lag-compensation
titulo: Lag compensation
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gambetta2014lagcomp, bernier2001latency, valve2026source, liu2022survey, lee2015evaluation, lee2017corner, lee2018advanced]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: depende-de, alvo: rtm.pred.entity-interpolation }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: complementa, alvo: rtm.pred.client-side-prediction }
  - { tipo: complementa, alvo: rtm.pred.server-reconciliation }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.net.clock-synchronization }
  - { tipo: relacionado-a, alvo: rtm.pred.comparison }
termos: [lag compensation, time warp, rewind, position history, shot around the corner, command execution time, rollback limit]
---

# Lag compensation

## Definição e terminologia

Lag compensation é a técnica em que o servidor autoritativo, ao processar uma ação instantânea de um cliente (tipicamente um disparo), reconstrói o estado do mundo tal como aquele cliente o via no instante da ação, avalia a ação contra esse estado passado e depois restaura o presente [F: gambetta2014lagcomp; F: bernier2001latency]. Bernier resume: "You can think of lag compensation as taking a step back in time, on the server" [F: bernier2001latency].

Terminologia nas fontes:

- **Time warp**: nome que a taxonomia de Liu, Xu e Claypool dá à técnica ("rolls back game state to when the player action occurred on the client, applies the action, then rolls the game state forward to the current time"), notando que ela "is often called, somewhat confusingly, latency compensation or lag compensation" e às vezes "simply called rollback" [F: liu2022survey, §4.3.1.1]. A taxonomia atribui a origem do time warp a Jefferson (1985), no contexto de simulação distribuída de eventos discretos [F: liu2022survey, §4.3.1.1].
- **Lag compensation**: nome usado por Bernier, pela Valve e por Gambetta [F: bernier2001latency; F: valve2026source; F: gambetta2014lagcomp].
- **Rewind / unlag**: termos coloquiais; não aparecem como definição nas fontes verificadas [I].

O que não é: não é client-side prediction (que roda no cliente) nem reconciliação; é uma técnica do servidor. Também não é "rollback netcode" de jogos de luta no sentido de lockstep com re-simulação em todos os pares, embora a taxonomia agrupe ambos sob time warp [F: liu2022survey, §4.3.1.1; I].

## Problema que resolve

Com client-side prediction e entity interpolation, o jogador vê a si mesmo no presente e os outros no passado (cerca de 100 ms no exemplo de Gambetta) [F: gambetta2014lagcomp]. Um tiro perfeitamente alinhado na tela erra no servidor, porque a mira estava sobre a posição de 100 ms antes; Gambetta usa o exemplo do sniper e afirma que "It would be much worse to miss an unmissable shot!" [F: gambetta2014lagcomp]. Bernier descreve a situação anterior à técnica: o jogador precisava mirar à frente do alvo conforme a própria latência; com 100 ms de latência e alvo a 500 unidades/s, mirar 50 unidades adiante [F: bernier2001latency]. A documentação da Valve diz que o problema é que um tiro dado no tempo do cliente chega ao servidor quando o alvo já saiu da posição [F: valve2026source].

Lee e Chang (2015) mediram em Counter-Strike: Global Offensive que lag compensation e tick rate mais alto aumentam significativamente o desempenho dos jogadores [F: lee2015evaluation].

## Fundamentos e funcionamento

### Passos no servidor

Bernier descreve o algoritmo executado antes de rodar o comando do jogador [F: bernier2001latency]:

1. Calcular uma latência razoavelmente precisa do jogador.
2. Buscar, no histórico do servidor para aquele jogador, a atualização recebida pouco antes de ele emitir o comando.
3. Mover os outros jogadores para trás, até onde estavam no momento em que o comando foi criado, levando em conta a latência e a interpolação usada pelo cliente naquele frame (`lerp_msec` do usercmd).
4. Executar o comando (disparos, raycasts) contra as posições antigas.
5. Restaurar os jogadores às posições atuais.

A Valve dá a fórmula do instante-alvo: "Command Execution Time = Current Server Time - Packet Latency - Client View Interpolation" [F: valve2026source]. Só os outros jogadores são movidos para trás; o servidor guarda o histórico de posições por 1 segundo [F: valve2026source]. Bernier acrescenta que às vezes é preciso recuar também estado como vivo/morto ou agachado [F: bernier2001latency].

Gambetta descreve a versão conceitual: o cliente envia o evento com "the exact timestamp of your shot, and the exact aim of the weapon"; como o servidor recebe todos os inputs com timestamp, ele pode "reconstruct the world at any instant in the past", inclusive como o mundo aparecia para aquele cliente [F: gambetta2014lagcomp]. Gambetta não detalha o armazenamento do histórico [F: gambetta2014lagcomp].

### Histórico de posições

O servidor mantém, por jogador, uma série temporal de poses (posição, orientação, hitboxes, flags relevantes). A profundidade do histórico limita o rewind: 1 segundo na Valve [F: valve2026source]. A memória cresce com `jogadores × tickrate × profundidade × tamanho da pose`; com 66,67 ticks/s (timestep de 15 ms, padrão do Source) e 1 s, são cerca de 67 poses por jogador [F: valve2026source, para os números; I, para o cálculo].

### Interação com a interpolação

A fórmula inclui a interpolação do cliente; a Valve afirma que desativá-la no cliente pode gerar resultados indesejados, e que o servidor "sabe" da interpolação de entidades do cliente e corrige esse erro [F: valve2026source]. Bernier fundamenta: o recuo precisa considerar latência e atraso de interpolação, porque o cliente via os alvos no passado por ambos os motivos [F: bernier2001latency].

### Precisão

A Valve observa que pequenas diferenças de tempo, de poucos milissegundos, podem causar erros de vários centímetros em alvos rápidos, de modo que o acerto não é pixel-perfect [F: valve2026source]. A estimativa de latência é parte do algoritmo [F: bernier2001latency]; ver `rtm.net.clock-synchronization`.

### Limites de rewind

Lee e Chang (2017) investigaram como latência e velocidade de movimento afetam as distâncias de rollback e concluíram que um limite de 250 ms para a compensação é razoável para velocidade de movimento de 4 m/s; constataram também que jogadores experientes percebem com razoável precisão a frequência com que são atingidos "ao redor da esquina" [F: lee2017corner]. A taxonomia reporta que Lee e Chang (2018) descrevem como FPS comerciais limitam até onde o servidor rebobina e propõem um "advanced time warp" em que o cliente identifica que está seguro (usando seu tempo local) e impede o rollback [F: liu2022survey, §4.3.1.1; metadados em lee2018advanced]. O texto completo de Lee e Chang (2018) não foi aberto nesta sessão.

## Requisitos e pressupostos

- Servidor autoritativo que recebe comandos com timestamp ou número de tick [F: gambetta2014lagcomp].
- Estimativa confiável da latência de cada cliente e do seu atraso de interpolação (enviado no comando, como `lerp_msec`) [F: bernier2001latency].
- Histórico de estado por entidade com profundidade igual ao rewind máximo [F: valve2026source].
- Ação de resolução instantânea (hitscan). Bernier observa que projéteis autônomos colocam questões difíceis (em que tempo vivem, quanto recuar os outros) e que no Half-Life não recebem compensação [F: bernier2001latency].
- Decisão de design explícita: Bernier afirma que a decisão de implementar é do game designer, porque muda a sensação do jogo [F: bernier2001latency].

## Vantagens e limitações

Vantagens:

- O atirador acerta mirando diretamente no que vê, sem compensar a própria latência [F: bernier2001latency].
- Cada jogador recebe resposta completa às próprias ações; foi a escolha da Valve para Half-Life, Team Fortress e Counter-Strike, cujos benefícios superaram as inconsistências [F: bernier2001latency].
- Ganho mensurável de desempenho do jogador [F: lee2015evaluation].

Limitações e trade-offs de justiça:

- **"Shot around the corner" / atingido atrás da cobertura.** O alvo pode ser atingido depois de já ter se protegido, porque o servidor recuou sua hitbox para quando ainda estava exposto. Gambetta: "they may still be shot up to a few milliseconds after they took cover" e "It is somewhat unfair, but it's the most agreeable solution for everyone involved" [F: gambetta2014lagcomp]. Bernier: um jogador muito atrasado (cerca de 500 ms) pode acertar alguém que, para quem tem baixa latência, "may have darted around a corner" [F: bernier2001latency]. A Valve afirma que esse problema não tem solução geral, por causa da velocidade relativamente baixa dos pacotes [F: valve2026source]. A taxonomia descreve o mesmo artefato com o exemplo da Figura 12 [F: liu2022survey, §4.3.1.1].
- **Favorece quem tem mais latência**, no sentido de que o jogador atrasado tem seus tiros avaliados no passado dos outros [I, com base em bernier2001latency]. Bernier argumenta que, em FPS com campo de visão de cerca de 90 graus ou menos, o alvo normalmente não vê a mira, o que reduz a sensação de injustiça; em jogos onde se olha para um lado e se corre para outro (tanques), o caso é menos claro [F: bernier2001latency].
- **Rewind limitado**: além do limite (1 s na Valve; 250 ms sugerido por Lee e Chang 2017 para 4 m/s), o atirador volta a precisar compensar [F: valve2026source; F: lee2017corner].

### Relação com anti-cheat

A Valve explica por que o servidor não pode simplesmente aceitar um "hit" calculado pelo cliente: pacotes podem ser alterados no caminho por "cheat proxies" (man-in-the-middle), mesmo com VAC [F: valve2026source]. Lag compensation preserva a autoridade: o cliente só informa quando e para onde atirou; o servidor decide o acerto [F: gambetta2014lagcomp]. Interpretação: a superfície de abuso restante é o próprio timestamp e a latência reportada; um cliente que declara latência maior do que tem ganha rewind extra, o que é uma razão prática para o servidor medir a latência em vez de confiar no cliente e para limitar o rewind [I]. Ver `rtm.sec.cheating`.

## Alternativas e comparações

| Abordagem | Quem compensa | Justiça percebida | Fonte |
|---|---|---|---|
| Sem compensação (mirar à frente) | O jogador, manualmente | Mira não corresponde ao que se vê | [F: bernier2001latency] |
| Feedback de acerto (som de hit no Quake 3) | O jogador, com ajuda | Perde eficácia com latência alta ou oscilante | [F: bernier2001latency] |
| Lag compensation (time warp) | O servidor | "Shot around the corner" para o alvo | [F: gambetta2014lagcomp] |
| Advanced lag compensation (cliente sinaliza que está seguro) | Servidor + cliente | Proposta de Lee e Chang 2018, via survey | [F: liu2022survey] |
| Time delay (igualar latências) | Servidor, atrasando todos | Mais justo e consistente, mais lento | [F: liu2022survey, §4.3.1] |

## Métricas e métodos de avaliação

- Precisão de tiro e desempenho do jogador sob latência artificial, método de Lee e Chang (2015) [F: lee2015evaluation].
- Distância de rollback (quanto a hitbox foi recuada) em função de latência e velocidade, método de Lee e Chang (2017) [F: lee2017corner].
- Frequência percebida de "shot around the corner" em questionário, também em Lee e Chang (2017) [F: lee2017corner].
- Ferramentas de inspeção: a Valve expõe `sv_showimpacts 1` para mostrar hitboxes de cliente e servidor e `net_fakelag` para simular latência [F: valve2026source]. Ver `rtm.perf.network-emulation`.

## Exemplo técnico independente de domínio

```
# Servidor
historico[e] <- fila de (tick, pose) com profundidade = REWIND_MAX   # ex.: 1 s

a cada tick:
    para cada entidade e: historico[e].adicionar((tick_atual, pose(e)))

ao receber cmd de c com acao_instantanea:
    latencia <- estimar_latencia(c)                 # medida pelo servidor
    t_alvo <- tempo_servidor - latencia - interp_cliente(c)
    t_alvo <- max(t_alvo, tempo_servidor - REWIND_MAX)
    salvar <- {}
    para cada entidade e != c:
        salvar[e] <- pose(e)
        pose(e) <- interpolar(historico[e], t_alvo)  # inclui estado como agachado
    resultado <- resolver_acao(cmd)                  # raycast contra poses antigas
    para cada e em salvar: pose(e) <- salvar[e]
    aplicar(resultado)
```

Diagrama de sequência (latência 100 ms, interpolação 100 ms):

```
t=0    C vê alvo em P(t=-100) (interpolação), atira, envia {t=0, mira}
t=100  S recebe. t_alvo = 100 - 100 - 100 = -100. Rebobina alvo para P(-100).
       Raycast acerta. Restaura. Envia resultado.
t=200  C e alvo recebem "acerto". Se o alvo se cobriu entre t=-100 e t=100,
       ele é atingido já atrás da cobertura.
```

## Relações com outros conceitos

Depende de `rtm.arch.authoritative-server` (quem rebobina), de `rtm.pred.entity-interpolation` (o atraso de interpolação entra na fórmula) e de `rtm.net.latency`. Complementa `rtm.pred.client-side-prediction` e `rtm.pred.server-reconciliation`, formando com elas o conjunto descrito por Gambetta. Relaciona-se com `rtm.sec.cheating` (preserva a autoridade; limites de rewind contêm abuso de latência) e com `rtm.net.clock-synchronization` (estimativa de latência e instante da ação). Síntese em `rtm.pred.comparison`.

## Lacunas e questões abertas

- Páginas da Valve retornaram HTTP 403; texto verificado em cópia integral de terceiros. A página "Lag Compensation" da wiki (que, segundo resultado de busca, define `sv_maxunlag` com padrão e máximo de 1 s) não foi aberta: não verificado.
- Texto completo de Lee e Chang (2018) não foi aberto; o conteúdo é citado via o survey de Liu, Xu e Claypool e os metadados da Crossref.
- Compensação para projéteis com tempo de voo e para ações contínuas (feixes, áreas) não é resolvida pelas fontes [F: bernier2001latency, para a ressalva; H, para o restante].
- Não há, nas fontes verificadas, evidência sobre o limite de rewind ideal fora de FPS nem sobre a aceitabilidade do "shot around the corner" em outros gêneros [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gambetta2014lagcomp | tecnico | 2026-10-29 |
| bernier2001latency | tecnico (artigo GDC 2001; original 403, verificado em cópia integral) | 2026-10-29 |
| valve2026source | fornecedor (original 403, verificado em cópia integral) | 2026-10-29 |
| liu2022survey | academico | 2026-10-29 |
| lee2015evaluation | academico (abstract e metadados verificados) | 2026-10-29 |
| lee2017corner | academico (abstract e metadados verificados) | 2026-10-29 |
| lee2018advanced | academico (apenas metadados verificados; conteúdo via liu2022survey) | 2026-10-29 |
