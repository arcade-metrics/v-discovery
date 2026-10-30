---
id: dat.rd.repositories-and-versioning
titulo: Repositórios de dados, DOI de dataset e versionamento
tipo: comparacao
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [zenodo2026policies, zenodo2026aboutrecords, zenodo2026versioning, zenodo2026manageversions, dataverse2026datasetmgmt, dataverse2026collectionmgmt, osf2026embargo, osf2026registrations, dvc2026dataversioning, dvc2026remotes, gitlfs2026home, gitannex2026home, gitannex2026drop, datacite2026schema47, scienceeurope2021rdmguide, fapesp2024faqpgd]
relacoes:
  - { tipo: relacionado-a, alvo: dat.rd.fair-principles }
  - { tipo: complementa, alvo: dat.rd.data-management-plans }
  - { tipo: complementa, alvo: dat.rd.data-documentation }
  - { tipo: complementa, alvo: kg.eng.versioning-and-provenance }
  - { tipo: complementa, alvo: lae.dq.provenance-and-lineage }
  - { tipo: relacionado-a, alvo: iop.fund.mapeamento-e-proveniencia }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
termos: [repositório de dados, DOI, concept DOI, version DOI, DataCite, embargo, acesso restrito, termos de acesso, guestbook, período de retenção, tombstone, registro OSF, DVC, Git LFS, git-annex, versão maior e menor]
---

# Repositórios de dados, DOI de dataset e versionamento

## Definição e terminologia

Um **repositório de dados** é um serviço que recebe, identifica, descreve, preserva e dá acesso a datasets. A Science Europe lista critérios mínimos para um repositório confiável em quatro tópicos: identificadores persistentes (com suporte a versionamento), metadados (públicos e mantidos "even for non-published, protected, retracted, or deleted data"), acesso e licenças (incluindo "ensure confidentiality and respect rights of data subjects") e preservação [F: scienceeurope2021rdmguide, Criteria for the Selection of Trustworthy Repositories]. **Versionamento de dataset** é o registro de estados sucessivos do conjunto de dados com identificadores estáveis por versão. Ferramentas como DVC, Git LFS e git-annex versionam arquivos grandes durante o trabalho, mas não são repositórios de publicação: não emitem DOI nem garantem preservação [I].

## Problema que resolve

Dados citados num artigo precisam continuar resolvíveis e imutáveis; dados de menores precisam ser descobríveis sem serem baixáveis por qualquer pessoa. O repositório resolve o primeiro problema com DOI e congelamento de arquivos, e o segundo com metadados públicos e arquivos restritos ou embargados [I]. A FAPESP lembra que páginas pessoais e drives "não são locais válidos para manter os dados de pesquisa após o fim da pesquisa" [F: fapesp2024faqpgd, III.3].

## Fundamentos e funcionamento

### Zenodo

Zenodo aceita qualquer formato, com limite de 50 GB por registro (cotas maiores sob pedido), registra DOI na DataCite ao publicar e exporta metadados em DataCite, Dublin Core e MARCXML [F: zenodo2026policies; zenodo2026aboutrecords]. Arquivos podem ser depositados em acesso aberto, fechado, embargado ou restrito; no embargo, o acesso aos dados é bloqueado até a data final e então liberado automaticamente; no acesso restrito, o compartilhamento depende da aprovação do depositante [F: zenodo2026policies, Access to data objects; Embargo status; Restricted Access]. A documentação afirma que "metadata for all records in Zenodo are always publicly accessible" e que a restrição existe para conteúdo embargado, em revisão ou que não pode ser disponibilizado, citando "anonymized clinical trial data" [F: zenodo2026aboutrecords]. Os metadados são licenciados em CC0 e colhidos por OAI-PMH [F: zenodo2026policies].

Depois de publicado, um registro não admite alteração de arquivos nem de identificador; atualizar dados exige nova versão, que é "a completely new record with separate metadata, files and persistent identifier" ligada às demais [F: zenodo2026aboutrecords; zenodo2026manageversions]. Na primeira publicação o Zenodo registra dois DOIs, um da versão e outro que representa todas as versões (**concept DOI**), que resolve para a versão mais recente; a documentação recomenda citar o DOI da versão para reprodutibilidade e explica que sufixos ".v1" não são legíveis por máquina, preferindo ligar DOIs semanticamente nos metadados [F: zenodo2026versioning]. A política prevê retirada com página tombstone que mantém DOI e URL, retenção pela vida útil do CERN (programa experimental de pelo menos 20 anos) e checksum MD5 verificado periodicamente [F: zenodo2026policies].

### Dataverse (instalação Harvard e outras)

O guia do Dataverse (v. 6.12.1) descreve: arquivos restritos não podem ser baixados sem permissão; ao restringir, o depositante preenche **termos de acesso** e pode habilitar "Request Access"; curadores concedem acesso por arquivo a usuários ou grupos [F: dataverse2026datasetmgmt, Restricted Files + Terms of Access; File-level permissions]. O **guestbook**, configurado na coleção, coleta dados de quem baixa arquivos (conta, afiliação, perguntas como finalidade de uso) e exporta-os em CSV [F: dataverse2026collectionmgmt, Dataset Guestbooks]. **Embargos** por arquivo publicam o identificador e os metadados mas bloqueiam o conteúdo até a data final, sem permitir pedidos de acesso durante o embargo; não podem ser alterados pelo usuário depois de publicados; e permitem embargos "rolling" por versão [F: dataverse2026datasetmgmt, Embargoes]. **Períodos de retenção** tornam o conteúdo inacessível após uma data, para casos em que arquivos devem ser indisponibilizados "e.g. to meet legal requirements", mas "actual destruction is not automatically handled" [F: dataverse2026datasetmgmt, Retention Periods]. Versões são numeradas como maior e menor: adicionar ou remover arquivos exige versão maior; a aba de versões mostra diferenças [F: dataverse2026datasetmgmt, Dataset Versions]. Há ainda metadados de privacidade diferencial experimentais para arquivos tabulares restritos [F: dataverse2026datasetmgmt].

### OSF

O OSF permite embargar registros, que ficam "safely recorded and timestamped but not publicly accessible" e aparecem como "page not found" para quem não tem permissão; o embargo dura até quatro anos [F: osf2026embargo]. Arquivos de projeto anexados a um registro têm limite de 5 GB [F: osf2026registrations]. É adequado a pré-registro e materiais; para dataset restrito de longo prazo, as fontes consultadas não descrevem controle de acesso equivalente ao do Dataverse [I].

### Versionamento durante o trabalho

O DVC guarda em Git um pequeno arquivo `.dvc` "human-readable" que funciona como marcador do dado, endereçado por hash, enquanto o conteúdo vai para cache e para um remoto escolhido pelo usuário (S3, SSH, diretório local e outros); credenciais devem ficar em `.dvc/config.local`, fora do Git [F: dvc2026dataversioning; dvc2026remotes]. O Git LFS substitui arquivos grandes "with text pointers inside Git" e guarda o conteúdo num servidor remoto (versão 3.8.1 anunciada como atualização de segurança na página) [F: gitlfs2026home]. O git-annex gerencia arquivos grandes sem guardar o conteúdo no Git, com checksums e criptografia [F: gitannex2026home], e `git annex drop` recusa remover conteúdo se não puder verificar cópias suficientes (numcopies) [F: gitannex2026drop].

Para dados de menores, essas ferramentas só versionam bem se o remoto tiver controle de acesso adequado; e apagar um dado pessoal exige remover o objeto do cache e de cada remoto, não só do histórico de ponteiros [I].

### DataCite

O DataCite Metadata Schema 4.7 (lançado em 03/03/2026) é a versão vigente [F: datacite2026schema47]. As propriedades obrigatórias são Identifier, Creator, Title, Publisher, PublicationYear e ResourceType; RelatedIdentifier é recomendada; Version e Rights são opcionais [F: datacite2026schema47, Overview]. Sobre Version, a documentação sugere "track major_version.minor_version" e "register a new identifier for a major version change", deixando a cada curador definir o que é maior ou menor [F: datacite2026schema47, Version].

## Alternativas e comparações

| Critério | Zenodo | Dataverse | OSF | DVC / Git LFS / git-annex |
|---|---|---|---|---|
| DOI | sim, DataCite, por versão + concept DOI | um identificador (DOI ou Handle) por dataset, não por versão | não verificado nesta sessão | não |
| Metadados públicos com arquivos fechados | sempre | sim (embargo e restrição) | não (embargo oculta o registro) | não se aplica |
| Pedido de acesso | aprovação do depositante | Request Access + termos + guestbook | não verificado | depende do remoto |
| Embargo | até data final, liberação automática | por arquivo, inalterável após publicação | até 4 anos | não |
| Retenção/eliminação | retirada com tombstone; arquivos preservados | período de retenção, destruição manual | não verificado | remoção manual de cache e remotos |
| Limite | 50 GB por registro | por instalação | 5 GB anexados ao registro | do remoto |

Fontes da tabela: [F: zenodo2026policies; zenodo2026aboutrecords; zenodo2026versioning; dataverse2026datasetmgmt; osf2026embargo; osf2026registrations; dvc2026remotes]. O Dataverse cria "one persistent identifier per dataset and doesn't create new ones for each version" [F: dataverse2026datasetmgmt, Embargoes].

## Vantagens e limitações

Zenodo garante metadados abertos e arquivos restritos, o que atende ao padrão FAIR com acesso controlado, mas preserva arquivos mesmo após retirada da vista pública ("records can be retracted from public view; however, the data files and record are preserved") [F: zenodo2026policies], o que exige cuidado antes de depositar dados que possam precisar ser eliminados [I]. O Dataverse tem o controle de acesso mais granular entre os consultados, mas o guestbook coleta dados pessoais de quem baixa, que também precisam de base e retenção definidas [I]. O OSF esconde o registro inteiro sob embargo, o que impede a descoberta durante o período [F: osf2026embargo; I].

## Exemplo técnico independente de domínio

```
trabalho:  git (codigo + .dvc) -> remoto DVC institucional com ACL   # dados pseudonimizados
release 1.0: deposito -> DOI_v1; metadados+dicionario abertos; arquivos restritos
correcao de rotulos (menor): DataCite Version 1.1, mesmo DOI se o curador definir como menor
novo lote de coleta (maior): novo DOI_v2; RelatedIdentifier IsNewVersionOf DOI_v1 [nome nao verificado]
pedido de eliminacao: avaliar se o arquivo publicado contem o titular; retirada + nova versao
```

## Relações com outros conceitos

Implementa `dat.rd.fair-principles` (F1, A1.2, A2, R1.1) e executa o que `dat.rd.data-management-plans` declara; o que acompanha o depósito está em `dat.rd.data-documentation`. Versionamento e proveniência como conceito geral estão em `kg.eng.versioning-and-provenance` e `lae.dq.provenance-and-lineage`; o mapeamento de proveniência entre formatos em `iop.fund.mapeamento-e-proveniencia`. O que pode ir para metadados públicos depende de `psg.deid.reidentification-risk` e `psg.access.minimization-and-privacy-by-design`.

## Lacunas e questões abertas

- Os nomes exatos dos valores de relationType para versões no DataCite 4.7 (por exemplo IsNewVersionOf) não foram confirmados na página aberta.
- Não foram consultados repositórios institucionais brasileiros (por exemplo, instalações Dataverse de universidades paulistas) nem suas políticas para dados de menores.
- Controle de acesso e DOI no OSF não foram verificados nesta sessão.
- A versão vigente do DVC não foi registrada; a documentação menciona migração para DVC 3.0.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| zenodo2026policies | fornecedor | 2026-10-30 |
| zenodo2026aboutrecords | fornecedor | 2026-10-30 |
| zenodo2026versioning | fornecedor | 2026-10-30 |
| zenodo2026manageversions | fornecedor | 2026-10-30 |
| dataverse2026datasetmgmt | fornecedor | 2026-10-30 |
| dataverse2026collectionmgmt | fornecedor | 2026-10-30 |
| osf2026embargo | fornecedor | 2026-10-30 |
| osf2026registrations | fornecedor | 2026-10-30 |
| dvc2026dataversioning | fornecedor | 2026-10-30 |
| dvc2026remotes | fornecedor | 2026-10-30 |
| gitlfs2026home | fornecedor | 2026-10-30 |
| gitannex2026home | fornecedor | 2026-10-30 |
| gitannex2026drop | fornecedor | 2026-10-30 |
| datacite2026schema47 | normativo | 2026-10-30 |
| scienceeurope2021rdmguide | tecnico | 2026-10-30 |
| fapesp2024faqpgd | normativo | 2026-10-30 |
