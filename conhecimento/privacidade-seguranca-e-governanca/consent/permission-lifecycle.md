---
id: psg.consent.permission-lifecycle
titulo: Ciclo de vida das permissões
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, lei104062002, lei8069eca, eu2016gdpr, cfr16312coppa, ftc2025coppafinalrule, iso291842020, crc2021gc25, cns5102016]
relacoes:
  - { tipo: depende-de, alvo: psg.consent.parental-consent }
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: psg.consent.child-assent }
  - { tipo: complementa, alvo: psg.audit.processing-records }
  - { tipo: complementa, alvo: iop.fund.identidade-e-contexto }
  - { tipo: relacionado-a, alvo: psg.access.school-roles }
  - { tipo: relacionado-a, alvo: psg.legal.gdpr-k-and-coppa }
termos: [ciclo de vida da permissão, permissão, registro de consentimento, recibo de consentimento, revogação, mudança de finalidade, renovação de consentimento, renovação de aviso, transição à maioridade, término do tratamento, eliminação, bloqueio, versão do aviso, consentimento separado]
---

# Ciclo de vida das permissões

## Definição e terminologia

"Permissão" é aqui o termo de sistema para a autorização registrada de tratar certos dados de um titular para uma finalidade, sob uma base legal, com um aviso de versão conhecida, dada por alguém (o titular ou seu representante) em certo momento e por certo canal. O ciclo de vida da permissão é o conjunto de estados e transições por que ela passa: obtenção e prova, uso, revisão por mudança de aviso ou finalidade, renovação, revogação, migração de quem a detém (por exemplo quando a criança atinge a maioridade), término e eliminação ou conservação dos dados. Permissão não é sinônimo de consentimento: o consentimento é uma das bases legais [F: brasil2018lgpd, art. 7, I], e um sistema registra permissões também para tratamentos fundados em outras bases, para fins de transparência e prova [I].

A ISO/IEC 29184:2020, que "specifies controls which shape the content and the structure of online privacy notices as well as the process of asking for consent" [F: iso291842020, cláusula 1], chama o artefato de prova de "consent receipt or consent record" e traz exemplo em anexo informativo [F: iso291842020, sumário, Anexo B]. A CNS 510/2016 usa "registro do consentimento ou do assentimento" para o documento, em qualquer mídia, que registra a concessão [F: cns5102016, art. 2, XIX].

## Problema que resolve

A LGPD põe sobre o controlador o ônus de provar que o consentimento foi obtido conforme a lei [F: brasil2018lgpd, art. 8, §2], exige revogação "a qualquer momento [...] por procedimento gratuito e facilitado" [F: brasil2018lgpd, art. 8, §5], obriga a informar o titular com destaque quando mudam finalidade, forma e duração, identidade do controlador ou uso compartilhado, podendo ele revogar [F: brasil2018lgpd, art. 8, §6 e art. 9, §2], e manda eliminar os dados ao término do tratamento, salvo hipóteses de conservação [F: brasil2018lgpd, arts. 15 e 16]. Nenhuma dessas obrigações é cumprível sem um registro estruturado que saiba, para cada dado tratado, qual permissão o cobre, em que versão de aviso, e quem pode revogá-la. Para crianças, soma-se o fato de que quem deu a permissão (o responsável) não é o titular, e que o titular um dia deixará de ser criança.

## Fundamentos e funcionamento

### Estados e transições

```
[solicitada] --aviso v exibido, verificação ok--> [ativa(v)]
[ativa(v)]   --mudança de aviso/finalidade compatível--> [ativa(v+1)] (informar com destaque)
[ativa(v)]   --finalidade incompatível--> [solicitada(v+1)] (novo consentimento; a antiga continua só para o antigo)
[ativa(v)]   --revogação--> [revogada] (tratamentos passados ratificados; eliminação se requerida)
[ativa(v)]   --finalidade alcançada | fim do período--> [encerrada] --> eliminação ou conservação (art. 16)
[ativa(v)]   --titular atinge 18--> [a confirmar pelo titular] --confirmação--> [ativa, detentor=titular]
```
Os eventos são os do art. 8 §§5–6, art. 9 §2 e art. 15 da LGPD [F: brasil2018lgpd]; a transição de maioridade é construção deste documento, discutida abaixo [I].

### O que registrar

Do texto legal decorre o conteúdo mínimo do registro [I, a partir de brasil2018lgpd, arts. 8, 9, 14 e 18]: titular; quem deu a permissão e em que qualidade (titular, pai, mãe, responsável legal); vínculo verificado e método de verificação (art. 14 §5); finalidade específica, uma por permissão, porque autorização genérica é nula (art. 8 §4); elementos de dados cobertos; base legal; versão e cópia do aviso exibido, com as sete informações do art. 9 (finalidade, forma e duração, identificação e contato do controlador, uso compartilhado, responsabilidades, direitos); se o tratamento é condição para o serviço (art. 9 §3); data e hora; canal e forma da manifestação (escrita ou "outro meio que demonstre a manifestação de vontade", art. 8 caput); e, depois, cada evento de revisão, revogação, término e eliminação com sua data. A ISO/IEC 29184 acrescenta controles que viram campos: aviso sobre "retention period", "participation of PII principal" e "information about accessing the choices made for consent" [F: iso291842020, sumário, 5.3.11, 5.3.12 e 5.3.14], e, no consentimento, "separate consent to necessary and optional elements of PII", "frequency" e "timeliness" [F: iso291842020, sumário, 5.4.6–5.4.8]. A LGPD também obriga controlador e operador a manter "registro das operações de tratamento de dados pessoais que realizarem" [F: brasil2018lgpd, art. 37]; o registro de permissões é a face voltada ao titular desse inventário (ver `psg.audit.processing-records`).

### Revogação

O consentimento "pode ser revogado a qualquer momento mediante manifestação expressa do titular, por procedimento gratuito e facilitado, ratificados os tratamentos realizados sob amparo do consentimento anteriormente manifestado enquanto não houver requerimento de eliminação" [F: brasil2018lgpd, art. 8, §5]; a revogação é direito do titular [F: brasil2018lgpd, art. 18, IX], exercido "mediante requerimento expresso do titular ou de representante legalmente constituído" [F: brasil2018lgpd, art. 18, §3], e é hipótese de término do tratamento "resguardado o interesse público" [F: brasil2018lgpd, art. 15, III]. O GDPR exige que "it shall be as easy to withdraw as to give consent" e que a retirada não afete a licitude do tratamento anterior [F: eu2016gdpr, art. 7(3)]. A revogação não implica automaticamente eliminação: a eliminação dos dados tratados com consentimento é direito distinto (art. 18, VI), limitado pelas hipóteses de conservação do art. 16 (obrigação legal, pesquisa com anonimização, transferência lícita, uso exclusivo anonimizado) [F: brasil2018lgpd, arts. 16 e 18, VI]. O controlador deve ainda comunicar correção, eliminação, anonimização ou bloqueio aos agentes com quem compartilhou dados [F: brasil2018lgpd, art. 18, §6, redação da Lei 13.853/2019]. O Comitê dos Direitos da Criança pede que crianças e responsáveis possam "easily access stored data, rectify [...] and delete" e que se assegure "the right of children to withdraw their consent" [F: crc2021gc25, §72].

### Mudança de finalidade e de condições

Quando houver "mudanças da finalidade para o tratamento de dados pessoais não compatíveis com o consentimento original, o controlador deverá informar previamente o titular [...] podendo o titular revogar o consentimento" [F: brasil2018lgpd, art. 9, §2]; alteração de finalidade, forma e duração, identificação do controlador ou uso compartilhado exige informar "com destaque de forma específica do teor das alterações" [F: brasil2018lgpd, art. 8, §6]. Lê-se daí [I] que mudança compatível pede nova versão de aviso com informação destacada, e mudança incompatível pede nova permissão, sem reaproveitar a antiga. A ISO/IEC 29184 dedica a cláusula 5.5 a "change of conditions", com "renewing notice" e "renewing consent" [F: iso291842020, sumário, 5.5.1–5.5.3]. A COPPA exige consentimento parental também "to any material change in the collection, use, or disclosure practices to which the parent has previously consented" [F: cfr16312coppa, §312.5(a)(1)], e a FTC, ao emendar a regra em 2025, indicou que acrescentar um terceiro a uma categoria já divulgada tende a não ser mudança material, ao contrário de divulgar a operador com práticas diferentes das notificadas [F: ftc2025coppafinalrule, discussão do §312.4(d)]. O Comitê dos Direitos da Criança afirma que dados colhidos para fins definidos "should be protected and exclusive to those purposes" e que o reuso em outro contexto, inclusive escolar, deve ser "transparent, accountable and subject to the consent of the child, parent or caregiver, as appropriate" [F: crc2021gc25, §73].

### Transição à maioridade

"A menoridade cessa aos dezoito anos completos, quando a pessoa fica habilitada à prática de todos os atos da vida civil" [F: lei104062002, art. 5]; antes disso, entre 16 e 18 a pessoa é relativamente incapaz [F: lei104062002, art. 4, I]. A LGPD não regula o que acontece com o consentimento dado pelo responsável quando o titular completa 18 anos. O GDPR também não, mas o considerando 65 diz que o direito ao apagamento é relevante "where the data subject has given his or her consent as a child and is not fully aware of the risks" e pode ser exercido "notwithstanding the fact that he or she is no longer a child" [F: eu2016gdpr, considerando 65], e o art. 17(1)(f) lista como fundamento de apagamento os dados coletados em serviços oferecidos a crianças sob o art. 8(1) [F: eu2016gdpr, art. 17(1)(f)]. Recomendação deste documento, sem fonte normativa [I]: ao completar 18 anos, o detentor da permissão passa a ser o titular; o sistema notifica o titular, apresenta o aviso vigente em linguagem para adulto e oferece confirmar, ajustar ou revogar; o responsável perde o poder de revogar e o acesso de representante é encerrado; o histórico de quem consentiu e quando é preservado como prova. Variante mais cautelosa, inspirada no considerando 65 [I]: tratar a permissão herdada como "a confirmar" e suspender finalidades opcionais até a confirmação. A transição aos 12 anos (criança para adolescente, no ECA [F: lei8069eca, art. 2]) também merece evento próprio, porque o §1 do art. 14 fala só em crianças e a informação deve acompanhar as capacidades evolutivas [F: crc2021gc25, §19]; o que muda juridicamente é questão aberta (ver `psg.consent.parental-consent`).

## Requisitos e pressupostos

- Identidade estável do titular e do responsável e registro do vínculo entre eles, com data de nascimento confiável do titular para disparar as transições de idade (ver `iop.fund.identidade-e-contexto`) [I].
- Avisos versionados e imutáveis depois de publicados, para que o registro aponte para o texto exato exibido [I, a partir de brasil2018lgpd, art. 8, §2].
- Propagação: cada dado armazenado ou derivado deve ser rastreável à permissão que o cobre, inclusive em cópias compartilhadas, para cumprir o art. 18 §6 [F: brasil2018lgpd].
- Prazos de atendimento "previstos em regulamento" [F: brasil2018lgpd, art. 18, §5]; o regulamento não foi consultado (ver Lacunas).

## Vantagens e limitações

Um ciclo de vida explícito transforma obrigações difusas em eventos auditáveis e evita o erro de tratar revogação como eliminação ou mudança de aviso como novo consentimento. Limitações: o registro de permissões é ele próprio dado pessoal e deve ter retenção definida; a granularidade por finalidade multiplica pedidos e pode gerar fadiga, tensão que a ISO/IEC 29184 reconhece ao tratar de "frequency" do consentimento [F: iso291842020, sumário, 5.4.7]; e a transição à maioridade exige contatar um adulto que pode não usar mais o serviço, caso em que a saída conservadora é encerrar finalidades opcionais [I].

## Alternativas e comparações

| Evento | LGPD | GDPR | COPPA |
|---|---|---|---|
| Prova da permissão | Ônus do controlador [F: brasil2018lgpd, art. 8 §2] | Controlador demonstra [F: eu2016gdpr, art. 7(1)] | Não tratada em §312.5 |
| Revogação | Gratuita, facilitada, a qualquer tempo; passado ratificado [F: brasil2018lgpd, art. 8 §5] | Tão fácil quanto dar; passado lícito [F: eu2016gdpr, art. 7(3)] | Aviso de que o responsável pode revogar nos métodos por e-mail e SMS [F: cfr16312coppa, §312.5(b)(2)(viii)–(ix)] |
| Mudança de finalidade | Informar com destaque; nova permissão se incompatível [F: brasil2018lgpd, art. 8 §6, art. 9 §2] | Não tratada no art. 7 | Novo consentimento para mudança material [F: cfr16312coppa, §312.5(a)(1)] |
| Fim do tratamento | Eliminação, salvo art. 16 [F: brasil2018lgpd, arts. 15–16] | Apagamento ao retirar consentimento, salvo outra base [F: eu2016gdpr, art. 17(1)(b)] | Política escrita de retenção exigida pela emenda de 2025 [F: ftc2025coppafinalrule, §312.10] |
| Maioridade | Silente | Apagamento de dados dados quando criança [F: eu2016gdpr, art. 17(1)(f), considerando 65] | Silente no §312.5 |

## Exemplo técnico independente de domínio

```
registro_permissao {
  id, titular_id, detentor: {pessoa_id, papel: titular|mae|pai|responsavel_legal},
  vinculo_verificado: {metodo, data},
  base_legal, finalidade (uma), elementos_de_dados[], condicao_para_servico: bool,
  aviso: {versao, hash, formato_exibido}, manifestacao: {canal, forma, data_hora},
  estado: solicitada|ativa|a_confirmar|revogada|encerrada,
  eventos[]: {tipo: revisao|renovacao|revogacao|transicao_idade|termino|eliminacao, data, por}
}
ao_mudar_aviso(v_nova): se incompativel(finalidade, v_nova) -> criar nova solicitada; senão -> notificar destaque, versao=v_nova
ao_revogar(p): p.estado=revogada; parar tratamento; propagar(agentes_compartilhados); se pedido_eliminacao: aplicar art.16
ao_aniversario(titular, 18): para p em permissoes(titular): p.detentor=titular; p.estado=a_confirmar; encerrar acesso do representante
```

## Relações com outros conceitos

Depende de `psg.consent.parental-consent` (o que entra no registro) e de `psg.legal.lgpd-children`. Complementa `psg.consent.child-assent` (a retirada do assentimento é evento do ciclo), `psg.audit.processing-records` (o registro do art. 37, do qual este é a projeção por titular) e `iop.fund.identidade-e-contexto` (identidade e vínculo que sustentam detentor e titular). Relaciona-se com `psg.access.school-roles` (quem pode ver e operar permissões) e com `psg.legal.gdpr-k-and-coppa`.

## Lacunas e questões abertas

- A Kantara Consent Receipt Specification v1.1 não pôde ser aberta (páginas da wiki vazias para acesso automatizado; PDF não localizado); por isso não é citada, embora seja a referência usual para o formato de recibo. O Anexo B da ISO/IEC 29184 cumpre o papel aqui, mas só o sumário foi lido.
- O regulamento da ANPD sobre prazos de atendimento aos direitos do titular (art. 18 §5) não foi consultado.
- Não há fonte normativa brasileira sobre o que ocorre com o consentimento parental na maioridade; a recomendação acima é construção do documento.
- O "ECA Digital" pode trazer regras próprias de revogação e de contas de adolescentes; verificar em `psg.legal.eca-and-digital-eca`.
- Interação entre revogação do consentimento parental e tratamentos fundados em outras bases (por exemplo obrigação escolar) precisa de análise em `psg.legal.lgpd-children`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| lei104062002 | normativo | 2026-10-29 |
| lei8069eca | normativo | 2026-10-29 |
| eu2016gdpr | normativo (via reprodução gdpr-info.eu) | 2026-10-29 |
| cfr16312coppa | normativo (eCFR via LII) | 2026-10-29 |
| ftc2025coppafinalrule | normativo | 2026-10-29 |
| iso291842020 | normativo (escopo, sumário e 5.1–5.2.4 via amostra) | 2026-10-29 |
| crc2021gc25 | normativo (soft law) | 2026-10-29 |
| cns5102016 | normativo (via BVS/MS) | 2026-10-29 |
