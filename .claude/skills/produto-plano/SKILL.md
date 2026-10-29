---
name: produto-plano
description: Escreve o plano de execução (04-plano.md) do MVP — arquitetura em alto nível, modelo de dados, integrações, marcos, riscos técnicos e decisões em aberto. Use quando o usuário perguntar "como a gente constrói isso", pedir arquitetura, stack, modelo de dados, cronograma, roadmap ou plano de entrega de um app — e sempre que um produto em `produtos/` tiver 03-mvp.md e faltar 04-plano.md.
---

# Plano de execução

Este documento é a ponte entre o escopo e o primeiro commit. Ele precisa ser suficiente para começar a construir e honesto sobre o que ainda não está decidido.

## Antes de escrever

Leia `02-prd.md` (requisitos não funcionais, principalmente) e `03-mvp.md`. O plano cobre **apenas o escopo do MVP**; arquitetura pensada para o produto maduro no primeiro mês é a forma mais cara de errar.

## Como escrever bem cada parte

**Escolha a stack por restrição, não por preferência.** Pergunte e registre: experiência da equipe, prazo, orçamento, necessidade de offline, exigência de loja de apps, requisitos de dados sensíveis. Para cada decisão relevante, escreva a alternativa descartada e o motivo — é isso que evita refazer a discussão em três meses. Se o usuário não tem preferência, recomende uma opção e explique o trade-off em uma linha, sem transformar o documento em comparativo de frameworks.

**Modele os dados a partir dos fluxos.** Liste as entidades, os campos que realmente existem no MVP e as relações. Marque o que é dado pessoal ou sensível, porque isso muda armazenamento, retenção e o que você precisa oferecer de exclusão.

**Trate integrações como risco.** Para cada serviço externo: para que serve, custo, limite de uso, o que acontece se cair, e qual é o plano B. Integração costuma ser onde o cronograma estoura.

**Marcos por capacidade, não por camada.** "Fluxo de registro funcionando ponta a ponta" é marco; "backend pronto" não é, porque não dá para demonstrar nem testar com usuário. Ordene os marcos na mesma ordem de risco definida no MVP.

**Estimativas com faixa e premissa.** Dê intervalos ("2 a 3 semanas, assumindo uma pessoa em tempo integral") em vez de números secos, e nomeie a premissa junto. Se não houver base para estimar, diga isso em vez de inventar.

**Registre o que não foi decidido.** Uma lista de decisões em aberto, cada uma com o que ela bloqueia e quando precisa estar resolvida, vale mais do que uma decisão prematura escrita com confiança falsa.

## Entrega

Preencha `assets/plano-template.md` e grave em `produtos/<slug>/04-plano.md`.

Com o plano fechado, o ciclo natural é construir o primeiro marco e voltar ao `00-brief.md` para registrar o que o uso real ensinou sobre as hipóteses. Lembre o usuário disso: o brief é um documento vivo, não um registro histórico.
