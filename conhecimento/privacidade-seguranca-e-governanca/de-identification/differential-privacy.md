---
id: psg.deid.differential-privacy
titulo: Privacidade diferencial
tipo: tecnica
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [dwork2006differential, dworkroth2014algorithmic, nist2025sp800226, nist2023sp800188]
relacoes:
  - { tipo: parte-de, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: alternativa-a, alvo: psg.deid.k-anonymity-and-extensions }
  - { tipo: avaliado-por, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
  - { tipo: relacionado-a, alvo: adp.eval.heterogeneous-populations }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
termos: [privacidade diferencial, epsilon, delta, bases vizinhas, sensibilidade, mecanismo de Laplace, perda de privacidade, orçamento de privacidade, composição, pós-processamento, privacidade de grupo, unidade de privacidade, nível de evento, nível de usuário, modelo central, modelo local, dado sintético]
---

# Privacidade diferencial

## Definição e terminologia

A **privacidade diferencial** é uma definição matemática de privacidade para a divulgação de estatísticas ou de resultados de análise sobre uma base de dados, e não uma técnica específica. Dwork a introduziu em 2006 (Definição 2): uma função aleatorizada K dá epsilon-privacidade diferencial se, para todos os conjuntos de dados D1 e D2 que diferem em no máximo um elemento, e para todo S no contradomínio de K, Pr[K(D1) em S] <= exp(epsilon) * Pr[K(D2) em S] [F: dwork2006differential, §4]. A versão com relaxamento delta, consolidada por Dwork e Roth (Definição 2.4), é: um algoritmo aleatorizado M é (epsilon, delta)-diferencialmente privado se, para todo S e todo par de bases x, y com distância L1 no máximo 1, Pr[M(x) em S] <= exp(epsilon) * Pr[M(y) em S] + delta; quando delta = 0 diz-se epsilon-diferencialmente privado [F: dworkroth2014algorithmic, §2.3]. Bases que diferem em um registro são **vizinhas**; a quantidade ln(Pr[M(x) = xi] / Pr[M(y) = xi]) é a **perda de privacidade** incorrida ao observar a saída xi, e (epsilon, delta)-DP garante que seu valor absoluto fica limitado por epsilon com probabilidade pelo menos 1 - delta [F: dworkroth2014algorithmic, §2.3].

Em linguagem corrente, o NIST SP 800-226 (versão final, março de 2025) descreve a garantia como a semelhança entre dois mundos hipotéticos, com e sem os dados de uma pessoa: a probabilidade de qualquer resultado é "about the same" em ambos, e o quão próximo é governado pelo parâmetro epsilon, também chamado "privacy loss" ou "privacy budget" [F: nist2025sp800226, §2.1 e §2.1.1]. Três propriedades distinguem a DP de técnicas de desidentificação: trata toda informação como potencialmente identificadora; resiste a ataques baseados em dados auxiliares, inclusive os ainda não inventados; e é composicional, de modo que a perda total de várias releases pode ser calculada [F: nist2025sp800226, §1.2 e §2.1.2].

O que não é: não é anonimização de microdados (não há registros "anonimizados" para publicar; o que sai são respostas ou dados sintéticos com ruído) [I]; não é garantia absoluta de sigilo: Dwork demonstra que o desideratum de Dalenius de 1977 ("nothing about an individual should be learnable from the database that cannot be learned without access to the database") é impossível para qualquer mecanismo útil, e que a ameaça vale até para quem não está na base (exemplo da altura de Terry Gross em relação à média das mulheres lituanas) [F: dwork2006differential, resumo e §1].

## Problema que resolve

A impossibilidade de Dalenius obriga a trocar garantias absolutas por relativas: "any given disclosure will be, within a small multiplicative factor, just as likely whether or not the individual participates in the database", de modo que há "only nominal gain to be had by concealing or misrepresenting one's data" [F: dwork2006differential, §4]. Dwork e Roth formulam a promessa em termos econômicos: proteger o indivíduo de qualquer dano adicional que decorra da presença dos seus dados na análise [F: dworkroth2014algorithmic, §2.3.1]. O NIST SP 800-226 acrescenta a motivação prática: desidentificação por redação é vulnerável a ataques de ligação (87% da população dos EUA identificável por sexo, CEP e data de nascimento), e mesmo estatísticas agregadas sofrem ataques de reconstrução, pois "publishing enough statistics will always result in accurate reconstruction attacks" [F: nist2025sp800226, §1.1].

## Fundamentos e funcionamento

**Sensibilidade e mecanismo de Laplace.** A sensibilidade L1 de uma função f é o máximo de ||f(x) - f(y)||_1 sobre pares de bases vizinhas; captura "the magnitude by which a single individual's data can change the function f in the worst case" (Definição 3.1) [F: dworkroth2014algorithmic, §3.3]. O mecanismo de Laplace (Definição 3.3) devolve f(x) + (Y1, ..., Yk) com Yi independentes de Lap(delta_f / epsilon), e preserva (epsilon, 0)-DP (Teorema 3.6) [F: dworkroth2014algorithmic, §3.3]. Dwork já apresentava o mesmo resultado (Teorema 4: ruído exponencial simétrico de escala sigma dá delta_f/sigma-DP; para epsilon-DP escolhe-se sigma >= delta_f / epsilon) e observava que consultas de contagem têm sensibilidade 1 e que, em histogramas, a sensibilidade da consulta vetorial inteira é 1 e não k [F: dwork2006differential, §5.1]. Alternativamente, ruído gaussiano calibrado dá (epsilon, delta)-DP [F: dworkroth2014algorithmic, §3.3, nota 1].

**Pós-processamento, composição e grupos.** Qualquer função dos resultados de um mecanismo (epsilon, delta)-DP, sem acesso à base, continua (epsilon, delta)-DP (Proposição 2.1) [F: dworkroth2014algorithmic, §2.3]. A composição de k mecanismos (epsilon_i, delta_i)-DP é (soma de epsilon_i, soma de delta_i)-DP (Teorema 3.16, "the epsilons and the deltas add up"), com limites mais finos no teorema de composição avançada (Teorema 3.20) [F: dworkroth2014algorithmic, §2.3 e §3.5]. Um mecanismo (epsilon, 0)-DP é (k*epsilon, 0)-DP para grupos de k pessoas (Teorema 2.2), o que "addresses, for example, the question of privacy in surveys that include multiple family members"; a garantia enfraquece linearmente com o tamanho do grupo e, como os autores notam, deve-se esperar que "privacy bounds disintegrate with increasing group size", já que o objetivo é revelar agregados sobre grupos grandes [F: dworkroth2014algorithmic, §2.3; dwork2006differential, §4].

**Orçamento de privacidade.** Pela composição, epsilon funciona como orçamento: dez análises com epsilon_i = 0,1 consomem epsilon total = 1; epsilon é um limite superior da perda, não uma medida dela [F: nist2025sp800226, §2.2]. Dwork e Roth advertem que valores de epsilon da ordem de 1/||x||_1 (inverso do tamanho da base) "are very dangerous": permitem "preservar privacidade" publicando os registros completos de poucos participantes [F: dworkroth2014algorithmic, §2.3].

**Unidade de privacidade.** A definição de "vizinhança" fixa o que é protegido. Em **nível de evento**, bases vizinhas diferem em uma transação ou linha; em **nível de usuário**, diferem em todos os dados de uma pessoa. O NIST mostra que o nível de evento "can result in surprisingly weak privacy guarantees": protege uma visita a uma URL mas não visitas repetidas, uma viagem de táxi mas não os destinos habituais, uma leitura de medidor mas não a tendência de consumo; limitar a contribuição total de cada usuário converte a garantia em nível de usuário, e limites que se renovam por dia ou mês protegem só o período [F: nist2025sp800226, §2.4.2]. O NIST afirma que "the safest default for any differential privacy guarantee is user-level privacy or a total contribution bound" [F: nist2025sp800226, §2.4.2]. Para séries de interação de aprendizes, isso significa que a unidade relevante é o aluno, não o evento de clique [I].

**Modelos de confiança.** No **modelo central**, um curador confiável guarda os dados e adiciona ruído às respostas, com a menor quantidade de ruído possível; no **modelo local**, cada indivíduo adiciona ruído aos próprios dados antes de enviá-los, eliminando o curador confiável ao custo de mais ruído [F: nist2025sp800226, §4.2.1 e §4.2.2]. A DP também pode gerar dados sintéticos: o NIST SP 800-188 observa que gastar o orçamento na criação de um dataset sintético, em vez de em consultas interativas, dá resultados consistentes para todos os usuários [F: nist2023sp800188, §4.5].

## Requisitos e pressupostos

- Consultas com sensibilidade conhecida e limitada; funções com sensibilidade alta (máximos, somas sem limite) exigem recorte (*clipping*) de contribuições [I, consequência direta da Definição 3.1].
- Uma unidade de privacidade escolhida explicitamente e documentada; o NIST trata a escolha de epsilon e da unidade como "the most direct measure of the strength of a differential privacy guarantee" [F: nist2025sp800226, §1 e §2.4].
- Contabilidade do orçamento ao longo de todas as releases e análises, inclusive futuras, pois a perda acumula [F: nist2025sp800226, §2.2; nist2023sp800188, §4.3.11].
- Fonte de aleatoriedade adequada e implementação correta; o NIST lista desafios de implementação (canais laterais, ponto flutuante) na seção 4.3 [F: nist2025sp800226, sumário §4.3; conteúdo não lido em detalhe nesta sessão].
- No modelo central, um curador de fato confiável; a falta de confiança no coletor é "often a primary motivation" para a DP e leva ao modelo local [F: nist2025sp800226, §4.2.1].

## Vantagens e limitações

Vantagens: definição rigorosa; resistência a dados auxiliares presentes e futuros; composição que permite calcular a perda máxima de duas releases (epsilon = 1 e epsilon = 1,5 somam no máximo 2,5), "not true of most other de-identification techniques" [F: nist2025sp800226, §1.2; nist2023sp800188, §4.3.11]; imunidade a pós-processamento [F: dworkroth2014algorithmic, §2.3].

Limitações: a escolha de epsilon é problema em aberto; o NIST afirma que "we offer no specific guidelines on their selection", registra que um estudo sugere epsilon de 0,1 como proteção forte e valores abaixo de 1 como razoáveis, que muitas implantações usaram 1 < epsilon <= 20, e que releases com epsilon >= 10 podem deixar *outliers* vulneráveis (dados sintéticos com epsilon = 10 sujeitos a ataques de ligação; redes neurais com epsilon = 10 e dados de treino adversariais vazando informação) [F: nist2025sp800226, §2.2]. O ruído tem escala delta_f/epsilon independente do tamanho da base, logo o erro relativo é maior em contagens pequenas: subgrupos raros (uma turma, alunos com uma característica incomum) são os mais afetados [I, consequência do mecanismo de Laplace]. A utilidade pode falhar de forma relevante: o NIST relata que um modelo de dosagem de varfarina treinado com dados modificados segundo a DP "produced higher mortality rates in simulation" que o modelo sem alteração [F: nist2023sp800188, §3.2.3, nota 21]. A DP também pode introduzir viés estatístico, tema da seção 3.3 do SP 800-226 [F: nist2025sp800226, sumário §3.3; não lido em detalhe]. Ferramentas, padrões e boas práticas ainda "are not easily accessible outside of academic research communities" [F: nist2025sp800226, §1.2].

## Alternativas e comparações

| Critério | k-anonimato e extensões | Privacidade diferencial (central) | Privacidade diferencial (local) | Enclave com revisão manual |
|---|---|---|---|---|
| Natureza da garantia | Propriedade sintática da tabela publicada | Limite probabilístico sobre qualquer saída | Idem, sem curador confiável | Nenhuma formal; depende da revisão |
| Resistência a dados auxiliares futuros | Não [F: nist2023sp800188, §2.2] | Sim [F: nist2025sp800226, §1.2] | Sim | Depende do que sai |
| Perda acumulada entre releases | Não calculável [F: nist2023sp800188, §4.3.11] | Soma de epsilons [F: dworkroth2014algorithmic, Teorema 3.16] | Idem | Não calculável |
| Saída | Microdados | Estatísticas, modelos ou dado sintético | Dados individuais ruidosos | Resultados aprovados |
| Custo em utilidade | Supressão e generalização | Ruído proporcional a delta_f/epsilon | Ruído maior que no central | Baixo, mas lento |

## Métricas e métodos de avaliação

Epsilon e delta por release e acumulados; unidade de privacidade (evento, usuário, limite de contribuição); acurácia das respostas (erro absoluto ou relativo esperado dado o ruído) e viés; a publicação dos parâmetros, que o NIST diz estabelecer confiança sem criar risco adicional [F: nist2025sp800226, §2.2]. O NIST menciona auditorias e medidas empíricas de privacidade (seção 2.7) e o Collaborative Research Cycle como esforço de benchmarking de algoritmos de desidentificação com métricas de fidelidade, utilidade e privacidade [F: nist2025sp800226, §2.2 e sumário §2.7].

## Exemplo técnico independente de domínio

```
estado: orcamento_total := 1.0; gasto := 0.0        # epsilon total aceito para a base
unidade := "usuario"; limite_contribuicao := 1      # cada pessoa conta no máximo uma vez por consulta

função contar_privado(base, predicado, epsilon):
    exigir gasto + epsilon <= orcamento_total
    contagem := número de usuários distintos em base que satisfazem predicado   # sensibilidade 1
    ruido := amostra de Laplace(escala = 1 / epsilon)
    gasto := gasto + epsilon
    registrar(consulta, epsilon, gasto, data)
    retornar contagem + ruido

# histograma por categoria: uma consulta vetorial de sensibilidade 1 (cada usuário em uma célula)
função histograma_privado(base, atributo, epsilon):
    exigir gasto + epsilon <= orcamento_total
    para cada categoria c: h[c] := contagem(base, atributo = c) + Laplace(1 / epsilon)
    gasto := gasto + epsilon
    retornar h          # pós-processamento (arredondar, truncar negativos) não consome orçamento
```

## Relações com outros conceitos

Parte de `psg.deid.anonymization-and-pseudonymization` como a família de garantias formais; alternativa a `psg.deid.k-anonymity-and-extensions`; avaliada por `psg.deid.reidentification-risk` no sentido de que epsilon é o limite de perda e os estudos de reidentificação medem se o limite escolhido foi suficiente. Relaciona-se com `lae.dq.bias-and-validity` (ruído e viés em indicadores) e com `adp.eval.heterogeneous-populations` (grupos pequenos recebem erro relativo maior). Relaciona-se com `psg.access.minimization-and-privacy-by-design`: o modelo local e o limite de contribuição são formas de minimizar o que o curador precisa guardar.

## Lacunas e questões abertas

- Não há, nas fontes consultadas, recomendação de epsilon para dados educacionais ou de menores; o NIST espera que "domain and task-specific best practices will start to emerge with time" [F: nist2025sp800226, §2.2].
- O SP 800-226 foi lido nas seções 1, 2.1, 2.2, 2.4 e 4.2; as seções sobre variantes (2.3), viés (3.3), aprendizado de máquina (3.5) e desafios de implementação (4.3) não foram lidas e ficam para expansão.
- Como combinar DP (para estatísticas publicadas) com pseudonimização (para a base longitudinal interna) num mesmo programa de pesquisa, e como registrar isso no RIPD, não foi encontrado em fonte normativa.
- Aplicação a modelos de aluno treinados com DP (DP-SGD) e seu impacto em subgrupos de alunos com deficiência: sem fonte verificada nesta sessão [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| dwork2006differential | academico | 2026-10-29 |
| dworkroth2014algorithmic | academico (livro, texto aberto no site dos autores) | 2026-10-29 |
| nist2025sp800226 | tecnico | 2026-10-29 |
| nist2023sp800188 | tecnico | 2026-10-29 |
