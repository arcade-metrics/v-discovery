---
revisao: rodada 1
lente: coerência com o projeto (vuoo.md, PIPE-TC Fase 2; ciatec.md, CCD)
material: produtos/vuoo-linguagem/ (00 a 05 + vuoo-linguagem.html)
data: 2026-10-27
postura: adversarial (perspectiva CIATec / avaliador FAPESP PIPE-TC)
---

# Revisão · Rodada 1 · Coerência com o projeto

## Veredito curto

O estudo é bom como linguagem de interface. Como peça de um projeto PIPE-TC com critérios de passagem psicométricos, ele tem quatro problemas que um avaliador acharia na primeira leitura. Primeiro, descreve o A/B do PP3 de um jeito diferente do que está na proposta. Segundo, os cinco microjogos de exemplo misturam a camada curricular no caminho da resposta medida e com isso contaminam os construtos que o PP1 e o PP3 precisam preservar. Terceiro, ele libera personalização (tema, modo calmo, "Do meu jeito", variantes A/B/n) dentro do bloco de medida. Quarto, o vocabulário do painel do professor proíbe exatamente as categorias que o gêmeo produz ("abaixo do esperado para a idade") e que o PP4 mede ("identificação de risco"). Além disso, faltam superfícies inteiras que o projeto exige: consultas em linguagem natural com caminho de evidência, predição com incerteza, confirmação de alertas, saídas em formato de PEI e captura por câmera. O DUA, que está no título dos dois projetos, aparece uma única vez no estudo.

Contagem: **4 bloqueantes, 16 importantes, 7 menores.**

Convenção: "vuoo" = `projeto/vuoo.md`; "ciatec" = `projeto/ciatec.md`. Os números de linha da fonte se referem ao texto sem a imagem base64.

---

## Bloqueantes

### C1 · O A/B do PP3 está descrito errado, e as hipóteses dependem de braços que o projeto não financia
- **Severidade:** bloqueante
- **Onde:** `02-gamificacao.md`, "O que medir": *"Preservação da medida: correlação com o instrumento de referência nas variantes **com e sem gamificação**"*. `01-brief.md`, HIP-1: *"No A/B do PP3, a variante previsível tem retorno […] menor que a variante com recompensa surpresa"*. HIP-2: *"[…] ou a taxa de conclusão cai abaixo da versão **sem recompensa**"*. `05-decisoes.md` D-04: *"A HIP-1 testa isso no A/B do PP3."*
- **Problema:** o PP3 não compara versões com e sem gamificação, nem previsível contra surpresa, nem com e sem recompensa. Ele compara **Bot adaptativo × versão sem adaptação**, e as duas são gamificadas. HIP-1 e HIP-2 ficam sem desenho que as teste. Se alguém tentar acomodá-las no PP3, vai criar braços que o poder do estudo não cobre: são 40 por variante, com efeito mínimo detectável de d ≥ 0,63. Cada braço a mais derruba esse poder. Um avaliador leria a mudança como alteração não declarada do protocolo.
- **Evidência na fonte:** vuoo, PP3: *"os estudantes são distribuídos aleatoriamente, dentro de cada grupo, entre a versão com VUOO Bot adaptativo e uma versão sem adaptação, com 40 por variante, o que detecta diferenças de d de 0,63 ou maior […] A captura é considerada preservada se a correlação com o instrumento de referência se mantiver em ambas as variantes."* F3.3: *"Teste A/B do companheiro adaptativo contra uma versão sem adaptação (40 por variante)"*.
- **Correção:** (1) Reescrever o trecho de `02` e o critério de falsificação de HIP-1 e HIP-2 para os braços reais: "Bot adaptativo × Bot não adaptativo, ambos com a mesma linguagem". (2) Levar HIP-1 (previsível × surpresa) e HIP-2 (participação × desempenho) para lugares onde há desenho e n para elas: os testes A/B de configuração entre turmas do PP5 (vuoo F5.2, *"testes A/B de configurações de entrega entre turmas"*) ou o A/B/n do CIATec (ciatec §3.2.5, ≥ 500 por grupo). Declarar isso em `05-decisoes.md`. (3) Acrescentar uma nota: "esta linguagem não altera o desenho do PP3".

### C2 · Os microjogos de dupla camada põem o conteúdo curricular dentro da resposta medida e contaminam o construto
- **Severidade:** bloqueante
- **Onde:** `04-microjogos.md`, conceitos 1 a 4. Também `vuoo-linguagem.html`, cartão "Microjogo: Sinal Aberto, controle inibitório com consciência fonológica".
- **Problema:** em todos os exemplos, a dimensão curricular **decide qual é a resposta certa** na tarefa que mede a função executiva. Com isso, o erro passa a misturar dois construtos:
  - **Sinal Aberto** (go/no-go + /b/): a criança que não domina o fonema comete erros de "comissão" e "omissão" que são de consciência fonológica, e não de controle inibitório. O tempo de reação passa a incluir processamento auditivo e lexical, numa sala que o próprio brief supõe barulhenta e sem fone. O mockup do HTML mostra outra tarefa (círculo/quadrado, sem fonema), o que deixa a incoerência à vista.
  - **Bolhas** (Fitts + número): o alvo só se distingue "pelo número". A tarefa vira busca visual mais reconhecimento numérico, e o tempo de movimento deixa de seguir a lei de Fitts. "Do menor para o maior" acrescenta sequenciamento e memória de trabalho. O próprio texto diz que a bolha "não se destaca por cor" para não alterar a medida, mas a alteração já veio pelo número.
  - **Ninho de Memória** (Corsi + sílabas BO-LA): formar uma palavra conhecida permite codificação verbal e agrupamento. O span deixa de ser visuoespacial.
  - **Trilho Certo:** o regime é "treino", mas o texto diz que "planejamento é medido". É uma contradição interna. No regime de treino há pista e desaceleração (`02` §5), o que invalida a medida.
- **Evidência na fonte:** vuoo OE5: dupla camada *"validados quanto à preservação dos construtos de captura pelo CIATec/CCD"*. OE1: *"preservando os construtos clínicos"*. PP3, critério: r ≥ 0,40 em 2/3 das métricas. PP1, critério: r ≥ 0,50 e CCI ≥ 0,75. Tabela 5, vermelho: *"Perda do construto na migração"*. E §4 lembra que o desempenho de neurodivergentes é *"mais sensível ao contexto, à familiaridade com a tarefa"*, então a contaminação curricular atinge os grupos de forma diferente e enviesa a "diferença entre grupos" exigida no PP1.
- **Correção:** acrescentar a `04` uma **regra de composição da dupla camada**, aprovada pelo CIATec: (a) nos blocos de medida, o conteúdo curricular **não pode ser a dimensão que discrimina a resposta**. Ele entra como roupa (o que se toca é a figura de um "bolo", mas o go é dado pelo sinal) ou em blocos separados de treino dentro do mesmo microjogo (regime misto). (b) Quando o conteúdo precisar discriminar, usar só itens que a criança já domina, verificados antes, e registrar isso. (c) Refazer os 5 conceitos com essa regra e marcar cada um como "proposta sujeita a parecer de preservação do CIATec (vuoo E1.3/F1.2)". (d) Corrigir o Trilho Certo para "misto" ou "medida".

### C3 · Personalização livre dentro do bloco de medida: tema, modo calmo, "Do meu jeito", escala de texto e variantes A/B/n
- **Severidade:** bloqueante
- **Onde:** `02` ("Tema de interesse: […] A medida não muda (R0)"; "Do meu jeito"); `03` §5 (o modo calmo troca `ceu`, `sol`, `folha`, inclusive no alvo; "Uma cor forte por tela, e ela está no alvo"; "Variantes para o A/B/n": saturação de `ceu` entre 35% e 60%); `03` §6 (escala de texto até 150%); `04` (os temas mudam a "roupa" do estímulo).
- **Problema:** o estudo herda da pesquisa `b` (R0) a classificação de "cor, som, animação decorativa, mascote" como apresentação, livre para personalizar. Num go/no-go ou numa tarefa de tempo de reação, porém, **a cor, o contraste e a saliência do alvo são parâmetros do estímulo**: alteram o tempo de reação. Tema de interesse (trem para quem tem hiperfoco em trem) muda familiaridade e engajamento, e o projeto afirma que isso pesa mais para neurodivergentes. A frase "a medida não muda" é uma hipótese não testada escrita como fato. Somadas, as variações (6 temas × 2 modos × 3 escalas × 3 intensidades × presença do Bot × 5 variantes do CIATec) criam variância não controlada nos mesmos blocos de que depende a correlação do PP3.
- **Evidência na fonte:** vuoo §4: desempenho neurodivergente *"mais sensível ao contexto, à familiaridade com a tarefa e ao nível de engajamento"*. F1.2: *"normalização das variáveis de captura"*. PP3: preservação *"em ambas as variantes"*. ciatec §3.2.5: cinco interfaces visuais testadas para "engajamento **e aprendizagem**".
- **Correção:** (1) Separar formalmente **palco de medida** (estímulos travados: cor, contraste, tamanho, tema, som e animação definidos no protocolo do CIATec, sem efeito de modo calmo, tema ou escala) e **moldura** (faixa, Bot fora do palco, Pouso, Caminho: personalizáveis). (2) O tema entra no palco de medida só como parâmetro registrado e, se possível, contrabalanceado, com análise de invariância no PP3. (3) Registrar todas as configurações ativas por sessão como covariáveis. (4) Trocar "A medida não muda" por "Hipótese: a medida não muda. Teste: invariância por tema no PP3". (5) Restringir as variantes do A/B/n à moldura nos jogos com regime de medida.

### C4 · O vocabulário do painel bloqueia o que o gêmeo produz e o que o PP4 mede, e omite a "orientação de encaminhamento"
- **Severidade:** bloqueante
- **Onde:** `03` §12, glossário: evitar *"abaixo, atrasado"*; *"Alertas nunca usam 'risco' sozinho"*; exemplo *"Padrão diferente do esperado **para a turma**"*. `05` D-16 ("risco" fora da interface). `vuoo-linguagem.html`: *"A evolução é da criança em relação a ela mesma."* `00` [IN-04] cita a ética do vuoo sem a parte do encaminhamento.
- **Problema:** (a) O gêmeo classifica cada estudante em *"abaixo, dentro e acima do esperado para a idade"*. Esse é o alvo do PP2. A linguagem proíbe "abaixo" e ancora o painel em progresso intraindividual. A informação central do produto fica sem forma de ser dita. (b) O PP4 tem como critério de passagem uma **redução de 30% no tempo até a identificação do risco**, além da acurácia dessa identificação em relação à classificação de referência. Um painel que só mostra avanço e fala em "padrão diferente" torna a identificação mais lenta e mais ambígua. É uma decisão de linguagem que pode, sozinha, derrubar o critério. (c) "Esperado para a turma" é uma norma por turma, diferente da norma etária do gêmeo. Em turmas pequenas, ou com vários estudantes com PEI, ela fica estatisticamente frágil. E é comparação entre crianças, o que o estudo proíbe em outros lugares. (d) A fonte exige que os padrões atípicos venham **"com orientação de encaminhamento"**. O estudo cita a frase pela metade e não tem nenhum padrão de encaminhamento.
- **Evidência na fonte:** vuoo PP2: *"classificação do desempenho em faixas definidas pelo instrumento de referência (abaixo, dentro e acima do esperado para a idade)"*. PP4: *"tempo até a identificação do risco, a acurácia dessa identificação frente à classificação de referência"*; critério *"redução de 30% ou mais no tempo até a identificação do risco"*. Ética: *"Padrões atípicos são comunicados à escola como sinais pedagógicos, **com orientação de encaminhamento** e sem rotulagem."* F4.2: *"alertas de risco"*.
- **Correção:** (1) Permitir no painel do professor a faixa descritiva por idade, nomeando o construto e o instrumento: "Controle inibitório: abaixo do esperado para 7 anos (instrumento X, 9 sessões)". Continua proibido nomear condição. A proibição de "abaixo" fica restrita à tela da criança e ao relatório para a família. (2) Manter "sinal" como rótulo de interface, mas com uma tabela de correspondência "alerta de risco (projeto) = sinal de atenção (UI)" para os relatórios FAPESP. (3) Criar o componente **Encaminhamento** (o que observar, com quem conversar, que serviço da rede acionar), sem diagnóstico. (4) Trocar a norma "para a turma" pela norma etária do instrumento. (5) Levar duas ou três variantes de vocabulário para o F4.1 e o co-design, medindo tempo e acurácia de identificação antes do F4.3.

---

## Importantes

### C5 · Ameaças à execução do A/B do PP3 que a própria linguagem cria
- **Severidade:** importante
- **Onde:** `03` §4 ("O Bot sempre: 2. pode ser escondido pela criança ou pelo professor"; regra 6, "não fala durante bloco de medida"); `02` §16 (limite de 2 voos por dia, voo com fim); `02` §3 ("a ausência da criança quase nunca é escolha dela").
- **Problema:** (a) **O braço de controle não está definido.** Os quatro comportamentos são disparados por sinais do gêmeo, mas o estudo não diz o que faz o "Bot não adaptativo": fica parado, segue um roteiro fixo, sorteia comportamentos? (b) **Bot ocultável** por criança ou professor significa que parte do braço adaptativo não recebe o tratamento. Isso dilui o efeito previsto (d ≥ 0,63 já é alto). (c) **"Retorno em sessões subsequentes"** é desfecho do PP3, mas o próprio estudo argumenta, com razão, que na escola o retorno é decidido pela escola e não pela criança. O desfecho fica pouco sensível ao Bot. (d) O **limite diário e o voo com fim** criam teto para "tempo em tarefa", outro desfecho. (e) Com o Bot calado e parado nos blocos de medida, a preservação da captura passa "por construção", o que um avaliador pode ler como teste trivial.
- **Evidência na fonte:** vuoo PP3: desfecho *"taxa de conclusão das atividades, tempo em tarefa e retorno em sessões subsequentes"*; F3.1: *"regras de transição a partir das saídas do gêmeo"*.
- **Correção:** especificar na linguagem a variante "Bot não adaptativo" (mesma arte, mesmo lugar, comportamento fixo por fase). Travar a ocultação do Bot e o "Do meu jeito" durante o estudo, ou registrá-los para análise por intenção de tratar. Propor ao PP3 desfechos de engajamento sob controle da criança ("Voar de novo" voluntário, "Agora não", pausas, conclusão). Fixar o mesmo limite diário nos dois braços. Declarar explicitamente que o Bot fica fora do palco nos dois braços, para que a comparação de captura seja limpa e não trivial.

### C6 · Continuidade entre PP1 e PP3: qual versão foi calibrada, e em que condição
- **Severidade:** importante
- **Onde:** o estudo não menciona o PP1 nem o redesenho para smartphone (F1.2, mês 3 a 5). `01` descreve o uso em sala com rodízio, 30 colegas e sem fone.
- **Problema:** a calibração do PP1 (r ≥ 0,50; CCI ≥ 0,75) vale para a **versão gamificada aplicada no mês 5 a 8 por aplicador treinado**. Se os microjogos do PP3 (com temas, Bot, dupla camada e 45 a 70 s de jogo) forem outra versão, a validade do PP1 não se transfere e o PP3 revalida tudo com n = 80. Além disso, a duração de 60 a 90 s não aparece na fonte. Não há evidência de que esse número de tentativas sustente um CCI ≥ 0,75. As condições de sala que o estudo assume também não são as condições validadas, que tiveram aplicador.
- **Evidência na fonte:** vuoo PP1: *"a versão gamificada, por aplicador treinado da Wemoga"*; F1.2: *"Redesenho dos instrumentos para smartphone […] Parecer de preservação dos construtos [C]"*, E1.3 no mês 5.
- **Correção:** definir um **núcleo de medida congelado** a partir do PP1 (estímulos, tempos, número de tentativas, feedback), que o microjogo apenas envolve. Aplicar a moldura da linguagem já na versão do PP1, ou declarar que o PP1 usa uma moldura neutra e que a troca será validada no PP3. Pedir ao CIATec o número mínimo de tentativas por construto e derivar dele a duração, em vez de fixar 60 a 90 s de antemão. Distinguir na linguagem um "modo aplicação" (estudos) e um "modo sala" (rotina).

### C7 · Palco 4:3 escalável e orientação livre mudam o estímulo físico entre aparelhos
- **Severidade:** importante
- **Onde:** `03` §11 ("O palco tem proporção fixa de 4:3 […] o mesmo microjogo roda igual em qualquer tela"); `05` D-13 ("Orientação livre").
- **Problema:** com proporção fixa, o tamanho físico do alvo e a amplitude do movimento variam cerca de três vezes entre um celular de 360 px e um tablet de 10". O índice de dificuldade de Fitts é invariante à escala só em teoria. Com alvos pequenos sob o dedo, o erro e o tempo de movimento mudam. A orientação livre muda o tamanho do palco no meio da sessão. "Roda igual" é falso no que importa para a medida.
- **Evidência na fonte:** vuoo F1.2: *"normalização das variáveis de captura"*; §6a: OpenBubble mede *"tempo de reação e a lei de Fitts"*; pesquisa `b` R35 já fala em alvos em mm.
- **Correção:** especificar os estímulos de medida em **milímetros**, com calibração por DPI do aparelho. Travar a orientação nos blocos de medida. Registrar o modelo e a tela do aparelho por sessão. Definir uma tela mínima para o regime de medida. Pedir ao CIATec o perfil de aparelho de referência.

### C8 · Elementos dinâmicos e perceptíveis durante a medida contradizem o próprio brief
- **Severidade:** importante
- **Onde:** `01`: *"um timer visível altera hesitação"*. Mas `02` §1, passo 6, e `04` (anatomia: "Fim com aviso […] a barra muda para `lavanda` […] conta para a medida: sim"); `03` §11 (barra de duração sempre presente no layout); `04` conceito 3 (o Bot "mostra a sequência, olhando para cada ninho", em bloco medido); `02` §5 ("A criança não percebe a troca de regime").
- **Problema:** o estudo afirma que um timer visível contamina a medida e, em seguida, põe uma barra que esvazia e **muda de cor nos últimos 10 s de um bloco medido**. O olhar do Bot no Ninho de Memória é uma pista adicional durante a codificação do span e contradiz a regra de o Bot ficar fora da medida. A afirmação de que a criança não percebe a troca de regime não tem teste. No treino há pista e som diferenciado, na medida não há, e o contraste pode afetar o engajamento e a ansiedade justamente na medida.
- **Evidência na fonte:** vuoo PP3 (*"sem comprometer essa captura"*); [IN-17] do próprio estudo.
- **Correção:** barra oculta por padrão nos blocos de medida, salvo se o protocolo exigir. Sem mudança de cor dentro do bloco. Aviso de fim só entre blocos. O Bot não sinaliza estímulos medidos: a sequência é apresentada pelo próprio palco. Reescrever "a criança não percebe" como hipótese, a ser verificada no co-design e no PP3. Documentar a exceção "essencial" da WCAG 2.2.1 para tarefas com tempo.

### C9 · Superfícies do professor e do gestor que o projeto exige e a linguagem não cobre
- **Severidade:** importante, perto de bloqueante para o PP4
- **Onde:** `03` §12 (só cartões de observação e um exemplo de gestor). Nenhum arquivo trata de consultas em linguagem natural, de predição ou de formato de PEI. "Graph RAG" e "linguagem natural" aparecem só em [IN-21].
- **Problema:** o grupo VUOO do estudo de eficácia (PP4) usa **relatórios, alertas e consultas em linguagem natural**. A linguagem não define: (a) o padrão de resposta do Graph RAG (estrutura, exibição do caminho de evidência, o que fazer quando não há evidência, como recusar perguntas diagnósticas); (b) como mostrar **predição e incerteza**, que é o produto central do gêmeo; (c) **saídas em formato de PEI** aceitas pelas secretarias (F4.1); (d) a **confirmação do alerta pelo professor**, que é a métrica do PP5 (*"proporção confirmada pelo professor responsável"*); (e) a **exportação para prestação de contas** (F4.2); (f) como a linguagem garante o critério de DUA do PP4 (efeito que não varia com o letramento digital).
- **Evidência na fonte:** vuoo PP4 (grupo VUOO *"dispõe dos relatórios, dos alertas e das consultas em linguagem natural"*); PP2 (*"caminho de evidência recuperável em todas as respostas"*); PP5 (precisão dos alertas por confirmação); F4.1, F4.2; §4 (*"independentemente do nível de letramento digital"*).
- **Correção:** acrescentar a `03` uma seção "Painel do professor" com componentes e falas-modelo para: resposta em linguagem natural (afirmação, evidência que pode ser expandida, limite: "não sei" e "não respondo diagnóstico"); faixa de predição com intervalo, em linguagem simples; botões "Confirmo / Não observei / Encaminhado" em cada alerta; modelo de PEI exportável; exportação para gestor. Testar com estratificação por letramento no co-design.

### C10 · Construto rotulado errado no exemplo-mestre do professor
- **Severidade:** importante
- **Onde:** `03` §12: *"Davi S. — **Atenção sustentada**"* com evidência *"jogo da luz (**controle inibitório**)"*; alerta-modelo *"[…] em atenção sustentada"*. O HTML usa outro rótulo ("Esperar antes de agir").
- **Problema:** o card-exemplo atribui a um construto um dado que mede outro. "Atenção sustentada" nem está na lista de construtos do projeto. Num produto cuja promessa é rastreabilidade, e cujo PP4 mede a confiança do professor, este é exatamente o erro que o avaliador vai citar. Os dois documentos também divergem entre si.
- **Evidência na fonte:** vuoo §4: funções executivas = *"planejamento, controle inibitório, flexibilidade cognitiva e memória de trabalho"*. Variáveis atencionais vêm do Wemoga Eye, não do go/no-go.
- **Correção:** usar o nome do construto da ontologia, com um subtítulo em linguagem simples ("Controle inibitório: esperar antes de agir"). Criar uma regra: o rótulo do cartão vem sempre da ontologia (vuoo F2.1), nunca de texto livre. Alinhar o `03` com o HTML.

### C11 · O DUA, que está no título dos dois projetos, está quase ausente
- **Severidade:** importante
- **Onde:** a sigla "DUA" aparece uma vez (`00`, [IN-02]). Não há nenhuma ocorrência de "Desenho/Design Universal". `03` §11: *"Só toque simples"*; `04`: acionadores ficam como pendência.
- **Problema:** o VUOO opera o DUA *"em dois níveis"*: no design das micro-atividades e como critério da interface do professor. O CIATec o tem como fundamento. O estudo faz várias coisas compatíveis com o DUA, mas não as organiza pelos três princípios (múltiplos meios de engajamento, representação e ação/expressão). O meio de expressão é um só (toque simples), sem alternativa planejada (voz, olhar via Wemoga Eye, acionador). Um avaliador CIATec/FAPESP espera essa rastreabilidade.
- **Evidência na fonte:** vuoo título, §4 (*"oferecendo múltiplos meios de representação, engajamento e expressão"*; DUA *"em dois níveis simultâneos"*), F3.2 (*"fundamentado no DUA"*); ciatec resumo e objetivos.
- **Correção:** acrescentar uma matriz DUA × linguagem (princípio → decisões → lacunas). Para ação e expressão, definir quais meios alternativos geram um **perfil de parâmetros próprio** (C3) e quais ficam só no treino. Ligar a pendência de acionadores ao F3.2 e à consultoria de design instrucional.

### C12 · A colaboração do CIATec foi rebaixada a "fase 2" e o Céu da turma é apresentado como se a cumprisse
- **Severidade:** importante
- **Onde:** `02` §10 (o Céu da turma *"traz para o VUOO o pilar aprender a conviver e a colaboração que o CIATec pede"*); §18 e `04` (voo em dupla e Ponte em Dupla "para depois"); `03` §1 (os 4 jogos do CIATec rodam no VUOO "com os mesmos componentes").
- **Problema:** para o CIATec, a plataforma **é composta por jogos colaborativos**, ligados à evidência de jogo colaborativo com **mediador (professor ou IA)**, e o brincar colaborativo exige *"consciência mútua, coordenação e comunicação"*. Um contador anônimo de estrelas não atende a essa definição. Se os jogos do CIATec vão rodar com os componentes do VUOO, a biblioteca precisa de colaboração agora, e não de um cartão de dupla rascunhado. O papel do Bot como **mediador** num jogo colaborativo, que é a ponte natural entre os dois projetos, não aparece. Os pilares "ser" e "conviver" ficam reduzidos ao Ninho e ao Céu, e todos os cinco conceitos são "conhecer" ou "fazer".
- **Evidência na fonte:** ciatec resumo (*"A plataforma será composta por jogos colaborativos acessíveis"*); §1 (mediador professor ou IA; Hijab et al.); Tabela 2 (os temas de "viver juntos" e "ser" são de trabalho em equipe e apoio mútuo).
- **Correção:** deixar de afirmar que o Céu da turma cumpre a colaboração. Chamá-lo de "pertencimento assíncrono". Especificar já os componentes colaborativos mínimos (turno, objetivo compartilhado, comunicação por pictograma entre pares, Bot como mediador) para os jogos do CIATec, separados do regime de medida individual. Incluir ao menos um conceito de "conviver" e um de "ser" com mecânica real.

### C13 · O estudo prescreve o desenho de pesquisa do CIATec (A/B/n, feedback adaptativo, classificações)
- **Severidade:** importante
- **Onde:** `03` §5 (*"as variantes mudam valores de tokens dentro de faixas"*); `05` D-08 (*"'Classificação' é interpretada como nível individual […] visível só ao professor"*); `02` §5 (feedback fixo por regime); `01`, riscos (*"O CIATec testar 5 interfaces visuais quebra a identidade"*).
- **Problema:** o A/B/n do CIATec quer identificar *"as combinações mais eficazes para o engajamento e a aprendizagem"* entre **cinco interfaces visuais distintas, dois tipos de feedback e dois sistemas de progressão**. Limitar as variantes a ajustes de saturação pode tornar os efeitos indetectáveis e esvaziar a pergunta. O estudo não diz quais seriam os dois tipos de feedback nem o segundo sistema de progressão, e só tem o Caminho. O CIATec também quer IA que ajuste *"desafios, estímulos e feedbacks"* **em tempo real**, e o estudo trava o feedback por regime. "Classificações" foi decidido em D-08 quando deveria ser uma pergunta ao CIATec. Um produto comercial definindo a variável experimental de um CCD público é um problema de governança.
- **Evidência na fonte:** ciatec §3.2.5; OE5 do CIATec (*"IA adaptativa que ajuste desafios, estímulos e feedbacks"*); resumo (*"ajustados em tempo real"*); §3.2.4 (*"feedback adaptativo, progressão, classificações"*).
- **Correção:** reescrever como **proposta ao CIATec**, com três listas: invariantes de segurança (sem vermelho, sem perda, sem ranking entre crianças), variáveis experimentais abertas (interface, tipo de feedback no treino, sistema de progressão) e restrições de medida (C3). Oferecer candidatos concretos para os dois tipos de feedback e para o segundo sistema de progressão. Mover D-08 para "pergunta pendente ao CIATec".

### C14 · Ciência aberta, governança e propriedade intelectual: jogos do CIATec dentro do VUOO e o personagem do Bot
- **Severidade:** importante
- **Onde:** `03` §1 (*"Os 4 jogos do CIATec podem rodar dentro do VUOO com o selo 'Jogo do CIATec'"*); `05` D-01; `03` §4 (Bot como marca VUOO, fabricável para a animatrônica).
- **Problema:** a plataforma do CIATec é aberta, de uso gratuito sob aprovação do comitê gestor, e o uso comercial deve respeitar *"as licenças e a governança do projeto"*. Pôr os jogos do CIATec dentro de um SaaS pago, sem ressalva, pode ser lido como apropriação. O Bot é desenhado para servir a uma **animatrônica que é projeto do grupo CIATec**, com apoio da Wemoga. A titularidade do personagem e da arte não está prevista. O acordo de PI do F1.1 cobre registros INPI, SDK e Wemoga Eye, não personagem nem marca.
- **Evidência na fonte:** ciatec "Aplicações comerciais" (uso gratuito, comitê gestor, licenças); vuoo §9b (*"apoia o grupo CIATec no desenvolvimento de um projeto de animatrônica"*); F1.1 (escopo do acordo de PI).
- **Correção:** registrar em `05` uma decisão D-17: os jogos do CIATec continuam acessíveis gratuitamente fora do VUOO, e a integração depende do comitê gestor. Incluir personagem, marca e arte do Bot no acordo de PI (F1.1/E5.5). Marcar a animatrônica como do CIATec, e a compatibilidade como requisito compartilhado.

### C15 · Insumos omitem tensões das fontes com "sem rótulo" e "não clínico"
- **Severidade:** importante
- **Onde:** `00` [IN-04], [IN-05].
- **Problema:** o arquivo diz *"Nada aqui é opinião"*, mas seleciona. O CIATec propõe *"desenvolver um modelo de IA capaz de identificar, ao longo das atividades, padrões específicos que podem ser associados ao TEA"* e prevê aplicações futuras de *"apoio diagnóstico"*. Isso tensiona o "sem rótulo" e o "não clínico" que o estudo trata como absolutos. Se os jogos do CIATec rodam dentro do VUOO, a linguagem precisa dizer onde fica esse sinal: só na base de pesquisa, nunca na interface.
- **Evidência na fonte:** ciatec §1 (último parágrafo antes de "Objetivos"); "Aplicações comerciais" (dispositivos médicos, apoio diagnóstico). vuoo, ética (base de pesquisa separada).
- **Correção:** acrescentar um [IN-33] com a tensão, e uma regra explícita: inferências associadas a condição ficam restritas à base de pesquisa e nunca chegam à interface do professor, do gestor ou da criança.

### C16 · A captura por câmera (Wemoga Eye) não está coberta
- **Severidade:** importante
- **Onde:** só [IN-16] menciona. Nada em `02`, `03`, `04`, `05`.
- **Problema:** o projeto prevê eye e head tracking *"nas micro-atividades gamificadas"*. Isso exige: um padrão de aviso de câmera para a criança e para o professor (indicador visível, linguagem do assentimento), a regra de que o Bot e animações fora do palco não podem competir pelo olhar durante a captura atencional, e tratamento LGPD de dado de imagem de criança. A linguagem é a camada onde isso aparece para o usuário.
- **Evidência na fonte:** vuoo §5 e §9b/§9c (*"aplicação direta na captura de variáveis atencionais nas micro-atividades"*); ética (art. 14 da LGPD, assentimento).
- **Correção:** criar o componente "Câmera ligada" (luz da antena com estado próprio, pictograma, frase-modelo), a regra de Bot imóvel e fora do campo durante a captura, e a pendência jurídica sobre a câmera.

### C17 · Decisões "caras" travadas antes do co-design que o projeto financia
- **Severidade:** importante
- **Onde:** `05` D-02 (metáfora) e D-03 (mascote), ambas com "Reversibilidade: cara". `01`: *"O dono do produto delegou as decisões"*.
- **Problema:** o VUOO financia co-design com professores (OE6, três ciclos) e duas consultorias, de R$ 100 mil e R$ 50 mil, para definir *"a gramática de interação do companheiro digital **com base nos resultados do PP3**"*. O CIATec define seus jogos *"de forma participativa"*. Fechar identidade e personagem como irreversíveis antes disso contraria o método declarado nos dois projetos. E dá a um avaliador o argumento de que a consultoria orçada é redundante, ou de que o co-design é decorativo.
- **Evidência na fonte:** vuoo OE6, F3.4, §8 (as duas consultorias); ciatec §3.2 (co-criação), OE2 (rede colaborativa e aberta).
- **Correção:** reclassificar D-02 e D-03 como "proposta para o 1º ciclo de co-design", com critério de aceite e alternativa. Explicitar que este estudo é **insumo** das consultorias e não substitui o entregável delas.

### C18 · As hipóteses com crianças não têm estudo financiado nem protocolo ético no PIPE
- **Severidade:** importante
- **Onde:** `01` HIP-3 (*"grupos focais, crianças típicas"*), HIP-4 (*"teste de compreensão"* com o 1º ano), HIP-6 (*"teste de preferência"*), *"o teste de preferência entra no primeiro ciclo de co-design"*.
- **Problema:** o co-design do PIPE envolve **15 a 20 professores e coordenadores**, não crianças. Testes com crianças exigem protocolo no CEP, submetido com dois meses de antecedência. O estudo com crianças que existe para usabilidade, com grupos focais de estudantes, é o transversal do CIATec (200 estudantes, PT2).
- **Evidência na fonte:** vuoo F3.4, ética (*"novos protocolos dos PPs 3 a 5 são submetidos com pelo menos dois meses de antecedência"*); ciatec §3.2.2.
- **Correção:** para cada HIP com crianças, indicar onde ela roda (CIATec PT2, sub-estudo do PP3 com emenda ao CEP, ou piloto do PP5) e o prazo de submissão ética. Tirar "teste de preferência no co-design".

### C19 · O Bot sem boca contradiz a evidência que o estudo cita para justificá-lo
- **Severidade:** importante
- **Onde:** `03` §4 (*"Não há boca. A boca é o traço que mais varia entre expressões, o que torna a leitura menos estável"*; *"Crianças autistas leem emoção melhor em rostos de desenho simples (pesquisa b)"*).
- **Problema:** a pesquisa `b` (R33) recomenda **"boca clara"**. A evidência citada (Rosset et al.; Pino et al.) é sobre rostos de desenho **com boca**, e a vantagem foi observada em imagens **estáticas**, não animadas (Brosnan, a confirmar). A frase "a boca torna a leitura menos estável" não tem fonte e inverte a recomendação. O motivo real é a fabricação (animatrônica), que é legítimo, mas é um trade-off e não evidência. Isso pesa sobre a HIP-4 e sobre a exigência de "mediação sem dependência de linguagem verbal" (F3.1).
- **Evidência na fonte:** pesquisa `b`, R33 e o bloco [MODERADA]; vuoo F3.1.
- **Correção:** declarar o trade-off ("sem boca por fabricabilidade, contra a recomendação R33"). Prever uma boca de luz no visor como alternativa barata (matriz de LED). Pôr a legibilidade das 6 expressões, com e sem boca, como teste antecipado da HIP-4.

### C20 · A Coleção previsível contradiz a meta-análise citada como "motor"
- **Severidade:** importante
- **Onde:** `02` (*"O motor é outro: previsibilidade, competência percebida […] (Deci, Koestner & Ryan […] R27)"*); §9 (*"A cada 3 voos concluídos […] A próxima peça aparece antes de ser ganha"*); `05` D-07 (releitura de R28).
- **Problema:** na meta-análise de Deci, Koestner e Ryan (1999), as recompensas **esperadas e contingentes à conclusão ou ao engajamento** são as que mais reduzem a motivação intrínseca. As **inesperadas** não têm esse efeito. O "faltam 2 voos" é exatamente uma recompensa esperada e contingente à conclusão. A pesquisa `b` pediu coleção "inesperada" por esse motivo. A D-07 relê R28 como "não condicionada a desempenho" e inverte o sentido. Pode haver boa razão (o ECA Digital e a ansiedade com incerteza), mas a evidência citada não sustenta a escolha.
- **Evidência na fonte:** pesquisa `b` R28 (*"ela deve ser **inesperada**"*). A pergunta do PP3 é sobre engajamento, então o efeito de enfraquecimento é relevante.
- **Correção:** reescrever a D-07 como trade-off explícito (previsibilidade e conformidade × risco de enfraquecer a motivação intrínseca). Considerar peças **não anunciadas mas não aleatórias** (entregues em marcos fixos sem contador), ou elogio informativo como motor principal e coleção como secundária. Deixar como candidato a variável do A/B do PP5 ou do CIATec (ver C1).

### C21 · Afirmações sobre evidência sem a calibração devida (agrupado)
- **Severidade:** importante, pelo conjunto
- **Onde e problema:**
  - `02` §1: *"a previsibilidade é **a acomodação mais forte** para o TEA"*. É um superlativo sem fonte. A pesquisa `b` lista várias práticas baseadas em evidência, sem hierarquia.
  - `02` §8: *"agenda visual é apoio de evidência forte […] e funciona como lista de tarefas **para todos**"*. A pesquisa `b` registra a ressalva (Leaf et al., 2021, critérios frouxos da NCAEP), que o texto omite. "Para todos" não tem fonte.
  - `02`: *"Os números são reais (+17%)"*. São dados divulgados pela própria Duolingo, não estudo independente.
  - `01`: *"um timer visível altera hesitação; uma animação […] altera atenção"*. É plausível, mas está escrito como fato e sem fonte.
  - `00` [IN-28]: *"Saúde mental é desfecho monitorado"*. No CIATec, SDQ, RCADS e PANAS são **"triagens"** do estudo transversal de usabilidade, sem desenho pré/pós declarado. "A gamificação não pode gerar ansiedade mensurável" é inferência.
- **Correção:** trocar superlativos por qualificações ("uma das acomodações com mais apoio"). Repor as ressalvas da pesquisa. Marcar números de empresa como "dado da empresa". Reescrever [IN-28] como "o CIATec aplica triagens de saúde mental; recomenda-se usá-las como contra-indicador".

---

## Menores

### C22 · `00-insumos.md` mistura requisito derivado com citação de fonte
- **Onde:** [IN-04], [IN-05], [IN-13], [IN-17], [IN-25], [IN-28], todas com frases em negrito que são inferência (ex.: *"O Bot precisa ser fabricável em impressão 3D"*; *"A linguagem visual precisa ser parametrizável por tokens"*), num arquivo que diz *"Nada aqui é opinião"*.
- **Correção:** separar cada IN em "fonte diz" e "implicação [DERIVADO]".

### C23 · `99-pendencias.md` não existe
- **Onde:** `00` e `01` remetem a ele as lacunas e todos os `[ASSUMIDO]`. O arquivo não está na pasta.
- **Correção:** criar o arquivo ou corrigir as referências. Sem ele, não há rastreabilidade das premissas.

### C24 · Inconsistências de público e entre documentos
- **Onde:** `01` e HTML dizem *"6 a 11 anos"*; [IN-01] e o CIATec dizem *"6 e 12 anos"*. [IN-01] cita "vuoo §1" para "1º ao 5º ano, rede pública de SP", mas o VUOO diz "anos iniciais" e inclui B2B privado. O HTML usa o botão *"PARAR"*, contra a regra do `03` (*"Parar por hoje"*). O rótulo do cartão do professor diverge entre `03` e o HTML (C10).
- **Correção:** unificar em 6 a 12 anos e "anos iniciais, rede pública (entrada) e privada (B2B)". Alinhar os textos dos botões.

### C25 · A operacionalização dos quatro comportamentos não está marcada como proposta
- **Onde:** `03` §4, tabela de comportamentos.
- **Problema:** o VUOO só nomeia os quatro comportamentos. As definições ("espelhar = repetir o gesto"; "provocar = convite opcional") são interpretação e não estão marcadas como `[ASSUMIDO]`. "Recuar" mistura comportamento do Bot com ajuste de dificuldade do gêmeo. Um "provocar" sempre recusável pode deixar o gêmeo sem dados em faixas mais altas de dificuldade. Faltam os gatilhos quantitativos que o F3.1 pede (*"regras de transição"*).
- **Correção:** marcar como proposta. Separar "o que o Bot expressa" de "o que o gêmeo decide". Prever limiares como parâmetros do CMS.

### C26 · O comportamento offline não está descrito
- **Onde:** [IN-07] é citado, mas Céu da turma, Coleção, Dias de voo e o resumo do professor dependem de sincronização.
- **Correção:** definir estados offline (estrela "a acender", peça garantida localmente) e exigir carimbo de tempo local no tempo de reação, com regra de sincronização. Não mostrar ao professor "não voou" quando a sessão só não sincronizou.

### C27 · Pequenas distorções de fonte
- **Onde:** `03` §4: *"a animatrônica que a Wemoga já desenvolve com o CIATec"*. A fonte diz que a Wemoga **apoia** um projeto do grupo CIATec. `01`: *"O PEI é escrito a partir de observação, laudos […] É isso que o VUOO quer **substituir**"*. O VUOO se posiciona como apoio, e *"não como substitutos dos instrumentos clínicos"* (vuoo §4).
- **Correção:** "apoia o projeto de animatrônica do CIATec"; "É isso que o VUOO quer complementar com evidência contínua".

---

## Verificação dos códigos [IN-xx]

| Código | Situação |
|---|---|
| IN-02, 03, 05, 06, 07, 08, 09, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 31, 32 | Citação confere com a fonte e a seção. |
| IN-01 | Seção errada. A faixa de idade e "rede pública de SP" vêm do CIATec, não de "vuoo §1". O VUOO inclui o B2B (C24). |
| IN-04 | Citação incompleta: falta "com orientação de encaminhamento" (C4). Omite a meta do CIATec de identificar "padrões associados ao TEA" (C15). |
| IN-13 | A fonte confere. O requisito de fabricação em 3D é inferência apresentada como fonte (C22). |
| IN-17 | A citação confere, mas o uso em `01` e `02` distorce os braços do A/B (C1). |
| IN-28 | Exagera: são "triagens", não desfecho (C21). |
| IN-30 | Não cita a seção. Omite que o uso comercial da base do CIATec depende de licença e governança (C14). |

## Ordem sugerida de correção

1. C1, C2, C3 e C4, antes de qualquer circulação para o CIATec ou de uso em relatório FAPESP.
2. C5 a C10, antes do início do PP3 (mês 8) e do F4.1 (mês 14).
3. C11 a C21, na próxima revisão do estudo.
4. C22 a C27, junto com o item 3.
