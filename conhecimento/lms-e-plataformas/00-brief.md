---
id: lms.brief
titulo: Brief do domínio LMS e plataformas de referência
tipo: relatorio
dominio: lms-e-plataformas
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: LMS e plataformas de referência

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Estudo técnico de plataformas existentes como referência de arquitetura, mecânicas e integração. Três famílias: sistemas de gestão de aprendizagem (Moodle, Canvas, Google Classroom); plataformas adaptativas (ALEKS, MATHia, DreamBox, Khan Academy e similares); jogos sérios e aplicações para neurodivergência com evidência publicada (EndeavorRx, Cogmed e similares). Para cada plataforma: arquitetura pública, modelo de adaptação quando documentado, padrões de interoperabilidade suportados, evidências de eficácia e críticas.

O estudo do Duolingo em `benchmarks/duolingo/` (raiz do repositório) é o primeiro documento desta família. Decisão tomada em 29/10/2026: benchmarks com imagens e índices JSON ficam em `benchmarks/`, fora do modelo documental; este domínio registra cada um como estudo de caso curto com id (`serious-games/duolingo.md`, `lms.case.duolingo`).

Fora do escopo: comparação comercial, precificação, decisões de adoção.

## Estrutura sugerida

- `lms/`: Moodle, Canvas, Google Classroom.
- `adaptive/`: plataformas adaptativas.
- `serious-games/`: jogos sérios com evidência, com atenção a educação especial.
- `comparisons/`: tabelas por critério (adaptação, interoperabilidade, acessibilidade, evidência).

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. Documentação oficial e de desenvolvedor de cada plataforma, com versão.
2. Artigos revisados por pares sobre eficácia (ensaios, metanálises); registros regulatórios quando existirem (ex.: FDA para EndeavorRx).
3. Relatórios de avaliação independentes (ex.: What Works Clearinghouse, Evidence for ESSA).
4. Diretrizes de acessibilidade aplicáveis (WCAG) e como cada plataforma as declara atender.

## Perguntas abertas

- Que plataformas documentam publicamente o modelo de adaptação?
- Quais têm evidência de eficácia em populações neurodivergentes?
- Que padrões de interoperabilidade cada uma expõe de fato (não só declara)?
