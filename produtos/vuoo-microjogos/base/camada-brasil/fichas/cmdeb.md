# Ficha: CMDEB – Conjunto Mínimo de Dados da Educação Básica

Ficha curta. A transcrição completa (156 variáveis, domínios de código, ocorrência e categoria) está em [../cmdeb/](../cmdeb/README.md) e não é repetida aqui. Plataforma e API: [mec-gestao-presente.md](mec-gestao-presente.md).

```yaml
id: br.mec.cmdeb
name: Conjunto Mínimo de Dados da Educação Básica
acronym: CMDEB
jurisdiction: Brasil (federal)
issuing_organization: Ministério da Educação (SEB/MEC)
reference_type: modelo de informação instituído por portaria (Anexo da Portaria MEC 832/2025, que altera a Portaria MEC 234/2025)
domain: [D1, D3, D7, D8]
official_url: https://mecnormas.mec.gov.br/pesquisa/detalhar/8017
repository_url: ../cmdeb/
version: "Portaria MEC 832, de 16/12/2025 (DOU 17/12/2025)"
publication_date: 2025-12-17
last_updated: 2025-12-17 (Anexo atualizável por ato do Ministro, art. 14 §4º)
legal_status: "vigente; conteúdo mínimo e tipos de dado definidos no art. 13; transmissão preferencialmente por API (art. 14 §1º); coleta gradual (art. 14 §3º)"
mandatory_scope: "dados de referência e de registro são 'obrigatórios' (art. 13 §3º) no âmbito do MEC Gestão Presente; alcance sobre redes não aderentes: ver Q-11"
education_levels: [educação básica]
geographic_scope: nacional
language: pt-BR
license: domínio público (ato normativo)
technical_formats: [tabela no Anexo; implementado em JSON pela API CMDEB v2]
api_available: sim (API CMDEB v2, ver mec-gestao-presente.md)
data_model_available: sim
ontology_available: não
schemas_available: "OpenAPI 3.1 da API v2 (E36)"
implementation_examples: Swagger da API v2
related_standards: [br.mec.gestao-presente, br.inep.censo-escolar, br.mec.educadados]
entities: [Estudante, Responsável, Matrícula, Turma, Componente curricular, Frequência (componente e turma), Avaliação de desempenho, Profissional, Formação, Vínculo com a rede, Alocação em turma/componente, Instituição de ensino]
relationships: ver ../modelo-de-dados.md §3.1
vocabularies: "domínios inline (cmdeb/10 a 40); diferenças com o Censo em ../terminologia.md"
core_relevance: alta
regional_adapter_relevance: muito alta
limitations: "inconsistências internas (CO_ENTIDADE com 8 ou 11 dígitos; NOME_TURMA numérico no bloco 2.1); divergências com a API v2; códigos diferentes do Censo para o mesmo conceito"
open_questions: [Q-06, Q-11, Q-12]
sources: [E31, E36]
access_date: 2026-11-05
research_status: completo (transcrição prévia em ../cmdeb/; análise complementar nesta frente)
```

Achados novos desta frente sobre o CMDEB: divergências Portaria × API v2 em [../modelo-de-dados.md](../modelo-de-dados.md) §3.3; tabelas de correspondência CMDEB × Censo em [../terminologia.md](../terminologia.md) §2–9.
