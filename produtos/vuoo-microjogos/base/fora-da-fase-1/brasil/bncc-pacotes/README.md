# bncc-pacotes: análise das interfaces para máquina e aplicação ao VUOO

> **Fonte:** repositório [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) (<https://github.com/bncc-dev/bncc-pacotes>), commit `e9b4985` (15/10/2026), 103 commits no histórico. Versões no commit: `@bncc/dados` 0.7.0, `@bncc/mcp` 0.5.0, `bncc` (PyPI) 0.6.0, dados embutidos `dados-2026.08` (commit `9c26897` do bncc-dados). Mantido pela Profy Tecnologias Educacionais Ltda. Código sob MIT, dados embutidos sob CC BY 4.0, nome e identidade visual "bncc.dev" não licenciados. Analisado em 2026-11-04.

> **Inspirar, não copiar.** Este material existe para o VUOO **aprender com** o bncc-pacotes, não para reproduzi-lo. Não copiamos código, textos de documentação, descrições de tools, nomes de produto nem identidade visual. O texto desta pasta é análise nossa, com o arquivo de origem citado em cada seção. Onde o VUOO precisar do **dado** da BNCC, consome-se da fonte publicada (pacote, API ou release), com a atribuição exigida pela CC BY 4.0. Onde precisar de um mecanismo parecido, ele é redesenhado para o nosso contexto e registrado como ADR próprio em `produtos/vuoo-microjogos/padroes/`.

## Para que serve

O bncc-pacotes é a camada que transforma um dataset curricular verificado (o [bncc-dados](https://github.com/bncc-dev/bncc-dados), analisado em [../bncc-dados/](../bncc-dados/README.md)) em **interfaces consumíveis**: biblioteca TypeScript, biblioteca Python e servidor MCP para agentes de IA, local e hospedado. O VUOO planeja uma camada equivalente para o próprio grafo de conhecimento e para o VUOO Bot. Esta pasta:

1. **Disseca** o repositório: arquitetura, API, busca, MCP, qualidade, operação e os incidentes que moldaram as regras.
2. **Traduz** o que vale para a arquitetura do VUOO, com o que adotar, adaptar ou recusar, e lista candidatos a ADR.

Divisão de donos (regra "cada fato tem um dono"): o **dataset** (extração, schema, verificação, versionamento do dado) é assunto de [../bncc-dados/](../bncc-dados/README.md). Esta pasta é dona da **camada de distribuição em profundidade**; o resumo em [../bncc-dados/05-distribuicao.md](../bncc-dados/05-distribuicao.md) aponta para cá.

## Conteúdo

| Arquivo | O que tem |
|---|---|
| [01-arquitetura.md](01-arquitetura.md) | Desenho em uma frase, monorepo e linha de corte, os quatro projetos, núcleo injetável e cascas, subpaths, ecossistema |
| [02-api-e-modelo.md](02-api-e-modelo.md) | Superfície de consulta, registro resolvido, proveniência, vigência, filtros, decodificador, erros que ensinam, dados embutidos |
| [03-busca.md](03-busca.md) | O algoritmo de busca: normalização, palavras vazias, radical, BM25, estratos, índice serializável, medições |
| [04-mcp.md](04-mcp.md) | As 7 tools, descrição como produto, instruções do servidor, MCP remoto stateless em Workers, rate limit, CORS, erros HTTP |
| [05-qualidade-e-paridade.md](05-qualidade-e-paridade.md) | Fixture dourada (50 casos), contrato de paridade, testes por camada, CI |
| [06-operacao-e-governanca.md](06-operacao-e-governanca.md) | Sincronização pinada, `VERSAO.json`, publicação, gate da 1.0, changelog, licenças, segurança, templates, AGENTS.md, métricas de uso |
| [07-licoes-e-incidentes.md](07-licoes-e-incidentes.md) | Os incidentes registrados e a regra que cada um gerou |
| [10-aplicacao-vuoo.md](10-aplicacao-vuoo.md) | **A tradução:** adotar, adaptar, recusar; arquitetura proposta para o VUOO; candidatos a ADR; perguntas em aberto |

## Leitura rápida

1. **O dado não nasce aqui.** Os pacotes embutem uma cópia pinada (commit + SHA-256) do dataset; ninguém edita os JSONs à mão.
2. **Uma única implementação de consulta por linguagem.** Toda a lógica vive numa função que recebe os dados por parâmetro (`criarConsultas(dados)`); biblioteca, MCP local, MCP remoto e API só injetam dados e delegam.
3. **Duas linguagens, uma prova.** Um único arquivo de consultas douradas roda no vitest e no pytest; se um lado diverge, o CI reprova.
4. **Para agentes, a descrição da tool é produto** e o erro ensina: código inexistente recebe explicação, nunca `null`, para não convidar à alucinação.
5. **Zero rede e zero dependência** nos pacotes de dados: funciona offline, sem chave, sem serviço no caminho da consulta.

## Como foi obtido

`git clone` do repositório público em 2026-11-04 (cópia de trabalho no scratchpad da sessão, fora deste repositório). Lidos na íntegra: `README.md`, `AGENTS.md`, `DECISOES.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`, `CITATION.cff`, `LICENSE*`, `docs/*.md`, `mcp-worker/README.md`, `mcp-worker/wrangler.toml`, `.github/` (CI, templates de PR e issue), todo o código de `packages/bncc/src/`, `packages/mcp/src/`, `mcp-worker/src/`, `scripts/` e os testes. Dados embutidos e fixture inspecionados por script (contagens e formato de registro). Nenhum arquivo do repositório foi copiado para cá.

## Limites

- Retrato do commit `e9b4985`. O CHANGELOG marca 0.7.0 / 0.5.0 / 0.6.0 como "a publicar" nesse commit; as versões no npm e PyPI podem estar à frente.
- Não analisados aqui (repos separados): `bncc-site` (Astro), `bncc-api` (REST em Workers), `bncc-benchmark` (só resumido em [../bncc-dados/05-distribuicao.md](../bncc-dados/05-distribuicao.md)), `bncc-playground`. O `docs/plano-abertura.md` citado em D8 é interno e não está no repo.
- Nada foi executado (build, testes, servidor). As afirmações sobre comportamento vêm do código e da documentação.
