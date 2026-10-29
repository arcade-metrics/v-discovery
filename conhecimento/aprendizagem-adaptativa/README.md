---
id: adp.index
titulo: Aprendizagem adaptativa e gêmeos digitais para aprendizagem
tipo: mapa
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Aprendizagem adaptativa e gêmeos digitais para aprendizagem

Base de conhecimento agnóstica sobre modelagem do conhecimento do estudante, aprendizagem adaptativa, repetição espaçada e gêmeos digitais de aprendizagem. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo e fontes prioritárias em [`00-brief.md`](00-brief.md).

## Como navegar

Comece pelo [mapa de conceitos](mapa-conceitos.md), que mostra as dependências entre documentos, e pelo [glossário](glossario.md). A [matriz comparativa](matriz-comparativa.md) resume os modelos lado a lado; o [mapa de evidências](mapa-evidencias.md) separa o que está empiricamente estabelecido do que é proposta ainda não validada. O [relatório](relatorio.md) registra cobertura, lacunas e próximos passos desta versão.

Leitura sugerida para quem chega sem contexto:

1. `instructional-design/kli-framework.md` e `instructional-design/knowledge-components.md`: o vocabulário comum (knowledge component) que todo modelo de aluno usa.
2. `learner-models/learner-model.md`: o que é um modelo de aluno e onde ele vive dentro de um sistema tutor.
3. `knowledge-tracing/comparison.md`: as quatro famílias de estimação de domínio (BKT, logístico, DKT, sucessores) e o que os benchmarks independentes de fato mostram.
4. `item-response/item-response-theory.md` e `item-response/elo-rating.md`: a tradição psicométrica e sua versão dinâmica e leve.
5. `spaced-repetition/memory-and-forgetting.md` e `spacing-and-testing-effects.md`: por que esquecimento importa, mesmo para quem só pensa em knowledge tracing.
6. `spaced-repetition/comparison.md`: Leitner/SM-2 × HLR × FSRS, sem presumir vencedor.
7. `adaptation/adaptive-learning-systems.md` e `sequencing-policies.md`: como tudo isso vira decisão de o que mostrar a seguir.
8. `digital-twins/learning-digital-twin.md`: a investigação crítica do termo que motivou este domínio — leia antes de usar a expressão "gêmeo digital" em qualquer contexto.
9. `evaluation/`: como saber se um modelo é bom (métricas, protocolos) e se o sistema funciona de fato (eficácia educacional, populações heterogêneas).

## Pastas

| Pasta | Conteúdo | Prefixo de id |
|---|---|---|
| `instructional-design/` | framework KLI, knowledge components, Learning Factors Analysis | `adp.id.*` |
| `learner-models/` | modelo de aluno, overlay model, open learner model | `adp.lm.*` |
| `knowledge-tracing/` | BKT, modelos logísticos (AFM/PFA), DKT, sucessores atencionais, comparação | `adp.kt.*` |
| `item-response/` | IRT (1PL/2PL/3PL, CAT), Elo aplicado a educação | `adp.irt.*` |
| `spaced-repetition/` | memória e esquecimento, efeitos de espaçamento e teste, Leitner/SM-2, HLR, FSRS, comparação | `adp.sr.*` |
| `adaptation/` | sistemas adaptativos, políticas de sequenciamento e seleção | `adp.adapt.*` |
| `digital-twins/` | origem do conceito, human digital twin, learning digital twin, arquitetura e validação | `adp.dt.*` |
| `evaluation/` | métricas preditivas, protocolos de validação, eficácia educacional, populações heterogêneas | `adp.eval.*` |

A lista completa de ids planejados está em [`_plano-ids.md`](_plano-ids.md). A área `assessment/` (evidence-centered design, stealth assessment) prevista no brief original ainda não foi escrita; ver `relatorio.md`.

## Convenções do domínio

- "Gêmeo digital de aprendizagem" é tratado como termo em disputa, não como fato consolidado: `digital-twins/learning-digital-twin.md` verifica, para cada fonte, se ela de fato propõe um gêmeo do aluno (e não de laboratório, equipamento ou campus) e se há implementação avaliada, não apenas arquitetura proposta.
- Nenhuma família de knowledge tracing é tratada como superior por padrão. Comparações exigem fonte de benchmark, de preferência independente dos autores do modelo avaliado (ver a ressalva recorrente sobre o FSRS, cujo benchmark público é mantido pelos próprios autores do algoritmo).
- Esquecimento é tratado como propriedade transversal: BKT clássico o ignora por construção, e isso é documentado como limitação, não omitido.
- Avaliar o MODELO (métricas preditivas, calibração) e avaliar a POLÍTICA ou o SISTEMA (eficácia educacional) são tratados como perguntas distintas, cada uma com seus próprios documentos em `evaluation/`.
