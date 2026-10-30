---
id: acs.adapt.algorithmic-adaptation-and-autonomy
titulo: Adaptação algorítmica e autonomia
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [findlater2004comparison, gajos2008predictability, horvitz1999principles, wobbrock2011ability, vanderheiden2012autopersonalization, imsglobal2021afapnp, gag2026fulllist, microsoft2022xag108]
relacoes:
  - { tipo: depende-de, alvo: acs.part.self-determination }
  - { tipo: complementa, alvo: acs.adapt.preference-profiles }
  - { tipo: complementa, alvo: psg.ai.transparency-and-human-oversight }
  - { tipo: complementa, alvo: adp.lm.open-learner-model }
  - { tipo: relacionado-a, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: relacionado-a, alvo: gam.diff.dynamic-difficulty-adjustment }
  - { tipo: relacionado-a, alvo: acs.adapt.adapting-games-and-activities }
  - { tipo: relacionado-a, alvo: psg.consent.child-assent }
termos: [interface adaptativa, interface adaptável, iniciativa mista, controlabilidade, previsibilidade, acurácia da adaptação, invocação e término diretos, transparência da adaptação, ability-based design, autonomia, controle do aprendiz]
---

# Adaptação algorítmica e autonomia

## Definição e terminologia

A literatura de interação humano-computador distingue três formas de mudar uma interface conforme a pessoa: adaptativa, em que "The system controls change"; adaptável (ou personalizável), em que "The user controls change"; e de iniciativa mista, em que o controle é compartilhado [F: findlater2004comparison, introdução]. Adaptação algorítmica, aqui, é a adaptativa: o sistema infere do comportamento o que mudar (dificuldade, ritmo, apresentação, apoio) e muda. Os algoritmos e modelos em si são tema de `adp.adapt.adaptive-learning-systems` e `adp.lm.learner-model`; este documento trata do que a adaptação precisa respeitar para ser acessível e preservar a escolha da pessoa.

O que não é: não é proibição de adaptar. O *ability-based design* recomenda interfaces "self-adaptive or user-adaptable" que se ajustem às capacidades, e diz que a adaptação pode "move the burden of conforming from the human user to the system" [F: wobbrock2011ability, Tabela I e §1].

## Problema que resolve

Duas falhas opostas. Sem adaptação, a pessoa precisa se ajustar ao sistema ou configurá-lo, o que é mais difícil justamente para quem mais precisa (ver `acs.adapt.preference-profiles`). Com adaptação opaca, o sistema decide por ela: Horvitz lista como problemas centrais dos agentes de interface "poor guessing about the goals and needs of users", "poor timing of action" e pouca oportunidade de o usuário guiar a invocação dos serviços automáticos e refinar resultados [F: horvitz1999principles, princípios]. Para crianças e pessoas com deficiência, que já têm muitas decisões tomadas por outros, a segunda falha pesa mais; o construto de autodeterminação que fundamenta essa preocupação está em `acs.part.self-determination` [I].

## Fundamentos e funcionamento

### O que a evidência de IHC mostra

Findlater e McGrenere compararam menus estáticos, adaptáveis e adaptativos com 27 participantes. O menu estático foi significativamente mais rápido que o adaptativo; o adaptável foi mais rápido que o adaptativo "under certain conditions"; e a maioria preferiu o adaptável [F: findlater2004comparison, resumo]. No detalhe, 15 participantes escolheram o adaptável como preferido; 55% preferiram o adaptável, 30% o adaptativo e 15% o estático, e os autores sugerem que combinar os dois numa interface de iniciativa mista pode atender melhor uma população variada [F: findlater2004comparison, resultados e conclusões].

Gajos e colegas variaram previsibilidade e acurácia de uma barra adaptativa. A acurácia melhorou desempenho e uso; previsibilidade e acurácia aumentaram a satisfação; e a sensação de estar no controle subiu com ambas. A conclusão relevante aqui: "because predictability and accuracy affect different aspects of users' satisfaction, improvements to one of these factors cannot fully offset the losses to the other" [F: gajos2008predictability, resultados e conclusões].

Esses estudos são com adultos sem deficiência declarada e tarefas de seleção em menus; a transposição para aprendizes com deficiência é inferência [I].

### Princípios de controle

Dos doze princípios de Horvitz para interfaces de iniciativa mista, cinco se aplicam diretamente: considerar a incerteza sobre os objetivos do usuário; agir só quando o benefício esperado supera o custo; usar diálogo para resolver incertezas importantes; permitir "efficient direct invocation and termination" do serviço automático; e reduzir o alcance da ação quando a incerteza é alta, preferindo "doing less" mas corretamente [F: horvitz1999principles, princípios 2, 4, 5, 6 e 8]. O *ability-based design* acrescenta o princípio de transparência: dar ao usuário consciência das adaptações e meios para "inspect, override, discard, revert, store, retrieve, preview, and test" cada uma, o que vale para adaptativas e adaptáveis, para que "all adaptations remain visible and changeable" [F: wobbrock2011ability, Tabela I e §3].

### Onde a adaptação ajuda e onde retira a escolha

Interpretação deste documento a partir das fontes [I]:

- Ajuda quando compensa barreira de acesso estável e mensurável (por exemplo, ampliar alvos para quem erra o apontamento) e a pessoa vê e pode desfazer a mudança [F: wobbrock2011ability, §5, sobre sistemas que medem desempenho de apontamento e redesenham a interface].
- Ajuda quando a pessoa não consegue configurar sozinha e a inferência substitui um formulário inacessível, desde que o resultado vire preferência declarada e editável [I].
- Retira a escolha quando muda o objetivo da atividade (reduz a dificuldade da habilidade-alvo) sem aviso; aí deixa de ser acomodação e vira modificação silenciosa (ver `acs.adapt.accommodation-vs-modification`) [I].
- Retira a escolha quando a pessoa queria o desafio. As diretrizes de jogos pedem que a dificuldade possa mudar "either through settings or adaptive difficulty" [F: gag2026fulllist] e que o jogador possa mudá-la a qualquer momento [F: microsoft2022xag108]; a adaptação automática é uma opção, não um substituto da configuração.

### Preferência declarada como limite da inferência

A arquitetura GPII põe a preferência armazenada como entrada do *matchmaker* [F: vanderheiden2012autopersonalization]; o PNP separa o que deve ser ativado, o que o usuário pode ativar e o que é proibido [F: imsglobal2021afapnp, §4.1.49 a §4.1.51]. Recomendação deste documento [I]: tratar a preferência declarada como restrição que a adaptação inferida não pode violar, e a inferência como sugestão que a pessoa confirma.

## Requisitos e pressupostos

- A pessoa precisa perceber que algo mudou, por um canal que ela acessa (aviso visual e falado, símbolo para usuários de CAA) [I].
- Desfazer e desligar precisam ser operáveis pelo mesmo meio de acesso que a pessoa usa (acionador, olhar) [I].
- Quem decide o grau de automação para uma criança envolve responsável e equipe, mas a voz da criança deve ser ouvida (ver `psg.consent.child-assent`) [I].

## Vantagens e limitações

A adaptação automática reduz o esforço de configuração e pode alcançar quem não sabe o que pedir. Limitações: perda de previsibilidade e da sensação de controle [F: gajos2008predictability]; erros de inferência que a pessoa não consegue corrigir se a interface de correção é inacessível [I]; e confusão entre ajuste de acesso e redução de expectativa [I]. A personalização adaptável, por sua vez, exige esforço e descoberta; os próprios dados de Findlater e McGrenere mostram uma minoria que preferiu a adaptativa [F: findlater2004comparison].

## Alternativas e comparações

| Abordagem | Quem decide | Previsibilidade | Esforço da pessoa | Risco à autonomia |
|---|---|---|---|---|
| Estática acessível | Projetista | Alta | Nenhum | Baixo, mas não se ajusta [I] |
| Adaptável (preferência declarada) | Pessoa ou mediador | Alta | Configurar [F: findlater2004comparison] | Baixo |
| Adaptativa opaca | Sistema | Baixa [F: gajos2008predictability] | Nenhum | Alto [I] |
| Iniciativa mista com transparência | Sistema sugere, pessoa confirma | Média a alta | Confirmar [F: horvitz1999principles] | Baixo a médio [I] |

## Métricas e métodos de avaliação

Os estudos citados medem tempo de tarefa, erros, uso da parte adaptativa e satisfação, inclusive um item de "In Control" [F: gajos2008predictability; findlater2004comparison]. Para aprendizes com deficiência, faltam medidas validadas; indicadores possíveis [I]: proporção de adaptações revertidas pela pessoa, tempo até reverter, frequência com que a pessoa escolhe outro nível do que o sugerido e relato da própria pessoa por meio acessível.

## Exemplo técnico independente de domínio

```
ao detectar(padrao_de_erros):
    sugestao = inferir_ajuste(padrao_de_erros)          # ex.: aumentar alvo, mais tempo
    se sugestao viola perfil.declarado ou sugestao ∈ perfil.proibir: descartar
    se sugestao.afeta(atividade.construto): exigir_confirmacao(pessoa, mediador?)
    senão se confianca(sugestao) < limiar: perguntar(pessoa, canal_acessivel)
    senão: aplicar(sugestao); avisar(pessoa); manter botao_desfazer acessível
    registrar(sugestao, decisao, quem_decidiu)
    se pessoa.reverte(sugestao) repetidamente: parar de sugerir esse tipo
```

## Relações com outros conceitos

Depende de `acs.part.self-determination`, que define o construto de autonomia, e complementa `acs.adapt.preference-profiles`. A transparência e a supervisão humana como requisito de governança estão em `psg.ai.transparency-and-human-oversight`; tornar visível ao aprendiz o que o sistema pensa dele é `adp.lm.open-learner-model`. Os algoritmos estão em `adp.adapt.adaptive-learning-systems` e `gam.diff.dynamic-difficulty-adjustment`.

## Lacunas e questões abertas

- Não se encontrou estudo que compare adaptável x adaptativo com crianças com deficiência ou usuários de acesso alternativo; a evidência citada é com adultos e tarefas de menu.
- O trabalho de Jameson e Schwarzkopf (2002) sobre controlabilidade, citado por Findlater e McGrenere, não foi aberto.
- Como representar no dado de aprendizagem que uma adaptação foi automática, sugerida ou escolhida é questão aberta para `dat.qual.granularity-and-constructs`.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| findlater2004comparison | academico | 2026-10-30 |
| gajos2008predictability | academico | 2026-10-30 |
| horvitz1999principles | academico | 2026-10-30 |
| wobbrock2011ability | academico | 2026-10-30 |
| vanderheiden2012autopersonalization | academico | 2026-10-30 |
| imsglobal2021afapnp | normativo | 2026-10-30 |
| gag2026fulllist | fornecedor | 2026-10-30 |
| microsoft2022xag108 | fornecedor | 2026-10-30 |
