---
id: lae.ind.dashboards-and-olm
titulo: Dashboards de learning analytics e sua relação com o open learner model
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [schwendimann2017dashboards, jivet2018license, jivet2017awareness, bennett2018dashboardliteracy, pozdniakov2024vizliteracy, bullkay2016smili]
relacoes:
  - { tipo: relacionado-a, alvo: lae.found.analytics-cycle }
  - { tipo: complementa, alvo: adp.lm.open-learner-model }
  - { tipo: depende-de, alvo: lae.ind.engagement-indicators }
  - { tipo: relacionado-a, alvo: lae.ind.dropout-and-risk-prediction }
termos: [learning analytics dashboard, LAD, data literacy, dashboard literacy, visualization literacy, open learner model, awareness, comparação social, sense-making]
---

# Dashboards de learning analytics e sua relação com o open learner model

## Definição e terminologia

Um *learning analytics dashboard* (LAD) é uma interface gráfica que apresenta dados sobre o processo ou o comportamento de aprendizagem de um ou mais alunos — por exemplo, frequência, uso de biblioteca, desempenho — de forma resumida e visual, para apoiar algum tipo de sense-making (dar sentido aos dados) por parte de quem o consulta [F: schwendimann2017dashboards, descrição do escopo da revisão]. Schwendimann et al., em revisão sistemática de literatura sobre o tema, definem o campo de pesquisa de dashboards como voltado a identificar que dados são significativos para diferentes interessados (stakeholders) e como esses dados podem ser apresentados para apoiar processos de sense-making [F: schwendimann2017dashboards].

Este documento trata exclusivamente da perspectiva de visualização e apresentação de indicadores agregados de aprendizagem a diferentes públicos. A modelagem cognitiva do aluno que por vezes alimenta esse tipo de interface — isto é, a representação interna de conhecimento, habilidade ou progresso de um aluno construída por um sistema — é tratada em profundidade em `adp.lm.open-learner-model`, que já cobre o framework SMILI de Bull e Kay para *open learner models* (OLM). A relação entre os dois conceitos é discutida na seção de relações abaixo; aqui não se repete a descrição do framework SMILI nem dos modos de apresentação e manutenção de um OLM.

## Problema que resolve

Dashboards de LA nasceram, em larga medida, com foco institucional — por exemplo, identificar alunos em risco ou dar a gestores uma visão agregada de turmas e cursos —, ao passo que um OLM tende a ter como consumidor primário o próprio aprendiz, com propósito declarado de apoiar metacognição e confiança [F: bullkay2016smili, conforme já documentado em `adp.lm.open-learner-model`]. Um dashboard resolve o problema de tornar dados de uso e desempenho, que de outra forma ficariam dispersos em logs e planilhas, visíveis e acionáveis para quem precisa decidir algo a partir deles — seja o próprio aluno ajustando seu estudo, seja o professor decidindo onde intervir, seja o gestor acompanhando indicadores de um programa.

## Fundamentos e funcionamento

### Para quem o dashboard é feito, e como isso muda o design

A pergunta "para quem" molda decisões de design que vão além da escolha de gráfico. Jivet et al., em revisão sistemática sobre dashboards voltados a aprendizes, constatam que muito poucas avaliações de dashboard levam em conta os conceitos educacionais que fundamentaram teoricamente seu desenho — ou seja, boa parte dos dashboards de aprendiz é avaliada sem checar se o desenho de fato se apoiou em alguma teoria de aprendizagem, e não apenas na disponibilidade técnica do dado [F: jivet2018license].

Um achado recorrente dessa linha de pesquisa diz respeito ao recurso de comparação entre pares: em revisão anterior dos mesmos autores sobre dashboards voltados a aprendizes, o desenho corrente tende a incentivar competição entre colegas em vez de orientar o aluno para o domínio do conteúdo, o que produz referências de comparação enganosas (o aluno se situa "acima" ou "abaixo" da média da turma, sem que isso diga algo sobre o que ainda precisa aprender) [F: jivet2017awareness, resumo consolidado por fonte secundária]. A mesma linha de trabalho relata que a maioria dos desenhos de dashboard torna o aluno consciente (*aware*) de seu processo de aprendizagem, mas não necessariamente converte essa consciência em mudança de comportamento, cognição ou emoção — ou seja, *awareness* não é suficiente por si só, e os autores recomendam que outros instrumentos pedagógicos complementem o dashboard, integrados ao desenho instrucional, em vez de o dashboard operar isolado [F: jivet2017awareness, resumo consolidado por fonte secundária].

Para gestores e formuladores de política, por outro lado, a literatura de learning analytics em geral (ver `adp.lm.open-learner-model`, que documenta essa mudança em relação ao OLM) aponta expansão do público de dashboards institucionais para incluir também pesquisadores educacionais e gestores escolares, à medida que os campos de Learning Analytics, Learning at Scale e Educational Data Mining amadureceram [F: bullkay2016smili, via `adp.lm.open-learner-model`]. Esse público tende a consumir indicadores agregados por turma, curso ou coorte, não o detalhe por aluno que um OLM ou um dashboard de aprendiz expõe.

### Estado da pesquisa sobre dashboards: um campo ainda jovem

Schwendimann et al. buscaram sistematicamente em cinco bases acadêmicas principais e no Google Scholar, obtendo 346 artigos candidatos, dos quais 55 foram incluídos na análise final da revisão [F: schwendimann2017dashboards]. A conclusão central da revisão é que o campo ainda é jovem: a maioria dos estudos é exploratória ou de prova de conceito, faltando pesquisa longitudinal em contextos autênticos e comparação sistemática entre diferentes desenhos de dashboard [F: schwendimann2017dashboards].

### Literacia de dados necessária para interpretar um dashboard

Um dashboard tecnicamente correto não garante interpretação correta por quem o consulta. Duas linhas de evidência, de públicos diferentes, sustentam esse ponto:

- **Do lado do aluno**, Bennett e Folley (2018) propõem o conceito de *dashboard literacy*, descrevendo-o como uma prática de literacia — mais próxima de uma questão de identidade e reflexão do que de uma habilidade puramente técnica — e não apenas competência técnica de leitura de gráfico. O conceito tem três componentes, derivados dos pilares de *feedback literacy* de Sutton (2012): *knowing* (saber), *becoming* (tornar-se) e *acting* (agir) [F: bennett2018dashboardliteracy]. No estudo, com 24 alunos de último ano de graduação em uma universidade do Reino Unido, os autores relatam que a resposta ao dashboard é altamente individual, dependente da disposição e orientação de aprendizagem de cada aluno, e recomendam cautela no uso, dado o potencial efeito do dashboard sobre o bem-estar do estudante [F: bennett2018dashboardliteracy].
- **Do lado do professor**, Pozdniakov et al. (2024) investigam como a *literacia de visualização* (capacidade de ler e interpretar corretamente um gráfico ou representação visual de dados) afeta a interpretação de dashboards por professores, inclusive quando o dashboard inclui recursos de orientação visual (destaque de cor, anotações — por vezes chamados de "data storytelling"). Professores com baixa literacia de visualização produziram interpretações mais rasas do dashboard do que professores com alta literacia; por outro lado, literacia de visualização não se associou de forma significativa à taxa de conclusão correta da tarefa, e a orientação visual adicional não ajudou os professores a aprofundar suas interpretações — embora algum nível de orientação tenha ajudado na conclusão correta de tarefas, orientação excessiva pôde ser prejudicial [F: pozdniakov2024vizliteracy].

Em conjunto, essas duas linhas de evidência indicam que a literacia necessária para interpretar um dashboard corretamente não é genérica: envolve tanto uma dimensão técnica (ler o gráfico) quanto uma dimensão reflexiva/identitária (o que fazer com o que se vê), e essa segunda dimensão é pouco endereçada pelo desenho técnico do dashboard em si [I].

## Requisitos e pressupostos

- Para que um dashboard apoie sense-making, pressupõe-se algum nível mínimo de literacia de dados ou de visualização no público consultado; a pesquisa revisada aqui indica que esse pressuposto frequentemente não se verifica sem suporte adicional (andaime pedagógico, orientação) [F: pozdniakov2024vizliteracy].
- Pressupõe-se que o indicador exibido tenha validade de medição — por exemplo, se o dashboard expõe "engajamento", pressupõe-se que o indicador subjacente de fato capture o que esse rótulo promete (ver `lae.ind.engagement-indicators` para as limitações dessa correspondência).
- Para dashboards com comparação entre pares, pressupõe-se que a comparação social funcione como motivador e não como desincentivo; a literatura revisada mostra que esse pressuposto não se sustenta de forma uniforme — comparação não foi percebida positivamente por todos os aprendizes [F: jivet2018license].

## Vantagens e limitações

Vantagens: trace data resumida em visualização permite ao usuário perceber, em um único relance, padrões que não seriam visíveis em dados brutos — daí o título da revisão de Schwendimann et al., "Perceiving Learning at a Glance" [F: schwendimann2017dashboards].

Limitações:

- **Campo pouco maduro**: predominância de estudos exploratórios e de prova de conceito, sem comparação sistemática entre desenhos nem estudos longitudinais em uso real e sustentado [F: schwendimann2017dashboards].
- **Fraca fundamentação teórica**: a maioria das avaliações de dashboard para aprendizes não verifica se o desenho se baseou em alguma teoria de aprendizagem reconhecida [F: jivet2018license].
- **Comparação social com efeito ambíguo**: o recurso mais comum (comparar o aluno à média da turma) tende a reforçar competição em vez de orientar para domínio do conteúdo, e nem todo aprendiz reage bem a ele [F: jivet2017awareness, resumo consolidado; jivet2018license].
- **Awareness sem mudança de comportamento**: tornar o aluno ciente de seus dados não implica, por si só, mudança de comportamento, cognição ou emoção — a lacuna entre mostrar o dado e gerar ação é um achado central dessa linha de pesquisa [F: jivet2017awareness, resumo consolidado].
- **Literacia desigual do público**: tanto estudos com alunos quanto com professores mostram que a interpretação do mesmo dashboard varia por literacia prévia (de dados, de visualização) e por disposição individual, o que significa que o mesmo painel pode informar bem um usuário e confundir ou mesmo prejudicar o bem-estar de outro [F: bennett2018dashboardliteracy; pozdniakov2024vizliteracy].

## Alternativas e comparações

| Aspecto | Dashboard institucional (gestor) | Dashboard de professor | Dashboard/OLM do aprendiz |
|---|---|---|---|
| Unidade de análise típica | turma, curso, coorte, programa | turma, aluno individual dentro da turma | o próprio aluno |
| Propósito declarado mais comum | monitorar indicadores agregados, identificar risco em escala | decidir onde intervir pedagogicamente | metacognição, autorregulação, confiança no sistema |
| Literacia exigida do público | leitura de indicador agregado, frequentemente já familiar a relatórios institucionais | literacia de visualização (achados de Pozdniakov et al. mostram variação relevante) | literacia de dashboard no sentido de Bennett e Folley (saber, tornar-se, agir) |
| Risco documentado nesta pesquisa | fora do escopo direto das fontes revisadas aqui | orientação visual em excesso pode prejudicar interpretação [F: pozdniakov2024vizliteracy] | efeito sobre bem-estar do aluno, resposta muito individual [F: bennett2018dashboardliteracy] |

Comparado a um OLM (ver `adp.lm.open-learner-model`), um dashboard de learning analytics tende a expor indicadores agregados de uso e desempenho (frequência, notas, comparação com a turma), enquanto um OLM expõe uma representação do estado de conhecimento do próprio aprendiz construída por um modelo de aluno subjacente; a linha entre os dois nem sempre é nítida na prática — um mesmo produto pode combinar elementos dos dois —, mas a distinção conceitual de propósito (institucional/agregado vs. metacognitivo/individual) é útil para orientar decisões de design [F: bullkay2016smili, via `adp.lm.open-learner-model`].

## Métricas e métodos de avaliação

A pesquisa revisada aqui não aponta um conjunto único e consolidado de métricas de avaliação de dashboard; os métodos mais citados são estudo de caso e protótipo avaliados por usabilidade ou percepção do usuário, sem replicação sistemática entre estudos [F: schwendimann2017dashboards]. Jivet et al. propõem avaliar dashboards também pelo critério de fundamentação teórica (quais conceitos de aprendizagem embasaram o desenho), não apenas por métricas de uso ou satisfação [F: jivet2018license]. Pozdniakov et al. usam análise de rede epistêmica (epistemic network analysis) sobre protocolos de verbalização (*think-aloud*) para comparar a profundidade de interpretação entre professores de diferentes níveis de literacia de visualização [F: pozdniakov2024vizliteracy].

## Exemplo técnico independente de domínio

Esboço de decisão de design que incorpora as dimensões discutidas acima, independente de plataforma:

```
definir_dashboard(publico, proposito):
    dados = selecionar_indicadores(publico, proposito)
        # gestor: agregados por coorte/curso
        # professor: por turma, com destaque para casos que exigem decisão
        # aluno: individual, com ou sem comparação com pares

    se publico == aluno e incluir_comparacao_com_pares:
        avaliar_risco(motivacao_por_competicao vs. desmotivacao)  # efeito documentado como ambíguo

    forma = escolher_visualizacao(literacia_estimada(publico))
        # literacia baixa -> preferir formas simples, evitar sobrecarga de anotação

    andaime = adicionar_apoio_interpretativo(publico)
        # obrigatório se literacia_estimada(publico) for baixa;
        # cuidado: orientacao em excesso pode ser contraproducente (achado empirico)

    avaliar(dashboard, fundamentacao_teorica_explicita=True)
        # nao avaliar so por uso/satisfacao; registrar qual teoria de aprendizagem
        # (se houver) embasou cada elemento do desenho
```

## Relações com outros conceitos

Relaciona-se com `lae.found.analytics-cycle` como a etapa de apresentação/ação do ciclo de learning analytics. Depende de `lae.ind.engagement-indicators` e, por extensão, de qualquer indicador que alimente o painel — a validade do dashboard não pode exceder a validade do indicador que ele exibe. Relaciona-se com `lae.ind.dropout-and-risk-prediction` como uma possível superfície de exposição de um escore de risco a professores ou orientadores. Complementa `adp.lm.open-learner-model`: este documento trata da perspectiva de visualização de indicadores agregados de uso e desempenho, enquanto `adp.lm.open-learner-model` trata em profundidade da abertura de um modelo cognitivo de aluno (o framework SMILI, formas de apresentação e de manutenção do modelo, propósitos de abertura); quem precisar da discussão sobre modelo de aluno aberto deve consultar aquele documento, não este.

## Lacunas e questões abertas

- Schwendimann et al. (2017) foi consultado apenas por resumo e metadados nesta sessão — o artigo está atrás de paywall da IEEE e nenhuma cópia de acesso aberto do texto completo foi localizada. A categorização detalhada de tipos de dashboard e a definição formal que os autores propõem (mencionadas no resumo, mas não detalhadas aqui) ficam como lacuna a preencher com leitura do texto completo.
- Jivet et al. (2017, "Awareness is Not Enough") e Jivet et al. (2018, "License to evaluate") também foram consultados apenas por resumo e descrições de terceiros nesta sessão; tentativas de acessar os PDFs de acesso aberto hospedados em core.ac.uk e no repositório da Universidade Aberta dos Países Baixos foram bloqueadas por proteção anti-automação (Cloudflare) durante a pesquisa. As citações usadas aqui são, portanto, de segunda mão quanto à formulação exata dos autores, embora a substância (crítica à comparação social, distinção entre awareness e mudança de comportamento, falta de fundamentação teórica em avaliações) seja consistente entre múltiplas fontes secundárias independentes.
- Não foi localizada, nesta pesquisa, uma revisão equivalente à de Bennett e Folley ou Pozdniakov et al. voltada especificamente a gestores/formuladores de política como público de dashboard; a literatura revisada aqui concentra-se em aluno e professor, deixando a perspectiva de gestor como lacuna de cobertura deste documento.
- A relação prática entre "dashboard de LA" e "OLM" — se e quando um produto deveria ser classificado como um ou outro, ou como híbrido — não tem, nas fontes revisadas, um critério operacional consolidado; a distinção proposta na seção de alternativas e comparações é uma síntese deste documento, não um resultado extraído diretamente de uma única fonte [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| schwendimann2017dashboards | academico (apenas resumo e metadados) | 2026-10-29 |
| jivet2018license | academico (apenas resumo e metadados) | 2026-10-29 |
| jivet2017awareness | academico (apenas resumo e metadados) | 2026-10-29 |
| bennett2018dashboardliteracy | academico (resumo consultado via página do editor) | 2026-10-29 |
| pozdniakov2024vizliteracy | academico (resumo consultado via página do editor) | 2026-10-29 |
| bullkay2016smili | academico (reuso de fonte já verificada em `adp.lm.open-learner-model`) | 2026-10-29 |
