---
id: acs.part.inclusive-and-participatory-design
titulo: Desenho inclusivo e design participativo com pessoas com deficiência
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [treviranus2018dimensions, idrc2026inclusiveguide, microsoft2026inclusivedesign, microsoft2025inclusive101, druin1999role, druin2002role, frauenberger2011designing, benton2015widening, spiel2019agency, ansari2026participatory, charlton2000nothing]
relacoes:
  - { tipo: depende-de, alvo: acs.found.disability-models }
  - { tipo: complementa, alvo: acs.found.universal-design }
  - { tipo: complementa, alvo: acs.asmt.user-testing-with-at }
  - { tipo: complementa, alvo: acs.part.self-determination }
  - { tipo: relacionado-a, alvo: acs.at.aac }
  - { tipo: relacionado-a, alvo: psg.consent.child-assent }
  - { tipo: relacionado-a, alvo: dat.ethics.consent-and-assent-in-research }
termos: [desenho inclusivo, três dimensões do desenho inclusivo, one-size-fits-one, deficiência como desajuste, persona spectrum, solve for one extend to many, design participativo, co-design, nothing about us without us, papéis da criança no design, design partner, informant, tester, participação por procuração, key informant, agência]
---

# Desenho inclusivo e design participativo com pessoas com deficiência

## Definição e terminologia

**Desenho inclusivo** (*inclusive design*) é, na formulação do Inclusive Design Research Centre (IDRC, OCAD University), um desenho que considera toda a diversidade humana e se organiza em três dimensões: reconhecer a diversidade e a singularidade de cada pessoa; usar processos e ferramentas inclusivos; e buscar impacto benéfico mais amplo [F: idrc2026inclusiveguide]. Treviranus, diretora do IDRC, descreve a primeira dimensão como configurações "one-size-fits-one configurations that can be optimized to each user" e a segunda como "Use inclusive, open & transparent processes, and co-design with people who have a diversity of perspectives" [F: treviranus2018dimensions]. A documentação de fornecedor da Microsoft define o desenho inclusivo como "a methodology that enables and draws on the full range of human diversity" e enuncia três princípios: reconhecer a exclusão, aprender com a diversidade e "Solve for one, extend to many" [F: microsoft2026inclusivedesign].

**Design participativo** (*participatory design*, PD) e **co-design** designam processos em que os futuros usuários tomam parte nas decisões de projeto, não só nos testes. Na literatura de interação criança-computador, Benton e Johnson definem o ponto central da participação como "the action of decision-making, i.e. being given the opportunity and support to influence rather than simply providing an opinion" [F: benton2015widening, §1].

O lema "nothing about us without us", que dá título ao livro de Charlton sobre opressão e empoderamento de pessoas com deficiência [F: charlton2000nothing, metadados], é invocado pelo IDRC para afirmar que pessoas com deficiência devem ser parceiras e não sujeitos de pesquisa ou participantes simbólicos [F: idrc2026inclusiveguide].

O que não é: desenho inclusivo não é desenho segregado para um grupo diagnóstico, nem sinônimo de conformidade com norma (ver `acs.std.wcag`, fora desta área); design participativo não é teste de usabilidade, embora possa incluí-lo [I].

## Problema que resolve

Projetos para crianças com deficiência tendem a ser definidos por adultos e por metas corretivas. A revisão crítica de Spiel et al. (185 artigos, 148 projetos sobre tecnologia para crianças autistas) concluiu que 76,2% dos artigos seguiam uma abordagem "informed" (o projeto parte da literatura, sem os usuários), que só 7,3% dos projetos aplicaram processo participativo e que, dos 21 projetos que envolveram partes interessadas, só 10 envolveram diretamente as crianças [F: spiel2019agency, §5]. Os autores concluem que as crianças viram "a secondary audience to the largely externally defined purposes" [F: spiel2019agency, resumo]. Benton e Johnson observam que crianças com necessidades educacionais especiais e deficiência (SEND) tiveram "more limited opportunities to influence technology design" por precisarem de mais apoio durante o processo [F: benton2015widening, §1].

## Fundamentos e funcionamento

### Deficiência como desajuste

A Microsoft adota a fórmula "Disability is equal to mismatched human interactions" e situa a deficiência "at the points of interaction between a person and society" [F: microsoft2025inclusive101]. O *persona spectrum* estende uma necessidade a cenários permanentes, temporários e situacionais (uma pessoa com um braço só; um braço machucado; alguém segurando um bebê) [F: microsoft2025inclusive101]. Essa leitura é próxima do modelo social e do biopsicossocial descritos em `acs.found.disability-models` [I].

### Papéis da criança no processo de design

Druin propôs quatro papéis: *user* (a criança usa tecnologia existente enquanto adultos observam), *tester* (testa protótipos), *informant* (contribui em fases escolhidas pelos pesquisadores) e *design partner* (é "equal stakeholder" durante todo o processo) [F: druin1999role, §1; druin2002role, metadados]. Cada papel inclui elementos dos anteriores [F: druin1999role]. Guha, Druin e colegas, ao revisitar os papéis, afirmaram que um não é melhor que o outro (citado em [F: benton2015widening, §4.1]).

Para crianças com SEND, a literatura adaptou esses papéis [F: benton2015widening, §5.2]:

- Frauenberger et al. adaptaram a escada de Arnstein em três estilos: não participativo; **participação por procuração** (pai, cuidador ou professor fala pela criança); e participação plena.
- Keay-Bright definiu o *key informant* para crianças autistas com comunicação muito limitada, que contribuem interagindo com protótipos rápidos, sem diálogo verbal, e com decisão final do adulto.
- No projeto PD4CAT, com uma menina de quatro anos com paralisia cerebral e dificuldades severas de comunicação, os pesquisadores tiraram requisitos da observação dela e dos cuidadores e depois a envolveram em protótipos de papel para escolher forma, cor e organização da interface; concluíram que ela "was as active as any other team member because she provided the peculiar knowledge she possessed about herself".

### Interpretar o que a criança propõe

No projeto ECHOES (ambiente de aprendizagem de habilidades sociais para crianças com e sem autismo), Frauenberger, Good e Keay-Bright usaram atividades de interesse sensorial e de narrativa para aproximar o mundo imaginário das crianças das restrições do sistema [F: frauenberger2011designing, resumo]. Segundo a síntese de Benton e Johnson, as crianças "expressed their ideas in ways that would not allow us to simply transfer them into our design", e a equipe passou a extrair qualidades das ideias (por exemplo, objetos que se tornam seres vivos) em vez do conteúdo literal [F: benton2015widening, §5.3.1].

## Requisitos e pressupostos

- Apoio à comunicação adequado a cada criança; a revisão de 2026 recomenda estratégias alinhadas à comunicação aumentativa e alternativa e apoio de pais e terapeutas [F: ansari2026participatory, tabela 4].
- Adultos em papéis explícitos: facilitação, motivação, cuidado, procuração e co-design [F: benton2015widening, §6.1].
- Consentimento dos responsáveis e assentimento contínuo da criança (ver `psg.consent.child-assent`).
- Tempo: a maioria dos projetos revisados teve menos de 10 crianças com SEND e cinco sessões ou menos [F: benton2015widening, §5.1].

## Vantagens e limitações

Benefícios relatados para as crianças incluem prazer, empoderamento, orgulho, confiança e habilidades sociais e criativas, mas "there has been no systematic investigation, monitoring or evaluation of these beneficial impacts" [F: benton2015widening, §5.3.2]. Também houve tédio, confusão, frustração e aflição com a espera, e a maioria dos artigos não discutiu efeitos negativos [F: benton2015widening, §5.3.2]. A procuração tem limites: é "unlikely that adults acting as proxies for children with SEND can truly represent the children's views" [F: benton2015widening, §6.1.4]. A evidência é concentrada em autismo: 19 de 49 artigos na revisão de 2015 [F: benton2015widening, §7] e seis de oito estudos na revisão de 2026 sobre tecnologia de comunicação [F: ansari2026participatory, §4.1]. Spiel et al. advertem que incluir crianças não basta se a participação não for "fundamentally meaningful" [F: spiel2019agency, §8.1].

## Alternativas e comparações

| Abordagem | Quem decide | Adequada quando | Risco |
|---|---|---|---|
| Desenho informado pela literatura | Equipe adulta | Pouco acesso aos usuários | Metas externas, criança como público secundário [F: spiel2019agency] |
| Criança como *tester* | Adultos, com feedback da criança | Basta indicar se gosta ou não [F: benton2015widening, §4.1] | Influência só tardia |
| Participação por procuração | Pais, professores | A participação direta seria danosa ou inviável | Visão do adulto no lugar da criança [F: benton2015widening, §6.1.4] |
| *Key informant* / observação do brincar | Adultos interpretam ações | Comunicação não verbal ou não simbólica | Interpretação enviesada [I] |
| *Design partner* | Compartilhada | Criança com meios de dialogar e tempo longo | Sobrecarga [F: ansari2026participatory, §6] |

## Métricas e métodos de avaliação

Benton e Johnson propõem um contínuo de impactos positivos (experiência agradável, empoderamento, competência, habilidades duradouras) e recomendações de relato com quatro lentes: epistemologia, partes interessadas, valores e resultados [F: benton2015widening, §5.3.2 e §7]. A revisão de 2026 pede validação sistemática dos resultados do PD [F: ansari2026participatory, tabela 4]. Indicadores úteis [I]: proporção de decisões de projeto rastreáveis a contribuições das crianças; papel exercido por cada criança em cada fase; registro de recusas e sinais de desconforto.

## Exemplo técnico independente de domínio

```
para cada criança c no projeto:
    perfil_com = avaliar_comunicação(c)            # fala | símbolos | sinais | não simbólica
    papel[c] = escolher(papel_viável(perfil_com), preferência(c))
    para cada fase f em [explorar, idear, prototipar, avaliar]:
        atividade = adaptar(f, perfil_com)         # pranchas, protótipo rápido, brincar livre
        contribuições = registrar(c, atividade, forma=perfil_com)
        se sinais_de_desconforto(c): pausar; reavaliar assentimento
    decisões += vincular(contribuições, decisão_de_projeto, interpretado_por=adulto)
relatar(papéis, procuradores, decisões_rastreáveis, impactos_positivos_e_negativos)
```

## Relações com outros conceitos

Depende de `acs.found.disability-models` para a ideia de deficiência como desajuste. Complementa `acs.found.universal-design` (o produto) com o processo; complementa `acs.asmt.user-testing-with-at`, que trata de testes. Liga-se a `acs.part.self-determination`: participar de decisões é exercício de agência causal. Relaciona-se com `acs.at.aac` (meios de expressão), `psg.consent.child-assent` e `dat.ethics.consent-and-assent-in-research`.

## Lacunas e questões abertas

- O texto integral de Frauenberger, Good e Keay-Bright (2011) e o de Druin (2002) não foram abertos; usou-se o resumo do primeiro e o relatório técnico de 1999 do segundo.
- Quase não há estudos de design participativo com crianças com deficiência intelectual moderada a profunda fora do autismo e da paralisia cerebral.
- Não foi localizada revisão que meça se o design participativo melhora o uso ou a eficácia da tecnologia resultante.
- Falta método validado para interpretar contribuições não verbais sem projetar nelas a visão do adulto.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| treviranus2018dimensions | tecnico | 2026-10-30 |
| idrc2026inclusiveguide | tecnico | 2026-10-30 |
| microsoft2026inclusivedesign | fornecedor | 2026-10-30 |
| microsoft2025inclusive101 | fornecedor | 2026-10-30 |
| druin1999role | academico (relatório técnico) | 2026-10-30 |
| druin2002role | academico [metadados] | 2026-10-30 |
| frauenberger2011designing | academico (resumo no repositório) | 2026-10-30 |
| benton2015widening | academico (cópia do autor) | 2026-10-30 |
| spiel2019agency | academico | 2026-10-30 |
| ansari2026participatory | academico | 2026-10-30 |
| charlton2000nothing | academico [metadados] | 2026-10-30 |
