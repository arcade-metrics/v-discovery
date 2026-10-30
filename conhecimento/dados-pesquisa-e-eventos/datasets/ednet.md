---
id: dat.ds.ednet
titulo: EdNet
tipo: estudo-de-caso
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [choi2020ednet, riiid2020ednetrepo]
relacoes:
  - { tipo: parte-de, alvo: dat.ds.comparison }
  - { tipo: complementa, alvo: adp.kt.deep-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.kt.comparison }
  - { tipo: avaliado-por, alvo: adp.eval.predictive-metrics }
  - { tipo: complementa, alvo: dat.qual.granularity-and-constructs }
  - { tipo: relacionado-a, alvo: dat.ev.event-model }
  - { tipo: relacionado-a, alvo: dat.rd.data-documentation }
  - { tipo: relacionado-a, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
termos: [EdNet, KT1, KT2, KT3, KT4, bundle, elapsed_time, cursor_time, deslocamento de timestamp, hierarquia de abstração]
---

# EdNet

## Definição e terminologia

**EdNet** é um dataset de interações de estudantes com um sistema de tutoria com IA para preparação ao teste TOEIC (Listening and Reading), publicado pela equipe de pesquisa da empresa que opera o serviço, na Coreia do Sul; os autores o apresentam como "a large-scale hierarchical dataset of diverse student activities" e, em 2020, "the largest public IES dataset released to date" [F: choi2020ednet, Abstract]. IES aqui é "Interactive Educational System". O artigo foi publicado no AIED 2020 (LNCS) e está aberto no arXiv (v3, 01/07/2020) [F: choi2020ednet].

Termos: **bundle** é um conjunto de questões que compartilham passagem, imagem ou áudio e são apresentadas juntas; o aluno precisa responder todas para completá-lo [F: choi2020ednet, §2.2]. **KT1 a KT4** são quatro recortes do mesmo log, em resolução crescente [F: choi2020ednet, §2.2].

## Problema que resolve

Os autores argumentam que ASSISTments, Junyi, Synthetic e STATICS não são grandes o bastante para modelos baseados em dados e registram só resolução de questões [F: choi2020ednet, §1]. EdNet acrescenta escala e tipos de ação além da resposta: ler explicações, assistir aulas em vídeo, eliminar alternativas, tocar e pausar áudio, comprar [F: choi2020ednet, §2.1].

## Fundamentos e funcionamento

### Escala e população

O artigo informa 131.441.538 interações de 784.309 alunos desde 2017, média de 441,20 interações por aluno, 13.169 questões e 1.021 aulas marcadas com 293 tipos de habilidade [F: choi2020ednet, §2.1]. O serviço tinha cerca de 780.000 alunos na Coreia do Sul e roda em Android, iOS e web [F: choi2020ednet, §2]. Idade, escolaridade e demografia não são informadas [I]; o público de um preparatório para o TOEIC é presumivelmente jovem adulto ou adulto, sem confirmação na fonte [H].

### Hierarquia KT1 a KT4

| Nível | O que contém | Alunos | Logs | Tipos de log | Colunas (repositório) |
|---|---|---|---|---|---|
| KT1 | pares questão-resposta, desde 18/04/2017 | 784.309 | 95.293.926 | 1 | timestamp, solving_id, question_id, user_answer, elapsed_time |
| KT2 | ações de resolução (entrar, responder, sair do bundle), desde 27/08/2018 | 297.444 | 56.360.602 | 3 | timestamp, action_type, item_id, source, user_answer, platform |
| KT3 | KT2 + entrar/sair de explicações e aulas | 297.915 | 89.270.654 | 4 | como KT2 |
| KT4 | todas as ações coletadas, incluindo áudio, eliminação de alternativa, pagamento, cupom | 297.915 | 131.441.538 | 13 | KT2 + cursor_time |

Contagens [F: choi2020ednet, Table 1, §2.2]; colunas e datas de início [F: riiid2020ednetrepo]. Há ainda tabelas de conteúdo: questões, aulas, itens de pagamento e cupons [F: riiid2020ednetrepo]; a Figura 2 do artigo lista, para questões, id, parte, bundle e tag [F: choi2020ednet, Fig. 2].

### Granularidade e tempo

O grão vai de resposta (KT1) a ação de interface (KT4) [F: choi2020ednet, §2.2]. Em KT1, `timestamp` e `elapsed_time` estão em milissegundos [F: riiid2020ednetrepo]; os exemplos do artigo mostram timestamps Unix em milissegundos também em KT2 a KT4 e, em KT4, `cursor_time` de 0 e 10000 associado a tocar e pausar áudio [F: choi2020ednet, Tables 2-5]. Cada evento de interface tem seu próprio carimbo, o que permite derivar latências entre ações (entrar no bundle, eliminar alternativa, selecionar, sair) [I]. Atenção: em KT1 o `elapsed_time` é atribuído por bundle (o exemplo repete 47000 para três questões do mesmo bundle) [F: choi2020ednet, Table 2], então não é tempo por questão [I].

### Desidentificação, licença e acesso

Licença Creative Commons Attribution-NonCommercial 4.0 International, "for research purposes only" [F: choi2020ednet, §1; riiid2020ednetrepo]. Download por links públicos indicados no repositório, em arquivos zip, um CSV por aluno nomeado `{user_id}.csv`; KT1 tem 1,2 GB compactado e 5,6 GB descompactado [F: riiid2020ednetrepo]. O repositório informa que os timestamps foram "shifted by fixed values due to security issues"; não descreve como os ids de aluno foram gerados [F: riiid2020ednetrepo]. Não há campos demográficos [I].

## Vantagens e limitações

Vantagens: maior escala pública entre os datasets de KT comparados pelos autores [F: choi2020ednet, Table 1]; ações não avaliativas (aula, explicação, áudio, eliminação) registradas; tempo em milissegundos por evento; licença explícita e links públicos de download [F: riiid2020ednetrepo].

Limitações e problemas conhecidos:
- **Inconsistência de contagens no próprio artigo**: o resumo fala em 131.417.236 interações e o corpo em 131.441.538; o texto dá 95.294.926 consumos de questões e a tabela, 95.293.926 [F: choi2020ednet, Abstract, §2.1, Table 1].
- **Documentação com divergências**: a descrição do KT1 lista `solving_id`, mas o exemplo usa coluna de bundle; o texto do KT4 cita `erase_choice` e o exemplo usa `eliminate_choice`; valores de `source` têm erros de digitação; atributos de aula indisponíveis aparecem como -1 [F: riiid2020ednetrepo].
- **Desfecho ausente**: escores reais do teste "are not released yet" [F: riiid2020ednetrepo].
- **Conteúdo não disponível**: só ids e tags, sem texto das questões [F: choi2020ednet, Table 1].
- **População única e não descrita**: um único serviço comercial, um domínio (inglês como língua estrangeira para teste) e sem demografia, o que limita generalização para outras idades e domínios [I]; ver `lae.dq.bias-and-validity`.
- **Deslocamento fixo de tempo**: preserva intervalos, mas impede análises de calendário (hora do dia, dia letivo) [I].

## Métricas e métodos de avaliação

Usos propostos pelos autores: knowledge tracing (o SAINT foi treinado no KT1), previsão de abandono de sessão em ambiente móvel, pré-treinamento para tarefas com poucos rótulos e simuladores de aluno para recomendação por aprendizado por reforço [F: choi2020ednet, §4]. A avaliação típica é AUC na previsão da resposta seguinte; ver `adp.eval.predictive-metrics` e `adp.kt.comparison`.

## Exemplo técnico independente de domínio

```
# derivar latências por questão a partir de um log no estilo KT2/KT4
para cada aluno, ordenar eventos por timestamp (ms)
para cada bundle b:
    t_enter = timestamp(enter b)
    para cada respond q em b:
        latencia_q = timestamp(respond q) - (timestamp(respond anterior em b) ou t_enter)
    hesitacao = contar(eliminate_choice, select) antes do respond      # só KT4
descartar sessões com lacunas > limiar (app em segundo plano, offline)
```

## Relações com outros conceitos

Parte de `dat.ds.comparison`. Usado para treinar e comparar modelos de `adp.kt.deep-knowledge-tracing` e `adp.kt.comparison`. A hierarquia KT1-KT4 é exemplo de como um mesmo log de eventos (`dat.ev.event-model`) é publicado em vários grãos, tema de `dat.qual.granularity-and-constructs`. O deslocamento de timestamps e os ids por arquivo são escolhas de `psg.deid.anonymization-and-pseudonymization`. As divergências de documentação mostram por que um datasheet (`dat.rd.data-documentation`) importa.

## Lacunas e questões abertas

- Não foi verificado o método de geração dos `user_id` nem se o deslocamento de tempo é igual para todos os alunos.
- A unidade de `cursor_time` não está declarada no repositório; os exemplos sugerem milissegundos, sem confirmação.
- Não há versão ou data de release dos arquivos; mudanças posteriores no conteúdo baixado não são rastreáveis.
- Faixa etária e escolaridade dos alunos não são informadas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| choi2020ednet | academico | 2026-10-30 |
| riiid2020ednetrepo | fornecedor | 2026-10-30 |
