---
produto: VUOO
slug: vuoo-microjogos
etapa: decisoes
status: vivo
atualizado_em: 2026-11-06
---

# Decisões e questões abertas do produto

Dono único das decisões de produto `D-nn` e das questões abertas `A-nn` dos microjogos. Os outros documentos citam o código e apontam para cá; não repetem o texto.

## Séries de código

| Série | O que é | Onde mora |
|---|---|---|
| `D-01` a `D-23` | Decisões do estudo anterior de linguagem. **Precedente**: só valem se uma decisão daqui as adotar. | [base/precedente-linguagem/05-decisoes.md](base/precedente-linguagem/05-decisoes.md) |
| `D-24` em diante | Decisões de produto. A numeração continua a do precedente para não haver dois `D-01` no mesmo produto. | este arquivo, §1 |
| `INF-01` a `INF-22` | Decisões de infraestrutura e dados. | [base/relatorio-infra-vuoo.md](base/relatorio-infra-vuoo.md) §7 |
| `A-nn` | Questões abertas de estilo e identidade. | este arquivo, §2 |
| `P-nn`, `M-nn` | Pontas soltas do PRD e do MVP. | [02-prd.md](02-prd.md) §14, [03-mvp.md](03-mvp.md) §8 |
| `RN-nn`, `ADR-nn` | Regras de negócio e decisões de arquitetura. | [regras/](regras/LEIAME.md), [padroes/](padroes/LEIAME.md) |

Não confundir: `D1` a `D8` sem hífen são os **domínios do Core** (D1 organização acadêmica, D3 pessoas…), definidos em [base/_convencoes.md](base/_convencoes.md); `D1` a `D37` nas fichas do SAEB são **descritores** oficiais da matriz; `HIP-1` e `HIP-2` são as hipóteses do [00-brief.md](00-brief.md), e as `HIP-1` a `HIP-6` do precedente são outras, citadas sempre como `[PRECEDENTE HIP-n]`.

## 1. Decisões de produto

Tomadas pelo usuário em 30/10/2026; o estudo que as fundamenta é `base/parametrizacao-estilo.md`.

| Código | Decisão |
|---|---|
| **D-24** | Público-base: **ensino fundamental (anos iniciais e finais) e ensino médio**, aproximadamente 6 a 17 anos, incluindo o público da educação especial. |
| **D-25** | Dois lados: aluno (jogador) e professor/gestor. O estudo de estilo trata só do aluno. |
| **D-26** | Fundamentos: desenho universal, design centrado no ser humano e DUA. |
| **D-27** | O estilo é **adaptativo e parametrizado**: movimento, cor, som, tamanho e demais eixos são configuráveis. O **padrão é moderado**, mas o sistema é projetado para funcionar nos **dois extremos** (mínimo e máximo). |
| **D-28** | Há **muitos presets**, além de **personalização** pelo aluno, que pode salvar a própria combinação. |
| **D-29** | Arte, estilo, wireframes e componentes **partem da parametrização**. Numa fase posterior, os parâmetros serão **acionáveis por IA**. |
| **D-30** | O produto é o **VUOO**. Isto amplia o público das propostas (1º ao 5º ano em `[IN-06]` e na proposta do CIATec) para o fundamental inteiro e o médio. |
| **D-31** | **Identidade visual começa do zero**: paleta, tipografia, personagem e marca. As propostas de identidade do estudo anterior (cor `ceu`, Bot, Andika) ficam como precedente, não como ponto de partida. É a primeira frente de design. |
| **D-32** | O orçamento de produção das variantes (animação, som, estéticas, Libras, audiodescrição) é ajustado **depois do primeiro ciclo completo de uma atividade e dos testes**. Desenvolve-se desde já prevendo essa fase. |
| **D-33** | O VUOO é **aplicativo** (Android e iOS, smartphone e tablet), sobretudo para o aluno, e **também precisa funcionar na web**. |
| **D-34** | O cliente do aluno é feito em **Flutter** desde o início, *mobile first*. A versão web do aluno é o build web do mesmo código (D-36). |
| **D-35** | A primeira versão construída chama-se **v0.0.0**, não "protótipo". Antes dela, escreve-se uma documentação orientadora para o seu desenvolvimento. |
| **D-36** | **Aluno:** Flutter no app (Android e iOS) e o build web do mesmo código como secundário; atividades com medida só no app. **Professor e gestor:** web em React. **Tokens de estilo** em arquivo único no formato W3C Design Tokens, lido pelos dois. |
| **D-37** | **Animação em três camadas.** *Código Flutter*: interface e peças simples de jogo (escala, posição, cor, rebote), guiadas pelos tokens de movimento. *Rive*: personagens e peças interativas com estados; custo por animador, runtime MIT, arquivos exportados seguem funcionando sem assinatura. *After Effects → Lottie*: animações lineares (celebrações, conquistas, aberturas, ícones), com guia de recursos suportados para aparelhos fracos. Alternativa registrada caso o Rive seja vetado: Spine (licença única). |

## 2. Questões abertas

| # | Pergunta | Situação / quem responde |
|---|---|---|
| A-01 | ~~Nome e slug do produto~~ | resolvido: VUOO (D-30) |
| A-02 | Padrões por etapa: alvo (64/56/48), fonte, leitura automática, agenda | usuário + co-design |
| A-03 | Música no padrão moderado: só no mapa (proposta) ou desligada | usuário |
| A-04 | ~~Quais 4 bases aparecem na calibração inicial~~ | resolvido: não há calibração no primeiro acesso; o estilo fica nas configurações, com 3 bases na v0.0.0 ([02-prd.md](02-prd.md) §5 e §8) |
| A-05 | Posição dos controles fixos (a regra de que não mudam de lugar já vale) | design |
| A-06 | Nível de autonomia inicial da IA (proposta: 1) e quem autoriza os níveis 2 e 3 | usuário + jurídico |
| A-07 | Família pode sugerir ajustes? | usuário |
| A-08 | ~~Stack e ferramenta de animação~~ | resolvido: D-34, D-36, D-37 |
| A-09 | ~~Haverá atividades com medida?~~ | resolvido: sim, a avaliação em momentos marcados, com estímulos protegidos de estilo e mecânicas ([02-prd.md](02-prd.md) §7). O protocolo (quais tarefas, frequência, quem define) segue aberto como **P-08** do PRD |
| A-10 | Orçamento de produção das variantes | adiado para depois do primeiro ciclo (D-32) |
| A-11 | Recompensa aleatória e eventos-surpresa: fora por princípio ou por configuração | usuário, depois de `gam.*` |
| A-12 | Paleta, tipografia, personagem e marca (logotipo, nome do personagem) | primeira frente de design (D-31). É a mesma pendência que a **P-11** do PRD |
| A-13 | Linguagem de formas dominante (redonda, blocada ou afunilada) | design, a partir dos esboços em [exemplos-de-design/](../../exemplos-de-design/) |
| A-14 | A metáfora do voo e o vocabulário (Caminho, Ninho, Pouso, Penas, Céu) continuam? | usuário; proposta do precedente (D-02) |
| A-15 | Tom de voz para anos finais e ensino médio (tamanho de frase, registro, humor) | usuário + co-design |
| A-16 | Conjunto de pictogramas próprio para o público ampliado | design (precedente D-15) |
