---
id: lms.plano-ids
titulo: Plano de identificadores do domínio
tipo: mapa
dominio: lms-e-plataformas
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Plano de identificadores do domínio lms-e-plataformas

Lista de ids planejados para a primeira versão, derivada da estrutura sugerida em `00-brief.md`. Relações entre documentos usam estes ids, nunca caminhos de arquivo. Prefixos de área: `plat` (LMS), `adapt` (plataformas adaptativas), `sg` (jogos sérios e aplicações com evidência), `case` (estudos de caso que apontam para `benchmarks/`), `cmp` (comparações).

Cada documento de plataforma segue a mesma pauta do brief: arquitetura pública, modelo de adaptação quando documentado, padrões de interoperabilidade suportados de fato, declaração de acessibilidade, evidências de eficácia e críticas. Fora do escopo: preço e decisão de adoção.

| Pasta | Id | Arquivo | Escopo em uma linha |
|---|---|---|---|
| lms | lms.plat.moodle | lms/moodle.md | Moodle: arquitetura de plugins, padrões (LTI, SCORM, xAPI via plugin, IMS CC), acessibilidade declarada, evidência |
| lms | lms.plat.canvas | lms/canvas.md | Canvas LMS: APIs, LTI Advantage, Caliper, acessibilidade declarada |
| lms | lms.plat.google-classroom | lms/google-classroom.md | Google Classroom: APIs, integrações, limites como LMS, acessibilidade |
| adaptive | lms.adapt.aleks | adaptive/aleks.md | ALEKS: teoria dos espaços de conhecimento, modelo de adaptação público, evidência (WWC) |
| adaptive | lms.adapt.mathia | adaptive/mathia.md | MATHia (Carnegie Learning): tutor cognitivo, KLI, evidência (RAND 2014) |
| adaptive | lms.adapt.dreambox | adaptive/dreambox.md | DreamBox: adaptação intra-lição, evidência (Harvard CEPR), críticas |
| adaptive | lms.adapt.khan-academy | adaptive/khan-academy.md | Khan Academy: mastery learning, recomendação, evidência e críticas |
| serious-games | lms.sg.endeavorrx | serious-games/endeavorrx.md | EndeavorRx: tratamento digital com autorização FDA para TDAH, ensaios, limites |
| serious-games | lms.sg.cogmed | serious-games/cogmed.md | Cogmed: treino de memória de trabalho, metanálises e controvérsia sobre transferência |
| serious-games | lms.sg.cognitive-training-controversy | serious-games/cognitive-training-controversy.md | Treino cognitivo comercial (CogniFit, Lumosity e similares): evidência, ações regulatórias, consenso científico |
| comparisons | lms.cmp.adaptation-models | comparisons/adaptation-models.md | Comparação dos modelos de adaptação documentados publicamente |
| comparisons | lms.cmp.interoperability-and-accessibility | comparisons/interoperability-and-accessibility.md | Padrões expostos de fato e declarações de acessibilidade (VPAT, WCAG), por plataforma |
| comparisons | lms.cmp.efficacy-evidence | comparisons/efficacy-evidence.md | Evidência de eficácia por plataforma: desenho, população, tamanho de efeito, avaliador independente |
| serious-games | lms.case.duolingo | serious-games/duolingo.md | Estudo de caso já existente: aponta para `benchmarks/duolingo/` |
| (raiz) | lms.index | README.md | |
| (raiz) | lms.glossario | glossario.md | já existe (aponta para o glossário do benchmark); será ampliado |
| (raiz) | lms.mapa | mapa-conceitos.md | |
| (raiz) | lms.matriz | matriz-comparativa.md | |
| (raiz) | lms.relatorio | relatorio.md | |
| (raiz) | lms.plano-ids | _plano-ids.md | |
| (raiz) | lms.brief | 00-brief.md | |
