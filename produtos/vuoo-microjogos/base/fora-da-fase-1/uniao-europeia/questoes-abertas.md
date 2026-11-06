# Questões abertas: União Europeia

## Candidatos a entidade do Core

| # | Conceito | Origem | Por que não cabe no Core provisório | Proposta [I] |
|---|---|---|---|---|
| UE-C1 | Qualificação (Qualification) | ELM, EQF | C.CRD é a instância; C.PRG é etapa escolar; C.CMP é item curricular. Falta "especificação de reconhecimento formal concedida por autoridade competente" | subtipo de C.CMP ou entidade C.QLF; na educação básica corresponde ao certificado de conclusão de etapa |
| UE-C2 | Escala de proficiência / esquema de notas | DigComp, ELM GradingScheme | C.VOC é genérico; níveis de proficiência pertencem ao framework e têm ordem | entidade C.SCL (escala ordenada, ligada a C.CFW ou C.ASM) |
| UE-C3 | Direito resultante (Entitlement) | ELM | sem alvo | provavelmente não necessário na educação básica; registrar como extensão |
| UE-C4 | Acreditação | ELM AMS | sem alvo | fora do escopo básico; extensão |
| UE-C5 | Crédito | ECTS, ELM | sem alvo | atributo opcional de C.PRG/C.CMP |
| UE-C6 | Distribuição de resultados da coorte | ELM | sem alvo | derivável; não modelar |
| UE-C7 | Separação Especificação × Instância | ELM (padrão geral) | o Core provisório lista entidades sem explicitar o par | adotar como regra de modelagem (C.ASM↔C.RES, C.CMP↔C.CRD, C.ACT↔C.EVT) |

## Lacunas de verificação

1. **ELM 3.3 × 3.1**: só a 3.1 foi inspecionada (GitHub arquivado). Diferenças de classes/propriedades na 3.2/3.3 não verificadas; baixar o dataset `snb-model` do EU Vocabularies.
2. **Códigos das 37 listas controladas** não extraídos.
3. **Anexo VI da Recomendação EQF 2017** (dados mínimos de qualificação): EUR-Lex não respondeu.
4. **DigComp 3.0 dados legíveis por máquina**: página do catálogo JRC devolveu erro; formato e licença desconhecidos.
5. **DigComp 2.2: 8 níveis** e nomes das áreas: conhecimento prévio, não reconferido.
6. **DigCompEdu níveis** (A1–C2) não confirmados; framework em revisão até 2027.
7. **GDPR art. 8**: tabela de idade por Estado-membro não verificada em fonte primária (já pendente em `psg.legal.gdpr-k-and-coppa`).
8. **Art. 165 TFUE**: competência nacional afirmada por [I], texto não lido.
9. **"European Higher Education Interoperability Framework"**: não encontrado como documento formal; tratado como o conjunto EWP/EMREX/ESC.
10. **EDC × EUDI Wallet**: relação não verificada.
11. **Padrões nacionais de dados escolares** nos 27 Estados (identificadores de aluno, censos): não levantados; seriam o trabalho real de um adaptador UE.

## Conflitos e ambiguidades

- O README do ELM no GitHub diz "European Learning Model"; o `rdfs:label` da ontologia diz "Europass Learning Model". Mesmo artefato, nome mudou.
- `elm:Group` existe, mas não equivale a turma; nome semelhante, conceito diferente (regra 6 do briefing).
- DigComp 2.2 (8 níveis) e 3.0 (4 níveis) convivem em uso; alinhamento entre versões não é publicado pelo JRC [não verificado].
