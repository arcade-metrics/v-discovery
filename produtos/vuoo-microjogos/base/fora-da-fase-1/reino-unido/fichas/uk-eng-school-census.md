# School Census (Inglaterra) e Common Transfer File

```yaml
id: uk-eng-school-census
name: School census (business and technical specification 2026 to 2027)
acronym: School Census
jurisdiction: Inglaterra
issuing_organization: Department for Education (DfE)
reference_type: coleta estatutária de dados + especificação técnica
domain: [D1, D3, D5, D7, D8]
official_url: https://www.gov.uk/guidance/complete-the-school-census
repository_url: n/a
version: "2026 to 2027, especificação v1.2"
publication_date: guia publicado 2019-07-30
last_updated: guia atualizado 2026-10-13
legal_status: obrigatório: seção 537A do Education Act 1996; Education (Information About Individual Pupils) (England) Regulations 2013; Education (Information About Young Children) (England) Regulations 2009
mandatory_scope: escolas mantidas, academies, free schools, special schools, PRUs/AP (escolas independentes têm coleta própria, SLASC)
education_levels: nursery a pós-16 escolar
geographic_scope: Inglaterra
language: inglês
license: unknown
technical_formats: [XML (anexos A e B: estrutura das mensagens), W3C XML Schema]
api_available: não (envio de arquivo pelo serviço COLLECT [I: nome não confirmado nesta sessão])
data_model_available: sim (níveis, módulos, itens CBDS)
ontology_available: não
schemas_available: sim (XML Schema citado na especificação)
implementation_examples: MIS comerciais (release de software de maio/2026 para o censo de outono/2026)
related_standards: [uk-eng-cbds, uk-identificadores, uk-eng-send-ehcp]
entities: School, Pupil, Class (agregado), módulos
relationships: escola 1..n alunos; dados de turma agregados no nível escola
vocabularies: code sets CBDS
core_relevance: alta: mostra a fronteira entre dado transacional e dado de coleta
regional_adapter_relevance: muito alta
limitations: turma só como agregado (contagens e tipo) e apenas para primárias; sem vínculo aluno–turma–professor
open_questions: datas exatas dos censos 2026–27 (Anexo C) não extraídas
sources: [S-UK-03, S-UK-04]
access_date: 2026-11-05
research_status: verificado (especificação lida)
```

## Análise técnica

**Estrutura** [S-UK-04]: dois níveis, **School** e **Pupil**; cada nível é composto por **módulos** com itens relacionados. Coleta **trimestral** (autumn, spring, summer), com módulos diferentes por termo; escolas de seis termos mapeiam termos 1–2/3–4/5–6. Dados **snapshot** (situação no dia do censo) e **contínuos** (frequência, suspensões e exclusões, períodos de FSM, aims pós-16, alternative provision, learner funding): censos sucessivos montam a série histórica.

**Módulos do nível escola:** school characteristics; admission appeals (primária, infantil, secundária; só primavera); pupil reconciliation; **class information**; miscellaneous.
**Módulos do nível aluno:** pupil identifiers; pupil characteristics; pupil status; alternative provision placement; **special educational needs** (usado para financiamento); managed moves (novo); termly suspension and permanent exclusion; home information; free breakfast club attendance; termly attendance; post-16 learning aims [S-UK-04].

**Turma.** O módulo de turma pede Class type (N00267), Class key stage (N00268) e Class activity (N00247) **para todas as turmas de escolas primárias** e anos até o 6 em escolas all-through; serve para controlar o limite legal de 30 alunos por professor em turmas infantis (exceções N00665–N00672) [S-UK-04]. Não há ligação aluno–turma no censo. [I] O vínculo aluno–turma–professor existe no MIS, não no padrão nacional.

**Identificadores no censo.** ULN (N00011) obrigatório para todo aluno com 14 anos ou mais no dia do censo [S-UK-04]; UPN para todos; URN/LAESTAB para a escola.

**SEN no censo** [S-UK-04]: provisão registrada segundo o SEND Code of Practice 2015; no censo de **primavera** coleta-se tipo de SEN para alunos com provisão `E` (EHC plan) ou `K` (SEN support); **no máximo dois tipos**, ordenados por ranking (N00024), sem empate em 1; indicadores de SEN unit (N00022) e resourced provision (N00023) coletados todo termo, só para provisão designada pela LA.

**Common Transfer File (CTF).** Arquivo de transferência entre escolas; o CTF 26 (implementação a partir de agosto de 2026) usa itens e code sets do CBDS [S-UK-05, busca]. Lição [I]: o padrão nacional define o **pacote de transferência** do histórico do aluno entre escolas, o que o Core deve conseguir exportar.

**Frequência** (CS066): marca por **sessão** (manhã/tarde), com ~35 códigos (presente, ausências autorizadas/não autorizadas, atividade educacional aprovada, impossibilidade de comparecer Y1–Y7…) [S-UK-02]. [I] C.SCH/C.EVT do Core precisam suportar meio período como unidade de presença.
