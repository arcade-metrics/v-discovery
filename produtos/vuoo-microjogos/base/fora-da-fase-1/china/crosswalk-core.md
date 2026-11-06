# Crosswalk: conceitos chineses → Core provisório

Alvos: entidades C.xxx de [_convencoes.md §4](../../_convencoes.md). Tipos: **exata**, **aproximada**, **parcial**, **mais ampla** (o conceito chinês é mais amplo que o alvo), **mais restrita**, **inexistente**. Todas as linhas são **mapeamento proposto por esta pesquisa [I]**, apoiado nas definições de [modelo-de-dados.md](modelo-de-dados.md) e nas fichas; nenhuma norma chinesa declara equivalência com o Core.

## 1. Organização (D1)

| Conceito | Fonte | Alvo | Tipo | Observação |
|---|---|---|---|---|
| 学校（机构） escola/instituição | JY/T 0633 tab. 2 | C.ORG | exata | `kind` por 办学类型码 (GB/T 33782 tab. 4) ou 单位性质代码 (JY/T 0637 A.2) |
| 教育行政部门 órgão educacional | JY/T 0633, 0661 | C.ORG (`kind` = órgão) | aproximada | hierarquia central–província–cidade–condado (5 níveis do 学籍) [C11] |
| 主管部门码 órgão supervisor | JY/T 0633 1.12 | relação pai de C.ORG | parcial | só código de categoria, não a instituição |
| 举办者 mantenedor | JY/T 0633 1.11 | C.ORG (`kind` = mantenedora) | parcial | código de categoria, não entidade |
| 校区 campus | JY/T 0633 1.19 | C.ORG filho ou C.LOC | aproximada | conjunto dentro da escola; sem identificador global |
| 房间用途统计 salas por uso | JY/T 0639 4.7 | C.LOC (agregado) | parcial | só contagem e área |
| 学年 / 学期 ano letivo / semestre | 课程方案 (39 semanas) | C.SES | aproximada | não modelado nas normas de dados |
| 学段 etapa (código) | JY/T 0637 A.1 | C.PRG | exata | hierarquia por prefixo |
| 学段 faixa de anos (currículo) | 课程标准 | C.PRG (segmento) | aproximada | depende de "六三"/"五四" |
| 年级 ano/série | 课程方案, JY/T 0639 | C.PRG (série) | exata | 1–9 obrigatória; 1–12 na 0639 |
| 学制 "六三"/"五四" | 课程方案 | C.PRG (variante de estrutura) | inexistente | ver QA-15 |
| 学制 duração em anos | JY/T 0633 3.6 | atributo de C.ENR/C.PRG | aproximada | |
| 专业 curso/área (técnico, superior) | JY/T 0633 3.4 | C.PRG | aproximada | fora do escopo EF+EM, exceto médio técnico |
| 课程 (disciplina) | 课程方案 tab. 1 | C.SUB | exata | |
| 国家/地方/校本课程 | 课程方案 | C.CFW (`issuer_level`) | parcial | camada de emissor do currículo |
| 班级 turma | — | C.GRP | inexistente nas normas lidas | `not_found` (QA-04) |
| 选课 / 排课 seleção / horário | JY/T 0661 anexo B (só categoria) | C.OFR / C.SCH | não verificada | sem modelo |
| 教学点 ponto de ensino | JY/T 0637 A.2 (2342) | C.ORG (`kind`) | aproximada | unidade vinculada a escola |

## 2. Pessoas e vínculos (D1/D3)

| Conceito | Fonte | Alvo | Tipo | Observação |
|---|---|---|---|---|
| 人员 pessoa | JY/T 0633 tab. 3 | C.PER | mais ampla | traz atributos que o Core não deve ter como fixos (政治面貌, 户口, 籍贯, 民族) |
| 学生 estudante | JY/T 0633 tab. 3 + 4 | C.LRN | exata | papel sobre pessoa |
| 教职工 servidor | JY/T 0633 tab. 3 + 5 | C.STF | exata | |
| 专任教师 professor regente | JY/T 0633 4.22 | C.STF (papel) | mais restrita | |
| 在编 / 用人形式 / 合同 vínculo funcional | JY/T 0633 4.8–4.10 | C.STF | parcial | contrato de trabalho sem alvo (QA-22) |
| 教职工状态 situação funcional | JY/T 0633 A.7 | C.STF (estado) via C.VOC | aproximada | |
| 家庭成员 membro da família | JY/T 0637 tab. 2 | C.GRD | mais ampla | familiar ≠ responsável legal; falta marca de guarda |
| 联系人 contato (aluno) | JY/T 0633 3.10–3.12 | C.GRD | aproximada | |
| 监护人 responsável legal (consente) | PIPL art. 31 | C.GRD + C.CNS | parcial | a norma de dados não identifica quem é o responsável legal |
| 学籍 registro escolar | 学籍管理办法 | C.ENR (pessoa × escola) | aproximada | vínculo nacional, um por pessoa, com estados e transferências |
| 现就读学校 / 所属学校 escola atual / de pertencimento | JY/T 0633 3.2/3.3 | C.ENR (dois tipos de vínculo) | parcial | Core precisa de `kind` de vínculo |
| 转学 transferência | 学籍 art. 15 | evento de C.ENR | aproximada | |
| 学习经历 trajetória escolar | JY/T 0637 tab. 4 | C.ENR histórico | aproximada | escola + etapa + datas |
| 工作经历 trajetória profissional | JY/T 0637 tab. 5 | — | inexistente | fora do Core educacional |
| 教师资格证 certificado docente | JY/T 0633 4.21 | C.CRD | aproximada | |
| 骨干/特岗/公费师范生/心理健康教师 | JY/T 0633 4.11–4.17 | atributos de C.STF via C.VOC | aproximada | |

## 3. Identificadores e vocabulários (D8)

| Conceito | Fonte | Alvo | Tipo | Observação |
|---|---|---|---|---|
| 学校（机构）标识码 a10 | JY/T 0633 1.1 | C.IDN `scheme=cn-moe-school` | exata | |
| 统一社会信用代码 | GB 32100 | C.IDN `scheme=cn-uscc` | exata | |
| 个人标识码 a19 | JY/T 0633 2.1 | C.IDN `scheme=cn-moe-person` | exata | |
| 学籍号 | 学籍 art. 8 | C.IDN `scheme=cn-xueji` | exata | entrada restrita (art. 24) |
| 身份证件类型 + 号 | JY/T 0633 2.11–2.12 | C.IDN (scheme pelo tipo) | exata | dado sensível; evitar armazenar fora do adaptador |
| 通行证 ID passe nacional | JY/T 0641 | C.IDN `scheme=smartedu-pass` | aproximada | protocolo unknown |
| 行政区划码, 民族码, 性别码, 学历码… | GB/T 2260, 3304, 2261, 4658 | C.VOC | exata | conjuntos externos versionados |
| 学段代码, 单位性质代码, anexo A da 0633 | JY/T 0633/0637 | C.VOC | exata | |
| 数字教育资源基础分类代码 | JY/T 0644 | C.VOC (para C.ACT) | não verificada | |
| norma de origem do elemento (编号, versão) | todas | C.PRV | aproximada | registrar `JY/T 0633—2022#2.1` como proveniência |

## 4. Currículo e avaliação (D2/D4/D5)

| Conceito | Fonte | Alvo | Tipo | Observação |
|---|---|---|---|---|
| 课程方案 plano curricular | 2022 | C.CFW | aproximada | define disciplinas e carga, não objetivos |
| 课程标准 padrão de disciplina | 2022 | C.CFW | exata | um por disciplina, versão 2022年版 |
| 核心素养 competências nucleares | 课程标准 | C.CMP (`kind`=competência) | aproximada | por disciplina (não verificado nos 16) |
| 课程内容 conteúdo | 课程标准 | C.CMP (`kind`=conteúdo) | aproximada | |
| 学业质量 padrão de qualidade acadêmica | 课程标准 | C.RES (nível de desempenho) / C.CMP | parcial | descritor de desempenho, sem escala numérica verificada |
| 跨学科主题学习 aprendizagem interdisciplinar (≥ 10%) | 课程方案 | C.ACT + C.CAS | parcial | regra de proporção sem alvo |
| 课时 / 教学时间 carga | 课程方案 | C.SCH / C.PRG | parcial | |
| 电子学档 e-portfólio | JY/T 0641; GB/T 36366 | C.EVD | não verificada | |
| 考试 avaliação na plataforma | JY/T 0641 | C.ASM / C.RES | aproximada | funcional, sem modelo |
| 教师数字素养 competência digital docente | JY/T 0646 | C.CFW (docente) | não verificada | |

## 5. Experiência, inclusão e governança (D6–D8)

| Conceito | Fonte | Alvo | Tipo | Observação |
|---|---|---|---|---|
| 数字教育资源 recurso digital | JY/T 0641, 0644, 0650 | C.ACT | aproximada | |
| 同步/异步在线教学 ensino síncrono/assíncrono | JY/T 0641 | C.SCH / C.ACT | aproximada | |
| 用户行为数据 / 用户建模 | JY/T 0641 §6.5 | C.EVT | aproximada | sujeita à PIPL art. 24 |
| 随班就读 inclusão em classe comum | JY/T 0639 2.10 | C.SUP | parcial | só contagem; nenhum dado individual |
| 特殊教育 (etapa/escola) | JY/T 0637 A.1, A.2 | C.PRG / C.ORG `kind` | aproximada | não converter em necessidade individual |
| 监护人同意 consentimento do responsável | PIPL 31 | C.CNS | exata | sujeito ≠ titular |
| 单独同意 consentimento separado | PIPL 29, 39 | C.CNS (por finalidade/destinatário) | aproximada | exige granularidade |
| 授权 autorização a plataforma conectada | JY/T 0641 | C.CNS (destinatário + atributos + estado) | aproximada | |
| 数据分类分级 classe/nível de dados | JY/T 0661, DSL 21 | — | inexistente | candidato a entidade/atributo do Core (QA-11) |
| 数据出境 transferência ao exterior | PIPL 38–40, CAC 2024 | — | inexistente | candidato: registro de transferência/residência (QA-16) |
| registro de acesso aprovado a dado de menor | 条例 art. 36 | C.PRV (parcial) | parcial | Core precisa de trilha de acesso com aprovação |
| auditoria anual | 条例 art. 37; PIPL 54 | — | inexistente | operação, não dado de domínio |
| indicadores agregados por escola | JY/T 0639 | — | inexistente | candidato (QA-10) |

## 6. Conceitos sem alvo no Core provisório

| Conceito | Proposta [I] |
|---|---|
| Classe e nível de dados por conjunto (L1–L5) | atributo/entidade `DataClassification` genérica (serve à LGPD e a outros regimes) |
| Residência e transferência de dados | `DataResidency` por instância/tenant + registro de transferência (base legal, receptor, volume) |
| Variante de estrutura de anos ("六三"/"五四") | `ProgramStructure` por implantação, ligando anos a segmentos |
| Camada do emissor curricular (nacional/provincial/escola) | atributo `issuer_level` em C.CFW e composição de frameworks |
| Indicador agregado (contagens por escola) | `AggregateIndicator` derivado, fora do núcleo transacional |
| Vínculo de trabalho (编制, contrato) | extensão de C.STF no adaptador; não precisa ir ao Core |
| Tipo de vínculo escolar (atual × pertencimento) | `kind` em C.ENR |
| Turma | existe no Core (C.GRP), mas não foi encontrada na norma chinesa: o adaptador precisa de fonte (sistema da escola) |
