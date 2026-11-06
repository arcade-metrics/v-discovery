# Ficha: Lei 12.764/2012 (Política Nacional de Proteção dos Direitos da Pessoa com TEA)

> Texto compilado lido no Planalto em 2026-11-05.

```yaml
id: br.lei-12764-tea
name: "Lei nº 12.764, de 27 de dezembro de 2012 (Lei Berenice Piana): Política Nacional de Proteção dos Direitos da Pessoa com Transtorno do Espectro Autista"
acronym: Lei 12.764/2012
jurisdiction: Brasil (federal)
issuing_organization: Congresso Nacional / Presidência
reference_type: lei (regulamentada pelo Decreto 8.368/2014)
domain: [D7, D8]
official_url: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12764.htm
repository_url: not_applicable
version: "compilada; alterações: Lei 13.977/2020 (CIPTEA, art. 3-A e art. 1 §3), Lei 15.131/2025 (art. 3 §§1 e 2), Lei 15.256/2025 (art. 2, IX)"
publication_date: 2012-12-28
last_updated: 2025
legal_status: em vigor
mandatory_scope: poder público; gestor escolar (art. 7)
education_levels: [todos]
geographic_scope: nacional
language: pt-BR
license: domínio público [I]
technical_formats: [HTML]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: [Decreto SP 67.634/2023 (PEIPTEA); Res. SEDUC-SP 129/2025]
related_standards: [br.lbi, br.aee-pneepei]
entities: [pessoa com TEA, acompanhante especializado, CIPTEA (carteira), relatório médico com CID (para a CIPTEA)]
relationships: [pessoa com TEA é pessoa com deficiência "para todos os efeitos legais" (art. 1 §2)]
vocabularies: [definição clínica em dois incisos (art. 1 §1, I e II)]
core_relevance: média
regional_adapter_relevance: alta
limitations: [definição é clínica; CIPTEA envolve dado de saúde (CID)]
open_questions: [Q-INC-03]
sources: [E-33]
access_date: 2026-11-05
research_status: verificado
```

## Pontos de dados [I salvo indicação]

- **Acompanhante especializado** em classe comum "em casos de necessidade comprovada" (art. 3 §1, redação da Lei 15.131/2025). "Comprovada" não diz por qual documento; a Port. MEC 421/2026 manda definir a necessidade de profissional de apoio **no estudo de caso** (art. 14). O adaptador registra a necessidade pelo estudo de caso, não pelo laudo.
- **CIPTEA** (art. 3-A): requerimento com "relatório médico" com CID; validade de 5 anos. É documento de identificação de saúde: a plataforma **não** deve coletá-la como requisito; se recebida, é dado sensível (LGPD art. 5 II).
- **Recusa de matrícula** de aluno com TEA ou deficiência: multa de 3 a 20 salários-mínimos ao gestor (art. 7). Regra de negócio para gestão de matrícula, não para dado.
- Lei estadual SP 17.669/2023 trata do prazo de validade do laudo de TEA (citada nos considerandos da Res. SEDUC 129/2025; não aberta).
