---
id: iop.cred.open-badges
titulo: Open Badges 3.0
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2026ob30, w3c2025vcdm, imsglobal2025clr20]
relacoes:
  - { tipo: depende-de, alvo: iop.cred.verifiable-credentials }
  - { tipo: complementa, alvo: iop.cred.clr }
  - { tipo: complementa, alvo: iop.comp.case }
  - { tipo: relacionado-a, alvo: iop.fund.privacidade-e-seguranca }
termos: [badge, assertion, achievement, endorsement, baking, AchievementCredential]
---

# Open Badges 3.0

## Definição e terminologia

Open Badges é o padrão do 1EdTech para emissão de conquistas digitais verificáveis.

Versão consultada: **Open Badges Specification, Spec Version 3.0, Final Release (Document Version 1.4.5), emitida em 29 de junho de 2026** [F: imsglobal2026ob30].

**Modelo de dados** [F: imsglobal2026ob30]: o tipo principal é `AchievementCredential`, com classes de apoio como `Achievement`, `AchievementSubject`, `Profile` e `Alignment`; há também `EndorsementCredential`; as seções de exemplo e verificação referem-se a `OpenBadgeCredential`.

## Problema que resolve

Representar uma conquista — curso, competência, participação — de forma que o portador possa apresentá-la a qualquer terceiro e esse terceiro possa verificá-la sem depender do emissor [I].

## Fundamentos e funcionamento

**Relação com Verifiable Credentials.** A especificação se alinha às convenções do Verifiable Credentials Data Model v2.0 para *Defined Achievement Claims* e *Skill Claims*; uma Assertion passa a ser também uma Verifiable Credential, e credenciais podem ser agrupadas em Comprehensive Learner Records e em Verifiable Presentations. Os esquemas seguem o VCDM v2.0, com esquemas separados para credenciais que seguem o VCDM v1.1, e verificadores podem aceitar qualquer um dos dois [F: imsglobal2026ob30].

**Provas (§8).** Dois formatos: **JWT** (assinaturas VC-JWT), com passos para montar o header JOSE, o payload e a prova, e para verificar a credencial; e **Linked Data Proofs**, assinaturas embutidas, com passos de criação e verificação. A seção cobre também gestão de chaves e dereferenciamento de chave pública [F: imsglobal2026ob30, §8].

**Baking (§5.3).** A especificação cobre embutir os dados do badge em arquivos PNG e SVG, com procedimentos de *baking* e extração [F: imsglobal2026ob30, §5.3].

**API (§6) e segurança (§7).** A API REST inclui `getCredentials`, `upsertCredential`, `getProfile`, `putProfile` e um endpoint de descoberta de serviço; a segurança usa OAuth 2.0 Authorization Code Grant [F: imsglobal2026ob30, §6, §7].

## Requisitos e pressupostos

- O emissor mantém chaves e as publica de forma resolvível pelo verificador [I].
- O titular tem onde armazenar a credencial; o *baking* em PNG/SVG é o paliativo que permite circular a credencial como imagem [I].
- Para que o badge signifique algo comparável, o `Alignment` aponta para um identificador de competência externo (ver `iop.comp.case`) [I].

## Vantagens e limitações

Vantagens [I]: ecossistema consolidado de emissores e carteiras; a adoção do VCDM 2.0 traz verificação criptográfica sem depender do emissor; `EndorsementCredential` permite que terceiros respaldem uma conquista, o que ataca o problema de confiança no emissor.

Limitações [I]:
- Convivência de esquemas VCDM 1.1 e 2.0 [F: imsglobal2026ob30] aumenta o custo do verificador.
- Dois formatos de prova (JWT e Linked Data Proofs) significam que interoperar plenamente exige implementar ambos.
- Um badge isolado diz pouco: a comparabilidade depende do alinhamento a competências e da reputação do emissor [I].

## Alternativas e comparações

| Necessidade | Open Badges 3.0 | CLR 2.0 | VC genérica |
|---|---|---|---|
| Uma conquista | sim | sim, como item | sim |
| Conjunto de conquistas com relações | não | sim [F: imsglobal2025clr20] | não por si |
| Circular como imagem | sim (baking) | não | não |
| Vocabulário educacional | sim | sim | não |

## Relações com outros conceitos

Depende de `iop.cred.verifiable-credentials`. Complementa `iop.cred.clr` (a especificação do CLR descreve a definição de DC Assertion como compartilhada entre os dois [F: imsglobal2025clr20]) e `iop.comp.case`.

## Lacunas e questões abertas

- O changelog (seção G) não foi lido; as diferenças em relação a Open Badges 2.0 quanto a baking e API permanecem não verificadas.
- O documento tem mais de 700 mil caracteres e foi lido parcialmente; detalhes de `Achievement` e `Alignment` não foram verificados.
- Interoperabilidade real entre carteiras: não avaliada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2026ob30 | normativo | 2026-10-29 |
| w3c2025vcdm | normativo | 2026-10-29 |
| imsglobal2025clr20 | normativo | 2026-10-29 |
