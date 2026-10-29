---
id: adp.dt.learning-digital-twin
titulo: Learning digital twin (gêmeo digital do aprendiz)
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [furini2022pillars, bachmann2024dteducation, rigoni2024sciencetwins, lin2024hdtsurvey, fuller2020enabling, grieves2017emergent]
relacoes:
  - { tipo: parte-de, alvo: adp.dt.human-digital-twin }
  - { tipo: depende-de, alvo: adp.dt.digital-twin-origins }
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
  - { tipo: complementa, alvo: adp.lm.open-learner-model }
  - { tipo: relacionado-a, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: complementa, alvo: adp.dt.architecture-and-validation }
  - { tipo: avaliado-por, alvo: adp.eval.evaluation-protocols }
termos: [learning digital twin, student digital twin, digital twin of the learner, cognitive twin, smart classroom, digital twin in education]
---

# Learning digital twin (gêmeo digital do aprendiz)

## Definição e terminologia

Não existe definição consolidada. A proposta mais citada em veículo de alto alcance é a de Furini et al. (Communications of the ACM): digital twins como "réplicas digitais de estudantes", criadas combinando dados de histórico acadêmico e atividades de estudo (inseridos manualmente), consumo de material didático digital e comportamento no campus (coletados automaticamente), para alimentar recomendação e previsão personalizadas [F: furini2022pillars]. A terminologia é instável: as fontes usam "digital twin of the student", "student's digital twin", "digital student profile" e, em trabalho de workshop, "learning digital twin (num certo sentido, uma instância do seu gêmeo cognitivo no escopo do curso)" [F: rigoni2024sciencetwins]; o survey de human digital twins usa HDT para sistemas de sala de aula [F: lin2024hdtsurvey]. Nenhuma das revisões abertas define formalmente "learning digital twin" como termo técnico [I].

O que não é: a maior parte do que a literatura chama de "digital twin em educação" **não** é gêmeo do aluno, e sim gêmeo de laboratórios, equipamentos, experimentos ou campi usados como recurso didático (ver abaixo). Convém também não confundir com o uso de DT como *tema* de ensino (cursos que ensinam a construir twins industriais) [F: bachmann2024dteducation].

## Problema que resolve

O problema declarado por Furini et al. é a rigidez dos modelos de ensino frente a estudantes com trabalho, família, restrições financeiras e deficiências — com evasão universitária de cerca de 40% nos EUA e 10% na Europa, segundo as fontes que citam — e a promessa é personalização: recomendar o que estudar, quando e como, e prever nota, risco de reprovação e de evasão [F: furini2022pillars]. É, na essência, o mesmo problema que motiva sistemas adaptativos e learning analytics (`adp.adapt.adaptive-learning-systems`); a novidade reivindicada está na metáfora do espelhamento contínuo e individual [I].

## Verificação crítica da literatura

### (a) Do que tratam as revisões de "digital twin em educação"

A revisão de Bachmann et al. (SBIE 2024, bases Scopus e MDPI) organiza todo o campo em: STEAM (laboratórios e equipamentos virtualizados, campi virtuais, gamificação), educação em saúde (gêmeos de pacientes e órgãos para treinar profissionais), ensino de arquitetura/engenharia/construção e treinamento técnico-industrial — ou seja, exclusivamente gêmeos de coisas e processos usados para ensinar; não há categoria nem seção para gêmeos do aluno [F: bachmann2024dteducation]. A mini-revisão de Rigoni e Düştegör sobre smart classrooms encontra o mesmo quadro: twins de experimentos (Telelab, laboratórios de mecânica dos fluidos, HPLC, robótica, sistemas de controle), monitoramento de presença (DeepClassRooms) e rastreamento de olhar da turma; os autores classificam a integração de DT em salas de aula como "ainda em estágios iniciais" [F: rigoni2024sciencetwins]. Isso confirma a hipótese de que o gêmeo do aprendiz é minoritário na literatura da área [F: bachmann2024dteducation] [F: rigoni2024sciencetwins].

### (b) Trabalhos que propõem gêmeo digital DO aluno

- **Furini et al. 2022** (CACM): proposta de modelo de aprendizagem personalizada em três camadas (infraestrutura multimídia/IoT; dados — criação do twin do estudante e produção de material enriquecido; apresentação — interfaces acessíveis), com oito desafios de pesquisa. É um artigo de visão: os próprios autores admitem que o cenário "pode soar como ficção científica" e nenhum componente é implementado ou avaliado no artigo [F: furini2022pillars]. [H] enquanto sistema.
- **Pitelinsky et al. 2024** (citado por Rigoni & Düştegör): "digital twins e perfis digitais básicos de estudantes" para analisar desempenho, comportamento e necessidades [F: rigoni2024sciencetwins]. Fonte original não aberta.
- **Razzaq et al., DeepClassRooms** (citado por Lin et al. e Rigoni & Düştegör): framework de DT implementado com CNNs para monitorar presença e expressões faciais de alunos e professores em campus — implementação real, mas de vigilância de sala, não de modelo cognitivo do aprendiz [F: lin2024hdtsurvey] [F: rigoni2024sciencetwins] [I].
- **Rigoni & Düştegör 2024**: o gêmeo construído é do *experimento* (sensores Arduino/RaspberryPi); o "learning digital twin de cada estudante" aparece só como trabalho futuro, a construir sobre o registro de respostas dos alunos [F: rigoni2024sciencetwins]. [H].

### (c) Critérios que distinguiriam um learning digital twin de um learner model

Aplicando os critérios definidores herdados de `adp.dt.digital-twin-origins` [I]:

| Critério (origem) | Learner model típico | O que o LDT exigiria |
|---|---|---|
| Atualização contínua e automática [F: fuller2020enabling] | atualiza a cada resposta observada; já é um "digital shadow" [I] | fluxo multimodal contínuo (sensores, logs, contexto) [F: furini2022pillars] |
| Bidirecionalidade [F: fuller2020enabling] | o modelo informa a política adaptativa, que age sobre o aluno — o laço já existe em sistemas adaptativos [I] | recomendação/intervenção automática explícita como canal virtual→físico [F: furini2022pillars] |
| Simulação what-if [F: grieves2017emergent] | raro; modelos como BKT preveem apenas a próxima resposta [I] | "voar missões futuras": simular trajetórias de estudo alternativas antes de executá-las [I, por analogia com F: glaessgen2012paradigm em adp.dt.digital-twin-origins] |
| Fidelidade individual (DTI) [F: grieves2017emergent] | parâmetros por aluno sobre modelo populacional [I] | modelo individual com histórico completo de ciclo de vida do aprendiz [I] |

A leitura crítica: pelos dois primeiros critérios, um sistema adaptativo convencional (modelo de aluno + política de sequenciamento) **já satisfaz** a definição funcional de digital twin; o que as propostas de LDT acrescentam de fato é a ambição de abrangência (dados além do desempenho: presença, biblioteca, sono, posição na sala [F: furini2022pillars]) e a capacidade de simulação contrafactual — e esta segunda quase nunca é especificada tecnicamente [I]. Há, portanto, risco real de o termo ser re-rotulação de learner modeling e learning analytics com vocabulário da Indústria 4.0 [H].

### (d) Estado da evidência

Nenhuma das fontes abertas relata um gêmeo digital do aprendiz implementado e avaliado empiricamente quanto a efeito sobre aprendizagem [I]. O que existe de empírico na interseção DT×educação: avaliação comparativa de *treinamento com gêmeo de equipamento* (estudo com grupos usando DT de braço robótico contra material em papel, com melhor preparo do grupo DT [F: bachmann2024dteducation]); redução de 26% de custo de laboratório com DT [F: bachmann2024dteducation]; e sistemas de monitoramento implementados (DeepClassRooms) [F: lin2024hdtsurvey]. As propostas de gêmeo do aluno em si permanecem conceituais [F: furini2022pillars] [F: rigoni2024sciencetwins].

## Requisitos e pressupostos

Além dos de `adp.dt.human-digital-twin`: instrumentação de espaços educacionais (IoT, câmeras, Wi-Fi) e consentimento compatível com LGPD/GDPR — Furini et al. repetem que "todos os esforços devem considerar regulações de privacidade" [F: furini2022pillars]; dados de desempenho suficientes por aluno (ver `adp.kt.bayesian-knowledge-tracing` para o custo de estimar estados latentes com dados esparsos) [I]; e um modelo cognitivo capaz de simulação prospectiva — pressuposto mais forte que o de qualquer learner model em uso [H].

## Vantagens e limitações

Vantagens potenciais, se realizado: unificação de fontes de dados hoje dispersas; recomendações e alertas de risco em linguagem de intervenção; inclusão de estudantes com restrições de presença [F: furini2022pillars]. Limitações: vigilância extensiva de menores/estudantes e seus riscos de privacidade e consentimento [F: furini2022pillars] [F: bachmann2024dteducation]; custo de infraestrutura e divisão digital [F: bachmann2024dteducation]; e o risco conceitual de prometer "espelho fiel" quando o substrato é um modelo estatístico calibrado — fidelidade retórica acima da fidelidade mensurável [H].

## Métricas e métodos de avaliação

Nada específico publicado nas fontes abertas [I]. Por construção, um LDT deveria ser avaliado como modelo preditivo (calibração, AUC — `adp.eval.predictive-metrics`), como sistema adaptativo (efeito em aprendizagem — `adp.eval.educational-effectiveness`) e como twin (fidelidade e sincronização — `adp.dt.architecture-and-validation`) [I].

## Exemplo técnico independente de domínio

Especificação mínima que diferenciaria um LDT de um learner model, em pseudocódigo [I]:

```
estado = modelo_de_aluno(historico)          # ex.: overlay + traçado de conhecimento
loop contínuo:
    e = eventos.ler()                        # respostas, acessos, contexto (multimodal)
    estado.atualizar(e)                      # físico -> virtual (shadow)
    para cada plano p em planos_candidatos:  # simulação what-if (marca distintiva)
        resultado[p] = simular(estado, p, horizonte)
    acao = escolher(resultado)               # política
    entregar(acao)                           # virtual -> físico (fecha o twin)
    registrar(previsao=resultado[acao])      # para validação prospectiva
```

## Relações com outros conceitos

Parte de `adp.dt.human-digital-twin` (especialização ao aprendiz). O contraste central é com `adp.lm.learner-model`: a tese deste documento é que o LDT só se distingue de um learner model acoplado a um sistema adaptativo (`adp.adapt.adaptive-learning-systems`) se entregar simulação what-if e integração multimodal contínua [I]. `adp.lm.open-learner-model` complementa: abrir o twin ao aluno responde em parte às críticas de representação herdadas do HDT [I]. A avaliação remete a `adp.eval.evaluation-protocols`.

## Lacunas e questões abertas

- Não localizamos revisão sistemática dedicada ao gêmeo digital *do aluno* (as encontradas cobrem DT em educação em geral); candidatas em periódicos de educação (Smart Learning Environments, Education and Information Technologies) não retornaram em buscas específicas. Uma revisão SLR de 2025 (Indonesian Journal of Educational Technology/IJET) que distinguiria "Digital Twin of the Learner" como domínio foi tentada e não aberta (HTTP 403): não verificada.
- A revisão sistemática de learner models de Böck et al. (2025, UMUAI), que lista "digital twin" entre as palavras-chave, foi localizada mas não lida; cruzá-la com este documento é o próximo passo natural.
- Furini et al. não citam a literatura de AIED/learner modeling (Corbett & Anderson, Bull & Kay ausentes das referências) — o diálogo entre as duas comunidades parece não existir [F: furini2022pillars, pela lista de referências] [I].
- Falta qualquer estudo que registre previsões de um LDT antes dos desfechos (validação prospectiva); sem isso, a reivindicação de "espelho" é inverificável [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| furini2022pillars | academico | 2026-10-29 |
| bachmann2024dteducation | academico | 2026-10-29 |
| rigoni2024sciencetwins | academico | 2026-10-29 |
| lin2024hdtsurvey | academico | 2026-10-29 |
| fuller2020enabling | academico | 2026-10-29 |
| grieves2017emergent | academico | 2026-10-29 |
