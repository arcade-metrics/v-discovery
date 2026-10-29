# Checklist de revisão

Antes de mudar `status` para `revisado`:

## Identidade e metadados
- [ ] `id` segue `<dominio>.<area>.<slug>` e é único na base.
- [ ] Frontmatter completo: tipo, domínio, datas, `consultado_em`, fontes, relações, termos.
- [ ] Todas as chaves em `fontes` existem em `referencias/bibliografia.bib`.
- [ ] Todos os alvos em `relacoes` existem ou estão listados como lacuna no mapa de conceitos.

## Conteúdo
- [ ] Definição clara, com nomes alternativos e o que o conceito não é.
- [ ] Problema que resolve está explícito.
- [ ] Números, versões, limites e resultados têm `[F]` com fonte.
- [ ] Interpretações estão marcadas `[I]`; hipóteses, `[H]`.
- [ ] Vantagens e limitações aparecem lado a lado.
- [ ] Alternativas comparadas em tabela quando há mais de duas.
- [ ] Exemplo técnico não depende de domínio nem de produto.
- [ ] Nenhuma menção a produto ou projeto consumidor.
- [ ] Recomendações de implementação marcadas como recomendação, com a fonte que recomenda.

## Fontes
- [ ] Cada fonte está no índice com URL, tipo e data de consulta.
- [ ] Especificação normativa, documentação de fornecedor e opinião técnica estão diferenciadas no texto.
- [ ] Nenhuma URL ou DOI sem verificação.

## Consistência
- [ ] Termos batem com o glossário do domínio.
- [ ] Não duplica conceito já documentado; se sobrepõe, relaciona com `parte-de` ou `complementa`.
- [ ] Mapa de conceitos do domínio atualizado.
