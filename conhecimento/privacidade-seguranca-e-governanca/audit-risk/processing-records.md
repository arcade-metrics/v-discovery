---
id: psg.audit.processing-records
titulo: Registro das operações de tratamento e inventário de dados
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, anpd22022, anpd182024, anpd2023ripdfaq, eu2016gdpr, sgd2026guiaripd, nist2020privacyframework]
relacoes:
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: complementa, alvo: psg.audit.audit-trails }
  - { tipo: complementa, alvo: psg.audit.privacy-risk-management }
  - { tipo: complementa, alvo: psg.consent.permission-lifecycle }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: psg.sec.incident-management }
  - { tipo: especificado-por, alvo: iop.br.lgpd }
termos: [registro das operações de tratamento, inventário de dados, mapeamento de dados, encarregado, agente de tratamento de pequeno porte, registro simplificado, records of processing activities, finalidade, base legal, prazo de retenção]
---

# Registro das operações de tratamento e inventário de dados

## Definição e terminologia

O **registro das operações de tratamento** é a documentação, mantida pelo controlador e pelo operador, de cada conjunto de operações realizadas com dados pessoais, organizada por finalidade. A LGPD determina: "O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem, especialmente quando baseado no legítimo interesse" (art. 37) [F: brasil2018lgpd]. A lei não detalha o conteúdo do registro; o regulamento da ANPD para agentes de pequeno porte permite cumpri-lo "de forma simplificada" e prevê que a ANPD fornecerá modelo (art. 9 e parágrafo único) [F: anpd22022]. No GDPR, o instituto equivalente é o **record of processing activities** do art. 30, cujo conteúdo é enumerado na norma [F: eu2016gdpr, art. 30]. Em português corrente, "inventário de dados" e "mapeamento de dados" designam o levantamento que alimenta o registro; aqui, inventário é o levantamento técnico (sistemas, campos, fluxos) e registro é o documento normativo derivado dele [I].

O que o registro não é: não é a trilha de auditoria por evento (`psg.audit.audit-trails`), não é o relatório de impacto (`psg.audit.ripd-dpia`), que parte dele mas avalia risco, e não é o aviso de privacidade ao titular, embora o alimente [I].

## Problema que resolve

Uma plataforma educacional trata dados de alunos, responsáveis e professores em dezenas de operações com finalidades, bases legais e prazos distintos: matrícula, adaptação pedagógica, comunicação com a família, analytics, suporte. Sem um registro por finalidade, não há como demonstrar o princípio de responsabilização e prestação de contas, definido como "demonstração, pelo agente, da adoção de medidas eficazes e capazes de comprovar a observância" das normas (art. 6, X) [F: brasil2018lgpd], nem como responder ao titular, que "tem direito ao acesso facilitado às informações sobre o tratamento de seus dados" (art. 9) [F: brasil2018lgpd]. O registro é também o ponto de partida do RIPD: o guia federal afirma que a elaboração do relatório "pressupõe que o órgão ou entidade tenha previamente mapeado as operações de tratamento", identificando finalidades, bases legais, tipos de dados, agentes e prazos de retenção [F: sgd2026guiaripd, §5].

## Fundamentos e funcionamento

### Conteúdo de referência

Como a LGPD não enumera campos, o art. 30(1) do GDPR serve de modelo de referência, não de obrigação [I]. Ele exige, para o controlador: (a) nome e contato do controlador, controlador conjunto, representante e encarregado; (b) finalidades; (c) categorias de titulares e de dados; (d) categorias de destinatários; (e) transferências internacionais; (f) prazos previstos de eliminação, quando possível; (g) descrição geral das medidas de segurança, quando possível [F: eu2016gdpr, art. 30(1)]. O registro deve ser escrito, inclusive em formato eletrônico, e disponibilizado à autoridade a pedido (art. 30(3), (4)) [F: eu2016gdpr]. A isenção para organizações com menos de 250 pessoas não vale quando o tratamento for provável fonte de risco, não for ocasional ou incluir categorias especiais de dados (art. 30(5)) [F: eu2016gdpr].

Os itens que a ANPD recomenda reunir no RIPD indicam o que ela espera encontrar documentado a montante: descrição do tratamento "desde a coleta até a eliminação", dados pessoais e sensíveis, categorias de titulares, dados "de crianças e adolescentes ou de outra categoria de vulneráveis", volume e número de titulares, fonte de coleta, finalidade justificada por dado, compartilhamentos internos e externos, "política de armazenamento (descrever os prazos de retenção e métodos de descarte)" e hipótese legal por finalidade [F: anpd2023ripdfaq]. Uma síntese razoável para o registro LGPD é, portanto, o art. 30(1) do GDPR acrescido de hipótese legal por finalidade, sinalização de dados sensíveis e de menores, e vínculo com o RIPD quando houver [I].

### Papéis: controlador, operador, encarregado

O art. 37 obriga controlador e operador [F: brasil2018lgpd]. O encarregado, cuja indicação o art. 41 exige do controlador, tem entre suas atividades "orientar os funcionários e os contratados" e "executar as demais atribuições determinadas pelo controlador" (art. 41, §2, III e IV) [F: brasil2018lgpd]. O regulamento da ANPD de 2024 torna explícito que cabe ao encarregado prestar assistência e orientação na elaboração e implementação do "registro das operações de tratamento de dados pessoais" (art. 16, II), ao lado do registro de incidentes (16, I) e do relatório de impacto (16, III), e que isso "não confere ao encarregado a responsabilidade, perante a ANPD, pela conformidade" (art. 17) [F: anpd182024]. Agentes de pequeno porte não são obrigados a indicar encarregado, desde que mantenham canal de comunicação com o titular (art. 11) [F: anpd22022]; mas não se beneficiam do regime diferenciado os que "realizem tratamento de alto risco" (art. 3, I), e o uso de dados sensíveis ou de dados de crianças e adolescentes é critério específico de alto risco (art. 4, II, d) [F: anpd22022]. Para uma plataforma educacional com menores, o registro simplificado dificilmente se aplica, mesmo a uma startup [I].

### Ciclo de vida e manutenção

O registro tem de refletir o término do tratamento, que ocorre, entre outras hipóteses, pela "verificação de que a finalidade foi alcançada ou de que os dados deixaram de ser necessários" (art. 15, I), e a eliminação subsequente, ressalvadas as hipóteses de conservação do art. 16 [F: brasil2018lgpd]. Cada linha do registro deve, assim, carregar o critério de término e o prazo de retenção [I]. No NIST Privacy Framework, a categoria Inventory and Mapping (ID.IM-P) descreve o resultado "Data processing by systems, products, or services is understood and informs the management of privacy risk", com a subcategoria ID.IM-P1 sobre inventário de sistemas que processam dados [F: nist2020privacyframework, Table 2]. Esse inventário técnico é a fonte da qual o registro jurídico é derivado, e mudanças no inventário (novo campo, novo fluxo, novo fornecedor) devem disparar atualização do registro [I].

## Requisitos e pressupostos

- Uma unidade de registro estável: a operação ou conjunto de operações com a mesma finalidade, que é também a unidade do RIPD segundo a ANPD ("um RIPD corresponde a cada projeto/processo do controlador que contenha um conjunto de operações de tratamento voltadas para uma mesma finalidade") [F: anpd2023ripdfaq].
- Identificação do papel (controlador, operador, controlador conjunto) em cada operação, porque a obrigação é de ambos e os conteúdos diferem [I].
- Versionamento do registro, para que se saiba o que estava declarado na data de um evento questionado, em paralelo à trilha de auditoria [I].

## Vantagens e limitações

O registro é a evidência mais barata de prestação de contas e o pré-requisito do RIPD e dos avisos de privacidade [I]. Suas limitações: a LGPD não fixa conteúdo, então organizações diferentes produzem documentos incomparáveis; o registro descreve a intenção, não a execução, e por isso precisa da trilha de auditoria para provar que o tratamento real seguiu o declarado; e registros mantidos manualmente envelhecem rápido em sistemas que mudam a cada versão [I].

## Alternativas e comparações

| Critério | LGPD art. 37 | GDPR art. 30 | Res. CD/ANPD 2/2022 art. 9 |
|---|---|---|---|
| Quem registra | Controlador e operador | Controlador e operador (30(1) e 30(2)) | Agentes de pequeno porte |
| Conteúdo | Não enumerado | Enumerado (a) a (g) | Simplificado, modelo da ANPD |
| Isenção | Nenhuma | Menos de 250 pessoas, com exceções | Não vale para alto risco |
| Ênfase | "especialmente quando baseado no legítimo interesse" | Disponibilizar à autoridade | Flexibilização sem isentar princípios (art. 6) |
| Fonte | [F: brasil2018lgpd] | [F: eu2016gdpr] | [F: anpd22022] |

## Métricas e métodos de avaliação

Completude: fração das operações do inventário técnico com linha correspondente no registro; divergência entre campos coletados e campos declarados [I]. Atualidade: tempo entre mudança no sistema e atualização do registro [I]. Rastreabilidade: cada operação de alto risco aponta para um RIPD e cada campo sensível aponta para uma hipótese legal do art. 11 [I]. Verificação cruzada com a trilha: amostrar eventos reais e confirmar que a operação consta do registro com a mesma finalidade [I].

## Exemplo técnico independente de domínio

```
operacao:
  id: op-017
  nome: adaptacao_de_percurso
  papel: controlador                      # ou operador, com o controlador indicado
  finalidade: ajustar sequencia de atividades ao desempenho do aprendiz
  hipotese_legal: art. 7, V (execucao de contrato) | art. 11, ... para dados sensiveis
  titulares: [aprendiz (crianca, adolescente), responsavel]
  dados: [respostas, tempo_de_resposta, estimativa_de_dominio]
  dados_sensiveis: [laudo_de_saude -> art. 11]        # sinalizado
  menores: sim                                        # critério específico Res. 2/2022 art. 4
  fonte: coleta direta na plataforma
  destinatarios: [escola (controlador conjunto?), fornecedor de hospedagem (operador)]
  transferencia_internacional: nao
  retencao: ate termino do vinculo + prazo legal X; criterio art. 15, I
  eliminacao: anonimizacao agregada ou exclusao
  seguranca: ref. politica PS-03
  ripd: RIPD-2026-03
  versao: 4   desde: 2026-02-10   aprovado_por: encarregado@...
```

## Relações com outros conceitos

Depende de `psg.legal.lgpd-children` para as hipóteses legais aplicáveis a menores e de `iop.br.lgpd` para as definições do art. 5. Complementa `psg.audit.ripd-dpia` (o registro é insumo do relatório), `psg.audit.audit-trails` (intenção versus execução) e `psg.audit.privacy-risk-management` (inventário como primeira categoria do Identify-P). O registro de consentimentos e revogações por titular, que é outro artefato, fica em `psg.consent.permission-lifecycle`; a minimização que o registro deve evidenciar, em `psg.access.minimization-and-privacy-by-design`. O registro de incidentes, listado ao lado no art. 16 do regulamento do encarregado, é tratado em `psg.sec.incident-management`.

## Lacunas e questões abertas

- O modelo de registro simplificado que a ANPD se comprometeu a fornecer (Res. 2/2022, art. 9, parágrafo único) não foi localizado em página oficial nesta sessão; fontes secundárias descrevem uma planilha, não verificada.
- Não há regulamento da ANPD detalhando o conteúdo mínimo do registro do art. 37 para agentes em geral; o conteúdo proposto aqui é síntese a partir do GDPR e das recomendações da ANPD para o RIPD, marcada como tal.
- O Regulamento de Dosimetria (Res. CD/ANPD 4/2023), que pode tratar a existência de registros como critério de boas práticas, não pôde ser aberto em fonte oficial nesta sessão e não foi citado.
- Fica em aberto se escola e plataforma são controladores conjuntos ou controlador e operador em cada operação; a resposta muda quem registra o quê.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| anpd22022 | normativo | 2026-10-29 |
| anpd182024 | normativo | 2026-10-29 |
| anpd2023ripdfaq | tecnico | 2026-10-29 |
| eu2016gdpr | normativo (texto lido em espelho) | 2026-10-29 |
| sgd2026guiaripd | tecnico | 2026-10-29 |
| nist2020privacyframework | tecnico | 2026-10-29 |
