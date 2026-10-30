---
id: dat.qual.granularity-and-constructs
titulo: Granularidade de evento e preservação de construtos cognitivo-motores
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [bridges2020timing, anwyl2021realistic, deleeuw2016psychophysics, pronk2020mental, freeman2010mousetracker, mackenzie1992fitts, fitts1954information, iso92414112012, w3c2026hrtime, mdn2026performancenow, mdn2026eventtimestamp, mdn2026requestanimationframe, mdn2026devicepixelratio, mdn2026getcoalescedevents, w3c2026pointerevents3, lamport1978time]
relacoes:
  - { tipo: depende-de, alvo: dat.ev.event-model }
  - { tipo: depende-de, alvo: dat.qual.clocks-and-ordering }
  - { tipo: complementa, alvo: dat.ev.game-telemetry }
  - { tipo: complementa, alvo: dat.qual.schema-validation-and-evolution }
  - { tipo: avaliado-por, alvo: lae.psy.reliability-and-validity }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
  - { tipo: relacionado-a, alvo: dat.ds.comparison }
termos: [granularidade de evento, tempo de reação, acurácia temporal, precisão temporal, lag, cronometria externa, tempo relativo, tempo de iniciação, trajetória de ponteiro, eventos coalescidos, índice de dificuldade, largura efetiva, covariável de dispositivo, devicePixelRatio, taxa de atualização]
---

# Granularidade de evento e preservação de construtos cognitivo-motores

## Definição e terminologia

**Granularidade de evento** é a combinação de três escolhas de registro: a unidade do evento (resultado de tentativa, entrada individual ou amostra contínua), a resolução temporal do carimbo e a resolução espacial das coordenadas [I]. Lamport já observa que "the choice of what constitutes an event affects the ordering of events in a process" [F: lamport1978time, nota 1]; o mesmo vale para os construtos que se pode reconstruir depois [I]. Os construtos tratados aqui são tempo de reação (RT), hesitação (latência de início, pausas, inversões de direção), sequência de decisões, padrões de erro e trajetória de ponteiro.

Dois termos de medição são centrais. Bridges et al. definem **precisão** como "trial-to-trial variability", o erro variável ou jitter, e **acurácia** como o "constant error", também chamado "lag", "offset" ou "bias" [F: bridges2020timing, Introduction]. Um lag constante e conhecido pode ser subtraído, e se cancela em diferenças entre condições; o erro variável "cannot be corrected afterwards" [F: bridges2020timing, Introduction]. Granularidade não é volume: registrar tudo a 1 kHz sem relógio adequado não preserva RT, e registrar só o resultado da tentativa com relógio perfeito não preserva trajetória [I].

## Problema que resolve

Quem registra só a resposta final (acerto, erro, RT por clique) perde o curso temporal da decisão. Freeman e Ambady observam que, quando só RTs são usados, "fine-grained temporal information about how a participant's response evolves over time can be lost" [F: freeman2010mousetracker, Introduction]. Ao mesmo tempo, dados coletados em navegador e em dispositivos do participante trazem lag e jitter que variam por plataforma, navegador, sistema e hardware [F: anwyl2021realistic, Discussion; bridges2020timing, Abstract]. A pergunta é qual a menor unidade e resolução que permitem recalcular o construto depois, e quais covariáveis precisam acompanhar o dado para que a variação técnica possa ser modelada [I].

## Fundamentos e funcionamento

### O que a literatura mede sobre RT em navegador

- **de Leeuw e Motz (2016)**, busca visual com participantes humanos, tentativas intercaladas entre Psychophysics Toolbox e JavaScript (jsPsych) em computadores independentes: o JavaScript registrou RTs em média 26,8 ms mais longos (HDI 95% de 8,18 a 44,5 ms), sem diferença confiável na variabilidade das distribuições nem na inclinação da função de busca; os autores concluem que o JavaScript é "a suitable tool for measuring response times" [F: deleeuw2016psychophysics, Abstract, Effects of software package].
- **Bridges et al. (2020)**, mais de 110.000 tentativas medidas com Black Box Toolkit e caixa de resposta de 1 kHz: pacotes de laboratório com precisão média abaixo de 1 ms; online, a maioria dos pacotes teve precisão de RT "at least under 10 ms in all browsers" e o PsychoPy abaixo de 3,5 ms [F: bridges2020timing, Abstract]. O estudo alerta que teclados USB comuns podem acrescentar 20 a 40 ms, segundo Neath et al. (2011), e que a acurácia absoluta "is poor in browsers"; comparações de RT absoluto entre participantes são "unwise for web-based data" [F: bridges2020timing, Introduction, Conclusions].
- **Anwyl-Irvine et al. (2021)**, atuador robótico sobre teclados de desktop e laptop reais: RTs com lag médio de 80 ms, chegando a 100 ms em algumas configurações; as plataformas são adequadas a estudos que não exijam acurácia de RT abaixo de 100 ms ou de apresentação abaixo de 2 quadros; a plataforma contribuiu mais variância que o dispositivo [F: anwyl2021realistic, Discussion]. Os autores recomendam delineamento intraparticipante e restrição de navegador quando o tempo for crítico [F: anwyl2021realistic, Discussion].
- **Pronk et al. (2020)**, solenoide sobre telas sensíveis ao toque e teclados: RTs "consistently overestimated" em ambos os tipos de dispositivo; diferenças de superestimação entre dispositivos afetam pouco a detecção de diferenças de grupo, mas podem afetar a fidedignidade de diferenças individuais, mais para RT absoluto que para RT relativo [F: pronk2020mental, Abstract]. Bridges et al. resumem a versão pré-print desse estudo como lags de 50 a 70 ms na maioria das configurações, 133 ms num caso, e variabilidade de 5 a 10 ms [F: bridges2020timing, Introduction].

A variabilidade humana é maior que a técnica: Bridges et al. citam desvio-padrão acima de 80 ms em RTs individuais de uma tarefa binária [F: bridges2020timing, Introduction], e Anwyl-Irvine et al. afirmam que variabilidade de 10 a 30 ms "is unlikely to obscure clear differences between conditions" [F: anwyl2021realistic, Discussion]. A consequência para granularidade é que o lag técnico é tolerável quando o construto é uma diferença intraparticipante, e problemático quando é um RT absoluto comparado entre dispositivos [I].

### Resolução do carimbo de tempo no navegador

A especificação W3C High Resolution Time arredonda carimbos a uma resolução de pelo menos 100 µs, ou 5 µs em contextos com isolamento de origem cruzada, e permite valores mais grossos e jitter como mitigação de ataques de temporização [F: w3c2026hrtime]. A MDN confirma esses valores para `performance.now()` [F: mdn2026performancenow]. Para `Event.timeStamp`, o carimbo nativo do evento de entrada, a MDN informa intervalos de arredondamento por navegador: 0,1 ms no Chrome (0,005 ms isolado), 1 ms no Safari (0,02 ms isolado), 1 ms no Firefox com `privacy.reduceTimerPrecision` (0,02 ms isolado) e 16,667 ms ou mais com `privacy.resistFingerprinting` ativo [F: mdn2026eventtimestamp]. A resolução efetiva do carimbo é, portanto, uma covariável e não uma constante [I].

O instante de exibição do estímulo é quantizado pelo quadro. O callback de `requestAnimationFrame` tem frequência que "will generally match the display refresh rate", tipicamente 60 Hz e também 75, 120 e 144 Hz; seu carimbo marca o fim da renderização do quadro anterior, com "minimal precision of 1 millisecond", e as chamadas são pausadas em abas de fundo na maioria dos navegadores [F: mdn2026requestanimationframe]. Pronk et al. expressam erros de apresentação como diferença em quadros, cerca de 16,67 ms a 60 Hz [F: pronk2020mental, Introduction]. Não adianta, portanto, carimbar a resposta em microssegundos se o início do estímulo só é conhecido no quadro [I].

### Trajetória, hesitação e coalescência de eventos

O MouseTracker amostra a posição do mouse a cerca de 60 a 75 Hz, registrando a cada 13 a 16 ms o tempo bruto e as coordenadas x e y em pixels; a partir daí calcula desvio máximo (MD), área sob a curva (AUC), x-flips e y-flips (inversões de direção, usadas como índice de complexidade e vacilação), tempo de iniciação, velocidade e aceleração [F: freeman2010mousetracker, Runner; Measuring complexity]. Para comparar tentativas de durações diferentes, as trajetórias são normalizadas por interpolação linear para 101 passos [F: freeman2010mousetracker, Time normalization]. Os autores também alertam que o tipo de dispositivo apontador (touchpad, mouse, tela) muda a qualidade motora da trajetória [F: freeman2010mousetracker, Influences of Hardware].

Em navegadores, o agente de usuário pode juntar várias atualizações de ponteiro num único `pointermove`, com "a reduction in the granularity and accuracy when tracking, especially with fast and large movements"; `getCoalescedEvents()` devolve as amostras não coalescidas e exige contexto seguro [F: mdn2026getcoalescedevents]. A especificação Pointer Events Level 3 (Recomendação W3C de 30/06/2026) exige que a lista coalescida esteja "chronologically sorted by timeStamp" e que o evento despachado possa ter processamento adicional, "for example to align with the display refresh rate" [F: w3c2026pointerevents3, §10]. Registrar só o `pointermove` despachado é, assim, amostrar no ritmo de quadros e não no ritmo do sensor [I].

### Lei de Fitts e o que registrar no fim do movimento

MacKenzie resume a formulação original de Fitts como `ID = log2(2A/W)` e `MT = a + b·ID`, e a variante baseada no teorema de Shannon `MT = a + b·log2(A/W + 1)`, que evita índices negativos [F: mackenzie1992fitts, §2.2, §3.3]. A largura efetiva `We` corrige a dispersão real dos pontos finais: se o desvio-padrão das coordenadas finais é conhecido, `We = 4,133 × DP` [F: mackenzie1992fitts, p. 107]. Isso implica registrar a coordenada do ponto final de cada seleção, inclusive as erradas, e não apenas acerto ou erro [I]. O dado clássico de Fitts (1954), reproduzido por MacKenzie, tem `MT = 12,8 + 94,7·ID` ms [F: mackenzie1992fitts, Fig. 3; fitts1954information, metadados]. A ISO/TS 9241-411:2012 especifica métodos de avaliação de dispositivos de entrada físicos [F: iso92414112012, metadados].

## Requisitos e pressupostos

Granularidade mínima proposta por construto, síntese deste documento a partir das fontes acima [I]:

| Construto | Evento mínimo | Carimbo | Limite reportado na literatura |
|---|---|---|---|
| Tempo de reação | início do estímulo (quadro) e resposta, mesma origem monotônica | `rAF` para estímulo, `Event.timeStamp` para resposta | lag de 25 a 45 ms além do nativo em estudos anteriores; 80 a 100 ms com teclados reais; jitter < 10 ms em boas configurações [F: bridges2020timing; anwyl2021realistic] |
| Hesitação | amostras de ponteiro desde a exibição até a resposta; foco e visibilidade | idem, por amostra | amostragem de 60 a 75 Hz no MouseTracker [F: freeman2010mousetracker] |
| Sequência de decisões | cada ação com número de sequência por sessão | monotônico + sequência | ver `dat.qual.clocks-and-ordering` |
| Padrão de erro | resposta dada, resposta esperada, coordenada final | idem | `We` exige dispersão dos pontos finais [F: mackenzie1992fitts] |
| Trajetória | eventos coalescidos com x, y, tipo de ponteiro, pressão | `timeStamp` de cada amostra | coalescência reduz granularidade [F: mdn2026getcoalescedevents] |

Covariáveis do dispositivo, registradas uma vez por sessão e de novo quando mudam [I]: `devicePixelRatio`, que é razão entre pixels físicos e CSS, muda com zoom e com troca de monitor e não informa DPI físico [F: mdn2026devicepixelratio]; taxa de atualização estimada pela mediana dos intervalos de `rAF`, já que a frequência do callback acompanha a da tela [F: mdn2026requestanimationframe; I]; `pointerType` (`mouse`, `pen`, `touch`), `width`, `height` e `pressure`, que vale 0,5 em hardware sem pressão [F: w3c2026pointerevents3]; isolamento de origem cruzada, que fixa a resolução do relógio [F: w3c2026hrtime]; navegador, sistema e versão, que explicam parte da variância [F: anwyl2021realistic, Discussion]; tipo de teclado ou tela; tamanho da janela. A latência de toque do dispositivo não é exposta por nenhuma das APIs consultadas; só a cronometria externa a mede [I].

## Vantagens e limitações

Registrar no nível de entrada permite recalcular RT, MD, AUC, x-flips e `We` com outras definições depois, o que é condição de reprodutibilidade [I]. O custo é volume e risco: a especificação Pointer Events adverte que o caminho exato do ponteiro pode ser informação que o usuário considera confidencial e recomenda limitar a precisão de coordenadas, por exemplo a não mais que um décimo de pixel físico [F: w3c2026pointerevents3, §12]. Nenhuma granularidade corrige o lag absoluto entre dispositivos; só o delineamento (intraparticipante, RT relativo) o neutraliza [F: bridges2020timing, Conclusions; pronk2020mental, Abstract].

## Métricas e métodos de avaliação

Validação por cronometria externa (fotodiodo, atuador) na configuração real é recomendada por Bridges et al. e por Anwyl-Irvine et al. [F: bridges2020timing, Abstract; anwyl2021realistic, Discussion]; Pronk et al. usam o mesmo método (brilho medido por sensor, respostas por solenoide) [F: pronk2020mental, Introduction]. Internamente: distribuição dos intervalos de `rAF` (quadros perdidos), fração de `pointermove` com lista coalescida não vazia, quantização observada dos carimbos e taxa de abas ocultas durante tentativas [I]. A fidedignidade dos índices derivados é tratada em `lae.psy.reliability-and-validity`.

## Exemplo técnico independente de domínio

```
tentativa:
  sessao: s-91; seq: 412; esquema: tentativa@3
  estimulo: {id: item-77, exibido_em_quadro: 18233.4}     # rAF, ms desde timeOrigin
  resposta: {t: 18871.9, alvo: opcao_b, esperado: opcao_a, ponto_final: [412.5, 188.0]}
  amostras: [[18240.1, 300.0, 520.0], [18248.3, 301.5, 515.2], ...]  # coalescidas: t, x, y
  oculto_durante: false
dispositivo (por sessao):
  pointerType: touch; dpr: 2.625; viewport: [412, 915]; refresh_est_hz: 60
  isolado: false; ua: "...", resolucao_relogio_obs_ms: 0.1
```

## Relações com outros conceitos

Depende do envelope de `dat.ev.event-model` e dos relógios de `dat.qual.clocks-and-ordering`; complementa `dat.ev.game-telemetry`, que decide o que instrumentar, e `dat.qual.schema-validation-and-evolution`, que versiona a definição de tentativa. É avaliado por `lae.psy.reliability-and-validity`; o viés introduzido por dispositivos correlacionados com a população é tema de `lae.dq.bias-and-validity`; a granularidade dos datasets públicos é comparada em `dat.ds.comparison`.

## Lacunas e questões abertas

- Não há medição consultada de lag e jitter de RT em tablets e celulares usados por crianças; Anwyl-Irvine et al. testaram quatro computadores e sugerem replicar em telas sensíveis ao toque.
- A latência de toque de cada aparelho não é observável por API; falta método leve de calibração em campo.
- O artigo de Fitts (1954) e a ISO/TS 9241-411 não foram abertos; os valores vêm de MacKenzie (1992).
- Não foi verificado se `getCoalescedEvents()` já funciona em todos os navegadores móveis relevantes; a MDN o marca como não Baseline.
- Falta evidência de qual taxa de amostragem mínima preserva MD, AUC e x-flips; o valor de 60 a 75 Hz é o de uma ferramenta, não um limiar demonstrado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| bridges2020timing | academico | 2026-10-30 |
| anwyl2021realistic | academico | 2026-10-30 |
| deleeuw2016psychophysics | academico | 2026-10-30 |
| pronk2020mental | academico | 2026-10-30 |
| freeman2010mousetracker | academico | 2026-10-30 |
| mackenzie1992fitts | academico | 2026-10-30 |
| fitts1954information | academico [metadados] | 2026-10-30 |
| iso92414112012 | normativo [metadados] | 2026-10-30 |
| w3c2026hrtime | normativo | 2026-10-30 |
| w3c2026pointerevents3 | normativo | 2026-10-30 |
| mdn2026performancenow | fornecedor | 2026-10-30 |
| mdn2026eventtimestamp | fornecedor | 2026-10-30 |
| mdn2026requestanimationframe | fornecedor | 2026-10-30 |
| mdn2026devicepixelratio | fornecedor | 2026-10-30 |
| mdn2026getcoalescedevents | fornecedor | 2026-10-30 |
| lamport1978time | academico | 2026-10-30 |
