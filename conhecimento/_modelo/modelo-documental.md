# Modelo documental

Vale para todos os domínios de `conhecimento/`. O objetivo é que cada documento seja legível sozinho, rastreável até a fonte e convertível no futuro para um grafo (RDF/SKOS/OWL) sem retrabalho.

## 1. Identificadores

Formato: `<dominio>.<area>.<slug>`, em inglês, minúsculas, hífens.

| Domínio | Prefixo |
|---|---|
| realtime-multiplayer | `rtm` |
| aprendizagem-adaptativa | `adp` |
| grafo-conhecimento-educacional | `kg` |
| interoperabilidade | `iop` |
| lms-e-plataformas | `lms` |
| dados-pesquisa-e-eventos | `dat` |
| gamificacao-e-jogos | `gam` |
| learning-analytics-e-avaliacao | `lae` |
| fundamentos-pedagogicos | `ped` |
| privacidade-seguranca-e-governanca | `psg` |
| acessibilidade-educacao-especial-e-dua | `acs` |

Exemplos: `rtm.sync.snapshot-interpolation`, `iop.spec.xapi`, `adp.model.bayesian-knowledge-tracing`.

Um id nunca muda depois de publicado. Se o conceito for renomeado, o arquivo muda de nome e o id permanece. Se o conceito for dividido ou fundido, todas as referências ao id antigo são reescritas para os novos e o id antigo deixa de existir; não fica documento de redirecionamento.

## 2. Frontmatter YAML

```yaml
---
id: rtm.sync.snapshot-interpolation
titulo: Snapshot interpolation
tipo: conceito          # conceito | tecnica | protocolo | padrao | framework | estudo-de-caso | comparacao | glossario | mapa | relatorio
dominio: realtime-multiplayer
status: rascunho        # rascunho | revisado
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29   # data em que as fontes foram consultadas
fontes: [fiedler2014snapshot, gambetta2014entity]   # chaves de referencias/bibliografia.bib
relacoes:
  - { tipo: parte-de, alvo: rtm.sync.state-synchronization-family }
  - { tipo: alternativa-a, alvo: rtm.sync.state-synchronization }
  - { tipo: depende-de, alvo: rtm.net.latency }
termos: [snapshot, interpolation delay, jitter buffer]   # termos do glossário que este doc define ou usa
---
```

## 3. Relações tipadas

| Tipo | Semântica | Mapeamento futuro |
|---|---|---|
| `parte-de` | o conceito é uma subdivisão do alvo | `skos:broader` |
| `depende-de` | só faz sentido ou só funciona dado o alvo | propriedade própria (`kb:dependsOn`) |
| `alternativa-a` | resolve o mesmo problema por outro caminho | `kb:alternativeTo` (simétrica) |
| `complementa` | costuma ser usado junto com o alvo | `kb:complements` (simétrica) |
| `especificado-por` | o alvo é a norma ou especificação | `kb:specifiedBy` |
| `implementado-por` | o alvo é framework ou produto que o implementa | `kb:implementedBy` |
| `avaliado-por` | o alvo é métrica ou método de avaliação | `kb:evaluatedBy` |
| `relacionado-a` | relação não tipada, usar com moderação | `skos:related` |

Relações apontam sempre para ids, nunca para caminhos de arquivo. O mapa de conceitos de cada domínio é gerado a partir delas.

## 4. Seções do documento

Use as que se aplicam, nesta ordem. Não crie seção vazia.

1. **Definição e terminologia**: o que é, nomes alternativos, o que não é.
2. **Problema que resolve**
3. **Fundamentos e funcionamento**
4. **Algoritmos e modelos relevantes**
5. **Requisitos e pressupostos**: o que precisa ser verdade para a técnica funcionar.
6. **Vantagens e limitações**
7. **Alternativas e comparações**: tabela quando houver mais de duas.
8. **Métricas e métodos de avaliação**
9. **Exemplo técnico independente de domínio**: pseudocódigo ou diagrama, nunca código de produto.
10. **Relações com outros conceitos**: espelha o frontmatter em prosa curta.
11. **Lacunas e questões abertas**
12. **Fontes**: lista das chaves citadas, com tipo de fonte e data de consulta.

## 5. Marcas de afirmação

- `[F]` fato documentado, com citação `[F: chave]` ou `[F: chave, §seção]`.
- `[I]` interpretação ou síntese do autor do documento.
- `[H]` hipótese, ainda sem verificação.

Parágrafos sem marca são considerados `[I]`. Números, versões, limites e resultados experimentais exigem `[F]` com fonte.

## 6. Tipos de fonte

`normativo`, `fornecedor`, `academico`, `tecnico`, `secundario`. O tipo é registrado no índice de fontes e, quando relevante, no próprio texto ("a RFC define", "a documentação do fornecedor afirma", "o autor recomenda").

## 7. Versões e datas

Informações que dependem de versão (API de framework, versão de protocolo, limite de plano) trazem a versão no texto e a data de consulta no frontmatter. Quando a fonte tem versão, a entrada BibTeX inclui o campo `version`.

## 8. Glossário e mapa

Cada domínio mantém `glossario.md` (termo, definição curta, id do documento que aprofunda) e `mapa-conceitos.md` (lista de relações e um diagrama em texto). O índice raiz em `glossario/README.md` aponta para os glossários dos domínios.
