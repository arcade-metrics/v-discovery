---
id: lae.brief
titulo: Brief do domínio learning analytics, mineração de dados e avaliação
tipo: relatorio
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: learning analytics, mineração de dados e avaliação

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Como transformar interações de alunos em indicadores confiáveis e em julgamentos de valor sobre aprendizagem. Inclui: fundamentos e métodos de Learning Analytics (LA) e Educational Data Mining (EDM), e o que distingue as duas tradições; proveniência e qualidade dos dados usados para análise (linhagem, versionamento, vieses de coleta, ética de uso secundário); construção de indicadores de participação e desempenho (engajamento, risco de evasão, painéis de acompanhamento); desenho de avaliação formativa e somativa e sua relação com os indicadores; psicometria clássica e moderna aplicada à validação de instrumentos (teoria clássica dos testes, confiabilidade, validade de construto, fairness); métodos para avaliar se uma intervenção ou produto educacional de fato gera resultado de aprendizagem (desenho experimental e quase-experimental, efeito de tratamento, replicação).

Fora do escopo: esquema de evento e telemetria bruta, FAIR, LGPD e datasets públicos (ficam em `dados-pesquisa-e-eventos`); teoria de resposta ao item, Elo e knowledge tracing como modelos de aluno (ficam em `aprendizagem-adaptativa/item-response` e `aprendizagem-adaptativa/knowledge-tracing`, citados aqui apenas como insumo de indicador); formatos padronizados de registro e troca de avaliação, como xAPI, Caliper e QTI (ficam em `interoperabilidade`).

## Estrutura sugerida

- `foundations/`: Learning Analytics vs. Educational Data Mining, histórico, comunidades e venues de referência.
- `data-quality/`: proveniência, linhagem, qualidade e vieses dos dados usados em análise.
- `indicators/`: indicadores de participação, engajamento e desempenho, painéis.
- `assessment-design/`: avaliação formativa e somativa, alinhamento construtivo.
- `psychometrics/`: teoria clássica dos testes, confiabilidade, validade, fairness em medição (TRI aprofundada remete a `aprendizagem-adaptativa`).
- `evaluation-methods/`: desenho experimental e quase-experimental para avaliar resultados educacionais.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. Siemens e Baker, origens e definições de Learning Analytics; Romero e Ventura, revisões de Educational Data Mining.
2. Society for Learning Analytics Research (SoLAR) e International Educational Data Mining Society, atas de LAK e EDM.
3. Gašević, Dawson e Siemens, sobre qualidade e proveniência de dados em LA.
4. Crocker e Algina, "Introduction to Classical and Modern Test Theory".
5. AERA/APA/NCME, "Standards for Educational and Psychological Testing".
6. Biggs, alinhamento construtivo ("constructive alignment"); Black e Wiliam, avaliação formativa.
7. Shadish, Cook e Campbell, "Experimental and Quasi-Experimental Designs for Generalized Causal Inference".

## Perguntas abertas

- Onde fica a fronteira prática entre um indicador de LA e um modelo preditivo de `aprendizagem-adaptativa`?
- Que garantias de qualidade de dado um indicador exige antes de ser exposto num painel?
- Como validar instrumentos de avaliação formativa de baixo custo sem infraestrutura de TRI completa?
- Que desenho de avaliação de resultado é viável dentro do ciclo de produto, sem virar um estudo acadêmico à parte?
