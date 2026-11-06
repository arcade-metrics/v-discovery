# Cadeia de confiança

> **Fonte:** bncc-dados (commit `9c26897`): `docs/metodologia.md`, `DECISOES.md` (decisões 1 a 14), `pipeline/verificar.py`, `pipeline/validar.py`, `pipeline/validar_schema.py`, `fontes/README.md`, `.github/workflows/validacao.yml`. Analisado em 2026-11-04.

O centro da estratégia é responder "por que confiar neste dado?" com **testes que rodam sempre**, e não com afirmações. São sete elos.

## 1. Fontes arquivadas e identificadas

- Cada fonte fica no repositório como foi obtida, com data e SHA-256 numa tabela.
- Notas de proveniência registram o que se sabe sobre a fonte: serviço oficial fora do ar, versões erradas circulando (o PDF do Ensino Médio no site do MEC é um rascunho pré-homologação), PDF malformado que exige normalização técnica.
- Há uma hierarquia explícita entre as fontes: **o documento homologado prevalece** sobre a planilha, mesmo quando a planilha é a fonte de extração.
- Material de apoio sem licença clara de redistribuição saiu do repositório e foi trocado por um mapa produzido pelo projeto, que é verificado contra a fonte oficial. Os arquivos originais ficaram registrados só por nome e hash.

## 2. Extração determinística

- Parsing por regra, **sem LLM na cadeia de dados** e sem intervenção manual.
- Divergências conhecidas entre fontes oficiais são corrigidas por um **mapa explícito dentro do extrator** (código → trecho da fonte de extração → trecho do homologado). A correção fica reproduzível e auditável, e não é uma edição no JSON.
- O extrator trata artefatos de layout: linhas de continuação de célula, notas de rodapé dentro da célula, hífen de quebra de linha, ligaduras tipográficas, marcadores de continuação de quadro.

## 3. Verificação caractere a caractere

Para cada registro, o verificador acha o código no PDF homologado e compara o texto depois de uma **normalização tipográfica declarada** (unicode NFC, hífen de quebra, aspas, ligaduras, espaços, colunas intercaladas pelo extrator de texto). O resultado por registro é um destes:

| Status | Significado |
|---|---|
| ok | Texto idêntico; a página é gravada no registro |
| divergente | Diferença real, ou o PDF continua a frase depois do fim do texto (truncamento) |
| requer_conferencia_visual | Só casa ignorando espaços e hífens. **Nunca vira ok sozinho** |
| nao_encontrado | Código ausente do PDF |

A passagem de "requer conferência visual" para "ok" só acontece com uma **exceção registrada**: código, página conferida e motivo.

Também se verificam entidades sem código (competências), procurando o texto inteiro, inclusive quando atravessa duas páginas. Páginas que repetem o texto como exemplo ilustrativo (capítulo de estrutura) são excluídas da localização, e um contrato garante que nenhum localizador aponte para elas.

## 4. Validação de formato com autoteste negativo

- JSON Schemas fechados (draft 2020-12), com tipos compartilhados (padrões de código, slug, fonte, vigência).
- O validador **corrompe registros de propósito** (código inválido, campo extra, organização errada para o componente, data no lugar de data-version, URL fora do gov.br) e exige que o schema os rejeite. Se uma corrupção passar, o schema está frouxo e o CI falha.

É a prova de que a validação morde, e não só passa.

## 5. Contratos de domínio

Um script único concentra cerca de 30 checagens. A taxonomia é o que vale replicar:

| Família | Exemplos |
|---|---|
| Gramática | Todo código decodifica |
| Contagens-gabarito | Total e distribuição por componente, área e campo batem com números fixados no código |
| Integridade referencial | Toda referência aponta para entidade existente |
| Regras estruturais | A organização corresponde ao componente; a competência bate com o dígito do código; a área atribuída é igual à decodificada |
| Unicidade e continuidade | Sem duplicatas; sequência contínua de 1 a n em cada grupo |
| Qualidade de nomes | Nenhum nome partido por quebra de linha, com nota de rodapé ou com hífen de quebra |
| Verificação | Todos os registros ok; nenhum localizador em página proibida |
| Vocabulários | Contagem, unicidade, URL oficial, ementa nula só onde a fonte não tem |
| **Completude por varredura** | Busca por regex de todos os códigos no PDF inteiro: o conjunto encontrado é igual ao do dataset. Nada falta, nada sobra |

O mesmo script roda um conjunto de **consultas do caso âncora** (perguntas reais de um produto consumidor, como "habilidades de LP do 3º ao 6º ano agrupadas por prática") e registra as respostas no relatório. O dado é testado pelo uso que se espera dele.

Há ainda um diff opcional contra uma base independente (outra linhagem do mesmo dado), usado como validação cruzada.

## 6. Derivados determinísticos

- SQLite e CSV são gerados com ordenação estável e metadados (versão da release, hashes das fontes).
- O SQLite é comparado por **dump lógico** em texto, porque os bytes do arquivo variam entre versões da biblioteca.
- Caminhos e nomes são normalizados (unicode NFC) para que o metadado não mude entre sistemas operacionais.

## 7. CI que reproduz tudo

O workflow refaz a cadeia inteira num ambiente limpo e termina com `git diff --exit-code` sobre o canônico e os derivados. Consequências:

- edição manual em `dados/` reprova por definição;
- mudança de pipeline que altere o dado aparece no diff do PR;
- a `main` é sempre reproduzível.

## Revisão humana onde a máquina não decide

Uma heurística (o pareamento dos objetivos da EI entre faixas etárias, que o quadro oficial mostra por posição mas não identifica) foi revisada por uma equipe pedagógica, e a confirmação ficou registrada na nota de cada registro afetado.

## Lições da auditoria (o que deu errado e como foi corrigido)

Uma auditoria independente, em três vias (duas determinísticas e uma leitura visual de 100% dos registros), achou 11 textos errados num dataset que se dizia 100% verificado. As causas são as armadilhas que um projeto replicado deve evitar desde o início:

| Falha | Causa | Correção adotada |
|---|---|---|
| Truncamentos passavam | O verificador só checava se o texto do dataset era **prefixo** do PDF | Checar se o PDF continua a frase depois do fim do texto |
| Texto corrompido aprovado | O fallback "ignorando espaços e hífens" aprovava sozinho | O fallback só sinaliza; aprovar exige exceção registrada |
| Decisão escrita e não aplicada | Havia decisão documentada, mas o extrator não tinha camada de correção | Mapa de correções dentro do extrator, aplicado em toda execução |
| Diagnóstico errado | Uma suposta "perda de glifo" era divergência real | Conferência visual da página impressa antes de concluir |
| Partes nunca verificadas | Competências e nomes de contexto ficavam fora da verificação | Verificar **tudo** o que é texto da fonte, não só a entidade principal |
| Página errada | Primeiro match caía em exemplo ilustrativo | Excluir páginas ilustrativas; contrato impede regressão |

A regra geral: **cada falha encontrada vira um contrato novo**, para não voltar.
