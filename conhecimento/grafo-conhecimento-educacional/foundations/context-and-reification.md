---
id: kg.found.context-and-reification
titulo: Contexto, reificação e anotação de arestas
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, w3c2026rdf12concepts, w3c2014rdf11concepts, w3c2013provo, neo4j2026graphconcepts]
relacoes:
  - { tipo: parte-de, alvo: kg.found.knowledge-graphs }
  - { tipo: depende-de, alvo: kg.found.identifiers-and-triples }
  - { tipo: complementa, alvo: kg.eng.versioning-and-provenance }
  - { tipo: especificado-por, alvo: kg.std.prov-o }
  - { tipo: relacionado-a, alvo: kg.found.rdf-vs-property-graphs }
  - { tipo: relacionado-a, alvo: kg.mod.evidence-and-mastery }
termos: [contexto, reificação, RDF reification, n-ary relation, singleton property, named graph, triple term, reifier, triple annotation, RDF-star, proveniência, validade temporal]
---

# Contexto, reificação e anotação de arestas

## Definição e terminologia

Contexto, aqui, é tudo que qualifica uma afirmação sem fazer parte dela: desde quando vale, quem a produziu, com que confiança, sob que escopo. Hogan et al. tratam o assunto sob o título *context*, observando que dados podem ser verdadeiros apenas com respeito a um certo contexto, e dando o contexto temporal como exemplo central [F: hogan2021knowledgegraphs, §3.3].

**Reificação** é o mecanismo que permite "making statements about statements in a generic manner (or in the case of a graph, for defining edges about edges)" [F: hogan2021knowledgegraphs, §3.3.2].

Em RDF 1.2, um **triple term** é uma tripla RDF usada como termo dentro de outra tripla; uma **reifying triple** é uma tripla cujo predicado é `rdf:reifies` e cujo objeto é um triple term; o sujeito dessa tripla é o **reifier** [F: w3c2026rdf12concepts, §1.5]. Quando o triple term corresponde a uma tripla asserida no grafo, o subconjunto de triplas que têm o reifier como sujeito é chamado **triple annotation** [F: w3c2026rdf12concepts, §1.5].

O que não é: contexto não é metadado do arquivo. É metadado da afirmação, e precisa ser consultável junto com ela. [I]

## Problema que resolve

A tripla não tem onde guardar qualificação. "Conceito A é pré-requisito de conceito B" é uma afirmação; "segundo a curadoria de outubro de 2026, com confiança 0,8, válida para a versão 3 do currículo" é a mesma afirmação qualificada — e não cabe em três componentes.

[I] Em um grafo educacional isso não é detalhe: quase toda aresta interessante é contextual. Um pré-requisito vale para um currículo e não para outro; um alinhamento entre habilidade e item foi feito por alguém, em alguma data, e pode ser revisto; uma evidência de domínio tem timestamp e um instrumento de origem.

## Fundamentos e funcionamento

Hogan et al. organizam as opções em três famílias [F: hogan2021knowledgegraphs, §3.3]:

### 1. Representação direta

Tratar o contexto como dado qualquer: transformar a relação em nó. A aresta `A preRequisitoDe B` vira um nó `rel-1` ligado a origem, destino e aos atributos de contexto [F: hogan2021knowledgegraphs, §3.3.1]. Especificações existentes padronizam partes disso: a Time Ontology, para entidades e intervalos temporais, e o PROV Data Model, para proveniência — entidades derivadas de outras, geradas ou usadas por atividades, atribuídas a agentes [F: hogan2021knowledgegraphs, §3.3.1]. Ver kg.std.prov-o.

### 2. Reificação

Três formas documentadas para grafos dirigidos com arestas rotuladas [F: hogan2021knowledgegraphs, §3.3.2]:

| Forma | Como funciona |
|---|---|
| RDF reification | um nó novo representa a aresta e é ligado ao sujeito (via `subject`), ao objeto (via `object`) e ao rótulo (via `predicate`) |
| Relações n-árias | o nó de origem é ligado diretamente ao nó da aresta com o rótulo da aresta; o nó de destino é ligado ao nó da aresta via `value` |
| Singleton properties | o identificador da aresta é usado como o próprio rótulo da aresta, ligado ao rótulo original via `singleton` |

Ponto crítico: "in general, a reified edge does not assert the edge it reifies; for example, we may reify an edge to state that it is no longer valid" [F: hogan2021knowledgegraphs, §3.3.2].

### 3. Representação de aridade maior

Três opções [F: hogan2021knowledgegraphs, §3.3.3]:

- **Grafo nomeado**: colocar a aresta em um grafo nomeado e definir o contexto sobre o nome do grafo. É apontada como a mais flexível, porque permite atribuir contexto a várias arestas de uma vez.
- **Grafo de propriedades**: o contexto é um atributo da aresta [F: neo4j2026graphconcepts].
- **RDF-star**: extensão de RDF que permite definir arestas como nós [F: hogan2021knowledgegraphs, §3.3.3]. Esse caminho foi incorporado ao padrão em RDF 1.2 na forma de triple terms e reifying triples [F: w3c2026rdf12concepts, §1.5].

### O desenho de RDF 1.2

A especificação é explícita sobre quem deve aparecer nas demais afirmações: "it is expected that the reifiers (rather than the triple terms) will be used in further statements" [F: w3c2026rdf12concepts, §1.5]. O reifier pode denotar coisas variadas relacionadas à proposição do triple term, "such as a statement or belief that the proposition holds", e o significado de `rdf:reifies` é "deliberately generic" por causa dessa diversidade; pode haver múltiplos reifiers distintos para a mesma proposição abstrata, por exemplo afirmações com fontes diferentes [F: w3c2026rdf12concepts, §1.5].

Usando triple terms não asseridos "one can make statements about unasserted statements" — por exemplo, quando não se tem certeza de que a proposição é verdadeira [F: w3c2026rdf12concepts, §1.5]. Termos dentro de um triple term têm a mesma denotação que teriam em uma tripla asserida; por isso diz-se que triple terms são *transparentes* [F: w3c2026rdf12concepts, §1.5].

## Requisitos e pressupostos

- Decidir, antes de modelar, se o contexto se aplica a uma aresta ou a um conjunto de arestas. Se for conjunto, grafo nomeado é mais barato [F: hogan2021knowledgegraphs, §3.3.3].
- Saber se o consumidor do grafo fala a forma escolhida. RDF 1.2 ainda é Candidate Recommendation Snapshot (07/04/2026) [F: w3c2026rdf12concepts]; a reificação clássica de RDF 1.1 é universalmente suportada e verbosa.
- Aceitar o custo em triplas. [I] Reificar uma aresta custa pelo menos três a quatro triplas adicionais mais as do contexto.

## Vantagens e limitações

| Forma | Vantagem | Limitação |
|---|---|---|
| Nó de relação (direta) | funciona em qualquer stack; consultável com SPARQL simples | muda a forma do grafo; a aresta direta deixa de existir |
| RDF reification | padrão desde RDF 1.0; não assere a aresta | verbosa; consultas longas |
| Relações n-árias | menos indireção que a reificação clássica | semântica não padronizada |
| Singleton property | uma aresta por contexto | explode o número de predicados distintos |
| Grafo nomeado | contexto compartilhado por muitas arestas; é RDF padrão [F: w3c2014rdf11concepts, §4] | granularidade por grafo, não por aresta |
| Grafo de propriedades | atributo direto na aresta | fora do ecossistema RDF/SPARQL |
| Triple term (RDF 1.2) | padrão em curso, conciso, com sintaxe abreviada prevista em Turtle [F: w3c2026rdf12concepts, §1.5] | status ainda de Candidate Recommendation |

## Exemplo técnico independente de domínio

A mesma afirmação qualificada, em quatro formas:

```turtle
# 1. nó de relação (representação direta)
:rel-1 a :RelacaoPreRequisito ;
       :origem :cA ; :destino :cB ;
       :confianca 0.8 ;
       prov:wasAttributedTo :curadoria ;
       prov:generatedAtTime "2026-10-29T00:00:00Z"^^xsd:dateTime .

# 2. grafo nomeado: contexto compartilhado por muitas arestas
GRAPH <https://example.org/g/curadoria/2026-10> { :cA :preRequisitoDe :cB . }
<https://example.org/g/curadoria/2026-10>
       prov:wasAttributedTo :curadoria ;
       prov:generatedAtTime "2026-10-29T00:00:00Z"^^xsd:dateTime .

# 3. RDF reification (RDF 1.1)
_:r rdf:type rdf:Statement ;
    rdf:subject :cA ; rdf:predicate :preRequisitoDe ; rdf:object :cB ;
    :confianca 0.8 .

# 4. reifying triple com triple term (RDF 1.2)
:cA :preRequisitoDe :cB .                       # tripla asserida
_:x rdf:reifies <<( :cA :preRequisitoDe :cB )>> .
_:x :confianca 0.8 ; prov:wasAttributedTo :curadoria .
```

[I] As formas 1 e 2 são as únicas que funcionam hoje em qualquer triplestore com SPARQL 1.1. A forma 4 segue a especificação em curso e a sintaxe concreta depende do que Turtle 1.2 fixar — a especificação prevê que sintaxes concretas "may have shortcuts for specifying reifying triples and triple annotations more succinctly" [F: w3c2026rdf12concepts, §1.5], sem que a forma final tenha sido verificada aqui.

## Relações com outros conceitos

Parte de kg.found.knowledge-graphs. Depende de kg.found.identifiers-and-triples. Complementa kg.eng.versioning-and-provenance (grafo nomeado é ao mesmo tempo unidade de contexto e de versão). Especificado por kg.std.prov-o para o caso da proveniência. Relaciona-se com kg.found.rdf-vs-property-graphs (o grafo de propriedades resolve anotação de aresta nativamente) e com kg.mod.evidence-and-mastery (evidência é afirmação contextualizada por natureza).

## Lacunas e questões abertas

- Hogan et al. remetem a Hernández et al. para comparação detalhada de alternativas de reificação e suas forças e fraquezas relativas [F: hogan2021knowledgegraphs, §3.3.2]; esse trabalho não foi consultado.
- O custo de consulta de cada forma não foi medido em nenhuma fonte consultada.
- Qual forma adotar para anotar alinhamentos currículo-item em escala de milhares de arestas continua em aberto. [H] Grafo nomeado por lote de curadoria parece o melhor compromisso entre custo e granularidade, mas não há evidência aqui.
- A disponibilidade de triple terms em implementações não foi levantada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2026rdf12concepts | normativo | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| neo4j2026graphconcepts | fornecedor | 2026-10-29 |
