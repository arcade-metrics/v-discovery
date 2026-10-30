---
id: gam.instr.telemetry-as-evidence
titulo: Telemetria de jogo como evidência de construto
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [mislevy2015psychometrics, mislevy2012design, kerr2012identifying, saopedro2013leveraging, gobert2013logfiles, owen2020learning, shute2013stealth, ventura2013validity, ventura2013investigation, shute2016measuring, kim2016applying, lumsden2016gamification, kane2013validating]
relacoes:
  - { tipo: depende-de, alvo: gam.instr.evidence-centered-design }
  - { tipo: depende-de, alvo: dat.ev.game-telemetry }
  - { tipo: depende-de, alvo: dat.qual.granularity-and-constructs }
  - { tipo: complementa, alvo: gam.instr.stealth-assessment }
  - { tipo: avaliado-por, alvo: lae.psy.reliability-and-validity }
  - { tipo: relacionado-a, alvo: lae.psy.fairness-in-measurement }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: acs.adapt.accommodation-vs-modification }
  - { tipo: relacionado-a, alvo: lae.ind.engagement-indicators }
  - { tipo: relacionado-a, alvo: gam.evid.special-education-and-neurodivergence }
termos: [evidence identification, evidence accumulation, work product, variável observável, indicador, detector, text replay tagging, feature engineering, cluster analysis fuzzy, coeficiente de Dunn, heartbeat de estado, variância irrelevante ao construto, sub-representação do construto, medida de domínio misto, validade convergente, validade de critério, argumento de validade, generalizabilidade]
---

# Telemetria de jogo como evidência de construto

## Definição e terminologia

Um evento de jogo é **evidência** de um construto quando existe um argumento explícito, com garantia e respaldo, que liga o evento, no seu contexto, a uma variável do modelo de aluno; sem esse argumento ele é só telemetria [I, a partir de `gam.instr.evidence-centered-design`]. A passagem tem duas etapas com nome próprio: *evidence identification*, que calcula variáveis observáveis a partir do *work product*, e *evidence accumulation*, que atualiza as variáveis de competência com base nas observáveis [F: kim2016applying, Step 7]. "Indicador" é usado pela literatura de stealth assessment para a observável derivada do log [F: shute2013stealth, Fig. 5]. A captura em si (eventos, envelope, relógios) está em `dat.ev.game-telemetry` e `dat.qual.granularity-and-constructs` e não é repetida aqui.

## Problema que resolve

Mislevy et al. resumem: o entusiasmo com jogos vem de captar dados finos, e "a primary challenge in fulfilling the potential of log files [...] lies in evidence identification. What are the important features of the work product, and how do we apply scoring rules?" [F: mislevy2015psychometrics, §3.2.2]. Kerr e Chung chamam essa etapa de "one of the most serious bottlenecks" para quem aplica ECD a jogos, porque a interpretação de uma ação depende do que mais o aluno faz [F: kerr2012identifying, resumo, §1.2]. Este documento responde à pergunta do brief: que eventos são evidência válida, e como validar o vínculo do log ao indicador.

## Fundamentos e funcionamento

### Cadeia do log ao indicador

```
evento + estado do jogo -> work product (tentativa, fase, sessão)
  -> evidence identification: regra ou detector -> variável observável
  -> evidence accumulation: modelo de medida -> variável de competência
  -> indicador reportado (com incerteza) -> uso (feedback, adaptação, relatório)
```

Três decisões determinam se a cadeia se sustenta [I]:

1. **Contexto junto do evento.** Logs costumam ter carimbo de tempo, identificador, local, ação e detalhe, mas precisam ser complementados com variáveis de estado; num jogo de simulação urbana, um "heartbeat" a cada 30 segundos de jogo registrava os níveis das medidas principais, o que permitiu distinguir "bulldoze in low-pollution scenario" de "bulldoze in high-pollution scenario" [F: mislevy2015psychometrics, §3.2.2 Log Files].
2. **Unidade do work product.** Kerr e Chung analisaram tentativas, definidas do carregamento ou reinício da fase até o reinício ou a conclusão, e cada fase separadamente, "because the same action might have different meanings in different levels" [F: kerr2012identifying, Method].
3. **Regra de ausência.** Na rede de um jogo de física, se o jogador resolveu a fase com um agente, só aquele agente foi tratado como observado; se não resolveu, só os agentes que o designer julgava aplicáveis [F: kim2016applying, Step 7]. Tratar não uso como erro inventaria evidência negativa [I].

### Duas rotas para definir observáveis

A identificação de evidência em logs é "frequently tackled by combining a priori hypotheses about the relationships between observables and constructs with exploratory data analysis and data mining" [F: mislevy2015psychometrics, §3.2.2]. Owen e Baker organizam os métodos de mineração em cinco categorias (predição, descoberta de estrutura, mineração de relações, descoberta com modelos e visualização) e os associam a estágios de desenvolvimento do jogo: visualização no início, descoberta de estrutura e relações no meio, predição perto do lançamento [F: owen2020learning, Overview]. O alerta de Mislevy, Behrens, DiCerbo e Levy é que padrões minerados não são psicometria enquanto não se modela "the dependence of these variables on the latent variables" [F: mislevy2012design, p. 32].

**Rota exploratória (exemplo).** Kerr e Chung aplicaram análise de clusters fuzzy às ações de 155 alunos de 6º a 8º ano num jogo de adição de frações, com cerca de 40 minutos de jogo [F: kerr2012identifying, §2]. O log registrou só cliques deliberados, para eliminar ruído que "only contributes construct-irrelevant variance" [F: kerr2012identifying, Method]. Os coeficientes de Dunn normalizados variaram de 0,13 a 0,66 nas 18 fases (média 0,35), indicando dados difusos [F: kerr2012identifying, §4.1.2]. Os clusters revelaram erros de unidade e de partição que os autores não haviam previsto, e uma estratégia de jogo sem matemática, colocar as peças na ordem em que aparecem, que respondeu por 19% dos erros e por 32% das tentativas numa fase [F: kerr2012identifying, §4.1]. Ou seja, parte do comportamento observado era evidência sobre o jogo, não sobre frações [I].

**Rota supervisionada (exemplo).** Sao Pedro, Baker, Gobert e colegas treinaram detectores de comportamento de investigação científica em 148 alunos de 8º ano: trechos de log foram rotulados por humanos com *text replay tagging* (kappa médio de 0,86 entre codificadores nas dez etiquetas, 0,69 para planejar experimentos controlados), e árvores de decisão foram validadas por validação cruzada no nível do aluno [F: saopedro2013leveraging, §4]. O detector de experimentos controlados teve A' = 0,85 e kappa = 0,47 [F: saopedro2013leveraging, §4]. Agregadas por aluno, as estimativas correlacionaram com um teste de múltipla escolha (r = 0,26) e com uma tarefa prática em outro domínio (r = 0,37 a 0,38), n = 134 [F: saopedro2013leveraging, §5]. A versão em periódico de aprendizagem do mesmo grupo não foi lida [F: gobert2013logfiles, metadados].

## Requisitos e pressupostos

- Construto definido antes da instrumentação; o evento é escolhido porque a teoria do construto prevê variação nele [F: mislevy2015psychometrics, §3.2].
- Codificação humana ou critério externo disponível para validar regras: Shute e Ventura só implantariam indicadores com pelo menos 80% de acurácia frente à análise humana de replays [F: shute2013stealth, p. 60].
- Covariáveis de dispositivo e condição, quando o indicador usa tempo ou movimento (ver `dat.qual.granularity-and-constructs`).
- Registro da condição de acomodação, para não misturar evidência obtida sob exigências diferentes (ver `acs.adapt.accommodation-vs-modification`).

## Vantagens e limitações

Mislevy et al. listam as ameaças: **sub-representação do construto**, quando o jogo não evoca parte da capacidade, e **variância irrelevante ao construto**, quando o desempenho exige outra coisa; falta de conhecimento prévio, não saber usar a interface e não saber o que se espera, e "the very factors that can make games engaging--narrative lines, competition, time pressure--can also work against some students" [F: mislevy2015psychometrics, §5.4]. Estudos de generalizabilidade em avaliação de desempenho são "sobering": formato, contexto, conteúdo e ocasião pesam muito [F: mislevy2015psychometrics, §5.2]. Para comparar indivíduos, caminhos diferentes no mesmo jogo, familiaridade com a interface e engajamento variável dificultam a comparabilidade [F: mislevy2015psychometrics, §5.3].

### O caso cognitivo-motor

Indicadores baseados em tempo e movimento são os mais baratos de extrair e os mais expostos a variância irrelevante [I]. Três resultados publicados delimitam o problema:

- **Persistência medida por tempo.** O tempo em fases não resolvidas correlacionou r = 0,51 com uma medida externa de persistência em jogadores de baixo desempenho (n = 70), mas só r = 0,22 nos de alto desempenho (n = 84); o mesmo tempo indica coisas diferentes conforme o jogador seja desafiado ou não [F: ventura2013validity, Tab. 2, Tab. 3].
- **Navegação espacial em 3D.** Numa tarefa de coletar gemas com teclado e mouse, aplicada sem supervisão a 323 universitários, o tempo predisse a escolha de curso de exatas após controlar gênero, matemática do SAT e autorrelato (beta padronizado 0,24) [F: ventura2013investigation, Results]. Os autores afirmam que a tarefa exige pouco controle motor, mas o uso de videogames continuou associado ao escore após controles (r parcial 0,15), e eles não conseguiram excluir a hipótese de seleção [F: ventura2013investigation, Results, Discussion].
- **Tarefas cognitivas gamificadas.** Uma revisão sistemática de 33 estudos (31 tarefas) achou correlações de 0,45 a 0,60 entre versões gamificadas e convencionais nos estudos de validação mais simples, mas também medidas de domínio misto: um jogo de acertar alvos correlacionou com inibição (r = 0,60) e com atualização de memória (r = 0,35); outro, válido para velocidade de processamento num estudo (r = 0,55), teve correlações instáveis na replicação; e um terceiro não detectou os erros de comissão de adultos com TDAH que a tarefa convencional detectou [F: lumsden2016gamification, Results]. A revisão não encontrou evidência de que gamificar melhore a qualidade do dado e viu indícios de que pode piorá-la [F: lumsden2016gamification, Conclusions].

## Métricas e métodos de avaliação

Mislevy et al. propõem tratar confiabilidade, generalizabilidade, comparabilidade e validade como qualidades do argumento [F: mislevy2015psychometrics, §5]. Para confiabilidade: KR-20 ou alfa quando todos fazem o mesmo; variância posterior ou entropia quando a quantidade de evidência difere entre jogadores; e reamostragem, que funciona até sem modelo [F: mislevy2015psychometrics, §5.1]. A validade depende do uso: para adaptação interna, experimentos A/B com regras diferentes; para feedback ao aluno, desempenho e uso de conceitos fora do jogo; para avaliação de fim de curso, evidência convergente de meios alternativos [F: mislevy2015psychometrics, §5.4]. O enquadramento de validação de interpretações e usos de Kane está em `lae.psy.reliability-and-validity` [F: kane2013validating, metadados].

| Etapa da cadeia | Pergunta de validação | Método publicado |
|---|---|---|
| Evento a observável | A regra reconhece o que um humano reconheceria? | concordância com replay, limiar de 80% [F: shute2013stealth, p. 60]; kappa entre codificadores e A' em validação cruzada por aluno [F: saopedro2013leveraging, §4] |
| Observável a competência | Quanta evidência há? | alfa, variância posterior, reamostragem [F: mislevy2015psychometrics, §5.1]; calibração e depuração da rede, que achou uma observável com codificação invertida [F: kim2016applying, Step 9 e 10] |
| Competência a critério | Converge com medidas externas do construto? | r = 0,40 a 0,41 com Raven e MicroDYN, n = 47 [F: shute2016measuring, Results] |
| Indicador a uso | Prediz o que o uso exige? | correlação parcial com pós-teste [F: ventura2013validity, Results]; transferência para outra tarefa [F: saopedro2013leveraging, §5] |

## Exemplo técnico independente de domínio

```
regra_de_evidencia "experimento_controlado":
  work_product = tentativas da fase (início/reinício -> reinício/conclusão)
  contexto     = estado das variáveis do simulador a cada execução
  observavel   = 1 se duas execuções diferem em exatamente uma variável manipulável
  ausente      se a fase não oferece mais de uma variável manipulável
  covariaveis  = tipo de ponteiro, condição de acomodação, versão do conteúdo
validacao:
  amostra de clips -> 2 codificadores -> kappa por etiqueta
  detector         -> validação cruzada por aluno -> A', kappa
  estimativa       -> corr(medida externa) e corr_parcial(pos_teste | pre_teste)
  subgrupos        -> repetir por dispositivo e por perfil de acessibilidade
```

## Relações com outros conceitos

Depende de `gam.instr.evidence-centered-design` para a estrutura e de `dat.ev.game-telemetry` e `dat.qual.granularity-and-constructs` para a captura. Complementa `gam.instr.stealth-assessment`. É avaliado pelos critérios de `lae.psy.reliability-and-validity`; diferenças por subgrupo são tema de `lae.psy.fairness-in-measurement`. Estimativas por habilidade com aprendizagem entre tentativas usam `adp.kt.bayesian-knowledge-tracing`, que no estudo de detectores não superou uma média simples [F: saopedro2013leveraging, §5]. Indicadores de engajamento extraídos do mesmo log estão em `lae.ind.engagement-indicators`.

## Lacunas e questões abertas

- Não se localizou estudo publicado que valide indicadores cognitivo-motores de jogo com crianças com deficiência motora, TEA ou TDAH; a única evidência com TDAH lida é negativa.
- O artigo de 2013 sobre métricas de investigação (periódico de ciências da aprendizagem) e o artigo de Kane (2013) só tiveram metadados verificados; o relatório "digital ocean" de DiCerbo e Behrens não foi localizado em versão aberta.
- Nenhuma fonte lida estima quantos eventos por construto bastam para uma confiabilidade-alvo em jogo.
- A invariância dos indicadores entre dispositivos (toque e mouse) não foi testada nos estudos de validação de jogos lidos.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| mislevy2015psychometrics | academico | 2026-10-30 |
| mislevy2012design | academico | 2026-10-30 |
| kerr2012identifying | academico | 2026-10-30 |
| saopedro2013leveraging | academico (versão aberta ERIC) | 2026-10-30 |
| gobert2013logfiles | academico [metadados] | 2026-10-30 |
| owen2020learning | academico (versão do autor) | 2026-10-30 |
| shute2013stealth | academico (livro aberto) | 2026-10-30 |
| ventura2013validity | academico (cópia dos autores) | 2026-10-30 |
| ventura2013investigation | academico | 2026-10-30 |
| shute2016measuring | academico (cópia da autora) | 2026-10-30 |
| kim2016applying | academico (cópia da autora) | 2026-10-30 |
| lumsden2016gamification | academico | 2026-10-30 |
| kane2013validating | academico [metadados] | 2026-10-30 |
