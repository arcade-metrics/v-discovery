---
id: lae.psy.classical-test-theory
titulo: Teoria clássica dos testes (CTT)
tipo: conceito
dominio: learning-analytics-e-avaliacao
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [crockeralgina1986ctt, hambletonjones1993comparison]
relacoes:
  - { tipo: relacionado-a, alvo: adp.irt.item-response-theory }
  - { tipo: alternativa-a, alvo: adp.irt.item-response-theory }
termos: [classical test theory, escore observado, escore verdadeiro, erro de medição, índice de dificuldade, índice de discriminação, correlação item-total, dependência de amostra, dependência de teste, confiabilidade]
---

# Teoria clássica dos testes (CTT)

## Definição e terminologia

A teoria clássica dos testes (Classical Test Theory, CTT) é o modelo de medição mais antigo e ainda mais usado na prática de avaliação educacional: assume que o escore observado de uma pessoa em um teste (X) é a soma de um escore verdadeiro (T), não observável, e um erro de medição aleatório (E): X = T + E [I, formulação-padrão amplamente reproduzida na literatura de psicometria; a formalização completa com seus axiomas está em crockeralgina1986ctt]. T é definido como a esperança matemática do escore observado em repetições hipotéticas e independentes da mesma medição na mesma pessoa, e E é o desvio de X em relação a essa esperança em cada aplicação [I]. Nomes alternativos: "teoria do escore verdadeiro" (true score theory). O que não é: CTT não modela a resposta a itens individuais como função de um traço latente contínuo — isso é o objeto da teoria de resposta ao item (IRT, ver `adp.irt.item-response-theory`); CTT opera no nível do escore total do teste, não no nível do item isoladamente, ainda que defina estatísticas descritivas por item (ver abaixo) [I].

## Problema que resolve

Toda medição em ciências humanas é imperfeita: a mesma pessoa, testada de novo em condições equivalentes, não produziria exatamente o mesmo escore. A CTT oferece um modelo estatístico mínimo para essa imprecisão — decompor o escore em parte "verdadeira" e parte "erro" — que permite definir formalmente confiabilidade (a proporção da variância do escore observado atribuível ao escore verdadeiro) sem exigir pressupostos fortes sobre a forma funcional da resposta a cada item [I]. Esse modelo fundamenta estatísticas de uso corrente em construção e revisão de testes: quão difícil e quão discriminativo é cada item, e quão consistente é o teste como um todo (ver `lae.psy.reliability-and-validity`).

## Fundamentos e funcionamento

### Pressupostos do modelo clássico

1. **Linearidade**: o escore observado é soma linear de escore verdadeiro e erro, X = T + E [I].
2. **Esperança do erro é zero**: E(E) = 0, ou seja, o erro não enviesa o escore verdadeiro na média de repetições hipotéticas [I].
3. **Erro não correlacionado com o escore verdadeiro**: cov(T, E) = 0 [I].
4. **Erros não correlacionados entre si em formas distintas do teste**: cov(E₁, E₂) = 0 entre duas aplicações ou formas paralelas [I].

Desses pressupostos decorre que a variância do escore observado se decompõe em variância do escore verdadeiro mais variância do erro, σ²(X) = σ²(T) + σ²(E), base da definição clássica de confiabilidade como σ²(T)/σ²(X) (ver `lae.psy.reliability-and-validity`) [I].

### Estatísticas clássicas de item

A CTT descreve cada item do teste por estatísticas calculadas diretamente dos dados de resposta, sem estimar parâmetros de um modelo de variável latente:

- **Índice de dificuldade (p-value)**: proporção de respondentes que acertam o item (ou respondem na direção correta, em itens não dicotômicos); apesar do nome, quanto maior o valor, mais fácil é o item [I, terminologia padrão da área; fonte primária seria crockeralgina1986ctt, não lida em texto completo nesta sessão]. Convenção prática: a dificuldade média de um teste de proveito bem construído fica geralmente entre 0,5 e 0,7, embora isso seja convenção de desenho, não regra formal [I].
- **Índice de discriminação**: tradicionalmente, a correlação entre o acerto no item e o escore total do teste (correlação item-total), interpretada como a capacidade do item de diferenciar respondentes de alta e baixa proficiência [I]. A forma "corrigida" exclui o próprio item do escore total ao calcular a correlação, evitando a autocorrelação espúria que infla o índice quando o item é parte da soma com a qual é correlacionado [I]. Convenções usuais tratam valores de correlação item-total abaixo de aproximadamente 0,10–0,20 como indicação de item problemático, e valores acima de 0,50 como incomuns mesmo para bons itens — novamente convenções, não limiares formais [I].
- **Correlação item-total**: ver acima; é o mesmo índice usado como proxy de discriminação na tradição CTT, calculável com correlação ponto-bisserial (item dicotômico × escore contínuo) ou outras formas conforme o tipo de item [I].

Essas estatísticas são insumo direto para revisão de itens (remover ou reescrever itens com discriminação baixa ou negativa, ajustar dificuldade) e para o cálculo de confiabilidade do teste como um todo (ver `lae.psy.reliability-and-validity`) [I].

## Algoritmos e modelos relevantes

A CTT não define um algoritmo de estimação complexo: os parâmetros de item (p-value, correlação item-total) são estatísticas amostrais simples, computáveis em uma única passada pelos dados, sem iteração nem otimização numérica — diferença central frente aos procedimentos de máxima verossimilhança da IRT (JMLE, MML), que exigem estimação iterativa [I; contraste descrito em `adp.irt.item-response-theory`, seção Estimação]. Essa simplicidade computacional é, em si, parte do motivo de a CTT permanecer de uso corrente mesmo onde a IRT está disponível [I].

## Requisitos e pressupostos

Ver seção de pressupostos acima. Adicionalmente, a interpretação de confiabilidade calculada sob CTT pressupõe que a amostra de respondentes usada para estimar as estatísticas seja representativa da população-alvo de aplicação do teste — porque, ao contrário da IRT, os parâmetros clássicos de item e de teste não são invariantes entre amostras (ver Limitações) [I].

## Vantagens e limitações

**Vantagens**: simplicidade conceitual e computacional; estatísticas de item interpretáveis sem necessidade de software especializado de calibração; funciona com amostras pequenas, onde a estimação de parâmetros de IRT (sobretudo 2PL e 3PL) é instável ou inviável [I]. Essa simplicidade é citada por Hambleton e Jones como uma das razões práticas para a persistência do uso de CTT no desenvolvimento de testes, ao lado da IRT [F: hambletonjones1993comparison — artigo identificado e citação confirmada; conteúdo detalhado do módulo não pôde ser extraído nesta sessão, ver Lacunas].

**Limitações**: 

- **Dependência de amostra (sample-dependence)**: os índices de dificuldade e discriminação de um item mudam conforme a população que respondeu ao teste — um item parece mais fácil em uma amostra de alto desempenho e mais difícil em uma de baixo desempenho, ainda que a "dificuldade intrínseca" do item não tenha mudado [I; este é exatamente o problema que a invariância de item da IRT resolve, conforme descrito em `adp.irt.item-response-theory`, seção Problema que resolve].
- **Dependência de teste (test-dependence)**: o escore de uma pessoa depende de quais itens especificamente compõem o teste aplicado — um exame com itens mais fáceis produz escores mais altos para a mesma proficiência real, o que dificulta comparar pessoas que fizeram versões diferentes do teste sem um procedimento adicional de equalização [I].
- **Confiabilidade como coeficiente único**: a CTT descreve a precisão de medição do teste inteiro por um único número (ver `lae.psy.reliability-and-validity`), que não captura que a precisão real varia ao longo da escala de proficiência — um teste pode medir bem respondentes de nível médio e mal os de nível muito alto ou muito baixo, distinção que só a função de informação da IRT torna explícita [I; descrita em `adp.irt.item-response-theory`, seção Estimação].

## Alternativas e comparações

| Aspecto | CTT | IRT (1–3PL) |
|---|---|---|
| Unidade de análise | escore total do teste [I] | resposta a cada item, função de um traço latente [F: rizopoulos2006ltm, citado em `adp.irt.item-response-theory`] |
| Estatísticas de item | dificuldade (p-value) e discriminação (correlação item-total), amostrais diretas [I] | parâmetros de dificuldade, discriminação e acerto ao acaso, estimados por modelo [F: nguyen2014irt, citado em `adp.irt.item-response-theory`] |
| Invariância | não: parâmetros variam entre amostras e entre testes [I] | sim, quando o modelo ajusta: parâmetros de item e de pessoa comparáveis entre amostras [F: nguyen2014irt, citado em `adp.irt.item-response-theory`] |
| Precisão de medição | um coeficiente de confiabilidade para o teste inteiro [I] | função de informação, variável ao longo da escala de traço [F: nguyen2014irt, citado em `adp.irt.item-response-theory`] |
| Requisito de amostra | funciona com amostras pequenas [I] | amostras maiores, sobretudo para 2PL/3PL [F: nguyen2014irt, citado em `adp.irt.item-response-theory`] |
| Uso típico | construção e revisão de testes de baixo custo, avaliação formativa de sala de aula, instrumentos de pesquisa em ciências sociais [I] | bancos de itens calibrados, testes adaptativos, equalização entre formas [F: magis2012catr, citado em `adp.irt.item-response-theory`] |

A IRT não substitui integralmente a CTT na prática: como nota a literatura que compara os dois marcos, a escolha depende de recursos (tamanho de amostra, software, expertise técnica disponível) e da finalidade do teste — para instrumentos de uso único, de baixo risco, construídos por equipes sem infraestrutura de calibração, a CTT permanece a opção padrão por sua simplicidade, mesmo reconhecendo suas limitações teóricas frente à IRT [F: hambletonjones1993comparison — tema central do artigo, conforme descrição confirmada por fontes secundárias; ver Lacunas quanto ao detalhamento não lido diretamente].

## Métricas e métodos de avaliação

As próprias estatísticas de item (dificuldade, discriminação, correlação item-total) funcionam como métricas de qualidade do item dentro da CTT; a avaliação do teste como um todo é feita por coeficientes de confiabilidade (alfa de Cronbach e alternativas), tratados em `lae.psy.reliability-and-validity`, e não redefinidos aqui.

## Exemplo técnico independente de domínio

Cálculo de estatísticas clássicas de item a partir de uma matriz de respostas binárias (pseudocódigo):

```
entrada: matriz R[pessoa][item] com 0/1 (erro/acerto)
escore_total[pessoa] = soma(R[pessoa][:])

para cada item j:
    p_j = média(R[:][j])                       # índice de dificuldade
    escore_sem_j[pessoa] = escore_total[pessoa] - R[pessoa][j]   # corrige autocorrelação
    discriminacao_j = correlacao(R[:][j], escore_sem_j)          # correlação item-total corrigida

sinalizar para revisão: itens com discriminacao_j < limiar_minimo (ex. 0.20)
                        ou p_j muito próximo de 0 ou de 1 (pouca variância)
```

## Relações com outros conceitos

A CTT é tratada aqui como alternativa histórica e prática à IRT (`adp.irt.item-response-theory`), que resolve as mesmas necessidades de medição — descrever dificuldade, discriminação e precisão — por um caminho diferente, com invariância de parâmetros como diferença central. As estatísticas de item da CTT alimentam diretamente a análise de confiabilidade (`lae.psy.reliability-and-validity`). A fronteira entre viés de item detectável por CTT (diferenças brutas de desempenho entre grupos) e funcionamento diferencial de item propriamente dito é discutida em `lae.psy.fairness-in-measurement`.

## Lacunas e questões abertas

- O artigo de Hambleton e Jones (1993), citado aqui como referência central sobre o trade-off simplicidade-versus-garantias-estatísticas entre CTT e IRT, foi localizado como módulo instrucional em PDF aberto da NCME, mas o arquivo é uma digitalização comprimida cujo texto não pôde ser extraído nesta sessão; as afirmações sobre seu conteúdo vêm de descrições de terceiros sobre o artigo, não de leitura direta. Revisão futura deveria obter uma cópia com camada de texto.
- Crocker e Algina (1986), citado como referência normativa da formalização da CTT (axiomas do escore verdadeiro), não foi acessado em texto completo nesta sessão — apenas metadados bibliográficos foram verificados. A formulação de axiomas apresentada aqui segue a exposição padrão da literatura de psicometria, não uma citação direta do livro.
- Não foram localizadas, nesta sessão, fontes quantitativas atuais (ex. levantamentos de uso) sobre a proporção de testes educacionais de larga escala que ainda usam CTT pura versus IRT; a afirmação de que CTT "continua amplamente usada" é tratada como [I], apoiada apenas na persistência do tema na literatura comparativa, não em dado censitário.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| crockeralgina1986ctt | academico [metadados] | 2026-10-29 |
| hambletonjones1993comparison | academico [citação confirmada; conteúdo não extraído] | 2026-10-29 |
