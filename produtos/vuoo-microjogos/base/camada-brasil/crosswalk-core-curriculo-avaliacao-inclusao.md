# Crosswalk: conceitos brasileiros de currículo, avaliação e inclusão → entidades provisórias do Core

> Alvos: entidades de [../_convencoes.md](../_convencoes.md) §4. Tipos de equivalência: **exata**, **aproximada**, **parcial**, **mais ampla** (o conceito local é mais amplo que o alvo), **mais restrita**, **inexistente**. Nenhuma equivalência foi declarada só por semelhança de nome; a coluna "Por quê" diz o critério. Data: 2026-11-05.

## Currículo (D2, D4)

| Conceito local | Fonte | Alvo Core | Equivalência | Por quê / perda |
|---|---|---|---|---|
| BNCC (documento) | Res. CNE/CP 2/2017 e 4/2018 | C.CFW | exata | documento curricular versionado |
| Complemento de Computação | Res. CNE/CEB 1/2022 | C.CFW (com `derivadoDe` BNCC, tipo complemento) | exata | documento próprio, organização própria |
| Currículo Paulista | Del. CEE-SP | C.CFW (esfera estadual, `derivadoDe` BNCC) | exata | idem; a derivação é C.CAS |
| Parâmetros dos IFAs (Anexo) | Res. CNE/CEB 4/2025 | C.CFW | aproximada | é parte de uma resolução, não documento curricular autônomo; itens sem código |
| Matriz de referência do Saeb | Inep | C.CFW (tipo matriz) | aproximada | é framework de avaliação, não de ensino; versões coexistem (2001 e BNCC) |
| Edição do texto | vuoo-base v1.1 (`bncc-2018`, `bncc-computacao-2022`), bncc-dados | C.CFW.version | parcial | o Core precisa distinguir edição do texto, ato e versão do dataset; uma só "versão" perde informação |
| Habilidade (EF, EM) | BNCC | C.CMP | exata | unidade de aprendizagem com código |
| Objetivo de aprendizagem e desenvolvimento (EI) | BNCC | C.CMP | exata | idem, organizado por campo × grupo etário |
| Objeto de conhecimento | BNCC | C.CMP (tipo conteúdo) | aproximada | não é resultado de aprendizagem; associado n:n às habilidades |
| Competência geral / específica | BNCC | C.CMP | aproximada | nível mais alto; no EF sem vínculo com habilidade |
| Unidade temática, prática de linguagem, campo de atuação, eixo, campo de experiências, "linguagens" (CP) | BNCC, CP | C.CMP (nó organizador) | parcial | o Core não tem tipo "nó organizador"; requer `kind` controlado |
| Área do conhecimento | BNCC, DCNEM art. 17 | C.CMP (organizador) **e** agrupamento de C.SUB | parcial | papel duplo: estrutura do currículo e agrupamento de componentes |
| Componente curricular (BNCC) | BNCC | C.SUB | aproximada | o componente do documento curricular não é o componente ofertado pela rede ("Redação e Leitura" ⊂ LP) |
| Componente de rede (Redação e Leitura, Educação Financeira) | Res. SEDUC 84/2024 | C.SUB + C.CAS (cobertura) | parcial | cobre parte das habilidades de outro componente |
| Código BNCC (`EF67LP08`) | BNCC | C.IDN / `notation` em C.CMP | mais restrita | não é identificador único (forma impressa diferente, ex. `EF05CO011`; reuso e desdobramento no CP) |
| Habilidade CP reanuada (`EF01AR01`) | CP | C.CMP + C.CAS `derivaDe` | — | relação 1:n com a BNCC |
| Habilidade CP desdobrada (`EF01LP10A`) | CP | C.CMP + C.CAS `derivaDe` | — | parte de uma habilidade |
| Habilidade CP criada (`*`) | CP | C.CMP | — | sem C.CAS de origem |
| Progressão por ano/bloco | BNCC | atributo de C.CMP (anos) | parcial | não é pré-requisito; C.CAS `prerequisito` **inexistente** na fonte |
| Formação Geral Básica | Lei 14.945, DCNEM | C.PRG (parte do programa) | aproximada | é carga e conjunto de componentes, não programa autônomo |
| Itinerário formativo (IFA, FTP) | Lei 14.945, DCNEM, Res. 4/2025 | C.PRG (percurso escolhido) | aproximada | envolve escolha do estudante e oferta por escola |
| Eixo estruturante do IFA | Res. 4/2025 art. 11 | C.VOC | exata | vocabulário fechado de 4 valores |
| Regime curricular por coorte | DCNEM arts. 39 e 42 | **inexistente** | inexistente | candidato a entidade (`AdocaoCurricular`, Q-CUR-05) |
| Base comum × parte diversificada | DCN | C.CFW (composição) | parcial | o Core precisa compor frameworks com proveniência por item |

## Avaliação (D5)

| Conceito local | Fonte | Alvo Core | Equivalência | Por quê / perda |
|---|---|---|---|---|
| Saeb, SARESP (programa) | Inep, Seduc-SP | C.ASM (agrupador) | aproximada | o Core não distingue programa × edição × instrumento; necessário |
| Edição (Saeb 2025) | Portaria Inep 435/2025 | C.ASM | aproximada | idem |
| Teste cognitivo por área e etapa | Portaria 435 | C.ASM | exata | instrumento |
| Questionário contextual | Portaria 435 | C.ASM (tipo questionário) | parcial | não produz proficiência; dados de contexto |
| Descritor (`D1`) | matriz 2001 | C.CMP (de matriz) | aproximada | identificador local à matriz (etapa × área) |
| Habilidade da matriz BNCC | matriz 2022 | C.CMP (de matriz) | aproximada | sem código; posição eixo × eixo cognitivo |
| Item | Saeb | C.ITM | exata | não divulgado (art. 25) |
| Escala de proficiência | Inep | C.VOC + métrica (C.RES) | parcial | o Core precisa de entidade Escala com métrica e comparabilidade |
| Nível de proficiência (Saeb) | Inep | C.VOC.Code | exata | intervalo + descrição |
| Nível SARESP / classificação Insuficiente-Suficiente-Avançado | SARESP | C.VOC.Code (outro esquema) | exata | múltiplos esquemas sobre o mesmo valor |
| Padrão de alfabetização (743) | CNCA/Inep | C.VOC.Code (corte binário) | exata | idem |
| Proficiência individual | avaliação estadual/rede | C.RES | exata | |
| Resultado agregado de escola/rede | Saeb | C.RES (sujeito agregado) | parcial | o Core precisa de sujeito agregado e regras de divulgação |
| Sistema de avaliação da rede (nota, menção, conceito) | CMDEB | C.VOC (esquema de C.RES) | exata | |
| Atendimento especializado na prova | Portaria 435 art. 17 | C.SUP (acomodação aplicada) | aproximada | concedido pelo cadastro do Censo, não pelo plano |
| Eixo cognitivo (Reconhecer…Produzir) | matriz BNCC | C.VOC | exata | taxonomia de 4 valores |

## Inclusão (D7)

| Conceito local | Fonte | Alvo Core | Equivalência | Por quê / perda |
|---|---|---|---|---|
| Barreira (6 tipos) | LBI art. 3 IV | C.SUP (barreira) | exata | |
| Adaptação razoável | LBI art. 3 VI | C.SUP (acomodação) | aproximada | conceito jurídico com limite de "ônus desproporcional"; o Core não modela o limite |
| Tecnologia assistiva, CAA | LBI; Port. 421 art. 10 II | C.SUP (recurso) | exata | |
| Profissional de apoio escolar, intérprete de Libras, guia-intérprete | Port. 421 arts. 10 e 12 | C.SUP (apoio humano) + C.STF | parcial | é apoio **e** pessoa/papel |
| Nível de apoio 1–3 (SP) | Res. SEDUC 129 Anexo II | C.SUP.intensidade | aproximada | escala local, sem equivalência validada com SIS-C nem com níveis do DSM-5 |
| Estudo de caso / API (SP) | Dec. 12.686 art. 11; Dec. SP 67.635 art. 8 | **inexistente** (entre C.SUP e C.PLN) | inexistente | candidato a entidade (Q-INC-01) |
| PAEE | Port. 421 art. 10 | C.PLN (seção) | parcial | é o registro do estudo de caso e dos serviços, não plano de ensino |
| PEI | Port. 421 art. 11; SP Anexo IV | C.PLN (seção) | aproximada | em SP é por componente × bimestre, ligado a habilidades do CP |
| Plano de AEE (Res. 4/2009) | CNE | C.PLN | aproximada | nome anterior; alcance restrito ao AEE |
| Devolutiva à família | Port. 421 art. 11 IV; SP Anexo V | C.EVD + C.GRD | parcial | registro com ciência do responsável |
| Público da educação especial / categoria CMDEB | LDB art. 58; CMDEB | **sem alvo adequado**; aproximável a atributo de C.LRN com sensibilidade alta | inexistente | não é necessidade de apoio (P5); entidade administrativa separada |
| Laudo, relatório médico, CIPTEA | Lei 12.764; Res. SEDUC 129 | C.EVD (documento) | parcial | evidência opcional, nunca pré-condição |
| Transtorno de aprendizagem (Lei 14.254) | Lei 14.254 | C.SUP (sem elegibilidade) | parcial | apoio sem plano formal obrigatório |
| Autorização para contato com terapeuta | SP Anexo II | C.CNS | aproximada | consentimento de compartilhamento dentro do plano |

## Privacidade (D8, parte legal)

| Conceito local | Fonte | Alvo Core | Equivalência | Por quê |
|---|---|---|---|---|
| Base legal (arts. 7 e 11) | LGPD | C.CNS (LegalBasis) | mais ampla | C.CNS é "Consent / LegalBasis"; consentimento é só uma das bases |
| Consentimento parental específico e em destaque | LGPD art. 14 §1 | C.CNS + C.GRD | exata | |
| Avaliação de melhor interesse | Enunciado ANPD 1/2023 | atributo de C.CNS | parcial | documento de justificativa |
| Dado sensível (saúde) | LGPD art. 5 II | atributo de sensibilidade (C.VOC) por campo | parcial | o Core não prevê classificação por campo |
| Registro de operações, RIPD | LGPD arts. 37–38 | C.PRV | parcial | |
| Revisão de decisão automatizada | LGPD art. 20 | C.PRV (inferência) | parcial | |
| Privacidade por padrão; vedação de perfilamento publicitário | Lei 15.211 arts. 7, 22, 26 | política de configuração (fora do modelo de dados) | inexistente | regra de produto |
