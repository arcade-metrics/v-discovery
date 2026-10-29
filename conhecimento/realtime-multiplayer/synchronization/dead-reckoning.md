---
id: rtm.sync.dead-reckoning
titulo: Dead reckoning
tipo: tecnica
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2012dis, ryan2006deadreckoning, npsdisdictionary, opendisdeadreckoning, gambetta2014entity, fiedler2014snapshot, fiedler2015statesync]
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-replication }
  - { tipo: especificado-por, alvo: rtm.std.index }
  - { tipo: alternativa-a, alvo: rtm.sync.snapshot-interpolation }
  - { tipo: relacionado-a, alvo: rtm.sync.state-synchronization }
  - { tipo: relacionado-a, alvo: rtm.pred.entity-interpolation }
  - { tipo: complementa, alvo: rtm.sync.interest-management }
  - { tipo: depende-de, alvo: rtm.net.bandwidth }
termos: [dead reckoning, extrapolation, error threshold, heartbeat, DRM, Entity State PDU, convergence smoothing]
---

# Dead reckoning

## Definição e terminologia

Dead reckoning (DR) é a técnica em que cada réplica extrapola a posição e a orientação de uma entidade remota a partir do último estado recebido (posição, velocidade e, opcionalmente, aceleração e velocidade angular), e o emissor só envia uma nova atualização quando sua própria extrapolação, calculada com o mesmo algoritmo, diverge do estado real além de um limiar (*threshold*) [F: ryan2006deadreckoning]. O nome vem da navegação, em que a posição é estimada a partir de rumo, velocidade e tempo decorrido. [I]

Termos: *dead reckoning model* (DRM), nome dos algoritmos padronizados em DIS; *Entity State PDU*, a unidade de dados que carrega o estado da entidade em DIS; *heartbeat*, atualização periódica emitida mesmo sem violação de limiar; *convergence* ou *smoothing*, a transição suave da posição extrapolada para a posição corrigida [F: ryan2006deadreckoning]. Gambetta, em contexto de jogos, usa "dead reckoning" como sinônimo de extrapolação a partir de posição, velocidade, direção e aceleração anteriores [F: gambetta2014entity].

O que não é: não é interpolação (que usa só dados passados reais e atrasa a exibição) e não é simulação local completa (como em `rtm.sync.state-synchronization`); é extrapolação cinemática por entidade. [I]

## Problema que resolve

Em simulações distribuídas com muitas entidades, enviar o estado de cada uma a cada passo satura a rede. DR reduz a taxa de envio: se uma entidade viaja em linha reta a velocidade constante, sua posição pode ser extrapolada com exatidão e nenhuma atualização é necessária até que ela manobre [F: ryan2006deadreckoning]. O custo é a possibilidade de erro entre atualizações e um salto visível quando a correção chega [F: gambetta2014entity].

## Fundamentos e funcionamento

### Origem normativa: DIS, IEEE 1278.1

A norma IEEE 1278.1 define as mensagens (Protocol Data Units, PDUs) trocadas entre aplicações de simulação distribuída; a edição 1278.1-2012 foi aprovada em 2012-08-30, publicada em 2012-12-19, substitui a 1278.1-1995 e consta como "Inactive-Reserved" desde 2023-03-30, com um projeto P1278.1 ativo como sucessor [F: ieee2012dis]. A página da norma não menciona dead reckoning; o conteúdo normativo sobre DR vem de fontes que a descrevem, não do texto da norma, que não abrimos (não verificado).

Segundo Ryan e Oliver, DIS emprega DR para limitar a taxa de emissão de Entity State PDUs: cada aplicação mantém um modelo de alta fidelidade das entidades que gera e um modelo dead-reckoned; quando os dois diferem além do limiar, uma Entity State PDU é emitida [F: ryan2006deadreckoning]. Os autores afirmam que a norma (edição 1278.1a-1998, a mais recente quando escreveram) fornece um conjunto padrão de 11 algoritmos de DR para posição e orientação [F: ryan2006deadreckoning]. O dicionário de dados DIS mantido pelo NPS lista o campo *Dead Reckoning Algorithm* com os valores 0 Other, 1 Static, 2 DRM(F,P,W), 3 DRM(R,P,W), 4 DRM(R,V,W), 5 DRM(F,V,W), 6 DRM(F,P,B), 7 DRM(R,P,B), 8 DRM(R,V,B), 9 DRM(F,V,B) [F: npsdisdictionary]; isto é, oito DRMs mais Static e Other. A diferença entre "11 algoritmos" e os 10 valores enumerados não pôde ser conciliada sem o texto da norma; ver Lacunas. O *Dead Reckoning Parameter Record* do Entity State PDU tem 320 bits e inclui o algoritmo (8 bits), a aceleração linear e a velocidade angular, com 120 bits reservados [F: npsdisdictionary].

### Nomenclatura dos algoritmos

Os DRMs são identificados por três letras: a primeira indica orientação fixa (F) ou rotacionando (R); a segunda, se a taxa mantida constante é a de posição (P, velocidade constante) ou a de velocidade (V, aceleração constante); a terceira, coordenadas do mundo (W) ou do corpo (B) [F: ryan2006deadreckoning]. A biblioteca Open-DIS implementa classes correspondentes (por exemplo `DIS_DR_FPW_02`, "movimento linear constante", e `DIS_DR_RVW_04`, "movimento linear com aceleração e rotação") [F: opendisdeadreckoning].

### Equações de extrapolação

Primeira ordem (FPW): `P1 = P0 + V0·t`. Segunda ordem (FVW): `P1 = P0 + V0·t + ½·A0·t²`, onde o índice 0 denota os valores no início do intervalo e t a duração [F: ryan2006deadreckoning]. Ryan e Oliver também estudaram uma terceira ordem que usa a variação da aceleração entre as duas últimas atualizações, com pelo menos 10 operações em ponto flutuante [F: ryan2006deadreckoning]. As equações de orientação (velocidade angular, matrizes de rotação) não aparecem nas fontes abertas: não verificado.

### Limiar de erro e heartbeat

A emissão é disparada quando a diferença entre o estado real e o extrapolado excede o limiar. Ryan e Oliver apontam ambiguidade na redação da norma (seção 4.5.2.1.2.1 e B.1.1 da edição citada por eles) entre duas interpretações: diferença por componente (qualquer |Δx|, |Δy|, |Δz| acima do limiar) e diferença vetorial (|Δp| acima do limiar); a vetorial garante que a entidade nunca fique mais longe que o limiar, enquanto por componente ela pode estar a 1,56 m com limiar de 1 m (Δ = 0,9 m em cada eixo) [F: ryan2006deadreckoning]. O limiar de orientação padrão citado é de 3 graus [F: ryan2006deadreckoning].

Como uma entidade em movimento retilíneo uniforme nunca viola o limiar, ela desapareceria por timeout; o *heartbeat* resolve isso: a norma define taxas padrão por PDU, com 5 s para Entity State (`HRT_BEAT_TIMER`) e timeout igual ao multiplicador `HRT_BEAT_MPLIER` (padrão 2,4) vezes a taxa, ou seja, 12 s [F: ryan2006deadreckoning].

### Convergência suave

Quando a correção chega, trocar a posição extrapolada pela recebida produz um salto. Ryan e Oliver mencionam que técnicas de suavização podem eliminar esses saltos no display e citam trabalho anterior de Lin, Wang e Wang (1996) sobre suavização da imagem dead-reckoned [F: ryan2006deadreckoning]; esse trabalho não foi aberto (não verificado). Uma técnica concreta e verificada, de outra família, é a suavização visual de Fiedler: manter um offset entre a posição física corrigida e a visual e decaí-lo por frame com fator adaptativo (0,95 para erros até 25 cm, 0,85 para 1 m ou mais) [F: fiedler2015statesync]; o princípio se aplica a DR. [I]

## Algoritmos e modelos relevantes

Resultados do modelo de Ryan e Oliver, para uma aeronave a 200 m/s em órbita circular com limiar de 1 m e heartbeat desligado (1000 s): com raio de 1000 m, 125 PDUs por órbita em primeira ordem contra 33 em segunda ordem; com raio de 20 000 m, 628 contra 93; em todos os casos a primeira ordem exige cerca de três vezes mais PDUs [F: ryan2006deadreckoning]. Variando o limiar com raio de 5000 m: 392/71 PDUs a 0,5 m, 314/58 a 1 m, 130/34 a 5 m, 43/16 a 50 m [F: ryan2006deadreckoning]. A terceira ordem reduziu a taxa de 0,216 para 0,153 PDU/s com limiar de 5 m, mas com erro RMS praticamente igual (0,034 m contra 0,033 m), o que os autores consideram não justificar o custo [F: ryan2006deadreckoning]. O modelo concordou com um gerador de forças comparativas comercial com erro melhor que 0,1% [F: ryan2006deadreckoning].

Os autores sugerem limiares por tipo de entidade (por exemplo 1 m para navios, 10 m para aeronaves) ou adaptativos, proporcionais à velocidade: `p_threshold = p_constant·|v|`, limitado entre `p_min` e `p_max`; e observam que a relação entre velocidade, limiar e taxa de PDUs é fortemente não linear (de 0,22 PDU/s para um navio a 10 m/s com 1 m a 1,511 PDU/s para um míssil a 500 m/s com 50 m) [F: ryan2006deadreckoning]. Citam ainda Lee et al. (2003), que propõem limiares dependentes de área de interesse, para que entidades próximas recebam mais atualizações que distantes [F: ryan2006deadreckoning]; esse trabalho não foi aberto.

## Requisitos e pressupostos

- Movimento previsível em escala de tempo do intervalo entre atualizações: Gambetta afirma que DR funciona bem para carros ou navios e que interpolação é preferível quando direção e velocidade podem mudar instantaneamente, como em shooters 3D [F: gambetta2014entity].
- O emissor executa o mesmo algoritmo de extrapolação que os receptores, caso contrário o limiar não mede o erro real dos receptores [F: ryan2006deadreckoning] [I].
- Relógios razoavelmente alinhados: Ryan e Oliver citam Aggarwal et al. (2004) sobre a necessidade de relógios sincronizados para precisão em jogos com DR [F: ryan2006deadreckoning]; ver `rtm.net.clock-synchronization`.

## Vantagens e limitações

Vantagens: redução drástica da taxa de atualização para trajetórias suaves [F: ryan2006deadreckoning]; nenhum atraso de exibição adicionado [F: gambetta2014entity]; padronizado para interoperabilidade entre simuladores [F: ryan2006deadreckoning].

Limitações: salto de correção quando a previsão falha [F: gambetta2014entity]; limiares padrão pequenos demais para entidades rápidas [F: ryan2006deadreckoning]; a extrapolação ignora colisões e restrições: Fiedler observa que cubos extrapolados atravessam o chão e são corrigidos depois, que extrapolação só funciona razoavelmente para movimento quase linear e por 50 a 250 ms, e recomenda evitá-la para corpos rígidos [F: fiedler2014snapshot]. Com física não determinística ou interações frequentes entre objetos, a divergência cresce rápido e DR cinemático deixa de ser suficiente; a alternativa é simulação local com correções (`rtm.sync.state-synchronization`). [I]

## Alternativas e comparações

| Aspecto | Dead reckoning | Snapshot/entity interpolation | State synchronization |
|---|---|---|---|
| Atraso de exibição | nenhum [F: gambetta2014entity] | 100 ms a 350 ms [F: gambetta2014entity] [F: fiedler2014snapshot] | 4 a 5 frames [F: fiedler2015statesync] |
| Artefato típico | salto na correção [F: gambetta2014entity] | nenhum, movimento atrasado [F: gambetta2014entity] | pops sob perda em rajada [F: fiedler2015statesync] |
| Taxa de envio | dirigida por limiar + heartbeat [F: ryan2006deadreckoning] | fixa [F: fiedler2014snapshot] | orçamento + prioridade [F: fiedler2015statesync] |
| Entidades ideais | veículos, aeronaves [F: gambetta2014entity] [F: ryan2006deadreckoning] | avatares ágeis [F: gambetta2014entity] | física interativa [F: fiedler2015statesync] |

## Métricas e métodos de avaliação

PDUs por segundo ou por manobra; erro RMS entre trajetória real e extrapolada; fração de heartbeat sobre PDUs totais [F: ryan2006deadreckoning]. Lin e Schab (1994), citados por Ryan e Oliver, avaliaram DR por carga de rede, carga computacional, precisão e suavidade visual [F: ryan2006deadreckoning] (não aberto).

## Exemplo técnico independente de domínio

```
# emissor: mantém estado real e réplica dead-reckoned com o mesmo DRM dos receptores
a_cada_passo(dt):
    real = simular(real, dt)
    dr.t += dt
    p_dr = dr.p0 + dr.v0*dr.t + 0.5*dr.a0*dr.t^2          # FVW (segunda ordem)
    se |real.p - p_dr| > limiar_pos ou angulo(real.rot, rot_dr) > limiar_rot
       ou dr.t >= heartbeat:                               # 5 s por padrão em DIS
        enviar(EntityState{p: real.p, v: real.v, a: real.a, rot, w, drm: FVW})
        dr = {p0: real.p, v0: real.v, a0: real.a, t: 0}

# receptor: extrapola e converge suavemente ao receber correção
ao_receber(u): alvo = u; alvo.t = 0; offset = pos_exibida - u.p
a_cada_frame(dt):
    alvo.t += dt
    p = alvo.p + alvo.v*alvo.t + 0.5*alvo.a*alvo.t^2
    offset *= fator(|offset|)                              # decaimento, ex.: 0,85 a 0,95
    exibir(p + offset)
```

## Relações com outros conceitos

Parte de `rtm.sync.state-replication`. A norma IEEE 1278.1 deve constar em `rtm.std.index`. Alternativa a `rtm.sync.snapshot-interpolation` e a `rtm.pred.entity-interpolation` para entidades remotas; antecessor conceitual da extrapolação em `rtm.sync.state-synchronization`. Limiares dependentes de distância ligam DR a `rtm.sync.interest-management`.

## Lacunas e questões abertas

- O texto da IEEE 1278.1 (qualquer edição) não foi aberto; equações de orientação, valores padrão de limiar e a contagem exata de algoritmos (11 segundo Ryan e Oliver; 10 valores enumerados no dicionário NPS) ficam não verificados.
- Ryan e Oliver: o PDF não traz ano nem venue; o ano 2006 é inferido dos metadados do arquivo e da biografia de Oliver (ingressou na DSTO em 2006). Os autores anunciam um artigo futuro sobre DR de orientação; não localizado.
- Trabalhos citados por Ryan e Oliver (Lin e Schab 1994; Lin, Wang e Wang 1996; Lee et al. 2003; Aggarwal et al. 2004) não foram abertos.
- Não há fonte verificada sobre DR em motores de jogo modernos com física não determinística além das observações de Fiedler.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ieee2012dis | normativo (só página da norma) | 2026-10-29 |
| ryan2006deadreckoning | academico | 2026-10-29 |
| npsdisdictionary | secundario | 2026-10-29 |
| opendisdeadreckoning | secundario | 2026-10-29 |
| gambetta2014entity | tecnico | 2026-10-29 |
| fiedler2014snapshot | tecnico | 2026-10-29 |
| fiedler2015statesync | tecnico | 2026-10-29 |
