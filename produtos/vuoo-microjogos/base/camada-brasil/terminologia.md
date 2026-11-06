# Terminologia e vocabulários controlados: Brasil (organização e dados)

Dono: frente "organização e dados". Este arquivo reúne os **códigos oficiais** que o adaptador Brasil precisa carregar para D1, D3 e D8, com a fonte de cada tabela. Quando o mesmo conceito tem códigos diferentes no **Censo Escolar (INEP)** e no **CMDEB/MEC Gestão Presente**, as duas colunas aparecem lado a lado: os dois sistemas **não usam o mesmo código** para a mesma coisa, e isso é a principal armadilha do adaptador.

Fontes (detalhe em [evidencias-organizacao.md](evidencias-organizacao.md)):

- **Censo 2026**: Layout de Importação e Exportação 2026, versão V5 [E02], tabelas auxiliares 2026 [E04], Caderno de Conceitos 2026 [E06].
- **Censo SA 2025**: Layout da Situação do Aluno 2025 [E09] e Caderno da 2ª etapa 2025 [E10].
- **CMDEB**: Portaria MEC 832/2025, transcrita em [cmdeb/](cmdeb/README.md) [E31]; **API v2**: OpenAPI do SGP [E36].

Os códigos são reproduzidos como publicados (inclusive saltos de numeração). Domínios CMDEB não repetidos aqui ficam em [cmdeb/10-estudante.md](cmdeb/10-estudante.md), [cmdeb/20-trajetoria.md](cmdeb/20-trajetoria.md), [cmdeb/30-profissionais.md](cmdeb/30-profissionais.md) e [cmdeb/40-instituicoes.md](cmdeb/40-instituicoes.md).

Acesso a todas as fontes: 2026-11-05.

---

## 1. Conceitos (definições oficiais resumidas)

| Conceito | Definição | Fonte |
|---|---|---|
| Censo Escolar | Pesquisa estatística declaratória anual do INEP, em regime de colaboração; fornecimento obrigatório para escolas públicas e privadas (Decreto 6.425/2008, art. 4º, conforme o Caderno) | E06 p. 2; E22 |
| Data de referência | Última quarta-feira de maio (Portaria MEC 264/2007); em 2026, 27/05/2026 | E07 |
| 1ª etapa (Matrícula Inicial) | Coleta de escola, gestor, turma, aluno e profissional escolar em sala de aula, com a realidade na data de referência | E07 |
| 2ª etapa (Situação do Aluno) | Coleta de rendimento e movimento dos alunos declarados na 1ª etapa; base das taxas de rendimento e do Ideb | E10 §1 |
| Ano letivo | "Período do ano em que são desenvolvidas as atividades escolares"; no Censo, início até a data de referência | E06 p. 16; E10 §3 |
| Turma | Unidade declarada no registro 20, com tipo, mediação, horário semanal, etapa e organização; o aluno se vincula a ela no registro 60 (não existe registro "matrícula" separado na importação) [I a partir de E02] | E02 abas 20, 60 |
| Tipo de turma | Curricular (etapa de ensino); Curricular com atividade complementar; Atividade complementar; AEE | E06 p. 49 |
| Matrícula (Censo) | Vínculo aluno × turma; recebe "Código da Matrícula" do INEP, devolvido só na exportação | E02 aba 60 campo 7; E09 aba 90 campo 7 |
| Matrícula (CMDEB) | Registro próprio (`ID_SGP_MATRICULA`) com etapa, ano, datas e situação; vínculo à turma é opcional no registro e feito por "enturmação" | E31; E36 |
| AEE | Atividade pedagógica complementar (deficiência e TEA) ou suplementar (AH/SD); "a matrícula no AEE não substitui a matrícula e a frequência do estudante na classe comum" | E06 p. 49–50 |
| Classe especial | Turma curricular que atende exclusivamente alunos com deficiência, TEA e AH/SD | E06 p. 47 |
| Classe bilíngue de surdos | Libras como L1 e português escrito como L2; não é turma de AEE; sem tradutor-intérprete | E06 p. 47 |
| Unidade vinculada | Unidade em endereço distinto da escola-sede, com prédio próprio, sem ser unidade gestora/orçamentária | E06 p. 17 |
| Órgão regional | Subdivisão administrativa da secretaria de educação (diretoria/regional de ensino) | E06 p. 13 |
| Identificação única (INEP) | Número de 12 caracteres gerado pelo Educacenso no cadastro de aluno, profissional ou gestor; não editável | E06 p. 66 |
| Inue | Identificador Nacional Único do Estudante = CPF, "de uso obrigatório em todas as bases de dados e registros administrativos dos sistemas de ensino" | E21 art. 26 I; E30 art. 7º |
| Rendimento escolar | Resultados dos alunos matriculados no término do ano letivo (aprovado, reprovado, concluinte) | E10 §3 |
| Movimento escolar | Mudança de vínculo após a data de referência e antes do fim do ano letivo (transferido, deixou de frequentar, falecido) | E10 §3 |
| Admissão após | Situação de aluno que ingressou na escola após a data de referência | E10 §3, §4 |

---

## 2. Instituição (escola)

### 2.1 Situação de funcionamento

| Censo 2026 (reg. 00 c3) | Rótulo Censo | CMDEB `SITUACAO_FUNCIONAMENTO_INSTITUICAO` | Rótulo CMDEB |
|---|---|---|---|
| — | — | 0 | Não informado |
| 1 | Em atividade | 1 | Em funcionamento |
| 2 | Paralisada (atividades temporariamente suspensas) | 2 | Paralisada |
| 3 | Extinta (atividades definitivamente encerradas; pública extinta por ato da secretaria) | 3 | Inativada |

Fonte: E02 aba 00; E06 p. 15; [cmdeb/40-instituicoes.md](cmdeb/40-instituicoes.md). "Extinta" × "Inativada": equivalência não declarada por nenhuma fonte; tratada como aproximada [I].

### 2.2 Dependência administrativa

| Código (Censo 00 c21 = CMDEB `DEP_ADMINISTRATIVA_INSTITUICAO`) | Rótulo |
|---|---|
| 0 | Não informado (só CMDEB) |
| 1 | Federal |
| 2 | Estadual |
| 3 | Municipal (Censo: não pode ser 3 quando município = 5300108, Brasília) |
| 4 | Privada |

### 2.3 Localização / zona

| Código | Rótulo | Onde |
|---|---|---|
| 0 | Não informado | só CMDEB |
| 1 | Urbana | Censo (00 c19; 30 c54) e CMDEB |
| 2 | Rural | Censo e CMDEB |

### 2.4 Localização diferenciada (códigos DIFERENTES)

| Conceito | Censo 2026 (00 c20; 30 c55) | CMDEB (`*_LOCALIZACAO_DIFERENCIADA`) |
|---|---|---|
| Não informado | — | 0 |
| Não está em área de localização diferenciada | **7** | **1** |
| Área de assentamento | **1** | **4** |
| Terra indígena | 2 | **3** |
| Comunidade quilombola | **3** | **2** |
| Área onde se localizam povos e comunidades tradicionais | **8** | **5** |

### 2.5 Órgão ao qual a escola pública está vinculada (Censo 00 c22–25, marcação 0/1, pode haver mais de um)

Secretaria de Educação/MEC; Secretaria de Segurança Pública/Forças Armadas/Militar; Secretaria da Saúde/Ministério da Saúde; Outro órgão da administração pública. Dupla/tripla vinculação só se oficializada em legislação (E06 p. 12).

### 2.6 Mantenedora da escola privada (Censo 00 c26–31, marcação 0/1) e categoria (c32)

Mantenedoras: Empresa/grupo empresarial ou pessoa física; Sindicatos, associações, cooperativas; ONG; Instituição sem fins lucrativos; Sistema S; Oscip.

| Categoria da escola privada (c32) | Rótulo |
|---|---|
| 1 | Particular |
| 2 | Comunitária |
| 3 | Confessional |
| 4 | Filantrópica |

### 2.7 Regulamentação e esfera do órgão (Censo 00 c49, c50)

| c49 Regulamentação/autorização | | c50 Esfera do conselho/órgão (V5) | |
|---|---|---|---|
| 0 | Não | 1 | Federal |
| 1 | Sim | 2 | Estadual |
| 2 | Em tramitação | 3 | Municipal |
| | | 4 | Estadual e Municipal |
| | | 6 | Federal SETEC |

A aba "atualizações da versão" registra que em V5 o código 5 ("Federal e Estadual") saiu e entrou 6 ("Federal SETEC") (E02).

### 2.8 Unidade vinculada (Censo 00 c51)

| Código | Rótulo |
|---|---|
| 0 | Sem vínculo com outra instituição |
| 1 | Unidade vinculada a escola de educação básica (exige c52 Código da Escola Sede) |
| 2 | Unidade ofertante de educação superior (exige c53 Código da IES) |

### 2.9 Parceria/convênio com o poder público (Censo 00 c33–46)

Marcação 0/1 de secretaria estadual/municipal responsável e das formas: Termo de colaboração, Termo de fomento, Acordo de cooperação (Lei 13.019/2014), Contrato de prestação de serviço, Termo de cooperação técnica e financeira, Contrato de consórcio público/Convênio de cooperação. Formas permitidas por dependência: Anexo 5 do leiaute (E02).

---

## 3. Turma

### 3.1 Tipo de turma (códigos DIFERENTES)

| Conceito | Censo 2026 (20 c14) | CMDEB `TIPO_TURMA` / API `tipo_turma` |
|---|---|---|
| Não informado | — | 0 |
| Curricular (etapa de ensino) | **6** | **1** |
| Curricular com atividade complementar | **9** | **2** |
| Atividade complementar | **4** | **3** |
| Atendimento educacional especializado (AEE) | **5** | **4** |

Fonte: E02 aba 20 e aba "atualizações da versão"; [cmdeb/20-trajetoria.md](cmdeb/20-trajetoria.md) §2.2; E36 `TurmaCadastroData.tipo_turma`. Mudança estrutural: no leiaute 2025 eram três campos separados (14 Curricular, 15 Atividade complementar, 16 AEE); em 2026 viraram um campo de seleção (E02, aba "atualizações da versão", v1). O adaptador precisa versionar o leiaute por ano.

### 3.2 Tipo de mediação didático-pedagógica

| Código | Censo (20 c6) | CMDEB `TIPO_MEDIACAO_DIDATICO_PEDAGOGICA` |
|---|---|---|
| 0 | — | Não informado |
| 1 | Presencial | Presencial |
| 2 | Semipresencial | Semipresencial |
| 3 | Educação a distância (EaD) | Educação a Distância (EAD) |

Definições: E06 p. 46 (alternância é considerada presencial). Horários da turma só para mediação presencial (E02 aba 20 c7–13).

### 3.3 Local de funcionamento diferenciado da turma (códigos DESLOCADOS)

| Conceito | Censo 2026 (20 c21) | CMDEB `TURMA_LOCALIZACAO` |
|---|---|---|
| Não informado | — | 0 |
| Não está em local diferenciado | **0** | **1** |
| Sala anexa | 1 | 2 |
| Unidade de atendimento socioeducativo | 2 | 3 |
| Unidade prisional | 3 | 4 |

### 3.4 Formas de organização da turma (LDB art. 23)

| Código (Censo 20 c28 = CMDEB `TURMA_FORMA_ORGANIZACAO`) | Rótulo |
|---|---|
| 0 | Não informado (só CMDEB) |
| 1 | Série/Ano (séries anuais) |
| 2 | Períodos semestrais |
| 3 | Ciclo(s) |
| 4 | Grupos não seriados com base na idade ou competência |
| 5 | Módulos |

No Censo: obrigatório para turma curricular, exceto educação infantil (etapas 1, 2, 3 → nulo); combinações etapa × forma no Anexo 6 (ex.: "Períodos semestrais" não é permitido no EF; "Ciclos" não é permitido em EJA e cursos técnicos) (E02). "Alternância" é campo separado no Censo (20 c29, 0/1), não opção de forma. O CMDEB acrescenta quantidade total e atual de etapas da forma de organização (sem equivalente no Censo).

### 3.5 Turno (só CMDEB)

`TURNO_TURMA`: 0 Não informado; 1 Matutino; 2 Vespertino; 3 Noturno; 4 Integral. O Censo **não** tem turno: registra hora de início e fim por dia da semana (`hh:mm-hh:mm`, minutos múltiplos de 5) (E02 aba 20 c7–13).

### 3.6 Organização curricular da turma (ensino médio)

| Conceito | Censo (20 c30–32, marcação 0/1, combináveis) | CMDEB `ORGANIZACAO_CURRICULAR_TURMA` (código único) |
|---|---|---|
| Não informado | — | 0 |
| Formação geral básica (FGB) | c30 = 1 | 1 |
| Itinerário formativo de aprofundamento (IFA) | c31 = 1 | 2 |
| FGB + itinerário formativo | c30 = 1 e c31 = 1 | 3 |
| Itinerário de formação técnica e profissional (IFTP) | c32 = 1 | 4 |
| Não se aplica | (campos nulos fora do EM) | 5 |

A combinação FGB + IFTP (curso técnico integrado) não tem código próprio no CMDEB [I]. Áreas do IFA (Censo 20 c33–36): Linguagens; Matemática; Ciências da natureza; Ciências humanas e sociais aplicadas. Tipo do curso do IFTP (c37): 1 Curso técnico; 2 Qualificação profissional técnica.

### 3.7 Outros marcadores de turma (Censo 2026)

| Campo | Valores |
|---|---|
| 20 c22 Turma de Educação Especial (classe especial) | 0 Não, 1 Sim (só tipo 6 ou 9) |
| 20 c66 Turma de Educação Bilíngue de Surdos | 0 Não, 1 Sim |
| 20 c29 Turma de Formação por Alternância | 0 Não, 1 Sim |
| 20 c15–20 Tipo de atividade complementar | até 6 códigos de 5 dígitos da Tabela de Tipo de Atividade Complementar 2026 (145 atividades em 11 áreas: 1 Cultura, Artes e Educação Patrimonial; 2 Esporte e Lazer; 3 Acompanhamento Pedagógico; 4 Educação em Direitos Humanos, Cidadania e Civismo; 10 Iniciação Científica; 13 Educação Ambiental; 14 Comunicação, Mídias e Cultura Digital; 15 Multiculturalismo; 17 Trabalho e Educação para o consumo, financeira e fiscal; 19 Saúde e Educação Socioemocional; 20 Educação Alimentar e Nutricional) (E04) |

CMDEB tem `OFERTA_EDUCACAO_ESPECIAL` (0 Não informado; 1 Educação Especial na Perspectiva Inclusiva; 2 Educação Bilíngue de Surdos) e a API v2 acrescenta `turma_bilingue` (0/1 Sim/2 Não), fora da Portaria (E36).

### 3.8 Modalidade (só CMDEB como campo)

`MODALIDADE_ENSINO_ESTUDANTE` (na turma): 0 Não informado; 1 Ensino Regular; 2 Educação Especial; 3 EJA; 4 Educação Profissional. No Censo 2026, a modalidade **não é campo**: deriva da etapa (EJA = 69–74, 67), da classe especial (c22) e do itinerário/curso técnico [I a partir de E02 e E04].

---

## 4. Etapa de ensino

### 4.1 Tabela de Etapas 2026 (Censo) com etapa agregada

| Etapa agregada | Código | Etapa de ensino | Idade mín.–máx. do aluno (Anexo 3) | CMDEB aluno | CMDEB turma/instituição |
|---|---|---|---|---|---|
| 301 Educação Infantil | 1 | Creche (0 a 3 anos) | 0–6 | sim | sim |
| | 2 | Pré-escola (4 e 5 anos) | 3–9 | sim | sim |
| | 3 | Unificada (0 a 5 anos) | — (aluno informa 1 ou 2 em "Turma multi") | não na Portaria; **sim** na API v2 | sim |
| 302 Ensino Fundamental | 14 | EF 9 anos – 1º ano | 4–50 | sim | sim |
| | 15 | 2º ano | 5–50 | sim | sim |
| | 16 | 3º ano | 5–50 | sim | sim |
| | 17 | 4º ano | 6–50 | sim | sim |
| | 18 | 5º ano | 7–50 | sim | sim |
| | 19 | 6º ano | 8–50 | sim | sim |
| | 20 | 7º ano | 9–50 | sim | sim |
| | 21 | 8º ano | 10–50 | sim | sim |
| | **41** | 9º ano | 12–50 | sim | sim |
| 303 Multi e correção de fluxo | 22 | EF 9 anos – multi | — (aluno: 14–21, 41) | não | sim |
| | 23 | EF 9 anos – correção de fluxo | — (aluno: 14–21, 41) | não | sim |
| | 56 | EI e EF – multietapa | — (aluno: 1, 2, 14–21, 41) | não | sim |
| 304 Ensino Médio | 25 | EM 1ª série | 12–58 | sim | sim |
| | 26 | 2ª série | 12–58 | sim | sim |
| | 27 | 3ª série | 12–58 | sim | sim |
| | 28 | 4ª série | 12–58 | sim | sim |
| | 29 | Não seriada | 12–58 | sim | sim |
| 305 EM Normal/Magistério | 35–38 | 1ª a 4ª série | 12–58 | sim | sim |
| 306 EJA (fundamental, médio e integrada) | 69 | EJA EF anos iniciais (1º segmento) | 12–93 | sim | sim |
| | 70 | EJA EF anos finais (2º segmento) | 12–93 | sim | sim |
| | 72 | EJA EF anos iniciais e finais (multietapas) | — (aluno: 69 ou 70) | não | sim |
| | 71 | EJA EM (3º segmento) | 15–93 | sim | sim |
| | 74 | Curso técnico integrado na modalidade EJA | 15–94 | sim | sim |
| | 73 | Curso FIC integrado na EJA – nível fundamental | 12–94 | sim | sim |
| | 67 | Curso FIC integrado na EJA – nível médio | 15–94 | sim | sim |
| 308 Curso técnico e qualificação profissional (FIC) | 39 | Curso técnico – concomitante | 13–58 | sim | sim |
| | 40 | Curso técnico – subsequente | 13–75 | sim | sim |
| | 64 | Curso técnico misto | — (aluno: 39 ou 40) | não | sim |
| | 68 | Qualificação profissional (FIC) – concomitante | 12–94 | sim | sim |
| | **75** | Qualificação profissional (FIC) – não vinculada | 12–94 | **ausente no CMDEB** | **ausente no CMDEB** |
| (sem etapa) | 0 | — | — | "Não aplicável" para AEE e atividade complementar (CMDEB) | idem |

Fontes: E04 "Tabela de Etapas 2026", abas "Etapas de ensino" e "Tipo de turma X Etapa"; E02 Anexo 3 (idades), aba 60 c8 (turma multi); [cmdeb/20-trajetoria.md](cmdeb/20-trajetoria.md); E36. Códigos históricos 30–34 (curso técnico integrado) não são mais etapa: no Censo 2026 o técnico integrado é EM (304/305) com FGB + IFTP (E02 aba 20 c24 regra; E06 p. 54). Habilitação etapa × mediação × tipo de turma: Anexo 7 (ex.: EaD só para EM, Normal, EJA 70/71/74/73/67 e cursos técnicos/FIC) (E02).

### 4.2 Séries/anos finais (para "concluinte")

EF 9º ano (41); EM 3ª, 4ª série e não seriada (27, 28, 29); Normal 3ª e 4ª (37, 38); e, no leiaute SA 2025, também 39, 40, 67, 68, 70, 71, 73, 74 (E10 §5.2; E09 aba 90 c8 regra 4).

### 4.3 Período da oferta EJA (só CMDEB)

`ESTUDANTE_ANO_PERIODO`: 1, 2, 3 = primeiro, segundo, terceiro terço da carga horária da oferta EJA.

---

## 5. Pessoa (registro 30 do Censo; CMDEB blocos 1 e 3)

### 5.1 Sexo (códigos e escopo DIFERENTES)

| Código | Censo (30 c11) | CMDEB estudante | CMDEB profissional |
|---|---|---|---|
| 0 | — | Não informado | — |
| 1 | Masculino | Masculino | Masculino |
| 2 | Feminino | Feminino | Feminino |
| 3 | — | Intersexo | Intersexo |
| 4 | — | Prefere não informar | Prefere não informar |

CMDEB profissional tem ainda `PROFISSIONAL_GENERO` (0–5) sem equivalente no Censo.

### 5.2 Cor/raça (códigos 4 e 5 INVERTIDOS)

| Conceito | Censo (30 c12) | CMDEB |
|---|---|---|
| Não declarada / não informado | 0 | 0 |
| Branca | 1 | 1 |
| Preta | 2 | 2 |
| Parda | 3 | 3 |
| **Amarela** | **4** | **5** |
| **Indígena** | **5** | **4** |

Censo exige "Povo indígena" (Tabela de Povos Indígenas, código até 3 dígitos, 30 c13) quando indígena (E02, E04). Quilombola: só CMDEB (estudante 0 Não / 1 Sim na Portaria; API v2: 0 Não informado / 1 Sim / 2 Não) (E31, E36).

### 5.3 Nacionalidade

| Censo 30 c14 | Rótulo |
|---|---|
| 1 | Brasileira |
| 2 | Brasileira – nascido no exterior ou naturalizado |
| 3 | Estrangeira |

País de nacionalidade (30 c15): Tabela de Países do INEP (ex.: 76 Brasil, 4 Afeganistão), cujos números coincidem com ISO 3166-1 numérico nos casos verificados [I]; o CMDEB declara ISO 3166-1 numérico para estudante e texto livre para profissional (E04, E31).

### 5.4 Filiação (Censo 30 c8–10)

0 Não declarado/Ignorado; 1 Filiação 1 e/ou Filiação 2. Filiação 1 "preferencialmente o nome da mãe". Vínculo do responsável: só CMDEB (`ESTUDANTE_VINCULO_RESPONSAVEL_*`, 0–5; ver [cmdeb/10-estudante.md](cmdeb/10-estudante.md)).

### 5.5 Deficiência, TEA e altas habilidades (estrutura DIFERENTE)

Censo: um indicador geral (30 c17, 0/1) + 11 marcadores 0/1. CMDEB: lista multivalorada de códigos `[1..n]`.

| Conceito | Censo 2026 (campo do reg. 30) | CMDEB código |
|---|---|---|
| Não informado | — | 0 |
| Cegueira | c18 | 3 |
| Baixa visão | c19 | 1 |
| Visão monocular | c20 | 2 |
| Surdez | c21 | 5 |
| Deficiência auditiva | c22 | 4 |
| Surdocegueira | c23 | 6 |
| Deficiência física | c24 | 7 |
| Deficiência intelectual | c25 | 8 |
| **Deficiência múltipla** | **c26** (só se houver mais de uma em c18–c25) | **ausente** |
| Transtorno do espectro autista | c27 | 9 |
| Altas habilidades/superdotação | c28 | 10 |
| Não possui | c17 = 0 | 11 |

Regras Censo: c17 = 1 obrigatório se aluno em classe especial ou AEE; não se altera de 1 para 0 via migração (E02 aba 30).

### 5.6 Transtornos que impactam o desenvolvimento da aprendizagem (só Censo)

Indicador 30 c29 (0/1, só para aluno) e marcadores c30–c35: Discalculia ou outro transtorno da matemática e raciocínio lógico; Disgrafia, disortografia ou outro transtorno da escrita e ortografia; Dislalia ou outro transtorno da linguagem e comunicação; Dislexia; TDAH; Transtorno do Processamento Auditivo Central (TPAC). Sem equivalente no CMDEB. O Caderno 2026 registra que a declaração pode se basear no Estudo de Caso, no Plano de AEE ou no PEI, e que a exigência de laudo médico como condição para matrícula, AEE ou declaração ao Censo é vedada pelo Decreto 12.686/2025 e pela Portaria MEC 421/2026, art. 7º §4 (E06 p. 61–62). O aprofundamento normativo desses itens é da frente de inclusão.

### 5.7 Recursos para uso em sala e em avaliações do INEP (Saeb) (só Censo)

Marcadores 30 c36–c49: Auxílio ledor; Auxílio transcrição; Guia-intérprete; Tradutor-intérprete de Libras; Leitura labial; Prova ampliada (fonte 18); Prova superampliada (fonte 24); CD com áudio para deficiente visual; Prova de Língua Portuguesa como segunda língua para surdos e deficientes auditivos; Prova em vídeo em Libras; Material didático em Braille; Prova em Braille; Tempo adicional; Nenhum. Compatibilidade recurso × deficiência/transtorno: Anexo 4 do leiaute (ex.: nenhum recurso para quem tem só AH/SD; transtornos admitem apenas ledor, transcrição e tempo adicional) (E02).

### 5.8 Maior nível de escolaridade concluído (Censo 30 c56, profissional e gestor)

| Código | Rótulo |
|---|---|
| 1 | Não concluiu o ensino fundamental |
| 2 | Ensino fundamental |
| 7 | Ensino médio |
| 6 | Educação superior |

CMDEB usa outra escala (`CO_NIVEL_ESCOLARIDADE` 0–11) (E31).

---

## 6. Vínculo do aluno (registro 60) e apoio

### 6.1 Tipo de AEE (estrutura e códigos DIFERENTES)

| Atividade | Censo 2026 reg. 60 (marcador) | Tabela AEE 2026 (código) | CMDEB `TIPO_ATENDIMENTO_ESPECIALIZADO` |
|---|---|---|---|
| Não informado | — | — | 0 |
| Desenvolvimento de funções cognitivas | c10 | 4 | 1 |
| Desenvolvimento de vida autônoma | c11 | 12 | 2 |
| Enriquecimento curricular | c12 | 8 | 3 |
| Ensino da informática acessível | c13 | 10 | 4 |
| Ensino da Libras | c14 | 6 | 5 |
| Ensino da Língua Portuguesa como segunda língua | c15 | 11 | 6 |
| Técnicas de cálculo no Soroban | c16 | 9 | 7 |
| Ensino do Sistema Braille | c17 | 1 | 9 |
| Técnicas de orientação e mobilidade | c18 | 5 | 8 |
| Comunicação Alternativa e Aumentativa (CAA) | c19 | 7 | 10 |
| Recursos ópticos e não ópticos | c20 | 3 | 11 |

Censo: marcadores 0/1 só quando a turma é tipo 5 (AEE), vários por aluno. CMDEB: código único `[1..1]` na matrícula (E02 aba 60; E04; E31).

### 6.2 Apoio pedagógico (só CMDEB)

`ESTUDANTE_APOIO_PEDAGOGICO`: 0 a 6 (ver [cmdeb/20-trajetoria.md](cmdeb/20-trajetoria.md)). O Censo registra apoio pela via do profissional da turma (função 8 "Profissional de apoio escolar", reg. 50) e dos recursos (5.7), não por aluno.

### 6.3 Escolarização em outro espaço (Censo 60 c21)

1 Não recebe escolarização fora da escola; 2 Em hospital; 3 Em domicílio.

### 6.4 Transporte escolar público (Censo 60 c22–33)

Utiliza (0/1); poder público responsável (1 Estadual, 2 Municipal); tipos de veículo rodoviário e aquaviário (marcadores).

---

## 7. Situação do aluno / da matrícula (códigos e semântica DIFERENTES)

### 7.1 Censo – 2ª etapa (Situação do Aluno), leiaute 2025 v3

| Código | Rótulo | Restrições de uso (regras do leiaute) | Definição (Caderno 2ª etapa) |
|---|---|---|---|
| 1 | Transferido | permitido em "admissão após" | mudou de escola com requerimento formal; mudança de modalidade na mesma escola conta como transferência |
| 2 | Deixou de frequentar | permitido em "admissão após" | abandonou antes do fim do ano letivo sem pedir transferência |
| 3 | Falecido | | faleceu antes do fim do ano letivo |
| 4 | Reprovado | não para EI (1, 2) | não alcançou os critérios mínimos |
| 5 | Aprovado | não para EI | alcançou os critérios; progressão parcial/dependência = Aprovado |
| 6 | Aprovado concluinte | só em etapas finais (27, 28, 29, 37, 38, 39, 40, 41, 67, 68, 70, 71, 73, 74) | aprovado com emissão de certificado da etapa |
| 7 | Sem movimentação | só EI (1, 2) | rendimento não se aplica e o aluno permaneceu até o fim |
| 8 | Em andamento | só 39, 40, 67, 68, 69, 70, 71, 73, 74 | EJA e técnico/FIC com atividades não concluídas no fim do ano letivo |

Fonte: E09 abas 90 e 91; E10 §3–5. **Atenção**: a mesma planilha tem regras contraditórias sobre 7 e 8 (ver [questoes-abertas-organizacao.md](questoes-abertas-organizacao.md) Q-04).

### 7.2 CMDEB / API v2 (situação da matrícula, atualizável a qualquer momento)

| Código | Rótulo CMDEB | Equivalente Censo SA (aproximado) [I] |
|---|---|---|
| 0 | Em andamento | (matrícula ativa; sem equivalente anual) |
| 1 | Informação incorreta | (correção, não situação) |
| 2 | Transferência para outra unidade escolar dentro da mesma rede | 1 Transferido |
| 3 | Transferência para outra unidade escolar em outra rede pública | 1 Transferido |
| 4 | Transferência para outra unidade escolar em outra rede privada | 1 Transferido |
| 5 | Transferência para outra rede não identificada | 1 Transferido |
| 6 | Evasão | sem equivalente direto (Censo mede evasão entre anos, não como situação) |
| 7 | Abandono | 2 Deixou de frequentar |
| 8 | Óbito informado | 3 Falecido |
| 9 | Reclassificação | sem equivalente (LDB art. 23 §1) |
| 10 | Aprovado | 5 Aprovado |
| 11 | Concluinte (API exige forma de conclusão: 1 Regular, 2 Encceja, 3 Enem, 4 Programa/Prova de aceleração) | 6 Aprovado concluinte |
| 12 | Reprovado | 4 Reprovado |
| 19 | Concluinte Encceja + 400h (só na Portaria; ausente da API v2) | 6 [I] |
| 21 | Transferência entre modalidades (EM <> EJA) | 1 Transferido (o Censo trata mudança de modalidade como transferência) |
| 22 | Trancamento de matrícula em curso técnico | sem equivalente |
| 23 | Concluinte EMR Encceja (só na Portaria; ausente da API v2) | 6 [I] |

Fontes: [cmdeb/20-trajetoria.md](cmdeb/20-trajetoria.md) §2.1; E36 `MatriculaMovimentacaoData`. Não existe nas fontes CMDEB o equivalente a "Sem movimentação" (EI) nem "Em andamento" no sentido do Censo (curso não concluído no fim do ano) distinto de "0 Em andamento" [I].

### 7.3 Situação da avaliação no componente (CMDEB)

`SITUACAO_DESEMPENHO_ESTUDANTE_COMPONENTE_CURRICULAR`: 0 Não informado; 1 Aprovado; 2 Reprovado. Sistema de avaliação do componente (`SISTEMA_AVALIACAO_DESEMPENHO`, 0–10): ver [cmdeb/20-trajetoria.md](cmdeb/20-trajetoria.md) §2.3 (domínio da frente de avaliação).

---

## 8. Componentes curriculares / áreas do conhecimento

Mesma numeração no Censo (Tabela de Áreas do Conhecimento/Componentes Curriculares 2026; reg. 20 c39–65; reg. 50 c9–33) e no CMDEB (`CO_COMPONENTE_CURRICULAR`) nos casos conferidos.

| Área (CMDEB `CO_COMPONENTE_CURRICULAR_AREA_CONHECIMENTO`) | Código | Componente |
|---|---|---|
| 1 Linguagens | 6 | Língua/Literatura Portuguesa |
| | 7 | Língua/Literatura estrangeira – Inglês |
| | 8 | Língua/Literatura estrangeira – Espanhol |
| | 30 | Língua/Literatura estrangeira – Francês |
| | 9 | Língua/Literatura estrangeira – outra |
| | 27 | Língua indígena |
| | 23 | Libras |
| | 31 | Língua Portuguesa como Segunda Língua |
| | 10 | Arte (Educação Artística, Teatro, Dança, Música, Artes Plásticas e outras) |
| | 11 | Educação Física |
| 2 Matemática | 3 | Matemática |
| 3 Ciências da Natureza | 1 | Química |
| | 2 | Física |
| | 4 | Biologia |
| | 5 | Ciências |
| 4 Ciências Humanas e Sociais | 12 | História |
| | 13 | Geografia |
| | 14 | Filosofia |
| | 28 | Estudos Sociais |
| | 29 | Sociologia |
| 99 Outras áreas | 16 | Informática/Computação |
| | 17 | Áreas do conhecimento profissionalizantes |
| | 25 | Áreas do conhecimento pedagógicas |
| | 26 | Ensino religioso |
| | 32 | Estágio curricular supervisionado |
| | 33 | Projeto de vida |
| | 99 | Outras áreas do conhecimento |

Fonte: E04 "Tabela de Áreas do conhecimento_Componentes Curriculares 2026"; E31. No Censo a turma declara se **oferece** cada componente (0/1); não há carga horária por componente nem identificador de oferta. Regras de compatibilidade componente × etapa: "Tabela de Regras de Áreas do Conhecimento 2026" (E04, não transcrita).

---

## 9. Profissionais

### 9.1 Função que exerce na turma (Censo reg. 50 c7) × CMDEB `CO_FUNCAO` (códigos DIFERENTES)

| Função | Censo 2026 | CMDEB |
|---|---|---|
| Docente | 1 | 1 |
| Auxiliar/assistente educacional | 2 (só turma 6 ou 9) | 4 |
| Profissional/monitor de atividade complementar | 3 (só turma 4 ou 9) | 7 |
| Tradutor e intérprete de Libras | 4 (exige aluno ou profissional com surdez/DA/surdocegueira na turma) | 2 |
| Docente titular – coordenador de tutoria – EaD | 5 (só EaD) | 5 |
| Docente tutor – auxiliar – EaD | 6 (só EaD) | 8 |
| Guia-intérprete | 7 | 3 |
| Profissional de apoio escolar para alunos com deficiência (Lei 13.146/2015) | 8 | 6 |
| Instrutor da educação profissional | 9 | 9 |
| Diretor(a), vice, coordenador pedagógico, secretário escolar, merendeira, auxiliar na escola, gestor na secretaria, outros | fora do reg. 50 (gestor no reg. 40; demais só em contagem no reg. 10 c119–138) | 10, 16, 11, 12, 15, 17, 14, 99 |

### 9.2 Gestor escolar (Censo reg. 40)

| Campo | Códigos |
|---|---|
| c5 Cargo | 1 Diretor(a); 2 Outro cargo |
| c6 Critério de acesso ao cargo/função (só diretor de escola em atividade) | 1 Proprietário ou sócio-proprietário (vedado para pública); 2 Exclusivamente por indicação/escolha da gestão; 3 Processo seletivo qualificado e escolha/nomeação da gestão; 4 Concurso público específico (vedado para privada); 5 Exclusivamente por processo eleitoral com a comunidade escolar (vedado para privada); 6 Processo seletivo qualificado e eleição com a comunidade (vedado para privada); 7 Outros |
| c7 Situação funcional / tipo de vínculo | 1 Concursado/efetivo/estável; 2 Contrato temporário; 3 Contrato terceirizado; 4 Contrato CLT |

### 9.3 Tipo de vínculo (Censo reg. 40 c7 e reg. 50 c8) × CMDEB `CO_TIPO_VINCULO`

| Conceito | Censo | CMDEB |
|---|---|---|
| Não informado | — | 0 |
| Concursado/efetivo/estável (estatutário efetivo) | 1 | 1 |
| Contrato temporário | 2 | 2 |
| Contrato terceirizado | 3 | 3 |
| Contrato CLT | 4 | 4 |
| Cargo comissionado | — | 5 |

No Censo, o vínculo do docente só é informado em escola pública e para funções 1, 5, 6 (E02 aba 50 c8). Situação do vínculo com a rede (ativo, inativo, licença…): só CMDEB (`SITUACAO_VINCULO_PROFISSIONAL_REDE`).

---

## 10. Identificadores e códigos geográficos

Ver detalhamento em [fichas/inep-identificadores.md](fichas/inep-identificadores.md). Resumo dos formatos:

| Identificador | Formato | Emissor | Fonte |
|---|---|---|---|
| Código de escola – INEP (`CO_ENTIDADE`) | 8 dígitos, fixo | INEP (via secretaria estadual no cadastro da escola nova) | E02 aba 00 c2; E06 p. 6 |
| Identificação única INEP de pessoa (aluno, profissional, gestor) | 12 dígitos, fixo | Educacenso | E02 aba 30 c4; E06 p. 66 |
| Código da turma – INEP | numérico até 10 dígitos; só na exportação | INEP | E09 aba 90 c4; E02 aba 20 c4 |
| Código da matrícula – INEP | numérico até 12 dígitos; só na exportação | INEP | E09 aba 90 c7; E02 aba 60 c7 |
| Código da turma na escola (sistema próprio) | alfanumérico até 20, único por escola | escola/rede | E02 aba 20 c3 |
| Código da pessoa no sistema próprio | alfanumérico até 20, único por escola | escola/rede | E02 aba 30 c3 |
| CPF | 11 dígitos, validado contra a Receita Federal | Receita Federal | E02 aba 30 c5 |
| Matrícula da certidão de nascimento (certidão nova) | 32 caracteres: 30 numéricos + 2 numéricos ou "XX" | cartório (CNJ) | E02 aba 30 c50 |
| Município (IBGE) | 7 dígitos | IBGE (Tabela de Municípios 2026 do INEP) | E02 aba 00 c8; E04 |
| UF (IBGE) | 2 dígitos | IBGE | E04 |
| Distrito | 2 dígitos no arquivo (código completo de 9 dígitos na tabela) | IBGE via INEP | E02 aba 00 c9; E04 |
| Órgão regional de ensino | alfanumérico até 5, por UF/município (Tabela de Órgãos Regionais 2026; 108 linhas para SP) | secretaria estadual (alteração só pela coordenação estadual) | E02 aba 00 c18; E04; E06 p. 13 |
| Região administrativa (DF) | Tabela de Regiões Administrativas 2026 | INEP | E04 |
| CNPJ mantenedora principal / escola privada | 14 dígitos | Receita Federal | E02 aba 00 c47–48 |
| CNPJ da secretaria de educação / unidade executora | até 14 | Receita Federal | E31 bloco 4 |
| Código da IES | até 9 dígitos (Censo 00 c53); Tabela de IES até 7 (30 c60) | INEP/e-MEC | E02; E04 |
| Língua indígena; povo indígena; país; curso técnico; curso superior; área de pós-graduação | tabelas auxiliares | INEP | E04 |
| IDs SGP (`ID_SGP_ESTUDANTE`, `_MATRICULA`, `_TURMA`, `_COMPONENTE_CURRICULAR`, `_PROFISSIONAL`) | numéricos gerados pelo SGP (componente: alfanumérico na Portaria) | MEC | E31; E36 |
| Códigos da rede (`CO_MATRICULA_REDE`, `CO_TURMA_REDE`, `PROFISSIONAL_IDENTIFICACAO_INSTITUICAO`) | alfanuméricos livres | rede | E31 |
| RA (Registro do Aluno), SP | número + dígito + UF | SEDUC-SP (SED) | E40 |
