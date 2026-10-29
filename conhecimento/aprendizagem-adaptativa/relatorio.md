---
id: adp.relatorio
titulo: Relatório da primeira versão do domínio aprendizagem adaptativa e gêmeos digitais para aprendizagem
tipo: relatorio
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Relatório: primeira versão do domínio aprendizagem adaptativa e gêmeos digitais para aprendizagem

Data: 2026-10-29. Esta é a "primeira versão funcional" pedida pela especificação de pesquisa: estrutura, mapa conceitual, bibliografia inicial e os documentos principais fundamentados em fontes verificadas. Todos os documentos estão em `status: rascunho`; a passagem para `revisado` exige o checklist de `_modelo/checklist-revisao.md` por leitor humano.

## Método aplicado

Oito frentes de pesquisa em paralelo, uma por área (knowledge tracing; item response theory e sucessores atencionais do DKT; memória e esquecimento; algoritmos de repetição espaçada; learner models e KLI; adaptação e sequenciamento; gêmeos digitais de aprendizagem; avaliação), cada uma restrita a abrir as fontes antes de citá-las. Três das oito frentes foram interrompidas por limite de uso da API a meio da execução e retomadas a partir do próprio histórico, sem perda de trabalho. Cada frente produziu seus documentos e um fragmento de bibliografia e índice; os fragmentos foram mesclados em `referencias/bibliografia.bib` e `referencias/indice-fontes.md` por `_modelo/mesclar_referencias.py`. O validador `_modelo/validar.py` confirmou: ids únicos com prefixo correto, todos os alvos de relação existentes, todas as chaves de fonte presentes na bibliografia, nenhuma menção a produto consumidor.

## Cobertura

| Área | Documentos | Observação |
|---|---|---|
| instructional-design | 2 | framework KLI (Koedinger, Corbett & Perfetti 2012) e knowledge components, com Learning Factors Analysis |
| learner-models | 2 | learner model (overlay, inner/outer loop) e open learner model (SMILI☺) |
| knowledge-tracing | 5 | BKT, modelos logísticos (AFM/PFA), DKT, sucessores atencionais (SAKT/AKT/DKVMN), comparação |
| item-response | 2 | IRT (1PL/2PL/3PL, CAT) e Elo aplicado a educação |
| spaced-repetition | 6 | memória e esquecimento, efeitos de espaçamento e teste, algoritmos clássicos (Leitner/SM-2), HLR, FSRS, comparação |
| adaptation | 2 | sistemas adaptativos (inner/outer loop, taxonomia) e políticas de sequenciamento (mastery, Elo, MDP/POMDP) |
| digital-twins | 4 | origem do conceito, human digital twin, learning digital twin, arquitetura e validação |
| evaluation | 4 | métricas preditivas, protocolos de validação, eficácia educacional, populações heterogêneas |
| raiz | 7 | brief, README, glossário, mapa, matriz comparativa, mapa de evidências, plano de ids, este relatório |

Totais: 27 documentos conceituais (29 contando brief e plano de ids), 260 linhas de relações e documentos na seção gerada do mapa (ver `mapa-conceitos.md` para a contagem detalhada por tipo de relação), 94 chaves de bibliografia citadas diretamente no domínio (97 entradas nos fragmentos, com pequena sobreposição intencional de chaves reaproveitadas entre áreas, como `corbett1995kt` e `pelanek2016elo`).

Marcas de afirmação no corpo dos documentos: 1.190 citações de fato com chave de fonte, 153 interpretações marcadas `[I]`, 16 hipóteses marcadas `[H]`.

## O que a especificação de pesquisa pediu e onde está

| Entregável | Local |
|---|---|
| Estrutura de diretórios | `aprendizagem-adaptativa/` (8 pastas temáticas, mais `_plano-ids.md`) |
| README com escopo, organização e contribuição | `README.md` deste domínio e `conhecimento/README.md` |
| Glossário técnico | `glossario.md` |
| Mapa conceitual e relações entre modelos | `mapa-conceitos.md` |
| Documentos técnicos fundamentados em fontes primárias | as 8 pastas temáticas |
| Bibliografia BibTeX | fragmentos mesclados em `conhecimento/referencias/bibliografia.bib` |
| Matriz comparativa dos modelos | `matriz-comparativa.md` |
| Mapa de evidências, limitações e lacunas | `mapa-evidencias.md` |
| Relatório de cobertura e prioridades | este arquivo |

## Decisões de reconciliação com o brief original do domínio

A pasta `aprendizagem-adaptativa/` já existia com um brief anterior (`00-brief.md`) organizado em `learner-models/`, `knowledge-tracing/`, `item-response/`, `adaptation/`, `assessment/`, `digital-twins/`, `evaluation/`. A especificação de pesquisa mais recente propôs uma estrutura paralela (`adaptive-learning/`, `spaced-repetition/`, `instructional-design/`, `learner-state-estimation/`). As duas foram reconciliadas em `_plano-ids.md`:

- `spaced-repetition/` e `instructional-design/` foram adicionadas como áreas novas, porque a especificação as pedia explicitamente e o brief anterior não as cobria.
- `learner-state-estimation/` não virou pasta própria: sua pauta (estimativas, incerteza, evolução temporal) foi distribuída entre `knowledge-tracing/` (estimação por modelo) e `evaluation/` (calibração e protocolos), por já serem tratadas ali com profundidade suficiente para não duplicar.
- `adaptive-learning/` da especificação corresponde a `adaptation/` do brief anterior; manteve-se o nome já em uso.
- `assessment/` (evidence-centered design, stealth assessment) ficou **fora** desta primeira versão: nenhuma das oito frentes de pesquisa teve essa atribuição. Registrado como lacuna de cobertura abaixo, não como decisão de escopo definitiva.
- Ajuste dinâmico de dificuldade (Hunicke 2005), previsto no brief anterior, também não foi pesquisado nesta rodada.

## Fontes que não puderam ser verificadas

Padrão recorrente: bibliotecas digitais pagas (ACM, IEEE, Springer, Elsevier, Wiley, Taylor & Francis) bloquearam acesso automatizado na maior parte das tentativas. Consequências registradas, por área:

- **Beck & Chang 2007** (identifiability em modelagem de aluno) e **Cen, Koedinger & Junker 2006** (versão publicada do LFA): Springer exigiu autenticação; conteúdo citado via fontes alternativas abertas que descrevem os mesmos resultados (van de Sande 2013; versão de workshop de 2005 do LFA).
- **Bull & Kay 2007 e Bull 2020** (Open Learner Models): IOS Press e IEEE Xplore bloquearam; conteúdo sustentado pelo framework SMILI☺ de 2016, efetivamente lido.
- **Ye, Su & Cao 2022 e Su et al. 2023** (fundamentos do FSRS): ACM e IEEE bloquearam mesmo via link de acesso de autor; entraram na bibliografia só com metadados.
- **Jones et al. 2020** (revisão sistemática de digital twin, CIRP JMST): HTTP 403 em quatro repositórios diferentes; só metadados.
- **VanLehn 2011, Kulik & Fletcher 2016, Doroudi & Brunskill 2019** (eficácia de ITS e fairness em KT): parcialmente bloqueados; registrados como lacuna textual nos respectivos documentos, sem números inventados a partir deles.
- **Rasch 1960, Lord 1980, Bjork & Bjork 1992 (capítulo original), Wixted & Ebbesen 1991, Averell & Heathcote 2011**: confirmados apenas por metadados (catálogo, Crossref); conteúdo citado via fontes substitutas abertas quando havia uma equivalente (ex. capítulo de 2023 dos próprios Bjork).
- **Thompson & Weiss 2011** (CAT): bloqueado por proteção anti-bot; não citado.

Todas essas situações estão marcadas no documento correspondente e na nota da entrada BibTeX, com `[metadados]` no título do índice quando aplicável.

## Lacunas de conhecimento e questões abertas

Consolidadas das oito frentes; a lista completa com mais detalhe está em `mapa-evidencias.md`. As perguntas abertas do brief original são respondidas, com reservas, ao longo dos documentos de `knowledge-tracing/`, `digital-twins/` e `evaluation/`; a pergunta sobre "definição operacional de gêmeo digital" tem resposta direta e crítica em `adp.dt.learning-digital-twin`.

1. **Maturidade do conceito de learning digital twin.** A conclusão central desta versão: a maior parte da literatura rotulada "digital twin em educação" trata de laboratórios, equipamentos e campi, não do aluno. Onde a ideia de gêmeo do aprendiz aparece, é proposta de pesquisa futura, nunca sistema implementado e avaliado prospectivamente. Ver `adp.dt.learning-digital-twin` para a argumentação completa.
2. **Avaliação independente do FSRS.** Todo benchmark público encontrado é mantido pela mesma organização que desenvolve o algoritmo.
3. **Desempenho real do Half-Life Regression fora do artigo original.** Reanálise de Ilídio et al. 2026 encontra AUC próxima do acaso para os métodos originais.
4. **Populações heterogêneas e necessidades educacionais específicas.** Pesquisa de fairness em KT cobre alguns atributos (SES, urbanicidade, língua), mas não conecta diretamente com Universal Design for Learning nem cobre deficiência com profundidade.
5. **Área `assessment/` não coberta.** Evidence-centered design e stealth assessment ficaram fora desta versão.
6. **Incerteza da estimativa de estado do aluno.** Nenhuma fonte verificável e específica foi localizada sobre intervalos de confiança para o estado inferido (em oposição a point estimates).

## Próximos passos sugeridos

1. **Revisão humana** dos 27 documentos com o checklist, começando pelos de comparação (`adp.kt.comparison`, `adp.sr.comparison`) e pelos quatro documentos de `digital-twins/`, que concentram as sínteses críticas `[I]`.
2. **Segunda rodada de fontes bloqueadas** com acesso institucional (ACM, IEEE, Springer, Elsevier, Wiley) para fechar as lacunas de Bull & Kay, Cen & Koedinger, VanLehn 2011 e Doroudi & Brunskill 2019.
3. **Cobrir `assessment/`** (evidence-centered design, stealth assessment) e ajuste dinâmico de dificuldade, pendentes do brief anterior.
4. **Revisitar `adp.dt.learning-digital-twin` em 2027**: é a área mais jovem e instável da literatura; uma nova busca em 12-18 meses pode revelar implementações que hoje não existem.
5. **Conversão para grafo.** Com ids, relações tipadas e termos no frontmatter, um script pode gerar SKOS a partir dos arquivos; vale fazê-lo junto com o domínio `grafo-conhecimento-educacional`, que definirá o vocabulário — mesma recomendação já registrada no relatório do domínio `realtime-multiplayer`.
