---
titulo: "Apêndice: estudo de caso VUOO"
capitulo: apendice
atualizado_em: 2026-10-29
origem: produtos/vuoo-linguagem/ (02-gamificacao.md, 03-linguagem.md, 05-decisoes.md), 27/10/2026
---

# Apêndice · Estudo de caso: a tradução feita para o VUOO

Um exemplo concreto de como a matriz do cap. 00 §6 e os guarda-corpos do cap. 05 §3 viraram decisões de produto. O VUOO é um conjunto de microjogos para crianças de **6 a 11 anos** com TEA, TDAH, dislexia ou DCD, usado **em sala, mediado pelo professor**, na rede pública de São Paulo, em cooperação com um centro de pesquisa que também usa os microjogos para **medir** construtos cognitivos. Essa última condição adiciona uma restrição que nem toda plataforma terá: a gamificação não pode tocar o "palco de medida".

Os documentos completos estão em `produtos/vuoo-linguagem/`. Aqui vai só o mapa.

## 1. A ideia que organiza

> O Duolingo recompensa o resultado e pune a ausência. O VUOO reconhece a presença e não pune nada.

Toda mecânica passa por três perguntas: **engaja?** (a criança volta?), **é segura?** (funciona sem medo de perder, comparação, culpa, imprevisibilidade, sobrecarga?), **fica fora da medida?** (não altera o estímulo nem a resposta que o microjogo mede?). Só entra se passar nas três; quando falha em uma, é transformada.

## 2. Onde a gamificação mora

Toda tela tem duas zonas: o **palco de medida** (estímulos definidos pelo protocolo de pesquisa, congelados; nada de tema, modo suave, Bot ou variante de A/B entra ali) e a **moldura** (tudo o que está fora do palco e entre blocos). A gamificação vive só na moldura.

## 3. Vocabulário: Duolingo → VUOO

| Duolingo | VUOO | O que muda |
|---|---|---|
| Lição | **Voo** | 3 microjogos, sempre o mesmo número, mesma rotina em 9 fases (o que vem → demonstração → prática → "pronto?" → …) |
| Exercício | **Microjogo** | atividade com bloco de medida e/ou de treino |
| Missões diárias | **Plano de hoje** | faixa com os pictogramas dos microjogos do voo, sempre visível, definida pelo professor |
| Caminho | **Caminho** | mapa pessoal em que cada dia de voo desenha mais um trecho; **só cresce** |
| Ofensiva | **Penas** | uma pena por dia em que voou, numa fileira que só cresce; sem dias da semana, sem casas vazias, sem total numérico |
| Baús, gemas, loja | **Coleção** | peças para o Bot entregues em marcos fixos de dias de voo, sem contador e sem anúncio |
| Ligas | **Céu da turma** | constelação coletiva: cada criança que voou acende uma estrela; sem prazo, sem falta |
| Tela de fim de lição | **Pouso** | uma tela, de participação, sem porcentagem |
| Duo (que cobra) | **VUOO Bot** | par previsível, afeto não contingente ao desempenho |
| XP | — | removido |
| Vidas / energia | — | removido |
| Notificações | — | só para o professor, sobre acesso |
| (não existe) | **Ninho** | espaço de pausa com opções calmas, oferecido em pontos fixos |
| (não existe) | **Modo suave** | menos som, cor e movimento na moldura, a um toque, sem marcação |

"Voo" é substantivo próprio da sessão e nunca verbo nem figura de linguagem para a criança: o botão é "Jogar de novo", não "Voar de novo".

## 4. Matriz-resumo

| Mecânica do Duolingo | Engaja | Segura | Fora da medida | Destino |
|---|---|---|---|---|
| Lição curta | sim | sim | sim | Voo (rotina fixa) |
| XP | sim | não | não | removido |
| Ofensiva que zera | sim | não | sim | Penas que só crescem |
| Vidas / energia | médio | não | não | removido |
| Feedback verde/vermelho | sim | parcial | não | dois regimes, na moldura |
| Timer / bônus de velocidade | sim | não | não | barra oculta na medida; sem bônus |
| Trilha | sim | parcial | sim | Caminho que só cresce |
| Missões diárias | sim | parcial | parcial | Plano de hoje |
| Baús / gemas / loja | sim | não | sim | Coleção em marcos, sem contador |
| Ligas | sim | não | sim | Céu da turma, sem prazo nem falta |
| Mascote que cobra | sim | não | sim | VUOO Bot com afeto não contingente |
| Notificações | sim | não | sim | só para o professor |
| Celebração com % | sim | parcial | não | Pouso de participação |
| Prática personalizada | sim | parcial | sim | adaptação entre blocos |
| Teste de nível | médio | parcial | sim | Primeiro voo com aviso e assentimento |
| Sessão infinita | sim | não | sim | limite diário com teto |
| Quests de amigos | sim | sim | não | colaboração sem medida individual |

## 5. O que medir

**Métrica-norte:** crianças com pelo menos 3 dias de voo com captura válida por mês escolar. Conta **crianças**, não voos, para não premiar quem joga mais.

**Guarda-corpos:** a taxa de pausas oferecidas e aceitas não pode cair por efeito de mudança de design; é proibido por escrito qualquer experimento que reduza a visibilidade da pausa, do Ninho ou do "Agora não".

**Indicadores:** dias de voo por criança por semana escolar; % de microjogos iniciados que chegam ao fim; preservação da medida (correlação com o instrumento de referência nos braços com e sem Bot adaptativo); configurações ativas por sessão como covariáveis; pulos e pausas por voo como contra-indicadores.

## 6. O que esse caso ensina para uma plataforma mais ampla

1. Separar **onde a gamificação pode agir** de onde não pode (no VUOO, por causa da medida; em outras plataformas, por causa do conteúdo pedagógico ou da avaliação).
2. Dar **nomes próprios e literais** às mecânicas adaptadas, em vez de reaproveitar os nomes do Duolingo com significado trocado.
3. Escrever os guarda-corpos **antes** dos experimentos, incluindo o que é proibido testar.
4. Fazer a métrica-norte contar **pessoas que participam**, não volume.
5. Tratar o modo de baixa estimulação e a pausa como recursos **para todos**, sem marcar a criança que os usa.
