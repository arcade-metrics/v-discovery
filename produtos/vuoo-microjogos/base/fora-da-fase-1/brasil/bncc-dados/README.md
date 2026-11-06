# bncc-dados: análise da arquitetura e estratégia de replicação

> **Fonte:** repositório [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados), commit `9c26897` (15/10/2026), release de conteúdo `dados-2026.08`, formato `schema-v1.1.0`, DOI de conceito [10.5281/zenodo.21625233](https://doi.org/10.5281/zenodo.21625233). Complementos: [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) (`docs/arquitetura.md`, `docs/paridade.md`) e [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) (README). Mantido pela Profy Tecnologias Educacionais. Dados sob CC BY 4.0 (atribuição: "bncc.dev, mantido pela Profy"), código sob MIT. Analisado em 2026-11-04.

## Para que serve

O bncc-dados transforma um documento normativo (a BNCC, em PDF e planilhas do MEC) em **dado aberto, verificado e rastreável**, com garantias que outros produtos podem assumir. Esta pasta faz duas coisas:

1. **Analisa** como a estratégia funciona: arquitetura, modelo de dados, cadeia de confiança, governança e distribuição.
2. **Descreve como replicá-la** nas nossas próprias fontes normativas, a começar pelo CMDEB ([../cmdeb/](../../../camada-brasil/cmdeb/README.md)), que serve de piloto.

Aqui não se copia o conteúdo (habilidades, textos) nem o código do repositório. O texto é análise nossa e cita o arquivo de origem quando um ponto vem de lá. O dado da BNCC, quando um produto precisar dele, deve ser consumido da fonte (pacote, API ou release), com atribuição.

## Conteúdo

| Arquivo | O que tem |
|---|---|
| [01-arquitetura.md](01-arquitetura.md) | Camadas, fluxo do dado, organização de pastas, ecossistema de repositórios |
| [02-modelo-de-dados.md](02-modelo-de-dados.md) | Princípios de modelagem: identificadores, gramática de códigos, proveniência, vigência, multi-documento |
| [03-cadeia-de-confianca.md](03-cadeia-de-confianca.md) | Como o dado é provado: extração determinística, verificação, contratos, completude, CI |
| [04-governanca.md](04-governanca.md) | Versionamento, registro de decisões, changelog, contribuição, licenças, documentação para agentes |
| [05-distribuicao.md](05-distribuicao.md) | Pacotes, paridade entre linguagens, MCP, API, site e benchmark |
| [10-replicacao.md](10-replicacao.md) | **O playbook:** fases, artefatos mínimos, checklists, armadilhas e aplicação ao CMDEB |

## Leitura rápida

A estratégia se apoia em cinco ideias, detalhadas nos arquivos acima:

1. **A fonte oficial é imutável e fica arquivada** com hash. Todo o resto é gerado a partir dela.
2. **Nada é editado à mão.** Um pipeline determinístico (sem LLM) reproduz o dataset, e o CI reprova qualquer diferença.
3. **Cada registro prova de onde veio** (arquivo, linha ou página) e é conferido caractere a caractere contra o documento homologado.
4. **Toda ambiguidade da fonte vira uma decisão escrita**, numerada, com contexto, decisão e fonte. Não existe correção silenciosa.
5. **Dado e conveniência ficam separados.** Os dados e os pacotes são abertos para sempre; a monetização fica só em serviços sobre eles.
