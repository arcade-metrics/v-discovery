# Ficha: Novo Ensino Médio (Lei 14.945/2024, DCNEM 2024 e Parâmetros dos IFAs 2025)

> Acesso: 2026-11-05. Textos lidos: Lei 14.945/2024 (Planalto, compilado); Res. CNE/CEB 2/2024 (cópia da Seduc-PA do documento assinado); Res. CNE/CEB 4/2025 (cópia do DOU via ANEC); Portaria Inep 435/2025 (cópia do DOU via ANEC); Res. SEDUC-SP 84/2024 (cópia hospedada pela Unesp).

```yaml
id: br.novo-ensino-medio
name: "Reforma do Ensino Médio de 2024: Lei 14.945/2024, DCNEM (Res. CNE/CEB 2/2024) e Parâmetros Nacionais dos IFAs (Res. CNE/CEB 4/2025)"
acronym: NEM 2024 / DCNEM / IFA
jurisdiction: Brasil (federal), com implementação estadual
issuing_organization: Congresso Nacional / Presidência (lei); CNE/CEB (resoluções)
reference_type: [lei, norma (resolução do CNE)]
domain: [D4, D2, D5, D1]
official_url:
  - https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l14945.htm
  - https://www.seduc.pa.gov.br/site/public/upload/arquivo/probncc/RESOLUCAO%20CNE-CEB%202-2024-f599f.pdf (cópia; DOU 14/11/2024, Seção 1, p. 48)
  - https://anec.org.br/wp-content/uploads/2025/05/RESOLUCAO-CNE_CEB-No-4-DE-12-DE-MAIO-DE-2025.pdf (cópia; DOU 13/05/2025, Seção 1, p. 36)
repository_url: not_found
version: "Lei 14.945 de 31/07/2024; Res. CNE/CEB 2 de 13/11/2024 (vigor 02/12/2024); Res. CNE/CEB 4 de 12/05/2025"
publication_date: 2024-08-01 (lei, DOU)
last_updated: 2025-05-13
legal_status: em vigor
mandatory_scope: sistemas de ensino e escolas públicas e privadas que ofertam EM (DCNEM art. 1 e 2)
education_levels: [EM]
geographic_scope: nacional
language: pt-BR
license: domínio público (atos oficiais) [I]
technical_formats: [HTML, PDF]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: [Res. SEDUC-SP 84/2024 (matrizes do EM paulista)]
related_standards: [br.bncc (EM 2018), br.dcn, br.saeb, br.curriculo-paulista]
entities: [formação geral básica (FGB), itinerário formativo de aprofundamento (IFA), itinerário de formação técnica e profissional, área do conhecimento, componente curricular obrigatório, componente eletivo, projeto de vida, eixo curricular estruturante, competência comum dos IFAs, objetivo de aprendizagem da área (competência + "demonstrando a capacidade de")]
relationships: [FGB → BNCC EM; IFA → área(s) aprofundada(s); IFA → 4 eixos estruturantes (todos obrigatórios); IFA → competências comuns e de área do Anexo; estudante → regime curricular por coorte de ingresso]
vocabularies: [4 áreas e componentes obrigatórios (DCNEM art. 17); 4 eixos estruturantes (Res. 4/2025 art. 11); 10 competências comuns dos IFAs (Anexo)]
core_relevance: alta: obriga o Core a suportar coexistência de regimes curriculares por coorte e caminhos de escolha (itinerário)
regional_adapter_relevance: alta: SP já reorganizou matrizes (Res. SEDUC 84/2024)
limitations: [competências e habilidades dos IFAs no Anexo da Res. 4/2025 não têm código; matrizes do Saeb/Enem para o EM ainda não alinhadas (prazos 2027/2028)]
open_questions: [Q-CUR-05, Q-AVA-04]
sources: [E-07 a E-12]
access_date: 2026-11-05
research_status: verificado (textos primários ou cópias fiéis de DOU)
```

## Fatos normativos que viram regra de dados

| Fato | Fonte | Regra para o Core/adaptador [I] |
|---|---|---|
| FGB mínima de 2.400 h; 2.100 h com formação técnica | Lei 14.945, LDB art. 35-C e par. único | carga horária mínima é atributo do **programa** (C.PRG), validada por regime |
| Itinerários com mínimo de 600 h; ao menos 2 itinerários com ênfases distintas por escola, salvo FTP | LDB art. 36, caput e §2º-A; DCNEM art. 18 e 19 | itinerário = C.PRG filho (percurso) com escolha do estudante; oferta por escola |
| Áreas e componentes obrigatórios da FGB: LP e literaturas, inglês, artes, educação física; matemática; biologia, física, química; filosofia, geografia, história, sociologia | DCNEM art. 17 | vocabulário de componentes do EM no adaptador (C.SUB) |
| Educação digital obrigatória no EM, "na forma definida em cada sistema" | DCNEM art. 17 §4 | ligação a br.bncc-computacao |
| Ingressantes de 2025 podem ter "matriz curricular de transição"; ingressantes de 2026 com organização "plenamente atualizada" | DCNEM art. 39 §§1 e 2 | **regime curricular por coorte**: o vínculo do estudante aponta a versão do currículo vigente na sua entrada |
| Quem entrou antes da DCNEM 2024 pode seguir a Res. 3/2018 em regime de transição | DCNEM art. 42 e 43 (revoga a Res. 3/2018 "ressalvado o regime de transição") | dois C.CFW de estrutura (2018 e 2024) válidos ao mesmo tempo |
| IFAs organizados em 4 eixos: Método, Conhecimento e Ciência; Mediação e Intervenção Sociocultural; Inovação e Intervenção Tecnológica; Mundo do Trabalho e Transformação Social | Res. 4/2025 art. 11 | vocabulário controlado de eixo |
| Anexo: 10 competências comuns aos IFAs e, por área, competências com lista "Demonstrando a capacidade de:" | Res. 4/2025, Anexo | itens **sem código oficial**: id cunhado obrigatório (regra bncc-dados) |
| Inep deve elaborar matrizes do Saeb e do Enem alinhadas à DCNEM até 20/12/2025; adaptação do Saeb até 2027 e do Enem até 2028 | DCNEM art. 30, §§4 a 6; Res. 4/2025 art. 28 §§1 e 2 | avaliação do EM em transição; ver br.saeb |
| Saeb 2025 aplicou ao EM (3ª e 4ª séries) apenas as matrizes de 2001 | Portaria Inep 435/2025, art. 9, VI | idem |

A Portaria Inep 435/2025 cita expressamente o "art. 30 da Resolução CNE/CEB nº 2, de 13 de novembro de 2024" ao manter as matrizes de 2001 no EM.

## Caso SP (rede estadual)

A Res. SEDUC 84/2024 organiza o EM em 3 séries, FGB de 2.400 h que "contempla as Competências e Habilidades previstas no Currículo Paulista - Etapa do Ensino Médio", e cria componentes de rede que carregam **parte** das habilidades de outro componente: "Redação e Leitura" contempla parte das habilidades de Língua Portuguesa; "Educação Financeira", parte das de Matemática (art. 4, §1, III e IV). Consequência [I]: a relação componente da rede → habilidade do currículo é n:n e não segue a área do documento curricular; o Core precisa de `C.CAS` do tipo "componente ofertado cobre habilidade".
