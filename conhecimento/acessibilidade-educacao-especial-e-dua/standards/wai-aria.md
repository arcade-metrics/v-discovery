---
id: acs.std.wai-aria
titulo: WAI-ARIA 1.2 e ARIA Authoring Practices Guide
tipo: padrao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2023aria12, w3c2026aria13wd, w3c2026usingaria, w3c2026apg, w3c2026apgreadmefirst]
relacoes:
  - { tipo: parte-de, alvo: acs.std.comparison }
  - { tipo: complementa, alvo: acs.std.wcag }
  - { tipo: depende-de, alvo: acs.at.screen-readers-and-accessibility-apis }
  - { tipo: relacionado-a, alvo: acs.at.alternative-access }
  - { tipo: avaliado-por, alvo: acs.asmt.user-testing-with-at }
termos: [WAI-ARIA, papel, estado, propriedade, árvore de acessibilidade, API de acessibilidade, região viva, landmark, padrão de componente, primeira regra do ARIA, gestão de foco, semântica nativa]
---

# WAI-ARIA 1.2 e ARIA Authoring Practices Guide

## Definição e terminologia

WAI-ARIA (Accessible Rich Internet Applications) é a especificação do W3C que acrescenta semântica de acessibilidade a conteúdo web. A versão vigente é a WAI-ARIA 1.2, W3C Recommendation de 6 de junho de 2023, que substitui a 1.1 [F: w3c2023aria12, status]. Ela "provides an ontology of roles, states, and properties that define accessible user interface elements": papéis dizem o tipo do elemento; estados e propriedades, seus atributos e comportamento; as APIs de acessibilidade das plataformas expõem essas informações às tecnologias assistivas, e o mapeamento para essas APIs está numa especificação separada (Core Accessibility API Mappings) [F: w3c2023aria12, resumo].

O ARIA Authoring Practices Guide (APG) é o guia do W3C que explica "how to apply accessibility semantics to common design patterns and widgets", com padrões de componente, cada um com ao menos um exemplo funcional, e práticas como regiões landmark, nomes e descrições acessíveis e interfaces de teclado [F: w3c2026apg].

O que não é: ARIA não muda aparência nem comportamento. Quando um papel sobrepõe a semântica do elemento hospedeiro, "there are no changes in the DOM, only in the accessibility tree" [F: w3c2023aria12]. Também não é critério de conformidade: quem diz o que precisa ser acessível é a WCAG (`acs.std.wcag`); ARIA é um dos meios de satisfazer, por exemplo, nome, papel e valor de componentes [I].

## Problema que resolve

Interfaces construídas com elementos genéricos (um botão desenhado com `div`, uma árvore, uma grade, um temporizador) chegam ao leitor de tela sem nome, papel nem estado. ARIA permite declarar essa semântica e anunciar mudanças assíncronas, tornando componentes ricos utilizáveis por quem depende de tecnologia assistiva (`acs.at.screen-readers-and-accessibility-apis`) [I].

## Fundamentos e funcionamento

### Categorias de papéis (WAI-ARIA 1.2, §5.3)

| Categoria | Exemplos | Observação |
|---|---|---|
| Abstratos | (só para a ontologia) | autores não devem usá-los |
| Widget | button, slider, tab; contêineres listbox, menu, tree, grid | componentes interativos |
| Estrutura de documento | list, table, heading, article | não interativos |
| Landmark | banner, main, navigation, search | regiões de navegação |
| Regiões vivas | alert, log, status, timer | atualizações assíncronas |
| Janela | dialog, alertdialog | |

Fonte da tabela: [F: w3c2023aria12, §5.3].

### Teclado e foco são responsabilidade do autor

A especificação "neither requires nor forbids user agents from enhancing native presentation and interaction behaviors" e determina que "Authors MUST manage focus" em contêineres como grid, listbox, menu, tree e tablist; as interações de teclado recomendadas ficam no APG, não na especificação [F: w3c2023aria12]. O APG formula isso como princípio: "A role is a promise", e "unlike HTML input elements, ARIA roles do not cause browsers to provide keyboard behaviors or styling" [F: w3c2026apgreadmefirst]. O segundo princípio é que ARIA pode tanto encobrir quanto reforçar a semântica nativa, o que dá poder e perigo [F: w3c2026apgreadmefirst].

### A primeira regra do ARIA

O documento "Using ARIA" formula quatro regras. A primeira: "If you can use a native HTML element or attribute with the semantics and behavior you require already built in", use-o em vez de redefinir um elemento com papel, estado ou propriedade ARIA; as demais são não alterar a semântica nativa sem necessidade, tornar todo controle ARIA interativo operável por teclado e não aplicar `role="presentation"` ou `aria-hidden="true"` a elementos focáveis [F: w3c2026usingaria]. Atenção: esse documento passou a W3C Discontinued Draft em 24 de fevereiro de 2026, mantido como referência histórica, e o W3C indica o APG para orientação atual [F: w3c2026usingaria, status]. O APG preserva o espírito da regra sob o título "No ARIA is better than Bad ARIA" [F: w3c2026apgreadmefirst].

### Suporte real

O APG adverte que "testing assistive technology interoperability is essential before using code from this guide in production", e que seus exemplos não incluem contornos para falhas de navegadores e tecnologias assistivas [F: w3c2026apgreadmefirst]. Por isso, ARIA correto na especificação não garante anúncio correto em uma combinação concreta de navegador e leitor de tela; isso só se confirma testando (`acs.asmt.user-testing-with-at`) [I].

### Próxima versão

A WAI-ARIA 1.3 está em Working Draft (4 de junho de 2026), com novos papéis sectionheader e sectionfooter, uma API ariaNotify e regra que proíbe `aria-hidden=true` no elemento raiz [F: w3c2026aria13wd]. Para projeto, a referência estável continua sendo a 1.2 [I].

## Requisitos e pressupostos

- A plataforma expõe uma árvore de acessibilidade e a tecnologia assistiva a consome; fora da web (motores de jogo, telas desenhadas em canvas) ARIA não se aplica diretamente e é preciso usar a API de acessibilidade nativa da plataforma [I].
- Comportamento de teclado e foco implementado pelo autor, coerente com o papel declarado [F: w3c2023aria12; w3c2026apgreadmefirst].

## Vantagens e limitações

Vantagens: vocabulário único e estável para semântica de componentes; padrões de componente com exemplos e modelo de teclado documentado [F: w3c2026apg].

Limitações: ARIA serve sobretudo a quem usa leitor de tela e, em parte, controle por voz e varredura que dependem de nomes e papéis; não resolve barreiras cognitivas, de tempo ou de precisão motora [I]. Uso incorreto piora a experiência, o que motivou a regra "No ARIA is better than Bad ARIA" [F: w3c2026apgreadmefirst]. Nenhuma estatística sobre a frequência de erros em páginas com ARIA foi verificada nesta sessão.

## Alternativas e comparações

| Abordagem | Quando usar | Limite |
|---|---|---|
| Elemento HTML nativo | sempre que existir com a semântica e o comportamento desejados | repertório fixo de componentes |
| ARIA sobre elemento genérico | componente sem equivalente nativo (árvore, grade, abas) | autor implementa teclado e foco |
| API nativa da plataforma | aplicativos e jogos fora do DOM | específica de cada plataforma |

Síntese [I], a partir de [F: w3c2026usingaria; w3c2023aria12].

## Exemplo técnico independente de domínio

```
componente "grade de cartas selecionáveis":
    contêiner role=grid, aria-label="Cartas"
    célula role=gridcell, aria-selected=true|false
    foco: um único tabindex=0 dentro da grade (roving tabindex)
    teclado: setas movem o foco; Espaço/Enter alterna seleção    # promessa do papel grid
    anúncio de resultado: região role=status (não interrompe)
    checagem: existe elemento nativo equivalente? se sim, usá-lo
```

## Relações com outros conceitos

Complementa `acs.std.wcag`, cujos critérios de nome, papel e valor ARIA ajuda a satisfazer. Depende de `acs.at.screen-readers-and-accessibility-apis` (árvore e APIs). Relaciona-se com `acs.at.alternative-access`, porque varredura e controle por voz também navegam pela semântica exposta. É avaliada por `acs.asmt.user-testing-with-at`.

## Lacunas e questões abertas

- O APG não declara se é normativo; a página inicial o descreve como guia [F: w3c2026apg]. Tratar como orientação.
- Não foi verificado o número de padrões de componente do APG nem a cobertura de suporte por leitor de tela.
- A relação entre ARIA e acessibilidade de jogos em canvas ou motores próprios não tem norma do W3C equivalente; fica para `acs.at.screen-readers-and-accessibility-apis`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2023aria12 | normativo | 2026-10-30 |
| w3c2026aria13wd | normativo (rascunho) | 2026-10-30 |
| w3c2026usingaria | normativo (rascunho descontinuado) | 2026-10-30 |
| w3c2026apg | normativo (guia informativo do W3C) | 2026-10-30 |
| w3c2026apgreadmefirst | normativo (guia informativo do W3C) | 2026-10-30 |
