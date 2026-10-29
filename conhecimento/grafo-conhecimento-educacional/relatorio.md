---
id: kg.relatorio
titulo: Relatório da primeira versão do domínio grafo de conhecimento educacional
tipo: relatorio
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Relatório: primeira versão do domínio grafo de conhecimento educacional

Data: 2026-10-29. Esta é a "primeira versão funcional" pedida pelo brief: estrutura, mapa conceitual, bibliografia inicial e documentos principais fundamentados em fontes verificadas. Todos os documentos conceituais estão em `status: rascunho`; a passagem para `revisado` exige o checklist de `_modelo/checklist-revisao.md` por leitor humano.

## Método aplicado

Sete frentes, uma por pasta, com a regra de abrir cada fonte antes de citá-la. Uma segunda rodada, posterior à primeira versão deste relatório, recuperou os textos integrais que haviam ficado como resumo ou metadados e preencheu a lacuna de text-to-SPARQL; as correções que isso produziu estão registradas abaixo. As especificações W3C, as páginas de catálogo IEEE e 1EdTech, os portais de ESCO, DCMI, schema.org, BNCC e Credential Engine, e os PDFs de Hogan et al., Noy e McGuinness e Edge et al. foram baixados e lidos nesta sessão. Metadados de artigos não acessíveis foram verificados via API do Crossref e via API do arXiv.

Os fragmentos de bibliografia e índice foram mesclados em `referencias/bibliografia.bib` e `referencias/indice-fontes.md` por `_modelo/mesclar_referencias.py`. O validador `_modelo/validar.py` confirmou, sobre a base inteira: 191 documentos, 191 ids únicos com prefixo correto, todos os alvos de relação existentes, todas as chaves de fonte presentes na bibliografia, nenhuma menção a produto consumidor. **Zero erros e zero avisos.**

## Cobertura

| Área | Documentos | Observação |
|---|---|---|
| foundations | 6 | grafos de conhecimento, triplas e identidade, ontologias, inferência, contexto e reificação, RDF versus grafos de propriedades |
| standards | 10 | RDF 1.1/1.2, RDFS, OWL 2, SKOS, SPARQL 1.1, SHACL, JSON-LD, PROV-O, índice normativo, comparação |
| vocabularies | 7 | IEEE LOM, Dublin Core e LRMI, schema.org LearningResource, CASE, ESCO, CTDL, comparação |
| modeling | 4 | separação de camadas, modelo conceitual, competências e objetivos, evidência e estado de domínio |
| curriculum | 4 | frameworks de competência, BNCC, pré-requisitos, taxonomias cognitivas |
| retrieval | 3 | Graph RAG, embeddings de grafo, tradução de pergunta em consulta |
| engineering | 5 | metodologias, construção, qualidade, versionamento e proveniência, armazenamento |
| raiz | 6 | brief, README, glossário, mapa de conceitos, plano de ids, este relatório |

Totais: **45 documentos, 226 relações tipadas, 385 termos distintos nos frontmatters, 50 fontes na bibliografia** — todas as 50 efetivamente citadas por algum documento.

Fontes por tipo: 23 normativas, 15 acadêmicas, 11 de fornecedor, 1 técnica. A predominância de fontes normativas reflete a natureza do domínio: a pilha W3C e os padrões educacionais são o seu núcleo.

Marcas de afirmação no corpo dos documentos: **674 citações de fato com chave de fonte, 270 interpretações marcadas `[I]`, 24 hipóteses marcadas `[H]`.**

## O que o brief pediu e onde está

| Entregável | Local |
|---|---|
| Estrutura de diretórios | `grafo-conhecimento-educacional/` (7 pastas) |
| Glossário | `glossario.md`, com 9 seções temáticas |
| Mapa conceitual | `mapa-conceitos.md`: visão geral escrita à mão mais seção gerada com todos os documentos e relações |
| Documentação dos padrões | `standards/`, com `index.md` registrando status normativo de 25 especificações |
| Comparações tecnológicas | `standards/comparison.md`, `vocabularies/comparison.md`, `foundations/rdf-vs-property-graphs.md`, `engineering/storage-and-query.md` |
| Bibliografia BibTeX | `conhecimento/referencias/bibliografia.bib` (fragmentos `kg-*.bib`) |
| Índice de referências com URL, tipo e data | `conhecimento/referencias/indice-fontes.md` |
| Exemplos verificáveis de modelagem e consulta | seção "Exemplo técnico" de cada documento: Turtle, TriG, JSON-LD, SPARQL, Cypher e shapes SHACL |
| Recomendação de separar os três elementos | `modeling/layer-separation.md`, retomada em `modeling/conceptual-model.md`, `modeling/evidence-and-mastery.md` e `engineering/storage-and-query.md` |

### As seis questões fundamentais do brief

| Questão | Onde é respondida | Resposta em uma linha |
|---|---|---|
| Como representar formalmente o conhecimento educacional? | kg.mod.conceptual-model, kg.std.comparison | SKOS para a espinha curricular, propriedades próprias para pré-requisito e evidência, SHACL para as regras, OWL só onde a consistência formal pagar o custo |
| Como modelar pré-requisitos e progressões? | kg.curr.prerequisites | propriedade própria, porque nenhum padrão consultado a define bem; afirmar só o vínculo imediato, obter o fecho por consulta; aciclicidade é regra a validar, não propriedade herdada |
| Quando RDF/OWL e quando grafos de propriedades? | kg.found.rdf-vs-property-graphs | RDF quando o grafo publica, reusa vocabulários ou tem esquema como produto; grafo de propriedades quando é interno e quase toda aresta tem atributo; a conversão entre os dois é sem perda |
| Como integrar currículos, ontologias e fontes? | kg.curr.competency-frameworks, kg.voc.comparison | crosswalks com `skos:*Match` (não `owl:sameAs`), em grafos nomeados próprios, com proveniência e versão da fonte externa registradas |
| Como validar consistência e qualidade semântica? | kg.std.shacl, kg.eng.quality | SHACL para forma e acurácia sintática; amostragem com especialista para acurácia semântica; as dimensões de cobertura e representatividade de Hogan et al. operacionalizadas em consultas |
| Como relacionar currículo e modelos individuais? | kg.mod.layer-separation, kg.mod.evidence-and-mastery | três camadas separadas, ligadas pelo IRI do conceito; a estimativa nunca é aresta simples, sempre nó qualificado com instante, incerteza e proveniência |

## Ampliações em relação ao brief

- **`modeling/` não estava previsto** como pasta no brief, que sugeria `foundations/`, `standards/`, `vocabularies/`, `curriculum/`, `retrieval/` e `engineering/`. Foi criada porque a recomendação de separar os três elementos — explícita no pedido — exigia desenvolvimento próprio, e porque as questões de granularidade (conceito, competência, objetivo) não cabiam em `curriculum/`.
- **`foundations/context-and-reification.md`** foi acrescentado por necessidade: a pergunta do brief sobre representar progressão e temporalidade "sem explosão de triplas" é, no fundo, o problema de anotação de aresta, e ele reaparece em pré-requisitos, alinhamentos e evidências.
- **`retrieval/text-to-query.md`** foi acrescentado porque Graph RAG e consulta a grafo curado são coisas diferentes, e confundi-las é erro comum.
- **Referências cruzadas para `aprendizagem-adaptativa`**: seis ids daquele domínio são referenciados daqui, listados em `_plano-ids.md`. A fronteira entre as duas bases é o knowledge component.

## Correções obtidas na segunda rodada de busca

Os artigos do arXiv têm PDF aberto e o FAIR é publicado em acesso livre; na primeira rodada eles haviam ficado em resumo ou metadados. A leitura integral produziu **três correções factuais** que contradizem o que os resumos sugeriam. Registro aqui porque são exatamente o tipo de erro que uma base de conhecimento existe para evitar.

**1. Pré-requisitos: a afirmação do resumo não se sustenta na tabela.** O resumo de Alatrash et al. diz "higher precision than existing methods". A tabela 4 do próprio artigo mostra que a precisão do método proposto supera as linhas de base **apenas em um dos três domínios** (Data Mining, 1,00 contra 0,85 do AdaBoost); em Physics o AdaBoost é melhor (0,87 contra 0,76). E o recall fica entre 0,13 e 0,27, contra 0,49 a 0,90 das linhas de base. `curriculum/prerequisites.md` agora traz a tabela completa e a ressalva.

**2. Construção: a diferença entre top-down e bottom-up não é significativa.** O resumo de Ain et al. diz que bottom-up supera top-down. Os números: P@15 de 0,807 contra 0,812; acurácia por amostragem de 0,38 contra 0,40; e **dois testes t sem diferença estatisticamente significativa**. O achado relevante do estudo não é a comparação, e sim a acurácia absoluta de cerca de 0,40 — que é o que justifica o humano no circuito. `engineering/construction.md` foi reescrito nesse trecho.

**3. Graph RAG em educação: n = 3.** A avaliação de Abdelmagied et al. tem três instrutores e três cursos. É indício de viabilidade, não evidência de eficácia, e `retrieval/graph-rag.md` agora diz isso.

Ganhos de conteúdo na mesma rodada:

- **A lacuna de text-to-SPARQL foi preenchida.** Havia literatura abundante, incluindo um TEXT2SPARQL Challenge em segunda edição no ESWC 2026. `retrieval/text-to-query.md` foi reescrito sobre cinco fontes novas e deixou de ser recomendação sem apoio. O achado central, de Allemang e Sequeda: acurácia de 16,7% em text-to-SQL direto, 54,2% com representação em grafo, 72,55% acrescentando validação determinística da consulta contra a ontologia (OBQC) e reparo por LLM — com 8% de "não sei" e 20% de taxa de erro. A validação da consulta **não usa LLM**: é SPARQL sobre regras de domínio e contradomínio. Isso confirmou, com números, as salvaguardas que o documento antes só recomendava.
- **FAIR foi lido**: os quinze princípios estão agora tabulados em `engineering/quality.md`, com o mapeamento para as decisões deste domínio (F1 são os IRIs estáveis, I2 é o reuso de vocabulário, R1.2 é PROV-O).
- **EDUKG foi lido**: 635 classes, 1.759 propriedades, 252 milhões de entidades, 3,86 bilhões de triplos — contra 4 e 6 classes de MOOC-KG e HEKG. A faixa de escala entrou em `foundations/ontologies.md`.
- **Os dez critérios de Alatrash et al.** estão tabulados em `curriculum/prerequisites.md`, junto com os três pressupostos estruturais que eles declaram (transitividade, assimetria, ausência de autoconexão) — que confirmam a aciclicidade como pressuposto do modelo.

## Fontes que permanecem não verificadas integralmente

| Acesso | Fontes |
|---|---|
| Texto integral | hogan2021knowledgegraphs, noy2001ontology101, edge2024graphrag, wilkinson2016fair, zhao2022edukg, alatrash2025prerequisite, ain2025topdown, abdelmagied2025graphrag, yao2019jointembedding, allemang2024ontologies, meyer2024sparqlcap, diallo2024neuralsparql |
| Só metadados (Crossref) | krathwohl2002revision, liang2015prerequisite, guarino2009ontoclean, suarez2011neon, duqueramos2013oquare, fettach2022kgeducation |
| Só resumo (arXiv) | smeros2026text2sparql, zhang2026saga |

Consequências que permanecem:

- **Krathwohl continua inacessível** (Taylor & Francis, pago), portanto `curriculum/cognitive-taxonomies.md` **ainda não enumera os níveis da taxonomia de Bloom revisada** nem descreve suas duas dimensões. O exemplo técnico usa níveis genéricos por essa razão.
- **OntoClean, NeOn e OQuaRE** (Springer e Elsevier, pagos) aparecem como ponteiros, não como prescrição.
- **O survey de Fettach et al.** continua inacessível: o IEEE Xplore retornou HTTP 418 em duas tentativas, inclusive pela via de acesso aberto do IEEE Access.

Textos pagos ou bloqueados por plataforma:

- **IEEE 1484.12.1-2020 (LOM)**: texto normativo pago. O que consta vem da página pública do catálogo IEEE SA: resumo, status, datas e categorias.
- **ISO/IEC 39075:2024 (GQL)**: a página da ISO retornou HTTP 403. O que consta vem do site do comitê de padronização e do openCypher.
- **BNCC**: o documento em navegação é renderizado por JavaScript; apenas o sumário e a página inicial puderam ser extraídos. O formato do código alfanumérico de habilidade **não foi verificado**, e o exemplo em `curriculum/bncc.md` registra isso.

## O que este domínio propõe e nenhuma fonte afirma

Registro explícito, para que leitores não confundam síntese com evidência. O seguinte é recomendação desta base:

1. **A separação em três camadas** (grafo conceitual, modelo do aluno, dados observados). Apoiada em propriedades documentadas de grafos nomeados e na observação de que a literatura já trabalha com EduKG e PKG distintos, mas não afirmada como prática estabelecida por nenhuma fonte.
2. **O modelo conceitual mínimo** de `modeling/conceptual-model.md`, com suas oito competency questions, não validado contra implementação.
3. **A cadeia de quatro níveis** framework → habilidade → objetivo → conceito, cujas definições são operacionais, não ontológicas.
4. **O mapeamento CASE → SKOS** de `vocabularies/case.md`, que perde `isPartOf` e `exemplar`.
5. **O mapeamento da BNCC para grafo**, em `curriculum/bncc.md`, que é a maior parte daquele documento.
6. **Duas métricas de `retrieval/text-to-query.md`**: taxa de vazio enganoso e taxa de seleção do catálogo. As demais salvaguardas daquele documento deixaram de ser proposta e passaram a ter apoio em [F: allemang2024ontologies].
7. **As métricas operacionalizadas** de `engineering/quality.md`: as dimensões são de Hogan et al., a tradução em consultas educacionais é daqui.

## Próximos passos sugeridos

Em ordem de retorno esperado:

1. **Resultados do TEXT2SPARQL Challenge.** É a fonte mais provável de estado da arte atualizado, e nenhum dos trabalhos do desafio foi lido além de metadados.
2. **Abrir o survey de Fettach et al.** por outra via, e procurar revisões sistemáticas recentes de grafos de conhecimento educacional lidas integralmente.
3. **Ler Krathwohl** e verificar se existe publicação da taxonomia revisada como vocabulário SKOS reutilizável; sem isso, `curriculum/cognitive-taxonomies.md` fica incompleto.
4. **Testar o OBQC sobre um grafo curricular.** O método de Allemang e Sequeda é determinístico, documentado e depende só de `rdfs:domain` e `rdfs:range`; nenhum benchmark educacional existe, e produzir um é trabalho de baixo custo e alto retorno.
5. **Verificar a BNCC**: formato do código de habilidade, contagens por componente, existência de publicação em SKOS, RDF ou CASE por alguma iniciativa.
6. **Abrir o modelo semântico do ESCO** em RDF/XML e registrar o padrão de IRI, as classes e as propriedades; hoje só a descrição da página de download está verificada.
7. **Localizar o modelo de informação de CASE 1.1** (a URL do `/info/` retornou 404) e confirmar se o `CFAssociationTypeEnum` mudou em relação a 1.0.
8. **Prototipar o modelo conceitual** contra um currículo real, executar as oito competency questions e registrar o que não funcionou. É o único modo de sair de "proposta" para "validado".
9. **Benchmarks de armazenamento**: `engineering/storage-and-query.md` não compara desempenho porque nenhum benchmark independente foi consultado.

## Observações sobre a base como um todo

Este domínio tem uma responsabilidade adicional, registrada no brief: definir como a própria base `conhecimento/` será convertida em grafo. O modelo documental de `_modelo/` já antecipa isso com ids estáveis, relações tipadas e frontmatter estruturado, e `_modelo/modelo-documental.md` §3 mapeia as relações para `skos:broader` e propriedades próprias.

[I] Duas observações, à luz do que foi pesquisado:

- O mapeamento previsto está correto no essencial. `parte-de` → `skos:broader` é adequado, e as demais relações como propriedades próprias seguem exatamente a recomendação deste domínio para pré-requisitos: não forçar semântica SKOS onde ela não serve.
- Falta uma peça: o modelo documental não prevê **proveniência nem versão** dos documentos além de `criado`/`atualizado`. Quando a base virar grafo, cada documento será uma entidade com autor e derivação, e `prov:wasDerivedFrom` entre versões seria mais útil que a data de atualização. Isso é sugestão para a revisão de `_modelo/`, não alteração feita aqui.
