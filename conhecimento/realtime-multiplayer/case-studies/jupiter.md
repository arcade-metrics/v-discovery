---
id: rtm.case.jupiter
titulo: "Jupiter (Xerox PARC): transformação de operações cliente-servidor sob alta latência"
tipo: estudo-de-caso
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
ano_do_sistema: 1995
fontes: [nichols1995jupiter]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.sync.operational-transformation }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.proto.tcp }
  - { tipo: relacionado-a, alvo: rtm.net.latency }
  - { tipo: relacionado-a, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.net.ordering-and-reliability }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
termos: [operational transformation, xform, optimistic concurrency control, state space, dOPT, groupware]
---

# Jupiter (Xerox PARC): transformação de operações cliente-servidor sob alta latência

## Contexto e gênero de interação

Jupiter era um mundo virtual multiusuário e multimídia do Xerox PARC para colaboração remota de longo prazo, com documentos e ferramentas compartilhados e áudio/vídeo opcionais, construído sobre um servidor LambdaMOO não modificado, com aplicações escritas na linguagem MOO e executadas no servidor. A fonte é "High-Latency, Low-Bandwidth Windowing in the Jupiter Collaboration System", de David A. Nichols, Pavel Curtis, Michael Dixon e John Lamping (Xerox PARC), nos anais do UIST '95, pp. 111-120, DOI 10.1145/215585.215706 [F: nichols1995jupiter]. O DOI e os metadados foram verificados no registro Crossref [F: nichols1995jupiter].

Gênero: colaboração síncrona em widgets (editor de texto, desenho vetorial, sliders, botões), sem adversários e sem exigência de taxa de atualização fixa [I].

## Restrições de projeto

Reportado pelos autores [F: nichols1995jupiter]:

- latências de resposta ocasionalmente de "alguns segundos", causadas pela serialização de ações no servidor e por usuários em linhas discadas de baixa banda e rotas longas ou congestionadas;
- múltiplas plataformas de cliente (Unix com Tcl/Tk e Microsoft Windows nativo);
- o cliente evolui devagar; a lógica das aplicações vive no servidor;
- conexão TCP do cliente ao servidor central.

## Arquitetura escolhida

Servidor central guarda o estado de todos os objetos e executa todo o código; clientes gerenciam entrada e saída locais. Cliente e servidor comunicam-se em termos de widgets de alto nível e eventos de usuário, não de eventos de teclado/mouse e primitivas gráficas, o que transmite menos dados e com menos frequência do que um sistema de janelas em rede tradicional (X) [F: nichols1995jupiter]. Ambos mantêm cópia completa do valor de cada widget: a do cliente permite refletir mudanças imediatamente; a do servidor coordena atualizações entre clientes e evita viagens de ida e volta para as aplicações [F: nichols1995jupiter].

Os autores classificam o controle de concorrência em pessimista versus otimista e em centralizado versus distribuído, e escolhem otimista e centralizado: o cliente aplica mudanças imediatamente, sem esperar o servidor; o servidor serializa. Eles observam que os sistemas otimistas anteriores (GroupDesign, Grove) eram totalmente distribuídos, e que a maior parte da complexidade vinha de ter que aceitar mudanças de qualquer participante a qualquer momento [F: nichols1995jupiter].

## Técnicas usadas

### Protocolo de sincronização bidirecional

Quando mensagens se cruzam na rede, cada receptor "conserta" a mensagem recebida em relação ao seu estado atual com uma função `xform(c, s) = {c', s'}`, tal que o cliente aplicando c e depois s', e o servidor aplicando s e depois c', chegam ao mesmo estado. Exemplo dos autores: para deleções, `xform(del x, del y)` ajusta o índice maior pela deleção anterior e vira no-op quando x = y [F: nichols1995jupiter].

O protocolo rotula cada mensagem com o estado (número de mensagens do cliente e do servidor processadas) em que o emissor estava. O espaço de estados é um reticulado bidimensional; sem conflito, cliente e servidor percorrem o mesmo caminho; com conflito, divergem e usam `xform` para reconvergir. Quando a divergência passa de um passo, o receptor precisa guardar o lado transformado (c') para transformar mensagens seguintes; o algoritmo mantém uma fila de mensagens enviadas e ainda não confirmadas e transforma cada mensagem recebida contra toda a fila, atualizando a fila no processo [F: nichols1995jupiter].

Pontos finos reportados: acks pegam carona no tráfego oposto, mas tráfego unilateral exige acks explícitos periódicos (no-ops) para a fila não crescer sem limite; e travas (locks) por janela exigem que os contadores de mensagem sejam mantidos em granularidade pelo menos tão fina quanto a das travas, senão uma mensagem esperando trava pode ser confirmada incorretamente pela resposta a outra [F: nichols1995jupiter].

### Consistência n-ária por serialização no servidor

O protocolo otimista roda apenas em cada enlace cliente-servidor. Ao receber uma mensagem de um cliente, o servidor a aplica à cópia local e a reenvia aos demais clientes da janela. O algoritmo par a par faz cada cliente parecer síncrono ao servidor, o que torna suficiente o simples eco das mudanças; como o valor de cada cliente é igual ao do servidor em repouso, todos são iguais entre si [F: nichols1995jupiter].

### Comparação com dOPT

A `xform` corresponde à matriz T do dOPT (Grove), mas dispensa prioridades de desempate, pois só há dois participantes por enlace; como não há multicast, assume-se transporte ordenado e confiável (TCP) e omite-se o código de reordenação; e o algoritmo corrige um problema do dOPT quando sites divergem por mais de um passo [F: nichols1995jupiter].

### Escolha das transformações

Jupiter tinha 19 mensagens de cliente e 24 de servidor sobre widgets, 456 pares potenciais; considerando apenas conflitos dentro do mesmo tipo de widget, 65 casos; agrupando mensagens semelhantes do StrokeEdit, 41 casos no total. Para widgets simples (Numeric, Boolean), um lado é o "vencedor" e a mensagem perdedora é descartada. Para TextEdit, Replace versus Replace remove todas as regiões pedidas e insere os textos de ambos, ordenados pelo início das regiões, com texto do servidor primeiro em empate; quando uma inserção cai dentro da região apagada pela outra, o texto é inserido mesmo assim e a operação transformada é dividida em duas mensagens. Diretrizes declaradas: o conjunto de operações deve ser fechado sob as transformações; não descartar entrada do usuário; não confundir o código da aplicação [F: nichols1995jupiter].

## Resultados e números reportados

- 19 mensagens de cliente, 24 de servidor, 456 pares potenciais, reduzidos a 65 e depois a 41 casos de transformação [F: nichols1995jupiter].
- Latência de resposta "ocasionalmente de alguns segundos" nas condições que motivaram o projeto [F: nichols1995jupiter].
- Razão de compressão de 20:1 citada para o sistema HBX, como trabalho relacionado que não elimina ida e volta [F: nichols1995jupiter].
- Não há avaliação experimental de latência percebida ou banda do próprio Jupiter [I].

## Lições documentadas pelos autores

Contribuições declaradas: simplificação significativa do algoritmo de Ellis e Gibbs ao assumir canal ordenado e confiável entre exatamente dois participantes; mecanismo para compartilhamento n-ário com o algoritmo par a par; e discussão pragmática do projeto das funções de transformação, que os autores dizem ser difícil e cheia de concessões (por exemplo, manter ou não traços desenhados após a aplicação mudar o modo do widget, decisão que "volta à discussão de tempos em tempos") [F: nichols1995jupiter].

## O que é opinião e o que é fato

- Fato: arquitetura, algoritmo, invariantes, contagem de casos e escolhas de transformação [F: nichols1995jupiter].
- Opinião dos autores: que "as melhores transformações nem sempre são óbvias" e que a combinação centralizado + otimista "dá o melhor dos dois" [F: nichols1995jupiter] [I].
- Interpretação deste documento: Jupiter é o antecedente direto da arquitetura OT cliente-servidor usada por editores de texto colaborativos posteriores; sua ideia central é reduzir o problema n-ário a n problemas binários com um serializador central [I].

## Limites do estudo

- Sistema de 1995, com clientes Tcl/Tk e MOO; a implementação não é comparável em escala a serviços atuais [I].
- Sem métricas; a validação é argumentativa e por construção [I].
- Texto plano apenas; sem formatação rica, cujas transformações são mais numerosas [I].

## Relações com outros conceitos

Instância fundadora de `rtm.sync.operational-transformation` em topologia `rtm.arch.authoritative-server` (servidor serializador) sobre `rtm.proto.tcp` (ordem e confiabilidade assumidas, `rtm.net.ordering-and-reliability`). Motivado por `rtm.net.latency` e `rtm.net.bandwidth` baixas. A aplicação local imediata com correção posterior é o análogo, em colaboração, de `rtm.pred.client-side-prediction`. Contrasta com `rtm.sync.crdt`, que dispensa o serializador central.

## Lacunas e questões abertas

- Correção formal das transformações para TextEdit não é demonstrada no artigo; a garantia declarada é a convergência quando todas as mensagens são processadas [F: nichols1995jupiter] [I].
- Comportamento com desconexão longa e filas grandes de mensagens não confirmadas não é discutido [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nichols1995jupiter | academico (UIST '95, ACM; PDF espelhado em lively-kernel.org; DOI verificado via Crossref) | 2026-10-29 |
