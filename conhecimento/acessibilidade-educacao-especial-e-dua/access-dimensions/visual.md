---
id: acs.dim.visual
titulo: Acessibilidade visual (baixa visão, cegueira e deficiência de visão de cores)
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2024wcag22, w3c2026wcag3wd, myndex2022apcaw3, who2019worldvision, birch2012worldwide, w3c2024descriptionvisual, abnt2016nbr16452, gameaccessibility2026fulllist]
relacoes:
  - { tipo: especificado-por, alvo: acs.std.wcag }
  - { tipo: complementa, alvo: acs.at.screen-readers-and-accessibility-apis }
  - { tipo: complementa, alvo: acs.dim.auditory }
  - { tipo: complementa, alvo: acs.dim.cognitive-accessibility }
  - { tipo: complementa, alvo: acs.adapt.preference-profiles }
  - { tipo: relacionado-a, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: avaliado-por, alvo: acs.asmt.conformance-evaluation }
termos: [baixa visão, cegueira, deficiência de visão de cores, daltonismo, luminância relativa, razão de contraste, texto grande, contraste não textual, redimensionamento de texto, reflow, espaçamento de texto, APCA, audiodescrição, audiodescrição estendida, transcrição descritiva]
---

# Acessibilidade visual (baixa visão, cegueira e deficiência de visão de cores)

## Definição e terminologia

Acessibilidade visual é a remoção de barreiras para pessoas cegas, com baixa visão ou com deficiência de visão de cores (daltonismo). As barreiras e as respostas são diferentes [I]:
- **Cegueira**: a informação visual precisa de alternativa não visual. Isso inclui texto lido por leitor de tela ou braile e audiodescrição de vídeo.
- **Baixa visão**: a informação continua visual, mas precisa de contraste, ampliação, reflow e espaçamento.
- **Deficiência de visão de cores**: a cor não pode ser o único meio de transmitir informação.

Este documento trata as barreiras e os requisitos. A estrutura do WCAG fica em `acs.std.wcag`, e o funcionamento dos leitores de tela fica em `acs.at.screen-readers-and-accessibility-apis`.

## Problema que resolve

A OMS estima que "at least 2.2 billion people around the world have a vision impairment" e que, em pelo menos 1 bilhão de casos, ela "could have been prevented or is yet to be addressed" [F: who2019worldvision, página do relatório]. A deficiência hereditária de visão vermelho-verde atinge cerca de 8% dos homens e 0,4% das mulheres de ascendência europeia, e entre 4% e 6,5% dos homens chineses e japoneses [F: birch2012worldwide, resumo]. Em uma turma típica, portanto, é provável haver pelo menos um aluno com dificuldade de distinguir vermelho e verde [I]. Feedback de acerto e erro só por verde e vermelho é uma barreira comum em atividades educacionais [I].

## Fundamentos e funcionamento

### Contraste: luminância relativa e razão de contraste

O WCAG 2.2 define a luminância relativa de uma cor sRGB como `L = 0.2126·R + 0.7152·G + 0.0722·B`. Cada canal é linearizado assim: com `C = C8bit/255`, se `C <= 0.04045` então `C/12.92`, senão `((C + 0.055)/1.055)^2.4` [F: w3c2024wcag22, glossário, relative luminance]. A norma registra que o limiar era 0,03928 antes de maio de 2021 e que a troca "has no practical effect" [F: w3c2024wcag22, glossário, nota 2]. A razão de contraste é `(L1 + 0.05)/(L2 + 0.05)`, com L1 a cor mais clara, e vai de 1:1 a 21:1 [F: w3c2024wcag22, glossário, contrast ratio].

Requisitos por critério [F: w3c2024wcag22, critérios citados]:

| Critério | Nível | Requisito |
|---|---|---|
| 1.4.3 Contrast (Minimum) | AA | Texto 4,5:1; texto grande 3:1 |
| 1.4.6 Contrast (Enhanced) | AAA | Texto 7:1; texto grande 4,5:1 |
| 1.4.11 Non-text Contrast | AA | 3:1 para componentes de interface e partes de gráficos necessárias à compreensão |
| 1.4.1 Use of Color | A | Cor não é o único meio visual de transmitir informação, indicar ação, pedir resposta ou distinguir elemento |

"Texto grande" é texto com "at least 18 point or 14 point bold" [F: w3c2024wcag22, glossário, large scale]. Texto incidental e logotipos ficam isentos de 1.4.3 e 1.4.6 [F: w3c2024wcag22, 1.4.3].

### Ampliação, reflow e espaçamento

Pela 1.4.4 (AA), o texto deve poder ser ampliado "up to 200 percent without loss of content or functionality", sem tecnologia assistiva. Legendas e imagens de texto ficam fora [F: w3c2024wcag22, 1.4.4]. Pela 1.4.10 Reflow (AA), o conteúdo deve ser apresentado sem rolagem em duas dimensões a uma largura "equivalent to 320 CSS pixels" (rolagem vertical) ou a uma altura de 256 CSS pixels (rolagem horizontal). Ficam isentas partes que exigem layout bidimensional, como mapas, diagramas, vídeo, jogos e tabelas de dados [F: w3c2024wcag22, 1.4.10]. Pela 1.4.12 (AA), nada pode se perder quando o usuário aplica altura de linha de 1,5 vez a fonte, espaçamento de parágrafo de 2 vezes, espaçamento entre letras de 0,12 vez e entre palavras de 0,16 vez [F: w3c2024wcag22, 1.4.12].

A isenção de "jogos" no reflow tem uma consequência: atividades lúdicas em canvas com layout fixo cumprem a 1.4.10, mas continuam inacessíveis a quem usa ampliação de 400%. Esse é um requisito de desenho que a conformidade não garante [I].

### APCA e o contraste no WCAG 3

O APCA (*Accessible Perceptual Contrast Algorithm*) foi desenvolvido "as an assessment method for W3 Silver/WCAG3". Ele produz um valor Lc com sinal, que muda conforme a polaridade (texto claro em fundo escuro ou o inverso), entre cerca de -108 e 106. Seu repositório diz que está "being evaluated as a replacement for WCAG 2 contrast math" [F: myndex2022apcaw3, README, versão 0.1.9 de 2022]. No rascunho do WCAG 3.0 de 10/09/2026, porém, o requisito de contraste de texto diz "@@[contrast measure to be determined]", e uma nota editorial afirma que "The contrast algorithm used in WCAG 3 is yet to be determined". O APCA não é nomeado [F: w3c2026wcag3wd, Text contrast]. O mesmo rascunho diz que o WCAG 3 "does not deprecate WCAG 2" e que ainda há "several years of work" [F: w3c2026wcag3wd, §1.1]. Hoje, só a razão de contraste do WCAG 2 dá conformidade. O APCA pode servir como verificação adicional de legibilidade, sem valor normativo [I].

### Audiodescrição e alternativas a vídeo

O WCAG define audiodescrição como "narration added to the soundtrack to describe important visual details that cannot be understood from the main soundtrack alone" [F: w3c2024wcag22, glossário]. Para vídeo pré-gravado, a norma pede o seguinte [F: w3c2024wcag22, 1.2.3, 1.2.5, 1.2.7, 1.2.8]:
- 1.2.3 (A): audiodescrição ou alternativa em texto;
- 1.2.5 (AA): audiodescrição;
- 1.2.7 (AAA): audiodescrição estendida, quando as pausas da trilha sonora não bastam;
- 1.2.8 (AAA): alternativa completa em texto.

O recurso do W3C/WAI *Description of Visual Information* (atualizado em 17/09/2024) explica que a descrição deve incluir o texto que aparece no vídeo. Ele lembra que vídeos em que só uma pessoa fala costumam dispensar descrição e que a "descriptive transcript" atende o nível A [F: w3c2024descriptionvisual]. No Brasil, a ABNT NBR 16452, *Acessibilidade na comunicação: Audiodescrição* (09/2016, 13 páginas), "fornece diretrizes para a produção da audiodescrição" [F: abnt2016nbr16452, metadados].

### Jogos e atividades

As *Game Accessibility Guidelines* listam como básicos o alto contraste entre texto e fundo, um tamanho de fonte padrão legível, elementos interativos grandes e bem espaçados e "no essential information is conveyed by a fixed colour alone". Como avançados, listam faixa de audiodescrição, suporte a leitor de tela e voz gravada para todo texto [F: gameaccessibility2026fulllist, categoria Vision].

## Requisitos e pressupostos

- Tokens de cor definidos com razão de contraste calculada, inclusive para estados como foco, erro e desabilitado, e para ícones (1.4.11).
- Todo sinal por cor redundante com forma, texto ou posição (1.4.1).
- Layout que suporte 200% de texto e reflow a 320 CSS px. Em canvas de atividade, ampliação própria [I].
- Vídeo com audiodescrição ou transcrição descritiva definida no roteiro, e não depois [I].

## Vantagens e limitações

A razão de contraste do WCAG 2 é simples, verificável por ferramenta e normativa. A limitação é que ela trata do mesmo jeito as duas polaridades, e foi por isso que surgiu o APCA [I, a partir de myndex2022apcaw3]. O próprio rascunho do WCAG 3 considera a possibilidade de um requisito separado "if red/green color vision deficiency (CVD) is not accounted for within the contrast algorithm" [F: w3c2026wcag3wd, nota editorial]. Reflow e ampliação têm isenções amplas para conteúdo bidimensional, justamente o caso de muitos jogos.

## Alternativas e comparações

| Barreira | Resposta na norma | Resposta além da norma |
|---|---|---|
| Baixo contraste | 1.4.3 / 1.4.6 / 1.4.11 | Tema de alto contraste escolhido pelo usuário; APCA como verificação adicional |
| Cor como único sinal | 1.4.1 | Paletas testadas com simulação de deficiência de visão de cores [I] |
| Texto pequeno | 1.4.4, 1.4.10, 1.4.12 | Ampliação própria em canvas; perfil de preferência (`acs.adapt.preference-profiles`) |
| Conteúdo visual de vídeo | 1.2.3, 1.2.5, 1.2.7 | Audiodescrição segundo a NBR 16452; transcrição descritiva |

## Exemplo técnico independente de domínio

```
contraste(c1, c2):
    lin(v) = v/12.92 se v <= 0.04045 senão ((v+0.055)/1.055)^2.4     # v = canal/255
    L(c) = 0.2126*lin(c.r) + 0.7152*lin(c.g) + 0.0722*lin(c.b)
    (a, b) = ordenar_desc(L(c1), L(c2))
    retornar (a + 0.05) / (b + 0.05)

validar_token(texto, fundo, grande):
    minimo = 3.0 se grande senão 4.5          # 1.4.3 AA
    falhar se contraste(texto, fundo) < minimo
feedback(acerto): cor E ícone E texto ("Certo")   # nunca só verde/vermelho (1.4.1)
```

## Relações com outros conceitos

É especificado por `acs.std.wcag`. Complementa `acs.at.screen-readers-and-accessibility-apis` (alternativa não visual), `acs.dim.auditory` (a audiodescrição é a mesma lógica no sentido inverso das legendas), `acs.dim.cognitive-accessibility` (espaçamento e contraste também ajudam a ler) e `acs.adapt.preference-profiles` (tema, fonte, ampliação). Relaciona-se com `acs.std.game-accessibility-guidelines`. A verificação passa por `acs.asmt.conformance-evaluation`.

## Lacunas e questões abertas

- Braile e linhas braile não foram cobertos aqui, porque nenhuma fonte foi aberta. O assunto pertence a `acs.at.screen-readers-and-accessibility-apis`.
- O *World report on vision* foi consultado só pela página de publicação da OMS. As categorias de gravidade por acuidade visual não foram verificadas.
- A ABNT NBR 16452 aparece no catálogo como "Vigente" e, na mesma página, como "cancelada". O status e o conteúdo normativo precisam ser confirmados na ABNT.
- A data em que o APCA saiu do rascunho do WCAG 3 só aparece em fontes secundárias e não foi verificada no W3C.
- Não se localizou estudo aberto sobre prevalência de deficiência de visão de cores na população brasileira.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2024wcag22 | normativo | 2026-10-30 |
| w3c2026wcag3wd | normativo (rascunho de trabalho) | 2026-10-30 |
| myndex2022apcaw3 | tecnico (repositório do autor do algoritmo) | 2026-10-30 |
| who2019worldvision | tecnico (página da publicação da OMS) | 2026-10-30 |
| birch2012worldwide | academico (resumo PubMed) | 2026-10-30 |
| w3c2024descriptionvisual | tecnico (recurso informativo W3C/WAI) | 2026-10-30 |
| abnt2016nbr16452 | normativo [metadados] | 2026-10-30 |
| gameaccessibility2026fulllist | tecnico | 2026-10-30 |
