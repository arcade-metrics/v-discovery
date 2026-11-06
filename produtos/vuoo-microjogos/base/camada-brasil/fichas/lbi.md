# Ficha: LBI (Lei Brasileira de Inclusão, Lei 13.146/2015)

> Ficha **curta**: análise completa e quadro de obrigatoriedade para plataformas em `conhecimento/acessibilidade-educacao-especial-e-dua/brazil/lbi.md` (acs.br.lbi). Acesso: 2026-11-05 (texto não reaberto; datas e dispositivos conforme acs.br.lbi, consultado em 2026-10-30).

```yaml
id: br.lbi
name: Lei Brasileira de Inclusão da Pessoa com Deficiência (Estatuto da Pessoa com Deficiência)
acronym: LBI
jurisdiction: Brasil (federal)
issuing_organization: Congresso Nacional / Presidência
reference_type: lei
domain: [D7, D8]
official_url: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm
repository_url: not_applicable
version: "Lei 13.146 de 06/07/2015, compilada, com alterações até a Lei 15.249/2025"
publication_date: 2015-07-07
last_updated: 2025 (Lei 15.249/2025, CAA)
legal_status: em vigor
mandatory_scope: poder público; instituições privadas de ensino nos incisos do art. 28 §1; sítios de empresas com sede ou representação no país (art. 63)
education_levels: [todos]
geographic_scope: nacional
language: pt-BR
license: domínio público [I]
technical_formats: [HTML]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: not_applicable
related_standards: [br.aee-pneepei, br.portaria-mec-421-2026, Convenção ONU (Decreto 6.949/2009), WCAG (via art. 63, [I])]
entities: [pessoa com deficiência, barreira (6 tipos), acessibilidade, desenho universal, tecnologia assistiva, adaptação razoável, profissional de apoio escolar, avaliação biopsicossocial, formatos acessíveis]
relationships: [deficiência = impedimento × barreira (art. 2); avaliação biopsicossocial considera funções e estruturas, fatores socioambientais, limitação de atividades e restrição de participação (art. 2 §1)]
vocabularies: [tipos de barreira (art. 3, IV, a–f): urbanísticas, arquitetônicas, nos transportes, nas comunicações e na informação, atitudinais, tecnológicas]
core_relevance: alta: fornece o vocabulário legal de C.SUP (barreira, adaptação razoável, TA) que não depende de diagnóstico
regional_adapter_relevance: alta
limitations: [art. 63 sem regulamento técnico (acs.br.lbi)]
open_questions: [Q-INC-03]
sources: [acs.br.lbi]
access_date: 2026-11-05
research_status: verificado em conhecimento/
```

## Acréscimo para o Core [I]

- O modelo legal é **relacional** (impedimento em interação com barreiras). Isso sustenta, por lei, representar a necessidade como par (barreira no contexto, apoio que a remove), que é o desenho de `C.SUP` proposto no [modelo de dados](../modelo-de-dados-curriculo-avaliacao-inclusao.md).
- Os seis tipos de barreira do art. 3, IV, servem de enum de `Barreira.tipo` no adaptador; a Res. SEDUC-SP 129/2025 usa um subconjunto ("comunicacionais, arquitetônicas, atitudinais ou outras").
- Art. 28 §1: recursos de acessibilidade em escola privada sem cobrança adicional. Impacto em modelo de cobrança, não em dado.
