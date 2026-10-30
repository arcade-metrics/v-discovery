---
id: dat.ds.assistments
titulo: Datasets públicos do ASSISTments
tipo: estudo-de-caso
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [heffernan2014assistments, assistments2026skillbuilder0910, assistments2026interpret, assistments2026data2012, assistments2026data2015, assistments2017competition, assistments2026terms, xiong2016going, liu2022pykt, choi2020ednet, gervet2020when, abdelrahman2023ktsurvey, koedinger2010datashop]
relacoes:
  - { tipo: parte-de, alvo: dat.ds.comparison }
  - { tipo: complementa, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: complementa, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.kt.comparison }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
  - { tipo: relacionado-a, alvo: dat.qual.loss-and-deduplication }
  - { tipo: relacionado-a, alvo: dat.rd.data-documentation }
  - { tipo: relacionado-a, alvo: dat.ethics.research-vs-operation }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
termos: [ASSISTments, skill builder, problema original, scaffolding, ms_first_response, first_response_time, overlap_time, opportunity, detector de afeto, duplicação de registros]
---

# Datasets públicos do ASSISTments

## Definição e terminologia

**ASSISTments** é uma plataforma de tutoria e avaliação hospedada pelo Worcester Polytechnic Institute (WPI), nos Estados Unidos; o nome junta "assistance" (tutoria) e "assessment" (relato ao professor) [F: heffernan2014assistments, Abstract]. Professores montam conjuntos de problemas com respostas, dicas, soluções e vídeos, ou usam conteúdo pronto; o aluno recebe correção imediata [F: heffernan2014assistments, Abstract]. Os **datasets ASSISTments** são extrações públicas desses logs, disponibilizadas por ano letivo, e são o conjunto de referência mais usado em knowledge tracing: o pyKT chama o de 2009-2010 de "the standard benchmark for KT methods over the last decade" [F: liu2022pykt, §3.2].

Termos próprios: **skill builder** é um conjunto de problemas de matemática em que o aluno termina ao acertar três seguidos; pedir dica ou "Break this Problem Into Steps" marca a questão como errada; a última dica dá a resposta [F: assistments2026skillbuilder0910]. **Problema original** é o problema principal; **scaffolding** são as subquestões abertas quando o aluno erra o original (`original` = 1 ou 0) [F: assistments2026interpret; choi2020ednet, §3.2].

## Problema que resolve

Fornece sequências reais de resposta por aluno e por habilidade, com tempo de resposta, contagem de tentativas e de dicas, numa população escolar, o que permite treinar e comparar modelos de traçado de conhecimento [I]. A plataforma também funciona como ambiente de experimentos randomizados: os autores relatam uso em mais de 18 estudos publicados e "a few dozen" publicações de mineração de dados até 2014 [F: heffernan2014assistments, Abstract].

## Fundamentos e funcionamento

### Publicador e população

Publicado pela equipe do ASSISTments no WPI. A origem é a preparação para testes estaduais de alto impacto em escolas de ensino fundamental II e médio americanas, com itens do MCAS de Massachusetts, a partir de 2003 [F: heffernan2014assistments]; Choi et al. descrevem os problemas originais como itens de matemática do 8º ano do MCAS [F: choi2020ednet, §3.2]. Mais de 50.000 alunos usaram a plataforma no ano letivo 2013-2014, número que dobrava a cada ano havia oito anos; o uso é majoritariamente por professores de matemática [F: heffernan2014assistments, Abstract]. A faixa etária não é declarada nos datasets; por ser ensino fundamental II, corresponde aproximadamente a 11 a 14 anos [I].

### Os datasets

| Dataset | Conteúdo declarado pela fonte | Tamanho | Fonte |
|---|---|---|---|
| 2009-2010 skill builder | respostas em skill builders de matemática | 4.217 alunos, 26.688 questões, 123 tags, 346.860 interações na versão atualizada, só 17.751 questões com KC; a versão original tinha 525.535 linhas com duplicatas | [F: abdelrahman2023ktsurvey; choi2020ednet, Table 1; xiong2016going, §4.1] |
| 2012-2013 com afeto | ano letivo inteiro, com predições de afeto por problema | 46.674 alunos, 179.999 questões, 265 tags, 6.123.270 logs | [F: assistments2026data2012; choi2020ednet, Table 1] |
| 2015 skill builder | 100 skill builders com mais respostas | 19.917 alunos, 100 tags, 708.631 logs | [F: assistments2026data2015; choi2020ednet, Table 1] |
| 2017 (competição longitudinal) | clickstream de 2004-2007 no ensino fundamental II, ligado a desfechos posteriores (curso no ensino médio, faculdade, primeiro emprego) | não informado na página | [F: assistments2017competition] |

A página do dataset de 2015 não traz dicionário de dados, contagens nem citação; as contagens acima são de terceiros [F: assistments2026data2015].

### Granularidade e campos

O grão é **aluno × problema** (uma linha por tentativa de problema, com resumo das ações), não por ação [I]. Campos documentados na página de interpretação [F: assistments2026interpret]:
- `user_id`; `order_id`, "chronological", id do log original;
- `correct`: 1 se certo na primeira tentativa, 0 se errado ou se pediu ajuda; em dissertativa pode ser fracionário (nota do professor);
- `first_response_time`: "Time between start time and first student action (asking for hint or entering an answer)", em milissegundos;
- `attempt_count`, `hint_count`, `original`, `skill_id`, `opportunity`, `opportunity_original`;
- `overlap_time`: tempo para completar o problema em milissegundos, com o aviso "This field is often computed incorrectly";
- `problem_end_time`: deveria ser instante, mas hoje é milissegundos após o início.

O de 2012-2013 usa `ms_first_response`, `start_time`, `end_time`, `problem_type`, `type` (Linear, Random, Mastery), a coluna `actions` com o log bruto e quatro colunas de afeto (`Average_confidence` de FRUSTRATED, CONFUSED, CONCENTRATING, BORED) entre 0 e 1 [F: assistments2026data2012]. As colunas de afeto são **predições de detectores**, não observações [F: assistments2026data2012].

### Desidentificação, licença e acesso

Não há licença aberta: o uso depende de aceitar termos que exigem tornar públicos dados e algoritmos nos artigos ("If you want to not share your source code, then you can not use this data"), não repassar os dados, usá-los só para o fim declarado, não tentar descobrir informação pessoal e, se a encontrar, apagá-la e avisar a equipe; os termos lembram que dados de aluno estão sob a FERPA [F: assistments2026terms]. A desidentificação aparece como substituição de identificadores (`user_id`, `teacher_id`, `school_id`) [F: assistments2026interpret], sem descrição de método. O IRB do WPI aprovou a execução de estudos externos na plataforma sob isenção de dado desidentificado, cabendo a cada pesquisador externo obter a própria aprovação [F: heffernan2014assistments]. O texto das questões de 2012-2013 não é público e exige pedido ao coordenador [F: assistments2026data2012]. A competição de 2017 descreve seu clickstream como "carefully deidentified" [F: assistments2017competition].

## Vantagens e limitações

Vantagens: população escolar real; latência até a primeira ação em milissegundos; dicas e scaffolding registrados; anos diferentes do mesmo sistema; o de 2012-2013 traz contexto de escola e turma e detectores de afeto; dados ASSISTments também foram enviados ao DataShop [F: koedinger2010datashop, §I].

Limitações e problemas conhecidos:
- **Duplicação no 2009-2010.** A própria página avisa "Duplicated data records have been detected" e oferece versão corrigida, com uma linha por aluno-problema e habilidades múltiplas fundidas em `skill1_skill2` [F: assistments2026skillbuilder0910]. Xiong et al. contaram 123.778 linhas duplicadas em 525.535 (23,6%), diferentes só nos campos de oportunidade, e identificaram ainda dois problemas: linhas repetidas por habilidade em problemas com várias habilidades e mistura de problemas originais e de scaffolding; com dados limpos o DKT não supera o PFA [F: xiong2016going]. Detalhes em `adp.kt.deep-knowledge-tracing`.
- **Pré-processamento não comparável.** O AUC relatado do DKT no ASSISTments2009 varia de 0,73 a 0,821 entre artigos [F: liu2022pykt, §3.3], e o survey de Abdelrahman et al. considera a versão original do 2009 não confiável e diz que resultados com versões diferentes ou com duplicatas "should not be directly compared" [F: abdelrahman2023ktsurvey].
- **Habilidades sem rótulo.** No 2012, 126.908 das 179.999 questões não têm nenhum dos 265 KCs, o que o survey associa ao desempenho menor dos modelos nesse conjunto [F: abdelrahman2023ktsurvey].
- **Campos de tempo frágeis:** `overlap_time` frequentemente errado e `problem_end_time` com semântica trocada [F: assistments2026interpret].
- **Viés de seleção:** o de 2015 cobre só os 100 skill builders mais respondidos [F: assistments2026data2015]; a regra de três acertos seguidos faz o número de itens por aluno depender do desempenho [I]. Ver `lae.dq.bias-and-validity`.

## Métricas e métodos de avaliação

Uso típico: previsão de acerto na próxima questão, medida por AUC, comparando regressão logística, BKT e modelos profundos. Gervet et al. usam quatro versões (2009, 2012, 2015, 2017) entre nove datasets; a regressão logística lidera no 2009 e o DKT no 2012, 2015 e 2017 [F: gervet2020when]. No 2017, o dataset registra todas as tentativas consecutivas no mesmo item, enquanto os outros registram só a primeira [F: gervet2020when]; ver `adp.kt.comparison` e `adp.eval.predictive-metrics`.

## Exemplo técnico independente de domínio

```
# checagem mínima antes de usar um log aluno x problema
assert unique(order_id)                       # duplicatas (caso 2009-2010)
linhas_por_problema = count(order_id, skill)  # >1 => linha replicada por habilidade
filtrar original == 1 se o modelo supõe uma resposta por item
descartar overlap_time; derivar duração de start_time/end_time quando confiáveis
registrar versão do arquivo e passos de limpeza no README do dataset derivado
```

## Relações com outros conceitos

Parte de `dat.ds.comparison`. Base empírica clássica de `adp.kt.bayesian-knowledge-tracing`, `adp.kt.deep-knowledge-tracing` e `adp.kt.comparison`. O episódio de duplicação ilustra `dat.qual.loss-and-deduplication` e a necessidade de documentação em `dat.rd.data-documentation`. Os experimentos na plataforma em uso escolar são o caso de `dat.ethics.research-vs-operation`. Logs por aluno com escola e turma tocam em `psg.deid.reidentification-risk`.

## Lacunas e questões abertas

- O texto integral dos termos e das páginas de 2017 não informa número de alunos nem campos da competição longitudinal; não verificado.
- Não há descrição pública do método de desidentificação nem de idade ou série dos alunos por dataset.
- Contagens de 2012 e 2015 vêm de terceiros (Choi et al., pyKT) e mudam com o pré-processamento; não há tabela oficial.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| heffernan2014assistments | academico | 2026-10-30 |
| assistments2026skillbuilder0910 | fornecedor | 2026-10-30 |
| assistments2026interpret | fornecedor | 2026-10-30 |
| assistments2026data2012 | fornecedor | 2026-10-30 |
| assistments2026data2015 | fornecedor | 2026-10-30 |
| assistments2017competition | fornecedor | 2026-10-30 |
| assistments2026terms | fornecedor | 2026-10-30 |
| xiong2016going | academico | 2026-10-30 |
| liu2022pykt | academico | 2026-10-30 |
| choi2020ednet | academico | 2026-10-30 |
| gervet2020when | academico | 2026-10-30 |
| abdelrahman2023ktsurvey | academico | 2026-10-30 |
| koedinger2010datashop | academico | 2026-10-30 |
