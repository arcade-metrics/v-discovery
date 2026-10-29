---
id: rtm.pred.client-side-prediction
titulo: Client-side prediction
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [gambetta2014architecture, gambetta2014prediction, gambetta2014demo, bernier2001latency, valve2026source, fiedler2010networking, liu2022survey, wikipedia2026csp]
relacoes:
  - { tipo: depende-de, alvo: rtm.arch.authoritative-server }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: complementa, alvo: rtm.pred.server-reconciliation }
  - { tipo: complementa, alvo: rtm.pred.entity-interpolation }
  - { tipo: complementa, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.pred.comparison }
termos: [client-side prediction, self-prediction, dumb client, user command, input buffer, misprediction, shared simulation code]
---

# Client-side prediction

## Definição e terminologia

Client-side prediction é a técnica em que o cliente aplica a entrada do jogador local à sua cópia do estado imediatamente, sem esperar a confirmação do servidor autoritativo, assumindo que o servidor aceitará essa entrada [F: gambetta2014prediction]. O servidor continua sendo a única autoridade: se a simulação local divergir, o cliente é corrigido [F: gambetta2014prediction; F: bernier2001latency].

Nomes alternativos encontrados nas fontes:

- **Self-prediction**: termo usado pela taxonomia de Liu, Xu e Claypool, que registra que "self-prediction is often called client-side prediction in papers, online blogs and player posts" [F: liu2022survey, §4.2.1].
- **Input prediction**: nome usado pela documentação do fornecedor Valve para a mesma técnica no motor Source [F: valve2026source].
- **Prediction** (sem qualificador): uso de Bernier 2001 e de Gambetta; nesta base, "predição" sem qualificador refere-se a esta técnica, e a predição de outras entidades é tratada como *other-prediction* (interpolação e extrapolação; ver `rtm.pred.entity-interpolation` e `rtm.sync.dead-reckoning`) [I].

O que não é: client-side prediction não dá ao cliente autoridade sobre o estado. Um cliente adulterado pode mostrar o que quiser localmente, mas isso não altera o que os outros jogadores veem [F: gambetta2014prediction]. Também não é predição do que *outros* jogadores farão; a documentação da Valve afirma que só é possível prever o próprio jogador e entidades afetadas apenas por ele, pois não há como saber antecipadamente as teclas dos outros [F: valve2026source].

## Problema que resolve

No modelo de servidor autoritativo com "dumb client", o cliente envia a intenção ("quero mover um quadrado para a direita") e só exibe o resultado quando o servidor responde [F: gambetta2014architecture]. O atraso entre ação e resposta é no mínimo o tempo de ida e volta (RTT). Gambetta exemplifica com 50 ms em cada sentido, o que dá cerca de 100 ms entre apertar a tecla e ver o movimento, e afirma que meio segundo de atraso torna o jogo injogável [F: gambetta2014architecture]. Bernier descreve o mesmo problema a partir do Half-Life: sem predição, uma latência de 500 ms é aceitável em LAN e inaceitável na internet [F: bernier2001latency].

Gambetta observa que o modelo de dumb client funciona bem em jogos por turnos (estratégia, pôquer) e em LAN, e só falha em jogos rápidos pela internet [F: gambetta2014architecture]. Portanto a técnica resolve um problema de responsividade que nem toda aplicação tem [I].

Historicamente, Fiedler atribui a introdução da técnica a QuakeWorld, citando Carmack: "I am now allowing the client to guess at the results of the users movement" [F: fiedler2010networking]. A Wikipedia (fonte secundária) registra Duke Nukem 3D (1996) como primeiro FPS conhecido a usá-la, antes de QuakeWorld [F: wikipedia2026csp]; este dado não foi confirmado em fonte primária.

## Fundamentos e funcionamento

O cliente executa, para a entidade controlada pelo jogador local, a mesma lógica que o servidor executaria, e exibe o resultado no mesmo frame em que a entrada ocorreu [F: gambetta2014prediction]. Em paralelo, envia a entrada ao servidor. Quando o servidor responde com o estado autoritativo, na maior parte dos casos ele coincide com o que o cliente já mostrou, e nada visível acontece [F: gambetta2014prediction].

Elementos que as fontes consideram essenciais:

1. **Código de simulação compartilhado.** Bernier descreve que o Half-Life SDK compartilha o código de movimento (`pm_shared`) entre cliente e servidor, de modo que a mesma entrada produza o mesmo resultado em ambos [F: bernier2001latency]. A Valve reitera que o cliente prevê "usando o mesmo código e as mesmas regras do servidor" [F: valve2026source]. Fiedler descreve que o cliente de QuakeWorld passou a rodar parte da lógica do jogo, incluindo colisão, atrito e gravidade [F: fiedler2010networking].
2. **Entrada como comando datado.** Bernier descreve o *user command* (usercmd) do Half-Life com campos `msec` (duração do frame simulado), `viewangles`, `forwardmove`/`sidemove`/`upmove`, `buttons` e `lerp_msec` (tempo de interpolação do cliente, usado depois pela lag compensation) [F: bernier2001latency]. O comando carrega a duração para que o servidor reproduza exatamente a simulação do cliente [I].
3. **Buffer de entradas não confirmadas.** O cliente guarda os comandos ainda não reconhecidos pelo servidor. Bernier dá o número: com 50 fps e 100 ms de RTT, o cliente acumula cerca de 5 comandos não reconhecidos [F: bernier2001latency]. Fiedler descreve o mesmo como um buffer circular de estados e entradas recentes do jogador local [F: fiedler2010networking]. Esse buffer é o que a reconciliação consome (ver `rtm.pred.server-reconciliation`).
4. **Correção pelo servidor.** Quando chega um estado autoritativo, o cliente compara a posição recebida com a prevista; qualquer diferença é um erro de predição e o servidor tem a palavra final [F: valve2026source]. Sweeney, citado por Fiedler, resume: o cliente quase sempre reproduz o movimento do servidor e só é corrigido em eventos externos e imprevisíveis, como ser atingido por um foguete [F: fiedler2010networking].

A taxonomia de Liu, Xu e Claypool classifica a técnica em *Prediction > Self-Prediction*, define *Prediction* como estimar "the game state at a client without having the official game state from the server" e aponta o custo inerente: quando a predição está errada, a correção "is noticeable and may even be jarring to the player" [F: liu2022survey, §4.2].

### Efeitos colaterais e estado só do cliente

Como os comandos pendentes podem ser reexecutados várias vezes (ver reconciliação), Bernier recomenda que sons e efeitos (passos, disparo) sejam disparados apenas na primeira execução de cada comando; o cliente marca quais comandos ainda não foram previstos [F: bernier2001latency]. Dados que existem só no cliente (exemplo do autor: altura do olho ao agachar) precisam ser guardados em uma janela deslizante de estados intermediários e copiados ao confirmar um comando [F: bernier2001latency].

### Predição de armas

Bernier estende a predição ao disparo: estado da arma (munição, próximo disparo, animação) entra no estado autoritativo, a lógica de tiro vai para código compartilhado, e troca, saque e guarda de armas passam a ser previstos [F: bernier2001latency]. O autor ressalva que projéteis autônomos colocam questões difíceis e que, no Half-Life, não recebem compensação, embora o som do disparo seja previsto [F: bernier2001latency].

## Requisitos e pressupostos

- **Servidor autoritativo.** A técnica pressupõe que a verdade vem do servidor; sem isso não há o que prever nem contra o que corrigir [F: gambetta2014prediction]. Ver `rtm.arch.authoritative-server`.
- **Determinismo suficiente.** Gambetta afirma que, dado o mesmo estado e as mesmas entradas, o resultado deve ser totalmente previsível; caso contrário a predição local não corresponde ao servidor [F: gambetta2014prediction]. Fiedler afirma que, se as simulações de cliente e servidor forem parecidas, as correções são raras [F: fiedler2010networking]. Interpretação: o requisito é mais fraco que o do lockstep determinístico (`rtm.arch.deterministic-lockstep`), porque divergências são toleradas e corrigidas; o que importa é que sejam raras e pequenas [I].
- **Maioria das entradas válidas.** Gambetta assume que a maior parte das entradas recebidas pelo servidor é válida; a predição aposta nesse caso comum [F: gambetta2014prediction].
- **Cliente capaz de simular.** A taxonomia nota que a técnica é natural porque "most clients run a fully-functional game engine" [F: liu2022survey, §4.2.1]. Clientes muito leves (thin clients, streaming) não têm essa capacidade [I].
- **Entidade controlada exclusivamente pelo jogador.** Só o que depende apenas da entrada local pode ser previsto [F: valve2026source].

## Vantagens e limitações

Vantagens:

- Resposta ao jogador no mesmo frame, independente da latência [F: gambetta2014prediction]. Na demo de Gambetta, com predição e reconciliação ativas, o movimento do próprio jogador fica quase instantâneo mesmo com 250 ms ou 500 ms de lag simulado [F: gambetta2014demo].
- Mantém o servidor autoritativo; não abre superfície de cheating por si só [F: gambetta2014prediction].
- Fiedler registra que, na transição Quake para QuakeWorld, a técnica "proved popular with both high and low latency players" (via Wikipedia, secundária) [F: wikipedia2026csp]; Fiedler cita que a arquitetura inicial fora pensada para conexões abaixo de 200 ms, enquanto a maioria dos usuários tinha mais de 300 ms [F: fiedler2010networking].

Limitações:

- Só melhora a entidade do próprio jogador; os outros continuam com movimento irregular se o servidor atualizar pouco [F: gambetta2014demo]. Por isso é combinada com `rtm.pred.entity-interpolation`.
- Mispredição produz correção visível ("salto"). Gambetta mostra que sem reconciliação o salto é inaceitável; com reconciliação, resta o caso de divergência real [F: gambetta2014prediction]. A Valve distribui a correção no tempo (`cl_smoothtime`; valor não informado no texto) [F: valve2026source].
- Exige duplicar lógica no cliente, com disciplina para manter cliente e servidor equivalentes [I]; Bernier descreve o custo de reorganizar o código em módulos compartilhados [F: bernier2001latency].
- Decisões irreversíveis (morte) não devem ser previstas: Gambetta recomenda que o cliente aguarde confirmação do servidor antes de matar um personagem, mesmo que a vida local tenha chegado a zero, citando o caso de um item de cura usado pelo oponente antes do ataque chegar [F: gambetta2014prediction].

## Alternativas e comparações

| Abordagem | Resposta ao jogador | Autoridade | Observação |
|---|---|---|---|
| Dumb client (sem predição) | Após o RTT | Servidor | Adequado a turnos e LAN [F: gambetta2014architecture] |
| Client-side prediction | Imediata para a própria entidade | Servidor | Exige código compartilhado e reconciliação [F: bernier2001latency] |
| Lockstep determinístico | Após receber entradas de todos | Distribuída | Latência do jogador mais lento; determinismo estrito [F: fiedler2010networking] |
| Cliente autoritativo sobre posição | Imediata | Cliente | Fácil de trapacear; "The Server Is The Man" (Sweeney, citado por Fiedler) [F: fiedler2010networking] |

Comparação completa em `rtm.pred.comparison`.

## Métricas e métodos de avaliação

- **Taxa e magnitude de erro de predição.** A Valve expõe `cl_showerror 1` para visualizar erros de predição no cliente [F: valve2026source]. Em avaliação, pode-se medir a distância entre estado previsto e estado autoritativo a cada confirmação [I].
- **Latência percebida.** O ganho esperado é reduzir o atraso ação-resposta de RTT para zero frames, o que pode ser medido com latência artificial (a demo de Gambetta e o `net_fakelag` da Valve são exemplos de emulação) [F: gambetta2014demo; F: valve2026source]. Ver `rtm.perf.network-emulation` e `rtm.perf.qoe-thresholds`.
- O survey de Liu, Xu e Claypool lista estudos de usuário com *self-prediction* em faixas de latência de 0 a 900 ms, mas não extraímos resultados numéricos específicos [F: liu2022survey, tabela de estudos].

## Exemplo técnico independente de domínio

Pseudocódigo do loop do cliente com predição e buffer de entradas (a reconciliação está em `rtm.pred.server-reconciliation`):

```
estado_local      <- estado inicial recebido do servidor
seq               <- 0
pendentes         <- fila vazia

a cada frame (dt):
    entrada <- ler_entrada()
    seq <- seq + 1
    cmd <- { seq, dt, entrada }
    enviar_ao_servidor(cmd)
    pendentes.adicionar(cmd)
    estado_local <- simular(estado_local, cmd)     # mesma função usada no servidor
    renderizar(estado_local)
```

Diagrama de sequência em texto, latência de 100 ms em cada sentido:

```
t=0    Cliente: tecla "direita" -> aplica localmente (x: 10 -> 11), envia cmd#1
t=100  Servidor: recebe cmd#1, simula (x = 11), envia estado {x=11, ultimo=1}
t=200  Cliente: recebe {x=11, ultimo=1}; coincide com a predição -> nada visível
```

Sem predição, o cliente só mostraria x = 11 em t = 200 [I, com base em gambetta2014prediction].

## Relações com outros conceitos

Depende de `rtm.arch.authoritative-server` (sem autoridade central não há correção) e de `rtm.net.latency` (é a latência que motiva a técnica). Complementa `rtm.pred.server-reconciliation` (consome o buffer de entradas), `rtm.pred.entity-interpolation` (cobre as outras entidades) e `rtm.pred.lag-compensation` (resolve a mira no servidor). Relaciona-se com `rtm.arch.deterministic-lockstep` (requisito de determinismo mais estrito) e com `rtm.sec.cheating` (a técnica não reduz a autoridade do servidor). Síntese comparativa em `rtm.pred.comparison`.

## Lacunas e questões abertas

- As páginas da Valve (Source Multiplayer Networking e o artigo de Bernier) retornaram HTTP 403 ao acesso direto em 2026-10-29; o texto foi verificado em cópias integrais em inglês hospedadas em terceiros (ver tabela de fontes). Valores padrão de `cl_smoothtime` e detalhes de versão do motor não foram verificados.
- A atribuição a Duke Nukem 3D (1996) vem de fonte secundária e não foi confirmada em fonte primária.
- Não localizamos, nesta sessão, estudo acadêmico que quantifique o ganho de QoE da predição isoladamente; o survey de Liu, Xu e Claypool é o ponto de partida para essa busca [H].
- Grau de determinismo necessário na prática (ponto flutuante entre plataformas, ordem de atualização) não é quantificado pelas fontes; permanece como questão de engenharia [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gambetta2014architecture | tecnico | 2026-10-29 |
| gambetta2014prediction | tecnico | 2026-10-29 |
| gambetta2014demo | tecnico | 2026-10-29 |
| bernier2001latency | tecnico (artigo GDC 2001; original 403, verificado em cópia integral) | 2026-10-29 |
| valve2026source | fornecedor (original 403, verificado em cópia integral) | 2026-10-29 |
| fiedler2010networking | tecnico | 2026-10-29 |
| liu2022survey | academico | 2026-10-29 |
| wikipedia2026csp | secundario | 2026-10-29 |
