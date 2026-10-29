---
id: psg.deid.reidentification-risk
titulo: Risco de reidentificação
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nist2023sp800188, anpd2023anonimizacaoprocesso, anpd2023anonimizacaojuridica, brasil2018lgpd, sweeney2000demographics, sweeney2002kanonymity, narayanan2008robust, rocher2019estimating, daries2014privacy, waldo2014anonymity, datashop2026terms, nist2025sp800226, iso27559v2022]
relacoes:
  - { tipo: parte-de, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: complementa, alvo: psg.deid.k-anonymity-and-extensions }
  - { tipo: complementa, alvo: psg.deid.differential-privacy }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: adp.eval.heterogeneous-populations }
  - { tipo: relacionado-a, alvo: lae.psy.fairness-in-measurement }
  - { tipo: relacionado-a, alvo: iop.br.lgpd }
termos: [reidentificação, risco de reidentificação, ataque de ligação, dados auxiliares, unicidade, cenário do promotor, cenário do jornalista, singling out, linkability, inferência, release-and-forget, acordo de uso de dados, enclave, Five Safes, Disclosure Review Board, estudo de reidentificação, taxa condicional de reidentificação, esparsidade, dados de alta dimensionalidade, dados ligados]
---

# Risco de reidentificação

## Definição e terminologia

**Reidentificação** é o "process by which information is attributed to de-identified data in order to identify the individual to whom the de-identified data relate" (definição da OCDE adotada pelo NIST); **risco de reidentificação** é a probabilidade de que um terceiro reidentifique titulares num dataset desidentificado, tipicamente função da probabilidade de ocorrência e dos impactos adversos [F: nist2023sp800188, §2.2]. A ANPD chama de risco de reidentificação "o risco de identificação incidente sobre dados anonimizados" e, seguindo a tradição de segurança computacional, o expressa como ataques de um "atacante" hipotético com certas habilidades, conhecimento ou acesso, figura que não se confunde com criminoso: pesquisadores que testam a robustez de bases públicas são o exemplo [F: anpd2023anonimizacaojuridica, §4.3].

Três formas de risco, na terminologia que a ANPD importa da literatura europeia: **distinção** (*singling out*: isolar os registros que destacam um indivíduo), **ligação** (*linkability*: conectar pelo menos dois registros do mesmo indivíduo ou grupo) e **inferência** (deduzir, com probabilidade significativa, o valor de um atributo a partir de outros) [F: anpd2023anonimizacaojuridica, §4.3]. O NIST distingue, na tradição de controle de divulgação estatística, divulgação de identidade, de atributo e inferencial, e observa que as duas primeiras são casos de alta confiança da terceira [F: nist2023sp800188, §2.2].

Probabilidades que o NIST propõe nomear de forma autodescritiva: **KIRP** (*known inclusion re-identification probability*, achar o registro de alguém que se sabe estar na amostra, o antigo "risco do promotor"), **UIRP** (*unknown inclusion*, sem saber se a pessoa está na base, o antigo "risco do jornalista"), **RMP** (*record-matching probability*, para alguém sorteado da população) e **IP** (*inclusion probability*, inferir a mera presença) [F: nist2023sp800188, §3.2.1]. A ANPD mantém os nomes **cenário do promotor** (o atacante sabe que o titular está no conjunto) e **cenário do jornalista** (o atacante quer reidentificar qualquer titular, sem informação a priori sobre quem está presente) [F: anpd2023anonimizacaoprocesso, §2.3, notas 3 e 4].

## Problema que resolve

A LGPD condiciona a saída do regime de dados pessoais à impossibilidade de reversão "com esforços razoáveis", a ser aferida por fatores objetivos como custo, tempo e tecnologia disponível [F: brasil2018lgpd, art. 12, caput e §1]. Medir o risco de reidentificação é, portanto, a operação que decide se um dataset é anonimizado para fins legais e, para pesquisa, se pode ser compartilhado e em que modelo. A ANPD exige que o risco mensurado assuma "a forma de probabilidade" e seja comparado com um limite aceitável fixado antes [F: anpd2023anonimizacaoprocesso, §2.3].

## Fundamentos e funcionamento

**Estudos clássicos.** Sweeney (2000), com dados do Censo dos EUA de 1990, estimou que 87% da população (216 de 248 milhões) era provavelmente única por {CEP de 5 dígitos, sexo, data de nascimento}, 53% por {município, sexo, data de nascimento} e 18% por {condado, sexo, data de nascimento}, concluindo que "few characteristics are needed to uniquely identify a person" [F: sweeney2000demographics, resumo]; a ligação da lista de eleitores com dados hospitalares identificou o governador de Massachusetts [F: sweeney2002kanonymity, §1]. Narayanan e Shmatikov (2008) atacaram o dataset do Netflix Prize (100.480.507 avaliações de 480.189 assinantes) e mostraram que microdados de alta dimensionalidade e esparsos ("a pair of random records are located far apart") são reidentificáveis com pouca informação auxiliar: com 8 avaliações (2 delas podendo estar erradas) e datas com erro de até 14 dias, 99% dos registros são identificados unicamente; com 2 avaliações e datas com erro de 3 dias, 68%; sem datas, 84% dos assinantes são únicos se o atacante conhece 6 de 8 filmes fora dos 500 mais avaliados; e, com avaliações públicas do IMDb, identificaram registros de usuários reais [F: narayanan2008robust, §1 e §5]. Rocher, Hendrickx e de Montjoye (2019) propuseram um modelo generativo baseado em cópulas gaussianas que estima a probabilidade de uma reidentificação específica estar correta mesmo em datasets muito incompletos (treinado com 1% da população, AUC entre 0,84 e 0,97 em 210 populações); estimam que 99,98% dos americanos seriam corretamente reidentificados em qualquer dataset com 15 atributos demográficos; mostram que {CEP, data de nascimento, sexo, número de filhos} identificaria 79,4% da população de Massachusetts com confiança acima de 0,80; e concluem que a amostragem não dá negabilidade plausível e que isso "seriously challenge[s] the technical and legal adequacy of the de-identification release-and-forget model" [F: rocher2019estimating, resumo, resultados e discussão].

**Fatores que elevam o risco.** O NIST aponta: membros de populações vulneráveis, cuja característica os faz "stand out in the dataset"; residentes de áreas de população pequena; indivíduos com múltiplos traços em localização restrita (o exemplo de uma veterana grávida e desempregada no condado de Baltimore) [F: nist2023sp800188, §3.2.1]. Dados ligados: pseudônimos permitem ligar registros ao longo do tempo; identificadores familiares ligam pais e filhos; "given a long sequence of tests, each individual in a dataset would have a unique constellation of heart rate measurements"; e localização ao longo do tempo cria padrões que permitem distinguir um indivíduo "even with a small number of recorded locations per individual" [F: nist2023sp800188, §4.3.10]. Alta dimensionalidade: num levantamento anônimo que liga respostas de pais e filhos, um filho pode achar as respostas dos pais procurando as próprias e seguindo o vínculo [F: nist2023sp800188, §4.3.9, nota 34]. Composição: releases múltiplas, *snapshots* periódicos, novas tecnologias ou ordens judiciais podem combinar-se de forma imprevisível, e só a privacidade diferencial permite somar a perda [F: nist2023sp800188, §4.3.11]. O risco cresce com o tempo, "as vulnerabilities are likely to increase" com técnicas melhores e mais informação contextual; o NIST recomenda assumir que bases públicas "could be subjected to sustained, worldwide re-identification attempts", sem no entanto atribuir ao intruso capacidades oniscientes, e que o grau de sensibilidade aparente do dataset não reduz o risco, pois reidentificá-lo pode ser passo para reidentificar outro [F: nist2023sp800188, §3.2.1].

**Modelos de compartilhamento e controles.** O NIST descreve um espectro: *release-and-forget* (publicação na internet, difícil de revogar); acordo de uso de dados (DUA, com cláusulas que proíbem tentativa de reidentificação, ligação e redistribuição, negociado com pesquisadores qualificados ou por *click-through*); dados sintéticos com validação; e enclave (dados ficam segregados, consultas vetadas, resultados devolvidos) [F: nist2023sp800188, §3.4]. Recomenda metodologia repetível como os Five Safes (projetos, pessoas, dados, ambiente e saídas seguros) e um Disclosure Review Board [F: nist2023sp800188, §3.5 e §3.6]. Se o dano potencial é grande, as opções são elevar a desidentificação, aceitando menor acurácia, ou restringir o acesso a pesquisadores qualificados em enclave [F: nist2023sp800188, §3.2.1]. Liberar só uma amostra reduz a probabilidade de reidentificação porque o intruso não sabe se o alvo está presente, mas reduz poder estatístico [F: nist2023sp800188, §3.4]; Rocher et al. argumentam que esse efeito é fraco [F: rocher2019estimating, discussão]. Um exemplo de controle contratual em dados educacionais: os termos de uso do DataShop exigem que os dados sejam para pesquisa, não comercial, e que o usuário "will not make any attempts to de-anonymize the data" nem crie dataset com informação que identifique estudantes [F: datashop2026terms].

## Requisitos e pressupostos

- Conhecimento das bases auxiliares existentes e prováveis, públicas e privadas, inclusive as vendidas por *data brokers*, sem o que o cálculo de probabilidades vira "a fundamentally meaningless exercise", crítica que o NIST registra e responde exigindo especialistas [F: nist2023sp800188, §3.2.1].
- Limite de risco fixado antes e majorado quando a base é pública ou compartilhada [F: anpd2023anonimizacaoprocesso, §2.3].
- Registro de todas as releases anteriores, pois cada nova release deve ser avaliada à luz das anteriores [F: nist2023sp800188, §3.4; sweeney2002kanonymity, §4].
- Monitoramento pós-release e reavaliação periódica [F: nist2023sp800188, §4.3.11 e §4.3.13].

## Vantagens e limitações

Medir risco permite decisões proporcionais (publicar, licenciar, enclave) e documentáveis, como exigem a ANPD e o art. 12 §1. Limitações: o risco verdadeiro é desconhecido e cresce com o tempo [F: nist2023sp800188, §3.2.1]; estudos de reidentificação testam vulnerabilidades genéricas, mas "do not determine whether someone with intimate knowledge of a specific respondent can find that respondent", e a única proteção para um indivíduo específico de alto risco é perturbação ou remoção [F: nist2023sp800188, §4.6.3]; e baixa unicidade populacional não protege os indivíduos que são únicos [F: rocher2019estimating, discussão].

## Alternativas e comparações

| Modelo de compartilhamento | Risco de reidentificação | Controle principal | Custo em utilidade e acesso | Fonte |
|---|---|---|---|---|
| Release-and-forget | Máximo; irrevogável; sujeito a ataques mundiais sustentados | Só a desidentificação | Baixo custo de acesso; alto custo em utilidade para atingir risco aceitável | [F: nist2023sp800188, §3.4 e §3.2.1] |
| Acordo de uso (DUA, click-through) | Reduzido por proibição contratual de reidentificar e redistribuir | Contrato e qualificação do pesquisador | Médio | [F: nist2023sp800188, §3.4; datashop2026terms] |
| Dados sintéticos com validação | Baixo nos dados; validação no original | Modelo gerador (eventualmente com DP) | Resultados aproximados; validação lenta | [F: nist2023sp800188, §3.4 e §4.4] |
| Enclave ou interface de consulta | Dados não saem; risco nas saídas | Vetagem de consultas, DP nas respostas, log | Alto custo operacional | [F: nist2023sp800188, §3.4 e §4.5] |

## Métricas e métodos de avaliação

Unicidade na amostra e na população; tamanho das classes de equivalência e risco por classe (1/k), com risco médio ponderado do conjunto, majorado por fator contextual quando a base é pública ou compartilhada [F: anpd2023anonimizacaoprocesso, §2.3]; KIRP, UIRP, RMP, IP [F: nist2023sp800188, §3.2.1]; **taxa condicional de reidentificação** em estudos com intruso motivado (ligações confirmadas divididas por ligações suspeitas), que, acima do limiar acordado para qualquer estrato, indica que o dado não deve sair de ambiente controlado [F: nist2023sp800188, §4.6.3]; probabilidade individual de reidentificação correta estimada por modelo generativo, com AUC e taxa de falsa descoberta como qualidade do estimador [F: rocher2019estimating, resumo]; e, para mecanismos com ruído, epsilon acumulado (`psg.deid.differential-privacy`). A ISO/IEC 27559:2022 oferece um framework de avaliação de identificabilidade e governança do ciclo de vida do dado desidentificado [F: iso27559v2022, metadados].

## Exemplo técnico independente de domínio

```
entrada: dataset de interação D (titular pseudonimizado, eventos com data e hora, atributos demográficos,
         atributo sensível S), finalidade F, candidatos a modelo de compartilhamento M
1. quase-identificadores explícitos QI := {idade ou ano de nascimento, sexo, escola ou região, turma}
2. quase-identificadores implícitos: a série temporal de cada titular (datas, horários, sequência de
   itens) é tratada como QI de alta dimensionalidade; verificar unicidade: fração de titulares cuja
   sequência de (dia, item) é única dentro de D e dentro de qualquer release anterior
3. populações pequenas: para cada classe de equivalência c de QI, se |c| < k ou se o valor de S em c é
   homogêneo, marcar c como de alto risco (ex.: 1 aluno com uma característica rara em uma turma)
4. medir: risco_promotor := max sobre c de 1/|c|; risco_jornalista := média ponderada de 1/|c|;
   unicidade_sequencial := resultado do passo 2; majorar se M = público
5. decidir: se risco > RRA para M = release-and-forget, então
      ou elevar a desidentificação (generalizar datas para semana, truncar sequências, suprimir c)
      e repetir 2-4, aceitando perda de utilidade documentada,
      ou mudar M para DUA ou enclave, e publicar só estatísticas com DP (unidade = titular)
6. registrar RRA, RRM, bases auxiliares consideradas, releases anteriores, decisão e data; agendar revisão
```

## Relações com outros conceitos

Parte de `psg.deid.anonymization-and-pseudonymization`: é o teste que decide se o processo de anonimização atingiu o art. 12. Complementa `psg.deid.k-anonymity-and-extensions` (as classes de equivalência são a métrica base) e `psg.deid.differential-privacy` (o orçamento epsilon é a forma de limitar risco em respostas). Complementa `psg.audit.ripd-dpia`: a medição de risco e a escolha do modelo de compartilhamento são conteúdo do relatório de impacto. Relaciona-se com `psg.legal.lgpd-children` (melhor interesse e dados de menores elevam o dano potencial), `psg.access.minimization-and-privacy-by-design` (coletar menos atributos reduz unicidade), `adp.eval.heterogeneous-populations` e `lae.psy.fairness-in-measurement` (subgrupos pequenos e raros são os mais reidentificáveis e os mais afetados por supressão) e `iop.br.lgpd`.

## Lacunas e questões abertas

- Resposta à pergunta do brief, sob a forma de hipótese fundamentada [H, apoiada nas fontes acima]: para dataset de interação de menores, não há nível de anonimização de microdados que torne seguro o modelo *release-and-forget*, porque a série temporal é quase-identificador de alta dimensionalidade (Narayanan e Shmatikov; NIST §4.3.10) e turmas pequenas com característica rara produzem classes de equivalência unitárias (NIST §3.2.1). O compartilhamento defensável combina acordo de uso ou enclave, pseudonimização com chave guardada fora, k-anonimato com l-diversidade nos atributos demográficos e sensíveis (incluindo deficiência) e divulgação pública apenas de estatísticas com privacidade diferencial em nível de usuário. Faltam fonte normativa brasileira e estudos empíricos com dados educacionais de menores que validem valores concretos de k ou epsilon.
- O estudo de Daries et al. (2014), que mediu o custo em utilidade do k-anonimato em dados de MOOC, não foi lido no original (ver `psg.deid.k-anonymity-and-extensions`).
- Trabalhos de desidentificação em repositórios educacionais (por exemplo a documentação do PSLC DataShop sobre identificadores anônimos) não foram localizados além dos termos de uso; a prática concreta de pseudonimização desses repositórios fica sem fonte.
- O guia da ANPD sobre anonimização, com apêndice de técnicas de mensuração de risco, não foi publicado em versão final até a data de consulta.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nist2023sp800188 | tecnico | 2026-10-29 |
| anpd2023anonimizacaoprocesso | tecnico | 2026-10-29 |
| anpd2023anonimizacaojuridica | tecnico | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
| sweeney2000demographics | academico (working paper) | 2026-10-29 |
| sweeney2002kanonymity | academico | 2026-10-29 |
| narayanan2008robust | academico (pré-print arXiv) | 2026-10-29 |
| rocher2019estimating | academico | 2026-10-29 |
| daries2014privacy | academico (texto integral não acessado) | 2026-10-29 |
| waldo2014anonymity | secundario | 2026-10-29 |
| datashop2026terms | fornecedor | 2026-10-29 |
| nist2025sp800226 | tecnico | 2026-10-29 |
| iso27559v2022 | normativo (somente metadados) | 2026-10-29 |
