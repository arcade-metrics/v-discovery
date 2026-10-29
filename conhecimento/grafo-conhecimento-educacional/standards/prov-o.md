---
id: kg.std.prov-o
titulo: PROV-O
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2013provo, hogan2021knowledgegraphs, w3c2012owl2overview, wilkinson2016fair, w3c2024dcat3]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.std.owl2 }
  - { tipo: complementa, alvo: kg.found.context-and-reification }
  - { tipo: complementa, alvo: kg.eng.versioning-and-provenance }
  - { tipo: relacionado-a, alvo: kg.mod.evidence-and-mastery }
termos: [PROV-O, PROV Data Model, prov:Entity, prov:Activity, prov:Agent, prov:wasGeneratedBy, prov:wasDerivedFrom, prov:wasAttributedTo, prov:used, prov:wasInformedBy, prov:startedAtTime, prov:actedOnBehalfOf, Starting Point Terms, Expanded Terms, Qualified Terms, proveniência]
---

# PROV-O

## Definição e terminologia

"The PROV Ontology (PROV-O) expresses the PROV Data Model using the OWL2 Web Ontology Language (OWL2). It provides a set of classes, properties, and restrictions that can be used to represent and interchange provenance information generated in different systems and under different contexts. It can also be specialized to create new classes and properties to model provenance information for different applications and domains" [F: w3c2013provo, resumo].

Hogan et al. descrevem o PROV Data Model como a especificação de como proveniência pode ser descrita em grafos RDF, em que entidades (grafos, nós, documento físico) são derivadas de outras entidades, são geradas ou usadas por atividades (extração, autoria) e são atribuídas a agentes (pessoas, software, organizações) [F: hogan2021knowledgegraphs, §3.3.1].

## Status normativo

W3C Recommendation de 30/04/2013, editada por Timothy Lebo (Rensselaer Polytechnic Institute), Satya Sahoo (Case Western Reserve University) e Deborah McGuinness (Rensselaer Polytechnic Institute) [F: w3c2013provo].

## Fundamentos e funcionamento

### Três níveis de adoção

A ontologia agrupa seus termos em três categorias para dar uma introdução incremental: **Starting Point terms**, **Expanded terms** e termos para **qualificar relacionamentos**. Usuários "may only need to use parts of the entire ontology, depending on their needs and according to how much detail they want to include" [F: w3c2013provo, §2].

Os termos de ponto de partida, cuja familiaridade é recomendada antes de prosseguir [F: w3c2013provo, §2]:

| Termo | Papel |
|---|---|
| `prov:Entity` | coisa cuja proveniência se descreve |
| `prov:Activity` | o que gerou ou usou entidades |
| `prov:Agent` | quem é responsável |
| `prov:wasGeneratedBy` | entidade → atividade que a gerou |
| `prov:wasDerivedFrom` | entidade → entidade de origem |
| `prov:wasAttributedTo` | entidade → agente |
| `prov:startedAtTime` | início de atividade |
| `prov:used` | atividade → entidade usada |
| `prov:wasInformedBy` | atividade → atividade |
| `prov:actedOnBehalfOf` | agente → agente |

[I] Dez termos cobrem quase tudo que um grafo educacional precisa registrar sobre a origem de suas afirmações. O nível "qualificado" existe para quando é preciso descrever a própria relação (quando, por quem, com que papel), e é aí que PROV-O encontra o problema de anotação de aresta tratado em kg.found.context-and-reification.

### Por que importa neste domínio

[I] Três usos diretos:

1. **Curadoria curricular.** Quem afirmou que o conceito A é pré-requisito de B, quando, com base em quê. Sem isso, revisar o grafo é adivinhação.
2. **Extração automática.** Quando arestas vêm de um pipeline de extração (ver kg.eng.construction), a atividade que as gerou e a versão do modelo usado são parte do dado, não do log.
3. **Evidência de aprendizagem.** Uma evidência tem origem (um instrumento, uma sessão), um instante e um responsável. Ver kg.mod.evidence-and-mastery.

A proveniência também é requisito de publicação: os princípios FAIR tratam de gestão e curadoria de dados científicos [F: wilkinson2016fair, metadados verificados via Crossref; texto integral não consultado]. Ver kg.eng.quality.

## Requisitos e pressupostos

- OWL 2 como linguagem subjacente; PROV-O é expressa em OWL 2 [F: w3c2013provo, resumo].
- Decisão sobre granularidade: proveniência por tripla, por lote de curadoria ou por grafo nomeado. [I] Por grafo nomeado costuma ser o único viável em escala (ver kg.found.context-and-reification).
- Disciplina de registro no momento da escrita. Proveniência reconstruída depois é adivinhada.

## Vantagens e limitações

Vantagens: vocabulário padronizado, evita reinventar `criadoPor`/`criadoEm`; especializável para domínios próprios, como a própria especificação prevê [F: w3c2013provo, resumo]; três níveis permitem adoção incremental.

Limitações: a expressão completa (termos qualificados) é verbosa; proveniência por tripla é impraticável em escala sem reificação; e a ontologia não diz nada sobre *confiança* — só sobre origem. [I] Confiança é modelagem própria.

## Alternativas e comparações

| Precisa de | Opção |
|---|---|
| Origem, autoria, derivação de afirmações | PROV-O [F: w3c2013provo] |
| Versão da ontologia | `owl:versionIRI` [F: w3c2012owl2overview] |
| Contexto de validade temporal de uma aresta | reificação, grafo nomeado ou triple term [F: hogan2021knowledgegraphs, §3.3] |
| Metadados de catálogo de dados | DCAT 3 [F: w3c2024dcat3] |

## Exemplo técnico independente de domínio

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix ex:   <https://example.org/> .

# 1. proveniência por grafo nomeado: um lote de curadoria
ex:g/curadoria-2026-10 a prov:Entity ;
    prov:wasGeneratedBy  ex:atividade/revisao-curricular-2026-10 ;
    prov:wasAttributedTo ex:agente/equipe-curriculo .

ex:atividade/revisao-curricular-2026-10 a prov:Activity ;
    prov:startedAtTime "2026-10-01T00:00:00Z"^^xsd:dateTime ;
    prov:used          ex:fonte/documento-curricular-v3 .

ex:agente/equipe-curriculo a prov:Agent , prov:Organization .

# 2. derivação: a versão nova do grafo deriva da anterior
ex:g/curadoria-2026-10 prov:wasDerivedFrom ex:g/curadoria-2026-04 .

# 3. extração automática: o agente é software
ex:g/extraido-2026-10 a prov:Entity ;
    prov:wasGeneratedBy  ex:atividade/extracao-de-conceitos ;
    prov:wasAttributedTo ex:agente/pipeline-extracao .
ex:agente/pipeline-extracao a prov:Agent , prov:SoftwareAgent .
```

[I] Separar o grafo curado do grafo extraído em grafos nomeados distintos resolve ao mesmo tempo proveniência, confiança e política de atualização: consultas podem incluir só o curado, ou ambos com peso diferente.

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.std.owl2. Complementa kg.found.context-and-reification (PROV-O diz *o que* registrar; a reificação diz *onde pendurar*) e kg.eng.versioning-and-provenance. Relaciona-se com kg.mod.evidence-and-mastery.

## Lacunas e questões abertas

- Os documentos companheiros (PROV-DM, PROV-CONSTRAINTS, PROV-AQ) não foram consultados; só PROV-O.
- A errata do PROV-O "may include some normative corrections" [F: w3c2013provo] e não foi consultada.
- Não há, nas fontes consultadas, prática estabelecida de granularidade de proveniência em grafos educacionais. [H] Grafo nomeado por lote de curadoria mais `prov:wasDerivedFrom` entre versões parece suficiente, mas não foi verificado contra caso real.
- Como representar confiança (não só origem) de arestas extraídas automaticamente continua aberto; ver kg.eng.construction.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2013provo | normativo | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
| wilkinson2016fair | academico | 2026-10-29 |
| w3c2024dcat3 | normativo | 2026-10-29 |
