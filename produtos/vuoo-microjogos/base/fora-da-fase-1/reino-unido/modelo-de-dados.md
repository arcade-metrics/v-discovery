# Modelo de dados: Reino Unido

Não há modelo de dados britânico único. Há **quatro** sistemas de coleta (Inglaterra: CBDS + School Census; Escócia: ScotXed; País de Gales: PLASC; Irlanda do Norte: School Census DE, especificação não encontrada). Todos são **modelos de coleta** (snapshot periódico + séries contínuas), não modelos transacionais. Fontes em [evidencias.md](evidencias.md).

## 1. Inglaterra (CBDS / School Census 2026–27)

```
LA (LA number, 3)
 └─ School (URN 6; LAESTAB = LA+Estab 7; UKPRN 8; phase N00280; SEN type aprovado CS077)
     ├─ Class [agregado, só primárias]: nome, tipo (CS036), key stage (CS037), ano (CS086, M=misto),
     │        nº professores, nº adultos não docentes, nº alunos da casa / de outras escolas, atividade (CS035)
     └─ Pupil (UPN 13; Former UPN; ULN 10 se ≥14; UCI)
         ├─ Identificação: nomes legal/preferido/anterior, sexo, data nasc.
         ├─ Características: etnia (CS080 + fonte CS093), língua, FSM (períodos), pupil premium
         ├─ Status/matrícula: enrolment status (CS007: C, M, S, F, O, G, P), data de entrada, ano NC atual (CS086)
         ├─ SEN: provisão (CS096: N/K/E), tipos (CS071) com ranking (máx. 2 no censo), SEN unit / resourced provision
         ├─ Frequência: sessões possíveis/presentes/ausências por motivo (CS066, por meio período)
         ├─ Suspensões e exclusões (datas, até 3 motivos, sessões, revisão)
         ├─ Managed moves (destino URN, motivo)
         ├─ Alternative provision placement (URN/UKPRN do provedor, padrão de frequência)
         ├─ Home information (endereço, UPRN)
         └─ Post-16 learning aims
Contact (do aluno, em MIS/CTF): prioridade, relação (CS012), responsabilidade parental (bool), telefones (CS011), e-mail
```

| Aspecto | Inglaterra |
|---|---|
| Identificadores primários | UPN (aluno), URN (escola); secundários ULN, LAESTAB, UKPRN, TRN |
| Cardinalidades declaradas | máx. 2 tipos de SEN no censo; até 3 motivos de suspensão; contatos 1..n com prioridade 1–10 |
| Hierarquia | LA → escola; academy trusts como grupos no GIAS (não no CBDS) [I] |
| Enums | code sets CSnnn versionados, com aba de arquivados |
| Validação | regra por item (formato, dígito verificador, faixas 0–400 sessões) + regras cruzadas nas especificações |
| Temporalidade | por termo (autumn/spring/summer); itens contínuos com datas de início e fim |
| CRUD | não: retorno completo por coleta; correções em reenvio |
| Serialização | XML (W3C XML Schema) |
| Transferência entre escolas | CTF (Common Transfer File) com itens CBDS |
| Extensão | RFC ao DfE |
| Autenticação | serviço de coleta do DfE (detalhe não verificado) |

**Turma e matrícula.** Não há vínculo aluno↔turma nem turma↔professor no padrão nacional; turma aparece como agregado. O vínculo aluno↔escola tem tipo (registro único, principal, subsidiário, convidado). [I] Gestão de turmas, horários e ofertas pertence ao MIS e a padrões de mercado (ex.: dados de MIS via APIs comerciais), não ao DfE.

## 2. Escócia (ScotXed 2026)

```
School ─ Pupil (SCN 9) ─ stage (P1–P7, S1–S6, S9, SP) ─ registration class (P1–P7)
                       ─ attendance at special schools/units (meios-dias 0–10)
                       ─ Need record 0..n: category (motivo ASN) ; types 0..n (CSP, IEP, AssessedDisabled, DeclaredDisabled, Child's Plan)
                       ─ nature of additional support 0..n (01–06, 99)
School ─ class size (componente primário)
```
Spec em XLSX com mín./máx. de ocorrência, tipo (ex.: `Code (2c)`, `Non-negative Integer (9n)`), nome XML (ex.: `student-stage`) e regras numeradas (erro × consulta; ex.: 1110 dígito do SCN; 1070 idade × estágio em 1º de março) [S-UK-09].

## 3. País de Gales (PLASC 2026)

Aluno com UPN (esquema compartilhado com a Inglaterra [S-UK-02]); `Pupil ALN provision` (N/C/L) obrigatório; `Additional needs` (código 4c) obrigatório, ≥1 por aluno; fluência em galês; dados de escola (refeições, conselho, pessoal em retirada para o SWAC) [S-UK-15].

## 4. Irlanda do Norte

Censo anual em outubro; especificação de dados **não encontrada**. Registro SEN por estágio e statement [S-UK-17].

## 5. Comparação das quatro nações

| Elemento | Inglaterra | Escócia | País de Gales | Irlanda do Norte |
|---|---|---|---|---|
| Id do aluno | UPN | SCN | UPN | not_found |
| Data do censo | trimestral (3 censos) | anual, set. (9/9/2026) | anual, jan. (20/1/2026) | anual, out. |
| Unidade de ano | Year group R, 1–14 | Stage P1–S6 | Year group [I] | Year 1–14 (primária de 7 anos) |
| Estágio curricular | Key stage 1–4 (+EYFS) | Nível CfE (Early–Fourth) independente do estágio | Progression step 1–5 [I] | Foundation, KS1–KS4 |
| Necessidade: estado | provisão N/K/E | registro de necessidade + tipo de plano | ALN provision N/C/L | estágio 1–2 / statement |
| Necessidade: tipo | 14 códigos, ranking ≤2 | 25 motivos, inclui sociais | 15 códigos | not_found |
| Plano individual | EHC plan (seções A–K), mantido pela LA | CSP (estatutário), IEP, Child's Plan | IDP mantido pela escola ou pela LA | statement |
| Turma no dado nacional | agregado (primária) | registration class (primária) | agregado | not_found |
