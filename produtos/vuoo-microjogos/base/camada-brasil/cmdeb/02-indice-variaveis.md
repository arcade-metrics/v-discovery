# Índice de variáveis

> **Fonte:** Portaria MEC nº 832, de 16/12/2025 (DOU 17/12/2025), Anexo "Conjunto Mínimo de Dados da Educação Básica - CMDEB". MEC Normas: <https://mecnormas.mec.gov.br/pesquisa/detalhar/8017>. DOU: <https://www.in.gov.br/web/dou/-/portaria-mec-n-832-de-16-de-dezembro-de2025-675840850>. Coletado em 2026-11-04.

156 variáveis, na ordem do Anexo. Detalhes (nome, formato, domínios) no arquivo do bloco.

| Variável | Bloco / seção | Ocorr. | Tipo | Categoria | Arquivo |
|---|---|---|---|---|---|
| `ID_SGP_ESTUDANTE` | 1 | [1..1] | Numérico | Referência | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_CPF` | 1 | [1..1] | Numérico | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_NIS` | 1 | [0..1] | Numérico | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_NOME` | 1 | [1..1] | Alfabético | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_NOME_SOCIAL` | 1 | [0..1] | Alfabético | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_DT_NASCIMENTO` | 1 | [1..1] | Data | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_TELEFONE` | 1 | [0..1] | Numérico | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_EMAIL` | 1 | [0..1] | Alfanumérico com @ | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_RESPONSAVEL_1_NOME` | 1 | [1..1] | Alfabético | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_VINCULO_RESPONSAVEL_1` | 1 | [1..1] | Código | Registro | [10-estudante.md](10-estudante.md) |
| `RESPONSAVEL_1_CPF` | 1 | [0..1] | Numérico | Complementar | [10-estudante.md](10-estudante.md) |
| `RESPONSAVEL_1_TELEFONE` | 1 | [0..1] | Numérico | Complementar | [10-estudante.md](10-estudante.md) |
| `RESPONSAVEL_1_E_MAIL` | 1 | [0..1] | Alfanumérico com @ | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_RESPONSAVEL_2_NOME` | 1 | [0..1] | Alfabético | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_VINCULO_RESPONSAVEL_2` | 1 | [0..1] | Código | Complementar | [10-estudante.md](10-estudante.md) |
| `RESPONSAVEL_2_CPF` | 1 | [0..1] | Numérico | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_SEXO` | 1 | [1..1] | Código | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_RACA_COR` | 1 | [1..1] | Código | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_QUILOMBOLA` | 1 | [1..1] | Código | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_DEFICIENCIA` | 1 | [1..n] | Código | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_NECESSIDADE_NUTRICIONAL` | 1 | [0..1] | Código | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_NACIONALIDADE` | 1 | [1..n] | Código | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_CO_MUNICIPIO_RES` | 1 | [1..1] | Numérico | Registro | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_CEP_RES` | 1 | [0..1] | Numérico | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_LOGRADOURO_RES` | 1 | [0..1] | Alfanumérico | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_BAIRRO_RES` | 1 | [0..1] | Alfanumérico | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_NU_ENDERECO_RES` | 1 | [0..1] | Alfanumérico | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_LOCALIZACAO_GEOGRAFICA` | 1 | [0..1] | Código | Complementar | [10-estudante.md](10-estudante.md) |
| `ESTUDANTE_LOCALIZACAO_DIFERENCIADA` | 1 | [0..1] | Código | Complementar | [10-estudante.md](10-estudante.md) |
| `ID_SGP_MATRICULA` | 2 / 2.1 | [1..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `ESTUDANTE_MATRICULA_SITUACAO` | 2 / 2.1 | [0..1] | Código | Situacional | [20-trajetoria.md](20-trajetoria.md) |
| `ESTUDANTE_ETAPA_DE_ENSINO` | 2 / 2.1 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `ESTUDANTE_APOIO_PEDAGOGICO` | 2 / 2.1 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TIPO_ATENDIMENTO_ESPECIALIZADO` | 2 / 2.1 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `ESTUDANTE_REFORCO` | 2 / 2.1 | [0..1] | Código | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `NU_ANO_MATRICULA` | 2 / 2.1 | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `DATA_INICIO_MATRICULA` | 2 / 2.1 | [1..1] | Data | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `DATA_FIM` | 2 / 2.1 | [0..1] | Data | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `DATA_CONCLUSAO_ENSINO_MEDIO` | 2 / 2.1 | [0..1] | Data | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `ESTUDANTE_ANO_PERIODO` | 2 / 2.1 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `ESTUDANTE_MATRICULA_INTEGRAL` | 2 / 2.1 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `CO_MATRICULA_REDE` | 2 / 2.1 | [0..1] | Alfanumérico com caracteres especiais | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `NOME_TURMA` | 2 / 2.1 | [0..1] | Numérico | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_TURMA` | 2 / 2.1 | [0..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `CO_ENTIDADE` | 2 / 2.1 | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `NO_ENTIDADE` | 2 / 2.1 | [1..1] | Alfanumérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_TURMA` | 2 / 2.2 | [1..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `NOME_TURMA` | 2 / 2.2 | [1..n] | Alfanumérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TURNO_TURMA` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TIPO_TURMA` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TURMA_ETAPA_DE_ENSINO` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `MODALIDADE_ENSINO_ESTUDANTE` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `OFERTA_EDUCACAO_ESPECIAL` | 2 / 2.2 | [0..1] | Código | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `TIPO_MEDIACAO_DIDATICO_PEDAGOGICA` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `DATA_INICIO_PERIODO_LETIVO` | 2 / 2.2 | [1..1] | Data | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `DATA_INICIO_TURMA` | 2 / 2.2 | [1..1] | Data | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `DATA_FIM_TURMA` | 2 / 2.2 | [0..1] | Data | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `ORGANIZACAO_CURRICULAR_TURMA` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TURMA_VAGAS` | 2 / 2.2 | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TURMA_LOCALIZACAO` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TURMA_FORMA_ORGANIZACAO` | 2 / 2.2 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TURMA_ORGANIZACAO_QUANTIDADE_ TOTAL` | 2 / 2.2 | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `TURMA_ORGANIZACAO_QUANTIDADE_ATUAL` | 2 / 2.2 | [0..1] | Numérico | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `CO_ENTIDADE` | 2 / 2.2 | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `CO_TURMA_REDE` | 2 / 2.2 | [0..1] | Alfanumérico com caracteres especiais | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_COMPONENTE_CURRICULAR` | 2 / 2.3 | [1..1] | Alfanumérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `CO_COMPONENTE_CURRICULAR_AREA_ CONHECIMENTO` | 2 / 2.3 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `CO_COMPONENTE_CURRICULAR` | 2 / 2.3 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `NOME_AREA_CONHECIMENTO_INSTITUICAO _ENSINO` | 2 / 2.3 | [0..1] | Alfabético | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `NOME_COMPONENTE_CURRICULAR_ INSTITUICAO_ENSINO` | 2 / 2.3 | [0..1] | Alfabético | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `COMPONENTE_CURRICULAR_CARGA_ HORARIA` | 2 / 2.3 | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `SISTEMA_AVALIACAO_DESEMPENHO` | 2 / 2.3 | [1..1] | Código | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_MATRICULA` | 2 / 2.4.a | [1..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_TURMA` | 2 / 2.4.a | [0..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_COMPONENTE_CURRICULAR` | 2 / 2.4.a | [1..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `MES_REFERENCIA` | 2 / 2.4.a | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `ANO_REFERENCIA` | 2 / 2.4.a | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `HL_OFERTADA_COMPONENTE_CURRICULAR_ PERIODO` | 2 / 2.4.a | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `HL_PRESENTE_COMPONENTE_CURRICULAR_ ESTUDANTE_PERIODO` | 2 / 2.4.a | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `JUSTIFICATIVA_SUSPENSAO_AULAS` | 2 / 2.4.a | [0..1] | Código | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_MATRICULA` | 2 / 2.4.b | [1..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_TURMA` | 2 / 2.4.b | [0..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `MES_REFERENCIA` | 2 / 2.4.b | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `ANO_REFERENCIA` | 2 / 2.4.b | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `HL_OFERTADA_TURMA_PERIODO` | 2 / 2.4.b | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `HL_PRESENTE_TURMA_ESTUDANTE_ PERIODO` | 2 / 2.4.b | [1..1] | Numérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `JUSTIFICATIVA_SUSPENSAO_AULAS` | 2 / 2.4.b | [0..1] | Código | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_MATRICULA` | 2 / 2.5 | [1..1] | Numérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_COMPONENTE_CURRICULAR` | 2 / 2.5 | [1..1] | Alfanumérico | Referência | [20-trajetoria.md](20-trajetoria.md) |
| `DESEMPENHO_ESTUDANTE_COMPONENTE_ CURRICULAR` | 2 / 2.5 | [1..1] | Alfanumérico | Registro | [20-trajetoria.md](20-trajetoria.md) |
| `SITUACAO_DESEMPENHO_ESTUDANTE_ COMPONENTE_CURRICULAR` | 2 / 2.5 | [0..1] | Código | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `NOME_COMPONENTE_CURRICULAR_ INSTITUICAO_ENSINO` | 2 / 2.5 | [0..1] | Alfabético | Complementar | [20-trajetoria.md](20-trajetoria.md) |
| `ID_SGP_PROFISSIONAL` | 3 | [1..1] | Numérico | Referência | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_IDENTIFICACAO_INSTITUICAO` | 3 | [0..1] | Numérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_CPF` | 3 | [1..1] | Numérico | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_NOME` | 3 | [1..1] | Alfabético | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_NOME_SOCIAL` | 3 | [0..1] | Alfabético | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_DT_NASCIMENTO` | 3 | [1..1] | Data | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_SEXO` | 3 | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_GENERO` | 3 | [0..1] | Código | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_RACA_COR` | 3 | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_QUILOMBOLA` | 3 | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_DEFICIENCIA` | 3 | [1..n] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_NACIONALIDADE` | 3 | [1..n] | Alfabético | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_CO_MUNICIPIO_RES` | 3 | [1..1] | Numérico | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_CO_UF_RES` | 3 | [1..1] | Numérico | Registro | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_CEP_RES` | 3 | [0..1] | Numérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_DS_LOGRADOURO_RES` | 3 | [0..1] | Alfanumérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_BAIRRO_RES` | 3 | [0..1] | Alfanumérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_NU_ENDERECO_RES` | 3 | [0..1] | Alfanumérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_LOCALIZACAO_GEOGRAFICA` | 3 | [0..1] | Código | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_LOCALIZACAO_DIFERENCIADA` | 3 | [0..1] | Código | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_TELEFONE` | 3 | [0..1] | Numérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_E_MAIL` | 3 | [0..1] | Alfanumérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `CO_NIVEL_ESCOLARIDADE` | 3 | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `CO_TIPO_ENSINO_MEDIO` | 3 | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `NATUREZA_INSTITUICAO_ MEDIO_PROFISSIONAL` | 3 | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `ID_FORMACAO` | 3 / Formação Acadêmica - Profissional Da Educação | [1..1] | Numérico | Registro | [30-profissionais.md](30-profissionais.md) |
| `CO_TIPO_FORMACAO_ACADEMICA` | 3 / Formação Acadêmica - Profissional Da Educação | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `CO_AREA_CONHECIMENTO_FORMACAO_ ACADEMICA` | 3 / Formação Acadêmica - Profissional Da Educação | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `NO_INSTITUICAO_ENSINO_FORMACAO_ ACADEMICA` | 3 / Formação Acadêmica - Profissional Da Educação | [0..1] | Alfabético | Complementar | [30-profissionais.md](30-profissionais.md) |
| `NATUREZA_INSTITUICAO_SUPERIOR_ PROFISSIONAL` | 3 / Formação Acadêmica - Profissional Da Educação | [0..1] | Código | Complementar | [30-profissionais.md](30-profissionais.md) |
| `ANO_INICIO_FORMACAO_ ACADEMICA` | 3 / Formação Acadêmica - Profissional Da Educação | [0..1] | Data | Complementar | [30-profissionais.md](30-profissionais.md) |
| `ANO_CONCLUSAO_FORMACAO_ACADEMICA` | 3 / Formação Acadêmica - Profissional Da Educação | [1..1] | Data | Registro | [30-profissionais.md](30-profissionais.md) |
| `CO_TIPO_VINCULO` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [1..1] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `SITUACAO_VINCULO_PROFISSIONAL_REDE` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [1..1] | Código | Referência | [30-profissionais.md](30-profissionais.md) |
| `DATA_INICIO_VINCULO_PROFISSIONAL_REDE` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [1..1] | Data | Registro | [30-profissionais.md](30-profissionais.md) |
| `DATA_FIM_VINCULO_PROFISSIONAL_REDE` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [0..1] | Data | Complementar | [30-profissionais.md](30-profissionais.md) |
| `CO_ENTIDADE` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [1..1] | Numérico | Registro | [30-profissionais.md](30-profissionais.md) |
| `CO_FUNCAO` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [1..n] | Código | Registro | [30-profissionais.md](30-profissionais.md) |
| `DATA_INGRESSO` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [1..1] | Data | Registro | [30-profissionais.md](30-profissionais.md) |
| `DATA_FIM` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [0..1] | Data | Complementar | [30-profissionais.md](30-profissionais.md) |
| `CARGA_HORARIA_SEMANAL` | 3 / Vínculo Do Profissional De Educação Com A Rede De Ensino | [0..1] | Numérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `ID_SGP_PROFISSIONAL` | 3 / Vínculo Do Profissional De Educação À Turmas E Componentes Curriculares | [1..1] | Numérico | Referência | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_TURMA` | 3 / Vínculo Do Profissional De Educação À Turmas E Componentes Curriculares | [1..n] | Alfanumérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `ID_SGP_TURMA` | 3 / Vínculo Do Profissional De Educação À Turmas E Componentes Curriculares | [1..n] | Numérico | Referência | [30-profissionais.md](30-profissionais.md) |
| `NOME_COMPONENTE_CURRICULAR_ INSTITUICAO_ENSINO` | 3 / Vínculo Do Profissional De Educação À Turmas E Componentes Curriculares | [1..n] | Alfabético | Complementar | [30-profissionais.md](30-profissionais.md) |
| `ID_SGP_COMPONENTE_CURRICULAR` | 3 / Vínculo Do Profissional De Educação À Turmas E Componentes Curriculares | [1..n] | Numérico | Referência | [30-profissionais.md](30-profissionais.md) |
| `PROFISSIONAL_IDENTIFICACAO_ INSTITUICAO` | 3 / Vínculo Do Profissional De Educação À Turmas E Componentes Curriculares | [1..n] | Numérico | Complementar | [30-profissionais.md](30-profissionais.md) |
| `CO_ENTIDADE` | 4 | [1..1] | Numérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `NO_ENTIDADE` | 4 | [1..1] | Alfabético | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `CO_MUNICIPIO_ENTIDADE` | 4 | [1..1] | Numérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `CO_UF_RES_ENTIDADE` | 4 | [1..1] | Numérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `CEP_INSTITUICAO` | 4 | [1..1] | Numérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `ENDERECO_INSTITUICAO` | 4 | [1..1] | Alfanumérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `DEP_ADMINISTRATIVA_INSTITUICAO` | 4 | [1..1] | Código | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `INSTITUICAO_LOCALIZACAO_GEOGRAFICA` | 4 | [1..1] | Código | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `INSTITUICAO_LOCALIZACAO_DIFERENCIADA` | 4 | [1..1] | Código | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `SITUACAO_FUNCIONAMENTO_INSTITUICAO` | 4 | [1..1] | Código | Situacional | [40-instituicoes.md](40-instituicoes.md) |
| `INSTITUICAO_E_MAIL` | 4 | [1..1] | Alfanumérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `INSTITUICAO_TELEFONE` | 4 | [1..1] | Numérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `INSTITUICAO_ETAPA_DE_ENSINO` | 4 | [1..n] | Código | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `CNPJ_UNIDADE_EXECUTORA` | 4 | [0..1] | Numérico | Complementar | [40-instituicoes.md](40-instituicoes.md) |
| `CNPJ_SECRETARIA_EDUCACAO` | 4 | [1..1] | Numérico | Registro | [40-instituicoes.md](40-instituicoes.md) |
| `LONGITUDE_INSTITUICAO_ENSINO` | 4 | [0..1] | Numérico | Complementar | [40-instituicoes.md](40-instituicoes.md) |
| `LATITUDE_INSTITUICAO_ENSINO` | 4 | [0..1] | Numérico | Complementar | [40-instituicoes.md](40-instituicoes.md) |
