# Ficha: LGPD aplicada a dados de estudantes

> Ficha **curta**. Donos: `conhecimento/privacidade-seguranca-e-governanca/legal-framework/lgpd-children.md` (psg.legal.lgpd-children: art. 14, Enunciado CD/ANPD 1/2023, guia de legítimo interesse, dados sensíveis, art. 20) e `iop.br.lgpd` (troca de dados entre sistemas). Aqui só os **requisitos que o Core precisa suportar**. Acesso: 2026-11-05.

```yaml
id: br.lgpd-educacao
name: Lei Geral de Proteção de Dados Pessoais aplicada a crianças, adolescentes e dados educacionais
acronym: LGPD
jurisdiction: Brasil (federal)
issuing_organization: Congresso Nacional; ANPD (regulação e orientação)
reference_type: [lei, regulamento (resoluções CD/ANPD), orientação (enunciado, guias)]
domain: [D8, D7, D3]
official_url:
  - https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
  - https://www.gov.br/anpd/
repository_url: not_applicable
version: "Lei 13.709/2018 compilada (alterações até a Lei 15.352/2026, segundo psg.legal.lgpd-children)"
publication_date: 2018-08-15
last_updated: 2026
legal_status: em vigor
mandatory_scope: todo controlador e operador que trata dados no Brasil (escola, rede, fornecedor)
education_levels: [todos]
geographic_scope: nacional, com regras de transferência internacional
language: pt-BR
license: domínio público [I]
technical_formats: [HTML]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: not_found
related_standards: [br.eca-digital, br.aee-pneepei (Dec. 12.686 art. 12 §5 remete à LGPD art. 14)]
entities: [titular, controlador, operador, encarregado, base legal, consentimento, dado pessoal sensível, dado de criança, registro de operações, RIPD, incidente, transferência internacional]
relationships: [operação de tratamento → base legal (1) → finalidade; dado sensível → bases do art. 11 apenas]
vocabularies: [bases legais art. 7 (10) e art. 11; direitos do titular art. 18]
core_relevance: alta (C.CNS, C.PRV, classificação de dados)
regional_adapter_relevance: alta
limitations: [sem guia abrangente da ANPD para crianças (psg.legal.lgpd-children); nada específico sobre registros escolares]
open_questions: [Q-DAD-01, Q-DAD-02, Q-DAD-03, Q-DAD-04]
sources: [psg.legal.lgpd-children, E-34]
access_date: 2026-11-05
research_status: verificado em conhecimento/; transferência internacional por fontes secundárias
```

## Requisitos que o Core precisa suportar

| # | Requisito | Base | Suporte no Core [I] |
|---|---|---|---|
| L1 | **Base legal por operação**, registrada antes de iniciar | LGPD arts. 7, 11, 37 | `C.CNS` não é só "consentimento": é `LegalBasis` com tipo (enum dos arts. 7 e 11), finalidade, operação e justificativa; registro de operações (art. 37) |
| L2 | Consentimento parental **específico e em destaque** de um dos pais/responsável quando a base for consentimento e o titular for criança (< 12 anos); verificação razoável | art. 14 §§1 e 5 | `Consent` com sujeito (criança), outorgante (C.GRD com vínculo), escopo, data, meio de verificação, revogação (art. 8 §5) |
| L3 | Outras bases admitidas para crianças, desde que prevaleça o melhor interesse, avaliado no caso | Enunciado CD/ANPD 1/2023 | `LegalBasis.avaliacaoMelhorInteresse` (texto/ref. a documento) obrigatória para titular < 18 |
| L4 | Dado de deficiência, laudo, diagnóstico, hipótese diagnóstica, acompanhamento terapêutico = **dado sensível de saúde**; legítimo interesse não se aplica | arts. 5 II, 11; guia ANPD 2024 | classificação de sensibilidade **por campo**; bases restritas ao art. 11; inferência de condição também é sensível (art. 11 §1) |
| L5 | Minimização: não condicionar participação a dados além do estritamente necessário | art. 14 §4 | campos de diagnóstico sempre opcionais (convergente com Port. MEC 421 art. 7 §4) |
| L6 | Informação pública e acessível sobre dados coletados e direitos, adequada à criança | art. 14 §§2 e 6 | metadados de finalidade por campo exportáveis para aviso de privacidade |
| L7 | Revisão de decisão automatizada e explicação de critérios | art. 20 | `C.PRV` em toda inferência (modelo, versão, entradas); trilha para revisão humana |
| L8 | **Retenção**: término do tratamento e eliminação, com conservação autorizada para obrigação legal ou regulatória, pesquisa (anonimizada sempre que possível), transferência a terceiro conforme a lei ou uso exclusivo do controlador anonimizado | arts. 15 e 16 (conferidos no Planalto em 2026-11-05) | política de retenção **por categoria de dado**, com motivo de conservação; prazo de guarda de registros escolares é questão de outra norma (Q-DAD-02) |
| L9 | **Transferência internacional** só nas 9 hipóteses do art. 33 (adequação, cláusulas-padrão/específicas, consentimento específico e em destaque, execução de política pública etc.); regulamento e cláusulas-padrão da ANPD (Res. CD/ANPD 19/2024; prazo para adotar as cláusulas terminou em 23/08/2025) | arts. 33–36; Res. CD/ANPD 19/2024 (fontes secundárias) | registrar localização do processamento e mecanismo de transferência por operador/subprocessador. **Não foi encontrado dispositivo que exija armazenar dados no Brasil** (leitura dos arts. 3, 15, 16 e 33 no Planalto em 2026-11-05; últimos ~25 mil caracteres da página não lidos; Q-DAD-03) |
| L10 | Documentos de AEE (PAEE, PEI) com dados pessoais e sensíveis devem observar a LGPD "com atenção ao seu art. 14" | Dec. 12.686 art. 12 §5 | o plano individual herda L1–L8 e tem controle de acesso por papel |
