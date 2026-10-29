---
id: rtm.sync.crdt
titulo: CRDT (Conflict-free Replicated Data Types)
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [shapiro2011crdt, preguica2018crdt, kleppmann2016json, roh2011rga, nicolaescu2016yata, yjs2026docs, yjs2026readme, yjs2026sharedtypes, yjs2026awareness, automerge2026hello, automerge2026conflicts, automerge2026mergerules, automerge2026counters, automerge2026text, automerge2026concepts, crdttech2026, ellis1989concurrency]
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-replication }
  - { tipo: alternativa-a, alvo: rtm.sync.operational-transformation }
  - { tipo: depende-de, alvo: rtm.net.logical-clocks }
  - { tipo: depende-de, alvo: rtm.rel.delivery-semantics }
  - { tipo: complementa, alvo: rtm.mp.presence }
  - { tipo: relacionado-a, alvo: rtm.arch.peer-to-peer }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.sync.delta-compression }
termos: [CRDT, strong eventual consistency, state-based CRDT, operation-based CRDT, join semilattice, G-Counter, PN-Counter, LWW-Register, OR-Set, add-wins set, RGA, tombstone, delta-state CRDT, state vector]
---

# CRDT (Conflict-free Replicated Data Types)

## Definição e terminologia

Um **CRDT** é um tipo de dado replicado cujas réplicas podem ser atualizadas de forma independente e concorrente, sem coordenação, e que convergem para o mesmo estado por construção. O índice crdt.tech, mantido por Kleppmann, Bieniusa e Shapiro, define: "a data structure that simplifies distributed data storage systems and multi-user applications"; réplicas "can always be merged into a consistent state", automaticamente, "without requiring any special conflict resolution code or user intervention", e "they do not assume the use of a single server" [F: crdttech2026].

O artigo fundador é Shapiro, Preguiça, Baquero e Zawirski, "Conflict-Free Replicated Data Types", em *Stabilization, Safety, and Security of Distributed Systems* (SSS 2011), LNCS, pp. 386-400, DOI 10.1007/978-3-642-24550-3_29 [F: shapiro2011crdt; metadados verificados via Crossref, texto integral não acessível nesta sessão]. Uma versão técnica estendida (INRIA RR-7506, "A comprehensive study of Convergent and Commutative Replicated Data Types") é citada na literatura, mas não pôde ser aberta (não verificado).

Duas famílias [F: preguica2018crdt, §3.1]:

- **State-based** (CvRDT, *convergent*): réplicas trocam estados e aplicam uma função `merge`.
- **Operation-based** (CmRDT, *commutative*): réplicas propagam operações; cada atualização tem um *generator* (sem efeitos colaterais, roda na origem) e um *effector* (aplicado em todas as réplicas).

A garantia é **strong eventual consistency (SEC)**: além de convergir eventualmente, duas réplicas que receberam o mesmo conjunto de atualizações têm o mesmo estado imediatamente, sem rollback. [I] A definição formal está em Shapiro et al. 2011; aqui está parafraseada a partir do resumo de Preguiça: "CRDTs guarantee that all replicas converge to the same state when all updates propagate to all replicas" [F: preguica2018crdt, §3].

O que não é: CRDT não é consenso (não escolhe um valor único em disputa; incorpora todos ou aplica uma regra determinística) nem transação (não dá atomicidade entre objetos).

## Problema que resolve

Sistemas geo-replicados com consistência fraca deixam réplicas "temporarily diverge" e precisam de um mecanismo para fundir atualizações concorrentes; CRDTs são apresentados como "a principled answer" a esse problema [F: preguica2018crdt, resumo]. Em colaboração em tempo real, o problema equivalente é permitir que cada usuário edite localmente, inclusive offline, e que todos convirjam ao reconectar; Automerge afirma que cada usuário pode atualizar sua cópia "even offline" e que as mudanças concorrentes "merge automatically" sem servidor central [F: automerge2026hello].

## Fundamentos e funcionamento

### Condições de convergência

Para state-based, Preguiça resume o resultado de Shapiro et al.: as réplicas convergem se (i) os estados possíveis formam um *join semilattice* sob uma ordem parcial ≤; (ii) toda atualização é uma inflação, `s ≤ u(s)`; (iii) `merge` produz o *join* (menor limite superior) `s1 ⊔ s2` [F: preguica2018crdt, §3.1.1]. Basta que o grafo de sincronização seja conexo para que todas as atualizações cheguem a todas as réplicas [F: preguica2018crdt, §3.1.1].

Para operation-based: se os effectors forem entregues em ordem causal, as réplicas convergem se as operações concorrentes comutam; sem ordem causal, todas devem comutar; se puderem ser entregues mais de uma vez, devem ser idempotentes; "most operation-based CRDT designs require exactly-once and causal delivery" [F: preguica2018crdt, §3.1.2]. Ver rtm.rel.delivery-semantics e rtm.net.logical-clocks.

### Variantes de sincronização

*Delta-state CRDTs* propagam *delta-mutators* (mudanças desde a última comunicação) em vez do estado inteiro; na primeira comunicação o estado completo é necessário. *Pure operation-based* propagam a operação original, ao custo de mais metadados. Quando atualizações devem ser propagadas imediatamente, "state-based synchronization is the worst choice"; após falhas, state-based e delta-based permitem ressincronizar recebendo o estado [F: preguica2018crdt, §3.1.3-3.1.4].

### Metadados e coleta de lixo

Projetos antigos (sobretudo state-based) guardavam *tombstones* para dados removidos, tornando o armazenado "larger (and sometimes much larger) than the actual data"; projetos modernos evitam isso, mas ainda guardam metadados "que crescem linearmente com o número de réplicas" para rastrear concorrência e predecessores causais, por exemplo um vector clock O(n) no add-wins set state-based [F: preguica2018crdt, §4.1.1]. O Yjs remove conteúdo deletado e mescla structs precedentes para reduzir metadados; tombstones só podem ser coletados "when struct order no longer matters", como quando o pai foi deletado; a coleta pode ser desativada para restaurar conteúdo antigo [F: yjs2026readme].

### Relação com relógios lógicos

Identificadores únicos de operação costumam ser pares (timestamp, id de réplica); com um relógio de Lamport é possível definir uma ordem total compatível com *happens-before* [F: preguica2018crdt, §4.1, nota 17]. O Yjs identifica cada struct por (client, clock) e usa um *state vector* com "o próximo clock esperado de cada cliente" para calcular o que falta a um par; a documentação observa que isso é "similar a version vectors mas não é usado para rastrear causalidade" [F: yjs2026readme]. O Automerge decide concorrência na mesma chave por LWW "using the operation's internal ID, not wall-clock time", comparando primeiro o contador e desempatando pelo actor ID [F: automerge2026conflicts]. Ver rtm.net.logical-clocks.

## Algoritmos e modelos relevantes

| CRDT | Família | Semântica | Fonte |
|---|---|---|---|
| Counter op-based | op | `inc(n)` com effector `val := val + n`; comutativo | [F: preguica2018crdt, alg. 1] |
| G-Counter / PN-Counter | state | vetor de parciais positivos e negativos por réplica; `merge` por max e min por entrada; valor = Σ | [F: preguica2018crdt, alg. 2] |
| LWW-Register | state | (valor, timestamp totalmente ordenado); `merge` mantém o maior timestamp | [F: preguica2018crdt, alg. 3] |
| OR-Set / add-wins set | op | pares (elemento, uid); `rmv` remove só os uids observados; adds concorrentes a um remove vencem | [F: preguica2018crdt, alg. 4] |
| Add-wins set state-based | state | pares + vector clock; `merge` descarta pares ausentes no outro lado mas já observados por ele | [F: preguica2018crdt, alg. 5] |
| Sequências (Treedoc, Logoot, RGA, WOOT) | ambas | ids densos que codificam posição relativa (Treedoc usa árvore) ou ligação ao predecessor | [F: preguica2018crdt, §4.1] [F: roh2011rga] |
| YATA | op | base do Yjs; implementação "modificada" do algoritmo do artigo de Nicolaescu et al. 2016 | [F: yjs2026readme] [F: nicolaescu2016yata] |
| JSON CRDT | op | listas e mapas aninhados, merge no cliente, "does not depend on ordering guarantees from the network" | [F: kleppmann2016json] |

RGA (*Replicated Growable Array*) é definido em Roh, Jeon, Kim e Lee, "Replicated abstract data types: Building blocks for collaborative applications", JPDC 71(3), 2011, pp. 354-368, DOI 10.1016/j.jpdc.2010.12.006 [F: roh2011rga; metadados verificados, texto não consultado].

### Implementações

**Yjs**: "A CRDT framework with a powerful abstraction of shared data"; tipos `Y.Map`, `Y.Array`, `Y.Text`, `Y.XmlFragment`, `Y.XmlElement`, `Y.XmlText` [F: yjs2026sharedtypes]; atualizações binárias (formato V1 padrão, V2 opcional com "much better compression"), `encodeStateAsUpdate` com state vector alvo para enviar só diferenças, `mergeUpdates`, `diffUpdate`; atualizações são "commutative" e "idempotent", logo "can be applied in any order and multiple times" [F: yjs2026readme]; a página inicial afirma que "the order in which document updates are applied doesn't matter" e que "Yjs doesn't need a central source of truth" [F: yjs2026docs]. A documentação do fornecedor afirma ser "the fastest CRDT implementation by far", citando um repositório de benchmarks [F: yjs2026docs]; afirmação não verificada de forma independente. Provedores de rede (y-websocket, y-webrtc, Hocuspocus, entre outros) e de persistência (y-indexeddb etc.) são listados [F: yjs2026readme]. O README nota que um projeto de prova formal encontrou que "the pseudocode in the original YATA paper contains errors" [F: yjs2026readme].

**Automerge**: "a library of data structures for building collaborative applications"; cada mudança retorna um "immutable snapshot"; funciona com "any connection-oriented network protocol" e até por transferência unidirecional; implementações JavaScript e Rust (WebAssembly, C API) [F: automerge2026hello]. Regras de fusão: mapas mantêm sets concorrentes em chaves distintas; na mesma chave "all nodes agree on the chosen value" e os perdedores ficam acessíveis por `getConflicts` com semântica de registro multivalor; listas identificam elementos por id, inserções concorrentes após o mesmo elemento são ordenadas arbitrariamente mas igual em todos os nós; texto segue as regras de listas, formatação segue Peritext; contadores somam todos os incrementos [F: automerge2026mergerules] [F: automerge2026conflicts] [F: automerge2026counters]. Texto é editado por `splice`; `updateText` computa diffs e a documentação recomenda chamá-lo "after every keystroke" porque diffs grandes "will not merge well with concurrent changes" [F: automerge2026text]. Repositórios e `DocHandle` tratam rede e armazenamento, com "an efficient sync protocol" por documento [F: automerge2026concepts].

## Requisitos e pressupostos

- Entrega confiável; op-based tipicamente exige entrega causal e exatamente-uma-vez, ou operações comutativas e idempotentes [F: preguica2018crdt, §3.1.2].
- Identificadores únicos de réplica ou cliente (Yjs `clientID`, Automerge actor ID) e relógios lógicos; ver rtm.net.logical-clocks.
- Grafo de sincronização conexo para state-based [F: preguica2018crdt, §3.1.1].
- Aceitação, pelo produto, da semântica de conflito escolhida (add-wins, remove-wins, LWW); Preguiça observa que o desenvolvedor "must select" entre elas [F: preguica2018crdt, §2].

## Vantagens e limitações

Vantagens: sem servidor central nem coordenação; offline nativo; convergência garantida por construção [F: crdttech2026] [F: automerge2026hello]. Limitações: metadados que crescem com réplicas e com histórico [F: preguica2018crdt, §4.1.1]; semântica de conflito fixa por tipo, nem sempre a que o usuário espera ([I] LWW em texto perde intenção); state-based é caro para propagação imediata [F: preguica2018crdt, §3.1.4]; [I] invariantes globais (por exemplo, "no máximo um vencedor") não são expressáveis sem coordenação.

## Alternativas e comparações

| Critério | CRDT | OT (rtm.sync.operational-transformation) | Servidor autoritativo (rtm.arch.authoritative-server) |
|---|---|---|---|
| Topologia | P2P ou cliente-servidor | tipicamente cliente-servidor | cliente-servidor |
| Ordem de entrega | op-based: causal; state-based: qualquer | sequência do servidor | sequência do servidor |
| Offline | nativo | difícil (histórico de transformações) | não |
| Metadados | ids e vetores por elemento | log de operações no servidor | estado único |
| Invariantes globais | não | parcial (servidor pode rejeitar) | sim |

[I] Fontes: comparação derivada das propriedades documentadas em [F: preguica2018crdt] e [F: ellis1989concurrency]; ver o documento de OT para detalhes.

## Métricas e métodos de avaliação

[I] Tamanho do estado e dos metadados em função do número de operações e réplicas; tamanho de atualização por edição; tempo de merge; tempo de carga de documento com histórico; convergência verificada por teste de propriedade (aplicar operações em permutações e comparar estados). Yjs cita um repositório de benchmarks [F: yjs2026docs]; Kleppmann e Beresford formalizam a semântica para prova de convergência [F: kleppmann2016json].

## Exemplo técnico independente de domínio

G-Counter state-based (adaptado de [F: preguica2018crdt, alg. 2], só a parte positiva):

```
estado: P: mapa<replica, int>, todos 0
inc(): P[eu] := P[eu] + 1
valor(): Σ_r P[r]
merge(X, Y): para cada r em chaves(X) ∪ chaves(Y): Z[r] := max(X[r], Y[r])
propriedades: inc é inflação (P só cresce); merge é join por componente; comuta, associa, idempotente
```

OR-Set op-based (adaptado de [F: preguica2018crdt, alg. 4]):

```
estado: S: conjunto de pares (elemento, uid), inicial ∅
lookup(e): existe (e, u) em S
add(e):  generator -> (add, e, novo_uid())      # uid = (clock_lamport, replica)
         effector(e, u) -> S := S ∪ {(e, u)}
rmv(e):  generator -> (rmv, e, {u | (e, u) ∈ S})  # só uids observados
         effector(e, U) -> S := S \ {(e, u) | u ∈ U}
concorrência: add(e) em A ∥ rmv(e) em B  -> o uid novo de A não está em U de B  -> e permanece (add-wins)
requisito: entrega causal e exatamente-uma-vez dos effectors
```

## Relações com outros conceitos

Parte de rtm.sync.state-replication. Alternativa a rtm.sync.operational-transformation. Depende de rtm.net.logical-clocks (ids e ordem causal) e de rtm.rel.delivery-semantics (entrega causal, exatamente-uma-vez). Complementa rtm.mp.presence (awareness do Yjs é um CRDT de estado efêmero [F: yjs2026awareness]). Relaciona-se com rtm.arch.peer-to-peer, rtm.rel.reconnection (ressincronização por state vector) e rtm.sync.delta-compression (delta-state).

## Lacunas e questões abertas

- Texto integral de Shapiro et al. 2011 e do RR-7506 não acessível nesta sessão (HAL bloqueou acesso automatizado; Springer exige sessão); a definição formal de SEC e o teorema de equivalência state/op-based estão citados por intermédio de Preguiça 2018.
- Texto de Roh et al. 2011 (RGA) e de Nicolaescu et al. 2016 (YATA) não consultado; só metadados.
- A alegação de desempenho do Yjs é do fornecedor; falta benchmark independente revisado.
- Como combinar CRDT com um servidor que aplica invariantes de jogo (por exemplo, inventário limitado) é questão aberta; a literatura consultada trata colaboração, não regras competitivas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| shapiro2011crdt | academico | 2026-10-29 |
| preguica2018crdt | academico | 2026-10-29 |
| kleppmann2016json | academico | 2026-10-29 |
| roh2011rga | academico | 2026-10-29 |
| nicolaescu2016yata | academico | 2026-10-29 |
| yjs2026docs | fornecedor | 2026-10-29 |
| yjs2026readme | fornecedor | 2026-10-29 |
| yjs2026sharedtypes | fornecedor | 2026-10-29 |
| yjs2026awareness | fornecedor | 2026-10-29 |
| automerge2026hello | fornecedor | 2026-10-29 |
| automerge2026conflicts | fornecedor | 2026-10-29 |
| automerge2026mergerules | fornecedor | 2026-10-29 |
| automerge2026counters | fornecedor | 2026-10-29 |
| automerge2026text | fornecedor | 2026-10-29 |
| automerge2026concepts | fornecedor | 2026-10-29 |
| crdttech2026 | tecnico | 2026-10-29 |
| ellis1989concurrency | academico | 2026-10-29 |
