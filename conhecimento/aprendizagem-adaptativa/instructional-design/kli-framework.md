---
id: adp.id.kli-framework
titulo: Knowledge-Learning-Instruction (KLI) framework
tipo: framework
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [koedinger2012kli, vanlehn2006behavior]
relacoes:
  - { tipo: parte-de, alvo: adp.id.knowledge-components }
  - { tipo: complementa, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: adp.sr.spacing-and-testing-effects }
  - { tipo: relacionado-a, alvo: adp.adapt.sequencing-policies }
  - { tipo: avaliado-por, alvo: adp.eval.educational-effectiveness }
termos: [KLI framework, knowledge component, learning event, instructional event, assessment event, memory and fluency, induction and refinement, understanding and sense-making, alignment hypothesis, asymmetry hypothesis]
---

# Knowledge-Learning-Instruction (KLI) framework

## Definição e terminologia

O **Knowledge-Learning-Instruction (KLI) framework**, proposto por Koedinger, Corbett e Perfetti (2012), é uma teoria que relaciona três taxonomias coordenadas — tipos de conhecimento, tipos de processos de aprendizagem e tipos de instrução — com o objetivo de aproximar ciência cognitiva e prática educacional ("bridging the science-practice chasm") [F: koedinger2012kli]. O framework organiza a análise em torno de três categorias de eventos: **Learning Events**, **Instructional Events** e **Assessment Events** [F: koedinger2012kli].

Instructional Events e Assessment Events são atividades observáveis, ou mudanças observáveis, no ambiente instrucional, controladas por um instrutor, designer instrucional ou experimentador; Instructional Events visam produzir aprendizagem (causam Learning Events) e podem ser observados em uma aula; Assessment Events envolvem respostas do estudante que são avaliadas — algumas são instrucionais, outras não, e embora costumem ser itens de teste, podem também estar embutidas na própria instrução [F: koedinger2012kli]. Learning Events, por sua vez, são essencialmente mudanças em estados cognitivos e cerebrais que podem ser inferidas a partir de dados, mas não observadas nem controladas diretamente [F: koedinger2012kli]. O framework caracteriza as mudanças de conhecimento resultantes desses Learning Events em termos de Knowledge Components (KCs; ver `adp.id.knowledge-components`), e usa inferências sobre Instructional e Assessment Events observáveis para inferir o não observável (Learning Events e mudanças de KC) [F: koedinger2012kli].

O que o KLI não é: não é um modelo computacional de aluno (como o learner model de `adp.lm.learner-model`), nem um algoritmo de sequenciamento; é uma teoria organizadora que fornece vocabulário e hipóteses testáveis para ligar desenho instrucional a mecanismos de aprendizagem [I].

## Problema que resolve

Koedinger, Corbett e Perfetti observam que há recomendações conflitantes na literatura sobre qual tipo de instrução é ótima, sem critério claro de quando cada uma se aplica — um exemplo de oposição é contrastado no artigo, e os autores propõem hipóteses de como essa oposição pode ser resolvida a partir de diferenças nos tipos de KC envolvidos [F: koedinger2012kli]. O framework resolve a falta de uma linguagem comum que ligue, de forma testável, "que tipo de conhecimento" a "que tipo de processo de aprendizagem" a "que tipo de instrução é eficaz" — sem essa ligação, cada domínio e cada estudo usa sua própria terminologia e os resultados não generalizam.

## Fundamentos e funcionamento

### Os três tipos de processos de aprendizagem (Learning Events)

O framework distingue três classes amplas de processos que produzem mudanças de conhecimento levando a aprendizagem robusta [F: koedinger2012kli]:

1. **Memory and fluency building processes**: a memória é fortalecida continuamente, desde a formação inicial de um KC até cada uso subsequente; opera sobre todo tipo de KC, da associação não-verbal mais simples ao esquema variável-variável verbal mais complexo [F: koedinger2012kli]. A memória melhora com maior frequência de exposição (implicando prática), é mais robusta quando a recuperação (e não o reconhecimento) é exigida (o "testing effect") e quando a prática é distribuída no tempo (o "spacing effect") [F: koedinger2012kli]. Mesmo após o KC já produzir respostas corretas, processos de fluência continuam, via compilação de conhecimento (proceduralização de uma codificação declarativa inicial, com composição de KCs pequenos em um KC maior) e fortalecimento de memória (acesso mais rápido e confiável com uso repetido) [F: koedinger2012kli].

2. **Induction and refinement processes**: modificam KCs, especialmente as condições que controlam sua recuperação e aplicação, adicionando características relevantes ausentes (discriminação) ou removendo características irrelevantes (generalização); são não-verbais, embora a aprendizagem resultante possa ser produzida por eventos verbais [F: koedinger2012kli]. O exemplo dado: a partir de exemplos em que ângulos iguais parecem iguais em um diagrama, um novato em geometria pode induzir o KC "se ângulos parecem iguais, então são iguais" — correto em alguns casos, mas incorreto e carente de refinamento, que pode remover a característica irrelevante ("parecem iguais") ou adicionar uma relevante ("ângulos opostos em retas que se cruzam") [F: koedinger2012kli].

3. **Understanding and sense-making processes**: estratégias de aprendizagem robustas em que o estudante se engaja em pensamento explícito, mediado por linguagem, para criar conhecimento — incluem estratégias de compreensão, autoexplicação e argumentação social; ao contrário da indução e do refinamento, são deliberadas, ocorrendo quando o estudante escolhe se engajar nelas, e são explicitamente apoiadas por linguagem ou símbolos externos [F: koedinger2012kli]. Esses processos podem transformar associações constante-constante em fatos, categorias variável-constante em conceitos, e produções variável-variável em regras — ou, quando focam na justificativa de uma relação, transformar regras em princípios (ver a taxonomia de KCs em `adp.id.knowledge-components`) [F: koedinger2012kli].

Os autores enfatizam que não há mapeamento um-para-um entre esses processos e resultados de aprendizagem robusta: por exemplo, não é o caso de que só sense-making leve a transferência — aprendizagem acelerada futura pode vir de (1) aprender a aprender, (2) adquirir conceitos profundos que facilitam aprendizagem em novo domínio, ou (3) aumentar "espaço cognitivo" por meio de fluência com conhecimento central [F: koedinger2012kli].

### Instructional Events e os três tipos correspondentes de instrução

A taxonomia de instrução segue diretamente a taxonomia de aprendizagem, com três categorias principais: instrução que reforça memória e fluência; instrução que reforça indução e refinamento; e instrução que reforça compreensão e sense-making [F: koedinger2012kli]. Exemplos de princípios instrucionais em cada categoria, do mais simples ao mais complexo [F: koedinger2012kli]:

- **Memória e fluência**: *Spacing and Testing* (retenção de longo prazo é reforçada por intervalos mais longos entre práticas e quando é exigida recuperação ativa) [F: koedinger2012kli]; *Optimized Scheduling* (seleção de instâncias de prática com base em estatísticas prévias e na experiência de cada estudante com cada KC-alvo, derivando matematicamente quando repetir a prática de um KC) [F: koedinger2012kli].
- **Indução e refinamento**: *Timely Feedback* (resposta avaliativa logo após a tentativa do estudante) [F: koedinger2012kli]; *Feature Focusing* (a instrução leva a aprendizagem mais robusta quando guia a atenção do estudante para características válidas ou relevantes dos KCs-alvo — demonstrado, por exemplo, destacando o radical semântico de um caractere chinês ao passar o mouse sobre ele) [F: koedinger2012kli]; *Worked Examples* (estudantes aprendem de forma mais eficiente e robusta quando exemplos resolvidos são intercalados com prática de resolução de problemas, em vez de só resolver problemas) [F: koedinger2012kli].
- **Compreensão e sense-making**: *Prompted Self-Explanation* (incentivar o estudante a explicar para si mesmo partes da instrução produz aprendizagem mais robusta do que não oferecer tais explicações) [F: koedinger2012kli]; *Accountable Talk* (uso pelo professor de "movimentos de fala" que tornam os estudantes responsáveis por conhecimento preciso, raciocínio rigoroso e pela comunidade da sala de aula) [F: koedinger2012kli].

### Dependência entre tipos de conhecimento e instrução adequada: as hipóteses de alinhamento e assimetria

Koedinger, Corbett e Perfetti cruzam uma tabela de KCs (do mais simples ao mais complexo, incluindo exemplos reais como vocabulário chinês, artigos em francês e inglês, regras de álgebra e geometria, princípios de física) com princípios instrucionais testados experimentalmente, marcando onde há evidência de que o princípio melhora a eficiência de aprendizagem robusta para aquele tipo de KC [F: koedinger2012kli]. Dessa análise emergem duas hipóteses concorrentes [F: koedinger2012kli]:

- **Hipótese de alinhamento** (*alignment hypothesis*): a complexidade da instrução deveria estar alinhada com a complexidade do conhecimento-alvo — (1) para conhecimento simples, formas complexas de instrução não são necessárias, e (2) para conhecimento complexo, formas simples não são necessárias [F: koedinger2012kli].
- **Hipótese de assimetria** (*asymmetry hypothesis*): conhecimento simples torna-se embutido em conhecimento mais complexo, de modo que a instrução para KCs complexos pode incluir Instructional Events mais simples, mas a instrução para KCs simples não se beneficiaria de Instructional Events mais complexos [F: koedinger2012kli]. Os autores argumentam que essa segunda hipótese é "mais aproximadamente correta": para aprender uma associação constante-constante arbitrária (um fato), um processo de generalização como a indução de categorias é desnecessário, e para uma associação arbitrária não há estrutura de justificativa que permita regenerar o KC — a re-derivação só funciona para conhecimento com uma racionalização subjacente (conhecimento complexo) [F: koedinger2012kli]. Por outro lado, KCs mais complexos, como aprender artigos do inglês, exigem tanto indução de uma estrutura de categoria quanto memorização dessa estrutura, de modo que métodos de reforço de memória simples (espaçamento, teste, agendamento otimizado) continuam sendo relevantes mesmo para KCs complexos — o que argumenta contra a hipótese de alinhamento [F: koedinger2012kli].

Os autores reconhecem um contra-argumento: métodos instrucionais complexos (accountable talk, autoexplicação) podem atingir indiretamente os mesmos resultados que métodos simples (por exemplo, reforço de memória), de modo que o uso de instrução mais complexa pode não valer o tempo extra que costuma exigir — e enfatizam que toda análise de eficiência instrucional deve considerar o custo de tempo, não só o resultado de aprendizagem [F: koedinger2012kli].

## Algoritmos e modelos relevantes

O framework não prescreve um algoritmo único, mas se apoia em modelos estatísticos de curva de aprendizagem (ver a Figura 2 do artigo, com curvas de tempo de desempenho correto por oportunidade sucessiva, construídas a partir de dados do DataShop) para inferir a complexidade relativa de diferentes KCs [F: koedinger2012kli]. A análise de alinhamento/assimetria é operacionalizada comparando, para cada tipo de KC na taxonomia (ver `adp.id.knowledge-components`), se um princípio instrucional foi experimentalmente demonstrado como eficaz ("+"), sem diferença ("0") ou sem experimento relevante (célula vazia) [F: koedinger2012kli].

## Requisitos e pressupostos

- Decomposição prévia do domínio em KCs identificáveis a partir do desempenho em tarefas relacionadas (ver `adp.id.knowledge-components`) [F: koedinger2012kli].
- Capacidade de observar Instructional Events e Assessment Events; Learning Events e mudanças de KC permanecem inferidos, nunca observados diretamente [F: koedinger2012kli].
- Dados longitudinais suficientes para construir curvas de aprendizagem por KC e comparar efeitos de diferentes Instructional Events sobre o mesmo tipo de KC [I].

## Vantagens e limitações

Vantagens: o framework oferece uma linguagem comum que atravessa domínios (segunda língua, matemática, ciências), permitindo comparar princípios instrucionais testados em contextos muito diferentes [F: koedinger2012kli]; gera hipóteses testáveis e explícitas (alinhamento versus assimetria) em vez de recomendações genéricas por domínio [F: koedinger2012kli].

Limitações: os próprios autores reconhecem que mais pesquisa é necessária para esclarecer os limites de generalidade dos princípios instrucionais em função da complexidade do conhecimento-alvo [F: koedinger2012kli]; a análise de complexidade de KC (condições constantes/variáveis, resposta constante/variável, verbal/não-verbal, com/sem racionalização) é uma aproximação de primeira ordem, declarada como "talvez incompleta" pelos próprios autores [F: koedinger2012kli].

## Alternativas e comparações

| Aspecto | KLI framework | VanLehn (inner loop/outer loop) |
|---|---|---|
| Nível de análise | tipos de conhecimento, aprendizagem e instrução, cruzados [F: koedinger2012kli] | comportamento operacional de sistemas tutores (seleção de tarefa, feedback, avaliação) [F: vanlehn2006behavior] |
| Unidade central | Knowledge Component, Learning Event, Instructional Event, Assessment Event [F: koedinger2012kli] | step, learning event, knowledge component, student model [F: vanlehn2006behavior] |
| Pergunta principal | que tipo de instrução é ótimo para que tipo de conhecimento? [F: koedinger2012kli] | como estruturar os laços de decisão de um tutor? [F: vanlehn2006behavior] |

Os dois frameworks compartilham a noção de Knowledge Component e de Learning Event (VanLehn define learning event como "a construção ou aplicação de um knowledge component" [F: vanlehn2006behavior], consistente com o uso em KLI) [I], mas operam em níveis diferentes: KLI é uma teoria sobre o que torna a instrução eficaz; VanLehn descreve a arquitetura comportamental de um sistema tutor. Os dois são complementares, não concorrentes.

## Métricas e métodos de avaliação

O framework é avaliado empiricamente por experimentos que comparam Instructional Events contrastantes sobre o mesmo KC, medindo ganhos de aprendizagem robusta (retenção de longo prazo e transferência), não apenas desempenho imediato [F: koedinger2012kli]. Não há, no artigo, uma métrica numérica única proposta pelos autores para "robustez" da aprendizagem; o conceito é operacionalizado por desenho experimental (teste de retenção tardio, teste de transferência) em cada estudo citado [I].

## Exemplo técnico independente de domínio

Esquema de decisão para escolher o tipo de Instructional Event a partir da categoria de KC-alvo, seguindo a hipótese de assimetria [F: koedinger2012kli]:

```
escolher_instrucao(kc):
    categoria = classificar_kc(kc)   # ver taxonomia em adp.id.knowledge-components
    se categoria == "constante-constante":       # fato, associação
        usar(Spacing, Testing, Optimized_Scheduling)
    senão se categoria == "variavel-constante":  # categoria, conceito
        usar(Spacing, Testing)                   # memoria ainda necessaria
        usar(Feature_Focusing)                   # induzir a condicao variavel
    senão se categoria in ("variavel-variavel-sem-racionale",
                            "variavel-variavel-com-racionale"):  # regra, principio
        usar(Spacing, Testing)                   # hipotese de assimetria: ainda se aplica
        usar(Worked_Examples, Feature_Focusing)
        se categoria == "com-racionale":
            usar(Prompted_Self_Explanation, Accountable_Talk)
```

## Relações com outros conceitos

Parte de (pressupõe) `adp.id.knowledge-components`: o KLI define formalmente o que é um KC e sua taxonomia. Complementa `adp.lm.learner-model`, pois a granularidade do modelo de aluno (overlay por KC) é a mesma unidade analítica do KLI. Relaciona-se com `adp.sr.spacing-and-testing-effects`, de onde vêm os princípios de memória e fluência citados, e com `adp.adapt.sequencing-policies`, que opera decisões de sequenciamento potencialmente informadas pelas hipóteses de alinhamento/assimetria. É avaliado por `adp.eval.educational-effectiveness`.

## Lacunas e questões abertas

- O artigo usa o termo "Assessment Event" de forma mais ampla do que "item de teste" (pode estar embutido na instrução) [F: koedinger2012kli], mas o texto consultado não detalha critérios operacionais para distinguir, na prática, um Assessment Event embutido de um Instructional Event comum — ponto que caberia aprofundar com a literatura de stealth assessment (fora do escopo de atribuição deste documento).
- A oposição entre hipótese de alinhamento e hipótese de assimetria é apresentada como ainda não resolvida pelos próprios autores, que pedem mais pesquisa para delimitar os limites de generalidade [F: koedinger2012kli]; não localizamos, nesta pesquisa, trabalho posterior que resolva a disputa.
- Não verificamos a versão publicada final na Wiley (retornou HTTP 403 na sessão); o documento usa a "authors' final version" depositada no Figshare, que traz a paginação e o DOI da versão publicada impressos no próprio PDF [F: koedinger2012kli].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| koedinger2012kli | academico | 2026-10-29 |
| vanlehn2006behavior | academico | 2026-10-29 |
