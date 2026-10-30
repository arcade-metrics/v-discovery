---
id: dat.rd.data-management-plans
titulo: Plano de gestão de dados (PGD/DMP)
tipo: conceito
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [fapesp2026gestaodedados, fapesp2024faqpgd, ec2016h2020fairdmp, scienceeurope2021rdmguide, dmptool2026about, dcc2026dmponline]
relacoes:
  - { tipo: depende-de, alvo: dat.rd.fair-principles }
  - { tipo: complementa, alvo: dat.rd.repositories-and-versioning }
  - { tipo: complementa, alvo: dat.rd.data-documentation }
  - { tipo: complementa, alvo: dat.ethics.cep-conep-system }
  - { tipo: complementa, alvo: dat.ethics.consent-and-assent-in-research }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
termos: [plano de gestão de dados, PGD, DMP, data management plan, período de carência, embargo, data steward, maDMP, DMP machine-actionable, opt-out, rubrica de avaliação de DMP, comitê de acesso a dados]
---

# Plano de gestão de dados (PGD/DMP)

## Definição e terminologia

Um **plano de gestão de dados** (PGD; em inglês data management plan, DMP) é o documento que descreve, desde a proposta, como os dados de um projeto serão coletados, documentados, armazenados, compartilhados e preservados. A Comissão Europeia o define como descrição do "data management life cycle for the data to be collected, processed and/or generated" por um projeto [F: ec2016h2020fairdmp, §2]. A Science Europe o apresenta como apoio ao pesquisador para considerar "all relevant aspects of data management from the very beginning of a research project" e insiste que não deve ser "a bureaucratic burden" [F: scienceeurope2021rdmguide, Introduction to the Core Requirements]. Um **DMP machine-actionable** (maDMP) é a versão estruturada, cujas informações podem ser atualizadas e consultadas ao longo do projeto; a DMPTool descreve a transformação "from a static text file into an interoperable, networked hub of information" [F: dmptool2026about].

O que o PGD não é: não é o protocolo submetido ao comitê de ética (ver `dat.ethics.cep-conep-system`), embora deva remeter a ele; não é o termo de consentimento (ver `dat.ethics.consent-and-assent-in-research`); e não é a documentação do dataset publicado (ver `dat.rd.data-documentation`), que é seu produto posterior [I].

## Problema que resolve

Sem planejamento, decisões sobre formato, consentimento para compartilhamento, repositório e custos são tomadas no fim do projeto, quando já não podem ser corrigidas [I]. A FAPESP justifica a gestão de dados por reprodutibilidade, reuso, novas análises e formação de pesquisadores, e observa que o PGD "vem se tornando componente obrigatório na fase de submissão de um projeto" em agências da América do Norte, Austrália e de países europeus [F: fapesp2026gestaodedados]. A Science Europe aponta a variação de exigências entre financiadores como problema para pesquisadores com várias fontes de fomento e propõe requisitos mínimos comuns [F: scienceeurope2021rdmguide].

## Fundamentos e funcionamento

### Requisitos da FAPESP

A página de gestão de dados da FAPESP (consultada em 2026-10-30, sem data de atualização exibida) afirma que, "para determinadas modalidades e chamadas", o PGD faz parte dos anexos obrigatórios; que a Fundação "não tem um modelo próprio"; que chamadas para Centros (CEPID, CPE, CPD) seguem diretrizes próprias; e que, nos demais casos, o plano é um "texto de até duas páginas" com [F: fapesp2026gestaodedados]:

- a) descrição dos dados e metadados produzidos pelo projeto (amostras, registros, formulários, software, bancos de dados, material didático e outros);
- b) quando aplicável, restrições legais ou éticas para compartilhamento e políticas para garantir privacidade, confidencialidade, segurança e propriedade intelectual;
- c) política de preservação e compartilhamento, com o **período de carência** antes do compartilhamento e o período durante o qual os dados serão preservados e disponibilizados;
- d) mecanismos, formatos e padrões de armazenamento que tornem os itens acessíveis a terceiros, podendo usar repositórios de outras instituições.

O FAQ da FAPESP (atualizado em 16/07/2024) acrescenta [F: fapesp2024faqpgd]: "todo projeto submetido à FAPESP precisa ter um PGD, exceto PIPE e Iniciação Científica", inclusive projetos teóricos, que respondem "Não se aplica" aos itens b a d; planos para centros têm até 5 páginas e os demais no máximo 2; a FAPESP requer PDF; não há formulário FAPESP cadastrado na DMPTool, que traz modelos de USP, UNICAMP e UNESP; o PGD pode evoluir, e mudanças devem ser relatadas nos relatórios intermediários; o relatório final deve indicar o link ou o DOI dos dados, e, se não puderem ser divulgados por razões éticas ou legais, isso deve constar desde o início, podendo-se publicar só a descrição em metadados; páginas pessoais e drives "não são locais válidos" para os dados após o fim da pesquisa; e a FAPESP "recomenda que os dados sejam catalogados e disponibilizados em repositórios abertos e de acesso livre" (cita Zenodo, figshare e re3data).

Há uma divergência de escopo entre as duas páginas: a principal fala em "determinadas modalidades e chamadas" e o FAQ em "todo projeto" com duas exceções [F: fapesp2026gestaodedados; fapesp2024faqpgd]. Na dúvida, a chamada específica prevalece [I].

### Modelo H2020 e requisitos centrais da Science Europe

O modelo FAIR do H2020 (versão 3.0, 26/07/2016) organiza o DMP em seis blocos: resumo dos dados; dados FAIR (encontráveis, abertamente acessíveis, interoperáveis, reusáveis); alocação de recursos; segurança; aspectos éticos; outros [F: ec2016h2020fairdmp, Anexo 1]. Ele exige a primeira versão até o sexto mês, atualização a cada mudança significativa e, no mínimo, nas avaliações periódicas, e trata o DMP como "a living document" com número de versão [F: ec2016h2020fairdmp, §4 e Anexo 1]. Na parte de acesso, pergunta se há necessidade de "a data access committee", se as condições de acesso estão descritas em licença legível por máquina e "how will the identity of the person accessing the data be ascertained?"; na parte de reuso, pede que embargos sejam justificados e limitados [F: ec2016h2020fairdmp, Anexo 1, 2.2 e 2.4]. Participar do piloto não significa abrir todos os dados, e há opt-out em qualquer fase [F: ec2016h2020fairdmp, §1].

A Science Europe (edição estendida, janeiro de 2021) define seis requisitos centrais, com quinze perguntas-guia, e afirma que "all six core requirements need to be addressed" [F: scienceeurope2021rdmguide, Core Requirements]: (1) descrição e coleta ou reuso de dados; (2) documentação e qualidade; (3) armazenamento e backup durante a pesquisa; (4) requisitos legais e éticos e códigos de conduta; (5) compartilhamento e preservação de longo prazo, incluindo embargo e DOI por dataset; (6) responsabilidades e recursos, incluindo quem é o data steward. A orientação recomenda ao menos duas cópias em locais separados e desaconselha laptops e pendrives [F: scienceeurope2021rdmguide, 3a].

### Ferramentas

A FAPESP indica DMPTool e DMPonline, que oferecem centenas de modelos e questionários guiados [F: fapesp2026gestaodedados]. A DMPTool é aplicação gratuita e de código aberto, mantida em parceria entre a California Digital Library e o Digital Curation Centre desde 2016, e sua API segue o "RDA Common Standard Metadata schema v1.0" para troca de metadados de DMP, com emissão de DMP-IDs desde abril de 2021 [F: dmptool2026about]. O DMPonline, do DCC, seleciona o modelo do financiador a partir de três perguntas iniciais e exibe orientação de financiadores e universidades [F: dcc2026dmponline].

## Requisitos e pressupostos

- O consentimento e o assentimento precisam prever o compartilhamento e a preservação que o PGD declara; a Science Europe pede "informed consent for preservation and/or sharing of personal data" [F: scienceeurope2021rdmguide, 4a], e o H2020 pergunta se o consentimento para compartilhamento está incluído [F: ec2016h2020fairdmp, Anexo 1, 5].
- Orçamento para curadoria e preservação: H2020 pergunta custos de tornar dados FAIR e de preservação de longo prazo [F: ec2016h2020fairdmp, Anexo 1, 3].
- Repositório escolhido antes da coleta, com suporte a acesso restrito se os dados forem de menores (ver `dat.rd.repositories-and-versioning`) [I].

## Alternativas e comparações

| Critério | FAPESP | H2020 (v3.0, 2016) | Science Europe (2021) |
|---|---|---|---|
| Obrigatoriedade | anexo obrigatório (exceto PIPE e IC, segundo o FAQ) | obrigatório no piloto, salvo opt-out | requisito mínimo recomendado a financiadores |
| Tamanho | até 2 páginas (centros: 5) | não fixado | não fixado |
| Estrutura | 4 itens (a a d) | 6 seções, modelo opcional | 6 requisitos, 15 perguntas |
| Prazo | na submissão; mudanças nos relatórios | versão inicial até o mês 6 | não fixado |
| Acesso restrito | restrições legais e éticas no item b; metadados mesmo sem dados | comitê de acesso, identificação do usuário | procedimento de acesso gerenciado |
| Avaliação | não descrita nas páginas consultadas | não é critério de avaliação | rubrica com dois níveis |

Fontes da tabela: [F: fapesp2026gestaodedados; fapesp2024faqpgd; ec2016h2020fairdmp; scienceeurope2021rdmguide].

## Métricas e métodos de avaliação

A Science Europe oferece uma rubrica para revisores com dois níveis, "Sufficiently Addressed" e "Insufficiently Addressed", e adverte que ela "must be seen as guidance, not as a ready-made tool (such as a checklist)" [F: scienceeurope2021rdmguide, DMP Evaluation Rubric]. Para dados sensíveis, considera insuficiente a explicação vaga sobre segurança e proteção [F: scienceeurope2021rdmguide, Rubric 3b].

## Exemplo técnico independente de domínio

Esqueleto de PGD de duas páginas, nos quatro itens da FAPESP, para dados de interação de crianças [I]:

```
a) Dados: eventos de interação pseudonimizados (JSON Lines -> Parquet), dicionário de variáveis,
   questionários, código de análise. Metadados: DataCite + README + datasheet.
b) Restrições: dados de menores; base legal e TCLE/TALE aprovados pelo CEP; pseudonimização na
   coleta; tabela de correspondência fora do dataset; nenhum dado direto nos metadados públicos.
c) Preservação/compartilhamento: metadados e dicionário abertos na publicação do artigo;
   arquivos em acesso restrito após carência de N meses; acesso por termo de uso de dados
   e aprovação do responsável; preservação por X anos; eliminação da correspondência ao fim.
d) Mecanismos: repositório com DOI e acesso restrito; versionamento do dataset; formatos abertos.
```

## Relações com outros conceitos

O PGD declara como `dat.rd.fair-principles` será atendido; o repositório, o DOI e o embargo ficam em `dat.rd.repositories-and-versioning`; o que acompanha os dados em `dat.rd.data-documentation`. Deve ser coerente com o protocolo ético (`dat.ethics.cep-conep-system`) e com os termos de consentimento e assentimento (`dat.ethics.consent-and-assent-in-research`). Base legal, pseudonimização e minimização ficam em `psg.legal.lgpd-children`, `psg.deid.anonymization-and-pseudonymization` e `psg.access.minimization-and-privacy-by-design`.

## Lacunas e questões abertas

- As "Diretrizes para Planos de Gestão de Dados para propostas de Centros (CEPID, CPE, CPD)" da FAPESP não foram abertas.
- A página principal da FAPESP não exibe data; o FAQ é de 16/07/2024. Não se verificou se há portaria ou norma da FAPESP que formalize os quatro itens.
- O modelo H2020 foi lido em cópia hospedada por biblioteca universitária (o servidor da Comissão devolveu página de erro); não foi aberto o modelo equivalente do Horizon Europe.
- Não foram encontradas exigências de PGD de CAPES ou CNPq nesta sessão.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| fapesp2026gestaodedados | normativo | 2026-10-30 |
| fapesp2024faqpgd | normativo | 2026-10-30 |
| ec2016h2020fairdmp | normativo | 2026-10-30 |
| scienceeurope2021rdmguide | tecnico | 2026-10-30 |
| dmptool2026about | fornecedor | 2026-10-30 |
| dcc2026dmponline | fornecedor | 2026-10-30 |
