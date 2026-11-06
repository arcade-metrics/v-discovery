# Servidor MCP: local e remoto

> **Fonte:** [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes), commit `e9b4985`: `packages/mcp/src/tools.ts`, `packages/mcp/src/servidor.ts`, `packages/mcp/test/tools.test.ts`, `mcp-worker/README.md`, `mcp-worker/src/index.ts`, `mcp-worker/src/dados.ts`, `mcp-worker/wrangler.toml`, `mcp-worker/test/mcp.test.ts`, `docs/arquitetura.md`, `docs/manutencao.md`, `AGENTS.md`. Analisado em 2026-11-04.
>
> Inspirar, não copiar: ver o aviso em [README.md](README.md). As descrições das tools do bncc-pacotes **não** devem ser copiadas; o que se aproveita é o método de escrevê-las.

## As 7 tools

| Tool | Faz | Entrada | Limite padrão / máx. |
|---|---|---|---|
| `bncc_lookup` | registro completo por código | `codigo` | (um registro) |
| `bncc_buscar` | busca textual ordenada | `texto`, `etapa?`, `componente?`, `ano?`, `limite` | 20 / 100 |
| `bncc_listar` | listagem por filtros estruturados | `etapa` + filtros da etapa, `limite` | 50 / 200 |
| `bncc_decodificar` | anatomia de um código, sem consultar dados | `codigo` | |
| `bncc_progressao_ei` | o mesmo objetivo nas 3 faixas etárias | `codigo` | |
| `bncc_estrutura` | coleções estruturais; sem argumento, índice com contagens | `colecao?` (enum) | |
| `bncc_estatisticas` | contagens + versão do dado | | |

Convenções: prefixo do domínio (`bncc_`), snake_case, títulos e descrições em português. Quatro nomes convergem com um servidor MCP pioneiro de terceiros (lookup, buscar, listar, estatisticas), para quem já conhecia; três são novos.

**Poucas tools, de propósito.** O runbook pede para avaliar se uma consulta nova "merece virar tool", porque "tools demais confundem o agente". O MCP expõe 7 das 9 consultas do núcleo; `indiceBusca` e `versao` ficam fora (versão vai dentro de `bncc_estatisticas`).

## Descrição de tool é produto

Regra do `AGENTS.md`: a descrição se revisa como copy. Cada descrição segue a mesma anatomia:

1. **O que faz**, com exemplos concretos de entrada (códigos das três etapas).
2. **Quando usar** ("sempre que o usuário mencionar um código", "para cobertura curricular").
3. **Como interpretar a saída** (`{total, exibindo, resultados}`; se `total > exibindo`, refine ou aumente o limite).
4. **Regra anti-alucinação** ("nunca cite de memória"; "decodificar não confere existência, use lookup").
5. **Vocabulário válido** inline (siglas dos componentes, áreas, campos, faixas), para o agente não adivinhar parâmetros.

Os parâmetros têm `describe()` no schema zod com exemplo; enums onde o domínio é fechado (`etapa`, `colecao`); faixas numéricas validadas (`ano` 1 a 9).

## Instruções do servidor

O handshake MCP carrega um texto de `instructions` gerado em runtime, com:

- contagem dinâmica do dataset (não fica desatualizada quando o dado muda);
- três regras numeradas: não inventar códigos ou textos; não deduzir códigos de vizinhos (com a explicação da centena no EM); ao citar, incluir código e fonte;
- mapa do domínio em uma linha por etapa, com exemplo de código;
- aviso de que o complemento de Computação está incluído;
- a data-version.

É o "system prompt" que o servidor injeta no agente. Gerado por função (`instrucoesServidor`) compartilhada entre stdio e remoto.

## Formato das respostas

- JSON estruturado como texto (`content[0].text`), indentado com 1 espaço.
- Listagens passam por `compacto()` (código, etapa, texto, pontuação, nome do componente/área/campo, anos) e por `limitar()` (`{total, exibindo, resultados}`). Não inunda o contexto do agente.
- Registro completo (lookup) sempre com `fonte`.
- Erros com `isError: true` e `{erro: mensagem}`, onde a mensagem é a mesma pedagógica do núcleo.

## Casca fina, runtime-agnóstica

`registrarTools(servidor, consultas, versao)` recebe o objeto `Consultas` já montado. Handlers têm uma linha útil (chamar a consulta, embrulhar em `json` ou `erro`). O stdio monta `Consultas` com a casca de disco; o remoto, com `criarConsultas` sobre JSONs importados. Nenhuma tool contém lógica de domínio: se precisar, ela vai para o núcleo, nas duas linguagens.

## MCP remoto (mcp.bncc.dev)

Stack: Cloudflare Workers + Hono + `@hono/mcp` (streamable HTTP sobre Request/Response padrão web). Bundle ~368 KB gzip.

| Decisão | Detalhe | Por quê |
|---|---|---|
| Stateless | `McpServer` e transporte novos por request, `sessionIdGenerator: undefined`, sem Durable Objects | tools só de leitura, dado imutável por data-version; evita colisão de ids entre clientes |
| JSON, não SSE | `enableJsonResponse: true` | resposta simples por POST |
| Dados no escopo do módulo | `criarConsultas` uma vez por cold start | custo de indexação pago uma vez |
| `POST /` e `POST /mcp` | `/mcp` é a URL canônica; a raiz também atende | elimina erro de quem cola a URL sem path |
| `GET` de navegador | `Accept: text/html` recebe página humana de documentação | a URL do MCP é também a página de ajuda |
| `GET` SSE e `DELETE` | 405 com `{erro, dica}` explicando que não há sessão nem stream | erros que ensinam também em HTTP |
| 404 e 500 | `{erro, dica}` apontando a URL certa ou onde reportar | idem |
| Erro de protocolo | `HTTPException` do transporte é repassada, não mascarada como 500 | um 500 fazia o ChatGPT abortar em vez de negociar a versão do protocolo |
| 202 sem corpo | notificações respondem 202 vazio; corrige o `"null"` que a lib devolvia | conformidade com a especificação |
| Rate limit | 60 req/min por IP, binding nativo do Workers; o 429 aponta o MCP local como alternativa sem limite | proteger o serviço sem cadastro nem chave |
| Tolerância | sem o binding (dev e testes), segue sem limite | testes não dependem de infraestrutura |
| CORS aberto | expõe `mcp-session-id` e `mcp-protocol-version` | clientes MCP de navegador precisam ler esses headers |
| Header de versão | `X-BNCC-Data-Version` em toda resposta | observabilidade e citação |
| Sem cadastro, sem chave | | atrito zero: colar a URL no cliente |
| Sem `workers.dev` | só o domínio próprio | uma URL pública, uma reputação |
| Anti-bot desligado | Browser Integrity Check da Cloudflare off para o subdomínio | barrava User-Agents de bibliotecas HTTP com 403 antes do worker; endpoint de máquina se protege por rate limit |

Os namespaces de rate limit são numerados por serviço (API, contato, MCP) e reservados, mesmo depois de um serviço sair do repo.

## Testes do MCP

- **Tools** (`tools.test.ts`): cliente real do SDK via transporte em memória. Conferem: exatamente 7 tools; lookup com fonte; código inexistente com `isError` e mensagem pedagógica; limite e total; pontuação decrescente; listagem nas três etapas; decodificar código inexistente; progressão; estrutura sem argumento; versão nas estatísticas; instruções com contagem e versão.
- **Worker** (`mcp.test.ts`, 20 casos): handshake, notificação 202 sem corpo, versão de protocolo desconhecida vira erro JSON-RPC (nunca 500), tools via HTTP, Computação, raiz atende MCP, página HTML, 405s, preflight CORS, 429 e ausência do binding.
- **E2E** contra o binário real (`scripts/e2e.mjs`) e **teste de aceitação** (`scripts/teste-completo.mjs`).
- **Produção:** MCP Inspector em modo CLI listando as tools no endpoint público depois de cada deploy.

## Distribuição do MCP

- Local: `npx -y @bncc/mcp` (Claude Code: `claude mcp add`; Claude Desktop e Cursor: bloco JSON).
- Remoto: colar a URL em Claude, ChatGPT ou Cursor.
- Listado no Smithery (indexa por organização/repositório, não pelo nome do pacote). Registries ainda não usados anotados no runbook: mcp.so, Glama, LobeHub, awesome-mcp-servers; todos pedem o mesmo conjunto de metadados, "prepare uma vez e reaproveite".
