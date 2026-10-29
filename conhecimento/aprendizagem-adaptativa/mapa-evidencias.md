---
id: adp.evidencias
titulo: Mapa de evidências, limitações e lacunas de pesquisa
tipo: mapa
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Mapa de evidências, limitações e lacunas de pesquisa

Consolida, por área, o que está empiricamente estabelecido ([F] replicado e aberto à verificação), o que é hipótese ou proposta ainda não validada ([H]/conceitual), e o que a pesquisa aberta simplesmente não cobre. Não repete citações já detalhadas nos documentos; aponta para eles.

## O que está bem estabelecido

| Achado | Força da evidência | Documento |
|---|---|---|
| O efeito de espaçamento (massed vs. spaced) é real e replicado em centenas de experimentos | meta-análise de 317 experimentos, Cepeda et al. 2006 | adp.sr.spacing-and-testing-effects |
| O efeito de teste (retrieval practice > reestudo) se inverte com o intervalo de retenção | Roediger & Karpicke 2006; meta-análise Rowland 2014 (g=0,50) | adp.sr.spacing-and-testing-effects |
| A curva de esquecimento de Ebbinghaus tem forma replicável, embora o ajuste exponencial vs. potência ainda seja debatido | Murre & Dros 2015 (réplica de 2015) | adp.sr.memory-and-forgetting |
| BKT e modelos logísticos continuam competitivos com DKT em benchmarks independentes multi-dataset | Gervet et al. 2020, JEDM | adp.kt.comparison |
| Boa parte da vantagem do DKT sobre BKT em AUC desaparece quando o BKT é estendido para modelar esquecimento | Khajah, Lindsey & Mozer 2016 | adp.kt.deep-knowledge-tracing, adp.sr.memory-and-forgetting |
| Sucessores atencionais do DKT (SAKT, DKVMN) performam pior que o DKT quando reavaliados sob protocolo padronizado sem vazamento | pyKT (Liu et al. 2022); só AKT mantém ganho real | adp.kt.deep-kt-successors |
| Sistemas tutores inteligentes têm efeito positivo médio sobre instrução convencional, mas não superam tutoria humana individual | meta-análise Ma, Adesope, Nesbit & Liu 2014 (g=0,41 vs. não-ITS; g=-0,11 vs. humano) | adp.eval.educational-effectiveness |

## O que é hipótese, proposta conceitual ou decisão de engenharia ainda não validada

| Proposta | Status | Documento |
|---|---|---|
| "Learning digital twin" como categoria distinta de learner model | proposta de pesquisa futura na maior parte das fontes; nenhuma implementação avaliada prospectivamente localizada | adp.dt.learning-digital-twin |
| FSRS supera algoritmos clássicos de repetição espaçada em uso real | benchmark existente (srs-benchmark) é mantido pelos próprios autores do algoritmo; sem avaliação independente localizada | adp.sr.fsrs |
| Sequenciamento formulado como MDP/POMDP produz ganho consistente sobre heurísticas simples | revisão de Doroudi et al. 2019 encontra vantagem significativa em 21 de 36 estudos, com forte variação entre clusters metodológicos — não é um resultado único e consistente | adp.adapt.sequencing-policies |
| Half-Life Regression generaliza como preditor de retenção fora do corpus original | reanálise de Ilídio et al. 2026 encontra AUC próxima do acaso (0,51) para os métodos originais do HLR | adp.sr.half-life-regression |
| Arquiteturas e padrões de validação específicos para digital twins de aprendizagem | nenhum padrão equivalente ao ISO 23247 (manufatura) foi localizado para educação; tudo é proposta | adp.dt.architecture-and-validation |

## Lacunas de pesquisa (onde a literatura aberta é escassa ou ausente)

1. **Learning digital twin como sistema implementado e avaliado.** Nenhuma fonte aberta descreve um gêmeo digital do aluno com validação prospectiva (previsão registrada antes do desfecho observado). `adp.dt.learning-digital-twin`.
2. **Estudantes com necessidades educacionais específicas em sistemas adaptativos.** A pesquisa sobre fairness em knowledge tracing e learning analytics cobre atributos como urbanicidade, SES e língua; cobertura direta de deficiência é escassa, e nenhuma fonte conecta diretamente as diretrizes de Universal Design for Learning (CAST) a auditoria estatística de viés em modelos adaptativos. `adp.eval.heterogeneous-populations`.
3. **Avaliação independente do FSRS.** Todo benchmark público localizado é mantido pela mesma organização que desenvolve o algoritmo. `adp.sr.fsrs`.
4. **Incerteza da estimativa de estado do aluno.** Não foi localizada fonte verificável e específica sobre intervalos de confiança ou distribuições de incerteza para o estado inferido por um modelo de aluno (em oposição a point estimates como probabilidade de domínio). `adp.eval.predictive-metrics`.
5. **Combinação de evidence-centered design e stealth assessment com os modelos aqui descritos.** A área `assessment/` prevista no brief original não foi coberta nesta primeira versão (ver `relatorio.md`).
6. **Benchmarks de identifiability do BKT em dados reais de larga escala.** A degeneração de parâmetros é documentada analiticamente (van de Sande 2013), mas sem levantamento sistemático de sua frequência prática fora do artigo que a descreve. `adp.kt.bayesian-knowledge-tracing`.
7. **Ajuste dinâmico de dificuldade (DDA) fora de jogos.** Previsto no brief original (Hunicke 2005), não foi pesquisado nesta rodada; registrado como candidato para expansão.

## Inconsistências conhecidas entre documentos

- `adp.kt.comparison` e `adp.sr.memory-and-forgetting` convergem no mesmo achado (Khajah et al. 2016) a partir de ângulos diferentes (comparação de famílias de KT vs. papel do esquecimento); não é duplicação, é a mesma evidência suportando duas afirmações distintas e complementares.
- O documento de HLR (`adp.sr.half-life-regression`) relata desempenho forte no artigo original e desempenho fraco em reanálise posterior; isso é inconsistência real na literatura, preservada como tal, não uma escolha editorial.
