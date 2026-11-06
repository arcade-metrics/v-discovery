# Relatório: infraestrutura agnóstica de padrões para o VUOO

**Data:** 2026-11-05.

**Para quem:** equipe de produto e engenharia da Wemoga que vai desenhar a arquitetura do produto VUOO: nuvem, backend, banco, identidade, proteção de dados, app e pipeline de eventos.

**Produto, não projeto.** O produto VUOO é independente do projeto de pesquisa com o CIATec/CCD (decisão D8, §7.1b). A proposta em projeto/vuoo.md é só contexto. Versões anteriores deste relatório se referiam às fases F1.2 e F2.1 e a uma base de pesquisa; esse enquadramento foi retirado em 2026-11-05.

**Estado:** proposta. Nada aqui é decisão. As decisões viram ADR (pasta `padroes/` desta solução) depois da revisão humana.

**Base:** pesquisa com 7 frentes paralelas, cerca de 120 fichas e mais de 300 evidências com URL e data de acesso. Os detalhes ficam nas pastas citadas em cada seção.

---

## 1. Em uma página

1. **O VUOO deve ter um Core próprio, mínimo e neutro, e não adotar um padrão existente como núcleo.** OneRoster e Ed-Fi carregam viés americano e não cobrem aprendiz, experiência nem inclusão (D3, D6, D7). O CASE não gradua equivalências. Nenhum padrão modela PEI, apoio ou gêmeo digital. O desenho que sustenta "Core neutro + adaptadores" é o da UE: um vocabulário central neutro com perfis de aplicação por jurisdição (SEMIC), o mesmo que o ELM usa.
2. **O Core é escrito uma vez, como ontologia OWL/SKOS, e o resto é gerado a partir dela:** esquema relacional, JSON Schema/OpenAPI, R2RML e contexto JSON-LD. Isso deixa aberto um grafo OWL/SPARQL, se o produto o adotar, e segue o método da BNCC verificada que já analisamos ([brasil/bncc-dados/](fora-da-fase-1/brasil/bncc-dados/README.md)).
3. **Cada jurisdição é um perfil e um adaptador:**
   - o perfil restringe o Core (SHACL), acrescenta conceitos no próprio namespace e carrega os vocabulários oficiais como `ConceptScheme`;
   - o adaptador importa e exporta cada formato de fonte, versionado;
   - OneRoster, CASE, xAPI/Caliper e VC/Open Badges são views de exportação, não modelos internos.
4. **O Brasil é o único adaptador implementado agora.** A pesquisa trouxe o que ele precisa: leiaute do Censo 2026 campo a campo, contrato OpenAPI da API CMDEB v2 do Gestão Presente, tabelas de códigos, identificadores, regras da LDB, modelo curricular (BNCC e Currículo Paulista), Saeb/SARESP e o modelo de PEI da Portaria MEC 421/2026 e da Res. SEDUC-SP 129/2025.
5. **EUA, UE, Reino Unido e China ficam em standby, mas foram testados contra o Core.** Todos cabem com acréscimos genéricos, sem regra específica de país:
   - papéis como atribuição;
   - identificadores com scheme;
   - classificação de dados por atributo;
   - registro de divulgação;
   - plano com mantenedor.

   A China só cabe como **implantação separada no território**, operada por entidade local.
6. **Implantação:** uma célula por jurisdição (Brasil em região brasileira, cobrindo também logs, backups, telemetria e eventuais chamadas de LLM). O tenant é a rede ou secretaria; o aluno avulso entra num tenant próprio, a rede geral (D9). Não há base de pesquisa no produto (D14).

## 2. Arquitetura proposta

```
┌──────────────────────── Célula jurisdicional BR (região de nuvem no Brasil) ────────────────────────┐
│                                                                                                     │
│  Adaptadores BR (camada anticorrupção)             Views de exportação                              │
│   ├ Censo Escolar (1 serializador por ano)          ├ OneRoster 1.2 (para LMS)                      │
│   ├ API CMDEB v2 / Gestão Presente                  ├ CASE (currículo)                              │
│   ├ SED-SP (a pesquisar)                            ├ xAPI / Caliper (eventos)                      │
│   └ BNCC / Currículo Paulista (dataset verificado)  └ VC 2.0 / Open Badges 3.0                      │
│                 │                                                ▲                                  │
│                 ▼                                                │                                  │
│  Perfil vuoo-br: SHACL + ConceptSchemes (Censo, CMDEB, BNCC…) + mapeamentos SSSOM                   │
│                 │                                                                                   │
│                 ▼                                                                                   │
│  Base operacional (relacional = implementação do vuoo-core)                                         │
│   tenant = rede/secretaria · RLS em pool ou schema/banco dedicado · bitemporal nos vínculos         │
│                 │ R2RML                                                                             │
│                 ├──► grafo do aluno: consulta virtual (Ontop) ou materializado por tenant            │
│                 │      (se o produto adotar embeddings ou Graph RAG)                                │
│                 │                                                                                   │
│                 └──► log de eventos do app (§7.9): atividade + uso do app, séries em bloco          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
   Grafo curricular público (RDF nativo, versionado, sem dado pessoal): global, replicável entre células
   vuoo-core (OWL + SKOS) → gera esquema relacional, JSON Schema/OpenAPI, R2RML, @context JSON-LD (no CI)
```

| Decisão proposta | Por quê | Fonte |
|---|---|---|
| Core próprio mínimo + perfis (Opção B) | Neutro por construção; os padrões existentes viram views; deixa aberto um grafo OWL | [core/padroes-de-arquitetura.md §6](camada-agnostica/padroes-de-arquitetura.md) |
| Perfil restringe, extensão só no namespace da jurisdição, nunca redefinir termo do Core | Precedentes nas extensões Ed-Fi, nos perfis OneRoster e no DCAT-AP | idem §1.3 |
| Mapeamentos como dado (SKOS + SSSOM), `exactMatch` só após revisão | A transitividade gera equivalências falsas | idem §1, risco 2 |
| Identificador = lista `{scheme, issuer, value, vigência, status, usoPermitido}` | CPF, ID INEP e ID SGP no BR; UPN, ULN e SCN no UK; ID de 19 caracteres na China | [core/README.md](camada-agnostica/core-v0.1.md) P4 |
| Vínculos bitemporais (matrícula, enturmação, papel, apoio, PEI) | Códigos INEP refeitos todo ano; conflito Ed-Fi × OneRoster | idem P3 |
| Grafo híbrido: curricular nativo e público; aluno via R2RML | Dado pessoal fica onde já é protegido; qualquer consulta semântica sobre aluno roda por tenant dentro da célula | padroes-de-arquitetura §5 |
| Célula por jurisdição; tenant = rede | Residência; a rede é a controladora LGPD; a China exige operador local | idem §4; [china/](fora-da-fase-1/china/README.md) |

## 3. O Core v0.1

O modelo completo está em [core/README.md](camada-agnostica/core-v0.1.md). São cerca de 35 entidades em D1–D8 com 12 princípios. As mudanças em relação à lista provisória são as que mais afetam o banco:

- **Pessoa + atribuição de papel**, no lugar de subtipos Aluno, Professor e Responsável.
- **Matrícula em dois níveis**: com a organização/etapa e com a turma/oferta. Tem tipo (escolarização, AEE, complementar), eventos de situação e frequência como entidade.
- **Etapa** (`EducationalStage`) com nível ISCED obrigatório, separada de **programa de serviço** (AEE, tempo integral).
- **Currículo com quatro relógios** (ato, edição, versão do dado, coorte) e uma entidade **Adoção Curricular**, porque a DCNEM 2024 faz dois Ensinos Médios conviverem por coorte.
- **Resultado separado de classificação**: os cortes do Saeb, do SARESP e do CNCA são esquemas versionados aplicados sobre o mesmo valor.
- **Inclusão em três eixos**:
  - perfil de apoio (barreira → apoio → acomodação), que existe sem laudo;
  - elegibilidade administrativa, sensível e isolada, que nunca alimenta a personalização;
  - documento de suporte, opcional.

  O plano individual tem seções tipadas, mantenedor e revisões.
- **Governança como dado:** classificação por atributo, base legal por operação, registro de divulgação, acordo de dados com prazos e local de processamento, e declaração/snapshot para envios oficiais (Censo).

## 4. O módulo Brasil

O índice completo está em [brasil/README.md](camada-brasil/README-estudo-brasil.md).

### 4.1 Componentes

| Componente | O que faz | Insumo pronto | Falta |
|---|---|---|---|
| **Perfil `vuoo-br`** | SHACL de cardinalidades e vocabulários obrigatórios; extensões BR (classe especial, turma multietapa, localização diferenciada…) | [modelo-de-dados.md](camada-brasil/modelo-de-dados.md) §4 | escrever as shapes |
| **Vocabulários BR** | ConceptSchemes do Censo 2026 e do CMDEB: etapa, modalidade, cor/raça, deficiência, função, situação, dependência… | [terminologia.md](camada-brasil/terminologia.md) | **crosswalk Censo × CMDEB**: não existe oficial, então é nosso, em SSSOM |
| **Identidade** | Resolução por CPF (Inue) → ID INEP → certidão → nome + nascimento + filiação; todos guardados com scheme | modelo-de-dados §6 | decidir se o CPF é obrigatório no cadastro; estado "CPF pendente" |
| **Adaptador Censo Escolar** | Exporta os registros 00/10/20/30/40/50/60 (1ª etapa) e a Situação do Aluno (2ª etapa); reimporta os códigos INEP gerados | leiaute 2026 V5 campo a campo | leiaute da Situação 2026 (não publicado); 2025 tem 7/8 contraditórios |
| **Adaptador Gestão Presente** | Cliente da API CMDEB v2: estudante, matrícula, enturmação, frequência mensal, desempenho, profissionais | OpenAPI lido; divergências Portaria × API documentadas | confirmar com o MEC o alcance da obrigatoriedade (só para redes aderentes) |
| **Currículo** | Extrai a BNCC da fonte oficial do MEC; importa o Currículo Paulista com `derivaDe`; modela os IFAs da Res. CNE/CEB 4/2025 | [bncc/](camada-brasil/bncc/README.md), [bncc-computacao/](camada-brasil/bncc-computacao/README.md), [bncc-dados/](fora-da-fase-1/brasil/bncc-dados/README.md), modelo-de-dados-curriculo §1 | escolher o texto canônico (2017 × 2018); sentido oficial de `*` e A/B/C no CP; volume EM do CP |
| **Avaliação** | Escalas e esquemas de classificação do Saeb, SARESP e CNCA; alinhamento item→habilidade por curadoria | modelo-de-dados-curriculo §2 | cortes atuais do SARESP; escalas Saeb-BNCC |
| **Inclusão / PEI** | Estudo de caso, PAEE/PEI com o mínimo federal (Port. 421 arts. 10–11) e o formato SP (Anexos II–V), prazos e revisões | modelo-de-dados-curriculo §3 | posição jurídica sobre laudo (SP 129 × MEC 421) |
| **Regras LDB** | Validação de carga, dias letivos, frequência de 75% (e 60% na EI), idade por etapa | modelo-de-dados §5 | conferir a redação literal da LDB |
| **Privacidade BR** | Base legal por operação, sensibilidade por campo, consentimento parental, ECA Digital | fichas lgpd-educacao e eca-digital | papéis de controlador e operador; prazos de guarda |

### 4.2 Ordem de construção sugerida (pelo risco)

1. **Core + identidade + organização + matrícula** (C.ORG, C.PER, C.ROL, C.IDN, C.ENR, C.GRP, C.SES). Tudo depende disso, e é onde o Censo e o CMDEB mais divergem.
2. **Vocabulários e mapeamentos** (C.VOC, C.MAP), com o Censo 2026 e o CMDEB carregados e o crosswalk entre eles.
3. **Currículo** (C.CFW, C.CMP, C.CAS, C.ADP) a partir do dataset verificado. É pré-requisito da camada curricular das micro-atividades.
4. **Inclusão e PEI** (C.SUP, C.ELG, C.PLN). É o núcleo de valor da interface do professor.
5. **Exportação para o Censo e a API CMDEB.** Só é necessária quando uma rede pedir, e sai mais barata depois dos itens 1–2.
6. **Avaliação externa** (Saeb, SARESP). Serve de referência para relatórios; prioridade menor.

## 5. Adaptadores em standby: o que cada um exigiria

| Jurisdição | O que exige do Core (genérico) | O que fica no perfil | Bloqueios | Pasta |
|---|---|---|---|---|
| **EUA** | Atribuição de papel com vigência; catálogo de curso; frequência; rubrica; classificação e registro de divulgação (FERPA) | Descriptors do Ed-Fi; programas de serviço; CCSS e NGSS (composição tridimensional) | Nenhum técnico. Leis estaduais de privacidade variam por estado. | [estados-unidos/](fora-da-fase-1/estados-unidos/README.md) |
| **UE** | Especificação × instância (ELM `specifiedBy`); níveis como `skos:Concept` | Qualificação, crédito, EQF, DigComp; envelope EDC/VC com selo eIDAS | O ELM não cobre turma, matrícula nem calendário: o D1 vem do país-membro. A idade de consentimento digital varia de 13 a 16. | [uniao-europeia/](fora-da-fase-1/uniao-europeia/README.md) |
| **Reino Unido** | Identificador com uso permitido; tipo de registro da matrícula; plano com mantenedor | UPN, ULN, LAESTAB; SEN N/K/E; EHCP A–K; quatro nações separadas | Children's Code (design para crianças) | [reino-unido/](fora-da-fase-1/reino-unido/README.md) |
| **China** | Classificação de dados (L1–L5); registro de residência e transferência; variante de estrutura de anos | JY/T 0633/0637/0639; ID de escola com 10 e de pessoa com 19 caracteres; 学籍 | Implantação no território, operador local, ICP, registro do app educacional, limite de 50% de capital estrangeiro. Dados de menores de 14 anos são sensíveis. | [china/](fora-da-fase-1/china/README.md) |
| **Internacional** | ISCED como pivô de nível; datas, idioma, país e identificadores padronizados | — | Textos ISO e IEEE são pagos | [internacional/](camada-agnostica/internacional/README.md) |

## 6. Riscos

| # | Risco | Mitigação proposta |
|---|---|---|
| R1 | **Core com viés brasileiro**, já que o Brasil é o único adaptador real | Regra P1 (duas jurisdições ou princípio transversal) e teste de neutralidade contra os crosswalks em standby antes de aceitar cada entidade |
| R2 | **Equivalência falsa por transitividade** (BR→Core→EUA) | `exactMatch` só com revisão; SSSOM com confiança e justificativa |
| R3 | **Residência incompleta**: logs, observabilidade, backups ou API de LLM fora do Brasil | Requisito explícito da arquitetura, incluindo SDKs de analytics e de crash no app (§7.9); avaliar fornecedores de LLM com região no Brasil |
| R3a | **Protótipo nos EUA (D7) receber dado real** por atalho ("só um teste") | Condições do §7.8: só dados sintéticos e critério de saída antes de qualquer dado real |
| R4 | **Bypass de RLS** por superusuário, `BYPASSRLS` ou dono da tabela | `FORCE ROW LEVEL SECURITY`; papéis de aplicação sem privilégio; teste automatizado |
| R5 | **Ontologia além de OWL 2 QL** não roda virtualmente no Ontop | Decidir, quando o grafo for desenhado, o que é materializado; manter o Core operacional em QL |
| R6 | **Leiaute do Censo muda todo ano** | Um serializador por ano; testes com os arquivos de exemplo do INEP |
| R7 | **Normas em movimento**: Inue/EducaDados com atos futuros; padrão nacional de interoperabilidade não editado; SP 129 contestada (PDL 30/2025) | Vocabulários e regras como dado versionado; revisão trimestral das fichas |
| R8 | **Dado sensível de inclusão vazando para a personalização** | C.ELG isolado por permissão; a plataforma não infere categoria diagnóstica (LGPD art. 11 §1) |
| R9 | **Custo de governança** de vocabulários e mapeamentos sem dono | "Cada fato tem um dono" vale também para mapeamentos; dono nomeado por ConceptScheme |

## 7. Decisões

Escopo: só arquitetura. Não se gera código nesta etapa.

### 7.1 Decididas em 2026-11-05

| # | Decisão | Consequência na arquitetura |
|---|---|---|
| D1 | **O CPF é o identificador preferencial do estudante.** Quem não tem CPF é cadastrado mesmo assim, ligado a um responsável. | Ver §7.3. A pessoa é referenciada pelo UUID interno, e o CPF é um identificador da lista. Estado de identidade `cpf_pendente`. |
| D2 | **BNCC canônica = edição 2018** (atualização 06/11/2026: a base canônica mora no repositório **vuoo-base** (`fontes/bncc/`, https://github.com/arcade-metrics/v-base): fonte oficial `BNCC_EI_EF_110518_versaofinal_site.pdf` (versão final, EI, EF e EM) e cópia de trabalho `BNCC_reparado.pdf`), extraída por pipeline próprio da fonte oficial do MEC. | A transcrição de 2017 em `brasil/bncc/` fica como fonte histórica. As diferenças entre as duas viram `EdicaoDoTexto` e mapeamento. |
| D4 | **Laudo é campo, não documento.** O VUOO não armazena arquivos; quando houver, a referência vem por API do sistema da rede. | C.DOC passa a guardar só metadados e referência externa (ver §7.4). Não há armazenamento de arquivos clínicos. |
| D5 | **A residência no Brasil vale também para as APIs de LLM e embeddings**, se o produto as usar. | Só serve fornecedor com modelo disponível em região brasileira, a verificar por modelo. É requisito da arquitetura. |
| D6 | **Granularidade mínima do código = Brasil.** SP é o piloto, mas nada é programado especificamente para SP; variações de estado e rede entram como campos opcionais e dados. | Ver §7.5. |

| D1a | **Uma pessoa pode ter vários documentos, e todos ficam sempre vinculados a ela.** Sem CPF, vale por exemplo a certidão de nascimento. | Confirma §7.3. Os documentos são identificadores com scheme presos ao UUID da pessoa, mais o vínculo com o responsável. |
| D3 | **Papéis LGPD conforme §7.6.** Na operação com escola ou rede, a escola/rede é controladora e a Wemoga/VUOO é operadora. *(Revista na segunda rodada: a parte sobre base de pesquisa e CEP caiu com a D14.)* | Ver §7.6. |
| D7 | **O protótipo roda numa máquina virtual na AWS, provavelmente numa região dos EUA, por custo.** A residência no Brasil (D5) vale a partir da versão oficial. | Exceção temporária e registrada. Ver §7.8. |

### 7.1b Decididas em 2026-11-05 (segunda rodada: produto e app)

| # | Decisão | Consequência na arquitetura |
|---|---|---|
| D8 | **O produto VUOO é independente do projeto de pesquisa com o CIATec/CCD** e começa do zero. A proposta em `projeto/` é só contexto. | Nenhum requisito, métrica ou prazo vem das fases, pacotes ou amostras do projeto. |
| D9 | **O cliente é a escola ou a rede.** Na versão inicial existe também o **uso avulso**: o aluno baixa e usa sem escola, para ter a experiência, e entra numa **rede geral** com um **professor geral**. | A rede geral é um tenant como os outros, operado pela Wemoga. Ver §7.6 (controlador) e §7.9. |
| D10 | **Entrega inicial: app nativo Android e iOS, instalado no celular do aluno**, com micro-atividades de 5 a 15 minutos por dia. | O app é o cliente principal; a web fica para professor e gestão. |
| D11 | **Autorização dos pais com o menor atrito possível.** Na rede, o responsável recebe um link que já o autentica. No uso avulso, a autorização do responsável entra no fluxo de instalação. | Nenhum dado do aluno é coletado antes de a autorização estar registrada; o primeiro acesso exige rede. Ver §7.9. |
| D12 | **Offline: trilhas baixadas no aparelho; resultados guardados e enviados quando houver rede.** Provisório: uma trilha por semana, a rever depois dos testes de peso. | Fila local de eventos; pacotes de trilha versionados. Ver §7.9. |
| D13 | **Captura de interação no celular e no tablet: toque, gestos e sensores inerciais. Sem visão computacional.** Também entra um **rastreamento de uso do app inteiro**, além dos eventos de atividade. | Dois fluxos no mesmo pipeline: atividade e uso do app. Séries de sensores em bloco. Ver §7.9. |
| D14 | **Não há base de pesquisa no produto.** | O silo de pesquisa e o pipeline com CEP saem da arquitetura (§7.7). |
| D15 | **O histórico acompanha o aluno, que é o titular dos dados.** A migração entre escolas acontece por requisição da nova escola e aprovação do aluno ou responsável, e fica sempre disponível. A escola anterior mantém o histórico do período em que o aluno esteve lá. A nova escola lê o histórico anterior sem nenhum dado que identifique a escola de origem. | Matrícula como concessão de acesso; repositório do aluno por pessoa; view com a organização ocultada. Ver §7.9.6. |
| D16 | **Cadeia global para quem não tem escola:** rede geral → escola geral → turma geral → professor geral, com a mesma estrutura de uma rede real. No Brasil é o `global_brazil`, criado com estrutura simulada **depois que o resto estiver implementado**. | Tenant comum operado pela Wemoga; professor geral é papel de sistema; alunos da turma geral não se veem. Ver §7.9.6. |
| D17 | **Sensores e toque são normalizados no aparelho** para permitir comparação geral. Taxa máxima inicial de 100 Hz; taxas diferentes são permitidas por sistema e aparelho, sempre registradas, e tratadas na estatística depois. | Biblioteca única de normalização para Android e iOS, versionada no envelope. Ver §7.9.7. |
| D18 | **O aluno avulso não compartilha dados com ninguém; os dados são dele.** Se ele decidir entrar numa escola, pode levar o histórico, pelo fluxo da D15. | Na rede geral não há concessão a terceiros; a única saída é a migração aprovada pelo titular. |
| D19 | **Revogação pelo titular, sem prazo e sem veto.** A escola recebe um aviso e precisa dar um "ciente", que só registra que ela soube e não limita a exclusão. Continua existindo o registro de que o aluno esteve na escola, mas ele deixa de estar ligado aos dados de atividade. O histórico de atividade daquele período deixa de ser visível para a escola. | Ver §7.9.6, "Revogação". |
| D20 | **Opção B aprovada:** Core próprio mínimo + perfis por jurisdição + mapeamentos como dado. O Core v0.1 é a base dos ADRs. | §1–§3 deixam de ser proposta quanto à opção; as entidades seguem em revisão. |
| D21 | **Revogação em camadas, cada uma opção do titular:** (1) tirar o acesso da escola; (2) tirar os dados do treino do VUOO; (3) exportar os dados; (4) revogar tudo. O treino do VUOO cruza com o **perfil da escola**, senão não há como cruzar os dados. A comunicação de cada camada é clara e suave. | Base de treino com perfil da escola; ferramenta de exportação; ver §7.9.6, "Camadas de revogação". |
| D22 | **O repositório do aluno é do aluno**, fora de qualquer tenant. Ele é relacionado depois a uma rede, como **titular** (vínculo atual), **legado** (vínculo anterior) ou **global** (sem vínculo, `global_brazil`). | Nenhum dado do aluno dentro de silo de rede; nenhuma cópia na migração. Ver §7.9.6. |

### 7.2 Ainda pendentes

1. **Peso da trilha semanal e janela offline** (validade do login sem rede), a fixar depois dos testes.
2. **Dicionário de variáveis de atividade e telemetria**, com as features calculadas no aparelho e a fração de amostra bruta. É decisão de produto: vai para o PRD desta solução e o desenho das micro-atividades, não para este relatório.
3. **Perfil da escola no treino:** quais atributos entram (tipo de rede, região, porte, faixas de indicadores…) e em que granularidade, para não reidentificar escola pequena (§7.9.6).
4. **Textos das camadas de revogação** e formato da exportação, com o jurídico.
5. **Comparação entre aparelhos:** sem banco de testes por enquanto; atraso de toque e ruído de sensor são ajustados ao longo do desenvolvimento, com o perfil do aparelho registrado em cada evento (D17).

Resolvidas: passagem do avulso para a rede (D15, D18); papel do professor geral (papel de sistema, D16); taxa dos sensores (até 100 Hz, D17); compartilhamento no avulso (não há, D18); revogação (D19, D21); Opção B (D20); repositório do aluno fora dos silos (D22).

### 7.3 Estudante sem CPF

O identificador agnóstico do Core é o **UUID interno da pessoa** (C.PER). É ele que matrícula, plano e eventos referenciam. Documentos são **identificadores** (C.IDN `{scheme, issuer, value, vigência, status}`) presos a esse UUID. Não existe um "document_id global" que substitua o CPF; existe uma pessoa estável com vários documentos opcionais.

Para quem não tem CPF:

1. **Vínculo com o responsável** (C.REL): o estudante aponta para a pessoa do responsável, que tem seu próprio CPF ou documento. O vínculo tem tipo (mãe, pai, tutor legal…), vigência e direitos (consentimento, acesso).
2. **Outros documentos do próprio estudante**, cada um com seu scheme, na ordem que o INEP usa:
   - matrícula da certidão de nascimento nova (32 dígitos, `br-certidao`);
   - ID INEP, quando já existir (`br-inep-pessoa`);
   - para estrangeiros, RNM/CRNM ou passaporte (`br-rnm`, `passport`, com país emissor).
3. **Estado de identidade** `cpf_pendente`, com data e motivo. A rede é avisada para regularizar; a LC 220/2025 exige o CPF.
4. **Deduplicação** por nome + data de nascimento + filiação + município de nascimento, sempre com revisão humana. Nunca há fusão automática de pessoas.

**Regra:** o CPF do responsável nunca é usado como identificador do estudante. Ele não distingue irmãos, mistura titulares de dados (LGPD) e quebra a deduplicação. O responsável é outra pessoa, ligada por C.REL.

[I] Hoje o CPF costuma ser emitido junto com a certidão de nascimento, então o caso "sem CPF" tende a se concentrar em estrangeiros e registros antigos. Isso não foi verificado na pesquisa.

### 7.4 Laudo como campo

A recomendação é guardar o **mínimo**:

- tipo de documento (laudo, relatório, parecer pedagógico, CIPTEA);
- categoria do emissor (médico, psicólogo, escola…);
- data de emissão e validade;
- situação (apresentado, pendente, em investigação);
- **referência externa** (sistema de origem + id), para consulta por API.

Evitar CID e texto clínico enquanto nenhuma regra de negócio exigir. Mesmo sem o arquivo, esses campos continuam sendo **dado sensível** (LGPD art. 11), porque revelam condição de saúde. Ficam junto da elegibilidade (C.ELG), com acesso isolado, e não alimentam a personalização.

### 7.5 Variações de estado e rede sem código específico

Regra: **o que varia por estado ou rede tem que caber em dado**, num destes cinco mecanismos que o Core já tem:

| Variação (exemplo SP) | Mecanismo | Código novo? |
|---|---|---|
| RA do aluno (SED-SP) | mais um identificador: C.IDN com scheme `br-sp-ra` | não |
| Currículo Paulista | C.CFW de esfera estadual + C.ADP (a rede adota) + associação `derivaDe` com a BNCC | não |
| Níveis de apoio 1–3, formulário de PEI de SP | vocabulário (C.VOC) com dono SEDUC-SP; seções opcionais do plano; o mínimo federal da Port. 421 é o obrigatório | não |
| Cortes do SARESP | esquema de classificação (C.PCS) | não |
| Prazos locais (PEI em 30 dias letivos) | regra de validação como dado (shape SHACL opcional, ligada ao tenant) | não |

Consequência: o perfil `vuoo-br` tem campos **obrigatórios** só onde a lei federal manda (LDB, Censo, CMDEB, Port. 421) e campos **opcionais** para o resto. A integração com a SED-SP, quando vier, é um adaptador de troca como outro qualquer, sem alterar o Core nem o perfil.

### 7.6 Papéis LGPD: proposta

Sim, os papéis são da escola/rede e do VUOO, mas dependem de **quem decide a finalidade** em cada uso do dado:

| Uso | Controlador (decide para quê) | Operador (trata em nome de) |
|---|---|---|
| Operação pedagógica: turma, PEI, atividades, relatórios ao professor | **escola ou rede** (quem contrata; na pública, a secretaria) | **VUOO** |
| Uso avulso na rede geral (D9) | **Wemoga/VUOO** (não há escola; a finalidade é do produto) | — |
| Rastreamento de uso do app (D13) | o controlador do tenant, para a operação; VUOO só com dado agregado | VUOO |
| Melhoria do produto com dado agregado ou anonimizado | VUOO, se o dado não for mais pessoal | — |
| Treino dos modelos de predição do VUOO, com dado pseudonimizado e perfil da escola (D21, §7.9.6) | **VUOO**, com consentimento próprio do responsável, revogável à parte `[A CONFIRMAR: jurídico]` | — |

Na arquitetura:

- o acordo por tenant (C.AGR) fixa finalidades e papéis; na rede geral, o acordo é o termo de uso aceito pelo responsável;
- a base legal é registrada por operação (C.CNS); no avulso, o consentimento do responsável (LGPD art. 14) é a base da coleta;
- uso do app e eventos de atividade têm finalidades diferentes, então têm base legal e retenção próprias.

### 7.7 Base de pesquisa: fora do produto

Decisão D14 (2026-11-05): o produto não tem base de pesquisa. Saem da arquitetura o silo físico, o pipeline de anonimização com protocolo CEP e a regra de que dado de neurodivergência só existe na pesquisa. As fichas de `conhecimento/dados-pesquisa-e-eventos/research-ethics/` continuam como conhecimento, mas não orientam o produto.

Se um parceiro de pesquisa quiser dados no futuro, isso é uma **exportação** sob acordo próprio (C.AGR) com registro de divulgação (C.DSC), e não um componente da plataforma.

### 7.8 Protótipo fora do Brasil (exceção temporária)

**Registro:** em 2026-11-05 ficou decidido que o protótipo roda numa máquina virtual única na AWS, provavelmente numa região dos EUA, por custo. A residência no Brasil, inclusive para LLM (D5), vale a partir da **versão oficial**.

Condições propostas para que a exceção não crie risco:

1. **Nenhum dado pessoal real de estudante, responsável ou profissional no protótipo.** Só dados sintéticos ou simulados. Dados reais nos EUA seriam transferência internacional de dados de crianças (LGPD art. 33).
2. **Testes de campo com crianças reais**, inclusive no modo avulso, só depois da célula BR.
3. **A região é parâmetro, não premissa:** infraestrutura descrita como código, sem dependência de serviço disponível só em região americana. A migração para o Brasil deve ser uma reimplantação, não uma reescrita.
4. **A célula BR (§2) é o desenho-alvo.** No protótipo, tudo fica numa VM só. O isolamento por tenant vale a partir da versão oficial e é validado antes de qualquer dado real.
5. **Critério de saída:** nenhum piloto com escola real e nenhum aluno avulso real antes da célula brasileira estar no ar.

### 7.9 Dados do app: volume, latência, offline e pipeline (proposta)

Discussão de 2026-11-05 sobre as decisões D9 a D13. Os números são estimativa nossa [I], sem medição; servem para dimensionar, não para contratar. Base: `conhecimento/dados-pesquisa-e-eventos/` (events, quality) e `conhecimento/realtime-multiplayer/reliability-security/` (entrega, reconexão).

#### 7.9.1 Volume

Premissas: 5 a 15 minutos por dia, cerca de 10 minutos dentro de atividade.

| Fluxo | Bruto por dia, por aluno | Comprimido |
|---|---|---|
| Eventos discretos de atividade (resposta, acerto, tentativa, tempo de reação) | ~150 KB | ~30 KB |
| Toque e gestos (amostras coalescidas, só durante o contato) | ~200 KB | ~60 KB |
| Sensores inerciais (acelerômetro + giroscópio, 6 eixos, de 60 a 100 Hz conforme o aparelho, só dentro da atividade, binário) | ~1 a 1,7 MB | ~0,4 a 0,7 MB |
| Uso do app (abertura, telas, navegação, erros) | ~30 KB | ~10 KB |

Total: de 1,4 a 2 MB bruto e de 0,5 a 0,8 MB comprimido por aluno por dia, ou seja, de 10 a 25 MB por mês. Com 100 mil alunos, o armazenamento cresce de 1,5 a 2,5 TB por mês. Com normalização e features no aparelho (D17), o que sobe de série bruta é só a amostra de validação. O custo é baixo e a vazão é modesta.

Leitura:

- **Os sensores inerciais são quase todo o volume.** A taxa e o que se calcula no aparelho (features em vez de série bruta) são a alavanca principal (§7.2, item 5).
- **O que pesa para a família é a rede, não o servidor.** Upload: eventos discretos e de uso vão por qualquer rede; séries brutas, por padrão, só por Wi-Fi. Download: o pacote de trilha semanal tem orçamento de tamanho, reaproveita a biblioteca de imagens já instalada e baixa só a diferença entre versões.
- **Série amostral não é linha no banco.** Ela vai como bloco comprimido para armazenamento de objetos, referenciada pelo evento discreto que a contém.

#### 7.9.2 Latência

| Laço | Onde roda | Requisito |
|---|---|---|
| Estímulo → resposta → feedback na atividade | no aparelho | um quadro, sem rede |
| Progressão na trilha (próxima atividade, recompensa) | no aparelho, com as regras do pacote | sem rede |
| Envio de resultados | em segundo plano, quando houver rede | de minutos a dias |
| Telas do professor, da gestão e dos pais | API | requisição e resposta comum |

Não há tempo real de rede no produto: nenhum WebSocket, servidor autoritativo ou predição. O "tempo real" do VUOO é de **medição**, resolvido no aparelho com relógio monotônico, âncora de sessão e número de sequência (`dat.qual.clocks-and-ordering`).

O requisito novo é o **frescor**. O servidor vê o aluno na última sincronização, então toda tela de professor mostra "sincronizado em …". Sem isso, quem fez a atividade sem rede parece quem não fez.

#### 7.9.3 Offline e app

- **Fatos, não estado.** O app envia resultados como eventos imutáveis (C.EVT), cada um com a versão da trilha e do conteúdo em que foi feito. O servidor recalcula progresso, sequência de dias e recompensas. Não há edição concorrente do lado do aluno, então não há CRDT. O lado do professor (PEI, observações) fica online.
- **Fila local** em banco do próprio app (SQLite), com `id` e sequência gerados no aparelho e gravados antes do envio. O envio é em lote e idempotente, e só sai da fila o que o servidor confirmou (`dat.qual.loss-and-deduplication`).
- **Segundo plano:** o agendador do Android é confiável; no iOS a execução em segundo plano é oportunista. A regra é sincronizar ao abrir, ao fechar e ao terminar uma atividade, e tratar o segundo plano como bônus.
- **Pacote de trilha** versionado e assinado: manifesto, regras de progressão e mídia. Provisório: uma semana à frente (D12).
- **Relógio:** a sequência de dias usa a data local derivada da âncora monotônica e confere com a hora de recebimento no servidor, porque a criança pode adiantar o relógio do celular.
- **Dado local mínimo:** a fila carrega o UUID da pessoa, nunca nome nem CPF, e é limpa depois da confirmação.

#### 7.9.4 Autorização e identidade no app

- **Primeiro acesso exige rede.** Nenhum evento do aluno é gravado antes de a autorização do responsável estar registrada (C.CNS). Isso é candidato a regra de negócio.
- **Na rede:** a escola cadastra o aluno, e o responsável recebe um link de uso único que o autentica e registra a autorização. O app do aluno é vinculado por código ou QR gerado nesse fluxo.
- **No avulso:** o fluxo de instalação pede o contato do responsável, e a autorização chega pelo mesmo tipo de link. O aluno entra no tenant da rede geral (D9).
- **Login do aluno sem e-mail nem senha:** o aparelho vinculado é a credencial, com renovação periódica quando houver rede. A validade sem rede é a da janela offline (§7.2, item 4).

#### 7.9.5 Pipeline de eventos

1. **Envelope CloudEvents 1.0** com extensões VUOO: sequência por sessão, carimbo monotônico, âncora e fonte do relógio, versão do conteúdo e hash da configuração ativa (`dat.ev.event-model`). O ator é o UUID interno. xAPI e Caliper são views de exportação.
2. **Dois fluxos no mesmo envelope:**
   - **atividade**: pedagógico, alimenta progresso e relatórios;
   - **uso do app**: produto e operação.

   Os dois têm `type`, finalidade, base legal e retenção próprios (§7.6).
3. **Séries amostrais** (toque, sensores) como bloco em armazenamento de objetos, referenciado pelo evento discreto.
4. **Ingestão por HTTP em lote**, com `Idempotency-Key`, deduplicação por `(source, id)`, hora de recebimento e detecção de lacunas por sequência como métrica de perda.
5. **Log de eventos imutável** como fonte de verdade só para C.EVT. O resto do Core segue relacional e bitemporal, sem event sourcing completo nem CQRS (`dat.ev.event-sourcing`).
6. **Projeções** sobre o log: progresso e recompensas, painel do professor, métricas de uso do produto e exportação xAPI. Guardar o bruto desde o primeiro dia permite que modelos futuros sejam só projeções novas.
7. **Sem fila de mensagens dedicada no começo:** Postgres e armazenamento de objetos, com a fila como porta substituível.
8. **Nada de SDK de analytics ou crash de terceiros mandando dado para fora da célula.** O rastreamento de uso (D13) passa pelo mesmo pipeline, ou por ferramenta hospedada na célula BR (D5, R3).

**Sessão de atividade:** C.SES é o calendário letivo (`AcademicSession`), e o evento precisa de contexto próprio. Entra no Core como C.ASN (`ActivitySession`), em D6, junto com C.EVT.

#### 7.9.6 Histórico do aluno, concessões e cadeia global (D15, D16)

**Enquadramento LGPD.** O aluno é o **titular**; "propriedade" não é conceito da LGPD. Na operação, o controlador é a escola ou a rede. A migração é **portabilidade iniciada pelo titular** (art. 18), e a escola nova passa a controlar o que recebe. Para menor de idade, quem aprova é o responsável; o adolescente dá o aceite junto (art. 14).

**Matrícula como concessão.** Eventos e resultados ficam ligados à pessoa (UUID) e à matrícula em que foram gerados. O acesso de uma organização vem de uma concessão (C.GRT):

| Situação | Concessão |
|---|---|
| Matrícula ativa | automática, leitura e escrita, enquanto a matrícula vale |
| Escola anterior, depois da saída | só leitura, limitada ao período em que o aluno estava lá |
| Escola nova, histórico anterior | só leitura, por requisição da escola e aprovação do titular ou responsável, revogável |

A concessão tem quem recebe, escopo (matrículas ou períodos), categorias de dado, finalidade, base legal (C.CNS), vigência e revogação, e é bitemporal como os demais vínculos. Cada acesso fica no registro de divulgação (C.DSC).

**O que migra, por categoria:**

| Categoria | Padrão |
|---|---|
| Atividades e resultados (gerados pelo aluno) | migra |
| PEI e plano de apoio | só com aprovação explícita |
| Observações livres do professor | não migra, porque texto livre costuma identificar a escola |

**Organização oculta.** A escola nova vê o histórico por uma view que troca rede, escola, turma e professor por "vínculo anterior n (período)". Isso é **minimização, não anonimato**: a versão do currículo adotado, o calendário e o conteúdo da rede ainda podem indicar a origem. O aluno e o responsável veem tudo.

**Repositório do aluno (D22).** O repositório é do aluno e fica fora de qualquer tenant, dentro da célula. Ele se relaciona com redes por três tipos de vínculo:

| Vínculo | Quando | Acesso da rede |
|---|---|---|
| **titular** | matrícula ativa | leitura e escrita, pela concessão da matrícula |
| **legado** | matrícula encerrada | só leitura do período em que o aluno esteve lá |
| **global** | aluno sem escola | `global_brazil`, sem acesso humano (professor geral é papel de sistema) |

**Isolamento e sem redundância.** Os dados de organização (turmas, professores, PEI na escola) seguem isolados por tenant. Os dados do aluno ficam só no repositório dele, acessado por concessão. Cada evento é gravado **uma vez**:

- migrar é criar uma linha de concessão, não copiar dados;
- painéis e relatórios da escola são projeções recalculáveis, sem cópia do bruto;
- os eventos referenciam a versão do conteúdo, não o conteúdo;
- a série bruta sobe só como amostra de validação (D17).

Uma rede que exija banco dedicado isola nele só os dados de organização; **o repositório do aluno nunca vai para dentro do silo** (D22). Assim nenhuma migração gera cópia.

**Revogação (D19).** O titular revoga, e a revogação vale na hora:

1. A concessão da escola termina, e a escola deixa de ver o histórico de atividade do aluno naquele período. Painéis e relatórios são recalculados sem ele.
2. A escola recebe o aviso e precisa dar o "ciente". O ciente é registrado, mas não condiciona nada.
3. O **registro de que o aluno esteve na escola** (matrícula, vigência e os registros legais que a escola é obrigada a guardar) continua existindo, mas sem ligação com os dados de atividade.
4. O aluno continua com o histórico inteiro no repositório dele.
5. Fica um registro da revogação, sem o conteúdo, para prestação de contas (C.DSC).

**Camadas de revogação (D21).** Cada camada é uma escolha separada do titular (ou do responsável), mostrada nesta ordem, da mais leve para a mais forte:

| Camada | O que acontece | O que continua |
|---|---|---|
| 1. Tirar o acesso da escola (D19) | a escola deixa de ver o histórico de atividade; recebe aviso e dá ciente | o registro de que o aluno esteve lá; o repositório do aluno; o treino do VUOO |
| 2. Tirar do treino do VUOO | os dados do aluno saem da base de treino e não entram em treinos novos | o uso do app; os modelos já treinados não são desfeitos, mas o próximo treino não usa os dados |
| 3. Exportar os dados | o titular baixa o histórico (portabilidade, LGPD art. 18 V) em formato aberto (JSON/CSV, com view xAPI) | tudo; exportar não revoga nada |
| 4. Revogar tudo | eliminação dos dados do aluno (art. 18 VI) e encerramento da conta | só os registros legais que a escola é obrigada a guardar e o registro da própria revogação |

**Treino com perfil da escola.** O treino do VUOO precisa cruzar os dados do aluno com o **perfil da escola**, senão não há como comparar contextos. A base de treino guarda:

- um pseudônimo do aluno e um pseudônimo da escola, para que o modelo trate a escola como agrupamento;
- atributos de perfil da escola, generalizados (tipo de rede, região, porte, faixas de indicadores), lista a fechar (§7.2, item 3);
- nenhum nome, CPF, código INEP ou nome de escola.

A chave entre o aluno e o pseudônimo fica do lado do repositório do aluno, não na base de treino. É ela que permite cumprir a camada 2 depois.

**Comunicação suave e verdadeira.** Na camada 1, a mensagem deixa claro, sem alarme, que a escola não verá mais o histórico e que os dados continuam ajudando o VUOO **sem o nome do aluno e sem o nome da escola**. A mensagem também mostra, na mesma tela, as camadas 2 a 4 como opções. Ela não promete anonimato: pela LGPD, dado pseudonimizado ainda é dado pessoal (art. 12), e por isso o treino tem consentimento próprio e revogável. Textos com o jurídico (§7.2, item 4).

**Cadeia global (`global_brazil`).** É um tenant comum, operado pela Wemoga, com a mesma hierarquia de uma rede real: rede geral, escola geral, turma geral e professor geral. Assim, compartilhar, migrar e os relatórios funcionam igual nos dois modos. O professor geral é **papel de sistema**: feedback automático e conteúdo padrão, sem pessoa olhando os dados. Alunos da turma geral **não se veem** (sem lista nem ranking entre crianças desconhecidas). A estrutura é criada como simulação depois que o resto estiver implementado. Na migração do avulso para uma escola, vale o mesmo fluxo de concessão.

#### 7.9.7 Normalização no aparelho (D17)

Objetivo: comparar alunos de forma geral, entre aparelhos e sistemas.

| Camada | Diferença entre plataformas | Normalização |
|---|---|---|
| Unidades | o iOS entrega aceleração em g, o Android em m/s²; cada um separa a gravidade de um jeito | SI (m/s², rad/s), gravidade separada, orientação da tela registrada |
| Tempo | carimbos desde o boot, com resoluções diferentes; a taxa real oscila | relógio monotônico; reamostragem para a taxa-alvo; registro da taxa real e da variação |
| Toque | pixel, ponto e dp; tamanhos de tela; taxa de toque de 60 a 240 Hz; pressão ausente em muitos aparelhos | coordenadas em mm físicos e relativas ao alvo; tempo desde o início do estímulo |
| Aparelho | ruído do sensor e atraso do toque variam por modelo | perfil do aparelho; alguns segundos de "aparelho parado" no início da sessão para medir o ruído de base |
| Features | — | medidas calculadas no aparelho (tempo de reação, tempo de movimento, desvio de trajetória, jerk, energia na faixa de tremor…), lista a definir (§7.2, item 4) |

- **Taxa:** máximo inicial de 100 Hz. Cada aparelho entrega o que o sistema permitir até esse teto, e a taxa efetiva vai no evento. As diferenças de taxa são tratadas na estatística depois, sem exigir taxa igual de todos. Acima de 200 Hz o Android 12+ pede permissão especial (a verificar); com teto de 100 Hz, isso não se aplica.
- **Uma implementação só:** a mesma biblioteca de normalização para Android e iOS. Duas implementações do mesmo algoritmo quebram a comparabilidade.
- **Versionada:** cada evento leva a versão do normalizador e o perfil do aparelho. Uma versão nova não mistura dados sem marcação.
- **Amostra bruta:** uma fração das sessões sobe também em bruto, só por Wi-Fi, para validar e recalibrar o normalizador.
- **Efeito de aparelho no servidor:** com muitos alunos, o efeito de cada modelo pode ser estimado estatisticamente. A base de conhecimento não tem medição publicada de atraso em aparelhos usados por crianças (`dat.relatorio`, lacuna 1), por isso o banco de testes próprio (§7.2, item 5).

## 8. Próximos passos

1. **Revisão humana** deste relatório e de [core/README.md](camada-agnostica/core-v0.1.md).
2. **Matriz única de neutralidade** (entidade do Core × 5 jurisdições), consolidando os crosswalks.
3. **ADRs candidatos:**
   - Core como ontologia com perfis;
   - regras de extensão;
   - mapeamentos SSSOM;
   - identificadores com scheme;
   - bitemporalidade;
   - célula por jurisdição e tenant por rede;
   - grafo híbrido;
   - app offline com fila local e pacotes de trilha;
   - pipeline de eventos (envelope, dois fluxos, séries em bloco, ingestão idempotente);
   - repositório do aluno por pessoa e matrícula como concessão de acesso (D15);
   - normalização de sensores e toque no aparelho, com biblioteca única e versionada (D17).
4. **Fechar as lacunas que bloqueiam o Brasil** ([brasil/README.md](camada-brasil/README-estudo-brasil.md), "O que falta").
5. **Prova de conceito pequena:** `vuoo-core` em OWL com C.ORG, C.PER, C.ROL, C.IDN, C.ENR e C.GRP; shapes `vuoo-br`; carga de uma escola fictícia; exportação para o registro 60 do Censo e para OneRoster. Isso valida a cadeia ontologia → relacional → R2RML → views.

## 9. Limites desta pesquisa

- **Brasil:** a LDB foi lida em paráfrase (o download falhou). O site do SARESP respondeu 403. Os textos das DCN de 2009/2010 não foram abertos.
- **ISO/IEEE e ISCED:** os textos ISO e IEEE são pagos. Os PDFs oficiais do ISCED deram 404/403, e parte dos códigos ISCED-F veio de reprodução secundária.
- **China:** JY/T 0643—2025 (proteção de dados em plataformas educacionais) e o formato oficial do 学籍号 não foram verificados.
- **Reino Unido:** a Curriculum for Wales veio de conhecimento prévio (as páginas deram 404).
- **EUA:** os tipos de extensão do Ed-Fi e as enumerações do Edu-API não foram verificados.
- **Onde estão as lacunas:** cada pasta lista as suas em `questoes-abertas*.md`, e as afirmações não verificadas estão marcadas `[I]` ou `not_found`.
