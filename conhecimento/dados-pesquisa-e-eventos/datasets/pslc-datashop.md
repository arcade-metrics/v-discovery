---
id: dat.ds.pslc-datashop
titulo: PSLC DataShop
tipo: estudo-de-caso
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [koedinger2010datashop, koedinger2008open, datashop2026about, datashop2026kcmodels, datashop2026importformat, datashop2026export, datashop2026glossary, datashop2026faq, datashop2026terms, datashop2026irb, stamper2010kddcup, datashop2010kddcuprules, yu2010feature, liu2022pykt, choi2020ednet]
relacoes:
  - { tipo: parte-de, alvo: dat.ds.comparison }
  - { tipo: depende-de, alvo: adp.id.knowledge-components }
  - { tipo: complementa, alvo: adp.id.kli-framework }
  - { tipo: complementa, alvo: dat.ev.event-model }
  - { tipo: complementa, alvo: dat.qual.granularity-and-constructs }
  - { tipo: complementa, alvo: dat.rd.repositories-and-versioning }
  - { tipo: complementa, alvo: dat.rd.data-documentation }
  - { tipo: relacionado-a, alvo: dat.ethics.cep-conep-system }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
termos: [DataShop, transação, passo, problema, oportunidade, student-step rollup, student-problem rollup, knowledge component model, Additive Factors Model, shareability, KDD Cup 2010]
---

# PSLC DataShop

## Definição e terminologia

O **DataShop** é um repositório e aplicação web para dados de interação entre estudantes e software educacional, criado no Pittsburgh Science of Learning Center (PSLC) na Carnegie Mellon University; os autores o descrevem como "a data repository and web application for learning science researchers and educational data mining researchers" [F: koedinger2010datashop, §I]. A documentação atual o define como "a data analysis service for the learning science community", com dois serviços: um repositório central para guardar dados de pesquisa e um conjunto de ferramentas de análise e relatório [F: datashop2026about]. A versão do software indicada no rodapé em 30/10/2026 é 11.4.0, de 23/03/2026 [F: datashop2026terms].

DataShop não é um dataset único: é um repositório de muitos datasets, de domínios, idades e sistemas diferentes, organizados em projetos [F: koedinger2010datashop, §I]. O que todos têm em comum é o **formato**, e é esse formato que faz do DataShop referência para quem projeta um esquema de evento de aprendizagem [I].

Vocabulário do glossário oficial [F: datashop2026glossary]:
- **transação**: "an interaction between the student and the tutoring system"; pedido de dica, tentativa errada e tentativa certa contam uma transação cada, e um passo pode ter várias;
- **passo** (step): "an observable part of the solution to a problem", parcialmente determinado pela interface;
- **problema**: tarefa que tipicamente envolve vários passos;
- **knowledge component** (KC): "a piece of information that can be used to accomplish tasks";
- **oportunidade**: cada vez que um passo com o KC associado aparece; todas as tentativas e dicas naquele passo contam uma oportunidade;
- **KC model**: "a list of mappings between each step and one or more knowledge components", também chamado transfer model ou skill model.

## Problema que resolve

Dados de software educacional historicamente ficavam em formatos heterogêneos (logs de streaming, logs resumidos, bancos próprios de cada pesquisador) [F: koedinger2010datashop, Introduction]. O DataShop propõe um formato comum e descritivo, "descriptive, not prescriptive", que registra a interação em grão fino com o contexto dela, sem tentar descrever recursos de aprendizagem a priori como SCORM ou conteúdo de teste como QTI [F: koedinger2010datashop, §II]. Isso permite reanálise secundária, comparação de modelos de KC sobre os mesmos dados e curvas de aprendizagem padronizadas [F: koedinger2010datashop, §II, §IV].

## Fundamentos e funcionamento

### Modelo de log

O modelo tem três construtos: mensagem de contexto (aluno, problema, sessão), mensagem de ferramenta (ação do aluno na interface) e mensagem de tutor (resposta do sistema à ação); o par ferramenta-tutor ligado pelo contexto vira uma **transação** [F: koedinger2010datashop, §II]. A transação guarda aluno, sessão, tempo, problema, passo, número da tentativa, tipo (tentativa ou pedido de dica), entrada, resposta do tutor, nível de dica, condição experimental e KCs [F: koedinger2010datashop, §II]. Ações "untutored", como tocar um áudio ou navegar páginas, são guardadas como mensagens de ferramenta sem par [F: koedinger2010datashop, §II]. A entrada pode ser em XML, inclusive enviada em tempo real ao servidor de logging, ou em texto tabulado; os logs XML são processados toda noite [F: koedinger2010datashop, §III].

### Formato de transação tabulado

Colunas obrigatórias: `Anon Student Id`, `Session Id`, `Time`, `Level (título)`, `Problem Name` e ao menos um de `Step Name`, `Selection` ou `Action` [F: datashop2026importformat]. Opcionais relevantes: `Time Zone`, `Student Response Type` e `Tutor Response Type` (por exemplo `ATTEMPT`, `HINT_REQUEST`, `RESULT`, `HINT_MSG`), `Outcome` (`CORRECT`, `INCORRECT`, `HINT`), `Selection`/`Action`/`Input`, `Feedback Text`, `Help Level`, `Condition Name`/`Condition Type`, `KC (modelo)`, `School`, `Class`, campos customizados `CF (nome)` e `Event Type` (`assess`, `instruct`, `assess_instruct`), que altera a contagem de oportunidades [F: datashop2026importformat]. `Time` é a hora local do evento, "such as when a student presses return"; o formato de exportação usa precisão de milissegundo (`yyyy-MM-dd HH:mm:ss.SSS`), e a importação aceita também precisão de segundo e de minuto [F: datashop2026importformat].

### Exportações

Há três exportações tabuladas: por transação, por aluno-passo (student-step) e por aluno-problema [F: datashop2026export]. A student-step traz `Step Start Time`, `Step Duration`, `Correct Step Duration`, `Error Step Duration`, `First Attempt`, `Incorrects`, `Hints`, `Corrects` e, por modelo de KC, `Opportunity` e `Predicted Error Rate`, esta uma estimativa do Additive Factors Model [F: datashop2026export]. A duração do passo é a soma das durações das transações atribuídas a ele; o início do passo usa o tempo da transação anterior se ela ocorreu até 10 minutos antes, senão fica nulo [F: datashop2026export]. A agregação student-step é a base das curvas de aprendizagem e do Performance Profiler [F: koedinger2010datashop, §II].

### Modelos de KC

Um passo pode ter zero, um ou vários KCs; pesquisadores importam mapeamentos alternativos e o DataShop calcula medidas de ajuste como BIC para compará-los, e alguns datasets chegaram a dez modelos de KC [F: koedinger2010datashop, §II]. A documentação atual informa cinco medidas por modelo: AIC, BIC e três valores de RMSE de validação cruzada, com BIC como ordenação padrão [F: datashop2026kcmodels]. O conceito e o método estão em `adp.id.knowledge-components`.

### Escala

Em maio de 2008 havia 114 datasets em 42 projetos, cerca de 18 milhões de transações e 70.000 horas-aluno, com ações registradas "roughly every 20 seconds" [F: koedinger2008open, Abstract, §2]. Em junho de 2009, 164 datasets em 50 projetos, 25 milhões de transações e mais de 111.000 horas-aluno [F: koedinger2010datashop, §I]. A página inicial em 30/10/2026 informava apenas 747.999 ações de aluno adicionadas nos últimos três meses; não foi localizado total atual [F: datashop2026about].

## Requisitos e pressupostos

### Acesso, desidentificação e termos

- Datasets públicos podem ser usados sem permissão; privados exigem pedido de acesso ao PI pelo próprio sistema [F: datashop2026faq].
- Desde abril de 2012, todo dataset novo declara o tipo de coleta (não humano; humano sob IRB sem consentimento; humano sob IRB com consentimento) e anexa aprovação e, quando houver, o termo de consentimento [F: datashop2026irb]. Compartilhar fora da equipe exige revisão de "shareability"; o dado é compartilhável se não for de seres humanos ou se o IRB permitir o compartilhamento, e deve estar desidentificado, isto é, "the identity of subjects is not knowable from the data" [F: datashop2026irb].
- Termos de uso, vigentes desde 16/01/2012: não tentar desanonimizar, não criar dataset com informação que identifique alunos, uso só para pesquisa e não comercial, não redistribuir dados obtidos no DataShop [F: datashop2026terms]. O FAQ exige reconhecer a fonte na publicação [F: datashop2026faq].
- O identificador do aluno é `Anon Student Id` [F: datashop2026importformat]; a documentação consultada não descreve como o repositório gera ou verifica esse pseudônimo, o que fica com o depositante [I].

## Vantagens e limitações

Vantagens: grão de transação com resposta do sistema, contexto e KC; tempo em milissegundos; longitudinal por semestre ou ano [F: koedinger2010datashop, Introduction]; vários modelos de KC comparáveis sobre os mesmos dados; ferramentas prontas de curva de aprendizagem [I].

Limitações: populações, domínios e qualidade variam por dataset, e cada um precisa ser avaliado isoladamente [I]; nem todo dataset é público (STATICS2011 é obtido por pedido, segundo Choi et al.) [F: choi2020ednet, §3.3]; a duração do passo depende de regras de atribuição (limiar de 10 minutos), então não é latência pura de resposta [F: datashop2026export]; os termos proíbem redistribuição, o que limita republicar subconjuntos derivados [F: datashop2026terms].

## Alternativas e comparações

Comparação com ASSISTments, EdNet, OULAD, Junyi e Duolingo SLAM em `dat.ds.comparison`. O **KDD Cup 2010** é hospedado pelo DataShop: cinco datasets de dois sistemas de tutoria de álgebra (três de desenvolvimento, dois de desafio), em formato aluno-passo com `Anon Student Id`, hierarquia do problema, `Step Start Time`, `Correct First Attempt` e colunas de KC e oportunidade [F: datashop2010kddcuprules]. Os conjuntos de desafio Algebra 2008-2009 e Bridge to Algebra 2008-2009 têm 8.918.055 e 20.012.499 passos de treino [F: yu2010feature, Table 1]. A versão Algebra 2005 é descrita como respostas de alunos de 13 a 14 anos [F: liu2022pykt, §3.2]. Citação pedida: Stamper et al. (2010) com o nome do conjunto [F: stamper2010kddcup].

## Exemplo técnico independente de domínio

```
# uma transação (formato tabulado, colunas mínimas + resposta do sistema)
Anon Student Id  Session Id  Time                     Level(Unit)  Problem Name  Step Name  Student Response Type  Outcome    KC(Default)
stu_7f3a         s_0042      2026-03-14 13:05:22.481  frações      P12           num_1      ATTEMPT                INCORRECT  equivalencia
stu_7f3a         s_0042      2026-03-14 13:05:29.903  frações      P12           num_1      HINT_REQUEST           HINT       equivalencia
stu_7f3a         s_0042      2026-03-14 13:05:41.115  frações      P12           num_1      ATTEMPT                CORRECT    equivalencia
# rollup aluno-passo derivado: First Attempt=incorrect, Incorrects=1, Hints=1, Corrects=1, Opportunity=n
```

## Relações com outros conceitos

Faz parte da comparação `dat.ds.comparison`. Depende da noção de KC (`adp.id.knowledge-components`) e do KLI (`adp.id.kli-framework`). O modelo contexto-ferramenta-tutor é referência para `dat.ev.event-model` e para a discussão de grão em `dat.qual.granularity-and-constructs`. Como repositório, complementa `dat.rd.repositories-and-versioning` e `dat.rd.data-documentation`; a revisão de shareability ligada ao IRB tem paralelo em `dat.ethics.cep-conep-system`; o risco de reidentificação de logs finos está em `psg.deid.reidentification-risk`. Modelos treinados nos seus dados são avaliados por `adp.eval.predictive-metrics`.

## Lacunas e questões abertas

- Não foi localizado total atual de datasets, alunos e transações; a página de métricas não carregou (ECONNRESET).
- Não foi aberta a página de exportação "Export Format History"; mudanças de colunas entre versões não foram verificadas.
- O número de alunos de cada conjunto do KDD Cup 2010 não foi verificado em fonte primária.
- A documentação não diz como o `Anon Student Id` é produzido nem se há verificação de desidentificação além da declaração do depositante.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| koedinger2010datashop | academico | 2026-10-30 |
| koedinger2008open | academico | 2026-10-30 |
| datashop2026about | fornecedor | 2026-10-30 |
| datashop2026kcmodels | fornecedor | 2026-10-30 |
| datashop2026importformat | fornecedor | 2026-10-30 |
| datashop2026export | fornecedor | 2026-10-30 |
| datashop2026glossary | fornecedor | 2026-10-30 |
| datashop2026faq | fornecedor | 2026-10-30 |
| datashop2026terms | fornecedor | 2026-10-30 |
| datashop2026irb | fornecedor | 2026-10-30 |
| stamper2010kddcup | fornecedor | 2026-10-30 |
| datashop2010kddcuprules | fornecedor | 2026-10-30 |
| yu2010feature | academico | 2026-10-30 |
| liu2022pykt | academico | 2026-10-30 |
| choi2020ednet | academico | 2026-10-30 |
