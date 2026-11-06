# Modelo de dados

> **Fonte:** bncc-dados (commit `9c26897`): `docs/modelo-de-dados.md`, `docs/dicionario-de-dados.md`, `schema/*.json`, `pipeline/codigos.py`, estrutura dos JSON em `dados/`. Analisado em 2026-11-04. Análise própria; contagens conferidas nos arquivos.

## Princípio: honestidade estrutural

A BNCC organiza cada etapa de um jeito diferente. O modelo **não força um formato comum** com campos nulos: cada etapa tem a própria entidade e a própria organização.

| | Educação Infantil | Ensino Fundamental | Ensino Médio |
|---|---|---|---|
| Unidade | objetivo de aprendizagem | habilidade | habilidade |
| Organização | campo de experiências × grupo etário | unidade temática; em LP, campos de atuação + prática; em LI, eixo | área do conhecimento (e LP como componente) |
| Tempo | 3 faixas etárias | ano ou bloco de anos | sem seriação |
| Vínculo com competência | não há | não há por habilidade | 1 (no código) ou 1 a n (LP, da planilha) |

As assimetrias da fonte **viram dado**, não exceção de código. Exemplos: componente sem habilidades próprias tem uma flag que diz isso; componente presente só em alguns anos declara os anos; um campo da organização é obrigatório só para o componente que o usa, e o schema impõe essa regra.

Lição para replicar: **modele a fonte como ela é**, mesmo que fique irregular. Normalizar para um formato bonito apaga informação e cria dado que a fonte não sustenta.

## Identificadores

Há dois regimes, e a fronteira entre eles é nítida:

| Regime | Quando | Forma | Regra |
|---|---|---|---|
| Código oficial | A fonte já tem identificador (ex.: `EF67LP08`) | O código como publicado | É a chave primária. Nunca é reutilizado |
| Id cunhado | A fonte não tem (competência, unidade temática, objeto de conhecimento) | Slug em kebab-case com prefixo do tipo (ex.: `ef-comp-lp-prat-leitura`) | Imutável depois de publicado. Única exceção: id criado por defeito de extração, removido com mapa de substituição publicado |

O prefixo do slug carrega a hierarquia (etapa, componente, tipo de entidade). Assim o id é legível e não colide entre componentes.

## Gramática de códigos

Os códigos oficiais são **decodificáveis**: a partir do código se obtêm etapa, ano ou faixa, componente ou área e sequência. O projeto implementa essa gramática em três lugares, que precisam bater entre si:

1. uma função decodificadora no pipeline (lança erro para código malformado);
2. expressões regulares nos JSON Schemas;
3. portes da função nos pacotes npm e PyPI.

A gramática é usada **contra a própria fonte**: quando uma planilha oficial põe uma habilidade na aba errada, vale a área decodificada do código, e não a aba. Também valida combinações (um bloco de anos que não existe para certo componente é rejeitado).

Duas regras de interpretação ficam explícitas para os consumidores:

- Um código bem formado que não está nos dados **não existe**. A existência vem do dataset, não da gramática.
- A sequência é contínua dentro de cada grupo decodificado, mas não indica ordem pedagógica. Em códigos de EM, a centena é a competência, e não um salto na numeração.

## Espinha estrutural

Um arquivo separado guarda as entidades que organizam o resto: documentos curriculares, etapas, modalidades (EJA como transversal, com segmentos mapeados para etapas), áreas, componentes, recortes temporais, campos de experiência, direitos de aprendizagem, competências gerais e específicas. Os arquivos das aprendizagens só **referenciam** essas entidades por id, e a integridade referencial é checada.

## Campos transversais de todo registro normativo

### Proveniência (`fonte`)

Cada registro diz de onde veio, em dois níveis:

| Campo | Conteúdo |
|---|---|
| documento | id do documento normativo (ex.: `bncc-2018`) |
| arquivo | nome do arquivo em `fontes/` |
| proveniencia | como e quando o arquivo foi obtido |
| localizador | posição na fonte de extração (aba e linha da planilha; página do PDF) |
| localizador_pdf | página do documento homologado em que o texto foi conferido |

A separação entre "de onde extraí" e "onde conferi" é o que permite usar uma fonte mais estruturada (planilha) e provar contra a mais autoritativa (PDF homologado).

### Vigência (`vigencia`)

`{status: vigente | alterado | revogado, desde, ate}`, em que `desde` e `ate` são **versões do dataset** (`dados-AAAA.MM`), e não datas do ato. O registro nunca é apagado: revogar muda o status e preenche `ate`. O consumidor filtra por `status`.

## Multi-documento

O documento normativo é uma entidade (`documento_curricular`, com `tipo`, `esfera` e `derivado_de`). O complemento de Computação entrou como segundo documento, com organização própria (eixos, objetos de conhecimento com hierarquia pai/filho, competências próprias), sem alterar uma linha da BNCC 2018. É a prova de que o modelo aceita novos atos normativos sem migração.

## Vocabulários de referência

Além do núcleo curricular, o dataset publica dois vocabulários pequenos:

- **Marcos legais:** 20 atos (da Constituição a leis recentes) com tipo, título, ementa oficial transcrita, nota do projeto **separada** da ementa, URL oficial (o schema exige domínio gov.br) e relações tipadas com entidades do dataset.
- **Perfis:** os papéis do ecossistema escolar (professor, aluno, gestor, responsável, coordenador) com sinônimos. Serve de nomenclatura e não carrega lógica de permissão.

## O que o modelo se recusa a inventar

Fica registrado, como parte do modelo, o que **não** está no dado porque a fonte não sustenta:

- progressão formal entre habilidades de anos diferentes;
- vínculo habilidade × competência no Fundamental;
- equivalência entre objetos de conhecimento de nomes diferentes.

Esse tipo de conteúdo interpretativo vai para uma camada de anotação separada, com fonte e licença próprias, e nunca para o núcleo canônico.

## Dicionário de dados

Cada campo de cada arquivo é documentado com tipo, obrigatoriedade, significado, valores permitidos e um exemplo real, cobrindo todos os caminhos dos schemas. Mudança de schema exige atualizar o dicionário no mesmo PR.
