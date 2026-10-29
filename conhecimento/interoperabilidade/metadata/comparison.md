---
id: iop.md.comparison
titulo: Comparação entre IEEE LOM, Dublin Core e LRMI/schema.org
tipo: comparacao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [standict2026lom, dcmi2020terms, dcmi2026lrmi, schemaorg2026learningresource, imsglobal2022qti30]
relacoes:
  - { tipo: relacionado-a, alvo: iop.md.ieee-lom }
  - { tipo: relacionado-a, alvo: iop.md.dublin-core }
  - { tipo: relacionado-a, alvo: iop.md.lrmi-schema-org }
  - { tipo: complementa, alvo: iop.fund.dados-vs-protocolo }
termos: [metadados, perfil de aplicação, descoberta, catálogo]
---

# Comparação: LOM, Dublin Core e LRMI/schema.org

## Definição e terminologia

Os três descrevem recursos, em níveis de especificidade crescente quanto ao educacional e decrescente quanto à generalidade [I].

## Alternativas e comparações

| Dimensão | IEEE LOM | Dublin Core | LRMI / schema.org |
|---|---|---|---|
| Mantenedor | IEEE [F: standict2026lom] | DCMI [F: dcmi2020terms] | DCMI + Schema.org [F: dcmi2026lrmi] |
| Versão de referência | 1484.12.1-2020 [F: standict2026lom] | DCMI Metadata Terms, 2020-01-20 [F: dcmi2020terms] | schema.org v30.1 para LearningResource [F: schemaorg2026learningresource] |
| Cobertura educacional | alta | nenhuma | média |
| Serialização usual | XML | RDF, JSON-LD | JSON-LD |
| Alcance em busca web | baixo | médio | alto |
| Custo de catalogação | alto | baixo | baixo a médio |
| Alinhamento a competências | por classificação | não | `teaches`, `assesses`, `educationalAlignment` [F: schemaorg2026learningresource] |
| Estabilidade | norma formal | recomendação estável | tipo marcado como novo na versão consultada [F: schemaorg2026learningresource] |

Células sem citação são interpretação [I].

## Fundamentos e funcionamento

**Os três não são mutuamente exclusivos** [I]. O padrão de uso observado nas próprias especificações é de composição: o QTI 3.0 perfila ao mesmo tempo o 1EdTech Metadata v1.3 e o IEEE LOM [F: imsglobal2022qti30, §2.4]; LRMI se apoia no vocabulário do schema.org e declara seus esquemas de conceitos em SKOS [F: dcmi2026lrmi]; e cada termo de `dcterms:` é subpropriedade do termo correspondente em `dc:` [F: dcmi2020terms].

**Regra de decisão** [I]:

1. Catálogo institucional com federação entre repositórios e necessidade de descrever pedagogia em detalhe: LOM com perfil de aplicação explícito.
2. Recurso publicado na web, para ser encontrado: schema.org com LearningResource, e Dublin Core onde já existir.
3. Em qualquer dos casos, o alinhamento a competências vai por identificador externo (`iop.comp.case`, `iop.comp.ctdl`), não por texto livre.

## Métricas e métodos de avaliação

Proporção de recursos com os campos do perfil preenchidos; proporção de valores de competência e nível vindos de vocabulário controlado; taxa de recuperação em busca por critério educacional [I].

## Relações com outros conceitos

Agrega os três documentos da área; complementa `iop.fund.dados-vs-protocolo` (todos os três são padrões de dados, nenhum define protocolo).

## Lacunas e questões abertas

- Não há mapeamento declarado e verificado entre LOM e LRMI nesta base; seria o insumo para uma estratégia de catálogo duplo.
- A versão corrente de LRMI não pôde ser citada (ver `iop.md.lrmi-schema-org`).
- Falta levantar qual esquema é usado em repositórios brasileiros de recursos educacionais abertos.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| standict2026lom | secundario | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
| dcmi2026lrmi | normativo | 2026-10-29 |
| schemaorg2026learningresource | normativo | 2026-10-29 |
| imsglobal2022qti30 | normativo | 2026-10-29 |
