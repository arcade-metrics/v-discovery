# Terminologia: currículo, avaliação e inclusão (Brasil)

> Frente currículo, avaliação e inclusão. Conceitos, códigos e vocabulários controlados com a fonte de cada um. A terminologia de organização (etapas, modalidades, situação de matrícula, identificadores) é da outra frente, em `terminologia.md`. Evidências `E-nn` em [evidencias-curriculo-avaliacao-inclusao.md](evidencias-curriculo-avaliacao-inclusao.md). Acesso: 2026-11-05. **[I]** = inferência própria.

## 1. Gramática dos códigos da BNCC

Fonte: decodificador do bncc-dados, portado em [bncc-pacotes/02-api-e-modelo.md](../fora-da-fase-1/brasil/bncc-pacotes/02-api-e-modelo.md); exemplos conferidos nas transcrições [bncc/](bncc/README.md) e [bncc-computacao/](bncc-computacao/README.md).

| Padrão | Exemplo | Partes | Observação |
|---|---|---|---|
| `EI` + grupo etário `01`–`03` + campo + seq. | `EI02TS01` | grupo 02, campo TS | campos: `EO` O eu, o outro e o nós; `CG` Corpo, gestos e movimentos; `TS` Traços, sons, cores e formas; `EF` Escuta, fala, pensamento e imaginação; `ET` Espaços, tempos, quantidades, relações e transformações |
| `EI` + grupo + `CO` + seq. | `EI03CO01` | Computação | só grupo 03 na transcrição |
| `EF` + ano `01`–`09` ou bloco + componente + seq. | `EF67LP08` | anos 6 e 7, LP | blocos: `12`, `15`, `35`, `67`, `69`, `89`, válidos só para certos componentes (Arte `15`,`69`; EF `12`,`35`,`67`,`89`; LP todos; CO `15`,`69`) |
| `EM13` + área + competência (1 díg.) + seq. (2 díg.) | `EM13LGG103` | área LGG, competência 1, item 03 | áreas: `LGG`, `MAT`, `CNT`, `CHS`. Depois de `EM13LGG105` vem `EM13LGG201` |
| `EM13LP` + seq. | `EM13LP02` | LP no EM | sem competência no código |
| `EM13CO` + seq. | `EM13CO26` | Computação no EM | sem competência no código |

Componentes do EF no código: `LP` Língua Portuguesa, `AR` Arte, `EF` Educação Física, `LI` Língua Inglesa, `MA` Matemática, `CI` Ciências, `GE` Geografia, `HI` História, `ER` Ensino Religioso, `CO` Computação (complemento 2022).

Grupos etários da EI: `EI01` Bebês (zero a 1 ano e 6 meses), `EI02` Crianças bem pequenas, `EI03` Crianças pequenas ([bncc/10-educacao-infantil.md](bncc/10-educacao-infantil.md)).

Regras: decodificar ≠ existir; a sequência não é ordem pedagógica; dois códigos do EF (EF05LP25, EF04LP27) aparecem duas vezes com textos diferentes no PDF de 2017 ([bncc/98-decisoes.md](bncc/98-decisoes.md)).

## 2. Códigos do Currículo Paulista (EI/EF, 2019)

Fonte: PDF do Currículo Paulista (E-15). Contagem automática, não auditada [I].

| Forma | Exemplo | Significado | Base |
|---|---|---|---|
| igual à BNCC | `EF01LP05` | "Ensino Fundamental, 1º Ano, Língua Portuguesa, habilidade 5", "mantendo-se a estrutura proposta pela BNCC" | CP, LP, p. 111 |
| bloco reanuado | `EF01AR01` (de `EF15AR01`); `EF03EF01` (de `EF35EF01`) | "a dezena alterada indica que a habilidade se refere ao 1º ano" | CP, Arte e Educação Física |
| sufixo de letra | `EF01LP10A`, `EF01LP10B`, `EF01LP25C` | partes de uma habilidade BNCC [I] | 451 ocorrências distintas |
| asterisco | `EF01GE12*`, `EF01HI09*`, `EF01EF13*` | habilidade criada no CP [I; o documento declara que habilidades foram criadas em EF e HI] | 132 ocorrências distintas |

Total observado: 1.945 códigos distintos no PDF EI/EF (1.362 no formato BNCC puro).

## 3. Saeb: matrizes de referência

| Termo | Definição operacional | Fonte |
|---|---|---|
| Matriz de referência 2001 | LP: **tópicos** (I. Procedimentos de leitura; II. Implicações do suporte, do gênero e/ou do enunciador; III. Relação entre textos; IV. Coerência e coesão; V. Recursos expressivos e efeitos de sentido; VI. Variação linguística) com **descritores** `Dn`; MT: **temas** com descritores `Dn` | E-22 |
| Descritor | item da matriz 2001, numerado por etapa e área (`D1`…`D21` em LP 9º; até `D37` em MT 9º); número **não** é único entre etapas | E-22 |
| Matriz alinhada à BNCC | eixo do conhecimento × eixo cognitivo, habilidades numeradas por célula | E-21 |
| Eixo cognitivo | `Reconhecer`, `Analisar`, `Avaliar`, `Produzir` (Linguagens 5º e 9º) | E-21 |
| Eixo do conhecimento (LP 2º ano) | Apropriação do Sistema de Escrita Alfabética; Leitura; Produção textual | E-21 |
| Eixo do conhecimento (Linguagens 5º/9º) | Leitura; Análise linguística/Semiótica; Produção de texto (rótulos observados) | E-21 |
| População-alvo / de referência | "conjunto de escolas, redes e sistemas que se pretende avaliar" / "que efetivamente será avaliado" | E-12, art. 5 |
| Dimensões de qualidade | atendimento escolar; ensino e aprendizagem; investimento; profissionais da educação; gestão; equidade; cidadania, direitos humanos e valores | E-12, art. 3 |

## 4. Saeb: escalas e níveis de proficiência

### 4.1 LP e MT, matrizes 2001 (Inep, *Escalas de proficiência do Saeb*, 2020; E-19)

Níveis de 25 pontos; limite inferior incluído ("maior ou igual a… e menor que…"). Os níveis descrevem habilidades cumulativas.

| Etapa e área | Nível 0 | Nível 1 | Passo | Último nível |
|---|---|---|---|---|
| 5º EF LP | < 125 | 125 a < 150 | 25 | Nível 9: ≥ 325 |
| 5º EF MT | < 125 | 125 a < 150 | 25 | Nível 10: ≥ 350 |
| 9º EF LP | < 200 | 200 a < 225 | 25 | Nível 8: ≥ 375 |
| 9º EF MT | < 200 | 200 a < 225 | 25 | Nível 9: ≥ 400 |
| 3ª EM LP | < 225 | 225 a < 250 | 25 | Nível 8: ≥ 400 |
| 3ª EM MT | < 225 | 225 a < 250 | 25 | Nível 10: ≥ 450 |

Nota do documento: no 5º ano, "O Saeb não utilizou itens que avaliam as habilidades deste nível" (nível 0); na 3ª série, "O Saeb não utilizou itens da 3ª série que avaliam as habilidades do Nível 0".

### 4.2 Matrizes alinhadas à BNCC (Inep, *Escalas de proficiência do Saeb: 2º, 5º e 9º ano*, 2025; E-20)

| Etapa e área | Nível "Abaixo de 1" | Nível 1 | Passo | Último nível observado no texto extraído |
|---|---|---|---|---|
| 2º EF LP | < 650 | 650 a < 675 | 25 | Nível 8: ≥ 825 |
| 2º EF MT | < 650 | 650 a < 675 | 25 | Nível 9: ≥ 850 |
| 5º EF CN | < 175 | 175 a < 200 | 25 | Nível 8: 350 a < 375 (topo não confirmado) |
| 5º EF CH | < 200 | 200 a < 225 | 25 | Nível 7 (intervalo não extraído) |
| 9º EF CN | < 200 | 200 a < 225 | 25 | Nível 8: 375 a < 400 (topo não confirmado) |
| 9º EF CH | < 200 | 200 a < 225 | 25 | Nível 9: ≥ 400 |

Rótulo do nível mais baixo muda entre famílias: "Nível 0" (2001) × "Nível Abaixo de 1" (BNCC). Para LP e MT de 5º e 9º alinhadas à BNCC, escala publicada: **not_found**.

### 4.3 Pontos de corte derivados

| Corte | Valor | Escala | Fonte |
|---|---|---|---|
| Padrão nacional de alfabetização (CNCA) | 743 | Saeb 2º ano | E-26 (agência oficial; ato do Inep não aberto) |

## 5. SARESP: níveis (LP, edição 2014; E-23)

| Nível | 3º EF | 5º EF | 7º EF | 9º EF | 3ª EM | Classificação |
|---|---|---|---|---|---|---|
| Abaixo do Básico | < 125 | < 150 | < 175 | < 200 | < 250 | Insuficiente |
| Básico | 125–<175 | 150–<200 | 175–<225 | 200–<275 | 250–<300 | Suficiente |
| Adequado | 175–<225 | 200–<250 | 225–<275 | 275–<325 | 300–<375 | Suficiente |
| Avançado | ≥ 225 | ≥ 250 | ≥ 275 | ≥ 325 | ≥ 375 | Avançado |

Escala: a do Saeb ("na mesma escala de desempenho da Prova Brasil/Saeb"). Cortes de MT e da edição vigente: não verificados.

## 6. Ensino Médio 2024–2025

| Vocabulário | Valores | Fonte |
|---|---|---|
| Partes do currículo | Formação Geral Básica (FGB); Itinerário Formativo de Aprofundamento (IFA); Itinerário de Formação Técnica e Profissional | E-08, E-07 |
| Áreas e componentes obrigatórios da FGB | Linguagens e suas tecnologias (LP e literaturas, língua inglesa, artes, educação física); Matemática e suas tecnologias (matemática); Ciências da natureza e suas tecnologias (biologia, física, química); Ciências humanas e sociais aplicadas (filosofia, geografia, história, sociologia) | E-07, art. 17 |
| Eixos curriculares estruturantes dos IFAs | Método, Conhecimento e Ciência; Mediação e Intervenção Sociocultural; Inovação e Intervenção Tecnológica; Mundo do Trabalho e Transformação Social | E-09, art. 11 |
| Competências comuns dos IFAs | 10 itens numerados 1–10 no Anexo, **sem código** | E-09, Anexo |
| Objetivos de aprendizagem de área (IFA) | competência numerada + lista "Demonstrando a capacidade de:" sem código | E-09, Anexo |
| Componentes de rede SP | "Redação e Leitura" (parte de LP); "Educação Financeira" (parte de MT) | E-11, art. 4 §1 |

## 7. Inclusão

### 7.1 Categoria administrativa de deficiência, TEA e AH/SD (CMDEB, `ESTUDANTE_DEFICIENCIA`, [1..n])

Fonte: [cmdeb/10-estudante.md](cmdeb/10-estudante.md) (Portaria MEC 832/2025, Anexo). Dono: frente de organização; reproduzido aqui só por ser vocabulário de D7.

| Código | Rótulo |
|---|---|
| 0 | Não informado |
| 1 | Baixa visão |
| 2 | Visão monocular |
| 3 | Cegueira |
| 4 | Deficiência auditiva |
| 5 | Surdez |
| 6 | Surdocegueira |
| 7 | Deficiência física |
| 8 | Deficiência intelectual |
| 9 | Transtorno do espectro autista |
| 10 | Altas habilidades/superdotação |
| 11 | Não possui |

### 7.2 Conceitos normativos

| Termo | Definição (fonte) |
|---|---|
| Barreira | entrave que limita ou impede a participação (LBI art. 3, IV); tipos: urbanísticas, arquitetônicas, nos transportes, nas comunicações e na informação, atitudinais, tecnológicas (acs.br.lbi) |
| Adaptação razoável | ajustes "que não acarretem ônus desproporcional e indevido, quando requeridos em cada caso" (LBI art. 3, VI, via acs.br.lbi) |
| Tecnologia assistiva | produtos, recursos, metodologias, estratégias, práticas e serviços que promovam funcionalidade e participação (LBI art. 3, III, via acs.br.lbi) |
| Estudo de caso | etapa inicial para identificar estudante público da educação especial, em 4 etapas: demandas individuais e barreiras; análise das barreiras e do contexto escolar; potencialidades e demandas de apoio; estratégias e recursos de acessibilidade (Dec. 12.686 art. 11, via acs.asmt.pei-and-aee-plans) |
| PAEE | "documento que faz o registro do estudo de caso" (Port. MEC 421 art. 10) |
| PEI | "documento que contempla o plano de acessibilização curricular" (Port. MEC 421 art. 11); em SP, "estabelece a acessibilização curricular, adaptações e estratégias para o acesso ao currículo comum" (Res. SEDUC 129 art. 2, IV) |
| API (SP) | Avaliação Pedagógica Inicial: "documento pedagógico elaborado por professor especializado, na forma de estudo de caso" (Dec. SP 67.635 art. 8); "equivalente ao Estudo de Caso" (Res. SEDUC 129 art. 2, II) |
| Profissional de apoio escolar | atua em locomoção, higiene e alimentação, interação social e comunicação, uso de TA (Port. MEC 421 art. 12) |

### 7.3 Tipos de apoio (vocabulários concretos)

| Vocabulário | Valores | Fonte |
|---|---|---|
| Áreas de apoio do profissional (federal) | locomoção; higiene; alimentação; interação; comunicação; uso de tecnologia assistiva | Port. MEC 421 art. 14 |
| Serviços avaliados no PAEE (federal) | profissional de apoio escolar; tradutor e intérprete de Libras; guia-intérprete; recursos de TA e CAA | Port. MEC 421 art. 10, II–III |
| Funções do profissional de apoio (SP, PAEE) | alimentação; higiene pessoal, íntima e bucal; locomoção; autocuidado; mediação e auxílio nas atividades escolares; suporte à comunicação e interação social; socialização | Res. SEDUC 129, Anexo III |
| Serviços (SP, PAEE) | recursos pedagógicos, de acessibilidade e TA; professor de Libras ou interlocutor de Libras; professor instrutor-mediador ou guia-intérprete; profissional de apoio escolar | Res. SEDUC 129, Anexo III |
| Nível de apoio (SP) | `1` maior parte autônoma, apoio pontual; `2` apoio frequente, ajustes contínuos de rotina e currículo acessível; `3` apoio muito substancial e contínuo | Res. SEDUC 129, Anexo II, II |
| Hipótese de escrita (SP, estudo de caso) | pré-silábico; silábico; silábico-alfabético; alfabético | Res. SEDUC 129, Anexo II, VI |
| Domínio de Libras / Braille (SP) | básico; intermediário; avançado | idem |

Observação [I]: o "Nível de Apoio 1/2/3" paulista tem os mesmos números da gradação de suporte do DSM-5 para TEA, mas o texto o descreve em termos pedagógicos e funcionais e o aplica a todo o público elegível; **não** tratar como equivalente.

## 8. Privacidade (enum mínimo para o Core)

| Vocabulário | Valores | Fonte |
|---|---|---|
| Bases legais (dados pessoais) | consentimento; obrigação legal ou regulatória; execução de políticas públicas; estudos por órgão de pesquisa; execução de contrato; exercício regular de direitos; proteção da vida; tutela da saúde; legítimo interesse; proteção do crédito | LGPD art. 7 (psg.legal.lgpd-children) |
| Bases legais (dados sensíveis) | consentimento específico e destacado; sem consentimento, quando indispensável para: obrigação legal, políticas públicas, pesquisa, exercício de direitos, proteção da vida, tutela da saúde, prevenção à fraude | LGPD art. 11 |
| Faixa etária legal | criança (< 12 anos); adolescente (12 a < 18) | ECA art. 2 |
| Hipóteses de conservação após término | obrigação legal ou regulatória; pesquisa (anonimização sempre que possível); transferência a terceiro; uso exclusivo do controlador anonimizado | LGPD art. 16 (E-34) |
