---
id: kg.curr.bncc
titulo: BNCC como grafo
tipo: estudo-de-caso
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [mec2026bncc, mec2026bnccabase, w3c2009skos, onedtech2025case, w3c2013provo]
relacoes:
  - { tipo: parte-de, alvo: kg.curr.competency-frameworks }
  - { tipo: depende-de, alvo: kg.std.skos }
  - { tipo: complementa, alvo: kg.mod.competencies-and-objectives }
  - { tipo: relacionado-a, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: kg.eng.construction }
termos: [BNCC, competência geral, competência específica, área de conhecimento, componente curricular, unidade temática, prática de linguagem, objeto de conhecimento, habilidade, campo de experiências, etapa]
---

# BNCC como grafo

## Definição e terminologia

"A Base Nacional Comum Curricular (BNCC) é um documento de caráter normativo que define o conjunto orgânico e progressivo de aprendizagens essenciais que todos os alunos devem desenvolver ao longo das etapas e modalidades da Educação Básica" [F: mec2026bncc].

Seu estatuto jurídico: "Conforme definido na Lei de Diretrizes e Bases da Educação Nacional (LDB, Lei nº 9.394/1996), a Base deve nortear os currículos dos sistemas e redes de ensino das Unidades Federativas, como também as propostas pedagógicas de todas as escolas públicas e privadas de Educação Infantil, Ensino Fundamental e Ensino Médio, em todo o Brasil" [F: mec2026bncc].

"A Base estabelece conhecimentos, competências e habilidades que se espera que todos os estudantes desenvolvam ao longo da escolaridade básica. Orientada pelos princípios éticos, políticos e estéticos traçados pelas Diretrizes Curriculares Nacionais da Educação Básica, a Base soma-se aos propósitos que direcionam a educação brasileira para a formação humana integral e para a construção de uma sociedade justa, democrática e inclusiva" [F: mec2026bncc].

## Problema que resolve

[I] A BNCC é o framework de competência de referência para qualquer sistema educacional brasileiro, e é a âncora natural de um grafo curricular no país. O problema é que ela é publicada como documento, não como dados: o portal oferece "BNCC para navegação", "BNCC em PDF" e "BNCC em planilha" [F: mec2026bncc]. Nenhuma dessas formas é um grafo.

Consequência: cada consumidor faz sua própria extração, cada extração produz identificadores diferentes, e não há correspondência automática entre duas implementações. Ver kg.found.identifiers-and-triples.

## Fundamentos e funcionamento

### Estrutura documental

O sumário do documento completo revela a arquitetura [F: mec2026bnccabase]:

| Nível | Elemento | Observação |
|---|---|---|
| Transversal | **Competências gerais da BNCC** | seção própria na introdução |
| Organizacional | **Estrutura da BNCC** | seção 2 |
| Etapa | **Educação Infantil**, **Ensino Fundamental**, **Ensino Médio** | seções 3, 4 e 5 |
| Educação Infantil | **campos de experiências**; **objetivos de aprendizagem e desenvolvimento**; **direitos de aprendizagem e desenvolvimento** | seções 3.1, 3.2 |
| Ensino Fundamental | **áreas** (ex.: Linguagens), com **competências específicas de área** | seção 4.1 |
| Componente | **componentes curriculares** (ex.: Língua Portuguesa, Arte), com **competências específicas de componente** | seções 4.1.1, 4.1.2 |
| Organização do componente | **unidades temáticas** (Arte e demais) ou **práticas de linguagem** (Língua Portuguesa), **objetos de conhecimento** e **habilidades** | seções 4.1.1.1, 4.1.2.1 |
| Segmento | **Anos Iniciais** e **Anos Finais** do Ensino Fundamental | subdivisão das seções por componente |

[I] Dois pontos a reter para a modelagem:

1. **A Educação Infantil tem estrutura própria**: campos de experiências e objetivos de aprendizagem e desenvolvimento, não unidades temáticas e habilidades. Um modelo único para as três etapas não funciona sem abstração.
2. **A organização interna varia por componente**: Língua Portuguesa usa "práticas de linguagem" onde Arte usa "unidades temáticas" [F: mec2026bnccabase]. O modelo precisa de um nível genérico ("eixo organizador") com subtipos.

### Mapeamento proposto para grafo

[I] Proposta deste documento, apoiada nas construções SKOS documentadas [F: w3c2009skos]:

| Elemento da BNCC | Construção |
|---|---|
| BNCC inteira | `skos:ConceptScheme` |
| Competência geral | `skos:Concept`, `skos:topConceptOf` |
| Etapa, área, componente | `skos:Concept` com `skos:broader`, formando a espinha |
| Unidade temática / prática de linguagem / campo de experiências | `skos:Concept` (subtipo por classe própria) |
| Objeto de conhecimento | `skos:Concept` |
| Habilidade / objetivo de aprendizagem e desenvolvimento | `skos:Concept`, com `skos:notation` para o código |
| Código alfanumérico da habilidade | `skos:notation` |
| Enunciado da habilidade | `skos:prefLabel` |
| Relação habilidade → competência específica | propriedade própria |
| Relação habilidade → objeto de conhecimento | propriedade própria ou `skos:broader` |

A hierarquia em SKOS deve conter **só vínculos imediatos**, conforme a convenção da especificação [F: w3c2009skos, §8.1]; o fecho se obtém por consulta (ver kg.found.reasoning).

### Pré-requisitos não estão na BNCC

[I] A BNCC define progressão por etapa e ano, mas não publica relações de pré-requisito entre habilidades. Isso é trabalho a fazer por curadoria ou inferência — ver kg.curr.prerequisites e kg.eng.construction. É a diferença entre ter o currículo em grafo e ter um grafo útil para diagnóstico.

### Publicação como framework CASE

[I] O CASE existe exatamente para o caso da BNCC: substituir o documento PDF por versão legível por máquina, com GUIDs, trocável entre sistemas [F: onedtech2025case, §1]. Não foi verificado nesta sessão se existe publicação oficial ou de terceiros da BNCC como CASE Framework.

## Requisitos e pressupostos

- Uma extração a partir da planilha ou do PDF, com validação. [I] A extração é a parte frágil: mudanças de formatação quebram parsers.
- Identificadores próprios, com o código da BNCC como `skos:notation` e não como IRI — o código pode mudar entre edições; o IRI não deve.
- Proveniência da extração registrada: versão do documento, data, método [F: w3c2013provo]. Ver kg.eng.versioning-and-provenance.
- Tratamento explícito da Educação Infantil, cuja estrutura difere.

## Vantagens e limitações

Vantagens de ter a BNCC em grafo: âncora normativa para todo o resto do currículo; relatórios de cobertura automáticos; alinhamento com currículos próprios como dados; ponto de partida para pré-requisitos.

Limitações: não há publicação oficial em formato de grafo; a extração é custosa e frágil; os códigos de habilidade não são IRIs e não há garantia de estabilidade entre edições; a estrutura varia por etapa e por componente; e a BNCC não traz pré-requisitos nem níveis cognitivos explícitos. [I]

## Métricas e métodos de avaliação

[I] Para validar uma extração: contagem de habilidades por componente e ano contra o documento; unicidade de código; ausência de habilidade órfã (sem objeto de conhecimento nem unidade temática); ausência de ciclo na hierarquia. SHACL cobre as três primeiras com o núcleo e a última com SHACL-SPARQL — ver kg.std.shacl.

## Exemplo técnico independente de domínio

```trig
GRAPH ex:g/bncc/extracao-2026-10 {
  ex:fw/bncc a skos:ConceptScheme ;
      skos:prefLabel "Base Nacional Comum Curricular"@pt .

  ex:bncc/ef a skos:Concept ;
      skos:inScheme ex:fw/bncc ; skos:prefLabel "Ensino Fundamental"@pt ;
      skos:topConceptOf ex:fw/bncc .

  ex:bncc/matematica a skos:Concept ;
      skos:inScheme ex:fw/bncc ; skos:prefLabel "Matemática"@pt ;
      skos:broader  ex:bncc/ef ;
      a v:ComponenteCurricular .

  ex:bncc/un/numeros a skos:Concept ;
      skos:inScheme ex:fw/bncc ; skos:prefLabel "Números"@pt ;
      skos:broader  ex:bncc/matematica ;
      a v:UnidadeTematica .

  # habilidade: IRI próprio, código como notation
  ex:bncc/hab/4f21 a skos:Concept , v:Habilidade ;
      skos:inScheme  ex:fw/bncc ;
      skos:notation  "EF05MA07" ;
      skos:prefLabel "Resolver e elaborar problemas envolvendo frações equivalentes"@pt ;
      skos:broader   ex:bncc/un/numeros ;
      v:anoEscolar   5 .
}

# proveniência da extração: sem isso, a origem do grafo é desconhecida
ex:g/bncc/extracao-2026-10 a prov:Entity ;
    prov:wasGeneratedBy  ex:atividade/extracao-bncc ;
    prov:wasAttributedTo ex:agente/pipeline-extracao ;
    v:fonte "BNCC em planilha, portal MEC, consultado em 2026-10-29" .
```

[I] O código `EF05MA07` do exemplo é ilustrativo: o formato do código alfanumérico da BNCC não foi verificado contra o documento nesta sessão.

## Relações com outros conceitos

Parte de kg.curr.competency-frameworks. Depende de kg.std.skos. Complementa kg.mod.competencies-and-objectives (a BNCC fornece a camada "habilidade"). Relaciona-se com iop.comp.case (o formato de troca que caberia) e kg.eng.construction (a extração).

## Lacunas e questões abertas

- **A maior parte deste documento é proposta, não descrição.** O que está verificado é o estatuto normativo, a base legal, os formatos de publicação e a estrutura de seções do documento [F: mec2026bncc; mec2026bnccabase]. O mapeamento para grafo é deste documento.
- O formato do código alfanumérico de habilidade não foi verificado: a página de navegação do documento é renderizada por JavaScript e o texto das seções não pôde ser extraído.
- As contagens (quantas habilidades, quantos objetos de conhecimento) não foram levantadas.
- Não foi verificado se existe publicação da BNCC em SKOS, RDF ou CASE, oficial ou de terceiros.
- A BNCC do Ensino Médio tem estrutura de itinerários formativos que não foi examinada.
- Não foi verificado se o portal versiona o documento; nenhuma indicação de versão aparece na página inicial [F: mec2026bncc].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| mec2026bncc | normativo | 2026-10-29 |
| mec2026bnccabase | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
