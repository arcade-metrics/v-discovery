---
id: iop.ros.sif
titulo: SIF (Systems Interoperability Framework)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [a4l2021sifspecs, a4l2022sifna]
relacoes:
  - { tipo: alternativa-a, alvo: iop.ros.oneroster }
  - { tipo: alternativa-a, alvo: iop.ros.ed-fi }
  - { tipo: relacionado-a, alvo: iop.ros.comparison }
termos: [locale, data model, infrastructure, zona, Open API, xPress Roster]
---

# SIF (Systems Interoperability Framework)

## Definição e terminologia

SIF é o conjunto de especificações da comunidade Access 4 Learning (A4L) para interoperabilidade entre sistemas educacionais. Diferencia dois planos: o **data model**, específico por localidade, e a **infrastructure**, independente de localidade [F: a4l2021sifspecs].

Modelos de dados publicados por localidade: Austrália, Nova Zelândia, América do Norte e Reino Unido, mais o Infrastructure Data Model independente de localidade [F: a4l2021sifspecs]. Todas as localidades exceto o Reino Unido, e o modelo de infraestrutura, têm definição Open API publicada [F: a4l2021sifspecs].

A especificação de implementação da América do Norte na versão **4.3** está publicada no arquivo da A4L [F: a4l2022sifna].

## Problema que resolve

Padronizar a troca de dados entre sistemas escolares de uma mesma jurisdição, respeitando que o modelo de dados escolar é diferente em cada país — algo que um padrão único não consegue fazer sem virar um denominador comum pequeno demais [I].

## Fundamentos e funcionamento

A separação entre infraestrutura e modelo de dados é a característica estrutural: a infraestrutura define como os sistemas se descobrem e trocam mensagens; o modelo de dados define o conteúdo, e varia por localidade [F: a4l2021sifspecs] [I].

A publicação de definições Open API para quase todas as localidades [F: a4l2021sifspecs] indica que a geração atual é orientada a REST, e não ao modelo de agentes e zonas das gerações anteriores [I] — isso não foi verificado em fonte primária.

## Requisitos e pressupostos

- Existe uma localidade de referência com modelo publicado; usar SIF fora das localidades suportadas significa adotar a infraestrutura sem o modelo [I].

## Vantagens e limitações

Vantagens [I]: reconhecimento explícito de que o modelo de dados é jurisdicional; separação limpa entre transporte e conteúdo; definições Open API facilitam geração de clientes.

Limitações [I]:
- Não há localidade brasileira publicada entre as listadas [F: a4l2021sifspecs]; adotar SIF no Brasil exigiria criar e manter um modelo próprio.
- A documentação consultada é um índice de links, com última atualização registrada em novembro de 2021 [F: a4l2021sifspecs]; o estado corrente das especificações não foi verificado.
- Menor presença no debate público recente que OneRoster e Ed-Fi [H].

## Alternativas e comparações

Ver `iop.ros.comparison`.

## Métricas e métodos de avaliação

Não verificadas: a página consultada não descreve programa de conformidade.

## Relações com outros conceitos

Alternativa a `iop.ros.oneroster` e `iop.ros.ed-fi`.

## Lacunas e questões abertas

- Versões correntes de infraestrutura (3.x) e dos modelos por localidade não confirmadas em fonte primária; a página consultada não traz números de versão, e a versão NA 4.3 vem do arquivo de arquivos da A4L [F: a4l2022sifna].
- Arquitetura (zonas, ZIS, agentes versus REST) não verificada.
- Relação entre SIF e CEDS/Ed-Fi: não verificada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| a4l2021sifspecs | fornecedor | 2026-10-29 |
| a4l2022sifna | fornecedor | 2026-10-29 |
