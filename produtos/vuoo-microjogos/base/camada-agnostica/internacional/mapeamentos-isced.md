# Mapeamentos ISCED 2011 por país (UIS)

Pivô proposto para o crosswalk de níveis educacionais do Core (C.PRG). Fonte única: as planilhas de **mapeamento ISCED 2011 validadas pelo UIS**, uma por país, publicadas em [uis.unesco.org/en/isced-mappings](https://uis.unesco.org/en/isced-mappings) [N04]. Acesso em 2026-11-05. As planilhas foram baixadas com `curl.exe` para `D:\tmp\isced_dl\` (fora do repositório) e lidas célula a célula; aba e coluna estão indicadas em cada tabela.

O que é um mapeamento, segundo o UIS: "the conversion of a national education system into the international agreed categories defined by ISCED"; os mapeamentos se baseiam na resposta de cada Estado-membro ao questionário do UIS e são acrescentados "on a rolling basis" [N03, p. 3]; "At present, ISCED mappings are available for two hundred and one (201) countries" [N03, p. 4].

## 0. Leitura das tabelas

| Coluna | Significado | Origem na planilha |
|---|---|---|
| Programa nacional | nome no idioma nacional, como está na planilha | "Name of the programme in national language" |
| Idade teórica | "Theoretical starting age" | idem |
| Duração | "Theoretical duration of the programme" (anos) | idem |
| ISCED-P | código de programa, 3 dígitos | "ISCED-2011 level (ISCED-P, 3-digits)" |
| ISCED-A | código de escolaridade obtida ao concluir | "ISCED-2011 level of qualification/educational attainment (ISCED-A, 3 digits)" |

Códigos explicados em [terminologia.md](terminologia.md). Programas de adultos (EJA, *ensino recorrente*, *Abendschulen*), de reconhecimento de competências e a maior parte da educação profissional foram **omitidos** aqui por não serem foco da VUOO; constam nas planilhas.

Há dois modelos de planilha: Brasil (2012/2013) usa o modelo antigo (aba "Scope UOE", colunas D–Z); EUA, Portugal, Alemanha e Reino Unido usam o modelo UOE mais novo (aba "Scope UOE", ISCED-P na coluna T, ISCED-A na coluna AA); China usa uma aba única ("Sheet1") com layout próprio.

## 1. Brasil

Fonte: `ISCED_2011_Mapping_Brazil.xlsx` [N05], aba "Scope UOE", linhas 3–14. **Ano de referência: 2012/2013** (coluna B). O arquivo é anterior à BNCC (2017/2018) e ao Novo Ensino Médio; a planilha antiga lista o arquivo como de 02/02/2016 [N04, listagem de busca].

| Etapa nacional | Idade teórica | Duração | Anos acumulados desde o início do ISCED 1 (col. K) | ISCED-P | ISCED-A |
|---|---|---|---|---|---|
| Educação Infantil – creche | 0 | 3 | — | 010 | 020 |
| Educação Infantil – pré-escola | 4 | 2 | — | 020 | 020 |
| Ensino Fundamental do 1º ao 5º ano | 6 | 5 | 5 | 100 | 100 |
| Ensino Fundamental (de 6º ao 9º ano) | 11 | 4 | 9 | 244 | 244 |
| Ensino Médio | 15 | 3 | 12 | 344 | 344 |
| Educação Profissional de Nível Médio (integrada e concomitante) | 15 | 3 | 12 | 354 | 354 |
| Formação de Professores na Modalidade Normal em Nível Médio | 15 | 3 | 12 | 354 | 354 |
| Educação Profissional de Nível Médio (subsequente) | 18 | 1 | 13 | 451 | 354 |

Escolaridade obrigatória e gratuita (aba "Compulsory and free education", linhas 10 e 20): **4 a 17 anos, 14 anos de duração**, com nota do UIS citando a Lei 12.796/2013 e a EC 59/2009 [N05].

Observações:
- A creche recebe ISCED-P 010 e ISCED-A 020 na mesma linha; pela lógica do ISCED-A, frequentar ECED não equivale a ter frequentado pré-primária [I]. Registrado em [questoes-abertas.md](questoes-abertas.md) (QI-03).
- A planilha usa idade teórica 11 para o 6º ano; com entrada aos 6 no 1º ano, o 6º ano começa aos 11 [I, coerente].
- Não há linha para Educação Especial nem para AEE: no Brasil o AEE é transversal às etapas [I; ver `acs.br.*` em `conhecimento/`].

## 2. Estados Unidos

Fonte: `ISCED_2011_Mapping_United_States_of_America.xlsx` [N06], aba "Scope UOE". **Ano de referência: 2020/2021** (coluna C).

| Programa nacional | Idade teórica | Duração | ISCED-P | ISCED-A |
|---|---|---|---|---|
| Head Start / Public preschool or pre-kindergarten / Private Preschool | 3–5 | 1–3 | 020 | 020 |
| Kindergarten | 4–6 | 1 | 020 | 020 |
| Elementary education (grades 1-6) | 5–7 | 6 | 100 | 100 |
| Middle education (grades 7-9) | 11–13 | 3 | 244 | 244 |
| Secondary/High school education (grades 10-12) | 14–17 | 3 | 344 | 344, 354 |
| GED or High school equivalency Programme | 16+ | "Missing (O)" | 344 | 344 |
| Special education | "Missing (O)" | "Missing (O)" | "020, 100, 244, 344" | 900 |
| English as a second language | "Missing (O)" | "Missing (O)" | "020, 100, 244, 344" | 900 |

Escolaridade obrigatória (aba "Compulsory and free education", linha 11): início **4–6**, fim **16**, com a nota "The age range for compulsory education in the USA varies by subnational entity" [N06].

Observações:
- O UIS adota o corte 1–6 / 7–9 / 10–12. Muitas redes usam 6–8 (*middle*) e 9–12 (*high*); o mapeamento nacional não representa essa variação estadual [I]. Para o adaptador EUA, o pivô deve ser a **série** (grade), não o nome da escola [I].
- *Special education* aparece como programa que atravessa os níveis 020–344, sem nível próprio. É o único dos seis mapeamentos que lista educação especial como linha [N06].

## 3. União Europeia: Portugal (representativo) e Alemanha

### 3.1 Portugal

Fonte: `ISCED_2011_Mapping_Portugal.xlsx` [N07], aba "Scope UOE". **Ano de referência: 2020/2021**.

| Programa nacional | Idade teórica | Duração | ISCED-P | ISCED-A |
|---|---|---|---|---|
| Educação pré-escolar | 3–5 | 3 | 020 | 020 |
| 1.º Ciclo do ensino básico – Ensino regular | 6 | 4 | 100 | 100 |
| 2.º Ciclo do ensino básico – Ensino regular | 10 | 2 | 100 | 100 |
| 3.º Ciclo do ensino básico – Ensino regular | 12 | 3 | 244 | 244 |
| 3.º Ciclo do ensino básico – Cursos profissionais | 12 | 3 | 254 | 254 |
| Ensino secundário – Regular – Cursos científico-humanísticos | 15 | 3 | 344 | 344 |
| Ensino secundário – Cursos profissionais | 15 | 3 | 354 | 354 |

Escolaridade obrigatória: **6 a 18 anos, 12 anos** (linha 11) [N07].

Observação: o 2.º ciclo (5.º e 6.º anos) é ISCED 1. Uma etapa nacional chamada "ensino básico" atravessa os níveis 1 e 2; o nome não decide o nível [N07].

### 3.2 Alemanha

Fonte: `ISCED_2011_Mapping_Germany.xlsx` [N08], aba "Scope UOE". **Ano de referência: 2020/21**.

| Programa nacional | Idade teórica | Duração | ISCED-P | ISCED-A |
|---|---|---|---|---|
| Krippen (unter 3 Jahren) | 0 | "up to 3 years" | 010 | 000 |
| Kindergärten (3 Jahre bis Schuleintritt) | 3 | 3 | 020 | 000 |
| Grundschulen | 6 | 4 | 100 | 100 |
| Förderschulen (Klassen 1–4) | 6 | 4 | 100 | 100 |
| Schulartunabhängige Orientierungsstufe (Klassen 5 und 6) | 10 | 2 | 241 | "a" |
| Hauptschulen / Realschulen / Gymnasien (Klassen 5–9/10) / Integrierte Gesamtschulen | 10 | 5–6 | 244 | 244 |
| Förderschulen (Klassen 5–10) | 10 | 5–6 | 244 | 244 |
| Gymnasien (Klassen 11–13 oder 10–12, gymnasiale Oberstufe) | 15/16–18 | 3 | 344 | 344 |
| Berufsschulen (Duales System) Erstausbildung | 16–18 | 3 | 354 | 354 |

Escolaridade obrigatória: **6 a 18 anos, 13 anos** (linha 11) [N08]. O ISCED-A "000" na educação infantil e o "a" (não aplicável) são grafias da própria planilha.

Observações:
- Escolas especiais (*Förderschulen*) são mapeadas no **mesmo nível** dos programas regulares; há ainda "Prog.9.1", alunos de educação especial que não podem ser alocados a um nível [N08]. Para a VUOO, isso confirma que educação especial é atributo transversal (C.SUP/C.PLN), não nível (C.PRG) [I].
- Grundschule de 4 anos é o padrão do arquivo; estados com 6 anos de primária (ex.: Berlim) não aparecem separados [I; não verificado].

## 4. Reino Unido (Inglaterra e Escócia)

Fonte: `ISCED_2011_Mapping_United_Kingdom.xlsx` [N09], aba "Scope UOE". **Ano de referência: 2020/2021**. O arquivo cobre o Reino Unido inteiro e separa linhas por nação quando os programas diferem.

| Programa nacional | Nação | Idade teórica | Duração | ISCED-P | ISCED-A |
|---|---|---|---|---|---|
| Day nurseries / Children's Centres / Registered childminders | UK | 0 | 3 | 010 | "10" |
| Reception and nursery classes in schools | UK | 3 | 1–2 | 020 | "20" |
| Primary school (Keystage 1-2) | UK | 4–5 | 6–7 | 100 | 100 |
| Secondary school (KeyStage 3) | Inglaterra, País de Gales, Irlanda do Norte | 11 | 3 | 244 | 244 |
| Secondary school (National 1-4 / Intermediate 1) | Escócia | 12 | 3 | 244 | 244 |
| Secondary School (Keystage 4) | Inglaterra, País de Gales, Irlanda do Norte | 14 | 2 | 342 | "244, 342 if 5+ grades 9-4 gained (previously A*-C)" |
| Secondary School (National 5 / Intermediate 2) | Escócia | 15 | 1 | 342 | 244 |
| A Level | Inglaterra, País de Gales, Irlanda do Norte | 16 | 2 | 344 | 344 |
| T Level | Inglaterra | 16 | 2 | 354 | 354 |
| Higher | Escócia | 16 | 1 | 344 | 343 |
| Advanced Higher | Escócia | 17 | 1 | 344 | 344 |

Escolaridade obrigatória (código GB): **5 a 18 anos, 13 anos** (linha 11) [N09]. A planilha não separa idades por nação nesse campo.

Observações:
- KS4/GCSE é ISCED-P **342** (conclusão parcial do nível 3). O ISCED-A depende do **resultado** (244 ou 342 conforme notas) [N09]: a escolaridade obtida não é função só do programa cursado. O Core precisa guardar programa (C.PRG/C.ENR) e resultado (C.RES/C.CRD) separados [I].
- *Reception* aparece como 020 enquanto a primária declara idade inicial 4–5 e duração 6–7: a planilha deixa ambígua a fronteira entre Reception e Year 1 [I]. Ver QI-04.

## 5. China

Fonte: `ISCED_2011_Mapping_China.xlsx` [N10], aba "Sheet1", linhas 7–11. **Ano de referência: 2023** (célula A3: "School Year reference: 2023").

| Programa nacional | Inglês (planilha) | Idade teórica | Duração | ISCED-P | ISCED-A |
|---|---|---|---|---|---|
| 学前教育 | Pre-primary education | 3 | 3 | 020 | 020 |
| 小学 | Primary education | 6 | 6 | 100 | 100 |
| 普通初中 | Junior secondary education | 12 | 3 | 244 | 244 |
| 普通高中 | Senior secondary education | 15 | 3 | 344 | 344 |
| 职业高中 | Vocational high school education | 15 | 3 | 354 | 354 |

Nota da linha 9: a participação do ISCED 2 profissional "is small and decreasing since 2013" [N10]. A planilha da China não traz a aba de escolaridade obrigatória; a duração da obrigatória fica `not_found` nesta fonte.

## 6. Síntese para o Core (proposta)

| País | Ano ref. | Primária (ISCED 1) | Sec. inferior (ISCED 2) | Sec. superior (ISCED 3) | Obrigatória |
|---|---|---|---|---|---|
| Brasil | 2012/13 | EF 1º–5º, 6 anos, 5 a | EF 6º–9º, 11 anos, 4 a | EM, 15 anos, 3 a | 4–17 |
| EUA | 2020/21 | grades 1–6, 5–7 anos, 6 a | grades 7–9, 11–13 anos, 3 a | grades 10–12, 14–17 anos, 3 a | 4–6 a 16 (varia) |
| Portugal | 2020/21 | 1.º+2.º ciclos, 6 anos, 4+2 a | 3.º ciclo, 12 anos, 3 a | secundário, 15 anos, 3 a | 6–18 |
| Alemanha | 2020/21 | Grundschule, 6 anos, 4 a | Sek I, 10 anos, 5–6 a | Sek II, 15/16 anos, 3 a | 6–18 |
| RU (Ing.) | 2020/21 | KS1–2, 4–5 anos, 6–7 a | KS3, 11 anos, 3 a | KS4 (342) + A level (344), 14/16 anos | 5–18 (UK) |
| RU (Esc.) | 2020/21 | primária (UK) | S1–S3, 12 anos, 3 a | National 5 / Higher / Adv. Higher | 5–18 (UK) |
| China | 2023 | 小学, 6 anos, 6 a | 初中, 12 anos, 3 a | 高中, 15 anos, 3 a | not_found |

Consequências para o desenho [I]:
1. **ISCED é pivô de nível, não de série.** Nenhum mapeamento desce ao ano/série; a granularidade é o programa nacional. Para crosswalk série↔série, o Core precisa de um ordinal próprio. Candidato: "anos acumulados desde o início do ISCED 1", que é coluna explícita no modelo antigo do UIS (Brasil, col. K) [N05]. Ver QI-01.
2. **Uma etapa nacional pode cruzar níveis** (Portugal: ensino básico = ISCED 1+2; Brasil: Ensino Fundamental = ISCED 1+2). C.PRG deve permitir que o nível ISCED seja atribuído ao segmento (anos iniciais/finais), não ao nome da etapa.
3. **Educação especial não é nível** em nenhum dos seis mapeamentos; aparece transversal (EUA, "020, 100, 244, 344") ou embutida (Alemanha, Förderschulen nos níveis regulares).
4. **Ano de referência importa.** O mapeamento do Brasil é de 2012/2013; os demais vão de 2020/2021 a 2023. O Core deve versionar o mapeamento (C.PRV: fonte, ano de referência, data de acesso) e não tratá-lo como fato perene.
5. **A revisão do ISCED está em curso** (painel criado em junho de 2023; recomendações de emenda ao ISCED-P/A e revisão ampla do ISCED-F) [N02; N03, pp. 5–6]. O código ISCED no Core deve levar `scheme = isced-2011` explícito para permitir conviver com a edição seguinte.
