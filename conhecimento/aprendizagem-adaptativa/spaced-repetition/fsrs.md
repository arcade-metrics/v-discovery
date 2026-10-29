---
id: adp.sr.fsrs
titulo: FSRS (Free Spaced Repetition Scheduler)
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [fsrs2026algorithm, fsrs2026optimization, srsbenchmark2026, anki2026algofaq, anki2026deckoptions, anki2025release, ye2022ssp, su2023dynamics, maimemo2022sspmmc, maimemo2023sspmmcplus]
relacoes:
  - { tipo: depende-de, alvo: adp.sr.memory-and-forgetting }
  - { tipo: alternativa-a, alvo: adp.sr.classical-algorithms }
  - { tipo: alternativa-a, alvo: adp.sr.half-life-regression }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
termos: [FSRS, DSR model, difficulty, stability, retrievability, desired retention, forgetting curve, review log]
---

# FSRS (Free Spaced Repetition Scheduler)

## Definição e terminologia

FSRS é uma família de algoritmos de repetição espaçada de código aberto que modela a memória de cada item por três componentes — o modelo DSR: *difficulty* (D, dificuldade, limitada a [1, 10]), *stability* (S, estabilidade, definida como o intervalo em que a retrievabilidade cai a 90%) e *retrievability* (R, probabilidade de recordação no momento) — e ajusta seus parâmetros ao histórico de revisões de cada usuário [F: fsrs2026algorithm]. A wiki do projeto aponta como base de pesquisa dois artigos revisados por pares da linha MaiMemo: Ye, Su e Cao (KDD 2022) e Su, Ye, Nie, Cao e Chen (IEEE TKDE 2023) [F: fsrs2026algorithm]; ambos tratam do problema de agendamento como caminho mínimo estocástico sobre um modelo de memória com propriedade de Markov (ver "Lacunas" sobre o acesso ao texto completo).

Versão e data: a versão corrente documentada na wiki é o **FSRS-6**, com 21 parâmetros (w0–w20) [F: fsrs2026algorithm]; o Anki 25.07 (publicado em 4 de julho de 2025) foi a versão que incorporou o FSRS-6 ("FSRS-6 brings further algorithm improvements") [F: anki2025release]. Um FSRS-7 aparece no benchmark dos autores, ainda não descrito na wiki na data de consulta [F: srsbenchmark2026] [I]. O FSRS está disponível no Anki desde o 23.10, como opção que o usuário ativa no lugar do algoritmo derivado do SM-2 [F: anki2026algofaq].

O que não é: não é um modelo de knowledge tracing — prevê recordação de itens memorizados isoladamente, sem noção de habilidade (skill) compartilhada entre itens [I].

## Problema que resolve

Os algoritmos clássicos usam parâmetros fixos (`adp.sr.classical-algorithms`); o HLR ajusta um modelo global por população (`adp.sr.half-life-regression`). O FSRS ataca duas pontas: (1) prever R por item e por usuário, com parâmetros otimizados no histórico individual de revisões; (2) deixar o usuário controlar o trade-off retenção × carga de revisões por um único alvo, a *desired retention* — o intervalo agendado é o tempo em que R prevista cai até esse alvo [F: anki2026deckoptions] [I].

## Fundamentos e funcionamento

Equações principais, conforme a wiki "The Algorithm" (notação: G é a nota, 1 = again, 2 = hard, 3 = good, 4 = easy) [F: fsrs2026algorithm]:

- **Curva de esquecimento (FSRS-6)**: `R(t, S) = (1 + factor · t/S)^(−w20)`, com `factor = 0.9^(−1/w20) − 1`, o que garante `R(S, S) = 0.9`. O expoente de decaimento w20 é treinável, com padrão 0,1542. (No FSRS-4.5 o decaimento era fixo em −0,5 com factor 19/81.)
- **Estabilidade inicial**: `S0(G) = w_{G−1}` — quatro parâmetros, um por nota da primeira revisão.
- **Dificuldade inicial**: `D0(G) = w4 − e^{w5·(G−1)} + 1`.
- **Atualização de dificuldade com reversão à média**: `ΔD = −w6·(G−3)`; `D' = D + ΔD·(10−D)/9`; `D'' = w7·D0(4) + (1−w7)·D'` — a dificuldade converge lentamente para a de um item "fácil".
- **Crescimento da estabilidade após acerto**: `S'_r = S · (e^{w8} · (11−D) · S^{−w9} · (e^{w10·(1−R)} − 1) · w15^{[G=hard]} · w16^{[G=easy]} + 1)`. O fator de crescimento é ≥ 1 para acertos e diminui com D maior, S maior e R maior — revisar quando R está baixa rende mais estabilidade.
- **Estabilidade pós-lapso**: `S'_f = w11 · D^{−w12} · ((S+1)^{w13} − 1) · e^{w14·(1−R)}`.
- **Revisões no mesmo dia (FSRS-6)**: `S'(S, G) = S · e^{w17·(G−3+w18)} · S^{−w19}`.

Linhagem de versões, pela mesma fonte: FSRS v1 (7 parâmetros), v2 (14), v3 (13), v4 e FSRS-4.5 (17), FSRS-5 (19), FSRS-6 (21) [F: fsrs2026algorithm].

**Otimização**: os parâmetros são ajustados por máxima verossimilhança sobre os logs de revisão (tabela `revlog` do Anki: carta, timestamp, nota), agrupados por carta e ordenados no tempo; a perda tem a forma de entropia cruzada binária sobre o desfecho de cada revisão, treinada com backpropagation through time em PyTorch — sem necessidade de observar estabilidade diretamente [F: fsrs2026optimization]. No Anki, a otimização é por preset, recomendada mensalmente; a documentação alerta que menos de algumas centenas de revisões é causa comum de mau desempenho [F: anki2026deckoptions].

**Agendamento**: com a desired retention DR (padrão 0,9 no Anki; recomendação de ficar abaixo de 0,97 [F: anki2026deckoptions]), o próximo intervalo é o t que resolve R(t, S) = DR; para DR = 0,9, t = S por construção [I, derivado da curva acima].

## Requisitos e pressupostos

- Histórico de revisões com timestamp e nota por item; centenas de revisões para otimização individual confiável [F: anki2026deckoptions].
- Pressuposto de Markov no estado (D, S): o próximo estado depende do atual, da nota e de R — os artigos da linha MaiMemo constroem o agendamento ótimo sobre essa propriedade [F: maimemo2022sspmmc] [F: fsrs2026algorithm].
- Itens tratados como independentes: sem transferência entre itens relacionados nem modelagem de habilidade [I].

## Vantagens e limitações

Vantagens: parâmetros ajustados ao indivíduo; estado (D, S, R) interpretável em termos psicológicos; controle explícito do trade-off carga × retenção; código aberto com ecossistema de implementação (Anki e outros) [F: anki2026deckoptions] [I].

Limitações e ressalvas críticas:

- **A evidência quantitativa principal vem dos próprios autores.** O srs-benchmark é mantido na organização open-spaced-repetition — a mesma que desenvolve o FSRS; o README credita o FSRS a Jarrett Ye e direciona submissões a L-M-Sherlock [F: srsbenchmark2026], e a identidade entre o mantenedor e o primeiro autor do artigo KDD (Junyao Ye) é inferência nossa a partir dos créditos cruzados dos repositórios [I]. Não localizamos avaliação independente revisada por pares do FSRS tal como distribuído.
- Os números do benchmark medem acurácia preditiva de R, não desfecho de aprendizagem; não há, nas fontes consultadas, experimento controlado com alunos comparando FSRS a SM-2 ou HLR em retenção real [I].
- Dados do benchmark: usuários de Anki que doaram coleções (10 mil usuários, ~727 milhões de revisões, dataset público anki-revlogs-10k no Hugging Face) — população auto-selecionada de usuários assíduos [F: srsbenchmark2026] [I].
- Com poucos dados por usuário a otimização degrada; o próprio fornecedor documenta o limiar de "algumas centenas de revisões" [F: anki2026deckoptions].
- A afirmação da documentação do Anki de que o FSRS alcança a mesma retenção com menos revisões é afirmação de fornecedor [F: anki2026algofaq].

## Alternativas e comparações

Resultados do srs-benchmark, sem revisões de mesmo dia, médias com IC de 99% — **benchmark mantido pelos autores do FSRS** [F: srsbenchmark2026]:

| Modelo | Parâmetros | Log loss ↓ | RMSE(bins) ↓ | AUC ↑ |
|---|---|---|---|---|
| FSRS-7 recency (100 épocas) | — | 0,3363 | 0,0576 | 0,7243 |
| FSRS-6 | 21 | 0,3460 | 0,0653 | 0,7034 |
| FSRS-5 | 19 | 0,3561 | 0,0742 | 0,7010 |
| FSRS-4.5 | 17 | 0,3625 | 0,0764 | 0,6891 |
| HLR | 3 | 0,4694 | 0,1275 | 0,6369 |
| AVG (baseline constante) | — | 0,3945 | — | — |

O melhor modelo geral do benchmark não é um FSRS: RWKV-Instant, rede neural treinada entre usuários (não otimizada por usuário), com log loss 0,2773 e AUC 0,8329 [F: srsbenchmark2026] — indício de que o teto preditivo está acima do DSR, ao custo de interpretabilidade e de treino populacional [I]. Comparação completa com Leitner, SM-2, HLR e KT com esquecimento em `adp.sr.comparison`.

## Métricas e métodos de avaliação

Log loss, RMSE(bins) e AUC, com validação temporal (TimeSeriesSplit em 5 partes, treinando no passado e testando no futuro) [F: srsbenchmark2026]. Ver `adp.eval.predictive-metrics`.

## Exemplo técnico independente de domínio

```
# FSRS-6, por item; w = vetor de 21 parâmetros otimizado no histórico
revisar(item, nota G, agora):
    t = agora - item.ultima_revisao
    R = (1 + factor * t / item.S) ** (-w20)      # factor = 0.9**(-1/w20) - 1
    se primeira_revisao: item.S = S0(G); item.D = D0(G)
    senao:
        item.D = atualizar_D(item.D, G)           # reversao a media
        item.S = (G == 1) ? S_pos_lapso(item.D, item.S, R)
                          : S_pos_acerto(item.D, item.S, R, G)
    # agenda: proximo t tal que R(t, S) = retencao_desejada
    intervalo = item.S * ((DR ** (-1/w20)) - 1) / factor
```

Estrutura conforme as equações da wiki [F: fsrs2026algorithm]; a linha do intervalo é derivação nossa da curva de esquecimento [I].

## Relações com outros conceitos

Operacionaliza estabilidade e retrievabilidade de `adp.sr.memory-and-forgetting` como estado por item. Alternativa treinável por indivíduo a `adp.sr.classical-algorithms` e a `adp.sr.half-life-regression`. A escolha da retenção-alvo ótima — formulada nos artigos da linha MaiMemo como minimização do custo de revisão por caminho mínimo estocástico, com dataset público de 220 milhões de logs [F: maimemo2023sspmmcplus] — conecta-se a `adp.adapt.sequencing-policies`.

## Lacunas e questões abertas

- Texto completo dos dois artigos revisados por pares não acessado: KDD 2022 (DOI 10.1145/3534678.3539081) devolve 403 no ACM mesmo via o link de acesso dos autores (maimemo.com/paper), e o TKDE 2023 (DOI 10.1109/TKDE.2023.3251721) é fechado (OpenAlex: sem cópia aberta). Entram na bibliografia como [metadados]; o conteúdo citado aqui vem das wikis e READMEs dos autores, abertos hoje.
- Relação exata entre o DHP dos artigos e o DSR do FSRS-6 distribuído: a wiki cita os artigos como base, mas as equações distribuídas evoluíram além do publicado; não está claro o que do FSRS-6 tem aval revisado por pares [I].
- FSRS-7: presente no benchmark, sem documentação na wiki nem release no Anki na data de consulta; versão e equações a registrar quando publicadas.
- Falta avaliação independente (fora da organização open-spaced-repetition) e falta evidência experimental de desfecho de aprendizagem.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fsrs2026algorithm | tecnico | 2026-10-29 |
| fsrs2026optimization | tecnico | 2026-10-29 |
| srsbenchmark2026 | tecnico | 2026-10-29 |
| anki2026algofaq | fornecedor | 2026-10-29 |
| anki2026deckoptions | fornecedor | 2026-10-29 |
| anki2025release | fornecedor | 2026-10-29 |
| ye2022ssp | academico (metadados) | 2026-10-29 |
| su2023dynamics | academico (metadados) | 2026-10-29 |
| maimemo2022sspmmc | tecnico | 2026-10-29 |
| maimemo2023sspmmcplus | tecnico | 2026-10-29 |
