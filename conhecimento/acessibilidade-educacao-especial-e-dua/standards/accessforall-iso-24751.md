---
id: acs.std.accessforall-iso-24751
titulo: ISO/IEC 24751 e 1EdTech AccessForAll
tipo: padrao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [iso2475112008, iso2475122008, iso2475132008, iso2475142023, imsglobal2021afapnp, imsglobal2012afabestpractice, edtech2026accessibility]
relacoes:
  - { tipo: parte-de, alvo: acs.std.comparison }
  - { tipo: complementa, alvo: acs.adapt.preference-profiles }
  - { tipo: complementa, alvo: acs.std.wcag }
  - { tipo: relacionado-a, alvo: acs.found.disability-models }
  - { tipo: relacionado-a, alvo: adp.lm.learner-model }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
  - { tipo: relacionado-a, alvo: iop.fund.conformidade-e-certificacao }
termos: [AccessForAll, AfA, ISO/IEC 24751, necessidades e preferências pessoais, PNP, descrição de recurso digital, DRD, modo de acesso, adaptação, adaptação parcial, adaptação total, correspondência perfil-recurso, abordagem funcional]
---

# ISO/IEC 24751 e 1EdTech AccessForAll

## Definição e terminologia

AccessForAll (AfA) é uma abordagem de acessibilidade por correspondência: descreve-se o que a pessoa precisa e prefere, descreve-se o que cada recurso oferece, e o sistema entrega a combinação adequada. Existe em duas linhagens:

- **ISO/IEC 24751**, "Individualized adaptability and accessibility in e-learning, education and training", do JTC 1/SC 36. A parte 1 (2008) é o arcabouço e modelo de referência; a parte 2 (2008), "Access for all" personal needs and preferences for digital delivery; a parte 3 (2008), "Access for all" digital resource description; as três estão em vigor, confirmadas em revisão de 2026 [F: iso2475112008, metadados; iso2475122008, metadados; iso2475132008, metadados]. Não existe ISO/IEC 24751-1:2023: a edição de 2023 é a parte 4, que especifica um serviço de registro de conceitos AfA, um formato JSON para trocar entradas e operações REST, e substitui a ISO/IEC TS 24751-4:2019 [F: iso2475142023, metadados].
- **1EdTech (antiga IMS Global) AccessForAll**, cuja versão 2.0 (2009) é a última marcada como Final; a 3.0 está como Public Draft desde 2012, e o modelo de informação PNP 3.0 tem o rótulo "Public Draft 2" atualizado em 18/01/2021 na lista de especificações [F: edtech2026accessibility]; a página do próprio documento o marca "IMS Candidate Final" com a mesma data [F: imsglobal2021afapnp]. A divergência de rótulo é registrada aqui sem resolução.

Pelo resumo de catálogo, a ISO/IEC 24751-2 toma como especificação de referência o IMS Accessibility for LIP, e a 24751-3 se baseia no IMS AccessForAll Meta-data v1 [F: iso2475122008, metadados; iso2475132008, metadados].

O que não é: não é diagnóstico nem registro de deficiência; não é norma de conformidade de conteúdo (isso é WCAG); e não é, por si, um algoritmo adaptativo.

## Problema que resolve

Conteúdo conforme à WCAG ainda pode não servir a uma pessoa concreta: quem lê braile precisa de outra coisa que quem usa ampliação, e as duas podem ser cegas. O PNP 3.0 diz que trata de habilidades funcionais "rather than with the name and other details of a human impairment (a medical approach)" e que saber que alguém é cego não diz se lê braile ou usa leitor de tela [F: imsglobal2021afapnp, §2.1]. O objetivo declarado da ISO/IEC 24751-1 é parear cada aprendiz com ferramentas de interface e recursos adequados, servindo a pessoas com deficiência e a quem está em contexto incapacitante [F: iso2475112008, metadados].

## Fundamentos e funcionamento

### Lado da pessoa: PNP

O PNP é uma linguagem comum e legível por máquina para descrever como o aprendiz prefere interagir com recursos digitais, incluindo a configuração de tecnologias assistivas; pode ser usado sozinho (configurar a interface) ou com o DRD (escolher recursos) [F: imsglobal2021afapnp]. Grupos de preferências do PNP 3.0 [F: imsglobal2021afapnp]:

| Grupo | Exemplos |
|---|---|
| Exibição | alto contraste, ampliação, inversão, aparência do texto, coluna única, régua de leitura |
| Saída alternativa | texto em fala, dispositivos táteis e braile |
| Controle e entrada | controle completo por teclado, mascaramento de respostas |
| Conteúdo e língua | linguagem simplificada, tradução, língua de sinais, legendas, transcrição, audiodescrição, texto alternativo |
| Apoio educacional e testagem | tempo adicional, encorajamento, ferramentas na tela (calculadora, glossário, dicionário), complexidade |
| Segurança e ambiente | evitar riscos (ex.: imagens piscantes), pausas |

A ISO/IEC 24751-2 cobre, pelo resumo, os grupos de necessidades e preferências, o ordenamento de prioridades e a conformidade de aplicações de entrega e de sistemas de acesso alternativo [F: iso2475122008, metadados].

### Lado do recurso: DRD

O DRD descreve o recurso com vocabulário compartilhado: modos de acesso, distinção entre recurso original e adaptado, adaptabilidade [F: iso2475132008, metadados]. O guia de boas práticas do AfA 3.0 descreve a correspondência: compara o `accessMode` do recurso (ex.: visual) com o `accessModeRequired` da pessoa (ex.: textual); procura adaptações por `hasAdaptation` no original ou por registros que declaram `isAdaptationOf`; infere modos a partir de `adaptationType`; e distingue adaptações parciais, que só complementam ("a partial adaption cannot be substituted for the original"), das totais, que substituem [F: imsglobal2012afabestpractice]. Sem adaptação disponível, o sistema pode recorrer a transformação automática ou serviço humano [F: imsglobal2012afabestpractice].

## Requisitos e pressupostos

- Recursos com metadados de acessibilidade confiáveis; sem DRD, não há correspondência [I].
- Alguém declara o perfil. O guia prevê editores e assistentes de preferência, mas não descreve configuração assistida por terceiros e lembra que a pessoa pode não se considerar com deficiência [F: imsglobal2012afabestpractice]. Quem declara, e com que autonomia, é tema de `acs.adapt.preference-profiles`.
- O contexto (dispositivo, ambiente) altera preferências, mas a modelagem de contexto foi adiada no AfA 3.0 [F: imsglobal2012afabestpractice].

## Vantagens e limitações

Vantagens: separa necessidade funcional de diagnóstico, o que alinha o padrão aos modelos não médicos de deficiência (`acs.found.disability-models`) e reduz dado sensível [I, a partir de imsglobal2021afapnp]; cobre preferências cognitivas e de apoio (linguagem simplificada, tempo, encorajamento) que a WCAG não alcança [F: imsglobal2021afapnp].

Limitações: a linha 1EdTech nunca finalizou a 3.0 [F: edtech2026accessibility]; o texto ISO é pago e não foi lido; não se localizou nesta sessão evidência de adoção ampla. Um perfil de preferências é, ainda assim, dado pessoal que pode revelar deficiência; a minimização (`psg.access.minimization-and-privacy-by-design`) se aplica [I].

## Alternativas e comparações

| Opção | Escopo | Status |
|---|---|---|
| ISO/IEC 24751-1 a 3 (2008) | arcabouço, PNP, DRD | em vigor, confirmadas em 2026 [metadados] |
| ISO/IEC 24751-4 (2023) | registro de conceitos AfA e API | em vigor [metadados] |
| 1EdTech AfA 2.0 (2009) | PNP e DRD | Final |
| 1EdTech AfA 3.0 / PNP 3.0 | PNP e DRD revistos | rascunho; rótulo divergente |
| Preferências do sistema operacional | exibição, fala, entrada | não portável entre sistemas [I] |

## Exemplo técnico independente de domínio

```
pnp  = { accessModeRequired: [{existing: visual, adaptationRequest: textual}],
         extraTime: 1.5, hazardAvoidance: [flashing], language: "pt-BR" }
drd(recurso R) = { accessMode: [visual], hasAdaptation: [R_alt] }
drd(R_alt)     = { accessMode: [textual], adaptationType: alternativeText, isAdaptationOf: R }
entregar(R, pnp):
    se R.accessMode satisfaz pnp: entregar R
    senão A = buscar_adaptacao(R, pnp)       # hasAdaptation ou isAdaptationOf
          se A.parcial: entregar R + A senão: entregar A
          se nada: transformacao_automatica(R) ou pedido_a_servico_humano(R)
```

## Relações com outros conceitos

Complementa `acs.adapt.preference-profiles` (quem declara e como) e `acs.std.wcag` (conformidade do conteúdo, base sobre a qual a adaptação opera). Relaciona-se com `adp.lm.learner-model`, onde um perfil de acesso pode viver ao lado do modelo do aprendiz, e com `iop.fund.conformidade-e-certificacao`.

## Lacunas e questões abertas

- Texto das partes 1 a 4 da ISO/IEC 24751 não acessado (pago); conteúdo descrito só pelos resumos de catálogo.
- Divergência entre "Public Draft 2" e "Candidate Final" para o PNP 3.0 não resolvida.
- Não se verificou relação formal entre AfA 3.0 e as propriedades de acessibilidade de outros vocabulários de metadados.
- Sem evidência empírica localizada sobre ganhos de aprendizagem com correspondência AfA.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| iso2475112008 | normativo [metadados] | 2026-10-30 |
| iso2475122008 | normativo [metadados] | 2026-10-30 |
| iso2475132008 | normativo [metadados] | 2026-10-30 |
| iso2475142023 | normativo [metadados] | 2026-10-30 |
| imsglobal2021afapnp | normativo (especificação de consórcio) | 2026-10-30 |
| imsglobal2012afabestpractice | normativo (rascunho público) | 2026-10-30 |
| edtech2026accessibility | normativo (página de status) | 2026-10-30 |
