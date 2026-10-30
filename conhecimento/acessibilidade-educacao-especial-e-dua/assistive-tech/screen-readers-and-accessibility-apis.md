---
id: acs.at.screen-readers-and-accessibility-apis
titulo: Leitores de tela e APIs de acessibilidade das plataformas
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2026coreaam12, android2026accessibilitynodeinfo, google2026talkbackgestures, apple2026uikitaccessibility, apple2026accessibilityactivate, microsoft2025uiautomation, microsoft2026narrator, webaim2026survey11, webaim2024survey10]
relacoes:
  - { tipo: parte-de, alvo: acs.at.classification-iso-9999 }
  - { tipo: depende-de, alvo: acs.std.wai-aria }
  - { tipo: especificado-por, alvo: acs.std.wcag }
  - { tipo: complementa, alvo: acs.at.alternative-access }
  - { tipo: complementa, alvo: acs.dim.visual }
  - { tipo: relacionado-a, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: avaliado-por, alvo: acs.asmt.user-testing-with-at }
termos: [leitor de tela, API de acessibilidade, árvore de acessibilidade, nome acessível, papel, estado, foco de acessibilidade, explorar por toque, AccessibilityNodeInfo, UI Automation, padrão de controle, UIAccessibility, ação personalizada, modo de varredura, TalkBack, VoiceOver, Narrator]
---

# Leitores de tela e APIs de acessibilidade das plataformas

## Definição e terminologia

Leitor de tela é a tecnologia assistiva que apresenta a interface em fala sintetizada ou braile e permite operá-la sem ver a tela. Ele não lê pixels: consulta uma **API de acessibilidade** do sistema operacional, que expõe cada elemento da interface como um objeto com nome, papel (role), estado, valor e ações. O conjunto desses objetos forma a **árvore de acessibilidade**. A Core-AAM descreve as APIs de acessibilidade como o que torna possível "to communicate accessibility information about user interfaces to assistive technologies", e "expor" um elemento como criar nós de objeto acessível na árvore e preenchê-los com estados e propriedades específicos da API [F: w3c2026coreaam12, introdução].

O que não é: a árvore de acessibilidade não é a árvore de componentes visuais. A documentação do Android afirma que, para um serviço de acessibilidade, o conteúdo da janela é "a tree of accessibility node infos, which may or may not map one-to-one to the view hierarchy" [F: android2026accessibilitynodeinfo]. Leitor de tela também não é o mesmo que síntese de fala embutida em um aplicativo (texto lido em voz alta); este último não dá navegação nem operação [I].

## Problema que resolve

Sem a camada de API, cada leitor de tela teria de entender cada toolkit gráfico. A UI Automation resolve isso no Windows ao mapear propriedades diferentes para uma só: a "Content" de um botão WPF, a "Caption" de um botão Win32 e o "ALT" de uma imagem HTML viram a propriedade **Name** [F: microsoft2025uiautomation]. Na web, a Core-AAM especifica como papéis, estados e eventos de WAI-ARIA viram objetos de cada API de plataforma [F: w3c2026coreaam12].

## Fundamentos e funcionamento

### Web: Core-AAM

A Core-AAM 1.2 está em Candidate Recommendation Draft de 21 de outubro de 2026; a última Recommendation é a 1.1 [F: w3c2026coreaam12, status]. Ela mapeia para MSAA com IAccessible2 1.3, UI Automation, ATK/AT-SPI, a API de acessibilidade do macOS (AX API) e a Android Accessibility API [F: w3c2026coreaam12]. Exemplo de mapeamento de papel: `button` vira ROLE_SYSTEM_PUSHBUTTON (MSAA), Button (UIA), ROLE_PUSH_BUTTON (ATK) e AXButton (AX API); estados como `aria-checked`, `aria-expanded` e `aria-pressed` têm tabelas próprias, e há eventos para mudança de estado, de conteúdo, de foco e de seleção [F: w3c2026coreaam12]. O navegador "MUST always use the WAI-ARIA semantics" quando presentes, salvo exceções, e "SHOULD prune empty descendants from the accessibility tree" [F: w3c2026coreaam12].

### Android

`AccessibilityNodeInfo` (desde a API 14) representa "a node of the window content as well as actions that can be requested from its source"; depois de entregue a um serviço, o nó fica imutável, e "a custom view is free to report itself as a tree of accessibility node info" [F: android2026accessibilitynodeinfo]. O nó tem texto, descrição de conteúdo (`setContentDescription`), descrição de estado (`getStateDescription`) e ações como `ACTION_CLICK`, `ACTION_LONG_CLICK` e `ACTION_ACCESSIBILITY_FOCUS` ("Action that gives accessibility focus to the node") [F: android2026accessibilitynodeinfo]. No TalkBack, arrastar o dedo fala o item sob ele (explorar por toque), deslizar para a direita ou esquerda vai ao item seguinte ou anterior, e tocar duas vezes ativa o item com foco [F: google2026talkbackgestures].

### iOS

A documentação da Apple afirma que os controles do UIKit "come with built-in accessibility"; elementos personalizados que não herdam de classes acessíveis precisam ser expostos por subclasse de `UIAccessibilityElement` [F: apple2026uikitaccessibility]. `UIAccessibilityElement` serve, por exemplo, para ícones ou imagens de texto desenhados dentro de uma view, criando um elemento por item [F: apple2026uikitaccessibility]. O sistema chama `accessibilityActivate()` "when a VoiceOver user double taps the selected element", e a documentação sugere usá-lo para ativar "a control that requires a complex gesture" difícil de executar com VoiceOver ligado [F: apple2026accessibilityactivate]. Ações personalizadas (`UIAccessibilityCustomAction`) aparecem no rotor de ações do VoiceOver [F: apple2026uikitaccessibility].

### Windows

Na UI Automation, todo elemento é um `IUIAutomationElement` numa árvore com a área de trabalho como raiz, filtrável em visão bruta, de controle ou de conteúdo; cada elemento tem um tipo de controle e expõe padrões de controle (control patterns) com propriedades e métodos, sem correspondência um para um entre tipos e padrões; os clientes se registram para eventos específicos [F: microsoft2025uiautomation]. Provedores UIA oferecem ponte para clientes MSAA [F: microsoft2025uiautomation]. O Narrator, leitor de tela embutido no Windows 11, tem modo de varredura (scan mode) e listas de títulos e de pontos de referência [F: microsoft2026narrator].

### Uso real

A pesquisa WebAIM nº 11 (julho e agosto de 2026, 1780 respostas válidas, amostra não controlada) encontrou como leitor principal em computador JAWS 55,0%, NVDA 32,9% e VoiceOver 6,5%; 91,8% usam leitor de tela em celular, com VoiceOver em 72,2% e TalkBack em 29,5% dos que usam leitores móveis; 67,8% navegam primeiro por títulos numa página longa, contra 71,6% em 2024; e 60,1% usam IA para gerar descrição de imagens [F: webaim2026survey11]. Cegueira foi relatada por 83,2% e deficiência cognitiva ou de aprendizagem por 3,0% [F: webaim2026survey11]. Na edição anterior, com coleta em dezembro de 2023 e janeiro de 2024, os principais eram JAWS 40,5% e NVDA 37,7% [F: webaim2024survey10]. A diferença entre edições indica que a distribuição oscila com a amostra, e convém não tratá-la como participação de mercado [I].

## Requisitos e pressupostos

- Todo elemento interativo precisa de nome, papel e estado expostos pela API da plataforma, e de uma ação equivalente ao gesto visual [I, a partir das três documentações].
- Interfaces desenhadas diretamente (canvas, motores de jogo) não geram árvore sozinhas: é preciso criar nós virtuais (`AccessibilityNodeInfo` para view personalizada, `UIAccessibilityElement` no iOS) [F: android2026accessibilitynodeinfo; apple2026uikitaccessibility].
- Gestos complexos (arrastar, desenhar, multitoque) precisam de alternativa ativável por toque duplo ou ação personalizada [F: apple2026accessibilityactivate].

## Vantagens e limitações

A camada de API separa conteúdo de apresentação e permite que leitores de tela, acesso por acionador e controle por voz usem a mesma árvore [I]. Limitações: cada plataforma tem vocabulário próprio e nem todo conceito tem mapeamento direto, razão pela qual a Core-AAM recorre a atributos de objeto quando falta propriedade nativa [F: w3c2026coreaam12]; a navegação é linear e serial, o que cobra tempo em interfaces densas [I]; e a pesquisa WebAIM sub-representa usuários com deficiência intelectual e crianças, de modo que pouco diz sobre esse público [F: webaim2026survey11; I].

## Alternativas e comparações

| Plataforma | API | Unidade | Ativação pelo leitor | Leitor nativo |
|---|---|---|---|---|
| Web | ARIA mapeado pela Core-AAM | nó da árvore de acessibilidade | depende da API de destino | depende do sistema |
| Android | Accessibility API | `AccessibilityNodeInfo` | `ACTION_CLICK`, toque duplo | TalkBack |
| iOS | UIAccessibility | elemento acessível | `accessibilityActivate()`, toque duplo | VoiceOver |
| Windows | UI Automation | `IUIAutomationElement` com padrões | métodos dos padrões de controle | Narrator |

## Métricas e métodos de avaliação

Inspeção da árvore com ferramentas da plataforma (a Microsoft cita o Inspect do Windows SDK [F: microsoft2025uiautomation]); testes de tarefa com usuários de leitor de tela (ver `acs.asmt.user-testing-with-at`); e verificação dos critérios de nome, papel e valor do WCAG (ver `acs.std.wcag`).

## Exemplo técnico independente de domínio

```
# cena desenhada em canvas com três cartas clicáveis
para cada carta c em cena:
    no = criar_no_virtual(id=c.id, limites=c.retangulo_na_tela)
    no.papel   = "botão"
    no.nome    = c.rotulo_textual              # não "imagem1"
    no.estado  = {selecionado: c.selecionada, desativado: not c.jogavel}
    no.acoes   = [ativar -> jogar(c), acao_personalizada("descartar") -> descartar(c)]
ao_mudar(c): emitir_evento(mudanca_de_estado, no(c))   # o leitor anuncia
```

## Relações com outros conceitos

Parte de `acs.at.classification-iso-9999`. Depende de `acs.std.wai-aria` (semântica na web) e é avaliado pelos critérios de `acs.std.wcag` e por `acs.asmt.user-testing-with-at`. Complementa `acs.at.alternative-access`, que usa a mesma árvore para acionadores e voz, e `acs.dim.visual`. Diretrizes de jogos que tratam leitor de tela ficam em `acs.std.game-accessibility-guidelines`.

## Lacunas e questões abertas

- A documentação da Apple sobre `accessibilityLabel`, `accessibilityTraits` e `accessibilityHint` não retornou texto legível na consulta; esses atributos são citados só pela existência no UIKit [I].
- Não foi encontrada pesquisa aberta sobre uso de leitores de tela por crianças em idade escolar.
- O comportamento de motores de jogo multiplataforma frente às APIs nativas não foi verificado nesta área.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2026coreaam12 | normativo (Candidate Recommendation Draft) | 2026-10-30 |
| android2026accessibilitynodeinfo | fornecedor (API level 37) | 2026-10-30 |
| google2026talkbackgestures | fornecedor | 2026-10-30 |
| apple2026uikitaccessibility | fornecedor | 2026-10-30 |
| apple2026accessibilityactivate | fornecedor | 2026-10-30 |
| microsoft2025uiautomation | fornecedor | 2026-10-30 |
| microsoft2026narrator | fornecedor | 2026-10-30 |
| webaim2026survey11 | tecnico | 2026-10-30 |
| webaim2024survey10 | tecnico | 2026-10-30 |
