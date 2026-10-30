---
id: acs.std.game-accessibility-guidelines
titulo: Diretrizes de acessibilidade em jogos (GAG, XAG, APX)
tipo: padrao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [gameaccessibility2026fulllist, gameaccessibility2026timing, gameaccessibility2026simplecontrols, microsoft2023xag, microsoft2022xag107, ablegamers2022apx, ablegamers2022slowitdown, ablegamers2022domorewithless, w3c2024wcag22, w3c2023understandingtiming, etsi2026en301549]
relacoes:
  - { tipo: parte-de, alvo: acs.std.comparison }
  - { tipo: complementa, alvo: acs.std.wcag }
  - { tipo: complementa, alvo: acs.adapt.adapting-games-and-activities }
  - { tipo: relacionado-a, alvo: acs.at.alternative-access }
  - { tipo: relacionado-a, alvo: acs.dim.motor }
  - { tipo: relacionado-a, alvo: acs.dim.cognitive-accessibility }
  - { tipo: relacionado-a, alvo: gam.diff.dynamic-difficulty-adjustment }
  - { tipo: relacionado-a, alvo: gam.evid.special-education-and-neurodivergence }
termos: [Game Accessibility Guidelines, Xbox Accessibility Guidelines, Accessible Player Experiences, padrão de acesso, padrão de desafio, remapeamento, alternância em vez de segurar, quick time event, ações simultâneas, velocidade de jogo, esquema de controle simplificado, acionador, varredura, rastreamento ocular, atraso pós-aceitação]
---

# Diretrizes de acessibilidade em jogos (GAG, XAG, APX)

## Definição e terminologia

Três conjuntos de diretrizes tratam a acessibilidade da jogabilidade, não só da interface. Nenhum é norma formal:

- **Game Accessibility Guidelines (GAG)**: "a collaborative effort between a group of studios, specialists and academics", organizadas por categoria (motora, cognitiva, visão, audição, fala, geral) e por nível: básico ("easy to implement, wide reaching and apply to almost all game mechanics"), intermediário ("require some planning and effort but often just good general game design") e avançado ("complex adaptations for profound impairments and specific niche mechanics") [F: gameaccessibility2026fulllist]. A página não informa versão nem data.
- **Xbox Accessibility Guidelines (XAG)**, documentação de fornecedor (Microsoft), versão 3.2 de 8 de junho de 2023; cada diretriz tem objetivo, perguntas de escopo, áreas-chave, diretrizes de implementação, exemplos e impacto por tipo de jogador; o próprio texto diz que não pretende servir de checklist de conformidade legal [F: microsoft2023xag].
- **Accessible Player Experiences (APX)**, da AbleGamers Foundation: 22 padrões de projeto, 12 de acesso (enviar entrada e receber informação do jogo) e 10 de desafio ("adding flexibility to challenge", não removê-lo); a fundação recomenda priorizar acesso quando os recursos são limitados [F: ablegamers2022apx].

## Problema que resolve

A WCAG excetua limites de tempo essenciais e eventos em tempo real [F: w3c2024wcag22, 2.2.1; w3c2023understandingtiming]. Em jogo, tempo, precisão e sequência de comandos costumam ser o próprio desafio, logo "essenciais" no sentido da WCAG. As diretrizes de jogos ocupam esse espaço: tratam como tornar o desafio ajustável sem retirá-lo [I].

## Fundamentos e funcionamento

### Barreiras de mecânica e tempo para acionadores, varredura e rastreamento ocular

A XAG 107 (entrada) separa três demandas que o simples remapeamento não resolve [F: microsoft2022xag107]:

- **velocidade**: acionar controles em rápida sucessão; a diretriz lembra que jogadores podem usar acionadores montados perto da cabeça, braços ou pernas, que "take more time and effort to move";
- **complexidade**: botões simultâneos ou sequências que exigem coordenação e memória;
- **duração**: manter um botão pressionado por longos períodos.

As diretrizes de implementação da XAG 107 pedem: navegar a interface "by using single, non-simultaneous key presses"; remapear todos os controles, de preferência por ação e não só por botão; evitar sequências rápidas de pressionamentos (quick time events), segurar teclas por tempo longo e pressionar dois botões ao mesmo tempo, e, quando inevitáveis, oferecer alternativa menos exigente ou permitir pular o trecho; operar sem gestos multiponto e de trajetória; ativar no evento de soltar com cancelamento; oferecer alternativa digital para fala e movimento; não exigir dois analógicos; e ajustar a sensibilidade analógica em ao menos 50% para mais ou para menos. Em dispositivos móveis, pede compatibilidade com o acesso por acionador da plataforma, controle por voz, alvos de toque redimensionáveis (sugestão de 15 mm em telefones e 24 mm em tablets) e esquemas de controle simplificados [F: microsoft2022xag107].

Na GAG, as diretrizes motoras incluem, no nível básico, ajustar a velocidade do jogo, a sensibilidade dos controles e remapear controles; no intermediário, evitar ou oferecer alternativa a segurar botões, evitar entradas repetidas e não exigir ações simultâneas; no avançado, "provide very simple control schemes that are compatible with assistive technology devices, such as switch or eye tracking", um intervalo de 0,5 s entre entradas (atraso pós-aceitação) e "do not make precise timing essential to gameplay" [F: gameaccessibility2026fulllist]. A página sobre esquemas simples explica que quem usa acionadores ou rastreamento ocular costuma executar poucas entradas, que o rastreamento ocular mapeia para posição analógica do ponteiro e não para botões, e que "the more you are able to simplify the controls, the more of these kind of setups will be compatible" [F: gameaccessibility2026simplecontrols]. A página sobre tempo recomenda alternativas, ações executáveis com o jogo pausado ou mecanismo para pular [F: gameaccessibility2026timing]. Nenhuma das duas páginas trata explicitamente de varredura; a XAG 107 é a única das fontes lidas que descreve varredura por grupos e linhas [F: microsoft2022xag107].

Síntese das barreiras [I, a partir das fontes acima]: janela de reação curta; pressionar e segurar; repetição rápida; combinação simultânea; sequência a memorizar; gesto de trajetória ou arraste; alvo pequeno ou móvel; movimento contínuo de câmera ou mira. Para varredura, cada escolha custa vários ciclos de varredura, o que multiplica o tempo de resposta; para rastreamento ocular, fixar o olhar para ativar disputa o olhar com a percepção do jogo [H].

### Cognição

A GAG cognitiva inclui evitar imagens piscantes e padrões repetitivos e usar linguagem simples (básico), modo de prática sem falha, lembrete do objetivo corrente e ajuste de velocidade (intermediário) [F: gameaccessibility2026fulllist]. A APX "Do More With Less" reduz o número de ações de uma sequência, citando jogadores com deficiência de membro superior e com deficiência cognitiva que se beneficiam de "fewer, more memorable controls" [F: ablegamers2022domorewithless]. A XAG 107 também reconhece que combinações de botões bloqueiam quem não consegue lembrá-las [F: microsoft2022xag107].

### Desafio ajustável

A APX "Slow It Down" permite "reduce the speed, volume, and variety of events in the game", para jogadores com deficiência física que precisam de mais tempo para responder e com deficiência cognitiva que precisam de mais tempo para processar [F: ablegamers2022slowitdown]. Os demais padrões de desafio incluem House Rules, Bypass, Undo Redo, Helping Hand, Training Ground, Play Alongside, Total Recall e Save Early, Save Often [F: ablegamers2022apx]. Na GAG, dificuldade aparece na categoria geral, com níveis variados e ajuste durante o jogo, inclusive por dificuldade adaptativa [F: gameaccessibility2026fulllist]; o mecanismo adaptativo pertence a `gam.diff.dynamic-difficulty-adjustment`.

## Vantagens e limitações

Vantagens: cobrem exatamente o que a WCAG deixa como "essencial"; organizam por barreira e não por diagnóstico; a GAG gradua o esforço por nível [F: gameaccessibility2026fulllist; ablegamers2022apx].

Limitações: são diretrizes de fornecedor ou de comunidade, sem processo formal de normalização nem critério de teste com resultado binário; a própria XAG recusa o papel de checklist legal [F: microsoft2023xag]. A GAG não traz versão nem data [F: gameaccessibility2026fulllist]. Não se localizou nesta sessão evidência empírica comparando a eficácia das diretrizes.

## Alternativas e comparações

| Conjunto | Mantenedor | Estrutura | Natureza |
|---|---|---|---|
| GAG | coletivo de estúdios, especialistas e acadêmicos | categorias e níveis básico, intermediário, avançado | técnica, aberta |
| XAG 3.2 | fornecedor de plataforma | diretrizes numeradas com escopo, implementação e impacto | fornecedor, não legal |
| APX | entidade sem fins lucrativos | 22 padrões, acesso e desafio | linguagem de projeto |
| WCAG 2.2 | W3C | critérios testáveis A/AA/AAA | norma; exclui o essencial |
| EN 301 549, 5.9 | ETSI/CEN/CENELEC | requisito sobre ações simultâneas | norma de compra [F: etsi2026en301549, cl. 5.9] |

## Exemplo técnico independente de domínio

```
para cada mecânica M da atividade:
    demandas = {janela_reacao, segurar, repetir, simultaneo, sequencia, trajetoria, precisao}
    para cada d em demandas(M):
        oferecer pelo menos um: ajustar_velocidade | alternar_em_vez_de_segurar |
                                 acao_unica_remapeavel | agir_com_pausa | pular_trecho
    garantir: navegação por entradas únicas e não simultâneas; ativação ao soltar
    registrar: se d é o objetivo pedagógico, decidir em adaptation/ se ajustar muda o construto
```

## Relações com outros conceitos

Complementa `acs.std.wcag` e `acs.adapt.adapting-games-and-activities` (como compensar sem descaracterizar). Relaciona-se com `acs.at.alternative-access`, `acs.dim.motor` e `acs.dim.cognitive-accessibility`; com `gam.diff.dynamic-difficulty-adjustment` (ajuste automático de dificuldade) e `gam.evid.special-education-and-neurodivergence` (evidência de eficácia).

## Lacunas e questões abertas

- Não foi lida a lista completa de diretrizes XAG nem a página de cada padrão APX além dos dois citados.
- Valores como 0,5 s de atraso e 15 ou 24 mm de alvo são recomendações das fontes, não resultados experimentais verificados aqui.
- Faltam diretrizes específicas para varredura em jogo (tempo de ciclo, ordem de varredura) nas fontes lidas.
- A distinção entre ajuste de acesso e alteração do objetivo da atividade fica para `acs.adapt.accommodation-vs-modification`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gameaccessibility2026fulllist | tecnico | 2026-10-30 |
| gameaccessibility2026timing | tecnico | 2026-10-30 |
| gameaccessibility2026simplecontrols | tecnico | 2026-10-30 |
| microsoft2023xag | fornecedor | 2026-10-30 |
| microsoft2022xag107 | fornecedor | 2026-10-30 |
| ablegamers2022apx | tecnico | 2026-10-30 |
| ablegamers2022slowitdown | tecnico | 2026-10-30 |
| ablegamers2022domorewithless | tecnico | 2026-10-30 |
| w3c2024wcag22 | normativo | 2026-10-30 |
| w3c2023understandingtiming | normativo (informativo) | 2026-10-30 |
| etsi2026en301549 | normativo | 2026-10-30 |
