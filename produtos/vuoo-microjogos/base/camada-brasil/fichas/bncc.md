# Ficha: BNCC (Base Nacional Comum Curricular)

> Frente currículo, avaliação e inclusão. Ficha **curta**: o conteúdo normativo da EI e do EF já está transcrito em [../bncc/](../bncc/README.md) e o modelo de dados de referência em [../bncc-dados/02-modelo-de-dados.md](../../fora-da-fase-1/brasil/bncc-dados/02-modelo-de-dados.md); a leitura como grafo está em `conhecimento/grafo-conhecimento-educacional/curriculum/bncc.md` (kg.curr.bncc). Aqui só o que falta para o Core. Acesso: 2026-11-05.

```yaml
id: br.bncc
name: Base Nacional Comum Curricular
acronym: BNCC
jurisdiction: Brasil (federal)
issuing_organization: Ministério da Educação; aprovada pelo Conselho Nacional de Educação (Conselho Pleno)
reference_type: norma (documento curricular de caráter normativo, instituído por resolução do CNE)
domain: [D2, D4]
official_url: https://basenacionalcomum.mec.gov.br/
repository_url: not_found (não há repositório oficial de dados); linhagem independente bncc-dev/bncc-dados, ver ../bncc-dados/
version: "EI e EF: versão homologada de 20/12/2017 (Res. CNE/CP 2/2017); EM: Res. CNE/CP 4/2018; documento integrado de 2018"
publication_date: 2017-12-22 (Res. CNE/CP 2/2017); 2018-12-17 (Res. CNE/CP 4/2018, DOU 18/12/2018)
last_updated: unknown (o portal não exibe número de versão; kg.curr.bncc)
legal_status: obrigatória como referência para currículos das redes e propostas pedagógicas (LDB art. 26 e 35-D; Res. CNE/CP 2/2017 e 4/2018)
mandatory_scope: sistemas e redes de ensino e escolas públicas e privadas de EI, EF e EM
education_levels: [EI, EF anos iniciais, EF anos finais, EM]
geographic_scope: nacional
language: pt-BR
license: unknown (documento público; licença explícita not_found). bncc-dados: CC BY 4.0
technical_formats: [PDF, planilha (XLSX) do portal, navegação HTML]
api_available: false (oficial)
data_model_available: false (oficial); sim na linhagem bncc-dados
ontology_available: false
schemas_available: false (oficial); JSON Schema em bncc-dados
implementation_examples: [../bncc/ (transcrição 2017), ../bncc-dados/, ../bncc-pacotes/]
related_standards: [br.bncc-computacao, br.novo-ensino-medio, br.dcn, br.curriculo-paulista, br.saeb]
entities: [competência geral, competência específica de área, competência específica de componente, etapa, área, componente curricular, campo de experiências, direito de aprendizagem, grupo etário, unidade temática, prática de linguagem, campo de atuação, eixo, objeto de conhecimento, habilidade, objetivo de aprendizagem e desenvolvimento]
relationships: [habilidade → objeto de conhecimento (n:n na linha do quadro), objeto → unidade temática, habilidade → ano ou bloco de anos, habilidade EM → competência específica (no código), objetivo EI → campo × grupo etário]
vocabularies: [gramática de códigos EI/EF/EM, ver terminologia-curriculo-avaliacao-inclusao.md §1]
core_relevance: alta: é o C.CFW de referência nacional; testa o Core com estruturas diferentes por etapa
regional_adapter_relevance: alta: chave de alinhamento de currículo estadual, avaliação (Saeb, SARESP) e PEI
limitations: [sem pré-requisitos, sem vínculo habilidade-competência no EF, códigos impressos em duplicidade (EF05LP25, EF04LP27), textos que mudaram entre 2017 e 2018 sem mudar o código]
open_questions: [Q-CUR-01, Q-CUR-02, Q-CUR-03 em questoes-abertas-curriculo-avaliacao-inclusao.md]
sources: [E-01, E-02, E-03, E-04 em evidencias-curriculo-avaliacao-inclusao.md]
access_date: 2026-11-05
research_status: verificado (EI/EF por transcrição própria; EM por linhagem bncc-dados e atos do CNE)
```

## Análise técnica (§6.3), só o que acrescenta

| Item | Situação | Onde |
|---|---|---|
| Entidades e atributos | Estrutura assimétrica por etapa: EI (objetivo × campo × grupo etário), EF (habilidade × unidade temática/prática × objeto × ano/bloco), EM (habilidade × área × competência; LP como componente) | [../bncc-dados/02-modelo-de-dados.md](../../fora-da-fase-1/brasil/bncc-dados/02-modelo-de-dados.md) |
| Identificador primário | Código oficial impresso (`EF67LP08`); entidades sem código recebem id cunhado | idem |
| Gramática | Decodificável; tabela em [terminologia §1](../terminologia-curriculo-avaliacao-inclusao.md) | [../bncc-pacotes/02-api-e-modelo.md](../../fora-da-fase-1/brasil/bncc-pacotes/02-api-e-modelo.md) |
| Temporalidade | Dois textos para o mesmo código: 2017 e 2018 diferem em 9 textos de habilidade e 8 objetos de conhecimento do EF, com código igual | [../bncc/99-verificacao.md](../bncc/99-verificacao.md) |
| Unicidade | O código **não** é chave única no texto de 2017: 2 códigos impressos duas vezes com textos diferentes | [../bncc/98-decisoes.md](../bncc/98-decisoes.md), decisão 2 |
| Ordem | Número sequencial não é ordem pedagógica; no EM a centena é a competência | [../bncc-pacotes/02-api-e-modelo.md](../../fora-da-fase-1/brasil/bncc-pacotes/02-api-e-modelo.md) |
| Extensão | Complementos entram como novo documento (Computação, 2022) sem alterar a BNCC | [bncc-computacao.md](bncc-computacao.md) |
| Serialização, API, autenticação, conformidade | Não há oficiais | not_found |

## Consequências para o Core [I]

1. `C.CMP` precisa de identidade **separada do código**: o par (documento, versão do texto, código) identifica o enunciado; o código sozinho não basta (duplicidade de 2017, textos diferentes 2017×2018). Isso confirma a recomendação de kg.curr.bncc de usar o código como `notation`, não como IRI.
2. `C.CFW` precisa de versão de **texto** (edição do documento) distinta da versão do **ato** (resolução) e da **versão do dataset** (bncc-dados usa `dados-AAAA.MM`).
3. A hierarquia não é uniforme: o Core deve aceitar níveis organizadores tipados (campo de experiências, unidade temática, prática de linguagem, campo de atuação, eixo, área), sem nível obrigatório.
