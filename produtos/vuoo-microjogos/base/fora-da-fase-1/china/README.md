# China — adaptador de referência

**Estado: standby (referência).** Documentado o suficiente para mostrar que um adaptador China cabe sem mudar o Core e para registrar as restrições legais fortes (localização de dados, menores), sem detalhar campo a campo além do que foi lido ([_convencoes.md §1](../../_convencoes.md)). Pesquisa de 2026-11-05; fontes em [evidencias.md](evidencias.md). Parte §3.3 do [briefing](../../padroes-README.md). Nenhum documento sobre a China existia em `conhecimento/` (a comparação `conhecimento/privacidade-seguranca-e-governanca/legal-framework/comparison.md` não cita a China).

## Escopo

Normas de dados educacionais do MOE (JY/T 0633/0637/0639-2022 e séries relacionadas), normas nacionais GB/T de gestão educacional e de campus inteligente, identificadores (escola, pessoa, 学籍号), a Plataforma Nacional de Educação Inteligente (smartedu.cn) e suas normas, o currículo da educação obrigatória de 2022, e o quadro legal (PIPL, DSL, CSL, proteção on-line de menores, transferência internacional, registro de apps educacionais, acesso ao mercado).

**Correção do briefing:** JY/T 0634-2022 e JY/T 0635-2022 **não existem** no cadastro oficial; os temas pedidos estão em **JY/T 0637—2022** (pessoal) e **JY/T 0639—2022** (escolas de educação básica). Ver [QA-01](questoes-abertas.md).

## Índice

| Arquivo | Conteúdo |
|---|---|
| [modelo-de-dados.md](modelo-de-dados.md) | metaestrutura JY/T, escola, pessoa, estudante, servidor, família, trajetórias, agregados de escola, conta da plataforma, identificadores, classificação de dados |
| [terminologia.md](terminologia.md) | conceitos com pinyin e falsos amigos; tabelas de códigos (anexos A da 0633 e 0637, disciplinas, níveis L1–L5) |
| [cobertura.md](cobertura.md) | matriz referência × D1–D8 |
| [crosswalk-core.md](crosswalk-core.md) | conceito chinês → C.xxx com tipo de equivalência; conceitos sem alvo |
| [questoes-abertas.md](questoes-abertas.md) | textos não lidos, verificações pendentes, candidatos a entidade do Core |
| [evidencias.md](evidencias.md) | fontes (C01–C30), tipo de fonte, afirmações → fonte |

**Fichas** (`fichas/`):

| Ficha | Tipo | Situação |
|---|---|---|
| [jyt-0633-2022](fichas/jyt-0633-2022.md) 教育基础数据 | norma setorial (dados) | texto integral lido |
| [jyt-0637-2022](fichas/jyt-0637-2022.md) 教育系统人员基础数据 | norma setorial (dados) | texto oficial integral lido |
| [jyt-0639-2022](fichas/jyt-0639-2022.md) 中小学校基础数据 | norma setorial (dados agregados) | texto integral lido |
| [jyt-0634-0635-2022](fichas/jyt-0634-0635-2022.md) | referências do briefing | não existem |
| [jyt-1001-1007-2012](fichas/jyt-1001-1007-2012.md) 教育管理信息 | normas setoriais | só título e datas; continuam vigentes |
| [gbt-gestao-educacional](fichas/gbt-gestao-educacional.md) GB/T 33782, 35298, 29808, 36351, 4658, 21365 | normas nacionais | só metadados |
| [gbt-36342-2018](fichas/gbt-36342-2018.md) 智慧校园总体框架 | norma nacional | só metadados |
| [smartedu-plataforma](fichas/smartedu-plataforma.md) + JY/T 0641, 0650, 0643 | plataforma + normas setoriais | 0641 lida; 0650 e 0643 só escopo; sem API pública |
| [recursos-digitais](fichas/recursos-digitais.md) JY/T 0644, 0607–0609, 0646 | normas setoriais | só metadados |
| [jyt-0661-2025](fichas/jyt-0661-2025.md) 教育数据分类分级指南 | norma setorial (governança) | texto oficial integral lido |
| [xueji-2025](fichas/xueji-2025.md) 中小学生学籍管理办法 | regulamento ministerial | artigos verificados |
| [curriculo-obrigatorio-2022](fichas/curriculo-obrigatorio-2022.md) 义务教育课程方案和课程标准 | documento curricular | plano lido (imagem); padrões não lidos |
| [pipl](fichas/pipl.md) 个人信息保护法 | lei | artigos verificados |
| [dsl](fichas/dsl.md) 数据安全法 | lei | artigos verificados |
| [csl](fichas/csl.md) 网络安全法 (2016, alt. 2025) | lei | artigos de 2016 + decisão de 2025 |
| [protecao-menores](fichas/protecao-menores.md) 未成年人网络保护条例 + 未成年人保护法 | regulamento + lei | regulamento verificado; lei por trecho |
| [transferencia-2024](fichas/transferencia-2024.md) 促进和规范数据跨境流动规定 | regulamento (CAC) | verificado |
| [ndsr-2024](fichas/ndsr-2024.md) 网络数据安全管理条例 | regulamento | artigos verificados |
| [apps-educacionais-2019](fichas/apps-educacionais-2019.md) 备案 de apps educacionais | regulamento ministerial + parecer | verificado |
| [acesso-ao-mercado](fichas/acesso-ao-mercado.md) lista negativa 2024 + 双减 | regulamento + política | itens verificados |

## Resumo em 10 linhas

1. O núcleo de dados educacionais é a JY/T 0633—2022 (recomendada, vigente desde 2022-11-30): escola, pessoa única e extensões de estudante e servidor, como dicionário de dados em PDF, sem esquema nem API.
2. JY/T 0637 (família, contato, trajetórias) e JY/T 0639 (contagens por escola básica) completam o conjunto; não substituem a série JY/T 1001–1007-2012, que segue vigente.
3. Identificadores nacionais "únicos e vitalícios": escola a10 e pessoa a19, atribuídos pela administração educacional; o 学籍号 é gerado pelo sistema nacional e seu formato não é publicado oficialmente.
4. Turma, oferta, horário e sala não aparecem em nenhuma norma de dados lida; avaliação (D5) e apoio individual (D7) também não.
5. O currículo obrigatório de 2022 tem 3 camadas (nacional, provincial, escola), 9 anos em "六三" ou "五四", 12 linhas de disciplinas e 核心素养 por disciplina, só em PDF.
6. A smartedu.cn é portal nacional com conta de nome real e autorização a plataformas conectadas; não há API pública localizada.
7. PIPL: todo dado de menor de 14 anos é sensível e exige consentimento separado dos pais e regras próprias; vale também para quem opera de fora da China.
8. Enviar ao exterior dado sensível de qualquer número de pessoas exige contrato-padrão ou certificação; a partir de 10 mil pessoas, avaliação de segurança da CAC; o 学籍 não pode ser passado a terceiros sem lei ou aprovação de governo.
9. JY/T 0661—2025 classifica dados educacionais em L1–L5; dados de uma província inteira são "importantes" (L4) e ficam, na prática, presos ao território.
10. Conclusão provisória: o Core cabe sem regra chinesa, mas só como **implantação separada no território**, operada por entidade local, com classificação de dados, consentimento granular e trilha de acesso como recursos genéricos do Core.

## O que um adaptador China exigiria

**Implantação (o que torna inviável o modelo de instância única) [I]:**
- **Instância separada na China continental**, com armazenamento, processamento, backups, logs, telemetria e treinamento de modelos no território. Fundamentos: dado de aluno < 14 é sensível (PIPL 28) e sua saída exige contrato-padrão, certificação ou avaliação da CAC mais consentimento separado (PIPL 38–39; CAC 2024 arts. 7–8); 学籍 só sai com lei ou aprovação (学籍 art. 24); dados de escala provincial são L4/importantes (JY/T 0661; DSL 21, 31); pedidos de autoridades estrangeiras exigem aprovação chinesa (PIPL 41; DSL 36).
- **Entidade local** e licença/registro de internet: ICP备案 (e licença de valor agregado se houver receita, capital estrangeiro ≤ 50%), 等级保护定级备案, registro de prestador de app educacional na província e registro de uso pelas escolas (C21, C23). Modelo comercial só via escolas/órgãos; oferta direta a famílias de conteúdo de disciplinas da educação obrigatória cai no 双减 (aprovação, proibição de capital estrangeiro e de cursos estrangeiros).
- Sem federação de dados pessoais entre instâncias; só conteúdo não pessoal (currículo, itens, recursos) e agregados não classificados como importantes podem circular, e mesmo esses passam por revisão de conteúdo local.

**Do adaptador (local, sem tocar no Core) [I]:**
- Importação/exportação nos formatos da JY/T 0633/0637/0639 (inclusive os microformatos `{chave:número}` da 0639) e geração de indicadores por escola.
- Tabelas C.VOC: anexos A da 0633 e 0637, GB/T 2260, 3304, 2261, 4658, 33782 (após leitura), disciplinas e anos do currículo 2022.
- C.IDN com esquemas `cn-moe-school`, `cn-moe-person`, `cn-xueji`, `cn-uscc`, `smartedu-pass`; documento de identidade só se exigido e com classificação sensível.
- Atributos chineses sensíveis (政治面貌, 民族, 户口, 籍贯, saúde) como extensões classificadas, nunca no núcleo.
- Fluxos de consentimento: responsável para < 14; consentimento separado por finalidade sensível; autorização por plataforma conectada; política de privacidade específica para menores.
- Operação: auditoria anual de dados de menores reportada à CAC, aprovação e registro de cada acesso de funcionário a dado de menor, notificação de incidente à CAC e às famílias, painel do responsável (consulta, cópia, correção, exclusão, portabilidade), identidade real para chat/mural, modo menor se a escala exigir.
- Estrutura de anos por implantação ("六三"/"五四") e currículo em três camadas.

**O que o Core precisa ter, de forma genérica, para o adaptador caber [I]:** rótulo de classificação de dados por conjunto com herança do máximo (QA-11); residência de dados por instância e registro de transferência (QA-16b); C.CNS com sujeito ≠ titular, finalidade, destinatário e revogação; trilha de acesso com aprovação (C.PRV); `kind` de vínculo em C.ENR; variante de estrutura de programa (QA-15); `issuer_level` em C.CFW. Nada disso é exclusivo da China: LGPD e GDPR pedem versões das mesmas capacidades.

**O que tornaria o Core inviável na China [I]:** depender de identificador nacional obrigatório; centralizar dados pessoais ou telemetria numa região fora da China; treinar modelos globais com dados de alunos chineses; exigir integração com serviços de identidade, analytics ou IA hospedados no exterior.

## Não verificado

Textos de GB/T 33782 e 35298 (códigos e regra do 学校标识码), JY/T 1001–1007-2012, JY/T 0643—2025 (proteção de dados de plataformas educacionais), JY/T 0650, 0644, 0607–0609, 0646, GB/T 36342, os 16 padrões curriculares, o currículo do ensino médio, regras de ICP/telecom, regras de algoritmos e de IA generativa, e o texto consolidado da CSL de 2026. Detalhes em [questoes-abertas.md](questoes-abertas.md).
