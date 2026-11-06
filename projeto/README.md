# projeto/: fontes e insumos

Camada zero do repositório. Aqui ficam os documentos que **ninguém deste repositório escreveu** e a extração estruturada do que eles dizem.

**O produto VUOO é independente destes projetos** (decisão de 2026-11-05). As propostas de pesquisa (PIPE-TC, CCD) são **contexto e inspiração**: não definem requisito, escopo, prazo, métrica nem arquitetura do produto. Um insumo `IN-nn` só passa a valer para o produto quando uma decisão de produto (`D-nn`, `RN-nn`, `ADR-nn`) o adota explicitamente.

| Arquivo | O que é |
|---|---|
| `vuoo.md` | Proposta PIPE-TC Fase 2 (Wemoga + CIATec/CCD), texto integral. Ainda tem marcas `[PLACEHOLDER]` e `[REFERÊNCIA]` do original. |
| `ciatec.md` | Proposta do Centro de Ciência para o Desenvolvimento (CCD/FAPESP), texto integral. |
| `insumos.md` | Pontos extraídos das duas propostas (contexto, não restrição do produto), com código estável `IN-nn` e fonte de cada uma. Congelado em IN-01 a IN-35; novos entram a partir de IN-36. |

## As camadas do repositório e a regra contra redundância

```
projeto/        fontes primárias e insumos IN-nn           (contexto)
conhecimento/   base técnica agnóstica, ids estáveis        (conceito)
benchmarks/     estudos agnósticos de produtos existentes   (observação)
produtos/       decisões, regras e padrões de cada produto  (decisão)
```

A referência só desce: produtos cita conhecimento, benchmarks e projeto; conhecimento não cita produto nenhum (o validador de `conhecimento/_modelo/validar.py` proíbe); benchmarks não registram decisão de produto.

**Cada fato tem um dono, o resto aponta.**

- Um insumo de projeto existe uma vez, em `insumos.md`, com código `IN-nn`. Ele é contexto; só restringe o produto se uma decisão de produto o adotar.
- Um conceito técnico existe uma vez, em `conhecimento/`, com um id. Se dois domínios precisam dele, um é dono e o outro mantém um documento de redirecionamento com o id antigo.
- Uma decisão de produto existe uma vez, em `produtos/<slug>/`, com código `D-nn` (decisão) ou `RN-nn` (regra de negócio).
- Cópia de arquivo nunca. Quando um arquivo muda de lugar, todas as referências são atualizadas; não fica ponteiro nem nota de "movido de".

## Como citar

- Insumo: `[IN-17]`.
- Conceito: pelo id, por exemplo `iop.lr.xapi` ou `adp.kt.bayesian-knowledge-tracing`.
- Benchmark: pelo caminho, por exemplo `benchmarks/duolingo/01-recompensas.md §3`.
- Decisão: `D-20` com o slug do produto quando houver ambiguidade.
