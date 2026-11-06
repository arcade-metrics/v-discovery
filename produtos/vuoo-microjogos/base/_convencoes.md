# Convenções da pesquisa de padrões

Regras comuns a todas as pastas desta `base/`. O briefing completo está em [README.md](padroes-README.md); este arquivo fixa **formato de entrega** e o **vocabulário provisório do Core** usado nos crosswalks. Criado em 2026-11-05.

## 1. Estado de cada jurisdição

| Pasta | Estado | Profundidade exigida |
|---|---|---|
| [brasil/](camada-brasil/README-estudo-brasil.md) | **ativo**: módulo a implementar | fichas completas, modelo de dados campo a campo, vocabulários com códigos, regras de validação, identificadores |
| [estados-unidos/](fora-da-fase-1/estados-unidos/README.md) | standby (referência) | fichas, entidades principais, crosswalk com o Core, lacunas |
| [uniao-europeia/](fora-da-fase-1/uniao-europeia/README.md) | standby | idem |
| [reino-unido/](fora-da-fase-1/reino-unido/README.md) | standby | idem |
| [china/](fora-da-fase-1/china/README.md) | standby | idem |
| [internacional/](camada-agnostica/internacional/README.md) | transversal, alimenta o Core | fichas, o que cada padrão oferece ao Core (classificação, formato, vocabulário) |
| [core/](camada-agnostica/core-v0.1.md) | síntese | modelo conceitual agnóstico, glossário canônico, crosswalk consolidado |

"Standby" significa: documentado o suficiente para que um adaptador futuro seja **viável sem mudar o Core**, mas sem detalhar campo a campo.

## 2. Estrutura de cada pasta de jurisdição

```
<jurisdicao>/
  README.md              escopo, estado, índice, resumo em 10 linhas
  fichas/<id>.md         uma por referência: YAML da §6.2 do briefing + análise técnica §6.3
  modelo-de-dados.md     entidades, atributos, identificadores, cardinalidades (D1–D8)
  terminologia.md        conceitos, códigos e vocabulários controlados (com os códigos quando houver)
  cobertura.md           matriz referência × D1..D8 (Completa/Parcial/Indireta/Ausente/Não verificada)
  crosswalk-core.md      conceito local → entidade provisória do Core (§4), com tipo de equivalência
  questoes-abertas.md    ambiguidades, conflitos, decisões pendentes
  evidencias.md          registro: afirmação → fonte (URL), versão, data de acesso
```

Fontes já mineradas (como `brasil/bncc/`, `brasil/cmdeb/`) mantêm sua estrutura própria e são **citadas**, não reescritas.

No Brasil a pesquisa tem duas frentes. A de organização e dados é dona de `modelo-de-dados.md` e `terminologia.md`, e seus demais arquivos levam o sufixo `-organizacao`. A de currículo, avaliação e inclusão usa o sufixo `-curriculo-avaliacao-inclusao` em todos os arquivos.

## 3. Regras de escrita

1. Português, `.md`, tabelas quando houver lista.
2. Toda afirmação factual tem fonte (URL oficial) e data de acesso. Inferência própria leva a marca **[I]**. Informação não encontrada: `unknown` ou `not_found`; nunca preencher por inferência.
3. **Cada fato tem um dono.** Se o padrão já tem documento em `conhecimento/` (ex.: `iop.ros.ed-fi`, `iop.br.educacenso`, `psg.leg.lgpd-children`), a ficha **aponta** para ele pelo caminho relativo e só acrescenta o que falta para o desenho do Core (entidades, identificadores, cardinalidades, códigos). Ver [inventario-existente.md](inventario-existente.md).
4. Distinguir: lei, regulamento, norma técnica, padrão voluntário, framework, vocabulário, recomendação.
5. Não declarar obrigatoriedade sem ato normativo explícito citado.
6. Não declarar equivalência só por nomes semelhantes.
7. Downloads: usar `curl.exe` (TLS do Python falha nesta máquina). PDFs grandes não são baixados para o repo sem discussão; registrar URL e páginas consultadas.

## 4. Entidades provisórias do Core (para crosswalk)

Lista de trabalho, **não** é o modelo final; serve só para que todos os crosswalks usem os mesmos alvos. Quem encontrar conceito sem alvo adequado registra em `questoes-abertas.md` como "candidato a entidade do Core".

| Código | Entidade provisória | Domínio | Nota |
|---|---|---|---|
| C.ORG | Organization | D1 | rede, mantenedora, secretaria, escola, unidade; hierárquica |
| C.LOC | Location | D1 | prédio, sala, espaço |
| C.SES | AcademicSession | D1 | ano letivo, período, etapa do calendário; hierárquica, com datas |
| C.PRG | Program / GradeLevel | D1 | etapa, modalidade, série/ano, curso |
| C.SUB | Subject / CurricularComponent | D1/D4 | disciplina, componente curricular |
| C.GRP | Group | D1 | turma (acadêmica) **ou** grupo de aprendizagem (flexível); atributo `kind` |
| C.OFR | Offering / Section | D1 | componente oferecido a um grupo num período, com profissionais e horário |
| C.SCH | Schedule / Meeting | D1 | horário, sessão, evento |
| C.PER | Person | D1/D3 | dados pessoais mínimos |
| C.LRN | Learner (papel) | D3 | |
| C.STF | Staff (papel) | D1 | professor, profissional de apoio, gestor |
| C.GRD | Guardian / Relationship | D1 | responsável e vínculo |
| C.ENR | Enrollment | D1 | vínculo pessoa × (org, programa, grupo, oferta) com vigência e situação |
| C.CFW | CompetencyFramework | D2/D4 | documento curricular versionado (BNCC, CCSS…) |
| C.CMP | CompetencyItem | D2/D4 | competência, habilidade, objetivo, objeto de conhecimento |
| C.CAS | CompetencyAssociation | D2/D4 | pré-requisito, equivalência, alinhamento, hierarquia |
| C.ASM | Assessment / Instrument | D5 | instrumento, prova, protocolo |
| C.ITM | AssessmentItem | D5 | |
| C.RES | Result / Score | D5 | resultado, nível de desempenho, escala |
| C.EVD | Evidence / Observation | D3/D5 | |
| C.ACT | LearningActivity / Resource | D6 | atividade, jogo, recurso |
| C.EVT | LearningEvent | D6 | evento de interação (telemetria) |
| C.SUP | SupportNeed / Accommodation | D7 | necessidade, barreira, recurso de apoio, adaptação; sem reduzir a diagnóstico |
| C.PLN | IndividualPlan | D7 | PEI / plano de AEE e equivalentes |
| C.CRD | Credential / Achievement | D3 | |
| C.IDN | Identifier | D8 | identificador externo com `scheme` (INEP, CPF, UPN, etc.) |
| C.CNS | Consent / LegalBasis | D8 | |
| C.PRV | Provenance | D8 | origem, versão, data, sistema-fonte |
| C.VOC | ControlledVocabulary / Code | D8 | conjunto de códigos versionado (SKOS) |

Tipos de equivalência no crosswalk: **exata**, **aproximada**, **parcial** (cobre parte), **mais ampla**, **mais restrita**, **inexistente**.
