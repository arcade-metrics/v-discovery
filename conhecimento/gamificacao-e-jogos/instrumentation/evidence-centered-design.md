---
id: gam.instr.evidence-centered-design
titulo: Evidence-centered design (ECD)
tipo: framework
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [mislevy2003structure, mislevy2004brief, mislevy2015psychometrics, mislevy2012design, kim2016applying, shute2011stealth]
relacoes:
  - { tipo: depende-de, alvo: lae.psy.reliability-and-validity }
  - { tipo: complementa, alvo: gam.instr.stealth-assessment }
  - { tipo: complementa, alvo: gam.instr.telemetry-as-evidence }
  - { tipo: complementa, alvo: dat.ev.game-telemetry }
  - { tipo: complementa, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: lae.psy.fairness-in-measurement }
termos: [evidence-centered design, argumento de avaliação, análise de domínio, modelagem de domínio, paradigma, conceptual assessment framework, student model, competency model, evidence model, regra de evidência, modelo de medida, variável observável, task model, variável de modelo de tarefa, assembly model, presentation model, delivery system model, arquitetura de quatro processos, evidence identification, evidence accumulation, work product, calibração, Q-matrix aumentada]
---

# Evidence-centered design (ECD)

## Definição e terminologia

Evidence-centered design (ECD, "projeto centrado em evidência") é um framework para projetar avaliações como argumentos de evidência. O artigo de referência parte de uma frase que resume o problema: "we observe what students say, do, or make in a few particular circumstances, and attempt to infer what they know, can do, or have accomplished more generally" [F: mislevy2003structure, resumo]. Os autores definem a avaliação como "a machine for reasoning about what students know, can do, or have accomplished, based on a handful of things they say, do, or make in particular settings" [F: mislevy2003structure, Introduction]. ECD foi desenvolvido no Educational Testing Service (ETS) como linguagem comum para estatísticos, autores de tarefas, desenvolvedores de entrega e designers de interface [F: mislevy2004brief, p. 2].

Nomes alternativos: "evidence-centered assessment design". Em jogos, Shute rebatiza o student model de *competency model* (o modelo instanciado para um aluno continua sendo o student model) e o task model de *action model*, porque o que se modela são sequências de ações [F: shute2011stealth, p. 510-511]. O que ECD não é: não é um modelo psicométrico (acomoda CTT, IRT, classes latentes e redes bayesianas) e não é um método de mineração de dados; é a estrutura que diz o que cada modelo precisa justificar [F: mislevy2004brief, p. 10; mislevy2012design, resumo].

## Problema que resolve

Dados ricos não se interpretam sozinhos. Os autores advertem que não se pode "construct 'good tasks' in isolation, however, and hope that someone down the line will figure out 'how to score it'"; a avaliação complexa precisa ser projetada desde o início em torno das inferências pretendidas, das observações que as sustentam, das situações que evocam essas observações e da cadeia de raciocínio que as liga [F: mislevy2004brief, p. 2]. Em jogos, onde o dado é um rastro de ações e não uma resposta a item, esse é o gargalo: Shute pergunta "What is wheat and what is chaff?" e responde com ECD [F: shute2011stealth, p. 504]. Relatórios da base (aprendizagem adaptativa, learning analytics) registravam a ausência deste framework; este documento cobre a estrutura, e `gam.instr.telemetry-as-evidence` cobre a passagem do log ao indicador.

## Fundamentos e funcionamento

### A avaliação como argumento

O argumento segue o esquema de Toulmin: a inferência vai do dado (D) à afirmação (C) por meio de uma garantia (*warrant*, W), uma generalização que precisa de respaldo (*backing*, B) em teoria, pesquisa ou experiência; explicações alternativas (A) e dados de refutação (R) qualificam a inferência [F: mislevy2003structure, p. 12-13]. Familiaridade, motivação, oportunidade de aprender e condições de aplicação podem "erode the value of students' performances as evidence" [F: mislevy2003structure, p. 12]. Há dois tipos de dado: o que o aluno faz e as características da situação em que o faz; as garantias dizem respeito à relação entre ambos [F: mislevy2003structure, p. 13]. Em jogo, isso significa que o evento sem o estado do jogo não é evidência [I].

### Camadas de projeto

O framework organiza o projeto em camadas: **análise de domínio** (reunir conhecimento sobre o domínio, ainda não organizado em termos de avaliação); **modelagem de domínio**, em *paradigmas* de proficiência (afirmações possíveis), de evidência (o que o aluno diria ou faria) e de tarefa (situações que permitem obter a evidência); **conceptual assessment framework** (CAF), o projeto técnico; e o **sistema de entrega de quatro processos** [F: mislevy2003structure, Fig. 1, p. 5-6]. O processo não é linear: iterações sobem e descem as camadas conforme testes de campo modificam o argumento [F: mislevy2003structure, nota 2].

### Os modelos do CAF

| Modelo | Pergunta | Conteúdo |
|---|---|---|
| Student model | O que medimos? | Variáveis latentes de conhecimento e habilidade, com distribuição de probabilidade que expressa a crença atual [F: mislevy2004brief, p. 7-9] |
| Evidence model | Como medimos? | Regras de evidência (do *work product* a variáveis observáveis) e modelo de medida (das observáveis às variáveis do student model) [F: mislevy2004brief, p. 9-10] |
| Task model | Onde medimos? | Família de tarefas possíveis, com variáveis de modelo de tarefa que controlam o valor de evidência [F: mislevy2004brief, p. 11-12] |
| Assembly model | Quanto medimos? | Metas de precisão por variável e restrições de equilíbrio de conteúdo [F: mislevy2004brief, p. 12-13] |
| Presentation model | Como aparece? | Como as tarefas são apresentadas e capturadas em cada meio [F: mislevy2004brief, p. 13] |
| Delivery system model | Como tudo funciona junto? | Integração dos modelos e aspectos transversais: plataforma, segurança, tempo [F: mislevy2004brief, p. 14] |

Um task model "does not represent a single task, but rather a family of potential tasks waiting to be written", e as tarefas da família não são clones: servem para "understanding and controlling evidential variation" [F: mislevy2004brief, p. 12]. A separação permite reusar tarefas com evidence models diferentes: um uso diagnóstico pede student model mais fino que um uso de seleção [F: mislevy2004brief, p. 14].

### Arquitetura de quatro processos

Todo sistema de avaliação contém, em alguma forma, quatro processos [F: mislevy2004brief, p. 14-16]: **seleção de atividade** (escolhe a próxima tarefa e quando parar); **apresentação** (mostra a tarefa e captura o *work product*; o exemplo citado inclui "a simulator which can capture an activity trace"); **processamento de resposta**, também chamado *evidence identification* (extrai as observáveis); e **pontuação sumária**, ou *evidence accumulation* (atualiza o student model). Uma biblioteca de tarefas e evidências fornece a cada processo os dados de que precisa [F: mislevy2004brief, p. 16; mislevy2003structure, Fig. 1]. Parâmetros das regras e do modelo de medida vêm de dados de pré-teste, por **calibração** [F: mislevy2004brief, p. 17].

### ECD em jogos

Mislevy et al. aplicam as camadas a jogos: o *work product* passa a incluir rastros de estado e ação ("log files, click streams, slime trails, and transaction lists"); a regra de evidência pode usar metadados e paradados (o contexto e as consequências das ações anteriores); e a granularidade das variáveis do student model depende do uso, mais fina para os ciclos curtos que guiam o jogo e mais grossa para relatórios [F: mislevy2015psychometrics, §2, §3.3]. A *evidence identification* é "the center of the bridge from performances to inferences" [F: mislevy2015psychometrics, §3.2].

## Algoritmos e modelos relevantes

O modelo de medida pode ser CTT, IRT, modelos de classes latentes, diagnóstico cognitivo ou redes bayesianas; no exemplo de referência, um teste adaptativo usa IRT e um protótipo de simulação usa redes bayesianas [F: mislevy2004brief, p. 10, 16]. Mislevy et al. observam que CTT funciona quando as observações são tentativas independentes e semelhantes, sem aprendizagem entre elas, e falha quando a evidência tem dependências, mistura habilidades ou quando a proficiência muda durante a observação [F: mislevy2015psychometrics, §3.3.1]. Para estimação por item e por habilidade, ver `adp.irt.item-response-theory` e `adp.kt.bayesian-knowledge-tracing`.

## Requisitos e pressupostos

- Afirmações sobre o aluno explícitas antes de projetar tarefas e eventos [F: mislevy2004brief, p. 2].
- Registro das características da situação junto com a ação [F: mislevy2003structure, p. 13].
- Dados de campo para calibrar regras e parâmetros [F: mislevy2004brief, p. 17].
- Equipe multidisciplinar trabalhando sobre os mesmos objetos de projeto [F: mislevy2004brief, p. 2].

## Vantagens e limitações

Vantagens: torna explícito o argumento e cada elo dele, o que permite auditar e reusar partes [F: mislevy2003structure, resumo]; acomoda qualquer modelo psicométrico [F: mislevy2004brief, p. 10]. Limitações: o projeto completo é caro; Kim, Almond e Shute precisaram de um procedimento de dez passos para uma única família de tarefas, e a primeira versão da rede, com parâmetros de especialistas, teve correlação com o pós-teste em torno de 0,1, subindo para cerca de 0,36 após calibração com dados de campo [F: kim2016applying, Step 8]. Os autores ressalvam que redes bayesianas "are not a panacea": não ajudam se o jogo não fornece evidência adequada ou exige competências não modeladas [F: kim2016applying, Discussion].

## Alternativas e comparações

| Abordagem | Ponto de partida | Risco principal |
|---|---|---|
| ECD | Afirmações e argumento, depois tarefas e eventos | Custo de projeto; modelo pode não caber nos dados [I] |
| Mineração exploratória de logs (EDM) | Padrões nos dados disponíveis | Variáveis sem relação explícita com variáveis latentes [F: mislevy2012design, p. 32] |
| Pontuação ad hoc do jogo (pontos, fases) | Mecânica do jogo | Sem quantificação do valor de evidência [F: mislevy2012design, p. 32] |

Mislevy, Behrens, DiCerbo e Levy defendem que ECD e mineração de dados não são opostos: a mineração faz geração e seleção de atributos que alimentam a *evidence identification*, num diálogo entre projeto e descoberta [F: mislevy2012design, resumo, p. 32].

## Exemplo técnico independente de domínio

Uma Q-matrix aumentada liga cada tarefa às variáveis do student model e guarda dificuldade e discriminação estimadas por especialistas, usadas como priors [F: kim2016applying, Step 1, Step 5]:

```
tarefa   | obs           | habilidade_A | habilidade_B | dificuldade(prior) | discriminacao(prior)
fase_07  | resultado_fase|      1       |      0       |  ouro: 2, prata: 1 |  1.2
fase_08  | resultado_fase|      1       |      1       |  ouro: 3, prata: 1 |  0.8
# calibração: priors x 10 como pseudo-observações + contagens de campo -> novas tabelas
```

## Relações com outros conceitos

Depende da teoria de validade de `lae.psy.reliability-and-validity`. O student model de ECD é um caso de `adp.lm.learner-model`; a captura que alimenta o processo de apresentação é tratada em `dat.ev.game-telemetry`. A aplicação a jogos está em `gam.instr.stealth-assessment` e o percurso do evento ao indicador em `gam.instr.telemetry-as-evidence`. Equidade da medida: `lae.psy.fairness-in-measurement`.

## Lacunas e questões abertas

- A versão em periódico de 2003 e o relatório ETS RR-03-16 não foram abertos; usaram-se as versões CRESST (CSE TR 597 e CSE Report 632) dos mesmos textos.
- O relatório de 2014 do GlassLab (*Psychometric considerations in game-based assessment*) não abriu; usou-se o capítulo de 2015 dos mesmos autores.
- Falta documentação aberta de custo e tempo de um projeto ECD completo em jogo comercial.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| mislevy2003structure | academico (CSE TR 597) | 2026-10-30 |
| mislevy2004brief | academico (CSE Report 632) | 2026-10-30 |
| mislevy2015psychometrics | academico | 2026-10-30 |
| mislevy2012design | academico | 2026-10-30 |
| kim2016applying | academico (cópia da autora) | 2026-10-30 |
| shute2011stealth | academico (cópia da autora) | 2026-10-30 |
