# Ficha: Next Generation Science Standards

> Sem documento em `conhecimento/`. Ficha completa, como framework curricular.

```yaml
id: us.ngss
name: Next Generation Science Standards
acronym: NGSS
jurisdiction: Estados Unidos (adoção estadual)
issuing_organization: NGSS Lead States (26 estados) com Achieve, Inc.; marcas transferidas à WestEd em maio de 2020 [E26, trecho]; base no NRC "A Framework for K-12 Science Education" (2012)
reference_type: framework curricular (padrões de desempenho em ciências)
domain: [D2, D4, D5]   # D5: assessment boundary e evidence statements
official_url: https://www.nextgenscience.org/
repository_url: not_found (sem publicação legível por máquina localizada no site oficial)
version: release de abril de 2013 [E25]
publication_date: 2013-04
last_updated: unknown
legal_status: framework voluntário adotado por ato estadual
mandatory_scope: estados adotantes (contagem atual não verificada em fonte oficial; fontes secundárias citam ~20 estados + DC)
education_levels: K-12 (K a 5 por série; MS e HS por banda) [E25]
geographic_scope: EUA
language: inglês
license: "© 2013 Achieve, Inc." em edições impressas; DCIs reproduzidos do Framework NRC com copyright da National Academy of Sciences (2012); uso de marca exige revisão pela WestEd [E26, trecho]
technical_formats: HTML, PDF
api_available: not_found
data_model_available: parcial (arquitetura documentada em "How to Read")
ontology_available: not_found
schemas_available: not_found
implementation_examples: códigos de PE, ex. 2-PS1-2, HS-PS1-1 [E25]
related_standards: [CCSS (connection boxes), NRC Framework, CASE (publicação não confirmada)]
entities: PerformanceExpectation; foundation boxes: ScienceAndEngineeringPractice, DisciplinaryCoreIdea (com sub-ideia), CrosscuttingConcept; ClarificationStatement; AssessmentBoundary; ConnectionBox [E25]
relationships: PE construída de SEP + DCI + CCC (cada elemento das caixas marcado com o código da PE); conexões a DCIs da mesma série, a DCIs de outras séries (articulação) e a CCSS [E25]
vocabularies: códigos de disciplina/ideia central (PS1–PS4, LS1–LS4, ESS1–ESS3, ETS) e sub-ideias (PS1A…) [E25]
core_relevance: alta — único framework do pacote com estrutura **multidimensional** (cada objetivo é combinação de três dimensões)
regional_adapter_relevance: alta (ciências nos estados adotantes)
limitations: sem formato legível por máquina oficial localizado; contagem de adoção atual não confirmada
open_questions: Q10, Q13
sources: [E24, E25, E26]
access_date: 2026-11-05
research_status: verificado em fonte oficial (estrutura e códigos); licença e adoção por trecho
```

## Análise técnica

**Três dimensões** [E24]: Práticas (científicas e de engenharia); Conceitos Transversais (sete, ex.: padrões, causa e efeito, sistemas e modelos de sistemas); Ideias Centrais Disciplinares, em quatro domínios: ciências físicas, ciências da vida, ciências da Terra e do espaço, e engenharia, tecnologia e aplicações da ciência. "Will be combined to form each standard" [E24].

**Arquitetura de cada padrão** [E25]: título; caixa de performance expectations (PEs); três *foundation boxes* (SEP, DCI, CCC); seção de conexões. PEs são "the assessable statements of what students should know and be able to do"; alguns estados consideram só as PEs como "o padrão", outros incluem caixas e conexões — "The writing team is neutral on that issue". PEs "are not a set of instructional or assessment tasks". Abaixo da PE: *clarification statements* (exemplos) e *assessment boundary* ("limits to large scale assessment").

**Códigos** [E25]: "the first digit indicates a grade K-5, or specifies MS (middle school) or HS (high school). The next alpha-numeric code specifies the discipline, core idea and sub-idea… the number at the end of each code indicates the order in which that statement appeared as a DCI in the Framework." Ex.: `2-PS1-2`, `HS-PS1-1`. Uma DCI pode ser "moved from K-2" para outra série.

**Lições para o Core [I]:**
1. Um objetivo (PE) é **composto** por elementos de três esquemas diferentes → C.CAS precisa de relação de composição com papel (`dimension`), não só hierarquia.
2. O mesmo conjunto de PEs é apresentado em dois arranjos (por tópico e por DCI; visto só em trecho de busca, edição da National Academies Press com capítulo "Arranged by Topics", não lido) → múltiplas hierarquias sobre os mesmos C.CMP; a árvore não pode ser propriedade do item.
3. "Assessment boundary" é restrição de avaliação ligada ao objetivo → atributo/associação entre C.CMP e C.ASM.
4. Divergência normativa sobre o que é "o padrão" (só PE ou PE + caixas) deve ser registrada no adaptador, não resolvida no Core.
