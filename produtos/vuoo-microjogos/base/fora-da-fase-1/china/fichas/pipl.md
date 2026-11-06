# Ficha: 中华人民共和国个人信息保护法 (PIPL, Lei de Proteção de Informações Pessoais)

> A China não aparece em `conhecimento/privacidade-seguranca-e-governanca/legal-framework/comparison.md` (verificado em 2026-11-05); esta ficha é a primeira análise da PIPL no repositório.

```yaml
id: cn.pipl
name: 中华人民共和国个人信息保护法 (Personal Information Protection Law)
acronym: PIPL
jurisdiction: China
issuing_organization: Comitê Permanente da Assembleia Popular Nacional (13ª, 30ª sessão) [C13]
reference_type: lei
domain: [D8, D3]
official_url: https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
repository_url: n/a
version: 2021
publication_date: 2021-08-20 [C13]
last_updated: not_found (sem alteração localizada)
legal_status: vigente desde 2021-11-01 (art. 74) [C13]
mandatory_scope: tratamento de dados de pessoas físicas na China; extraterritorial quando o fim é oferecer produtos/serviços a pessoas na China (art. 3)
education_levels: todos
geographic_scope: nacional + extraterritorial
language: chinês
license: n/a
technical_formats: n/a
api_available: n/a
data_model_available: n/a
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [DSL, CSL, 未成年人网络保护条例, 促进和规范数据跨境流动规定, 网络数据安全管理条例, GB/T 35273-2020, JY/T 0643-2025]
entities: [indivíduo, controlador (个人信息处理者), receptor no exterior, informação sensível, responsável legal]
relationships: menor < 14 → consentimento do responsável; transferência → receptor + consentimento separado
vocabularies: categorias de informação sensível (art. 28)
core_relevance: alta (C.CNS, C.PER, residência de dados)
regional_adapter_relevance: alta
limitations: volumes que disparam localização (art. 40) e a avaliação vêm de regulamento da CAC (ver ficha transferencia-2024)
open_questions: [QA-16]
sources: [C13]
access_date: 2026-11-05
research_status: artigos relevantes verificados no texto oficial
```

## Artigos que afetam a arquitetura [C13]

| Art. | Regra | Efeito no desenho [I] |
|---|---|---|
| 3 | aplica-se ao tratamento no território; e fora dele quando o fim é oferecer produto/serviço a pessoas na China | operar da nuvem brasileira para escolas chinesas **não** afasta a PIPL |
| 28 | sensível inclui biometria, saúde, localização e "**不满十四周岁未成年人的个人信息**"; só com finalidade específica, necessidade suficiente e proteção rigorosa | quase todo dado de aluno até ~8º ano é sensível em bloco |
| 29 | sensível exige **consentimento separado** (单独同意) | consentimento granular por finalidade |
| 30 | aviso adicional sobre necessidade e impacto | texto de aviso específico por finalidade |
| 31 | menor de 14: **consentimento dos pais ou outro responsável** e **regras de tratamento específicas** | C.CNS com sujeito ≠ titular; política de privacidade própria para menores |
| 38 | saída do país: avaliação de segurança da CAC, certificação ou contrato-padrão (ou outra condição legal) | ver ficha [transferencia-2024](transferencia-2024.md) |
| 39 | saída do país: informar receptor, finalidade, tipos de dados e direitos; **consentimento separado** | um fluxo de consentimento específico para transferência |
| 40 | CIIO e controladores acima do volume fixado pela CAC **armazenam no território**; saída só com avaliação | |
| 41 | não fornecer a autoridades judiciais/policiais estrangeiras sem aprovação chinesa | conflito potencial com pedidos legais de outras jurisdições sobre uma instância única |
| 45 | acesso, cópia e **portabilidade** (quando atendidas condições da CAC) | exportação por titular |
| 52–53 | responsável por proteção de dados acima de volume; **controlador estrangeiro do art. 3 nomeia representante/estrutura na China** | |
| 54–55 | auditoria periódica de conformidade; avaliação de impacto antes de tratar sensível, transferir ao exterior, decisões automatizadas | DPIA por funcionalidade |
| 58 | obrigações extras para plataformas grandes | |
| 24 | decisão automatizada: transparência e equidade; push de informação por decisão automatizada exige opção não baseada em características pessoais ou recusa fácil; decisão de impacto relevante dá direito a explicação e a recusar decisão só automatizada | recomendação adaptativa precisa de modo sem perfil e de explicação [I] |
