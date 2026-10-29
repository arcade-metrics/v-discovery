---
id: psg.access.minimization-and-privacy-by-design
titulo: Minimização, limitação de finalidade e privacy by design
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, eu2016gdpr, cavoukian2011pbd, nist2020sp80053r5, nist2014sp800162]
relacoes:
  - { tipo: complementa, alvo: psg.access.rbac-and-abac }
  - { tipo: complementa, alvo: psg.access.school-roles }
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: complementa, alvo: psg.sec.encryption-and-key-management }
  - { tipo: complementa, alvo: iop.fund.privacidade-e-seguranca }
  - { tipo: relacionado-a, alvo: psg.audit.ripd-dpia }
  - { tipo: relacionado-a, alvo: psg.audit.processing-records }
termos: [minimização de dados, necessidade, finalidade, adequação, limitação de finalidade, privacy by design, privacy by default, segregação de bases, base operacional, base de pesquisa, esquema de dados, identificabilidade, vinculabilidade, retenção]
---

# Minimização, limitação de finalidade e privacy by design

## Definição e terminologia

**Minimização** é o princípio de coletar e manter só o dado pessoal necessário a uma finalidade declarada. A LGPD o chama de **necessidade**: "limitação do tratamento ao mínimo necessário para a realização de suas finalidades" [F: brasil2018lgpd, art. 6, III]. Dois princípios vizinhos o completam: **finalidade**, "realização do tratamento para propósitos legítimos, específicos, explícitos e informados ao titular" [F: brasil2018lgpd, art. 6, I], e **adequação**, "compatibilidade do tratamento com as finalidades informadas ao titular, de acordo com o contexto do tratamento" [F: brasil2018lgpd, art. 6, II]. Juntos, formam o que a literatura chama de limitação de finalidade: um dado coletado para operar a aula não pode ser reusado para outra coisa sem nova justificativa [I].

**Privacy by design** (PbD) é a exigência de que a proteção seja decidida na concepção do sistema, não acrescentada depois. Cavoukian enuncia sete princípios fundacionais: proativo e preventivo; privacidade como configuração padrão; privacidade embutida no design; funcionalidade plena (soma positiva); segurança de ponta a ponta; visibilidade e transparência; respeito à privacidade do usuário [F: cavoukian2011pbd, apêndice A]. A LGPD determina que as medidas de segurança "deverão ser observadas desde a fase de concepção do produto ou do serviço até a sua execução" [F: brasil2018lgpd, art. 46, §2] e que os sistemas de tratamento "devem ser estruturados de forma a atender aos requisitos de segurança", às boas práticas e aos princípios da lei [F: brasil2018lgpd, art. 49]. O GDPR, no art. 25, exige que o controlador "implement appropriate technical and organisational measures" já "at the time of the determination of the means for processing" (by design) e garanta que, "by default, only personal data which are necessary for each specific purpose of the processing are processed" (by default), o que abrange quantidade coletada, extensão do tratamento, prazo de guarda e acessibilidade [F: eu2016gdpr, art. 25(1)-(2)].

O que não é: minimização não é anonimização (que trata de tornar não identificável o que já foi coletado; ver `psg.deid.anonymization-and-pseudonymization`) nem controle de acesso (que decide quem vê o que existe; ver `psg.access.school-roles`). Minimização atua antes dos dois: decide o que passa a existir [I].

## Problema que resolve

Plataformas educacionais registram interações com granularidade fina, e o esquema de eventos tende a crescer por conveniência. Cada campo a mais é um dado a proteger, a explicar ao responsável, a reter e a apagar. Cavoukian formula o princípio do padrão: "if an individual does nothing, their privacy still remains intact" [F: cavoukian2011pbd, princípio 2]. Em contexto de crianças, isso importa duplamente porque a LGPD veda condicionar a participação em jogos ou aplicações à coleta de dados além do necessário à atividade [F: brasil2018lgpd, art. 14, §4] e exige que o tratamento observe o melhor interesse da criança [F: brasil2018lgpd, art. 14].

## Fundamentos e funcionamento

### Minimização como decisão de esquema

A forma mais barata de proteger um dado é não tê-lo. Cavoukian recomenda que o desenho de sistemas "begin with non-identifiable interactions and transactions, as the default" e que "identifiability, observability, and linkability of personal information should be minimized" [F: cavoukian2011pbd, princípio 2]. Em termos de esquema, isso significa decidir, campo a campo: (a) se o campo é necessário à finalidade declarada; (b) se pode ser substituído por uma versão menos identificável (faixa etária em vez de data de nascimento; identificador pseudônimo em vez de nome no fluxo de eventos); (c) se pode ser derivado sob demanda em vez de armazenado; (d) por quanto tempo precisa existir [I]. O GDPR nomeia explicitamente a pseudonimização e a minimização como exemplos de medidas de proteção desde a concepção [F: eu2016gdpr, art. 25(1)].

### Limitação de finalidade como segregação de bases

Uma plataforma escolar tem pelo menos duas finalidades distintas: operar o ensino (mostrar ao professor o progresso de cada aluno, nominalmente) e pesquisar ou melhorar o produto (analisar padrões em massa). A LGPD trata a segunda como hipótese própria quando feita por órgão de pesquisa, "garantida, sempre que possível, a anonimização dos dados pessoais" [F: brasil2018lgpd, art. 7, IV]. O princípio da adequação [F: brasil2018lgpd, art. 6, II] impede que a base operacional seja simplesmente aberta para análise: o contexto informado ao titular foi o de ensino [I].

A tradução arquitetural é manter **bases segregadas por finalidade**: a base operacional, nominal, com acesso por papel (`psg.access.school-roles`); e a base de pesquisa, derivada por um pipeline que pseudonimiza ou anonimiza (`psg.deid.anonymization-and-pseudonymization`), remove campos sem uso analítico e não permite ligação de volta ao aluno sem procedimento controlado. O SP 800-53 oferece dois controles de apoio: AC-16, que vincula atributos de privacidade à informação para aplicar "data retention limits, permitted uses of personally identifiable information", inclusive consentimento individual [F: nist2020sp80053r5, AC-16]; e AC-6(4), que prevê "separate processing domains to enable finer-grained allocation of user privileges" [F: nist2020sp80053r5, AC-6(4)]. Chaves e segredos distintos por base são tratados em `psg.sec.encryption-and-key-management`.

### Privacy by default

O art. 25(2) do GDPR acrescenta que, por padrão, os dados pessoais não devem ficar acessíveis a um número indefinido de pessoas sem intervenção do titular [F: eu2016gdpr, art. 25(2)]. Cavoukian traduz isso em "the default settings shall be the most privacy protective" quando o uso não estiver claro, com presunção de privacidade e princípio da precaução [F: cavoukian2011pbd, princípio 2]. Para uma plataforma escolar, os padrões afetados são: perfil do aluno invisível a outros alunos; telemetria detalhada desligada até haver finalidade e base legal; exportação de dados nominal só por papéis definidos [I].

### Relação com controle de acesso

Minimização e controle de acesso são complementares, não substitutos. O SP 800-162 observa que ABAC pode decidir sem conhecimento prévio do sujeito, mas a responsabilização exige rastrear identidade nas decisões [F: nist2014sp800162, §2.3]; o AC-24(2) prevê decisões sem identidade do usuário quando a privacidade é prioritária [F: nist2020sp80053r5, AC-24(2)]. A base de pesquisa é o lugar natural para esse segundo regime: o analista acessa por atributo (projeto aprovado, período) e nunca vê identificador direto [I].

## Requisitos e pressupostos

- Finalidades enumeradas e registradas antes do desenho do esquema (ver `psg.audit.processing-records`); sem lista de finalidades não há como julgar necessidade [I].
- Um pipeline unidirecional da base operacional para a de pesquisa, com regras documentadas de remoção e transformação de campos [I].
- Avaliação de impacto (RIPD) que documente o risco de cada campo mantido; Cavoukian recomenda avaliações de impacto publicadas, "clearly documenting the privacy risks and all measures taken to mitigate those risks" [F: cavoukian2011pbd, princípio 3] (ver `psg.audit.ripd-dpia`).
- Para menores, consentimento e demais bases conforme `psg.legal.lgpd-children`.

## Vantagens e limitações

Vantagens: menos campos reduzem superfície de vazamento, custo de retenção e de atendimento a direitos do titular [I]; a segregação permite que a análise em massa avance sem abrir a base nominal, e Cavoukian argumenta que privacidade e funcionalidade não são soma zero [F: cavoukian2011pbd, princípio 4]. Limitações: a necessidade é julgada contra a finalidade, e finalidades de pesquisa exploratória são difíceis de enumerar de antemão, o que tensiona o princípio [I]; pseudonimização mantém o dado pessoal (ver `psg.deid.anonymization-and-pseudonymization`), logo a base de pesquisa continua sujeita à lei [I]; os sete princípios de Cavoukian são declarações de alto nível sem critério de verificação próprio, e o próprio documento se apresenta como "reference framework" a ser detalhado para auditoria [F: cavoukian2011pbd, propósito]; a afirmação de soma positiva é programática, não demonstrada [I].

## Alternativas e comparações

| Critério | Cavoukian, 7 princípios | LGPD art. 6, 46 §2 e 49 | GDPR art. 25 |
|---|---|---|---|
| Natureza | quadro de referência de autoridade de proteção de dados (Ontário) [F: cavoukian2011pbd] | lei [F: brasil2018lgpd] | regulamento [F: eu2016gdpr] |
| By design | princípios 1 e 3 (proativo, embutido) | art. 46 §2: desde a concepção até a execução | art. 25(1): no momento de definir os meios |
| By default | princípio 2: padrão mais protetivo | não há dispositivo explícito; decorre de necessidade e adequação (art. 6) [I] | art. 25(2): só o necessário a cada finalidade, por padrão |
| Minimização | "data minimization" como FIP mapeada ao princípio 2 | art. 6, III (necessidade) | citada como exemplo de medida no art. 25(1) |
| Demonstração de conformidade | sugere avaliações de impacto publicadas | art. 50: programa de governança demonstrável à autoridade | art. 25(3): certificação aprovada como elemento de prova |

## Métricas e métodos de avaliação

Indicadores propostos [I]: número de campos de dado pessoal por finalidade registrada; proporção de campos identificadores diretos no fluxo de eventos; prazo de retenção por tabela; número de acessos nominais à base de pesquisa (meta: zero). Métodos: revisão periódica dos atributos de privacidade, exigida por AC-16f [F: nist2020sp80053r5, AC-16]; RIPD por mudança de esquema (`psg.audit.ripd-dpia`); teste de reidentificação da base de pesquisa (`psg.deid.reidentification-risk`).

## Exemplo técnico independente de domínio

```
# Esquema de evento de interação: antes e depois da revisão de necessidade
antes:  {aluno_nome, data_nascimento, cpf_responsavel, ip, texto_livre, item, acerto, tempo_ms, ts}
depois: {aluno_pid, faixa_etaria, item, acerto, tempo_ms, ts}
        # aluno_pid: pseudônimo por aluno, tabela de ligação em base separada
        # ip e texto_livre removidos: sem finalidade declarada
        # cpf_responsavel: só na base de consentimento, nunca no fluxo de eventos

# Segregação por finalidade
base_operacional  (nominal)   finalidade=ensino        acesso=por papel (school-roles)
base_pesquisa     (pseudônima) finalidade=pesquisa      acesso=por atributo (projeto, período)
pipeline: operacional -> remover(identificadores diretos) -> generalizar(idade) -> pesquisa
regra: nenhum caminho pesquisa -> operacional sem procedimento registrado
```

## Relações com outros conceitos

Complementa `psg.access.rbac-and-abac` e `psg.access.school-roles`: minimização decide o que existe, controle de acesso decide quem vê. Depende de `psg.legal.lgpd-children` para bases legais e melhor interesse. Complementa `psg.deid.anonymization-and-pseudonymization` (como a base de pesquisa é derivada), `psg.sec.encryption-and-key-management` (segregação de chaves entre bases) e `iop.fund.privacidade-e-seguranca` (minimização no que atravessa a fronteira entre sistemas). Relaciona-se com `psg.audit.ripd-dpia` e `psg.audit.processing-records`.

## Lacunas e questões abertas

- O texto oficial do GDPR no EUR-Lex não pôde ser carregado nesta sessão (respostas vazias); o art. 25 foi lido em reprodução de terceiro (gdpr-info.eu). Os arts. 5(1)(b) e 5(1)(c), que enunciam limitação de finalidade e minimização, não foram lidos e por isso não são citados.
- ISO 31700-1:2023 (privacy by design para bens e serviços de consumo) não foi acessada (página da ISO com acesso negado); só resultados de busca em catálogos indicam sua existência, o que não basta para citar.
- Guias da ANPD sobre tratamento de dados de crianças e sobre segurança não foram consultados nesta área; ficam para `psg.legal.lgpd-children` e `psg.sec.threat-model-education`.
- Se a plataforma, e não um órgão de pesquisa, pode usar o art. 7, IV, ou se a melhoria do produto cai em outra base legal, é questão jurídica não resolvida aqui.
- A leitura da LGPD foi feita em página com codificação de acentos corrompida; as citações foram normalizadas e devem ser conferidas contra o texto do Planalto antes da revisão.
- Indicadores de minimização propostos não têm validação em literatura consultada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| eu2016gdpr | normativo (lido em reprodução gdpr-info.eu) | 2026-10-29 |
| cavoukian2011pbd | tecnico | 2026-10-29 |
| nist2020sp80053r5 | normativo | 2026-10-29 |
| nist2014sp800162 | tecnico | 2026-10-29 |
