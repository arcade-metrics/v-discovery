---
id: rtm.perf.network-emulation
titulo: Emulação de condições de rede
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [tcnetem2026, clumsy2026, toxiproxy2026, chrome2026network, chrome2026throttling, fiedler2014snapshot, fiedler2014lockstep, rfc3393, rfc7680, principlesofchaos2019]
relacoes:
  - { tipo: depende-de, alvo: rtm.perf.metrics }
  - { tipo: depende-de, alvo: rtm.net.latency }
  - { tipo: depende-de, alvo: rtm.net.jitter }
  - { tipo: depende-de, alvo: rtm.net.packet-loss }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
  - { tipo: complementa, alvo: rtm.perf.load-testing }
  - { tipo: complementa, alvo: rtm.perf.qoe-thresholds }
  - { tipo: complementa, alvo: rtm.rel.reconnection }
  - { tipo: complementa, alvo: rtm.rel.fault-tolerance }
  - { tipo: relacionado-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.arch.deterministic-lockstep }
  - { tipo: avaliado-por, alvo: rtm.perf.metrics }
termos: [netem, qdisc, delay, loss, reorder, duplicate, corrupt, rate, Gilbert-Elliott, toxic, throttling, matriz de cenários]
---

# Emulação de condições de rede

## Definição e terminologia

Emulação de rede é a introdução deliberada e controlada de latência, variação de atraso, perda, duplicação, reordenação, corrupção e limite de banda no caminho entre cliente e servidor, para observar o sistema sob condições que a rede local do desenvolvedor nunca produz. Distingue-se de *simulação* (modelo matemático sem tráfego real) e de *teste de carga* (muitos clientes; ver `rtm.perf.load-testing`): aqui o tráfego é real e o que varia é a qualidade do caminho.

Ferramentas com documentação verificada: **tc-netem** (Linux), disciplina de fila que "can impose delay, loss, duplication, corruption, reordering, and rate limits on packets" [F: tcnetem2026]; **clumsy** (Windows), que usa WinDivert para capturar pacotes vivos e aplicar "lag/drop/tamper/.." antes de reenviá-los [F: clumsy2026]; **Toxiproxy**, "a TCP proxy written in Go" com cliente HTTP, "a framework for simulating network conditions" [F: toxiproxy2026]; e o **throttling do Chrome DevTools**, com presets e perfis personalizados [F: chrome2026network; F: chrome2026throttling].

## Problema que resolve

Técnicas como interpolação de snapshots, predição e reconciliação, reconexão e deduplicação (ver `rtm.sync.snapshot-interpolation`, `rtm.pred.client-side-prediction`, `rtm.rel.reconnection`, `rtm.rel.delivery-semantics`) só se manifestam, e só têm bugs visíveis, com latência, jitter e perda. Sem emulação, o desenvolvimento acontece a sub-milissegundo e zero perda, e os defeitos aparecem nos usuários. A emulação também é o instrumento para reproduzir os experimentos de `rtm.perf.qoe-thresholds` e os eventos de `rtm.rel.fault-tolerance`.

## Fundamentos e funcionamento

### tc-netem (Linux)

A página de manual documenta as opções [F: tcnetem2026]:

- `delay TIME [JITTER [CORRELATION]] [distribution {uniform|normal|pareto|paretonormal}]`: latência com variação opcional e correlação entre pacotes consecutivos; exemplo `tc qdisc change dev eth0 root netem delay 100ms 20ms distribution normal`.
- `loss random PERCENT [CORRELATION]`: perda independente; `loss state p13 [p31 [p32 [p23 [p14]]]]`: cadeia de Markov de 4 estados (bom, rajada, perda independente); `loss gemodel p [r [1-h [1-k]]]`: modelo Gilbert-Elliott de perda em rajada; flag `ecn` marca em vez de descartar; exemplo `tc qdisc change dev eth0 root netem loss 0.1%`.
- `corrupt PERCENT`: altera conteúdo em posição aleatória; `duplicate PERCENT`: copia pacotes; exemplo `tc qdisc change dev eth0 root netem duplicate 1%`.
- `reorder PERCENT [CORRELATION] [gap DISTANCE]`: envia uma fração imediatamente e atrasa o resto; exemplo `tc qdisc change dev eth0 root netem delay 10ms reorder 25% 50%`; alternativa `gap 5 delay 10ms` envia cada quinto pacote imediatamente.
- `rate RATE [PACKETOVERHEAD [CELLSIZE [CELLOVERHEAD]]]`: limita vazão emulando sobrecarga de enlace; exemplo `tc qdisc add dev eth0 root netem rate 5kbit 20 100 5`.
- `slot` emula meios com janelas de transmissão; `seed` torna perda e corrupção reproduzíveis.

Limitações documentadas: a precisão é limitada pela granularidade do timer do kernel; "Reordering needs enough delay", pois sem atraso maior que o intervalo entre pacotes não há reordenação; para resultados realistas com TCP, "netem must be placed on the ingress of the receiver host" por causa do TCP Small Queues; combinar netem com outras qdiscs "may not always work" [F: tcnetem2026]. [I] Para UDP de jogo, aplicar nas duas interfaces (cliente e servidor, ou nos dois sentidos de um roteador intermediário) para que ida e volta sejam independentes; o `seed` é o que torna um cenário reproduzível em CI.

### clumsy (Windows)

Oferece as funções Lag (segura pacotes), Drop (descarta aleatoriamente), Throttle (bloqueia por um intervalo e envia em lote), Duplicate, Out of order e Tamper (altera bits); captura só os pacotes que casam com um filtro por direção, protocolo (TCP/UDP), porta ou IP, "leaving others untouched"; funciona em Windows Vista/7 e posteriores [F: clumsy2026]. A própria página o descreve como "an easy and painless (though suboptimal) option" [F: clumsy2026]. [I] É a ferramenta de mesa do desenvolvedor Windows: sem configuração de rede, filtrável por porta do jogo; não substitui netem para experimentos controlados.

### Toxiproxy

Proxy TCP com "toxics" aplicáveis por sentido (`upstream`: cliente para servidor; `downstream`: servidor para cliente, padrão da latência) e com `toxicity` (probabilidade de aplicação, padrão 100%): `latency` (com `jitter`), `bandwidth` (KB/s), `slow_close`, `timeout` (bloqueia dados e fecha após o tempo; 0 descarta até remoção), `reset_peer` (RST), `slicer` (fatia o fluxo com atraso opcional), `limit_data` e `packet_loss` [F: toxiproxy2026]. O projeto se apresenta como meio de "prove with tests that your application doesn't have single points of failure", com uso típico de envolver um bloco de teste num toxic e afirmar o comportamento [F: toxiproxy2026]. [I] Por ser TCP, serve a WebSocket e a dependências (banco de checkpoint, matchmaking), não a UDP; é a ferramenta natural para testes automatizados de reconexão (`timeout`, `reset_peer`) e de degradação de dependências (`rtm.rel.fault-tolerance`).

### Chrome DevTools

O painel Network oferece presets "fast 4G, slow 4G, 3G", a opção Offline e perfis personalizados; a documentação registra que o DevTools também aplica throttling a conexões WebSocket (desde a versão 99) e exibe um ícone de aviso enquanto ativo [F: chrome2026network]. Um perfil personalizado define nome, download e upload em Kbps, latência em ms, perda de pacotes em porcentagem, tamanho da fila de pacotes e um flag de reordenação; a página observa que os parâmetros de pacote permitem testar aplicações WebRTC sem software de terceiros [F: chrome2026throttling]. Os valores numéricos dos presets não constam nas páginas consultadas (não verificado). [I] É emulação no navegador, por aba; serve para clientes web, não para o servidor nem para clientes nativos.

### Condições usadas por praticantes

Fiedler documenta as condições sob as quais testa suas demonstrações: no artigo sobre interpolação de snapshots, os vídeos foram gravados "at 5% packet loss with +/- 2 frames of jitter @ 60fps" a 10 pacotes por segundo, e o autor relata que "the amount of delay that works best at 2-5% packet loss is 3X the packet send rate" [F: fiedler2014snapshot]; no artigo sobre lockstep determinístico, compara TCP "at 100ms latency and 1% packet loss", TCP "at 250ms latency and 5% packet loss" e UDP com entradas redundantes "with 2 seconds of latency and 25% packet loss" [F: fiedler2014lockstep]. [I] Esses pares (100 ms/1%, 250 ms/5%) são úteis como pontos de uma matriz, porque vêm de um praticante que os usa para demonstrar quando uma técnica quebra; não são medidas de redes reais.

### Matriz de cenários

[I] Proposta qualitativa, com os números citados de fonte onde existem; os demais eixos devem ser preenchidos com medições da própria população de usuários:

| Cenário | Latência | Variação | Perda | Banda | Eventos | Fonte dos números |
|---|---|---|---|---|---|---|
| Local | ~0 | ~0 | 0 | ilimitada | nenhum | linha de base |
| Boa | baixa, estável | pequena | ~0 | ampla | nenhum | sem número verificado |
| Média | 100 ms | moderada | 1% | ampla | nenhum | par de Fiedler [F: fiedler2014lockstep] |
| Ruim | 250 ms | alta, distribuição normal | 5% | limitada | reordenação | par de Fiedler [F: fiedler2014lockstep]; 5% de perda em snapshots [F: fiedler2014snapshot] |
| Móvel | variável | rajadas (Gilbert-Elliott) | em rajada | variável | queda total de 5 a 30 s; troca de IP | modelo `gemodel` do netem [F: tcnetem2026]; durações sem fonte |
| Hostil | 2 s | alta | 25% | mínima | reset, timeout | stress de Fiedler [F: fiedler2014lockstep] |

Cada cenário deve registrar a métrica (ver `rtm.perf.metrics`) e o critério: por exemplo, em "Ruim", mispredictions por minuto e p99 do RTT de aplicação dentro do limiar da classe (ver `rtm.perf.qoe-thresholds`); em "Móvel", tempo de reconexão e zero duplicação de comandos (ver `rtm.rel.delivery-semantics`).

### Variação de atraso versus "jitter"

A RFC 3393 evita o termo "jitter" por ambíguo e define IPDV como diferença entre atrasos de ida de pacotes selecionados [F: rfc3393, §1.1, §2.4]; o parâmetro `JITTER` do netem é a amplitude da variação em torno de `TIME`, com distribuição escolhível [F: tcnetem2026]. [I] Ao emular, declarar a distribuição e a correlação; perda e atraso independentes por pacote (o padrão sem correlação) são o caso mais benigno; redes reais têm rajadas, que o `gemodel` e a correlação representam melhor. A RFC 7680 lembra que atraso acima do limiar é contado como perda [F: rfc7680, §2.4], o que o `timeout` do Toxiproxy e o `delay` extremo do netem produzem de formas distintas.

## Requisitos e pressupostos

- Emulação em interface ou proxy entre processos reais; emular dentro do próprio processo do jogo (buffer de pacotes com atraso) é útil em desenvolvimento, mas não exercita a pilha de rede do sistema operacional [I].
- Reprodutibilidade: `seed` no netem [F: tcnetem2026]; `toxicity` fixa em 100% no Toxiproxy para testes determinísticos, menor para caos [F: toxiproxy2026].
- Medir o que se emulou: um ping de aplicação confirma que a latência configurada chegou ao caminho certo.

## Vantagens e limitações

- netem é o mais completo e o único com modelos de rajada; exige Linux e privilégio, e tem as restrições de posição e timer documentadas [F: tcnetem2026].
- Toxiproxy é programável por API e ideal para CI; só TCP [F: toxiproxy2026].
- clumsy e DevTools são de uso imediato na máquina do desenvolvedor; não são reproduzíveis por script da mesma forma.
- Nenhuma ferramenta emula mudança de endereço IP (troca Wi-Fi/celular); isso exige desligar e religar interfaces ou usar NAT dinâmico, sem fonte verificada para um método padrão.

## Alternativas e comparações

| Ferramenta | Plataforma | Camada | UDP | Rajadas | Scriptável |
|---|---|---|---|---|---|
| tc-netem | Linux | IP (qdisc) | sim | sim (`state`, `gemodel`) [F: tcnetem2026] | sim |
| clumsy | Windows | pacote (WinDivert) | sim [F: clumsy2026] | não documentado | não documentado |
| Toxiproxy | qualquer (Go) | TCP (proxy) | não [F: toxiproxy2026] | via `toxicity` | sim (HTTP) |
| Chrome DevTools | navegador | aba | só WebRTC via parâmetros de pacote [F: chrome2026throttling] | não | não |

## Métricas e métodos de avaliação

Ver `rtm.perf.metrics`. Para cada cenário: RTT p50/p95/p99 medido pela aplicação (verifica a emulação), perda e reordenação observadas por sequência, mispredictions por minuto, tamanho de buffer de interpolação, tempo de reconexão. Em experimentos de caos, comparar steady state entre grupo com e sem emulação [F: principlesofchaos2019].

## Exemplo técnico independente de domínio

```text
# Cenario "Ruim" com netem, reproduzivel (comandos conforme a pagina de manual)
tc qdisc add dev eth0 root netem delay 250ms 40ms distribution normal \
    loss gemodel 5% 30% reorder 2% 50% rate 2mbit seed 42
# ... executar o cliente, coletar metricas ...
tc qdisc del dev eth0 root

# Teste automatizado de reconexao com Toxiproxy (pseudocodigo)
proxy = toxiproxy.create("game", listen = ":9000", upstream = "server:8000")
client.connect("localhost:9000") ; client.join(room)
proxy.add_toxic("drop", type = "timeout", stream = "downstream", attrs = {timeout = 0})
sleep(10 s)                                   # dentro da janela de graca
proxy.remove_toxic("drop")
assert client.reconnected_within(5 s) and client.state == server.state(room)
assert server.duplicates_applied(client) == 0
```

## Relações com outros conceitos

Depende de `rtm.perf.metrics` e das propriedades de rede (`rtm.net.latency`, `rtm.net.jitter`, `rtm.net.packet-loss`, `rtm.net.bandwidth`). Complementa `rtm.perf.load-testing` (carga sob rede ruim), `rtm.perf.qoe-thresholds` (reprodução de experimentos), `rtm.rel.reconnection` e `rtm.rel.fault-tolerance`. Relaciona-se a `rtm.sync.snapshot-interpolation` e `rtm.arch.deterministic-lockstep`, cujas demonstrações de referência usam as condições citadas. Avaliado por `rtm.perf.metrics`.

## Lacunas e questões abertas

- Valores numéricos dos presets de throttling do Chrome (Fast 4G, Slow 4G, 3G): não constam nas páginas consultadas.
- Não foi localizada nesta sessão fonte com distribuições medidas de latência, jitter e perda em redes móveis atuais para preencher os cenários "Boa" e "Móvel" com números.
- Fiedler usa as condições em demonstrações; não foi localizado texto em que ele recomende explicitamente emular rede ruim durante o desenvolvimento, embora a prática esteja implícita; registrado como prática do autor, não como recomendação citada.
- Método padrão para emular troca de endereço IP (migração de rede) não verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| tcnetem2026 | tecnico | 2026-10-29 |
| clumsy2026 | tecnico | 2026-10-29 |
| toxiproxy2026 | tecnico | 2026-10-29 |
| chrome2026network | fornecedor | 2026-10-29 |
| chrome2026throttling | fornecedor | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2014lockstep | tecnico | 2026-10-29 |
| rfc3393 | normativo | 2026-10-29 |
| rfc7680 | normativo | 2026-10-29 |
| principlesofchaos2019 | tecnico | 2026-10-29 |
