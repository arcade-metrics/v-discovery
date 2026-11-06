# União Europeia

**Estado:** standby (referência). Documentado para provar que um adaptador UE futuro cabe sem mudar o Core; sem detalhamento campo a campo. Convenções em [../_convencoes.md](../../_convencoes.md). Pesquisa de 2026-11-05.

## Escopo

Referenciais comuns europeus (§3.2 do [briefing](../../padroes-README.md)): ELM, EDC/Europass, EQF, ESCO (complemento), DigComp 2.2/3.0, DigCompEdu, LifeComp, GreenComp, ECTS, EWP/EMREX; competência nacional (Eurydice, ISCED); GDPR art. 8 e AI Act (apontamento). Fora: padrões nacionais de cada Estado-membro.

## Resumo em 10 linhas

1. A UE **não** tem sistema escolar nem modelo de dados escolar comum; organização e dados da educação básica são nacionais (Eurydice descreve 40 sistemas).
2. O único modelo de dados formal é o **ELM** (OWL + SHACL + JSON-LD; v3.3 vigente; GitHub arquivado na 3.1, licença EUPL-1.2).
3. O ELM modela **aprendizagem, avaliação, qualificação e credencial**; confirma-se que **não** modela turma, matrícula, calendário, horário nem oferta com professor.
4. Padrão central do ELM: **Especificação × Instância (Claim)** ligadas por `specifiedBy`, com concessão (`awardedBy`) como proveniência.
5. Quase todo atributo categórico do ELM é `skos:Concept` de uma das **37 listas controladas** Europass (EQF, ISCED, DigComp, competências-chave...).
6. EDC = claims ELM dentro de **W3C VC**, com selo eletrônico eIDAS obrigatório.
7. EQF: 8 níveis × (conhecimento, habilidades, responsabilidade e autonomia); é nível de **qualificação**, não ano escolar.
8. DigComp 3.0 (nov/2025): 5 áreas, 21 competências, **4 níveis** (a 2.2 tinha 8); dados em planilha e LOD.
9. LifeComp (9 competências, P1–L3) e GreenComp (12 competências) não têm escala de níveis; DigCompEdu está em revisão até 2027.
10. Lacunas do Core reveladas: qualificação, escala de proficiência, crédito e a regra especificação × instância.

## O que um adaptador UE exigiria

- **Por Estado-membro**: identificadores nacionais de aluno/escola, estrutura de anos e etapas, códigos de necessidades educacionais especiais, idade de consentimento digital (13–16). Isso é o grosso do trabalho e está fora desta pasta. [I]
- **Comum europeu**: exportar C.CRD como EDC (ELM + VC + selo eIDAS); mapear C.PRG para ISCED e qualificações finais para EQF/NQF como C.VOC; importar DigComp/LifeComp/GreenComp/ESCO como C.CFW versionados; alinhar via C.CAS.
- **Governança**: C.CNS parametrizado por jurisdição; proveniência de decisões de IA (AI Act).
- **Nada disso exige mudar o Core**, desde que ele adote: identificador com esquema (C.IDN), vocabulário SKOS externo (C.VOC), framework versionado (C.CFW) e as candidatas UE-C1/UE-C2 de [questoes-abertas.md](questoes-abertas.md). [I]

## Índice

| Arquivo | Conteúdo |
|---|---|
| [fichas/eu-elm.md](fichas/eu-elm.md) | European Learning Model (análise principal) |
| [fichas/eu-edc-europass.md](fichas/eu-edc-europass.md) | Europass e European Digital Credentials |
| [fichas/eu-eqf.md](fichas/eu-eqf.md) | EQF |
| [fichas/eu-esco.md](fichas/eu-esco.md) | ESCO (complemento; dono: `iop.comp.esco`) |
| [fichas/eu-digcomp.md](fichas/eu-digcomp.md) | DigComp 2.2 e 3.0 |
| [fichas/eu-digcompedu-lifecomp-greencomp.md](fichas/eu-digcompedu-lifecomp-greencomp.md) | DigCompEdu, LifeComp, GreenComp |
| [fichas/eu-ects-ewp-emrex.md](fichas/eu-ects-ewp-emrex.md) | ECTS, EWP, EMREX/ELMO (superior, curto) |
| [fichas/eu-competencia-nacional.md](fichas/eu-competencia-nacional.md) | Competência nacional, Eurydice, ISCED |
| [fichas/eu-gdpr-ai-act.md](fichas/eu-gdpr-ai-act.md) | GDPR, AI Act, EN 301 549 (apontamentos) |
| [modelo-de-dados.md](modelo-de-dados.md) | Entidades e atributos do ELM; estrutura dos frameworks |
| [terminologia.md](terminologia.md) | Definições ELM, 37 listas Europass, EQF, DigComp 3.0 |
| [cobertura.md](cobertura.md) | Matriz referência × D1–D8 |
| [crosswalk-core.md](crosswalk-core.md) | Conceito UE → C.xxx |
| [questoes-abertas.md](questoes-abertas.md) | Candidatos a entidade do Core, lacunas |
| [evidencias.md](evidencias.md) | Registro de fontes |

## Já analisado em `conhecimento/` (citado, não reescrito)

`iop.comp.esco` (ESCO), `iop.cred.verifiable-credentials` (VC), `psg.legal.gdpr-k-and-coppa` (GDPR art. 8), `psg.ai.eu-ai-act-and-brazil` (AI Act), `acs.std.procurement-en-301-549-and-section-508` (EN 301 549).
