---
produto: VUOO
slug: vuoo-microjogos
etapa: base/estrutura-escolar
status: cópia de referência, revisada para os microjogos
atualizado_em: 2026-11-05
---

# Base: estrutura escolar, pessoas e inclusão

Recorte copiado do estudo de padrões já feito (OneRoster, Ed-Fi, CEDS, Edu-API, Censo Escolar/INEP, CMDEB), para esta pasta ser autossuficiente. Os códigos `C.xxx` são os nomes estáveis das entidades.

## 1. Organização acadêmica

| Código | Entidade | Nota |
|---|---|---|
| C.ORG | Organização | Tipos: sistema, rede, mantenedora, escola, unidade. Relações N:N com tipo e vigência (não é uma árvore única). |
| C.LOC | Local (sala) | Opcional: o Censo não identifica salas. |
| C.SES | Período letivo | Hierárquico: ano letivo → período → bimestre. Tem calendário (dia letivo ou não). |
| C.STG | Etapa | Etapa, segmento, ano/série, modalidade, com nível ISCED. |
| C.SVC | Programa de serviço | AEE, tempo integral, atividade complementar. |
| C.SUB | Componente curricular | Código nacional (Tabela de Áreas do Censo). |
| C.CRS | Curso | Opcional no Brasil (o Censo não tem catálogo). |
| C.OFR | Oferta | Componente × turma × período × professores. No OneRoster é *class*. |
| C.GRP | Turma / grupo | Tipo: turma acadêmica, grupo de aprendizagem, grupo de AEE. |
| C.SCH | Horário | |
| C.ENR | Matrícula | Dois níveis: na escola/etapa e na turma/oferta. Tipo: escolarização, AEE, complementar. |
| C.ENS | Situação da matrícula | Eventos de situação (os 17 do CMDEB). |
| C.ATT | Frequência | Agregada ou por evento. |

## 2. Pessoas e papéis

| Código | Entidade | Nota |
|---|---|---|
| C.PER | Pessoa | Mínimo de dados pessoais. Identificada por UUID interno. |
| C.IDN | Identificador | Documentos presos à pessoa: CPF (preferencial), certidão de nascimento, ID INEP, RNM, passaporte. |
| C.ROL | Papel | Vocabulário: aluno, professor, gestor, profissional de apoio, responsável. Uma pessoa pode ter vários. |
| C.REL | Vínculo entre pessoas | Responsável × aluno, com tipo de vínculo e direitos (consentimento, acesso). |

Regras:

- Aluno sem CPF é cadastrado mesmo assim, ligado ao responsável, com estado `cpf_pendente`.
- O CPF do responsável nunca identifica o aluno.
- Deduplicação de pessoas sempre com revisão humana.

## 3. Inclusão

| Código | Entidade | Nota |
|---|---|---|
| C.SUP | Perfil de apoio | Barreiras, potencialidades, apoios e acomodações. Existe sem diagnóstico. **É o que alimenta a adaptação.** |
| C.ELG | Elegibilidade (educação especial) | Categoria administrativa para coletas oficiais. Sensível, acesso isolado, **nunca alimenta a personalização**. |
| C.DOC | Referência de documento | Laudo, relatório, parecer, CIPTEA. **Só metadados e referência externa; o VUOO não guarda o arquivo.** Sensível. |
| C.PLN | Plano individual | PEI/PAEE: seções, metas, acompanhamentos e revisões. Mínimo federal da Portaria MEC 421/2026. |

Laudo, mesmo só como campo, é dado sensível (LGPD art. 11). Evitar CID e texto clínico.

## 4. Decisões já tomadas que tocam os microjogos

| Decisão |
|---|
| O cliente é a escola ou a rede. Existe também o **uso avulso**: o aluno entra numa rede geral, com escola, turma e professor gerais, na mesma estrutura de uma rede real. |
| O aluno avulso não compartilha dados com ninguém. Se entrar numa escola, leva o histórico com a aprovação dele ou do responsável. |
| O histórico é do aluno. A escola nova lê o histórico sem ver qual era a escola anterior. |
| Autorização do responsável com o menor atrito: link que já autentica. Nenhum dado do aluno é coletado antes dela. |
| Login do aluno sem e-mail nem senha: o aparelho vinculado (código ou QR) é a credencial. |
| Na operação com a escola, a escola é controladora e o VUOO é operador (LGPD). No avulso, o VUOO é controlador. |
| Variações de estado e rede entram como dado (campos opcionais, vocabulários), nunca como código específico. |
