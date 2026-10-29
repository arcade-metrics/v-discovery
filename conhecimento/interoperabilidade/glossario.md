---
id: iop.glossario
titulo: Glossário de interoperabilidade educacional
tipo: glossario
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Glossário: interoperabilidade educacional

Termos consolidados do domínio, com definição curta e o id do documento que aprofunda e cita a fonte. Termos em inglês quando esse é o uso corrente na literatura e nas especificações.

## Camadas e conceitos gerais

| Termo | Definição | Documento |
|---|---|---|
| interoperabilidade técnica | capacidade de conectar e trocar dados: transporte, formato, autenticação | iop.fund.niveis-de-interoperabilidade |
| interoperabilidade semântica | capacidade de atribuir o mesmo significado aos dados trocados | iop.sem.interoperabilidade-semantica |
| interoperabilidade organizacional | alinhamento de processos, papéis e acordos entre as instituições que trocam dados | iop.fund.niveis-de-interoperabilidade |
| interoperabilidade jurídica | existência de base legal para a troca | iop.fund.niveis-de-interoperabilidade |
| perfil de aplicação | documento que fixa, para uma comunidade, campos obrigatórios e valores válidos de um padrão | iop.sem.interoperabilidade-semantica |
| binding | regra de serialização de um modelo abstrato em um formato concreto (XML, JSON, CSV) | iop.fund.dados-vs-protocolo |
| crosswalk | correspondência declarada entre elementos de dois modelos de dados | iop.fund.mapeamento-e-proveniencia |
| proveniência | registro de origem, transformação e autoridade de um dado | iop.fund.mapeamento-e-proveniencia |
| conformidade | satisfazer os requisitos normativos de uma especificação | iop.fund.conformidade-e-certificacao |
| certificação | reconhecimento por terceiro de aprovação em um conjunto de testes | iop.fund.conformidade-e-certificacao |

## Identidade

| Termo | Definição | Documento |
|---|---|---|
| IFI (inverse functional identifier) | identificador único de um Agent xAPI: `mbox`, `mbox_sha1sum`, `openid` ou `account` | iop.fund.identidade-e-contexto |
| `account` | IFI composto por `homePage` e `name`, usado para identificadores opacos | iop.lr.xapi |
| `registration` | UUID que agrupa os eventos de uma mesma tentativa ou inscrição | iop.lr.xapi |
| `sourcedId` | identificador de entidade atribuído pelo sistema de origem, no OneRoster | iop.ros.oneroster |
| `deployment_id` | identificador da instalação de uma ferramenta em uma plataforma, no LTI | iop.tool.lti-core |
| pseudonimização | substituição do identificador direto por um opaco, com tabela de resolução sob controle | iop.fund.privacidade-e-seguranca |

## Registro de experiências

| Termo | Definição | Documento |
|---|---|---|
| statement | unidade de registro do xAPI: actor, verb, object, mais result e context | iop.lr.xapi |
| LRS (Learning Record Store) | repositório que recebe e serve statements xAPI | iop.lr.xapi |
| voiding | única forma suportada de desfazer um statement xAPI | iop.lr.xapi |
| SubStatement | statement embutido como objeto de outro, sem id próprio | iop.lr.xapi |
| AU (assignable unit) | unidade lançável e rastreável do cmi5 | iop.lr.cmi5 |
| moveOn | critério de satisfação de uma AU no cmi5 | iop.lr.cmi5 |
| masteryScore | limiar de aprovação, decimal de 0 a 1, passado pelo LMS à AU | iop.lr.cmi5 |
| cmi5 allowed / defined | classificação de statements conforme usem ou não o vocabulário e a categoria cmi5 | iop.lr.cmi5 |
| Sensor | componente que emite dados Caliper a partir da aplicação | iop.lr.caliper |
| Envelope | contêiner de transporte Caliper, com metadados do Sensor | iop.lr.caliper |
| perfil (Caliper) | vocabulário tipado de eventos para uma área de atividade | iop.lr.caliper |
| SCO | unidade de conteúdo lançável e rastreável no SCORM | iop.tool.scorm |
| PIF | pacote de intercâmbio SCORM (diretório ou ZIP com `imsmanifest.xml`) | iop.tool.scorm |

## Integração de ferramentas e avaliação

| Termo | Definição | Documento |
|---|---|---|
| plataforma / ferramenta | os dois papéis do LTI: quem lança e quem é lançado | iop.tool.lti-core |
| claim | propriedade do token de lançamento LTI | iop.tool.lti-core |
| NRPS | serviço LTI de leitura de membros e papéis de um contexto | iop.tool.lti-advantage |
| AGS | serviço LTI de line items, scores e results | iop.tool.lti-advantage |
| line item | coluna de nota criada pela ferramenta na plataforma | iop.tool.lti-advantage |
| Deep Linking | fluxo LTI em que o usuário seleciona conteúdo na ferramenta | iop.tool.lti-advantage |
| content item | item devolvido pelo Deep Linking: link, ltiResourceLink, file, html, image | iop.tool.lti-advantage |
| cartridge | pacote Common Cartridge com conteúdo, links e avaliações | iop.tool.common-cartridge |
| Thin CC | perfil reduzido do Common Cartridge, centrado em links | iop.tool.common-cartridge |
| PCI | Portable Custom Interaction: interação customizada portável do QTI 3.0 | iop.asmt.qti |
| CAT | Computer Adaptive Testing, nativo no QTI 3.0 | iop.asmt.qti |

## Dados escolares, metadados e competências

| Termo | Definição | Documento |
|---|---|---|
| rostering | troca de dados de turmas, pessoas e matrículas | iop.ros.oneroster |
| Unifying Data Model | modelo lógico não normativo por trás do Ed-Fi Data Standard | iop.ros.ed-fi |
| descriptor | vocabulário controlado do Ed-Fi (citado, não verificado) | iop.ros.ed-fi |
| locale (SIF) | jurisdição para a qual um modelo de dados SIF é publicado | iop.ros.sif |
| elemento de dado | unidade de significado definida pelo CEDS | iop.ros.ceds |
| leiaute | formato posicional do arquivo de migração do Educacenso | iop.br.educacenso |
| objeto de aprendizagem | recurso descrito por metadados LOM | iop.md.ieee-lom |
| `teaches` / `assesses` | propriedades de LearningResource que ligam recurso a competência | iop.md.lrmi-schema-org |
| `educationalAlignment` | alinhamento de um recurso a um framework educacional | iop.md.lrmi-schema-org |
| framework (CASE) | conjunto publicado de competências e padrões curriculares com identificadores | iop.comp.case |
| CTDL-ASN | esquema do Credential Engine para competências | iop.comp.ctdl |
| qualificação (ESCO) | um dos três pilares da classificação europeia | iop.comp.esco |

## Credenciais, semântica e saúde

| Termo | Definição | Documento |
|---|---|---|
| verifiable credential | credencial à prova de adulteração, com autoria verificável criptograficamente | iop.cred.verifiable-credentials |
| issuer / holder / verifier | os três papéis do ecossistema de credenciais verificáveis | iop.cred.verifiable-credentials |
| proof embutida / envelopante | prova dentro do documento (Data Integrity) ou encapsulando-o (JOSE/COSE) | iop.cred.verifiable-credentials |
| assertion | afirmação de que um sujeito obteve uma conquista | iop.cred.open-badges |
| baking | embutir os dados do badge em um arquivo PNG ou SVG | iop.cred.open-badges |
| ClrCredential | registro de topo do Comprehensive Learner Record | iop.cred.clr |
| `skos:Concept` | unidade de um vocabulário controlado em SKOS | iop.sem.vocabularios-e-skos |
| `exactMatch` / `closeMatch` | equivalência confiável versus similaridade parcial entre conceitos | iop.sem.vocabularios-e-skos |
| qualificador (CIF) | escala de 0 a 4 que gradua o problema em um domínio da CIF | iop.health.cif |
| capacidade × desempenho | o que a pessoa faz em ambiente padronizado versus no ambiente atual | iop.health.cif |
| Profile (FHIR) | restrição de um Resource para um caso de uso, via StructureDefinition | iop.health.fhir |
| ValueSet / ConceptMap | seleção de códigos válidos e correspondência entre sistemas de código, no FHIR | iop.health.fhir |

## Regime jurídico

| Termo | Definição | Documento |
|---|---|---|
| dado pessoal | informação relacionada a pessoa natural identificada ou identificável | iop.br.lgpd |
| dado pessoal sensível | dado sobre saúde, origem racial, convicção, biometria e afins, vinculado a pessoa natural | iop.br.lgpd |
| base legal | hipótese do art. 7 da LGPD que autoriza o tratamento | iop.br.lgpd |
| princípio da necessidade | limitação do tratamento ao mínimo necessário à finalidade | iop.br.lgpd |
