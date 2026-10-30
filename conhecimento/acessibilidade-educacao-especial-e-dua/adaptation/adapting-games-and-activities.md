---
id: acs.adapt.adapting-games-and-activities
titulo: Adaptação de jogos e atividades lúdicas
tipo: tecnica
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [gag2026fulllist, gag2026timing, gag2026bypass, microsoft2023xag, microsoft2022xag108, microsoft2022xag117, grammenos2009designing, yuan2011game, sireci2003effects, hinkle2024accommodations]
relacoes:
  - { tipo: especificado-por, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: depende-de, alvo: acs.adapt.accommodation-vs-modification }
  - { tipo: complementa, alvo: acs.at.alternative-access }
  - { tipo: complementa, alvo: acs.dim.motor }
  - { tipo: complementa, alvo: acs.dim.cognitive-accessibility }
  - { tipo: relacionado-a, alvo: gam.diff.dynamic-difficulty-adjustment }
  - { tipo: relacionado-a, alvo: gam.evid.special-education-and-neurodivergence }
  - { tipo: relacionado-a, alvo: acs.adapt.algorithmic-adaptation-and-autonomy }
termos: [mecânica central, ajuste de velocidade, tempo preciso, quick time event, modo assistido, remapeamento de controles, esquema de controle simplificado, dificuldade por mecânica, modo de dificuldade ultrabaixa, pular trecho, modo de prática, jogo universalmente acessível, universos paralelos de jogo]
---

# Adaptação de jogos e atividades lúdicas

## Definição e terminologia

Adaptar um jogo ou atividade lúdica é mudar tempos, velocidades, entradas, estímulos, dificuldade ou feedback para que uma pessoa com outra configuração de capacidades consiga jogar, preservando o que faz a atividade ser ela mesma. As diretrizes de referência (Game Accessibility Guidelines e Xbox Accessibility Guidelines) são descritas como norma em `acs.std.game-accessibility-guidelines`; este documento organiza as técnicas e o critério para aplicá-las.

"Mecânica central" (*core mechanic*) é a ação principal que o jogo exige; as Game Accessibility Guidelines usam o termo sem defini-lo e contrapõem a ele os desafios que "sit outside the core mechanic" [F: gag2026bypass]. Em atividade educacional, a pergunta equivalente é qual habilidade a atividade quer exercitar ou medir (ver `acs.adapt.accommodation-vs-modification`) [I].

## Problema que resolve

Jogos exigem mais do que aplicações comuns. O resumo de Grammenos, Savidis e Stephanidis afirma que jogos são "usually far more demanding than typical interactive applications in terms of motor and sensory skills", por dispositivos especiais, técnicas de interação complicadas e ênfase no controle visual, o que os torna inacessíveis a grande parte das pessoas com deficiência [F: grammenos2009designing, resumo]. As Xbox Accessibility Guidelines observam que "difficulty" é "a subjective construct", resultado do equilíbrio entre as capacidades do jogador e as barreiras do jogo, e que mecânicas "difíceis" podem ser intransponíveis para um jogador com certa deficiência [F: microsoft2022xag108, Overview]. Para quem usa acionadores, varredura ou rastreamento ocular, tempo preciso e entradas repetidas são as barreiras mais diretas (ver `acs.at.alternative-access`) [I].

## Fundamentos e funcionamento

As diretrizes do fornecedor e da comunidade convergem em seis famílias de técnica.

**Tempo e velocidade.** As GAG pedem "an option to adjust the game speed" (motor e cognitivo, nível básico) e "Do not make precise timing essential to gameplay – offer alternatives, actions that can be carried out while paused" (motor, avançado) [F: gag2026fulllist]. A página dessa diretriz lembra que há jogadores "who find any kind of timing difficult or impossible" e cita como alternativas pausar para planejar ações, remover cronômetros de quebra-cabeças e tornar opcionais os trechos de tempo preciso; reconhece que muitos jogos "are inherently about timing", mas diz que tornar o tempo opcional "can even be possible" mesmo nesses [F: gag2026timing]. A XAG 108 pede que jogos de um jogador sejam "pausable at any time", inclusive em cenas não interativas [F: microsoft2022xag108].

**Entrada.** "Allow controls to be remapped / reconfigured" (básico); "Avoid repeated inputs (button-mashing/quick time events)" (intermediário); "Provide very simple control schemes that are compatible with assistive technology devices, such as switch or eye tracking" (avançado) [F: gag2026fulllist]. A XAG 108 sugere considerar um modo que permita concluir o jogo inteiro "by using a greatly reduced control scheme" [F: microsoft2022xag108].

**Dificuldade.** As GAG pedem "a wide choice of difficulty levels", que a dificuldade possa mudar "during gameplay, either through settings or adaptive difficulty", e expor "as many variables as possible" [F: gag2026fulllist]. A XAG 108 recomenda quatro ou mais predefinições, mudança de dificuldade "at any time without losing game progress", um modo de dificuldade ultrabaixa, ajuste separado por mecânica ("Puzzle Difficulty and Combat Difficulty" ou assistências) e nomes de modo que não depreciem o jogador [F: microsoft2022xag108]. O texto dá o caso de quem tem dificuldade motora e quer reduzir o combate sem reduzir os quebra-cabeças, e o inverso para deficiência visual ou cognitiva [F: microsoft2022xag108, Overview].

**Modos assistidos e atalhos.** "Include assist modes such as auto-aim and assisted steering"; "Offer a means to bypass gameplay elements that aren't part of the core mechanic" [F: gag2026fulllist]. A justificativa é que exigências extras "can add interest, but also exclude unnecessarily" [F: gag2026bypass].

**Prática e progresso.** "Include a means of practicing without failure, such as a practice level or sandbox mode"; salvamento automático e manual [F: gag2026fulllist; microsoft2022xag108].

**Estímulos.** Evitar imagens intermitentes e padrões repetitivos; permitir desligar movimento de fundo [F: gag2026fulllist]. A XAG 117 pede meios de pausar, ocultar ou desligar conteúdo que pisca, rola ou se atualiza sozinho, e opções para desligar tremor de câmera e balanço de cabeça, ajustar campo de visão e sensibilidade da câmera [F: microsoft2022xag117].

### Desenho universal em vez de modo especial

O conceito de *universally accessible games* propõe jogos "proactively designed to optimally fit and adapt to individual gamer characteristics and to be concurrently played among people with diverse abilities, without requiring particular adjustments or modifications"; para multijogador, os autores propõem "Parallel Game Universes" [F: grammenos2009designing, resumo]. A revisão de Yuan, Folmer e Harris sobre acessibilidade de jogos existe e é citada como panorama da área, mas não foi lida [F: yuan2011game, metadados].

## Requisitos e pressupostos

- Saber qual é a mecânica central e qual é o objetivo de aprendizagem ou de medida, porque é contra eles que se decide o que ajustar [I].
- Ajustes disponíveis desde o início e alteráveis a qualquer momento sem perda de progresso [F: microsoft2022xag108].
- O status das XAG: o fornecedor as apresenta como boas práticas que "aren't intended to act as a checklist to validate any type of compliance or legal requirements" (versão 3.2, 08/06/2023) [F: microsoft2023xag].

## Atividades que também servem de medida

Quando o jogo produz dado sobre aprendizagem, cada ajuste muda o significado do dado. Recomendação deste documento [I]: classificar cada ajuste em relação ao construto da atividade, aplicar livremente os que só tocam exigências irrelevantes ao construto e registrar a condição de jogo junto com o evento. Ajustar velocidade é acomodação se o construto é, por exemplo, reconhecimento de palavras sem limite de tempo, e modificação se o construto é fluência. A literatura sobre testes mostra que tempo estendido costuma ajudar todos, e mais quem tem deficiência, o que Sireci, Li e Scarpati leem como sinal de que as condições padrão podem ser "too stringent for all students" [F: sireci2003effects, p. 60]: um limite de tempo que não faz parte do objetivo pode simplesmente ser retirado para todos [I]. Pular um trecho que é a própria habilidade-alvo é modificação e, em avaliação, invalida o resultado [F: hinkle2024accommodations, p. 3].

## Vantagens e limitações

Ajustes por mecânica preservam o desafio desejado e removem o indesejado; ajustes de estímulo beneficiam também quem tem sensibilidade sensorial ou ao movimento [F: microsoft2022xag117]. Limitações: as diretrizes são de fornecedor e comunidade, sem avaliação de eficácia publicada junto a elas; a fronteira entre "tornar acessível" e "tornar fácil" é debatida e o próprio fornecedor remete a esse debate [F: microsoft2022xag108, Resources]; e a dificuldade adaptativa automática levanta as questões de autonomia de `acs.adapt.algorithmic-adaptation-and-autonomy` [I].

## Alternativas e comparações

| Estratégia | Exemplo | Efeito sobre o desafio | Risco para a medida |
|---|---|---|---|
| Ajuste de velocidade ou tempo | Velocidade global, pausa ativa [F: gag2026fulllist] | Remove exigência temporal | Alto se o construto é fluência [I] |
| Remapeamento e simplificação de entrada | Um acionador, rastreamento ocular [F: gag2026fulllist] | Remove exigência motora | Baixo [I] |
| Dificuldade por mecânica | Combate x quebra-cabeça [F: microsoft2022xag108] | Mantém o desafio escolhido | Depende da mecânica ajustada [I] |
| Modo assistido | Mira automática [F: gag2026fulllist] | Substitui parte da ação | Alto se a ação assistida é o alvo [I] |
| Pular trecho | Fora da mecânica central [F: gag2026bypass] | Remove trecho | Inválido se o trecho é o alvo [I] |
| Desenho universal | Jogo jogável por todos juntos [F: grammenos2009designing, resumo] | Variável | Exige construto claro desde o desenho [I] |

## Exemplo técnico independente de domínio

```
atividade = { construto: {"discriminar_fonemas"},
              mecanicas: { selecionar: {tempo_limite: 3s}, arrastar: {precisao: alta} } }
ajustes_disponiveis = [velocidade(0.25..1.0), sem_tempo_limite, entrada_varredura(1 acionador),
                       alvo_maior, pular_minijogo, dicas_extras]
para ajuste em escolhas_do_jogador ∪ perfil.ativar:
    tipo = "acomodacao" se ajuste.afeta ∩ atividade.construto == ∅ senão "modificacao"
    aplicar(ajuste)                                   # pode mudar a qualquer momento
    evento.contexto.ajustes.append({ajuste, tipo})    # o dado carrega a condição
se uso == "medida" e existe tipo == "modificacao": marcar(evento, "nao_comparavel")
```

## Relações com outros conceitos

Especificado por `acs.std.game-accessibility-guidelines`; depende de `acs.adapt.accommodation-vs-modification` para o critério. Complementa `acs.at.alternative-access`, `acs.dim.motor` e `acs.dim.cognitive-accessibility`. Dificuldade dinâmica como mecânica e a evidência de jogos em educação especial ficam em `gam.diff.dynamic-difficulty-adjustment` e `gam.evid.special-education-and-neurodivergence`.

## Lacunas e questões abertas

- O artigo de Grammenos et al. (2009) só teve o resumo lido e a revisão de Yuan et al. (2011) só os metadados; ambos sem cópia aberta.
- Não se encontrou estudo que meça se ajustes de tempo e entrada em jogos educacionais alteram a validade das medidas extraídas deles.
- Quais velocidades e janelas de tempo são viáveis com varredura por acionador é questão para `acs.at.alternative-access`; aqui não há valores verificados.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gag2026fulllist | fornecedor (diretrizes de comunidade) | 2026-10-30 |
| gag2026timing | fornecedor | 2026-10-30 |
| gag2026bypass | fornecedor | 2026-10-30 |
| microsoft2023xag | fornecedor (XAG v3.2) | 2026-10-30 |
| microsoft2022xag108 | fornecedor | 2026-10-30 |
| microsoft2022xag117 | fornecedor | 2026-10-30 |
| grammenos2009designing | academico (resumo via OpenAlex) | 2026-10-30 |
| yuan2011game | academico [metadados] | 2026-10-30 |
| sireci2003effects | tecnico | 2026-10-30 |
| hinkle2024accommodations | tecnico | 2026-10-30 |
