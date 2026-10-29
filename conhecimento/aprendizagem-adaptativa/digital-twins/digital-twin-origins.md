---
id: adp.dt.digital-twin-origins
titulo: Origens e definições do conceito de digital twin
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [grieves2014whitepaper, grieves2017emergent, glaessgen2012paradigm, fuller2020enabling, jones2020characterising, lin2024hdtsurvey]
relacoes:
  - { tipo: relacionado-a, alvo: adp.dt.human-digital-twin }
  - { tipo: relacionado-a, alvo: adp.dt.learning-digital-twin }
  - { tipo: complementa, alvo: adp.dt.architecture-and-validation }
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
termos: [digital twin, digital model, digital shadow, digital twin prototype, digital twin instance, mirrored spaces model, information mirroring model]
---

# Origens e definições do conceito de digital twin

## Definição e terminologia

Um *digital twin* (gêmeo digital) é um construto informacional virtual que representa um objeto ou sistema físico específico e permanece vinculado a ele, por fluxo de dados, ao longo do ciclo de vida [F: grieves2017emergent]. Grieves e Vickers definem o digital twin como "um conjunto de construtos de informação virtuais que descreve completamente um produto físico manufaturado, potencial ou real, do nível micro atômico ao nível macro geométrico", e distinguem o *Digital Twin Prototype* (DTP, que descreve o artefato prototípico: requisitos, modelo 3D, listas de materiais e processos) do *Digital Twin Instance* (DTI, vinculado a um exemplar físico específico durante toda a sua vida, com histórico de serviço e estados operacionais capturados de sensores), ambos operados em um *Digital Twin Environment* (DTE) para fins preditivos e interrogativos [F: grieves2017emergent].

A definição aeroespacial, de Glaessgen e Stargel (NASA/USAF), é: "um Digital Twin é uma simulação integrada, multifísica, multiescala e probabilística de um veículo ou sistema *as-built*, que usa os melhores modelos físicos disponíveis, atualizações de sensores, histórico de frota etc. para espelhar a vida de seu gêmeo voador correspondente" [F: glaessgen2012paradigm]. No mesmo artigo, uma nota de rodapé atribui a concepção original do termo ao Defense Sciences Office da DARPA, e uma figura apresenta o conceito como "Virtual Digital Fleet Leader (a.k.a. Digital Twin)" [F: glaessgen2012paradigm].

O que não é: um modelo digital sem troca automática de dados com o objeto físico não é um digital twin. Fuller et al. consolidam a distinção em três níveis de integração: *digital model* (sem troca automática de dados), *digital shadow* (fluxo automático apenas do físico para o digital) e *digital twin* (fluxo automático bidirecional: mudanças no objeto físico alteram o digital e vice-versa) [F: fuller2020enabling]. Os mesmos autores apontam como equívocos comuns tratar qualquer modelo 3D como digital twin e observam que parte da literatura rotula como "twin" o que, pela definição, é apenas shadow ou model [F: fuller2020enabling].

## Problema que resolve

O problema original é duplo. No ciclo de vida de produto (Grieves): trabalhar apenas com o objeto físico torna caro e lento investigar comportamento, e informação é tratada como substituto de recursos físicos desperdiçados (tempo, energia, material); o gêmeo digital permite projetar, testar e operar a versão virtual antes e durante a vida da física, mitigando comportamentos emergentes imprevistos e indesejáveis (categoria "UU" na taxonomia PD/PU/UD/UU do capítulo) [F: grieves2017emergent]. Na engenharia aeroespacial (NASA/USAF): certificação e sustentação baseadas em similitude, fatores de segurança heurísticos e inspeção por "líder de frota" não escalam para veículos mais leves, cargas maiores e missões sem precedente; o twin substituiria parte dessa heurística por simulação de altíssima fidelidade continuamente atualizada por sensores, prevendo saúde estrutural, vida útil remanescente e probabilidade de sucesso da missão de cada veículo individual [F: glaessgen2012paradigm].

## Fundamentos e funcionamento

### Linha do tempo documentada

- **2002**: apresentação de Michael Grieves à indústria na Universidade de Michigan ("Conceptual Ideal for PLM", 3 de dezembro de 2002), já com todos os elementos do modelo: espaço real, espaço virtual, fluxo de dados do real para o virtual, fluxo de informação do virtual para o real e subespaços virtuais (VS1...VSn) [F: grieves2017emergent].
- **2003 em diante**: o modelo é usado nos primeiros cursos de PLM da Universidade de Michigan como *Mirrored Spaces Model*; aparece assim em artigo de 2005 e como *Information Mirroring Model* no livro de 2006 [F: grieves2017emergent]. O whitepaper de 2014 data a introdução do conceito "em 2003, no meu curso executivo de PLM na Universidade de Michigan" [F: grieves2014whitepaper] — a pequena divergência (2002 × 2003) é entre a apresentação à indústria e o curso [I].
- **Nome "Digital Twin"**: Grieves afirma ter introduzido o termo no livro *Virtually Perfect* (2011, p. 133) e o atribui a John Vickers, da NASA, com quem trabalhava [F: grieves2014whitepaper]; o capítulo de 2017 repete que o termo foi "anexado ao conceito por referência à forma do coautor [Vickers] de descrever o modelo" [F: grieves2017emergent].
- **2010–2012**: a NASA usa o conceito em seus roadmaps tecnológicos (TA 11 e TA 12, 2010) e Glaessgen & Stargel publicam o paper da sessão especial sobre Digital Twin da 53ª conferência SDM da AIAA (2012), primeira definição aeroespacial consolidada [F: glaessgen2012paradigm].
- **Pré-história**: surveys posteriores apontam o programa Apollo como precursor — um "gêmeo físico" em terra para simular o veículo em voo — ainda que não fosse um sistema digital [F: lin2024hdtsurvey].

### Elementos definidores

Sintetizando as fontes primárias, quatro elementos aparecem de forma estável [I]: (1) um objeto físico individual; (2) uma representação virtual desse objeto (não de sua classe); (3) conexão de dados do físico para o virtual e de informação do virtual para o físico — bidirecionalidade [F: grieves2017emergent] [F: fuller2020enabling]; (4) vínculo mantido ao longo do ciclo de vida (criação, produção, operação, descarte) [F: grieves2017emergent]. A versão NASA acrescenta: atualização contínua por sensores embarcados (IVHM), atualização bayesiana das previsões, previsão de vida útil remanescente e capacidade de avaliar consequências de mudanças de missão em tempo quase real [F: glaessgen2012paradigm].

## Requisitos e pressupostos

- Instrumentação do objeto físico e canal de dados contínuo; sem fluxo automático, obtém-se no máximo um digital model [F: fuller2020enabling].
- Modelos com fidelidade suficiente para que previsões substituam teste físico; a NASA considera isso exigir "abordagens revolucionárias de verificação e validação" e classifica o conceito como improvável de amadurecer "por muitas décadas" [F: glaessgen2012paradigm].
- Dados de qualidade, sem ruído e ininterruptos; infraestrutura de TI e integração entre fornecedores — Grieves prevê que a falta de interoperabilidade entre softwares de fornecedores, mais que a técnica, será o gargalo [F: grieves2017emergent] [F: fuller2020enabling].

## Vantagens e limitações

Vantagens documentadas: custo virtual decrescente contra custo físico crescente; testes destrutivos sem destruir nada; detecção de comportamento emergente indesejado antes do deploy; "front-running" — simular à frente do sistema real para apoiar decisão em crise [F: grieves2017emergent]; redução de peso estrutural e certificação por simulação no caso aeroespacial [F: glaessgen2012paradigm].

Limitações: obstáculos organizacionais (silos de informação), conhecimento físico incompleto e explosão do número de estados simuláveis [F: grieves2017emergent]; falta de padronização e de arquitetura genérica, e definições que pouco evoluíram entre 2012 e 2019, dificultando distinguir digital twins de modelos e simulações em geral [F: fuller2020enabling]. A revisão sistemática de Jones et al. (92 publicações da década anterior; consultada apenas por metadados e abstract) consolida 13 características do conceito e aponta sete lacunas, entre elas níveis de fidelidade, propriedade dos dados e benefícios percebidos [F: jones2020characterising, metadados/abstract].

## Alternativas e comparações

| Nível de integração | Fluxo físico→virtual | Fluxo virtual→físico | Exemplo típico |
|---|---|---|---|
| Digital model | manual | manual | planta ou projeto CAD [F: fuller2020enabling] |
| Digital shadow | automático | manual/ausente | dashboard alimentado por sensores [F: fuller2020enabling] |
| Digital twin | automático | automático | replicação de fábrica com atuação [F: fuller2020enabling] |

Na revisão categórica de Fuller et al., 66% dos trabalhos analisados eram de manufatura, 19% de cidades inteligentes e 15% de saúde, e vários artigos que se declaravam "digital twin" foram reclassificados como shadow ou model pelos critérios acima [F: fuller2020enabling].

## Métricas e métodos de avaliação

Grieves propõe os *Tests of Virtuality* (teste sensorial-visual, teste de desempenho e teste de refletividade) para avaliar quão bem o sistema virtual espelha o físico [F: grieves2017emergent]; a NASA avalia o twin pela comparação contínua entre resposta prevista e resposta real do veículo [F: glaessgen2012paradigm]. Detalhes em `adp.dt.architecture-and-validation`.

## Exemplo técnico independente de domínio

Modelo conceitual mínimo, conforme a figura de 2002 [F: grieves2017emergent]:

```
Espaço Real (objeto físico O)  --dados-->   Espaço Virtual (twin T de O)
Espaço Real (objeto físico O)  <--info--    Espaço Virtual (T, VS1..VSn)

loop por fase do ciclo de vida:
    medir estado de O (sensores, inspeção)
    atualizar T com o estado medido           # físico -> virtual
    simular em T (inclusive cópias VS_i para testes destrutivos)
    devolver a O decisões/ajustes derivados   # virtual -> físico
```

## Relações com outros conceitos

Este documento é a base histórica e terminológica da área `digital-twins` do domínio: `adp.dt.human-digital-twin` transfere o conceito para pessoas; `adp.dt.learning-digital-twin` examina sua aplicação ao aprendiz; `adp.dt.architecture-and-validation` detalha camadas, sincronização e validação. A relação com `adp.lm.learner-model` importa porque a exigência de bidirecionalidade e vínculo de ciclo de vida é o critério usado adiante para testar se "gêmeo digital de aprendizagem" difere de modelagem de aluno convencional [I].

## Lacunas e questões abertas

- O texto completo de Jones et al. (2020) não pôde ser aberto nesta sessão (HTTP 403 no ScienceDirect, no CORE e nos repositórios Pure de Bristol e Aberystwyth); apenas metadados e abstract verificados. As 13 características, portanto, não são detalhadas aqui.
- O whitepaper de Grieves é patrocinado pela Dassault Systèmes [F: grieves2014whitepaper]; convém ler a narrativa de origem com essa procedência em mente [I].
- A atribuição do termo a Vickers vem do próprio Grieves; não localizamos documento independente de Vickers anterior a 2010 que use o termo. Não verificado.
- A nota da NASA de que o conceito foi "originalmente concebido pelo DSO/DARPA" [F: glaessgen2012paradigm] conflita parcialmente com a narrativa Grieves/Vickers; as fontes não se citam mutuamente sobre esse ponto [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| grieves2014whitepaper | tecnico | 2026-10-29 |
| grieves2017emergent | academico | 2026-10-29 |
| glaessgen2012paradigm | academico | 2026-10-29 |
| fuller2020enabling | academico | 2026-10-29 |
| jones2020characterising | academico (apenas metadados/abstract) | 2026-10-29 |
| lin2024hdtsurvey | academico | 2026-10-29 |
