# Pesquisa B: Neurodivergência, acessibilidade e linguagem visual/interativa do VUOO

> Escopo: crianças de 6 a 11 anos (1º ao 5º ano, rede pública de SP). O foco são estudantes com TEA, TDAH, dislexia e TDC (Transtorno do Desenvolvimento da Coordenação), mas o produto atende a turma inteira (UDL, visão transdiagnóstica). São microjogos de 60 a 90 s que medem e treinam tempo de reação, coordenação, atenção e funções executivas, usados em tablet ou computador na escola, com o companheiro "VUOO Bot".
> Data da pesquisa: outubro de 2026. Método: busca web (WebSearch/WebFetch) em artigos revisados por pares, guias oficiais (W3C, gov.uk) e guias da indústria de games.

## Como ler a força da evidência

- **[FORTE]**: meta-análise ou revisão sistemática com achado consistente, ou norma técnica consolidada (WCAG).
- **[MODERADA]**: estudos experimentais isolados ou pequenos, ou revisões com achados heterogêneos.
- **[ESPECIALISTA]**: guias de prática, consenso de designers ou especialistas, ou relatos de pessoas autistas, sem teste controlado.

Uma ressalva geral: quase toda a literatura sobre design para crianças neurodivergentes usa amostras pequenas. Mesmo onde há estudos, a maioria das recomendações abaixo é de nível moderado ou de especialista. Isso reforça a necessidade de testar com as próprias crianças (ver R40).

---

## 0. Tensão central do VUOO: medir vs. acomodar

Os jogos **medem** tempo de reação e coordenação. Várias acomodações recomendadas mudam a própria medida: mais tempo, alvos maiores, velocidade reduzida, remoção do cronômetro. Se essas acomodações forem aplicadas sem registro, os dados ficam contaminados. Se forem negadas, o produto exclui justamente o público-alvo.

- **R0.** Separe "configurações de apresentação" de "parâmetros da tarefa".
  - **Configurações de apresentação** não alteram a medida: cor, som, animação decorativa, tipografia, narração, mascote. São livres para personalizar.
  - **Parâmetros da tarefa** alteram a medida: tamanho de alvo, janela de tempo, velocidade. São versionados, registrados junto de cada sessão como metadado e comparados apenas entre sessões com o mesmo perfil.
  - O relatório para o professor deve mostrar o desempenho **relativo à própria criança** (progresso intraindividual), não ranking.

---

## 1. Processamento sensorial no TEA (e na turma inteira)

### Evidência

**[FORTE] Diferenças sensoriais são centrais no TEA.**
- A meta-análise de Ben-Sasson et al. (2009, 14 estudos) e sua atualização (2019, 55 estudos, 4.606 pessoas autistas) encontraram efeitos grandes de hiper-responsividade, hiporresponsividade e busca sensorial em comparação com controles típicos.
- A **hiper-responsividade** é o padrão que melhor distingue o TEA de outros grupos clínicos.
- A diferença é maior na faixa de **6 a 9 anos**, exatamente o público do VUOO.
- Como os perfis são opostos (hiper e hipo), não existe um único "nível certo" de estímulo. Personalização é obrigatória, e não um extra.

**[FORTE] Intolerância ao som é muito comum.** A meta-análise de Williams, Suzman & Woynaroski (2021, *Ear and Hearing*) estimou a prevalência de hiperacusia no TEA em cerca de 41% (questionário) e 27% (medida observacional). A prevalência ao longo da vida de "baixa tolerância sonora" fica entre 50% e 70%.

**[MODERADA] Preferência de cor.**
- Grandgeorge & Masataka (2016, *Frontiers in Psychology*) testaram 29 meninos com TEA (4 a 17 anos) e 38 controles.
- Os meninos autistas preferiram menos o **amarelo** e mais o **verde** e o **marrom**. Os autores atribuem isso à hipersensibilidade: o amarelo, de alta luminância, seria sobrecarregante.
- Limites: amostra pequena, só meninos, ambiente clínico, sem replicação robusta. Use como sinal para evitar amarelo saturado em grandes áreas, e não como regra de paleta.

**[MODERADA] Ambiente visual carregado reduz atenção e aprendizagem em crianças pequenas, inclusive típicas.**
- Fisher, Godwin & Seltman (2014, *Psychological Science*): crianças da educação infantil numa sala muito decorada ficaram mais tempo fora da tarefa e aprenderam menos.
- Crítica (Imuta & Scarf, 2014): parte do efeito pode ser novidade, e não irrelevância.
- Implicação para a turma toda: fundo e decoração competem com o estímulo-alvo, o que é crítico em tarefas de atenção e tempo de reação.

**[MODERADA] Previsibilidade é valorizada.** Diretrizes Delphi com especialistas para jogos destinados a crianças autistas (Alves et al., 2021) destacam que o "comportamento previsível e constante dos componentes tecnológicos" é muito apreciado. A revisão de mais de 70 artigos sobre jogos sérios para crianças autistas de 6 a 12 anos (SAI, 2023) agrupa os princípios em estética, experiência e feedback.

**[FORTE, norma] WCAG 2.2, critérios relevantes.**

| Critério | Nível | Exigência | Implicação para o VUOO |
|---|---|---|---|
| 1.4.1 Uso de cor | A | Cor não pode ser o único meio de informação | Certo/errado e times também por forma ou ícone |
| 1.4.3 Contraste mínimo | AA | 4,5:1 para texto, 3:1 para texto grande | Todo texto e instrução |
| 1.4.11 Contraste não textual | AA | 3:1 para componentes e gráficos | Alvos do jogo e botões |
| 1.4.12 Espaçamento de texto | AA | Suportar entrelinha 1,5, espaço entre letras 0,12em e entre palavras 0,16em | Modo leitura |
| 2.2.1 Tempo ajustável | A | Permitir desligar, ajustar ou estender limites de tempo (exceção: tempo essencial, como em tempo real) | Os jogos de TR se enquadram na exceção; menus e instruções não |
| 2.2.2 Pausar, parar, ocultar | A | Movimento automático com mais de 5 s precisa poder ser pausado | Animações de fundo, mascote em loop |
| 2.3.1 Três flashes | A | No máximo 3 flashes por segundo | Explosões e efeitos de acerto |
| 2.3.3 Animação por interação | AAA | Movimento disparado por interação pode ser desativado | Parallax, zoom, tremor de tela |
| 2.5.5 Tamanho do alvo (aprimorado) | AAA | 44×44 px CSS | Mínimo prático para crianças |
| 2.5.8 Tamanho do alvo (mínimo) | AA | 24×24 px CSS | Mínimo legal, insuficiente para crianças |

**[ESPECIALISTA] Guias de design.**
- **W3C COGA, *Making Content Usable for People with Cognitive and Learning Disabilities*.** São 8 objetivos. Os padrões mais pertinentes:
  - 4.2.3 design visual consistente
  - 4.4.4 linguagem literal
  - 4.4.9 uma instrução por vez
  - 4.5.1 controles e conteúdo não se movem inesperadamente
  - 4.5.9 evitar perda de dados e "timeouts"
  - 4.5.10 dar feedback
  - 4.6.1 limitar interrupções
  - 4.6.3 evitar excesso de conteúdo
  - 4.9.1 deixar o usuário controlar quando o conteúdo se move
  - 4.9.3 suportar simplificação
  - 4.9.4 interface personalizada e familiar
- **UK Home Office, pôster "Designing for users on the autistic spectrum" (Karwai Pun, 2016).**
  - Fazer: cores simples, linguagem clara e literal, layouts simples e previsíveis, botões descritivos, consistência.
  - Não fazer: cores vivas e contrastantes demais, figuras de linguagem e expressões idiomáticas, blocos de texto, botões vagos ("clique aqui"), layout imprevisível.
  - Os pôsteres de dislexia e motor complementam: imagens e diagramas, alinhamento à esquerda, alvos grandes, nada de interações que exijam precisão ou movimento fino.
- **Game Accessibility Guidelines.** Básico: sem flashes ou padrões repetitivos, velocidade ajustável, alvos grandes e espaçados, linguagem simples, tutorial interativo, fonte legível por padrão. Intermediário: volumes separados, ocultar movimento de fundo, sons distintos por evento, modo de prática sem falha, lembretes de objetivo, nada de pressionar repetidamente ou de quick-time events, nada de ações simultâneas. Avançado: nenhum evento súbito inesperado, ocultar elementos não interativos, nenhuma exigência de timing preciso, cooldown de 0,5 s para entrada.
- **AbleGamers APX.** São 22 padrões, divididos em Access e Challenge. Os relevantes aqui: *Second Channel* (toda informação em dois canais), *Clear Text*, *Leave It There* (informação persistente), *Training Ground* (área de treino), *Helping Hand* (assistência opcional), *Undo/Redo*.
- **BBC GEL / Accessible Games Guidelines.** A BBC exige um mínimo de acessibilidade para publicar jogos infantis (CBeebies, CBBC, Bitesize). Exemplo: jogos jogáveis com 2 botões ou switch.
- **Microsoft Inclusive Design.** "Resolva para um, estenda para muitos" e o espectro de personas (permanente, temporário, situacional). Exemplo situacional: a sala de aula barulhenta torna o áudio inutilizável para todos, não só para quem tem hiperacusia.

### Recomendações

- **R1. Paleta de base com saturação moderada.** Use fundos neutros e quentes, de baixa saturação (off-white, areia, verde-acinzentado claro). Reserve a cor saturada só para o **alvo** e a ação principal. A regra é "uma coisa colorida por vez = o que importa agora".
- **R2. Evite amarelo e laranja saturados e vermelho puro em grandes áreas.** Se o amarelo for cor da marca, use tons dessaturados ou mostarda/ocre em áreas pequenas. Prefira verdes, azuis acinzentados e terrosos nos campos amplos. A evidência é moderada; valide em teste.
- **R3. Contraste alto onde importa, sem "vibração".** Texto deve ter pelo menos 4,5:1 (mire em 7:1 para instruções), e alvos e botões pelo menos 3:1 contra o fundo. Evite pares complementares saturados lado a lado (vermelho/verde, azul/laranja puros), que produzem vibração visual. Evite branco puro #FFF com preto puro #000 em grandes blocos; use #1F2328 sobre #FAF7F0, por exemplo.
- **R4. Nunca use só cor.** Certo/errado, estados e categorias também levam forma, ícone ou padrão (WCAG 1.4.1), o que atende também ao daltonismo (~8% dos meninos).
- **R5. Fundo "silencioso" durante a tarefa.** Nada de elementos decorativos animados atrás do alvo e nada de parallax. A decoração fica só nas telas de transição e recompensa, e mesmo lá é desligável.
- **R6. Animação funcional, curta e previsível.** Transições de 150 a 300 ms com easing suave. Nada de tremor de tela, zoom súbito, estroboscópio ou mais de 3 flashes por segundo (WCAG 2.3.1). Todo loop com mais de 5 s precisa poder ser pausado (2.2.2). Respeite `prefers-reduced-motion` e ofereça interruptor próprio (2.3.3).
- **R7. Som opcional, com volumes separados e padrão "baixo".** Faixas independentes para música, efeitos e voz. **Música desligada por padrão** durante a tarefa. Efeitos curtos, suaves, sem graves fortes nem agudos estridentes, sem sons de alarme ou buzina para erro. Tudo que é sonoro também aparece visualmente (*Second Channel*). Lembre que a escola tem sala barulhenta e às vezes não tem fone.
- **R8. Nada súbito.** Nenhum som, pop-up ou elemento entra sem aviso. A entrada do VUOO Bot é anunciada e lenta.

**Fontes (seção 1)**
- Ben-Sasson et al. 2009: https://pubmed.ncbi.nlm.nih.gov/18512135/
- Ben-Sasson et al. 2019, atualização: https://cris.haifa.ac.il/en/publications/update-of-a-meta-analysis-of-sensory-symptoms-in-asd-a-new-decade/
- Williams, Suzman & Woynaroski 2021, hiperacusia: https://pmc.ncbi.nlm.nih.gov/articles/PMC8349927
- Grandgeorge & Masataka 2016: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5179595/
- Fisher, Godwin & Seltman 2014: https://www.cmu.edu/news/stories/archives/2014/may/may27_decoratedclassrooms.html
- Crítica de Imuta & Scarf 2014: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4274873/
- Alves et al. 2021, Delphi: https://library.iated.org/view/ALVES2021PLA
- Princípios de jogos sérios para TEA: https://thesai.org/Downloads/Volume14No5/Paper_100-Serious_Game_Design_Principles_for_Children_with_Autism.pdf
- W3C COGA: https://www.w3.org/TR/coga-usable/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Understanding 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Understanding 2.3.3: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- UK Home Office, pôsteres: https://accessibility.blog.gov.uk/2016/09/02/dos-and-donts-on-designing-for-accessibility/
- Game Accessibility Guidelines: https://gameaccessibilityguidelines.com/full-list/
- AbleGamers APX: https://accessible.games/apx
- BBC e acessibilidade em jogos infantis: https://abilitynet.org.uk/news-blogs/making-gaming-accessible-masses
- Microsoft Inclusive Design Toolkit: https://download.microsoft.com/download/b/0/d/b0d4bf87-09ce-4417-8f28-d60703d672ed/inclusive_toolkit_manual_final.pdf

---

## 2. Tipografia para leitores iniciantes e disléxicos

### Evidência

**[FORTE/MODERADA] Tamanho maior ajuda crianças.**
- Wilkins et al. (2009), com crianças de 7 a 9 anos: texto maior foi verificado cerca de 9% mais rápido, e o aumento da fonte elevou a "idade de leitura" medida em cerca de 4 meses.
- Hughes & Wilkins concluem que a tipografia infantil "fica pequena cedo demais". A altura-x típica de livros iniciais é de cerca de 4 mm.

**[MODERADA/FORTE] Espaçamento entre letras ajuda disléxicos.**
- Zorzi et al. (2012, *PNAS*), com 74 crianças disléxicas italianas e francesas de 8 a 14 anos: espaçamento extra-largo dobrou a acurácia e aumentou a velocidade em mais de 20%. O mecanismo é a redução do *crowding*, e quem lê pior ganha mais.
- Houve debate sobre a especificidade do efeito (se ajuda disléxicos mais que leitores mais novos), mas o efeito é considerado replicável.

**[MODERADA, negativa] OpenDyslexic não funciona.** Wery & Diliberto (2017, *Annals of Dyslexia*): nenhuma melhora de velocidade ou acurácia em crianças disléxicas comparada a Arial e Times, e nenhuma criança preferiu a fonte. Outros estudos com Dyslexie chegam a conclusões semelhantes: o ganho, quando aparece, vem do espaçamento, e não do desenho das letras.

**[FRACA] Lexend.** O principal estudo envolveu cerca de 20 alunos do 3º ano, foi ligado ao desenvolvedor e não tem replicação independente. A ideia central (largura e espaçamento ajustáveis) é coerente com Zorzi, mas a evidência específica é fraca.

**[FRACA/ESPECIALISTA] Atkinson Hyperlegible.** Foi projetada pelo Braille Institute para baixa visão, com diferenciação máxima entre caracteres confundíveis (I/l/1, O/0, b/d com terminais distintos). Não encontrei estudos com crianças. Comparações informais a colocam no mesmo patamar de outras sans-serif humanistas. É uma boa escolha pela diferenciação, mas não é "comprovadamente superior". A versão *Atkinson Hyperlegible Next* (2025) tem mais pesos.

**[ESPECIALISTA] Andika (SIL).** Feita especificamente para alfabetização: "a" e "g" de um só andar, como na escrita à mão, e I/l/1 distintos. A justificativa é de especialistas em letramento, sem teste controlado. Licença OFL.

**[ESPECIALISTA] British Dyslexia Association, *Dyslexia Style Guide*.**
- Sans-serif, 12 a 14 pt ou mais.
- Entrelinha de 1,5.
- Espaçamento de letras em torno de 35% da largura média da letra.
- Fundo creme ou pastel em vez de branco puro.
- Alinhamento à esquerda, sem justificar.
- Evitar itálico, sublinhado e TEXTO LONGO EM CAIXA ALTA; usar negrito para ênfase.

**[ESPECIALISTA/contexto BR] Letra bastão (caixa alta) na alfabetização brasileira.**
- É prática disseminada começar pela letra de imprensa maiúscula ("bastão"). As razões: traçado mais simples, letras mais distintas entre si (sem espelhamento b/d/p/q) e presença na escrita social (placas, embalagens).
- Há corrente que defende a "dupla caixa" desde o início.
- Para o VUOO, a criança do 1º ano (6 anos) pode não reconhecer bem minúsculas. Ainda assim, caixa alta reduz a forma das palavras e é pior para frases longas, como indica a BDA.

### Recomendações

- **R9. Família tipográfica.** Use **Andika** ou **Atkinson Hyperlegible (Next)** como fonte de interface e instrução. Ambas são gratuitas (OFL), têm diferenciação I/l/1 e funcionam em PT-BR. A Andika tem vantagem para o 1º e 2º ano ("a" e "g" de um andar, como a criança escreve). Não adote OpenDyslexic como padrão; no máximo, ofereça-a como opção de preferência, sem prometer benefício.
- **R10. Caixa alta por série/perfil.**
  - 1º ano e início do 2º, e quem marcar "LETRA BASTÃO" nas configurações: palavras soltas, rótulos e instruções curtas em CAIXA ALTA.
  - A partir do 2º e 3º ano: frases em caixa mista (sentence case).
  - Deixe isso como opção configurável pelo professor, e não fixa.
- **R11. Tamanho generoso.** Instrução principal com no mínimo 24 a 28 px CSS em tablet (altura-x de cerca de 4 mm na distância de uso). Rótulos com no mínimo 18 a 20 px. Ofereça escala de texto em 3 passos (100%, 125%, 150%) sem quebrar o layout.
- **R12. Espaçamento e entrelinha.** Entrelinha de 1,4 a 1,6. Espaço entre letras levemente aberto por padrão (+2% a +5%) e um modo "espaçado" (+12% a 15%, alinhado ao WCAG 1.4.12 e a Zorzi). Linhas curtas (até ~40 caracteres para iniciantes), alinhadas à esquerda, sem hifenização, sem itálico e sem sublinhado decorativo.
- **R13. Texto mínimo, sempre com narração.** O 1º ano ainda não lê com fluência e disléxicos leem com esforço. Toda instrução tem **áudio** (botão de alto-falante persistente, com replay ilimitado) e **pictograma**. O texto é apoio, não o canal principal.

**Fontes (seção 2)**
- Wilkins et al. 2009, tamanho de fonte em crianças: https://repository.essex.ac.uk/1476/
- Zorzi et al. 2012, *PNAS*: https://pmc.ncbi.nlm.nih.gov/articles/PMC3396504
- Comentário sobre Zorzi: https://pmc.ncbi.nlm.nih.gov/articles/PMC3396535
- Réplica de Zorzi: https://pmc.ncbi.nlm.nih.gov/articles/PMC3497756
- Wery & Diliberto 2017, OpenDyslexic: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5629233/
- Kuster et al. 2018, Dyslexie: https://link.springer.com/article/10.1007/s11881-017-0154-6
- Lexend, site e estudo do desenvolvedor: https://lexend.com/
- Crítica à evidência do Lexend: https://www.goguardian.com/blog/could-a-change-of-font-improve-reading-fluency
- Atkinson Hyperlegible: https://www.allaboutvision.com/conditions/blindness-low-vision/atkinson-hyperlegible-typeface
- Andika, notas de design: https://ctan.csail.mit.edu/fonts/andika/doc/design.pdf
- SIL typefaces (Material.io): https://material.io/blog/sil-typefaces
- BDA, resumo do Style Guide: https://ako.ac.nz/assets/Knowledge-centre/ALNACC-Resources/Dyslexia-resources/230907-Dyslexia-Friendly-Style-Guide.pdf
- Modo para dislexia (Smashing): https://smashingmagazine.com/2021/11/dyslexia-friendly-mode-website
- Dupla caixa na alfabetização: https://biblat.unam.mx/en/revista/revista-de-educacao-publica/articulo/a-dupla-caixa-e-o-espaco-em-branco-no-processo-de-alfabetizacao
- Nova Escola, tipos de letra no 1º ano: https://novaescola.org.br/planos-de-aula/fundamental/1ano/lingua-portuguesa/brincando-com-parlendas-tipos-de-letra/3943

---

## 3. Feedback, erro, previsibilidade, tempo e linguagem

### Evidência

**[FORTE] Intolerância à incerteza e ansiedade.** A revisão sistemática com meta-análise de Jenkinson, Milne & Thompson (2020), com 12 estudos, mostra associação robusta entre intolerância à incerteza e ansiedade no TEA. Previsibilidade não é "mimo"; ela atua sobre um mecanismo de ansiedade.

**[FORTE] Apoios visuais e CAA.** A revisão NCAEP (Steinbrenner et al., 2020) cobriu 972 estudos e identificou 28 práticas baseadas em evidência para autismo. Entre elas estão **Visual Supports**, **Augmentative and Alternative Communication**, **Technology-Aided Instruction**, **Prompting** e **Antecedent-Based Interventions**. Um caveat: a revisão foi criticada por critérios de inclusão frouxos (Leaf et al., 2021).

**[MODERADA] Erros repetidos levam à fuga.**
- Aprendizagem sem erro ("errorless") e dicas graduais reduzem comportamentos de fuga e frustração em alguns estudos de caso único.
- Altas taxas de erro estão associadas a respostas de fuga da tarefa.
- Prompting tem status de prática baseada em evidência (32 estudos de caso único).

**[MODERADA] Feedback imediato é especialmente importante no TDAH.** A revisão de Luman, Oosterlaan & Sergeant (2005; 22 estudos, 1.181 crianças) concluiu que reforço melhora desempenho e motivação em todos, mas um pouco mais em TDAH, e que crianças com TDAH preferem fortemente recompensa **imediata**. Pela teoria da aversão à espera (Sonuga-Barke), esperar é aversivo para crianças com TDAH quando a espera é real, e não hipotética.

**[MODERADA] Linguagem figurada.** A revisão de escopo de 2025 sobre linguagem figurada no TEA confirma dificuldade com metáforas, expressões idiomáticas e ironia em parte das crianças autistas, com grande variação individual. Mesmo com idade mental maior, metáforas novas continuam difíceis.

**[MODERADA] TDC.** Crianças com TDC aprendem sequências motoras tão bem quanto colegas quando a exigência de execução fina é removida (Lejeune et al., 2013). O gargalo é a execução, e não a aprendizagem. O feedback aumentado ajuda a reconhecer o erro (estudo de codesign em RA, 2024).

**[ESPECIALISTA] Guias.**
- COGA 4.4.4 (linguagem literal), 4.4.9 (uma instrução por vez), 4.5.9 (evitar timeouts), 4.5.10 (feedback).
- Pôster autismo do Home Office: sem figuras de linguagem, botões descritivos.
- Game Accessibility Guidelines: tutorial interativo, modo de prática sem falha, lembrete do objetivo.
- APX: *Training Ground*, *Leave It There*.

**[ESPECIALISTA] ARASAAC.** São mais de 13.500 pictogramas de CAA, do Governo de Aragão, desenhados por Sergio Palao, sob licença **CC BY-NC-SA**. O NC proíbe uso comercial e o SA exige a mesma licença nas obras derivadas. Se o VUOO tiver modelo comercial (venda a redes, por exemplo), é preciso consultar a ARASAAC ou usar símbolos próprios/abertos compatíveis.

### Recomendações

#### Erro sem punição

- **R14. Erro = informação, nunca castigo.**
  - Sem som de buzina ou alarme, sem "X" vermelho grande, sem tremor de tela, sem perder vidas, sem "GAME OVER".
  - O erro é sinalizado de forma **neutra e breve**: o alvo correto pisca suavemente ou recebe um contorno, com um som discreto e diferente do de acerto.
  - Em seguida, uma **pista do que fazer**, e não do que fez de errado: "Toque no círculo azul", e não "Errado!".
- **R15. Separe "erro de medida" de "erro de aprendizagem".**
  - Em jogos de medição (por exemplo, tempo de reação, go/no-go), o feedback por tentativa deve ser idêntico e neutro, para não enviesar a medida.
  - Em jogos de treino, use dicas graduais: 1ª tentativa sem dica, 2ª com destaque leve, 3ª com demonstração (*Helping Hand*).
- **R16. Erros consecutivos baixam a dificuldade automaticamente**, sem anunciar como fracasso. Exemplo: 3 erros seguidos levam o jogo a desacelerar, e o Bot diz "Vamos mais devagar". Registre a mudança como parâmetro (R0).
- **R17. A tela final de cada microjogo mostra o que a criança fez, e não o que faltou.** "Você tocou 12 estrelas!" em vez de "12/20". Comparações só com a própria criança ("2 a mais que da última vez"), e só se positivas ou neutras. Com resultado pior, omita a comparação.

#### Previsibilidade e rotina

- **R18. Rotina fixa idêntica em todos os microjogos.** A sequência é sempre a mesma:
  1. Tela de "o que vem" (pictograma + nome do jogo + duração em forma visual)
  2. Demonstração de 1 tentativa
  3. "Pronto?" com a criança tocando para começar (ela inicia, e não o sistema)
  4. Jogo
  5. Fim com aviso
  6. Tela de "o que você fez"
  7. "Próximo:" com prévia
  Botões, posições e cores de navegação nunca mudam entre jogos (COGA 4.2.3).
- **R19. Painel de agenda visual da sessão.** Uma faixa com os pictogramas dos 3 a 5 jogos do dia, com o atual destacado e os concluídos marcados com "feito". A criança sempre sabe onde está e quanto falta.
- **R20. Avisos de transição.** Cerca de 10 s antes do fim do jogo, um indicador visual calmo (barra que esvazia, sem números piscando, sem som de urgência). Toda mudança de tela é anunciada pelo Bot ("Agora vamos para..."). Nunca troque de tela sem a criança tocar em "continuar", exceto no fim natural do jogo.
- **R21. Tempo visível, mas não ansioso.** A duração aparece como **forma que esvazia** (círculo ou barra), sem contagem regressiva numérica grande, sem vermelho e sem tique-taque. Ofereça a opção de ocultar o indicador. Nos menus e instruções não há limite de tempo (WCAG 2.2.1, COGA 4.5.9). A pressão de tempo existe só dentro da tarefa, quando ela é a própria medida.
- **R22. Pausa sempre disponível.** Botão de pausa fixo, grande, no mesmo canto em todos os jogos. Pausar não penaliza: a tentativa em curso é descartada da medida e marcada.

#### Linguagem

- **R23. Linguagem literal, curta e no presente.** Uma instrução por frase e um verbo de ação por frase ("Toque na estrela"). Sem metáforas, ironia, trocadilhos ou expressões ("arrasou!", "voando baixo", "quebrou o recorde", "fique de olho"). Elogio descritivo e concreto ("Você tocou rápido") em vez de hipérbole ("Você é um gênio!"). Isso vale também para o nome e as falas do VUOO Bot.
- **R24. Botões descritivos com verbo + pictograma.** "JOGAR", "REPETIR INSTRUÇÃO", "PAUSAR", "SAIR", e nunca "OK" ou "Vamos lá?" ambíguos.
- **R25. Pictogramas consistentes ao lado do texto e da fala.** Um pictograma por conceito, sempre o mesmo (por exemplo, o mesmo ícone para "tocar", "esperar", "não tocar"). Estilo plano, contorno claro, sem perspectiva. Use o padrão visual ARASAAC como referência. Verifique a licença CC BY-NC-SA para uso comercial ou crie um conjunto próprio com o mesmo princípio.
- **R26. Demonstração em vez de explicação.** Cada jogo começa com uma mão animada fazendo a ação uma vez (*Training Ground*), seguida de uma tentativa de prática que não conta para a medida.

**Fontes (seção 3)**
- Intolerância à incerteza e ansiedade no TEA, meta-análise 2020: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7539603/
- NCAEP, 2020 Evidence-Based Practices Report: https://ncaep.fpg.unc.edu/?p=395
- NCAEP, Executive Summary: https://ncaep.fpg.unc.edu/sites/ncaep.fpg.unc.edu/files/imce/documents/EBP%20Executive%20Summary.pdf
- AFIRM, Prompting (EBP brief): https://afirm.fpg.unc.edu/sites/afirm.fpg.unc.edu/files/imce/resources/PP%20EBP%20Brief%20Packet.pdf
- Taxas de erro e fuga (J Behav Educ 2020): https://link.springer.com/article/10.1007/s10864-020-09407-0
- Luman, Oosterlaan & Sergeant 2005: https://www.epistemonikos.org/en/documents/3d4ebe091cff46bfd07e428a947ec137f76f6b5b
- Aversão à espera (Sonuga-Barke, Southampton): https://eprints.soton.ac.uk/397632
- Linguagem figurada no TEA, revisão de escopo 2025: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12649625/
- TDC e videogames, revisão sistemática: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6335818/
- TDC, codesign em RA: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11311161/
- ARASAAC: https://arasaac.org/about-us
- Termos de uso ARASAAC: https://arasaac.org/terms-of-use
- W3C COGA: https://www.w3.org/TR/coga-usable/

---

## 4. Gamificação, recompensas e o VUOO Bot

### Evidência

**[FORTE, com debate] Recompensas extrínsecas podem minar a motivação intrínseca.**
- Deci, Koestner & Ryan (1999), meta-análise de 128 estudos: recompensas tangíveis e esperadas, contingentes à participação, conclusão ou desempenho, reduziram a motivação intrínseca de livre escolha (d entre -0,28 e -0,40).
- O efeito foi mais forte em **crianças** que em universitários.
- Feedback verbal positivo e informativo **aumentou** a motivação em universitários, com efeito menor em crianças.
- Cameron & Pierce contestam a generalidade do achado. O consenso prático: recompensa **inesperada, informativa e não controladora** tem baixo risco; recompensa **esperada, tangível e controladora** tem alto risco.

**[MODERADA] Gamificação aumenta o engajamento em TEA e TDAH, mas a evidência é fraca.**
- A revisão de ambientes gamificados para estudantes com TEA (2023) mostra que feedback, recompensas e missões aumentam a motivação.
- Revisões de jogos sérios para TDAH relatam mais participação e entusiasmo.
- Todas ressaltam amostras pequenas, curta duração e ausência de dados longitudinais.

**[MODERADA] Reforço no TDAH.** Ver Luman et al. (2005), seção 3: imediatismo e saliência importam. Em estudo de 2009, a frequência e a magnitude do reforço afetaram de modo diferente os grupos com TDAH e com TEA, o que mostra variabilidade e não justifica uma "dose única".

**[MODERADA] Rankings (leaderboards) prejudicam quem está embaixo.**
- Em vários estudos, a divulgação de desempenho relativo elevou o desempenho de quem já ia bem (+0,15 DP) e **reduziu o de quem ia mal (-0,30 DP)**.
- Com alunos de 5º e 6º ano, o interesse cresceu só nas posições altas.
- Em turma inclusiva, as crianças neurodivergentes tendem a ficar nas posições baixas em tarefas de TR e coordenação, sobretudo com TDC. Ranking é contraindicado.

**[MODERADA] Cooperação.** Jogos colaborativos que exigem ação conjunta aumentaram a interação social positiva de crianças autistas (8 a 11 anos) sem aumentar comportamentos negativos. Os estudos são pequenos e nenhum compara diretamente preferência por cooperação versus competição.

**[ESPECIALISTA, sem estudo controlado em crianças] Streaks (sequências).** Funcionam por aversão à perda. Há relatos de ansiedade e compulsão (crianças com traços ansiosos ou obsessivos). O guia de design recomenda nunca tornar a perda catastrófica.

**[MODERADA/ESPECIALISTA] ABA vs. abordagem neuroafirmativa.**
- Críticas do movimento da neurodiversidade (sistematizadas por Mathur et al., 2024): foco em conformidade, apagamento da identidade autista, foco restrito em comportamento observável.
- Em survey com 226 adultos autistas (Chazin et al., 2024), houve alta aprovação de dispositivos de comunicação e acomodações sensoriais, e **desaprovação de reforçadores arbitrários (comestíveis, fichas/tokens)**.
- Princípios afirmativos propostos: qualidade de vida como meta, interesses especiais como motor, **assentimento** (a criança pode recusar ou parar), medir bem-estar e não só conformidade.

**[MODERADA] Rostos de desenho e emoção.**
- Crianças autistas processam emoções em **rostos de desenho/avatar** de forma mais típica que em rostos reais (Rosset et al., 2008 e 2012).
- No estudo de rastreamento ocular de Pino et al. (2021), elas reconheceram melhor as emoções em avatares.
- Em um estudo com adolescentes (Brosnan et al., 2015), a vantagem apareceu com **imagens estáticas** e não com animadas (resultado de fonte secundária, a confirmar).
- Implicação: um mascote estilizado, com expressões simples e exageradas, é mais legível que um rosto realista.

### Recomendações

- **R27. Recompensa informativa, imediata e não controladora.**
  - O reforço principal é **feedback imediato de competência**: o alvo reage ao toque (micro-animação de 100 a 200 ms + som suave). Isso atende o TDAH (imediatismo) sem criar economia de fichas.
  - Elogio descritivo do Bot ("Você esperou a luz verde"), e não avaliativo ("Muito bem, bom menino").
- **R28. Sem economia de pontos ou moedas como motor.** Não use moedas, lojas, tokens trocáveis nem "ganhe X para desbloquear Y". Se houver coleção (adesivos, peças do Bot), ela deve ser **inesperada** e ligada a **participação ou esforço**, e não a desempenho ou velocidade. Nunca pode ser perdida.
- **R29. Sem rankings, sem comparação entre colegas, sem streaks punitivos.**
  - Nada de leaderboard de turma.
  - Progresso só **intraindividual** (álbum ou mapa de jornada pessoal que só cresce).
  - Se houver "dias seguidos", ele **nunca zera**; conte "dias em que você jogou" (cumulativo).
  - O professor vê dados individuais em painel privado, e não em telão.
- **R30. Cooperação, e não competição, quando houver social.** Metas de turma cumulativas e anônimas ("A turma acendeu 300 estrelas hoje") ou modos em dupla onde ambos contribuem para o mesmo objetivo. Assim nenhuma criança fica exposta como "a mais lenta".
- **R31. Assentimento e saída digna.** A criança pode sempre pular um jogo ("Agora não"), pausar ou parar, sem consequência negativa e sem o Bot ficar "triste". Registre o "pular" como dado (sinal de sobrecarga ou desinteresse), nunca como falha.
- **R32. Interesses como tema, e não como prêmio.** Permita escolher o **tema visual** do jogo (espaço, animais, trens, dinossauros...). A mecânica e a medida continuam idênticas. É a recomendação neuroafirmativa de usar interesses especiais, sem condicioná-los ao desempenho.
- **R33. O VUOO Bot como "par previsível", e não como juiz.**
  - **Rosto simples**: olhos grandes, boca clara, poucas linhas, sem traços realistas.
  - Expressões **poucas e exageradas** (feliz, calmo, curioso, surpreso), sempre acompanhadas da palavra e de um pictograma da emoção ("Estou contente").
  - **Nunca** expressa decepção, tristeza ou raiva em resposta ao desempenho da criança. Em erro, fica neutro ou encorajador.
  - Animação lenta, sem piscar ou mexer constantemente em idle (ou com idle desligável). Voz calma, ritmo pausado, frases curtas e literais.
  - Comportamento **idêntico em todos os jogos**: mesma posição, mesma entrada, mesmas falas-modelo.
  - Pode ser escondido ou desativado (alguns autistas acham personagens falantes intrusivos).
- **R34. Recompensa visual da tela final com intensidade ajustável.**
  - Modo padrão: celebração breve (até 2 s), sem confetes em tela cheia e sem fogos com flash.
  - Modo "festa": mais efeitos, para quem busca estímulo (hiporresponsivos e alguns perfis de TDAH).
  - Modo calmo: só um selo estático e o texto.

**Fontes (seção 4)**
- Deci, Koestner & Ryan 1999: https://depts.washington.edu/techdocs/papers/deciExtrinsicRewardsAndIntrinsicMotivation99.pdf
- Deci, Koestner & Ryan 2001 (educação): https://www.selfdeterminationtheory.org/SDT/documents/2001_DeciKoestnerRyan.pdf
- Gamificação e jogos sérios para TEA, revisão: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10173233/
- Jogos sérios para TDAH, revisão: https://arxiv.org/pdf/2105.02970
- Gamificação em TEA (Universidade de Twente): https://essay.utwente.nl/essays/65757
- Rankings e desempenho relativo: https://download.uni-mainz.de/RePEc/pdf/Discussion_Paper_1908.pdf
- Leaderboards em competição de matemática por equipes: https://trepo.tuni.fi/handle/10024/130150
- Leaderboards com crianças: https://frontiersin.org/journals/education/articles/10.3389/feduc.2019.00165/text
- Jogo colaborativo com robô KASPAR: https://uhra.herts.ac.uk/id/eprint/3808/
- Coop-Quarto: https://queensu.scholaris.ca/items/3a44b798-2cd8-4f8a-8f5e-2bec2fc3774a
- Brincar colaborativo no Qatar (Frontiers 2024): https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1273757/epub
- Streaks, UX e psicologia: https://smashingmagazine.com/2026/02/designing-streak-system-ux-psychology/
- Mathur et al. 2024, neurodiversidade e ABA: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11219658/
- Behavior Analysis in Practice 2025: https://link.springer.com/article/10.1007/s40617-025-01149-7
- Rosset et al., rostos de desenho: https://mijn.bsl.nl/typical-emotion-processing-for-cartoon-but-not-for-real-faces-in/547186
- Rosset et al. 2012, priming afetivo: https://insar.confex.com/imfar/2012/webprogram/Paper10520.html
- Brosnan et al. 2015: https://researchportal.bath.ac.uk/en/publications/emotion-recognition-in-animated-compared-to-human-stimuli-in-adol/
- Pino et al. 2021, avatares: https://ricerca.univaq.it/bitstream/11697/169962/2/s10639-021-10552-w.pdf

---

## 5. Controles de personalização e interação motora

### Evidência

**[FORTE, norma]** WCAG 2.5.8 (24 px, AA) e 2.5.5 (44 px, AAA), 2.2.1, 2.2.2, 2.3.3, 1.4.12 e 1.4.4 (redimensionar texto até 200%).

**[MODERADA] Precisão motora infantil.**
- Brown, Anthony et al. (CHI 2013): crianças de 7 a 10 anos erraram 26% dos toques contra 16% dos adultos, com alvos de 3 a 13 mm. O erro é maior com alvos pequenos e com crianças menores.
- A lei de Fitts vale para crianças de 5 a 10 anos (Woodward et al., 2020), mas é imprecisa abaixo de ~4 mm.
- Para pessoas com limitação motora, Findlater et al. (CHI 2017) sugerem alvos de pelo menos 18 mm. Isso é relevante para TDC.

**[ESPECIALISTA]**
- Game Accessibility Guidelines: velocidade ajustável, alvos grandes e espaçados, sem segurar botão, sem ações simultâneas, sem timing preciso essencial, cooldown de 0,5 s, salvar configurações, perfis de configuração.
- COGA 4.9.3 e 4.9.4 (simplificação e interface personalizada).
- APX *Flexible Controls*.

### Recomendações

- **R35. Alvos grandes por padrão.** Botões de interface com no mínimo **64×64 px CSS (~12 a 15 mm em tablet)** e pelo menos 16 px de espaçamento. Isso fica muito acima do mínimo WCAG, porque crianças de 6 a 7 anos e crianças com TDC erram muito mais. Alvos de jogo com ~15 mm no padrão, e no perfil "alvo grande" pelo menos 20 mm (lembrando que isso é parâmetro de tarefa, ver R0). Área de toque maior que o desenho visível.
- **R36. Só toque simples.** Toque simples é a interação primária. Nada de arrastar de precisão, toque duplo, pressionar e segurar, multitoque ou pinça como requisito. Aceite o toque **na soltura** dentro da área, com tolerância a pequeno deslize. Ignore toques repetidos em menos de ~300 a 500 ms em botões de interface (evita duplo acionamento por tremor ou impulsividade), mas não nas tarefas de TR, onde cada toque é dado.
- **R37. Painel "Do meu jeito" (criança) + "Ajustes da turma/aluno" (professor), salvo por perfil.**
  - **Apresentação (livre):** som geral, música, efeitos e voz com volumes separados; animações (normal, reduzida, nenhuma); intensidade de cor (normal, suave, alto contraste); tamanho do texto (3 passos); letra bastão sim/não; espaçamento ampliado; fonte (Andika, Atkinson ou OpenDyslexic como preferência); Bot (mostrar, só voz, oculto); celebração (calma, padrão, festa); indicador de tempo (visível ou oculto); tema de interesse.
  - **Tarefa (só o professor, registrada):** velocidade (lenta, padrão, rápida), tamanho do alvo, número de tentativas, prática extra.
- **R38. Atalho "Modo Calmo" (baixo estímulo) com um toque.** Um único botão, também na tela de pausa, que aplica ao mesmo tempo: música off, efeitos a 30%, animação reduzida, cores suaves, celebração calma, Bot só com voz. Ofereça-o também como **perfil inicial** quando o professor marcar a criança com sensibilidade sensorial. Lembre que a hiper-responsividade afeta 30% a 40% ou mais das crianças autistas, e crianças típicas também se beneficiam em sala barulhenta.
- **R39. Respeite as configurações do sistema** (`prefers-reduced-motion`, `prefers-contrast`, tamanho de fonte do SO) como valores iniciais. Mostre a primeira configuração **visualmente**, com prévia ao vivo ("Assim fica o som. Gostou?"), e não como lista de checkboxes.
- **R40. Codesign e teste.** Teste protótipos com crianças autistas, com TDAH, disléxicas e com TDC da rede de SP, além de professores do AEE. Meça: aceitação de cor e som, compreensão das instruções sem adulto, taxa de "pular", erros de toque por tamanho de alvo. A evidência de base é pequena, e esse teste é o que validará R1 a R39.

**Fontes (seção 5)**
- Brown et al. CHI 2013, alvos de toque com crianças: https://lisa-anthony.com/wp-content/uploads/2013/04/brown-et-al-chi2013mobacc.pdf
- Woodward et al. AVI 2020, Fitts com crianças: https://init.cise.ufl.edu/wp-content/uploads/sites/378/2021/05/woodward-et-al-AVI2020.pdf
- Findlater et al. CHI 2017, toque e limitação motora: https://faculty.washington.edu/leahkf/pubs/CHI2017-TouchscreenAccess.pdf
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Game Accessibility Guidelines: https://gameaccessibilityguidelines.com/full-list/
- AbleGamers APX: https://accessible.games/apx
- W3C COGA, objetivo 8: https://www.w3.org/TR/coga-usable/

---

## 6. Síntese por nível de evidência

| Nível | Achados principais |
|---|---|
| **Forte** | Diferenças sensoriais no TEA são prevalentes e bidirecionais (hiper e hipo), daí a necessidade de personalizar. Hiperacusia afeta cerca de 30% a 40%. Intolerância à incerteza está ligada à ansiedade. Apoios visuais, CAA e prompting são práticas baseadas em evidência. Recompensas esperadas e tangíveis minam a motivação intrínseca, mais em crianças. WCAG como norma. |
| **Moderada** | Espaçamento entre letras ajuda disléxicos. Fonte maior ajuda crianças. OpenDyslexic não ajuda. Ambiente visual carregado reduz atenção. Rankings prejudicam quem está embaixo. Rostos de desenho são mais legíveis para crianças autistas. Feedback imediato favorece o TDAH. Erros repetidos levam à fuga. Colaboração aumenta interação positiva. Preferência por verde e marrom em vez de amarelo (estudo único). Crianças erram mais toques. |
| **Especialista** | Guias COGA, Home Office, GAG, APX, BBC GEL, BDA. Letra bastão no início da alfabetização. Andika e Atkinson como fontes. Streaks geram ansiedade. Crítica neuroafirmativa a reforçadores arbitrários. |
| **Fraca ou ausente** | Lexend e Atkinson com crianças. Parâmetros numéricos específicos de animação e som para TEA. Comparação direta entre cooperação e competição. Timing em touchscreen para TDC. |

## 7. As 10 recomendações prioritárias

1. **R0**: separar apresentação (personalizável livremente) de parâmetros de tarefa (registrados), para acomodar sem contaminar a medida.
2. **R38/R37**: "Modo Calmo" com um toque e painel de personalização salvo por perfil.
3. **R1/R5**: paleta pouco saturada, fundo silencioso, cor forte só no alvo.
4. **R7**: som opcional, música desligada por padrão, volumes separados, tudo também visual.
5. **R14/R17**: erro neutro e informativo, sem castigo; tela final mostra o que a criança fez.
6. **R18–R21**: rotina idêntica em todos os jogos, agenda visual, avisos de transição, tempo como forma que esvazia.
7. **R23/R25/R13**: linguagem literal + pictograma + narração em toda instrução.
8. **R28/R29**: sem moedas, sem ranking, sem streak que zera; progresso só intraindividual.
9. **R33**: VUOO Bot estilizado, expressões poucas e rotuladas, nunca decepcionado, ocultável.
10. **R35/R36**: alvos de pelo menos 64 px (~12 a 15 mm) e só toque simples.
