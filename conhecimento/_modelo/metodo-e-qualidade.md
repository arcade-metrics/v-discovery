# Método de pesquisa e critérios de qualidade

## Método, por área

1. Identifique os conceitos fundamentais e a terminologia consolidada.
2. Localize as fontes primárias e os padrões aplicáveis.
3. Registre as evidências e suas limitações.
4. Compare abordagens, tecnologias e alternativas.
5. Identifique lacunas de conhecimento e questões ainda abertas.
6. Produza documentos com referências verificáveis.
7. Revise consistência, duplicações e relações entre documentos.

Não se limite a resumir páginas. Construa uma estrutura coerente e navegável: um conceito por documento, relações tipadas entre eles.

## Prioridade de fontes

1. Especificações normativas (RFC, W3C, IEEE, ISO).
2. Documentação oficial da tecnologia estudada, com versão.
3. Artigos revisados por pares e livros acadêmicos.
4. Artigos e palestras técnicas de referência (praticantes reconhecidos, conferências como GDC).
5. Fontes secundárias, apenas quando agregam algo que as anteriores não têm.

Não invente referência, DOI, URL ou resultado experimental. Se não conseguiu verificar, escreva "não verificado" e deixe a lacuna registrada.

## Qualidade e rastreabilidade

- Toda afirmação técnica relevante possui fonte verificável.
- Diferencie especificação normativa, documentação de fornecedor e opinião técnica.
- Registre versões e datas quando a informação depender delas.
- Preserve citações completas e links para as fontes originais.
- Evite duplicação de conceitos e inconsistências terminológicas; o glossário é a referência.
- Não apresente recomendação de implementação como fato universal.
- Nenhum documento cita produto ou projeto consumidor da base.

## Interoperabilidade futura

A base é independente de qualquer aplicação, mas preparada para integração com grafos de conhecimento. Identificadores persistentes, relações tipadas e frontmatter estruturado permitem gerar RDF/SKOS a partir dos arquivos. Não é necessário implementar ontologia completa agora; é necessário não bloquear essa conversão.

## Primeira versão funcional antes de expandir

Cada domínio entrega primeiro: estrutura, mapa conceitual, bibliografia inicial e os documentos principais fundamentados em fontes verificadas. Só depois expande cobertura.
