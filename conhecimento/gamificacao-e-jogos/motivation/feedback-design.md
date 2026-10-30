---
id: gam.motiv.feedback-design
titulo: Projeto de feedback em atividades lúdicas
tipo: conceito
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [shute2008focus, hattietimperley2007feedback, kluger1996effects, wisniewski2020power, deci1999metaanalytic, wouters2013instructional, clearinghouse2018wouters, mayer2016role]
relacoes:
  - { tipo: complementa, alvo: gam.motiv.self-determination-theory }
  - { tipo: complementa, alvo: gam.motiv.intrinsic-extrinsic-and-overjustification }
  - { tipo: complementa, alvo: gam.motiv.flow }
  - { tipo: relacionado-a, alvo: gam.mech.points-badges-leaderboards }
  - { tipo: relacionado-a, alvo: gam.instr.stealth-assessment }
  - { tipo: relacionado-a, alvo: lae.asmt.formative-and-summative }
  - { tipo: relacionado-a, alvo: ped.id.cognitive-load-theory }
  - { tipo: relacionado-a, alvo: ped.synth.effect-size-in-education }
  - { tipo: relacionado-a, alvo: acs.dim.cognitive-accessibility }
termos: [feedback formativo, verificação, elaboração, feedback corretivo, feedback de alta informação, feedback imediato, feedback atrasado, feedback de velocidade, feedback no nível da tarefa, feedback no nível do processo, feedback no nível da autorregulação, feedback no nível do self, elogio, feedback normativo, feedback autorreferenciado, Feedback Intervention Theory, FIT]
---

# Projeto de feedback em atividades lúdicas

## Definição e terminologia

Shute define feedback formativo como "information communicated to the learner that is intended to modify his or her thinking or behavior to improve learning" [F: shute2008focus, p. 153]. Hattie e Timperley o tratam como informação dada por um agente sobre aspectos do desempenho ou da compreensão e organizam-no em três perguntas (para onde vou, como estou indo, qual o próximo passo) e quatro níveis: tarefa, processo, autorregulação e self [F: hattietimperley2007feedback, p. 81-90]. Neste documento, feedback é a informação que a atividade devolve sobre a resposta; pontos e insígnias são recompensas, tratadas em `gam.motiv.intrinsic-extrinsic-and-overjustification`, embora na prática uma mesma mensagem possa ser as duas coisas [I].

## Problema que resolve

Em jogos, feedback é constante (sons, pontos, animações) e barato de produzir. A pergunta de projeto não é se dar feedback, mas qual tipo, quando e sobre o quê, porque uma parte grande das intervenções de feedback piora o desempenho [F: kluger1996effects, resumo].

## Fundamentos e funcionamento

### Tipo: verificação x elaboração

Verificação é o julgamento simples de certo ou errado; elaboração é a parte informativa que dá pistas para chegar à resposta correta [F: shute2008focus, p. 158]. A elaboração pode tratar do tema, da resposta, do erro específico, dar exemplos resolvidos ou orientação geral; Shute relata consenso crescente de que elaboração específica à resposta melhora o desempenho, sobretudo a eficiência, mais do que verificação simples ou "responda até acertar" [F: shute2008focus, p. 158-159]. A metanálise de Wisniewski, Zierer e Hattie confirma o gradiente: reforço ou punição, d = 0,24 (k = 39; IC 0,06 a 0,43); feedback corretivo, d = 0,46 (k = 238; IC 0,39 a 0,55); feedback de alta informação, d = 0,99 (k = 42; IC 0,82 a 1,15) [F: wisniewski2020power, Tabela 3].

### Tempo: imediato x atrasado

Os resultados sobre tempo são inconsistentes [F: shute2008focus, p. 165]. Hattie e Timperley atribuem parte da inconsistência ao nível: na metanálise de Kulik e Kulik (53 estudos), algum atraso foi benéfico em situação de teste (0,36) e o feedback imediato foi benéfico durante atividades em sala (0,28); num estudo de Clariana et al., o feedback atrasado teve efeito de −0,06 em itens fáceis, 0,35 em médios e 1,17 em difíceis [F: hattietimperley2007feedback, p. 98]. Shute resume que o atrasado pode favorecer a transferência e o imediato a eficiência em habilidades procedimentais, e registra a recomendação de Mason e Bruning: imediato para alunos de baixo desempenho, atrasado para os de alto desempenho em tarefas complexas [F: shute2008focus, p. 165-166, 179]. Para tarefa difícil em relação à capacidade do aluno, Shute recomenda feedback imediato, ao menos no início [F: shute2008focus, p. 179].

### Foco: tarefa x pessoa

A Feedback Intervention Theory propõe que o feedback desloca a atenção entre três níveis (aprendizagem da tarefa, motivação para a tarefa e metatarefas, incluindo o self) e que sua eficácia "decreases as attention moves up the hierarchy closer to the self and away from the task" [F: kluger1996effects, resumo]. Nas análises de moderadores após exclusões, o efeito médio foi d = 0,38 em 470 efeitos, dos quais 32% negativos; feedback com elogio teve d = 0,09 contra 0,34 sem elogio; feedback desencorajador, −0,14 contra 0,33; com a solução correta, 0,43 contra 0,25; sobre a velocidade de melhora, 0,55 contra 0,28; por computador, 0,41 contra 0,23 [F: kluger1996effects, p. 273, Tabela 2]. Hattie e Timperley concluem que o elogio dirigido à pessoa tem pouca informação e desvia a atenção da tarefa, e distinguem esse elogio do que se refere a esforço, autorregulação e processo [F: hattietimperley2007feedback, p. 96]. Shute recomenda usar elogio "sparingly, if at all" e não interromper quem está imerso na tarefa [F: shute2008focus, p. 178], e, para alunos de baixo desempenho, feedback autorreferenciado (o próprio progresso) em vez de normativo (comparação com outros) [F: shute2008focus, p. 167].

### Feedback como evento motivacional

Feedback positivo verbal aumentou a motivação intrínseca no conjunto dos estudos (d = 0,33 em livre escolha) [F: deci1999metaanalytic, resumo], mas não em crianças, e, quando dado de modo controlador, reduz a motivação (ver `gam.motiv.intrinsic-extrinsic-and-overjustification`) [F: deci1999metaanalytic, p. 657]. No conjunto da metanálise de 2020, o efeito do feedback foi maior sobre resultados cognitivos (d = 0,51; k = 597) que sobre resultados motivacionais (d = 0,33; k = 109) [F: wisniewski2020power, Tabela 3].

## Requisitos e pressupostos

- Uma meta clara contra a qual o feedback compara o desempenho [F: hattietimperley2007feedback, p. 87-89].
- Saber qual habilidade a atividade treina, para que a elaboração trate do erro relevante [I].
- Para elaboração automática, um modelo de erros ou de respostas esperadas; sem ele, o sistema só verifica [I].

## Vantagens e limitações

O feedback está entre as intervenções educacionais de maior efeito médio: d = 0,48 (IC 0,44 a 0,51) em 435 estudos, 994 efeitos e mais de 61.000 participantes, após excluir 35 valores extremos [F: wisniewski2020power, resumo e §Outlier Analysis]. As limitações estão na variância:

- **Efeitos negativos.** Na metanálise de Kluger e DeNisi (607 efeitos, 23.663 observações), o efeito médio foi d = 0,41, mas mais de um terço das intervenções diminuiu o desempenho [F: kluger1996effects, resumo]. Em Wisniewski et al., 17% dos efeitos foram negativos (antes da exclusão de extremos) [F: wisniewski2020power, §General Impact of Feedback].
- **Heterogeneidade e viés.** I² = 86,47% e assimetria no funil, produzida só pelos artigos de periódico [F: wisniewski2020power, §Bias and Heterogeneity].
- **Tarefas.** Feedback em tarefas físicas teve d = −0,11, e no quartil de maior complexidade, 0,03 [F: kluger1996effects, p. 273, Tabela 2].
- **População.** Kluger e DeNisi incluem estudos de várias áreas e idades; as recomendações de Shute vêm sobretudo de estudos com estudantes; nenhuma das fontes isola crianças pequenas [I].

## Alternativas e comparações

| Decisão | Opção com melhor evidência | Condição ou ressalva |
|---|---|---|
| Tipo | Elaboração específica ao erro | d = 0,99 alta informação x 0,46 corretivo [F: wisniewski2020power, Tabela 3] |
| Tempo | Imediato em tarefa nova ou difícil | Atrasado pode favorecer transferência [F: shute2008focus, p. 179] |
| Foco | Tarefa e processo | Elogio à pessoa: d = 0,09 [F: kluger1996effects, p. 273] |
| Referência | Progresso próprio | Evitar normativo para baixo desempenho [F: shute2008focus, p. 167] |
| Canal | Computador | d = 0,41 x 0,23 [F: kluger1996effects, p. 273] |

### Evidência em jogos

Uma metanálise de suporte instrucional em aprendizagem baseada em jogos (29 estudos, 107 comparações; 907 escolares em 28 comparações e 2.768 universitários ou adultos) encontrou efeito geral d = 0,34, maior para habilidades de transferência (d = 0,62) que para conhecimento (0,33) e desempenho no jogo (0,19), sem diferença significativa entre faixas etárias; o feedback foi definido como informação sobre a correção da resposta [F: clearinghouse2018wouters, p. 2-3; wouters2013instructional, metadados]. Mayer conclui, a partir de pesquisa de valor agregado, que acrescentar conselhos ou explicações ao jogo está entre os recursos mais promissores [F: mayer2016role, resumo].

## Métricas e métodos de avaliação

Comparar versões que diferem só no feedback (valor agregado), com medida de aprendizagem fora do jogo, retenção tardia e medida de motivação de livre escolha [F: mayer2016role, resumo; deci1999metaanalytic, p. 646]. Relatar a proporção de efeitos negativos, não só a média [I]. Tamanhos de efeito: ver `ped.synth.effect-size-in-education`.

## Exemplo técnico independente de domínio

```
ao_responder(item, resposta, aluno):
    correto = verificar(item, resposta)
    se aluno.em_sequencia_fluida e correto: sinal_discreto(); retornar   # não interromper
    msg = verificacao(correto)
    se não correto:
        erro = classificar_erro(item, resposta)          # requer modelo de erros
        msg += dica_especifica(erro) se aluno.tentativas < 2 senão solucao_comentada(item)
    msg += progresso_proprio(aluno, habilidade(item))   # autorreferenciado, sem ranking
    proibido: mensagens sobre a pessoa ("você é inteligente"), comparação com colegas
    tempo = imediato se item.dificuldade_relativa(aluno) alta senão resumo_ao_fim_da_fase
```

## Relações com outros conceitos

Complementa `gam.motiv.self-determination-theory` (feedback informativo x controlador), `gam.motiv.intrinsic-extrinsic-and-overjustification` (elogio como recompensa verbal) e `gam.motiv.flow` (feedback claro como precondição). Relaciona-se com `gam.mech.points-badges-leaderboards` (placares são feedback normativo), `gam.instr.stealth-assessment` e `lae.asmt.formative-and-summative`. A carga de mensagens extensas remete a `ped.id.cognitive-load-theory` e a `acs.dim.cognitive-accessibility`.

## Lacunas e questões abertas

- Nenhuma fonte lida isola efeitos de feedback com crianças de 4 a 10 anos ou com deficiência intelectual.
- A metanálise de Wouters e van Oostendorp não foi lida na íntegra; o tamanho de efeito do feedback isolado não foi verificado.
- Não se encontrou evidência sobre feedback sonoro e visual contínuo típico de jogos (efeitos de "juice") sobre aprendizagem.
- A tabela de Hattie e Timperley com efeitos por tipo saiu desalinhada na extração; seus números não foram usados.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| shute2008focus | academico | 2026-10-30 |
| hattietimperley2007feedback | academico | 2026-10-30 |
| kluger1996effects | academico | 2026-10-30 |
| wisniewski2020power | academico | 2026-10-30 |
| deci1999metaanalytic | academico | 2026-10-30 |
| wouters2013instructional | academico [metadados] | 2026-10-30 |
| clearinghouse2018wouters | secundario | 2026-10-30 |
| mayer2016role | academico (resumo) | 2026-10-30 |
