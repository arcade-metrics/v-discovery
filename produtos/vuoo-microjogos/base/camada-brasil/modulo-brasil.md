## 4. O módulo Brasil

O índice completo está em este diretório.

### 4.1 Componentes

| Componente | O que faz | Insumo pronto | Falta |
|---|---|---|---|
| **Perfil `vuoo-br`** | SHACL de cardinalidades e vocabulários obrigatórios; extensões BR (classe especial, turma multietapa, localização diferenciada…) | modelo-de-dados.md §4 | escrever as shapes |
| **Vocabulários BR** | ConceptSchemes do Censo 2026 e do CMDEB: etapa, modalidade, cor/raça, deficiência, função, situação, dependência… | terminologia.md | **crosswalk Censo × CMDEB**: não existe oficial, então é nosso, em SSSOM |
| **Identidade** | Resolução por CPF (Inue) → ID INEP → certidão → nome + nascimento + filiação; todos guardados com scheme | modelo-de-dados §6 | decidir se o CPF é obrigatório no cadastro; estado "CPF pendente" |
| **Adaptador Censo Escolar** | Exporta os registros 00/10/20/30/40/50/60 (1ª etapa) e a Situação do Aluno (2ª etapa); reimporta os códigos INEP gerados | leiaute 2026 V5 campo a campo | leiaute da Situação 2026 (não publicado); 2025 tem 7/8 contraditórios |
| **Adaptador Gestão Presente** | Cliente da API CMDEB v2: estudante, matrícula, enturmação, frequência mensal, desempenho, profissionais | OpenAPI lido; divergências Portaria × API documentadas | confirmar com o MEC o alcance da obrigatoriedade (só para redes aderentes) |
| **Currículo** | Extrai a BNCC da fonte oficial do MEC (no repositório **vuoo-base** (`fontes/bncc/`, https://github.com/arcade-metrics/v-base): fonte oficial `BNCC_EI_EF_110518_versaofinal_site.pdf` (versão final, EI, EF e EM) e cópia de trabalho `BNCC_reparado.pdf`); importa o Currículo Paulista com `derivaDe`; modela os IFAs da Res. CNE/CEB 4/2025 | bncc/, bncc-computacao/, bncc-dados/, modelo-de-dados-curriculo §1 | escolher o texto canônico (2017 × 2018); sentido oficial de `*` e A/B/C no CP; volume EM do CP |
| **Avaliação** | Escalas e esquemas de classificação do Saeb, SARESP e CNCA; alinhamento item→habilidade por curadoria | modelo-de-dados-curriculo §2 | cortes atuais do SARESP; escalas Saeb-BNCC |
| **Inclusão / PEI** | Estudo de caso, PAEE/PEI com o mínimo federal (Port. 421 arts. 10–11) e o formato SP (Anexos II–V), prazos e revisões | modelo-de-dados-curriculo §3 | posição jurídica sobre laudo (SP 129 × MEC 421) |
| **Regras LDB** | Validação de carga, dias letivos, frequência de 75% (e 60% na EI), idade por etapa | modelo-de-dados §5 | conferir a redação literal da LDB |
| **Privacidade BR** | Base legal por operação, sensibilidade por campo, consentimento parental, ECA Digital | fichas lgpd-educacao e eca-digital | papéis de controlador e operador; prazos de guarda |

### 4.2 Ordem de construção sugerida (pelo risco)

1. **Core + identidade + organização + matrícula** (C.ORG, C.PER, C.ROL, C.IDN, C.ENR, C.GRP, C.SES). Tudo depende disso, e é onde o Censo e o CMDEB mais divergem.
2. **Vocabulários e mapeamentos** (C.VOC, C.MAP), com o Censo 2026 e o CMDEB carregados e o crosswalk entre eles.
3. **Currículo** (C.CFW, C.CMP, C.CAS, C.ADP) a partir do dataset verificado. É pré-requisito da camada curricular das micro-atividades.
4. **Inclusão e PEI** (C.SUP, C.ELG, C.PLN). É o núcleo de valor da interface do professor.
5. **Exportação para o Censo e a API CMDEB.** Só é necessária quando uma rede pedir, e sai mais barata depois dos itens 1–2.
6. **Avaliação externa** (Saeb, SARESP). Serve de referência para relatórios; prioridade menor.

