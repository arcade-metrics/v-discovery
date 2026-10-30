---
id: gam.fund.comparison
titulo: Gamificação x jogo sério x aprendizagem baseada em jogos x simulação
tipo: comparacao
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [deterding2014game, seaborn2015gamification, landers2014developing, plass2015foundations, sailer2020gamification, clark2016digital, hamari2014does, koivisto2019rise, vlachopoulos2017effect, djaouti2011classifying]
relacoes:
  - { tipo: complementa, alvo: gam.fund.gamification }
  - { tipo: complementa, alvo: gam.fund.serious-games-and-gbl }
  - { tipo: avaliado-por, alvo: gam.evid.meta-analyses }
  - { tipo: avaliado-por, alvo: gam.evid.study-designs-and-quality }
  - { tipo: relacionado-a, alvo: gam.mech.mda-and-design-frameworks }
  - { tipo: relacionado-a, alvo: adp.eval.educational-effectiveness }
termos: [gamificação, jogo sério, aprendizagem baseada em jogos, simulação, playful learning, integração do conteúdo à mecânica, comparação de mídia, comparação de valor agregado]
---

# Gamificação x jogo sério x aprendizagem baseada em jogos x simulação

## Definição e terminologia

Os quatro termos não são do mesmo tipo, e boa parte da confusão vem de compará-los como se fossem [I]:

- **Gamificação**: uso de elementos de design de jogo em contexto não lúdico, sem produzir um jogo completo [F: deterding2014game, §4]. É uma técnica de design aplicada a uma atividade que já existe [F: sailer2020gamification, p. 78].
- **Jogo sério**: um artefato, um jogo completo com finalidade principal não recreativa [F: deterding2014game, §4.2; djaouti2011classifying, resumo].
- **Aprendizagem baseada em jogos (GBL)**: uma abordagem pedagógica, jogo com resultados de aprendizagem definidos [F: plass2015foundations, p. 259]. Usa jogos sérios, mas também jogos comerciais ou não digitais.
- **Simulação**: modelo dinâmico de um sistema real que pretende fidelidade e validade; difere do jogo pela ausência necessária de conflito, regras artificiais e metas predeterminadas [F: vlachopoulos2017effect, p. 4, citando Sauvé et al. 2007]. Pode ser usada com ou sem camada de jogo (jogo de simulação).

Plass et al. acrescentam **playful learning** como categoria que contém as anteriores: ambiente de aprendizagem com um ou mais elementos de jogo, seja ou não um jogo [F: plass2015foundations, p. 278].

## Problema que resolve

Escolher entre as abordagens exige saber o que cada uma pretende afetar e quanto custa. A literatura usa os termos de forma inconsistente: em educação, "gamificação" já foi usada para designar GBL e jogos sérios [F: seaborn2015gamification, §3.2], e as revisões de jogos e simulações apontam "terminological ambiguity" [F: vlachopoulos2017effect, p. 3]. Sem a distinção, resultados de uma abordagem são atribuídos a outra [I].

## Alternativas e comparações

| Critério | Gamificação | Jogo sério | GBL (abordagem) | Simulação |
|---|---|---|---|---|
| Natureza | Processo de design sobre atividade existente [F: sailer2020gamification, p. 78] | Artefato: jogo completo [F: deterding2014game, §4.3] | Uso pedagógico de jogos [F: plass2015foundations, p. 259] | Modelo de sistema real [F: vlachopoulos2017effect, p. 4] |
| O que pretende afetar | Comportamentos e atitudes ligados à aprendizagem, que por sua vez moderam ou medeiam o resultado [F: landers2014developing, resumo]; mudança de comportamento é o objetivo mais declarado [F: seaborn2015gamification, §5.1] | A aprendizagem diretamente, pela manipulação de atributos do jogo, sem esse mediador comportamental [F: landers2014developing, resumo] | Engajamento cognitivo, afetivo, comportamental e sociocultural com o conteúdo [F: plass2015foundations, p. 262] | Aplicação de conhecimento e habilidades a problemas realistas [F: vlachopoulos2017effect, p. 4] |
| Integração do conteúdo à mecânica | Baixa: o conteúdo e a tarefa ficam; acrescentam-se pontos, insígnias, placares [F: plass2015foundations, p. 259] | Alta quando a mecânica central é a habilidade-alvo (learning mechanic) [F: plass2015foundations, p. 268] | Depende do jogo escolhido e da mediação [I] | O conteúdo é o próprio modelo; a "mecânica" é manipular o sistema [I] |
| Exige instrução eficaz à parte | Sim: a gamificação não substitui a instrução [F: sailer2020gamification, p. 78] | Não necessariamente: o jogo pode ser a instrução [I] | Em geral sim (mediação, debriefing) [H] | Frequentemente sim [H] |
| Custo de produção | Baixo a moderado [I] | Alto: projetar jogo e conteúdo juntos, equilibrando conteúdo e jogabilidade [F: plass2015foundations, p. 259] (custo em si: [I]) | Variável: baixo se reusa jogo existente, alto se produz [I] | Alto quando exige fidelidade [I] |
| Evidência típica | Revisões com resultados mistos, estudos curtos e pequenos [F: hamari2014does, §5.1; koivisto2019rise, resumo]; metanálise em aprendizagem com g pequeno a moderado [F: sailer2020gamification, resumo] | Metanálises de comparação de mídia e de valor agregado [F: clark2016digital, resumo] | A mesma de jogos sérios, mais estudos de mediação do professor [I] | Frequentemente agrupada com jogos nas revisões, o que dificulta separar o efeito [F: vlachopoulos2017effect, p. 2] |
| Risco característico | Dependência de recompensa extrínseca; efeito de novidade [F: seaborn2015gamification, §5.2.1, §5.2.2] | Mecânica desalinhada do objetivo [F: plass2015foundations, p. 268] | Pressupor motivação sem medir aprendizagem [F: plass2015foundations, p. 276] | Fidelidade sem estrutura de aprendizagem [H] |

### Números de referência (detalhes em `gam.evid.meta-analyses`)

- Gamificação da aprendizagem, estudos de 2013 a 2017 (escola, ensino superior, formação profissional): cognitivos g = 0,49 (IC 95% 0,30 a 0,69; k = 19; N = 1686); motivacionais g = 0,36 (IC 0,18 a 0,54; k = 16; N = 2246); comportamentais g = 0,25 (IC 0,04 a 0,46; k = 9; N = 951). Só o efeito cognitivo foi estável no subconjunto de alto rigor [F: sailer2020gamification, resumo].
- Jogos digitais x condições sem jogo, estudantes de 6 a 25 anos (K-16): g = 0,33 (IC 0,19 a 0,48; 57 estudos, 209 tamanhos de efeito). Versões ampliadas x versões padrão do mesmo jogo: g = 0,34 (IC 0,17 a 0,51; 20 estudos) [F: clark2016digital, resumo].
- No mesmo conjunto de jogos, designs rudimentares ("the mere addition of points and/or badges to schoollike tasks") tiveram média de 0,53 e designs mais elaborados, 0,25, mas a diferença não foi significativa (p = 0,07) e os autores pedem que não seja lida como vantagem [F: clark2016digital, Resultados].

Os números não são diretamente comparáveis entre as linhas: populações, comparadores, critérios de inclusão (Clark et al. excluíram simulações não chamadas de jogo) e períodos diferem [F: clark2016digital, Método] [I].

## Vantagens e limitações

A comparação por critério ajuda a escolher, mas as categorias se sobrepõem. Deterding et al. e Seaborn e Fels reconhecem que separar um sistema gamificado de um jogo é subjetivo e depende da percepção de quem joga [F: seaborn2015gamification, §3.2, §5.1]. Plass et al. vão além: mesmo a distinção entre jogo e ambiente não lúdico "is very difficult to achieve on an abstract, generalizable level" [F: plass2015foundations, p. 262].

## Métricas e métodos de avaliação

Duas famílias de desenho, que respondem a perguntas diferentes [F: clark2016digital, resumo]:
- **Comparação de mídia**: jogo (ou camada gamificada) contra instrução sem jogo. Responde "vale usar?".
- **Comparação de valor agregado**: duas versões do mesmo jogo que diferem num elemento. Responde "qual elemento funciona?".

Para gamificação, Hamari et al. pedem que se meçam as três camadas (affordance, resultado psicológico, resultado comportamental) num mesmo modelo, o que nenhum dos 24 estudos fez [F: hamari2014does, §5.1]. O comparador importa: Sailer e Homner incluíram o tipo de instrução do grupo de comparação como moderador [F: sailer2020gamification, p. 82]. Ver `gam.evid.study-designs-and-quality` e `adp.eval.educational-effectiveness`.

## Exemplo técnico independente de domínio

```
dado objetivo O, conteúdo C, prazo P, orçamento B:
  se C já tem atividades eficazes e o problema é adesão:
      gamificação; medir comportamento E aprendizagem; testar retirada da camada
  senão se O é uma habilidade que pode ser a ação central de um jogo:
      jogo sério com mecânica alinhada a O; avaliar por valor agregado
  senão se O exige praticar num sistema realista:
      simulação (com ou sem camada de jogo)
  registrar sempre: comparador, população, duração, instrumento
```

A árvore acima é recomendação deste documento [I], não de uma fonte.

## Relações com outros conceitos

Complementa `gam.fund.gamification` e `gam.fund.serious-games-and-gbl`, que aprofundam cada coluna. Os números vêm de `gam.evid.meta-analyses`; a qualidade dos desenhos, de `gam.evid.study-designs-and-quality`; o alinhamento mecânica-objetivo, de `gam.mech.mda-and-design-frameworks`. A noção geral de eficácia educacional está em `adp.eval.educational-effectiveness`.

## Lacunas e questões abertas

- Custo de produção não tem fonte empírica nesta área; todas as células de custo são [I].
- Não há metanálise lida que compare diretamente gamificação e jogo sério para o mesmo conteúdo e população.
- A fronteira simulação x jogo foi documentada por revisão secundária; Sauvé et al. (2007) e Aldrich (2009) não foram abertos.
- Nenhuma das fontes examinou a comparação em educação especial; ver `gam.evid.special-education-and-neurodivergence`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| deterding2014game | academico | 2026-10-30 |
| seaborn2015gamification | academico | 2026-10-30 |
| landers2014developing | academico (resumo) | 2026-10-30 |
| plass2015foundations | academico | 2026-10-30 |
| sailer2020gamification | academico | 2026-10-30 |
| clark2016digital | academico | 2026-10-30 |
| hamari2014does | academico | 2026-10-30 |
| koivisto2019rise | academico (resumo) | 2026-10-30 |
| vlachopoulos2017effect | academico | 2026-10-30 |
| djaouti2011classifying | academico (resumo) | 2026-10-30 |
