---
produto: VUOO
slug: vuoo-microjogos
etapa: base/captura-de-interacao
status: cópia de referência, revisada para os microjogos
atualizado_em: 2026-11-05
---

# Base: captura de interação, sensores e dados do app

Recorte copiado da discussão de infraestrutura de 05/11/2026, para esta pasta ser autossuficiente. Os números são estimativa, sem medição: servem para dimensionar.

## 1. Decisões já tomadas

| Decisão |
|---|
| **Captura no celular e no tablet: toque, gestos e sensores inerciais. Sem visão computacional.** Também se registra o uso do app inteiro, além dos eventos de atividade. |
| **Sensores e toque são normalizados no aparelho** para permitir comparação geral. Taxa máxima inicial de 100 Hz. Taxas diferentes são aceitas por sistema e aparelho, sempre registradas e tratadas depois na estatística. |
| **Offline:** trilhas baixadas no aparelho; resultados guardados e enviados quando houver rede. |

## 2. O que se captura

| Fluxo | O quê | Bruto/dia/aluno | Comprimido |
|---|---|---|---|
| Eventos de atividade | resposta, acerto, tentativa, tempo de reação | ~150 KB | ~30 KB |
| Toque e gestos | toques e arrastos, amostrados só durante o contato | ~200 KB | ~60 KB |
| Sensores inerciais | acelerômetro + giroscópio, 6 eixos, 60 a 100 Hz, só dentro da atividade | ~1 a 1,7 MB | ~0,4 a 0,7 MB |
| Uso do app | abertura, telas, navegação, erros | ~30 KB | ~10 KB |

Total: 0,5 a 0,8 MB comprimido por aluno por dia (10 a 25 MB por mês). Os sensores são quase todo o volume, e calcular medidas no aparelho é a principal forma de reduzir.

Rede da família: eventos de atividade e de uso vão por qualquer rede; séries brutas, por padrão, só por Wi-Fi.

## 3. Latência

| Laço | Onde roda | Requisito |
|---|---|---|
| Estímulo → resposta → feedback | no aparelho | um quadro, sem rede |
| Progressão na trilha | no aparelho, com as regras do pacote | sem rede |
| Envio de resultados | quando houver rede | de minutos a dias |

Não há tempo real de rede. O "tempo real" é de **medição**, resolvido no aparelho com relógio monotônico, âncora de sessão e número de sequência. Toda tela de professor mostra "sincronizado em …".

## 4. Normalização no aparelho

| Camada | Diferença entre plataformas | Normalização |
|---|---|---|
| Unidades | iOS em g, Android em m/s²; gravidade separada de jeitos diferentes | SI (m/s², rad/s), gravidade separada, orientação da tela registrada |
| Tempo | carimbos desde o boot; a taxa real oscila | relógio monotônico; reamostragem para a taxa-alvo; taxa real registrada |
| Toque | pixel, ponto, dp; telas diferentes; taxa de 60 a 240 Hz; pressão ausente em muitos aparelhos | coordenadas em mm físicos e relativas ao alvo; tempo desde o início do estímulo |
| Aparelho | ruído do sensor e atraso do toque variam por modelo | perfil do aparelho; alguns segundos de "aparelho parado" no início para medir o ruído |
| Medidas | — | calculadas no aparelho: tempo de reação, tempo de movimento, desvio de trajetória, jerk, energia na faixa de tremor… (lista a definir) |

Regras:

- **Uma implementação só** para Android e iOS. Duas implementações quebram a comparação.
- **Versionada:** cada evento leva a versão do normalizador e o perfil do aparelho.
- **Amostra bruta:** uma fração das sessões sobe em bruto, só por Wi-Fi, para validar o normalizador.
- **Efeito do aparelho** é estimado estatisticamente no servidor. Não há medição publicada de atraso em aparelhos usados por crianças, por isso será preciso um banco de testes próprio.

## 5. Eventos

- Envelope **CloudEvents 1.0**, com sequência por sessão, carimbo monotônico, versão do conteúdo e da configuração ativa. O ator é o UUID interno, nunca nome nem CPF.
- Dois fluxos: **atividade** (pedagógico) e **uso do app** (produto), com finalidade, base legal e retenção próprias.
- Séries de toque e sensores vão como bloco comprimido, referenciado pelo evento discreto.
- Fila local no aparelho; envio em lote e idempotente; só sai da fila o que o servidor confirmou.
- Nenhum SDK de analytics ou crash de terceiros mandando dado para fora.
- Exportação em xAPI e Caliper.

## 6. Pendente

- Lista de medidas calculadas no aparelho e fração de amostra bruta.
- Peso do pacote de trilha e validade do login sem rede.
