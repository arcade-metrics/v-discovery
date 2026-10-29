---
id: kg.mod.evidence-and-mastery
titulo: Evidência e estado de domínio no grafo
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, w3c2013provo, w3c2026rdf12concepts, w3c2014rdf11concepts, schemaorg2026learningresource, abdelmagied2025graphrag]
relacoes:
  - { tipo: parte-de, alvo: kg.mod.conceptual-model }
  - { tipo: depende-de, alvo: kg.mod.layer-separation }
  - { tipo: depende-de, alvo: kg.found.context-and-reification }
  - { tipo: especificado-por, alvo: kg.std.prov-o }
  - { tipo: relacionado-a, alvo: kg.found.reasoning }
  - { tipo: complementa, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
termos: [evidência, estado de domínio, mastery, estimativa, observação, append-only, validade temporal, incerteza, recomputação, personal knowledge graph]
---

# Evidência e estado de domínio no grafo

## Definição e terminologia

- **Observação**: um fato registrado sobre o que o aluno fez. "Respondeu o item 77 em 42 segundos, incorretamente, às 14:03 de 29/10/2026." Imutável.
- **Evidência**: uma observação interpretada à luz do grafo conceitual. A mesma resposta vira evidência sobre os conceitos que o item avalia.
- **Estado de domínio** (*mastery*): a estimativa, em um instante, de que o aluno domina um conceito. Derivada, probabilística, revisável.

[I] A distinção importa porque as três têm regimes diferentes: observação é append-only, evidência é derivada do grafo conceitual vigente, estado de domínio é recalculável. Ver kg.mod.layer-separation.

O que não é: estado de domínio não é uma aresta afirmada do grafo conceitual. Afirmar `aluno :domina conceito` sem qualificar instante, confiança e modelo que a produziu destrói a possibilidade de auditoria e de recomputação. [I]

## Problema que resolve

[I] Quatro propriedades que uma modelagem ingênua perde:

| Propriedade | Por que importa |
|---|---|
| Temporalidade | domínio decai; uma estimativa sem instante é inútil |
| Incerteza | 0,82 e 0,51 levam a decisões pedagógicas diferentes |
| Rastreabilidade | de que observações e de que modelo saiu a estimativa |
| Recomputabilidade | quando o algoritmo melhora, as estimativas antigas devem poder ser refeitas |

Hogan et al. tratam esse espaço sob *context*: dados podem ser verdadeiros apenas com respeito a um certo contexto, com o contexto temporal como caso central [F: hogan2021knowledgegraphs, §3.3]. E registram que *timeliness* — "the degree to which the knowledge graph is currently up-to-date with the real world state" — é dimensão de qualidade: um grafo pode ser semanticamente acurado agora e tornar-se inacurado rapidamente se não houver procedimento de atualização [F: hogan2021knowledgegraphs, §7.1.3].

[I] Em um grafo com estado de domínio, *timeliness* não é uma preocupação ocasional: é a natureza do dado.

## Fundamentos e funcionamento

### Por que reificar

Uma estimativa de domínio é, por construção, uma afirmação qualificada. As opções de modelagem são as de kg.found.context-and-reification. [I] Na prática, três funcionam:

| Forma | Vantagem | Custo |
|---|---|---|
| Nó de estimativa (representação direta) | funciona em qualquer stack; consulta simples com SPARQL | um nó por (aluno, conceito, instante) |
| Grafo nomeado por rodada de cálculo | contexto compartilhado; proveniência natural por `prov:used` | granularidade por lote, não por estimativa |
| Triple term / reifying triple (RDF 1.2) | conciso | RDF 1.2 em Candidate Recommendation Snapshot [F: w3c2026rdf12concepts] |

A recomendação deste documento é combinar as duas primeiras: **nó de estimativa dentro de grafo nomeado por rodada**. O nó carrega a incerteza; o grafo carrega a proveniência. [I]

### Proveniência obrigatória

Os termos de ponto de partida de PROV-O bastam: `prov:Entity`, `prov:Activity`, `prov:Agent`, `prov:wasGeneratedBy`, `prov:used`, `prov:wasAttributedTo`, `prov:startedAtTime` [F: w3c2013provo, §2].

A declaração crítica é `prov:used`: a rodada de cálculo declara **de que dados observados e de que versão do grafo conceitual** derivou. [I] Sem isso, quando o currículo muda, não há como saber se uma estimativa antiga se refere ao mesmo conceito.

### Estratégia de retenção

[I] Guardar toda estimativa de todo aluno para todo conceito a cada rodada é inviável. Três políticas, com trade-offs distintos:

| Política | Volume | Auditoria | Recomputação |
|---|---|---|---|
| Só o estado corrente | mínimo | nenhuma | possível, se observações estiverem íntegras |
| Estado corrente + log de rodadas | médio | boa | possível |
| Toda estimativa, append-only | alto | total | desnecessária |

A segunda é o compromisso usual. Em todos os casos, **as observações nunca são descartadas**: elas são a fonte de verdade da qual tudo o mais deriva.

### A fronteira com a aprendizagem adaptativa

Como se calcula a estimativa — knowledge tracing bayesiano, modelos logísticos, teoria de resposta ao item — é assunto do domínio `aprendizagem-adaptativa` (adp.kt.bayesian-knowledge-tracing, adp.irt.item-response-theory). Este documento trata apenas de **como representar o resultado no grafo**, não de como produzi-lo. [I]

A literatura de grafos educacionais já separa os dois: o pipeline de Graph RAG de Abdelmagied et al. usa EduKGs e *Personal Knowledge Graphs* (PKGs) como estruturas distintas [F: abdelmagied2025graphrag, resumo].

### O que o item avalia

A ligação entre observação e conceito passa pelo item, e o vínculo item → conceito é o que transforma resposta em evidência. schema.org oferece `assesses`: "the item being described is intended to assess the competency or learning outcome defined by the referenced term" [F: schemaorg2026learningresource].

[I] Quando um item avalia mais de um conceito, uma resposta errada não diz qual falhou. Esse é o problema de atribuição de crédito, tratado no domínio vizinho. No grafo, a consequência é que a aresta `avalia` deveria admitir peso — e isso a traz de volta para o território da anotação de aresta.

## Requisitos e pressupostos

- As três camadas separadas (kg.mod.layer-separation).
- Observações imutáveis com instante e instrumento.
- Toda estimativa com instante, incerteza e proveniência; nenhuma estimativa afirmada como fato simples.
- Identificadores de conceito estáveis entre versões do currículo (kg.found.identifiers-and-triples).

## Vantagens e limitações

Vantagens: estimativas auditáveis e recomputáveis; a incerteza é dado, não convenção; a separação entre observado e derivado sobrevive a mudanças de algoritmo; proveniência padronizada com PROV-O.

Limitações: volume; cada estimativa qualificada custa um nó e várias triplas; consultas que cruzam estado de domínio e grafo conceitual são mais longas; e um triplestore pode não ser a tecnologia certa para a camada de observações. [I]

## Alternativas e comparações

| Modelagem | Consequência |
|---|---|
| `aluno :domina conceito` (aresta simples) | sem instante, sem incerteza, sem proveniência; insustentável |
| `aluno :domina conceito` + propriedades no aluno | não escala para muitos conceitos |
| Nó de estimativa | o proposto; custo em nós |
| Grafo de propriedades com atributos na aresta | compacto; fora do ecossistema RDF (ver kg.found.rdf-vs-property-graphs) |
| Estado fora do grafo, só referência por IRI | melhor para volume; junção por aplicação |

## Exemplo técnico independente de domínio

```trig
# observações: imutáveis
GRAPH ex:g/observado {
  ex:resp/9f81 a v:Resposta ;
      v:aluno ex:aluno/1234 ; v:item ex:item/77 ;
      v:correta false ; v:duracaoSegundos 42 ;
      v:instante "2026-10-29T14:03:11Z"^^xsd:dateTime .
}

# estimativas: nó por (aluno, conceito), dentro de um grafo por rodada
GRAPH ex:g/modelo/2026-10-29T15:00Z {
  ex:est/1234-8f3a a v:EstimativaDeDominio ;
      v:aluno          ex:aluno/1234 ;
      v:conceito       ex:c/8f3a ;
      v:probabilidade  0.41 ;
      v:instante       "2026-10-29T15:00:00Z"^^xsd:dateTime ;
      v:nObservacoes   7 .
}

# proveniência da rodada: de onde veio e com que modelo
ex:g/modelo/2026-10-29T15:00Z a prov:Entity ;
    prov:wasGeneratedBy  ex:rodada/2026-10-29T15 ;
    prov:wasDerivedFrom  ex:g/modelo/2026-10-29T09:00Z .

ex:rodada/2026-10-29T15 a prov:Activity ;
    prov:startedAtTime "2026-10-29T15:00:00Z"^^xsd:dateTime ;
    prov:used          ex:g/observado , ex:g/conceitual/v3 ;
    prov:wasAttributedTo ex:agente/estimador-v2.1 .
```

```sparql
# conceitos em que o aluno está abaixo do limiar, mas cujos pré-requisitos já domina
SELECT ?c ?p WHERE {
  GRAPH ex:g/modelo/2026-10-29T15:00Z {
    ?e v:aluno ex:aluno/1234 ; v:conceito ?c ; v:probabilidade ?p .
  }
  FILTER (?p < 0.6)
  FILTER NOT EXISTS {
    GRAPH ex:g/conceitual/v3 { ?pre v:preRequisitoDe ?c }
    GRAPH ex:g/modelo/2026-10-29T15:00Z {
      ?e2 v:aluno ex:aluno/1234 ; v:conceito ?pre ; v:probabilidade ?p2 .
      FILTER (?p2 < 0.6)
    }
  }
}
```

[I] Essa consulta é a competency question 6 de kg.mod.conceptual-model em forma executável: o que o aluno está pronto para aprender. Repare que ela atravessa duas camadas e exige que ambas estejam no mesmo dataset ou federadas.

## Relações com outros conceitos

Parte de kg.mod.conceptual-model. Depende de kg.mod.layer-separation e de kg.found.context-and-reification. Especificado por kg.std.prov-o. Relaciona-se com kg.found.reasoning. Atravessa domínio: complementa adp.lm.learner-model e relaciona-se com adp.kt.bayesian-knowledge-tracing, que tratam de como a estimativa é produzida.

## Lacunas e questões abertas

- A modelagem proposta não foi validada contra implementação; é recomendação deste documento.
- Não foi levantado o custo real em triplas nem o desempenho de consultas que cruzam camadas.
- Peso na aresta `avalia` (quando um item avalia vários conceitos) traz de volta o problema de anotação de aresta e não foi resolvido aqui.
- [H] Guardar estado corrente mais log de rodadas, descartando estimativas intermediárias após um período, parece o compromisso certo entre volume e auditoria — não verificado.
- Decaimento de domínio ao longo do tempo é modelado pelos algoritmos do domínio vizinho (ver adp.sr.memory-and-forgetting); se o grafo deve guardar a curva ou só o último valor é questão aberta.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| w3c2026rdf12concepts | normativo | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| abdelmagied2025graphrag | academico | 2026-10-29 |
