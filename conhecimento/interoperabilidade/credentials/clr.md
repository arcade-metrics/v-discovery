---
id: iop.cred.clr
titulo: Comprehensive Learner Record (CLR) 2.0
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2025clr20, imsglobal2026ob30, w3c2025vcdm]
relacoes:
  - { tipo: depende-de, alvo: iop.cred.verifiable-credentials }
  - { tipo: complementa, alvo: iop.cred.open-badges }
  - { tipo: complementa, alvo: iop.asmt.qti }
  - { tipo: relacionado-a, alvo: iop.comp.case }
termos: [CLR, ClrCredential, assertion, association, rubrica, ResultDescription]
---

# Comprehensive Learner Record 2.0

## Definição e terminologia

O CLR é o padrão do 1EdTech para criar, transmitir e renderizar o conjunto de conquistas de uma pessoa em formato legível por máquina, conversível em registros digitais verificáveis [F: imsglobal2025clr20].

Versão consultada: **Comprehensive Learner Record Standard Version 2.0, Final Release, Document Version 1.1, emitida em 14 de outubro de 2025** [F: imsglobal2025clr20].

**Modelo de dados** [F: imsglobal2025clr20]:

| Classe | Papel |
|---|---|
| `ClrCredential` | o registro de topo; a partir da 2.0, um CLR também é uma Verifiable Credential, com o publicador como emissor |
| `ClrSubject` | identifica o estudante, que deve ser o único sujeito da credencial |
| `Association` / `AssociationType` | relações entre assertions dentro do mesmo CLR |
| modelos compartilhados | `Achievement`, `AchievementCredential`, `Alignment`, `Result`, `ResultDescription`, `RubricCriterionLevel`, e enumerações como `AchievementType`, `ResultType`, `ResultStatusType` |

O conteúdo da claim é um conjunto de assertions, um conjunto opcional de definições de conquista e associações opcionais [F: imsglobal2025clr20].

## Problema que resolve

Um badge isolado não conta uma trajetória. O CLR representa o conjunto, com as relações entre as conquistas, e com resultados expressos em rubricas em vez de apenas uma nota [I].

## Fundamentos e funcionamento

**Rubricas.** Um `Result` pode registrar o nível de rubrica atingido, e um `ResultDescription` pode definir a rubrica, com níveis como "approaches", "meets" e "exceeds" [F: imsglobal2025clr20]. É o ponto em que o padrão de credenciais encontra a avaliação por critérios [I].

**Relação com Open Badges.** A definição de DC Assertion é compartilhada entre Open Badges 3.0 e CLR 2.0; um Open Badge é uma assertion única empacotada como credencial verificável, enquanto um CLR é uma coleção de assertions. O Implementation Guide do Open Badges 3.0 é listado como recurso companheiro para implementação e certificação [F: imsglobal2025clr20].

**Relação com Verifiable Credentials.** Os esquemas principais são baseados no VCDM v2.0, com esquemas compatíveis com v1.1 também fornecidos, e verificadores podem aceitar qualquer um [F: imsglobal2025clr20].

**API e provas.** Endpoints `getCredentials`, `upsertCredential`, `getProfile`, `putProfile` e `getServiceDescription`, com paginação e comportamento de retry; segurança por OAuth 2.0 Authorization Code Grant, com refresh, revogação de token e registro dinâmico de cliente; credenciais assinadas por JWT ou Linked Data Proof [F: imsglobal2025clr20].

## Requisitos e pressupostos

- Existe um publicador institucional que assume o papel de emissor do registro completo [F: imsglobal2025clr20] [I].
- As conquistas referenciam definições de competência estáveis, ou o registro vira uma lista de títulos [I].

## Vantagens e limitações

Vantagens [I]: representa trajetória, não eventos isolados; rubricas no modelo; mesma base de assertions do Open Badges, o que permite emitir badges individuais e o registro agregado sem modelos paralelos.

Limitações [I]:
- Exige maturidade institucional alta: emissor, chaves, carteira e política de registro.
- Sujeito único por credencial [F: imsglobal2025clr20] exige um CLR por estudante, com implicações operacionais de escala.
- Convivência VCDM 1.1/2.0, como no Open Badges.

## Alternativas e comparações

Ver a tabela em `iop.cred.open-badges`.

## Relações com outros conceitos

Depende de `iop.cred.verifiable-credentials`; complementa `iop.cred.open-badges` (assertions compartilhadas) e `iop.asmt.qti` (resultados e rubricas); relaciona-se a `iop.comp.case` para os alvos de alinhamento.

## Lacunas e questões abertas

- Documento extenso, lido parcialmente; o vocabulário completo de `AssociationType` não foi verificado.
- Relação entre CLR e histórico escolar oficial brasileiro: não avaliada.
- Requisitos de certificação do CLR 2.0: não verificados.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2025clr20 | normativo | 2026-10-29 |
| imsglobal2026ob30 | normativo | 2026-10-29 |
| w3c2025vcdm | normativo | 2026-10-29 |
