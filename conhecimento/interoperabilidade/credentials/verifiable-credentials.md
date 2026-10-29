---
id: iop.cred.verifiable-credentials
titulo: W3C Verifiable Credentials Data Model 2.0
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2025vcdm, imsglobal2026ob30, imsglobal2025clr20]
relacoes:
  - { tipo: especificado-por, alvo: iop.cred.open-badges }
  - { tipo: complementa, alvo: iop.cred.clr }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: relacionado-a, alvo: iop.fund.privacidade-e-seguranca }
termos: [credencial verificável, emissor, titular, verificador, apresentação verificável, prova, proof]
---

# Verifiable Credentials Data Model 2.0

## Definição e terminologia

O Verifiable Credentials Data Model (VCDM) é o modelo do W3C para credenciais digitais cuja autoria pode ser verificada criptograficamente. É **W3C Recommendation, publicada em 15 de maio de 2025**, produzida pelo Verifiable Credentials Working Group [F: w3c2025vcdm].

Conceitos centrais [F: w3c2025vcdm]:

- **Claim**: afirmação sobre um sujeito, expressa como relação sujeito-propriedade-valor.
- **Credential**: uma ou mais claims da mesma entidade, mais metadados como emissor, período de validade e informação de status.
- **Verifiable credential**: credencial à prova de adulteração, com autoria verificável criptograficamente; a propriedade `proof` aponta para um grafo de prova separado.
- **Presentation** e **verifiable presentation**: dados derivados de uma ou mais credenciais, compartilhados com um verificador específico.

**Papéis** [F: w3c2025vcdm]: **issuer** (afirma claims e emite a credencial para o titular), **holder** (possui credenciais e gera apresentações; frequentemente, mas nem sempre, é o sujeito), **verifier** (recebe e verifica), além de *subject* e *verifiable data registry*.

## Problema que resolve

Permitir que uma afirmação sobre uma pessoa (concluiu um curso, domina uma competência) seja verificável por qualquer terceiro, sem consultar o emissor e sem que o emissor saiba quando e onde a credencial foi apresentada [I].

## Fundamentos e funcionamento

**Segurança.** Um documento conforme deve ser protegido por ao menos um mecanismo. A especificação ilustra dois [F: w3c2025vcdm]: prova **embutida**, baseada em Verifiable Credential Data Integrity 1.0, em que a prova é um grafo nomeado referenciado pela propriedade `proof`; e prova **envelopante**, baseada em Securing Verifiable Credentials using JOSE and COSE, em que o payload é encapsulado e assinado.

**Contexto.** Credenciais e apresentações devem incluir a propriedade `@context`, cujo primeiro item deve ser a URL `https://www.w3.org/ns/credentials/v2`; os itens seguintes podem ser URLs ou objetos de contexto JSON-LD [F: w3c2025vcdm].

**Uso em educação.** Open Badges 3.0 alinha-se às convenções do VCDM v2.0, e uma Assertion passa a ser também uma Verifiable Credential [F: imsglobal2026ob30]. No CLR 2.0, a partir da versão 2.0 um CLR também é uma Verifiable Credential, com o publicador como emissor [F: imsglobal2025clr20]. Ambas as especificações fornecem esquemas para VCDM v2.0 e, em paralelo, esquemas compatíveis com VCDM v1.1, e permitem que verificadores aceitem qualquer um dos dois [F: imsglobal2026ob30; imsglobal2025clr20].

## Requisitos e pressupostos

- O verificador consegue resolver a chave pública do emissor por um meio confiável.
- O titular tem onde guardar a credencial (carteira digital) e controla quando apresentá-la [I].
- O emissor mantém mecanismo de status (revogação) ao longo da vida útil da credencial [I].

## Vantagens e limitações

Vantagens [I]: separa o modelo de dados do mecanismo de assinatura, o que permite evoluir criptografia sem mudar o modelo; coloca o titular no centro do fluxo de apresentação, com ganho direto de privacidade; é Recommendation do W3C, não especificação de consórcio setorial.

Limitações [I]:
- Exige infraestrutura de chaves e de carteiras que, na educação básica pública, não existe.
- A convivência entre VCDM 1.1 e 2.0 nos esquemas de Open Badges e CLR [F: imsglobal2026ob30] transfere para o verificador o custo de aceitar os dois.
- Revogação e status permanecem a parte operacionalmente mais difícil [I].

## Alternativas e comparações

| Abordagem | Verificação | Dependência do emissor online |
|---|---|---|
| PDF assinado | manual ou por software de assinatura | não, mas sem modelo de dados |
| Consulta à API do emissor | sim | total |
| Verifiable Credential | criptográfica, por terceiro | só para status/revogação |

## Relações com outros conceitos

É a base de `iop.cred.open-badges` e `iop.cred.clr`. Relaciona-se a `iop.fund.privacidade-e-seguranca`.

## Lacunas e questões abertas

- As especificações de securing (VC-JOSE-COSE e Data Integrity) não foram consultadas; os detalhes de assinatura permanecem não verificados.
- Mecanismos de status/revogação (StatusList) não consultados.
- Aplicabilidade no Brasil (relação com ICP-Brasil e com certificados de conclusão oficiais): não avaliada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2025vcdm | normativo | 2026-10-29 |
| imsglobal2026ob30 | normativo | 2026-10-29 |
| imsglobal2025clr20 | normativo | 2026-10-29 |
