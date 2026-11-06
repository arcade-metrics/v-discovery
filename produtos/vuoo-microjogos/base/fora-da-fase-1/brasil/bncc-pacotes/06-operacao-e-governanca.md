# Operação e governança

> **Fonte:** [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes), commit `e9b4985`: `scripts/sincronizar-dados.mjs`, `packages/bncc/dados/VERSAO.json`, `docs/manutencao.md`, `DECISOES.md` (D6 a D9), `CHANGELOG.md`, `CONTRIBUTING.md`, `AGENTS.md`, `SECURITY.md`, `CITATION.cff`, `LICENSE`, `LICENSE-DADOS.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/*`, `scripts/estatisticas.mjs`, `scripts/lib/coleta.mjs`, `python/pyproject.toml`. Analisado em 2026-11-04.
>
> Inspirar, não copiar: ver o aviso em [README.md](README.md). Governança do **dataset** (decisões de interpretação, versionamento do dado, DOI) tem dono em [../bncc-dados/04-governanca.md](../bncc-dados/04-governanca.md).

## Sincronização pinada do dado

Um script (Node, só biblioteca padrão) recebe o caminho de um checkout do dataset e:

1. **Recusa checkout sujo** (`git status --porcelain` não vazio → sai com erro).
2. Lê o commit (`rev-parse HEAD`).
3. Calcula SHA-256 de cada um dos 7 arquivos de uma lista explícita (origem → nome no pacote).
4. Determina a **data-version**: a tag `dados-*` exata do commit; senão, a tag `dados-*` mais recente alcançável **se a pasta `dados/` for idêntica à dela** (cobre um commit só de documentação depois da tag); senão, cai no campo `vigencia.desde` do primeiro registro, com aviso.
5. Copia os arquivos para os dois destinos (npm e Python) e grava `VERSAO.json` igual nos dois.

`VERSAO.json` real: `data_version`, `origem` (URL do repo), `commit` (hash completo), `sincronizado_de` (só o nome do diretório, nunca o caminho absoluto, ver D8 em [07-licoes-e-incidentes.md](07-licoes-e-incidentes.md)) e `checksums_sha256` por arquivo. O arquivo viaja dentro do tarball e do wheel e é exposto em runtime por `versao()`.

## Publicação (runbook)

Só o mantenedor humano publica: npm pede 2FA no navegador, PyPI pede token. Agentes de IA são proibidos de publicar (`AGENTS.md`, regra 5).

1. **No PR da versão:** bump nos três manifestos; entrada no CHANGELOG com data `a publicar`; busca por textos em README, `docs/` e no worker que ainda descrevam o comportamento antigo.
2. **Registries, na main atualizada:** build; `pnpm publish` do pacote de dados; `pnpm publish` do MCP; limpar `dist/` e `uv build` + `uv publish` do Python. Sempre `pnpm publish` (D6). Limpar `dist/` porque o `uv publish` envia tudo o que estiver lá, inclusive versões antigas.
3. **Smoke real** em ambiente limpo, com a versão exata, exercitando a mudança.
4. **Deploy do MCP remoto**, obrigatório quando os pacotes mudam (ele builda do workspace, não do npm): bump, build, testes, `--dry-run` do bundle, deploy, Inspector contra produção; conferir `serverInfo.version`, o header de versão do dado e uma chamada à tool afetada.
5. **Registrar a publicação** num commit dedicado (`docs: registra a publicação de ...`): troca `a publicar` pela data, anota as verificações feitas e os números observados, fecha as issues apontando PR e versões.

Detalhe registrado: em semver 0.x, `^0.y.z` não aceita minor nova, então consumidores não recebem 0.x novas sozinhos.

## Gate da 1.0 (D9)

A `1.0.0` dos três pacotes só sai depois da release `dados-v1.0.0` do dataset, que traz **revisão pedagógica registrada**. Pré-releases 0.x podem sair antes: o gate protege a revisão pedagógica do dado, não a superfície de código. A leitura literal anterior ("nada sai até a 1.0") travava um export necessário e obrigava um consumidor interno a usar um tarball vendorizado.

## Changelog

Uma seção por pacote, versões em ordem decrescente, mais uma seção "Não publicado" no topo. Cada entrada diz: o que mudou, por que, issue de origem, **se muda semântica** (justifica minor), impacto na fixture (casos novos, valores revisados com o antigo anotado), data-version embutida e, no MCP, desde quando está no ar no remoto. Mudanças de dado citam o número da decisão e o DOI da versão no dataset.

## Registro de decisões (`DECISOES.md`)

Mesmo formato nos três repos do ecossistema: `## Dn · título`, **Decisão**, **Por quê**, e quando cabe **Custo aceito**, **Consequências**, **Aplicado em**, **O que não mudou**, **O que fica de fora**. O objetivo declarado é que "ninguém precise arqueologia de commit". Decisões D1 a D10 resumidas ao longo desta pasta.

## Contribuição

- **Regra de ouro** (núcleo injetável como única superfície) e cinco regras derivadas: não editar dados à mão; API muda nas duas linguagens ou em nenhuma; fixture não se ajusta para passar; zero dependências de runtime (dependência nova exige justificativa); nunca inventar códigos.
- **Lista explícita do que não se aceita**, incluindo "conteúdo gerado por LLM apresentado como texto oficial" e "material de terceiros com licença incompatível (ex.: CC BY-NC)". Por isso não há camada de priorização curricular de terceiros licenciada como não comercial.
- **Template de PR** com categoria (`correcao`, `api`, `mcp`, `dados`, `editorial`) e checkboxes da regra de ouro, da paridade e do checklist local. "Se você precisou escrever a mesma lógica duas vezes no mesmo runtime, pare e abra uma issue."
- **Templates de issue** que **roteiam**: erro no conteúdo do dado vai para o repo do dataset (link direto no `config.yml`), dúvida de uso vai para Discussions, segurança vai para o canal privado. Issue de "nova consulta ou tool" exige caso de uso, assinatura nas duas linguagens e checkbox obrigatório confirmando que a lógica vai para o núcleo.

## Documentação para agentes de IA

`AGENTS.md` curto e imperativo: o que o repo é; 7 regras que nunca se quebram; convenções (API pt-BR, prefixo das tools, erros que ensinam, **sem travessão em documento público**); comandos; e um "mapa do domínio em 30 segundos" com os três formatos de código. Os mesmos princípios aparecem no `CONTRIBUTING.md` para humanos.

## Licenças e marca

- Código MIT, dados CC BY 4.0, em arquivos separados, e um `LICENSE` que explica a divisão: o mesmo artefato publicado carrega as duas naturezas, e uma licença única "mentiria sobre uma delas". O `pyproject.toml` anota que o campo `license = "MIT"` descreve só o código.
- Atribuição sugerida dos dados: "Dados da BNCC estruturados por bncc.dev (https://github.com/bncc-dev/bncc-dados), CC BY 4.0".
- **Nome e identidade visual não licenciados**: "o código é livre; a marca não". Derivados não podem se apresentar como o projeto.
- `CITATION.cff` do software, com referência ao dataset (versão, DOI da versão e DOI de conceito) e o aviso de que, para citar o dado, usa-se o CITATION do dataset.

## Segurança

`SECURITY.md` com escopo específico do tipo de projeto: código que execute algo ao ser importado (por isso zero dependências), dependência ou CI comprometidos, abuso do endpoint público, **segredo exposto no histórico ou dentro do tarball publicado**, cadeia de publicação. Erro de dado explicitamente **não** é segurança. Canal por e-mail com prefixo de assunto ou reporte privado do GitHub; prazos-alvo de 3 dias úteis (recebimento) e 10 dias úteis (avaliação).

## Métricas de uso com privacidade

Script de painel no terminal que junta downloads do npm e PyPI (públicos), requisições do Cloudflare (MCP remoto) e da AWS (API e site), e acrescenta uma linha a um histórico. Escolhas:

- **O histórico é o ponto:** as fontes têm retenção curta (janela móvel nos registries; um dia por consulta no plano gratuito do Cloudflare). "O dado que não for capturado hoje não existe mais depois."
- **O histórico mora fora do repositório** (diretório do usuário): o repo é público e série de tráfego não é material de divulgação.
- **Nenhum IP coletado ou gravado:** agregação sempre por serviço.
- Coleta separada da apresentação, para o mesmo código servir CLI hoje e uma função serverless depois. Cada fonte falha isolada: sem credencial, é marcada indisponível e o resto sai igual.
