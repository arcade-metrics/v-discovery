---
id: iop.md.ieee-lom
titulo: IEEE LOM (1484.12.1, Learning Object Metadata)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2020lom, ieee2020lomxml, standict2026lom, imsglobal2022qti30, imsglobal2011cc, dcmi2020terms, schemaorg2026learningresource]
relacoes:
  - { tipo: alternativa-a, alvo: iop.md.dublin-core }
  - { tipo: alternativa-a, alvo: iop.md.lrmi-schema-org }
  - { tipo: complementa, alvo: iop.tool.common-cartridge }
  - { tipo: relacionado-a, alvo: iop.md.comparison }
  - { tipo: relacionado-a, alvo: kg.mod.conceptual-model }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [LOM, learning object, learning object metadata, objeto de aprendizagem, metadado educacional, esquema conceitual de dados, categoria educational, categoria classification, categoria relation, binding XML, perfil de aplicação]
---

# IEEE LOM (1484.12.1)

## Definição e terminologia

IEEE LOM é o padrão de metadados para objetos de aprendizagem. A norma especifica "a conceptual data schema that defines the structure of a metadata instance for a learning object". Para efeito da norma, **learning object** é "any entity, digital or non-digital, that is used for learning, education, or training"; uma instância de metadados para um objeto de aprendizagem "describes relevant characteristics of the learning object to which it applies" [F: ieee2020lom, resumo].

Essas características são reagrupadas em categorias: *general*, *life cycle*, *meta-metadata*, *educational*, *technical*, *rights*, *relation*, *annotation* e *classification* [F: ieee2020lom, resumo].

O esquema conceitual "specifies the data elements of which a metadata instance for a learning object is composed and allows for linguistic diversity of both learning objects and the metadata instances that describe them" [F: ieee2020lom, resumo].

## Status normativo

IEEE 1484.12.1-2020, **Active Standard**, do comitê C/LT (Learning Technology) da IEEE Computer Society, desenvolvido pelo grupo de trabalho SCORMRENEW. Supersede 1484.12.1-2002. Aprovação do PAR em 2019-09-05, aprovação da diretoria em 2020-09-24, publicação em 2020-11-16 [F: ieee2020lom]. As mesmas datas constam de repositório secundário de normas [F: standict2026lom].

O binding XML é norma separada: IEEE 1484.12.3-2020 define "a World Wide Web Consortium (W3C) Extensible Markup Language (XML) Schema definition language binding of the learning object metadata (LOM) data model defined in IEEE Std 1484.12.1-2002"; nota-se que o texto do catálogo referencia a edição de 2002 do modelo de dados [F: ieee2020lomxml].

## Problema que resolve

Permitir que repositórios distintos descrevam recursos educacionais de forma comparável, de modo que a busca e a federação de catálogos funcionem entre instituições [I].

## Fundamentos e funcionamento

A norma declara explicitamente seu papel de base para outras normas: "it is intended that this standard will be referenced by other standards that will define the implementation descriptions of the data schema, so that a metadata instance for a learning object can be used by a learning technology system to manage, locate, evaluate, or exchange learning objects" [F: ieee2020lom, resumo].

E declara a intenção de fundo: "to specify a base schema, which can be used to build on as practice develops, for instance in order to facilitate automatic, adaptive scheduling of learning objects by software agents" [F: ieee2020lom, resumo]. [I] Esse trecho é notável: a adaptação automática por agentes de software está no escopo declarado da norma desde a edição original. O que LOM oferece é o vocabulário para descrever o recurso, não para descrever o aluno.

### Uso por outros padrões

LOM é usado como vocabulário de metadados por outros padrões de interoperabilidade: o QTI 3.0 perfila o IEEE LOM, além do 1EdTech Metadata v1.3 [F: imsglobal2022qti30, §2.4]; a partir do Common Cartridge v1.3, links LTI dentro de um cartridge podem carregar metadados LOM completos e padrões curriculares [F: imsglobal2011cc].

### Perfil de aplicação

O mecanismo central de uso prático é o **perfil de aplicação**: um subconjunto de elementos com vocabulários e obrigatoriedades definidos para uma comunidade. Sem perfil, implementações preenchem elementos diferentes e a comparabilidade não se materializa [I].

### O que LOM cobre e o que não cobre

[I] Pelo resumo normativo, LOM descreve **o recurso**: o que é, quem fez, como se usa, a que se relaciona, sob que direitos, em que classificação. Não descreve: a competência em si (isso é CASE, ESCO, CTDL; ver `iop.comp.case`, `iop.comp.esco`, `iop.comp.ctdl`), o estado do aluno, nem a evidência de aprendizagem. Em um grafo de conhecimento educacional, portanto, LOM ocupa a camada de **recursos**, ligada por alinhamento à camada de **competências**. Ver `kg.mod.layer-separation`.

### Relação com outros vocabulários

[I] LOM é anterior ao ecossistema RDF educacional e tem forma de esquema de metadados, não de ontologia. Dublin Core cobre parte semelhante do espaço de descrição de recurso, com menos elementos e uso mais amplo [F: dcmi2020terms]; schema.org `LearningResource` cobre o mesmo campo com vocabulário de Web aberta e propriedades de alinhamento pedagógico explícitas (`teaches`, `assesses`, `educationalAlignment`) [F: schemaorg2026learningresource].

## Requisitos e pressupostos

- Existe um perfil de aplicação acordado entre os participantes da federação [I].
- Há disciplina de catalogação: LOM é um esquema rico, e o custo de preenchimento recai sobre quem publica o recurso [I].
- Para uso em grafo RDF, é preciso um mapeamento de LOM para RDF; a norma define esquema conceitual e o binding publicado é XML [F: ieee2020lomxml]. Nenhum mapeamento RDF oficial foi verificado.
- O texto integral da norma é pago; o que consta aqui vem da página pública do catálogo IEEE SA e de repositório secundário.

## Vantagens e limitações

Vantagens [I]: norma IEEE ativa, com ciclo de revisão formal, escopo bem delimitado e amplamente conhecida em repositórios de objetos de aprendizagem; cobre explicitamente a dimensão educacional (nível, público, tipo de interatividade, tempo típico de aprendizagem), ausente em esquemas genéricos; suporte explícito a diversidade linguística [F: ieee2020lom, resumo]; base referenciada por outras normas, por desenho.

Limitações [I]:
- Forma de esquema de metadados XML, não de grafo; nasceu em contexto de repositórios institucionais, enquanto a web de dados atual descreve recursos educacionais em JSON-LD com schema.org (ver `iop.md.lrmi-schema-org`).
- Esquema extenso: na prática, só uma fração dos elementos é preenchida. [H] A categoria *educational* seria a menos preenchida em repositórios reais; hipótese não verificada.
- Sem perfil de aplicação, a interoperabilidade semântica não se realiza mesmo com conformidade total ao esquema.
- Acesso pago ao texto; não cobre competências nem o aluno.

## Alternativas e comparações

Ver `iop.md.comparison` (dimensão a dimensão) e `kg.voc.comparison` (por camada). Em resumo: LOM para repositórios que já o adotam e para conformidade com normas que o referenciam; schema.org para descoberta na Web aberta; Dublin Core para o núcleo mínimo de descrição.

## Exemplo técnico independente de domínio

[I] As categorias de LOM mapeadas às camadas de um grafo educacional; mapeamento proposto por este documento, não pela norma:

```
LOM, categoria            →  camada do grafo
general, technical        →  Recurso (identificação, formato)
life cycle, meta-metadata →  Proveniência (ver kg.std.prov-o)
rights                    →  Recurso (licenciamento)
relation                  →  arestas Recurso → Recurso
classification            →  arestas Recurso → Conceito/Competência (alinhamento)
educational               →  atributos pedagógicos do Recurso
annotation                →  anotação contextual (ver kg.found.context-and-reification)
```

## Relações com outros conceitos

Alternativa a `iop.md.dublin-core` (que, na prática, o complementa) e a `iop.md.lrmi-schema-org`. Complementa `iop.tool.common-cartridge` e `iop.asmt.qti`, que o perfilam. No domínio do grafo: relaciona-se com `kg.mod.conceptual-model` (onde os recursos entram no modelo).

## Lacunas e questões abertas

- O texto normativo completo não foi consultado (acesso pago). A lista de elementos de dados por categoria, os vocabulários de valores, a semântica exata de `classification` e as diferenças em relação à edição de 2002 não puderam ser verificados.
- Não foi verificado se existe binding ou mapeamento RDF oficial de LOM.
- Nota de inconsistência a verificar: o resumo de 1484.12.3-2020 na página do catálogo refere-se ao modelo de dados de 1484.12.1-**2002**, enquanto 1484.12.1-2020 é a edição ativa [F: ieee2020lomxml; ieee2020lom]. Pode ser texto de catálogo não atualizado.
- A taxa de preenchimento real das categorias em repositórios não foi levantada.
- Qual perfil de aplicação LOM é usado em repositórios brasileiros de recursos educacionais? Não verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ieee2020lom | normativo | 2026-10-29 |
| ieee2020lomxml | normativo | 2026-10-29 |
| standict2026lom | secundario | 2026-10-29 |
| imsglobal2022qti30 | normativo | 2026-10-29 |
| imsglobal2011cc | normativo | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |

## Histórico

Fusão, em 29/10/2026, de `iop.md.ieee-lom` (interoperabilidade, 71 linhas) com `kg.voc.ieee-lom` (grafo de conhecimento educacional, 101 linhas). Nenhum parágrafo foi descartado; a ressalva do documento de interoperabilidade de que as datas vinham só de repositório secundário foi resolvida pela página do catálogo IEEE SA consultada pela frente do grafo. `kg.voc.ieee-lom` permanece como redirecionamento.
