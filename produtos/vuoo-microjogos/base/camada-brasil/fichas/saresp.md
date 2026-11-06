# Ficha: SARESP (Sistema de Avaliação de Rendimento Escolar do Estado de São Paulo)

> Caso de avaliação estadual. A página oficial `educacao.sp.gov.br/saresp` respondeu 403 ao acesso automatizado em 2026-11-05. Os cortes de nível vêm do *Relatório Pedagógico SARESP 2014 – Língua Portuguesa* (documento oficial da Seduc-SP, ISSN 2236-8574), obtido de cópia hospedada no site da FEP/IF-USP; a edição 2025 só foi vista por imprensa. Acesso: 2026-11-05.

```yaml
id: br.sp.saresp
name: Sistema de Avaliação de Rendimento Escolar do Estado de São Paulo
acronym: SARESP
jurisdiction: Estado de São Paulo
issuing_organization: Secretaria da Educação do Estado de São Paulo
reference_type: programa de avaliação externa estadual
domain: [D5, D2]
official_url:
  - https://www.educacao.sp.gov.br/saresp/ (403 em 2026-11-05)
  - https://fep.if.usp.br/~profis/arquivo/avaliacao/saresp/RP_LP_2014_online.pdf (cópia de terceiro do relatório oficial)
repository_url: not_found
version: "cortes verificados: edição 2014; edição vigente (2025) não verificada em fonte oficial"
publication_date: 2014 (relatório usado)
last_updated: 2026-02 (divulgação do SARESP 2025, segundo imprensa)
legal_status: programa da rede estadual; base normativa (resolução anual) not_found nesta sessão
mandatory_scope: rede estadual de SP; adesão de redes municipais (não verificado)
education_levels: ["2014: 3º, 5º, 7º, 9º EF e 3ª EM (LP e MT); 2025: 2º, 5º, 9º EF e EM segundo imprensa"]
geographic_scope: SP
language: pt-BR
license: unknown
technical_formats: [PDF]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: [Idesp (indicador estadual; não verificado nesta sessão)]
related_standards: [br.saeb (mesma escala), br.sp.curriculo-paulista]
entities: [nível de proficiência, classificação agregada (Insuficiente/Suficiente/Avançado), escala de desempenho, matriz de referência (2009, ligada ao currículo estadual de 2010), redação com escala própria]
relationships: [nível → intervalo da escala Saeb por ano/série; classificação → agrupamento de níveis]
vocabularies: ["4 níveis: Abaixo do Básico, Básico, Adequado, Avançado; 3 classificações: Insuficiente, Suficiente, Avançado"]
core_relevance: alta: mostra que o mesmo C.RES numérico recebe **dois** rótulos de nível (Saeb 0..10 e SARESP 4 níveis) e um terceiro agrupamento
regional_adapter_relevance: alta (prioridade SP)
limitations: [cortes e matriz vigentes não confirmados; relação atual com o Currículo Paulista não verificada]
open_questions: [Q-AVA-05, Q-AVA-06]
sources: [E-23, E-24]
access_date: 2026-11-05
research_status: parcial
```

## Análise técnica

**Escala**: o relatório de 2014 apresenta os resultados de LP e MT "na mesma escala de desempenho da Prova Brasil/Saeb", com TRI em todos os anos/séries, e informa que o 3º ano foi incluído "na mesma escala dos demais… ancorada no Saeb, após devida equalização" (RP LP 2014, apresentação).

**Níveis de LP (Quadro 2, RP LP 2014)**:

| Nível | 3º EF | 5º EF | 7º EF | 9º EF | 3ª EM |
|---|---|---|---|---|---|
| Abaixo do Básico | < 125 | < 150 | < 175 | < 200 | < 250 |
| Básico | 125 a < 175 | 150 a < 200 | 175 a < 225 | 200 a < 275 | 250 a < 300 |
| Adequado | 175 a < 225 | 200 a < 250 | 225 a < 275 | 275 a < 325 | 300 a < 375 |
| Avançado | ≥ 225 | ≥ 250 | ≥ 275 | ≥ 325 | ≥ 375 |

Classificação agregada (Quadro 1): **Insuficiente** = Abaixo do Básico; **Suficiente** = Básico e Adequado; **Avançado** = Avançado. Descrições: Básico = "domínio mínimo… mas possuem as estruturas necessárias para interagir com a proposta curricular no ano/série subsequente"; Adequado = "domínio pleno… desejáveis para o ano/série". Redação tem escala própria por nota (Abaixo do Básico < 50; Básico 50 a < 65; …).

Os cortes de Matemática não foram verificados nesta sessão (Q-AVA-05).

**Consequência para o Core [I]**: `C.RES` deve separar **valor na escala** (ex.: 231,4, escala Saeb LP) de **classificações derivadas**, cada uma com seu esquema de corte versionado e dependente de (etapa, área, edição): nível Saeb, nível SARESP, agrupamento SARESP. A mesma proficiência pode ser "Nível 4" no Saeb e "Adequado" no SARESP.
