---
id: kg.found.ontologies
titulo: Ontologia
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [noy2001ontology101, hogan2021knowledgegraphs, w3c2012owl2overview, w3c2014rdfschema, w3c2009skos, zhao2022edukg, guarino2009ontoclean]
relacoes:
  - { tipo: complementa, alvo: kg.found.knowledge-graphs }
  - { tipo: especificado-por, alvo: kg.std.owl2 }
  - { tipo: especificado-por, alvo: kg.std.rdfs }
  - { tipo: depende-de, alvo: kg.found.identifiers-and-triples }
  - { tipo: relacionado-a, alvo: kg.found.reasoning }
  - { tipo: relacionado-a, alvo: kg.eng.methodologies }
  - { tipo: alternativa-a, alvo: kg.std.skos }
termos: [ontologia, classe, propriedade, indivíduo, axioma, restrição, taxonomia, vocabulário controlado, competency question, esquema]
---

# Ontologia

## Definição e terminologia

Noy e McGuinness definem ontologias como "explicit formal specifications of the terms in the domain and relations among them", atribuindo a formulação a Gruber (1993), e acrescentam que uma ontologia "defines a common vocabulary for researchers who need to share information in a domain", incluindo "machine-interpretable definitions of basic concepts in the domain and relations among them" [F: noy2001ontology101, §1].

Em OWL 2, uma ontologia fornece "classes, properties, individuals, and data values" e é armazenada como documento da Web semântica; ontologias OWL 2 podem ser usadas junto com informação escrita em RDF e são trocadas primariamente como documentos RDF [F: w3c2012owl2overview, resumo].

Há um gradiente, não uma dicotomia. [I] Da menor para a maior força semântica: lista controlada de termos → taxonomia (hierarquia) → esquema de conceitos SKOS (hierarquia com semântica frouxa, ver kg.std.skos) → vocabulário RDFS (classes, propriedades, domínio e contradomínio) → ontologia OWL (restrições, cardinalidade, disjunção, inferência).

O que não é: uma ontologia não é o grafo de dados (o grafo instancia a ontologia); não é um esquema de banco relacional (não impõe o fechamento de mundo nem valida por padrão — validação é tarefa de SHACL, ver kg.std.shacl); e não é um modelo de domínio de código.

## Problema que resolve

Noy e McGuinness listam cinco motivos para desenvolver uma ontologia: compartilhar entendimento comum da estrutura da informação entre pessoas ou agentes de software; permitir reuso de conhecimento de domínio; tornar explícitas as premissas do domínio; separar conhecimento de domínio de conhecimento operacional; e analisar conhecimento de domínio [F: noy2001ontology101, §1].

[I] Em um grafo educacional, a ontologia é o que impede que "competência", "habilidade", "objetivo" e "descritor" sejam usados de forma intercambiável por equipes diferentes — e, se o forem, torna o conflito visível em vez de silencioso.

## Fundamentos e funcionamento

### Componentes

- **Classes** e hierarquia de classes (subsunção). Em RDFS, `rdfs:Class` e `rdfs:subClassOf` [F: w3c2014rdfschema].
- **Propriedades** com domínio e contradomínio (`rdfs:domain`, `rdfs:range`) [F: w3c2014rdfschema].
- **Indivíduos** (instâncias) e valores de dados [F: w3c2012owl2overview, resumo].
- **Axiomas e restrições**: em OWL 2, cardinalidade, disjunção, equivalência, características de propriedade. Ver kg.std.owl2.

### Regras fundamentais de projeto

Noy e McGuinness enunciam três regras:

1. "There is no one correct way to model a domain — there are always viable alternatives. The best solution almost always depends on the application that you have in mind and the extensions that you anticipate."
2. "Ontology development is necessarily an iterative process."
3. "Concepts in the ontology should be close to objects (physical or logical) and relationships in your domain of interest. These are most likely to be nouns (objects) or verbs (relationships) in sentences that describe your domain."

[F: noy2001ontology101, §3]

A primeira regra tem consequência direta: não existe "a ontologia correta de educação". A escolha entre modelar "competência" como classe ou como conceito SKOS depende do que se vai perguntar ao grafo. [I]

### Competency questions

A forma recomendada de delimitar escopo é esboçar as perguntas que a base de conhecimento deve responder — as *competency questions*, atribuídas por Noy e McGuinness a Gruninger e Fox (1995). Elas "serve as the litmus test later: Does the ontology contain enough information to answer these types of questions?" [F: noy2001ontology101, §3, Step 1]. Ver kg.eng.methodologies.

### Ontologia e grafo

Hogan et al. situam a ontologia como a forma de representar conhecimento quantificado: afirmações simples cabem como arestas; se o grafo pretende acumular afirmações quantificadas ("toda capital é uma cidade"), "a more expressive way to represent knowledge — such as ontologies or rules — is required", e métodos dedutivos podem então derivar e acumular conhecimento adicional [F: hogan2021knowledgegraphs, §1].

### Escala observada em educação

O EDUKG, grafo de K-12, define "635 classes and 1759 properties in EDUKG ontology without subject boundaries" — 445 propriedades de objeto e 1.314 de tipo de dado — e publica mais de 252 milhões de entidades e 3,86 bilhões de triplos [F: zhao2022edukg, resumo e §1].

Para contraste, os mesmos autores observam que grafos educacionais construídos sobre cursos abertos têm ontologia rasa: MOOC-KG e HEKG definem 4 e 6 classes, respectivamente, e "their ontology can only represent subject-specific knowledge at a shallow level" [F: zhao2022edukg, §1].

[I] A faixa de 4 a 635 classes não reflete desacordo metodológico, e sim escopos diferentes: modelar a estrutura de um curso custa poucas classes; modelar o conteúdo das disciplinas custa centenas. A pergunta a responder antes de escolher é qual dos dois o grafo precisa fazer.

## Requisitos e pressupostos

- Uso declarado. Sem as perguntas que a ontologia deve responder, não há critério para decidir entre alternativas de modelagem [F: noy2001ontology101, §3, Step 1].
- Disposição para iterar. O processo de design iterativo "will likely continue through the entire lifecycle of the ontology" [F: noy2001ontology101, §3].
- Consideração de reuso antes de criar. "It is almost always worth considering what someone else has done"; o reuso pode ser requisito quando o sistema precisa interagir com aplicações já comprometidas com vocabulários particulares [F: noy2001ontology101, §3, Step 2]. Ver kg.voc.comparison.

## Vantagens e limitações

Vantagens: semântica explícita e verificável; inferência; interoperabilidade com quem adota os mesmos termos; documentação executável do domínio.

Limitações: custo alto de construção e manutenção; expressividade cobra preço computacional (ver a tabela de complexidade em kg.std.owl2); e uma ontologia mal dimensionada é pior que nenhuma — formaliza um acordo que não existe. [I] Guarino e Welty propõem com OntoClean uma análise formal de decisões ontológicas baseada em noções metapropriedades como rigidez [F: guarino2009ontoclean, metadados verificados via Crossref; texto não consultado]; ver kg.eng.quality.

## Alternativas e comparações

| Opção | Expressividade | Custo | Quando serve |
|---|---|---|---|
| Lista controlada | nenhuma | mínimo | enumerar valores de um campo |
| SKOS | hierarquia frouxa, sem compromisso lógico | baixo | currículos, taxonomias, tesauros |
| RDFS | classes, propriedades, domínio, contradomínio | médio | esquema leve com inferência de tipo |
| OWL 2 EL/QL/RL | restrições com garantias polinomiais | médio-alto | ontologias grandes ou sobre muitos dados |
| OWL 2 DL completo | máxima dentro do decidível | alto | domínios que exigem consistência formal |

[I] Síntese das características documentadas em [F: w3c2014rdfschema], [F: w3c2009skos] e [F: w3c2012owl2overview, §2.4]; a coluna "quando serve" é recomendação deste documento, não afirmação das fontes.

## Exemplo técnico independente de domínio

```turtle
# RDFS: esquema mínimo
:Conceito       a rdfs:Class .
:Competencia    a rdfs:Class ; rdfs:subClassOf :Conceito .
:preRequisitoDe a rdf:Property ;
    rdfs:domain :Conceito ; rdfs:range :Conceito .

# OWL 2: acrescenta compromisso lógico
:preRequisitoDe a owl:ObjectProperty , owl:TransitiveProperty ;
    owl:propertyDisjointWith :equivalenteA .
:Competencia owl:disjointWith :Recurso .
```

[I] A segunda forma permite detectar que um grafo em que um conceito é pré-requisito de si mesmo e equivalente a outro viola as declarações — mas só se um raciocinador for executado, e ao custo documentado em kg.std.owl2. Declarar `owl:TransitiveProperty` em pré-requisito é uma decisão de modelagem com efeito colateral: o fecho transitivo passa a ser inferido, o que pode ser desejável para consulta e indesejável para apresentação.

## Relações com outros conceitos

Complementa kg.found.knowledge-graphs (é a camada de esquema). Especificada por kg.std.owl2 e kg.std.rdfs. Alternativa a kg.std.skos quando o compromisso lógico não é necessário. Depende de kg.found.identifiers-and-triples. Relaciona-se com kg.found.reasoning e kg.eng.methodologies.

## Lacunas e questões abertas

- Não foi levantado nesta sessão um inventário avaliado de ontologias educacionais publicadas e mantidas; EDUKG foi consultado só pelo resumo [F: zhao2022edukg].
- OntoClean e NeOn foram verificados apenas por metadados; a aplicabilidade de seus critérios a ontologias educacionais permanece em aberto.
- Como dimensionar o corte entre SKOS e OWL em um grafo curricular é a decisão de maior impacto deste domínio e ainda não tem critério mensurável aqui. Ver kg.std.comparison.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| noy2001ontology101 | academico | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
| w3c2014rdfschema | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| zhao2022edukg | academico | 2026-10-29 |
| guarino2009ontoclean | academico | 2026-10-29 |
