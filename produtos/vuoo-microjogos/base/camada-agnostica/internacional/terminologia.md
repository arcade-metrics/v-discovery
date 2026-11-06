# Terminologia — padrões internacionais transversais

Códigos e vocabulários controlados que o Core pode reutilizar. Acesso às fontes em 2026-11-05. Fontes em [evidencias.md](evidencias.md).

**Limite desta transcrição.** O PDF oficial do ISCED 2011 (UIS, 2012) e o do ISCED-F 2013 não puderam ser abertos nesta sessão: as URLs do UIS responderam 404 e o UNESDOC respondeu 403 ao acesso automatizado [N11, N12]. As tabelas abaixo foram montadas assim:
- nomes dos níveis e campos amplos: Eurostat [N14] e FAQ oficial do UIS [N03];
- dimensões e legenda de códigos: legenda oficial embutida na planilha de mapeamento da China [N10, linhas 22–34] e páginas BIBB [N15];
- campos estreitos e detalhados do ISCED-F: reprodução do "Appendix 1" do ISCED-F 2013 em documento universitário [N12, secundária];
- lista completa de códigos ISCED-P/A de 3 dígitos: conhecimento prévio do Anexo do ISCED 2011, **conferido** contra todos os códigos efetivamente usados nos seis mapeamentos [N05–N10]. Linhas marcadas **[conferir]** não aparecem em nenhum mapeamento lido e precisam ser checadas no PDF antes de virar dado do Core.

## 1. ISCED 2011: níveis (1º dígito)

| Código | Nível (en) | Nível (pt, tradução de trabalho) | Idade teórica de entrada nos 6 mapeamentos |
|---|---|---|---|
| 0 | Early childhood education ("less than primary" para escolaridade) | Educação na primeira infância | 0 (010); 3–5 (020) |
| 1 | Primary education | Ensino primário | 4–7 |
| 2 | Lower secondary education | Ensino secundário inferior | 10–13 |
| 3 | Upper secondary education | Ensino secundário superior | 14–16 |
| 4 | Post-secondary non-tertiary education | Pós-secundário não superior | 18 |
| 5 | Short-cycle tertiary education | Superior de ciclo curto | 18 |
| 6 | Bachelor's or equivalent level | Bacharelado ou equivalente | 18 |
| 7 | Master's or equivalent level | Mestrado ou equivalente | 22 |
| 8 | Doctoral or equivalent level | Doutorado ou equivalente | 22–25 |

Nomes: [N14]. Idades: colunas de idade teórica dos mapeamentos [N05–N10]. ISCED 2011 foi adotado pela 36ª Conferência Geral da UNESCO, em novembro de 2011, e publicado em 2012 [N01; N11, metadados].

Critérios de classificação (resumo; **[conferir]** no texto do ISCED 2011, §§ dos níveis 1–3): o nível 1 tem entrada típica entre 5 e 7 anos e duração típica de 6 anos (faixa 4–7); o nível 2 dura tipicamente 3 anos (faixa 2–5); o nível 3 tem entrada típica entre 14 e 16 anos e se completa tipicamente 12 a 13 anos após o início do nível 1. O critério principal é o **conteúdo** do programa; idade e duração são critérios auxiliares [I, a confirmar]. Os seis mapeamentos são coerentes com essas faixas (tabela acima).

## 2. ISCED 2011: dimensões complementares

Legenda oficial na planilha da China [N10, linhas 22–34] e FAQ [N03, p. 4]:

| Dimensão | Níveis | Valores |
|---|---|---|
| Tipo (nível 0) | 0 | ECED = Early childhood educational development; Pre-primary |
| Orientação | 2–5 | G = General; V = Vocational |
| Orientação | 6–8 | academic / professional; U = unspecified orientation |
| Conclusão (*completion*) | 2–8 | F = Full completion of level; P = Partial completion (só ISCED 2 e 3); N = No completion |
| Acesso | 2–4 | Y = dá acesso direto a nível ISCED superior; N = não dá |
| Posição na estrutura de graus | 6–7 | First degree; Long first degree; Second or further degree (after Bachelor or equivalent); Second or further degree (after Master or equivalent) |

O ISCED usa "parallel three-digit coding schemes for education programmes (ISCED-P) and educational attainment (ISCED-A), with nine distinct levels identified in both schemes" [N03, p. 5].

## 3. ISCED-P (programas): códigos de 3 dígitos

Estrutura: 1º dígito = nível; 2º = categoria (orientação; no nível 0, tipo); 3º = subcategoria (conclusão e acesso; nos níveis 6–7, posição na estrutura de graus). Coluna "visto em" indica o mapeamento onde o código aparece.

| Código | Rótulo (en) | Visto em |
|---|---|---|
| 010 | Early childhood educational development | BR, DE, UK |
| 020 | Pre-primary education | BR, US, PT, DE, UK, CN |
| 100 | Primary education | todos |
| 241 / 251 | Lower secondary, general / vocational — insufficient for level completion or partial level completion, without direct access to upper secondary | 241: DE |
| 242 / 252 | … — sufficient for partial level completion, without direct access to upper secondary | [conferir] |
| 243 / 253 | … — sufficient for level completion, without direct access to upper secondary | [conferir] |
| 244 / 254 | … — sufficient for level completion, with direct access to upper secondary | 244: todos; 254: BR, PT, DE, UK |
| 341 / 351 | Upper secondary, general / vocational — insufficient for level completion or partial level completion, without direct access to tertiary | 351: PT, DE |
| 342 / 352 | … — sufficient for partial level completion, without direct access to tertiary | 342: UK |
| 343 / 353 | … — sufficient for level completion, without direct access to tertiary | 353: DE |
| 344 / 354 | … — sufficient for level completion, with direct access to tertiary | todos |
| 441 / 451 | Post-secondary non-tertiary — insufficient for level completion | 451: BR [rótulo conferir: no BR a linha é curso subsequente de 1 ano] |
| 443 / 453 | … — sufficient for level completion, without direct access to tertiary | 453: CN |
| 444 / 454 | … — sufficient for level completion, with direct access to tertiary | 444: CN |
| 541 / 551 | Short-cycle tertiary, general / vocational — insufficient for level completion | [conferir] |
| 544 / 554 | … — sufficient for level completion | 554: BR, CN |
| 6x1 | Bachelor's, insufficient for level completion (x = 4 academic, 5 professional, 6 unspecified) | [conferir] |
| 6x5 | Bachelor's, first degree (3–4 years) | 645, 655: BR; 665: CN |
| 6x6 | Bachelor's, long first degree (more than 4 years) | 666: CN |
| 6x7 | Bachelor's, second or further degree (following a bachelor's or equivalent) | 657: BR; 667: CN |
| 7x1 | Master's, insufficient for level completion | [conferir] |
| 7x6 | Master's, long first degree (at least 5 years) | 766: PT |
| 7x7 | Master's, second or further degree (following a bachelor's or equivalent) | 747, 757: BR; 767: CN, PT |
| 7x8 | Master's, second or further degree (following a master's or equivalent) | 768: PT |
| 8x4 | Doctoral or equivalent (x = 4, 5, 6) | 864: BR, CN [3º dígito: conferir] |
| 999 | Not elsewhere classified | [conferir] |

## 4. ISCED-A (escolaridade obtida): códigos

Para ISCED-A, o 3º dígito dos níveis 2–4 segue a lógica de conclusão/acesso (sem o "insuficiente", que é classificado no nível abaixo); nos níveis 5–8 o 3º dígito é **0** (não detalhado) [N15; confirmado pelos mapeamentos].

| Código | Rótulo | Visto em |
|---|---|---|
| 000 / 010 / 020 / 030 | Nível 0: nunca frequentou / alguma educação infantil / algum primário sem conclusão | 020: BR, US, PT, CN; 000: DE; "10", "20": UK [rótulos: conferir] |
| 100 | Primary education | todos |
| 242, 243, 244 / 252, 253, 254 | Lower secondary, por orientação e conclusão/acesso | 244: todos; 254: BR, PT, DE |
| 342, 343, 344 / 352, 353, 354 | Upper secondary | 342, 343: UK; 344: todos; 354: BR, US, PT, DE, UK, CN; 352: PT; 353: DE |
| 443, 444 / 453, 454 | Post-secondary non-tertiary | 444, 453: CN |
| 540 / 550 / 560 | Short-cycle tertiary (geral / profissional / não especificada) | 550: BR, CN |
| 640 / 650 / 660 | Bachelor's | 640, 650: BR; 660: CN |
| 740 / 750 / 760 | Master's | 740, 750: BR; 760: CN |
| 840 / 850 / 860 | Doctoral | 860: BR, CN; 840: DE [N15] |
| 900 | (usado pelos EUA para programas transversais: Special education, ESL) | US [N06] [significado oficial: conferir] |

## 5. ISCED-F 2013 (campos de educação e formação)

Estrutura: 11 campos amplos (2 dígitos), campos estreitos (3 dígitos) e detalhados (4 dígitos). A Eurostat fala em 29 estreitos e cerca de 80 detalhados [N14]; o registro da ONU contabiliza 11 / 58 / 149 itens, contagem que inclui os códigos genéricos "0", "8" e "9" [N13]. Uso em dados da UE desde 2016 [N14]. Adotado em 2013, publicado em 2014 (ISBN 978-92-9189-150-4) [N13].

Regras de códigos genéricos, citação do Appendix 1 [N12]: "8" é usado para programas interdisciplinares atribuídos ao campo amplo predominante (ex.: 0288); "0" quando não há informação além do nível superior da hierarquia; "9" no nível detalhado para o que não cabe nos campos listados; "9999", "999" ou "99" quando o campo é desconhecido.

| Amplo | Estreito | Detalhado |
|---|---|---|
| 00 Generic programmes and qualifications | 001 Basic programmes and qualifications | 0011 Basic programmes and qualifications |
| | 002 Literacy and numeracy | 0021 Literacy and numeracy |
| | 003 Personal skills and development | 0031 Personal skills and development |
| 01 Education | 011 Education | 0111 Education science; 0112 Training for pre-school teachers; 0113 Teacher training without subject specialization; 0114 Teacher training with subject specialization |
| 02 Arts and humanities | 021 Arts | 0211 Audio-visual techniques and media production; 0212 Fashion, interior and industrial design; 0213 Fine arts; 0214 Handicrafts; 0215 Music and performing arts |
| | 022 Humanities (except languages) | 0221 Religion and theology; 0222 History and archaeology; 0223 Philosophy and ethics |
| | 023 Languages | 0231 Language acquisition; 0232 Literature and linguistics |
| 03 Social sciences, journalism and information | 031 Social and behavioural sciences | 0311 Economics; 0312 Political sciences and civics; 0313 Psychology; 0314 Sociology and cultural studies |
| | 032 Journalism and information | 0321 Journalism and reporting; 0322 Library, information and archival studies |
| 04 Business, administration and law | 041 Business and administration | 0411 Accounting and taxation; 0412 Finance, banking and insurance; 0413 Management and administration; 0414 Marketing and advertising; 0415 Secretarial and office work; 0416 Wholesale and retail sales; 0417 Work skills |
| | 042 Law | 0421 Law |
| 05 Natural sciences, mathematics and statistics | 051 Biological and related sciences | 0511 Biology; 0512 Biochemistry |
| | 052 Environment | 0521 Environmental sciences; 0522 Natural environments and wildlife |
| | 053 Physical sciences | 0531 Chemistry; 0532 Earth sciences; 0533 Physics |
| | 054 Mathematics and statistics | 0541 Mathematics; 0542 Statistics |
| 06 Information and Communication Technologies (ICTs) | 061 Information and Communication Technologies (ICTs) | 0611 Computer use; 0612 Database and network design and administration; 0613 Software and applications development and analysis |
| 07 Engineering, manufacturing and construction | 071 Engineering and engineering trades | 0711 Chemical engineering and processes; 0712 Environmental protection technology; 0713 Electricity and energy; 0714 Electronics and automation; 0715 Mechanics and metal trades; 0716 Motor vehicles, ships and aircraft |
| | 072 Manufacturing and processing | 0721 Food processing; 0722 Materials (glass, paper, plastic and wood); 0723 Textiles (clothes, footwear and leather); 0724 Mining and extraction |
| | 073 Architecture and construction | 0731 Architecture and town planning; 0732 Building and civil engineering |
| 08 Agriculture, forestry, fisheries and veterinary | 081 Agriculture | 0811 Crop and livestock production; 0812 Horticulture |
| | 082 Forestry | 0821 Forestry |
| | 083 Fisheries | 0831 Fisheries |
| | 084 Veterinary | 0841 Veterinary |
| 09 Health and welfare | 091 Health | 0911 Dental studies; 0912 Medicine; 0913 Nursing and midwifery; 0914 Medical diagnostic and treatment technology; 0915 Therapy and rehabilitation; 0916 Pharmacy; 0917 Traditional and complementary medicine and therapy |
| | 092 Welfare | 0921 Care of the elderly and of disabled adults; 0922 Child care and youth services; 0923 Social work and counselling |
| 10 Services | 101 Personal services | 1011 Domestic services; 1012 Hair and beauty services; 1013 Hotel, restaurants and catering; 1014 Sports; 1015 Travel, tourism and leisure |
| | 102 Hygiene and occupational health services | 1021 Community sanitation; 1022 Occupational health and safety |
| | 103 Security services | 1031 Military and defence; 1032 Protection of persons and property |
| | 104 Transport services | 1041 Transport services |

Contagem desta tabela: 11 amplos, 29 estreitos, 80 detalhados, coerente com a Eurostat [N14].

Relevância para a VUOO [I]: o ISCED-F classifica **programas e qualificações** a partir do secundário, não componentes curriculares. Um programa de ensino geral (EF, EM regular) cai em 00 / 0011. Não serve como vocabulário de C.SUB (Matemática ≠ 0541, que é campo de formação superior/profissional). Útil só para itinerários técnicos/profissionais e formação docente.

## 6. Vocabulários de base (formatos e códigos)

| Tema | Padrão | Forma canônica proposta no Core | Exemplos |
|---|---|---|---|
| Instante | RFC 3339 (perfil da ISO 8601) [N31] | `YYYY-MM-DDThh:mm:ss[.fff]Z` ou com offset; armazenar em UTC | `2026-11-05T13:20:00-03:00` |
| Instante com fuso nomeado | RFC 9557 (atualiza RFC 3339) [N31b] | sufixo `[Area/City]` só quando o fuso civil importa (calendário escolar) | `2026-11-05T08:00:00-03:00[America/Sao_Paulo]` |
| Data civil | ISO 8601 / RFC 3339 `full-date` | `YYYY-MM-DD` sem hora (nascimento, início de ano letivo) | `2026-02-02` |
| Duração / intervalo | ISO 8601 | `PnYnMnDTnHnMnS`; intervalo `início/fim` | `PT45M`; `2026-02-02/2026-12-18` |
| Idioma | BCP 47 = RFC 5646 + RFC 4647 [N32]; subtags de ISO 639 [N30] | etiqueta BCP 47 completa, não código ISO 639 solto | `pt-BR`, `en-GB`, `zh-Hans-CN`, `bzs` (Libras) [I: código de Libras a conferir no registro IANA] |
| País | ISO 3166-1 alfa-2 [N33] | maiúsculas | `BR`, `US`, `PT`, `DE`, `GB`, `CN` |
| Subdivisão | ISO 3166-2 [N33] | `PAÍS-SUB` | `BR-SP`, `US-CA`, `GB-ENG`, `GB-SCT` [I: conferir lista vigente] |
| Município, escola, aluno | fora da ISO | C.IDN com `scheme` do adaptador | `scheme = ibge-municipio`, `inep-escola` |
| Identificador interno | UUID, RFC 9562 [N24] | UUIDv7 | — |
| Identificador público de conceito | URI HTTP persistente [N29] | `https://<domínio>/<tipo>/<id>` estável, sem extensão de arquivo | — |
| Nível educacional | ISCED 2011 (ISCED-P, ISCED-A) | código + `scheme = isced-2011-p` / `isced-2011-a` | `244` |
| Campo de formação | ISCED-F 2013 | código 2–4 dígitos + `scheme = isced-f-2013` | `0114` |
