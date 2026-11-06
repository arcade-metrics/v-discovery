# Ficha: Portaria MEC 421/2026 (regulamenta a PNEEI)

> Verificada nesta sessão no texto "Vigente" do MECNormas (cópia em PDF hospedada pelo IFG: `PORTARIA MEC No 421, DE 15 DE MAIO DE 2026.pdf`), que registra a alteração do art. 29 pela Portaria MEC 550/2026. Já analisada em acs.br.pneepei-and-aee e acs.asmt.pei-and-aee-plans (2026-10-30); esta ficha confirma o texto e extrai os campos. Acesso: 2026-11-05.

```yaml
id: br.portaria-mec-421-2026
name: "Portaria MEC nº 421, de 15 de maio de 2026: dispõe sobre a PNEEI e a Reneei"
acronym: Port. MEC 421/2026
jurisdiction: Brasil (federal)
issuing_organization: Ministério da Educação (Ministro Leonardo Osvaldo Barchini Rosa)
reference_type: regulamento (portaria ministerial que regulamenta o Decreto 12.686/2025)
domain: [D7, D3, D1]
official_url:
  - https://mecnormas.mec.gov.br/ (registro do ato; app web)
  - https://www.ifg.edu.br/attachments/article/47027/PORTARIA%20MEC%20No%20421,%20DE%2015%20DE%20MAIO%20DE%202026.pdf (impressão da página MECNormas)
repository_url: not_found
version: "texto vigente com alteração da Portaria MEC 550, de 18/06/2026 (art. 29)"
publication_date: 2026-05-18
last_updated: 2026-06-18
legal_status: em vigor desde a publicação (art. 39)
mandatory_scope: redes de ensino da educação básica (AEE, PAEE, PEI); instituições federais (arts. 7 §1, 8)
education_levels: [EI 0–3 (atenção precoce), EF, EM, educação profissional e superior federal]
geographic_scope: nacional
language: pt-BR
license: domínio público [I]
technical_formats: [HTML, PDF]
api_available: false
data_model_available: false (conteúdo mínimo, sem formulário)
ontology_available: false
schemas_available: false
implementation_examples: [Res. SEDUC-SP 129/2025 (anterior à portaria; ver ficha própria)]
related_standards: [br.aee-pneepei, br.lbi, br.sp.resolucao-seduc-129-2025]
entities: [PAEE, PEI, estudo de caso, SRM, profissional de apoio escolar, tradutor e intérprete de Libras, guia-intérprete, Reneei (centros de referência, observatório, núcleos de acessibilização de materiais, autodefensoria, núcleo intersetorial)]
relationships: [PAEE "faz o registro do estudo de caso"; PEI "contempla o plano de acessibilização curricular"; ambos "a partir do estudo de caso"; profissional de apoio atua em consonância com PAEE e PEI]
vocabularies: [campos mínimos do PAEE (art. 10, I–IV) e do PEI (art. 11, I–IV); áreas de apoio do profissional (art. 12 e 14)]
core_relevance: alta: é a única norma federal com **conteúdo mínimo** de plano individual
regional_adapter_relevance: alta
limitations: [não define formato, metas mensuráveis, periodicidade de registro além da revisão anual, nem regras de acesso aos dados]
open_questions: [Q-INC-01, Q-INC-04, Q-INC-05]
sources: [E-29]
access_date: 2026-11-05
research_status: verificado (texto MECNormas; conferência no DOU não feita)
```

## Campos exigidos (texto literal resumido)

| Documento | Campo mínimo | Dispositivo |
|---|---|---|
| PAEE | definição de materiais e recursos para eliminar ou minimizar as barreiras no contexto educacional | art. 10, I |
| PAEE | avaliação da necessidade e da capacidade de disponibilização de recursos de tecnologia assistiva e comunicação aumentativa e alternativa | art. 10, II |
| PAEE | avaliação da necessidade de profissional de apoio escolar, tradutor e intérprete de Libras e guia-intérprete | art. 10, III |
| PAEE | demandas para formação em Educação Especial Inclusiva e para acionamento da rede de proteção social, quando for o caso | art. 10, IV |
| PEI | atividades em SRM ou outros espaços do AEE e sua articulação com o professor regente e demais profissionais | art. 11, I |
| PEI | medidas de acessibilidade curricular, didático-pedagógica e avaliativa, quando indicadas pelo estudo de caso | art. 11, II |
| PEI | estratégias de acompanhamento e de monitoramento do plano | art. 11, III |
| PEI | registro das devolutivas às famílias | art. 11, IV |
| Ambos | revisão anual, "de modo a compatibilizá-los com a avaliação contínua do estudante" | art. 7, §3 |
| Ambos | podem ser documento único, observados os critérios mínimos | art. 7, §2 |
| Apoio escolar | necessidade definida no estudo de caso, considerando apoios em locomoção, higiene, alimentação, interação, comunicação e uso de TA | art. 14 |
| Transição | redes com documentos análogos: até 3 anos (até maio de 2029) para adequar | art. 37 |
| Proibição | matrícula, escolarização e AEE não condicionados a diagnóstico, laudo ou relatório de profissional de saúde | art. 7, §4 |

## Análise técnica [I]

- **Cardinalidade**: 1 estudo de caso → 1 PAEE → 1 PEI por estudante por ciclo de revisão (no mínimo anual), com histórico de versões. Com documento único (art. 7 §2), PAEE e PEI são seções de um mesmo registro: o Core deve modelar **seções obrigatórias**, não documentos.
- **Vocabulário de apoio** que a portaria já fornece: {locomoção, higiene, alimentação, interação, comunicação, uso de tecnologia assistiva} (art. 14) e {profissional de apoio, tradutor-intérprete de Libras, guia-intérprete} (art. 10 III). Base para enum de `C.SUP.tipoDeApoio` no adaptador.
- **Medidas avaliativas** do PEI (art. 11 II) ligam C.PLN a C.ASM: acomodação em avaliação é atributo do plano consumido pela avaliação.
- O **Observatório** (art. 24) produzirá indicadores da PNEEI: possível futura coleta de dados de rede (Q-INC-05).
