# projeto/: fontes e insumos

Camada zero do repositório. Aqui ficam os documentos que **ninguém deste repositório escreveu**, mas que restringem tudo o que se decide, e a extração estruturada do que eles dizem.

| Arquivo | O que é |
|---|---|
| `vuoo.md` | Proposta PIPE-TC Fase 2 (Wemoga + CIATec/CCD), texto integral. Ainda tem marcas `[PLACEHOLDER]` e `[REFERÊNCIA]` do original. |
| `ciatec.md` | Proposta do Centro de Ciência para o Desenvolvimento (CCD/FAPESP), texto integral. |
| `insumos.md` | Restrições extraídas das duas propostas, com código estável `IN-nn` e fonte de cada uma. Congelado em IN-01 a IN-35; novos entram a partir de IN-36. |

## As camadas do repositório e a regra contra redundância

```
projeto/        fontes primárias e insumos IN-nn           (fato de origem)
conhecimento/   base técnica agnóstica, ids estáveis        (conceito)
benchmarks/     estudos agnósticos de produtos existentes   (observação)
produtos/       decisões, regras e padrões de cada produto  (decisão)
```

A referência só desce: produtos cita conhecimento, benchmarks e projeto; conhecimento não cita produto nenhum (o validador de `conhecimento/_modelo/validar.py` proíbe); benchmarks não registram decisão de produto.

**Cada fato tem um dono, o resto aponta.**

- Uma restrição de projeto existe uma vez, em `insumos.md`, com código `IN-nn`.
- Um conceito técnico existe uma vez, em `conhecimento/`, com um id. Se dois domínios precisam dele, um é dono e o outro mantém um documento de redirecionamento com o id antigo.
- Uma decisão de produto existe uma vez, em `produtos/<slug>/`, com código `D-nn` (decisão) ou `RN-nn` (regra de negócio).
- Cópia de arquivo nunca: quando um arquivo muda de lugar, o caminho antigo vira um ponteiro curto dizendo para onde foi.

## Como citar

- Insumo: `[IN-17]`.
- Conceito: pelo id, por exemplo `iop.lr.xapi` ou `adp.kt.bayesian-knowledge-tracing`.
- Benchmark: pelo caminho, por exemplo `benchmarks/duolingo/01-recompensas.md §3`.
- Decisão: `D-20` com o slug do produto quando houver ambiguidade.
