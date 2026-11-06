# Ficha: Compromisso Nacional Criança Alfabetizada e Indicador Criança Alfabetizada

> Acesso: 2026-11-05.

```yaml
id: br.cnca
name: Compromisso Nacional Criança Alfabetizada
acronym: CNCA
jurisdiction: Brasil (federal, por adesão de estados e municípios)
issuing_organization: Presidência da República (Decreto 11.556/2023); MEC; Inep
reference_type: [decreto (política pública), indicador]
domain: [D5]
official_url:
  - https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/D11556.htm
  - https://agenciagov.ebc.com.br/noticias/202507/58-dos-municipios-melhoraram-alfabetizacao (agência oficial, para o ponto de corte)
repository_url: not_found
version: "Decreto 11.556, de 12/06/2023"
publication_date: 2023-06-12
last_updated: unknown
legal_status: decreto em vigor (alterações não verificadas)
mandatory_scope: entes que aderirem (art. 32 obriga quem aderir e não tiver avaliação anual a instituí-la)
education_levels: [EF 1º e 2º anos (alfabetização até o fim do 2º ano, art. 5)]
geographic_scope: nacional
language: pt-BR
license: domínio público [I]
technical_formats: [HTML]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: [avaliações estaduais anuais do 2º ano que alimentam o indicador]
related_standards: [br.saeb, br.sp.saresp]
entities: [avaliação de leitura da escola, avaliação estadual anual, Saeb, padrão de alfabetização (ponto de corte), indicador criança alfabetizada]
relationships: [Inep define diretrizes de complementaridade Saeb × sistemas estaduais (art. 31); MEC com Inep define o nível de alfabetizado (art. 33)]
vocabularies: ["padrão nacional de alfabetização: 743 pontos na escala Saeb do 2º ano (Pesquisa Alfabetiza Brasil, Inep, 2023, segundo a Agência Gov)"]
core_relevance: média: exemplo de **ponto de corte binário** sobre escala contínua, usado como indicador oficial
regional_adapter_relevance: alta (avaliações estaduais de alfabetização usam itens/escala do Inep)
limitations: [ponto de corte verificado em agência oficial de notícias, não no ato do MEC/Inep que o fixa]
open_questions: [Q-AVA-07]
sources: [E-25, E-26]
access_date: 2026-11-05
research_status: parcial
```

## Para o modelo [I]

O "alfabetizado" é uma classificação derivada (binária) de uma proficiência na escala do 2º ano, distinta dos níveis descritivos da mesma escala (Abaixo de 1 a 8). Mais um caso de múltiplos esquemas de corte sobre o mesmo resultado (ver saeb.md e saresp.md). Para o PEI paulista, a "proficiência em leitura e escrita" é registrada em **hipóteses de escrita** (pré-silábico a alfabético), outro vocabulário, qualitativo, sobre o mesmo construto.
