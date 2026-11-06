---
id: kg.index
titulo: Grafo de conhecimento educacional
tipo: mapa
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Grafo de conhecimento educacional

Base de conhecimento agnóstica sobre representação semântica de conhecimento educacional: ontologias, padrões W3C, vocabulários de competência, modelagem de currículo e recuperação sobre grafo. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo e fontes prioritárias em [`00-brief.md`](00-brief.md).

## Como navegar

Comece pelo [mapa de conceitos](mapa-conceitos.md), que mostra as quatro decisões em cadeia que organizam o domínio, e pelo [glossário](glossario.md). O [relatório](relatorio.md) registra cobertura, lacunas e próximos passos desta versão.

Leitura sugerida para quem chega sem contexto:

1. `foundations/knowledge-graphs.md`: o que é um grafo de conhecimento e por que a definição é disputada.
2. `foundations/rdf-vs-property-graphs.md`: a primeira decisão, e por que ela é menos irreversível do que parece.
3. `standards/comparison.md`: que camada da pilha usar para quê, e as quatro confusões que custam caro.
4. `vocabularies/comparison.md`: o que reusar e o que criar; a conclusão é que o que falta criar é pequeno.
5. `modeling/layer-separation.md`: a recomendação central deste domínio — grafo conceitual, modelo do aluno e dados observados são três coisas.
6. `modeling/conceptual-model.md`: o modelo mínimo proposto, com as competency questions que o justificam.
7. `curriculum/prerequisites.md`: a relação que mais valor agrega, e que nenhum padrão define bem.
8. `retrieval/` e `engineering/`: como consultar, construir, medir e versionar.

## Pastas

| Pasta | Conteúdo | Prefixo de id |
|---|---|---|
| `foundations/` | grafos de conhecimento, triplas e identidade, ontologias, inferência, contexto e reificação, RDF versus grafos de propriedades | `kg.found.*` |
| `standards/` | RDF 1.1 e 1.2, RDFS, OWL 2, SKOS, SPARQL 1.1, SHACL, JSON-LD, PROV-O, índice normativo e comparação | `kg.std.*` |
| `vocabularies/` | comparação dos vocabulários (o que reusar e o que criar). IEEE LOM, Dublin Core, schema.org LearningResource, CASE, ESCO e CTDL moram em `interoperabilidade/` (`iop.md.*`, `iop.comp.*`) | `kg.voc.comparison` |
| `modeling/` | separação de camadas, modelo conceitual, competências e objetivos, evidência e estado de domínio | `kg.mod.*` |
| `curriculum/` | frameworks de competência, BNCC, pré-requisitos e progressões, taxonomias cognitivas | `kg.curr.*` |
| `retrieval/` | Graph RAG, embeddings de grafo, tradução de pergunta em consulta | `kg.ret.*` |
| `engineering/` | metodologias, construção e povoamento, qualidade, versionamento e proveniência, armazenamento | `kg.eng.*` |

A lista completa de ids planejados, as referências cruzadas para o domínio `aprendizagem-adaptativa` e os candidatos não criados estão em [`_plano-ids.md`](_plano-ids.md).

## Convenções do domínio

- **Status normativo sempre explícito.** W3C Recommendation, Candidate Recommendation Snapshot, Working Group Note, IEEE Active Standard, 1EdTech Final Release e padrão de facto são coisas diferentes e aparecem nomeadas como tal. O índice está em `standards/index.md`.
- **Separação entre o que a fonte diz e o que este domínio propõe.** Boa parte de `modeling/` é proposta, não descrição de prática estabelecida, e está marcada `[I]`. A recomendação de três camadas, o modelo conceitual mínimo e as métricas de qualidade operacionalizadas são deste domínio, não das fontes.
- **Vocabulários de fornecedor dependem de versão.** schema.org (release 30.1), ESCO (v1.2.1, release v6.0.0) e CASE (v1.1) têm versão e data de consulta registradas; afirmações sobre eles envelhecem.
- **Textos pagos ou inacessíveis são marcados.** IEEE 1484.12.1-2020, ISO/IEC 39075:2024 e vários artigos foram verificados apenas por metadados ou por página de catálogo. Cada documento registra isso em "Lacunas e questões abertas"; nenhum afirma conteúdo que não pôde ser lido.
- **Este domínio define como esta base será convertida em grafo.** O modelo documental em `_modelo/` usa ids estáveis, relações tipadas e frontmatter estruturado precisamente para permitir essa conversão; o mapeamento das relações para `skos:broader` e propriedades próprias está em `_modelo/modelo-documental.md`, §3.

## Relação com os domínios vizinhos

- **`aprendizagem-adaptativa`** trata de como se estima o que um aluno sabe. Este domínio trata de como representar o que há para saber e como registrar a estimativa. A fronteira está em `modeling/layer-separation.md`, e a unidade compartilhada é o knowledge component (`adp.id.knowledge-components`).
- **`interoperabilidade`** trata dos formatos de troca de dados (xAPI, LTI, QTI, OneRoster, Caliper). CASE aparece aqui porque é vocabulário de competência antes de ser protocolo; os demais ficam lá.
- **`dados-pesquisa-e-eventos`** trata da camada de observações: esquemas de evento, telemetria, LGPD. Este domínio para na fronteira: diz que a camada existe e por que deve ficar separada, não como modelá-la.
