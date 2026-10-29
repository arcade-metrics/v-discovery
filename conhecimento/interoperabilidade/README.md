---
id: iop.index
titulo: Padrões de interoperabilidade educacional
tipo: mapa
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Padrões de interoperabilidade educacional

Base agnóstica sobre padrões, protocolos e modelos de dados para troca de informação entre sistemas educacionais, e entre sistemas educacionais e de saúde. Segue o modelo documental, o método e o checklist de [`../_modelo/`](../_modelo/). Escopo e fontes prioritárias em [`00-brief.md`](00-brief.md).

## Como navegar

Comece pelo [catálogo de padrões](catalogo-padroes.md), que lista cada padrão com órgão mantenedor, versão vigente e status, e pela [matriz comparativa](matriz-comparativa.md), que organiza a escolha por caso de uso. O [mapa de conceitos](mapa-conceitos.md) mostra as relações entre documentos; o [glossário](glossario.md), os termos; o [relatório](relatorio.md), cobertura e lacunas desta versão.

Leitura sugerida para quem chega sem contexto:

1. `fundamentos/niveis-de-interoperabilidade.md`: por que um sistema pode trocar dados com outro sem que nenhum dos dois entenda o significado educacional desses dados.
2. `fundamentos/dados-vs-protocolo.md`: o que cada padrão de fato especifica — modelo de dados, vocabulário, binding, protocolo ou empacotamento.
3. `learning-records/comparison.md`: xAPI, cmi5, Caliper e SCORM, e quando usar cada um.
4. `tool-integration/lti-core.md` e `tool-integration/lti-advantage.md`: como ferramentas externas se integram a um LMS.
5. `rostering/comparison.md`: de onde vêm turmas, matrículas e notas.
6. `semantics/interoperabilidade-semantica.md`: o problema que sobra depois que a camada técnica funciona.
7. `brazil/`: o que disso se aplica no Brasil, e o que não se aplica.

## Pastas

| Pasta | Conteúdo | Prefixo de id |
|---|---|---|
| `fundamentos/` | camadas de interoperabilidade, identidade, mapeamento, conformidade, privacidade | `iop.fund.*` |
| `learning-records/` | xAPI, cmi5, Caliper, comparação | `iop.lr.*` |
| `tool-integration/` | LTI 1.3, LTI Advantage, SCORM, Common Cartridge | `iop.tool.*` |
| `assessment/` | QTI 3.0 | `iop.asmt.*` |
| `rostering/` | OneRoster, Ed-Fi, SIF, CEDS, comparação | `iop.ros.*` |
| `metadata/` | IEEE LOM, Dublin Core, LRMI/schema.org, comparação | `iop.md.*` |
| `competencies/` | CASE, CTDL/CTDL-ASN, ESCO | `iop.comp.*` |
| `credentials/` | W3C Verifiable Credentials, Open Badges 3.0, CLR 2.0 | `iop.cred.*` |
| `semantics/` | vocabulários e SKOS, interoperabilidade semântica | `iop.sem.*` |
| `health/` | CIF, FHIR | `iop.health.*` |
| `brazil/` | Educacenso, LGPD | `iop.br.*` |

## Documentos de raiz

| Arquivo | Conteúdo |
|---|---|
| [`catalogo-padroes.md`](catalogo-padroes.md) | um padrão por linha: mantenedor, versão, data, status, o que especifica |
| [`matriz-comparativa.md`](matriz-comparativa.md) | escolha por caso de uso, com sobreposições e complementaridades |
| [`exemplos-payloads.md`](exemplos-payloads.md) | estruturas de mensagem ilustrativas, lado a lado |
| [`mapa-conceitos.md`](mapa-conceitos.md) | relações tipadas entre documentos |
| [`glossario.md`](glossario.md) | termos do domínio |
| [`relatorio.md`](relatorio.md) | cobertura, decisões e lacunas desta versão |
| [`_plano-ids.md`](_plano-ids.md) | ids planejados e o que ficou adiado |

## Fronteiras com outros domínios

- Transporte em tempo real (WebSocket, WebRTC, QUIC): `realtime-multiplayer`.
- RDF, OWL, ontologias e Graph RAG: `grafo-conhecimento-educacional`. Aqui só entra SKOS, como cola entre vocabulários.
- Esquemas de evento próprios, telemetria, FAIR e datasets: `dados-pesquisa-e-eventos`.
- Avaliação de LMS e plataformas concretas: `lms-e-plataformas`.
