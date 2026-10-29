# Base de conhecimento da stack tecnológica

Base técnica, agnóstica e reutilizável sobre os domínios tecnológicos que sustentam plataformas educacionais adaptativas. Não contém decisões de nenhum produto. A ponte entre esta base e um produto vive na pasta do produto (ex.: `produtos/<slug>/stack.md`), que cita os identificadores dos conceitos daqui.

## Organização

```
conhecimento/
  _modelo/                         modelo documental, método, checklist (vale para todos os domínios)
  referencias/                     bibliografia.bib única e índice de fontes com data de consulta
  glossario/                       índice dos glossários por domínio
  realtime-multiplayer/            tempo real, redes, protocolos, sincronização, multiplayer
  aprendizagem-adaptativa/         modelos de aluno, knowledge tracing, adaptação, gêmeos digitais
  grafo-conhecimento-educacional/  RDF/SKOS/OWL, ontologias educacionais, Graph RAG
  interoperabilidade/              xAPI, LTI, QTI, OneRoster, Caliper, CIF, FHIR
  lms-e-plataformas/               benchmark de LMS, plataformas adaptativas e jogos sérios
  dados-pesquisa-e-eventos/        telemetria, esquemas de evento, FAIR, ética de pesquisa, datasets
  gamificacao-e-jogos/             gamificação, jogos sérios, motivação, dificuldade, evidências
  learning-analytics-e-avaliacao/  LA/EDM, qualidade de dado, indicadores, avaliação, psicometria
  fundamentos-pedagogicos/         teorias, desenho instrucional, ciência da aprendizagem, inclusão, padrões de evidência
  privacidade-seguranca-e-governanca/  LGPD e menores, consentimento, anonimização, segurança, governança de IA
  acessibilidade-educacao-especial-e-dua/  DUA, WCAG/ARIA/ISO 24751, tecnologia assistiva, adaptações, barreiras e suporte
```

Cada domínio tem um `00-brief.md` com escopo, fontes prioritárias e perguntas abertas. O restante do domínio segue o modelo em [`_modelo/modelo-documental.md`](_modelo/modelo-documental.md).

## Estado por domínio

| Domínio | Prefixo de id | Estado |
|---|---|---|
| realtime-multiplayer | `rtm` | primeira versão |
| aprendizagem-adaptativa | `adp` | primeira versão |
| grafo-conhecimento-educacional | `kg` | primeira versão |
| interoperabilidade | `iop` | primeira versão |
| lms-e-plataformas | `lms` | brief (`duolingo_benchmark/` na raiz do repo é o primeiro estudo) |
| dados-pesquisa-e-eventos | `dat` | brief |
| gamificacao-e-jogos | `gam` | brief |
| learning-analytics-e-avaliacao | `lae` | primeira versão |
| fundamentos-pedagogicos | `ped` | brief |
| privacidade-seguranca-e-governanca | `psg` | brief |
| acessibilidade-educacao-especial-e-dua | `acs` | brief |

Ordem sugerida de pesquisa, por dependência: dados e eventos, interoperabilidade, grafo de conhecimento, aprendizagem adaptativa, learning analytics e avaliação. Privacidade, segurança e governança corre em paralelo a dados e eventos, porque ambos alimentam as restrições dos demais. Realtime e plataformas são independentes e podem correr em paralelo. Fundamentos pedagógicos é transversal: convém pesquisar cedo, porque define os padrões de evidência que aprendizagem adaptativa, gamificação, plataformas e avaliação usam. Gamificação e jogos depende de dados e eventos (instrumentação) e de aprendizagem adaptativa (dificuldade), e alimenta plataformas (jogos sérios concretos). Acessibilidade, educação especial e DUA é transversal como fundamentos pedagógicos: define requisitos que plataformas, gamificação e aprendizagem adaptativa precisam respeitar, e convém pesquisar junto com fundamentos pedagógicos para fechar a fronteira de DUA e tecnologia assistiva.

## Como contribuir

1. Leia `_modelo/modelo-documental.md` e `_modelo/metodo-e-qualidade.md`.
2. Crie o documento a partir de `_modelo/template-conceito.md`, com id estável e frontmatter completo.
3. Toda afirmação técnica relevante aponta para uma chave da `referencias/bibliografia.bib`. Não invente URL, DOI ou resultado.
4. Registre a fonte em `referencias/indice-fontes.md` com tipo e data de consulta.
5. Passe o documento pelo `_modelo/checklist-revisao.md` antes de marcar `status: revisado`.
6. Atualize o glossário e o mapa de conceitos do domínio.

## Convenções

- Pastas e prosa em português. Identificadores, chaves BibTeX e termos consolidados em inglês, como aparecem na literatura.
- Marcas de afirmação: `[F]` fato com fonte, `[I]` interpretação do autor do documento, `[H]` hipótese ainda não verificada.
- Tipos de fonte: `normativo` (RFC, W3C, IEEE, ISO), `fornecedor` (documentação oficial de produto), `academico` (revisado por pares, livro acadêmico), `tecnico` (artigo ou palestra de referência de praticante), `secundario` (resumo, blog, notícia).
- Recomendações de implementação são sempre marcadas como tal e nunca apresentadas como fato universal.
