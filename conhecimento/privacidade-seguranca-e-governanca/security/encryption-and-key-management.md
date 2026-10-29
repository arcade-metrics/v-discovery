---
id: psg.sec.encryption-and-key-management
titulo: Criptografia em trânsito e em repouso e gestão de chaves
tipo: tecnica
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [nist2020sp80057, nist2020sp800175b, nist2019fips1403, owasp2026cryptostorage, rfc8446, brasil2018lgpd, anpd152024, anpd2026cis, anpd2021pequenoporte]
relacoes:
  - { tipo: complementa, alvo: psg.sec.threat-model-education }
  - { tipo: complementa, alvo: psg.sec.incident-management }
  - { tipo: complementa, alvo: psg.sec.iso-27001-and-27701 }
  - { tipo: depende-de, alvo: rtm.sec.transport-security }
  - { tipo: complementa, alvo: rtm.sec.authentication }
  - { tipo: complementa, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: complementa, alvo: psg.access.rbac-and-abac }
  - { tipo: complementa, alvo: psg.audit.audit-trails }
termos: [dados em repouso, dados em trânsito, chave de cifra de dados (DEK), chave de cifra de chaves (KEK), criptoperíodo, módulo criptográfico, HSM, AEAD, rotação de chave, re-keying, estado de chave, sanitização criptográfica, segregação de bases]
---

# Criptografia em trânsito e em repouso e gestão de chaves

## Definição e terminologia

Cifrar é transformar texto claro em texto cifrado de modo que só quem tem a chave recupere o original; o NIST descreve que a confidencialidade de dados é em geral provida por cifras de bloco simétricas, com AES aprovado nos três tamanhos de chave e o 3DES de três chaves ainda permitido, mas deprecado [F: nist2020sp800175b, §4.1]. **Dados em trânsito** são os que atravessam uma rede; **dados em repouso** são os armazenados. O guia da ANPD para agentes de pequeno porte adota explicitamente essa dupla, associando "segurança dos dados pessoais armazenados" a dados em repouso e "segurança das comunicações" a dados em trânsito [F: anpd2021pequenoporte, notas 10 e 12].

**Gestão de chaves** é o conjunto de funções que geram, distribuem, armazenam, trocam, arquivam e destroem chaves; a referência é o NIST SP 800-57 Parte 1, rev. 5 (maio de 2020), que cobre serviços de segurança, tipos de chave, proteções exigidas para cada tipo e funções de gestão [F: nist2020sp80057]. **Módulo criptográfico** é o componente (hardware, software ou firmware) que executa as operações; o FIPS 140-3 (março de 2019) define quatro níveis de segurança crescentes para esses módulos e se alinha à ISO/IEC 19790:2012 [F: nist2019fips1403]. Este documento não repete TLS, DTLS e QUIC, tratados em `rtm.sec.transport-security`; aqui entram o que fica em repouso, as chaves e a segregação de bases.

## Problema que resolve

A LGPD obriga os agentes a adotar "medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais" de acessos não autorizados e de destruição, perda, alteração ou difusão acidental ou ilícita, desde a concepção do produto [F: brasil2018lgpd, art. 46, §2]. A criptografia é a medida que, se bem gerida, muda o resultado de um incidente: o art. 48, §3, manda a autoridade considerar, no juízo de gravidade, a comprovação de medidas técnicas que tornem os dados afetados ininteligíveis a terceiros não autorizados [F: brasil2018lgpd, art. 48, §3], e a página da ANPD sobre comunicação de incidentes lista entre os fatores de avaliação "se os dados estavam protegidos (por exemplo, criptografia)" [F: anpd2026cis]; a própria comunicação à ANPD deve descrever "as medidas técnicas e de segurança utilizadas para a proteção dos dados pessoais, adotadas antes e após o incidente" [F: anpd152024, art. 6, §2, III]. A ANPD sugere ainda que quem armazena dados sensíveis implemente soluções que dificultem a identificação do titular, "como as técnicas de pseudonimização", dando a criptografia como exemplo [F: anpd2021pequenoporte, §46]. Mas cifra sem gestão de chaves é ilusão: o SP 800-57 lembra que informação protegida por criptografia "is secure only if the algorithms remain strong and the keys have not been compromised" [F: nist2020sp80057, §5.5].

## Fundamentos e funcionamento

### Tipos de chave e hierarquia

O SP 800-57 enumera 19 tipos de chave; os relevantes para dados em repouso são a **chave simétrica de cifra de dados** (aplica e remove confidencialidade; em modos autenticados, uma só chave faz autenticação e cifra), a **chave simétrica de envelopamento de chaves** (key-wrapping key, "sometimes called key-encrypting keys"), usada para cifrar outras chaves, e a **chave-mestra ou de derivação**, da qual se derivam chaves de dados ou de envelopamento [F: nist2020sp80057, §5.1.1]. O OWASP traduz isso em prática: a chave de dados (DEK) deve ser armazenada cifrada por uma chave de cifra de chaves (KEK) pelo menos tão forte quanto ela; chaves não entram no código-fonte nem no controle de versão; "where possible, encryption keys should be stored in a separate location from encrypted data"; e, quando houver, usam-se HSM, HSM virtual ou cofres de chave do provedor [F: owasp2026cryptostorage].

### Algoritmos e modos

O OWASP recomenda AES com chave de pelo menos 128 bits, idealmente 256; modos autenticados (GCM e CCM) como primeira preferência; se indisponíveis, CTR ou CBC com autenticação separada por Encrypt-then-MAC; ECB "should not be used outside of very specific circumstances"; RSA com pelo menos 2048 bits e padding OAEP; números aleatórios só de CSPRNG; e senhas nunca cifradas de forma reversível, mas processadas por hash de senha [F: owasp2026cryptostorage]. [I] Para dados de alunos, o ponto prático é que cifra autenticada (AEAD) protege também contra adulteração silenciosa, o que importa em cache offline e em sincronização.

### Criptoperíodo e rotação

"A cryptoperiod is the time span during which a specific key is authorized for use by legitimate entities"; defini-lo limita a quantidade de material disponível para criptanálise, a exposição se uma chave vazar e o tempo para ataques físicos ou procedimentais [F: nist2020sp80057, §5.3]. A duração depende da força do mecanismo e das consequências da exposição (sensibilidade e vida útil da informação, criticidade, custo de recuperação); criptoperíodos curtos "may be counter-productive" quando negação de serviço é a preocupação principal e a troca de chaves é propensa a erro [F: nist2020sp80057, §5.3.1-5.3.3]. A Tabela 1 traz sugestões por tipo, da ordem de uma única transação para chaves efêmeras a poucos anos; para a chave privada de assinatura, 1 a 3 anos [F: nist2020sp80057, tabela 1]. Trocar a chave pode ser **re-keying** (chave nova independente da antiga, obrigatória após comprometimento) ou **key update** (derivada da antiga) [F: nist2020sp80057, §8.2.3]. O OWASP lista os gatilhos de rotação (suspeita de comprometimento, fim do criptoperíodo, limite de uso do modo, mudança na segurança do algoritmo) e prefere, para dados existentes, decifrar e recifrar com a chave nova [F: owasp2026cryptostorage].

### Estados, armazenamento e comprometimento

Uma chave passa por estados: pré-ativação, ativa (proteger e/ou processar), suspensa, desativada (só processar), comprometida (só processar) e destruída; as transições costumam exigir registro em logs de auditoria e nos metadados da chave [F: nist2020sp80057, §7]. Chaves em repouso devem ser protegidas conforme a seção 6.1 da norma, com cópias em locais separados para disponibilidade; destruir a chave que decifra um grande volume é uma forma de **sanitização criptográfica** [F: nist2020sp80057, §6.2.2]. O SP 800-175B acrescenta que chaves podem viver só dentro de um módulo validado, ou ser envelopadas ou divididas em componentes, e que backup e arquivo exigem capacidade de recuperação restrita a entidades autorizadas [F: nist2020sp800175b, §5.4.3]. Diante de comprometimento, "all use of the key to apply cryptographic protection to information [...] shall cease, and the compromised key shall be revoked"; as medidas preventivas incluem minimizar o tempo da chave em claro, impedir que humanos a vejam, confiná-la a contêineres físicos (HSM, módulos), manter sistema de responsabilização por acesso, destruir chaves ao fim do uso e ter plano de recuperação; o sistema deve ser desenhado para que o comprometimento de uma chave "compromises as little data as possible", por exemplo, com uma chave por pessoa ou por grupo pequeno [F: nist2020sp80057, §5.5-5.5.2].

### Módulos validados

O FIPS 140-3 cobre onze áreas (especificação do módulo, interfaces, papéis e autenticação, segurança de software/firmware, ambiente operacional, segurança física, segurança não invasiva, gestão de parâmetros sensíveis, autotestes, garantia de ciclo de vida e mitigação de outros ataques) e é validado pelo CMVP; o próprio texto adverte que "conformance to this standard is not sufficient to ensure that a particular module is secure" e que a adoção está disponível a organizações privadas [F: nist2019fips1403]. O SP 800-175B pede algoritmos validados em módulos validados FIPS 140 [F: nist2020sp800175b, §5.4.5]; para uma plataforma educacional brasileira, isso é critério de escolha de biblioteca ou provedor, não obrigação legal [I].

### Segregação de bases

[I] Quando há uma base de operação (identificada) e uma de pesquisa (pseudonimizada), a gestão de chaves é o que torna a separação real: chaves distintas por base e por finalidade, chave de pseudonimização guardada fora da base de pesquisa e com acesso restrito, e KEKs separadas por ambiente. Isso segue o princípio do SP 800-57 de "using different keys for different purposes" para limitar o dano de um comprometimento [F: nist2020sp80057, §5.5]. A definição legal de pseudonimização, que exige informação adicional "mantida separadamente pelo controlador em ambiente controlado e seguro", é tratada em `psg.deid.anonymization-and-pseudonymization`.

## Requisitos e pressupostos

- Fonte de aleatoriedade criptográfica em todos os ambientes, inclusive no aparelho [F: owasp2026cryptostorage].
- Um lugar seguro para a KEK raiz (HSM, KMS do provedor ou módulo validado); sem ele, a hierarquia de chaves é só ofuscação [I].
- Inventário de chaves com metadados (tipo, estado, criptoperíodo, dono), porque as transições de estado devem ser registradas [F: nist2020sp80057, §7].
- Backups: o guia da ANPD recomenda cópias completas, regulares, em locais distintos e "não sincronizadas online (em tempo real)" para resistir a ransomware [F: anpd2021pequenoporte, §49]; backups cifrados precisam de backup da chave, ou são inúteis [I].

## Vantagens e limitações

Cifra em repouso com chaves bem geridas reduz a gravidade de um vazamento de mídia, backup ou aparelho e é reconhecida no juízo de gravidade do art. 48 [F: brasil2018lgpd, art. 48, §3]. Limites: o OWASP observa que "the best way to protect sensitive information is to not store it in the first place" e que a aplicação deve continuar segura "even if cryptographic controls fail" [F: owasp2026cryptostorage]; cifra não protege contra quem tem acesso legítimo à aplicação (ver `psg.access.rbac-and-abac`), nem contra credenciais roubadas (ver `rtm.sec.authentication`); e a camada escolhida define o que fica protegido: "Which layer(s) are most appropriate will depend on the threat model" [F: owasp2026cryptostorage].

## Alternativas e comparações

| Camada de cifra em repouso | Protege contra | Não protege contra | Observação |
|---|---|---|---|
| Disco/volume do servidor | roubo físico de mídia, descarte | qualquer acesso via SO ou banco | transparente; gestão de chave pelo provedor [I] |
| Banco (cifra transparente, TDE) | leitura de arquivos do banco e backups | consultas autorizadas, DBA | chave em KMS; não separa por finalidade [I] |
| Aplicação (por campo ou registro) | DBA, backups, outras aplicações | bug na própria aplicação | permite chave por escola, por base, por finalidade; busca e índice ficam limitados [I] |
| Aparelho (cache offline) | perda ou roubo do tablet | aluno com sessão aberta | chave por aparelho, apagamento remoto [F: anpd2021pequenoporte, §62] |

A escolha de camada é decisão do modelo de ameaças, não regra geral [F: owasp2026cryptostorage].

## Métricas e métodos de avaliação

Fração dos dados pessoais de menores cobertos por cifra em repouso, por camada; chaves fora do criptoperíodo; tempo entre suspeita de comprometimento e revogação; chaves com acesso humano em claro (deve ser zero) [F: nist2020sp80057, §5.5.2]; resultado de restauração de backup cifrado em teste periódico; uso de módulos validados quando exigido por contrato [I].

## Exemplo técnico independente de domínio

```text
# Hierarquia de chaves (política, não código)
KEK_raiz          : HSM/KMS; nunca exportável; rotação por criptoperíodo; acesso auditado
KEK_operacao      : envelopada por KEK_raiz; uma por ambiente (prod, homolog)
DEK_escola[e]     : envelopada por KEK_operacao; cifra registros da escola e; AES-256-GCM
DEK_pesquisa      : envelopada por KEK_pesquisa (distinta); base pseudonimizada
K_pseudo          : chave da função de pseudonimização; guardada fora da base de pesquisa
K_aparelho[d]     : derivada no aparelho d; cifra o cache offline; apagável remotamente

on_sync(lote, d):   verificar MAC do lote com K_aparelho[d]; rejeitar duplicatas por id
on_export_pesquisa: id_pseudo = PRF(K_pseudo, id_aluno); nunca copiar DEK_escola
on_suspeita(k):     estado(k) = comprometida; cessar proteção; re-keying; recifrar dados
on_descarte(d):     destruir K_aparelho[d]  # sanitização criptográfica (SP 800-57 §6.2.2)
```

## Relações com outros conceitos

Depende de `rtm.sec.transport-security` para o trânsito (TLS 1.3 fornece autenticação do servidor, confidencialidade e integridade do canal [F: rfc8446, §1]). Complementa `rtm.sec.authentication` (chaves de assinatura de tokens seguem a mesma gestão), `psg.deid.anonymization-and-pseudonymization` (a chave de pseudonimização é o segredo que separa as bases), `psg.access.rbac-and-abac` (cifra não substitui autorização), `psg.audit.audit-trails` (transições de estado de chave são eventos auditáveis) e `psg.sec.incident-management` (dado ininteligível muda a gravidade). Os requisitos de gestão vêm, no plano de sistema de gestão, de `psg.sec.iso-27001-and-27701`.

## Lacunas e questões abertas

- A Tabela 1 do SP 800-57 foi lida em extração de texto com alinhamento imperfeito; só o valor da chave privada de assinatura (1 a 3 anos) foi conferido com segurança.
- O SP 800-57 Parte 2 (política e planejamento) e Parte 3 não foram abertos.
- A página do OWASP não exibe data de versão; a chave usa o ano de consulta.
- Não foi localizada norma brasileira que obrigue módulos validados FIPS 140-3 ou equivalente para dados educacionais; a exigência do SP 800-175B é para o governo federal dos EUA.
- Fica aberta a relação entre cifra por campo e as necessidades de consulta analítica da base de pesquisa (ver `psg.deid.differential-privacy`).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nist2020sp80057 | normativo | 2026-10-29 |
| nist2020sp800175b | normativo | 2026-10-29 |
| nist2019fips1403 | normativo | 2026-10-29 |
| owasp2026cryptostorage | tecnico | 2026-10-29 |
| rfc8446 | normativo | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
| anpd152024 | normativo | 2026-10-29 |
| anpd2026cis | tecnico | 2026-10-29 |
| anpd2021pequenoporte | tecnico | 2026-10-29 |
