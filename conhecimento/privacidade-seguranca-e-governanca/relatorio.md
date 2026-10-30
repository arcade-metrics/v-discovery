---
id: psg.relatorio
titulo: Relatório da primeira versão do domínio privacidade, segurança e governança
tipo: relatorio
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Relatório: primeira versão do domínio privacidade, segurança e governança

Data: 2026-10-30. Esta é a primeira versão funcional pedida por `_modelo/metodo-e-qualidade.md`: estrutura, documentos principais fundamentados em fontes verificadas, bibliografia, glossário, mapa e matriz. Todos os documentos estão em `status: rascunho`. A passagem para `revisado` exige o checklist de `_modelo/checklist-revisao.md` por leitor humano.

## Método aplicado

Sete frentes de pesquisa em paralelo, uma por pasta prevista no brief (`legal-framework`, `consent`, `access-control`, `de-identification`, `security`, `ai-governance`, `audit-risk`). Cada frente seguiu o plano de ids de `_plano-ids.md` e teve três regras: abrir a fonte antes de citá-la; registrar como lacuna o que não pôde abrir (texto pago, bloqueio de acesso automatizado, só metadados); e confirmar, no frontmatter real, todo id de outro domínio usado em relação. Seis frentes consultaram fontes em 2026-10-29; a de `ai-governance`, em 2026-10-30.

Cada frente produziu seus documentos e um fragmento de bibliografia e índice em `referencias/fragmentos/psg-<area>.bib` e `psg-<area>-indice.md`. Os fragmentos foram mesclados em `referencias/bibliografia.bib` e `referencias/indice-fontes.md` por `_modelo/mesclar_referencias.py`. Os arquivos de índice do domínio (README, glossário, mapa, matriz e este relatório) foram escritos depois, só a partir dos 26 documentos, sem pesquisa nova. O validador `_modelo/validar.py`, rodado sobre a base inteira, confirmou ids únicos com prefixo correto, alvos de relação existentes (inclusive em outros domínios), chaves de fonte presentes na bibliografia e nenhuma menção a produto consumidor: 0 avisos, 0 erros.

## Cobertura

| Área | Documentos | Conteúdo |
|---|---|---|
| legal-framework | 4 | LGPD e menores (art. 14, Enunciado 1/2023, guia de legítimo interesse); ECA e Estatuto Digital (Lei 15.211/2025, Decretos 12.622/2025 e 12.880/2026); GDPR, AADC e COPPA 2025; comparação por critério |
| consent | 3 | consentimento parental (forma, verificação, prova); assentimento (CNS 466/2012 e 510/2016, Convenção, UNICEF, deficiência intelectual e de comunicação); ciclo de vida das permissões (revogação, mudança de finalidade, maioridade) |
| access-control | 3 | RBAC, ABAC e ReBAC (Ferraiolo e Kuhn, Sandhu, SP 800-162, Zanzibar, SP 800-53); papéis escolares e matriz de visões (OneRoster, CEDS); minimização e privacy by design (Cavoukian, LGPD, GDPR art. 25) |
| de-identification | 4 | anonimização e pseudonimização (LGPD arts. 12 e 13, estudos técnicos da ANPD, SP 800-188); k-anonimato, l-diversidade e t-closeness; privacidade diferencial (Dwork, Dwork e Roth, SP 800-226); risco de reidentificação (Sweeney, Narayanan e Shmatikov, Rocher et al.) |
| security | 4 | modelo de ameaças (STRIDE, LINDDUN, K12 SIX, DBIR 2025); criptografia e gestão de chaves (SP 800-57, OWASP, FIPS 140-3); incidentes (Res. CD/ANPD 15/2024, SP 800-61r3); ISO/IEC 27001 e 27701 e SP 800-53 |
| ai-governance | 4 | NIST AI RMF, ISO/IEC 42001, UNICEF e UNESCO; AI Act (com o Regulamento 2026/1744) e PL 2338/2023; transparência e supervisão humana (LGPD art. 20, XAI em educação); model cards e datasheets |
| audit-risk | 4 | trilhas de auditoria (família AU, SP 800-92, RFC 5424 e 3161, PROV-O); registro das operações (art. 37, Res. 2/2022, Res. 18/2024); RIPD/DPIA (ANPD, WP29, CNIL, guia federal); gestão de riscos de privacidade (NIST Privacy Framework, IR 8062) |
| raiz | 7 | brief, plano de ids, README, glossário, mapa, matriz comparativa, este relatório |

Totais: 26 documentos conceituais (28 contando brief e plano de ids). 203 relações tipadas no mapa de conceitos: 93 `complementa`, 69 `relacionado-a`, 19 `depende-de`, 10 `parte-de`, 5 `especificado-por`, 4 `avaliado-por`, 3 `alternativa-a`. 116 chaves de fonte distintas no frontmatter dos documentos. Os sete fragmentos têm 117 entradas e 111 chaves distintas (`eu2016gdpr` está em quatro fragmentos; `nist2020sp80053r5`, `iso270012022` e `ftc2025coppafinalrule`, em dois); as outras cinco chaves citadas (`brasil2018lgpd`, `imsglobal2022oneroster`, `nces2026ceds`, `rfc8446`, `w3c2013provo`) já estavam na bibliografia por outros domínios. 325 termos declarados nos campos `termos:`.

Marcas de afirmação no corpo dos 26 documentos, contadas por script (ocorrências de colchete aberto com a marca, fora do frontmatter; um colchete com duas citações conta uma vez):

| Área | `[F]` | `[I]` | `[H]` |
|---|---|---|---|
| legal-framework | 159 | 23 | 0 |
| consent | 155 | 18 | 0 |
| access-control | 101 | 30 | 1 |
| de-identification | 149 | 6 | 3 |
| security | 112 | 36 | 3 |
| ai-governance | 88 | 30 | 0 |
| audit-risk | 134 | 48 | 0 |
| **Total** | **898** | **191** | **7** |

## O que o brief pediu e onde está

| Entregável | Local |
|---|---|
| Estrutura de diretórios | `privacidade-seguranca-e-governanca/` (7 pastas temáticas, mais `_plano-ids.md`) |
| README com escopo, navegação e convenções | `README.md` deste domínio |
| Glossário | `glossario.md` |
| Mapa conceitual | `mapa-conceitos.md` |
| Documentos fundamentados em fontes primárias | as 7 pastas temáticas |
| Bibliografia BibTeX | fragmentos `psg-*.bib` mesclados em `conhecimento/referencias/bibliografia.bib` |
| Matriz comparativa | `matriz-comparativa.md` (nove comparações) |
| Relatório de cobertura e lacunas | este arquivo |

## Fontes que não puderam ser verificadas

Padrão recorrente: o EUR-Lex não carregou conteúdo para acesso automatizado; as normas ISO e ABNT são pagas e o site da ISO respondeu 403; editoras acadêmicas (ACM, Wiley, Taylor & Francis) bloquearam texto integral em parte das tentativas. Cada caso está na seção "Lacunas" do documento e na nota da entrada BibTeX do fragmento. Por área:

- **legal-framework**: GDPR lido em espelho não oficial (gdpr-info.eu); art. 20 e art. 52, II da LGPD reconferidos no Planalto em 30/10/2026; sanções do GDPR (art. 83) e da COPPA não verificadas; COPPA lida na edição do CFR de 1/1/2025, anterior à revisão, com os dispositivos novos lidos no Federal Register; o guia da FTC sobre COPPA não tem data de atualização; AADC lido só nos padrões 1 e 3, anexo B e arranjos transitórios. Lei 15.211/2025 lida na página do Planalto, com codificação corrompida; vetos, MPs 1.317/2025 e 1.319/2025 e Lei 15.352/2026 vistos só pelas notas de redação. Decreto 12.880/2026 lido em parte. Resolução CD/ANPD 2/2022 não aberta nesta área.
- **consent**: versão publicada no DOU do Enunciado CD/ANPD 1/2023 aberta só em 30/10/2026, na harmonização; Ward et al. 2025 só por metadados; Coker 2025 só por resumo; ISO/IEC 29184 só por sumário e amostra; Kantara Consent Receipt v1.1 não abriu e não é citada; regulamento da ANPD sobre prazos de atendimento ao titular não consultado. Resoluções CNS lidas em cópia da BVS, que não substitui o DOU.
- **access-control**: INCITS 359-2012 só por metadados; Sandhu et al. 1996 lido na pré-publicação do NIST, sem conferir a paginação da IEEE; GDPR art. 25 em espelho; ISO 31700-1:2023 não acessada e não citada; vocabulário de papéis do CEDS não localizado além de três entidades.
- **de-identification**: ISO/IEC 20889 e 27559 só por metadados; minuta do guia de anonimização da ANPD não lida (só a nota técnica de abertura e os dois estudos técnicos); Daries et al. 2014 inacessível (ACM 403, DSpace 429), com o efeito no caso edX vindo do NIST SP 800-188 e do post do coautor; SP 800-226 lido só nas seções 1, 2.1, 2.2, 2.4 e 4.2.
- **security**: textos da ISO/IEC 27001:2022, ABNT NBR 27001 e ISO/IEC 27701:2019 não lidos; contagem de 93 controles vem de fonte secundária (DQS); ISO/IEC 27701:2025 não verificada; PDF do SP 800-53 não aberto; crosswalk OLIR não renderizou; Shostack 2014 só por metadados; relatório CIS 2026 só pela página de resumo; formulário de comunicação de incidentes da ANPD não aberto; tabela 1 do SP 800-57 lida com alinhamento imperfeito.
- **ai-governance**: AI Act e Regulamento 2026/1744 lidos no espelho AI Act Explorer; ISO/IEC 42001 e 23894 só por metadados e sumário; textos integrais das duas publicações da UNESCO não carregaram, e o limite de 13 anos vem de notícia da ONU; diretrizes da Comissão sobre o art. 6 e Anexo IV do AI Act não lidos; Mitchell et al. e Conati et al. lidos em versão arXiv.
- **audit-risk**: ISO/IEC 27002:2022 (controles 8.15 a 8.17), ISO/IEC 29134:2023, ISO 31000:2018 e ISO/IEC 27005:2022 só por metadados e amostra; SP 800-92 rev. 1 é rascunho sem versão final; Privacy Framework 1.1 só pela página do rascunho; NIST PRAM não aberta; modelo de registro simplificado da ANPD não localizado; Regulamento de Dosimetria (Res. CD/ANPD 4/2023) não aberto e não citado.

## Inconsistências entre documentos, para revisão

Encontradas na leitura dos 26 documentos para este índice e harmonizadas em 30/10/2026, com conferência na fonte primária.

1. **Histórico do art. 20 da LGPD. Resolvido.** Conferido no Planalto (texto original e compilado da Lei 13.709/2018, MP 869/2018 e Lei 13.853/2019): a redação original de 2018 previa revisão "por pessoa natural"; a MP 869/2018 deu ao caput a redação sem a expressão; a Lei 13.853/2019, de conversão, fixou esse texto, e o §3 que ela incluiu foi vetado. psg.legal.lgpd-children (que estava errado) e psg.ai.transparency-and-human-oversight passaram a ter a mesma redação, citando também as novas chaves `mpv8692018` e `lei138532019`.
2. **Texto do Enunciado CD/ANPD 1/2023. Resolvido.** Aberto o PDF da publicação no DOU (24/05/2023, edição 98, seção 1, p. 129). psg.consent.parental-consent passou a citar o texto publicado (`anpd2023enunciado1`), com a data correta; a minuta do voto (`anpd2023voto12`) fica só para o histórico de aprovação e para a diferença de redação (a minuta remetia ao "caput do art. 14" e explicitava os dados sensíveis). A lacuna sobre a versão publicada foi retirada.
3. **DBIR 2025, envio ao destinatário errado. Resolvido.** Os dois números estão no relatório, com bases diferentes, ambos na seção Educational Services: Misdelivery é 17% de todas as violações do setor (p. 73) e 60% das violações por erro do setor (p. 74). psg.sec.incident-management e psg.sec.threat-model-education trazem agora a mesma frase, com as duas bases e as páginas.
4. **Chaves duplicadas. Resolvido.** ECA: ficou `lei8069eca`; `lei80691990` foi substituída em psg.consent.parental-consent e psg.consent.permission-lifecycle e removida do fragmento e do índice de consent. SP 800-53 rev. 5: ficou `nist2020sp80053r5`; `nist2020sp80053` foi substituída em psg.sec.iso-27001-and-27701 e na matriz comparativa e removida do fragmento e do índice de security; a nota da entrada única registra as três leituras (famílias AC e AU no PDF, página do CSRC). COPPA: são documentos diferentes e as duas chaves ficam: `ftc2025coppa` é a Part 312 na edição anual do CFR de 1/1/2025, anterior à emenda; `cfr16312coppa` é o §312.5 no eCFR via LII, já com a emenda de 2025. psg.consent.parental-consent e psg.legal.comparison dizem agora qual edição leram.
5. **Lacunas que outra frente fechou. Resolvido.** psg.consent.parental-consent remete o ECA Digital a psg.legal.eca-and-digital-eca e o §312.2 da COPPA a psg.legal.gdpr-k-and-coppa; psg.audit.ripd-dpia remete o texto do ECA Digital a psg.legal.eca-and-digital-eca; psg.legal.lgpd-children remete o texto da Res. CD/ANPD 2/2022 a psg.audit.ripd-dpia; psg.legal.comparison remete o art. 35 do GDPR a psg.audit.ripd-dpia (tabela e lacuna). Nenhuma afirmação nova foi acrescentada com base nessas remissões.
6. **Sanção da LGPD. Resolvido.** O art. 52, II foi conferido no texto compilado do Planalto: multa simples de até 2% do faturamento no Brasil, limitada a R$ 50 milhões por infração, sem nota de alteração; a Lei 13.853/2019 não alterou o inciso II. psg.legal.comparison indica a data da conferência, e a lacuna de psg.legal.lgpd-children registra a verificação, restando só os demais dispositivos do art. 52.
7. **Dono do termo "pseudonimização". Resolvido.** O dono é psg.deid.anonymization-and-pseudonymization. A linha do glossário de `interoperabilidade` aponta agora para esse id e mantém só a frase sobre o uso na troca entre sistemas.

## Lacunas de conhecimento consolidadas

1. **Regulação brasileira ainda por vir.** Não há guia abrangente da ANPD sobre dados de crianças (psg.legal.lgpd-children), regulamento de RIPD previsto no art. 55-J, XIII (psg.audit.ripd-dpia), regulamentação do art. 20 (psg.ai.transparency-and-human-oversight), versão final do guia de anonimização (psg.deid.anonymization-and-pseudonymization), critério objetivo de "larga escala" (psg.sec.incident-management) nem regulamentação de age assurance prevista no Decreto 12.880/2026 (psg.legal.comparison).
2. **Quem consente pelo adolescente e quem é controlador.** A LGPD não diz quem consente entre 12 e 18 anos (psg.consent.parental-consent). Escola, rede e fornecedor como controlador, operador ou controladores conjuntos ficam em aberto em psg.legal.lgpd-children, psg.legal.eca-and-digital-eca, psg.sec.incident-management e psg.audit.processing-records.
3. **Transição à maioridade.** Sem norma brasileira; a regra de psg.consent.permission-lifecycle é construção do documento.
4. **Assentimento em serviço.** Não há revisão aberta sobre assentimento de crianças com deficiência de comunicação fora da pesquisa, nem instrumento validado de qualidade do assentimento (psg.consent.child-assent).
5. **Valores de referência.** Nenhuma fonte dá k, l, t ou epsilon para dados educacionais ou de menores (psg.deid.k-anonymity-and-extensions, psg.deid.differential-privacy).
6. **Avaliação desagregada por deficiência.** Como medir desempenho por grupo de deficiência sem ampliar o tratamento de dado sensível (psg.ai.model-documentation).
7. **Explicação a responsáveis e crianças.** Não há estudos de explicação de decisões adaptativas para esses públicos, nem para crianças com deficiência intelectual (psg.ai.transparency-and-human-oversight).
8. **Retenção da trilha de auditoria.** Sem orientação da ANPD para trilhas com dados de menores; o prazo fica na ponderação entre os arts. 16 e 20 (psg.audit.audit-trails).
9. **Dados brasileiros de incidentes em escolas.** Os números são dos EUA (psg.sec.threat-model-education).
10. **Calibração do "indivíduo típico".** Nenhuma fonte de risco de privacidade calibra verossimilhança e impacto para crianças (psg.audit.privacy-risk-management).
11. **Propostas não validadas.** Matriz de visões por papel (psg.access.school-roles, `[H]`), indicadores de minimização (psg.access.minimization-and-privacy-by-design), taxa de aceite como sinal de viés de automação (psg.ai.transparency-and-human-oversight), inferência de deficiência ou estado emocional por telemetria fina (psg.sec.threat-model-education, `[H]`).

## Respostas às perguntas abertas do brief

| Pergunta do brief | Resposta desta versão | Id |
|---|---|---|
| Qual a base legal adequada para cada tratamento de uma plataforma usada pela escola, e quando o consentimento parental do art. 14 é de fato exigido? | Pelo Enunciado CD/ANPD 1/2023, qualquer base dos arts. 7 ou 11 serve, desde que o melhor interesse prevaleça no caso concreto. O consentimento parental é exigido quando o controlador escolhe o consentimento como base para dado de criança. O documento traz um mapa de bases candidatas por operação (cadastro, interações, laudo, publicidade, pesquisa, contato único). Ficam em aberto adolescentes e o papel da escola como controladora. | psg.legal.lgpd-children, psg.consent.parental-consent |
| Como desenhar assentimento significativo para crianças com deficiência intelectual ou de comunicação? | Como processo contínuo, não formulário: avaliação prévia do modo de comunicação, material adaptado (figuras, símbolos, Talking Mats, sinais, dispositivos de fala), concordância afirmativa explícita, leitura de sinais não verbais de dissentimento, registro em qualquer mídia e reavaliação periódica. Em serviço, é boa prática, não exigência legal. A evidência sobre materiais acessíveis é fraca. | psg.consent.child-assent |
| Que controles adicionais o dado de laudo e deficiência impõe a modelos de aluno que o usam como atributo? | É dado sensível de saúde: só bases do art. 11, sem legítimo interesse; o art. 11, §1 alcança inferências de deficiência feitas pelo modelo. O regente vê só a adaptação derivada, não o diagnóstico. Dado de menores ou sensível é critério específico de alto risco, o que leva ao RIPD. A avaliação desagregada por deficiência exige base legal própria e segue em aberto. | psg.legal.lgpd-children, psg.access.school-roles, psg.audit.ripd-dpia, psg.ai.model-documentation |
| Que nível de anonimização torna um dataset de interação de menores compartilhável para pesquisa sem risco relevante de reidentificação? | Hipótese fundamentada `[H]`: nenhum nível de anonimização de microdados torna seguro o modelo release-and-forget, porque a série temporal é quase-identificador de alta dimensionalidade e turmas pequenas geram classes unitárias. O compartilhamento defensável combina acordo de uso ou enclave, pseudonimização com chave separada, k-anonimato com l-diversidade nos atributos demográficos e sensíveis e publicação só de estatísticas com privacidade diferencial em nível de usuário. Faltam valores validados de k e epsilon. | psg.deid.reidentification-risk, psg.deid.k-anonymity-and-extensions, psg.deid.differential-privacy |
| Como explicar uma decisão de adaptação do modelo para professor e responsável sem expor o modelo inteiro? | Por explicação local e contrafactual, em camadas ("por quê" e "como"), com versão própria para cada público: o professor recebe fatores principais, confiança, limites e botão de rejeitar; o responsável, o que mudou, por quê, quem revisou e como pedir revisão. A documentação global fica no model card. Alertas ficam em fila para decisão humana; adaptações automáticas são expostas e reversíveis. | psg.ai.transparency-and-human-oversight, psg.ai.model-documentation |
| Que trilha de auditoria mínima permite reconstruir por que o sistema recomendou algo a um aluno numa data passada? | Registro de decisão em cinco camadas: referências ou hashes das entradas com instante de leitura, id e versão do modelo, versão de regras e configuração, saída e ações humanas posteriores; carimbo em UTC, pseudônimo do aluno, hash encadeado e carimbo de TSA por lote. No AI Act, o deployer guarda logs por ao menos seis meses. A retenção para menores segue sem orientação da ANPD. | psg.audit.audit-trails, psg.ai.eu-ai-act-and-brazil |

## Próximos passos sugeridos

1. **Revisão humana** dos 26 documentos com o checklist, começando pelos que dependem de espelho ou só de metadados: psg.legal.gdpr-k-and-coppa, psg.ai.eu-ai-act-and-brazil, psg.sec.iso-27001-and-27701 e psg.ai.ai-governance-frameworks.
2. **Inconsistências entre documentos**: harmonizadas em 30/10/2026 (ver seção acima); repetir a checagem a cada nova frente.
3. **Segunda rodada de fontes** com acesso institucional ou oficial: EUR-Lex (GDPR, AI Act, Regulamento 2026/1744), normas ISO e ABNT, Daries et al. 2014, formulário de incidentes da ANPD.
4. **Acompanhar mudanças com data**: tramitação do PL 2338/2023 na Câmara, regulamentação de age assurance pela ANPD, revisão do AI RMF 1.0, versão final do Privacy Framework 1.1, ISO/IEC 27701:2025 e versão final do guia de anonimização da ANPD.
5. **Fechar a fronteira com `dados-pesquisa-e-eventos`**: alinhar psg.consent.child-assent com dat.ethics.consent-and-assent-in-research e psg.access.minimization-and-privacy-by-design com dat.ethics.research-vs-operation, para que cada fato tenha um dono.
6. **Conversão para grafo.** Com ids, relações tipadas e termos no frontmatter, um script pode gerar SKOS a partir dos arquivos, junto com `grafo-conhecimento-educacional`, como já recomendado nos relatórios dos domínios em primeira versão.
