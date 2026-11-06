# Crosswalk Reino Unido → Core provisório

Alvos de [../_convencoes.md](../../_convencoes.md) §4. Todo mapeamento é **[I]**, apoiado nas definições de [terminologia.md](terminologia.md).

| Conceito local | Nação / fonte | Alvo Core | Tipo | Observação |
|---|---|---|---|---|
| Local Authority (LA) | ENG/WAL, CBDS N00216 | C.ORG (kind=autoridade local) | aproximada | também mantém EHC plan/IDP e é "home LA" do aluno |
| School / Establishment | todos | C.ORG (kind=escola) | exata | |
| Academy trust / establishment group (GIAS) | ENG | C.ORG (hierarquia) | aproximada | não está no CBDS |
| URN / LAESTAB / UKPRN / SCN / UPN / ULN / UCI / TRN | CBDS, ScotXed | C.IDN | exata | com `scheme`, vigência, status, uso permitido |
| Census term (autumn/spring/summer) | ENG | C.SES | aproximada | termo de coleta, não necessariamente o termo escolar (escolas de 6 termos) |
| Year group (CS086) | ENG/WAL/NI | C.PRG (grade level) | aproximada | `M`, `X` e anos 12–14 não têm análogo simples |
| Key stage (CS037) | ENG, NI | C.PRG (etapa) | aproximada | agrupa anos; turma pode ser `M` |
| Stage P1–S6 | SCO | C.PRG | aproximada | |
| Nível CfE (Early–Fourth) | SCO | C.CMP (nível do framework) / C.RES (nível alcançado) | parcial | não é etapa de matrícula |
| Progression step | WAL | C.CMP (marco de progressão) | aproximada | [I] estrutura não verificada |
| Class (censo, agregado) | ENG | C.GRP (kind=turma) | parcial | só contagens e tipo; sem membros |
| Registration class | SCO | C.GRP (kind=turma de registro) | aproximada | |
| SEN unit / resourced provision | ENG | C.GRP ou C.LOC + C.SUP | parcial | é provisão designada, não turma comum |
| Enrolment status C/M/S/G/P | ENG CS007 | C.ENR (situação + tipo de registro) | parcial | o Core precisa de `registration_kind` (único, principal, subsidiário, convidado) |
| Alternative provision placement | ENG | C.ENR (em outra C.ORG) | aproximada | |
| Managed move | ENG | C.ENR (transferência com motivo) | aproximada | |
| Contact / Relationship (CS012) | ENG | C.GRD | aproximada | inclui contatos não familiares (médico, assistente social); responsabilidade parental é booleano separado |
| Attendance mark por sessão (CS066) | ENG | C.EVT (presença) ligado a C.SCH | parcial | unidade = meio dia; motivo codificado |
| Pupil SEN provision N/K/E | ENG | C.SUP (nível de apoio) | aproximada | estado com vigência |
| Pupil SEN type + ranking | ENG | C.SUP (categoria local, ordenada) | aproximada | categoria em C.VOC do adaptador |
| EHC plan (A–K) | ENG | C.PLN | aproximada | `maintained_by` = LA; seções tipadas; ciclo de vida |
| ALN provision N/C/L | WAL | C.SUP + C.PLN | aproximada | o código codifica quem mantém o plano |
| IDP | WAL | C.PLN | aproximada | |
| Additional needs (DYSL…) | WAL | C.SUP | aproximada | |
| ASN category (motivo) | SCO | C.SUP | exata no espírito (barreira/necessidade de apoio) | inclui fatores sociais |
| CSP / IEP / Child's Plan | SCO | C.PLN | aproximada | CSP é estatutário, multi-agência |
| AssessedDisabled / DeclaredDisabled | SCO | **sem alvo** | inexistente | estatuto de deficiência distinto de necessidade e de plano |
| Nature of additional support | SCO | C.SUP (recurso/serviço de apoio) | parcial | quem presta o apoio (setor) |
| SEN statement / stage | NI | C.PLN / C.SUP | aproximada | |
| National Curriculum (framework) | ENG | C.CFW | exata | versão 2014; revisão prevista |
| Programme of study / attainment target | ENG | C.CMP | aproximada | sem identificador oficial |
| Subject (CS063 etc.) | ENG | C.SUB | aproximada | vários code sets de disciplina (CS013, CS049, CS063, CS095) para usos distintos |
| CfE curriculum area / experiences and outcomes / benchmarks | SCO | C.SUB / C.CMP / C.RES-escala | aproximada | |
| Area of Learning and Experience / statement of what matters | WAL | C.SUB / C.CMP | aproximada | |
| Teacher (TRN), School Workforce | ENG | C.STF | aproximada | workforce é coleta separada |
| Exclusion / suspension | ENG | **sem alvo** | inexistente | evento disciplinar com sessões e motivos; candidato a extensão de C.ENR ou entidade própria |
| Free school meals / pupil premium | ENG | **sem alvo** | inexistente | elegibilidade a benefício com período; atributo do adaptador |
| Lawful basis (s.537A EA 1996) | ENG | C.CNS | aproximada | base legal de coleta, não consentimento |
| Children's higher protection matters / AADC | UK | C.CNS + política de produto | parcial | requisito de design, não dado |
| CTF (Common Transfer File) | ENG | exportação de C.LRN + C.ENR + C.SUP + C.RES | — | formato de troca, não entidade |
