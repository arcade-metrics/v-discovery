# GDPR (art. 8) e AI Act (fichas curtas, apontamento)

## GDPR

```yaml
id: eu-gdpr
name: Regulamento (UE) 2016/679 (General Data Protection Regulation)
acronym: GDPR / RGPD
jurisdiction: UE/EEE
issuing_organization: Parlamento Europeu e Conselho
reference_type: lei (regulamento, aplicação direta)
domain: [D8]
official_url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
repository_url: n/a
version: texto consolidado (versão não verificada nesta sessão)
publication_date: 2016-05-04
last_updated: unknown
legal_status: obrigatório
mandatory_scope: todo tratamento de dados pessoais no âmbito do art. 3
education_levels: todos
geographic_scope: UE/EEE (e extraterritorial, art. 3(2))
language: todas as línguas oficiais
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [eu-ai-act, uk-gdpr]
entities: titular, responsável, subcontratante, base legal, consentimento
relationships: n/a
vocabularies: bases legais do art. 6
core_relevance: alta (C.CNS, C.PRV)
regional_adapter_relevance: alta
limitations: idade do art. 8 varia por Estado-membro (13 a 16)
open_questions: tabela de idades por Estado-membro não verificada em fonte primária
sources: [S-UE-23]
access_date: 2026-11-05
research_status: apontado
```

**Dono do fato:** `conhecimento/privacidade-seguranca-e-governanca/legal-framework/gdpr-k-and-coppa.md` (`psg.legal.gdpr-k-and-coppa`). Lá estão o art. 8(1) (16 anos, Estado pode baixar até 13), o art. 8(2) (esforços razoáveis de verificação) e a exclusão do legítimo interesse para autoridades públicas (art. 6(1)).

**O que falta para o Core [I]:** C.CNS precisa de `jurisdiction` e de uma **idade-limite parametrizada por Estado** (não constante); e de base legal distinta de consentimento (missão de interesse público, art. 6(1)(e)), que é a base típica de escola pública. A tabela de idades por Estado-membro continua pendente (já registrada no documento dono).

## AI Act

```yaml
id: eu-ai-act
name: Regulamento (UE) 2024/1689 (Artificial Intelligence Act)
acronym: AI Act
jurisdiction: UE
issuing_organization: Parlamento Europeu e Conselho
reference_type: lei (regulamento)
domain: [D5, D6, D8]
official_url: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
repository_url: n/a
version: ver documento dono (inclui redação de 2026 do art. 113, Digital Omnibus)
publication_date: 2024
last_updated: ver documento dono
legal_status: obrigatório, aplicação escalonada
mandatory_scope: provedores e implantadores de sistemas de IA; educação no Anexo III
education_levels: todos
geographic_scope: UE
language: todas
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [eu-gdpr]
entities: provider, deployer, sistema de alto risco
relationships: n/a
vocabularies: categorias do Anexo III
core_relevance: alta para registro de decisões automatizadas (C.PRV, C.EVD)
regional_adapter_relevance: alta
limitations: n/a
open_questions: ver documento dono
sources: [S-UE-24]
access_date: 2026-11-05
research_status: apontado
```

**Dono do fato:** `conhecimento/privacidade-seguranca-e-governanca/ai-governance/eu-ai-act-and-brazil.md` (`psg.ai.eu-ai-act-and-brazil`): quando a educação é alto risco, obrigações e calendário.

**O que falta para o Core [I]:** qualquer avaliação ou recomendação automatizada (C.RES gerado por IA, alocação em percurso adaptativo) precisa carregar proveniência que diga "gerado por sistema X versão Y, revisado por humano Z", para permitir logs e supervisão humana exigidos para alto risco.

## Acessibilidade (EN 301 549)

Já analisada em `conhecimento/acessibilidade-educacao-especial-e-dua/standards/procurement-en-301-549-and-section-508.md` (`acs.std.procurement-en-301-549-and-section-508`). Requisito de produto, sem efeito no modelo de dados do Core.
