---
id: iop.comp.ctdl
titulo: CTDL e CTDL-ASN (Credential Transparency Description Language)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [credengine2026ctdl, credentialengine2026ctdl, w3c2009skos, esco2026what, onedtech2025case]
relacoes:
  - { tipo: alternativa-a, alvo: iop.comp.case }
  - { tipo: complementa, alvo: iop.cred.open-badges }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: alternativa-a, alvo: iop.comp.esco }
  - { tipo: complementa, alvo: kg.curr.competency-frameworks }
  - { tipo: relacionado-a, alvo: kg.std.rdf }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [CTDL, CTDL-ASN, QData, Credential Engine, Credential Registry, Issuer Identity Registry, linked data, credencial, competência, learning and career pathway, transfer value, de facto standard]
---

# CTDL e CTDL-ASN

## Definição e terminologia

"The Credential Transparency Description Language (CTDL) is the family of de facto standards for making descriptions of credentials and other resources available as data for search and discovery and cross-system interoperability. You can think of the CTDL as a large dictionary of terms that is at your fingertips for creating descriptions where you can use all of the terms or only those terms that meet your needs" [F: credentialengine2026ctdl]. Foi criado pela Credential Engine [F: credengine2026ctdl].

O problema declarado: "Discovering and understanding credentials, competencies, and learning and career pathways is difficult. To fix this problem, we created the CTDL schema, a common language for any organization to use with their information systems to empower learners, workers, educators, employers, and policymakers" [F: credentialengine2026ctdl].

A família tem três esquemas [F: credengine2026ctdl]:

| Esquema | Objeto |
|---|---|
| CTDL | credenciais e recursos relacionados: oportunidades de aprendizagem, avaliações, trajetórias (*pathways*), valor de transferência |
| CTDL-ASN | competências: objetivos, habilidades e padrões acadêmicos, profissionais e ocupacionais |
| QData | dados numéricos e estatísticos, como taxas de conclusão e indicadores de emprego e renda |

Note-se a autodescrição: **família de padrões de facto**, não norma de organismo de padronização [F: credentialengine2026ctdl]. [I] Isso é relevante ao avaliar risco de adoção.

## Problema que resolve

Tornar comparáveis as credenciais oferecidas por milhares de instituições, com as competências que elas certificam e os resultados que produzem, informação que, sem padrão, existe apenas em prosa nos sites das instituições [I].

## Fundamentos e funcionamento

Segundo o mantenedor, "the power of the CTDL comes from every term having semantic meaning and from using a model based on specifications for the semantic web. This means that the CTDL is designed to include terms for linking data" [F: credentialengine2026ctdl]. A página descreve o modelo como baseado em especificações da web semântica, com estrutura de linked data, sem nomear RDF explicitamente [F: credengine2026ctdl].

A estrutura de dados ligados "enables telling complete stories to answer questions such as how much a credential cost, how long to earn it, requirements to enroll, courses that are required, transfer value, preparation for other credentials, jobs it prepares people for, pathway options, outcomes, and more" [F: credentialengine2026ctdl].

As ferramentas de publicação da Credential Engine produzem dados como *linked data* CTDL, publicados no **Credential Registry** como Linked Open Data; o Credential Finder usa CTDL para exibir os dados do registro [F: credengine2026ctdl]. O registro "hosts detailed information about credentials", e o **Issuer Identity Registry** "establishes a consistent and verifiable way to identify credential issuers so the data behind every credential stays trustworthy, no matter where it travels" [F: credentialengine2026ctdl].

A combinação relevante para a interoperabilidade [I]: CTDL-ASN descreve competências, CTDL descreve a credencial que as certifica, e Open Badges/CLR carregam a afirmação de que uma pessoa específica as possui (ver `iop.cred.open-badges`).

### Onde entra em um grafo educacional

[I] CTDL cobre a ponta da trajetória que nem CASE nem currículos nacionais cobrem: o que a aprendizagem vale fora da escola. Em um grafo que vai da habilidade curricular até a empregabilidade, as camadas se encaixam assim:

```
conceito curricular  →  competência  →  credencial  →  ocupação
   (BNCC, CASE)         (CASE, ESCO)      (CTDL)       (ESCO, CBO)
```

As perguntas que a lista do CTDL enumera (custo, tempo, requisitos de matrícula, cursos exigidos, valor de transferência, preparação para outras credenciais, empregos para os quais prepara) são exatamente as que um grafo curricular isolado não consegue responder [F: credentialengine2026ctdl].

## Requisitos e pressupostos

- Modelagem em linked data; o próprio mantenedor descreve o modelo como "based on specifications for the semantic web" [F: credentialengine2026ctdl]. A instituição publica no Credential Registry ou mantém sua própria publicação em linked data [I].
- O consumidor processa RDF/JSON-LD, ou usa as APIs do registro [I].
- Dependência de um mantenedor único (Credential Engine) e de um registro central.
- Contexto norte-americano. [I] O vocabulário foi desenhado em torno do ecossistema de credenciais dos EUA; a transposição para outros sistemas educacionais não é automática.

## Vantagens e limitações

Vantagens [I]: cobre credenciais, competências, trajetórias e dados quantitativos com um vocabulário só; desenhado para linked data desde o início e publicado como Linked Open Data, o que permite consulta federada; tem registro público associado; o escopo de perguntas que responde é amplo e documentado; alinhado com a prática de SKOS para esquemas de conceitos [F: w3c2009skos].

Limitações [I]:
- "De facto standards" é a caracterização do próprio mantenedor [F: credentialengine2026ctdl]: não é norma de organismo de normalização, diferentemente de IEEE ou W3C; mantenedor único.
- Centrado no mercado de credenciais dos Estados Unidos; a descrição de ocupações e resultados de emprego reflete esse contexto.
- Pouco aplicável à educação básica, onde o objeto não é credencial, e sim currículo (aí, CASE).
- A sobreposição com ESCO (competências) e CASE (frameworks) exige decisão de qual é a fonte de verdade para cada camada.

## Alternativas e comparações

| Necessidade | CTDL/CTDL-ASN | CASE | ESCO |
|---|---|---|---|
| Competências da educação básica | fraco | forte | fraco |
| Credenciais e qualificações | forte | não cobre | parcial |
| Ocupações e mercado de trabalho | forte | não cobre | forte |
| Jurisdição de referência | EUA | internacional | União Europeia |

Por camada, com os números e as fontes de cada vocabulário:

| Camada | CTDL | ESCO | CASE |
|---|---|---|---|
| Credencial | sim, é o foco [F: credentialengine2026ctdl] | qualificações [F: esco2026what] | não |
| Competência | sim [F: credentialengine2026ctdl] | sim, 13.939 [F: esco2026what] | sim, como `CFItem` [F: onedtech2025case] |
| Framework curricular | parcial | não | sim, é o foco [F: onedtech2025case] |
| Ocupação | ligada por "jobs it prepares people for" [F: credentialengine2026ctdl] | sim, 3.039 [F: esco2026what] | não |
| Trajetória (pathway) | sim [F: credentialengine2026ctdl] | não explicitamente | parcial, via `precedes` |
| Governança | Credential Engine, padrão de facto | Comissão Europeia, DG EMPL | 1EdTech, Final Release |
| Multilíngue | não verificado | 28 idiomas [F: esco2026what] | não aplicável |

Ver também `kg.voc.comparison`.

## Exemplo técnico independente de domínio

[I] Esquema de ligação entre as camadas, sem comprometer com os IRIs reais de nenhum dos vocabulários (não verificados):

```turtle
# a competência curricular própria alinha-se a uma competência de framework externo
ex:c/analise-de-dados skos:closeMatch <IRI-da-competencia-no-framework-externo> .

# a credencial declara exigir essa competência
ex:cred/tecnico-dados ex:exigeCompetencia ex:c/analise-de-dados .

# e prepara para ocupações
ex:cred/tecnico-dados ex:preparaPara <IRI-da-ocupacao> .
```

A tradução desse esquema para os termos reais do CTDL exige o dicionário de termos, que não foi consultado.

## Relações com outros conceitos

Alternativa a `iop.comp.case` conforme o domínio, e a `iop.comp.esco` no recorte de empregabilidade (ESCO é o equivalente europeu no eixo ocupacional); complementa `iop.cred.open-badges`; depende de `iop.sem.vocabularios-e-skos`. No domínio do grafo: complementa `kg.curr.competency-frameworks` e relaciona-se com `kg.std.rdf`.

## Lacunas e questões abertas

- O dicionário de termos do CTDL não foi aberto: as páginas consultadas são institucionais e descrevem o padrão, não o enumeram. Nenhum termo concreto do CTDL é citado neste documento, por isso. Namespaces (`ceterms:`, `ceasn:`) e URIs aparecem em resultados de busca mas não foram confirmados em página consultada diretamente (as tentativas resultaram em 403 e redirecionamentos).
- Não foi verificado se o CTDL publica ontologia OWL, contexto JSON-LD ou esquema SHACL.
- Versão e data do vocabulário corrente: não verificadas.
- Mapeamento declarado entre CTDL-ASN e CASE: não verificado. O site menciona também CTDL-VAT, uma ferramenta de avaliação de fornecedores, não examinada [F: credentialengine2026ctdl].
- A aplicabilidade ao sistema educacional brasileiro não foi avaliada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| credengine2026ctdl | fornecedor | 2026-10-29 |
| credentialengine2026ctdl | fornecedor | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
