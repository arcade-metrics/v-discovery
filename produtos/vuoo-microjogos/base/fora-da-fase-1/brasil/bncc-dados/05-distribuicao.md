# Distribuição

> **Fonte:** bncc-dados (commit `9c26897`): `README.md` (formas de acesso); bncc-pacotes: `docs/arquitetura.md`, `docs/paridade.md`, `fixtures/consultas-douradas.json`; bncc-benchmark: `README.md`. Analisado em 2026-11-04.

> **Análise detalhada** da camada de pacotes e MCP (API, busca, tools, paridade, operação, incidentes e aplicação ao VUOO): [../bncc-pacotes/](../bncc-pacotes/README.md). Este arquivo fica como resumo.

## Formas de acesso

Todas servem o mesmo dado, da mesma data-version:

| Mecanismo | Para quem | Característica |
|---|---|---|
| Arquivos JSON no repositório | Qualquer um | Fonte canônica, zero dependência |
| SQLite, dump SQL, CSV | Analistas, planilhas, SQL | Derivados conferidos no CI |
| Release no Zenodo | Pesquisa | DOI por versão, preservação de longo prazo |
| Pacote npm | Apps JavaScript/TypeScript | Dado embutido, sem dependências, funciona offline |
| Pacote PyPI | Python, notebooks | Idem; pandas como extra opcional |
| Servidor MCP local | Agentes de IA no computador do usuário | Roda com um comando, sem limite de uso |
| Servidor MCP remoto | Agentes em interfaces web | Só colar a URL; sem cadastro, com limite por IP |
| API REST | Integrações | Gratuita, sem chave, OpenAPI |
| Site | Pessoas | Uma página permanente por aprendizagem, em HTML, Markdown e CSV |

## Princípios da camada de distribuição

1. **Dado nunca flutua.** Cada pacote embute os JSON de um commit específico, com data-version e checksums num arquivo de versão. O script de sincronização recusa checkout sujo.
2. **Uma implementação por runtime.** O MCP importa o pacote npm e não reimplementa consulta. A duplicação inevitável (npm × PyPI) é vigiada por contrato.
3. **Núcleo injetável.** A lógica de consulta recebe os dados como parâmetro, sem acesso a disco. A mesma lógica roda em Node, em ambiente serverless e no site.
4. **API no idioma do dado.** Funções em português, na convenção de cada linguagem (camelCase no npm, snake_case no PyPI).
5. **Erros ensinam.** Um código inexistente recebe uma explicação ("bem formado, mas não existe; a numeração é contínua no grupo"), e não um `null` silencioso.

## Paridade entre linguagens: consultas douradas

Um único arquivo de casos de teste (operação, argumentos, resultado esperado) é executado pelo runner de cada pacote. Regras do contrato:

- A fixture só muda por mudança de dado justificada, operação nova (implementada nos dois pacotes) ou caso de cobertura novo. Nunca para um teste passar.
- Um runner novo se adapta à fixture, e não o contrário.
- Toda operação pública ganha pelo menos um caso.
- Os valores esperados vêm do dataset validado e incluem as consultas do caso âncora.

## Desenho das ferramentas MCP

- Poucas ferramentas (7): lookup por código, busca, listagem, estatísticas, decodificação, progressão e estrutura.
- Respostas em JSON estruturado; listagens sempre com limite padrão e total, para não inundar o contexto do agente.
- A `fonte` aparece em todo registro completo, para o agente poder citar.
- As instruções do servidor carregam um resumo do domínio.
- Camadas de terceiros com licença incompatível (não comercial) ficam de fora.

## Benchmark como prova de valor

Um repositório separado mede quanto os LLMs inventam códigos e textos da BNCC **sem** acesso à fonte estruturada, e quanto isso cai **com** grounding via MCP ou API. A metodologia é aberta e as respostas cruas são públicas, com um conjunto de teste privado contra contaminação.

Alguns resultados da rodada publicada: a fidelidade ao texto oficial varia de 88% a 3% entre modelos, e acertar o texto e recusar código falso são habilidades distintas. O benchmark transforma a tese do projeto ("dado estruturado e verificado reduz alucinação") em número e alimenta um leaderboard no site.

## Sequência de lançamento observada

1. Dataset completo e verificado, com CI (primeira data-version).
2. Pré-releases dos pacotes e do MCP (0.x), pinadas na data-version.
3. Site estático consumindo o pacote.
4. MCP remoto e API hospedada.
5. Auditoria independente → patch de correção → reforma do verificador.
6. Documentação completa (dicionário, política de conteúdo, inglês) e limpeza de licenças para o registro como bem público digital.
7. Benchmark.

A versão 1.0 dos pacotes fica condicionada a uma release de dados com revisão pedagógica registrada.
