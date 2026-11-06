---
titulo: Visão geral do Duolingo como referência
capitulo: 00
atualizado_em: 2026-10-29
estado_de_referencia: Duolingo, outubro de 2026 (iOS/Android), cursos de idiomas, Math, Music, Chess
publico_do_benchmark: plataforma de jogos sérios para educação especial (uso amplo)
marcas: "[V] fonte primária · [S] fonte secundária · [I] inferência"
---

# 00 · Visão geral

## 1. A tese em um parágrafo

O Duolingo é um produto de **retenção diária**. Entre 2018 e 2022 o time de produto descobriu, com um modelo de simulação, que a alavanca de maior impacto no número de usuários ativos diários (DAU) era a **CURR** (Current User Retention Rate: a chance de alguém ativo hoje, e ativo em pelo menos um dos 6 dias anteriores, continuar ativo amanhã). Mexer na CURR teve cerca de **5x** o impacto da segunda alavanca; em 4 anos a CURR subiu 21%, o churn diário dos melhores usuários caiu mais de 40% e o DAU cresceu 4,5x [V]. Quase toda a gamificação (ofensiva, ligas, missões, notificações, baús) existe para **fazer a pessoa voltar amanhã**, não para ela aprender mais em cada sessão. A empresa mesma admitiu o viés e criou uma métrica de "tempo aprendendo bem" (TSLW) para corrigi-lo (cap. 01 §1 e cap. 04).

Imagens: `00-visao-modelo-de-crescimento-baldes-de-usuarios.png`, `00-visao-curr-composicao-diagrama.jpg`, `00-visao-simulacao-sensibilidade-alavancas-dau-mau.jpg`, `00-visao-dau-crescimento-4-5x-apos-curr.jpg`.

Fontes: https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth · https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks

## 2. Os três andares do sistema

Uma forma útil de ler o produto (Deconstructor of Fun, abr/2025 [S]; imagens `00-visao-dof-*`):

| Andar | Pergunta que responde | Mecânicas |
|---|---|---|
| **Meta** | Por que eu uso este produto? | Compromisso explícito escolhido no onboarding (meta diária, meta de ofensiva), mapa da jornada (caminho com seções e unidades), assinatura Super/Max |
| **Fun** | Por que estou animado hoje? | Core loop de 3 a 5 minutos: exercício → feedback imediato → progresso visível; variedade de formatos; personagens; recompensas (XP, baú), missões diárias, eventos cronometrados |
| **Lock-in** | Por que volto amanhã? | Ofensiva, pressão social (Friends Quest, Friend Streak), pressão de status (liga semanal), baús diários, lembretes por push, e-mail e widget |

O que faz o conjunto funcionar é a **sobreposição de prazos**: a cada item (segundos), a cada lição (minutos), a cada dia (ofensiva, missões), a cada semana (liga, Friends Quest), a cada mês (insígnia), a cada marco (7, 30, 50, 100, 365 dias). Sempre há algo prestes a vencer.

## 3. O loop central, em 60 segundos

1. **Abrir**: home com caminho linear; o nó ativo pulsa; "START +35 XP" (`02-gameplay-caminho-popup-licao-start-35xp.png`).
2. **Lição**: ~15 exercícios, 2 a 5 min, formatos alternados (tocar, montar, ouvir, falar, parear). Começa fácil (reconhecer) e termina difícil (digitar). Barra de progresso no topo.
3. **Feedback por item**: faixa verde com elogio e som ascendente, ou faixa vermelha com a resposta correta e som descendente; o personagem reage; combo a cada 5/10 acertos. O item errado volta no fim.
4. **Fim**: fanfarra, XP, precisão, tempo; depois uma cascata de telas: ofensiva, missões diárias, liga, baú, conquista (`02-gameplay-fim-de-licao-*`, `01-recompensas-*`).
5. **Amanhã**: notificação escolhida por um algoritmo *bandit*; widget com o Duo cada vez mais aflito até a meia-noite (`01-recompensas-widget-*`).

Detalhes no cap. 02.

## 4. Glossário

| Termo | O que é |
|---|---|
| **XP** | Pontos por atividade. Alimentam meta diária, ligas, missões. ~35 por lição nova (2025) |
| **Ofensiva** (streak) | Dias consecutivos com ao menos uma lição. Congelamento, reparo, Perfect Streak, Streak Society |
| **Liga** | Ranking semanal de ~30 pessoas por XP, 10 divisões, promoção/rebaixamento |
| **Missões** (quests) | 3 diárias, mensal (insígnia), de amigos (semanal), de família |
| **Gemas** | Moeda. Compra congelamento, recarga de energia, desafios cronometrados, reparo de liga |
| **Baú** | Recompensa de conteúdo variável (gemas, boost, congelamento) |
| **Corações → Energy** | Vidas (até 2025) → barra de energia gasta por exercício (2025+) |
| **Caminho** (path) | Trilha linear única (desde nov/2022) que substituiu a árvore de habilidades |
| **Seção > Unidade > Nível > Lição** | Hierarquia do curso; unidades alinhadas ao CEFR |
| **Legendary** | Replay mais difícil de um nó concluído; nó fica dourado |
| **Practice Hub** | Aba de prática: erros, palavras, fala, escuta, histórias, rádio |
| **Birdbrain** | Modelo de IA que estima P(acerto) por exercício e pessoa; monta a lição |
| **TSLW** | Time Spent Learning Well: proxy de aprendizagem usado nos testes A/B |
| **Super / Max** | Assinaturas. Super: sem anúncios, energia ilimitada. Max: + Video Call e Roleplay com IA |
| **Duo** | Mascote-coruja. No app, coach; nas redes, persona "unhinged" |
| **World Characters** | Elenco de 10 personagens com voz, personalidade e visemas |
| **Shape language** | Regra de ilustração: tudo a partir de retângulo arredondado, círculo e triângulo arredondado |
| **Rive** | Ferramenta de animação com máquina de estados, usada nos personagens |

## 5. O que o próprio Duolingo tira quando desenha para crianças

O **Duolingo ABC** (alfabetização, 3 a 8 anos) não tem anúncios, compras, ligas, moeda nem social; o estilo visual arredondado de hoje nasceu no Duolingo Kids em 2018 [V/S]. É o sinal mais forte de que "a jogabilidade do Duolingo" que vale a pena copiar para crianças é **o loop de lição + feedback + personagem + progresso visível**, e **não** ofensiva com perda, ligas, corações e culpa (cap. 02 §6 e cap. 05).

## 6. Matriz de decisão (recomendação para uma plataforma de educação especial) [I]

Vereditos gerais. O cap. 05 detalha por perfil de aluno; a seção 7 resume como traduzir uma mecânica.

| Mecânica | Veredito | Por quê, em uma linha | Forma adaptada |
|---|---|---|---|
| Lição curta, feedback imediato, barra de progresso | **Adotar** | Evidência robusta; funciona para quem tolera pouco a espera | Sessão de 1 a 3 min; feedback multimodal (voz + animação + ícone); erro em cor neutra; teto de itens extras |
| Fim de lição com celebração | **Adotar, enxuto** | Reforço informativo ajuda; cascata de 5 telas sobrecarrega | Uma tela, um reforço, um próximo passo; respeitar modo de baixa estimulação |
| Personagem com reação (Rive) | **Adotar** | Dá previsibilidade e afeto; técnica leve | Máquina de estados; reação ao erro = curiosidade, nunca tristeza |
| Shape language, espaço branco, botão 3D | **Adotar** | Baixa carga visual; alvos grandes | + modo de baixa estimulação, código duplo cor+forma |
| Adaptação de dificuldade (Birdbrain) | **Adotar** | Maior valor pedagógico, menor risco | Taxa de acerto alvo alta; ajuste visível e editável pelo educador |
| Caminho linear | **Adaptar** | Previsibilidade ajuda; bloqueio duro trava | Próximo passo claro + educador reordena + rotas por modalidade |
| Missões | **Adaptar** | Cooperativas são aproveitáveis; de desempenho excluem | Missões de grupo, de esforço/exploração, anunciadas com antecedência |
| Conquistas | **Adaptar** | Cumulativas são seguras; de tempo/desempenho não | Nunca se perdem; todas alcançáveis; ligadas a habilidades |
| XP numérico | **Substituir** | Premia volume; só faz sentido em comparação | Progresso concreto e não numérico, ligado a domínio |
| Ofensiva diária | **Substituir** | Perda leva ao abandono; acesso diário não é dado | Contador que só cresce; ritmo coletivo pausado pelo calendário |
| Ligas / ranking | **Não usar** | Expõe os mesmos alunos na lanterna | Meta coletiva; dados individuais só no painel do educador |
| Corações / Energy | **Não usar** | Interrompe quem mais precisa praticar | Errar nunca interrompe; tempo é do educador |
| Gemas, baús aleatórios, loja | **Não usar** | Recompensa variável ≈ loot box; risco legal no Brasil | Recompensas determinísticas e anunciadas |
| Notificações com culpa | **Não usar** | Ironia é lida literalmente por parte do público | Sem push para a criança; informação ao responsável/educador |
| Social por "amigos" | **Não usar** | Amplifica exclusão; LGPD/ECA Digital | Grupo fechado como unidade |
| Humor sarcástico / "unhinged" | **Não usar** | Ambíguo e potencialmente angustiante | Humor físico e literal; personalidade estável |
| Métrica de aprendizagem (TSLW) | **Adotar o princípio** | Até o Duolingo precisou corrigir a gamificação | Métrica-norte de habilidades consolidadas, não de DAU |

## 7. Como traduzir uma mecânica sem copiá-la [I]

1. Separar **onde a gamificação pode agir** de onde não pode: a avaliação, o conteúdo pedagógico ou qualquer medida ficam fora do alcance de recompensas, temas e testes A/B.
2. Dar **nomes próprios e literais** às mecânicas adaptadas, em vez de reaproveitar os nomes do Duolingo com significado trocado.
3. Escrever os guarda-corpos **antes** dos experimentos, incluindo o que é proibido testar (por exemplo, reduzir a visibilidade da pausa).
4. Fazer a métrica-norte contar **pessoas que participam**, não volume, para não premiar quem joga mais.
5. Tratar o modo de baixa estimulação e a pausa como recursos **para todos**, sem marcar quem os usa.

## 8. Como os capítulos se relacionam

```
00 visão ─┬─ 01 recompensas ──┐
          ├─ 02 gameplay ─────┼─ 04 evidências e críticas ─ 05 riscos por perfil
          └─ 03 estilo ───────┘
```

Cada mecânica em 01, 02 e 03 tem um campo "risco na educação especial" curto; o cap. 05 consolida por perfil de aluno e o cap. 04 reúne a força da evidência.
