---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-linguagem
etapa: 05-decisoes
status: em revisão
atualizado_em: 2026-10-27
---

# 05 · Registro de decisões

> **Precedente (2026-11-05).** Decisões tomadas no enquadramento do projeto de pesquisa. O produto VUOO é independente dele; estas decisões valem para o produto só quando forem adotadas nos documentos da raiz de vuoo-microjogos. Ver [LEIAME](LEIAME.md).

O dono do produto delegou as decisões. Cada uma está registrada como discussão: pergunta, opções, argumentos, decisão e custo de voltar atrás. **Reversibilidade:** *barata* = token ou texto; *média* = componentes ou telas; *cara* = identidade ou arquitetura. Decisões revistas depois das rodadas de revisão estão marcadas **[revista]**, com o achado que motivou a mudança (ver `revisao/discussao-rodadas-1-2.md`).

**Natureza das decisões:** este estudo é insumo do co-design (OE6) e das consultorias do PIPE. Decisões de identidade (D-02, D-03, D-09, D-11) são **propostas para o 1º ciclo de co-design**, com critério de aceite. Decisões de segurança (D-05, D-06, D-07, D-12, D-17, D-19, D-20) são **invariantes**: o co-design pode mudar a forma, mas não o que elas protegem.

---

### D-01 · De quem é a linguagem
- **Opções:** (a) marca VUOO com endosso do CIATec; (b) identidade CIATec com o VUOO dentro; (c) marca dupla.
- **Decisão: (a).** O VUOO é o produto comercial que chega à escola; o CIATec é plataforma aberta de ciência; a FAPESP proíbe similaridade e exige autorização para o logo (I1, I3); marca dupla faria a criança ver duas identidades.
- **Reversibilidade:** média.

### D-02 · Metáfora central · *proposta para co-design* [revista: C17]
- **Opções:** voo/trajetória; jardim; espaço; cidade.
- **Proposta: voo/trajetória.** Está no nome e no título do projeto; rende Caminho, penas, Pouso, Ninho e Céu com um vocabulário só. O jardim sugere cuidado clínico; o espaço é clichê com fundo escuro; a cidade é complexa de ilustrar.
- **Cuidado:** "voo" é nome próprio da sessão, nunca verbo ou figura para a criança ("Jogar de novo", não "Voar de novo") (S11).
- **Critério de aceite no co-design:** professores entendem o vocabulário sem explicação e não o acham infantil para o 4º e 5º ano.

### D-03 · Mascote · *proposta para co-design* [revista: C19, S8]
- **Opções:** pássaro; robô; forma abstrata.
- **Proposta: robô com asas**, com **olhos e boca de luz no visor**. A boca é recomendada pela pesquisa (R33) e não custa nada ao animatrônico, porque o visor é uma tela. A versão anterior, sem boca, se apoiava numa afirmação sem fonte e foi corrigida.
- **Critério de aceite:** HIP-4 (≥ 80% de compreensão das expressões no 1º ano), testada no estudo de usabilidade do CIATec antes de fechar a arte.

### D-04 · Quanto do Duolingo copiar
- **Decisão:** a forma (sessão curta, rotina fixa, caminho, personagem, fim claro), não o motor (aversão à perda, comparação, recompensa variável).
- **Argumento contrário:** sem aversão à perda, a retenção pode cair. **Resposta:** a responsabilidade pelo acesso ao aparelho é da escola, e o professor recebe avisos de acesso. **[revista: S3]** O Céu da turma **não** é instrumento de pressão de retorno: ele foi redesenhado sem prazo e sem falta.

### D-05 · Recompensar desempenho ou participação · *invariante*
- **Decisão: participação.** Recompensa por acerto ou velocidade contamina a medida e cria comparação. O retorno de competência é imediato e informativo (o alvo reage), não moeda (R27). **[revista: S5]** O Pouso também não mostra contagem de acertos.

### D-06 · Ofensiva · *invariante* [revista: S7]
- **Decisão:** uma pena por dia de voo, numa **fileira que só cresce**, sem dias da semana, casas vazias ou total numérico. Uma grade de calendário com casas vazias mostra a ausência.

### D-07 · Coleção · *invariante* [revista: C20, S6]
- **Tensão:** R28 pede coleção inesperada (recompensas esperadas e contingentes enfraquecem a motivação intrínseca, Deci et al. 1999); I5 proíbe sorteio; S6 aponta o "Faltam N" como gancho.
- **Decisão:** peça a cada **3 dias de voo**, **sem contador e sem anúncio**, com escolha entre **3 peças equivalentes**. Inesperada para a criança, determinística para o sistema, sem raridade. Por dia de voo, para que jogar mais no mesmo dia não acelere nada.
- **A versão anterior** (previsível, com "Faltam 2 voos") contrariava a evidência citada e foi trocada.

### D-08 · Social: competição, cooperação ou colaboração [revista: C12, C13]
- **Decisão:** sem competição. **Pertencimento assíncrono** no v1 (Céu da turma, uma estrela por criança por dia, sem prazo). **Componentes de colaboração** já na biblioteca (turno, barra compartilhada, pictogramas entre pares, Bot mediador), para os jogos do CIATec.
- **"Classificações" do CIATec:** pergunta aberta ao CIATec, e não decisão deste estudo (`99-pendencias.md`).

### D-09 · Vermelho · *proposta para co-design*
- **Decisão: sem vermelho na moldura.** Erro não é perigo (R14); vermelho saturado em grande área é aversivo para parte das crianças autistas (R2); no painel, vermelho vira alerta de diagnóstico. No palco de medida, quem decide é o protocolo; a recomendação ao CIATec é forma + cor também lá (E33).

### D-10 · Âmbar na marca
- **Decisão:** `sol` só em áreas pequenas e só para recompensa.

### D-11 · Tipografia · *proposta para co-design*
- **Decisão:** Andika para a criança, Atkinson Hyperlegible Next para o adulto. Caixa alta configurável. Nenhuma das duas tem estudo com crianças; o que tem evidência é espaçamento e tamanho, que estão fixados.

### D-12 · O Bot durante a medida · *invariante* [revista: C8]
- **Decisão:** fora do palco, imóvel e calado durante todo bloco de medida, nos dois braços do PP3. Não apresenta estímulos medidos (a sequência de Luzes em Ordem é apresentada pelo palco).

### D-13 · Celular ou tablet [revista: C7]
- **Decisão:** moldura responsiva de 360 px a 10". **Palco de medida em milímetros**, com calibração por DPI, orientação travada e tela mínima definida pelo CIATec. Aparelho registrado por sessão.

### D-14 · Limite diário [revista: S19]
- **Decisão:** padrão de 2 voos por dia, definido pelo professor, com **teto técnico de 3**. Em modo aparelho compartilhado (padrão), o Pouso só oferece "Parar por hoje".

### D-15 · Pictogramas
- **Decisão:** conjunto próprio, porque a licença do ARASAAC proíbe uso comercial. **[revista: S15]** Os pictogramas da moldura podem ser trocados pelos símbolos que a criança já usa no AEE.

### D-16 · "Risco" ou "sinal" [revista: C4]
- **Decisão:** na interface, "sinal de atenção". Nos relatórios FAPESP, a tabela de correspondência "alerta de risco (projeto) = sinal de atenção (interface)". O sinal vem sempre com contexto, encaminhamento e botões de confirmação (D-17).

### D-17 · O cartão do professor: norma ou progresso individual? · *invariante* (nova; C4 × S4)
- **Tensão:** o gêmeo classifica "abaixo, dentro, acima do esperado para a idade", e o PP4 mede tempo e acurácia da identificação de risco (C4). Comparação normativa com nome de construto num cartão com nome de criança vira rótulo (S4).
- **Decisão:** duas camadas. **Abertura:** ação observável + evolução da criança em relação a ela mesma. **Detalhe:** construto da ontologia, instrumento, sessões, faixa para a idade **neste jogo** com incerteza, e o que o jogo mede e não mede. **Sinal de atenção:** só depois de N sessões, contexto primeiro, encaminhamento, botões "Confirmo / Não observei / Já encaminhado". Rodapé de limite em todo cartão, interruptor de sugestões, painel nunca projetável. **Comparação com a turma: proibida.**
- **Risco aceito:** a camada dupla pode deixar a identificação mais lenta que um semáforo. **Mitigação:** levar 2 ou 3 variantes de vocabulário ao F4.1 e ao co-design, medindo tempo e acurácia de identificação antes do F4.3 (C4).

### D-18 · Governança e propriedade intelectual (nova; C14)
- **Decisão:**
  1. Os jogos do CIATec continuam acessíveis gratuitamente fora do VUOO.
  2. Rodar dentro do VUOO depende do comitê gestor do CIATec.
  3. **Personagem, marca e arte do Bot** precisam entrar no acordo de PI (F1.1, E5.5), que hoje cobre só registros INPI, SDK e Wemoga Eye.
  4. A animatrônica é projeto do CIATec. A compatibilidade com o Bot é requisito compartilhado.

### D-19 · A plataforma sabe quem tem Plano Educacional Individualizado? · *invariante* (nova; S2)
- **Decisão:**
  1. A plataforma **não sabe diagnóstico**. A base operacional não guarda laudo nem rótulo diagnóstico (vuoo, ética).
  2. A plataforma **pode saber se a criança tem Plano Educacional Individualizado**, informado pelo AEE, porque a interface pedagógica gera saídas para o plano (OE7).
  3. Esse dado é tratado como **dado sensível de criança**: base legal declarada, RIPD, acesso só do professor regente e do AEE, nunca visível à criança ou aos colegas, nunca no gestor abaixo do nível de diretoria.
  4. Uso "por perfil" na pesquisa só com consentimento específico (TCLE dos responsáveis e assentimento da criança).
- **`[A CONFIRMAR]`** com a assessoria jurídica do PIPE: a base legal (art. 11, II, "b", política pública, ou consentimento) e o RIPD.

### D-20 · Palco de medida e moldura · *invariante* (nova; C3, C6, C7, C8)
- **Decisão:** toda tela de microjogo tem um palco de medida definido pelo protocolo do CIATec e congelado a partir do PP1. A linguagem vive só na moldura. Tema, Modo suave, alto contraste, escala de texto, Bot e variantes A/B/n não entram no palco de medida. Configurações ativas são registradas por sessão como covariáveis.
- **Por quê:** é a única forma de a linguagem não ameaçar os critérios psicométricos do PP1 e do PP3.
- **Reversibilidade:** cara. É a decisão mais importante deste estudo.

### D-21 · Canal de voz por configuração de fone · *invariante* (nova; E1)
- **Tensão:** voz ajuda quem não lê; voz em sala sem fone expõe a adaptação de uma criança aos colegas (S9).
- **Decisão:** o professor configura cada aparelho como `Fone: não` (padrão) ou `Fone: sim`. Sem fone, só são faladas as falas iguais para todos (nome do jogo, instrução, avisos, fim). Pista, recuo, pausa, pular, convite, Ninho e ajustes ficam em texto e pictograma. **Número nunca é falado.** Tabela em `06` §3.

### D-22 · A antena do Bot é só emoção (nova; E3)
- **Decisão:** a antena indica só o estado emocional do Bot. Estados do sistema (câmera ligada, offline) ficam na moldura, com pictograma e rótulo. Misturar os dois na mesma luz faria "curioso" e "câmera ligada" parecerem iguais.

### D-23 · Fonte única para fluxo, falas e Bot (nova; E4, E13, S21)
- **Decisão:** `06-especificacao-base.md` é a fonte única de fluxo, falas e reações do Bot. Os demais arquivos apontam para ele. A página visual ilustra e, se divergir, o `.md` prevalece.
- **Por quê:** a rodada 3 mostrou que manter a mesma especificação em três lugares produziu divergência mesmo depois de uma revisão dedicada a alinhar.
