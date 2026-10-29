---
id: iop.fund.mapeamento-e-proveniencia
titulo: Mapeamento entre padrões e preservação de proveniência
tipo: tecnica
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [w3c2009skos, iso2020ts20748, adl2016xapidata, imsglobal2020caliper, dcmi2020terms, imsglobal2017case]
relacoes:
  - { tipo: depende-de, alvo: iop.sem.vocabularios-e-skos }
  - { tipo: complementa, alvo: iop.sem.interoperabilidade-semantica }
  - { tipo: relacionado-a, alvo: iop.lr.comparison }
termos: [crosswalk, perfil de aplicação, mapeamento, proveniência, perda semântica, exactMatch, closeMatch]
---

# Mapeamento entre padrões e proveniência

## Definição e terminologia

**Crosswalk** (ou mapeamento) é a correspondência declarada entre os elementos de dois modelos de dados. **Proveniência** é o registro de onde um dado veio, por qual transformação passou e sob qual autoridade foi afirmado [I].

O SKOS fornece o vocabulário canônico para declarar correspondências entre esquemas de conceitos: `skos:exactMatch` e `skos:closeMatch` para equivalência, `skos:broadMatch`, `skos:narrowMatch` e `skos:relatedMatch` para correspondências hierárquicas e associativas entre esquemas distintos [F: w3c2009skos].

## Problema que resolve

Nenhum sistema vive em um padrão só. Um jogo emite xAPI, a secretaria consome Ed-Fi, o repositório descreve em LOM e a competência está em CASE. Cada travessia entre modelos é uma oportunidade de perder informação de forma silenciosa [I].

## Fundamentos e funcionamento

**Três tipos de perda em um mapeamento** [I]:

1. **Perda de granularidade**: o destino tem menos distinções que a origem. Um evento de jogo com 12 campos vira um `completed` booleano.
2. **Perda de precisão semântica**: `closeMatch` tratado como `exactMatch`. O destino afirma algo mais forte do que a origem autorizava.
3. **Perda de proveniência**: o destino não registra que o dado foi derivado, nem por qual regra, e o resultado passa a ser indistinguível de um dado observado diretamente.

**Mecanismos de preservação disponíveis nos padrões**:

- xAPI: `authority` é definido pelo LRS quando não fornecido ou quando não há relação de confiança forte [F: adl2016xapidata]; `context.extensions` e `object.definition.extensions` permitem carregar o payload original; declarações são tidas como permanentes, e a única forma suportada de desfazer é o *voiding* [F: adl2016xapidata].
- Caliper: o envelope carrega metadados sobre o Sensor emissor [F: imsglobal2020caliper, §1.2]; os identificadores de Event são UUID em forma de URN (`urn:uuid:<UUID>`) [F: imsglobal2020caliper, §2.1], o que dá uma chave estável para rastrear a origem de um registro derivado.
- Dublin Core: `dcterms:source` e as propriedades de relação servem para apontar o recurso de origem; o conjunto `/terms/` tem restrições formais que `/elements/1.1/` não tem — cada termo de `/terms/` é subpropriedade do correspondente em `/elements/1.1/` [F: dcmi2020terms].
- CASE: fornece identificadores únicos referenciáveis para padrões curriculares, pensados para uso em certificados e históricos [F: imsglobal2017case]. É a peça que permite afirmar "este resultado se refere a esta competência" sem copiar o texto da competência.

**Regra prática** [I]: preserve o registro original imutável e trate toda tradução como *view* derivada, com identificador próprio e ponteiro para a origem. Mapeamento destrutivo em tempo de ingestão é irreversível.

## Requisitos e pressupostos

- Os dois modelos têm identificadores estáveis; sem isso, o crosswalk não pode ser declarado, só executado em código.
- O mapeamento é versionado junto com as versões dos dois padrões. Uma correspondência válida entre OneRoster 1.1 e Ed-Fi 3.x não é automaticamente válida para 1.2 e 6.0 [I].

## Vantagens e limitações

Declarar o mapeamento como dado (SKOS, tabela versionada) em vez de embuti-lo em código torna-o auditável e revisável por quem entende o domínio educacional, não só por quem escreve o ETL [I].

Limitação: mapeamentos declarativos cobrem bem correspondência de termos e mal correspondência estrutural (um campo da origem que vira três no destino, com condicional) [I].

## Alternativas e comparações

| Estratégia | Reversível | Custo | Quando usar |
|---|---|---|---|
| Canônico interno + adaptadores | sim, se o canônico for o mais rico | alto no início | muitos padrões de entrada e saída |
| Tradução ponto a ponto | não | baixo por par, quadrático no total | dois ou três sistemas estáveis |
| Armazenar o original e derivar sob demanda | sim | custo de armazenamento | quando a análise futura é desconhecida |

## Métricas e métodos de avaliação

- **Cobertura**: fração dos campos da origem com correspondência declarada.
- **Fidelidade de ida e volta**: fração dos registros que, traduzidos para o destino e de volta, reproduzem o original.
- **Densidade de extensões**: quantos dados viajam em campos de extensão em vez de campos do modelo — indicador de desalinhamento entre o padrão e o caso de uso [I].

## Exemplo técnico independente de domínio

```
origem:  evento rico (12 campos)
         |
         +--> registro canônico imutável (id próprio, authority, timestamp)
                 |
                 +--> view A: statement xAPI   (link: context.extensions.sourceId)
                 +--> view B: linha Ed-Fi      (coluna: source_record_id)

crosswalk declarado:
  campoOrigem:acerto        skos:exactMatch   destino:success
  campoOrigem:tempoResposta skos:closeMatch   destino:duration   # unidade difere
```

## Relações com outros conceitos

Depende de `iop.sem.vocabularios-e-skos` para o vocabulário de correspondências e complementa `iop.sem.interoperabilidade-semantica`. A comparação concreta entre dois modelos de evento está em `iop.lr.comparison`.

## Lacunas e questões abertas

- A ISO/IEC TS 20748-3:2020 traz orientações de mapeamento entre representações de learning analytics, usando xAPI e Caliper como referência [F: iso2020ts20748]; o texto não foi lido e deveria substituir parte das heurísticas acima.
- Falta avaliar o uso de PROV-O (W3C) para registrar proveniência de forma padronizada; não consultado nesta rodada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2009skos | normativo | 2026-10-29 |
| iso2020ts20748 | normativo (metadados) | 2026-10-29 |
| adl2016xapidata | normativo | 2026-10-29 |
| imsglobal2020caliper | normativo | 2026-10-29 |
| dcmi2020terms | normativo | 2026-10-29 |
| imsglobal2017case | normativo | 2026-10-29 |
