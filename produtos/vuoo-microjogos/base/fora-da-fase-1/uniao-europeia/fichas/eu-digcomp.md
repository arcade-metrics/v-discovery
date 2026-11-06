# DigComp 2.2 e DigComp 3.0

```yaml
id: eu-digcomp
name: The Digital Competence Framework for Citizens
acronym: DigComp
jurisdiction: União Europeia
issuing_organization: Comissão Europeia, Joint Research Centre (JRC), com DG EMPL
reference_type: framework de competências (não normativo)
domain: [D2, D4, D5]
official_url: https://joint-research-centre.ec.europa.eu/digcomp/digcomp-framework_en
repository_url: https://data.jrc.ec.europa.eu/collection/id-00414 (coleção de dados DigComp 3.0; página não abriu nesta sessão)
version: "3.0 (vigente; 5ª edição, nov/2025); 2.2 (2022-03-17) ainda difundida"
publication_date: "2.2: 2022-03-17 (JRC128415); 3.0: novembro de 2025 (fontes secundárias e página JRC)"
last_updated: unknown
legal_status: framework de referência; sem força normativa
mandatory_scope: nenhum
education_levels: cidadãos em geral (inclui estudantes)
geographic_scope: UE (uso internacional amplo)
language: inglês + traduções
license: unknown
technical_formats: [PDF, planilha, "linked open data" (resultados de aprendizagem da 3.0)]
api_available: not_found
data_model_available: parcial (estrutura tabular)
ontology_available: "lista controlada 'Digital Competence Framework' na coleção Europass (SKOS)"
schemas_available: not_found
implementation_examples: EDC podem referenciar DigComp
related_standards: [eu-esco, eu-elm, eu-digcompedu, BNCC Computação (comparação a fazer)]
entities: CompetenceArea (5), Competence (21), ProficiencyLevel, LearningOutcome/Example
relationships: área contém competências; competência tem níveis e resultados
vocabularies: Digital Competence Framework (EU Vocabularies)
core_relevance: alta como caso de teste de C.CFW/C.CMP com níveis de proficiência
regional_adapter_relevance: alta (alinhamento de competência digital em qualquer jurisdição)
limitations: mudança de 8 para 4 níveis entre 2.2 e 3.0 quebra comparabilidade direta
open_questions: formato exato e licença do "linked open data" da 3.0
sources: [S-UE-10, S-UE-11, S-UE-12]
access_date: 2026-11-05
research_status: parcial
```

## Análise

**DigComp 3.0** (página JRC): 5 áreas, 21 competências, **4 níveis de proficiência** (Basic, Intermediate, Advanced, Highly advanced); resultados de aprendizagem em planilha e em "linked open data" [S-UE-10]. Fontes secundárias registram publicação em 11/11/2025, IA integrada ao longo do framework e consolidação dos 8 níveis anteriores em 4 [S-UE-12].

**DigComp 2.2** (2022): mesmas 5 áreas, 21 competências, "more than 250 new examples of knowledge, skills and attitudes" [S-UE-11]; **8 níveis** de proficiência (dado da 2.1/2.2 não confirmado na página consultada; [I] por conhecimento prévio).

Lista completa de áreas e competências da 3.0 em [terminologia.md](../terminologia.md#digcomp-30).

**Modelo implícito:** Área → Competência → Nível → Resultado/exemplo (conhecimento, habilidade, atitude). [I] Mapeia direto para C.CFW (framework versionado) + C.CMP (área e competência como itens hierárquicos) + um atributo de **escala de proficiência** que o Core provisório não tem como entidade própria.

**Lição [I]:** a mudança 8→4 níveis entre versões mostra que (1) o framework precisa de versão explícita, (2) alinhamentos entre versões são C.CAS com tipo de equivalência, (3) níveis pertencem ao framework, não ao item.
