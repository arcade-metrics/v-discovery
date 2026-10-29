---
id: adp.lm.learner-model
titulo: Learner model
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [vanlehn2006behavior, bullkay2016smili, chrysafiadi2013review, abyaa2019learner]
relacoes:
  - { tipo: parte-de, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: depende-de, alvo: adp.id.knowledge-components }
  - { tipo: complementa, alvo: adp.lm.open-learner-model }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.dt.learning-digital-twin }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
termos: [learner model, student model, overlay model, inner loop, outer loop, mastery learning, macroadaptive learning, assignment of credit]
---

# Learner model

## Definição e terminologia

Um *learner model* (modelo de aluno) é a informação persistente que um sistema de aprendizagem mantém sobre cada estudante para adaptar suas decisões pedagógicas. Self (1974), citado por Bull e Kay, descrevia o *student model* como aquilo que permite "a um professor humano ou ao próprio programa de ensino [...] determinar quanto [um estudante] sabe em cada momento" [F: bullkay2016smili]. VanLehn descreve o conteúdo típico: pares atributo-valor em que o atributo é um traço (um knowledge component, um estilo de aprendizagem) e o valor é a estimativa do tutor de que o estudante possui aquele traço; o modelo pode conter ainda dados externos (notas padronizadas, histórico) e dados de desempenho (tarefas concluídas, tempo, pedidos de ajuda, erros). Ele observa que "student model" é um nome estranho para uma coleção tão heterogênea de dados, mas é o termo tradicional [F: vanlehn2006behavior].

Os termos *student model* e *learner model* nomeiam o mesmo conceito; o segundo, mais recente, destaca o papel ativo do aprendiz e a aplicabilidade fora da educação formal [F: bullkay2016smili]. O que o conceito não é: não é o *modelo de domínio* (a representação do conteúdo a aprender), não é o registro bruto de eventos de interação, e não é um dashboard — ver a seção sobre learning analytics abaixo.

Existem surveys dedicados ao tema: Chrysafiadi e Virvou (2013) revisam abordagens de modelagem de estudante da década anterior [F: chrysafiadi2013review, metadados], e Abyaa, Khalidi Idrissi e Bennani (2019) publicaram revisão sistemática de cinco anos de literatura sobre learner modelling [F: abyaa2019learner, metadados]; nenhum dos dois textos completos pôde ser aberto nesta pesquisa (ver Lacunas).

## Problema que resolve

Sem um registro do que cada estudante sabe, um sistema só pode tratar todos da mesma forma. O modelo de aluno é o que permite decisões adaptativas: VanLehn descreve o tutor como dois laços — o *outer loop*, que executa uma vez por tarefa e escolhe a próxima tarefa, e o *inner loop*, que executa uma vez por passo da solução, dá feedback e dicas, e "também pode avaliar a competência em evolução do estudante e atualizar um student model, que é usado pelo outer loop para selecionar a próxima tarefa apropriada" [F: vanlehn2006behavior]. O modelo é, portanto, a ponte entre a observação fina (passos) e a decisão grossa (sequenciamento).

## Fundamentos e funcionamento

### O que o modelo representa

- **Conhecimento e habilidades**: estimativas de domínio por knowledge component (KC), incluindo KCs incorretos (misconceptions), que permitem escolher tarefas remediadoras [F: vanlehn2006behavior]. VanLehn define "mastery" como a probabilidade de que um KC seja aplicado quando deveria ser aplicado [F: vanlehn2006behavior].
- **Traços estáveis**: alguns sistemas representam estilos e preferências (explicação visual versus verbal) para escolher tarefas compatíveis [F: vanlehn2006behavior].
- **Afeto**: sensores têm sido usados para modelar emoções do aprendiz (Arroyo et al. 2009; Woolf 2010, citados por Bull e Kay) [F: bullkay2016smili].
- **Metacognição**: o modelo exposto ao aprendiz tornou-se fonte de informação para promover aprendizagem autorregulada e habilidades metacognitivas [F: bullkay2016smili]; o documento `adp.lm.open-learner-model` aprofunda.

### Overlay sobre um modelo de domínio

No *overlay model*, o domínio é representado como uma estrutura (por exemplo, uma rede semântica) e o progresso do estudante é modelado como uma sobreposição sobre essa estrutura — a abordagem remonta a Carbonell (1970), em que o domínio era uma rede semântica e o progresso do estudante um overlay sobre ela [F: bullkay2016smili]. Na prática corrente, o overlay é um vetor de estimativas de domínio, uma por KC do modelo de domínio [I]. Bull e Kay distinguem duas tradições: modelos com validade cognitiva (model tracing dos cognitive tutors, constraint-based tutors) e a abordagem "pragmática", sem pretensão de validade cognitiva, em que o modelo representa só o que o sistema precisa para agir — Self (1990) argumentou que o problema "intratável" da modelagem de estudante pode ser contornado assim, e que um vetor simples de escores de domínio por objetivo de aprendizagem já é útil para personalização [F: bullkay2016smili].

### Papel no sistema tutor: inner loop e outer loop

No outer loop, VanLehn identifica quatro desenhos, do mais simples ao mais complexo: menu escolhido pelo estudante; sequência fixa; *mastery learning* (tarefas de uma unidade até dominá-la); e *macroadaptação*, em que o tutor conhece os KCs exercitados por cada tarefa, mantém estimativa de domínio por KC e escolhe a tarefa pela sobreposição entre KCs da tarefa e KCs dominados [F: vanlehn2006behavior]. Quanto mais adaptativo o outer loop, mais rico o modelo exigido: um laço de sequência fixa precisa só de um ponteiro; a macroadaptação precisa de estimativa por KC [F: vanlehn2006behavior].

No inner loop, a avaliação é um dos cinco serviços típicos (feedback mínimo, feedback específico de erro, dicas, avaliação de conhecimento, revisão da solução) [F: vanlehn2006behavior]. A atualização do modelo a partir de passos enfrenta dois problemas clássicos: *assignment of credit* (um passo correto pode ter várias derivações possíveis, logo vários conjuntos de KCs candidatos) e *assignment of blame* (num passo errado que exige vários KCs, basta um ausente para bloquear o passo); técnicas de raciocínio sob incerteza, como redes bayesianas, são usadas para ambos [F: vanlehn2006behavior]. A estimação probabilística do overlay por modelo é tratada em `adp.kt.bayesian-knowledge-tracing` e `adp.kt.logistic-models`.

### Granularidade

VanLehn distingue avaliação *fine-grained* (probabilidade de domínio por KC) de *coarse-grained* (um número para a competência geral) e propõe a heurística: quanto maior a decisão, mais grossa a avaliação necessária — tutores, que tomam muitas decisões pequenas, são os principais consumidores de avaliações finas; instrutores têm pouco uso para 500 números por estudante [F: vanlehn2006behavior].

## Requisitos e pressupostos

- Um modelo de domínio decomposto em unidades (KCs) para que o overlay tenha sobre o que se apoiar; ver `adp.id.knowledge-components` [I].
- Persistência entre sessões: o modelo precisa ser armazenado em servidor ou disco para o outer loop funcionar ao longo de várias tarefas e sessões [F: vanlehn2006behavior].
- Evidência observável: só passos (eventos de interface) são observáveis; eventos de aprendizagem e KCs são inferidos [F: vanlehn2006behavior].
- Clareza de propósito: VanLehn alerta que é fácil superconstruir a avaliação; deve-se projetar apenas o que as decisões do sistema exigem [F: vanlehn2006behavior].

## Vantagens e limitações

Vantagens: habilita mastery learning e macroadaptação [F: vanlehn2006behavior]; modelos independentes de uma única aplicação (learner model servers) permitem reuso por várias aplicações e agregação de dados de múltiplas fontes ao longo do tempo [F: bullkay2016smili].

Limitações: o modelo é uma inferência, não uma medida direta — pouca evidência e evidência mista podem produzir a mesma estimativa (1 acerto em 2 versus 20 acertos em 40) [F: vanlehn2006behavior]; o conhecimento do estudante muda, o que levanta a questão de quando descartar evidência antiga [F: vanlehn2006behavior]; a interpretação de ajuda recebida como evidência é ambígua [F: vanlehn2006behavior]; e críticos notam que, em muitos sistemas, "o student model não passa de um livro de notas sofisticado" [F: vanlehn2006behavior].

## Alternativas e comparações

| Aspecto | Learner model | Learning analytics | Gêmeo digital de aprendizagem |
|---|---|---|---|
| Objeto representado | conhecimento, habilidades e traços do aprendiz, por KC [F: vanlehn2006behavior] | dados de atividade em torno de recursos de aprendizagem, com origem em uso institucional (alunos em risco) [F: bullkay2016smili] | metáfora de réplica computacional da pessoa; ver `adp.dt.learning-digital-twin` [I] |
| Consumidor primário | o próprio sistema (inner/outer loop) [F: vanlehn2006behavior] | instituição, professor, pesquisador [F: bullkay2016smili] | varia conforme a definição adotada [H] |
| Estrutura | modelo do conhecimento do aprendiz | repositórios estruturados em torno dos recursos, "não um modelo do conhecimento ou das habilidades do aprendiz" [F: bullkay2016smili] | em aberto na literatura [H] |

Bull e Kay observam que os grandes repositórios de dados de LMS e MOOCs "ainda não foram projetados como learner models" [F: bullkay2016smili]. A relação com gêmeos digitais não é aprofundada aqui: a hipótese de trabalho é que um "gêmeo digital de aprendizagem" exige, no mínimo, um learner model persistente e atualizado continuamente, mas a definição operacional que o distinguiria é questão aberta do domínio [H].

## Métricas e métodos de avaliação

A qualidade do modelo é avaliada pela acurácia preditiva sobre desempenho futuro e pela calibração das probabilidades; ver `adp.eval.predictive-metrics` e `adp.eval.evaluation-protocols`. VanLehn cita duas técnicas empíricas para validar a decomposição em KCs subjacente: predição de transferência entre tarefas e predição de curvas de aprendizagem suaves [F: vanlehn2006behavior].

## Exemplo técnico independente de domínio

Overlay mínimo com contadores, seguindo a descrição de VanLehn (frequência de aplicações sobre oportunidades, com os problemas de crédito e culpa explícitos) [F: vanlehn2006behavior]:

```
modelo[kc] = { sucessos: 0, oportunidades: 0 }

ao_observar_passo(passo):
    kcs = analisador_de_passos(passo)        # KCs que derivam o passo
    se passo.correto:
        para kc em kcs:                      # crédito: pode ser ambíguo
            modelo[kc].sucessos += 1
            modelo[kc].oportunidades += 1
    senão:
        kc_culpado = atribuir_culpa(kcs)     # culpa: um KC ausente basta
        modelo[kc_culpado].oportunidades += 1

dominio_estimado(kc) = modelo[kc].sucessos / modelo[kc].oportunidades
```

Este estimador congela o aprendiz no tempo; modelos que tratam aprendizagem e esquecimento estão em `adp.kt.bayesian-knowledge-tracing` e `adp.sr.memory-and-forgetting` [I].

## Relações com outros conceitos

Parte de `adp.adapt.adaptive-learning-systems` (é o componente que torna a adaptação possível). Depende de `adp.id.knowledge-components` como vocabulário do overlay. É complementado por `adp.lm.open-learner-model`, que expõe o modelo ao próprio aprendiz. É estimado por técnicas de `adp.kt.bayesian-knowledge-tracing` e avaliado por `adp.eval.predictive-metrics`. A relação com `adp.dt.learning-digital-twin` registra a fronteira conceitual com a metáfora de gêmeo digital.

## Lacunas e questões abertas

- Os surveys de Chrysafiadi e Virvou (2013) e de Abyaa et al. (2019) foram verificados apenas por metadados (Elsevier e Springer exigem autenticação; nenhuma cópia aberta localizada via OpenAlex); uma taxonomia consolidada das dimensões modeladas (conhecimento, afeto, metacognição, contexto) fica pendente de leitura dessas revisões.
- VanLehn (2006) lista questões de avaliação ainda abertas no próprio texto: descarte de evidência antiga, tratamento de ajuda como evidência, dificuldade desigual entre learning events [F: vanlehn2006behavior]; o estado atual dessas questões deve ser coberto pelos documentos de knowledge tracing.
- A definição operacional que distinguiria um "gêmeo digital de aprendizagem" de um learner model tradicional permanece aberta (pergunta do brief do domínio).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| vanlehn2006behavior | academico | 2026-10-29 |
| bullkay2016smili | academico | 2026-10-29 |
| chrysafiadi2013review | academico (apenas metadados) | 2026-10-29 |
| abyaa2019learner | academico (apenas metadados) | 2026-10-29 |
