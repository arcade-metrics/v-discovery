## 2. Arquitetura proposta

```
┌──────────────────────── Célula jurisdicional BR (região de nuvem no Brasil) ────────────────────────┐
│                                                                                                     │
│  Adaptadores BR (camada anticorrupção)             Views de exportação                              │
│   ├ Censo Escolar (1 serializador por ano)          ├ OneRoster 1.2 (para LMS)                      │
│   ├ API CMDEB v2 / Gestão Presente                  ├ CASE (currículo)                              │
│   ├ SED-SP (a pesquisar)                            ├ xAPI / Caliper (eventos)                      │
│   └ BNCC / Currículo Paulista (dataset verificado)  └ VC 2.0 / Open Badges 3.0                      │
│                 │                                                ▲                                  │
│                 ▼                                                │                                  │
│  Perfil vuoo-br: SHACL + ConceptSchemes (Censo, CMDEB, BNCC…) + mapeamentos SSSOM                   │
│                 │                                                                                   │
│                 ▼                                                                                   │
│  Base operacional (relacional = implementação do vuoo-core)                                         │
│   tenant = rede/secretaria · RLS em pool ou schema/banco dedicado · bitemporal nos vínculos         │
│                 │ R2RML                                                                             │
│                 ├──► grafo do aluno: consulta virtual (Ontop) ou materializado por tenant            │
│                 │      (se o produto adotar embeddings ou Graph RAG)                                │
│                 │                                                                                   │
│                 └──► log de eventos do app (§7.9): atividade + uso do app, séries em bloco          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
   Grafo curricular público (RDF nativo, versionado, sem dado pessoal): global, replicável entre células
   vuoo-core (OWL + SKOS) → gera esquema relacional, JSON Schema/OpenAPI, R2RML, @context JSON-LD (no CI)
```

| Decisão proposta | Por quê | Fonte |
|---|---|---|
| Core próprio mínimo + perfis (Opção B) | Neutro por construção; os padrões existentes viram views; deixa aberto um grafo OWL | padroes-de-arquitetura.md §6 |
| Perfil restringe, extensão só no namespace da jurisdição, nunca redefinir termo do Core | Precedentes nas extensões Ed-Fi, nos perfis OneRoster e no DCAT-AP | idem §1.3 |
| Mapeamentos como dado (SKOS + SSSOM), `exactMatch` só após revisão | A transitividade gera equivalências falsas | idem §1, risco 2 |
| Identificador = lista `{scheme, issuer, value, vigência, status, usoPermitido}` | CPF, ID INEP e ID SGP no BR; UPN, ULN e SCN no UK; ID de 19 caracteres na China | core-v0.1.md P4 |
| Vínculos bitemporais (matrícula, enturmação, papel, apoio, PEI) | Códigos INEP refeitos todo ano; conflito Ed-Fi × OneRoster | idem P3 |
| Grafo híbrido: curricular nativo e público; aluno via R2RML | Dado pessoal fica onde já é protegido; qualquer consulta semântica sobre aluno roda por tenant dentro da célula | padroes-de-arquitetura §5 |
| Célula por jurisdição; tenant = rede | Residência; a rede é a controladora LGPD; a China exige operador local | idem §4; china/ |

## 3. O Core v0.1

O modelo completo está em core-v0.1.md. São cerca de 35 entidades em D1–D8 com 12 princípios. As mudanças em relação à lista provisória são as que mais afetam o banco:

- **Pessoa + atribuição de papel**, no lugar de subtipos Aluno, Professor e Responsável.
- **Matrícula em dois níveis**: com a organização/etapa e com a turma/oferta. Tem tipo (escolarização, AEE, complementar), eventos de situação e frequência como entidade.
- **Etapa** (`EducationalStage`) com nível ISCED obrigatório, separada de **programa de serviço** (AEE, tempo integral).
- **Currículo com quatro relógios** (ato, edição, versão do dado, coorte) e uma entidade **Adoção Curricular**, porque a DCNEM 2024 faz dois Ensinos Médios conviverem por coorte.
- **Resultado separado de classificação**: os cortes do Saeb, do SARESP e do CNCA são esquemas versionados aplicados sobre o mesmo valor.
- **Inclusão em três eixos**:
  - perfil de apoio (barreira → apoio → acomodação), que existe sem laudo;
  - elegibilidade administrativa, sensível e isolada, que nunca alimenta a personalização;
  - documento de suporte, opcional.

  O plano individual tem seções tipadas, mantenedor e revisões.
- **Governança como dado:** classificação por atributo, base legal por operação, registro de divulgação, acordo de dados com prazos e local de processamento, e declaração/snapshot para envios oficiais (Censo).

