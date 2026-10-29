---
id: adp.eval.educational-effectiveness
titulo: Eficácia educacional versus precisão preditiva
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ma2014its, pane2013ctai, ieswwc2026ctai, gervet2020when, pelanek2018details]
relacoes:
  - { tipo: complementa, alvo: adp.eval.predictive-metrics }
  - { tipo: complementa, alvo: adp.eval.evaluation-protocols }
  - { tipo: avaliado-por, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: relacionado-a, alvo: adp.eval.heterogeneous-populations }
  - { tipo: relacionado-a, alvo: adp.id.kli-framework }
termos: [effect size, Hedges g, ensaio clínico randomizado, RCT, meta-análise, mastery learning, intelligent tutoring system]
---

# Eficácia educacional versus precisão preditiva

## Definição e terminologia

Precisão preditiva (medida por AUC, RMSE, log-likelihood — ver `adp.eval.predictive-metrics`) quantifica quão bem um modelo de aluno antecipa o desempenho futuro de um aluno em dados históricos. Eficácia educacional é algo distinto: o quanto o uso de um sistema (que incorpora um modelo de aluno e uma política de adaptação) melhora resultados de aprendizagem reais, tipicamente medidos por testes de proficiência pré e pós-intervenção, em comparação com um grupo de controle [F: pane2013ctai]. As duas coisas não são a mesma pergunta nem necessariamente correlacionadas: Gervet et al. observam que "a eficácia de sistemas tutores inteligentes é determinada principalmente por seu elo mais fraco", e apontam que esse elo mais fraco hoje costuma ser a política instrucional e o modelo de domínio, não a precisão do modelo preditivo [F: gervet2020when]. Eficácia educacional é tipicamente reportada como *effect size* (tamanho de efeito), com Hedges's g sendo a métrica mais comum nas meta-análises consultadas — a diferença de médias padronizada entre grupo que usou o sistema e grupo de controle, com correção para viés de amostra pequena [F: ma2014its].

## Problema que resolve

Um modelo de aluno pode ter excelente AUC ou RMSE e, ainda assim, a política de adaptação construída sobre ele pode não produzir ganho de aprendizagem — ou pior, produzir efeito nulo ou negativo. A métrica preditiva não observa o desfecho educacional; ela observa apenas se o modelo previu corretamente o que o aluno já teria feito. Avaliar eficácia resolve a pergunta que interessa a quem decide adotar um sistema: alunos aprendem mais, ou aprendem o mesmo conteúdo em menos tempo, usando este sistema em vez da alternativa? Essa pergunta exige desenho experimental (idealmente ensaio controlado randomizado) e medidas de resultado externas ao próprio sistema (provas de proficiência, não logs de interação) [F: pane2013ctai].

## Fundamentos e funcionamento

### Meta-análise de sistemas tutores inteligentes: Ma, Adesope, Nesbit & Liu (2014)

Ma et al. conduziram uma meta-análise de 107 effect sizes, envolvendo 14.321 participantes, extraídos de estudos que compararam aprendizagem com sistemas tutores inteligentes (ITS) contra ambientes não-ITS [F: ma2014its]. Os resultados centrais, sob modelo de efeitos aleatórios: o uso de ITS esteve associado a maior desempenho em comparação com instrução em grande grupo liderada por professor (g = 0,42), com instrução baseada em computador não-ITS (g = 0,57), e com livros-texto ou cadernos de exercício (g = 0,35) [F: ma2014its]. Não houve diferença significativa entre aprender com ITS e aprender com tutoria humana individualizada (g = −0,11) nem com instrução em pequeno grupo (g = 0,05) [F: ma2014its]. Sob modelo de efeito fixo, o efeito global combinado (todas as 107 comparações, k=106 graus de liberdade) foi g = 0,36 (p < 0,001), com heterogeneidade estatisticamente significativa (Q(106) = 390,52, p < 0,001, I² = 0,73); sob modelo de efeitos aleatórios o efeito global foi g = 0,41 (p < 0,001) [F: ma2014its]. A alta heterogeneidade (I² = 0,73) indica que o efeito varia substancialmente entre estudos, o que motivou os autores a investigar moderadores — tipo de ITS, tipo de tratamento de comparação, tipo de desfecho medido, e se o conhecimento-alvo era procedural ou declarativo [F: ma2014its]. Os autores também separaram 9 effect sizes (785 participantes) de estudos em que o grupo controle não recebeu nenhum tratamento instrucional; nesse subconjunto, o efeito médio sob modelo de efeitos aleatórios foi g = 1,23, substancialmente maior que o efeito contra alternativas instrucionais ativas [F: ma2014its]. Os autores reportam que sua análise de viés de publicação é consistente com a afirmação de que ITS são ferramentas de aprendizagem relativamente eficazes [F: ma2014its].

### RCT de larga escala: Cognitive Tutor Algebra I (Pane et al., RAND)

Pane, Griffin, McCaffrey e Karam conduziram um ensaio controlado randomizado em escala, com escolas de ensino médio e fundamental de sete estados dos EUA pareadas e randomizadas entre continuar com o currículo de álgebra vigente ou adotar o Cognitive Tutor Algebra I (CTAI), um currículo que combina material tradicional com software de tutoria adaptativa baseado em mastery learning [F: pane2013ctai]. O desenho avaliou dois anos consecutivos de implementação, com coortes separadas de ensino médio e fundamental [F: pane2013ctai]. Os resultados **não são uniformemente positivos**: no primeiro ano de implementação, os efeitos estimados não foram estatisticamente significativos em nenhum dos dois níveis escolares — negativos (não significativos) no ensino médio e próximos de zero no ensino fundamental [F: pane2013ctai]. No segundo ano, porém, os modelos ajustados por covariáveis estimaram efeitos positivos e significativos para a coorte 2 do ensino médio, na faixa de 0,14 a 0,21 desvio-padrão (significativos ao nível de 0,05 nos modelos 2 a 4) [F: pane2013ctai]; a coorte 2 do ensino fundamental teve estimativas de magnitude semelhante (0,20 a 0,23 nos quintis mais baixos de desempenho prognóstico), mas não estatisticamente significativas, atribuído pelos autores ao tamanho amostral menor (a coorte de ensino fundamental tinha cerca de um terço do tamanho da coorte de ensino médio) [F: pane2013ctai]. Os autores traduzem o efeito de 0,20 desvio-padrão do segundo ano como equivalente a mover um aluno do percentil 50 para o percentil 58 na distribuição do pós-teste, ou aproximadamente oito pontos percentuais [F: pane2013ctai]. Os autores também relatam um achado metodologicamente relevante: as escolas do grupo de tratamento apresentavam, antes da intervenção, escore médio de pré-teste 0,328 desvio-padrão mais baixo que o grupo controle (p < 0,01) — uma diferença de seleção que, segundo os autores, justifica o ajuste por covariáveis e explica por que as estimativas não ajustadas (Modelo 1) são sistematicamente mais baixas que as ajustadas [F: pane2013ctai].

O relatório do What Works Clearinghouse (WWC) sobre o mesmo estudo, consultado separadamente, classifica a evidência como "atende aos padrões do WWC sem ressalvas" (desenho experimental), mas sua tabela de achados para o ensino médio marca ambos os desfechos reportados (exame de proficiência em álgebra, um e dois anos) como **não significativos**, em aparente contradição com a frase de resumo da mesma página, que afirma "efeito positivo estatisticamente significativo encontrado para o domínio" [F: ieswwc2026ctai]. Essa discrepância entre o texto-resumo e a tabela de achados do WWC não foi resolvida nesta pesquisa e é registrada como observação, não como fato assentado [I]. Para o ensino fundamental, o próprio WWC classifica o efeito de domínio como "indeterminado" [F: ieswwc2026ctai].

### Controvérsias metodológicas

Duas tensões metodológicas aparecem de forma recorrente nas fontes consultadas:

1. **Comparação com tutoria humana.** Ma et al. relatam ausência de diferença significativa entre ITS e tutoria humana individualizada (g = −0,11) [F: ma2014its] — um achado citado, em outras fontes buscadas nesta pesquisa mas não abertas de forma verificável (VanLehn 2011), como responsável por revisar para baixo a crença histórica de que tutoria humana teria efeito muito maior que tutoria por computador. Como essa fonte específica não foi aberta nesta sessão, a comparação exata entre os dois corpos de evidência (Ma et al. 2014 versus a revisão de VanLehn) não pôde ser verificada diretamente e não é afirmada aqui como fato — ver Lacunas.
2. **Medida de desfecho.** Nas meta-análises de ITS, a heterogeneidade estatística é alta (I² = 0,73 em Ma et al.) e parcialmente explicada por diferenças no tipo de teste usado como desfecho — testes "locais" (desenvolvidos pelo próprio estudo ou grupo de pesquisa) tendem a mostrar efeitos maiores que testes padronizados externos, uma distinção que a literatura de meta-análise de tutoria por computador identifica como fonte importante de variação entre estudos [I, inferido da discussão de heterogeneidade em ma2014its]. No RCT de Pane et al., o desfecho foi um exame de proficiência padronizado (CTB/McGraw-Hill), e mesmo assim o resultado variou drasticamente entre o primeiro e o segundo ano de implementação dentro do mesmo desenho experimental — o que os autores atribuem tentativamente à curva de aprendizagem dos professores no uso do currículo, embora reconheçam que uma análise exploratória dessa hipótese não produziu resultados estatisticamente conclusivos [F: pane2013ctai].

## Requisitos e pressupostos

- Avaliação de eficácia exige desfecho medido fora do próprio sistema (prova externa de proficiência), não apenas métricas internas de interação ou predição [F: pane2013ctai].
- Desenho experimental com grupo de controle e, preferencialmente, randomização (ao nível de escola, turma ou aluno) é necessário para isolar o efeito do sistema de fatores de seleção — o próprio RCT de Pane et al. encontrou diferença de pré-teste entre grupos apesar da randomização por pareamento, exigindo ajuste estatístico [F: pane2013ctai].
- Efeitos observados em um ano de implementação podem não se repetir no ano seguinte dentro do mesmo desenho, o que sugere que a maturidade de implementação (familiaridade de professores e alunos com o sistema) é uma variável relevante e raramente controlada explicitamente [F: pane2013ctai].

## Vantagens e limitações

Meta-análises como a de Ma et al. agregam muitos estudos pequenos e conseguem detectar um efeito médio positivo e robusto a análise de viés de publicação, mas sua alta heterogeneidade (I² = 0,73) significa que o número único "g = 0,41" esconde variação substancial — nem todo ITS, em todo contexto, produz esse efeito [F: ma2014its]. RCTs de larga escala como o de Pane et al. têm validade interna mais forte (randomização, ajuste por covariáveis), mas um único estudo, mesmo grande, pode produzir resultados que não se replicam de um ano para o outro dentro do próprio desenho — como de fato ocorreu [F: pane2013ctai]. Relatórios de clearinghouse como o WWC agregam critérios de qualidade metodológica padronizados entre estudos, mas, como mostrado acima, podem conter inconsistências internas entre resumo textual e tabela de achados que exigem checagem cuidadosa antes de citação [F: ieswwc2026ctai].

## Alternativas e comparações

| Fonte de evidência | Tipo de desenho | Achado central | Força da evidência |
|---|---|---|---|
| Ma et al. 2014 | meta-análise (107 effect sizes, 14.321 participantes) | g = 0,41 (ITS vs. não-ITS, efeitos aleatórios); g = −0,11 vs. tutoria humana [F: ma2014its] | agrega muitos estudos, mas heterogeneidade alta (I²=0,73) |
| Pane et al. (RAND WR-984) 2013 | RCT, 2 anos, 7 estados dos EUA | efeito nulo ano 1; +0,14 a 0,21 DP ano 2 (ensino médio, significativo) [F: pane2013ctai] | validade interna forte, mas resultado instável entre anos |
| WWC (ies.ed.gov) 2026 | revisão de evidência (meta-avaliação de um único RCT) | classifica desenho como rigoroso, mas marca desfechos reportados como não significativos [F: ieswwc2026ctai] | revisão de terceiros; inconsistência interna não resolvida |

## Métricas e métodos de avaliação

Hedges's g (effect size padronizado, com correção para amostra pequena) é a métrica de referência nas meta-análises revisadas, reportado com erro padrão e intervalo de confiança de 95% [F: ma2014its]. Modelos de efeito fixo (assumem um único efeito verdadeiro compartilhado por todos os estudos) e de efeitos aleatórios (assumem que o efeito verdadeiro varia entre estudos) são reportados lado a lado; Ma et al. seguem a recomendação da literatura de meta-análise de tratar o modelo de efeitos aleatórios como mais realista dado a diversidade de implementações de ITS, mas reportam ambos para permitir comparação com meta-análises anteriores que usaram efeito fixo [F: ma2014its]. O teste de heterogeneidade Q e a estatística I² quantificam o quanto a variação entre effect sizes individuais excede o que se esperaria por acaso amostral [F: ma2014its]. No RCT de Pane et al., a unidade de inferência estatística é o desvio-padrão do pós-teste, com significância avaliada por testes de Wald conjuntos para verificar se o efeito varia por quintil de desempenho prognóstico [F: pane2013ctai].

## Exemplo técnico independente de domínio

Esboço do desenho que separa, de forma explícita, avaliação de modelo preditivo e avaliação de eficácia educacional:

```
ETAPA 1 - avaliacao do modelo preditivo (ver adp.eval.predictive-metrics):
    treinar modelo M com dados historicos
    validar com protocolo explicito (ver adp.eval.evaluation-protocols)
    reportar AUC, RMSE, calibracao          # isto NAO mede aprendizagem

ETAPA 2 - avaliacao de eficacia (este documento):
    definir desfecho externo: prova de proficiencia pre/pos, independente do sistema
    desenhar grupo de controle (ideal: randomizacao por escola/turma/aluno)
    implantar o sistema (modelo M + politica de adaptacao) no grupo de tratamento
    medir desfecho em ambos os grupos apos periodo de uso
    calcular effect size (ex.: Hedges g) com intervalo de confianca
    reportar separadamente por subgrupo relevante e por ano/coorte de implementacao
         # um efeito nulo no ano 1 nao implica efeito nulo no ano 2 (ver pane2013ctai)

CONCLUSAO: um M com otima ETAPA 1 nao garante bom resultado na ETAPA 2;
as duas etapas respondem perguntas diferentes e exigem desenhos diferentes.
```

## Relações com outros conceitos

Este documento depende dos conceitos de `adp.eval.predictive-metrics` e `adp.eval.evaluation-protocols` como pré-requisito para entender por que precisão preditiva não é suficiente. Ele se relaciona com `adp.adapt.adaptive-learning-systems`, cuja eficácia agregada (modelo + política) é o que de fato está sob teste nos RCTs aqui descritos, e com `adp.eval.heterogeneous-populations`, que trata de uma limitação adicional: mesmo um efeito médio positivo pode esconder desempenho desigual entre subgrupos de alunos.

## Lacunas e questões abertas

- VanLehn (2011), "The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems" (Educational Psychologist, DOI 10.1080/00461520.2011.611369), é citado por múltiplas fontes secundárias como a referência central que revisou para baixo os effect sizes históricos de tutoria humana e de ITS (reportando d ≈ 0,79 para tutoria humana e d ≈ 0,76 para ITS, segundo resumos de terceiros). Não foi possível abrir uma cópia de texto completo nesta sessão (fechado no editor e sem repositório aberto localizado via OpenAlex); portanto, esses números não são citados aqui como [F] e a comparação entre essa revisão e Ma et al. (2014) permanece não verificada.
- Kulik & Fletcher (2016), "Effectiveness of Intelligent Tutoring Systems: A Meta-Analytic Review" (Review of Educational Research), reportaria — segundo resumos de terceiros não verificados diretamente — um efeito mediano de aproximadamente 0,66 desvio-padrão sobre 50 avaliações controladas. Uma cópia hospedada pelo Institute for Defense Analyses (apps.dtic.mil) foi tentada, mas o download retornou uma página HTML em vez do PDF nesta sessão; não é citada aqui como [F].
- A inconsistência interna na página do WWC entre o resumo textual ("efeito positivo estatisticamente significativo") e a tabela de achados (ambos os desfechos marcados como não significativos) não foi resolvida; pode refletir diferença entre a avaliação de "domínio" (que combina múltiplos desfechos ou estudos) e o desfecho individual reportado, mas essa hipótese não foi confirmada na própria página.
- Não foram localizadas, nesta pesquisa, meta-análises ou RCTs de grande escala específicos sobre plataformas de aprendizagem adaptativa fora do domínio de matemática/álgebra; a generalização dos achados acima para outras áreas de conteúdo não está estabelecida pelas fontes aqui reunidas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ma2014its | academico | 2026-10-29 |
| pane2013ctai | academico | 2026-10-29 |
| ieswwc2026ctai | secundario | 2026-10-29 |
| gervet2020when | academico | 2026-10-29 |
| pelanek2018details | academico | 2026-10-29 |
