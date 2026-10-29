---
id: psg.audit.privacy-risk-management
titulo: Gestão de riscos de privacidade como processo contínuo
tipo: framework
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nist2020privacyframework, nist2025privacyframework11, nist2017ir8062, iso310002018, iso270052022, cnil2018piamethodology, brasil2018lgpd, anpd2023ripdfaq]
relacoes:
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: complementa, alvo: psg.audit.processing-records }
  - { tipo: complementa, alvo: psg.audit.audit-trails }
  - { tipo: complementa, alvo: psg.sec.iso-27001-and-27701 }
  - { tipo: complementa, alvo: psg.ai.ai-governance-frameworks }
  - { tipo: complementa, alvo: psg.sec.incident-management }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
termos: [risco de privacidade, ação de dados problemática, previsibilidade, gerenciabilidade, desassociabilidade, Core, Profile, Implementation Tier, Identify-P, Govern-P, Control-P, Communicate-P, Protect-P, apetite a risco, risco residual, cenário de risco, evento temido]
---

# Gestão de riscos de privacidade como processo contínuo

## Definição e terminologia

O NIST Privacy Framework define **privacy risk** como "The likelihood that individuals will experience problems resulting from data processing, and the impact should they occur", e **problematic data action** como "A data action that could cause an adverse effect for individuals" [F: nist2020privacyframework, Appendix B]. **Gestão de riscos de privacidade** é "A cross-organizational set of processes for identifying, assessing, and responding to privacy risks", e **avaliação de risco de privacidade** é o subprocesso de identificar e avaliar riscos específicos [F: nist2020privacyframework, Appendix B]. O NIST IR 8062 introduz o modelo de risco e os três **objetivos de engenharia de privacidade**: **predictability**, "Enabling of reliable assumptions by individuals, owners, and operators about PII and its processing by a system"; **manageability**, "Providing the capability for granular administration of PII including alteration, deletion, and selective disclosure"; e **disassociability**, "Enabling the processing of PII or events without association to individuals or devices beyond the operational requirements of the system" [F: nist2017ir8062, Appendix B].

A CNIL define risco como "a hypothetical scenario that describes a feared event and all the threats that would allow this to occur", estimado em severidade e verossimilhança [F: cnil2018piamethodology, §3]. A ISO 31000:2018 é a norma genérica de gestão de riscos, organizada em princípios, estrutura e processo, com avaliação de riscos dividida em identificação, análise e avaliação (cláusula 6.4) [F: iso310002018, metadados e sumário]. A ISO/IEC 27005:2022, quarta edição, orienta a gestão de riscos de segurança da informação alinhada à ISO/IEC 27001:2022 e à ISO 31000:2018, introduz "risk scenario concepts" e contrasta a identificação de riscos baseada em eventos com a baseada em ativos [F: iso270052022, Foreword].

O que não é: não é o RIPD, que é um produto pontual do processo (`psg.audit.ripd-dpia`); não é gestão de riscos de segurança, que é um subconjunto; e não é medição estatística de viés de modelos, que fica em outros domínios e aqui aparece apenas como subcategoria a acompanhar [I].

## Problema que resolve

O NIST sustenta que gerir risco de cibersegurança "is not sufficient, as privacy risks can also arise by means unrelated to cybersecurity incidents": um sistema pode funcionar exatamente como projetado e ainda criar problemas para as pessoas, de "dignity-type effects such as embarrassment or stigmas" a "discrimination, economic loss, or physical harm" [F: nist2020privacyframework, §1.2.1]. O IR 8062 acrescenta que "only individuals—not agencies—can directly experience a privacy problem", o que torna a estimativa de impacto "especially challenging" [F: nist2017ir8062, §3.2.1]. Numa plataforma educacional, uma recomendação pedagógica correta do ponto de vista técnico pode estigmatizar um aluno perante a turma; esse é um risco de privacidade sem incidente de segurança [I]. A LGPD faculta aos controladores um programa de governança em privacidade que estabeleça "políticas e salvaguardas adequadas com base em processo de avaliação sistemática de impactos e riscos à privacidade" (art. 50, §2, I, d) e exige demonstrar sua efetividade quando apropriado (art. 50, §2, II) [F: brasil2018lgpd]. A ANPD descreve a gestão de riscos como "processo sistemático da gestão organizacional que determina a aplicação equilibrada de controles diante do perfil de riscos" [F: anpd2023ripdfaq].

## Fundamentos e funcionamento

### O modelo de risco

No modelo de segurança, os fatores são a probabilidade de uma ameaça explorar uma vulnerabilidade e o impacto; no modelo de privacidade, "the problematic data action plays the same functional role in framing the adverse event as do threats" [F: nist2017ir8062, §3.2.1]. Verossimilhança é "the probability that a data action will become problematic for a representative or typical individual whose PII is processed by the system", e depende da percepção dos usuários e do contexto; impacto é "the magnitude of cost or harm from the problematic data action", para o qual o IR 8062 sugere proxies como custos de conformidade, falha de missão, reputação e cultura interna [F: nist2017ir8062, §3.2.1]. A avaliação orienta-se pela identificação das "discrete data actions" do sistema e pela determinação de quais podem ser problemáticas, considerando o contexto [F: nist2017ir8062, §3.2.2]. O Privacy Framework liga o problema do indivíduo ao impacto organizacional (abandono do serviço, custos de não conformidade, dano reputacional) para trazer o risco de privacidade "into parity with other risks" [F: nist2020privacyframework, §1.2.1, Figure 3].

As respostas possíveis são mitigar, transferir ou compartilhar (contratos; avisos e consentimento como compartilhamento com o indivíduo), evitar (renunciar ao tratamento) e aceitar [F: nist2020privacyframework, §1.2.2]. O IR 8062 ressalta que "Risk can be managed, but it cannot be eliminated" e que o objetivo é um grau aceitável de risco residual [F: nist2017ir8062, §3.2.1].

### A estrutura do Privacy Framework 1.0

Publicado em 16 de janeiro de 2020, o framework é voluntário e composto de **Core**, **Profiles** e **Implementation Tiers** [F: nist2020privacyframework, cover; Figure 1]. O Core organiza resultados em Funções, Categorias e Subcategorias; as cinco Funções são: **Identify-P**, "Develop the organizational understanding to manage privacy risk for individuals arising from data processing"; **Govern-P**, "Develop and implement the organizational governance structure to enable an ongoing understanding of the organization's risk management priorities that are informed by privacy risk"; **Control-P**, "Develop and implement appropriate activities to enable organizations or individuals to manage data with sufficient granularity to manage privacy risks"; **Communicate-P**, "Develop and implement appropriate activities to enable organizations and individuals to have a reliable understanding and engage in a dialogue about how data are processed and associated privacy risks"; e **Protect-P**, "Develop and implement appropriate data processing safeguards", que cobre a sobreposição com cibersegurança [F: nist2020privacyframework, §2.1]. Profiles são seleções priorizadas do Core; um Current Profile e um Target Profile expõem lacunas e recursos necessários [F: nist2020privacyframework, §2.2]. Os Tiers são Partial, Risk Informed, Repeatable e Adaptive, representam progressão não compulsória, e "successful implementation ... is based upon achieving the outcomes described in an organization's Target Profile(s) and not upon Tier determination" [F: nist2020privacyframework, §2.3].

A categoria Risk Assessment (ID.RA-P) traz as subcategorias centrais do processo: fatores contextuais identificados, incluindo demografia e sensibilidade dos dados (ID.RA-P1); "Data analytic inputs and outputs are identified and evaluated for bias" (ID.RA-P2); ações problemáticas e problemas identificados (ID.RA-P3); verossimilhança e impacto usados para priorizar (ID.RA-P4); respostas priorizadas e implementadas (ID.RA-P5) [F: nist2020privacyframework, Table 2]. A categoria Monitoring and Review (GV.MT-P) fecha o ciclo: "Privacy risk is re-evaluated on an ongoing basis and as key factors ... change" (GV.MT-P1), com procedimentos para receber e responder a ações problemáticas relatadas por fontes internas e externas (GV.MT-P5) e incorporar lições aprendidas (GV.MT-P6) [F: nist2020privacyframework, Table 2]. O rascunho da versão 1.1 foi publicado em 14 de abril de 2025 como Initial Public Draft, com comentários até 13 de junho de 2025, realinhando o framework ao Cybersecurity Framework 2.0 e melhorando a usabilidade; versão final não localizada [F: nist2025privacyframework11].

### Processo contínuo

A síntese das fontes dá um ciclo em cinco passos [I]: (1) inventariar ações de dados e contexto (ID.IM-P, registro do art. 37); (2) para cada ação, perguntar se pode tornar-se problemática para um aluno, responsável ou professor típico, usando os três eventos temidos da CNIL como mínimo e os problemas do NIST como catálogo; (3) estimar verossimilhança e impacto e priorizar; (4) responder e registrar risco residual aceito, com responsável; (5) monitorar gatilhos (mudança de modelo, nova finalidade, incidente, nova regulação) e reavaliar. A ANPD exige que a identificação e análise dos fatores sejam "documentadas e justificadas" e alerta que "múltiplos fatores de risco pode[m] aumentar o nível de risco", devendo-se analisar "dependências e efeitos combinados" [F: anpd2023ripdfaq].

## Requisitos e pressupostos

- Declaração de apetite a risco e critérios de impacto, probabilidade e aceitação definidos antes da avaliação, para que o RIPD não vire matriz paralela (ver `psg.audit.ripd-dpia`) [I].
- Capacidade de ouvir os indivíduos: o IR 8062 sugere dados demográficos, extrapolação de cenários similares e grupos focais ou pesquisas para estimar se usuários considerariam uma ação problemática [F: nist2017ir8062, §3.2.1]; com crianças, isso exige assentimento e mediação adequados [I].
- Registro de decisões de resposta vinculado a controles concretos, muitos dos quais são os de `psg.sec.iso-27001-and-27701` [I].

## Vantagens e limitações

O modelo separa risco de privacidade de risco de segurança e dá vocabulário para problemas sem incidente; o Privacy Framework é agnóstico de jurisdição e mapeável a referências informativas [F: nist2020privacyframework, §3.1]. Limitações reconhecidas pelas próprias fontes: "Assessing the impact on individuals is an area that needs further research" [F: nist2017ir8062, §3.2.1]; o framework "do[es] not have the force and effect of law" [F: nist2020privacyframework, cover]; e nenhuma das fontes trata especificamente de crianças como população de referência para a verossimilhança, o que obriga a adaptar o "indivíduo típico" [I].

## Alternativas e comparações

| Critério | NIST PF 1.0 + IR 8062 | ISO 31000:2018 / ISO/IEC 27005:2022 | CNIL PIA | LGPD art. 50 |
|---|---|---|---|---|
| Unidade de risco | Ação de dados problemática | Evento ou ativo; cenário de risco (27005) | Evento temido + ameaças | Não define |
| Impacto medido em | Problemas para o indivíduo, com proxies organizacionais | Objetivos da organização | Prejuízo ao titular | Liberdades e direitos |
| Estrutura | Core, Profiles, Tiers | Princípios, estrutura, processo | 4 passos | Programa de governança |
| Status | Voluntário, EUA | Norma internacional, paga | Método público, França | Lei, facultativo |
| Fonte | [F: nist2020privacyframework; nist2017ir8062] | [F: iso310002018; iso270052022] | [F: cnil2018piamethodology] | [F: brasil2018lgpd] |

## Métricas e métodos de avaliação

Maturidade: Tier atual versus Tier alvo, usado como comunicação de recursos e não como fim [F: nist2020privacyframework, §2.3]. Lacuna de perfil: subcategorias do Target Profile não atingidas [I]. Risco residual: número e severidade dos riscos aceitos acima do apetite, com responsável e prazo [I]. Reavaliação: proporção de gatilhos (incidentes, mudanças de modelo, novas finalidades) seguidos de reavaliação documentada (GV.MT-P1) [I]. Viés: existência e periodicidade da avaliação de entradas e saídas analíticas (ID.RA-P2), cuja medição em si pertence a outros domínios [I].

## Exemplo técnico independente de domínio

```
registro_de_risco:
  id: R-014
  acao_de_dados: "exibir ranking de desempenho da turma ao professor"   # IR 8062: data action
  contexto: {titulares: menores, sensibilidade: desempenho + laudo, visibilidade: terceiros}
  problema_potencial: estigmatizacao de aluno com deficiencia perante colegas
  evento_temido_cnil: acesso ilegitimo (exposicao alem do necessario)
  verossimilhanca: 3/4   # percepcao do individuo tipico (aluno, responsavel)
  impacto: 4/4           # dano psicologico; proxies: abandono, reputacao
  nivel: alto
  resposta: mitigar -> ranking anonimizado por faixa; override docente registrado (ver trilha)
  residual: medio, aceito por: diretor de produto, em: 2026-03-01, revisao: 2026-09-01
  gatilhos: nova versao do modelo | incidente | nova orientacao ANPD
  subcategorias: [ID.RA-P3, ID.RA-P4, ID.RA-P5, GV.MT-P1]
```

## Relações com outros conceitos

Complementa `psg.audit.ripd-dpia` (o RIPD é o instantâneo documental do processo), `psg.audit.processing-records` (o inventário é a entrada do Identify-P) e `psg.audit.audit-trails` (a trilha é ao mesmo tempo controle de mitigação e ação de dados a avaliar). A gestão de riscos de segurança da ISO/IEC 27005 e os controles de mitigação ficam em `psg.sec.iso-27001-and-27701`; incidentes como gatilho, em `psg.sec.incident-management`. A governança de IA de `psg.ai.ai-governance-frameworks` adota estrutura análoga de funções, e a subcategoria ID.RA-P2 é o ponto de contato com a medição de viés. O risco de reidentificação (`psg.deid.reidentification-risk`) e a minimização (`psg.access.minimization-and-privacy-by-design`) são, respectivamente, um risco típico e uma resposta típica.

## Lacunas e questões abertas

- O Privacy Framework 1.1 permanece, pelo que foi verificado, em rascunho de abril de 2025; a seção sobre IA mencionada por fontes secundárias não foi lida no original e não foi citada.
- ISO 31000:2018 e ISO/IEC 27005:2022 foram consultadas apenas em amostras de prefácio e sumário; definições e etapas detalhadas não foram conferidas no texto integral.
- A NIST Privacy Risk Assessment Methodology (PRAM), citada pelo framework como catálogo ilustrativo de problemas, não foi aberta.
- Não há, nas fontes consultadas, calibração de verossimilhança e impacto para crianças e adolescentes como "indivíduo típico"; é uma lacuna metodológica relevante para o domínio.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nist2020privacyframework | tecnico | 2026-10-29 |
| nist2025privacyframework11 | tecnico (rascunho; metadados e resumo) | 2026-10-29 |
| nist2017ir8062 | tecnico | 2026-10-29 |
| iso310002018 | normativo [metadados e amostra] | 2026-10-29 |
| iso270052022 | normativo [metadados e amostra] | 2026-10-29 |
| cnil2018piamethodology | tecnico | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
| anpd2023ripdfaq | tecnico | 2026-10-29 |
