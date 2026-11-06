# Padrões de arquitetura: núcleo canônico, extensões e mapeamentos

**Pasta:** `base/camada-agnostica/` · **Escrito em:** 2026-11-05 · **Status:** pesquisa; nada aqui é decisão até virar ADR.

> **Produto independente (2026-11-05).** O produto VUOO é independente do projeto de pesquisa com o CIATec/CCD; `projeto/vuoo.md` é só contexto. As menções à proposta, às fases F1.x e F2.x e à base de pesquisa foram revistas; as decisões valem as de [../relatorio-infra-vuoo.md §7](../relatorio-infra-vuoo.md).

**Pergunta:** como sistemas reais estruturam *núcleo canônico + extensões + mapeamentos*, para fundamentar o Core agnóstico e os adaptadores regionais do VUOO ([briefing §2 e §9](../padroes-README.md)). Evidências numeradas `E01…E54` em [evidencias-arquitetura.md](evidencias-arquitetura.md). Inferência própria: **[I]**. Não encontrado: `not_found`.

**Base já existente (citada, não reescrita):**
mapeamento e proveniência (`iop.fund.mapeamento-e-proveniencia`),
identidade e contexto,
dados × protocolo,
comparação de rostering,
modelo conceitual e separação de camadas do grafo,
versionamento e proveniência,
papéis escolares,
e a estratégia de dado normativo verificado em [bncc-dados](../fora-da-fase-1/brasil/bncc-dados/01-arquitetura.md) e [aplicação ao VUOO](../fora-da-fase-1/brasil/bncc-pacotes/10-aplicacao-vuoo.md). Entidades `C.xxx` são as provisórias de [_convencoes.md §4](../_convencoes.md).

## Resumo em 10 linhas

1. Os padrões maduros separam três mecanismos que costumam ser confundidos: **extensão aditiva** (Ed-Fi Extensions, OneRoster `metadata`, Clever `ext`), **perfil restritivo** (OneRoster profiles, DCAT-AP, ELM) e **projeção de acesso** (Ed-Fi API Profiles).
2. O modelo que melhor descreve "Core agnóstico + adaptador regional" é o da UE/SEMIC: **Core Vocabulary neutro de contexto + Application Profile** com ontologia reutilizada, shapes SHACL e vocabulários obrigatórios (E24–E27); o ELM o aplica à educação (E23).
3. Vocabulários controlados viram **dado com dono**: o namespace do descriptor Ed-Fi diz quem governa o valor, e desde a v4.0 o mapeamento entre vocabulários também é dado (E03–E05).
4. Para crosswalk entre jurisdições, **CASE é pobre** (só `exactMatchOf`, de sentido estreito, e `isRelatedTo`; E17–E18); SKOS tem a gradação necessária (E20) e SSSOM dá os metadados do mapeamento (E21).
5. Plataformas de rostering (Clever, ClassLink, SDS) normalizam para um **modelo próprio parecido com OneRoster**, guardam o id da fonte como atributo e não como chave (E39–E44).
6. Nenhuma plataforma pública encontrada mapeia currículos de **vários países** num grafo; o caso mais próximo, o Learning Commons KG, usa um **pivô** (CCSS) e Jaccard sobre componentes (E49–E50).
7. Residência: multinacionais operam **células por jurisdição** e, na China, até operador separado (E45); o pacote de "data region" do Google não cobre logs (E46).
8. Para isolamento de tenant, o critério da AWS é explícito: o perfil regulatório do dado empurra para silo (E53).
9. Grafo × operacional: o padrão OBDA/VKG (R2RML + Ontop) permite SPARQL sobre o relacional sem copiar dado (E36–E38); o Ed-Fi já publica OneRoster como **view derivada** do canônico (E09).
10. Proposta: Core próprio e mínimo em OWL/SKOS, adaptadores como Application Profiles, mapeamentos como dado, ACL por jurisdição, células de implantação por jurisdição, e o grafo em duas formas (curado nativo, aluno virtual/materializado).

---

## P1. Núcleo canônico e mecanismos de extensão nos padrões

### 1.1 Comparação

| Padrão | Núcleo | Extensão aditiva | Vocabulário extensível | Perfil | Mapeamento entre vocabulários | Validação |
|---|---|---|---|---|---|---|
| **Ed-Fi** | Data Standard (UDM) | Extension Framework: entidade nova, extensão de entidade, subclasse; fora disso é proibido (E01); API: `_ext` e rota `/<namespace>/…` (E02) | descriptors com namespace = governança (E03, E04) | **API Profiles** = projeção por cliente (IncludeOnly; campos novos ficam fora por padrão) (E06, E07) | **mapeamento de descriptors como dado** desde a v4.0 (E05) | API Guidelines (ver `iop.ros.ed-fi`) |
| **OneRoster 1.2** | Base + 12 classes | **só** em `metadata` (E11); operações novas permitidas, mudar as existentes não (E10) | 5 enums, termos com `ext:` (E12) | **perfil restritivo**: remove opcionais, aperta restrições, nunca acrescenta (E13, E14) | não tem | certificação 1EdTech |
| **CEDS** | dicionário de elementos | n/a (é referência) | é o próprio vocabulário | n/a | **CEDS Align**: cada sistema mapeia seu dicionário ao CEDS e compara mapas (E29) | não tem |
| **CASE 1.1** | CFDocument/CFItem/CFAssociation | atributo `extensions` em várias classes (E19) | `CFAssociationTypeEnum` com `ext:` (E17) | não define | `exactMatchOf` (item derivado → item original), `isRelatedTo`, `isTranslationOf`, `replacedBy` (E17, E18) | suíte de certificação |
| **SKOS** | Concept/ConceptScheme | n/a | cada esquema é um vocabulário | n/a | `exactMatch` (transitiva), `closeMatch` (não transitiva), `broad/narrow/relatedMatch`, com disjunções (E20) | condições de integridade S46 etc. |
| **JSON-LD 1.1** | contexto | contextos adicionais | n/a | n/a | n/a | n/a; `@protected` evita que um contexto local redefina termos do núcleo (E22) |
| **SHACL** | — | — | — | shapes = perfil executável (`kg.std.shacl`) | — | relatório de validação |
| **ELM (UE)** | ontologia ELM | perfis específicos | listas controladas europeias (EQF, ESCO, ISCED-F) | **APs**: LOQ, EDC, AMS, PID, cada um com SHACL; JSON Schema só no EDC (E23) | via vocabulários comuns | SHACL |
| **SEMIC / DCAT-AP** | Core Vocabularies, neutras de contexto (E24) | perfil pode adicionar classes e propriedades, desde que **não sejam parecidas** com as do núcleo (E26) | perfil deve incluir os vocabulários obrigatórios e pode acrescentar outros (E26) | AP = ontologia reutilizada + shapes (E25); perfis nacionais (DCAT-AP.de) e temáticos (GeoDCAT-AP) (E27) | n/a | SHACL publicado e validador |
| **W3C PROF** | — | — | — | descreve um perfil e seus artefatos por papel: validação, restrições, schema, vocabulário (Note 2019, papéis "at risk") (E28) | — | — |

### 1.2 Leitura

**Três operações diferentes, três mecanismos diferentes** [I]:

| Operação | O que faz | Onde aparece | Risco se misturada |
|---|---|---|---|
| **Restringir** (perfil) | aperta cardinalidade, fixa vocabulário, remove opcional | OneRoster §8.2 (E13), DCAT-AP (E26), APs ELM (E23) | um "perfil" que acrescenta campos deixa de ser compatível com o núcleo |
| **Acrescentar** (extensão) | campo ou entidade nova, em namespace de quem a define | Ed-Fi (E01, E02), OneRoster `metadata` (E11), Clever `ext` (E41) | extensões não coordenadas reconstroem o problema que o padrão resolve (`iop.ros.ed-fi`) |
| **Projetar** (visão de acesso) | escolhe o que um cliente lê e escreve | Ed-Fi API Profiles (E06) | confundir projeção de privacidade com perfil de conformidade |

**O namespace é a regra de governança.** Ed-Fi diz que o namespace do descriptor indica *quem governa o valor* (E03); OneRoster e CASE marcam termo proprietário com `ext:` (E12, E17); o Ed-Fi põe a entidade estendida sob `/<namespace>/` (E02). [I] Para o VUOO, isso vira a regra: todo termo tem um IRI cujo namespace identifica a autoridade (`vuoo:core`, `vuoo:br`, `inep:`, `bncc:`), e um adaptador só cria termos no próprio namespace.

**Mapear vocabulários como dado não é teoria.** O Ed-Fi registra mapeamentos de descriptors como dado, porque os sistemas K12 mapeiam para vários contextos ao mesmo tempo (E05); o CEDS Align faz o mesmo no nível de elemento (E29); o SSSOM formaliza os metadados (justificativa, confiança, autor, data, versão das duas fontes) (E21). Isso confirma a regra já registrada em `iop.fund.mapeamento-e-proveniencia` ("declarar o mapeamento como dado... torna-o auditável").

**CASE não basta para crosswalk entre jurisdições** [I]. O vocabulário de associações do CASE 1.1 tem uma equivalência só, `exactMatchOf`, definida para ligar um item *derivado* ao item original (E18), e nenhuma correspondência aproximada ou hierárquica entre frameworks independentes. Usar `exactMatchOf` entre BNCC e Common Core afirmaria mais do que a fonte autoriza (a "perda de precisão semântica" de `iop.fund.mapeamento-e-proveniencia`). As alternativas no CASE são `isRelatedTo` com `notes` (E18, E19) ou um termo `ext:` (E17). O SKOS tem a gradação certa (E20). Uma consequência menos óbvia: **`skos:exactMatch` é transitiva** (E20), então uma cadeia BR→Core→EUA declarada com `exactMatch` gera por inferência uma equivalência BR↔EUA que ninguém revisou. O pivô deve usar `closeMatch` sempre que houver dúvida [I].

### 1.3 Que padrão de perfil de aplicação serve para adaptadores regionais?

Resposta curta [I]: **o modelo SEMIC (Core Vocabulary + Application Profile), com as regras de extensão do DCAT-AP, as regras de namespace do Ed-Fi e a disciplina restritiva do OneRoster**, descrito com W3C PROF.

| Componente do adaptador regional | Padrão de referência | Artefato |
|---|---|---|
| Ontologia: reusa o Core e acrescenta só o que é local | SEMIC AP (E25), Ed-Fi Extensions (E01) | módulo OWL `vuoo-<jur>` que importa `vuoo-core` |
| Restrições locais (obrigatoriedades, cardinalidades, formatos de código) | OneRoster profile (E13), DCAT-AP (E26), ELM (E23) | shapes SHACL `vuoo-<jur>-shapes` |
| Vocabulários locais | Ed-Fi descriptors (E03, E04), SKOS | `skos:ConceptScheme` por lista oficial (ex.: etapas do Censo), versionado |
| Mapeamento para o Core | SKOS §10 (E20) + SSSOM (E21) + Ed-Fi descriptor mapping (E05) | conjunto de mapeamentos versionado, com justificativa |
| Bindings de troca (CSV, API, XML do órgão) | ACL (E30), Ed-Fi→OneRoster como view (E08, E09) | código do adaptador, testes de ida e volta |
| Descrição do pacote | W3C PROF (E28) | `prof:Profile` com `isProfileOf vuoo-core` e recursos por papel |

**Regras de conformidade propostas** (adaptadas de E26, E13 e E01) [I]:

1. Todo dado válido num perfil regional é válido no Core: o perfil não relaxa nada que o Core exige.
2. O perfil pode tornar obrigatório o que é opcional no Core, apertar formatos e fixar vocabulários.
3. O perfil pode acrescentar classes e propriedades **somente no próprio namespace** e **não pode** acrescentar algo semelhante a um conceito do Core. Se isso acontecer, é sinal de que falta algo no Core: vira "candidato a entidade do Core" em `questoes-abertas.md`, conforme [_convencoes.md §4](../_convencoes.md).
4. Mudar o comportamento de uma operação do Core é proibido; operações novas ficam no adaptador (E10).
5. Todo perfil publica shapes, vocabulários e mapeamentos com versão, e declara contra qual versão do Core foi feito.

---

## P2. Padrões de software

### 2.1 Anti-corruption layer e portas e adaptadores

O ACL é uma fachada ou adaptador entre subsistemas que não compartilham semântica (Evans, DDD). O guia da Microsoft acrescenta três cautelas: o ACL deve concentrar **tradução, sem regra de negócio**; ele adiciona latência e um serviço a operar; e não se justifica quando não há diferença semântica (E30). Portas e adaptadores (Cockburn, E31) dão a forma: o domínio define portas, e cada tecnologia externa entra por um adaptador.

Para o VUOO [I]:

- Cada jurisdição tem **adaptadores de entrada** (Educacenso, SIS da rede, OneRoster de um parceiro) e **de saída** (relatórios para a secretaria, PEI no formato aceito), e o ACL fica dentro deles.
- O Core não importa tipos regionais. Regra verificável: o pacote `core` não depende de nenhum pacote `adapter-*`, o que um teste de arquitetura checa no CI.
- Regras locais de validação ficam nas shapes do perfil (P1.3), não no código do ACL, porque assim são dado revisável.

### 2.2 Canonical data model: benefícios e riscos

O padrão EIP justifica o modelo canônico pela contagem de tradutores (6 sistemas: 30 tradutores ponto a ponto contra 12 com o canônico), mas admite que ele parece complicado quando há poucos participantes (E32). `iop.fund.mapeamento-e-proveniencia` já compara as três estratégias (canônico, ponto a ponto, original mais derivação sob demanda).

Riscos conhecidos do canônico [I], com a mitigação observada em sistemas reais:

| Risco | Como aparece | Mitigação com precedente |
|---|---|---|
| **Superconjunto inchado** | o canônico tenta conter todos os campos de todos os países | núcleo mínimo e extensão em namespace (Ed-Fi E01; SEMIC E24) |
| **Mínimo denominador comum** | perde distinções locais, como as assimetrias da BNCC | "honestidade estrutural": modelar a fonte como ela é ([bncc-dados/02](../fora-da-fase-1/brasil/bncc-dados/02-modelo-de-dados.md)); guardar o registro original imutável (`iop.fund.mapeamento-e-proveniencia`) |
| **Gargalo de governança** | toda mudança local exige mudar o Core | perfis e vocabulários com ciclo de versão próprio (E05, E26) |
| **Equivalência falsa** | campo local "cabe" num campo do Core com sentido diferente | equivalência graduada (SKOS, E20) e tipos de equivalência de [_convencoes.md](../_convencoes.md) |
| **Canônico capturado por um padrão** | adotar OneRoster ou Ed-Fi como Core importa o viés dos EUA | ver a opção A em §6; Ed-Fi é "fortemente ancorado no contexto dos Estados Unidos" (`iop.ros.ed-fi`) |

Métrica de saúde já proposta na base: a **densidade de extensões**, ou seja, quantos dados viajam fora do modelo. Valor alto indica desalinhamento entre Core e uso real (`iop.fund.mapeamento-e-proveniencia`).

### 2.3 Vocabulários versionados como dado

Os precedentes convergem:

- Ed-Fi: descriptor = valor controlado com namespace do governante; valores locais preservados; mapeamentos como dado (E03–E05).
- Microsoft SDS: listas de valores (série, disciplina) com padrão fixo e **expansíveis pelo cliente** ("Managing List of Values") (E43).
- OneRoster e CASE: termos `ext:` (E12, E17).
- BNCC verificada: vigência por registro com `desde`/`ate` em data-version; registro nunca é apagado ([bncc-dados/02](../fora-da-fase-1/brasil/bncc-dados/02-modelo-de-dados.md)).
- Grafo: IRI estável e versão no grafo nomeado (`kg.eng.versioning-and-provenance`).

Síntese [I]: `C.VOC` = `skos:ConceptScheme` com IRI do governante, versão, vigência e licença; `C.VOC` item = `skos:Concept` com `skos:notation` igual ao código oficial; mapeamentos num conjunto à parte. Um código revogado continua resolvível.

### 2.4 Identificadores múltiplos por entidade

| Sistema | Chave primária | Ids externos | Lição |
|---|---|---|---|
| OneRoster 1.2 | `sourcedId` atribuído pela fonte, sem PII (E15) | `userIds[]` com tipo + identificador (E16) | o id de troca não é o id natural |
| Clever | Clever ID (E40) | `sis_id` escopado ao distrito; `state_id` não garantido (E40, E41) | id da fonte é atributo, não chave de vínculo |
| Ed-Fi → OneRoster | MD5 de chaves naturais (E08) | `metadata.edfi.naturalKey` (E09) | id derivado determinístico; rastreável até a fonte |
| SDS | `sourcedId` da fonte, reusado entre períodos (E43) | carimbado no objeto do Entra ID | reuso entre anos depende de a fonte manter o id |
| xAPI | IFI, exatamente um por Agent | `account{homePage,name}` | ver `iop.fund.identidade-e-contexto` |

Padrão proposto [I]: id interno opaco (UUID) por entidade, nunca exposto como id natural, mais uma coleção `C.IDN{scheme, value, issuer, validFrom, validTo, status}`, em que `scheme` é um IRI (ex.: `inep:escola`, `inep:aluno`, `br:cpf`, `oneroster:sourcedId@<emissor>`) e a unicidade vale por `(scheme, issuer, value)`, nunca por `value` sozinho. A colisão de `sis_id` entre distritos que o Clever relata (E40) é o caso que isso previne. Cuidado com o MD5 de chave natural (E08): se a chave contém CPF ou outro dado pessoal, o hash é reversível por dicionário, como acontece com `mbox_sha1sum` em `iop.fund.identidade-e-contexto`. Para pseudônimos, usar HMAC com chave sob custódia [I].

### 2.5 Temporalidade (matrícula, turma, papéis)

Fowler distingue **histórico real** (corrigível retroativamente) e **histórico de registro** (append-only, "o que sabíamos quando") (E33). O OneRoster já traz vigência em papéis (`beginDate`/`endDate`, ver papéis escolares), e o SDS segmenta o dado de turma por ano letivo, com um ano ativo por vez (E43).

Proposta [I]:

| Entidade | Tempo válido (`validFrom`/`validTo`) | Tempo de registro (`recordedAt`, append-only) | Por quê |
|---|---|---|---|
| `C.ENR` matrícula, enturmação, `C.STF` alocação, papel | sim | **sim (bitemporal)** | correções retroativas do Educacenso e da secretaria; o acesso por escopo depende de "quem era regente em tal data" |
| `C.GRP`, `C.OFR`, `C.SES` | sim | sim | turmas mudam no meio do ano |
| `C.SUP`, `C.PLN` (apoio, PEI) | sim | sim | auditoria: o que o professor via quando decidiu |
| `C.CFW`, `C.CMP` (currículo) | vigência por versão do documento (data-version) | versão do grafo | já resolvido em bncc-dados e kg.eng.versioning |
| `C.EVT` eventos | instante do evento | instante de ingestão | imutáveis (camada 3) |

### 2.6 Proveniência por campo vindo de fonte externa

Precedentes: o Ed-Fi ecoa recurso e chave natural de origem em cada registro OneRoster derivado (E09); a BNCC verificada separa "de onde extraí" de "onde conferi" ([bncc-dados/02](../fora-da-fase-1/brasil/bncc-dados/02-modelo-de-dados.md)); o PROV-O fornece o vocabulário (`kg.std.prov-o`).

Granularidade [I]:

- **Por lote de ingestão** (`prov:Activity` = execução do adaptador, com `prov:used` = arquivo ou chamada de origem com hash): é o mínimo, e barato.
- **Por registro**: `sourceSystem`, `sourceRecordId` e `ingestRun`, como o `metadata.edfi`.
- **Por campo**: só onde há fontes concorrentes para o mesmo atributo (ex.: data de nascimento vinda do Educacenso × da escola). Tabela `field_assertion(entity, attribute, value, source, run, recordedAt)` com regra explícita de precedência. No RDF, a forma natural seria o triple term do RDF 1.2, mas a especificação ainda é Candidate Recommendation (E34); até ela virar Recommendation, usar grafo nomeado por lote (`kg.found.context-and-reification`).

---

## P3. Plataformas multi-país e multi-sistema

### 3.1 Rostering normalizado

| Plataforma | Modelo interno | Entrada | Extensão | Identidade | Achado |
|---|---|---|---|---|---|
| **Clever** | próprio: distrito → escola → seção; cursos e períodos como objetos | SIS (sync) | `ext` definido pelo distrito (E41) | Clever ID primário; `sis_id` escopado (E40) | "represent district data as it exists in the SIS" e, ao mesmo tempo, normaliza códigos como raça (E39) |
| **ClassLink Roster Server** | OneRoster 1.1/1.2 certificado (E42) | OneRoster API ou CSV | Preprocessor ajusta dados do SIS e acrescenta metadados (E42) | `sourcedId` | normalização acontece *antes* da entrega, num pré-processador configurável |
| **Microsoft SDS** | SDS v2.1 CSV, de forma OneRoster (orgs, users, roles, classes, enrollments) (E44) | CSV v2.1/v1, OneRoster API (E43) | List of Values expansível (E43) | `sourcedId` da fonte, carimbado no Entra ID | formatos regionais legados (**SDS UK CSV**, Clever CSV, plugin PowerSchool) foram **absorvidos** pelo formato canônico (E43) |

[I] O padrão comum às três: um **modelo canônico próprio de forma OneRoster**, adaptadores de entrada por fonte, id da fonte guardado como atributo e vocabulários com núcleo fixo e extensão controlada. A trajetória do SDS (de formatos por país e por fornecedor para um formato canônico) é o argumento empírico mais forte a favor de Core mais adaptadores.

### 3.2 Alinhamento curricular multi-framework

| Iniciativa | Escopo | Mecanismo | Achado |
|---|---|---|---|
| **Learning Commons Knowledge Graph** | 50 estados dos EUA + DC; matemática, ELA, ciências, estudos sociais (E49) | padrões em CASE (CASE Network 2); crosswalk estado → CCSS por **Jaccard de Learning Components** compartilhados (E50) | pivô único (CCSS), direção única, métrica explícita, "does not imply ... progression"; frameworks substituídos permanecem com o id (E49) |
| **Achievement Standards Network (D2L)** | representações legíveis por máquina de objetivos de aprendizagem (E48) | importação de outcomes no Brightspace | jurisdições e licença `not_found` nas páginas abertas |
| **Khan Academy** | conteúdo alinhado à BNCC no site em português (E51) | `not_found` (mecanismo não público) | estudo independente acha alinhamento parcial (E51) |
| Kiddom, outros | — | não pesquisados (E52) | — |

[I] **Nenhuma fonte pública encontrada mapeia currículos de vários países num mesmo grafo.** O precedente operacional (Learning Commons) ensina três coisas aplicáveis:

1. **Pivô em vez de pares.** Liga-se cada framework a um pivô, e não cada par entre si (o mesmo argumento de contagem de E32).
2. **Alinhamento calculado com evidência explícita** (componentes compartilhados, contagens), e não declarado por semelhança de texto.
3. **Frameworks antigos não somem.** Isso coincide com a vigência por data-version da BNCC verificada.

Para o VUOO, o pivô não deve ser um framework nacional, nem a BNCC nem o CCSS: deve ser a **camada de conceitos do próprio grafo** (`Conceito`/knowledge component de `kg.mod.conceptual-model`), que faz o papel dos Learning Components [I].

### 3.3 Residência de dados nas plataformas

| Plataforma | Regiões | Observação |
|---|---|---|
| Microsoft SDS | todas, exceto China e Alemanha (E43) | na China, o M365 é **outra instância, de outro operador** (21Vianet), sujeita às leis locais, com recursos faltando (E45) |
| Google Workspace for Education | em repouso: EUA, Europa ou sem preferência; só nas edições Standard e Plus (E46) | **não cobre logs nem cache**; o local de processamento só existe no Enterprise Plus (E46) |
| Canvas | EUA, Canadá, UE (Irlanda, Alemanha), Austrália, Singapura (doc. 2021/22) (E47) | região na América do Sul: `not_found` |
| Brightspace | `not_found` | — |

[I] A lição para o VUOO é que "dado no Brasil" precisa cobrir também **logs, backups, cache, filas e chamadas a APIs de LLM**. Se o produto usar APIs de modelos de linguagem, elas entram na mesma regra (D5 do relatório), e o pacote de data region do Google mostra como esses itens costumam ficar de fora. O mesmo vale para SDKs de analytics e de crash no app.

---

## P4. Multi-tenancy, residência e separação de bases

### 4.1 Modelos de isolamento

O AWS SaaS Lens define **silo** (recursos dedicados por tenant, com identidade e operação compartilhadas), **pool** (recursos compartilhados) e **bridge** (misto, por serviço), e diz que o perfil regulatório do dado pode levar um serviço para silo (E53). No pool, o isolamento por linha do PostgreSQL (RLS) é o mecanismo usual, mas superusuários, papéis `BYPASSRLS` e o dono da tabela (sem `FORCE`) o ignoram (E35). Isso precisa entrar como requisito de configuração [I].

### 4.2 Proposta de unidades [I]

```
Célula jurisdicional (deploy completo, região de nuvem da jurisdição; ex.: célula BR em região no Brasil)
 └─ Tenant = rede / secretaria / mantenedora (C.ORG raiz)    ← unidade de contrato, de controlador LGPD e de isolamento
     └─ Escolas, turmas, pessoas (escopo por papel: school-roles)
Base operacional (por célula; pool com RLS por tenant ou schema por tenant)
Grafo curricular público (global, sem dado pessoal; replicável entre células)
```

| Decisão | Opção | Por quê |
|---|---|---|
| Tenant | rede/secretaria | é quem contrata e responde pelo tratamento; os papéis já são escopados por organização (papéis escolares) |
| Operacional | **bridge**: pool com RLS para redes pequenas, schema ou banco dedicado para redes grandes ou que exijam por contrato | AWS (E53) |
| Jurisdição | **célula por jurisdição**, mesmo código do Core, adaptador e perfil ativos por célula | residência; precedente de instância separada na China (E45) |
| China | célula própria, possivelmente com **operador local** e paridade de recursos reduzida | E45; PIPL art. 40 (fonte secundária, E54); a confirmar pela pasta [china/](../fora-da-fase-1/china/) |
| Grafo curricular | global e público | o grafo conceitual "quer ser publicado" (camadas) |

---

## P5. Onde fica o grafo (OWL) em relação ao modelo operacional

### 5.1 Três arranjos

| Arranjo | Como | Prós | Contras |
|---|---|---|---|
| **Virtual KG / OBDA** | ontologia + mapeamentos **R2RML** sobre o relacional; Ontop traduz SPARQL para SQL (E36–E38) | sem cópia; dado pessoal fica onde já é protegido (RLS, tenant); uma fonte de verdade | expressividade limitada a **OWL 2 QL** (E36); desempenho depende do SQL gerado; embeddings e Graph RAG precisam de material indexado |
| **Materialização (ETL)** | ingestão periódica para triplestore em grafos nomeados por lote | consultas rápidas; OWL mais rico; base para embeddings | duplicação de dado pessoal; defasagem; o apagamento LGPD precisa propagar |
| **Híbrido** | grafo curricular **nativo** em RDF (curado, versionado); dado de aluno no relacional com **R2RML**, consultado virtualmente ou materializado sob demanda por tenant | cada camada no seu regime (`kg.mod.layer-separation`, `kg.eng.storage-and-query`) | dois motores; consistência referencial por IRI |

Precedente de "canônico relacional, padrão exposto como view derivada": o Ed-Fi serve OneRoster 1.2 a partir de materialized views sobre o ODS, com proveniência embutida (E09). [I] O mesmo arranjo serve ao VUOO para exportações (OneRoster, CASE, xAPI), cada uma uma view do Core.

### 5.2 Como isso conversa com o Core agnóstico [I]

```
                vuoo-core (OWL + SKOS)  ← fonte única do modelo conceitual
                 │ gera / é mapeado para
   ┌─────────────┼──────────────────────┬──────────────────────┐
   JSON Schema   esquema relacional      R2RML (relacional→Core)  @context JSON-LD (@protected)
   (APIs)        (base operacional)      (VKG, exportações)       (troca/APIs semânticas)
                 │
   perfis regionais = vuoo-<jur> (OWL) + shapes SHACL + SKOS + mapeamentos SSSOM
                 │ validam
   dado operacional (via R2RML → RDF) e dado de troca (JSON-LD)
```

- O Core é escrito **uma vez como ontologia** e os demais artefatos são derivados e conferidos no CI, como na cadeia da BNCC verificada ([bncc-dados/01](../fora-da-fase-1/brasil/bncc-dados/01-arquitetura.md), "nenhuma camada é editada à mão").
- O relacional é **implementação** do Core, não um segundo modelo; o R2RML é o contrato entre os dois.
- As shapes SHACL do perfil regional validam o mesmo dado nos dois caminhos.
- Se o produto adotar Graph RAG, ele consulta o grafo curricular nativo e, para dado de aluno, o grafo materializado **por tenant e dentro da célula**, de modo que nada de dado pessoal sai da jurisdição para indexação.

---

## 6. Opções para o VUOO

### Opção A: adotar um padrão existente como Core (OneRoster + CASE, ou Ed-Fi)

| Prós | Contras |
|---|---|
| interoperabilidade imediata nos EUA e com fornecedores certificados | viés de jurisdição; Ed-Fi "fortemente ancorado" nos EUA (`iop.ros.ed-fi`) |
| especificação, certificação e ferramentas prontas | OneRoster só admite extensão em `metadata` (E11), e perfis não podem acrescentar (E13); não cobre D3, D6 e D7 (aprendiz, experiência, inclusão) |
| menos modelagem própria | CASE não gradua equivalência (E18); o Core ficaria refém do ciclo de versão de terceiros |

### Opção B: Core próprio mínimo + perfis de aplicação regionais + mapeamentos como dado (**proposta**)

| Prós | Contras |
|---|---|
| neutro por construção (SEMIC E24); regras de extensão com precedente (E01, E13, E26) | custo inicial de modelagem e governança |
| OneRoster, CASE, xAPI e Ed-Fi viram **views/adaptadores** (precedente E09) | exige disciplina: shapes, vocabulários e mapeamentos versionados desde o primeiro adaptador |
| deixa aberto um grafo OWL/SPARQL, se o produto o adotar | risco de canônico inchado se a regra 3 de §1.3 não for aplicada |

### Opção C: adaptadores ponto a ponto sem Core

| Prós | Contras |
|---|---|
| mais barata com 1 ou 2 integrações | custo quadrático (E32); contradiz o princípio do [briefing §2](../padroes-README.md); não reversível (`iop.fund.mapeamento-e-proveniencia`) |

### Recomendação (proposta, não decisão; vira ADR só após a revisão do coordenador)

| Tema | Proposta | Base |
|---|---|---|
| **Camadas** | (1) Core: ontologia `vuoo-core` mínima, só D1–D8 agnósticos; (2) perfis regionais `vuoo-<jur>`; (3) adaptadores de troca (ACL) por fonte e formato; (4) views de exportação por padrão (OneRoster, CASE, xAPI) | E24–E26, E30, E09 |
| **Extensão** | adicionar só no namespace da jurisdição; restringir por SHACL; proibido redefinir termo do Core (`@protected` no contexto JSON-LD); semelhante ao Core = candidato ao Core | E01, E02, E13, E22, E26 |
| **Mapeamento** | conjunto de mapeamentos como dado (SKOS + metadados SSSOM: justificativa, confiança, autor, versão de origem e destino); pivô = conceitos do Core; `exactMatch` só após revisão (é transitiva); CASE só como formato de exportação | E05, E20, E21, E50 |
| **Identificadores** | UUID interno opaco + `C.IDN{scheme IRI, issuer, value, vigência}`; unicidade por `(scheme, issuer, value)`; id da fonte é atributo; pseudônimo por HMAC, nunca hash simples de dado pessoal | E15, E16, E40, E08 |
| **Temporalidade** | bitemporal (válido + registro) para matrícula, enturmação, papel, alocação, apoio e PEI; vigência por data-version para currículo; eventos imutáveis | E33, E43, bncc-dados/02 |
| **Vocabulários** | `skos:ConceptScheme` por lista oficial, com IRI do governante, versão, vigência e licença; códigos revogados continuam resolvíveis; expansão local só no namespace do tenant ou da jurisdição | E03, E04, E43 |
| **Proveniência** | PROV por lote de ingestão sempre; por registro (`sourceSystem`, `sourceRecordId`) sempre; por campo só onde há fontes concorrentes | E09, `kg.std.prov-o`, E34 |
| **Grafo × operacional** | híbrido: grafo curricular nativo em RDF (público, versionado); dado de aluno relacional com R2RML, virtual (Ontop) para consulta e materializado por tenant para embeddings e Graph RAG; Core em OWL como fonte, relacional e JSON Schema gerados | E36–E38, `kg.mod.layer-separation` |
| **Multi-tenant e residência** | célula por jurisdição; tenant = rede/secretaria; bridge (pool com RLS + silo opcional); residência cobrindo logs, backups, telemetria e LLM | E35, E45, E46, E53 |

**Candidatos a ADR** : Core como ontologia mínima com perfis SEMIC-like; regras de extensão e namespace; mapeamentos como dado (SKOS+SSSOM); identificadores `scheme+issuer`; bitemporalidade de vínculos; célula por jurisdição e tenant por rede; grafo híbrido com R2RML.

### Riscos principais

1. **Core inchado ou com viés brasileiro.** O Brasil é o único adaptador real agora; tudo o que ele exigir tende a "subir" para o Core. Mitigação: a regra 3 de §1.3 e um teste de viabilidade do perfil EUA ou UE (em standby) antes de aceitar cada entidade nova [I].
2. **Equivalência falsa propagada por transitividade** (`exactMatch`) no pivô (E20).
3. **Residência incompleta**: logs, observabilidade, backups e APIs de LLM fora do Brasil (E46).
4. **Bypass de RLS** por papéis administrativos ou pelo dono da tabela (E35).
5. **OBDA limitado a OWL 2 QL** (E36): a ontologia do grafo, se usar construções mais ricas, não roda virtualmente; fica decidir o que é materializado.
6. **Dependência de especificações instáveis**: RDF 1.2 ainda é CR (E34); os papéis do PROF são "at risk" (E28); JSON Schema do ELM só cobre o EDC (E23).
7. **Custo de governança** dos vocabulários e mapeamentos sem dono definido; a regra "cada fato tem um dono" de [_convencoes.md §3](../_convencoes.md) precisa valer também para mapeamentos.

### Lacunas (`not_found` ou não verificado)

- Regiões de hospedagem do Brightspace; região sul-americana do Canvas (documento de 2021/22).
- Mecanismo técnico de alinhamento multi-currículo de Khan Academy e Kiddom; jurisdições e licença do ASN.
- Regras atuais (DCAT-AP 3.x) de extensão de perfis; a página consultada é da v1.1 e está arquivada (E26).
- Texto oficial do PIPL art. 40 (fonte secundária, E54), a cargo da pasta `china/`.
- Desempenho real do Ontop sobre o esquema do VUOO: precisa de prova de conceito com as competency questions de `kg.mod.conceptual-model`.
