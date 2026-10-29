---
id: ped.brief
titulo: Brief do domínio fundamentos pedagógicos e evidências científicas
tipo: relatorio
dominio: fundamentos-pedagogicos
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: fundamentos pedagógicos e evidências científicas

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Base pedagógica e critérios de evidência que justificam o que uma tecnologia educacional ensina, como ensina e como se prova que funciona. Inclui: teorias de aprendizagem (behaviorismo, cognitivismo, construtivismo e socioconstrutivismo, conectivismo como proposta contestada) e o que cada uma prevê de verificável; desenho instrucional (modelos de processo como ADDIE, princípios de Gagné e Merrill, teoria da carga cognitiva, aprendizagem multimídia, 4C/ID); ciência da aprendizagem (memória, prática de recuperação, espaçamento, intercalação, exemplos resolvidos, transferência, metacognição, e o que distingue achado de laboratório de achado em sala); estratégias de ensino inclusivo (Desenho Universal para a Aprendizagem, instrução explícita, práticas baseadas em evidência para TEA, TDAH e deficiência intelectual, tecnologia assistiva, marco legal brasileiro da educação inclusiva); revisões sistemáticas e metanálises (protocolos, PRISMA, avaliação de risco de viés, heterogeneidade, viés de publicação, interpretação de tamanho de efeito em educação, críticas a sínteses de segunda ordem); hierarquias e padrões de evidência para intervenções educacionais (What Works Clearinghouse, níveis da ESSA, EEF, padrões do CEC para educação especial, desenhos de caso único); validação científica de tecnologias educacionais (do princípio pedagógico ao estudo de eficácia, fidelidade de implementação, certificações e selos de evidência, o caso das terapias digitais com aprovação regulatória).

Fora do escopo: mecânica do desenho experimental e quase-experimental aplicado a dados do produto (fica em `learning-analytics-e-avaliacao/evaluation-methods`, aqui entram os padrões de evidência que esse desenho precisa atender); KLI, componentes de conhecimento e algoritmos de repetição espaçada (ficam em `aprendizagem-adaptativa/instructional-design` e `aprendizagem-adaptativa/spaced-repetition`, aqui entra o achado da ciência da aprendizagem que os sustenta); motivação, flow e metanálises específicas de jogos (ficam em `gamificacao-e-jogos`); evidências de plataformas concretas (ficam em `lms-e-plataformas`); ética em pesquisa com menores (fica em `dados-pesquisa-e-eventos`).

## Estrutura sugerida

- `learning-theories/`: teorias de aprendizagem, previsões testáveis, mal-entendidos comuns (estilos de aprendizagem, pirâmide de aprendizagem).
- `instructional-design/`: modelos de processo, princípios de instrução, carga cognitiva, multimídia, 4C/ID, alinhamento entre objetivo, atividade e avaliação.
- `learning-sciences/`: estratégias de estudo com evidência, memória e esquecimento, transferência, metacognição, validade ecológica.
- `inclusive-teaching/`: DUA, instrução explícita, práticas baseadas em evidência por população, tecnologia assistiva, legislação brasileira.
- `evidence-synthesis/`: revisões sistemáticas, metanálises, PRISMA, risco de viés, tamanho de efeito em educação, críticas a Hattie e a sínteses de sínteses.
- `evidence-standards/`: WWC, ESSA, EEF, padrões do CEC, desenhos de caso único, fidelidade de implementação.
- `edtech-validation/`: da teoria ao estudo de eficácia, ciclos de validação de produto, selos e certificações, terapias digitais.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. Ertmer e Newby, 1993, comparação entre behaviorismo, cognitivismo e construtivismo; Illeris (org.), "Contemporary Theories of Learning"; Vygotsky, zona de desenvolvimento proximal.
2. Gagné et al., "Principles of Instructional Design"; Merrill, 2002, "First Principles of Instruction"; Sweller, teoria da carga cognitiva; Mayer, "Multimedia Learning"; van Merriënboer e Kirschner, "Ten Steps to Complex Learning".
3. National Research Council, "How People Learn" (2000) e National Academies, "How People Learn II" (2018); Sawyer (org.), "The Cambridge Handbook of the Learning Sciences"; Dunlosky et al., 2013, técnicas de estudo; Pashler et al., 2008, sobre estilos de aprendizagem.
4. CAST, diretrizes do Desenho Universal para a Aprendizagem (versão vigente); Archer e Hughes, "Explicit Instruction"; Steinbrenner et al., 2020 (NCAEP), práticas baseadas em evidência para TEA; Lei 13.146/2015 (Lei Brasileira de Inclusão) e Política Nacional de Educação Especial na Perspectiva da Educação Inclusiva (2008).
5. Higgins et al., "Cochrane Handbook for Systematic Reviews of Interventions"; Page et al., 2021, PRISMA 2020; Borenstein et al., "Introduction to Meta-Analysis"; Cheung e Slavin, 2016, efeito de características metodológicas sobre tamanho de efeito; Kraft, 2020, interpretação de tamanho de efeito em educação; Hattie, "Visible Learning", e críticas (ex.: Bergeron e Rivard, 2017).
6. What Works Clearinghouse, "Procedures and Standards Handbook" (versão vigente); níveis de evidência da ESSA; Education Endowment Foundation, padrões de avaliação; Cook et al., 2014, padrões do CEC para práticas baseadas em evidência; Horner et al., 2005, e Kratochwill et al., desenhos de caso único; Carroll et al., 2007, fidelidade de implementação.
7. Hirsh-Pasek et al., 2015, "Putting Education in 'Educational' Apps"; revisões sobre eficácia de apps educacionais infantis; documentação de selos de evidência (ex.: Digital Promise, ESSA Evidence) e de terapias digitais com aprovação regulatória, a localizar na pesquisa.

## Perguntas abertas

- Que teorias de aprendizagem fazem previsões que um produto digital consegue testar, e quais são só enquadramento?
- Quais achados da ciência da aprendizagem se replicam com crianças com TEA, TDAH ou deficiência intelectual, e quais foram medidos só com universitários típicos?
- Como aplicar o DUA sem que vire checklist genérico de acessibilidade?
- Que tamanho de efeito é realista esperar de uma intervenção digital em educação especial, e contra qual linha de base?
- Desenhos de caso único bastam para afirmar eficácia em populações pequenas e heterogêneas, ou são só o ponto de partida?
- Qual o caminho mínimo de validação que um produto pode percorrer antes de afirmar que é "baseado em evidência"?
- Que padrão de evidência (WWC, ESSA, EEF, CEC) faz sentido adotar no Brasil, onde não há equivalente oficial?
