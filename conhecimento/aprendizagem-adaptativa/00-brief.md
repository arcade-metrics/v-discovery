---
id: adp.brief
titulo: Brief do domínio aprendizagem adaptativa e gêmeos digitais para aprendizagem
tipo: relatorio
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: aprendizagem adaptativa e gêmeos digitais para aprendizagem

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Modelagem do aluno e adaptação da experiência de aprendizagem a partir de dados de interação. Inclui: modelos de aluno (learner models) e modelos de aluno abertos; knowledge tracing e estimação de domínio; teoria de resposta ao item e modelos de habilidade; ajuste dinâmico de dificuldade; sequenciamento e recomendação de atividades; avaliação embutida em jogos (stealth assessment) e evidence-centered design; gêmeos digitais aplicados a pessoas e à educação, com atenção à diferença entre a metáfora e o modelo computacional; interpretabilidade das inferências para quem decide.

Fora do escopo: pedagogia geral, design de conteúdo, interfaces. Infraestrutura de dados e eventos fica em `dados-pesquisa-e-eventos`; representação semântica fica em `grafo-conhecimento-educacional`.

## Estrutura sugerida

- `learner-models/`: modelos de aluno, overlay, modelos abertos.
- `knowledge-tracing/`: BKT, PFA, DKT e sucessores, comparações.
- `item-response/`: IRT, modelos de rating (Elo) para aprendizagem.
- `adaptation/`: DDA, sequenciamento, políticas de seleção.
- `assessment/`: ECD, stealth assessment, validade.
- `digital-twins/`: origem, definições, aplicações a pessoas e educação, limites.
- `evaluation/`: métricas (AUC, RMSE, calibração), protocolos (validação interna e prospectiva).

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. Corbett e Anderson, 1995, knowledge tracing (BKT).
2. Pavlik, Cen e Koedinger, 2009, Performance Factors Analysis.
3. Piech et al., 2015, Deep Knowledge Tracing, e revisões posteriores sobre KT.
4. Pelánek, trabalhos sobre modelos de aluno e Elo aplicado a educação.
5. Bull e Kay, Open Learner Models.
6. VanLehn, 2006, comportamento de sistemas tutores, e Koedinger, Corbett e Perfetti, framework KLI.
7. Mislevy, Steinberg e Almond, Evidence-Centered Design; Shute, stealth assessment.
8. Hunicke, 2005, ajuste dinâmico de dificuldade.
9. Grieves, origem do conceito de gêmeo digital; revisões sistemáticas sobre gêmeos digitais em educação e sobre human digital twins.
10. Baker e colaboradores, educational data mining e learning analytics.

## Perguntas abertas

- Qual a definição operacional de "gêmeo digital" que distingue o conceito de um modelo de aluno tradicional?
- Que evidências existem de que modelos baseados em grafos superam KT clássico em populações heterogêneas?
- Como avaliar interpretabilidade de inferências para professores?
- Quais requisitos de dados mínimos cada família de modelo exige?
