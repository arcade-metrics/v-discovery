# Modelo de dados — China

Entidades, atributos, identificadores e cardinalidades das normas de dados educacionais chinesas efetivamente lidas. Pesquisa de 2026-11-05; chaves `[Cxx]` em [evidencias.md](evidencias.md). Estado da jurisdição: **standby** (ver [README.md](README.md)). Transcrevemos campo a campo só o que foi visto no texto (JY/T 0633, 0637, 0639 e 0641, todas de 2022); o resto fica `not_found`.

## 1. Arquitetura das normas de dados (2022)

| Norma | Título oficial | Tradução | Papel no conjunto |
|---|---|---|---|
| JY/T 0633—2022 | 教育基础数据 | Dados básicos da educação (inglês oficial: *Common education data*) | núcleo: escola (instituição), pessoa, extensão de estudante e de servidor |
| JY/T 0637—2022 | 教育系统人员基础数据 | Dados básicos de pessoas do sistema educacional (*General personnel data in education system*) | estende a pessoa: família, contato, trajetória escolar, trajetória profissional |
| JY/T 0639—2022 | 中小学校基础数据 | Dados básicos de escolas primárias e secundárias (*Common data specification for primary and secondary schools*) | estende a escola de educação básica: perfil, **contagens** de alunos e servidores, condições de funcionamento |

Fontes: [C01], [C02], [C03]. As três foram publicadas e entraram em vigor em 2022-11-30 (capa) e não declaram substituir nenhuma norma (o prefácio não traz cláusula de substituição, e o cadastro SAMR mostra `REVISE_STD_CODES` vazio) [C01–C03, C06].

**Origem dos elementos.** A JY/T 0633 declara que seus elementos vêm "principalmente" da GB/T 33782—2017 (códigos básicos de gestão educacional) e da GB/T 35298—2017 (informação básica de gestão educacional), com acréscimos [C01, introdução]. Essas duas GB/T não foram lidas (ver [questoes-abertas.md](questoes-abertas.md), QA-03).

**Metaestrutura comum dos elementos** (idêntica nas três normas; JY/T 0633 §4.2, 0637 §5, 0639 §4.2):

| Atributo do elemento | Valores |
|---|---|
| 编号 (número) | identificador do elemento dentro da norma (ex.: `1.1`, `2.2.1`) |
| 中文名称 | nome em chinês |
| 约束 | `M` 必备 (obrigatório) / `O` 可选 (opcional) |
| 数据类型 | `C` string, `N` numérico, `D` data (GB/T 7408), `B` binário, `S` conjunto (aninhável); a 0639 acrescenta `M` 币值型 (moeda: moeda+unidade+valor, 4 casas decimais) e não usa `B` |
| 数据格式 | `a` caractere, `n` número; `a10` fixo, `a..100` até 100, `..ul` ilimitado, `n9,2`, `YYYYMMDD`/`YYYYMM` |
| 值域 | por referência a norma, por texto, por enumeração, por regra ou sem restrição |
| 说明 | explicação |

Observação [I]: na 0639 a letra `M` serve tanto para "obrigatório" (约束) quanto para o tipo moeda (数据类型); um importador precisa ler a coluna, não a letra.

Não há esquema XML/JSON, API nem regra de serialização em nenhuma das três normas: são **dicionários de dados** em tabela [C01–C03].

## 2. Escola / instituição — 学校（机构）基础数据类 (JY/T 0633, tabela 2)

| Nº | Elemento | Trad. | M/O | Tipo/formato | Valor / regra |
|---|---|---|---|---|---|
| 1.1 | 学校（机构）标识码 | código de identificação da escola/instituição | M | C a10 | GB/T 33782—2017 §4.1; "教育行政部门统一编制的全国范围内终身唯一的标识码" |
| 1.2 | 统一社会信用代码 | código unificado de crédito social | M | C a18 | GB 32100 (18 posições: órgão de registro, região, código da organização, dígito verificador) |
| 1.3 | 学校（机构）名称 | nome | M | C a..100 | nome padrão em chinês, igual ao do selo oficial |
| 1.4 | 学校（机构）英文名称 | nome em inglês | O | C a..180 | |
| 1.5 | 学校（机构）地址 | endereço | M | C a..180 | província/município/condado/distrito/rua/número |
| 1.6 | 邮政编码 | CEP | M | C a6 | |
| 1.7 | 行政区划码 | código de divisão administrativa | M | C a6 | GB/T 2260 |
| 1.8 | 所在地城乡类型码 | tipo urbano/rural | M | C a3 | GB/T 33782—2017, tabela 5 |
| 1.9 | 成立时间 | data de fundação | M | D YYYYMMDD | |
| 1.10 | 办学类型码 | tipo de escola | M | C a3 | GB/T 33782—2017, tabela 4 |
| 1.11 | 举办者码 | categoria do mantenedor | M | C a3 | GB/T 33782—2017 §5.2.9 |
| 1.12 | 主管部门码 | órgão supervisor | M | C a3 | GB/T 33782—2017 §5.2.9 |
| 1.13 | 法定代表人姓名 | representante legal | M | C a..50 | |
| 1.14 | 办学（园）许可证书号 | nº da licença de funcionamento | O | C a15 | escolas privadas (民办) |
| 1.15 | 党组织负责人姓名 | responsável pela organização do PCCh | O | C a..50 | |
| 1.16 | 行政负责人姓名 | dirigente administrativo | M | C a..50 | |
| 1.17 | 联系电话 | telefone | M | C a..30 | |
| 1.18 | 电子邮箱 | e-mail | O | C a..100 | |
| 1.19 | 校区基本信息 | campi | M | S | GB/T 35298—2017, tabela 15: {nº do campus, nome, endereço, CEP, telefone, fax, responsável} |

Nota da norma: tabela derivada da GB/T 35298—2017, tabela 14, com modificações [C01].

**Cardinalidade [I]:** escola 1—N campus (conjunto `S`). Não há elemento de hierarquia entre instituições além do código do órgão supervisor (1.12); rede/mantenedora não são entidades.

## 3. Pessoa — 人员基础数据类 (JY/T 0633, tabela 3)

Usado para **estudantes e servidores** (§5.3.1 e §5.4.1 remetem à tabela 3) e para toda pessoa do sistema na JY/T 0637 (§6.2) [C01, C02].

| Nº | Elemento | Trad. | M/O | Tipo/formato | Valor / regra |
|---|---|---|---|---|---|
| 2.1 | 个人标识码 | código de identificação pessoal | M | C a19 | "由教育行政部门统一编码，全国范围内终身唯一的个人识别标识码" |
| 2.2 | 姓名 | nome (conjunto) | M | S | nome do documento de identidade |
| 2.2.1 | 中文姓名 | nome chinês | M | C a..50 | estrangeiro sem nome chinês: "无中文名" |
| 2.2.2 | 姓名拼音 | pinyin | M | C a..100 | GB/T 28039 (ex.: "Zhang San") |
| 2.2.3 | 外文姓名 | nome estrangeiro | O | C a..100 | obrigatório para estrangeiros |
| 2.2.4 | 曾用名 | nome anterior | O | C a..100 | |
| 2.3 | 性别码 | sexo | M | C a1 | GB/T 2261.1 |
| 2.4 | 出生日期 | nascimento | M | D YYYYMMDD | |
| 2.5 | 出生地码 | local de nascimento | O | C a6 | GB/T 2260 |
| 2.6 | 籍贯码 | origem ancestral (籍贯) | O | C a6 | GB/T 2260 (registro domiciliar do avô paterno) |
| 2.7 | 民族码 | etnia | M | C a2 | GB/T 3304; "0" = desconhecido/não informado |
| 2.8 | 国籍/地区码 | nacionalidade/região | M | C a3 | GB/T 2659 |
| 2.9 | 户口类别代码 | tipo de registro domiciliar (户口) | O | C a1 | GA 324.1 |
| 2.10 | 户口所在地码 | local do 户口 | O | C a6 | GB/T 2260 |
| 2.11 | 身份证件类型码 | tipo de documento | M | C a1 | GB/T 29808—2013 §7.100 |
| 2.12 | 身份证件号 | nº do documento | M | C a..20 | ex.: número de cidadão |
| 2.13 | 港澳台侨外码 | vínculo HK/Macau/Taiwan/ultramar | O | C a2 | GB/T 29808—2013 §7.26 |
| 2.14 | 政治面貌码 | filiação política | M | C a5 | GB/T 4762 |
| 2.15 | 婚姻状况码 | estado civil | O | C a2 | GB/T 2261.2 |
| 2.16 | 健康状况码 | estado de saúde | O | C a2 | GB/T 2261.3 |
| 2.17 | 照片 | foto 3×4 | O | B | |
| 2.18 | 照片上传日期 | data da foto | O | D | |
| 2.19 | 最高学历码 | maior escolaridade | O | C a2 | GB/T 4658 |
| 2.20 | 所学专业码 | área de formação | O | C a6 | catálogos de disciplinas/cursos do MOE |
| 2.21 | 获得最高学位码 | maior grau | O | C a3 | GB/T 6864 |
| 2.22–2.25 | 授学位学校名称/代码, 学位专业码, 授位国家/地区码 | instituição, curso e país do grau | O | | GB 32100, GB/T 2659 |
| 2.26 | 境外获得最高学历学位 | formação no exterior | O | C a..500 | texto livre formatado |

Atributos sensíveis do ponto de vista da PIPL/JY/T 0661 [I]: 2.7 etnia, 2.14 filiação política, 2.16 saúde, 2.17 foto (biometria se usada para reconhecimento facial), 2.12 documento; e **todos** os dados de menores de 14 anos (PIPL art. 28) [C13, C05].

## 4. Extensão de estudante — 学生扩展信息数据子类 (JY/T 0633, tabela 4)

| Nº | Elemento | Trad. | M/O | Tipo/formato | Valor / regra |
|---|---|---|---|---|---|
| 3.1 | 学生类别码 | categoria de estudante | M | C a5 | GB/T 33782—2017, tabela 24; "cinco níveis, cinco dígitos" |
| 3.2 | 现就读学校（机构）标识码 | escola onde estuda | M | C a10 | GB/T 33782—2017 §4.1 |
| 3.3 | 所属学校（机构）标识码 | escola a que pertence | M | C a10 | idem |
| 3.4 | 所学专业名称 | curso | O | C a..50 | catálogos de cursos (relevante p/ médio técnico e superior) |
| 3.5 | 入学年月 | ingresso | M | D YYYYMM | |
| 3.6 | 学制 | duração regulamentar (anos) | M | N n3,1 | |
| 3.7 | 学习方式码 | regime (tempo integral etc.) | M | C a2 | anexo A.1 |
| 3.8 | 学习形式码 | forma de estudo | O | C a4 | GA/T 2000.169 |
| 3.9 | 结束学业年月 | término | M | D YYYYMM | |
| 3.10 | 联系人关系码 | relação do contato | M | C a2 | GB/T 4761 (relações familiares) |
| 3.11 | 联系人姓名 | nome do contato | M | C a..50 | |
| 3.12 | 联系人电话 | telefone do contato | M | C a..30 | |

Observações [I]:
- 3.2 × 3.3 distinguem "escola onde está de fato" e "escola a que pertence": é a mesma separação que o 学籍 faz entre matrícula registrada e frequência (o regulamento de 2025 combate o 人籍分离, separação pessoa/registro) [C11]. No Core isso pede duas relações C.ENR ou um atributo de papel na matrícula.
- Não há turma, série/ano, componente, oferta, horário nem situação de matrícula na JY/T 0633. **Turma (班级) e curso/oferta (课程) não aparecem em nenhuma das três normas lidas** (`not_found`). A tabela A.1 da JY/T 0661 cita 学籍数据, 选课数据, 排课数据 como categorias de dados, mas sem modelo [C05].
- O responsável aparece só como "contato" (3.10–3.12), sem entidade própria; a entidade de família está na JY/T 0637 (§5 abaixo).

## 5. Extensão de servidor — 教职工扩展信息数据子类 (JY/T 0633, tabela 5)

| Nº | Elemento | Trad. | M/O | Formato | Valor |
|---|---|---|---|---|---|
| 4.1 | 联系电话号码 | telefone | M | a..30 | |
| 4.2 | 学校（机构）标识码 | escola | M | a10 | GB/T 33782 §4.1 |
| 4.3 | 参加工作年月 | início da vida profissional | M | YYYYMM | |
| 4.4 | 入职年月 | entrada nesta escola | M | YYYYMM | |
| 4.5 | 来源码 | origem | M | a3 | GB/T 33782, tabela 64 |
| 4.6 | 来源地区码 | região de origem | M | a6 | GB/T 2260 |
| 4.7 | 类别码 | categoria de servidor | M | a2 | GB/T 33782, tabela 63 |
| 4.8 | 是否在编 | servidor efetivo (编制) | M | a1 | 0/1 |
| 4.9 | 用人形式码 | forma de contratação | M | a1 | anexo A.2; quando 4.8 = 0 |
| 4.10 | 签订合同情况码 | tipo de contrato | M | a1 | anexo A.3 |
| 4.11 | 是否县级以上骨干教师 | professor-referência (nível ≥ condado) | O | a1 | 0/1 |
| 4.12 | 是否师范类专业毕业 | formado em licenciatura | O | a1 | 0/1 |
| 4.13 | 是否免费(公费)师范生 | bolsista de licenciatura pública | O | a1 | anexo A.4 |
| 4.14 | 是否特岗教师 | professor do programa de postos especiais | O | a1 | anexo A.5 |
| 4.15 | 是否受过特教专业培养培训 | formação em educação especial | O | a1 | 0/1 |
| 4.16 | 是否有特殊教育从业证书 | certificado de educação especial | O | a1 | 0/1 |
| 4.17 | 是否心理健康教师 | professor de saúde mental | O | a1 | anexo A.6 |
| 4.18 | 党政职务类别码 | cargo partidário/administrativo | O | a2 | GB/T 29808 §7.159 |
| 4.19 | 工人技术等级码 | nível técnico (operários) | O | a1 | GB/T 14946.2—2019 |
| 4.20 | 聘任专业技术职务 | cargo técnico-profissional | O | a3 | GB/T 8561 |
| 4.21 | 教师资格证 | nº(s) do certificado de qualificação docente | M | a..100 | vários separados por vírgula; "0" se não tiver |
| 4.22 | 是否专任教师 | professor regente | M | a1 | 0/1 |
| 4.23 | 教职工状态 | situação funcional | M | a2 | anexo A.7 |

Identificação de docentes: o professor usa o mesmo 个人标识码 (2.1) da pessoa; o certificado de qualificação docente (4.21) é um segundo identificador com regra própria não lida (`not_found`). Um "número nacional do professor" separado não foi localizado em fonte oficial (`not_found`; ver QA-06).

## 6. Pessoa estendida — JY/T 0637 (tabelas 2–5)

Modelo de informação (§4): 人员基本数据类 (= JY/T 0633 tabela 3) + quatro classes [C02].

| Classe | Elementos (M em negrito) | Cardinalidade [I] |
|---|---|---|
| 家庭成员数据类 (membros da família) | **2.1 家庭关系码** (GB/T 4761), **2.2 姓名**, 2.3 民族码, 2.4 工作单位, 2.5 通信地址, 2.6 电话号码, 2.7 电子邮箱 | pessoa 1—N familiares; familiar não tem identificador |
| 联系方式数据类 (contato) | **3.1 电话**, 3.2 e-mail, **3.3 endereço postal**, 3.4 CEP, 3.5 户籍地址, 3.6 常住地址, 3.7 即时通讯号 ("微信：ABC123；QQ：1234"), **3.8 联系人姓名**, **3.9 联系人关系码**, 3.10 endereço, **3.11 telefone**, 3.12 e-mail do contato | 1—1 |
| 学习经历数据类 (trajetória escolar) | **4.1 起始年月**, **4.2 终止年月**, **4.3 学段** (anexo A.1), **4.4 学校名称**, **4.5 学校标识码** (a10), 4.6 专业码, 4.7 学历代码 (GB/T 4658), 4.8 学位代码, 4.9 exterior, 4.10 学习概况 (resumo: conteúdos, avaliações; a..1000) | pessoa 1—N períodos com vigência |
| 工作经历数据类 (trajetória profissional) | **5.1/5.2 início/fim**, **5.3 工作单位**, **5.4 工作单位代码** (GB 32100; "0" se não houver), **5.5 país**, **5.6 单位性质** (anexo A.2), 5.7 resumo, 5.8 职务代码 (GB/T 12403), 5.9 职级代码 (GB/T 12407), 5.10 职称代码 (GB/T 8561) | pessoa 1—N |

§6.7: os elementos "podem ser estendidos conforme a necessidade do negócio"; nenhum mecanismo formal de extensão é definido [C02].

## 7. Escola de educação básica — JY/T 0639 (agregados)

A JY/T 0639 (escopo: 小学、初中和普通高中) reutiliza a escola da JY/T 0633 e acrescenta **contagens**, não registros individuais [C03]:

| Classe | Conteúdo | Nº de elementos |
|---|---|---|
| 学校概要扩展 (perfil) | 1.1 校庆日 aniversário, 1.2 校长姓名 diretor, 1.3 fax, 1.4 主页地址 site, 1.5 历史沿革 histórico | 5 |
| 学生管理基础 (alunos) | 2.1 matriculados (com 学籍 registrado no início do ano), 2.2 meninas, 2.3 minorias étnicas, 2.4 distribuição por **ano 1–12** (`{一年级:人数;…;十二年级:人数}`), 2.5 por idade (faixas próprias de primário, ginásio e médio), 2.6 internos, 2.7 filhos de migrantes, 2.8 filhos de trabalhadores migrantes, 2.9 crianças rurais deixadas para trás (留守儿童), **2.10 特殊教育在校生数 (estudantes de educação especial em classe comum, 随班就读)**, 2.11 aptidão física aprovada, 2.12 visão deficiente, 2.13 concluintes, 2.14 ingressantes | 14 |
| 教职工管理基础 (servidores) | totais por categoria (regente, apoio pedagógico, administrativo, serviços), por sexo, etnia, escolaridade, cargo técnico (5 níveis + não definido), faixa etária, disciplina lecionada (`{学科:人数}`), filiação ao PCCh, referência, saúde mental, movimentação | 14 (+ subelementos) |
| 办学条件基础 (condições) | patrimônio (moeda, 10 mil yuan), áreas (m²), salas por uso (`{教室:数量,面积;实验室:…}`), salas multimídia, nº de terminais digitais, acervo, recursos digitais, conformidade de equipamentos (0/1), banda do campus (Mbps), rede/wi-fi (0/1) | 21 |

Os três grupos admitem "extensão por atributo" (§5.2.2, 5.3.2, 5.4.2) sem mecanismo definido. Elementos com valor tipo `{chave:número;…}` são **strings com microformato**, não estruturas [C03].

Leitura para o Core [I]: a JY/T 0639 é um formulário estatístico de escola (parecido com partes do Censo Escolar brasileiro), não um modelo transacional. O Core não tem entidade de indicador agregado (ver [crosswalk-core.md](crosswalk-core.md) e QA-10).

## 8. Plataforma — conta e autorização (JY/T 0641)

A JY/T 0641—2022 (智慧教育平台 基本功能要求) é norma funcional, não de dados, mas fixa a identidade do usuário da plataforma nacional [C04 §6.1]:

| Conceito | Regra |
|---|---|
| 通行证 (passe) | "identidade do usuário após autenticação unificada" (§3) |
| Registro | informações básicas obrigatórias: **papel** (estudante, professor, pais, servidor escolar, servidor da administração educacional, outros), nome, escola/instituição; informações de conta: **tipo e número de documento** (RIC chinês, autorização de residência HK/Macau/Taiwan, passaporte) e **celular**; "完成平台服务体系的实名认证" (autenticação com nome real) |
| Login | senha ou SMS |
| Autorização (授权管理) | ao entrar pela 1ª vez em outra plataforma conectada, vincula a conta; o conteúdo autorizado inclui nome, sexo, escola, província/cidade/distrito e ID do passe; o usuário vê e revoga autorizações |
| Recomendação | modelagem de usuário por cliques, visualizações, reprodução, curtidas, favoritos, comentários (§6.5) |

Cardinalidade [I]: pessoa 1—1 passe; passe 1—N autorizações a plataformas, cada uma com data e estado. Não há protocolo técnico (OAuth/OIDC/SAML não citados): `not_found`.

## 9. Identificadores

| Identificador | Objeto | Formato | Atribuição | Fonte |
|---|---|---|---|---|
| 学校（机构）标识码 | escola/instituição | a10 | órgão educacional, único nacional e vitalício; regra de composição na GB/T 33782—2017 §4.1 (não lida) | [C01] |
| 统一社会信用代码 | pessoa jurídica | a18 | GB 32100 | [C01] |
| 个人标识码 | pessoa (aluno, servidor) | a19 | órgão educacional, único nacional e vitalício; regra de composição `not_found` | [C01] |
| 学籍号 | estudante (registro escolar nacional) | `not_found` em fonte oficial | "gerado e atribuído automaticamente pelo sistema nacional de 学籍 segundo regras próprias, um por pessoa, vitalício" (art. 8) | [C11] |
| 学籍号 (fonte secundária) | idem | prefixo G + nº do documento de identidade; L = provisório; J = sem documento válido | relato jornalístico de 2016 | [C12] secundária |
| 身份证件号 | pessoa | a..20 | documento civil | [C01] |
| 教师资格证号 | professor | a..100 (lista) | `not_found` | [C01] |
| 通行证 ID | conta na plataforma nacional | `not_found` | autenticação unificada com documento e celular | [C04] |

Relação [I]: o 个人标识码 tem 19 posições e o 学籍号 descrito pela fonte secundária tem 1 letra + 18 dígitos (19); **não há fonte oficial dizendo que são o mesmo identificador** (QA-05).

## 10. Classificação dos dados (JY/T 0661—2025)

Não é modelo de entidades, mas impõe um **atributo de classe e nível por conjunto de dados** que o Core precisa carregar [C05]:

- Classes de escola (§5.2): 学生数据, 教职工数据, 教学管理数据, 科研管理数据, 校务管理数据, 其他数据, com subclasses no anexo B.
- Níveis (§6): L5 dados centrais, L4 dados importantes, L3–L1 dados gerais. Regras que alcançam uma plataforma como a VUOO: dados pessoais de < 100 mil pessoas ou dados sensíveis de < 10 mil → L1; dados de aluno, servidor e ensino de uma escola básica inteira → L2; dados pessoais de 1–10 milhões ou sensíveis de 100 mil–1 milhão → L3; "dados básicos educacionais de abrangência provincial" → L4; "de abrangência nacional" → L5.
- Princípios: cada conjunto em uma só classe e um só nível; "就高从严" (vale o nível mais alto); atualização dinâmica.
- Fluxo (§7): inventário → classificação → **catálogos de dados centrais e importantes enviados ao MOE para aprovação**; catálogos de dados gerais registrados no órgão superior.

Consequência [I]: o Core precisa de um rótulo de classificação por conjunto de dados (não por campo), herdado pelo nível mais alto; ver QA-11 e [crosswalk-core.md](crosswalk-core.md).

## 11. Currículo (D2/D4)

Estrutura do currículo da educação obrigatória (课程方案 2022) em [fichas/curriculo-obrigatorio-2022.md](fichas/curriculo-obrigatorio-2022.md). Resumo de modelo [I]:

- C.CFW: 课程方案 (plano) + 16 课程标准 (padrões por disciplina), versão "2022年版", com três níveis de emissor: 国家课程 (nacional), 地方课程 (provincial), 校本课程 (escolar).
- C.PRG: 9 anos (一至九年级), estrutura "六三" (6+3) ou "五四" (5+4); 学段 (segmentos) nos padrões das disciplinas. Correspondência com ISCED 2011 (小学 = 100, 普通初中 = 244, 普通高中 = 344, 职业高中 = 354) já transcrita em [../internacional/mapeamentos-isced.md §5](../../camada-agnostica/internacional/mapeamentos-isced.md) [C28]; não repetida aqui.
- C.SUB: 12 linhas de disciplinas nacionais na tabela 1 (ver terminologia).
- C.CMP: 核心素养 (competências nucleares) por disciplina, 课程内容 e 学业质量 (padrão de qualidade acadêmica). A codificação de itens dentro dos padrões não foi verificada (QA-14); **não foi localizada versão legível por máquina** (`not_found`).

## 12. O que não foi encontrado

| Item pedido | Situação |
|---|---|
| JY/T 0634-2022 e JY/T 0635-2022 | não localizadas no cadastro SAMR nem em busca (QA-01) |
| Turma (班级), curso/oferta (课程开设), horário, sala | ausentes das normas lidas; podem estar na JY/T 1004-2012 (não lida) |
| Regra de composição do 学校标识码 e do 个人标识码 | em GB/T 33782—2017 §4.1 (não lida) |
| Formato oficial do 学籍号 | não publicado no regulamento de 2025 |
| Esquemas, APIs, payloads, regras de validação além de formato | inexistentes nas normas lidas |
| Educação especial individual (D7) | só contagem agregada (JY/T 0639, 2.10) e qualificação do professor (0633, 4.15–4.16) |
