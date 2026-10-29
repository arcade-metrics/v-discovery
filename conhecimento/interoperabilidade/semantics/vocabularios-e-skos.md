---
id: iop.sem.vocabularios-e-skos
titulo: Vocabulários controlados e SKOS
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2009skos, dcmi2026lrmi, credengine2026ctdl]
relacoes:
  - { tipo: complementa, alvo: iop.sem.interoperabilidade-semantica }
  - { tipo: complementa, alvo: iop.fund.mapeamento-e-proveniencia }
  - { tipo: relacionado-a, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: iop.md.dublin-core }
termos: [SKOS, Concept, ConceptScheme, prefLabel, broader, narrower, exactMatch, closeMatch]
---

# Vocabulários controlados e SKOS

## Definição e terminologia

SKOS (*Simple Knowledge Organization System*) é o modelo de dados do W3C para representar sistemas de organização do conhecimento — tesauros, esquemas de classificação, sistemas de cabeçalhos de assunto e taxonomias — como dados RDF legíveis por máquina. É **W3C Recommendation de 18 de agosto de 2009**, editada por Alistair Miles e Sean Bechhofer, produzida pelo Semantic Web Deployment Working Group [F: w3c2009skos].

Namespace: `http://www.w3.org/2004/02/skos/core#`, prefixo `skos:` [F: w3c2009skos].

**Vocabulário central** [F: w3c2009skos]:

| Grupo | Termos |
|---|---|
| Classes | `skos:Concept`, `skos:ConceptScheme`, `skos:Collection`, `skos:OrderedCollection` |
| Rótulos | `skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel` (para busca textual) |
| Hierarquia e associação | `skos:broader`, `skos:narrower`, `skos:broaderTransitive`, `skos:narrowerTransitive`, `skos:related` |
| Pertencimento a esquema | `skos:inScheme`, `skos:hasTopConcept`, `skos:topConceptOf` |
| Mapeamento | `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch` |

O SKOS é descrito como "standard, low-cost migration path" para levar sistemas existentes à web semântica, utilizável sozinho ou junto com OWL; a especificação é definida como ontologia OWL Full [F: w3c2009skos].

## Problema que resolve

Padrões de intercâmbio definem campos; quase todos deixam o *valor* do campo em aberto. SKOS dá a forma canônica de publicar as listas de valores com identificadores, rótulos multilíngues, hierarquia e — crucialmente — correspondências entre listas de origens diferentes [I].

## Fundamentos e funcionamento

**A distinção entre `exactMatch` e `closeMatch` é o instrumento central de honestidade semântica** [I]: `exactMatch` afirma equivalência utilizável com confiança em aplicações de recuperação; `closeMatch` afirma similaridade suficiente para algumas aplicações. Tratar um `closeMatch` como `exactMatch` é a forma mais comum de perda silenciosa em integrações (ver `iop.fund.mapeamento-e-proveniencia`).

**Uso em padrões educacionais.** O LRMI declara seus esquemas de conceitos em RDF usando SKOS [F: dcmi2026lrmi]. O CTDL é descrito pelo mantenedor como modelo baseado em especificações da web semântica, com estrutura de linked data [F: credengine2026ctdl].

## Requisitos e pressupostos

- Cada conceito tem URI estável sob controle de quem publica o vocabulário.
- Há política de versionamento: conceitos não são apagados, são marcados como obsoletos com apontamento para o substituto [I].

## Vantagens e limitações

Vantagens [I]: custo baixo (não exige ontologia formal); multilinguismo nativo por `prefLabel` com tag de idioma; mapeamentos declarados como dado, auditáveis.

Limitações [I]:
- `skos:broader` não é, por si, relação de subclasse lógica; usar SKOS como se fosse OWL leva a inferências indevidas — a própria especificação distingue os dois usos [F: w3c2009skos] [I].
- SKOS descreve a organização de conceitos, não a estrutura interna de uma competência (pré-requisitos, níveis de proficiência); para isso, é preciso CASE, CTDL-ASN ou modelagem própria.

## Exemplo técnico independente de domínio

```turtle
<https://exemplo/vocab/tipos-recurso> a skos:ConceptScheme ;
  skos:prefLabel "Tipos de recurso educacional"@pt-BR .

<https://exemplo/vocab/tipos-recurso/video> a skos:Concept ;
  skos:inScheme <https://exemplo/vocab/tipos-recurso> ;
  skos:prefLabel "vídeo"@pt-BR, "video"@en ;
  skos:broader <https://exemplo/vocab/tipos-recurso/audiovisual> ;
  skos:exactMatch <https://outro.exemplo/terms/Video> ;
  skos:closeMatch <https://terceiro.exemplo/terms/MovingImage> .
```

## Relações com outros conceitos

Complementa `iop.sem.interoperabilidade-semantica` e `iop.fund.mapeamento-e-proveniencia`. Os vocabulários de competência (`iop.comp.case`, `iop.comp.ctdl`, `iop.comp.esco`) e de metadados (`iop.md.dublin-core`, `iop.md.lrmi-schema-org`) são os candidatos naturais a publicação em SKOS.

RDF, OWL e modelagem de ontologias são tratados no domínio `grafo-conhecimento-educacional`; aqui o escopo é apenas o uso de SKOS como cola entre padrões de interoperabilidade.

## Lacunas e questões abertas

- SKOS-XL (rótulos como entidades) não coberto.
- Não foi verificado se ESCO e CASE publicam em SKOS, o que determinaria a viabilidade de um mapeamento declarativo entre eles.
- Falta um perfil mínimo de publicação de vocabulário para esta base (que propriedades exigir).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2009skos | normativo | 2026-10-29 |
| dcmi2026lrmi | normativo | 2026-10-29 |
| credengine2026ctdl | fornecedor | 2026-10-29 |
