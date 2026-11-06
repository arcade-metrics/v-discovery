---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-microjogos
etapa: revisão independente, rodada 2
lente: segurança e respeito à criança
data: 2026-10-27
---

# Revisão rodada 2 · Segurança e respeito à criança

**Olhares combinados:** neurodesenvolvimento e educação especial (postura neuroafirmativa); ética de design para crianças (dark patterns, AADC, ECA Digital – Lei 15.211/2025, LGPD art. 14); adulto autista que estudou em escola pública.

**Postura:** adversarial. O estudo é bom e já resolve os problemas óbvios (streak, vidas, ranking, Duo que cobra). Por isso esta revisão procura os problemas que sobraram e que são menos visíveis: pressão que mudou de lugar sem sumir, números que viraram nota por outro nome, falas "literais" que não são, e uma camada de dados que o estudo de linguagem trata como problema de outro documento, quando a linguagem é justamente o que a expõe.

**Escala:** *bloqueante* = não pode ir para teste com crianças assim; *importante* = corrigir antes do co-design ou do piloto; *menor* = corrigir na próxima versão.

**Resumo dos achados**

| # | Achado | Severidade |
|---|---|---|
| S1 | A HIP-1 prevê um braço A/B com recompensa-surpresa em crianças | bloqueante |
| S2 | Dado sensível (diagnóstico/PEI) entra pela porta dos fundos; aviso à família é enganoso; falta o aviso à criança | bloqueante |
| S3 | O Céu da turma é, assumidamente, o instrumento de pressão; projetado na lousa com "Faltam 6 estrelas" + "Ver quem" | bloqueante |
| S4 | Painel do professor: comparação normativa, rótulo de construto, sem limite explícito e sem controle das recomendações | bloqueante |
| S5 | O Pouso mostra contagens de desempenho: é nota por outro nome e vaza o resultado da medida | importante |
| S6 | Coleção: "Faltam N voos" é gancho de gradiente de meta, ao lado do "Voar de novo" | importante |
| S7 | Dias de voo: a semana com casas vazias tracejadas mostra a ausência | importante |
| S8 | Expressão do Bot depende do desempenho; o "calmo" pós-erro se lê como triste; sem boca contra a evidência | importante |
| S9 | O Bot fala em voz alta, sem fone, o que denuncia a adaptação ao colega do lado | importante |
| S10 | O Ninho oferecido depois de erros vira "cantinho do pensamento" | importante |
| S11 | Falas-modelo que não são literais para uma criança autista de 6 anos | importante |
| S12 | O som de "pista" (duas notas descendentes) é o som universal de "errou" | importante |
| S13 | A métrica-norte pune pausa e Ninho; o "pular" vira dado sem proteção | importante |
| S14 | Aparelho compartilhado: login por avatar sem senha-figura expõe o perfil de uma criança a outra | importante |
| S15 | Lacunas de acessibilidade: Libras, acionadores, baixa visão, DI e idade, CAA, deficiência motora no painel | importante |
| S16 | A criança não é informada de que é medida (AADC 11, LGPD 14 §6) | importante |
| S17 | Vocabulário: "Modo calmo", "Provocar", "Espelhar", "típicas", persona deficitária | menor |
| S18 | Exemplo do painel usa a persona com TEA, com nome e inicial de sobrenome | menor |
| S19 | Limite diário sem teto, "Voar de novo" no aparelho em rodízio, ordem dos botões | menor |
| S20 | Relato ao gestor ranqueia turmas e permite reidentificação em células pequenas | menor |
| S21 | Inconsistências entre `.md` e `.html` que mudam o comportamento | menor |

---

## Bloqueantes

### S1 · O A/B da HIP-1 põe crianças num braço de recompensa variável
- **Severidade:** bloqueante
- **Onde:** `01-brief.md`, HIP-1: *"No A/B do PP3, a variante previsível tem retorno […] menor que a variante com recompensa surpresa"*. `05-decisoes.md`, D-04: *"A HIP-1 testa isso no A/B do PP3."*
- **Problema:** para falsear a HIP-1, o estudo prevê uma variante com "recompensa surpresa" aplicada a crianças reais, inclusive neurodivergentes. É exatamente o que D-07, I5 e a seção 9 de `02-gamificacao.md` proíbem. Dizer "a gente não faz recompensa variável, só testa" não protege a criança que caiu no braço B.
- **Por que importa:** I5 veda estética de sorteio "mesmo sem dinheiro", porque ela explora a vulnerabilidade de crianças com TDAH. A pesquisa `b` liga incerteza a ansiedade no TEA. O ECA Digital, art. 18, §2º, proíbe interface manipulada, e pesquisa não é exceção. Um CEP tende a barrar um braço que expõe crianças vulneráveis a um mecanismo que o próprio protocolo considera nocivo.
- **Correção:** reescrever a HIP-1 sem um braço de recompensa variável. Opções: (a) comparar "previsível" com "sem coleção" (controle mínimo); (b) comparar com um *benchmark* histórico de retenção de produtos escolares; (c) se a surpresa for indispensável, usar só surpresa **de forma** (animação de entrega diferente), nunca **de conteúdo ou de contingência**, e registrar isso em D-07. Acrescentar ao brief: "Nenhuma variante de teste pode conter mecânica que este estudo classifica como não segura."

### S2 · Dado sensível entra pela porta dos fundos; os avisos de privacidade não dizem a verdade
- **Severidade:** bloqueante
- **Onde:**
  - `01-brief.md`, persona: *"Tem diagnóstico de TEA, mas a escola não exibe isso em lugar nenhum e a plataforma também não sabe."*
  - `03-linguagem.md` §12, cartão do professor: *"Sugestão: registrar o avanço no objetivo 2 do Plano Educacional Individualizado."* Gestor: *"214 estudantes com Plano Educacional Individualizado têm acompanhamento contínuo registrado."*
  - `02-gamificacao.md`, métricas: *"Uso do Modo calmo e do Ninho, por perfil, só na base de pesquisa."*
  - `03-linguagem.md` §12, Família: *"O que o VUOO guarda? Só os jogos, para a professora ajudar."*
- **Problema:**
  1. O brief afirma que a plataforma não sabe quem tem diagnóstico. A linguagem do painel e do gestor só funciona se ela souber quem tem PEI e qual é o objetivo 2 do PEI. "Por perfil" na base de pesquisa quer dizer cruzar com condição. Ter PEI é, na prática, dado de saúde ou de deficiência: **dado sensível de criança** (LGPD arts. 11 e 14).
  2. O aviso à família diz "só os jogos". O VUOO guarda tempo de reação, hesitação, erros de comissão e omissão, pulos, pausas e uso do Ninho, e infere uma trajetória (o gêmeo digital). "Só os jogos" minimiza a coleta e induz a erro, o contrário do que pede o art. 14, §6º.
  3. O aviso **para a criança**, narrado pelo Bot, que I12 exige, não aparece em nenhuma tela do estudo. Só existe a versão impressa para a família.
  4. Nenhum documento menciona RIPD, base legal, retenção ou quem acessa o dado individual, embora I10 peça RIPD de forma explícita.
- **Por que importa:** para a rede, a legitimidade do VUOO depende disto (I30: "redes públicas estão mais atentas a dados depois das críticas às plataformas da SEDUC"). Para a criança autista, um dado de PEI cruzado com padrões de comportamento é exatamente o "rótulo" que o projeto promete não criar (`[IN-04]`).
- **Correção:**
  - Decidir e registrar em `05-decisoes.md` (nova D-17): **a plataforma sabe ou não sabe quem tem PEI/diagnóstico?** Se não sabe, tirar do painel e do gestor qualquer texto que dependa disso, e o professor faz o vínculo com o PEI fora do sistema. Se sabe, declarar como dado sensível, com base legal (política pública, art. 11, II, "b", sob o Enunciado CD/ANPD 1/2023), RIPD, acesso restrito ao professor regente e ao AEE, e nunca usado em "por perfil" sem consentimento específico de pesquisa (TCLE dos responsáveis + assentimento da criança).
  - Reescrever o aviso à família: *"O VUOO guarda como seu filho joga: o que ele tocou, quanto tempo levou e quando pausou. A professora usa isso para planejar as aulas. Ninguém de fora da escola vê o nome dele."*
  - Criar a tela do aviso à criança (ver S16).

### S3 · O Céu da turma é a pressão social que saiu da criança e voltou pela turma
- **Severidade:** bloqueante
- **Onde:**
  - `05-decisoes.md`, D-04: *"a pressão de retorno vai para o professor (lembrete, Céu da turma)"*.
  - `vuoo-linguagem.html`, Céu: *"Faltam 6 estrelas para o trem desta semana."* (texto para ser projetado na lousa).
  - `03-linguagem.md` §12: *"4 crianças ainda não voaram esta semana […] [ver quem]"*.
  - `02-gamificacao.md` §10: *"Quando a constelação da semana se completa […]"* (não diz o que acontece quando ela não se completa).
- **Problema:** o próprio registro de decisões chama o Céu de instrumento de pressão. Ele é anônimo no nível da estrela, mas não no da sala: em uma turma de 30, com rodízio de aparelho, todo mundo sabe quem não jogou. A professora tem um botão "Ver quem" e uma lousa com "Faltam 6 estrelas". O resultado previsível é "a gente não completou o trem por causa do Davi", dito no recreio. As crianças que mais faltam ao VUOO são as que saem para AEE, terapia ou atendimento, as que faltam por saúde e as que se desregulam e pulam. São exatamente as que o projeto quer proteger. Além disso, o Céu conta voos, não crianças, e com "Voar de novo" quem joga duas vezes vale o dobro. Isso cria uma hierarquia de contribuição.
- **Por que importa:** R29 e R30 permitem metas coletivas **cumulativas e anônimas** ("A turma acendeu 300 estrelas hoje"), sem prazo e sem falta. As críticas a ClassDojo e Kahoot (pesquisa `c`) documentam o constrangimento público de alunos da educação especial. AADC padrão 13 (*nudge*) e ECA Digital art. 18 §2º (interface manipulativa) cobrem a pressão de pares induzida pelo design. HIP-3 tem confiança "baixa", e o risco aqui é assimétrico: se falhar, falha em cima das crianças vulneráveis.
- **Correção:**
  1. **Sem "Faltam".** O Céu mostra só o que foi aceso: "A turma acendeu 18 estrelas." Sem contagem regressiva e sem fração.
  2. **Sem prazo que falha.** A constelação não vence na sexta. Ela se completa quando se completar, e a seguinte começa dali. Não existe estado "não completou". Documentar isso explicitamente.
  3. **Uma estrela por criança por dia**, não por voo, para que jogar mais não valha mais.
  4. **Desacoplar o Céu do lembrete.** O lembrete ao professor não fica na mesma tela nem no mesmo fluxo do Céu. "Ver quem" nunca aparece em modo projeção (ver S4).
  5. Reformular o lembrete como acesso, não como comportamento da criança: *"4 crianças ainda não tiveram vez no aparelho esta semana."*
  6. Tirar o Céu da justificativa de retenção em D-04 ou assumir o risco por escrito, com critério de parada no co-design: se uma criança for citada nominalmente como culpada, o Céu sai.

### S4 · O painel do professor ainda produz rótulo, mesmo sem a palavra "risco"
- **Severidade:** bloqueante
- **Onde:** `03-linguagem.md` §12 (Professor): *"Davi S. — Atenção sustentada"*; *"Padrão diferente do esperado para a turma em atenção sustentada"*. HTML: *"Davi S. · Esperar antes de agir"*. D-16.
- **Problema:**
  1. **Comparação normativa.** "Diferente do esperado para a turma" compara a criança com os colegas, embora a página diga que "a evolução é da criança em relação a ela mesma". Um professor lê "atenção" + "diferente do esperado" como "possível TDAH", com ou sem a palavra. O eufemismo não muda a inferência.
  2. **Rótulo de construto errado e patologizante.** O jogo é go/no-go (controle inibitório), e o cartão do `.md` diz "Atenção sustentada". Nomes de construto ("atenção", "controle inibitório", "memória de trabalho") são o vocabulário dos laudos. O HTML ("Esperar antes de agir") está melhor, mas os dois documentos divergem.
  3. **Falta o limite explícito** que I29 exige: "isto não substitui a avaliação da equipe".
  4. **Falta o controle para desligar recomendações automáticas** (I10; ECA Digital art. 17, §4º, V) e o caminho para contestar ou corrigir um sinal (LGPD art. 20, revisão de decisão automatizada).
  5. **Não há regra de uso:** o painel pode ser projetado? exportado? enviado ao gestor com nome? anexado a um encaminhamento? usado em conselho de classe para reter a criança no ano? Sem essas regras, "sinal pedagógico" vira prova documental.
- **Por que importa:** o brief diz que a professora "desconfia de plataforma que diz o que meu aluno tem". O risco maior é a professora que confia demais. Para um adulto autista, um papel com "padrão diferente do esperado em atenção" num prontuário escolar aos 7 anos acompanha a pessoa por anos.
- **Correção:**
  - Proibir a comparação com a turma no cartão individual. Só comparação intraindividual ("no começo do mês… agora…"). A comparação com a norma, se existir, fica para a equipe do CIATec, em documento técnico.
  - Rotular por **ação observável** em linguagem de sala, nunca por construto: "Esperar o sinal", "Lembrar a ordem", "Separar por regra". O construto fica no "De onde veio", com um link "o que isso mede e o que não mede".
  - Rodapé fixo em todo cartão individual: *"Isto é uma pista de sala de aula. Não é avaliação nem diagnóstico, e não substitui a equipe."*
  - Interruptor "Mostrar sugestões automáticas" (padrão ligado, desligável) e botão "Isto não confere com o que vejo", que registra e abaixa o peso do sinal.
  - Regra de linguagem: **sinal de queda nunca sai sozinho**; só depois de N sessões, e acompanhado de hipóteses de contexto ("mudou de aparelho? de horário? de sala?") antes de qualquer hipótese sobre a criança.
  - Painel nunca em modo projeção; exportação individual só para o próprio professor e o AEE; nada individual para o gestor.

---

## Importantes

### S5 · "O que você fez" com número é nota por outro nome, e vaza a medida
- **Severidade:** importante
- **Onde:** `04-microjogos.md`: *"Você esperou o sinal 9 vezes"*, *"Você tocou 14 bolhas"*, *"Você lembrou uma sequência de 4"*, *"O trem chegou na estação em 5 passos"*. `02-gamificacao.md` §13.
- **Problema:**
  1. São contagens de **acerto**. Na sala, viram "eu fiz 14, você fez 9". "Sequência de 4" é literalmente o *span* de Corsi, a nota do teste. "5 passos" tem um ótimo conhecido (menos é melhor), e a criança que levou 11 passos ouve isso.
  2. Em jogo de **regime de medida**, o feedback por tentativa é neutro de propósito (R15). Mostrar o total de acertos no fim devolve à criança a informação de desempenho que o regime escondeu, e isso pode alterar a estratégia na sessão seguinte (validade).
  3. Não existe regra para o caso **zero** ou muito baixo: "Você esperou o sinal 0 vezes" / "1 vez".
  4. Elogio descritivo virando vigilância: a criança aprende que o Bot conta tudo o que ela faz. Para algumas crianças autistas, que já vivem sob observação constante, isso é desconfortável.
- **Por que importa:** R17 recomenda "o que fez", mas o exemplo dela é de jogo de treino. O estudo removeu o XP justamente porque ele "alimenta comparação" (§2), e o número no Pouso faz o mesmo papel.
- **Correção:** no **regime de medida**, o Pouso descreve participação, não acerto: *"Você jogou o jogo das bolhas."* / *"Você jogou até o fim."* No **regime de treino**, contagem permitida, mas de **tentativas ou ações**, nunca de acerto, e nunca de passos com ótimo conhecido. Regra explícita: se a contagem de acertos for menor que um mínimo, usar a frase de participação. Nunca falar o número em voz alta (a voz chega ao colega, ver S9). Mostrar só no texto.

### S6 · Coleção: "Faltam N voos" é gancho de gradiente de meta
- **Severidade:** importante
- **Onde:** `02-gamificacao.md` §9 e D-07: *"Próxima peça: asa listrada. Faltam 2 voos."* HTML, Pouso: *"Faltam 3 voos"* imediatamente acima de "VOAR DE NOVO / PARAR".
- **Problema:** previsibilidade não resolve o efeito de **gradiente de meta** (quanto mais perto da recompensa, mais esforço para alcançá-la). Pôr "Faltam 2 voos" na mesma tela do "Voar de novo" é o padrão do "só mais um" que o §16 diz combater. "Faltam" é a moldura de falta que o princípio 3 ("nunca o que faltou") proíbe. Para uma criança com TDAH, a peça anunciada vira fixação. Para uma criança autista, vira uma promessa: se o rodízio não deixar jogar, "faltam 2" fica pendente por dias. Além disso, as peças aparecem no Bot, e o Bot de cada criança aparece em aparelhos compartilhados e no recreio ("o meu Bot tem chapéu, o seu não"). A coleção vira o marcador de status que o XP era.
- **Por que importa:** ECA Digital art. 17 §4º II (recompensa que estende artificialmente o uso); AADC padrão 13; R28 (não usar "ganhe X para desbloquear Y").
- **Correção:**
  - Não mostrar contagem regressiva. Mostrar a peça anunciada **sem** número ("A próxima peça é a asa listrada.") e **fora do Pouso**, no Caminho, longe do botão de continuar.
  - Ganho **por dia de voo**, não por voo, para que o "Voar de novo" não acelere a coleção.
  - Pensar em peças que não marcam quantidade: cada criança escolhe entre peças equivalentes, em vez de acumular. Ou a coleção fica visível só para a dona, sem aparecer no Bot fora do perfil dela.

### S7 · Dias de voo: a semana com casas vazias é a ofensiva de volta
- **Severidade:** importante
- **Onde:** `03-linguagem.md` §11: *"5 dias; dia com voo recebe uma pena; dia sem voo fica vazio, sem marca negativa."* HTML: casa vazia com **borda tracejada** (`border: 2px dashed`). `02-gamificacao.md` §3: *"A ofensiva vira 'dias de voo da turma' no painel do professor."*
- **Problema:** uma fileira de 5 casas onde a terça está vazia e tracejada **é** uma marca. A borda tracejada é a convenção de "falta preencher". Uma criança perfeccionista (perfil comum em TEA e ansiedade) vê um buraco na semana que não pode consertar. E se a contagem cumulativa ("40 dias de voo") for exibida, ela é comparável entre crianças, e quem falta por terapia ou internação fica sempre atrás.
- **Por que importa:** R29 e I6 pedem algo "cumulativo e sem perdas, como um diário de voo, um álbum ou um mapa que só cresce". Uma grade fixa de calendário não é um álbum que só cresce: ela tem lugares vazios por construção.
- **Correção:** trocar a grade da semana por uma **fileira que só cresce**, com uma pena por dia de voo, sem dias da semana e sem casas vazias. Não mostrar o total numérico para a criança. No painel, "dias de voo da turma" sem ranking e sem meta.

### S8 · O afeto do Bot ainda depende do desempenho, e o "calmo" se lê como triste
- **Severidade:** importante (bloqueante se o teste de compreensão da HIP-4 não for feito antes de fechar a arte)
- **Onde:** `03-linguagem.md` §4, Expressões e Comportamentos. *"Calmo: arcos para baixo, meio fechados; asas paradas, abaixadas"*, usado em **Recuar** (*"Erros seguidos, hesitação crescente"*). *"Celebrar → contente"*. HTML: `calmo` = olhos em ∪ e asas rodadas para baixo. *"Sem boca"*. `01-brief.md`: *"o Bot é meu"*.
- **Problema:**
  1. **Contingência afetiva.** O Bot fica *contente* quando a criança acerta ou termina e fica *calmo* (olhos baixos, asas caídas) quando ela erra. Mesmo sem arte de "triste", a criança aprende que o estado emocional do Bot segue o desempenho dela. É o mecanismo do Duo com sinal trocado, e é o que I9 e R33 ("nunca expressa decepção em resposta ao desempenho") querem impedir.
  2. **Leitura.** Olhos em ∪ semicerrados + asas abaixadas é a postura canônica de abatimento (o "u_u"). Sem boca para desambiguar, a leitura fica ainda mais incerta. A pesquisa `b` (R33) recomenda **boca clara**. O estudo tirou a boca por conveniência do animatrônico, contra a evidência citada, e a própria HIP-4 depende da legibilidade do rosto.
  3. **"Surpreso"** usa a mesma cor de antena do "contente" (`sol`), e "surpresa" contradiz o princípio 1 ("previsível"). Não está dito quando o Bot fica surpreso.
  4. **Vínculo.** "O Bot é meu", peças "para o Bot" e um nome dado pela criança formam um laço de cuidado (Tamagotchi). Isso é bom para o engajamento, mas cria dependência emocional, ainda mais com um animatrônico físico na sala. Crianças autistas podem formar vínculos intensos com personagens, e a regra para quando o Bot muda, é escondido pelo professor ou o produto é desligado na escola não existe.
- **Correção:**
  - Expressão do Bot **não contingente a acerto/erro**. Em erro e em Recuar, usar **atento** (neutro) ou **pensando**, nunca uma expressão nova. *Contente* só em pontos fixos que todo mundo alcança (fim do voo, peça nova), independentemente do desempenho.
  - Redesenhar o "calmo" com olhos não caídos (ovais semiabertos e retos) e asas na posição neutra, não abaixadas. Testar as 6 expressões com crianças de 1º ano, autistas e não autistas, **antes** de fechar a arte. Considerar uma boca simples só na tela (o animatrônico pode usar o LED).
  - Dar ao "surpreso" uma cor de antena própria e uma regra de uso, ou removê-lo.
  - Regras de vínculo: o professor **não** esconde o Bot de uma criança específica sem ela saber (ver S9); toda mudança de aparência do Bot é anunciada antes; o Bot não diz "estou contente *com você*".

### S9 · A voz em sala sem fone denuncia a adaptação ao colega do lado
- **Severidade:** importante
- **Onde:** `01-brief.md`: *"sala com 30 colegas e sem fone"*, *"sem que um perceba que a tela foi ajustada para o outro"*. `03-linguagem.md` §4 Recuar: *"Vamos mais devagar." / "Quer ir para o Ninho?"* §6: *"O professor troca para caixa mista por turma ou por criança."* R38 (pesquisa): Modo calmo como perfil inicial "quando o professor marcar a criança".
- **Problema:** Júlia, ao lado de Davi, ouve o Bot do Davi dizer "Vamos mais devagar" e "Quer ir para o Ninho?". A adaptação fica invisível na tela, mas audível na sala. O mesmo vale para ajustes feitos pelo professor por criança (caixa alta só para uma criança do 3º ano, Modo calmo marcado pelo professor, Bot escondido): são diferenças visíveis em aparelho compartilhado e decididas sem a criança.
- **Correção:**
  - Falas de **Recuar** e de oferta de pausa ficam **só em texto + pictograma** quando não há fone (padrão). A voz fica para instrução e fim de jogo, que são iguais para todos.
  - Ajustes por criança feitos pelo professor aparecem para a criança na tela "Do meu jeito" ("A professora deixou assim. Você pode mudar."), e nenhum ajuste por criança muda algo que outra criança vê.
  - Princípio 5 acrescido: "nem a tela, **nem o som**".

### S10 · O Ninho oferecido depois de erros vira "cantinho do pensamento"
- **Severidade:** importante
- **Onde:** `03-linguagem.md` §4 Recuar (*"Quer ir para o Ninho?"* depois de erros seguidos), falas: *"Vamos respirar devagar. Junto comigo."*; `02-gamificacao.md`: *"a tela escurece suavemente"*.
- **Problema:** se o Ninho é oferecido quando a criança erra, ele passa a significar "você está errando, vá se acalmar". Com o tempo, é o *time-out* da sala, com o mesmo estigma, e o colega ouve (S9). "Vamos respirar devagar" é uma instrução, não um convite; para parte das crianças autistas, a atenção dirigida à respiração (interocepção) aumenta a ansiedade. "Junto comigo" é literalmente falso: o Bot é um robô e não respira, e uma criança literal pode apontar isso. A tela que escurece pode assustar quem tem medo de escuro ou ler como "desligou".
- **Por que importa:** a pesquisa `b` traz a crítica neuroafirmativa à ABA (Mathur et al., 2024): foco em conformidade e em comportamento observável. Uma pausa que o sistema dispara por erro é regulação de comportamento, não autorregulação.
- **Correção:** o Ninho é oferecido em **pontos fixos** (tela de pausa, entre microjogos), nunca como reação a erro. No Ninho, várias opções iguais e opcionais: olhar o céu, ouvir o vento, respirar com o Bot, só esperar. Fala: *"Aqui você pode descansar. Toque em Voltar quando quiser."* O Bot "mostra" a respiração com as asas, sem dizer "comigo". Escurecer pouco, sem chegar a parecer apagado.

### S11 · Falas-modelo que não são literais para uma criança autista de 6 anos
- **Severidade:** importante
- **Onde e correção:**

| Fala | Arquivo | Problema | Proposta |
|---|---|---|---|
| "Toque quando o sinal **abrir**." | HTML, Sinal Aberto | "Sinal abrir" é expressão de trânsito; nada abre. O visual é um círculo cheio. | "Toque quando aparecer o círculo." |
| "**Voar** de novo" | botão, §16 e HTML | D-02 diz que "voo" nunca é figura de linguagem. Como verbo, é: a criança não voa. | "Jogar de novo" (e "Voo" fica só como substantivo de nome próprio). |
| "Hoje acabou. **Amanhã tem mais.**" | §12 | Falso na sexta, véspera de feriado e quando o rodízio não alcança a criança. Para uma criança autista, promessa quebrada pesa. Também é um gancho de retorno. | "Os jogos de hoje acabaram." |
| "Pausado. Toque em Jogar para **voltar**." | §12 | "Voltar" é também o pictograma de navegação "voltar" (sair). Ambíguo. | "Pausado. Toque em Jogar para continuar o jogo." |
| "Tem um **jeito** novo. Quer **ver**?" | §4 Provocar | "Jeito" é vago. "Ver" sugere assistir, e o que vem é jogar algo mais difícil. Uma criança que aceita "ver" e recebe uma tarefa sente que foi enganada. | "Tem um jogo um pouco diferente. Quer jogar?" + prévia visual. |
| Acerto: "**às vezes** 'Isso.'" | §12 | "Às vezes" é reforço de razão variável, o mecanismo que o estudo baniu, e quebra a previsibilidade. | Regra determinística: nunca falar no acerto, ou sempre no 1º acerto de cada microjogo. |
| Erro: "Toque no círculo azul." | §12, R14 | A criança não fica sabendo que o toque anterior não valeu. Muitas pessoas autistas preferem a informação explícita e neutra à correção implícita; a correção implícita parece pegadinha. Além disso, no Sinal Aberto o círculo é verde (`folha`), não azul. | "Esse não era. Toque no círculo." (neutro, sem "errado"). Revisar a regra 5 do Bot: proibir "errado/quase/de novo não", não proibir "não" como informação. |
| "Você esperou o sinal 9 vezes." | §4, §12 | A criança não sabe se 9 é bom e não sabe o que "esperou o sinal" quer dizer, já que tocou várias vezes. Ver também S5. | No treino: "Você esperou o quadrado passar 9 vezes." Na medida: frase de participação. |
| "Toque quando **ouvir** uma palavra que começa com /b/" | 04, Sinal Aberto | Dois verbos, condicional, e "/b/" não se fala. Contradiz a regra "uma frase, um verbo". | "Toque na figura que começa com **bê**." + demonstração. |
| "Que surpresa!" | §4, rótulos | Quebra o padrão "Estou ___" dos outros rótulos. | "Estou surpreso." (ou remover a expressão, ver S8). |
| "Agora: o jogo da luz." vs "Sinal Aberto" | §12 vs 04/HTML | O mesmo jogo tem dois nomes. | Um nome só, igual em fala, texto e pictograma. |
| "Vamos mais devagar." | §4 | "Vamos" atribui à criança uma decisão que o sistema tomou. Ouvido pelo colega (S9). | Só texto: "O jogo vai ficar mais devagar." |
| "Oi! Hoje tem 3 jogos." | §12 | Falso se o limite ou o rodízio cortar o voo. | Gerar a frase a partir do plano real do dia. |

### S12 · O som de "pista" é o som universal de "errou"
- **Severidade:** importante
- **Onde:** `03-linguagem.md` §10: *"pista: duas notas descendentes, mais graves que a do alvo, sem tom de 'errado'"*.
- **Problema:** duas notas descendentes e graves são exatamente o *earcon* de falha da cultura de jogos ("uó-uó"). Escrever "sem tom de errado" na especificação não muda o que a criança ouve. Na sala sem fone, o colega também ouve.
- **Correção:** a pista usa um timbre **diferente** do alvo, mas no mesmo registro e sem contorno descendente (por exemplo, uma nota única e suave de outro instrumento), ou nenhum som. Validar no co-design com a pergunta "o que esse som quer dizer?".

### S13 · A métrica-norte pune pausa e Ninho
- **Severidade:** importante
- **Onde:** `02-gamificacao.md`, "O que medir": *"Um voo conta quando chega ao Pouso e seus blocos de medida passam nos critérios de qualidade do CIATec (**sem interrupção**…)"*. §17: *"Pausar descarta a tentativa […] marca como interrompida."*
- **Problema:** se a métrica-norte só conta voos sem interrupção, toda pausa e toda ida ao Ninho reduzem a métrica que o time persegue. Em seis meses, alguém otimiza: o botão de pausa fica menor, o Ninho some do Recuar, a oferta de pausa deixa de aparecer. É um dark pattern organizacional, não de tela, mas chega à criança. Os pulos ("Agora não") são registrados como dado; o estudo não diz se o professor os vê por criança. Se vê, a recusa deixa de ser segura ("ele pulou 5 vezes").
- **Correção:** métrica-norte com **guarda-corpos**: "voos com medida válida **sem queda** na taxa de pausas oferecidas e aceitas". Separar "interrompido por pausa" (válido como dado de autorregulação) de "inválido". Proibir por escrito qualquer experimento que reduza a visibilidade da pausa, do Ninho ou do "Agora não". Pulos só agregados no painel, nunca por criança, a menos que a equipe do AEE peça.

### S14 · Aparelho compartilhado: uma criança vê o perfil da outra
- **Severidade:** importante
- **Onde:** `03-linguagem.md` §8 (avatares para se identificar sem ler); I26 (*"'senha-figura' opcional"*), que o estudo não incorpora; §4: *"Se a criança der um nome a ele, o nome é dela."*
- **Problema:** com login por avatar, sem segundo fator, qualquer criança toca no avatar de outra e vê o Caminho, a Coleção, os Dias de voo e os ajustes "Do meu jeito" dela, inclusive o Modo calmo. Também pode jogar no lugar dela, o que contamina o gêmeo e o painel. Nomear o Bot exige entrada de texto livre, que pode receber o nome completo da criança ou ofensas.
- **Correção:** senha-figura (2 ou 3 figuras) ligada por padrão a partir do 2º ano, opcional no 1º. Tela de troca de criança que limpa o estado. Nome do Bot escolhido de uma lista, não digitado. Registrar como requisito de segurança (LGPD art. 46).

### S15 · Lacunas de acessibilidade
- **Severidade:** importante
- **Onde:** `04-microjogos.md`, "Acessibilidade transversal"; `03-linguagem.md` §5–§11.
- **Problemas e correções:**
  1. **Surdez.** Não há **Libras**. Para uma criança surda de 6 anos não leitora, texto + pictograma não é equivalente à voz; a primeira língua dela é a Libras. Correção: vídeo curto em Libras nas instruções e no aviso de privacidade (LBI art. 28). Nos jogos de consciência fonológica, a "alternativa visual com a letra" mede outra coisa; a criança deve ser **dispensada** da medida, com registro, e não medida por uma alternativa que gera dado incomparável e um "sinal" falso no painel.
  2. **Acionadores.** O estudo deixa como pendência, mas um projeto que se vende como inclusivo não pode ir para piloto sem saber o que acontece com uma criança com paralisia cerebral na turma. Correção: decidir antes do piloto quais jogos têm modo varredura (*scanning*); nos jogos de tempo de reação, dispensa com registro.
  3. **Baixa visão e cegueira.** Sem modo de alto contraste (R37 cita "alto contraste" e o estudo não adota). O estímulo de "não tocar" (quadrado vazado em `contorno`, 3,5:1) é o mais fraco da tela. Não há plano de leitor de tela nem de suporte a ampliação do sistema no palco. Correção: token de alto contraste, borda do estímulo ≥ 4,5:1, e declarar quais jogos são inacessíveis a crianças cegas e qual é a alternativa pedagógica.
  4. **Deficiência intelectual e idade.** Um estudante de 10 ou 11 anos com DI que lê como alguém de 1º ano recebe caixa alta e o Bot "fofo" do 1º ano. A configuração por "série" vira sinal visível. Correção: separar **nível de leitura** de **aparência por idade**; temas e ilustração apropriados para 9–11 anos com a mesma simplicidade de texto.
  5. **CAA.** Crianças que usam CAA têm um sistema de símbolos próprio. Um conjunto de pictogramas diferente do que elas usam em sala (D-15) é uma segunda língua. Correção: mapear os pictogramas do VUOO para os mais usados no AEE e permitir trocar o símbolo de "tocar/esperar/pausar" pelo da criança.
  6. **Deficiência motora no painel.** Uma criança com TDC ou PC que jogar no perfil padrão vai gerar, toda semana, "padrão diferente do esperado" em tempo de reação. Correção: o painel suprime sinais de construtos motores quando há perfil de parâmetros alternativo, e nunca sugere "alvo maior" como sinal sobre a criança.
  7. **Tempo.** Nos jogos de treino, um limite de tempo precisa ser ajustável (WCAG 2.2.1); a exceção "essencial" só vale para os blocos de medida. Explicitar isso.

### S16 · A criança não é informada de que é medida
- **Severidade:** importante
- **Onde:** `02-gamificacao.md` §5: *"A criança não percebe a troca de regime"*; §14 (adaptação invisível); §15: *"o Primeiro voo é uma apresentação, não um teste"*, mas *"serve de calibração para o gêmeo"*.
- **Problema:** esconder a adaptação **dos colegas** é correto. Esconder **da própria criança** que ela está sendo medida é outra coisa. O AADC (padrão 11) pede sinal claro quando a criança é monitorada, e a LGPD art. 14 §6º pede informação adequada ao entendimento dela. Chamar de "não é um teste" uma sessão de calibração é, para adultos, impreciso. Para uma criança autista que depois descobre, é uma quebra de confiança.
- **Correção:** tela de aviso narrada pelo Bot no Primeiro voo e acessível pelo "Sobre": *"O VUOO guarda como você joga: o que você tocou e quanto tempo levou. A sua professora vê isso para te ajudar. Seus colegas não veem."* Botão "Ouvir de novo". No Primeiro voo: *"Agora você vai jogar para o VUOO te conhecer."* Assentimento simples da criança ("Quero jogar / Agora não"), com "Agora não" respeitado.

---

## Menores

### S17 · Vocabulário
- **"Modo calmo"** (`02`, `03`, HTML): o nome sugere que quem o usa precisa se acalmar, e é aí que nasce o marcador social que a HIP-5 teme. Correção: nomear pelo efeito, não pelo estado da pessoa: "Menos som e cor" ou "Modo suave".
- **"Provocar"** e **"Espelhar"** (`[IN-11]`, §4): "provocar" em português é implicar, e "espelhar" lembra o treino de imitação recíproca da clínica. Se ficarem só em documento técnico, tudo bem. Proibir que cheguem ao painel. Espelhar o gesto da criança pode ser lido como imitação zombeteira; testar.
- **"Crianças típicas"** (brief, HIPs): usar "neurotípicas" ou "sem condição identificada" de forma consistente; "típica" sugere que a outra é atípica no sentido de errada.
- **Glossário** (§12): "estudante autista (respeitando a família)". A preferência a respeitar é também a da **própria pessoa**, quando ela tiver uma, e não só a da família. Acrescentar "e a da criança".
- **Persona** (brief): Davi é descrito pelo que não faz ("ainda não lê", "se assusta", "desiste"). Júlia é descrita pelo que quer. Acrescentar o que Davi quer e sabe fazer (sabe de cor todas as linhas de trem, por exemplo), para que o time não projete só déficit.
- **"TEA"/"Transtorno"** fica restrito a documentos técnicos; na interface nunca aparece (já coberto pela regra 9 do Bot e por D-16, apenas confirmar).

### S18 · O exemplo do painel usa a persona com TEA, com nome e inicial
- **Severidade:** menor
- **Onde:** `03-linguagem.md` §12 e HTML: *"Davi S."*, a mesma criança que o brief descreve como autista.
- **Problema:** o mockup associa um nome e uma inicial de sobrenome a um diagnóstico dentro do material de design. Se o material circular (consultoria, CIATec, SEDUC), ensina que esse formato está bem. Se houver um Davi S. real na turma piloto, vira exposição.
- **Correção:** usar nomes claramente fictícios e sem inicial (ou "Estudante A") nos mockups, e nunca a persona com diagnóstico no exemplo de painel. Regra para o produto: o painel mostra o primeiro nome e só mostra a inicial quando houver homônimo.

### S19 · Limite diário e botões do fim
- **Severidade:** menor
- **Onde:** D-14, `02` §16, HTML.
- **Problema:** o professor define o limite, mas não há **teto** (um professor pode pôr 10). "Voar de novo" num aparelho em rodízio cria disputa ("você já jogou!"). No HTML, os botões são "VOAR DE NOVO" e "PARAR" (no `.md`, "Parar por hoje"), e o de continuar fica à esquerda, posição de leitura primeira.
- **Correção:** teto técnico (por exemplo, 3 por dia) que o professor não ultrapassa. Em modo aparelho compartilhado, "Voar de novo" não aparece. "Parar por hoje" à esquerda ou acima. Uniformizar os rótulos.

### S20 · Relato ao gestor
- **Severidade:** menor
- **Onde:** §12, Gestor: *"87% das turmas […] voaram pelo menos 3 dias por semana"*; *"214 estudantes com PEI"*.
- **Problema:** porcentagem por turma vira ranking de professores, e a pressão desce até a criança. A contagem de estudantes com PEI por escola pequena reidentifica crianças.
- **Correção:** não ordenar turmas nem escolas; supressão de células com n < 5 ou 10; não reportar "com PEI" abaixo do nível de diretoria.

### S21 · Inconsistências entre `.md` e `.html` que mudam o comportamento
- **Severidade:** menor
- **Onde e diferença:**
  - Coleção: "Faltam 2 voos" (`02`, D-07) × "Faltam 3 voos" (HTML).
  - Cartão: "Atenção sustentada" (`03`) × "Esperar antes de agir" (HTML).
  - Instrução: "Toque quando a luz ficar verde" (`03`) × "Toque quando o sinal abrir" (HTML); "jogo da luz" × "Sinal Aberto".
  - Botão: "Parar por hoje" (`03`) × "PARAR" (HTML).
  - Bot: R33 pede "boca clara" × D-03 "sem boca" (ver S8).
- **Correção:** escolher uma versão e propagar. Neste estudo, a fala é a especificação: duas versões de uma fala são duas especificações.

---

## Conformidade: quadro rápido

| Exigência | Situação no estudo | Achado |
|---|---|---|
| ECA Digital art. 7º (privacidade por padrão) | Parcial: sem senha-figura, perfis visíveis entre crianças | S14 |
| ECA Digital art. 8º IV / 17 §4º II (uso compulsivo, recompensa que estende o uso) | Parcial: limite sem teto, "Faltam N voos" junto do "Voar de novo" | S6, S19 |
| ECA Digital art. 17 §4º V (desligar recomendação) | Ausente no painel | S4 |
| ECA Digital art. 18 §2º (interface manipulada) | Risco: Céu com "Faltam", A/B com surpresa | S1, S3 |
| ECA Digital art. 20 (loot box) | Atendido no produto; violado no braço de teste | S1 |
| LGPD art. 11 (dado sensível) | Não tratado; o painel depende de dado de PEI | S2 |
| LGPD art. 14 §1º/§6º (consentimento; informação adequada à criança) | Aviso à família impreciso; aviso à criança ausente | S2, S16 |
| LGPD art. 20 (revisão de decisão automatizada) | Ausente | S4 |
| AADC 11 (sinal de monitoramento) | Ausente | S16 |
| AADC 13 (*nudge*) | Residual: Céu, Coleção, botão de continuar | S3, S6, S19 |
| LBI art. 28 (recursos de acessibilidade) | Sem Libras, sem acionador, sem alto contraste | S15 |
| RIPD (I10) | Não mencionado | S2 |
