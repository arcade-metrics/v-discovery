---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-linguagem
etapa: 06-especificacao-base
status: em revisão
atualizado_em: 2026-10-27
---

# 06 · Base de especificação

Criado depois da rodada 3 (`revisao/rodada-3-execucao.md`, E1–E4), que mostrou que o estudo descrevia a linguagem mas não o suficiente para alguém desenhar o fluxo ou implementar o Bot sem o autor. Este arquivo é a **fonte única** para três coisas: o fluxo, as falas e as reações do Bot. **Onde houver divergência com outro arquivo, este prevalece.**

Não é a especificação completa. A especificação completa é entregável da consultoria de especificação de produto do PIPE. Os itens que ainda faltam estão no fim deste arquivo.

---

## 1. Fluxo da criança (E4)

```
[Troca de criança] turma → avatar → senha-figura (2º ano em diante)
        │
        ├─ primeira vez ─▶ [Primeiro voo] aviso de dados + assentimento → avatar → tema → Do meu jeito → voo curto
        │
        ▼
[Caminho]  ← tela inicial da criança
   penas no topo · linha de voo · peça nova (se houver marco) · botão JOGAR
   │                                  (no limite do dia: "Os jogos de hoje acabaram." no lugar do botão)
   ▼
[Plano de hoje] faixa com os jogos do voo
   │
   ▼
[Microjogo] 9 fases (04-microjogos.md, anatomia) ── Pausar ──▶ [Pausa]
   │                                                         Continuar (primário)
   │                                                         Pular este jogo
   │                                                         Ninho
   │                                                         Sair do voo
   │                                                         Do meu jeito
   ▼
[Próximo] prévia · "Agora não / Jogar"   ("Agora não" = pular o próximo)
   │  (repete até acabar o Plano)
   ▼
[Pouso] o que a criança fez · "Parar por hoje"  (+ "Jogar de novo", só em aparelho individual)
   │
   ▼
[Caminho] a linha cresce; se for marco de coleção, escolha da peça
   │
   ▼
"Parar por hoje" ─▶ [Troca de criança]
```

**Regras das encruzilhadas:**
- **O Caminho é a tela inicial.** Penas e peça nova vivem ali, longe dos botões de continuar.
- **Pular** existe em dois lugares: na tela "Próximo" ("Agora não") e dentro da Pausa ("Pular este jogo"). O jogo pulado **sai do Plano de hoje** com uma transição de 200 ms, sem marca (E17).
- **Segundo voo do dia em aparelho compartilhado:** a criança entra de novo num rodízio posterior e encontra o botão JOGAR no Caminho. "Jogar de novo" no Pouso só existe em aparelho individual. Assim o limite padrão (2) e o modo compartilhado (padrão) não se anulam.
- **"Os jogos de hoje acabaram."** aparece no Caminho, no lugar do botão JOGAR, quando o limite foi atingido.
- **"Sobre"** fica dentro do "Do meu jeito" e repete o aviso de dados narrado (S16).
- **Ninho:** entra pela Pausa ou pela tela "Próximo" (ícone de Ninho ao lado de "Agora não"). Sai por "Continuar", que volta ao ponto de onde a criança veio.

## 2. Fluxo do professor (resumo)

`Turma` (lista de crianças + avisos de acesso) → `Criança` (cartões por jogo, camadas 1 e 2) → `Sinal de atenção` (contexto, encaminhamento, 3 botões) → `Perguntar` (linguagem natural) → `Exportar` (saída para o Plano Educacional Individualizado). `Céu da turma` é uma tela separada, a única projetável. `Ajustes` da turma e por criança.

**Estados do sinal depois do gesto do professor** (E19):
- **"Confirmo o que observei"**: o cartão fica com a marca "Você confirmou em 27/10 · desfazer" e sai da lista de sinais ativos.
- **"Não observei isso em sala"**: mesma marca e saída da lista; o peso do sinal é reduzido no gêmeo.
- **"Já encaminhado"**: mesma marca e saída da lista; não volta a aparecer pelo mesmo padrão por 30 dias `[ASSUMIDO]`.
- **"Desfazer"** fica disponível por 7 dias.

---

## 3. Canal de voz (E1)

**Configuração por aparelho, feita pelo professor:** `Fone: não` (padrão) ou `Fone: sim`.

| Tipo de fala | Fone: não | Fone: sim |
|---|---|---|
| Nome do jogo e instrução (antes do bloco) | voz + texto + pictograma | voz + texto + pictograma |
| Aviso de dados, Primeiro voo | voz + texto + pictograma + Libras | idem |
| Fim de voo, fim de microjogo, peça nova | voz **sem número** + texto | voz sem número + texto |
| Pista, recuo, pausa, pular, convite, Ninho, ajustes | **só texto + pictograma** | voz + texto |
| Qualquer número | **só texto** | **só texto** |

**Regra de implementação:** se uma string tem parâmetro numérico, a versão falada é a string `.voz`, que não tem o número. Critério de aceite: nenhuma string com `{n}` é sintetizada em voz.

## 4. Tabela de falas da criança (E13, E14, E31)

Fonte única. `.texto` é o que aparece; `.voz` é o que se fala (vazio = não se fala). Plural: `{n_jogos}` = "1 jogo" / "{n} jogos". `{n}` sempre conta os **jogos concluídos neste voo, sem os pulados**.

| ID | Gatilho | `.texto` | `.voz` | Canal sem fone |
|---|---|---|---|---|
| `voo.inicio` | Plano de hoje aparece | Oi! Hoje tem {n_jogos}. | Oi! Vamos jogar. | voz + texto |
| `jogo.anuncio` | Fase "O que vem" | Agora: {nome_jogo}. | Agora: {nome_jogo}. | voz + texto |
| `jogo.instrucao` | Demonstração e Pronto? | {instrucao} (ex.: Toque quando aparecer o círculo.) | idem | voz + texto |
| `jogo.transicao_treino` | Entre bloco de medida e de treino | Agora: {nome_treino}. (ex.: Agora: figuras e sons.) | idem | voz + texto |
| `treino.pista` | Erro no bloco de treino | Esse não. {instrucao_treino} (ex.: Esse não. Toque na figura que começa com bê.) | idem | **só texto** |
| `treino.devagar` | Recuo | O jogo vai ficar mais devagar. | idem | **só texto** |
| `jogo.fim_medida` | Fim de bloco de medida | Você jogou {nome_jogo} até o fim. | idem | voz + texto |
| `jogo.fim_treino` | Fim de bloco de treino | Você {acao_treino} {n}. (ex.: Você tocou em 8 figuras.) | Você jogou {nome_treino}. | voz + texto |
| `jogo.convite` | Gêmeo introduz jogo novo | Tem um jogo novo. Quer jogar? | idem | **só texto** |
| `pausa` | Toque em Pausar | Pausado. | idem | **só texto** |
| `pular` | Pular | Tudo bem. Agora: próximo jogo. | idem | **só texto** |
| `ninho.entrada` | Entrar no Ninho | Aqui você pode descansar. | idem | **só texto** |
| `voo.fim` | Pouso | Hoje você jogou {n_jogos}. | Você jogou os jogos de hoje. | voz + texto |
| `colecao.marco` | Marco de coleção no Caminho | Uma peça nova para o Bot. Escolha uma. | idem | voz + texto |
| `dia.limite` | Limite atingido | Os jogos de hoje acabaram. | idem | voz + texto |
| `ajuste.professor` | Do meu jeito, com ajuste do professor | {A professora / O professor} deixou assim. Você pode mudar. | idem | **só texto** |
| `bot.mudanca` | Mudança de arte imposta pelo sistema | Hoje o Bot está com uma asa nova. Você pode trocar em Do meu jeito. | idem | voz + texto |
| `dados.aviso` | Primeiro voo e Sobre | O VUOO guarda como você joga. A sua professora vê. Seus colegas não veem. | idem | voz + texto + Libras |
| `camera.aviso` | Antes de ligar a câmera | A câmera vai ver para onde você olha. Ela não guarda seu rosto. `[A CONFIRMAR]` | idem | voz + texto + Libras |

**Regras de redação** (substituem as de `03` §12 onde divergirem):
- **Uma ação pedida por frase** (e não "um verbo por frase", que é impossível com "Toque quando aparecer o círculo.").
- **Até 8 palavras por frase.** Exceção: avisos de dados e de câmera, divididos em frases curtas.
- **Sem personificação** de objetos ("a câmera vai ver", não "a câmera vai olhar para você").
- **Um nome por coisa**, e **nenhum nome de jogo igual a um termo do sistema** (Ninho, Caminho, Pouso, Penas, Céu) (E9).

## 5. Bot: estados e matriz evento → reação (E2, E3, E23, E26)

### Estados
| Estado | Expressão | Antena | Movimento | Pisca? |
|---|---|---|---|---|
| `entrando` | atento | apagada | desliza da **esquerda** para a posição fixa, 400 ms, ease-out; com reduced-motion, aparece com fade de 200 ms | não |
| `atento` | atento | apagada (contorno, sem luz) | parado | a cada 4–6 s (não no Modo suave) |
| `falando` | atento | apagada | boca alterna entre a linha do atento e um "o" pequeno a cada sílaba tônica, sem sincronia labial fina | não |
| `espelhando` | atento | apagada | inclina 8° em direção ao toque, 200 ms ida e volta, em **todo** toque registrado no treino, certo ou errado | não |
| `curioso` | curioso | `ceu` | uma asa sobe 20°, 300 ms | sim |
| `carregando` | pensando | `lavanda`, pulso senoidal de 2 s | parado | não |
| `contente` | contente | `sol` | as duas asas sobem 20° uma vez, 300 ms | não |
| `sossegado` | sossegado | `folha` | asas sobem e descem 6° num ciclo de 6 s | não |
| `imovel_medida` | atento | apagada | **nenhum** | **não** |
| `oculto` | — | — | não aparece; as falas ficam só no balão, com o pictograma do Bot pequeno | — |

**A antena é só emoção.** A câmera **não** usa a antena: o estado "Câmera ligada" é um pictograma fixo, com o rótulo "Câmera ligada", no canto inferior esquerdo da moldura (E3).

### Matriz evento → reação
| Evento | Bot (estado) | Som | Fala (ID) | Comum aos dois braços do PP3? |
|---|---|---|---|---|
| Plano de hoje aparece | `entrando` → `falando` → `atento` | — | `voo.inicio` | sim |
| Fase "O que vem" / instrução | `falando` | — | `jogo.anuncio`, `jogo.instrucao` | sim |
| Início de bloco de medida | `imovel_medida` | do protocolo | — (a instrução fica como **texto estático** na moldura, sem balão) | sim |
| Toque no bloco de medida | `imovel_medida` | do protocolo | — | sim |
| Fim de bloco de medida | `atento` → `falando` | três notas ascendentes | `jogo.fim_medida` | sim |
| Toque registrado no treino (certo **ou** errado) | `espelhando` | — (o retorno de competência é **do alvo**: reação de 100–200 ms + nota de marimba **no alvo certo**) | — | sim |
| Erro no treino | `espelhando` (igual ao acerto) | kalimba, nota única | `treino.pista` | sim |
| Recuo (decisão do gêmeo) | `atento` (**sem mudança de expressão**) | — | `treino.devagar` | **só adaptativo** |
| Convite a jogo novo (decisão do gêmeo: introduzir um microjogo que a criança ainda não jogou) | `curioso` | — | `jogo.convite` | **só adaptativo** |
| Carregando | `carregando` | — | — | sim |
| Pausa | `atento` | — | `pausa` | sim |
| Entrar no Ninho | `sossegado` | vento muito baixo | `ninho.entrada` | sim |
| Fim do voo (Pouso) | `contente` | três notas ascendentes | `voo.fim` | sim |
| Marco de coleção | `contente` | arpejo curto | `colecao.marco` | sim |
| Câmera liga | `atento` | — | `camera.aviso` | sim |

**Prioridade quando eventos coincidem:** marco de coleção > fim do voo > limite do dia. Um evento por vez, com 400 ms entre eles. Só uma fala por vez; a anterior termina antes.

**Fim de microjogo × fim do voo:** o fim de microjogo usa `atento` + fala; `contente` fica para o fim do voo e para marcos, que todos alcançam.

**Variante não adaptativa (braço de controle do PP3):** idêntica, exceto as linhas marcadas "só adaptativo", que não acontecem. A dificuldade segue progressão fixa por fase (E23).

**Critério de aceite:** nenhuma transição de estado do Bot tem como entrada "acerto" ou "erro". A matriz acima mostra o mesmo estado para os dois.

## 6. Precedência de configurações (E6)

1. `prefers-reduced-motion` e o tamanho de fonte do sistema definem os **valores iniciais**.
2. O professor ajusta por turma ou por criança.
3. A criança sobrescreve no "Do meu jeito" e vê o que o professor ajustou.
4. O **Modo suave** é um atalho que muda ao mesmo tempo: cor da moldura (tokens `suave-*`), efeitos a 30%, música desligada, Bot sem piscar, celebração **quieta**.
5. **Nenhuma configuração muda o palco de medida.**

**Intensidade de celebração:** **quieta** (selo estático), **padrão**, **festa**. O nome "suave" fica só para o Modo suave (E6).

## 7. Tokens além da cor (E8, E20)

| Grupo | Tokens |
|---|---|
| **Espaço** (base 4) | `esp-1` 4 · `esp-2` 8 · `esp-3` 12 · `esp-4` 16 · `esp-5` 24 · `esp-6` 32 · `esp-7` 48 · `esp-8` 64 |
| **Raio** | `raio-s` 8 · `raio-m` 14 · `raio-l` 20 · `raio-pill` 999 |
| **Foco** | anel `ceu` de 3 px, afastamento de 3 px (5,52:1 sobre `papel`) |
| **Alvo mínimo** | criança: 64 × 64 com `esp-4` entre alvos · adulto: 44 × 44 |
| **Borda de alvo** | `contorno` 2 px (3,5:1). `nevoa` nunca delimita alvo |
| **Contorno de pista** | `lavanda-tinta` 3 px |
| **Pena, estrela offline, próximo voo** | `sol-icone` (3,4:1), nunca `sol` sobre fundo claro |
| **Traço do casco do Bot** | `contorno` 2 px (obrigatório) |
| **Movimento** | `dur-curta` 150 ms · `dur-media` 250 ms · `dur-entrada` 400 ms · curva `ease-out` padrão |
| **Tipografia da criança** | peso 400 corpo, 700 títulos e botões; tracking `+0.03em` (espaçado: `+0.12em`); entrelinha: título 1,25, instrução 1,4, corpo 1,5 |
| **Som** | voz 100%, efeitos 50% (30% no Modo suave), música 0% por padrão `[A CONFIRMAR valores em LUFS]` |

**Estados de componente:** padrão, pressionado (`ceu-profundo`), foco (anel), desabilitado (`nevoa` com texto `tinta-suave`, sem esconder), carregando (Bot `carregando`), feito (visto `folha`), pulado (sai da lista), offline (contorno pontilhado `sol-icone`).

**Reflow em telas pequenas:**
- O palco reserva **primeiro** a área mínima definida pelo CIATec (P10), e a moldura usa o que sobra.
- A instrução quebra em até 2 linhas. A partir da escala de texto de 125%, o Bot sai da linha da instrução e vai para o canto da faixa inferior.
- Se ainda assim não couber, o aparelho é registrado como "abaixo da tela mínima" para o bloco de medida, e só o treino roda.

## 8. Penas e Céu: regras de crescimento (E18, E24)

- **Penas:** ficam no topo do Caminho. A cada 10 penas, elas se juntam num **galho** (um desenho, sem número). Altura máxima de uma linha; os galhos vêm antes das penas soltas. A pena do dia tem um anel `sol-icone` (forma, não só cor).
- **Céu da turma:** a constelação tem **número de crianças da turma × 5** estrelas. O texto conta as estrelas da constelação atual ("A turma acendeu 18 estrelas."). Só se desenham as linhas **entre estrelas já acesas**, porque um contorno completo mostra o que falta. Não existe "Ver quem". O aviso de acesso ao aparelho fica em outra tela do painel. Texto do Céu com no mínimo 48 px numa projeção de 1080p.

## 9. O que ainda falta para virar especificação

Entregáveis que este estudo **não** produz e que são da consultoria de especificação de produto e do ilustrador (`99-pendencias.md`, P30–P34):
- **Folha de modelo do Bot:** turnaround, proporções, grade de luz do visor (ex.: 16 × 10 pontos) com as 5 expressões em coordenadas, tamanhos por contexto (moldura 52 px, Caminho 48 px, Pouso 96 px, Ninho 160 px `[ASSUMIDO]`).
- **Tokens em JSON** no formato W3C Design Tokens, gerados a partir de `ferramentas/paleta.json` e desta seção 7.
- **Biblioteca de componentes** com anatomia e estados, em 360 px e em tablet.
- **Inventário de pictogramas** com nome canônico igual ao rótulo do botão (E32).
- **Mockups** de treino com pista, Pausa → Ninho e escolha de peça (E28).
