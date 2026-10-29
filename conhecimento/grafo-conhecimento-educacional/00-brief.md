---
id: kg.brief
titulo: Brief do domínio grafo de conhecimento educacional
tipo: relatorio
dominio: grafo-conhecimento-educacional
status: revisado
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: grafo de conhecimento educacional

> Primeira versão do domínio concluída em 2026-10-29. Escopo, estrutura e perguntas abertas abaixo foram o ponto de partida; o resultado, a cobertura alcançada e as lacunas remanescentes estão em [`relatorio.md`](relatorio.md). As perguntas abertas desta seção foram respondidas em [`relatorio.md`](relatorio.md#as-seis-questões-fundamentais-do-brief), com as ressalvas registradas lá.

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Representação semântica de conhecimento educacional: competências, currículo, instrumentos, atividades e relações entre eles. Inclui: fundamentos de grafos de conhecimento e ontologias; padrões W3C (RDF, RDFS, OWL, SKOS, SPARQL, SHACL, JSON-LD); vocabulários e ontologias educacionais existentes; representação de currículos e frameworks de competência; recuperação aumentada por grafo (Graph RAG) e combinação com embeddings; qualidade e governança de ontologias.

Este domínio também define como a própria base `conhecimento/` será convertida em grafo. O modelo documental em `_modelo/` deve ser revisado à luz do que for pesquisado aqui.

Fora do escopo: modelos preditivos sobre o grafo (ficam em `aprendizagem-adaptativa`), formatos de troca de dados (ficam em `interoperabilidade`).

## Estrutura sugerida

- `foundations/`: grafos de conhecimento, ontologias, triplas, raciocínio.
- `standards/`: RDF 1.1, RDFS, OWL 2, SKOS, SPARQL 1.1, SHACL, JSON-LD.
- `vocabularies/`: IEEE LOM, Dublin Core, schema.org (LearningResource), CASE, ESCO e similares.
- `curriculum/`: representação de currículos nacionais e frameworks de competência como grafo.
- `retrieval/`: Graph RAG, SPARQL com LLM, embeddings de grafo.
- `engineering/`: metodologias de construção de ontologia, qualidade, versionamento.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. W3C: RDF 1.1, OWL 2, SKOS Reference, SPARQL 1.1, SHACL, JSON-LD 1.1.
2. Hogan et al., 2021, survey "Knowledge Graphs".
3. IEEE 1484.12.1 (LOM); Dublin Core Metadata Initiative; schema.org.
4. 1EdTech CASE (Competencies and Academic Standards Exchange).
5. Edge et al., 2024, Graph RAG (Microsoft Research).
6. Noy e McGuinness, "Ontology Development 101"; metodologias NeOn e similares.
7. Literatura sobre ontologias para educação e currículo; levantar revisões sistemáticas recentes.

## Perguntas abertas

- Que ontologias educacionais existentes cobrem competências e também instrumentos de avaliação?
- Como representar progressão e temporalidade (trajetória) em RDF sem explosão de triplas?
- Quais critérios de qualidade de ontologia são aplicáveis e mensuráveis?
- Como versionar um grafo em produção mantendo identificadores estáveis?
