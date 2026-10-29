---
id: iop.md.dublin-core
titulo: Dublin Core (DCMI Metadata Terms)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [dcmi2020terms]
relacoes:
  - { tipo: alternativa-a, alvo: iop.md.ieee-lom }
  - { tipo: complementa, alvo: iop.md.lrmi-schema-org }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: relacionado-a, alvo: iop.md.comparison }
termos: [DCMI Metadata Terms, elemento, namespace, subpropriedade, descrição de recurso]
---

# Dublin Core

## Definição e terminologia

**DCMI Metadata Terms** é o vocabulário de descrição de recursos mantido pela Dublin Core Metadata Initiative. A versão corrente consultada tem identificador datado de **2020-01-20**, com status de **DCMI Recommendation** [F: dcmi2020terms].

**Namespaces** [F: dcmi2020terms]:

| Namespace | Conteúdo |
|---|---|
| `http://purl.org/dc/elements/1.1/` | os quinze elementos originais |
| `http://purl.org/dc/terms/` | o vocabulário principal de termos |
| `http://purl.org/dc/dcmitype/` | DCMI Type Vocabulary |
| `http://purl.org/dc/dcam/` | termos para descrever os próprios termos DCMI |

**Os quinze elementos**: contributor, coverage, creator, date, description, format, identifier, language, publisher, relation, rights, source, subject, title, type [F: dcmi2020terms].

## Problema que resolve

Dar um conjunto mínimo e universal de propriedades para descrever qualquer recurso, de modo que catálogos heterogêneos possam ao menos trocar o essencial [I].

## Fundamentos e funcionamento

**Relação entre os dois namespaces.** `/elements/1.1/` foi criado em 2000 para os quinze elementos originais e será suportado indefinidamente. `/terms/` foi criado em 2001 para novos termos; em 2008, os quinze elementos foram espelhados ali com restrições formais — por exemplo, `dcterms:date` tem range literal, enquanto `dc:date` não tem. Cada elemento de `/terms/` é subpropriedade do correspondente em `/elements/1.1/`; a maioria dos usuários pode tratar os pares como equivalentes, mas a DCMI encoraja o uso de `/terms/` [F: dcmi2020terms].

Essa relação de subpropriedade é exatamente o tipo de declaração que torna um mapeamento verificável por máquina em vez de convencionado por documento (ver `iop.fund.mapeamento-e-proveniencia`) [I].

## Requisitos e pressupostos

- Para uso educacional, Dublin Core sozinho é insuficiente: não traz nível de ensino, competência ensinada nem tipo de recurso educacional. Esses vêm de LRMI/schema.org ou LOM [I].

## Vantagens e limitações

Vantagens [I]: adoção amplíssima e estável; semântica formal publicada em RDF, o que o torna base natural para grafos; custo de adoção quase nulo para o conjunto de quinze elementos.

Limitações [I]:
- Genérico por projeto: não descreve nada do que é especificamente educacional.
- A coexistência dos dois namespaces gera ambiguidade em implementações descuidadas.

## Alternativas e comparações

Ver `iop.md.comparison`.

## Exemplo técnico independente de domínio

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

## Relações com outros conceitos

Alternativa parcial a `iop.md.ieee-lom` (genérico versus educacional) e complementar a `iop.md.lrmi-schema-org`, que acrescenta as propriedades educacionais. Depende de `iop.sem.vocabularios-e-skos` para o uso em grafos.

## Lacunas e questões abertas

- O conjunto completo de termos de `/terms/` (bem além dos quinze) não foi inventariado aqui.
- Não foi verificado se há recomendação DCMI posterior a 2020-01-20.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| dcmi2020terms | normativo | 2026-10-29 |
