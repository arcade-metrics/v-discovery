---
id: iop.comp.esco
titulo: ESCO (European Skills, Competences, Qualifications and Occupations)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [esco2025what, w3c2009skos]
relacoes:
  - { tipo: alternativa-a, alvo: iop.comp.ctdl }
  - { tipo: complementa, alvo: iop.comp.case }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
termos: [classificação, ocupação, habilidade, qualificação, multilíngue]
---

# ESCO

## Definição e terminologia

ESCO é a classificação europeia de habilidades, competências, qualificações e ocupações: um dicionário multilíngue de ocupações e habilidades para o mercado de trabalho e para a educação e formação na União Europeia [F: esco2025what].

É mantida pela DG Employment, Social Affairs and Inclusion (DG EMPL) da Comissão Europeia, desenvolvida com partes interessadas [F: esco2025what].

**Versão e escala** [F: esco2025what]:

| Item | Valor |
|---|---|
| Versão | ESCO v1.2.1, atualizada em 10 de dezembro de 2025 (release v6.0.0) |
| Primeira versão completa | ESCO v1, 28 de julho de 2017 |
| Ocupações | 3.039 |
| Habilidades | 13.939, ligadas às ocupações |
| Idiomas | 28 (idiomas oficiais da UE mais islandês, norueguês, ucraniano e árabe) |

Os três pilares, conforme o menu de classificação da página: ocupações, habilidades e competências, e qualificações [F: esco2025what].

## Problema que resolve

Permitir que vagas, currículos, qualificações e programas de formação de países diferentes falem da mesma habilidade, em idiomas diferentes, com o mesmo identificador [I].

## Fundamentos e funcionamento

A classificação é disponibilizada por portal online, com download da versão corrente e uma API própria [F: esco2025what]. A estrutura de classificação multilíngue com relações entre conceitos é exatamente o caso de uso do SKOS [F: w3c2009skos] [I]; a página consultada, porém, não menciona RDF nem SKOS [F: esco2025what].

## Requisitos e pressupostos

- O caso de uso é de empregabilidade, qualificação ou formação profissional. Para currículo da educação básica, ESCO não é o vocabulário certo [I].

## Vantagens e limitações

Vantagens [I]: multilíngue por construção, incluindo idiomas fora da UE; mantido por instituição pública estável; disponível por API e download.

Limitações [I]:
- Granularidade de mercado de trabalho: habilidades ocupacionais, não objetivos de aprendizagem de crianças.
- Enraizado no contexto europeu: a correspondência com classificações brasileiras (CBO, catálogos do sistema S) precisa ser construída.
- Não verificado se a publicação é feita em RDF/SKOS, o que afetaria a estratégia de integração em grafo.

## Alternativas e comparações

Ver a tabela em `iop.comp.ctdl`.

## Relações com outros conceitos

Alternativa europeia a `iop.comp.ctdl` no eixo ocupacional; complementa `iop.comp.case`, que cobre currículo. Depende de `iop.sem.vocabularios-e-skos`.

## Lacunas e questões abertas

- Relação com ISCO-08 e com o EQF: não mencionada na página consultada.
- Formato de publicação (RDF/SKOS?) e URIs dos conceitos: não verificados.
- Numeração confusa entre "ESCO v1.2.1" e "release v6.0.0" na própria página [F: esco2025what]; esclarecer qual identifica a classificação e qual identifica o pacote de publicação.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| esco2025what | fornecedor | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
