# Ficha: Educação especial, AEE, PNEEPEI (2008) e PNEEI (Decreto 12.686/2025)

> Ficha **curta**: a análise normativa completa (linha do tempo 2008–2026, público, oferta, laudo) é dona de `conhecimento/acessibilidade-educacao-especial-e-dua/brazil/pneepei-and-aee.md` (acs.br.pneepei-and-aee); o plano como instrumento, de `.../assessment/pei-and-aee-plans.md` (acs.asmt.pei-and-aee-plans). Aqui só o que falta para o Core. A Portaria MEC 421/2026 tem ficha própria. Acesso: 2026-11-05.

```yaml
id: br.aee-pneepei
name: Política de educação especial na perspectiva inclusiva e Atendimento Educacional Especializado
acronym: PNEEPEI (2008) / PNEEI (2025) / AEE
jurisdiction: Brasil (federal)
issuing_organization: MEC (política de 2008); Presidência (Decreto 12.686/2025, alterado pelo 12.773/2025); CNE/CEB (Res. 4/2009)
reference_type: [documento de política (2008), decreto, resolução do CNE]
domain: [D7, D3, D1]
official_url:
  - https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12773.htm
  - ver lista de fontes em acs.br.pneepei-and-aee
repository_url: not_found
version: "PNEEI: Decreto 12.686 de 20/10/2025, alterado pelo Decreto 12.773 de 08/12/2025"
publication_date: 2025-10-21
last_updated: 2025-12-09
legal_status: em vigor (decreto); PNEEPEI 2008 é documento de política
mandatory_scope: sistemas e redes de ensino (dever de ofertar AEE); extensão literal a privadas com fins lucrativos não verificada (acs.br.pneepei-and-aee)
education_levels: [EI (atenção precoce 0–3 anos), EF, EM, superior]
geographic_scope: nacional
language: pt-BR
license: domínio público [I]
technical_formats: [HTML]
api_available: false
data_model_available: false (conteúdo mínimo de documentos, sem formato)
ontology_available: false
schemas_available: false
implementation_examples: [Res. SEDUC-SP 129/2025, anexos II a V]
related_standards: [br.portaria-mec-421-2026, br.lbi, br.lei-12764-tea, br.lei-14254, br.sp.decreto-67635, cmdeb (campo ESTUDANTE_DEFICIENCIA)]
entities: [estudante público da educação especial, estudo de caso, PAEE, PEI, sala de recursos multifuncionais, professor de AEE, profissional de apoio escolar, tradutor-intérprete de Libras, guia-intérprete, recurso de acessibilidade, tecnologia assistiva, CAA, barreira, potencialidade, demanda de apoio]
relationships: [estudo de caso → PAEE (registro) → PEI (acessibilização curricular); profissional de apoio atua "em consonância" com PAEE e PEI; AEE complementa/suplementa, não substitui a classe comum]
vocabularies: [público: deficiência, TEA, altas habilidades ou superdotação; etapas do estudo de caso (Dec. 12.686 art. 11 §1)]
core_relevance: alta: define C.SUP e C.PLN no Brasil e proíbe o laudo como porta de entrada
regional_adapter_relevance: alta
limitations: [sem formato nacional de documento; sem metas mensuráveis obrigatórias (comparação com IEP em acs.asmt.pei-and-aee-plans)]
open_questions: [Q-INC-01, Q-INC-02, Q-INC-06]
sources: [E-27, E-28, conhecimento/ (acs.br.pneepei-and-aee, acs.asmt.pei-and-aee-plans)]
access_date: 2026-11-05
research_status: verificado em conhecimento/ (2026-10-30); portaria reconferida aqui
```

## O que o Core precisa suportar (derivado das normas citadas em conhecimento/) [I]

| Requisito | Base | Implicação |
|---|---|---|
| Elegibilidade e apoio sem laudo | Dec. 12.686 art. 11 §7 e art. 14 §2; Port. 421 art. 7 §4 | `C.SUP` e `C.PLN` não podem ter campo de diagnóstico obrigatório nem regra que dependa dele |
| Estudo de caso em 4 etapas (demandas e barreiras; análise de barreiras e contexto; potencialidades e demandas de apoio; estratégias e recursos) | Dec. 12.686 art. 11 §1 | entidade `EstudoDeCaso` com barreiras, contexto, potencialidades, demandas; candidata a entidade do Core (Q-INC-01) |
| Participação do estudante e da família em todo o processo | Dec. 12.686 art. 11 §3 | participantes tipados no plano; registro de devolutivas |
| Dados pessoais e sensíveis nos documentos seguem LGPD art. 14 | Dec. 12.686 art. 12 §5 | plano é dado sensível de criança: ver lgpd-educacao.md |
| Parecer pedagógico autoriza dispositivo digital portátil como TA | Dec. 12.686 art. 12 §4 | o uso da própria plataforma como TA pode exigir um ato da escola registrado (autorização) |
| Censo Escolar registra deficiência/TEA/AH-SD por categoria | CMDEB `ESTUDANTE_DEFICIENCIA` (11 códigos) | a categoria administrativa existe e é exigida em coletas oficiais; deve ficar isolada do modelo pedagógico (Q-INC-03) |
