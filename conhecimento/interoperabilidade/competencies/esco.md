---
id: iop.comp.esco
titulo: ESCO (European Skills, Competences, Qualifications and Occupations)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [esco2025what, esco2026what, esco2026download, w3c2009skos, credentialengine2026ctdl]
relacoes:
  - { tipo: alternativa-a, alvo: iop.comp.ctdl }
  - { tipo: complementa, alvo: iop.comp.case }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: implementado-por, alvo: kg.std.skos }
  - { tipo: complementa, alvo: kg.curr.competency-frameworks }
  - { tipo: relacionado-a, alvo: kg.found.identifiers-and-triples }
  - { tipo: relacionado-a, alvo: kg.voc.comparison }
termos: [ESCO, classificação, ocupação, habilidade, competência, qualificação, classificação multilíngue, crosswalk, ESCO API, DG EMPL]
---

# ESCO

## Definição e terminologia

"ESCO (European Skills, Competences, Qualifications and Occupations) is the European multilingual classification of Skills, Competences and Occupations." Funciona "as a dictionary, describing, identifying and classifying professional occupations and skills relevant for the EU labour market and education and training". Os conceitos e as relações entre eles "can be understood by electronic systems, which allows different online platforms to use ESCO for services like matching jobseekers to jobs on the basis of their skills, suggesting trainings to people who want to reskill or upskill" [F: esco2026what].

É mantida pela Direção-Geral de Emprego, Assuntos Sociais e Inclusão (DG EMPL) da Comissão Europeia, desenvolvida com partes interessadas, disponível em portal online e consultável gratuitamente [F: esco2025what; esco2026what].

**Versão e escala** [F: esco2025what; esco2026what]:

| Item | Valor |
|---|---|
| Versão corrente | ESCO v1.2.1, atualizada em 10 de dezembro de 2025 (release v6.0.0) |
| Primeira versão completa | ESCO v1, 28 de julho de 2017 |
| Ocupações | 3.039 |
| Habilidades e competências | 13.939, ligadas às ocupações |
| Idiomas | 28 (idiomas oficiais da UE mais islandês, norueguês, ucraniano e árabe) |

Os três pilares, conforme o menu de classificação do portal: ocupações, habilidades e competências, e qualificações [F: esco2025what].

O objetivo declarado é "support job mobility across Europe and therefore a more integrated and efficient labour market, by offering a 'common language' on occupations and skills that can be used by different stakeholders on employment and education and training topics" [F: esco2026what].

## Problema que resolve

Permitir que vagas, currículos, qualificações e programas de formação de países diferentes falem da mesma habilidade, em idiomas diferentes, com o mesmo identificador [I].

## Fundamentos e funcionamento

[I] O que torna ESCO relevante para interoperabilidade e para um grafo de conhecimento educacional não é o conteúdo ocupacional em si, mas três propriedades:

1. **Identificadores estáveis e públicos** para competências. É um conjunto de IRIs de terceiro que se pode referenciar em vez de inventar (ver `kg.found.identifiers-and-triples`).
2. **Multilinguismo nativo** em 28 idiomas [F: esco2026what], o que resolve rótulos sem custo próprio.
3. **Modelagem semântica padrão**. O modelo ESCO, descrito pelo portal como "the semantic model behind the ESCO taxonomy", "uses RDF, OWL and SKOS technologies and it provides domain-specific classes and properties for the labour market"; pode ser acessado em formatos HTML e RDF/XML [F: esco2026download]. Isso torna o alinhamento com um grafo próprio uma questão de `skos:*Match` e não de tradução de esquema [F: w3c2009skos]. (A página "What is ESCO?" não menciona RDF nem SKOS [F: esco2025what]; a confirmação vem da página de download.)

### Distribuição

Os dados podem ser baixados em RDF, TTL, ODS, CSV, XML e JSON-LD, "which allows a wide range of users to use the data in various scenarios and to be integrated into their applications and services" [F: esco2026download]. Há também uma API: a Comissão oferece a ESCO Web Services API e a ESCO Local API, e "the content of the messages exchanged via the APIs is based on the ESCO data model specified in Ontology Web Language (OWL)" [F: esco2026download].

O portal oferece tabelas de mapeamento EURES para países e outros *crosswalks* [F: esco2026what, menu de navegação].

### Limite de aplicabilidade

[I] ESCO é uma classificação **ocupacional**, não curricular. Suas competências são do mercado de trabalho ("soldar", "negociar contratos"), não do currículo escolar ("resolver problemas com frações equivalentes"). Em educação básica a sobreposição é pequena; em educação profissional, técnica e superior ela cresce; em requalificação, ESCO é o vocabulário natural.

Portanto, em um grafo de educação básica, ESCO entra como vocabulário de **destino**, para onde as competências curriculares eventualmente apontam quando se quer falar de empregabilidade, e não como espinha dorsal.

## Requisitos e pressupostos

- O caso de uso é de empregabilidade, qualificação ou formação profissional. Para currículo da educação básica, ESCO não é o vocabulário certo [I].
- Dependência de um vocabulário mantido por terceiro, com ciclo de versão próprio (v1.2.1, release v6.0.0, 10/12/2025) [F: esco2026what]. Mudanças de versão podem alterar ou retirar conceitos.
- Acesso por download ou API [F: esco2026what]. Consulta federada por SPARQL não foi verificada.
- Decisão sobre copiar ou referenciar. [I] Copiar congela a versão e torna o grafo autossuficiente; referenciar mantém atualizado e cria dependência de disponibilidade.

## Vantagens e limitações

Vantagens [I]: gratuito, público, multilíngue por construção (incluindo idiomas fora da UE), mantido por instituição pública estável; escala útil (13.939 competências); disponível por API e download; publicado em RDF/OWL/SKOS, logo integrável sem tradução de modelo; ligado a ocupações, o que dá significado prático às competências.

Limitações [I]:
- Granularidade de mercado de trabalho: habilidades ocupacionais, não objetivos de aprendizagem de crianças; cobertura fraca de currículo escolar.
- Enraizado no contexto europeu (28 idiomas incluem português, mas a perspectiva é do mercado da UE): a correspondência com classificações brasileiras (CBO, catálogos do sistema S) precisa ser construída.
- Versionamento externo é risco de manutenção.

## Alternativas e comparações

| Necessidade | Vocabulário |
|---|---|
| Competências do mercado de trabalho europeu, multilíngue | ESCO [F: esco2026what] |
| Credenciais, competências e trajetórias de aprendizagem e trabalho | CTDL [F: credentialengine2026ctdl]; ver `iop.comp.ctdl` |
| Framework curricular trocável entre sistemas | CASE; ver `iop.comp.case` |
| Currículo nacional brasileiro | BNCC; ver `kg.curr.bncc` |

A tabela comparativa por camada está em `iop.comp.ctdl`; a comparação ampla de vocabulários, em `kg.voc.comparison`.

## Exemplo técnico independente de domínio

```turtle
# alinhamento de uma competência curricular própria a ESCO, sem igualá-las
ex:c/estatistica-descritiva a skos:Concept ;
    skos:prefLabel  "Estatística descritiva"@pt ;
    skos:closeMatch <http://data.europa.eu/esco/skill/XXXXXXXX> .

# proveniência do alinhamento, porque alinhamento é afirmação contextual
GRAPH ex:g/alinhamento-esco-v1.2.1 {
  ex:c/estatistica-descritiva skos:closeMatch <http://data.europa.eu/esco/skill/XXXXXXXX> .
}
ex:g/alinhamento-esco-v1.2.1
    prov:wasAttributedTo ex:agente/curadoria ;
    ex:versaoFonte "ESCO v1.2.1 (release v6.0.0)" .
```

[I] O IRI de ESCO no exemplo é um marcador de posição: o padrão exato de IRI do ESCO não foi verificado. Registrar a versão da fonte no grafo nomeado é a defesa contra o versionamento externo.

## Relações com outros conceitos

Alternativa europeia a `iop.comp.ctdl` no eixo ocupacional; complementa `iop.comp.case`, que cobre currículo; depende de `iop.sem.vocabularios-e-skos`. No domínio do grafo: implementado por `kg.std.skos`; complementa `kg.curr.competency-frameworks`; relaciona-se com `kg.found.identifiers-and-triples`.

## Lacunas e questões abertas

- O padrão de IRI do ESCO e a estrutura exata de suas classes e propriedades não foram verificados: o modelo semântico em RDF/XML não foi aberto, apenas sua descrição na página de download [F: esco2026download].
- A ESCO API não foi consultada; não foi verificado se há endpoint SPARQL além das APIs REST descritas.
- A cobertura de ESCO para competências de educação básica não foi medida.
- Crosswalks entre ESCO e frameworks brasileiros (CBO, BNCC) não foram levantados.
- Relação com ISCO-08 e com o EQF: não mencionada nas páginas consultadas.
- Numeração confusa entre "ESCO v1.2.1" e "release v6.0.0" na própria página [F: esco2025what]; esclarecer qual identifica a classificação e qual identifica o pacote de publicação.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| esco2025what | fornecedor | 2026-10-29 |
| esco2026what | fornecedor | 2026-10-29 |
| esco2026download | fornecedor | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| credentialengine2026ctdl | fornecedor | 2026-10-29 |
