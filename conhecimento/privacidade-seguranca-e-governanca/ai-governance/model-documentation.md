---
id: psg.ai.model-documentation
titulo: Model cards, datasheets e documentação de modelos de aprendizagem
tipo: padrao
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [mitchell2019modelcards, gebru2021datasheets, eu2024aiact, nist2023airmf, khosravi2022explainable]
relacoes:
  - { tipo: parte-de, alvo: psg.ai.ai-governance-frameworks }
  - { tipo: complementa, alvo: psg.ai.transparency-and-human-oversight }
  - { tipo: complementa, alvo: dat.rd.data-documentation }
  - { tipo: complementa, alvo: lae.dq.provenance-and-lineage }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: avaliado-por, alvo: adp.eval.heterogeneous-populations }
  - { tipo: avaliado-por, alvo: lae.psy.fairness-in-measurement }
  - { tipo: relacionado-a, alvo: psg.ai.eu-ai-act-and-brazil }
termos: [model card, datasheet for datasets, avaliação desagregada, análise interseccional, uso pretendido, uso fora de escopo, instruções de uso, limiar de decisão, documentação de modelo]
---

# Model cards, datasheets e documentação de modelos de aprendizagem

## Definição e terminologia

**Model cards** são "short documents accompanying trained machine learning models that provide benchmarked evaluation in a variety of conditions", incluindo grupos culturais, demográficos e interseccionais relevantes para o domínio de aplicação, e que declaram o contexto de uso pretendido e o procedimento de avaliação [F: mitchell2019modelcards, Abstract]. **Datasheets for datasets** documentam a motivação, composição, processo de coleta, usos recomendados e demais aspectos de um conjunto de dados, por analogia às folhas de dados de componentes eletrônicos [F: gebru2021datasheets, §1]. Os dois são complementares: o datasheet descreve os dados que alimentam o modelo; o model card, o modelo treinado [F: mitchell2019modelcards, §1].

O que não é: documentação de modelo não é a explicação de uma decisão individual (`psg.ai.transparency-and-human-oversight`), não é a trilha de auditoria (`psg.audit.audit-trails`) nem a documentação de dados de pesquisa em geral, que fica em `dat.rd.data-documentation`. Aqui o foco é o modelo de aprendizagem que decide ou recomenda sobre alunos.

## Problema que resolve

Os autores dos model cards apontam a ausência de "standardized documentation procedures" para comunicar características de desempenho de modelos, problema mais grave em aplicações de alto impacto, entre as quais citam educação [F: mitchell2019modelcards, §1]. Para o datasheet, o problema é o descompasso entre o contexto de implantação e os dados de treino ou avaliação, ou dados que refletem vieses sociais indesejados [F: gebru2021datasheets, §1]. No regime regulatório, a mesma necessidade aparece como dever: o MAP 2.2 do NIST pede documentar limites de conhecimento e como a saída pode ser supervisionada [F: nist2023airmf, Tabela 2], o MEASURE 2.9 pede que o modelo seja "explained, validated, and documented" [F: nist2023airmf, Tabela 3], e o AI Act exige instruções de uso para sistemas de alto risco [F: eu2024aiact, art. 13(2)].

## Fundamentos e funcionamento

### Seções de um model card

Mitchell et al. propõem nove seções [F: mitchell2019modelcards, Fig. 1, §4]:

1. **Model details**: quem desenvolveu, data, versão, tipo, algoritmo, restrições de equidade aplicadas, licença, contato.
2. **Intended use**: usos e usuários primários e **usos fora de escopo**.
3. **Factors**: grupos, condições ambientais, atributos técnicos relevantes e os usados na avaliação.
4. **Metrics**: medidas de desempenho, **limiares de decisão**, formas de estimar variação.
5. **Evaluation data** e 6. **Training data**: conjuntos, motivação, pré-processamento; se o treino for proprietário, ao menos a distribuição sobre grupos.
7. **Quantitative analyses**: resultados unitários e interseccionais.
8. **Ethical considerations** e 9. **Caveats and recommendations**.

Os autores defendem métricas "broken down by individual cultural, demographic, or phenotypic groups, domain-relevant conditions, and intersectional analysis" [F: mitchell2019modelcards, §1] e afirmam que a seção de detalhes "should not be seen as a requirement to compromise private information or reveal proprietary training techniques" [F: mitchell2019modelcards, §4.1]. Sugerem também mecanismos como privacidade diferencial para que indivíduos do conjunto de teste não sejam identificáveis por suas características [F: mitchell2019modelcards, §3].

### Perguntas de um datasheet

O datasheet organiza perguntas em sete seções: motivação, composição, processo de coleta, pré-processamento e rotulagem, usos, distribuição e manutenção [F: gebru2021datasheets, §3]. Perguntas com impacto direto em dados de menores: se o conjunto identifica subpopulações (por exemplo idade e gênero) e como; se contém dados sensíveis; se os indivíduos consentiram, como, e se receberam "a mechanism to revoke their consent"; e se houve análise de impacto sobre os titulares, "e.g., a data protection impact analysis" [F: gebru2021datasheets, §3.2, §3.3]. Os autores insistem que o processo "is not intended to be automated", porque o objetivo é provocar reflexão de quem cria o conjunto [F: gebru2021datasheets, §1.1].

### Instruções de uso do AI Act como documentação exigível

O art. 13(3) do AI Act lista o conteúdo mínimo das instruções de uso: identidade do provider; finalidade; acurácia com suas métricas e circunstâncias que a afetam; riscos previsíveis; capacidades de explicar a saída; desempenho por pessoas ou grupos; especificações dos dados de entrada e informação sobre dados de treino, validação e teste; mudanças pré-determinadas; medidas de supervisão humana; recursos e vida útil; e mecanismos de coleta e interpretação de logs [F: eu2024aiact, art. 13(3)]. [I] O model card cobre quase todos esses itens; faltam-lhe tipicamente vida útil, manutenção, logs e medidas de supervisão, que precisam ser acrescentados quando o card serve de base às instruções de uso.

## Requisitos e pressupostos

- Versionamento: um card por versão do modelo; para dados dinâmicos, os autores do datasheet recomendam acompanhar versões atualizadas com datasheets atualizados [F: gebru2021datasheets, §4].
- Dados de grupo para avaliação desagregada, que podem não existir justamente por proteção de dados [F: gebru2021datasheets, §4]; em educação especial, atributos de deficiência são dado sensível de saúde, e o uso para avaliação exige base legal própria (`psg.legal.lgpd-children`) [I].
- Proveniência dos dados de treino e avaliação (`lae.dq.provenance-and-lineage`) [I].

## Vantagens e limitações

Vantagens: tornam explícitos uso pretendido e fora de escopo, o que limita reaproveitamento indevido (por exemplo, usar um modelo de recomendação para nota ou retenção) [I]; preparam o RIPD e as instruções de uso; permitem comparar modelos [F: mitchell2019modelcards, §3]. Limitações declaradas pelos próprios autores: a utilidade depende "on the integrity of the creator(s) of the card", não é provável padronizar o card a ponto de impedir representações enganosas, e ele é "one transparency tool among many", ao lado de auditoria por terceiros e testes adversariais [F: mitchell2019modelcards, §6]. Datasheets "do not provide a complete solution" para vieses e danos, e o criador não antecipa todos os usos [F: gebru2021datasheets, §4]. Em educação, há ainda o risco de documentar modelos complexos onde um interpretável teria desempenho comparável [F: khosravi2022explainable, §3.5].

## Alternativas e comparações

| Artefato | Objeto | Público principal | Obrigatório? |
|---|---|---|---|
| Datasheet | conjunto de dados | quem escolhe ou reutiliza dados | não (prática) |
| Model card | modelo treinado | quem adota, supervisiona ou é afetado | não (prática) |
| Instruções de uso (AI Act art. 13) | sistema de alto risco | deployer | sim, na UE, para alto risco |
| Avaliação desagregada por grupo | desempenho | avaliador, auditor | exigida em parte por art. 13(3)(b)(v) |

## Métricas e métodos de avaliação

Completude: proporção das seções preenchidas e itens do art. 13(3) cobertos [I]. Atualidade: defasagem entre a versão em produção e a versão documentada [I]. Utilidade: teste com professores e gestores verificando se, só com o card, identificam usos fora de escopo e limites [I]. A avaliação desagregada em si pertence a `adp.eval.heterogeneous-populations` e `lae.psy.fairness-in-measurement`.

## Exemplo técnico independente de domínio

```
model_card:
  detalhes: {modelo: rastreamento_de_conhecimento, versao: 7, data: 2026-09, contato: ...}
  uso_pretendido: ordenar exercícios de prática por domínio estimado
  fora_de_escopo: [nota, aprovação/retenção, diagnóstico clínico, comparação entre escolas]
  fatores_avaliados: [ano escolar, rede, uso de tecnologia assistiva*]   # *com base legal
  metricas: {AUC: ..., calibracao: ..., limiar_alerta: 0.3, IC: bootstrap}
  dados: {treino: datasheet#ds-12, avaliacao: datasheet#ds-13}
  resultados: {por_fator: ..., interseccional: [ano x tecnologia_assistiva]}
  supervisao: professor pode rejeitar; ver psg.ai.transparency-and-human-oversight
  ressalvas: desempenho não verificado para alunos com < 20 interações
```

## Relações com outros conceitos

Parte de `psg.ai.ai-governance-frameworks` (evidência do MEASURE 2.9). Complementa `psg.ai.transparency-and-human-oversight` (explicação global versus local), `dat.rd.data-documentation` e `lae.dq.provenance-and-lineage` (dados) e `psg.audit.ripd-dpia` (o card alimenta o relatório). Avaliado por `adp.eval.heterogeneous-populations` e `lae.psy.fairness-in-measurement`. A exigência legal está em `psg.ai.eu-ai-act-and-brazil`.

## Lacunas e questões abertas

- Não foram localizados modelos de model card específicos para modelos de aprendizagem ou para populações de educação especial.
- O conteúdo do Anexo IV do AI Act (documentação técnica) e do art. 11 não foi lido; a comparação ficou restrita ao art. 13.
- Como fazer avaliação desagregada por deficiência sem ampliar o tratamento de dado sensível permanece em aberto.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| mitchell2019modelcards | academico | 2026-10-30 |
| gebru2021datasheets | academico | 2026-10-30 |
| eu2024aiact | normativo (espelho consolidado) | 2026-10-30 |
| nist2023airmf | tecnico | 2026-10-30 |
| khosravi2022explainable | academico | 2026-10-30 |
