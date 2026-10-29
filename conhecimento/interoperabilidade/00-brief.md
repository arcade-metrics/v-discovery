---
id: iop.brief
titulo: Brief do domínio padrões de interoperabilidade
tipo: relatorio
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: padrões de interoperabilidade

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

A primeira versão do domínio já existe: comece pelo [README](README.md). As diferenças entre a estrutura sugerida abaixo e a adotada estão registradas em [`_plano-ids.md`](_plano-ids.md), e o que ficou em aberto, em [`relatorio.md`](relatorio.md).

## Escopo

Padrões para troca de dados e integração entre sistemas educacionais, e entre sistemas educacionais e de saúde. Inclui: rastreamento de experiências de aprendizagem (xAPI, cmi5, Caliper); integração de ferramentas e conteúdo (LTI, SCORM, Common Cartridge, QTI); dados de matrícula e roster (OneRoster, Ed-Fi); credenciais (Open Badges, CLR); classificações e trocas do lado clínico relevantes para perfis cognitivo-motores (CIF da OMS, HL7 FHIR); padrões e sistemas brasileiros (Educacenso/INEP, sistemas estaduais). Para cada padrão: versão vigente, órgão mantenedor, modelo de dados, cobertura, adoção e limites.

Fora do escopo: transporte em tempo real (fica em `realtime-multiplayer`), semântica de currículo (fica em `grafo-conhecimento-educacional`).

## Estrutura sugerida

- `learning-records/`: xAPI, cmi5, Caliper, comparações.
- `tool-integration/`: LTI 1.3 e Advantage, SCORM, Common Cartridge.
- `assessment/`: QTI.
- `rostering/`: OneRoster, Ed-Fi.
- `credentials/`: Open Badges, CLR.
- `health/`: CIF, FHIR, pontos de contato com educação.
- `brazil/`: Educacenso, sistemas estaduais, requisitos legais de integração.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. IEEE 9274.1.1 (xAPI) e documentação ADL; cmi5.
2. 1EdTech: LTI 1.3 e LTI Advantage, QTI 3, OneRoster 1.2, Caliper Analytics 1.2, Common Cartridge, Open Badges 3.0, CLR 2.0, CASE.
3. ADL SCORM 2004.
4. Ed-Fi Alliance, data standard.
5. OMS, Classificação Internacional de Funcionalidade (CIF); HL7 FHIR R5.
6. INEP, Censo Escolar e Educacenso; documentação pública de sistemas estaduais.

## Perguntas abertas

- Onde xAPI e Caliper se sobrepõem e quando cada um é mais adequado?
- Como mapear eventos de jogo para statements xAPI sem perder granularidade?
- Que padrão cobre dados cognitivo-motores de forma a dialogar com saúde e educação?
- Quais integrações públicas no Brasil têm API documentada?
