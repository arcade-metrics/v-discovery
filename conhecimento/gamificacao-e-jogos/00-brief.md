---
id: gam.brief
titulo: Brief do domínio gamificação, jogos sérios e aprendizagem baseada em jogos
tipo: relatorio
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: gamificação, jogos sérios e aprendizagem baseada em jogos

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Fundamentos de projeto e avaliação de jogos com finalidade educacional. Inclui: definições e fronteiras entre gamificação, jogos sérios (serious games) e aprendizagem baseada em jogos (game-based learning); mecânicas, regras e sistemas de progressão (pontos, níveis, conquistas, economias, árvores de habilidade, loops de jogo); engajamento, motivação e feedback (teoria da autodeterminação, flow, motivação intrínseca e extrínseca, tipos e tempo de feedback); jogos individuais e colaborativos (cooperação, competição, papéis, interdependência); adaptação dinâmica da dificuldade (dynamic difficulty adjustment, zona de desenvolvimento proximal, flow como alvo); instrumentação e telemetria de jogos com fins de avaliação (evidence-centered design, stealth assessment, eventos que viram evidência); evidências de eficácia educacional (metanálises, desenhos de estudo, efeitos por tipo de mecânica e por população, com atenção a educação especial e neurodivergência). Para cada mecânica ou abordagem: o que é, o construto que pretende afetar, pressupostos, evidência disponível e riscos conhecidos.

Fora do escopo: estudo de jogos e plataformas concretas (fica em `lms-e-plataformas`, que cobre jogos sérios com evidência publicada); infraestrutura de eventos, esquemas, privacidade e datasets (fica em `dados-pesquisa-e-eventos`, aqui entra só o desenho de quais eventos de jogo são evidência de quê); modelos de aluno e knowledge tracing (ficam em `aprendizagem-adaptativa`, aqui entra a adaptação no nível da mecânica de jogo); transporte e sincronização de partidas multiplayer (ficam em `realtime-multiplayer`).

## Estrutura sugerida

- `fundamentos/`: gamificação, jogos sérios, game-based learning, definições e taxonomias.
- `mechanics/`: mecânicas, regras, loops, sistemas de progressão, economias, frameworks de projeto (MDA, LM-GM).
- `motivation/`: autodeterminação, flow, motivação intrínseca e extrínseca, efeito de superjustificação, feedback.
- `social-play/`: jogo individual, cooperativo, competitivo, aprendizagem colaborativa mediada por jogo.
- `difficulty/`: adaptação dinâmica da dificuldade, modelos de desafio, relação com aprendizagem adaptativa.
- `instrumentation/`: evidence-centered design, stealth assessment, telemetria de jogo voltada a avaliação, métricas de engajamento.
- `evidence/`: metanálises, desenhos de estudo, efeitos por mecânica e por população, educação especial.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. Deterding, Dixon, Khaled e Nacke, 2011, definição de gamificação; Hamari, Koivisto e Sarsa, 2014, revisão empírica.
2. Hunicke, LeBlanc e Zubek, 2004, framework MDA; Salen e Zimmerman, "Rules of Play"; Arnab et al., 2015, modelo LM-GM.
3. Ryan e Deci, teoria da autodeterminação; Ryan, Rigby e Przybylski, 2006, motivação em videogames; Csikszentmihalyi, flow; Malone, 1981, motivação intrínseca em jogos.
4. Hunicke, 2005, e revisões sobre dynamic difficulty adjustment (ex.: Zohaib, 2018).
5. Mislevy, Steinberg e Almond, evidence-centered design; Shute, stealth assessment; Drachen, Seif El-Nasr e Canossa, "Game Analytics".
6. Metanálises de eficácia: Wouters et al., 2013; Clark, Tanner-Smith e Killingsworth, 2016; Sailer e Homner, 2020; revisões sistemáticas de Connolly et al., 2012, e Boyle et al., 2016.
7. Revisões sobre jogos sérios e gamificação em educação especial e populações neurodivergentes (TEA, TDAH, deficiência intelectual), a localizar na pesquisa.

## Perguntas abertas

- Quais mecânicas têm efeito medido sobre aprendizagem, e não só sobre engajamento ou tempo de uso?
- Recompensas extrínsecas (pontos, sequências, conquistas) reduzem a motivação intrínseca em crianças? Em que condições?
- Como separar dificuldade do jogo de dificuldade do conteúdo ao adaptar, e como isso se integra a um modelo de aluno?
- Que eventos de jogo são evidência válida de um construto cognitivo-motor, e como validar esse vínculo?
- Jogo colaborativo melhora resultados em educação especial, ou depende de mediação do professor?
- Que desenhos de estudo bastam para afirmar eficácia, e quais metanálises têm qualidade metodológica suficiente?
