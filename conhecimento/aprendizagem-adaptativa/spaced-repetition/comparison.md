---
id: adp.sr.comparison
titulo: Comparação de algoritmos de repetição espaçada
tipo: comparacao
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [settles2016hlr, ilidio2026hlr, wozniak1990sm2, fsrs2026algorithm, srsbenchmark2026, anki2026deckoptions, choffin2019das3h]
relacoes:
  - { tipo: relacionado-a, alvo: adp.sr.classical-algorithms }
  - { tipo: relacionado-a, alvo: adp.sr.half-life-regression }
  - { tipo: relacionado-a, alvo: adp.sr.fsrs }
  - { tipo: relacionado-a, alvo: adp.sr.memory-and-forgetting }
  - { tipo: relacionado-a, alvo: adp.kt.comparison }
  - { tipo: relacionado-a, alvo: adp.kt.logistic-models }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
termos: [spaced repetition, scheduler, memory model, time windows, q-matrix, desired retention, personalização por aluno]
---

# Comparação de algoritmos de repetição espaçada

## Definição e terminologia

Este documento compara cinco famílias que resolvem o agendamento de revisões: sistema de Leitner e SM-2 (`adp.sr.classical-algorithms`), half-life regression (`adp.sr.half-life-regression`), FSRS (`adp.sr.fsrs`) e modelos de knowledge tracing com esquecimento — aqui representados por DASH e DAS3H, modelos logísticos com janelas temporais de prática (Choffin et al., 2019) [F: choffin2019das3h]. As três primeiras famílias agendam *itens* memorizados isoladamente (flashcards, vocabulário); a última estima memória de *habilidades* (knowledge components) exercitadas por itens variados, cenário em que itens novos precisam ser respondidos por generalização [F: choffin2019das3h].

## Problema que resolve

Escolher algoritmo de repetição espaçada é um trade-off entre dados exigidos, personalização, acurácia preditiva e interpretabilidade. A comparação abaixo organiza a evidência publicada para essa decisão; nenhuma das fontes consultadas sustenta superioridade universal de uma família [I].

## Alternativas e comparações

| Dimensão | Leitner | SM-2 | HLR | FSRS (FSRS-6) | KT com esquecimento (DASH/DAS3H) |
|---|---|---|---|---|---|
| Modelo de memória | nenhum explícito; caixas = intervalos que dobram/caem pela metade [F: settles2016hlr] | nenhum explícito; intervalo multiplicado por ease factor por item [F: wozniak1990sm2] | curva exponencial `p = 2^(−Δ/h)`, meia-vida log-linear nas features [F: settles2016hlr] | DSR: estado (D, S) por item, curva de potência `R = (1 + f·t/S)^(−w20)` [F: fsrs2026algorithm] | logística: habilidade − dificuldade + janelas temporais de acertos/tentativas por skill [F: choffin2019das3h] |
| Parâmetros | 0 treináveis | 0 treináveis; EF por item derivado das notas [F: wozniak1990sm2] | pesos globais por curso (3 features de interação + ~20k lexemas no artigo) [F: settles2016hlr] | 21 por usuário (w0–w20) [F: fsrs2026algorithm] | dezenas a centenas por população (2 por janela por skill no DAS3H) [F: choffin2019das3h] |
| Dados exigidos | acerto/erro por item | nota 0–5 por item | milhões de traces com p, Δ e features [F: settles2016hlr] | logs com timestamp e nota; centenas de revisões por usuário [F: anki2026deckoptions] | logs com timestamp + q-matrix item→skills [F: choffin2019das3h] |
| Personalização | nenhuma (regra fixa) | por item, via notas; nada do aluno | global; aluno entra por contadores; efeitos aleatórios por aluno/lexema em extensões [F: ilidio2026hlr] | por aluno (parâmetros individuais) e por item (estado D, S) [F: anki2026deckoptions] | por população, com habilidade por aluno e curvas por skill [F: choffin2019das3h] |
| Evidência publicada | baselines em dois estudos abertos [F: settles2016hlr] [F: ilidio2026hlr] | nenhuma avaliação preditiva publicada localizada [I] | ACL 2016 com experimentos de usuário; reanálise aberta de 2026 [F: settles2016hlr] [F: ilidio2026hlr] | benchmark dos próprios autores; sem avaliação independente localizada [F: srsbenchmark2026] [I] | EDM 2019, 3 datasets públicos, validação cruzada por aluno [F: choffin2019das3h] |
| Interpretabilidade | total (regras visíveis) | alta (EF e intervalos) | alta: pesos por feature legíveis como dificuldade [F: settles2016hlr] | média: estado DSR legível, mas 21 parâmetros interagindo [I] | alta: curvas de aprendizado/esquecimento por skill [F: choffin2019das3h] |
| Limite característico | intervalo independe do material e do aluno [F: settles2016hlr] | EF confunde item e aluno; sem previsão de recordação [I] | AUC perto do acaso no dataset original [F: ilidio2026hlr] | evidência auto-reportada; itens independentes [I] | não agenda revisões por si; exige q-matrix curada [F: choffin2019das3h] [I] |

## Evidência empírica em detalhe

Três corpos de evidência aberta, cada um com seu viés de origem:

1. **Dados Duolingo (taxas de recordação por sessão, linguagem).** HLR venceu Leitner e Pimsleur em MAE (0,128 vs. 0,235 e 0,445), mas Leitner teve a melhor AUC (0,542) [F: settles2016hlr]. Na reanálise independente de Ilídio et al., todos os métodos originais ficaram com AUC ≤ 0,51; só extensões com efeitos mistos e Random Forest passaram de 0,60 [F: ilidio2026hlr]. Estudo conduzido com dados da própria plataforma, mas publicado com dataset e código abertos [F: settles2016hlr].
2. **Dados Anki (revisões binárias de flashcards; benchmark mantido pelos autores do FSRS).** FSRS-6: log loss 0,3460 e AUC 0,7034; HLR: 0,4694 e 0,6369 (pior que a baseline constante em log loss); melhor modelo geral: rede neural RWKV-Instant (0,2773 / 0,8329), treinada entre usuários [F: srsbenchmark2026]. O conflito de interesse é estrutural: o benchmark vive na organização que desenvolve o FSRS [F: srsbenchmark2026] [I].
3. **Datasets de tutores de matemática (habilidades múltiplas).** DAS3H superou DASH, IRT, PFA e AFM em AUC nos três datasets (entre ~0,74 e ~0,83 conforme o dataset), e as features de janelas temporais elevaram a AUC de forma consistente — evidência de que modelar esquecimento melhora KT, e de que curvas por skill diferem entre si [F: choffin2019das3h].

As três linhas não são comparáveis entre si: alvos (proporção de acertos vs. resultado binário), populações e protocolos diferem [I].

## Em que condições cada família se justifica

- **Leitner/SM-2**: sem histórico acumulado, sem infraestrutura de treino, ou quando a transparência da regra importa mais que acurácia — e como baseline obrigatória em qualquer avaliação [I].
- **HLR**: itens com features ricas e dados massivos *por população*, quando se quer um modelo global interpretável e há poucas revisões por par aluno-item; a extensão com efeitos mistos é o caminho quando dificuldade de item e habilidade de aluno variam muito [F: ilidio2026hlr] [I].
- **FSRS**: usuários individuais com centenas de revisões registradas e necessidade de controlar carga × retenção por item; aceitando que a evidência quantitativa disponível é dos próprios autores [F: srsbenchmark2026] [I].
- **KT com esquecimento (DASH/DAS3H)**: quando o que se revisa são *habilidades* aplicadas em itens variados (matemática, ciências), com q-matrix disponível — cenário em que agendar flashcards não faz sentido [F: choffin2019das3h].
- Um sistema pode compor famílias: estimar memória com um modelo e decidir o momento da revisão com uma política separada (`adp.adapt.sequencing-policies`) [I].

## Métricas e métodos de avaliação

MAE, AUC e correlações de ranqueamento no corpo Duolingo [F: settles2016hlr] [F: ilidio2026hlr]; log loss, RMSE(bins) e AUC com validação temporal no srs-benchmark [F: srsbenchmark2026]; AUC e NLL com validação cruzada em nível de aluno no corpo EDM [F: choffin2019das3h]. A escolha da métrica muda o vencedor — HLR venceu em MAE e perdeu em AUC no mesmo experimento [F: settles2016hlr]; ver `adp.eval.predictive-metrics`.

## Exemplo técnico independente de domínio

Esqueleto comum que todas as famílias instanciam de formas diferentes:

```
para cada item/skill k no momento t:
    m_k = modelo.estimar(historico_k, t)      # caixa, EF, meia-vida, (D,S,R), somatorio logistico
    urgencia_k = criterio(m_k)                # ex.: R prevista abaixo da retencao-alvo
proximo = argmax(urgencia)                    # ou agendar t futuro em que criterio dispara
apos resposta: modelo.atualizar(historico_k)
```

A diferença essencial está em `estimar`: regra fixa (Leitner/SM-2), regressão global (HLR/DASH/DAS3H) ou estado por item com parâmetros individuais (FSRS) [I].

## Relações com outros conceitos

Sintetiza `adp.sr.classical-algorithms`, `adp.sr.half-life-regression` e `adp.sr.fsrs` à luz de `adp.sr.memory-and-forgetting`. DASH/DAS3H pertencem à família logística de `adp.kt.logistic-models` e aparecem na comparação geral de KT em `adp.kt.comparison`; este documento cobre apenas seu papel como modelos de esquecimento para agendamento.

## Lacunas e questões abertas

- Não existe, nas fontes abertas consultadas, benchmark neutro que compare as cinco famílias no mesmo dataset com o mesmo alvo; o mais próximo é o srs-benchmark, mantido pelos autores de um dos competidores.
- Falta evidência de desfecho de aprendizagem (retenção medida, não predição) comparando FSRS a alternativas; os únicos experimentos de usuário em escala localizados são os do HLR, que mediram engajamento [F: settles2016hlr].
- SM-2 segue sem avaliação preditiva formal publicada que tenhamos localizado.
- Como combinar modelos de item (FSRS) com modelos de habilidade (DAS3H) num mesmo sistema é questão aberta; Choffin et al. apontam a extensão a agendamento adaptativo de skills como trabalho futuro [F: choffin2019das3h].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| settles2016hlr | academico | 2026-10-29 |
| ilidio2026hlr | academico | 2026-10-29 |
| wozniak1990sm2 | fornecedor | 2026-10-29 |
| fsrs2026algorithm | tecnico | 2026-10-29 |
| srsbenchmark2026 | tecnico | 2026-10-29 |
| anki2026deckoptions | fornecedor | 2026-10-29 |
| choffin2019das3h | academico | 2026-10-29 |
