---
id: adp.kt.logistic-models
titulo: Modelos logísticos de knowledge tracing (AFM, PFA)
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [pelanek2017overview, pavlik2009pfa, cen2005lfa, cen2006lfa, gervet2020when, corbett1995kt]
relacoes:
  - { tipo: alternativa-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: alternativa-a, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: relacionado-a, alvo: adp.irt.elo-rating }
  - { tipo: depende-de, alvo: adp.id.knowledge-components }
  - { tipo: relacionado-a, alvo: adp.id.kli-framework }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: relacionado-a, alvo: adp.kt.comparison }
termos: [logistic function, AFM, PFA, LFA, Rasch model, Q-matrix, learning curve, skill estimate, compensatory model]
---

# Modelos logísticos de knowledge tracing (AFM, PFA)

## Definição e terminologia

Os modelos logísticos de aprendizagem modelam a habilidade como variável contínua que muda gradualmente com a prática e mapeiam um valor logit m (habilidade acumulada menos dificuldade) para a probabilidade de acerto pela função logística σ(x) = 1/(1+e^(−x)) [F: pelanek2017overview]. Os principais membros usados em knowledge tracing são o Additive Factors Model (AFM), formulado dentro do método Learning Factors Analysis (LFA) de Cen, Koedinger e Junker, e o Performance Factors Analysis (PFA) de Pavlik, Cen e Koedinger [F: pelanek2017overview] [F: pavlik2009pfa]. "LFA" designa a rigor o método de busca de modelos cognitivos; "AFM" designa o modelo estatístico usado na busca — a literatura usa os dois nomes para o mesmo modelo logístico [I].

O que não é: não é um modelo de estado latente binário (essa é a família BKT, `adp.kt.bayesian-knowledge-tracing`), nem um modelo de teste estático: a IRT clássica assume habilidade fixa durante o teste, enquanto estes modelos somam um termo de aprendizagem por oportunidade de prática [F: pelanek2017overview].

## Problema que resolve

Dois problemas ligados: (1) prever desempenho quando um passo exige múltiplos componentes de conhecimento — o AFM/PFA soma as contribuições de todos os KCs do passo (modelo compensatório), o que o BKT clássico não acomoda [F: pavlik2009pfa]; (2) avaliar e melhorar o próprio modelo cognitivo do domínio: o LFA usa o modelo logístico como função de avaliação em uma busca A* sobre modelos de KCs gerados por operadores de split/add/merge, guiada por AIC/BIC [F: cen2005lfa] [F: cen2006lfa, metadados].

## Fundamentos e funcionamento

### Forma geral e relação com Rasch/IRT

O modelo de um parâmetro da IRT (Rasch) prediz σ(α_s − δ_i): habilidade do aluno menos dificuldade do item [F: gervet2020when]. O AFM é uma elaboração do modelo de Rasch: acrescenta, por KC, um ganho proporcional ao número de oportunidades de prática [F: pavlik2009pfa]. Na forma de regressão dada por Cen, Koedinger e Junker [F: cen2005lfa]:

```
ln[p/(1−p)] = α_s + Σ_j β_j·x_ij + Σ_j γ_j·x_ij·t_ij
```

onde α_s é a proficiência do aluno, β_j a facilidade do KC j, x_ij a presença do KC no passo e t_ij o número de oportunidades anteriores do aluno com o KC (γ_j é a taxa de aprendizagem do KC) [F: cen2005lfa]. O fundamento empírico é a curva de aprendizagem: taxa de erro declinante com a prática (lei de potência de Newell e Rosenbloom), e a observação de Corbett, Anderson e O'Brien de que "blips" na curva indicam um KC mal decomposto [F: cen2005lfa].

### PFA

O AFM ignora se as respostas anteriores foram certas ou erradas — todos os alunos "acumulam aprendizado de forma idêntica" — e por isso serve mal à adaptação individual [F: pavlik2009pfa]. O PFA reconfigura o modelo para ser sensível ao desempenho: remove α_s (não estimável a priori em uso adaptativo) e divide a contagem de prática em sucessos e fracassos [F: pavlik2009pfa]:

```
m(i, j∈KCs, s, f) = Σ_j ( β_j + γ_j·s_ij + ρ_j·f_ij )
p = 1/(1 + e^(−m))
```

com s_ij sucessos anteriores e f_ij fracassos anteriores do aluno i no KC j, escalados por γ_j e ρ_j [F: pavlik2009pfa]. Pelánek dá formulação equivalente como par atualização/predição: θ_k := θ_k + γ·c + δ·(1−c) e P(correto) = σ(Σ_k Q_ik(β_k + θ_k)), com Q-matrix explícita [F: pelanek2017overview].

### O framework unificador de Pelánek

Pelánek organiza os modelos de aluno em componentes comuns: dados globais (parâmetros de população e de domínio) e locais (estado do aluno, parâmetros de item), ligados por quatro procedimentos — busca de estrutura de KCs, ajuste de parâmetros (offline), equação de atualização e equação de predição (online) [F: pelanek2017overview]. Nesse esquema, BKT e PFA diferem só na realização dos componentes: BKT atualiza um θ probabilístico por regra de Bayes; PFA atualiza um θ contínuo por incremento e prediz via logística [F: pelanek2017overview]. O Elo rating adaptado à educação é um membro da mesma família com dificuldade de item atualizada online [F: pelanek2017overview]; ver `adp.irt.elo-rating`. A escolha entre famílias pode ser orientada pelo framework KLI: processos de memória e fluência mudam gradualmente e caem naturalmente nos modelos logísticos; o pressuposto de transição discreta do BKT é mais apropriado a processos de compreensão com KCs de granularidade fina [F: pelanek2017overview].

## Requisitos e pressupostos

- Q-matrix (mapeamento item→KCs), tipicamente manual, possivelmente refinada por busca automática (LFA, fatoração de matrizes) [F: pelanek2017overview] [F: cen2005lfa].
- Pressuposto compensatório na combinação de múltiplos KCs (a soma permite que um KC forte compense um fraco); modelos conjuntivos existem como alternativa [F: pavlik2009pfa] [F: pelanek2017overview].
- Habilidade monotônica: nas formas básicas, contagens só crescem; esquecimento exige extensões (janelas de tempo como DAS3H, decaimento) [F: gervet2020when] [F: pelanek2017overview].
- Ajuste por regressão logística padrão, rápido e com ótimo global do gradiente — vantagem prática sobre o ajuste EM/busca do BKT [F: pavlik2009pfa].

## Vantagens e limitações

Vantagens: parâmetros interpretáveis (facilidade, taxas de aprendizado por sucesso/fracasso); múltiplos KCs por passo; ajuste rápido e convexo [F: pavlik2009pfa]; o logit contínuo serve para prever latência de resposta e otimizar seleção de prática [F: pavlik2009pfa]; com os features certos (contagens totais + dificuldade de item, "Best-LR"), lidera em vários benchmarks [F: gervet2020when].

Limitações: o AFM puro não reage ao desempenho individual [F: pavlik2009pfa]; as formas básicas ignoram ordem temporal exata e recência [F: gervet2020when]; o PFA, sem parâmetro de aluno, captura menos variabilidade individual que o LFA completo [F: pavlik2009pfa]; dependem da qualidade da Q-matrix — que em vários datasets públicos acrescenta pouco poder preditivo [F: gervet2020when].

## Alternativas e comparações

Comparação direta PFA × KT de Corbett (4 datasets de tutores reais, A′ = área sob ROC) [F: pavlik2009pfa]:

| Dataset | KT (melhor variante) A′ | PFA A′ |
|---|---|---|
| Physics | 0,708 | 0,719 |
| Geometry | 0,667 | 0,685 |
| Algebra | 0,692 | 0,711 |
| Fractions | 0,706 | 0,723 |

Os autores atribuem a vantagem do PFA ao fato de o KT exagerar a evidência de um único erro (que, descontado o slip, implica estado "não aprendido"), enquanto o PFA ajusta gradualmente [F: pavlik2009pfa]. Pelánek, porém, adverte que comparações BKT × logísticos não são conclusivas nem generalizam: a escolha depende do domínio e do propósito [F: pelanek2017overview]. Resultados em larga escala (Gervet et al. 2020) e a matriz completa estão em `adp.kt.comparison`.

## Exemplo técnico independente de domínio

```
# PFA online, um estado por (aluno, KC)
ao observar resposta (aluno, passo com KCs K, correta c):
    para cada k em K:
        se c: s[k] += 1  senão: f[k] += 1
predizer(passo com KCs K):
    m = soma sobre k em K de ( beta[k] + gama[k]*s[k] + rho[k]*f[k] )
    retornar 1/(1 + exp(-m))
# beta, gama, rho ajustados por regressão logística sobre dados históricos
```

## Relações com outros conceitos

Alternativa a `adp.kt.bayesian-knowledge-tracing` e `adp.kt.deep-knowledge-tracing` (comparação em `adp.kt.comparison`). Generaliza o modelo de Rasch de `adp.irt.item-response-theory`; o `adp.irt.elo-rating` é a variante com atualização online de dificuldade. Depende de `adp.id.knowledge-components` (Q-matrix) e o método LFA é justamente uma forma de refinar esse modelo de domínio; o enquadramento pedagógico da escolha de família vem de `adp.id.kli-framework`. Avaliado por `adp.eval.predictive-metrics`.

## Lacunas e questões abertas

- A versão publicada do LFA (ITS 2006, LNCS, pp. 164-175) não foi aberta (Springer exige autenticação); o conteúdo veio da versão de workshop aberta no LearnLab (cen2005lfa), cujo ano e veículo não constam do PDF. As equações conferem com a descrição do LFA em pavlik2009pfa.
- O PDF aberto do PFA (cópia ERIC) rasteriza parte das equações como imagem; a forma reproduzida aqui segue o texto descritivo do próprio artigo e a reformulação de Pelánek.
- Não há consenso sobre quando o pressuposto compensatório falha; Pelánek registra o "credit assignment problem" de múltiplos KCs como questão aberta [F: pelanek2017overview].
- Instructional Factors Analysis (Chi et al. 2011), que acrescenta eventos instrucionais sem resposta, é citada por Pelánek mas não foi aberta nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| pelanek2017overview | academico | 2026-10-29 |
| pavlik2009pfa | academico | 2026-10-29 |
| cen2005lfa | academico | 2026-10-29 |
| cen2006lfa | academico (apenas metadados) | 2026-10-29 |
| gervet2020when | academico | 2026-10-29 |
| corbett1995kt | academico | 2026-10-29 |
