---
id: adp.eval.heterogeneous-populations
titulo: Limitações para populações heterogêneas e necessidades educacionais específicas
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [baker2022bias, gardner2019slicing, castudl2024, pelanek2015metrics]
relacoes:
  - { tipo: complementa, alvo: adp.eval.predictive-metrics }
  - { tipo: complementa, alvo: adp.eval.evaluation-protocols }
  - { tipo: relacionado-a, alvo: adp.eval.educational-effectiveness }
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: adp.lm.open-learner-model }
termos: [viés algorítmico, fairness, ABROCA, slicing analysis, não-malealidade, Universal Design for Learning, bias desconhecido, bias conhecido]
---

# Limitações para populações heterogêneas e necessidades educacionais específicas

## Definição e terminologia

Viés algorítmico em educação é a situação em que um algoritmo — um modelo de aluno, um detector de afeto, um classificador de risco de evasão — produz predições ou decisões sistematicamente menos precisas, ou sistematicamente mais prejudiciais, para um subgrupo específico de alunos [F: baker2022bias]. Baker e Hawn, cuja revisão é a fonte central deste documento, adotam deliberadamente uma definição restrita e operacional em vez de uma definição puramente matemática de justiça (*fairness*): propõem um "teste de não-maleabilidade" (*non-malleability test*) para decidir quais categorias devem ser consideradas em termos de viés algorítmico — um estudante pode escolher gamificar um sistema, e o projetista pode desenhar experiências menos sujeitas a isso, mas um professor ou projetista não pode mudar a raça, localização nacional ou gênero de um estudante [F: baker2022bias]. Esse teste aponta outras categorias relevantes: onde o aluno mora (em granularidade mais fina que o país), origem nacional, status socioeconômico, língua nativa, deficiências, idade, e situação de trabalho dos pais que afeta mobilidade do estudante (trabalho migrante ou ocupações de alto risco, como as militares) [F: baker2022bias]. *Fairness* (justiça algorítmica), nesse contexto, é usualmente operacionalizada como diferença de acurácia preditiva entre subgrupos definidos por essas categorias — não como uma propriedade única e consensual, dado que há múltiplas definições formais concorrentes de justiça na literatura de machine learning mais ampla [F: gardner2019slicing]. O que viés algorítmico em educação **não é**: não é, segundo Baker e Hawn, necessariamente o mesmo que desempenho desigual causado pela escolha intencional do próprio aluno (como "jogar o sistema" para obter respostas corretas sem aprender) — esse tipo de diferença de acurácia é descartado pelo teste de não-maleabilidade, porque o comportamento é escolhido, não uma característica imutável do aluno [F: baker2022bias].

## Problema que resolve

Modelos de aluno são tipicamente ajustados e validados sobre uma população agregada (ver `adp.eval.evaluation-protocols`), e uma métrica de desempenho global (ver `adp.eval.predictive-metrics`) pode ser boa mesmo quando o modelo funciona mal para subgrupos específicos — porque o agregado é dominado pelo subgrupo majoritário [I, inferido do uso de slicing analysis em gardner2019slicing]. Isso é especialmente relevante quando o modelo guia decisões de alto risco: alocação de conteúdo adaptativo, sinalização de risco de evasão, pontuação automática de redação [F: baker2022bias]. O caso tornado público mais citado por Baker e Hawn é a controvérsia de notas do GCSE e A-Level no Reino Unido em 2020, em que uma fórmula (desenvolvida manualmente, não por um algoritmo automatizado, pelo órgão regulador nacional de qualificações) atribuiu notas previstas piores a estudantes de escolas públicas e notas melhores — inclusive melhores que a predição do próprio professor — a estudantes de escolas independentes menores [F: baker2022bias]. Modelos de knowledge tracing e analytics de aprendizagem enfrentam o mesmo risco estrutural, mas, segundo os autores, a pesquisa empírica sobre exatamente quais grupos são afetados, e em que estágio do pipeline de desenvolvimento, ainda é "muito esparsa" [F: baker2022bias].

## Fundamentos e funcionamento

### Evidência empírica por categoria populacional

Baker e Hawn organizam a evidência empírica revisada por categoria de subpopulação, distinguindo categorias "fortemente estudadas" (raça/etnia, gênero, nacionalidade) de categorias "pouco estudadas". Para o escopo deste documento — populações heterogêneas e necessidades educacionais específicas —, os achados mais relevantes nas categorias pouco estudadas são:

- **Deficiências (disabilities).** Paquette e colaboradores (citados por Baker e Hawn) observam que "muito poucos" artigos publicados em educational data mining entre 2015 e 2019 consideram o status de deficiência do aluno; dos que consideram, a maioria foca em *detectar* se um aluno tem deficiência, não em avaliar se outro modelo é enviesado em relação a esse status [F: baker2022bias]. Ainda assim, os autores identificam pelo menos dois estudos que investigam viés algorítmico ligado a deficiência: Loukina e Buzick avaliaram um sistema de reconhecimento de fala usado em teste de fluência de inglês (SpeechRater) e encontraram acurácia muito menor para alunos que aparentavam ter um transtorno de fala (segundo anotação de aplicadores de teste) mas não haviam solicitado acomodação, em comparação com alunos sem transtorno aparente ou que haviam solicitado acomodação [F: baker2022bias]. Riazy e colaboradores investigaram se a predição de resultado de curso era afetada por status de deficiência autorrelatado e encontraram que alunos com deficiência tinham desempenho pior no curso e que os algoritmos geralmente **superestimavam** o sucesso desses alunos, embora a evidência de diferença de qualidade de predição fosse "razoavelmente fraca" [F: baker2022bias].
- **Urbanicidade.** Ocumpaugh e colaboradores estudaram detectores de confusão, frustração, tédio e concentração engajada treinados em populações urbana, suburbana, rural e combinada; detectores foram geralmente mais eficazes para alunos novos dentro da população em que foram treinados do que para outras populações, e um detector treinado na população combinada funcionou melhor para alunos urbanos e suburbanos do que para rurais — efeito que os autores atribuem a diferenças reais de urbanicidade, não a raça ou status socioeconômico de confusão, já que suburbano e rural tinham perfil racial semelhante, e urbano e rural tinham perfil socioeconômico semelhante [F: baker2022bias]. Em contraste, Samei e colaboradores testaram detectores de atributos de perguntas em sala de aula treinados em dados urbanos e não-urbanos (e vice-versa) e não encontraram degradação de desempenho [F: baker2022bias].
- **Status socioeconômico.** Yudelson e colaboradores treinaram e testaram modelos entre escolas com proporções alta, média e baixa de alunos elegíveis para almoço gratuito ou a preço reduzido (proxy comum de status socioeconômico nos EUA) e encontraram que modelos treinados em escolas com alta proporção de alunos de baixo SES não funcionavam tão bem em outras escolas, mas modelos treinados em outras escolas funcionavam igualmente bem nas escolas de baixo SES — com diferenças, porém, pequenas em magnitude [F: baker2022bias].
- **Língua nativa e dialeto.** Há evidência de viés em pontuação automática de redação relacionada a diferenças sistemáticas de nota entre falantes de línguas nativas diferentes com proficiência comparável (por exemplo, falantes de árabe recebendo notas sistematicamente mais baixas que falantes de chinês) [F: baker2022bias]. Os autores afirmam explicitamente não terem conseguido identificar nenhum trabalho sobre viés algorítmico relacionado especificamente a **dialeto** do aluno em educação — em contraste com atenção relativamente maior a dialeto em pesquisa de viés algorítmico fora da educação [F: baker2022bias].
- **Status de conexão militar.** Baker, Berning e Gowda treinaram modelos de predição de formatura no ensino médio e nota do SAT em alunos sem conexão militar na família e testaram em alunos com conexão militar (e vice-versa), encontrando evidência de degradação moderada de qualidade do modelo [F: baker2022bias].

### Medindo desempenho desigual: slicing analysis e ABROCA

Gardner, Brooks e Baker propõem um método para avaliar injustiça (*unfairness*) em modelos preditivos de aluno chamado "slicing analysis": avaliar o desempenho do modelo separadamente para cada fatia (*slice*) definida por um atributo protegido (por exemplo, gênero), em vez de apenas reportar um número agregado [F: gardner2019slicing]. Para quantificar a diferença, os autores introduzem uma métrica nova, ABROCA (*Absolute Between-ROC Area*), que mede a área absoluta entre as curvas ROC de dois subgrupos — uma forma de capturar diferença de acurácia que não depende de escolher um único limiar de classificação [F: gardner2019slicing]. Em um estudo de caso de modelos de evasão (*dropout*) de MOOC, aplicando cinco modelos replicados da literatura a um conjunto de 44 MOOCs distintos e mais de quatro milhões de alunos, os autores encontram: (1) diferenças significativas de justiça (medida por ABROCA) conforme o algoritmo estatístico e o conjunto de features usados; (2) que a razão de desbalanceamento de gênero, a área curricular e o curso específico usado para treinar um modelo têm associação significativa com o valor de ABROCA; e (3) que não há evidência de um *tradeoff* estrito entre desempenho preditivo e justiça — ou seja, não é necessário, em geral, sacrificar acurácia para obter um modelo mais justo [F: gardner2019slicing]. Essa ausência de tradeoff estrito é um achado metodologicamente relevante: sugere que a prática de "slicing analysis" pode ser incorporada à validação de modelos de aluno (ver `adp.eval.evaluation-protocols`) sem custo automático de desempenho agregado [F: gardner2019slicing].

### De viés desconhecido a viés conhecido

Baker e Hawn propõem uma progressão para o campo: primeiro vem o "viés desconhecido" — situações em que não se sabe se um modelo é enviesado para um grupo, seja porque ninguém investigou (um tipo de "não sabemos o que não sabemos", que os autores classificam como particularmente preocupante), seja porque se sabe que o viés pode existir mas falta o dado necessário para medi-lo (por exemplo, por restrições de privacidade sobre status de deficiência) — depois vem o "viés conhecido" (medido e documentado), e só então é possível avançar de justiça (*fairness*, no sentido estreito de paridade estatística) para equidade (*equity*, que considera o contexto e as necessidades diferenciadas de cada grupo) [F: baker2022bias]. Os autores identificam como o maior "desconhecido desconhecido" (*unknown unknown*) do campo a falta de trabalho empírico sobre como o viés algorítmico afeta grupos de alunos fora dos Estados Unidos, em granularidade mais fina que o nível nacional — um viés centrado nos EUA que atravessa praticamente toda a literatura que revisam [F: baker2022bias].

### Universal Design for Learning como referência de desenho, não de métrica

As diretrizes de Universal Design for Learning (UDL), mantidas pela organização CAST, não são uma métrica de viés algorítmico, mas um framework de desenho instrucional baseado em "percepções científicas sobre como humanos aprendem", organizado em três redes — "múltiplos meios de engajamento", "múltiplos meios de representação" e "múltiplos meios de ação e expressão" —, com nove diretrizes e 36 considerações na versão 3.0 (lançada em 30/07/2024) [F: castudl2024]. A página do framework afirma responder a "chamados para abordar barreiras enraizadas em vieses e sistemas de exclusão" [F: castudl2024]. A relevância de UDL para este documento é indireta: é um framework de desenho de experiência de aprendizagem voltado a antecipar necessidades de uma população heterogênea de alunos (incluindo estudantes com deficiência) desde a concepção, o que é conceitualmente complementar, mas distinto, da auditoria estatística de viés de um modelo já treinado (via slicing analysis ou ABROCA) [I]. Nenhuma das fontes abertas nesta pesquisa articula explicitamente uma integração entre UDL e avaliação quantitativa de viés em modelos de knowledge tracing ou learning analytics — essa conexão permanece uma lacuna de pesquisa, não um fato estabelecido.

## Requisitos e pressupostos

- Medir viés por subgrupo exige que o atributo protegido (gênero, deficiência, status socioeconômico etc.) esteja disponível nos dados — e Baker e Hawn observam que restrições de privacidade sobre justamente os atributos mais sensíveis (como deficiência) podem impedir a própria pesquisa que detectaria o viés, criando uma tensão entre proteção de privacidade e capacidade de auditoria [F: baker2022bias].
- Slicing analysis e ABROCA pressupõem que o atributo de fatiamento (por exemplo, gênero) seja observado de forma binária ou categórica no dataset; o estudo de Gardner et al. é explicitamente limitado a uma análise binária de gênero [F: gardner2019slicing].
- Ausência de diferença detectada em slicing analysis não implica ausência de viés em granularidade mais fina (por exemplo, interseção de duas categorias) ou em populações não representadas na amostra original [I].

## Vantagens e limitações

A abordagem de "teste de não-maleabilidade" de Baker e Hawn tem a vantagem de oferecer um critério prático para decidir quais categorias merecem investigação como viés algorítmico, mas deixa de fora categorias comportamentais que também podem refletir desigualdade estrutural (por exemplo, diferenças de oportunidade de prática em casa) [I]. Slicing analysis com ABROCA tem a vantagem de não exigir um tradeoff assumido entre justiça e desempenho — os próprios autores mostram empiricamente que esse tradeoff não é estrito no seu caso de estudo — mas sua aplicação depende de dados de atributo protegido disponíveis e de volume suficiente por subgrupo para estimativas estáveis [F: gardner2019slicing]. A revisão de Baker e Hawn tem a vantagem de cobrir sistematicamente múltiplas subpopulações pouco estudadas, mas os próprios autores reconhecem que a literatura de base é "muito esparsa" nessas categorias, de modo que a revisão frequentemente reporta um único estudo por categoria — insuficiente para generalização [F: baker2022bias].

## Alternativas e comparações

| Abordagem | O que mede/orienta | Aplicação no ciclo de vida | Limitação principal |
|---|---|---|---|
| Teste de não-maleabilidade (Baker & Hawn) | quais categorias devem ser tratadas como viés algorítmico | enquadramento conceitual, antes da auditoria | não resolve como medir, só o quê medir [F: baker2022bias] |
| Slicing analysis + ABROCA (Gardner et al.) | diferença de acurácia preditiva entre subgrupos | auditoria pós-treino do modelo | exige atributo protegido disponível e amostra suficiente por fatia [F: gardner2019slicing] |
| Universal Design for Learning (CAST) | desenho da experiência instrucional para variabilidade de alunos | desenho, anterior ao treino do modelo | não é uma ferramenta de auditoria estatística; integração com avaliação de viés não documentada nas fontes revisadas [F: castudl2024] |

## Métricas e métodos de avaliação

ABROCA (área absoluta entre curvas ROC de subgrupos) é a métrica proposta por Gardner et al. especificamente para medir diferença de justiça sem depender da escolha de um limiar único [F: gardner2019slicing] — uma extensão, para contexto de subgrupos, da família de métricas baseada em ROC/AUC já discutida em `adp.eval.predictive-metrics`, com a mesma limitação herdada de que AUC considera apenas ordenação relativa, não calibração absoluta, dentro de cada subgrupo [F: pelanek2015metrics]. Baker e Hawn, em sua revisão mais ampla, não endossam uma métrica única de viés, observando que a comunidade de pesquisa em geral carece de "pacotes padronizados e específicos para educação" para calcular métricas de viés e conduzir auditorias — uma das lacunas que sua tabela de recomendações busca endereçar [F: baker2022bias].

## Exemplo técnico independente de domínio

Esboço de uma auditoria de viés por slicing analysis, aplicável a qualquer modelo preditivo de aluno treinado conforme `adp.eval.evaluation-protocols`:

```
entrada: modelo M ja treinado e validado; atributo protegido A (ex.: deficiencia, binario/categorico)
         conjunto de teste com predicoes p_i, observacoes o_i, e valor de A para cada i

para cada valor a de A:
    subconjunto_a = { i : A_i = a }
    construir curva ROC de M restrita a subconjunto_a

para cada par de valores (a, b) de A:
    ABROCA(a, b) = area absoluta entre as curvas ROC de a e de b

reportar:
    - ABROCA para cada par de subgrupos relevante
    - tamanho de cada subgrupo (fatias pequenas tem estimativas instaveis)
    - desempenho agregado (ex.: AUC global) ao lado do ABROCA
         # para verificar se ha ou nao tradeoff entre desempenho agregado e disparidade

se ABROCA for alto entre subgrupos de uma categoria que passa no teste de nao-maleabilidade:
    tratar como viés algorítmico conhecido (nao mais desconhecido)
    documentar e considerar mitigacao antes de uso em decisao de alto risco
```

## Relações com outros conceitos

Este documento estende `adp.eval.predictive-metrics` e `adp.eval.evaluation-protocols` ao perguntar não apenas "o modelo prediz bem, em média?" mas "o modelo prediz igualmente bem para todos os subgrupos relevantes?". Relaciona-se com `adp.eval.educational-effectiveness` porque um efeito médio positivo documentado em um RCT (como o de Cognitive Tutor Algebra I) pode, em princípio, esconder heterogeneidade de efeito entre subpopulações não reportada nesse nível de agregação — conexão que nenhuma das fontes consultadas nesta pesquisa específica confirma empiricamente para esse caso, mas que segue logicamente da lógica de slicing analysis [I]. Relaciona-se também com `adp.lm.learner-model` e `adp.lm.open-learner-model`, cuja estrutura de representação do conhecimento do aluno é o objeto sobre o qual o viés, quando existe, se manifesta.

## Lacunas e questões abertas

- A pesquisa empírica sobre viés algorítmico envolvendo deficiência em sistemas adaptativos de educação é, nas palavras da própria fonte central deste documento, escassa: Baker e Hawn relatam apenas dois estudos (Loukina & Buzick; Riazy et al.) tratando diretamente desse recorte, nenhum deles especificamente sobre knowledge tracing ou sistemas de sequenciamento adaptativo — a lacuna é real e não apenas um artefato de busca incompleta nesta pesquisa [F: baker2022bias].
- Não foi localizada, entre as fontes abertas, nenhuma aplicação de slicing analysis ou ABROCA especificamente a modelos de knowledge tracing (BKT, DKT, PFA); o estudo de Gardner et al. trata de predição de evasão em MOOC, um problema relacionado mas distinto.
- Doroudi & Brunskill (2019), que (segundo resumos de terceiros não verificados nesta sessão) discutem simulações mostrando que BKT pode ser menos equitativo que um modelo logístico alternativo mesmo quando a precisão agregada é semelhante, não pôde ser aberto (página da autora fora do ar; nenhum mirror aberto localizado); não é citado aqui como [F].
- A integração entre Universal Design for Learning e auditoria quantitativa de viés em modelos adaptativos não é documentada por nenhuma fonte aberta nesta pesquisa; trata-se de uma lacuna de pesquisa genuína, não apenas de busca, dado que os dois corpos de literatura (desenho instrucional inclusivo e fairness em machine learning educacional) parecem, pelas fontes revisadas, não se citarem mutuamente.
- A quase totalidade da evidência revisada por Baker e Hawn é centrada nos Estados Unidos; os próprios autores identificam isso como o maior "desconhecido desconhecido" do campo [F: baker2022bias].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| baker2022bias | academico | 2026-10-29 |
| gardner2019slicing | academico | 2026-10-29 |
| castudl2024 | fornecedor | 2026-10-29 |
| pelanek2015metrics | academico | 2026-10-29 |
