---
id: iop.md.dublin-core
titulo: Dublin Core (DCMI Metadata Terms)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [dcmi2020terms, dcmi2026lrmi, w3c2009skos, schemaorg2026learningresource, ieee2020lom]
relacoes:
  - { tipo: alternativa-a, alvo: iop.md.ieee-lom }
  - { tipo: complementa, alvo: iop.md.lrmi-schema-org }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: relacionado-a, alvo: iop.md.comparison }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: relacionado-a, alvo: kg.std.skos }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [Dublin Core, DCMI Metadata Terms, elemento, namespace, namespace /terms/, namespace /elements/1.1/, subpropriedade, vocabulary encoding scheme, syntax encoding scheme, descrição de recurso, LRMI, concept scheme]
---

# Dublin Core e DCMI Metadata Terms

## Definição e terminologia

**DCMI Metadata Terms** é o vocabulário de descrição de recursos mantido pela Dublin Core Metadata Initiative: "an up-to-date specification of all metadata terms maintained by the Dublin Core Metadata Initiative, including properties, vocabulary encoding schemes, syntax encoding schemes, and classes" [F: dcmi2020terms].

**Namespaces** [F: dcmi2020terms]:

| Namespace | Conteúdo |
|---|---|
| `http://purl.org/dc/elements/1.1/` | os quinze elementos originais |
| `http://purl.org/dc/terms/` | o vocabulário principal de termos |
| `http://purl.org/dc/dcmitype/` | DCMI Type Vocabulary |
| `http://purl.org/dc/dcam/` | termos para descrever os próprios termos DCMI |

**Os quinze elementos**: contributor, coverage, creator, date, description, format, identifier, language, publisher, relation, rights, source, subject, title, type [F: dcmi2020terms].

A especificação documenta os dois namespaces principais, lista esquemas de codificação de vocabulário e de sintaxe, e classes [F: dcmi2020terms, sumário].

## Status normativo

DCMI Recommendation, emitida em 2020-01-20, criada pelo DCMI Usage Board. O identificador da versão é `http://dublincore.org/specifications/dublin-core/dcmi-terms/2020-01-20/` [F: dcmi2020terms].

## Problema que resolve

Dar um conjunto mínimo e universal de propriedades para descrever qualquer recurso, de modo que catálogos heterogêneos possam ao menos trocar o essencial [I].

## Fundamentos e funcionamento

### Relação entre os dois namespaces

`/elements/1.1/` foi criado em 2000 para os quinze elementos originais e será suportado indefinidamente. `/terms/` foi criado em 2001 para novos termos; em 2008, os quinze elementos foram espelhados ali com restrições formais: por exemplo, `dcterms:date` tem range literal, enquanto `dc:date` não tem. Cada elemento de `/terms/` é subpropriedade do correspondente em `/elements/1.1/`; a maioria dos usuários pode tratar os pares como equivalentes, mas a DCMI encoraja o uso de `/terms/` [F: dcmi2020terms].

[I] A distinção importa num grafo: `dcterms:creator` (namespace `/terms/`) tem contradomínio definido; `dc:creator` (namespace `/elements/1.1/`) é literal livre. Misturar os dois gera inconsistência de tipo silenciosa. Já a relação de subpropriedade declarada é exatamente o tipo de afirmação que torna um mapeamento verificável por máquina em vez de convencionado por documento (ver `iop.fund.mapeamento-e-proveniencia`).

### Papel em um grafo educacional

[I] Dublin Core é o núcleo mínimo de descrição de qualquer recurso: título, criador, data, idioma, assunto, tipo, formato, direitos, relação. É o vocabulário que não precisa de justificativa: se um grafo tem recursos, usa Dublin Core para o básico e vocabulário especializado para o resto.

A DCMI descreve sua própria abordagem de metadados como visando "pragmatic interoperability among traditional and newer technologies on the basis of knowledge graph design principles" [F: dcmi2020terms, página da DCMI, seção Metadata Basics].

### LRMI

A camada educacional sobre o Dublin Core é o LRMI, também mantido pela DCMI: classes, propriedades e *concept schemes* (declarados em SKOS) para descrição de recursos educacionais, construídos sobre schema.org [F: dcmi2026lrmi]. O LRMI é tratado em `iop.md.lrmi-schema-org`. [I] A consequência prática para quem usa Dublin Core: onde schema.org admite `Text` ou `DefinedTerm` (por exemplo em `learningResourceType` e `educationalUse` [F: schemaorg2026learningresource]), os concept schemes do LRMI oferecem os conceitos SKOS a usar como valores controlados [F: dcmi2026lrmi; w3c2009skos].

## Requisitos e pressupostos

- Escolha explícita entre os namespaces `/terms/` e `/elements/1.1/`, e disciplina em não misturá-los sem necessidade [I].
- Para uso educacional, Dublin Core sozinho é insuficiente: não traz nível de ensino, competência ensinada nem tipo de recurso educacional. Esses vêm de LRMI/schema.org ou LOM [I].
- Para usar os concept schemes do LRMI como valores, um entendimento de SKOS (ver `kg.std.skos`) [F: dcmi2026lrmi].

## Vantagens e limitações

Vantagens [I]: adoção amplíssima e estável, com termos estáveis desde os anos 1990; semântica formal publicada em RDF, o que o torna base natural para grafos; custo de adoção quase nulo para o conjunto de quinze elementos; o LRMI acrescenta a camada educacional com valores controlados declarados em SKOS.

Limitações [I]:
- Genérico por projeto: não descreve nada do que é especificamente educacional; `dcterms:subject` não distingue "ensina" de "trata de".
- A coexistência dos dois namespaces gera ambiguidade em implementações descuidadas.
- A relação entre LRMI Terms, LRMI 1.1 e as propriedades correspondentes de schema.org exige atenção para não duplicar afirmações.

## Alternativas e comparações

| Necessidade | Vocabulário |
|---|---|
| Núcleo de descrição de recurso | DCMI Metadata Terms [F: dcmi2020terms] |
| Propriedades pedagógicas na Web aberta | schema.org LearningResource [F: schemaorg2026learningresource]; ver `iop.md.lrmi-schema-org` |
| Valores controlados para essas propriedades | LRMI concept schemes, em SKOS [F: dcmi2026lrmi] |
| Metadados de objeto de aprendizagem em repositório | IEEE LOM [F: ieee2020lom]; ver `iop.md.ieee-lom` |

Comparação dimensão a dimensão em `iop.md.comparison`; por camada de cobertura, em `kg.voc.comparison`.

## Exemplo técnico independente de domínio

Em JSON-LD, só Dublin Core:

```json
{
  "@context": { "dcterms": "http://purl.org/dc/terms/" },
  "@id": "https://repo.exemplo/recursos/42",
  "dcterms:title": "Sequência didática sobre frações",
  "dcterms:creator": "https://repo.exemplo/pessoas/17",
  "dcterms:language": "pt-BR",
  "dcterms:license": "https://creativecommons.org/licenses/by/4.0/",
  "dcterms:source": "https://outro.exemplo/recursos/9"
}
```

Em Turtle, Dublin Core para a descrição e schema.org para a relação pedagógica:

```turtle
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema:  <https://schema.org/> .
@prefix ex:      <https://example.org/id/> .

ex:r/4412 a schema:LearningResource ;
    dcterms:title     "Introdução a frações equivalentes"@pt ;
    dcterms:creator   ex:agente/equipe-conteudo ;
    dcterms:created   "2026-03-14"^^xsd:date ;
    dcterms:language  "pt-BR" ;
    dcterms:license   <https://creativecommons.org/licenses/by/4.0/> ;
    schema:teaches    ex:c/8f3a .
```

[I] Dublin Core para o que é descrição de recurso; schema.org para o que é relação pedagógica. A divisão evita usar `dcterms:subject` para dizer "ensina", afirmação mais forte e mais útil.

## Relações com outros conceitos

Alternativa parcial a `iop.md.ieee-lom` (genérico versus educacional; na prática os dois se complementam) e complementar a `iop.md.lrmi-schema-org`, que acrescenta as propriedades educacionais. Depende de `iop.sem.vocabularios-e-skos` para o uso em grafos. No domínio do grafo: depende de `kg.std.rdf` e relaciona-se com `kg.std.skos` (os concept schemes do LRMI).

## Lacunas e questões abertas

- O conjunto completo de termos de `/terms/` (bem além dos quinze) não foi inventariado elemento a elemento; só o cabeçalho de status, o sumário e exemplos.
- Não foi verificado se há recomendação DCMI posterior a 2020-01-20.
- Os LRMI Terms em RDF e os concept schemes individuais não foram abertos; a descrição vem da página da especificação [F: dcmi2026lrmi].
- A relação exata entre cada termo LRMI e a propriedade schema.org correspondente não foi mapeada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| dcmi2020terms | normativo | 2026-10-29 |
| dcmi2026lrmi | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| ieee2020lom | normativo | 2026-10-29 |

## Histórico

Fusão, em 29/10/2026, de `iop.md.dublin-core` (interoperabilidade, 89 linhas) com `kg.voc.dublin-core` (grafo de conhecimento educacional, 112 linhas). Nenhum parágrafo foi descartado; os dois exemplos foram mantidos porque usam serializações diferentes. A descrição detalhada do LRMI (LRMI Terms, concept schemes, LRMI 1.1), que estava no documento do grafo, foi levada para `iop.md.lrmi-schema-org`, dono do assunto. `kg.voc.dublin-core` permanece como redirecionamento.
