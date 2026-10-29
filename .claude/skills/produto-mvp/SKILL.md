---
name: produto-mvp
description: Define o escopo da primeira versão (03-mvp.md) a partir do PRD — linha de corte, o que fica de fora, ordem de construção pelo risco e critérios de aceite por feature. Use quando o usuário perguntar "por onde começo", "o que entra na v1", "qual o MVP disso", pedir priorização de features, corte de escopo ou um primeiro milestone — e sempre que um produto em `produtos/` tiver 02-prd.md e faltar 03-mvp.md.
---

# Escopo do MVP

A pergunta aqui não é "o que dá pra cortar". É **qual é a menor coisa que testa a hipótese mais frágil com usuários de verdade**. Um MVP que entrega tudo um pouco pior não ensina nada; um MVP que entrega um fluxo inteiro muito bem ensina se o produto tem razão de existir.

## Antes de cortar

Leia `00-brief.md` (principalmente a hipótese mais frágil) e `02-prd.md`. Se o PRD não existir, veja a skill `produto`.

## Como decidir o corte

**Comece pela hipótese, não pela lista.** Pergunte: para validar `[HIP-n]`, o que o usuário precisa conseguir fazer de ponta a ponta? Esse fluxo é o MVP. Tudo que não participa dele vai para fora, mesmo que seja fácil de construir — facilidade não é critério de inclusão.

**Um fluxo completo vence três pela metade.** Se o usuário não chega ao momento de valor, ele não gera sinal nenhum, e você fica com um lançamento sem aprendizado.

**Ordene pelo risco, não pela facilidade.** Construa primeiro o que pode provar que a ideia está errada. Se a parte duvidosa é a última do cronograma, você descobre o problema quando já gastou tudo.

**A lista de "fora" é a entrega mais importante do documento.** Ela deve ser visivelmente maior que a de dentro, e cada item precisa de um motivo e de um gatilho de retorno: o que teria que acontecer para isso entrar depois. Sem gatilho, "fora do MVP" vira "esquecido".

**Nomeie o manual aceitável.** Muita coisa pode ser feita a mão no começo: curadoria, cadastro, suporte, cobrança. Diga explicitamente o que será manual e até quando aguenta. Isso tira semanas do cronograma e costuma ensinar mais sobre o produto do que o código.

**Resista ao arredondamento.** Se ao final o MVP contém quase todo o PRD, o corte não aconteceu. Volte e pergunte quais features estão lá por medo de parecer incompleto e não por necessidade de validar.

## Critérios de aceite

Para cada item de dentro, escreva critérios no formato *Dado / Quando / Então*, cobrindo o caminho feliz e pelo menos um caminho de erro. São eles que permitem alguém construir e você verificar sem discussão.

## Como saber se deu certo

Defina antes de construir: que sinal, em quanto tempo, com quantos usuários, nos faz continuar, pivotar ou parar. Escrever o critério de fracasso agora é o que impede a racionalização depois.

## Entrega

Preencha `assets/mvp-template.md` e grave em `produtos/<slug>/03-mvp.md`. Diga ao usuário quanto do PRD ficou de fora (em número de requisitos) — é a melhor medida de que o corte foi real. Próximo passo: `produto-plano`.
