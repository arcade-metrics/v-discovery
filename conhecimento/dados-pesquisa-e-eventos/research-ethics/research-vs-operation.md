---
id: dat.ethics.research-vs-operation
titulo: Pesquisa versus operação - base de pesquisa, base operacional e experimentos em serviço
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [cns4662012, cns5102016, cns6742022, conep2023oficiocircular12, lei148742024, brasil2018lgpd, anpd2023guiapesquisa, cioms2016guidelines, wma2024helsinki, kramer2014experimental, verma2014expression, meyer2015twocheers, kitto2019practical, slade2013ethical]
relacoes:
  - { tipo: depende-de, alvo: dat.ethics.cep-conep-system }
  - { tipo: complementa, alvo: dat.ethics.consent-and-assent-in-research }
  - { tipo: relacionado-a, alvo: lae.evalm.experimental-design }
  - { tipo: relacionado-a, alvo: lae.found.analytics-cycle }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
  - { tipo: relacionado-a, alvo: adp.eval.evaluation-protocols }
  - { tipo: complementa, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: psg.audit.ripd-dpia }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: dat.rd.data-management-plans }
  - { tipo: relacionado-a, alvo: dat.rd.fair-principles }
termos: [base operacional, base de pesquisa, uso secundário, tratamento posterior, presunção de compatibilidade, órgão de pesquisa, acervo, experimento de produto, teste A/B, experimento de campo, A/B illusion, pesquisa encoberta, retenção de informação, custodiante de dados, dado codificado, opt-out informado, consentimento amplo, desenvolvimento organizacional]
---

# Pesquisa versus operação: base de pesquisa, base operacional e experimentos em serviço

## Definição e terminologia

**Base operacional** é o conjunto de dados coletados para prestar um serviço (autenticar, registrar progresso, adaptar conteúdo, emitir relatórios ao professor). **Base de pesquisa** é o conjunto de dados tratados sob um protocolo de pesquisa aprovado, para produzir conhecimento generalizável. A distinção não está nos dados, mas na finalidade e no método: a Resolução CNS 466/2012 define pesquisa como "processo formal e sistemático que visa à produção, ao avanço do conhecimento e/ou à obtenção de respostas para problemas mediante emprego de método científico" [F: cns4662012, II.12], e inclui na pesquisa com seres humanos "o manejo de seus dados, informações ou materiais biológicos" [F: cns4662012, II.14]. **Uso secundário** (na LGPD, "tratamento posterior") é usar para pesquisa um dado coletado para outra finalidade. **Experimento de produto** ou **teste A/B** é a comparação controlada entre variantes de um serviço em usuários reais; o termo é do mercado, e Meyer observa que "A/B testing (as marketers and data scientists refer to it) or experimentation (as scientists in other fields call it)" designam a mesma prática [F: meyer2015twocheers, resumo].

O que não é: a separação não é só técnica (dois bancos de dados); é uma separação de finalidade, base legal, consentimento e governança, que a técnica materializa [I].

## Problema que resolve

Serviços digitais de aprendizagem geram registros finos de interação que são, ao mesmo tempo, insumo operacional e matéria-prima de pesquisa. Sem fronteira explícita, três falhas aparecem [I]: (1) dado coletado com consentimento de serviço é publicado como pesquisa sem protocolo; (2) um experimento que altera a experiência de crianças é tratado como ajuste de produto e escapa à revisão ética; (3) pesquisadores recebem a base operacional inteira, com identificadores, quando o protocolo exigia só um extrato. O caso de referência é o experimento de contágio emocional, que manipulou a exposição de "people (N = 689,003)" a expressões emocionais no feed de uma rede social e declarou que os termos de uso, aceitos por todos os usuários, constituíam "informed consent for this research" [F: kramer2014experimental, Materials and Methods]. A revista publicou uma "Editorial Expression of Concern": o comitê de ética da universidade dos coautores determinou que o projeto, conduzido "for internal purposes" pela empresa, não estava sob seu programa de proteção; a empresa não estava obrigada às regras federais de pesquisa, mas "it is nevertheless a matter of concern" que a coleta possa ter envolvido práticas "not fully consistent with the principles of obtaining informed consent and allowing participants to opt out" [F: verma2014expression]. A literatura de learning analytics trata o mesmo problema desde Slade e Prinsloo (2013) [F: slade2013ethical, metadados]; Kitto e Knight argumentam que os quadros éticos existentes "fail to inform those building LA solutions" em casos-limite [F: kitto2019practical, resumo].

## Fundamentos e funcionamento

### Quando a operação vira pesquisa (regime ético)

As resoluções do CNS dispensam de apreciação a atividade "com o intuito exclusivamente de educação, ensino, extensão ou treinamento, sem finalidade de pesquisa científica", mas, se surgir "a intenção de incorporação dos resultados dessas atividades em um projeto de pesquisa, dever-se-á, de forma obrigatória, apresentar o protocolo" [F: cns6742022, art. 26, VIII, b; cns5102016, art. 1, §2]. Também dispensam a pesquisa feita "exclusivamente com informações ou dados já disponibilizados de forma agregada, sem possibilidade de identificação individual" e a atividade que descreve "o processo produtivo ou administrativo para fins, exclusivamente, de desenvolvimento organizacional" [F: cns6742022, art. 26, V e XI]; a Conep esclareceu que este último inciso se refere a coletas "sem o registro de dados, opiniões ou percepções de pessoas" [F: conep2023oficiocircular12, item 3, XI]. Leitura deste documento [I]: análise operacional sobre dados individuais de alunos, feita para publicar ou generalizar, não cabe em nenhuma dispensa e exige protocolo; o gatilho é a intenção de produzir conhecimento, não o momento em que o dado foi coletado. A Lei 14.874/2024 vale para pesquisa com seres humanos "em todas as áreas do conhecimento", no que couber e conforme regulamento [F: lei148742024, art. 63].

### Uso secundário da base operacional

Pela Resolução 674/2022, pesquisa feita "exclusivamente a partir de acervo de dados pré-existentes, em meio físico ou eletrônico, que não sejam de acesso público" é do tipo A1, de tramitação expressa; pedir dispensa de consentimento para acervo "que tenha dados pessoais identificadores" é fator de modulação, assim como a anonimização irreversível [F: cns6742022, arts. 7 I, 10 I b e II a, 13]. Os dados de um protocolo "não poderão ser usados para outros fins além dos previstos" [F: cns4662012, IV.7], e a lei restringe dados da pesquisa à finalidade do projeto salvo autorização expressa no TCLE para pesquisas futuras [F: lei148742024, art. 45]. Internacionalmente, Helsinque pede consentimento para coleta, armazenamento e "foreseeable secondary use" de dados identificáveis, e admite pesquisa secundária sem consentimento, quando impossível ou impraticável, só após aprovação de comitê [F: wma2024helsinki, §32]. O CIOMS permite ao comitê dispensar o consentimento para dados coletados "for past research, clinical or other purposes" se a pesquisa for inviável sem a dispensa, tiver valor social importante e risco não maior que mínimo, e exige que o custodiante compartilhe "only anonymised or coded data", mantendo consigo a chave do código [F: cioms2016guidelines, diretriz 12].

### Base legal (LGPD)

A LGPD autoriza o tratamento "para a realização de estudos por órgão de pesquisa, garantida, sempre que possível, a anonimização" (dados comuns e sensíveis) e a conservação para esse fim [F: brasil2018lgpd, arts. 7 IV, 11 II c e 16 II]; mas órgão de pesquisa é só ente público ou pessoa jurídica "sem fins lucrativos" com pesquisa na missão institucional [F: brasil2018lgpd, art. 5, XVIII]. A ANPD orienta que agentes fora dessa definição, como empresas com fins lucrativos, podem pesquisar com amparo em outra base (consentimento, legítimo interesse, obrigação legal), e que para dados sensíveis o legítimo interesse não se aplica [F: anpd2023guiapesquisa, Agentes de tratamento não qualificados como órgãos de pesquisa]. A ANPD reconhece "presunção de compatibilidade quando o uso secundário dos dados se destina à finalidade de realização de estudos e pesquisas, especialmente por órgãos de pesquisa", sem "autorização irrestrita": é preciso pesar natureza dos dados, expectativas legítimas, princípios, segurança e "os padrões éticos aplicáveis" [F: anpd2023guiapesquisa, Regime jurídico]. Em estudos de saúde pública, a lei exige tratamento "exclusivamente dentro do órgão", em ambiente controlado e, sempre que possível, com anonimização ou pseudonimização [F: brasil2018lgpd, art. 13]; a ANPD sugere usar esses parâmetros em outras áreas [F: anpd2023guiapesquisa, Padrões éticos aplicáveis]. A Lei 14.874 regula a proteção de dados dos participantes, aplicando a LGPD "subsidiariamente" [F: lei148742024, art. 61]. Dados de crianças seguem o melhor interesse [F: brasil2018lgpd, art. 14] (ver `psg.legal.lgpd-children`).

### Experimentos A/B em escola

Pela tipificação da 674, estudos que "visam verificar o efeito de produto ou técnica em investigação, deliberadamente aplicado no participante em virtude da pesquisa, de forma prospectiva, com grupo-controle ou não" são tipo C, e C1 quando o objeto não é medicamento nem dispositivo de saúde [F: cns6742022, art. 9]; C1 tramita na modalidade colegiada [F: cns6742022, art. 13, §1]. Estudos que avaliam "exclusivamente, o processo de ensino-aprendizagem", relações de autoridade ou dependência e pesquisa encoberta são fatores de modulação [F: cns6742022, art. 10, I e, I f e II g]. Um teste A/B com alunos identificados, feito para gerar conhecimento, enquadra-se como C1 [I]; o TCLE deve informar a "possibilidade de inclusão em grupo controle ou experimental" [F: cns4662012, IV.3, a]. Se informar o objetivo enviesar o resultado, o caminho é a pesquisa encoberta justificada ao CEP, com consentimento posterior quando factível [F: cns5102016, art. 2, XV], ou a retenção parcial de informação com revelação antes da análise e direito de retirar os dados [F: cioms2016guidelines, diretriz 10, comentário].

Há uma posição contrária relevante. Meyer argumenta que a regulação de pesquisa admite dispensar consentimento quando ele é inviável e o risco é mínimo, e cunha a "A/B illusion": a tendência de ver o experimento que testa uma prática como mais suspeito do que implantar a prática sem teste, o que pode "overregulate research and underprotect a practice's end-users" [F: meyer2015twocheers, resumo]. É opinião da autora, formulada para o contexto norte-americano e para adultos [I].

## Alternativas e comparações

| Atividade | Exemplo | Regime ético (CNS) | Base legal típica |
|---|---|---|---|
| Operação | Adaptar a próxima atividade ao desempenho | Fora do sistema [I] | Execução do serviço ou outra base (ver `psg.legal.lgpd-children`) |
| Melhoria interna sem dado individual | Fluxo administrativo | Dispensa, art. 26 XI [F: cns6742022] | Não se aplica se não houver dado pessoal |
| Estatística agregada já disponibilizada | Relatório público por turma | Dispensa, art. 26 V [F: cns6742022] | Não se aplica se anonimizado |
| Uso secundário de base identificada | Modelar trajetórias para artigo | Protocolo, tipo A1 [F: cns6742022, art. 7] | Art. 7 IV / 11 II c se órgão de pesquisa; senão outra base [F: anpd2023guiapesquisa] |
| Experimento prospectivo | Teste A/B de duas sequências didáticas para publicar | Protocolo, tipo C1, colegiada [F: cns6742022, arts. 9 e 13] | Idem, mais TCLE e assentimento [F: cns4662012, IV.6] |

## Vantagens e limitações

Separar as bases permite pesquisar sem expor a operação e operar sem esperar pareceres. Limitações: a fronteira depende de intenção declarada, que pode mudar no meio do caminho e exige emenda ou novo protocolo [I]; experimentos contínuos de melhoria, comuns em produtos digitais, não têm categoria própria nas normas brasileiras, e o CIOMS deixou fora de escopo modelos que integram pesquisa e serviço [F: cioms2016guidelines, Preface]; e a dispensa de revisão para fins internos, como no caso de 2014, pode ser formalmente correta e ainda assim eticamente questionada [F: verma2014expression].

## Exemplo técnico independente de domínio

Recomendação deste documento, inspirada no modelo de custodiante do CIOMS e na pseudonimização da LGPD [F: cioms2016guidelines, diretriz 12; brasil2018lgpd, art. 13 §4]:

```
[base operacional] --(custodiante: aplica protocolo_id, filtro de consentimento,
                      pseudonimiza, minimiza campos, registra extração)--> [extrato de pesquisa]
  chave de pseudônimo: só no custodiante          extrato: só campos listados no protocolo
  evento de retirada de consentimento -> remove participante dos extratos futuros
  publicação: só agregados ou dados anonimizados [F: brasil2018lgpd, art. 13 §1]

experimento(variantes, populacao):
    se finalidade inclui conhecimento generalizável: exigir parecer(C1) antes de alocar
    alocar por aleatorização registrada; logar variante por pseudônimo
    mudança de variante, métrica ou população -> emenda
```

## Relações com outros conceitos

Depende de `dat.ethics.cep-conep-system` e complementa `dat.ethics.consent-and-assent-in-research`. O desenho e a validade do experimento estão em `lae.evalm.experimental-design` e `lae.dq.bias-and-validity`; o ciclo de dados em `lae.found.analytics-cycle`; avaliações com usuários em `adp.eval.evaluation-protocols`. A pseudonimização, a minimização e o RIPD estão em `psg.deid.anonymization-and-pseudonymization`, `psg.access.minimization-and-privacy-by-design` e `psg.audit.ripd-dpia`. Guarda e compartilhamento do extrato estão em `dat.rd.data-management-plans` e `dat.rd.fair-principles`.

## Lacunas e questões abertas

- Não há norma brasileira específica para experimentos contínuos de produto em ambiente educacional; o enquadramento como C1 é interpretação deste documento.
- O Anexo II da Resolução 674 (efeito de "processo de ensino-aprendizagem" na tramitação) não estava legível na cópia consultada.
- Kitto e Knight (2019) e Meyer (2015) foram lidos só no resumo; Slade e Prinsloo (2013) só nos metadados (repositório bloqueado ao acesso automatizado).
- Não se verificou se uma empresa com fins lucrativos que pesquisa com dados de serviço está, na prática, sujeita à fiscalização do Sistema Nacional pela Lei 14.874.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| cns4662012 | normativo (cópia BVS/MS) | 2026-10-30 |
| cns5102016 | normativo (cópia BVS/MS) | 2026-10-30 |
| cns6742022 | normativo (impressão do DOU) | 2026-10-30 |
| conep2023oficiocircular12 | normativo (ofício da Conep) | 2026-10-30 |
| lei148742024 | normativo | 2026-10-30 |
| brasil2018lgpd | normativo | 2026-10-30 |
| anpd2023guiapesquisa | tecnico | 2026-10-30 |
| cioms2016guidelines | normativo (soft law) | 2026-10-30 |
| wma2024helsinki | normativo (soft law) | 2026-10-30 |
| kramer2014experimental | academico | 2026-10-30 |
| verma2014expression | academico (nota editorial) | 2026-10-30 |
| meyer2015twocheers | academico (resumo) | 2026-10-30 |
| kitto2019practical | academico (resumo) | 2026-10-30 |
| slade2013ethical | academico [metadados] | 2026-10-30 |
