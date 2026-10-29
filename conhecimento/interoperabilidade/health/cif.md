---
id: iop.health.cif
titulo: CIF / ICF (Classificação Internacional de Funcionalidade)
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [who2001icf, cdc2024icfoverview]
relacoes:
  - { tipo: complementa, alvo: iop.health.fhir }
  - { tipo: complementa, alvo: iop.sem.interoperabilidade-semantica }
  - { tipo: relacionado-a, alvo: iop.fund.privacidade-e-seguranca }
termos: [funcionalidade, deficiência, fatores ambientais, qualificador, desempenho, capacidade]
---

# CIF (ICF)

## Definição e terminologia

A CIF — em inglês, ICF, *International Classification of Functioning, Disability and Health* — é descrita pela OMS como "a classification and terminology of health and health-related domains", o arcabouço para medir saúde e deficiência em nível individual e populacional; inclui uma lista de fatores ambientais, porque funcionalidade e deficiência ocorrem em um contexto [F: who2001icf].

Foi endossada pelos 191 Estados-Membros na 54ª Assembleia Mundial da Saúde, em 22 de maio de 2001 (resolução WHA 54.21), como padrão internacional para descrever e medir saúde e deficiência [F: who2001icf]. É mantida sob governança da OMS, e as atualizações oficiais anuais são aprovadas na reunião de outubro da rede WHO-FIC [F: who2001icf]. Compartilha a mesma fundação da CID e da ICHI, inclusive o mesmo conjunto de códigos de extensão [F: who2001icf].

**Estrutura.** Duas partes, cada uma com dois componentes: Parte 1, funcionalidade e deficiência (funções e estruturas do corpo; atividades e participação); Parte 2, fatores contextuais (fatores ambientais e fatores pessoais) [F: cdc2024icfoverview]. Funções do corpo são as funções fisiológicas dos sistemas corporais, incluindo as psicológicas; estruturas do corpo são as partes anatômicas [F: cdc2024icfoverview]. Fatores pessoais são reconhecidos no modelo mas não são classificados na CIF [F: cdc2024icfoverview].

**Qualificadores.** O qualificador genérico vai de 0 (nenhum problema) a 4 (problema completo), com 8 para não especificado e 9 para não aplicável; fatores ambientais usam escala própria, de barreira ou facilitador. Dois construtos operacionalizam a escala nos domínios de atividades e participação: *performance* (o que a pessoa faz no ambiente atual) e *capacity* (o que consegue fazer em ambiente padronizado); a diferença entre os dois indica onde a intervenção pode agir [F: cdc2024icfoverview].

## Problema que resolve

Descrever funcionalidade de forma comparável entre saúde, educação e assistência social, sem reduzir a pessoa a um diagnóstico — é o que torna possível que um relato pedagógico e um relato clínico falem do mesmo fenômeno [I].

## Fundamentos e funcionamento

Para interoperabilidade, a CIF entra como **vocabulário**, não como protocolo: os códigos (`b`, `s`, `d`, `e` mais dígitos) são valores que podem preencher campos de outros padrões — um recurso de observação FHIR, uma extensão xAPI, um campo de perfil de aluno [I].

A distinção entre capacidade e desempenho [F: cdc2024icfoverview] tem consequência direta para dados educacionais: um resultado medido num jogo é desempenho em ambiente específico, não capacidade; tratar os dois como a mesma coisa é erro semântico, não técnico [I].

## Requisitos e pressupostos

- A codificação é feita por profissional habilitado; não é derivável automaticamente de telemetria [I].
- Dado codificado em CIF é informação de saúde e, portanto, dado pessoal sensível no regime da LGPD (ver `iop.fund.privacidade-e-seguranca`) [I].

## Vantagens e limitações

Vantagens [I]: modelo biopsicossocial, que inclui o ambiente como fator; padrão internacional endossado por todos os Estados-Membros da OMS [F: who2001icf]; compartilha fundação com a CID, o que facilita conviver com dados clínicos [F: who2001icf].

Limitações [I]:
- Granularidade e esforço de codificação altos; na prática, usam-se *core sets* por condição (não verificados nesta rodada).
- Fatores pessoais não classificados [F: cdc2024icfoverview] deixam de fora parte do que o contexto educacional considera relevante.
- Não há, nas fontes consultadas, binding de intercâmbio: é classificação, não formato.

## Relações com outros conceitos

Complementa `iop.health.fhir`, que fornece o transporte para dados clínicos, e `iop.sem.interoperabilidade-semantica`, por ser vocabulário de fechamento semântico.

## Lacunas e questões abertas

- A estrutura detalhada (domínios b1–b8, s1–s8, d1–d9, e1–e5), o esquema de codificação alfanumérico e as regras de qualificador vêm de fonte secundária [F: cdc2024icfoverview]; a publicação da OMS não foi consultada diretamente.
- *Core sets* da CIF aplicáveis a crianças e jovens (ICF-CY) não investigados.
- Uso da CIF em sistemas educacionais brasileiros: não verificado.
- Como representar códigos CIF dentro de FHIR (CodeSystem/ValueSet): não verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| who2001icf | normativo | 2026-10-29 |
| cdc2024icfoverview | secundario | 2026-10-29 |
