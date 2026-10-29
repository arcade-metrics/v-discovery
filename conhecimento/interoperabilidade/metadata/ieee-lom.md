---
id: iop.md.ieee-lom
titulo: IEEE LOM (Learning Object Metadata)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [standict2026lom, imsglobal2022qti30, imsglobal2011cc]
relacoes:
  - { tipo: alternativa-a, alvo: iop.md.dublin-core }
  - { tipo: alternativa-a, alvo: iop.md.lrmi-schema-org }
  - { tipo: complementa, alvo: iop.tool.common-cartridge }
  - { tipo: relacionado-a, alvo: iop.md.comparison }
termos: [objeto de aprendizagem, metadado educacional, perfil de aplicação]
---

# IEEE LOM

## Definição e terminologia

IEEE LOM é o padrão de metadados para objetos de aprendizagem: um esquema de elementos para descrever recursos educacionais (identificação, ciclo de vida, aspectos técnicos, educacionais, de direitos e de classificação).

A edição corrente é a **IEEE 1484.12.1-2020**, que substitui a IEEE 1484.12.1-2002 [F: standict2026lom]. Segundo registros de catálogos de normas consultados por busca, a aprovação pelo board é de 2020-09-24 e a publicação de 2020-11-16; a fonte consultada é um repositório secundário, não a página do IEEE [I].

## Problema que resolve

Permitir que repositórios distintos descrevam recursos educacionais de forma comparável, de modo que a busca e a federação de catálogos funcionem entre instituições [I].

## Fundamentos e funcionamento

LOM é usado como vocabulário de metadados por outros padrões deste domínio: o QTI 3.0 perfila o IEEE LOM, além do 1EdTech Metadata v1.3 [F: imsglobal2022qti30, §2.4]; a partir do Common Cartridge v1.3, links LTI dentro de um cartridge podem carregar metadados LOM completos e padrões curriculares [F: imsglobal2011cc].

O mecanismo central de uso prático é o **perfil de aplicação**: um subconjunto de elementos com vocabulários e obrigatoriedades definidos para uma comunidade. Sem perfil, implementações preenchem elementos diferentes e a comparabilidade não se materializa [I].

## Requisitos e pressupostos

- Existe um perfil de aplicação acordado entre os participantes da federação.
- Há disciplina de catalogação: LOM é um esquema rico, e o custo de preenchimento recai sobre quem publica o recurso [I].

## Vantagens e limitações

Vantagens [I]: cobre explicitamente a dimensão educacional (nível, público, tipo de interatividade, tempo típico de aprendizagem), ausente em esquemas genéricos; é norma IEEE, com ciclo de revisão formal.

Limitações [I]:
- Esquema extenso: na prática, só uma fração dos elementos é preenchida.
- Nasceu em contexto XML e de repositórios institucionais; a web de dados atual descreve recursos educacionais em JSON-LD com schema.org (ver `iop.md.lrmi-schema-org`).
- Sem perfil de aplicação, a interoperabilidade semântica não se realiza mesmo com conformidade total ao esquema.

## Alternativas e comparações

Ver `iop.md.comparison`.

## Relações com outros conceitos

Alternativa a `iop.md.dublin-core` e `iop.md.lrmi-schema-org`. Complementa `iop.tool.common-cartridge` e `iop.asmt.qti`, que o perfilam.

## Lacunas e questões abertas

- A lista de elementos e categorias da edição 2020, e as diferenças em relação à de 2002, não foram verificadas: a norma é paga e a página do IEEE não foi alcançada na consulta (a URL tentada retornou conteúdo de outra série de normas).
- Existe binding RDF oficial da edição 2020? Não verificado.
- Qual perfil de aplicação LOM é usado em repositórios brasileiros de recursos educacionais? Não verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| standict2026lom | secundario | 2026-10-29 |
| imsglobal2022qti30 | normativo | 2026-10-29 |
| imsglobal2011cc | normativo | 2026-10-29 |
