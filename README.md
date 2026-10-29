# Discovery: base curada do VUOO

Repositório de descoberta do produto VUOO (Wemoga + CIATec/CCD, EACH/USP). Reúne as fontes do projeto, uma base de conhecimento técnica agnóstica, benchmarks de produtos existentes e as decisões de produto, em camadas que só se referenciam de cima para baixo.

```
projeto/        propostas (PIPE-TC, CCD) e insumos IN-nn extraídos delas      → projeto/README.md
conhecimento/   11 domínios técnicos, ids estáveis, sem menção a produto       → conhecimento/README.md
benchmarks/     teardowns de produtos existentes (hoje: Duolingo)              → benchmarks/README.md
produtos/       vuoo/ (plataforma, regras, padrões) e vuoo-linguagem/ (estudo) → produtos/vuoo/LEIAME.md
.claude/skills/ skills de produto que geram os specs em produtos/              → abaixo
```

A regra que organiza tudo: **cada fato tem um dono, o resto aponta** (detalhe em `projeto/README.md`). Validação da base de conhecimento: `python conhecimento/_modelo/validar.py`.

---

# Infra de produto: da ideia ao plano

Cinco skills para Claude Code que transformam uma ideia de app em um conjunto de specs versionados no repo.

## Instalação

Copie as pastas para as skills do projeto (ficam versionadas junto com o código):

```bash
mkdir -p .claude/skills
cp -r produto produto-descoberta produto-prd produto-mvp produto-plano .claude/skills/
```

Ou, para usar em qualquer projeto, troque o destino por `~/.claude/skills/`.

## Uso

Abra o Claude Code na raiz do repo e diga a ideia. A skill `produto` identifica a etapa e chama a seguinte. Para continuar depois:

> continua o produto diario-de-treino

## O que é gerado

```
produtos/<slug>/
  00-brief.md      problema, público, hipóteses, riscos
  01-contexto.md   alternativas de hoje, concorrentes (opcional)
  02-prd.md        jobs, fluxos, requisitos, métricas
  03-mvp.md        corte de escopo, ordem por risco, critérios de aceite
  04-plano.md      arquitetura, dados, marcos, riscos técnicos
```

O estado vive nos arquivos, não na conversa: qualquer sessão nova lê a pasta e sabe onde parou.

## Convenções

- `[ASSUMIDO]` — inferido, precisa de confirmação
- `[A CONFIRMAR]` — depende de dado externo
- `[HIP-n]` — hipótese do brief; requisitos e features apontam para ela

Commite `produtos/` junto com o código. O valor maior aparece quando o PRD muda no mesmo diff da feature.
