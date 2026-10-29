---
id: iop.comp.ctdl
titulo: CTDL e CTDL-ASN (Credential Engine)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [credengine2026ctdl, w3c2009skos]
relacoes:
  - { tipo: alternativa-a, alvo: iop.comp.case }
  - { tipo: complementa, alvo: iop.cred.open-badges }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: relacionado-a, alvo: iop.comp.esco }
termos: [CTDL, CTDL-ASN, QData, Credential Registry, linked data, competência]
---

# CTDL e CTDL-ASN

## Definição e terminologia

CTDL (*Credential Transparency Description Language*) é descrito pelo mantenedor como "the family of de facto standards for making descriptions of credentials and other resources available as data", servindo de vocabulário comum para busca, descoberta e interoperabilidade entre sistemas. Foi criado pela Credential Engine [F: credengine2026ctdl].

A família tem três esquemas [F: credengine2026ctdl]:

| Esquema | Objeto |
|---|---|
| CTDL | credenciais e recursos relacionados: oportunidades de aprendizagem, avaliações, trajetórias (*pathways*), valor de transferência |
| CTDL-ASN | competências: objetivos, habilidades e padrões acadêmicos, profissionais e ocupacionais |
| QData | dados numéricos e estatísticos, como taxas de conclusão e indicadores de emprego e renda |

## Problema que resolve

Tornar comparáveis as credenciais oferecidas por milhares de instituições, com as competências que elas certificam e os resultados que produzem — informação que, sem padrão, existe apenas em prosa nos sites das instituições [I].

## Fundamentos e funcionamento

As ferramentas de publicação da Credential Engine produzem dados como *linked data* CTDL, publicados no **Credential Registry** como Linked Open Data; o Credential Finder usa CTDL para exibir os dados do registro [F: credengine2026ctdl]. A página descreve o modelo como baseado em especificações da web semântica, com estrutura de linked data, sem nomear RDF explicitamente [F: credengine2026ctdl].

A combinação relevante para este domínio [I]: CTDL-ASN descreve competências, CTDL descreve a credencial que as certifica, e Open Badges/CLR carregam a afirmação de que uma pessoa específica as possui (ver `iop.cred.open-badges`).

## Requisitos e pressupostos

- A instituição publica no Credential Registry ou mantém sua própria publicação em linked data [I].
- O consumidor processa RDF/JSON-LD, ou usa as APIs do registro [I].

## Vantagens e limitações

Vantagens [I]: cobre credenciais, competências e dados quantitativos no mesmo modelo; publicado como linked data aberto, o que permite consulta federada; alinhado com a prática de SKOS para esquemas de conceitos [F: w3c2009skos] [I].

Limitações [I]:
- Centrado no mercado de credenciais dos Estados Unidos; a descrição de ocupações e resultados de emprego reflete esse contexto.
- "De facto standards" é a caracterização do próprio mantenedor [F: credengine2026ctdl]: não é norma de organismo de normalização, diferentemente de IEEE ou W3C.
- Pouco aplicável à educação básica, onde o objeto não é credencial, e sim currículo (aí, CASE).

## Alternativas e comparações

| Necessidade | CTDL/CTDL-ASN | CASE | ESCO |
|---|---|---|---|
| Competências da educação básica | fraco | forte | fraco |
| Credenciais e qualificações | forte | não cobre | parcial |
| Ocupações e mercado de trabalho | forte | não cobre | forte |
| Jurisdição de referência | EUA | internacional | União Europeia |

## Relações com outros conceitos

Alternativa a `iop.comp.case` conforme o domínio; complementa `iop.cred.open-badges`; relaciona-se a `iop.comp.esco` como equivalente europeu no eixo ocupacional.

## Lacunas e questões abertas

- Namespaces (`ceterms:`, `ceasn:`) e URIs aparecem em resultados de busca mas não foram confirmados em página consultada diretamente (as tentativas resultaram em 403 e redirecionamentos); ficam registrados como não verificados.
- Versão e data do vocabulário corrente: não verificadas.
- Mapeamento declarado entre CTDL-ASN e CASE: não verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| credengine2026ctdl | fornecedor | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
