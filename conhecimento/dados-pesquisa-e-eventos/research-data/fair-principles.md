---
id: dat.rd.fair-principles
titulo: Princípios FAIR para dados de pesquisa
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [wilkinson2016fair, gofair2026fairprinciples, wilkinson2018fairmetrics, ec2016h2020fairdmp, scienceeurope2021rdmguide, fapesp2024faqpgd, zenodo2026aboutrecords, zenodo2026policies, dataverse2026datasetmgmt]
relacoes:
  - { tipo: complementa, alvo: dat.rd.data-management-plans }
  - { tipo: implementado-por, alvo: dat.rd.repositories-and-versioning }
  - { tipo: complementa, alvo: dat.rd.data-documentation }
  - { tipo: complementa, alvo: kg.std.prov-o }
  - { tipo: complementa, alvo: lae.dq.provenance-and-lineage }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: dat.ethics.research-vs-operation }
termos: [FAIR, findable, accessible, interoperable, reusable, machine-actionable, identificador persistente, metadados ricos, licença de uso de dados, proveniência, métrica FAIR, acesso controlado, metadados abertos, "as open as possible, as closed as necessary"]
---

# Princípios FAIR para dados de pesquisa

## Definição e terminologia

Os **princípios FAIR** são quatro desideratos (Findable, Accessible, Interoperable, Reusable) e suas elaborações, publicados em 2016 como "guideposts" para quem publica e preserva dados acadêmicos [F: wilkinson2016fair]. Os autores enfatizam que os princípios "precede implementation choices, and do not suggest any specific technology, standard, or implementation-solution; moreover, the Principles are not, themselves, a standard or a specification" [F: wilkinson2016fair, The Principles precede implementation]. O texto usa **machine-actionable** para "a continuum of possible states" em que um objeto digital fornece informação cada vez mais detalhada a um agente computacional autônomo [F: wilkinson2016fair]; a página da GO FAIR resume a ênfase como a capacidade de sistemas computacionais encontrarem, acessarem, interoperarem e reusarem dados "with none or minimal human intervention" [F: gofair2026fairprinciples].

O que FAIR não é: não é sinônimo de dado aberto. Os autores das métricas FAIR escrevem que "openness is not a requirement of FAIRness, since there are data that cannot be made public due to privacy or confidentiality reasons" [F: wilkinson2018fairmetrics]. Também não é medida de qualidade ou impacto: "the FAIR-compliance of a resource is distinct from its impact" [F: wilkinson2018fairmetrics].

## Problema que resolve

Dados de pesquisa gerados com dinheiro público costumam ficar em formatos e locais que impedem descoberta e reuso; o artigo original nota que financiadores, editores e agências passaram a exigir planos de gestão de dados, mas que "what constitutes 'good data management' is, however, largely undefined" [F: wilkinson2016fair, Introduction]. FAIR oferece um vocabulário comum para essa exigência, independente de disciplina, e coloca a máquina como usuário de primeira classe, porque volume e velocidade dos dados tornam a curadoria só humana inviável [F: wilkinson2016fair; gofair2026fairprinciples]. Para dados de interação de crianças com software educacional, o problema é duplo: tornar o dataset reusável por outros pesquisadores sem expor os titulares [I].

## Fundamentos e funcionamento

Os quinze subprincípios, na redação da GO FAIR, que coincide com a do Box 2 do artigo [F: gofair2026fairprinciples; wilkinson2016fair, Box 2]:

| Letra | Subprincípio (resumo) |
|---|---|
| F1 | (meta)dados recebem identificador global, único e persistente |
| F2 | dados descritos com metadados ricos (definidos por R1) |
| F3 | metadados incluem explicitamente o identificador do dado que descrevem |
| F4 | (meta)dados registrados ou indexados em recurso pesquisável |
| A1 | (meta)dados recuperáveis pelo identificador via protocolo de comunicação padronizado |
| A1.1 | protocolo aberto, gratuito e universalmente implementável |
| A1.2 | protocolo permite procedimento de autenticação e autorização, quando necessário |
| A2 | metadados acessíveis mesmo quando os dados não estão mais disponíveis |
| I1 | linguagem formal, acessível, compartilhada e amplamente aplicável para representação de conhecimento |
| I2 | vocabulários que seguem os princípios FAIR |
| I3 | referências qualificadas a outros (meta)dados |
| R1 | (meta)dados ricamente descritos com pluralidade de atributos precisos e relevantes |
| R1.1 | licença de uso de dados clara e acessível |
| R1.2 | proveniência detalhada |
| R1.3 | padrões comunitários do domínio |

Três subprincípios sustentam a conciliação com dados restritos: A1.2 admite autenticação e autorização no protocolo; A2 separa o destino dos metadados do destino dos dados; R1.1 exige licença clara, que pode ser restritiva [I]. O próprio artigo de 2016 dá como exemplo de "A" o Dataverse, que fornece interfaces de máquina para buscar, ler metadados e baixar arquivos "using a token to grant access when data files are restricted" [F: wilkinson2016fair, Examples of FAIRness].

### FAIR com dados de menores

A pergunta do brief (como conciliar FAIR com proteção de dados de menores) tem resposta direta nas fontes: separar metadados públicos de dados com acesso controlado. Wilkinson et al. (2018) afirmam que dados que não podem ser públicos "can reach a high level of FAIRness by, for example, providing public metadata describing the nature of the data source, and by providing a clear path by which data access can be requested" [F: wilkinson2018fairmetrics]. A Comissão Europeia formula a mesma ideia como política: o piloto de dados abertos do H2020 segue "as open as possible, as closed as necessary" e pede que o plano explique por que certos dados não podem ser compartilhados, "clearly separating legal and contractual reasons from voluntary restrictions", e como a identidade de quem acessa será verificada [F: ec2016h2020fairdmp, §1 e Anexo 1, 2.2]. O guia da Science Europe pede, para dados pessoais, consentimento informado para preservação e compartilhamento, consideração de anonimização e pseudonimização e explicação sobre "a managed access procedure in place for authorised users of personal data" [F: scienceeurope2021rdmguide, 4a]. A FAPESP admite o mesmo arranjo: se os dados não puderem ser divulgados por razões éticas ou legais, isso deve constar desde o início do plano, e "várias instituições permitem descrever os dados usando metadados, mesmo que os dados não possam ser disponibilizados" [F: fapesp2024faqpgd, III.5].

Os mecanismos concretos dos repositórios estão em `dat.rd.repositories-and-versioning`: no Zenodo, "metadata for all records in Zenodo are always publicly accessible" enquanto os arquivos podem ser restritos ou embargados [F: zenodo2026aboutrecords]; no Dataverse, arquivos restritos com termos de acesso e pedido de acesso, e embargos que publicam identificador e metadados mas negam os arquivos até a data final [F: dataverse2026datasetmgmt, Restricted Files + Terms of Access; Embargoes].

Consequência de projeto [I]: como os metadados ficam abertos e, no Zenodo, sob CC0 [F: zenodo2026policies, Metadata access and reuse], eles próprios não podem conter dado pessoal nem permitir reidentificação (escola pequena, turma, cidade, faixa etária estreita); a avaliação disso pertence a `psg.deid.reidentification-risk`. O que entra nos metadados abertos é decisão de minimização (`psg.access.minimization-and-privacy-by-design`), e a base legal e o consentimento parental, em `psg.legal.lgpd-children`.

## Vantagens e limitações

Vantagens: vocabulário aceito por financiadores e repositórios (H2020, Science Europe e FAPESP se referem a FAIR) [F: ec2016h2020fairdmp; scienceeurope2021rdmguide; fapesp2024faqpgd]; acomoda dados fechados sem abandonar descoberta e citação [F: wilkinson2018fairmetrics]. Limitações: os princípios são "aspirational" e geraram "a wide range of interpretations of FAIRness" [F: wilkinson2018fairmetrics]; não dizem o que é suficiente para dados de menores, nem tratam de risco de reidentificação via metadados [I]; A2 (metadados persistem) pode conflitar com pedido de eliminação de titular se os metadados contiverem dado pessoal, o que reforça mantê-los agregados [H].

## Métricas e métodos de avaliação

O grupo FAIR Metrics propôs um modelo de métrica com os campos identificador, nome, princípio a que se aplica, o que se mede, por que medir, o que deve ser fornecido, como medir, o que é resultado válido e para quais recursos é relevante, e derivou "14 exemplar universal metrics covering each of the FAIR sub-principles" (FM-F1A, FM-F1B, FM-F2, FM-F3, FM-F4, FM-A1.1, FM-A1.2, FM-A2, FM-I1, FM-I2, FM-I3, FM-R1.1, FM-R1.2, FM-R1.3) [F: wilkinson2018fairmetrics, Table 1]. O grupo optou por medir "FAIRness for machines", porque FAIRness para pessoas dependeria da experiência de cada usuário, e exige que boa métrica seja clara, realista, discriminante, mensurável e universal [F: wilkinson2018fairmetrics]. Uma autoavaliação com nove respondentes mostrou que algumas métricas, e às vezes o princípio subjacente, "were not always well-understood" [F: wilkinson2018fairmetrics]. FM-A1.2 pede documento público que detalhe procedimentos adicionais de autorização, o que se aplica diretamente a datasets restritos [F: wilkinson2018fairmetrics].

## Exemplo técnico independente de domínio

```
registro_publico (aberto, CC0):           # F1-F4, A2, R1.1
  doi: 10.xxxx/abcd                        # identificador persistente
  titulo, criadores, ano, palavras_chave
  descricao: populacao agregada (faixa etaria ampla, n total), periodo, protocolo etico aprovado
  dicionario_de_variaveis: link publico   # R1, sem valores individuais
  licenca: termos de uso de dados restritos (sem redistribuicao, sem reidentificacao)
  acesso: "restrito; pedido via formulario + aprovacao do responsavel"   # A1.2, FM-A1.2
arquivos (restritos):                      # A1.2
  eventos_pseudonimizados.parquet  -> liberados por token apos aprovacao
apos eliminacao dos dados:                 # A2
  registro_publico permanece, com nota de retirada
```

## Relações com outros conceitos

O plano que declara como cada subprincípio será atendido está em `dat.rd.data-management-plans`; repositórios, DOI, embargo e acesso controlado em `dat.rd.repositories-and-versioning`; os metadados ricos de R1 e o dicionário de dados em `dat.rd.data-documentation`. A proveniência de R1.2 pode ser expressa com `kg.std.prov-o` e a linhagem analítica com `lae.dq.provenance-and-lineage`. Anonimização, pseudonimização e risco de reidentificação ficam em `psg.deid.anonymization-and-pseudonymization` e `psg.deid.reidentification-risk`; base legal para dados de crianças em `psg.legal.lgpd-children`; a separação entre base de pesquisa e operacional em `dat.ethics.research-vs-operation`.

## Lacunas e questões abertas

- A página da GO FAIR não exibe data de atualização; a redação dos subprincípios foi conferida contra o artigo de 2016.
- Não foi encontrada orientação de órgão brasileiro (ANPD, CONEP) sobre publicação de metadados de datasets de pesquisa com crianças; o que pode constar no registro público é decisão de cada protocolo.
- Não foi verificado se ferramentas automáticas de avaliação FAIR posteriores a 2018 tratam datasets com acesso controlado sem penalizá-los.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| wilkinson2016fair | academico | 2026-10-30 |
| gofair2026fairprinciples | tecnico | 2026-10-30 |
| wilkinson2018fairmetrics | academico | 2026-10-30 |
| ec2016h2020fairdmp | normativo | 2026-10-30 |
| scienceeurope2021rdmguide | tecnico | 2026-10-30 |
| fapesp2024faqpgd | normativo | 2026-10-30 |
| zenodo2026aboutrecords | fornecedor | 2026-10-30 |
| zenodo2026policies | fornecedor | 2026-10-30 |
| dataverse2026datasetmgmt | fornecedor | 2026-10-30 |
