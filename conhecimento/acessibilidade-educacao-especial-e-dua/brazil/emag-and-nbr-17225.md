---
id: acs.br.emag-and-nbr-17225
titulo: eMAG 3.1 e ABNT NBR 17225 — requisitos brasileiros de acessibilidade digital
tipo: padrao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [governodigital2014emag31, slti2007portaria3, decreto52962004, lei131462015, abnt2025nbr17225, agenciagov2025nbr17225, cgibr2025nbr17225, mpf2025art63, decreto56262005]
relacoes:
  - { tipo: complementa, alvo: acs.br.lbi }
  - { tipo: relacionado-a, alvo: acs.std.wcag }
  - { tipo: relacionado-a, alvo: acs.std.comparison }
  - { tipo: relacionado-a, alvo: acs.std.procurement-en-301-549-and-section-508 }
  - { tipo: avaliado-por, alvo: acs.asmt.conformance-evaluation }
  - { tipo: relacionado-a, alvo: acs.br.libras }
termos: [eMAG, Modelo de Acessibilidade em Governo Eletrônico, SISP, adoção compulsória, adesão voluntária, ABNT NBR 17225, requisito, recomendação, validação automática, validação manual, ASES, audiodescrição, legenda, janela de Libras]
---

# eMAG 3.1 e ABNT NBR 17225

## Definição e terminologia

O **eMAG** (Modelo de Acessibilidade em Governo Eletrônico) é o conjunto de recomendações de acessibilidade web do governo federal brasileiro, mantido pelo órgão de governo digital; a versão vigente é a "Versão 3.1 - Abril 2014" [F: governodigital2014emag31, capa]. O próprio documento diz que "o eMAG trata de uma versão especializada do documento internacional WCAG", voltada ao governo brasileiro, e afirma que "o eMAG não exclui qualquer boa prática de acessibilidade do WCAG" [F: governodigital2014emag31, seção 1]. A versão 3.0 foi feita "apoiando-se na WCAG 2.0, lançada em dezembro de 2008", e a 3.1 trouxe "melhorias no conteúdo do texto para torná-lo mais compreensível" [F: governodigital2014emag31, seções 1.2 e 1.3].

A **ABNT NBR 17225:2025**, "Acessibilidade em conteúdo e aplicações web — Requisitos", é norma técnica brasileira de adoção voluntária, elaborada no Comitê Brasileiro de Acessibilidade (ABNT/CB-040), Comissão de Estudo de Acessibilidade para a Inclusão Digital, e lançada em 11/3/2025 [F: abnt2025nbr17225, metadados; cgibr2025nbr17225]. O texto integral não foi aberto nesta pesquisa; o que se diz do conteúdo vem de comunicados oficiais e técnicos.

O que não são: nenhum dos dois é lei. O eMAG é obrigatório por portaria para um conjunto delimitado de órgãos; a NBR 17225 só se torna obrigatória se um ato normativo a incorporar [I, a partir de mpf2025art63].

## Problema que resolve

A LBI exige acessibilidade de sítios "conforme as melhores práticas e diretrizes de acessibilidade adotadas internacionalmente" sem dizer quais [F: lei131462015, art. 63]. O eMAG e a NBR 17225 traduzem esse dever genérico em critérios verificáveis em português, o primeiro para a administração federal, a segunda para qualquer organização [I].

## Fundamentos e funcionamento

### eMAG 3.1

**Base de obrigatoriedade.** A Portaria SLTI/MPOG nº 3, de 7/5/2007, determina que portais, sítios, sistemas e programas de TIC da "Administração Pública Federal direta, autárquica e fundacional" sigam diretrizes sistematizadas no eMAG, "de adoção compulsória pelos órgãos e entidades integrantes do Sistema de Administração dos Recursos de Informação e Informática – SISP" [F: slti2007portaria3, art. 1, caput e §1]. Para estados, municípios, Distrito Federal e "pessoas jurídicas de direito privado que mantenham relacionamento por meio eletrônico com a Administração Pública Federal", a disseminação se dá "por meio da adesão voluntária" [F: slti2007portaria3, art. 1, §2]. O eMAG descreve a portaria como tendo tornado "sua observância obrigatória nos sítios e portais do governo brasileiro" [F: governodigital2014emag31, seção 1.2], formulação mais ampla que a da própria portaria; prevalece o texto da portaria [I]. O Decreto 5.296/2004 já obrigava a acessibilidade dos portais da administração pública, com símbolo na página de entrada [F: decreto52962004, art. 47].

**Estrutura.** As 45 recomendações "não estão divididas por níveis de prioridade e sim por área" [F: governodigital2014emag31, seções 1.3 e 3]; a versão 3.0 promoveu o "abandono dos níveis de prioridade A, AA e AAA" [F: governodigital2014emag31, seção 1.2]. As seções são Marcação, Comportamento (DOM), Conteúdo/Informação, Apresentação/Design, Multimídia e Formulário [F: governodigital2014emag31, seção 3].

**Multimídia e Libras.** A recomendação 5.1 exige alternativa para vídeo e legendas para vídeo com áudio, mas trata Libras como desejável: "é desejável que os vídeos com áudio apresentem alternativa na Língua Brasileira de Sinais (Libras)"; a 5.2 exige transcrição de áudio gravado, "também é desejável a alternativa em Libras"; a 5.3 exige audiodescrição para vídeo pré-gravado cujo conteúdo visual não esteja na faixa de áudio; 5.4 e 5.5 exigem controle de áudio e de animação [F: governodigital2014emag31, recomendações 5.1 a 5.5].

**Avaliação.** O documento indica o ASES como ferramenta e adverte que "os validadores automáticos por si só não determinam se um sítio está ou não acessível", sendo "necessária uma posterior validação manual" [F: governodigital2014emag31, seção 2.3].

### ABNT NBR 17225:2025

Segundo o comunicado do Comitê Gestor da Internet, a norma "traz 146 orientações, divididas entre requisitos e recomendações", sobre "interação por teclado, imagens, cabeçalho, uso de cores, formulários, entre outros" [F: cgibr2025nbr17225]. A agência oficial do governo federal informa que ela traz "um checklist prático", foi construída com participação do Ministério dos Direitos Humanos e da Cidadania e de outros órgãos federais, e contribui para o cumprimento do art. 63 da LBI [F: agenciagov2025nbr17225]. O comunicado do CGI.br informa que o conteúdo "pode ser consultado gratuitamente" em plataforma da ABNT [F: cgibr2025nbr17225]. Em 29/8/2025 o MPF registrou que a norma ainda "carece de um ato do Poder Executivo que torne esses e outros parâmetros obrigatórios" [F: mpf2025art63].

## Requisitos e pressupostos

O eMAG pressupõe o modelo de conteúdo de páginas web de 2008 a 2014 (WCAG 2.0); não cobre aplicativos nativos nem critérios acrescentados depois na família WCAG 2.x [I]. A aplicação da NBR 17225 a aplicativos não pôde ser confirmada sem abrir o texto [I].

## Vantagens e limitações

| Aspecto | eMAG 3.1 | ABNT NBR 17225:2025 |
|---|---|---|
| Natureza | Recomendações governamentais | Norma técnica ABNT |
| Força | Compulsório para o SISP; voluntário para os demais [F: slti2007portaria3] | Voluntária até ato que a incorpore [F: mpf2025art63] |
| Base internacional | WCAG 2.0 [F: governodigital2014emag31] | Alinhamento a padrões internacionais afirmado em comunicado [F: agenciagov2025nbr17225]; versão WCAG não verificada |
| Tamanho | 45 recomendações em 6 seções | 146 itens entre requisitos e recomendações [F: cgibr2025nbr17225] |
| Níveis | Sem níveis A/AA/AAA | Requisito x recomendação |
| Libras em vídeo | "Desejável" (5.1, 5.2) | Não verificado |
| Atualização | Sem revisão desde abril de 2014 | Primeira edição, 2025 |
| Acesso | Gratuito, publicado pelo governo | Consulta gratuita informada; texto não aberto aqui |

Vantagens do eMAG: gratuito, em português, com validação automática e manual descritas. Limitações: defasado em mais de uma década e ancorado numa versão antiga de WCAG [I]. A NBR 17225 é mais recente e granular, mas sem força cogente e com acesso ao texto mediado pela ABNT [I].

## Métricas e métodos de avaliação

O eMAG combina validador automático (ASES) e inspeção manual [F: governodigital2014emag31, seção 2.3]; a NBR 17225 traz checklist de testes [F: agenciagov2025nbr17225]. Métodos gerais de conformidade (amostragem, regras de teste, limites das ferramentas) ficam em `acs.asmt.conformance-evaluation`.

## Exemplo técnico independente de domínio

Seleção de referencial técnico por tipo de mantenedor (recomendação deste documento, não exigência legal):

```
se mantenedor ∈ SISP: base = eMAG 3.1 (compulsório) + WCAG 2.x vigente (boa prática admitida pelo eMAG)
senão se mantenedor é empresa com sede no Brasil ou órgão não-SISP:
    base = LBI art. 63 (obrigação) com NBR 17225 como critério técnico (voluntário)
para vídeo educativo: legenda (eMAG 5.1) + audiodescrição se houver conteúdo só visual (5.3)
    + janela de Libras: desejável no eMAG; obrigatória em curso médio/superior a distância (Dec. 5.626 art. 24)
```

O último item decorre do Decreto 5.626/2005, que manda a programação visual de cursos a distância de nível médio e superior "dispor de sistemas de acesso à informação como janela com tradutor e intérprete de Libras" e legenda oculta [F: decreto56262005, art. 24].

## Relações com outros conceitos

Complementa `acs.br.lbi` (art. 63). A família WCAG e o estado do WCAG 3 ficam em `acs.std.wcag`; a comparação entre normas, em `acs.std.comparison`; o paralelo com normas de compra pública estrangeiras, em `acs.std.procurement-en-301-549-and-section-508`. Avaliado por `acs.asmt.conformance-evaluation`. As exigências de Libras em conteúdo digital estão em `acs.br.libras`.

## Lacunas e questões abertas

- Texto integral da NBR 17225 não aberto (acesso mediado pela ABNT); a relação exata com WCAG 2.2, afirmada em fontes secundárias vistas só em resultados de busca, não foi verificada e não é citada como fato.
- Não localizado, em 30/10/2026, ato federal que torne a NBR 17225 obrigatória ou que substitua o eMAG no SISP; a notícia do governo digital sobre o tema exigiu autenticação e não abriu.
- Não verificado se a Portaria SLTI 3/2007 foi alterada; a página de legislação do governo digital a lista sem indicação de revogação.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| governodigital2014emag31 | normativo (documento técnico oficial) | 2026-10-30 |
| slti2007portaria3 | normativo | 2026-10-30 |
| decreto52962004 | normativo | 2026-10-30 |
| decreto56262005 | normativo | 2026-10-30 |
| lei131462015 | normativo | 2026-10-30 |
| abnt2025nbr17225 | normativo [metadados] | 2026-10-30 |
| agenciagov2025nbr17225 | tecnico (agência oficial de notícias) | 2026-10-30 |
| cgibr2025nbr17225 | tecnico (comunicado do CGI.br) | 2026-10-30 |
| mpf2025art63 | tecnico (notícia oficial do MPF) | 2026-10-30 |
