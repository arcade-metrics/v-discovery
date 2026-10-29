# VUOO · Produto (nível da plataforma)

Pasta do produto VUOO como um todo: gêmeo digital, grafo de conhecimento, VUOO Bot, micro-atividades, interface do professor, CMS e operação. Os estudos temáticos ficam em pastas irmãs com prefixo `vuoo-` (hoje, [`../vuoo-linguagem/`](../vuoo-linguagem/)), e esta pasta os cita em vez de repetir.

Criada em 29/10/2026 com a estrutura reservada e vazia. Preenche-se pelo pipeline das skills de produto (`.claude/skills/produto*`), nesta ordem, e só depois pelas regras e padrões.

```
produtos/vuoo/
  LEIAME.md          este arquivo
  00-brief.md        problema, público, hipóteses, riscos           (a escrever, skill produto-descoberta)
  01-contexto.md     alternativas e concorrentes                    (opcional; ver benchmarks/ e vuoo.md Tabelas 1 a 3)
  02-prd.md          jobs, fluxos, requisitos, métricas             (a escrever, skill produto-prd)
  03-mvp.md          corte de escopo, ordem por risco, aceite       (a escrever, skill produto-mvp)
  04-plano.md        arquitetura, dados, marcos, riscos técnicos    (a escrever, skill produto-plano)
  regras/            registro de regras de negócio RN-nn            (reservado)
  padroes/           registro de padrões de desenvolvimento ADR-nn  (reservado)
```

## O que já está decidido em outro lugar

| Onde | O quê |
|---|---|
| [`../../projeto/insumos.md`](../../projeto/insumos.md) | 35 restrições das propostas, IN-01 a IN-35 |
| [`../vuoo-linguagem/05-decisoes.md`](../vuoo-linguagem/05-decisoes.md) | 23 decisões de linguagem e gamificação, D-01 a D-23; as marcadas *invariante* são candidatas a regra de negócio |
| [`../vuoo-linguagem/99-pendencias.md`](../vuoo-linguagem/99-pendencias.md) | 34 pendências por responsável, P1 a P34 |
| [`../../projeto/vuoo.md`](../../projeto/vuoo.md) | Pacotes de pesquisa PP1 a PP5, fases F1.1 a F5.4, critérios de passagem, ética |

## Convenções desta pasta

- Cabeçalho YAML das skills (`produto`, `slug: vuoo`, `etapa`, `status`, `atualizado_em`).
- Marcas `[ASSUMIDO]`, `[A CONFIRMAR]`, `[HIP-n]` como no restante de `produtos/`.
- Toda regra e todo padrão citam: o insumo `IN-nn` que os origina, a decisão `D-nn` que os fixou e o id de `conhecimento/` que os embasa. Sem os três, o item fica marcado `[A CONFIRMAR]`.
