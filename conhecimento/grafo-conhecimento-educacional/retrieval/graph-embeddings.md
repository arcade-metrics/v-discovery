---
id: kg.ret.graph-embeddings
titulo: Embeddings de grafo
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, yao2019jointembedding, alatrash2025prerequisite]
relacoes:
  - { tipo: parte-de, alvo: kg.found.reasoning }
  - { tipo: alternativa-a, alvo: kg.ret.graph-rag }
  - { tipo: complementa, alvo: kg.eng.construction }
  - { tipo: relacionado-a, alvo: kg.curr.prerequisites }
  - { tipo: relacionado-a, alvo: kg.eng.quality }
termos: [knowledge graph embedding, entity embedding, relation embedding, scoring function, completamento de grafo, inferência indutiva, literal, dimensão]
---

# Embeddings de grafo

## Definição e terminologia

**Knowledge graph embeddings** são representações vetoriais densas das entidades e relações de um grafo. Hogan et al. descrevem o objetivo principal como "to create a dense representation of the graph" em um espaço de dimensão tipicamente entre 50 e 1.000; o embedding do grafo "is composed of an entity embedding" para cada nó e de representações para os rótulos de aresta; cada abordagem "defines a scoring function that accepts" o embedding do nó sujeito, o do rótulo da aresta e o do nó objeto, e computa um valor [F: hogan2021knowledgegraphs, §5.2].

São um método **indutivo**: aprendem padrões dos dados, em contraste com os métodos dedutivos de regras e ontologias [F: hogan2021knowledgegraphs, §1, §5]. Os embeddings "can use self-supervision to learn" [F: hogan2021knowledgegraphs, §5].

O que não é: um embedding não é uma afirmação. Produz pontuações, não fatos. Tratar a saída como aresta do grafo sem marcação de confiança e proveniência é erro de modelagem. [I]

## Problema que resolve

[I] Duas tarefas que a consulta estrutural não resolve:

1. **Completamento**: sugerir arestas que provavelmente faltam. Em um grafo curricular, propor relações de pré-requisito candidatas à revisão humana.
2. **Similaridade**: "que conceitos se parecem com X", quando semelhança não é hierarquia nem relação declarada.

## Fundamentos e funcionamento

### O caso educacional é atípico

Yao et al. observam explicitamente que modelos convencionais de embedding "rely on structural relationships among entities and relations", mas que "in educational knowledge graphs, structural relationships are not the focus. Instead, rich literals of the graphs are more valuable". Propõem um modelo que considera informação estrutural e literal conjuntamente [F: yao2019jointembedding, resumo].

[I] Essa observação é importante e contraintuitiva: em um grafo curricular, os enunciados das habilidades — texto longo e descritivo — carregam mais sinal que a topologia, que costuma ser uma árvore rasa. Métodos que ignoram os literais desperdiçam a maior parte da informação.

É coerente com o que Alatrash et al. fazem ao inferir pré-requisitos: dos dez critérios que combinam, apenas três são baseados em grafo; os demais vêm de estrutura do documento, hyperlinks da Wikipédia, hierarquia da DBpedia e análise de texto [F: alatrash2025prerequisite, tabela 1]. O grafo é uma fonte entre cinco categorias, não a principal.

### Relação com métodos dedutivos

Hogan et al. tratam ainda mineração de regras, que opera sob suposições de completude parcial, como a *Partial Completeness Assumption* [F: hogan2021knowledgegraphs, §5.4]. [I] Isso importa porque um grafo educacional é sabidamente incompleto: ausência de aresta de pré-requisito não significa ausência de dependência.

## Requisitos e pressupostos

- Volume suficiente de arestas para treinar. [I] Um grafo curricular de alguns milhares de nós com topologia de árvore pode não ter sinal estrutural suficiente — daí a relevância dos literais.
- Uma decisão sobre o que fazer com a saída: entrada em revisão humana ou aresta direta com confiança. A primeira é a recomendação deste documento.
- Marcação de proveniência e confiança nas arestas geradas (ver kg.std.prov-o, kg.found.context-and-reification).

## Vantagens e limitações

Vantagens: encontram padrões que a curadoria não enxerga; escalam; a similaridade vetorial resolve consultas que a estrutura não resolve.

Limitações: a saída não é explicável; um grafo educacional raso oferece pouco sinal estrutural [F: yao2019jointembedding]; embeddings sobre grafo incompleto propagam a incompletude; e o modelo precisa ser retreinado quando o grafo muda. [I]

## Alternativas e comparações

| Objetivo | Abordagem | Observação |
|---|---|---|
| Caminho e fecho | SPARQL property path | exato, explicável (kg.std.sparql) |
| Derivar fatos de axiomas | OWL / RDFS | dedutivo, explicável (kg.found.reasoning) |
| Sugerir arestas faltantes | embeddings, mineração de regras | indutivo, não explicável [F: hogan2021knowledgegraphs, §5] |
| Pré-requisitos a partir de texto e grafo | critérios múltiplos combinados por votação | [F: alatrash2025prerequisite] |
| Perguntas globais sobre corpus | Graph RAG | kg.ret.graph-rag |

## Métricas e métodos de avaliação

[I] Para completamento, as métricas usuais do campo são de ranqueamento (posição da aresta correta entre candidatas). Nenhuma fonte consultada reporta números para grafos educacionais; Yao et al. propõem um modelo e reportam avaliação, mas o texto integral não foi consultado [F: yao2019jointembedding].

A métrica que importa neste domínio é outra: **taxa de aceitação em revisão humana**. Se a curadoria rejeita a maioria das sugestões, o método custa mais do que entrega. [I]

## Exemplo técnico independente de domínio

```
# papel no fluxo de curadoria: sugerir, não afirmar
grafo curado  ──┐
                ├──> modelo de embedding ──> candidatas ranqueadas
literais        ──┘                                │
                                                   ▼
                                          revisão humana
                                                   │
                      ┌────────────────────────────┴───────────┐
                      ▼                                        ▼
         aceita: entra no grafo curado            rejeita: registra como negativa
         com proveniência de origem               (sinal para o próximo treino)
```

```turtle
# candidata gerada por modelo, no seu próprio grafo, nunca misturada ao curado
GRAPH ex:g/candidatas/embedding-2026-10 {
  ex:cand/5512 a v:CandidataPreRequisito ;
      v:origem    ex:c/proporcao ;
      v:destino   ex:c/escala ;
      v:pontuacao 0.71 ;
      v:status    v:PendenteRevisao .
}
ex:g/candidatas/embedding-2026-10
    prov:wasAttributedTo ex:agente/modelo-embedding-v1 ;
    prov:used            ex:g/conceitual/v3 .
```

## Relações com outros conceitos

Parte de kg.found.reasoning (é o ramo indutivo). Alternativa a kg.ret.graph-rag. Complementa kg.eng.construction (povoamento do grafo). Relaciona-se com kg.curr.prerequisites (o caso de uso mais direto) e kg.eng.quality.

## Lacunas e questões abertas

- O texto de Yao et al. foi consultado via arXiv, mas seus resultados experimentais não foram tabulados aqui: o documento usa apenas a observação qualitativa sobre o peso dos literais, que é o ponto relevante para modelagem. A versão publicada em periódico (Springer, DOI 10.1007/978-3-030-41099-5_12) não foi consultada.
- A seção 5.2 do survey de Hogan et al. foi consultada apenas nos parágrafos introdutórios; as famílias de modelos (translacionais, tensoriais, neurais) não foram descritas aqui para não afirmar sem leitura.
- Não há, nas fontes consultadas, evidência de que arestas de pré-requisito sugeridas por embedding melhorem resultados pedagógicos.
- [H] Em grafos curriculares, métodos baseados em literais devem superar os puramente estruturais, dada a observação de Yao et al. [F: yao2019jointembedding] e a composição de critérios de Alatrash et al., em que apenas 3 dos 10 critérios são de grafo [F: alatrash2025prerequisite, tabela 1]; não verificado com números.
- A taxa de aceitação em revisão humana, proposta aqui como métrica central, não é usada por nenhuma fonte consultada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| yao2019jointembedding | academico | 2026-10-29 |
| alatrash2025prerequisite | academico | 2026-10-29 |
