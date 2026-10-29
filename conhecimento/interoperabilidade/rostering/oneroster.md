---
id: iop.ros.oneroster
titulo: OneRoster 1.2
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2022oneroster, imsglobal2019ltinrps]
relacoes:
  - { tipo: complementa, alvo: iop.tool.lti-advantage }
  - { tipo: alternativa-a, alvo: iop.ros.ed-fi }
  - { tipo: alternativa-a, alvo: iop.ros.sif }
  - { tipo: depende-de, alvo: iop.fund.identidade-e-contexto }
  - { tipo: relacionado-a, alvo: iop.ros.comparison }
termos: [rostering, sourcedId, lineItem, class, enrollment, academicSession, CSV binding, ARP]
---

# OneRoster 1.2

## Definição e terminologia

OneRoster é o padrão do 1EdTech para intercâmbio de turmas, pessoas, matrículas e notas entre o sistema de informação escolar e as aplicações que a escola usa.

Versão consultada: **OneRoster Version 1.2, IMS Final Release, Document Version 2, emitida em 19 de setembro de 2022**, disponibilizada para adoção pela comunidade [F: imsglobal2022oneroster].

**Conjunto documental** [F: imsglobal2022oneroster]: Rostering Service (Information Model e REST Binding); Gradebook Service (Information Model e REST Binding) mais o IMS Assessment Results Profile (ARP); Resource Service (Information Model e REST Binding); CSV Binding; Implementation Guide e Conformance and Certification Guide.

## Problema que resolve

Toda aplicação educacional precisa saber quem está em qual turma. Sem padrão, cada fornecedor recebe uma planilha com formato próprio, por e-mail, uma vez por bimestre [I].

## Fundamentos e funcionamento

**Entidades.** Pessoas, cursos, matrículas e notas; rosters de turma, itens de gradebook (results, lineItems, categories) e recursos [F: imsglobal2022oneroster].

**Famílias de serviço.** Rostering, Gradebook e Resource [F: imsglobal2022oneroster].

**Bindings.** REST e CSV [F: imsglobal2022oneroster]. O binding CSV é o que torna o padrão viável em redes onde o sistema de origem não expõe API — é uma troca em lote, não em tempo real [I].

**Identidade.** Cada entidade tem um `sourcedId` atribuído pelo sistema de origem (ver `iop.fund.identidade-e-contexto`).

## Requisitos e pressupostos

- Existe um sistema de origem único e autoritativo para matrícula. Com duas fontes, `sourcedId` deixa de ser chave confiável [I].
- Para o binding REST, o provedor expõe API autenticada; para o CSV, há processo operacional de geração e ingestão com periodicidade acordada [I].

## Vantagens e limitações

Vantagens [I]: escopo bem delimitado (rostering, nota e recurso), o que torna a implementação viável; o binding CSV reduz a barreira de entrada para redes públicas; separa o problema de "quem está na turma" do problema de "como lanço a ferramenta" (LTI).

Limitações [I]:
- Modelo de dados escolar mínimo: não cobre frequência, disciplina, programas, avaliação externa nem finanças — para isso, Ed-Fi ou SIF (ver `iop.ros.comparison`).
- Troca em lote via CSV implica dados defasados entre sincronizações.
- Não modela competências nem currículo (ver `iop.comp.case`).

## Alternativas e comparações

| Necessidade | OneRoster | LTI NRPS | Ed-Fi |
|---|---|---|---|
| Carga institucional de turmas | sim | não | sim |
| Lista de membros no contexto de um lançamento | não | sim [F: imsglobal2019ltinrps] | não |
| Dados escolares amplos | não | não | sim |
| Troca sem API (arquivo) | sim (CSV) | não | não |

## Métricas e métodos de avaliação

Conformidade pelo Conformance and Certification Guide do conjunto [F: imsglobal2022oneroster]. Em operação: defasagem entre a matrícula real e a refletida na aplicação; taxa de registros rejeitados por `sourcedId` desconhecido [I].

## Exemplo técnico independente de domínio

```
GET /ims/oneroster/rostering/v1p2/classes/{sourcedId}/students
GET /ims/oneroster/gradebook/v1p2/classes/{sourcedId}/lineItems

CSV binding (lote):  orgs.csv, academicSessions.csv, courses.csv,
                     classes.csv, users.csv, enrollments.csv
```

Nomes de endpoint ilustrativos: a estrutura exata do binding REST não foi lida nesta rodada [I].

## Relações com outros conceitos

Complementa `iop.tool.lti-advantage`: OneRoster faz a carga institucional, NRPS responde a consulta pontual no contexto de um lançamento. Alternativa a `iop.ros.ed-fi` e `iop.ros.sif` para intercâmbio de dados escolares, com escopo menor.

## Lacunas e questões abertas

- Os documentos de REST binding não foram lidos (URLs tentadas retornaram 404): endpoints, escopos OAuth 2 e semântica de paginação permanecem não verificados.
- O Assessment Results Profile (ARP) merece documento próprio; relação com QTI Results Reporting não verificada.
- Adoção do OneRoster no Brasil: não verificada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2022oneroster | normativo | 2026-10-29 |
| imsglobal2019ltinrps | normativo | 2026-10-29 |
