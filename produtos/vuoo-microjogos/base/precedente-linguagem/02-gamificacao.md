---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-linguagem
etapa: 02-gamificacao
status: em revisão
atualizado_em: 2026-10-27
---

# 02 · A jogabilidade do Duolingo, traduzida para o VUOO

O pedido foi "a jogabilidade do Duolingo: recompensas, tarefas". Este documento pega cada mecânica do Duolingo e decide o que fazer com ela no VUOO. Toda mecânica passa por três perguntas:

1. **Engaja?** Ajuda a criança a voltar? O gêmeo digital depende disso (`[IN-27]`).
2. **É segura?** Funciona sem medo de perder, comparação social, culpa, imprevisibilidade ansiogênica ou sobrecarga? (pesquisa `b`; ECA Digital e AADC na pesquisa `d`)
3. **Fica fora da medida?** Deixa intactos o estímulo e a resposta que o microjogo mede? (`[IN-17]`)

Uma mecânica só entra se passar nas três. Quando falha em uma, é transformada. Códigos: `[IN-xx]` = `00-insumos.md`; `Rxx` = `pesquisa/b-neurodivergencia.md`; `Ixx` = `pesquisa/d-institucional.md`; `Cxx`/`Sxx` = achados das revisões em `revisao/`.

## A ideia que organiza tudo

> **O Duolingo recompensa o resultado e pune a ausência. O VUOO reconhece a presença e não pune nada.**

O motor do Duolingo é aversão à perda: a ofensiva pode zerar, as vidas podem acabar, a liga pode rebaixar. A empresa divulga ganhos expressivos com isso (ligas: +17% de tempo de estudo; ofensiva: ganhos de retenção em D14). São **dados da própria empresa**, de adultos, e a pesquisa sobre ofensivas documenta o custo: quem tem ofensiva longa evita desafios para não arriscá-la, e uma ofensiva quebrada leva ao abandono, mais ainda quando a pessoa se culpa (Silverman & Barasch, 2023, na pesquisa `a`). Para crianças pequenas, o próprio Duolingo tira quase tudo isso: o Duolingo ABC não tem competição, anúncios nem compras.

O VUOO aproveita do Duolingo a **forma**: sessão curta, rotina idêntica, um caminho que mostra a trajetória, um personagem que torna aquilo pessoal, um fim claro. O **motor** é outro: previsibilidade das regras, retorno imediato de competência e pertencimento à turma (Deci, Koestner & Ryan, na pesquisa `b`, R27).

## Onde a gamificação mora: moldura, nunca palco de medida

Toda tela de microjogo tem duas zonas (detalhe em `03` §11):

- **Palco de medida:** onde aparecem os estímulos dos blocos que capturam construtos. Cor, contraste, tamanho em milímetros, posição, tempo, som e número de tentativas são **definidos pelo protocolo do CIATec**, congelados a partir do PP1 (C6). Nada deste documento entra ali: nem tema, nem Modo suave, nem escala de texto, nem Bot, nem barra de tempo, nem variante de A/B/n (C3, C8).
- **Moldura:** tudo o que está fora do palco e tudo o que acontece entre blocos. É onde a gamificação vive.

## Vocabulário do sistema

Substantivos concretos e literais (R23). "Voo" é o nome próprio da sessão, como "lição" no Duolingo. **Nunca é verbo nem figura de linguagem** para a criança: o botão é "Jogar de novo", e não "Voar de novo" (S11).

| Termo no VUOO | O que é | Equivalente no Duolingo |
|---|---|---|
| **Voo** | Uma sessão: 3 microjogos seguidos | Lição |
| **Microjogo** | Uma atividade com bloco de medida e/ou bloco de treino (`[IN-15]`, `04`) | Exercício |
| **Plano de hoje** | Faixa com os pictogramas dos microjogos do voo, sempre visível | Missões diárias |
| **Caminho** | Mapa pessoal onde cada dia de voo desenha mais um trecho da linha de voo do Bot. Só cresce. | Trilha (path) |
| **Penas** | Uma pena por dia em que a criança voou, numa fileira que só cresce. Sem dias da semana, sem casas vazias, sem total numérico. | Ofensiva (streak) |
| **Coleção** | Peças para o Bot, entregues em marcos fixos de dias de voo, sem contador e sem anúncio | Baús, gemas, loja |
| **Céu da turma** | Constelação coletiva: cada criança que voou no dia acende uma estrela. Sem prazo, sem falta. | Ligas |
| **Pouso** | Tela de fim do voo | Tela de fim de lição |
| **Ninho** | Espaço de pausa com opções calmas, oferecido em pontos fixos | Não existe |
| **Modo suave** | Menos som, cor e movimento na moldura, com um toque | Não existe |

## Mecânica por mecânica

### 1. Lição → Voo
**No Duolingo:** de 3 a 5 minutos, ritmo rápido, tela de fim com XP e precisão.
**Decisão: manter a forma e fixar a rotina.** Um voo tem sempre o mesmo número de microjogos (3 `[ASSUMIDO]`), e cada microjogo segue os mesmos passos (R18):

1. **O que vem:** pictograma, nome falado, duração mostrada como forma.
2. **Demonstração:** uma mão animada faz a ação uma vez (R26).
3. **Prática:** uma tentativa que não conta para a medida.
4. **Pronto?:** **a criança toca para começar.**
5. **Jogo:** bloco de medida e/ou bloco de treino (`04`).
6. **O que você fez.**
7. **Próximo:** prévia e botão par "Agora não / Jogar".

**Fonte canônica das fases:** as 9 fases de `04-microjogos.md`, que desdobram o "Jogo" em bloco de medida, transição e bloco de treino. Botões pares são sempre escritos na ordem visual, da esquerda para a direita.

**A duração não é fixada aqui.** Ela deriva do número mínimo de tentativas por construto definido pelo CIATec (C6). A estimativa de 60 a 90 s é `[A CONFIRMAR]`.
**Por quê:** a rotina previsível é uma das acomodações com mais apoio na literatura para crianças autistas (pesquisa `b`, seção 3) e não tem custo conhecido para as outras.

### 2. XP → não existe
**Decisão: remover.** Nenhum ponto numérico para a criança.
**Por quê:** XP mede desempenho (bônus de perfeição e velocidade), alimenta comparação e é economia de fichas (R28). O que ele tem de bom, mostrar que se avançou, o Caminho faz sem número.

### 3. Ofensiva → Penas
**No Duolingo:** dias seguidos; zera se falhar um dia.
**Decisão: uma pena por dia de voo, numa fileira que só cresce** (R29, I6, S7). Não há calendário, dias da semana nem casas vazias, porque uma grade com casas vazias mostra a ausência. Não há total numérico, porque um total é comparável no recreio.
**Por quê:** na escola, a ausência raramente é escolha da criança: rodízio de aparelho, falta do professor, internet, AEE, terapia.
**Retenção:** a responsabilidade pelo acesso fica com a escola. O professor recebe um aviso de **acesso** ("3 crianças ainda não tiveram vez no aparelho esta semana"), e não de comportamento da criança (S3).

### 4. Vidas / energia → não existe
**Decisão: remover.** Errar não custa nada (R14).
**Por quê:** o próprio Duolingo abandonou os corações porque iniciantes ficavam sem vidas duas vezes mais que os demais (pesquisa `a`). E o erro é dado valioso para o gêmeo.

### 5. Feedback de acerto e erro → dois regimes, na moldura
**No Duolingo:** som brilhante e faixa verde no acerto; som grave e faixa vermelha no erro.

| | **Bloco de treino** | **Bloco de medida** |
|---|---|---|
| Quem define | Design instrucional | **Protocolo do CIATec**, por instrumento |
| Retorno por tentativa | **No alvo:** o alvo certo reage ao toque (100–200 ms) com uma nota de marimba. No erro: kalimba, fala `treino.pista` ("Esse não. Toque na figura que começa com bê.") e o alvo certo ganha contorno `lavanda-tinta` (S11, E14) | O que o protocolo determina. Padrão sugerido: retorno idêntico para toda tentativa (R15) |
| Ajuda | Gradual: sem dica → destaque → demonstração | Nenhuma |
| Dificuldade | 3 erros seguidos: o jogo fica mais devagar, avisado só por texto e pictograma (`treino.devagar`) (R16, S9, S11). O Bot **não muda de expressão** (E2) | Fixa no bloco; muda entre blocos por decisão do gêmeo, registrada (R0) |
| Bot | Fora do palco; **o mesmo gesto em todo toque registrado, certo ou errado** (espelhar). O retorno de competência é do alvo, nunca do Bot (E2) | Fora do palco, em `imovel_medida`: sem gesto, sem piscar, calado (C8, D-12) |

**Nunca, em nenhum bloco:** "X" vermelho, buzina, tremor, "ERRADO", "GAME OVER", som descendente de falha (S12).
**Hipótese, não fato:** a criança pode perceber a diferença entre os dois regimes. Isso é verificado no PP3 e no co-design (C8).

### 6. Tempo
**Decisão:** no **bloco de medida**, a barra de duração fica **oculta por padrão**; só aparece se o protocolo exigir, e nunca muda de cor dentro do bloco. O aviso de fim acontece **só entre blocos** (C8). No **bloco de treino**, a barra é uma forma que esvazia, sem números, sem vermelho, sem tique-taque, e o limite é ajustável pelo professor (R21, I18, WCAG 2.2.1). Nenhum microjogo dá bônus por velocidade.

### 7. Trilha → Caminho
**No Duolingo:** caminho do currículo, com o futuro bloqueado.
**Decisão:** o Caminho mostra a **trajetória feita**. Cada dia de voo desenha mais um trecho da linha do Bot sobre uma paisagem. Não há cadeado nem trecho bloqueado à vista; o próximo voo é sempre um só (`[IN-32]`, R29).

### 8. Missões diárias → Plano de hoje
**Decisão: agenda visual** (R19). Os pictogramas do voo, com o atual destacado e os concluídos com um visto. Sem missões de desempenho.
**Por quê:** a agenda visual é uma prática com apoio para crianças autistas. A pesquisa `b` registra a ressalva de que parte dessa evidência usa critérios frouxos (Leaf et al., 2021). Para as outras crianças, é uma lista de tarefas; não há estudo específico sobre o efeito nelas.

### 9. Baús, gemas, loja → Coleção em marcos
**No Duolingo:** baús com conteúdo variável, gemas como moeda, loja.
**Decisão (D-07 revista):**
- A cada **3 dias de voo**, a criança ganha uma peça para o Bot. **Por dia de voo, não por voo**: jogar duas vezes no mesmo dia não acelera nada.
- **Sem contador e sem anúncio.** Nada de "Faltam 2". A peça aparece no Caminho, longe do botão de continuar (S6).
- **Nada aleatório.** Em cada marco, a criança **escolhe entre 3 peças equivalentes**, sem raridade e sem valor diferente (I5).
- Peças cosméticas, ligadas ao tema de interesse da criança (R32). Nada se perde, compra ou troca.

**Por quê:** recompensas esperadas e contingentes à conclusão são as que mais enfraquecem a motivação intrínseca (Deci, Koestner & Ryan, 1999); as inesperadas, não (C20, R28). Sorteio é proibido (I5, ECA Digital). Contador perto do botão de continuar é gancho de "só mais um" (S6). O marco fixo sem anúncio atende os três: é inesperado para a criança e determinístico para o sistema.

### 10. Ligas → Céu da turma
**No Duolingo:** ligas semanais com promoção e rebaixamento.
**Decisão:** remover toda comparação individual e criar um **pertencimento assíncrono** (C12):
- Cada criança que voou no dia acende **uma estrela**. Uma por criança por dia, para que quem joga mais não valha mais (S3).
- O Céu mostra só o que foi aceso: "A turma acendeu 18 estrelas." **Sem "Faltam", sem fração, sem prazo.** A constelação se completa quando se completar, e a próxima começa dali. Não existe o estado "não completou".
- É anônimo: ninguém vê quem acendeu qual estrela.
- Pode ser projetado na lousa. **Nada mais do VUOO pode.** O aviso de acesso ao professor nunca fica na mesma tela do Céu, e não existe "Ver quem" (E18). Tamanho da constelação e regras de desenho em `06` §8.
- **Critério de parada:** se, no piloto ou no co-design, alguma criança for apontada como culpada pela constelação, o Céu sai do produto.

**O que o Céu não é:** colaboração. O CIATec define colaboração como jogo com consciência mútua, coordenação e comunicação entre crianças, com mediador (`[IN-19]`). Isso está na seção 18.
**Sobre as "classificações" do CIATec (`[IN-26]`):** pergunta aberta ao CIATec (`99-pendencias.md`). A recomendação deste estudo é que sejam níveis individuais de desafio, visíveis só ao professor.

### 11. Duo, o mascote que cobra → VUOO Bot, o par previsível
**Decisão:** o Bot aproveita do Duo **a função** (dar rosto e vínculo) e **inverte o caráter**. Nunca fica triste, nunca cobra, nunca chama a criança de volta, e **sua expressão não depende do acerto ou do erro da criança** (S8). Regras em `03` §4.

### 12. Notificações → só para o professor, e sobre acesso
**Decisão:** nenhuma notificação para a criança (I7). O professor recebe avisos sobre **acesso ao aparelho**, nunca sobre "crianças que não voaram" como comportamento.

### 13. Celebração de fim de lição → Pouso
**Decisão:** o Pouso reconhece **participação** (S5):
- Depois de um bloco de medida: "Você jogou o jogo das bolhas até o fim." Nenhum número de acerto, porque devolveria à criança o resultado que o regime de medida esconde.
- Depois de um bloco de treino: contagem de **ações**, e nunca de acertos nem de passos com resultado ótimo conhecido ("Você separou 16 cartões.").
- Números aparecem só em texto, nunca falados em voz alta (S9).
- Intensidade da celebração em 3 níveis (R34): **quieta** (selo estático), **padrão** (animação do Bot de até 2 s), **festa** (mais movimento, sem flashes).
- Dois botões de mesmo peso: **"Parar por hoje"** à esquerda e **"Jogar de novo"** à direita. Em modo aparelho compartilhado (padrão), só aparece "Parar por hoje" (S19).

### 14. Prática personalizada → adaptação invisível aos colegas, explicada à criança
**Decisão:** o gêmeo escolhe os microjogos e ajusta a dificuldade **entre blocos**. Os colegas não veem nem ouvem isso (S9). A própria criança sabe que é acompanhada (seção 15).

### 15. Teste de nivelamento → Primeiro voo, com aviso e assentimento
**Decisão:** o Primeiro voo:
1. O Bot explica, com voz, texto, pictograma e Libras: "O VUOO guarda como você joga: o que você tocou e quanto tempo levou. A sua professora vê isso para te ajudar. Seus colegas não veem." Botão "Ouvir de novo" (S16, I12, S15).
2. Assentimento: "Agora não / Quero jogar". "Agora não" é respeitado.
3. Avatar escolhido numa galeria, sem foto; senha-figura a partir do 2º ano (I11, S14).
4. Tema de interesse (R32).
5. "Do meu jeito": som, movimento, intensidade, presença do Bot, com prévia ao vivo (R37, R39).
6. Primeiro voo: "Agora você vai jogar para o VUOO te conhecer."

Se houver captura por câmera (Wemoga Eye), o aviso e o assentimento são específicos para ela (`03` §11, C16).

### 16. Sessão infinita → Voo com fim
**Decisão:**
- O professor define o limite diário, com padrão de 2 e **teto técnico de 3** voos por dia (D-14, S19).
- Ao atingir o limite: "Os jogos de hoje acabaram." Sem "amanhã tem mais", que é falso em véspera de feriado e é gancho de retorno (S11).
- Nada de reprodução automática.

### 17. Pausa, pular e Ninho
- **Pausa** sempre no mesmo canto (R22). Pausar descarta a tentativa em andamento e a registra como **interrompida por pausa**, que é **dado válido de autorregulação**, e não voo inválido (S13).
- **Pular** ("Agora não") é sempre permitido. Vira dado só agregado no painel, nunca por criança, salvo pedido da equipe do AEE (S13).
- **Ninho:** oferecido **em pontos fixos** (na tela de Pausa e na tela "Próximo"; fluxo em `06` §1), **nunca como reação a erro** (S10). Dentro dele, opções iguais e opcionais: olhar o céu, ouvir o vento, ver o Bot mexer as asas devagar, só esperar. Fala: "Aqui você pode descansar. Toque em Continuar quando quiser." A tela escurece pouco, sem parecer desligada.

### 18. Quests de amigos → Colaboração, desde já na biblioteca
**Decisão (C12):** a biblioteca de componentes já inclui o que os jogos colaborativos do CIATec precisam:
- **turno visível** (de quem é a vez, por avatar e cor da moldura);
- **objetivo compartilhado** (uma barra para os dois);
- **comunicação por pictograma entre pares** (um conjunto fechado: "sua vez", "me ajuda", "pronto", "espera");
- **Bot como mediador** (anuncia turnos, descreve o que a dupla fez, nunca o que cada um fez).

Os jogos colaborativos **não têm bloco de medida individual**: o desempenho de uma criança depende da outra. A medida individual fica nos microjogos individuais. Exemplos em `04`.

## O que o VUOO tem e o Duolingo não

- **Ninho:** espaço de autorregulação para todos (pilar **aprender a ser**).
- **Do meu jeito:** a criança ajusta a moldura. Ajustes feitos pelo professor aparecem para ela: "A professora deixou assim. Você pode mudar." (S9)
- **Modo suave:** um toque que reduz som, cor e movimento **na moldura**, oferecido a todos sem marcação (R38, HIP-5). O nome descreve o efeito, não o estado da criança (S17).
- **Tema de interesse:** muda a ilustração da moldura e dos blocos de treino. No palco de medida, só se o protocolo do CIATec permitir, como parâmetro registrado e com teste de invariância (C3).

## Matriz-resumo

| Mecânica do Duolingo | Engaja | Segura | Fora da medida | Destino no VUOO |
|---|---|---|---|---|
| Lição curta | sim | sim | sim | **Voo** (rotina fixa) |
| XP | sim | não | não | removido |
| Ofensiva que zera | sim | não | sim | **Penas** que só crescem |
| Vidas / energia | médio | não | não | removido |
| Feedback verde/vermelho | sim | parcial | não | **Dois regimes**, na moldura |
| Timer / bônus de velocidade | sim | não | não | barra oculta na medida; sem bônus |
| Trilha | sim | parcial | sim | **Caminho** que só cresce |
| Missões diárias | sim | parcial | parcial | **Plano de hoje** |
| Baús / gemas / loja | sim | não | sim | **Coleção** em marcos, sem contador |
| Ligas | sim | não | sim | **Céu da turma** sem prazo nem falta |
| Mascote que cobra | sim | não | sim | **VUOO Bot** com afeto não contingente |
| Notificações | sim | não | sim | só para o professor, sobre acesso |
| Celebração com % | sim | parcial | não | **Pouso** de participação |
| Prática personalizada | sim | parcial | sim | adaptação entre blocos |
| Teste de nível | médio | parcial | sim | **Primeiro voo** com aviso e assentimento |
| Sessão infinita | sim | não | sim | limite diário com teto |
| Quests de amigos | sim | sim | não | **colaboração** sem medida individual |

## O que medir

**Métrica-norte: crianças com pelo menos 3 dias de voo com captura válida por mês escolar** `[ASSUMIDO]`.
- **Captura válida:** blocos de medida que passam nos critérios de qualidade do CIATec.
- **Interrupção por pausa não invalida o voo:** o bloco interrompido é descartado, o resto conta.
- Conta **crianças**, não voos, para não premiar quem joga mais.

**Guarda-corpos** (S13):
- A taxa de pausas oferecidas e aceitas não pode cair por efeito de mudança de design.
- **Proibido por escrito:** qualquer experimento que reduza a visibilidade da pausa, do Ninho ou do "Agora não".

**Indicadores:**
- **Retorno:** dias de voo por criança por semana escolar. Testa a HIP-1, entre turmas.
- **Conclusão:** % de microjogos iniciados que chegam ao "O que você fez".
- **Preservação da medida:** correlação com o instrumento de referência nos dois braços do PP3 (Bot adaptativo × não adaptativo).
- **Configurações ativas por sessão** (Modo suave, tema, escala, Bot oculto) registradas como covariáveis (C3, C5).
- **Contra-indicadores:** pulos e pausas por voo; triagens de saúde mental do CIATec (`[IN-28]`).
