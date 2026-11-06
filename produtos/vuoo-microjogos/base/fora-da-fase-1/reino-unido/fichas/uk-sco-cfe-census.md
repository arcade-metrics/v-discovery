# Escócia: Curriculum for Excellence, ScotXed / Pupil Census, ASN

```yaml
id: uk-sco-cfe-census
name: Curriculum for Excellence; Scottish Exchange of Data (ScotXed) school-pupil census; Additional Support for Learning
acronym: CfE / ScotXed / ASN
jurisdiction: Escócia
issuing_organization: Scottish Government (ScotXed Unit, Education Analytical Services); Education Scotland (currículo)
reference_type: currículo nacional (framework) + coleta estatística anual com especificação de dados
domain: [D1, D2, D4, D7, D8]
official_url: https://www.gov.scot/publications/scottish-exchange-of-data-school-pupil-census/ ; https://education.gov.scot/curriculum-for-excellence/
repository_url: n/a
version: "School and Pupils Data Spec 2026 v4.0 (XLSX); rascunho 2027"
publication_date: página do censo 2024-05-17
last_updated: 2026-06-19 (datas e spec 2026)
legal_status: censo é coleta estatística nacional; ASN sob Education (Additional Support for Learning) (Scotland) Act 2004; código de prática "Supporting Children's Learning" 4ª edição (2026) [busca]
mandatory_scope: escolas públicas, via autoridades locais
education_levels: early learning a S6
geographic_scope: Escócia
language: inglês (e gaélico em partes)
license: unknown
technical_formats: [XML (nomes de elemento na spec, ex. scottish-candidate-number), XLSX (spec), validação ProcXed]
api_available: não
data_model_available: sim (spec com campos, cardinalidade mín./máx., tipo, códigos e regras de validação)
ontology_available: não
schemas_available: parcial (nomes XML na spec)
implementation_examples: n/a
related_standards: [uk-identificadores, uk-eng-send-ehcp]
entities: School, Pupil, Class (tamanho de turma), Need record
relationships: aluno 0..n registros de necessidade com categoria e tipos
vocabularies: student-stage (P1–P7, S1–S6, S9, SP); categorias de ASN; tipos de plano; natureza do apoio
core_relevance: muito alta para D7 (modelo não médico de necessidade)
regional_adapter_relevance: alta
limitations: currículo não legível por máquina (experiences and outcomes e benchmarks em documentos)
open_questions: códigos numéricos de todas as categorias ASN (só "10 Learning disability" extraído)
sources: [S-UK-09, S-UK-12, S-UK-13]
access_date: 2026-11-05
research_status: verificado (spec 2026 inspecionada)
```

## Curriculum for Excellence

Oito áreas curriculares: Expressive arts; Literacy and English; Health and wellbeing; Numeracy and mathematics; Religious and moral education; Sciences; Social studies; Technologies. Ferramentas: **experiences and outcomes** (planejar e avaliar progresso) e **benchmarks** ("national standards expected within each curriculum area at each level") [S-UK-12]. Níveis: Early (idade 3 a P1), First (P2–P4), Second (P5–P7), Third/Fourth (S1–S3), depois Senior Phase (S4–S6); progressão "at their own pace" [S-UK-13].

[I] Diferença-chave para o Core: o **nível curricular** (Early…Fourth) não coincide com o **estágio** (P1…S6) e o aluno avança no seu ritmo; o governo publica estatística de "achievement of CfE levels" por estágio. C.PRG (estágio) e nível alcançado (C.RES sobre C.CMP de nível) precisam ser separados.

## Pupil census (ScotXed)

Dia do censo 2026: **9 de setembro de 2026**; envio ao governo até 6/10/2026 [S-UK-09]. Itens observados na spec 2026 [S-UK-09]:

- **Scottish Candidate Number** (9 dígitos, obrigatório, único por aluno, dígito verificador mód. 11 com pesos 3,2,7,6,5,4,3,2).
- **Student Stage** (código 2c): P1–P7, S1–S6, S9 (secundário 18+), SP (escola especial sem estágio atribuível); consistência idade × estágio em 1º de março (ex.: P1 3–6 anos), regra de tipo de escola × estágio.
- **Registration Class** (nome da turma de registro, para P1–P7).
- **Attendance at special schools/units or classes** (meios-dias, 0–10).
- **Need record** com **categoria** (motivo do apoio adicional) e **tipos** (plano/estatuto): `01` CSP (Co-ordinated Support Plan), `02` IEP, `03` AssessedDisabled, `04` DeclaredDisabled, `06` Child's Plan.
- **Nature of additional support provided**: `01` especialista docente, `02` especialista não docente, `03` serviço social, `04` saúde, `05` voluntário, `06` professor da turma, `99` outro.

**Categorias de motivo do apoio (ASN)** [S-UK-09]: Learning disability (código 10); Dyslexia; Other specific learning difficulty; Other moderate learning difficulty; Visual impairment; Hearing impairment; Deafblind; Physical or motor impairment; Language or speech disorder; Autistic spectrum disorder; Social, emotional and behavioural difficulty; Physical health problem; Mental health problem; **Interrupted learning; English as an additional language; Looked after; More able pupil; Communication support needs; Young carer; Bereavement; Substance misuse; Family issues; Risk of exclusion**; Not disclosed/declared; Other.

### Lição para o Core (D7) [I]

O modelo escocês de "additional support needs" é **mais amplo que deficiência**: inclui fatores sociais e circunstanciais (cuidador jovem, luto, criança acolhida, inglês como língua adicional, altas habilidades). Deficiência é registrada à parte como **estatuto** (avaliada ou declarada) e o plano (CSP, IEP, Child's Plan) é outro eixo. É o exemplo mais claro, entre os vistos, de C.SUP como **barreira/necessidade de apoio** e não como diagnóstico, e confirma que o Core precisa de três eixos independentes: motivo do apoio, estatuto de deficiência, tipo de plano.
