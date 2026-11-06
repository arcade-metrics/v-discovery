# Questões abertas: Reino Unido

## Candidatos a entidade/atributo do Core

| # | Conceito | Origem | Problema | Proposta [I] |
|---|---|---|---|---|
| UK-C1 | Tipo de registro da matrícula (único, principal, subsidiário, convidado) | CBDS CS007 | C.ENR só tem vigência e situação | atributo `registration_kind`; permitir 2 C.ENR ativos com papéis distintos |
| UK-C2 | Estatuto de deficiência (avaliado/declarado) separado de necessidade e de plano | ScotXed | C.SUP mistura necessidade e condição | atributo opcional de C.SUP ou entidade C.DIS de acesso restrito |
| UK-C3 | Ranking de necessidades | CBDS N00024 | C.SUP sem ordem | atributo `rank` |
| UK-C4 | Plano com mantenedor e ciclo de vida | EHC (LA), IDP (escola/LA), CSP | C.PLN sem `maintained_by` nem eventos | `maintained_by` (C.ORG), seções tipadas, eventos (pedido, emissão, revisão, emenda, cessação, transferência) |
| UK-C5 | Evento disciplinar (suspensão, exclusão, managed move) | CBDS | sem alvo | entidade de extensão ligada a C.ENR |
| UK-C6 | Elegibilidade a benefício (FSM, pupil premium) | CBDS | sem alvo | extensão do adaptador (C.VOC + período) |
| UK-C7 | Uso permitido do identificador | UPN | C.IDN sem finalidade | atributo `permitted_use` |
| UK-C8 | Presença por sessão (meio dia) com motivo codificado | CS066 | C.EVT genérico | perfil de C.EVT "attendance" com unidade de sessão e motivo C.VOC |
| UK-C9 | Nível curricular alcançado distinto do estágio de matrícula | CfE | C.PRG vs C.RES | modelar "nível alcançado" como C.RES sobre C.CMP de nível |

## Lacunas de verificação

1. **Datas dos censos ingleses 2026–27** (Anexo C da especificação) não extraídas.
2. **Licença** do CBDS e das especificações (presumivelmente OGL) não confirmada.
3. **Irlanda do Norte**: especificação do censo, identificador de aluno e lista de tipos de SEN não encontrados; reforma do framework SEN não verificada.
4. **Curriculum for Wales**: seis áreas, 27 statements of what matters [não citado], progression steps 1–5: conhecimento prévio, páginas hwb devolveram 404.
5. **National Curriculum revisado** (publicação prevista primavera/2027, ensino em set/2028): só fontes secundárias; PDF da resposta oficial não aberto.
6. **Reforma SEND na Inglaterra** pós-2025 (Schools White Paper): não verificada; pode alterar códigos de provisão.
7. **DPA 2018 s.9** (idade 13) e **DUAA 2025 s.81**: textos não abertos na legislation.gov.uk.
8. **GIAS** (glossário e API) bloqueou acesso (403); definição formal de LAESTAB apoiada em API de estatísticas e páginas de estabelecimento.
9. **CTF 26**: especificação não aberta; só o vínculo ao CBDS.
10. **Escócia**: código de prática "Supporting Children's Learning" 4ª edição (2026) visto só em resultado de busca; códigos numéricos das categorias ASN além de "10" não extraídos.

## Conflitos e ambiguidades

- "Class" no CBDS é **registration group** (N00091: "Class equates to registration group"), não oferta de disciplina. Nome igual a "turma", conceito mais restrito.
- ADHD é categoria própria no País de Gales (sob SPLD) e não existe em CS071 da Inglaterra; DS existe na Inglaterra e não no País de Gales. Equivalência entre nações é parcial.
- SEMH (Inglaterra) × BESD (País de Gales) × SEBD (Escócia): nomes próximos, definições não comparadas.
- "Year 8" significa idades diferentes na Inglaterra e na Irlanda do Norte (primária de 7 anos na NI).
