---
id: adp.irt.elo-rating
titulo: Elo rating aplicado a sistemas educacionais adaptativos
tipo: tecnica
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [pelanek2016elo, papousek2014adaptive]
relacoes:
  - { tipo: depende-de, alvo: adp.irt.item-response-theory }
  - { tipo: alternativa-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: alternativa-a, alvo: adp.kt.logistic-models }
  - { tipo: complementa, alvo: adp.adapt.sequencing-policies }
  - { tipo: relacionado-a, alvo: adp.sr.memory-and-forgetting }
  - { tipo: relacionado-a, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
termos: [Elo rating, uncertainty function, cold start, shifted logistic function, PFAE, prior knowledge estimation, target success rate, online update]
---

# Elo rating aplicado a sistemas educacionais adaptativos

## Definição e terminologia

O Elo rating system (Elo, 1978) é um sistema de rating de jogadores de xadrez: cada jogador tem um rating atualizado após cada partida, proporcionalmente ao quão surpreendente foi o resultado [F: pelanek2016elo]. Em educação, interpreta-se a resposta de um aluno a um item como uma partida entre o aluno e o item, o que dá uma forma barata de estimar dinamicamente habilidade de alunos e dificuldade de itens [F: pelanek2016elo]. A função de probabilidade é uma reparametrização do modelo de Bradley-Terry para comparações pareadas; a versão original do xadrez usa base 10 e constante 400 por razões históricas, sem impacto no princípio [F: pelanek2016elo]. Extensões conhecidas no mundo dos jogos: Glicko e TrueSkill, bayesianas [F: pelanek2016elo]. O que não é: não é um modelo de aprendizagem com pressupostos cognitivos (como BKT); é um estimador online de parâmetros do tipo Rasch.

## Problema que resolve

Modelos de IRT exigem calibração com amostras grandes e estimação iterativa; BKT e PFA também não são triviais de usar online — tudo isso torna o desenvolvimento de sistemas adaptativos mais caro e demorado [F: pelanek2016elo]. O Elo dá adaptatividade "a partir dos dados", sem entrada de especialista nem recalibração: um parâmetro por aluno e por item, atualizado por equações simples após cada resposta [F: pelanek2016elo]. É particularmente atraente para grupos-alvo médios (conteúdo escolar em línguas pequenas, treinamento corporativo), grandes o bastante para aprender dos dados e pequenos demais para justificar sistemas construídos por especialistas [F: pelanek2016elo].

## Fundamentos e funcionamento

### Equações básicas

Com habilidade θs do aluno s, dificuldade di do item i e resposta correct ∈ {0,1}:

- P(correct = 1) = 1/(1 + e^−(θs − di))
- θs := θs + K · (correct − P(correct = 1))
- di := di + K · (P(correct = 1) − correct)

com valores iniciais 0 e K constante de sensibilidade [F: pelanek2016elo]. A relação com o Rasch é direta: mesma forma funcional de previsão; a diferença está na estimação (máxima verossimilhança na IRT, atualização heurística no Elo) e no pressuposto (habilidade constante na IRT básica, habilidade variável no Elo) [F: pelanek2016elo]. O Elo também corresponde a descida de gradiente estocástica com uma única passada pelos dados, com K no papel da taxa de aprendizado [F: pelanek2016elo].

### Função de incerteza no lugar de K

K pequeno converge devagar; K grande fica instável, dependente das últimas respostas [F: pelanek2016elo]. A melhoria usada na maioria das extensões é uma função de incerteza decrescente no número n de respostas: U(n) = a/(1 + bn), com a = 1, b = 0,05 ajustados por busca em grade — a escolha exata pouco importa [F: pelanek2016elo] [F: papousek2014adaptive]. Variantes: U(n) = w0/(1 + a·e^{bn}) (Wauters et al. 2011) e incerteza atualizada por tempo desde a última tentativa (Klinkenberg et al. 2011), ambas citadas via Pelánek [F: pelanek2016elo]. Abordagens principiadas (Glicko, TrueSkill, filtro de partículas) não trazem vantagem significativa sobre a forma pragmática em modelagem de alunos, e são difíceis de modificar — por exemplo, para a logística deslocada de múltipla escolha [F: pelanek2016elo]. Como itens recebem muito mais respostas que alunos, pode valer usar funções de incerteza diferentes para cada lado [F: pelanek2016elo].

### Extensões educacionais

- **Múltipla escolha**: com k opções, P = 1/k + (1 − 1/k)/(1 + e^−(θs−di)) (logística deslocada) [F: pelanek2016elo].
- **Multivariada**: habilidades correlacionadas por knowledge component; após resposta em KC i, todas as habilidades j são atualizadas com peso c_ij: θsj := θsj + c_ij·K·(correct − P) [F: pelanek2016elo].
- **Aprendizagem assimétrica (PFAE)**: responder é também oportunidade de aprender, então usa-se γ para acertos e δ para erros: θ += γ·(1−P) se correto, θ += δ·P se incorreto; a variante pode ser vista como extensão do PFA, daí o nome "PFA Extended/Elo" [F: pelanek2016elo] [F: papousek2014adaptive].
- **Tempo de resposta**: para problemas em que o tempo é a medida de desempenho, a atualização usa o logaritmo do tempo de solução (log-normalmente distribuído); há também a regra "high speed, high stakes" de Klinkenberg et al. para combinar correção e tempo [F: pelanek2016elo].
- **Memória de curto prazo**: em conhecimento declarativo, o efeito de uma repetição próxima é modelado somando f(t) = w/t à habilidade local, com w = 80 ajustado aos dados [F: pelanek2016elo] [F: papousek2014adaptive]; ver `adp.sr.memory-and-forgetting`.

## Requisitos e pressupostos

- Dados suficientes: pelo menos cerca de 100 alunos para boas estimativas de dificuldade de item [F: pelanek2016elo].
- Domínio de estrutura simples (fatos, vocabulário, habilidades básicas); domínios com pré-requisitos entre habilidades pedem modelos mais ricos [F: pelanek2016elo].
- Para estimação de conhecimento prévio com habilidade global única, homogeneidade de alunos e itens; populações mistas exigem modelos estendidos ou predição por grupo [F: papousek2014adaptive]. Em um teste dessa hipótese com subconjuntos independentes de itens, a correlação entre "sub-habilidades" ficou em torno de 0,6, considerada alta o bastante [F: papousek2014adaptive].

## Vantagens e limitações

Vantagens: simplicidade de implementação (um parâmetro por aluno e por item, só K ou U(n) a configurar); uso online natural; desempenho comparável a modelos mais complexos; atualização de conteúdo barata — item novo entra com dificuldade 0 e o sistema aprende dos dados [F: pelanek2016elo]. Em dados simulados com seleção adaptativa de itens, o Elo produz estimativas de dificuldade quase iguais às da JMLE do Rasch (enquanto a proporção de acertos falha, e não melhora com mais alunos); com o banco estimado, cerca de 10 respostas bastam para estimar a habilidade de um aluno novo com correlação 0,8 com o valor verdadeiro — mitigação do cold start de aluno [F: pelanek2016elo]. Em dados reais de geografia, a correlação entre estimativas do Elo e da JMLE foi 0,97 [F: papousek2014adaptive].

Limitações: não fornece garantias estatísticas sobre as estimativas, ao contrário de modelos IRT bem calibrados usados em CAT — é para prática adaptativa e testes de baixo risco [F: pelanek2016elo]. Por não assumir nada sobre a natureza da aprendizagem, não se deve esperar desempenho ótimo em situações específicas [F: pelanek2016elo]. [I] Herda também o viés de laço fechado de qualquer sistema adaptativo: o modelo determina quais dados são coletados, e superestimar conhecimento faz o sistema parar de coletar a evidência que o contradiria — discussão explícita em [F: papousek2014adaptive].

## Alternativas e comparações

Comparação empírica em prática adaptativa de fatos de geografia (métrica primária RMSE; os autores argumentam que AUC é inadequada quando o valor absoluto da previsão importa) [F: papousek2014adaptive]:

| Modelo | RMSE | AUC |
|---|---|---|
| BKT | 0,262 | 0,668 |
| PFA | 0,265 | 0,669 |
| PFAE | 0,262 | 0,682 |
| PFAE + tempo | 0,259 | 0,714 |

O PFAE venceu BKT e PFA padrão nas três métricas relatadas, e a informação de tempo melhora ainda mais [F: papousek2014adaptive]. Para a estimação de dificuldade de itens, as alternativas são proporção de acertos (falha sob seleção adaptativa) e JMLE da IRT (equivalente em qualidade, inviável online) [F: pelanek2016elo]. Ver tabela mais ampla em `adp.irt.item-response-theory` e `adp.kt.comparison`.

## Contexto empírico publicado

O estudo de caso de Pelánek é um sistema online de prática adaptativa de fatos de geografia (outlinemaps.org / slepemapy.cz) com mais de 1200 itens, mais de 100.000 estudantes e mais de 15 milhões de respostas [F: pelanek2016elo]. Arquitetura modular em três passos independentes: estimação de conhecimento prévio (Elo com habilidade global), estimação de conhecimento corrente (PFAE com efeito de memória de curto prazo) e construção da questão, que mira uma taxa de acerto alvo de 75% e escolhe alvo, tipo de questão e número de opções por funções de escore [F: pelanek2016elo] [F: papousek2014adaptive]. Arquitetura semelhante foi usada para anatomia, testes de direção, gramática tcheca e vocabulário, e o Elo com tempo de resposta para aritmética básica (Math Garden, MatMat) [F: pelanek2016elo].

## Exemplo técnico independente de domínio

Estimador online com função de incerteza e múltipla escolha (equações de [F: pelanek2016elo]):

```
responder(aluno s, item i, correto em {0,1}, k_opcoes):
    P = 1/k + (1 - 1/k) * sigmoide(theta[s] - d[i])    # k=inf -> logistica padrao
    Us = a / (1 + b * n_respostas[s])                   # incerteza do aluno
    Ui = a / (1 + b * n_respostas[i])                   # incerteza do item
    theta[s] += Us * (correto - P)
    d[i]     += Ui * (P - correto)
    n_respostas[s] += 1; n_respostas[i] += 1

# valores de referencia: a = 1, b = 0.05; theta e d iniciam em 0
# variante com aprendizagem (PFAE): usar gamma*(1-P) no acerto e delta*P no erro
```

## Relações com outros conceitos

Depende formalmente do modelo de Rasch descrito em `adp.irt.item-response-theory` (mesma forma funcional, estimação diferente). Alternativa online ao `adp.kt.bayesian-knowledge-tracing` e ao PFA de `adp.kt.logistic-models`, com o PFAE como híbrido. A seleção de questões por taxa de acerto alvo conecta com `adp.adapt.sequencing-policies`; o efeito de memória de curto prazo e esquecimento, com `adp.sr.memory-and-forgetting`; a escolha de métrica (RMSE versus AUC), com `adp.eval.predictive-metrics`.

## Lacunas e questões abertas

- O texto lido de Pelánek (2016) é o accepted manuscript no site do autor; volume e páginas da versão final de Computers & Education não foram verificados (DOI confirmado no próprio manuscrito).
- Klinkenberg et al. (2011), Wauters et al. (2011, 2012), Nižnan et al. (2015) e Pelánek (2014, 2015) são citados aqui apenas via Pelánek (2016) e Papoušek et al. (2014); cópias não foram abertas.
- Não há, nas fontes lidas, avaliação experimental de impacto do Elo em resultado de aprendizagem (pré/pós-teste); os autores apontam a dificuldade de avaliar seleção de questões com validade ecológica [F: papousek2014adaptive].
- Extensões para domínios com pré-requisitos entre habilidades são apontadas como em aberto [F: pelanek2016elo].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| pelanek2016elo | academico | 2026-10-29 |
| papousek2014adaptive | academico | 2026-10-29 |
