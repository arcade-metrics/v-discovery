---
id: adp.lm.open-learner-model
titulo: Open learner model
tipo: conceito
dominio: aprendizagem-adaptativa
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [bullkay2016smili, bullkay2007smili, bull2020olm, vanlehn2006behavior]
relacoes:
  - { tipo: parte-de, alvo: adp.lm.learner-model }
  - { tipo: complementa, alvo: adp.lm.learner-model }
  - { tipo: alternativa-a, alvo: adp.dt.learning-digital-twin }
  - { tipo: relacionado-a, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: avaliado-por, alvo: adp.eval.educational-effectiveness }
termos: [open learner model, OLM, SMILI, skill meter, negotiated learner model, inspectable learner model, editable learner model, learning analytics dashboard]
---

# Open learner model

## Definição e terminologia

Um *open learner model* (OLM) é um learner model (ver `adp.lm.learner-model`) que o sistema expõe ao usuário — o próprio aprendiz, professores, colegas e/ou outros interessados no processo educacional — em uma forma compreensível por humanos, em vez de exibir regras internas ou representações complexas de conhecimento [F: bullkay2016smili]. Em princípio, qualquer tipo de modelo de aluno pode ser aberto, inclusive os inferidos por redes bayesianas, mapeamento conceitual, modelagem baseada em restrições (constraint-based) e algoritmos ponderados mais simples [F: bullkay2016smili]. O que distingue um OLM de um modelo fechado é exatamente essa exposição: "modelos fechados não exibem nenhuma informação ao usuário final, embora possam compartilhar dados com outros sistemas" [F: bullkay2016smili].

O termo consolidado na literatura é o framework **SMILI☺** (*Student Models that Invite the Learner In*), criado por Bull e Kay em 2007 para descrever, comparar e criticar OLMs de forma sistemática [F: bullkay2007smili, metadados; F: bullkay2016smili]. Uma revisão de 2016 pelos mesmos autores observa que o framework acabou servindo a um papel mais amplo do que o previsto: não foi usado como ferramenta de comparação sistemática, mas passou a moldar a própria definição do que é um OLM e a informar seu design [F: bullkay2016smili]. O que um OLM não é: não é um relatório estático de notas (isso seria mais próximo de um boletim) nem, necessariamente, um dashboard de learning analytics — a diferença está no propósito de suportar ação do próprio usuário sobre seu processo de aprendizagem, discutida abaixo.

## Problema que resolve

Modelos de aluno tradicionais são internos ao sistema tutor e usados só para decidir o que fazer a seguir (ver o outer loop em `adp.lm.learner-model`) [F: vanlehn2006behavior]. Isso deixa o aprendiz (e o professor) sem acesso ao que o sistema "pensa" que eles sabem. Abrir o modelo resolve um problema de opacidade: sem visibilidade, o aprendiz não pode planejar seu estudo, verificar se o sistema está certo, ou negociar uma correção. OLMs de várias naturezas têm demonstrado ganhos de aprendizagem significativos [F: bullkay2016smili].

## Fundamentos e funcionamento

### O framework SMILI original (2007)

O framework original respondia a cinco perguntas sobre um OLM, com respostas livres para as duas primeiras e tabelas-modelo para as três últimas [F: bullkay2016smili]:

1. **Contexto**: como o OLM se encaixa na interação geral? Quão central é na interface?
2. Como foi avaliado?
3. **O QUE** está aberto?
4. **COMO** é apresentado?
5. **QUEM** controla o acesso?

Para WHAT, HOW e WHO, as colunas da tabela eram os **propósitos** de abrir o modelo: melhorar a acurácia do modelo; apoiar processos metacognitivos de planejamento, monitoramento e reflexão; facilitar colaboração ou competição; facilitar navegação; respeitar o direito do aprendiz de acessar e controlar seus dados pessoais e sua confiança no modelo; e usar o modelo como avaliação do aprendiz [F: bullkay2016smili]. As linhas eram elementos de cada pergunta — por exemplo, para WHAT, a extensão do modelo acessível (completo ou parcial) [F: bullkay2016smili]. Em geral, considerava-se importante que o acesso ao modelo completo fosse relevante para o direito de acesso a dados, controle e confiança; para os demais propósitos, acesso parcial (dados selecionados) era suficiente — exceto quando o modelo era usado como avaliação do aprendiz, caso em que a abertura não era considerada essencial, salvo em avaliação formativa [F: bullkay2016smili].

### Propósitos de abrir o modelo

Os propósitos listados acima funcionam como o eixo central do framework. Entre eles, dois são citados com mais detalhe:

- **Reflexão, planejamento e monitoramento (metacognição)**: desde a mudança de "student model" para "learner model", o papel do modelo passou de componente interno de um sistema de ensino a "cidadão de primeira classe", com valor próprio fora de qualquer sistema de ensino específico — essa mudança de papel habilitou o OLM como fonte importante de informação para estimular aprendizagem autorregulada e habilidades metacognitivas, relevante tanto para um domínio específico quanto para o desenvolvimento geral de abordagens de aprendizagem profunda [F: bullkay2016smili].
- **Confiança**: ligada à capacidade do usuário de examinar e, em alguns desenhos, contestar o modelo.

### Formas de apresentação e manutenção

Bull e Kay distinguem dois eixos de design: **como** o modelo é apresentado e **como** é mantido [F: bullkay2016smili].

Sobre apresentação, exemplos citados incluem *skill meters* simples, usados por um professor para acompanhar o progresso de grupos em sala de aula [F: bullkay2016smili]; mapas conceituais; animações do código de um aprendiz ao lado do código de um especialista, para destacar misconceptions [F: bullkay2016smili]; e, no sistema Next-TELL, múltiplas visualizações do mesmo modelo subjacente — skill meters, tabela, treemap, rede de competências e nuvem de palavras — selecionáveis pelo usuário [F: bullkay2016smili]. Dados de log de uso em três escolas mostraram diferenças reais no uso relativo das visualizações entre aprendizes e professores, embora os dados não expliquem por que cada visualização foi escolhida [F: bullkay2016smili]. Cada forma tem trade-offs: o treemap é útil para modelos grandes e hierárquicos, mas dificulta comparar competências de partes diferentes da árvore; tabela e skill meters exigem rolagem em modelos grandes; a rede dá visão geral em pouco espaço, mas pode ser difícil de ler; a nuvem de palavras mostra rapidamente extremos (pontos fortes e fracos), mas dificulta ver competências intermediárias [F: bullkay2016smili].

Sobre manutenção, há um continuum entre controle do sistema e controle do usuário [F: bullkay2016smili]:
- **Inspectable** (só visualização): o controle do conteúdo é inteiramente do sistema.
- **Editável**: o aprendiz pode alterar diretamente o conteúdo do modelo, sem contestação do sistema.
- **Com adição de evidência**: o usuário contribui dados adicionais, considerados pelo sistema junto com outras informações.
- **Negociado**: usuário e sistema buscam concordar sobre a representação por meio de alguma forma de discussão, com as mesmas ações disponíveis para ambas as partes [F: bullkay2016smili].
- **Persuasão**: o usuário pode contestar o modelo, mas precisa demonstrar seu novo nível de conhecimento (por exemplo, respondendo questões); o sistema mantém o controle e só atualiza o modelo se for "persuadido com sucesso" [F: bullkay2016smili].

### A revisão de 2016: mudanças desde o framework original

Bull e Kay identificam várias mudanças no cenário desde 2007 que motivaram a revisão do SMILI [F: bullkay2016smili]:

- Emergência dos campos de Learning Analytics (LA), Learning at Scale (L@S), Educational Data Mining (EDM) e Quantified Self (QS), com crescimento de volume de dados de aprendizagem muito além do previsto originalmente [F: bullkay2016smili].
- Mudança de papel do modelo: de componente embutido em um sistema de ensino único para serviço de modelo de aluno independente e reutilizável por várias aplicações, inclusive agregando dados de múltiplas fontes externas [F: bullkay2016smili].
- Expansão do leque de interessados: além de aprendiz, professor e colegas (e o genérico "outros" do framework original, que já cobria pais), a origem institucional da Learning/Academic Analytics trouxe foco em gestores escolares e formuladores de política, e o Educational Data Mining trouxe o pesquisador educacional como novo interessado em dados de aprendizagem [F: bullkay2016smili].
- Novas tecnologias de captura e apresentação: tabletops interativos combinados com Kinect e microfones direcionais para modelar colaboração em grupo [F: bullkay2016smili]; robôs táteis físicos que ajudam o aprendiz a usar seus skill meters em sala de aula [F: bullkay2016smili]; sensores de rastreamento ocular e de emoção [F: bullkay2016smili].
- Barateamento do armazenamento (Lei de Moore): modelos antigos, limitados por recursos computacionais modestos, mantinham tipicamente apenas um subconjunto comprimido de dados, muitas vezes restrito à sessão corrente; a computação em nuvem tornou viável manter modelos muito grandes ao longo de toda a vida de aprendizagem do usuário [F: bullkay2016smili].

A revisão apresenta duas versões atualizadas do framework — uma simplificada e uma que preserva a complexidade total da versão original — ambas com categorias adicionais que podem ser aplicadas, omitidas ou substituídas conforme o caso [F: bullkay2016smili].

### Evidências de efeito

Bull e Kay afirmam que "OLMs de vários tipos demonstraram ganhos de aprendizagem significativos", citando como exemplos trabalhos sobre tutores baseados em restrições e tutores cognitivos, entre outros [F: bullkay2016smili]. O artigo não detalha magnitudes de efeito nem protocolos experimentais desses estudos citados; a avaliação rigorosa de efetividade é tratada em `adp.eval.educational-effectiveness`.

## Requisitos e pressupostos

- Um learner model subjacente capaz de ser traduzido para uma representação compreensível por humanos; modelos complexos e detalhados (model tracing, constraint-based) colocam o desafio de que não é claro se — ou como — mostrar toda sua extensão de forma significativa ao aprendiz [F: bullkay2016smili].
- Definição prévia do(s) propósito(s) de abertura, pois a forma de apresentação apropriada depende do propósito, do público-alvo, do contexto de aprendizagem e das tarefas a realizar [F: bullkay2016smili].
- Para formas negociadas ou de persuasão, um mecanismo de diálogo ou de avaliação que decida quando o modelo deve ser atualizado [F: bullkay2016smili].

## Vantagens e limitações

Vantagens: suporte a reflexão e autorregulação; possibilidade de corrigir erros do modelo via negociação ou edição; reuso do modelo por múltiplas aplicações quando implementado como serviço independente [F: bullkay2016smili].

Limitações: modelos cognitivamente complexos (model tracing, constraint-based) são difíceis de expor de forma útil ao aprendiz [F: bullkay2016smili]; grandes repositórios de dados de LMS e MOOCs atuais são estruturados em torno dos recursos de aprendizagem, não como modelo do conhecimento do aprendiz, o que limita seu potencial para mineração educacional e para servir de base a um OLM [F: bullkay2016smili]; o próprio framework SMILI, originalmente pensado para comparação sistemática entre sistemas, não foi de fato usado dessa forma pela comunidade [F: bullkay2016smili].

## Alternativas e comparações

| Aspecto | OLM inspectable | OLM editável | OLM negociado | OLM por persuasão |
|---|---|---|---|---|
| Quem controla o conteúdo | sistema [F: bullkay2016smili] | aprendiz [F: bullkay2016smili] | compartilhado, mesmas ações para ambas as partes [F: bullkay2016smili] | sistema, mediante prova do aprendiz [F: bullkay2016smili] |
| Mecanismo de mudança | nenhum (só visualização) | edição direta | discussão estruturada | resposta a questões de avaliação |
| Risco principal | modelo pode ficar desatualizado | aprendiz pode inserir dado incorreto sem checagem | custo de processo de negociação | pode não refletir conhecimento tácito não verbalizável |

Comparado a um *learning analytics dashboard* institucional, o OLM tende a ter como consumidor primário o próprio aprendiz e seu propósito declarado inclui metacognição e confiança, ao passo que os dashboards de LA nasceram com foco institucional (por exemplo, identificar alunos em risco) [F: bullkay2016smili]. Dashboards de learning analytics também levantam a pergunta geral de "o que deveria ser visualizado", pergunta que a comunidade de Learning Analytics discute de forma análoga ao OLM [F: bullkay2016smili]. A relação com `adp.dt.learning-digital-twin` fica registrada como `alternativa-a`: ambos propõem alguma forma de representação do aprendiz voltada a um usuário humano, mas partem de linhagens conceituais diferentes (framework de interface para modelo de aluno versus metáfora de réplica computacional da pessoa) [I].

## Métricas e métodos de avaliação

O framework original dedicava uma das cinco perguntas centrais a "como foi avaliado", pedindo uma visão geral das avaliações conduzidas e da evidência coletada sobre a efetividade do OLM [F: bullkay2016smili]. Não há, no material revisado, um conjunto único de métricas quantitativas padronizadas para OLMs; a avaliação é reportada por estudo (ganhos de aprendizagem pré/pós, uso observado em log, estudos de campo "in the wild") [F: bullkay2016smili]. Ver `adp.eval.evaluation-protocols` para protocolos gerais de avaliação no domínio.

## Exemplo técnico independente de domínio

Estrutura mínima de dados para um OLM com os dois eixos — apresentação e controle de acesso — tratados de forma independente do learner model subjacente:

```
olm_view(modelo, usuario, proposito):
    dados = selecionar_extensao(modelo, proposito)      # completo ou parcial
    forma = escolher_apresentacao(usuario.preferencia)  # skill meter, treemap, rede, nuvem...
    renderizar(dados, forma)

olm_update(modelo, usuario, mudanca_proposta, modo):
    caso modo de
        INSPECTABLE:  rejeitar(mudanca_proposta)
        EDITAVEL:     aplicar(modelo, mudanca_proposta)
        NEGOCIADO:    iniciar_dialogo(usuario, modelo, mudanca_proposta)
        PERSUASAO:    evidencia = solicitar_prova(usuario)
                      se avaliar(evidencia) >= limiar:
                          aplicar(modelo, mudanca_proposta)
```

## Relações com outros conceitos

Parte de e complementa `adp.lm.learner-model`: todo OLM pressupõe um learner model subjacente, e abrir o modelo é uma forma de uso complementar à sua função interna de adaptação. Relaciona-se com `adp.adapt.adaptive-learning-systems` porque o mesmo modelo pode alimentar simultaneamente decisões automáticas (outer loop) e a visualização para o usuário. É alternativa, na linhagem conceitual, a `adp.dt.learning-digital-twin`. É avaliado, em termos de impacto educacional, por `adp.eval.educational-effectiveness`.

## Lacunas e questões abertas

- O artigo original de Bull e Kay (2007) foi verificado apenas por metadados nesta pesquisa: a página do DOI (IOS Press) e o espelho em CORE retornaram HTTP 403 na sessão; o conteúdo detalhado das tabelas 2, 3 e 4 do framework original (elementos linha a linha) foi descrito aqui apenas via o resumo que a revisão de 2016 faz dele, não pela leitura direta.
- Bull (2020), "There are Open Learner Models About!" (IEEE TLT), foi verificado apenas por metadados (IEEE exige autenticação; nenhuma cópia aberta localizada via OpenAlex); não foi possível incorporar sua visão mais recente sobre o estado do campo.
- Não encontramos, nas fontes abertas, uma meta-análise quantitativa do efeito de OLMs sobre aprendizagem (apenas a afirmação qualitativa de Bull e Kay de que "ganhos significativos" foram demonstrados, com exemplos pontuais) [F: bullkay2016smili].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| bullkay2016smili | academico | 2026-10-29 |
| bullkay2007smili | academico (apenas metadados) | 2026-10-29 |
| bull2020olm | academico (apenas metadados) | 2026-10-29 |
| vanlehn2006behavior | academico | 2026-10-29 |
