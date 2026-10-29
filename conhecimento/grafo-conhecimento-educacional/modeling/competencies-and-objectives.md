---
id: kg.mod.competencies-and-objectives
titulo: Competências, habilidades e objetivos de aprendizagem
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [onedtech2025case, ims2017case10, esco2026what, credentialengine2026ctdl, mec2026bncc, krathwohl2002revision, schemaorg2026learningresource, w3c2009skos]
relacoes:
  - { tipo: parte-de, alvo: kg.mod.conceptual-model }
  - { tipo: complementa, alvo: kg.curr.cognitive-taxonomies }
  - { tipo: complementa, alvo: kg.curr.competency-frameworks }
  - { tipo: depende-de, alvo: kg.std.skos }
  - { tipo: relacionado-a, alvo: kg.voc.case }
  - { tipo: relacionado-a, alvo: adp.id.knowledge-components }
termos: [competência, habilidade, objetivo de aprendizagem, learning outcome, descritor, verbo de ação, nível cognitivo, granularidade, operacionalização]
---

# Competências, habilidades e objetivos de aprendizagem

## Definição e terminologia

Os termos são usados de forma inconsistente entre padrões e entre países. O que as fontes consultadas efetivamente dizem:

- **CASE** trata "academic learning standards, competencies, and skills" como coisas a trocar, sem distingui-las no modelo: todas são `CFItem` [F: onedtech2025case, resumo e §1].
- **ESCO** classifica "Skills, Competences and Occupations" e descreve 13.939 competências ligadas a ocupações [F: esco2026what].
- **schema.org** usa "competency or learning outcome" como alvo de `teaches` e `assesses`, e define `competencyRequired` como "Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something" [F: schemaorg2026learningresource].
- **BNCC** "estabelece conhecimentos, competências e habilidades que se espera que todos os estudantes desenvolvam ao longo da escolaridade básica" e define "o conjunto orgânico e progressivo de aprendizagens essenciais" [F: mec2026bncc].
- **CTDL** fala de "credentials, competencies, and learning and career pathways" [F: credentialengine2026ctdl].

[I] Nenhuma dessas fontes define formalmente a diferença entre competência, habilidade e objetivo. A distinção que este documento adota é operacional, não ontológica:

| Termo | Definição operacional adotada | Observável? |
|---|---|---|
| **Conceito** | unidade de conhecimento a que se pode referir | não diretamente |
| **Competência** | o que se espera que o aluno seja capaz de fazer, mobilizando conceitos | só por desempenho |
| **Habilidade** | competência tal como enunciada por um framework oficial, com código | idem |
| **Objetivo de aprendizagem** | formulação operacional, com verbo de ação e nível cognitivo, usada para desenhar atividade e avaliação | sim, por construção |

O critério que separa competência de objetivo: **um objetivo diz como se verifica que foi atingido**. [I] "Compreender frações equivalentes" é competência mal formulada como objetivo, porque "compreender" não especifica observável; "identificar frações equivalentes a uma fração dada" é objetivo.

## Problema que resolve

[I] Três problemas concretos:

1. **Granularidade.** Uma habilidade da BNCC é larga demais para adaptação (um sistema não adapta em cima de "EF05MA07"); um knowledge component é fino demais para currículo. Sem camadas explícitas, a equipe oscila entre as duas e o grafo fica inconsistente.
2. **Rastreabilidade ao currículo oficial.** Se o objetivo operacional não aponta para a habilidade oficial, não há como relatar cobertura curricular.
3. **Nível cognitivo.** "Lembrar frações equivalentes" e "criar problemas com frações equivalentes" são a mesma matéria e requisitos diferentes. Sem o nível, o grafo os trata como iguais.

## Fundamentos e funcionamento

### A cadeia de granularidade

[I] Proposta deste documento:

```
Framework oficial              BNCC: habilidade EF05MA07 (código, enunciado)
        ↓ operacionaliza
Objetivo de aprendizagem       verbo + objeto + condição + nível cognitivo
        ↓ mobiliza
Conceito / knowledge component unidade inferível do desempenho
        ↓ avaliado por
Item                           unidade avaliativa
```

A relação `operacionaliza` é de muitos para um: várias formulações operacionais para uma habilidade oficial. A relação `mobiliza` é de muitos para muitos.

A camada de baixo é a que o domínio vizinho trata: um *knowledge component* é "uma unidade adquirida de função ou estrutura cognitiva que pode ser inferida a partir do desempenho em um conjunto de tarefas relacionadas" (adp.id.knowledge-components). [I] Isso dá o critério de granularidade do nível mais fino: um conceito é fino o bastante quando o desempenho em tarefas relacionadas permite inferi-lo separadamente.

### Verbo e nível cognitivo

Krathwohl descreve a revisão da taxonomia de Bloom [F: krathwohl2002revision, metadados verificados via Crossref; texto integral não consultado]. Ver kg.curr.cognitive-taxonomies para o que a taxonomia revisada propõe.

O CASE oferece `hasSkillLevel`, cuja definição normativa cita explicitamente "Cognitive Level (Blooms Taxonomy)" entre os exemplos de nível que o destino da associação pode definir [F: ims2017case10, tabela 7.3.1]. [I] Ou seja: o padrão já prevê ligar item de framework a nível cognitivo por associação, e não por atributo — o que preserva a hierarquia da taxonomia.

### Modelagem

[I] Recomendação deste documento:

- `Competencia` e `Habilidade` como `skos:Concept` em esquemas distintos (`skos:ConceptScheme` por framework), ligadas por `skos:exactMatch` ou `skos:closeMatch` quando uma é o espelho da outra em outro framework [F: w3c2009skos].
- `ObjetivoDeAprendizagem` como classe própria, porque tem estrutura interna (verbo, objeto, condição) que `skos:Concept` não comporta.
- `nivelCognitivo` como relação para um conceito de uma taxonomia publicada como esquema SKOS, não como literal.
- `operacionaliza` e `mobiliza` como propriedades próprias.

## Requisitos e pressupostos

- Um framework oficial a que ancorar; sem ele, a camada "habilidade" não existe e a cadeia tem três níveis.
- Uma taxonomia cognitiva adotada e publicada como vocabulário (ver kg.curr.cognitive-taxonomies).
- Disciplina de formulação: objetivos sem verbo observável quebram a função da camada. [I]

## Vantagens e limitações

Vantagens: separa o que o currículo oficial exige do que o sistema precisa para adaptar; mantém rastreabilidade para relatório de cobertura; o nível cognitivo deixa de ser texto livre; a camada de conceito conecta com a modelagem de aluno do domínio vizinho.

Limitações: quatro níveis são muito para currículos pequenos; `operacionaliza` e `mobiliza` precisam de manutenção ativa; não há padrão que valide essa cadeia, logo o alinhamento depende de curadoria; e a distinção competência/habilidade é nomenclatura brasileira — outros contextos usam "standard", "learning outcome" ou "competency" sem a mesma divisão. [I]

## Alternativas e comparações

| Arranjo | Níveis | Quando serve |
|---|---|---|
| Só habilidade oficial | 1 | relatório de cobertura curricular; insuficiente para adaptação |
| Habilidade + conceito | 2 | adaptação simples, sem desenho instrucional explícito |
| Habilidade + objetivo + conceito | 3 | o proposto aqui, sem a camada de framework múltiplo |
| Framework + habilidade + objetivo + conceito | 4 | quando há mais de um framework a atender (nacional, institucional, internacional) |

[I] Tabela proposta por este documento.

## Exemplo técnico independente de domínio

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ex:   <https://example.org/id/> .
@prefix v:    <https://example.org/voc/> .

# habilidade oficial, como vem do framework
ex:hab/EF05MA07 a skos:Concept ;
    skos:inScheme  ex:fw/oficial ;
    skos:notation  "EF05MA07" ;
    skos:prefLabel "Resolver e elaborar problemas envolvendo frações equivalentes"@pt .

# objetivo operacional, com estrutura interna
ex:obj/112 a v:ObjetivoDeAprendizagem ;
    v:verbo           ex:bloom/aplicar ;
    v:enunciado       "Identificar, entre quatro frações dadas, as equivalentes a uma fração de referência"@pt ;
    v:condicao        "sem calculadora, denominadores até 24"@pt ;
    v:nivelCognitivo  ex:bloom/aplicar ;
    v:operacionaliza  ex:hab/EF05MA07 ;
    v:mobiliza        ex:c/8f3a , ex:c/multiplicacao .

# a taxonomia é vocabulário, não literal
ex:bloom/aplicar a skos:Concept ;
    skos:inScheme  ex:tax/bloom-revisada ;
    skos:prefLabel "Aplicar"@pt ;
    skos:broader   ex:bloom/processo-cognitivo .
```

```sparql
# cobertura: habilidades oficiais sem nenhum objetivo que as operacionalize
SELECT ?h WHERE {
  ?h skos:inScheme ex:fw/oficial .
  FILTER NOT EXISTS { ?o v:operacionaliza ?h }
}
```

## Relações com outros conceitos

Parte de kg.mod.conceptual-model. Complementa kg.curr.cognitive-taxonomies e kg.curr.competency-frameworks. Depende de kg.std.skos. Relaciona-se com kg.voc.case (`hasSkillLevel`, `CFItem`) e, no domínio vizinho, com adp.id.knowledge-components (a granularidade do nível mais fino).

## Lacunas e questões abertas

- As definições de competência, habilidade e objetivo adotadas aqui são operacionais e propostas por este documento; nenhuma fonte consultada as define formalmente.
- O texto de Krathwohl não foi consultado; só os metadados via Crossref [F: krathwohl2002revision].
- Não foi verificado se existe publicação da taxonomia de Bloom revisada como vocabulário SKOS reutilizável.
- [H] A quantidade certa de objetivos por habilidade oficial é desconhecida; a suspeita é que fique entre 3 e 10 para habilidades de currículo nacional, mas não há medição.
- Como tratar competências socioemocionais, que a BNCC inclui entre as competências gerais [F: mec2026bncc], não foi examinado: elas não se decompõem em conceitos da mesma forma.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| onedtech2025case | normativo | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
| credentialengine2026ctdl | fornecedor | 2026-10-29 |
| mec2026bncc | normativo | 2026-10-29 |
| krathwohl2002revision | academico | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
