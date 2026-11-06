# European Qualifications Framework (EQF)

```yaml
id: eu-eqf
name: European Qualifications Framework for lifelong learning
acronym: EQF (pt: QEQ)
jurisdiction: União Europeia (adesão voluntária de outros países)
issuing_organization: Conselho da UE (Recomendação) / Comissão Europeia
reference_type: recomendação (instrumento não vinculativo) + quadro de referência de níveis
domain: [D2, D4, D8]
official_url: https://europass.europa.eu/en/description-eight-eqf-levels
repository_url: n/a; nível disponível como lista controlada http://data.europa.eu/snb/eqf/
version: Recomendação do Conselho de 22 de maio de 2017 (substitui a de 2008)
publication_date: 2017-06-15 (JO C 189) [verificado por busca, texto EUR-Lex não aberto]
last_updated: unknown
legal_status: recomendação; não obriga Estados-membros
mandatory_scope: nenhum; Estados referenciam seus quadros nacionais (NQF) voluntariamente
education_levels: todos os níveis de qualificação (1 a 8)
geographic_scope: UE + países participantes
language: todas as línguas oficiais
license: n/a
technical_formats: lista controlada SKOS (EU Vocabularies)
api_available: n/a
data_model_available: n/a (é escala)
ontology_available: como skos:ConceptScheme
schemas_available: n/a
implementation_examples: elm:EQFLevel em qualificações do QDR
related_standards: [NQFs nacionais, QF-EHEA (Bolonha), ISCED 2011, eu-elm]
entities: Level (1..8) com descritores Knowledge / Skills / Responsibility and autonomy
relationships: NQF level ↔ EQF level (referenciação nacional)
vocabularies: eqf
core_relevance: média: exemplo de escala de nível como vocabulário externo; pouco útil para educação básica
regional_adapter_relevance: média (qualificações de saída do secundário costumam estar em EQF 3-4)
limitations: descreve qualificações, não anos escolares; não aplicável a progressão dentro da educação básica
open_questions: campos do Anexo VI (dados mínimos de publicação de qualificações) não lidos
sources: [S-UE-07, S-UE-08, S-UE-09]
access_date: 2026-11-05
research_status: parcial
```

## Análise

Oito níveis, cada um descrito em três colunas: **Knowledge**, **Skills**, **Responsibility and autonomy** [S-UE-07]. Descritores de conhecimento (literais) estão em [terminologia.md](../terminologia.md#eqf). A página da Europass também relaciona os níveis 5–8 ao quadro de qualificações do Espaço Europeu de Ensino Superior (Bergen, 2005) [S-UE-07].

Relação com NQFs: cada país "referencia" seu quadro nacional ao EQF; o ELM tem `EQFLevel` e `NQFLevel` separados na `Qualification`, ambos `skos:Concept` [S-UE-02]. O Anexo VI da Recomendação de 2017 define elementos de dados para publicar qualificações com nível EQF, base do QDR [S-UE-09]; o conteúdo do anexo **não foi lido** (EUR-Lex não respondeu).

**Para o Core [I]:** EQF é exemplo de **nível de qualificação** distinto de **ano/etapa** (C.PRG) e de **nível de proficiência** de uma competência (DigComp). O Core precisa de três eixos de "nível" que não se confundem. Não há alvo exato no Core provisório para "nível de qualificação" (ver questões abertas).
