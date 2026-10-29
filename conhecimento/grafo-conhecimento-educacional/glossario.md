---
id: kg.glossario
titulo: Glossário de grafo de conhecimento educacional
tipo: glossario
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Glossário: grafo de conhecimento educacional

Termos consolidados do domínio. Cada entrada tem definição curta e o id do documento que a aprofunda e cita a fonte. Termos em inglês quando esse é o uso consolidado na literatura. Termos definidos em outro domínio desta base apontam para o id de origem.

## Grafos e modelos de dados

| Termo | Definição | Documento |
|---|---|---|
| grafo de conhecimento | grafo de dados que acumula e transmite conhecimento do mundo real; nós são entidades, arestas são relações | kg.found.knowledge-graphs |
| grafo de dados (data graph) | o grafo que obedece a um modelo de dados baseado em grafo; o substrato do grafo de conhecimento | kg.found.knowledge-graphs |
| EduKG | grafo de conhecimento educacional; termo usado operacionalmente na literatura, sem definição normativa | kg.found.knowledge-graphs |
| grafo dirigido com arestas rotuladas | modelo de nós ligados por arestas rotuladas; o modelo padronizado correspondente é RDF | kg.found.rdf-vs-property-graphs |
| grafo de propriedades | modelo que admite rótulo e pares propriedade-valor em nós e arestas | kg.found.rdf-vs-property-graphs |
| graph dataset | conjunto de grafos nomeados mais um grafo padrão | kg.found.knowledge-graphs, kg.std.rdf |
| schema, identity, context | os três elementos-chave para lidar com a diversidade de grafos montados de muitas fontes | kg.found.knowledge-graphs |

## RDF e identidade

| Termo | Definição | Documento |
|---|---|---|
| tripla | sujeito (IRI ou blank node), predicado (IRI), objeto (IRI, literal ou blank node) | kg.found.identifiers-and-triples, kg.std.rdf |
| grafo RDF | conjunto de triplas RDF | kg.std.rdf |
| RDF dataset | exatamente um grafo padrão sem nome mais zero ou mais grafos nomeados | kg.std.rdf |
| grafo nomeado | par formado por um IRI ou blank node (o graph name) e um grafo RDF | kg.found.identifiers-and-triples |
| IRI | identificador global; único tipo admitido na posição de predicado | kg.found.identifiers-and-triples |
| blank node | nó sem identificador global, local ao documento; não referenciável de fora | kg.found.identifiers-and-triples |
| literal | valor com datatype, opcionalmente com language tag | kg.found.identifiers-and-triples |
| triple term | tripla RDF usada como termo na posição de objeto de outra tripla; novidade de RDF 1.2 | kg.std.rdf, kg.found.context-and-reification |
| reifying triple | tripla cujo predicado é `rdf:reifies` e cujo objeto é um triple term | kg.found.context-and-reification |
| reifier | sujeito de uma reifying triple; é ele, e não o triple term, que aparece nas demais afirmações | kg.found.context-and-reification |
| triple annotation | conjunto de triplas que têm o reifier como sujeito, quando o triple term corresponde a uma tripla asserida | kg.found.context-and-reification |

## Esquema, ontologia e inferência

| Termo | Definição | Documento |
|---|---|---|
| ontologia | especificação formal e explícita dos termos de um domínio e das relações entre eles | kg.found.ontologies |
| competency question | pergunta que a base deve conseguir responder; serve de teste de aceitação da ontologia | kg.eng.methodologies, kg.mod.conceptual-model |
| entailment | relação pela qual um grafo acarreta afirmações não explícitas nele | kg.found.reasoning |
| open world assumption (OWA) | a ausência de uma aresta não permite concluir sua falsidade; vale em RDF, RDFS e OWL | kg.found.reasoning |
| closed world assumption (CWA) | o que não está no grafo é assumido falso | kg.found.reasoning |
| sound / complete | só produz respostas corretas / produz todas as respostas corretas | kg.found.reasoning, kg.std.owl2 |
| materialização | gravar as triplas derivadas em vez de computá-las na consulta | kg.found.reasoning |
| fecho transitivo | todas as relações alcançáveis por encadeamento de uma relação | kg.found.reasoning, kg.curr.prerequisites |
| perfil OWL | subconjunto sintático de OWL 2 que troca expressividade por eficiência de raciocínio | kg.std.owl2 |
| OWL 2 EL / QL / RL | perfis: ontologias grandes em tempo polinomial / consulta conjuntiva em AC0 sobre dados / regras sobre triplas | kg.std.owl2 |
| complexidade de dados / taxonômica / combinada | medidas de complexidade em função das asserções / dos axiomas / de tudo | kg.std.owl2 |

## SKOS e vocabulários controlados

| Termo | Definição | Documento |
|---|---|---|
| skos:Concept | unidade de significado em um vocabulário; não é classe cujos membros se instanciem | kg.std.skos |
| skos:ConceptScheme | o esquema de conceitos; em currículo, o framework | kg.std.skos, kg.curr.competency-frameworks |
| skos:broader / narrower | vínculo hierárquico direto; por convenção, só imediato, e não declarados transitivos | kg.std.skos |
| skos:broaderTransitive | vínculo direto ou indireto; por convenção não usado para asserções, só para inferir o fecho | kg.std.skos |
| skos:related | vínculo associativo; disjunto do hierárquico no modelo de dados SKOS | kg.std.skos |
| skos:prefLabel / altLabel / hiddenLabel | rótulo preferido, alternativo e oculto do mesmo conceito | kg.std.skos |
| skos:notation | código do conceito, distinto de seu identificador | kg.std.skos, kg.curr.bncc |
| propriedades de mapeamento SKOS | `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch`; alinham sem igualar logicamente | kg.curr.competency-frameworks |
| crosswalk | mapeamento entre dois frameworks; afirmação contextual, com autor, data e critério | kg.curr.competency-frameworks |

## Validação, contexto e proveniência

| Termo | Definição | Documento |
|---|---|---|
| shapes graph / data graph | o grafo com as condições / o grafo validado contra elas | kg.std.shacl |
| SHACL-SPARQL | as restrições e componentes baseados em SPARQL, além da linguagem núcleo | kg.std.shacl |
| validation report | resultado da validação, com `sh:conforms` e os resultados individuais; é ele próprio um grafo RDF | kg.std.shacl, kg.eng.quality |
| reificação | mecanismo para fazer afirmações sobre afirmações, ou definir arestas sobre arestas | kg.found.context-and-reification |
| singleton property | forma de reificação em que o identificador da aresta é o próprio rótulo da aresta | kg.found.context-and-reification |
| proveniência | registro de origem, autoria e derivação de uma afirmação | kg.std.prov-o, kg.eng.versioning-and-provenance |
| prov:Entity / Activity / Agent | as três classes de ponto de partida de PROV-O | kg.std.prov-o |
| owl:versionIRI | o IRI que identifica uma versão da ontologia | kg.eng.versioning-and-provenance |

## Entidades educacionais

| Termo | Definição | Documento |
|---|---|---|
| conceito | unidade de conhecimento referenciável por currículo e por recurso | kg.mod.conceptual-model |
| competência | o que se espera que o aluno seja capaz de fazer, mobilizando conceitos | kg.mod.competencies-and-objectives |
| habilidade | competência tal como enunciada por um framework oficial, com código | kg.mod.competencies-and-objectives |
| objetivo de aprendizagem | formulação operacional, com verbo observável e nível cognitivo | kg.mod.competencies-and-objectives |
| knowledge component (KC) | unidade adquirida de função ou estrutura cognitiva, inferível do desempenho em tarefas relacionadas | adp.id.knowledge-components |
| recurso de aprendizagem | obra com orientação explícita para aprendizagem, educação ou aquisição de habilidade | iop.md.lrmi-schema-org |
| learning object | qualquer entidade, digital ou não, usada para aprendizagem, educação ou treinamento | iop.md.ieee-lom |
| instrumento / item | o que avalia / a unidade avaliativa dentro dele | kg.mod.conceptual-model |
| evidência | observação interpretada à luz do grafo conceitual | kg.mod.evidence-and-mastery |
| estado de domínio (mastery) | estimativa, em um instante, de que o aluno domina um conceito; derivada e revisável | kg.mod.evidence-and-mastery |
| observação | fato registrado sobre o que o aluno fez; imutável | kg.mod.evidence-and-mastery |
| learner model | informação persistente que um sistema mantém sobre cada estudante para adaptar decisões | adp.lm.learner-model |
| pré-requisito | relação que define a ordem lógica em que conceitos devem ser aprendidos | kg.curr.prerequisites |
| taxonomia cognitiva | classificação do que se espera que o aluno faça com o conhecimento | kg.curr.cognitive-taxonomies |

## Padrões educacionais

| Termo | Definição | Documento |
|---|---|---|
| LOM | esquema conceitual de metadados de objeto de aprendizagem, em nove categorias | iop.md.ieee-lom |
| DCMI Metadata Terms | especificação corrente de todos os termos de metadados mantidos pela DCMI | iop.md.dublin-core |
| LRMI | classes, propriedades e concept schemes da DCMI para descrição de recursos educacionais | iop.md.dublin-core |
| LearningResource | tipo schema.org para obras com orientação explícita para aprendizagem | iop.md.lrmi-schema-org |
| teaches / assesses / competencyRequired | propriedades schema.org que ligam recurso a competência | iop.md.lrmi-schema-org |
| AlignmentObject | item schema.org que descreve alinhamento entre recurso e nó de framework educacional | iop.md.lrmi-schema-org |
| CASE | padrão 1EdTech para troca de padrões acadêmicos, competências e habilidades | iop.comp.case |
| CFDocument / CFItem / CFAssociation | o framework / o item / a associação tipada, no modelo CASE | iop.comp.case |
| precedes | associação CASE: a origem vem antes do destino em tempo ou ordem | iop.comp.case, kg.curr.prerequisites |
| hasSkillLevel | associação CASE cujo destino define um nível de habilidade, p. ex. nível cognitivo | iop.comp.case, kg.curr.cognitive-taxonomies |
| ESCO | classificação multilíngue europeia de competências, habilidades e ocupações | iop.comp.esco |
| CTDL | família de padrões de facto para descrição de credenciais e competências | iop.comp.ctdl |
| BNCC | documento normativo que define as aprendizagens essenciais da Educação Básica no Brasil | kg.curr.bncc |

## Recuperação e construção

| Termo | Definição | Documento |
|---|---|---|
| Graph RAG | abordagem baseada em grafo para responder perguntas sobre corpus de texto privado | kg.ret.graph-rag |
| query-focused summarization (QFS) | tarefa de sumarizar um corpus em função de uma pergunta; o que RAG convencional não faz | kg.ret.graph-rag |
| community summary | resumo pré-gerado de um grupo de entidades proximamente relacionadas | kg.ret.graph-rag |
| comprehensiveness / diversity / empowerment / directness | os quatro critérios de avaliação de respostas usados por Edge et al. | kg.ret.graph-rag |
| knowledge graph embedding | representação vetorial densa de entidades e relações do grafo | kg.ret.graph-embeddings |
| scoring function | função que pontua uma tripla a partir dos embeddings de seus componentes | kg.ret.graph-embeddings |
| top-down / bottom-up | construir a partir de estrutura existente / extrair conceitos do material e organizar depois | kg.eng.construction |
| human-in-the-loop | revisão humana do grafo extraído antes da publicação | kg.eng.construction |

## Qualidade e operação

| Termo | Definição | Documento |
|---|---|---|
| fitness for purpose | a definição de qualidade adotada: adequação ao uso declarado | kg.eng.quality |
| acurácia sintática | grau em que os dados respeitam as regras gramaticais do domínio e do modelo | kg.eng.quality |
| acurácia semântica | grau em que os valores representam corretamente fenômenos do mundo real | kg.eng.quality |
| timeliness | grau em que o grafo está atualizado em relação ao estado do mundo | kg.eng.quality |
| completude de esquema / propriedade / população / ligação | os quatro aspectos da completude | kg.eng.quality |
| representatividade | grau de viés do grafo como amostra do grafo ideal | kg.eng.quality |
| triplestore | banco que armazena triplas RDF e responde SPARQL | kg.eng.storage-and-query |
| property path | construção SPARQL para percorrer caminhos, inclusive de comprimento arbitrário | kg.std.sparql |
| text-to-query | tradução de pergunta em linguagem natural para consulta estruturada ao grafo | kg.ret.text-to-query |
| GQL | ISO/IEC 39075:2024, linguagem de consulta padronizada para grafos de propriedades | kg.found.rdf-vs-property-graphs |
