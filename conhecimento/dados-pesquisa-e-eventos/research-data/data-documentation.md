---
id: dat.rd.data-documentation
titulo: Documentação de dataset (datasheets, dicionário de dados, codebook, README)
tipo: comparacao
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [gebru2021datasheets, holland2018nutrition, bender2018datastatements, ddi2014codebook25, ddi2020lifecycle33, cornell2026readme, dataverse2026datasetmgmt, datacite2026schema47, wilkinson2016fair, scienceeurope2021rdmguide]
relacoes:
  - { tipo: depende-de, alvo: dat.rd.fair-principles }
  - { tipo: complementa, alvo: dat.rd.repositories-and-versioning }
  - { tipo: complementa, alvo: dat.rd.data-management-plans }
  - { tipo: complementa, alvo: dat.ds.comparison }
  - { tipo: complementa, alvo: kg.std.prov-o }
  - { tipo: complementa, alvo: lae.dq.provenance-and-lineage }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: dat.ethics.consent-and-assent-in-research }
termos: [datasheet for datasets, dataset nutrition label, data statement, dicionário de dados, codebook, DDI-Codebook, DDI-Lifecycle, README de dataset, metadados de citação, documentação de proveniência]
---

# Documentação de dataset (datasheets, dicionário de dados, codebook, README)

## Definição e terminologia

**Documentação de dataset** é o conjunto de textos e metadados que permite a outra pessoa, ou ao próprio autor tempos depois, interpretar e reusar corretamente os dados. Distinguem-se aqui cinco formas [I]:

- **Datasheet for datasets**: questionário em prosa sobre motivação, composição, coleta, pré-processamento, usos, distribuição e manutenção [F: gebru2021datasheets, §3].
- **Dataset Nutrition Label**: painel modular, parte qualitativo e parte gerado automaticamente, com uma visão geral dos "ingredients" do dataset [F: holland2018nutrition, Abstract].
- **Data statement**: caracterização de dataset linguístico que permite entender "how experimental results might generalize, how software might be appropriately deployed, and what biases might be reflected" [F: bender2018datastatements, §1].
- **Codebook / dicionário de dados**: descrição variável a variável; o DDI-Codebook é a versão leve do padrão DDI, "intended primarily to document simple survey data" [F: ddi2014codebook25].
- **README de dataset**: arquivo de texto simples que acompanha os arquivos; a Cornell Data Services o recomenda quando não há padrão de metadados apropriado [F: cornell2026readme].

O que a documentação não é: não substitui os metadados de citação do repositório (DataCite), que servem à descoberta (F2, F4), nem o PGD, que é um plano e não descreve o dataset final [I].

## Problema que resolve

Gebru et al. notam que não havia "standardized process for documenting machine learning datasets" e propõem que cada dataset tenha uma datasheet, por analogia com componentes eletrônicos [F: gebru2021datasheets, §1]. O princípio FAIR R1 exige metadados ricos com "a plurality of accurate and relevant attributes", e R1.2 exige proveniência detalhada [F: wilkinson2016fair, Box 2]. A Science Europe pede no PGD a descrição de metodologia de coleta, forma de organização e controle de qualidade [F: scienceeurope2021rdmguide, 2a-2b]. Para dados de interação educacional, a documentação é o que permite a outro pesquisador saber o que cada evento mede, em que relógio e com que perdas [I].

## Fundamentos e funcionamento

### Datasheets for Datasets

As perguntas seguem as etapas do ciclo de vida, foram refinadas durante cerca de dois anos com equipes de produto e revisão jurídica, e "are not intended to be prescriptive" [F: gebru2021datasheets, §1-§3]. Os autores afirmam que o processo "is not intended to be automated", porque automatizar contraria o objetivo de reflexão do criador [F: gebru2021datasheets, §1]. Para dados sobre pessoas, a seção de composição pergunta se o dataset identifica subpopulações (por exemplo, por idade), se é possível identificar indivíduos "either directly or indirectly (i.e., in combination with other data)" e se contém dados sensíveis [F: gebru2021datasheets, §3.2]. A seção de coleta pergunta se os indivíduos foram notificados, se consentiram (reproduzindo a linguagem exata), se há mecanismo para revogar o consentimento e se foi feita análise de impacto sobre os titulares [F: gebru2021datasheets, §3.3]. A seção de manutenção pergunta sobre limites de retenção prometidos aos titulares e sobre suporte a versões antigas [F: gebru2021datasheets, §3.7]. Por decisão após revisão jurídica, perguntas sobre conformidade regulatória foram trocadas por perguntas factuais [F: gebru2021datasheets, §2].

### Dataset Nutrition Label

O protótipo de 2018 tem sete módulos: Metadata (o único obrigatório), Provenance, Variables, Statistics, Pair Plots, Probabilistic Model e Ground Truth Correlations [F: holland2018nutrition, Table 1]. Os autores notam que alguns módulos podem servir de "proxies" sem expor os dados, enquanto outros, como distribuições, "would allow adversaries to approximate the dataset contents", e que a escolha de módulos depende de "privacy concerns" [F: holland2018nutrition, §2.1]. Entre módulos futuros listam um focado em privacidade, que indique informação sensível e se houve consentimento [F: holland2018nutrition, §2.1]. O documento traz no cabeçalho "DRAFT MAY 2018" e foi publicado como pré-print no arXiv [F: holland2018nutrition, p. 1].

### Data statements

O esquema proposto tem, na forma longa: curation rationale, language variety (com etiqueta BCP-47), speaker demographic, annotator demographic, speech situation, text characteristics, recording quality, other e provenance appendix; a forma curta, de 60 a 100 palavras, aponta para a longa [F: bender2018datastatements, §5]. Os autores reconhecem a tensão entre detalhe e privacidade: considerações sobre "the privacy of the people involved (speakers, annotators) might preclude including certain kinds of information, especially with small groups" [F: bender2018datastatements, §4]. Gebru et al. sugerem integrar essas perguntas numa datasheet de dataset linguístico [F: gebru2021datasheets, §1].

### DDI

A DDI Alliance mantém dois produtos principais: DDI-Codebook 2.5 (com revisão 2.5.1 de 29/01/2014, sem mudança de namespace) e DDI-Lifecycle 3.3, publicado em 15/04/2020, que acrescenta, entre outros, coleta de dados não baseada em survey (Measurements) e gestão de classificações [F: ddi2014codebook25; ddi2020lifecycle33]. A página da Alliance informa que o conjunto de produtos DDI foi reconhecido como norma internacional na ISO/PAS 25955:2026 [F: ddi2014codebook25]. O Dataverse exporta metadados de datasets publicados em "DDI (Data Documentation Initiative Codebook 2.5)", além de DataCite 4, Dublin Core, Schema.org JSON-LD e Croissant [F: dataverse2026datasetmgmt, Supported Metadata Export Formats].

### README de dataset

A Cornell Data Services recomenda texto simples, um README por agrupamento lógico de arquivos, datas em ISO 8601 e vocabulários padronizados [F: cornell2026readme]. O conteúdo sugerido cobre informação geral (responsáveis, datas e local de coleta, financiamento), compartilhamento e acesso (licenças ou restrições, citação recomendada, links), visão dos arquivos (descrição, relações, histórico de versões), metodologia (coleta, processamento, software com versões, controle de qualidade) e informação específica por arquivo (número de variáveis e de linhas, lista de variáveis com definições, códigos de dado ausente) [F: cornell2026readme].

## Alternativas e comparações

| Critério | Datasheet | Nutrition Label | Data statement | DDI-Codebook | README (Cornell) |
|---|---|---|---|---|---|
| Forma | prosa por perguntas | módulos visuais | prosa, longa e curta | XML legível por máquina | texto simples |
| Automação | deliberadamente manual | parte automática | manual | gerável por ferramenta | manual |
| Nível de variável | não é o foco | Variables, Statistics | não | sim | sim |
| Consentimento e titulares | perguntas explícitas | módulo futuro | permissão de falantes | não verificado | não |
| Risco de privacidade da própria documentação | perguntas sobre identificação | reconhecido (distribuições) | reconhecido (grupos pequenos) | não verificado | não tratado |

Fontes da tabela: [F: gebru2021datasheets; holland2018nutrition; bender2018datastatements; ddi2014codebook25; cornell2026readme].

As formas se combinam: DataCite para citação e descoberta [F: datacite2026schema47], README e dicionário (ou DDI) para interpretação, datasheet para contexto ético e de uso [I].

## Vantagens e limitações

Datasheets tornam explícitos consentimento, subpopulações e possibilidade de identificação, o que é central para dados de crianças; custam tempo e não são legíveis por máquina [F: gebru2021datasheets; I]. O nutrition label agiliza a triagem, mas estatísticas descritivas publicadas podem vazar informação [F: holland2018nutrition, §2.1]. Em datasets de menores com acesso restrito, a documentação pública deve ser agregada e passar pela mesma avaliação de risco de reidentificação que os dados (ver `psg.deid.reidentification-risk`) [I].

## Exemplo técnico independente de domínio

```
README.txt (publico)
  titulo, DOI, versao 1.1 (2026-03-01), licenca/termos de acesso, citacao
  responsaveis, financiamento, periodo de coleta (mes/ano), local: "escolas publicas, estado X"
  arquivos: events.parquet (restrito), variables.csv (publico), datasheet.md (publico)
  metodos: instrumentacao, relogio (UTC, monotono por sessao), pseudonimizacao, perdas conhecidas
variables.csv (publico; formato tipo codebook)
  nome, tipo, unidade, dominio, codigo_ausente, definicao
datasheet.md (publico)
  composicao: faixas etarias agregadas; possibilidade de identificacao indireta e mitigacao
  coleta: TCLE/TALE aprovados (sem nomes de escolas); mecanismo de retirada; analise de impacto
  manutencao: retencao prometida, politica de versoes, contato do curador
```

## Relações com outros conceitos

Atende a R1 e R1.2 de `dat.rd.fair-principles`, é depositada junto com os dados em `dat.rd.repositories-and-versioning` e prevista no item a do PGD (`dat.rd.data-management-plans`). A comparação de documentação de datasets públicos de educação fica em `dat.ds.comparison`. A proveniência pode ser expressa com `kg.std.prov-o` e `lae.dq.provenance-and-lineage`; o que se informa sobre consentimento depende de `dat.ethics.consent-and-assent-in-research`.

## Lacunas e questões abertas

- O texto lido de Gebru et al. foi a versão 8 do arXiv (dez. 2021); a versão da Communications of the ACM foi confirmada só por metadados do Crossref.
- A documentação técnica dos elementos de DDI-Codebook 2.5 (por exemplo, como registrar restrições de acesso) não foi aberta.
- Não há, nas fontes consultadas, modelo de datasheet específico para dados de interação educacional de crianças; o exemplo acima é síntese deste documento.
- O guia de README da Cornell não traz data de atualização visível.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| gebru2021datasheets | academico | 2026-10-30 |
| holland2018nutrition | academico (pré-print) | 2026-10-30 |
| bender2018datastatements | academico | 2026-10-30 |
| ddi2014codebook25 | normativo | 2026-10-30 |
| ddi2020lifecycle33 | normativo | 2026-10-30 |
| cornell2026readme | tecnico | 2026-10-30 |
| dataverse2026datasetmgmt | fornecedor | 2026-10-30 |
| datacite2026schema47 | normativo | 2026-10-30 |
| wilkinson2016fair | academico | 2026-10-30 |
| scienceeurope2021rdmguide | tecnico | 2026-10-30 |
