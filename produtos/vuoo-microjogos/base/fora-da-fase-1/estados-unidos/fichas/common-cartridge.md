# Ficha: Common Cartridge

> Análise em conhecimento/interoperabilidade/tool-integration/common-cartridge.md (`iop.tool.common-cartridge`).

```yaml
id: us.common-cartridge
name: Common Cartridge
acronym: CC
jurisdiction: internacional (1EdTech)
issuing_organization: 1EdTech Consortium
reference_type: padrão voluntário (formato de pacote)
domain: [D6, D4]
official_url: https://www.1edtech.org/standards/common-cartridge
repository_url: unknown
version: 1.3 (conjunto mais recente de 2013; Thin CC 2015)
publication_date: 2013
last_updated: 2015 (Thin CC)
legal_status: voluntário
mandatory_scope: nenhum
education_levels: K-12, ensino superior
geographic_scope: internacional
language: inglês
license: unknown
technical_formats: ZIP + XML (Content Packaging), QTI, links LTI
api_available: não
data_model_available: parcial (manifesto)
ontology_available: not_found
schemas_available: sim (XSD)
implementation_examples: ver conhecimento
related_standards: [QTI, LTI, CASE (metadado de alinhamento)]
entities: [Cartridge/Manifest, Organization (árvore de conteúdo), Resource, WebLink, LTI link, QTI assessment]
relationships: árvore de itens → recursos
vocabularies: tipos de recurso
core_relevance: baixa — referência para importar/exportar C.ACT em lote
regional_adapter_relevance: baixa
limitations: padrão estável, sem evolução ativa
open_questions: []
sources: [conhecimento]
access_date: 2026-11-05
research_status: apontado (sem nova pesquisa)
```

## O que falta para o crosswalk

Nada essencial para o Core: CC é formato de transporte de C.ACT e C.ASM. Atenção a um falso amigo: o elemento "organization" do manifesto é **árvore de conteúdo**, não C.ORG [I].
