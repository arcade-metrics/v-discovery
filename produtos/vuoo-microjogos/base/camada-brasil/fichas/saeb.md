# Ficha: Saeb (Sistema de Avaliação da Educação Básica)

> Acesso: 2026-11-05. Documentos lidos (PDFs oficiais do Inep obtidos via WebFetch e convertidos para texto em diretório temporário; parte do texto tem fonte corrompida e só a estrutura e os números foram usados): Portaria Inep 435/2025 (cópia do DOU); *Escalas de proficiência do Saeb* (Inep, 2020; SHA-256 `9b45fbf0…`); *Escalas de proficiência do Saeb: 2º, 5º e 9º ano* (Inep, 2025; SHA-256 `395c808c…`); *Matrizes de referência de Língua Portuguesa/Linguagens – BNCC* (Inep, 2022; SHA-256 `93e38839…`); matrizes de LP e MT de 2001 (republicação Inep 2022).

```yaml
id: br.saeb
name: Sistema de Avaliação da Educação Básica
acronym: Saeb
jurisdiction: Brasil (federal; aplicação em parceria com estados, DF e municípios)
issuing_organization: Inep/MEC
reference_type: [programa de avaliação externa em larga escala, regulamento (portaria anual do Inep)]
domain: [D5, D2, D7]
official_url:
  - https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb/matrizes-e-escalas
  - https://download.inep.gov.br/saeb/escala_de_proficiencias_saeb_2025.pdf
  - https://download.inep.gov.br/publicacoes/institucionais/avaliacoes_e_exames_da_educacao_basica/escalas_de_proficiencia_do_saeb.pdf
  - https://download.inep.gov.br/educacao_basica/saeb/matriz-de-referencia-de-linguagens_BNCC.pdf
  - https://download.inep.gov.br/educacao_basica/saeb/matriz-de-referencia-de-lingua-portuguesa_2001.pdf
  - https://download.inep.gov.br/educacao_basica/saeb/matriz-de-referencia-de-matematica_2001.pdf
repository_url: not_found (microdados existem no portal do Inep; não inspecionados nesta sessão)
version: "Saeb 2025 (Portaria Inep 435, de 03/07/2025, DOU 07/07/2025)"
publication_date: 2025-07-07
last_updated: 2026-07 (metadados do PDF de escalas 2025; resultados do Saeb 2025 divulgados em ago/2026 segundo imprensa)
legal_status: regulamento federal (portaria do Inep com base no Decreto 9.432/2018 e Portaria MEC 458/2020)
mandatory_scope: escolas da população de referência (públicas: censitário em 5º e 9º EF e 3ª/4ª EM; amostral no 2º EF, EI, privadas e CN/CH)
education_levels: [EI (só questionários), EF 2º, 5º, 9º anos, EM 3ª e 4ª séries]
geographic_scope: nacional
language: pt-BR
license: "É permitida a reprodução total ou parcial desta publicação, desde que citada a fonte" (publicações do Inep)
technical_formats: [PDF; microdados CSV (não verificado)]
api_available: false
data_model_available: parcial (matriz → escala → nível; sem schema)
ontology_available: false
schemas_available: false
implementation_examples: [SARESP usa a mesma escala (ver saresp.md); Indicador Criança Alfabetizada usa ponto de corte na escala do 2º ano]
related_standards: [br.bncc, br.novo-ensino-medio, br.saresp, br.cnca, iop.asmt.qti (formato de item, não usado pelo Inep)]
entities: [instrumento (teste cognitivo, questionário), matriz de referência, tópico/tema, descritor (2001), eixo do conhecimento e eixo cognitivo (BNCC), habilidade da matriz, item (não divulgado), escala de proficiência, nível de proficiência, população-alvo, população de referência, resultado agregado, atendimento especializado]
relationships: [teste → matriz (versão 2001 ou BNCC); matriz → etapa × área; descritor/habilidade → tópico ou eixo; nível → intervalo da escala; nível → descrição cumulativa de habilidades; resultado → escola/rede/UF/país]
vocabularies: [níveis por etapa e área com intervalos (terminologia §4); eixos cognitivos Reconhecer, Analisar, Avaliar, Produzir; 7 dimensões de qualidade (Portaria 435 art. 3)]
core_relevance: alta: modelo de referência para C.ASM/C.ITM/C.RES com escala e níveis versionados
regional_adapter_relevance: alta
limitations: [itens não divulgados (art. 25); resultados só agregados (mín. 10 estudantes e 80% de participação por escola, art. 22); matrizes BNCC não citam códigos BNCC; duas famílias de matriz coexistem]
open_questions: [Q-AVA-01, Q-AVA-02, Q-AVA-03, Q-AVA-04]
sources: [E-12, E-18 a E-22]
access_date: 2026-11-05
research_status: verificado (portaria e documentos do Inep); microdados não inspecionados
```

## Análise técnica (§6.3)

### Instrumentos do Saeb 2025 (Portaria Inep 435/2025, arts. 9 a 11 e Anexo I)

| Etapa | Teste | Matriz | Formato |
|---|---|---|---|
| EI | não há teste | — | questionários de diretor e professor, amostral |
| 2º EF | LP e MT | alinhadas à BNCC | amostral, públicas e privadas |
| 5º e 9º EF | LP e MT | 2001 **e** alinhadas à BNCC | censitário nas públicas; amostral nas privadas |
| 5º e 9º EF | CN e CH | alinhadas à BNCC | amostral |
| 3ª e 4ª EM | LP e MT | 2001 | censitário nas públicas, "em consonância ao disposto no art. 30 da Resolução CNE/CEB nº 2" |

### Duas famílias de matriz

| | Matriz 2001 | Matriz alinhada à BNCC (Inep, 2022) |
|---|---|---|
| Organização | tópicos (LP, ex.: "I. Procedimentos de leitura") ou temas (MT) com **descritores** `D1`, `D2`… | **eixo do conhecimento** (ex.: Leitura, Análise linguística/semiótica, Produção textual) × **eixo cognitivo** (Reconhecer, Analisar, Avaliar, Produzir), com habilidades numeradas dentro da célula |
| Identificador | `D` + número, **por etapa e área**: `D1` do 5º ano LP ≠ `D1` do 9º ano MT | número local na célula; **sem código** global |
| Ligação com BNCC | nenhuma | nenhum código BNCC citado (0 ocorrências de `EF..` no texto da matriz de Linguagens) |
| 2º ano | — | lista simples de habilidades por eixo (ex.: "Ler palavras.", "Escrever texto.") |

Consequência [I]: o alinhamento item Saeb → habilidade BNCC **não é publicado**; qualquer mapeamento é curadoria e deve ser `aproximada` com proveniência própria.

### Escala e níveis

- Escala TRI única por área para 5º, 9º EF e 3ª EM, com níveis de **25 pontos**; o nível 0 de LP e MT do 5º ano é "Desempenho menor que 125"; o nível 1 é "maior ou igual a 125 e menor que 150" (Inep, 2020, Quadros 1 e 2). Tabela completa em [terminologia §4](../terminologia-curriculo-avaliacao-inclusao.md).
- Os níveis são **cumulativos** ("Além das habilidades anteriormente citadas, os estudantes provavelmente são capazes de…"), e alguns níveis existem sem itens ("O Saeb não utilizou itens que avaliam as habilidades deste nível").
- 2º ano (BNCC): escala com faixas também de 25 pontos, "Nível Abaixo de 1" < 650 até nível 8 (≥ 825) em LP e nível 9 (≥ 850) em MT (Inep, 2025). Isto é coerente com uma escala de outra métrica (centrada em 750) [I]; o documento não declara média e desvio no texto extraído.
- CN e CH de 5º e 9º (BNCC): "Nível Abaixo de 1" com cortes 175 (CN 5º) e 200 (CH 5º; CN e CH 9º), passos de 25 (Inep, 2025).
- Não foi localizada escala publicada para LP e MT de 5º e 9º **alinhada à BNCC**; os documentos listados na página "Matrizes e escalas" cobrem 2001 (LP/MT) e BNCC (2º ano; CN/CH). Ver Q-AVA-02.

### Regras de validação e publicação

- Resultado de escola só com ≥ 10 estudantes presentes e ≥ 80% de participação; município ≥ 10 e ≥ 50% (art. 22).
- Atendimento especializado depende do cadastro do aluno na Matrícula Inicial do Censo Escolar (art. 15 e 17, par. único); não há instrumento adaptado para quem só é identificado no agendamento (art. 16). Recursos: tempo adicional, sala extra, prova ampliada, braille e ledor no 9º ano (art. 17).
- Itens não divulgados de imediato (art. 25); recurso do diretor contra resultado preliminar (art. 26).

### Temporalidade

A escala de 2001 sustenta séries históricas; as matrizes BNCC introduzem nova métrica (2º ano) e a aplicação dupla em 2025 indica transição [I]. Um resultado do Saeb só é interpretável com (edição, etapa, área, matriz, escala) explícitos.
