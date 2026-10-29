---
id: iop.comp.case
titulo: CASE (Competencies and Academic Standards Exchange)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2017case, credengine2026ctdl]
relacoes:
  - { tipo: complementa, alvo: iop.md.lrmi-schema-org }
  - { tipo: alternativa-a, alvo: iop.comp.ctdl }
  - { tipo: complementa, alvo: iop.asmt.qti }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
termos: [competência, padrão curricular, framework, alinhamento, identificador referenciável]
---

# CASE

## Definição e terminologia

CASE é o serviço do 1EdTech para publicar e trocar competências e padrões curriculares em formato legível por máquina.

Versão consultada: **1EdTech Competencies and Academic Standards Exchange (CASE) Service Version 1.0, 1EdTech Final Release, emitida em 7 de julho de 2017** [F: imsglobal2017case].

## Problema que resolve

Padrões curriculares e competências são tipicamente publicados como PDF ou HTML, feitos para leitura humana. CASE substitui isso por definições legíveis por máquina "both syntactically and semantically", permitindo que sistemas troquem e administrem esses dados, apoiando alinhamentos comuns e fornecendo identificadores únicos referenciáveis para uso em certificados e históricos [F: imsglobal2017case].

Esse é o ponto de articulação de todo o domínio [I]: sem identificador estável de competência, o alinhamento de um recurso (`teaches`), de um item de avaliação e de um resultado de aluno não pode ser expresso de forma verificável — só como texto repetido em cada sistema.

## Fundamentos e funcionamento

O conjunto documental inclui um Information Model e um binding REST/JSON, publicados como documentos separados [F: imsglobal2017case].

O padrão de uso, derivado do problema declarado [I]: a autoridade curricular publica o framework uma vez, com identificadores; todos os demais sistemas referenciam esses identificadores em vez de copiar o texto do padrão. Mudanças no currículo passam a ser versionadas na origem.

## Requisitos e pressupostos

- Existe uma autoridade que publica o framework e mantém os identificadores estáveis ao longo das revisões curriculares [I].
- Os consumidores referenciam por identificador, e não por título ou código impresso [I].

## Vantagens e limitações

Vantagens [I]: resolve a camada semântica de currículo com um identificador referenciável; desenhado para ser citado por credenciais e históricos [F: imsglobal2017case].

Limitações [I]:
- A versão corrente é de 2017 [F: imsglobal2017case]; não foi verificado se há versão posterior.
- Exige um publicador institucional. Onde o currículo não é publicado em CASE — caso do Brasil, não verificado —, a adoção significa publicar o currículo você mesmo, assumindo papel de autoridade que não se tem.
- Não resolve equivalência entre frameworks diferentes; para isso, é preciso declarar correspondências (ver `iop.fund.mapeamento-e-proveniencia`).

## Alternativas e comparações

| Necessidade | CASE | CTDL-ASN | SKOS puro |
|---|---|---|---|
| Publicar framework curricular | sim | sim [F: credengine2026ctdl] | parcial |
| Serviço REST definido | sim | registro próprio | não |
| Foco | educação básica e currículo | credenciais e mercado de trabalho | genérico |
| Ecossistema | 1EdTech | Credential Engine | web semântica |

## Relações com outros conceitos

Complementa `iop.md.lrmi-schema-org` (fornece os identificadores que vão em `teaches`/`assesses`) e `iop.asmt.qti` (alinhamento de itens). Alternativa a `iop.comp.ctdl` conforme o domínio de uso. Depende de `iop.sem.vocabularios-e-skos`.

## Lacunas e questões abertas

- O Information Model não foi lido (as URLs tentadas retornaram 404 ou página vazia): classes (CFDocument, CFItem, CFAssociation, CFRubric, CFConcept) e o vocabulário de tipos de associação permanecem não verificados, embora sejam citados na literatura secundária.
- Existe CASE 1.1 ou 2.0? Não verificado.
- Há publicação da BNCC em CASE? Não verificado — questão central para uso no Brasil.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2017case | normativo | 2026-10-29 |
| credengine2026ctdl | fornecedor | 2026-10-29 |
