# Modelo de dados: Brasil (D1, D3, D8)

Dono: frente "organização e dados". Descreve as entidades, atributos, identificadores e cardinalidades que o **adaptador Brasil** precisa representar, a partir de três fontes normativas/técnicas que coexistem:

1. **Censo Escolar / Educacenso (INEP)**: leiaute de migração 2026 (V5), arquivo texto delimitado por `|`, anual, com data de referência [E02, E05].
2. **CMDEB / MEC Gestão Presente (MEC)**: modelo de informação da Portaria MEC 832/2025, já transcrito em [cmdeb/](cmdeb/README.md), e sua implementação na **API CMDEB v2** (OpenAPI 3.1, JSON, lotes assíncronos) [E31, E36].
3. **LDB e LC 220/2025 + Portaria MEC 269/2026**: restrições legais de organização (etapas, carga, frequência) e o **CPF como Identificador Nacional Único do Estudante (Inue)** [E20, E21, E30].

Códigos de todos os campos codificados: [terminologia.md](terminologia.md). Fontes: [evidencias-organizacao.md](evidencias-organizacao.md). Inferências marcadas [I]. Acesso: 2026-11-05.

---

## 1. Visão geral: dois modelos que não têm o mesmo formato

| Aspecto | Censo Escolar (Educacenso) | CMDEB (SGP, API v2) |
|---|---|---|
| Natureza | pesquisa estatística declaratória, obrigatória (Decreto 6.425/2008, segundo E06) | plataforma de gestão; CMDEB "padrão orientativo… obrigatório" segundo o MEC (E34), adesão à plataforma voluntária (E33) |
| Periodicidade | anual: 1ª etapa (foto na data de referência, 27/05/2026) e 2ª etapa (situação no fim do ano letivo) | contínua; frequência mensal; janelas de envio definidas pela SEB (Portaria 832, art. 14) |
| Formato | arquivo `.txt` ISO-8859-1, registros por linha, campos separados por `|`, fim `99|`; maiúsculas sem acento; ≤ 20 MB, ≤ 100 escolas por arquivo | JSON por lotes, snake_case, token Bearer de 5 min, pré-validação com HTTP 422 (E35, E36); ou planilhas com cabeçalhos em CAIXA ALTA |
| Matrícula | vínculo aluno × turma (registro 60); não há entidade "matrícula" independente na importação | entidade própria `matricula` (`ID_SGP_MATRICULA`), com etapa, datas, situação; enturmação separada |
| Situação | 8 códigos na 2ª etapa, um por vínculo de escolarização | 17 códigos, atualizáveis por "movimentação" a qualquer momento |
| Identificador de pessoa | ID INEP (12 dígitos); CPF obrigatório só para gestor, profissional brasileiro e aluno de EJA | CPF obrigatório para estudante (`[1..1]`) e profissional; `ID_SGP_*` gerados pelo MEC |
| Componente curricular | marcação "oferece/não oferece" por turma (lista fixa) | entidade `componente_curricular` com carga horária e sistema de avaliação, ligada à turma e ao profissional |
| Frequência e notas | não coletadas | frequência mensal em horas (por turma e por componente) e resultado de avaliação por componente |

Consequência para o Core [I]: o Censo é uma **visão anual derivável** de um modelo operacional; o CMDEB está mais próximo de um modelo operacional (matrícula, enturmação, frequência), mas com granularidade mensal. O Core deve guardar eventos/vigências e gerar as duas saídas.

---

## 2. Censo Escolar 2026: estrutura do arquivo de migração

Fonte: E02, aba "regras gerais" (regras 1 a 42) e abas de registro.

### 2.1 Registros e ordem

| Registro | Entidade | Nº de campos | Deve vir após | Cardinalidade por escola |
|---|---|---|---|---|
| 00 | Escola: identificação, funcionamento, vinculação, mantenedora | 53 | início do arquivo, 40 ou 60 | exatamente 1 |
| 10 | Escola: caracterização e infraestrutura | 187 | 00 | exatamente 1 (só escola em atividade) |
| 20 | Turma | 66 | 10 ou 20 | 1..1.500 (≥ 1 para escola em atividade) |
| 30 | Pessoa física (aluno, profissional ou gestor) | 110 | 00, 20 ou 30 | 1..n; cada pessoa precisa de ≥ 1 vínculo 40, 50 ou 60 |
| 40 | Vínculo de gestor escolar | 7 | 30 ou 40 | 1..3 |
| 50 | Vínculo de profissional escolar em sala de aula × turma | 38 | 40 ou 50 | ≥ 1 por turma |
| 60 | Vínculo de aluno × turma (matrícula) | 33 | 50 ou 60 | ≥ 1 por turma |
| 99 | Fim de arquivo (`99|`) | — | último | 1 por arquivo |

Escola paralisada ou extinta (00 c3 = 2 ou 3): só registros 00, 30 e 40 (regra 18).

### 2.2 Regras gerais de validação relevantes para o adaptador

| Nº | Regra (resumo) | Efeito |
|---|---|---|
| 1 | Codificação ISO-8859-1 | Recusada |
| 2 | `.txt`, ≤ 20 MB, nome ≤ 20 caracteres `[A-Za-z0-9_]` | Recusada |
| 23–24 | ≤ 100 escolas por arquivo; ≤ 1.500 turmas por escola | Recusada |
| 25 | Não pode haver duas turmas na mesma escola com nome, mediação, horários, tipo, local diferenciado, classe especial e etapa iguais | Recusada |
| 26–27 | Toda turma tem ≥ 1 aluno (60) e ≥ 1 profissional (50) | Recusada |
| 28 | Sem minúsculas nem acentos | Recusada |
| 29 | Proibida a "descaracterização" de pessoa: alterar mais de um campo do grupo 1 (nome, nascimento, filiação 1, filiação 2) junto com algum do grupo 2 (sexo, cor/raça, país, município de nascimento, deficiência), ou três do grupo 1 | Recusada |
| 30 | Uma pessoa só pode ter um registro por turma | Recusada |
| 31 | Aluno não pode estar em duas turmas presenciais com horário coincidente (Tabela de Regras Horários Coincidentes) | Importada parcialmente |
| 32–33 | Aluno: ≤ 4 vínculos em turmas com etapa; ≤ 2 em turmas com etapa diferente de 39, 40, 64 e 68 | Importada parcialmente |
| 34 | ≤ 4 vínculos em AEE ou atividade complementar sem escolarização | Importada parcialmente |
| 35 | Vínculo em itinerário formativo exclusivo (sem FGB) é incompatível com vínculo em etapa 1, 2, 14–18 | Importada parcialmente |
| 37–40 | **Resolução de identidade da pessoa**: 1º ID INEP; 2º CPF; 3º certidão nova; 4º nome + nascimento + filiação (1 e 2 em qualquer ordem). Um único resultado: reaproveita; zero ou mais de um: cria nova pessoa | Processamento |

Status por escola: Importada, Importada parcialmente, Recusada; status do arquivo derivado (Anexo 1).

### 2.3 Registro 00: Escola (campos estruturais)

| Campo | Nome | Obg. | Tipo / tamanho | Regras-chave |
|---|---|---|---|---|
| 2 | Código de escola – INEP | s | num 8 fixo | coerente com a UF do município; deve existir no cadastro INEP |
| 3 | Situação de funcionamento | s | seleção 1–3 | |
| 4 | Data de início do ano letivo | c | data `dd/mm/aaaa` | entre 29/05/2025 e 27/05/2026 se em atividade, senão nulo |
| 5 | Data de término do ano letivo | c | data | a partir de 28/05/2026, posterior ao início e anterior a 26/05/2027 |
| 6 | Nome da escola | s | alfa ≤ 100 | |
| 7 | CEP | s | num 8 | |
| 8 | Município | s | num 7 (IBGE) | só perfis INEP, Setec ou Estado alteram |
| 9 | Distrito | s | num 2 | deve existir para o município |
| 10–17 | Endereço, número, complemento, bairro, DDD, telefones, e-mail | s/n | | |
| 18 | Código do órgão regional de ensino | n | alfa ≤ 5 | da UF do município; nulo para federal Setec; só INEP ou Estado alteram |
| 19 | Localização/zona | s | 1–2 | |
| 20 | Localização diferenciada | s | 1, 2, 3, 7, 8 | |
| 21 | Dependência administrativa | s | 1–4 | 3 vedado em Brasília (5300108); só INEP ou Estado alteram |
| 22–25 | Órgão ao qual a escola pública está vinculada | c | 0/1 cada | |
| 26–31 | Mantenedora da escola privada | c | 0/1 cada | |
| 32 | Categoria da escola privada | c | 1–4 | só se dependência = 4 |
| 33–46 | Parceria/convênio com secretaria estadual/municipal e formas de contratação | c | 0/1 | Anexo 5 |
| 47 | CNPJ da mantenedora principal da escola privada | c | num 14 | |
| 48 | CNPJ da escola privada | n | num 14 | CNPJ válido |
| 49–50 | Regulamentação/autorização e esfera do órgão | c | | |
| 51 | Unidade vinculada / ofertante de educação superior | c | 0–2 | |
| 52 | Código da Escola Sede | c | num 8 | ativa, diferente da atual, mesma dependência e UF |
| 53 | Código da IES | c | num ≤ 9 | |

Não há no Censo identificador de **rede** nem de **secretaria**: a rede é inferida por dependência administrativa + município (municipal) ou UF (estadual) [I]. A mantenedora privada é identificada só por CNPJ (c47).

### 2.4 Registro 10: Caracterização da escola (resumo por grupo)

187 campos, quase todos marcadores 0/1: local de funcionamento (prédio próprio, sala em outra escola, unidade socioeducativa, prisional…), forma de ocupação, compartilhamento de prédio com até 6 escolas (códigos INEP), água, energia, esgoto, lixo, 40 tipos de dependência física (inclui "Sala de recursos multifuncionais para AEE", "Laboratório de robótica" novo em 2026), 10 recursos de acessibilidade, quantidades de salas (dentro/fora, climatizadas, acessíveis, cantinho da leitura), equipamentos, internet, quantitativos de 19 categorias de profissionais que não estão em sala, alimentação, materiais pedagógicos (inclui educação especial, bilíngue de surdos), língua de ensino indígena, exame de seleção, cotas, órgãos colegiados, atualização do PPP, educação ambiental (E02 aba 10). Relevante para `C.LOC` e para acessibilidade física (frente de inclusão); não detalhado aqui.

### 2.5 Registro 20: Turma

| Campo | Nome | Obg. | Tipo / tamanho | Regras-chave |
|---|---|---|---|---|
| 2 | Código de escola – INEP | s | num 8 | |
| 3 | **Código da turma na entidade/escola** | s | alfa ≤ 20 | único na escola; chave de ligação com 50 e 60 no arquivo |
| 4 | **Código da turma – INEP** | n | — | nulo na importação; preenchido só na exportação |
| 5 | Nome da turma | s | alfa ≤ 80 | sugestão do Caderno: ano/série + turma + turno, ex. "7º AM" (E06 p. 56) |
| 6 | Tipo de mediação didático-pedagógica | s | 1–3 | |
| 7–13 | Horário por dia (domingo a sábado) | c | `hh:mm-hh:mm` | só presencial; minutos múltiplos de 5; início < fim |
| 14 | Tipo de turma | s | 4, 5, 6, 9 | |
| 15–20 | Tipo de atividade complementar (até 6) | c | num 5 | Tabela de Atividade Complementar |
| 21 | Local de funcionamento diferenciado | s | 0–3 | |
| 22 | Turma de educação especial (classe especial) | c | 0/1 | só tipo 6 ou 9 |
| 23 | Etapa agregada | c | 301–308 | obrigatório se tipo 6 ou 9 |
| 24 | Etapa | c | Tabela de Etapas | coerência mediação × tipo × etapa (Anexo 7); se etapa ≠ 1 exige docente (50 c7 = 1 ou 5) |
| 25 | Código do eixo do curso de qualificação profissional (novo 2026) | c | num 2 | |
| 26 | Código do curso | c | ≤ 8 | Tabela de Cursos da Educação Profissional |
| 27 | Carga horária total (horas) (novo 2026) | c | num ≤ 4 | só IFTP ou etapas 39, 40, 67, 68, 73, 75; Anexo 8 (ex.: técnico integrado ≥ 3.000 h; FIC ≥ 160 h) |
| 28 | Forma de organização da turma | c | 1–5 | nulo na EI; Anexo 6 |
| 29 | Formação por alternância | s | 0/1 | |
| 30–32 | Organização curricular: FGB, IFA, IFTP | c | 0/1 | só EM |
| 33–36 | Áreas do itinerário formativo | c | 0/1 | |
| 37–38 | Tipo e código do curso do IFTP | c | | |
| 39–65 | Componentes curriculares oferecidos (27 códigos) | c | 0/1 | |
| 66 | Turma de educação bilíngue de surdos | s | 0/1 | |

**Não existem no Censo**: data de início/fim da turma, turno codificado, vagas, ano/período letivo da turma (herda o ano letivo da escola, registro 00 c4–5), carga horária por componente, professor por componente com carga [I a partir de E02].

### 2.6 Registro 30: Pessoa física

| Campo | Nome | Obg. | Tipo / tamanho | Regras-chave |
|---|---|---|---|---|
| 3 | **Código da pessoa no sistema próprio** | s | alfa ≤ 20 | único na escola; liga 30 a 40/50/60 no arquivo |
| 4 | **Identificação única (INEP)** | n | num 12 fixo | única na escola; não pode ser de pessoa falecida; deve existir na base |
| 5 | **CPF** | c | num 11 | obrigatório para gestor (40), profissional (50) brasileiro (nacionalidade 1 ou 2) e aluno de EJA (etapas 67, 69–74); válido e não cancelado na Receita Federal; único na escola |
| 6 | Nome completo | s | A–Z ≤ 100 | se CPF informado, igual ao da Receita; senão ≥ 2 palavras, sem 5 caracteres iguais seguidos |
| 7 | Data de nascimento | s | data | ≤ data de referência; idades do Anexo 3; igual à Receita se CPF |
| 8–10 | Filiação (indicador, filiação 1, filiação 2) | s/c | | |
| 11 | Sexo | s | 1–2 | |
| 12–13 | Cor/raça; povo indígena | s/c | | |
| 14–16 | Nacionalidade; país; município de nascimento | s/c | | |
| 17–28 | Deficiência, TEA, AH/SD (indicador + 11 tipos) | s/c | 0/1 | indicador = 1 obrigatório se aluno em classe especial ou AEE; deficiência múltipla só com ≥ 2 |
| 29–35 | Transtorno que impacta a aprendizagem (indicador + 6 tipos) | c | 0/1 | só se houver vínculo 60 |
| 36–49 | Recursos para sala de aula e avaliações do INEP (Saeb) | c | 0/1 | só aluno com deficiência/TEA/transtorno; Anexo 4 |
| 50 | Matrícula da certidão de nascimento (certidão nova) | c | alfa 32 | só aluno; não pode repetir entre alunos |
| 51–55 | País e CEP de residência; município; zona; localização diferenciada | c/n | | |
| 56–69 | Escolaridade, tipo de EM, cursos superiores (até 3, com IES e ano), complementação pedagógica | c | | profissional/gestor |
| 70–88 | Pós-graduações (até 6) | c | | |
| 89–109 | Formação continuada ≥ 80 h (21 temas) | c | 0/1 | |
| 110 | E-mail | n | ≤ 100 | |

Campos comuns por papel (gestor, profissional, aluno): Anexo 2 do leiaute (E02).

### 2.7 Registro 40: Gestor escolar

Campos: escola INEP; código da pessoa no sistema próprio; ID INEP; **Cargo** (1 Diretor, 2 Outro cargo); **Critério de acesso** (1–7, só diretor); **Situação funcional/tipo de vínculo** (1–4). Até 3 por escola. Idade 18–95 (Anexo 3).

### 2.8 Registro 50: Profissional escolar em sala de aula × turma

| Campo | Nome | Obg. | Regras-chave |
|---|---|---|---|
| 3–4 | Código da pessoa; ID INEP | s/n | |
| 5 | Código da turma na escola | s | deve existir em um 20 |
| 6 | Código da turma – INEP | n | só exportação |
| 7 | Função que exerce na turma | s | 1–9 (restrições por tipo de turma e mediação) |
| 8 | Situação funcional/tipo de vínculo | c | só escola pública e função 1, 5, 6 |
| 9–33 | Áreas/componentes que leciona (até 25 códigos) | c | só função 1 ou 5; cada código precisa estar "oferecido" no 20 |
| 34–37 | Áreas do itinerário formativo | c | |
| 38 | Leciona no IFTP | c | |

Profissional fora de sala (diretor-adjunto, coordenador, secretário, psicólogo, etc.) **não é identificado individualmente**: só quantidade no registro 10 c119–138 (E02). Substituto: se o titular estiver afastado na data de referência e voltar em até 30 dias, informam-se os dois (E06 p. 85).

### 2.9 Registro 60: Aluno × turma (matrícula)

| Campo | Nome | Obg. | Regras-chave |
|---|---|---|---|
| 3–4 | Código da pessoa; ID INEP | s/n | ID igual ao do 30 correspondente |
| 5 | Código da turma na escola | s | deve existir em um 20 |
| 6 | Código da turma – INEP | n | só exportação |
| 7 | **Código da matrícula** | n | nulo na importação; só exportação |
| 8 | Turma multi (etapa do aluno) | c | obrigatório quando a etapa da turma é 3, 22, 23, 56, 64 ou 72 (ex.: turma 22 → 14–21, 41) |
| 9 | Carga horária integralizada pelo aluno (novo 2026) | c | só IFTP ou etapas 39, 40, 67, 68, 73, 75; 0 = nenhuma |
| 10–20 | Tipo de AEE (11 marcadores) | c | só turma tipo 5 |
| 21 | Escolarização em outro espaço | c | 1 não; 2 hospital; 3 domicílio |
| 22–33 | Transporte escolar público | c | |

### 2.10 2ª etapa: Situação do Aluno (leiaute 2025 v3)

| Registro | Campos | Conteúdo |
|---|---|---|
| 89 | 4 | Escola INEP; CPF do gestor; nome do gestor |
| 90 | 8 | Situação de vínculo existente: escola; código da turma na escola (opcional, não armazenado); **código da turma INEP** (≤ 10 dígitos); **ID INEP do aluno** (12); código do aluno na escola (não armazenado); **código da matrícula** (≤ 12, recebido na exportação); situação (1–8) |
| 91 | 10 | **Admissão após** (aluno que entrou depois da data de referência): escola; turma INEP (opcional); ID INEP do aluno; matrícula deve ser nula; mediação e etapa (quando sem turma INEP); situação |

Regras: um registro 90 por matrícula ativa de escolarização em turma que não seja itinerário exclusivo (regra 9); cada escola pode importar uma vez no período preliminar e uma vez na retificação (regra 11). Para alunos com mais de um vínculo de escolarização, o sistema escolhe a matrícula por critérios a–h (sem rendimento, mesma etapa, etapa equivalente, mesma mediação…) (E09 regras gerais). A situação só é registrada para a turma curricular; AEE, atividade complementar e itinerário exclusivo não têm rendimento (E10 §2.2).

### 2.11 Arquivo de identificação (pré-migração)

9 campos: código do aluno na escola (≤ 20, obrigatório); CPF; matrícula da certidão (32); nome; nascimento; filiação 1; filiação 2; município de nascimento (obrigatório); ID INEP (nulo, preenchido no retorno). Prioridade de busca: CPF → certidão → nome + nascimento + filiações + município. Retorna resultados "certos" e "prováveis" (E03; E05 3º e 4º passos).

---

## 3. CMDEB / API CMDEB v2: entidades e operações

Campos, tipos, ocorrências e domínios do CMDEB: [cmdeb/02-indice-variaveis.md](cmdeb/02-indice-variaveis.md) (156 variáveis). Aqui só o que falta para o desenho: entidades, chaves, operações e divergências entre Portaria e API.

### 3.1 Entidades e chaves

| Entidade CMDEB | Chave MEC | Chave da rede | Chaves externas | Relações |
|---|---|---|---|---|
| Estudante | `ID_SGP_ESTUDANTE` | — | `ESTUDANTE_CPF` [1..1], `ESTUDANTE_NIS` [0..1] | 1..2 responsáveis embutidos (nome, vínculo, CPF, contato) |
| Matrícula | `ID_SGP_MATRICULA` | `CO_MATRICULA_REDE` | `CO_ENTIDADE` (INEP escola) | N:1 estudante; 0..1 turma (`ID_SGP_TURMA`); 1 etapa; 1 ano (`NU_ANO_MATRICULA`) |
| Turma | `ID_SGP_TURMA` | `CO_TURMA_REDE` | `CO_ENTIDADE` | N componentes (`id_sgp_componente_curricular` como lista separada por `;` na API) |
| Componente curricular | `ID_SGP_COMPONENTE_CURRICULAR` | nome local | `CO_COMPONENTE_CURRICULAR` (código nacional = Censo) | carga horária total; sistema de avaliação |
| Frequência por componente (mensal) | matrícula + componente + mês + ano | | | horas ofertadas × horas presentes; justificativa de suspensão |
| Frequência por turma (mensal) | matrícula + mês + ano | | | idem |
| Avaliação de desempenho | matrícula + componente | | | resultado alfanumérico; aprovado/reprovado |
| Profissional | `ID_SGP_PROFISSIONAL` | `PROFISSIONAL_IDENTIFICACAO_INSTITUICAO` | `PROFISSIONAL_CPF` | 1..n formações (`ID_FORMACAO`); 1..n vínculos com a rede |
| Vínculo profissional × rede | (profissional + escola + função + datas) [I] | | `CO_ENTIDADE` | `CO_FUNCAO` [1..n]; tipo e situação do vínculo; datas de início/fim; carga semanal |
| Alocação profissional × turma × componente | (profissional + turma + componente) | | | é a **oferta** (C.OFR) que o Censo não tem |
| Instituição de ensino | `CO_ENTIDADE` (INEP) | — | `CNPJ_SECRETARIA_EDUCACAO` [1..1], `CNPJ_UNIDADE_EXECUTORA` [0..1] | etapas ofertadas [1..n] |

### 3.2 Operações (API v2)

Todas as escritas são **lotes assíncronos** (POST cria, PUT edita), consultados por `/api/v2/lotes/{id}` e `/erros` (E35, E36):

| Recurso | Operações |
|---|---|
| `/estudantes` | cadastro sem turma, cadastro com turma, edição de dados pessoais, listagem |
| `/matriculas` | enturmação, edição de enturmação, edição de matrícula, **movimentação** (muda situação), **confirmar conclusão** |
| `/frequencia-mensal-matricula/{ano}/{mes}` | cadastro e edição de lote, listagem, **faltantes**; matrículas inativas com frequência |
| `/turmas` | cadastro, edição, listagem; componentes de uma turma |
| `/componentes-curriculares` | cadastro, edição, listagem |
| `/avaliacao-desempenho` | cadastro, edição, listagem |
| `/profissionais` | cadastro, edição; funções; formações; enturmação (alocação a turma/componente) |
| `/instituicoes-ensino` | cadastro, edição, listagem |
| `/pessoas` | solicitações de alteração cadastral; validações cadastrais |
| `/pdm` | elegibilidades e incentivos do Pé-de-Meia (somente leitura) |
| `/auth` | login (CPF do operador + senha), refresh, termos de autorização |

Não há operação de exclusão de estudante ou matrícula; o encerramento é por movimentação com `data_fim` (E36) [I].

### 3.3 Divergências Portaria 832/2025 × API v2 (verificadas no OpenAPI em 2026-11-05)

| Item | Portaria (Anexo) | API v2 |
|---|---|---|
| `ESTUDANTE_QUILOMBOLA` | 0 Não; 1 Sim | 0 Não informado; 1 Sim; 2 Não |
| Situação da matrícula | inclui 19 e 23 (concluintes via Encceja) | 19 e 23 ausentes; adiciona `estudante_matricula_forma_conclusao` (1 Regular, 2 Encceja, 3 Enem, 4 Aceleração), obrigatório com 11 |
| Etapa do estudante | não inclui 3 (EI unificada) nem 22, 23, 56 | inclui 3, 22, 23, 56 na enturmação |
| Campos novos | — | `estudante_situacao_rua`, `turma_bilingue`, `estudante_co_uf_res` |
| Modalidade | atributo da turma | exigido também no cadastro de estudante sem turma |
| `CO_ENTIDADE` | "11 caracteres" no bloco 2.1; "8" no bloco 4 | "8 caracteres numéricos" |
| Telefone | `DDD-NNNNNNNNN` | `DDDNNNNNNNNN`, 11 a 12 dígitos |

---

## 4. Modelo conceitual Brasil (proposta para o adaptador) [I]

Síntese das duas fontes em entidades; cada linha aponta a origem. Cardinalidades: `1`, `0..1`, `1..n`, `0..n`.

### 4.1 Organização (D1)

| Entidade BR | Atributos principais | Identificadores | Cardinalidades | Origem |
|---|---|---|---|---|
| **Sistema de ensino** | esfera (federal, estadual/DF, municipal) | — | 1 por ente federado; escola privada de EB pertence ao sistema estadual (exceto EI privada, municipal) | LDB arts. 16–18 (E20) |
| **Rede** (ente mantenedor público) | dependência (1–3); UF; município | `CNPJ_SECRETARIA_EDUCACAO` (CMDEB); no Censo, derivada de dependência + UF/município | 1 rede : n escolas | E02 00 c21; E31 |
| **Órgão regional** | nome | código ≤ 5 por UF (Tabela de Órgãos Regionais) | 1 rede estadual : n órgãos; 1 escola : 0..1 | E02 00 c18; E04 |
| **Mantenedora privada** | tipo (6 marcadores), categoria (1–4) | CNPJ 14 | 1 mantenedora : n escolas | E02 00 c26–32, c47 |
| **Escola** (unidade escolar) | nome, endereço, zona, localização diferenciada, situação, dependência, ano letivo (início/fim) | **Código INEP 8 dígitos**; CNPJ (privada; unidade executora) | 1 escola : 0..n unidades vinculadas (via "escola sede") | E02 00 |
| **Unidade vinculada** | endereço próprio; sem gestão orçamentária | código INEP próprio + código da escola sede | n : 1 escola sede (mesma dependência e UF) | E02 00 c51–52; E06 p. 17 |
| **Local físico** (prédio, sala, dependência) | infraestrutura (reg. 10) | — (o Censo não identifica salas) | escola : 1..n locais; prédio compartilhado com até 6 escolas | E02 10 |
| **Ano letivo / período letivo** | data início, data fim | (escola, ano) no Censo; `DATA_INICIO_PERIODO_LETIVO` na turma (CMDEB) | escola : 1 ano letivo por ano de censo; turma : 1 período | E02 00 c4–5; E31 2.2 |
| **Turma** | nome, tipo, mediação, horário semanal (Censo) ou turno (CMDEB), etapa, forma de organização, organização curricular, local diferenciado, classe especial, bilíngue, alternância, vagas (CMDEB), datas (CMDEB) | código na escola (≤ 20); **código INEP da turma** (≤ 10, só exportação); `ID_SGP_TURMA`; `CO_TURMA_REDE` | escola : 1..1.500 turmas; turma : 1..n alunos; 1..n profissionais | E02 20; E31 |
| **Componente curricular** | código nacional (Tabela de Áreas), nome local, carga horária, sistema de avaliação | código nacional; `ID_SGP_COMPONENTE_CURRICULAR` | turma : 0..27 componentes oferecidos | E02 20 c39–65; E31 2.3 |
| **Oferta** (turma × componente × profissional) | carga, profissional | composta | só CMDEB (alocação); no Censo existe só profissional × turma com lista de componentes | E31 bloco 3; E02 50 c9–33 |

### 4.2 Pessoas e vínculos (D1, D3)

| Entidade BR | Atributos | Identificadores | Cardinalidades | Origem |
|---|---|---|---|---|
| **Pessoa** | nome, nome social (CMDEB), nascimento, sexo, cor/raça, povo indígena, nacionalidade, país, município de nascimento, filiação, residência, deficiência/TEA/AH-SD, transtornos | **ID INEP (12)**; **CPF (11) = Inue**; certidão nova (32); NIS (CMDEB); código no sistema próprio (≤ 20, por escola); `ID_SGP_ESTUDANTE` / `ID_SGP_PROFISSIONAL` | 1 pessoa : n papéis | E02 30; E21; E30; E31 |
| **Responsável** | nome, vínculo (0–5), CPF, contato | CPF (opcional) | estudante : 1..2 (CMDEB); Censo só tem filiação textual | E31 bloco 1 |
| **Matrícula / vínculo de aluno** | etapa, ano, data início, data fim, situação, tempo integral, apoio pedagógico, AEE, turma multi, carga integralizada, escolarização em outro espaço, transporte | código INEP da matrícula (≤ 12); `ID_SGP_MATRICULA`; `CO_MATRICULA_REDE` | aluno : 0..n matrículas por ano; Censo limita ≤ 4 com etapa, ≤ 2 com etapa fora de 39/40/64/68, ≤ 4 AEE/atividade complementar | E02 60, regras 32–34; E31 2.1 |
| **Situação da matrícula** (evento) | código, data, forma de conclusão | — | matrícula : 1 situação final por ano (Censo) ou n eventos (CMDEB) | E09; E36 |
| **Vínculo de gestor** | cargo, critério de acesso, tipo de vínculo | — | escola : 1..3 | E02 40 |
| **Vínculo profissional × turma** | função (1–9), tipo de vínculo, componentes, itinerários | — | turma : 1..n; pessoa : 0..n | E02 50 |
| **Vínculo profissional × rede** | função [1..n], tipo e situação de vínculo, datas, carga semanal, escola de lotação | — | só CMDEB | E31 bloco 3 |
| **Formação do profissional** | escolaridade, cursos superiores, pós, formação continuada | `ID_FORMACAO` (CMDEB) | pessoa : 0..n | E02 30 c56–109; E31 |

### 4.3 Registros de acompanhamento (D3)

| Entidade BR | Atributos | Granularidade | Origem |
|---|---|---|---|
| Frequência | horas ofertadas, horas presentes, justificativa de suspensão | mensal, por matrícula × turma ou × componente | CMDEB 2.4 (E31) |
| Avaliação de desempenho | resultado, situação | por matrícula × componente (período não especificado) | CMDEB 2.5 |
| Rendimento/movimento anual | situação 1–8 | por matrícula de escolarização × ano | Censo 2ª etapa (E09) |
| Necessidade de apoio | deficiência, transtornos, recursos Saeb, AEE, apoio pedagógico | por pessoa (Censo 30) e por matrícula (CMDEB) | E02; E31 (detalhe normativo: frente de inclusão) |

---

## 5. Restrições legais de organização (LDB) que viram regra de validação

Fonte: Lei 9.394/1996 compilada (E20), lida em paráfrase; conferir redação literal antes de citar.

| Regra | Artigo | Uso no modelo |
|---|---|---|
| Educação escolar = educação básica (EI, EF, EM) + educação superior | art. 21 | níveis/etapas de `C.PRG` |
| EB obrigatória e gratuita dos 4 aos 17 anos | art. 4º I | alerta de matrícula ausente [I] |
| EI: creche até 3 anos; pré-escola 4–5 anos | art. 30 | etapas 1 e 2 |
| EI: avaliação por acompanhamento e registro, sem promoção; ≥ 800 h/ano em ≥ 200 dias; jornada ≥ 4 h (parcial) ou 7 h (integral); frequência mínima 60% | art. 31 | situação EI sem aprovado/reprovado (coerente com E09); regra de frequência EI |
| EF obrigatório, início aos 6 anos, duração mínima 9 anos | art. 32 | etapas 14–21, 41 |
| EF: jornada ≥ 4 h de efetivo trabalho em sala | art. 34 | validação de horário da turma [I] |
| EM: duração mínima 3 anos | art. 35 | etapas 25–29 |
| Organização em séries anuais, períodos semestrais, ciclos, alternância regular, grupos não seriados (idade, competência) ou outra forma | art. 23 caput | `forma_organizacao` (5 códigos + alternância) |
| Reclassificação, inclusive na transferência | art. 23 §1 | situação CMDEB 9 "Reclassificação" |
| Calendário adequado às peculiaridades locais sem reduzir carga horária | art. 23 §2 | calendário por escola/rede, não nacional |
| Carga mínima anual: 800 h (EF) e 1.000 h (EM), em ≥ 200 dias letivos | art. 24 I | validação de calendário e de carga |
| Classificação por promoção, transferência ou avaliação da escola (exceto 1º ano do EF) | art. 24 II | origem da matrícula [I] |
| Progressão parcial permitida no regime seriado | art. 24 III | Censo: aluno em dependência = "Aprovado" (E10 §5.2) |
| Classes com alunos de séries distintas para línguas, artes ou outros componentes | art. 24 IV | turma multi/agrupamento por componente |
| Frequência mínima de 75% do total de horas letivas para aprovação | art. 24 VI | regra de rendimento a partir da frequência CMDEB |
| Escola expede históricos, declarações de conclusão, diplomas/certificados | art. 24 VII | `C.CRD` |
| Base nacional comum + parte diversificada | art. 26 | componentes (frente de currículo) |
| EJA para quem não teve acesso ou continuidade na idade própria | art. 37 | etapas 69–74, 67 |
| Educação especial: modalidade, preferencialmente na rede regular, da EI ao longo da vida | art. 58 | classe especial, AEE (frente de inclusão) |
| Cadastro nacional de alunos com altas habilidades/superdotação | art. 59-A | identificador/registro adicional (não localizado como sistema) |
| Profissionais da educação básica: categorias I a V | art. 61 | `C.STF` (CMDEB usa art. 61 como definição, Portaria 832 art. 13 §5º) |
| Sistemas: federal, estaduais/DF, municipais e seus componentes | arts. 8º, 16–18 | `C.ORG` tipo "sistema"; escola privada de EF/EM no sistema estadual |

---

## 6. Resolução de identidade e chaves para o adaptador [I]

1. **Pessoa**: chave de negócio preferencial = **CPF** (Inue, LC 220 art. 26 I; Portaria 269 art. 7º). Fallbacks: ID INEP (12) → certidão nova (32) → nome + nascimento + filiação + município de nascimento (mesma ordem do INEP, E02 regras 37–40; E03). Guardar todos como `C.IDN` com `scheme` (`br-cpf`, `br-inep-pessoa`, `br-certidao`, `br-sgp-estudante`, `br-sgp-profissional`, `br-sp-ra`…).
2. **Escola**: código INEP (8) como chave; CNPJ como identificador secundário.
3. **Turma**: o identificador INEP só existe **depois** da importação e muda por ano; usar chave própria e mapear `br-inep-turma`, `br-sgp-turma`, `br-rede-turma` por ano.
4. **Matrícula**: idem (código INEP da matrícula só na exportação; `ID_SGP_MATRICULA` gerado pelo MEC).
5. **Ano**: toda chave de turma/matrícula é qualificada pelo ano do censo; o leiaute muda a cada ano (ex.: tipo de turma 2025 → 2026), logo o adaptador precisa de versões por ano.
