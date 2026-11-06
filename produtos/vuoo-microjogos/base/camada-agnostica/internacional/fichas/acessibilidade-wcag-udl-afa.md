# Ficha curta: acessibilidade transversal — WCAG 2.2, CAST UDL 3.0, ISO/IEC 24751 (AccessForAll)

> Análises completas, já atualizadas em outubro/novembro de 2026, em `conhecimento/acessibilidade-educacao-especial-e-dua/`:
> - standards/wcag.md (`acs.std.wcag`): WCAG 2.2 e estado do WCAG 3;
> - udl/udl-guidelines.md (`acs.udl.udl-guidelines`): UDL 3.0;
> - standards/accessforall-iso-24751.md (`acs.std.accessforall-iso-24751`) e adaptation/preference-profiles.md (`acs.adapt.preference-profiles`).
>
> Não repetir. Abaixo, só status (conferido nesses documentos) e o que o Core precisa representar.

## Status

| Padrão | Status registrado em `conhecimento/` | Fonte do status |
|---|---|---|
| WCAG 2.2 | W3C Recommendation de 2023-10-05, reeditada em 2024-12-12; publicada como ISO/IEC 40500:2025 | `acs.std.wcag`, §1 |
| WCAG 3 | Working Draft de 2026-09-10; "several years of work" pela frente; conformidade em níveis 1–6 ainda instável | `acs.std.wcag`, "O estado do WCAG 3" |
| CAST UDL Guidelines | versão 3.0, lançada em 2024-07-30; 3 princípios, 9 diretrizes, 36 considerações; tradução oficial pt-BR | `acs.udl.udl-guidelines` |
| ISO/IEC 24751 | Partes 1–3 (2008) em vigor, confirmadas em revisão de 2026; Parte 4 (2023): registro de conceitos AfA, JSON e REST | `acs.std.accessforall-iso-24751` |

Nada novo a acrescentar nesta sessão: o pedido de "verificar se WCAG 3 avançou" já está respondido no documento existente com fonte de setembro de 2026.

```yaml
id: int.accessibility-cross
name: WCAG 2.2 / CAST UDL Guidelines 3.0 / ISO/IEC 24751 AccessForAll
jurisdiction: internacional (W3C; CAST, organização sem fins lucrativos dos EUA; ISO/IEC JTC 1/SC 36)
reference_type: recomendação W3C (e norma ISO/IEC 40500) / framework pedagógico / norma técnica
domain: [D6, D7]
official_url: https://www.w3.org/TR/WCAG22/ ; https://udlguidelines.cast.org/ ; https://www.iso.org/ (24751)
version: WCAG 2.2; UDL 3.0; 24751-1/-2/-3:2008, 24751-4:2023
core_relevance: alta
open_questions: [QI-19, QI-20]
sources: [conhecimento/]
access_date: 2026-11-05
research_status: apontado
```

## O que o Core precisa representar (proposta)

| Necessidade | Padrão-fonte | Onde no Core [I] |
|---|---|---|
| Nível de conformidade declarado de cada atividade/recurso (A, AA, AAA; critérios não atendidos) | WCAG 2.2 | atributo de C.ACT (`accessibilityConformance`), com versão do padrão |
| Alvo de produto | WCAG 2.2 AA | requisito não funcional, não dado |
| Necessidades e preferências de acesso da pessoa (modo de acesso, adaptação desejada, legenda, leitura em voz, tempo estendido) | ISO/IEC 24751-2 (PNP) | **candidata a entidade nova** C.PRF (AccessPreference), ligada a C.LRN e separada de C.SUP: preferência ≠ necessidade diagnosticada |
| Descrição do que o recurso oferece (modos de acesso, adaptações disponíveis) | ISO/IEC 24751-3 (DRD); schema.org `accessMode`, `accessibilityFeature` | atributos de C.ACT |
| Correspondência perfil × recurso | AfA | regra de serviço, não dado |
| Anotação de desenho DUA de uma atividade (quais considerações apoia) | UDL 3.0 (códigos como 7.1, 1.2, 4.1) | C.VOC `scheme = cast-udl-3.0`, associado a C.ACT; o CAST diz que DUA não é "a prescription or a checklist" (ver `acs.udl.udl-guidelines`), então é anotação, não conformidade |
