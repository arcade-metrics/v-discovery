---
id: psg.sec.incident-management
titulo: Gestão de incidentes e comunicação à ANPD e aos titulares
tipo: protocolo
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-30
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, anpd152024, anpd2026cis, anpd2021pequenoporte, nist2025sp80061, k12six2022stateofk12, verizon2025dbir, cis2026k12]
relacoes:
  - { tipo: especificado-por, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: psg.sec.threat-model-education }
  - { tipo: complementa, alvo: psg.sec.encryption-and-key-management }
  - { tipo: parte-de, alvo: psg.sec.iso-27001-and-27701 }
  - { tipo: depende-de, alvo: psg.audit.audit-trails }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: complementa, alvo: psg.audit.processing-records }
  - { tipo: complementa, alvo: psg.consent.parental-consent }
  - { tipo: relacionado-a, alvo: rtm.rel.fault-tolerance }
termos: [incidente de segurança, risco ou dano relevante, comunicação de incidente, controlador, encarregado, registro de incidente, ciclo de vida de resposta a incidentes, CSF 2.0, lições aprendidas, agente de tratamento de pequeno porte]
---

# Gestão de incidentes e comunicação à ANPD e aos titulares

## Definição e terminologia

O regulamento da ANPD define **incidente de segurança** como "qualquer evento adverso confirmado, relacionado à violação das propriedades de confidencialidade, integridade, disponibilidade e autenticidade da segurança de dados pessoais", e define cada propriedade, inclusive autenticidade (garantia de que a informação foi produzida, modificada ou destruída por determinada pessoa, equipamento ou sistema) [F: anpd152024, art. 3, II, V, XI, XII, XIII]. O NIST distingue **evento** (qualquer ocorrência observável em ativos computacionais), **evento adverso** (com consequência negativa, qualquer causa) e **incidente de cibersegurança**, ocorrência que "actually or imminently jeopardizes, without lawful authority, the integrity, confidentiality, or availability of information or an information system" ou viola políticas [F: nist2025sp80061, §1]. [I] As duas definições se complementam: a da ANPD exige confirmação e envolve dado pessoal; a do NIST abrange a análise que leva da suspeita à confirmação.

**Gestão de incidentes** é o processo que vai da preparação à comunicação e às lições aprendidas. **Comunicação de incidente** é o "ato do controlador que comunica à ANPD e ao titular de dados a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante" [F: anpd152024, art. 3, IV]. Não é o mesmo que o plano de continuidade (ver `rtm.rel.fault-tolerance`), embora um incidente de disponibilidade acione os dois [I].

## Problema que resolve

A LGPD determina que "o controlador deverá comunicar à autoridade nacional e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante aos titulares", em prazo razoável definido pela autoridade, com conteúdo mínimo (natureza dos dados, titulares envolvidos, medidas de segurança, riscos, motivos da demora, medidas de mitigação); a autoridade pode determinar ampla divulgação e medidas de reversão, e avalia, no juízo de gravidade, se os dados foram tornados ininteligíveis [F: brasil2018lgpd, art. 48]. O art. 50 inclui "planos de resposta a incidentes e remediação" entre os elementos do programa de governança em privacidade [F: brasil2018lgpd, art. 50, §2]. Em educação, o problema é agravado pela baixa capacidade: 66% dos distritos americanos têm uma ou duas pessoas para segurança [F: cis2026k12], o K12 SIX relata exigências de divulgação "quite weak" e distritos que tomaram medidas para evitar divulgar [F: k12six2022stateofk12], e no DBIR 2025, seção Educational Services, os erros respondem por 29% das violações do setor, com envio ao destinatário errado (Misdelivery) como principal variedade de erro: 17% de todas as violações do setor (p. 73) e 60% das violações por erro (p. 74) [F: verizon2025dbir, Educational Services, p. 73-74]. [I] Um fluxo de incidentes bem definido é o que permite a uma equipe pequena cumprir prazos de dias úteis sob pressão.

## Fundamentos e funcionamento

### O regulamento brasileiro (Resolução CD/ANPD nº 15/2024)

Aprovada em 24 de abril de 2024, a resolução regulamenta o art. 48 e altera o regulamento de pequeno porte para remeter a ela [F: anpd152024, arts. 1-2 e anexo, art. 1]. Seus pontos operacionais:

- **Critérios.** Há risco ou dano relevante quando o incidente "puder afetar significativamente interesses e direitos fundamentais dos titulares" e, cumulativamente, envolver ao menos um de: dados sensíveis; "dados de crianças, de adolescentes ou de idosos"; dados financeiros; dados de autenticação em sistemas; dados sob sigilo legal, judicial ou profissional; ou dados em larga escala. Afetar significativamente inclui impedir o exercício de direitos ou o uso de um serviço e causar danos materiais ou morais, "tais como discriminação, violação à integridade física, ao direito à imagem e à reputação, fraudes financeiras ou roubo de identidade"; larga escala considera número de titulares, volume, duração, frequência e extensão geográfica [F: anpd152024, art. 5]. [I] Para uma plataforma escolar, o critério de crianças e adolescentes está quase sempre presente; a questão passa a ser o "afetar significativamente".
- **Prazo e forma à ANPD.** Três dias úteis, contados do conhecimento pelo controlador de que o incidente afetou dados pessoais, por formulário eletrônico, pelo encarregado ou representante com documento de vínculo; complementação fundamentada em até vinte dias úteis; prazos em dobro para agentes de pequeno porte [F: anpd152024, art. 6, caput, §§1, 3-5, 8]. A página da ANPD informa que o envio é por peticionamento no SEI!ANPD, com formulário preliminar ou completo, e que informações adicionais seguem por peticionamento intercorrente [F: anpd2026cis].
- **Conteúdo à ANPD.** Natureza e categoria dos dados; número de titulares, "discriminando, quando aplicável, o número de crianças, de adolescentes ou de idosos"; medidas de segurança antes e depois; riscos e impactos; motivos da demora; medidas de reversão; datas de ocorrência e de conhecimento; dados do encarregado; identificação do controlador (e declaração de pequeno porte, se for o caso) e do operador; descrição com causa principal; e total de titulares das atividades afetadas [F: anpd152024, art. 6, §2].
- **Titulares.** Mesmo prazo de três dias úteis; linguagem "simples e de fácil entendimento"; de forma direta e individualizada pelos meios usuais (telefone, e-mail, mensagem, carta); se inviável, por site, aplicativos, redes sociais e canais de atendimento, com visualização direta por no mínimo três meses; declaração à ANPD de que a comunicação foi feita em até três dias úteis após o prazo; incluir recomendações de mitigação pode contar como boa prática [F: anpd152024, art. 9].
- **Registro.** O controlador mantém registro de todo incidente, "inclusive daquele não comunicado", por no mínimo cinco anos, com data de conhecimento, circunstâncias, natureza dos dados, número de titulares, avaliação de risco, medidas, forma e conteúdo da comunicação ou motivos da ausência dela [F: anpd152024, art. 10].
- **Poderes da ANPD.** Pedir o registro das operações, o RIPD e o relatório de tratamento do incidente; determinar medidas preventivas imediatas, com multa diária; determinar ampla divulgação às expensas do controlador quando a comunicação for insuficiente; apurar de ofício incidentes não comunicados e instaurar processo sancionador por descumprimento dos prazos [F: anpd152024, arts. 8, 15, 16-17, 19, 21].

### O ciclo de vida (NIST SP 800-61 rev. 3)

A revisão 3 (abril de 2025) substitui o ciclo "Preparation / Detection & Analysis / Containment, Eradication & Recovery / Post-Incident Activity" por um modelo baseado nas seis funções do CSF 2.0: Govern, Identify e Protect preparam e reduzem incidentes; Detect, Respond e Recover os descobrem, contêm, erradicam e recuperam, "as well as perform incident reporting, notification, and other incident-related communications"; e a categoria Improvement (ID.IM) recebe lições aprendidas de todas as funções, continuamente, porque hoje "recovering from them often takes weeks or months" [F: nist2025sp80061, §2.1, tabela 1]. Entre os exemplos de incidente estão ransomware que também exfiltra, phishing que compromete contas, credenciais de administrador em provedor SaaS e software de fornecedor comprometido [F: nist2025sp80061, §1]. [I] Para o controlador brasileiro, a comunicação regulatória é uma atividade de Respond com prazo legal; o registro de cinco anos e as lições aprendidas são Improvement.

### Divisão de responsabilidades

O regulamento atribui o dever ao controlador; a ANPD recomenda que obrigações de comunicação entre controlador e operador constem em contrato [F: anpd2026cis]. O guia de pequeno porte sugere cláusulas de segurança com fornecedores de TI e um ambiente que incentive funcionários e clientes a reportar incidentes e vulnerabilidades [F: anpd2021pequenoporte, §§29, 32]. [I] Numa plataforma usada por escolas, é preciso definir antes quem é controlador (escola, rede de ensino ou fornecedor) para cada base, pois o prazo de três dias úteis corre a partir do conhecimento pelo controlador.

## Requisitos e pressupostos

- Trilhas de auditoria e registros de tratamento que permitam, em dias, dizer quais dados, de quantos titulares (e quantas crianças), foram afetados (ver `psg.audit.audit-trails`, `psg.audit.processing-records`).
- Encarregado nomeado, com documento de vínculo pronto, e acesso ao SEI!ANPD configurado antes do primeiro incidente [F: anpd152024, art. 6, §5; F: anpd2026cis].
- Canais de contato com responsáveis legais atualizados; a comunicação ao titular criança passa pelo responsável (ver `psg.consent.parental-consent`) [I].
- Classificação de dados e modelo de ameaças que antecipem os cenários prováveis (ver `psg.sec.threat-model-education`).

## Vantagens e limitações

Um processo formal reduz o tempo de decisão e produz o registro que a ANPD pode exigir; a comunicação transparente é objetivo explícito do regulamento (confiança do titular, responsabilização) [F: anpd152024, art. 2]. Limites: os critérios do art. 5 exigem juízo ("afetar significativamente"), e a ANPD pode discordar e apurar de ofício [F: anpd152024, art. 16]; o prazo de três dias úteis é curto para investigação forense completa, daí a comunicação preliminar com complementação em vinte dias úteis [F: anpd152024, art. 6, §3]. O NIST adverte que detalhes de como executar resposta mudam tanto que "it is no longer feasible to capture and maintain that information in a single static publication" [F: nist2025sp80061, §1.1].

## Alternativas e comparações

| Referência | Natureza | O que determina | Prazo | Fonte |
|---|---|---|---|---|
| LGPD art. 48 | lei | dever de comunicar, conteúdo mínimo, poderes da ANPD | "prazo razoável" definido pela ANPD | [F: brasil2018lgpd] |
| Resolução CD/ANPD 15/2024 | regulamento | critérios, prazos, forma, registro, processo | 3 dias úteis (6 para pequeno porte); 20 para complementar | [F: anpd152024] |
| NIST SP 800-61 rev. 3 | guia (voluntário fora do governo dos EUA) | ciclo de vida alinhado ao CSF 2.0 | nenhum | [F: nist2025sp80061] |
| Guia ANPD pequeno porte | boas práticas sem efeito vinculante | medidas preventivas; remete o art. 48 a norma própria | nenhum | [F: anpd2021pequenoporte, §§15, 72] |

## Métricas e métodos de avaliação

Tempo entre ocorrência e conhecimento; entre conhecimento e comunicação à ANPD e aos titulares (meta: dentro de três dias úteis); fração de incidentes registrados versus comunicados, com motivo documentado [F: anpd152024, art. 10, §1, VIII]; completude dos doze itens do art. 6, §2, na primeira comunicação; tempo de recuperação do serviço; exercícios simulados por ano; lições aprendidas incorporadas ao modelo de ameaças [I].

## Exemplo técnico independente de domínio

```text
# Runbook mínimo (pseudo-fluxo), plataforma escolar hipotética
D0  detectar(evento) -> triagem: é adverso? envolve dado pessoal? confirmado?
    se confirmado: incidente = registrar(data_conhecimento, circunstancias)   # art. 10
    conter(): revogar sessões/tokens afetados, isolar base, preservar logs
D0  classificar(): sensivel? crianca_adolescente? autenticacao? larga_escala?  # art. 5
    afeta_significativamente? (direitos, uso do serviço, dano material/moral)
    se (afeta and algum_criterio): comunicar = True
D+3 dias úteis (x2 se pequeno porte):
    comunicar_anpd(formulario_preliminar, 12 itens do art. 6 §2, doc. do encarregado)
    comunicar_titulares(linguagem simples; direto e individualizado; senão site por >= 3 meses)
D+6 declarar_a_anpd(meios usados para comunicar titulares)                    # art. 9 §4
D+20 dias úteis: complementar(causa raiz, número final de titulares e de crianças)
sempre: erradicar(), recuperar(), lições_aprendidas() -> modelo de ameaças, RIPD
5 anos: guardar registro, mesmo se comunicar == False, com motivo
```

Exemplo de aplicação: credencial de professor obtida por phishing dá acesso ao painel de uma turma de 30 alunos por dois dias. É evento adverso confirmado, viola confidencialidade, envolve dado de criança e dado de autenticação (dois critérios do art. 5); se os dados visíveis permitem identificar e localizar os alunos, afeta significativamente direitos. Comunica-se à ANPD e aos responsáveis em três dias úteis; a comunicação cita que a base de pesquisa não foi afetada por estar pseudonimizada com chave separada (ver `psg.sec.encryption-and-key-management`) [I].

## Relações com outros conceitos

Especificado por `psg.legal.lgpd-children`, que aprofunda o art. 14 e o melhor interesse. Parte do sistema de gestão descrito em `psg.sec.iso-27001-and-27701`. Depende de `psg.audit.audit-trails` para reconstruir o que foi afetado e complementa `psg.audit.processing-records` e `psg.audit.ripd-dpia`, documentos que a ANPD pode requisitar [F: anpd152024, art. 8]. Complementa `psg.sec.threat-model-education` (os cenários previstos) e `psg.sec.encryption-and-key-management` (dado ininteligível no juízo de gravidade). Relaciona-se a `rtm.rel.fault-tolerance` na recuperação de disponibilidade.

## Lacunas e questões abertas

- Não foi aberto o formulário de comunicação vigente (arquivo .docx na página da ANPD); os campos citados vêm do regulamento, não do formulário.
- O guia da ANPD de 2021 remete o art. 48 a um guia específico; esse guia anterior (orientações de 2021 sobre incidentes) não foi localizado em versão vigente, e a página atual da ANPD já reflete a resolução de 2024.
- Não há critério objetivo publicado para "larga escala"; o regulamento prevê orientações futuras [F: anpd152024, art. 5, §3].
- Quem é controlador em arranjos escola–rede–fornecedor não é tratado aqui; depende de `psg.legal.lgpd-children` e dos contratos.
- Não foram lidas as tabelas 2 e 3 do SP 800-61r3 (perfil comunitário por subcategoria); só as seções 1-2.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| anpd152024 | normativo | 2026-10-29 |
| anpd2026cis | tecnico | 2026-10-29 |
| anpd2021pequenoporte | tecnico | 2026-10-29 |
| nist2025sp80061 | tecnico | 2026-10-29 |
| k12six2022stateofk12 | tecnico | 2026-10-29 |
| verizon2025dbir | tecnico | 2026-10-29 |
| cis2026k12 | tecnico (página de resumo) | 2026-10-29 |
