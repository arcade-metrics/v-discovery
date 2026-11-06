# Modelo de dados: currículo, avaliação e inclusão (adaptador Brasil)

> Frente currículo, avaliação e inclusão (D2, D4, D5, D7 e parte legal de D8). Organização, identificadores e Censo são da outra frente (`modelo-de-dados.md`). Este documento descreve **o que as fontes brasileiras exigem ou sustentam**, entidade por entidade, e propõe a forma de representá-lo; não é o modelo final do Core (briefing §7: "não propor a implementação definitiva antes de concluir o inventário"). Fichas em [fichas/](fichas/); códigos em [terminologia](terminologia-curriculo-avaliacao-inclusao.md); evidências `E-nn` em [evidencias](evidencias-curriculo-avaliacao-inclusao.md). Data: 2026-11-05. **[I]** = proposta ou inferência própria.

## 0. Princípios tirados das fontes

| # | Princípio | Fato que o impõe |
|---|---|---|
| P1 | **Modelar a fonte como ela é**: estrutura por etapa e por documento, sem nível obrigatório | BNCC: EI, EF e EM organizados de formas diferentes ([bncc-dados/02](../fora-da-fase-1/brasil/bncc-dados/02-modelo-de-dados.md)); Computação com objeto em 2 níveis; IFAs sem código |
| P2 | **Código não é identidade** | a forma impressa pode diferir do código (`EF05CO011`, impresso com três dígitos na BNCC Computação; vuoo-base `ferramentas/METODO.md`); Currículo Paulista reusa códigos BNCC e cria `EF01AR01` que não existe na BNCC |
| P3 | **Três relógios** para currículo: vigência do ato, edição do texto, versão do dado; e um quarto, a **coorte** do estudante | DCNEM 2024 arts. 39, 42 e 43: currículos de 2018 e 2024 coexistem por coorte |
| P4 | **Resultado ≠ classificação**: o valor na escala é um dado; níveis são esquemas de corte versionados e múltiplos | Saeb (níveis 0..10), SARESP (4 níveis + 3 classes), CNCA (743, binário) sobre a mesma escala |
| P5 | **Necessidade de apoio ≠ diagnóstico ≠ elegibilidade administrativa** | Port. MEC 421 art. 7 §4; Dec. 12.686 art. 11 §7; Lei 14.254 (apoio fora da educação especial); CMDEB exige categoria para coleta oficial |
| P6 | **Classificação de sensibilidade por campo**, não por entidade | o Estudo de Caso paulista mistura dados pedagógicos, de saúde e de terceiros no mesmo formulário |

## 1. Currículo (D4, D2)

### 1.1 Entidades

| Entidade [I] | Core | O que representa no Brasil | Exemplos |
|---|---|---|---|
| `DocumentoCurricular` | C.CFW | documento normativo ou referencial, com esfera | BNCC; BNCC Computação; Parâmetros dos IFAs (Res. CNE/CEB 4/2025, Anexo); Currículo Paulista EI/EF; Currículo Paulista EM |
| `AtoNormativo` | C.PRV (+ C.CFW) | ato que institui, altera ou revoga | Res. CNE/CP 2/2017; Res. CNE/CP 4/2018; Res. CNE/CEB 1/2022; Deliberação CEE-SP 186/2020 (parcialmente revogada pela 236/2025) |
| `EdicaoDoTexto` | C.CFW.version | texto específico de um documento | BNCC versão final (SHA `ad623d7b…`); BNCC Computação 2022 (SHA `60aab0b1…`); CP 26/07/2019 (SHA `53e60892…`) |
| `NoOrganizador` | C.CMP (tipo organizador) | nível estrutural tipado | etapa, área, componente, campo de experiências, grupo etário, unidade temática, prática de linguagem, campo de atuação, eixo, "linguagens" (CP Arte), competência específica, eixo estruturante (IFA) |
| `ItemCurricular` | C.CMP | unidade de aprendizagem | habilidade, objetivo de aprendizagem e desenvolvimento, competência geral, competência comum de IFA, "capacidade" de IFA, objeto de conhecimento |
| `AssociacaoCurricular` | C.CAS | relação tipada entre itens | `pertenceA`, `trataDeObjeto`, `derivaDe` (com subtipo), `criadoLocalmente`, `equivalente`, `alinhadoA`, `coberturaPorComponente` |
| `AdocaoCurricular` | (candidata) | rede/escola adota uma edição para um programa e coortes | rede estadual SP adota CP EM para ingressantes 2026 |

### 1.2 Atributos essenciais

**DocumentoCurricular**

| Campo | Tipo | Card. | Regra / origem |
|---|---|---|---|
| `id` | id cunhado imutável | 1 | ex. `bncc-2018`, `bncc-computacao-2022` (ids do vuoo-base v1.1), `sp-curriculo-paulista-efi` |
| `titulo` | texto | 1 | como publicado |
| `esfera` | enum {nacional, estadual, municipal, rede, escola} | 1 | DCN: base comum + parte diversificada |
| `jurisdicao` | ref C.ORG | 1 | União; Estado de SP |
| `tipo` | enum {base_normativa, complemento, parametros, referencial_estadual, curriculo_rede, ppp} | 1 | |
| `derivadoDe` | ref DocumentoCurricular | 0..n | CP → BNCC; BNCC Computação → BNCC (complemento) |
| `etapas` | lista C.PRG | 1..n | |
| `atos` | lista AtoNormativo com papel {institui, homologa, altera, revoga_parcial, revoga} | 1..n | |

**AtoNormativo**

| Campo | Tipo | Card. | Exemplo |
|---|---|---|---|
| `tipo` | enum {lei, decreto, resolucao_cne, parecer_cne, portaria, deliberacao_cee, resolucao_secretaria} | 1 | |
| `numero`, `data`, `publicacao` (veículo, data, seção, página) | texto/data | 1 | Res. CNE/CEB 2/2024; DOU 14/11/2024, S1, p. 48 |
| `vigenciaDesde`, `vigenciaAte` | data | 1 / 0..1 | DCNEM 2024: vigência 02/12/2024 |
| `regimeDeTransicao` | texto + regra | 0..1 | DCNEM art. 42: Res. 3/2018 mantida para matriculados antes |
| `url`, `hash` | URL, SHA-256 | 1 / 0..1 | |

**ItemCurricular**

| Campo | Tipo | Card. | Regra |
|---|---|---|---|
| `id` | id cunhado | 1 | **nunca** o código (P2) |
| `documento`, `edicao` | ref | 1 | |
| `notation` | texto | 0..1 | código oficial; obrigatório quando a fonte imprime; ausente nos IFAs e em enunciados gerais da Computação |
| `notationImpressa` | texto | 0..1 | forma como impressa quando difere (ex. `EF09GE01)` sem parêntese) |
| `texto` | texto | 1 | como impresso na edição |
| `tipo` | enum {habilidade, objetivo_aprendizagem_desenvolvimento, competencia_geral, competencia_especifica, competencia_comum_ifa, capacidade_ifa, objeto_conhecimento} | 1 | |
| `anos` | lista de ano/série ou faixa etária | 0..n | `EF67LP08` → [6, 7]; CP `EF01AR01` → [1] |
| `abrangencia` | enum {especifica_do_ano, articulavel_entre_anos} | 0..1 | CP, LP |
| `localizador` | {pagina_impressa, pagina_pdf, quadro, linha} | 1 | rastreabilidade (no vuoo-base v1.1, cada item traz `pagina_pdf`) |
| `vigencia` | {status: vigente/alterado/revogado, desde, ate} | 1 | desde/até = versões do dataset (bncc-dados) |
| `ordemNoDocumento` | inteiro | 0..1 | P1: ordem impressa ≠ ordem do código (CP LP anos iniciais) |

**AssociacaoCurricular**

| `tipo` | Origem | Cardinalidade | Equivalência |
|---|---|---|---|
| `pertenceA` (item → nó organizador) | quadro do documento | n:1 (ou n:n quando a célula agrupa) | — |
| `trataDeObjeto` (habilidade → objeto) | linha do quadro | n:n | — |
| `desenvolveCompetencia` | código (EM áreas) ou planilha (EM LP) | n:1 / n:n | não existe no EF (bncc-dados) |
| `derivaDe` {reanuacao, desdobramento, adaptacao_textual, sem_alteracao} | CP → BNCC (pelo código, a validar pelo texto) | 1:n BNCC → CP | `mais_restrita` (reanuação, desdobramento) ou `aproximada` |
| `criadoLocalmente` | CP `*` [I] | — | `inexistente` na BNCC |
| `coberturaPorComponente` (componente ofertado → item) | Res. SEDUC 84/2024 (Redação e Leitura ⊂ LP) | n:n | — |
| `alinhadoA` (item de matriz de avaliação ↔ item curricular) | **não publicado** pelo Inep | n:n | só `aproximada`, com proveniência de curadoria |
| `prerequisito` | **não existe nas fontes** | — | camada de anotação separada (kg.curr.bncc) |

Toda associação carrega `fonte` {normativa, derivada_por_regra, curadoria} e `proveniencia` (C.PRV).

**AdocaoCurricular** [I, candidata a entidade do Core, Q-CUR-05]

| Campo | Card. | Exemplo |
|---|---|---|
| `organizacao` (rede, escola) | 1 | Seduc-SP |
| `documento`, `edicao` | 1 | CP EM |
| `programa` (etapa, itinerário) | 1..n | EM, FGB |
| `coortesDeIngresso` ou `vigencia` | 1 | ingressantes ≥ 2026 (DCNEM art. 39 §2) |
| `atoLocal` | 0..1 | Res. SEDUC 84/2024 |

### 1.3 Nacional × estadual × rede: como ligar [I]

```
BNCC (esfera nacional)                         Parâmetros IFA (nacional, sem códigos)
  └─ ItemCurricular EF15AR01 ──derivaDe{reanuacao}──▶ CP EF01AR01, EF02AR01 … (estadual)
  └─ ItemCurricular EF01LP10 ──derivaDe{desdobramento}──▶ CP EF01LP10A, EF01LP10B
                                     CP EF01GE12* ──criadoLocalmente
Rede estadual SP ──AdocaoCurricular──▶ CP (EI/EF; EM para coortes)
Componente de rede "Redação e Leitura" ──coberturaPorComponente──▶ subconjunto de itens CP LP EM
PEI SP (estudante × componente × bimestre) ──visa──▶ itens CP
SARESP / Saeb item ──alinhadoA (curadoria)──▶ itens CP / BNCC
```

Regras de validação propostas:
1. `notation` válida pela gramática do **documento** (BNCC e CP compartilham a forma; `EM13CO` tem regra própria).
2. Item `derivaDe` deve apontar para item de documento listado em `DocumentoCurricular.derivadoDe`.
3. `equivalente` só com texto idêntico na mesma edição comparada (registro da comparação).
4. Um estudante tem, para cada (programa, período), exatamente uma `AdocaoCurricular` aplicável, resolvida por coorte de ingresso (P3).

## 2. Avaliação (D5)

### 2.1 Entidades

| Entidade [I] | Core | Brasil |
|---|---|---|
| `ProgramaDeAvaliacao` | C.ASM (agrupador) | Saeb; SARESP; avaliação estadual de alfabetização (CNCA); avaliação da rede (bimestral) |
| `EdicaoDeAvaliacao` | C.ASM | Saeb 2025 (Portaria Inep 435/2025); SARESP 2025 |
| `Instrumento` | C.ASM | teste cognitivo (área × etapa), questionário (aluno, professor, diretor, secretário, família) |
| `MatrizDeReferencia` | C.CFW (tipo matriz) | Saeb 2001 (tópicos/temas + descritores), Saeb BNCC (eixo conhecimento × eixo cognitivo), matriz SARESP (2009) |
| `ItemDeMatriz` | C.CMP (tipo descritor/habilidade de matriz) | `D1` LP 5º (2001); "Localizar informação explícita" (Linguagens 5º, eixo Leitura × Reconhecer) |
| `Item` | C.ITM | itens não divulgados (Portaria 435 art. 25) |
| `Escala` | C.VOC + métrica | escala Saeb LP 2001 (5º, 9º, 3ª EM); escala Saeb 2º ano (BNCC); escalas CN e CH (BNCC) |
| `EsquemaDeNiveis` | C.VOC | níveis Saeb por etapa/área; níveis SARESP por ano/série; corte CNCA |
| `Nivel` | C.VOC.Code | Nível 3 do 5º LP: [175, 200), descrição cumulativa |
| `Resultado` | C.RES | proficiência individual ou agregada |
| `Acomodacao` | C.SUP aplicado | tempo adicional, sala extra, prova ampliada, braille, ledor (Portaria 435 art. 17) |
| `SistemaDeAvaliacaoDaRede` | C.VOC | CMDEB `SISTEMA_AVALIACAO_DESEMPENHO` (nota 0–10; menções; conceitos; aprovação; percentual; híbrido; competências; TRI; diagnóstico) |

### 2.2 Atributos essenciais

**EdicaoDeAvaliacao**: `programa`, `ano`, `atoRegulador` (AtoNormativo), `periodoDeAplicacao` (20 a 31/10/2025), `populacaoAlvo`, `criteriosDeExclusao` (multisseriadas, correção de fluxo, EJA, classes especiais, indígenas sem LP L1; art. 7), `regrasDeDivulgacao` (≥ 10 presentes e ≥ 80% participação na escola; art. 22).

**Instrumento**: `tipo` {teste, questionario}, `area`, `etapa` (2º, 5º, 9º EF; 3ª/4ª EM), `matriz` (ref, **1..n**: em 2025 o 5º/9º usa 2001 **e** BNCC), `formato` {censitario, amostral}, `redes` {publica, privada}.

**MatrizDeReferencia**: `familia` {saeb_2001, saeb_bncc, saresp_2009, …}, `etapa`, `area`, `estrutura` {topico_descritor, eixo_conhecimento×eixo_cognitivo, lista}, `publicacao` (Inep 2022 para ambas as famílias).

**ItemDeMatriz**: `id` cunhado; `notation` local (`D1`) **qualificada por matriz** (o `D1` do 5º LP não é o `D1` do 9º MT); `eixoConhecimento`, `eixoCognitivo` ou `topico`; `texto`.

**Escala**: `id`, `metrica` {saeb_0_500, saeb_2ano, …}, `areas`, `etapas` comparáveis na mesma métrica (5º, 9º, 3ª EM em LP 2001), `fonte`.

**EsquemaDeNiveis**: `escala`, `etapa`, `area`, `edicaoOuVigencia`, `tipo` {descritivo_cumulativo (Saeb), normativo_4 (SARESP), binario_corte (CNCA)}, `agrupamentos` (SARESP: Insuficiente/Suficiente/Avançado).

**Nivel**: `rotulo` ("Nível 0", "Nível Abaixo de 1", "Adequado"), `limiteInferior` (incluído), `limiteSuperior` (excluído), `descricao`, `semItens` (bool: "O Saeb não utilizou itens…").

**Resultado**

| Campo | Card. | Nota |
|---|---|---|
| `sujeito` | 1 | estudante (C.LRN) **ou** agregado (turma, escola, rede, município, UF, país) |
| `instrumento`, `edicao` | 1 | |
| `valor` + `escala` | 0..1 | proficiência TRI; ausente em avaliações qualitativas |
| `classificacoes` | 0..n | {esquema, nivel}; derivadas, recalculáveis (P4) |
| `indicadoresDeAgregado` | 0..n | participação (%), nº de presentes, média; usados nas regras de divulgação |
| `acomodacoesAplicadas` | 0..n | ref Acomodacao, com origem (cadastro do Censo / PEI) |
| `proveniencia` | 1 | sistema-fonte, data, microdado/boletim |

Observação: o Saeb não devolve resultado individual (agregado com critérios mínimos); avaliações estaduais e da rede sim. A VUOO tende a consumir resultados agregados oficiais e produzir resultados individuais próprios (formativos) [I]; ambos cabem em `Resultado` com `sujeito` distinto.

### 2.3 Regras e consequências

- Acomodação no Saeb depende do **cadastro na Matrícula Inicial do Censo** (Portaria 435 arts. 15–17): a necessidade registrada no PEI não chega à avaliação federal se não estiver no Censo. Integração PEI → Censo é da outra frente; aqui fica o vínculo `Acomodacao.origem`.
- Alinhamento matriz ↔ currículo **não é publicado** (0 códigos BNCC na matriz de Linguagens): `alinhadoA` só por curadoria.
- Transição: EM avaliado por matriz 2001 até a adaptação do Saeb (prazo 2027, Res. CNE/CEB 4/2025 art. 28 §1). Esquemas de nível precisam de vigência.

## 3. Inclusão (D7, com D3)

### 3.1 Como representar necessidade de apoio sem reduzir a diagnóstico

As normas brasileiras já organizam o tema em torno de **barreira → apoio**, e a categoria clínica fica fora do caminho crítico (P5). Proposta [I]:

```
Estudante (C.LRN)
 ├─ PerfilDeApoio  (C.SUP; pedagógico; existe sem elegibilidade e sem diagnóstico)
 │    ├─ Barreira[]        {contexto, tipo (LBI art. 3 IV), descricao, fonte (estudante|família|professor), data}
 │    ├─ Potencialidade[]  {descricao, area}
 │    ├─ Apoio[]           {tipo (vocab. Port. 421 art. 14 / SP Anexo III), intensidade (ex. SP nível 1–3),
 │    │                     ambiente (sala comum|AEE|colaborativo|avaliação|plataforma), responsavel, vigência}
 │    └─ Acomodacao[]      {alvo: atividade|avaliação|material, descrição, ex.: tempo adicional, ledor, ampliação}
 ├─ ElegibilidadeEducacaoEspecial  (administrativa; opcional; sensível)
 │    {categorias (CMDEB ESTUDANTE_DEFICIENCIA), base (estudo de caso | documento), situação (confirmada|em investigação), vigência}
 ├─ DocumentoDeSuporte[]  (opcional; sensível)  {tipo: laudo|relatório|parecer pedagógico|CIPTEA, emissor, data, validade}
 └─ PlanoIndividual (C.PLN)  … ver 3.2
```

Regras:
1. Nenhum `Apoio`, `Acomodacao` ou `PlanoIndividual` exige `ElegibilidadeEducacaoEspecial` ou `DocumentoDeSuporte` para existir (Port. MEC 421 art. 7 §4; Dec. 12.686 art. 11 §7).
2. Estudante com dislexia ou TDAH (Lei 14.254) tem `PerfilDeApoio` sem elegibilidade: o acompanhamento específico é obrigação da escola, mas não há plano federal obrigatório.
3. `ElegibilidadeEducacaoEspecial` existe para coletas oficiais (Censo/CMDEB) e para fluxos administrativos locais (SP: sala de recursos, professor por especialidade); é isolada por permissão e não alimenta personalização [I].
4. A plataforma **não infere** categoria diagnóstica a partir de interação (LGPD art. 11 §1 trata inferência como sensível; psg.legal.lgpd-children).

### 3.2 Plano individual (PAEE, PEI)

**Federal (Port. MEC 421/2026)**: conteúdo mínimo, documento único permitido, revisão anual. **SP (Res. SEDUC 129/2025)**: formulários oficiais, PEI por componente e bimestre, atualização bimestral, prazo de 30 dias letivos. Modelo que acomoda os dois [I]:

| Entidade | Campos | Card. | Fonte |
|---|---|---|---|
| `EstudoDeCaso` | estudante; data; participantes[] (papel: prof. AEE, regente, família, estudante, gestão, serviços); barreiras[]; contexto escolar; potencialidades[]; demandas de apoio[]; estratégias e recursos[]; nível de apoio (SP) 0..1; observações pedagógicas (SP: hipótese de escrita, Libras/Braille, comunicação, motor); relatório consolidado | 1 por ciclo | Dec. 12.686 art. 11 §1; SP Anexo II |
| `PlanoIndividual` | estudante; estudoDeCaso; versão; vigência; status; `secoes` {paee, pei} (documento único permitido) | 1 vigente por estudante | Port. 421 art. 7 §2 |
| `SecaoPAEE` | materiais e recursos para barreiras; necessidade e capacidade de TA e CAA; necessidade de profissional de apoio, intérprete de Libras, guia-intérprete (com motivo); demandas de formação e de rede de proteção; habilidades a desenvolver no AEE (SP); planejamento por período (SP: bimestres 1–4); orientações por destinatário (regente, colaborativo, equipe); aquisições (SP: PDDE-Paulista); medidas para superar barreiras (SP) | 1 | Port. 421 art. 10; SP Anexo III |
| `MetaDoPlano` (PEI) | componente curricular (C.SUB/C.OFR); período (C.SES, ex. bimestre); itens curriculares visados[] (C.CMP, CP em SP); estratégias e intervenções; recursos de acessibilidade; **medidas avaliativas** (acomodações); instrumentos de acompanhamento; recursos indicados (vídeos, jogos, atividades → C.ACT); responsável (regente) | 0..n por (componente, período) | Port. 421 art. 11; SP Anexo IV |
| `Acompanhamento` | data; progressos; desafios; próximas intervenções; evidências (C.EVD) | 0..n | Port. 421 art. 11 III; SP Anexo V |
| `DevolutivaFamilia` | data; tipo {acolhimento, retorno_periodico}; conteúdo; ciência/assinatura do responsável | 1..n | Port. 421 art. 11 IV; SP art. 4 e Anexo V |
| `Revisao` | data; motivo {anual, bimestral, mudança}; decisão {manter, ajustar, encerrar} | ≥ 1/ano (federal); bimestral (SP) | Port. 421 art. 7 §3; SP art. 14 §5 |
| `Assinatura` | papel; pessoa; data | n | SP Anexos II–V |
| `AutorizacaoDeContato` | profissional externo; sim/não; justificativa | 0..n | SP Anexo II, V |

Validações propostas: PAEE e Estudo de Caso dentro de 30 dias letivos do início da frequência (adaptador SP); revisão em ≤ 12 meses (federal); toda `MetaDoPlano` aponta ao menos um item curricular **da adoção curricular vigente** do estudante (liga 3.2 a 1.3); `medidas avaliativas` do plano propagam para `Acomodacao` em avaliações da plataforma.

Comparação com IEP (EUA): o modelo brasileiro não exige metas anuais mensuráveis nem relato periódico de progresso (acs.asmt.pei-and-aee-plans); SP aproxima isso com objetivos bimestrais e relatório de progresso aos pais [I].

## 4. Dados e privacidade aplicados a este domínio (D8 legal)

| Categoria de campo | Exemplos | Sensível (LGPD art. 5 II)? | Base típica [I] |
|---|---|---|---|
| Curricular e de desempenho | resultados, metas do PEI, hipótese de escrita | não | política pública (rede pública) ou contrato/legítimo interesse com teste de balanceamento |
| Barreiras, apoios, acomodações | "ledor", "tempo adicional", nível de apoio | **a avaliar**: revelam condição de saúde por associação (art. 11 §1) → tratar como sensível [I] | art. 11 II (obrigação legal / política pública) para a rede; consentimento específico para fornecedor fora desse papel |
| Elegibilidade, laudo, CID, hipótese diagnóstica, acompanhamento terapêutico | CMDEB categoria; SP Anexo II V | **sim** | art. 11 |
| Dados de terceiros | contato do terapeuta | dado pessoal de terceiro | autorização registrada (SP) |

Requisitos L1–L10 (LGPD) e E1–E6 (ECA Digital) em [fichas/lgpd-educacao.md](fichas/lgpd-educacao.md) e [fichas/eca-digital.md](fichas/eca-digital.md). Consequências diretas no modelo: `sensibilidade` por campo; `LegalBasis` por operação (não por entidade); `Consent` com outorgante responsável e verificação; retenção por categoria com motivo de conservação (art. 16); proveniência de toda inferência (art. 20); registro de localização de processamento por operador (art. 33).
