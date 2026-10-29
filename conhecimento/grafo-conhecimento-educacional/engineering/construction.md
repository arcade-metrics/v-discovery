---
id: kg.eng.construction
titulo: Construção e povoamento do grafo
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ain2025topdown, zhao2022edukg, alatrash2025prerequisite, edge2024graphrag, hogan2021knowledgegraphs, w3c2013provo, w3c2017shacl]
relacoes:
  - { tipo: complementa, alvo: kg.eng.methodologies }
  - { tipo: depende-de, alvo: kg.std.prov-o }
  - { tipo: avaliado-por, alvo: kg.eng.quality }
  - { tipo: relacionado-a, alvo: kg.curr.prerequisites }
  - { tipo: relacionado-a, alvo: kg.ret.graph-rag }
  - { tipo: relacionado-a, alvo: kg.curr.bncc }
termos: [construção de grafo, top-down, bottom-up, human-in-the-loop, extração de conceitos, entity linking, sustentabilidade, Simple Random Sampling, validação por especialista, curadoria]
---

# Construção e povoamento do grafo

## Definição e terminologia

Construção é o conjunto de atividades que leva de fontes (documentos curriculares, materiais, bancos de itens) a um grafo povoado. Distingue-se da modelagem (kg.eng.methodologies): ali se define o esquema; aqui se produzem as instâncias e as arestas.

Duas estratégias nomeadas pela literatura consultada [F: ain2025topdown]:

- **Top-down**: partir de uma estrutura de conhecimento existente e mapear o material nela.
- **Bottom-up**: extrair conceitos do material e organizá-los depois.

## Problema que resolve

Hogan et al. colocam o ponto de partida sem rodeios: independentemente das fontes, "data extracted for the initial knowledge graph will usually be incomplete, and will contain duplicate, contradictory or even incorrect statements — especially when taken from multiple sources" [F: hogan2021knowledgegraphs, §7].

[I] Portanto a pergunta não é como construir um grafo correto, mas como construir um grafo cuja incorreção seja conhecida, medida e reduzível.

No caso específico dos pré-requisitos, Alatrash et al. registram que a anotação manual é "time-consuming and inconsistent" [F: alatrash2025prerequisite, resumo]. [I] "Inconsistent" é a palavra importante: curadoria humana em escala não é só cara, é variável.

## Fundamentos e funcionamento

### Top-down versus bottom-up: o que a evidência diz

Ain et al. compararam as duas abordagens na plataforma de MOOCs CourseMapper. O resumo afirma que os resultados "indicate that the Bottom-up approach outperforms the Top-down approach in accurately identifying and mapping key knowledge concepts" [F: ain2025topdown, resumo]. **Os números do artigo mostram diferença mínima e estatisticamente não significativa** [F: ain2025topdown, §5, tabela 1]:

| Pipeline | P@15 (estudo com usuários) | MRR | MAP | Acurácia SRS (média ± margem) |
|---|---|---|---|---|
| Top-down | 0,807 | 0,941 | 0,807 | 0,38 ± 0,048 |
| Bottom-up | 0,812 | 0,941 | 0,812 | 0,40 ± 0,049 |

Os autores registram: "The results (Table 1) showed similar performance between both models. However, the bottom-up approach showed slightly better precision at higher k-values and MAP... **A T-test revealed no significant differences between the models.** In terms of user experience, the bottom-up EduKG was rated more favorably by the participants" [F: ain2025topdown, §5.1]. Na avaliação de acurácia por amostragem aleatória simples, de novo: "a T-test found no statistically significant difference" [F: ain2025topdown, §5.2].

Escala do estudo: 19 participantes (de 47 convidados), de três cursos, avaliando 34 materiais de aprendizagem, com os 15 conceitos principais de cada grafo; na validação por amostragem, dois anotadores revisaram cerca de 180 a 200 amostras por modelo, em 4 horas [F: ain2025topdown, §5.1, §5.2].

[I] Três leituras, e convém manter as três:

1. **A diferença entre as abordagens não está demonstrada.** O que o estudo mostra é que as duas têm desempenho semelhante, com leve preferência subjetiva dos participantes pela bottom-up.
2. **A acurácia absoluta é o achado relevante**: cerca de 0,38 a 0,40 na validação por amostragem. Dois em cada cinco triplos extraídos são considerados corretos pelos anotadores. É esse número, e não a comparação entre pipelines, que justifica o passo seguinte.
3. **O humano no circuito não é opcional** nesse desenho — é a resposta dos próprios autores ao número acima: "to further enhance EduKG accuracy, we integrate a Human-in-the-Loop approach, allowing course moderators to review and refine the EduKG before publication" [F: ain2025topdown, resumo].

Compare-se com o EDUKG, que faz o contrário: define 635 classes e 1.759 propriedades "without subject boundaries" e, guiado por essa ontologia, propõe "a semi-automated method for interactively acquiring knowledge from textbooks" [F: zhao2022edukg, §1]. As palavras "semi-automated" e "interactively" apontam na mesma direção do humano no circuito.

A escala publicada do EDUKG: "more than 252 million entities and 3.86 billion triplets" [F: zhao2022edukg, resumo]. Para contraste, os autores observam que grafos educacionais construídos sobre cursos abertos têm ontologia rasa — MOOC-KG e HEKG definem 4 e 6 classes, respectivamente [F: zhao2022edukg, §1].

[I] A distância entre 4 classes e 635 não é questão de capricho: é a diferença entre modelar a estrutura de um curso e modelar o conteúdo das disciplinas. Ver kg.mod.conceptual-model.

### Sustentabilidade

O EDUKG estabelece "a general mechanism based on our proposed generalized entity linking system for EDUKG's sustainable maintenance", para "index heterogeneous online data incrementally" conforme os recursos crescem [F: zhao2022edukg, resumo e §1]. [I] O problema que isso endereça é real: um grafo construído uma vez e nunca mais atualizado perde valor rapidamente — é a dimensão de *timeliness* de kg.eng.quality.

### Inferência de relações

Para pré-requisitos, Alatrash et al. propõem método não supervisionado que combina dez critérios — baseados em documento, em hyperlinks da Wikipédia, em grafo e em texto — por um algoritmo de votação, reportando maior precisão que métodos existentes com escalabilidade e adaptabilidade [F: alatrash2025prerequisite, resumo]. Ver kg.curr.prerequisites.

### Extração por modelo de linguagem

O pipeline do GraphRAG usa um LLM para derivar um grafo de entidades a partir dos documentos fonte, com chunking de tamanho pré-especificado que "ensures relevant information is distributed across chunks, rather than concentrated (and potentially lost) in a single context window" [F: edge2024graphrag, resumo e §2]. Os índices resultantes nos experimentos: 8.564 nós e 20.691 arestas para um corpus de 1 milhão de tokens; 15.754 nós e 19.520 arestas para 1,7 milhão [F: edge2024graphrag, §5.1].

[I] Essas razões — algo entre 5 e 15 nós por mil tokens de fonte — dão ordem de grandeza útil para dimensionar um projeto, ainda que os corpora não sejam educacionais.

### O arranjo recomendado

[I] Síntese deste documento, apoiada no que as fontes reportam:

| Camada do grafo | Origem | Revisão |
|---|---|---|
| Estrutura curricular (frameworks, habilidades) | extração do documento oficial, top-down | validação determinística: contagens, códigos únicos, aciclicidade |
| Conceitos a partir de materiais | extração bottom-up [F: ain2025topdown] | humano no circuito [F: ain2025topdown] |
| Alinhamento material → currículo | sugestão automática | revisão humana por amostragem |
| Pré-requisitos | inferência multicritério [F: alatrash2025prerequisite] + curadoria | revisão humana antes de uso em diagnóstico |
| Evidências e estado de domínio | cálculo sobre observações | não aplicável; é derivado (kg.mod.evidence-and-mastery) |

Três regras que atravessam todas as linhas:

1. **Cada origem em seu grafo nomeado**, com proveniência PROV-O [F: w3c2013provo]. Curado e extraído nunca se misturam.
2. **Confiança explícita** em tudo que não foi revisado por humano.
3. **Validação SHACL** antes de publicar qualquer lote [F: w3c2017shacl].

## Requisitos e pressupostos

- Esquema definido antes do povoamento, pelo menos em versão inicial (kg.eng.methodologies).
- Capacidade de revisão humana proporcional ao volume extraído; sem ela, o humano no circuito é figura de retórica. [I]
- Proveniência registrada no momento da escrita, não reconstruída depois.
- Um procedimento de amostragem para validação, como a amostragem aleatória simples usada por Ain et al. [F: ain2025topdown].

## Vantagens e limitações

Vantagens da construção assistida: cobre volume que curadoria manual não cobre; a extração é reproduzível, enquanto a anotação manual é "inconsistent" [F: alatrash2025prerequisite]; e a separação por origem permite usar só o curado quando a decisão é crítica.

Limitações: a qualidade depende do extrator e não é uniforme; a revisão humana é o gargalo e o custo real; extração de documento oficial (PDF, planilha) é frágil a mudanças de formatação (ver kg.curr.bncc); e grafos extraídos por LLM podem contradizer o grafo curado sem que ninguém perceba. [I]

## Métricas e métodos de avaliação

[I] Por etapa:

| Etapa | Métrica |
|---|---|
| Extração da estrutura curricular | contagens conferidas contra o documento; unicidade de código; zero ciclos |
| Extração de conceitos | precisão por validação de especialista em amostra aleatória simples; referência observada: acurácia de 0,38 a 0,40 [F: ain2025topdown, tabela 1] |
| Inferência de pré-requisitos | precisão contra conjunto de referência [F: alatrash2025prerequisite] |
| Revisão humana | taxa de aceitação das sugestões; concordância entre revisores |
| Grafo publicado | relatório SHACL sem violações [F: w3c2017shacl]; dimensões de kg.eng.quality |

## Exemplo técnico independente de domínio

```
# pipeline, com separação de origem preservada do início ao fim

documento oficial ──[extração determinística]──> g/fw/oficial/<versão>
                                                    │ validação SHACL
                                                    ▼
materiais ──[extração por LLM, bottom-up]──> g/extraido/<lote>
                                                    │ amostragem + revisão humana
                                                    ▼
                                             g/curado/<lote>
                                                    │
multicritério ──[inferência]──> g/pre-requisitos/inferido/<lote>
                                                    │ revisão antes de uso em diagnóstico
                                                    ▼
                                    g/pre-requisitos/curado/<lote>

# consulta de produção decide que grafos incluir conforme a criticidade da decisão
```

```sparql
# auditoria: arestas em uso que nunca passaram por revisão humana
SELECT ?g (COUNT(*) AS ?n) WHERE {
  GRAPH ?g { ?s ?p ?o }
  ?g prov:wasAttributedTo ?agente .
  ?agente a prov:SoftwareAgent .
  FILTER NOT EXISTS { ?g v:revisadoPor ?humano }
} GROUP BY ?g
```

## Relações com outros conceitos

Complementa kg.eng.methodologies (esquema antes de povoamento). Depende de kg.std.prov-o. Avaliado por kg.eng.quality. Relaciona-se com kg.curr.prerequisites (inferência), kg.ret.graph-rag (o pipeline de indexação é construção) e kg.curr.bncc (extração do documento oficial).

## Lacunas e questões abertas

- **Discrepância registrada**: o resumo de Ain et al. afirma que bottom-up supera top-down, mas os testes t do próprio artigo não encontram diferença significativa em nenhuma das duas avaliações [F: ain2025topdown, §5.1, §5.2]. Este documento reporta os números, não o resumo.
- O estudo de Ain et al. tem 19 participantes e uma plataforma; os números não devem ser generalizados.
- A acurácia de 0,38 a 0,40 refere-se a triplos do tipo (slide, contains, conceito) em material de MOOC [F: ain2025topdown, §5.2]; não há medição equivalente para extração de estrutura curricular a partir de documento oficial.
- Não há, nas fontes consultadas, medição do custo de revisão humana por aresta nem do ponto em que ela deixa de compensar. Ain et al. registram 4 horas para dois anotadores revisarem cerca de 380 amostras [F: ain2025topdown, §5.2], o que dá ordem de grandeza, mas para uma tarefa de julgamento binário, não de correção.
- As razões nó/token do GraphRAG [F: edge2024graphrag, §5.1] vêm de corpora não educacionais.
- [H] Para a estrutura curricular, top-down é obrigatório (o currículo oficial é dado); o resultado de Ain et al. aplica-se à camada de conceitos extraídos de material, não à estrutura. Essa separação é interpretação deste documento, não afirmação dos autores.
- Como detectar contradição entre grafo extraído e grafo curado é problema aberto; nenhuma fonte consultada o trata.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ain2025topdown | academico | 2026-10-29 |
| zhao2022edukg | academico | 2026-10-29 |
| alatrash2025prerequisite | academico | 2026-10-29 |
| edge2024graphrag | academico | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
