# Brasil: adaptador ativo

**Estado:** ativo. É o primeiro adaptador a ser implementado sobre o Core agnóstico ([../core/](../camada-agnostica/core-v0.1.md)). Pesquisa de 2026-11-05 em duas frentes (organização e dados; currículo, avaliação e inclusão), somada às transcrições de fonte feitas antes. Formato e regras em [../_convencoes.md](../_convencoes.md).

## Resumo em 10 linhas

1. **Identidade do estudante:** a LC 220/2025 (art. 26 I) e a Portaria MEC 269/2026 (art. 7º) tornam o **CPF** o identificador nacional (Inue). Convivem com ele o ID INEP de 12 dígitos e o `ID_SGP_*` do MEC. O Core guarda uma lista de identificadores com `scheme`.
2. **Censo e CMDEB não usam o mesmo formato.** Uma matrícula no Censo é aluno × turma; no CMDEB é aluno × escola × etapa × ano, com enturmação à parte. Os códigos também divergem para o mesmo conceito (cor/raça, tipo de turma, AEE…), e não há tabela oficial que os relacione.
3. Os códigos INEP de turma e matrícula **só existem depois da exportação** e mudam todo ano. As chaves estáveis precisam ser nossas.
4. O leiaute do Censo **muda de estrutura todo ano**, então o adaptador precisa de um serializador por ano de censo.
5. A situação do aluno tem **8 códigos anuais** no Censo e **17 códigos por evento** no CMDEB.
6. **Código curricular não é identidade.** A forma impressa pode diferir do código (`EF05CO011`, impresso com três dígitos na BNCC Computação) e o Currículo Paulista reaproveita e desdobra códigos. A BNCC vem do vuoo-base v1.1, com id próprio por item (`bncc-2018/<CODIGO>`, `bncc-computacao-2022/<CODIGO>`) e o código como atributo.
7. **Três relógios no currículo** (vigência do ato, edição do texto, versão do dado) mais a **coorte**: a DCNEM 2024 faz o Ensino Médio de 2018 e o de 2024 conviverem.
8. **Avaliação:** o valor na escala é um dado; os cortes (níveis do Saeb, SARESP, os 743 pontos do CNCA) são classificações versionadas por cima dele.
9. **Inclusão:** necessidade de apoio, elegibilidade administrativa e diagnóstico ficam separados. A Portaria MEC 421/2026 fixa o conteúdo mínimo de PAEE e PEI e proíbe exigir laudo. A Res. SEDUC-SP 129/2025 traz formulários próprios e entra em conflito em alguns pontos.
10. **Dados:** a base legal é registrada por operação e a sensibilidade por campo. Barreiras e acomodações devem ser tratadas como dado sensível. A LGPD não exige que os dados fiquem no Brasil; a hospedagem no Brasil é decisão do projeto.

## Índice

### Transcrições de fonte

A BNCC (versão final) e a BNCC Computação não são transcritas aqui: a fonte única é o repositório **vuoo-base**, release v1.1 (https://github.com/arcade-metrics/v-base), em `dados/bncc-2018.json` e `dados/bncc-computacao-2022.json`.

| Pasta | Conteúdo |
|---|---|
| [cmdeb/](cmdeb/README.md) | CMDEB, Anexo da Portaria MEC 832/2025 |
| [bncc-dados/](../fora-da-fase-1/brasil/bncc-dados/README.md) | Arquitetura de dado normativo verificado e playbook de replicação |
| [bncc-pacotes/](../fora-da-fase-1/brasil/bncc-pacotes/README.md) | Distribuição para máquina (npm, PyPI, MCP) e aplicação ao VUOO |

### Pesquisa de 2026-11-05

| Arquivo | Frente organização e dados | Frente currículo, avaliação e inclusão |
|---|---|---|
| Modelo de dados | [modelo-de-dados.md](modelo-de-dados.md) | [modelo-de-dados-curriculo-avaliacao-inclusao.md](modelo-de-dados-curriculo-avaliacao-inclusao.md) |
| Terminologia (códigos) | [terminologia.md](terminologia.md) | [terminologia-curriculo-avaliacao-inclusao.md](terminologia-curriculo-avaliacao-inclusao.md) |
| Crosswalk com o Core | [crosswalk-core-organizacao.md](crosswalk-core-organizacao.md) | [crosswalk-core-curriculo-avaliacao-inclusao.md](crosswalk-core-curriculo-avaliacao-inclusao.md) |
| Cobertura D1–D8 | [cobertura-organizacao.md](cobertura-organizacao.md) | [cobertura-curriculo-avaliacao-inclusao.md](cobertura-curriculo-avaliacao-inclusao.md) |
| Questões abertas | [questoes-abertas-organizacao.md](questoes-abertas-organizacao.md) | [questoes-abertas-curriculo-avaliacao-inclusao.md](questoes-abertas-curriculo-avaliacao-inclusao.md) |
| Evidências | [evidencias-organizacao.md](evidencias-organizacao.md) | [evidencias-curriculo-avaliacao-inclusao.md](evidencias-curriculo-avaliacao-inclusao.md) |

### Fichas ([fichas/](fichas/))

- **Organização e dados:** [educacenso](fichas/educacenso.md), [inep-identificadores](fichas/inep-identificadores.md), [ldb](fichas/ldb.md), [educadados](fichas/educadados.md) (LC 220/2025 e Portaria 269/2026), [mec-gestao-presente](fichas/mec-gestao-presente.md), [cmdeb](fichas/cmdeb.md), [sed-sp](fichas/sed-sp.md)
- **Currículo:** [bncc](fichas/bncc.md), [bncc-computacao](fichas/bncc-computacao.md), [novo-ensino-medio](fichas/novo-ensino-medio.md), [dcn](fichas/dcn.md), [curriculo-paulista](fichas/curriculo-paulista.md)
- **Avaliação:** [saeb](fichas/saeb.md), [saresp](fichas/saresp.md), [cnca](fichas/cnca.md), [sinaes](fichas/sinaes.md) (standby)
- **Inclusão:** [aee-pneepei](fichas/aee-pneepei.md), [portaria-mec-421-2026](fichas/portaria-mec-421-2026.md), [resolucao-seduc-sp-129-2025](fichas/resolucao-seduc-sp-129-2025.md), [decreto-sp-67635](fichas/decreto-sp-67635.md), [lbi](fichas/lbi.md), [lei-14254](fichas/lei-14254.md), [lei-12764-tea](fichas/lei-12764-tea.md)
- **Dados:** [lgpd-educacao](fichas/lgpd-educacao.md), [eca-digital](fichas/eca-digital.md)

## O que falta para implementar

As decisões de 2026-11-05 estão em [../relatorio-infra-vuoo.md §7](../relatorio-infra-vuoo.md):

- CPF preferencial, com vínculo ao responsável para quem não tem;
- BNCC versão final como texto canônico: repositório **vuoo-base**, release v1.1 (https://github.com/arcade-metrics/v-base), `dados/bncc-2018.json` e `dados/bncc-computacao-2022.json`, extraídos da fonte oficial `fontes/bncc/BNCC_EI_EF_110518_versaofinal_site.pdf` (método em `ferramentas/METODO.md`);
- laudo como campo, sem armazenar documento;
- residência no Brasil inclusive para LLM;
- granularidade mínima Brasil, com variações de SP como dado e campos opcionais.

Ainda falta:

- leiaute da Situação do Aluno 2026, que ainda não foi publicado;
- redação literal da LDB;
- confirmar os papéis LGPD propostos (§7.6).

Itens de SP, como os cortes do SARESP e os códigos `*`/A/B/C do Currículo Paulista, deixaram de bloquear: entram como dado quando houver.
