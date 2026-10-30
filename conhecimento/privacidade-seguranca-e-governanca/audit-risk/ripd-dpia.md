---
id: psg.audit.ripd-dpia
titulo: Relatório de impacto à proteção de dados (RIPD/DPIA)
tipo: protocolo
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-30
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, anpd22022, anpd2023ripdfaq, anpd182024, sgd2026guiaripd, sgd2026modeloripd, eu2016gdpr, wp292017wp248, cnil2018piamethodology, iso291342023]
relacoes:
  - { tipo: depende-de, alvo: psg.audit.processing-records }
  - { tipo: depende-de, alvo: psg.audit.privacy-risk-management }
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: psg.audit.audit-trails }
  - { tipo: complementa, alvo: psg.legal.gdpr-k-and-coppa }
  - { tipo: complementa, alvo: psg.legal.eca-and-digital-eca }
  - { tipo: complementa, alvo: psg.ai.ai-governance-frameworks }
  - { tipo: complementa, alvo: psg.ai.transparency-and-human-oversight }
  - { tipo: relacionado-a, alvo: psg.sec.incident-management }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: especificado-por, alvo: iop.br.lgpd }
termos: [RIPD, DPIA, PIA, alto risco, critério geral, critério específico, avaliação de impacto, necessidade e proporcionalidade, risco residual, consulta prévia, versão publicizável, evento temido]
---

# Relatório de impacto à proteção de dados (RIPD/DPIA)

## Definição e terminologia

A LGPD define o **relatório de impacto à proteção de dados pessoais** (RIPD) como "documentação do controlador" que descreve os processos de tratamento que podem gerar riscos às liberdades civis e aos direitos fundamentais, com as medidas de mitigação adotadas (art. 5, XVII) [F: brasil2018lgpd]. No GDPR, o instituto é a **data protection impact assessment** (DPIA) do art. 35; a CNIL usa **privacy impact assessment** (PIA) como sinônimo e aplica a sigla a ambos [F: cnil2018piamethodology, Foreword]. A ISO/IEC 29134:2023, segunda edição, publicada em maio de 2023, dá diretrizes para o processo de PIA e para a estrutura do relatório; só seus metadados foram verificados [F: iso291342023, metadados].

O RIPD não é o registro das operações (art. 37), que o antecede; não é a avaliação de risco de segurança da informação, que é um de seus insumos; e não é um documento de aprovação única: a ANPD recomenda "revisão contínua" e o WP29 afirma que "Carrying out a DPIA is a continual process, not a one-time exercise" [F: anpd2023ripdfaq; wp292017wp248, §III.D.a].

## Problema que resolve

A pergunta prática é quando o relatório é obrigatório. A LGPD trata o RIPD como documento que a ANPD "poderá determinar" (art. 38) ou "poderá solicitar" quando a base for o legítimo interesse (art. 10, §3), e dá à autoridade competência para editar regulamentos sobre "relatórios de impacto à proteção de dados pessoais para os casos em que o tratamento representar alto risco" (art. 55-J, XIII, incluído pela Lei 13.853/2019) [F: brasil2018lgpd]. A ANPD reconhece que a lei "não determina, como regra geral, o encaminhamento do relatório à ANPD" e que o controlador "tem o dever de encaminhar o RIPD apenas quando requisitado" [F: anpd2023ripdfaq]. Mas, "como regra geral, é recomendado elaborar o RIPD em todo contexto em que as operações de tratamento de dados pessoais possam gerar alto risco", e isso "deverá ser avaliado pelo agente de tratamento" [F: anpd2023ripdfaq]. O problema que o relatório resolve é, portanto, demonstrar antes do tratamento que o controlador identificou e tratou riscos, sob o princípio da responsabilização (art. 6, X) [I].

## Fundamentos e funcionamento

### Quando: o teste de alto risco

Enquanto não há regulamento específico, a ANPD orienta adotar como parâmetro o art. 4 do regulamento para agentes de pequeno porte: o tratamento é de alto risco se, no caso concreto, estiver presente "ao menos, um critério geral" e "um critério específico" [F: anpd2023ripdfaq; anpd22022, art. 4]. Os critérios gerais são tratamento "em larga escala" e tratamento "que possa afetar significativamente interesses e direitos fundamentais dos titulares"; os específicos são "uso de tecnologias emergentes ou inovadoras", "vigilância ou controle de zonas acessíveis ao público", "decisões tomadas unicamente com base em tratamento automatizado de dados pessoais, inclusive aquelas destinadas a definir o perfil pessoal, profissional, de saúde, de consumo e de crédito ou os aspectos da personalidade do titular" e "utilização de dados pessoais sensíveis ou de dados pessoais de crianças, de adolescentes e de idosos" [F: anpd22022, art. 4]. Larga escala considera "número significativo de titulares", volume, duração, frequência e extensão geográfica (§1); afetar significativamente inclui impedir o exercício de direitos ou o uso de um serviço e causar discriminação (§2) [F: anpd22022]. A ANPD acrescenta que esses critérios "não devem ser considerados exaustivos" [F: anpd2023ripdfaq].

Aplicado a uma plataforma educacional com dados de menores e de saúde ou deficiência: o critério específico (d) está satisfeito por definição; se a plataforma adapta conteúdo por decisão automatizada que define "perfil ... de saúde ... ou os aspectos da personalidade", o critério (c) também; o uso de modelos de IA pode caracterizar (a) [I]. Basta então um critério geral: uma rede escolar com número significativo de alunos configura larga escala, e uma adaptação que restrinja o acesso de um aluno a conteúdos ou o classifique pode "afetar significativamente" seus direitos [I]. A conclusão deste documento é que o RIPD é, na prática, exigível para essa classe de plataforma, ainda que a obrigação formal na LGPD permaneça condicionada à determinação da ANPD [I]. O guia federal vai além e recomenda considerar o relatório "também quando a operação de tratamento apresentar isoladamente dois ou mais desses fatores de risco", invocando o WP29 [F: sgd2026guiaripd, §3.1], e lembra que a Lei 15.211/2025 (ECA Digital) traz obrigações adicionais para dados de crianças e adolescentes em ambientes digitais [F: sgd2026guiaripd, §3.1].

No GDPR, o art. 35(1) exige a DPIA antes do tratamento quando, "in particular using new technologies", ele for provável fonte de alto risco; o art. 35(3) cita avaliação sistemática e extensiva com perfilamento e decisões com efeito significativo, tratamento em larga escala de categorias especiais e monitoramento sistemático de área pública [F: eu2016gdpr, art. 35]. O WP29 deriva nove critérios: avaliação ou pontuação; decisão automatizada com efeito significativo; monitoramento sistemático; dados sensíveis ou de natureza altamente pessoal; larga escala; cruzamento de bases; dados de titulares vulneráveis, que "may include children (they can be considered as not able to knowingly and thoughtfully oppose or consent to the processing of their data)"; uso inovador de tecnologia; e tratamento que impede o exercício de um direito ou o uso de um serviço [F: wp292017wp248, §III.B.a]. A regra prática: "In most cases, a data controller can consider that a processing meeting two criteria would require a DPIA", e em alguns casos basta um [F: wp292017wp248, §III.B.a]. O recital 75 lista entre os riscos o tratamento de dados "of vulnerable natural persons, in particular of children" e a avaliação de aspectos pessoais para criar perfis [F: eu2016gdpr, recital 75].

### Conteúdo

O conteúdo mínimo da LGPD é "a descrição dos tipos de dados coletados, a metodologia utilizada para a coleta e para a garantia da segurança das informações e a análise do controlador com relação a medidas, salvaguardas e mecanismos de mitigação de risco adotados" (art. 38, parágrafo único) [F: brasil2018lgpd]. A ANPD recomenda doze blocos: identificação dos agentes e do encarregado; partes consultadas e pareceres; justificativa da elaboração; projeto ou processo; sistemas de informação; descrição do tratamento da coleta à eliminação, com dados, dados sensíveis, categorias de titulares, dados de crianças e adolescentes, volume, fonte, finalidade por dado, compartilhamentos e política de armazenamento; análise de hipótese legal por finalidade; análise de princípios; riscos ao titular; resultado da metodologia; medidas e salvaguardas; comentários e aprovações [F: anpd2023ripdfaq]. O GDPR exige descrição sistemática, avaliação de necessidade e proporcionalidade, avaliação dos riscos e medidas previstas (art. 35(7)), e a consulta aos titulares ou representantes "where appropriate" (35(9)) [F: eu2016gdpr]. O Anexo 2 do WP29 converte isso em critérios de aceitabilidade de uma metodologia, incluindo que origem, natureza e severidade dos riscos sejam apreciadas para cada risco de "illegitimate access, undesired modification, and disappearance of data" e que o parecer do encarregado seja buscado [F: wp292017wp248, Annex 2].

O modelo federal de 2026 organiza o relatório por "produto ou serviço" e distingue a versão integral, para governança interna e envio à ANPD quando solicitado, da versão publicizável, que deve evitar expor fluxos detalhados, arquitetura, matriz de riscos preenchida, riscos residuais e controles específicos [F: sgd2026modeloripd, Orientações 4]. A ANPD confirma que a divulgação não é obrigatória, mas que a versão pública "pode ser distinta da versão interna" para resguardar segredos [F: anpd2023ripdfaq].

### Método

A CNIL estrutura o PIA em quatro passos: estudo do contexto; estudo dos princípios fundamentais, cobrindo proporcionalidade e necessidade e os direitos dos titulares; estudo dos riscos de segurança dos dados, para cada evento temido (acesso ilegítimo, modificação indesejada, desaparecimento), estimando severidade e verossimilhança; e validação formal, que pode ser aprovação, aprovação condicionada ou recusa do tratamento [F: cnil2018piamethodology, §1 a §4]. A CNIL declara o método compatível com o WP29 e com a ISO 31000, e afirma que ele "should be implemented as soon as a new processing of personal data is designed" [F: cnil2018piamethodology, Introduction; How is a PIA carried out?]. A ANPD deixa a escolha da metodologia ao controlador, recomendando as "reconhecidas como boas práticas pela comunidade técnica" e exigindo que a identificação dos fatores de risco seja "documentada e justificada" [F: anpd2023ripdfaq].

### Quem e quando

O controlador elabora e aprova; a ANPD diz ser "desejável que o encarregado seja consultado" [F: anpd2023ripdfaq], e o regulamento de 2024 inclui o RIPD entre as matérias em que o encarregado presta assistência (art. 16, III) [F: anpd182024]. O WP29 lembra que o controlador "remains ultimately accountable" mesmo que terceiros executem, e que operadores devem assistir [F: wp292017wp248, §III.D.b]. Momento: antes de iniciar o tratamento e, se não for possível, "assim que se identificar um tratamento que possa gerar alto risco" [F: anpd2023ripdfaq]. Gatilhos de revisão segundo o guia federal: nova finalidade ou novo dado, mudança de hipótese legal, novo agente ou compartilhamento, novas orientações da ANPD, incidente de segurança, com revisão periódica anual como boa prática [F: sgd2026guiaripd, §4.5]; o GDPR exige revisão "at least when there is a change of the risk" (art. 35(11)) [F: eu2016gdpr].

## Requisitos e pressupostos

- Registro das operações já existente (`psg.audit.processing-records`), pois o relatório descreve o que foi mapeado [F: sgd2026guiaripd, §5].
- Metodologia de risco definida e alinhada à governança institucional, para que o RIPD "não constitua uma matriz de riscos paralela" [F: sgd2026guiaripd, §4.4]; ver `psg.audit.privacy-risk-management`.
- Base legal identificada por finalidade, inclusive para dados sensíveis de menores (`psg.legal.lgpd-children`) [I].

## Vantagens e limitações

O relatório antecipa riscos, documenta a ponderação e serve como "evidências primárias de conformidade em processos de fiscalização" [F: sgd2026guiaripd, §5]. Limitações: a LGPD não fixa a obrigação direta, e o critério de alto risco é emprestado de um regulamento para pequeno porte; a análise de impacto sobre titulares é a parte mais frágil de qualquer metodologia, como reconhece a literatura de risco (ver `psg.audit.privacy-risk-management`); e um RIPD genérico para "a plataforma" diluiu riscos que só aparecem por finalidade, o que a ANPD evita ao recomendar um relatório por projeto ou processo [F: anpd2023ripdfaq; I].

## Alternativas e comparações

| Critério | LGPD + ANPD | GDPR + WP29 | CNIL PIA |
|---|---|---|---|
| Gatilho | Alto risco: 1 geral + 1 específico (Res. 2/2022 art. 4); não exaustivo | Provável alto risco; 9 critérios, regra de 2 | Não define gatilho; remete ao art. 35(1) |
| Obrigação | Determinação da ANPD; recomendação geral | Obrigação direta antes do tratamento | Método, não obrigação |
| Conteúdo mínimo | Art. 38, p.u., + 12 blocos recomendados | Art. 35(7) a-d; Anexo 2 | Contexto, princípios, riscos, validação |
| Envio à autoridade | Só quando requisitado | Consulta prévia se risco residual alto (art. 36) | Idem GDPR |
| Fonte | [F: brasil2018lgpd; anpd2023ripdfaq] | [F: eu2016gdpr; wp292017wp248] | [F: cnil2018piamethodology] |

## Métricas e métodos de avaliação

Cobertura: operações de alto risco com RIPD aprovado antes do início [I]. Aceitabilidade metodológica: conformidade com o Anexo 2 do WP29, item a item [F: wp292017wp248, Annex 2]. Residual: riscos acima do nível de aceitação formalmente aceitos com justificativa e responsável [F: sgd2026guiaripd, §4.4]. Vitalidade: tempo entre gatilho de revisão e nova versão [I].

## Exemplo técnico independente de domínio

```
teste_de_alto_risco(operacao):
  geral = larga_escala(operacao) or afeta_significativamente(operacao)
  especifico = tecnologia_inovadora or vigilancia_publica
             or decisao_unicamente_automatizada or (dados_sensiveis or menores_ou_idosos)
  se geral and especifico: RIPD obrigatório pelo parâmetro ANPD
  senão se contagem_criterios_wp29(operacao) >= 2: RIPD recomendado (guia federal)
  senão: documentar a avaliação e a decisão de não elaborar

ripd:
  escopo: produto_ou_servico -> lista de operacoes (ref. registro art. 37)
  secoes: contexto | tratamento | hipoteses legais | principios | direitos |
          riscos (evento_temido x fonte x verossimilhanca x severidade) |
          medidas | residuais aceitos | consultas (encarregado, titulares) | aprovacao
  versoes: integral (interna) | publicizavel (sem matriz, sem arquitetura)
  revisao: gatilhos + anual
```

## Relações com outros conceitos

Depende de `psg.audit.processing-records`, `psg.audit.privacy-risk-management` e `psg.legal.lgpd-children`. Complementa `psg.audit.audit-trails`, que aparece no relatório como salvaguarda de rastreabilidade e, ao mesmo tempo, como operação a avaliar; `psg.legal.gdpr-k-and-coppa` e `psg.legal.eca-and-digital-eca` para as referências comparativas e o ECA Digital; `psg.ai.ai-governance-frameworks` e `psg.ai.transparency-and-human-oversight` para o critério de decisão automatizada. Incidentes (`psg.sec.incident-management`) são gatilho de revisão; o risco de reidentificação (`psg.deid.reidentification-risk`) é um dos riscos a avaliar.

## Lacunas e questões abertas

- A ANPD ainda não editou o regulamento específico de RIPD previsto no art. 55-J, XIII; a página de perguntas e respostas, modificada em 23/09/2026, continua a remeter ao art. 4 da Res. 2/2022.
- O texto da ISO/IEC 29134:2023 não foi acessado; sua estrutura de relatório não pôde ser comparada com os blocos da ANPD.
- O ECA Digital (Lei 15.211/2025) é citado pelo guia federal; o texto da lei foi lido em psg.legal.eca-and-digital-eca, e o relatório de impacto que ela prevê aparece em psg.legal.comparison. A integração desse relatório com o RIPD da LGPD não é tratada aqui.
- Falta orientação sobre como consultar crianças e responsáveis na elaboração do relatório (art. 35(9) do GDPR; "público externo" na ANPD), em especial alunos com deficiência intelectual ou de comunicação.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| anpd22022 | normativo | 2026-10-29 |
| anpd2023ripdfaq | tecnico | 2026-10-29 |
| anpd182024 | normativo | 2026-10-29 |
| sgd2026guiaripd | tecnico | 2026-10-29 |
| sgd2026modeloripd | tecnico | 2026-10-29 |
| eu2016gdpr | normativo (texto lido em espelho) | 2026-10-29 |
| wp292017wp248 | tecnico | 2026-10-29 |
| cnil2018piamethodology | tecnico | 2026-10-29 |
| iso291342023 | normativo [metadados] | 2026-10-29 |
