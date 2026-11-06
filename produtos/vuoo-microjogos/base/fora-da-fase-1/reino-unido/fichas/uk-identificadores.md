# Identificadores educacionais britânicos

```yaml
id: uk-identificadores
name: Identificadores de aluno, aprendiz, candidato, profissional e estabelecimento (UPN, ULN, UCI, SCN, TRN, URN, DfE number/LAESTAB, UKPRN)
acronym: UPN / ULN / UCI / SCN / TRN / URN / LAESTAB / UKPRN
jurisdiction: Inglaterra (UPN também País de Gales); Escócia (SCN); UK (ULN, UKPRN)
issuing_organization: DfE (UPN, URN via GIAS, TRN), LAs (atribuem UPN), Learning Records Service (ULN), UKRLP (UKPRN), organizações de exames (UCI), Scottish Government/SQA (SCN)
reference_type: esquemas de identificação definidos em dicionário de dados
domain: [D8, D1]
official_url: https://www.gov.uk/government/publications/common-basic-data-set-cbds-database
repository_url: n/a
version: CBDS May 2026; ScotXed School and Pupils Data Spec 2026 v4.0
publication_date: n/a
last_updated: 2026-05-11 (CBDS)
legal_status: exigidos nas coletas estatutárias
mandatory_scope: escolas que enviam censos
education_levels: escolar; ULN e UKPRN atravessam para FE/superior
geographic_scope: ver por identificador
language: inglês
license: n/a
technical_formats: strings/inteiros com dígito verificador
api_available: GIAS (consulta de estabelecimentos) [I: API não verificada]
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [uk-eng-cbds, uk-sco-cfe-census]
entities: n/a
relationships: n/a
vocabularies: n/a
core_relevance: muito alta (desenho de C.IDN)
regional_adapter_relevance: muito alta
limitations: identificador do aluno muda entre jurisdições do UK (UPN × SCN) e entre fases (UPN escolar × ULN ≥14)
open_questions: identificador de aluno na Irlanda do Norte não encontrado
sources: [S-UK-02, S-UK-09, S-UK-06]
access_date: 2026-11-05
research_status: verificado (Inglaterra e Escócia)
```

## Tabela

| Id | Identifica | Formato | Verificação | Quem atribui / onde vale | Fonte |
|---|---|---|---|---|---|
| UPN | aluno em escola mantida | 13 car.: letra verificadora + 3 dígitos de LA + 9; temporário termina em letra | letra: pesos 2..13, mód. 23, letras sem I/O/S | Inglaterra e País de Gales; "for use in the educational context during a child's school career only" | CBDS N00001 |
| Former UPN | UPN anterior (ex.: temporário) | igual | igual | | N00002 |
| ULN | aprendiz (vida toda, 14+) | 10 dígitos, 1º ≠ 0 | dígito verificador mód. 11 | Learning Records Service; obrigatório no censo a partir de 14 anos | N00011; School Census |
| UCI | candidato a exame externo | 13 car. (`999999999999A` ou `99999B999999A`) | termina em letra; algoritmo not_found | organizações de exames | N00180 |
| TRN (Teacher Number) | professor | 7 dígitos | n/a | DfE (antigo número GTC) | N00539 |
| URN | estabelecimento | 6 dígitos | n/a | GIAS (antigo Edubase); sequencial | N00278, N00211 |
| LA number | autoridade local | 3 dígitos | CS003 | DfE/ONS | N00216 |
| DfE Establishment Number | escola dentro da LA | 4 dígitos (0000–9999, XXXX, MMMM, LLLL) | n/a | DfE | N00279 |
| LAESTAB / "DfE number" | escola | LA (3) + Estab (4) = 7 dígitos, exibido "NNN/NNNN" | n/a | GIAS | busca GIAS/API de estatísticas |
| UKPRN | provedor de aprendizagem | 8 dígitos (10000000–99999999) | n/a | UK Register of Learning Providers | N00530 |
| UPRN | imóvel/endereço | até 12 dígitos | n/a | registro de endereços | N00185 |
| Ofsted EY URN | provedor de educação infantil | `AA999999` ou numérico | n/a | Ofsted | N00253 |
| SCN | aluno na Escócia | 9 dígitos | dígito verificador mód. 11 (pesos 3,2,7,6,5,4,3,2); único por aluno | Escócia (ScotXed) | Data Spec 2026 §3.1.4.24, §3.2.3.6 |

## Lições para o Core [I]

1. **Um aluno, vários identificadores simultâneos e sucessivos**: UPN (escolar), ULN (a partir de 14, vitalício), UCI (exames), Former UPN (histórico). C.IDN deve ser 1..n por pessoa, com `scheme`, `valid_from/to`, `issuer` e `status` (temporário/definitivo).
2. **Escola com dois identificadores e um composto**: URN (estável, nacional) e LAESTAB (LA + número local, muda se a escola muda de LA ou de tipo). C.IDN precisa suportar identificador **composto** e a regra de que o identificador estável é o preferido para chaves.
3. **Validação por esquema**: dígitos/letras verificadoras diferentes por esquema; o Core guarda o `scheme` e delega a validação ao adaptador.
4. **Finalidade restrita**: UPN só no contexto educacional. C.IDN deve carregar `permitted_use`, para que exportações não vazem o identificador para fins não educacionais.
5. **Jurisdição dentro do país**: o mesmo aluno que se muda da Escócia para a Inglaterra troca SCN por UPN. Identidade não pode depender de um único esquema nacional.
