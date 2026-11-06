---
id: kg.curr.cognitive-taxonomies
titulo: Taxonomias cognitivas no grafo
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [krathwohl2002revision, ims2017case10, schemaorg2026learningresource, w3c2009skos, mec2026bnccabase]
relacoes:
  - { tipo: parte-de, alvo: kg.mod.competencies-and-objectives }
  - { tipo: depende-de, alvo: kg.std.skos }
  - { tipo: relacionado-a, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: kg.mod.conceptual-model }
  - { tipo: relacionado-a, alvo: adp.id.knowledge-components }
termos: [taxonomia cognitiva, taxonomia de Bloom, taxonomia revisada, nível cognitivo, dimensão do processo cognitivo, dimensão do conhecimento, Depth of Knowledge, hasSkillLevel, verbo de ação]
---

# Taxonomias cognitivas no grafo

## Definição e terminologia

Uma **taxonomia cognitiva** classifica o que se espera que o aluno faça com o conhecimento — lembrar, aplicar, analisar — em vez de classificar o conhecimento em si.

A referência mais citada no campo é a taxonomia de Bloom e sua revisão. Krathwohl publicou uma visão geral dessa revisão em *Theory Into Practice* 41(4), 2002, pp. 212-218 [F: krathwohl2002revision, metadados verificados via Crossref; texto integral não consultado].

O que não é: um nível cognitivo não é a dificuldade do item. Uma tarefa de "lembrar" pode ser difícil e uma de "criar" pode ser fácil. São eixos independentes. [I]

## Problema que resolve

[I] Sem nível cognitivo, o grafo trata como equivalentes objetivos que não são:

- "Lembrar a definição de fração equivalente"
- "Aplicar a identificação de frações equivalentes em um problema"
- "Criar um problema que exija frações equivalentes"

São a mesma matéria e exigências diferentes. A consequência prática: um sistema que recomenda recursos sem considerar o nível entrega material de memorização a quem precisa aplicar, e vice-versa. E um relatório de cobertura curricular que ignora o nível declara coberto um currículo que só foi coberto superficialmente.

## Fundamentos e funcionamento

### O que os padrões oferecem

- **CASE** tem `hasSkillLevel`, definida como: "The destination of this association is understood to define a given skill level i.e. Reading Lexile 100, Depth Knowledge 2, or Cognitive Level (Blooms Taxonomy) etc." [F: ims2017case10, tabela 7.3.1]. Três coisas se depreendem dessa definição: (i) o nível é o **destino de uma associação**, não um atributo literal; (ii) a taxonomia de Bloom é citada explicitamente como caso de uso; (iii) "Depth of Knowledge" e "Lexile" aparecem no mesmo mecanismo, ou seja, o padrão não privilegia uma taxonomia.
- **schema.org** tem `educationalLevel`, mas é outra coisa: "the level in terms of progression through an educational or training context", com exemplos 'beginner', 'intermediate', 'advanced' [F: schemaorg2026learningresource]. É nível de progressão, não nível cognitivo. [I] Confundir os dois é erro comum.
- **BNCC**: o documento organiza-se por competências, habilidades e objetos de conhecimento [F: mec2026bnccabase]; não foi verificado se atribui níveis cognitivos explícitos às habilidades.

### Modelagem

[I] Recomendação deste documento, seguindo o desenho que o CASE já adota:

1. A taxonomia é **vocabulário publicado**, não enumeração no código: um `skos:ConceptScheme` com seus níveis como `skos:Concept`, hierarquizados por `skos:broader` quando a taxonomia tiver estrutura [F: w3c2009skos].
2. O vínculo objetivo → nível é uma **relação**, não um literal. Isso preserva a hierarquia, permite consultar "tudo que está em nível igual ou superior a aplicar" e permite trocar de taxonomia sem reescrever os dados.
3. **Mais de uma taxonomia pode coexistir** no mesmo grafo, cada uma em seu esquema, com alinhamentos entre elas por `skos:*Match` quando defensáveis. O `hasSkillLevel` do CASE admite isso por construção, ao aceitar Lexile, DOK e Bloom no mesmo mecanismo [F: ims2017case10].

### Verbo de ação

[I] Na prática de desenho instrucional, o nível cognitivo é sinalizado pelo verbo do enunciado do objetivo. Essa correspondência verbo → nível é convenção útil e frágil: o mesmo verbo pode indicar níveis diferentes conforme o contexto da tarefa. Tratar o verbo como evidência do nível, e não como definição dele, evita classificação automática equivocada.

## Requisitos e pressupostos

- Uma taxonomia escolhida e publicada como vocabulário antes de povoar os objetivos.
- Objetivos formulados com verbo observável (ver kg.mod.competencies-and-objectives).
- Aceitação de que a classificação é interpretativa e, portanto, tem autor e data — logo, proveniência (ver kg.std.prov-o).

## Vantagens e limitações

Vantagens: distingue exigências que a matéria sozinha não distingue; permite relatório de cobertura por nível; habilita recomendação sensível ao tipo de tarefa; e o padrão de troca (CASE) já prevê o mecanismo.

Limitações: a classificação é subjetiva e varia entre classificadores; a hierarquia de níveis é discutível (nem toda taxonomia é estritamente ordenada); e há risco de sobre-modelagem — se o grafo não usa o nível em nenhuma consulta, ele é custo sem retorno. [I]

## Alternativas e comparações

| Opção | Vantagem | Limitação |
|---|---|---|
| Nível como relação a vocabulário SKOS | hierarquia consultável; múltiplas taxonomias; alinhável | mais nós |
| Nível como literal (`"aplicar"`) | simples | sem hierarquia; sem validação; sem alinhamento |
| Nível como valor numérico (DOK 1-4) | ordenação trivial | perde a semântica do nível |
| `schema:educationalLevel` | padrão existente | é progressão, não cognição [F: schemaorg2026learningresource] |
| CASE `hasSkillLevel` | padrão existente, no desenho correto | só dentro do ecossistema CASE [F: ims2017case10] |

## Exemplo técnico independente de domínio

```turtle
# a taxonomia como vocabulário: estrutura genérica, sem comprometer com os níveis
# de nenhuma taxonomia específica (os nomes abaixo são ilustrativos)
ex:tax/cognitiva a skos:ConceptScheme ;
    skos:prefLabel "Taxonomia cognitiva adotada"@pt ;
    v:fonte "referência bibliográfica da taxonomia"@pt .

ex:nivel/n1 a skos:Concept ; skos:inScheme ex:tax/cognitiva ;
    skos:prefLabel "Nível 1"@pt ; v:ordem 1 .
ex:nivel/n3 a skos:Concept ; skos:inScheme ex:tax/cognitiva ;
    skos:prefLabel "Nível 3"@pt ; v:ordem 3 .

# o objetivo aponta para o nível; a classificação tem proveniência
GRAPH ex:g/classificacao-cognitiva/2026-10 {
  ex:obj/112 v:nivelCognitivo ex:nivel/n3 .
}
ex:g/classificacao-cognitiva/2026-10 prov:wasAttributedTo ex:agente/curadoria .

# segunda taxonomia coexistindo, com alinhamento declarado
ex:dok/2 a skos:Concept ; skos:inScheme ex:tax/dok .
ex:nivel/n3 skos:closeMatch ex:dok/2 .
```

```sparql
# cobertura por nível: quantos objetivos existem em cada nível, por componente
SELECT ?componente ?nivel (COUNT(?o) AS ?n) WHERE {
  ?o v:nivelCognitivo ?nivel ; v:operacionaliza ?h .
  ?h skos:broader+ ?componente .
  ?componente a v:ComponenteCurricular .
} GROUP BY ?componente ?nivel ORDER BY ?componente ?nivel
```

[I] Essa consulta é o teste de superficialidade de um currículo implementado: se todos os objetivos de um componente caem nos níveis mais baixos, a cobertura declarada não corresponde à exigência.

## Relações com outros conceitos

Parte de kg.mod.competencies-and-objectives. Depende de kg.std.skos. Relaciona-se com iop.comp.case (`hasSkillLevel`), kg.mod.conceptual-model e, no domínio vizinho, com adp.id.knowledge-components.

## Lacunas e questões abertas

- **O texto de Krathwohl não foi consultado**; apenas os metadados via Crossref [F: krathwohl2002revision]. Por isso este documento não enumera os níveis da taxonomia revisada nem descreve suas duas dimensões: fazê-lo seria afirmar sem fonte verificada. O exemplo usa níveis genéricos por essa razão.
- Não foi verificado se existe publicação da taxonomia de Bloom revisada como vocabulário SKOS reutilizável.
- Depth of Knowledge e Lexile, citados pelo CASE [F: ims2017case10], não foram investigados.
- Não foi verificado se a BNCC atribui níveis cognitivos às habilidades.
- A confiabilidade entre classificadores ao atribuir níveis a objetivos não foi levantada na literatura.
- [H] Se o grafo não tiver consulta que use o nível cognitivo, a camada é custo sem retorno — o que torna a competency question "cobertura por nível" o teste de necessidade desta modelagem.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| krathwohl2002revision | academico | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| mec2026bnccabase | normativo | 2026-10-29 |
