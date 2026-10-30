---
id: dat.relatorio
titulo: Relatório da primeira versão do domínio dados de pesquisa e eventos
tipo: relatorio
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Relatório: primeira versão do domínio dados de pesquisa e eventos

Data: 2026-10-30. Esta é a "primeira versão funcional" pedida por `_modelo/metodo-e-qualidade.md`: estrutura, mapa conceitual, bibliografia inicial e os documentos principais fundamentados em fontes abertas antes de citadas. Todos os documentos estão em `status: rascunho`. A passagem para `revisado` exige o checklist de `_modelo/checklist-revisao.md` por leitor humano.

## Método aplicado

Cinco frentes de pesquisa em paralelo, uma por pasta prevista no brief (`events`, `quality`, `research-data`, `research-ethics`, `datasets`). Cada frente abriu as fontes antes de citá-las e registrou, no texto e na nota BibTeX, quando leu só metadados, só o resumo, um pré-print ou uma cópia hospedada por terceiros. Ids de outros domínios citados em relação foram conferidos no frontmatter real. Cada frente produziu seus documentos e um fragmento de bibliografia e índice (`referencias/fragmentos/dat-*.bib` e `dat-*-indice.md`). Os fragmentos foram mesclados em `referencias/bibliografia.bib` e `referencias/indice-fontes.md` por `_modelo/mesclar_referencias.py`. Os arquivos de índice (README, glossário, mapa, matriz e este relatório) foram sintetizados só a partir dos 20 documentos, sem pesquisa nova. O validador `_modelo/validar.py`, rodado sobre a base inteira, confirma ids únicos com prefixo `dat`, alvos de relação existentes (inclusive os de outros domínios), chaves de fonte presentes na bibliografia e nenhuma menção a produto consumidor.

## Cobertura

| Área | Documentos | Observação |
|---|---|---|
| events | 5 | modelo de evento (CloudEvents, OpenTelemetry, xAPI), telemetria de jogos (Seif El-Nasr et al., Serrano-Laguna et al.), event sourcing e CQRS, OpenTelemetry e W3C Trace Context, mapeamento para xAPI 1.0.3 e 2.0 com perfis |
| quality | 4 | granularidade e construtos (RT, hesitação, trajetória, lei de Fitts), relógios e ordenação (monotônico, parede, NTP, âncora), perda e deduplicação (outbox, `Idempotency-Key`, armazenamento do navegador), esquema (JSON Schema, Avro, Protobuf) |
| research-data | 4 | princípios FAIR e métricas, planos de gestão de dados (FAPESP, H2020, Science Europe), repositórios (Zenodo, Dataverse, OSF) e versionamento, documentação de dataset (datasheet, nutrition label, data statement, DDI, README) |
| research-ethics | 3 | sistema CEP/Conep e Sistema Nacional (Resoluções 466, 510, 674, Lei 14.874/2024, Decreto 12.651/2025), consentimento e assentimento em protocolo, pesquisa versus operação e testes A/B |
| datasets | 4 | PSLC DataShop, ASSISTments, EdNet e comparação com KDD Cup 2010, OULAD, Junyi 2015 e 2020 e Duolingo SLAM |
| raiz | 7 | brief, plano de ids, README, glossário, mapa, matriz comparativa, este relatório |

Totais: 20 documentos de conteúdo (22 contando brief e plano de ids). O mapa de conceitos registra 178 relações tipadas (79 `complementa`, 70 `relacionado-a`, 16 `depende-de`, 6 `parte-de`, 4 `avaliado-por`, 2 `implementado-por`, 1 `especificado-por`); 84 delas apontam para outros domínios, sobretudo `psg`, `lae`, `adp` e `rtm`. Os frontmatters citam 135 chaves de fonte distintas. Os cinco fragmentos têm 116 entradas novas; as outras 19 chaves já existiam na bibliografia, vindas de outros domínios (por exemplo `lamport1978time`, `rfc5905`, `adl2016xapidata`, `wilkinson2016fair`, `brasil2018lgpd`).

Marcas de afirmação no corpo dos 20 documentos, contadas por script: 609 citações de fato com chave (`[F: ...]`), 168 interpretações (`[I]`, incluindo 8 em que a marca I fecha a mesma chave de uma citação de fato), 4 hipóteses (`[H]`). As hipóteses estão em `dat.qual.loss-and-deduplication` (perda concentrada no fim das sessões), `dat.qual.schema-validation-and-evolution` (binário para volume alto), `dat.rd.fair-principles` (metadados persistentes contra pedido de eliminação) e `dat.ds.ednet` (público jovem adulto ou adulto).

## Achado central

Nenhum dataset público de referência verificado cobre crianças dos anos iniciais com eventos cognitivo-motores finos (`dat.ds.comparison`). Nenhum deles traz, ao mesmo tempo: população de cerca de 6 a 10 anos declarada; trajetória de ponteiro ou toque e tempo de reação medido desde o início do estímulo; metadados de relógio e dispositivo; indicadores de deficiência em crianças; documentação de consentimento e assentimento de crianças; dados em português ou de contexto brasileiro. Os datasets servem como referência de formato (DataShop), de evento de interface com tempo em milissegundos (EdNet KT4) e de população escolar mais jovem com latência (ASSISTments), não como base para estudo com essa população. O Junyi 2020 é o candidato mais próximo, mas série escolar e resolução do tempo não foram verificadas.

## O que o brief pediu e onde está

| Entregável | Local |
|---|---|
| Estrutura de diretórios | `dados-pesquisa-e-eventos/` (5 pastas, mais `_plano-ids.md`) |
| README com escopo, organização e convenções | `README.md` deste domínio e `conhecimento/README.md` |
| Glossário técnico | `glossario.md` |
| Mapa conceitual e relações | `mapa-conceitos.md` |
| Documentos técnicos fundamentados | as 5 pastas temáticas |
| Bibliografia BibTeX | fragmentos `dat-*` mesclados em `conhecimento/referencias/bibliografia.bib` |
| Matriz comparativa | `matriz-comparativa.md` |
| Relatório de cobertura e prioridades | este arquivo |

Das fontes prioritárias do brief, k-anonimato (Sweeney) e privacidade diferencial (Dwork) não foram pesquisadas aqui: ficam em `privacidade-seguranca-e-governanca`, conforme o próprio escopo do brief.

## Fontes que não puderam ser verificadas em texto integral

Registradas nas seções "Lacunas" e "Fontes" de cada documento e nas notas dos fragmentos `referencias/fragmentos/dat-*.bib`:

- **events**: o livro "Game Analytics" de Seif El-Nasr, Drachen e Canossa (2013) só por metadados, e a classificação de métricas citada por revisão aberta; o capítulo de Zoeller só pelo resumo; "Designing Data-Intensive Applications" de Kleppmann só por metadados; o livro de Young está marcado pela própria página como 90 % completo (2017); o texto pago da IEEE 9274.1.1-2023 não foi lido, usou-se o texto base aberto do grupo de trabalho; Serrano-Laguna et al. lido em pré-print; o registro xapi.vocab.pub não respondeu; a data de publicação da CloudEvents 1.0.2 e o estado da Trace Context Level 2 não foram verificados.
- **quality**: Fitts (1954) e a ISO/TS 9241-411 só por metadados, com valores tirados de MacKenzie (1992); documentação de relógios e toque do iOS não aberta; o bug de `performance.now()` em suspensão só pela nota da MDN; especificações W3C de Background Sync e Storage não abertas; `Idempotency-Key` é rascunho IETF -08; JSON Schema 2020-12 circula como Internet-Draft expirado; tabelas de compatibilidade do Confluent lidas de forma parcial.
- **research-data**: diretrizes da FAPESP para centros (CEPID, CPE, CPD) não abertas; página principal da FAPESP sem data; modelo H2020 lido em cópia de biblioteca universitária e modelo Horizon Europe não aberto; exigências de CAPES e CNPq não encontradas; Gebru et al. lido no arXiv v8, versão CACM só por metadados; elementos do DDI-Codebook 2.5 não abertos; nomes de `relationType` do DataCite 4.7 não confirmados; controle de acesso e DOI do OSF não verificados; guia da Cornell e página da GO FAIR sem data; versão do DVC não registrada.
- **research-ethics**: Anexo II da Resolução 674/2022 ilegível na cópia consultada, e a vigência plena da resolução depende da Plataforma Brasil; posse e normas da Instância Nacional não verificadas; ação direta de inconstitucionalidade contra a lei citada em buscas e não verificada em fonte primária; manual da Plataforma Brasil, Carta Circular 1/2021 e Ofício Circular 2/2021 da Conep não abertos; Kitto e Knight (2019) e Meyer (2015) só pelo resumo; Slade e Prinsloo (2013) só por metadados; Resolução 674 e guia da ANPD lidos em cópias hospedadas por instituições de terceiros.
- **datasets**: total atual de datasets e transações do DataShop não localizado (página de métricas não carregou); histórico de formatos de exportação não aberto; número de alunos do KDD Cup 2010 e da competição ASSISTments 2017 não verificado; contagens ASSISTments 2012 e 2015 de terceiros; método de geração dos ids e unidade de `cursor_time` do EdNet não declarados; página do Junyi 2020 lida só pela API de metadados; contagens e unidades do Junyi 2015 em parte por fonte secundária.

## Lacunas de conhecimento consolidadas

1. **Medição de tempo em dispositivos de crianças.** Não há medição de lag e jitter de RT em tablets e celulares usados por crianças, nem método leve de calibração da latência de toque em campo (`dat.qual.granularity-and-constructs`).
2. **Taxa de amostragem mínima de trajetória.** O valor de 60 a 75 Hz é o de uma ferramenta, não um limiar demonstrado para desvio máximo, área sob a curva e inversões (`dat.qual.granularity-and-constructs`).
3. **Fonte do relógio no envelope.** Nenhuma especificação lida padroniza a declaração da fonte de relógio e do desvio, nem da configuração ativa (`dat.ev.event-model`, `dat.ev.instrumentation-and-opentelemetry`).
4. **Perfil xAPI para medidas motoras.** Não foi verificado se existe perfil publicado para tempo de reação ou trajetória (`dat.ev.event-to-xapi-mapping`).
5. **Perda em coleta educacional.** Falta evidência empírica de quanto se perde no fim das sessões e se a perda se associa a características dos participantes; aplicações nativas não foram pesquisadas (`dat.qual.loss-and-deduplication`).
6. **Mudança de significado sem mudança de forma.** Nenhuma regra de compatibilidade de esquema detecta nova definição operacional de um campo (`dat.qual.schema-validation-and-evolution`).
7. **Metadados públicos de datasets de crianças.** Não há orientação de órgão brasileiro sobre o que pode constar no registro público; nem modelo de datasheet para dados de interação de crianças (`dat.rd.fair-principles`, `dat.rd.data-documentation`).
8. **Eliminação em repositórios e logs.** O Zenodo preserva arquivos retirados da vista pública; o Dataverse não destrói automaticamente; não se sabe se comitês aceitam crypto-shredding como eliminação (`dat.rd.repositories-and-versioning`, `dat.ev.event-sourcing`).
9. **Regime ético em transição.** Prazos da lei (dias úteis) e da resolução (dias) não coincidem; critérios de risco dependem de norma da Instância Nacional; forma do assentimento na lei ainda não harmonizada com o registro da 510 (`dat.ethics.cep-conep-system`, `dat.ethics.consent-and-assent-in-research`).
10. **Experimentos contínuos de produto.** Não há norma brasileira específica; o enquadramento de teste A/B com alunos identificados como tipo C1 é interpretação (`dat.ethics.research-vs-operation`).
11. **Datasets com crianças pequenas.** Não foi feita busca sistemática por datasets de leitura inicial ou jogos educativos, nem dentro do DataShop (`dat.ds.comparison`).

## Pontos para o revisor humano

- `dat.rd.fair-principles` e `dat.rd.repositories-and-versioning` declaram `implementado-por` uma para a outra; pela semântica do modelo documental, só a direção FAIR → repositórios se sustenta.
- `dat.ev.event-model` declara `complementa` para `dat.qual.clocks-and-ordering`, `dat.qual.loss-and-deduplication` e `dat.qual.schema-validation-and-evolution`, que declaram `parte-de` de volta.
- Na tabela de granularidade mínima de `dat.qual.granularity-and-constructs`, a faixa "lag de 25 a 45 ms além do nativo em estudos anteriores" é atribuída a Bridges et al. e Anwyl-Irvine et al., mas não aparece no corpo do documento.
- `dat.ev.event-model` e `dat.qual.clocks-and-ordering` leem de forma diferente a regra da CloudEvents para `time` não determinável (mesmo algoritmo por `source`, ou preenchimento com o tempo atual); convém harmonizar.
- O exemplo de `dat.rd.repositories-and-versioning` registra novo DOI para versão maior; isso vale para o Zenodo, não para o Dataverse, que mantém um identificador por dataset.

## Respostas às perguntas abertas do brief

| Pergunta | Resposta nesta versão | Id |
|---|---|---|
| Qual a granularidade mínima de evento que preserva construtos cognitivo-motores? | Parcial. Registrar no nível de entrada: início do estímulo pelo quadro e resposta na mesma origem monotônica; amostras coalescidas de ponteiro com x, y e tipo; coordenada do ponto final, inclusive em erros; número de sequência por sessão; covariáveis de dispositivo por sessão. O lag técnico é tolerável para diferenças intraparticipante e problemático para RT absoluto entre dispositivos. Não há limiar de amostragem demonstrado. | dat.qual.granularity-and-constructs, dat.qual.clocks-and-ordering |
| Como conciliar FAIR com proteção de dados de menores? | Respondida nas fontes: FAIR não exige abertura. Metadados públicos, sem dado pessoal e sem permitir reidentificação; dados em acesso controlado, com caminho claro de pedido (A1.2, A2, R1.1); repositório com arquivos restritos e metadados abertos. | dat.rd.fair-principles, dat.rd.repositories-and-versioning |
| Que esquema de evento permite mapeamento sem perda para xAPI? | Respondida como síntese: um esquema interno que é superconjunto do statement, com destino declarado em extensão de IRI controlado para o que o xAPI não tem (tempo em ns, sequência, versão de esquema, configuração, fonte de relógio), validado por perfil, com o log interno como fonte de verdade e o LRS como projeção. A perda ocorre em tempo sub-milissegundo, fuso local, duração e propriedades fora dos pontos de extensão. | dat.ev.event-to-xapi-mapping, dat.ev.event-model |
| Quais requisitos específicos a FAPESP impõe a planos de gestão de dados? | Respondida: texto de até duas páginas (centros: cinco), em PDF, com quatro itens (dados e metadados; restrições legais e éticas; preservação e compartilhamento com período de carência; mecanismos e formatos); exigido de todo projeto exceto PIPE e IC segundo o FAQ; link ou DOI no relatório final; páginas pessoais e drives não valem. As duas páginas da FAPESP divergem no escopo da obrigatoriedade. | dat.rd.data-management-plans |

## Próximos passos sugeridos

1. **Revisão humana** dos 20 documentos com o checklist, começando pelos pontos da seção anterior e pelos documentos com mais fontes só por metadados ou resumo (`dat.ev.game-telemetry`, `dat.ethics.research-vs-operation`, `dat.qual.granularity-and-constructs`).
2. **Medição própria de tempo** em tablets e celulares típicos de escola, com cronometria externa, para fechar a lacuna 1, já que nenhuma fonte a cobre.
3. **Busca sistemática de datasets com crianças pequenas**, inclusive dentro do DataShop, e verificação de série e tempo do Junyi 2020.
4. **Segunda rodada de fontes** com acesso institucional: livro de Game Analytics, IEEE 9274.1.1-2023, diretrizes da FAPESP para centros, Anexo II da Resolução 674, normas da Instância Nacional.
5. **Ficha de dataset própria**: modelo de datasheet e dicionário para dados de interação de crianças, combinando `dat.rd.data-documentation` com a ficha de candidato de `dat.ds.comparison`.
6. **Conversão para grafo.** Com ids, relações tipadas e termos no frontmatter, um script pode gerar SKOS a partir dos arquivos, junto com o domínio `grafo-conhecimento-educacional`, como já registrado nos relatórios de outros domínios.
