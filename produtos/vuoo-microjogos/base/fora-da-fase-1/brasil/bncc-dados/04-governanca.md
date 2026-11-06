# Governança

> **Fonte:** bncc-dados (commit `9c26897`): `docs/versionamento.md`, `CHANGELOG.md`, `DECISOES.md`, `CONTRIBUTING.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/*.yml`, `docs/politica-de-conteudo.md`, `docs/divisao-aberto-comercial.md`, `dados/LICENSE.md`, `CITATION.cff`, `AGENTS.md`, `llms.txt`. Analisado em 2026-11-04.

## Versionamento em duas trilhas

| Trilha | Formato | Responde a |
|---|---|---|
| Conteúdo | `dados-AAAA.MM`, patch `dados-AAAA.MM.N` | De quando é o retrato das fontes |
| Formato | semver do schema, `schema-vX.Y.Z` | Se a mudança quebra quem já consome |

As trilhas não se misturam: corrigir um texto não muda o schema, e adicionar um campo opcional não muda o conteúdo.

- Releases são tags imutáveis. Errou, publica-se um patch, e a tag nunca é movida.
- A versão da release vive num único lugar (`CITATION.cff`), e os derivados a leem de lá.
- Cada release vai para o Zenodo e recebe um DOI por versão e um DOI de conceito, que sempre resolve para a mais recente.

## Regras de ciclo de vida do registro

1. Registro publicado nunca é apagado (muda o status de vigência).
2. Código nunca é reutilizado.
3. Toda mudança de conteúdo cita a fonte oficial que a motivou.
4. Id cunhado é imutável, salvo defeito de extração, com mapa de substituição publicado.

## Taxonomia de eventos

| Evento | Tratamento |
|---|---|
| Mudança normativa (o mundo mudou) | Atualiza registro e vigência; changelog `normativa`; nova data-version |
| Errata oficial | Igual à mudança normativa, com a errata como fonte |
| Novo ato ou complemento | Novo documento ligado por `derivado_de`; não toca nos existentes |
| Correção de extração (nós erramos) | Corrige; changelog `correcao`; patch |
| Mudança de formato | Semver do schema |

A distinção entre `normativa` e `correcao` é obrigatória no changelog. O consumidor precisa saber se a norma mudou ou se o projeto errou.

## Registro de decisões

Toda inconsistência da fonte vira uma entrada numerada, com **contexto → decisão → fonte**. Propriedades do formato que valem copiar:

- Uma decisão pode ser **revista** por outra posterior, e as duas ficam: a antiga ganha a nota "revista pela decisão N".
- Riscos assumidos são registrados como risco, e não como ausência de risco, com a alternativa que fica disponível se a situação mudar.
- Cada entrada termina com a fonte concreta (páginas, arquivos, data da conferência).
- O extrator e o verificador referenciam o número da decisão nos comentários; o código e o registro apontam um para o outro.

Tipos de decisão que aparecem no projeto e devem ser esperados em qualquer fonte normativa:

| Tipo | Exemplo genérico |
|---|---|
| Fonte de extração contradiz a homologada | Planilha omite palavra presente no PDF → prevalece o homologado |
| Posição contradiz o identificador | Registro na aba errada → prevalece o código |
| Erro tipográfico da própria norma | Código com dígito a mais → canonizar pela gramática e guardar a forma impressa no localizador |
| Relação implícita na fonte | Vínculo mostrado por posição num quadro → reconstruir por regra e submeter à revisão humana |
| Licença de material de apoio | Material sem licença de redistribuição → substituir por mapa próprio verificado |
| Defeito do próprio pipeline | Ids gerados por quebra de linha → remover com mapa de substituição |

## Changelog

Organizado por release e, dentro dela, por Dados, Schema e Editorial. Cada item leva a categoria (`normativa`, `correcao`, `schema`, `editorial`) e, quando houver, o número da decisão. Mudanças de dado listam os códigos afetados.

## Contribuição

- Regra de ouro: **correção exige fonte oficial** (documento, página ou localizador).
- Divergência entre fontes oficiais exige propor também a entrada de decisão.
- Não se aceita: dado sem proveniência (inclusive gerado por LLM), conteúdo interpretativo no núcleo, material de terceiros com licença incompatível.
- O template de PR tem um checklist: não editei `dados/` à mão, rodei o pipeline, atualizei schema, decisões e changelog.
- Há templates de issue por tipo: correção de dado (com campo obrigatório de fonte oficial e confirmação de que é ato federal), mudança normativa, novo formato ou derivado.
- Branches com prefixo do tipo (`correcao/`, `normativa/`, `schema/`, `docs/`).

## Política de conteúdo

Documento público com: o que o dataset distribui, o que conta como problema (texto divergente, metadado errado, conteúdo indevido, dado pessoal), como os problemas são detectados, como reportar (issue pública para erro de dado, e-mail privado para dado pessoal ou segurança) e prazos-alvo de resposta, avaliação e correção.

O cuidado com dado pessoal aparece até nos detalhes: o metadado de autoria de uma planilha de apoio, que trazia o nome de um servidor, foi removido. O código de conduta tem uma seção sobre crianças e adolescentes, que proíbe dado de estudante em issues.

## Licenças e divisão aberto/comercial

- O texto normativo é ato oficial e não tem proteção autoral (Lei 9.610/98, art. 8º, IV). A licença CC BY 4.0 cobre a compilação, a estrutura, os identificadores e a curadoria.
- Código sob MIT.
- Compromisso público, registrado desde o primeiro commit: dados, pacotes, MCP local e site são **irrevogavelmente abertos**. Só serviços de conveniência (API com SLA, suporte, integrações sob medida) podem ser comerciais, e nada passa da coluna aberta para a comercial.
- O projeto se preparou para o registro como Digital Public Good, o que forçou a limpeza de licenças de todo o conteúdo distribuído.

## Documentação para agentes de IA

- `AGENTS.md`: regras invioláveis (nunca inventar códigos nem textos, nunca editar dado gerado, a área vem do código, texto normativo é imutável), um mapa do domínio em 30 segundos, como rodar o pipeline e convenções de idioma.
- `llms.txt`: resumo do dataset e links para cada arquivo de dados e documento.

Isso trata o agente de IA como consumidor de primeira classe, e a anti-alucinação como requisito.

## Bilinguismo

O português é a versão de referência. README, docs, notas de fontes e arquivos de comunidade têm versão em inglês, atualizada no mesmo PR. O registro de decisões tem só um resumo em inglês.
