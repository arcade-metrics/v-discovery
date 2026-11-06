# Ficha: ISCED 2011 — International Standard Classification of Education

```yaml
id: int.isced-2011
name: International Standard Classification of Education 2011
acronym: ISCED 2011 (ISCED-P, ISCED-A)
jurisdiction: internacional (UNESCO)
issuing_organization: UNESCO Institute for Statistics (UIS); manual operacional conjunto UIS/OCDE/Eurostat
reference_type: classificação estatística internacional (não é norma técnica nem lei)
domain: [D1, D3, D8]
official_url: https://www.uis.unesco.org/en/methods-and-tools/isced
repository_url: not_found (sem repositório de dados; mapeamentos em planilhas, ver int.isced-mappings)
version: ISCED 2011 (adotada pela 36ª Conferência Geral da UNESCO, nov. 2011)
publication_date: 2012
last_updated: FAQ oficial de 2025-08 [N03]; revisão em curso [N02]
legal_status: voluntário para Estados-membros; obrigatório em coletas estatísticas da UE por regulamento (Eurostat cita Reg. 2013/317 e 2013/912) [N14; trecho]
mandatory_scope: estatística internacional (UIS/OCDE/Eurostat); nenhum efeito sobre currículo
education_levels: 0–8 (da primeira infância ao doutorado)
geographic_scope: global
language: en (texto integral); traduções fr, es, ar, ru, zh [N13]
license: unknown para o texto de 2012; manual operacional CC BY-NC-ND 3.0 IGO (resultado de busca, não verificado)
technical_formats: PDF; mapeamentos nacionais em XLSX
api_available: not_found
data_model_available: parcial (variáveis de classificação, sem esquema formal)
ontology_available: not_found (oficial)
schemas_available: not_found
implementation_examples: mapeamentos UIS de 201 países [N03, p. 4]; dados UOE (UNESCO-OCDE-Eurostat)
related_standards: [int.isced-f-2013, ISCED-T 2021, EQF (UE), ISCED 1997]
entities: [programa educacional (unidade de classificação), qualificação, nível, escolaridade obtida]
relationships: programa → nível (1:1 por programa); programa → qualificação; qualificação → nível de escolaridade
vocabularies: níveis 0–8; ISCED-P e ISCED-A de 3 dígitos; orientação; conclusão; acesso; posição na estrutura de graus (ver terminologia.md)
core_relevance: alta — pivô de nível para C.PRG
regional_adapter_relevance: alta — cada adaptador declara seu mapeamento
limitations: não desce a série/ano; não classifica componente curricular; classifica programa, não escola nem aluno
open_questions: [QI-01, QI-02, QI-05]
sources: [N01, N02, N03, N11, N14, N15]
access_date: 2026-11-05
research_status: parcial — PDF oficial não acessado (404/403); estrutura confirmada por FAQ, Eurostat e mapeamentos
```

## Análise técnica (§6.3)

- **Unidade de classificação:** o programa educacional e a qualificação a ele associada; ISCED "classif[ies] education programmes and related qualifications by education levels and fields" [N03, p. 1].
- **Esquemas paralelos:** ISCED-P (programa) e ISCED-A (escolaridade obtida), ambos com 3 dígitos e 9 níveis [N03, p. 5]. Um mesmo programa pode levar a ISCED-A diferente conforme o resultado (Reino Unido, KS4: ISCED-P 342 → ISCED-A 244 ou 342) [N09].
- **Hierarquia:** nível (1º dígito) → categoria (2º) → subcategoria (3º). Tabela completa em [terminologia.md](../terminologia.md).
- **Identificadores:** só o código; não há URI oficial por código [I; not_found].
- **Versionamento:** ISCED 1976 → 1997 → 2011; revisão em curso desde 2023 (ISCED Review Panel, 16 membros; recomendações de emenda ao ISCED-P/A) [N02; N03, pp. 5–6]. Data de adoção da próxima edição: not_found.
- **Extensão:** códigos 9/99/999 para "não classificado"; nada além disso.
- **Conformidade:** validação pelo UIS de cada mapeamento nacional [N03, p. 3].

## O que o Core adota (proposta)

1. `C.PRG.iscedLevel` (código ISCED-P, `scheme = isced-2011-p`) atribuído ao **segmento** da etapa (ex.: EF anos iniciais = 100; anos finais = 244), com proveniência (C.PRV) do mapeamento usado.
2. `C.CRD`/`C.RES` podem levar ISCED-A como escolaridade obtida, separado do programa cursado.
3. Não usar ISCED para série/ano; ver QI-01 sobre um ordinal "anos desde o início do ISCED 1".
