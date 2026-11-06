---
produto: VUOO
slug: vuoo-conversa-curricular
etapa: brief-ecossistema
status: rascunho
atualizado_em: 2026-11-05
---

# Brief: VUOO (ecossistema)

> **Movido em 06/11/2026** de `produtos/vuoo/00-brief.md`, apagado. Guarda o desenho do ecossistema (componentes A, B e C) e as hipóteses HIP-3 a HIP-6, usadas por esta pasta. A parte dos microjogos foi incorporada em `../vuoo-microjogos/00-brief.md`, que prevalece para eles.

## Em uma frase

O VUOO é um ecossistema para escolas e redes do ensino fundamental e médio. Ele tem três componentes: **microjogos** no celular de todos os alunos da turma, já adaptados à educação especial; **conversa com IA sobre BNCC e inclusão**, a partir de uma base oficial curada; e **conversa com IA sobre a própria escola e cada aluno**, a partir dos dados dos microjogos.

## Os três componentes

| | Componente | Para quem | O que faz | Status de desenvolvimento |
|---|---|---|---|---|
| **C** | **Microjogos** | Aluno | Micro-atividades de 5 a 15 min por dia, no celular e offline. Começam funcionais e ficam ancoradas na BNCC. Adaptam-se ao comportamento do aluno (DUA). | **Núcleo do desenvolvimento.** É onde vai a maior parte do esforço. |
| **A** | **Conversa curricular** | Professor, AEE, coordenação | Ambiente conversacional e MCP sobre BNCC e inclusão. Usa a base curada de fontes do governo federal e dos estados. | **Pipeline paralelo**, que começa quando a estrutura do Core estiver pronta. |
| **B** | **Conversa da escola** | Gestor, professor | Ambiente conversacional e MCP sobre a escola: performance, uso, atividades e cada aluno individualmente. | **Só mockup na v1**, isolado, para as pessoas entenderem a proposta. |

Regras do ecossistema:

- **A** e **B** aceitam o LLM que o cliente conectar. O VUOO entrega a base, o MCP e os testes de alucinação.
- **C** alimenta **B**. Sem uso do C, o B não tem dados.
- **A** e **B** se conectam por filtros diferentes. Até onde vai essa conexão é `[A CONFIRMAR]`.
- Tudo é separado em camadas depois, quando o Core estiver pronto.

## O problema

Uma turma regular tem alunos com perfis muito diferentes, entre eles alunos da educação especial. O professor precisa:

- fazer **cada aluno** avançar no currículo;
- adaptar atividades e montar o PEI, que agora é exigido pela Portaria MEC 421/2026 e, em SP, pela Res. SEDUC-SP 129/2025;
- saber **o que está acontecendo com cada aluno**.

Hoje ele não tem tempo, material adaptado nem informação organizada para fazer isso. Cada parte da dor é atacada por um componente:

| Dor | Componente |
|---|---|
| "Não sei como adaptar a BNCC e montar o PEI para este aluno." | A |
| "Não tenho atividade que engaje a turma toda, inclusive os alunos com deficiência." | C |
| "Não sei o que está acontecendo com cada aluno." | B |

## Quem tem o problema

- **Quem paga:** a escola ou a rede de ensino (D9).
- **Quem usa o C:** todos os alunos da turma, do EF ao EM, com a adaptação à educação especial já embutida (premissa do DUA). Também o aluno avulso, que usa sem escola (D9, D18).
- **Quem usa o A e o B:** professor regente, professor do AEE, coordenação e gestão.

**Exemplo concreto** `[ASSUMIDO]`: uma professora de 4º ano numa escola municipal, com 30 alunos. Dois têm TEA e um tem deficiência intelectual. Ela precisa entregar o PEI desses três e não sabe por onde começar na BNCC. Sem nenhum instrumento, também não sabe dizer se eles avançaram no bimestre.

**Quem parece público e não é:**
- **Escola que quer um produto só para educação especial.** O VUOO é universal: a turma inteira usa o mesmo app.
- **Clínica ou terapeuta.** O VUOO não faz diagnóstico nem guarda laudo como documento (D4).

## O que acontece hoje

`[A CONFIRMAR]` O que escolas e professores usam hoje para:
- montar o PEI;
- adaptar atividades;
- acompanhar o aluno.

A suposição `[ASSUMIDO]` é que usam documentos em Word, planilhas, pesquisa solta na internet, materiais impressos e ChatGPT genérico, sem base confiável. Ainda não foi verificado com escolas.

## Hipóteses

| # | Hipótese | Como saberíamos que é falsa | Confiança |
|---|----------|------------------------------|-----------|
| HIP-1 | **(C) Os alunos voltam aos microjogos por conta própria, de 5 a 15 min por dia, sem o professor cobrar.** | Menos da metade dos alunos de uma turma piloto usa 3 ou mais dias por semana depois da 3ª semana. `[A CONFIRMAR]` o limiar. | baixa |
| HIP-2 | (C) A mesma atividade, com adaptação automática, serve tanto para o aluno da educação especial quanto para o resto da turma. Ninguém precisa de uma "versão separada". | Professores pedem atividades diferentes para os alunos da educação especial, ou esses alunos não conseguem concluir as atividades. | média |
| HIP-3 | (A) O professor prefere perguntar sobre BNCC e inclusão a uma base curada a perguntar ao ChatGPT ou buscar no Google. | O professor volta menos de uma vez por semana, ou não percebe diferença de qualidade. | média |
| HIP-4 | (A) Os testes de alucinação mostram que a base curada responde com menos erro que um LLM sem base. | No conjunto de testes, a taxa de erro com e sem base é parecida. | média |
| HIP-5 | (B) O gestor entende o valor do B só pelo mockup, sem dados reais. | No mockup, gestores não conseguem dizer que pergunta fariam ou para que usariam. | média |
| HIP-6 | (Ecossistema) A escola paga pelo conjunto porque os três componentes juntos valem mais que separados. | A escola quer comprar só o A, ou só o C, e o preço do conjunto não se sustenta. | baixa |

**Hipótese mais frágil:** HIP-1 `[ASSUMIDO]`. Se o aluno não usa o C:
- o B fica sem dados;
- a adaptação ao aluno não tem com o que trabalhar;
- sobra só o A, que é outro produto, menor.

Por isso ela é a primeira coisa que o MVP testa.

## Proposta de valor

- **Professor:** "Pergunto sobre o meu aluno, a BNCC e a inclusão, e recebo uma resposta confiável, com fonte, em minutos."
- **Aluno:** "É um jogo curto que eu consigo fazer e que é do meu jeito."
- **Gestor:** "Vejo e converso sobre o que acontece em cada turma e com cada aluno, sem pedir relatório a ninguém."

## Não-objetivos

- **Não é produto só de educação especial.** É universal, por DUA.
- **Não faz diagnóstico e não guarda laudo como documento.** Laudo é um campo, com referência externa (D4).
- **Não fornece o LLM.** O cliente conecta o dele; o VUOO entrega a base, o MCP e os testes.
- **Não usa visão computacional** (D13).
- **Não tem base de pesquisa** (D14).
- **Não depende do projeto CIATec** (D8).
- **Não é implementado fora do Brasil agora.** Outras jurisdições ficam em standby (D20).

## Riscos

| Risco | Tipo | Impacto | O que reduziria |
|-------|------|---------|-----------------|
| O aluno não volta aos microjogos (HIP-1) | usuário | alto | Turma piloto cedo, medindo retorno semanal antes de produzir muito conteúdo |
| A Lei 15.100/2025 restringe o celular do aluno na escola | legal | alto | Encaixar o uso na exceção pedagógica e de acessibilidade, ou desenhar o uso para casa `[A CONFIRMAR]` |
| Conversar sobre um aluno específico expõe dado sensível de menor (deficiência) a um LLM de terceiros | legal | alto | Estratégia de anonimizar antes do LLM e reidentificar dentro do VUOO. **Fica na teoria por enquanto** `[A CONFIRMAR]` |
| Custo de produzir microjogos para EF+EM inteiro | negócio | alto | V1 com recorte funcional pequeno, ligado à BNCC pela base do A |
| Três componentes dividem a equipe e nenhum fica bom | negócio | médio | C como núcleo; A em pipeline paralelo só depois do Core; B só mockup |
| O app falha em aparelhos baratos ou com pouco armazenamento | técnico | médio | Trilha semanal leve (D12); ajustar ao longo do desenvolvimento |
| A escola não vê valor para pagar (HIP-6) | mercado | alto | Validar preço e disposição com 3 a 5 escolas antes do lançamento |

## Pontas soltas

- `[A CONFIRMAR]` O que escolas e professores usam hoje para montar o PEI e acompanhar o aluno.
- `[A CONFIRMAR]` Até onde o A se conecta com o B, e com que filtros.
- `[A CONFIRMAR]` A estratégia de anonimização para conversar sobre um aluno com LLM externo. Discussão teórica, fora da v1.
- `[A CONFIRMAR]` Se o uso do C é em sala, em casa ou nos dois, diante da Lei 15.100/2025.
- `[A CONFIRMAR]` O limiar de engajamento que confirma ou derruba a HIP-1.
- `[A CONFIRMAR]` Quais habilidades funcionais entram primeiro e como se ligam à BNCC.
- `[ASSUMIDO]` HIP-1 (engajamento do aluno) é a hipótese mais frágil.
- `[ASSUMIDO]` O exemplo concreto da professora de 4º ano.
- **Fora do brief:** os testes de alucinação são entregável de uma equipe dedicada. Entram no cronograma só quando o resto estiver pronto.
