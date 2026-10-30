---
id: acs.found.disability-models
titulo: Modelos de deficiência
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [decreto69492009, lei131462015, crpd2016gc4, crpd2018gc6, who2002icfguide, who2001icf, who2011worldreport, oliver2013social, shakespeare2001social, retief2018models, idrc2026whatisinclusive]
relacoes:
  - { tipo: complementa, alvo: acs.found.barriers-and-reasonable-accommodation }
  - { tipo: complementa, alvo: acs.found.universal-design }
  - { tipo: relacionado-a, alvo: iop.health.cif }
  - { tipo: relacionado-a, alvo: acs.br.lbi }
  - { tipo: relacionado-a, alvo: acs.asmt.barriers-and-support-needs }
  - { tipo: relacionado-a, alvo: acs.part.inclusive-and-participatory-design }
termos: [modelo de deficiência, modelo médico, modelo social, modelo biopsicossocial, modelo de direitos humanos, impedimento, deficiência, funcionalidade, capacidade, desempenho, fatores ambientais, fatores pessoais, igualdade inclusiva, avaliação biopsicossocial, deficiência como descompasso]
---

# Modelos de deficiência

## Definição e terminologia

Um modelo de deficiência é uma forma de responder onde a deficiência está (no corpo, no ambiente ou na interação) e, por consequência, quem deve mudar e quem decide. A revisão de Retief e Letšosa descreve nove modelos "dominantes" (moral ou religioso, médico, social, identitário, de direitos humanos, cultural, de caridade, econômico e de limites) por uma abordagem tipológica [F: retief2018models, resumo e conclusão]. Para tecnologia educacional importam quatro: médico, social, biopsicossocial e de direitos humanos.

- **Modelo médico (ou individual)**: a OMS o descreve como aquele que vê a deficiência como "a feature of the person, directly caused by disease, trauma or other health condition", que pede tratamento individual para "'correct' the problem with the individual" [F: who2002icfguide, p. 8].
- **Modelo social**: vê a deficiência como "a socially-created problem and not at all an attribute of an individual", que exige resposta política porque o problema vem de um ambiente "unaccommodating" [F: who2002icfguide, p. 9]. Na formulação britânica da UPIAS, retomada por Retief e Letšosa, impedimento é a condição do corpo e deficiência é "the disadvantage or restriction of activity caused by a contemporary social organisation" [F: retief2018models, seção do modelo social]. A revisão de trinta anos do próprio Oliver foi confirmada só por metadados [F: oliver2013social, metadados].
- **Modelo biopsicossocial**: síntese proposta pela OMS como base da CIF, "an integration of medical and social" [F: who2002icfguide, p. 9].
- **Modelo de direitos humanos**: o Comitê da CDPD afirma que ele "recognizes that disability is a social construct and impairments must not be taken as a legitimate ground for the denial or restriction of human rights", e que a deficiência é "one of several layers of identity" [F: crpd2018gc6, §9].

O que não é: modelo de deficiência não é instrumento de avaliação nem codificação clínica. A CIF como sistema de códigos e qualificadores está em `iop.health.cif`; aqui ela entra só como modelo conceitual.

## Problema que resolve

Sem um modelo explícito, sistemas e equipes adotam por padrão o modelo médico: a pessoa é descrita pelo diagnóstico, e a resposta é corrigir a pessoa. O Comitê da CDPD registra que leis e políticas ainda tratam a deficiência por modelos "charity and/or medical", incompatíveis com a Convenção [F: crpd2018gc6, §2], e que sob o modelo médico as pessoas são "'reduced' to their impairments" [F: crpd2018gc6, §8]. Escolher o modelo é escolher o que se mede e o que se muda; é por isso que a pergunta "como avaliar barreiras e suporte sem reduzir a pessoa a um diagnóstico" começa aqui [I].

## Fundamentos e funcionamento

### A definição jurídica é interacional

A Convenção, promulgada no Brasil pelo Decreto 6.949/2009 após aprovação pelo rito do §3 do art. 5 da Constituição (equivalência a emenda constitucional) [F: decreto69492009, preâmbulo do decreto], reconhece "que a deficiência é um conceito em evolução e que a deficiência resulta da interação entre pessoas com deficiência e as barreiras devidas às atitudes e ao ambiente" [F: decreto69492009, Convenção, preâmbulo, e]. Pessoas com deficiência são as que têm "impedimentos de longo prazo de natureza física, mental, intelectual ou sensorial" que, em interação com barreiras, podem obstruir a participação plena [F: decreto69492009, Convenção, art. 1]. A LBI repete a estrutura: impedimento de longo prazo "o qual, em interação com uma ou mais barreiras, pode obstruir sua participação plena e efetiva na sociedade em igualdade de condições com as demais pessoas" [F: lei131462015, art. 2, caput]. Impedimento sozinho não é deficiência; a deficiência é o resultado da interação [I].

### A CIF como modelo biopsicossocial

A OMS argumenta que, sozinhos, nem o modelo médico nem o social são adequados, "although both are partially valid": a deficiência é "always an interaction between features of the person and features of the overall context" [F: who2002icfguide, p. 9]. Na CIF, funcionalidade abrange funções do corpo, atividades e participação, e deficiência é termo guarda-chuva para impedimentos, limitações de atividade e restrições de participação; fatores ambientais interagem com todos esses componentes [F: who2002icfguide, p. 2]. O Relatório Mundial sobre a Deficiência adotou a CIF como quadro conceitual e a chama de "workable compromise between medical and social models" [F: who2011worldreport, cap. 1, p. 4]; os fatores ambientais "can be either facilitators or barriers" e incluem produtos e tecnologia, ambiente, apoio e relacionamentos, atitudes, e serviços, sistemas e políticas [F: who2011worldreport, cap. 1, caixa 1.1, p. 5].

Três ideias da CIF servem diretamente à avaliação sem rótulo:

1. **Universalidade.** A CIF "'mainstreams' the experience of disability and recognises it as a universal human experience" e, ao deslocar o foco "from cause to impact", põe todas as condições de saúde em pé de igualdade [F: who2002icfguide, p. 3]; a deficiência é "a matter of more or less, not yes or no" [F: who2011worldreport, caixa 1.1, p. 5].
2. **Capacidade x desempenho.** Capacidade é o que a pessoa faz em ambiente padronizado; desempenho, o que faz no ambiente habitual [F: who2002icfguide, p. 2]. Se a capacidade supera o desempenho, "some aspect of the environment is a barrier"; se fica abaixo, o ambiente "has facilitated performance" [F: who2002icfguide, p. 12].
3. **Fatores pessoais** são reconhecidos, mas ainda não classificados [F: who2011worldreport, caixa 1.1, p. 5]. A OMS endossou a CIF na resolução WHA 54.21, de 2001, e a versão para crianças e jovens (CIF-CJ) foi reincorporada à CIF [F: who2001icf].

### O modelo de direitos humanos

O Comitê da CDPD vai além do modelo social e do biopsicossocial: trata a deficiência como construção social e o impedimento como parte da diversidade humana, e liga o modelo à **igualdade inclusiva**, com quatro dimensões: redistributiva, de reconhecimento, participativa e de acomodação, esta última "to make space for difference as a matter of human dignity" [F: crpd2018gc6, §§9 e 11]. No Comentário Geral nº 4, o Comitê aponta como obstáculo à educação inclusiva "the failure to understand or implement the human rights model of disability, in which barriers within the community and society, rather than personal impairments, exclude persons with disabilities" [F: crpd2016gc4, §4(a)]. Para Degener, citada por Retief e Letšosa, o modelo de direitos humanos difere do social por oferecer "a theoretical framework for disability policy" e por tratar também de dor, identidade, prevenção e pobreza [F: retief2018models, seção do modelo de direitos humanos].

### Desenho como lugar da deficiência

O Inclusive Design Research Centre reformula a deficiência no contexto de projeto como "a mismatch between the needs of the individual and the design of the product, system or service", de modo que ela "can be experienced by anyone excluded by the design" [F: idrc2026whatisinclusive]. É a leitura que conecta este documento a `acs.found.universal-design` [I].

## Vantagens e limitações

| Modelo | O que ajuda a ver | Crítica principal |
|---|---|---|
| Médico | Necessidades de saúde reais; tratamento e reabilitação | Reduz a pessoa ao impedimento e legitima exclusão [F: crpd2018gc6, §8] |
| Social | Barreiras do ambiente; resposta política | Ignora a realidade do impedimento e a dualidade impedimento/deficiência é contestada [F: shakespeare2001social, resumo; retief2018models] |
| Biopsicossocial (CIF) | Interação, barreiras e facilitadores, capacidade x desempenho | Fatores pessoais não classificados; codificação exige profissional (ver `iop.health.cif`) [F: who2011worldreport, caixa 1.1] |
| Direitos humanos | Obrigações, não discriminação, participação da pessoa | Mais normativo que descritivo; não dá, sozinho, instrumento de medida [I] |

Shakespeare e Watson argumentam que é hora de ir além do modelo social britânico, com três críticas centrais: o impedimento, o dualismo impedimento/deficiência e a identidade; propõem "an embodied ontology" como ponto de partida [F: shakespeare2001social, resumo]. Na síntese de Retief e Letšosa, os críticos lembram que "We are not just disabled people, we are also people with impairments" [F: retief2018models, seção do modelo social]. O Relatório Mundial resume que a deficiência "should be viewed neither as purely medical nor as purely social" [F: who2011worldreport, cap. 1, p. 4].

## Requisitos e pressupostos

- A LBI torna a avaliação da deficiência, "quando necessária", biopsicossocial, por equipe multiprofissional e interdisciplinar, considerando impedimentos, fatores socioambientais, psicológicos e pessoais, limitação no desempenho de atividades e restrição de participação [F: lei131462015, art. 2, §1, I a IV]; o Poder Executivo "criará instrumentos para avaliação da deficiência" [F: lei131462015, art. 2, §2]. A situação de regulamentação desses instrumentos não foi verificada nesta sessão.
- O Comitê afirma que a adaptação razoável na educação "may not be conditional on a medical diagnosis of impairment and should be based instead on the evaluation of social barriers to education" [F: crpd2016gc4, §29]. Daí a resposta conceitual à pergunta do brief: avaliar o descompasso entre pessoa e ambiente (barreiras, facilitadores, desempenho em contexto) e as preferências da pessoa, e não a categoria diagnóstica [I].

## Exemplo técnico independente de domínio

```
registro_funcionalidade(pessoa, contexto):
    # o diagnóstico, se existir, é atributo opcional e restrito; nunca chave de decisão
    atividade = "ler instrução de tarefa"
    desempenho = observar(pessoa, atividade, ambiente=habitual)
    capacidade = observar(pessoa, atividade, ambiente=padronizado_sem_apoio)
    fatores = [ {fator: "texto só visual", efeito: barreira},
                {fator: "leitura em voz alta disponível", efeito: facilitador} ]
    se capacidade > desempenho: procurar barreira no ambiente
    se capacidade < desempenho: registrar facilitador que deve ser mantido
    preferencias = perguntar(pessoa)          # voz da pessoa, não só do avaliador
```

## Relações com outros conceitos

Complementa `acs.found.barriers-and-reasonable-accommodation` (o que fazer com a barreira identificada) e `acs.found.universal-design` (evitar a barreira no projeto). Relaciona-se com `iop.health.cif` (a CIF como codificação), `acs.br.lbi` (definições legais), `acs.asmt.barriers-and-support-needs` (instrumentos) e `acs.part.inclusive-and-participatory-design` (participação da pessoa no desenho).

## Lacunas e questões abertas

- O texto integral de Oliver (2013) e de Shakespeare e Watson (2001) não foi acessado; as críticas ao modelo social vêm do resumo e da síntese de Retief e Letšosa.
- O Comentário Geral nº 6 foi lido na versão avançada não editada; o nº 4, em reprodução não oficial. A numeração de parágrafos deve ser conferida nas versões oficiais.
- O manual oficial completo da CIF (2001) não foi consultado; usou-se o guia introdutório da OMS (2002).
- Instrumento federal de avaliação biopsicossocial previsto no art. 2, §2, da LBI: estado de regulamentação não verificado (fica para `acs.br.lbi`).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| decreto69492009 | normativo | 2026-10-30 |
| lei131462015 | normativo | 2026-10-30 |
| crpd2016gc4 | normativo (soft law; reprodução não oficial) | 2026-10-30 |
| crpd2018gc6 | normativo (soft law; versão avançada) | 2026-10-30 |
| who2002icfguide | tecnico | 2026-10-30 |
| who2001icf | normativo | 2026-10-30 |
| who2011worldreport | tecnico | 2026-10-30 |
| oliver2013social | academico [metadados] | 2026-10-30 |
| shakespeare2001social | academico [resumo] | 2026-10-30 |
| retief2018models | academico | 2026-10-30 |
| idrc2026whatisinclusive | tecnico | 2026-10-30 |
