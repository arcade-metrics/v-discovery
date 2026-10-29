---
id: adp.matriz-modelos
titulo: Matriz comparativa dos modelos de estudante
tipo: comparacao
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Matriz comparativa dos modelos de estudante

Síntese entre as três famílias de modelagem do domínio — knowledge tracing, teoria de resposta ao item/Elo e repetição espaçada — e os dois conceitos que as envolvem (learner model aberto, digital twin). Cada linha remete ao documento que fundamenta a comparação em detalhe; esta matriz não substitui as comparações internas de cada área (`adp.kt.comparison`, `adp.sr.comparison`), que trazem tabelas mais finas dentro de cada família.

## Modelos de estimação de domínio

| Critério | BKT | Modelos logísticos (AFM/PFA) | DKT | Sucessores atencionais (AKT) | IRT estático | Elo |
|---|---|---|---|---|---|---|
| O que representa | probabilidade discreta de domínio por KC (adp.kt.bayesian-knowledge-tracing) | logit de acerto como soma de efeitos por KC e prática (adp.kt.logistic-models) | vetor latente contínuo via RNN/LSTM (adp.kt.deep-knowledge-tracing) | estado ponderado por atenção sobre interações passadas (adp.kt.deep-kt-successors) | traço latente de habilidade, estático por aplicação (adp.irt.item-response-theory) | rating escalar atualizado a cada resposta (adp.irt.elo-rating) |
| Modela esquecimento? | não, por padrão (adp.sr.memory-and-forgetting) | parcialmente, via decaimento de oportunidades em variantes [I] | implicitamente, se o dado o contiver [I] | implicitamente [I] | não (instrumento estático) (adp.irt.item-response-theory) | parcialmente, via incerteza decrescente mas sem decaimento temporal explícito (adp.irt.elo-rating) |
| Dados mínimos exigidos | sequências por aluno e por KC, idealmente > 1 skill por item (adp.kt.bayesian-knowledge-tracing) | histórico de oportunidades por KC (adp.kt.logistic-models) | grandes volumes de sequências (milhares de alunos) (adp.kt.deep-knowledge-tracing) | grandes volumes, mais sensível a vazamento de avaliação (adp.kt.deep-kt-successors) | banco de itens calibrado, amostra para calibração (adp.irt.item-response-theory) | poucas dezenas de respostas por aluno (cold start mitigado) (adp.irt.elo-rating) |
| Interpretabilidade | alta (4 parâmetros com significado direto) (adp.kt.bayesian-knowledge-tracing) | alta (coeficientes de dificuldade e ganho) (adp.kt.logistic-models) | baixa (estado distribuído) (adp.kt.deep-knowledge-tracing) | baixa a média (pesos de atenção dão alguma leitura) (adp.kt.deep-kt-successors) | alta (parâmetros psicométricos padronizados) (adp.irt.item-response-theory) | alta (rating comparável a Elo de xadrez) (adp.irt.elo-rating) |
| Desempenho preditivo publicado (benchmarks independentes) | referência-base, competitivo em vários datasets (adp.kt.comparison) | Best-LR líder em 4 de 9 datasets no benchmark de Gervet et al. 2020 (adp.kt.comparison) | líder em 5 de 9 datasets no mesmo benchmark, mas ganho sobre BKT com esquecimento é pequeno (adp.kt.comparison, adp.sr.memory-and-forgetting) | SAKT e DKVMN ficam abaixo do DKT em reavaliação padronizada (pyKT); só AKT mantém ganho real e modesto (~0,01–0,03 AUC) (adp.kt.deep-kt-successors) | não comparável diretamente (tarefa estática, não sequencial) [I] | RMSE/AUC competitivos com BKT/PFA em dados reais (Papoušek, Pelánek & Stanislav 2014) (adp.irt.elo-rating) |
| Custo computacional | baixo [I] | baixo [I] | alto (treino de rede neural) [I] | alto [I] | baixo a médio (estimação por máxima verossimilhança) [I] | muito baixo (atualização online fechada) (adp.irt.elo-rating) |
| Utilidade pedagógica declarada | mastery learning, decisões de parada claras (adp.kt.bayesian-knowledge-tracing) | diagnóstico de KC problemático, usado em LFA (adp.id.knowledge-components) | menos direta, exige pós-processamento para decisão [I] | idem DKT [I] | seleção de item em CAT (adp.irt.item-response-theory) | seleção de item por dificuldade alvo, baixo custo de implantação (adp.irt.elo-rating) |
| Quando se justifica | poucos dados, necessidade de explicar a decisão a professor/aluno (OLM) [I] | quando dificuldade e taxa de aprendizado por KC interessam separadamente [I] | grande volume de dados, aceitação de caixa-preta, ganho real validado por re-benchmark [I] | mesmas condições do DKT, exigindo validação cuidadosa contra vazamento (adp.kt.deep-kt-successors) | avaliação pontual e comparável entre alunos (testes padronizados, CAT) (adp.irt.item-response-theory) | prática contínua com poucos dados por aluno/item, custo de implantação baixo (adp.irt.elo-rating) |

## Repetição espaçada

| Critério | Leitner / SM-2 | Half-Life Regression (HLR) | FSRS |
|---|---|---|---|
| Modelo de memória | caixas discretas / intervalo multiplicado por ease factor fixo (adp.sr.classical-algorithms) | meia-vida exponencial, função log-linear de features (adp.sr.half-life-regression) | DSR: dificuldade, estabilidade, retrievability, com reversão à média (adp.sr.fsrs) |
| Personalização | nenhuma (parâmetros fixos globais) (adp.sr.classical-algorithms) | por aluno/item, via features linearmente combinadas (adp.sr.half-life-regression) | por aluno (otimização dos 21 parâmetros sobre histórico individual) (adp.sr.fsrs) |
| Evidência publicada | amplamente implementado (Anki), mas baixo poder preditivo quando avaliado como modelo (adp.sr.classical-algorithms) | MAE 0,128 vs. 0,235 do Leitner no artigo original; reanálise posterior (Ilídio et al. 2026) encontra AUC perto do acaso (0,51) nos métodos originais (adp.sr.half-life-regression) | benchmark srs-benchmark favorável, mas mantido pelos próprios autores do algoritmo — sem avaliação independente localizada (adp.sr.fsrs) |
| Interpretabilidade | alta (regra simples e pública) (adp.sr.classical-algorithms) | média (pesos lineares por feature) (adp.sr.half-life-regression) | média a baixa (equações não lineares, 21 parâmetros) (adp.sr.fsrs) |
| Quando se justifica | ausência de dados de histórico, simplicidade de implantação [I] | quando há features ricas por item e é aceitável relação linear com o log da meia-vida [I] | quando há histórico de revisões suficiente por aluno para otimizar os parâmetros e se aceita dependência do mantenedor do benchmark [I] |

## Conceitos envolventes

| Critério | Open Learner Model | Learning Digital Twin |
|---|---|---|
| Natureza | learner model existente, exposto ao aluno/professor (adp.lm.open-learner-model) | metáfora emprestada da manufatura, aplicada (de forma majoritariamente conceitual) ao aluno (adp.dt.learning-digital-twin) |
| Maturidade | prática estabelecida, com frameworks (SMILI☺) e décadas de estudos (adp.lm.open-learner-model) | majoritariamente proposta de pesquisa futura; sem arquitetura de referência nem validação prospectiva publicada (adp.dt.learning-digital-twin) |
| O que a distinguiria de um learner model tradicional | já é, por definição, um learner model com interface de exposição [I] | integração multimodal contínua e capacidade de simulação what-if — nenhuma fonte aberta implementa e avalia isso [H] |

## Conclusão honesta

Nenhuma família domina em todas as dimensões. BKT e modelos logísticos seguem competitivos e mais interpretáveis; ganhos de modelos profundos sobre eles, quando avaliados com protocolo que evita vazamento de dados, são reais mas modestos (não os 4–6% anunciados nos artigos originais de alguns sucessores). Em repetição espaçada, o HLR original tem desempenho preditivo fraco quando reavaliado, e o FSRS carece de avaliação por terceiros independentes dos seus autores. "Learning digital twin" não é, hoje, uma categoria de modelo comparável às demais: é uma proposta conceitual sem implementação madura o bastante para entrar nesta matriz em pé de igualdade.
