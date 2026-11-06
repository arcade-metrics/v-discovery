# Ficha curta: W3C Verifiable Credentials 2.0 e Open Badges 3.0

> Análise completa em conhecimento/interoperabilidade/credentials/verifiable-credentials.md (`iop.cred.verifiable-credentials`), open-badges.md (`iop.cred.open-badges`) e clr.md (`iop.cred.clr`). Não repetir.

## Status (conferido nos documentos existentes)

| Padrão | Status | Onde |
|---|---|---|
| VC Data Model 2.0 | **W3C Recommendation, 2025-05-15**; `@context` com primeiro item `https://www.w3.org/ns/credentials/v2` | `iop.cred.verifiable-credentials` |
| Open Badges 3.0 | Final Release, documento 1.4.5, 2026-06-29; alinhado ao VCDM 2.0 (Assertion é também VC); mantém esquemas VCDM 1.1 em paralelo | `iop.cred.open-badges` |
| CLR 2.0 | CLR passa a ser VC | `iop.cred.clr` |

Resposta ao briefing: sim, o VC 2.0 virou Recommendation em 2025, e o Open Badges 3.0 está alinhado a ele.

```yaml
id: int.credentials
name: W3C Verifiable Credentials Data Model 2.0; 1EdTech Open Badges 3.0
jurisdiction: internacional (W3C; 1EdTech)
reference_type: recomendação W3C; padrão voluntário de consórcio
domain: [D3, D5, D8]
core_relevance: média — C.CRD; baixa prioridade para educação básica com neurodivergentes [I]
open_questions: [QI-21]
sources: [conhecimento/]
access_date: 2026-11-05
research_status: apontado
```

## O que falta para o Core

- C.CRD deve conseguir ser **exportada** como OB 3.0 `AchievementCredential` (VC 2.0), com `Achievement` alinhado a C.CMP por URI persistente [I].
- Cuidado específico do público: uma credencial que revele apoio recebido (ex.: "concluído com adaptação") vira dado sensível portável; o Core não deve carregar C.SUP em credenciais exportáveis por padrão [I] (QI-21).
