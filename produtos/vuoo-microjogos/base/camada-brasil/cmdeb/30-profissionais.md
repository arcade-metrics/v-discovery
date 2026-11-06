# Profissionais da educação

> **Fonte:** Portaria MEC nº 832, de 16/12/2025 (DOU 17/12/2025), Anexo "Conjunto Mínimo de Dados da Educação Básica - CMDEB". MEC Normas: <https://mecnormas.mec.gov.br/pesquisa/detalhar/8017>. DOU: <https://www.in.gov.br/web/dou/-/portaria-mec-n-832-de-16-de-dezembro-de2025-675840850>. Coletado em 2026-11-04.

Bloco: **3. Registro dos Profissionais da Educação**. Colunas e categorias: ver [01-metodo.md](01-metodo.md). Domínios de código ficam na coluna Formatação, como na fonte (`<br>` = quebra de linha).

| Ocorr. | Nome do dado | Variável | Tipo | Formatação / domínio | Categoria |
|---|---|---|---|---|---|
| [1..1] | Número de Identificação (ID) do Profissional da Educação Gerado pelo Sistema Gestão Presente | ID_SGP_PROFISSIONAL | Numérico | Sequência de caracteres numéricos | Referência |
| [0..1] | Número de Identificação (ID) da Matrícula do Profissional da Educação Gerado pela Rede/Instituição de Ensino | PROFISSIONAL_IDENTIFICACAO_INSTITUICAO | Numérico | Sequência de caracteres numéricos | Complementar |
| [1..1] | Número do CPF do Profissional de Educação | PROFISSIONAL_CPF | Numérico | Sequência de 11 caracteres numérico, sem caracteres especiais (., -, ;) | Registro |
| [1..1] | Nome Completo do Profissional da Educação | PROFISSIONAL_NOME | Alfabético | Sequência de caracteres alfabéticos | Registro |
| [0..1] | Nome Social do Profissional da Educação | PROFISSIONAL_NOME_SOCIAL | Alfabético | Sequência de caracteres alfabéticos | Complementar |
| [1..1] | Data de Nascimento do Profissional da Educação | PROFISSIONAL_DT_NASCIMENTO | Data | Data no formato DD/MM/AAAA | Registro |
| [1..1] | Sexo do Profissional da Educação | PROFISSIONAL_SEXO | Código | Código de acordo com o domínio:<br>1. Masculino;<br>2. Feminino;<br>3. Intersexo<br>4. Prefere não informar; | Registro |
| [0..1] | Gênero do Profissional da Educação | PROFISSIONAL_GENERO | Código | Código de acordo com o domínio:<br>0. Não informado;<br>1. Cisgênero;<br>2. Transgênero;<br>3. Não-binário;<br>4. Outro;<br>5. Prefiro não informar; | Complementar |
| [1..1] | Raça/Cor do Profissional da Educação | PROFISSIONAL_RACA_COR | Código | Código de acordo com o domínio:<br>0. Não informado;<br>1. Branco(a);<br>2. Preto(a);<br>3. Pardo(a);<br>4. Indígena;<br>5. Amarelo(a); | Registro |
| [1..1] | Profissional da Educação se Autodeclara Quilombola | PROFISSIONAL_QUILOMBOLA | Código | Código de acordo com o domínio:<br>1. Sim<br>2. Não<br>0. Não informado | Registro |
| [1..n] | Profissional da Educação com Deficiência, TEA ou Altas Habilidades/Superdotação | PROFISSIONAL_DEFICIENCIA | Código | Código de acordo com o domínio:<br>0. Não informado;<br>1. Baixa visão;<br>2. Visão monocular;<br>3. Cegueira;<br>4. Deficiência auditiva;<br>5. Surdez;<br>6. ⁠Surdocegueira;<br>7. Deficiência física;<br>8. Deficiência intelectual;<br>9. Transtorno do espectro autista;<br>10. Altas habilidades/superdotação;<br>11. Não possui | Registro |
| [1..n] | Nacionalidade do Profissional da Educação | PROFISSIONAL_NACIONALIDADE | Alfabético | Sequência de caracteres alfabéticos | Registro |
| [1..1] | Código IBGE do Município de Residência do Profissional da Educação | PROFISSIONAL_CO_MUNICIPIO_RES | Numérico | Sequência de 7 caracteres numéricos | Registro |
| [1..1] | Código IBGE do Estado de Residência do Profissional da Educação | PROFISSIONAL_CO_UF_RES | Numérico | Sequência de 2 caracteres numérico | Registro |
| [0..1] | CEP de Resdiência do Profissional da Educação | PROFISSIONAL_CEP_RES | Numérico | Sequência de 8 caracteres numéricos | Complementar |
| [0..1] | Endereço de Residência do Estudante (Logradouro) | PROFISSIONAL_DS_LOGRADOURO_RES | Alfanumérico | Sequência de até 1000 caracteres alfanuméricos | Complementar |
| [0..1] | Bairro de Residência do Profissional da Educação | PROFISSIONAL_BAIRRO_RES | Alfanumérico | Sequência de até 1000 caracteres alfanuméricos | Complementar |
| [0..1] | Número da Residência do Profissional da Educação | PROFISSIONAL_NU_ENDERECO_RES | Alfanumérico | Sequência de até 6 caracteres alfanuméricos. Caso não possua número informar 00 | Complementar |
| [0..1] | Localização Geográfica da Residência do Profissional da Educação | PROFISSIONAL_LOCALIZACAO_GEOGRAFICA | Código | Código de acordo com domínio:<br>0. Não informado;<br>1. Urbana;<br>2. Rural; | Complementar |
| [0..1] | Localização Diferenciada do Profissional da Educação | PROFISSIONAL_LOCALIZACAO_DIFERENCIADA | Código | Código de acordo com domínio:<br>0. Não informado;<br>1. Não está em área de localização diferenciada;<br>2. Comunidade quilombola;<br>3. Terra indígena;<br>4. Área de assentamento;<br>5. Área onde se localizam povos e comunidades tradicionais; | Complementar |
| [0..1] | Telefone de Contato do Profissional da Educação | PROFISSIONAL_TELEFONE | Numérico | Formato do telefone (DDD) NNNNNNNNN | Complementar |
| [0..1] | E-mail do Profissional da Educação | PROFISSIONAL_E_MAIL | Alfanumérico | E-mail do profissional da educação | Complementar |
| [1..1] | Nível de Escolaridade do Profissional da Educação | CO_NIVEL_ESCOLARIDADE | Código | Código de acordo com o domínio:<br>0. Não informado;<br>1. Ensino Fundamental Incompleto;<br>2. Ensino Fundamental Completo;<br>3. Ensino Médio Incompleto;<br>4. Ensino Médio Completo;<br>5. Ensino Técnico Completo;<br>6. Ensino Superior Incompleto;<br>7. Ensino Superior Completo;<br>8. Pós-graduação - Especialização;<br>9. Pós-graduação - Mestrado;<br>10. Pós-graduação - Doutorado;<br>11. Sem instrução | Registro |
| [1..1] | Tipo de Ensino Médio Cursado pelo Profissional da Educação | CO_TIPO_ENSINO_MEDIO | Código | Códigos de acordo com o domínio:<br>0. Não Informado;<br>1. Formação geral;<br>2. Modalidade normal / magistério;<br>3. Curso técnico;<br>4. Magistério indígena - modalidade normal; | Registro |
| [1..1] | Natureza Administrativa da Instituição do Ensino Médio do Profissional da Educação | NATUREZA_INSTITUICAO_ MEDIO_PROFISSIONAL | Código | Códigos de acordo com o domínio:<br>0. Não informada;<br>1. Pública;<br>2. Privada; | Registro |

## FORMAÇÃO ACADÊMICA - PROFISSIONAL DA EDUCAÇÃO

| Ocorr. | Nome do dado | Variável | Tipo | Formatação / domínio | Categoria |
|---|---|---|---|---|---|
| [1..1] | Número de Identificação (ID) da Formação do Profissional Gerado pelo Sistema Gestão Presente | ID_FORMACAO | Numérico | Sequência de caracteres numéricos | Registro |
| [1..1] | Tipo da Formação Acadêmica | CO_TIPO_FORMACAO_ACADEMICA | Código | Códigos de acordo com o domínio:<br>0. Não Informada;<br>1. Formação Superior - Tecnológico;<br>2. Formação Superior - Licenciatura;<br>3. Formação Superior - Bacharelado;<br>5. Pós-graduação - Especialização;<br>6. Pós-graduação - Mestrado;<br>7. Pós-graduação - Doutorado;<br>8. Formação Técnica; | Registro |
| [1..1] | Área de Conhecimento da Formação Acadêmica | CO_AREA_CONHECIMENTO_FORMACAO_ ACADEMICA | Código | Código de acordo com domínio:<br>0. Não informada;<br>1. Educação;<br>2. Artes e humanidades;<br>3. Ciências sociais, comunicação e informação;<br>4. Negócios, administração e direito;<br>5. Ciências naturais, matemática e estatística;<br>6. Computação e Tecnologias da Informação e Comunicação (TIC);<br>7. Engenharia, produção e construção;<br>8. Agricultura, silvicultura, pesca e veterinária;<br>9. Saúde e bem-estar;<br>10. Serviços;<br>99. Programas básicos; | Registro |
| [0..1] | Nome da Instituição de Ensino Superior da Formação do Profissional da Educação | NO_INSTITUICAO_ENSINO_FORMACAO_ ACADEMICA | Alfabético | Sequência de caracteres alfabéticos | Complementar |
| [0..1] | Natureza Administrativa da Instituição de Ensino Superior da Formação do Profissional da Educação | NATUREZA_INSTITUICAO_SUPERIOR_ PROFISSIONAL | Código | Códigos de acordo com o domínio:<br>0. Não informada;<br>1. Pública;<br>2. Privada; | Complementar |
| [0..1] | Ano de Início do Ensino Superior do Profissional da Educação | ANO_INICIO_FORMACAO_ ACADEMICA | Data | Ano no formato AAAA | Complementar |
| [1..1] | Ano de Conclusão do Ensino Superior do Profissional da Educação | ANO_CONCLUSAO_FORMACAO_ACADEMICA | Data | Ano no formato AAAA | Registro |

## VÍNCULO DO PROFISSIONAL DE EDUCAÇÃO COM A REDE DE ENSINO

| Ocorr. | Nome do dado | Variável | Tipo | Formatação / domínio | Categoria |
|---|---|---|---|---|---|
| [1..1] | Tipo de Vínculo Empregatício com a Rede de Ensino | CO_TIPO_VINCULO | Código | Código de acordo com o domínio:<br>0. Não informado;<br>1. Estatutário efetivo;<br>2. Contrato temporário;<br>3. Terceirizado;<br>4. Contrato CLT;<br>5. Cargo comissionado; | Registro |
| [1..1] | Situação do Vínculo do Profissional da Educação com a Rede de Ensino | SITUACAO_VINCULO_PROFISSIONAL_REDE | Código | Códigos de acordo com o domínio:<br>1. Ativo;<br>2. Inativo;<br>3. Suspenso;<br>4. Licença;<br>5. Readaptado;<br>0. Não Aplicável; | Referência |
| [1..1] | Data de Início do Vínculo do Profissional da Educação com a Rede de Ensino | DATA_INICIO_VINCULO_PROFISSIONAL_REDE | Data | Data no formato DD/MM/AAAA | Registro |
| [0..1] | Data do Fim do Vínculo do Profissional da educação com a Rede de Ensino | DATA_FIM_VINCULO_PROFISSIONAL_REDE | Data | Data no formato DD/MM/AAAA | Complementar |
| [1..1] | Código do INEP da Instituição que o Profissional da Educação está Lotado | CO_ENTIDADE | Numérico | Sequência de caracteres numéricos | Registro |
| [1..n] | Função Exercida pelo Profissional da Educação na Rede/Instituição de Ensino | CO_FUNCAO | Código | Código de acordo com o domínio:<br>Dentro da sala de aula:<br>1. Docente;<br>2. Tradutor(a) e Intérprete de Libras;<br>3. Guia-Intérprete;<br>4. Auxiliar/assistente educacional;<br>5. Docente titular - coordenador(a) de tutoria (de módulo ou disciplina) - EaD;<br>6. Profissional de apoio escolar para alunos com deficiência (Lei nº 13.146/2015);<br>7. Profissional/monitor de atividade complementar;<br>8. Docente tutor(a) - auxiliar (de módulo ou disciplina) - EaD;<br>9. Instrutor(a) de educação profissional;<br>Na instituição de ensino:<br>10. Diretor(a);<br>16. Vice Diretor(a)<br>11. Coordenador(a) Pedagógico(a);<br>12. Secretário(a) Escolar;<br>15. Merendeira;<br>17. Auxiliar na escola<br>Na secretaria de educação:<br>14. Gestor (a)<br>Demais funções:<br>99. Outros | Registro |
| [1..1] | Data de Início da Função Exercida pelo Profissional da Educação na Rede/Instituição de Ensino | DATA_INGRESSO | Data | Data no formato DD/MM/AAAA | Registro |
| [0..1] | Data do Fim da Função Exercida pelo Profissional da Educação na Rede/Instituição de Ensino | DATA_FIM | Data | Data no formato DD/MM/AAAA | Complementar |
| [0..1] | Carga Horária de Trabalho do Profissional da Educação | CARGA_HORARIA_SEMANAL | Numérico | Sequência de caracteres numéricos | Complementar |

## VÍNCULO DO PROFISSIONAL DE EDUCAÇÃO À TURMAS E COMPONENTES CURRICULARES

| Ocorr. | Nome do dado | Variável | Tipo | Formatação / domínio | Categoria |
|---|---|---|---|---|---|
| [1..1] | Número de Identificação (ID) do Profissional da Educação Gerado pelo Sistema Gestão Presente | ID_SGP_PROFISSIONAL | Numérico | Sequência de caracteres numéricos | Referência |
| [1..n] | Nome da Turma Vinculada ao Profissional na Instituição de Ensino | PROFISSIONAL_TURMA | Alfanumérico | Sequência de caracteres alfanuméricos | Complementar |
| [1..n] | Número de Identificação (ID) da Turma do Estudante Gerado pelo Sistema Gestão Presente | ID_SGP_TURMA | Numérico | Sequência de caracteres numéricos | Referência |
| [1..n] | Nome do Componente Curricular Vinculado ao Profissional na Instituição de Ensino | NOME_COMPONENTE_CURRICULAR_ INSTITUICAO_ENSINO | Alfabético | Sequência de caracteres alfabéticos | Complementar |
| [1..n] | Número de Identificação (ID) do Componente Curricular Gerado pelo Sistema Gestão Presente | ID_SGP_COMPONENTE_CURRICULAR | Numérico | Sequência de caracteres numéricos | Referência |
| [1..n] | Número de Identificação (ID) da Matrícula do Profissional da Educação Gerado pela Rede/Instituição de Ensino | PROFISSIONAL_IDENTIFICACAO_ INSTITUICAO | Numérico | Sequência de caracteres numéricos | Complementar |

