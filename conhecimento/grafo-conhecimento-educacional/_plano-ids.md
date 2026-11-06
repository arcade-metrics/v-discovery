---
id: kg.plano-ids
titulo: Plano de identificadores do domínio
tipo: mapa
dominio: grafo-conhecimento-educacional
status: revisado
criado: 2026-10-29
atualizado: 2026-10-29
---

# Plano de identificadores do domínio grafo-conhecimento-educacional

Lista de ids do domínio. Relações entre documentos usam estes ids. Todos os ids abaixo existem em disco (verificado em 2026-10-29 por `_modelo/validar.py`, que reportou 40 documentos, 40 ids únicos e zero erros).

| Pasta | Id | Arquivo |
|---|---|---|
| foundations | kg.found.knowledge-graphs | foundations/knowledge-graphs.md |
| foundations | kg.found.identifiers-and-triples | foundations/identifiers-and-triples.md |
| foundations | kg.found.ontologies | foundations/ontologies.md |
| foundations | kg.found.reasoning | foundations/reasoning.md |
| foundations | kg.found.context-and-reification | foundations/context-and-reification.md |
| foundations | kg.found.rdf-vs-property-graphs | foundations/rdf-vs-property-graphs.md |
| standards | kg.std.index | standards/index.md |
| standards | kg.std.rdf | standards/rdf.md |
| standards | kg.std.rdfs | standards/rdfs.md |
| standards | kg.std.owl2 | standards/owl2.md |
| standards | kg.std.skos | standards/skos.md |
| standards | kg.std.sparql | standards/sparql.md |
| standards | kg.std.shacl | standards/shacl.md |
| standards | kg.std.json-ld | standards/json-ld.md |
| standards | kg.std.prov-o | standards/prov-o.md |
| standards | kg.std.comparison | standards/comparison.md |
| vocabularies | kg.voc.comparison | vocabularies/comparison.md |
| modeling | kg.mod.conceptual-model | modeling/conceptual-model.md |
| modeling | kg.mod.layer-separation | modeling/layer-separation.md |
| modeling | kg.mod.competencies-and-objectives | modeling/competencies-and-objectives.md |
| modeling | kg.mod.evidence-and-mastery | modeling/evidence-and-mastery.md |
| curriculum | kg.curr.competency-frameworks | curriculum/competency-frameworks.md |
| curriculum | kg.curr.bncc | curriculum/bncc.md |
| curriculum | kg.curr.prerequisites | curriculum/prerequisites.md |
| curriculum | kg.curr.cognitive-taxonomies | curriculum/cognitive-taxonomies.md |
| retrieval | kg.ret.graph-rag | retrieval/graph-rag.md |
| retrieval | kg.ret.graph-embeddings | retrieval/graph-embeddings.md |
| retrieval | kg.ret.text-to-query | retrieval/text-to-query.md |
| engineering | kg.eng.methodologies | engineering/methodologies.md |
| engineering | kg.eng.construction | engineering/construction.md |
| engineering | kg.eng.quality | engineering/quality.md |
| engineering | kg.eng.versioning-and-provenance | engineering/versioning-and-provenance.md |
| engineering | kg.eng.storage-and-query | engineering/storage-and-query.md |
| raiz | kg.brief | 00-brief.md |
| raiz | kg.index | README.md |
| raiz | kg.glossario | glossario.md |
| raiz | kg.mapa | mapa-conceitos.md |
| raiz | kg.relatorio | relatorio.md |
| raiz | kg.plano-ids | _plano-ids.md |

## Relações para outros domínios

Este domínio referencia ids de `aprendizagem-adaptativa`, cujo escopo é vizinho e complementar. As referências são sempre por id, nunca por caminho de arquivo.

| Id externo | Referenciado por | Natureza |
|---|---|---|
| adp.id.knowledge-components | kg.mod.conceptual-model, kg.mod.competencies-and-objectives, kg.mod.layer-separation, kg.curr.cognitive-taxonomies | a unidade compartilhada pelas duas bases |
| adp.lm.learner-model | kg.mod.layer-separation, kg.mod.evidence-and-mastery | a camada 2 vista do outro lado |
| adp.kt.bayesian-knowledge-tracing | kg.mod.evidence-and-mastery | como a estimativa é produzida |
| adp.adapt.sequencing-policies | kg.curr.prerequisites | o uso das relações de pré-requisito |
| adp.sr.memory-and-forgetting | kg.mod.evidence-and-mastery (em prosa) | decaimento do domínio ao longo do tempo |
| adp.eval.educational-effectiveness | kg.ret.graph-rag, kg.curr.prerequisites (em prosa) | a métrica que importa no fim |

## Candidatos não criados

Registrados aqui para não serem reinventados, com a razão de não terem documento próprio nesta versão:

| Id candidato | Razão |
|---|---|
| kg.std.turtle, kg.std.ntriples | serializações; cobertas de passagem em kg.std.rdf e kg.std.json-ld |
| kg.std.owl-time | a Time Ontology aparece citada em kg.found.context-and-reification, mas a especificação não foi consultada |
| kg.voc.asn, kg.voc.open-badges | não consultados nesta sessão |
| kg.voc.lti, kg.voc.qti, kg.voc.caliper, kg.voc.oneroster | pertencem ao domínio `interoperabilidade` |
| kg.curr.bncc-em | itinerários formativos do Ensino Médio não examinados |
| kg.ret.vector-rag | RAG vetorial é contraste, não assunto deste domínio |
| kg.eng.federation | consulta federada citada em kg.std.sparql; sem fonte própria consultada |
