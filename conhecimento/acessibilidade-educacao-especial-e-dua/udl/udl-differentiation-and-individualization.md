---
id: acs.udl.udl-differentiation-and-individualization
titulo: DUA, diferenciação pedagógica e adaptação individual
tipo: comparacao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [tomlinson2003differentiating, tomlinson2014differentiated, stanford2009making, grifulfreixenet2020exploring, ok2017udl, us2008heoaudl, cast2024udl30organizer, cast2024faq, cast2024udlgoal, roski2024learning, edyburn2010recognize]
relacoes:
  - { tipo: parte-de, alvo: acs.udl.udl-guidelines }
  - { tipo: relacionado-a, alvo: acs.udl.udl-evidence }
  - { tipo: complementa, alvo: acs.adapt.accommodation-vs-modification }
  - { tipo: complementa, alvo: acs.asmt.pei-and-aee-plans }
  - { tipo: relacionado-a, alvo: acs.adapt.preference-profiles }
  - { tipo: relacionado-a, alvo: acs.adapt.algorithmic-adaptation-and-autonomy }
  - { tipo: relacionado-a, alvo: acs.std.wcag }
  - { tipo: relacionado-a, alvo: adp.adapt.adaptive-learning-systems }
  - { tipo: relacionado-a, alvo: lae.asmt.formative-and-summative }
  - { tipo: complementa, alvo: ped.incl.udl-in-practice }
termos: [diferenciação pedagógica, differentiated instruction, prontidão, interesse, perfil de aprendizagem, retrofit, abordagem proativa, abordagem reativa, adaptação individual, acomodação, plano individual, escolha do aprendiz, adaptação pelo sistema, checklist de acessibilidade]
---

# DUA, diferenciação pedagógica e adaptação individual

## Definição e terminologia

Três abordagens à variabilidade dos aprendizes costumam ser confundidas:

- **DUA (UDL)**: framework de desenho que antecipa a variabilidade e embute opções nos objetivos, métodos, materiais e avaliações, para todos (ver `acs.udl.udl-guidelines`). Ok et al. resumem: "Rather than adapting and/or modifying lessons as they are being administered, UDL focuses on building supports proactively into lesson goals, curriculum resources, instructional practices, and assessments" [F: ok2017udl, p. 116].
- **Diferenciação pedagógica** (*differentiated instruction*, DI): Tomlinson et al. a definem como abordagem em que os professores "proactively modify curricula, teaching methods, resources, learning activities, and student products to address the diverse needs of individual students and small groups of students", em resposta a prontidão (*readiness*), interesse e perfil de aprendizagem [F: tomlinson2003differentiating, p. 121]. A obra de referência é *The Differentiated Classroom* [F: tomlinson2014differentiated, metadados].
- **Adaptação individual**: ajustes para uma pessoa determinada, como acomodações e planos individuais. A definição legal norte-americana de UDL inclui prover "appropriate accommodations" [F: us2008heoaudl, §1003(24)], o que mostra que o DUA não elimina a acomodação individual, apenas reduz a quantidade de casos que dependem dela [I]. Acomodação versus modificação está em `acs.adapt.accommodation-vs-modification`; o plano individual, em `acs.asmt.pei-and-aee-plans`.

**Retrofit** é o nome dado ao ajuste feito depois que o currículo já foi planejado e o aluno não progride: "a reactive rather than a proactive approach" que "forces learners to fit into the existing program" [F: stanford2009making].

## Problema que resolve

Separar as três evita dois erros: tratar o DUA como sinônimo de "ter alternativas" (o que o reduz a checklist) e supor que um desenho universal dispensa a resposta individual. Também responde à pergunta do brief sobre como aplicar o DUA sem que ele vire checklist genérico de acessibilidade [I].

## Fundamentos e funcionamento

### Onde DUA e diferenciação se sobrepõem

A distinção "proativo versus reativo" não separa limpidamente os dois: Tomlinson et al. afirmam que a diferenciação eficaz "is proactive, rather than reactive" e criticam a prática de planejar uma aula para todos e ajustar na hora [F: tomlinson2003differentiating, pp. 131-132]. Listam ainda como características o uso de pequenos grupos flexíveis, materiais variados, ritmo variável e avaliação contínua da compreensão [F: tomlinson2003differentiating, pp. 132-133]. Na prática, o que muda é a unidade de decisão: o DUA desenha opções para a turma antes de conhecer cada aluno; a diferenciação usa informação sobre alunos e grupos concretos (prontidão, interesse, perfil) para ajustar [I].

A revisão sistemática de Griful-Freixenet et al. (27 artigos) encontrou três interpretações da relação na literatura: complementar, mas com um modelo subordinado ao outro; diferenciação incorporada ao DUA, quando entendida como "diferenciar"; e incompatível, posição que, segundo os autores, frequentemente ignora a teoria mais recente [F: grifulfreixenet2020exploring, resumo]. Stanford e Reeves tratam o retrofit como uma forma de diferenciação e o DUA como outra via, planejada desde o início [F: stanford2009making].

### Escolha do aprendiz, decisão do professor, decisão do sistema

| Dimensão | DUA | Diferenciação | Adaptação individual | Adaptação por sistema adaptativo |
|---|---|---|---|---|
| Quando decide | No desenho, antes da aula [F: ok2017udl, p. 116] | No planejamento, com dados da turma [F: tomlinson2003differentiating, p. 121] | Depois de identificar a necessidade de uma pessoa [I] | Durante o uso, por modelo [I] |
| Quem escolhe a opção | Prioriza o aprendiz: "Optimize choice and autonomy" (7.1) [F: cast2024udl30organizer] | Professor, por grupo ou aluno [F: tomlinson2003differentiating, p. 121] | Equipe e família, registrado em plano [I] | Algoritmo [I] |
| Unidade | Turma inteira | Grupos e indivíduos | Indivíduo | Indivíduo |
| Base de informação | Variabilidade previsível | Prontidão, interesse, perfil | Avaliação de barreiras e necessidades | Rastro de interação |
| Meta declarada | Agência do aprendiz [F: cast2024udlgoal] | Maximizar a oportunidade de cada um [F: tomlinson2003differentiating, p. 121] | Acesso equitativo [I] | Eficiência de aprendizagem [I] |

O ponto sensível para ambientes digitais é a coluna "quem escolhe": um sistema que escolhe a representação pelo aprendiz cumpre a letra das opções múltiplas, mas pode contrariar a meta de agência [I; ver `acs.adapt.algorithmic-adaptation-and-autonomy`]. Há evidência descritiva de que, quando podem escolher, os aprendizes mantêm padrões consistentes (por exemplo, vídeo ou texto, tarefa com ou sem ajuda), formando perfis distintos de uso [F: roski2024learning, resumo], o que sugere que preferências declaradas e observadas podem alimentar perfis portáveis (`acs.adapt.preference-profiles`) [H].

### DUA não é checklist de acessibilidade

O CAST afirma que as diretrizes "are not meant to be a prescription or a checklist" e que se deve partir de um objetivo de aprendizagem específico [F: cast2024faq]. Comparação com uma norma de acessibilidade como `acs.std.wcag` [I]:

| Critério | Norma de acessibilidade | DUA |
|---|---|---|
| Objeto | Conteúdo e interface | Objetivo, método, material e avaliação |
| Pergunta | O recurso é perceptível e operável? | O que impede este aprendiz de atingir este objetivo? |
| Resultado | Conformidade verificável | Decisão de desenho justificada |
| Relação | Pré-requisito da consideração 4.2 [F: cast2024udl30organizer] | Vai além: engajamento, linguagem, função executiva |

Práticas que impedem a degeneração em checklist, recomendadas por este documento a partir das fontes [I]: (1) começar pelo objetivo e pelo construto que será avaliado, como recomenda o CAST [F: cast2024faq]; (2) para cada opção, nomear a barreira prevista e a consideração correspondente, como Ok et al. pedem aos pesquisadores [F: ok2017udl, p. 134]; (3) registrar o que foi deliberadamente não usado; (4) verificar se as opções são de fato usadas e por quem; (5) manter um canal de adaptação individual para o que o desenho não previu. A preocupação de Edyburn com um construto que a área "cannot define" é o risco que essas práticas tentam mitigar [F: edyburn2010recognize].

## Vantagens e limitações

DUA reduz o volume de retrofit e não exige diagnóstico para oferecer apoio [I]. Limitações: opções em excesso aumentam a carga de decisão; o DUA não substitui a avaliação de necessidades individuais nem a acomodação que a própria definição legal prevê [F: us2008heoaudl, §1003(24)]. Ok et al. observam que os educadores precisam de habilidades para "modify and adapt the curriculum" e que o tempo de planejamento preocupa os professores [F: ok2017udl, p. 136]. A diferenciação, por sua vez, depende de avaliação contínua, que exige tempo e instrumentos [F: tomlinson2003differentiating, p. 133].

## Exemplo técnico independente de domínio

```
para cada atividade:
    objetivo, construto = definir()
    opcoes = desenhar_opcoes(barreiras_previstas(objetivo))     # DUA: para todos
    para cada grupo em agrupar(dados_formativos):                 # diferenciação
        ajustar(ritmo, material, apoio, grupo)
    para cada aluno com plano_individual:                         # adaptação individual
        aplicar(acomodacoes(aluno))   # sem alterar construto; senão é modificação, registrar
    se sistema_sugere(opcao, aluno):
        mostrar_sugestao(); aluno_decide()                        # preserva agência
    registrar(uso_das_opcoes, desempenho_no_construto)
```

## Relações com outros conceitos

Parte de `acs.udl.udl-guidelines`; a evidência comparativa está em `acs.udl.udl-evidence`. Complementa `acs.adapt.accommodation-vs-modification` e `acs.asmt.pei-and-aee-plans`. A decisão por algoritmo liga-se a `acs.adapt.algorithmic-adaptation-and-autonomy` e `adp.adapt.adaptive-learning-systems`; a avaliação contínua da diferenciação, a `lae.asmt.formative-and-summative`. O uso em sala fica em `ped.incl.udl-in-practice`.

## Lacunas e questões abertas

- O texto integral de Griful-Freixenet et al. (2020) e o livro de Tomlinson (2014) não foram lidos.
- Não foi encontrado estudo empírico que compare diretamente DUA, diferenciação e adaptação individual em resultados de aprendizagem.
- O Plano Nacional de Tecnologia Educacional dos EUA (2024), que segundo fontes secundárias dedica seção ao DUA, não pôde ser aberto; não é citado.
- Falta evidência sobre quando a escolha do aprendiz supera a escolha do sistema, especialmente para crianças com deficiência intelectual.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| tomlinson2003differentiating | academico | 2026-10-30 |
| tomlinson2014differentiated | academico [metadados] | 2026-10-30 |
| stanford2009making | academico (artigo de prática) | 2026-10-30 |
| grifulfreixenet2020exploring | academico (resumo) | 2026-10-30 |
| ok2017udl | academico | 2026-10-30 |
| us2008heoaudl | normativo | 2026-10-30 |
| cast2024udl30organizer | fornecedor | 2026-10-30 |
| cast2024faq | fornecedor | 2026-10-30 |
| cast2024udlgoal | fornecedor | 2026-10-30 |
| roski2024learning | academico (resumo) | 2026-10-30 |
| edyburn2010recognize | academico (trecho inicial) | 2026-10-30 |
