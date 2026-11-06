# Terminologia — China

Conceitos, falsos amigos e vocabulários controlados com códigos, quando o código foi visto na fonte. Pesquisa de 2026-11-05; chaves `[Cxx]` em [evidencias.md](evidencias.md). Traduções são desta pesquisa.

## 1. Conceitos

| Termo | Pinyin | Tradução | Definição / uso | Fonte | Cuidado |
|---|---|---|---|---|---|
| 教育基础数据 | jiàoyù jīchǔ shùjù | dados básicos da educação | elementos "de alta frequência, gerais e centrais" dos sistemas de informação educacional | [C01] | não é "dados básicos" no sentido de mínimos; é o núcleo compartilhado |
| 数据元素 / 数据集 / 数据类 | | elemento / conjunto / classe de dados | metaestrutura das normas JY/T de dados | [C01] | "数据类" agrupa elementos, não é classe de objeto |
| 学校（机构） | | escola (instituição) | qualquer instituição educacional, inclusive órgãos | [C01] | inclui unidades não escolares |
| 校区 | xiàoqū | campus | unidade física de uma escola, conjunto dentro da escola | [C01] | não é escola separada |
| 学籍 | xuéjí | registro escolar / situação de matrícula | registro nacional do estudante; regime "一人一籍、籍随人走" (um registro por pessoa, que acompanha a pessoa) | [C11] | mais amplo que matrícula em turma; é vínculo administrativo nacional |
| 学籍号 | xuéjí hào | número de registro escolar | "一人一号，终身不变", gerado pelo sistema nacional | [C11] | formato não publicado oficialmente |
| 国家学籍系统 | | sistema nacional de 学籍 | 国家中小学生学籍信息管理系统; implantação centralizada, uso em 5 níveis (central, província, cidade, condado, escola) | [C11] | |
| 人籍分离 / 空挂学籍 | | separação pessoa-registro / registro "pendurado" | aluno frequenta escola diferente da do registro / registro sem aluno | [C11] | o regulamento de 2025 manda corrigir |
| 转学 | zhuǎnxué | transferência | iniciada pela escola de destino no sistema nacional; 10 dias úteis por nível | [C11] | |
| 学生可信教育数字身份 | | identidade digital educacional confiável do estudante | identidade baseada no 学籍 para reconhecimento e compartilhamento entre sistemas | [C11 art. 24] | conceito, sem especificação localizada |
| 个人标识码 | | código de identificação pessoal | a19, único nacional e vitalício | [C01] | relação com 学籍号 não confirmada |
| 学校标识码 | | código de identificação da escola | a10, único nacional e vitalício | [C01] | |
| 教职工 / 专任教师 | | servidores / professor regente | 专任教师 = professor com docência como função principal | [C01, C03] | "教职工" inclui apoio e administrativo |
| 在编 | zàibiān | efetivo (dentro da quota de cargos públicos, 编制) | | [C01] | sem equivalente direto no Brasil; ≈ servidor efetivo |
| 骨干教师 | | professor-referência | reconhecido em nível de condado ou superior | [C01] | |
| 特岗教师 | | professor do programa de postos especiais | | [C01] | programa nacional para áreas rurais [I] |
| 学段 | xuéduàn | segmento/etapa | anexo A.1 da JY/T 0637; nos padrões curriculares, faixa de anos | [C02, C26] | dois usos diferentes (etapa de ensino × faixa de anos) |
| 学制 | xuézhì | sistema de anos / duração | "六三" (6 primário + 3 ginásio) ou "五四" (5+4); na JY/T 0633, 3.6 = duração regulamentar em anos | [C26, C01] | |
| 年级 | niánjí | ano/série | 一至九年级 na obrigatória; 一至十二 na JY/T 0639 | [C26, C03] | |
| 义务教育 | | educação obrigatória | 9 anos | [C26] | |
| 国家课程 / 地方课程 / 校本课程 | | currículo nacional / local (provincial) / da escola | três categorias do plano de 2022 | [C26] | camadas de emissor, não disciplinas |
| 课程方案 / 课程标准 | | plano curricular / padrão curricular por disciplina | o plano fixa disciplinas, anos e carga; o padrão fixa 课程性质、理念、目标、内容、学业质量、实施 | [C26] | |
| 核心素养 | héxīn sùyǎng | competências nucleares | eixo dos padrões de 2022 ("凝练课程所要培养的核心素养") | [C26] | não é lista única nacional; cada disciplina define as suas [I, não verificado nos 16 padrões] |
| 学业质量 | | qualidade acadêmica (padrão de desempenho) | descrição do desempenho esperado em termos de núcleo de competências | [C26] | aproxima-se de descritor de nível |
| 跨学科主题学习 | | aprendizagem temática interdisciplinar | ≥ 10% da carga de cada disciplina | [C26] | |
| 综合实践活动 | | atividades práticas integradas | disciplina nacional, anos 1–9 | [C26] | |
| 智慧教育平台 | | plataforma de educação inteligente | "plataforma integrada de serviço público educacional" com 4 blocos (básica, profissional, superior, serviços) | [C04] | |
| 通行证 | tōngxíngzhèng | passe (conta unificada) | identidade após autenticação unificada | [C04] | |
| 实名认证 | | autenticação com nome real | registro com documento e celular | [C04, C15 art. 24] | |
| 教育移动应用 / 教育APP | | aplicativo móvel educacional | app com professores, alunos e pais como usuários principais e ensino/aprendizagem como cenário principal | [C21 art. 2] | define o escopo do 备案 |
| 备案 | bèi'àn | registro/notificação prévia | prestador (提供者备案) e usuário institucional (使用者备案) | [C21] | não é autorização, mas é condição de uso por escolas |
| 自研自用 | | desenvolvido e usado internamente | opção de registro do usuário | [C21] | |
| 敏感个人信息 | | informação pessoal sensível | inclui biometria, saúde, localização e **toda informação de menores de 14 anos** | [C13 art. 28] | menor de 14 é sensível por idade, não por conteúdo |
| 单独同意 | dāndú tóngyì | consentimento separado | exigido para sensível (art. 29) e para transferência internacional (art. 39) | [C13] | não basta aceite geral de termos |
| 监护人同意 | | consentimento do responsável | menores de 14 (PIPL art. 31) | [C13] | |
| 个人信息处理者 | | controlador (agente de tratamento) | quem decide finalidade e meio | [C13] | |
| 重要数据 / 核心数据 | | dado importante / dado central | categorias da Lei de Segurança de Dados; catálogos setoriais | [C14 art. 21] | na educação, ver JY/T 0661 |
| 数据出境 | shùjù chūjìng | saída de dados do território | transferência internacional | [C19] | inclui acesso remoto [I, não verificado] |
| 关键信息基础设施运营者 (CIIO) | | operador de infraestrutura crítica | obrigação de armazenar no território | [C15 art. 37] | designação feita pelas autoridades setoriais |
| 网络安全等级保护 | | proteção por níveis de segurança cibernética (MLPS) | sistema de classificação obrigatório | [C15 art. 21] | pré-requisito do 备案 de app |
| ICP备案 | | registro de serviço de informação na internet | pré-requisito do 备案 de app | [C21 art. 9] | |
| 未成年人模式 | | modo menor | exigido de plataformas com muitos usuários menores | [C17 art. 20, 43] | |
| 双减 | shuāng jiǎn | "dupla redução" | política de 2021 que restringe reforço escolar | [C24] | |

## 2. Vocabulários controlados com códigos

### 2.1 学习方式码 — regime de estudo (JY/T 0633, A.1) [C01]

| Código | Nome | Tradução |
|---|---|---|
| 1 | 全脱产（离岗） | tempo integral (afastado do trabalho) |
| 2 | 半脱产（半离岗） | meio período |
| 3 | 不脱产（不离岗） | sem afastamento |

### 2.2 用人形式码 — forma de contratação (A.2) [C01]

| Código | Nome | Código | Nome |
|---|---|---|---|
| 11 | 博士后 pós-doutorando | 31 | 双师型非在编教师 professor "duplo" não efetivo |
| 12 | 专职科研人员 pesquisador | 32 | 兼职、兼课 tempo parcial |
| 13 | 非在编合同制人员 contratado não efetivo | 41 | 返聘退休人员 aposentado recontratado |
| 21 | 人事代理 agência de pessoal | 99 | 其他 outros |
| 22 | 劳务派遣 terceirizado | | |

### 2.3 签订合同情况码 — contrato (A.3) [C01]

0 未签合同; 1 劳动合同（固定期限）; 2 劳动合同（无固定期限）; 3 劳动合同（以完成一定工作任务为期限）; 4 劳务合同（缴纳社保）; 5 劳务合同（不缴纳社保）; 9 其他合同.

### 2.4 免费(公费)师范生类型码 (A.4) [C01]

0 否; 1 2007–2018/07 免费师范生 de universidade normal do MOE; 2 idem, local; 3 desde 2018/08 公费师范生 do MOE; 4 desde 2018/08, local.

### 2.5 特岗教师类型码 (A.5) e 心理健康教师类型码 (A.6) [C01]

A.5: 0 否; 1 中央特岗教师; 2 地方特岗教师. A.6: 0 否; 1 专职 (exclusivo); 2 兼职 (acumulado).

### 2.6 教职工状态码 — situação funcional (A.7) [C01]

| Código | Nome | Código | Nome |
|---|---|---|---|
| 11 | 在职 em exercício | 44 | 长病假 licença médica longa |
| 21 | 借调机关 cedido a órgão | 51 | 退休 aposentado |
| 22 | 借调事业单位 cedido a entidade pública | 52 | 离休 aposentado (veterano) |
| 23 | 借调其他事业单位 | 53 | 延聘 prorrogado |
| 31 | 挂职锻炼 estágio em outro cargo | 61 | 合同终止 contrato encerrado |
| 32 | 交流轮岗 rodízio | 62 | 辞职 demissão voluntária |
| 33 | 进修 aperfeiçoamento | 63 | 开除 demitido |
| 34 | 因公出国 no exterior a serviço | 64 | 下落不明 paradeiro desconhecido |
| 41 | 停薪留职 licença sem vencimento | 65 | 死亡 falecido |
| 42 | 待岗 aguardando posto | 99 | 其他 |
| 43 | 待退休 pré-aposentadoria | | |

### 2.7 学段代码 — etapa de ensino (JY/T 0637, A.1) [C02]

| Código | Nome | Tradução |
|---|---|---|
| 1 | 高等教育 | educação superior |
| 11 / 111 / 112 / 113 | 普通高等教育 / 研究生 / 本科 / 专科 | superior regular / pós / graduação / tecnólogo |
| 12 / 121 / 122 / 123 | 高等职业教育 / 研究生 / 本科 / 专科 | superior profissional / … |
| 2 | 高中阶段教育 | etapa do ensino médio |
| 21 | 高中 | médio regular |
| 22 | 中等职业教育 | médio técnico |
| 3 | 初中阶段教育 | etapa ginasial (anos 7–9) |
| 31 | 初中 | ginásio |
| 32 | 成人初中 | ginásio de adultos |
| 4 | 小学阶段教育 | primário |
| 5 | 学前教育 | pré-escola |
| 6 | 工读学校 | escola de reeducação pelo trabalho |
| 7 | 特殊教育 | educação especial |
| 99 | 其他 | outros |

Observação [I]: "特殊教育" (7) é uma **etapa** paralela, não um atributo do aluno; ao mapear para C.PRG/C.SUP, não converter etapa em necessidade individual.

### 2.8 单位性质代码 — natureza da instituição (JY/T 0637, A.2; trecho educacional) [C02]

| Código | Nome | Código | Nome |
|---|---|---|---|
| 10 / 11 / 12 | 机关 / ≥ provincial / < provincial | 2331 | 初级中学 ginásio |
| 20 | 事业单位 entidade pública | 2332 | 九年一贯制学校 escola de 9 anos |
| 21 | 科研设计单位 | 2333 | 职业初中 |
| 22 | 高等学校 (221 本科, 222 本科职业, 223 高职专科, 224 成人高校, 229 outros) | 234 | 普通小学 (2341 小学, 2342 小学教学点 ponto de ensino) |
| 23 | 其他教育单位 | 235 | 幼儿园 |
| 231 | 普通高中 (2311 完全中学, 2312 高级中学, 2313 十二年一贯制学校) | 236 | 工读学校 |
| 232 | 中等职业教育 (2321 普通中专, 2322 成人中专, 2323 职业高中, 2324 技工学校, 2325 outros) | 237 | 特殊教育学校（专门学校） |
| 233 | 初中学校 | 238 | 成人中小学 |

Demais: 24 saúde, 25 esporte e cultura, 29 outras entidades públicas, 30–39 empresas (31 estatal, 32 joint venture, 33 privada, 34 estrangeira, 35 coletiva, 39 outra), 40 forças armadas, 50 organização social, 60 organização internacional, 70 defesa, 80 finanças, 99 outros.

### 2.9 Códigos citados por referência, não vistos

| Vocabulário | Norma | Situação |
|---|---|---|
| 学校标识码 (composição) | GB/T 33782—2017 §4.1 | `not_found` |
| 城乡类型码 (urbano/rural, a3) | GB/T 33782—2017 tabela 5 | `not_found` |
| 办学类型码 (tipo de escola, a3) | GB/T 33782—2017 tabela 4 | `not_found` (a JY/T 0637 A.2 dá uma lista paralela de natureza de instituição) |
| 举办者码, 主管部门码 | GB/T 33782—2017 §5.2.9 | `not_found` |
| 学生类别码 (5 níveis × 5 dígitos) | GB/T 33782—2017 tabela 24 | `not_found` |
| 教职工类别码, 来源码 | GB/T 33782—2017 tabelas 63, 64 | `not_found` |
| 身份证件类型码, 港澳台侨外码, 是否 | GB/T 29808—2013 §7.100, 7.26, 7.99 (7.99: 0 否 / 1 是, visto pelo uso) | parcial |
| 性别, estado civil, saúde | GB/T 2261.1/.2/.3 | `not_found` |
| 民族 (etnia) | GB/T 3304 | `not_found` |
| 学历 (escolaridade) | GB/T 4658 (vigente: GB/T 4658-2006 [C07]) | `not_found` |
| 行政区划 (divisão administrativa, 6 dígitos) | GB/T 2260 | `not_found` |
| 数字教育资源基础分类代码 | JY/T 0644—2022 | título e escopo apenas [C06] |

### 2.10 Disciplinas da educação obrigatória (课程方案 2022, tabela 1) [C26]

| Categoria | Disciplina | Anos |
|---|---|---|
| 国家课程 | 道德与法治 moral e Estado de direito | 1–9 |
| | 语文 língua chinesa | 1–9 |
| | 数学 matemática | 1–9 |
| | 外语 língua estrangeira (英语, 日语, 俄语…) | 3–9 |
| | 历史、地理 história, geografia | 7–9 |
| | 科学 ciências | 1–6 |
| | 物理、化学、生物学（或科学） | 7–9 |
| | 信息科技 tecnologia da informação | 3–8 |
| | 体育与健康 educação física e saúde | 1–9 |
| | 艺术 artes | 1–9 |
| | 劳动 trabalho | 1–9 |
| | 综合实践活动 atividades práticas integradas | 1–9 |
| 地方课程 | definido pela província | — |
| 校本课程 | definido pela escola | — |

Nota da tabela: arranjo "六三"; o "五四" pode ser derivado. Sem códigos de disciplina no documento.

### 2.11 Níveis de classificação de dados educacionais (JY/T 0661—2025) [C05]

| Nível | Nome | Exemplos de regra (basta uma) |
|---|---|---|
| L5 | 核心数据 dados centrais | ≥ 100 milhões de pessoas ou ≥ 10 milhões com dados sensíveis; dados básicos educacionais de abrangência nacional |
| L4 | 重要数据 dados importantes | 10–100 milhões, ou 1–10 milhões sensíveis; dados básicos e de gestão de abrangência provincial |
| L3 | 一般数据 geral | 1–10 milhões, ou 100 mil–1 milhão sensíveis; dados de aluno/servidor/ensino de uma universidade inteira |
| L2 | 一般数据 geral | 100 mil–1 milhão, ou 10 mil–100 mil sensíveis; dados de aluno/servidor/ensino de uma escola básica inteira |
| L1 | 一般数据 geral | < 100 mil, ou < 10 mil sensíveis; dados de gestão de uma escola básica |
