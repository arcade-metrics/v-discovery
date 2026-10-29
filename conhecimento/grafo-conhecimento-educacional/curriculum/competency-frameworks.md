---
id: kg.curr.competency-frameworks
titulo: Frameworks de competência como grafo
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [onedtech2025case, ims2017case10, esco2026what, esco2026download, credentialengine2026ctdl, mec2026bncc, w3c2009skos, w3c2013provo]
relacoes:
  - { tipo: parte-de, alvo: kg.mod.conceptual-model }
  - { tipo: depende-de, alvo: kg.std.skos }
  - { tipo: complementa, alvo: kg.curr.bncc }
  - { tipo: complementa, alvo: kg.curr.prerequisites }
  - { tipo: relacionado-a, alvo: kg.voc.case }
  - { tipo: relacionado-a, alvo: kg.voc.esco }
  - { tipo: relacionado-a, alvo: kg.eng.versioning-and-provenance }
termos: [framework de competência, concept scheme, crosswalk, alinhamento, mapeamento, versionamento de currículo, autoridade, código de habilidade]
---

# Frameworks de competência como grafo

## Definição e terminologia

Um **framework de competência** é um conjunto organizado e publicado de competências, habilidades ou padrões acadêmicos, com autoridade declarada. Exemplos verificados nesta sessão: a BNCC, que "define o conjunto orgânico e progressivo de aprendizagens essenciais que todos os alunos devem desenvolver" e tem caráter normativo [F: mec2026bncc]; a ESCO, com 3.039 ocupações e 13.939 competências [F: esco2026what]; os frameworks trocados por CASE, chamados **CASE Frameworks** [F: onedtech2025case, §1].

[I] O que torna um conjunto de competências um *framework*, e não apenas uma lista, são três propriedades: autoridade (quem o publica), identidade (códigos estáveis) e versão.

## Problema que resolve

[I] Uma instituição opera simultaneamente sob vários frameworks: o currículo nacional, o currículo próprio, o de um exame externo, eventualmente um de competências profissionais. As mesmas aulas precisam ser relatadas contra todos. Sem representação em grafo, cada par exige uma planilha de correspondência mantida à mão.

O CASE coloca o problema nestes termos: a meta é "replace the current ways of documenting a learning standard and competency, typically a PDF or HTML document, by a method that is both human and machine-readable" [F: onedtech2025case, §1].

## Fundamentos e funcionamento

### Representação

[I] A forma canônica, apoiada nas propriedades documentadas de SKOS [F: w3c2009skos]:

| Elemento do framework | Construção |
|---|---|
| o framework em si | `skos:ConceptScheme` |
| cada item | `skos:Concept` com `skos:inScheme` |
| código oficial | `skos:notation` |
| enunciado | `skos:prefLabel` |
| variantes de redação | `skos:altLabel` |
| hierarquia interna | `skos:broader`, só vínculo imediato [F: w3c2009skos, §8.1] |
| itens de topo | `skos:topConceptOf` |

### Alinhamento entre frameworks (crosswalk)

As opções, por força decrescente de compromisso [I]:

| Construção | Significado | Risco |
|---|---|---|
| `owl:sameAs` | identidade lógica; propaga todas as afirmações | quase sempre errado entre frameworks |
| `skos:exactMatch` | intercambiáveis em recuperação de informação | forte, mas sem consequência lógica |
| `skos:closeMatch` | suficientemente próximos para uso | o padrão prático |
| `skos:broadMatch`/`narrowMatch` | um cobre mais que o outro | o caso mais comum na realidade |
| CASE `exactMatchOf` | "Equivalent to. Used to connect derived CFItem to CFItem in original source CFDocument" [F: ims2017case10] | específico ao contexto de derivação |

[I] O erro recorrente é usar `exactMatch` onde a correspondência é parcial. Habilidades de frameworks diferentes raramente coincidem; `broadMatch` e `narrowMatch` descrevem melhor a realidade e preservam a informação de que a correspondência é imperfeita.

### Alinhamento é afirmação contextual

[I] Um crosswalk tem autor, data e critério. Dois especialistas produzem mapeamentos diferentes entre os mesmos frameworks, e ambos podem estar defensáveis. Portanto: alinhamentos em grafo nomeado próprio, com proveniência PROV-O [F: w3c2013provo], e nunca misturados às arestas internas do framework.

Isso também resolve o versionamento: quando o framework externo lança nova versão, o grafo de alinhamento anterior continua válido para a versão anterior e pode ser substituído sem tocar no resto. Ver kg.eng.versioning-and-provenance.

### Associações para fora

CASE 1.1 introduziu a possibilidade de `CFAssociation` apontar para frameworks não-CASE, com o campo `targetType` para orientar implementadores, mudança descrita como grande porque "it can no longer be assumed the target is a CASE object" [F: onedtech2025case].

[I] Isso é o que permite que um framework CASE aponte para um conceito de um grafo próprio ou para ESCO sem exigir que tudo seja CASE — exatamente o que um grafo de conhecimento precisa.

### Fontes de framework verificadas

| Framework | Autoridade | Formato publicado | Versão verificada |
|---|---|---|---|
| BNCC | MEC, Brasil; caráter normativo pela LDB [F: mec2026bncc] | PDF, planilha, navegação web [F: mec2026bncc] | não versionada publicamente na página consultada |
| ESCO | Comissão Europeia, DG EMPL [F: esco2026what] | RDF, TTL, ODS, CSV, XML, JSON-LD; API [F: esco2026download] | v1.2.1, release v6.0.0, 2025-12-10 [F: esco2026what] |
| CASE (como mecanismo) | 1EdTech [F: onedtech2025case] | JSON + REST | spec v1.1, 2025-01-24 [F: onedtech2025case] |
| CTDL | Credential Engine; "de facto standards" [F: credentialengine2026ctdl] | linked data | não verificada |

[I] A linha da BNCC é a mais problemática: um framework normativo nacional publicado em PDF e planilha exige que cada consumidor faça sua própria extração, e cada extração produz identificadores diferentes. Ver kg.curr.bncc.

## Requisitos e pressupostos

- Identificadores próprios para os itens do framework, mesmo quando ele publica códigos: o código é `skos:notation`, não o IRI (ver kg.found.identifiers-and-triples).
- Versão declarada de cada framework importado.
- Alinhamentos em grafos nomeados separados, com proveniência.
- Uma política para o que acontece quando um item do framework externo é retirado. [I] CASE oferece `replacedBy` para o caso de substituição [F: ims2017case10].

## Vantagens e limitações

Vantagens: um único grafo responde a vários frameworks; crosswalks viram dados consultáveis em vez de planilhas; a versão do framework externo fica registrada; relatórios de cobertura curricular ficam automáticos.

Limitações: manter crosswalks é trabalho humano contínuo; frameworks publicados em PDF exigem extração própria e frágil; e correspondências parciais, que são a maioria, não têm representação satisfatória além de `broadMatch`/`narrowMatch`. [I]

## Métricas e métodos de avaliação

[I] Cobertura de alinhamento (fração de itens do framework externo com ao menos uma correspondência); fração de correspondências `exactMatch` versus parciais; concordância entre curadores em um subconjunto; itens do currículo próprio sem ancoragem em nenhum framework oficial.

## Exemplo técnico independente de domínio

```trig
# o framework importado, com versão declarada
GRAPH ex:g/fw/oficial/2026 {
  ex:fw/oficial a skos:ConceptScheme ;
      skos:prefLabel "Framework oficial"@pt ;
      v:versaoFonte  "edição 2026" .

  ex:hab/EF05MA07 a skos:Concept ;
      skos:inScheme  ex:fw/oficial ;
      skos:notation  "EF05MA07" ;
      skos:prefLabel "Resolver e elaborar problemas envolvendo frações equivalentes"@pt ;
      skos:broader   ex:hab/unidade-numeros-5ano .
}

# o crosswalk em grafo próprio, com proveniência e critério
GRAPH ex:g/crosswalk/proprio-oficial/2026-10 {
  ex:comp/221 skos:closeMatch  ex:hab/EF05MA07 .
  ex:comp/222 skos:narrowMatch ex:hab/EF05MA07 .   # a própria é mais específica
}
ex:g/crosswalk/proprio-oficial/2026-10
    prov:wasAttributedTo ex:agente/curadoria ;
    prov:generatedAtTime "2026-10-15T00:00:00Z"^^xsd:dateTime ;
    v:criterio "correspondência de objeto de conhecimento e nível cognitivo"@pt .
```

```sparql
# cobertura: itens do framework oficial sem nenhum alinhamento
SELECT ?h ?cod WHERE {
  GRAPH ex:g/fw/oficial/2026 { ?h skos:inScheme ex:fw/oficial ; skos:notation ?cod }
  FILTER NOT EXISTS {
    GRAPH ?cw { ?x ?p ?h . FILTER (?p IN (skos:exactMatch, skos:closeMatch, skos:broadMatch, skos:narrowMatch)) }
  }
}
```

## Relações com outros conceitos

Parte de kg.mod.conceptual-model. Depende de kg.std.skos. Complementa kg.curr.bncc (um framework concreto) e kg.curr.prerequisites. Relaciona-se com kg.voc.case, kg.voc.esco e kg.eng.versioning-and-provenance.

## Lacunas e questões abertas

- Não foi localizado crosswalk publicado entre BNCC e qualquer framework internacional.
- A prática real de uso de `broadMatch`/`narrowMatch` em crosswalks educacionais não foi levantada; a recomendação é derivada da semântica documentada em SKOS [F: w3c2009skos], não de prática observada.
- Não foi verificado se alguma iniciativa publica a BNCC como CASE Framework ou como esquema SKOS.
- [H] A fração de correspondências que são exatas entre dois currículos nacionais é provavelmente pequena (abaixo de 30%), mas isso é intuição, não medição.
- O tratamento de itens retirados entre versões (`replacedBy` em CASE [F: ims2017case10]) não foi examinado em caso real.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| onedtech2025case | normativo | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
| esco2026download | fornecedor | 2026-10-29 |
| credentialengine2026ctdl | fornecedor | 2026-10-29 |
| mec2026bncc | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
