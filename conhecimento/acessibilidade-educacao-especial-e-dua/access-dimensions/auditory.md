---
id: acs.dim.auditory
titulo: Acessibilidade auditiva (surdez e baixa audição)
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2024wcag22, w3c2024captions, who2026deafnessfactsheet, who2021worldhearing, gameaccessibility2026fulllist]
relacoes:
  - { tipo: especificado-por, alvo: acs.std.wcag }
  - { tipo: complementa, alvo: acs.br.libras }
  - { tipo: complementa, alvo: acs.dim.visual }
  - { tipo: complementa, alvo: acs.dim.cognitive-accessibility }
  - { tipo: relacionado-a, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: relacionado-a, alvo: acs.adapt.adapting-games-and-activities }
  - { tipo: complementa, alvo: acs.adapt.preference-profiles }
termos: [surdez, baixa audição, perda auditiva incapacitante, legenda, legenda para surdos, legenda fechada, legenda aberta, legenda automática, transcrição, interpretação em língua de sinais, redundância visual do som, áudio de fundo, características sensoriais]
---

# Acessibilidade auditiva (surdez e baixa audição)

## Definição e terminologia

Acessibilidade auditiva é a remoção de barreiras para pessoas surdas e com baixa audição, e para quem não pode ouvir naquele momento. A OMS distingue os grupos assim [F: who2026deafnessfactsheet]:
- *hard of hearing*: perda "ranging from mild to severe";
- *deaf*: pessoas que "mostly have profound hearing loss, which implies very little or no hearing";
- perda auditiva incapacitante: perda "greater than 35 decibels (dB) in the better hearing ear".

A mesma página observa que pessoas com baixa audição podem se beneficiar de legendas, e que algumas pessoas surdas usam língua de sinais [F: who2026deafnessfactsheet]. A distinção importa porque são dois públicos [I]. Para quem tem a língua de sinais como primeira língua, legenda em português escrito é conteúdo em segunda língua. Para quem perdeu audição e é oralizado, a legenda é o meio principal.

Terminologia do W3C/WAI: *captions* são texto na mesma língua do áudio, com fala e informação não verbal. *Subtitles* são tradução para outra língua e, em geral, não cumprem função de acessibilidade [F: w3c2024captions]. Legenda fechada pode ser ligada e desligada. Legenda aberta fica sempre visível [F: w3c2024captions]. Em português, "legenda para surdos e ensurdecidos" (LSE) é o termo corrente para *captions* [I].

## Problema que resolve

A OMS projeta que, até 2050, "nearly 2.5 billion people" terão algum grau de perda auditiva e mais de 700 milhões terão perda incapacitante. A estimativa atual é de cerca de 95,1 milhões de crianças e jovens de 5 a 19 anos com perda auditiva [F: who2026deafnessfactsheet]. O relatório de referência da OMS é o *World report on hearing* (2021) [F: who2021worldhearing, metadados]. Em ambientes educacionais digitais, as barreiras típicas são [I]:
- vídeo sem legenda;
- instrução falada sem texto;
- feedback só sonoro, como um som de acerto ou de erro;
- tempo que depende de pista sonora;
- áudio de fundo que encobre a fala.

## Fundamentos e funcionamento

### Mídia temporal no WCAG

Os requisitos ficam na diretriz 1.2 [F: w3c2024wcag22, 1.2.1 a 1.2.9]:

| Critério | Nível | Requisito |
|---|---|---|
| 1.2.1 Audio-only (Prerecorded) | A | Alternativa que apresente informação equivalente (transcrição) |
| 1.2.2 Captions (Prerecorded) | A | Legendas para todo áudio pré-gravado em mídia sincronizada |
| 1.2.4 Captions (Live) | AA | Legendas para áudio ao vivo em mídia sincronizada |
| 1.2.6 Sign Language (Prerecorded) | AAA | Interpretação em língua de sinais para todo áudio pré-gravado |
| 1.2.8 Media Alternative (Prerecorded) | AAA | Alternativa completa em texto para mídia sincronizada |
| 1.2.9 Audio-only (Live) | AAA | Alternativa equivalente para áudio ao vivo |

A norma define legenda como alternativa "for both speech and non-speech audio information needed to understand the media content" [F: w3c2024wcag22, glossário, captions]. Define interpretação em língua de sinais como "translation of one language, generally a spoken language, into a sign language" [F: w3c2024wcag22, glossário]. A língua de sinais fica no nível AAA, ou seja, fora da conformidade AA que costuma ser exigida [I]. No Brasil, o estatuto da Libras e o que ele implica para conteúdo digital ficam em `acs.br.libras`.

Outros critérios afetam quem ouve pouco [F: w3c2024wcag22, critérios citados]:
- 1.4.2 Audio Control (A): áudio automático com mais de 3 segundos deve poder ser pausado ou ter volume próprio.
- 1.4.7 Low or No Background Audio (AAA): em áudio de fala pré-gravado, o som de fundo deve ser inexistente, desligável ou "at least 20 decibels lower" que a fala.
- 1.3.3 Sensory Characteristics (A): instruções não podem depender só de características sensoriais, inclusive "sound".

### Qualidade da legenda

O recurso *Captions/Subtitles* do W3C/WAI (atualizado em 17/09/2024) diz que legendas atendem também quem processa melhor a informação escrita do que a falada. Ele recomenda identificar quem fala e incluir efeitos sonoros [F: w3c2024captions]. Sobre legenda automática, o WAI diz que "Automatically-generated captions do not meet user needs or accessibility requirements". Um dos exemplos citados é a troca de "4 to 5 minutes" por "45 minutes", que inverte o sentido [F: w3c2024captions].

### Redundância visual do som em jogos e atividades

As *Game Accessibility Guidelines* tratam como básico "Ensure no essential information is conveyed by sounds alone", legendas para toda fala importante e volumes separados para efeitos, fala e música. Como intermediário, recomendam indicar quem está falando, legendar sons de fundo significativos, ligar a legenda antes de qualquer som tocar e oferecer chave estéreo/mono. Como avançado, recomendam língua de sinais e legenda com velocidade de leitura adequada [F: gameaccessibility2026fulllist, categoria Hearing]. Em atividade educacional, isso quer dizer que todo evento sonoro com função pedagógica precisa de equivalente visual [I]. Exemplos: o som de acerto, o alerta de tempo e a voz que dá a instrução.

## Requisitos e pressupostos

- Inventário de eventos sonoros: para cada um, decidir se carrega informação e qual é o equivalente visual ou háptico [I].
- Legenda revisada por pessoa. Legenda automática é rascunho [F: w3c2024captions].
- Decisão explícita sobre língua de sinais para conteúdo de instrução, considerando o público e o marco legal (`acs.br.libras`), mesmo sendo AAA [I].
- Controle de volume por canal e pausa do áudio automático (1.4.2).

## Vantagens e limitações

Legendas e transcrições também servem a quem está em ambiente ruidoso, a quem aprende a língua e a quem prefere ler [F: w3c2024captions]. Limitações:
- legenda em língua escrita não substitui a língua de sinais para quem a tem como primeira língua [I];
- a norma não define taxa de leitura nem sincronização mínima (as diretrizes de jogos citam "appropriate words-per-minute" sem número) [F: gameaccessibility2026fulllist];
- a redundância visual aumenta a carga visual, o que pode conflitar com padrões cognitivos de reduzir distrações (`acs.dim.cognitive-accessibility`) [I].

## Alternativas e comparações

| Alternativa | Atende | Não atende bem | Nível WCAG |
|---|---|---|---|
| Legenda (LSE) | Pessoas com baixa audição e surdos oralizados; ruído | Quem tem língua de sinais como primeira língua e lê pouco | A (pré-gravado), AA (ao vivo) |
| Transcrição | Áudio puro; busca; leitura no próprio ritmo | Conteúdo em que o tempo importa | A (1.2.1) |
| Janela de língua de sinais | Usuários de língua de sinais | Quem não usa língua de sinais | AAA (1.2.6) |
| Sinal visual ou háptico de evento sonoro | Qualquer pessoa que não ouve no momento | Pessoas cegas (precisa coexistir com o som) | 1.3.3 (instruções); prática de jogos |

## Exemplo técnico independente de domínio

```
evento_sonoro = { id, função: [feedback | alerta | instrução | ambiente], som, visual, háptico? }
validar(atividade):
    para cada e em atividade.eventos_sonoros:
        se e.função != ambiente e e.visual == nulo: erro("som sem equivalente visual")
    para cada vídeo: exigir legenda revisada; se instrução central: considerar janela de língua de sinais
    áudio automático > 3 s: exigir pausa ou volume próprio          # 1.4.2
apresentar(e): tocar(e.som) E mostrar(e.visual)   # simultâneo, não alternativo
```

## Relações com outros conceitos

É especificado por `acs.std.wcag` (diretriz 1.2). Complementa `acs.br.libras`, que trata a língua e as obrigações brasileiras. Complementa `acs.dim.visual`, onde a audiodescrição é o caso simétrico, e `acs.dim.cognitive-accessibility`, onde a transcrição também serve a quem precisa ler no próprio ritmo. Relaciona-se com `acs.std.game-accessibility-guidelines` e com `acs.adapt.adapting-games-and-activities`. A legenda e a janela de sinais são preferências que entram em `acs.adapt.preference-profiles`.

## Lacunas e questões abertas

- O *World report on hearing* (2021) só teve a página de publicação verificada. Os números citados vêm da nota descritiva da OMS de 03/03/2026.
- Não foram abertas normas brasileiras de legendagem e janela de Libras, como a ABNT NBR 15290. Essa verificação cabe a `acs.br.libras`.
- Falta evidência aberta sobre legenda e língua de sinais para crianças em fase de alfabetização, que podem não ler a legenda a tempo [H].
- Não foi encontrado parâmetro normativo de velocidade de legenda (caracteres por segundo) em fonte aberta.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2024wcag22 | normativo | 2026-10-30 |
| w3c2024captions | tecnico (recurso informativo W3C/WAI) | 2026-10-30 |
| who2026deafnessfactsheet | tecnico (nota descritiva da OMS) | 2026-10-30 |
| who2021worldhearing | tecnico [metadados] | 2026-10-30 |
| gameaccessibility2026fulllist | tecnico | 2026-10-30 |
