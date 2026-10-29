# Padrões de desenvolvimento do VUOO (reservado)

Registro de decisões de arquitetura e padrões técnicos, no formato de ADR (Architecture Decision Record), um por arquivo, com código estável `ADR-nn`. Pasta criada em 29/10/2026 e deixada vazia de propósito: os padrões serão escritos junto com `04-plano.md`, depois da base de conhecimento estar completa nos domínios que os embasam.

## Formato previsto (a confirmar no primeiro ADR)

```yaml
---
id: ADR-01
titulo:
status: proposto | aceito | substituído
contexto: [IN-06, IN-07]                  # insumos
embasamento: [iop.lr.xapi, dat.ev.event-model]   # ids de conhecimento/
substitui:
atualizado_em: AAAA-MM-DD
---
```

Corpo: contexto; decisão; alternativas consideradas, com o id de conhecimento de cada uma; consequências; como se verifica a conformidade.

## Candidatos já identificados na proposta (`../../../projeto/vuoo.md`, F1.2 a F3.1)

Nuvem no Brasil e ambientes; separação física das bases; identidade por perfil; PWA/app com uso offline; ontologia em OWL com consultas SPARQL; pipeline semântico com embeddings e Graph RAG; esquema de eventos de captura e mapeamento para xAPI; conformidade WCAG; CMS de micro-atividades; calibração do palco de medida por DPI.
