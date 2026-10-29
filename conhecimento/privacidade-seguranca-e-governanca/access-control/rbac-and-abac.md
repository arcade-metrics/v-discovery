---
id: psg.access.rbac-and-abac
titulo: Modelos de controle de acesso: RBAC, ABAC e ReBAC
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ferraiolokuhn1992rbac, sandhu1996rbacmodels, nist2014sp800162, nist2020sp80053r5, pang2019zanzibar, nist2026rbacproject, incits2012rbac]
relacoes:
  - { tipo: complementa, alvo: psg.access.school-roles }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: depende-de, alvo: iop.fund.identidade-e-contexto }
  - { tipo: relacionado-a, alvo: rtm.sec.authentication }
  - { tipo: relacionado-a, alvo: psg.audit.audit-trails }
termos: [controle de acesso, RBAC, ABAC, ReBAC, papel, permissão, sessão, hierarquia de papéis, menor privilégio, separação de deveres, atributo, política digital, PDP, PEP, tupla de relação, explosão de papéis]
---

# Modelos de controle de acesso: RBAC, ABAC e ReBAC

## Definição e terminologia

Controle de acesso é o mecanismo que decide se um sujeito (usuário ou processo agindo por ele) pode executar uma operação sobre um objeto (registro, arquivo, função). O NIST SP 800-53 descreve a aplicação de acesso (access enforcement) como o controle "between active entities or subjects (i.e., users or processes acting on behalf of users) and passive entities or objects (i.e., devices, files, records, domains)" [F: nist2020sp80053r5, AC-3]. A decisão de acesso e a sua aplicação podem ficar em componentes distintos: o SP 800-53 separa explicitamente access control decisions (AC-24) de access enforcement (AC-3) [F: nist2020sp80053r5, AC-24].

Três famílias de modelo organizam a literatura consultada:

- **RBAC** (role-based access control): decisões baseadas nas funções que um usuário pode exercer na organização; "a role can be thought of as a set of transactions that a user or set of users can perform within the context of an organization" [F: ferraiolokuhn1992rbac, §2]. Sandhu et al. definem papel como "a job function or job title within the organization with some associated semantics regarding the authority and responsibility conferred on a member of the role" [F: sandhu1996rbacmodels, §4.1].
- **ABAC** (attribute-based access control): "an access control method where subject requests to perform operations on objects are granted or denied based on assigned attributes of the subject, assigned attributes of the object, environment conditions, and a set of policies that are specified in terms of those attributes and conditions" [F: nist2014sp800162, §2.2].
- **ReBAC** (relationship-based access control): a autorização deriva de relações armazenadas entre usuários e objetos e entre objetos. O sistema Zanzibar, descrito pelo Google, representa listas de controle de acesso como tuplas `object#relation@user`, em que o usuário pode ser um identificador ou um userset (`object#relation`), o que permite grupos aninhados e herança entre objetos [F: pang2019zanzibar, §2.1]. O termo ReBAC não aparece no artigo; é o nome pelo qual a literatura se refere a esse estilo [I].

O que RBAC não é: não é a lista de grupos do sistema operacional. Para Sandhu et al., um grupo costuma ser só uma coleção de usuários, enquanto um papel é "both a collection of users on one side and a collection of permissions on the other", intermediário entre os dois conjuntos [F: sandhu1996rbacmodels, §3]. Também não se confunde com MAC e DAC: Ferraiolo e Kuhn classificam RBAC como forma de controle não discricionário, porque "the users cannot pass access permissions on to other users at their discretion" [F: ferraiolokuhn1992rbac, §2]; Sandhu et al. consideram RBAC neutro em relação a política, podendo coexistir com MAC e DAC [F: sandhu1996rbacmodels, §3].

## Problema que resolve

Em organizações onde o usuário final não "possui" a informação que acessa, o controle discricionário (DAC) deixa a concessão de acessos à vontade de cada usuário; Ferraiolo e Kuhn argumentam que, nesses casos, a corporação ou agência é a dona dos objetos e o controle deve se basear em funções, administrado centralmente [F: ferraiolokuhn1992rbac, §1-2, §7]. Uma escola ou rede de ensino é exatamente esse caso: o professor não é dono dos dados do aluno, e o acesso decorre da função exercida [I].

O problema que ABAC resolve é outro: o SP 800-162 observa que RBAC "does not easily support multi-factor decisions" como localização física ou treinamento recente, e que tentar expressá-las em papéis gera "numerous roles that are ad hoc and limited in membership", a chamada "role explosion" [F: nist2014sp800162, §2.1]. ReBAC, por sua vez, surge quando a autorização depende de relações entre objetos (documento dentro de pasta, membro de grupo que é membro de outro grupo) e de consistência global dessas relações [F: pang2019zanzibar, §1].

## Fundamentos e funcionamento

**RBAC formal (1992).** Ferraiolo e Kuhn enunciam três regras: atribuição de papel (um sujeito só executa transações se tiver um papel ativo), autorização de papel (o papel ativo deve estar entre os autorizados para o sujeito) e autorização de transação (a transação deve estar autorizada para o papel ativo) [F: ferraiolokuhn1992rbac, §3]. Os autores admitem uma quarta regra opcional, que controla o modo de acesso (leitura, escrita, inclusão) de uma transação a um objeto, útil para requisitos de confidencialidade, e dão o exemplo do médico com leitura e escrita no arquivo de prescrições e do farmacêutico só com leitura [F: ferraiolokuhn1992rbac, §3].

**Família RBAC0-RBAC3 (1996).** Sandhu et al. definem quatro modelos de referência: RBAC0 (usuários, papéis, permissões e sessões, com as relações muitos-para-muitos UA, usuário-papel, e PA, permissão-papel), RBAC1 (acrescenta hierarquia de papéis, uma ordem parcial em que o papel sênior herda as permissões do júnior), RBAC2 (acrescenta restrições, como papéis mutuamente exclusivos) e RBAC3 (consolida os dois) [F: sandhu1996rbacmodels, §4]. A sessão é a ativação, pelo usuário, de um subconjunto de seus papéis; as permissões disponíveis são a união das permissões dos papéis ativos, e o fato de poder manter um papel poderoso desativado "supports the principle of least privilege" [F: sandhu1996rbacmodels, §4.1]. O modelo prevê papéis privados para impedir que permissões de um papel júnior subam pela hierarquia quando isso não é desejável, por exemplo para trabalho em andamento que o supervisor não deve ver [F: sandhu1996rbacmodels, §4.2].

**Padronização.** O NIST informa que seu modelo foi adotado como ANSI/INCITS 359-2004 em 11 de fevereiro de 2004 e revisado como INCITS 359-2012, composto de duas partes: o RBAC Reference Model e o RBAC System and Administrative Functional Specification [F: nist2026rbacproject]. O texto da norma não foi acessado nesta sessão [F: incits2012rbac, metadados].

**ABAC (SP 800-162).** Os elementos são atributos de sujeito, atributos de objeto, condições de ambiente (hora, dia, localização, nível de ameaça) e política; o mecanismo de controle de acesso (ACM) avalia regras, atributos do sujeito, atributos do objeto e condições de ambiente para computar a decisão [F: nist2014sp800162, §2.2]. Na implantação em escala, o guia distingue política em linguagem natural (NLP), política digital (DP, regras compiláveis em código executável) e metapolítica (MP, política sobre prioridade e conflito entre políticas), e descreve os pontos funcionais PEP (aplicação), PDP (decisão), PIP (informação) e PAP (administração) [F: nist2014sp800162, §2.4]. O guia adverte que a responsabilização pode se perder se as decisões forem baseadas em atributos sem rastrear o identificador do sujeito em cada decisão [F: nist2014sp800162, §2.3].

**ReBAC (Zanzibar).** As relações efetivas não vêm só das tuplas armazenadas: userset rewrite rules declaradas por namespace permitem relações concêntricas (todo owner é editor, todo editor é viewer) e herança via objeto pai ("look up the parent folder of the document and inherit its viewers") [F: pang2019zanzibar, §2.3.1]. O artigo destaca o problema do "new enemy": se a ordem entre remover um usuário de uma ACL e alterar o conteúdo não for respeitada, o usuário removido pode ver conteúdo novo; a solução descrita combina consistência externa com leituras de snapshot limitadas por um token (zookie) [F: pang2019zanzibar, §2.2].

**Controles do SP 800-53 rev. 5.** A família AC traz RBAC e ABAC como aprimoramentos de AC-3: AC-3(7) exige aplicar política RBAC sobre sujeitos e objetos definidos, e explica que privilégios "are instead acquired through role assignments"; AC-3(13) exige política ABAC baseada em atributos organizacionais, de ação, de ambiente e de recurso [F: nist2020sp80053r5, AC-3(7), AC-3(13)]. AC-5 (separação de deveres) e AC-6 (menor privilégio) são controles independentes: AC-6 manda "allowing only authorized accesses for users (or processes acting on behalf of users) that are necessary to accomplish assigned organizational tasks" [F: nist2020sp80053r5, AC-5, AC-6]. AC-16 trata de atributos de segurança e de privacidade vinculados à informação, incluindo "personally identifiable information processing permissions, including individual consent" [F: nist2020sp80053r5, AC-16]. AC-24(2) prevê decisões de acesso baseadas em atributos que não incluem a identidade do usuário, para casos em que preservar a privacidade individual é prioritário [F: nist2020sp80053r5, AC-24(2)].

## Requisitos e pressupostos

- RBAC pressupõe que funções organizacionais sejam estáveis e enumeráveis; Sandhu et al. relatam que permissões por papel mudam devagar em comparação com a filiação de usuários a papéis [F: sandhu1996rbacmodels, §2].
- ABAC pressupõe atributos de sujeito e de objeto definidos, mantidos por autoridades de atributo, com nomes e valores normalizados entre organizações; "without a sufficient set of object and subject attributes, ABAC does not work" [F: nist2014sp800162, §2.4.2].
- ReBAC pressupõe que as relações estejam armazenadas de forma consistente e que a ordem causal entre mudanças de ACL e de conteúdo seja respeitada [F: pang2019zanzibar, §2.2].
- Todos pressupõem autenticação prévia: Ferraiolo e Kuhn excluem o login do conceito de transação [F: ferraiolokuhn1992rbac, §3]. A autenticação em canais de tempo real fica em `rtm.sec.authentication`.

## Vantagens e limitações

| Modelo | Vantagens documentadas | Limitações documentadas |
|---|---|---|
| RBAC | Administração centralizada: entrada, mudança de função e saída de pessoas viram concessão e revogação de filiação a papéis [F: ferraiolokuhn1992rbac, §4]; suporta menor privilégio, separação de deveres e abstração de dados [F: sandhu1996rbacmodels, §2]; é fácil saber quem tem acesso a quê, pois a decisão vem de papéis e não de regras distribuídas [I] | Não suporta bem decisões multifatoriais nem contexto dinâmico; risco de explosão de papéis [F: nist2014sp800162, §2.1]; não controla sequências de operações [F: sandhu1996rbacmodels, §2]; RBAC não garante por si os princípios que suporta, pois o administrador pode configurá-lo violando-os [F: sandhu1996rbacmodels, §2] |
| ABAC | Acomoda o "usuário externo inesperado" sem pré-provisionar identidade; regras e objetos não mudam quando novos sujeitos entram [F: nist2014sp800162, §2.3]; granularidade fina (projeto, horário) [F: nist2014sp800162, §3.1.2.1, nota 3] | Custo de desenvolvimento e manutenção pode exceder o benefício; auditoria "antes do fato" (quem tem acesso a este objeto?) exige simular a decisão para cada sujeito [F: nist2014sp800162, §3.1.2.1, §3.1.2.3]; raiz de confiança distribuída entre autoridades de atributo [F: nist2014sp800162, §3.1.2.5] |
| ReBAC | Expressa compartilhamento por relação (dono, editor, leitor) e herança via hierarquia de objetos com um só modelo de dados [F: pang2019zanzibar, §2.1, §2.3] | A consistência das relações é um problema de sistemas distribuídos (new enemy), e o Expand para enumerar quem tem acesso exige seguir referências indiretas [F: pang2019zanzibar, §2.2, §2.4.5] |

## Alternativas e comparações

Os três modelos não são excludentes. O SP 800-53 descreve RBAC e ABAC como enhancements alternativos de um mesmo controle, implementáveis como forma mandatória ou discricionária [F: nist2020sp80053r5, AC-3(7), AC-3(13)]. O SP 800-162 nota que ABAC "is not the right solution for every access control problem", mas é viável "for environments where subjects and objects carry a rich set of attributes and access decisions involve complex relationships among these attributes" [F: nist2014sp800162, §3.1.2.1]. Em uma plataforma escolar, a combinação típica é RBAC para o vocabulário de funções (quem é professor, quem é responsável), com atributos de contexto (turma, ano letivo, vínculo ativo) e relações (responsável-de, regente-de) decidindo o escopo; a comparação aplicada aos papéis escolares está em `psg.access.school-roles` [I].

## Métricas e métodos de avaliação

O SP 800-162 identifica duas capacidades de revisão: saber que acessos cada indivíduo tem antes de qualquer pedido (before the fact audit) e saber quem tem acesso a um objeto; ambas são diretas em RBAC e custosas em ABAC [F: nist2014sp800162, §3.1.2.3]. O SP 800-53 exige auditar mudanças em atributos (AC-16e) e revisar periodicamente sua aplicabilidade (AC-16f) [F: nist2020sp80053r5, AC-16]. Zanzibar reporta latência de 95º percentil inferior a 10 ms e disponibilidade acima de 99,999% em três anos de produção, métricas típicas de um serviço de autorização em linha [F: pang2019zanzibar, abstract].

## Exemplo técnico independente de domínio

```
# RBAC0 (Sandhu et al.): UA ⊆ U×R, PA ⊆ P×R; sessão ativa um subconjunto de papéis
permitido(sessao, perm) := ∃ r ∈ papeis_ativos(sessao) : (perm, r) ∈ PA

# ABAC (SP 800-162): política em termos de atributos e condições de ambiente
regra ler_prontuario:
  permitir se sujeito.tipo == "equipe_clinica"
          e objeto.tipo == "prontuario"
          e objeto.unidade == sujeito.unidade
          e ambiente.hora ∈ expediente

# ReBAC (notação de Zanzibar): tuplas object#relation@user
pasta:A#viewer@grupo:turma1#member      # membros da turma veem a pasta
doc:relatorio#parent@pasta:A            # o documento está na pasta A
# rewrite: viewer(doc) = this ∪ editor(doc) ∪ viewer(parent(doc))
check(doc:relatorio#viewer, usuario_42) -> true se usuario_42 ∈ grupo:turma1#member
```

## Relações com outros conceitos

Complementa `psg.access.school-roles`, que aplica estes modelos ao vocabulário de papéis escolares, e `psg.access.minimization-and-privacy-by-design`, onde o menor privilégio reaparece como decisão de esquema. Depende de `iop.fund.identidade-e-contexto`, que descreve como identidade, papel e contexto chegam pelos padrões de interoperabilidade. Relaciona-se com `rtm.sec.authentication` (autenticação, pressuposto de qualquer decisão de acesso) e com `psg.audit.audit-trails` (registro das decisões, exigido pela responsabilização discutida no SP 800-162).

## Lacunas e questões abertas

- O texto da INCITS 359-2012 não foi acessado; a descrição de suas partes vem da página do projeto do NIST. Verificar se a edição vigente é a reafirmação de 2022 mencionada em catálogos de normas (não verificada).
- O artigo de Sandhu et al. foi lido na versão de pré-publicação hospedada pelo NIST (revisada em outubro de 1995); a paginação da versão IEEE Computer não foi conferida.
- O SP 800-162 inclui atualizações "as of 08-02-2019" (errata); não foi verificado quais seções mudaram em relação à edição de janeiro de 2014.
- A comparação formal de expressividade entre RBAC, ABAC e ReBAC (por exemplo, se ReBAC é redutível a ABAC com atributos relacionais) não foi coberta por fonte primária nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ferraiolokuhn1992rbac | academico | 2026-10-29 |
| sandhu1996rbacmodels | academico | 2026-10-29 |
| nist2014sp800162 | tecnico | 2026-10-29 |
| nist2020sp80053r5 | normativo | 2026-10-29 |
| pang2019zanzibar | academico | 2026-10-29 |
| nist2026rbacproject | tecnico | 2026-10-29 |
| incits2012rbac | normativo [metadados] | 2026-10-29 |
