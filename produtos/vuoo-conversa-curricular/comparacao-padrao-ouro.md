---
produto: VUOO · Componente A (conversa curricular)
slug: vuoo-conversa-curricular
etapa: contexto
status: rascunho
atualizado_em: 2026-11-05
---

# Comparação com o padrão ouro (componente A)

> **Fontes.** bncc.dev: <https://bncc.dev/>, <https://bncc.dev/benchmark/> (v0.3.0, medida em 18/09/2026) e <https://bncc.dev/benchmark/estudo-mcp/>, consultados em 05/11/2026, mais a análise dos dois repositórios em [../../PRD/padroes/brasil/bncc-dados/](../vuoo-microjogos/base/fora-da-fase-1/brasil/bncc-dados/README.md) e [bncc-pacotes/](../vuoo-microjogos/base/fora-da-fase-1/brasil/bncc-pacotes/README.md). As demais referências vêm de pesquisa web em 05/11/2026.
>
> **Marcas:**
> - **[V]**: conferido em fonte primária ou abstract.
> - **[S]**: só em fonte secundária.
> - **[NV]**: não verificado.
> - **[I]**: interpretação nossa.

## 1. Quem é referência em quê

| Referência | Tipo | Por que importa para o A |
|---|---|---|
| **bncc.dev** (Profy, BR) | dataset BNCC + pacotes + MCP + benchmark | concorrente direto na metade curricular |
| **Oak National Academy: Aila + Oak MCP** (UK, agência pública) | assistente de planejamento + MCP do currículo nacional | o mais próximo do nosso desenho: **MCP de conteúdo oficial para o LLM que o professor já usa**. Tem guardrails em 4 camadas e moderação independente [V] |
| **Learning Commons Knowledge Graph + Evaluators** (ex-CZI, EUA) | grafo de standards dos 50 estados (via CASE) + MCP + juízes LLM abertos | identificador estável entre tools; avaliadores publicados separados do gerador [V] |
| **1EdTech CASE / CASE Network 2** | padrão de intercâmbio de standards | GUID por item, associações tipadas para crosswalk e progressão [V] |
| **Stanford RegLab: "Hallucination-Free?"** (JELS 2025) | avaliação de IA jurídica comercial (Lexis+ AI, Westlaw) | o método de referência para medir alucinação **em lei**, com "misgrounding" e "mudança de lei" [V] |
| **LexML / URN LEX (RFC 9676, 2025)** | identificador de norma brasileira | identificador de dispositivo **com versão temporal** [V] |
| **normas.leg.br / Dados Abertos do Senado** | legislação federal compilada, por artigo, com histórico | possível fonte de extração com histórico de alterações [S] |
| **Jus IA (Jusbrasil)** | IA jurídica brasileira | camada de verificação de citações contra a base [S] |
| **ALCE, FActScore, TREC RAG 2024, ARES, LegalBench-RAG** | métodos de avaliação de RAG e citação | métricas por afirmação; suporte parcial; juiz calibrado; recuperação avaliada à parte [V] |
| **UK DfE "Generative AI: product safety standards"** (2026) | 13 padrões para produtos de IA em educação | checklist de governança; não trata de acurácia [V] |
| **OWASP LLM Top 10 2025 e MCP Top 10 (beta)** | segurança | prompt injection, poisoning de RAG, tool poisoning [S] |

Khanmigo e MagicSchool **não publicam métricas de alucinação** [S]. Publicar as nossas é um diferencial possível [I].

## 2. Números que dão a escala do problema

| Fonte | Condição | Resultado |
|---|---|---|
| bncc.dev v0.3.0 | 19 modelos, de memória, 17.100 respostas | 39% das transcrições com texto inventado ou trocado; 26% dos códigos reais negados [V] |
| bncc.dev, estudo MCP | 6 modelos, sem × com MCP | 28,3% de invenção → 0,0% (2.557 respostas). **O estudo é do próprio fornecedor, e o gabarito é o mesmo dataset da fonte** [V] |
| Stanford, IA jurídica comercial | 202 consultas pré-registradas | Lexis+ AI alucina cerca de 17%, Westlaw cerca de 33%, mesmo com RAG e citação [V] |
| ALCE | geração com citação | mesmo o melhor modelo deixa 50% das saídas sem suporte completo (ELI5) [V] |

**Leitura [I]:** na BNCC, o problema está medido e uma solução está demonstrada. Um lookup verificado zera a invenção de **código**. Em lei, ferramentas comerciais com RAG ainda alucinam de 17% a 33%. O erro dominante não é inventar a norma: é **citar uma fonte real que não sustenta a afirmação**, ou aplicar uma norma revogada. Ninguém mediu isso para a legislação educacional brasileira. É aí que o A tem espaço.

## 3. Placar por mecanismo

Os 15 mecanismos que a pesquisa identificou como padrão ouro, cruzados com o que cada referência faz e com o que o A propõe.

Legenda: ● faz · ◐ faz em parte · ○ não faz · — não se aplica.

| # | Mecanismo | bncc.dev | Oak | Learning Commons | IA jurídica (Lexis/Jus IA) | **A (proposta)** | Onde no PRD |
|---|---|---|---|---|---|---|---|
| 1 | Identificador canônico estável por unidade citável | ● código BNCC | ◐ id de aula | ● CASE UUID | ● | ● código BNCC + URN LEX | RF-01, RF-02 |
| 2 | Citação no nível do dispositivo, resolvível ao texto oficial | ● (habilidade + página) | ◐ link da aula | ● | ◐ | ● artigo, parágrafo, inciso, alínea | RF-02, RF-04 |
| 3 | Vigência temporal / point-in-time | ◐ vigência por registro, sem consulta por data | ○ | ○ | ◐ [NV] | ● consulta "vigente em data" | RF-03 |
| 4 | Grafo de alteração e revogação consultável | ○ (só um documento) | ○ | ◐ progressões | ◐ | ● inclusive `conflita_com` | RF-05 |
| 5 | Medir "citação que sustenta", não só "citação que existe" | ○ mede só existência e transcrição | ◐ | ◐ | ● Stanford mede | ● precisão de citação | RF-22, RF-23 |
| 6 | Métricas por afirmação (citation recall/precision) | ○ | ○ | ◐ | ◐ | ● | RF-23 |
| 7 | Suporte parcial como classe própria | ○ | ○ | ○ | ◐ | ● | RF-23 |
| 8 | Recusa calibrada; falsa premissa; recusa contada à parte | ● separa invenção de incerteza | ◐ fallback ao LLM | ○ | ● Stanford | ● + contra-indicador de recusa excessiva | RF-18, métricas |
| 9 | Golden set com anotação humana e juiz calibrado | ◐ validação humana planejada para a 1.0 | ● LLM-juiz calibrado | ● Evaluators | ◐ | ● 2 anotadores + kappa; **gabarito independente da base** | RF-22 |
| 10 | Recuperação avaliada separada da geração | ○ | ○ | ○ | ● LegalBench-RAG | ● golden set de busca | RF-13 |
| 11 | Regressão a cada troca de modelo ou prompt | ◐ rodadas periódicas | ◐ | ● | ? | ● por tenant e a cada release | RF-23 a RF-25 |
| 12 | Moderação independente do gerador | ○ | ● IACMA | ○ | ● camada de verificação (Jus IA) [S] | ● verificador determinístico pós-resposta | RF-10 |
| 13 | MCP com poucas tools tipadas, limites e autenticação | ● 7 tools, sem auth | ● | ● API key | — | ● até 9 tools, OAuth por tenant | RF-08, RF-11, RNF-09 |
| 14 | Segurança de RAG e MCP (injection, poisoning) | ◐ rate limit | ● 4 camadas | ◐ | ? | ◐ requisito escrito, desenho a mapear | RNF-09, mapeamento 4.10 |
| 15 | Transparência e governança publicadas | ● decisões, changelog, licença | ● Transparency Record + DfE | ◐ | ◐ | ◐ changelog + declaração ao usuário; falta registro de transparência | RF-28, RNF-11 |

### Mecanismos que o A acrescenta e nenhuma referência tem junta

| Mecanismo | Por quê |
|---|---|
| **Teste de alucinação do LLM do próprio cliente**, com e sem base (RF-23, RF-24) | No modelo em que o cliente traz o LLM, o número genérico não serve. O Oak e o bncc.dev entregam a base, mas não medem o LLM que o cliente conectou [I] |
| **Detecção de dado pessoal de aluno antes do LLM** (RF-17) | Exclusivo do contexto de educação especial com LLM de terceiros. O DfE pede privacidade, mas não esse mecanismo [I] |
| **Conflito normativo como dado, sem decidir** (RF-05, C4) | Federal × estadual é o caso real da Port. 421 × Res. SEDUC 129 (Q-INC-07) |
| **Aviso de mudança normativa ao usuário** (RF-26, RF-27) | As referências versionam a base, mas não avisam quem usou a versão antiga [I] |
| **Interpretação pedagógica rotulada e separada da norma** (RF-06) | O bncc.dev faz isso nos alinhamentos da EI (`nota`); o Oak mistura com o conteúdo da aula |

## 4. Lacunas do A diante do padrão ouro

O que o PRD ainda não cobre bem e precisa entrar no mapeamento:

1. **Registro de transparência algorítmica público**, no modelo do Aila e dos padrões 1, 4 e 9 do DfE. Hoje só existe a declaração ao usuário (RNF-11). Proposta: um documento público por data-version, com propósito, limites, modelo de avaliação e últimos resultados.
2. **Moderação independente de conteúdo**, não só de citação. O verificador do RF-10 confere a citação, mas não pega orientação pedagógica inadequada, como uma sugestão capacitista. O Oak usa um agente que não vê o prompt. Avaliar se cabe no A (mapeamento 4.7).
3. **OWASP MCP Top 10 (tool poisoning)**. Entra no bloco 4.10 do mapeamento como ameaça específica: descrições de tool e conteúdo de fonte como vetor de injeção.
4. **Recuperação avaliada com trecho-ouro** (estilo LegalBench-RAG). O golden set de busca do RF-13 precisa de dispositivo-ouro por pergunta, não só de resposta-ouro.
5. **Intervalo de confiança nas métricas** (ARES/PPI, bootstrap como o bncc.dev). Precisa ser acrescentado ao protocolo de avaliação.

## 5. Onde o bncc.dev é melhor e não vale competir

| Ponto | Decisão proposta |
|---|---|
| Dataset BNCC verificado, com DOI | extração própria da fonte oficial, com a mesma exigência de verificação |
| Benchmark público de 19 modelos na BNCC | citar como linha de base, sem replicar. O nosso benchmark é de **legislação** e do **LLM do cliente** |
| Pacotes abertos npm/PyPI e MCP sem cadastro | não competir em distribuição gratuita de BNCC. O MCP do A pode até **delegar** a parte BNCC ao bncc.dev `[A CONFIRMAR]`: dependência externa em produção × base própria pinada |

**Risco competitivo [I]:** o bncc.dev declara serviços pagos para "secretarias, redes, editoras e edtechs" (currículos estaduais, mapas de progressão). Se ele estender o mesmo método à legislação de inclusão, o diferencial do A passa a ser **o ambiente para o professor, o teste por LLM do cliente e a integração com C e B**, e não a base. Por isso a fase M0 do mapeamento mede cedo onde está o valor (HIP-A2).

## 6. Pontos para o regulatório brasileiro (a verificar)

- **Parecer CNE/CP 15/2026** (aprovado em 01/09/2026, súmula no DOU em 06/10/2026): classifica usos de IA na educação por risco e proíbe o uso autônomo por alunos até o 5º ano [S]. A homologação pelo MEC não foi confirmada [NV]. O A é de uso do professor, o que provavelmente o põe em risco baixo [I]. Ler o texto e incluí-lo **no corpus** do A, porque o professor vai perguntar sobre ele.
- **Referencial do MEC para uso responsável de IA na educação** (consulta pública até 29/10/2025) [S/NV].
- **PL 2338/2023:** "Aguardando Parecer do Relator na Comissão Especial" da Câmara, conforme ficha consultada em 05/11/2026 [V].
- **AI Act (referência, D20 em standby):** educação é alto risco quando a IA avalia, admite ou classifica aluno. O A não faz nenhum dos três. As obrigações do Anexo III foram adiadas para 02/12/2027 [S].

## Referências

- bncc.dev: <https://bncc.dev/benchmark/>, <https://bncc.dev/benchmark/estudo-mcp/>, <https://github.com/bncc-dev/bncc-benchmark>
- Oak: <https://arxiv.org/abs/2508.05360>, <https://arxiv.org/abs/2502.10410>, <https://www.gov.uk/algorithmic-transparency-records/oak-national-academy-aila-oaks-ai-lesson-assistant>, <https://www.thenational.academy/mcp>
- Learning Commons: <https://docs.learningcommons.org/knowledge-graph/using-knowledge-graph/mcp-server>, <https://docs.learningcommons.org/evaluators/understanding-evaluators/introduction>
- 1EdTech CASE: <https://www.1edtech.org/standards/case>
- Stanford: <https://arxiv.org/abs/2405.20362> (JELS 22(2), 2025, doi:10.1111/jels.12413)
- LegalBench-RAG: <https://arxiv.org/abs/2408.10343>; CLERC: <https://arxiv.org/abs/2406.17186>
- URN LEX: <https://datatracker.ietf.org/doc/rfc9676/>
- ALCE: <https://arxiv.org/abs/2305.14627>; FActScore: <https://arxiv.org/abs/2305.14251>; ARES: <https://arxiv.org/abs/2311.09476>; TREC RAG 2024: <https://arxiv.org/abs/2411.09607>, <https://arxiv.org/abs/2504.15205>
- PL 2338/2023: <https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262>
