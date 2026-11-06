# Ficha: LDB – Lei de Diretrizes e Bases da Educação Nacional (organização)

Escopo desta ficha: **organização** (níveis, etapas, modalidades, formas de organização, carga, dias letivos, frequência, classificação/reclassificação, sistemas de ensino). Currículo (art. 26 e seguintes) e educação especial (arts. 58–60) ficam com a frente de currículo/inclusão; aqui só aparecem como restrição de modelo.

```yaml
id: br.lei.ldb
name: Lei de Diretrizes e Bases da Educação Nacional
acronym: LDB
jurisdiction: Brasil (federal)
issuing_organization: Congresso Nacional / Presidência da República
reference_type: lei ordinária
domain: [D1, D4, D7]
official_url: https://www.planalto.gov.br/ccivil_03/leis/l9394.htm
repository_url: not_applicable
version: "Lei 9.394/1996, texto compilado do Planalto consultado em 2026-11-05 (alteração mais recente vista: Lei 15.468/2026)"
publication_date: 1996-12-23
last_updated: "2026 (Leis 15.326/2026, 15.462/2026 e 15.468/2026 aparecem no compilado)"
legal_status: lei federal vigente
mandatory_scope: todos os sistemas de ensino (federal, estaduais, DF, municipais) e instituições públicas e privadas
education_levels: [educação infantil, ensino fundamental, ensino médio, EJA, educação profissional, educação especial, educação superior]
geographic_scope: nacional
language: pt-BR
license: domínio público (texto legal)
technical_formats: [HTML]
api_available: não
data_model_available: não (normativo)
ontology_available: não
schemas_available: não
implementation_examples: not_applicable
related_standards: [br.inep.censo-escolar, br.mec.cmdeb, br.lc220-sne]
entities: [Sistema de ensino, Nível, Etapa, Modalidade, Escola, Turma/classe, Profissional da educação]
relationships: "sistema → instituições; nível → etapas; etapa → forma de organização"
vocabularies: [níveis e etapas, formas de organização do art. 23]
core_relevance: alta (fixa as formas de organização que o Core deve admitir sem presumir série anual)
regional_adapter_relevance: alta (regras de validação: carga, dias, frequência)
limitations: "o texto foi lido por ferramenta que devolveu paráfrase; o download direto falhou; conferir redação literal antes de citar"
open_questions: [Q-09]
sources: [E20]
access_date: 2026-11-05
research_status: parcial (artigos de organização verificados em paráfrase)
```

## Pontos de organização (paráfrase do compilado, E20)

| Tema | Artigo | Conteúdo |
|---|---|---|
| Obrigatoriedade | 4º I–II | EB obrigatória e gratuita dos 4 aos 17 anos (pré-escola, EF, EM); EI gratuita até 5 anos |
| Regime de colaboração | 8º | União, estados, DF e municípios organizam seus sistemas em colaboração; União coordena a política nacional |
| Avaliação nacional | 9º VI | União assegura avaliação nacional do rendimento escolar no EF, EM e superior |
| Competências | 10, 11 | Estados: assegurar EF e oferecer com prioridade o EM; baixar normas complementares. Municípios: oferecer EI e, com prioridade, EF; outros níveis só com necessidades atendidas |
| Sistemas | 16, 17, 18 | Federal (instituições federais, IES privadas, órgãos federais); estaduais/DF (instituições estaduais, IES municipais, **escolas privadas de EF e EM**, órgãos estaduais; no DF também EI privada); municipais (instituições municipais de EF, EM e EI, **EI privada**, órgãos municipais) |
| Níveis | 21 | Educação básica (EI, EF, EM) e educação superior |
| Formas de organização | 23 caput | séries anuais, períodos semestrais, ciclos, alternância regular de períodos de estudos, grupos não seriados com base na idade, competência ou outros critérios, ou forma diversa, quando o interesse do processo de aprendizagem recomendar |
| Reclassificação | 23 §1 | a escola pode reclassificar alunos, inclusive transferidos do país ou do exterior, com base em normas curriculares gerais |
| Calendário | 23 §2 | adequado às peculiaridades locais, inclusive climáticas e econômicas, sem reduzir a carga horária legal |
| Carga e dias | 24 I | ≥ 800 h/ano no EF e ≥ 1.000 h/ano no EM, em ≥ 200 dias de efetivo trabalho escolar, excluído o tempo de exames finais |
| Classificação | 24 II | em qualquer série/etapa (exceto 1º ano do EF): por promoção, por transferência, ou por avaliação da escola independentemente de escolarização anterior |
| Progressão parcial | 24 III | admitida nos estabelecimentos com progressão regular por série |
| Classes de alunos de séries distintas | 24 IV | para línguas, artes ou outros componentes, com níveis equivalentes de adiantamento |
| Avaliação e recuperação | 24 V | contínua e cumulativa; aceleração; avanço mediante verificação; aproveitamento de estudos; recuperação |
| Frequência | 24 VI | controle pela escola; mínimo de **75%** do total de horas letivas para aprovação |
| Documentos | 24 VII | escola expede históricos, declarações de conclusão de série e diplomas ou certificados |
| EI | 29, 30, 31 | até 5 anos; creche até 3, pré-escola 4–5; avaliação por acompanhamento sem promoção; ≥ 800 h em ≥ 200 dias; ≥ 4 h (parcial) ou 7 h (integral); frequência mínima de 60%; documentação do desenvolvimento |
| EF | 32, 34 | obrigatório, início aos 6 anos, ≥ 9 anos; jornada ≥ 4 h de trabalho efetivo em sala, ampliada progressivamente |
| EM | 35 | ≥ 3 anos |
| EJA | 37, 38 | para quem não teve acesso ou continuidade; cursos e exames supletivos (EF > 15 anos; EM > 18 anos) |
| Educação especial | 58, 59, 59-A, 60 | modalidade, preferencialmente na rede regular, da EI ao longo da vida; cadastro nacional de alunos com AH/SD (59-A) |
| Profissionais | 61, 67 | categorias I–V de profissionais da EB; valorização (ingresso por concurso público, piso, carreira) |

Não localizado na LDB (E20): dispositivo sobre identificador do estudante ou "Sistema Nacional de Educação" (a matéria está na LC 220/2025, ver [educadados.md](educadados.md)).

## Implicações para o Core [I]

- `C.PRG` não pode presumir "série anual": o art. 23 admite seis formas, e o Censo/CMDEB codificam cinco (+ alternância como marcador). `C.GRP` precisa de `kind` (turma acadêmica, grupo não seriado, módulo, AEE, atividade complementar).
- `C.SES` é por sistema/escola (art. 23 §2), não nacional; a única data nacional é a de referência do Censo.
- Regras de aprovação (75% de frequência; EI sem promoção; progressão parcial) são regras do adaptador, não do Core.
