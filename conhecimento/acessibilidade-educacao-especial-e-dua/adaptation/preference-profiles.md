---
id: acs.adapt.preference-profiles
titulo: Perfis de preferência e personalização por preferência declarada
tipo: conceito
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [imsglobal2021afapnp, imsglobal2012afabestpractice, vanderheiden2012autopersonalization, fluid2026prefsframework, w3c2026mediaqueries5, mdn2026prefersreducedmotion, wobbrock2011ability]
relacoes:
  - { tipo: especificado-por, alvo: acs.std.accessforall-iso-24751 }
  - { tipo: parte-de, alvo: acs.udl.udl-differentiation-and-individualization }
  - { tipo: complementa, alvo: acs.adapt.algorithmic-adaptation-and-autonomy }
  - { tipo: complementa, alvo: acs.adapt.accommodation-vs-modification }
  - { tipo: relacionado-a, alvo: acs.found.disability-models }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: iop.fund.identidade-e-contexto }
termos: [perfil de preferências, necessidades e preferências pessoais, PNP, descrição funcional, personalização por preferência declarada, auto-personalização, matchmaker, enactor, preferência do usuário (media feature), conjunto de ativação, conjunto de proibição, fingerprinting]
---

# Perfis de preferência e personalização por preferência declarada

## Definição e terminologia

Um perfil de preferência é um registro, legível por máquina, de como uma pessoa precisa ou prefere interagir com recursos e interfaces digitais: modalidade de apresentação, ampliação, contraste, legendas, tempo adicional, ferramentas de apoio e assim por diante. A especificação 1EdTech AccessForAll (AfA) 3.0 chama esse registro de *Personal Needs and Preferences* (PNP) e o define como modelo de informação comum para descrever as necessidades e preferências do aprendiz ao acessar recursos ou serviços entregues digitalmente; ele pode ser usado sozinho (por exemplo, para configurar uma interface) ou em par com a *Digital Resource Description* (DRD), que descreve o recurso, para casar recurso e pessoa [F: imsglobal2021afapnp, §1 e §2]. A norma que formaliza esse modelo (ISO/IEC 24751) é tratada em `acs.std.accessforall-iso-24751`; aqui interessa o uso.

Personalização por preferência declarada é o arranjo em que a adaptação parte do que a pessoa (ou alguém por ela) declarou, e não do que o sistema inferiu do comportamento. O contraste com a adaptação inferida é tema de `acs.adapt.algorithmic-adaptation-and-autonomy`.

O que não é: não é um prontuário. O PNP descreve funcionalidade e tecnologia usada, "rather than with the name and other details of a human impairment (a medical approach)"; saber que alguém é cego, diz a especificação, não indica por si que adaptação usar [F: imsglobal2021afapnp, §2.1].

## Problema que resolve

Sem um perfil portável, cada sistema obriga a pessoa a reconfigurar tudo, e quem mais depende da configuração (quem não enxerga o menu de configurações, quem não consegue operar o controle de ampliação) é justamente quem tem mais dificuldade para fazê-la. O artigo que apresenta a *Global Public Inclusive Infrastructure* (GPII) parte da constatação de que "it is not possible to create an interface that is usable by all" e propõe uma abordagem "one-size-fits-one" em que as interfaces se ajustam a partir de necessidades armazenadas "on a token or in the cloud" [F: vanderheiden2012autopersonalization, resumo]. Os autores também criticam o modelo tradicional de tecnologia assistiva por partir de um "user group" (o usuário cego típico) em vez do indivíduo, o que deixa de fora quem não cabe no perfil-padrão [F: vanderheiden2012autopersonalization, introdução].

## Fundamentos e funcionamento

### Conteúdo de um perfil

O modelo PNP do AfA 3.0 (status *IMS Candidate Final*, revisão de 18/01/2021) organiza atributos em grupos: modo de acesso a substituir e tipo de adaptação exigida (`access-mode-required`, `adaptation-type-required`), riscos a evitar (`hazard-avoidance`, como estímulo luminoso intermitente), requisitos de entrada e interoperabilidade com tecnologia assistiva, língua da interface e das adaptações (inclusive língua de sinais), apoios de aprendizagem (linguagem simplificada, encorajamento, `additional-testing-time`), exibição (ampliação, alto contraste, inversão de polaridade, leitura por linha, coluna única), saída em fala, tátil e braile, e ferramentas na tela (calculadora, dicionário, glossário, corretor ortográfico) [F: imsglobal2021afapnp, §4.1]. Três atributos estruturam o comportamento do sistema: o conjunto a ativar na inicialização ("MUST be activated"), o conjunto que o usuário "MAY" ativar durante a atividade e o conjunto que "MUST be prohibited" [F: imsglobal2021afapnp, §4.1.49 a §4.1.51]. O conjunto de proibição é o ponto em que o perfil encontra a questão do construto: uma calculadora que é apoio em ciências pode ser modificação em aritmética (ver `acs.adapt.accommodation-vs-modification`) [I].

### Perfis por contexto

A especificação prevê que "A learner may have one or more defined sets of needs and preferences", porque elas "may vary according to the learning context", e que o usuário deve poder alternar entre conjuntos [F: imsglobal2021afapnp, §2.2 e §2.3]. O guia de boas práticas do AfA 3.0 (rascunho público de 2012) admite que o contexto pode depender de preferências, capacidades do dispositivo e ambiente, mas deixa a modelagem de contexto para depois e não especifica qual adaptação entregar quando várias casam com o perfil [F: imsglobal2012afabestpractice, §2 e §7.1].

### Arquitetura de auto-personalização

A GPII descreve seis funções: captura de necessidades e preferências, armazenamento (nuvem, USB ou outro), identificação da pessoa perante o servidor "but not necessarily to the device", um *matchmaker* que decide as configurações de cada dispositivo, um *settings handler* que as aplica e a interface adaptada [F: vanderheiden2012autopersonalization, seção de componentes]. O primeiro pilar é permitir que as pessoas descubram o que as ajuda e guardem isso "in a common, portable, private, and secure manner" [F: vanderheiden2012autopersonalization, seção de inovação prática]. O projeto europeu Cloud4all desenvolveu e testou partes dessa arquitetura [F: vanderheiden2012autopersonalization].

No nível de componente web, o *Preferences Framework* do Fluid Project separa esquemas (preferências, valores e padrões), painéis (onde o usuário ajusta) e *enactors* (que aplicam a preferência ao conteúdo), e a documentação afirma que o framework "does not prescribe a single means by which content should be delivered to users" [F: fluid2026prefsframework].

### Preferências do sistema operacional e da web

A forma mais difundida de perfil hoje é a configuração de acessibilidade do sistema operacional, exposta à web por *media features* de preferência. O rascunho de Media Queries Level 5 (W3C, *Working Draft* de 19/02/2026) define `prefers-reduced-motion` (`no-preference | reduce`), `prefers-reduced-transparency`, `prefers-contrast` (`no-preference | less | more | custom`), `forced-colors` (`none | active`), `prefers-color-scheme` (`light | dark`) e `prefers-reduced-data` [F: w3c2026mediaqueries5, §12]. A documentação do MDN mapeia `prefers-reduced-motion` para os ajustes de "Reduce motion" ou "Remove animations" em Windows, macOS, iOS, Android e ambientes Linux, e lembra que animações de escala e panorâmica podem desencadear desconforto em pessoas com distúrbios vestibulares [F: mdn2026prefersreducedmotion].

## Requisitos e pressupostos

- Vocabulário comum entre quem declara e quem aplica; sem ele, o perfil não é portável [F: imsglobal2021afapnp, §1].
- Descrição funcional, não diagnóstica [F: imsglobal2021afapnp, §2.1].
- Controle do titular: a especificação pede que o usuário possa "change, expand, replace, or completely remove" seu perfil e levá-lo "to new systems or new situations for reuse" [F: imsglobal2021afapnp, §2.2].
- Um meio de descobrir a preferência: a especificação supõe um assistente interativo ("wizard") [F: imsglobal2021afapnp, §2.2]; a GPII trata a descoberta como componente próprio [F: vanderheiden2012autopersonalization].

## Quem declara o perfil

A especificação AfA não diz quem preenche o formulário [F: imsglobal2021afapnp, §2.2], e o guia de 2012 só observa que o usuário "might not consider themselves disabled" [F: imsglobal2012afabestpractice, §8.2]. Para crianças e para pessoas com deficiência intelectual ou de comunicação, a declaração tende a ser mediada por responsável, professor ou profissional de apoio [I]. Recomendação deste documento [I]: registrar quem declarou cada valor (a própria pessoa, o responsável, a escola), permitir que a pessoa altere o que não for restrição de avaliação, e tratar a voz da criança como em `psg.consent.child-assent`. O princípio de transparência do *ability-based design*, que pede dar ao usuário meios de "inspect, override, discard, revert, store, retrieve, preview, and test" as adaptações, vale também para perfis declarados por terceiros [F: wobbrock2011ability, Tabela I].

## Vantagens e limitações

Vantagens: a pessoa configura uma vez e reaproveita; a decisão fica com ela; a descrição funcional evita rotular. Limitações: o perfil é dado sensível por inferência. O próprio W3C alerta que as *media features* de preferência são risco de *fingerprinting* porque "are correlated with characteristics of the user themselves" e que várias refletem necessidades de acessibilidade; o agente de usuário pode desativá-las para quem pediu proteção contra rastreamento [F: w3c2026mediaqueries5, §17]. Um PNP armazenado em servidor amplia esse risco [I]; ver `psg.access.minimization-and-privacy-by-design`. A especificação AfA consultada não tem seção de privacidade [F: imsglobal2021afapnp] e o guia de 2012 também não trata do tema [F: imsglobal2012afabestpractice]. Por fim, a infraestrutura universal imaginada pela GPII não se tornou padrão de mercado [I].

## Alternativas e comparações

| Mecanismo | Quem declara | Portabilidade | Granularidade | Risco de exposição |
|---|---|---|---|---|
| Configuração do sistema operacional + media features | Usuário no dispositivo | Por dispositivo | Poucas preferências gerais [F: w3c2026mediaqueries5, §12] | *Fingerprinting* [F: w3c2026mediaqueries5, §17] |
| Painel de preferências na aplicação | Usuário na aplicação | Nenhuma fora da aplicação | Alta, local | Baixo se local |
| PNP AfA / ISO 24751 | Usuário, mediador ou assistente | Entre sistemas compatíveis [F: imsglobal2021afapnp, §2.2] | Alta, inclui avaliação | Perfil identificável em servidor [I] |
| Auto-personalização em nuvem (GPII) | Usuário, com ferramenta de descoberta | Entre dispositivos [F: vanderheiden2012autopersonalization] | Alta | Concentração em servidor [I] |

## Exemplo técnico independente de domínio

```
perfil = { titular: id_pseudonimo,
           conjuntos: [ {contexto: "leitura", ampliacao: 2.0, alto_contraste: sim,
                          declarado_por: "titular"},
                        {contexto: "avaliacao", tempo_adicional: 1.5, leitura_em_voz: sim,
                          proibir: [calculadora], declarado_por: "equipe_escolar"} ] }
ao iniciar(atividade):
    c = escolher_conjunto(perfil, atividade.contexto)    # pessoa pode trocar
    aplicar(c.ativar_na_inicializacao); oferecer(c.ativar_como_opcao)
    bloquear(c.proibir ∩ atividade.restricoes_de_construto)
    combinar com media features do dispositivo (prefers-reduced-motion etc.)
```

## Relações com outros conceitos

Especificado por `acs.std.accessforall-iso-24751`. Parte da individualização tratada em `acs.udl.udl-differentiation-and-individualization`. Complementa `acs.adapt.algorithmic-adaptation-and-autonomy` (preferência declarada x inferida) e `acs.adapt.accommodation-vs-modification` (o que o conjunto de proibição deve conter). A descrição funcional ecoa `acs.found.disability-models`. Privacidade em `psg.access.minimization-and-privacy-by-design`; identidade portável em `iop.fund.identidade-e-contexto`.

## Lacunas e questões abertas

- O status final do PNP 3.0 não foi confirmado: a página consultada diz *Candidate Final* (2021) e não se localizou versão *Final*.
- Não se encontrou avaliação empírica recente da GPII ou do Cloud4all além do artigo de 2012; resultados de uso real ficam sem verificação.
- A documentação atual do UI Options do Fluid (lista de preferências e versão) não abriu; só a página geral do framework foi lida.
- Falta orientação publicada sobre quem declara o perfil de criança com deficiência e como conciliar a voz dela com restrições de avaliação.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2021afapnp | normativo (especificação de consórcio, Candidate Final) | 2026-10-30 |
| imsglobal2012afabestpractice | normativo (rascunho público, guia) | 2026-10-30 |
| vanderheiden2012autopersonalization | academico | 2026-10-30 |
| fluid2026prefsframework | fornecedor (documentação de projeto aberto) | 2026-10-30 |
| w3c2026mediaqueries5 | normativo (Working Draft) | 2026-10-30 |
| mdn2026prefersreducedmotion | fornecedor (documentação de referência) | 2026-10-30 |
| wobbrock2011ability | academico | 2026-10-30 |
