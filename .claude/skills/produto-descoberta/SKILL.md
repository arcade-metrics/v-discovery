---
name: produto-descoberta
description: Conduz a descoberta de uma ideia de app ou feature por meio de entrevista e produz o brief (00-brief.md) com problema, público, hipóteses, premissas e riscos — e, opcionalmente, o contexto competitivo (01-contexto.md). Use sempre que alguém trouxer uma ideia ainda crua, disser "tive uma ideia", "acho que isso resolveria tal problema", "será que vale a pena construir isso", ou quando faltar o 00-brief.md de um produto em `produtos/`. Use também antes de escrever qualquer PRD quando o problema ainda não estiver escrito em lugar nenhum.
---

# Descoberta de produto

Seu trabalho aqui **não** é organizar o que o usuário já sabe. É encontrar o que ele ainda não examinou. A maior parte das ideias de app chega com a solução pronta e o problema por escrever; o brief só presta se inverter isso.

## Como conduzir

**Comece devolvendo a ideia.** Antes de perguntar qualquer coisa, reformule o que entendeu em 3 ou 4 linhas: quem tem o problema, o que acontece hoje, o que o app mudaria. Peça correção. Isso revela mal-entendidos cedo e mostra ao usuário que você está ouvindo.

**No máximo 3 perguntas por rodada.** Entrevista não é formulário. Faça as perguntas, ouça, e deixe a resposta decidir a próxima rodada. Se ele responder algo surpreendente, puxe esse fio em vez de voltar ao roteiro.

**Persiga o incômodo, não o conforto.** As perguntas que importam são as que o usuário ainda não se fez. Se cada resposta confirmar a ideia, você está perguntando errado.

**Aceite "não sei".** Um "não sei" honesto vira `[A CONFIRMAR]` no brief e provavelmente é o item mais valioso do documento. Não force um chute e não trate como falha.

**Não concorde por educação.** Se a ideia tem um furo evidente (o público não paga por isso, a alternativa atual é grátis e boa o bastante, o valor só aparece com rede já formada), diga. Com cuidado, mas diga. O usuário está aqui para descobrir isso agora e não depois de seis meses de código.

Leia `references/perguntas.md` para o banco de perguntas por área. Não use todas: escolha as que atacam a parte mais frágil da ideia.

## O que o brief precisa conter para prestar

- **Problema descrito sem mencionar a solução.** Se você não consegue escrever o problema sem citar o app, provavelmente ainda é uma solução em busca de problema.
- **Público específico.** "Pessoas que treinam" não serve. "Quem treina sozinho em academia e segue uma planilha que alguém montou" serve, porque dá para encontrar cinco dessas pessoas amanhã.
- **O que acontece hoje.** Todo problema real já tem uma solução ruim em uso: planilha, grupo de WhatsApp, caderno, nada. Se não existe comportamento atual, desconfie de que o problema não dói.
- **Hipóteses numeradas e falsificáveis.** `[HIP-1] Quem treina sozinho abandona a planilha em até 3 semanas por falta de registro.` Cada uma precisa de um jeito de estar errada.
- **A hipótese mais frágil, marcada.** Qual é a que, se cair, derruba o produto inteiro? Ela vira a primeira coisa a testar no MVP.
- **Riscos e não-objetivos.** O que este produto deliberadamente não vai resolver.

## Sinais de que o brief ainda está fraco

Revise contra esta lista antes de entregar. Se dois ou mais aparecerem, volte e faça mais uma rodada de perguntas.

- O problema só existe se você assumir que o app existe.
- Todas as hipóteses são confortáveis de confirmar.
- Nenhum `[A CONFIRMAR]` — descoberta honesta sempre deixa pontas soltas.
- O público é um segmento demográfico em vez de um comportamento.
- A seção de riscos lista só riscos técnicos.

## Entrega

Preencha `assets/brief-template.md` e grave em `produtos/<slug>/00-brief.md`.

Depois, ofereça o `01-contexto.md`: alternativas usadas hoje, concorrentes diretos, por que agora, e o diferencial que sobra depois de descontar o que já existe. Se você tiver busca disponível, pesquise; se não, construa a partir do que o usuário conhece e marque o que precisa de verificação. Use `assets/contexto-template.md`.

Encerre dizendo qual hipótese ficou mais frágil e qual é o próximo passo (`produto-prd`).
