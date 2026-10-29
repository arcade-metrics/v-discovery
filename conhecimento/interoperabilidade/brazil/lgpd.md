---
id: iop.br.lgpd
titulo: LGPD aplicada à troca de dados educacionais
tipo: conceito
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd]
relacoes:
  - { tipo: complementa, alvo: iop.fund.privacidade-e-seguranca }
  - { tipo: complementa, alvo: iop.br.educacenso }
  - { tipo: relacionado-a, alvo: iop.fund.identidade-e-contexto }
termos: [dado pessoal, dado sensível, base legal, consentimento, finalidade, necessidade, melhor interesse]
---

# LGPD aplicada à interoperabilidade educacional

## Definição e terminologia

A Lei 13.709, de 14 de agosto de 2018, é a Lei Geral de Proteção de Dados Pessoais [F: brasil2018lgpd].

**Definições relevantes (art. 5)** [F: brasil2018lgpd]: dado pessoal é "informação relacionada a pessoa natural identificada ou identificável" (inciso I); dado pessoal sensível abrange origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou organização, dado referente à saúde ou à vida sexual, e dado genético ou biométrico, quando vinculado a pessoa natural (inciso II).

**Princípios (art. 6)** [F: brasil2018lgpd]: o tratamento observa a boa-fé e, entre outros, os princípios da **finalidade** (propósitos legítimos, específicos, explícitos e informados ao titular, sem tratamento posterior incompatível), da **adequação** (compatibilidade do tratamento com as finalidades informadas, conforme o contexto) e da **necessidade** (limitação ao mínimo necessário, com dados pertinentes, proporcionais e não excessivos).

**Bases legais (art. 7)** [F: brasil2018lgpd]: consentimento do titular; cumprimento de obrigação legal ou regulatória; execução de políticas públicas pela administração pública; realização de estudos por órgão de pesquisa, com anonimização sempre que possível; execução de contrato; exercício regular de direitos em processo; proteção da vida ou da incolumidade física; tutela da saúde; proteção do crédito; e legítimo interesse do controlador, salvo quando prevalecerem direitos e liberdades fundamentais do titular.

**Crianças e adolescentes (art. 14)** [F: brasil2018lgpd]: o tratamento deve atender ao melhor interesse; para crianças, exige consentimento específico e em destaque de pelo menos um dos pais ou responsável legal, e o controlador deve empreender esforços razoáveis para verificar esse consentimento.

## Problema que resolve

Define quais trocas são lícitas. Em educação básica pública, com titulares que são crianças, essa é a restrição mais forte sobre o desenho de qualquer integração [I].

## Fundamentos e funcionamento

**Consequências diretas para o desenho de integrações** [I]:

1. **Escolha da base legal antes da arquitetura.** Escola pública operando política pública e escola privada operando contrato invocam bases diferentes [F: brasil2018lgpd, art. 7], com implicações distintas sobre o que pode ser repassado a fornecedores.
2. **O princípio da necessidade** [F: brasil2018lgpd, art. 6] tem tradução técnica direta: escopos OAuth mínimos, pseudonimização de identificadores, e recusa de campos que o fornecedor pede "por via das dúvidas" (ver `iop.fund.privacidade-e-seguranca`).
3. **O princípio da finalidade** [F: brasil2018lgpd, art. 6] proíbe o reuso incompatível: dados coletados para acompanhamento pedagógico não migram automaticamente para pesquisa sem tratar a questão da base legal — a lei prevê hipótese própria para estudo por órgão de pesquisa, com anonimização sempre que possível [F: brasil2018lgpd, art. 7].
4. **Dados de saúde e funcionalidade são sensíveis** [F: brasil2018lgpd, art. 5, II]: perfis que incorporem informação clínica ou de diagnóstico (ver `iop.health.cif`) estão em regime mais estrito.
5. **Consentimento parental verificável** [F: brasil2018lgpd, art. 14] é requisito de produto, não apenas de contrato: o fluxo precisa existir no sistema.

## Requisitos e pressupostos

- Há registro de quais campos saem em cada integração, com finalidade e base legal declaradas por integração.
- Existe fluxo de consentimento parental quando a base legal for o consentimento.
- Dados pseudonimizados têm a tabela de reidentificação sob controle e com retenção definida.

## Vantagens e limitações

Limitação deste documento [I]: é uma leitura dos artigos citados aplicada à interoperabilidade, não parecer jurídico. Decisões concretas sobre base legal exigem análise do caso e do papel de cada parte (controlador, operador).

## Relações com outros conceitos

Complementa `iop.fund.privacidade-e-seguranca` (que trata dos mecanismos técnicos) e `iop.br.educacenso` (envio obrigatório, que corre sob base legal de obrigação legal).

## Lacunas e questões abertas

- Artigos sobre papéis de controlador e operador, relatório de impacto, transferência internacional e sanções não foram cobertos (leitura parcial do texto da lei).
- Regulamentações e orientações da ANPD sobre dados de crianças em contexto escolar: não consultadas.
- Interação com o Marco Civil da Internet e com normas do setor educacional: não investigada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
