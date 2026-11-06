# Ficha: MEC Gestão Presente (Sistema Gestão Presente, Gestão Presente na Escola) e API CMDEB v2

O modelo de informação (CMDEB) está transcrito em [../cmdeb/](../cmdeb/README.md). Esta ficha cobre a **plataforma**, a **obrigatoriedade**, o **modo de envio** e a **API**.

```yaml
id: br.mec.gestao-presente
name: MEC Gestão Presente – Plataforma de Dados da Educação Básica
acronym: SGP (Sistema Gestão Presente), GPE (Gestão Presente na Escola), GPEI (módulo Educação Infantil)
jurisdiction: Brasil (federal, com adesão de redes estaduais e municipais)
issuing_organization: Ministério da Educação, Secretaria de Educação Básica (SEB/MEC); Comitê Tripartite
reference_type: plataforma governamental instituída por portaria + especificação de API
domain: [D1, D3, D8]
official_url: https://www.gov.br/mec/pt-br/mec-gestao-presente
repository_url: https://api-cmde2.gestaopresente.mec.gov.br/docs
version: "Portaria MEC 234/2025 (alterada pela 832/2025); SGP nova versão lançada em 10/03/2026; API CMDEB v2.0.0 (OpenAPI 3.1.0)"
publication_date: 2025-04-03 (DOU, Portaria 234)
last_updated: "2026-05-21 (lista de adesões citada na página do SGP); OpenAPI lida em 2026-11-05"
legal_status: "plataforma instituída por portaria; adesão voluntária por acordo de adesão via Simec (E33); o MEC descreve o CMDEB como 'padrão orientativo' e 'obrigatório' (E34) — a obrigatoriedade para quem não aderiu não está demonstrada por ato lido"
mandatory_scope: "redes que aderiram (secretarias estaduais e municipais e instituições federais de EB, FAQ E37); adesão ao SGP é pré-requisito dos demais módulos"
education_levels: [educação infantil, ensino fundamental, ensino médio (ainda na versão antiga do SGP), EJA, educação profissional]
geographic_scope: nacional
language: pt-BR
license: not_found
technical_formats: [JSON (API REST), planilhas oficiais (cabeçalhos em CAIXA ALTA)]
api_available: "sim: REST, lotes assíncronos, token Bearer (validade 5 min), snake_case, HTTP 422 na pré-validação; produção https://api-cmde2.gestaopresente.mec.gov.br, homologação https://api-cmde2.hmg.gestaopresente.mec.gov.br"
data_model_available: "sim (CMDEB, 156 variáveis; OpenAPI com 106 schemas)"
ontology_available: não
schemas_available: "OpenAPI 3.1 em /api/v2/openapi.json (público)"
implementation_examples: "exemplos de payload no Swagger/Redoc (não transcritos); exemplo de LoginRequest no schema"
related_standards: [br.mec.cmdeb, br.inep.censo-escolar, br.mec.educadados, programa Pé-de-Meia, PNLD Digital]
entities: [Estudante, Matrícula, Turma, Componente curricular, Frequência mensal, Avaliação de desempenho, Profissional, Função, Formação, Alocação, Instituição de ensino, Lote]
relationships: ver ../modelo-de-dados.md §3
vocabularies: "domínios do CMDEB (cmdeb/) com divergências na API (../modelo-de-dados.md §3.3)"
core_relevance: alta (único modelo nacional operacional, com frequência e notas)
regional_adapter_relevance: muito alta (canal de envio para redes públicas aderentes)
limitations: "texto integral da Portaria 234 não lido; manual da nova versão com link quebrado (404); ensino médio ainda na versão antiga; periodicidade das janelas definida pela SEB fora das portarias lidas; API não tem exclusão; divergências Portaria × API"
open_questions: [Q-06, Q-10, Q-11, Q-12]
sources: [E31, E32, E33, E34, E35, E36, E37]
access_date: 2026-11-05
research_status: completo para API e modelo; parcial para base normativa (Portaria 234)
```

## Funcionamento (E34)

| Aspecto | Achado |
|---|---|
| Módulos | **SGP**: plataforma de dados que recebe dados das redes (já usada no Pé-de-Meia para matrícula e frequência mensal de ~8 milhões de estudantes do EM); **GPE**: sistema de gestão escolar gratuito (matrícula, enturmação, diário de classe com frequência e notas, quadro de horários, app de frequência offline); **GPEI**: fila e matrícula em creche (Portaria MEC 830/2025) |
| Transição 2026 | nova versão do SGP (10/03/2026) para EI, EF e profissionais de todas as etapas; EM continua na versão antiga até aviso do MEC |
| Envio | manual (planilhas oficiais) ou automatizado (API) |
| Operadores | até 5 por município/estado, indicados na adesão via Simec; inclusão por ofício assinado pelo secretário |
| Janelas | "janela de envio de dados" com prazos e contagem regressiva no painel; calendário definido pela SEB (Portaria 832 art. 14) |
| GPE | 1º ciclo (2025): 800 redes; 2º ciclo (2026): 2.513 municípios, que a partir de abril/2026 enviam dados diretamente pelo sistema |
| Usos declarados | trajetória do estudante, transferências entre redes, histórico escolar, PNLD Digital (acesso às obras conforme a escola de vínculo) |

## API CMDEB v2 (E35, E36)

| Item | Detalhe |
|---|---|
| Autenticação | `POST /api/v2/auth/login` com `username` = CPF do operador e `password`; token Bearer de 5 min; `POST /auth/refresh`; chave PGP enviada por ofício (cartilha) |
| Lotes | toda escrita gera lote; `GET /api/v2/lotes`, `/lotes/{id}`, `/lotes/{id}/erros` |
| Recursos | estudantes, matrículas (enturmação, edição, movimentação, confirmar conclusão), frequência mensal (por ano/mês; faltantes), turmas, componentes, avaliação de desempenho, profissionais (funções, formações, enturmação), instituições, pessoas (validação cadastral), Pé-de-Meia (leitura) |
| Nomenclatura | snake_case na API (`forma_organizacao_turma`), CAIXA ALTA nas planilhas; nomes derivados das variáveis do CMDEB em minúsculas |
| Validação | campos obrigatórios, tipos e atributos não reconhecidos → HTTP 422 |
| Homologação | dados enviados são descartados; não usar dados reais |

## Relação com o Censo Escolar [I]

Nenhuma fonte lida afirma que o SGP alimenta ou substitui o Censo. Os dois coexistem: o Censo é obrigatório por decreto e usa ID INEP; o SGP usa CPF e IDs SGP, mas reaproveita o **código INEP da escola** (`CO_ENTIDADE`) e os **códigos nacionais de etapa e componente** do Censo (com diferenças em outros domínios, ver [../terminologia.md](../terminologia.md)).
