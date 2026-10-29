---
id: psg.brief
titulo: Brief do domínio privacidade, segurança e governança
tipo: relatorio
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: privacidade, segurança e governança

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Como tratar dados de crianças e adolescentes em plataformas educacionais de forma lícita, segura e auditável, e como governar os modelos de IA que decidem sobre a aprendizagem deles. Inclui: LGPD aplicada a menores (art. 14, melhor interesse, bases legais em contexto escolar), ECA e orientações da ANPD; consentimento parental, assentimento da criança e gestão de permissões ao longo do tempo (revogação, mudança de finalidade, maioridade); controle de acesso (RBAC/ABAC, papéis escolares como aluno, responsável, professor e gestor) e minimização de dados por desenho; anonimização e pseudonimização (k-anonimato, privacidade diferencial, risco de reidentificação, quando o dado deixa de ser pessoal segundo a LGPD); segurança de dados educacionais (modelo de ameaças, criptografia em trânsito e em repouso, gestão de incidentes e comunicação à ANPD); governança de IA e de modelos de aprendizagem (transparência, explicabilidade, viés, supervisão humana, documentação de modelos); auditoria, rastreabilidade e gestão de riscos (trilhas de auditoria, registro das operações de tratamento, RIPD/DPIA, frameworks de risco).

Fora do escopo: mecanismos de privacidade na troca entre sistemas, como escopos OAuth e identidade federada (ficam em `interoperabilidade/fundamentos/privacidade-e-seguranca.md` e `interoperabilidade/brazil/lgpd.md`, citados aqui); ética de pesquisa com seres humanos (CEP/CONEP), FAIR e planos de gestão de dados (ficam em `dados-pesquisa-e-eventos`); medição de viés e fairness como propriedade estatística de modelos e instrumentos (fica em `aprendizagem-adaptativa/evaluation` e `learning-analytics-e-avaliacao/psychometrics`; aqui entra apenas o processo de governança que exige e acompanha essa medição); segurança de rede e de tempo real do jogo (fica em `realtime-multiplayer/reliability-security`).

## Estrutura sugerida

- `legal-framework/`: LGPD com foco em menores, ECA, regulamentos e guias da ANPD, comparação de referência com GDPR-K e COPPA.
- `consent/`: consentimento parental, assentimento, gestão de permissões, revogação e transição à maioridade.
- `access-control/`: modelos de controle de acesso, papéis escolares, minimização e privacy by design.
- `de-identification/`: anonimização, pseudonimização, k-anonimato, privacidade diferencial, risco de reidentificação.
- `security/`: modelo de ameaças para dados educacionais, criptografia, gestão de incidentes.
- `ai-governance/`: governança de IA e de modelos de aprendizagem, transparência, supervisão humana, model cards.
- `audit-risk/`: trilhas de auditoria, rastreabilidade, registro de operações, RIPD/DPIA, gestão de riscos.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. Lei 13.709/2018 (LGPD), em especial art. 14; Lei 8.069/1990 (ECA); enunciados e guias da ANPD sobre tratamento de dados de crianças e adolescentes e sobre segurança para agentes de tratamento de pequeno porte.
2. ABNT NBR ISO/IEC 27001 e 27701 (gestão de segurança e de privacidade da informação).
3. NIST Privacy Framework e NIST SP 800-53 (controles de segurança e privacidade); NIST SP 800-188 (desidentificação de dados governamentais).
4. Sweeney, k-anonimato; Dwork e Roth, "The Algorithmic Foundations of Differential Privacy".
5. NIST AI Risk Management Framework (AI RMF 1.0); ISO/IEC 42001 (sistema de gestão de IA); Regulamento Europeu de IA, que classifica sistemas educacionais como alto risco; tramitação do PL 2338/2023 no Brasil.
6. Mitchell et al., "Model Cards for Model Reporting".
7. UNICEF, "Policy Guidance on AI for Children"; UNESCO, orientações sobre IA generativa na educação.

## Perguntas abertas

- Qual a base legal adequada para cada tratamento de uma plataforma usada pela escola, e quando o consentimento parental do art. 14 é de fato exigido?
- Como desenhar assentimento significativo para crianças com deficiência intelectual ou de comunicação, público do produto de educação especial?
- Dados de laudo e de deficiência são dado sensível de saúde; que controles adicionais isso impõe a modelos de aluno que os usam como atributo?
- Que nível de anonimização torna um dataset de interação de menores compartilhável para pesquisa sem risco relevante de reidentificação?
- Como explicar uma decisão de adaptação do modelo para professor e responsável sem expor o modelo inteiro?
- Que trilha de auditoria mínima permite reconstruir por que o sistema recomendou algo a um aluno numa data passada?
