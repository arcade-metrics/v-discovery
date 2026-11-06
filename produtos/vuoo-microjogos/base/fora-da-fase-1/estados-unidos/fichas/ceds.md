# Ficha: CEDS — Common Education Data Standards

> Análise conceitual em conhecimento/interoperabilidade/rostering/ceds.md (`iop.ros.ceds`). Aqui: versão, componentes e organização de elementos/opções.

```yaml
id: us.ceds
name: Common Education Data Standards
acronym: CEDS
jurisdiction: Estados Unidos
issuing_organization: National Center for Education Statistics (NCES), U.S. Department of Education, com CEDS Stakeholder Group
reference_type: vocabulário / dicionário de dados (com modelo de referência IDS e ontologia)
domain: [D1, D3, D5, D7, D8]   # P-20W segundo literatura; ver open_questions
official_url: https://ceds.ed.gov/
repository_url: https://github.com/CEDStandards/CEDS-Elements
version: 14.0.0.0 (arquivo de elementos no repositório) [E17]
publication_date: unknown (release anual, tipicamente jan/fev) [E17]
last_updated: unknown
legal_status: voluntário [conhecimento: nces2026ceds]
mandatory_scope: nenhum
education_levels: educação infantil a força de trabalho (declarado na literatura; não confirmado em fonte primária)
geographic_scope: EUA
language: inglês
license: Apache-2.0 (repositório CEDS-Elements) [E17]
technical_formats: planilha (xlsx), banco relacional (IDS), ontologia (formato não confirmado)
api_available: não
data_model_available: sim (Integrated Data Store, IDS; Domain Entity Schema)
ontology_available: sim, "CEDS Ontology" com versionamento alinhado [E17]; serialização não verificada
schemas_available: sim (scripts IDS; não inspecionados)
implementation_examples: CCSS publica XML "following the CEDS schema" [E19]
related_standards: [Ed-Fi (alinhado), CCSS (XML em esquema CEDS)]
entities: Domain Entity Schema = domínio → entidade → categoria → propriedade (elemento) [E16]; mais de 70 entidades (trecho, E18)
relationships: elemento ↔ option set; elemento ↔ entidade
vocabularies: option sets (valores com definição) por elemento [E17]
core_relevance: média — referência de método (elemento definido + opção definida + versão anual), não de conteúdo
regional_adapter_relevance: média (camada semântica para mapear Ed-Fi/OneRoster de um mesmo cliente EUA)
limitations: vocabulário dos EUA; sem transporte; lista de domínios não legível no portal (carregada por script)
open_questions: Q06
sources: [E15, E16, E17, E18, E19]
access_date: 2026-11-05
research_status: parcial — versão e organização verificadas no repositório; domínios não listados
```

## Acréscimos

- **Organização do vocabulário.** O repositório contém "standard element names, definitions, and option sets", com as opções tendo definição própria, e entidades com definição [E17]. Mudanças exigem caso de uso submetido em GitHub Issues [E17].
- **Hierarquia.** "Domain Entity Schema (DES) provides a hierarchy of domains, entities, categories, and properties" [E16]. Propriedades em "Extend" não foram adotadas pela comunidade [E16].
- **Versionamento.** Release oficial anual; entre releases, números incrementais; a release anual realinha todos os recursos (elementos, IDS, ontologia) a uma versão comum [E17].
- **Lição [I]:** separar definição do elemento, conjunto de opções e versão do conjunto é exatamente o que C.VOC precisa; o CEDS mostra o ciclo de governança (caso de uso → issue → release anual).
