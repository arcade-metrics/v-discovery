---
id: iop.asmt.qti
titulo: QTI 3.0 (Question and Test Interoperability)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2022qti30, imsglobal2011cc]
relacoes:
  - { tipo: complementa, alvo: iop.tool.common-cartridge }
  - { tipo: complementa, alvo: iop.md.ieee-lom }
  - { tipo: relacionado-a, alvo: iop.tool.lti-advantage }
  - { tipo: relacionado-a, alvo: iop.comp.case }
termos: [assessmentItem, assessmentTest, response processing, PCI, CAT, APIP, acessibilidade]
---

# QTI 3.0

## Definição e terminologia

QTI é o padrão do 1EdTech para representar itens de avaliação, provas e seus relatórios de resultado, permitindo troca entre ferramentas de autoria, bancos de itens, montadores de prova, plataformas de aprendizagem e sistemas de aplicação [F: imsglobal2022qti30, §1, §2].

Versão consultada: **QTI 3.0, 1EdTech Final Release, Spec Version 3.0, Document Version 1.0, emitida em 1 de maio de 2022** [F: imsglobal2022qti30].

O modelo é definido de forma abstrata em UML, com um binding XML fortemente recomendado para intercâmbio, e pontos de extensão bem definidos para encapsular dados proprietários [F: imsglobal2022qti30, §2].

## Problema que resolve

Bancos de itens ficam presos à ferramenta que os criou. QTI separa a representação do item da plataforma que o aplica, e inclui no modelo a informação de acessibilidade, que de outro modo se perde na migração [I].

## Fundamentos e funcionamento

**Conjunto documental (§2.4)** [F: imsglobal2022qti30]: Best Practice and Implementation Guide (QTI-IMPL-30), Conformance and Certification (QTI-CERT-30), Terms and Definitions (QTI-TERM-30), APIP-to-QTI 3 Migration Guide (QTI-MIGR-30), o ASI Information Model e seu binding, Metadata Information Model and Binding (QTI-MD-BIND-30), Results Reporting (QTI-RR-30), Usage Data (QTI-UD-30), arquivos XSD e exemplos.

**Empacotamento e metadados (§2.4).** O QTI 3.0 perfila o 1EdTech Content Packaging v1.2, o AccessForAll PNPv3, o AfA Digital Resource Description e o Metadata v1.3, e também perfila o IEEE LOM [F: imsglobal2022qti30, §2.4].

**Novidades da 3.0 (§1).** Suporte a HTML5 e web components, vocabulário compartilhado de apresentação, recursos de acessibilidade, Computer Adaptive Testing nativo e Portable Custom Interactions (PCI) nativas [F: imsglobal2022qti30, §1].

**Relação com QTI 2.x e APIP (§1, §2.3).** QTI 2.2 e APIP 1.0 permitiam ajustes do ambiente de avaliação específicos do candidato; o QTI 3.0 foi desenvolvido para resolver problemas surgidos depois do QTI 2.1 e do APIP 1.0, e entre seus objetivos declarados está fundir APIP e QTI em uma única especificação, acrescentar informação de apresentação e integrar recursos de acessibilidade [F: imsglobal2022qti30, §1, §2.3]. O guia QTI-MIGR-30 é o caminho para migrar informação APIP [F: imsglobal2022qti30, §2.4].

## Requisitos e pressupostos

- O sistema de aplicação implementa *response processing* e *outcome processing* conforme o modelo, e não apenas a renderização do item [I].
- Para PCI, a plataforma executa componentes de terceiros com segurança [I].

## Vantagens e limitações

Vantagens [I]: acessibilidade incorporada ao modelo, e não acoplada por fora; CAT nativo; extensões previstas; cobre também relatório de resultados (QTI-RR-30) e dados de uso (QTI-UD-30).

Limitações [I]:
- Complexidade alta: o conjunto documental tem mais de dez documentos [F: imsglobal2022qti30, §2.4].
- Implementações parciais são comuns; dois sistemas "QTI 3" podem suportar conjuntos diferentes de interações.
- Migração a partir de QTI 2.x/APIP exige guia próprio, isto é, não é automática [F: imsglobal2022qti30, §2.4] [I].

## Alternativas e comparações

| Necessidade | QTI 3.0 | AGS (LTI) | formato proprietário |
|---|---|---|---|
| Representar o item | sim | não | sim |
| Aplicar e processar resposta | sim | não | sim |
| Devolver nota ao LMS | via resultados | sim | depende |
| Acessibilidade padronizada | sim | não | raramente |
| Portabilidade entre fornecedores | alta | n/a | nenhuma |

## Métricas e métodos de avaliação

Conformidade pelo QTI-CERT-30 [F: imsglobal2022qti30, §2.4]. Em avaliação de fornecedor: número de tipos de interação suportados, suporte a PCI e resultado da importação de um pacote de referência [I].

## Relações com outros conceitos

Complementa `iop.tool.common-cartridge`, que transporta itens QTI dentro de cartridges [F: imsglobal2011cc], e `iop.md.ieee-lom`, perfilado pelo QTI para metadados. Relaciona-se a `iop.comp.case`, que fornece identificadores para as competências a que um item se alinha [I].

## Lacunas e questões abertas

- A página de overview não detalha response processing, outcome processing nem a lista de interações; é preciso ler QTI-INFO-30 e QTI-BIND-30.
- Perfil de conformidade mínimo exigido pelas plataformas mais usadas: não verificado.
- Relação entre QTI Results Reporting e o Assessment Results Profile do OneRoster: não verificada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2022qti30 | normativo | 2026-10-29 |
| imsglobal2011cc | normativo | 2026-10-29 |
