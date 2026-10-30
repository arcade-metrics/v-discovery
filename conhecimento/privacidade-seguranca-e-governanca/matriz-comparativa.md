---
id: psg.matriz
titulo: Matriz comparativa de regimes, modelos e técnicas do domínio
tipo: comparacao
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Matriz comparativa de regimes, modelos e técnicas do domínio

Nove comparações centrais do domínio. Cada célula traz, entre parênteses, o id do documento que a sustenta e, quando o documento cita, a chave da fonte e o dispositivo. As citações completas e as ressalvas de leitura (espelho, metadados) estão nos documentos de origem. Células marcadas `[I]` são interpretação do documento de origem, não fato da fonte.

## 1. Regimes legais para dados de menores: LGPD, Estatuto Digital, GDPR, AADC e COPPA

Fonte única das células: psg.legal.comparison, que remete a psg.legal.lgpd-children, psg.legal.eca-and-digital-eca e psg.legal.gdpr-k-and-coppa.

| Critério | LGPD + ECA | Estatuto Digital (Lei 15.211/2025) | GDPR | AADC (Reino Unido) | COPPA (revisão 2025) |
|---|---|---|---|---|---|
| Quem é "criança" | até 12 incompletos; adolescente de 12 a 18 (`lei8069eca`, art. 2) | adota o ECA (`lei15211ecadigital`, art. 2, §1) | menor de 16; Estados podem baixar até 13 (`eu2016gdpr`, art. 8(1)) | menor de 18, em cinco faixas de 0-5 a 16-17 (`ico2020aadc`, anexo B) | menor de 13 (`ftc2025coppa`, §312.2) |
| Regime reforçado alcança | crianças (§1) e adolescentes (caput) (`brasil2018lgpd`, art. 14) | serviços direcionados a menores ou de acesso provável (`lei15211ecadigital`, art. 1) | crianças, só com base em consentimento e serviço oferecido diretamente a elas (`eu2016gdpr`, art. 8) | serviço "likely to be accessed by children" (`ico2020aadc`) | serviço dirigido a menores de 13 ou com conhecimento efetivo (`ftc2025coppa`) |
| Base legal | qualquer do art. 7 ou 11 com melhor interesse prevalecente (`anpd2023enunciado1`); legítimo interesse só com balanceamento documentado (`anpd2024legitimointeresse`) | não altera bases; veda perfilamento publicitário (`lei15211ecadigital`, arts. 22 e 26) | qualquer do art. 6; legítimo interesse pesa contra o controlador se o titular é criança e não vale para autoridade pública (`eu2016gdpr`, art. 6(1)) | não altera bases; condiciona o desenho | consentimento parental verificável como regra, com exceções do §312.5(c) (`ftc2025coppa`) |
| Verificação parental | "esforços razoáveis [...] tecnologias disponíveis" (`brasil2018lgpd`, art. 14, §5) | consentimento para download, "vedada a presunção de autorização" (`lei15211ecadigital`, art. 12, §2) | "reasonable efforts [...] available technology" (`eu2016gdpr`, art. 8(2)) | não trata consentimento; age assurance proporcional ao risco (`ico2020aadc`, §3) | métodos enumerados, inclusive "text plus" desde 2025 (`ftc2025coppa`, §312.5(b)(2); `ftc2025coppafinalrule`) |
| Consentimento pela escola | sem regra; ANPD aceita legítimo interesse da escola em relação direta (exemplo do wi-fi) (`anpd2024legitimointeresse`, ex. 2) | sem regra | sem regra específica | sem regra | escola como "parent's agent", só para fim educacional (`ftc2025coppafaq`, §N); exceção formal não adotada em 2025 (`ftc2025coppafinalrule`) |
| Desenho | informação acessível à criança; não condicionar participação a dados excessivos (`brasil2018lgpd`, art. 14, §§4 e 6) | privacidade por padrão no nível mais alto; gestão de riscos; sem uso compulsivo (`lei15211ecadigital`, arts. 7 e 8) | linguagem clara para crianças (`eu2016gdpr`, art. 12(1)) | 15 padrões (defaults, minimização, geolocalização, nudges, perfilamento) (`ico2020aadc`) | programa de segurança escrito; política de retenção escrita; retenção indefinida proibida (`ftc2025coppafinalrule`) |
| Dado de saúde e deficiência | sensível, só art. 11; legítimo interesse excluído (`brasil2018lgpd`, arts. 5, II e 11; `anpd2024legitimointeresse`) | não trata | categoria especial; consentimento explícito ou lei (`eu2016gdpr`, art. 9) | sem regra própria [I] | entra como personal information quando identificável [I] |
| Decisão automatizada | revisão e informação sobre critérios (`brasil2018lgpd`, art. 20) | não trata | direito de não ser submetido; "should not concern a child" (`eu2016gdpr`, art. 22; cons. 71) | padrão de "profiling" (só o título foi lido) (`ico2020aadc`) | não trata |
| Avaliação de impacto | ANPD "poderá determinar"; orienta fazer em alto risco (`brasil2018lgpd`, art. 38; `anpd2024legitimointeresse`) | relatório se o tratamento exceder o estritamente necessário (`lei15211ecadigital`, art. 16) | DPIA, art. 35 (ver seção 9) | DPIA obrigatória, padrão 2 (`ico2020aadc`) | não exige |
| Autoridade | ANPD | ANPD (`lei15211ecadigital`, art. 34; `decreto126222025`) | autoridades nacionais | ICO | FTC |
| Sanção máxima | multa até 2% do faturamento, limitada a R$ 50 milhões por infração (`brasil2018lgpd`, art. 52, II) | multa até 10% do faturamento do grupo no Brasil; suspensão e proibição pelo Judiciário (`lei15211ecadigital`, art. 35) | não verificado | sem multa própria; aplicado via UK GDPR (`ico2020aadc`) | não verificado |

Leitura [I], de psg.legal.comparison: o Brasil é mais exigente no alcance do melhor interesse (até 18 anos e qualquer base legal) e na multa do Estatuto Digital; é silencioso em consentimento pela escola, métodos de verificação parental e padrões de desenho por faixa etária, onde COPPA e AADC servem de referência de prática.

## 2. Modelos de controle de acesso: RBAC, ABAC e ReBAC

Fonte: psg.access.rbac-and-abac; aplicação a papéis escolares em psg.access.school-roles.

| Critério | RBAC | ABAC | ReBAC |
|---|---|---|---|
| Decide por | papel ativo na sessão; papel como conjunto de transações (`ferraiolokuhn1992rbac`, §2; `sandhu1996rbacmodels`, §4) | atributos de sujeito e objeto, condições de ambiente e política (`nist2014sp800162`, §2.2) | relações armazenadas entre usuários e objetos, tuplas `object#relation@user` (`pang2019zanzibar`, §2.1) |
| Referência | INCITS 359-2012 (só metadados) (`nist2026rbacproject`; `incits2012rbac`); SP 800-53 AC-3(7) (`nist2020sp80053r5`) | NIST SP 800-162; SP 800-53 AC-3(13) (`nist2014sp800162`; `nist2020sp80053r5`) | Zanzibar, Google; o termo ReBAC não aparece no artigo [I] (`pang2019zanzibar`) |
| Vantagem documentada | administração centralizada; suporta menor privilégio e separação de deveres (`ferraiolokuhn1992rbac`, §4; `sandhu1996rbacmodels`, §2) | aceita sujeito externo inesperado sem pré-provisionar; granularidade fina (`nist2014sp800162`, §2.3) | compartilhamento por relação e herança via hierarquia de objetos num só modelo (`pang2019zanzibar`, §2.3) |
| Limitação documentada | decisões multifatoriais geram explosão de papéis (`nist2014sp800162`, §2.1); não garante por si os princípios que suporta (`sandhu1996rbacmodels`, §2) | custo de manutenção; auditoria "antes do fato" exige simular a decisão (`nist2014sp800162`, §3.1.2.1 e §3.1.2.3) | consistência das relações é problema distribuído ("new enemy"); enumerar quem tem acesso exige seguir referências (`pang2019zanzibar`, §2.2 e §2.4.5) |
| Saber quem tem acesso a quê | direto (`nist2014sp800162`, §3.1.2.3) | custoso (`nist2014sp800162`, §3.1.2.3) | via Expand, seguindo referências indiretas (`pang2019zanzibar`, §2.4.5) |
| Pressuposto | funções estáveis e enumeráveis (`sandhu1996rbacmodels`, §2) | atributos definidos e mantidos por autoridades (`nist2014sp800162`, §2.4.2) | ordem causal entre mudança de ACL e de conteúdo (`pang2019zanzibar`, §2.2) |
| Uso na escola [I] | nomear a função (professor, responsável) (psg.access.school-roles) | contexto: turma, ano letivo, vínculo ativo; agregados sem identidade (AC-24(2)) (psg.access.school-roles) | escopo: responsável-de, regente-de, atende (psg.access.school-roles) |

Os três não são excludentes; a combinação típica numa plataforma escolar é híbrida [I] (psg.access.rbac-and-abac).

## 3. Saídas de desidentificação: pseudonimização, anonimização de microdados, privacidade diferencial e enclave

Fonte: psg.deid.anonymization-and-pseudonymization (tabela "Alternativas"), com psg.deid.reidentification-risk e psg.deid.differential-privacy.

| Critério | Pseudonimização | Microdados anonimizados (k-anonimato e extensões) | Privacidade diferencial (agregados ou sintéticos) | Enclave ou interface de consulta |
|---|---|---|---|---|
| Base | LGPD art. 13, §4 (`brasil2018lgpd`) | LGPD art. 12; supressão e generalização (`brasil2018lgpd`; `anpd2023anonimizacaoprocesso`, §2.4) | Dwork 2006; Dwork e Roth 2014 (`dwork2006differential`; `dworkroth2014algorithmic`) | NIST SP 800-188, §3.4 e §4.5 (`nist2023sp800188`) |
| Reversível pelo controlador | sim, pela chave separada (psg.deid.anonymization-and-pseudonymization) | não, se bem feito | não | o dado original fica no enclave |
| Sai do regime da LGPD [I] | não; continua pessoal para quem tem a chave | sim, sob o teste do art. 12 | sim, sob o mesmo teste | não para o dado interno; sim para saídas aprovadas |
| Preserva ligação longitudinal | sim, e por isso aumenta o risco de reidentificação por outros meios (`nist2023sp800188`, §2.2) | parcial | não (não há microdado) | sim, internamente |
| Garantia formal | não | não; risco medido empiricamente (`anpd2023anonimizacaoprocesso`, §2.3) | sim, limite matemático epsilon; perdas se somam entre releases (`dworkroth2014algorithmic`, Teorema 3.16) | depende do mecanismo de resposta |
| Risco típico de reidentificação | ligação por pseudônimo e séries (`nist2023sp800188`, §4.3.10) | ligação, homogeneidade, releases múltiplas (psg.deid.k-anonymity-and-extensions) | outliers vulneráveis com epsilon alto, a partir de 10 (`nist2025sp800226`, §2.2) | risco concentrado nas saídas (psg.deid.reidentification-risk) |
| Custo em utilidade | baixo | supressão e generalização; no caso edX, distorção de resultados (`nist2023sp800188`, §5.4; `waldo2014anonymity`) | ruído proporcional a sensibilidade/epsilon; subgrupos pequenos mais afetados [I] | baixo em utilidade, alto custo operacional (psg.deid.reidentification-risk) |

## 4. Modelos sintáticos de anonimização: k-anonimato, l-diversidade e t-closeness

Fonte: psg.deid.k-anonymity-and-extensions.

| Critério | k-anonimato | l-diversidade | t-closeness |
|---|---|---|---|
| Proposto por | Sweeney (`sweeney2002kanonymity`) | Machanavajjhala, Kifer, Gehrke e Venkitasubramaniam (`machanavajjhala2007ldiversity`) | Li, Li e Venkatasubramanian (`li2007tcloseness`) |
| Exigência | cada combinação de quase-identificador aparece ao menos k vezes (`sweeney2002kanonymity`, §3.1) | cada classe tem ao menos l valores "bem representados" do atributo sensível; variantes distinta, entropia e (c,l) recursiva (`machanavajjhala2007ldiversity`, §4) | distância EMD entre a distribuição sensível da classe e a da tabela não passa de t (`li2007tcloseness`, §4 e §5) |
| Protege contra | divulgação de identidade por ligação | divulgação de atributo por homogeneidade e conhecimento de fundo | ganho de informação sobre a distribuição do atributo sensível |
| Ataque que o motivou | ligação com lista de eleitores (caso Weld) (`sweeney2002kanonymity`, §1) | homogeneidade e conhecimento de fundo (`machanavajjhala2007ldiversity`, §1.1) | assimetria e similaridade (`li2007tcloseness`, §3) |
| Ataques que permanecem | homogeneidade, conhecimento de fundo, releases complementares e temporais (`sweeney2002kanonymity`, §4) | assimetria e similaridade; inviável quando um valor sensível domina (`li2007tcloseness`; `machanavajjhala2007ldiversity`, §4.2) | perda acumulada entre releases não calculável; sem garantia probabilística formal (psg.deid.k-anonymity-and-extensions) |
| Parâmetro | k | l, c | t |
| Métrica de risco associada | risco por classe 1/k; média ponderada no cenário do jornalista (`anpd2023anonimizacaoprocesso`, §2.3) | entropia por classe | EMD por classe |

Nenhum dos três tem valor de referência da ANPD (psg.deid.k-anonymity-and-extensions, Lacunas).

## 5. Taxonomias de ameaça: STRIDE e LINDDUN

Fonte: psg.sec.threat-model-education.

| Critério | STRIDE | LINDDUN |
|---|---|---|
| Origem | Microsoft (`microsoft2017stride`) | grupo DistriNet, KU Leuven (`kuleuven2026linddun`) |
| Foco | segurança | privacidade |
| Categorias | Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege (`microsoft2017stride`) | Linking, Identifying, Non-repudiation, Detecting, Data disclosure, Unawareness and unintervenability, Non-compliance (`kuleuven2026linddunthreats`) |
| Unidade de análise | elemento do DFD | fluxo de dado pessoal; GO usa baralho, PRO usa interações do DFD (`kuleuven2026linddun`) |
| Variantes de método | não descritas na fonte | GO (leve), PRO (sistemático), MAESTRO (dirigido por modelo) (`kuleuven2026linddun`) |
| Não-repúdio | propriedade desejável (negar uma ação é ameaça) [I] | ameaça (atribuir uma ação a alguém pode expô-lo) [I] |
| O que não captura | coleta excessiva num sistema perfeitamente seguro [I] | exige mapear fluxos de dado pessoal em detalhe [I] |
| Quando usar | todo sistema | início com equipe mista (GO); sistemas com muitos fluxos de dado pessoal (PRO) |

O modelo de ameaças é insumo técnico do RIPD, não o substitui [I] (psg.sec.threat-model-education).

## 6. Referências de segurança e privacidade: ISO/IEC 27001, ISO/IEC 27701, NIST SP 800-53 e guia da ANPD

Fonte: psg.sec.iso-27001-and-27701.

| Critério | ISO/IEC 27001:2022 (ABNT NBR) | ISO/IEC 27701:2019 | NIST SP 800-53 rev. 5 | Guia ANPD para pequeno porte |
|---|---|---|---|---|
| Natureza | requisitos de SGSI + Anexo A (`iso270012022`; `abnt2022nbr27001`) | extensão PIMS da 27001 e 27002 (`iso277012019`) | catálogo de controles em 20 famílias (`nist2020sp80053r5`) | boas práticas sem efeito vinculante (`anpd2021pequenoporte`) |
| Certificável | sim | sim, junto com a 27001 | não | não |
| Cobre privacidade | indiretamente, via controles de PII do Anexo A | sim | sim, família PII Processing and Transparency (`nist2020sp80053r5`) | sim |
| Estrutura | seções 4 a 10 obrigatórias, sem exclusão (`abnt2022nbr27001`); 93 controles em 4 temas, segundo fonte secundária (`dqs2023iso27001`) | requisitos e orientações para controladores e operadores (`iso277012019`) | famílias como AC, AU, IR, PT, RA, SC (`nist2020sp80053r5`) | política simplificada, treinamento, acesso com MFA, backups, cláusulas com fornecedores (`anpd2021pequenoporte`) |
| Relação com a LGPD [I] | demonstra arts. 46, 49 e 50 | controladores e operadores | sem relação formal; crosswalk com a 27001, não 1:1 (`nist2020sp80053r5`) | orientação da própria autoridade |
| Acesso ao texto | pago; só metadados lidos | pago; só metadados lidos | aberto; só a página oficial lida | aberto; lido |
| Situação na consulta | vigente, com emenda de 2024 (`iso270012022`) | retirada em 14/10/2025, substituída pela 27701:2025, não avaliada (`iso277012019`) | release 5.2.0 em ago. 2025 (`nist2020sp80053r5`) | versão 1.0, out. 2021 (`anpd2021pequenoporte`) |

## 7. Frameworks de governança de IA: NIST AI RMF, ISO/IEC 42001, UNICEF e UNESCO

Fonte: psg.ai.ai-governance-frameworks.

| Critério | NIST AI RMF 1.0 | ISO/IEC 42001:2023 | UNICEF, Policy Guidance 2.0 | UNESCO (2021 e 2023) |
|---|---|---|---|---|
| Natureza | framework voluntário (`nist2023airmf`) | norma certificável de sistema de gestão (`iso420012023`) | orientação de política (`unicef2021aichildren`) | recomendação adotada por 193 Estados e guia de IA generativa (`unesco2021ethicsai`; `unesco2023genaiguidance`) |
| Unidade de análise | sistema e ciclo de vida | organização (AIMS) | política pública e sistema | Estado e instituição de ensino |
| Estrutura | GOVERN, MAP, MEASURE, MANAGE; sete características de IA confiável (`nist2023airmf`, §3 e §5) | avaliação de impacto de sistema de IA (6.1.4 e 8.4); Anexos A e B (`iso420012023`, sumário) | nove requisitos sobre a fundação dos direitos da criança (`unicef2021aichildren`) | dez princípios; abordagem "human-agent and age-appropriate" (`unesco2021ethicsai`; `unesco2023genaiguidance`) |
| Foco em crianças | não específico | não verificado | central | presente: idade mínima de 13 sugerida para uso em sala, só por notícia da ONU (`unnews2023genaischools`) |
| Supervisão humana | GOVERN 3.2, MAP 3.5, MANAGE 2.4 (`nist2023airmf`, Tabelas 1, 2 e 4) | não verificado | human-in-the-loop em decisões-chave (`unicef2021aichildren`, req. 6) | "human oversight and determination" (`unesco2021ethicsai`) |
| Acesso | aberto | pago; só metadados | aberto | aberto; textos integrais não carregaram |
| Papel no uso combinado [I] | como mapear e medir | como manter isso como processo auditável | o que proteger | o que proteger, em sala de aula |

## 8. Regimes legais para decisão automatizada sobre aprendizes: AI Act, PL 2338/2023 e LGPD art. 20

Fontes: psg.ai.eu-ai-act-and-brazil e psg.ai.transparency-and-human-oversight.

| Critério | AI Act (UE 2024/1689) | PL 2338/2023 (texto do Senado) | LGPD art. 20 |
|---|---|---|---|
| Status em 30/10/2026 | em vigor; alto risco do Anexo III aplicável a partir de 2/12/2027, pela redação do Regulamento 2026/1744 (`eu2024aiact`, art. 113; `eu2026omnibusai`) | na Câmara, "Aguardando Parecer" (`camara2026pl2338tramitacao`) | em vigor (`brasil2018lgpd`) |
| Gatilho educacional | sistema que avalia resultados de aprendizagem e dirige o processo (Anexo III, 3(b)); perfilamento é sempre alto risco (`eu2024aiact`, art. 6(3)) | avaliação "determinante" no progresso acadêmico ou monitoramento de estudantes (`pl23382023`, art. 14, II) | decisão unicamente automatizada que afete interesses (`brasil2018lgpd`, art. 20) |
| Supervisão humana | desenhada pelo provider, atribuída pelo deployer a pessoas com competência e autoridade (`eu2024aiact`, arts. 14 e 26) | direito e dever: "compreender, interpretar, decidir e intervir" (`pl23382023`, arts. 6 e 8) | revisão a pedido, sem exigir pessoa natural (`brasil2018lgpd`, art. 20, notas de redação) |
| Explicação | instruções ao deployer (art. 13); explicação ao afetado (art. 86) (`eu2024aiact`) | explicação gratuita em linguagem simples (`pl23382023`, arts. 6 e 7) | critérios e procedimentos, ressalvado segredo comercial (`brasil2018lgpd`, art. 20, §1) |
| Avaliação de impacto | gestão de riscos com atenção a menores de 18 (art. 9(9)); FRIA para entes públicos (art. 27) (`eu2024aiact`) | avaliação de impacto algorítmico obrigatória para alto risco (`pl23382023`, art. 25) | RIPD quando exigido (psg.audit.ripd-dpia) |
| Logs | deployer guarda logs por ao menos seis meses (`eu2024aiact`, art. 26(6)) | Administração registra quem usou, para quê (`pl23382023`, art. 23, I) | não exige; ANPD pode auditar aspectos discriminatórios se houver recusa por segredo (`brasil2018lgpd`, art. 20, §2) |

Leitura [I], de psg.ai.eu-ai-act-and-brazil: o PL é mais estreito no gatilho e mais largo nos direitos individuais; o AI Act é mais detalhado nas obrigações técnicas do fornecedor.

## 9. Quando o relatório de impacto é exigido: ANPD, GDPR com WP29 e CNIL

Fonte: psg.audit.ripd-dpia.

| Critério | LGPD + ANPD | GDPR + WP29 | CNIL (método PIA) |
|---|---|---|---|
| Natureza da obrigação | a ANPD "poderá determinar" (art. 38) ou "poderá solicitar" no legítimo interesse (art. 10, §3); recomendação geral de elaborar em alto risco (`brasil2018lgpd`; `anpd2023ripdfaq`) | obrigação direta antes do tratamento provável de alto risco (`eu2016gdpr`, art. 35(1)) | método, não obrigação (`cnil2018piamethodology`) |
| Gatilho | alto risco = ao menos um critério geral + um específico, do art. 4 da Res. CD/ANPD 2/2022; lista não exaustiva (`anpd22022`, art. 4; `anpd2023ripdfaq`) | nove critérios do WP29; em regra, dois bastam (`wp292017wp248`, §III.B.a) | não define gatilho; remete ao art. 35(1) do GDPR |
| Menores como critério | critério específico "dados pessoais de crianças, de adolescentes e de idosos" (`anpd22022`, art. 4) | "vulnerable data subjects", que "may include children" (`wp292017wp248`, §III.B.a); recital 75 (`eu2016gdpr`) | não tratado na fonte |
| Decisão automatizada como critério | sim, inclusive para definir perfil de saúde ou personalidade (`anpd22022`, art. 4) | sim, avaliação ou pontuação e decisão com efeito significativo (`wp292017wp248`) | não tratado na fonte |
| Conteúdo mínimo | art. 38, parágrafo único, + 12 blocos recomendados (`brasil2018lgpd`; `anpd2023ripdfaq`) | art. 35(7), alíneas a a d; Anexo 2 do WP29 (`eu2016gdpr`; `wp292017wp248`) | contexto, princípios, riscos por evento temido, validação (`cnil2018piamethodology`, §1 a §4) |
| Envio à autoridade | só quando requisitado (`anpd2023ripdfaq`) | consulta prévia se o risco residual for alto (art. 36) | idem GDPR |
| Revisão | revisão contínua; guia federal sugere gatilhos e revisão anual (`anpd2023ripdfaq`; `sgd2026guiaripd`, §4.5) | ao menos quando o risco muda (`eu2016gdpr`, art. 35(11)); "continual process" (`wp292017wp248`) | desde a concepção do tratamento (`cnil2018piamethodology`) |

Aplicação [I], de psg.audit.ripd-dpia: numa plataforma educacional com dados de menores, o critério específico está satisfeito por definição; basta um critério geral (larga escala ou afetar significativamente direitos). O guia federal acrescenta a regra de dois fatores do WP29 (`sgd2026guiaripd`, §3.1).

Ressalva: psg.legal.comparison registra o art. 35 do GDPR como "não lido nesta sessão", enquanto psg.audit.ripd-dpia o leu em espelho. As células do GDPR nesta seção seguem psg.audit.ripd-dpia.
