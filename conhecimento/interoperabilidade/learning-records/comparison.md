---
id: iop.lr.comparison
titulo: Comparação entre xAPI, cmi5, Caliper e SCORM
tipo: comparacao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ieee2023xapi, adl2016xapidata, aicc2016cmi5, imsglobal2020caliper, adl2016discovery, iso2020ts20748, scorm2026versions]
relacoes:
  - { tipo: relacionado-a, alvo: iop.lr.xapi }
  - { tipo: relacionado-a, alvo: iop.lr.caliper }
  - { tipo: relacionado-a, alvo: iop.lr.cmi5 }
  - { tipo: relacionado-a, alvo: iop.tool.scorm }
  - { tipo: complementa, alvo: iop.fund.mapeamento-e-proveniencia }
termos: [registro de experiência, telemetria, vocabulário aberto, vocabulário fechado]
---

# Comparação: xAPI, cmi5, Caliper e SCORM

## Definição e terminologia

Os quatro padrões respondem à pergunta "como registro o que o aluno fez?", mas em escopos diferentes: SCORM registra dentro de um conteúdo lançado por LMS; cmi5 faz o mesmo sobre xAPI; xAPI registra qualquer experiência; Caliper registra telemetria de plataforma com vocabulário tipado [I].

## Problema que resolve

Escolher entre eles sem comparação explícita leva a dois erros frequentes [I]: tratar xAPI e Caliper como concorrentes diretos em todo caso de uso, e adotar xAPI sem decidir vocabulário, obtendo dados tecnicamente válidos e analiticamente inúteis.

## Alternativas e comparações

| Dimensão | SCORM | cmi5 | xAPI | Caliper 1.2 |
|---|---|---|---|---|
| Mantenedor | ADL | AICC/cmi5 WG | IEEE LTSC (9274.1.1) [F: ieee2023xapi] | 1EdTech [F: imsglobal2020caliper] |
| Versão de referência | 2004 4th Ed. (2009) [F: scorm2026versions] | Quartz 1st Ed. (2016) [F: aicc2016cmi5] | 2.0 / IEEE 9274.1.1-2023 [F: ieee2023xapi] | 1.2 (2020) [F: imsglobal2020caliper] |
| Vocabulário | fechado (`cmi.*`) | 9 verbos definidos [F: aicc2016cmi5] | aberto (IRI de verbo) [F: adl2016xapidata] | fechado por perfil [F: imsglobal2020caliper, §3] |
| Serialização | XML + API JS | JSON | JSON | JSON-LD [F: imsglobal2020caliper, §4] |
| Transporte | API JavaScript no navegador | REST para LRS | REST para LRS | Sensor → Endpoint HTTP [F: imsglobal2020caliper, §5] |
| Lançamento definido | sim | sim [F: aicc2016cmi5] | não | não |
| Critério de conclusão | sim | `moveOn` [F: aicc2016cmi5] | não | não |
| Funciona fora do navegador | não | sim | sim | sim |
| Identidade | interna ao LMS | Agent xAPI [F: aicc2016cmi5] | IFI [F: adl2016xapidata] | Entity com id |
| Extensibilidade | baixa | média | alta | baixa a média |
| Comparabilidade entre fornecedores | alta (vocabulário único) | alta dentro do perfil | baixa sem perfil acordado | alta dentro do perfil |

A tabela é síntese do autor a partir das fontes citadas em cada célula; células sem citação são interpretação [I].

## Fundamentos e funcionamento

**O eixo real da escolha é vocabulário aberto versus fechado** [I]. xAPI entrega extensibilidade e cobra interoperabilidade semântica: quem emite decide o IRI do verbo, e quem consome precisa conhecer essa decisão. Caliper entrega comparabilidade e cobra cobertura: se a atividade não cabe em um perfil, o modelo não a descreve bem.

Em 2016, ADL e IMS registraram que as duas especificações têm origens distintas e não são equivalentes, que ambas usam uma estrutura de tripla (Actor/Verb/Object no xAPI; Actor/Action/Activity no Caliper), que há diferenças consideráveis na estrutura e no uso das definições de Object e Activity, e que a adoção não deveria ser "one-or-the-other" [F: adl2016discovery]. A mesma fonte indica que, à época, as organizações não haviam acordado alinhamento ou convergência [F: adl2016discovery]. O estado atual dessa relação não foi verificado [H].

**Combinações viáveis** [I]:
- xAPI com perfil próprio documentado, para atividades atípicas, e Caliper para a telemetria de plataforma — dois fluxos, um registro canônico (ver `iop.fund.mapeamento-e-proveniencia`).
- cmi5 quando existe LMS e o conteúdo precisa ser marcado como concluído, mantendo statements *allowed* para a riqueza interna da atividade.
- SCORM apenas quando há exigência de compatibilidade com LMS legado.

## Métricas e métodos de avaliação

Para decidir num caso concreto, medir sobre uma amostra de eventos reais [I]: fração de eventos que cabe em perfil Caliper existente; número de verbos distintos necessários; necessidade de registrar atividade fora do navegador; existência de consumidor externo que já exige um dos formatos.

## Relações com outros conceitos

Agrega `iop.lr.xapi`, `iop.lr.cmi5`, `iop.lr.caliper` e `iop.tool.scorm`. A estratégia de conviver com mais de um padrão está em `iop.fund.mapeamento-e-proveniencia`.

## Lacunas e questões abertas

- A ISO/IEC TS 20748-3:2020 traz regras de mapeamento entre xAPI e Caliper [F: iso2020ts20748]; sem o texto, as recomendações acima são do autor.
- Relação atual entre ADL/IEEE e 1EdTech quanto a convergência: não verificada.
- Não há, nesta rodada, dados de adoção de mercado por padrão; sem isso, a dimensão "ecossistema" fica de fora da tabela.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ieee2023xapi | normativo | 2026-10-29 |
| adl2016xapidata | normativo | 2026-10-29 |
| aicc2016cmi5 | normativo | 2026-10-29 |
| imsglobal2020caliper | normativo | 2026-10-29 |
| adl2016discovery | secundario | 2026-10-29 |
| iso2020ts20748 | normativo (metadados) | 2026-10-29 |
| scorm2026versions | tecnico | 2026-10-29 |
