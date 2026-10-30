---
id: acs.index
titulo: Acessibilidade, educação especial e Desenho Universal para a Aprendizagem
tipo: mapa
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Acessibilidade, educação especial e Desenho Universal para a Aprendizagem

Base de conhecimento agnóstica sobre como tornar ambientes digitais de aprendizagem utilizáveis e participáveis por toda a variabilidade de aprendizes, com atenção a pessoas com deficiência e ao público da educação especial. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo, fontes prioritárias e perguntas abertas estão em [`00-brief.md`](00-brief.md).

O domínio cobre nove frentes: modelos de deficiência, barreira, adaptação razoável e desenho universal; o DUA (UDL) com as diretrizes do CAST, a evidência e a relação com diferenciação; as normas de acessibilidade digital (WCAG, WAI-ARIA, ISO/IEC 24751, EN 301 549, Section 508) e as diretrizes de jogos; tecnologia assistiva (classificação, leitores de tela e APIs, acesso alternativo, CAA); as dimensões de acesso cognitiva, visual, auditiva e motora; adaptação de interface e de atividade (perfis de preferência, acomodação x modificação, jogos, adaptação algorítmica); participação, autodeterminação e design participativo; avaliação de conformidade, testes com usuários, instrumentos de barreira e suporte, PEI e plano de AEE; e o marco brasileiro (LBI, política de educação especial e AEE, eMAG e ABNT NBR 17225, Libras).

## Como navegar

Comece pelo [mapa de conceitos](mapa-conceitos.md) e pelo [glossário](glossario.md). A [matriz comparativa](matriz-comparativa.md) põe lado a lado modelos de deficiência, deveres jurídicos, abordagens de desenho, normas técnicas, meios de acesso, licenças de símbolos, perfis de preferência, formas de adaptação, métodos e instrumentos de avaliação, planos individuais e o quadro de obrigatoriedade brasileiro. O [relatório](relatorio.md) registra método, cobertura, fontes não verificadas, lacunas, inconsistências para revisão e respostas às perguntas do brief.

Leitura sugerida para quem chega sem contexto:

1. `foundations/disability-models.md`, depois `barriers-and-reasonable-accommodation.md` e `universal-design.md`: onde está a deficiência (na interação, não no corpo), os dois deveres distintos (acessibilidade *ex ante* e adaptação razoável *ex nunc*) e de onde vem a ideia de desenho universal. Quase todos os outros documentos dependem desses três.
2. `brazil/lbi.md`: as definições legais brasileiras e o quadro do que é obrigatório e do que é só recomendado para plataformas educacionais.
3. `standards/wcag.md` e `standards/comparison.md`: o piso técnico verificável e o que cada outra norma acrescenta. Depois, conforme a necessidade, `wai-aria.md`, `procurement-en-301-549-and-section-508.md`, `accessforall-iso-24751.md` e `game-accessibility-guidelines.md`.
4. `access-dimensions/cognitive-accessibility.md`, `visual.md`, `auditory.md` e `motor.md`: barreiras e requisitos por dimensão, começando pela cognitiva, onde a WCAG cobre menos.
5. `assistive-tech/classification-iso-9999.md`, `screen-readers-and-accessibility-apis.md`, `alternative-access.md` e `aac.md`: o que a tecnologia assistiva é, como ela lê a interface e que tempos e alvos ela exige.
6. `udl/udl-guidelines.md`, `udl-evidence.md` e `udl-differentiation-and-individualization.md`: o framework, o que de fato foi testado e como ele se separa de diferenciação e de adaptação individual.
7. `adaptation/accommodation-vs-modification.md`, depois `preference-profiles.md`, `adapting-games-and-activities.md` e `algorithmic-adaptation-and-autonomy.md`: o critério do construto, a preferência declarada, a adaptação de mecânicas e quando adaptar automaticamente retira a escolha.
8. `participation/inclusive-and-participatory-design.md`, `self-determination.md` e `participation-as-construct.md`: a pessoa como participante do desenho e como agente causal, e como medir participação.
9. `assessment/conformance-evaluation.md`, `user-testing-with-at.md`, `barriers-and-support-needs.md` e `pei-and-aee-plans.md`: como avaliar o produto e como avaliar barreiras e apoios sem reduzir a pessoa a um diagnóstico.
10. `brazil/pneepei-and-aee.md`, `emag-and-nbr-17225.md` e `libras.md`: a linha do tempo da política de educação especial até a Portaria MEC 421/2026, os referenciais técnicos brasileiros e os deveres sobre Libras.

## Pastas

| Pasta | Conteúdo | Prefixo de id | Documentos |
|---|---|---|---|
| `foundations/` | modelos de deficiência; barreira, acessibilidade e adaptação razoável; desenho universal e desenho inclusivo | `acs.found.*` | 3 |
| `udl/` | DUA e diretrizes do CAST 3.0; evidência empírica; DUA x diferenciação x adaptação individual | `acs.udl.*` | 3 |
| `standards/` | WCAG 2.2 e WCAG 3; WAI-ARIA 1.2 e APG; ISO/IEC 24751 e AccessForAll; EN 301 549 e Section 508; GAG, XAG e APX; comparação | `acs.std.*` | 6 |
| `assistive-tech/` | conceito e ISO 9999; leitores de tela e APIs de acessibilidade; acionadores, varredura, olhar e voz; CAA e licenças de símbolos | `acs.at.*` | 4 |
| `access-dimensions/` | acessibilidade cognitiva (COGA, linguagem simples, leitura fácil); visual; auditiva; motora | `acs.dim.*` | 4 |
| `adaptation/` | perfis de preferência; acomodação x modificação; adaptação de jogos e atividades; adaptação algorítmica e autonomia | `acs.adapt.*` | 4 |
| `participation/` | desenho inclusivo e design participativo; autodeterminação; participação como construto | `acs.part.*` | 3 |
| `assessment/` | avaliação de conformidade (WCAG-EM 2.0, ACT Rules, ferramentas, VPAT); testes com usuários de TA; barreiras e suporte; PEI e plano de AEE | `acs.asmt.*` | 4 |
| `brazil/` | LBI e quadro de obrigatoriedade; PNEEPEI, PNEEI e AEE; eMAG 3.1 e NBR 17225; Libras | `acs.br.*` | 4 |

A lista completa de ids planejados está em [`_plano-ids.md`](_plano-ids.md).

## Convenções do domínio

- **Fronteira com `fundamentos-pedagogicos`.** Este domínio é dono das definições, diretrizes, normas e do marco legal: o que é DUA, o que a WCAG exige, o que a LBI obriga, o que é um PEI. `fundamentos-pedagogicos` trata o uso em sala e a eficácia pedagógica, citando ids `acs.*`: DUA em sala em `ped.incl.udl-in-practice`, tecnologia assistiva no ensino em `ped.incl.assistive-technology-in-teaching`, práticas baseadas em evidência por população em `ped.incl.evidence-based-practices-by-population`, delineamentos de caso único em `ped.std.single-case-designs`.
- **Fronteira com `interoperabilidade`.** A CIF entra aqui só como modelo conceitual de funcionalidade, barreira e facilitador. A CIF como padrão de codificação e intercâmbio fica em `iop.health.cif`. Conformidade versus certificação fica em `iop.fund.conformidade-e-certificacao`.
- **Fronteira com `aprendizagem-adaptativa` e `gamificacao-e-jogos`.** Modelos de aluno e algoritmos de adaptação ficam em `adp.*`; dificuldade dinâmica e evidência de jogos em educação especial, em `gam.diff.dynamic-difficulty-adjustment` e `gam.evid.special-education-and-neurodivergence`. Aqui entra só o que a adaptação e a mecânica precisam respeitar para serem acessíveis e preservarem a escolha.
- **Fronteira com `privacidade-seguranca-e-governanca`, `learning-analytics-e-avaliacao` e `dados-pesquisa-e-eventos`.** Dado de deficiência como dado sensível, assentimento e papéis escolares ficam em `psg.*`; validade, confiabilidade e equidade de medidas, em `lae.psy.*`; ética de pesquisa e a lei de Fitts como medida, em `dat.*`.
- **Norma estrangeira é referência, não obrigação.** IDEA (IEP), Section 508, EN 301 549 e a definição legal norte-americana de UDL entram como referência de desenho. A obrigação brasileira está em `acs.br.*`.
- **Rascunho e nota não são norma.** WCAG 3, WAI-ARIA 1.3 e Core-AAM 1.2 são rascunhos; COGA, WCAG-EM 2.0 e o APG são orientação do W3C, não critério de conformidade. Os documentos dizem o status de cada um com data.
- **Leitura parcial é declarada.** Normas ISO e ABNT foram lidas, em geral, só por metadados ou amostra; vários artigos, só pelo resumo. A tabela de fontes de cada documento marca `[metadados]` ou "(resumo)", e a seção "Lacunas" diz o que não foi lido.
- **Fonte de fornecedor é marcada.** CAST, XAG, documentação de plataformas e licenças de símbolos são fontes de fornecedor; o texto diz isso quando relevante.
- **Recomendação de desenho não é fato.** Limiares de alvo e tempo nos exemplos, regras de decisão de perfil e indicadores propostos são marcados `[I]` ou `[H]`.
