---
id: rtm.sync.interest-management
titulo: Interest management
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [boulanger2006comparing, morse2000interest, liu2014interest, frohnmayer2000tribes, fiedler2015statesync, madhav2015multiplayer, ryan2006deadreckoning]
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-replication }
  - { tipo: complementa, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: complementa, alvo: rtm.sync.state-synchronization }
  - { tipo: complementa, alvo: rtm.sync.dead-reckoning }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
  - { tipo: relacionado-a, alvo: rtm.mp.rooms-and-matches }
  - { tipo: relacionado-a, alvo: rtm.rt.communication-patterns }
  - { tipo: relacionado-a, alvo: rtm.sec.cheating }
termos: [interest management, area of interest, aura, nimbus, relevance filtering, scope, region-based, visibility-based, publish-subscribe]
---

# Interest management

## Definição e terminologia

Interest management (IM) é o processo de determinar qual informação é relevante para cada participante de um ambiente virtual distribuído e enviar a cada um apenas as atualizações relevantes [F: boulanger2006comparing]. Liu e Theodoropoulos a definem como a técnica de otimizar o fluxo de dados em ambientes virtuais distribuídos e simulações em larga escala, essencial para escalabilidade à medida que esses sistemas crescem em volume de dados e sensibilidade à latência [F: liu2014interest].

Termos: *area of interest* (AOI), a região que um participante percebe; *aura*, a área que delimita a presença de um objeto, e *nimbus*, a área em que ele percebe outros, no modelo espacial de Benford e Fahlén citado por Boulanger et al.: x percebe y quando o nimbus de x intersecta a aura de y [F: boulanger2006comparing]; *relevance filtering*, sinônimo usado em simulação militar; *scope*, termo do TRIBES para o conjunto de objetos cuja cópia (*ghost*) existe em um cliente [F: frohnmayer2000tribes]; *Object Scope and Relevancy* é o título da seção correspondente no capítulo de escalabilidade de Madhav e Glazer [F: madhav2015multiplayer].

O que não é: IM não é compressão (reduz o que é enviado, não como é codificado) nem priorização temporal pura (que decide quando enviar o que é relevante); as três se combinam. [I]

## Problema que resolve

Transmitir todo estado a todos não escala: Boulanger et al. afirmam que broadcast de todas as mudanças de estado a todos os jogadores de um jogo massivo não é viável, e que as mensagens crescem com o número de jogadores [F: boulanger2006comparing]. Um jogador precisa apenas de um subconjunto do mundo, em geral o que seu avatar percebe [F: boulanger2006comparing]. No TRIBES, o *Ghost manager* não replica todos os objetos porque replicar custa rede; objetos entram e saem de *scope*, sua cópia é transferida ao entrar e apagada ao sair [F: frohnmayer2000tribes].

## Fundamentos e funcionamento

### Modelo publish-subscribe

Boulanger et al. abstraem IM como publish-subscribe: publicadores produzem eventos, assinantes os consomem, e IM é a função que determina quando um assinante descobre um publicador, assina e cancela a assinatura [F: boulanger2006comparing]. Na implementação deles, cada publicador tem um canal; quando um publicador passa a casar com o interesse de um assinante sem assinatura, o servidor envia uma cópia completa do objeto (*content message*) e assina o cliente ao canal; depois seguem *update messages* parciais; no traço medido, uma content message custou em média 1,5 vez uma update message [F: boulanger2006comparing]. Ver `rtm.rt.communication-patterns`.

### Classes de esquemas

Os esquemas dividem-se em *space-based* (extrínsecos: pela posição relativa) e *class-based* (intrínsecos: por atributos do objeto), classificação que os autores atribuem a Morse [F: boulanger2006comparing]. Dentro dos espaciais:

- **Aura-nimbus puro** (distância euclidiana): fino, mas custa O(M·N) para M assinantes e N publicadores [F: boulanger2006comparing].
- **Region-based**: o mundo é particionado em regiões estáticas e a área de assinatura é a união das regiões que intersectam a AOI; hexágonos aproximam melhor um círculo que quadrados; NPSNET usava hexágonos com um grupo multicast por hexágono; funciona melhor com objetos distribuídos de forma uniforme [F: boulanger2006comparing].
- **Visibility-based**: considera o que o jogador vê, não um raio fixo; RING pré-computava visibilidade entre regiões [F: boulanger2006comparing].
- **Obstacle-aware por triangulação**: os autores propõem particionar o mundo em triângulos (Delaunay com área máxima, obstáculos como furos) e armazená-lo como grafo, de modo que regiões próximas mas separadas por obstáculo fiquem distantes no grafo [F: boulanger2006comparing].

Liu e Theodoropoulos propõem uma taxonomia mais ampla e discutem os compromissos de projeto de cada abordagem [F: liu2014interest]; o texto completo não foi aberto, apenas o resumo. Morse, Bic e Dillencourt (2000) pesquisaram sistemas de IM em ambientes virtuais de larga escala [F: morse2000interest]; só os metadados foram verificados.

### Relevância temporal: prioridade

Mesmo dentro da AOI, nem tudo precisa ir em todo pacote. O TRIBES atualiza cada objeto em *scope* "a uma taxa baseada em sua prioridade e máscara de estado", com a prioridade atribuída pela camada de simulação no processo de scoping, e suporta objetos "ghost always", sempre em scope [F: frohnmayer2000tribes]. O *priority accumulator* de Fiedler é a mesma ideia com garantia de não starvation (ver `rtm.sync.state-synchronization`) [F: fiedler2015statesync]. Madhav e Glazer tratam disso na seção *Prioritization and Frequency* do mesmo capítulo [F: madhav2015multiplayer]. Em DIS, Ryan e Oliver citam proposta de limiares de dead reckoning dependentes da área de interesse, para que entidades próximas recebam mais atualizações que distantes [F: ryan2006deadreckoning].

## Algoritmos e modelos relevantes

Boulanger et al. compararam oito algoritmos no framework Mammoth com um traço real de 28 jogadores (jogo Orbius, mundo 30×30, 12 minutos) e dois traços aleatórios: Euclidean Distance, Square Tile, Hexagonal Tile, Ray Visibility (referência ideal), Tile Distance, Tile Visibility, Tile Neighbor e Tile Path Distance [F: boulanger2006comparing]. Resultados principais:

- Algoritmos que consideram obstáculos reduzem as mensagens de atualização entre jogadores em até um fator de 6, especialmente em ambientes densos (dentro de edifícios) [F: boulanger2006comparing].
- Square Tile teve a pior filtragem: mais do dobro das mensagens do Ray Visibility no menor raio, piorando com raios maiores [F: boulanger2006comparing].
- Hexagonal ficou a 17% mais update messages e 14% mais content messages que a distância euclidiana [F: boulanger2006comparing].
- Tile Visibility filtrou 3% mais updates que Hexagonal com raio 2 e 23% mais com raio 5 [F: boulanger2006comparing].
- Path Distance ficou mais perto do limite inferior (cerca de duas vezes as mensagens do Ray Visibility) com esforço computacional 3 a 6 vezes menor, e sem pré-processamento complexo [F: boulanger2006comparing].
- Em escalabilidade (1000 a 3000 objetos), algoritmos por tiles têm grande vantagem de CPU sobre Ray Visibility e Distance, que computam interesse contra todo publicador do mundo [F: boulanger2006comparing].
- Traços aleatórios reproduzem os resultados relativos, desde que a posição inicial dos bots (dentro ou fora de edifícios) reflita o jogo real [F: boulanger2006comparing].

Os autores observam que a visibilidade exata nem sempre é desejável: convém pré-buscar objetos "prestes a ser descobertos" para evitar o *missed interaction problem* e descoberta tardia sob latência [F: boulanger2006comparing]. Também apontam o trade-off de Rak e Van Hook entre regiões menores (melhor filtragem) e custo de assinar e cancelar grupos multicast [F: boulanger2006comparing].

## Requisitos e pressupostos

- Uma noção de relevância computável no servidor (posição, visibilidade, equipe, canal). [I]
- Mecanismo de entrega seletiva: unicast por cliente (TCP ou UDP), ou multicast, que os autores consideram não disponível de forma geral na internet por restrições de ISPs e firewalls [F: boulanger2006comparing].
- Replicação de objeto com ciclo de vida (criar cópia ao entrar em scope, destruir ao sair) [F: frohnmayer2000tribes].
- Mundo com estrutura espacial estável para esquemas por região ou triangulação; os autores assumiram obstáculos estáticos [F: boulanger2006comparing].

## Vantagens e limitações

Vantagens: redução de mensagens por cliente proporcional à fração do mundo que ele percebe; custo de CPU controlável com esquemas por tiles [F: boulanger2006comparing]. IM também limita o que o cliente sabe, o que é relevante contra trapaças de informação (ver `rtm.sec.cheating`) [I].

Limitações: custo de assinatura e cancelamento; aproximação da AOI por regiões gera mensagens desnecessárias; descoberta tardia quando o filtro é apertado demais [F: boulanger2006comparing]; aglomeração de jogadores em uma região derrota esquemas por região, exigindo balanceamento [F: boulanger2006comparing]. Ganhos com tiles menores foram "surpreendentemente sutis" no mundo testado, com 28 jogadores [F: boulanger2006comparing].

## Alternativas e comparações

| Esquema | Precisão da AOI | Custo de cálculo | Observação |
|---|---|---|---|
| Euclidean Distance | boa (círculo) | O(M·N) [F: boulanger2006comparing] | não escala com objetos |
| Square Tile | pior [F: boulanger2006comparing] | constante por jogador | 9 tiles fixos |
| Hexagonal Tile | +17% updates vs distância [F: boulanger2006comparing] | baixo | aproxima melhor o círculo |
| Ray Visibility | ideal (limite inferior) [F: boulanger2006comparing] | alto | sem pré-busca |
| Tile Path Distance | ~2× o ideal, 3 a 6× menos CPU [F: boulanger2006comparing] | baixo, sem pré-processamento | obstacle-aware |

## Métricas e métodos de avaliação

Número médio de update messages e content messages por cliente por raio de interesse; CPU do servidor por tamanho de tile e por densidade de objetos; variação entre repetições (0,4% no experimento) [F: boulanger2006comparing]. Ver `rtm.perf.metrics` e `rtm.perf.load-testing`.

## Exemplo técnico independente de domínio

Filtragem espacial por grade com assinatura incremental.

```
grade: dicionário celula -> conjunto de objetos; tamanho_celula ~ raio_interesse
scope[c]: conjunto de objetos atualmente replicados no cliente c

a_cada_tick_de_IM(cliente c):
    celulas = células que intersectam o círculo (pos(c), raio_interesse)   # hexágonos aproximam melhor
    relevantes = união de grade[cel] para cel em celulas
    para o em relevantes - scope[c]: enviar_criacao(c, o)   # content message: estado completo
    para o em scope[c] - relevantes: enviar_remocao(c, o)
    scope[c] = relevantes

ao_mudar_estado(o):
    para c com o em scope[c]: marcar_para_update(c, o)      # entra no priority accumulator / state mask
```

Variante obstacle-aware: substituir `celulas` por busca em largura no grafo de triângulos limitada por distância de caminho [F: boulanger2006comparing].

## Relações com outros conceitos

Parte de `rtm.sync.state-replication`; complementa `rtm.sync.snapshot-interpolation` e `rtm.sync.state-synchronization` reduzindo o conjunto de objetos a replicar, e `rtm.sync.dead-reckoning` via limiares por distância. Em arquiteturas de salas (`rtm.mp.rooms-and-matches`), a sala é a forma mais grosseira de IM. [I] O padrão publish-subscribe está em `rtm.rt.communication-patterns`.

## Lacunas e questões abertas

- Morse, Bic e Dillencourt (2000): só metadados verificados (Presence 9(1), 52-68, DOI 10.1162/105474600566619); o texto está atrás de acesso restrito.
- Liu e Theodoropoulos (2014): só o resumo verificado (ACM Computing Surveys, vol. 46, DOI 10.1145/2535417); a taxonomia completa não foi lida.
- Boulanger et al.: PDF da McGill aberto; o DOI (10.1145/1230040.1230069) apareceu em resultado de busca e não foi aberto na página do editor.
- Data Distribution Management da HLA (IEEE 1516.1) é o mecanismo normativo de IM em simulação militar, mas a página da norma não o menciona e o texto não foi aberto: não verificado.
- O experimento de Boulanger et al. é 2D, com 28 jogadores e obstáculos estáticos; generalização para 3D e milhares de jogadores é hipótese. [H]

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| boulanger2006comparing | academico | 2026-10-29 |
| morse2000interest | academico (metadados) | 2026-10-29 |
| liu2014interest | academico (resumo) | 2026-10-29 |
| frohnmayer2000tribes | tecnico | 2026-10-29 |
| fiedler2015statesync | tecnico | 2026-10-29 |
| madhav2015multiplayer | academico (sumário) | 2026-10-29 |
| ryan2006deadreckoning | academico | 2026-10-29 |
