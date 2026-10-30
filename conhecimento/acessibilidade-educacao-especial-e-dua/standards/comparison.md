---
id: acs.std.comparison
titulo: Comparação das normas e diretrizes de acessibilidade digital
tipo: comparacao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2024wcag22, w3c2026wcag3intro, iso405002025, w3c2021cogausable, w3c2023aria12, iso2475122008, imsglobal2021afapnp, edtech2026accessibility, etsi2026en301549, accessboard2017section508, gameaccessibility2026fulllist, microsoft2023xag, ablegamers2022apx]
relacoes:
  - { tipo: relacionado-a, alvo: acs.std.wcag }
  - { tipo: relacionado-a, alvo: acs.std.wai-aria }
  - { tipo: relacionado-a, alvo: acs.std.accessforall-iso-24751 }
  - { tipo: relacionado-a, alvo: acs.std.procurement-en-301-549-and-section-508 }
  - { tipo: relacionado-a, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: relacionado-a, alvo: acs.br.emag-and-nbr-17225 }
  - { tipo: relacionado-a, alvo: iop.fund.conformidade-e-certificacao }
termos: [norma de conformidade, especificação de semântica, perfil de preferências, norma de compra, diretriz de jogo, obrigatoriedade, cobertura cognitiva, exceção de essencial, camadas de acessibilidade]
---

# Comparação das normas e diretrizes de acessibilidade digital

## Definição e terminologia

Os cinco documentos desta área não competem: respondem a perguntas diferentes. A WCAG diz quando um conteúdo é acessível; a WAI-ARIA diz como expor semântica a tecnologias assistivas; a AccessForAll (ISO/IEC 24751) diz como casar um recurso com a pessoa; a EN 301 549 e a Section 508 dizem o que se exige em compra e regulação; as diretrizes de jogos dizem como tornar a jogabilidade ajustável. A comparação abaixo usa os critérios pedidos no plano: escopo, obrigatoriedade, cobertura cognitiva e aplicabilidade a jogos [I].

## Problema que resolve

Evita dois erros comuns: tratar conformidade WCAG como garantia de acesso, e tratar diretrizes de jogos ou perfis de preferência como substitutos da conformidade. Cada camada cobre lacunas da anterior [I].

## Alternativas e comparações

### Visão geral

| Documento | Mantenedor | Versão vigente | Natureza | Obrigatoriedade |
|---|---|---|---|---|
| WCAG 2.2 (`acs.std.wcag`) | W3C | Recommendation 2023, reeditada 12/12/2024; ISO/IEC 40500:2025 | norma de conformidade de conteúdo | só quando lei ou contrato a incorpora [F: w3c2024wcag22; iso405002025, metadados] |
| WCAG 3 | W3C | Working Draft 10/09/2026 | rascunho | nenhuma; "a few more years" [F: w3c2026wcag3intro] |
| WAI-ARIA 1.2 + APG (`acs.std.wai-aria`) | W3C | Recommendation 06/06/2023 | especificação de semântica | meio, não fim [F: w3c2023aria12] |
| ISO/IEC 24751 / AfA (`acs.std.accessforall-iso-24751`) | ISO/IEC JTC 1/SC 36; 1EdTech | partes 1 a 3 (2008), 4 (2023); AfA 2.0 Final, 3.0 rascunho | modelo de perfil e de descrição de recurso | voluntária [F: iso2475122008, metadados; edtech2026accessibility] |
| EN 301 549 (`acs.std.procurement-en-301-549-and-section-508`) | ETSI, CEN, CENELEC | V4.1.1 (2026-09) | norma harmonizada de TIC | presunção de conformidade com diretivas da UE [F: etsi2026en301549, prefácio] |
| Section 508 | US Access Board | Revised Standards 2017 | regra federal | obrigatória para agências federais dos EUA [F: accessboard2017section508] |
| GAG, XAG, APX (`acs.std.game-accessibility-guidelines`) | coletivo; fornecedor; AbleGamers | GAG sem versão; XAG 3.2 (2023); APX | diretrizes de projeto | voluntárias; a XAG recusa papel de checklist legal [F: microsoft2023xag] |

### Escopo

| Documento | Web | Software não web | Documentos | Hardware | Jogabilidade |
|---|---|---|---|---|---|
| WCAG 2.2 | sim | por analogia [I] | por analogia [I] | não | não (exceção de essencial) |
| WAI-ARIA | sim | não | não | não | não |
| AfA / 24751 | recursos de aprendizagem digitais | sim | sim | não | indireto [I] |
| EN 301 549 | cl. 9 | cl. 11 | cl. 10 | sim | só 5.9 e tempos [F: etsi2026en301549] |
| Section 508 | WCAG 2.0 | WCAG 2.0 (E207.2) | WCAG 2.0 (E205.4) | sim | não [F: accessboard2017section508] |
| GAG, XAG, APX | parcial | sim | não | controles | sim |

### Cobertura cognitiva

| Documento | O que cobre | Tipo de exigência |
|---|---|---|
| WCAG 2.2 | ajuda consistente, reentrada, autenticação sem teste cognitivo; nível de leitura só em AAA; o W3C admite não cobrir todas as necessidades [F: w3c2024wcag22] | critério testável |
| COGA (W3C) | oito objetivos, de clareza a processos sem memória e personalização [F: w3c2021cogausable] | orientação suplementar, não obrigatória |
| WCAG 3 | meta de cobrir "more needs of people with cognitive disabilities" [F: w3c2026wcag3intro] | rascunho |
| AfA PNP | linguagem simplificada, tempo adicional, encorajamento, ferramentas de apoio [F: imsglobal2021afapnp] | preferência individual |
| EN 301 549 / 508 | 4.2.10 e 302.9: "simpler and easier" [F: etsi2026en301549, cl. 4.2.10; accessboard2017section508] | desempenho funcional, sem teste objetivo [I] |
| GAG, APX | linguagem simples, prática sem falha, lembrete de objetivo, menos ações, ritmo [F: gameaccessibility2026fulllist; ablegamers2022apx] | diretriz de projeto |

### Aplicabilidade a jogos e ao acesso alternativo

| Barreira | WCAG 2.2 | EN 301 549 | Diretrizes de jogos |
|---|---|---|---|
| Limite de tempo | 2.2.1, salvo essencial ou tempo real | idem em cl. 11 | tempo preciso não essencial; ajuste de velocidade (GAG); Slow It Down (APX) |
| Ações simultâneas | não há critério geral | 5.9 | evitar (GAG, XAG 107) |
| Segurar ou repetir | não há critério | não | evitar ou alternar (GAG, XAG 107) |
| Gesto e arraste | 2.5.1, 2.5.7 | via WCAG | XAG 107 |
| Alvo pequeno | 2.5.8 (24 px), 2.5.5 (44 px) | via WCAG | alvos ajustáveis (XAG 107) |
| Acionador, varredura, olhar | indireto (teclado, 2.1.1) | 5.1 funcionalidade fechada | esquemas simples compatíveis com acionador e rastreamento ocular (GAG avançado) |

Fontes da tabela: os documentos de cada id; síntese [I].

## Vantagens e limitações

Leitura combinada [I]: conformidade WCAG 2.2 AA é o piso, verificável e incorporado por norma; não garante acesso cognitivo nem jogabilidade. O que preenche: orientação COGA e linguagem simples para cognição (`acs.dim.cognitive-accessibility`); perfis de preferência para a variação individual (`acs.std.accessforall-iso-24751`, `acs.adapt.preference-profiles`); diretrizes de jogos para tempo, precisão e sequência; e testes com usuários de tecnologia assistiva para o que nenhum critério mede (`acs.asmt.user-testing-with-at`).

## Métricas e métodos de avaliação

Só WCAG, EN 301 549 e Section 508 têm critérios com resultado binário de teste; AfA se verifica por conformidade de dados; as diretrizes de jogos se verificam por revisão de projeto e teste com jogadores [I]. Métodos em `acs.asmt.conformance-evaluation` e `acs.asmt.user-testing-with-at`.

## Relações com outros conceitos

Agrega os cinco documentos da área e relaciona-se com `acs.br.emag-and-nbr-17225`, onde se verifica qual dessas normas o marco brasileiro adota, e com `iop.fund.conformidade-e-certificacao`.

## Lacunas e questões abertas

- Não há norma que torne obrigatória a acessibilidade da jogabilidade; as diretrizes de jogos são voluntárias.
- Falta critério testável para compreensão de conteúdo por crianças e por pessoas com deficiência intelectual.
- O estado de citação da EN 301 549 V4.1.1 no Jornal Oficial da UE não foi verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2024wcag22 | normativo | 2026-10-30 |
| w3c2026wcag3intro | normativo (informativo) | 2026-10-30 |
| iso405002025 | normativo [metadados] | 2026-10-30 |
| w3c2021cogausable | normativo (Group Note) | 2026-10-30 |
| w3c2023aria12 | normativo | 2026-10-30 |
| iso2475122008 | normativo [metadados] | 2026-10-30 |
| imsglobal2021afapnp | normativo | 2026-10-30 |
| edtech2026accessibility | normativo | 2026-10-30 |
| etsi2026en301549 | normativo | 2026-10-30 |
| accessboard2017section508 | normativo | 2026-10-30 |
| gameaccessibility2026fulllist | tecnico | 2026-10-30 |
| microsoft2023xag | fornecedor | 2026-10-30 |
| ablegamers2022apx | tecnico | 2026-10-30 |
