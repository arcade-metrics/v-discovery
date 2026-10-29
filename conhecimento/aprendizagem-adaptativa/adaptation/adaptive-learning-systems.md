---
id: adp.adapt.adaptive-learning-systems
titulo: Aprendizagem adaptativa (adaptive learning systems)
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [vanlehn2006behavior, brusilovsky2001adaptive, corbett1995kt, pelanek2017overview, martin2020adaptive]
relacoes:
  - { tipo: depende-de, alvo: adp.lm.learner-model }
  - { tipo: depende-de, alvo: adp.id.knowledge-components }
  - { tipo: complementa, alvo: adp.adapt.sequencing-policies }
  - { tipo: relacionado-a, alvo: adp.kt.bayesian-knowledge-tracing }
  - { tipo: relacionado-a, alvo: adp.lm.open-learner-model }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: relacionado-a, alvo: adp.dt.learning-digital-twin }
  - { tipo: avaliado-por, alvo: adp.eval.educational-effectiveness }
termos: [adaptive learning, adaptivity, adaptability, outer loop, inner loop, student model, macroadaptation, mastery learning, adaptive presentation, adaptive navigation support]
---

# Aprendizagem adaptativa (adaptive learning systems)

## Definição e terminologia

Um sistema de aprendizagem adaptativa é um sistema que constrói um modelo das características, do conhecimento ou dos objetivos de cada usuário e usa esse modelo para adaptar algum aspecto da experiência a esse usuário específico, em vez de apresentar o mesmo conteúdo e a mesma sequência a todos [F: brusilovsky2001adaptive]. Essa definição, formulada originalmente para hipermídia adaptativa em geral, aplica-se diretamente ao caso educacional: hipermídia educacional adaptativa foi, historicamente, a primeira e mais numerosa família de sistemas adaptativos a surgir, precisamente porque estudantes diferentes têm conhecimento prévio, objetivos e preferências diferentes, e um currículo único raramente serve a todos igualmente bem [F: brusilovsky2001adaptive].

VanLehn descreve o mesmo fenômeno do ponto de vista dos sistemas tutores: um sistema tutor se comporta *como se* tivesse dois laços de controle — um laço externo (*outer loop*), que executa uma vez por tarefa e decide qual tarefa o aluno deve fazer a seguir, e um laço interno (*inner loop*), que executa uma vez por passo dentro da tarefa e é responsável por obter os passos corretos do aluno e por ajudá-lo quando ele erra ou pede ajuda [F: vanlehn2006behavior]. Sistemas sem laço interno — que apenas atribuem uma tarefa, coletam a resposta final e avaliam — são chamados de Computer-Aided Instruction (CAI), Computer-Based Training (CBT) ou Web-Based Homework (WBH); sistemas com laço interno são chamados de Intelligent Tutoring Systems (ITS) [F: vanlehn2006behavior]. Os termos "laço externo"/"laço interno" descrevem o comportamento observável do sistema, não necessariamente sua arquitetura de software [F: vanlehn2006behavior].

**O que não é.** Adaptividade não é o mesmo que adaptabilidade (*adaptability*). Brusilovsky reserva "adaptativo" para sistemas em que é o próprio sistema que decide a adaptação a partir de um modelo de usuário, e "adaptável" para sistemas em que é o usuário quem ajusta manualmente a apresentação ou a navegação — por exemplo, páginas personalizadas como portais configuráveis manualmente ou organizadores de favoritos são tipicamente adaptáveis, mas não adaptativos; só uma minoria desses sistemas de gerenciamento de favoritos chega a ser adaptativa de fato [F: brusilovsky2001adaptive]. Essa distinção é o que separa aprendizagem adaptativa de personalização superficial: uma interface que deixa o aluno escolher cor, fonte ou ordem de módulos é adaptável, mas só passa a ser adaptativa quando o próprio sistema infere algo sobre o aluno (conhecimento, objetivo, preferência) e usa essa inferência para mudar o que é mostrado, dirigido pelo sistema e não pela escolha explícita do usuário [I, a partir de F: brusilovsky2001adaptive].

Adaptividade também não é sinônimo de recomendação ad hoc ou de "trilhas" estáticas rotuladas por nível: exige um modelo de usuário atualizado a partir da interação e uma lógica de adaptação que o consome continuamente, não uma segmentação fixa decidida uma vez no design [I].

## Problema que resolve

Instrução individualizada — um tutor humano ajustando ritmo, conteúdo e explicação a cada aluno — é difícil de escalar. VanLehn enquadra o papel do laço externo como decidir qual tarefa ajudará o aluno a aprender, dado tudo o que o sistema já infere sobre ele; o papel do laço interno é obter os passos certos e ajudar no momento do erro [F: vanlehn2006behavior]. Sem essa adaptação, um currículo único deixa alguns alunos praticando o que já sabem e outros avançando sem ter dominado pré-requisitos — o problema que a hipermídia educacional adaptativa também busca resolver, ajustando a apresentação e os links de navegação ao conhecimento e aos objetivos de cada estudante [F: brusilovsky2001adaptive].

## Fundamentos e funcionamento

### O que pode ser adaptado

Brusilovsky distingue dois níveis de adaptação em hipermídia: adaptação em nível de conteúdo (*adaptive presentation*) e adaptação em nível de links (*adaptive navigation support*) [F: brusilovsky2001adaptive]. Adaptive presentation se subdivide em adaptação de texto (inserir/remover fragmentos, *stretchtext*, alterar ou reordenar fragmentos, atenuar fragmentos — todas formas de "canned text adaptation") e adaptação de multimídia e de modalidade, escolhendo entre texto, áudio, vídeo ou animação conforme preferências, habilidades e estilo de aprendizagem do usuário [F: brusilovsky2001adaptive]. Adaptive navigation support se subdivide em ocultar, ordenar, anotar ou guiar diretamente os links, além de adaptar mapas de hipertexto — e, mais recentemente, em gerar novos links não autorados, não apenas adaptar os já existentes [F: brusilovsky2001adaptive].

Essa taxonomia de "o que pode ser adaptado" mapeia para a linguagem mais comum em sistemas tutores: adaptação de **conteúdo** (qual material, em que modalidade), de **sequência** (que tarefa ou link vem a seguir — o correspondente educacional de adaptive navigation support, tratado em `adp.adapt.sequencing-policies`), de **feedback** (o que o laço interno diz ao aluno a cada passo) e de **apresentação** (como a informação é mostrada). VanLehn documenta a adaptação de feedback como responsabilidade central do laço interno: sistemas variam desde dar feedback imediato a cada passo (Algebra Cognitive Tutor) até não dar feedback nem dicas enquanto o aluno resolve, revisando só ao final (SQL-Tutor) [F: vanlehn2006behavior].

### Os quatro desenhos de laço externo

VanLehn identifica quatro métodos comuns, em ordem crescente de complexidade, para o laço externo selecionar a próxima tarefa [F: vanlehn2006behavior]:

1. **Menu**: o próprio aluno escolhe a tarefa seguinte em um menu (ex.: Andes, usado como apoio de lição de casa junto com aulas presenciais tradicionais) [F: vanlehn2006behavior].
2. **Sequência fixa**: o sistema atribui tarefas em uma ordem predeterminada (ex.: AutoTutor), garantindo que o aluno termine uma tarefa antes de avançar, o que aumenta a chance de ter dominado pré-requisitos [F: vanlehn2006behavior].
3. **Mastery learning**: o currículo é estruturado em unidades ou níveis de dificuldade; o sistema continua atribuindo tarefas da unidade corrente até que o aluno domine o conhecimento da unidade, só então liberando a próxima — por isso alunos diferentes terminam o currículo tendo feito números diferentes de tarefas [F: vanlehn2006behavior]. Esse desenho é mais usado em cursos autoguiados (*self-paced*) e raramente em cursos com ritmo de turma, onde instrutores precisam manter os alunos juntos [F: vanlehn2006behavior].
4. **Macroadaptação**: para cada tarefa possível, o sistema sabe quais componentes de conhecimento ela exercita; para cada componente, mantém uma estimativa do domínio do aluno; a tarefa seguinte é escolhida pelo recobrimento entre os componentes da tarefa e os componentes já dominados (e, em variantes mais ricas, também por componentes incorretos — concepções equivocadas — ou por traços estáveis como estilo de aprendizagem) [F: vanlehn2006behavior]. O Algebra Cognitive Tutor usa esse desenho [F: vanlehn2006behavior].

Mastery learning como pedagogia tem origem fora da computação: Bloom a propôs como estratégia de instrução em que a maior parte dos alunos pode atingir o domínio do conteúdo se variáveis como tempo de instrução e qualidade do ensino forem ajustadas a cada aluno, em vez de fixas [F: bloom1968mastery, metadados]. VanLehn observa que mastery learning, como desenho de laço externo, exige que o sistema tenha alguma forma de avaliar o domínio do aluno sobre o conteúdo da unidade — idealmente feita pelo próprio laço interno durante a prática, ou, quando isso não é viável, por tarefas de avaliação dedicadas [F: vanlehn2006behavior].

### Arquitetura: modelo de domínio, modelo de aluno, modelo pedagógico

Para que o laço externo funcione ao longo de múltiplas tarefas e sessões, a informação sobre o aluno precisa ser persistida; essa estrutura persistente é chamada, por convenção da área, de **modelo de aluno** (*student model*), ainda que o termo seja usado para uma coleção heterogênea de dados: desde um simples ponteiro para a próxima tarefa de uma lista (laço de sequência fixa) até pares atributo-valor — componentes de conhecimento, estilos, preferências — no caso macroadaptativo, podendo incluir também notas padronizadas, tempo gasto, número de erros e pedidos de ajuda [F: vanlehn2006behavior]. O documento `adp.lm.learner-model` aprofunda essa estrutura. O conteúdo do que é adaptado (tarefas, textos, explicações) e a lógica de que par tarefa-componente existe formam o que a literatura chama de **modelo de domínio** — em VanLehn, o conjunto de tarefas disponíveis e os componentes de conhecimento que cada uma exercita [F: vanlehn2006behavior]; em Corbett e Anderson, o "modelo de aluno ideal" (*ideal student model*), um modelo executável do conhecimento procedural do domínio contra o qual o aluno é comparado por *overlay* [F: corbett1995kt]. A lógica de decisão que consome o modelo de aluno e o modelo de domínio para escolher a próxima tarefa ou intervenção — o laço externo em si — corresponde ao que outras tradições da área chamam de **modelo pedagógico** ou **modelo instrucional**.

## Algoritmos e modelos relevantes

- **Overlay model**: o modelo do aluno é uma sobreposição do modelo de domínio ideal — para cada regra ou componente do domínio, uma estimativa de que o aluno já o possui [F: corbett1995kt]. É a base de BKT (`adp.kt.bayesian-knowledge-tracing`) e de boa parte dos modelos macroadaptativos descritos por VanLehn.
- **Modelos probabilísticos de estado do aluno** (BKT, modelos logísticos): fornecem a estimativa contínua de domínio por componente que alimenta tanto mastery learning quanto macroadaptação; ver `adp.kt.bayesian-knowledge-tracing` e `adp.kt.logistic-models` para o funcionamento interno [F: pelanek2017overview].
- **Seleção por modo** (*fading the scaffolding*): além de escolher a tarefa, alguns laços externos escolhem o modo de apoio — demonstração completa, dica antes de cada passo, ou resolução livre — tipicamente começando com mais apoio e reduzindo-o gradualmente conforme o aluno avança [F: vanlehn2006behavior].
- **Planejamento com replanejamento**: desenhos mais sofisticados, pouco comuns na prática, planejam uma sequência inteira de tarefas a partir do modelo de aluno e a revisam ao detectar uma concepção equivocada grave a meio da sequência [F: vanlehn2006behavior].

## Requisitos e pressupostos

- Um conjunto suficientemente rico de tarefas para o laço externo escolher: VanLehn estima a necessidade de centenas de problemas por curso, e mais ainda quando o desenho é mastery learning ou macroadaptativo, pois alunos percorrem quantidades diferentes de tarefas [F: vanlehn2006behavior].
- Um modelo de domínio que associe tarefas a componentes de conhecimento, exigido por mastery learning e sobretudo por macroadaptação [F: vanlehn2006behavior]; ver `adp.id.knowledge-components`.
- Um modelo de aluno persistente e atualizável a cada oportunidade, não um rótulo estático definido uma vez [F: vanlehn2006behavior] [F: corbett1995kt].
- Para mastery learning especificamente, alguma forma de avaliação do domínio, feita pelo laço interno ou por tarefas de teste dedicadas [F: vanlehn2006behavior].
- Ritmo autoguiado (self-paced): mastery learning e macroadaptação assumem que alunos podem avançar em ritmos diferentes; cursos com ritmo de turma limitam o uso desses desenhos na prática [F: vanlehn2006behavior].

## Vantagens e limitações

Vantagens: tarefas mais compatíveis com o nível atual do aluno tendem a reduzir tempo gasto em conteúdo já dominado e a evitar avanço sem pré-requisitos [F: vanlehn2006behavior]; hipermídia adaptativa reduz a sobrecarga de navegação ao esconder, anotar ou reordenar links irrelevantes para o objetivo e o conhecimento do usuário [F: brusilovsky2001adaptive].

Limitações: macroadaptação e mastery learning exigem bancos de tarefas muito maiores que sequências fixas, e tarefas "gastam-se" quando alunos compartilham informação entre si [F: vanlehn2006behavior]; mastery learning é difícil de operar em cursos com ritmo de turma [F: vanlehn2006behavior]; a revisão sistemática de Martin et al. sobre pesquisa em adaptive learning entre 2009 e 2018 está registrada aqui apenas por metadados — o resumo indica 61 artigos analisados, estilo de aprendizagem como característica do aluno mais estudada como fonte de adaptação, e feedback e navegação adaptativos como alvos mais investigados, mas essas contagens não foram verificadas no texto completo do artigo nesta sessão [F: martin2020adaptive, metadados].

## Alternativas e comparações

| Desenho de laço externo | Unidade de decisão | Exige modelo de componentes? | Ritmo adequado |
|---|---|---|---|
| Menu | o aluno escolhe | não | qualquer |
| Sequência fixa | ordem predeterminada | não | turma ou individual |
| Mastery learning | unidade/nível de dificuldade | parcialmente (por unidade) | self-paced |
| Macroadaptação | componente de conhecimento | sim | self-paced |

Fonte da tabela: [F: vanlehn2006behavior]. A adaptação de conteúdo e de navegação em hipermídia (adaptive presentation / adaptive navigation support) é um recorte ortogonal a essa tabela: qualquer um dos quatro desenhos de laço externo pode, em princípio, ser combinado com adaptação de apresentação [I].

## Métricas e métodos de avaliação

A literatura revisada por Doroudi, Aleven e Brunskill usa predominantemente desempenho em pós-teste e tempo até o domínio (*time to mastery*) como variáveis de desfecho para avaliar se uma política adaptativa de sequenciamento supera uma linha de base [F: vanlehn2006behavior, para a noção de mastery como critério; ver `adp.adapt.sequencing-policies` para o detalhamento dessas métricas e da evidência empírica]. Avaliação de modelos de estado do aluno em si (precisão preditiva via AUC, RMSE) é tratada em `adp.eval.predictive-metrics` e não se confunde com avaliação de efetividade pedagógica do sistema adaptativo como um todo, tratada em `adp.eval.educational-effectiveness`.

## Exemplo técnico independente de domínio

Esqueleto do laço externo, parametrizável pelos quatro desenhos de VanLehn [F: vanlehn2006behavior]:

```
estado_aluno: mapa componente -> estimativa_dominio   # o "modelo de aluno"
banco_tarefas: lista de (tarefa, componentes_exercitados)

escolher_proxima_tarefa(desenho, estado_aluno, banco_tarefas, historico):
    caso desenho == MENU:
        retornar tarefa escolhida pelo usuario em banco_tarefas
    caso desenho == SEQUENCIA_FIXA:
        retornar proxima tarefa nao feita na ordem predefinida
    caso desenho == MASTERY_LEARNING:
        unidade = unidade_corrente(historico)
        se todo componente de unidade tem estado_aluno[c] >= limiar:
            avancar para proxima unidade
        retornar tarefa nao feita da unidade corrente
    caso desenho == MACROADAPTACAO:
        candidatas = tarefas cujos componentes tem alguma lacuna
                     (poucos componentes com estado_aluno[c] < limiar)
        retornar a candidata com melhor recobrimento
               entre componentes dominados e nao dominados

apos cada tarefa resolvida:
    para cada componente c exercitado na tarefa:
        estado_aluno[c] = atualizar(estado_aluno[c], resposta)   # ex.: BKT
```

O laço interno (não detalhado aqui) intercepta cada passo dentro da tarefa, decide se dá feedback imediato, dica ou nenhuma intervenção, e é o que alimenta `atualizar(...)` com evidência de granularidade fina quando disponível [F: vanlehn2006behavior].

## Relações com outros conceitos

Depende de um modelo de aluno (`adp.lm.learner-model`) persistente e de uma decomposição do domínio em componentes de conhecimento (`adp.id.knowledge-components`) para os desenhos de mastery learning e macroadaptação. Complementa `adp.adapt.sequencing-policies`, que aprofunda especificamente as políticas de seleção e ordenação de atividades, incluindo a formulação como problema de decisão sequencial. Relaciona-se com `adp.kt.bayesian-knowledge-tracing`, cujo critério de mastery (probabilidade de conhecimento ≥ 0,95) é o exemplo mais citado de avaliação de domínio usada por um laço externo de mastery learning [F: corbett1995kt]. Relaciona-se também com `adp.lm.open-learner-model` (exposição do modelo de aluno ao próprio aluno) e com `adp.irt.item-response-theory` (outra forma de modelar a relação aluno-item usada em adaptação). É avaliado, quanto a efetividade educacional, pelos protocolos de `adp.eval.educational-effectiveness`.

## Lacunas e questões abertas

- Aleven, McLaughlin, Glenn e Koedinger (2017), capítulo "Instruction based on adaptive learning technologies" no Handbook of Research on Learning and Instruction, é citado com frequência como referência central para a distinção entre adaptar a diferenças e adaptar a semelhanças entre alunos (a "Adaptivity Grid" com laços de design, tarefa e passo). Não foi possível abrir uma cópia do capítulo nesta sessão (paywall da Taylor & Francis); não é citado como [F] e fica como lacuna para verificação futura.
- Kabudi, Pappas e Olsen (2021), mapeamento sistemático sobre sistemas de aprendizagem adaptativa com IA, foi localizado mas todas as tentativas de baixar o texto completo (ScienceDirect, CORE, repositório da Universidade de Agder) retornaram erro 403 nesta sessão; não citado.
- Martin et al. (2020) está na bibliografia apenas por metadados (resumo do registro ERIC); os números específicos do resumo (61 artigos, estilo de aprendizagem como característica mais estudada) são citados aqui com a ressalva explícita de não terem sido verificados no corpo do artigo.
- VanLehn (2006) não discute hipermídia adaptativa, e Brusilovsky (2001) não discute mastery learning ou macroadaptação; a correspondência traçada aqui entre as duas taxonomias (conteúdo/sequência/feedback/apresentação de um lado, presentation/navigation do outro) é uma síntese do autor deste documento, não uma equivalência estabelecida por nenhuma das duas fontes [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| vanlehn2006behavior | academico | 2026-10-29 |
| brusilovsky2001adaptive | academico | 2026-10-29 |
| corbett1995kt | academico | 2026-10-29 |
| pelanek2017overview | academico | 2026-10-29 |
| bloom1968mastery | academico (apenas metadados) | 2026-10-29 |
| martin2020adaptive | academico (apenas metadados) | 2026-10-29 |
