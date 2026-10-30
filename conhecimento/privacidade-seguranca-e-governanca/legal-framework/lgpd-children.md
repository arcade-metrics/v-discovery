---
id: psg.legal.lgpd-children
titulo: LGPD aplicada a crianças e adolescentes
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [brasil2018lgpd, mpv8692018, lei138532019, lei8069eca, anpd2023enunciado1, anpd2024legitimointeresse]
relacoes:
  - { tipo: parte-de, alvo: psg.legal.comparison }
  - { tipo: complementa, alvo: psg.legal.eca-and-digital-eca }
  - { tipo: complementa, alvo: iop.br.lgpd }
  - { tipo: complementa, alvo: iop.fund.privacidade-e-seguranca }
  - { tipo: relacionado-a, alvo: psg.consent.parental-consent }
  - { tipo: relacionado-a, alvo: psg.consent.child-assent }
  - { tipo: relacionado-a, alvo: psg.audit.ripd-dpia }
  - { tipo: relacionado-a, alvo: psg.audit.processing-records }
  - { tipo: relacionado-a, alvo: psg.ai.transparency-and-human-oversight }
  - { tipo: relacionado-a, alvo: psg.sec.incident-management }
termos: [melhor interesse, base legal, consentimento específico e em destaque, dado pessoal sensível, dado referente à saúde, legítimo interesse, teste de balanceamento, controlador, operador, RIPD]
---

# LGPD aplicada a crianças e adolescentes

## Definição e terminologia

A Lei 13.709/2018 (LGPD) dedica um único artigo ao tratamento de dados de menores: o art. 14 determina que "o tratamento de dados pessoais de crianças e de adolescentes deverá ser realizado em seu melhor interesse, nos termos deste artigo e da legislação pertinente" [F: brasil2018lgpd, art. 14]. A lei não define "criança" nem "adolescente"; a definição vem do art. 2 do Estatuto da Criança e do Adolescente: criança é "a pessoa até doze anos de idade incompletos", adolescente "aquela entre doze e dezoito anos de idade" [F: lei8069eca, art. 2].

Três termos da própria LGPD estruturam este documento: **base legal** (as hipóteses dos art. 7 e 11 que autorizam um tratamento); **consentimento**, definido como "manifestação livre, informada e inequívoca pela qual o titular concorda com o tratamento" [F: brasil2018lgpd, art. 5, XII]; e **dado pessoal sensível**, que inclui "dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural" [F: brasil2018lgpd, art. 5, II]. O "melhor interesse" não é definido na LGPD; a ANPD o lê à luz do art. 3 da Convenção sobre os Direitos da Criança e do Comentário Geral 14 (2013) do Comitê da ONU, que o descreve como direito substantivo, princípio interpretativo e regra processual [F: anpd2024legitimointeresse, §Dados pessoais de crianças e adolescentes].

O que este documento não cobre: a forma e a prova do consentimento parental (psg.consent.parental-consent), o assentimento da criança (psg.consent.child-assent) e a LGPD na troca de dados entre sistemas, que fica em iop.br.lgpd.

## Problema que resolve

Uma plataforma educacional trata dados de alunos menores em dezenas de operações distintas: cadastro, autenticação, registro de interações, modelagem do aprendiz, comunicação com responsáveis, relatórios para a escola. A pergunta prática é qual base legal sustenta cada uma e quando o consentimento parental do art. 14, §1 é de fato exigido. Uma leitura literal do §1 ("o tratamento de dados pessoais de crianças deverá ser realizado com o consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal" [F: brasil2018lgpd, art. 14, §1]) sugeria que consentimento seria a única base possível para crianças; a ANPD fixou interpretação diferente em 2023, descrita abaixo.

## Fundamentos e funcionamento

### Anatomia do art. 14

- **Caput**: melhor interesse como critério geral para crianças e adolescentes [F: brasil2018lgpd, art. 14].
- **§1**: consentimento "específico e em destaque" de ao menos um dos pais ou responsável legal, redigido para "crianças" (não para adolescentes) [F: brasil2018lgpd, art. 14, §1]. [I] A distinção textual entre caput (crianças e adolescentes) e §1 (crianças) é a razão pela qual o regime de consentimento parental reforçado é normalmente lido como aplicável a menores de 12 anos.
- **§2**: os controladores "deverão manter pública a informação sobre os tipos de dados coletados, a forma de sua utilização e os procedimentos para o exercício dos direitos" do art. 18 [F: brasil2018lgpd, art. 14, §2].
- **§3**: dados de crianças podem ser coletados sem o consentimento do §1 "quando a coleta for necessária para contatar os pais ou o responsável legal, utilizados uma única vez e sem armazenamento, ou para sua proteção", e "em nenhum caso poderão ser repassados a terceiro" sem esse consentimento [F: brasil2018lgpd, art. 14, §3].
- **§4**: proibição de condicionar a participação "em jogos, aplicações de internet ou outras atividades ao fornecimento de informações pessoais além das estritamente necessárias à atividade" [F: brasil2018lgpd, art. 14, §4].
- **§5**: "todos os esforços razoáveis para verificar que o consentimento [...] foi dado pelo responsável pela criança, consideradas as tecnologias disponíveis" [F: brasil2018lgpd, art. 14, §5].
- **§6**: informação "simples, clara e acessível, consideradas as características físico-motoras, perceptivas, sensoriais, intelectuais e mentais do usuário, com uso de recursos audiovisuais quando adequado", voltada aos pais e "adequada ao entendimento da criança" [F: brasil2018lgpd, art. 14, §6].

### A posição da ANPD sobre bases legais

O Enunciado CD/ANPD nº 1, de 22 de maio de 2023, publicado no DOU de 24/05/2023, tem redação única: "O tratamento de dados pessoais de crianças e adolescentes poderá ser realizado com base nas hipóteses legais previstas no art. 7º ou no art. 11 da Lei Geral de Proteção de Dados Pessoais (LGPD), desde que observado e prevalecente o seu melhor interesse, a ser avaliado no caso concreto, nos termos do art. 14 da Lei" [F: anpd2023enunciado1]. Ou seja, segundo a autoridade, o consentimento parental não é a única base legal possível; é uma entre as dez do art. 7 (consentimento, obrigação legal, políticas públicas, pesquisa, contrato, exercício de direitos, proteção da vida, tutela da saúde, legítimo interesse, proteção do crédito) [F: brasil2018lgpd, art. 7] e as do art. 11 para dados sensíveis.

O guia orientativo da ANPD sobre legítimo interesse (fev. 2024) detalha o requisito adicional: o tratamento de dados de menores com base no legítimo interesse "pressupõe que o controlador leve em consideração, de forma prioritária, o melhor interesse"; se o teste de balanceamento for inconclusivo ou não houver medidas de mitigação adequadas, "deverá ser adotada outra base legal". O controlador deve "elaborar teste de balanceamento e manter registro da justificativa" demonstrando (i) o que foi considerado melhor interesse, (ii) os critérios de ponderação e (iii) que o tratamento não gera riscos desproporcionais [F: anpd2024legitimointeresse, §Dados pessoais de crianças e adolescentes]. O guia considera o legítimo interesse "mais apropriado em situações nas quais há uma relação prévia e direta do controlador com os titulares e quando o tratamento visa a assegurar a proteção de seus direitos e interesses ou viabilizar a prestação de serviços que os beneficiem" [F: anpd2024legitimointeresse].

Dois exemplos do guia são diretamente escolares. No exemplo 2 (coleta de dados ao acessar a rede wi-fi da escola, para autenticação e segurança), a ANPD vê "indícios de que a coleta [...] pode ser efetuada com base no legítimo interesse", por existir relação prévia e direta entre escola e estudantes, condicionado ao teste de balanceamento [F: anpd2024legitimointeresse, exemplo 2]. No exemplo 3 (aplicativo educacional de geografia que exibe publicidade de alimentos ultraprocessados com base em "legítimo interesse" para "aprimoramento do aplicativo"), a ANPD conclui que o legítimo interesse "não será a hipótese legal mais apropriada", por não haver legítima expectativa do titular e por conflito com o melhor interesse [F: anpd2024legitimointeresse, exemplo 3].

### Dados de deficiência e laudo como dado sensível

Um laudo, um diagnóstico ou um atributo "aluno com deficiência X" é "dado referente à saúde" e, portanto, dado pessoal sensível [F: brasil2018lgpd, art. 5, II]. O art. 11 restringe as bases: consentimento "de forma específica e destacada, para finalidades específicas" dado pelo "titular ou seu responsável legal" (inciso I), ou, sem consentimento, só "nas hipóteses em que for indispensável para" obrigação legal, políticas públicas, pesquisa, exercício de direitos, proteção da vida, tutela da saúde ou prevenção à fraude (inciso II) [F: brasil2018lgpd, art. 11]. O legítimo interesse não está no art. 11; o guia da ANPD afirma expressamente que "o legítimo interesse não é aplicável ao tratamento de dados pessoais sensíveis" [F: anpd2024legitimointeresse, fase 1]. O §1 do art. 11 estende o regime a "qualquer tratamento de dados pessoais que revele dados pessoais sensíveis e que possa causar dano" [F: brasil2018lgpd, art. 11, §1]. [I] Isso alcança inferências: um modelo que deduz deficiência a partir de padrões de interação passa a tratar dado sensível mesmo sem laudo cadastrado. O §4 veda a comunicação ou uso compartilhado de dados de saúde entre controladores "com objetivo de obter vantagem econômica", com exceções [F: brasil2018lgpd, art. 11, §4].

### Decisões automatizadas

O art. 20, na redação da Lei 13.853/2019, dá ao titular "direito a solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado" que afetem seus interesses, e o §1 obriga o controlador a fornecer "informações claras e adequadas a respeito dos critérios e dos procedimentos" usados, observado segredo comercial [F: brasil2018lgpd, art. 20]. A redação original de 2018 previa revisão "por pessoa natural"; a MP 869/2018 deu ao caput a redação sem a expressão, e a Lei 13.853/2019, de conversão, fixou esse texto; o §3 incluído pela Lei 13.853/2019 foi vetado [F: brasil2018lgpd, art. 20, notas de redação; F: mpv8692018; F: lei138532019]. O tratamento aprofundado fica em psg.ai.transparency-and-human-oversight.

## Requisitos e pressupostos

| Exigência | Natureza | Fonte |
|---|---|---|
| Tratamento no melhor interesse, avaliado no caso concreto | obrigatória (lei) | [F: brasil2018lgpd, art. 14]; [F: anpd2023enunciado1] |
| Base legal identificada para cada operação, antes de iniciá-la | obrigatória (lei) | [F: brasil2018lgpd, art. 7 e 11] |
| Se a base for consentimento e o titular for criança: específico, em destaque, de pai ou responsável, com esforços razoáveis de verificação | obrigatória (lei) | [F: brasil2018lgpd, art. 14, §1 e §5] |
| Consentimento revogável, por escrito ou meio que demonstre a vontade, com ônus da prova do controlador; autorizações genéricas nulas | obrigatória (lei) | [F: brasil2018lgpd, art. 8] |
| Informação pública sobre tipos de dados, uso e exercício de direitos; linguagem acessível à criança e aos pais | obrigatória (lei) | [F: brasil2018lgpd, art. 14, §2 e §6] |
| Não condicionar participação a dados além do estritamente necessário | obrigatória (lei) | [F: brasil2018lgpd, art. 14, §4] |
| Dados de saúde (laudo, deficiência) só nas hipóteses do art. 11 | obrigatória (lei) | [F: brasil2018lgpd, art. 11] |
| Registro das operações de tratamento | obrigatória (lei) | [F: brasil2018lgpd, art. 37] |
| Medidas de segurança e comunicação de incidentes à ANPD e ao titular | obrigatória (lei) | [F: brasil2018lgpd, art. 46 e 48] |
| Teste de balanceamento documentado, se a base for legítimo interesse | orientação da ANPD | [F: anpd2024legitimointeresse] |
| RIPD: a lei diz que a ANPD "poderá determinar"; a ANPD orienta elaborá-lo quando o tratamento é de alto risco e cita dados de menores como critério de alto risco (Resolução CD/ANPD 2/2022, não aberta nesta sessão) | obrigatória segundo a orientação, facultativa no texto da lei | [F: brasil2018lgpd, art. 38]; [F: anpd2024legitimointeresse] |
| Programa de governança em privacidade | facultativa ("poderão") | [F: brasil2018lgpd, art. 50] |

## Vantagens e limitações

A interpretação do Enunciado 1/2023 evita que toda operação de uma plataforma escolar dependa de consentimento parental, o que seria frágil (revogável a qualquer momento, art. 8, §5) para operações que a escola precisa executar de qualquer modo [I]. Em contrapartida, transfere ao controlador o ônus de demonstrar, operação por operação, que o melhor interesse prevalece, com documentação [F: anpd2024legitimointeresse]. A principal limitação do quadro atual é a ausência de regulamento específico da ANPD sobre dados de menores: há um enunciado de uma frase e um guia sobre uma base legal, não um guia abrangente (ver Lacunas).

## Alternativas e comparações

Mapa [I] de bases legais candidatas para operações típicas de uma plataforma usada por escola, derivado do texto da lei e dos exemplos da ANPD; cada caso exige o teste do melhor interesse no concreto:

| Operação | Base candidata | Observação |
|---|---|---|
| Cadastro e autenticação de alunos a pedido da escola | legítimo interesse (art. 7, IX) ou execução de contrato com a escola (art. 7, V); escola pública: políticas públicas (art. 7, III; art. 23) | análogo ao exemplo 2 da ANPD [F: anpd2024legitimointeresse] |
| Registro de interações para feedback pedagógico ao aluno | legítimo interesse, se há relação direta e serviço que beneficia o titular | teste de balanceamento obrigatório pela orientação da ANPD |
| Atributo de deficiência ou laudo em modelo de aluno | art. 11, I (consentimento específico e destacado do responsável) ou art. 11, II, a/b quando a escola tem obrigação legal ou política pública que exija | legítimo interesse excluído [F: anpd2024legitimointeresse] |
| Publicidade ou perfilamento comercial | nenhuma base considerada adequada pela ANPD no exemplo 3 | ver também psg.legal.eca-and-digital-eca |
| Pesquisa com dados de interação | órgão de pesquisa, com anonimização sempre que possível (art. 7, IV; art. 11, II, c) | ética de pesquisa fica em outro domínio |
| Contato único com os pais sem armazenamento | art. 14, §3 | sem repasse a terceiros |

## Exemplo técnico independente de domínio

```
função base_legal(operacao, titular):
    se titular.idade < 12: regime = "crianca" senão se < 18: regime = "adolescente"
    se operacao.dados contém saude|biometria|genetico ou operacao.infere_sensivel:
        candidatas = {art11.I consentimento_destacado_responsavel, art11.II.*}   # sem legitimo interesse
    senão:
        candidatas = {art7.I..X}
    para cada base em candidatas:
        se base == legitimo_interesse:
            teste = balanceamento(interesse, expectativa_do_titular, riscos, mitigacoes, melhor_interesse)
            se teste.inconclusivo: continuar
        se melhor_interesse_prevalece(operacao, regime):
            registrar(operacao, base, justificativa)        # art. 37 + guia ANPD
            se regime == "crianca" e base == consentimento:
                exigir(consentimento_especifico_em_destaque, verificacao_razoavel)   # art. 14 §1, §5
            retornar base
    retornar "não tratar"
```

## Relações com outros conceitos

Parte da comparação psg.legal.comparison. Complementa psg.legal.eca-and-digital-eca, que traz a camada do ECA e do Estatuto Digital sobre a mesma plataforma. Complementa iop.br.lgpd e iop.fund.privacidade-e-seguranca: a aplicação da LGPD à troca de dados entre sistemas (escopos, identidade federada, contratos entre controlador e operador) fica lá. A forma do consentimento parental e o assentimento são aprofundados em psg.consent.parental-consent e psg.consent.child-assent; o RIPD e o registro de operações, em psg.audit.ripd-dpia e psg.audit.processing-records; incidentes, em psg.sec.incident-management; art. 20, em psg.ai.transparency-and-human-oversight.

## Lacunas e questões abertas

- A ANPD não publicou, até a data de consulta, um guia orientativo abrangente sobre dados de crianças e adolescentes; o que existe é o Enunciado 1/2023, um estudo preliminar de 2022 citado pelo guia de legítimo interesse (não aberto nesta sessão) e a seção do guia de 2024. Notícias de uma tomada de subsídios em 2024 para um projeto regulatório não foram confirmadas em página oficial.
- A Resolução CD/ANPD 2/2022, que lista dados de menores entre os critérios de alto risco, é citada aqui via guia de 2024; o texto da resolução foi lido em psg.audit.ripd-dpia.
- O texto consultado no Planalto apresenta versões sobrepostas de dispositivos alterados por MP 869/2018, Lei 13.853/2019, MP 1.317/2025 e Lei 15.352/2026. O art. 52, II foi conferido no texto compilado em 30/10/2026: multa simples de até 2% do faturamento no Brasil, "limitada, no total, a R$ 50.000.000,00 (cinquenta milhões de reais) por infração", sem nota de alteração [F: brasil2018lgpd, art. 52, II]; os demais incisos e parágrafos do art. 52 não foram reconferidos.
- Não há posição da ANPD sobre quando a verificação do §5 é "razoável" para uma plataforma escolar; o assunto fica para psg.consent.parental-consent.
- A escola como controladora, operadora ou controladora conjunta com o fornecedor da plataforma não é tratada aqui; o guia da ANPD sobre agentes de tratamento não foi consultado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-30 |
| mpv8692018 | normativo | 2026-10-30 |
| lei138532019 | normativo | 2026-10-30 |
| lei8069eca | normativo | 2026-10-29 |
| anpd2023enunciado1 | normativo | 2026-10-29 |
| anpd2024legitimointeresse | tecnico | 2026-10-29 |
