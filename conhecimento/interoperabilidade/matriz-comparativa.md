---
id: iop.matriz
titulo: Matriz comparativa por caso de uso
tipo: comparacao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2023xapi, imsglobal2020caliper, aicc2016cmi5, imsglobal2019lti13, imsglobal2019ltinrps, imsglobal2019ltiags, imsglobal2022oneroster, edfi2026datastandard, imsglobal2022qti30, imsglobal2017case, imsglobal2026ob30, imsglobal2025clr20, schemaorg2026learningresource, who2001icf]
relacoes:
  - { tipo: complementa, alvo: iop.catalogo }
  - { tipo: depende-de, alvo: iop.fund.dados-vs-protocolo }
  - { tipo: relacionado-a, alvo: iop.lr.comparison }
  - { tipo: relacionado-a, alvo: iop.ros.comparison }
  - { tipo: relacionado-a, alvo: iop.md.comparison }
termos: [caso de uso, sobreposição, complementaridade, escolha de padrão]
---

# Matriz comparativa por caso de uso

## Como usar

O catálogo (`iop.catalogo`) lista os padrões; esta matriz parte da pergunta prática. Cada linha é uma necessidade concreta; as colunas indicam o padrão principal, as alternativas e o que falta decidir depois de escolher.

## Matriz

| Necessidade | Padrão principal | Alternativas | O que ainda falta decidir |
|---|---|---|---|
| Registrar o que o aluno fez, em qualquer contexto | xAPI [F: ieee2023xapi] | Caliper | vocabulário de verbos e IRIs de atividade; política de identidade |
| Registrar telemetria de plataforma comparável entre fornecedores | Caliper 1.2 [F: imsglobal2020caliper] | xAPI com perfil | perfil aplicável; o que fazer com eventos fora dos perfis |
| Marcar conteúdo como concluído a partir de um LMS | cmi5 [F: aicc2016cmi5] | SCORM | `moveOn` e `masteryScore` por AU |
| Lançar ferramenta externa dentro do LMS | LTI 1.3 [F: imsglobal2019lti13] | integração própria | mapeamento de papéis; `deployment_id` por instalação |
| Ler a lista de participantes de uma turma no contexto do lançamento | LTI NRPS [F: imsglobal2019ltinrps] | OneRoster | consentimento para atributos pessoais |
| Devolver nota ao LMS | LTI AGS [F: imsglobal2019ltiags] | OneRoster Gradebook | escopos concedidos; granularidade do line item |
| Carregar turmas e matrículas em escala institucional | OneRoster 1.2 [F: imsglobal2022oneroster] | Ed-Fi, SIF | REST ou CSV; periodicidade; autoridade de `sourcedId` |
| Reunir dados escolares amplos para análise e política | Ed-Fi [F: edfi2026datastandard] | SIF | domínios necessários; política de extensões |
| Trocar itens e provas entre sistemas | QTI 3.0 [F: imsglobal2022qti30] | formato proprietário | perfil de interações suportadas |
| Referenciar competências e currículo | CASE [F: imsglobal2017case] | CTDL-ASN, SKOS próprio | quem publica o framework; versionamento |
| Descrever um recurso educacional para descoberta | schema.org/LearningResource [F: schemaorg2026learningresource] | IEEE LOM, Dublin Core | vocabulário dos valores educacionais |
| Emitir uma conquista verificável | Open Badges 3.0 [F: imsglobal2026ob30] | VC genérica | formato de prova; alinhamento a competência |
| Representar a trajetória completa de um estudante | CLR 2.0 [F: imsglobal2025clr20] | conjunto de badges | papel de emissor institucional; rubricas |
| Descrever funcionalidade e barreiras de forma comparável com saúde | CIF [F: who2001icf] | vocabulário próprio | quem codifica; base legal (dado sensível) |
| Cumprir obrigação nacional de dados de matrícula no Brasil | Educacenso | nenhuma | leiaute vigente do ano |

## Sobreposições reais

Os pares abaixo são confundidos com frequência. Em cada caso, a sobreposição é parcial [I]:

| Par | Sobrepõem em | Não sobrepõem em |
|---|---|---|
| xAPI × Caliper | registro de eventos de aprendizagem | xAPI cobre fora do navegador e vocabulário aberto; Caliper cobre perfis fechados e JSON-LD |
| LTI NRPS × OneRoster | saber quem está na turma | NRPS é consulta pontual e somente leitura no contexto do lançamento [F: imsglobal2019ltinrps]; OneRoster é carga institucional |
| LTI AGS × OneRoster Gradebook | nota | AGS é no contexto de uma ferramenta lançada; OneRoster é sincronização de gradebook |
| OneRoster × Ed-Fi | dados escolares | OneRoster cobre rostering; Ed-Fi cobre domínios amplos |
| CASE × CTDL-ASN | competências | CASE em currículo escolar; CTDL-ASN em credenciais e trabalho |
| Open Badges × CLR | credencial verificável | badge é uma assertion; CLR é a coleção com relações [F: imsglobal2025clr20] |
| LOM × LRMI | metadados educacionais | LOM em catálogo institucional; LRMI na web aberta |
| cmi5 × LTI | lançamento | cmi5 lança conteúdo; LTI lança ferramenta |

## Complementaridades que valem registrar

- LTI (lançamento) + Caliper (telemetria): os perfis Tool Launch e Tool Use do Caliper descrevem exatamente a atividade mediada por LTI [F: imsglobal2020caliper] [I].
- OneRoster (quem) + LTI (como entra) + xAPI ou Caliper (o que fez) + CASE (sobre o quê) + CLR (o que ficou registrado): é a cadeia completa, e cada elo é um padrão distinto [I].
- CEDS ou outro dicionário por baixo de qualquer padrão de intercâmbio: significado não vem junto com o transporte (ver `iop.sem.interoperabilidade-semantica`) [I].

## Lacunas e questões abertas

- A matriz não pondera adoção de mercado, que em muitos casos decide mais que a adequação técnica; faltam dados verificados.
- Nenhuma linha considera custo de implementação; seria necessário estimar por padrão.
- Casos de uso específicos de educação especial e acessibilidade (além de QTI e CIF) não estão cobertos.
