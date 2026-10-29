---
id: iop.relatorio
titulo: Relatório da primeira versão do domínio
tipo: relatorio
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Relatório: primeira versão do domínio interoperabilidade

## O que esta versão entrega

44 documentos novos, mais o brief que já existia — 45 arquivos com frontmatter no total. 40 fontes novas na bibliografia central. Validação sem erros nem avisos por `_modelo/validar.py`.

| Área | Documentos | Cobertura |
|---|---|---|
| `fundamentos/` | 6 | camadas, classificação de padrões, identidade, mapeamento, conformidade, privacidade |
| `learning-records/` | 4 | xAPI, cmi5, Caliper, comparação |
| `tool-integration/` | 4 | LTI Core, LTI Advantage, SCORM, Common Cartridge |
| `assessment/` | 1 | QTI 3.0 |
| `rostering/` | 5 | OneRoster, Ed-Fi, SIF, CEDS, comparação |
| `metadata/` | 4 | IEEE LOM, Dublin Core, LRMI/schema.org, comparação |
| `competencies/` | 3 | CASE, CTDL, ESCO |
| `credentials/` | 3 | W3C VC 2.0, Open Badges 3.0, CLR 2.0 |
| `semantics/` | 2 | SKOS, interoperabilidade semântica |
| `health/` | 2 | CIF, FHIR |
| `brazil/` | 2 | Educacenso, LGPD |
| raiz | 8 | README, catálogo, matriz, exemplos, mapa, glossário, plano de ids, relatório |

## Decisões de estrutura

- **`fundamentos/` foi acrescentado** à estrutura do brief. A especificação de pesquisa pede explicitamente a distinção entre interoperabilidade técnica, semântica e organizacional, e esse recorte não cabia em nenhuma pasta de padrão.
- **`metadata/`, `competencies/` e `semantics/` foram acrescentados** porque a segunda parte da especificação cobre modelos de dados e vocabulários (LOM, Dublin Core, LRMI, CASE, CEDS, ESCO, CTDL, SKOS), não apenas protocolos.
- **RDF e OWL ficaram fora.** Pertencem a `grafo-conhecimento-educacional`. Aqui entra apenas SKOS, no papel de cola entre vocabulários de padrões distintos. `iop.sem.vocabularios-e-skos` registra a fronteira.
- **Open Badges e CLR foram tratados como derivados de W3C VC**, com documento próprio para o modelo do W3C. As duas especificações do 1EdTech declaram alinhamento ao VCDM 2.0, o que torna essa a ordem natural de leitura.
- **`catalogo-padroes.md` e `matriz-comparativa.md` são documentos distintos**: o catálogo é o inventário com versão e status; a matriz parte do caso de uso. Juntá-los produziria uma tabela ilegível.

## Qualidade das fontes

| Tipo de fonte | Entradas | Observação |
|---|---|---|
| normativo | 25 | especificações e normas consultadas diretamente |
| fornecedor | 7 | páginas oficiais de mantenedores (1EdTech, Ed-Fi, A4L, NCES, Credential Engine, Comissão Europeia) |
| tecnico | 2 | documentação de praticante (Rustici/SCORM) |
| secundario | 6 | usados onde a fonte primária não foi acessível, sempre sinalizado no texto |

Seis especificações foram lidas apenas parcialmente porque excedem o limite de leitura de uma requisição (Caliper 1.2, LTI 1.3, LTI AGS, Open Badges 3.0, CLR 2.0, VCDM 2.0, DCMI Terms). As partes não lidas estão registradas como lacuna em cada documento.

## Lacunas prioritárias

Em ordem de impacto sobre a utilidade da base:

1. **Perfis xAPI.** Vários documentos apontam que a interoperabilidade semântica do xAPI depende de perfis, e a especificação de Profiles do ADL não foi consultada. É a maior lacuna do domínio.
2. **Educacenso.** Não foi localizada documentação oficial do INEP sobre o leiaute vigente nem sobre API. As fontes disponíveis são manuais de fornecedor de 2013–2016. Sem isso, a parte brasileira do domínio fica apoiada em material indireto.
3. **ISO/IEC TS 20748-3:2020.** É a referência normativa para mapeamento entre xAPI e Caliper, citada em três documentos e não lida (norma paga). Avaliar aquisição.
4. **CASE Information Model.** As URLs do modelo de informação retornaram 404 ou página vazia; classes e tipos de associação permanecem não verificados, embora CASE seja o ponto de articulação entre currículo, recurso, avaliação e credencial.
5. **Certificação 1EdTech.** As páginas de programa retornaram 404; a relação entre certificação e associação à organização continua em aberto, e é relevante para requisitos de edital.
6. **IEEE 1484.12.1-2020 (LOM).** Norma paga; a página do IEEE não foi alcançada. Elementos e mudanças em relação a 2002 não verificados.
7. **Bindings REST do OneRoster.** Endpoints, escopos e paginação não verificados; o documento descreve o conjunto documental, não a API.
8. **SCORM.** O site da ADL não respondeu (ECONNREFUSED). Nomes das funções da API e datas das edições vêm de fonte técnica de terceiro ou ficaram sem verificação.

## Versões que podem estar desatualizadas

As fontes consultadas não declaram versão corrente para CEDS, SIF, LRMI e CTDL, e não foi possível confirmar se existem versões posteriores de Caliper 1.2, cmi5 Quartz, CASE 1.0 e Common Cartridge 1.3. O catálogo registra "versão de referência", não "versão mais recente"; essa distinção precisa ser mantida na próxima revisão.

## Próximos passos sugeridos

1. Ler a especificação de perfis xAPI e criar `iop.lr.xapi-profiles`.
2. Buscar documentação oficial do INEP e reescrever `iop.br.educacenso` sobre fonte primária; investigar sistemas estaduais.
3. Produzir um perfil de aplicação de exemplo — o artefato que falta para tornar `iop.sem.interoperabilidade-semantica` operacional.
4. Verificar se BNCC ou currículos estaduais estão publicados em CASE; é a pergunta que decide a estratégia de competências no Brasil.
5. Ler os bindings REST de OneRoster e o Information Model do CASE, fechando as duas lacunas de modelo de dados mais citadas.
6. Validar os exemplos de `exemplos-payloads.md` contra os esquemas oficiais.
7. Revisar documentos para `status: revisado` com o `_modelo/checklist-revisao.md`, começando pelos de `fundamentos/`.

## Pendências de método

- Nenhum documento foi promovido a `status: revisado`. Todos são `rascunho`.
- Não há, nesta rodada, fonte acadêmica revisada por pares: o domínio é de especificações, mas a literatura sobre falhas de interoperabilidade semântica em contextos educacionais reais seria um complemento útil e não foi buscada.
