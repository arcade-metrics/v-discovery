---
id: acs.brief
titulo: Brief do domínio acessibilidade, educação especial e Desenho Universal para a Aprendizagem
tipo: relatorio
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: acessibilidade, educação especial e Desenho Universal para a Aprendizagem

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Como tornar ambientes digitais de aprendizagem utilizáveis e participáveis por toda a variabilidade de aprendizes, com atenção a pessoas com deficiência e público da educação especial. Inclui: Desenho Universal para a Aprendizagem (DUA/UDL), suas diretrizes, a evidência disponível e a relação com diferenciação pedagógica e adaptação individual; normas de acessibilidade digital (WCAG, WAI-ARIA, ISO/IEC 24751 AccessForAll, normas de compra pública como EN 301 549 e Section 508) e diretrizes específicas de acessibilidade em jogos; tecnologias assistivas (conceito e classificação, leitores de tela e APIs de acessibilidade das plataformas, acesso alternativo por acionadores, varredura e rastreamento ocular, comunicação aumentativa e alternativa); acessibilidade cognitiva, sensorial (visual e auditiva) e motora, incluindo linguagem simples e leitura fácil; adaptações de interface e de atividade (personalização por preferência declarada, acomodação versus modificação, adaptação de mecânicas e tempos em atividades lúdicas); participação, autonomia e desenho inclusivo (modelos de deficiência, desenho inclusivo, design participativo com pessoas com deficiência, autodeterminação); avaliação de barreiras e de necessidades de suporte (avaliação de conformidade, testes com usuários de tecnologia assistiva, instrumentos de barreira ambiental e de intensidade de suporte, plano educacional individualizado e plano de AEE); marco brasileiro (LBI, política de educação especial na perspectiva inclusiva, AEE, eMAG, ABNT NBR 17225, Libras). Para cada norma, técnica ou instrumento: o que é, quem mantém, versão vigente, que barreira enfrenta, evidência disponível e limites.

Fora do escopo: a CIF como padrão de codificação e intercâmbio com sistemas de saúde (fica em `interoperabilidade`, `iop.health.cif`; aqui a CIF entra só como modelo conceitual de funcionalidade, barreira e facilitador); modelos de aluno e adaptação algorítmica em si (ficam em `aprendizagem-adaptativa`, aqui entra apenas o que a adaptação precisa respeitar para ser acessível e preservar autonomia); mecânicas de jogo, dificuldade dinâmica e evidência de eficácia de jogos em educação especial (ficam em `gamificacao-e-jogos`, aqui entra a acessibilidade da interação e das mecânicas); LGPD e tratamento de dado sensível de saúde e deficiência (fica em `privacidade-seguranca-e-governanca`); psicometria e validação de instrumentos de desempenho (fica em `learning-analytics-e-avaliacao`); práticas de ensino baseadas em evidência por população (instrução explícita, práticas para TEA, TDAH e deficiência intelectual) e padrões de evidência em educação especial, como os do CEC (ficam em `fundamentos-pedagogicos`); diagnóstico clínico.

Fronteira com `fundamentos-pedagogicos/inclusive-teaching/`, que também lista DUA, tecnologia assistiva e legislação brasileira: este domínio é a fonte das definições, diretrizes, normas e do marco legal; aquele trata o uso pedagógico e a evidência de eficácia em sala, citando ids `acs.*` em vez de redefinir os conceitos. A divisão precisa ser confirmada entre os dois briefs antes da pesquisa.

## Estrutura sugerida

- `foundations/`: modelos de deficiência (médico, social, biopsicossocial, direitos humanos), barreira e acessibilidade, adaptação razoável, desenho universal.
- `udl/`: DUA/UDL e diretrizes do CAST, evidência empírica, comparação com diferenciação e adaptação individual, aplicação a ambientes digitais.
- `standards/`: WCAG 2.2 e estado do WCAG 3, WAI-ARIA e Authoring Practices, ISO/IEC 24751 e AccessForAll, EN 301 549 e Section 508, diretrizes de acessibilidade em jogos, comparação.
- `assistive-tech/`: conceito e classificação (ISO 9999), leitores de tela e APIs de acessibilidade, acesso alternativo, comunicação aumentativa e alternativa, baixa visão e braile.
- `access-dimensions/`: acessibilidade cognitiva e de aprendizagem, linguagem simples e leitura fácil, visual, auditiva (legendas, audiodescrição, línguas de sinais), motora.
- `adaptation/`: personalização de interface e perfis de preferência, acomodação versus modificação, adaptação de atividades e jogos, adaptatividade algorítmica e autonomia.
- `participation/`: desenho inclusivo, design participativo, autonomia e autodeterminação, participação como construto.
- `assessment/`: avaliação de conformidade (WCAG-EM, ACT Rules, limites das ferramentas automáticas), testes com usuários, avaliação de barreiras, necessidades de suporte, PEI e plano de AEE.
- `brazil/`: LBI, PNEEPEI e AEE, eMAG e ABNT NBR 17225, Libras.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. CAST, UDL Guidelines 3.0 (2024); Meyer, Rose e Gordon, "Universal Design for Learning: Theory and Practice"; revisões sistemáticas e metanálises sobre UDL (ex.: Capp, 2017; Al-Azawei, Serenelli e Lundqvist, 2016; King-Sears et al., 2023).
2. W3C/WAI: WCAG 2.2, rascunho de WCAG 3, WAI-ARIA 1.2 e ARIA Authoring Practices Guide, WCAG-EM, ACT Rules, "Making Content Usable for People with Cognitive and Learning Disabilities" (COGA).
3. ISO/IEC 24751 e 1EdTech AccessForAll; ISO 9999 (classificação de produtos assistivos); ISO 24495-1 (linguagem simples); Inclusion Europe, padrões de leitura fácil.
4. ETSI EN 301 549; US Section 508 (Revised 508 Standards).
5. ONU, Convenção sobre os Direitos das Pessoas com Deficiência (2006) e Comentário Geral nº 4 (educação inclusiva); OMS, CIF.
6. Game Accessibility Guidelines; Microsoft Xbox Accessibility Guidelines; AbleGamers, Accessible Player Experiences.
7. Inclusive Design Research Centre (OCAD); Microsoft Inclusive Design; literatura sobre design participativo e co-design com pessoas com deficiência.
8. AAIDD, Supports Intensity Scale e paradigma de suportes; Wehmeyer, autodeterminação; Imms et al., família de construtos relacionados à participação (fPRC); Booth e Ainscow, Index for Inclusion.
9. Brasil: Lei 13.146/2015 (LBI); PNEEPEI, 2008; Decreto 7.611/2011 (AEE); Lei 10.436/2002 e Decreto 5.626/2005 (Libras); eMAG 3.1; ABNT NBR 17225; Comitê de Ajudas Técnicas (CAT/SDH) sobre tecnologia assistiva; status do Decreto 10.502/2020.

## Perguntas abertas

- Que parte do DUA tem evidência experimental sobre aprendizagem e que parte é prescrição de desenho ainda sem teste?
- Onde a conformidade com WCAG deixa de garantir acesso, sobretudo para barreiras cognitivas, e o que preenche essa lacuna?
- Como representar preferências e necessidades de acesso de forma portável entre sistemas, e quem deve declarar esse perfil?
- Quando adaptar automaticamente ajuda e quando retira da pessoa a escolha sobre como aprender?
- Que mecânicas e tempos de jogo são barreiras para acionadores, varredura ou rastreamento ocular, e como compensar sem descaracterizar a atividade?
- Como avaliar barreiras e necessidades de suporte sem reduzir a pessoa a um diagnóstico?
- Quais requisitos legais e normativos brasileiros são obrigatórios para plataformas educacionais digitais, e quais são apenas recomendados?
