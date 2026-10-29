---
id: iop.br.educacenso
titulo: Educacenso e o Censo Escolar
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [qacademico2015educacenso, imsglobal2022oneroster, edfi2026datastandard]
relacoes:
  - { tipo: alternativa-a, alvo: iop.ros.oneroster }
  - { tipo: complementa, alvo: iop.br.lgpd }
  - { tipo: relacionado-a, alvo: iop.ros.comparison }
termos: [Censo Escolar, leiaute, migração, ID INEP, arquivo texto]
---

# Educacenso

## Definição e terminologia

Educacenso é o sistema do INEP para a coleta do Censo Escolar da educação básica. Para este domínio, o que importa é o seu mecanismo de intercâmbio: escolas e redes enviam dados ao INEP, e esse envio tem formato definido [I].

**Mecanismo documentado.** Manuais de sistemas acadêmicos descrevem a exportação como geração de um arquivo texto com os dados no leiaute definido pelo MEC/INEP, enviado depois pelo site do Educacenso; antes da transmissão definitiva, o arquivo passa por programa validador e pode ser testado em ambiente de treinamento [F: qacademico2015educacenso]. O procedimento inclui exportar os IDs INEP já gerados para docentes e alunos em anos anteriores, para reaproveitá-los na nova migração [F: qacademico2015educacenso].

As fontes consultadas são manuais de fornecedor de sistema acadêmico, de 2015, não documentação do INEP [I].

## Problema que resolve

Consolidar nacionalmente os dados de matrícula da educação básica. O efeito colateral relevante para este domínio é que o Censo é, na prática, o vocabulário comum de dados escolares no Brasil — o papel que o CEDS ocupa nos Estados Unidos [I].

## Fundamentos e funcionamento

**Troca em lote por arquivo, com leiaute posicional.** O leiaute define tipos, tamanhos e formatos dos campos [F: qacademico2015educacenso]. Em termos de `iop.fund.dados-vs-protocolo`, é modelo de dados mais binding, sem protocolo nem API [I].

**ID INEP como identificador nacional.** O reaproveitamento dos IDs entre edições [F: qacademico2015educacenso] indica um identificador persistente de aluno e de docente em escala nacional — o ativo mais valioso do sistema para interoperabilidade, e o mais sensível do ponto de vista de proteção de dados (ver `iop.br.lgpd`) [I].

**Periodicidade anual.** Uma troca por ano não serve a nenhum uso operacional: não substitui rostering (ver `iop.ros.oneroster`) nem alimenta análise contínua [I].

## Requisitos e pressupostos

- A escola ou rede opera um sistema acadêmico capaz de gerar o leiaute vigente do ano, que muda entre edições [I].
- A conferência final é responsabilidade da instituição: os manuais alertam que pode haver divergência entre o exportado e a realidade da escola [F: qacademico2015educacenso].

## Vantagens e limitações

Vantagens [I]: cobertura nacional e identificador persistente; vocabulário de fato compartilhado por todos os sistemas acadêmicos brasileiros.

Limitações [I]:
- Troca anual em arquivo, sem API documentada para envio.
- Leiaute próprio, sem correspondência publicada com padrões internacionais.
- A documentação acessível é de fornecedores, não do órgão; o material consultado é de 2015 e pode estar desatualizado.

## Alternativas e comparações

| Necessidade | Educacenso | OneRoster | Ed-Fi |
|---|---|---|---|
| Obrigação legal no Brasil | sim | não | não |
| Rostering operacional | não | sim [F: imsglobal2022oneroster] | sim [F: edfi2026datastandard] |
| Frequência | anual | contínua ou em lote | contínua |
| Identificador nacional | sim (ID INEP) | não | não |

## Relações com outros conceitos

Alternativa parcial a `iop.ros.oneroster` quanto a papel (dados de matrícula), não quanto a uso. Complementa `iop.br.lgpd`.

## Lacunas e questões abertas

- **Lacuna principal**: não foi localizada documentação oficial do INEP sobre o leiaute vigente nem sobre existência de API de envio. As buscas retornaram manuais de fornecedores (2013–2016) e uma proposta acadêmica de API para consulta a dados públicos, que não é via de entrada no Educacenso. Verificar diretamente em `inep.gov.br` e no Caderno de Conceitos do Censo Escolar.
- Sistemas estaduais (SEDUC-SP e congêneres) e suas APIs: não investigados.
- Mapeamento entre o leiaute do Censo e OneRoster ou Ed-Fi: não existe nesta base e seria um artefato útil.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| qacademico2015educacenso | secundario | 2026-10-29 |
| imsglobal2022oneroster | normativo | 2026-10-29 |
| edfi2026datastandard | fornecedor | 2026-10-29 |
