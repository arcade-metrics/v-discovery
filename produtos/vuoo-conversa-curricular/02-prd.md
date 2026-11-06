---
produto: VUOO Elo (componente A do VUOO)
slug: vuoo-conversa-curricular
etapa: 02-prd
status: revisão 2 (completo, aguardando revisão dos [ASSUMIDO])
atualizado_em: 2026-11-05
---

# PRD: VUOO Elo, conversa sobre BNCC e legislação de inclusão

> **Escopo deste documento.** PRD do componente **A** do VUOO ([brief-ecossistema.md](brief-ecossistema.md)): o produto desejado, sem corte de MVP (o corte vem no `03-mvp.md`). Hipóteses `HIP-n` são do brief do VUOO; `HIP-A` são só deste componente.
>
> Documentos irmãos:
> - [mapeamento-da-solucao.md](mapeamento-da-solucao.md): plano de mapeamento bloco a bloco, corpus e casos âncora;
> - [arquitetura-de-conhecimento.md](arquitetura-de-conhecimento.md): grafo, lematização, tesauro e recuperação;
> - [comparacao-padrao-ouro.md](comparacao-padrao-ouro.md): bncc.dev e padrão ouro em IA curricular, jurídica e avaliação de RAG.

## Resumo em 5 linhas

1. **Para quem:** professor regente, professor do AEE e coordenação, que precisam adaptar a BNCC e cumprir a norma de educação especial.
2. **Problema:** LLM genérico inventa código da BNCC (28% a 39% das respostas, benchmark bncc.dev) e artigo de lei; a norma de inclusão mudou muito em 2025 e 2026.
3. **Produto:** uma conversa pronta e um MCP sobre uma **base curada por dispositivo, com vigência**, organizada por uma **ontologia** e um **grafo de conhecimento**.
4. **Garantia:** toda citação é conferida antes de aparecer; a qualidade é medida por golden set, inclusive no LLM do cliente.
5. **Fora:** dado de escola ou aluno, diagnóstico, parecer jurídico e telas além da conversa.

## Decisões do componente A (05/11/2026)

| # | Decisão | Efeito neste PRD |
|---|---|---|
| DA-1 | **Só conversa + MCP.** Ambiente de conversa no estilo Claude/ChatGPT e servidor MCP para o cliente de IA de quem quiser. Sem telas de busca, exportação ou painéis. | Checklists e avisos vivem na conversa. |
| DA-2 | **Vem pronto e não usa dado de escola nem de aluno.** Base carregada; o ambiente já traz um LLM operado pelo VUOO. Dado de escola é outro produto (o B). | Sem cadastro de turma ou aluno; PEI de aluno específico fora. |
| DA-3 | **Hospedagem e residência (D5) em aberto.** O MVP roda onde for mais prático. | Não bloqueia o MVP; fecha antes da venda a redes. |
| DA-4 | **Validação externa (pesquisa) depois da solução pronta.** | Golden set anotado pela equipe, com gabarito da fonte oficial. |
| DA-5 | **O conhecimento é modelado por uma ontologia própria (VUOO-A)**, alinhada a padrões abertos: gUFO (topo), ELI (legislação), SKOS (currículo, tesauro e DUA) e PROV-O (proveniência). Regras de integridade em SHACL. | RF-29 a RF-33. |
| DA-6 | **O LLM nunca consulta a base livremente.** Só chama tools; cada tool roda consultas fixas, parametrizadas e testadas. | RF-33; reduz injeção e erro de consulta. |
| DA-7 | **DUA = CAST UDL Guidelines 3.0**, modelado como esquema SKOS. Não há ontologia de DUA pronta para reusar. | RF-32. |

## Diferença em relação ao concorrente direto

O bncc.dev (Profy) resolve **a BNCC como dado para IA**. O componente A só se justifica pelo que ele não faz.

| | bncc.dev | Componente A do VUOO |
|---|---|---|
| BNCC | dataset verificado | extração própria da fonte oficial do MEC |
| Legislação de educação especial | não | **núcleo**: por dispositivo, com vigência, federal + módulo estadual |
| Modelo de conhecimento | JSON plano, sem relações entre documentos | ontologia + grafo (regulamenta, altera, revoga, conflita) |
| Busca | radical por regras + BM25 | lematização, tesauro do professor, busca híbrida |
| Ligação BNCC ↔ inclusão ↔ DUA | não | camada de interpretação rotulada |
| Para o professor | instruções para colar no ChatGPT | conversa pronta (DA-1, DA-2) |
| Teste de alucinação | benchmark público genérico | relatório no LLM **do cliente**, BNCC e legislação |

## Jobs to be done

| # | Job | Hipótese |
|---|-----|----------|
| JOB-1 | Quando preciso planejar para um aluno com deficiência numa turma regular, quero saber que habilidades da BNCC trabalhar e que adaptações a norma permite e pede, para não começar do zero. | HIP-3 |
| JOB-2 | Quando preciso escrever ou revisar o PEI ou o PAEE, quero saber o que a norma vigente exige (conteúdo mínimo, participantes, prazos, revisão), para entregar um documento aceito. | HIP-3 |
| JOB-3 | Quando família, direção ou secretaria discute um direito (profissional de apoio, laudo, sala de recursos), quero o texto exato e vigente, com artigo e data, para sustentar a conversa. | HIP-3 |
| JOB-4 | Quando a rede conecta a IA que já usa, quer que ela pare de inventar código da BNCC e artigo de lei, para liberá-la aos professores sem risco. | HIP-4 |
| JOB-5 | Quando a secretaria escolhe ou renova um LLM, quer saber quanto cada opção erra, com e sem a base, para decidir com número. | HIP-4 |
| JOB-6 | Quando sai norma nova ou alteração, quero saber o que muda na minha prática, para não seguir regra revogada. | HIP-A1 |
| JOB-7 | Quando uso um termo do dia a dia ("aluno de inclusão", "laudo", "cuidador"), quero ser entendido e aprender o termo correto da norma, sem ser corrigido de forma constrangedora. | HIP-A3 |

| # | Hipótese nova | Como saberíamos que é falsa | Confiança |
|---|---|---|---|
| HIP-A1 | O professor valoriza saber **qual norma vale hoje e o que mudou**, não só o texto. | Avisos de mudança ignorados (abertura < 20%) e histórico de vigência nunca consultado. `[ASSUMIDO]` limiar | média |
| HIP-A2 | Legislação de inclusão é a pergunta mais frequente, e é ela que diferencia o A do bncc.dev. | Em uso real, > 80% das perguntas são só de BNCC. `[ASSUMIDO]` limiar | média |
| HIP-A3 | Entender o vocabulário do professor (tesauro + lematização) melhora a resposta de forma perceptível. | No golden set de busca, o ganho do tesauro sobre BM25 puro fica abaixo de 5 pontos de recall@10. `[ASSUMIDO]` limiar | média |

## Personas

- **Marta, professora regente do 4º ano** `[ASSUMIDO]`. Escola municipal, 30 alunos, dois com TEA e um com DI. Planeja à noite, no celular ou notebook. Conhece a BNCC pelo código, não lê decreto. Quer resposta curta, com o que fazer amanhã.
- **Rogério, professor do AEE** `[ASSUMIDO]`. Sala de recursos, escreve PAEE e PEI. Lê norma e precisa citá-la. Desconfia de IA. Valor = fonte exata e vigência.
- **Cláudia, coordenadora pedagógica** `[ASSUMIDO]`. Responde à secretaria e às famílias. Quer segurança jurídica e material para formação.
- **TI da rede (integrador).** Conecta o MCP no LLM da rede. Quer instalação simples, logs, privacidade e um número de qualidade.
- **Curadoria VUOO (interna).** Mantém a base: registra normas e alterações, revisa a camada de interpretação e o tesauro, aprova releases.

## Fluxos principais

### Fluxo 1: pergunta curricular e de inclusão (JOB-1, JOB-3, JOB-7)

1. A professora entra no ambiente de conversa com login da rede ou conta individual.
2. Pergunta: "Tenho um aluno com TEA no 4º ano que ainda não lê. Que habilidades de Língua Portuguesa priorizo e que adaptações posso fazer?"
3. Se a mensagem tiver dado pessoal de aluno, o sistema avisa e propõe a versão anonimizada **antes** de enviar ao LLM (RF-17).
4. O pipeline de linguagem reconhece entidades (4º ano, LP, TEA) e normaliza termos pelo tesauro (RF-30, RF-31).
5. O LLM chama as tools: habilidades por ano e componente, dispositivos sobre acessibilidade curricular, diretrizes DUA ligadas.
6. A resposta vem em três blocos:
   - **o que a norma diz**: texto oficial, citado por código ou dispositivo;
   - **orientação pedagógica**: interpretação, rotulada como tal;
   - **fontes**: links para dispositivo e habilidade, com data de vigência.
7. O verificador confere cada código e dispositivo citado (RF-10). O que não confere é marcado ou removido.
8. A professora abre uma fonte e vê o texto oficial com página ou dispositivo.
9. Ela segue a conversa ("e para matemática?"): o contexto ativo (4º ano, TEA) continua valendo e aparece na tela (RF-34).
10. Ela avalia a resposta e pode reportar erro (RF-20).

**Momento de valor:** na mesma resposta, as habilidades certas do 4º ano com códigos conferidos **e** o artigo que autoriza a adaptar, sem abrir PDF.

**Caminhos de erro:**
- **Sem evidência na base:** diz isso, mostra o que buscou e sugere reformular. Não completa com a memória do LLM sem rótulo.
- **Pergunta diagnóstica** ("ele parece ter TDAH?"): recusa explicada e redirecionamento pedagógico (RF-18).
- **O LLM ignora as tools:** o verificador marca as citações; o fato entra na telemetria daquele LLM.
- **LLM principal fora do ar:** a conversa segue no LLM de reserva, com aviso (RNF-04).
- **Conflito entre normas** (ex.: Res. SEDUC-SP 129/2025 × Port. MEC 421/2026 sobre laudo; Q-INC-07): mostra os dois dispositivos, diz que há conflito e **não** decide qual prevalece.
- **Termo inadequado** ("portador de deficiência"): entende a pergunta e usa o termo correto na resposta, com nota curta e neutra (RF-30).

### Fluxo 2: "o que a norma exige para o PEI?" (JOB-2)

1. O professor do AEE pergunta: "O que o PEI precisa ter na rede estadual de SP?"
2. O sistema usa a jurisdição do tenant ou pergunta (RF-19).
3. A resposta traz o mínimo federal (Port. MEC 421/2026, art. 11, I a IV; revisão anual, art. 7, §3) e, separado, o que a norma estadual acrescenta (Res. SEDUC-SP 129/2025), com o prazo de adequação.
4. Mostra um **checklist** na conversa, cada item ligado ao dispositivo (RF-21).

**Momento de valor:** checklist ligado ao dispositivo, pronto para conferir o PEI que ele já tem.

**Caminho de erro:** rede sem norma estadual na base → "só a norma federal está coberta para a sua rede"; nunca extrapola de outro estado.

### Fluxo 3: integração do MCP pela rede (JOB-4)

1. A TI recebe a URL do MCP e as credenciais do tenant (OAuth).
2. Conecta no cliente de IA (ChatGPT, Claude, Gemini, Copilot, agente próprio).
3. Roda o **teste de conexão** (RF-24): "tools chamadas: sim/não; citações conferidas: x/y".
4. Libera para os professores.

**Momento de valor:** no LLM da própria rede, a queda de citações inventadas com a base ligada.

**Caminhos de erro:** cliente sem MCP → usa o ambiente de conversa do VUOO. LLM que não chama tools → o relatório diz isso e recomenda configuração.

### Fluxo 4: (removido pela DA-1)

Sem busca direta. "EF04LP05" ou "LBI art. 28" são respondidos pela conversa, que chama o lookup.

### Fluxo 5: relatório de alucinação do LLM da rede (JOB-5)

1. A secretaria escolhe um ou mais LLMs.
2. O VUOO roda o golden set em duas condições: sem base e com MCP (RF-23).
3. Entrega relatório com invenção, misgrounding, recusa correta e excessiva, precisão de citação, custo e intervalo de confiança.

**Momento de valor:** um número dela, no LLM dela.

**Caminho de erro:** LLM rejeita temperatura 0 ou falha chamadas → registrado por resposta e reportado.

### Fluxo 6: aviso de mudança normativa (JOB-6)

1. Sai no DOU um ato que altera um dispositivo da base (ex.: Port. MEC 550/2026 alterou o art. 29 da 421).
2. O monitor abre item de triagem (RF-26); a curadoria registra a nova versão (Fluxo 7).
3. Quem consultou aquele dispositivo nos últimos 90 dias vê, no início da próxima conversa, o aviso com o antes e o depois (RF-27).
4. Respostas antigas no histórico ganham a marca "baseada em versão anterior da norma".

**Momento de valor:** o professor descobre a mudança pelo VUOO antes de descobrir pela secretaria.

### Fluxo 7: curadoria e release da base (persona Curadoria)

1. Entra um item de triagem: monitor, reporte de usuário ou revisão planejada.
2. O curador registra a mudança: nova norma, nova versão de dispositivo, correção, termo do tesauro ou interpretação.
3. Um segundo curador revisa toda mudança normativa e de interpretação (quatro olhos, RF-36).
4. O pipeline gera a nova data-version: valida SHACL (RF-29), roda o golden set (RF-25) e compara com a versão anterior.
5. Se passar, publica com changelog (RF-28) e registro de transparência atualizado (RNF-11). Se falhar, a release é bloqueada e o motivo aparece.

**Momento de valor:** uma alteração publicada no DOU vira base atualizada e testada em até 7 dias.

## Primeira sessão e estado vazio

- **Tela inicial não fica em branco:** 6 perguntas de exemplo ligadas aos jobs ("o que o PEI precisa ter?", "laudo é obrigatório para o AEE?", "habilidades de MT do 2º ano para um aluno com DI", "o que mudou com o Decreto 12.686?" etc.).
- **Uma linha de cobertura:** o que a base cobre, o que não cobre e a data-version (RF-37).
- **Nada a configurar:** sem cadastro de turma ou aluno (DA-2). Conectar LLM próprio é opcional.
- **Rede sem módulo estadual:** aviso logo no início ("sua rede: SP estadual; normas estaduais cobertas: …" ou "só federal").
- **Primeira resposta:** o bloco "fontes" vem aberto na primeira vez, para mostrar que tudo é conferível.

## Requisitos funcionais

### Base curada (dado)

| # | Requisito | Job | Hipótese | Prioridade |
|---|-----------|-----|----------|------------|
| RF-01 | A base contém a BNCC (edição 2018, todas as etapas) e o complemento de Computação, extraídos por pipeline próprio da fonte oficial do MEC; cada registro é conferido contra o PDF homologado e guarda a página de origem. | JOB-1 | HIP-3, HIP-4 | alta |
| RF-02 | A base contém o corpus normativo de inclusão de [mapeamento-da-solucao.md §3](mapeamento-da-solucao.md#3-corpus-normativo), modelado **por dispositivo** (artigo, parágrafo, inciso, alínea), com identificador estável no padrão URN LEX (RFC 9676) quando houver. | JOB-2, JOB-3 | HIP-3 | alta |
| RF-03 | Todo dispositivo tem vigência (desde, até, ato que incluiu, alterou ou revogou). Uma consulta com data devolve o texto **vigente naquela data**. | JOB-3, JOB-6 | HIP-A1 | alta |
| RF-04 | Todo registro tem proveniência (PROV-O): fonte, localizador, URL oficial, data de obtenção e hash do arquivo-fonte arquivado. | JOB-3, JOB-4 | HIP-4 | alta |
| RF-05 | Relações entre normas são dado: `regulamenta`, `altera`, `revoga`, `cita`, `conflita_com` (esta com nota e sem decidir qual prevalece). | JOB-3, JOB-6 | HIP-3 | alta |
| RF-06 | A **camada de interpretação** (orientações, ligação habilidade ↔ adaptação ↔ DUA, perguntas frequentes) fica separada do texto normativo, sempre rotulada, com autor e data de revisão. | JOB-1 | HIP-3 | alta |
| RF-07 | Normas estaduais e de rede entram como **módulo por jurisdição**, ativado pelo tenant, sem alterar a resposta de quem não o ativou (D6). | JOB-2 | HIP-3 | média |

### Ontologia, grafo e linguagem (DA-5, DA-6, DA-7)

| # | Requisito | Job | Hipótese | Prioridade |
|---|-----------|-----|----------|------------|
| RF-29 | Existe uma ontologia VUOO-A versionada (OWL em Turtle), alinhada a gUFO, ELI, SKOS e PROV-O. Todo dado da base é validado contra regras SHACL (ex.: todo dispositivo tem vigência e fonte; não há versões vigentes sobrepostas; toda interpretação tem autor). Uma violação bloqueia a release. | JOB-3, JOB-4 | HIP-4 | alta |
| RF-30 | Existe um **tesauro SKOS** do domínio: termo da norma (`prefLabel`), termos do professor e siglas (`altLabel`) e termos inadequados (`hiddenLabel`, ex.: "portador de deficiência"). A conversa entende todos e responde com o termo da norma. | JOB-7 | HIP-A3 | alta |
| RF-31 | O processamento de pt-BR usa lematização com modelo fixado por versão, dicionário de siglas (AEE, PEI, PAEE, SRM, TEA, AH/SD, Libras), termos compostos e reconhecimento por regra de códigos BNCC, citações de norma (→ URN), etapa, ano e público. | JOB-1, JOB-7 | HIP-A3 | alta |
| RF-32 | A camada DUA representa as **CAST UDL Guidelines 3.0** (princípios, diretrizes, considerações) como esquema SKOS. Ligações entre DUA, habilidade e público ficam só na camada de interpretação (RF-06). | JOB-1 | HIP-3 | média |
| RF-33 | O grafo é consultado só por tools com consultas fixas, parametrizadas e cobertas por teste. O LLM nunca escreve SPARQL nem SQL (DA-6). | JOB-4 | HIP-4 | alta |

### MCP e consulta

| # | Requisito | Job | Hipótese | Prioridade |
|---|-----------|-----|----------|------------|
| RF-08 | O MCP expõe poucas tools (meta: até 9), cada uma com descrição escrita como produto: o que faz, quando usar, como ler a saída, regra anti-invenção, vocabulário válido. Conjunto inicial em [mapeamento-da-solucao.md §4.6](mapeamento-da-solucao.md#46-mcp-tools-propostas). | JOB-4 | HIP-4 | alta |
| RF-09 | Código ou dispositivo inexistente recebe explicação e sugestão ("EF04LP99 não existe; o 4º ano de LP vai até EF04LP27"). Nunca `null` nem resultado vazio sem texto. | JOB-4 | HIP-4 | alta |
| RF-10 | A tool `verificar_citacoes` recebe um texto e diz, para cada código e dispositivo citado, se existe, se o texto confere e se está vigente. O ambiente de conversa a roda em **toda** resposta antes de exibir. | JOB-4 | HIP-4 | alta |
| RF-11 | Listagens devolvem `{total, exibindo, resultados}` com limite padrão. | JOB-4 | HIP-4 | média |
| RF-12 | Toda resposta do MCP declara a data-version da base. | JOB-4, JOB-6 | HIP-4 | alta |
| RF-13 | A busca é híbrida: lookup exato → BM25 sobre lemas → vetorial por dispositivo e habilidade → fusão → expansão no grafo filtrada pela data → reordenação. A busca semântica nunca substitui o lookup verificado. Um golden set de busca mede cada etapa. | JOB-1, JOB-3 | HIP-3, HIP-A3 | alta |
| RF-14 | (Removido pela DA-1: sem API REST pública.) | — | — | — |

### Ambiente de conversa

| # | Requisito | Job | Hipótese | Prioridade |
|---|-----------|-----|----------|------------|
| RF-15 | O ambiente funciona pronto, com LLM operado pelo VUOO e trocável por configuração sem mudar a base (DA-2). | JOB-1, JOB-4 | HIP-3 | alta |
| RF-16 | Toda resposta segue os três blocos (norma, orientação rotulada, fontes com vigência). Resposta sem citação verificada leva o aviso "sem fonte na base". | JOB-1, JOB-3 | HIP-3, HIP-4 | alta |
| RF-17 | Dado pessoal identificável de aluno (nome com condição, CPF, nascimento, matrícula) é detectado **antes** do envio ao LLM; o sistema oferece trocar por marcador e bloqueia o envio até a pessoa confirmar. | JOB-1 | HIP-3 | alta |
| RF-18 | Pergunta diagnóstica ou clínica recebe recusa explicada e redirecionamento pedagógico. | JOB-1 | HIP-4 | alta |
| RF-19 | Quando a jurisdição muda a resposta, o sistema usa a do tenant ou pergunta; nunca responde com norma de outro estado como se fosse a do usuário. | JOB-2 | HIP-3 | alta |
| RF-20 | O usuário avalia cada resposta (útil / não útil / errada) e reporta erro de dado, que vira item de curadoria separado de bug. | JOB-3 | HIP-3 | média |
| RF-21 | Checklist de conteúdo mínimo do PEI e do PAEE, por jurisdição, na conversa, com cada item ligado ao dispositivo. Sem exportação (DA-1). | JOB-2 | HIP-3 | média |
| RF-34 | A conversa é multi-turno e mantém um **contexto ativo** (etapa, ano, componente, público, jurisdição, data de referência), visível e editável pelo usuário. | JOB-1 | HIP-3 | alta |
| RF-35 | Cada resposta pode mostrar "como cheguei aqui": tools chamadas, dispositivos e habilidades consultados e resultado da verificação. | JOB-3, JOB-4 | HIP-4 | média |
| RF-37 | Uma tool `base_sobre` informa cobertura, lacunas conhecidas e data-version; a conversa usa isso para dizer o que não sabe. | JOB-4 | HIP-4 | média |
| RF-38 | Perguntas com data ("o que valia em 2024?") consultam a base naquela data (RF-03) e dizem qual versão foi usada. | JOB-3, JOB-6 | HIP-A1 | média |

### Avaliação e qualidade

| # | Requisito | Job | Hipótese | Prioridade |
|---|-----------|-----|----------|------------|
| RF-22 | **Golden set** versionado, de BNCC e legislação, em pelo menos 8 tarefas: transcrição, existência, geração com citação, lookup reverso, vigência em data, hierarquia e conflito, pergunta sem resposta na base e recusa (diagnóstico, dado pessoal). Gabarito tirado da fonte oficial pela equipe (DA-4). Inclui os casos âncora C1 a C15 do mapeamento. | JOB-4, JOB-5 | HIP-4 | alta |
| RF-23 | A bateria roda em qualquer LLM, "sem base" e "com MCP", e reporta: invenção; *misgrounding* (citação real que não sustenta a afirmação); suporte parcial; precisão e cobertura de citação por afirmação (ALCE); recusa correta e excessiva; chamadas falhas; IC 95% por taxa. | JOB-5 | HIP-4 | alta |
| RF-24 | O teste de conexão (10 a 20 itens) roda na configuração do tenant em menos de 5 minutos. | JOB-4 | HIP-4 | média |
| RF-25 | Nenhuma data-version, mudança de prompt ou troca de modelo vai a produção se o golden set regredir na precisão de citação ou na recusa correta, medido com LLM de referência fixo. | JOB-4 | HIP-4 | alta |

### Mudança normativa e curadoria

| # | Requisito | Job | Hipótese | Prioridade |
|---|-----------|-----|----------|------------|
| RF-26 | Um monitor diário do DOU e do MEC Normas detecta atos que citam normas da base e abre item de triagem. Publicar a alteração é ato humano. | JOB-6 | HIP-A1 | média |
| RF-27 | Quando um dispositivo muda, quem o consultou nos últimos 90 dias `[ASSUMIDO]` recebe aviso com o antes e o depois; respostas antigas ganham a marca "baseada em versão anterior". | JOB-6 | HIP-A1 | média |
| RF-28 | Changelog público por data-version, nas categorias normativa, correção, interpretação, tesauro e schema. | JOB-6 | HIP-A1 | baixa |
| RF-36 | Toda mudança normativa ou de interpretação passa por um segundo curador antes de entrar na release; autor, revisor e data ficam registrados (PROV-O). | JOB-3 | HIP-4 | alta |

## Requisitos não funcionais

| # | Área | Requisito |
|---|------|-----------|
| RNF-01 | Privacidade | O A **não recebe nem armazena dado de aluno** por desenho. O histórico é do professor e fica no tenant, com retenção padrão de 90 dias `[ASSUMIDO]`. Conversas não treinam modelo nenhum. |
| RNF-02 | Privacidade / LLM | No ambiente do VUOO, o LLM é contratado com cláusula de não-treino e retenção mínima; provedor e região ficam documentados para a LGPD (a região fecha com a D5, DA-3). Pelo MCP, o LLM é do cliente e o VUOO só recebe as chamadas de tool. |
| RNF-03 | Desempenho | Lookup em até 300 ms e busca em até 800 ms (p95) no MCP remoto, sem contar o LLM. Primeira palavra da resposta na conversa em até 3 s (p50) `[ASSUMIDO]`. |
| RNF-04 | Disponibilidade | LLM de reserva configurado; se o principal cair, a conversa segue e avisa. Rate limit por tenant no MCP, com 429 explicativo. |
| RNF-05 | Reprodutibilidade | Base gerada por pipeline determinístico, sem LLM na extração. A mesma fonte gera os mesmos bytes; o CI reprova qualquer diferença. |
| RNF-06 | Rastreabilidade | Cada resposta guarda data-version, versão do prompt e do modelo, tools chamadas, citações e resultado da verificação. |
| RNF-07 | Acessibilidade | WCAG 2.2 AA e eMAG: teclado, leitor de tela, ajuste de fonte, linguagem simples opcional. |
| RNF-08 | Licença | BNCC e normas são domínio público (Lei 9.610/98, art. 8º, IV). Licença do CAST UDL 3.0 `[A CONFIRMAR]` antes de publicar a camada DUA. Licença da curadoria VUOO em aberto. |
| RNF-09 | Segurança | MCP com OAuth 2.1 por tenant, sem acesso a outro dado do VUOO. Defesas contra prompt injection vinda das fontes e contra tool poisoning (OWASP LLM Top 10 2025: LLM01, LLM08, LLM09; OWASP MCP Top 10). |
| RNF-10 | Idioma | pt-BR em tudo: tools, descrições, erros e documentação. |
| RNF-11 | Governança de IA | Transparência ao usuário: o que é IA, qual modelo, qual base e data, e que não substitui orientação jurídica nem da secretaria. Registro de transparência público por data-version, no modelo do Aila (Oak). |
| RNF-12 | Padrões abertos | A base é exportável em RDF (Turtle) e SKOS; o LLM é trocável (RF-15). Nenhuma peça central depende de um fornecedor único. |
| RNF-13 | Custo | Custo de LLM e de infraestrutura por conversa é medido e exposto num painel interno; teto por conversa `[A CONFIRMAR]`. |
| RNF-14 | Observabilidade | Trace por resposta (pergunta → tools → verificação → resposta), sem dado pessoal, para depurar erro de qualidade. |

## Decisões técnicas recomendadas (boas práticas)

> Recomendações que viram ADR no `04-plano.md`. Ficam aqui porque foram pedidas junto com o PRD. Detalhes em [arquitetura-de-conhecimento.md](arquitetura-de-conhecimento.md).

| Camada | Recomendação | Por quê |
|---|---|---|
| Ontologia | OWL + SKOS + ELI + PROV-O em Turtle, editada no Protégé, versionada no git | Padrões W3C e UE estáveis; diffs legíveis |
| Ontologia de topo | gUFO + UFO-L (direitos e deveres) | Modela papéis, vigência e relações jurídicas; é leve |
| Regras | SHACL, validado com pySHACL no CI | Padrão W3C para integridade de grafo |
| Pipeline de dados | Python + rdflib + spaCy (`pt_core_news_lg`, versão fixada) | Ecossistema mais maduro para PDF, NLP e RDF |
| Grafo | Oxigraph (SPARQL 1.1) | Leve e embutível; serve a milhares de nós quase imutáveis |
| Busca | Postgres + BM25 (ParadeDB) + pgvector com BGE-M3; reordenação com bge-reranker-v2-m3 | Multilíngue, open source, um banco para texto e vetor |
| Núcleo + MCP | TypeScript + MCP SDK oficial, consultas SPARQL fixas, OAuth 2.1 | SDK de referência; cumpre a DA-6 |
| Conversa | Next.js + LLM trocável (provedor principal + reserva) | DA-1, RF-15, RNF-04 |
| Avaliação | Python + promptfoo, golden set versionado | RF-22 a RF-25 |
| CI e infra | GitHub Actions + Docker | Release bloqueada por falha no SHACL ou no golden set |

Isso revê a §6 da [arquitetura-de-conhecimento.md](arquitetura-de-conhecimento.md): o grafo vai para o Oxigraph e a busca fica no Postgres.

## Métricas de sucesso

| Métrica | Fonte | Baseline | Meta | Horizonte |
|---------|-------|----------|------|-----------|
| Citações inventadas **exibidas** sem marca | verificador (RF-10) | `[A CONFIRMAR]` medir sem base | 0% | desde o piloto |
| Invenção no golden set com MCP, por LLM | RF-23 | sem base: 28,3% na BNCC (bncc.dev); legislação `[A CONFIRMAR]` | ≤ 2% | piloto |
| Precisão de citação (a fonte sustenta a afirmação) | RF-23, juiz validado por humano | `[A CONFIRMAR]` | ≥ 90% | 6 meses |
| Recusa correta (sem resposta, diagnóstico) | golden set | `[A CONFIRMAR]` | ≥ 95% | piloto |
| Recall@10 da busca com tesauro × BM25 puro (HIP-A3) | golden set de busca | BM25 puro | +5 pontos | antes do piloto |
| Violações SHACL na release | CI | — | 0 | sempre |
| Professores que voltam ≥ 1×/semana na semana 4 (HIP-3) | telemetria | `[A CONFIRMAR]` | ≥ 40% `[ASSUMIDO]` | 8 semanas de piloto |
| Respostas "útil" entre as avaliadas | RF-20 | — | ≥ 70% `[ASSUMIDO]` | piloto |
| Perguntas com legislação de inclusão (HIP-A2) | classificação das perguntas | — | ≥ 30% `[ASSUMIDO]` | piloto |
| Tempo do DOU até a base atualizada | changelog × DOU | — | ≤ 7 dias | 6 meses |

**Contra-indicadores:**
- **Recusa excessiva:** "não encontrei" em perguntas com gabarito na base. Zerar a alucinação recusando tudo é a forma errada de bater a meta.
- **Dado de aluno nas conversas:** quanto o RF-17 dispara. Se subir, o A está sendo usado como o B sem as proteções do B.
- **Interpretação sem revisão:** itens da camada de interpretação com revisão vencida. Se subir, a curadoria não acompanha o produto.

## Fora de escopo nesta visão

- **Parecer jurídico.** O A informa a norma; não decide caso concreto nem conflito.
- **Diagnóstico ou triagem clínica**, e leitura de laudo (D4).
- **Dado de escola, turma ou aluno**, inclusive o PEI preenchido de um aluno (DA-2).
- **Telas além da conversa** (DA-1).
- **Jurisdições fora do Brasil** (D20).

## Além da v1

- Currículos estaduais e municipais como módulos (Currículo Paulista primeiro, D6).
- Jurisprudência selecionada (STF ADI 6590, ADI 5357) como camada rotulada.
- Base de legislação de inclusão como dado aberto, se a estratégia comercial permitir.
- Benchmark público de alucinação em legislação educacional brasileira.
- Respostas em Libras (vídeo) e em linguagem simples certificada.

## Glossário

| Termo | Significado |
|---|---|
| Dispositivo | Unidade citável de uma norma: artigo, parágrafo, inciso, alínea. |
| Vigência / point-in-time | Texto válido numa data específica. |
| URN LEX (RFC 9676) | Identificador padrão de normas brasileiras, ex.: `urn:lex:br:federal:lei:2015-07-06;13146`. |
| ELI | European Legislation Identifier: vocabulário para obra, versão e dispositivo de norma. |
| SKOS | Padrão W3C para tesauros e esquemas de conceitos. |
| PROV-O | Padrão W3C de proveniência (quem, quando, a partir de quê). |
| gUFO / UFO-L | Ontologia de topo leve e sua extensão para relações jurídicas. |
| SHACL | Padrão W3C de regras de validação de grafo. |
| SPARQL | Linguagem de consulta de grafos RDF. |
| Misgrounding | Citação real que não sustenta o que foi afirmado. |
| Golden set | Conjunto de perguntas com gabarito, usado para medir qualidade. |
| DUA | Desenho Universal para a Aprendizagem (CAST UDL 3.0). |

## Suposições a validar

- `[ASSUMIDO]` Personas Marta, Rogério e Cláudia: confirmar com 3 a 5 entrevistas.
- `[ASSUMIDO]` Limiares: 40% de retorno semanal, 70% "útil", 30% de perguntas de inclusão, +5 pontos de recall, 90 dias de aviso e de retenção, 3 s até a primeira palavra.
- `[ASSUMIDO]` BNCC inteira (EI, EF, EM) na base, e não só EF + EM.
- `[ASSUMIDO]` Login por conta da rede ou individual.
- `[A CONFIRMAR]` Corpus estadual da v1: só SP ou mais estados.
- `[A CONFIRMAR]` Quem faz a curadoria interna (dois curadores, para o RF-36) até a pesquisa (DA-4).
- `[A CONFIRMAR]` Licença do CAST UDL 3.0 para uso comercial.
- `[A CONFIRMAR]` Teto de custo por conversa (RNF-13).
- `[A CONFIRMAR]` Se o A é vendido separado do C (HIP-6).
- `[A CONFIRMAR]` Atualizar o brief do VUOO: com a DA-2, o A deixa de ser "LLM só do cliente".
