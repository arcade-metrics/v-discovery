---
id: kg.found.identifiers-and-triples
titulo: Triplas, IRIs e identidade
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2014rdf11concepts, w3c2026rdf12concepts, hogan2021knowledgegraphs, w3c2020jsonld11]
relacoes:
  - { tipo: parte-de, alvo: kg.found.knowledge-graphs }
  - { tipo: especificado-por, alvo: kg.std.rdf }
  - { tipo: complementa, alvo: kg.eng.versioning-and-provenance }
  - { tipo: relacionado-a, alvo: kg.found.context-and-reification }
termos: [tripla, IRI, blank node, literal, datatype, language tag, RDF graph, RDF dataset, named graph, default graph, graph name, triple term, identidade]
---

# Triplas, IRIs e identidade

## Definição e terminologia

Uma **tripla RDF** tem três componentes: sujeito, que é um IRI ou um blank node; predicado, que é um IRI; objeto, que é um IRI, um literal ou um blank node [F: w3c2014rdf11concepts, §3.1]. Um **grafo RDF** é um conjunto de triplas RDF [F: w3c2014rdf11concepts, §3].

Um **RDF dataset** é uma coleção de grafos RDF que compreende exatamente um grafo padrão (*default graph*), sem nome e possivelmente vazio, e zero ou mais grafos nomeados, cada um um par formado por um IRI ou blank node (o *graph name*) e um grafo RDF [F: w3c2014rdf11concepts, §4].

Em RDF 1.2, atualmente Candidate Recommendation Snapshot de 07/04/2026, os elementos de uma tripla podem ser também **triple terms**: uma tripla RDF usada como termo dentro de outra tripla, na posição de objeto [F: w3c2026rdf12concepts, resumo e §1.5]. Há quatro tipos de nó no grafo: IRIs, literais, blank nodes e triple terms [F: w3c2026rdf12concepts, §3].

O que não é: a tripla não é um registro de tabela com três colunas fixas; é uma afirmação atômica. Um blank node não é um identificador global — é local ao documento e não deve ser usado para designar algo que outro sistema precise referenciar. [I]

## Problema que resolve

O par (identificador global, afirmação atômica) é o que permite que duas fontes falem da mesma coisa sem combinarem esquema antes. Hogan et al. tratam *identity* como um dos três elementos-chave para lidar com a diversidade de grafos montados de muitas fontes: identidade "denotes which nodes in the graph (or in external sources) refer to" a mesma entidade do mundo [F: hogan2021knowledgegraphs, §1].

[I] Em educação, o problema concreto é que a mesma habilidade aparece como `EF05MA07` na BNCC, como um GUID em um framework CASE e como uma linha de planilha no banco de itens. Sem um IRI canônico e sem mapeamentos declarados, cada integração recria o vínculo à mão.

## Fundamentos e funcionamento

### IRIs

O predicado é sempre um IRI; sujeito e objeto podem ser [F: w3c2014rdf11concepts, §3.1]. O IRI faz dois trabalhos ao mesmo tempo: identifica e, por ser uma URI, pode ser desreferenciado para obter a descrição. [I] Essa dupla função é o que torna o custo de escolher o esquema de IRI alto: muda-se o domínio e quebram-se referências externas.

Consequência prática: um id é um compromisso de longo prazo. [I] O modelo documental desta base adota a mesma regra — um id nunca muda depois de publicado (ver `_modelo/modelo-documental.md`).

### Literais e tipos

Literais carregam datatype; RDF 1.1 usa os datatypes built-in do XML Schema [F: w3c2014rdf11concepts, §5]. RDF 1.2 acrescenta *directional language-tagged strings*, que têm um componente de direção de base para permitir especificar a direção inicial do texto para apresentação por um agente de usuário [F: w3c2026rdf12concepts, resumo].

### Blank nodes

Blank nodes existem para afirmar que algo existe sem nomeá-lo. [I] São úteis para estruturas auxiliares (listas, nós n-ários) e perigosos como âncora de identidade: não sobrevivem a uma recarga nem podem ser citados de fora. A recomendação prática desta base: usar IRI para tudo que um terceiro possa precisar referenciar; blank node só para estrutura interna. [I]

### Grafos nomeados

O dataset com grafos nomeados é o mecanismo nativo para separar origens e versões. Hogan et al. observam que gerir vários grafos em vez de um monolítico permite "update or refine data from one source, to distinguish untrustworthy sources from more trustworthy ones" [F: hogan2021knowledgegraphs, §2.1.4]. Ver kg.eng.versioning-and-provenance.

### Serialização e JSON-LD

JSON-LD 1.1 é uma serialização JSON para linked data, publicada como W3C Recommendation em 16/07/2020 [F: w3c2020jsonld11]. [I] Importa aqui porque permite que um sistema que já troca JSON receba IRIs e tipagem sem mudar o formato de transporte, só acrescentando um contexto. Ver kg.std.json-ld.

## Requisitos e pressupostos

- Um esquema de IRI com dono e política de persistência. Sem isso a identidade é frágil.
- Separação entre o identificador do conceito e o identificador do documento que o descreve. [I] RDF 1.1 discute o tratamento de identificadores de fragmento em IRIs dentro de grafos RDF precisamente porque essa distinção é fonte de erro [F: w3c2014rdf11concepts, resumo].
- Uma política explícita para equivalência entre identificadores de fontes diferentes (`owl:sameAs`, `skos:exactMatch`, `CFAssociation` do tipo `exactMatchOf`), com ciência de que `owl:sameAs` tem consequências lógicas fortes. Ver kg.std.owl2 e kg.std.skos.

## Vantagens e limitações

Vantagens: integração sem acordo prévio de esquema; granularidade máxima (cada afirmação é adicionável e removível de forma independente); versionamento por grafo nomeado.

Limitações: a tripla não anota a si mesma — qualquer contexto sobre a afirmação exige reificação, nó n-ário, grafo nomeado ou triple term, todos com custo (ver kg.found.context-and-reification); e o número de triplas cresce rápido, já que toda propriedade de toda entidade é uma linha.

## Alternativas e comparações

| Estratégia de identidade | Estabilidade | Legibilidade | Risco |
|---|---|---|---|
| IRI com domínio próprio e caminho opaco (`/id/c/8f3a`) | alta | baixa | exige catálogo de rótulos |
| IRI com slug legível (`/id/c/fracoes-equivalentes`) | média | alta | tenta renomear quando o conceito muda de nome |
| Reuso de IRI de terceiro (ESCO, CASE) | alta, mas externa | média | dependência de disponibilidade e versão do terceiro |
| Blank node | nenhuma fora do documento | nenhuma | não referenciável |

[I] Comparação derivada das propriedades definidas em [F: w3c2014rdf11concepts, §3] e da prática de reuso descrita em [F: hogan2021knowledgegraphs, §3.2].

## Exemplo técnico independente de domínio

```turtle
# IRI estável e opaco para o conceito; rótulo é dado, não identidade
<https://example.org/id/c/8f3a> a                skos:Concept ;
    skos:prefLabel  "Frações equivalentes"@pt ;
    skos:notation   "C-8F3A" .

# mapeamento declarado para um identificador externo, sem igualar logicamente
<https://example.org/id/c/8f3a> skos:closeMatch <http://data.europa.eu/esco/skill/XXXX> .

# a mesma afirmação em um grafo nomeado, para isolar a origem
GRAPH <https://example.org/g/curadoria/2026-10> {
  <https://example.org/id/c/8f3a> :preRequisitoDe <https://example.org/id/c/1b2c> .
}
```

[I] `skos:closeMatch` e não `owl:sameAs`: ver kg.std.skos para a diferença de força entre os dois.

## Relações com outros conceitos

Parte de kg.found.knowledge-graphs. Especificado por kg.std.rdf. Complementa kg.eng.versioning-and-provenance (grafos nomeados como unidade de versão). Relaciona-se com kg.found.context-and-reification (o que fazer quando a tripla precisa de anotação).

## Lacunas e questões abertas

- RDF 1.2 está em Candidate Recommendation Snapshot (07/04/2026) [F: w3c2026rdf12concepts]; a adoção por triplestores e bibliotecas não foi levantada nesta sessão, e o status pode mudar.
- Não foi levantada prática consolidada para esquemas de IRI em grafos curriculares nacionais; a BNCC publica códigos alfanuméricos (ver kg.curr.bncc), não IRIs.
- Critérios para escolher entre `owl:sameAs`, `skos:exactMatch` e mapeamento por propriedade própria ao integrar currículos carecem de fonte empírica aqui.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| w3c2026rdf12concepts | normativo | 2026-10-29 |
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2020jsonld11 | normativo | 2026-10-29 |
