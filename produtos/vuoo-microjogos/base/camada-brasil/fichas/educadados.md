# Ficha: EducaDados (Infraestrutura Nacional de Dados da Educação, Inde) e Sistema Nacional de Educação (LC 220/2025)

Duas normas encadeadas: a **Lei Complementar 220/2025** institui o Sistema Nacional de Educação (SNE) e, nos arts. 24–26, a **Inde** com o **CPF como Identificador Nacional Único do Estudante (Inue)**; a **Portaria MEC 269/2026** regulamenta a Inde, dá a ela o nome **EducaDados** e institui a **Plataforma Nacional de Dados da Educação**.

```yaml
id: br.mec.educadados
name: Infraestrutura Nacional de Dados da Educação – EducaDados; Plataforma Nacional de Dados da Educação
acronym: Inde / EducaDados / Inue
jurisdiction: Brasil (federal, com aplicação aos entes federados)
issuing_organization: "Congresso Nacional (LC 220/2025); Ministério da Educação, Secretaria de Gestão da Informação, Inovação e Avaliação de Políticas Educacionais (Portaria 269/2026)"
reference_type: lei complementar + regulamento (portaria ministerial)
domain: [D8, D3]
official_url: https://mecnormas.mec.gov.br/pesquisa/detalhar/9047
repository_url: not_found
version: "LC 220, de 31/10/2025 (DOU 03/11/2025); Portaria MEC 269, de 24/03/2026 (DOU 26/03/2026)"
publication_date: 2026-03-26
last_updated: 2026-03-26
legal_status: "vigente; Portaria 269 art. 2º: 'de observância obrigatória pela Administração Pública direta, autárquica e fundacional da União, dos estados, do Distrito Federal e dos municípios e, no que couber, pelos estabelecimentos educacionais privados e comunitários'"
mandatory_scope: "Inue (CPF) obrigatório nas bases e registros administrativos dos sistemas de ensino quando houver tratamento de dados em nível de estudante (Portaria 269 art. 7º; LC 220 art. 26 I)"
education_levels: [todos os níveis dos sistemas de ensino]
geographic_scope: nacional
language: pt-BR
license: domínio público (atos normativos)
technical_formats: not_found (o "Padrão Nacional de Interoperabilidade da Educação" ainda não foi publicado)
api_available: "previsto como produto de dados (Portaria 269 art. 15 §2º VI: 'Interface de Programação de Aplicações - API para consumo de dados'); not_found em operação"
data_model_available: "não; 'conjuntos mínimos de dados' a definir pelo MEC com os sistemas (art. 8º) [I: o CMDEB é o conjunto mínimo já existente para a EB, mas a Portaria 269 não o cita]"
ontology_available: não
schemas_available: não
implementation_examples: not_found
related_standards: [br.mec.cmdeb, br.mec.gestao-presente, br.inep.censo-escolar, iop.br.lgpd]
entities: [Estudante (via Inue), conjuntos mínimos de dados, Plataforma, Comitê Consultivo CC/EducaDados]
relationships: "Inde → conjuntos mínimos + padrão de interoperabilidade + plataforma + transparência (LC 220 art. 26 I–V)"
vocabularies: not_found
core_relevance: alta (fixa o identificador nacional do estudante e a obrigação de interoperar)
regional_adapter_relevance: alta
limitations: "regulamento é de princípios; padrão técnico, modelos informacionais, protocolos e composição do comitê dependem de atos futuros (arts. 9–11, 21, 23); implementação gradual (art. 22)"
open_questions: [Q-02, Q-07, Q-10]
sources: [E21, E30]
access_date: 2026-11-05
research_status: completo para o texto normativo; especificações técnicas not_found
```

## Conteúdo normativo (E21, E30)

| Tema | LC 220/2025 | Portaria MEC 269/2026 |
|---|---|---|
| Criação | art. 24: institui a Inde (interoperabilidade, compartilhamento, qualidade, segurança; LGPD) | art. 1º: regulamenta a Inde, denominada **EducaDados**, e institui a Plataforma Nacional de Dados da Educação |
| Governança | art. 25: União/MEC organiza, normatiza, coordena e supervisiona | art. 16: MEC, pela Secretaria de Gestão da Informação, Inovação e Avaliação de Políticas Educacionais; arts. 17–21: Comitê Consultivo CC/EducaDados (composição em ato próprio) |
| **Inue** | art. 26 I: "a instituição do Cadastro de Pessoas Físicas (CPF) como o Identificador Nacional Único do Estudante (Inue), de uso obrigatório em todas as bases de dados e registros administrativos dos sistemas de ensino da União, dos Estados, do Distrito Federal e dos Municípios, com a finalidade de assegurar a interoperabilidade dos dados educacionais" (transcrição literal); §2º: uso para indicadores de fluxo, retenção, mobilidade, trajetórias, evasão | art. 7º: CPF constitui o Inue, "de uso obrigatório nas bases de dados e registros administrativos dos sistemas de ensino quando houver tratamento de dados em nível de estudante"; §2º: indicadores de trajetória |
| Conjuntos mínimos | art. 26 II e §1º | art. 8º: definidos e atualizados pelo MEC em colaboração com os sistemas; critérios de finalidade pública, necessidade, padronização, proteção de dados |
| Padrão de interoperabilidade | art. 26 III: protocolos técnicos, modelos de dados, autenticação, validação, integridade, segurança | arts. 9–11: "Padrão Nacional de Interoperabilidade da Educação" com, no mínimo, protocolos de intercâmbio, modelos informacionais e requisitos de segurança; sistemas de ensino "deverão observar" |
| Plataforma | art. 26 IV | arts. 12–15: compartilhamento entre sistemas; acesso por esfera de competência, finalidade pública, necessidade e perfis; produtos (estatísticas, indicadores, painéis, relatórios, **API**) |
| Deveres dos entes | arts. 6º XI e 7º VIII: estados e municípios fornecem dados de forma tempestiva, regular e padronizada pela plataforma nacional (paráfrase) | — |
| Escolas privadas | art. 26 §3º: no que couber | art. 2º: no que couber |
| Vigência | publicação | publicação (26/03/2026); implementação gradual (art. 22) |

## Relação com o restante [I]

- MEC Gestão Presente (Portaria 234/2025) e CMDEB (Portaria 832/2025) **precedem** a LC 220 e a Portaria 269; a Portaria 269 não os menciona. O MEC já trata o SGP como "Plataforma de Dados da Educação Básica" (E34). Não há ato que declare o SGP como a "Plataforma Nacional de Dados da Educação" nem o CMDEB como "conjunto mínimo" da EducaDados (ver Q-10).
- A LC 220 menciona o Censo apenas para indicadores de avaliação (art. 50 §1º I, paráfrase); não altera o Decreto 6.425/2008.
- O Inue (CPF) choca com a prática do Censo de não exigir CPF de aluno fora da EJA (E02 30 c5). Transição não regulamentada.

## Implicação para o Core

O Core deve aceitar o CPF como identificador de pessoa com `scheme=br-cpf`, tratado como dado pessoal (finalidade: interoperabilidade), e o adaptador Brasil deve exigir CPF de estudante quando operar dados "em nível de estudante" para redes públicas, registrando a base legal (C.CNS) como "obrigação legal: LC 220 art. 26 I; Portaria MEC 269/2026 art. 7º". Detalhe de base legal e minimização: frente de privacidade.
