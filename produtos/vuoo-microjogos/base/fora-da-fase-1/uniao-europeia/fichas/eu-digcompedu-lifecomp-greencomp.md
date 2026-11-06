# DigCompEdu, LifeComp e GreenComp

Três frameworks do JRC agrupados numa ficha porque têm a mesma natureza (framework conceitual não normativo, sem modelo de dados) e o mesmo papel para o Core (instâncias de C.CFW). Cada um tem seu bloco YAML.

## DigCompEdu

```yaml
id: eu-digcompedu
name: European Framework for the Digital Competence of Educators
acronym: DigCompEdu
jurisdiction: União Europeia
issuing_organization: Comissão Europeia, JRC
reference_type: framework de competências docentes
domain: [D1 (perfil do profissional), D2]
official_url: https://joint-research-centre.ec.europa.eu/digcompedu_en
repository_url: not_found
version: "2017 (JRC107466); atualização lançada em maio de 2026, versão final prevista para a primavera de 2027"
publication_date: 2017 [I: ano do relatório JRC107466]
last_updated: 2026 (processo de atualização em curso)
legal_status: framework de referência
mandatory_scope: nenhum
education_levels: educadores de todos os níveis
geographic_scope: UE
language: inglês + traduções
license: unknown
technical_formats: [PDF]
api_available: not_found
data_model_available: não
ontology_available: not_found
schemas_available: not_found
implementation_examples: not_found
related_standards: [eu-digcomp]
entities: Area (6), Competence (22), ProficiencyLevel
relationships: área contém competências
vocabularies: not_found como lista controlada
core_relevance: baixa (competência de profissional, não de aprendiz)
regional_adapter_relevance: baixa
limitations: só PDF; em revisão
open_questions: nomes e número de níveis (A1–C2, [I]) não confirmados na página
sources: [S-UE-13]
access_date: 2026-11-05
research_status: parcial
```

Seis áreas, 22 competências: Professional engagement; Digital resources; Teaching and learning; Assessment; Empowering learners; Facilitating learners' digital competence [S-UE-13]. Atualização iniciada em maio de 2026 [S-UE-13].

## LifeComp

```yaml
id: eu-lifecomp
name: The European Framework for Personal, Social and Learning to Learn Key Competence
acronym: LifeComp
jurisdiction: União Europeia
issuing_organization: Comissão Europeia, JRC
reference_type: framework conceitual de competências (não prescritivo)
domain: [D2, D4]
official_url: https://joint-research-centre.ec.europa.eu/lifecomp_en
repository_url: not_found
version: 2020 (JRC120911)
publication_date: 2020 [I: ano do relatório]
last_updated: unknown
legal_status: framework de referência; desdobra a Recomendação do Conselho de maio de 2018 sobre competências-chave
mandatory_scope: nenhum
education_levels: todos
geographic_scope: UE
language: inglês
license: unknown
technical_formats: [PDF]
api_available: not_found
data_model_available: não
ontology_available: "indireto: lista 'Key competences for lifelong learning' na coleção Europass"
schemas_available: not_found
implementation_examples: not_found
related_standards: [Key Competences 2018, eu-greencomp]
entities: Area (3), Competence (9, códigos P1–L3), Descriptor
relationships: área contém competências
vocabularies: códigos P1..P3, S1..S3, L1..L3
core_relevance: média: competências socioemocionais próximas das competências gerais da BNCC
regional_adapter_relevance: média
limitations: sem níveis de proficiência ("non-prescriptive")
open_questions: número de descritores por competência não confirmado
sources: [S-UE-14, S-UE-15]
access_date: 2026-11-05
research_status: verificado (estrutura)
```

Três áreas (Personal, Social, Learning to learn) e nove competências codificadas: P1 Self-regulation, P2 Flexibility, P3 Wellbeing, S1 Empathy, S2 Communication, S3 Collaboration, L1 Growth mindset, L2 Critical thinking, L3 Managing learning; framework "non-prescriptive", sem escala de níveis [S-UE-15].

## GreenComp

```yaml
id: eu-greencomp
name: The European Sustainability Competence Framework
acronym: GreenComp
jurisdiction: União Europeia
issuing_organization: Comissão Europeia, JRC
reference_type: framework conceitual de competências
domain: [D2, D4]
official_url: https://joint-research-centre.ec.europa.eu/greencomp-european-sustainability-competence-framework_en
repository_url: not_found
version: 2022 (JRC128040)
publication_date: 2022 [I: ano do relatório]
last_updated: unknown
legal_status: framework de referência
mandatory_scope: nenhum
education_levels: todos
geographic_scope: UE
language: inglês + traduções
license: unknown
technical_formats: [PDF]
api_available: not_found
data_model_available: não
ontology_available: not_found
schemas_available: not_found
implementation_examples: not_found
related_standards: [eu-lifecomp]
entities: Area (4), Competence (12)
relationships: área contém 3 competências interligadas
vocabularies: not_found como lista controlada
core_relevance: média (tema transversal; teste de C.CMP sem níveis)
regional_adapter_relevance: média
limitations: sem níveis de proficiência definidos
open_questions: existência de versão legível por máquina
sources: [S-UE-16, S-UE-17]
access_date: 2026-11-05
research_status: verificado (estrutura)
```

Quatro áreas e doze competências: Embodying sustainability values (Valuing sustainability, Supporting fairness, Promoting nature); Embracing complexity in sustainability (Systems thinking, Critical thinking, Problem framing); Envisioning sustainable futures (Futures literacy, Adaptability, Exploratory thinking); Acting for sustainability (Political agency, Collective action, Individual initiative). A página não define escala de proficiência e diz que não se espera o nível máximo em todas [S-UE-17].

## Lição comum [I]

Os três frameworks são **árvores rasas (área → competência) sem identificadores persistentes publicados** (exceto os códigos P1–L3 do LifeComp) e quase sem dado legível por máquina. Um adaptador precisaria cunhar URIs próprios e registrar a proveniência (C.PRV). O Core deve aceitar C.CFW **com ou sem** escala de níveis.
