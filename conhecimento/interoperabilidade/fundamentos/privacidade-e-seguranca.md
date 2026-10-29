---
id: iop.fund.privacidade-e-seguranca
titulo: Privacidade, consentimento e segurança na troca de dados educacionais
tipo: conceito
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, imsglobal2019lti13, imsglobal2019ltinrps, imsglobal2026ob30, imsglobal2025clr20, aicc2016cmi5, adl2016xapidata]
relacoes:
  - { tipo: complementa, alvo: iop.fund.identidade-e-contexto }
  - { tipo: depende-de, alvo: iop.br.lgpd }
  - { tipo: relacionado-a, alvo: iop.cred.verifiable-credentials }
termos: [minimização, finalidade, consentimento, escopo OAuth, dado pessoal sensível, pseudonimização]
---

# Privacidade e segurança

## Definição e terminologia

Em interoperabilidade educacional, privacidade não é um módulo acoplado no fim: é uma restrição sobre **quais campos atravessam a fronteira entre sistemas**, sob **que base legal** e **por quanto tempo** [I].

A LGPD define dado pessoal como informação relacionada a pessoa natural identificada ou identificável, e dado pessoal sensível como aquele sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a organização, saúde ou vida sexual, dado genético ou biométrico, quando vinculado a pessoa natural [F: brasil2018lgpd, art. 5, I e II]. Entre os princípios do art. 6 estão finalidade (propósitos legítimos, específicos, explícitos e informados, sem tratamento posterior incompatível), adequação (compatibilidade com as finalidades informadas) e necessidade (limitação ao mínimo necessário, com dados pertinentes, proporcionais e não excessivos) [F: brasil2018lgpd, art. 6].

## Problema que resolve

Padrões de interoperabilidade facilitam a troca por construção. Sem limite explícito, o caminho de menor esforço é enviar tudo que o esquema permite — e o esquema permite muito [I].

## Fundamentos e funcionamento

**Mecanismos de controle presentes nos padrões consultados:**

- **Transporte protegido**: o LTI 1.3 exige HTTPS com TLS para mensagens e serviços, e para todas as URLs contidas neles [F: imsglobal2019lti13, §3.5].
- **Autenticação de serviço**: as ferramentas obtêm tokens de acesso pelo perfil JWT de autenticação de cliente OAuth 2.0, e `iss` e `sub` do client assertion devem ser ambos o `client_id` da ferramenta [F: imsglobal2019lti13, §6.2].
- **Escopos como limite de finalidade**: o NRPS define o escopo `.../lti-nrps/scope/contextmembership.readonly`, que autoriza apenas GET sobre a URL de membros do contexto [F: imsglobal2019ltinrps]. O escopo é o instrumento técnico que implementa o princípio da necessidade [I].
- **Divulgação condicionada a consentimento**: no NRPS, atributos como nome e e-mail só são compartilhados pela plataforma mediante consentimento [F: imsglobal2019ltinrps].
- **Minimização no lançamento**: a especificação cmi5 orienta que o objeto `actor` passado na URL de lançamento não contenha informação pessoal sensível [F: aicc2016cmi5].
- **Identificação mínima**: o LTI exige que a ferramenta identifique usuários apenas pelo identificador único, e não por outros atributos [F: imsglobal2019lti13, §3.3].
- **Credenciais sob controle do titular**: Open Badges 3.0 e CLR 2.0 usam OAuth 2.0 Authorization Code Grant para as APIs, o que coloca o titular no fluxo de autorização [F: imsglobal2026ob30; imsglobal2025clr20].

**Imutabilidade versus direito de eliminação.** O xAPI parte do princípio de que declarações são permanentes, e a única forma suportada de desfazer é o *voiding* [F: adl2016xapidata]. Isso tensiona com o direito de eliminação previsto na LGPD [I]. A saída usual é separar o registro de evento (pseudonimizado, permanente) da tabela de resolução de identidade (eliminável) — ver `iop.fund.identidade-e-contexto` [I].

**Dados de crianças.** A LGPD exige que o tratamento de dados de crianças e adolescentes atenda ao melhor interesse, e que, para crianças, haja consentimento específico e em destaque de pelo menos um dos pais ou responsável legal, com esforços razoáveis de verificação pelo controlador [F: brasil2018lgpd, art. 14]. Em contexto escolar, isso afeta diretamente quais atributos podem ser repassados a ferramentas de terceiros [I].

**Dados de saúde e funcionalidade.** Informação de saúde é dado sensível [F: brasil2018lgpd, art. 5, II]. Qualquer troca que use CIF ou FHIR (ver `iop.health.cif`, `iop.health.fhir`) entra nesse regime, com base legal própria [I].

## Requisitos e pressupostos

- Há um mapa de quais campos saem por cada integração, com finalidade declarada por campo. Sem esse mapa, não há como demonstrar necessidade [I].
- Escopos são concedidos por integração, não globalmente.
- Retenção é definida por tipo de registro, e o apagamento é testado.

## Vantagens e limitações

Os padrões consultados oferecem bons instrumentos para a camada técnica (TLS, OAuth, escopos) e instrumentos fracos para a camada jurídica: nenhum deles carrega, no próprio payload, a finalidade do tratamento ou a base legal invocada [I]. Essa lacuna é preenchida fora do padrão, por contrato.

## Alternativas e comparações

| Estratégia | Efeito sobre risco | Custo |
|---|---|---|
| Enviar identificador direto (e-mail) | alto | nenhum |
| Pseudonimizar com `account` opaco | médio-baixo | serviço de resolução |
| Agregar antes de enviar | baixo | perde análise individual |
| Processar na borda e enviar só o resultado | baixo | arquitetura mais complexa |

## Métricas e métodos de avaliação

Número de campos pessoais por integração ativa; proporção de integrações com escopo mínimo; tempo entre pedido de eliminação e apagamento efetivo; resultado de teste de reidentificação sobre a base pseudonimizada [I].

## Relações com outros conceitos

Complementa `iop.fund.identidade-e-contexto` (a escolha do identificador é a decisão de privacidade mais consequente) e depende de `iop.br.lgpd` para o regime jurídico brasileiro.

## Lacunas e questões abertas

- Não foram consultados os guias de privacidade do 1EdTech (rubrica de privacidade do TrustEd Apps); a página retornou 404.
- Falta documento sobre retenção e anonimização de bases de eventos — tema de fronteira com `dados-pesquisa-e-eventos`.
- Não foi verificado o regime aplicável a dados de alunos em pesquisa acadêmica (art. 7 da LGPD, hipótese de estudo por órgão de pesquisa com anonimização sempre que possível) [F: brasil2018lgpd, art. 7].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| imsglobal2019lti13 | normativo | 2026-10-29 |
| imsglobal2019ltinrps | normativo | 2026-10-29 |
| imsglobal2026ob30 | normativo | 2026-10-29 |
| imsglobal2025clr20 | normativo | 2026-10-29 |
| aicc2016cmi5 | normativo | 2026-10-29 |
| adl2016xapidata | normativo | 2026-10-29 |
