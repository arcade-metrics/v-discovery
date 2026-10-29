---
id: lae.matriz
titulo: Matriz comparativa de tradições e métodos do domínio
tipo: comparacao
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Matriz comparativa de tradições e métodos do domínio

Três comparações centrais do domínio: as duas tradições de análise (LA x EDM), as duas tradições de medição de desempenho (CTT x IRT, esta última aprofundada em `aprendizagem-adaptativa`) e as duas famílias de desenho para avaliar se uma intervenção funciona (experimental x quase-experimental).

## Learning Analytics vs. Educational Data Mining

| Critério | Learning Analytics (LA) | Educational Data Mining (EDM) |
|---|---|---|
| Comunidade/venue de origem | SoLAR, conferência LAK desde 2011 (lae.found.la-vs-edm) | International Educational Data Mining Society, conferência EDM (lae.found.la-vs-edm) |
| Ênfase declarada | humano no loop, intervenção institucional e pedagógica, sentido dado pelo analista | descoberta automatizada de padrão, métodos (relationship mining, structure discovery, prediction models) (lae.found.la-vs-edm) |
| Unidade de análise típica | aluno, curso, instituição (multinível) (lae.found.analytics-cycle) | conjunto de dados de interação, muitas vezes agregado entre instituições (lae.found.la-vs-edm) |
| Saída típica | dashboard, relatório, alerta para ação humana (lae.ind.dashboards-and-olm) | modelo preditivo, padrão descoberto, estrutura latente (lae.found.la-vs-edm) |
| Fronteira na prática | sobreposição ampla; muitos estudos se identificam com as duas tradições [I] | idem [I] |

## Teoria clássica dos testes (CTT) vs. Teoria de Resposta ao Item (IRT)

A IRT é aprofundada em `adp.irt.item-response-theory`; aqui a comparação cobre apenas os pontos citados por ambos os lados.

| Critério | CTT | IRT |
|---|---|---|
| O que estima | escore observado = escore verdadeiro + erro, por teste (lae.psy.classical-test-theory) | traço latente de habilidade do respondente, independente do item específico (adp.irt.item-response-theory) |
| Estatísticas de item | índice de dificuldade (p-value) e discriminação (correlação item-total), dependentes da amostra (lae.psy.classical-test-theory) | parâmetros de dificuldade/discriminação/acerto ao acaso, em tese invariantes à amostra (adp.irt.item-response-theory) |
| Dependência de amostra/teste | alta — estatísticas mudam com a amostra e com o teste usado (lae.psy.classical-test-theory) | baixa, sob os pressupostos do modelo (unidimensionalidade, independência local) (adp.irt.item-response-theory) |
| Exigências de dados/calibração | baixas, aplicável a qualquer teste pequeno (lae.psy.classical-test-theory) | banco de itens calibrado, amostra maior para estimar parâmetros (adp.irt.item-response-theory) |
| Uso típico | avaliações de sala de aula, instrumentos de baixo custo de implantação (lae.psy.classical-test-theory) | testes padronizados, testes adaptativos computadorizados (CAT) (adp.irt.item-response-theory) |
| Por que a CTT persiste apesar das limitações | simplicidade de cálculo e interpretação, custo de implantação menor (Hambleton & Jones 1993) (lae.psy.classical-test-theory) | — |

## Desenho experimental vs. quase-experimental para avaliar resultado educacional

| Critério | RCT (experimental) | Quase-experimental |
|---|---|---|
| Atribuição ao tratamento | aleatória (lae.evalm.experimental-design) | não aleatória — por critério de corte, por grupo pré-existente, ou pré-pós com comparação (lae.evalm.experimental-design) |
| Validade interna | mais forte, menos ameaças de confundimento por desenho (lae.evalm.experimental-design) | depende do desenho específico; mais vulnerável a confundimento não observado (lae.evalm.experimental-design) |
| Exemplos citados | A/B testing em produto educacional como RCT em miniatura (Kohavi, Tang & Xu 2020) (lae.evalm.experimental-design) | regressão descontínua (Thistlethwaite & Campbell 1960), diferenças em diferenças (Card & Krueger 1994) (lae.evalm.experimental-design) |
| Quando se justifica | quando randomização é viável e aceitável eticamente/operacionalmente [I] | quando randomizar não é viável, mas há um critério de corte ou grupo de comparação plausível [I] |
| Cuidado adicional em plataforma digital | unidade de randomização (aluno vs. turma), contaminação entre grupos, SUTVA (lae.evalm.experimental-design) | mesmas ameaças de validade interna listadas em Shadish, Cook & Campbell 2002, sem o controle que a randomização dá (lae.evalm.experimental-design) |

Em qualquer um dos dois desenhos, o resultado só é interpretável com tamanho de efeito reportado ao lado da significância estatística, e com a ressalva de que um único estudo — mesmo um RCT bem desenhado — raramente é suficiente diante da taxa de não replicação observada em ciências sociais (lae.evalm.effect-size-and-replication).
