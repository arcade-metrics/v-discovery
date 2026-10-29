---
id: kg.found.knowledge-graphs
titulo: Grafo de conhecimento
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, w3c2014rdf11concepts, neo4j2026graphconcepts, fettach2022kgeducation, zhao2022edukg, alatrash2025prerequisite, wilkinson2016fair]
relacoes:
  - { tipo: depende-de, alvo: kg.found.identifiers-and-triples }
  - { tipo: complementa, alvo: kg.found.ontologies }
  - { tipo: complementa, alvo: kg.found.context-and-reification }
  - { tipo: especificado-por, alvo: kg.std.rdf }
  - { tipo: relacionado-a, alvo: kg.found.rdf-vs-property-graphs }
  - { tipo: relacionado-a, alvo: kg.found.reasoning }
  - { tipo: relacionado-a, alvo: kg.mod.conceptual-model }
termos: [knowledge graph, data graph, directed edge-labelled graph, property graph, graph dataset, entidade, relação, schema, identity, context]
---

# Grafo de conhecimento

## Definição e terminologia

Não há definição única. O survey de Hogan et al. registra que "the definition of a 'knowledge graph' remains contentious", com definições variando de propostas técnicas específicas a propostas gerais inclusivas [F: hogan2021knowledgegraphs, §1]. Os autores adotam uma definição inclusiva: um grafo de conhecimento é "a graph of data intended to accumulate and convey knowledge of the real world, whose nodes represent entities of interest and whose edges represent relations between these entities" [F: hogan2021knowledgegraphs, §1].

Nessa definição, o *grafo de dados* (*data graph*) obedece a um modelo de dados baseado em grafo, que pode ser um grafo dirigido com arestas rotuladas, um grafo de propriedades ou outro [F: hogan2021knowledgegraphs, §1]. "Conhecimento" é "something that is known": pode ser acumulado de fontes externas ou extraído do próprio grafo. Afirmações simples ("Santiago é a capital do Chile") cabem como arestas; afirmações quantificadas ("toda capital é uma cidade") exigem representação mais expressiva, como ontologias ou regras, e então métodos dedutivos podem derivar conhecimento adicional [F: hogan2021knowledgegraphs, §1].

Três elementos recorrentes, porque grafos de conhecimento costumam ser montados a partir de muitas fontes, com estrutura e granularidade diversas: *schema* (estrutura de alto nível), *identity* (que nós se referem a que coisa no mundo ou em fontes externas) e *context* (sob que condições uma afirmação vale) [F: hogan2021knowledgegraphs, §1].

O que não é: um grafo de conhecimento não é por si só uma ontologia (ver kg.found.ontologies — a ontologia é o esquema, não os dados), não é um banco de dados de um tipo específico (o modelo é independente da implementação) e não é um índice vetorial (ver kg.ret.graph-embeddings).

**Grafo de conhecimento educacional (EduKG)** é o recorte deste domínio: um grafo cujas entidades são conceitos, competências, objetivos de aprendizagem, recursos, atividades e instrumentos, e cujas arestas são as relações entre eles. [I] O termo aparece na literatura sem definição normativa; os trabalhos consultados o usam operacionalmente para designar grafos que "organize various learning entities and their relationships to support structured and adaptive learning" [F: alatrash2025prerequisite, resumo]. A escala varia em ordens de magnitude: de ontologias de 4 a 6 classes em grafos de MOOC a 635 classes e 3,86 bilhões de triplos no EDUKG, para K-12 [F: zhao2022edukg, resumo e §1].

## Problema que resolve

Dados educacionais chegam fragmentados: um currículo em PDF, um banco de itens em planilha, telemetria em um esquema de eventos, metadados de recurso em outro padrão. Cada integração par a par custa um conector. Um grafo oferece um modelo único em que entidades de origens distintas são identificadas de forma estável e ligadas por relações tipadas, de modo que uma consulta atravessa fronteiras de sistema. [I]

Na educação especificamente, a motivação declarada pelos trabalhos consultados é dupla: dar ordem lógica ao conteúdo (relações de pré-requisito, que definem "the logical order in which concepts should be learned" [F: alatrash2025prerequisite, resumo]) e sustentar adaptação e recomendação sobre essa estrutura [F: fettach2022kgeducation, metadados do título e resumo].

## Fundamentos e funcionamento

### Modelos de grafo

Hogan et al. descrevem três construções básicas [F: hogan2021knowledgegraphs, §2.1]:

- **Grafo dirigido com arestas rotuladas** (*directed edge-labelled graph*, também chamado *multi-relational graph*): conjunto de nós e arestas rotuladas entre eles. O modelo padronizado correspondente é RDF [F: hogan2021knowledgegraphs, §2.1.1].
- **Grafo de propriedades** (*property graph*): permite associar um rótulo e um conjunto de pares propriedade-valor tanto a nós quanto a arestas [F: hogan2021knowledgegraphs, §2.1.3]. É o modelo de bancos como o Neo4j, cuja documentação descreve nós com zero ou mais rótulos, relações com direção única e exatamente um tipo, e propriedades chave-valor em ambos [F: neo4j2026graphconcepts].
- **Graph dataset**: um conjunto de grafos nomeados mais um grafo padrão, útil para gerir várias fontes, atualizar uma sem tocar nas outras e distinguir fontes confiáveis das demais [F: hogan2021knowledgegraphs, §2.1.4]. Em RDF isso é o *RDF dataset* [F: w3c2014rdf11concepts, §4].

Os dois primeiros modelos são intertraduzíveis: "property graphs can be translated to/from directed edge-labelled graphs without loss of information"; grafos dirigidos rotulados são o modelo mais minimal, grafos de propriedades o mais flexível, e a escolha "will be secondary to other practical factors" [F: hogan2021knowledgegraphs, §2.1.3]. Ver kg.found.rdf-vs-property-graphs.

### Camadas

[I] Um grafo de conhecimento operacional se organiza em camadas que convém não confundir:

1. **Vocabulário/ontologia**: as classes, propriedades e restrições (kg.found.ontologies, kg.std.owl2, kg.std.skos).
2. **Dados**: as instâncias e suas relações.
3. **Contexto**: validade temporal, proveniência, confiança (kg.found.context-and-reification, kg.std.prov-o).
4. **Derivação**: o que é inferido e não afirmado (kg.found.reasoning).

Essa separação importa porque cada camada tem ritmo de mudança, dono e critério de qualidade diferentes. Ver kg.mod.layer-separation para a aplicação dela ao caso educacional.

## Requisitos e pressupostos

- Identificadores estáveis para as entidades. Sem isso, não há como integrar fontes nem versionar (ver kg.found.identifiers-and-triples).
- Decisão explícita sobre hipótese de mundo. Sob a *closed world assumption*, o que não está no grafo é falso; sob a *open world assumption*, o que não está no grafo simplesmente não é afirmado, e não se pode concluir sua negação [F: hogan2021knowledgegraphs, §4.1, apêndice B]. RDF e OWL adotam mundo aberto; bancos relacionais, mundo fechado. [I] Isso muda o significado de "o aluno não domina X": ausência de evidência não é evidência de ausência.
- Um modelo de esquema, ainda que mínimo. Sem esquema o grafo degenera em pares nome-valor sem semântica compartilhada. [I]

## Vantagens e limitações

Vantagens: integra fontes heterogêneas sob um modelo único; relações são dados de primeira classe, consultáveis e extensíveis sem migração de esquema; permite inferência sobre a estrutura; admite publicação e reuso (ver kg.eng.quality e o princípio FAIR em [F: wilkinson2016fair, metadados]).

Limitações: o custo de modelagem é antecipado e alto; a qualidade depende de curadoria contínua, e Hogan et al. observam que dados extraídos para um grafo inicial "will usually be incomplete, and will contain duplicate, contradictory or even incorrect statements" [F: hogan2021knowledgegraphs, §7]; raciocínio expressivo é caro ou indecidível (ver kg.std.owl2); e representar contexto (tempo, confiança) infla o grafo (ver kg.found.context-and-reification).

## Alternativas e comparações

| Abordagem | Esquema | Relações | Integração de fontes | Inferência |
|---|---|---|---|---|
| Relacional normalizado | fixo, migrações custosas | tabelas de junção | por ETL par a par | só por consulta |
| Documento (JSON) | implícito | aninhamento | por convenção | nenhuma |
| Grafo de propriedades | flexível, sem semântica formal | primeira classe, com atributos | por chave compartilhada | por consulta de caminho |
| RDF + ontologia | explícito e publicável | primeira classe | por IRI global | dedutiva, formalizada |

[I] A tabela sintetiza as propriedades documentadas em [F: hogan2021knowledgegraphs, §2] e [F: neo4j2026graphconcepts]; não há fonte única que a apresente nesta forma.

## Métricas e métodos de avaliação

Hogan et al. tratam qualidade como *fitness for purpose* e organizam dimensões em acurácia (sintática, semântica, atualidade), cobertura (completude, representatividade) e outras [F: hogan2021knowledgegraphs, §7.1-7.2]. Ver kg.eng.quality, que detalha essas dimensões e as métricas associadas.

## Exemplo técnico independente de domínio

Mesma informação em três modelos, sem comprometer com produto nem com currículo específico:

```
# grafo dirigido com arestas rotuladas (estilo RDF, Turtle abreviado)
:conceito-A  :preRequisitoDe  :conceito-B .
:conceito-A  rdf:type         :Conceito .

# grafo de propriedades (estilo Cypher)
(:Conceito {id:'A'})-[:PRE_REQUISITO_DE {forca:0.8, fonte:'curadoria'}]->(:Conceito {id:'B'})

# grafo dirigido + contexto por nó intermediário (reificação direta)
:rel-1  rdf:type        :RelacaoPreRequisito ;
        :origem         :conceito-A ;
        :destino        :conceito-B ;
        :forca          0.8 ;
        :proveniencia   :curadoria-2026 .
```

[I] Os três representam a mesma afirmação. O segundo e o terceiro conseguem anotar a aresta; o primeiro, não, sem recorrer a reificação ou a grafos nomeados (ver kg.found.context-and-reification).

## Relações com outros conceitos

Depende de kg.found.identifiers-and-triples (identidade e unidade mínima de afirmação). Complementa kg.found.ontologies (a camada de esquema) e kg.found.context-and-reification (a camada de contexto). Especificado por kg.std.rdf quando o modelo escolhido é RDF. Relaciona-se com kg.found.rdf-vs-property-graphs (escolha de modelo), kg.found.reasoning (o que se deriva) e kg.mod.conceptual-model (o recorte educacional).

## Lacunas e questões abertas

- O survey de Fettach et al. sobre grafos de conhecimento em educação e empregabilidade não pôde ser aberto nesta sessão; só os metadados foram verificados [F: fettach2022kgeducation]. Falta uma revisão sistemática recente lida integralmente.
- Não há definição normativa de "grafo de conhecimento educacional"; o termo é usado operacionalmente na literatura consultada. [H] Uma definição útil separaria grafo curricular, modelo do aluno e dados observados (ver kg.mod.layer-separation), mas isso é proposta deste domínio, não consenso da área.
- O ponto de equilíbrio entre curadoria manual e extração automática não está estabelecido; ver kg.eng.construction.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| neo4j2026graphconcepts | fornecedor | 2026-10-29 |
| fettach2022kgeducation | academico | 2026-10-29 |
| zhao2022edukg | academico | 2026-10-29 |
