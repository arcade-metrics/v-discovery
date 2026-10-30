---
id: gam.instr.stealth-assessment
titulo: Stealth assessment
tipo: tecnica
dominio: gamificacao-e-jogos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [shute2011stealth, shute2013stealth, shute2013assessment, ventura2013validity, shute2016measuring, kim2016applying, rahimi2023stealth, mislevy2015psychometrics, mislevy2012design]
relacoes:
  - { tipo: depende-de, alvo: gam.instr.evidence-centered-design }
  - { tipo: complementa, alvo: gam.instr.telemetry-as-evidence }
  - { tipo: complementa, alvo: adp.lm.learner-model }
  - { tipo: avaliado-por, alvo: lae.psy.reliability-and-validity }
  - { tipo: complementa, alvo: gam.diff.dynamic-difficulty-adjustment }
  - { tipo: relacionado-a, alvo: gam.motiv.flow }
  - { tipo: relacionado-a, alvo: gam.motiv.feedback-design }
  - { tipo: relacionado-a, alvo: lae.asmt.formative-and-summative }
  - { tipo: relacionado-a, alvo: psg.consent.child-assent }
termos: [stealth assessment, avaliação embutida, game-based assessment, competency model, action model, indicador, rede bayesiana, validade convergente, validade de critério, medida de desempenho de persistência, troféu ouro e prata, worked example]
---

# Stealth assessment

## Definição e terminologia

Stealth assessment ("avaliação furtiva" ou "invisível") é avaliação "seamlessly woven directly into the fabric of the instructional environment", um processo em que dados de desempenho são coletados continuamente durante o jogo e inferências sobre competências são guardadas num modelo dinâmico do aprendiz [F: shute2011stealth, p. 504-505]. Shute e Ventura a definem como "ECD-based assessments that are woven directly and invisibly into the fabric of the gaming environment" [F: shute2013stealth, p. 31]. A autora usou o termo formalmente pela primeira vez em 2005, mas cita como precursor um ambiente de descoberta guiada de microeconomia dos anos 1980 que monitorava habilidades de investigação [F: shute2011stealth, p. 503-504].

Termo vizinho: *game-based assessment* (GBA), uso de atividades de jogo como tarefas para obter evidência de habilidades [F: kim2016applying, resumo]. Stealth assessment é uma forma de GBA que estende ECD a jogos [F: kim2016applying, Introduction]. O que não é: não é a pontuação nativa do jogo (vida, inventário, posição), que Shute contrasta com variáveis adicionais de competência [F: shute2011stealth, p. 508], nem um questionário inserido entre fases.

## Problema que resolve

Testes tradicionais interrompem a experiência; Shute afirma que avaliações típicas "are likely to disrupt flow in good games" [F: shute2011stealth, p. 508]. A proposta busca apoiar a aprendizagem, manter o flow (ver `gam.motiv.flow`) e reduzir a ansiedade de teste "while not sacrificing validity and reliability" [F: shute2011stealth, p. 505]. Os pressupostos declarados são quatro: aprender fazendo melhora a aprendizagem; atributos podem ser medidos durante o jogo; forças e fraquezas podem ser aproveitadas; e feedback formativo apoia o aluno [F: shute2011stealth, p. 506].

## Fundamentos e funcionamento

A técnica herda os modelos de ECD (`gam.instr.evidence-centered-design`): competency model, evidence model e action model; a sequência de ações é a fonte de evidência, e redes bayesianas acumulam a evidência nas variáveis de competência [F: shute2011stealth, p. 510-512]. Dois desafios de medida são apontados: as ações de um jogo são dependentes entre si, ao contrário de itens independentes, e uma ação não equivale a "one question=one fact" [F: shute2011stealth, p. 509].

Para cada competência define-se uma lista de indicadores observáveis no jogo. No jogo de física estudado por Shute e Ventura, a persistência tem como indicadores o tempo em problema não resolvido, o número de reinícios e o número de retornos a problemas não resolvidos [F: shute2013stealth, Fig. 5]. A regra que gera cada indicador é verificada contra codificação humana de replays; os autores declaram que classificações automáticas com menos de 80% de acurácia em relação à avaliação humana não seriam implementadas [F: shute2013stealth, p. 60].

Os dois exemplos do capítulo de 2011 (pensamento sistêmico num mundo 3D e resolução criativa de problemas num jogo comercial) são *worked examples*: um aluno hipotético e indicadores com valores atribuídos por dois especialistas, que concordaram bastante entre si [F: shute2011stealth, p. 514-517]. Não são estudos de validação [I].

## Requisitos e pressupostos

- Competência definida a partir de revisão de literatura e revisada por especialistas [F: shute2011stealth, p. 505].
- Alinhamento entre mecânica e competência; sem ele a rede não recebe evidência adequada [F: kim2016applying, Discussion].
- Volume de jogo suficiente: os autores do estudo com 47 alunos recomendam sessões mais longas e distribuídas para melhorar validade e confiabilidade [F: shute2016measuring, §5.1].
- Medidas externas alinhadas ao construto para validar [F: shute2016measuring, §5].

## Vantagens e limitações

Vantagens declaradas: medir competências difíceis de captar em testes (criatividade, persistência, resolução de problemas) e dar base para feedback e adaptação [F: shute2011stealth, p. 505, 509]. Limitações registradas pelas próprias fontes: granularidade do competency model difícil de acertar; evidência de jogo colaborativo difícil de atribuir a cada aluno [F: shute2011stealth, p. 518]; dados esparsos quando cada jogador escolhe fases diferentes, o que impediu calcular o alfa da medida de persistência [F: ventura2013validity, Results]; generalização limitada, pois desempenho em um contexto diz pouco de outro [F: mislevy2015psychometrics, §5.2].

Tensão ética [I]: a avaliação é "invisível" por desenho, mas os mesmos autores defendem que a saída seja transparente, "players should be aware of how they are doing relative to important competencies" [F: shute2013stealth, p. 31]. Com crianças, a invisibilidade da coleta precisa ser conciliada com consentimento e assentimento (ver `psg.consent.child-assent`).

## Métricas e métodos de avaliação

Os estudos publicados validam principalmente por correlação com medidas externas e por predição de pós-teste. Uma revisão sistemática em andamento identificou 93 estudos de stealth assessment; dos 60 já codificados, 42 eram de validação, 4 usavam as estimativas para adaptação ou feedback e 14 só descreviam o projeto; 24 usavam validade convergente, 18 outros métodos (predição de pós-teste, acurácia de classificação) e os demais não especificavam validação [F: rahimi2023stealth]. A técnica, portanto, foi mais validada do que usada para adaptar [I].

| Estudo | Construto e jogo | Amostra | Resultado de validade |
|---|---|---|---|
| Shute, Ventura e Kim 2013 | física qualitativa, jogo de física 2D | 167 alunos de 8º e 9º ano, cerca de 4 h em 1,5 semana | ganho pré-pós significativo, t(154) = 2,12, p < 0,05; troféus de ouro por agente correlacionados com o pré-teste; teste externo com alfa 0,72 e 0,73 [F: shute2013assessment, Results] |
| Kim, Almond e Shute 2016 (mesmo jogo) | física, rede bayesiana | dados de campo do mesmo projeto | correlação da estimativa da rede com o pós-teste em torno de 0,1 com priors de especialistas e de 0,36 após calibração [F: kim2016applying, Step 8] |
| Ventura e Shute 2013 | persistência, tempo em fases difíceis | 154 alunos de 8º e 9º ano | r = 0,51 com medida externa de persistência nos 70 de baixo desempenho e r = 0,22 nos 84 de alto; r parcial = 0,26 com o pós-teste nos de baixo desempenho; sem relação com autorrelato [F: ventura2013validity, Tab. 2, Tab. 3] |
| Shute et al. 2016 | resolução de problemas, jogo comercial modificado em tablet | 47 alunos de 7º ano com dados completos, cerca de 3 h | r = 0,40 com matrizes de Raven e r = 0,41 com MicroDYN; alfa 0,76 entre facetas; faceta de planejamento com r = 0,98 com o escore geral [F: shute2016measuring, Results] |

Os tamanhos de amostra são pequenos e as populações são de escolas norte-americanas; nenhum estudo acima inclui alunos com deficiência como grupo analisado [I].

## Alternativas e comparações

| Opção | Interrupção do jogo | Evidência de validade | Custo |
|---|---|---|---|
| Stealth assessment | nenhuma por desenho | correlacional, amostras pequenas [F: rahimi2023stealth] | alto: modelo, regras, calibração [F: kim2016applying] |
| Testes pré e pós fora do jogo | total, fora da sessão | instrumentos estabelecidos | baixo, mas sem processo [I] |
| Perguntas embutidas entre fases | parcial | itens convencionais | médio [I] |
| Pontuação nativa do jogo | nenhuma | sem argumento de evidência [F: mislevy2012design, p. 32] | baixo [I] |

## Exemplo técnico independente de domínio

```
competencia: persistencia
indicadores (por fase, do log):
  t_nao_resolvida = soma(duracao) onde fase.resultado == "nao_resolvida"
  reinicios       = contagem(evento == "reiniciar") onde fase nao resolvida
regra_de_aceite: acuracia(indicador_auto vs codificacao_humana_replay) >= 0.80
acumulacao: rede_bayesiana.atualizar(no="persistencia", evidencia=categorizar(indicadores))
validacao: corr(estimativa, medida_externa_de_persistencia); corr_parcial(estimativa, pos_teste | pre_teste)
```

## Relações com outros conceitos

Depende de `gam.instr.evidence-centered-design`; a escolha e validação de cada indicador está em `gam.instr.telemetry-as-evidence`. A estimativa alimenta um `adp.lm.learner-model` e pode orientar `gam.diff.dynamic-difficulty-adjustment` e feedback (`gam.motiv.feedback-design`). O uso formativo ou somativo segue `lae.asmt.formative-and-summative`; os critérios de validade, `lae.psy.reliability-and-validity`.

## Lacunas e questões abertas

- O estudo de 2016 tem 47 alunos; os autores anunciam validação maior que não foi localizada nesta pesquisa.
- A revisão sistemática de 2023 é um resumo de duas páginas de estudo em andamento; não há versão completa consultada.
- A fonte que valida a medida de persistência por tempo não controla velocidade motora nem familiaridade com a interface.
- Falta evidência de stealth assessment com estudantes com deficiência ou neurodivergentes (ver `gam.evid.special-education-and-neurodivergence`).
- O efeito da avaliação invisível sobre o comportamento quando o aluno descobre que é avaliado não foi estudado nas fontes lidas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| shute2011stealth | academico (cópia da autora) | 2026-10-30 |
| shute2013stealth | academico (livro aberto) | 2026-10-30 |
| shute2013assessment | academico (cópia da autora) | 2026-10-30 |
| ventura2013validity | academico (cópia dos autores) | 2026-10-30 |
| shute2016measuring | academico (cópia da autora) | 2026-10-30 |
| kim2016applying | academico (cópia da autora) | 2026-10-30 |
| rahimi2023stealth | academico (resumo estendido) | 2026-10-30 |
| mislevy2015psychometrics | academico | 2026-10-30 |
| mislevy2012design | academico | 2026-10-30 |
