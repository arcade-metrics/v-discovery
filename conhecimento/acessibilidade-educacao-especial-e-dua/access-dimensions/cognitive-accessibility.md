---
id: acs.dim.cognitive-accessibility
titulo: Acessibilidade cognitiva e de aprendizagem
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2024wcag22, w3c2021cogausable, lei152632025, iso2449512023, abnt2024nbriso244951, inclusioneurope2010infoforall, wilson2026easyread, gameaccessibility2026fulllist]
relacoes:
  - { tipo: especificado-por, alvo: acs.std.wcag }
  - { tipo: complementa, alvo: acs.dim.visual }
  - { tipo: complementa, alvo: acs.at.aac }
  - { tipo: complementa, alvo: acs.adapt.preference-profiles }
  - { tipo: relacionado-a, alvo: acs.adapt.accommodation-vs-modification }
  - { tipo: avaliado-por, alvo: acs.asmt.user-testing-with-at }
  - { tipo: relacionado-a, alvo: acs.std.game-accessibility-guidelines }
  - { tipo: relacionado-a, alvo: acs.br.lbi }
  - { tipo: relacionado-a, alvo: psg.consent.child-assent }
  - { tipo: relacionado-a, alvo: ped.incl.evidence-based-practices-by-population }
termos: [acessibilidade cognitiva, deficiência cognitiva e de aprendizagem, COGA, padrão de desenho, linguagem simples, leitura fácil, Easy Read, nível de leitura, teste de função cognitiva, simplificação, sobrecarga cognitiva, coprodução]
---

# Acessibilidade cognitiva e de aprendizagem

## Definição e terminologia

Acessibilidade cognitiva é a remoção de barreiras de conteúdo e interação que afetam pessoas com deficiências cognitivas e de aprendizagem. O documento de referência do W3C, *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA, Working Group Note de 29/04/2021), descreve essas deficiências como dificuldades "relating to cognitive functions", com efeito sobre aprendizagem, comunicação, leitura, escrita ou matemática, processamento de informação nova ou complexa, "memory and attention or visual, language, or numerical thinking" [F: w3c2021cogausable, §2.2]. O escopo inclui deficiência intelectual, transtornos específicos de aprendizagem, neurodiversidade e perdas adquiridas, como demência e lesão cerebral [F: w3c2021cogausable, resumo e §6].

Três famílias de resposta se sobrepõem e convém não confundir [I]:
- **Padrões de desenho cognitivo** (COGA): regras de interface, navegação, erro, memória e ajuda.
- **Linguagem simples** (*plain language*): técnica de redação para o público em geral, normalizada na ISO 24495-1:2023 e, no Brasil, na Lei 15.263/2025.
- **Leitura fácil** (*easy-to-read*, *Easy Read*): adaptação mais intensa, desenhada para pessoas com deficiência intelectual e verificada por elas [F: inclusioneurope2010infoforall, p. 5 e 9].

O que não é: não é uma camada de WCAG nem requisito de conformidade. O próprio COGA diz: "Following this guidance is not required for conformance to WCAG" [F: w3c2021cogausable, §2].

## Problema que resolve: onde WCAG não cobre

O WCAG 2.2 admite o limite no próprio texto. Segundo o resumo, seguir a norma traz "some accommodation for learning disabilities and cognitive limitations; but will not address every user need" [F: w3c2024wcag22, resumo]. A introdução registra "significant challenges" para definir critérios cognitivos, por causa do prazo e da dificuldade de consenso sobre "testability, implementability, and international considerations" [F: w3c2024wcag22, Background on WCAG 2]. A seção de conformidade avisa que mesmo o nível AAA não basta, "particularly in the cognitive, language, and learning areas", e indica o COGA como guia complementar [F: w3c2024wcag22, WCAG 2 Layers of Guidance].

Os critérios que tocam cognição existem, mas quase todos ficam no nível AAA. A própria norma diz que "It is not recommended that Level AAA conformance be required as a general policy for entire sites" [F: w3c2024wcag22, 5.2.1, nota 2]. Exemplos: 3.1.3 Unusual Words, 3.1.4 Abbreviations, 3.1.5 Reading Level (versão mais simples quando o texto exige leitura acima do "lower secondary education level"), 2.2.3 No Timing e 2.2.6 Timeouts [F: w3c2024wcag22, critérios citados]. Nos níveis A e AA, a versão 2.2 acrescentou 3.2.6 Consistent Help, 3.3.7 Redundant Entry e 3.3.8 Accessible Authentication (Minimum). Este último proíbe exigir "a cognitive function test (such as remembering a password or solving a puzzle)" sem alternativa [F: w3c2024wcag22, 3.2.6, 3.3.7, 3.3.8]. A estrutura e os níveis da norma ficam em `acs.std.wcag`.

Assim, as lacunas típicas que WCAG A/AA não fecha são [I, a partir das fontes acima]: vocabulário e sintaxe do texto, quantidade de conteúdo por tela, metáforas e ícones abstratos, dependência de memória entre passos, tempo para ler e decidir e ajuda humana. O COGA trata o assunto como guia de processo, com objetivos, padrões, personas e testes com usuários. A linguagem simples e a leitura fácil tratam o texto.

## Fundamentos e funcionamento

### COGA: oito objetivos e padrões

O COGA organiza a orientação em oito objetivos, cada um com histórias de usuário, padrões de desenho, personas e perguntas de teste [F: w3c2021cogausable, §2.1 e §4]:

| Objetivo | Exemplos de padrões |
|---|---|
| 1. Ajudar a entender o que as coisas são e como usá-las | 4.2.2 hierarquia e desenho familiares; 4.2.7 ícones que ajudam |
| 2. Ajudar a encontrar o que se precisa | 4.3.5 dividir mídia em partes; 4.3.6 oferecer busca |
| 3. Usar conteúdo claro e compreensível | 4.4.1 palavras claras; 4.4.4 linguagem literal; 4.4.13 alternativas para conceitos numéricos |
| 4. Ajudar a evitar erros e saber corrigi-los | 4.5.1 nada se move inesperadamente; 4.5.9 evitar perda de dados e *timeouts*; 4.5.10 dar retorno |
| 5. Ajudar a manter o foco | 4.6.1 limitar interrupções; 4.6.3 evitar excesso de conteúdo |
| 6. Não depender de memória | 4.7.1 login que não depende de memória; 4.7.5 não exigir cálculo nem memorização |
| 7. Oferecer ajuda e suporte | 4.8.1 ajuda humana; 4.8.7 lembretes |
| 8. Permitir adaptação e personalização | 4.9.1 controle sobre o que se move; 4.9.3 permitir simplificação |

Alguns padrões trazem parâmetros concretos. O 4.4.1 manda usar palavras comuns e diz: "Look at the most common 1500 words or phrases". Termos novos devem ter explicação "within one click or event" [F: w3c2021cogausable, 4.4.1.2]. O 4.9.3 observa que "Typically, a simple application has 3 to 6 functions" e manda manter fácil o retorno à versão completa [F: w3c2021cogausable, 4.9.3.4]. O 4.5.9 manda evitar limites de tempo e permitir salvar o trabalho aos poucos. Quando o limite for inevitável, o usuário deve saber no início quanto tempo terá e se perderá dados [F: w3c2021cogausable, 4.5.9.2].

Para verificar um padrão, o COGA usa os exemplos "use" e "avoid": o padrão está "probably applied" se um exemplo "use" foi implementado e os "avoid" foram evitados. Declarações testáveis estão em desenvolvimento e cobrem só parte dos padrões [F: w3c2021cogausable, §2.1.1].

### Linguagem simples

A ISO 24495-1:2023 (1.ª edição, ISO/TC 37, 14 páginas) "establishes governing principles and guidelines for developing plain language documents". Ela se aplica "only to printed or digital information that is primarily in the form of text" [F: iso2449512023, resumo do catálogo]. A ABNT adotou o texto como ABNT NBR ISO 24495-1:2024, *Linguagem Simples, Parte 1: Princípios e diretrizes norteadores* [F: abnt2024nbriso244951, metadados]. O texto integral das duas normas não foi aberto, então os princípios não são reproduzidos aqui.

No Brasil, a Lei 15.263, de 14/11/2025, institui a Política Nacional de Linguagem Simples para órgãos e entidades da administração pública de todos os Poderes e entes [F: lei152632025, art. 1]. A lei define linguagem simples como "o conjunto de técnicas destinadas à transmissão clara e objetiva de informações" [F: lei152632025, art. 4]. Um dos objetivos é "facilitar a compreensão da comunicação pública pelas pessoas com deficiência" [F: lei152632025, art. 2, VII]. O art. 5 lista dezoito técnicas, entre elas frases curtas e em ordem direta, uma ideia por parágrafo, palavras comuns, sigla precedida do nome completo, informação mais importante primeiro, voz ativa, "linguagem acessível à pessoa com deficiência" e "testar com o público-alvo se a mensagem está compreensível" [F: lei152632025, art. 5, I a XVIII]. A lei obriga o poder público. Para uma plataforma educacional privada, ela é referência técnica e não obrigação [I].

### Leitura fácil

Os padrões europeus *Information for all*, de Inclusion Europe, foram criados em 2010 no projeto *Pathways* [F: inclusioneurope2010infoforall, página do editor]. Eles cobrem informação escrita, eletrônica, em vídeo e em áudio [F: inclusioneurope2010infoforall, sumário]. Regras típicas:
- envolver pessoas com deficiência intelectual na produção e na verificação ("Always involve people with intellectual disabilities") [F: inclusioneurope2010infoforall, regra geral 5];
- evitar metáforas, siglas, porcentagens e números grandes [F: inclusioneurope2010infoforall, regras 10, 12 e 13];
- começar cada frase em nova linha e não quebrar palavras entre linhas [F: inclusioneurope2010infoforall, seção 2, regras 17 e 18];
- em sites, pedir a pessoas com deficiência intelectual que testem o site e evitar pop-ups [F: inclusioneurope2010infoforall, seção 3, regras 1 e 4].

O documento observa que as diretrizes do WAI "are not easy to read" e define as suas como específicas para deficiência intelectual [F: inclusioneurope2010infoforall, seção 3].

## Requisitos e pressupostos

- Conformidade WCAG como piso: o COGA lembra que pessoas com deficiência cognitiva podem ter também deficiências motoras ou visuais e manda sempre seguir o WCAG [F: w3c2021cogausable, §2].
- Participação do público na concepção e no teste, presente nos três referenciais [F: w3c2021cogausable, §5; lei152632025, art. 5, XVIII; inclusioneurope2010infoforall, regra geral 5].
- Escolha consciente do nível de adaptação. Linguagem simples serve ao público geral. Leitura fácil é um produto à parte, com versão própria e ligação clara a partir da página principal [F: inclusioneurope2010infoforall, seção 3].

## Vantagens e limitações

Vantagens: os padrões COGA descrevem barreiras que o WCAG deixou de fora e vêm com personas e roteiros de teste. Linguagem simples tem agora base legal no Brasil e norma técnica adotada pela ABNT. Limitações:
- O COGA não é normativo e ainda não tem testes completos [F: w3c2021cogausable, §2.1.1].
- A evidência de eficácia da leitura fácil é fraca. A revisão de 29 estudos em saúde encontrou variação na produção e no controle de qualidade e evidência empírica "limited". A conclusão é que essa base "largely consists of low-quality research" [F: wilson2026easyread, resumo].
- Simplificar conteúdo de avaliação pode mudar o que se mede. Essa fronteira é tratada em `acs.adapt.accommodation-vs-modification` [I].
- Os padrões de Inclusion Europe proíbem fontes serifadas e textos muito juntos sem citar estudo de legibilidade [F: inclusioneurope2010infoforall, seção 2]. Trate-os como consenso de praticantes [I].

## Alternativas e comparações

| Critério | WCAG 2.2 A/AA | COGA | Linguagem simples (ISO 24495-1, Lei 15.263) | Leitura fácil (Inclusion Europe) |
|---|---|---|---|---|
| Natureza | Norma, conformidade testável | Nota do W3C, guia complementar | Norma técnica; lei para o setor público | Padrão de organização da sociedade civil |
| Público | Todas as deficiências | Deficiências cognitivas e de aprendizagem | Público geral, incluindo pessoas com deficiência | Pessoas com deficiência intelectual |
| Objeto | Conteúdo e interface web | Interface, processo, texto, ajuda | Texto | Texto, site, vídeo, áudio |
| Verificação | Critérios de sucesso | Exemplos "use"/"avoid"; teste com usuários | Teste com o público-alvo (Lei, art. 5, XVIII) | Verificação por pessoas com deficiência intelectual |

## Exemplo técnico independente de domínio

```
revisar_tela(tela):
    exigir conformidade WCAG A/AA                 # piso (acs.std.wcag)
    para cada rótulo, instrução, mensagem de erro:   # COGA 4.4.1 "Getting Started"
        trocar termo raro por palavra comum ou explicar em 1 toque
    se tela tem limite de tempo: remover, ou avisar no início e salvar progresso   # 4.5.9
    se fluxo exige lembrar dado de passo anterior: preencher ou permitir selecionar  # 3.3.7 / 4.7.5
    oferecer modo simplificado (3 a 6 funções) com volta fácil ao completo   # 4.9.3
    texto longo: resumo no topo; versão em leitura fácil como recurso separado
    testar com pessoas do público, registrando onde travam
```

## Relações com outros conceitos

É especificado em parte por `acs.std.wcag` (critérios cognitivos e limites da norma). Complementa `acs.dim.visual`, porque espaçamento, contraste e redimensionamento também servem à leitura. Complementa `acs.at.aac`, porque símbolos e pictogramas são o meio de quem não lê texto. Complementa `acs.adapt.preference-profiles`, que guarda a escolha de modo simplificado. A avaliação passa por `acs.asmt.user-testing-with-at`. Relaciona-se com `acs.adapt.accommodation-vs-modification`, com `acs.std.game-accessibility-guidelines` (categoria cognitiva: progredir em textos no próprio ritmo e praticar sem falhar [F: gameaccessibility2026fulllist]), com `acs.br.lbi`, com `psg.consent.child-assent` (termos em leitura fácil) e com `ped.incl.evidence-based-practices-by-population`.

## Lacunas e questões abertas

- O texto integral da ISO 24495-1 e da NBR ISO 24495-1 não foi aberto. O catálogo de um revendedor mostra a NBR como "Vigente" e também como "cancelada", e o status deve ser confirmado na ABNT.
- O documento COGA tem a data de 2021. Não foi verificado se as declarações testáveis (*Testable Statements*) já cobrem todos os padrões.
- Não se localizou padrão brasileiro de leitura fácil equivalente ao de Inclusion Europe, nem estudo que compare linguagem simples e leitura fácil com crianças.
- Não há métrica validada de "nível de leitura" para o português que corresponda ao critério 3.1.5. Fórmulas de legibilidade em inglês não se transferem sem validação [H].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2024wcag22 | normativo | 2026-10-30 |
| w3c2021cogausable | normativo (Working Group Note, não normativa para conformidade) | 2026-10-30 |
| lei152632025 | normativo | 2026-10-30 |
| iso2449512023 | normativo (resumo do catálogo; texto integral não acessado) | 2026-10-30 |
| abnt2024nbriso244951 | normativo [metadados] | 2026-10-30 |
| inclusioneurope2010infoforall | tecnico | 2026-10-30 |
| wilson2026easyread | academico | 2026-10-30 |
| gameaccessibility2026fulllist | tecnico | 2026-10-30 |
