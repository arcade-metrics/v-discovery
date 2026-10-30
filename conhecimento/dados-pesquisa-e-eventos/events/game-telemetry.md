---
id: dat.ev.game-telemetry
titulo: Telemetria de jogos
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [seifelnasr2013gameanalytics, zoeller2013telemetry, su2021review, serranolaguna2017applying, otel2026semconvsession, cncf2026cloudevents, w3c2021tracecontext]
relacoes:
  - { tipo: depende-de, alvo: dat.ev.event-model }
  - { tipo: complementa, alvo: dat.ev.event-to-xapi-mapping }
  - { tipo: complementa, alvo: dat.ev.instrumentation-and-opentelemetry }
  - { tipo: complementa, alvo: dat.qual.granularity-and-constructs }
  - { tipo: complementa, alvo: dat.qual.loss-and-deduplication }
  - { tipo: relacionado-a, alvo: dat.ethics.research-vs-operation }
  - { tipo: complementa, alvo: lae.found.analytics-cycle }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: psg.deid.anonymization-and-pseudonymization }
termos: [telemetria de jogo, game analytics, game metrics, métricas de jogador, métricas de processo, métricas de desempenho, telemetria voltada ao desenvolvedor, telemetria voltada ao usuário, completable, alternativa, variável significativa, sessão, amostragem]
---

# Telemetria de jogos

## Definição e terminologia

**Telemetria de jogo** é a coleta remota e contínua de dados sobre o uso de um jogo, em geral como eventos enviados do cliente para um serviço [I]. A literatura distingue três camadas: telemetria (o dado bruto coletado), **métricas** (variáveis, atributos e valores calculados a partir dele) e **game analytics**, "the process of identifying and communicating meaningful patterns that can be used for game decision making" [F: su2021review, §1, citando Seif El-Nasr et al.]. A obra de referência é o livro organizado por Seif El-Nasr, Drachen e Canossa, que se apresenta como "the first book on game telemetry, game metrics and game analytics" e cobre, entre outros tópicos, "design of telemetry systems" [F: seifelnasr2013gameanalytics, metadados]. O texto integral do livro não foi acessado; as afirmações sobre sua classificação vêm de revisão aberta que o cita.

O que não é: telemetria não é avaliação. Ela registra comportamento observável; o construto (aprendizagem, motricidade, atenção) só aparece quando um modelo de medida interpreta os eventos [I].

## Problema que resolve

Jogos produzem interações em alta frequência e em contextos não supervisionados. Sem instrumentação explícita, o que o jogador fez se perde ou fica implícito no estado final [I]. Serrano-Laguna et al. observam que a padronização dos dados coletados é "one of the key open issues" de learning analytics e que jogos sérios são caso particularmente difícil porque "generate a diverse range of data" [F: serranolaguna2017applying, Abstract].

## Fundamentos e funcionamento

### Classes de métrica e de público

Segundo a classificação de Seif El-Nasr et al., reproduzida por Su, Backlund e Engström, as métricas de jogo dividem-se em **métricas de jogador** (comportamento e pesquisa de usuário), **de processo** (acompanhamento do desenvolvimento) e **de desempenho** (taxa de quadros, erros, execução do cliente) [F: su2021review, §2]. A mesma revisão subdivide a análise de desenvolvimento em gameplay, interface, sistema, processo e desempenho; a análise de interface pressupõe que "all the menu and button settings can be recorded" [F: su2021review, §5.2.2].

Zoeller separa **telemetria voltada ao desenvolvedor**, que coleta como desenvolvedores e testadores interagem com o jogo inacabado para melhorar a produção, de **telemetria voltada ao usuário**, "typically collected after a game is launched and mainly aimed at tracking, analyzing and visualizing player behavior" [F: zoeller2013telemetry, resumo]. Para pesquisa, as duas coexistem e precisam ser separáveis no dado: eventos de teste interno não podem contaminar amostras [I].

### Modelo de interação para jogos com propósito educativo

Serrano-Laguna et al. derivam de uma revisão de jogos sérios um modelo em que cada interação tem cinco atributos: "1) a timestamp [...] 2) a user id [...] 3) an action [...] 4) a target [...] and 5) an optional value" [F: serranolaguna2017applying, §3]. Os alvos são de três tipos [F: serranolaguna2017applying, §3.1 a §3.3]:

| Tipo de alvo | Exemplos | Ações | Métricas derivadas |
|---|---|---|---|
| completable | jogo, sessão, nível, missão | start, progress (0,0 a 1,0), complete | completude, vezes completado, tempo para completar |
| alternative | pergunta, menu, caminho, diálogo | select, unlock | opções escolhidas e desbloqueadas |
| meaningful variable | pontuação, moedas, vida, posição | set | valor final e evolução |

Os autores alertam que interações customizadas demais levam à "loss of the automatic or semi-automatic processes that the standard is intended to support" [F: serranolaguna2017applying, §3.4].

### Sessão como unidade

A convenção semântica de sessão do OpenTelemetry define sessão como o período que abrange as atividades da aplicação e do usuário, atribui um `session.id` a todos os logs, eventos e spans emitidos nesse período e prevê `session.previous_id` para encadear sessões quando há expiração por inatividade [F: otel2026semconvsession]. A convenção está em status *Development* [F: otel2026semconvsession].

## Requisitos e pressupostos

- O que instrumentar é decidido antes da coleta, a partir das perguntas de pesquisa; telemetria retroativa não existe [I].
- O cliente tem buffer local e reenvio, pois atividades lúdicas costumam rodar em redes instáveis (ver `dat.qual.loss-and-deduplication`).
- Identificadores de jogador são pseudônimos e não reutilizáveis fora do estudo (ver `psg.deid.anonymization-and-pseudonymization`).

## Vantagens e limitações

Vantagens [I]: observação não intrusiva, alta resolução temporal, escala e reprodutibilidade do instrumento (o mesmo código coleta igual em todos os dispositivos).

Limitações:
- Custo de coleta: cada evento ocupa banda, bateria e armazenamento; a CloudEvents recomenda eventos compactos e só garante encaminhamento até 64 KByte [F: cncf2026cloudevents, §Size Limits].
- Amostragem herdada de ferramentas de observabilidade é inadequada para pesquisa: a flag `sampled` do W3C Trace Context existe porque registrar todas as requisições "becomes prohibitively expensive, at load" [F: w3c2021tracecontext, §3.2.2.5.1], mas descartar eventos de um participante enviesa a amostra [I].
- A revisão aponta como desafio aberto "how to ensure that the collected data can represent the player real demands" [F: su2021review, §6.1].

## Alternativas e comparações

| Abordagem | Granularidade | Custo | Uso típico em pesquisa |
|---|---|---|---|
| Eventos discretos de interação | ação a ação | médio | sequências, erros, latência de resposta |
| Amostragem periódica de estado (posição, variáveis) | fixa no tempo | alto | trajetórias, controle motor |
| Agregados no cliente (contadores por sessão) | sessão | baixo | engajamento; perde a sequência |
| Gravação de tela ou entrada bruta | máxima | muito alto | análise qualitativa; maior risco de privacidade |

Síntese deste documento [I]; a escolha entre elas é tratada em `dat.qual.granularity-and-constructs`.

## Métricas e métodos de avaliação

Qualidade da telemetria [I]: taxa de eventos perdidos por sessão (lacunas em `sequence`), proporção de sessões com início e fim registrados, atraso entre ocorrência e recebimento, e cobertura do plano de instrumentação (eventos previstos e efetivamente emitidos por versão do cliente).

## Exemplo técnico independente de domínio

Plano de instrumentação mínimo para uma atividade com níveis e escolhas [I]:

```
sessao.inicio       {session_id, previous_id?, device_pseudo, client_ver, content_ver, config_hash}
nivel.inicio        {nivel_id, tentativa}
alternativa.escolha {alternativa_id, opcao, correta?, latencia_ms, tentativa}
variavel.definida   {variavel, valor, unidade}
nivel.progresso     {nivel_id, progresso: 0.0..1.0}
nivel.fim           {nivel_id, sucesso, duracao_ms}
sessao.fim          {motivo: concluida|inatividade|fechada, eventos_emitidos}
```

## Relações com outros conceitos

Depende de `dat.ev.event-model` para o envelope; o modelo de interação mapeia para xAPI em `dat.ev.event-to-xapi-mapping`; a instrumentação técnica está em `dat.ev.instrumentation-and-opentelemetry`. A escolha de granularidade fica em `dat.qual.granularity-and-constructs`, e a separação entre dado operacional e de pesquisa em `dat.ethics.research-vs-operation`. A telemetria é a etapa de coleta do ciclo descrito em `lae.found.analytics-cycle`.

## Lacunas e questões abertas

- O livro de Seif El-Nasr, Drachen e Canossa (2013) não foi lido; o capítulo sobre boas práticas e o capítulo de Zoeller só foram vistos pelo resumo. A classificação de métricas está citada por fonte secundária.
- Não há, nas fontes lidas, recomendação quantitativa de taxa de amostragem de estado para jogos educativos.
- A convenção de sessão do OpenTelemetry ainda é *Development*; pode mudar.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| seifelnasr2013gameanalytics | academico [metadados] | 2026-10-30 |
| zoeller2013telemetry | academico (resumo) | 2026-10-30 |
| su2021review | academico | 2026-10-30 |
| serranolaguna2017applying | academico (versão preprint) | 2026-10-30 |
| otel2026semconvsession | normativo (Development) | 2026-10-30 |
| cncf2026cloudevents | normativo | 2026-10-30 |
| w3c2021tracecontext | normativo | 2026-10-30 |
