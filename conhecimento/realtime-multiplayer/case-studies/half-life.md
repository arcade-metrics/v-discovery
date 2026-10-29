---
id: rtm.case.half-life
titulo: "Half-Life (Valve): predição no cliente, interpolação e lag compensation"
tipo: estudo-de-caso
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
ano_do_sistema: 2001
fontes: [bernier2001latency]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.pred.server-reconciliation }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
  - { tipo: relacionado-a, alvo: rtm.pred.lag-compensation }
  - { tipo: relacionado-a, alvo: rtm.sync.dead-reckoning }
  - { tipo: relacionado-a, alvo: rtm.net.latency }
  - { tipo: relacionado-a, alvo: rtm.net.clock-synchronization }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
  - { tipo: relacionado-a, alvo: rtm.net.bandwidth }
termos: [client-side prediction, lag compensation, interpolation delay, extrapolation, position history, usercmd, shared code]
---

# Half-Life (Valve): predição no cliente, interpolação e lag compensation

## Contexto e gênero de interação

A fonte é o artigo "Latency Compensating Methods in Client/Server In-game Protocol Design and Optimization", de Yahn W. Bernier (Valve), apresentado na Game Developers Conference de 2001 [F: bernier2001latency]. O texto descreve o motor de Half-Life e seus mods (Counter-Strike, Team Fortress Classic): jogos de ação em primeira pessoa com entrada contínua, armas de acerto instantâneo (hitscan) e jogadores com movimento de alta aceleração [F: bernier2001latency].

O artigo é frequentemente associado ao motor Source, sucessor do motor de Half-Life; a página "Source Multiplayer Networking" da Valve Developer Community, que descreve o mesmo conjunto de técnicas no motor posterior, não pôde ser aberta nesta sessão (HTTP 403), por isso este caso se limita ao que Bernier descreve para Half-Life [I].

## Restrições de projeto

O autor descreve o ambiente de 2001 [F: bernier2001latency]:

- clientes em hardware e conexões variados, muitos ainda em modem; banda larga não era suposição aceitável, e conexões de banda larga "ruins" tinham latência e perda significativas;
- latências de 100 a 500 ms são usadas como exemplos ao longo do texto; o autor afirma que "a maioria dos jogadores ainda tem mais de 150 ms de latência";
- preocupação explícita com trapaça: confiar no cliente é descartado por isso;
- padrão de 20 atualizações por segundo do servidor para cada jogador, configurável pelo usuário até um limite (um usuário com conexão rápida poderia pedir 50 por segundo), e interpolação de 100 ms no cliente.

## Arquitetura escolhida

Cliente/servidor com servidor autoritativo: o servidor executa a lógica principal; os clientes, originalmente "burros", amostram entrada e a enviam como comandos de usuário (`usercmd_t`, com duração em ms, ângulos de visão, impulsos de movimento e botões). Sem compensação, um cliente com 500 ms de latência só vê o resultado de suas ações 500 ms depois, aceitável em LAN mas não na Internet [F: bernier2001latency].

O autor rejeita explicitamente mover a simulação de movimento e armas para o cliente ("estou na posição x e acertei o jogador 2 na cabeça"), como fazem simuladores militares fechados e jogos peer-to-peer, porque em Half-Life a motivação para hackear o cliente seria alta demais [F: bernier2001latency].

## Técnicas usadas

### Predição de movimento no cliente

O cliente guarda cada comando enviado com seu instante. A partir do último estado confirmado pelo servidor, reexecuta localmente os comandos ainda não confirmados usando o mesmo código de movimento do servidor (pasta `pm_shared` do SDK, "player movement shared"). Exemplo do autor: a 50 fps com 100 ms de latência de ida e volta, o cliente terá cinco comandos à frente do último confirmado, e os cinco são re-simulados a cada quadro [F: bernier2001latency].

Cuidados reportados: efeitos (sons de passos etc.) só devem ser disparados na primeira execução de um comando, não nas reexecuções; o servidor não deve enviar efeitos que o cliente já prediz; estado existente só no cliente exige guardar resultados intermediários em janela deslizante [F: bernier2001latency]. O autor nota que o sistema é semelhante ao do QuakeWorld [F: bernier2001latency].

A nota de rodapé sobre a variável `pushlatency` registra que usuários configuravam predição parcial por "superstição", o que deixava o movimento "como se estivesse em patins", e conclui que a predição completa deve ocorrer sempre e a variável deve ser removida [F: bernier2001latency].

### Predição de disparo de armas

A lógica de disparo também foi movida para código compartilhado; ammo, próximo instante de disparo e animação fazem parte do estado autoritativo replicado ao cliente, permitindo predizer disparo, troca e recolhimento de armas, de modo que o jogador sinta resposta "100%" a movimento e ativação de armas [F: bernier2001latency].

### Exibição dos outros jogadores: extrapolação versus interpolação

Extrapolação (simular adiante a partir da última posição e velocidade) falha porque o movimento dos jogadores tem "jerk" alto e física irrealista; o QuakeWorld limitava a extrapolação a 100 ms para reduzir o "warp" corretivo [F: bernier2001latency].

Interpolação: o cliente renderiza os outros no passado, com atraso de interpolação de 100 ms, interpolando entre as duas últimas atualizações; cada atualização traz o timestamp do servidor, e o cliente adota o relógio do servidor (rodando atrasado pela latência). Com 200 ms de interpolação seria possível perder uma atualização inteira sem engasgo, à custa de mais latência percebida [F: bernier2001latency].

O autor descreve o problema da "bola quicando": interpolar apenas até a última posição achata extremos. Half-Life mantém um "position history" (timestamp, origem, ângulos) por objeto e busca o par de amostras que envolve o instante alvo, o que segue a curva por todos os pontos amostrados e lida com atualizações de espaçamento irregular, que ocorrem porque o servidor adia o próximo pacote conforme o "rate" do usuário (com 20 atualizações/s, no mínimo 50 ms; com choke de banda ativo, 61 ms etc.) [F: bernier2001latency]. Teleportes precisam de tratamento especial (flag ou limiar de distância) para não serem interpolados [F: bernier2001latency].

### Lag compensation

Antes de executar um comando do jogador, o servidor: estima a latência do jogador; localiza no histórico a atualização de mundo que o jogador tinha recebido ao emitir o comando; move os outros jogadores de volta no tempo para onde estavam, descontando latência de conexão e a quantidade de interpolação que o cliente usava naquele quadro (campo `lerp_msec` do `usercmd_t`); executa o comando, incluindo ray casts de armas contra as posições antigas; e restaura todos às posições atuais. Estado adicional (vivo/morto, agachado) pode precisar ser retrocedido também [F: bernier2001latency].

Projéteis não são compensados em Half-Life; o autor expõe as perguntas em aberto (em que tempo vive o projétil? quanto retroceder os outros?) e diz que foram evitadas [F: bernier2001latency].

## Resultados e números reportados

- Padrão de 20 atualizações/s por jogador; usuário pode pedir até 50/s; interpolação de 100 ms [F: bernier2001latency].
- Exemplo de necessidade de "lead" sem compensação: 100 ms de latência e alvo a 500 unidades/s exigem mirar 50 unidades à frente [F: bernier2001latency].
- Limite de extrapolação do QuakeWorld: 100 ms [F: bernier2001latency].
- Cenário extremo de "tiro pela esquina" descrito com cerca de 500 ms de latência [F: bernier2001latency].

Não há medições de erro de predição, banda ou satisfação; o artigo é descritivo e argumentativo [I].

## Lições documentadas pelo autor

- Predição completa, sempre; configurações parciais pelo usuário causaram confusão [F: bernier2001latency].
- Compartilhar código de movimento e armas entre cliente e servidor minimiza discrepâncias de predição [F: bernier2001latency].
- Lag compensation é "uma decisão de design de jogo": permite mirar diretamente sem calcular lead, ao custo de inconsistências do ponto de vista de quem é atingido (o "tiro pela esquina", termo adotado pela comunidade). Nos dois casos típicos de FPS (jogadores correndo um contra o outro; alvo cruzando a linha de visão sem ver o atirador) o paradoxo é pouco perceptível. Para Half-Life, Team Fortress e Counter-Strike, os benefícios "facilmente superaram" as inconsistências [F: bernier2001latency].
- O autor observa que em jogos onde se olha para um lado e se move para outro (tanques), o paradoxo é menos claro [F: bernier2001latency].

## O que é opinião e o que é fato

- Fato: os algoritmos, campos de estrutura, valores padrão e exemplos numéricos [F: bernier2001latency].
- Opinião do autor: que os benefícios da lag compensation superam as inconsistências; que a "maioria" dos jogadores tem mais de 150 ms (afirmação sem fonte no texto); que confiar no cliente é inaceitável por trapaça [F: bernier2001latency] [I].
- Interpretação deste documento: o artigo é a formulação de referência do trio predição, interpolação e lag compensation que a literatura posterior reusa; seu valor está na explicitação dos compromissos de design, não em dados [I].

## Limites do estudo

- Reflete o ambiente de 2001 (modems, 20 atualizações/s); taxas e atrasos de interpolação de sistemas atuais podem diferir [I].
- Descreve o motor de Half-Life; a transposição para o motor Source não foi verificada aqui [I].
- Nenhum dado quantitativo de avaliação; o texto é uma exposição de técnicas e justificativas [I].

## Relações com outros conceitos

Exemplo de referência de `rtm.pred.client-side-prediction` com `rtm.pred.server-reconciliation` (reexecução dos comandos não confirmados a partir do último estado autoritativo), de `rtm.pred.entity-interpolation` (atraso de 100 ms e position history) e de `rtm.pred.lag-compensation` (rewind no servidor). A discussão de extrapolação conecta-se a `rtm.sync.dead-reckoning`. A adoção do relógio do servidor pelo cliente relaciona-se a `rtm.net.clock-synchronization`; a rejeição de confiar no cliente, a `rtm.sec.cheating`; o ajuste de pacotes pelo "rate" do usuário, a `rtm.net.bandwidth`.

## Lacunas e questões abertas

- Lag compensation de projéteis: deixada em aberto pelo próprio autor [F: bernier2001latency].
- Quantificação do custo de reexecutar N comandos por quadro em clientes com latência alta: não abordada [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| bernier2001latency | tecnico (artigo de praticante, GDC 2001; PDF espelhado em gamedevs.org) | 2026-10-29 |
