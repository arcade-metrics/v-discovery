---
id: kg.voc.comparison
titulo: Vocabulários educacionais, comparação
tipo: comparacao
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2020lom, dcmi2020terms, dcmi2026lrmi, schemaorg2026learningresource, schemaorg2026alignmentobject, onedtech2025case, ims2017case10, esco2026what, esco2026download, credentialengine2026ctdl, mec2026bncc, noy2001ontology101]
relacoes:
  - { tipo: relacionado-a, alvo: iop.md.ieee-lom }
  - { tipo: relacionado-a, alvo: iop.md.dublin-core }
  - { tipo: relacionado-a, alvo: iop.md.lrmi-schema-org }
  - { tipo: relacionado-a, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: iop.comp.esco }
  - { tipo: relacionado-a, alvo: iop.comp.ctdl }
  - { tipo: complementa, alvo: kg.mod.conceptual-model }
  - { tipo: relacionado-a, alvo: kg.std.comparison }
termos: [vocabulário, reuso, alinhamento, camada, recurso, competência, framework, credencial, ocupação, governança]
---

# Vocabulários educacionais, comparação

## Definição e terminologia

Este documento compara os vocabulários e especificações que descrevem entidades educacionais, para apoiar a decisão de **o que reusar e o que criar**. Noy e McGuinness colocam o reuso como segundo passo de qualquer desenvolvimento de ontologia: "it is almost always worth considering what someone else has done and checking if we can refine and extend existing sources for our particular domain and task", e o reuso pode ser requisito quando o sistema precisa interagir com aplicações já comprometidas com vocabulários particulares [F: noy2001ontology101, §3, Step 2].

## Problema que resolve

[I] Os vocabulários não competem; ocupam camadas diferentes. A confusão mais comum é escolher um e tentar esticá-lo para cobrir tudo — usar LOM para descrever competências, ou CASE para descrever recursos. A tabela de cobertura abaixo existe para tornar essa fronteira visível.

## Alternativas e comparações

### Cobertura por camada

| Vocabulário | Recurso | Competência | Framework curricular | Credencial | Ocupação | Aluno |
|---|---|---|---|---|---|---|
| Dublin Core / DCMI Terms | núcleo [F: dcmi2020terms] | não | não | não | não | não |
| LRMI | propriedades e concept schemes educacionais [F: dcmi2026lrmi] | como valor | não | não | não | não |
| IEEE LOM | exaustivo, 9 categorias [F: ieee2020lom] | só via `classification` | não | não | não | não |
| schema.org LearningResource | sim, com `teaches`/`assesses` [F: schemaorg2026learningresource] | referenciada, não definida | via `AlignmentObject` [F: schemaorg2026alignmentobject] | tangencia (`EducationalOccupationalCredential`, não verificado) | não | não |
| 1EdTech CASE | não | sim, `CFItem` [F: onedtech2025case] | sim, é o foco [F: onedtech2025case] | associável [F: onedtech2025case] | não | não |
| ESCO | não | sim, 13.939 [F: esco2026what] | não | qualificações [F: esco2026what] | sim, 3.039 [F: esco2026what] | não |
| CTDL | parcial | sim [F: credentialengine2026ctdl] | parcial | sim, é o foco [F: credentialengine2026ctdl] | ligada [F: credentialengine2026ctdl] | não |
| BNCC | não | competências e habilidades [F: mec2026bncc] | sim, para o Brasil [F: mec2026bncc] | não | não | não |

**Nenhum descreve o aluno.** [I] Essa é a lacuna estrutural do campo e a razão da recomendação de separar o grafo conceitual do modelo individual do aluno — ver kg.mod.layer-separation.

### Governança, formato e risco

| Vocabulário | Governança | Status | Formato nativo | Risco de adoção [I] |
|---|---|---|---|---|
| Dublin Core | DCMI Usage Board | DCMI Recommendation, 2020-01-20 [F: dcmi2020terms] | RDF | muito baixo |
| LRMI | LRMI Working Group (DCMI) | especificação DCMI [F: dcmi2026lrmi] | RDF, SKOS | baixo |
| IEEE LOM | IEEE C/LT | Active Standard, 2020-11-16 [F: ieee2020lom] | esquema conceitual; binding XML | médio: texto pago, sem binding RDF verificado |
| schema.org | consórcio aberto | vocabulário, release 30.1 [F: schemaorg2026learningresource] | RDF, usualmente JSON-LD | baixo, com ressalva da área "new" |
| CASE | 1EdTech | Final Release 1.1, 2025-01-24 [F: onedtech2025case] | JSON + REST | médio: sem contexto JSON-LD verificado |
| ESCO | Comissão Europeia, DG EMPL | v1.2.1, release v6.0.0, 2025-12-10 [F: esco2026what] | RDF, OWL, SKOS; downloads em RDF/TTL/JSON-LD e outros [F: esco2026download] | baixo, com dependência de versão externa |
| CTDL | Credential Engine | "family of de facto standards" [F: credentialengine2026ctdl] | linked data | médio: padrão de facto, mantenedor único |
| BNCC | MEC, Brasil | documento normativo, definido pela LDB [F: mec2026bncc] | PDF e planilha [F: mec2026bncc] | alto para máquinas: sem publicação em grafo verificada |

### Recomendação de uso combinado

[I] Recomendação deste documento, não das fontes. Para um grafo de conhecimento educacional em contexto brasileiro:

| Camada | Vocabulário | Papel |
|---|---|---|
| Descrição básica de recurso | Dublin Core / DCMI Terms | título, autoria, data, licença, idioma |
| Relação pedagógica do recurso | schema.org `teaches`, `assesses`, `competencyRequired` | ligar recurso a competência |
| Valores controlados pedagógicos | LRMI concept schemes | `learningResourceType`, `educationalUse` |
| Espinha curricular | SKOS próprio, alimentado pela BNCC | hierarquia, códigos, rótulos |
| Troca de frameworks | CASE | exportar e importar currículos entre sistemas |
| Ponte para empregabilidade | ESCO, por `skos:closeMatch` | quando o grafo chegar a educação profissional |
| Credenciais | CTDL | só se houver credenciamento no escopo |
| Pré-requisito, evidência, domínio | **vocabulário próprio** | nenhum padrão consultado cobre isso bem |

A última linha é a conclusão operacional desta comparação: **o que precisa ser criado é pequeno e bem delimitado** — pré-requisito com força e proveniência, evidência de aprendizagem, estado de domínio. Todo o resto se reusa. Ver kg.mod.conceptual-model.

## Métricas e métodos de avaliação

[I] Critérios para decidir reuso em um caso concreto: cobertura das competency questions pelo vocabulário candidato; estabilidade da governança; existência de binding RDF; custo de manter alinhamento quando a fonte externa versiona; e se a adoção é requisito de interoperabilidade com algum parceiro.

## Relações com outros conceitos

Relaciona-se com todos os documentos de `vocabularies/`, com kg.std.comparison (a escolha de camada técnica) e com kg.mod.conceptual-model (o que o modelo próprio precisa cobrir). Complementa kg.mod.conceptual-model.

## Lacunas e questões abertas

- Os textos integrais de IEEE LOM, do modelo de informação de CASE 1.1 e do dicionário de termos do CTDL não foram consultados; a comparação se apoia em resumos normativos e páginas de catálogo.
- `EducationalOccupationalCredential` de schema.org não foi verificado.
- Não foi verificada a existência de publicação da BNCC em formato de grafo. Ver kg.curr.bncc.
- Não há, entre as fontes consultadas, um crosswalk publicado entre BNCC e ESCO ou CASE.
- A linha "risco de adoção" é estimativa deste documento, sem base empírica.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ieee2020lom | normativo | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
| dcmi2026lrmi | normativo | 2026-10-29 |
| schemaorg2026learningresource | fornecedor | 2026-10-29 |
| schemaorg2026alignmentobject | fornecedor | 2026-10-29 |
| onedtech2025case | normativo | 2026-10-29 |
| ims2017case10 | normativo | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
| esco2026download | fornecedor | 2026-10-29 |
| credentialengine2026ctdl | fornecedor | 2026-10-29 |
| mec2026bncc | normativo | 2026-10-29 |
| noy2001ontology101 | academico | 2026-10-29 |
