# Qualidade e paridade entre linguagens

> **Fonte:** [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes), commit `e9b4985`: `docs/paridade.md`, `fixtures/consultas-douradas.json` (inspecionado por script), `packages/bncc/test/*.ts`, `python/tests/*.py`, `packages/mcp/test/tools.test.ts`, `mcp-worker/test/mcp.test.ts`, `.github/workflows/ci.yml`, `docs/manutencao.md` (seção CI). Analisado em 2026-11-04.
>
> Inspirar, não copiar: ver o aviso em [README.md](README.md).

## O risco que o mecanismo resolve

O plano do projeto registra como **risco número 1** da fase os pacotes npm e PyPI divergirem silenciosamente. Duas implementações da mesma lógica em linguagens diferentes são inevitáveis (runtimes diferentes); a resposta é um contrato executável.

## Consultas douradas

Um único arquivo JSON (`fixtures/consultas-douradas.json`) com `descricao`, `data_version` e uma lista de casos. Executado por dois runners: vitest no npm e pytest no PyPI.

Formato de um caso: `id`, `operacao`, `args`, `esperado`, `nota` opcional. `args` e `esperado` vêm em camelCase (convenção do TS); o runner Python converte mecanicamente para snake_case. Asserções abstratas (`praticaLinguagem`, `temLocalizadorPdf`, `competenciasNumeros`) são interpretadas por cada runner contra a forma do seu pacote.

Distribuição dos 50 casos no commit analisado:

| Operação | Casos | Confere |
|---|---|---|
| `contar_buscar` | 13 | quantidade de resultados de busca |
| `primeiros_buscar` | 7 | os N primeiros códigos, **posição a posição** |
| `decodificar` | 6 | partes do código |
| `contar_habilidadesEF` | 5 | contagem por filtro |
| `porCodigo` | 4 | etapa, anos, prática, fonte com página, competências |
| `contar_habilidadesEM` | 4 | contagem por filtro |
| `contar_objetivosEI` | 3 | contagem por filtro |
| `decodificar_erro` | 2 | mensagem de erro (regex) |
| `indice_busca_amostra` | 2 | radicais `k` e `kc` de um registro |
| `porCodigo_erro`, `contar_uniao_anos_ef`, `progressaoEI_codigos`, `estatisticas` | 1 cada | |

Prefixo `C*` no `id` marca as consultas do **caso de uso âncora** do projeto (teste de aceitação do dataset). Exemplo de âncora: 238 habilidades de Língua Portuguesa entre o 3º e o 6º ano.

## Regras do contrato

1. A fixture só muda por três motivos: mudança de dado justificada no changelog do dataset; operação nova da API (já implementada nas duas linguagens); caso novo de cobertura. **Nunca para o teste passar.**
2. Um runner novo se adapta à fixture, não o contrário. Foi assim que se validou a chegada do Python: 23 de 23 casos sem tocar o arquivo.
3. Toda operação pública ganha pelo menos um caso. "API sem caso dourado é API sem prova de paridade."
4. Valores esperados vêm do dataset validado, capturados por execução e conferidos contra o relatório de validação do dataset quando aplicável.
5. Quando um valor muda legitimamente (ex.: a busca da 0.5.0 levou `frações` de 6 para 22 resultados), o valor antigo fica anotado na `nota` do caso.

Contar não basta quando há ranking: dois pacotes podem devolver o mesmo conjunto em ordens diferentes. Por isso `primeiros_buscar` compara a ordem, com empate desfeito por código e pontuação arredondada antes de ordenar.

## Testes por camada

| Camada | O que se testa além da fixture |
|---|---|
| Núcleo TS (`nucleo.test.ts`) | não importa `node:fs`/`node:path`; mesmo registro que a API padrão; contagens com e sem o módulo de Computação; tabela de radicais e colisões aceitas; palavras vazias; ordem e desempate; singular, plural e derivado com mesmo topo; literal antes; parcial só quando necessário; caso EF08HI06 × EF08GE05; índice serializado reproduz `buscar()`; subpath de busca sem Node e sem dados |
| Pacote TS (`basico.test.ts`, `cjs-smoke.cjs`) | `versao()` com commit e checksums; case-insensitive; resolução de nomes; import CommonJS funcionando |
| Pacote Python | espelho da fixture + testes básicos |
| MCP | ver [04-mcp.md](04-mcp.md) |
| Worker | ver [04-mcp.md](04-mcp.md) |

## CI

Dois jobs, disparados em todo push e PR:

- `testar`: pnpm install com lockfile congelado, build e testes recursivos (npm, MCP, worker).
- `python`: `uv sync` e `pytest`.

O CI roda **exatamente** os mesmos comandos documentados para desenvolvimento local. Pegadinha registrada: a versão do pnpm vem só do `packageManager` do `package.json` raiz; declará-la também na action quebra.

## Verificações manuais obrigatórias antes de publicar

- `npm pack --dry-run`: o tarball é superfície pública própria; conferir que não entrou fixture interna, script de release nem caminho local.
- Smoke real depois de publicar: `npx` do MCP numa versão exata e `pip install` num venv limpo, repetindo uma consulta que exercite a mudança da versão; conferir que o MCP publicado aponta para a versão nova da lib.
