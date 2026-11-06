# VUOO International Education Standards Research

**Pasta:** `base/` de `produtos/vuoo-microjogos/`

**Estrutura:** convenções de entrega em [_convencoes.md](_convencoes.md);
o que já existia no repositório em
[inventario-existente.md](inventario-existente.md); uma pasta por
jurisdição ([brasil/](camada-brasil/README-estudo-brasil.md) ativo,
[estados-unidos/](fora-da-fase-1/estados-unidos/README.md),
[uniao-europeia/](fora-da-fase-1/uniao-europeia/README.md),
[reino-unido/](fora-da-fase-1/reino-unido/README.md) e [china/](fora-da-fase-1/china/README.md) em
standby), [internacional/](camada-agnostica/internacional/README.md) para os padrões
transversais e [core/](camada-agnostica/core-v0.1.md) para a síntese do Core agnóstico.
Relatório de infraestrutura: [relatorio-infra-vuoo.md](relatorio-infra-vuoo.md).

**Objetivo:** orientar agentes de pesquisa na identificação, análise e
organização de padrões, normas, frameworks, modelos de dados e
referenciais educacionais que fundamentem a arquitetura agnóstica da
VUOO e seus adaptadores regionais.

**Status:** documento inicial de pesquisa. As referências abaixo são
pontos de partida, não uma lista validada ou exaustiva. Os agentes devem
confirmar existência, versão vigente, escopo, autoridade emissora,
licenciamento e documentação oficial antes de consolidar qualquer
conclusão.

------------------------------------------------------------------------

## 1. Objetivo geral

Investigar como diferentes países e regiões representam e intercambiam
informações sobre:

-   organização institucional e acadêmica;
-   estudantes, professores e demais profissionais;
-   matrículas, turmas, disciplinas e componentes curriculares;
-   anos letivos, períodos, calendários, horários e espaços;
-   currículos, competências, habilidades e objetivos de aprendizagem;
-   conhecimentos, progressão e trajetórias individuais;
-   atividades, experiências de aprendizagem, avaliações e resultados;
-   inclusão, acessibilidade e adaptações;
-   identidade, segurança, privacidade e governança de dados;
-   interoperabilidade entre sistemas de gestão acadêmica, LMS e
    plataformas educacionais.

O resultado esperado é uma base de referência que permita especificar um
**VUOO Agnostic Core**, acompanhado de módulos regionais e mecanismos de
mapeamento.

## 2. Princípio arquitetural da VUOO

A arquitetura deverá separar dois níveis.

### 2.1 Core agnóstico

O núcleo define conceitos, entidades, relações e serviços que não
dependem de um país, currículo ou fornecedor específico.

Áreas conceituais iniciais:

1.  **Academic Organization Model:** organizações, unidades,
    calendários, anos letivos, cursos, etapas, turmas, grupos,
    matrículas, profissionais, disciplinas, horários e espaços.
2.  **Learning Model:** objetivos, competências, habilidades,
    conhecimentos, resultados e progressão.
3.  **Learner Model:** perfil educacional, conhecimentos demonstrados,
    evolução, necessidades e preferências relevantes para a
    aprendizagem.
4.  **Curriculum Model:** estruturas curriculares, componentes,
    referenciais, versões e relações entre objetivos e conteúdos.
5.  **Assessment Model:** instrumentos, itens, avaliações, rubricas,
    evidências e resultados.
6.  **Learning Experience Model:** atividades, aulas, jogos,
    intervenções, percursos e adaptações.
7.  **Inclusion & Accessibility Model:** acessibilidade, participação,
    barreiras, recursos de apoio e adaptações.
8.  **Interoperability & Governance Model:** identificadores,
    vocabulários, APIs, proveniência, consentimento, segurança e
    políticas de dados.

### 2.2 Adaptadores regionais

Cada módulo regional representa normas, estruturas e vocabulários de uma
jurisdição e mapeia seus conceitos para o Core.

Regiões iniciais:

-   Brasil;
-   União Europeia;
-   China;
-   Reino Unido;
-   Estados Unidos.

O Core não deve incorporar regras exclusivas de uma região. Os
adaptadores devem preservar os conceitos locais e explicitar perdas,
equivalências aproximadas ou incompatibilidades no mapeamento.

### 2.3 Princípio de independência

A organização acadêmica deve ser independente da organização das
experiências de aprendizagem. Um estudante pode estar matriculado em uma
turma e, simultaneamente, participar de grupos temporários, atividades
interturmas, atendimentos individualizados, jogos, intervenções e
percursos adaptativos.

Também devem ser diferenciados:

-   **Turma:** agrupamento acadêmico ou administrativo de estudantes.
-   **Disciplina/componente curricular:** área ou unidade curricular.
-   **Oferta de componente / classe de ensino:** realização de um
    componente para determinado grupo, período e contexto, com
    profissionais, horários e espaços associados.
-   **Grupo de aprendizagem:** agrupamento flexível, que pode ser
    temporário e atravessar turmas.
-   **Matrícula:** vínculo do estudante com uma organização, curso,
    etapa, turma ou oferta, conforme o contexto e o período de validade.

------------------------------------------------------------------------

## 3. Escopo geográfico e referências iniciais

As referências abaixo são candidatas para investigação. Não presumir que
todas sejam normas obrigatórias, que tenham o mesmo escopo ou que sejam
diretamente equivalentes.

### 3.1 Brasil

Investigar especialmente:

  -----------------------------------------------------------------------
  Referência                          Tema a investigar
  ----------------------------------- -----------------------------------
  BNCC                                Competências gerais, competências
                                      específicas, habilidades e objetos
                                      de conhecimento

  BNCC Computação                     Complemento curricular relativo à
                                      computação

  LDB                                 Organização nacional da educação

  Diretrizes Curriculares Nacionais   Diretrizes por etapa, modalidade e
  (DCNs)                              área

  EducaDados e atos normativos        Modelos informacionais,
  associados                          interoperabilidade, segurança e
                                      intercâmbio

  Conjunto Mínimo de Dados da         Dados mínimos e definições
  Educação Básica (CMDEB)             aplicáveis à educação básica

  MEC Gestão Presente                 Iniciativas de integração e gestão
                                      de dados educacionais

  Educacenso / Censo Escolar          Cadastro e coleta de dados de
                                      escolas, turmas, alunos e
                                      profissionais

  SAEB                                Avaliação da educação básica

  SINAES                              Avaliação da educação superior

  Catálogos e referenciais do INEP    Indicadores, conceitos e
                                      classificações educacionais
  -----------------------------------------------------------------------

Fontes iniciais:

-   https://basenacionalcomum.mec.gov.br/
-   https://www.planalto.gov.br/ccivil_03/leis/l9394.htm
-   https://www.gov.br/mec/
-   https://www.gov.br/inep/
-   https://mecnormas.mec.gov.br/
-   https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar

**Questões específicas:**

-   Quais dados são obrigatórios no Censo Escolar?
-   Quais identificadores são utilizados para estudantes, profissionais,
    escolas, turmas e cursos?
-   Quais são as definições oficiais de turma, etapa, modalidade,
    matrícula e situação do estudante?
-   Quais especificações técnicas de EducaDados estão publicadas e em
    vigor?
-   Como são representados calendário, período letivo, horário,
    componentes curriculares e atendimento educacional especializado?
-   Como representar redes, mantenedoras, escolas e unidades
    administrativas?
-   Quais regras variam por estado, município, rede ou etapa de ensino?

### 3.2 União Europeia

A União Europeia não deve ser tratada como um sistema escolar único.
Investigar os modelos europeus comuns e, separadamente, as diferenças
nacionais quando relevantes.

  -----------------------------------------------------------------------
  Referência                          Tema a investigar
  ----------------------------------- -----------------------------------
  European Learning Model (ELM)       Modelo semântico de aprendizagem,
                                      qualificações e credenciais

  European Qualifications Framework   Níveis de qualificações
  (EQF)                               

  ESCO                                Competências, habilidades,
                                      qualificações e ocupações

  DigComp                             Competência digital

  DigCompEdu                          Competência digital de educadores

  LifeComp                            Competências pessoais, sociais e de
                                      aprender a aprender

  GreenComp                           Competências para sustentabilidade

  Europass                            Perfil, histórico e credenciais de
                                      aprendizagem

  ECTS                                Créditos e mobilidade no ensino
                                      superior

  European Higher Education           Interoperabilidade no ensino
  Interoperability Framework          superior
  -----------------------------------------------------------------------

Fontes iniciais:

-   https://github.com/european-commission-empl/European-Learning-Model
-   https://europa.eu/europass/
-   https://europa.eu/europass/en/european-qualifications-framework-eqf
-   https://esco.ec.europa.eu/
-   https://joint-research-centre.ec.europa.eu/digcomp_en
-   https://joint-research-centre.ec.europa.eu/digcompedu_en
-   https://education.ec.europa.eu/

**Questões específicas:**

-   Quais entidades e relações o ELM efetivamente modela?
-   O ELM representa organização acadêmica e gestão de turmas ou
    concentra-se em aprendizagem, qualificações e credenciais?
-   Quais vocabulários e identificadores são reutilizáveis?
-   Como o EQF se relaciona com qualificações nacionais?
-   Quais dados são compartilhados entre países e quais permanecem sob
    competência nacional?
-   Quais padrões se aplicam à educação básica, profissional e superior?

### 3.3 China

Investigar os padrões nacionais de informatização educacional, as normas
técnicas publicadas pelo Ministério da Educação e os padrões nacionais
GB/T. Confirmar sempre a versão e o texto oficial.

  -----------------------------------------------------------------------
  Referência candidata                Tema a investigar
  ----------------------------------- -----------------------------------
  JY/T 0633-2022                      Investigar escopo e modelo de dados
                                      educacionais básicos

  JY/T 0637—2022 (corrigido; ver nota) Dados básicos de pessoal
                                      educacional

  JY/T 0639—2022 (corrigido; ver nota) Dados básicos de escolas de
                                      educação básica

  National Smart Education Platform   Plataforma nacional de serviços e
                                      recursos educacionais

  Education Informatization Standards Normas de informatização
                                      educacional

  GB/T                                Normas nacionais chinesas
                                      potencialmente aplicáveis

  Personal Information Protection Law Proteção de informações pessoais
  (PIPL)                              

  Data Security Law                   Segurança e governança de dados
  -----------------------------------------------------------------------

Fontes iniciais:

-   https://www.moe.gov.cn/
-   https://www.smartedu.cn/
-   https://openstd.samr.gov.cn/
-   https://www.npc.gov.cn/

**Nota de 2026-11-05:** no registro oficial da SAMR, os números JY/T
0634-2022 e JY/T 0635-2022 pertencem a outros setores. Os temas pedidos
estão em JY/T 0637—2022 (pessoal) e JY/T 0639—2022 (escolas de educação
básica). Detalhes em [china/](fora-da-fase-1/china/README.md).

**Questões específicas:**

-   Obter os textos oficiais e confirmar títulos, escopo e vigência das
    normas JY/T citadas.
-   Identificar os modelos de dados para escolas, estudantes,
    profissionais, turmas e atividades.
-   Investigar identificadores nacionais e regras de compartilhamento.
-   Identificar normas para plataformas, recursos digitais, segurança e
    classificação de dados.
-   Verificar requisitos de localização, transferência internacional e
    tratamento de dados pessoais.

### 3.4 Reino Unido

O Reino Unido contém sistemas educacionais distintos. A pesquisa deve
separar, no mínimo, Inglaterra, Escócia, País de Gales e Irlanda do
Norte. Não generalizar regras da Inglaterra para todo o Reino Unido.

  -----------------------------------------------------------------------
  Referência                          Tema a investigar
  ----------------------------------- -----------------------------------
  Common Basic Data Set (CBDS)        Definições e dados escolares comuns

  Department for Education (DfE) Data Padrões de dados educacionais
  Standards                           

  School Census                       Dados e regras de coleta escolar na
                                      Inglaterra

  National Curriculum                 Currículo da Inglaterra

  Curriculum for Wales                Currículo do País de Gales

  Curriculum for Excellence           Currículo da Escócia

  Northern Ireland Curriculum         Currículo da Irlanda do Norte

  UK GDPR e Data Protection Act 2018  Proteção de dados
  -----------------------------------------------------------------------

Fontes iniciais:

-   https://www.gov.uk/government/collections/common-basic-data-set
-   https://standards.education.gov.uk/
-   https://www.gov.uk/government/collections/national-curriculum
-   https://hwb.gov.wales/curriculum-for-wales/
-   https://education.gov.scot/
-   https://www.education-ni.gov.uk/
-   https://ico.org.uk/

**Questões específicas:**

-   Quais dados e códigos compõem o CBDS?
-   Como os sistemas representam escolas, estabelecimentos, estudantes,
    turmas, matrículas e profissionais?
-   Quais padrões são obrigatórios para fornecedores que integram
    sistemas com o DfE?
-   Quais diferenças existem entre as quatro jurisdições?
-   Como são representados os currículos e resultados de aprendizagem?

### 3.5 Estados Unidos

Investigar padrões nacionais, iniciativas estaduais e padrões de
organizações de interoperabilidade. Não presumir que um padrão seja
obrigatório em todos os estados.

  -----------------------------------------------------------------------
  Referência                          Tema a investigar
  ----------------------------------- -----------------------------------
  Ed-Fi Data Standard                 Modelo de dados operacionais e
                                      acadêmicos

  Common Education Data Standards     Definições e elementos comuns de
  (CEDS)                              dados

  OneRoster                           Intercâmbio de usuários, turmas,
                                      cursos e matrículas

  Edu-API                             Interoperabilidade de dados
                                      acadêmicos, especialmente no ensino
                                      superior

  CASE                                Intercâmbio de competências e
                                      padrões educacionais

  Learning Tools Interoperability     Integração de ferramentas e
  (LTI)                               plataformas

  Caliper Analytics                   Eventos e métricas de aprendizagem

  Question and Test Interoperability  Questões e avaliações
  (QTI)                               

  Common Cartridge                    Intercâmbio de conteúdos e cursos

  Comprehensive Learner Record (CLR)  Registros de conquistas e
                                      competências

  Open Badges                         Credenciais digitais

  Common Core State Standards         Referenciais curriculares adotados
                                      por estados

  Next Generation Science Standards   Padrões de aprendizagem em ciências
  (NGSS)                              

  FERPA                               Privacidade de registros
                                      educacionais
  -----------------------------------------------------------------------

Fontes iniciais:

-   https://docs.ed-fi.org/
-   https://ceds.ed.gov/
-   https://www.1edtech.org/standards/oneroster
-   https://www.1edtech.org/standards/edu-api
-   https://www.1edtech.org/standards/case
-   https://www.1edtech.org/standards/lti
-   https://www.1edtech.org/standards/caliper
-   https://www.1edtech.org/standards/qti
-   https://www.1edtech.org/standards/common-cartridge
-   https://www.1edtech.org/standards/comprehensive-learner-record
-   https://www.1edtech.org/standards/open-badges
-   https://www.thecorestandards.org/
-   https://www.nextgenscience.org/
-   https://studentprivacy.ed.gov/

**Questões específicas:**

-   Quais entidades compõem o modelo Ed-Fi e como se relacionam?
-   Quais elementos do CEDS são definições, modelos ou vocabulários?
-   Quais operações e recursos são cobertos pelo OneRoster?
-   Quais diferenças existem entre OneRoster, Edu-API e Ed-Fi?
-   Como CASE representa objetivos, competências e associações
    curriculares?
-   Como Caliper representa eventos e atividades de aprendizagem?
-   Quais dados são controlados por estados, distritos e instituições?

------------------------------------------------------------------------

## 4. Padrões internacionais transversais

Investigar padrões que possam sustentar o Core sem vinculação a uma
jurisdição.

  Referência                   Tema
  ---------------------------- -----------------------------------------------------
  UNESCO ISCED                 Classificação internacional dos níveis educacionais
  UNESCO ISCED-F               Classificação das áreas de educação e formação
  ISO 21001                    Sistemas de gestão para organizações educacionais
  ISO 29993                    Serviços de aprendizagem fora da educação formal
  IEEE LOM                     Metadados de objetos de aprendizagem
  W3C RDF                      Modelo de representação de dados em grafo
  W3C OWL                      Representação de ontologias
  W3C SKOS                     Vocabulários, conceitos e taxonomias
  W3C JSON-LD                  Dados ligados em formato JSON
  W3C Verifiable Credentials   Credenciais verificáveis
  CAST UDL Guidelines          Desenho Universal para Aprendizagem
  WCAG 2.2                     Acessibilidade de conteúdo e interfaces digitais

Fontes iniciais:

-   https://uis.unesco.org/en/topic/international-standard-classification-education-isced
-   https://www.iso.org/standard/66266.html
-   https://www.iso.org/
-   https://standards.ieee.org/ieee/1484.12.1/10385/
-   https://www.w3.org/RDF/
-   https://www.w3.org/OWL/
-   https://www.w3.org/2004/02/skos/
-   https://www.w3.org/TR/json-ld11/
-   https://www.w3.org/TR/vc-data-model-2.0/
-   https://udlguidelines.cast.org/
-   https://www.w3.org/TR/WCAG22/

------------------------------------------------------------------------

## 5. Domínios de pesquisa

Todos os agentes devem classificar os achados em um ou mais dos domínios
abaixo.

### D1. Academic Organization

-   organização, mantenedora, rede e unidade;
-   campus, escola, centro e departamento;
-   ano letivo e calendário;
-   período, semestre, trimestre e etapa;
-   curso, programa, série e nível;
-   turma, classe, grupo e seção;
-   estudante, responsável e profissional;
-   matrícula, transferência, trancamento e conclusão;
-   disciplina e componente curricular;
-   oferta de componente, professor e equipe;
-   sala, laboratório, espaço e recurso;
-   horário, grade, sessão e evento acadêmico.

### D2. Learning Model

-   domínio e área de conhecimento;
-   competência, habilidade e capacidade;
-   objetivo e resultado de aprendizagem;
-   conhecimento e conceito;
-   pré-requisito e progressão;
-   nível de domínio;
-   alinhamento entre objetivos e currículo;
-   relações hierárquicas e associações semânticas.

### D3. Learner Model

-   identidade e vínculos educacionais;
-   histórico e trajetória;
-   conhecimentos demonstrados;
-   evidências de aprendizagem;
-   progresso e domínio;
-   preferências relevantes para a experiência;
-   necessidades de apoio e adaptações;
-   participação e engajamento;
-   histórico de intervenções e resultados.

### D4. Curriculum Model

-   estrutura curricular;
-   áreas e componentes;
-   conteúdos e objetos de conhecimento;
-   competências e habilidades;
-   sequência e progressão;
-   versões e vigência;
-   referenciais nacionais, regionais e institucionais;
-   equivalências e mapeamentos entre currículos.

### D5. Assessment Model

-   avaliação diagnóstica, formativa e somativa;
-   instrumento e protocolo;
-   questão, item e tarefa;
-   rubrica e critério;
-   escala e nível de desempenho;
-   resultado, evidência e observação;
-   validade, confiabilidade e limitações;
-   avaliação automatizada e avaliação humana.

### D6. Learning Experience

-   curso, unidade, aula e sessão;
-   atividade, tarefa e projeto;
-   jogo sério e simulação;
-   intervenção e prática;
-   percurso e sequência;
-   adaptação e personalização;
-   recursos educacionais;
-   telemetria e eventos de interação;
-   participação individual e coletiva.

### D7. Inclusion & Accessibility

-   desenho universal para aprendizagem;
-   acessibilidade digital;
-   barreiras à participação;
-   recursos e tecnologias assistivas;
-   adaptações razoáveis;
-   apoios individualizados;
-   participação e funcionalidade;
-   CIF/ICF e classificações relacionadas;
-   representação de necessidades sem reduzir o estudante a
    diagnósticos.

### D8. Interoperability & Governance

-   identificadores e resolução de identidade;
-   APIs e contratos de dados;
-   formatos de intercâmbio;
-   vocabulários e classificações;
-   ontologias e grafos de conhecimento;
-   metadados e proveniência;
-   versionamento e compatibilidade;
-   autenticação e autorização;
-   consentimento e base legal;
-   privacidade, retenção e auditoria;
-   segurança e transferência internacional de dados.

------------------------------------------------------------------------

## 6. Protocolo de pesquisa para os agentes

### 6.1 Regras gerais

1.  Priorizar documentação oficial da entidade responsável pelo padrão.
2.  Consultar especificações técnicas, esquemas, modelos, APIs e
    exemplos de implementação.
3.  Registrar a versão exata consultada e a data de acesso.
4.  Distinguir lei, regulamento, norma técnica, padrão voluntário,
    framework, vocabulário e recomendação.
5.  Não tratar uma iniciativa como obrigatória sem evidência normativa
    explícita.
6.  Não inferir equivalência entre conceitos apenas porque possuem nomes
    semelhantes.
7.  Registrar divergências entre documentação, implementação e prática.
8.  Procurar repositórios oficiais, arquivos XSD/JSON Schema, APIs,
    exemplos e testes de conformidade.
9.  Identificar restrições de licença e uso.
10. Sinalizar documentos desatualizados, links quebrados e fontes
    secundárias.

### 6.2 Ficha obrigatória para cada referência

Cada referência pesquisada deve ter uma ficha contendo:

``` yaml
id:
name:
acronym:
jurisdiction:
issuing_organization:
reference_type:
domain:
official_url:
repository_url:
version:
publication_date:
last_updated:
legal_status:
mandatory_scope:
education_levels:
geographic_scope:
language:
license:
technical_formats:
api_available:
data_model_available:
ontology_available:
schemas_available:
implementation_examples:
related_standards:
entities:
relationships:
vocabularies:
core_relevance:
regional_adapter_relevance:
limitations:
open_questions:
sources:
access_date:
research_status:
```

Usar `unknown` ou `not_found` quando uma informação não estiver
disponível. Não preencher lacunas por inferência.

### 6.3 Análise técnica obrigatória

Para cada padrão que disponibilize modelo de dados, identificar:

-   entidades e atributos;
-   identificadores primários e externos;
-   cardinalidades e relacionamentos;
-   hierarquias;
-   enums, códigos e vocabulários;
-   regras de validação;
-   temporalidade e versionamento;
-   operações de criação, atualização e exclusão;
-   formatos de serialização;
-   mecanismos de extensão;
-   compatibilidade retroativa;
-   exemplos reais de payloads;
-   mecanismos de autenticação e autorização;
-   requisitos de conformidade.

### 6.4 Análise de cobertura

Classificar a cobertura de cada referência por domínio:

-   **Completa:** o domínio é tratado de forma explícita e substancial.
-   **Parcial:** há elementos relevantes, mas faltam partes importantes.
-   **Indireta:** o tema aparece apenas por associação ou integração.
-   **Ausente:** não foi identificada cobertura.
-   **Não verificada:** documentação insuficiente para concluir.

Não atribuir notas de qualidade. O objetivo é compreender escopo,
complementaridade e lacunas.

------------------------------------------------------------------------

## 7. Entregáveis esperados

Cada agente deve produzir:

1.  **Reference Profile:** ficha técnica de cada norma ou framework.
2.  **Data Model Inventory:** entidades, atributos, identificadores e
    relações.
3.  **Terminology Inventory:** conceitos, códigos, classificações e
    vocabulários.
4.  **API & Schema Inventory:** APIs, formatos, schemas e exemplos.
5.  **Compliance & Governance Report:** situação normativa, privacidade,
    segurança e licenciamento.
6.  **Domain Coverage Matrix:** cobertura dos oito domínios.
7.  **Crosswalk:** mapeamento de conceitos entre referências.
8.  **Open Issues:** ambiguidades, lacunas, conflitos e decisões
    pendentes.
9.  **Evidence Register:** fontes oficiais, páginas, versões e datas que
    sustentam cada conclusão.

Não propor a implementação definitiva antes de concluir o inventário e a
análise comparativa.

------------------------------------------------------------------------

## 8. Matriz comparativa consolidada

Criar uma matriz com uma linha por referência e, no mínimo, as seguintes
colunas:

  Campo             Descrição
  ----------------- ---------------------------------------------------------
  Referência        Nome e sigla
  Jurisdição        País, região ou internacional
  Emissor           Organização responsável
  Tipo              Lei, norma, padrão, framework ou vocabulário
  Versão            Versão vigente analisada
  Status            Obrigatório, voluntário, recomendação ou não verificado
  Domínios          D1 a D8
  Modelo de dados   Sim, parcial ou não
  API               Sim, parcial ou não
  Schema            RDF, JSON, XML, XSD, JSON Schema etc.
  Licença           Condições de uso
  Repositório       Código e documentação técnica
  Limitações        Restrições e lacunas
  Evidências        Fontes oficiais

------------------------------------------------------------------------

## 9. Resultado final da pesquisa

A pesquisa deverá permitir especificar:

### 9.1 VUOO Agnostic Core

-   modelo conceitual;
-   glossário canônico;
-   entidades e relações;
-   identificadores;
-   contratos de dados;
-   APIs internas;
-   versionamento;
-   regras de extensão;
-   governança e proveniência.

### 9.2 Regional Adapters

Para cada jurisdição:

-   modelo regional;
-   vocabulários e classificações;
-   regras obrigatórias;
-   identificadores locais;
-   mapeamentos para o Core;
-   validações;
-   importação e exportação;
-   APIs e formatos exigidos;
-   diferenças e incompatibilidades documentadas.

### 9.3 Crosswalk internacional

Construir tabelas de correspondência entre:

-   conceitos acadêmicos;
-   etapas e níveis educacionais;
-   estruturas curriculares;
-   competências e habilidades;
-   avaliações e resultados;
-   identidades e vínculos;
-   dados de organização escolar.

Toda correspondência deve indicar se é equivalência exata, aproximada,
parcial ou inexistente.

------------------------------------------------------------------------

## 10. Critérios de conclusão

A varredura estará pronta para subsidiar a arquitetura quando:

-   as referências prioritárias tiverem fichas verificadas;
-   as versões e situações normativas estiverem confirmadas;
-   os principais modelos de dados tiverem sido inspecionados;
-   as entidades e relações dos domínios D1 a D8 estiverem
    inventariadas;
-   as diferenças regionais estiverem documentadas;
-   os mapeamentos entre padrões tiverem evidências;
-   lacunas e conflitos estiverem registrados;
-   houver material suficiente para propor o glossário e o modelo
    conceitual agnóstico da VUOO.

**Regra final:** o objetivo não é reproduzir um padrão existente. É
construir uma arquitetura educacional interoperável, extensível e
independente de jurisdição, fundamentada em padrões verificáveis e capaz
de se adaptar às exigências locais.
