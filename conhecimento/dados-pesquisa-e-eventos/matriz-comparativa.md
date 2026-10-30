---
id: dat.matriz
titulo: Matriz comparativa do domínio dados de pesquisa e eventos
tipo: comparacao
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Matriz comparativa do domínio dados de pesquisa e eventos

Doze comparações centrais do domínio, em tabelas. Cada célula traz entre parênteses o id do documento que a sustenta e, quando o documento cita, a chave da fonte em `referencias/bibliografia.bib`. Células marcadas [I] são síntese do documento citado, não fato de fonte. Nada aqui acrescenta fato que não esteja nos documentos.

## 1. Envelope de evento: CloudEvents x OpenTelemetry x xAPI

| Critério | CloudEvents 1.0.2 | OpenTelemetry (EventRecord) | xAPI statement |
|---|---|---|---|
| Identidade | `source` + `id` único por evento distinto; reenvio pode repetir o `id` (dat.ev.event-model; cncf2026cloudevents) | sem id obrigatório (dat.ev.event-model; otel2026logsdatamodel) | `id` UUID, recomendado gerado pelo emissor (dat.ev.event-to-xapi-mapping; adl2016xapidata) |
| Relógios | um: `time`, opcional, instante da ocorrência (dat.ev.event-model; cncf2026cloudevents) | dois: `Timestamp` (relógio de origem) e `ObservedTimestamp` (coletor) (dat.ev.instrumentation-and-opentelemetry; otel2026logsdatamodel) | dois: `timestamp` (experiência) e `stored`, sempre sobrescrito pelo LRS (dat.ev.event-to-xapi-mapping; adl2016xapidata) |
| Formato e precisão do tempo | RFC 3339 (dat.qual.clocks-and-ordering; cncf2026cloudevents) | nanossegundos desde a época UNIX (dat.ev.event-model; otel2026logsdatamodel) | ao menos milissegundos, pode truncar além; na 2.0 o LRS pode truncar ou arredondar a 3 casas e converte para UTC; `duration` até 0,01 s (dat.ev.event-to-xapi-mapping; adl2016xapidata, ieee2026xapibasedocs) |
| Fonte do relógio declarada | não (dat.ev.event-model) | não (dat.ev.event-model) | não (dat.ev.event-model) |
| Versão de esquema | `dataschema`, ou versão no `type` (dat.ev.event-model; cncf2026cloudevents) | Schema URL do recurso (dat.ev.event-model; otel2026schemas) | `version` da especificação; conteúdo em `context.revision` (dat.ev.event-model; adl2016xapidata) |
| Correlação | extensão `traceparent` (dat.ev.instrumentation-and-opentelemetry; cncf2026cloudeventsdt) | trace/span e `session.id` (dat.ev.instrumentation-and-opentelemetry; otel2026semconvsession) | `registration`, `contextActivities` (dat.ev.instrumentation-and-opentelemetry) |
| Vocabulário de domínio | nenhum (dat.ev.event-model) | técnico; `EventName` de baixa cardinalidade (dat.ev.instrumentation-and-opentelemetry; otel2026semconvevents) | actor-verb-object, aberto, por perfis (dat.ev.event-to-xapi-mapping; adl2017xapiprofiles) |
| Situação | 1.0.2; intermediários só garantem 64 KByte (dat.ev.event-model; cncf2026cloudevents) | convenções de eventos e de sessão em *Development* (dat.ev.instrumentation-and-opentelemetry) | 1.0.3 e 2.0 (IEEE 9274.1.1-2023) (dat.ev.event-to-xapi-mapping; ieee2023xapi) |

Nenhum dos três registra qual relógio produziu o carimbo nem seu desvio; para evidência, isso vai para extensão [I] (dat.ev.event-model).

## 2. Persistência: CRUD x log append-only x event sourcing

| Critério | CRUD com estado atual | Log de eventos append-only, sem reidratar entidades | Event sourcing completo + CQRS |
|---|---|---|---|
| Histórico | nenhum (dat.ev.event-sourcing) | completo para eventos (dat.ev.event-sourcing) | completo, fonte de verdade (dat.ev.event-sourcing; fowler2005eventsourcing) |
| Complexidade | baixa (dat.ev.event-sourcing) | média (dat.ev.event-sourcing) | alta; CQRS acrescenta "risky complexity" na maioria dos sistemas (dat.ev.event-sourcing; fowler2011cqrs) |
| Uso indicado | dados de referência, perfis (dat.ev.event-sourcing; microsoft2026eventsourcing) | coleta de pesquisa; a operação pode continuar CRUD [I] (dat.ev.event-sourcing) | domínio com regras e replay de estado; desaconselhado para protótipos e MVPs (dat.ev.event-sourcing; microsoft2026eventsourcing) |
| Novas perguntas a dados antigos | não [I] (dat.ev.event-sourcing) | sim, por nova projeção [I] (dat.ev.event-sourcing) | sim, consulta temporal e replay (dat.ev.event-sourcing; fowler2005eventsourcing) |
| Correção | sobrescrita | evento compensatório [I] (dat.ev.event-sourcing) | evento compensatório ou upcaster; o original permanece (dat.ev.event-sourcing; microsoft2026eventsourcing) |
| Consistência e consulta | — | — | consistência eventual; consulta ad hoc exige projeção (dat.ev.event-sourcing; microsoft2026eventsourcing) |
| Eliminação de dado pessoal | — | — | conflito com o log imutável; dados pessoais fora do store ou crypto-shredding (dat.ev.event-sourcing; microsoft2026eventsourcing) |

## 3. Estratégias de carimbo de tempo

| Estratégia | Intervalos na sessão | Calendário | Ordem entre dispositivos | Risco principal |
|---|---|---|---|---|
| Só relógio de parede por evento | sujeitos a step acima de 125 ms (dat.qual.clocks-and-ordering; rfc5905) | sim | não; erro de dezenas de ms (dat.qual.clocks-and-ordering; rfc5905) | saltos e intervalos negativos [I] (dat.qual.clocks-and-ordering) |
| Só monotônico | exatos na resolução do relógio (dat.qual.clocks-and-ordering; w3c2026hrtime) | não | não | perda de âncora no calendário [I] (dat.qual.clocks-and-ordering) |
| Monotônico + sequência + âncora + recebimento no servidor | exatos [I] | derivado da âncora | causal, com sequenciador ou relógio lógico (dat.qual.clocks-and-ordering; lamport1978time) | sono e abas ocultas (dat.qual.clocks-and-ordering; mdn2026performancenow, mdn2026requestanimationframe) |
| Tempo do servidor estimado por offset | erro do offset | sim | aproximada | assimetria de rota, ver `rtm.net.clock-synchronization` (dat.qual.clocks-and-ordering) |

A terceira linha é a recomendação do domínio [I] (dat.qual.clocks-and-ordering). A resolução do carimbo no navegador é covariável: pelo menos 100 µs, ou 5 µs com isolamento de origem cruzada (dat.qual.granularity-and-constructs; w3c2026hrtime).

## 4. Estratégias de deduplicação e perda

| Mecanismo | Protege contra | Não protege contra |
|---|---|---|
| `id` por evento (`source` + `id`) | duplicata após reenvio (dat.qual.loss-and-deduplication; cncf2026cloudevents) | perda |
| Sequência por sessão e produtor | lacuna e reordenação na sessão [I] (dat.qual.loss-and-deduplication) | perda da sessão inteira |
| `Idempotency-Key` por lote | duplicação de lote por resposta perdida (dat.qual.loss-and-deduplication; jena2026idempotencykey) | duplicata de evento entre lotes diferentes |
| Outbox local em IndexedDB | perda por falha de rede (dat.qual.loss-and-deduplication; richardson2026transactionaloutbox) | evicção do armazenamento, durabilidade relaxada (dat.qual.loss-and-deduplication; mdn2026usingindexeddb) |
| Background Sync | envio só com a aplicação aberta (dat.qual.loss-and-deduplication; mdn2026backgroundsync) | navegadores sem suporte |
| Armazenamento persistente | evicção por pressão ou inatividade (dat.qual.loss-and-deduplication; mdn2026storagequotas) | apagamento pelo usuário |
| UUID determinístico do statement a partir de `source` + `id` | duplicata na projeção xAPI [I] (dat.ev.event-to-xapi-mapping) | — |
| Consumidor idempotente com último número de sequência processado | entrega pelo menos uma vez às projeções (dat.ev.event-sourcing; microsoft2026eventsourcing) | — |

O `Idempotency-Key` é rascunho IETF -08, não RFC (dat.qual.loss-and-deduplication; jena2026idempotencykey).

## 5. Formatos de esquema: JSON Schema x Avro x Protocol Buffers

| Critério | JSON Schema 2020-12 | Avro 1.12.0 | Protocol Buffers (proto3) |
|---|---|---|---|
| Identidade do campo | nome (dat.qual.schema-validation-and-evolution) | nome, com aliases (dat.qual.schema-validation-and-evolution; apache2026avrospec) | número (dat.qual.schema-validation-and-evolution; google2026protobufproto3) |
| Leitura de versão antiga | depende do modelo de conteúdo aberto ou fechado (dat.qual.schema-validation-and-evolution; confluent2026schemaevolution) | resolução escritor/leitor com defaults; sem default, erro (dat.qual.schema-validation-and-evolution; apache2026avrospec) | campos desconhecidos preservados (dat.qual.schema-validation-and-evolution; google2026protobufproto3) |
| Remoção de campo | `deprecated` é só anotação (dat.qual.schema-validation-and-evolution; jsonschema2022validation) | seguro se o leitor tiver default ou ignorar (dat.qual.schema-validation-and-evolution; apache2026avrospec) | reservar número e nome; reuso causa corrupção (dat.qual.schema-validation-and-evolution; google2026protobufproto3) |
| Validação de formato | `format` é anotação por padrão (dat.qual.schema-validation-and-evolution; jsonschema2022validation) | — | — |
| Legível sem ferramenta | sim [I] | não, binário com esquema [I] | não, binário [I] |
| Situação do texto | Internet-Draft de 2022 (dat.qual.schema-validation-and-evolution; jsonschema2022core) | especificação do projeto | guia oficial do projeto |

Para dados relidos anos depois, a compatibilidade transitiva é a que garante leitura de todas as versões antigas; o padrão do registro é BACKWARD, não transitivo (dat.qual.schema-validation-and-evolution; confluent2026schemaevolution). Binários para volume alto de amostras é hipótese [H] (dat.qual.schema-validation-and-evolution).

## 6. Tempo de reação: laboratório x online

| Critério | Laboratório (software nativo, hardware dedicado) | Online (navegador, dispositivo do participante) |
|---|---|---|
| Precisão (erro variável) | média abaixo de 1 ms (dat.qual.granularity-and-constructs; bridges2020timing) | na maioria dos pacotes abaixo de 10 ms em todos os navegadores; PsychoPy abaixo de 3,5 ms (dat.qual.granularity-and-constructs; bridges2020timing) |
| Acurácia (lag) | — | JavaScript 26,8 ms mais lento que Psychophysics Toolbox (dat.qual.granularity-and-constructs; deleeuw2016psychophysics); lag médio de 80 ms, até 100 ms com teclados reais (anwyl2021realistic); 50 a 70 ms na maioria das configurações, 133 ms num caso (bridges2020timing, sobre o pré-print de pronk2020mental) |
| Dispositivo de resposta | caixa de resposta de 1 kHz (dat.qual.granularity-and-constructs; bridges2020timing) | teclados USB podem acrescentar 20 a 40 ms; telas e teclados superestimam o RT (dat.qual.granularity-and-constructs; bridges2020timing, pronk2020mental) |
| Resolução do carimbo | — | 100 µs ou 5 µs isolado (`performance.now()`); `Event.timeStamp` de 0,1 a 1 ms por navegador, 16,667 ms ou mais com `resistFingerprinting` (dat.qual.granularity-and-constructs; w3c2026hrtime, mdn2026eventtimestamp) |
| Início do estímulo | — | quantizado pelo quadro, cerca de 16,67 ms a 60 Hz (dat.qual.granularity-and-constructs; pronk2020mental, mdn2026requestanimationframe) |
| RT absoluto entre participantes | — | "unwise" em dados web (dat.qual.granularity-and-constructs; bridges2020timing) |
| Delineamento recomendado | — | intraparticipante, RT relativo, restrição de navegador quando o tempo é crítico (dat.qual.granularity-and-constructs; anwyl2021realistic, pronk2020mental) |
| Validação | cronometria externa (dat.qual.granularity-and-constructs; bridges2020timing) | cronometria externa na configuração real (dat.qual.granularity-and-constructs; bridges2020timing, anwyl2021realistic) |

Nenhum estudo consultado mediu lag e jitter em tablets e celulares usados por crianças (dat.qual.granularity-and-constructs).

## 7. Repositórios: Zenodo x Dataverse x OSF

| Critério | Zenodo | Dataverse | OSF |
|---|---|---|---|
| DOI | DataCite, por versão, mais concept DOI (dat.rd.repositories-and-versioning; zenodo2026versioning) | um identificador (DOI ou Handle) por dataset, não por versão (dat.rd.repositories-and-versioning; dataverse2026datasetmgmt) | não verificado (dat.rd.repositories-and-versioning) |
| Metadados com arquivos fechados | sempre públicos, em CC0 (dat.rd.repositories-and-versioning; zenodo2026aboutrecords, zenodo2026policies) | públicos sob embargo e restrição (dat.rd.repositories-and-versioning; dataverse2026datasetmgmt) | não; o embargo oculta o registro (dat.rd.repositories-and-versioning; osf2026embargo) |
| Pedido de acesso | aprovação do depositante (dat.rd.repositories-and-versioning; zenodo2026policies) | Request Access, termos de acesso, guestbook (dat.rd.repositories-and-versioning; dataverse2026datasetmgmt, dataverse2026collectionmgmt) | não verificado |
| Embargo | até data final, liberação automática (dat.rd.repositories-and-versioning; zenodo2026policies) | por arquivo, inalterável após publicação, sem pedido durante o embargo (dat.rd.repositories-and-versioning; dataverse2026datasetmgmt) | até 4 anos (dat.rd.repositories-and-versioning; osf2026embargo) |
| Retirada e eliminação | retirada com tombstone; arquivos preservados (dat.rd.repositories-and-versioning; zenodo2026policies) | período de retenção; destruição manual (dat.rd.repositories-and-versioning; dataverse2026datasetmgmt) | não verificado |
| Versionamento | nova versão é novo registro ligado aos demais (dat.rd.repositories-and-versioning; zenodo2026manageversions) | versões maior e menor; arquivos novos exigem maior (dat.rd.repositories-and-versioning; dataverse2026datasetmgmt) | — |
| Limite | 50 GB por registro (dat.rd.repositories-and-versioning; zenodo2026policies) | por instalação | 5 GB anexados ao registro (dat.rd.repositories-and-versioning; osf2026registrations) |

DVC, Git LFS e git-annex versionam durante o trabalho, mas não emitem DOI nem garantem preservação [I] (dat.rd.repositories-and-versioning).

## 8. Plano de gestão de dados: FAPESP x H2020 x Science Europe

| Critério | FAPESP | H2020 (v3.0, 2016) | Science Europe (2021) |
|---|---|---|---|
| Obrigatoriedade | anexo obrigatório "para determinadas modalidades e chamadas" na página; "todo projeto", exceto PIPE e IC, no FAQ (dat.rd.data-management-plans; fapesp2026gestaodedados, fapesp2024faqpgd) | obrigatório no piloto, com opt-out (dat.rd.data-management-plans; ec2016h2020fairdmp) | requisito mínimo recomendado a financiadores (dat.rd.data-management-plans; scienceeurope2021rdmguide) |
| Tamanho e formato | até 2 páginas, centros até 5; PDF (dat.rd.data-management-plans; fapesp2024faqpgd) | não fixado | não fixado |
| Estrutura | 4 itens: dados e metadados; restrições legais e éticas; preservação e compartilhamento com carência; mecanismos e formatos (dat.rd.data-management-plans; fapesp2026gestaodedados) | 6 seções, modelo opcional (dat.rd.data-management-plans; ec2016h2020fairdmp) | 6 requisitos, 15 perguntas-guia (dat.rd.data-management-plans; scienceeurope2021rdmguide) |
| Prazo e atualização | na submissão; mudanças nos relatórios (dat.rd.data-management-plans; fapesp2024faqpgd) | versão inicial até o mês 6; documento vivo (dat.rd.data-management-plans; ec2016h2020fairdmp) | não fixado |
| Acesso restrito | restrições no item b; só metadados quando os dados não podem ser divulgados (dat.rd.data-management-plans; fapesp2024faqpgd) | comitê de acesso, identificação de quem acessa (dat.rd.data-management-plans; ec2016h2020fairdmp) | procedimento de acesso gerenciado (dat.rd.fair-principles; scienceeurope2021rdmguide) |
| Onde depositar | repositórios abertos; páginas pessoais e drives não valem (dat.rd.data-management-plans; fapesp2024faqpgd) | — | ao menos duas cópias em locais separados durante a pesquisa (dat.rd.data-management-plans; scienceeurope2021rdmguide) |
| Avaliação | não descrita nas páginas consultadas (dat.rd.data-management-plans) | não é critério de avaliação (dat.rd.data-management-plans) | rubrica com dois níveis (dat.rd.data-management-plans; scienceeurope2021rdmguide) |

## 9. Documentação de dataset: datasheet x nutrition label x data statement x DDI

| Critério | Datasheet for datasets | Dataset Nutrition Label | Data statement | DDI-Codebook |
|---|---|---|---|---|
| Forma | prosa por perguntas (dat.rd.data-documentation; gebru2021datasheets) | módulos visuais; só Metadata obrigatório (dat.rd.data-documentation; holland2018nutrition) | prosa, forma longa e curta de 60 a 100 palavras (dat.rd.data-documentation; bender2018datastatements) | XML legível por máquina (dat.rd.data-documentation) |
| Automação | deliberadamente manual (dat.rd.data-documentation; gebru2021datasheets) | parte automática (dat.rd.data-documentation; holland2018nutrition) | manual (dat.rd.data-documentation) | gerável por ferramenta; exportado pelo Dataverse (dat.rd.data-documentation; dataverse2026datasetmgmt) |
| Nível de variável | não é o foco (dat.rd.data-documentation) | módulos Variables e Statistics (dat.rd.data-documentation; holland2018nutrition) | não (dat.rd.data-documentation) | sim (dat.rd.data-documentation; ddi2014codebook25) |
| Consentimento e titulares | perguntas explícitas sobre notificação, consentimento e revogação (dat.rd.data-documentation; gebru2021datasheets) | módulo futuro (dat.rd.data-documentation; holland2018nutrition) | permissão de falantes (dat.rd.data-documentation) | não verificado (dat.rd.data-documentation) |
| Risco de privacidade da própria documentação | perguntas sobre identificação direta ou indireta (dat.rd.data-documentation; gebru2021datasheets) | reconhecido: distribuições permitem aproximar o conteúdo (dat.rd.data-documentation; holland2018nutrition) | reconhecido para grupos pequenos (dat.rd.data-documentation; bender2018datastatements) | não verificado |
| Situação | arXiv v8 (2021) e CACM (dat.rd.data-documentation; gebru2021datasheets) | pré-print "Draft May 2018" (dat.rd.data-documentation; holland2018nutrition) | artigo acadêmico (dat.rd.data-documentation; bender2018datastatements) | 2.5 (rev. 2.5.1, 2014); Lifecycle 3.3 de 2020 (dat.rd.data-documentation; ddi2014codebook25, ddi2020lifecycle33) |

O README de dataset, em texto simples, cobre o nível de variável e não trata consentimento (dat.rd.data-documentation; cornell2026readme). As formas se combinam: DataCite para citação, README e dicionário para interpretação, datasheet para contexto ético [I] (dat.rd.data-documentation).

## 10. Regime de revisão ética: Resoluções CNS x Lei 14.874/2024 com Decreto 12.651/2025

| Critério | Resoluções CNS (466/2012, 510/2016, 674/2022) e NO 001/2013 | Lei 14.874/2024 e Decreto 12.651/2025 |
|---|---|---|
| Natureza | normas do Conselho Nacional de Saúde (dat.ethics.cep-conep-system) | lei e decreto regulamentador (dat.ethics.cep-conep-system; lei148742024, decreto126512025) |
| Sistema | Sistema CEP/Conep (dat.ethics.cep-conep-system; cns4662012) | Sistema Nacional, com Instância Nacional e CEP (dat.ethics.cep-conep-system; lei148742024, decreto126512025) |
| Escopo | pesquisa com seres humanos, incluindo o manejo de seus dados (dat.ethics.cep-conep-system; cns4662012) | "em todas as áreas do conhecimento", no que couber e conforme regulamento (dat.ethics.cep-conep-system; lei148742024) |
| Classificação | tipificação A, B, C e modalidades de tramitação (dat.ethics.cep-conep-system; cns6742022) | grau de risco por análise multidimensional (população vulnerável, dados sensíveis ou IA, complexidade) (dat.ethics.cep-conep-system; decreto126512025) |
| Prazos | checagem até 7 dias; parecer em 15, 21, 30 ou 45 dias conforme a modalidade (dat.ethics.cep-conep-system; cns6742022) | 10 dias úteis para aceitar a submissão; 30 dias úteis para o parecer (dat.ethics.cep-conep-system; lei148742024) |
| Competência | colegiada especial em CEP acreditado ou Conep (dat.ethics.cep-conep-system; cns6742022) | CEP credenciado ou acreditado para risco baixo ou moderado; só acreditado para risco elevado (dat.ethics.cep-conep-system; lei148742024) |
| Crianças e adolescentes | justificativa da inclusão aprovada pelo CEP; proteção independente do risco (dat.ethics.cep-conep-system; cns4662012, cns5102016) | pesquisa essencial para a população e impossível com adultos capazes; comunicação ao Ministério Público (dat.ethics.cep-conep-system; lei148742024) |
| Forma do consentimento | TCLE escrito em duas vias (466); registro em qualquer mídia justificada (510) (dat.ethics.consent-and-assent-in-research; cns4662012, cns5102016) | TCLE assinado pelo representante e assentimento por termo escrito quando possível (dat.ethics.consent-and-assent-in-research; lei148742024) |
| Uso dos dados para outros fins | vedado além do protocolo e do consentimento (dat.ethics.consent-and-assent-in-research; cns4662012) | vedado salvo autorização expressa no TCLE para pesquisas futuras (dat.ethics.consent-and-assent-in-research; lei148742024) |
| Relação com a LGPD | exigência paralela (dat.ethics.cep-conep-system; anpd2023guiapesquisa) | LGPD aplicada subsidiariamente (dat.ethics.research-vs-operation; lei148742024) |
| Transição | normas do CNS valem até normas da Instância Nacional, se não contrariarem lei e decreto; Conep segue como instância recursal até a posse (dat.ethics.cep-conep-system; decreto126512025) | lei em vigor 90 dias após a publicação, sem regra própria de transição (dat.ethics.cep-conep-system; lei148742024) |

Em 2026, um protocolo ainda é preparado segundo as resoluções do CNS, com verificação caso a caso dos pontos em que a lei diverge [I] (dat.ethics.cep-conep-system).

## 11. Consentimento de pesquisa x consentimento LGPD

| Critério | TCLE (pesquisa) | Assentimento (pesquisa) | Consentimento LGPD (serviço) |
|---|---|---|---|
| Quem manifesta | participante capaz ou representante (dat.ethics.consent-and-assent-in-research; cns4662012) | criança, adolescente ou incapaz (dat.ethics.consent-and-assent-in-research; cns4662012) | titular; para crianças, um dos pais ou responsável (`psg.consent.parental-consent`) |
| Natureza | condição ética de participação (dat.ethics.consent-and-assent-in-research) | anuência que não substitui o TCLE (dat.ethics.consent-and-assent-in-research; cns5102016) | uma das bases legais, substituível por outra (dat.ethics.consent-and-assent-in-research; anpd2023guiapesquisa) |
| Forma | escrita (466); qualquer mídia justificada (510) (dat.ethics.consent-and-assent-in-research; cns5102016) | linguagem acessível; escrita quando possível (dat.ethics.consent-and-assent-in-research; lei148742024) | escrita ou outro meio que demonstre a vontade (`psg.consent.parental-consent`) |
| Quem aprova o texto | CEP, e Conep quando pertinente (dat.ethics.consent-and-assent-in-research; cns4662012) | CEP (dat.ethics.consent-and-assent-in-research) | controlador (dat.ethics.consent-and-assent-in-research) |
| Retirada | em qualquer fase, sem penalização (dat.ethics.consent-and-assent-in-research; cns4662012) | a qualquer momento (dat.ethics.consent-and-assent-in-research; cns5102016) | revogação (`psg.consent.permission-lifecycle`) |

A ANPD afirma que o consentimento pode ser dispensável pela LGPD e necessário do ponto de vista ético (dat.ethics.consent-and-assent-in-research; anpd2023guiapesquisa).

## 12. Datasets de referência

| Dataset | Grão da linha | População | Licença e acesso | Desidentificação |
|---|---|---|---|---|
| PSLC DataShop | transação; rollups aluno-passo e aluno-problema (dat.ds.comparison; datashop2026importformat) | varia por dataset (dat.ds.comparison; koedinger2010datashop) | termos próprios: só pesquisa, sem redistribuição, sem desanonimizar (dat.ds.pslc-datashop; datashop2026terms) | `Anon Student Id`; revisão de shareability ligada ao IRB (dat.ds.pslc-datashop; datashop2026irb) |
| KDD Cup 2010 | aluno-passo com `Correct First Attempt` (dat.ds.comparison; datashop2010kddcuprules) | Algebra 2005: alunos de 13 a 14 anos (dat.ds.comparison; liu2022pykt) | login no DataShop; citação de Stamper et al. (dat.ds.comparison; stamper2010kddcup) | `Anon Student Id` (dat.ds.comparison) |
| ASSISTments | aluno × problema (dat.ds.assistments) | ensino fundamental II e médio, matemática, EUA (dat.ds.comparison; heffernan2014assistments) | termos: sem repasse; dados e código devem ser publicados (dat.ds.assistments; assistments2026terms) | ids substituídos, método não descrito; FERPA citada (dat.ds.assistments; assistments2026interpret, assistments2026terms) |
| EdNet | resposta (KT1) até ação de interface (KT4) (dat.ds.ednet; choi2020ednet) | candidatos ao TOEIC na Coreia do Sul; idade não informada (dat.ds.ednet; choi2020ednet) | CC BY-NC 4.0, links públicos (dat.ds.ednet; riiid2020ednetrepo) | um arquivo por id; tempos deslocados por valor fixo (dat.ds.ednet; riiid2020ednetrepo) |
| OULAD | resumo diário de cliques por material (dat.ds.comparison; kuzilek2017oulad) | adultos em ensino a distância, Reino Unido (dat.ds.comparison; kuzilek2017oulad) | CC-BY 4.0 (dat.ds.comparison; kuzilek2017oulad) | k-anonimato com k = 5; idade e IMD generalizados (dat.ds.comparison; kuzilek2017oulad) |
| Junyi 2015 | tentativa de exercício (dat.ds.comparison; edudata2026junyi) | plataforma de matemática de Taiwan; idade não informada (dat.ds.comparison; chang2015junyi) | projeto público no DataShop; uso comercial vedado (dat.ds.comparison) | não descrita (dat.ds.comparison) |
| Junyi 2020 | tentativa de problema (dat.ds.comparison; junyi2020kaggle) | alunos da plataforma, 2018-2019; série não verificada (dat.ds.comparison; junyi2020kaggle) | CC BY-NC-SA 4.0, Kaggle (dat.ds.comparison; junyi2020kaggle) | não descrita (dat.ds.comparison) |
| Duolingo SLAM 2018 | token da resposta, certo ou errado (dat.ds.comparison; settles2018slam) | iniciantes nos primeiros 30 dias; idade não informada (dat.ds.comparison; settles2018slam) | CC BY-NC 4.0, Harvard Dataverse (dat.ds.comparison; settles2018slamdata) | id anônimo de 8 caracteres (dat.ds.comparison; settles2018slam) |

Tempo associado: milissegundo por transação no DataShop (dat.ds.pslc-datashop; datashop2026importformat); `first_response_time` em ms no ASSISTments, com `overlap_time` frequentemente errado (dat.ds.assistments; assistments2026interpret); timestamp Unix em ms por evento no EdNet (dat.ds.ednet; choi2020ednet); dia relativo no OULAD; `days` e `time` em segundos no SLAM (dat.ds.comparison).

Nenhum dataset verificado cobre crianças dos anos iniciais com população declarada, eventos cognitivo-motores finos e metadados de relógio e dispositivo [I] (dat.ds.comparison).
