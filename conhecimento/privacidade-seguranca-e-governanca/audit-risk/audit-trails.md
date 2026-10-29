---
id: psg.audit.audit-trails
titulo: Trilhas de auditoria e rastreabilidade de decisões
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nist2020sp80053r5, nist2006sp80092, nist2023sp80092r1, owasp2026loggingcheatsheet, rfc5424, rfc3161, iso270012022, iso270022022, w3c2013provo, brasil2018lgpd]
relacoes:
  - { tipo: depende-de, alvo: psg.audit.processing-records }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: complementa, alvo: psg.audit.privacy-risk-management }
  - { tipo: complementa, alvo: kg.std.prov-o }
  - { tipo: complementa, alvo: lae.dq.provenance-and-lineage }
  - { tipo: complementa, alvo: kg.eng.versioning-and-provenance }
  - { tipo: complementa, alvo: psg.ai.transparency-and-human-oversight }
  - { tipo: complementa, alvo: psg.sec.incident-management }
  - { tipo: relacionado-a, alvo: psg.sec.iso-27001-and-27701 }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: psg.access.rbac-and-abac }
  - { tipo: especificado-por, alvo: iop.br.lgpd }
termos: [trilha de auditoria, registro de auditoria, log, gestão de logs, evento auditável, não repúdio, carimbo de tempo, write-once, integridade de log, retenção de logs, registro de decisão, família AU, syslog, TSA]
---

# Trilhas de auditoria e rastreabilidade de decisões

## Definição e terminologia

Um **log** é "a record of the events occurring within an organization's systems and networks", composto de entradas, cada uma com informação sobre um evento específico; **gestão de logs** é o processo de gerar, transmitir, armazenar, analisar e descartar esses dados [F: nist2006sp80092, Executive Summary]. O rascunho da revisão 1 mantém a definição e descreve a gestão de logs como "generating, transmitting, storing, accessing, and disposing of log data" [F: nist2023sp80092r1, Abstract]. Uma **trilha de auditoria** (audit trail) é a coleção de registros de auditoria usada para detecção, análise e relato, distinta do registro individual que a compõe [F: nist2020sp80053r5, AU-9(1), Discussion]. Neste documento, **registro de decisão** designa o subconjunto da trilha que permite reconstruir uma decisão automatizada ou assistida sobre um aprendiz: entradas, versão do modelo, regras e configuração ativas, saída e ações humanas subsequentes [I].

O que a trilha de auditoria não é: não é o registro das operações de tratamento exigido pelo art. 37 da LGPD, que é um inventário por finalidade e não por evento (ver `psg.audit.processing-records`); não é o grafo de proveniência de dados de um pipeline analítico, embora possa usar o mesmo vocabulário (ver `lae.dq.provenance-and-lineage` e `kg.std.prov-o`); e não é o log operacional de depuração, cujo conteúdo e retenção obedecem a critérios distintos [I].

## Problema que resolve

Quando um sistema recomenda um conteúdo, ajusta uma dificuldade ou sinaliza um aluno numa data passada, responsável, professor e autoridade podem perguntar por quê. A LGPD dá ao titular o direito de "solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado" (art. 20, redação da Lei 13.853/2019) e obriga o controlador a fornecer "informações claras e adequadas a respeito dos critérios" da decisão (art. 20, §1) [F: brasil2018lgpd]. Sem registro contemporâneo de entradas, modelo e configuração, a revisão só pode reexecutar o sistema atual, que já não é o que decidiu [I]. Ao mesmo tempo, a própria trilha reúne dados pessoais de menores em grande volume e por longo prazo; o NIST observa que organizações devem considerar "how audit records can reveal information about individuals that may give rise to privacy risks and how best to mitigate such risks", em especial quando a trilha "records inputs or is based on patterns or time of usage" [F: nist2020sp80053r5, AU-3, Discussion]. O problema é, portanto, duplo: registrar o suficiente para reconstruir e não registrar o que cria novo risco [I].

## Fundamentos e funcionamento

### O que um registro precisa conter

O controle AU-3 do NIST SP 800-53 rev. 5 exige que registros de auditoria estabeleçam: "a. What type of event occurred; b. When the event occurred; c. Where the event occurred; d. Source of the event; e. Outcome of the event; and f. Identity of any individuals, subjects, or objects/entities associated with the event" [F: nist2020sp80053r5, AU-3]. O OWASP Logging Cheat Sheet organiza os atributos em quando (data e hora do log e do evento, identificador de interação), onde (identificador e versão da aplicação, endereço, localização no código), quem (endereço de origem, identidade do usuário se conhecida) e o quê (tipo, severidade, descrição, sinalizador de relevância de segurança), e sugere ainda ação, objeto, resultado, motivo e classificação do usuário [F: owasp2026loggingcheatsheet, Event attributes]. O AU-2 exige que a organização identifique os tipos de evento que o sistema é capaz de registrar, selecione o subconjunto efetivamente registrado e documente "a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations" [F: nist2020sp80053r5, AU-2].

Para reconstruir uma decisão, esses elementos genéricos precisam ser instanciados em cinco camadas, numa síntese deste documento [I]:

1. **Entradas**: identificadores ou hashes dos dados de entrada efetivamente usados (não uma cópia), com o instante de leitura, porque o estado do aluno muda continuamente.
2. **Modelo**: identificador e versão (ou hash do artefato) do modelo que produziu a saída; o vocabulário PROV-O trata isso como uma `prov:Activity` que `prov:used` uma `prov:Entity` (o modelo) e gerou outra (a recomendação), com `prov:wasAssociatedWith` apontando o `prov:Agent` responsável, podendo qualificar a associação com um `prov:Plan` que representa as regras seguidas [F: w3c2013provo, §3.1, §3.3].
3. **Regras e configuração**: versão do conjunto de regras pedagógicas, limiares e flags ativos no instante; a AU-3(1) permite incluir "access control or flow control rules invoked" como informação adicional [F: nist2020sp80053r5, AU-3(1)].
4. **Saída**: a recomendação ou decisão e o resultado do evento (AU-3 e).
5. **Ações humanas**: quem visualizou, aceitou, alterou ou reverteu a decisão, com identidade e instante, o que o AU-10 chama de evidência de não repúdio de que "an individual (or process acting on behalf of an individual) has performed" uma ação [F: nist2020sp80053r5, AU-10].

### Integridade e tempo

O AU-9 exige proteger "audit information and audit logging tools from unauthorized access, modification, and deletion" e alertar ao detectar violação; seus aprimoramentos preveem gravação em mídia write-once por hardware (AU-9(1)) e armazenamento em sistema fisicamente separado do auditado (AU-9(2)) [F: nist2020sp80053r5, AU-9]. O SP 800-92 descreve a verificação de integridade por message digest calculado por arquivo e guardado de forma segura, com os digests originais protegidos por criptografia aprovada ou mídia somente leitura [F: nist2006sp80092, §3.2]. O OWASP recomenda "build in tamper detection", copiar logs para mídia somente leitura o quanto antes, registrar e monitorar todo acesso aos logs e restringir e revisar periodicamente os privilégios de leitura [F: owasp2026loggingcheatsheet, Protection].

O RFC 5424 define a mensagem syslog como HEADER, STRUCTURED-DATA e MSG, com TIMESTAMP derivado do RFC 3339 e campos APP-NAME, PROCID e MSGID [F: rfc5424, §6]. A RFC é explícita sobre o que não fornece: não há mecanismo para detectar replay, as mensagens podem ser alteradas em trânsito e a confidencialidade depende de um mapeamento de transporte seguro, com TLS obrigatório na implementação e recomendado no uso [F: rfc5424, §8.4, §8.7, §8.8, §5.1]. O formato, portanto, resolve interoperabilidade, não integridade [I]. Para provar que um registro existia antes de um instante, o RFC 3161 define a Time-Stamp Authority (TSA), que recebe apenas o hash do dado e devolve um token assinado contendo `genTime`; a TSA deve usar fonte de tempo confiável, gerar um inteiro único por token, não examinar o imprint além do tamanho e não incluir a identidade do requisitante [F: rfc3161, §2.1]. Combinar hash encadeado dos registros com carimbos periódicos de uma TSA é uma técnica de integridade que não expõe conteúdo à terceira parte [I].

Sobre tempo, o AU-8 exige relógios internos e carimbos em UTC ou com offset explícito [F: nist2020sp80053r5, AU-8]; o SP 800-92 nota que relógios dessincronizados e múltiplos fusos tornam a normalização de tempos "particularly challenging" e recomenda NTP [F: nist2006sp80092, §3.2, nota 24]; o OWASP acrescenta que, quando sincronizar não for possível, convém medir o desvio ou registrar um nível de confiança no carimbo [F: owasp2026loggingcheatsheet, Event collection]. O AU-12(1) pede trilha correlacionada no tempo dentro de uma tolerância definida [F: nist2020sp80053r5, AU-12(1)].

### A trilha como risco de privacidade

O OWASP lista dados a excluir dos logs (código-fonte, identificadores de sessão, tokens de acesso, senhas, strings de conexão, chaves, dados de pagamento, informação comercialmente sensível) e dados a tratar com cautela, entre eles "non sensitive personal data", sugerindo "personal data de-identification techniques such as deletion, scrambling or pseudonymization" [F: owasp2026loggingcheatsheet, Data to exclude]. O SP 800-92 observa que logs podem capturar "sensitive information such as users' passwords and the content of e-mails", levantando preocupações de segurança e privacidade tanto para quem os revisa quanto para quem os acessa indevidamente [F: nist2006sp80092, §2.3.2]; o rascunho da revisão 1 inclui a tarefa de determinar se cada fonte "might intentionally or inadvertently capture sensitive data, including personal information" e como tratar divulgações inadvertidas [F: nist2023sp80092r1, TS-2.4, TS-4.3]. O AU-16(3) prevê medidas para "disassociate individuals from audit information" quando a trilha cruza fronteiras organizacionais [F: nist2020sp80053r5, AU-16(3)]. A ISO/IEC 27002:2022 trata o tema no controle 8.15, Logging, acompanhado de 8.16, Monitoring activities, e 8.17, Clock synchronization; só o sumário da norma foi consultado [F: iso270022022, metadados]. O Anexo A da ISO/IEC 27001:2022 referencia esses controles [F: iso270012022, metadados].

### Retenção e revisão

O AU-11 exige reter registros por período "consistent with records retention policy" para apoiar investigações e exigências regulatórias, e o AU-11(1) pede capacidade de recuperação de longo prazo, incluindo conversão de formato e documentação para interpretar registros antigos [F: nist2020sp80053r5, AU-11]. O SP 800-92 recomenda que a política defina, por tipo de log, quanto tempo preservar, como descartar, quem pode acessar e como os próprios acessos são registrados [F: nist2006sp80092, §4.2]. A LGPD determina a eliminação de dados após o término do tratamento, ressalvando o "cumprimento de obrigação legal ou regulatória pelo controlador" (art. 16, I) [F: brasil2018lgpd]. O AU-6 exige revisão e análise periódicas dos registros com relato a papéis definidos [F: nist2020sp80053r5, AU-6].

## Requisitos e pressupostos

- Versionamento de modelos, regras e configuração com identificadores estáveis; sem isso, o registro aponta para artefatos irreconstruíveis (ver `kg.eng.versioning-and-provenance`) [I].
- Identidade autenticada de quem age sobre a decisão, o que depende do controle de acesso (`psg.access.rbac-and-abac`) [I].
- Política de logging escrita, com os tipos de evento e a justificativa de suficiência exigidos pelo AU-2 [F: nist2020sp80053r5, AU-2].
- Pseudônimo estável do aluno na trilha, com a tabela de correspondência fora dela, para que o risco de reidentificação da trilha seja tratado como em `psg.deid.reidentification-risk` [I].

## Vantagens e limitações

A trilha de decisão permite responder a pedidos de revisão do art. 20 com o estado real da época e dá evidência para o princípio de responsabilização e prestação de contas (art. 6, X) [F: brasil2018lgpd; I]. Suas limitações: o volume cresce com cada decisão e cada visualização, o que o SP 800-92 identifica como desafio central de balancear recursos e dados [F: nist2006sp80092, §2.3]; registrar entradas por referência exige que os dados referenciados sobrevivam pelo mesmo prazo, o que conflita com minimização; e a integridade por hash ou TSA prova que o registro não mudou, não que ele era verdadeiro ao ser gravado [I].

## Alternativas e comparações

| Mecanismo | O que garante | O que não garante | Fonte |
|---|---|---|---|
| Syslog (RFC 5424) com TLS | Formato interoperável, confidencialidade em trânsito | Integridade fim a fim, detecção de replay | [F: rfc5424, §8] |
| Hash encadeado e mídia write-once | Detecção de alteração ou exclusão | Prova de tempo perante terceiros | [F: nist2020sp80053r5, AU-9(1); nist2006sp80092, §3.2] |
| Carimbo de tempo de TSA (RFC 3161) | Existência do registro antes de um instante, sem revelar conteúdo | Integridade entre carimbos; depende da chave da TSA | [F: rfc3161, §1, §2.1, §4] |
| Grafo PROV-O da decisão | Vínculo semântico entre entradas, atividade, modelo, agente e plano | Integridade ou retenção por si | [F: w3c2013provo, §3] |

Os quatro não competem: o grafo descreve, o hash protege, a TSA data e o syslog transporta [I].

## Métricas e métodos de avaliação

Teste de reconstrução: escolher decisões passadas ao acaso e verificar se entradas, versão do modelo, regras e ações humanas são recuperáveis apenas a partir da trilha, medindo cobertura e tempo de recuperação [I]. Cobertura de eventos: fração dos tipos de evento definidos no AU-2 efetivamente gerados (AU-12) [F: nist2020sp80053r5, AU-12]. Exposição: contagem de campos com dados pessoais diretos por registro, meta zero fora do pseudônimo [I]. Integridade: verificação periódica dos digests e dos tokens de tempo [I].

## Exemplo técnico independente de domínio

```
registro_de_decisao:
  id: uuid                      # AU-3 a
  ts_utc: 2026-03-14T13:05:22Z  # AU-8, RFC 3339
  sistema: recomendador@2.3.1   # AU-3 c, OWASP "where"
  sujeito: pseud:7f3a...        # pseudônimo, nunca identificador direto
  entradas: [{ref: estado_aluno#v812, hash: sha256:...}, {ref: sessao#4411, hash: ...}]
  modelo: {id: modelo_kt, versao: 7, hash: sha256:...}      # prov:used
  plano: {regras: regras_pedagogicas@v19, config: cfg#2026-03-01}  # prov:Plan
  saida: {tipo: recomendacao, item: atividade_3301, score: 0.71}   # AU-3 e
  agente: {tipo: sistema, id: svc-recomendador}            # prov:wasAssociatedWith
acoes_posteriores:
  - {ts_utc: ..., ator: prof:12, acao: visualizou}
  - {ts_utc: ..., ator: prof:12, acao: substituiu, nova_saida: atividade_3290, motivo: "..."}
integridade:
  hash_anterior: sha256:...     # encadeamento
  carimbo_tsa: {genTime: ..., serial: ...}   # RFC 3161, por lote
```

## Relações com outros conceitos

Depende de `psg.audit.processing-records`, que diz quais operações existem e por quê; a trilha registra eventos dentro delas. Complementa `psg.audit.ripd-dpia`, onde a trilha aparece como salvaguarda e como fonte de risco, e `psg.audit.privacy-risk-management`, que decide o que registrar a partir do risco. Usa o vocabulário de `kg.std.prov-o` e a noção de linhagem de `lae.dq.provenance-and-lineage`; o versionamento de artefatos fica em `kg.eng.versioning-and-provenance`. Alimenta `psg.ai.transparency-and-human-oversight` (revisão de decisões) e `psg.sec.incident-management` (investigação). A gestão de logs como controle de sistema de gestão está em `psg.sec.iso-27001-and-27701`.

## Lacunas e questões abertas

- O texto integral dos controles 8.15 a 8.17 da ISO/IEC 27002:2022 não foi acessado; só sumário e prefácio. O que o controle exige sobre conteúdo, proteção e retenção de logs fica por verificar.
- O rascunho do SP 800-92 rev. 1 (out. 2023) é playbook de planejamento e declara fora de escopo os detalhes de gestão de logs; não substitui a edição de 2006 em recomendações técnicas, e não foi localizada versão final.
- Não foi encontrada orientação da ANPD específica sobre retenção de trilhas de auditoria contendo dados de menores; o prazo adequado fica como questão de ponderação entre art. 16 e art. 20 da LGPD.
- Falta avaliar empiricamente quanto da capacidade de reconstrução se perde ao registrar entradas por hash em vez de cópia quando os dados de origem são eliminados por minimização.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nist2020sp80053r5 | normativo | 2026-10-29 |
| nist2006sp80092 | tecnico | 2026-10-29 |
| nist2023sp80092r1 | tecnico (rascunho) | 2026-10-29 |
| owasp2026loggingcheatsheet | tecnico | 2026-10-29 |
| rfc5424 | normativo | 2026-10-29 |
| rfc3161 | normativo | 2026-10-29 |
| iso270012022 | normativo [metadados] | 2026-10-29 |
| iso270022022 | normativo [metadados] | 2026-10-29 |
| w3c2013provo | normativo | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
