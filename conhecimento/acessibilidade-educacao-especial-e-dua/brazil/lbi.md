---
id: acs.br.lbi
titulo: Lei Brasileira de Inclusão (Lei 13.146/2015) e o quadro de obrigatoriedade para plataformas educacionais
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [lei131462015, lei100982000, decreto52962004, lei152492025, lei127642012, lei142542021, decreto69492009, slti2007portaria3, mpf2025art63, abnt2025nbr17225, decreto126862025, mecportaria4212026, decreto56262005, lei93941996]
relacoes:
  - { tipo: depende-de, alvo: acs.found.barriers-and-reasonable-accommodation }
  - { tipo: relacionado-a, alvo: acs.found.disability-models }
  - { tipo: complementa, alvo: acs.br.emag-and-nbr-17225 }
  - { tipo: complementa, alvo: acs.br.pneepei-and-aee }
  - { tipo: complementa, alvo: acs.br.libras }
  - { tipo: relacionado-a, alvo: acs.at.classification-iso-9999 }
  - { tipo: relacionado-a, alvo: acs.std.wcag }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
termos: [Lei Brasileira de Inclusão, Estatuto da Pessoa com Deficiência, pessoa com deficiência, avaliação biopsicossocial, acessibilidade, barreiras nas comunicações e na informação, barreiras tecnológicas, adaptações razoáveis, tecnologia assistiva, profissional de apoio escolar, formatos acessíveis, símbolo de acessibilidade, comunicação aumentativa e alternativa de baixa tecnologia]
---

# Lei Brasileira de Inclusão (Lei 13.146/2015)

## Definição e terminologia

A Lei 13.146, de 6 de julho de 2015, "Lei Brasileira de Inclusão da Pessoa com Deficiência (Estatuto da Pessoa com Deficiência)", é o estatuto geral dos direitos da pessoa com deficiência no Brasil. Entrou em vigor "após decorridos 180 (cento e oitenta) dias de sua publicação oficial" [F: lei131462015, art. 127]. Texto consultado no Planalto, versão compilada, em 30/10/2026, com alterações posteriores anotadas, entre elas a Lei 15.249/2025 (comunicação aumentativa e alternativa) [F: lei152492025].

Ela adota o conceito da Convenção sobre os Direitos das Pessoas com Deficiência, promulgada pelo Decreto 6.949/2009 "conforme o procedimento do § 3º do art. 5º da Constituição", isto é, com status de emenda constitucional [F: decreto69492009, preâmbulo]. Pessoa com deficiência é "aquela que tem impedimento de longo prazo" de natureza física, mental, intelectual ou sensorial que, em interação com barreiras, pode obstruir a participação plena [F: lei131462015, art. 2]. A avaliação, quando necessária, é biopsicossocial, feita por equipe multiprofissional [F: lei131462015, art. 2, §1]. O conceito e os modelos de deficiência ficam em `acs.found.disability-models`; este documento trata do que a lei obriga.

Definições do art. 3 relevantes para ambientes digitais de aprendizagem [F: lei131462015, art. 3]:

- **acessibilidade** (I): "possibilidade e condição de alcance para utilização, com segurança e autonomia", inclusive de "informação e comunicação, inclusive seus sistemas e tecnologias";
- **tecnologia assistiva ou ajuda técnica** (III): "produtos, equipamentos, dispositivos, recursos, metodologias, estratégias, práticas e serviços" que promovam funcionalidade e participação;
- **barreiras nas comunicações e na informação** (IV, d): entraves que dificultem "a expressão ou o recebimento de mensagens e de informações por intermédio de sistemas de comunicação e de tecnologia da informação"; **barreiras tecnológicas** (IV, f): "as que dificultam ou impedem o acesso da pessoa com deficiência às tecnologias";
- **adaptações razoáveis** (VI): ajustes "que não acarretem ônus desproporcional e indevido, quando requeridos em cada caso";
- **profissional de apoio escolar** (XIII): quem exerce "atividades de alimentação, higiene e locomoção" e atua nas atividades escolares em que for necessário.

O que não é: a LBI não é norma técnica. Ela não fixa critérios de sucesso, níveis de conformidade nem versão de diretriz; remete às "melhores práticas e diretrizes de acessibilidade adotadas internacionalmente" [F: lei131462015, art. 63].

## Problema que resolve

Antes da LBI, a acessibilidade digital estava em decreto e alcançava sobretudo a administração pública: o Decreto 5.296/2004 tornou obrigatória "a acessibilidade nos portais e sítios eletrônicos da administração pública" para pessoas com deficiência visual [F: decreto52962004, art. 47]. A LBI estende a obrigação a empresas privadas com sede ou representação no país, alarga o escopo para todas as deficiências e articula o dever de acessibilidade com o direito à educação inclusiva [I]. A LBI também reescreveu a Lei 10.098/2000 (Lei da Acessibilidade): o art. 2, IX, incluído em 2015, define comunicação como forma de interação que abrange "as línguas, inclusive a Língua Brasileira de Sinais", além de Braille, linguagem simples e comunicação aumentativa e alternativa; e o art. 17, na redação da Lei 15.249/2025, manda o poder público promover "a eliminação de barreiras na comunicação" para pessoas com necessidades complexas de comunicação [F: lei100982000, arts. 2 e 17].

## Fundamentos e funcionamento

### Educação (arts. 27 a 30)

A educação é direito da pessoa com deficiência, assegurados sistema educacional inclusivo em todos os níveis e aprendizado ao longo da vida [F: lei131462015, art. 27]. O art. 28 lista dezenove incumbências do poder público, entre elas: aprimoramento dos sistemas educacionais para garantir "condições de acesso, permanência," participação e aprendizagem (II); projeto pedagógico que institucionalize o atendimento educacional especializado (III); educação bilíngue, com Libras como primeira língua (IV); medidas individualizadas e coletivas (V); estudo de caso e plano de atendimento educacional especializado (VII); "oferta de ensino da Libras, do Sistema Braille e de uso de recursos de tecnologia assistiva" (XII); acesso a jogos e atividades recreativas no sistema escolar (XV); e, desde a Lei 15.249/2025, "sistemas de comunicação aumentativa e alternativa de baixa tecnologia para o atendimento educacional especializado" (XIX) [F: lei131462015, art. 28; lei152492025].

O §1 do art. 28 é decisivo para o setor privado: às instituições privadas "aplica-se obrigatoriamente o disposto nos incisos I, II, III, V, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII e XVIII", "sendo vedada a cobrança de valores adicionais de qualquer natureza" em mensalidades e matrículas [F: lei131462015, art. 28, §1]. Ficam fora do §1 os incisos IV (educação bilíngue), VI (pesquisa) e XIX (CAA de baixa tecnologia) [I, leitura da lista]. O art. 29 foi vetado. O art. 30 obriga instituições de ensino superior e de educação profissional e tecnológica, públicas e privadas, a oferecer em processos seletivos formulário para indicar recursos de acessibilidade, provas em formatos acessíveis, tecnologia assistiva, tempo adicional mediante solicitação e tradução do edital em Libras [F: lei131462015, art. 30].

### Acessibilidade digital (art. 63) e formatos acessíveis (art. 68)

"É obrigatória a acessibilidade nos sítios da internet mantidos por empresas com sede ou representação comercial no País ou por órgãos de governo, para uso da pessoa com deficiência, garantindo-lhe acesso às informações disponíveis, conforme as melhores práticas e diretrizes de acessibilidade adotadas internacionalmente" [F: lei131462015, art. 63]. "Os sítios devem conter símbolo de acessibilidade em destaque" [F: lei131462015, art. 63, §1].

O art. 68 define **formatos acessíveis** como "os arquivos digitais que possam ser reconhecidos e acessados por softwares leitores de telas ou outras tecnologias assistivas", "permitindo leitura com voz sintetizada, ampliação de caracteres, diferentes contrastes e impressão em Braille" [F: lei131462015, art. 68, §2]; obriga o poder público a excluir de compras de livros editoras "que não ofertem sua produção também em formatos acessíveis" [F: lei131462015, art. 68, §1]; e manda apoiar artigos científicos "em formato acessível, inclusive em Libras" [F: lei131462015, art. 68, §3].

### Tecnologia assistiva (arts. 74 e 75)

É garantido acesso a "produtos, recursos, estratégias, práticas, processos, métodos e serviços de tecnologia assistiva que maximizem sua autonomia, mobilidade pessoal e qualidade de vida" [F: lei131462015, art. 74]. O art. 75 obriga o poder público a um plano de medidas renovado a cada quatro anos (crédito, importação, pesquisa, desoneração, inclusão no rol do SUS) [F: lei131462015, art. 75]. Ambos se dirigem ao Estado; não criam dever direto para fornecedores de plataformas [I].

## Requisitos e pressupostos

O art. 63 está em vigor, mas sem regulamento técnico: em 29/08/2025 o Ministério Público Federal registrou que "o artigo 63 do texto ainda não foi objeto de um ato normativo" e recomendou à Secretaria de Governo Digital regulamentá-lo em 45 dias; a Secretaria indicou edição "até 31 de dezembro" de 2025 [F: mpf2025art63]. Não localizei esse ato em buscas feitas em 30/10/2026 (ver Lacunas). Para a administração pública federal há parâmetro técnico compulsório desde 2007, o eMAG [F: slti2007portaria3, art. 1, §1]; a ABNT NBR 17225:2025 é norma voluntária [F: abnt2025nbr17225, metadados] (ver `acs.br.emag-and-nbr-17225`).

## Alternativas e comparações

Quadro de obrigatoriedade para plataformas educacionais digitais (legislação federal; texto vigente em 30/10/2026). "Obrigatório" significa dever posto em lei, decreto ou ato normativo; "recomendado" significa norma voluntária ou dispositivo que só manda "buscar implementar".

| Requisito | Dispositivo | Natureza | A quem se aplica |
|---|---|---|---|
| Sítios acessíveis "conforme as melhores práticas" internacionais | LBI art. 63, caput | Obrigatório, sem regulamento técnico [F: mpf2025art63] | Empresas com sede ou representação no país; órgãos de governo |
| Símbolo de acessibilidade em destaque | LBI art. 63, §1; Dec. 5.296 art. 47, §2 | Obrigatório | Idem; portais da administração pública |
| Portais da administração pública acessíveis | Dec. 5.296/2004 art. 47 [F: decreto52962004] | Obrigatório | Administração pública |
| eMAG 3.1 | Portaria SLTI 3/2007 art. 1, §1 | Obrigatório (compulsório) | Órgãos do SISP (APF direta, autárquica, fundacional) |
| eMAG 3.1 | Portaria SLTI 3/2007 art. 1, §2 | Adesão voluntária | Estados, municípios, DF e pessoas jurídicas privadas que se relacionam eletronicamente com a APF |
| ABNT NBR 17225:2025 | Norma técnica | Recomendado (voluntária) [F: mpf2025art63] | Qualquer organização |
| Acesso, permanência, aprendizagem; AEE no projeto pedagógico; ensino de Libras, Braille e TA; apoio escolar | LBI art. 28, II, III, XII, XVII | Obrigatório | Poder público e, pelo §1, instituições privadas, sem cobrança adicional |
| Educação bilíngue (Libras L1) | LBI art. 28, IV; LDB arts. 60-A e 60-B [F: lei93941996] | Obrigatório | Poder público e sistemas de ensino; não incluído no §1 para privadas |
| Processo seletivo acessível, edital em Libras | LBI art. 30 | Obrigatório | IES e EPT públicas e privadas |
| Livros em formato acessível nas compras públicas | LBI art. 68, §1 | Obrigatório | Poder público comprador |
| Não recusar matrícula de aluno com TEA ou deficiência | Lei 12.764/2012 art. 7 | Obrigatório, multa de 3 a 20 salários-mínimos | "O gestor escolar, ou autoridade competente" [F: lei127642012, art. 7] |
| Acompanhamento de dislexia e TDAH | Lei 14.254/2021 arts. 1 a 3 | Obrigatório | Poder público; escolas públicas e privadas de educação básica [F: lei142542021, art. 2] |
| AEE, estudo de caso, PAEE e PEI sem exigência de laudo | Dec. 12.686/2025 arts. 11 e 12; Portaria MEC 421/2026 art. 7 | Obrigatório | Sistemas e redes de ensino [F: decreto126862025; mecportaria4212026] |
| Tradutor-intérprete, equipamentos e TIC para surdos | Dec. 5.626/2005 arts. 14, 21, 23 | Obrigatório para instituições federais; "buscarão implementar" para privadas e demais públicas | [F: decreto56262005, arts. 14 §3 e 23 §2] |
| Janela de Libras e legenda oculta | Dec. 5.626/2005 art. 24 | Obrigatório ("deve dispor") | Cursos de nível médio e superior a distância |
| Libras em vídeos e áudios | eMAG 3.1, recomendações 5.1 e 5.2 | Recomendado ("desejável") | Escopo do eMAG |
| Plano de TA, crédito e desoneração | LBI arts. 74 e 75 | Obrigatório | Poder público |

## Vantagens e limitações

A LBI dá base legal direta, exigível judicialmente, inclusive contra empresas privadas, e um vocabulário (barreira, adaptação razoável, tecnologia assistiva) coerente com a Convenção [I]. Limitações: o art. 63 fala em "sítios da internet", sem mencionar aplicativos; não define critério técnico nem prazo; e o símbolo do §1 não tem modelo fixado na lei [I]. O alcance a uma plataforma educacional privada que não seja "sítio" depende de interpretação [H].

## Exemplo técnico independente de domínio

Lista de verificação de enquadramento legal, em pseudocódigo:

```
para cada serviço digital S:
  se S é sítio web e o mantenedor é órgão de governo ou empresa com sede/representação no Brasil:
      exigir acessibilidade (LBI 63) + símbolo em destaque (63 §1)
      se o mantenedor integra o SISP: exigir eMAG 3.1 (Portaria 3/2007)
      referência técnica sugerida: NBR 17225 (voluntária)
  se S apoia escolarização (escola pública ou privada):
      prever recursos de acessibilidade e TA sem custo adicional (LBI 28 §1)
      não condicionar apoio a laudo (Dec. 12.686 art. 11 §7)
  se S oferece curso médio/superior a distância:
      janela de Libras + legenda oculta (Dec. 5.626 art. 24)
```

## Relações com outros conceitos

Depende de `acs.found.barriers-and-reasonable-accommodation` para os conceitos de barreira e adaptação razoável. Complementa `acs.br.emag-and-nbr-17225` (parâmetros técnicos), `acs.br.pneepei-and-aee` (política e AEE) e `acs.br.libras`. A definição legal de tecnologia assistiva dialoga com `acs.at.classification-iso-9999`. O "melhores práticas internacionais" do art. 63 aponta, na prática, para `acs.std.wcag` [I]. Dados de estudantes com deficiência coletados em PAEE e PEI seguem `psg.legal.lgpd-children`.

## Lacunas e questões abertas

- Não localizei, até 30/10/2026, decreto ou portaria federal que regulamente o art. 63 da LBI; buscas no Planalto e na imprensa oficial não retornaram ato. Deve ser reverificado no DOU.
- Projeto de lei que estenderia o art. 63 a aplicativos foi visto só em resultado de busca, sem abrir; não citado.
- Normas estaduais de São Paulo: não verifiquei decreto de política estadual de educação especial no site da ALESP ou no Diário Oficial; ver `acs.br.pneepei-and-aee` para o que foi verificado.
- O texto da página do Planalto aparece com codificação corrompida; as citações restauram acentos, conforme o próprio leitor relatou.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| lei131462015 | normativo | 2026-10-30 |
| lei100982000 | normativo | 2026-10-30 |
| decreto52962004 | normativo | 2026-10-30 |
| lei152492025 | normativo | 2026-10-30 |
| lei127642012 | normativo | 2026-10-30 |
| lei142542021 | normativo | 2026-10-30 |
| lei93941996 | normativo | 2026-10-30 |
| decreto69492009 | normativo | 2026-10-30 |
| decreto56262005 | normativo | 2026-10-30 |
| decreto126862025 | normativo | 2026-10-30 |
| mecportaria4212026 | normativo (via sistema MECNormas) | 2026-10-30 |
| slti2007portaria3 | normativo | 2026-10-30 |
| abnt2025nbr17225 | normativo [metadados] | 2026-10-30 |
| mpf2025art63 | tecnico (notícia oficial do MPF) | 2026-10-30 |
