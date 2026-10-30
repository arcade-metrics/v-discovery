---
id: psg.index
titulo: Privacidade, segurança e governança
tipo: mapa
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Privacidade, segurança e governança

Base de conhecimento agnóstica sobre como tratar dados de crianças e adolescentes em plataformas educacionais de forma lícita, segura e auditável, e como governar os modelos de IA que decidem sobre a aprendizagem deles. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo e fontes prioritárias em [`00-brief.md`](00-brief.md).

O domínio cobre sete frentes: o marco legal brasileiro para menores (LGPD, ECA, Estatuto Digital) com GDPR, AADC e COPPA como referência; consentimento parental, assentimento e ciclo de vida das permissões; controle de acesso, papéis escolares e minimização; anonimização, pseudonimização e risco de reidentificação; segurança (modelo de ameaças, criptografia, incidentes, sistemas de gestão); governança de IA; e auditoria, registro de operações, RIPD e gestão de riscos de privacidade.

## Como navegar

Comece pelo [mapa de conceitos](mapa-conceitos.md) e pelo [glossário](glossario.md). A [matriz comparativa](matriz-comparativa.md) põe lado a lado os regimes legais, os modelos de acesso, as técnicas de desidentificação, as taxonomias de ameaça, os sistemas de gestão, os frameworks e as leis de IA e os gatilhos de RIPD. O [relatório](relatorio.md) registra método, cobertura, fontes não verificadas, lacunas e respostas às perguntas do brief.

Leitura sugerida para quem chega sem contexto:

1. `legal-framework/lgpd-children.md`: o art. 14 da LGPD, o melhor interesse e o Enunciado 1/2023 da ANPD, que abre todas as bases legais para dados de menores. É o documento de que quase todos os outros dependem.
2. `legal-framework/eca-and-digital-eca.md` e `comparison.md`: a camada de direitos da criança (ECA e Lei 15.211/2025) e a comparação com GDPR, AADC e COPPA, para saber onde a norma brasileira é mais exigente e onde é silenciosa.
3. `consent/parental-consent.md`, `child-assent.md` e `permission-lifecycle.md`: quando o consentimento do responsável é exigido, como ouvir a criança (inclusive com deficiência intelectual ou de comunicação) e como registrar, revogar e migrar permissões até a maioridade.
4. `access-control/rbac-and-abac.md`, `school-roles.md` e `minimization-and-privacy-by-design.md`: quem vê o quê, e o que nem deveria existir para ser visto.
5. `de-identification/anonymization-and-pseudonymization.md`, depois `k-anonymity-and-extensions.md`, `differential-privacy.md` e `reidentification-risk.md`: quando um dado deixa de ser pessoal e quanto risco sobra.
6. `security/threat-model-education.md`, `encryption-and-key-management.md`, `incident-management.md` e `iso-27001-and-27701.md`: ameaças concretas, respostas técnicas, prazos de comunicação à ANPD e o sistema de gestão que mantém tudo isso vivo.
7. `ai-governance/ai-governance-frameworks.md`, `eu-ai-act-and-brazil.md`, `transparency-and-human-oversight.md` e `model-documentation.md`: o que governar num modelo que avalia ou recomenda, quando a lei o trata como alto risco e como explicar sem expor o modelo.
8. `audit-risk/processing-records.md`, `audit-trails.md`, `privacy-risk-management.md` e `ripd-dpia.md`: o inventário, a trilha que reconstrói decisões passadas, o processo contínuo de risco e o relatório de impacto que junta tudo.

## Pastas

| Pasta | Conteúdo | Prefixo de id | Documentos |
|---|---|---|---|
| `legal-framework/` | LGPD e menores, ECA e Estatuto Digital, GDPR/AADC/COPPA, comparação por critério | `psg.legal.*` | 4 |
| `consent/` | consentimento parental, assentimento da criança, ciclo de vida das permissões | `psg.consent.*` | 3 |
| `access-control/` | RBAC, ABAC e ReBAC; papéis escolares e separação de visões; minimização e privacy by design | `psg.access.*` | 3 |
| `de-identification/` | anonimização e pseudonimização; k-anonimato, l-diversidade, t-closeness; privacidade diferencial; risco de reidentificação | `psg.deid.*` | 4 |
| `security/` | modelo de ameaças (STRIDE, LINDDUN); criptografia e gestão de chaves; incidentes e comunicação à ANPD; ISO/IEC 27001 e 27701 | `psg.sec.*` | 4 |
| `ai-governance/` | NIST AI RMF, ISO/IEC 42001, UNICEF e UNESCO; AI Act e PL 2338/2023; transparência e supervisão humana; model cards e datasheets | `psg.ai.*` | 4 |
| `audit-risk/` | trilhas de auditoria; registro das operações (art. 37); RIPD/DPIA; gestão de riscos de privacidade | `psg.audit.*` | 4 |

A lista completa de ids planejados está em [`_plano-ids.md`](_plano-ids.md).

## Convenções do domínio

- **Fronteira com `interoperabilidade`.** Mecanismos de privacidade na troca entre sistemas (escopos OAuth, identidade federada, contratos entre controlador e operador na integração) e o texto geral da LGPD ficam em `iop.fund.privacidade-e-seguranca` e `iop.br.lgpd`. Aqui eles entram por relação (`complementa`, `especificado-por`). Papéis e matrículas vêm de `iop.ros.oneroster`, `iop.ros.ceds` e `iop.fund.identidade-e-contexto`; este domínio usa só o vocabulário de papéis.
- **Fronteira com `dados-pesquisa-e-eventos`.** Ética de pesquisa com seres humanos (CEP/CONEP), FAIR, planos de gestão de dados e documentação de dados de pesquisa ficam lá. Aqui o assentimento é tratado como boa prática de serviço, com o modelo da pesquisa como referência (`psg.consent.child-assent`), e o datasheet só como documentação do modelo de aprendizagem (`psg.ai.model-documentation`, que complementa `dat.rd.data-documentation`).
- **Fronteira com `learning-analytics-e-avaliacao` e `aprendizagem-adaptativa`.** A medição estatística de viés e de equidade (DIF, desempenho por subgrupo) fica em `lae.psy.fairness-in-measurement` e `adp.eval.*`. Aqui entra só o processo de governança que exige e acompanha essa medição (por exemplo MEASURE 2.11 do AI RMF, ID.RA-P2 do Privacy Framework). Proveniência de dados analíticos fica em `lae.dq.provenance-and-lineage`; a trilha de auditoria a reutiliza.
- **Fronteira com `realtime-multiplayer`.** TLS, DTLS, QUIC e autenticação de sessão ficam em `rtm.sec.transport-security` e `rtm.sec.authentication`; tolerância a falhas em `rtm.rel.fault-tolerance`. Este domínio trata dado em repouso, chaves e segregação de bases.
- **Fronteira com `grafo-conhecimento-educacional`.** O vocabulário PROV-O e o versionamento de artefatos ficam em `kg.std.prov-o` e `kg.eng.versioning-and-provenance`.
- **Norma estrangeira é referência, não obrigação.** GDPR, AADC, COPPA, AI Act e NIST entram como referência de desenho para operação brasileira. Cada documento diz quando a aplicação é direta e quando é analogia.
- **Projeto de lei não é lei.** O PL 2338/2023 é citado pelo texto do Senado, com a situação de tramitação na data de consulta.
- **Leitura em espelho ou só por metadados é declarada.** GDPR e AI Act foram lidos em espelhos não oficiais; normas ISO e ABNT, em geral só por metadados e sumário. A seção "Lacunas" de cada documento diz o que não foi lido.
- **Recomendação de desenho não é fato.** Matriz de visões por papel, transição à maioridade, taxa de aceite como sinal de viés de automação e indicadores de minimização são propostas dos documentos, marcadas `[I]` ou `[H]`.
