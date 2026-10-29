# Rubricas de qualidade

## Requisito

Bom quando: tem uma situação, um comportamento observável e um sujeito claro; pode ser verificado por alguém que não escreveu; não embute decisão de implementação sem motivo.

| Fraco | Melhor |
|-------|--------|
| O app deve ser rápido | Quando a tela de histórico abre, os últimos 30 registros aparecem em até 1s usando cache local |
| Suporte a notificações | Quando o usuário não registra treino por 3 dias, enviar uma notificação no horário habitual dele, no máximo 1 por semana |
| Boa experiência de cadastro | O usuário chega ao primeiro registro sem criar conta; a conta só é pedida ao sincronizar um segundo aparelho |
| O sistema deve usar PostgreSQL | O histórico precisa sobreviver à troca de aparelho e suportar consulta por período (a escolha do banco fica no plano técnico) |

Teste rápido: dá para escrever um critério de aceite a partir dele sem perguntar nada? Se não, falta informação.

## Métrica

Bom quando: o produto consegue mexer nela, ela reflete valor entregue, e você sabe de onde vem o número.

| Fraco | Melhor | Por quê |
|-------|--------|---------|
| Downloads | % que registra o segundo treino em 7 dias | mede hábito, não curiosidade |
| Tempo no app | Tempo até o primeiro registro concluído | aqui, menos é melhor |
| NPS no mês 1 | % que volta na semana 4 | comportamento acima de opinião |

Para cada métrica defina: fonte do dado, baseline (ou `[A CONFIRMAR]`), meta e horizonte. E um **contra-indicador**: o número que, se subir junto, revela que você otimizou a coisa errada.

## Job to be done

Formato útil: *Quando <situação>, quero <motivação>, para <resultado esperado>.*

Evite transformar feature em job só trocando a redação. Se dá para resolver o job de três formas totalmente diferentes, é um job; se só existe uma forma, provavelmente é feature.

## Requisito não funcional

Áreas que costumam ser esquecidas e merecem pelo menos uma linha cada: offline e perda de conexão, tamanho e custo de dados, privacidade e o que não é coletado, exclusão de conta e portabilidade, acessibilidade, idioma e fuso, e o que acontece quando um serviço externo cai.

## Sinais de PRD fraco

- Lista de features sem nenhum job.
- Nenhum `[ASSUMIDO]` depois de um brief cheio de pontas soltas.
- Métricas que ninguém sabe de onde sairiam.
- Nenhum caminho de erro descrito.
- Estado vazio e primeira sessão ausentes.
- Requisitos que não apontam para hipótese nenhuma.
