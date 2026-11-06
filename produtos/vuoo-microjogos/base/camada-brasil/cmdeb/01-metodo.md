# Método e categorias do Anexo

> **Fonte:** Portaria MEC nº 832/2025, Anexo (texto introdutório). <https://mecnormas.mec.gov.br/pesquisa/detalhar/8017>. Coletado em 2026-11-04.

Cada bloco do Anexo é uma tabela de 6 colunas.

| # | Coluna | Significado |
|---|---|---|
| 1 | Ocorrência | Obrigatoriedade e cardinalidade (ver abaixo) |
| 2 | Nome do dado | Descrição do dado |
| 3 | Modelo de informação | **Variável técnica** (nome interno), usada para interoperabilidade e padronização nacional |
| 4 | Tipo do dado | Numérico, Alfabético, Alfanumérico, Data, Código etc. |
| 5 | Formatação dos dados | Formato esperado e regras de preenchimento; para tipo Código, o domínio de valores |
| 6 | Categoria | Função do dado no sistema |

## Ocorrência

| Valor | Significado |
|---|---|
| `[1..1]` | obrigatório, ocorre uma única vez |
| `[0..1]` | opcional, no máximo uma vez |
| `[1..n]` | obrigatório, pode ocorrer várias vezes |
| `[0..n]` | opcional, pode ocorrer várias vezes |

## Categoria

| Categoria | Definição do Anexo |
|---|---|
| Registro | Dados básicos e obrigatórios, núcleo da informação sobre estudante, turma, escola ou gestor; essenciais para identificação, acompanhamento e conformidade com políticas públicas |
| Complementar | Dados adicionais e opcionais que detalham o registro principal; dispensáveis para o funcionamento mínimo |
| Referência | Identificadores únicos internos, como IDs gerados pelo Sistema Gestão Presente para rastrear matrículas, cadastros ou registros |
| Situacional | Status ou condição atual de um registro (ex.: ativo/inativo) |

## Observações sobre a fonte

- Nos domínios, o código **não é sequencial** (ex.: etapa de ensino pula de 28 a 29, 35 a 38, 41; situação de matrícula tem 12, 19, 21 a 23). Usar o código exatamente como publicado.
- A fonte tem pequenas inconsistências de grafia (ex.: `TURMA_ORGANIZACAO_QUANTIDADE_ TOTAL` com espaço; `[1.. 1]`). Mantidas na variável; normalizadas apenas na ocorrência.
- A tabela original usa linhas de continuação para domínios longos; aqui foram unidas na mesma célula com `<br>`.
