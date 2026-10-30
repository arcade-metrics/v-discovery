---
id: dat.glossario
titulo: Glossário de dados de pesquisa e eventos
tipo: glossario
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Glossário: dados de pesquisa e eventos

Termos consolidados do domínio, selecionados dos campos `termos:` dos frontmatters. Termos em inglês quando esse é o uso consolidado. A definição resume a do documento; cada entrada aponta para o documento que aprofunda. Termos que pertencem a outro domínio estão no fim, só com o id de lá.

## Eventos

| Termo | Definição | Documento |
|---|---|---|
| ocorrência | captura de uma afirmação de fato durante a operação de um sistema de software (CloudEvents) | dat.ev.event-model |
| evento | registro de dados que expressa uma ocorrência e seu contexto; uma ocorrência pode gerar mais de um evento | dat.ev.event-model |
| envelope / atributos de contexto | atributos lidos sem desserializar o payload (`id`, `source`, `type`, `time`, `dataschema` e outros) | dat.ev.event-model |
| payload (*event data*) | os dados da ocorrência, separados dos metadados de contexto | dat.ev.event-model |
| dataschema | URI do esquema do payload; mudança incompatível deve gerar URI diferente | dat.ev.event-model |
| sequência (`sequence`) | extensão CloudEvents com a posição do evento na sequência de uma `source`, recomendada monotônica e contígua | dat.ev.event-model |
| timestamp de ocorrência / de observação | instante em que o evento ocorreu no relógio de origem, e instante em que o coletor o observou | dat.ev.event-model |
| evento de interação | evento cuja ocorrência é uma ação do aprendiz sobre um elemento da atividade (toque, escolha, resposta, abandono) | dat.ev.event-model |
| telemetria de jogo | coleta remota e contínua de dados sobre o uso de um jogo, em geral como eventos do cliente para um serviço | dat.ev.game-telemetry |
| game metrics / game analytics | variáveis calculadas a partir da telemetria; processo de identificar e comunicar padrões úteis a decisões de jogo | dat.ev.game-telemetry |
| métricas de jogador, de processo, de desempenho | classes de métrica de Seif El-Nasr et al.: comportamento do jogador, acompanhamento do desenvolvimento, execução técnica | dat.ev.game-telemetry |
| telemetria voltada ao desenvolvedor / ao usuário | coleta durante o desenvolvimento e testes, e coleta após o lançamento sobre o comportamento do jogador (Zoeller) | dat.ev.game-telemetry |
| completable, alternative, meaningful variable | os três tipos de alvo do modelo de interação de Serrano-Laguna et al. (nível ou missão; escolha; pontuação ou posição) | dat.ev.game-telemetry |
| event sourcing | registrar toda mudança de estado como evento, guardado na ordem em que foi aplicado, pelo mesmo tempo de vida do estado | dat.ev.event-sourcing |
| event store / eventstream | registro append-only que é o *system of record*, com um stream por entidade | dat.ev.event-sourcing |
| projeção / materialized view / rehydration | leitura derivada do log; reidratar é obter o estado atual pelo replay dos eventos da entidade | dat.ev.event-sourcing |
| CQRS | separação entre o modelo de escrita e o de leitura; independente de event sourcing | dat.ev.event-sourcing |
| evento compensatório | novo evento que desfaz ou corrige o efeito de um anterior, que permanece no log | dat.ev.event-sourcing |
| upcasting | conversão de um evento de versão antiga para a atual no momento da leitura | dat.ev.event-sourcing |
| crypto-shredding | cifrar dados pessoais com chave por titular e apagar a chave para torná-los ilegíveis | dat.ev.event-sourcing |
| instrumentação | código inserido no software para emitir dados sobre a própria execução | dat.ev.instrumentation-and-opentelemetry |
| sinal (OpenTelemetry) | forma especializada de observabilidade: traces, métricas, logs e baggage | dat.ev.instrumentation-and-opentelemetry |
| span / trace | operação com início, fim e atributos; trace é o grafo acíclico de spans | dat.ev.instrumentation-and-opentelemetry |
| EventName | campo que torna um LogRecord um evento; deve identificar a estrutura do evento e ter baixa cardinalidade | dat.ev.instrumentation-and-opentelemetry |
| Timestamp / ObservedTimestamp | carimbo do relógio de origem e carimbo do coletor no modelo de logs do OpenTelemetry | dat.ev.instrumentation-and-opentelemetry |
| context propagation / traceparent | mecanismo que serializa o contexto entre serviços; cabeçalho W3C Trace Context com versão, trace-id, parent-id e flags | dat.ev.instrumentation-and-opentelemetry |
| telemetry schema / schema URL | esquema de telemetria versionado, identificado por URL única por versão, com transformações entre versões | dat.ev.instrumentation-and-opentelemetry |
| mapeamento sem perda | função do evento interno para um statement xAPI que permite reconstruir o evento sem ambiguidade de valor, tempo ou significado | dat.ev.event-to-xapi-mapping |
| perda por precisão | truncamento de tempo abaixo de milissegundo ou de duração abaixo de 0,01 s na projeção para xAPI | dat.ev.event-to-xapi-mapping |
| teste de ida e volta | projetar uma amostra de eventos, reconstruí-los e comparar campo a campo | dat.ev.event-to-xapi-mapping |

## Qualidade do dado na coleta

| Termo | Definição | Documento |
|---|---|---|
| granularidade de evento | combinação da unidade do evento, da resolução temporal do carimbo e da resolução espacial das coordenadas | dat.qual.granularity-and-constructs |
| precisão temporal | variabilidade de tentativa a tentativa (erro variável, jitter); não pode ser corrigida depois | dat.qual.granularity-and-constructs |
| acurácia temporal / lag | erro constante (lag, offset, bias); pode ser subtraído se conhecido | dat.qual.granularity-and-constructs |
| cronometria externa | validação do tempo com fotodiodo, atuador ou solenoide na configuração real | dat.qual.granularity-and-constructs |
| tempo relativo | diferença de tempo de reação entre condições do mesmo participante, que cancela o lag constante | dat.qual.granularity-and-constructs |
| trajetória de ponteiro / tempo de iniciação | amostras de posição até a resposta, das quais se derivam desvio máximo, área sob a curva e inversões de direção | dat.qual.granularity-and-constructs |
| eventos coalescidos | amostras de ponteiro que o navegador junta num único `pointermove`; recuperáveis por `getCoalescedEvents()` | dat.qual.granularity-and-constructs |
| índice de dificuldade / largura efetiva | grandezas da lei de Fitts; `We` usa a dispersão real dos pontos finais | dat.qual.granularity-and-constructs |
| covariável de dispositivo | característica registrada por sessão (devicePixelRatio, taxa de atualização, tipo de ponteiro, isolamento, navegador) | dat.qual.granularity-and-constructs |
| relógio monotônico | relógio que nunca retrocede e não sofre ajustes, válido só dentro de uma execução | dat.qual.clocks-and-ordering |
| relógio de parede | relógio de calendário, sujeito a ajustes e saltos; não serve para medir intervalos | dat.qual.clocks-and-ordering |
| time origin | o zero do relógio monotônico num documento ou num worker | dat.qual.clocks-and-ordering |
| step / slew | correção de relógio por salto ou por ajuste gradual (limiares do NTPv4) | dat.qual.clocks-and-ordering |
| carimbo duplo com âncora de sessão | carimbo monotônico por evento mais pares (monotônico, parede UTC) lidos no início e após suspensão | dat.qual.clocks-and-ordering |
| número de sequência por sessão | contador estritamente crescente por sessão e produtor, que ordena e revela lacunas | dat.qual.clocks-and-ordering |
| perda informativa | perda que não é aleatória e se concentra em certas redes, dispositivos ou momentos da sessão | dat.qual.loss-and-deduplication |
| chave de idempotência | valor gerado pelo cliente para o servidor reconhecer reenvios da mesma requisição (rascunho IETF) | dat.qual.loss-and-deduplication |
| outbox local | fila persistente no cliente onde o evento é gravado antes do envio e só removido após confirmação | dat.qual.loss-and-deduplication |
| armazenamento best-effort / persistente | armazenamento do navegador que pode ser apagado sob pressão, e o que só o usuário apaga | dat.qual.loss-and-deduplication |
| lacuna de sequência | número de sequência ausente entre eventos recebidos da mesma sessão | dat.qual.loss-and-deduplication |
| asserção / anotação | no JSON Schema, palavra-chave que faz o documento passar ou falhar, e informação coletada sem efeito obrigatório | dat.qual.schema-validation-and-evolution |
| esquema do escritor / do leitor | no Avro, o esquema usado na escrita e o usado na leitura, casados pela resolução de esquema | dat.qual.schema-validation-and-evolution |
| compatibilidade retroativa, progressiva, total, transitiva | BACKWARD, FORWARD, FULL e variantes _TRANSITIVE do registro de esquemas | dat.qual.schema-validation-and-evolution |
| número de campo reservado | no Protocol Buffers, número de campo removido que não pode ser reutilizado | dat.qual.schema-validation-and-evolution |
| modelo de conteúdo aberto / fechado | `additionalProperties` verdadeiro ou falso, que muda o que conta como mudança compatível | dat.qual.schema-validation-and-evolution |

## Dados de pesquisa

| Termo | Definição | Documento |
|---|---|---|
| FAIR | Findable, Accessible, Interoperable, Reusable: desideratos para dados de pesquisa, não uma norma técnica | dat.rd.fair-principles |
| machine-actionable | contínuo de estados em que um objeto digital informa cada vez mais a um agente computacional | dat.rd.fair-principles |
| identificador persistente / metadados ricos | F1 e F2/R1 dos princípios FAIR | dat.rd.fair-principles |
| acesso controlado com metadados abertos | arranjo em que metadados são públicos e os dados exigem pedido e autorização (A1.2, A2) | dat.rd.fair-principles |
| "as open as possible, as closed as necessary" | política do piloto de dados abertos do H2020 | dat.rd.fair-principles |
| métrica FAIR | modelo de métrica e as 14 métricas universais do grupo FAIR Metrics | dat.rd.fair-principles |
| plano de gestão de dados (PGD, DMP) | documento que descreve, desde a proposta, coleta, documentação, guarda, compartilhamento e preservação | dat.rd.data-management-plans |
| período de carência | tempo antes do compartilhamento dos dados exigido no item c do PGD da FAPESP | dat.rd.data-management-plans |
| maDMP | PGD estruturado e atualizável, legível por máquina | dat.rd.data-management-plans |
| data steward | responsável pela gestão de dados, previsto no requisito 6 da Science Europe | dat.rd.data-management-plans |
| comitê de acesso a dados | instância prevista no modelo H2020 para decidir pedidos de acesso | dat.rd.data-management-plans |
| repositório de dados | serviço que recebe, identifica, descreve, preserva e dá acesso a datasets | dat.rd.repositories-and-versioning |
| concept DOI / version DOI | no Zenodo, DOI que resolve para a versão mais recente, e DOI de cada versão | dat.rd.repositories-and-versioning |
| embargo | bloqueio dos arquivos até uma data, com metadados visíveis (Zenodo, Dataverse) ou registro oculto (OSF) | dat.rd.repositories-and-versioning |
| termos de acesso / guestbook | condições para pedir arquivos restritos, e formulário que coleta dados de quem baixa (Dataverse) | dat.rd.repositories-and-versioning |
| período de retenção | data após a qual o conteúdo fica inacessível no Dataverse; a destruição não é automática | dat.rd.repositories-and-versioning |
| tombstone | página que mantém DOI e URL de um registro retirado | dat.rd.repositories-and-versioning |
| DVC, Git LFS, git-annex | ferramentas de versionamento de arquivos grandes durante o trabalho; não emitem DOI | dat.rd.repositories-and-versioning |
| datasheet for datasets | questionário em prosa sobre motivação, composição, coleta, usos, distribuição e manutenção | dat.rd.data-documentation |
| dataset nutrition label | painel modular, parte gerado automaticamente, com a visão geral do dataset | dat.rd.data-documentation |
| data statement | caracterização de dataset linguístico em forma longa e curta | dat.rd.data-documentation |
| codebook / DDI-Codebook / DDI-Lifecycle | descrição variável a variável; versões leve e completa do padrão DDI | dat.rd.data-documentation |
| README de dataset | arquivo de texto simples que acompanha os arquivos, recomendado quando não há padrão de metadados | dat.rd.data-documentation |

## Ética em pesquisa

| Termo | Definição | Documento |
|---|---|---|
| Sistema CEP/Conep | arranjo de revisão ética prévia das resoluções do CNS, com CEP e a Comissão Nacional | dat.ethics.cep-conep-system |
| Sistema Nacional de Ética em Pesquisa com Seres Humanos | arranjo instituído pela Lei 14.874/2024, com instância nacional e CEP | dat.ethics.cep-conep-system |
| Plataforma Brasil | sistema oficial de submissão e acompanhamento de protocolos | dat.ethics.cep-conep-system |
| pesquisa envolvendo seres humanos | pesquisa que envolve o participante direta ou indiretamente, incluindo o manejo de seus dados | dat.ethics.cep-conep-system |
| protocolo de pesquisa | documentos com a descrição da pesquisa, informações ao participante e qualificação dos pesquisadores | dat.ethics.cep-conep-system |
| tipificação da pesquisa | tipos A, B e C da Resolução 674/2022, que substituem a gradação de risco anterior | dat.ethics.cep-conep-system |
| modalidade de tramitação | expressa, simplificada, colegiada ou colegiada especial, com prazos próprios | dat.ethics.cep-conep-system |
| fatores de modulação | condições que mudam a tramitação sem mudar o tipo da pesquisa | dat.ethics.cep-conep-system |
| emenda / extensão | modificação do projeto aprovado, e prorrogação sem mudança essencial | dat.ethics.cep-conep-system |
| CEP credenciado / acreditado | níveis de habilitação que definem a competência por grau de risco na Lei 14.874/2024 | dat.ethics.cep-conep-system |
| consentimento livre e esclarecido / TCLE | anuência do participante ou representante após esclarecimento completo; o documento escrito que a explicita | dat.ethics.consent-and-assent-in-research |
| assentimento / termo de assentimento | anuência da criança ou adolescente na medida de sua compreensão; documento em linguagem acessível | dat.ethics.consent-and-assent-in-research |
| registro do consentimento | documento em qualquer meio (papel, áudio, vídeo, digital) previsto na Resolução 510/2016 | dat.ethics.consent-and-assent-in-research |
| consentimento eletrônico | consentimento e assentimento em ambiente virtual, normatizados pelo Ofício Circular 23/2022 da Conep | dat.ethics.consent-and-assent-in-research |
| pesquisa encoberta | pesquisa sem informar objetivos nem obter consentimento prévio, só justificável em casos previstos | dat.ethics.consent-and-assent-in-research |
| objeção deliberada / co-consent | recusa de criança que ainda não assente, a ser respeitada; consentimento parental ao lado da anuência de adolescente (CIOMS) | dat.ethics.consent-and-assent-in-research |
| consentimento para pesquisas futuras | autorização expressa no TCLE para usar dados em outros projetos (Lei 14.874/2024, art. 45) | dat.ethics.consent-and-assent-in-research |
| base operacional / base de pesquisa | dados coletados para prestar um serviço, e dados tratados sob protocolo aprovado | dat.ethics.research-vs-operation |
| uso secundário (tratamento posterior) | uso para pesquisa de dado coletado com outra finalidade | dat.ethics.research-vs-operation |
| presunção de compatibilidade | entendimento da ANPD sobre uso secundário para estudos e pesquisas, sem autorização irrestrita | dat.ethics.research-vs-operation |
| órgão de pesquisa | ente público ou pessoa jurídica sem fins lucrativos com pesquisa na missão (LGPD, art. 5, XVIII) | dat.ethics.research-vs-operation |
| teste A/B (experimento de produto) | comparação controlada entre variantes de um serviço em usuários reais, vista pelo regime ético | dat.ethics.research-vs-operation |
| A/B illusion | tendência de ver o experimento que testa uma prática como mais suspeito que implantá-la sem teste (Meyer) | dat.ethics.research-vs-operation |
| custodiante de dados / dado codificado | quem guarda a chave do código e compartilha só dados anonimizados ou codificados (CIOMS) | dat.ethics.research-vs-operation |

## Datasets de referência

| Termo | Definição | Documento |
|---|---|---|
| dataset de referência | dataset público de interação educacional usado como base de comparação entre estudos | dat.ds.comparison |
| DataShop | repositório e aplicação web para dados de interação entre estudantes e software educacional | dat.ds.pslc-datashop |
| transação / passo / problema | interação aluno-sistema; parte observável da solução; tarefa com vários passos (glossário do DataShop) | dat.ds.pslc-datashop |
| oportunidade | cada vez que um passo com o KC associado aparece | dat.ds.pslc-datashop |
| student-step rollup / student-problem rollup | exportações agregadas por aluno e passo, e por aluno e problema | dat.ds.pslc-datashop |
| knowledge component model (KC model) | lista de mapeamentos entre cada passo e um ou mais KCs | dat.ds.pslc-datashop |
| shareability | revisão que decide se um dataset do DataShop pode ser compartilhado fora da equipe | dat.ds.pslc-datashop |
| KDD Cup 2010 | cinco datasets de tutores de álgebra em formato aluno-passo, hospedados no DataShop | dat.ds.pslc-datashop |
| skill builder | conjunto de problemas do ASSISTments concluído com três acertos seguidos | dat.ds.assistments |
| problema original / scaffolding | problema principal, e subquestões abertas quando o aluno erra o original | dat.ds.assistments |
| first_response_time / ms_first_response | tempo em ms entre o início e a primeira ação do aluno | dat.ds.assistments |
| detector de afeto | coluna com predição, não observação, de frustração, confusão, concentração ou tédio | dat.ds.assistments |
| duplicação de registros | defeito do dataset 2009-2010: 23,6% de linhas duplicadas | dat.ds.assistments |
| KT1 a KT4 | quatro recortes do EdNet em resolução crescente, de pares questão-resposta a todas as ações | dat.ds.ednet |
| bundle | conjunto de questões que compartilham passagem, imagem ou áudio | dat.ds.ednet |
| deslocamento de timestamp | soma de valor fixo aos carimbos, que preserva intervalos e impede análise de calendário | dat.ds.ednet |
| OULAD, Junyi Academy, Duolingo SLAM | datasets comparados: ensino a distância de adultos; matemática em Taiwan; aprendizes de segunda língua | dat.ds.comparison |

## Termos de outros domínios usados aqui

Definidos no domínio de origem; aqui só o id.

| Termo | Documento |
|---|---|
| xAPI, statement, xAPI Profile | iop.lr.xapi |
| Caliper, cmi5 | iop.lr.caliper, iop.lr.cmi5 |
| sincronização de relógio, NTP, offset | rtm.net.clock-synchronization |
| happens-before, relógio lógico, ordem causal | rtm.net.logical-clocks |
| jitter de rede | rtm.net.jitter |
| at-most-once, at-least-once, exactly-once | rtm.rel.delivery-semantics |
| anonimização, pseudonimização | psg.deid.anonymization-and-pseudonymization |
| k-anonimato | psg.deid.k-anonymity-and-extensions |
| risco de reidentificação | psg.deid.reidentification-risk |
| minimização, privacy by design | psg.access.minimization-and-privacy-by-design |
| consentimento parental (serviço) | psg.consent.parental-consent |
| assentimento da criança (serviço) | psg.consent.child-assent |
| RIPD / DPIA | psg.audit.ripd-dpia |
| LGPD e dados de crianças | psg.legal.lgpd-children |
| knowledge component (KC) | adp.id.knowledge-components |
| knowledge tracing (BKT, DKT) | adp.kt.bayesian-knowledge-tracing, adp.kt.deep-knowledge-tracing |
| proveniência, linhagem | lae.dq.provenance-and-lineage |
| desenho experimental, RCT | lae.evalm.experimental-design |
| PROV-O | kg.std.prov-o |
