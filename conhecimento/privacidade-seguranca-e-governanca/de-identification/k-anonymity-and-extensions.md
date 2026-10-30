---
id: psg.deid.k-anonymity-and-extensions
titulo: k-anonimato, l-diversidade e t-closeness
tipo: tecnica
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [sweeney2002kanonymity, machanavajjhala2007ldiversity, li2007tcloseness, sweeney2000demographics, anpd2023anonimizacaoprocesso, nist2023sp800188, rocher2019estimating, daries2014privacy, waldo2014anonymity]
relacoes:
  - { tipo: parte-de, alvo: psg.deid.anonymization-and-pseudonymization }
  - { tipo: alternativa-a, alvo: psg.deid.differential-privacy }
  - { tipo: avaliado-por, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
  - { tipo: relacionado-a, alvo: adp.eval.heterogeneous-populations }
termos: [k-anonimato, quase-identificador, classe de equivalência, generalização, supressão, l-diversidade, t-closeness, ataque de ligação, ataque de homogeneidade, ataque por conhecimento de fundo, ataque de assimetria, ataque de similaridade, ataque temporal, release complementar, divulgação de identidade, divulgação de atributo]
---

# k-anonimato, l-diversidade e t-closeness

## Definição e terminologia

O **k-anonimato** é um modelo formal de proteção para publicação de microdados tabulares proposto por Sweeney: "a release provides k-anonymity protection if the information for each person contained in the release cannot be distinguished from at least k-1 individuals whose information also appears in the release" [F: sweeney2002kanonymity, resumo]. Formalmente (Definição 3): dada uma tabela RT(A1,...,An) e o quase-identificador QI_RT associado, RT satisfaz k-anonimato se e somente se cada sequência de valores em RT[QI_RT] aparece com pelo menos k ocorrências em RT[QI_RT] [F: sweeney2002kanonymity, §3.1]. O **quase-identificador** (termo que Sweeney atribui a Dalenius) é o conjunto de atributos que, embora não identifiquem sozinhos, aparecem também em bases externas e permitem ligação (Definição 2 e "assumption (quasi-identifier)": o detentor dos dados conhece quais atributos aparecem externamente) [F: sweeney2002kanonymity, §3]. Cada grupo de registros com os mesmos valores de quase-identificador é uma **classe de equivalência** (termo usado por Li et al. e pela ANPD) [F: li2007tcloseness, §1; anpd2023anonimizacaoprocesso, §2.3].

As duas técnicas canônicas para atingir k-anonimato são **generalização** (substituir valores por outros menos específicos e semanticamente consistentes, por exemplo CEP 02141 por 0214*, data de nascimento por ano) e **supressão** (remover o valor ou o registro) [F: sweeney2002kanonymity, §2 e Figura 2; li2007tcloseness, §1]. O k-anonimato é "a special case of k-map protection where k is enforced on the released data": no k-map, k é medido contra a população externa; no k-anonimato, contra a própria tabela publicada [F: sweeney2002kanonymity, §3.1].

Dois tipos de divulgação indevida organizam as extensões: **divulgação de identidade** (um indivíduo é ligado a um registro) e **divulgação de atributo** (nova informação sobre um indivíduo é revelada, mesmo sem identificar seu registro) [F: li2007tcloseness, §1]. O k-anonimato protege contra a primeira; **l-diversidade** e **t-closeness** foram propostas para a segunda.

## Problema que resolve

A prática corrente de remover identificadores explícitos e supor anonimato falha porque os dados restantes podem ser ligados a outras bases. Sweeney relata que 87% da população dos Estados Unidos (216 de 248 milhões, Censo de 1990) tinha combinação provavelmente única de {CEP de 5 dígitos, sexo, data de nascimento}, e que, com a lista de eleitores de Cambridge comprada por vinte dólares, ligou dados hospitalares "anônimos" da Group Insurance Commission de Massachusetts ao então governador William Weld: seis pessoas na lista tinham sua data de nascimento, três eram homens e só ele morava no seu CEP [F: sweeney2002kanonymity, §1, Exemplo 1; sweeney2000demographics, resumo]. O k-anonimato torna a ligação ambígua entre pelo menos k candidatos; "the greater the number of candidates provided, the more ambiguous the linking" [F: sweeney2002kanonymity, §1].

## Fundamentos e funcionamento

**Ataques contra o k-anonimato reconhecidos por Sweeney.** (1) *Unsorted matching*: se duas releases k-anônimas da mesma tabela preservam a ordem das tuplas, o casamento por posição revela informação; corrige-se embaralhando aleatoriamente as linhas. (2) *Release complementar*: uma release posterior da mesma base deve tratar todos os atributos da release anterior como quase-identificador, ou basear-se nela; caso contrário, a junção (no exemplo, pelo atributo Problem) produz tuplas únicas. (3) *Ataque temporal*: bases mudam; uma release feita sobre a versão em t pode, ligada à release em t0, quebrar o k-anonimato, pelo que releases posteriores devem considerar a anterior como informação externa [F: sweeney2002kanonymity, §4.1 a §4.3].

**Ataques que motivam a l-diversidade.** Machanavajjhala, Kifer, Gehrke e Venkitasubramaniam mostram que uma tabela k-anônima pode vazar atributos sensíveis por *homogeneidade* (todos os registros da classe de equivalência têm o mesmo valor sensível: Alice sabe que Bob, 31 anos, CEP 13053, está numa classe de quatro registros em que todos têm câncer) e por *conhecimento de fundo* (Alice sabe que Umeko é japonesa e que a incidência de doença cardíaca entre japoneses é muito baixa, logo infere infecção viral) [F: machanavajjhala2007ldiversity, §1.1]. Num cálculo ilustrativo, com 60.000 tuplas, atributo sensível com três valores não correlacionados e 5-anonimização em cerca de 12.000 grupos, "1 out of every 81 groups will have no diversity", comprometendo cerca de 740 pessoas [F: machanavajjhala2007ldiversity, §1.1].

**Princípio da l-diversidade.** Uma classe de equivalência é l-diversa se tem pelo menos l valores "bem representados" do atributo sensível; a tabela é l-diversa se todas as classes o são [F: machanavajjhala2007ldiversity, §4; li2007tcloseness, Definição 1]. Instanciações: *l-diversidade distinta* (pelo menos l valores distintos; não impede inferência probabilística quando um valor domina); *l-diversidade por entropia* (Definição 4.1: para toda classe q, menos a soma de p(q,s) log p(q,s) é maior ou igual a log(l), o que implica pelo menos l valores distintos); e *(c,l)-diversidade recursiva* (Definição 4.2: ordenadas as contagens r1 >= r2 >= ... >= rm dos valores sensíveis na classe, exige-se r1 < c(rl + r(l+1) + ... + rm), de modo que o adversário precise eliminar l-1 valores para obter divulgação positiva) [F: machanavajjhala2007ldiversity, §4.1 e §4.2]. Os autores apontam a restrição: para que a l-diversidade por entropia seja possível, a entropia da tabela inteira deve ser pelo menos log(l), o que falha quando um valor sensível é muito comum (90% dos pacientes com "heart problems" inviabiliza (c,l)-diversidade recursiva com c < 9) [F: machanavajjhala2007ldiversity, §4.2].

**Ataques que motivam a t-closeness.** Li, Li e Venkatasubramanian argumentam que a l-diversidade "is neither necessary nor sufficient to prevent attribute disclosure": no *ataque de assimetria* (skewness), se 1% da população testa positivo e uma classe tem 50% de positivos, ela satisfaz 2-diversidade mas eleva muito a crença do observador; no *ataque de similaridade*, valores sensíveis distintos mas semanticamente próximos (doenças gástricas diferentes; salários em faixa estreita) revelam quase tanto quanto um valor único [F: li2007tcloseness, resumo e §3]. A **t-closeness** (Definição 2) exige que a distância entre a distribuição do atributo sensível em cada classe de equivalência e a distribuição na tabela inteira não exceda um limiar t; a distância escolhida é a Earth Mover's Distance (EMD), que incorpora a distância semântica entre valores; t "enables one to trade off between utility and privacy", pois limita justamente a correlação entre quase-identificadores e atributo sensível que a release poderia revelar [F: li2007tcloseness, §4 e §5].

## Requisitos e pressupostos

- O detentor consegue enumerar corretamente o quase-identificador. Sweeney admite que, se ele "misjudges which attributes are sensitive for linking", a release pode ser menos anônima do que se supõe, cabendo a políticas, leis e contratos a proteção complementar [F: sweeney2002kanonymity, §3].
- Existe uma hierarquia de generalização semanticamente aceitável para cada atributo; para dados não tabulares (imagens, fluxos) a ANPD observa que a generalização pode ser inviável [F: anpd2023anonimizacaoprocesso, §2.4].
- Releases múltiplas são controladas como um todo (ataques complementar e temporal) [F: sweeney2002kanonymity, §4].
- Para l-diversidade e t-closeness, o atributo sensível está identificado e sua distribuição global é conhecida pelo publicador [F: li2007tcloseness, §4].

## Vantagens e limitações

O k-anonimato é simples de explicar e verificar: quem conhece só o quase-identificador de um indivíduo não identifica seu registro com confiança maior que 1/k [F: li2007tcloseness, §2]. É a métrica base que a ANPD descreve para mensurar risco: classes de equivalência de tamanho 1 implicam risco de 100%, de tamanho 2, 50%, e o risco médio da tabela é a média ponderada [F: anpd2023anonimizacaoprocesso, §2.3, Tabela 2]. Limitações: não protege contra divulgação de atributo nem contra conhecimento de fundo [F: machanavajjhala2007ldiversity, §1.1]; a utilidade cai com k, l e t; Rocher et al. observam que garantias como k-anonimato "have been shown to be NP-Hard, hard to achieve in modern high-dimensional datasets, and not always sufficient" [F: rocher2019estimating, discussão, citando trabalhos de terceiros]; e não há forma de somar a perda de privacidade de duas releases k-anônimas, ao contrário da privacidade diferencial [F: nist2023sp800188, §4.3.11].

Em dados educacionais o custo em utilidade foi documentado: pesquisadores do MIT e de Harvard aplicaram k-anonimato (k = 5, segundo o coautor Jim Waldo) ao dataset de mais de 800 mil participantes de MOOCs da plataforma edX e, ao refazer as análises originais, obtiveram resultados significativamente diferentes; o NIST registra que, em um caso, a desidentificação reduziu a proporção reportada de estudantes do sexo feminino de 29% para 26% pela necessidade de suprimir atributos, e que "educational data de-identified with the k-anonymity model can also result in the introduction of bias that leads to spurious results" [F: waldo2014anonymity; nist2023sp800188, §3.2.3 nota 21 e §5.4 (esta citando Daries et al.); daries2014privacy, metadados]. O artigo original de Daries et al. não pôde ser lido nesta sessão (ver Lacunas).

## Alternativas e comparações

| Modelo | Protege contra | Parâmetro | Ataque que o motivou | Ataques que permanecem |
|---|---|---|---|---|
| k-anonimato [F: sweeney2002kanonymity] | Divulgação de identidade por ligação | k (tamanho mínimo da classe) | Ligação com bases externas (Weld) | Homogeneidade, conhecimento de fundo, releases múltiplas |
| l-diversidade [F: machanavajjhala2007ldiversity] | Divulgação de atributo por homogeneidade e por l-1 peças de conhecimento de fundo | l (valores bem representados), c | Homogeneidade e conhecimento de fundo | Assimetria, similaridade |
| t-closeness [F: li2007tcloseness] | Ganho de informação sobre a distribuição do atributo sensível na classe | t (distância EMD máxima) | Assimetria e similaridade | Não limita a perda acumulada entre releases; sem garantia probabilística formal |
| Privacidade diferencial (`psg.deid.differential-privacy`) | Qualquer inferência que dependa da presença de um indivíduo | epsilon, delta | Impossibilidade de Dalenius | Utilidade em grupos pequenos; escolha de epsilon |

## Métricas e métodos de avaliação

Tamanho mínimo e distribuição das classes de equivalência; proporção de registros suprimidos e grau de generalização (perda de informação); entropia e contagens ordenadas por classe (para l); EMD por classe (para t); e risco de reidentificação em cenários de promotor e jornalista, descritos em `psg.deid.reidentification-risk` [F: anpd2023anonimizacaoprocesso, §2.3]. A validação de utilidade deve refazer as análises pretendidas sobre o dado desidentificado e comparar com o original, como no caso edX [F: nist2023sp800188, §5.4].

## Exemplo técnico independente de domínio

```
entrada: tabela T, quase-identificador QI, atributo sensível S, hierarquias H[q], parâmetros k, l, t
repetir:
    classes := agrupar(T, QI)                       # classes de equivalência
    viola_k := {c em classes : |c| < k}
    viola_l := {c em classes : entropia(dist(S|c)) < log(l)}
    viola_t := {c em classes : EMD(dist(S|c), dist(S|T)) > t}
    se viola_k, viola_l e viola_t estão vazias: sair do laço
    q := atributo de QI com maior ganho de classes válidas por nível de H[q]
    T := generalizar(T, q, próximo nível de H[q])
    se nenhum q pode ser generalizado: suprimir registros das classes violadoras
embaralhar(T)                                           # contra unsorted matching
registrar(T.QI_publicado := QI ∪ atributos liberados)   # releases futuras tratam tudo como QI
publicar(T); medir utilidade: refazer análises-alvo em T e comparar com original
```

## Relações com outros conceitos

Parte de `psg.deid.anonymization-and-pseudonymization`, como família de técnicas para microdados; alternativa a `psg.deid.differential-privacy`, que troca a garantia sintática por um limite probabilístico; avaliado por `psg.deid.reidentification-risk`. Relaciona-se com `lae.dq.bias-and-validity`, porque supressão e generalização distorcem indicadores (o caso edX), e com `adp.eval.heterogeneous-populations`, porque subgrupos pequenos ou raros formam classes de equivalência pequenas e são os primeiros a ser suprimidos ou generalizados.

## Lacunas e questões abertas

- Daries et al. (2014), "Privacy, Anonymity, and Big Data in the Social Sciences" (Communications of the ACM 57(9), DOI 10.1145/2643132), não pôde ser lido: o repositório DSpace do MIT respondeu 429 e o site da ACM, 403. O valor k = 5 vem do post do coautor Jim Waldo; o efeito de 29% para 26% vem do NIST SP 800-188, que cita o artigo. Os quase-identificadores exatos usados e a proporção de registros removidos não foram verificados.
- A afirmação de que o k-anonimato ótimo é NP-difícil é citada por Rocher et al. a partir de outros trabalhos, não verificados aqui.
- Não há orientação da ANPD sobre valores de k, l ou t; a minuta do guia de anonimização menciona k-anonimização como técnica de mensuração (apêndice III), mas o texto não foi acessado.
- Como definir quase-identificador em séries temporais de interação (em que a própria sequência de eventos é identificadora) fica para `psg.deid.reidentification-risk`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| sweeney2002kanonymity | academico | 2026-10-29 |
| machanavajjhala2007ldiversity | academico | 2026-10-29 |
| li2007tcloseness | academico | 2026-10-29 |
| sweeney2000demographics | academico (working paper) | 2026-10-29 |
| anpd2023anonimizacaoprocesso | tecnico | 2026-10-29 |
| nist2023sp800188 | tecnico | 2026-10-29 |
| rocher2019estimating | academico | 2026-10-29 |
| daries2014privacy | academico (texto integral não acessado; via NIST e post do coautor) | 2026-10-29 |
| waldo2014anonymity | secundario (post do coautor) | 2026-10-29 |
