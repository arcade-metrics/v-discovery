---
id: iop.lr.cmi5
titulo: cmi5
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [aicc2016cmi5, aicc2026cmi5web, adl2016xapidata]
relacoes:
  - { tipo: parte-de, alvo: iop.lr.xapi }
  - { tipo: alternativa-a, alvo: iop.tool.scorm }
  - { tipo: complementa, alvo: iop.tool.lti-core }
termos: [AU, assignable unit, moveOn, masteryScore, launch URL, fetch URL, auth token, sessão]
---

# cmi5

## Definição e terminologia

cmi5 é um perfil do xAPI que define como um LMS lança conteúdo e como esse conteúdo reporta progresso, acrescentando as regras que o xAPI deixa em aberto para o caso "conteúdo lançado por LMS" [F: aicc2026cmi5web].

A versão corrente consultada é **Quartz, 1st Edition, de 1 de junho de 2016**, descrita como a primeira versão de produção destinada a implementação [F: aicc2016cmi5; aicc2026cmi5web].

Termos:

- **AU** (*Assignable Unit*): a unidade de rastreio lançável.
- **Block**: agrupamento de AUs e de outros blocks.
- **Course**: a raiz da estrutura.
- **moveOn**: critério de satisfação de uma AU.

## Problema que resolve

O xAPI não define lançamento, sessão, autenticação nem critério de conclusão. Sem essas regras, dois conteúdos xAPI válidos reportam progresso de formas incompatíveis e nenhum LMS consegue decidir se a atividade foi concluída. cmi5 cobre justamente lançamento de conteúdo, autenticação, gestão de sessão, relato e estrutura de curso [F: aicc2026cmi5web]. A motivação declarada inclui substituir AICC e SCORM, cujo modelo de dados era "complicado demais" e com muitos elementos opcionais não usados [F: aicc2026cmi5web].

## Fundamentos e funcionamento

**Estrutura de curso.** Course exige `id` IRI globalmente único, `title` e `description` (langstrings). Block exige `id`, `title` e `description`, e pode referenciar objetivos. AU exige `id` (IRI), `title`, `description` e `url`; tem `launchMethod` ("OwnWindow" ou "AnyWindow", padrão "AnyWindow") e, opcionalmente, `masteryScore`, `moveOn`, `activityType`, `launchParameters` e `entitlementKey` [F: aicc2016cmi5].

**Lançamento.** O LMS acrescenta à URL da AU, com codificação de URL, os parâmetros: `endpoint` (URL do LRS para as requisições xAPI), `fetch` (URL de uso único, chamada por POST para obter o token), `actor` (objeto Agent xAPI, sem informação pessoal sensível), `registration` (UUID da inscrição no curso) e `activityId` (IRI da AU, que deve diferir do id de publicação da AU) [F: aicc2016cmi5].

**Autenticação.** A URL de `fetch` devolve JSON com a propriedade `auth-token` (HTTP 200, `application/json`). A AU envia o token no header Authorization, esquema Basic, em todas as chamadas xAPI seguintes. O token é limitado à sessão; chamadas repetidas de fetch devem retornar erro. Códigos de erro: `1` (já usado ou expirado), `2` (erro geral de segurança), `3` (erro geral de aplicação) [F: aicc2016cmi5].

**Verbos definidos pelo cmi5.** `launched`, `initialized`, `completed`, `passed`, `failed`, `abandoned`, `waived`, `terminated`, `satisfied` [F: aicc2016cmi5].

**moveOn.** Valores: `Passed`, `Completed`, `CompletedAndPassed`, `CompletedOrPassed`, `NotApplicable` [F: aicc2016cmi5].

**masteryScore.** Decimal de 0 a 1 inclusive, com até 4 casas. O LMS o passa à AU em tempo de execução; se a AU reporta score escalado, statements `passed` devem atingir ou superar o valor e `failed` devem ficar abaixo [F: aicc2016cmi5].

**Classificação de statements.** *cmi5 defined*: usam verbos cmi5, o activity id de categoria cmi5 e o template de contexto cmi5; seguem as regras de sessão e satisfação. *cmi5 allowed*: qualquer verbo, com o template de contexto cmi5 mas sem o id de categoria; devem ocorrer entre `initialized` e `terminated` e não entram na gestão de sessão nem na satisfação. *cmi5 not-allowed*: qualquer statement que não esteja conforme [F: aicc2016cmi5].

## Requisitos e pressupostos

- O LRS aceita token Basic emitido pelo LMS para o escopo da sessão.
- O conteúdo é lançado por um LMS que implementa cmi5 (não cobre uso autônomo, fora de lançamento).
- A AU é responsável por emitir `initialized` e `terminated`; sem eles, a janela de statements *allowed* não existe [I].

## Vantagens e limitações

Vantagens [I]: resolve o problema real de "quando a atividade terminou"; mantém a liberdade do xAPI para o que acontece dentro da sessão (statements *allowed*); conteúdo pode rodar fora do iframe do LMS, inclusive em aplicação nativa.

Limitações:
- A versão corrente é de 2016 [F: aicc2016cmi5] e foi escrita sobre xAPI 1.0.x; a compatibilidade com xAPI 2.0 não foi verificada [H].
- O token na sessão é Basic sobre um segredo emitido pelo LMS, não OAuth; o controle de escopo é do LRS, não do protocolo [I].
- Não cobre o caso de atividade iniciada pelo aluno fora do LMS [I].

## Alternativas e comparações

| Necessidade | cmi5 | xAPI puro | SCORM |
|---|---|---|---|
| Lançamento padronizado | sim | não | sim |
| Critério de conclusão | `moveOn` | não definido | `cmi.completion_status` |
| Liberdade de modelagem no meio da sessão | alta (*allowed*) | total | baixa |
| Conteúdo fora do navegador | sim | sim | não |

## Métricas e métodos de avaliação

Proporção de sessões com par `initialized`/`terminated` completo; proporção de AUs que satisfazem `moveOn` sem intervenção manual [I].

## Exemplo técnico independente de domínio

```
GET  https://conteudo.exemplo/au/17
       ?endpoint=https%3A%2F%2Flrs.exemplo%2Fxapi%2F
       &fetch=https%3A%2F%2Flms.exemplo%2Ffetch%2Fabc
       &actor=%7B%22account%22%3A...%7D
       &registration=0b1b...-uuid
       &activityId=http%3A%2F%2Fexemplo%2Fau%2F17

POST https://lms.exemplo/fetch/abc        ->  200 { "auth-token": "..." }
PUT  https://lrs.exemplo/xapi/statements  ->  launched, initialized, ... , terminated
```

## Relações com outros conceitos

É um perfil de `iop.lr.xapi` (relação `parte-de`), alternativa a `iop.tool.scorm` no mesmo papel e complementar a `iop.tool.lti-core`, que resolve o lançamento de *ferramentas* enquanto cmi5 resolve o lançamento de *conteúdo* [I].

## Lacunas e questões abertas

- Existe versão posterior a Quartz 1st Edition? A página do projeto não nomeia versão corrente [F: aicc2026cmi5web]; verificar no repositório do grupo de trabalho.
- Compatibilidade com xAPI 2.0 / IEEE 9274.1.1 não verificada.
- Interação entre cmi5 e LTI quando o conteúdo é lançado por uma ferramenta LTI: não documentada nas fontes consultadas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| aicc2016cmi5 | normativo | 2026-10-29 |
| aicc2026cmi5web | secundario | 2026-10-29 |
| adl2016xapidata | normativo | 2026-10-29 |
