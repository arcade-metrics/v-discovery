---
id: kg.eng.methodologies
titulo: Metodologias de construção de ontologia
tipo: tecnica
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [noy2001ontology101, suarez2011neon, guarino2009ontoclean, hogan2021knowledgegraphs, zhao2022edukg, ain2025topdown]
relacoes:
  - { tipo: depende-de, alvo: kg.found.ontologies }
  - { tipo: complementa, alvo: kg.eng.quality }
  - { tipo: complementa, alvo: kg.eng.construction }
  - { tipo: relacionado-a, alvo: kg.mod.conceptual-model }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [metodologia, competency question, reuso de ontologia, desenvolvimento iterativo, NeOn, OntoClean, Ontology Development 101, escopo, classe, slot, facet, instância]
---

# Metodologias de construção de ontologia

## Definição e terminologia

Uma metodologia de ontologia prescreve a sequência de atividades para ir de um domínio a um artefato formal. A referência mais difundida é o guia de Noy e McGuinness, que apresenta "one possible process", advertindo que "there is no one 'correct' way or methodology for developing ontologies" [F: noy2001ontology101, §3].

## Fundamentos e funcionamento

### Os sete passos de Ontology 101

[F: noy2001ontology101, §3]:

| Passo | Atividade |
|---|---|
| 1 | Determinar o domínio e o escopo da ontologia |
| 2 | Considerar o reuso de ontologias existentes |
| 3 | Enumerar os termos importantes da ontologia |
| 4 | Definir as classes e a hierarquia de classes |
| 5 | Definir as propriedades das classes (*slots*) |
| 6 | Definir as *facets* dos slots |
| 7 | Criar instâncias |

**Passo 1.** As perguntas básicas: qual é o domínio que a ontologia cobrirá; para que será usada; para que tipos de perguntas a informação deve fornecer respostas; quem usará e manterá. As respostas "may change during the ontology-design process, but at any given time they help limit the scope of the model" [F: noy2001ontology101, §3, Step 1].

As **competency questions** são a ferramenta central desse passo, atribuídas por Noy e McGuinness a Gruninger e Fox (1995): esboçar as perguntas que a base deveria conseguir responder. "These questions will serve as the litmus test later: Does the ontology contain enough information to answer these types of questions? Do the answers require a particular level of detail or representation of a particular area? These competency questions are just a sketch and do not need to be exhaustive" [F: noy2001ontology101, §3, Step 1].

**Passo 2.** "It is almost always worth considering what someone else has done and checking if we can refine and extend existing sources for our particular domain and task. Reusing existing ontologies may be a requirement if our system needs to interact with other applications that have already committed to particular ontologies or controlled vocabularies" [F: noy2001ontology101, §3, Step 2]. Ver kg.voc.comparison.

**Passo 3.** Na seleção dos termos, convém escolher "the terms that describe objects having independent existence rather than" os que descrevem outra coisa [F: noy2001ontology101, §3, Step 4 referindo-se ao Step 3]. [I] É o critério que separa `Conceito` (existe por si) de `nivelCognitivo` (é propriedade de algo).

### As três regras fundamentais

[F: noy2001ontology101, §3]:

1. "There is no one correct way to model a domain — there are always viable alternatives. The best solution almost always depends on the application that you have in mind and the extensions that you anticipate."
2. "Ontology development is necessarily an iterative process."
3. "Concepts in the ontology should be close to objects (physical or logical) and relationships in your domain of interest. These are most likely to be nouns (objects) or verbs (relationships) in sentences that describe your domain."

Sobre a iteração: "After we define an initial version of the ontology, we can evaluate and debug it by using it in applications or problem-solving methods or by discussing it with experts in the field, or both. As a result, we will almost certainly need to revise the initial ontology. This process of iterative design will likely continue through the entire lifecycle of the ontology" [F: noy2001ontology101, §3].

[I] A consequência operacional é que o processo de construção precisa de versionamento desde o primeiro dia, não a partir da "versão final" — ver kg.eng.versioning-and-provenance.

### Outras metodologias

- **NeOn**: metodologia para engenharia de ontologias em rede, publicada por Suárez-Figueroa, Gómez-Pérez e Fernández-López em *Ontology Engineering in a Networked World* (2011), pp. 9-34 [F: suarez2011neon, metadados verificados via Crossref; texto integral não consultado].
- **OntoClean**: análise formal de decisões ontológicas; Guarino e Welty publicaram visão geral em *Handbook on Ontologies* (2009), pp. 201-220 [F: guarino2009ontoclean, metadados verificados via Crossref; texto integral não consultado]. Ver kg.eng.quality.

[I] Nenhuma das duas pôde ser lida nesta sessão; são registradas aqui como ponteiros, não como fonte de prescrição.

### Metodologia aplicada em grafo educacional

O EDUKG declara ter desenhado "an interdisciplinary and fine-grained ontology for uniformly modeling knowledge and resource in K-12 education", com 635 classes, 445 propriedades de objeto e 1.314 propriedades de tipo de dado, e, guiada por essa ontologia, uma "flexible methodology for interactively extracting factual knowledge from textbooks" [F: zhao2022edukg, resumo].

[I] A ordem importa: a ontologia primeiro, a extração guiada por ela. É o inverso do que acontece quando se começa pelos dados.

## Requisitos e pressupostos

- Competency questions escritas antes de modelar. Sem elas não há critério para escolher entre alternativas [F: noy2001ontology101, §3, Step 1].
- Um inventário do que já existe, antes de criar (passo 2).
- Disposição para revisar: o processo é iterativo por natureza [F: noy2001ontology101, §3].
- Acesso a especialistas de domínio para avaliar e depurar [F: noy2001ontology101, §3].

## Vantagens e limitações

Vantagens: o processo de sete passos é simples, verificável e publicado; as competency questions dão critério de parada e de aceitação; o passo de reuso evita trabalho duplicado.

Limitações: o guia é de 2001 e precede a prática atual de grafos construídos por extração automática; não trata de versionamento, proveniência nem validação, que hoje são centrais; e não oferece critério para decidir granularidade. [I]

## Alternativas e comparações

| Abordagem | Ponto de partida | Quando serve |
|---|---|---|
| Top-down, guiada por ontologia | competency questions e esquema | domínio conhecido, currículo existente |
| Bottom-up, a partir dos materiais | extração de conceitos do texto | corpus grande, domínio aberto |
| Híbrida com humano no circuito | ambos, com revisão | ver kg.eng.construction |

Ain et al. compararam abordagens top-down e bottom-up para construção automática de grafos educacionais; ver kg.eng.construction para o que reportam [F: ain2025topdown].

## Exemplo técnico independente de domínio

```
# os sete passos aplicados, com os artefatos de cada um
1. escopo          -> lista de competency questions (ver kg.mod.conceptual-model)
2. reuso           -> tabela de cobertura de vocabulários (ver kg.voc.comparison)
3. termos          -> glossário do domínio
4. classes         -> hierarquia de classes, só substantivos com existência própria
5. propriedades    -> relações tipadas, com domínio e contradomínio
6. facets          -> restrições: cardinalidade, tipo, valores permitidos -> SHACL
7. instâncias      -> povoamento (ver kg.eng.construction)

# critério de parada do passo 1: cada competency question tem consulta escrita
# que o esquema do passo 5 permite executar
```

[I] O passo 6 merece nota: o que Noy e McGuinness chamam de *facets* dos slots — tipo de valor, cardinalidade, valores permitidos — hoje se expressa melhor em SHACL do que em OWL, pela razão discutida em kg.std.shacl.

## Relações com outros conceitos

Depende de kg.found.ontologies. Complementa kg.eng.quality (os critérios de aceitação) e kg.eng.construction (o povoamento). Relaciona-se com kg.mod.conceptual-model (o resultado da aplicação desta metodologia neste domínio) e kg.voc.comparison (o passo 2).

## Lacunas e questões abertas

- NeOn e OntoClean foram verificados apenas por metadados [F: suarez2011neon; guarino2009ontoclean]; suas prescrições não puderam ser descritas.
- Ontology 101 é de 2001 e não cobre proveniência, versionamento, validação por SHACL nem construção assistida por modelos de linguagem.
- Não há, nas fontes consultadas, metodologia específica para ontologias educacionais; EDUKG descreve a sua, mas foi lido só pelo resumo [F: zhao2022edukg].
- [H] Para um grafo curricular, as competency questions parecem estabilizar rápido (menos de dez perguntas cobrem o uso), o que tornaria o passo 1 barato; não verificado.
- Como decidir granularidade continua sem critério metodológico; o critério operacional proposto em kg.mod.competencies-and-objectives (inferibilidade a partir do desempenho) vem do domínio vizinho, não desta literatura.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| noy2001ontology101 | academico | 2026-10-29 |
| suarez2011neon | academico | 2026-10-29 |
| guarino2009ontoclean | academico | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| zhao2022edukg | academico | 2026-10-29 |
| ain2025topdown | academico | 2026-10-29 |
