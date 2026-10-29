# Guia da frente de pesquisa

Instruções para quem (pessoa ou agente) produz os documentos de uma **área** de um domínio de `conhecimento/`. Complementa, sem substituir, `modelo-documental.md`, `metodo-e-qualidade.md` e `checklist-revisao.md`. Leia os três antes de começar.

## 1. O que uma frente entrega

Para a área atribuída (por exemplo `privacidade-seguranca-e-governanca/consent/`):

1. **Os documentos conceituais** listados no `_plano-ids.md` do domínio para essa área, um arquivo por id, no caminho indicado. Use `template-conceito.md`; só as seções que se aplicam, nesta ordem, sem seção vazia.
2. **Um fragmento de bibliografia**: `referencias/fragmentos/<prefixo>-<area>.bib`, com uma entrada BibTeX por fonte citada.
3. **Um fragmento de índice de fontes**: `referencias/fragmentos/<prefixo>-<area>-indice.md`, uma linha por fonte, no formato exato abaixo.
4. **Um relatório final curto** (na resposta, não em arquivo) no formato da seção 7.

Não edite nenhum outro arquivo do repositório. README, glossário, mapa, matriz e relatório do domínio são montados depois, a partir dos relatórios das frentes.

## 2. Regra de ouro: abrir antes de citar

Toda afirmação marcada `[F]` vem de uma fonte que você **abriu e leu** nesta sessão (WebFetch, ou download com `curl.exe -L` para a pasta de rascunho e leitura do PDF). Se a fonte não abriu (paywall, 403, timeout):

- não invente conteúdo, DOI, URL, número de página nem resultado;
- se houver fonte alternativa aberta que descreva o mesmo resultado (pré-print, página do autor, capítulo posterior dos mesmos autores), use-a e diga isso no texto;
- se só os metadados puderam ser confirmados (catálogo, Crossref), a entrada entra na bibliografia com `note = {Somente metadados verificados; texto integral nao acessado}` e o título no índice recebe o sufixo `[metadados]`; no corpo, cite como `[F: chave, metadados]` e só para o que os metadados sustentam (existência, autoria, ano, título);
- se nada pôde ser verificado, não cite: registre em "Lacunas e questões abertas".

Números, versões, limites, artigos de lei e resultados experimentais exigem `[F]` com fonte. Parágrafo sem marca é `[I]`. Hipótese sem verificação é `[H]`.

## 3. Prioridade e tipo de fonte

Ordem de preferência: `normativo` (lei, decreto, resolução, RFC, W3C, ISO, IEEE, norma técnica) > `fornecedor` (documentação oficial, com versão) > `academico` (revisado por pares, livro acadêmico) > `tecnico` (praticante reconhecido, relatório de órgão) > `secundario` (resumo, blog, notícia; só quando agrega algo que as anteriores não têm).

Para texto legal brasileiro, a fonte primária é o Planalto (`planalto.gov.br/ccivil_03/...`) ou o Diário Oficial; guias e enunciados da ANPD, do CNS e de órgãos públicos são `tecnico` ou `normativo` conforme a natureza. Informe sempre a redação vigente e a data de consulta; se o texto foi alterado por lei posterior, diga qual.

## 4. Frontmatter e id

```yaml
---
id: psg.consent.parental-consent          # exatamente o do _plano-ids.md
titulo: Consentimento parental
tipo: conceito          # conceito | tecnica | protocolo | padrao | framework | estudo-de-caso | comparacao
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [chave1, chave2]                  # só chaves do seu fragmento .bib ou já existentes em bibliografia.bib
relacoes:
  - { tipo: parte-de, alvo: psg.consent.comparison }
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: iop.br.lgpd }
termos: [consentimento parental, responsável legal, melhor interesse]
---
```

- Tipos de relação e sua semântica: `modelo-documental.md` §3. Relações apontam para ids, nunca para caminhos. Prefira ids do próprio `_plano-ids.md` e ids já existentes em outros domínios (lista no prompt da frente). Não aponte para id que não existe nem está planejado.
- `termos`: os termos que o documento define ou usa de forma técnica. É daí que sai o glossário.

## 5. Corpo do documento

Seções de `modelo-documental.md` §4, nesta ordem, só as que se aplicam: Definição e terminologia; Problema que resolve; Fundamentos e funcionamento; Algoritmos e modelos relevantes; Requisitos e pressupostos; Vantagens e limitações; Alternativas e comparações (tabela quando houver mais de duas); Métricas e métodos de avaliação; Exemplo técnico independente de domínio; Relações com outros conceitos; Lacunas e questões abertas; Fontes (tabela chave, tipo, consultado em).

Regras de redação:
- Prosa em português; termos consolidados em inglês quando é o uso da literatura; identificadores e chaves em ASCII minúsculo.
- Citação direta curta entre aspas, com `[F: chave, §seção]` ou `[F: chave, art. N]`.
- Diferencie no texto o que é norma ("a lei determina"), documentação de fornecedor ("a documentação afirma") e opinião técnica ("o autor recomenda").
- Recomendação de implementação é sempre marcada como recomendação, com quem recomenda.
- **Nenhuma menção a produto ou projeto consumidor** da base, nem a empresas ou centros parceiros. O validador rejeita.
- Exemplo técnico: pseudocódigo, diagrama em texto, trecho de política ou esquema; nunca código de produto.
- Tamanho de referência: 80 a 160 linhas por documento. Mais que isso, considere dividir (e avise no relatório).

## 6. Fragmentos de referência

**`.bib`**: convenção de chave `<sobrenome-primeiro-autor><ano><palavra-do-titulo>`, minúsculas, ASCII; lei brasileira: `lei<numero><ano>` (ex.: `lei13709lgpd`), decreto: `decreto<numero><ano>`, resolução: `<orgao><numero><ano>`; RFC: `rfc<numero>`; W3C: `w3c<ano><slug>`; ISO: `iso<numero><ano>`; documentação de fornecedor ou órgão: `<orgao><ano><slug>`. Campos obrigatórios: `url` e `urldate` (data de consulta); quando houver, `doi`, `version`, `note`. Antes de criar uma chave, verifique em `referencias/bibliografia.bib` se a fonte já existe e reutilize a chave existente (ela já está no índice; não a repita no seu fragmento).

**`-indice.md`**, exatamente:

```
# Índice de fontes — <dominio>/<area>

| Chave | Título | Tipo | Domínio | URL | Consultado em |
|---|---|---|---|---|---|
| chave | Autor, Título (veículo, ano, DOI se houver) | normativo | <dominio> | https://... | 2026-10-29 |
```

## 7. Relatório final da frente

Na resposta final, e só nela, até 80 linhas:

```
## Documentos escritos
- <id> — <caminho> — <n linhas> — <uma frase sobre o que cobre>

## Fontes
- abertas e lidas: N; só metadados: N; não citadas por falta de verificação: N
- bloqueadas (chave ou título, motivo): ...

## Glossário (termo | definição em uma linha | id que aprofunda)
- ...

## Comparações principais (para a matriz do domínio)
- <critério>: <opção A> vs <opção B>: <uma linha>

## Lacunas e questões abertas (consolidadas)
- ...

## Relações para fora da área (id origem → tipo → id alvo)
- ...

## Avisos
- qualquer desvio do plano de ids, documento dividido, seção omitida e por quê
```
