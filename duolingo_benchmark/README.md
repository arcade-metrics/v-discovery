# Benchmark Duolingo

Análise do Duolingo como referência para o desenho de uma **plataforma de jogos sérios para educação especial**. Cobre o sistema de recompensas, o gameplay e o estilo (visual, personagens, movimento, som, tom de voz), com números, evidência e uma leitura de risco por perfil de aluno.

Escrito primeiro para ser lido por modelos de linguagem (estrutura fixa, campos nomeados, marcas de confiança em cada afirmação, índice em JSON) e, em segundo lugar, por pessoas. Português do Brasil.

## Como usar

| Quer… | Leia |
|---|---|
| Entender em 10 minutos por que o Duolingo funciona e o que vale copiar | `00-visao-geral.md` |
| Detalhar uma mecânica de recompensa (XP, ofensiva, liga, baú, missão, notificação…) | `01-recompensas.md` |
| Detalhar o loop da lição, os tipos de exercício, o caminho, a adaptação, o feedback | `02-gameplay.md` |
| Paleta, tipografia, linguagem de forma, personagens, animação, som, copy | `03-estilo.md` |
| Saber o que é fato, o que é dado da empresa e o que é crítica documentada | `04-evidencias-e-criticas.md` |
| Avaliar o risco de cada mecânica para alunos da educação especial | `05-riscos-educacao-especial.md` |
| Ver um exemplo de tradução já feita para um produto específico | `apendice-caso-vuoo.md` |
| Achar uma captura de tela ou diagrama | `imagens/MANIFESTO.md` (tabela por capítulo) ou `imagens.json` |
| Consultar o índice de mecânicas legível por máquina | `benchmark.json` |
| Ler a pesquisa bruta de onde tudo saiu | `pesquisa/` |

## Convenções

- **Marcas de confiança**, em toda afirmação: **[V]** verificado em fonte primária (Duolingo, artigo acadêmico, documento regulatório) · **[S]** fonte secundária (imprensa, análises, guias, wiki) · **[I]** inferência ou observação não verificada.
- **Números do Duolingo** são, quase sempre, variações relativas de testes A/B ("+3,3% de retenção D14" = 3,3% a mais que o controle), medidas com adolescentes e adultos, e medem retenção ou engajamento, não aprendizagem. Nenhum foi medido com crianças nem com alunos da educação especial.
- **Datas**: o produto muda o tempo todo. Cada afirmação datada vale para a data; o estado de referência é outubro de 2026.
- **Cada mecânica** segue o mesmo esquema de campos: *o que é · como funciona · por que funciona · números · evidência externa · críticas · risco na educação especial · adaptações possíveis · imagens*. Isso permite comparar mecânicas entre si.
- **Imagens**: nomeadas `<capítulo>-<tema>-<detalhe>.<ext>`, por exemplo `01-recompensas-ofensiva-marco-fenix-animacao.gif`. O capítulo diz onde a imagem é citada.

## Estrutura

```
duolingo_benchmark/
  README.md                          este arquivo
  00-visao-geral.md                  tese, loop central, glossário, matriz de decisão
  01-recompensas.md                  XP, ofensiva, missões, gemas/baús/energia, ligas, conquistas, social, notificações, monetização
  02-gameplay.md                     lição, catálogo de exercícios, caminho, adaptação, feedback, produtos infantis, escolas, acessibilidade
  03-estilo.md                       paleta, tipografia, forma, personagens, movimento, som, tom de voz, telas
  04-evidencias-e-criticas.md        números, estudos, críticas, com força da evidência
  05-riscos-educacao-especial.md     lente por perfil: TEA, TDAH, dislexia, DCD, DI, deficiência visual, auditiva, motora
  apendice-caso-vuoo.md              estudo de caso: tradução feita para o VUOO (crianças de 6 a 11, rede pública de SP)
  benchmark.json                     índice de mecânicas, campos, veredito e imagens
  imagens.json                       índice das imagens (arquivo, descrição, fonte, tipo)
  imagens/                           359 capturas, diagramas e ilustrações + MANIFESTO.md
  pesquisa/                          relatórios brutos: teardown original (27/10/2026) e três pesquisas de aprofundamento (29/10/2026)
```

## Origem

- `pesquisa/2026-10-27-teardown-original-vuoo.md`: teardown feito para o projeto VUOO, com a lente de crianças neurodivergentes de 6 a 11 anos. É a base dos capítulos 00 a 04; o texto dos capítulos foi reescrito para não depender daquele produto.
- `pesquisa/2026-10-29-recompensas.md`, `-gameplay.md`, `-estilo.md`: pesquisas web de aprofundamento, cada uma com seção "Lacunas" listando o que não foi possível confirmar.
- As imagens vêm das páginas citadas nessas pesquisas (blog e site de design do Duolingo, Rive, App Store, Deconstructor of Fun, Lenny's Newsletter, Mobbin, screensdesign, Fonts In Use e outras). Foram baixadas em 29/10/2026.

## Limites conhecidos

1. Não há teste de mão documentado do **Duolingo ABC** (feedback de erro, som, timer) nem de **Duolingo for Schools** atual. Ver as seções "Lacunas" em `pesquisa/`.
2. Não há documentação oficial de **sound design** nem de **durações de animação**.
3. Valores de **XP e preços em gemas** variam por teste A/B, país e plataforma; são exemplos, não tabela oficial.
4. O site `design.duolingo.com` redireciona para o blog desde 2025; paleta e tipografia completas vieram de extrações de terceiros.
