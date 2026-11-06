# Padrões de desenvolvimento (ADR)

Decisões de arquitetura, uma por arquivo, com código estável `ADR-nn`. Pasta criada em 05/11/2026; os ADRs nascem com o `04-plano.md`.

## Formato

```yaml
---
id: ADR-01
titulo:
status: proposto | aceito | substituído
origem: []          # seção do 02-prd.md / 03-mvp.md
embasamento: []     # arquivos de base/
substitui:
atualizado_em: AAAA-MM-DD
---
```

Corpo: contexto; decisão; alternativas consideradas; consequências; como se verifica a conformidade.

## Candidatos

- Core agnóstico + perfil Brasil + mapeamentos como dado (`base/camada-agnostica/`, `base/camada-brasil/`).
- Identificador como lista; vínculos bitemporais; tenant por rede.
- Grafo de conhecimento em tabelas relacionais no MVP.
- Manifesto de atividade e motor de atividades.
- Eventos em CloudEvents, fila local e envio idempotente (`base/captura-de-interacao.md`).
- Stack de partida (`base/parametrizacao-estilo.md` §0): Flutter no app do aluno, React na web, tokens W3C, animação em código + Rive + Lottie.
