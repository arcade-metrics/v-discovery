---
id: kg.ret.text-to-query
titulo: Tradução de pergunta em consulta ao grafo
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [allemang2024ontologies, meyer2024sparqlcap, diallo2024neuralsparql, smeros2026text2sparql, zhang2026saga, w3c2013sparql11query, w3c2013sparql11overview, w3c2009skos, edge2024graphrag, abdelmagied2025graphrag, w3c2017shacl, w3c2012owl2overview]
relacoes:
  - { tipo: depende-de, alvo: kg.std.sparql }
  - { tipo: depende-de, alvo: kg.found.ontologies }
  - { tipo: complementa, alvo: kg.ret.graph-rag }
  - { tipo: complementa, alvo: kg.std.shacl }
  - { tipo: avaliado-por, alvo: kg.eng.quality }
termos: [text-to-SPARQL, text-to-SQL, KGQA, OBQC, LLM repair, aterramento, grounding, alucinação, I don't know, taxa de erro, consulta somente leitura, vocabulário controlado, TEXT2SPARQL Challenge]
---

# Tradução de pergunta em consulta ao grafo

## Definição e terminologia

É a geração, por um modelo de linguagem, de uma consulta estruturada — SPARQL, no caso de grafos RDF — a partir de uma pergunta em linguagem natural, para execução contra um grafo existente. A literatura usa **text-to-SPARQL**, por analogia a text-to-SQL, e **KGQA** (*knowledge graph question answering*) para a tarefa completa de responder perguntas sobre um grafo.

Distingue-se de Graph RAG (kg.ret.graph-rag): ali o grafo é construído do texto e serve de índice; aqui o grafo já existe e o modelo apenas traduz a pergunta. [I] São complementares.

## Problema que resolve

Um grafo curado é preciso e inacessível a quem não escreve consulta. Allemang e Sequeda formulam o objetivo em termos empresariais: usuários querem "ask questions and receive accurate, explainable and governed answers" [F: allemang2024ontologies, §1].

[I] Em educação, as competency questions de kg.mod.conceptual-model são formuladas em linguagem natural por desenho — "o que um aluno precisa saber antes de estudar X" — e precisam voltar a essa forma na interface.

## Fundamentos e funcionamento

### O grafo aumenta a acurácia, com números

A evidência central vem de Allemang e Sequeda, do data.world AI Lab, usando o benchmark *chat with the data* sobre um domínio de seguros [F: allemang2024ontologies]:

| Configuração | Acurácia |
|---|---|
| GPT-4, zero-shot, perguntas diretamente sobre banco SQL (text-to-SQL) | 16,7% [F: allemang2024ontologies, §1] |
| O mesmo, sobre uma representação em grafo de conhecimento do mesmo banco (text-to-SPARQL) | 54,2% [F: allemang2024ontologies, §1] |
| Acrescentando OBQC e LLM Repair | 72,55%, mais 8% de "I don't know"; taxa de erro de 20% [F: allemang2024ontologies, resumo e §1] |

Os autores resumem o primeiro salto: um sistema de QA sobre uma representação em grafo de um banco SQL empresarial "returns 3x more accurate results than a LLM without a Knowledge Graph" [F: allemang2024ontologies, §1].

Em perguntas de baixa complexidade sobre esquemas de baixa complexidade, a taxa de erro cai para 10,46%, "which is now at levels deemed to be acceptable by users" [F: allemang2024ontologies, §1].

### OBQC: validação determinística antes de executar

O **Ontology-based Query Check** verifica se a consulta gerada é válida aplicando regras baseadas na semântica da ontologia. Um conjunto de regras verifica o corpo da consulta (cláusula `WHERE`), outro verifica a cabeça (cláusula `SELECT`). O ponto decisivo: "the Ontology-based Query Check does not use an LLM. It is deterministic and based solely on the semantics of the ontology" [F: allemang2024ontologies, §3.1].

Exemplos de regras documentadas [F: allemang2024ontologies, §3.1]:

| Regra | O que verifica |
|---|---|
| Domain | o sujeito de um predicado é compatível com o domínio declarado |
| Range | o objeto de um predicado é compatível com o contradomínio declarado |
| Double Range | duas triplas com o mesmo objeto não impõem contradomínios conflitantes |
| Double Domain | duas triplas com o mesmo sujeito não impõem domínios conflitantes |
| Domain Range | se o objeto de uma tripla é o sujeito da seguinte, o contradomínio da primeira deve bater com o domínio da segunda |

Exemplo do template de erro gerado: "The property :against has range :PolicyCoverageDetail, but its object ?policy is a :Policy, which isn't a subclass of :PolicyCoverageDetail" [F: allemang2024ontologies, §3.1.2].

Frequência de acionamento das regras nos reparos [F: allemang2024ontologies, §4]:

| Regra | Uso |
|---|---|
| Double Domain | 37,47% |
| Domain Range | 22,78% |
| IRI Output | 18,40% |
| Subject Output | 11,91% |
| Domain | 4,69% |

Regras exclusivamente de domínio foram acionadas 42,16% das vezes; "surprisingly, rules exclusively related to range were invoked less than 1% of the time" [F: allemang2024ontologies, §4]. Regras relativas ao corpo da consulta foram acionadas 70% das vezes, contra 30% das relativas à cabeça [F: allemang2024ontologies, §1].

[I] Isso tem consequência direta de modelagem: declarar `rdfs:domain` nas propriedades do grafo educacional paga por si na validação de consulta, mesmo que a inferência de domínio nunca seja usada (ver kg.std.rdfs).

### LLM Repair e "eu não sei"

Detectado o erro, o prompt de reparo é mínimo: "We have a query {query} with some issues outlined here {issues} / Please re-write it." A nova consulta volta ao OBQC, e o ciclo repete até passar ou atingir o limite — três iterações nos experimentos. Nesse caso "the query generation is said to be unknown; there is no point in sending a query that is known to be faulty to the database" [F: allemang2024ontologies, §3.2].

O reparo não repete a pergunta nem a ontologia ao modelo: "the ontology input was taken into consideration by the OBQC, and the question is reflected in the query so far" [F: allemang2024ontologies, §3.2].

A conclusão que mais importa para um sistema educacional:

> "In contrast to a pure LLM-based system which is prone to hallucinations, when we get the wrong answer, we know it, and can report that to the user." [F: allemang2024ontologies, §3.2]

E: "'I don't know' is a valid answer and arguably a better answer than an inaccurate answer" [F: allemang2024ontologies, §4]. [I] Em educação essa assimetria é ainda mais forte que em uso empresarial: uma recomendação de estudo errada custa tempo do aluno e confiança no sistema.

### Os modelos ainda erram sozinhos

Meyer et al. mediram capacidades de LLMs para SPARQL `SELECT` com o framework LLM-KG-Bench, em dimensões de sintaxe, leitura semântica, criação semântica e papel da inclusão do grafo no prompt, avaliando modelos GPT, Gemini e Claude. Concluem que trabalhar com consultas SPARQL `SELECT` "is still challenging for LLMs and heavily depends on the specific LLM as well as the complexity of the task"; corrigir erros básicos de sintaxe "seems to pose no problems for the best of the current LLMs evaluated", mas "creating semantically correct SPARQL SELECT queries is difficult in several cases" [F: meyer2024sparqlcap, resumo].

[I] Sintaxe resolvida, semântica não — exatamente a lacuna que o OBQC preenche de forma determinística.

Diallo, Reyd e Zouaq avaliam a linha anterior, de tradução neural: comparam modelos pré-treinados, não pré-treinados e LLMs, com análise sistemática de erro e teste de generalização. Observam que "it is not trivial for a NMT model to learn to transform natural language into KB elements (URIs), particularly since most elements are seen very few times during training", e que palavras desconhecidas costumam ser elementos da base de conhecimento, "which can lead to irrelevant URIs in the generated queries" [F: diallo2024neuralsparql, resumo e §1].

[I] O problema dos URIs é o mesmo que o aterramento por rótulos resolve, e é a razão pela qual `skos:altLabel` importa aqui.

### O campo tem competição ativa

Existe um **TEXT2SPARQL Challenge**, em sua segunda edição, colocalizado com o Text2KG no ESWC 2026, em Dubrovnik [F: smeros2026text2sparql, metadados do local de publicação]. Trabalhos recentes exploram aterramento por esquema de forma agêntica [F: zhang2026saga, resumo].

### O que o modelo precisa saber

[I] Requisitos de aterramento, em ordem de importância, agora apoiados na evidência acima:

| Insumo | Papel | Apoio |
|---|---|---|
| Ontologia com domínio e contradomínio | aterra a geração e habilita o OBQC | [F: allemang2024ontologies, §3.1] |
| Rótulos e sinônimos dos conceitos | mapeiam a linguagem do usuário aos IRIs; atacam o problema de URIs raros | [F: diallo2024neuralsparql, §1] |
| Consultas de exemplo | fixam o padrão de uso de grafos nomeados e caminhos | [I] |
| Convenções do domínio | que `preRequisitoDe` afirma só o vínculo imediato e o fecho se obtém com `+` | [F: w3c2013sparql11query, §9.4] |

O segundo item é onde SKOS paga por si: `skos:altLabel` e `skos:hiddenLabel` registram as formas alternativas, inclusive grafias com erro comum, pelas quais um usuário se refere a um conceito [F: w3c2009skos].

### Salvaguardas

[I] Recomendações deste documento, as duas primeiras agora apoiadas em evidência:

1. **Validação determinística antes da execução** (OBQC ou equivalente), com reparo iterativo e limite de ciclos; falhar explicitamente em vez de executar consulta sabidamente errada [F: allemang2024ontologies, §3].
2. **"Não sei" como resposta de primeira classe** [F: allemang2024ontologies, §4].
3. **Somente leitura.** SPARQL 1.1 inclui linguagem de atualização e Graph Store HTTP Protocol [F: w3c2013sparql11overview, §1]; a conexão usada para consultas geradas não deve ter acesso a nenhum dos dois.
4. **Limite obrigatório** de resultados e tempo. Property paths não ancorados percorrem o fecho inteiro.
5. **Mostrar a consulta** junto da resposta.
6. **Catálogo de consultas aprovadas** para as perguntas recorrentes, reduzindo geração a seleção.

## Requisitos e pressupostos

- Uma ontologia com domínio e contradomínio declarados; sem ela não há OBQC [F: allemang2024ontologies, §3.1].
- Rótulos ricos nos conceitos [F: w3c2009skos].
- Endpoint somente leitura com limites.
- Um conjunto de perguntas de referência com respostas conhecidas, para avaliar.

## Vantagens e limitações

Vantagens: acurácia três vezes maior que text-to-SQL direto no benchmark de Allemang e Sequeda [F: allemang2024ontologies, §1]; a resposta vem de dados, não do modelo; a consulta é auditável; e o erro é detectável, o que permite dizer "não sei" em vez de errar.

Limitações: a taxa de erro permanece em 20% no melhor cenário medido, caindo a 10,46% só em perguntas e esquemas de baixa complexidade [F: allemang2024ontologies, resumo e §1]; criar consultas semanticamente corretas continua difícil para LLMs [F: meyer2024sparqlcap, resumo]; o benchmark é de domínio empresarial de seguros, não educacional; e manter aterramento e exemplos atualizados é custo contínuo. [I] Resultados vazios, sob mundo aberto, significam "não afirmado" e não "não existe" (ver kg.found.reasoning) — risco de leitura que nenhuma das fontes consultadas trata.

## Alternativas e comparações

| Pergunta do usuário | Caminho |
|---|---|
| Estrutural, sobre o currículo | tradução em consulta ao grafo curado [F: allemang2024ontologies] |
| Sobre o conteúdo dos materiais | RAG vetorial |
| Global, sobre o corpus | Graph RAG [F: edge2024graphrag] |
| Recorrente e bem definida | consulta parametrizada do catálogo, sem geração [I] |

## Métricas e métodos de avaliação

As métricas usadas pela literatura consultada: **acurácia** sobre benchmark com respostas conhecidas, **taxa de erro** e **taxa de desconhecidos** ("I don't know"), estratificadas por complexidade da pergunta e do esquema [F: allemang2024ontologies, §4]. Meyer et al. avaliam em dimensões separadas de sintaxe, leitura semântica e criação semântica [F: meyer2024sparqlcap, resumo].

[I] Acrescento, para uso educacional: **taxa de vazio enganoso** (resultados vazios lidos como negativa) e **taxa de seleção** (quando há catálogo, com que frequência a pergunta é atendida por consulta aprovada em vez de gerada). Nenhuma fonte consultada usa essas duas.

## Exemplo técnico independente de domínio

```
# aterramento mínimo fornecido ao modelo
Classes:    skos:Concept, v:Competencia, v:ObjetivoDeAprendizagem, v:Item, schema:LearningResource
Relações:   skos:broader (só vínculo imediato), v:preRequisitoDe (idem),
            v:mobiliza (domain v:Competencia, range skos:Concept),
            schema:teaches, schema:assesses
Grafos:     ex:g/conceitual/v3 (curado), ex:g/pre-requisitos/inferido-* (com confiança)
Convenções: fecho transitivo com "+"; sempre nomear o grafo; sempre usar LIMIT
```

```sparql
# pergunta: "o que o aluno precisa saber antes de frações equivalentes?"
SELECT DISTINCT ?pre ?rotulo WHERE {
  GRAPH ex:g/conceitual/v3 {
    ?pre v:preRequisitoDe+ ex:c/8f3a ;
         skos:prefLabel    ?rotulo .
  }
  FILTER (lang(?rotulo) = "pt")
} LIMIT 100
```

```sparql
# OBQC, regra Domain Range, adaptada de allemang2024ontologies §3.1.5:
# se o objeto de uma tripla é o sujeito da seguinte, o range da primeira
# deve ser compatível com o domain da segunda
SELECT ?p ?rangeP ?q ?domQ WHERE {
  GRAPH :query { ?s ?p ?o . ?o ?q ?o2 }
  ?p rdfs:range  ?rangeP .
  ?q rdfs:domain ?domQ .
  FILTER NOT EXISTS { ?rangeP rdfs:subClassOf* ?domQ }
}
# cada linha retornada é um erro a explicar ao LLM para reparo
```

[I] Esse é o ponto prático do documento: a regra acima é SPARQL comum sobre a consulta gerada tratada como dado. Não exige modelo, não exige raciocinador, e detecta a classe de erro mais frequente no estudo de referência.

## Relações com outros conceitos

Depende de kg.std.sparql e de kg.found.ontologies (a ontologia é o aterramento e a base do OBQC). Complementa kg.ret.graph-rag e kg.std.shacl (validação de forma, no caso dos dados; o OBQC valida a consulta). Avaliado por kg.eng.quality.

## Lacunas e questões abertas

- **Nenhum dos benchmarks consultados é educacional.** O de Allemang e Sequeda é de seguros empresariais; o de Meyer et al. é genérico. A transposição dos números para um grafo curricular não é garantida.
- Os textos de Smeros et al. e de Zhang e Tsuda foram consultados apenas por metadados e resumo.
- O TEXT2SPARQL Challenge publica resultados que não foram examinados aqui; é a fonte mais provável de estado da arte atualizado.
- As duas métricas propostas por este documento (vazio enganoso, taxa de seleção) não são usadas por nenhuma fonte consultada.
- [H] O catálogo de consultas aprovadas deve cobrir a maioria das perguntas reais de um grafo curricular, porque as competency questions são poucas e estáveis; não verificado.
- Como apresentar ao usuário a diferença entre "não existe" e "não afirmado" continua sem tratamento na literatura consultada.
- O OBQC depende de `rdfs:domain` e `rdfs:range` declarados; quanto de ontologia é necessário para que ele funcione bem não foi quantificado pelos autores.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| allemang2024ontologies | academico | 2026-10-29 |
| meyer2024sparqlcap | academico | 2026-10-29 |
| diallo2024neuralsparql | academico | 2026-10-29 |
| smeros2026text2sparql | academico | 2026-10-29 |
| zhang2026saga | academico | 2026-10-29 |
| w3c2013sparql11query | normativo | 2026-10-29 |
| w3c2013sparql11overview | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| edge2024graphrag | academico | 2026-10-29 |
| abdelmagied2025graphrag | academico | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
