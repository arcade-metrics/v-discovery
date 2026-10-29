---
id: lae.relatorio
titulo: Relatório da primeira versão do domínio learning analytics, mineração de dados e avaliação
tipo: relatorio
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Relatório: primeira versão do domínio learning analytics, mineração de dados e avaliação

Data: 2026-10-29. Esta é a "primeira versão funcional" pedida por `_modelo/metodo-e-qualidade.md`: estrutura, mapa conceitual, bibliografia inicial e os documentos principais fundamentados em fontes verificadas. Todos os documentos estão em `status: rascunho`; a passagem para `revisado` exige o checklist de `_modelo/checklist-revisao.md` por leitor humano.

## Método aplicado

Seis frentes de pesquisa em paralelo, uma por subpasta prevista no brief (`foundations`, `data-quality`, `indicators`, `assessment-design`, `psychometrics`, `evaluation-methods`), cada uma restrita a abrir as fontes antes de citá-las e a confirmar, lendo o frontmatter real, qualquer id de outro domínio (`aprendizagem-adaptativa`, `interoperabilidade`) citado em relação. Cada frente produziu seus documentos e um fragmento de bibliografia e índice; os fragmentos foram mesclados em `referencias/bibliografia.bib` e `referencias/indice-fontes.md` por `_modelo/mesclar_referencias.py`. O validador `_modelo/validar.py`, rodado sobre a base inteira, confirmou: ids únicos com prefixo `lae` correto, todos os alvos de relação existentes (inclusive os cross-domain), todas as chaves de fonte presentes na bibliografia, nenhuma menção a produto consumidor — 0 avisos, 0 erros.

## Cobertura

| Área | Documentos | Observação |
|---|---|---|
| foundations | 2 | LA vs. EDM (origens, LAK/SoLAR, IEDMS) e o ciclo de learning analytics (reference model, níveis micro/meso/macro) |
| data-quality | 2 | proveniência e linhagem (PROV-O como referência), vieses e validade de trace data |
| indicators | 3 | engajamento (Fredricks, Blumenfeld & Paris), predição de risco/evasão (Course Signals como caso histórico), dashboards e relação com open learner model |
| assessment-design | 2 | avaliação formativa/somativa/diagnóstica (Scriven, Black & Wiliam, Hattie & Timperley), alinhamento construtivo (Biggs, Bloom revisada, SOLO) |
| psychometrics | 3 | teoria clássica dos testes, confiabilidade e validade, equidade de medição (DIF) |
| evaluation-methods | 2 | desenho experimental e quase-experimental, tamanho de efeito e crise de replicação |
| raiz | 7 | brief, README, glossário, mapa, matriz comparativa, plano de ids, este relatório |

Totais: 14 documentos conceituais (16 contando brief e plano de ids), 34 relações tipadas registradas no mapa de conceitos (20 `relacionado-a`, 7 `depende-de`, 4 `complementa`, 2 `alternativa-a`, 1 `avaliado-por`), 71 chaves de fonte citadas no frontmatter dos documentos (69 entradas nos seis fragmentos de bibliografia, com pequena sobreposição intencional de chaves reaproveitadas de outros domínios: `baker2022bias`, `gardner2019slicing`, `bloom1968mastery`, `gasevic2015notforget`).

Marcas de afirmação no corpo dos documentos: 361 citações de fato com chave de fonte (`[F: ...]`), 184 interpretações marcadas `[I]`, 3 hipóteses marcadas `[H]`.

## O que o brief pediu e onde está

| Entregável | Local |
|---|---|
| Estrutura de diretórios | `learning-analytics-e-avaliacao/` (6 pastas temáticas, mais `_plano-ids.md`) |
| README com escopo, organização e convenções | `README.md` deste domínio e `conhecimento/README.md` |
| Glossário técnico | `glossario.md` |
| Mapa conceitual e relações entre documentos | `mapa-conceitos.md` |
| Documentos técnicos fundamentados em fontes primárias | as 6 pastas temáticas |
| Bibliografia BibTeX | fragmentos mesclados em `conhecimento/referencias/bibliografia.bib` |
| Matriz comparativa das dicotomias centrais | `matriz-comparativa.md` |
| Relatório de cobertura e prioridades | este arquivo |

## Fontes que não puderam ser verificadas em texto integral

Padrão recorrente: bibliotecas pagas (ACM, IEEE, Springer, Elsevier, Taylor & Francis) e proteção anti-bot (Cloudflare) bloquearam acesso automatizado em boa parte das tentativas. Consequências registradas, por área:

- **foundations**: Clow 2012 (base do ciclo de 4 elementos) bloqueado em todas as tentativas; reconstruído via slide deck do autor e citações em Chatti et al. 2014, sem conferência palavra por palavra. O rótulo "Capture, Report, Predict, Act, Refine" atribuído a Campbell & Oblinger 2007 não foi encontrado literalmente no texto integral consultado desse artigo — marcado "não verificado". Siemens & Long 2011 retornou 403; a distinção academic analytics vs. LA atribuída a esse artigo ficou como `[I]`, não `[F]`.
- **data-quality**: paginação de Slade & Prinsloo 2013 diverge entre repositórios; lista de autores de Fincham et al. 2019 diverge entre o registro institucional e os slides dos próprios autores — ambas as divergências sinalizadas no texto. Viés de amostragem por acesso a dispositivo especificamente em contexto de LA (não em dados de sensor em geral) não tem fonte dedicada localizada; registrado como inferência.
- **indicators**: artigo acadêmico original do Course Signals (LAK12) não acessado em texto integral — números de retenção vêm de fonte secundária (EDUCAUSE Review), e a crítica de causalidade reversa vem de fonte técnica especializada, não de réplica revisada por pares. Nenhuma medição empírica direta de "profecia autorrealizável" em sistemas de alerta precoce foi localizada — tratado como hipótese `[H]`. Henrie 2015, Arnold & Pistilli 2012, Schwendimann 2017, Jivet 2017/2018, Bennett & Folley 2018 e Pozdniakov et al. 2024 citados só por resumo/metadados.
- **assessment-design**: artigo completo de Black & Wiliam 1998 (*Assessment in Education*) ficou atrás de paywall; coberto pelo artigo-irmão mais curto (PDK) com os mesmos achados. Avaliação diagnóstica como categoria própria não tem fonte acadêmica primária localizada. Livros de Biggs 1996 (original), Anderson & Krathwohl 2001 e Biggs & Collis 1982 não foram abertos em texto integral, só verificados via fontes secundárias que os citam extensamente.
- **psychometrics**: textos centrais (Crocker & Algina 1986, Cronbach 1951, Sijtsma 2009, Standards AERA/APA/NCME 2014, módulo NCME de Hambleton & Jones) sem acesso aberto ou com falha técnica de extração; atribuições feitas via fontes secundárias acadêmicas convergentes, com ressalva registrada em cada documento. Nenhum review acadêmico primário de acesso aberto sobre DIF foi localizado; usado verbete de enciclopédia como fonte secundária, registrado como lacuna para substituição futura.
- **evaluation-methods**: Shadish, Cook & Campbell 2002 acessado só por metadados de catálogo. Críticas secundárias a Hattie sobre erros de cálculo (Higgins & Simpson 2011, Topphol 2011, Bergeron & Rivard 2017) só apareceram em fontes não acadêmicas, marcadas "não verificado". Sem DOI confirmado para Glass 1976. Taxa de replicação específica de estudos de eficácia de produtos educacionais digitais não encontrada; extrapolada da crise de replicação em psicologia geral, registrada como inferência.

Todas essas situações estão marcadas no documento correspondente e na nota da entrada BibTeX, quando aplicável.

## Lacunas de conhecimento e questões abertas

As perguntas abertas do brief original têm resposta parcial ao longo dos documentos; nenhuma foi fechada por completo.

1. **Fronteira entre indicador de LA e modelo preditivo de `aprendizagem-adaptativa`.** Permanece uma questão de ênfase e não de critério objetivo — registrado em `lae.found.la-vs-edm` como sobreposição ampla entre as duas tradições.
2. **Garantias de qualidade de dado antes de expor um indicador em dashboard.** `lae.dq.provenance-and-lineage` e `lae.dq.bias-and-validity` descrevem os riscos, mas não há um checklist operacional consolidado na literatura consultada — oportunidade para síntese própria numa revisão futura.
3. **Validação de instrumentos de avaliação formativa de baixo custo sem infraestrutura de TRI completa.** `lae.psy.classical-test-theory` documenta por que a CTT é usada nesse cenário, mas não há orientação quantitativa sobre o tamanho mínimo de amostra aceitável.
4. **Desenho de avaliação de resultado viável dentro do ciclo de produto.** `lae.evalm.experimental-design` cobre A/B testing como RCT em miniatura, mas a literatura específica de ritmo de produto (vs. ritmo de pesquisa acadêmica) é escassa nas fontes abertas encontradas.
5. **Área de evidence-centered design e stealth assessment não coberta.** Mencionada apenas de passagem no brief de outros domínios; não há documento próprio nesta versão.
6. **Avaliação diagnóstica como terceira categoria.** Sem fonte acadêmica primária dedicada localizada (ver `lae.asmt.formative-and-summative`).

## Próximos passos sugeridos

1. **Revisão humana** dos 14 documentos com o checklist, começando pelos que concentram citações de fonte bloqueada (`lae.found.analytics-cycle`, `lae.evalm.effect-size-and-replication`, `lae.psy.reliability-and-validity`).
2. **Segunda rodada de fontes bloqueadas** com acesso institucional (ACM, IEEE, Springer, Taylor & Francis) para fechar as lacunas de Clow 2012, Shadish/Cook/Campbell 2002, Crocker & Algina 1986 e Black & Wiliam 1998 em texto integral.
3. **Cobrir evidence-centered design e stealth assessment**, e aprofundar avaliação diagnóstica como categoria própria.
4. **Síntese própria de boas práticas de qualidade de dado para dashboard**, já que a literatura trata os riscos separadamente sem um checklist consolidado.
5. **Conversão para grafo.** Com ids, relações tipadas e termos no frontmatter, um script pode gerar SKOS a partir dos arquivos, junto com o domínio `grafo-conhecimento-educacional` — mesma recomendação já registrada nos relatórios de `realtime-multiplayer` e `aprendizagem-adaptativa`.
