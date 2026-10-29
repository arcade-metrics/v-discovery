---
id: rtm.sync.operational-transformation
titulo: Operational Transformation (OT)
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ellis1989concurrency, nichols1995jupiter, ressel1996integrating, sun1998ot, preguica2018crdt, kleppmann2016json, crdttech2026]
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-replication }
  - { tipo: alternativa-a, alvo: rtm.sync.crdt }
  - { tipo: depende-de, alvo: rtm.net.logical-clocks }
  - { tipo: depende-de, alvo: rtm.rel.delivery-semantics }
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.rt.realtime-systems }
termos: [operational transformation, transformation function, state vector, precedence property, convergence property, dOPT, TP1, TP2, Jupiter]
---

# Operational Transformation (OT)

## Definição e terminologia

**Operational Transformation** é uma técnica de controle de concorrência para edição colaborativa em que cada sítio aplica suas operações imediatamente e, ao receber operações remotas geradas concorrentemente, as **transforma** em função das operações locais já executadas, de modo que o efeito pretendido seja preservado e todos os sítios convirjam. O artigo fundador é Ellis e Gibbs, "Concurrency control in groupware systems", SIGMOD '89, pp. 399-407, DOI 10.1145/67544.66963 [F: ellis1989concurrency; metadados verificados via Crossref, texto integral lido].

Ellis e Gibbs caracterizam sistemas groupware de tempo real como "highly interactive", "real-time" (tempos de notificação comparáveis aos de resposta), "distributed", "volatile" (participantes entram e saem), "ad hoc" e "focused" (alto grau de conflito de acesso) [F: ellis1989concurrency, §1]. O algoritmo proposto, **dOPT** (*distributed operational transformation*), tem como vantagens "its simplicity of use and its responsiveness: users can operate directly on the data without obtaining locks" [F: ellis1989concurrency, resumo].

Termos:

- **Transformation matrix**: "the key to resolving conflicting operations"; matriz m × m (m = número de tipos de operação) cujas entradas são funções que transformam uma operação em face de outra [F: ellis1989concurrency, §4.1].
- **State vector**: vetor com N componentes em que a i-ésima indica "quantas operações do sítio i foram executadas" pelo sítio j; usado para detectar precedência [F: ellis1989concurrency, §4.2].
- **Priority**: valor atribuído a cada operação, "based upon the site identifiers, and is application dependent", para desempatar transformações [F: ellis1989concurrency, §4].

O que não é: OT não é lock (justamente o evita) nem serialização por ordem total, que Ellis e Gibbs rejeitam por perda de responsividade [F: ellis1989concurrency, §3].

## Problema que resolve

Os autores definem duas propriedades de correção. **Precedence Property**: se uma operação o precede p, então em cada sítio a execução de o acontece antes da de p. **Convergence Property**: "site objects are identical at all sites at quiescence" (quiescência = todas as operações geradas foram executadas em todos os sítios). "A groupware system is correct iff the convergence property and the precedence property are always satisfied" [F: ellis1989concurrency, §3]. A precedência é definida por: o precede p se foram gerados no mesmo sítio e o antes de p, ou se a execução de o no sítio de p aconteceu antes da geração de p [F: ellis1989concurrency, §3]; [I] é a relação *happens-before* de Lamport aplicada a operações de edição (ver rtm.net.logical-clocks).

Os autores observam que estender a precedência a uma ordem total (por algoritmo distribuído ou coordenador central) satisfaz ambas as propriedades, mas "responsiveness is lost since operations are not executed when" geradas e o comportamento desejado "is non-serializable" [F: ellis1989concurrency, §3 e resumo]. Locking tem três problemas: custo de obter o lock, granularidade e momento de requisição e liberação [F: ellis1989concurrency, §2.1].

## Fundamentos e funcionamento

### Esquema do dOPT

Intuitivamente: ao gerar uma operação, o sítio a executa, calcula sua prioridade e a envia com seu state vector a todos os outros. Ao receber uma operação: se o remetente executou operações que o receptor ainda não executou ("future operation"), ela é enfileirada; senão, se o receptor executou operações que o remetente não viu ("past operation"), a prioridade é verificada e "the operation may be transformed before it is executed" [F: ellis1989concurrency, §4]. O algoritmo mantém por sítio uma fila de requisições, um log e um state vector; a operação é adicionada ao log e o state vector é incrementado após a execução [F: ellis1989concurrency, §4.3]. É "fully distributed, and resilient to site failure" [F: ellis1989concurrency, §4].

### Propriedades de transformação TP1 e TP2

[I] A literatura posterior formalizou condições sobre as funções de transformação. Com notação usual, para operações concorrentes a e b, com a' = T(a, b) e b' = T(b, a):

- **TP1** (convergência para dois sítios): aplicar a e depois b' leva ao mesmo estado que aplicar b e depois a'.
- **TP2** (consistência com três ou mais operações concorrentes): transformar uma operação c contra a·b' deve dar o mesmo resultado que contra b·a'.

Essas propriedades são atribuídas a Ressel, Nitsche-Ruhland e Gunzenhäuser, "An integrating, transformation-oriented approach to concurrency control and undo in group editors", CSCW '96, pp. 288-297, DOI 10.1145/240080.240305 [F: ressel1996integrating; metadados verificados via Crossref, texto não consultado, formulação acima não verificada contra o original]. Sun e Ellis, "Operational transformation in real-time group editors: issues, algorithms, and achievements", CSCW '98, pp. 59-68, DOI 10.1145/289444.289469, revisam a família de algoritmos [F: sun1998ot; metadados verificados, texto não consultado]. [H] Satisfazer TP2 em geral para inserções e deleções em texto é o ponto sabidamente difícil, e vários algoritmos publicados tiveram contraexemplos; esta afirmação é de conhecimento comum na área, não verificada aqui contra fonte primária.

### Jupiter e o modelo cliente-servidor

Nichols, Curtis, Dixon e Lamping, "High-latency, low-bandwidth windowing in the Jupiter collaboration system", UIST '95, pp. 111-120, DOI 10.1145/215585.215706 [F: nichols1995jupiter; metadados verificados via Crossref, texto não consultado]. [I] O modelo Jupiter, conforme descrito na literatura secundária, substitui a topologia totalmente distribuída do dOPT por um servidor central que mantém um caminho de transformação com cada cliente; como cada cliente só transforma contra o servidor, o problema se reduz a pares (apenas TP1 é necessária). Esta descrição não foi verificada no texto original e fica marcada como não verificada; é o modelo que sistemas cliente-servidor de edição colaborativa costumam seguir.

### Preservação de intenção

[I] A transformação precisa codificar a semântica da operação: Ellis e Gibbs afirmam que "the algorithm must know some semantics of the operations", embora sua "overall structure is independent of the semantic information" [F: ellis1989concurrency, resumo]. Para texto, inserir em posição p após uma inserção concorrente em posição q < p desloca p; para deleções sobrepostas, a transformação deve evitar deletar duas vezes.

## Requisitos e pressupostos

- Entrega confiável e, no dOPT, state vectors para enfileirar operações "futuras" até que as precedentes cheguem [F: ellis1989concurrency, §4]; ver rtm.rel.delivery-semantics.
- Conjunto finito e conhecido de tipos de operação (a matriz é m × m) [F: ellis1989concurrency, §4.1].
- Funções de transformação corretas para todos os pares (e, em topologia distribuída, satisfazendo TP2).
- [I] Em cliente-servidor, um servidor que serializa as operações e mantém histórico para transformar operações atrasadas de clientes.

## Vantagens e limitações

Vantagens: responsividade (execução local imediata) e ausência de locks [F: ellis1989concurrency, §4]; [I] estado replicado é o próprio documento, sem metadados por elemento; o servidor pode validar e rejeitar operações (afinidade com rtm.arch.authoritative-server).

Limitações: [I] correção das funções de transformação é difícil de garantir, sobretudo TP2; o histórico de operações precisa ser mantido enquanto houver clientes atrasados; offline longo significa transformar contra uma fila longa; a topologia P2P exige vetores de estado O(N) por mensagem [F: ellis1989concurrency, §4.2].

## Alternativas e comparações

| Critério | OT | CRDT | Fonte |
|---|---|---|---|
| Como resolve concorrência | transforma a operação remota contra as locais | projeta operações comutativas ou estados que formam semilattice | [F: ellis1989concurrency] [F: preguica2018crdt] |
| Metadados por elemento | não (posições) | sim (ids únicos, tombstones ou vetores) | [F: preguica2018crdt, §4.1.1] |
| Dependência de ordem de entrega | precisa detectar precedência (state vector) ou servidor serializador | op-based: causal; state-based: nenhuma | [F: ellis1989concurrency, §4.2] [F: preguica2018crdt, §3.1] |
| Servidor central | opcional no dOPT; usual em Jupiter | desnecessário | [F: ellis1989concurrency] [F: crdttech2026] |
| Merge no cliente sem rede ordenada | não | sim ("does not depend on ordering guarantees from the network") | [F: kleppmann2016json] |

**Quando cada um é adequado** [I]:

- OT: edição de texto ou estruturas lineares com um servidor que já é ponto de serialização, poucos tipos de operação, clientes quase sempre conectados, necessidade de validar operações no servidor.
- CRDT: topologia P2P ou multi-servidor, offline prolongado, dados estruturados (mapas, conjuntos, contadores) em que a semântica add-wins ou LWW é aceitável, tolerância a metadados.

## Métricas e métodos de avaliação

[I] Tempo de resposta local (deve ser próximo de zero); tempo de notificação (Ellis e Gibbs definem *response time* e *notification time* como as duas medidas [F: ellis1989concurrency, §1]); tamanho do histórico retido; verificação de TP1/TP2 por teste exaustivo de pares e triplas de operações; convergência por simulação com atrasos aleatórios.

## Exemplo técnico independente de domínio

Transformação para duas operações em uma sequência (inserir e deletar), ilustrando TP1 em pseudocódigo; derivado do esquema de Ellis e Gibbs, não copiado de fonte:

```
op Ins(p, c)   # insere caractere c na posição p
op Del(p)      # remove o caractere na posição p

T(Ins(p1,c1), Ins(p2,c2)):          # transformar a primeira contra a segunda
  se p1 < p2 ou (p1 = p2 e prioridade(a) < prioridade(b)): retornar Ins(p1, c1)
  senão: retornar Ins(p1 + 1, c1)
T(Ins(p1,c), Del(p2)):  se p1 <= p2: Ins(p1, c) senão Ins(p1 - 1, c)
T(Del(p1), Ins(p2,c)):  se p1 < p2: Del(p1) senão Del(p1 + 1)
T(Del(p1), Del(p2)):    se p1 < p2: Del(p1); se p1 > p2: Del(p1 - 1); se p1 = p2: NoOp

verificação TP1 (teste): para todo estado s e par concorrente (a, b):
  aplicar(aplicar(s, a), T(b, a)) = aplicar(aplicar(s, b), T(a, b))
```

Esquema cliente-servidor com servidor serializador (modelo tipo Jupiter, [I]):

```
cliente: ao editar: aplicar local; enviar (op, versao_conhecida); pendentes += op
servidor: ao receber (op, v): para cada op' no histórico com versão > v: op := T(op, op')
          aplicar; histórico += op; versão++; difundir (op, versão) aos demais
cliente: ao receber op remota: para cada p em pendentes: (op, p) := (T(op, p), T(p, op)); aplicar op
```

## Relações com outros conceitos

Parte de rtm.sync.state-replication. Alternativa a rtm.sync.crdt. Depende de rtm.net.logical-clocks (precedência, state vectors) e de rtm.rel.delivery-semantics. Relaciona-se com rtm.arch.authoritative-server (servidor serializador que valida), rtm.pred.client-side-prediction (execução local otimista com correção posterior é análoga) e rtm.rt.realtime-systems (definições de tempo de resposta e notificação).

## Lacunas e questões abertas

- Textos de Nichols et al. 1995, Ressel et al. 1996 e Sun e Ellis 1998 não acessíveis nesta sessão (ACM retornou 403); apenas metadados via Crossref. A formulação de TP1/TP2 e a descrição do Jupiter estão marcadas como não verificadas.
- O artigo de Ellis e Gibbs foi lido em cópia de curso (decomposition.al), não no repositório da ACM.
- Não há, nas fontes consultadas, avaliação empírica comparando OT e CRDT em latência, largura de banda e tamanho de estado para o mesmo caso de uso; fica como questão aberta para rtm.perf.metrics.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ellis1989concurrency | academico | 2026-10-29 |
| nichols1995jupiter | academico | 2026-10-29 |
| ressel1996integrating | academico | 2026-10-29 |
| sun1998ot | academico | 2026-10-29 |
| preguica2018crdt | academico | 2026-10-29 |
| kleppmann2016json | academico | 2026-10-29 |
| crdttech2026 | tecnico | 2026-10-29 |
