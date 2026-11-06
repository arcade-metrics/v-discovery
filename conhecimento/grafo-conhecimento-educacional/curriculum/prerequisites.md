---
id: kg.curr.prerequisites
titulo: Pré-requisitos e progressões de aprendizagem
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [alatrash2025prerequisite, liang2015prerequisite, ims2017case10, w3c2009skos, w3c2017shacl, w3c2013sparql11query, hogan2021knowledgegraphs, mec2026bncc]
relacoes:
  - { tipo: parte-de, alvo: kg.mod.conceptual-model }
  - { tipo: depende-de, alvo: kg.found.reasoning }
  - { tipo: complementa, alvo: kg.curr.competency-frameworks }
  - { tipo: avaliado-por, alvo: kg.std.shacl }
  - { tipo: relacionado-a, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: kg.eng.construction }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
termos: [pré-requisito, prerequisite relation, progressão, sequência, DAG, aciclicidade, fecho transitivo, RefD, inferência de pré-requisito, ordem de apresentação]
---

# Pré-requisitos e progressões de aprendizagem

## Definição e terminologia

Uma **relação de pré-requisito** (PR) entre conceitos afirma que um deve ser aprendido antes do outro. Alatrash et al. a descrevem como crítica em grafos educacionais, por definir "the logical order in which concepts should be learned" [F: alatrash2025prerequisite, resumo].

Três coisas distintas são frequentemente confundidas [I]:

| Relação | Afirma | Exemplo |
|---|---|---|
| **Ordem de apresentação** | que um vem antes no material | capítulo 3 antes do 4 |
| **Pré-requisito pedagógico** | que sem um, o outro não se aprende | divisão antes de fração equivalente |
| **Hierarquia conceitual** | que um é mais geral que o outro | números racionais contém frações |

Só a segunda tem valor diagnóstico. A primeira é contingente à edição do material; a terceira é `skos:broader` (ver kg.std.skos).

## Problema que resolve

[I] Três usos, em ordem de valor:

1. **Diagnóstico**: se o aluno falha em X, o grafo diz o que verificar antes.
2. **Sequenciamento**: que conceitos estão disponíveis dado o estado atual (ver adp.adapt.sequencing-policies).
3. **Detecção de lacuna curricular**: conceitos que ninguém precede, ou que precedem nada, são suspeitos.

## Fundamentos e funcionamento

### O que os padrões oferecem

**Pouco.** [I] Nenhum dos vocabulários consultados tem uma relação de pré-requisito pedagógico bem definida:

- **CASE**: `precedes` é definida como "the origin of the association comes before the destination of the association in time or order" [F: ims2017case10, tabela 7.3.1]. É ordem, não dependência.
- **SKOS**: `skos:broader` é hierárquico; `skos:related` é associativo, e as duas categorias são tratadas como "fundamentally distinct in nature", com choque entre elas inconsistente com o modelo de dados [F: w3c2009skos, §8.6.10]. Nenhuma serve.
- **schema.org**: `competencyRequired` descreve o que deve ser demonstrado "in order to do something such as ... understand a LearningResource" — é do recurso para a competência, não entre conceitos.

Conclusão operacional: **pré-requisito é propriedade própria**. Ver kg.mod.conceptual-model.

### Propriedades estruturais

[I] Um conjunto de relações de pré-requisito forma, idealmente, um grafo acíclico dirigido (DAG). A literatura trata a aciclicidade como pressuposto declarado (ver abaixo), mas ela **não é garantida** por nenhum padrão:

- SKOS aceita ciclos explicitamente: "there is no condition requiring that `skos:broaderTransitive` be irreflexive" [F: w3c2009skos, §8.6.8].
- RDF não impõe nenhuma restrição estrutural [F: hogan2021knowledgegraphs].

Portanto aciclicidade é regra a validar, não propriedade herdada. Como está fora do núcleo do SHACL, exige SHACL-SPARQL [F: w3c2017shacl, §5] — o exemplo está em kg.std.shacl.

### Afirmado e derivado

Convém seguir o padrão que SKOS estabelece para hierarquia: propriedades distintas para o vínculo imediato e para o fecho. SKOS afirma só o vínculo direto com `skos:broader`, deixando `skos:broaderTransitive` para inferir o fecho, e por convenção esta última não é usada para asserções [F: w3c2009skos, §8.1].

[I] Aplicado a pré-requisitos: afirmar `preRequisitoDe` só entre vizinhos; obter o fecho por property path em SPARQL (`preRequisitoDe+` [F: w3c2013sparql11query, §9.4]) ou materializá-lo em `preRequisitoDeTransitivo`, em grafo nomeado separado. Ver kg.found.reasoning.

### Força e confiança

[I] Pré-requisito não é binário. "Divisão é pré-requisito de fração equivalente" é quase absoluto; "proporção é pré-requisito de escala" é tendência. Se o grafo pretende usar pré-requisitos para diagnóstico, precisa de força — e uma aresta com atributo é o problema de kg.found.context-and-reification.

Isso é reforçado pela origem dos dados: quando as relações são inferidas automaticamente (ver abaixo), vêm com confiança por construção.

### Três pressupostos estruturais

Alatrash et al. adotam explicitamente três pressupostos centrais, citando literatura anterior [F: alatrash2025prerequisite, §3]:

- **Transitividade**: se A é pré-requisito de B e B de C, então A é pré-requisito de C.
- **Assimetria**: se B precede A, então A não precede B.
- **Sem autoconexão**: "a concept cannot be a prerequisite of itself".

[I] Os dois últimos juntos implicam aciclicidade — e confirmam que ela é pressuposto declarado do modelo, não propriedade herdada do formalismo. Quem representa pré-requisitos em SKOS ou RDF precisa impô-la por validação.

### Inferência automática

A anotação manual é descrita como "time-consuming and inconsistent" [F: alatrash2025prerequisite, resumo]. Daí a linha de pesquisa em inferência automática.

Alatrash et al. propõem um método não supervisionado, sem dados rotulados: dez critérios em cinco categorias, combinados por um algoritmo de votação com limiar [F: alatrash2025prerequisite, §3, tabela 1]:

| Categoria | Critério | O que afirma |
|---|---|---|
| Documento | TemO (temporal order) | c1 precede c2 no material ou canal |
| Hyperlinks Wikipédia | HL-A | o hyperlink de c1 é mencionado no artigo de c2 |
| Hyperlinks Wikipédia | HL-Ab | o hyperlink de c1 aparece no resumo de c2 |
| Grafo | HL-RCA | o hyperlink de c1 está no resumo de um conceito relacionado a c2 |
| Grafo | RefD (reference distance) | o hyperlink de c1 é mencionado nos conceitos relacionados de c2 |
| Grafo | IOLR | c1 tem razão maior de links de entrada e saída apontando para c2 |
| Hierarquia | CatCon | c1 é uma categoria de c2 na hierarquia da DBpedia |
| Hierarquia | SuperCatCon | c1 é supercategoria de c2 na DBpedia |
| Hierarquia | CMH | a primeira ocorrência de c1 precede a de c2 entre canais |
| Texto | BERTropy | c1 tem entropia de tópico maior que c2 |

**Resultados, com a ressalva necessária.** O resumo afirma "higher precision than existing methods". A tabela 4 do próprio artigo qualifica bastante essa afirmação, comparando o algoritmo de votação a seis linhas de base sobre o conjunto AL-CPL [F: alatrash2025prerequisite, tabela 4]:

| Método | Data Mining (P / R / F1) | Physics (P / R / F1) | Macroeconomics (P / R / F1) |
|---|---|---|---|
| Votação (proposto) | **1,00** / 0,27 / 0,42 | 0,76 / 0,13 / 0,22 | 0,65 / 0,16 / 0,25 |
| RefD | 0,51 / 0,76 / 0,61 | 0,49 / 0,49 / 0,49 | — |
| Active Learning | 0,80 / 0,73 / 0,76 | 0,80 / 0,60 / 0,70 | — |
| Bagging-based AdaBoost | 0,85 / 0,85 / 0,85 | **0,87** / 0,87 / 0,86 | — |
| WikiCPRL | 0,59 / 0,90 / 0,68 | 0,43 / 0,83 / 0,57 | — |
| Neural Network | 0,62 / 0,68 / 0,65 | 0,53 / 0,62 / 0,57 | — |
| Linguistically-Driven Strategy | 0,81 / 0,81 / 0,81 | 0,77 / 0,71 / 0,74 | — |

[I] Lendo honestamente: a precisão do método proposto supera todas as linhas de base **apenas em Data Mining**; em Physics o AdaBoost tem precisão maior (0,87 contra 0,76). E o recall é drasticamente menor em todos os domínios (0,13 a 0,27, contra 0,49 a 0,90 das linhas de base), com F1 correspondentemente pior. A afirmação do resumo é mais forte do que a tabela sustenta.

Os autores explicitam o trade-off e o justificam: "we prioritize precision because minimizing false positives is more critical than capturing all possible PRs. Incorrect prerequisite suggestions could negatively affect learning paths and curriculum design"; e "in educational settings, misleading a learner with an incorrect prerequisite (false positive) is more harmful than omitting some prerequisites" [F: alatrash2025prerequisite, §4].

[I] A justificativa é correta e vale como princípio de projeto. Mas um método com recall de 0,13 em Physics encontra pouco mais de um em cada dez pré-requisitos existentes: serve para semear uma curadoria, não para povoar um grafo sozinho.

Sobre limiares: a precisão do algoritmo de votação chega a 1,0 com limiar θ = 0,28 no conjunto usado; para o critério RefD isoladamente, a precisão atinge o pico próximo de 0,9 em θ = 0,6, valor mais alto que o θ = 0,04 originalmente proposto na literatura, diferença que os autores atribuem ao espaço conceitual mais específico de sua plataforma [F: alatrash2025prerequisite, §4].

Liang et al. propõem uma medida de relações de pré-requisito entre conceitos [F: liang2015prerequisite, metadados verificados via Crossref; texto integral não consultado]; é a origem do critério RefD usado acima.

[I] O padrão que emerge: pré-requisitos inferidos entram no grafo como arestas com confiança, em grafo nomeado próprio, distintas das curadas. Ver kg.eng.construction.

### Progressão curricular

A BNCC define "o conjunto orgânico e **progressivo** de aprendizagens essenciais" [F: mec2026bncc]. [I] A progressão por ano/série é informação adicional e distinta do pré-requisito: um conceito pode ser pré-requisito de outro e os dois aparecerem no mesmo ano; outros dois podem estar em anos distantes sem relação de dependência.

Modelar a progressão como atributo do conceito (`ano: 5`) é simples e suficiente para a maioria das consultas; modelá-la como classe (`EtapaCurricular`) permite falar de bimestre, unidade e sequência didática, ao custo de mais nós. A escolha depende das competency questions. [I]

## Requisitos e pressupostos

- Uma fonte para as relações: curadoria, inferência ou ambas, com a origem declarada.
- Validação de aciclicidade, que não vem de graça [F: w3c2009skos, §8.6.8].
- Separação entre afirmado e derivado, se houver materialização.
- Decisão sobre força: binária ou com peso. Se com peso, decidir a forma de anotação antes de popular o grafo. [I]

## Vantagens e limitações

Vantagens: é a relação que mais valor agrega a um grafo educacional, porque sustenta diagnóstico e sequenciamento; a estrutura DAG permite algoritmos conhecidos (ordenação topológica, caminho mínimo); e a inferência automática reduz o custo de povoar.

Limitações: nenhum padrão a define bem; a validade pedagógica de uma relação inferida não é garantida pela precisão do método; o fecho transitivo cresce rápido; e a distinção entre ordem de apresentação e dependência cognitiva é fácil de perder na prática de curadoria. [I]

## Alternativas e comparações

| Como representar | Vantagem | Limitação |
|---|---|---|
| `preRequisitoDe` binária | simples; consulta com property path | não exprime força |
| Nó de relação com força e proveniência | exprime tudo | mais nós; consulta mais longa |
| Grafo nomeado por origem (curado / inferido) | separa autoridade; filtro por origem na consulta | granularidade por lote |
| CASE `precedes` | padrão existente | significa ordem, não dependência [F: ims2017case10] |
| `skos:related` | padrão existente | choca com a disjunção §8.6.10 [F: w3c2009skos] |

## Métricas e métodos de avaliação

Para inferidos, a literatura reporta precisão, recall, F1 e acurácia contra conjunto de referência, com ênfase declarada em precisão [F: alatrash2025prerequisite, §4]. [I] Para curados: taxa de ciclos detectados; conceitos órfãos (sem predecessor nem sucessor); concordância entre curadores. Para o uso: se o diagnóstico baseado em pré-requisitos melhora decisões pedagógicas — métrica que pertence ao domínio `aprendizagem-adaptativa` (ver adp.eval.educational-effectiveness).

## Exemplo técnico independente de domínio

```turtle
# relação curada, com força e origem explícitas
GRAPH ex:g/pre-requisitos/curado-2026-10 {
  ex:rel/812 a v:RelacaoPreRequisito ;
      v:origem   ex:c/divisao ;
      v:destino  ex:c/8f3a ;
      v:forca    0.95 .
}
ex:g/pre-requisitos/curado-2026-10 prov:wasAttributedTo ex:agente/curadoria .

# relação inferida, no seu próprio grafo, com confiança do método
GRAPH ex:g/pre-requisitos/inferido-2026-10 {
  ex:rel/9044 a v:RelacaoPreRequisito ;
      v:origem   ex:c/proporcao ;
      v:destino  ex:c/escala ;
      v:confianca 0.62 ;
      v:metodo    ex:metodo/votacao-multicriterio .
}
```

```sparql
# diagnóstico: dado um conceito falhado, que pré-requisitos verificar,
# considerando só relações acima de um limiar de força
SELECT DISTINCT ?pre WHERE {
  GRAPH ?g {
    ?r v:destino ex:c/8f3a ; v:origem ?pre .
    OPTIONAL { ?r v:forca ?f }
    OPTIONAL { ?r v:confianca ?c }
  }
  FILTER (COALESCE(?f, ?c, 0) >= 0.7)
}
```

## Relações com outros conceitos

Parte de kg.mod.conceptual-model. Depende de kg.found.reasoning (fecho transitivo). Complementa kg.curr.competency-frameworks. Avaliado por kg.std.shacl (aciclicidade). Relaciona-se com iop.comp.case (`precedes`), kg.eng.construction (inferência automática) e, no domínio vizinho, com adp.adapt.sequencing-policies (o uso das relações para decidir o que vem depois).

## Lacunas e questões abertas

- O texto de Liang et al. não foi consultado; só metadados via Crossref. A definição exata da medida RefD não foi examinada.
- **Discrepância registrada**: o resumo de Alatrash et al. afirma precisão superior aos métodos existentes, mas a tabela 4 do próprio artigo mostra que isso vale apenas em um dos três domínios, e com recall muito inferior. Este documento reporta a tabela, não o resumo.
- Os experimentos usam o conjunto AL-CPL e um conjunto de Biologia derivado de capítulos de livro didático [F: alatrash2025prerequisite, §4]; o segundo não foi examinado aqui.
- Não há, nas fontes consultadas, validação de que relações de pré-requisito inferidas melhoram resultados de aprendizagem.
- [H] Um limiar de confiança para usar relação inferida em diagnóstico precisa ser calibrado por domínio: Alatrash et al. encontram θ ótimo de 0,28 para o algoritmo de votação e 0,6 para RefD, contra 0,04 na literatura anterior, atribuindo a diferença ao espaço conceitual [F: alatrash2025prerequisite, §4]. Não há valor transferível entre domínios.
- Como representar progressão por ano sem duplicar conceitos permanece aberto; a BNCC organiza por etapa [F: mec2026bncc], mas o mesmo conceito reaparece em anos diferentes com profundidade distinta.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| alatrash2025prerequisite | academico | 2026-10-29 |
| liang2015prerequisite | academico | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| w3c2017shacl | normativo | 2026-10-29 |
| w3c2013sparql11query | normativo | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| mec2026bncc | normativo | 2026-10-29 |
