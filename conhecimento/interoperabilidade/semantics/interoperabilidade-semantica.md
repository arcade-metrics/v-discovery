---
id: iop.sem.interoperabilidade-semantica
titulo: Interoperabilidade semântica em sistemas educacionais
tipo: conceito
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ec2026nifo, w3c2009skos, adl2016xapidata, imsglobal2020caliper, imsglobal2017case, nces2026ceds, iso2020ts20748]
relacoes:
  - { tipo: parte-de, alvo: iop.fund.niveis-de-interoperabilidade }
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: complementa, alvo: iop.fund.mapeamento-e-proveniencia }
termos: [semântica, vocabulário, perfil de aplicação, significado, comparabilidade]
---

# Interoperabilidade semântica

## Definição e terminologia

Interoperabilidade semântica é a propriedade de dois sistemas atribuírem o mesmo significado aos dados que trocam. É uma das camadas do framework europeu de interoperabilidade, ao lado da jurídica, da organizacional e da técnica [F: ec2026nifo].

Distinção operacional [I]: a camada técnica responde "a mensagem chegou e foi aceita?"; a semântica responde "o que o receptor fez com ela corresponde ao que o emissor quis dizer?".

## Problema que resolve

É possível passar em toda a suíte de conformidade de um padrão e produzir dados inúteis. O exemplo canônico neste domínio [I]: dois sistemas emitem statements xAPI válidos; um usa o verbo `completed` para "chegou ao fim da atividade" e o outro para "atingiu o critério de domínio". O consumidor soma os dois e produz um indicador sem significado.

## Fundamentos e funcionamento

**Onde cada padrão deixa a semântica em aberto** [I]:

| Padrão | O que fica aberto | Mecanismo de fechamento |
|---|---|---|
| xAPI | IRI do verbo e da atividade; `extensions` | perfis xAPI; o `display` do verbo não deve ser usado para inferir significado [F: adl2016xapidata] |
| Caliper | menos aberto: vocabulário por perfil [F: imsglobal2020caliper, §3] | escolher o perfil correto; `General` como escape |
| LTI | vocabulário de papéis | mapeamento dos papéis locais |
| OneRoster, Ed-Fi | definição de cada campo | CEDS como dicionário comum [F: nces2026ceds] |
| LOM, Dublin Core, LRMI | valores dos campos educacionais | vocabulários SKOS |
| Avaliação (QTI) | o que o item mede | alinhamento a competências via CASE [F: imsglobal2017case] |

**Três instrumentos de fechamento semântico** [I]:

1. **Perfil de aplicação**: documento que fixa, para uma comunidade, quais campos são obrigatórios e quais valores são válidos. É o instrumento mais barato e o mais negligenciado.
2. **Vocabulário publicado com identificadores**: SKOS, com `prefLabel` multilíngue e mapeamentos explícitos [F: w3c2009skos].
3. **Referência a autoridade externa**: em vez de definir o significado, apontar para quem o define — identificadores CASE para competências [F: imsglobal2017case], CEDS para elementos de dado [F: nces2026ceds].

**Por que a camada semântica falha na prática** [I]: ela não tem dono. Conformidade técnica tem suíte de teste; semântica exige acordo entre pessoas que entendem de educação, em um artefato que ninguém é obrigado a produzir.

## Requisitos e pressupostos

- Existe um perfil de aplicação escrito e versionado antes da primeira integração em produção.
- Cada campo com valor livre tem um vocabulário designado ou uma justificativa explícita para ser livre.

## Vantagens e limitações

Fechar a semântica custa flexibilidade: um perfil restritivo rejeita casos de uso não previstos. A posição defensável é fechar o núcleo (o que será agregado e comparado) e deixar aberta a periferia (o que será analisado caso a caso), com marcação explícita da fronteira [I].

## Métricas e métodos de avaliação

- Número de termos distintos usados para a mesma ação semântica entre emissores.
- Proporção de dados que trafegam em campos de extensão.
- Teste de concordância: duas equipes classificam a mesma amostra de eventos com o perfil em mãos; a divergência mede a ambiguidade do perfil [I].

## Relações com outros conceitos

É a camada semântica de `iop.fund.niveis-de-interoperabilidade`; depende de `iop.sem.vocabularios-e-skos` e complementa `iop.fund.mapeamento-e-proveniencia`.

## Lacunas e questões abertas

- A ISO/IEC TS 20748-3:2020 é a referência normativa mais direta sobre mapeamento semântico entre representações de learning analytics [F: iso2020ts20748] e não foi lida.
- Não há, nesta base, um perfil de aplicação de exemplo; seria o próximo artefato útil.
- Falta literatura acadêmica sobre falhas semânticas documentadas em integrações educacionais reais; a busca desta rodada não cobriu bases acadêmicas.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ec2026nifo | normativo | 2026-10-29 |
| w3c2009skos | normativo | 2026-10-29 |
| adl2016xapidata | normativo | 2026-10-29 |
| imsglobal2020caliper | normativo | 2026-10-29 |
| imsglobal2017case | normativo | 2026-10-29 |
| nces2026ceds | fornecedor | 2026-10-29 |
| iso2020ts20748 | normativo (metadados) | 2026-10-29 |
