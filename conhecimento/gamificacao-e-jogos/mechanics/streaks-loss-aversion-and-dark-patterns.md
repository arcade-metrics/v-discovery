---
id: gam.mech.streaks-loss-aversion-and-dark-patterns
titulo: Ofensivas, aversão à perda, recompensa variável e padrões manipulativos
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [silverman2023broken, kahneman1979prospect, tversky1991loss, zagal2013dark, deterding2020against, gray2018dark, mathur2019dark, oecd2022dark, zendle2018video, zendle2019adolescents, king2018predatory, ico2020aadc, lei15211ecadigital]
relacoes:
  - { tipo: relacionado-a, alvo: gam.mech.points-badges-leaderboards }
  - { tipo: relacionado-a, alvo: gam.mech.core-loops-and-progression }
  - { tipo: relacionado-a, alvo: gam.motiv.intrinsic-extrinsic-and-overjustification }
  - { tipo: especificado-por, alvo: psg.legal.eca-and-digital-eca }
  - { tipo: relacionado-a, alvo: acs.part.self-determination }
  - { tipo: relacionado-a, alvo: dat.ethics.research-vs-operation }
  - { tipo: relacionado-a, alvo: lae.ind.engagement-indicators }
  - { tipo: relacionado-a, alvo: lms.case.duolingo }
termos: [ofensiva, streak, sequência registrada, reparo de ofensiva, vidas, aversão à perda, ponto de referência, recompensa variável, caixa de recompensa, loot box, padrão manipulativo, dark pattern, dark game design pattern, playing by appointment, uso compulsivo, sticky features]
---

# Ofensivas, aversão à perda, recompensa variável e padrões manipulativos

## Definição e terminologia

- **Ofensiva (streak)**: comportamento registrado em dias ou sessões consecutivos. Silverman e Barasch definem streak como "behaviors performed consecutively three or more times" e estudam a **sequência registrada** (logged streak), exibida ao usuário por um aplicativo [F: silverman2023broken, resumo].
- **Aversão à perda**: na teoria do prospecto, o valor é atribuído a ganhos e perdas em relação a um **ponto de referência**, e a função de valor é "generally steeper for losses than for gains"; "losses loom larger than gains" [F: kahneman1979prospect, resumo e §3]. Tversky e Kahneman estendem a ideia à escolha sem risco: "losses and disadvantages have greater impact on preferences than gains and advantages" [F: tversky1991loss, resumo].
- **Recompensa variável** e **caixa de recompensa (loot box)**: a lei brasileira define caixa de recompensa como funcionalidade de jogos eletrônicos que permite adquirir, "mediante pagamento", itens virtuais "ou de vantagens aleatórias", "sem conhecimento prévio de seu conteúdo" [F: lei15211ecadigital, art. 2, IV].
- **Padrão manipulativo (dark pattern)**: a definição de trabalho da OCDE é "business practices employing elements of digital choice architecture [...] that subvert or impair consumer autonomy, decision-making or choice" [F: oecd2022dark, §2]. Em jogos, Zagal, Björk e Lewis definem **dark game design pattern** como padrão usado intencionalmente "to cause negative experiences for players that are against their best interests and happen without their consent" [F: zagal2013dark, §3].

O que não é: ofensiva e vidas não são, por si, padrões manipulativos; a classificação depende de implementação, público e consentimento [F: zagal2013dark, §3]. Também não são medida de aprendizagem.

## Problema que resolve

Do ponto de vista de quem projeta, essas mecânicas resolvem retenção: fazer a pessoa voltar e continuar. O problema que este documento trata é o inverso: quando a mecânica que aumenta o retorno o faz contra o interesse do usuário, e por que crianças são o caso mais sensível [I].

## Fundamentos e funcionamento

### Ofensivas: a evidência revisada por pares

Silverman e Barasch (Journal of Consumer Research) relatam sete estudos, um de campo com dados de um aplicativo de contagem de passos e seis experimentos com 400 a 600 adultos cada, recrutados on-line [F: silverman2023broken, "Study Overview"]. Resultado central: uma sequência intacta exibida no registro aumenta a chance de repetir o comportamento em relação a uma sequência quebrada, "independent of actual past behavior", porque manter a sequência vira "a meaningful goal in and of itself" [F: silverman2023broken, resumo].

No estudo 3 (N = 602, questões de idiomas num aplicativo simulado), 78,33% escolheram continuar o mesmo idioma com sequência intacta contra 53,31% com sequência quebrada (OR = 3,17) [F: silverman2023broken, Study 3]. O registro amplificou o efeito nas duas direções: com sequência intacta, 92,47% continuaram com registro visível contra 64,94% sem registro (OR = 6,63); com sequência quebrada, 45,21% contra 60,90% (OR = 0,53) [F: silverman2023broken, Study 3]. Ou seja, exibir a ofensiva **reduz** a persistência de quem a quebrou [I]. O efeito cresce quando a pessoa se atribui a quebra e diminui quando é possível "reparar" a sequência [F: silverman2023broken, resumo].

Limites: todos os participantes eram adultos; a variável dependente era a escolha seguinte, não aprendizagem nem bem-estar; e o estudo-piloto registrou que 59% dos participantes já tinham "gone out of their way" para manter uma sequência e 27% tinham feito algo fora do aplicativo para isso [F: silverman2023broken, pilot study]. As recomendações práticas do artigo são dirigidas a empresas que querem engajamento, incluindo vender reparo de ofensiva por moeda do jogo [F: silverman2023broken, "Practical Implications"]. Dados de retenção publicados por fornecedores de aplicativos não foram usados aqui; seriam evidência do próprio fornecedor, não independente [I].

### Aversão à perda como mecanismo

[I] A ofensiva cria um ponto de referência (a sequência atual); perder um dia é codificado como perda, que pesa mais que o ganho equivalente [F: kahneman1979prospect, §3]. Os próprios Silverman e Barasch citam a aversão à perda como mecanismo possível, ainda não testado, para a assimetria entre sequência intacta e quebrada [F: silverman2023broken, "Future Directions"]. "Vidas" que se esgotam e colheitas que murcham seguem a mesma lógica: Zagal et al. descrevem o **playing by appointment**, em que o recurso "withers and loses its value" se o jogador não volta no horário do jogo [F: zagal2013dark, §4.1.2].

### Recompensa variável e caixas de recompensa

Kahneman e Tversky observam que o sobrepeso de probabilidades baixas "may contribute to the attractiveness of both insurance and gambling" [F: kahneman1979prospect, resumo]. Em levantamento com 7.422 jogadores adultos, o gasto com loot boxes se associou à gravidade de jogo problemático (η² = 0,054) [F: zendle2018video, resumo]. Com 1.155 adolescentes de 16 a 18 anos, a associação foi maior (η² = 0,120), descrita como moderada a grande e mais forte que em adultos [F: zendle2019adolescents, resumo]. Ambos os estudos são correlacionais, com amostras autosselecionadas recrutadas em fóruns on-line, e não permitem saber a direção causal [F: zendle2018video, "Limitations"; zendle2019adolescents]. King e Delfabbro chamam de "predatory monetization" os sistemas de compra que ocultam o custo de longo prazo até que o jogador esteja "financially and psychologically committed" [F: king2018predatory].

### Taxonomias de padrões manipulativos

Gray et al. organizam os padrões em cinco estratégias (nagging, obstruction, sneaking, interface interference, forced action) e incluem "gamification" em forced action: partes do serviço que só podem ser "earned" por uso repetido [F: gray2018dark, "Results"]. A OCDE adota a mesma categoria em sua taxonomia consolidada [F: oecd2022dark, p. 53]. Mathur et al. encontraram 1.818 instâncias de 15 tipos em cerca de 11 mil sites de compras e mostram que muitos padrões exploram vieses como escassez e efeito de enquadramento [F: mathur2019dark, resumo e §3].

Zagal et al. propõem perguntas-guia, por exemplo "How likely is the player to regret having spent money" e se o jogador sente que precisa jogar "primarily because of a sense of social obligation" [F: zagal2013dark, §4.2 e §4.3]. A crítica de Deterding, Stenros e Montola sustenta que o conceito é incoerente (trata estados subjetivos como propriedade do objeto), não explicita a ética em que se apoia e reflete preconceito contra jogos casuais e freemium, mas reconhece valor nas perguntas sobre transparência e arrependimento [F: deterding2020against].

## Requisitos e pressupostos

Para crianças, os riscos acima deixam de ser escolha de projeto e passam a ser obrigação:

- No Brasil, o Estatuto Digital exige configurações "que evitem o uso compulsivo" desde a concepção e por padrão [F: lei15211ecadigital, art. 8, IV] e veda caixas de recompensa em jogos "direcionados a crianças e a adolescentes" [F: lei15211ecadigital, art. 20]; a análise jurídica completa está em `psg.legal.eca-and-digital-eca`.
- No Reino Unido, o código de design apropriado à idade aponta "reward loops, continuous scrolling, notifications and auto-play" como estratégias de engajamento ("sticky features"), pede que opções de continuar sejam apresentadas "without suggesting that children will lose out if they don't" e recomenda pausa "without losing their progress in a game" [F: ico2020aadc, padrão 5]; o padrão 13 recomenda empurrar a criança para comportamentos de bem-estar, "such as taking breaks" [F: ico2020aadc, padrão 13].
- A OCDE registra que padrões manipulativos podem prejudicar desproporcionalmente "less educated consumers or children" [F: oecd2022dark, sumário executivo].

## Vantagens e limitações

Ofensivas aumentam a repetição imediata em adultos [F: silverman2023broken]. Limitações: nenhuma evidência revisada por pares localizada de que ofensivas melhorem aprendizagem; efeito negativo documentado sobre quem quebra a sequência [F: silverman2023broken, Study 3]; e incentivo a manter a sequência por si, desligado do objetivo [I]. Para crianças com deficiência, faltas por terapia, saúde ou rotina familiar não são escolha; uma mecânica que pune ausência penaliza justamente quem tem menos controle sobre o próprio tempo [H].

## Alternativas e comparações

| Mecânica | Construto pretendido | Alternativa menos coercitiva |
|---|---|---|
| Ofensiva diária com perda | hábito, regularidade | contagem cumulativa ou meta semanal flexível, sem zerar [I] |
| Vidas que se esgotam | cuidado na resposta | erro barato com feedback, sem bloqueio [I] |
| Caixa de recompensa | surpresa, novidade | recompensa conhecida e não paga; vedada a menores no Brasil [F: lei15211ecadigital, art. 20] |
| Recurso que murcha | retorno | progresso que espera o jogador [F: zagal2013dark, §4.1.2] |

## Exemplo técnico independente de domínio

```
regularidade:
  mostrar: total_de_sessoes_no_mes          # cumulativo, nunca zera
  nunca: zerar contador por ausência; notificar quebra; vender reparo
notificacoes: desligadas por padrão para menores; nenhuma mensagem de perda
pausa: salvar estado a qualquer momento, sem penalidade
auditoria: listar toda mecânica cujo efeito dependa de perda, aleatoriedade paga
           ou horário imposto; justificar ou remover
```

## Relações com outros conceitos

Relaciona-se com `gam.mech.points-badges-leaderboards`, `gam.mech.core-loops-and-progression` e `gam.motiv.intrinsic-extrinsic-and-overjustification`; especificado por `psg.legal.eca-and-digital-eca`. O direito de escolher quando parar dialoga com `acs.part.self-determination`. Métricas de retenção não são indicadores de aprendizagem (`lae.ind.engagement-indicators`), e otimizar retenção com dados de pesquisa levanta a questão de `dat.ethics.research-vs-operation`. O estudo de caso de plataforma comercial está em `lms.case.duolingo`.

## Lacunas e questões abertas

- Não se localizou estudo revisado por pares sobre ofensivas com crianças, nem sobre ofensivas e aprendizagem.
- Tversky e Kahneman (1991) e King e Delfabbro (2018) só tiveram resumo ou metadados lidos.
- A metanálise de Deci, Koestner e Ryan, relevante para recompensas, fica em `gam.motiv.intrinsic-extrinsic-and-overjustification`.
- A hipótese sobre crianças com deficiência acima é [H] e precisa de estudo.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| silverman2023broken | academico | 2026-10-30 |
| kahneman1979prospect | academico | 2026-10-30 |
| tversky1991loss | academico [metadados] | 2026-10-30 |
| zagal2013dark | academico | 2026-10-30 |
| deterding2020against | academico (resumo estendido) | 2026-10-30 |
| gray2018dark | academico | 2026-10-30 |
| mathur2019dark | academico | 2026-10-30 |
| oecd2022dark | tecnico (OCDE) | 2026-10-30 |
| zendle2018video | academico | 2026-10-30 |
| zendle2019adolescents | academico | 2026-10-30 |
| king2018predatory | academico [metadados] | 2026-10-30 |
| ico2020aadc | normativo | 2026-10-30 |
| lei15211ecadigital | normativo | 2026-10-30 |
