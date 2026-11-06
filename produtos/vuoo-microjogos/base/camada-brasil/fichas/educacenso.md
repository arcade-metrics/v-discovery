# Ficha: Censo Escolar da Educação Básica / Educacenso

Análise conceitual prévia (papel do Censo como "vocabulário comum", troca anual em arquivo): `conhecimento/interoperabilidade/brazil/educacenso.md` (iop.br.educacenso). Esta ficha **acrescenta** o que lá faltava: o leiaute oficial vigente, campo a campo, com regras e códigos. A lacuna registrada naquele documento ("não foi localizada documentação oficial do INEP sobre o leiaute vigente") está resolvida: o leiaute 2026 é público (E02).

```yaml
id: br.inep.censo-escolar
name: Censo Escolar da Educação Básica (coleta via Sistema Educacenso)
acronym: Censo Escolar / Educacenso
jurisdiction: Brasil (federal)
issuing_organization: INEP / Diretoria de Estatísticas Educacionais (DEED), Coordenação-Geral do Censo Escolar da Educação Básica
reference_type: pesquisa estatística oficial com leiaute técnico de intercâmbio (norma técnica do órgão); obrigatoriedade por decreto
domain: [D1, D3, D7, D8]
official_url: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar
repository_url: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/orientacoes/matricula-inicial/migracao
version: "Layout de Importação e Exportação da Matrícula Inicial 2026, versão V5 (planilha modificada em 2026-07-01); Layout de Identificação 2026 v1; Tabelas auxiliares 2026; Layout Situação do Aluno 2025 v3"
publication_date: 2026 (coleta da 1ª etapa de 27/05 a 31/07/2026)
last_updated: 2026-07-01 (metadado da planilha do leiaute)
legal_status: "obrigatório para escolas públicas e privadas de educação básica (Decreto 6.425/2008, art. 4º, conforme Caderno de Conceitos 2026, p. 2); cronograma 2026: Portaria nº 217, de 11/05/2026; data de referência: Portaria MEC 264/2007"
mandatory_scope: todas as escolas públicas e privadas de educação básica e educação profissional; dados usados no Fundeb (matrículas presenciais efetivas) e no Ideb (taxas de rendimento)
education_levels: [educação infantil, ensino fundamental, ensino médio, EJA, educação profissional técnica de nível médio, FIC]
geographic_scope: nacional
language: pt-BR
license: "publicações INEP: 'É permitida a reprodução total ou parcial desta publicação, desde que citada a fonte' (Caderno 2ª etapa 2025); licença específica do leiaute: not_found"
technical_formats: [arquivo texto .txt ISO-8859-1 delimitado por '|', planilhas XLSX (leiaute e tabelas), RAR (tabelas)]
api_available: "não para envio (migração por upload de arquivo no Educacenso); not_found API pública"
data_model_available: sim (leiaute de registros 00, 10, 20, 30, 40, 50, 60 e 89, 90, 91)
ontology_available: não
schemas_available: "planilha de leiaute com campo, obrigatoriedade, tamanho, tipo, valores permitidos, regras e momento de validação; sem XSD/JSON Schema"
implementation_examples: "Figura 5 'Exemplo de arquivo de importação' no PDF de instruções de migração 2026 (não transcrita)"
related_standards: [br.mec.cmdeb, br.mec.gestao-presente, br.lei.ldb, br.mec.educadados, iop.ros.oneroster, iop.ros.ed-fi, iop.ros.ceds]
entities: [Escola, Caracterização da escola, Turma, Pessoa física, Gestor (vínculo), Profissional escolar em sala (vínculo), Aluno (vínculo/matrícula), Situação do aluno]
relationships: "escola 1..1500 turmas; turma 1..n alunos e 1..n profissionais; pessoa 1..n vínculos (40/50/60); aluno ≤ 4 vínculos com etapa"
vocabularies: "Tabela de Etapas, de Áreas do Conhecimento/Componentes, de AEE, de Atividade Complementar, de Municípios, Distritos, Países, Povos e Línguas Indígenas, Órgãos Regionais, Cursos Técnicos, Cursos Superiores, IES, Áreas de Pós; códigos inline no leiaute"
core_relevance: alta (fonte dos códigos nacionais de etapa, componente e AEE; regras de unicidade; resolução de identidade)
regional_adapter_relevance: muito alta (saída obrigatória anual do adaptador Brasil para escolas que o operem)
limitations: "anual e por data de referência; sem frequência, notas, datas de matrícula, turno codificado nem oferta profissional×componente com carga; profissionais fora de sala só em contagem; leiaute muda todo ano; códigos de turma e matrícula INEP só existem após a importação"
open_questions: [Q-01, Q-03, Q-04, Q-05, Q-06]
sources: [E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11]
access_date: 2026-11-05
research_status: completo para 1ª etapa 2026; parcial para 2ª etapa (leiaute 2026 não publicado)
```

## Análise técnica (§6.3)

| Item | Achado |
|---|---|
| Entidades e atributos | Ver [../modelo-de-dados.md](../modelo-de-dados.md) §2 (todos os registros, com campos estruturais e regras) |
| Identificadores primários | Código de escola INEP (8); ID único INEP de pessoa (12); código da turma INEP (≤ 10) e da matrícula (≤ 12) só na exportação |
| Identificadores externos | CPF (Receita Federal), certidão de nascimento nova (32), IBGE município/distrito, CNPJ mantenedora/escola, códigos de IES, códigos do sistema próprio (≤ 20, únicos por escola) |
| Cardinalidades | ≤ 100 escolas/arquivo; 1 registro 00 e 1 registro 10 por escola; ≤ 1.500 turmas; ≤ 3 gestores; turma com ≥ 1 aluno e ≥ 1 profissional; aluno ≤ 4 vínculos com etapa, ≤ 2 fora de 39/40/64/68, ≤ 4 AEE/atividade complementar |
| Hierarquias | etapa agregada (301–308) → etapa; escola sede → unidade vinculada; UF → município → distrito; UF → órgão regional |
| Enums | [../terminologia.md](../terminologia.md) |
| Regras de validação | 42 regras gerais + regras por campo, cada uma com momento (validação/processamento) e efeito (Recusada / Importada parcialmente); anexos 3 (idades), 4 (recurso × deficiência), 5 (parceria × dependência), 6 (etapa × forma de organização), 7 (mediação × tipo de turma × etapa), 8 (carga horária) |
| Temporalidade | foto na data de referência (27/05/2026); ano letivo da escola com datas de início/fim; 2ª etapa registra situação no término do ano letivo; "admissão após" para quem entrou depois da data de referência |
| Versionamento | leiaute anual com histórico de versões dentro do ano (v1 a V5 em 2026) e aba de mudanças em relação ao ano anterior |
| Operações CRUD | importação (cria/atualiza) por arquivo; exportação do ano anterior para recuperar IDs; arquivo de identificação para obter ID de aluno antes da migração; retificação em período próprio; deduplicação de matrículas (05/11 a 14/11/2026) |
| Serialização | texto, uma linha por registro, campos separados por `|`, terminador `99|`; sem cabeçalho |
| Extensão | nenhuma (campos fixos por ano) |
| Compatibilidade retroativa | não garantida: em 2026 três campos de 2025 viraram um (tipo de turma), campos novos inseridos no meio (ex.: reg. 20 c25, c27) mudam a posição dos seguintes |
| Exemplos de payload | não transcritos (Figura 5 do PDF de instruções) |
| Autenticação/autorização | login gov/CPF no Educacenso; perfis Escola, Municipal, Estado, Setec, Regional, INEP com privilégios distintos (ex.: só INEP/Estado alteram dependência e órgão regional; Setec e Regional não exportam) |
| Conformidade | responsabilidade administrativa, civil e penal do responsável pela escola (Lei 8.429/1992, conforme Caderno); documentação comprobatória exigível por MEC, INEP, MP e órgãos de controle |

## Notas para o Core e o adaptador [I]

- O Censo é uma **visão derivada**: o adaptador deve ser capaz de gerar o arquivo da 1ª etapa a partir do estado na data de referência e o da 2ª etapa a partir das situações finais.
- O vínculo aluno × turma (registro 60) é a "matrícula" do Censo; o Core deve permitir mais de uma matrícula simultânea por aluno (escolarização + AEE + atividade complementar), com `kind`.
- Profissional de apoio escolar (função 8) e tradutor-intérprete de Libras (função 4) são vínculos de turma, não de aluno: o apoio individual ao estudante não é representável no Censo por pessoa atendida.
- Recursos para avaliações do INEP (reg. 30 c36–49) são atributos da pessoa, não da matrícula, e vinculados ao Saeb.
