---
id: psg.sec.threat-model-education
titulo: Modelo de ameaças para dados educacionais de menores
tipo: tecnica
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [threatmodelingmanifesto2026, microsoft2017stride, kuleuven2026linddun, kuleuven2026linddunthreats, shostack2014threat, k12six2022stateofk12, verizon2025dbir, cis2026k12, anpd152024, brasil2018lgpd]
relacoes:
  - { tipo: complementa, alvo: psg.sec.encryption-and-key-management }
  - { tipo: complementa, alvo: psg.sec.incident-management }
  - { tipo: complementa, alvo: psg.sec.iso-27001-and-27701 }
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: psg.access.rbac-and-abac }
  - { tipo: complementa, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: parte-de, alvo: psg.audit.privacy-risk-management }
  - { tipo: relacionado-a, alvo: rtm.sec.authentication }
  - { tipo: relacionado-a, alvo: rtm.sec.transport-security }
  - { tipo: relacionado-a, alvo: iop.fund.privacidade-e-seguranca }
termos: [modelo de ameaças, STRIDE, LINDDUN, fronteira de confiança, diagrama de fluxo de dados, ativo, ator de ameaça, vetor de ataque, superfície de ataque, risco ou dano relevante]
---

# Modelo de ameaças para dados educacionais de menores

## Definição e terminologia

O Threat Modeling Manifesto define modelagem de ameaças como "analyzing representations of a system to highlight concerns about security and privacy characteristics", organizada em quatro perguntas: "What are we working on?", "What can go wrong?", "What are we going to do about it?" e "Did we do a good enough job?" [F: threatmodelingmanifesto2026]. O resultado é um **modelo de ameaças**: uma representação do sistema (em geral um diagrama de fluxo de dados, DFD) com **ativos**, **atores de ameaça**, **fronteiras de confiança** e uma lista de ameaças priorizadas com respostas. Não é um teste de invasão, nem uma lista de vulnerabilidades conhecidas: é um exercício de projeto, feito antes e durante o desenvolvimento [I].

Duas taxonomias são usadas aqui. **STRIDE**, da Microsoft, classifica ameaças de segurança em Spoofing (uso ilegítimo de credenciais alheias), Tampering (modificação maliciosa de dados persistidos ou em trânsito), Repudiation (negar uma ação sem que se possa provar o contrário), Information Disclosure (exposição a quem não deveria ter acesso), Denial of Service e Elevation of Privilege [F: microsoft2017stride]. **LINDDUN**, criado pelo grupo DistriNet da KU Leuven, faz o mesmo para privacidade, com sete tipos: Linking ("Associating data items or user actions to learn more about an individual or group"), Identifying ("Learning the identity of an individual, through leaks, deduction, or inference"), Non-repudiation ("Being able to attribute a claim to an individual"), Detecting ("Deducing the involvement of an individual through observation"), Data disclosure ("Excessively collecting, storing, processing or sharing personal data"), Unawareness and unintervenability ("Insufficiently informing, involving or empowering individuals in the processing of their personal data") e Non-compliance ("Deviating from security and data management best practices, standards and legislation") [F: kuleuven2026linddun; F: kuleuven2026linddunthreats]. Note que não-repúdio é propriedade desejável em STRIDE e ameaça em LINDDUN: a mesma trilha que prova quem fez o quê pode expor uma criança [I].

A referência de livro é Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014, 624 p.), cujo autor foi responsável pela modelagem de ameaças no ciclo de desenvolvimento seguro da Microsoft; só os metadados foram verificados nesta sessão [F: shostack2014threat, metadados].

## Problema que resolve

Plataformas educacionais tratam dados de crianças e adolescentes, que a LGPD manda tratar "em seu melhor interesse" [F: brasil2018lgpd, art. 14] e que o regulamento da ANPD lista entre os critérios de incidente com "risco ou dano relevante", junto com dados sensíveis e "dados de autenticação em sistemas" [F: anpd152024, art. 5]. Os relatórios setoriais mostram que a ameaça é concreta. Nos EUA, o K-12 Cyber Incident Map catalogou 166 incidentes em 2021, em 162 distritos de 38 estados, e 1.331 desde 2016; em 2021, pela primeira vez, ransomware foi o tipo mais frequente, com 62 casos em 24 estados [F: k12six2022stateofk12]. O relatório atribui responsabilidade a quatro grupos: membros da comunidade escolar sem treinamento, "tech-savvy students" que contornam controles ou usam acesso legítimo para "disrupt, cheat, or even cause harm to others", fornecedores cujas práticas não são avaliadas na contratação, e criminosos que exploram alvos fáceis por phishing em massa ou que estudam o distrito [F: k12six2022stateofk12]. O Verizon DBIR 2025 registra para Educational Services 1.075 incidentes e 851 violações confirmadas; System Intrusion, Miscellaneous Errors e Social Engineering somam 80% das violações; atores externos 62% e internos 38%; motivação financeira em 88%; dados pessoais em 58% e credenciais em 12%; ransomware é a variedade de malware mais comum (30%), uso de credenciais roubadas lidera o hacking (24%), erros respondem por 29% com envio ao destinatário errado em 17%, e phishing é 77% da engenharia social [F: verizon2025dbir]. Um levantamento de 2026 com dados do MS-ISAC indica que 51% das escolas e distritos relataram incidente nos últimos 12 meses e que 66% têm só uma ou duas pessoas responsáveis por segurança [F: cis2026k12]. O modelo de ameaças é o instrumento para decidir, com esse contexto, onde gastar recursos escassos [I].

## Fundamentos e funcionamento

O Manifesto valoriza "a culture of finding and fixing design issues" sobre conformidade de checklist, "continuous refinement" sobre entrega única, e lista como padrões o "Systematic Approach" (aplicar conhecimento de forma estruturada, reproduzível), "Varied Viewpoints" (equipe diversa) e "Theory into Practice"; como antipadrões, o "Hero Threat Modeler" e a "Perfect Representation" ("there is no single ideal view") [F: threatmodelingmanifesto2026]. Em termos de processo, as quatro perguntas viram etapas [I]:

1. **O que estamos construindo.** Um DFD com processos, armazenamentos, fluxos, entidades externas e fronteiras de confiança. A ferramenta da Microsoft nasce de perguntas como "How can an attacker change the authentication data?" e "What happens if access is denied to the user profile database?" [F: microsoft2017stride].
2. **O que pode dar errado.** Aplicar STRIDE a cada elemento e LINDDUN a cada fluxo de dado pessoal. O LINDDUN oferece três métodos: GO (baralho de ameaças comuns, para brainstorm estruturado), PRO (sistemático, a partir do DFD, com suporte a ferramentas) e MAESTRO (dirigido por modelo) [F: kuleuven2026linddun].
3. **O que fazer.** Para cada ameaça: mitigar (controle), eliminar (remover a funcionalidade ou o dado), transferir (contrato, seguro) ou aceitar, com registro.
4. **Fizemos um bom trabalho.** Revisão a cada mudança de arquitetura, teste das mitigações e realimentação com incidentes reais (ver `psg.sec.incident-management`).

## Requisitos e pressupostos

- Um DFD honesto, incluindo integrações com terceiros (LMS, provedores de identidade, nuvem) e os fluxos que saem para pesquisa; a maior parte dos incidentes graves em escolas envolve fornecedores [F: k12six2022stateofk12].
- Inventário de dados com classificação (pessoal, sensível, de criança, de autenticação), porque os critérios do art. 5 do regulamento da ANPD dependem dessa classificação [F: anpd152024, art. 5].
- Participação de quem conhece a sala de aula: muitos vetores (aparelho compartilhado, senha colada no caderno) não aparecem a quem só vê a arquitetura [I].

## Vantagens e limitações

STRIDE é simples de ensinar e cobre as propriedades clássicas de segurança; não captura ameaças de privacidade que não violam nenhuma delas (um sistema perfeitamente seguro pode coletar demais) [I]. LINDDUN preenche essa lacuna, mas exige mapear fluxos de dados pessoais em detalhe. Ambos produzem listas longas; sem priorização por probabilidade e impacto, viram "Admiration for the Problem", antipadrão nomeado pelo Manifesto [F: threatmodelingmanifesto2026]. Nenhum dos dois substitui o RIPD (`psg.audit.ripd-dpia`), que é documento jurídico; o modelo de ameaças é um de seus insumos técnicos [I].

## Alternativas e comparações

| Abordagem | Foco | Unidade de análise | Quando usar | Fonte |
|---|---|---|---|---|
| STRIDE | segurança (C, I, D, autenticação, autorização, não-repúdio) | elemento do DFD | todo sistema | [F: microsoft2017stride] |
| LINDDUN GO | privacidade, leve | baralho de ameaças | início, equipe mista | [F: kuleuven2026linddun] |
| LINDDUN PRO | privacidade, exaustivo | interações do DFD | sistemas com muitos fluxos de dado pessoal | [F: kuleuven2026linddun] |
| Lista de incidentes do setor | empírico | tipos de incidente observados | calibrar probabilidade | [F: k12six2022stateofk12; F: verizon2025dbir] |

## Métricas e métodos de avaliação

Cobertura (fração de elementos do DFD com ameaças analisadas), número de ameaças por categoria STRIDE/LINDDUN, fração mitigada versus aceita, idade do modelo em relação à última mudança de arquitetura, e incidentes reais não previstos pelo modelo (ver `psg.sec.incident-management`) [I]. O Manifesto aponta que o resultado só vale "when they are of value to stakeholders" [F: threatmodelingmanifesto2026].

## Exemplo técnico independente de domínio

Cenário hipotético, sem produto específico: plataforma de atividades usada por escolas; alunos entre 6 e 14 anos; tablets compartilhados em sala; uso offline com sincronização ao reconectar; câmera e microfone opcionais em algumas atividades; contas de professor com visão de turma; duas bases, uma de operação (identificada) e uma de pesquisa (pseudonimizada), com finalidades distintas.

```text
DFD (resumo)
  [Aluno] --(tablet compartilhado, cache offline)--> (App) --sync TLS--> (API) --> [[DB operação]]
  [Professor] --(painel de turma)--> (API)
  [Responsável] --(consentimentos, relatórios)--> (API)
  (API) --(pseudonimização, export periódico)--> [[DB pesquisa]] --> [Pesquisadores]
  (App) --(câmera/microfone, quando ativados)--> (API)
  Fronteiras: aparelho (não confiável, compartilhado) | rede escolar | nuvem | base de pesquisa
```

| Elemento | Ameaça | Categoria | Resposta (exemplo) |
|---|---|---|---|
| Tablet compartilhado | aluno B abre a sessão de A deixada aberta; vê e altera respostas | S, T, I (STRIDE); Identifying (LINDDUN) | sessão curta por aluno, troca de aluno por seleção com PIN/figura, bloqueio por inatividade; ver `rtm.sec.authentication` |
| Cache offline | aparelho perdido com dados de vários alunos em claro | I | cache cifrado com chave por aparelho, apagamento remoto, retenção mínima; ver `psg.sec.encryption-and-key-management` |
| Sincronização | replay ou injeção de eventos forjados ao reconectar | S, T | assinatura/MAC dos lotes, idempotência por id de evento, validação no servidor; transporte em `rtm.sec.transport-security` |
| Câmera/microfone | captura além da atividade; gravação retida | Data disclosure, Unawareness | ativação só na atividade, indicador visível, processamento local quando possível, não persistir mídia bruta |
| Conta de professor | phishing ou credencial reutilizada dá acesso a toda a turma | S, E; Identifying | MFA, sessões revogáveis, alerta de login novo; é "dado de autenticação" para fins do art. 5 [F: anpd152024] |
| DB operação | acesso amplo de equipe interna; exportação indevida | I, E; Linking | RBAC/ABAC por papel escolar (`psg.access.rbac-and-abac`), trilha de auditoria, exportação só por fluxo de pesquisa |
| DB pesquisa | reidentificação por ligação com a base de operação | Linking, Identifying | pseudonimização com chave separada, sem campos diretos, acesso por projeto (`psg.deid.anonymization-and-pseudonymization`) |
| Painel do responsável | não-repúdio excessivo: histórico minuto a minuto da criança | Non-repudiation, Detecting | agregação, janelas de tempo, finalidade pedagógica explícita |
| Toda a plataforma | ransomware indisponibiliza aulas | D | backups não sincronizados em tempo real, plano de recuperação; ver `rtm.rel.fault-tolerance` |

[I] A tabela é ilustrativa; a priorização real depende do contexto de cada escola.

## Relações com outros conceitos

Complementa `psg.sec.encryption-and-key-management` (resposta às ameaças de divulgação) e `psg.sec.incident-management` (o que acontece quando o modelo falha). É parte de `psg.audit.privacy-risk-management` e alimenta `psg.audit.ripd-dpia`. Depende de `psg.legal.lgpd-children` para classificar dados e finalidades. Controles de acesso e de desidentificação, respostas típicas às ameaças de elevação de privilégio e de ligação, estão em `psg.access.rbac-and-abac` e `psg.deid.anonymization-and-pseudonymization`. Autenticação de sessão e cifra de transporte não são repetidas aqui: ver `rtm.sec.authentication` e `rtm.sec.transport-security`; privacidade na troca entre sistemas está em `iop.fund.privacidade-e-seguranca`.

## Lacunas e questões abertas

- O texto de Shostack (2014) não foi lido; a formulação original das quatro perguntas foi tomada do Manifesto, que o lista entre os autores.
- O Manifesto não exibe ano de publicação na página; a chave usa o ano de consulta.
- As páginas do LINDDUN não descrevem o método PRO passo a passo (as páginas de detalhe não foram abertas); a descrição acima é a da página inicial.
- Não há relatório brasileiro equivalente ao K12 SIX ou ao DBIR com estatística de incidentes em escolas; os números acima são dos EUA e não devem ser extrapolados sem ressalva.
- O K12 SIX não publicou edições posteriores a 2022 localizáveis nesta sessão; o relatório CIS 2026 foi lido apenas pela página de resumo.
- Falta fonte sobre ameaças específicas de sensores (acelerômetro, toque) para inferência de atributos de crianças; fica como [H] a hipótese de que telemetria fina permita inferir deficiência ou estado emocional.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| threatmodelingmanifesto2026 | tecnico | 2026-10-29 |
| microsoft2017stride | fornecedor | 2026-10-29 |
| kuleuven2026linddun | academico | 2026-10-29 |
| kuleuven2026linddunthreats | academico | 2026-10-29 |
| shostack2014threat | tecnico (metadados) | 2026-10-29 |
| k12six2022stateofk12 | tecnico | 2026-10-29 |
| verizon2025dbir | tecnico | 2026-10-29 |
| cis2026k12 | tecnico (página de resumo) | 2026-10-29 |
| anpd152024 | normativo | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
