---
id: acs.std.wcag
titulo: WCAG 2.2 e o estado do WCAG 3
tipo: padrao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2024wcag22, w3c2023wcag22new, w3c2023understandingtiming, w3c2023understandingtargetsize, w3c2023understandingreadinglevel, w3c2026wcag3wd, w3c2026wcag3intro, w3c2025wcag22iso, iso405002025, w3c2021cogausable, etsi2026en301549]
relacoes:
  - { tipo: parte-de, alvo: acs.std.comparison }
  - { tipo: complementa, alvo: acs.std.wai-aria }
  - { tipo: complementa, alvo: acs.dim.cognitive-accessibility }
  - { tipo: avaliado-por, alvo: acs.asmt.conformance-evaluation }
  - { tipo: relacionado-a, alvo: acs.at.alternative-access }
  - { tipo: relacionado-a, alvo: acs.dim.motor }
  - { tipo: relacionado-a, alvo: iop.fund.conformidade-e-certificacao }
termos: [WCAG, critério de sucesso, nível de conformidade, A, AA, AAA, POUR, página completa, processo completo, suporte de acessibilidade, essencial, evento em tempo real, teste de função cognitiva, tamanho de alvo, ISO/IEC 40500, WCAG 3, requisito central]
---

# WCAG 2.2 e o estado do WCAG 3

## Definição e terminologia

As Web Content Accessibility Guidelines (WCAG) são a recomendação do W3C para acessibilidade de conteúdo web. A versão vigente é a WCAG 2.2, publicada como W3C Recommendation em 5 de outubro de 2023 [F: w3c2023wcag22new] e reeditada em 12 de dezembro de 2024 [F: w3c2024wcag22]. Organiza-se em quatro princípios ("perceivable, operable, understandable, and robust"), diretrizes e critérios de sucesso testáveis, cada um num nível de conformidade A, AA ou AAA [F: w3c2024wcag22]. Em setembro de 2025 a WCAG 2.2 foi publicada como ISO/IEC 40500:2025 (edição 2), que substitui a ISO/IEC 40500:2012 (WCAG 2.0) [F: iso405002025, metadados; w3c2025wcag22iso]; a EN 301 549 V4.1.1 registra que "WCAG 2.2 is identical to ISO/IEC 40500:2025" [F: etsi2026en301549, cl. 9.0, nota 2].

O que não é: não é método de avaliação (isso é `acs.asmt.conformance-evaluation`), não é especificação de semântica para tecnologias assistivas (isso é `acs.std.wai-aria`) e não é obrigação legal por si; vira obrigação quando uma norma ou lei a incorpora (`acs.std.procurement-en-301-549-and-section-508`, `acs.br.emag-and-nbr-17225`).

## Problema que resolve

Dá um critério verificável e independente de tecnologia para dizer se uma página é acessível a pessoas com deficiências visuais, auditivas, físicas, de fala, cognitivas, de linguagem, de aprendizagem e neurológicas [F: iso405002025, metadados]. É a base comum de quase todas as normas de compra e leis de acessibilidade digital [I].

## Fundamentos e funcionamento

### Conformidade

Para o nível AA, "the web page satisfies all the Level A and Level AA success criteria"; a conformidade vale para páginas completas ("cannot be achieved if part of a web page is excluded") e para processos completos (todas as páginas de um processo conformes); só valem usos de tecnologia com suporte de acessibilidade, e conteúdo sem esse suporte não pode bloquear o resto da página [F: w3c2024wcag22, §Conformance Requirements]. "Essencial" é o que, se removido, "would fundamentally change the information or functionality of the content" [F: w3c2024wcag22, definições]; é a exceção mais usada em critérios de tempo e gesto, e por isso a mais relevante para jogos [I].

### O que a 2.2 acrescentou e removeu

A 2.2 acrescenta nove critérios [F: w3c2023wcag22new]:

| Critério | Nível | Exigência resumida |
|---|---|---|
| 2.4.11 Focus Not Obscured (Minimum) | AA | componente focado não fica inteiramente coberto por conteúdo do autor |
| 2.4.12 Focus Not Obscured (Enhanced) | AAA | nenhuma parte coberta |
| 2.4.13 Focus Appearance | AAA | indicador de foco com área e contraste mínimos |
| 2.5.7 Dragging Movements | AA | o que se faz arrastando pode ser feito "by a single pointer without dragging, unless dragging is essential" |
| 2.5.8 Target Size (Minimum) | AA | alvo de "at least 24 by 24 CSS pixels", com exceções |
| 3.2.6 Consistent Help | A | ajuda repetida aparece na mesma ordem relativa |
| 3.3.7 Redundant Entry | A | dado já informado é "auto-populated, or available for the user to select" |
| 3.3.8 Accessible Authentication (Minimum) | AA | nenhum teste de função cognitiva sem alternativa ou mecanismo de apoio |
| 3.3.9 Accessible Authentication (Enhanced) | AAA | idem, sem as exceções de reconhecer objetos e conteúdo pessoal |

Textos entre aspas: [F: w3c2024wcag22, critérios citados]. "Teste de função cognitiva" é "a task that requires the user to remember, manipulate, or transcribe information"; 3.3.8 admite exceções quando há alternativa, mecanismo de ajuda, reconhecimento de objetos ou identificação de conteúdo que o próprio usuário forneceu [F: w3c2024wcag22, 3.3.8 e definições]. A 2.5.8 excetua alvos espaçados (círculos de 24 px que não se cruzam), alvo equivalente, alvos em linha de texto, controles do agente de usuário e apresentação essencial [F: w3c2024wcag22, 2.5.8; w3c2023understandingtargetsize]. O nível AAA (2.5.5) pede 44 por 44 px CSS [F: w3c2024wcag22, 2.5.5]. A 2.2 removeu 4.1.1 Parsing, "obsolete and removed from WCAG 2.2" [F: w3c2023wcag22new].

### Critérios de tempo, movimento e estímulo

- 2.1.1 Keyboard (A): toda função operável por teclado sem tempos específicos por tecla, salvo quando depende do caminho do movimento [F: w3c2024wcag22, 2.1.1].
- 2.2.1 Timing Adjustable (A): cada limite de tempo pode ser desligado, ajustado (até ao menos dez vezes o padrão) ou estendido com aviso, pelo menos 20 s e ao menos dez extensões; exceções: evento em tempo real, limite essencial e limite acima de 20 horas [F: w3c2024wcag22, 2.2.1]. O Understanding justifica os 20 s ("20 seconds to hit 'any switch' is sufficient for almost all users") e lista como beneficiários pessoas com deficiência cognitiva, motora, visual e surdas [F: w3c2023understandingtiming]. Evento em tempo real é o que "occurs at the same time as the viewing and b) is not completely generated by the content" [F: w3c2024wcag22, definições].
- 2.2.2 Pause, Stop, Hide (A): movimento automático com mais de cinco segundos, ao lado de outro conteúdo, precisa poder ser pausado, parado ou oculto [F: w3c2024wcag22, 2.2.2].
- 2.3.1 Three Flashes or Below Threshold (A) [F: w3c2024wcag22, 2.3.1].
- 2.5.1 Pointer Gestures, 2.5.2 Pointer Cancellation e 2.5.4 Motion Actuation (A): gesto multiponto ou de trajetória tem alternativa de ponteiro único; ativação no evento de soltar ou com cancelamento; função por movimento do dispositivo tem alternativa e pode ser desativada [F: w3c2024wcag22, 2.5.1, 2.5.2, 2.5.4].

### O estado do WCAG 3

O rascunho mais recente é o Working Draft de 10 de setembro de 2026; diz ter "several years of work" pela frente e ser inapropriado citá-lo senão como trabalho em andamento [F: w3c2026wcag3wd, status]. A estrutura usa diretrizes como resultados, requisitos centrais ou suplementares, asserções organizacionais e métodos por tecnologia [F: w3c2026wcag3wd, resumo]. A página introdutória (25/09/2026) descreve níveis de relato de 1 a 6, com conformidade no nível 3 (todos os requisitos centrais), escopo além do conteúdo web e a meta de "cover more user needs, including more needs of people with cognitive disabilities"; a WCAG 2 não será descontinuada por vários anos após a finalização da 3 [F: w3c2026wcag3intro]. Esses números podem mudar a cada rascunho [I].

## Vantagens e limitações

Vantagens: critérios testáveis, neutros quanto à tecnologia, com status ISO e adoção por normas de compra [F: iso405002025, metadados; etsi2026en301549, cl. 9.0].

Limitação central, declarada pelo próprio W3C: as diretrizes "will not address every user need for people with these disabilities" [F: w3c2024wcag22, resumo]; na introdução, o W3C registra que "significant challenges were encountered in defining additional criteria to address cognitive, language, and learning" disabilities e remete a orientação suplementar [F: w3c2024wcag22, Background on WCAG 2]. O documento suplementar do W3C para esse público (COGA) se apresenta como não obrigatório para conformidade e cobre barreiras "that were not included in the current normative WCAG 2.x", com oito objetivos: entender o que as coisas são, encontrar o que se precisa, conteúdo claro, evitar e corrigir erros, ajudar o foco, processos que não dependam da memória, ajuda e suporte, adaptação e personalização [F: w3c2021cogausable]. Os novos critérios cognitivos da 2.2 (3.2.6, 3.3.7, 3.3.8) são estreitos: tratam ajuda, reentrada de dados e autenticação, não compreensão do conteúdo [I].

Para jogos e atividades lúdicas, as exceções "essencial" e "tempo real" deixam de fora justamente a mecânica: se o tempo é o desafio, 2.2.1 não exige ajuste [I, a partir de w3c2023understandingtiming]. A WCAG também não trata dificuldade, velocidade de jogo nem carga de memória de trabalho de uma tarefa; esse espaço é das diretrizes de jogos (`acs.std.game-accessibility-guidelines`) [I].

## Alternativas e comparações

Onde a WCAG para, o que preenche (síntese [I]):

| Barreira | Cobertura WCAG 2.2 | O que preenche |
|---|---|---|
| Linguagem difícil | 3.1.5 Reading Level, só AAA: alternativa quando o texto exige leitura acima dos anos finais do ensino fundamental [F: w3c2023understandingreadinglevel] | COGA; linguagem simples e leitura fácil (`acs.dim.cognitive-accessibility`) |
| Memória em processos | 3.3.7 e 3.3.8 (só reentrada e login) | COGA, objetivo "processes do not rely on memory" |
| Tempo como desafio da atividade | exceção de essencial | diretrizes de jogos; adaptação (`acs.adapt.adapting-games-and-activities`) |
| Preferência individual | não há perfil de usuário | AccessForAll (`acs.std.accessforall-iso-24751`) |
| Experiência real de uso | conformidade não mede | testes com usuários (`acs.asmt.user-testing-with-at`) |

## Exemplo técnico independente de domínio

```
para cada limite_de_tempo L na interface:
    se L.essencial ou L.tempo_real ou L.duracao > 20h: registrar_excecao(L, justificativa)
    senão exigir uma de: desligar(L) | ajustar(L, fator >= 10) |
                         avisar_e_estender(L, janela >= 20s, extensoes >= 10)
para cada alvo A: exigir A.tamanho >= 24x24 px CSS ou espacamento(A) ou equivalente(A)
```

## Relações com outros conceitos

Complementa `acs.std.wai-aria` (semântica para tecnologia assistiva) e `acs.dim.cognitive-accessibility` (o que a WCAG não cobre). É avaliada por `acs.asmt.conformance-evaluation`. Seus critérios de tempo e alvo informam `acs.at.alternative-access` e `acs.dim.motor`. A distinção entre conformidade e certificação está em `iop.fund.conformidade-e-certificacao`.

## Lacunas e questões abertas

- O texto da ISO/IEC 40500:2025 não foi acessado; o catálogo indica revisão em curso (estágio "to be revised" em 2026-02-05) e não foi possível confirmar o motivo.
- A seção de conformidade do WCAG 3 não foi lida por inteiro; os níveis de relato vêm da página introdutória.
- Não há critério WCAG que avalie compreensão de conteúdo por crianças; não se localizou norma que o faça.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2024wcag22 | normativo | 2026-10-30 |
| w3c2023wcag22new | normativo (página informativa do W3C) | 2026-10-30 |
| w3c2023understandingtiming | normativo (documento informativo) | 2026-10-30 |
| w3c2023understandingtargetsize | normativo (documento informativo) | 2026-10-30 |
| w3c2023understandingreadinglevel | normativo (documento informativo) | 2026-10-30 |
| w3c2026wcag3wd | normativo (rascunho) | 2026-10-30 |
| w3c2026wcag3intro | normativo (página informativa) | 2026-10-30 |
| w3c2025wcag22iso | normativo (notícia do W3C) | 2026-10-30 |
| iso405002025 | normativo [metadados] | 2026-10-30 |
| w3c2021cogausable | normativo (Group Note, não obrigatório) | 2026-10-30 |
| etsi2026en301549 | normativo | 2026-10-30 |
