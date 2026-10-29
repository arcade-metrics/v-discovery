---
id: psg.consent.parental-consent
titulo: Consentimento parental
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, lei80691990, lei104062002, anpd2023voto12, decreto997101990, crc2021gc25, eu2016gdpr, cfr16312coppa, ftc2025coppafinalrule, iso291842020]
relacoes:
  - { tipo: depende-de, alvo: psg.legal.lgpd-children }
  - { tipo: complementa, alvo: psg.consent.child-assent }
  - { tipo: complementa, alvo: psg.consent.permission-lifecycle }
  - { tipo: relacionado-a, alvo: psg.legal.gdpr-k-and-coppa }
  - { tipo: relacionado-a, alvo: psg.legal.eca-and-digital-eca }
  - { tipo: relacionado-a, alvo: psg.access.school-roles }
  - { tipo: complementa, alvo: iop.br.lgpd }
termos: [consentimento parental, responsável legal, consentimento específico e em destaque, verificação razoável, verifiable parental consent, holder of parental responsibility, melhor interesse, criança, adolescente, ônus da prova, vício de consentimento, autorização genérica]
---

# Consentimento parental

## Definição e terminologia

Consentimento parental é o consentimento, no sentido da LGPD, dado por um dos pais ou pelo responsável legal em nome de uma criança. A LGPD define consentimento como "manifestação livre, informada e inequívoca pela qual o titular concorda com o tratamento de seus dados pessoais para uma finalidade determinada" [F: brasil2018lgpd, art. 5, XII] e, no artigo dedicado a crianças e adolescentes, determina que "o tratamento de dados pessoais de crianças deverá ser realizado com o consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal" [F: brasil2018lgpd, art. 14, §1]. A lei não define "criança"; o ECA considera criança "a pessoa até doze anos de idade incompletos, e adolescente aquela entre doze e dezoito anos de idade" [F: lei80691990, art. 2], e é essa a definição que a interpretação corrente da LGPD toma emprestada [I]. A Convenção sobre os Direitos da Criança, promulgada no Brasil pelo Decreto 99.710/1990, usa outro corte: criança é "todo ser humano com menos de dezoito anos de idade, a não ser que [...] a maioridade seja alcançada antes" [F: decreto997101990, art. 1].

Nomes equivalentes em outros regimes: a regra COPPA dos Estados Unidos fala em *verifiable parental consent* [F: cfr16312coppa, §312.5(a)(1)]; o GDPR fala em consentimento "dado ou autorizado pelo titular da responsabilidade parental" (*holder of parental responsibility*) para serviços da sociedade da informação oferecidos diretamente a crianças [F: eu2016gdpr, art. 8(1)].

O que não é: não é o assentimento da própria criança (ver `psg.consent.child-assent`); não é a única base legal possível para dados de crianças e adolescentes (ver abaixo o enunciado da ANPD); e não é uma autorização ampla, pois "as autorizações genéricas para o tratamento de dados pessoais serão nulas" [F: brasil2018lgpd, art. 8, §4].

## Problema que resolve

Crianças não têm capacidade civil para consentir por si: o Código Civil declara absolutamente incapazes os menores de 16 anos e relativamente incapazes os maiores de 16 e menores de 18 [F: lei104062002, art. 3 e art. 4, I]. O consentimento parental resolve a lacuna de quem manifesta a vontade quando a base legal escolhida é o consentimento, ao mesmo tempo em que impõe ao controlador três ônus que não existem para adultos: destacar o pedido, verificar razoavelmente quem consentiu e informar em linguagem que a criança entenda [F: brasil2018lgpd, art. 14, §§1, 5 e 6]. O Comitê dos Direitos da Criança recomenda, no mesmo sentido, que onde o consentimento da criança for considerado insuficiente e o parental for exigido, as organizações verifiquem que o consentimento é "informed, meaningful and given by the child's parent or caregiver" [F: crc2021gc25, §71].

## Fundamentos e funcionamento

### Quando é exigido

A redação do art. 14 §1 gerou dúvida sobre se o consentimento parental seria a única base legal para dados de crianças. A ANPD, após estudo preliminar e tomada de subsídios entre 8 de setembro e 7 de outubro de 2022, com 78 contribuições, aprovou por unanimidade no Circuito Deliberativo 11/2023 um enunciado com o texto: "O tratamento de dados pessoais de crianças e adolescentes poderá ser realizado com base nas hipóteses legais previstas no art. 7º ou, no caso de dados sensíveis, no art. 11 da Lei Geral de Proteção de Dados Pessoais (LGPD), desde que observado e prevalecente o seu melhor interesse, a ser avaliado no caso concreto, nos termos do caput do art. 14 da Lei." [F: anpd2023voto12, voto do relator, minuta consolidada e votos dos demais diretores]. O relator registra que essa leitura coincide com enunciado da IX Jornada de Direito Civil do Conselho da Justiça Federal e com a orientação do ICO britânico sobre o GDPR [F: anpd2023voto12, §2.106], e que o tratamento "não deve observar somente o caput do artigo 14, mas sim todos os seus dispositivos" [F: anpd2023voto12, item 4]. A versão publicada do enunciado (Enunciado CD/ANPD nº 1/2023) não foi aberta nesta sessão; ver Lacunas.

Consequência prática [I]: o consentimento parental é exigido quando o controlador escolhe o consentimento como base legal para dados de criança; se escolher outra base dos arts. 7 ou 11, deve documentar a avaliação de melhor interesse no caso concreto, e os demais parágrafos do art. 14 (informação pública, não condicionamento, linguagem acessível) continuam aplicáveis. A lei prevê ainda uma exceção estreita: dados de crianças podem ser coletados sem o consentimento do §1 "quando a coleta for necessária para contatar os pais ou o responsável legal, utilizados uma única vez e sem armazenamento, ou para sua proteção", nunca repassados a terceiro sem esse consentimento [F: brasil2018lgpd, art. 14, §3]. A COPPA tem lista análoga e mais longa de exceções ao consentimento prévio, por exemplo coleta do contato do responsável só para obter o consentimento, com eliminação se ele não vier em prazo razoável [F: cfr16312coppa, §312.5(c)(1)].

Para adolescentes (12 a 18 anos) o §1 não fala em consentimento parental, e a lei não diz quem consente; é uma questão aberta (ver Lacunas). O GDPR fixa 16 anos como idade a partir da qual a criança consente sozinha para serviços da sociedade da informação, permitindo aos Estados-membros reduzir até 13 [F: eu2016gdpr, art. 8(1)].

### Forma e informação

O consentimento "deverá ser fornecido por escrito ou por outro meio que demonstre a manifestação de vontade do titular"; se por escrito, "deverá constar de cláusula destacada das demais cláusulas contratuais"; e "deverá referir-se a finalidades determinadas" [F: brasil2018lgpd, art. 8, caput, §1 e §4]. O consentimento é nulo se as informações tiverem "conteúdo enganoso ou abusivo" ou não forem apresentadas previamente com transparência [F: brasil2018lgpd, art. 9, §1]. No caso de crianças, soma-se o dever de manter pública "a informação sobre os tipos de dados coletados, a forma de sua utilização e os procedimentos para o exercício dos direitos" do art. 18 [F: brasil2018lgpd, art. 14, §2], e o de fornecer as informações "de maneira simples, clara e acessível, consideradas as características físico-motoras, perceptivas, sensoriais, intelectuais e mentais do usuário, com uso de recursos audiovisuais quando adequado", de modo a informar os pais e ser "adequada ao entendimento da criança" [F: brasil2018lgpd, art. 14, §6]. O GDPR exige que o pedido de consentimento embutido em declaração escrita seja "clearly distinguishable from the other matters, in an intelligible and easily accessible form, using clear and plain language" [F: eu2016gdpr, art. 7(2)].

A ISO/IEC 29184:2020 traduz essas exigências em controles de aviso e consentimento: expressão apropriada ao público-alvo, inclusive subgrupos em desvantagem [F: iso291842020, 5.2.3]; aviso multilíngue [F: iso291842020, 5.2.4]; e, na cláusula de consentimento, "informed and freely given consent", "independence from other consent" e "separate consent to necessary and optional elements of PII" [F: iso291842020, sumário, 5.4.3, 5.4.5 e 5.4.6].

### Verificação razoável

O controlador "deve realizar todos os esforços razoáveis para verificar que o consentimento [...] foi dado pelo responsável pela criança, consideradas as tecnologias disponíveis" [F: brasil2018lgpd, art. 14, §5]. O GDPR usa fórmula quase idêntica: "reasonable efforts to verify [...] taking into consideration available technology" [F: eu2016gdpr, art. 8(2)]. Nenhum dos dois lista métodos. A COPPA lista: o método deve ser "reasonably calculated, in light of available technology, to ensure that the person providing consent is the child's parent" [F: cfr16312coppa, §312.5(b)(1)], e os métodos reconhecidos incluem formulário assinado devolvido por correio, fax ou digitalização; cartão de crédito ou débito com notificação de transação; ligação para número gratuito com pessoal treinado; videoconferência com pessoal treinado; checagem de documento oficial contra base de dados, com eliminação imediata; autenticação baseada em conhecimento com perguntas dinâmicas de múltipla escolha que "a child age 12 or younger in the parent's household could not reasonably ascertain"; comparação de documento com foto e imagem facial confirmada por pessoal treinado, com eliminação após a confirmação; e, só para operadores que não divulgam dados a terceiros, e-mail ou mensagem de texto com passo adicional de confirmação [F: cfr16312coppa, §312.5(b)(2)(i)–(ix)]. Programas de porto seguro aprovados pela FTC podem homologar outros métodos [F: cfr16312coppa, §312.5(b)(3)]. A emenda de 2025 da regra, publicada em 90 FR 16918 (22 de abril de 2025), vigente desde 23 de junho de 2025 e com prazo de adequação até 22 de abril de 2026, codificou a autenticação baseada em conhecimento como método aprovado e admitiu mensagem de texto para iniciar o processo de consentimento [F: ftc2025coppafinalrule, DATES e discussão do §312.5(b)(2)(vi)].

### Prova

"Cabe ao controlador o ônus da prova de que o consentimento foi obtido em conformidade com o disposto nesta Lei" [F: brasil2018lgpd, art. 8, §2]; o GDPR impõe o mesmo dever de demonstração [F: eu2016gdpr, art. 7(1)]. Isso faz do registro do consentimento (quem, quando, para quê, com qual aviso, verificado como) parte inseparável do consentimento parental; o esquema de registro é tratado em `psg.consent.permission-lifecycle`. A ISO/IEC 29184 traz, em anexo informativo, exemplo de "consent receipt or consent record" [F: iso291842020, sumário, Anexo B].

### Não condicionamento e consentimento separado

Controladores "não deverão condicionar a participação dos titulares [crianças] em jogos, aplicações de internet ou outras atividades ao fornecimento de informações pessoais além das estritamente necessárias à atividade" [F: brasil2018lgpd, art. 14, §4]. No GDPR, condicionar um serviço a consentimento para dados desnecessários pesa contra a liberdade do consentimento [F: eu2016gdpr, art. 7(4)]. A COPPA exige dar ao responsável a opção de consentir com a coleta e uso sem consentir com a divulgação a terceiros, e obter consentimento separado para a divulgação, salvo se integral ao serviço [F: cfr16312coppa, §312.5(a)(2)]; a emenda de 2025 reforçou essa separação [F: ftc2025coppafinalrule, discussão do §312.5(a)(2)].

## Requisitos e pressupostos

- Saber quem é o responsável legal e por qual criança responde: o vínculo responsável–criança é um dado de identidade e de papel (ver `psg.access.school-roles`), sem o qual não há como "verificar que o consentimento foi dado pelo responsável" [I].
- Um aviso versionado, em linguagem acessível, que preceda o pedido [F: brasil2018lgpd, art. 9, §1].
- Finalidades enumeradas uma a uma, porque autorização genérica é nula [F: brasil2018lgpd, art. 8, §4].
- Um canal de revogação "gratuito e facilitado" desde o primeiro dia [F: brasil2018lgpd, art. 8, §5].

## Vantagens e limitações

O consentimento parental dá ao responsável controle explícito e revogável e produz trilha de prova; a lei o cerca de salvaguardas (destaque, verificação, linguagem). Como limitação, é frágil: nulo se o aviso for enganoso, revogável a qualquer tempo e inadequado como base para tratamentos de que o serviço não pode prescindir, como obrigações escolares ou proteção da criança [I, a partir de brasil2018lgpd, art. 8 §5, art. 9 §1 e art. 14 §3]. Em ambientes escolares o responsável muitas vezes não está presente no momento do uso, e a verificação forte (documento, videoconferência) tem custo e cria novos dados sensíveis, o que a própria COPPA mitiga exigindo eliminação imediata do material de verificação [F: cfr16312coppa, §312.5(b)(2)(v) e (vii)]. O Comitê dos Direitos da Criança alerta ainda que a supervisão parental deve ser "proportionate and in accordance with the child's evolving capacities" [F: crc2021gc25, §76].

## Alternativas e comparações

| Critério | LGPD | GDPR | COPPA (16 CFR 312) |
|---|---|---|---|
| Quem consente | Um dos pais ou responsável legal, para crianças [F: brasil2018lgpd, art. 14 §1] | Titular da responsabilidade parental, abaixo de 16 (ou 13 a 16 por lei nacional) [F: eu2016gdpr, art. 8(1)] | *Parent*, antes de qualquer coleta, uso ou divulgação [F: cfr16312coppa, §312.5(a)(1)] |
| Verificação | "esforços razoáveis", tecnologias disponíveis [F: brasil2018lgpd, art. 14 §5] | "reasonable efforts", tecnologia disponível [F: eu2016gdpr, art. 8(2)] | Lista de métodos aprovados e porto seguro [F: cfr16312coppa, §312.5(b)] |
| Prova | Ônus do controlador [F: brasil2018lgpd, art. 8 §2] | Controlador deve demonstrar [F: eu2016gdpr, art. 7(1)] | Não tratada no §312.5 |
| Consentimento separado | Finalidades determinadas; genérico é nulo [F: brasil2018lgpd, art. 8 §4] | Pedido destacado de outras matérias [F: eu2016gdpr, art. 7(2)] | Separado para divulgação a terceiros [F: cfr16312coppa, §312.5(a)(2)] |
| Exceções ao consentimento | Contato com os pais, uso único, proteção [F: brasil2018lgpd, art. 14 §3]; outras bases dos arts. 7 e 11 [F: anpd2023voto12] | Serviços preventivos ou de aconselhamento não exigem consentimento parental [F: eu2016gdpr, considerando 38] | Nove hipóteses em §312.5(c) [F: cfr16312coppa] |

Entre métodos de verificação, a escala de robustez descrita pela COPPA vai do e-mail com confirmação (aceito só sem divulgação a terceiros) até documento com reconhecimento facial e revisão humana; o critério de escolha é a proporcionalidade entre o risco do tratamento e o custo e intrusividade do método [I, a partir de cfr16312coppa, §312.5(b)(2)].

## Exemplo técnico independente de domínio

```
procedimento obter_consentimento_parental(crianca, responsavel, finalidades[], aviso_v):
    pré-condição: vinculo(responsavel, crianca) confirmado por cadastro ou documento
    exibir aviso_v em formato acessível (texto simples + áudio/vídeo quando adequado)
    para cada finalidade f em finalidades:              # uma caixa por finalidade, nenhuma pré-marcada
        f.necessaria ? informar "condição para o serviço" : oferecer opt-in separado
    metodo = escolher_verificacao(risco(finalidades))  # e-mail confirmado | pagamento | documento | videochamada
    se not verificar(responsavel, metodo): abortar e eliminar dados coletados para o pedido
    registrar(recibo = {crianca, responsavel, finalidades aceitas, aviso_v, metodo, data_hora, canal})
    eliminar material de verificação (imagem de documento, foto) após confirmação
    entregar ao responsável: cópia do recibo + link de revogação gratuito
```

## Relações com outros conceitos

Depende de `psg.legal.lgpd-children`, que aprofunda o art. 14, o melhor interesse e as bases legais; aqui só se trata do consentimento como uma delas. Complementa `psg.consent.child-assent` (a voz da própria criança, que o consentimento parental não substitui) e `psg.consent.permission-lifecycle` (registro, revogação e migração do que foi consentido). Relaciona-se com `psg.legal.gdpr-k-and-coppa` e `psg.legal.eca-and-digital-eca` para a comparação regulatória, com `psg.access.school-roles` para o papel "responsável" e com `iop.br.lgpd` para a visão de interoperabilidade.

## Lacunas e questões abertas

- O texto publicado do Enunciado CD/ANPD nº 1/2023 (Diário Oficial) não foi aberto; o conteúdo aqui citado vem do voto do relator e dos votos de acompanhamento no Circuito Deliberativo 11/2023, documento oficial da ANPD. Fontes secundárias indicam publicação em 24 ou 25 de maio de 2023; data não verificada em fonte primária.
- Quem consente por adolescentes (12 a 18) na LGPD: a lei não diz; o Código Civil os trata como relativamente incapazes a partir dos 16. Não foi localizada manifestação da ANPD sobre o ponto.
- A lei de proteção de crianças e adolescentes em ambientes digitais ("ECA Digital") não foi consultada nesta sessão; pode alterar deveres de verificação de idade e de consentimento. Fica para `psg.legal.eca-and-digital-eca`.
- As definições de "child" e "parent" da COPPA ficam em §312.2, não consultado; a idade de corte da regra deve ser confirmada lá.
- Não foi encontrada orientação brasileira sobre métodos aceitáveis de verificação do responsável; a lista da COPPA é referência comparativa, não norma aplicável.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| lei80691990 | normativo | 2026-10-29 |
| lei104062002 | normativo | 2026-10-29 |
| decreto997101990 | normativo | 2026-10-29 |
| anpd2023voto12 | tecnico (documento oficial da ANPD) | 2026-10-29 |
| crc2021gc25 | normativo (soft law, Comitê dos Direitos da Criança) | 2026-10-29 |
| eu2016gdpr | normativo (texto via reprodução gdpr-info.eu) | 2026-10-29 |
| cfr16312coppa | normativo (eCFR via LII) | 2026-10-29 |
| ftc2025coppafinalrule | normativo | 2026-10-29 |
| iso291842020 | normativo (escopo, sumário e cláusulas 5.1–5.2.4 via amostra) | 2026-10-29 |
