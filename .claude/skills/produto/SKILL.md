---
name: produto
description: Orquestra o fluxo de transformar uma ideia de app em um plano de produto completo, em etapas (brief, contexto, PRD, escopo de MVP, plano técnico). Use sempre que o usuário trouxer uma ideia de app, produto ou feature nova e quiser estruturar, planejar, escrever PRD, definir MVP, priorizar escopo ou montar roadmap — mesmo que ele não cite "produto" ou "PRD" e diga apenas coisas como "tive uma ideia de app", "me ajuda a tirar isso do papel", "o que a gente precisa construir primeiro" ou "quero transformar isso em algo concreto". Use também quando ele pedir para continuar, revisar ou atualizar um produto que já tem pasta em `produtos/`.
---

# Produto: do rascunho ao plano

Esta skill é o ponto de entrada. Ela decide **em que etapa o produto está** e chama a skill certa. Não execute as etapas aqui dentro; delegue.

## O pipeline

Cada etapa lê o arquivo da anterior e escreve o seu. Um produto vive em uma pasta própria:

```
produtos/<slug>/
  00-brief.md       problema, público, hipóteses, riscos       → produto-descoberta
  01-contexto.md    alternativas de hoje, concorrentes          → produto-descoberta (opcional)
  02-prd.md         jobs, requisitos, métricas de sucesso       → produto-prd
  03-mvp.md         corte de escopo e critérios de aceite       → produto-mvp
  04-plano.md       arquitetura, marcos, riscos técnicos        → produto-plano
```

O `<slug>` é curto, em minúsculas, com hífens: `diario-de-treino`, `split-de-conta`.

## Como começar uma sessão

1. Liste `produtos/` (crie a pasta se não existir).
2. Se o usuário citou um produto que já tem pasta, leia **todos** os arquivos dela antes de qualquer coisa. O estado está nos arquivos, não na memória da conversa.
3. Diga em uma frase onde o produto está e qual é o próximo passo. Depois chame a skill da etapa.
4. Se for ideia nova, confirme o slug com o usuário e vá para `produto-descoberta`.

## Regras do fluxo

**Não pule etapas em silêncio.** Se o usuário pedir um PRD e não houver `00-brief.md`, diga que escrever requisitos sem ter fechado o problema produz um documento bonito e inútil, e proponha 10 minutos de descoberta primeiro. Se ele insistir, siga em frente e marque as lacunas com `[ASSUMIDO]`.

**Tudo que for decidido vira arquivo.** Uma conclusão que ficou só no chat está perdida na próxima sessão. Ao final de qualquer etapa, grave o arquivo e mostre o caminho dele.

**Convenções de marcação**, usadas em todos os specs:

- `[ASSUMIDO]` — você inferiu, o usuário não confirmou. Precisa de validação dele.
- `[A CONFIRMAR]` — depende de dado externo, pesquisa ou decisão futura.
- `[HIP-n]` — referência a uma hipótese numerada do brief. Requisitos e features apontam para elas.

**Mudou algo lá atrás?** Se uma conversa invalidar uma hipótese do brief, atualize o `00-brief.md` e avise quais arquivos seguintes ficaram inconsistentes. Não reescreva os posteriores sem perguntar.

## Cabeçalho dos specs

Todo arquivo começa com:

```yaml
---
produto: <nome legível>
slug: <slug>
etapa: 00-brief | 01-contexto | 02-prd | 03-mvp | 04-plano
status: rascunho | em revisão | fechado
atualizado_em: AAAA-MM-DD
---
```

## Etapas sob demanda

O pipeline é a ordem recomendada, não uma prisão. É legítimo pular `01-contexto` quando o usuário já conhece bem o mercado, ou ir direto ao `04-plano` quando o MVP já está decidido fora daqui. O que não é legítimo é escrever uma etapa fingindo que a anterior existe.
