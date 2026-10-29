# Benchmarks de produtos

Estudos agnósticos de produtos existentes, feitos para referência de mecânicas, arquitetura, estilo e evidência. Cada benchmark é uma pasta própria, com imagens e índices legíveis por máquina, e **não** segue o modelo documental de `conhecimento/` (marcas, ids e frontmatter): o formato de benchmark é outro, feito para teardown de produto.

A ponte com a base de conhecimento é um documento curto de estudo de caso no domínio `lms-e-plataformas`, com id estável, que aponta para a pasta daqui. Os produtos consumidores (em `produtos/`) citam o benchmark pelo caminho e, quando traduzem uma mecânica, registram a tradução no próprio produto, nunca aqui.

| Benchmark | Pasta | Id em conhecimento | Estado |
|---|---|---|---|
| Duolingo | [duolingo/](duolingo/) | `lms.case.duolingo` | completo (29/10/2026) |

## Convenções

- Pasta em minúsculas, nome do produto.
- `README.md` na raiz do benchmark com "como usar", convenções de marca de confiança e estrutura.
- Pesquisa bruta em `pesquisa/`, datada; capítulos derivados na raiz.
- Imagens em `imagens/` com `MANIFESTO.md` e índice JSON.
- Nenhum arquivo é movido ou renomeado depois de publicado; outros documentos apontam para cá.

## Candidatos a próximos benchmarks

Citados na proposta do projeto (`projeto/vuoo.md`, Tabelas 1 a 3) e em `produtos/vuoo-linguagem/pesquisa/c-benchmark.md`: Cogmed, EndeavorRx, CogniFit, Ello, Matific, Elefante Letrado, Khan Academy Kids. Cada um entra quando houver decisão de produto que dependa dele.
