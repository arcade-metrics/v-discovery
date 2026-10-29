---
id: kg.voc.ctdl
titulo: CTDL (Credential Transparency Description Language)
tipo: padrao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [credentialengine2026ctdl, esco2026what, onedtech2025case]
relacoes:
  - { tipo: parte-de, alvo: kg.voc.comparison }
  - { tipo: alternativa-a, alvo: kg.voc.esco }
  - { tipo: complementa, alvo: kg.curr.competency-frameworks }
  - { tipo: relacionado-a, alvo: kg.std.rdf }
termos: [CTDL, Credential Engine, Credential Registry, credencial, competência, learning and career pathway, transfer value, linked data, de facto standard]
---

# CTDL (Credential Transparency Description Language)

## Definição e terminologia

"The Credential Transparency Description Language (CTDL) is the family of de facto standards for making descriptions of credentials and other resources available as data for search and discovery and cross-system interoperability. You can think of the CTDL as a large dictionary of terms that is at your fingertips for creating descriptions where you can use all of the terms or only those terms that meet your needs" [F: credentialengine2026ctdl].

O problema declarado: "Discovering and understanding credentials, competencies, and learning and career pathways is difficult. To fix this problem, we created the CTDL schema, a common language for any organization to use with their information systems to empower learners, workers, educators, employers, and policymakers" [F: credentialengine2026ctdl].

Note-se a autodescrição: **família de padrões de facto**, não norma de organismo de padronização [F: credentialengine2026ctdl]. [I] Isso é relevante ao avaliar risco de adoção.

## Fundamentos e funcionamento

Segundo o mantenedor, "the power of the CTDL comes from every term having semantic meaning and from using a model based on specifications for the semantic web. This means that the CTDL is designed to include terms for linking data" [F: credentialengine2026ctdl].

A estrutura de dados ligados "enables telling complete stories to answer questions such as how much a credential cost, how long to earn it, requirements to enroll, courses that are required, transfer value, preparation for other credentials, jobs it prepares people for, pathway options, outcomes, and more" [F: credentialengine2026ctdl].

O Credential Engine mantém, além do CTDL, o **Credential Registry**, que "hosts detailed information about credentials", e o **Issuer Identity Registry**, que "establishes a consistent and verifiable way to identify credential issuers so the data behind every credential stays trustworthy, no matter where it travels" [F: credentialengine2026ctdl].

### Onde entra em um grafo educacional

[I] CTDL cobre a ponta da trajetória que nem CASE nem currículos nacionais cobrem: o que a aprendizagem vale fora da escola. Em um grafo que vai da habilidade curricular até a empregabilidade, as camadas se encaixam assim:

```
conceito curricular  →  competência  →  credencial  →  ocupação
   (BNCC, CASE)         (CASE, ESCO)      (CTDL)       (ESCO, CBO)
```

As perguntas que a lista do CTDL enumera — custo, tempo, requisitos de matrícula, cursos exigidos, valor de transferência, preparação para outras credenciais, empregos para os quais prepara — são exatamente as que um grafo curricular isolado não consegue responder [F: credentialengine2026ctdl].

## Requisitos e pressupostos

- Modelagem em linked data; o próprio mantenedor descreve o modelo como "based on specifications for the semantic web" [F: credentialengine2026ctdl].
- Dependência de um mantenedor único (Credential Engine) e de um registro central.
- Contexto norte-americano. [I] O vocabulário foi desenhado em torno do ecossistema de credenciais dos EUA; a transposição para outros sistemas educacionais não é automática.

## Vantagens e limitações

Vantagens: cobre credenciais, competências e trajetórias com um vocabulário só; desenhado para linked data desde o início; tem registro público associado; o escopo de perguntas que responde é amplo e documentado.

Limitações: padrão de facto, não norma; mantenedor único; forte viés para o sistema de credenciais dos EUA; e a sobreposição com ESCO (competências) e CASE (frameworks) exige decisão de qual é a fonte de verdade para cada camada. [I]

## Alternativas e comparações

| Camada | CTDL | ESCO | CASE |
|---|---|---|---|
| Credencial | sim, é o foco [F: credentialengine2026ctdl] | qualificações [F: esco2026what] | não |
| Competência | sim [F: credentialengine2026ctdl] | sim, 13.939 [F: esco2026what] | sim, como `CFItem` [F: onedtech2025case] |
| Framework curricular | parcial | não | sim, é o foco [F: onedtech2025case] |
| Ocupação | ligada por "jobs it prepares people for" [F: credentialengine2026ctdl] | sim, 3.039 [F: esco2026what] | não |
| Trajetória (pathway) | sim [F: credentialengine2026ctdl] | não explicitamente | parcial, via `precedes` |
| Governança | Credential Engine, padrão de facto | Comissão Europeia, DG EMPL | 1EdTech, Final Release |
| Multilíngue | não verificado | 28 idiomas [F: esco2026what] | não aplicável |

Ver kg.voc.comparison.

## Exemplo técnico independente de domínio

[I] Esquema de ligação entre as camadas, sem comprometer com os IRIs reais de nenhum dos vocabulários (não verificados nesta sessão):

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

Parte de kg.voc.comparison. Alternativa a kg.voc.esco no recorte de empregabilidade. Complementa kg.curr.competency-frameworks. Relaciona-se com kg.std.rdf.

## Lacunas e questões abertas

- O dicionário de termos do CTDL não foi aberto: a página consultada é institucional e descreve o padrão, não o enumera. Nenhum termo concreto do CTDL é citado neste documento, por isso.
- Não foi verificado se o CTDL publica ontologia OWL, contexto JSON-LD ou esquema SHACL.
- A relação entre CTDL, CTDL-ASN (que segundo o conhecimento geral do campo trata de padrões acadêmicos) e CASE não foi verificada; o site menciona CTDL-VAT, uma ferramenta de avaliação de fornecedores, mas as variantes do vocabulário não foram examinadas [F: credentialengine2026ctdl].
- A aplicabilidade ao sistema educacional brasileiro não foi avaliada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| credentialengine2026ctdl | fornecedor | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
