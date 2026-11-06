# Ficha: Common Core State Standards

> Sem documento em `conhecimento/`. Ficha completa, como framework curricular.

```yaml
id: us.ccss
name: Common Core State Standards
acronym: CCSS
jurisdiction: Estados Unidos (adoção estadual)
issuing_organization: National Governors Association Center for Best Practices (NGA Center) e Council of Chief State School Officers (CCSSO) — titulares de copyright e marca [E20, E21]
reference_type: framework curricular (padrões de aprendizagem) — não é lei federal
domain: [D2, D4]
official_url: https://www.thecorestandards.org/
repository_url: XML por padrão e pacote para download em thecorestandards.org [E19]
version: 2010 (copyright "© Copyright 2010"); revisões individuais marcadas por sufixo (ex.: RF.4.4r2) [E19, E20]
publication_date: 2010
last_updated: unknown
legal_status: framework voluntário adotado por ato de cada estado
mandatory_scope: nos estados que o adotaram, por norma estadual (não verificada caso a caso)
education_levels: K-12; Matemática e ELA/Literacy (inclui literacia em História/Estudos Sociais, Ciências e Disciplinas Técnicas)
geographic_scope: 41 estados, DC, 4 territórios e DoDEA declarados como adotantes [E20]
language: inglês
license: Public License NGA/CCSSO — direito limitado, não exclusivo e gratuito de copiar, publicar e distribuir para fins de apoio à iniciativa; aviso de copyright obrigatório (isentos estados que adotaram integralmente) [E21]
technical_formats: HTML, XML (segue esquema CEDS) [E19]; CASE via CASE Network (anúncio datado) [E22]
api_available: not_found (no site oficial)
data_model_available: sim (hierarquia e XML)
ontology_available: not_found
schemas_available: XML em esquema CEDS [E19]
implementation_examples: URIs desreferenciáveis, ex. https://thecorestandards.org/2010/math/content/6/EE/1 [E19]
related_standards: [CEDS, CASE, NGSS (conexões com CCSS)]
entities: framework → set → grade → domain → cluster (só Matemática) → standard; ELA: strand/domain combinados, sem cluster; anchor standards como set opcional [E19]
relationships: hierarquia; NGSS cita CCSS em "connection boxes" [E25]
vocabularies: códigos de domínio (ex.: EE, OA, RL, RF) e de série
core_relevance: alta — caso de teste de C.CFW/C.CMP com identificação tripla e hierarquia de profundidade variável por área
regional_adapter_relevance: alta (adaptador EUA importaria CCSS e variantes estaduais)
limitations: estados revisaram/renomearam seus padrões; a página oficial afirma que estados "routinely review their academic standards and may choose to change or add onto" [E20]
open_questions: Q10, Q11
sources: [E19, E20, E21, E22]
access_date: 2026-11-05
research_status: verificado no site oficial; publicação CASE só por trecho
```

## Análise técnica

**Identificadores** [E19]:

| Forma | Exemplo | Uso |
|---|---|---|
| Notação de pontos (oficial com prefixo) | `CCSS.ELA-Literacy.RL.2.1`; `Math.6.EE.1` | humanos |
| URI desreferenciável | `https://thecorestandards.org/2010/math/content/6/EE/1` (+ "XML" no fim para o XML) | endereço de registro recomendado |
| GUID | `A7D3275BC52147618D6CFEE43FB1A47E` | máquinas ("There is no need for educators to decode GUIDs") |

Revisões recebem sufixo (`RF.4.4r2`) [E19]. Clusters de Matemática receberam identificadores próprios (A, B, C) para preservar o vínculo cluster→padrão [E19]. Os dados "represent the intent and language of the standards and go no further" [E19].

**Hierarquia** [E19]: Matemática: framework → set → grade → domain → cluster → standard. ELA/Literacy: um nível único combina strand e domain (ex.: Reading Standards for Literature, RL); "Clusters are part of the hierarchy in Math but not ELA/Literacy".

**Observação sobre o site** [E20]: a página consultada declara não ser afiliada à NGA nem ao CCSSO, embora publique a licença deles; o briefing indica `corestandards.org` e a própria página recomenda `www.corestandards.org` como endereço de registro [E19]. Tratar a autoridade do domínio como questão aberta (Q11).

**Lições para o Core [I]:**
1. Profundidade de hierarquia varia por área no mesmo framework → C.CMP não pode ter níveis fixos; nível é atributo tipado (`kind` = domain/cluster/standard).
2. Três identificadores para o mesmo item → C.IDN múltiplo por C.CMP, com um marcado como canônico.
3. Revisão de item individual sem nova versão do framework → versionamento em nível de C.CMP, não só de C.CFW.
