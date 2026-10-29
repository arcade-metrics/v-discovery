---
id: kg.mod.layer-separation
titulo: Separação entre grafo conceitual, modelo do aluno e dados observados
tipo: conceito
dominio: grafo-conhecimento-educacional
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hogan2021knowledgegraphs, w3c2014rdf11concepts, w3c2013provo, abdelmagied2025graphrag, alatrash2025prerequisite, noy2001ontology101]
relacoes:
  - { tipo: parte-de, alvo: kg.mod.conceptual-model }
  - { tipo: depende-de, alvo: kg.found.identifiers-and-triples }
  - { tipo: complementa, alvo: kg.mod.evidence-and-mastery }
  - { tipo: complementa, alvo: kg.found.context-and-reification }
  - { tipo: relacionado-a, alvo: kg.eng.versioning-and-provenance }
  - { tipo: relacionado-a, alvo: kg.ret.graph-rag }
  - { tipo: complementa, alvo: adp.lm.learner-model }
  - { tipo: complementa, alvo: adp.id.knowledge-components }
termos: [grafo conceitual, modelo do aluno, learner model, personal knowledge graph, dados observados, telemetria, camada, ritmo de mudança, LGPD]
---

# Separação entre grafo conceitual, modelo do aluno e dados observados

## Definição e terminologia

Três coisas diferentes costumam ser chamadas de "grafo de conhecimento educacional":

1. **Grafo conceitual educacional**: conceitos, competências, objetivos, recursos, instrumentos e as relações entre eles. É o mapa do domínio, igual para todos os alunos.
2. **Modelo individual de aprendizagem**: o estado estimado de um aluno em relação a esse mapa — o que domina, com que confiança, o que está pronto para aprender. É derivado, probabilístico e individual.
3. **Dados observados**: os eventos brutos — respostas, tempos, tentativas, sessões. São fatos registrados, imutáveis, com timestamp.

A literatura consultada já opera com essa distinção, ainda que sem nomeá-la assim: Abdelmagied et al. descrevem um pipeline de Graph RAG que usa "Educational Knowledge Graphs (EduKGs) **and** Personal Knowledge Graphs (PKGs)" [F: abdelmagied2025graphrag, resumo]. [I] São dois grafos, não um.

O domínio `aprendizagem-adaptativa` desta base chega à mesma fronteira pelo outro lado: o documento adp.lm.learner-model registra que um learner model "não é o modelo de domínio (a representação do conteúdo a aprender), não é o registro bruto de eventos de interação, e não é um dashboard". Camada 1 é o modelo de domínio daquele documento; camada 2, o learner model; camada 3, o registro bruto. A unidade que liga as duas bases é o knowledge component (adp.id.knowledge-components), que aqui aparece como conceito ou competência do grafo conceitual. [I]

## Problema que resolve

[I] Misturar as três em um grafo só cria quatro problemas simultâneos, e todos aparecem tarde:

| Problema | O que acontece |
|---|---|
| Ritmo de mudança | o grafo conceitual muda por curadoria, em meses; o modelo do aluno muda a cada resposta. Versionar um congela o outro. |
| Volume | conceitos são milhares; observações são bilhões. Otimizar o armazenamento para um prejudica o outro. |
| Proveniência e autoridade | uma aresta curricular é afirmada por curadoria humana; uma estimativa de domínio é calculada por um modelo. Sem separação, as duas se tornam indistinguíveis. |
| Privacidade | o grafo conceitual é publicável; os dados do aluno são pessoais e regulados. Um grafo único obriga o regime mais restritivo para tudo. |

O quarto é decisivo e não é técnico: **o grafo conceitual quer ser publicado; os dados do aluno não podem ser.** [I]

## Fundamentos e funcionamento

### As três camadas em detalhe

| | Grafo conceitual | Modelo do aluno | Dados observados |
|---|---|---|---|
| Entidades | conceito, competência, objetivo, recurso, instrumento, item | aluno × conceito | evento, resposta, sessão |
| Natureza das arestas | afirmadas por curadoria ou extração | derivadas por inferência estatística | nenhuma; são registros |
| Mutabilidade | baixa, por versão | alta, contínua | imutável (append-only) |
| Volume | 10³–10⁵ nós [I] | alunos × conceitos | 10⁶–10⁹+ registros [I] |
| Autoridade | curadoria humana | modelo | instrumento |
| Publicável | sim, é desejável | não | não |
| Regime de dados | aberto | pessoal, sensível | pessoal |
| Tecnologia adequada | grafo (RDF ou propriedades) | grafo ou armazenamento chave-valor | armazenamento colunar ou de eventos |

### Como se relacionam

[I] As camadas se ligam por referência, não por fusão:

```
Dados observados  --referenciam-->  itens e conceitos do Grafo conceitual
Modelo do aluno   --referenciam-->  conceitos do Grafo conceitual
Modelo do aluno   --derivado de-->  Dados observados
```

A chave de ligação é o identificador de conceito. Isso torna o esquema de IRI do grafo conceitual uma dependência de todas as três camadas — e reforça a regra de que um id publicado nunca muda (ver kg.found.identifiers-and-triples).

### Por que isso não contradiz "um grafo de conhecimento"

Hogan et al. observam que gerir vários grafos em vez de um monolítico é frequentemente desejável, permitindo atualizar ou refinar dados de uma fonte, distinguir fontes não confiáveis das confiáveis, e assim por diante; um *graph dataset* consiste em um conjunto de grafos nomeados mais um grafo padrão [F: hogan2021knowledgegraphs, §2.1.4]. RDF já oferece essa estrutura nativamente [F: w3c2014rdf11concepts, §4].

[I] Ou seja: a separação proposta aqui não é uma renúncia ao modelo de grafo; é o uso do mecanismo que o próprio modelo fornece. As três camadas podem viver em um mesmo *dataset*, em grafos nomeados distintos, com políticas distintas — ou em sistemas distintos, se o volume exigir.

### Onde a proveniência entra

Cada camada tem uma pergunta de proveniência própria [I]:

- Grafo conceitual: *quem afirmou isso e com base em quê*. PROV-O por lote de curadoria [F: w3c2013provo].
- Modelo do aluno: *que modelo, que versão, com que dados de entrada, quando*. A estimativa sem o modelo que a produziu não é auditável.
- Dados observados: *que instrumento, que sessão, que instante*. Imutável por construção.

## Requisitos e pressupostos

- Identificadores estáveis de conceito, compartilhados pelas três camadas.
- Uma política explícita de retenção e acesso por camada, dada a diferença de regime de dados pessoais. [I] A legislação aplicável (no Brasil, a LGPD) não foi analisada nesta sessão; o ponto aqui é arquitetural, não jurídico.
- Aceitação de que o modelo do aluno é derivado e descartável: deve poder ser recomputado a partir dos dados observados. Se não puder, virou fonte primária por acidente.

## Vantagens e limitações

Vantagens: cada camada escolhe sua tecnologia, seu ritmo de versão e seu regime de acesso; o grafo conceitual pode ser publicado e reusado; o modelo do aluno pode ser recomputado quando o algoritmo melhora; auditoria é possível porque afirmado, observado e derivado não se confundem.

Limitações: três sistemas em vez de um; consultas que atravessam camadas exigem junção; consistência referencial entre camadas precisa ser garantida explicitamente (um conceito removido do grafo conceitual deixa órfãs as estimativas que o referenciam). [I]

## Alternativas e comparações

| Arranjo | Quando serve | Risco |
|---|---|---|
| Grafo único com tudo | protótipo, escala pequena, um só time | o regime mais restritivo vale para tudo; versionamento trava |
| Grafos nomeados no mesmo dataset | escala média; todas as camadas cabem em um triplestore | volume de observações pode inviabilizar |
| Sistemas separados com referência por IRI | escala de produção | junção entre camadas é por aplicação |
| Grafo conceitual publicado + resto privado | quando a publicação é objetivo | exige disciplina para não vazar referência identificável |

[I] Tabela proposta por este documento; nenhuma fonte consultada a apresenta.

## Exemplo técnico independente de domínio

```trig
# Camada 1: grafo conceitual — publicável
GRAPH ex:g/conceitual/v3 {
  ex:c/8f3a a skos:Concept ; skos:prefLabel "Frações equivalentes"@pt .
  ex:c/8f3a ex:preRequisitoDe ex:c/1b2c .
  ex:item/221 ex:avalia ex:c/8f3a .
}
ex:g/conceitual/v3 prov:wasAttributedTo ex:agente/curadoria .

# Camada 3: dados observados — imutável, pessoal
GRAPH ex:g/observado {
  ex:resp/9f81 a ex:Resposta ;
      ex:aluno    ex:aluno/1234 ;
      ex:item     ex:item/221 ;
      ex:correta  true ;
      ex:instante "2026-10-29T14:03:11Z"^^xsd:dateTime .
}

# Camada 2: modelo do aluno — derivado, recomputável, pessoal
GRAPH ex:g/modelo/2026-10-29 {
  ex:est/aluno1234-c8f3a a ex:EstimativaDeDominio ;
      ex:aluno       ex:aluno/1234 ;
      ex:conceito    ex:c/8f3a ;
      ex:probabilidade 0.82 .
}
ex:g/modelo/2026-10-29
    prov:wasGeneratedBy  ex:atividade/estimativa-2026-10-29 ;
    prov:used            ex:g/observado , ex:g/conceitual/v3 .
```

[I] Repare no `prov:used` do último bloco: a estimativa declara de que versão do grafo conceitual e de que dados ela derivou. É o que torna possível responder "por que o sistema achou isso em outubro" depois que o currículo mudou.

## Relações com outros conceitos

Parte de kg.mod.conceptual-model. Depende de kg.found.identifiers-and-triples (a chave que liga as camadas). Complementa kg.mod.evidence-and-mastery (o detalhe da camada 2 e 3) e kg.found.context-and-reification. Relaciona-se com kg.eng.versioning-and-provenance e kg.ret.graph-rag (onde EduKG e PKG aparecem juntos na literatura). Atravessa domínio: complementa adp.lm.learner-model (a camada 2 vista de dentro da aprendizagem adaptativa) e adp.id.knowledge-components (a unidade compartilhada pelas duas bases).

## Lacunas e questões abertas

- A separação proposta é recomendação deste domínio, apoiada em propriedades documentadas dos modelos de grafo [F: hogan2021knowledgegraphs, §2.1.4] e na observação de que a literatura já trabalha com EduKG e PKG distintos [F: abdelmagied2025graphrag], mas **não é afirmada como prática estabelecida por nenhuma fonte consultada**.
- Os números de volume na tabela são estimativas de ordem de grandeza, não medições.
- Como manter consistência referencial quando o grafo conceitual versiona e as estimativas apontam para a versão anterior é problema aberto. [H] Apontar sempre para o IRI estável do conceito, e não para a versão, resolve a maioria dos casos; conceitos removidos continuam problemáticos.
- O enquadramento jurídico (LGPD) das três camadas não foi analisado; pertence ao domínio `dados-pesquisa-e-eventos`.
- Noy e McGuinness lembram que a melhor solução depende da aplicação pretendida [F: noy2001ontology101, §3]: para um protótipo pequeno, a separação em três pode ser custo sem retorno.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hogan2021knowledgegraphs | academico | 2026-10-29 |
| w3c2014rdf11concepts | normativo | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| abdelmagied2025graphrag | academico | 2026-10-29 |
| alatrash2025prerequisite | academico | 2026-10-29 |
| noy2001ontology101 | academico | 2026-10-29 |
