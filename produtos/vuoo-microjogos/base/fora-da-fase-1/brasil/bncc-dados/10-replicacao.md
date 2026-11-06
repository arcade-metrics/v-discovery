# Playbook de replicação

> **Fonte:** síntese própria a partir da análise de [01](01-arquitetura.md) a [05](05-distribuicao.md) (bncc-dados, commit `9c26897`, release `dados-2026.08`). O piloto usa o nosso [../cmdeb/](../../../camada-brasil/cmdeb/README.md) (Portaria MEC nº 832/2025, <https://mecnormas.mec.gov.br/pesquisa/detalhar/8017>). Escrito em 2026-11-04.

Como transformar **qualquer fonte normativa** (portaria, resolução, parecer, dicionário de dados oficial, base curricular) num dataset aberto, verificado e rastreável, com a mesma estratégia do bncc-dados.

## Quando vale aplicar

A estratégia custa caro (pipeline, CI, governança). Ela compensa quando a fonte atende a pelo menos três destes critérios:

- é **oficial e citável** (MEC, CNE, INEP, DOU);
- tem **identificadores ou estrutura repetitiva** (códigos, variáveis, tabelas);
- vai ser **consumida por máquina** (produto, integração, agente de IA);
- **muda com o tempo** (portaria que altera portaria, resolução nova);
- um erro de transcrição tem **custo real** (dado de aluno, conformidade legal, conteúdo pedagógico).

Para fonte lida uma vez, só por gente, basta a mineração em `.md` desta pasta `PRD/`.

---

## Fase 0: escopo e caso âncora

Antes de extrair, defina:

| Item | Pergunta | Saída |
|---|---|---|
| Caso âncora | Quais 10 a 15 perguntas concretas o produto vai fazer a esse dado? | Lista de consultas, que vira teste de aceitação (ver Fase 5) |
| Consumidores | Quem lê: app, agente, analista, pesquisa? | Define os formatos da Fase 8 |
| Fronteira do núcleo | O que é texto ou estrutura oficial e o que é interpretação nossa? | Regra escrita: interpretação vai para uma camada separada |
| Licença | O texto oficial é livre (Lei 9.610/98, art. 8º, IV). E a nossa curadoria? E o material de apoio? | Licença dos dados, licença do código, compromisso aberto/comercial |
| Dado pessoal | A fonte ou os exemplos podem conter dados de pessoas? | Regra de exclusão e canal privado de reporte |

## Fase 1: fontes

1. Obter **todas** as versões da fonte: a usada para extrair (a mais estruturada: planilha, JSON de API) e a **homologada**, usada para verificar (normalmente o PDF ou a publicação no DOU).
2. Arquivar cada arquivo **intocado**, com data de obtenção e SHA-256, numa tabela em `fontes/README.md`.
3. Escrever as notas de proveniência: de onde veio, se o serviço é instável, que versões erradas circulam, que normalização técnica é necessária (e que essa normalização é passo do pipeline, nunca da fonte).
4. Declarar a **hierarquia**: qual fonte prevalece quando divergem.
5. Para material de terceiros sem licença de redistribuição, não versionar o arquivo. Registrar nome e hash e, se precisar da estrutura, gerar uma vez um mapa próprio, que também é verificado contra a fonte oficial.

> **Atenção (regra desta pasta):** baixar fontes (PDF, planilha, JSON de API) para o repositório é um download e precisa de discussão antes.

## Fase 2: modelo

| Decisão | Regra |
|---|---|
| Entidades | Uma por tipo real da fonte. Não unificar tipos diferentes com campos nulos |
| Chave | Código oficial quando existe; slug cunhado e prefixado quando não existe |
| Gramática | Se o identificador é decodificável, escrever o decodificador **antes** do extrator; usar a gramática para corrigir a posição na fonte |
| Espinha | Entidades organizadoras num arquivo próprio; o resto só referencia por id |
| `fonte` em todo registro | documento, arquivo, proveniência, localizador na fonte de extração, localizador no homologado |
| `vigencia` em todo registro | status (vigente, alterado, revogado), desde e até, em data-version |
| Multi-documento | O ato normativo é entidade; ato que altera ou complementa entra ligado por `derivado_de` |
| Schema | JSON Schema fechado por arquivo, com tipos compartilhados (padrões de código, slug, fonte, vigência) |
| Recusas | Lista escrita do que o modelo **não** infere |

## Fase 3: extração

- Um script por tipo de fonte, determinístico, **sem LLM** e com o mínimo de dependências.
- Um mapa de **correções explícitas** dentro do extrator (identificador → trecho da fonte → trecho do homologado), cada uma citando o número da decisão.
- Tratar os artefatos de layout como regra: linha de continuação, nota de rodapé na célula, hífen de quebra, ligaduras, células mescladas, marcador de "(continuação)".
- Saída ordenada e estável (mesma entrada, mesmos bytes).

## Fase 4: verificação

- Para cada registro: localizar no homologado, comparar depois de uma normalização **declarada** e gravar a página.
- Detectar truncamento: o homologado continua a frase depois do fim do nosso texto?
- Match aproximado **nunca aprova sozinho**. Ele só vira ok com exceção registrada (registro, página, motivo).
- Verificar **todo** texto que vem da fonte, não só a entidade principal (nomes de grupos, competências, rótulos de domínio).
- Excluir páginas que repetem o texto como exemplo.
- Gravar o resultado por registro num arquivo versionado (`verificacao.json`).

## Fase 5: contratos

Um script, com código de saída, cobrindo as famílias abaixo:

- [ ] gramática: todo identificador decodifica
- [ ] contagens-gabarito: total e distribuição fixados no código
- [ ] integridade referencial
- [ ] regras estruturais do domínio
- [ ] unicidade e continuidade de sequência
- [ ] qualidade de nomes (sem pedaços de quebra de linha, notas ou hífens)
- [ ] verificação: todos ok, nenhum localizador proibido
- [ ] **completude por varredura**: os identificadores encontrados no homologado inteiro são iguais aos do dataset
- [ ] schema com **autoteste negativo** (corrupções de propósito precisam ser rejeitadas)
- [ ] consultas do caso âncora executadas e registradas no relatório

## Fase 6: derivados e CI

- Gerar SQLite e CSV do canônico, com tabela de metadados (versão, hashes das fontes).
- Comparar o SQLite por dump lógico, não por bytes.
- O CI, em todo push e PR, faz: instalar só o declarado → extrair → verificar → validar schema → validar contratos → derivar → `git diff --exit-code`.

## Fase 7: governança mínima

| Arquivo | Conteúdo mínimo |
|---|---|
| `README.md` | O que é, uso rápido, por que confiar (com números), formas de acesso, licenças, quem mantém |
| `DECISOES.md` | Entradas numeradas: contexto → decisão → fonte; revisões preservadas |
| `CHANGELOG.md` | Por release; categorias `normativa`, `correcao`, `schema`, `editorial` |
| `docs/modelo-de-dados.md` | Entidades, identificadores, gramática, recusas |
| `docs/dicionario-de-dados.md` | Cada campo: tipo, obrigatoriedade, significado, valores, exemplo |
| `docs/metodologia.md` | Os elos da cadeia de confiança, com os resultados atuais |
| `docs/versionamento.md` | Duas trilhas, regras de ciclo de vida, taxonomia de eventos, processo de release |
| `docs/politica-de-conteudo.md` | O que é distribuído, o que é problema, como reportar, prazos |
| `CONTRIBUTING.md` + templates de issue e PR | Correção exige fonte oficial; checklist do PR |
| `AGENTS.md` + `llms.txt` | Regras anti-invenção, mapa do domínio, como rodar o pipeline |
| `CITATION.cff` | Metadado de citação e fonte única da versão |
| Licenças | Dados (ex.: CC BY 4.0) e código (ex.: MIT), com nota de titularidade |

## Fase 8: distribuição, em degraus

Só avance de degrau quando o anterior estiver estável:

1. Arquivos canônicos e derivados no repositório, com release e tag.
2. Arquivamento com DOI (Zenodo), se houver público acadêmico.
3. Pacote com o dado embutido e pinado (arquivo de versão com commit e checksums) e núcleo de consulta injetável.
4. Servidor MCP como casca fina sobre o pacote: poucas ferramentas, respostas com limite e total, fonte em todo registro, erros que explicam.
5. Segunda linguagem só com fixture de paridade compartilhada.
6. Site e API hospedada, em repositórios próprios.
7. Benchmark de alucinação, se o valor do dataset precisar ser demonstrado.

## Fase 9: auditoria independente

Antes de chamar a release de estável:

- alguém que não escreveu o pipeline confere, por dois métodos determinísticos diferentes e por leitura visual de uma amostra (ou de tudo, se o volume permitir);
- cada falha encontrada vira correção **e** contrato novo;
- o resultado entra no registro de decisões.

## Critério de pronto (primeira release)

- [ ] CI verde reproduzindo o dataset do zero
- [ ] 100% dos registros com status ok e página no homologado
- [ ] completude por varredura sem faltas nem sobras
- [ ] autoteste negativo passando
- [ ] toda divergência da fonte registrada em `DECISOES.md`
- [ ] dicionário cobrindo 100% dos caminhos do schema
- [ ] caso âncora respondido pelo dado
- [ ] licença e atribuição definidas

## Armadilhas (vistas no bncc-dados)

| Armadilha | Prevenção |
|---|---|
| Verificar só prefixo | Checar a continuação no homologado |
| Fallback aproximado que aprova | Fallback só sinaliza |
| Decisão escrita e não aplicada | Correções vivem no extrator, não no texto |
| Verificar só a entidade principal | Verificar todo texto oriundo da fonte |
| Usar o primeiro match | Excluir páginas ilustrativas e checar por contrato |
| Off-by-one ao contar páginas | Contrato sobre o número de páginas |
| Afirmação na documentação sem teste ("a numeração tem lacunas") | Toda afirmação sobre o dado vira contrato |
| Material de apoio sem licença | Mapa próprio verificado no lugar do arquivo |
| Metadado pessoal escondido em arquivo de fonte | Inspecionar os metadados dos arquivos antes de versionar |
| Versão errada da fonte circulando | Notas de proveniência e hash do arquivo certo |

---

## Aplicação piloto: CMDEB

O CMDEB (Anexo da Portaria MEC nº 832/2025) já foi minerado em `.md` ([../cmdeb/](../../../camada-brasil/cmdeb/README.md)). Esta seção mapeia cada peça da estratégia para ele e mostra o que a análise já revelou.

### Mapeamento

| Conceito | No CMDEB |
|---|---|
| Fonte de extração | JSON da API do MEC Normas (`/pesquisa/api/atos/8017`), com o texto segmentado e as tabelas do Anexo |
| Fonte homologada | Publicação no DOU de 17/12/2025 |
| Documento normativo | `portaria-mec-832-2025`, que altera `portaria-mec-234-2025` (ligação `altera`, análoga a `derivado_de`) |
| Entidade principal | Variável do modelo de informação (156 linhas, 4 blocos) |
| Chave oficial | Nome técnico da variável (`ESTUDANTE_CPF`), mas **não é único**: ver achados |
| Espinha | Blocos e seções (1 Estudante; 2.1 a 2.5 Trajetória; 3 Profissionais e subseções; 4 Instituições), categorias (Referência, Registro, Situacional, Complementar), ocorrências |
| Vocabulários | Os domínios de código (sexo, raça/cor, deficiência, etapa de ensino, situação de matrícula…), cada um como entidade com seus valores |
| Vigência | Essencial: o art. 14, § 4º, prevê atualização do CMDEB por ato do Ministro |
| Caso âncora (exemplos) | "Quais variáveis são obrigatórias para o estudante?"; "Qual o código de etapa para o 6º ano?"; "Quais campos são dado pessoal sensível?"; "Que variáveis ligam turma a componente curricular?" |

### Achados que já seriam entradas de `DECISOES.md`

Levantados por script sobre as tabelas mineradas:

| # | Achado | Decisão a tomar |
|---|---|---|
| 1 | **156 linhas, 134 variáveis distintas**: 12 nomes se repetem entre seções (ex.: `CO_ENTIDADE` em 3 blocos, `ID_SGP_COMPONENTE_CURRICULAR` em 3 seções) | A chave passa a ser (seção, variável). As repetições são referências (chaves estrangeiras) entre blocos, e não duplicatas |
| 2 | **Tipo divergente para a mesma variável**: `ID_SGP_COMPONENTE_CURRICULAR` aparece como Alfanumérico e como Numérico; `NOME_TURMA`, como Alfanumérico e Numérico; `NO_ENTIDADE`, como Alfanumérico e Alfabético | Registrar a divergência por ocorrência, sem unificar em silêncio; consultar o DOU para ver se a divergência é da norma ou da transcrição do MEC Normas |
| 3 | **18 linhas (16 nomes distintos) com espaço espúrio no nome técnico** (ex.: `TURMA_ORGANIZACAO_QUANTIDADE_ TOTAL`) | Canonizar sem o espaço (gramática `^[A-Z0-9_]+$`) e guardar a forma impressa no localizador, como o bncc-dados fez com o código `EF05CO011` |
| 4 | A ocorrência `[0..n]` é definida no método, mas **nenhuma linha a usa** | Registrar; o contrato aceita os 4 valores e conta o uso real (88 `[1..1]`, 56 `[0..1]`, 12 `[1..n]`) |
| 5 | **Códigos de domínio não sequenciais** (etapa: 1, 2, 14 a 21, 41, 25 a 29, 35…; situação de matrícula: 0 a 12, 19, 21 a 23) | O código é o identificador oficial; um código ausente não existe (mesma regra do bncc-dados) |
| 6 | Na fonte, linhas de continuação partem os domínios longos | A regra de junção vira parte do extrator, com contrato de que nenhum valor de domínio fica órfão |
| 7 | A finalidade do tratamento de dados remete ao art. 4º da Portaria 234/2025, que não está nesta portaria | Ligar o documento 234/2025 (fonte a arquivar) ou registrar a lacuna |

### Contratos iniciais do CMDEB

- 156 linhas; por bloco 29 / 63 / 47 / 17; por categoria 82 Registro / 55 Complementar / 17 Referência / 2 Situacional.
- Toda ocorrência casa com `^\[[01]\.\.[1n]\]$`; toda variável canonizada casa com `^[A-Z0-9_]+$`.
- Todo tipo pertence ao conjunto fechado observado (Numérico, Código, Alfanumérico, Data, Alfabético, Alfanumérico com @, Alfanumérico com caracteres especiais).
- Toda variável de tipo Código tem domínio com pelo menos 2 valores, e os códigos são únicos dentro do domínio.
- Toda variável repetida entre seções tem o mesmo nome do dado ou uma divergência registrada.
- Completude por varredura: o número de linhas de dado no texto do DOU é igual ao do dataset.

### O que falta para o piloto virar dataset

1. **Arquivar as fontes** (JSON da API e publicação do DOU) com hash. É download, então precisa de aprovação.
2. Escrever o modelo em JSON Schema (variável, seção, domínio, valor de domínio, documento).
3. Portar o script de geração (hoje no scratchpad da sessão) para um `pipeline/` versionado, com saída JSON canônica; os `.md` atuais passariam a ser derivados.
4. Verificar contra o DOU e resolver os achados 2 e 7.
5. Montar o `DECISOES.md` com os 7 achados acima.

## Decisões em aberto para nós

| Decisão | Opções |
|---|---|
| Onde vive o dataset replicado | Repositório próprio (como o bncc-dados) ou pasta dentro do discovery. O padrão do bncc-dados recomenda repositório próprio, porque o dado envelhece em ritmo diferente do produto |
| Formato canônico × regra "tudo em `.md`" desta pasta | Manter `PRD/` como mineração em `.md` e o dataset canônico (JSON + schema) no repositório próprio, gerando os `.md` como derivados |
| Arquivamento de fontes | Exige download de PDF e JSON; decidir caso a caso |
| Licença da nossa curadoria | CC BY 4.0 (como o bncc-dados) ou outra |
| Abertura | Público desde o início ou interno até a primeira auditoria |
| Reuso da BNCC | Consumir o bncc-dados (pacote, API ou MCP) com atribuição, e não replicar o dado dele; cruzamentos com o CMDEB (área, etapa, componente) iriam para uma camada de anotação nossa |
| Próximas fontes candidatas | Portaria MEC 234/2025 (a alterada), Portaria MEC 421/2026 (acessibilidade, já citada no histórico do repositório) e outros dicionários de dados oficiais do MEC e do INEP |
