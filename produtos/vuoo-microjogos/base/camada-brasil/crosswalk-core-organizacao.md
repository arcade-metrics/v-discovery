# Crosswalk: conceitos brasileiros de organização e dados → Core provisório

Alvos: entidades provisórias `C.xxx` de [../_convencoes.md](../_convencoes.md) §4. Tipos de equivalência: exata, aproximada, parcial, mais ampla, mais restrita, inexistente. "Mais restrita" = o conceito brasileiro é mais restrito que o alvo. Equivalências não são declaradas por nenhuma fonte oficial: **todo o mapeamento é inferência [I]** baseada nas definições citadas (fontes em [evidencias-organizacao.md](evidencias-organizacao.md)). Acesso às fontes: 2026-11-05.

## 1. Organização (D1)

| Conceito BR | Fonte | Alvo | Equivalência | Nota |
|---|---|---|---|---|
| Sistema de ensino (federal, estadual/DF, municipal) | LDB arts. 16–18 | C.ORG (`type=education_system`) | mais restrita | nível normativo, não operacional; escola privada de EF/EM pertence ao sistema estadual |
| Rede de ensino / secretaria de educação | Censo 00 c21 (dependência) + UF/município; CMDEB `CNPJ_SECRETARIA_EDUCACAO` | C.ORG (`type=network`) | aproximada | o Censo não tem entidade "rede": derivar de dependência + ente; CMDEB identifica por CNPJ |
| Dependência administrativa (federal/estadual/municipal/privada) | Censo 00 c21; CMDEB | atributo de C.ORG | exata (como atributo) | vocabulário C.VOC `br-dependencia` |
| Órgão regional de ensino (DRE, URE, CRE) | Censo 00 c18; Tabela de Órgãos Regionais | C.ORG (`type=regional_office`), filho da rede | exata | código ≤ 5 por UF |
| Mantenedora da escola privada | Censo 00 c26–32, c47 | C.ORG (`type=maintainer`) | aproximada | identificada só por CNPJ; tipo por marcadores múltiplos |
| Escola / instituição de ensino | Censo 00; CMDEB bloco 4 | C.ORG (`type=school`) | exata | chave INEP 8 dígitos |
| Unidade vinculada (escola sede → unidade) | Censo 00 c51–52 | C.ORG (`type=school_unit`, `parent=sede`) | aproximada | tem código INEP próprio, mas sem autonomia orçamentária |
| Local de funcionamento, prédio, dependências físicas, salas | Censo 10 | C.LOC | parcial | Censo descreve infraestrutura por marcadores e contagens; não identifica salas individuais |
| Local de funcionamento diferenciado da turma (sala anexa, socioeducativo, prisional) | Censo 20 c21 | C.LOC (atributo da C.GRP) | parcial | |
| Ano letivo (datas de início e término da escola) | Censo 00 c4–5; LDB art. 23 §2, 24 I | C.SES (`type=school_year`) | exata | por escola; ≥ 200 dias e ≥ 800/1.000 h são regras do adaptador |
| Período letivo da turma | CMDEB `DATA_INICIO_PERIODO_LETIVO`, `DATA_INICIO_TURMA`, `DATA_FIM_TURMA` | C.SES (`type=term`) | aproximada | sem tipo de período (bimestre/semestre) explícito |
| Data de referência do Censo | Portaria MEC 264/2007; Censo 2026 = 27/05 | C.SES (`type=reference_date`) ou C.PRV (snapshot) | inexistente | ver Q-14 (candidato a conceito de "declaração/snapshot") |
| Mês/ano de referência da frequência | CMDEB 2.4 | C.SES (`type=month`) | aproximada | |
| Nível (educação básica, superior) | LDB art. 21 | C.PRG (`level`) | exata | |
| Etapa agregada (301–308) | Tabela de Etapas | C.PRG (hierarquia) | exata | |
| Etapa de ensino (1, 2, 14…41, 25…) | Tabela de Etapas; CMDEB | C.PRG (`grade_level`) + C.VOC `br-inep-etapa` | aproximada | mistura ano/série com tipo de oferta (multi, correção de fluxo, técnico concomitante) |
| Modalidade (regular, especial, EJA, profissional) | CMDEB `MODALIDADE_ENSINO_ESTUDANTE`; LDB | C.PRG (`modality`) | aproximada | no Censo é derivada da etapa/classe especial |
| Curso técnico / FIC (código do curso, eixo) | Censo 20 c25–26, c37–38; Tabela de Cursos | C.PRG (`program`) | exata | |
| Forma de organização (série, semestre, ciclo, grupo não seriado, módulo; alternância) | LDB art. 23; Censo 20 c28–29; CMDEB | atributo de C.PRG/C.GRP | exata (como vocabulário) | Core não deve presumir série anual |
| Organização curricular (FGB, IFA, IFTP) | Censo 20 c30–36; CMDEB | atributo de C.GRP/C.PRG | parcial | Censo combina por marcadores; CMDEB por código único |
| Componente curricular / área do conhecimento (código nacional) | Tabela de Áreas; CMDEB 2.3 | C.SUB + C.VOC `br-inep-componente` | exata | mesma numeração Censo/CMDEB |
| Turma curricular (etapa de ensino) | Censo 20 c14 = 6, 9 | C.GRP (`kind=academic_class`) | exata | |
| Turma de atividade complementar | Censo 20 c14 = 4 | C.GRP (`kind=extracurricular`) | aproximada | |
| Turma de AEE | Censo 20 c14 = 5; Caderno p. 49 | C.GRP (`kind=support_service`) | aproximada | não substitui a matrícula na classe comum |
| Turma multi / multietapa / correção de fluxo | Etapas 22, 23, 56, 3, 72, 64 | C.GRP com várias C.PRG | parcial | etapa do aluno vem do vínculo (60 c8) |
| Classe especial; classe bilíngue de surdos; turma de alternância | Censo 20 c22, c66, c29 | atributos de C.GRP | exata (como marcador) | |
| Turno (CMDEB) / horário semanal por dia (Censo) | CMDEB `TURNO_TURMA`; Censo 20 c7–13 | C.SCH | parcial | Censo: janela diária por dia da semana; CMDEB: turno; nenhum tem sessão/aula |
| Oferta de componente na turma com profissional e carga | CMDEB bloco 3 (alocação) + 2.3 | C.OFR | aproximada | Censo só marca "oferece" e lista componentes por docente |
| Vagas da turma | CMDEB `TURMA_VAGAS` | atributo de C.GRP | exata | |

## 2. Pessoas e vínculos (D1, D3)

| Conceito BR | Fonte | Alvo | Equivalência | Nota |
|---|---|---|---|---|
| Pessoa física (registro 30) | Censo 30; CMDEB blocos 1 e 3 | C.PER | exata | um registro para aluno, profissional e gestor |
| Aluno / estudante | Censo 60; CMDEB bloco 1 | C.LRN | exata | |
| Profissional escolar em sala de aula | Censo 50 | C.STF | mais restrita | Censo só identifica quem está em sala; demais só contagem |
| Profissional da educação (LDB art. 61) | CMDEB bloco 3 | C.STF | aproximada | inclui merendeira, secretário, gestor na secretaria |
| Gestor escolar (diretor, outro cargo) | Censo 40 | C.STF (`role=school_leader`) | exata | critério de acesso e vínculo como atributos |
| Função na turma (docente, auxiliar, intérprete, apoio, tutor EaD…) | Censo 50 c7; CMDEB `CO_FUNCAO` | papel em C.OFR/C.GRP + C.VOC | aproximada | códigos diferentes entre Censo e CMDEB |
| Vínculo do profissional com a rede (tipo, situação, datas, carga) | CMDEB bloco 3 | C.ENR (pessoa × org, papel staff) | aproximada | Censo só tem tipo de vínculo por turma |
| Formação do profissional | Censo 30 c56–109; CMDEB | C.CRD (de staff) | parcial | |
| Responsável e vínculo (filiação, acolhimento, tutela, guarda de fato) | CMDEB bloco 1; Censo filiação | C.GRD | aproximada | Censo só tem nomes de filiação; CMDEB tem vínculo codificado |
| Matrícula (vínculo aluno × turma) | Censo 60 | C.ENR (pessoa × C.GRP) | exata | código INEP da matrícula só após importação |
| Matrícula CMDEB (aluno × escola × etapa × ano, enturmação opcional) | CMDEB 2.1 | C.ENR (pessoa × C.ORG × C.PRG) | exata | separa matrícula de enturmação: o Core precisa dos dois níveis |
| Enturmação | API `/matriculas/enturmacao` | C.ENR (pessoa × C.GRP) | exata | |
| Tempo integral | CMDEB `ESTUDANTE_MATRICULA_INTEGRAL` | atributo de C.ENR | exata | |
| Situação da matrícula (CMDEB, 17 códigos) | CMDEB 2.1; API movimentação | C.ENR `status` + C.VOC | parcial | mistura movimento, rendimento e correção ("informação incorreta") |
| Situação do aluno (Censo 2ª etapa, 8 códigos) | Censo 90/91 | C.ENR `outcome` anual | parcial | rendimento e movimento num só código; só para matrícula de escolarização |
| Transferência, abandono/deixou de frequentar, evasão, falecido | Censo; CMDEB | eventos de C.ENR | aproximada | "evasão" (CMDEB 6) não tem equivalente no Censo |
| Reclassificação; classificação | LDB 23 §1, 24 II; CMDEB 9 | evento de C.ENR | aproximada | |
| Conclusão (concluinte; forma: regular, Encceja, Enem, aceleração) | Censo 6; CMDEB 11 + forma | C.CRD / evento de C.ENR | aproximada | |
| Admissão após (ingresso depois da data de referência) | Censo 91 | evento de C.ENR | inexistente no Core | ver Q-14 |
| Frequência mensal (horas ofertadas/presentes, por turma ou componente) | CMDEB 2.4 | inexistente | inexistente | candidato a entidade `AttendanceSummary` (Q-15); C.EVT é telemetria, não frequência escolar |
| Avaliação de desempenho por componente | CMDEB 2.5 | C.RES | aproximada | escala definida no componente (`SISTEMA_AVALIACAO_DESEMPENHO`) — frente de avaliação |
| Deficiência, TEA, AH/SD; transtornos de aprendizagem | Censo 30 c17–35; CMDEB | C.SUP | parcial | categorias diagnósticas; o Core deve armazenar como necessidade de apoio sem reduzir a diagnóstico (frente de inclusão) |
| Recursos para avaliações do INEP (Saeb) | Censo 30 c36–49 | C.SUP (`context=assessment`) | aproximada | |
| Tipo de AEE | Censo 60 c10–20; CMDEB | C.SUP / C.OFR (atividade de AEE) | parcial | Censo: por vínculo em turma de AEE; CMDEB: na matrícula |
| Apoio pedagógico (profissional de apoio, intérprete, tecnologia assistiva…) | CMDEB `ESTUDANTE_APOIO_PEDAGOGICO` | C.SUP | aproximada | |
| PEI / Plano de AEE / Estudo de Caso | Caderno 2026 p. 61–62 (como documentos aceitos) | C.PLN | inexistente no Censo/CMDEB | só citado como documento comprobatório |
| Escolarização em hospital/domicílio; transporte escolar | Censo 60 c21–33 | atributos de C.ENR | aproximada | |

## 3. Identificadores e governança (D8)

| Conceito BR | Fonte | Alvo | Equivalência | Nota |
|---|---|---|---|---|
| Código de escola INEP | Censo; CMDEB | C.IDN `scheme=br-inep-escola` | exata | |
| Identificação única INEP de pessoa | Censo 30 c4 | C.IDN `scheme=br-inep-pessoa` | exata | sensível |
| Código da turma INEP; código da matrícula INEP | Censo export | C.IDN `scheme=br-inep-turma` / `br-inep-matricula`, com ano | exata | anuais |
| CPF (Inue) | LC 220 art. 26 I; Portaria 269 art. 7º | C.IDN `scheme=br-cpf` | exata | obrigatório por lei para dados em nível de estudante |
| Certidão de nascimento nova; NIS | Censo 30 c50; CMDEB | C.IDN | exata | |
| IDs SGP; códigos da rede | CMDEB | C.IDN `scheme=br-sgp-*`, `br-rede-*` | exata | |
| RA (SP) | SED | C.IDN `scheme=br-sp-ra` | exata | número + dígito + UF |
| IBGE município/UF/distrito; CNPJ | Censo; CMDEB | C.IDN em C.ORG/C.LOC | exata | |
| Tabelas auxiliares (etapas, componentes, AEE, países, povos indígenas…) | E04 | C.VOC (versionado por ano) | exata | |
| Versão do leiaute; ano do censo; lote SGP; status de importação | E02; E36 | C.PRV | aproximada | |
| Base legal do tratamento (obrigação legal: Decreto 6.425/2008; LC 220; Portaria 269) | E06, E21, E30 | C.CNS | aproximada | detalhamento: frente de privacidade |
| Perfis de acesso (Escola, Municipal, Estado, Setec, INEP; operador SGP) | E05; E34 | inexistente no Core provisório | — | ligar a psg.access.school-roles |
