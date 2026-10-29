---
id: iop.ros.comparison
titulo: Comparação entre OneRoster, Ed-Fi, SIF e CEDS
tipo: comparacao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2022oneroster, edfi2026datastandard, a4l2021sifspecs, nces2026ceds, imsglobal2019ltinrps]
relacoes:
  - { tipo: relacionado-a, alvo: iop.ros.oneroster }
  - { tipo: relacionado-a, alvo: iop.ros.ed-fi }
  - { tipo: relacionado-a, alvo: iop.ros.sif }
  - { tipo: relacionado-a, alvo: iop.ros.ceds }
  - { tipo: complementa, alvo: iop.fund.dados-vs-protocolo }
termos: [rostering, modelo de dados escolar, vocabulário, jurisdição]
---

# Comparação: OneRoster, Ed-Fi, SIF e CEDS

## Definição e terminologia

Os quatro são citados juntos como "padrões de dados escolares", mas ocupam posições diferentes: OneRoster é um padrão de intercâmbio de escopo estreito; Ed-Fi é um modelo amplo com API normativa; SIF é uma infraestrutura com modelos por jurisdição; CEDS é um dicionário de elementos sem transporte [I].

## Alternativas e comparações

| Dimensão | OneRoster 1.2 | Ed-Fi | SIF | CEDS |
|---|---|---|---|---|
| Mantenedor | 1EdTech [F: imsglobal2022oneroster] | Ed-Fi Alliance [F: edfi2026datastandard] | Access 4 Learning [F: a4l2021sifspecs] | NCES [F: nces2026ceds] |
| Define vocabulário | sim | sim (alinhado a CEDS) [F: edfi2026datastandard] | sim, por localidade [F: a4l2021sifspecs] | sim, é o seu objeto [F: nces2026ceds] |
| Define API | sim (REST) [F: imsglobal2022oneroster] | sim (API Guidelines normativas) [F: edfi2026datastandard] | sim (Open API por localidade) [F: a4l2021sifspecs] | não |
| Troca em arquivo | sim (CSV) [F: imsglobal2022oneroster] | não documentado | não verificado | n/a |
| Escopo | turmas, pessoas, matrículas, notas, recursos [F: imsglobal2022oneroster] | domínios escolares amplos [F: edfi2026datastandard] | amplo, por jurisdição | dicionário de elementos |
| Jurisdição | internacional | EUA (extensível) | multi-localidade explícita [F: a4l2021sifspecs] | EUA |
| Certificação de terceiro | sim (guia de conformidade) [F: imsglobal2022oneroster] | conformidade por API Guidelines [F: edfi2026datastandard] | não verificada | adesão voluntária [F: nces2026ceds] |
| Custo de adoção | baixo a médio | alto | médio a alto | baixo (é mapeamento) |

Células sem citação são interpretação do autor [I].

## Fundamentos e funcionamento

**Regra de decisão** [I]:

1. Se a necessidade é "saber quem está em qual turma, para aplicações de sala de aula", OneRoster resolve, inclusive por CSV quando não há API na origem.
2. Se a necessidade é "reunir dados escolares amplos para análise e política", Ed-Fi é o modelo mais completo entre os consultados, ao custo de equipe de dados.
3. Se há uma jurisdição com modelo SIF publicado e sistemas já integrados por ele, SIF é o caminho de menor atrito local.
4. CEDS não é escolha alternativa às outras três: é a camada de significado que se usa *junto* com qualquer uma delas.

**Nota sobre o Brasil** [I]: nenhum dos quatro tem modelo brasileiro publicado. Os três primeiros exigiriam extensão ou mapeamento com o vocabulário do Censo Escolar (ver `iop.br.educacenso`); o CEDS serviria apenas como referência de método, não de conteúdo.

**Nota sobre LTI NRPS** [I]: NRPS não compete com nenhum dos quatro. Resolve a consulta pontual de membros no contexto de um lançamento, somente leitura [F: imsglobal2019ltinrps], e não serve de fonte institucional.

## Métricas e métodos de avaliação

Para escolher num caso concreto [I]: número de domínios de dados realmente necessários; existência de API no sistema de origem; capacidade da equipe de manter mapeamentos; exigência de certificação em edital.

## Relações com outros conceitos

Agrega os quatro documentos da área e complementa `iop.fund.dados-vs-protocolo`, que dá o critério de classificação usado na tabela.

## Lacunas e questões abertas

- Versões correntes de SIF e CEDS não confirmadas (ver os documentos respectivos); a tabela evita números por isso.
- Não há dados de adoção comparáveis entre os quatro.
- Falta avaliar o esforço real de um mapeamento Censo Escolar ↔ Ed-Fi ou ↔ OneRoster.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2022oneroster | normativo | 2026-10-29 |
| edfi2026datastandard | fornecedor | 2026-10-29 |
| a4l2021sifspecs | fornecedor | 2026-10-29 |
| nces2026ceds | fornecedor | 2026-10-29 |
| imsglobal2019ltinrps | normativo | 2026-10-29 |
