---
id: kg.eng.quality
titulo: Qualidade e avaliação do grafo
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, w3c2017shacl, wilkinson2016fair, duqueramos2013oquare, guarino2009ontoclean, w3c2013provo]
relacoes:
  - { tipo: avaliado-por, alvo: kg.std.shacl }
  - { tipo: complementa, alvo: kg.eng.construction }
  - { tipo: complementa, alvo: kg.eng.methodologies }
  - { tipo: depende-de, alvo: kg.std.prov-o }
  - { tipo: relacionado-a, alvo: kg.eng.versioning-and-provenance }
termos: [qualidade, fitness for purpose, acurácia sintática, acurácia semântica, timeliness, completude, representatividade, viés, OQuaRE, OntoClean, FAIR, métrica de qualidade]
---

# Qualidade e avaliação do grafo

## Definição e terminologia

Hogan et al. definem qualidade como **adequação ao propósito**: "By quality, we here refer to fitness for purpose. Quality assessment then helps to ascertain for which purposes a knowledge graph can be reliably used" [F: hogan2021knowledgegraphs, §7].

Distinguem **dimensões de qualidade**, que capturam aspectos qualitativos dos dados, de **métricas de qualidade**, que dão formas de medir aspectos quantitativos dessas dimensões [F: hogan2021knowledgegraphs, §7].

[I] A definição por adequação ao propósito é o que torna a avaliação possível: não há grafo "de boa qualidade" em abstrato, só grafo bom o suficiente para um uso declarado — que é, de novo, as competency questions.

## Fundamentos e funcionamento

### Acurácia

"Accuracy refers to the extent to which entities and relations — encoded by nodes and edges in the graph — correctly represent real-life phenomena", subdividida em três dimensões [F: hogan2021knowledgegraphs, §7.1]:

**Acurácia sintática** é "the degree to which the data are accurate with respect to the grammatical rules defined for the domain and/or data model". O exemplo dado: um valor incompatível com um `rdfs:range` declarado, ou malformado para o datatype. "A corresponding metric for syntactic accuracy is the ratio between the number of incorrect values of a given property and the total number of values for the same property." E: "Such forms of syntactic accuracy can typically be assessed using validation tools" [F: hogan2021knowledgegraphs, §7.1.1] — isto é, SHACL (kg.std.shacl).

**Acurácia semântica** é "the degree to which data values correctly represent real world phenomena, which may be affected by imprecise extraction results, imprecise entailments, vandalism, etc." Avaliá-la "is challenging": uma opção é verificação manual; outra, automática, é checar a relação contra várias fontes; outra ainda é "validate the quality of individual processes used to generate the knowledge graph, based on measures such as precision, possibly with the help of human experts or gold standards" [F: hogan2021knowledgegraphs, §7.1.2].

**Timeliness** é "the degree to which the knowledge graph is currently up-to-date with the real world state"; um grafo "may be semantically accurate now, but may quickly become inaccurate (outdated) if no procedures are in place to keep it up-to-date in a timely manner". Pode ser avaliada "based on how frequently the knowledge graph is updated with respect to underlying sources", com anotações temporais das mudanças e representações contextuais que capturem a validade temporal dos dados [F: hogan2021knowledgegraphs, §7.1.3].

### Cobertura

"Coverage refers to avoiding the omission of domain-relevant elements, which otherwise may yield incomplete query results or entailments, biased models, etc." [F: hogan2021knowledgegraphs, §7.2].

**Completude** é "the degree to which all required information is present in a particular dataset", e compreende quatro aspectos [F: hogan2021knowledgegraphs, §7.2.1]:

| Aspecto | Definição |
|---|---|
| completude de esquema | grau em que classes e propriedades do esquema estão representadas no grafo de dados |
| completude de propriedade | razão de valores faltantes para uma propriedade específica |
| completude de população | percentual de todas as entidades reais de um tipo representadas no conjunto |
| completude de ligação | grau em que as instâncias estão interligadas |

Medir completude diretamente "is non-trivial as it requires knowledge of a hypothetical ideal knowledge graph" com todos os elementos que o grafo deveria idealmente representar. As estratégias concretas envolvem comparação com *gold standards* que forneçam amostras do grafo ideal, ou medir o recall de métodos de extração sobre fontes completas [F: hogan2021knowledgegraphs, §7.2.1].

**Representatividade** "instead of focusing on the ratio of domain-relevant elements that are missing, rather focuses on assessing high-level biases in what is included/excluded from the knowledge graph". Assume que o grafo é incompleto — uma amostra do grafo ideal — e pergunta quão enviesada é essa amostra. "Biases may occur in the data, in the schema, or during reasoning." Exemplos de viés de dados: viés geográfico, que sub-representa entidades de certas partes do mundo; viés linguístico, que sub-representa recursos multilíngues para certas línguas; viés social, que sub-representa pessoas de determinados gêneros ou raças. Vieses de esquema podem resultar de definições de alto nível extraídas de dados enviesados, ou de definições semânticas que não cobrem casos incomuns. "Unrecognised biases may lead to adverse effects" [F: hogan2021knowledgegraphs, §7.2.2].

[I] A representatividade é a dimensão que um grafo educacional não pode ignorar. Se os materiais indexados vêm desproporcionalmente de uma região, de um tipo de escola ou de um conjunto de autores, o grafo herda esse recorte e passa a recomendar dentro dele. O mecanismo é o mesmo que Hogan et al. descrevem para turismo: o viés geográfico leva a promover desproporcionalmente o que já está sobre-representado, "potentially compounding future biases" [F: hogan2021knowledgegraphs, §7.2.2].

Medidas de representatividade "involve comparison of known statistical distributions with those of the knowledge graph" [F: hogan2021knowledgegraphs, §7.2.2].

### Qualidade de ontologia

Dois instrumentos registrados na literatura, ambos verificados apenas por metadados nesta sessão:

- **OntoClean**: análise formal de decisões ontológicas, por Guarino e Welty [F: guarino2009ontoclean, metadados verificados via Crossref; texto integral não consultado].
- **OQuaRE**: framework de qualidade de ontologias, avaliado por Duque-Ramos et al. em *Expert Systems with Applications* 40(7), 2013, pp. 2696-2703 [F: duqueramos2013oquare, metadados verificados via Crossref; texto integral não consultado].

### FAIR

Os princípios FAIR, de Wilkinson et al., são quinze, em quatro grupos [F: wilkinson2016fair]. Os que incidem diretamente sobre um grafo de conhecimento:

| Grupo | Princípio | Texto |
|---|---|---|
| Findable | F1 | "(meta)data are assigned a globally unique and persistent identifier" |
| Findable | F2, F4 | descritos com metadados ricos; registrados ou indexados em recurso pesquisável |
| Accessible | A1, A1.1 | recuperáveis pelo identificador via protocolo padronizado, aberto, gratuito e universalmente implementável |
| Accessible | A2 | "metadata are accessible, even when the data are no longer available" |
| Interoperable | I1 | "(meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation" |
| Interoperable | I2 | "(meta)data use vocabularies that follow FAIR principles" |
| Interoperable | I3 | "(meta)data include qualified references to other (meta)data" |
| Reusable | R1.1, R1.2, R1.3 | licença de uso clara; "detailed provenance"; conformidade a padrões relevantes da comunidade |

[I] A leitura para este domínio é direta, e é notável quanto da arquitetura recomendada aqui cai sob FAIR: F1 é a regra de IRIs estáveis de kg.found.identifiers-and-triples; A1.1 é satisfeito pelo protocolo SPARQL (kg.std.sparql); I1 é satisfeito por RDF e OWL; I2 é a razão para reusar SKOS, Dublin Core e schema.org em vez de inventar (kg.voc.comparison); I3 é o que os crosswalks com `skos:*Match` fazem; e R1.2 é PROV-O (kg.std.prov-o).

São critério de publicação do grafo conceitual — a camada que, segundo kg.mod.layer-separation, é a única publicável.

## Requisitos e pressupostos

- Um uso declarado, sem o qual "fitness for purpose" não é avaliável [F: hogan2021knowledgegraphs, §7].
- Shapes SHACL mantidas junto com o esquema [F: w3c2017shacl].
- Proveniência registrada, sem a qual acurácia semântica não é rastreável [F: w3c2013provo].
- Um *gold standard* ou amostra de referência para estimar completude [F: hogan2021knowledgegraphs, §7.2.1].

## Métricas e métodos de avaliação

[I] Operacionalização das dimensões de Hogan et al. para um grafo educacional:

| Dimensão | Métrica aplicada | Como medir |
|---|---|---|
| Acurácia sintática | razão de valores incorretos por propriedade [F: hogan2021knowledgegraphs, §7.1.1] | relatório SHACL [F: w3c2017shacl] |
| Acurácia semântica | precisão por amostra validada por especialista [F: hogan2021knowledgegraphs, §7.1.2] | amostragem aleatória + revisão |
| Timeliness | frequência de atualização ante a fonte [F: hogan2021knowledgegraphs, §7.1.3] | defasagem entre versão do framework oficial e versão do grafo |
| Completude de esquema | classes e propriedades sem instância | consulta |
| Completude de propriedade | habilidades sem rótulo, sem código, sem objeto de conhecimento | consulta ou SHACL `sh:minCount` |
| Completude de população | habilidades do documento oficial ausentes do grafo | contagem contra o documento |
| Completude de ligação | conceitos sem nenhum recurso nem item | a competency question 4 de kg.mod.conceptual-model |
| Representatividade | distribuição de materiais por origem, de itens por nível cognitivo, de cobertura por componente | comparação com distribuição esperada [F: hogan2021knowledgegraphs, §7.2.2] |

## Exemplo técnico independente de domínio

```sparql
# completude de ligação: conceitos sem nenhum recurso que os ensine
SELECT (COUNT(?c) AS ?semRecurso) WHERE {
  GRAPH ex:g/conceitual/v3 { ?c a skos:Concept }
  FILTER NOT EXISTS { ?r schema:teaches ?c }
}

# representatividade: distribuição de itens por nível cognitivo e componente
SELECT ?componente ?nivel (COUNT(?i) AS ?n) WHERE {
  ?i schema:assesses ?comp .
  ?comp v:nivelCognitivo ?nivel ; v:operacionaliza/skos:broader+ ?componente .
  ?componente a v:ComponenteCurricular .
} GROUP BY ?componente ?nivel

# timeliness: defasagem entre a versão da fonte e a do grafo
SELECT ?g ?fonte ?geradoEm WHERE {
  ?g prov:generatedAtTime ?geradoEm ; v:versaoFonte ?fonte .
} ORDER BY ?geradoEm
```

```turtle
# o relatório SHACL é RDF: guarde-o e consulte a evolução da qualidade
ex:validacao/2026-10-29 a sh:ValidationReport , prov:Entity ;
    sh:conforms false ;
    prov:generatedAtTime "2026-10-29T16:00:00Z"^^xsd:dateTime ;
    prov:used ex:g/conceitual/v3 .
```

[I] Guardar os relatórios SHACL como entidades PROV é o que transforma validação pontual em série temporal de qualidade — e torna possível responder se o grafo está melhorando.

## Relações com outros conceitos

Avaliado por kg.std.shacl. Complementa kg.eng.construction (a qualidade do que entra) e kg.eng.methodologies (os critérios de aceitação). Depende de kg.std.prov-o. Relaciona-se com kg.eng.versioning-and-provenance.

## Lacunas e questões abertas

- OQuaRE e OntoClean foram verificados apenas por metadados; suas dimensões concretas não puderam ser descritas. FAIR foi lido integralmente.
- Hogan et al. tratam outras dimensões de qualidade além de acurácia e cobertura [F: hogan2021knowledgegraphs, §7]; só essas duas foram lidas nesta sessão.
- Não há, nas fontes consultadas, limiares de aceitação para nenhuma dessas métricas em grafos educacionais.
- A dimensão de representatividade aplicada a materiais didáticos não foi tratada por nenhuma fonte consultada; a transposição do exemplo de turismo de Hogan et al. é interpretação deste documento.
- [H] Completude de ligação (conceitos sem recurso nem item) é provavelmente a métrica mais acionável em um grafo curricular novo, porque aponta trabalho concreto; não verificado contra prática.
- Como estimar completude de população sem gold standard, quando o documento oficial é PDF, continua em aberto; ver kg.curr.bncc.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
| wilkinson2016fair | academico | 2026-10-29 |
| duqueramos2013oquare | academico | 2026-10-29 |
| guarino2009ontoclean | academico | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
