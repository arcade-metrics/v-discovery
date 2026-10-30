---
id: gam.diff.challenge-and-zpd
titulo: Modelos de desafio, ZDP e a separação entre dificuldade do jogo e do conteúdo
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [wilson2019eighty, lomas2013optimizing, constant2019confidence, hunicke2004hamlet, zohaib2018dda, koidl2010dynamically, kickmeier2010micro, denisova2019deceptive]
relacoes:
  - { tipo: depende-de, alvo: ped.theory.sociocultural-and-zpd }
  - { tipo: complementa, alvo: gam.motiv.flow }
  - { tipo: complementa, alvo: gam.diff.dynamic-difficulty-adjustment }
  - { tipo: complementa, alvo: adp.adapt.sequencing-policies }
  - { tipo: complementa, alvo: adp.irt.elo-rating }
  - { tipo: depende-de, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: acs.adapt.accommodation-vs-modification }
  - { tipo: relacionado-a, alvo: dat.qual.granularity-and-constructs }
  - { tipo: relacionado-a, alvo: gam.instr.evidence-centered-design }
termos: [desafio ótimo, canal de flow, hipótese do U invertido, probabilidade de sucesso, regra dos 85%, região de aprendizagem proximal, dificuldade desejável, dificuldade objetiva, dificuldade percebida, dificuldade do jogo, dificuldade do conteúdo, micro-adaptatividade, macro-adaptatividade, modelo de jogador]
---

# Modelos de desafio, ZDP e a separação entre dificuldade do jogo e do conteúdo

## Definição e terminologia

Um modelo de desafio diz que nível de dificuldade uma atividade deve oferecer a cada pessoa e por quê. Três famílias aparecem na literatura de jogos e aprendizagem:

- **Canal de flow.** Desafio e habilidade devem crescer juntos para manter o jogador entre o tédio e a frustração; Hamlet foi desenhado para manter o jogador nesse canal [F: hunicke2004hamlet, Flow; zohaib2018dda, §1]. O construto de flow é tratado em `gam.motiv.flow`.
- **Hipótese do U invertido.** O engajamento máximo ocorreria em desafio moderado, decaindo para tarefas fáceis ou difíceis demais [F: lomas2013optimizing, introdução, citando Abuhamdeh e Csikszentmihalyi].
- **Dificuldade ótima para aprender.** A taxa de aprendizagem é máxima numa faixa de dificuldade, que Wilson et al. derivam formalmente para um caso restrito [F: wilson2019eighty, resumo]. Os mesmos autores ligam o resultado aos quadros da *Region of Proximal Learning*, que "builds on early work by Piaget and Vygotsky", e das *Desirable Difficulties* [F: wilson2019eighty, discussão].

A zona de desenvolvimento proximal (ZDP) de Vygotsky é um conceito pedagógico, com mediação e andaimes, documentado em `ped.theory.sociocultural-and-zpd`; aqui ela entra só como a ideia de que há uma faixa útil acima do que a pessoa já faz sozinha [I]. Taxa de acerto alvo não é a ZDP: a ZDP inclui o apoio de outro, e a taxa de acerto mede só o resultado da tarefa [I].

Dois pares de termos são necessários. **Dificuldade objetiva** é a probabilidade de falha estimada a partir dos resultados; **dificuldade percebida** é a estimativa que o próprio jogador faz [F: constant2019confidence, §4]. **Dificuldade do jogo** é a exigida pela mecânica (tempo, precisão, coordenação); **dificuldade do conteúdo** é a exigida pela habilidade que se quer ensinar ou medir [I]. Constant e Levieux, seguindo Levieux, distinguem dificuldades lógica, motora e sensorial [F: constant2019confidence, §1].

## Problema que resolve

Um sistema adaptativo precisa de um alvo (quanto desafio) e de um objeto (desafio de quê). Sem o primeiro, o ajuste não tem critério; sem o segundo, uma falha na mecânica é lida como falta de conhecimento e vice-versa [I].

## Fundamentos e funcionamento

### A regra dos 85% e seus limites

Para tarefas de classificação binária aprendidas por algoritmos de descida de gradiente estocástica, com ruído gaussiano, a taxa de erro de treino que maximiza a aprendizagem é cerca de 15,87%, isto é, acurácia em torno de 85%; treinar nessa dificuldade é exponencialmente mais rápido que treinar com dificuldade fixa [F: wilson2019eighty, resumo e introdução]. O resultado foi demonstrado em perceptron, rede de duas camadas com dígitos manuscritos e um modelo de aprendizagem perceptiva em macacos [F: wilson2019eighty, simulações]. Os limites são declarados pelos autores: com ruído laplaciano o ótimo cai para 82% e com ruído de Cauchy para 75%; treino em lote e tarefas com mais de duas categorias exigem extensão; um aprendiz bayesiano com memória perfeita não tem dificuldade ótima, porque a ordem dos exemplos não importa [F: wilson2019eighty, discussão]. Procedimentos de *staircase* em psicologia costumam mirar 80 a 85% de acerto [F: wilson2019eighty, discussão]. O artigo propõe que o modelo reproduz as regiões de flow, ansiedade e tédio, e deixa como questão aberta se medidas subjetivas de engajamento atingem o pico no ponto de aprendizagem máxima [F: wilson2019eighty, discussão]. Transpor o número para itens escolares de múltipla etapa, ou para crianças, é extrapolação [I].

### Engajamento ótimo não é aprendizagem ótima

Num jogo de estimativa na reta numérica, Lomas et al. manipularam tamanho do alvo, tipo de alvo, tempo-limite, conjunto de itens e sequenciamento em dois experimentos on-line (10.478 e 69.642 sessões anônimas, numa plataforma usada sobretudo por professores de 4º a 8º ano, com a sessão como unidade de sorteio) [F: lomas2013optimizing, experimentos 1 e 2]. No primeiro, alvos maiores elevaram o sucesso de 29% para 63% e produziram 34% mais tentativas e 18% mais tempo de jogo; o ajuste quadrático não foi significativo (p = 0,8) [F: lomas2013optimizing, resultados 1]. Em quase todos os casos, quanto mais fácil, mais tempo de jogo; e, num subconjunto de 1.392 jogadores, alvos maiores tiveram aprendizagem mais lenta (interação p = 0,02) [F: lomas2013optimizing, resumo e curvas de aprendizagem]. Os autores admitem que talvez o jogo não tenha ficado fácil o bastante para mostrar o lado direito do U, e que tempo de jogo pode não corresponder a diversão [F: lomas2013optimizing, discussão e limitações]. Para quem adapta, a consequência é que o alvo de engajamento e o alvo de aprendizagem podem divergir, e um sistema otimizado só para tempo de uso escolhe tarefas fáceis demais [I].

### Desafio objetivo e percebido divergem

Jogadores mantidos perto de 50% de sucesso superestimaram mais suas chances do que jogadores com dificuldade aleatória, nos jogos lógico e motor, mas não no sensorial [F: constant2019confidence, §5]. Lomas et al. levantam a hipótese de que dar ao jogador informação prévia sobre o desafio (*feedforward*) aumentaria a busca por desafio [F: lomas2013optimizing, discussão]. Dizer ao jogador que o jogo se adapta mudou a experiência e a pontuação [F: denisova2019deceptive, §6.2].

### Separar dificuldade do jogo e dificuldade do conteúdo

Lomas et al. já mostram as duas fontes de dificuldade no mesmo jogo: tamanho do alvo e tempo-limite são parâmetros de mecânica, conjunto de itens é conteúdo, e todos alteraram a taxa de sucesso [F: lomas2013optimizing, experimento 2]. A mesma taxa de sucesso pode, portanto, vir de mecânica fácil com conteúdo difícil ou o contrário [I].

O projeto de jogos educacionais adaptativos descrito por Koidl et al. anota cada situação de aprendizagem em três dimensões separadas: aprendizagem (habilidades exigidas e ensinadas), jogo (adequação a tipos de jogador, via modelo de jogador) e narrativa; o modelo de aluno e o modelo de jogador são atualizados pelas ações e a escolha da próxima cena pondera as três, com pesos que resolvem conflitos [F: koidl2010dynamically, §4]. Os autores distinguem micro-adaptatividade (intervenções locais, como dicas de um personagem, baseadas numa estrutura de pré-requisitos de habilidades) de macro-adaptatividade (sequência de situações e ritmo da história) [F: koidl2010dynamically, §3 a §5]. Kickmeier-Rust e Albert formulam a restrição de projeto: as medidas didáticas "must not compromise gaming experience, immersion and flow", e a micro-adaptatividade interpreta o comportamento do aprendiz de forma "non-invasive" [F: kickmeier2010micro, resumo]. A avaliação relatada por Koidl et al., com 71 alunos do ensino secundário, comparou pré e pós-teste sem grupo controle descrito [F: koidl2010dynamically, §6; I].

### Integração com o modelo de aluno

A estimativa de habilidade no conteúdo e a escolha do próximo item pertencem ao modelo de aluno e à política de sequenciamento (`adp.lm.learner-model`, `adp.adapt.sequencing-policies`); a seleção por taxa de sucesso alvo com Elo está em `adp.irt.elo-rating`. A proposta deste documento é tratar a dificuldade do jogo como faceta separada [I]:

- a política de conteúdo escolhe o item pelo modelo de aluno; o controlador de jogo ajusta só parâmetros de mecânica;
- toda observação registra os dois níveis, de jogo e de conteúdo (ver `dat.qual.granularity-and-constructs`);
- a atualização do modelo de aluno usa um modelo de resposta com as duas facetas, ou só as respostas obtidas com a mecânica num nível conhecido e fácil para aquela pessoa [I]. Precedente de método: Constant e Levieux estimam a dificuldade objetiva com o parâmetro de dificuldade e o tempo como efeitos fixos e um intercepto por jogador [F: constant2019confidence, §4].

Quando a mecânica não é o construto, ajustá-la funciona como acomodação; quando é, vira modificação (`acs.adapt.accommodation-vs-modification`) [I].

## Requisitos e pressupostos

- Construto declarado para cada atividade: o que é conteúdo e o que é mecânica [I].
- Parâmetros de jogo e de conteúdo que possam variar de forma independente [I].
- Alvo de sucesso escolhido conforme o objetivo (aprender, engajar, medir), não herdado de outro contexto [I].

## Vantagens e limitações

Separar as facetas protege a interpretação da evidência e permite acomodar barreiras motoras sem rebaixar a meta de aprendizagem [I]. Custa autoria (anotar cada situação em várias dimensões) e cria conflitos entre alvos, que Koidl et al. resolvem com pesos sem critério empírico relatado [F: koidl2010dynamically, §4; I].

## Alternativas e comparações

| Alvo de sucesso | Origem | Validade relatada |
|---|---|---|
| cerca de 85% | derivação para classificação binária [F: wilson2019eighty] | algoritmos de gradiente, ruído gaussiano |
| 80 a 85% | prática de *staircase* [F: wilson2019eighty, discussão] | psicofísica |
| 50% | DDA "canônico" em Constant e Levieux [F: constant2019confidence, §1] | gera superconfiança |
| 25 a 40%; cerca de 20% | Shapira; xadrez on-line, citados por Lomas et al. [F: lomas2013optimizing, discussão] | preferência e prazer relatados |
| quanto mais fácil, mais tempo de jogo | experimento on-line [F: lomas2013optimizing] | engajamento, não aprendizagem |

## Métricas e métodos de avaliação

Dificuldade objetiva por regressão logística de efeitos mistos e percebida por apostas [F: constant2019confidence, §4]; engajamento por duração voluntária e número de tentativas, combinados em log(tentativas x tempo) [F: lomas2013optimizing, experimento 1]; aprendizagem por curvas de erro ao longo das oportunidades de prática [F: lomas2013optimizing, curvas de aprendizagem]. Avaliar separação jogo/conteúdo exige variar as duas facetas de forma cruzada [I].

## Exemplo técnico independente de domínio

```
para cada rodada:
    item       = politica_conteudo.escolher(modelo_aluno, alvo_conteudo)
    parametros = controlador_jogo.ajustar(perfil_motor, alvo_jogo)
    resultado  = executar(item, parametros)
    registrar(item.dificuldade, parametros.nivel, resultado, tempo)
    se parametros.nivel <= nivel_seguro(perfil_motor):
        modelo_aluno.atualizar(item, resultado)        # evidência de conteúdo
    senão:
        modelo_aluno.atualizar_com_faceta(item, parametros.nivel, resultado)
    perfil_motor.atualizar(parametros.nivel, resultado)
```

Esquema proposto por este documento [I], a partir da separação de modelos de Koidl et al. [F: koidl2010dynamically, §4].

## Relações com outros conceitos

Depende da ZDP (`ped.theory.sociocultural-and-zpd`) e do modelo de aluno (`adp.lm.learner-model`); complementa flow (`gam.motiv.flow`), DDA (`gam.diff.dynamic-difficulty-adjustment`), sequenciamento (`adp.adapt.sequencing-policies`) e Elo (`adp.irt.elo-rating`); relaciona-se com acomodação x modificação, granularidade de construtos e evidence-centered design (`gam.instr.evidence-centered-design`).

## Lacunas e questões abertas

- Não foi encontrado nesta sessão estudo que cruze experimentalmente dificuldade de mecânica e de conteúdo e meça aprendizagem [I].
- A regra dos 85% não foi testada em crianças nem em tarefas escolares com mais de duas respostas [F: wilson2019eighty, discussão].
- O texto integral de Kickmeier-Rust e Albert não foi lido; a evidência empírica da micro-adaptatividade fica pendente [F: kickmeier2010micro, resumo].
- Que alvo de sucesso convém a estudantes com deficiência ou neurodivergentes (ver `gam.evid.special-education-and-neurodivergence`) [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| wilson2019eighty | academico | 2026-10-30 |
| lomas2013optimizing | academico | 2026-10-30 |
| constant2019confidence | academico | 2026-10-30 |
| hunicke2004hamlet | academico | 2026-10-30 |
| zohaib2018dda | academico | 2026-10-30 |
| koidl2010dynamically | academico | 2026-10-30 |
| kickmeier2010micro | academico (resumo) | 2026-10-30 |
| denisova2019deceptive | academico | 2026-10-30 |
