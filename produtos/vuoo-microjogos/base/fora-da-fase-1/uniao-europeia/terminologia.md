# Terminologia: União Europeia

Conceitos, códigos e vocabulários controlados. Fontes em [evidencias.md](evidencias.md).

## 1. Conceitos do ELM (definições oficiais, resumidas)

| Termo | Definição (rdfs:comment do ELM.ttl, v3.1) | Fonte |
|---|---|---|
| Learning Outcome | "what a learner knows, understands and is able to do on completion of a learning process", em termos de conhecimento, habilidades e responsabilidade e autonomia | S-UE-02 |
| Learning Achievement | "A recognised and/or awarded set of learning outcomes of an individual" | S-UE-02 |
| Learning Opportunity | "An opportunity to realise a given set of learning outcomes via a learning activity and/or assessment" | S-UE-02 |
| Learning Activity | "Any process which leads to the acquisition of knowledge, skills or responsibility and autonomy" | S-UE-02 |
| Learning Assessment | resultado de processo que estabelece em que medida o aprendiz atingiu conhecimentos, habilidades e competências contra critérios | S-UE-02 |
| Learning Entitlement | direito (ex.: exercer profissão, acessar oportunidade) resultante da aprendizagem | S-UE-02 |
| Qualification | "A specification of an assessment and validation process which is obtained when a competent authority determines that an individual has achieved learning outcomes to given standards" | S-UE-02 |
| Awarding Process | processo de uma organização conceder um Claim a uma pessoa com base numa Specification | S-UE-02 |
| European Digital Credential | "A set of claims made by an issuer in Europe, using the Europass Standards" | S-UE-02 |
| Grading Scheme | "A set of criteria that measures varying levels of achievement" | S-UE-02 |
| Result Distribution | histograma dos resultados de todos os estudantes de uma instância de curso | S-UE-02 |
| Group | "An entity that represents collection of Agents" | S-UE-02 |

## 2. Listas controladas Europass (EU Vocabularies, 37)

Coleção "Controlled lists", desenvolvida por ESCO e equipe EDC [S-UE-05]. URIs base `http://data.europa.eu/snb/<lista>/` (exemplos confirmados no perfil EDC: `eqf`, `isced-f`, `learning-setting`, `credential`, `claim-type`, `evidence-type`, `verification`, `verification-status`, `skill-type`, `skill-reuse-level`, `entitlement-status`, `accreditation`, `qdr`) [S-UE-04].

| Grupo | Listas |
|---|---|
| Níveis e classificações | European Qualifications Framework; Qualifications Framework; International Standard Classification of Education; Educational credit system |
| Competências | Skill type; Skill reusability level; Key competences for lifelong learning; Digital Competence Framework; Foreign language skill |
| Oportunidade e atividade | Learning opportunity type; Learning activity type; Learning setting type; Learning schedule type; Mode of learning and assessment; Target group; Learning opportunity information topic |
| Avaliação | Assessment type; Grade status; Method of supervision and verification |
| Credencial e verificação | Credential type; Claim type; Evidence type; Verifiable presentation type; Verification type; Verification status; Attachment type; Content encoding type |
| Direitos e acreditação | Entitlement type; Entitlement status; Accreditation type; Accreditation status; Accreditation decision; Recognition agreement type; Qualification information topic |
| Pessoa e contato | Family relationship; Communication channel type; Communication channel usage type |

Os códigos individuais de cada lista não foram extraídos nesta sessão (consultar EU Vocabularies).

## 3. EQF

| Nível | Knowledge (literal) |
|---|---|
| 1 | "Basic general knowledge" |
| 2 | "Basic factual knowledge of a field of work or study" |
| 3 | "Knowledge of facts, principles, processes and general concepts, in a field of work or study" |
| 4 | "Factual and theoretical knowledge in broad contexts within a field of work or study" |
| 5 | "Comprehensive, specialised, factual and theoretical knowledge within a field of work or study and an awareness of the boundaries of that knowledge" |
| 6 | "Advanced knowledge of a field of work or study, involving a critical understanding of theories and principles" |
| 7 | "Highly specialised knowledge, some of which is at the forefront of knowledge in a field of work or study, as the basis for original thinking and/or research" |
| 8 | "Knowledge at the most advanced frontier of a field of work or study and at the interface between fields" |

Colunas Skills e Responsibility and autonomy: ver S-UE-07. [I] Saídas típicas do ensino secundário europeu ficam nos níveis 3–4, mas a referenciação é nacional e não foi verificada país a país.

## 4. DigComp 3.0

Níveis de proficiência: **Basic, Intermediate, Advanced, Highly advanced** [S-UE-10].

| Código | Área / competência |
|---|---|
| 1 | Information search, evaluation and management |
| 1.1 | Browsing, searching and filtering information |
| 1.2 | Evaluating information |
| 1.3 | Managing information |
| 2 | Communication and collaboration |
| 2.1 | Interacting through and with digital technologies |
| 2.2 | Sharing through digital technologies |
| 2.3 | Engaging in citizenship through digital technologies |
| 2.4 | Collaborating through digital technologies |
| 2.5 | Digital behaviour |
| 2.6 | Managing digital identity |
| 3 | Content creation |
| 3.1 | Developing digital content |
| 3.2 | Integrating and re-elaborating digital content |
| 3.3 | Copyright and licences |
| 3.4 | Computational thinking and programming |
| 4 | Safety, wellbeing and responsible use |
| 4.1 | Protecting devices |
| 4.2 | Protecting personal data and privacy |
| 4.3 | Supporting wellbeing |
| 4.4 | Protecting the environment |
| 5 | Problem identification and solving |
| 5.1 | Identifying and solving technical problems |
| 5.2 | Identifying needs and digital technological responses |
| 5.3 | Identifying creative solutions using digital technologies |
| 5.4 | Identifying and addressing digital competence needs |

[I] Em relação à 2.2, a 3.0 renomeia áreas (ex.: "Information and data literacy" → "Information search, evaluation and management"; "Safety" → "Safety, wellbeing and responsible use") e introduz 3.4 "Computational thinking and programming" no lugar de "Programming". Os nomes da 2.2 vêm de conhecimento prévio e não foram reconferidos.

## 5. LifeComp, GreenComp, DigCompEdu

Ver [fichas/eu-digcompedu-lifecomp-greencomp.md](fichas/eu-digcompedu-lifecomp-greencomp.md) (listas completas com códigos P1–L3 do LifeComp e as 12 competências do GreenComp).

## 6. Outros termos

| Termo | Significado | Fonte |
|---|---|---|
| NQF | National Qualifications Framework, referenciado ao EQF | S-UE-07, S-UE-02 |
| QDR | Qualification Dataset Register: registro para publicar qualificações e oportunidades no portal Europass | S-UE-01 |
| ECTS credit | 25–30 h de trabalho; 60 créditos/ano | S-UE-18 |
| ISCED / ISCED-F | classificações UNESCO de nível e área (ficha em `internacional/`) | S-UE-02 |
| Eurypedia | enciclopédia Eurydice dos sistemas nacionais | S-UE-20 |
