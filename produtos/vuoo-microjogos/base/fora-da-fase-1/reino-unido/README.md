# Reino Unido

**Estado:** standby (referência). Documentado para provar que um adaptador britânico futuro cabe sem mudar o Core; sem detalhamento campo a campo. Convenções em [../_convencoes.md](../../_convencoes.md). Pesquisa de 2026-11-05.

## Escopo

§3.4 do [briefing](../../padroes-README.md), separando as quatro nações. Inglaterra: CBDS, DfE standards, School Census, identificadores, National Curriculum, SEND Code of Practice/EHC plan. Escócia: CfE, ScotXed pupil census, SCN, ASN. País de Gales: Curriculum for Wales, PLASC, ALN/IDP. Irlanda do Norte: currículo e censo (curto). UK: UK GDPR, DPA 2018, Data (Use and Access) Act 2025, ICO Children's Code.

## Resumo em 10 linhas

1. Não existe "sistema escolar do Reino Unido": são quatro, com identificadores, censos, currículos e vocabulários de necessidade distintos.
2. Inglaterra: o **CBDS** (planilha, maio/2026, 837 itens `N00001…`, code sets `CSnnn`) é o dicionário que todas as coletas do DfE referenciam; obrigatório na prática para fornecedores de MIS.
3. O **School Census** inglês é trimestral, em XML, com níveis escola e aluno; base legal s.537A Education Act 1996.
4. Turma só aparece como **agregado** (primárias) ou turma de registro (Escócia): o vínculo aluno–turma–professor não é dado nacional.
5. Matrícula tem **tipo de registro** (único, principal, subsidiário, convidado): o aluno pode estar em duas escolas ao mesmo tempo.
6. Identificadores com dígito verificador e escopo: **UPN** (Inglaterra e País de Gales, só uso educacional), **ULN** (≥14, vitalício), **SCN** (Escócia), **URN**/**LAESTAB**/**UKPRN** (escola/provedor).
7. SEN inglês = **provisão** (N/K/E) + **tipo** ranqueado (14 códigos, máx. 2) + **EHC plan** com seções legais A–K mantido pela LA.
8. País de Gales codifica **quem mantém o IDP** (escola × LA); Escócia registra **motivos de apoio amplos** (cuidador jovem, luto, criança acolhida, EAL) separados de deficiência e de plano.
9. Nenhum currículo das quatro nações é legível por máquina nem tem objetivos codificados; Inglaterra revisa o seu (previsão 2027/2028, não verificada).
10. Privacidade: AADC (15 padrões) e, desde 2026, o dever de "children's higher protection matters" (DUAA 2025 s.81).

## O que um adaptador UK exigiria

- **Um adaptador por nação** sobre um núcleo comum (identidade, privacidade), não um adaptador "UK". [I]
- C.IDN com vários esquemas por pessoa e por escola, vigência, status (temporário), identificador composto (LAESTAB) e **uso permitido**.
- C.ENR com `registration_kind` (dual registration) e transferências/managed moves; exportação **CTF**.
- C.SUP/C.PLN com: nível de apoio com vigência, categoria local ranqueada (C.VOC do adaptador), estatuto de deficiência separado, plano com mantenedor, seções e ciclo de vida.
- C.EVT de presença por **sessão** (meio dia) com motivo codificado.
- C.PRG com ano e estágio separados; C.CMP com nível curricular (CfE) distinto do estágio.
- Gerador de arquivos de coleta (XML) por nação a partir do Core; validação delegada ao adaptador (dígitos verificadores, regras cruzadas).
- Nada exige mudar o Core, **desde que** as candidatas UK-C1 a UK-C4 e UK-C7 de [questoes-abertas.md](questoes-abertas.md) sejam incorporadas como atributos. [I]

## Índice

| Arquivo | Conteúdo |
|---|---|
| [fichas/uk-eng-cbds.md](fichas/uk-eng-cbds.md) | CBDS (Inglaterra) |
| [fichas/uk-eng-school-census.md](fichas/uk-eng-school-census.md) | School Census 2026–27 e CTF |
| [fichas/uk-eng-dfe-standards.md](fichas/uk-eng-dfe-standards.md) | standards.education.gov.uk |
| [fichas/uk-identificadores.md](fichas/uk-identificadores.md) | UPN, ULN, UCI, SCN, TRN, URN, LAESTAB, UKPRN |
| [fichas/uk-eng-national-curriculum.md](fichas/uk-eng-national-curriculum.md) | National Curriculum |
| [fichas/uk-eng-send-ehcp.md](fichas/uk-eng-send-ehcp.md) | SEND Code of Practice, EHC plan, SEN como dado |
| [fichas/uk-sco-cfe-census.md](fichas/uk-sco-cfe-census.md) | Escócia: CfE, ScotXed, ASN |
| [fichas/uk-wal-cfw-plasc-aln.md](fichas/uk-wal-cfw-plasc-aln.md) | País de Gales: CfW, PLASC, ALN/IDP |
| [fichas/uk-ni-curriculum-census.md](fichas/uk-ni-curriculum-census.md) | Irlanda do Norte (curto) |
| [fichas/uk-gdpr-dpa-childrens-code.md](fichas/uk-gdpr-dpa-childrens-code.md) | UK GDPR, DPA 2018, DUAA 2025, Children's Code |
| [modelo-de-dados.md](modelo-de-dados.md) | Estruturas de coleta das quatro nações e comparação |
| [terminologia.md](terminologia.md) | Code sets com códigos (SEN, matrícula, ano, frequência, ASN, ALN) |
| [cobertura.md](cobertura.md) | Matriz referência × D1–D8 |
| [crosswalk-core.md](crosswalk-core.md) | Conceito UK → C.xxx |
| [questoes-abertas.md](questoes-abertas.md) | Candidatos ao Core, lacunas, conflitos |
| [evidencias.md](evidencias.md) | Registro de fontes |

## Já analisado em `conhecimento/` (citado, não reescrito)

`psg.legal.gdpr-k-and-coppa` (AADC e GDPR-K).
