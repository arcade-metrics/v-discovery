---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-microjogos
etapa: 99-pendencias
status: em revisão
atualizado_em: 2026-10-27
---

# 99 · Pendências

Tudo o que este estudo assumiu, não conseguiu confirmar ou depende de decisão de outra pessoa. Organizado por **quem responde**.

## Para o dono do produto (Wemoga)

| # | Pendência | Por que importa | Onde aparece |
|---|---|---|---|
| P1 | Confirmar a arquitetura de marca: VUOO autônomo, CIATec e FAPESP em endosso textual | Muda logotipo, créditos e telas | D-01 |
| P2 | Número do processo FAPESP para o bloco de créditos | Citação obrigatória pelo Termo de Outorga | `03` §1 |
| P3 | Uso individual ou compartilhado de aparelho nas escolas do piloto | Muda colaboração, login, botão "Jogar de novo" | `01`, D-14 |
| P4 | Há fone de ouvido nas escolas? | Define o canal de áudio padrão | `03` §4 e §10 |
| P5 | Limite diário padrão (2) e teto (3) | Uso compulsivo × volume de dados para o gêmeo | D-14 |
| P5b | Período em que um sinal marcado como "Já encaminhado" não reaparece (30 dias assumidos) | Evitar alerta repetido × perder mudança real | `06` §2 |
| P6 | Número de microjogos por voo (3) | Rotina e tempo de rodízio | `02` §1 |
| P7 | Métrica-norte: "crianças com ≥ 3 dias de voo com captura válida por mês escolar" | Orienta o time | `02`, O que medir |
| P8 | Orçamento de produção: conjunto próprio de pictogramas, vídeos em Libras, voz gravada, animação Rive do Bot, galeria de avatares | Não está no orçamento do PIPE como item; pode caber na consultoria de design instrucional | `03` §4, §7; `04` |
| P9 | Interface de família: só relatório imprimível? | O CIATec fala em vínculo escola-família | `03` §13 |

## Para o CIATec

| # | Pendência | Por que importa |
|---|---|---|
| P10 | **Núcleo de medida**: estímulos (mm, cor, contraste), tempos, número mínimo de tentativas e retorno por tentativa de cada instrumento | Define o palco de medida e a duração de cada microjogo (D-20, C6) |
| P11 | Aprovar a **regra de composição da dupla camada** e os 7 conceitos de `04` | Parecer de preservação (E1.3) |
| P12 | Tema de interesse pode entrar no palco de medida? Com teste de invariância? | Engajamento × validade (C3) |
| P13 | O que são as "classificações" do estudo de prova de conceito e do estudo de mundo real? | Se forem ranking entre crianças, conflitam com os invariantes de segurança |
| P14 | Aceitar a proposta para o A/B/n (invariantes, variáveis com candidatos, restrições de medida) | O desenho é do CIATec (C13) |
| P15 | Onde rodam HIP-3, HIP-4 e HIP-6 (estudo de usabilidade PT2, grupos focais de estudantes)? | As hipóteses com crianças precisam de estudo e de CEP (C18) |
| P16 | Meios alternativos de ação (voz, olhar, acionador): quais viram perfil de parâmetros e quais ficam só no treino? | DUA ação e expressão (C11, S15) |
| P17 | Os 4 jogos do CIATec rodam dentro do VUOO? Com o Bot? | Governança aberta (D-18) |
| P18 | Mínimo de sessões antes de um sinal de atenção; limiares dos comportamentos do Bot | Parâmetros de CMS (D-17, C25) |

## Para a assessoria jurídica (já orçada no PIPE)

| # | Pendência |
|---|---|
| P19 | Base legal e RIPD para o dado "tem Plano Educacional Individualizado" (D-19) |
| P20 | Personagem, marca e arte do Bot no acordo de PI (F1.1, E5.5) (D-18) |
| P21 | Câmera (Wemoga Eye): base legal, aviso, assentimento, o que é guardado (dado de imagem de criança) |
| P22 | Licença de pictogramas: confirmar que o ARASAAC não pode ser usado em SaaS e que o conjunto próprio não infringe |
| P23 | Conformidade do Céu da turma, da coleção e do limite diário com o ECA Digital (arts. 17, 18, 20) e o AADC |
| P24 | O Decreto SP 67.635/2023 citado no VUOO não foi encontrado no repositório da ALESP pela pesquisa `d`. **Conferir o número**: a proposta do PIPE o cita várias vezes |

## Para a consultoria de design instrucional e o co-design

| # | Pendência |
|---|---|
| P25 | Códigos BNCC / Currículo Paulista de cada bloco de treino (marcados `[A CONFIRMAR]` em `04`) |
| P26 | Teste do vocabulário do painel (2 ou 3 variantes) medindo tempo e acurácia de identificação, antes do F4.3 (D-17) |
| P27 | Teste do som de pista: "o que esse som quer dizer?" (S12) |
| P28 | O espelhar do Bot é lido como imitação zombeteira? (S17) |
| P29 | Formato de saída para o Plano Educacional Individualizado aceito pelas secretarias (F4.1) |
| P30 | Desenho final do logotipo e do Bot por designer de marca e ilustrador |
| P31 | Folha de modelo do Bot: turnaround, proporções, grade de luz do visor com as 5 expressões em coordenadas, tamanhos por contexto (`06` §9) |
| P32 | Tokens em JSON (W3C Design Tokens) a partir de `ferramentas/paleta.json` e `06` §7 |
| P33 | Biblioteca de componentes com anatomia e estados em 360 px e tablet; inventário de pictogramas com nome canônico |
| P34 | Mockups de treino com pista, Pausa → Ninho e escolha de peça; volumes de som em LUFS |

## Hipóteses assumidas sem dado

- `[ASSUMIDO]` A maioria das crianças do 1º ano não lê com autonomia; o canal primário é voz + imagem.
- `[ASSUMIDO]` Rodízio de aparelho de 10 a 15 minutos por criança.
- `[ASSUMIDO]` Sala barulhenta, sem fone.
- `[ASSUMIDO]` As expressões e os comportamentos do Bot (as definições operacionais de espelhar, provocar, celebrar, recuar) são proposta deste estudo, não especificação do projeto.

## Afirmações que precisam de verificação na fonte primária

Vieram de resumos secundários na pesquisa (`pesquisa/b-neurodivergencia.md`, `pesquisa/a-duolingo.md`):
- Prevalência de hiper-responsividade sensorial e hiperacusia no TEA (Ben-Sasson; Williams 2021).
- Leitura de emoção em rostos de desenho por crianças autistas (Brosnan 2015; Rosset; Pino).
- +28% de eficácia do Duolingo ABC (sem fonte primária).
- Número de exercícios por lição do Duolingo.
