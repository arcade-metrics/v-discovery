---
id: psg.legal.gdpr-k-and-coppa
titulo: GDPR, Age Appropriate Design Code e COPPA como referências comparativas
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [eu2016gdpr, ico2020aadc, ftc2025coppa, ftc2025coppafinalrule, ftc2025coppafaq]
relacoes:
  - { tipo: parte-de, alvo: psg.legal.comparison }
  - { tipo: alternativa-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.consent.parental-consent }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: psg.ai.transparency-and-human-oversight }
termos: [GDPR-K, information society service, holder of parental responsibility, verifiable parental consent, school authorization, age assurance, Age Appropriate Design Code, likely to be accessed by children, best interests of the child]
---

# GDPR, Age Appropriate Design Code e COPPA como referências comparativas

## Definição e terminologia

Três regimes estrangeiros são usados como referência de desenho para plataformas que tratam dados de menores. **GDPR-K** é o apelido informal dado às regras do Regulamento (UE) 2016/679 específicas para crianças, centradas no art. 8 e no considerando 38; o regulamento não usa esse termo. O **Age Appropriate Design Code** (AADC, também "Children's code") é o código de prática estatutário do Information Commissioner's Office do Reino Unido, "prepared under section 123 of the DPA 2018" [F: ico2020aadc, §About this code]. **COPPA** é a Children's Online Privacy Protection Rule, 16 CFR Part 312, da Federal Trade Commission dos Estados Unidos, que define "child" como "an individual under the age of 13" [F: ftc2025coppa, §312.2].

O que este documento não é: não é análise de aplicabilidade territorial desses regimes a operações no Brasil, nem substitui o estudo da LGPD (psg.legal.lgpd-children); serve para extrair critérios de desenho e para a comparação em psg.legal.comparison.

## Problema que resolve

A LGPD trata menores em um único artigo e a ANPD ainda não publicou guia abrangente. Os três regimes estrangeiros são mais antigos ou mais detalhados em pontos onde a norma brasileira é silenciosa: limiar de idade para consentimento digital, métodos aceitáveis de verificação parental, consentimento dado pela escola em nome dos pais, e padrões de desenho (configurações padrão, perfilamento, nudges, geolocalização). Conhecê-los permite antecipar requisitos que a regulamentação brasileira tende a incorporar [I].

## Fundamentos e funcionamento

### GDPR: art. 8, considerando 38 e dispositivos conexos

O considerando 38 afirma que "children merit specific protection with regard to their personal data, as they may be less aware of the risks, consequences and safeguards concerned", que tal proteção "should, in particular, apply to the use of personal data of children for the purposes of marketing or creating personality or user profiles", e que "the consent of the holder of parental responsibility should not be necessary in the context of preventive or counselling services offered directly to a child" [F: eu2016gdpr, considerando 38].

O art. 8 aplica-se apenas quando a base legal é o consentimento (art. 6(1)(a)) e o serviço é "information society service" oferecido diretamente a uma criança: o tratamento "shall be lawful where the child is at least 16 years old"; abaixo disso, só "if and to the extent that consent is given or authorised by the holder of parental responsibility"; os Estados-membros podem fixar idade menor, "provided that such lower age is not below 13 years" [F: eu2016gdpr, art. 8(1)]. O controlador "shall make reasonable efforts to verify" o consentimento parental "taking into consideration available technology" [F: eu2016gdpr, art. 8(2)]. [I] A estrutura é quase idêntica à do art. 14, §5 da LGPD ("esforços razoáveis [...] consideradas as tecnologias disponíveis"), o que sugere influência direta.

Três outros dispositivos importam para educação. O art. 6(1)(f) permite o legítimo interesse "except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject [...], in particular where the data subject is a child", e "shall not apply to processing carried out by public authorities in the performance of their tasks" [F: eu2016gdpr, art. 6(1)]. O art. 9(1) proíbe tratar "data concerning health", salvo exceções como consentimento explícito (9(2)(a)), interesse público relevante com base em lei (9(2)(g)) e pesquisa (9(2)(j)) [F: eu2016gdpr, art. 9]. O art. 12(1) exige informação "in a concise, transparent, intelligible and easily accessible form, using clear and plain language, in particular for any information addressed specifically to a child" [F: eu2016gdpr, art. 12(1)]. Sobre decisões automatizadas, o art. 22 garante o direito de não ser submetido a decisão "based solely on automated processing, including profiling" com efeitos jurídicos ou similarmente significativos, com salvaguardas mínimas de "human intervention", manifestação e contestação [F: eu2016gdpr, art. 22(1) e (3)]; o considerando 71 acrescenta que "such measure should not concern a child" [F: eu2016gdpr, considerando 71].

### UK Age Appropriate Design Code

O código "comes into force on 2 September 2020", após ser "laid before Parliament on 11 June 2020 and issued on 12 August 2020", e deu aos provedores até 2 September 2021 para se adequar [F: ico2020aadc, §About this code; §Transitional arrangements]. Aplica-se a provedores de "information society services" que tratam dados e são "likely to be accessed by children in the UK", e "it is not only for services aimed at children" [F: ico2020aadc, §About this code]. Pela section 127 do DPA 2018 o Commissioner "must take the code into account" ao avaliar conformidade, e "the courts must take its provisions into account wherever relevant" [F: ico2020aadc, §About this code].

São 15 padrões: best interests of the child; data protection impact assessments; age appropriate application; transparency; detrimental use of data; policies and community standards; default settings; data minimisation; data sharing; geolocation; parental controls; profiling; nudge techniques; connected toys and devices; online tools [F: ico2020aadc]. O primeiro padrão determina que "the best interests of the child should be a primary consideration when you design and develop online services", com origem no art. 3 da Convenção da ONU, e o ICO afirma ser "unlikely [...] that the commercial interests of an organisation will outweigh a child's right to privacy" [F: ico2020aadc, §1]. O terceiro padrão adota abordagem de risco: "either establish age with a level of certainty that is appropriate to the risks to the rights and freedoms of children" ou "apply the standards in this code to all your users instead"; os métodos listados são self-declaration, estimativa por inteligência artificial, verificação por terceiro, confirmação pelo titular da conta, medidas técnicas e "hard identifiers" (documentos), estes desaconselhados salvo risco que os justifique [F: ico2020aadc, §3]. O anexo B divide as faixas etárias em 0-5 ("pre-literate & early literacy"), 6-9 ("core primary school years"), 10-12 ("transition years"), 13-15 ("early teens") e 16-17 ("approaching adulthood") [F: ico2020aadc, anexo B].

### COPPA: 16 CFR Part 312 e a revisão de 2025

A regra exige "verifiable parental consent" antes de coletar informação pessoal de menores de 13 anos; qualquer método "must be reasonably calculated" a assegurar que quem consente é o responsável [F: ftc2025coppa, §312.5(b)(1)]. Os métodos enumerados incluem formulário assinado devolvido por correio, fax ou digitalização; transação monetária com notificação ao titular do cartão; ligação para número gratuito com pessoal treinado; videoconferência; verificação de documento oficial com exclusão posterior; e e-mail com passo adicional, admitido só quando não há divulgação a terceiros [F: ftc2025coppa, §312.5(b)(2)]. As exceções do §312.5(c) cobrem, entre outras, coleta de contato só para obter consentimento, resposta única a pedido da criança, proteção da segurança da criança e identificadores persistentes usados apenas para operações internas [F: ftc2025coppa, §312.5(c)]. O §312.8 exige "reasonable procedures to protect the confidentiality, security, and integrity" dos dados, e o §312.10 limita a retenção a "only as long as is reasonably necessary to fulfill the purpose for which the information was collected" [F: ftc2025coppa, §312.8 e §312.10].

A revisão final foi publicada em 90 FR 16918 (22 de abril de 2025), com vigência em 23 de junho de 2025 e prazo de conformidade até 22 de abril de 2026, salvo dispositivos indicados [F: ftc2025coppafinalrule, DATES]. Mudanças principais: a definição de personal information passa a incluir "a biometric identifier that can be used for the automated or semi-automated recognition of an individual" e "a government-issued identifier"; o operador "must obtain separate verifiable parental consent" para divulgar dados a terceiros; adiciona-se o método "text plus" (§312.5(b)(2)(ix)); exige-se "a written information security program" (§312.8(b)); e "personal information collected online from a child may not be retained indefinitely", com "a written data retention policy" obrigatória (§312.10) [F: ftc2025coppafinalrule]. A FTC declarou que "is not finalizing the proposed amendments to the Rule related to ed tech and the role of schools at this time", para evitar conflito com possíveis alterações nas regras do FERPA pelo Departamento de Educação [F: ftc2025coppafinalrule].

A posição sobre escolas permanece, portanto, no guia de perguntas frequentes da FTC: escolas "may act as the parent's agent and can consent under COPPA" em nome dos pais, mas só quando o operador coleta informação "for the use and benefit of the school, and for no other commercial purpose"; se usar os dados "for its own commercial purposes", precisa de consentimento parental direto. O operador deve dar à escola o aviso direto de suas práticas, a descrição dos tipos de dados coletados, a oportunidade de revisar e apagar os dados e de impedir coleta futura. A FTC recomenda que a decisão seja da escola ou rede, "rather than delegating that decision to the teacher", e que as escolas assegurem que operadores apaguem os dados quando não forem mais necessários ao fim educacional [F: ftc2025coppafaq, §N].

## Requisitos e pressupostos

- GDPR e COPPA condicionam o regime reforçado ao fato de o serviço ser oferecido diretamente à criança e, no GDPR, à base legal ser consentimento; o AADC se aplica por "likely to be accessed" independentemente da base legal [F: eu2016gdpr, art. 8; F: ico2020aadc; F: ftc2025coppa].
- Verificação parental "razoável" no GDPR e "reasonably calculated" na COPPA; só a COPPA enumera métodos aceitos [F: eu2016gdpr, art. 8(2); F: ftc2025coppa, §312.5(b)].
- Age assurance proporcional ao risco, com preferência por métodos menos invasivos [F: ico2020aadc, §3].

## Vantagens e limitações

A COPPA é o único dos três regimes com regra explícita para consentimento dado pela escola, o que resolve na prática o caso de plataforma contratada pela instituição; a contrapartida é o limite estrito ao fim educacional e a renúncia a qualquer uso comercial [F: ftc2025coppafaq, §N]. O AADC é o mais detalhado em desenho (15 padrões, faixas etárias) mas é código de prática, não lei: vincula pela consideração obrigatória do regulador e das cortes [F: ico2020aadc]. O GDPR tem a regra mais flexível (13 a 16 anos conforme o Estado) e exclui explicitamente o legítimo interesse para autoridades públicas, o que afeta escolas públicas [F: eu2016gdpr, art. 6(1)]. Nenhum dos três é diretamente aplicável a operações puramente brasileiras; seu uso aqui é de referência de desenho [I].

## Exemplo técnico independente de domínio

```
# Matriz de decisão de age assurance inspirada no padrão 3 do AADC
risco_do_tratamento = dpia.nivel          # baixo | medio | alto
se risco == baixo:  metodo = autodeclaracao + medidas_tecnicas (tela neutra, sem reenvio imediato)
se risco == medio:  metodo = confirmacao_pelo_titular_da_conta_adulta | estimativa_por_terceiro
se risco == alto:   metodo = verificacao_por_terceiro (resposta sim/nao, sem reter documento)
se certeza_insuficiente(metodo, risco): aplicar_padroes_do_codigo_a_todos_os_usuarios()
```

## Relações com outros conceitos

Parte de psg.legal.comparison. Alternativa de referência a psg.legal.lgpd-children (mesmo problema, outros ordenamentos). Métodos de verificação parental alimentam psg.consent.parental-consent; os padrões de desenho do AADC, psg.access.minimization-and-privacy-by-design; art. 22 do GDPR e considerando 71, psg.ai.transparency-and-human-oversight.

## Lacunas e questões abertas

- O texto do GDPR foi lido em espelho não oficial (gdpr-info.eu), porque o EUR-Lex (CELEX 32016R0679) e o legislation.gov.uk bloquearam acesso automatizado nesta sessão; as citações devem ser conferidas no Jornal Oficial antes de uso formal.
- O 16 CFR Part 312 foi lido na edição de 1º de janeiro de 2025 do CFR (govinfo), anterior à revisão de abril de 2025; a versão consolidada no eCFR não abriu. Os dispositivos novos foram lidos no texto do Federal Register.
- O guia de perguntas frequentes da FTC não exibe data de atualização; não foi possível confirmar se reflete a revisão de 2025.
- A seção de idades por Estado-membro do GDPR (quais países adotaram 13, 14, 15 ou 16) não foi verificada em fonte primária.
- O AADC foi lido nas páginas "About this code", padrões 1 e 3, anexo B e arranjos transitórios; os demais padrões foram vistos só pelo título.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| eu2016gdpr | normativo (lido em espelho) | 2026-10-29 |
| ico2020aadc | normativo (código de prática estatutário) | 2026-10-29 |
| ftc2025coppa | normativo | 2026-10-29 |
| ftc2025coppafinalrule | normativo | 2026-10-29 |
| ftc2025coppafaq | tecnico | 2026-10-29 |
