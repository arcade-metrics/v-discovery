---
id: psg.deid.anonymization-and-pseudonymization
titulo: Anonimização e pseudonimização
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, anpd2023anonimizacaojuridica, anpd2023anonimizacaoprocesso, anpd2024notatecnica6, anpd2023guiapesquisa, nist2023sp800188, iso20889v2018, iso27559v2022]
relacoes:
  - { tipo: especificado-por, alvo: iop.br.lgpd }
  - { tipo: depende-de, alvo: psg.deid.reidentification-risk }
  - { tipo: complementa, alvo: psg.deid.k-anonymity-and-extensions }
  - { tipo: complementa, alvo: psg.deid.differential-privacy }
  - { tipo: complementa, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: complementa, alvo: psg.sec.encryption-and-key-management }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.audit.ripd-dpia }
termos: [anonimização, dado anonimizado, pseudonimização, desidentificação, identificador direto, identificador indireto, quase-identificador, meios técnicos razoáveis, meios próprios, esforços razoáveis, reversibilidade, dado agregado, dado sintético]
---

# Anonimização e pseudonimização

## Definição e terminologia

A LGPD (Lei 13.709/2018, redação vigente consultada no Planalto em 2026-10-29) define **dado anonimizado** como "dado relativo a titular que não possa ser identificado", considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento [F: brasil2018lgpd, art. 5, III]. Define **anonimização** como a utilização de meios técnicos razoáveis e disponíveis no momento do tratamento por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo [F: brasil2018lgpd, art. 5, XI]. A **pseudonimização** aparece apenas no art. 13 §4: é o tratamento por meio do qual um dado perde a possibilidade de associação direta ou indireta a um indivíduo, "senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro" [F: brasil2018lgpd, art. 13, §4].

A literatura técnica usa o termo guarda-chuva **desidentificação** (*de-identification*). O NIST SP 800-188 (versão final, setembro de 2023) o define como "general term for any process of removing the association between a set of identifying data and the data subject", reserva *anonymization* para processos irreversíveis e, por considerar o termo enganoso (muitos processos ditos irreversíveis podem ser revertidos se surgir um dataset auxiliar), recomenda evitar a palavra e usar *de-identification* [F: nist2023sp800188, §2.2]. O mesmo documento define *pseudonymization* (a partir da ISO 25237) como o tipo particular de desidentificação que remove a associação com o titular e adiciona uma associação entre um conjunto de características e um ou mais pseudônimos; observa que ela é usada para que múltiplas observações do mesmo indivíduo ao longo do tempo possam ser casadas e para permitir reidentificação quando houver razão de política, e que a existência do pseudônimo "frequently increases the risk of re-identification through other means" [F: nist2023sp800188, §2.2].

A ISO/IEC 20889:2018 ("Privacy enhancing data de-identification terminology and classification of techniques", edição 1.0, 2018-11-06, 46 páginas) fornece o vocabulário e classifica as técnicas de desidentificação pelas suas características e pela aptidão para reduzir o risco de reidentificação, para controladores e operadores de PII, em alinhamento com os princípios da ISO/IEC 29100 [F: iso20889v2018, metadados]. A ISO/IEC 27559:2022 ("Privacy enhancing data de-identification framework", edição 1, 2022-11) "provides a framework for identifying and mitigating re-identification risks and risks associated with the lifecycle of de-identified data" [F: iso27559v2022, metadados]. Nenhuma das duas foi lida em texto integral nesta sessão.

Vocabulário operacional usado pela ANPD em seus estudos técnicos: **identificador direto** é o dado que por si só identifica unicamente uma pessoa natural (nome completo, CPF); **identificador indireto** é o que, sozinho, não identifica, mas pode ser agregado e vinculado a dados auxiliares para identificar (idade, CEP) [F: anpd2023anonimizacaoprocesso, apêndice I; anpd2024notatecnica6, §4.3, registra a inclusão do conceito de "dados auxiliares" na minuta do guia]. A literatura de k-anonimato chama o conjunto de identificadores indiretos de **quase-identificador** (ver `psg.deid.k-anonymity-and-extensions`).

O que anonimização **não é**: não é a simples remoção de nome e documento (isso é desidentificação ingênua, vulnerável a ligação com bases externas, ver `psg.deid.reidentification-risk`); não é criptografia nem hashing de identificadores diretos, que o NIST não recomenda como técnica de desidentificação, porque a chave pode vazar e hashes sem chave podem ser revertidos por força bruta [F: nist2023sp800188, §4.3.2]; e não é um estado binário: a ANPD afirma que a anonimização "não pode ser entendida como um processo discreto com dois estados distintos" e sim como "um processo contínuo baseado em riscos" [F: anpd2023anonimizacaoprocesso, §2.3].

## Problema que resolve

O art. 12 da LGPD determina que dados anonimizados não são considerados dados pessoais para os fins da lei, salvo quando o processo de anonimização for revertido "utilizando exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido" [F: brasil2018lgpd, art. 12, caput]. O §1 lista fatores objetivos para determinar o que é razoável: "custo e tempo necessários para reverter o processo de anonimização, de acordo com as tecnologias disponíveis, e a utilização exclusiva de meios próprios"; o §2 estende a condição de dado pessoal aos dados usados para formação de perfil comportamental de pessoa natural identificada; e o §3 autoriza a ANPD a dispor sobre padrões e técnicas de anonimização e a realizar verificações de segurança, ouvido o Conselho Nacional de Proteção de Dados Pessoais [F: brasil2018lgpd, art. 12, §1 a §3].

A anonimização é, portanto, a porta pela qual um dataset deixa o regime da LGPD. Para pesquisa, a lei a trata como medida desejável e não impositiva: os arts. 7, IV e 11, II, "c" autorizam estudos por órgão de pesquisa "garantida, sempre que possível, a anonimização" dos dados pessoais e dos dados sensíveis; o art. 13 exige, em estudos de saúde pública, tratamento exclusivamente dentro do órgão, ambiente controlado e seguro, vedação de transferência a terceiros e "sempre que possível, a anonimização ou pseudonimização"; e o art. 18, IV dá ao titular o direito de requerer anonimização de dados desnecessários ou excessivos [F: brasil2018lgpd, arts. 7, 11, 13 e 18; redação dos arts. 7, IV e 11, II, "c" conferida também em anpd2023guiapesquisa]. O guia orientativo da ANPD sobre pesquisa (versão 1.0, junho de 2023) conclui que "a anonimização ou a pseudonimização de dados pessoais não foram instituídas pela LGPD como medidas de segurança impositivas", nem como condição técnica para divulgação ou compartilhamento para pesquisa, mas que os parâmetros do art. 13 devem ser aplicados, no que couber, a pesquisas de outras áreas, especialmente com dados sensíveis [F: anpd2023guiapesquisa, p. 15-16 e 41]. O mesmo guia lembra que o tratamento de dados de crianças e adolescentes em pesquisa "deverá ser realizado sempre em seu melhor interesse", nos termos da LGPD e do ECA [F: anpd2023guiapesquisa, seção sobre estudos e pesquisas].

## Fundamentos e funcionamento

**Abordagem jurídica.** O estudo técnico jurídico da ANPD (versão 1.0, novembro de 2023) lê o art. 12 como adoção de uma "teoria objetiva do conceito amplo de dado pessoal", em que a possibilidade de reidentificação é avaliada tanto pelos meios próprios do agente quanto pelos meios e esforços razoáveis de terceiros; "meios próprios" são "as habilidades, os dados, instrumentos e técnicas disponíveis ao próprio agente de tratamento"; e a licitude dos meios é fator objetivo, de modo que crimes cibernéticos ou violação de contratos e políticas internas configuram esforços irrazoáveis [F: anpd2023anonimizacaojuridica, §3.4 e §4.4]. O estudo conclui que (a) a anonimização é processo, jurídico e técnico; (b) o ato inicial do processo é operação de tratamento, sujeita a finalidade e adequação; (c) há "consenso científico sobre a impraticabilidade de um cenário de ausência de risco de reidentificação"; (d) a anonimização não é medida impositiva; (e) o critério dos esforços razoáveis exige análise de riscos; e (f) a avaliação deve seguir um modelo baseado em riscos [F: anpd2023anonimizacaojuridica, §4.3 e considerações finais]. O estudo cita a Nota Técnica 46/2022/CGF/ANPD sobre microdados do INEP, segundo a qual a avaliação de reversão "deve se basear em evidências e em cenários que considerem aspectos objetivos da realidade", afastando cenários irreais ou que desconsiderem custos muito elevados [F: anpd2023anonimizacaojuridica, nota 61].

**Abordagem de processo.** O estudo técnico computacional da ANPD propõe etapas mínimas: definir o Risco de Reidentificação Aceitável (RRA) para o conjunto, dependente do contexto (dados sensíveis ou financeiros reduzem o limite); aplicar o conjunto de técnicas; medir o Risco de Reidentificação Mensurado (RRM) como probabilidade entre 0 e 1, majorado quando a base é pública ou compartilhada; comparar RRM com RRA, reiniciando o processo se RRM > RRA; e acompanhar operações posteriores (inclusão, alteração, deleção) que modifiquem o risco [F: anpd2023anonimizacaoprocesso, §2.3]. O estudo também exige documentação do processo, que dê uma "trilha dos estados que o conjunto de dados assumiu" [F: anpd2023anonimizacaoprocesso, §2.2].

**Famílias de técnicas.** A ANPD lista supressão, generalização, perturbação e permutação como técnicas para dados textuais estruturados, e observa que são limitadas para dados em fluxo, imagens e outros formatos não tabulares [F: anpd2023anonimizacaoprocesso, §2.4]. O NIST organiza a desidentificação em remoção ou transformação de identificadores diretos, transformação de quase-identificadores numéricos (*top/bottom coding*, microagregação), datas, localização, genoma, texto livre, e aponta desafios de agregação, alta dimensionalidade, dados ligados e composição [F: nist2023sp800188, §4.3]. Alternativas que não produzem microdados: dados sintéticos (parcial ou totalmente sintéticos, com ou sem validação, eventualmente gerados com privacidade diferencial) e interfaces de consulta interativa com ruído [F: nist2023sp800188, §4.4 e §4.5].

**Pseudonimização como técnica de segurança, não de saída do regime.** O art. 13 §4 condiciona a pseudonimização à "informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro" [F: brasil2018lgpd, art. 13, §4]: o dado pseudonimizado continua pessoal para o controlador, que detém o meio próprio de reversão (a chave) [I, leitura direta do art. 12 combinado com o art. 13 §4]. Isso faz da gestão da chave uma questão de segurança da informação, tratada em `psg.sec.encryption-and-key-management`.

## Requisitos e pressupostos

- Inventário dos atributos com classificação em identificador direto, indireto (quase-identificador) e sensível, feito por quem conhece as bases auxiliares disponíveis; o NIST alerta que "all information is potentially identifying information" e que a distinção exige especialista [F: nist2023sp800188, §2.2].
- Limite de risco aceitável definido antes da aplicação das técnicas, e não ajustado depois para caber no resultado [F: anpd2023anonimizacaoprocesso, §2.3].
- Modelo de compartilhamento decidido junto com o nível de desidentificação (publicação aberta, acordo de uso, enclave), porque quem acessa e como altera o risco esperado [F: nist2023sp800188, §3.4].
- Para pseudonimização: chave e tabela de correspondência fora do dataset, com controle de acesso e registro [F: brasil2018lgpd, art. 13, §4].
- Reavaliação periódica: a ANPD afirma que a avaliação "não pode ser episódica, mas sim iterativa", pois novos riscos surgem com avanços tecnológicos e novos dados auxiliares [F: anpd2023anonimizacaojuridica, §4.3].

## Vantagens e limitações

A anonimização bem documentada retira o dataset do regime da LGPD (art. 12) e viabiliza compartilhamento para pesquisa sem base legal adicional; a pseudonimização preserva a capacidade de ligar observações do mesmo indivíduo ao longo do tempo, essencial para séries de interação, e de atender direitos do titular [F: nist2023sp800188, §2.2]. Como limitações: o risco nunca é zero [F: anpd2023anonimizacaojuridica, §4.3]; técnicas de supressão e generalização reduzem a utilidade e podem introduzir viés não ignorável [F: nist2023sp800188, §2.2, verbete *redaction*]; e a pseudonimização, por manter a ligação longitudinal, aumenta o risco de reidentificação por outros meios [F: nist2023sp800188, §2.2]. A qualificação jurídica de "esforços razoáveis" é conceito jurídico indeterminado, o que a própria ANPD reconhece [F: anpd2023anonimizacaojuridica, §4.4].

## Alternativas e comparações

| Saída do processo | Reversível pelo controlador | Sai do regime da LGPD | Preserva ligação longitudinal | Garantia formal |
|---|---|---|---|---|
| Pseudonimização (art. 13 §4) | Sim, pela chave separada | Não | Sim | Não |
| Microdados anonimizados (supressão, generalização; k-anonimato) | Não, se bem feito | Sim, sob o teste do art. 12 | Parcial (pseudônimo por período, se houver) | Não; risco medido empiricamente |
| Dados agregados ou sintéticos com privacidade diferencial | Não | Sim, sob o mesmo teste | Não (não há microdado) | Sim, limite matemático de perda de privacidade |
| Enclave ou interface de consulta | Dado original fica no enclave | Não para o dado interno; sim para as saídas vetadas | Sim, internamente | Depende do mecanismo de resposta |

A tabela sintetiza [F: brasil2018lgpd, arts. 12 e 13] e [F: nist2023sp800188, §3.4, §4.4 e §4.5]; a coluna "sai do regime" é interpretação [I] do art. 12.

## Métricas e métodos de avaliação

A métrica central é o risco de reidentificação, tratado em `psg.deid.reidentification-risk`: tamanho da classe de equivalência (k), probabilidade de reidentificação em cenários de promotor e jornalista, estudos de reidentificação com intruso motivado e, para mecanismos com ruído, o parâmetro epsilon. A ANPD exige que o risco mensurado seja expresso como probabilidade e comparado ao limite aceitável [F: anpd2023anonimizacaoprocesso, §2.3]. A utilidade deve ser medida junto: o NIST recomenda validar se a acurácia do dado desidentificado é suficiente para o uso pretendido [F: nist2023sp800188, §4.6.1].

## Exemplo técnico independente de domínio

```
procedimento desidentificar(dataset D, finalidade F, modelo_de_compartilhamento M):
    classificar cada atributo de D em {direto, quase_identificador, sensivel, outro}
    RRA := limite_de_risco(F, M, ha_dados_sensiveis(D), ha_menores(D))   # etapa 1 (ANPD)
    se F exige ligar observações do mesmo titular ao longo do tempo:
        chave := gerar_chave_aleatoria(); guardar(chave, cofre_separado, acesso_restrito)
        D.id_titular := pseudonimo(chave, D.id_titular)      # continua dado pessoal
    senão:
        remover(D, atributos diretos)
    para cada atributo q em quase_identificadores:
        generalizar_ou_suprimir(D, q, hierarquia[q])        # etapa 2
    RRM := medir_risco(D, cenario in {promotor, jornalista}, bases_auxiliares_conhecidas)   # etapa 3
    se RRM > RRA: ajustar hierarquias; voltar à etapa 2
    registrar(trilha: atributos, técnicas, parâmetros, RRA, RRM, data, responsável)
    agendar reavaliação(D) a cada nova release, nova base auxiliar ou alteração de D
```

## Relações com outros conceitos

Especificado pelo texto legal documentado em `iop.br.lgpd`; depende de `psg.deid.reidentification-risk` para o teste de reversibilidade do art. 12; complementa `psg.deid.k-anonymity-and-extensions` e `psg.deid.differential-privacy`, que são as duas famílias de garantia aqui comparadas; complementa `psg.access.minimization-and-privacy-by-design` (coletar menos reduz o que precisa ser anonimizado) e `psg.sec.encryption-and-key-management` (guarda da chave de pseudonimização); relaciona-se com `psg.legal.lgpd-children` (melhor interesse em pesquisa com menores) e `psg.audit.ripd-dpia` (o processo documentado é insumo do relatório de impacto).

## Lacunas e questões abertas

- O "Guia de Anonimização e Pseudonimização" da ANPD foi submetido a consulta pública em 2024 como estudo preliminar, com quatro apêndices (esclarecimentos, caderno de técnicas, técnicas de mensuração de risco como k-anonimização e estudos de caso) [F: anpd2024notatecnica6, §4.9 a §4.12]; na página de materiais da ANPD consultada em 2026-10-29 não consta versão final publicada. O texto da minuta não foi lido em fonte oficial; só a nota técnica de abertura e os dois estudos técnicos.
- ISO/IEC 20889 e 27559 foram confirmadas apenas por metadados de catálogo; a classificação de técnicas da 20889 e o fluxo de avaliação da 27559 não foram verificados no texto.
- A LGPD não define "dado agregado" nem "dado sintético"; se e quando esses produtos passam pelo teste do art. 12 permanece questão interpretativa [H].
- O art. 12 §2 (perfil comportamental de pessoa identificada) tem implicação direta para modelos de aluno construídos a partir de dados de interação, ainda sem orientação específica da ANPD localizada nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| anpd2023anonimizacaojuridica | tecnico | 2026-10-29 |
| anpd2023anonimizacaoprocesso | tecnico | 2026-10-29 |
| anpd2024notatecnica6 | tecnico | 2026-10-29 |
| anpd2023guiapesquisa | tecnico | 2026-10-29 |
| nist2023sp800188 | tecnico | 2026-10-29 |
| iso20889v2018 | normativo (somente metadados) | 2026-10-29 |
| iso27559v2022 | normativo (somente metadados) | 2026-10-29 |
