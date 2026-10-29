---
id: psg.legal.comparison
titulo: Comparação LGPD, Estatuto Digital, GDPR, AADC e COPPA
tipo: comparacao
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [brasil2018lgpd, lei8069eca, lei15211ecadigital, anpd2023enunciado1, anpd2024legitimointeresse, eu2016gdpr, ico2020aadc, ftc2025coppa, ftc2025coppafinalrule, ftc2025coppafaq]
relacoes:
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.legal.eca-and-digital-eca }
  - { tipo: relacionado-a, alvo: psg.legal.gdpr-k-and-coppa }
  - { tipo: relacionado-a, alvo: psg.consent.parental-consent }
  - { tipo: relacionado-a, alvo: psg.audit.ripd-dpia }
  - { tipo: complementa, alvo: iop.br.lgpd }
termos: [limiar de idade, base legal, verificação parental, consentimento pela escola, privacidade por padrão, sanção administrativa, acesso provável]
---

# Comparação LGPD, Estatuto Digital, GDPR, AADC e COPPA

## Definição e terminologia

Este documento compara, por critério, os cinco instrumentos tratados na área legal-framework: LGPD (Lei 13.709/2018), Estatuto Digital da Criança e do Adolescente (Lei 15.211/2025), GDPR (Regulamento (UE) 2016/679), UK Age Appropriate Design Code (AADC) e COPPA (16 CFR Part 312, revisada em 2025). O ECA (Lei 8.069/1990) entra como fonte das definições de idade no Brasil. Os critérios seguem o plano do domínio: idade, base legal, verificação parental, papel da escola, desenho, dados sensíveis, decisões automatizadas e sanções. As afirmações por célula remetem aos documentos de origem, onde estão as citações completas.

## Problema que resolve

Equipes que desenham uma plataforma educacional brasileira precisam saber onde a norma nacional é mais exigente que as estrangeiras (e portanto não podem importar um desenho "GDPR-compliant" sem ajuste) e onde é silenciosa (e portanto podem adotar o regime estrangeiro como referência de boa prática) [I].

## Alternativas e comparações

### Tabela por critério

| Critério | LGPD + ECA | Estatuto Digital (Lei 15.211/2025) | GDPR | AADC | COPPA (2025) |
|---|---|---|---|---|---|
| Quem é "criança" | criança até 12 incompletos; adolescente 12 a 18 [F: lei8069eca, art. 2] | adota o ECA [F: lei15211ecadigital, art. 2, §1] | menor de 16, Estados podem baixar até 13 [F: eu2016gdpr, art. 8(1)] | menor de 18, faixas 0-5, 6-9, 10-12, 13-15, 16-17 [F: ico2020aadc, anexo B] | menor de 13 [F: ftc2025coppa, §312.2] |
| Regime reforçado para | crianças (§1) e adolescentes (caput) [F: brasil2018lgpd, art. 14] | crianças e adolescentes; serviços direcionados ou de acesso provável [F: lei15211ecadigital, art. 1] | crianças, só quando a base é consentimento em serviço oferecido diretamente a elas [F: eu2016gdpr, art. 8] | qualquer serviço "likely to be accessed by children" [F: ico2020aadc] | serviços dirigidos a menores de 13 ou com conhecimento efetivo [F: ftc2025coppa] |
| Base legal | qualquer do art. 7 ou 11, com melhor interesse prevalecente [F: anpd2023enunciado1]; legítimo interesse só com teste de balanceamento documentado [F: anpd2024legitimointeresse] | não altera bases; veda perfilamento publicitário [F: lei15211ecadigital, art. 22 e 26] | qualquer do art. 6; legítimo interesse pesa contra o controlador se o titular é criança e não vale para autoridades públicas [F: eu2016gdpr, art. 6(1)] | não altera bases; condiciona o desenho | consentimento parental verificável como regra, com exceções do §312.5(c) [F: ftc2025coppa] |
| Verificação parental | "esforços razoáveis [...] consideradas as tecnologias disponíveis" [F: brasil2018lgpd, art. 14, §5] | consentimento para download "vedada a presunção de autorização" [F: lei15211ecadigital, art. 12, §2] | "reasonable efforts [...] taking into consideration available technology" [F: eu2016gdpr, art. 8(2)] | não trata de consentimento; trata de age assurance proporcional ao risco [F: ico2020aadc, §3] | métodos enumerados, incluindo "text plus" desde 2025 [F: ftc2025coppa, §312.5(b)(2); F: ftc2025coppafinalrule] |
| Consentimento pela escola | sem regra; ANPD aceita legítimo interesse da escola em relação direta com alunos (exemplo wi-fi) [F: anpd2024legitimointeresse, ex. 2] | sem regra | sem regra específica | sem regra | escola como "parent's agent", só para fim educacional e sem uso comercial [F: ftc2025coppafaq, §N]; exceção formal não adotada em 2025 [F: ftc2025coppafinalrule] |
| Desenho e padrões | informação acessível à criança; não condicionar participação a dados excessivos [F: brasil2018lgpd, art. 14, §4 e §6] | privacidade por padrão no nível mais alto; gestão de riscos; sem uso compulsivo [F: lei15211ecadigital, art. 7 e 8] | linguagem clara para crianças [F: eu2016gdpr, art. 12(1)] | 15 padrões (defaults, minimização, geolocalização, nudges, perfilamento etc.) [F: ico2020aadc] | segurança escrita e política de retenção escrita; retenção indefinida proibida [F: ftc2025coppafinalrule] |
| Dado de saúde e deficiência | sensível; só art. 11; legítimo interesse excluído [F: brasil2018lgpd, art. 5, II e 11; F: anpd2024legitimointeresse] | não trata | categoria especial do art. 9; consentimento explícito ou lei [F: eu2016gdpr, art. 9] | sem regra própria; [I] coberto pelos padrões de DPIA e "detrimental use of data", cujo conteúdo não foi lido | não é categoria à parte; entra como personal information quando identificável [I] |
| Decisão automatizada | direito de revisão e de informação sobre critérios [F: brasil2018lgpd, art. 20] | não trata | direito de não ser submetido; intervenção humana; "should not concern a child" [F: eu2016gdpr, art. 22; cons. 71] | há padrão específico de "profiling" (título visto; conteúdo não lido) [F: ico2020aadc] | não trata |
| Avaliação de impacto | ANPD "poderá determinar" RIPD; ANPD orienta fazê-lo em alto risco [F: brasil2018lgpd, art. 38; F: anpd2024legitimointeresse] | relatório de impacto se o tratamento exceder o estritamente necessário [F: lei15211ecadigital, art. 16] | DPIA (art. 35, não lido nesta sessão) | padrão 2, DPIA obrigatória [F: ico2020aadc] | não exige |
| Autoridade | ANPD | ANPD, por decreto [F: lei15211ecadigital, art. 34] | autoridades nacionais | ICO | FTC |
| Sanção máxima | multa até 2% do faturamento, limitada a R$ 50 milhões por infração [F: brasil2018lgpd, art. 52, II] | multa até 10% do faturamento do grupo no Brasil; suspensão e proibição de atividades pelo Judiciário [F: lei15211ecadigital, art. 35] | não verificado nesta sessão | código, sem multa própria; aplicado via UK GDPR [F: ico2020aadc] | não verificado nesta sessão |

### Leitura da tabela

- **Onde o Brasil é mais exigente** [I]: o limiar de consentimento parental reforçado (12 anos) é mais baixo que o do GDPR (13 a 16), mas o melhor interesse se aplica até 18 e a qualquer base legal, o que não tem paralelo direto no GDPR; o Estatuto Digital traz deveres de desenho com força de lei e multa de 10%, acima do teto da LGPD. Um desenho conforme apenas ao GDPR, portanto, não basta.
- **Onde o Brasil é silencioso** [I]: consentimento dado pela escola (COPPA), métodos aceitos de verificação parental (COPPA), métodos de age assurance (AADC, agora em regulamentação pela ANPD via Decreto 12.880/2026) e padrões de desenho específicos por faixa etária (AADC). Nesses pontos os regimes estrangeiros funcionam como referência de prática.
- **Convergências** [I]: a fórmula "esforços razoáveis / tecnologias disponíveis" é comum à LGPD e ao GDPR; a proibição de perfilamento publicitário de menores aparece no Estatuto Digital, no considerando 38 do GDPR e no padrão de perfilamento do AADC; a retenção limitada à finalidade está na LGPD (necessidade, art. 6, III) e na COPPA (§312.10).

## Métricas e métodos de avaliação

Para avaliar a conformidade de uma plataforma contra esse quadro, os critérios verificáveis derivados das fontes são: (1) base legal registrada por operação, com teste de balanceamento documentado quando for legítimo interesse [F: anpd2024legitimointeresse]; (2) existência de RIPD quando houver dados de menores ou dados de saúde [F: anpd2024legitimointeresse; F: lei15211ecadigital, art. 16]; (3) configuração padrão auditável no nível mais protetivo [F: lei15211ecadigital, art. 7]; (4) política escrita de retenção com prazos [F: ftc2025coppafinalrule]; (5) informação em linguagem adequada à criança, testada com o público [F: brasil2018lgpd, art. 14, §6; F: eu2016gdpr, art. 12(1)]; (6) ausência de qualquer perfilamento publicitário [F: lei15211ecadigital, art. 22].

## Relações com outros conceitos

Os três documentos da área (psg.legal.lgpd-children, psg.legal.eca-and-digital-eca, psg.legal.gdpr-k-and-coppa) são partes desta comparação. As linhas "verificação parental" e "consentimento pela escola" são desenvolvidas em psg.consent.parental-consent; a linha "avaliação de impacto", em psg.audit.ripd-dpia. Complementa iop.br.lgpd, que trata a LGPD na troca de dados entre sistemas.

## Lacunas e questões abertas

- Sanções do GDPR (art. 83) e da COPPA (penalidades civis) não foram verificadas nesta sessão e ficaram como "não verificado".
- O art. 35 do GDPR (DPIA) não foi lido; a célula remete ao conhecimento geral e deve ser conferida.
- Falta na comparação a regulamentação da ANPD sobre age assurance prevista no Decreto 12.880/2026, ainda não editada na data de consulta.
- A comparação não cobre o FERPA (EUA), referido pela FTC como motivo para não finalizar a exceção escolar da COPPA, nem a Convenção sobre os Direitos da Criança em texto primário (citada via guia da ANPD).

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-29 |
| lei8069eca | normativo | 2026-10-29 |
| lei15211ecadigital | normativo | 2026-10-29 |
| anpd2023enunciado1 | normativo | 2026-10-29 |
| anpd2024legitimointeresse | tecnico | 2026-10-29 |
| eu2016gdpr | normativo (lido em espelho) | 2026-10-29 |
| ico2020aadc | normativo | 2026-10-29 |
| ftc2025coppa | normativo | 2026-10-29 |
| ftc2025coppafinalrule | normativo | 2026-10-29 |
| ftc2025coppafaq | tecnico | 2026-10-29 |
