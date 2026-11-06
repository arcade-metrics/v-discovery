---
etapa: discussão da rodada 3
data: 2026-10-27
---

# Discussão da rodada 3 · execução e consistência

Revisão independente com olhar de designer, desenvolvedor e ilustrador: 33 achados, E1–E33 (`rodada-3-execucao.md`).

## Correção de registro

A discussão das rodadas 1 e 2 dava o **S21** ("todas as divergências entre `.md` e `.html` alinhadas") e o **S15** (alto contraste) como aplicados. **Não estavam.** O HTML ainda dizia "6 a 11 anos", mantinha superlativos que o C21 mandou tirar, e o botão de Modo suave pintava o palco de medida, logo abaixo do texto que dizia que ele não muda. O alto contraste continuava `[A FAZER]`.

**O que mudou no método:** criei uma fonte única para fluxo, falas e Bot (`06-especificacao-base.md`, D-23) e reescrevi a página visual do zero, em vez de remendá-la. Ela agora declara que, em caso de divergência, os `.md` prevalecem.

## Decisões

| # | Decisão | O que mudou |
|---|---|---|
| E1 | **aceito** | Canal de voz por configuração de fone do aparelho (D-21). Tabela de falas com ID, `.texto`, `.voz` e canal em `06` §3–4. Número nunca é falado. A tabela de falas de `03` virou ponteiro para `06`. |
| E2 | **aceito** | O Bot faz **o mesmo gesto em todo toque**, certo ou errado. O retorno de competência fica no alvo (marimba no alvo certo). No recuo, o Bot não muda de expressão. "Pensando" só no carregamento. |
| E3 | **aceito** | Estados do Bot com expressão, antena, movimento, piscar e duração; matriz evento → reação; prioridade entre eventos (`06` §5). **A antena é só emoção** (D-22): a câmera virou pictograma e rótulo na moldura. "Imóvel na medida" inclui não piscar. |
| E4 | **aceito** | Mapa de fluxo da criança e do professor (`06` §1–2). O Caminho é a tela inicial. Pular fica na tela "Próximo" e na Pausa. O 2º voo em aparelho compartilhado começa num rodízio seguinte. "Sobre" fica dentro do "Do meu jeito". |
| E5 | **aceito** | O palco de medida e o painel redefinem os tokens do modo padrão, e o Modo suave só alcança os mockups da criança. |
| E6 | **aceito** | Tabela completa de tokens nos três modos em `paleta.json` e em `03` §5. Precedência em `06` §6. A intensidade de celebração passa a se chamar quieta, padrão e festa. |
| E7 | **aceito** | Novo token `sol-icone` (`#B07A1C`, 3,4:1) para penas e próximo voo sobre fundo claro. Borda de alvo em `contorno`. Contorno de pista em `lavanda-tinta`. Traço obrigatório no casco. 40 pares validados. |
| E8 | **aceito em parte** | Escala de espaço, raio, foco, alvo do adulto, movimento, tipografia e estados em `06` §7. Os mockups estão anotados como "escala 0,75". A biblioteca de componentes com anatomia completa fica para a consultoria (P33). |
| E9 | **aceito** | O jogo de memória passa a se chamar "Luzes em Ordem" e "Cuidar do Ninho" vira "Casa do Bot". Regra na ficha-modelo: o nome de um jogo não pode coincidir com termo do sistema. |
| E10 | **aceito** | A peça escolhida não precisa de aviso. Mudanças impostas pelo sistema são avisadas no início do voo, sem falar em amanhã (`bot.mudanca`). |
| E11 | **aceito** | Os oito itens corrigidos na reescrita do HTML. |
| E12 | **aceito** | No mockup de medida, o Bot fica imóvel e sem piscar e a instrução é texto estático. O pictograma atual usa `ceu`, e "esperar" foi trocado por "não tocar". |
| E13 | **aceito** | Strings com ID, plural e escopo de `{n}` em `06` §4. O fim de medida usa o nome próprio do jogo. |
| E14 | **aceito** | A pista usa a instrução do treino: "Esse não. Toque na figura que começa com bê." |
| E15 | **aceito** | Convenção: pares sempre na ordem visual, recusar à esquerda ("Agora não / Jogar"). |
| E16 | **aceito** | As 9 fases de `04` são canônicas. Cada bloco de treino tem um nome falado na ficha-modelo. |
| E17 | **aceito** | Jogo pulado sai do Plano de hoje sem marca. |
| E18 | **aceito** | Constelação = crianças × 5. Só se desenham as estrelas acesas e as linhas entre elas. "Ver quem" não existe. Texto do Céu em token, com tamanho mínimo para projeção. |
| E19 | **aceito** | Regra do rótulo reescrita (título = ação observável aprovada na ontologia). "Partida" × "voo". Chips com ícone, em `ceu-claro`; o sinal se distingue por ícone e texto, não por âmbar. Estados depois dos botões em `06` §2. O cartão do Bruno ficou completo. |
| E20 | **aceito** | Entrelinha por nível, tracking em em, pesos e regra de reflow em `06` §7. "Caixa alta" × "sem serifa" corrigido. |
| E21 | **aceito em parte** | Sossegado redesenhado (pálpebra reta com pupila visível, boca em curva leve). Curioso com o olho esquerdo fixo, Pensando olhando para cima e para a direita, traço do casco, olhos do logotipo alinhados com o Atento. A folha de modelo completa fica com o ilustrador (P31). |
| E22 | **aceito** | HIP-2 reescrita com os braços seguros de `03` §5. |
| E23 | **aceito** | Espelhar e Celebrar são comuns aos dois braços do PP3. Só Convidar e Recuar são adaptativos. |
| E24 | **aceito** | Penas no topo do Caminho; a cada 10, um galho; a pena do dia tem anel. |
| E25 | **aceito** | Alto contraste entregue e validado (tokens `ac-*`). |
| E26 | **aceito** | Gatilho do convite: introduzir um microjogo que a criança ainda não jogou. A dificuldade dentro de um jogo muda sem convite. |
| E27 | **aceito** | "Calmo" removido do HTML, do JSON e do resultado. CSS órfão removido. |
| E28 | **aceito em parte** | O mockup de treino com pista foi adicionado. Pausa → Ninho e escolha de peça ficam para a consultoria (P34). |
| E29 | **aceito** | `lang` definido por script (o esqueleto de publicação não permite `<html>` próprio), `role` nos rótulos, regiões roláveis focáveis, rótulo fixo no botão de alternância com `aria-describedby`, piscar limitado a 3 ciclos, alvos de 44 px no painel, cores decorativas em tokens. |
| E30 | — | Verificação, sem ação. |
| E31 | **aceito** | "Uma ação pedida por frase"; até 8 palavras, com exceção declarada para os avisos; sem personificação; "{A professora / O professor}"; "Agora: próximo jogo." |
| E32 | **aceito em parte** | Nomes alinhados nas falas. O inventário de pictogramas fica para a consultoria (P33). |
| E33 | **aceito** | D-09 reescrita (o go/no-go fica no palco); `superficie` = palco no treino; Ponte em Dupla confirma forma, não só cor; aviso de fim só entre blocos; período de 2 s no pulso; volumes de som pendentes em LUFS. |

## O que esta rodada mudou de fundo

1. **O estudo ganhou uma fonte única.** Antes, cada regra vivia em dois ou três lugares, e as revisões corrigiam um e deixavam o outro.
2. **O Bot virou especificável.** Com estados, matriz evento → reação e critério de aceite ("nenhuma transição tem como entrada acerto ou erro"), um animador e um desenvolvedor conseguem trabalhar sem o autor.
3. **A voz deixou de ser um detalhe.** Em sala sem fone, o canal de voz é o lugar onde a adaptação de uma criança fica pública. Agora isso é uma configuração explícita.
