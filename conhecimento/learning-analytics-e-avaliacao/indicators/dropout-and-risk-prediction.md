---
id: lae.ind.dropout-and-risk-prediction
titulo: Sistemas de alerta precoce e predição de risco de evasão
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [jayaprakash2014earlyalert, arnold2012coursesignals, caulfield2013coursesignals, baker2022bias]
relacoes:
  - { tipo: relacionado-a, alvo: lae.found.analytics-cycle }
  - { tipo: depende-de, alvo: lae.ind.engagement-indicators }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
  - { tipo: alternativa-a, alvo: lae.ind.dashboards-and-olm }
termos: [early warning system, EWS, alerta precoce, risco acadêmico, evasão, predição de evasão, falso positivo, falso negativo, profecia autorrealizável, viés algorítmico, equidade]
---

# Sistemas de alerta precoce e predição de risco de evasão

## Definição e terminologia

Um *early warning system* (EWS), ou sistema de alerta precoce, é um sistema que usa dados históricos e correntes do aluno para estimar, durante o curso ou programa — idealmente cedo o suficiente para permitir intervenção —, a probabilidade de um resultado acadêmico indesejado: reprovação em uma disciplina, evasão da disciplina ou do programa, ou não formatura [I, a partir da descrição dos sistemas revisados]. Jayaprakash et al. descrevem o objetivo de um desses sistemas como "prever estudantes 'em risco' nas semanas iniciais de um curso" para então acionar uma intervenção [F: jayaprakash2014earlyalert, p.(abstract/introdução)].

O que um EWS não é: não é, em si, a intervenção — é o componente de predição que decide quem recebe uma ação (email, contato de um orientador, sinalização ao professor); a eficácia do sistema combina a qualidade da predição com a qualidade e a adesão à intervenção subsequente, que é frequentemente avaliada separadamente [I]. Também não deve ser confundido com um modelo de aluno cognitivo de sistemas tutores (knowledge tracing, ver domínio `aprendizagem-adaptativa`): o alvo aqui é um resultado acadêmico agregado (aprovação, permanência), não o domínio de uma habilidade específica.

## Problema que resolve

Em turmas grandes ou em educação a distância, um professor não consegue identificar, por inspeção visual do desempenho, quais alunos estão em risco antes que seja tarde para agir — Jayaprakash et al. observam que a abordagem orientada a dados permite ao professor fazer predições de desempenho do aluno muito mais cedo no semestre (2 a 3 semanas após o início do curso), em comparação ao que o professor conseguiria perceber por inspeção visual, tipicamente só depois da prova intermediária [F: jayaprakash2014earlyalert, p.35]. O EWS resolve esse problema de informação tardia, trocando a espera por uma nota de prova por uma estimativa baseada em sinais disponíveis mais cedo (notas parciais, frequência, interação na plataforma).

## Fundamentos e funcionamento

### Variáveis preditoras típicas

A literatura converge em um conjunto relativamente estável de famílias de variáveis preditoras:

- **Desempenho prévio e corrente**: GPA cumulativo, notas parciais já lançadas no sistema de gestão da aprendizagem (LMS). No estudo da Open Academic Analytics Initiative (OAAI), a pontuação agregada de contribuições parciais para a nota final, extraída do gradebook do LMS (variável `RMN_SCORE_PARTIAL`), aparece como o preditor mais relevante do modelo de regressão logística, seguida por GPA cumulativo e situação acadêmica (`academic standing`) [F: jayaprakash2014earlyalert, p.26-27].
- **Frequência e interação na plataforma**: número de sessões logadas no sistema (no caso do OAAI, sessões no Sakai, `R_SESSIONS`) — um aumento no número de sessões reduziu a probabilidade esperada de estar em risco, controlando pelos demais preditores [F: jayaprakash2014earlyalert, p.27].
- **Modalidade e situação do aluno**: status online vs. presencial (`ONLINE_FLAG`), status de tempo integral vs. parcial (`RC_FTPT`), ano/classe do aluno (`RC_CLASS`) — por exemplo, alunos de tempo parcial tiveram razão de chances de estar em risco (vs. em situação regular) 2,443 vezes maior que alunos de tempo integral, controlando pelos demais preditores, no modelo do OAAI [F: jayaprakash2014earlyalert, p.27].
- **Dados socioeconômicos e demográficos**: usados em outros sistemas da literatura (por exemplo, o Course Signals de Purdue incorporou características demográficas e histórico acadêmico pregresso, além de notas e de esforço medido pela interação com o LMS Blackboard Vista) [F: arnold2012coursesignals, descrição consolidada por fontes secundárias — ver nota nas fontes].

### O caso do Course Signals (Purdue): sistema de referência na literatura de pesquisa

O Course Signals, descrito por Arnold e Pistilli (2012) nos anais da LAK 2012, é citado com frequência na literatura acadêmica de learning analytics como um dos primeiros EWS implementados em escala em uma instituição, por isso é tratado aqui como caso de estudo de pesquisa — não como produto a ser adotado — e com as ressalvas metodológicas documentadas abaixo [F: arnold2012coursesignals, metadados]. O sistema combinava notas, características demográficas, histórico acadêmico e esforço (medido por interação com o LMS) para gerar, para cada aluno em cada disciplina participante, um "sinal" visual (vermelho, amarelo ou verde) exibido ao próprio aluno, acompanhado de contato personalizado do professor [F: arnold2012coursesignals, metadados].

Entre 2007 e os anos seguintes, relatos institucionais (não o artigo acadêmico em si) descreveram ganhos de retenção associados ao uso do sistema — por exemplo, alunos que passaram por ao menos uma disciplina com Course Signals tendo taxa de retenção relatada de 87,42%, contra 69,40% entre os que não passaram, segundo descrição consolidada por fonte secundária (EDUCAUSE Review) [F: arnold2012coursesignals, descrição secundária; não verificado em texto primário nesta sessão]. Essa mesma fonte secundária já registra que a comparação não corresponde a um experimento controlado [F: arnold2012coursesignals, descrição secundária].

A crítica metodológica mais específica a essa alegação de retenção vem de análises publicadas fora do artigo original: Michael Caulfield, em 2013, propôs que o efeito observado poderia ser artefato de causalidade reversa — alunos que já tendiam a permanecer matriculados (por razões não relacionadas ao sistema) acabavam cursando mais disciplinas com Course Signals simplesmente por cursarem mais disciplinas no total, e não o contrário [F: caulfield2013coursesignals]. Uma simulação matemática construída por Alfred Essa, incorporando essa hipótese de causalidade reversa, reproduziu os padrões anômalos observados nos dados de Purdue (por exemplo, um efeito de retenção forte ao cursar duas disciplinas com o sistema, mas efeito nulo ou levemente negativo ao cursar apenas uma) sem supor qualquer efeito causal do próprio sistema [F: caulfield2013coursesignals]. A resposta de Purdue a essa análise, segundo o mesmo relato, não tratou diretamente da hipótese de causalidade reversa levantada [F: caulfield2013coursesignals].

### O caso da Open Academic Analytics Initiative (OAAI): avaliação de transferência entre instituições

Jayaprakash et al. (2014) relatam um esforço multi-institucional (Marist College como instituição de origem do modelo, testado depois em quatro instituições parceiras, incluindo community colleges e uma HBCU) para avaliar se um modelo preditivo treinado em uma instituição se mantém útil em outras, com contextos educacionais, demografia e taxas de retenção muito diferentes [F: jayaprakash2014earlyalert, p.34]. Usando *recall* (percentual de alunos em risco corretamente identificados) como indicador, o desempenho médio nas instituições parceiras ficou por volta de 74,5% em três das quatro instituições, chegando a 84,5% em uma rodada e caindo a 61% em outra — uma diferença de apenas cerca de 10 pontos percentuais em relação ao desempenho do modelo nos dados de origem (Marist), resultado que os autores descrevem como "surpreendente e encorajador" dada a expectativa de uma diferença bem maior [F: jayaprakash2014earlyalert, p.34-35]. Uma quarta instituição (identificada como NCAT) teve desempenho bem mais fraco, com *recall* médio de 52% — valor "bem abaixo" dos das demais, o que os autores assinalam merecer investigação adicional [F: jayaprakash2014earlyalert, p.35].

## Requisitos e pressupostos

- Disponibilidade de dados de desempenho (gradebook) e de interação (log de LMS) já nas primeiras semanas do período letivo; Jayaprakash et al. notam que, sem contribuições parciais para a nota final e/ou GPA cumulativo disponíveis, o modelo pode não se transferir bem a outros contextos institucionais, como programas de capacitação sem crédito acadêmico [F: jayaprakash2014earlyalert, p.35].
- Um atributo-alvo claro e mensurável no histórico (reprovação, evasão, não-retorno no período seguinte) para treinar o modelo supervisionado.
- Para auditoria de equidade do sistema, disponibilidade do atributo protegido (raça, gênero, status socioeconômico) nos dados — e Baker e Hawn observam, em outro contexto de modelagem educacional, que restrições de privacidade sobre justamente os atributos mais sensíveis podem impedir a própria pesquisa que detectaria o viés [F: baker2022bias].

## Vantagens e limitações

Vantagem central: antecipação. Um EWS bem calibrado permite intervenção semanas antes do que a inspeção humana tradicional possibilitaria [F: jayaprakash2014earlyalert, p.35].

Limitações e riscos documentados na literatura:

- **Falsos positivos e falsos negativos têm custo desigual e variam por subgrupo.** Baker e Hawn, revisando a literatura de viés algorítmico em aplicações educacionais (incluindo predição de risco de evasão e de reprovação), relatam que Anderson et al. (2019), ao diferenciar desempenho de um modelo de predição de formatura em seis anos por grupo racial/étnico, encontraram taxas de falso positivo mais altas para alunos brancos e taxas de falso negativo mais altas para alunos latinos, através de cinco algoritmos distintos [F: baker2022bias, p.15]. No recorte de gênero, o mesmo estudo de Anderson et al. encontrou taxas de falso negativo geralmente mais altas para alunos do sexo masculino [F: baker2022bias, p.16]. Hu e Rangwala (2020), analisando modelos de risco de reprovação em disciplina, encontraram desempenho geralmente pior para alunos afro-americanos, embora esse resultado não fosse consistente entre diferentes disciplinas universitárias [F: baker2022bias, p.15]. Em contraste, Christie et al. (2019) encontraram diferenças muito pequenas na qualidade de um modelo de evasão escolar por raça, possivelmente porque incluíram proxies de raça entre os preditores [F: baker2022bias, p.15].
- **Instabilidade entre instituições, períodos e subpopulações pequenas.** O próprio estudo do OAAI relatou queda de desempenho em uma das quatro instituições parceiras e variação entre semestres (primavera vs. outono de 2012), além de taxa média de falsos alarmes mais alta nas instituições parceiras (26%, com picos de 43%) do que nos dados de origem [F: jayaprakash2014earlyalert, p.35-36]. Baker e Hawn relatam, em outro estudo revisado (Anderson et al. 2019), que o desempenho do modelo foi "muito instável" para o subgrupo de alunos indígenas, presente em apenas 44 de mais de 14.000 casos da amostra [F: baker2022bias, p.15] — ilustrando como subgrupos pouco representados nos dados de treino produzem estimativas de risco pouco confiáveis para esses mesmos alunos.
- **Risco de profecia autorrealizável.** Quando a predição de risco é exibida a professores ou orientadores antes de qualquer verificação independente, existe o risco de que a expectativa gerada pelo rótulo "em risco" influencie o tratamento dado ao aluno (menos oportunidades, menor investimento pedagógico), reforçando o resultado previsto em vez de preveni-lo [I — mecanismo amplamente discutido na literatura de ciência de dados aplicada a políticas sociais; não foi localizada, nesta pesquisa, uma medição empírica desse efeito especificamente em EWS educacionais, o que fica registrado como lacuna].
- **Disputa sobre a própria validade causal do efeito reportado.** O episódio do Course Signals mostra que mesmo o indicador de desfecho mais básico de um EWS — "alunos expostos ao sistema se formam/permanecem mais" — pode ser artefato de seleção/causalidade reversa em vez de efeito do sistema, se a análise não isolar adequadamente quem já tinha maior probabilidade de permanecer matriculado por outras razões [F: caulfield2013coursesignals].

## Alternativas e comparações

| Abordagem | Granularidade da decisão | Principal risco documentado | Exemplo nesta pesquisa |
|---|---|---|---|
| Modelo único treinado localmente | específica à instituição | menor risco de desajuste de contexto, mas não transferível | modelo do OAAI testado apenas em Marist |
| Modelo treinado em uma instituição e transferido a outras | entre instituições | queda de desempenho em contextos muito diferentes do de origem | OAAI aplicado a quatro instituições parceiras, recall caindo a 52% em uma delas [F: jayaprakash2014earlyalert, p.35] |
| Sinal institucional amplo com intervenção padronizada (semáforo) | curso/aluno | opacidade do modelo para quem recebe o sinal; risco de profecia autorrealizável | Course Signals (Purdue) |

## Métricas e métodos de avaliação

Jayaprakash et al. reportam e comparam classificadores (regressão logística, SVM/SMO, entre outros) usando recall (percentual de alunos em risco corretamente identificados), taxa de falso positivo e precisão como métricas centrais, preferindo essas métricas à acurácia simples por causa do desbalanceamento de classes (poucos alunos efetivamente evadem ou reprovam, frente ao total) [F: jayaprakash2014earlyalert, p.26]. No conjunto de treino do OAAI, a regressão logística superou os demais classificadores testados, combinando recall acima de 84%, taxa de falso positivo abaixo de 13% e precisão próxima de 33% [F: jayaprakash2014earlyalert, p.26]. Para auditoria de equidade entre subgrupos, a literatura mais ampla de viés algorítmico em educação (não específica a EWS) usa métricas de paridade de taxas de erro entre grupos — ver `lae.dq.bias-and-validity` (documento planejado) para o tratamento mais geral dessas métricas.

## Exemplo técnico independente de domínio

Esboço do ciclo típico de um sistema de alerta precoce, incluindo o ponto em que a crítica de equidade e de causalidade se aplica:

```
entrada: histórico_academico(aluno), dados_lms(aluno, periodo_corrente)

treinar(modelo, historico_academico_com_desfecho_conhecido)
    # desfecho_conhecido = reprovou? evadiu? nao retornou?

a cada marco do periodo (ex.: 25%, 50%, 75% do curso):
    para cada aluno ativo:
        score_risco = modelo.prever(dados_lms[aluno, periodo_corrente])
        se score_risco > limiar:
            emitir_alerta(aluno, professor_ou_orientador)

    # pontos de atenção obrigatórios antes de agir sobre o alerta:
    auditar_taxa_erro_por_subgrupo(modelo, atributo_protegido)   # falso positivo/negativo desigual?
    checar_desenho_da_intervencao(alerta)                         # intervenção reforça estigma (profecia
                                                                   # autorrealizável) ou oferece apoio concreto?
    nao_inferir_causalidade_do_desfecho_agregado(modelo, dados)   # correlação de exposição != efeito causal
```

## Relações com outros conceitos

Relaciona-se com `lae.found.analytics-cycle` como uma das aplicações mais visíveis do ciclo de learning analytics (coletar, modelar, agir). Depende de indicadores de interação e frequência descritos em `lae.ind.engagement-indicators` como parte do conjunto de variáveis preditoras. A crítica de equidade e de falsos positivos/negativos desiguais entre subgrupos é um caso específico do problema mais geral tratado em `lae.dq.bias-and-validity` (relação `relacionado-a`; documento planejado neste domínio). É `alternativa-a` `lae.ind.dashboards-and-olm` no sentido de que ambos expõem um juízo de risco/progresso ao usuário, mas um EWS tipicamente empurra um alerta de forma automática e dirigida (push), enquanto um dashboard expõe informação para consulta (pull) [I].

## Lacunas e questões abertas

- O artigo de Arnold e Pistilli (2012, LAK12) não foi acessado em texto completo nesta sessão — a página do ACM Digital Library retornou HTTP 403 e nenhuma cópia aberta foi localizada. As afirmações sobre o funcionamento do sistema e os números de retenção vêm de descrições consolidadas por fontes secundárias (artigo do EDUCAUSE Review de 2012 e cobertura posterior), não do artigo acadêmico original; qualquer detalhe metodológico do artigo (por exemplo, especificação exata do modelo preditivo usado) permanece não verificado.
- A crítica de Caulfield e a simulação de Essa foram publicadas como posts de blog (e-Literate, 2013), não como artigo revisado por pares; são tratadas aqui como fonte secundária informada, mas não substituem uma réplica acadêmica publicada. Não foi localizada, nesta pesquisa, uma reanálise estatística formal e revisada por pares dos dados originais de Purdue que confirme ou refute especificamente a hipótese de causalidade reversa.
- Não foi localizada, nas fontes revisadas nesta sessão, uma medição empírica direta do efeito de profecia autorrealizável em sistemas de alerta precoce educacionais (ou seja, um estudo que isole o efeito de mostrar o rótulo de risco a um professor sobre o tratamento dado ao aluno, independentemente da acurácia do modelo); a menção a esse risco neste documento é uma inferência de mecanismo plausível, não um resultado medido [H].
- O estudo do OAAI não detalha, nas seções lidas nesta pesquisa, por que o desempenho foi consideravelmente mais fraco na quarta instituição parceira (NCAT); os próprios autores assinalam isso como questão em aberto [F: jayaprakash2014earlyalert, p.35].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| jayaprakash2014earlyalert | academico | 2026-10-29 |
| arnold2012coursesignals | academico (apenas metadados; conteúdo via fonte secundária) | 2026-10-29 |
| caulfield2013coursesignals | secundario | 2026-10-29 |
| baker2022bias | academico | 2026-10-29 |
