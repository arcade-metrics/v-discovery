# Ficha: BNCC Computação (Complemento à BNCC)

> Ficha **curta**: transcrição completa em [../bncc-computacao/](../bncc-computacao/README.md) (141 registros, com explicação e exemplos). Acesso: 2026-11-05.

```yaml
id: br.bncc-computacao
name: "Computação na Educação Básica: Complemento à BNCC"
acronym: BNCC Computação
jurisdiction: Brasil (federal)
issuing_organization: CNE/CEB (Parecer CNE/CEB 2/2022; Resolução CNE/CEB 1/2022); MEC
reference_type: norma (complemento curricular normativo)
domain: [D2, D4]
official_url: https://www.gov.br/mec/ (arquivo do portal não comparado; ver ../bncc-computacao/README.md, decisão 12)
repository_url: not_found (oficial)
version: "versão diagramada de 13/04/2022 (SHA-256 60aab0b1…)"
publication_date: 2022-10-04 (Res. CNE/CEB 1/2022, DOU 06/10/2022)
last_updated: unknown
legal_status: norma em vigor desde 01/11/2022 (Res. CNE/CEB 1/2022, art. 6, segundo cópia ABMES; texto integral não aberto nesta sessão)
mandatory_scope: unknown no detalhe (prazo de implementação não conferido no texto oficial; fonte secundária fala em 1 ano)
education_levels: [EI, EF, EM]
geographic_scope: nacional
language: pt-BR
license: unknown
technical_formats: [PDF]
api_available: false
data_model_available: false (oficial); sim em bncc-dados
ontology_available: false
schemas_available: false
implementation_examples: [../bncc-computacao/]
related_standards: [br.bncc, br.novo-ensino-medio (DCNEM 2024 art. 17 §4 torna a educação digital obrigatória no EM)]
entities: [eixo (Pensamento Computacional, Mundo Digital, Cultura Digital), objeto de conhecimento (com 2º nível nos anos finais), habilidade, competência específica (EF e EM), premissa (EI), explicação, exemplo de atividade]
relationships: [habilidade → eixo, habilidade → objeto (hierárquico), habilidade EM → competência]
vocabularies: ["códigos EI03CO01, EF01CO01, EF15CO01, EF69CO01, EM13CO01"]
core_relevance: média-alta: segundo documento no mesmo C.CFW prova o modelo multi-documento; traz "exemplos de atividade" que mapeiam para C.ACT
regional_adapter_relevance: alta
limitations: [sem alinhamento oficial entre faixas; códigos EM sem competência no código (diferente das áreas da BNCC EM)]
open_questions: [Q-CUR-04]
sources: [E-05, E-06]
access_date: 2026-11-05
research_status: verificado (transcrição); ato normativo conferido só por cópia de terceiros
```

## Análise técnica: o que acrescenta à BNCC

- **Mesmo esquema de código, outra semântica**: `EM13CO26` tem sequência contínua, sem centena de competência, ao contrário de `EM13LGG103`. Um decodificador único precisa de regra por documento [F: ../bncc-pacotes/02-api-e-modelo.md].
- **Objeto de conhecimento com dois níveis** nos anos finais e **enunciado geral sem código** [F: ../bncc-computacao/README.md]. O Core precisa aceitar `C.CMP` sem `notation`.
- **Conteúdo de experiência** (explicação e exemplos plugados/desplugados) é texto normativo anexo à habilidade: candidato a `C.ACT` com proveniência normativa, não curadoria [I].
- A Resolução CNE/CEB 2/2025, citada por redes municipais como exigência de informar se os referenciais contemplam Computação, **não foi aberta** (ver Q-CUR-04).
