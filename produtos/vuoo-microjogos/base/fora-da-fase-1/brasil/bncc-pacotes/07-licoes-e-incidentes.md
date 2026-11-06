# Lições e incidentes

> **Fonte:** [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes), commit `e9b4985`: `CHANGELOG.md`, `DECISOES.md` (D6, D8, D9, D10), `mcp-worker/README.md`, `mcp-worker/src/index.ts`, `docs/manutencao.md` (troubleshooting), histórico de commits (`git log`, 103 commits). Analisado em 2026-11-04.
>
> Inspirar, não copiar: ver o aviso em [README.md](README.md).

Cada regra rígida do repositório tem um incidente por trás. A tabela registra o que aconteceu e a regra que nasceu, para o VUOO herdar a lição sem repetir o erro.

| # | Incidente | Efeito | Regra que nasceu |
|---|---|---|---|
| 1 | MCP 0.1.0 publicado com `npm publish` | a dependência `workspace:*` não foi convertida; pacote ininstalável, depreciado no mesmo dia (09/07/2026) | D6: sempre `pnpm publish`; repetido no AGENTS, CONTRIBUTING e runbook |
| 2 | `VERSAO.json` gravava o caminho absoluto da máquina de quem sincronizou | o diretório pessoal do mantenedor viajou dentro do tarball do npm e do wheel do PyPI até a 0.3.1 / 0.2.0 | D8: só o nome do diretório; o `commit` é o que identifica a origem. Achado de auditoria antes de abrir o repo. Gerou o item "segredo dentro do tarball" no SECURITY e o `npm pack --dry-run` obrigatório |
| 3 | Filtro `componente: "CO"` em `buscar` devolvia sempre zero (issue #8) | os registros de Computação não têm o campo `componente` (é sintetizado na resolução) | o filtro passou a seguir a mesma regra das listagens; caso dourado novo |
| 4 | Busca por substring sem ranking (issues #9, #14) | `de` casava 94% da Base; `texto` casava `contexto`; singular e plural disjuntos | D10 inteiro, ver [03-busca.md](03-busca.md) |
| 5 | Mensagem de erro afirmava que a numeração tinha "lacunas legítimas" | a afirmação era falsa (verificado: sequências de 1 a n em todos os grupos) e **ensinava o agente a aceitar códigos inventados como plausíveis** | 0.6.1: mensagem e instruções corrigidas, com a regra da centena no EM. Lição: o texto do erro é afirmação factual e precisa ser verificado como o dado |
| 6 | Gate "nada sai antes da 1.0" lido literalmente | um export necessário ficou impublicável; um consumidor interno ficou preso a tarball vendorizado no próprio repo | D9: o gate protege a revisão pedagógica do dado, não a superfície de código |
| 7 | Browser Integrity Check da Cloudflare (issue #13) | 403 com `error code: 1010` para clientes HTTP de biblioteca, antes de chegar ao worker | desligado no subdomínio do MCP; nota no README: 403 em texto puro, sem `{erro, dica}`, é a CDN, não o código |
| 8 | Erro de protocolo virava 500 (issue #6) | o ChatGPT abortava a conexão em vez de negociar a versão do protocolo | repassar a `HTTPException` do transporte; teste "versão desconhecida vira erro JSON-RPC, nunca 500" |
| 9 | `@hono/mcp` respondia `"null"` com 202 | violava a especificação (202 sem corpo) | o worker reescreve a resposta até a correção upstream; teste dedicado |
| 10 | `pnpm deploy` | comando reservado do pnpm, não o script do projeto | sempre `pnpm run deploy`, anotado em dois lugares |
| 11 | `uv publish` enviou artefatos antigos | ele publica tudo o que está em `dist/` | `rm -rf dist` antes do build |
| 12 | Versão do pnpm declarada no `package.json` e na action do CI | `ERR_PNPM_BAD_PM_VERSION` | versão só no `packageManager` |
| 13 | Script ESM solto não achava dependências | a resolução ESM sobe a partir do arquivo | scripts que importam dependências moram dentro do pacote que as declara |
| 14 | `pip` do sistema no macOS aponta para Python 3.9 | `Requires-Python >=3.10` | manual de uso recomenda `uv` ou venv com interpretador explícito |

## Padrões que atravessam os incidentes

- **O erro vira regra escrita no lugar onde o próximo vai tropeçar**: AGENTS.md (agentes), CONTRIBUTING.md (contribuidores), runbook (mantenedor), comentário no código (quem edita). A mesma regra aparece em mais de um, de propósito.
- **Toda correção de comportamento ganha um teste** que reproduz o incidente, com o número da issue no nome.
- **Mudança de semântica é minor, sempre**, mesmo em 0.x, e o changelog diz qual consulta muda e quantos casos da fixture mudaram de valor.
- **O artefato publicado é tratado como superfície própria** (tarball, wheel, bundle do worker), com verificação separada do código-fonte.
