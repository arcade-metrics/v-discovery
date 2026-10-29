---
id: rtm.net.logical-clocks
titulo: Relógios lógicos (happens-before, relógios de Lamport, relógios vetoriais, relógios híbridos)
tipo: conceito
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [lamport1978time, lamport2026pubs, mattern1989virtual, schwarz1994detecting, kulkarni2014logical, shapiro2011crdt, rfc5905, fiedler2014lockstep]
relacoes:
  - { tipo: complementa, alvo: rtm.net.clock-synchronization }
  - { tipo: complementa, alvo: rtm.net.ordering-and-reliability }
  - { tipo: depende-de, alvo: rtm.rt.communication-patterns }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
  - { tipo: relacionado-a, alvo: rtm.sync.operational-transformation }
  - { tipo: relacionado-a, alvo: rtm.arch.event-driven }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: relacionado-a, alvo: rtm.mp.turn-based }
termos: [happens-before, relógio lógico, relógio de Lamport, relógio vetorial, eventos concorrentes, ordem causal, ordem total, hybrid logical clock, timestamp lógico]
---

# Relógios lógicos

## Definição e terminologia

Um **relógio lógico** atribui a cada evento um número (ou vetor) que respeita a ordem em que os eventos **podem ter se influenciado**, sem recorrer a tempo físico. Lamport define a relação **happened before** (`→`) por três condições: (1) `a` e `b` no mesmo processo e `a` antes de `b`; (2) `a` é o envio de uma mensagem e `b` sua recepção; (3) transitividade. Dois eventos são **concorrentes** se nenhum `→` o outro: "a → b means that it is possible for event a to causally affect event b. Two events are concurrent if neither can causally affect the other" [F: lamport1978time, §The Partial Ordering]. O artigo foi publicado em *Communications of the ACM* 21(7), 558-565, julho de 1978 [F: lamport1978time; lamport2026pubs].

O **Clock Condition** exige: "if a → b then C(a) < C(b)"; a recíproca não pode valer, pois obrigaria eventos concorrentes a ter o mesmo tempo [F: lamport1978time, §Logical Clocks]. Em terminologia posterior, um relógio que satisfaz só a implicação é **consistente com a causalidade**; um que satisfaz a equivalência **caracteriza a causalidade** [F: schwarz1994detecting, Def. 3.1].

## Problema que resolve

Em um sistema distribuído não há relógio comum confiável (ver `rtm.net.clock-synchronization`), mas é preciso: decidir se um evento pode ter causado outro; impor uma ordem total consistente em todos os nós (para replicar uma máquina de estados); e detectar atualizações concorrentes (para resolver conflitos). Lamport observa que uma ordem total das requisições "leads immediately to an algorithm to implement an arbitrary state machine" [F: lamport2026pubs]. Mattern parte do fato de que "a common time base does not exist" e que uma estrutura linear de tempo "is not (always) adequate for distributed systems" [F: mattern1989virtual, Abstract].

## Fundamentos e funcionamento

### Relógios de Lamport

Regras de implementação [F: lamport1978time, §Logical Clocks]:

- **IR1**: cada processo incrementa seu contador entre dois eventos sucessivos.
- **IR2**: (a) toda mensagem carrega `Tm = Ci(a)` do evento de envio; (b) ao receber, o processo ajusta seu contador para um valor maior que `Tm` e que o valor atual.

Para obter uma **ordem total** `⇒`, ordena-se pelos tempos e, em empate, por "any arbitrary total ordering < of the processes": `a ⇒ b` sse `Ci(a) < Cj(b)` ou (`Ci(a) = Cj(b)` e `Pi < Pj`) [F: lamport1978time, §Ordering the Events Totally]. A ordem total não é única; só a ordem parcial é determinada pelo sistema [F: lamport1978time, idem].

**Comportamento anômalo**: se o usuário cria dependências fora do sistema (telefona a alguém que emite outra requisição), a ordem total pode contrariar a percepção; a solução é a **Strong Clock Condition** com relógios físicos sincronizados [F: lamport1978time, §Anomalous Behavior; ver `rtm.net.clock-synchronization`].

### Relógios vetoriais

Lamport time "does not characterize causality": `L(e) < L(e')` pode ocorrer entre eventos independentes [F: schwarz1994detecting, §3]. Mattern propõe "vectors of clocks" que são "partially ordered and form a lattice" e representam a causalidade "in an isomorphic way" [F: mattern1989virtual, Abstract]; Fidge (1988) é creditado com proposta independente, mas seu artigo **não foi verificado** nesta sessão. Regras, com um componente por processo [F: mattern1989virtual, §Vector time; schwarz1994detecting, Def. 2.5]:

- evento local ou envio: `V[i] += 1`; a mensagem carrega `V`;
- recepção: `V = max(V, V_msg)` componente a componente, depois `V[i] += 1`.

Comparação: `u ≤ v` sse `u[k] ≤ v[k]` para todo `k`; `u < v` sse `u ≤ v` e `u ≠ v`; `u ‖ v` sse nem `u < v` nem `v < u`. Teorema: `e → e'` sse `V(e) < V(e')`, e `e ‖ e'` sse `V(e) ‖ V(e')` [F: schwarz1994detecting, Def. 3.2, Teor. 3.3]. O custo é o tamanho dos vetores, "a major drawback" para computações massivamente paralelas [F: schwarz1994detecting, §4].

### Relógios híbridos (HLC)

Kulkarni et al. propõem um relógio que "captures the causality relationship like logical clocks" e cujo componente lógico se mantém "always close to the NTP clock"; cabe nos 64 bits do carimbo NTP e tolera "NTP kinks and uncertainties"; os requisitos são: consistência com happens-before, espaço O(1), representação limitada e `|l.e − pt.e|` limitado [F: kulkarni2014logical, Abstract, §2]. Os autores mostram que um relógio de Lamport "ancorado" ingenuamente ao tempo físico deixa a diferença crescer sem limite em laços de mensagens [F: kulkarni2014logical, §3]. A versão publicada é "Logical Physical Clocks", OPODIS 2014, LNCS, pp. 17-32 [F: kulkarni2014logical, registro Crossref].

## Algoritmos e modelos relevantes

| Relógio | Tamanho | Garante | Detecta concorrência | Fonte |
|---|---|---|---|---|
| Lamport | 1 inteiro | consistente com `→`; ordem total com desempate | não | [F: lamport1978time] |
| vetorial | N inteiros | caracteriza `→` | sim | [F: mattern1989virtual; schwarz1994detecting] |
| híbrido (HLC) | 64 bits | consistente com `→`; próximo do físico | não | [F: kulkarni2014logical] |

## Requisitos e pressupostos

Relógios de Lamport e vetoriais pressupõem que **toda** comunicação carregue o carimbo (IR2a) e que recepções sejam processadas com a regra de ajuste; comunicação "por fora" (outro canal, humano) quebra a Strong Clock Condition [F: lamport1978time, §Anomalous Behavior]. Vetores exigem conhecer o conjunto de processos ou usar representação esparsa por pares `(id, contador)` [F: schwarz1994detecting, nota 2].

## Vantagens e limitações

Vantagens: independência de tempo físico; ordem total determinística para replicação; detecção exata de concorrência (vetores). Limitações: Lamport não detecta concorrência; vetores crescem com N; nenhum deles informa **quanto** tempo passou, o que importa para interpolação e buffers (ver `rtm.net.jitter`) [I].

## Alternativas e comparações

Em multiplayer, três estratégias de ordenação coexistem [I]:

1. **Servidor autoritativo como sequenciador**: o servidor atribui um número de tick/sequência a cada evento; isso é um relógio de Lamport centralizado, cuja ordem total é a do servidor (ver `rtm.arch.authoritative-server`).
2. **Lockstep**: a ordem é o número do quadro, e todas as entradas de um quadro são aplicadas em ordem fixa de jogador, que é o desempate "por processo" de Lamport [F: fiedler2014lockstep; lamport1978time].
3. **Colaboração sem servidor sequenciador** (CRDT, OT): réplicas precisam saber se duas operações são concorrentes; CRDTs baseados em operações exigem entrega causal e identificadores únicos, e os vetores de versão são o mecanismo usual. O artigo de Shapiro et al. (SSS 2011) teve apenas o registro bibliográfico verificado [F: shapiro2011crdt]; ver `rtm.sync.crdt` e `rtm.sync.operational-transformation`.

Comparação com relógios físicos: o NTP entrega offsets de dezenas de ms na Internet [F: rfc5905, §1], insuficiente para ordenar eventos separados por menos que isso; relógios lógicos ordenam corretamente qualquer par causalmente relacionado, independentemente do atraso [I].

## Métricas e métodos de avaliação

Tamanho dos carimbos (bytes por mensagem); fração de pares concorrentes detectados (só vetores); para HLC, `max |l − pt|` observado, que os autores reportam como "bounded" e pequeno sob estresse [F: kulkarni2014logical, §5].

## Exemplo técnico independente de domínio

Relógio vetorial para réplicas que trocam operações de edição:

```
estado: V = [0]*N; eu = i
ao gerar operacao op:
    V[eu] += 1; op.ts = copia(V); aplicar(op); difundir(op)
ao receber op de j:
    # entrega causal: todas as dependências já vistas?
    pronta = op.ts[j] == V[j] + 1 and all(op.ts[k] <= V[k] for k != j)
    if not pronta: adiar(op); return
    for k: V[k] = max(V[k], op.ts[k])
    aplicar(op)
comparar(a, b):
    if a.ts < b.ts: "a → b"  elif b.ts < a.ts: "b → a"  else: "concorrentes -> resolver conflito"
```

Relógio de Lamport para um sequenciador: substituir o vetor por um inteiro e desempatar por id de réplica, obtendo a ordem total `⇒` [F: lamport1978time].

## Relações com outros conceitos

Complementa `rtm.net.clock-synchronization` (tempo físico) e `rtm.net.ordering-and-reliability` (ordem por canal vs. ordem causal); depende de `rtm.rt.communication-patterns` (mensagens são o veículo dos carimbos); fundamenta `rtm.sync.crdt` e `rtm.sync.operational-transformation`; relaciona-se a `rtm.arch.event-driven`, `rtm.arch.deterministic-lockstep` e `rtm.mp.turn-based`.

## Lacunas e questões abertas

- Fidge (1988) não foi aberto (cópias indisponíveis); a atribuição de autoria conjunta dos relógios vetoriais fica como não verificada.
- O artigo de Shapiro et al. sobre CRDT só teve o registro Crossref verificado; a afirmação sobre entrega causal e vetores de versão deve ser confirmada em `rtm.sync.crdt`.
- Não foram encontradas fontes do domínio de jogos que usem relógios vetoriais explicitamente; a prática dominante é o sequenciador central. Falta levantamento em colaboração em tempo real.
- O artigo de Lamport foi lido em PDF digitalizado com OCR; citações literais foram conferidas, mas a numeração de seções segue os títulos, não números.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| lamport1978time | academico | 2026-10-29 |
| lamport2026pubs | tecnico | 2026-10-29 |
| mattern1989virtual | academico | 2026-10-29 |
| schwarz1994detecting | academico | 2026-10-29 |
| kulkarni2014logical | academico | 2026-10-29 |
| shapiro2011crdt | academico (registro Crossref) | 2026-10-29 |
| rfc5905 | normativo | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
