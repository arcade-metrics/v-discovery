---
id: lms.case.duolingo
titulo: Duolingo, estudo de caso (benchmark de referência)
tipo: estudo-de-caso
dominio: lms-e-plataformas
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: []
relacoes:
  - { tipo: relacionado-a, alvo: adp.sr.half-life-regression }
  - { tipo: relacionado-a, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: relacionado-a, alvo: lae.ind.engagement-indicators }
termos: [benchmark, teardown, ofensiva, liga, caminho, half-life regression, retenção]
---

# Duolingo, estudo de caso

## Definição e terminologia

Este documento é o registro, na base de conhecimento, do benchmark do Duolingo mantido em [`benchmarks/duolingo/`](../../../benchmarks/duolingo/) (raiz do repositório). O benchmark é o documento completo; este é só o ponto de entrada com id estável, para que outros documentos da base possam citá-lo por `lms.case.duolingo`.

O benchmark cobre o sistema de recompensas, o gameplay, o estilo (visual, personagens, movimento, som, tom de voz), a evidência disponível e as críticas, e uma leitura de risco por perfil de aluno da educação especial. Foi escrito como teardown de produto, em português, com 359 imagens indexadas e um índice de mecânicas em JSON.

## Por que fica fora do modelo documental

O benchmark usa marcas de confiança próprias (**[V]** verificado em fonte primária, **[S]** fonte secundária, **[I]** inferência), não as marcas `[F]`/`[I]`/`[H]` desta base; não tem frontmatter por documento nem chaves BibTeX; e carrega imagens e índices JSON. Convertê-lo ao modelo documental exigiria reescrever e perderia a estrutura de campos por mecânica, que é o que o torna comparável. A decisão (29/10/2026) foi mantê-lo íntegro em `benchmarks/` e registrá-lo aqui.

## O que o benchmark responde

| Pergunta | Onde |
|---|---|
| Por que o produto retém, e o que vale copiar | `benchmarks/duolingo/00-visao-geral.md` |
| Cada mecânica de recompensa, com números e críticas | `benchmarks/duolingo/01-recompensas.md` |
| Loop da lição, exercícios, caminho, adaptação, feedback | `benchmarks/duolingo/02-gameplay.md` |
| Paleta, tipografia, forma, personagens, animação, som, copy | `benchmarks/duolingo/03-estilo.md` |
| Força da evidência e críticas documentadas | `benchmarks/duolingo/04-evidencias-e-criticas.md` |
| Risco de cada mecânica por perfil de aluno | `benchmarks/duolingo/05-riscos-educacao-especial.md` |
| Glossário das mecânicas | `benchmarks/duolingo/00-visao-geral.md`, §4 |

## Limites conhecidos (resumo do README do benchmark)

- Os números do produto são, quase sempre, variações relativas de testes A/B, medidas com adolescentes e adultos, sobre retenção ou engajamento, não sobre aprendizagem; nenhum foi medido com crianças nem com alunos da educação especial.
- Não há teste de mão documentado do produto infantil nem da versão para escolas.
- Não há documentação oficial de sound design nem de durações de animação.
- O estado de referência é outubro de 2026; o produto muda continuamente.

## Relações com outros conceitos

O algoritmo de repetição espaçada do produto é tratado em `adp.sr.half-life-regression`; a adaptação de lição, em `adp.adapt.adaptive-learning-systems`; as métricas de retenção e engajamento usadas pelo produto, em `lae.ind.engagement-indicators`.

## Lacunas e questões abertas

- As afirmações do benchmark não estão ligadas a chaves da `bibliografia.bib`; as fontes estão listadas por URL em cada capítulo e em `benchmarks/duolingo/pesquisa/`. Se alguma afirmação precisar ser citada como `[F]` nesta base, a fonte primária deve entrar na bibliografia naquele momento.
- Os demais produtos previstos no brief deste domínio (plataformas adaptativas, jogos sérios com evidência regulatória) ainda não têm benchmark.

## Fontes

Nenhuma chave BibTeX: este documento não faz afirmação técnica própria. As fontes estão no benchmark.
