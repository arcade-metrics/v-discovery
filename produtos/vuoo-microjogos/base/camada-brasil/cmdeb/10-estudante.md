# Estudante

> **Fonte:** Portaria MEC nº 832, de 16/12/2025 (DOU 17/12/2025), Anexo "Conjunto Mínimo de Dados da Educação Básica - CMDEB". MEC Normas: <https://mecnormas.mec.gov.br/pesquisa/detalhar/8017>. DOU: <https://www.in.gov.br/web/dou/-/portaria-mec-n-832-de-16-de-dezembro-de2025-675840850>. Coletado em 2026-11-04.

Bloco: **1. Registro do Estudante**. Colunas e categorias: ver [01-metodo.md](01-metodo.md). Domínios de código ficam na coluna Formatação, como na fonte (`<br>` = quebra de linha).

| Ocorr. | Nome do dado | Variável | Tipo | Formatação / domínio | Categoria |
|---|---|---|---|---|---|
| [1..1] | Número de Identificação (ID) do Estudante do Sistema Gestão Presente | ID_SGP_ESTUDANTE | Numérico | Sequência de caracteres numéricos | Referência |
| [1..1] | Número do CPF do Estudante | ESTUDANTE_CPF | Numérico | Sequência de 11 caracteres numérico, sem caracteres especiais (., -, ;) | Registro |
| [0..1] | Número de Identificação Social do Estudante | ESTUDANTE_NIS | Numérico | Sequência de 11 caracteres numérico, sem caracteres especiais (., -, ;) | Complementar |
| [1..1] | Nome Completo do Estudante | ESTUDANTE_NOME | Alfabético | Sequência de caracteres alfabéticos | Registro |
| [0..1] | Nome Social do Estudante | ESTUDANTE_NOME_SOCIAL | Alfabético | Sequência de caracteres alfabéticos | Complementar |
| [1..1] | Data de Nascimento do Estudante | ESTUDANTE_DT_NASCIMENTO | Data | Data no formato DD/MM/AAAA | Registro |
| [0..1] | Telefone de Contato do Estudante | ESTUDANTE_TELEFONE | Numérico | Telefone do estudante. Formato DDD-NNNNNNNNN | Complementar |
| [0..1] | E-mail de Contato do Estudante | ESTUDANTE_EMAIL | Alfanumérico com @ | E-mail do aluno utilizado para fins educacionais | Complementar |
| [1..1] | Nome Completo do Responsável 1 do Estudante | ESTUDANTE_RESPONSAVEL_1_NOME | Alfabético | Sequência de caracteres alfabéticos | Registro |
| [1..1] | Vínculo do Responsável 1 com o Estudante | ESTUDANTE_VINCULO_RESPONSAVEL_1 | Código | Código de acordo com o domínio:<br>0. Não informado<br>1. Relação de filiação (natural, adotiva ou socioafetiva);<br>2. Em programa de acolhimento (institucional ou familiar);<br>3. Tutela ou guarda regularizada;<br>4. Guarda de fato, não regularizada legalmente;<br>5. Não identificado/não consta registro; | Registro |
| [0..1] | Número do CPF do Responsável 1 do Estudante | RESPONSAVEL_1_CPF | Numérico | Sequência de 11 caracteres numérico, sem caracteres especiais (., -, ;) | Complementar |
| [0..1] | Telefone de Contato do Responsável 1 do Estudante | RESPONSAVEL_1_TELEFONE | Numérico | Telefone do responsável do estudante. Formato DDD-NNNNNNNNN | Complementar |
| [0..1] | E-mail de Contato do Responsável 1 do Estudante | RESPONSAVEL_1_E_MAIL | Alfanumérico com @ | Sequência de caracteres alfanuméricos | Complementar |
| [0..1] | Nome Completo do Responsável 2 do Estudante | ESTUDANTE_RESPONSAVEL_2_NOME | Alfabético | Sequência de caracteres alfabéticos | Complementar |
| [0..1] | Vínculo do Responsável 2 com o Estudante | ESTUDANTE_VINCULO_RESPONSAVEL_2 | Código | Código de acordo com o domínio:<br>0. Não informado<br>1. Relação de filiação (natural, adotiva ou socioafetiva);<br>2. Em programa de acolhimento (institucional ou familiar);<br>3. Tutela ou guarda regularizada;<br>4. Guarda de fato, não regularizada legalmente;<br>5. Não identificado/não consta registro; | Complementar |
| [0..1] | Número do CPF do Responsável 2 do Estudante | RESPONSAVEL_2_CPF | Numérico | Sequência de 11 caracteres numérico, sem caracteres especiais (., -, ;) | Complementar |
| [1..1] | Sexo do Estudante | ESTUDANTE_SEXO | Código | Código de acordo com o domínio:<br>0. Não informado<br>1. Masculino;<br>2. Feminino;<br>3. Intersexo;<br>4. Prefere não informar; | Registro |
| [1..1] | Raça/Cor do Estudante | ESTUDANTE_RACA_COR | Código | Código de acordo com domínio:<br>0. Não informado<br>1. Branco(a);<br>2. Preto(a);<br>3. Pardo(a);<br>4. Indígena;<br>5. Amarelo(a); | Registro |
| [1..1] | Estudante se Autodeclara Quilombola | ESTUDANTE_QUILOMBOLA | Código | Código de acordo com o domínio:<br>0. Não;<br>1. Sim; | Registro |
| [1..n] | Estudante com Deficiência, Transtorno do Espectro Autista ou Altas Habilidades/Superdotação | ESTUDANTE_DEFICIENCIA | Código | Código de acordo com o domínio:<br>0. Não informado;<br>1. Baixa visão;<br>2. Visão monocular;<br>3. Cegueira;<br>4. Deficiência auditiva;<br>5. Surdez;<br>6. ⁠Surdocegueira;<br>7. Deficiência física;<br>8. Deficiência intelectual;<br>9. Transtorno do espectro autista;<br>10. Altas habilidades/superdotação;<br>11. Não possui | Registro |
| [0..1] | Estudante com Necessidade Nutricional Individualizada | ESTUDANTE_NECESSIDADE_NUTRICIONAL | Código | Código de acordo com o domínio:<br>1. Sim<br>2. Não<br>0. Não informado | Complementar |
| [1..n] | Código do país de nacionalidade do Estudante | ESTUDANTE_NACIONALIDADE | Código | Código numérico da ISO 3166-1 (códigos internacionais de países) | Registro |
| [1..1] | Código IBGE do Município de Residência do Estudante | ESTUDANTE_CO_MUNICIPIO_RES | Numérico | Sequência de 7 caracteres numéricos | Registro |
| [0..1] | CEP de Residência do Estudante | ESTUDANTE_CEP_RES | Numérico | Sequência de 8 caracteres numéricos | Complementar |
| [0..1] | Endereço de Residência do Estudante (Logradouro) | ESTUDANTE_LOGRADOURO_RES | Alfanumérico | Sequência de até 1000 caracteres alfanuméricos | Complementar |
| [0..1] | Bairro de Residência do Estudante | ESTUDANTE_BAIRRO_RES | Alfanumérico | Sequência de até 1000 caracteres alfanuméricos | Complementar |
| [0..1] | Número da Residência do Estudante | ESTUDANTE_NU_ENDERECO_RES | Alfanumérico | Sequência de até 6 caracteres alfanuméricos. Caso não possua número informar 00. | Complementar |
| [0..1] | Localização Geográfica da Residência do Estudante | ESTUDANTE_LOCALIZACAO_GEOGRAFICA | Código | Código de acordo com domínio:<br>0. Não informado;<br>1. Urbana;<br>2. Rural; | Complementar |
| [0..1] | Localização Diferenciada do Estudante | ESTUDANTE_LOCALIZACAO_DIFERENCIADA | Código | Código de acordo com domínio:<br>0. Não informado;<br>1. Não está em área de localização diferenciada;<br>2. Comunidade quilombola;<br>3. Terra indígena;<br>4. Área de assentamento;<br>5. Área onde se localizam povos e comunidades tradicionais; | Complementar |

