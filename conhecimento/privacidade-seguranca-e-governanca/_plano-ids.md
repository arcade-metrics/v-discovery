---
id: psg.plano-ids
titulo: Plano de identificadores do domínio
tipo: mapa
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Plano de identificadores do domínio privacidade-seguranca-e-governanca

Lista de ids planejados para a primeira versão, derivada da estrutura sugerida em `00-brief.md`. Relações entre documentos usam estes ids, nunca caminhos de arquivo. Prefixos de área: `legal`, `consent`, `access`, `deid`, `sec`, `ai`, `audit`.

| Pasta | Id | Arquivo | Escopo em uma linha |
|---|---|---|---|
| legal-framework | psg.legal.lgpd-children | legal-framework/lgpd-children.md | LGPD aplicada a crianças e adolescentes: art. 14, melhor interesse, bases legais em contexto escolar, enunciados e guias da ANPD |
| legal-framework | psg.legal.eca-and-digital-eca | legal-framework/eca-and-digital-eca.md | ECA (Lei 8.069/1990) e a lei de proteção de crianças em ambientes digitais ("ECA Digital"), no que toca plataformas educacionais |
| legal-framework | psg.legal.gdpr-k-and-coppa | legal-framework/gdpr-k-and-coppa.md | Referências comparativas: GDPR (art. 8 e considerandos sobre crianças), UK Age Appropriate Design Code, COPPA |
| legal-framework | psg.legal.comparison | legal-framework/comparison.md | Comparação LGPD x GDPR x COPPA x AADC por critério (idade, base legal, verificação parental, design, sanções) |
| consent | psg.consent.parental-consent | consent/parental-consent.md | Consentimento parental: quando é exigido, forma, verificação razoável, prova |
| consent | psg.consent.child-assent | consent/child-assent.md | Assentimento da criança: fundamentos (ética em pesquisa e direito), linguagem adequada à idade, deficiência intelectual e de comunicação |
| consent | psg.consent.permission-lifecycle | consent/permission-lifecycle.md | Gestão de permissões ao longo do tempo: revogação, mudança de finalidade, transição à maioridade, registro de consentimentos |
| access-control | psg.access.rbac-and-abac | access-control/rbac-and-abac.md | Modelos de controle de acesso (RBAC, ABAC, ReBAC), com a referência NIST |
| access-control | psg.access.school-roles | access-control/school-roles.md | Papéis escolares (aluno, responsável, professor, coordenador, gestor de rede, equipe de apoio) e separação de visões |
| access-control | psg.access.minimization-and-privacy-by-design | access-control/minimization-and-privacy-by-design.md | Minimização, limitação de finalidade e privacy by design/by default como requisitos de arquitetura |
| de-identification | psg.deid.anonymization-and-pseudonymization | de-identification/anonymization-and-pseudonymization.md | Definições (LGPD art. 5 e 12, ISO/IEC 20889), quando o dado deixa de ser pessoal, pseudonimização reversível |
| de-identification | psg.deid.k-anonymity-and-extensions | de-identification/k-anonymity-and-extensions.md | k-anonimato, l-diversidade, t-closeness; ataques de ligação e homogeneidade |
| de-identification | psg.deid.differential-privacy | de-identification/differential-privacy.md | Privacidade diferencial: definição, epsilon, mecanismos, orçamento de privacidade, limites práticos |
| de-identification | psg.deid.reidentification-risk | de-identification/reidentification-risk.md | Risco de reidentificação: métricas, estudos clássicos, NIST SP 800-188, dados de interação de menores |
| security | psg.sec.threat-model-education | security/threat-model-education.md | Modelo de ameaças para dados educacionais de menores: ativos, atores, vetores, metodologia (STRIDE, LINDDUN) |
| security | psg.sec.encryption-and-key-management | security/encryption-and-key-management.md | Criptografia em trânsito e em repouso, gestão de chaves, segregação de bases |
| security | psg.sec.incident-management | security/incident-management.md | Gestão de incidentes e comunicação à ANPD e aos titulares (art. 48 e regulamento) |
| security | psg.sec.iso-27001-and-27701 | security/iso-27001-and-27701.md | ISO/IEC 27001 e 27701 como sistemas de gestão; relação com NIST SP 800-53 |
| ai-governance | psg.ai.ai-governance-frameworks | ai-governance/ai-governance-frameworks.md | NIST AI RMF 1.0, ISO/IEC 42001, UNICEF e UNESCO sobre IA e crianças |
| ai-governance | psg.ai.eu-ai-act-and-brazil | ai-governance/eu-ai-act-and-brazil.md | AI Act europeu (educação como alto risco) e PL 2338/2023 no Brasil |
| ai-governance | psg.ai.transparency-and-human-oversight | ai-governance/transparency-and-human-oversight.md | Transparência, explicabilidade e supervisão humana em decisões sobre aprendizes (LGPD art. 20) |
| ai-governance | psg.ai.model-documentation | ai-governance/model-documentation.md | Model cards, datasheets e documentação de modelos de aprendizagem |
| audit-risk | psg.audit.audit-trails | audit-risk/audit-trails.md | Trilhas de auditoria e rastreabilidade de decisões: o que registrar, integridade, retenção |
| audit-risk | psg.audit.processing-records | audit-risk/processing-records.md | Registro das operações de tratamento (LGPD art. 37) e inventário de dados |
| audit-risk | psg.audit.ripd-dpia | audit-risk/ripd-dpia.md | Relatório de impacto à proteção de dados (RIPD/DPIA): quando, conteúdo, método |
| audit-risk | psg.audit.privacy-risk-management | audit-risk/privacy-risk-management.md | NIST Privacy Framework e gestão de riscos de privacidade como processo contínuo |
| (raiz) | psg.index | README.md | |
| (raiz) | psg.glossario | glossario.md | |
| (raiz) | psg.mapa | mapa-conceitos.md | |
| (raiz) | psg.matriz | matriz-comparativa.md | |
| (raiz) | psg.relatorio | relatorio.md | |
| (raiz) | psg.plano-ids | _plano-ids.md | |
| (raiz) | psg.brief | 00-brief.md | |
