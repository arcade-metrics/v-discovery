---
id: kg.mod.conceptual-model
titulo: Modelo conceitual do grafo educacional
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [noy2001ontology101, w3c2009skos, onedtech2025case, ims2017case10, schemaorg2026learningresource, ieee2020lom, zhao2022edukg, alatrash2025prerequisite, hogan2021knowledgegraphs]
relacoes:
  - { tipo: depende-de, alvo: kg.found.ontologies }
  - { tipo: complementa, alvo: kg.mod.layer-separation }
  - { tipo: complementa, alvo: kg.mod.competencies-and-objectives }
  - { tipo: complementa, alvo: kg.mod.evidence-and-mastery }
  - { tipo: depende-de, alvo: kg.voc.comparison }
  - { tipo: relacionado-a, alvo: kg.curr.prerequisites }
  - { tipo: relacionado-a, alvo: kg.std.comparison }
  - { tipo: relacionado-a, alvo: adp.id.knowledge-components }
termos: [modelo conceitual, conceito, competência, habilidade, objetivo de aprendizagem, recurso, instrumento, item, evidência, alinhamento, competency question]
---

# Modelo conceitual do grafo educacional

## Definição e terminologia

Este documento propõe o conjunto mínimo de classes e relações de um grafo conceitual educacional (camada 1 de kg.mod.layer-separation) e diz, para cada uma, de onde vem: vocabulário reusado ou vocabulário próprio.

É proposta, não padrão. Noy e McGuinness são explícitos: "there is no one correct way to model a domain — there are always viable alternatives. The best solution almost always depends on the application that you have in mind and the extensions that you anticipate" [F: noy2001ontology101, §3]. O que segue vale para o perfil de uso descrito nas competency questions abaixo.

## Problema que resolve

[I] Equipes educacionais usam "competência", "habilidade", "objetivo", "descritor", "conteúdo" e "tópico" de forma intercambiável. Um grafo obriga a decidir — e a decisão, se não for tomada explicitamente, é tomada por acidente na primeira tabela do banco.

## Fundamentos e funcionamento

### Competency questions

Noy e McGuinness recomendam esboçar as perguntas que a base deve responder; elas "serve as the litmus test later" [F: noy2001ontology101, §3, Step 1]. As deste modelo [I]:

1. O que um aluno precisa saber antes de estudar o conceito X?
2. Que recursos ensinam o conceito X? Quais o avaliam?
3. Que habilidades do currículo oficial um recurso cobre?
4. Que conceitos do currículo não têm nenhum recurso nem instrumento associado?
5. Dado que um aluno errou um item, que conceitos podem estar em falta?
6. Que caminho mínimo de conceitos leva do estado atual de um aluno até um objetivo?
7. Quem afirmou que o conceito X é pré-requisito de Y, quando e com que confiança?
8. Como a versão 3 do currículo difere da versão 2 em termos de conceitos e relações?

[I] As perguntas 1 a 4 são respondidas pela camada 1 sozinha. As 5 e 6 exigem as camadas 2 e 3. A 7 exige proveniência. A 8 exige versionamento. Isso já determina a maior parte do modelo.

### Classes

| Classe | Papel | Vocabulário |
|---|---|---|
| `Conceito` | unidade de conhecimento referenciável | `skos:Concept` [F: w3c2009skos] |
| `Competencia` | o que se espera que o aluno seja capaz de fazer | `skos:Concept` em esquema próprio; CASE `CFItem` na troca [F: onedtech2025case] |
| `ObjetivoDeAprendizagem` | formulação operacional de uma competência, com verbo e nível | próprio; ver kg.mod.competencies-and-objectives |
| `FrameworkCurricular` | o conjunto oficial (BNCC, um curso) | `skos:ConceptScheme`; CASE `CFDocument` [F: onedtech2025case] |
| `Recurso` | material que ensina | `schema:LearningResource` [F: schemaorg2026learningresource]; LOM onde já adotado [F: ieee2020lom] |
| `Instrumento` | o que avalia (prova, atividade, tarefa) | próprio |
| `Item` | unidade avaliativa dentro de um instrumento | próprio |
| `Evidencia` | observação que informa sobre domínio | próprio; ver kg.mod.evidence-and-mastery |

[I] `Conceito` e `Competencia` são distintos de propósito: "frações equivalentes" é conceito; "resolver problemas envolvendo frações equivalentes" é competência. A mesma competência mobiliza vários conceitos; o mesmo conceito aparece em várias competências. Fundir as duas simplifica o modelo e destrói a pergunta 5.

A correspondência com o domínio vizinho: o *knowledge component* de adp.id.knowledge-components é definido como "uma unidade adquirida de função ou estrutura cognitiva que pode ser inferida a partir do desempenho em um conjunto de tarefas relacionadas". [I] É o `Conceito` deste modelo quando visto do lado da modelagem do aluno — mesma entidade, dois usos.

### Relações

| Relação | Domínio → Contradomínio | Vocabulário |
|---|---|---|
| `broader` | Conceito → Conceito | `skos:broader`, só vínculo imediato [F: w3c2009skos, §8.1] |
| `preRequisitoDe` | Conceito → Conceito | **próprio**; nenhum padrão consultado cobre bem [I] |
| `mobiliza` | Competência → Conceito | próprio |
| `ensina` | Recurso → Conceito/Competência | `schema:teaches` [F: schemaorg2026learningresource] |
| `avalia` | Item/Instrumento → Conceito/Competência | `schema:assesses` [F: schemaorg2026learningresource] |
| `exige` | Recurso → Competência | `schema:competencyRequired` [F: schemaorg2026learningresource] |
| `alinhadoA` | Conceito próprio → item de framework externo | `skos:closeMatch` / `skos:exactMatch` [F: w3c2009skos] |
| `pertenceA` | Conceito → FrameworkCurricular | `skos:inScheme` [F: w3c2009skos] |
| `nivelCognitivo` | Competência → nível de taxonomia | próprio; CASE tem `hasSkillLevel` [F: ims2017case10] |

**O que precisa ser criado é pequeno**: `preRequisitoDe`, `mobiliza`, `nivelCognitivo`, mais as classes `Instrumento`, `Item` e `Evidencia`. Todo o resto se reusa. [I] Essa é a conclusão operacional de kg.voc.comparison.

### Escala esperada

O EDUKG, grafo de K-12, declara ontologia com 635 classes, 445 propriedades de objeto e 1.314 propriedades de tipo de dado [F: zhao2022edukg, resumo]. [I] Isso é uma ordem de grandeza acima do modelo proposto aqui, e a diferença é de propósito: EDUKG modela o conteúdo das disciplinas (as entidades de física, de história); este modelo fica na camada de estrutura curricular, deixando o conteúdo disciplinar como conceitos sem ontologia própria. Qual dos dois recortes serve depende das competency questions.

## Requisitos e pressupostos

- Identificadores estáveis (kg.found.identifiers-and-triples).
- As três camadas separadas (kg.mod.layer-separation); este modelo cobre só a primeira.
- Proveniência por lote de curadoria (kg.std.prov-o), exigida pela competency question 7.
- Versionamento do framework curricular (kg.eng.versioning-and-provenance), exigido pela 8.

## Vantagens e limitações

Vantagens: enxuto; reusa o que existe; as distinções que mantém (conceito × competência, recurso × instrumento) são as que as competency questions exigem; cabe em SKOS mais um punhado de propriedades próprias, portanto adota-se sem raciocinador.

Limitações: não cobre conteúdo disciplinar; não modela currículo como sequência temporal (ano, bimestre) — isso exigiria mais classes; não trata de turma, professor nem contexto institucional; e a decisão de não fundir conceito e competência cobra o preço de manter `mobiliza` atualizada. [I]

## Alternativas e comparações

| Decisão | Alternativa | Consequência |
|---|---|---|
| Conceito ≠ Competência | fundir em uma só classe | modelo menor; perde a pergunta 5 e o diagnóstico por conceito |
| Pré-requisito como propriedade própria | usar `skos:related` | choca com a disjunção §8.6.10 de SKOS [F: w3c2009skos] |
| Pré-requisito como propriedade própria | usar CASE `precedes` | `precedes` significa só "comes before ... in time or order" [F: ims2017case10] |
| Recurso ≠ Instrumento | tratar instrumento como recurso | `teaches` e `assesses` ficam no mesmo nó; perde a distinção de função |
| Nível cognitivo como relação | como atributo literal | perde a hierarquia da taxonomia; ver kg.curr.cognitive-taxonomies |

## Exemplo técnico independente de domínio

```turtle
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix schema: <https://schema.org/> .
@prefix ex:     <https://example.org/id/> .
@prefix v:      <https://example.org/voc/> .

# framework e conceitos
ex:fw/curriculo-v3 a skos:ConceptScheme .

ex:c/8f3a a skos:Concept ;
    skos:inScheme  ex:fw/curriculo-v3 ;
    skos:prefLabel "Frações equivalentes"@pt ;
    skos:broader   ex:c/numeros-racionais ;
    v:preRequisitoDe ex:c/1b2c .

# competência: mobiliza conceitos, tem nível cognitivo
ex:comp/221 a v:Competencia ;
    skos:prefLabel "Resolver problemas com frações equivalentes"@pt ;
    v:mobiliza     ex:c/8f3a , ex:c/divisao ;
    v:nivelCognitivo ex:bloom/aplicar ;
    skos:exactMatch <https://externo.example/framework/EF05MA07> .

# recurso ensina; item avalia
ex:r/4412  a schema:LearningResource ; schema:teaches  ex:c/8f3a .
ex:item/77 a v:Item                  ; schema:assesses ex:comp/221 ;
           v:pertenceAInstrumento ex:inst/prova-diagnostica-1 .
```

```sparql
# competency question 4: conceitos sem recurso nem item
SELECT ?c WHERE {
  ?c a skos:Concept ; skos:inScheme ex:fw/curriculo-v3 .
  FILTER NOT EXISTS { ?r schema:teaches  ?c }
  FILTER NOT EXISTS { ?comp v:mobiliza ?c . ?i schema:assesses ?comp }
}
```

## Relações com outros conceitos

Depende de kg.found.ontologies e de kg.voc.comparison (o que reusar). Complementa kg.mod.layer-separation (este é o detalhe da camada 1), kg.mod.competencies-and-objectives e kg.mod.evidence-and-mastery. Relaciona-se com kg.curr.prerequisites, kg.std.comparison e, no domínio vizinho, com adp.id.knowledge-components.

## Lacunas e questões abertas

- O modelo é proposta deste domínio, não validado contra implementação. As competency questions não foram testadas contra um grafo real.
- Não foi verificado se existe ontologia educacional publicada que já cubra esse recorte; EDUKG foi consultado só pelo resumo [F: zhao2022edukg].
- Turma, professor, sequência didática e contexto institucional ficaram fora e podem ser necessários.
- [H] Modelar `Competencia` como `skos:Concept` em esquema separado (em vez de classe própria) manteria tudo em SKOS e simplificaria a adoção, ao custo de perder a distinção de tipo na consulta. A escolha não foi testada.
- Como representar a progressão por ano/série sem explodir o número de conceitos continua aberto; ver kg.curr.prerequisites.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| noy2001ontology101 | academico | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| ieee2020lom | normativo | 2026-10-29 |
| zhao2022edukg | academico | 2026-10-29 |
| alatrash2025prerequisite | academico | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
