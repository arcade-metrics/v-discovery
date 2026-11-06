---
id: kg.std.json-ld
titulo: JSON-LD 1.1
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2020jsonld11, w3c2014rdf11concepts, schemaorg2026learningresource, onedtech2025case]
relacoes:
  - { tipo: parte-de, alvo: kg.std.index }
  - { tipo: depende-de, alvo: kg.std.rdf }
  - { tipo: complementa, alvo: iop.md.lrmi-schema-org }
  - { tipo: relacionado-a, alvo: iop.comp.case }
termos: [JSON-LD, context, @context, @id, @type, @graph, compaction, expansion, linked data, serialização]
---

# JSON-LD 1.1

## Definição e terminologia

JSON-LD 1.1 é "A JSON-based Serialization for Linked Data" [F: w3c2020jsonld11, título]. É uma das serializações concretas do modelo abstrato definido por RDF [F: w3c2014rdf11concepts, resumo].

A ideia central é o **contexto**: um documento JSON comum ganha semântica de linked data quando acompanhado de um mapeamento que associa suas chaves a IRIs. [I] O JSON continua sendo JSON para quem não se importa; passa a ser um grafo para quem se importa.

## Status normativo

W3C Recommendation de 16/07/2020, versão REC-json-ld11-20200716, editada por Gregg Kellogg, Pierre-Antoine Champin (LIRIS, Université de Lyon) e Dave Longley (Digital Bazaar). A Recommendation anterior é JSON-LD 1.0, de 16/01/2014 [F: w3c2020jsonld11].

## Fundamentos e funcionamento

[I] Os mecanismos que importam em um grafo educacional:

- `@context`: o mapeamento de termos para IRIs. Pode ser embutido ou referenciado por URL, o que permite publicar o vocabulário uma vez e referenciá-lo em todos os documentos.
- `@id`: o identificador do nó. É o que transforma um objeto JSON em entidade referenciável.
- `@type`: a classe do nó.
- `@graph`: agrupa nós; corresponde a um grafo nomeado quando acompanhado de `@id`.

Transformações definidas pela especificação incluem expansão (resolver tudo a IRIs completos) e compactação (reaplicar um contexto para obter JSON idiomático) [F: w3c2020jsonld11].

### Por que importa neste domínio

Duas razões concretas:

1. **Marcação de recursos educacionais na Web.** schema.org define os tipos e propriedades (`LearningResource`, `teaches`, `assesses`, `educationalAlignment`) [F: schemaorg2026learningresource]; JSON-LD é a forma usual de embuti-los em uma página. Ver iop.md.lrmi-schema-org.
2. **Troca de dados entre sistemas que já falam JSON.** O CASE, por exemplo, troca frameworks de competências como entidades JSON — `CFItem`, `CFDocument`, `CFAssociation` — com identificadores globalmente únicos (GUIDs) [F: onedtech2025case, §1]. [I] Um documento JSON com GUID está a um `@context` de distância de ser RDF.

## Requisitos e pressupostos

- Um contexto publicado e versionado. [I] Se o `@context` mudar o significado de um termo, todos os documentos que o referenciam mudam de sentido retroativamente — risco real quando o contexto é carregado por URL.
- Um processador JSON-LD, se o objetivo for converter para RDF; sem ele, o documento é só JSON.
- Identificadores em `@id` que sejam IRIs, não chaves locais (ver kg.found.identifiers-and-triples).

## Vantagens e limitações

Vantagens: adoção trivial em stacks que já usam JSON; não exige que o consumidor entenda RDF; permite acrescentar semântica a uma API existente sem quebrar clientes; é o caminho de marcação reconhecido por buscadores.

Limitações: a mesma informação admite muitas formas JSON-LD equivalentes, o que complica comparação textual de documentos; o contexto carregado por rede é uma dependência em tempo de execução; e a conversão para RDF esconde decisões (como coerção de tipo) de quem só lê o JSON. [I]

## Alternativas e comparações

| Serialização | Quando |
|---|---|
| JSON-LD | APIs, marcação de página, interoperabilidade com sistemas JSON [F: w3c2020jsonld11] |
| Turtle | leitura e escrita por humanos, ontologias, exemplos |
| N-Triples / N-Quads | carga em massa, diffs linha a linha |
| TriG | datasets com grafos nomeados |
| RDF/XML | sistemas legados |

[I] A tabela é recomendação deste documento; as serializações são especificadas em documentos próprios do W3C não consultados nesta sessão, exceto JSON-LD.

## Exemplo técnico independente de domínio

```json
{
  "@context": {
    "ex":   "https://example.org/voc/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prefLabel":     { "@id": "skos:prefLabel", "@language": "pt" },
    "preRequisitoDe":{ "@id": "ex:preRequisitoDe", "@type": "@id" }
  },
  "@graph": [
    {
      "@id":   "https://example.org/id/c/8f3a",
      "@type": "skos:Concept",
      "prefLabel": "Frações equivalentes",
      "preRequisitoDe": "https://example.org/id/c/1b2c"
    }
  ]
}
```

[I] `"@type": "@id"` na definição de `preRequisitoDe` é o que faz a string virar referência a um nó, e não um literal. Omitir isso é o erro mais comum ao escrever contextos à mão.

## Relações com outros conceitos

Parte de kg.std.index. Depende de kg.std.rdf. Complementa iop.md.lrmi-schema-org (JSON-LD é a forma usual de aplicar schema.org). Relaciona-se com iop.comp.case.

## Lacunas e questões abertas

- Os documentos companheiros (JSON-LD 1.1 Processing Algorithms and API, Framing) não foram consultados.
- Não foi verificado se o CASE publica um contexto JSON-LD oficial; a especificação consultada descreve entidades JSON e GUIDs, sem menção a `@context` nas seções lidas [F: onedtech2025case].
- O risco de versionamento de `@context` carregado por URL não tem tratamento documentado nas fontes consultadas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2020jsonld11 | normativo | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
