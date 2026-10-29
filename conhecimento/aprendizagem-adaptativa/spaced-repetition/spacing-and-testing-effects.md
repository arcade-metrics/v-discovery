---
id: adp.sr.spacing-and-testing-effects
titulo: Efeitos de espaçamento e de teste
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [cepeda2006distributed, cepeda2008spacing, roediger2006test, rowland2014testing, bjork2023difficulties]
relacoes:
  - { tipo: complementa, alvo: adp.sr.memory-and-forgetting }
  - { tipo: implementado-por, alvo: adp.sr.classical-algorithms }
  - { tipo: implementado-por, alvo: adp.sr.fsrs }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
  - { tipo: relacionado-a, alvo: adp.id.kli-framework }
termos: [spacing effect, lag effect, distributed practice, testing effect, retrieval practice, desirable difficulties, interstudy interval, retention interval]
---

# Efeitos de espaçamento e de teste

## Definição e terminologia

O *efeito de espaçamento* (spacing effect) é o ganho de retenção quando apresentações do mesmo material são separadas no tempo (spaced) em vez de consecutivas (massed); o *efeito de lag* compara níveis diferentes de espaçamento entre si; *distributed practice* é o termo genérico para ambos [F: cepeda2006distributed]. O *interstudy interval* (ISI) é o intervalo entre episódios de estudo do mesmo material; o *retention interval* (RI) é o intervalo entre o último estudo e o teste final [F: cepeda2006distributed].

O *efeito de teste* (testing effect, retrieval practice) é o ganho de retenção quando o aluno tenta recuperar o material da memória, em comparação com reestudá-lo pelo mesmo tempo [F: roediger2006test] [F: rowland2014testing]. *Desirable difficulties* é o rótulo cunhado por R. Bjork para condições de prática — espaçamento, intercalação (interleaving), variação contextual e prática de recuperação — que dificultam o desempenho durante o estudo mas frequentemente melhoram a retenção de longo prazo [F: bjork2023difficulties].

O que não é: espaçamento não é simplesmente "mais tempo de estudo" — os experimentos equiparam o tempo total e variam só a distribuição [F: cepeda2006distributed]; e o efeito de teste não é artefato de reexposição, pois aparece mesmo sem feedback, quando o teste só reexpõe o que o aluno consegue recordar [F: roediger2006test].

## Problema que resolve

São os dois efeitos empíricos mais robustos que um sequenciador de prática pode explorar: *quando* reapresentar um item (espaçamento) e *em que formato* (recuperação ativa em vez de reexposição). Dão a justificativa empírica dos algoritmos de repetição espaçada (`adp.sr.classical-algorithms`) e restrições concretas para políticas de sequenciamento (`adp.adapt.sequencing-policies`) [I].

## Fundamentos e funcionamento

### Efeito de espaçamento: magnitude

A meta-análise de Cepeda, Pashler, Vul, Wixted e Rohrer cobriu 839 avaliações de prática distribuída em 317 experimentos de 184 artigos, restritos a tarefas de memória verbal [F: cepeda2006distributed]. Na comparação direta massed × spaced (271 comparações), a prática espaçada produziu 47,3% de acerto no teste final contra 36,7% da prática massificada, t(540) = 6,6, p < .001; apenas 12 das 271 comparações mostraram efeito nulo ou negativo [F: cepeda2006distributed]. Mesmo com RI menor que 1 minuto, o espaçamento melhorou o desempenho final em 9 pontos percentuais [F: cepeda2006distributed].

### O gap ótimo depende do intervalo de retenção

O efeito de lag é não monotônico: para cada RI existe um ISI que maximiza a retenção, e aumentos além dele reduzem o desempenho; o ISI ótimo cresce com o RI — com RI abaixo de 1 minuto, ISIs abaixo de 1 minuto maximizam a retenção; com RI de 6 meses ou mais, ISIs de pelo menos 1 mês [F: cepeda2006distributed].

O estudo experimental de Cepeda, Vul, Rohrer, Wixted e Pashler quantificou essa superfície ("temporal ridgeline") com mais de 1.350 participantes aprendendo fatos, gaps de até 105 dias e teste final após RIs de 7, 35, 70 e 350 dias [F: cepeda2008spacing]. Resultados: com tempo total de estudo fixo, o gap ótimo deu ganho de 64% em recordação final sobre gap zero (d = 1,1) e 26% em reconhecimento (d = 1,5); por RI, os ganhos em recordação no gap ótimo versus gap zero foram de 10%, 59%, 111% e 77% [F: cepeda2008spacing]. Os gaps ótimos interpolados foram de aproximadamente 3, 8, 12 e 27 dias — ou seja, 43%, 23%, 17% e 8% dos RIs: o gap ótimo cresce em valor absoluto, mas *encolhe como proporção* do RI, de 20-40% de um RI de 1 semana para 5-10% de um RI de 1 ano [F: cepeda2008spacing]. Os autores ajustaram aos dados a forma `recall = A(bt + 1)^(-R)`, em que a taxa de esquecimento R cai com o gap — espaçar torna a curva de esquecimento mais rasa [F: cepeda2008spacing].

### Efeito de teste

No Experimento 1 de Roediger e Karpicke (textos em prosa, recordação livre, sem feedback), reestudar venceu no teste de 5 minutos (81% × 75% das unidades de ideia), mas o padrão inverteu nos testes atrasados: 68% × 54% a favor do teste após 2 dias (d = 0,95) e 56% × 42% após 1 semana (d = 0,83) [F: roediger2006test]. No Experimento 2, após 1 semana, estudar uma vez e testar três (STTT) superou estudar três e testar uma (SSST) e estudar quatro vezes (SSSS): 61% × 56% × 40% — embora SSSS vencesse aos 5 minutos (83% × 78% × 71%); o esquecimento proporcional entre 5 minutos e 1 semana foi de 52% (SSSS), 28% (SSST) e 14% (STTT) [F: roediger2006test].

A meta-análise de Rowland (159 tamanhos de efeito de 61 estudos) estimou o efeito médio de testar versus reestudar em g = 0,50, IC 95% [0,42, 0,58] [F: rowland2014testing]. Moderadores: efeito maior com feedback (g = 0,73) do que sem (g = 0,39); maior com teste inicial de recordação com pistas (g = 0,61) do que recordação livre (g = 0,29) ou reconhecimento (g = 0,29); maior com RI de pelo menos 1 dia (g = 0,69) do que abaixo de 1 dia (g = 0,41); e, sem feedback, sucesso inicial de recuperação de até 50% não produziu efeito confiável (g = 0,03), contra g = 0,56 com sucesso acima de 75% [F: rowland2014testing].

### Por que dificuldades seriam desejáveis

A explicação teórica dos Bjork (ver `adp.sr.memory-and-forgetting`): manipulações como espaçamento e variação *reduzem* a retrieval strength no momento da prática, e ganhos de storage strength são maiores justamente quando a retrieval strength está baixa; além disso, o ato de recuperar é um evento mais potente que o de reestudar [F: bjork2023difficulties]. Isso é proposta teórica que organiza os achados empíricos acima, não um achado independente [H]. Consequência metacognitiva documentada pelos autores: massificar e blocar fazem o desempenho imediato subir rápido e *parecem* melhores, induzindo alunos e professores a julgamentos errados sobre a própria aprendizagem [F: bjork2023difficulties] — coerente com os 5 minutos de Roediger e Karpicke, em que a condição pior a longo prazo vencia [F: roediger2006test].

## Requisitos e pressupostos

- A base empírica é dominada por material verbal (pares associados, listas, fatos, prosa) e laboratório; a meta-análise de Cepeda restringiu-se a tarefas verbais [F: cepeda2006distributed]. Generalização a habilidades complexas é pressuposto a validar [I].
- Para colher o efeito de teste sem feedback é preciso sucesso de recuperação razoável; com taxas de acerto baixas, feedback torna-se necessário [F: rowland2014testing].
- Explorar o gap ótimo exige saber (ou decidir) o intervalo de retenção alvo — quando o aluno precisará do conhecimento —, que raramente é dado em sistemas reais [I].

## Vantagens e limitações

São efeitos grandes, baratos e robustos: nenhuma mudança de conteúdo, só de agenda e formato [I]; magnitudes documentadas acima [F: cepeda2006distributed] [F: cepeda2008spacing] [F: rowland2014testing]. Limitações: o custo é desempenho imediato pior e sensação subjetiva de dificuldade, com risco de abandono ou de rejeição por alunos e professores [F: bjork2023difficulties]; o ISI ótimo não é uma proporção fixa do RI, então regras de bolso simples erram nas pontas [F: cepeda2008spacing]; e ISIs longos demais reduzem retenção (efeito não monotônico) [F: cepeda2006distributed].

## Alternativas e comparações

| Manipulação | Desempenho imediato | Retenção a prazo | Evidência |
|---|---|---|---|
| Prática massificada / blocada | melhor | pior | 36,7% × 47,3% final [F: cepeda2006distributed]; 83% × 71% aos 5 min [F: roediger2006test] |
| Prática espaçada (gap ótimo) | pior no estudo | +64% recordação vs. gap zero, d = 1,1 | [F: cepeda2008spacing] |
| Reestudo | melhor aos 5 min | pior a 2 dias e 1 semana | [F: roediger2006test] |
| Teste / retrieval practice | pior aos 5 min | g = 0,50 geral; g = 0,73 com feedback | [F: rowland2014testing] |
| Intervalos expansivos vs. fixos | — | em geral iguais ou levemente favoráveis ao expansivo, com contraexemplos | [F: cepeda2006distributed] |

Sobre a última linha: Cepeda et al. concluem que intervalos expansivos "either benefit learning or produce effects similar to studying with fixed spacing", registrando estudos com prejuízo e com benefício, sem diferença sistemática óbvia entre eles [F: cepeda2006distributed] — relevante porque os algoritmos clássicos de repetição espaçada assumem expansão (ver `adp.sr.classical-algorithms`).

## Métricas e métodos de avaliação

Diferença de acurácia no teste final e tamanhos de efeito (Cohen's d, Hedges g) são as medidas padrão [F: cepeda2006distributed] [F: rowland2014testing]. O delineamento mínimo tem dois episódios de estudo separados por ISI e teste final após RI, com tempo total de estudo equiparado [F: cepeda2006distributed]. Para sistemas adaptativos, o equivalente é avaliação prospectiva com RI explícito, não apenas acurácia de próxima resposta (`adp.eval.evaluation-protocols`, `adp.eval.educational-effectiveness`) [I].

## Exemplo técnico independente de domínio

Heurística de agenda derivada diretamente dos achados, para um planejador que conhece o intervalo de retenção alvo; os percentuais vêm de [F: cepeda2008spacing], a interpolação entre eles é interpretação [I]:

```
agendar_revisao(item, ri_alvo):             # ri_alvo: dias até o uso previsto
    # gap ótimo como fração do RI encolhe quando o RI cresce
    se ri_alvo <= 7:    fracao = 0.3        # ~20-40% para RI de 1 semana
    senão se ri_alvo <= 70: fracao = 0.2    # ~17-23% para RI de 1-2 meses
    senão:              fracao = 0.08       # ~5-10% para RI de ~1 ano
    gap = max(1, fracao * ri_alvo)
    retornar agora + gap

formato_da_revisao(item):
    # recuperação ativa com feedback > recuperação sem feedback > reexposição
    se p_estimada_de_acerto(item) muito baixa:
        retornar reapresentar_e_testar      # garante sucesso + feedback
    senão:
        retornar testar_com_feedback
```

## Relações com outros conceitos

Complementa `adp.sr.memory-and-forgetting`, que descreve os modelos de memória que explicam estes efeitos. É a base empírica implementada por `adp.sr.classical-algorithms` e `adp.sr.fsrs`, e restringe o espaço de políticas em `adp.adapt.sequencing-policies` (a melhor sequência local raramente é a melhor para retenção a prazo). A distinção desempenho imediato × aprendizagem duradoura conecta-se à separação entre desempenho e aprendizagem no framework KLI (`adp.id.kli-framework`).

## Lacunas e questões abertas

- Adesope et al. 2017 (meta-análise mais recente do efeito de teste) não foi consultada nesta sessão; Rowland 2014 cobre o essencial, mas uma atualização da estimativa fica pendente.
- A cópia aberta de Rowland 2014 usada é a versão online-first hospedada em curso da EPFL; a paginação final (1432-1463) vem dos metadados do DOI.
- Como combinar gap ótimo (que exige RI alvo) com sistemas em que o RI é desconhecido ou indefinido ("saber para sempre") é questão de projeto em aberto; os algoritmos de `adp.sr.classical-algorithms` respondem fixando uma retenção alvo em vez de um RI [I].
- Evidência de espaçamento e teste em habilidades procedimentais complexas e em populações heterogêneas (`adp.eval.heterogeneous-populations`) é mais rala que em memória verbal [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| cepeda2006distributed | academico | 2026-10-29 |
| cepeda2008spacing | academico | 2026-10-29 |
| roediger2006test | academico | 2026-10-29 |
| rowland2014testing | academico | 2026-10-29 |
| bjork2023difficulties | academico | 2026-10-29 |
