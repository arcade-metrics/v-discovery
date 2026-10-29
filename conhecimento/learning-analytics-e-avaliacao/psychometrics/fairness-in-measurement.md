---
id: lae.psy.fairness-in-measurement
titulo: Equidade e viés de medição em avaliação
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [wikipedia2026dif, jensen1980bias, aera2014standards, baker2022bias, gardner2019slicing, chinta2024fairaied]
relacoes:
  - { tipo: depende-de, alvo: lae.psy.reliability-and-validity }
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: relacionado-a, alvo: lae.psy.classical-test-theory }
termos: [differential item functioning, DIF, viés de teste, cultural loading, item impact, Mantel-Haenszel, fairness, equidade, viés algorítmico, fairness em educational data mining]
---

# Equidade e viés de medição em avaliação

## Definição e terminologia

Equidade de medição (measurement fairness) trata de se um instrumento de avaliação mede o mesmo construto, com a mesma precisão, para diferentes subgrupos de respondentes (por exemplo, definidos por gênero, raça/etnia, língua materna ou deficiência), de modo que diferenças de escore entre grupos reflitam diferenças reais no construto medido, não um artefato do próprio instrumento [I, síntese da literatura sobre o tema]. O conceito central para formalizar essa checagem no nível do item é o **differential item functioning (DIF)**, também chamado funcionamento diferencial do item: ocorre quando respondentes de grupos diferentes, mas com o mesmo nível do traço latente (mesma proficiência real), têm probabilidades desiguais de responder corretamente a um item [F: wikipedia2026dif]. A distinção crucial é entre DIF e **impacto do item (item impact)** ou diferença bruta de grupo: dois grupos apresentarem desempenho médio diferente no teste não configura, por si só, DIF, porque os grupos podem genuinamente diferir no traço que o teste mede; DIF exige condicionar a comparação ao nível de proficiência (via escore total ou estimativa de traço latente) antes de julgar se há tratamento desigual do item [F: wikipedia2026dif].

O termo "viés de teste culturalmente carregado" (culturally loaded test bias) remete a um debate histórico mais amplo sobre se testes padronizados — sobretudo de inteligência — discriminam grupos minoritários por conteúdo ou formato vinculados à cultura majoritária, independentemente da habilidade real medida. Esse debate ganhou formulação influente, e historicamente controversa, no livro de Jensen (1980), que propôs separar formalmente diferença estatística de grupo (um fato populacional) de viés de teste propriamente dito (uma falha psicométrica do instrumento), concluindo — de forma contestada por revisores contemporâneos — que a evidência então disponível não sustentava a hipótese de viés cultural generalizado nos testes de inteligência mais usados nos Estados Unidos à época [F: jensen1980bias, metadados e resumo via fontes secundárias; conclusões do autor não endossadas por esta base, apenas citadas como marco histórico da distinção metodológica entre diferença de grupo e viés — ver Lacunas]. A literatura e os marcos normativos posteriores deslocaram esse debate para fora da discussão qualitativa sobre "conteúdo culturalmente carregado" e para dentro do aparato estatístico de DIF, que permite testar item a item, de forma reprodutível, se um item funciona de modo diferente entre grupos controlando pela proficiência [I].

## Problema que resolve

Um instrumento de avaliação pode produzir escores consistentes (confiáveis, ver `lae.psy.reliability-and-validity`) e ainda assim penalizar sistematicamente um subgrupo por razões alheias ao construto de interesse — por exemplo, um problema de matemática ambientado em um contexto culturalmente específico pode ser mais difícil para quem não tem familiaridade com esse contexto, independentemente da habilidade matemática real. Detectar e corrigir esse tipo de falha é necessário tanto por motivos éticos e legais quanto porque viés de item não detectado compromete a validade do instrumento para os subgrupos afetados (ver a "evidência baseada nas consequências da testagem" em `lae.psy.reliability-and-validity`) — e, quando os escores desse instrumento alimentam um indicador ou um modelo preditivo de `aprendizagem-adaptativa`, o viés de medição se propaga para decisões automatizadas rio abaixo.

## Fundamentos e funcionamento

### Tipos de DIF

A literatura distingue dois padrões de funcionamento diferencial, definidos em termos das curvas características do item (ICC, ver `adp.irt.item-response-theory`) estimadas separadamente para cada grupo [F: wikipedia2026dif]:

- **DIF uniforme**: as curvas características do item dos dois grupos permanecem afastadas, sem se cruzar, ao longo de toda a escala do traço — um grupo é favorecido em todos os níveis de proficiência. Em termos de parâmetros de IRT, corresponde a discriminações iguais entre grupos, mas dificuldades diferentes [F: wikipedia2026dif].
- **DIF não uniforme**: a direção ou a magnitude da vantagem muda ao longo da escala — as curvas podem se cruzar em algum ponto, favorecendo um grupo em um extremo da proficiência e o outro grupo no extremo oposto. Corresponde a discriminações diferentes entre grupos, possivelmente também com dificuldades diferentes [F: wikipedia2026dif].

### Métodos de detecção

- **Mantel-Haenszel (MH)**: método baseado em tabelas de contingência qui-quadrado; os respondentes são agrupados em estratos de escore total (proxy de proficiência), formando uma tabela 2×2 por estrato, e os estratos são combinados em uma razão de chances comum (odds ratio). O Educational Testing Service (ETS) usa uma escala derivada desse odds ratio (delta MH) para classificar itens em categorias A (DIF desprezível), B (moderado) e C (grande) [F: wikipedia2026dif]. A limitação principal do método é detectar bem apenas DIF uniforme [F: wikipedia2026dif].
- **Regressão logística**: ajustada item a item, com preditores para o escore de pareamento (proxy de proficiência), a variável de grupo e a interação entre ambos; testa-se a significância conjunta via estatística qui-quadrado com 2 graus de liberdade. Diferença nos interceptos ou no efeito do escore de pareamento entre grupos sugere DIF uniforme; interação significativa sugere DIF não uniforme — o método de Swaminathan e Rogers mostrou, em simulação, maior poder que Mantel-Haenszel para detectar DIF não uniforme, mantendo poder equivalente para DIF uniforme [F: wikipedia2026dif].
- **Teste de razão de verossimilhanças baseado em IRT**: compara um modelo restrito, em que os parâmetros do item são forçados a ser iguais entre grupos, com um modelo livre, em que os parâmetros variam por grupo; a estatística G² = 2·ln(L_livre/L_restrito) é comparada a uma distribuição qui-quadrado com graus de liberdade iguais ao número de restrições testadas, usando itens-âncora (sem DIF, por suposição) para ancorar a escala comum entre grupos [F: wikipedia2026dif].

### Fairness em modelos preditivos que usam esses instrumentos como insumo

Quando escores de instrumentos psicométricos alimentam modelos preditivos educacionais — por exemplo, um modelo de risco de evasão construído sobre notas de avaliações formativas —, o viés de medição no insumo (DIF não corrigido) pode se somar a vieses introduzidos pelo próprio pipeline de aprendizado de máquina. Baker e Hawn revisam evidências empíricas de viés algorítmico em educação, cobrindo da coleta de dados ao uso do modelo, com maior volume de evidência para raça/etnia, gênero e nacionalidade, e menos evidência disponível para categorias como deficiência e status socioeconômico [F: baker2022bias]. Gardner, Brooks e Baker propõem uma análise de fatiamento (slicing analysis) para avaliar a equidade de modelos preditivos de desempenho estudantil, comparando métricas de desempenho do modelo entre subgrupos demográficos em vez de reportar apenas uma métrica agregada para a população inteira [F: gardner2019slicing]. Uma revisão mais recente situa esse problema no contexto mais amplo de IA educacional, argumentando que a literatura se divide entre trabalhos de fairness algorítmica sem contexto educacional específico e trabalhos de métodos educacionais que não tratam fairness, e propondo organizar as fontes de viés em três categorias — relacionadas a dados, ao algoritmo e à interação do usuário [F: chinta2024fairaied, resumo consultado via busca — texto integral não lido linha a linha nesta sessão]. [I] A ligação conceitual entre DIF e fairness algorítmica é direta: ambos perguntam se uma mesma "verdade" subjacente (proficiência real, ou risco real) está sendo medida ou predita de forma equivalente entre subgrupos, condicionando corretamente na variável de interesse antes de comparar grupos — a diferença é que DIF opera no nível do item psicométrico, com instrumental estatístico maduro e padronizado (MH, regressão logística, IRT), enquanto a literatura de fairness em EDM/LA ainda carece de um conjunto de métricas igualmente consolidado [F: chinta2024fairaied, quanto à constatação da lacuna de consolidação].

## Requisitos e pressupostos

- Detectar DIF exige uma medida de pareamento (matching variable) razoavelmente livre de viés — tipicamente o escore total do próprio teste ou uma estimativa de traço latente — para condicionar a comparação entre grupos; se essa variável de pareamento já carrega viés sistemático, os métodos de DIF podem não detectá-lo corretamente [I].
- Métodos baseados em IRT (teste de razão de verossimilhanças) exigem itens-âncora presumidamente livres de DIF para ancorar a escala comum entre grupos — pressuposto que precisa ser verificado iterativamente, não assumido a priori [F: wikipedia2026dif].
- Zumbo recomenda um mínimo de cerca de 20 itens para a análise de DIF ter poder estatístico razoável, segundo a página de referência consultada — não verificado diretamente na fonte primária [F: wikipedia2026dif, citando Zumbo 1999 indiretamente].
- Análises de fairness em modelos preditivos (slicing analysis) exigem que as categorias demográficas usadas para definir subgrupos estejam disponíveis e sejam de qualidade suficiente nos dados — problema que se conecta à proveniência e qualidade de dados tratada em `data-quality/` deste domínio.

## Vantagens e limitações

**Vantagens**: DIF oferece um critério estatístico operacional, item a item, que substitui o julgamento qualitativo impressionista sobre "conteúdo culturalmente carregado" por um procedimento reprodutível e auditável [I]. A análise de fatiamento de modelos preditivos estende esse espírito — métricas desagregadas por subgrupo, não apenas agregadas — para além da avaliação de itens, até indicadores e modelos de risco [F: gardner2019slicing].

**Limitações**: identificar DIF estatisticamente não implica automaticamente explicar sua causa — um item pode exibir DIF por motivos legítimos relacionados ao construto (por exemplo, um item de leitura em um teste de matemática realmente exige mais de respondentes com menor proficiência em leitura, o que pode ou não ser considerado viés dependendo do construto pretendido) [I, tensão amplamente discutida na literatura sobre a diferença entre DIF e "viés" propriamente dito]. A detecção de DIF depende da variável de pareamento estar livre de viés circular, o que nem sempre é trivial de garantir [I]. Na fronteira com fairness algorítmica, a revisão de Baker e Hawn nota que a maior parte da evidência empírica disponível se concentra em poucas categorias demográficas e em poucos países, deixando lacunas relevantes para outros contextos [F: baker2022bias].

## Alternativas e comparações

| Abordagem | Nível de análise | Instrumental típico | Maturidade |
|---|---|---|---|
| DIF clássico (Mantel-Haenszel) | item, dentro de um teste | tabela de contingência, odds ratio | alta, uso consolidado desde os anos 1980-90 [F: wikipedia2026dif] |
| DIF por regressão logística | item, dentro de um teste | regressão logística com interação grupo×proficiência | alta, mais sensível a DIF não uniforme [F: wikipedia2026dif] |
| DIF via IRT (razão de verossimilhanças) | item, dentro de um teste calibrado por IRT | comparação de modelos restrito/livre | alta, mas exige infraestrutura de calibração de IRT (ver `adp.irt.item-response-theory`) [F: wikipedia2026dif] |
| Slicing analysis de modelo preditivo | predição agregada de um modelo de ML educacional | métricas de desempenho desagregadas por subgrupo | emergente, sem padronização de métricas equivalente ao DIF [F: gardner2019slicing; chinta2024fairaied] |

## Métricas e métodos de avaliação

Ver Fundamentos acima (delta MH, estatística de regressão logística, G² de razão de verossimilhanças) para DIF no nível do item. Para modelos preditivos, a análise de fatiamento compara métricas de desempenho do modelo (acurácia, taxa de falsos positivos/negativos, calibração) entre subgrupos definidos por atributos demográficos, sem reduzir a avaliação de equidade a um único número agregado [F: gardner2019slicing].

## Exemplo técnico independente de domínio

Esboço do procedimento de Mantel-Haenszel para um item, de forma independente de software (pseudocódigo):

```
entrada: respostas (0/1) ao item, grupo (referência/focal), escore_total de cada respondente
estratificar respondentes por escore_total em k faixas

para cada estrato k:
    montar tabela 2x2: {grupo, acerto} dentro do estrato
    a_k, b_k, c_k, d_k = celulas da tabela (acerto/erro x referencia/focal)

alfa_MH = soma(a_k * d_k / n_k) / soma(b_k * c_k / n_k)   # odds ratio combinado
MH_D-DIF = -2.35 * ln(alfa_MH)                             # escala ETS; 0 indica ausência de DIF

classificar item conforme magnitude de MH_D-DIF (categorias A/B/C da ETS)
```

## Relações com outros conceitos

Depende da distinção entre confiabilidade e validade estabelecida em `lae.psy.reliability-and-validity` — DIF é, essencialmente, uma ameaça específica à validade de um instrumento para subgrupos, categorizável sob a "evidência baseada nas consequências da testagem" dos Standards. Usa o aparato de curvas características do item da teoria de resposta ao item (`adp.irt.item-response-theory`) como uma de suas formas de detecção. Contrasta com a teoria clássica dos testes (`lae.psy.classical-test-theory`), cujas estatísticas de item (dificuldade, discriminação) não condicionam por proficiência e por isso não distinguem, por si só, diferença de grupo de funcionamento diferencial de item.

## Lacunas e questões abertas

- O livro de Jensen (1980) é citado aqui apenas como marco histórico da distinção metodológica entre diferença de grupo e viés de teste; suas conclusões substantivas sobre ausência de viés cultural nos testes então vigentes foram contestadas por revisores contemporâneos e não são endossadas por esta base. O texto completo não foi acessado nesta sessão — apenas metadados e resumos de terceiros.
- Não foi localizada, nesta sessão, uma fonte acadêmica primária de acesso aberto sobre DIF (ex. um capítulo de handbook ou artigo de revisão); a exposição acima apoia-se no verbete da Wikipedia sobre DIF, tratado como fonte secundária por falta de alternativa primária acessível no tempo de pesquisa disponível. Revisão futura deveria substituir essa fonte por uma revisão acadêmica primária (ex. Holland e Wainer, 1993; Camilli, 2006; Zumbo, 1999), nenhuma delas verificada diretamente aqui.
- O artigo de Chinta et al. (2024) sobre fairness em IA educacional foi consultado apenas em resumo; a categorização de fontes de viés (dados, algoritmo, interação do usuário) não foi verificada linha a linha no corpo do artigo.
- Não foi aprofundada aqui a conexão entre fairness em medição e frameworks mais amplos de fairness algorítmica geral (ex. paridade demográfica, equalized odds) fora do contexto educacional — ficaria como extensão futura, possivelmente em um documento específico se o domínio crescer nessa direção.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| wikipedia2026dif | secundario | 2026-10-29 |
| jensen1980bias | academico [metadados; marco histórico controverso] | 2026-10-29 |
| aera2014standards | normativo [conteúdo via fontes secundárias] | 2026-10-29 |
| baker2022bias | academico | 2026-10-29 |
| gardner2019slicing | academico | 2026-10-29 |
| chinta2024fairaied | academico [resumo] | 2026-10-29 |
