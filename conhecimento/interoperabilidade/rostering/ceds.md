---
id: iop.ros.ceds
titulo: CEDS (Common Education Data Standards)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nces2026ceds, edfi2026datastandard]
relacoes:
  - { tipo: complementa, alvo: iop.ros.ed-fi }
  - { tipo: complementa, alvo: iop.sem.interoperabilidade-semantica }
  - { tipo: relacionado-a, alvo: iop.ros.comparison }
termos: [vocabulário comum, elemento de dado, P-20W, definição de elemento]
---

# CEDS (Common Education Data Standards)

## Definição e terminologia

CEDS é "a specified set of the most commonly used education data elements", um vocabulário comum que apoia a troca de dados entre estados, entre setores e níveis de ensino, e a prestação de contas federal nos Estados Unidos; serve para tornar os dados educacionais mais consistentes e comparáveis [F: nces2026ceds].

É desenvolvido pelo NCES com um CEDS Stakeholder Group, que reúne representantes de estados, distritos, instituições de ensino superior, agências estaduais de educação superior, organizações de educação infantil, escritórios de programas federais, organizações de padrões de interoperabilidade e associações e entidades sem fins lucrativos [F: nces2026ceds]. A adesão é voluntária [F: nces2026ceds].

## Problema que resolve

Padrões de intercâmbio resolvem o transporte; sobra a pergunta de o que cada campo significa. CEDS é um dicionário de elementos: não define API nem formato, define o significado dos dados [I]. É, nos termos de `iop.fund.dados-vs-protocolo`, um padrão de modelo de dados e vocabulário, sem binding nem protocolo.

## Fundamentos e funcionamento

O Ed-Fi Data Standard se declara alinhado ao CEDS [F: edfi2026datastandard], o que coloca o CEDS na camada semântica abaixo de padrões de intercâmbio — vários padrões podem apontar para as mesmas definições de elemento [I].

## Requisitos e pressupostos

- O uso efetivo exige mapear os campos dos sistemas locais para os elementos CEDS, trabalho de domínio, não de engenharia [I].
- Como a adesão é voluntária [F: nces2026ceds], o alinhamento é declarado pelo adotante e não certificado por terceiro — ao contrário do que ocorre com padrões 1EdTech (ver `iop.fund.conformidade-e-certificacao`) [I].

## Vantagens e limitações

Vantagens [I]: resolve a camada semântica sem obrigar a trocar de padrão de transporte; ancorado em uma instituição estatística nacional, o que dá estabilidade às definições.

Limitações [I]:
- Vocabulário construído para o sistema educacional dos Estados Unidos; a transposição para o Brasil exige mapeamento com o vocabulário do Censo Escolar (ver `iop.br.educacenso`), não adoção direta.
- Sem API nem formato: não substitui OneRoster, Ed-Fi ou SIF, apenas os complementa.

## Alternativas e comparações

| Papel | CEDS | Ed-Fi | OneRoster |
|---|---|---|---|
| Define significado dos elementos | sim | parcial (alinhado a CEDS) | parcial |
| Define modelo de troca | não | sim | sim |
| Define API | não | sim | sim |
| Cobertura | P-20W (segundo literatura secundária, não verificada) | escolar | rostering |

## Relações com outros conceitos

Complementa `iop.ros.ed-fi` (que se declara alinhado a ele) e `iop.sem.interoperabilidade-semantica`.

## Lacunas e questões abertas

- Versão corrente e data de lançamento não confirmadas: resultados de busca mencionam CEDS 7 e 7.1, e a página do NCES consultada não traz versão. Verificar em `ceds.ed.gov`.
- Componentes do CEDS (Data Model, Elements, Align, Connect, IDS) não descritos na página consultada.
- Escopo P-20W (da educação infantil ao mercado de trabalho) não confirmado em fonte primária.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nces2026ceds | fornecedor | 2026-10-29 |
| edfi2026datastandard | fornecedor | 2026-10-29 |
