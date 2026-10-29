---
id: iop.health.fhir
titulo: HL7 FHIR R5
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [hl72023fhir, who2001icf]
relacoes:
  - { tipo: complementa, alvo: iop.health.cif }
  - { tipo: relacionado-a, alvo: iop.fund.privacidade-e-seguranca }
  - { tipo: relacionado-a, alvo: iop.sem.interoperabilidade-semantica }
termos: [Resource, Profile, StructureDefinition, CodeSystem, ValueSet, ConceptMap, REST]
---

# HL7 FHIR R5

## Definição e terminologia

FHIR (*Fast Healthcare Interoperability Resources*) é o padrão da HL7 para troca de dados de saúde. A versão consultada é **v5.0.0 (Release 5)**, marcada como **STU** (*Standard for Trial-Use*); a página traz como data apenas a geração do documento, em 26 de março de 2023 [F: hl72023fhir].

**Conceitos centrais** presentes na documentação consultada [F: hl72023fhir]: tipos de Resource; Extensions, com registro próprio; Profiles, com `StructureDefinition` sob Conformance; API REST e Search; e terminologia por `CodeSystem`, `ValueSet`, `ConceptMap` e serviço de terminologia.

**Paradigmas de troca** [F: hl72023fhir]: REST (com Search), messaging, documents e services; o mesmo módulo lista também Databases e Subscriptions.

## Problema que resolve

Neste domínio, FHIR interessa como ponte: perfis cognitivo-motores, avaliações funcionais e laudos relevantes para o contexto educacional nascem do lado da saúde, e FHIR é o formato em que esses dados circulam [I].

## Fundamentos e funcionamento

A arquitetura relevante para interoperabilidade com educação [I]:

- **Resource + Profile**: o recurso é genérico; o perfil restringe-o para um caso de uso, por `StructureDefinition`. Qualquer integração séria usa perfis, não recursos crus [F: hl72023fhir] [I].
- **Terminologia**: `CodeSystem` publica um sistema de códigos, `ValueSet` seleciona um subconjunto utilizável em um campo, `ConceptMap` declara correspondências entre sistemas [F: hl72023fhir]. É o equivalente, no mundo FHIR, ao que SKOS faz no mundo RDF (ver `iop.sem.vocabularios-e-skos`) [I].
- **Múltiplos paradigmas**: REST para consulta ponto a ponto, documents para registros assinados, messaging para eventos, subscriptions para notificação [F: hl72023fhir].

A CIF entraria nesse arranjo como `CodeSystem`, com `ValueSet` por caso de uso [I] — não verificado se a OMS ou a HL7 publicam a CIF nesse formato.

## Requisitos e pressupostos

- Troca com sistemas de saúde exige base legal específica: dado de saúde é dado pessoal sensível (ver `iop.fund.privacidade-e-seguranca`) [I].
- O lado educacional precisa de um perfil acordado, não do modelo FHIR inteiro [I].

## Vantagens e limitações

Vantagens [I]: adoção ampla no setor de saúde; modelo de extensibilidade e perfis maduro; terminologia tratada como cidadã de primeira classe, o que é raro entre padrões educacionais.

Limitações [I]:
- Superfície enorme: adotar FHIR inteiro para trocar meia dúzia de observações é desproporcional; o caminho é um perfil mínimo.
- R5 é STU [F: hl72023fhir], não normativa em toda a extensão; versões coexistem em produção (R4 segue amplamente usada — não verificado).
- A fronteira educação–saúde é sobretudo jurídica e organizacional, não técnica; FHIR não ajuda nessas camadas [I].

## Relações com outros conceitos

Complementa `iop.health.cif` (FHIR transporta, CIF dá vocabulário). Relaciona-se a `iop.sem.interoperabilidade-semantica` pelo aparato de terminologia.

## Lacunas e questões abertas

- Data oficial de publicação e status normativo por parte do padrão: não verificados (a página traz apenas a data de geração).
- Existe `CodeSystem` FHIR publicado para a CIF? Não verificado.
- Perfis brasileiros (RNDS — Rede Nacional de Dados em Saúde) e sua aplicabilidade: não investigados.
- Bundle e FHIRPath não aparecem na página consultada e ficam sem cobertura.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| hl72023fhir | normativo | 2026-10-29 |
| who2001icf | normativo | 2026-10-29 |
