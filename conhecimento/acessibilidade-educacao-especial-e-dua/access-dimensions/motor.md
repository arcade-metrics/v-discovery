---
id: acs.dim.motor
titulo: Acessibilidade motora (alvos, tempo, gestos e tremor)
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2024wcag22, w3c2023understandingtargetsize, findlater2017comparing, anthony2014designing, gameaccessibility2026fulllist]
relacoes:
  - { tipo: especificado-por, alvo: acs.std.wcag }
  - { tipo: complementa, alvo: acs.at.alternative-access }
  - { tipo: complementa, alvo: acs.adapt.adapting-games-and-activities }
  - { tipo: relacionado-a, alvo: dat.qual.granularity-and-constructs }
  - { tipo: relacionado-a, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: complementa, alvo: acs.adapt.preference-profiles }
  - { tipo: relacionado-a, alvo: gam.diff.dynamic-difficulty-adjustment }
termos: [deficiência motora, tremor, espasticidade, alvo de toque, tamanho do alvo, espaçamento de alvo, pixel CSS, toque espúrio, holdover, gesto baseado em trajeto, gesto multiponto, cancelamento de ponteiro, arrastar, acionamento por movimento, limite de tempo ajustável, interface de teclado, lei de Fitts]
---

# Acessibilidade motora (alvos, tempo, gestos e tremor)

## Definição e terminologia

Acessibilidade motora é a remoção de barreiras para quem tem amplitude, força, precisão, velocidade ou resistência de movimento limitadas. Entram aí pessoas com tremor, espasticidade, paralisia cerebral, lesão medular e esclerose múltipla. O documento do W3C sobre tamanho de alvo cita "hand tremors, spasticity, and quadriplegia" [F: w3c2023understandingtargetsize]. As barreiras se agrupam em quatro famílias [I]:
- **alvos** pequenos ou próximos demais;
- **tempo**, como limites, reação rápida e toque longo;
- **gestos**, como arrastar, pinçar, traçar caminho e sacudir o aparelho;
- **modalidade**, quando a interface aceita só toque ou só mouse.

Quem não usa as mãos ou usa acionadores, varredura ou olhar é tratado em `acs.at.alternative-access`. Este documento cobre os requisitos de interface que tornam esse acesso possível.

## Problema que resolve

Pela lei de Fitts, o tempo de apontamento cresce com a distância e cai com a largura do alvo. A formulação, as fontes e o uso como medida estão em `dat.qual.granularity-and-constructs` e não são repetidos aqui [I]. Para pessoas com deficiência motora, o problema principal não é só o tempo, é o erro. No estudo de Findlater et al. (CHI 2017), com 16 participantes com deficiência motora de membros superiores e 16 sem, o toque foi mais rápido que o mouse. Ainda assim, só quem não tinha deficiência errou menos no toque, e os participantes com deficiência tiveram "a three-fold increase in pointing (tapping) errors on the touchscreen compared to the mouse" [F: findlater2017comparing, resumo].

## Fundamentos e funcionamento

### Tamanho e espaçamento de alvo

O WCAG 2.2 tem dois critérios [F: w3c2024wcag22, 2.5.8 e 2.5.5]:
- **2.5.8 Target Size (Minimum), nível AA**: alvo de "at least 24 by 24 CSS pixels". Alvos menores são aceitos se um círculo de 24 CSS px centrado em cada um não cruzar outro alvo. Há exceções para controle equivalente na mesma página, alvo dentro de texto, alvo definido pelo navegador e apresentação essencial.
- **2.5.5 Target Size (Enhanced), nível AAA**: alvo de "at least 44 by 44 CSS pixels".

O documento explicativo diz que "using larger target sizes will help many people" e recomenda mirar o critério 2.5.5 para controles importantes [F: w3c2023understandingtargetsize]. O pixel CSS é uma medida de ângulo visual ("about 0.0213 degrees"). Ele depende das dimensões da tela e da distância de visão, que o autor do conteúdo não controla [F: w3c2023understandingtargetsize]. Por isso o tamanho físico de 24 CSS px varia de aparelho para aparelho [I].

A evidência empírica pede alvos maiores que o mínimo AA:
- **Deficiência motora.** Com alvos de 6, 12 e 18 mm, a taxa de erro do grupo com deficiência caiu de 42,1% para 7,0%. Os autores concluem que alvos de toque "should be at least 18mm" para esse público, e notam que mesmo a 18 mm o erro foi de 7% [F: findlater2017comparing, Target size e Discussion]. Toques espúrios (dedos ou partes da mão a mais) ocorreram em 5,7% das tentativas de apontar e em 21,3% das de arrastar no grupo com deficiência [F: findlater2017comparing, Spurious touches].
- **Crianças.** Anthony et al. compararam crianças a partir de 7 anos e adultos com alvos de 0,125", 0,25", 0,375" e 0,5" (cerca de 3, 6, 10 e 13 mm) [F: anthony2014designing, Target Acquisition Task]. O alvo de 0,125" teve cerca de metade de erros na primeira tentativa, e as crianças de 7 a 10 anos erraram em média 30% dos alvos de 0,25" [F: anthony2014designing, Implications for Design]. Os autores registram que o resultado "contradicts our original hypothesis that children's smaller fingers might enable them to use smaller touch targets": quanto mais nova a criança, maior o alvo precisa ser [F: anthony2014designing]. Eles também descrevem *holdovers*, toques que caem no lugar do alvo anterior depois da troca de tela. Esses toques foram mais frequentes nas crianças de 7 a 10 anos [F: anthony2014designing, Holdovers].

### Tempo

Pela 2.2.1 Timing Adjustable (A), cada limite de tempo precisa permitir pelo menos uma de três coisas: ser desligado, ser ajustado a "at least ten times the length of the default setting" ou ser estendido com aviso e "at least 20 seconds" para responder, até dez vezes. As exceções são evento em tempo real, limite essencial e limite acima de 20 horas [F: w3c2024wcag22, 2.2.1]. A exceção "essential", em que estender o tempo "would invalidate the activity", é onde jogos e testes cronometrados entram. A decisão sobre o que é essencial pertence ao desenho pedagógico (`acs.adapt.adapting-games-and-activities`) [I].

### Gestos, cancelamento e teclado

O WCAG 2.2 exige [F: w3c2024wcag22, critérios citados]:
- 2.5.1 Pointer Gestures (A): gesto multiponto ou de trajeto deve ter alternativa com um único ponteiro.
- 2.5.2 Pointer Cancellation (A): a ação não dispara no toque inicial, ou pode ser abortada ou desfeita.
- 2.5.4 Motion Actuation (A): o que se aciona movendo o aparelho também se aciona por controle, e a resposta ao movimento pode ser desligada.
- 2.5.7 Dragging Movements (AA): arrastar tem alternativa sem arrastar.
- 2.1.1 Keyboard (A): toda função funciona por interface de teclado, exceto quando depende "on the path of the user's movement".

A 2.1.1 é o que permite usar acionadores e varredura, que em geral emulam teclado [I].

### Jogos e atividades

As *Game Accessibility Guidelines* listam como básicos elementos "large and well spaced", controles remapeáveis, velocidade ajustável e sensibilidade ajustável. Como intermediários, listam evitar botões mantidos pressionados e entradas repetidas (*button-mashing*, *quick time events*), além de alvos de precisão estacionários. Como avançados, listam esquemas compatíveis com acionador e rastreamento ocular, "a cool-down period (post acceptance delay) of 0.5 seconds between inputs" e não tornar tempo preciso essencial [F: gameaccessibility2026fulllist, categoria Motor].

## Requisitos e pressupostos

- Tamanho de alvo definido em unidade independente de densidade e testado em aparelhos reais. Para público com deficiência motora ou crianças pequenas, tomar 24 CSS px como piso legal e não como meta [I, a partir de findlater2017comparing e anthony2014designing].
- Espaço entre alvos e área ativa um pouco maior que a área visível, como recomendam Anthony et al. ("Increase active area for interface widgets") [F: anthony2014designing, tabela 3].
- Filtro de toques espúrios e de *holdovers*: ignorar o toque no lugar do alvo anterior por um intervalo curto [F: anthony2014designing].
- Nenhuma função que exija apenas arrastar, pinçar, segurar ou agir rápido.

## Vantagens e limitações

Alvos maiores reduzem erro para todos, mas ocupam espaço. Em tela pequena, isso força menos opções por tela, o que também ajuda a carga cognitiva [I]. Os estudos citados têm amostras pequenas: 32 participantes no de Findlater et al. e cerca de 70 adultos e crianças no de Anthony et al. Eles usaram tarefas de laboratório e não atividades educacionais reais [F: findlater2017comparing; anthony2014designing]. Nenhum dos dois estudou crianças com deficiência motora, que é justamente a interseção relevante para educação especial [I].

## Alternativas e comparações

| Barreira | Requisito normativo | Recomendação empírica ou de prática |
|---|---|---|
| Alvo pequeno | 24 CSS px (AA); 44 CSS px (AAA) | ≥ 18 mm para deficiência motora [F: findlater2017comparing]; alvos maiores para crianças de 7 a 10 anos [F: anthony2014designing] |
| Toque acidental | 2.5.2 (agir no levantar; desfazer) | Filtro de *holdover*; atraso de 0,5 s entre entradas [F: gameaccessibility2026fulllist] |
| Gesto complexo | 2.5.1, 2.5.7 | Botões equivalentes; evitar segurar |
| Tempo | 2.2.1 (desligar, ×10, +20 s) | Pausa a qualquer momento; velocidade de jogo ajustável |
| Modalidade única | 2.1.1 teclado | Suporte a acionador, varredura e olhar (`acs.at.alternative-access`) |

## Exemplo técnico independente de domínio

```
config_alvo(perfil):
    piso = 24 CSS px                                # 2.5.8
    se perfil.motor_reduzido ou perfil.idade < 11: alvo = max(piso, tamanho_fisico(18 mm))
    espaco_minimo = alvo / 2;  area_ativa = alvo * 1.2      # tolera toque um pouco fora
ao_tocar(p, t):
    se p perto de ultimo_alvo e t - t_troca_tela < 300 ms: ignorar   # holdover
    se dedos > 1 e modo == "apontar": usar só o primeiro contato     # toque espúrio
    acionar no levantar, não no tocar                               # 2.5.2
limite_tempo(atividade):
    se não essencial: oferecer desligar | ×10 | aviso + 20 s           # 2.2.1
```

Os valores 1,2, metade do alvo e 300 ms são ilustrativos e devem ser calibrados com usuários [H].

## Relações com outros conceitos

É especificado por `acs.std.wcag` (diretrizes 2.1, 2.2 e 2.5). Complementa `acs.at.alternative-access`, cujos dispositivos dependem de teclado e de ausência de tempo rígido. Complementa `acs.adapt.adapting-games-and-activities` (o que é tempo "essencial" numa atividade) e `acs.adapt.preference-profiles` (tamanho de alvo e tempo como preferência). Relaciona-se com `dat.qual.granularity-and-constructs`, onde a lei de Fitts é tratada como medida, com `acs.std.game-accessibility-guidelines` e com `gam.diff.dynamic-difficulty-adjustment`: ajustar velocidade por desempenho motor não pode ser confundido com ajustar dificuldade cognitiva [I].

## Lacunas e questões abertas

- Não se encontrou estudo aberto sobre tamanho de alvo de toque para crianças com deficiência motora, nem para crianças menores de 7 anos.
- Os documentos do W3C não trazem conversão oficial de CSS px para milímetros por classe de aparelho. A meta física exige medir nos aparelhos-alvo.
- O trabalho de Mott et al. sobre *Smart Touch*, que reconhece o ponto pretendido por *template matching*, foi localizado mas não aberto.
- A ISO/TS 9241-411, citada em `dat.qual.granularity-and-constructs`, não foi aberta.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2024wcag22 | normativo | 2026-10-30 |
| w3c2023understandingtargetsize | normativo (documento informativo do W3C) | 2026-10-30 |
| findlater2017comparing | academico | 2026-10-30 |
| anthony2014designing | academico | 2026-10-30 |
| gameaccessibility2026fulllist | tecnico | 2026-10-30 |
