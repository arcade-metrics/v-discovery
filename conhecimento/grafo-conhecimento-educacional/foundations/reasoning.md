---
id: kg.found.reasoning
titulo: Inferência e raciocínio sobre grafos
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, w3c2012owl2overview, w3c2012owl2profiles, w3c2014rdfschema, w3c2009skos, w3c2013sparql11overview, w3c2013sparql11query, w3c2017shacl]
relacoes:
  - { tipo: depende-de, alvo: kg.found.ontologies }
  - { tipo: parte-de, alvo: kg.found.knowledge-graphs }
  - { tipo: especificado-por, alvo: kg.std.owl2 }
  - { tipo: alternativa-a, alvo: kg.std.shacl }
  - { tipo: relacionado-a, alvo: kg.curr.prerequisites }
  - { tipo: relacionado-a, alvo: kg.eng.storage-and-query }
termos: [entailment, inferência dedutiva, inferência indutiva, open world assumption, closed world assumption, materialização, raciocínio em tempo de consulta, fecho transitivo, entailment regime, sound, complete]
---

# Inferência e raciocínio sobre grafos

## Definição e terminologia

**Entailment** é a relação pela qual um grafo acarreta afirmações que não estão explicitamente nele. Hogan et al. distinguem dedução (regras e axiomas que derivam novas arestas a partir das existentes) de indução (padrões aprendidos dos dados, com embeddings ou mineração de regras) [F: hogan2021knowledgegraphs, §1, §4, §5].

**Open world assumption (OWA)** e **closed world assumption (CWA)** são as duas hipóteses possíveis ao interpretar o grafo. Sob CWA, se uma aresta não está no grafo (nem é acarretada por ele), assume-se falsa; sob OWA, não se pode concluir a falsidade [F: hogan2021knowledgegraphs, §4.1 e apêndice B]. RDF, RDFS e OWL adotam OWA. [I]

**Sound** e **complete**: o OWL 2 Document Overview observa que uma implementação baseada em regras operando diretamente sobre triplas RDF arbitrárias "will always be sound (that is, only correct answers to queries will be computed), but it may not be complete (that is, it is not guaranteed that all correct answers to queries will be computed)" [F: w3c2012owl2overview, §2.4].

O que não é: inferência não é validação. Sob mundo aberto, um grafo que "falta" uma propriedade obrigatória não é inconsistente — é incompleto. Para verificar que os dados estão como se espera, usa-se SHACL (ver kg.std.shacl).

## Problema que resolve

Evita afirmar explicitamente tudo que decorre do que já foi afirmado. [I] Em um grafo curricular isso aparece de imediato: se a hierarquia tem 4 níveis e as relações de pré-requisito são declaradas só entre vizinhos, perguntar "tudo que precede o conceito X" exige ou materializar o fecho transitivo ou calculá-lo na consulta.

Também permite detectar contradições. SKOS, por exemplo, trata relação hierárquica e associativa como "fundamentally distinct in nature", de modo que um choque entre as duas "is not consistent with the SKOS data model" [F: w3c2009skos, §8.6.10]. Um raciocinador ou um validador pode encontrar esse choque antes que vire sugestão errada ao aluno.

## Fundamentos e funcionamento

### Níveis de inferência

| Nível | O que deriva | Custo |
|---|---|---|
| Nenhum | nada | zero |
| RDFS | tipo por `rdfs:domain`/`rdfs:range`, subsunção por `rdfs:subClassOf`, subpropriedade | baixo [F: w3c2014rdfschema] |
| OWL 2 RL | regras sobre triplas, sem inferir indivíduos novos | PTIME-complete para consistência e verificação de instância [F: w3c2012owl2profiles, tabela 10] |
| OWL 2 EL | subsunção em ontologias grandes | PTIME-complete [F: w3c2012owl2profiles, tabela 10] |
| OWL 2 QL | consulta conjuntiva reescrita para SQL | em AC0 em complexidade de dados [F: w3c2012owl2profiles, tabela 10] |
| OWL 2 DL (semântica direta) | tudo que OWL 2 exprime | N2EXPTIME-complete em complexidade combinada; complexidade de dados decidível mas em aberto, com limite inferior NP-hard [F: w3c2012owl2profiles, tabela 10] |
| OWL 2 semântica RDF-based | — | indecidível em todas as medidas [F: w3c2012owl2profiles, tabela 10] |

[I] A leitura prática: um grafo educacional que quer inferência barata e previsível fica em RDFS ou OWL 2 RL. OWL 2 DL completo só se justifica quando a consistência formal do modelo é o produto.

### Materialização versus tempo de consulta

[I] Duas estratégias, com o mesmo resultado lógico e custos opostos:

- **Materializar**: computar o fecho e gravar as triplas derivadas. Consulta rápida; escrita cara; invalidação complexa quando uma aresta muda; o grafo passa a misturar afirmado e derivado, e sem grafo nomeado separado perde-se a distinção.
- **Em tempo de consulta**: deixar o fecho para a consulta. SPARQL 1.1 oferece *property paths*, inclusive casamento de caminho de comprimento arbitrário [F: w3c2013sparql11query, §9.4], o que cobre fecho transitivo sem raciocinador. SPARQL 1.1 Entailment Regimes define a semântica de consultas sob regimes como RDF Schema, OWL ou RIF [F: w3c2013sparql11overview, §1].

### O caso do fecho transitivo em SKOS

SKOS resolve isso por convenção explícita, não por inferência: `skos:broader` e `skos:narrower` são usados "only to assert a direct (i.e., immediate) hierarchical link" e, para sustentar essa convenção, "are not declared as transitive properties"; `skos:broaderTransitive` e `skos:narrowerTransitive` existem para representar vínculo direto ou indireto e, por convenção, "are not used to make assertions" — servem para inferir o fecho transitivo [F: w3c2009skos, §8.1].

[I] Esse é um padrão reaproveitável: separar a aresta afirmada da aresta derivada em propriedades distintas, em vez de depender do raciocinador para distinguir. Vale literalmente para pré-requisitos (ver kg.curr.prerequisites).

### Ciclos

SKOS registra que um ciclo na relação hierárquica é consistente com seu modelo de dados: "there is no condition requiring that `skos:broaderTransitive` be irreflexive" [F: w3c2009skos, §8.6.8]. [I] Portanto, se o grafo educacional não pode ter ciclo de pré-requisito, essa restrição precisa ser imposta por validação (SHACL, ver kg.std.shacl) ou por axioma OWL próprio — não vem de graça.

### Indução

Hogan et al. tratam também métodos indutivos: embeddings de grafo aprendem representação densa que preserva estrutura e podem ser usados para completar o grafo [F: hogan2021knowledgegraphs, §5.2]; mineração de regras opera sob suposições de completude parcial, como a *Partial Completeness Assumption* [F: hogan2021knowledgegraphs, §5.4]. Ver kg.ret.graph-embeddings.

## Requisitos e pressupostos

- Hipótese de mundo declarada. Sob OWA, "o aluno não domina o conceito X" não decorre da ausência de evidência.
- Separação entre triplas afirmadas e derivadas, se houver materialização. Grafos nomeados servem para isso (ver kg.found.identifiers-and-triples).
- Perfil OWL escolhido conscientemente, com a tabela de complexidade à vista. Os resultados são de pior caso e não dizem o que algoritmos implementados fazem em instâncias típicas [F: w3c2012owl2profiles, §5].

## Vantagens e limitações

Vantagens: menos triplas afirmadas; consultas mais simples; detecção de contradição; semântica explícita em vez de lógica escondida em código de aplicação.

Limitações: custo computacional que escala mal com expressividade; materialização introduz problema de invalidação; e inferência sobre dados sujos propaga erro — Hogan et al. listam "imprecise entailments" entre as causas de inacurácia semântica [F: hogan2021knowledgegraphs, §7.1.2].

## Alternativas e comparações

| Precisa de | Use |
|---|---|
| Fecho transitivo para consulta | property path `+` em SPARQL [F: w3c2013sparql11query, §9.4] |
| Fecho transitivo para leitura rápida e repetida | materialização em grafo nomeado separado [I] |
| Garantir que os dados têm a forma esperada | SHACL [F: w3c2017shacl] |
| Garantir que o modelo não se contradiz | raciocinador OWL [F: w3c2012owl2overview, §2.4] |
| Descobrir relações ausentes | métodos indutivos [F: hogan2021knowledgegraphs, §5] |

## Exemplo técnico independente de domínio

```sparql
# fecho transitivo em tempo de consulta, sem raciocinador
SELECT ?anterior WHERE {
  ?anterior :preRequisitoDe+ <https://example.org/id/c/1b2c> .
}

# o mesmo, por propriedade derivada materializada em grafo separado
SELECT ?anterior WHERE {
  GRAPH <https://example.org/g/derivado> {
    ?anterior :preRequisitoDeTransitivo <https://example.org/id/c/1b2c> .
  }
}
```

```
# regra de materialização, estilo OWL 2 RL / N3, com a convenção SKOS aplicada a pré-requisitos
{ ?a :preRequisitoDe ?b }                             => { ?a :preRequisitoDeTransitivo ?b } .
{ ?a :preRequisitoDeTransitivo ?b . ?b :preRequisitoDeTransitivo ?c } => { ?a :preRequisitoDeTransitivo ?c } .
# detecção de ciclo: a aparecer no próprio fecho é erro de dado, não inconsistência lógica
```

## Relações com outros conceitos

Depende de kg.found.ontologies (sem esquema não há o que inferir). Parte de kg.found.knowledge-graphs. Especificado por kg.std.owl2. Alternativa a kg.std.shacl quando o objetivo é verificar forma e não derivar fatos. Relaciona-se com kg.curr.prerequisites (o caso de uso mais direto em educação) e kg.eng.storage-and-query (quem executa a inferência).

## Lacunas e questões abertas

- Não há, nas fontes consultadas, medição do custo de materializar o fecho de pré-requisitos em grafos curriculares reais; os números disponíveis são de complexidade de pior caso [F: w3c2012owl2profiles, §5].
- O tratamento de incerteza (uma relação de pré-requisito inferida com confiança 0,7) não é coberto por OWL nem por SKOS; exige modelagem de contexto (ver kg.found.context-and-reification). [H] Representar confiança como anotação da aresta e filtrar por limiar na consulta parece suficiente para uso prático, mas não foi verificado.
- Regimes de entailment em SPARQL: o suporte real por implementação não foi levantado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2012owl2overview | normativo | 2026-10-29 |
| w3c2012owl2profiles | normativo | 2026-10-29 |
| w3c2014rdfschema | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| w3c2013sparql11overview | normativo | 2026-10-29 |
| w3c2013sparql11query | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
