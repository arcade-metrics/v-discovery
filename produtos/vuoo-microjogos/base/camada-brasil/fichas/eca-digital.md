# Ficha: ECA Digital (Lei 15.211/2025) e ECA

> Ficha **curta**. Dono: `conhecimento/privacidade-seguranca-e-governanca/legal-framework/eca-and-digital-eca.md` (psg.legal.eca-and-digital-eca, consultado 2026-10-29). Aqui só os requisitos para o Core. Acesso: 2026-11-05 (texto não reaberto).

```yaml
id: br.eca-digital
name: Estatuto Digital da Criança e do Adolescente
acronym: ECA Digital
jurisdiction: Brasil (federal)
issuing_organization: Congresso Nacional; ANPD como autoridade administrativa autônoma (Decreto 12.622/2025); regulamento: Decreto 12.880/2026
reference_type: [lei, decreto regulamentador]
domain: [D8, D6]
official_url: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm
repository_url: not_applicable
version: "Lei 15.211 de 17/09/2025; vigência em 17/03/2026 (art. 41-A, incluído pela Lei 15.352/2026)"
publication_date: 2025-09-17
last_updated: 2026
legal_status: em vigor
mandatory_scope: produtos e serviços de TI direcionados a crianças e adolescentes ou de acesso provável (art. 1)
education_levels: [todos (alcança plataforma escolar por finalidade, [I] em psg.legal.eca-and-digital-eca)]
geographic_scope: nacional
language: pt-BR
license: domínio público [I]
technical_formats: [HTML]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: not_found
related_standards: [br.lgpd-educacao]
entities: [fornecedor, produto ou serviço de TI, acesso provável, supervisão parental, verificação de idade, relatório de transparência]
relationships: [ANPD fiscaliza; sanções até 10% do faturamento]
vocabularies: not_found
core_relevance: média-alta (configuração padrão e perfilamento)
regional_adapter_relevance: alta
limitations: [sem regra específica para serviço contratado pela escola (psg.legal.eca-and-digital-eca)]
open_questions: [Q-DAD-05]
sources: [psg.legal.eca-and-digital-eca]
access_date: 2026-11-05
research_status: verificado em conhecimento/
```

## Requisitos para o Core [I, derivados dos dispositivos citados no documento dono]

| # | Requisito | Dispositivo | Suporte |
|---|---|---|---|
| E1 | Privacidade **máxima por padrão** para usuário criança/adolescente | art. 7 | configurações do perfil com default protetivo; mudança registrada com autor |
| E2 | Gestão de riscos desde a concepção; evitar uso compulsivo | art. 8 | eventos de engajamento (C.EVT) sem mecânicas de retenção por padrão; avaliação de risco versionada |
| E3 | Vedado perfilamento para publicidade e perfis comportamentais para fins publicitários | arts. 22 e 26 | finalidade "publicidade" proibida no catálogo de finalidades; o modelo do aprendiz (perfilamento pedagógico) declara finalidade educacional |
| E4 | Relatório de impacto quando o tratamento exceder o estritamente necessário | art. 16, par. único | ligação RIPD ↔ operações (C.PRV) |
| E5 | Ferramentas de supervisão parental com padrão de alta proteção | cap. V | papel C.GRD com permissões de supervisão, distinto do papel da escola |
| E6 | Dados de verificação de idade usados só para esse fim; sem reter imagem ou documento | art. 13; Dec. 12.880 art. 24 | campo de idade derivada sem guarda do documento |
