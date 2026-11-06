# API de consulta e modelo exposto

> **Fonte:** [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes), commit `e9b4985`: `packages/bncc/src/tipos.ts`, `nucleo.ts`, `decodificar.ts`, `consultas.ts`; `python/bncc/_consultas.py`; `docs/manual-rapido.md`; `DECISOES.md` D3; dados embutidos em `packages/bncc/dados/` (inspecionados por script). Analisado em 2026-11-04.
>
> Inspirar, não copiar: ver o aviso em [README.md](README.md). O modelo do **dataset** (schema, identificadores, gramática de códigos) tem dono em [../bncc-dados/02-modelo-de-dados.md](../bncc-dados/02-modelo-de-dados.md); aqui fica só o que a camada de pacotes **expõe e acrescenta**.

## Superfície pública

| Função (TS / Python) | Retorno | Observação |
|---|---|---|
| `porCodigo` / `por_codigo` | registro resolvido | case-insensitive; lança erro explicativo se não existe |
| `habilidadesEF(filtro)` | lista | `componente`, `ano`, `unidadeTematica`, `pratica`, `campoAtuacao` |
| `habilidadesEM(filtro)` | lista | `area`, `competencia` (número), `apenasLP` |
| `objetivosEI(filtro)` | lista | `campo`, `grupoEtario` |
| `buscar(texto, filtro)` | lista ordenada, com `pontuacao` | filtros `etapa`, `componente`, `ano`; ver [03-busca.md](03-busca.md) |
| `indiceBusca()` | índice serializável | para reproduzir a busca no navegador |
| `progressaoEI(codigo)` | o mesmo objetivo nas 3 faixas etárias | só EI da BNCC 2018 |
| `decodificar(codigo)` | anatomia do código | não consulta o dataset |
| `estrutura()` | coleções estruturais | etapas, áreas, componentes, competências, campos |
| `estatisticas()` | contagens | inclui Computação quando o módulo está ligado |
| `versao()` | `{data_version, origem, commit, checksums_sha256}` | proveniência do dado embutido |
| `para_dataframe` (só Python, extra pandas) | DataFrame | conveniência para análise |

Nove consultas no núcleo. Filtros aceitam tanto a sigla curta (`'LP'`) quanto o id interno (`'ef-comp-lp'`): a normalização é feita no núcleo, não pelo chamador.

**API em português (D3).** `porCodigo()` no npm, `por_codigo()` no PyPI: mesma semântica, convenção de nome de cada linguagem. Justificativa: público brasileiro e um vocabulário (competência, habilidade, campo de experiências) sem equivalente estável em inglês; traduzir criaria uma camada de tradução mental.

## O registro resolvido

O dataset guarda referências por id (`"componente": "ef-comp-lp"`). A camada de pacotes entrega o registro **com os nomes resolvidos**, pronto para exibir ou citar. Forma comum a todas as etapas:

| Campo | Conteúdo |
|---|---|
| `codigo`, `etapa`, `texto` | identidade e enunciado oficial |
| `vigencia` | `{status: vigente / alterado / revogado, desde, ate}` |
| `fonte` | `{documento, arquivo, proveniencia, localizador, localizador_pdf}` |
| `documento` | presente só para módulos complementares (ex.: `computacao-2022`); ausente = documento principal |
| `pontuacao` | só em resultados de busca |

Campos por etapa: EI traz `campoExperiencias {id, nome}`, `grupoEtario`, `alinhamento`; EF traz `componente`, `anos`, `organizacao {tipo, nomes}`, `objetosConhecimento[]`; EM traz `area`, `componente | null`, `competenciasEspecificas[] {id, numero, texto}`, `camposAtuacaoSocial[]`.

Três padrões de modelagem que valem a pena notar:

1. **Organização do EF como união discriminada.** O mesmo tipo de registro organiza-se de três jeitos conforme o componente: `unidade_tematica` (a maioria), `campo_pratica` (Língua Portuguesa: campos de atuação + prática de linguagem) e `eixo` (Língua Inglesa: eixo + unidade temática). O campo `tipo` discrimina; a resolução devolve só os nomes que se aplicam.
2. **Proveniência em dois níveis.** `localizador` aponta a linha da planilha oficial; `localizador_pdf` aponta a página do PDF homologado. Exemplo real: `"aba Língua Portuguesa, linha 4"` e `"Base-Nacional-Comum-Curricular-BNCC.pdf, página PDF 101"`. A fonte vai junto em todo registro completo, para quem consome poder citar.
3. **Vigência por registro**, com a data-version como marco (`desde: "dados-2026.07"`), não uma data civil. Prepara o terreno para mudanças normativas sem apagar o histórico.

Os tipos TypeScript são **espelho manual** dos JSON Schemas do dataset; a validação de conformidade acontece no repositório de dados, não aqui.

## Decodificador de códigos

Função pura, sem dataset, porta fiel do decodificador do pipeline de dados. Gramáticas reconhecidas:

| Padrão | Exemplo | Partes |
|---|---|---|
| `EI` + grupo (01 a 03) + campo (EO, CG, TS, EF, ET) + sequência | `EI02TS01` | faixa etária, campo de experiências |
| `EI` + grupo + `CO` + sequência | `EI03CO01` | Computação na EI |
| `EF` + ano (01 a 09) ou bloco + componente + sequência | `EF67LP08` | anos 6 e 7, Língua Portuguesa |
| `EM13` + área (LGG, MAT, CNT, CHS) + competência (1 dígito) + sequência | `EM13LGG103` | competência 1, item 3 |
| `EM13LP` + sequência | `EM13LP02` | Língua Portuguesa no EM, sem competência no código |
| `EM13CO` + sequência | `EM13CO26` | Computação no EM |

Blocos do EF (`15`, `69`, `12`, `35`, `67`, `89`) só valem para certos componentes: Arte aceita `15` e `69`; Educação Física, `12`, `35`, `67`, `89`; Língua Portuguesa, todos; Computação, `15` e `69` além de ano a ano. Bloco inválido para o componente gera erro específico.

Separação importante: **decodificar não é validar existência.** Um código pode ser gramaticalmente perfeito e não existir. A tool do MCP diz isso explicitamente na descrição.

## Erros que ensinam

Quando o código é bem formado mas não está nos dados, o núcleo primeiro decodifica (o que gera erro de gramática se for o caso) e depois lança uma mensagem que explica **por que** não existe: a numeração é contínua dentro de cada grupo, e nos códigos de EM a centena é a competência (depois de `EM13LGG105` vem `EM13LGG201`, não `EM13LGG106`). Nunca devolve `null`.

O raciocínio: para uma fonte anti-alucinação, um `null` ou uma lista vazia sem contexto confirmam ao modelo de linguagem que ele pode inventar. A mensagem antecipa a inferência errada mais provável (deduzir o vizinho) e a desarma. A redação dessa mensagem foi corrigida em 0.6.1, quando se descobriu que afirmava "lacunas legítimas" na numeração que, verificadas, não existiam (ver [07-licoes-e-incidentes.md](07-licoes-e-incidentes.md)).

Outros erros seguem a mesma linha: progressão pedida para código que não é EI explica que o alinhamento só existe na EI; para código de Computação, explica que o complemento não tem alinhamento oficial entre faixas.

## Dados embutidos (dados-2026.08)

| Arquivo | Conteúdo | Contagem |
|---|---|---|
| `estrutura.json` | documentos curriculares, etapas, modalidades, áreas, componentes, recortes temporais, campos, direitos, competências | 2 documentos, 3 etapas, 9 áreas, 21 componentes, 10 competências gerais, 105 específicas |
| `educacao-infantil.json` | objetivos + alinhamentos entre faixas | 93 objetivos, 32 alinhamentos |
| `ensino-fundamental.json` | habilidades + contextos de organização | 1.304 habilidades, 873 contextos |
| `ensino-medio.json` | habilidades + contextos | 183 habilidades, 6 contextos |
| `computacao.json` | eixos, objetos, competências, objetivos e habilidades de Computação | 3 eixos, 59 objetos, 14 competências, 141 aprendizagens |
| `perfis.json` | papéis (professor, aluno, gestor, responsável, coordenador) com sinônimos | 5 |
| `marcos-legais.json` | normas que fundamentam a BNCC, com relações | 20 |
| `VERSAO.json` | data-version, commit de origem, SHA-256 de cada arquivo | 1 |

Total servido: 1.580 aprendizagens da BNCC 2018 + 141 de Computação = **1.721**. `perfis` e `marcos-legais` viajam no pacote mas não têm consulta própria na API.

Os **alinhamentos da EI** carregam nota de proveniência da própria interpretação, por exemplo: pareamento pela posição sequencial, "confirmado em revisão pedagógica (07/2026)". Interpretação do projeto fica marcada como tal, separada do texto oficial.
