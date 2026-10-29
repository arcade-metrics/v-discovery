---
id: rtm.case.index
titulo: "Estudos de caso de sistemas de tempo real e multiplayer"
tipo: mapa
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [bettner2001archers, sanglard2012quake3, bernier2001latency, frohnmayer2001tribes, wallace2019figma, nichols1995jupiter, ford2017overwatch, cone2018rocketleague, gamedeveloper2011haloreach]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.arch.comparison }
  - { tipo: relacionado-a, alvo: rtm.pred.comparison }
termos: []
---

# Estudos de caso de sistemas de tempo real e multiplayer

Critério de inclusão: existe fonte primária técnica (artigo ou palestra de quem construiu o sistema, ou revisão direta do código-fonte publicado) que foi aberta e lida nesta pesquisa. Cada caso documenta contexto, restrições, arquitetura, técnicas, números reportados, lições, separação entre fato e opinião, e limites.

## Tabela de casos

| Id | Caso | Ano do sistema | Gênero | Arquitetura | Técnicas principais | Fonte primária |
|---|---|---|---|---|---|---|
| rtm.case.age-of-empires | Age of Empires | 1997 | estratégia em tempo real | lockstep determinístico, peer-to-peer, UDP | turnos de comunicação de ~200 ms, comandos agendados 2 turnos à frente, speed control, RNG sincronizado, checksums de desync | bettner2001archers |
| rtm.case.quake3 | Quake III Arena | 1999 | ação em primeira pessoa | servidor autoritativo, UDP | snapshots (32 por cliente), delta contra último snapshot confirmado, fragmentação em 1.400 bytes, Huffman | sanglard2012quake3 |
| rtm.case.half-life | Half-Life (Valve) | 2001 | ação em primeira pessoa | servidor autoritativo | predição no cliente com código compartilhado, interpolação de 100 ms com position history, lag compensation por rewind | bernier2001latency |
| rtm.case.tribes | Starsiege: TRIBES / TRIBES II | 1998 | ação em equipe, mapas grandes | servidor autoritativo, UDP | quatro classes de entrega, notificação de pacotes sem retransmissão, ghosts com state mask e scoping por prioridade, moves repetidos 3x, bit packing | frohnmayer2001tribes |
| rtm.case.figma-multiplayer | Figma | 2016 | colaboração em editor visual | servidor autoritativo por documento, WebSocket | last-writer-wins por propriedade, IDs por cliente, fractional indexing, undo multiplayer, reconexão por reaplicação | wallace2019figma |
| rtm.case.jupiter | Jupiter (Xerox PARC) | 1995 | colaboração em widgets e texto | servidor central serializador, TCP | transformação de operações cliente-servidor (xform), espaço de estados 2D, eco para consistência n-ária | nichols1995jupiter |

## Padrões recorrentes entre os casos [I]

1. Em todos os seis casos há uma autoridade central ou um protocolo que torna a ordem dos eventos única: servidor autoritativo (Quake III, Half-Life, TRIBES, Figma, Jupiter) ou simulação determinística com turnos numerados (Age of Empires). Nenhum dos sistemas documentados confia no cliente para o resultado final; Bernier e Bettner/Terrano citam trapaça como motivo explícito.
2. A resposta local imediata é universal, mas sua forma depende do gênero: predição de movimento com reexecução de comandos (Half-Life, TRIBES), aplicação otimista com transformação (Jupiter), aplicação local com descarte de atualizações conflitantes não confirmadas (Figma), e, no lockstep, a simulação continua enquanto comandos futuros viajam (Age of Empires).
3. Confiabilidade é decidida pela semântica do dado, não pelo transporte: Quake III reenvia implicitamente ao fazer delta contra o último ack; TRIBES classifica dados em quatro modalidades e notifica perda sem retransmitir; Age of Empires implementa ordenação e reenvio por turno sobre UDP. Só os sistemas de colaboração (Jupiter, Figma) usam transporte ordenado e confiável (TCP, WebSocket), porque a ordem é insumo do algoritmo de convergência.
4. O que trafega é escolhido para minimizar banda em modems: comandos em vez de estado (Age of Empires), deltas e máscaras de estado parcial (Quake III, TRIBES), mudanças por propriedade (Figma), operações de alto nível sobre widgets em vez de eventos de entrada (Jupiter).
5. Priorização e escopo aparecem quando o mundo é grande: TRIBES é o único caso que documenta interest management com prioridade por objeto; Figma separa documento (sincronizado) de metadados (banco relacional).
6. Os autores que escrevem sobre jogos de ação (Bernier) tratam a compensação de latência como decisão de design com paradoxos aceitos; os de colaboração (Wallace, Nichols et al.) aceitam anomalias raras (objetos que somem por um instante, texto inserido em região apagada) em nome da simplicidade.
7. Limiares de percepção são reportados sem método: 250 ms "despercebido" em RTS (Bettner/Terrano), "a maioria acima de 150 ms" em FPS (Bernier), "alguns segundos" ocasionais em Jupiter. São observações de desenvolvimento, não experimentos.
8. Determinismo é recurso valioso e caro: Age of Empires o usa para todo o jogo (e ganha replays e detecção de trapaça), TRIBES só para o objeto controlado, Half-Life para o código compartilhado de movimento e armas. Em todos, os autores registram o custo de disciplina de programação.
9. Instrumentação e prototipagem antecipada aparecem como lição em dois casos de épocas distintas (metering permanente em Age of Empires; playground de três clientes na Figma).
10. Dois casos relatam realimentação negativa sob perda: TRIBES (reenvio de moves aumentava o pacote e a perda) e, por construção, Quake III (delta contra ack antigo cresce com perda). Nenhum dos textos quantifica o efeito.

## Casos não incluídos e por quê

- Overwatch (GDC 2017, "Overwatch Gameplay Architecture and Netcode", Timothy Ford, Blizzard): a existência do vídeo no canal oficial da GDC no YouTube foi verificada (oEmbed retorna título e canal "GDC Festival of Gaming"; artigo de Game Developer de 2019 confirma) [F: ford2017overwatch], mas o conteúdo técnico da palestra (command frames, rollback, favor-the-shooter) não pôde ser lido nesta sessão: a página do GDC Vault está em manutenção e nenhum serviço de transcrição acessível respondeu. Sem fonte primária legível, não há caso.
- Rocket League (GDC 2018, "It IS Rocket Science! The Physics of Rocket League Detailed", Jared Cone, Psyonix): mesma situação; vídeo verificado no canal oficial da GDC via oEmbed e artigo de Game Developer de abril de 2018 [F: cone2018rocketleague], conteúdo não lido.
- Halo: Reach (GDC 2011, "I Shot You First: Networking the Gameplay of Halo: Reach", David Aldridge, Bungie): artigo de Game Developer de 31 de maio de 2011 confirma a palestra de cerca de 2 horas disponibilizada gratuitamente no GDC Vault [F: gamedeveloper2011haloreach]; a página do Vault redireciona para aviso de manutenção e o conteúdo não pôde ser lido.
- Source Engine (página "Source Multiplayer Networking" da Valve Developer Community): o servidor respondeu HTTP 403 a todas as tentativas, inclusive à versão raw da wiki. O candidato foi coberto por `rtm.case.half-life`, baseado no artigo de Bernier (2001) que a página da Valve cita como origem; valores específicos do motor Source (tick rate, cl_interp) não foram verificados e não aparecem nos documentos.
- Google Docs: nenhuma fonte primária de engenharia foi buscada além de Jupiter; o artigo de Wallace cita Google Docs como usuário de OT, mas isso é menção secundária. Jupiter foi incluído como o caso primário de OT em produção.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| bettner2001archers | tecnico | 2026-10-29 |
| sanglard2012quake3 | tecnico | 2026-10-29 |
| bernier2001latency | tecnico | 2026-10-29 |
| frohnmayer2001tribes | tecnico | 2026-10-29 |
| wallace2019figma | tecnico (fornecedor) | 2026-10-29 |
| nichols1995jupiter | academico | 2026-10-29 |
| ford2017overwatch | tecnico (vídeo; só existência verificada) | 2026-10-29 |
| cone2018rocketleague | tecnico (vídeo; só existência verificada) | 2026-10-29 |
| gamedeveloper2011haloreach | secundario | 2026-10-29 |
