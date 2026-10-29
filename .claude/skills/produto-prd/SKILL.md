---
name: produto-prd
description: Escreve o PRD (02-prd.md) de um produto a partir do brief e do contexto — jobs to be done, fluxos principais, requisitos funcionais e não funcionais rastreáveis às hipóteses, e métricas de sucesso. Use quando o usuário pedir um PRD, documento de requisitos, especificação de produto, "o que o app precisa fazer", "escreve a spec disso", ou quando um produto em `produtos/` já tem 00-brief.md e falta o 02-prd.md. Use também para revisar ou atualizar um PRD existente.
---

# PRD

Um PRD serve para que uma pessoa que não participou da conversa consiga construir a coisa certa e discordar com precisão. Se o documento só faz sentido para quem estava na sala, ele falhou.

## Antes de escrever

Leia `produtos/<slug>/00-brief.md` e, se existir, `01-contexto.md`. Se o brief não existir, pare e diga por quê (ver a skill `produto`).

Releia as hipóteses. Cada requisito que você escrever precisa existir por causa de uma delas; os que não se encaixarem em nenhuma são candidatos a serem cortados agora, antes de custarem código.

## Como escrever bem cada parte

**Jobs, não features.** "Registrar a carga levantada" é feature. "Saber se estou progredindo sem ter que lembrar do que fiz semana passada" é o job. Escreva os jobs primeiro; as features saem deles e ficam mais fáceis de cortar depois.

**Fluxos antes de requisitos.** Descreva em passos o caminho principal, do primeiro contato até o momento de valor. A maior parte dos requisitos esquecidos aparece quando você percorre o fluxo: onde entram os dados, o que acontece na primeira vez, o que acontece quando dá errado.

**Requisitos testáveis.** Um requisito bom tem um estado observável. "O app deve ser rápido" não é verificável; "a lista abre com dados em cache em até 1s, mesmo offline" é. Prefira a forma "quando <situação>, o sistema <comportamento observável>".

**Rastreabilidade.** Todo requisito carrega a hipótese que o justifica: `RF-04 … [HIP-2]`. Quando uma hipótese cair, você sabe exatamente o que revisar.

**Primeira sessão e estados vazios.** Todo app é lindo com dados de demonstração e desconcertante no dia zero. Especifique o estado vazio, o onboarding mínimo e o que o usuário precisa fazer antes de ver valor. Esse custo de entrada é o que mata a maioria dos apps.

**Métricas acionáveis.** Uma métrica presta se uma mudança no produto consegue mexer nela e se ela diz algo sobre o valor entregue. "Downloads" raramente presta. "% de usuários que registram um segundo treino dentro de 7 dias" presta, porque testa a hipótese de hábito. Defina também o contra-indicador: o número que, se subir, significa que você otimizou a coisa errada.

**Marque o que você inventou.** Onde o brief for omisso e você preencher por inferência, use `[ASSUMIDO]` e junte tudo numa lista no fim. O usuário revisa essa lista em dois minutos; um PRD com invenções camufladas custa semanas.

Para as rubricas de qualidade (o que torna um requisito, uma métrica ou um critério bem escrito), leia `references/qualidade.md`.

## Escopo deste documento

O PRD descreve **o produto desejado**, não o que cabe na primeira versão. Não corte escopo aqui — isso é trabalho da skill `produto-mvp`, e misturar os dois faz você perder a visão de para onde o produto vai. Se algo for claramente de longo prazo, coloque na seção "Além da v1".

## Entrega

Preencha `assets/prd-template.md` e grave em `produtos/<slug>/02-prd.md`. Mostre ao usuário a lista de `[ASSUMIDO]` e pergunte sobre eles antes de considerar o documento fechado. Próximo passo: `produto-mvp`.
