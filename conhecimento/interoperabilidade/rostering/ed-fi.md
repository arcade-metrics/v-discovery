---
id: iop.ros.ed-fi
titulo: Ed-Fi Data Standard
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [edfi2026datastandard, nces2026ceds]
relacoes:
  - { tipo: alternativa-a, alvo: iop.ros.oneroster }
  - { tipo: alternativa-a, alvo: iop.ros.sif }
  - { tipo: depende-de, alvo: iop.ros.ceds }
  - { tipo: relacionado-a, alvo: iop.ros.comparison }
termos: [Unifying Data Model, domínio, extensão, API Guidelines, ODS/API, normativo]
---

# Ed-Fi Data Standard

## Definição e terminologia

O Ed-Fi Data Standard é uma especificação aberta, alinhada ao CEDS, que descreve o significado e a estrutura de dados educacionais. A documentação é explícita em dizer que o padrão "não é software", nem banco de dados, nem ferramenta de relatório [F: edfi2026datastandard].

**Versões e suporte** [F: edfi2026datastandard]:

| Linha | Lançamento | Observação |
|---|---|---|
| 6.x | 6.0 em 2025 | anos letivos cobertos em página própria de versões suportadas |
| 5.x | 5.0 em 2023; 5.1 e 5.2 em 2024 | destinada aos anos letivos de 2024-2025 a 2027-2028 |
| 4.0 | 2022 | para 2024-2025 e 2025-2026; sem minor release planejada |
| 3.x | 3.0 em 2018, até 3.3.1 em 2022 | 2024-2025 é o último ano de suporte de 3.3.1 |

## Problema que resolve

Secretarias e distritos precisam reunir dados de muitos sistemas (matrícula, frequência, avaliação, programas) num modelo único, para análise e prestação de contas. O Ed-Fi padroniza esse modelo e o contrato de API, em vez de padronizar apenas um recorte como o rostering [I].

## Fundamentos e funcionamento

**Unifying Data Model (UDM).** É o modelo lógico por trás do padrão. É explicitamente **não normativo**, e serve para manter as especificações consistentes entre si; as páginas de Best Practices, essas sim, são normativas [F: edfi2026datastandard].

**Domínios.** A versão 6 organiza os dados em domínios: matrícula, identificação de aluno, frequência, avaliação e registros acadêmicos, ensino e aprendizagem, programas, disciplina, saúde do estudante (apenas imunizações), pessoal e finanças/levantamentos. Educação especial está em acesso antecipado na 6.1 [F: edfi2026datastandard].

**Orientação a aluno.** O padrão é *student-centric*: agregados como taxa de frequência são excluídos e devem ser calculados a partir de dados em nível de aluno [F: edfi2026datastandard]. Essa decisão é o que torna o modelo reutilizável para análise, e também o que o torna pesado para quem só precisa de indicadores [I].

**Extensões.** Dados específicos de um estado ou distrito entram por extensões, regidas por diretrizes não normativas (Extension Framework Guidelines) [F: edfi2026datastandard].

**Relação com a API.** O ODS/API e a Ed-Fi API v8 são produtos da Alliance que implementam o padrão; qualquer um pode construir uma API compatível seguindo as API Guidelines, que são normativas [F: edfi2026datastandard].

**Alinhamento ao CEDS.** O padrão se declara alinhado ao CEDS [F: edfi2026datastandard], que é o vocabulário comum mantido pelo NCES [F: nces2026ceds] (ver `iop.ros.ceds`).

## Requisitos e pressupostos

- A instituição tem capacidade de operar uma API e de manter mapeamentos entre seus sistemas-fonte e o modelo.
- Há governança para decidir extensões; extensões não coordenadas reconstroem o problema que o padrão resolve [I].

## Vantagens e limitações

Vantagens [I]: cobertura ampla de domínios escolares; separação explícita entre o que é normativo e o que é orientação, o que facilita auditoria de conformidade (ver `iop.fund.conformidade-e-certificacao`); alinhamento declarado ao CEDS, o que dá semântica comum.

Limitações [I]:
- Custo de adoção alto comparado ao OneRoster; exige equipe de dados.
- Fortemente ancorado no contexto dos Estados Unidos (domínios como *discipline* e *finance* refletem a prestação de contas norte-americana); o uso fora desse contexto exige extensões e traduções.
- Ciclo de versões com quebras: a 5.0 introduziu mudanças incompatíveis em vários modelos [F: edfi2026datastandard] [I].

## Alternativas e comparações

Ver `iop.ros.comparison`.

## Métricas e métodos de avaliação

Conformidade pelas API Guidelines normativas [F: edfi2026datastandard]. Em operação: proporção de campos preenchidos por domínio, e proporção de dados que só cabem em extensão [I].

## Relações com outros conceitos

Alternativa a `iop.ros.oneroster` (escopo maior) e a `iop.ros.sif`. Depende semanticamente de `iop.ros.ceds`.

## Lacunas e questões abertas

- A relação exata entre Data Standard e descriptors (vocabulários controlados do Ed-Fi) não foi coberta pela página consultada.
- Licenciamento e modelo de governança da Ed-Fi Alliance: não verificados.
- Aplicabilidade ao contexto brasileiro frente ao Educacenso: não avaliada (ver `iop.br.educacenso`).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| edfi2026datastandard | fornecedor | 2026-10-29 |
| nces2026ceds | fornecedor | 2026-10-29 |
