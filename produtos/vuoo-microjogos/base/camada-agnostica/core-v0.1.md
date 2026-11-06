# Core agnóstico: síntese v0.1 (proposta)

**Estado:** proposta para discussão, escrita em 2026-11-05. **Não é decisão.** Cada decisão vira ADR (pasta `padroes/` desta solução) depois da revisão humana (plano acordado em 29/10/2026). Este arquivo consolida:

- os crosswalks das seis pastas de jurisdição;
- os "candidatos a entidade do Core" registrados nas questões abertas;
- a pesquisa de arquitetura em [padroes-de-arquitetura.md](padroes-de-arquitetura.md), com evidências em [evidencias-arquitetura.md](evidencias-arquitetura.md).

A lista provisória de [../_convencoes.md §4](../_convencoes.md) continua valendo como alvo dos crosswalks já escritos. Este arquivo propõe a revisão dessa lista.

## 1. Princípios (tirados das evidências)

| # | Princípio | De onde vem |
|---|---|---|
| P1 | **Core mínimo e neutro.** Uma entidade só entra no Core se pelo menos duas jurisdições a usarem com o mesmo sentido. O que existe em uma só fica no perfil regional. | Modelo SEMIC (Core Vocabulary + Application Profile), arquitetura P1.3; risco de viés brasileiro |
| P2 | **Papel é atribuição, não subtipo.** Pessoa × papel × organização (ou oferta) × vigência. | OneRoster Role, Edu-API Affiliation, Ed-Fi (EUA Q19); CMDEB, onde a mesma pessoa é estudante e profissional |
| P3 | **Vínculos são bitemporais**: tempo válido e tempo de registro, com identificador substituto e a vigência como atributo. | Conflito Ed-Fi × OneRoster (EUA §3); códigos INEP refeitos a cada ano (BR Q-03) |
| P4 | **Identificador é lista**, no formato `{scheme, issuer, value, vigência, status, usoPermitido}`. | CPF, ID INEP e ID SGP (BR Q-01); UPN, ULN, UCI, SCN e LAESTAB (UK); 学籍号 (CN) |
| P5 | **Código não é identidade.** Itens curriculares e de vocabulário têm IRI próprio; o código oficial é um atributo. | BNCC com forma impressa diferente do código (`EF05CO011` na Computação); Currículo Paulista; CCSS com identificação tripla |
| P6 | **Vocabulário é dado com dono.** Um `ConceptScheme` por lista oficial, versionado. Códigos revogados continuam resolvíveis. | Ed-Fi descriptors; 37 listas controladas do ELM; Censo × CMDEB |
| P7 | **Mapeamento é dado.** SKOS + SSSOM (justificativa, confiança, autor, versões). `exactMatch` só com revisão humana. | Arquitetura P1, risco 2 (transitividade) |
| P8 | **Valor ≠ classificação.** O resultado numa escala é um dado; os cortes são esquemas versionados aplicados sobre ele. | Saeb, SARESP, CNCA (BR); níveis EQF e de proficiência (UE) |
| P9 | **Apoio ≠ elegibilidade ≠ diagnóstico**: três eixos independentes, e o plano tem mantenedor e ciclo de vida. | Port. MEC 421/2026; SEND N/K/E e EHCP (UK); ALN/IDP (Gales); motivos amplos de apoio (Escócia) |
| P10 | **Sensibilidade por atributo, base legal por operação.** | LGPD arts. 11 e 14; FERPA directory info; PIPL (menores de 14 = dado sensível); Children's Code |
| P11 | **A organização acadêmica é independente da experiência de aprendizagem** (briefing §2.3). | Turma (Censo) × grupo de aprendizagem; homeroom (EUA) |
| P12 | **O nível educacional tem pivô internacional**: ISCED-P atribuído ao segmento. | [../internacional/mapeamentos-isced.md](internacional/mapeamentos-isced.md) |

## 2. Entidades do Core v0.1 (revisão da lista provisória)

Legenda da coluna Mudança: **=** mantida; **Δ** alterada; **+** nova; **→P** rebaixada para perfil regional.

### D1 Organização acadêmica

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.ORG | Organization | Δ | Subclasses tipadas: sistema, rede/autoridade, mantenedora, escola, unidade. As relações N:N vão para `OrganizationRelationship` com tipo e vigência (EUA lição 5; unidade vinculada × escola sede no BR). Não é uma árvore única. |
| C.LOC | Location | = | O Censo não identifica salas; o Core aceita local opcional. |
| C.SES | AcademicSession | Δ | Hierárquica (ano letivo → período → bimestre). Ganha `CalendarDate` (dia letivo ou não) para validar os 200 dias e a carga horária (LDB art. 24; EUA Q17). |
| C.STG | EducationalStage | Δ (era C.PRG) | Etapa, segmento, ano ou série, modalidade, com `iscedLevel` obrigatório. Renomeado porque *Program* no Ed-Fi é programa de serviço, um falso amigo. A estrutura de anos varia por organização: na China, 6+3 ou 5+4 (六三/五四). |
| C.SVC | ServiceProgram | + | AEE, tempo integral, alimentação gratuita (FSM no UK), atividade complementar. Os programas de serviço do Ed-Fi e as matrículas de AEE do Censo. |
| C.SUB | Subject / CurricularComponent | = | Código nacional (Tabela de Áreas do Censo) como identificador com scheme. |
| C.CRS | CourseDefinition | + | Unidade de catálogo, distinta de componente e de oferta (Ed-Fi Course, OneRoster Course, Edu-API CourseTemplate). **Opcional** no Brasil, onde o Censo não tem catálogo. |
| C.OFR | Offering / Section | = | Componente × grupo × período × profissionais. Em OneRoster é *class*; no CMDEB é a alocação. |
| C.GRP | Group | Δ | `kind`: turma acadêmica, homeroom, grupo de aprendizagem, grupo de AEE. Atributos BR (multietapa, classe especial, bilíngue) ficam no perfil. |
| C.SCH | Schedule / Meeting | = | |
| C.ENR | Enrollment | Δ | Dois níveis: vínculo com organização e etapa (CMDEB, Ed-Fi StudentSchoolAssociation) e vínculo com grupo ou oferta (Censo reg. 60, OneRoster). Tem `kind` (escolarização, AEE, complementar) e `registrationType` (principal, dual, guest no UK). Bitemporal. |
| C.ENS | EnrollmentStatusEvent | + | Eventos de situação (os 17 do CMDEB); a situação anual do Censo (8 códigos) é derivada deles. |
| C.ATT | Attendance | + | Agregado (horas ofertadas × presentes por mês, CMDEB) ou evento (Ed-Fi AttendanceEvent). Candidato registrado no BR (Q-15) e nos EUA (Q25). |

### Pessoas e papéis (D1, D3)

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.PER | Person | = | Mínimo de dados pessoais. Os atributos demográficos têm proveniência por organização informante (EUA lição 6). |
| C.ROL | RoleAssignment | + | Substitui C.LRN, C.STF e C.GRD como subtipos. Os papéis vêm de um vocabulário (aluno, docente, gestor, profissional de apoio, responsável…). |
| C.REL | PersonRelationship | Δ (era C.GRD) | Responsável × estudante, com tipo de vínculo (0–5 no CMDEB) e direitos (consentimento, acesso). |

### D2/D4 Currículo

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.CFW | CompetencyFramework | Δ | Tem quatro relógios: ato normativo, edição do texto, versão do dado e esfera (nacional, estadual, rede). |
| C.CMP | CompetencyItem | Δ | Tipado: organizador (área, unidade temática, eixo) ou item (habilidade, objetivo, objeto de conhecimento). O código oficial é atributo. |
| C.CAS | CompetencyAssociation | Δ | Tipos: hierarquia, `derivaDe` (desdobramento paulista), `composedOf` com dimensão (NGSS: SEP + DCI + CCC), alinhamento e pré-requisito. A equivalência entre frameworks vai para C.MAP. |
| C.ADP | CurriculumAdoption | + | Organização × edição × etapa × coorte × vigência. Necessária pela DCNEM 2024 (dois regimes por coorte) e pelos currículos estaduais (BR Q-CUR-05). |

### D5 Avaliação

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.ASM | Assessment / Instrument | = | |
| C.ITM | AssessmentItem | = | Alinhamento item→habilidade é curadoria, com proveniência: as matrizes Saeb-BNCC não citam códigos. |
| C.RES | Result | Δ | Só o valor na escala, com a escala identificada. |
| C.PCS | PerformanceClassificationScheme | + | Cortes e níveis versionados (níveis do Saeb, SARESP, 743 do CNCA, EQF). Um mesmo resultado pode ter várias classificações. |
| C.RUB | Rubric / CriterionLevel | + | CLR e CASE (EUA Q12); útil para observação docente. |
| C.EVD | Evidence / Observation | = | |

### D6 Experiência

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.ACT | LearningActivity / Resource | = | Micro-atividades e jogos do VUOO. |
| C.EVT | LearningEvent | = | Telemetria. Exportável como xAPI ou Caliper (views). Ligado à pessoa e à matrícula em que foi gerado; leva versão do conteúdo, do normalizador e perfil do aparelho ([relatório §7.9](../relatorio-infra-vuoo.md)). |
| C.ASN | ActivitySession | + | Sessão de uso de atividades no aparelho, contexto dos eventos (âncora de relógio, sequência, aparelho, taxa efetiva dos sensores). Distinta de C.SES, que é calendário letivo. |
| C.PTH | Pathway | → avaliar | Ed-Fi Path (EUA Q21) e percursos adaptativos. Fica para quando D6 for desenhado. |

### D7 Inclusão

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.SUP | SupportProfile | Δ | Barreira, potencialidade, apoio (tipo, intensidade, ambiente, vigência) e acomodação (alvo: atividade, avaliação ou material). Existe sem elegibilidade e sem diagnóstico. |
| C.ELG | Eligibility | + | Categoria administrativa para coletas oficiais (CMDEB, SEN primary need no UK). Sensível, com acesso isolado, e **nunca alimenta a personalização**. |
| C.DOC | SupportingDocumentReference | + | **Só metadados e referência externa; o VUOO não armazena o arquivo** (decisão de 2026-11-05). Campos: tipo, categoria do emissor, datas, situação e `{sistemaOrigem, idExterno}`. Sensível. |
| C.PLN | IndividualPlan | Δ | Seções tipadas (PAEE/PEI no BR; EHCP A–K na Inglaterra; IDP em Gales), `maintainer` (escola ou autoridade local), estudo de caso, metas ligadas a C.CMP, acompanhamentos, revisões e devolutivas. |

### D3 Registro e credenciais

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.CRD | Credential / Achievement | = | Envelope VC 2.0 / Open Badges 3.0 na exportação. Qualificação, crédito e acreditação (UE) ficam no perfil UE. |
| C.REC | AcademicRecord | → standby | Histórico e boletim (Ed-Fi, art. 24 VII da LDB). Entra quando houver emissão de histórico. |

### D8 Interoperabilidade e governança

| Código | Entidade | Mudança | Nota |
|---|---|---|---|
| C.IDN | Identifier | Δ | `{scheme IRI, issuer, value, vigência, status, usoPermitido}`; unicidade por `(scheme, issuer, value)`. O `usoPermitido` vem do UPN, que só vale no contexto educacional. |
| C.VOC | ControlledVocabulary | = | `skos:ConceptScheme` com governante, versão, vigência e licença. |
| C.MAP | Mapping | + | Mapeamento SSSOM entre conceitos ou códigos (Censo↔CMDEB, BNCC↔Currículo Paulista, etapa↔ISCED). |
| C.CNS | Consent / LegalBasis | Δ | A base legal é registrada **por operação**; o consentimento tem outorgante (responsável), verificação e assentimento da criança. |
| C.DCL | DataClassification | + | Sensibilidade por atributo (LGPD art. 11, FERPA directory info, PIPL) e nível do conjunto de dados (L1–L5 da JY/T 0661—2025). |
| C.DSC | DisclosureRecord | + | Registro de divulgação: destinatário, finalidade e base. Exigido pelo FERPA §99.32; útil para a LGPD. |
| C.GRT | AccessGrant | + | Concessão de acesso de uma organização aos dados do aluno: escopo (matrículas, períodos), categorias, finalidade, base legal, vigência, revogação; bitemporal. A matrícula ativa gera uma concessão automática; a migração entre escolas gera uma por aprovação do titular ou responsável, com a organização de origem oculta (decisão INF-15 do [relatório](../relatorio-infra-vuoo.md)). O repositório do aluno fica fora dos tenants, e cada concessão tem um tipo de vínculo: `titular` (matrícula ativa), `legado` (matrícula encerrada) ou `global` (sem escola) (INF-22). A revogação é em camadas: escola, treino do VUOO, exportação e eliminação total (INF-21). Princípio transversal (portabilidade: LGPD art. 18; FERPA). |
| C.AGR | DataAgreement / RetentionPolicy | + | Acordo por organização contratante: finalidades, prazos e local de processamento. Inclui o registro de residência e transferência internacional, exigido pelas regras da CAC de 2024. |
| C.PRV | Provenance | = | Sempre por lote e por registro; por campo só onde há fontes concorrentes. |
| C.DCLR | Declaration / Submission | + | Fotografia declarada a um órgão numa data de referência, com status de importação (Censo, School Census). |

**Fica fora do Core v0.1**, nos perfis ou em standby:

- **UE:** qualificação, crédito, entitlement, acreditação.
- **UK:** evento disciplinar, elegibilidade a benefício (vai para C.SVC ou o perfil UK).
- **EUA:** finanças, saúde, vínculo empregatício e avaliação docente.
- **BR:** atributos de infraestrutura do Censo (reg. 10).

## 3. Camadas e artefatos

Segue a recomendação de [padroes-de-arquitetura.md §6](padroes-de-arquitetura.md):

```
vuoo-core (OWL + SKOS)  ← fonte única; o resto é gerado e conferido no CI
  ├─ JSON Schema 2020-12 / OpenAPI 3.1  (APIs)
  ├─ esquema relacional                 (base operacional; implementação do Core, não 2º modelo)
  ├─ R2RML                              (relacional → RDF: grafo virtual/materializado, exportações)
  └─ @context JSON-LD (@protected)      (troca)
perfis regionais vuoo-br, vuoo-us, … = extensões no namespace da jurisdição + shapes SHACL + ConceptSchemes + mapeamentos SSSOM
adaptadores (camada anticorrupção) = importação/exportação por fonte e por versão (ex.: Censo 2026, API CMDEB v2)
views de exportação = OneRoster, CASE, xAPI/Caliper, VC/OB
```

Regras de extensão:

1. O perfil **restringe** o Core por SHACL (cardinalidade, vocabulário obrigatório).
2. O perfil **acrescenta** só no próprio namespace (`vuoo-br:`).
3. O perfil **não redefine** termos do Core.
4. Um conceito do perfil que se pareça com um do Core abre discussão sobre subir para o Core, e só sobe se cumprir P1.

## 4. Padrões-base

A proposta detalhada está em [../internacional/README.md](internacional/README.md):

- **Datas:** RFC 3339 em UTC para instantes, RFC 9557 para hora local com fuso, `YYYY-MM-DD` para datas civis.
- **Idioma e lugar:** BCP 47 para idioma; ISO 3166-1/-2 para país e estado (BR-SP).
- **Identificadores:** UUIDv7 interno.
- **Contratos:** JSON Schema 2020-12, OpenAPI 3.1, JSON-LD 1.1.
- **Semântica:** SKOS, PROV-O, SHACL.
- **Credenciais:** VC 2.0 e Open Badges 3.0.
- **Acessibilidade:** WCAG 2.2.
- **Nível educacional:** ISCED 2011.

## 5. Teste de neutralidade

Antes de aceitar o Core v0.1, cada entidade passa pelo crosswalk das cinco jurisdições. Ela é aceita se tiver equivalência exata ou aproximada em pelo menos duas, ou se for exigida por princípio transversal (D8). Os crosswalks por pasta já existem:

- [Brasil (organização)](../camada-brasil/crosswalk-core-organizacao.md)
- [Brasil (currículo)](../camada-brasil/crosswalk-core-curriculo-avaliacao-inclusao.md)
- [EUA](../fora-da-fase-1/estados-unidos/crosswalk-core.md)
- [UE](../fora-da-fase-1/uniao-europeia/crosswalk-core.md)
- [Reino Unido](../fora-da-fase-1/reino-unido/crosswalk-core.md)
- [China](../fora-da-fase-1/china/crosswalk-core.md)
- [Internacional](internacional/crosswalk-core.md)

Falta consolidar todos numa matriz única entidade × jurisdição. É o próximo passo da síntese.
