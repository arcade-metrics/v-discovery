# Ficha: Diretrizes Curriculares Nacionais (DCN) da educação básica

> Ficha guarda-chuva para as DCN que afetam currículo e inclusão. A LDB como organização (etapas, modalidades, matrícula) pertence à frente de organização. Acesso: 2026-11-05.

```yaml
id: br.dcn
name: Diretrizes Curriculares Nacionais da Educação Básica (gerais, por etapa e da educação especial/AEE)
acronym: DCN / DCNEB / DCNEM
jurisdiction: Brasil (federal)
issuing_organization: Conselho Nacional de Educação, Câmara de Educação Básica (resoluções homologadas pelo MEC)
reference_type: norma (resolução do CNE)
domain: [D4, D2, D5, D7]
official_url:
  - https://www.gov.br/mec/pt-br/cne/pdf/cne-divulgacao/cne_sintese_das_diretrizes_curriculares_da_educacao_basica.pdf (síntese oficial do CNE)
  - DCN gerais: Res. CNE/CEB 4/2010 (texto oficial não aberto; cópia de terceiros localizada)
  - DCNEM vigente: Res. CNE/CEB 2/2024, ver novo-ensino-medio.md
  - AEE: Res. CNE/CEB 4/2009, ver conhecimento/acessibilidade-educacao-especial-e-dua/brazil/pneepei-and-aee.md
repository_url: not_found
version: "Res. CNE/CEB 4/2010 (13/07/2010, DOU 14/07/2010); Res. CNE/CEB 2/2024 (DCNEM); Res. CNE/CEB 4/2009 (AEE, 02/10/2009)"
publication_date: 2010-07-14 (DCN gerais)
last_updated: unknown (alterações posteriores da Res. 4/2010 não verificadas)
legal_status: em vigor (DCN gerais e AEE: sem revogação expressa localizada; DCNEM 2018 revogada pela 2/2024 com regime de transição)
mandatory_scope: sistemas de ensino e escolas (as DCN orientam a elaboração dos currículos)
education_levels: [EI, EF, EM, modalidades]
geographic_scope: nacional
language: pt-BR
license: domínio público [I]
technical_formats: [PDF]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: not_found
related_standards: [br.bncc, br.novo-ensino-medio, br.aee-pneepei]
entities: [base nacional comum, parte diversificada, etapa, modalidade, área do conhecimento, componente curricular, projeto político-pedagógico, avaliação da aprendizagem, avaliação institucional, avaliação de redes; AEE, sala de recursos multifuncionais, plano de AEE (Res. 4/2009)]
relationships: [currículo da escola = base nacional comum + parte diversificada; PPP institucionaliza o AEE (Res. 4/2009 art. 10)]
vocabularies: [definições conceituais (ex.: "currículo", "área de conhecimento" na DCNEM 2024 art. 5)]
core_relevance: média: fixam a **camada** "parte diversificada" e a tríade de avaliação (aprendizagem, institucional, redes), mas não dão estrutura de dado
regional_adapter_relevance: média
limitations: [texto oficial da Res. 4/2010 e as DCN de EI (Res. 5/2009) e EF de 9 anos (Res. 7/2010) não abertos nesta sessão]
open_questions: [Q-CUR-07, Q-INC-06]
sources: [E-13, E-14, E-07]
access_date: 2026-11-05
research_status: parcial (DCNEM verificada; DCN gerais por síntese oficial e cópia secundária; DCN EI e EF não verificadas)
```

## O que interessa ao modelo de dados [I]

1. **Base comum + parte diversificada**: um currículo de rede ou escola é a composição de itens de um C.CFW nacional (BNCC) com itens próprios. O Core precisa de composição de frameworks com proveniência por item, e não de cópia.
2. **Definições oficiais de "currículo" e "área do conhecimento"** existem na DCNEM 2024 (art. 5, V e VI): "área de conhecimento: agrupamento de componentes curriculares com afinidade de matrizes epistemológicas…". Servem de `skos:definition` no adaptador.
3. **Três níveis de avaliação** (aprendizagem, institucional, redes) separam C.RES do estudante de indicadores agregados (Saeb, Ideb). O Core deve guardar resultado individual e agregado como entidades diferentes.
4. Res. CNE/CEB 4/2009 segue citada como vigente pelas redes (a Res. SEDUC-SP 129/2025 a invoca nos considerandos), apesar de regulamentar decreto revogado; ver acs.br.pneepei-and-aee.
