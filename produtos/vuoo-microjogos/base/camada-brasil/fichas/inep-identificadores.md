# Ficha: Identificadores educacionais no Brasil (INEP, MEC, CPF/Inue, IBGE, CNPJ)

Ficha transversal (D8). Não há um documento único do INEP sobre identificadores: as regras abaixo foram extraídas do leiaute do Censo 2026, do Caderno de Conceitos, da LC 220/2025 e da Portaria MEC 269/2026. Fundamentos conceituais de identidade: `conhecimento/interoperabilidade/fundamentos/` (iop.fund.identidade-e-contexto). Privacidade/LGPD: frente de privacidade e psg.legal.lgpd-children.

```yaml
id: br.identificadores-educacionais
name: Identificadores de escola, pessoa, turma e matrícula na educação básica brasileira
acronym: ID INEP / Inue / ID SGP
jurisdiction: Brasil (federal)
issuing_organization: INEP (códigos INEP), MEC (IDs SGP; regulamentação do Inue), Receita Federal (CPF, CNPJ), IBGE (município/UF/distrito), cartórios/CNJ (matrícula da certidão de nascimento)
reference_type: conjunto de identificadores definidos em lei complementar (Inue), portaria (Inue, IDs SGP) e norma técnica do INEP (códigos do Censo)
domain: [D8, D1, D3]
official_url: https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp220.htm
repository_url: not_found
version: "LC 220/2025; Portaria MEC 269/2026; Leiaute Censo 2026 V5; API CMDEB v2.0.0"
publication_date: 2025-11-03 (LC 220, DOU); 2026-03-26 (Portaria 269, DOU)
last_updated: 2026-07-01 (leiaute)
legal_status: "CPF como Inue: obrigatório por lei complementar (LC 220/2025, art. 26 I) e portaria (Portaria MEC 269/2026, art. 7º); códigos INEP: obrigatórios no âmbito do Censo"
mandatory_scope: "Inue: bases de dados e registros administrativos dos sistemas de ensino da União, estados, DF e municípios (e, no que couber, escolas privadas e comunitárias, art. 26 §3º da LC 220; art. 2º da Portaria 269) quando houver tratamento em nível de estudante"
education_levels: [educação básica]
geographic_scope: nacional
language: pt-BR
license: not_applicable
technical_formats: [numérico de tamanho fixo]
api_available: "parcial: API CMDEB v2 permite listar estudantes e profissionais por CPF (E36); consulta pública de ID INEP: not_found"
data_model_available: parcial
ontology_available: não
schemas_available: não
implementation_examples: not_found
related_standards: [br.inep.censo-escolar, br.mec.cmdeb, br.mec.educadados, iop.br.lgpd]
entities: [Escola, Pessoa, Turma, Matrícula, Componente, Profissional, Rede/Secretaria, Mantenedora]
relationships: ver tabela abaixo
vocabularies: [schemes de identificador]
core_relevance: alta (C.IDN com scheme; resolução de identidade)
regional_adapter_relevance: muito alta
limitations: "códigos de turma e matrícula INEP são anuais e só existem após o processamento; ID INEP de pessoa não é público; CPF não é obrigatório para alunos no Censo (exceto EJA) mas é no CMDEB e na LC 220 — conflito de transição"
open_questions: [Q-01, Q-02, Q-07, Q-08]
sources: [E02, E03, E05, E06, E09, E21, E30, E31, E36, E40]
access_date: 2026-11-05
research_status: completo para formatos; parcial para emissão e publicidade
```

## Tabela de identificadores

| Identificador | Formato | Emissor / momento | Unicidade | Público ou sensível | Fonte |
|---|---|---|---|---|---|
| **Código de escola INEP** (`CO_ENTIDADE`) | 8 dígitos | INEP; escola nova é cadastrada pela secretaria estadual, que informa o código; polos EaD não recebem código, cada local de oferta de EP recebe | nacional, permanente; prefixo coerente com a UF (regra 00 c2) | público (divulgado em sinopses e microdados de escola) [I] | E02 00 c2; E06 p. 6 |
| **ID único INEP de pessoa** | 12 dígitos | gerado pelo Educacenso no cadastro de aluno, profissional ou gestor; não editável; recuperado pela exportação do ano anterior ou pelo arquivo de identificação | nacional, permanente; pode ser "excluído no processo de deduplicação" | sensível (o INEP trata o arquivo de exportação como sigiloso, E05) | E02 30 c4; E06 p. 66; E05 |
| **Código da turma INEP** | numérico ≤ 10 | INEP após a importação; só exportação | por ano | interno | E02 20 c4; E09 90 c4 |
| **Código da matrícula INEP** | numérico ≤ 12 | INEP após a importação; só exportação; exigido na 2ª etapa | por ano | interno | E02 60 c7; E09 90 c7 |
| Código no sistema próprio (pessoa, turma) | alfanumérico ≤ 20 | escola/rede | único **por escola** no arquivo | interno | E02 20 c3; 30 c3 |
| **CPF** | 11 dígitos com DV | Receita Federal | nacional | dado pessoal; **Inue** por lei | E02 30 c5; E21; E30 |
| Matrícula da certidão de nascimento (certidão nova) | 32 caracteres (30 numéricos + DV numérico ou "XX") | cartório de registro civil | nacional; não pode repetir entre alunos | dado pessoal | E02 30 c50; E03 c3 |
| NIS | 11 dígitos | CadÚnico/Caixa [I] | nacional | dado pessoal | E31 (CMDEB) |
| `ID_SGP_ESTUDANTE`, `ID_SGP_MATRICULA`, `ID_SGP_TURMA`, `ID_SGP_PROFISSIONAL`, `ID_SGP_COMPONENTE_CURRICULAR`, `ID_FORMACAO` | numéricos (componente: alfanumérico na Portaria, inteiro/string na API) | Sistema Gestão Presente (MEC) | nacional no SGP | interno | E31; E36 |
| `CO_MATRICULA_REDE`, `CO_TURMA_REDE`, `PROFISSIONAL_IDENTIFICACAO_INSTITUICAO` | alfanuméricos com `@ , # !` | rede de ensino | por rede [I] | interno | E31 |
| Município IBGE | 7 dígitos | IBGE (Tabela de Municípios 2026 do INEP) | nacional | público | E02 00 c8; E04 |
| Distrito | 9 dígitos na tabela; 2 no arquivo | IBGE via INEP | por município | público | E04 |
| Órgão regional de ensino | alfanumérico ≤ 5 | secretaria estadual (alteração só pela coordenação estadual do Censo) | por UF | público [I] | E02 00 c18; E06 p. 13 |
| CNPJ da mantenedora principal / da escola privada | 14 dígitos | Receita Federal | nacional | público | E02 00 c47–48 |
| CNPJ da secretaria de educação / unidade executora | ≤ 14 | Receita Federal | nacional | público | E31 bloco 4 |
| Código da IES (unidade ofertante de superior) | ≤ 9 dígitos | INEP/e-MEC | nacional | público | E02 00 c53 |
| RA – Registro do Aluno (SP) | número + dígito + UF | SEDUC-SP (SED) | rede estadual SP | dado pessoal | E40; ver [sed-sp.md](sed-sp.md) |

## Resolução de identidade no Censo (regras 37–40 do leiaute)

1. ID INEP preenchido → identifica por ele.
2. Sem ID e com CPF → identifica por CPF (nome e nascimento passam a vir da Receita Federal).
3. Sem ID e sem CPF, com certidão nova → por certidão.
4. Nenhum dos três → busca por nome + nascimento + filiação (1 e 2 em qualquer ordem). Um resultado: reaproveita; zero ou vários: **cria nova pessoa**.

Regra anti-"descaracterização" (regra 29): não se pode trocar a identidade de um ID alterando, ao mesmo tempo, campos de identificação forte.

## Achado central para o Core [I]

Existem hoje **três chaves nacionais concorrentes para o estudante**: ID INEP (Censo), `ID_SGP_ESTUDANTE` (MEC) e CPF (Inue, obrigatório por LC 220 e Portaria 269). A norma mais recente e de maior hierarquia fixa o CPF. Mesmo assim, o Censo 2026 ainda aceita aluno sem CPF (fora da EJA) e resolve identidade por ID INEP primeiro. O Core deve tratar identificadores como lista `C.IDN(scheme, value, issuer, valid_from)` sem eleger um único "ID nacional", e o adaptador deve priorizar CPF quando presente.
