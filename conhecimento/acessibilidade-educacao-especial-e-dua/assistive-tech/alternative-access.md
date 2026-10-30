---
id: acs.at.alternative-access
titulo: Acesso alternativo - acionadores, varredura, rastreamento ocular e controle por voz
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [google2026switchaccess, google2026switchaccesssettings, apple2026switchcontrol, apple2026voicecontrol, google2026voiceaccess, nel2017modelling, simpson1999adaptive, jacob1990what, majaranta2009fast, beukelman2020aac, who2022globalreport]
relacoes:
  - { tipo: parte-de, alvo: acs.at.classification-iso-9999 }
  - { tipo: depende-de, alvo: acs.at.screen-readers-and-accessibility-apis }
  - { tipo: complementa, alvo: acs.dim.motor }
  - { tipo: complementa, alvo: acs.at.aac }
  - { tipo: complementa, alvo: acs.adapt.adapting-games-and-activities }
  - { tipo: especificado-por, alvo: acs.std.wcag }
  - { tipo: relacionado-a, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: relacionado-a, alvo: gam.diff.dynamic-difficulty-adjustment }
termos: [acesso alternativo, seleção direta, seleção indireta, acionador, varredura, varredura linear, varredura linha-coluna, seleção por grupos, varredura de ponto, varredura automática, varredura manual, tempo de varredura, atraso no primeiro item, ignorar toques repetidos, tempo de pressão, rastreamento ocular, tempo de permanência, problema do toque de Midas, controle por voz, sobreposição de números, ruído de temporização]
---

# Acesso alternativo: acionadores, varredura, rastreamento ocular e controle por voz

## Definição e terminologia

Acesso alternativo é o conjunto de meios para operar uma interface sem o toque, o mouse ou o teclado convencionais. Divide-se em **seleção direta** (a pessoa aponta o alvo: olhar, cabeça, voz) e **seleção indireta** (o sistema oferece os itens em sequência e a pessoa confirma: varredura). Beukelman e Light descrevem o acesso a sistemas de CAA como seleção direta "with a finger, toe, or eyes" ou seleção de itens "that are scanned or offered individually or in groups" [F: beukelman2020aac, cap. 1].

- **Acionador (switch):** dispositivo que gera um sinal binário. O Android aceita acionadores externos USB ou Bluetooth, teclas de teclado e botões do aparelho [F: google2026switchaccess]; o iOS aceita fontes externas, a tela, a câmera, toque traseiro, sons e gestos de fones [F: apple2026switchcontrol].
- **Varredura:** um realce percorre os itens; a ativação do acionador escolhe o item realçado.
- **Rastreamento ocular com tempo de permanência (dwell time):** seleção por olhar mantido no alvo por um tempo maior que a observação comum [F: majaranta2009fast, introdução].
- **Controle por voz:** comandos falados que nomeiam ou numeram elementos na tela [F: apple2026voicecontrol].

O que não é: o leitor de tela (`acs.at.screen-readers-and-accessibility-apis`) é saída e navegação para quem não vê; acesso alternativo é entrada para quem não usa as mãos com precisão. Ambos leem a mesma árvore de acessibilidade [I].

## Problema que resolve

Pessoas com deficiência motora grave não alcançam a precisão espacial e temporal que toque e mouse exigem. O relatório da OMS e UNICEF cita rastreamento ocular, interação cérebro-computador e entrada por voz como exemplos de produtos assistivos que se beneficiaram da inovação tecnológica, e às vezes a impulsionaram [F: who2022globalreport, seção 1]. O custo é de velocidade: cada meio troca precisão motora por tempo [I].

## Fundamentos e funcionamento

### Varredura e seus tempos

No Android (Switch Access), a varredura linear, que é o padrão, move o realce "through items on the screen one at time"; a varredura por linha e coluna realça a linha e depois o item, e a documentação diz que costuma ser mais rápida; a seleção por grupos só existe com a varredura automática desligada [F: google2026switchaccesssettings]. Os parâmetros de tempo documentados são [F: google2026switchaccesssettings]:

- **Auto-scan time:** segundos que o realce fica em cada item.
- **Delay on first item:** espera extra no primeiro item, somada ao tempo de varredura.
- **Number of scans:** quantas voltas a varredura dá.
- **Point scan / Line speed:** na varredura de ponto, linhas cruzam a tela a uma velocidade em cm/s, e a pessoa para cada linha no ponto desejado.
- **Ignore repeated presses** (antigo "debounce time"): quanto tempo ignorar o mesmo acionador depois de uma pressão.
- **Release to perform action:** ação na soltura, não na pressão.
- **Auto-select:** toca o item realçado automaticamente; desligado, abre menu de ações.

No iOS (Switch Control, iOS 27), há varredura automática, manual (exige pelo menos dois acionadores) e "Single Switch Step Scanning", em que o cursor avança a cada ativação e, sem ação dentro de um prazo, o item atual é selecionado; os ajustes incluem Auto Scanning Time, Pause on First Item, Loops, Move Repeat, Long Press, Tap Behavior, Hold Duration ("how long you need to press and hold a switch before it's accepted") e Ignore Repeat ("Ignore accidental repeated switch triggers") [F: apple2026switchcontrol]. A documentação não publica valores padrão nem faixas [F: google2026switchaccesssettings; apple2026switchcontrol].

### Taxa de comunicação e ruído

Nel, Kristensson e MacKay, citando Koester e Simpson, relatam que um usuário muito rápido de varredura com um acionador chega a cerca de 7 a 8 palavras por minuto, mas taxas de "1 wpm and lower are common"; num estudo com nove participantes, ajustar os parâmetros levou as faixas de 0,3 a 2,9 para 1,1 a 6,5 palavras por minuto [F: nel2017modelling, introdução]. O atraso de varredura tem custo dos dois lados: curto demais gera erros cuja correção derruba a taxa; longo demais desperdiça tempo a cada passo [F: nel2017modelling]. O "click-timing noise" faz o clique sair antes ou depois do pretendido, e "the best way to deal with click-timing noise is to increase the scanning delay"; os autores recomendam medir a distribuição de temporização de cada usuário antes de fixar o atraso [F: nel2017modelling, conclusão]. Simpson e Koester propuseram ajustar o atraso durante o uso, com base no desempenho medido, em vez de fixá-lo na avaliação clínica, e concluem que a adaptação automática "has the potential to enhance text-entry rate" [F: simpson1999adaptive, resumo].

### Rastreamento ocular

Jacob descreve o olhar como fixações de 200 a 600 ms ligadas por sacadas, com microtremor dentro da fixação; a precisão obtida foi de um a dois graus, "more like a touch screen" do que um mouse [F: jacob1990what]. O **problema do toque de Midas**: "Everywhere you look, another command is activated; you cannot look anywhere without issuing a command" [F: jacob1990what]. Suas observações: tempo de permanência de 150 a 250 ms funciona quando a seleção errada se desfaz trivialmente; não houve caso em que permanência longa ("over 3/4 second") sozinha fosse útil; para comandos difíceis de desfazer, confirmação por botão [F: jacob1990what]. Na digitação por olhar, a literatura anterior usava permanência fixa de 450 a 1000 ms e obtinha 5 a 10 palavras por minuto; com permanência ajustável pelo próprio usuário, onze estudantes sem deficiência foram de 6,9 para 19,9 palavras por minuto em dez sessões de 15 minutos, com a permanência média caindo de 876 para 282 ms [F: majaranta2009fast, resumo e resultados]. A área ativa era maior que a tecla visível, para tolerar erro de calibração, e um círculo animado mostrava o tempo decorrido [F: majaranta2009fast, método].

### Controle por voz

No iOS, o Voice Control mostra números, nomes ou uma grade sobre os elementos; a pessoa diz o nome ou número do item, ou um comando seguido do número da grade; com recursos de IA, pode descrever o item com palavras próprias [F: apple2026voicecontrol]. O Voice Access do Android abre aplicativos, navega e edita texto por voz, funciona em sete idiomas, inclusive português, e responde a qualquer voz, não só à do dono [F: google2026voiceaccess].

## Requisitos e pressupostos

- Todo alvo acionável precisa estar na árvore de acessibilidade com nome e ação; a varredura e a voz só alcançam o que a API expõe [I].
- O nome falado pela voz precisa coincidir com o rótulo visível, ou a pessoa não sabe o que dizer [I; ver `acs.std.wcag`].
- Os tempos são da pessoa, não do conteúdo: a interface não deve impor janela menor que o ciclo de varredura configurado [I].

## Vantagens e limitações

| Meio | O que exige da pessoa | Barreiras típicas de mecânica e tempo [I] |
|---|---|---|
| Varredura com acionador | um movimento voluntário repetível e temporizado | janelas de resposta curtas; alvos que se movem; muitos alvos (cada item é um passo); arrastar, segurar, multitoque e gestos simultâneos |
| Rastreamento ocular por permanência | fixação estável, calibração mantida | alvos pequenos ou próximos (precisão de 1 a 2 graus [F: jacob1990what]); leitura sobre alvos ativos (Midas); fadiga ocular com permanência longa [F: majaranta2009fast] |
| Controle por voz | fala inteligível, ambiente silencioso | elementos sem nome visível; ações contínuas (mirar, arrastar); ruído; comandos de terceiros [F: google2026voiceaccess] |

## Métricas e métodos de avaliação

Taxa de entrada (palavras por minuto, com palavra de 5 caracteres) e taxa de erro por distância mínima de edição são as métricas usadas em digitação por olhar [F: majaranta2009fast]. Para varredura, a recomendação de Nel et al. é medir a distribuição de temporização do clique do usuário e escolher o atraso que dê probabilidade de erro aceitável [F: nel2017modelling]. Para atividades, medir tempo até a seleção e seleções erradas por tarefa [I].

## Exemplo técnico independente de domínio

```
# custo mínimo de tempo para alcançar o item k (índice 1) numa grade de L linhas x C colunas
T  = tempo_de_varredura; T0 = atraso_no_primeiro_item
linear(k)          = T0 + (k-1)*T
linha_coluna(r,c)  = T0 + (r-1)*T  + T0 + (c-1)*T      # dois ciclos, um por linha e um por coluna
janela_minima_atividade >= pior_caso(itens) + tempo_de_pressao + margem_de_erro
# exemplo: 12 itens, T=1,0 s, T0=1,5 s -> linear pior caso = 12,5 s; 3x4 linha-coluna = 1,5+2+1,5+3 = 8 s
regra: se a atividade exige resposta em menos que janela_minima, ela é barreira para varredura
```

## Relações com outros conceitos

Parte de `acs.at.classification-iso-9999`; depende de `acs.at.screen-readers-and-accessibility-apis` (mesma árvore). Complementa `acs.dim.motor` (alvos, tempo, Fitts) e `acs.at.aac` (o mesmo acesso serve à comunicação). A adaptação da atividade a esses tempos fica em `acs.adapt.adapting-games-and-activities`; ajuste automático de parâmetros relaciona-se com `gam.diff.dynamic-difficulty-adjustment`. Critérios de tempo ajustável e de rótulo no nome estão em `acs.std.wcag`.

## Lacunas e questões abertas

- Os valores padrão e as faixas dos tempos de varredura no Android e no iOS não estão publicados nas páginas oficiais consultadas.
- O estudo de digitação por olhar com permanência ajustável usou adultos sem deficiência; não foi verificado estudo aberto equivalente com crianças ou com pessoas com deficiência motora.
- Os números de Koester e Simpson foram lidos via Nel et al., não no artigo original; o artigo de 1999 foi lido só no resumo.
- Não foram verificadas fontes abertas sobre interface cérebro-computador como meio de acesso escolar.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| google2026switchaccess | fornecedor | 2026-10-30 |
| google2026switchaccesssettings | fornecedor | 2026-10-30 |
| apple2026switchcontrol | fornecedor (iOS 27) | 2026-10-30 |
| apple2026voicecontrol | fornecedor (iOS 27) | 2026-10-30 |
| google2026voiceaccess | fornecedor | 2026-10-30 |
| nel2017modelling | academico (pré-print) | 2026-10-30 |
| simpson1999adaptive | academico (resumo) | 2026-10-30 |
| jacob1990what | academico | 2026-10-30 |
| majaranta2009fast | academico | 2026-10-30 |
| beukelman2020aac | academico (excerto) | 2026-10-30 |
| who2022globalreport | tecnico | 2026-10-30 |
