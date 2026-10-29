---
id: psg.access.school-roles
titulo: Papéis escolares e separação de visões sobre o aluno
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2022oneroster, ceds2026entities, nces2026ceds, brasil2018lgpd, nist2020sp80053r5, sandhu1996rbacmodels, ferraiolokuhn1992rbac, nist2014sp800162]
relacoes:
  - { tipo: depende-de, alvo: psg.access.rbac-and-abac }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: iop.ros.oneroster }
  - { tipo: relacionado-a, alvo: iop.ros.ceds }
  - { tipo: relacionado-a, alvo: iop.fund.identidade-e-contexto }
  - { tipo: relacionado-a, alvo: psg.consent.permission-lifecycle }
  - { tipo: relacionado-a, alvo: psg.audit.audit-trails }
termos: [papel escolar, professor regente, coordenador pedagógico, gestor de rede, responsável legal, atendimento educacional especializado, separação de visões, escopo de acesso, papel primário, papel secundário, vínculo temporal, dado sensível]
---

# Papéis escolares e separação de visões sobre o aluno

## Definição e terminologia

Papel escolar é a função que uma pessoa exerce em relação a uma organização de ensino (rede, escola, turma) e que determina o que ela pode ver e fazer sobre os dados de cada aluno. No OneRoster 1.2, cada usuário "must have at least one role and each role is assigned in the context of a single org", e um usuário pode ter muitos papéis em muitas organizações [F: imsglobal2022oneroster, §3.3]; o atributo `roles` do usuário é "a set of role/org tuples", cada tupla com `roleType` (`primary` ou `secondary`, com exatamente um papel primário por organização), `role`, `org`, `userProfile`, `beginDate` e `endDate` [F: imsglobal2022oneroster, §6.1.22, §6.1.30.12].

O vocabulário `RoleEnum` do OneRoster 1.2 contém `aide`, `counselor`, `districtAdministrator`, `guardian`, `parent`, `principal`, `proctor`, `relative`, `siteAdministrator`, `student`, `systemAdministrator` e `teacher`; entre as definições: `aide` é "someone who provides appropriate aid to the user but NOT also one of the other roles"; `counselor`, "someone who has care/pastoral supervision responsibility for one or more people"; `guardian`, "guardian of the user and NOT the Mother or Father"; `principal`, "the schools' Principal or other very senior academic administrator in the School", que "will have access to confidential/private data about teachers, etc."; `districtAdministrator`, responsável por sistemas dos sites do distrito ou acessados pelas escolas do distrito [F: imsglobal2022oneroster, §6.3.11]. O vocabulário é declarado extensível para "profiling and internationalisation" [F: imsglobal2022oneroster, §1.3]. Há um segundo vocabulário, `EnrolRoleEnum`, para o papel dentro de uma turma: `administrator`, `proctor`, `student` e `teacher` [F: imsglobal2022oneroster, §6.3.6].

O CEDS, vocabulário do NCES [F: nces2026ceds], organiza as pessoas em entidades por domínio; para o K12, define `K12 Student` como "a person for whom instruction, services, and/or care are provided in an elementary or secondary educational program", `K12 Staff` como "an individual who performs specified activities for any public or private education institution, agency, or household" e `Parent/Guardian` como "a person having parental or legal guardianship responsibility for a learner" [F: ceds2026entities]. Os documentos `iop.ros.oneroster` e `iop.ros.ceds` descrevem os dois padrões como um todo; aqui interessa só o vocabulário de papéis.

Os papéis brasileiros usados neste documento (professor regente, coordenador pedagógico, gestor de rede, responsável, equipe de atendimento educacional especializado, AEE) não têm correspondência um-a-um nesses vocabulários. O mapeamento proposto é interpretação: regente ≈ `teacher` com `EnrolRoleEnum=teacher` na turma; coordenador ≈ `principal` ou `siteAdministrator` com escopo de escola; gestor de rede ≈ `districtAdministrator`; responsável ≈ `parent`/`guardian`/`relative`; AEE ≈ `aide` ou `counselor` com escopo por aluno atendido [I].

## Problema que resolve

Um mesmo aluno é visto por pessoas com funções e necessidades diferentes. Sem separação de visões, o caminho de menor esforço é dar a todos a mesma tela, e o dado mais sensível (laudo, diagnóstico, situação familiar) passa a circular por quem não precisa dele. A LGPD exige "limitação do tratamento ao mínimo necessário para a realização de suas finalidades" (princípio da necessidade) [F: brasil2018lgpd, art. 6, III] e classifica como dado pessoal sensível, entre outros, o dado referente à saúde [F: brasil2018lgpd, art. 5, II]; o SP 800-53 exige menor privilégio, "allowing only authorized accesses ... that are necessary to accomplish assigned organizational tasks" [F: nist2020sp80053r5, AC-6]. Separação de visões é a tradução desses dois requisitos para o desenho de telas e de API [I].

## Fundamentos e funcionamento

### Vocabulário de papéis e escopo

Os modelos de `psg.access.rbac-and-abac` sugerem uma divisão de trabalho: RBAC nomeia a função (o que um "professor" pode fazer), e relações ou atributos delimitam o escopo (de quais alunos). O próprio OneRoster expressa isso ao vincular cada papel a uma organização e cada matrícula a uma turma [F: imsglobal2022oneroster, §3.3]. Um regente, portanto, não "vê alunos": vê os alunos das turmas em que sua matrícula tem `EnrolRoleEnum=teacher` no ano letivo corrente [I]. As datas `beginDate` e `endDate` do papel [F: imsglobal2022oneroster, §6.1.22] permitem expirar o acesso ao fim do vínculo, em vez de depender de remoção manual; o SP 800-53 prevê revogação de autorizações a partir de mudanças em atributos de sujeitos e objetos, com regras de prazo definidas pela organização [F: nist2020sp80053r5, AC-3(8)].

### Matriz de visões proposta

A tabela abaixo é uma proposta de separação [I], construída a partir do menor privilégio [F: nist2020sp80053r5, AC-6] e da necessidade [F: brasil2018lgpd, art. 6, III]. "Agregado" significa estatística por turma ou escola, sem linha por aluno.

| Categoria de dado do aluno | Regente | Coordenador | Gestor de rede | Responsável | Equipe AEE |
|---|---|---|---|---|---|
| Identificação e turma | suas turmas | sua escola | agregado; nominal só sob justificativa registrada | o próprio filho | alunos atendidos |
| Desempenho e progresso na disciplina | suas turmas, nominal | sua escola, nominal por exceção (encaminhamento) | agregado | o próprio filho | alunos atendidos |
| Interações detalhadas (tentativas, tempo, erros) | suas turmas | agregado | agregado | resumo do próprio filho | alunos atendidos, nominal |
| Laudo, deficiência, plano individualizado (sensível) | só o necessário à adaptação em sala, por aluno | só quem coordena o AEE | nunca nominal | o próprio filho, integral | integral, alunos atendidos |
| Contato e situação familiar | não | sim, sua escola | não | o próprio registro | quando necessário ao atendimento |
| Dados de outros alunos da turma | nomes, nunca desempenho individual | sua escola | agregado | nunca | nunca |

Três decisões da tabela merecem justificativa. Primeira: o gestor de rede opera sobre agregados, e o SP 800-53 prevê decisões de acesso "based on ... attributes that do not include the identity of the user" quando a privacidade individual é prioritária [F: nist2020sp80053r5, AC-24(2)]; o acesso nominal excepcional deve ficar registrado (ver `psg.audit.audit-trails`). Segunda: o coordenador não herda automaticamente a visão detalhada do regente. Sandhu et al. mostram que hierarquias de papéis fazem o papel sênior herdar tudo do júnior, e introduzem papéis privados exatamente para impedir essa herança quando "access to incomplete work in progress may not be appropriate for the senior role" [F: sandhu1996rbacmodels, §4.2]; aplicado à escola, senioridade administrativa não implica necessidade de ver o detalhe pedagógico [I]. Terceira: o laudo é dado sensível [F: brasil2018lgpd, art. 5, II] e seu tratamento deve observar o melhor interesse da criança [F: brasil2018lgpd, art. 14]; a equipe de AEE o vê integralmente porque ele é insumo do atendimento, enquanto o regente vê só a adaptação derivada (por exemplo, "usa leitor de tela", não o diagnóstico) [I]. Os fundamentos legais de cada base são aprofundados em `psg.legal.lgpd-children`.

### Papéis múltiplos e separação de deveres

A mesma pessoa pode ser professora de uma turma e mãe de um aluno de outra; o OneRoster modela isso com várias tuplas papel/organização [F: imsglobal2022oneroster, §6.1.30.12], e Sandhu et al. com sessões que ativam só os papéis necessários à tarefa [F: sandhu1996rbacmodels, §4.1]. A interface deve pedir a ativação explícita do papel, para que a visão de professor não vaze para a visão de responsável [I]. A separação de deveres (AC-5) manda, entre outras coisas, que "security personnel who administer access control functions do not also administer audit functions" [F: nist2020sp80053r5, AC-5]; na escola, quem atribui papéis (secretaria ou administrador do sistema) não deve ser quem revisa os registros de acesso [I]. Ferraiolo e Kuhn descrevem a separação dinâmica como a que depende de usuário e papel em tempo de execução, como proibir que alguém autorize o que ele próprio iniciou [F: ferraiolokuhn1992rbac, §6]; o análogo escolar é impedir que um professor revise, como coordenador, um encaminhamento que ele mesmo fez [I].

## Requisitos e pressupostos

- Uma fonte autoritativa de papéis e matrículas (ver `iop.ros.oneroster`); sem ela, o escopo "minhas turmas" não é computável [I].
- Papéis com vigência (`beginDate`/`endDate`) e revogação acoplada à saída da pessoa [F: imsglobal2022oneroster, §6.1.22; nist2020sp80053r5, AC-3(8)].
- Consentimento e demais bases legais para cada categoria de dado, inclusive do responsável para o dado sensível da criança (`psg.legal.lgpd-children`, `psg.consent.permission-lifecycle`).
- Registro das decisões de acesso com identidade do sujeito, pois o SP 800-162 alerta que a responsabilização se perde se decisões por atributos não forem rastreadas a sujeitos [F: nist2014sp800162, §2.3].

## Vantagens e limitações

Vantagens [I]: a matriz torna explícito o que cada função precisa, o que facilita o RIPD e a resposta a pedidos de acesso do titular; vocabulários padronizados permitem importar papéis do sistema de gestão em vez de recadastrá-los. Limitações: os vocabulários consultados não têm o papel de AEE nem o de coordenador pedagógico, e o perfil `aide` exclui explicitamente quem tem outro papel [F: imsglobal2022oneroster, §6.3.11], o que obriga a extensões locais; escolas pequenas acumulam funções em poucas pessoas, e separação de deveres pode ser inviável sem revisão compensatória [I]; a matriz proposta não foi validada empiricamente com equipes escolares [H].

## Exemplo técnico independente de domínio

```
# Política híbrida: papel (RBAC) nomeia a função, relação (ReBAC) delimita o escopo
papel(u, teacher, org=escola_X, ate=2026-12-20)
regente_de(u, turma_7B)                    # derivado de enrollment role=teacher
atende(e, aluno_42)                        # vínculo da equipe de AEE com o aluno

ver(u, aluno, categoria) :=
  categoria ∈ {identificacao, desempenho, interacoes} ∧ regente_de(u, turma(aluno))
  ∨ categoria = laudo_resumido ∧ regente_de(u, turma(aluno))
  ∨ categoria ∈ {laudo_integral, interacoes} ∧ atende(u, aluno)
  ∨ categoria = agregado(turma|escola|rede) ∧ papel(u, districtAdministrator)
  ∨ aluno ∈ filhos(u) ∧ categoria ≠ dados_de_terceiros
# toda avaliação de ver(...) é registrada com u, aluno, categoria, instante
```

## Relações com outros conceitos

Depende de `psg.access.rbac-and-abac` (modelos) e de `psg.legal.lgpd-children` (bases legais e dado sensível de criança). Complementa `psg.access.minimization-and-privacy-by-design`: a matriz decide quem vê; a minimização decide o que existe para ser visto. Relaciona-se com `iop.ros.oneroster`, `iop.ros.ceds` e `iop.fund.identidade-e-contexto` (de onde vêm papéis e contexto), com `psg.consent.permission-lifecycle` (vigência das permissões do responsável) e com `psg.audit.audit-trails` (registro das exceções).

## Lacunas e questões abertas

- O conjunto de opções de "Role" do CEDS não foi localizado nas páginas abertas (só as entidades K12 Student, K12 Staff e Parent/Guardian); o vocabulário completo fica não verificado.
- Não foi consultado vocabulário brasileiro de funções escolares (por exemplo, o do Censo Escolar) para ancorar "coordenador pedagógico", "gestor de rede" e "AEE"; o mapeamento para OneRoster é proposta.
- O vocabulário de papéis do LTI (instructor, learner, mentor etc.) não foi coberto; fica em `interoperabilidade`.
- A matriz de visões precisa de validação com equipes de AEE e de gestão; em especial, se o regente deve ver o tipo de deficiência ou apenas as adaptações.
- Como tratar o aluno maior de idade e o adolescente que pede sigilo em relação ao responsável não foi coberto; depende de `psg.legal.lgpd-children`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2022oneroster | normativo | 2026-10-29 |
| ceds2026entities | fornecedor | 2026-10-29 |
| nces2026ceds | fornecedor | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
| nist2020sp80053r5 | normativo | 2026-10-29 |
| sandhu1996rbacmodels | academico | 2026-10-29 |
| ferraiolokuhn1992rbac | academico | 2026-10-29 |
| nist2014sp800162 | tecnico | 2026-10-29 |
