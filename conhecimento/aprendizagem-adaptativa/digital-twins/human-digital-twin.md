---
id: adp.dt.human-digital-twin
titulo: Human digital twin
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [lin2024hdtsurvey, chen2023hdtnetworking, grieves2017emergent, fuller2020enabling, glaessgen2012paradigm]
relacoes:
  - { tipo: depende-de, alvo: adp.dt.digital-twin-origins }
  - { tipo: relacionado-a, alvo: adp.dt.learning-digital-twin }
  - { tipo: complementa, alvo: adp.dt.architecture-and-validation }
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
termos: [human digital twin, digital twin for workers, digital patient, cognitive mimetics, behavior modeling]
---

# Human digital twin

## Definição e terminologia

*Human digital twin* (HDT) é "a réplica, no mundo digital, de um humano do mundo físico" [F: lin2024hdtsurvey]. Chen et al. definem HDT como uma representação *in silico* do corpo de um indivíduo capaz de refletir seu estado molecular, fisiológico, emocional e psicológico e mudanças de estilo de vida [F: chen2023hdtnetworking, abstract]. O survey de Lin et al. registra que o campo nasceu no domínio industrial sob outros nomes — "digital twin for workers", "digital athlete" — e que o termo "human digital twin" aparece pela primeira vez na literatura em um estudo de simulação de operações de montagem automotiva (Baskaran et al.), que modelava corpos de trabalhadores para avaliar ergonomia e viabilidade de tarefas [F: lin2024hdtsurvey]. Miller e Spatz, em visão unificada citada pelo survey, caracterizam o humano a ser espelhado por oito categorias de atributos: físicos, fisiológicos, perceptuais, de desempenho cognitivo, personalidade, estado emocional, postura ética e comportamento [F: lin2024hdtsurvey].

O que não é: um avatar 3D ou um prontuário eletrônico isolado não constitui HDT; pela definição herdada de digital twin, exige-se fluxo de dados contínuo do humano para o modelo e retorno de informação (previsões, diagnósticos, recomendações) do modelo para o humano [F: lin2024hdtsurvey] [F: fuller2020enabling].

## Problema que resolve

Em saúde: falta de interação de informação em tempo real, dificuldade de monitorar doenças crônicas de curso longo e envelhecimento populacional; o HDT promete previsão, diagnóstico e monitoramento contínuo sem interferir na vida diária do paciente [F: lin2024hdtsurvey]. Na indústria (Industria 4.0/5.0): integrar o trabalhador ao sistema ciberfísico — alocação de tarefas, avaliação de fadiga e ergonomia, treinamento [F: lin2024hdtsurvey]. Em ambos os casos, o problema de fundo é o mesmo do digital twin industrial — substituir heurística e teste físico por modelo individual continuamente sincronizado [I].

## Fundamentos e funcionamento

Lin et al. propõem (e constatam na literatura) uma arquitetura em três blocos: (1) representação do humano no mundo físico, com coleta e percepção por sensores; (2) o HDT no mundo digital, com processamento de dados, modelagem, simulação e motor de análise/otimização; (3) interface humano-computador ligando os dois mundos [F: lin2024hdtsurvey]. Os dados de modelagem caem em cinco categorias: externos (altura, peso), fisiológicos (frequência cardíaca, pressão), comportamentais (sono, dieta, uso do telefone), de interação social e de ambiente [F: lin2024hdtsurvey]. A modelagem divide-se em física (órgãos, p.ex. gêmeos cardiovasculares e hepáticos; corpo, por modelagem paramétrica 3D, sequências RGB-D e escaneamento) e comportamental (atividade, interação social e estilo de vida) [F: lin2024hdtsurvey]. Chen et al. descrevem a cadeia em cinco camadas: aquisição de dados, comunicação, computação, gestão de dados e análise/decisão [F: chen2023hdtnetworking, abstract].

## Requisitos e pressupostos

- Sensoriamento contínuo e multimodal (vestíveis, smartphones, câmeras, mídias sociais, bases clínicas) com fusão de dados multi-fonte [F: lin2024hdtsurvey].
- Latência compatível com interação em tempo real; o survey cita 49 ms de atraso de transmissão de vídeo em 5G como viabilizador [F: lin2024hdtsurvey].
- Consentimento, proteção de dados e mecanismos de privacidade (aprendizado federado, blockchain são as mitigação discutidas) [F: lin2024hdtsurvey].
- Pressuposto crítico e frequentemente implícito: que o comportamento humano seja modelável e previsível a partir dos dados coletados — pressuposto muito mais frágil do que no caso de máquinas [I].

## O que muda quando o "objeto físico" é uma pessoa

Diferenças estruturais frente ao digital twin de artefatos, sintetizadas a partir das fontes [I, com apoios factuais indicados]:

- **Não-estacionariedade e agência**: Grieves e Vickers excluem explicitamente do seu modelo os "sistemas que evoluem" — que têm aleatoriedade embutida ou mudam as próprias regras em operação [F: grieves2017emergent]; pessoas são exatamente esse tipo de sistema, e aprendem em resposta ao próprio twin [I].
- **Ambiente não controlado**: a literatura de DT assume ambiente controlado; para HDT basta modelar as trocas entre pessoa e ambiente, não o ambiente completo [F: lin2024hdtsurvey].
- **Dados esparsos e heterogêneos**: dados humanos vêm em formas e sistemas diversos, gerando "ilhas de informação"; ontologias são a solução proposta, ainda não aplicada a HDT [F: lin2024hdtsurvey].
- **Incerteza**: no DT aeroespacial a incerteza é tratada com simulação probabilística e atualização bayesiana [F: glaessgen2012paradigm]; para humanos, parte da incerteza é irredutível por agência e contexto [H].
- **Ética e privacidade**: dados íntimos, risco de uso indevido, propriedade do twin e destino do twin após a morte (a maioria dos respondentes de um estudo citado quer que seu HDT seja apagado quando morrerem) [F: lin2024hdtsurvey].

## Vantagens e limitações

Vantagens relatadas: medicina de precisão com planos individualizados (o programa Twin Precision Treatment coletou e analisou sinais corporais por sensores e aplicativo para tratamento personalizado de diabetes, em estudo retrospectivo); monitoramento de atletas (framework SmartFit); previsão de estresse mental com 98% de acurácia usando 20 fontes de dados; ergonomia e alocação de tarefas na manufatura [F: lin2024hdtsurvey].

Limitações e críticas publicadas: o desenvolvimento do HDT "ainda está em sua infância" [F: lin2024hdtsurvey]. O survey discute críticas éticas: Braun argumenta que a ambiguidade fundamental da representação se agrava quando um HDT, e não a pessoa, age em seu nome, ameaçando a distinção entre verdadeiro e falso; De Maeyer e Markopoulos levantam o problema do término (apagar ou continuar o twin); Ryan sustenta que sistemas de IA não podem ser objeto de confiança no sentido humano, apenas de dependência; e há paralelos com as objeções éticas à clonagem digital e à "ressurreição digital" de falecidos [F: lin2024hdtsurvey]. Essas críticas foram lidas aqui através do survey, não nas fontes originais (ver Lacunas).

## Alternativas e comparações

| Aspecto | DT industrial | Human digital twin |
|---|---|---|
| Objeto | artefato projetado, especificável | pessoa, com agência e aprendizado [I] |
| Dados | sensores dedicados, alta taxa | vestíveis, autorrelato, mídia social, esparsos [F: lin2024hdtsurvey] |
| Modelo | físico (CAD, FEM, multifísica) [F: glaessgen2012paradigm] | físico (órgãos/corpo) + comportamental (ML) [F: lin2024hdtsurvey] |
| Validação | comparação com teste físico [F: glaessgen2012paradigm] | acurácia preditiva; sem equivalente a teste destrutivo [I] |
| Riscos | segurança industrial | privacidade, representação, autonomia [F: lin2024hdtsurvey] |

## Métricas e métodos de avaliação

A literatura de HDT avalia sobretudo acurácia preditiva de modelos de ML sobre dados retrospectivos (ex.: 98% no modelo de estresse; classificação de estado físico no SmartFit) e desempenho de componentes (erro milimétrico em reconstrução corporal 3D) [F: lin2024hdtsurvey]. Avaliação da fidelidade do *sistema* HDT como um todo — equivalente aos testes de virtualidade de Grieves — não aparece consolidada [I]; ver `adp.dt.architecture-and-validation` e `adp.eval.predictive-metrics`.

## Exemplo técnico independente de domínio

Fluxo de trabalho de um HDT, conforme Lin et al. [F: lin2024hdtsurvey], em pseudocódigo:

```
definir_proposito(aplicacao)            # determina atributos e dados relevantes
loop:
    d = sensores.ler(pessoa, ambiente)  # multi-fonte, multimodal
    interface.transferir(d)             # físico -> digital
    base.atualizar(d); limpar; fundir
    modelo = construir_ou_atualizar(base)   # físico (corpo/órgãos) + comportamento
    pred = modelo.simular_e_prever()
    if avaliar(pred, base) aceitável:   # motor de avaliação
        interface.devolver(pred)        # digital -> físico: sugestão/alerta
    else:
        otimizar(modelo)
```

## Relações com outros conceitos

Depende de `adp.dt.digital-twin-origins` (herda definição e níveis de integração). `adp.dt.learning-digital-twin` é a especialização do HDT para o aprendiz — um HDT restrito a atributos cognitivos e de aprendizagem [I]. `adp.lm.learner-model` é o conceito pré-existente em educação que o HDT parcialmente reinventa; a comparação é feita no documento central. A arquitetura e a validação são detalhadas em `adp.dt.architecture-and-validation`.

## Lacunas e questões abertas

- As críticas éticas (Braun 2021, "Represent me: please!", Journal of Medical Ethics; De Maeyer & Markopoulos 2020; Ryan 2020) foram citadas via survey; a cópia aberta de Braun foi tentada (jme.bmj.com, HTTP 403) e não verificada.
- O survey de Lin et al. não é uma revisão sistemática com protocolo PRISMA: a triagem (327 publicações, 2018–jul/2024, em Springer/IEEE/ACM/Elsevier) é descrita, mas sem critérios de qualidade explícitos [F: lin2024hdtsurvey] [I].
- Não localizamos, nas fontes abertas, nenhum HDT comportamental avaliado prospectivamente (previsões registradas antes dos desfechos); as acurácias relatadas são retrospectivas [I].
- A fronteira entre HDT e perfilamento de usuário convencional (recomendadores, modelos de personalidade) permanece mal definida na literatura [I]; o próprio survey classifica como HDT trabalhos que são modelos preditivos clássicos [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| lin2024hdtsurvey | academico | 2026-10-29 |
| chen2023hdtnetworking | academico (apenas abstract) | 2026-10-29 |
| grieves2017emergent | academico | 2026-10-29 |
| fuller2020enabling | academico | 2026-10-29 |
| glaessgen2012paradigm | academico | 2026-10-29 |
