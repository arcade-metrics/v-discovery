---
id: iop.tool.lti-advantage
titulo: LTI Advantage (NRPS, AGS, Deep Linking)
tipo: protocolo
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2019ltinrps, imsglobal2019ltiags, imsglobal2019ltidl, edtech2026lti, imsglobal2019lti13]
relacoes:
  - { tipo: depende-de, alvo: iop.tool.lti-core }
  - { tipo: complementa, alvo: iop.ros.oneroster }
  - { tipo: relacionado-a, alvo: iop.fund.privacidade-e-seguranca }
termos: [NRPS, AGS, Deep Linking, line item, score, membership, content item]
---

# LTI Advantage

## Definição e terminologia

LTI Advantage é o conjunto de serviços que se somam ao lançamento do LTI 1.3. A página do padrão lista três: Assignment and Grade Services (AGS) 2.0, para criar colunas de nota e publicar notas ligadas a um recurso; Names and Role Provisioning Services (NRPS) 2.0, para dados de usuários e seus papéis dentro de organizações; e Deep Linking (DL) 2.0, para o usuário selecionar e compartilhar conteúdo específico de uma ferramenta externa [F: edtech2026lti].

As três especificações consultadas são **Final Release de 16 de abril de 2019** [F: imsglobal2019ltinrps; imsglobal2019ltiags; imsglobal2019ltidl].

## Problema que resolve

O Core resolve "quem é o usuário e em que contexto ele está". Sobram três perguntas: quem mais está na turma (NRPS), como devolver a nota (AGS) e como o professor escolhe *qual* conteúdo da ferramenta vai no link (Deep Linking) [I].

## Fundamentos e funcionamento

### Names and Role Provisioning Services 2.0

A plataforma expõe um endpoint de memberships; a URL (`context_memberships_url`) chega pelo claim `https://purl.imsglobal.org/spec/lti-nrps/claim/namesroleservice` do lançamento LTI 1.3. A membership de um Resource Link usa o mesmo endpoint com o parâmetro `rlid`. A única ação definida é GET [F: imsglobal2019ltinrps].

- Media type: `application/vnd.ims.lti-nrps.v2.membershipcontainer+json`, no header Accept.
- Escopo: `https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly`, que autoriza GET sobre a URL de memberships.
- Retorno: objeto `context` com `id` obrigatório; lista de `members`, cada um com `user_id` e `roles` (URIs) obrigatórios e `status` `Active` ou `Inactive` (ausente implica `Active`; `Deleted` só aparece em relatórios de diferença). Atributos como nome e e-mail só são compartilhados com consentimento.
- Paginação por link `rel="next"`; link `rel="differences"` fornece relatório de mudanças desde a criação da URL [F: imsglobal2019ltinrps].

### Assignment and Grade Services 2.0

Substitui o Basic Outcomes do LTI 1.1 e atualiza o Result service do LTI 2.0 [F: imsglobal2019ltiags]. Três subserviços:

| Subserviço | Operação | Observação |
|---|---|---|
| LineItem | CRUD de colunas de nota | depende do escopo concedido |
| Score | escrita de notas | somente escrita |
| Result | leitura das notas correntes | somente leitura |

O claim de serviço é `https://purl.imsglobal.org/spec/lti-ags/claim/endpoint`, com as propriedades `lineitems`, `lineitem` e `scope`. A URL `lineitems` é o contêiner do contexto (GET com filtros, POST para criar); a URL `lineitem` é um item individual (GET, PUT, DELETE); a `id` do line item serve de base para POST de score e GET de result [F: imsglobal2019ltiags].

Media types: `application/vnd.ims.lis.v2.lineitem+json`, `application/vnd.ims.lis.v2.lineitemcontainer+json`, `application/vnd.ims.lis.v1.score+json`. Escopos: `.../scope/lineitem` (gestão completa), `.../scope/lineitem.readonly`, `.../scope/result.readonly` e `.../scope/score`. Campos visíveis de Score: `timestamp`, `activityProgress`, `gradingProgress`, `userId`, `scoreGiven`, `scoreMaximum` [F: imsglobal2019ltiags].

### Deep Linking 2.0

Dois tipos de mensagem, ambas JWT assinado: `LtiDeepLinkingRequest` (plataforma → ferramenta, inicia a seleção) e `LtiDeepLinkingResponse` (ferramenta → plataforma, com os itens selecionados ou criados) [F: imsglobal2019ltidl].

Tipos de content item [F: imsglobal2019ltidl]:

- `link`: URL totalmente qualificada, com opções de renderização (window, iframe, embed).
- `ltiResourceLink`: link para recurso LTI, em geral da mesma ferramenta, podendo incluir line item e configurações de disponibilidade.
- `file`: arquivo transferido da ferramenta para a plataforma, com URL de vida curta.
- `html`: fragmento HTML para embutir, que a plataforma deve sanitizar.
- `image`: URL de imagem, renderizada diretamente.

Fluxo: a plataforma redireciona o navegador do usuário ao endpoint da ferramenta com a requisição de deep linking, indicando os tipos aceitos; a ferramenta apresenta sua própria interface de seleção ou criação; a ferramenta devolve o navegador ao `deep_link_return_url` da plataforma por form POST autossubmetido, com um JWT contendo os itens — o que deve ocorrer mesmo quando nenhum item é selecionado [F: imsglobal2019ltidl].

## Requisitos e pressupostos

- O lançamento LTI 1.3 já funciona e a ferramenta obtém access tokens pelo fluxo OAuth 2 descrito em `iop.tool.lti-core` [F: imsglobal2019lti13, §6.2].
- Os escopos necessários foram concedidos no registro da ferramenta; sem `.../scope/score`, não há como publicar nota.

## Vantagens e limitações

Vantagens [I]: cobre o ciclo completo de uma atividade avaliada sem acoplar a ferramenta ao modelo de dados do LMS; escopos por serviço implementam o princípio da necessidade (ver `iop.fund.privacidade-e-seguranca`).

Limitações [I]:
- NRPS é somente leitura e por contexto; não serve como fonte de rostering institucional (para isso, `iop.ros.oneroster`).
- AGS modela coluna de nota, não rubrica nem competência; avaliação por critérios exige QTI ou CLR.
- O suporte a cada serviço varia por LMS; "suporta LTI 1.3" não implica suportar os três.

## Alternativas e comparações

| Necessidade | LTI Advantage | Alternativa |
|---|---|---|
| Lista de alunos de uma turma | NRPS (leitura, por contexto) | OneRoster (lote institucional) |
| Devolver nota | AGS Score | OneRoster Gradebook |
| Escolher conteúdo | Deep Linking | Common Cartridge (pacote estático) |

## Métricas e métodos de avaliação

Certificação do LTI Advantage pelo 1EdTech, com suíte de diagnóstico e certificação [F: edtech2026lti]. Em produção: taxa de erro por serviço e latência da publicação de nota [I].

## Relações com outros conceitos

Depende de `iop.tool.lti-core`. Complementa `iop.ros.oneroster`, que resolve rostering em lote, enquanto NRPS resolve a consulta pontual no contexto do lançamento.

## Lacunas e questões abertas

- O corpo completo da especificação AGS (notadamente as seções de Score e Result) não foi lido; detalhes de `activityProgress`/`gradingProgress` permanecem parcialmente verificados.
- Não foi verificado se há versões posteriores a 2.0 de qualquer dos três serviços.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2019ltinrps | normativo | 2026-10-29 |
| imsglobal2019ltiags | normativo | 2026-10-29 |
| imsglobal2019ltidl | normativo | 2026-10-29 |
| imsglobal2019lti13 | normativo | 2026-10-29 |
| edtech2026lti | fornecedor | 2026-10-29 |
