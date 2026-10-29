---
id: kg.eng.versioning-and-provenance
titulo: Versionamento e proveniência do grafo
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2013provo, w3c2012owl2syntax, w3c2014rdf11concepts, hogan2021knowledgegraphs, ims2017case10, onedtech2025case, esco2026what]
relacoes:
  - { tipo: depende-de, alvo: kg.std.prov-o }
  - { tipo: depende-de, alvo: kg.found.identifiers-and-triples }
  - { tipo: complementa, alvo: kg.found.context-and-reification }
  - { tipo: complementa, alvo: kg.eng.quality }
  - { tipo: relacionado-a, alvo: kg.curr.competency-frameworks }
  - { tipo: relacionado-a, alvo: kg.mod.layer-separation }
termos: [versionamento, owl:versionIRI, grafo nomeado, proveniência, replacedBy, identificador estável, snapshot, delta, retrocompatibilidade, dependência externa]
---

# Versionamento e proveniência do grafo

## Definição e terminologia

**Versionamento** é a capacidade de referir-se a um estado passado do grafo e de saber o que mudou entre dois estados. **Proveniência** é o registro de origem, autoria e derivação de cada afirmação.

[I] São problemas distintos e costumam ser resolvidos pelo mesmo mecanismo — o grafo nomeado — o que faz com que sejam confundidos. Versão responde "como era"; proveniência responde "quem disse e por quê".

## Problema que resolve

[I] Quatro situações concretas em um grafo educacional:

| Situação | O que se precisa |
|---|---|
| O currículo oficial lança nova edição | saber o que mudou; manter o alinhamento anterior válido para a versão anterior |
| Uma estimativa de domínio de março referencia um conceito removido em outubro | saber a que versão a estimativa se referia |
| Um crosswalk é contestado | saber quem o fez, quando e com que critério |
| Um pré-requisito inferido leva a uma recomendação errada | saber de que lote de extração veio e com que confiança |

A competency question 8 de kg.mod.conceptual-model — "como a versão 3 do currículo difere da versão 2" — é precisamente este documento.

## Fundamentos e funcionamento

### Os mecanismos disponíveis

| Mecanismo | O que versiona | Fonte |
|---|---|---|
| `owl:versionIRI` | a ontologia (esquema) | [F: w3c2012owl2syntax] |
| Grafo nomeado | um conjunto de afirmações | [F: w3c2014rdf11concepts, §4] |
| PROV-O `wasDerivedFrom` | a relação entre duas versões | [F: w3c2013provo, §2] |
| `replacedBy` do CASE | item que foi suplantado por outro | [F: ims2017case10, tabela 7.3.1] |

Hogan et al. registram a motivação de gerir vários grafos em vez de um monolítico: permite "update or refine data from one source, to distinguish untrustworthy sources from more trustworthy ones" [F: hogan2021knowledgegraphs, §2.1.4].

### A regra fundamental

**Identificadores de entidade não versionam; grafos sim.** [I]

Ou seja: o IRI do conceito "frações equivalentes" é o mesmo na versão 2 e na versão 3 do currículo. O que muda é o grafo nomeado em que as afirmações sobre ele vivem. Se o IRI carregasse a versão (`/v3/c/8f3a`), toda estimativa de domínio, todo alinhamento e toda referência externa quebrariam a cada edição.

Isso é a aplicação direta da regra de kg.found.identifiers-and-triples: um id nunca muda depois de publicado.

### Estratégias de versionamento

[I] Três arranjos, com trade-offs:

| Estratégia | Como | Custo | Consulta "como era em X" |
|---|---|---|---|
| Snapshot por versão | um grafo nomeado completo por versão | alto em espaço | trivial |
| Delta | um grafo com as mudanças desde a anterior | baixo | exige reconstrução |
| Grafo corrente + log de mudanças | o estado atual mais os deltas históricos | médio | reconstrução para trás |

Para um grafo curricular, que versiona em escala de meses e tem dezenas de milhares de triplas, snapshot é simples e barato o bastante. [I] Para a camada de estado de domínio, que muda continuamente, snapshot é inviável — ver kg.mod.evidence-and-mastery.

### Proveniência mínima

Os termos de ponto de partida de PROV-O bastam [F: w3c2013provo, §2]. O conjunto mínimo que este documento recomenda para cada grafo nomeado [I]:

```
prov:wasGeneratedBy   → a atividade (curadoria, extração, cálculo)
prov:wasAttributedTo  → o agente (equipe, pipeline, modelo)
prov:generatedAtTime  → quando
prov:used             → de que fontes e de que outros grafos derivou
prov:wasDerivedFrom   → a versão anterior deste mesmo grafo
```

`prov:used` é o campo que resolve o segundo caso da tabela de problemas: uma estimativa declara de que versão do grafo conceitual partiu.

### Dependências externas

Vocabulários de terceiros versionam por conta própria: ESCO está em v1.2.1, release v6.0.0, com última atualização em 10/12/2025 [F: esco2026what]; CASE v1.1 é de 24/01/2025 e introduziu o campo `CFDocument.caseVersion`, cujo "only expected value is 1.1 since this field does not exist for CASE 1.0" [F: onedtech2025case].

[I] A defesa é registrar, no grafo de alinhamento, a versão exata da fonte externa contra a qual o alinhamento foi feito. Quando a fonte avança, o alinhamento anterior não se torna errado — torna-se um alinhamento a uma versão anterior, o que é informação diferente e útil.

CASE oferece ainda `replacedBy`: "the origin of the association has been supplanted by, displaced by, or superseded by the destination of the association" [F: ims2017case10, tabela 7.3.1]. [I] É a construção certa para registrar que uma habilidade foi substituída por outra entre edições, preservando as referências antigas.

## Requisitos e pressupostos

- IRIs estáveis, independentes de versão (kg.found.identifiers-and-triples).
- Proveniência escrita no momento da criação do lote, não reconstruída.
- Política explícita sobre o que acontece com entidades removidas: manter com marcação de obsolescência, ou excluir. [I] Manter é quase sempre melhor, porque referências externas não desaparecem.
- Separação de camadas, já que cada uma versiona em ritmo diferente (kg.mod.layer-separation).

## Vantagens e limitações

Vantagens: consultas históricas sem infraestrutura extra, porque grafos nomeados são RDF padrão [F: w3c2014rdf11concepts, §4]; auditoria completa; alinhamentos sobrevivem a mudanças da fonte externa; recomputação de estimativas com contexto conhecido.

Limitações: espaço, se a estratégia for snapshot; consultas que atravessam versões ficam longas; não há padrão para *diff* de grafos RDF entre versões — a comparação é trabalho de aplicação; e a disciplina de proveniência depende de processo, não de tecnologia. [I]

## Alternativas e comparações

| Precisa de | Mecanismo |
|---|---|
| Versionar o esquema | `owl:versionIRI` [F: w3c2012owl2syntax] |
| Versionar as afirmações | grafo nomeado por versão [F: w3c2014rdf11concepts] |
| Ligar versões | `prov:wasDerivedFrom` [F: w3c2013provo] |
| Registrar substituição de item | `replacedBy` do CASE [F: ims2017case10] |
| Registrar validade temporal de uma aresta | reificação ou triple term (kg.found.context-and-reification) |

## Exemplo técnico independente de domínio

```trig
# esquema versionado por owl:versionIRI
<https://example.org/voc/> a owl:Ontology ;
    owl:versionIRI <https://example.org/voc/3.1.0> ;
    owl:priorVersion <https://example.org/voc/3.0.0> .

# afirmações versionadas por grafo nomeado; o IRI do conceito NÃO muda
GRAPH ex:g/conceitual/v3 { ex:c/8f3a skos:prefLabel "Frações equivalentes"@pt . }
GRAPH ex:g/conceitual/v2 { ex:c/8f3a skos:prefLabel "Equivalência de frações"@pt . }

ex:g/conceitual/v3 a prov:Entity ;
    prov:wasDerivedFrom  ex:g/conceitual/v2 ;
    prov:wasGeneratedBy  ex:atividade/revisao-2026-10 ;
    prov:wasAttributedTo ex:agente/curadoria ;
    prov:generatedAtTime "2026-10-29T00:00:00Z"^^xsd:dateTime .

# alinhamento ancorado na versão exata da fonte externa
GRAPH ex:g/alinhamento/externo-2026-10 {
  ex:c/estatistica v:alinhadoA <IRI-externo> .
}
ex:g/alinhamento/externo-2026-10 v:versaoFonte "v1.2.1 (release v6.0.0)" .
```

```sparql
# competency question 8: o que mudou entre v2 e v3
SELECT ?s ?p ?oAntigo ?oNovo WHERE {
  GRAPH ex:g/conceitual/v2 { ?s ?p ?oAntigo }
  OPTIONAL { GRAPH ex:g/conceitual/v3 { ?s ?p ?oNovo } }
  FILTER (!BOUND(?oNovo) || ?oAntigo != ?oNovo)
}
```

[I] Essa consulta é um diff ingênuo e serve para ilustrar; um diff correto precisa tratar blank nodes e triplas acrescentadas, o que SPARQL não resolve de forma direta.

## Relações com outros conceitos

Depende de kg.std.prov-o e de kg.found.identifiers-and-triples. Complementa kg.found.context-and-reification (o mesmo mecanismo serve a contexto e a versão) e kg.eng.quality (timeliness é medida contra a versão da fonte). Relaciona-se com kg.curr.competency-frameworks e kg.mod.layer-separation.

## Lacunas e questões abertas

- Não há padrão W3C para *diff* ou patch de grafos RDF entre versões; nenhuma fonte consultada o oferece.
- O custo de armazenar snapshots completos de um grafo curricular não foi estimado.
- Não foi verificado como ESCO e CASE documentam suas próprias mudanças entre versões além do que consta nas páginas consultadas.
- [H] Para a camada conceitual, snapshot por versão com `prov:wasDerivedFrom` entre elas parece suficiente e simples; para a camada de estado de domínio, log de rodadas com retenção limitada. Nenhuma das duas escolhas foi verificada contra implementação.
- Tratamento de blank nodes em comparação entre versões é problema conhecido e não resolvido aqui.
- A política correta para entidades removidas (manter obsoletas versus excluir) não tem referência nas fontes consultadas; `replacedBy` cobre substituição, não remoção pura [F: ims2017case10].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2013provo | normativo | 2026-10-29 |
| w3c2012owl2syntax | normativo | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
