# Questões abertas — Internacional

| Id | Questão | Por que importa | Encaminhamento proposto |
|---|---|---|---|
| QI-01 | **Candidato a atributo/entidade do Core:** ordinal de série neutro. ISCED não desce à série; crosswalk série↔série entre países precisa de um eixo próprio. Candidato: "anos acumulados desde o início do ISCED 1" (coluna K do modelo UIS antigo) mais idade teórica. | Sem isso, "3º ano BR" ↔ "Grade 3 US" ↔ "Year 4 ENG" fica por nome | decidir em `core/`; testar com os 6 mapeamentos |
| QI-02 | Nível ISCED atribuído ao **segmento** (anos iniciais/finais) e não à etapa: C.PRG precisa de hierarquia etapa → segmento → série | BR e PT têm etapas que cruzam ISCED 1 e 2 | modelar em C.PRG |
| QI-03 | Inconsistência no mapeamento BR: creche com ISCED-P 010 e ISCED-A 020 | importação automática herdaria o erro | tratar como dado do adaptador, com nota; confirmar no texto ISCED |
| QI-04 | Reino Unido: Reception (020) × primária com idade inicial 4–5 e duração 6–7 | fronteira ambígua para alunos de 4–5 anos | resolver no adaptador RU com fonte do DfE |
| QI-05 | Revisão do ISCED em curso; nova edição pode mudar códigos (níveis 6–8, ECE) | código sem `scheme` versionado quebraria | sempre `scheme = isced-2011-p/a` |
| QI-06 | ISCED-F não serve para componente curricular; o Core precisa de outro vocabulário neutro para C.SUB (ou nenhum) | evitar falsa equivalência Matemática ↔ 0541 | questão para `core/` |
| QI-07 | Mapeamento BR é de 2012/2013; existe versão mais nova no UIS? | BNCC e Novo Ensino Médio mudaram a estrutura | verificar periodicamente; a página não traz data |
| QI-08 | ISO 21001 e 29993: texto pago; requisitos de dados inferidos só pelos títulos | lista de verificação incompleta | decidir se vale comprar a 21001:2025 |
| QI-09 | **Candidato a entidade do Core:** Feedback / Complaint (satisfação e reclamação de partes interessadas, ISO 21001 9.1.2) | não há alvo em C.xxx | registrar em `core-v0.1.md` |
| QI-10 | Agenda escolar: guardar hora local + fuso IANA ou só instante UTC? | aulas recorrentes atravessam horário de verão (EUA, UE, RU) | proposta: hora local + fuso (RFC 9557 na serialização) |
| QI-11 | Subtags BCP 47 de línguas de sinais (bzs, ase, bfi, csl) não conferidas no registro IANA | dado de acessibilidade | conferir antes de fixar vocabulário |
| QI-12 | Abaixo de ISO 3166-2 não há padrão internacional (município, distrito escolar) | C.ORG precisa de jurisdição local | C.IDN com `scheme` por adaptador |
| QI-13 | UUIDv7 em IDs de aluno expõe instante de cadastro | privacidade de menores | v7 interno; pseudônimo em exportação |
| QI-14 | Domínio e política de URIs persistentes do Core (hash × 303; versão no caminho) | URIs publicados não podem mudar | decisão de produto |
| QI-15 | OpenAPI 3.1 × 3.2 | suporte de ferramentas | começar em 3.1; reavaliar |
| QI-16 | Tipos de equivalência do crosswalk ↔ propriedades SKOS de mapeamento: adotar formalmente? | crosswalks de todas as pastas | proposta em `int.w3c-semantic-stack` |
| QI-17 | IEEE 1484.20.3: classes não verificadas (texto pago); exportar C.CMP para SCD sem perda? | neutralidade do Core | obter texto ou artefatos IEEE SA Open |
| QI-18 | IEEE 2881-2025: termos não verificados | alinhamento C.ACT/C.EVT | idem |
| QI-19 | **Candidato a entidade do Core:** AccessPreference (C.PRF), separada de C.SUP | preferência de acesso não é necessidade nem diagnóstico | registrar em `core-v0.1.md` |
| QI-20 | Vocabulários de C.SUP: CIF, barreiras pedagógicas, AfA — qual é o mínimo neutro? | evitar reduzir a diagnóstico | questão compartilhada com `brasil/` (inclusão) |
| QI-21 | Credenciais exportáveis não devem carregar dados de apoio (C.SUP) | dado sensível portável | regra de privacidade |
