---
id: kg.std.comparison
titulo: Quando usar cada padrão da pilha
tipo: comparacao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2014rdf11concepts, w3c2014rdfschema, w3c2009skos, w3c2012owl2overview, w3c2012owl2profiles, w3c2017shacl, w3c2013sparql11overview, w3c2020jsonld11, w3c2013provo, noy2001ontology101, w3c2026rdf12concepts, zhao2022edukg]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: relacionado-a, alvo: kg.std.rdf }
  - { tipo: relacionado-a, alvo: kg.std.rdfs }
  - { tipo: relacionado-a, alvo: kg.std.skos }
  - { tipo: relacionado-a, alvo: kg.std.owl2 }
  - { tipo: relacionado-a, alvo: kg.std.shacl }
  - { tipo: relacionado-a, alvo: kg.std.sparql }
  - { tipo: relacionado-a, alvo: kg.found.rdf-vs-property-graphs }
termos: [pilha semântica, camada, expressividade, validação, inferência, serialização, custo de adoção]
---

# Quando usar cada padrão da pilha

## Definição e terminologia

Este documento não introduz conceito novo: organiza em um lugar a decisão de qual camada usar para quê. A lista de documentos por padrão está em kg.std.index.

## Problema que resolve

[I] Os padrões se sobrepõem em aparência e não em função, e a confusão mais cara é tratar OWL como validador. Mundo aberto significa que uma ontologia OWL não reclama de dado faltante — e equipes descobrem isso tarde. A tabela abaixo existe para evitar essa e três ou quatro confusões vizinhas.

## Alternativas e comparações

### Por função

| Função | Padrão | Por quê |
|---|---|---|
| Modelo de dados | RDF 1.1 / 1.2 | triplas, grafos, datasets com grafos nomeados [F: w3c2014rdf11concepts] |
| Esquema leve (classes, propriedades, rótulos) | RDFS | subsunção, domínio, contradomínio [F: w3c2014rdfschema] |
| Hierarquia de conceitos e vocabulário controlado | SKOS | hierárquico e associativo, rótulos, mapeamento entre esquemas [F: w3c2009skos] |
| Restrições lógicas e inferência expressiva | OWL 2 | classes, propriedades, indivíduos, com semântica formal [F: w3c2012owl2overview] |
| Validação de dados | SHACL | validar grafos RDF contra condições [F: w3c2017shacl] |
| Consulta e atualização | SPARQL 1.1 | onze Recommendations: linguagem, protocolo, formatos, federação [F: w3c2013sparql11overview] |
| Serialização para APIs e marcação | JSON-LD 1.1 | serialização JSON para linked data [F: w3c2020jsonld11] |
| Proveniência | PROV-O | entidades, atividades, agentes [F: w3c2013provo] |

### Por custo e maturidade

| Padrão | Status | Data | Custo de adoção [I] |
|---|---|---|---|
| RDF 1.1 | Recommendation | 25/02/2014 | baixo |
| RDF 1.2 | Candidate Recommendation Snapshot | 07/04/2026 | incerto: padrão em curso |
| RDFS | Recommendation | 25/02/2014 | muito baixo |
| SKOS | Recommendation | 18/08/2009 | muito baixo |
| OWL 2 | Recommendation | 11/12/2012 | alto |
| SPARQL 1.1 | Recommendation | 21/03/2013 | médio |
| SHACL | Recommendation | 20/07/2017 | médio |
| JSON-LD 1.1 | Recommendation | 16/07/2020 | baixo |
| PROV-O | Recommendation | 30/04/2013 | baixo (termos de ponto de partida) |

Datas e status conforme as próprias especificações [F: w3c2014rdf11concepts; w3c2026rdf12concepts; w3c2014rdfschema; w3c2009skos; w3c2012owl2overview; w3c2013sparql11overview; w3c2017shacl; w3c2020jsonld11; w3c2013provo].

### SKOS ou OWL para um currículo?

[I] A decisão mais consequente deste domínio. Critérios:

| Se... | então |
|---|---|
| a estrutura é uma hierarquia de itens com códigos e rótulos | SKOS basta |
| é preciso dizer que duas categorias são disjuntas, ou que uma relação é transitiva | OWL |
| é preciso impedir que um item fique sem rótulo ou sem código | SHACL, não OWL |
| é preciso ligar o currículo a um vocabulário externo sem herdar sua lógica | `skos:*Match`, não `owl:sameAs` |
| é preciso inferir "tudo que precede X" | property path em SPARQL ou materialização; OWL só se a transitividade já for declarada |

Recomendação deste domínio: **SKOS para a espinha curricular, propriedade própria para pré-requisito, SHACL para as regras, OWL só onde a consistência formal pagar o custo.** [I] A justificativa está em kg.std.skos (disjunção normativa entre hierárquico e associativo, §8.6.10) e em kg.std.owl2 (tabela de complexidade). Noy e McGuinness lembram que a melhor solução "almost always depends on the application that you have in mind and the extensions that you anticipate" [F: noy2001ontology101, §3] — portanto esta recomendação vale para o perfil de uso descrito em kg.mod.conceptual-model, não universalmente.

### Erros frequentes

[I] Quatro confusões que a tabela acima pretende evitar:

1. **OWL como validador.** `rdfs:range` e restrições OWL não rejeitam dados; inferem tipos. Validação é SHACL.
2. **`owl:sameAs` como mapeamento.** Iguala indivíduos e propaga todas as afirmações. Para alinhar currículos, use `skos:exactMatch` ou `skos:closeMatch`.
3. **`skos:broader` como pré-requisito.** São relações de natureza diferente, e SKOS trata hierárquico e associativo como disjuntos [F: w3c2009skos, §8.6.10].
4. **Materializar fecho transitivo no mesmo grafo dos dados afirmados.** Perde-se a distinção entre afirmado e derivado; use grafo nomeado separado.

## Métricas e métodos de avaliação

[I] Para decidir em um caso concreto, responda antes: quantas competency questions exigem inferência que SPARQL não resolve? Quantos vocabulários externos serão reusados? Há exigência de publicação aberta? Quantas regras de integridade existem? O custo de cada camada segue dessas respostas, não de preferência arquitetural.

## Relações com outros conceitos

Parte de kg.std.index. Relaciona-se com todos os documentos de `standards/` e com kg.found.rdf-vs-property-graphs (a decisão anterior a esta: qual modelo de grafo).

## Lacunas e questões abertas

- A coluna "custo de adoção" é estimativa deste documento, sem base empírica.
- Não foi levantado quantos grafos educacionais publicados usam OWL além de RDFS/SKOS; o EDUKG declara ontologia com 635 classes [F: zhao2022edukg, resumo], mas não foi verificado em que perfil.
- SHACL 1.2 e RDF 1.2 podem mudar o quadro; status não verificado além do que as páginas consultadas registram.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| w3c2026rdf12concepts | normativo | 2026-10-29 |
| w3c2014rdfschema | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
| w3c2012owl2profiles | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
| w3c2013sparql11overview | normativo | 2026-10-29 |
| w3c2020jsonld11 | normativo | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| noy2001ontology101 | academico | 2026-10-29 |
| zhao2022edukg | academico | 2026-10-29 |
