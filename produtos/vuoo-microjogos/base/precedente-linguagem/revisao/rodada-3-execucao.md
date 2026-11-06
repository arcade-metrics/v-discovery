---
etapa: revisão rodada 3 · execução e consistência
data: 2026-10-27
material: 00, 01, 02, 03, 04, 05, 99, vuoo-linguagem.html, ferramentas/
---

# Rodada 3 · Execução e consistência

Olhar combinado: designer de produto que desenha as telas amanhã sem falar com o autor, dev front-end que implementa tokens, componentes e o Bot, ilustrador/animador do Bot. Pergunta de fundo: dá para executar a partir disto?

**Resposta curta:** dá para começar a ilustração e a paleta. Ainda não dá para desenhar o fluxo nem implementar o Bot. Faltam três artefatos: o mapa de telas e fluxo, a matriz evento → reação (Bot, som, voz, texto, antena) e uma escala de tokens além da cor. Além disso, a tabela de falas contradiz a regra de voz, e o HTML regrediu em vários pontos que a discussão dá como "alinhados" (S21).

Contrastes novos calculados com `ferramentas/contraste.py` (mesmas funções), sobre pares que o script não cobre.

---

## Bloqueantes

### E1 · A tabela de falas manda falar em voz alta o que a regra de voz proíbe
- **Severidade:** bloqueante
- **Onde:** `03` §4 Voz ("**Em voz alta, só instruções e fim de jogo**… Recuo, pausa, Ninho e ajustes ficam em texto e pictograma") e regra de conduta 10. Contra: `03` §12, tabela de falas-modelo.
- **Problema:** a coluna "Canal" põe em **voz** a pista ("Esse não. Toque no círculo." → *texto + voz*), a pausa ("Pausado. Toque em Continuar." → *texto + voz*), o pular (*texto + voz*), o convite e a peça nova (*voz + texto*). Numa sala sem fone (premissa do brief), os colegas ouvem "Esse não" a cada erro de uma criança, e o princípio 5 ("nem o que os colegas ouvem") cai. Os números também: "Oi! Hoje tem {n} jogos." e "Hoje você jogou {n} jogos." são *voz + texto*, contra S5/S9 ("números nunca falados em voz alta") e contra a linha "Nunca: … número falado" da tabela dos três públicos. Um dev que implementar a coluna "Canal" literalmente viola as regras.
- **Correção:** fazer da coluna "Canal" a fonte única e alinhá-la à regra. Pista, pausa, pular, convite → `texto + pictograma` (voz só com fone detectado ou se o professor ligar). Começo e fim do voo → voz sem número ("Oi! Hoje tem jogos novos." / "Você jogou os jogos de hoje.") e número só no texto. Acrescentar a regra explícita: **"Se um campo {n} entra na frase, a versão falada omite o número."** Definir o que é "fone presente" (configuração do professor por aparelho? detecção de saída de áudio?).

### E2 · A reação do Bot ainda depende de acerto e erro em três lugares
- **Severidade:** bloqueante (animação e máquina de estados)
- **Onde:**
  - `02` §5, tabela, linha Bot: "gesto pequeno **no acerto**";
  - `03` §12: "Ação registrada (treino): gesto do Bot";
  - `03` §4: Recuar = "erros seguidos → expressão **pensando**", contra "nem muda de expressão porque ela errou" no mesmo §4;
  - `03` §10: "ação registrada no treino: uma nota de marimba" (em toda ação ou só no acerto?).
- **Problema:** S8 foi aceito ("expressão não contingente a acerto/erro"), mas o texto ainda prevê gesto no acerto. A cadeia 3 erros → recuo → *pensando* torna a expressão contingente ao erro, com um atraso. E *pensando* também é a expressão de "carregando", então a criança aprende que *pensando* = "eu errei". O animador não sabe se o gesto toca em todo toque (Espelhar: "inclina quando ela toca") ou só no acerto.
- **Correção:**
  1. Trocar "gesto pequeno no acerto" por "o mesmo gesto em **todo** toque registrado, certo ou errado" (é o Espelhar).
  2. A mesma regra vale para a nota de marimba: o retorno de competência fica no **alvo**, não no Bot nem no som.
  3. No recuo, o Bot fica **atento** (sem mudança). O aviso "O jogo vai ficar mais devagar." vai em texto e pictograma, e *pensando* fica só para carregamento. Se o autor quiser manter *pensando* no recuo, registrar a exceção a S8 e a justificativa.

### E3 · Não existe máquina de estados do Bot, e a luz da antena tem colisão
- **Severidade:** bloqueante (dev e animador)
- **Onde:** `03` §4 (expressões, comportamentos), §9 ("Rive, com máquina de estados"), §11 componente "Câmera ligada".
- **Problema:**
  - **Curioso** usa antena `ceu`, e **Câmera ligada** usa antena "`ceu` **fixa** (estado próprio)". Se a câmera estiver ligada e o Bot convidar, a luz é a mesma. A antena mistura dois significados: emoção do Bot e estado do sistema.
  - **Atento** tem antena "apagada", e o HTML pinta `nevoa` (1,18:1 sobre `papel`, ou seja, invisível). Qual é o valor?
  - Faltam definições para: o Bot durante o bloco de medida (que expressão? pisca ou não? "imóvel" inclui o piscar?); a boca durante a fala (anima com o TTS? fica parada?); a entrada (de que lado? curva? versão com `prefers-reduced-motion`?); o período do pulso de *pensando*; a amplitude das asas ("mexem pouco" = quantos graus? O HTML usa 22–24°); a expressão no **fim de microjogo** (Celebrar diz que acontece, mas *contente* só vale no fim do voo); o Bot oculto (pela criança ou pelo professor); a prioridade quando dois eventos coincidem (peça nova + fim do voo + limite do dia).
- **Correção:** entregar uma tabela `estado × entrada → saída` (estados: entrando, atento, falando, curioso, pensando-carregando, contente, sossegado, imóvel-medida, câmera, oculto; entradas: toque, erro de treino, recuo, carregando, fim de microjogo, fim de voo, peça, Ninho, início/fim de bloco de medida, câmera on/off, Modo suave, reduced-motion), com duração, curva e prioridade. Separar a antena em duas camadas, ou tirar a câmera da antena. Proposta: a câmera ganha um **anel no visor** ou só o pictograma na moldura, e a antena fica só para emoção. Fixar "imóvel = sem piscar, sem respirar, expressão atento".

### E4 · Não há mapa de telas nem fluxo, e as regras de fluxo se contradizem
- **Severidade:** bloqueante (designer)
- **Onde:** `02` §1, §13, §15–17; `03` §11; D-14.
- **Problema:**
  - **Onde fica o Caminho?** A peça "aparece no Caminho" e *contente* acontece na "chegada no Caminho", mas nada diz se o Caminho é a tela inicial, vem depois do Pouso ou fica num menu.
  - **Onde fica o botão Pular?** "Pular ('Agora não') é sempre permitido", mas a moldura só tem Pausar e Ouvir. Então Pular está só na tela "Próximo" ou também dentro da Pausa?
  - **O que tem a tela de Pausa?** Continuar, Ninho, Pular, Sair? Em que ordem?
  - **Padrões que se anulam:** o limite padrão é **2 voos/dia** (D-14), mas no modo aparelho compartilhado (**padrão**) o Pouso só mostra "Parar por hoje". Com os dois padrões, como começa o 2º voo?
  - **Quando aparece o "Os jogos de hoje acabaram."?** No Pouso, em lugar de "Hoje você jogou…", ou numa tela própria no próximo login?
  - **O que vem depois de "Parar por hoje"?** Troca de criança? Tela da turma?
  - **Onde ficam as penas?** O HTML põe a fileira no Pouso; `02` e `03` não dizem.
  - **Tela "Sobre":** S16 aceitou o aviso narrado no "Sobre", mas `03` só menciona o "Sobre" para créditos.
- **Correção:** um diagrama de fluxo (login/troca → início → [Primeiro voo] → Plano → microjogo [9 fases de `04`] → Pausa/Ninho → Pouso → Caminho/peça → fim) com o inventário de telas, e uma regra para cada encruzilhada acima. Resolver o par de padrões, por exemplo: "em aparelho compartilhado, o 2º voo do dia é iniciado pelo professor".

---

## Importantes

### E5 · O toggle de Modo suave do HTML pinta o palco de medida e o painel do professor
- **Severidade:** importante (demonstra o contrário de D-20, que o próprio estudo chama de "a decisão mais importante")
- **Onde:** `vuoo-linguagem.html` l. 304–307 e 610–616. A classe `.calmo` é aplicada a `#produto`, que contém o mockup "Sinal Aberto, bloco de medida" (`.palco-medida`, `.sinal-luz` em `var(--folha)`) e o painel.
- **Problema:** ao clicar, o estímulo do palco muda de cor, logo abaixo do texto "O palco de medida não muda". O painel do professor também muda, embora o Modo suave seja ajuste da criança.
- **Correção:** dar ao palco valores literais (fora dos tokens) ou restaurar os tokens dentro de `.palco-medida`. Restringir `.calmo` aos mockups da criança. Usar o caso como teste de aceitação para o dev: "trocar o tema não altera nenhum pixel dentro do palco".

### E6 · O escopo do Modo suave diverge, e "suave" nomeia duas coisas
- **Severidade:** importante
- **Onde:** `03` §5 (o Modo suave troca 4 tokens: papel, ceu, sol, folha). `vuoo-linguagem.html` l. 38–42 troca 11, incluindo `ceu-profundo`, `ceu-claro`, `sol-claro`, `folha-claro`, `lavanda`, `lavanda-claro` e `olho`, ou seja, os olhos do Bot. `paleta.json` só valida 4. `02` §13: intensidade de celebração "**suave** / padrão / festa". `01`: "intensidades sobre os mesmos tokens (padrão, suave, festa)".
- **Problema:** o dev não sabe qual conjunto implementar, e os 7 valores extras não passaram pelo script. Pelo meu cálculo passam: `superficie`/`ceu-profundo` suave 7,87; `tinta`/`lavanda` suave 6,79. Mas não constam do resultado. "Modo suave" (som + cor + movimento) e "intensidade suave" (celebração) são controles diferentes com o mesmo nome. Também falta a precedência entre Modo suave, "Do meu jeito" (som, movimento, intensidade), `prefers-reduced-motion` e ajustes do professor.
- **Correção:** uma tabela de tokens por modo (padrão / suave / alto contraste) com todos os tokens, gerada a partir de `paleta.json` e validada. Renomear a intensidade de celebração para "quieta / padrão / festa". Escrever a precedência, por exemplo: reduced-motion define o valor inicial → professor ajusta → a criança sobrescreve → o Modo suave é um atalho que mexe em som, cor e movimento ao mesmo tempo.

### E7 · Contraste: o script valida pares que não são os usados
- **Severidade:** importante
- **Onde:** `03` §5 ("23 pares, todos AA ou AAA"); `paleta.json`; HTML.
- **Problema:** pares reais sem validação, e reprovados:

  | Elemento | Par | Razão | Meta |
  |---|---|---|---|
  | Pena da fileira, estrela offline, "próximo voo" no Caminho | `sol` / `papel` | **2,04** | 3:1 (1.4.11) |
  | Pena sobre cartão | `sol` / `superficie` | **2,23** | 3:1 |
  | Pena no Modo suave | `sol` suave / `papel` suave | **2,46** | 3:1 |
  | Borda de `.btn-ic`, `.balao`, `.plano span` no HTML | `nevoa` / `superficie` | **1,29** | 3:1 (se a borda delimita o alvo) |
  | Contorno de pista, se for `lavanda` (`03` diz "lavanda: pista") | `lavanda` / `papel` | **2,46** | 3:1 |
  | Silhueta do Bot (casco sem contorno) | `casco` / `papel` | ~1,05 | — |

  O par `sol`/`tinta` do script ("pena sobre visor") só vale para o Céu. Na linha do script, `contorno`/`superficie` aparece como "AA-grande", o que confunde, porque é um par de UI (3:1).
- **Correção:** acrescentar ao `paleta.json` os pares de uso real (pena, estrela, próximo voo, borda de alvo, contorno de pista, foco). Escurecer `sol` para ícones ou dar à pena um traço `sol-tinta`. Usar `contorno`, e nunca `nevoa`, como borda de alvo. Fixar a cor do contorno de pista (por exemplo, `lavanda-tinta`, 8:1+). Exigir no Bot um traço `contorno` (3,16:1 sobre `casco`), como o HTML já faz sem que `03` mande.

### E8 · Não há escala de espaço, raio, foco nem estados de componente, e os mockups contradizem os poucos números que existem
- **Severidade:** importante
- **Onde:** `03` §11 (alvo 64×64, 16 px entre alvos; botão primário 64 px, raio 20 px; pictograma raio 4 px). HTML: `.btn-ic` 44×44, `.plano span` 30×30, `.btn` min-height 56 e raio 18, `.balao` 16 px, `.feito-item` 15 px, `.btn-p` ~35 px, `summary` 32 px.
- **Problema:** não existe token de espaçamento, de raio (além de dois valores), de elevação, de foco ou de estados. Só "pressionado = `ceu-profundo`" aparece. Faltam desabilitado, focado, carregando, selecionado, pulado. O HTML desenha alvos de 44 px e textos de 16 px para a criança sem dizer que está em escala, e o designer copia o que vê. O adulto (painel) não tem alvo mínimo.
- **Correção:** acrescentar a `03` uma escala `espaco-1..8` (base 4 ou 8), `raio-s/m/l/pill`, um token de foco (por exemplo, anel `ceu` de 3 px, offset 3 px, 5,52:1 sobre `papel`, já validado mas não escrito como regra), estados por componente e alvo mínimo do adulto (44 px). Nos mockups, ou se usam os números reais, ou se anota "escala 0,7".

### E9 · Mesmo nome para três coisas: Ninho, Ninhos, Cuidar do Ninho
- **Severidade:** importante
- **Onde:** `02` §17 (Ninho = espaço de pausa); `04` §3 "Ninhos" (memória de trabalho) e §7 "Cuidar do Ninho"; `03` §7 pictograma "Ninho"; `03` §12 regra 8 ("Um nome por coisa").
- **Problema:** "Agora: Ninhos." e "Toque em Ninho para descansar" num mesmo voo, para uma criança de 6 anos que não lê. O pictograma de ninho vai significar duas coisas. No painel, "Bruno joga Ninhos" convive com "pausas no Ninho".
- **Correção:** renomear o jogo de memória (por exemplo, "Janelas Acesas" ou "Ordem das Luzes") e "Cuidar do Ninho" (por exemplo, "Casa do Bot"). Acrescentar à ficha-modelo de `04` uma checagem: "o nome não coincide com nenhum termo do vocabulário do sistema".

### E10 · As regras de vínculo prometem o amanhã e anunciam a peça
- **Severidade:** importante
- **Onde:** `03` §4 Vínculo: "Toda mudança de aparência do Bot é anunciada antes ('Amanhã o Bot vai usar a asa nova.')". Contra `03` §12 regra 7 ("nunca promete o amanhã"), `02` §16 (recusa "Amanhã tem mais") e `02` §9 / D-07 (coleção "**sem anúncio**").
- **Problema:** a peça da coleção é mudança de aparência. Ou ela é anunciada antes, e então deixa de ser inesperada (C20), ou não é, e a regra de vínculo falha. A frase-exemplo também quebra a regra 7.
- **Correção:** separar os casos. A **peça escolhida pela criança** já vem anunciada pelo próprio gesto de escolher, então não precisa de aviso prévio. **Mudanças impostas pelo sistema** (redesenho, troca de arte) recebem aviso no início do voo em que acontecem, sem falar em amanhã: "Hoje o Bot está com uma asa nova. Você pode trocar em Do meu jeito."

### E11 · Regressões no HTML: S21 diz "todas as divergências alinhadas", e não estão
- **Severidade:** importante
- **Onde:** `vuoo-linguagem.html`
- **Lista:**
  1. l. 226: "crianças de **6 a 11 anos** da rede pública". C24 fixou **6 a 12** e "pública (entrada) e privada (B2B)".
  2. l. 245: "desenhada **um voo de cada vez**" e "a linha que cresce: … **a barra de duração do microjogo**". `03` §2 diz "um dia de cada vez" e "a fileira de penas". A barra fica oculta na medida, então não pode ser a linha de identidade.
  3. l. 300: "Uma cor forte por tela, **e ela está no alvo**", e o swatch `sol` como "só recompensa **e alvo**" (l. 598). `03` §5 regra 2 diz que, na moldura, a cor forte é a ação principal, e `sol` é **só** recompensa.
  4. l. 517: "rotina fixa de **7 passos**". `04` tem **9 fases** (com Transição e bloco de treino separados). Ver E16.
  5. Superlativos que C21 mandou trocar: "Previsibilidade é **a acomodação mais forte** para o TEA" (l. 517; `02` diz "uma das acomodações com mais apoio"); "Agenda visual tem **evidência forte**" (l. 523; `02` registra a ressalva de Leaf 2021); "o erro é **o dado mais valioso**" (l. 520); "Ranking expõe **sempre** as mesmas crianças" (l. 525).
  6. l. 527: o "Por quê" do Bot ("Crianças autistas tendem a ler a ironia literalmente") não justifica "afeto que não depende do desempenho". O motivo certo está em S8.
  7. l. 285–286: a lista "O Bot nunca" omite "sarcasmo, piada de duplo sentido" e "de novo não", e não traz a lista "O Bot sempre" nem as regras de vínculo.
  8. l. 511: "é segura **para crianças neurodivergentes**"; `02` pergunta "É segura?" para todas.
- **Correção:** aplicar os oito itens. Gerar as tabelas do HTML (falas, jogabilidade, regras do Bot) a partir dos `.md`, ou declarar no topo do HTML que o `.md` prevalece.

### E12 · Mockup do bloco de medida: o Bot pisca e "fala" durante a medida
- **Severidade:** importante
- **Onde:** HTML l. 333–342 e l. 214–217 (`.pisca` aplicado a todos os olhos); `03` §4 regra 6 e §11 ("Bot: fora, imóvel, calado").
- **Problema:** no mockup "Sinal Aberto, bloco de medida", o Bot pisca a cada 5 s e aparece com balão de fala "TOQUE QUANDO APARECER O CÍRCULO." durante o bloco. Nenhum documento diz se a instrução fica visível como texto estático durante a medida ou se sai. Também no mesmo mockup: o pictograma "atual" do Plano de hoje usa `folha`, que é o token de **concluído**; a legenda do estímulo diz "quadrado vazado = **esperar**", enquanto `04` e o conjunto de pictogramas dizem "**não tocar**" (e "esperar" é outro pictograma).
- **Correção:** escrever a regra: "durante o bloco de medida, a instrução fica como texto estático na moldura, sem balão nem Bot falando; o Bot fica em `imóvel-medida`" (ver E3). Tirar o piscar no mockup, usar `ceu` no pictograma atual e trocar "esperar" por "não tocar".

### E13 · Falas com o mesmo evento em versões diferentes, sem regra de plural nem de escopo
- **Severidade:** importante
- **Onde:**
  - fim do voo: `03` §4 Celebrar diz "Você jogou 3 jogos hoje."; `03` §12 e HTML dizem "Hoje você jogou {n} jogos.";
  - fim de medida: `02` §13 e a discussão S5 dizem "Você jogou **o jogo das bolhas** até o fim."; `03` §12, `04` e HTML dizem "Você jogou **Bolhas** até o fim.".
- **Problema:** viola a regra 8 de `03` §12. `{n} = 1` gera "1 jogos". Também não está definido se {n} conta os jogos do voo ou do dia (o teto é de 3 voos), nem se jogos pulados entram. Em "Fim de bloco de treino", o canal "número só no texto" não diz **o que a voz fala**.
- **Correção:** uma tabela de strings com ID (`fala.fim_voo`, `fala.fim_medida`…), parâmetros tipados, plural ("1 jogo" / "{n} jogos"), escopo de {n} ("jogos concluídos neste voo, sem os pulados") e a versão falada de cada uma. Escolher uma forma para o fim de medida: o nome próprio do jogo ("Bolhas"), coerente com a regra 8.

### E14 · O exemplo de pista contradiz o próprio jogo
- **Severidade:** importante
- **Onde:** `02` §5, `03` §12 e HTML: pista no treino = "Esse não. Toque no círculo." `04` §1: o **treino** do Sinal Aberto é de consciência fonológica (figuras), e o círculo é estímulo do **bloco de medida**, onde não há pista.
- **Problema:** o exemplo canônico mistura os dois regimes, que é justamente a fronteira que o estudo quer ensinar ao designer.
- **Correção:** trocar por um molde, "Esse não. {instrução curta do treino}.", com o exemplo "Esse não. Toque na figura que começa com bê."

### E15 · A ordem do botão par se contradiz em quatro lugares
- **Severidade:** importante (S19 dado como aceito)
- **Onde:** `03` §11 ("a opção de parar ou recusar à esquerda"); `02` §1 passo 7 ("Jogar / Agora não"); `04` anatomia ("Agora não / Jogar"); `02` §15 e `03` §11 Aviso de dados ("Quero jogar / Agora não"); `02` §13 ("Parar por hoje" à esquerda, certo).
- **Problema:** se a barra representa a ordem visual, dois lugares invertem a regra. Também aparece "Jogar" como rótulo em duas fases diferentes (Pronto? e Próximo), sem indicar se é o mesmo componente.
- **Correção:** escrever sempre na ordem visual esquerda → direita, declarar a convenção uma vez e corrigir `02` §1, §15 e `03` §11 para "Agora não / Jogar" e "Agora não / Quero jogar".

### E16 · Rotina de 7 passos ou anatomia de 9 fases?
- **Severidade:** importante
- **Onde:** `02` §1 (7 passos: O que vem, Demonstração, Prática, Pronto?, Jogo, O que você fez, Próximo); `04` (9 fases, com "Jogo" desdobrado em Medida, Transição e Treino); HTML ("7 passos").
- **Problema:** o designer não sabe se a Transição ("Agora: {parte de treino}.") é uma tela. A parte de treino também não tem nome para a criança, o que fere a regra 8: o que entra em {parte de treino}?
- **Correção:** adotar as 9 fases de `04` como canônicas e fazer `02` §1 apontar para elas. Definir o nome falado da parte de treino de cada jogo na ficha-modelo (por exemplo, "Agora: figuras e sons.").

### E17 · O Plano de hoje não tem estado "pulado"
- **Severidade:** importante
- **Onde:** `03` §11 Plano de hoje ("Atual com anel `ceu`; feito com visto `folha`"); `02` §17 ("Pular é sempre permitido").
- **Problema:** se a criança pula o 2º jogo, o slot fica sem visto: uma "casa vazia" na tela da criança, o que viola o princípio 3. Também não está definido se o slot pulado some ou se o próximo é inserido.
- **Correção:** definir que o jogo pulado **sai do Plano** com uma transição de 200 ms, sem marca. O Plano mostra só o que foi feito e o que vem.

### E18 · Céu da turma: tamanho indefinido, desenho que mostra a falta, "Ver quem" sem destino
- **Severidade:** importante
- **Onde:** `02` §10, `03` §11, HTML l. 402–418 e 619–622; discussão S3 ("'Ver quem' nunca em projeção").
- **Problema:**
  1. Quantas estrelas tem uma constelação? Com 30 crianças e 1 estrela por criança por dia, ela enche no 1º dia? O contador "A turma acendeu 18 estrelas." é do dia ou acumulado?
  2. O HTML desenha em `olho` a 35% o **contorno inteiro** do trem, com vértices sem estrela (x = 350 e 410, y = 150). É uma fração visual: mostra o que falta acender.
  3. S3 aceitou "Ver quem" fora da projeção, mas `02` diz "É anônimo: ninguém vê quem acendeu". Existe ou não uma vista "Ver quem", e para quem?
  4. A cor do texto `#C9D3DC` não é token. A tipografia da versão projetada não tem tamanho mínimo.
- **Correção:** fixar o tamanho da constelação (por exemplo, = nº de crianças × 5 dias) e o escopo do contador. Desenhar só as linhas entre estrelas já acesas. Eliminar "Ver quem" ou especificá-lo só para o professor, e registrar a decisão na discussão. Trocar `#C9D3DC` por um token. Fixar o tamanho mínimo para projeção (≥ 48 px a 1080p).

### E19 · Painel do professor: a regra contradiz o exemplo, e "sessão" tem dois sentidos
- **Severidade:** importante
- **Onde:** `03` §13; HTML l. 421–459.
- **Problema:**
  1. A regra diz "O rótulo vem **sempre da ontologia**, com subtítulo em linguagem de sala" (C10), mas o exemplo ("Ana · Esperar o sinal") tem título em linguagem de sala e o construto só na camada 2, como D-17 manda. A regra de C10 ficou antiga.
  2. "Sessão" é sinônimo de voo em `02` ("Voo: uma sessão"), mas em `03` §13 "9 sessões de Sinal Aberto" significa 9 partidas desse jogo. O SVG do HTML diz "ao longo de **9 voos**".
  3. Os chips "avanço", "sinal" e "acesso" não estão em nenhum `.md`. "avanço" é avaliativo, e não há chip para estabilidade ou queda. O chip "sinal" é âmbar **sem ícone**, contra `03` §5 regra 1 ("sinal de atenção usa `sol` **com ícone**") e regra 4.
  4. O cartão do Bruno no HTML não tem "Se o contexto não explica: observe…" nem o "De onde veio" que `03` exige.
  5. O estado do cartão depois de "Confirmo", "Não observei" e "Já encaminhado" não está desenhado (some? fica marcado? pode desfazer?).
  6. `sol` é "só recompensa" (D-10, `03` §5), mas também é a cor do sinal de atenção no painel.
- **Correção:** reescrever a regra de C10 como "título = ação observável aprovada na ontologia (rótulo de sala); construto técnico na camada 2". Usar "partida" para o jogo e "voo" para a sessão. Especificar o conjunto de chips com ícones e os estados pós-ação. Escrever a exceção de `sol` para o painel ou trocar a cor do sinal.

### E20 · A tipografia se contradiz e não diz o que acontece a 150% num celular
- **Severidade:** importante
- **Onde:** `03` §6.
- **Problema:**
  1. "Entrelinha de 1,5" contra a escala 28/40 (1,43), 36/44 (1,22) e 20/28 (1,4).
  2. Espaço entre letras "+3%"; o HTML usa 0,02em, 0,03em e 0,04em.
  3. Pesos da letra da criança não definidos (o HTML usa 700 em botões e títulos).
  4. Num celular de 360 px, com escala de 150%, a instrução de 28 px vira 42 px: cerca de 15 caracteres por linha ao lado do Bot de 52 px. "TOQUE QUANDO APARECER O CÍRCULO." ocupa 3 linhas, a moldura de baixo cresce e o palco, que é medido em mm, fica sem espaço.
  5. "Letra bastão" significa caixa alta em §6, mas em §3 descreve um desenho de letra sem serifa.
- **Correção:**
  - Fixar a entrelinha por nível (1,5 só para corpo).
  - Definir o tracking em em e os pesos.
  - Regra de reflow: a moldura tem altura máxima, e a instrução quebra em até 2 linhas e depois rola, ou o Bot some da linha da instrução a partir de 125%.
  - O palco reserva primeiro a área mínima do CIATec, e a moldura se ajusta ao que sobra. Abaixo disso, o aparelho é registrado como "abaixo da tela mínima".
  - Usar "caixa alta" em §6 e "sem serifa" em §3.

### E21 · Especificação do Bot insuficiente para o ilustrador
- **Severidade:** importante
- **Onde:** `03` §4 Forma e Expressões; HTML l. 544–569.
- **Problema:**
  - **Sossegado:** "ovais retos, semiabertos" é contraditório. O HTML desenha barras chatas, que se leem como olhos fechados, "dormindo" ou "desligado", justamente o que o Ninho quer evitar ("sem parecer desligado"). Com a boca "linha reta" igual à do Atento, as duas expressões diferem só nos olhos.
  - **Curioso:** "um olho maior". Qual? É fixo?
  - **Pensando:** "para cima e para o lado". Qual lado? O HTML mostra os dois olhos deslocados, sem direção clara.
  - **Casco:** não há regra de contorno (ver E7) nem proporções (casco : visor : asa).
  - **Tamanho:** não há tamanho do Bot por contexto (moldura, Pouso, Caminho, Ninho, Céu). "Mesmo tamanho em todos os microjogos" não diz qual.
  - **Logotipo:** o estudo desenha os olhos do "OO" vazados, e os olhos do Bot atento são ovais cheios. O logotipo e o rosto deixam de ser a mesma coisa (`03` §3: "O nome é o rosto do produto").
- **Correção:** uma folha de modelo (turnaround) com a grade de construção, proporções, traço, as 5 expressões com coordenadas de olhos e boca em uma grade do visor (por exemplo, 16×10 "pixels de luz", que também resolve a matriz de LED), e tamanhos por contexto. Redesenhar o Sossegado como ovais com a pálpebra superior reta, mantendo a pupila de luz visível, e diferenciar a boca (curva leve). Alinhar os olhos do logotipo com os do Atento.

### E22 · A HIP-2 testa um braço que D-05 proíbe
- **Severidade:** importante (S1 dado como aceito)
- **Onde:** `01` HIP-2 ("moldura que mostra **contagem de acerto** no treino"); D-05 *invariante* ("o Pouso também não mostra contagem de acertos"); `01` regra "nenhuma variante… não segura"; `03` §5, candidatos de "2 tipos de feedback" (nenhum mostra acerto).
- **Problema:** a hipótese descreve um braço que viola um invariante, e o ponteiro "ver `03` §5" aponta para variantes diferentes.
- **Correção:** reescrever a HIP-2 com os braços de `03` §5: (A) só retorno de competência × (B) retorno + descrição verbal, com desfecho em conclusão.

### E23 · Os braços do PP3 diferem em mais do que a adaptação
- **Severidade:** importante
- **Onde:** `03` §4, Celebrar ("fim de microjogo, fim de voo, marco de coleção") contra a variante não adaptativa ("celebra só no fim do voo").
- **Problema:** fim de microjogo e marco de coleção não são decisões do gêmeo; acontecem nos dois braços. Se só o braço adaptativo os celebra, a comparação mistura adaptação com quantidade de celebração, e o brief afirma "mesma linguagem".
- **Correção:** mover "fim de microjogo" e "marco de coleção" para comportamento **comum** aos dois braços. "Celebrar" adaptativo, se existir, precisa de um disparo do gêmeo; senão, sai da lista de comportamentos adaptativos.

### E24 · A fileira de penas não tem regra de crescimento
- **Severidade:** importante
- **Onde:** `03` §11 Fileira de penas; HTML `.penas`.
- **Problema:** depois de 100 dias de voo, a fileira tem 100 penas. Ela quebra linha, rola, agrupa ou comprime? Em que tela fica? (Ver E4.) A pena "nova" do HTML (contorno `sol`) não está nos `.md`.
- **Correção:** definir o contêiner (altura máxima, agrupamento visual sem número, por exemplo em ramos de 10 penas que viram um galho), a tela onde a fileira aparece e o destaque da pena do dia (forma, não só cor).

### E25 · O alto contraste continua `[A FAZER]`, mas é citado como existente
- **Severidade:** importante (regressão de S15)
- **Onde:** `03` §5 ("Alto contraste `[A FAZER]`"); `04` Acessibilidade ("token de alto contraste na moldura"); discussão S15 ("aceito").
- **Correção:** entregar o conjunto, ou marcar S15 como "aceito em parte" na discussão e tirar a afirmação de `04`.

### E26 · O Bot pode convidar para outra faixa, mas o convite é "sobre jogos novos"
- **Severidade:** importante
- **Onde:** `03` §4 Provocar: no "O que o gêmeo decide", "a criança está pronta para **outra faixa de dificuldade**"; no Limite, "o convite é sobre jogos novos, **não sobre o nível**".
- **Problema:** as duas colunas se contradizem. O dev não sabe o que dispara o convite.
- **Correção:** "Gatilho: o gêmeo quer introduzir um microjogo que a criança ainda não jogou. A dificuldade dentro de um jogo muda entre blocos sem convite."

---

## Menores

### E27 · Termos antigos e CSS órfão
- **Onde e o quê:**
  - HTML l. 37 comentário "**Modo calmo**"; classe `.calmo`; ids `t-calmo` e `t-calmo-desc`.
  - `paleta.json`: tokens `calmo-papel`, `calmo-ceu`, `calmo-sol`, `calmo-folha` e usos "no **modo calmo**", com eco em `resultado-contraste.txt`.
  - `paleta.json`: o par `lavanda-tinta`/`lavanda-claro` descrito como "ajuda / **tente de novo**", expressão que soa como fracasso e não está no repertório.
  - CSS sem uso no HTML: `.dias` e `.dias span` (calendário com dias da semana e **casas tracejadas vazias**, o antigo "Dias de voo" que S7 removeu), `.duracao`, `.par`, `.peca`, `.sinal-espera`, `.grid-3`, `.app.paisagem`, `.origem`.
  - A discussão (S8) fala em "'Calmo' redesenhado"; os arquivos dizem "Sossegado". A personalidade "calmo × apático" em `03` §2 está correta, mas vale um glossário para não confundir com a expressão.
- **Correção:** renomear para `suave` no HTML, no JSON e no resultado (rodar o script de novo), apagar o CSS órfão e atualizar a discussão.

### E28 · Falta o componente que mais aparece nas regras
- **Onde:** o HTML não mostra nenhum dos componentes que os `.md` especificam como novos ou críticos: bloco de **treino** com barra de duração e pista, botão par, Pausa, Ninho, Selo de peça (escolha entre 3), Do meu jeito, Aviso de dados, Câmera ligada, Troca de criança, Turno e Barra compartilhada.
- **Correção:** acrescentar pelo menos o treino com pista, a Pausa → Ninho e o Selo de peça, porque são os três em que o estudo mais mudou.

### E29 · Acessibilidade técnica do HTML
- **Problemas:**
  1. Sem `<!doctype html>`, `<html lang="pt-BR">` e `<meta charset="utf-8">`. Aberto como arquivo local, a página roda em quirks mode, o leitor de tela lê com voz em inglês e a codificação dos acentos depende de detecção.
  2. `aria-label` em `<span class="btn-ic">`, `<div class="plano">` e `<div class="penas">` sem `role`: é ignorado pelas tecnologias assistivas. Usar `role="img"` ou `role="group"`.
  3. `h4`/`h5` dentro dos mockups antes do `h3` da seção quebram a hierarquia de títulos. Usar `<p>` estilizado ou `role="presentation"`.
  4. O botão de alternância muda o texto **e** o `aria-pressed` ao mesmo tempo. Manter o rótulo fixo ("Modo suave") e variar só o estado. A descrição `#t-calmo-desc` não está ligada por `aria-describedby`.
  5. `.tabela` com `overflow-x:auto` e tabela de `min-width:620px`: a região rolável não tem `tabindex="0"`, `role="region"` nem `aria-label`.
  6. A animação `.pisca` é infinita e não tem controle de pausa, contrariando a regra que a própria página documenta (`03` §9, "todo loop com mais de 5 s tem pausa"). Só para com reduced-motion.
  7. `.btn-p` (~35 px) e `summary` (32 px) ficam abaixo de 44 px.
  8. O ipê do Caminho (`#D9A7C7`, 1,87:1) e `#0F151B` não são tokens. Para decoração não há exigência de contraste, mas são cores fora do sistema.

### E30 · Largura de 400 px
- **Verificação por leitura do CSS:** funciona. O corpo tem 368 px úteis. `.telas` (minmax 280) cai para 1 coluna, `.grid-5` para 3 colunas (~100 px cada), `.comportamentos` para 1, `.swatches` para 2, `.tendencia` para 1, e as tabelas rolam dentro do contêiner, sem rolagem horizontal da página. O `.selo-palco` (nowrap, 11 px) cabe no palco de ~328 px.
- **Ressalvas:** a região rolável não é focável (E29.5). Os mockups ficam com alvos de 44 px e textos de 15–16 px, o que reforça E8. O texto do Céu no SVG renderiza a ~11 px.

### E31 · Regras de tom que as próprias falas não cumprem
- **Problemas:**
  1. "Até 8 palavras": a fala do Primeiro voo ("O VUOO guarda como você joga: o que você tocou e quanto tempo levou.", 14 palavras) e a da câmera ("Agora a câmera vai olhar para onde você olha.", 9) passam do limite.
  2. "Um verbo por frase" é inviável: "Toque quando aparecer o círculo." tem dois verbos. Reescrever como "uma ação pedida por frase".
  3. "A câmera vai olhar" é personificação, que a regra 3 proíbe. Sugestão: "A câmera vai ver para onde você olha."
  4. "A professora deixou assim." é texto com gênero fixo; transformar em variável {professor/professora} ou "Sua turma está assim."
  5. "Vamos mais devagar." está na coluna "nunca", mas "Vamos para o próximo jogo." é a fala-modelo. Explicar o critério ou trocar por "Agora: próximo jogo."

### E32 · Pictogramas ambíguos
- **Onde:** `03` §7.
- **Problemas:**
  1. "Forma preenchida em `tinta` com contorno de 3 px arredondado" é ambíguo: o contorno tem a mesma cor do preenchimento? A grade é de 48 com raio 4 px, mas os pictogramas do HTML usam grade de 24, só contorno, em `contorno`.
  2. Nomes divergentes: o botão se chama "Ouvir", o pictograma "repetir instrução", e no aviso de dados aparece "Ouvir de novo".
  3. Faltam pictogramas para câmera (aparece só em estados), Do meu jeito, Parar por hoje, peça, pena e Caminho.
- **Correção:** um inventário de pictogramas com nome canônico igual ao rótulo do botão, e um exemplo de construção.

### E33 · Inconsistências pequenas de regra
1. D-09: "O go/no-go **da moldura** usa forma + cor". O go/no-go está no palco, e lá quem decide é o protocolo. Remover ou reescrever.
2. Tokens `03` §5: `superficie` = "fundo padrão **do palco**", contra §11 ("cor do palco: do protocolo"). Escrever "fundo padrão do palco **em blocos de treino**".
3. Componente Turno: "moldura na **cor da criança** da vez", mas não há tokens de cor por criança, e a cor não pode ser o único sinal. Ponte em Dupla: "a outra **confirma a cor**" usa só a cor.
4. C8 ("aviso de fim só entre blocos") não aparece em `02` §6 nem em `03` §11.
5. Pensando: "pulsando devagar" sem período. Fixar (por exemplo, 2 s, senoidal), bem abaixo de 3 Hz.
6. `03` §10: o volume padrão "baixo" não tem valor (LUFS/dB relativo por canal). Também não diz que música existe, se ela vem desligada.

---

## Regressão: o que a discussão das rodadas 1–2 diz que mudou e não mudou

| Achado | A discussão diz | Estado nos arquivos |
|---|---|---|
| C21 | superlativos trocados | **não aplicado no HTML** (E11.5) |
| C24 | faixa de 6 a 12; público e privado | **não aplicado no HTML** (6 a 11, só pública) |
| C3 | Modo suave e tema não entram no palco | `.md` ok; **HTML viola** (E5) |
| C8 | aviso de fim só entre blocos | **ausente** (E33.4); mockup com Bot piscando e balão durante a medida (E12) |
| C10 | rótulo da ontologia + subtítulo de sala | regra antiga mantida, contradiz o exemplo e D-17 (E19.1) |
| S1 | nenhum braço inseguro | **HIP-2 viola** (E22) |
| S3 | "Ver quem" nunca em projeção | os arquivos dizem que o Céu é anônimo; "Ver quem" não existe (E18.3) |
| S5 | fim de medida: "o jogo das bolhas" | só `02` §13 usa; o resto usa "Bolhas" (E13) |
| S5, S9 | números nunca falados | **tabela de falas põe {n} em voz** (E1) |
| S8 | expressão não contingente | gesto no acerto e *pensando* após erros (E2) |
| S9 | recuo e pausa nunca em voz alta | pausa, pular, pista e convite em voz (E1) |
| S15 | token de alto contraste | `[A FAZER]` (E25) |
| S16 | aviso narrado também no "Sobre" | não aparece em `03` (E4) |
| S17 | "Modo calmo" → "Modo suave" | `.md` ok; **HTML, `paleta.json` e resultado ainda dizem "calmo"** (E27) |
| S19 | rótulos e ordem uniformizados | ordem do botão par inconsistente (E15); padrões de 2 voos + aparelho compartilhado se anulam (E4) |
| S21 | todas as divergências `.md` × `.html` alinhadas | **falso**: E5, E11, E12, E18, E19, E27 |
| C19, S8 | boca de luz | **aplicado** no `.md` e no HTML |
| C20, S6, S7 | coleção sem contador; penas sem calendário | aplicado nos `.md`; CSS `.dias` órfão no HTML; conflito com a regra de vínculo (E10) |
| C2, C5, C6, C7, C9, C11–C18, C23, C25–C27, S2, S4, S10–S14, S18, S20 | — | aplicados (com as ressalvas de E19 e E23) |

---

## O que falta para virar especificação: entregáveis mínimos

1. **Mapa de telas e fluxo** (E4): inventário de telas da criança, professor, gestor e família, com cada encruzilhada resolvida (Pular, Pausa, 2º voo, limite, Parar por hoje → troca, onde ficam o Caminho e as penas).
2. **Matriz evento → reação** (E1, E2, E3): para cada evento, uma linha com Bot (estado), antena, som, voz (com e sem fone), texto, pictograma e duração. Ela é a fonte única para dev, animador e roteirista.
3. **Máquina de estados do Bot** (E3): estados, entradas, transições, prioridade, durações e curvas, variantes para Modo suave e reduced-motion, e variante não adaptativa (E23). Formato pronto para Rive.
4. **Folha de modelo do Bot** (E21): turnaround, proporções, traço, grade de luz do visor com as 5 expressões em coordenadas, tamanhos por contexto, compatível com a matriz de LED.
5. **Tokens em JSON** (formato W3C Design Tokens ou equivalente) para cor (padrão, suave, alto contraste), espaço, raio, elevação, foco, tipografia (família, tamanho, entrelinha, tracking, peso), movimento (durações e curvas) e som (volumes). Gerados de um só arquivo, que também alimenta o `contraste.py` (E6, E7, E8, E20).
6. **Biblioteca de componentes com estados**: padrão, pressionado, foco, desabilitado, carregando, feito, pulado, offline. Anatomia e medidas de cada componente da tabela de `03` §11, em 360 px e em tablet, retrato e paisagem.
7. **Tabela de strings com ID** (E13): parâmetros, plural, versão falada, canal e gatilho. Uma só, importada pelo HTML.
8. **Inventário de pictogramas** (E32), com nome canônico = rótulo do botão.
9. **Layout do palco × moldura com números** (E20): alturas mínima e máxima da moldura, área mínima do palco em mm (depende do P10), comportamento a 125% e 150%.
10. **Painel**: telas da turma e do cartão, conjunto de chips com ícones, estados pós-ação dos três botões, estado vazio ("sessões insuficientes"), estado "aguardando sincronização" (E19).
11. **Critérios de aceitação testáveis** para as invariantes. Exemplos: "nenhum pixel do palco muda com tema ou modo" (E5); "nenhuma string com {n} é sintetizada em voz" (E1); "nenhuma transição do Bot tem como entrada acerto ou erro" (E2).
