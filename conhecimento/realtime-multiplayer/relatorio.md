---
id: rtm.relatorio
titulo: Relatório da primeira versão do domínio tempo real e multiplayer
tipo: relatorio
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Relatório: primeira versão do domínio tempo real e multiplayer

Data: 2026-10-29. Esta é a "primeira versão funcional" pedida pelo brief: estrutura, mapa conceitual, bibliografia inicial e documentos principais fundamentados em fontes verificadas. Todos os documentos estão em `status: rascunho`; a passagem para `revisado` exige o checklist de `_modelo/checklist-revisao.md` por leitor humano.

## Método aplicado

Nove frentes de pesquisa em paralelo, uma por área, cada uma restrita a abrir as fontes antes de citá-las. Cada frente produziu seus documentos e um fragmento de bibliografia e índice; os fragmentos foram mesclados em `referencias/bibliografia.bib` e `referencias/indice-fontes.md` por `_modelo/mesclar_referencias.py`. O validador `_modelo/validar.py` confirmou: ids únicos com prefixo correto, todos os alvos de relação existentes, todas as chaves de fonte presentes na bibliografia, nenhuma menção a produto consumidor.

## Cobertura

| Área | Documentos | Observação |
|---|---|---|
| realtime | 2 | fundamentos hard/firm/soft, padrões de comunicação |
| networking | 7 | latência, jitter, perda, ordenação, banda, relógios físicos e lógicos |
| protocols | 8 | TCP, UDP, WebSocket, WebRTC, WebTransport, QUIC, HTTP streaming, comparação |
| standards | 1 | índice de RFCs e especificações com status normativo |
| architectures | 6 | autoritativo, relay, P2P, lockstep, orientado a eventos, comparação |
| synchronization | 8 | replicação, snapshot interpolation, state sync, dead reckoning, delta, interest management, CRDT, OT |
| prediction-reconciliation | 5 | predição, reconciliação, interpolação de entidades, lag compensation, comparação |
| multiplayer | 5 | salas, matchmaking, presença, turnos, ciclo de sessão |
| frameworks | 4 | Nakama 3.41.0, Colyseus 0.18.10, alternativas, comparação |
| reliability-security | 6 | reconexão, tolerância a falhas, semântica de entrega, autenticação, cheating, transporte |
| performance-testing | 4 | métricas, limiares de QoE, carga, emulação |
| case-studies | 7 | índice mais Age of Empires, Quake III, Half-Life, TRIBES, Figma, Jupiter |
| raiz | 6 | brief, README, glossário, mapa, plano de ids, este relatório |

Totais: 65 documentos conceituais, 617 relações tipadas, 375 fontes na bibliografia.

Fontes por tipo: 163 de fornecedor, 80 normativas, 75 técnicas, 44 acadêmicas, 13 secundárias. O peso de fornecedor vem dos quatro documentos de frameworks (118 fontes), que dependem de versão e têm data de consulta registrada.

Marcas de afirmação no corpo dos documentos: 2.395 citações de fato com chave de fonte, 519 interpretações marcadas `[I]`, 32 hipóteses marcadas `[H]`.

## O que o brief pediu e onde está

| Entregável | Local |
|---|---|
| Estrutura de diretórios | `realtime-multiplayer/` (12 pastas) |
| README com escopo, organização e contribuição | `README.md` do domínio e `conhecimento/README.md` |
| Glossário técnico | `glossario.md` (cerca de 170 entradas selecionadas de 436 termos) |
| Mapa de conceitos e dependências | `mapa-conceitos.md` (visão geral escrita à mão mais seção gerada com todos os docs e relações) |
| Documentos técnicos com fontes primárias | as 12 pastas |
| Bibliografia BibTeX | `conhecimento/referencias/bibliografia.bib` |
| Índice de referências com URL, tipo e data | `conhecimento/referencias/indice-fontes.md` |
| Critérios de qualidade e checklist | `conhecimento/_modelo/metodo-e-qualidade.md` e `checklist-revisao.md` |
| Relatório final | este arquivo |

Ampliação em relação ao brief original: turnos, colaboração (CRDT e OT), presença e ciclo de sessão receberam documentos próprios, porque têm requisitos diferentes dos jogos de ação e literatura própria.

## Fontes que não puderam ser verificadas

Padrão recorrente: a wiki da Valve (`developer.valvesoftware.com`) e as bibliotecas digitais da ACM, IEEE e Springer, além do HAL/Inria, bloquearam o acesso automatizado. Consequências:

- **Bernier 2001** (Valve, lag compensation): texto lido em espelhos (PDF em gamedevs.org, cópia integral em cnblogs). Cada documento que o cita diz de onde leu. O artigo "Source Multiplayer Networking" da Valve não foi lido; valores de tick rate e `cl_interp` do Source não aparecem em nenhum documento.
- **Shapiro et al. 2011** (CRDT): só metadados; o conteúdo foi citado por meio de Preguiça 2018 (arXiv, texto integral). A entrada BibTeX registra isso.
- **Ellis e Gibbs 1989** (OT): lido em cópia de curso; **Nichols et al. 1995** (Jupiter): PDF lido em espelho; **Ressel et al. 1996** (TP1/TP2): só metadados, formulação marcada como não verificada.
- **Herbrich et al. 2006** (TrueSkill): PDF com fontes ilegíveis; números vêm da página do projeto (fornecedor).
- **ITU-T G.1032 e G.1072**: só sumários; coeficientes não verificados.
- **Webb e Soh 2007** (cheating), **Ignat et al. 2015** (latência em colaboração), **Liu e Layland 1973**, **Kopetz 1997**: só metadados ou fonte secundária.
- **Palestras GDC** (Overwatch 2017, Rocket League 2018, Halo Reach 2011): existência confirmada, conteúdo inacessível (GDC Vault indisponível); casos não escritos.
- **IEEE 1278.1** (DIS, dead reckoning): só a página da norma; equações e limiares não verificados no texto normativo.

Todas essas situações estão marcadas no documento correspondente e na nota da entrada BibTeX.

## Lacunas de conhecimento e questões abertas

Consolidadas das nove frentes. As quatro primeiras respondem às perguntas abertas do brief.

1. **Limiares de latência por gênero.** Há evidência verificada para ação rápida (cerca de 100 ms), terceira pessoa (cerca de 500 ms) e estratégia (cerca de 1000 ms), de Claypool e Claypool 2006, e para corrida (50 ms não crítico, acima de 150 ms degrada), de Pantel e Wolf 2002 com n=12. Não há evidência numérica verificada para jogos por turnos nem para colaboração em tempo real. Os limiares reportados nos estudos de caso (250 a 500 ms em RTS) vêm sem método.
2. **WebTransport em 2026.** Drafts IETF em Working Group Last Call (versões de julho de 2026) e API W3C em Candidate Recommendation; MDN rotula como "newly available" desde março de 2026. Status pode mudar em meses; reverificar `rtm.proto.webtransport` e `rtm.std.index` no primeiro semestre de 2027.
3. **Nakama vs Colyseus.** A comparação em `rtm.fw.comparison` usa critérios verificáveis (licença, linguagem, autoridade, transporte, sincronização, matchmaking, presença, reconexão, persistência, escala, serviço gerenciado, maturidade). Não existe benchmark independente comparável; os números de capacidade são do fornecedor (Colyseus estima 1.000 a 2.000 conexões por vCPU; Nakama publica benchmarks sem data nem percentis). Nenhum dos dois documenta limites numéricos do modo relay.
4. **QoE fora de jogos de ação.** Nenhuma métrica padronizada; G.1032 e G.1072 são específicas de gaming e cloud gaming. "Misprediction" não tem definição normativa como métrica.
5. **Comparações quantitativas ausentes.** Não há estudo revisado por pares comparando snapshot interpolation e state synchronization, nem as cinco arquiteturas sob a mesma carga, nem OT e CRDT no mesmo caso de uso, nem head-of-line blocking medido entre WebSocket, WebTransport e WebRTC sob a mesma perda.
6. **Dados de redes atuais.** Faltam distribuições medidas de latência, jitter e perda em redes móveis recentes para preencher a matriz de cenários de `rtm.perf.network-emulation` com números; o traço de perda em rajada disponível é de ADSL em 2008.
7. **Combinação de técnicas.** Como combinar CRDT com invariantes impostas por servidor, e replicação de simulação com CRDT no mesmo sistema, não tem fonte.
8. **Detecção de trapaça em P2P e lockstep** (commit de entradas, lag switch): sem fonte primária; marcado como hipótese em `rtm.sec.cheating`.
9. **Sucessão de RFCs.** A RFC 8446 (TLS 1.3) foi obsoletada pela RFC 9846 em 2026, a RFC 8829 (JSEP) pela RFC 9429, a RFC 768 foi atualizada pela RFC 9868 e a RFC 9147 pela RFC 9853. `rtm.std.index` registra; `rtm.sec.transport-security` cita o conteúdo da RFC 8446 e tem nota para conferir na sucessora.
10. **Ecossistema de frameworks em mudança.** Hathora encerrado (maio de 2026, fonte secundária), Unity Multiplay repassado (março de 2026), PartyKit hospedado desligado (outubro de 2026). `rtm.fw.alternatives` deve ser revisado em seis meses.
11. **Datas de fontes técnicas.** Páginas de Gambetta e o PDF do TRIBES não trazem data; os anos nas chaves (2014, 2001) seguem convenção e estão marcados como não verificados no BibTeX.

## Inconsistências conhecidas entre documentos

- Chaves duplicadas em fragmentos com URLs de espelhos diferentes (nichols1995jupiter, shapiro2011crdt, bernier2001latency, rfc768, oasis2019mqtt, claypool2006latency). A mesclagem manteve a primeira ocorrência por ordem alfabética de fragmento; todas apontam para a mesma obra. Não afeta a rastreabilidade.
- Discrepância de citação do TrueSkill (NIPS 19 de 2006 vs volume publicado em 2007), adotada a primeira com nota.
- "11 algoritmos" de dead reckoning em Ryan e Oliver vs 10 valores enumerados no dicionário NPS; não conciliável sem o texto da norma.
- Colyseus: os documentos de multiplayer e de frameworks usam a mesma versão (0.18), verificado.

## Próximos passos sugeridos

1. **Revisão humana** dos 65 documentos com o checklist, começando pelos de comparação (`rtm.proto.comparison`, `rtm.arch.comparison`, `rtm.pred.comparison`, `rtm.fw.comparison`), que concentram as sínteses `[I]`.
2. **Promover relações.** 282 das 617 relações são `relacionado-a`. Reclassificar as que são de fato `depende-de` ou `complementa` melhora o grafo e a conversão futura para SKOS/OWL.
3. **Segunda rodada de fontes bloqueadas** com acesso institucional (ACM, IEEE, Springer, ITU) para fechar as lacunas 1, 4 e 5 e os estudos de caso de Overwatch, Rocket League e Halo Reach.
4. **Documentos candidatos** identificados pelas frentes: rollback netcode como documento próprio (hoje dentro de lockstep); event sourcing aplicado a sessões por turnos como estudo de caso; latência adicionada por brokers em cenários interativos; sincronização de relógio cliente-servidor em navegadores com medição.
5. **Agendar reverificação** em abril de 2027 de `rtm.proto.webtransport`, `rtm.std.index`, `rtm.fw.nakama`, `rtm.fw.colyseus` e `rtm.fw.alternatives`, que dependem de versão.
6. **Conversão para grafo.** Com ids, relações tipadas e termos no frontmatter, um script pode gerar SKOS a partir dos arquivos; vale fazê-lo junto com o domínio `grafo-conhecimento-educacional`, que definirá o vocabulário.
