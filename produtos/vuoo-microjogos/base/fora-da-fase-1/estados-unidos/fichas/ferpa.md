# Ficha: FERPA — Family Educational Rights and Privacy Act

> Verificação de cobertura: `conhecimento/` **não** cobre FERPA. O próprio legal-framework/comparison.md registra a lacuna ("A comparação não cobre o FERPA"), e gdpr-k-and-coppa.md só o cita como motivo de a FTC não finalizar a exceção escolar da COPPA. Ficha completa, com foco em **requisitos para o modelo de dados**.

```yaml
id: us.ferpa
name: Family Educational Rights and Privacy Act
acronym: FERPA
jurisdiction: Estados Unidos (federal)
issuing_organization: Congresso dos EUA (lei); U.S. Department of Education, Student Privacy Policy Office (regulamento e fiscalização)
reference_type: lei federal + regulamento
domain: [D8, D3]
official_url: https://studentprivacy.ed.gov/ferpa
repository_url: n/a
version: 20 U.S.C. §1232g (seção 444 do GEPA); 34 CFR Part 99, última emenda listada 76 FR 75641, 2011-12-02 [E27]
publication_date: 1974 (lei) — data da lei não lida em fonte primária nesta rodada
last_updated: 2011-12-02 (regulamento, última emenda listada) [E27]
legal_status: lei federal vinculante
mandatory_scope: agências e instituições educacionais que recebem fundos de programas do Departamento de Educação [I: condição de aplicabilidade da lei; texto de §99.1 não relido]
education_levels: K-12 e ensino superior
geographic_scope: EUA
language: inglês
license: domínio público (texto legal federal)
technical_formats: n/a
api_available: n/a
data_model_available: n/a (impõe atributos e registros)
ontology_available: n/a
schemas_available: n/a
implementation_examples: n/a
related_standards: [COPPA, PPRA, leis estaduais (SOPIPA etc.)]
entities: [education record, directory information, eligible student, parent, school official, legitimate educational interest, disclosure, record of disclosure, consent]
relationships: direitos dos pais transferem-se ao aluno elegível (18 anos ou ensino superior)
vocabularies: categorias de directory information definidas localmente por cada instituição
core_relevance: alta — exige no Core: classificação de atributos, opt-out, registro de divulgações, transferência de direitos por idade, base de acesso por papel+interesse
regional_adapter_relevance: obrigatória para operar nos EUA
limitations: eCFR bloqueado na sessão; texto lido na transcrição de studentprivacy.ed.gov
open_questions: Q14, Q15
sources: [E27, E28, E29]
access_date: 2026-11-05
research_status: verificado em fonte oficial (studentprivacy.ed.gov); eCFR não acessível
```

## Requisitos (34 CFR Part 99) [E27]

| Seção | Conteúdo | Requisito para o modelo de dados [I] |
|---|---|---|
| §99.3 education records | registros diretamente relacionados ao aluno e mantidos pela instituição ou por quem age por ela; exclui notas de memória de posse exclusiva, registros da unidade policial, registros de emprego, notas de provas corrigidas por colegas antes de recolhidas | marcar quais dados do VUOO são *education record* quando operado para a escola |
| §99.3 directory information | dado que "would not generally be considered harmful or an invasion of privacy if disclosed"; SSN nunca; ID de aluno só se não der acesso sem segundo fator | atributo `privacy_class` por campo, com valores definidos pela instituição |
| §99.3 eligible student | "has reached 18 years of age or is attending an institution of postsecondary education" | regra de transferência de direitos de C.GRD para C.LRN por idade/etapa |
| §99.3 PII | inclui identificadores indiretos (ex.: data de nascimento) e informação "linked or linkable to a specific student" | desidentificação deve considerar quase-identificadores |
| §99.7 notificação anual | direitos de inspecionar, emendar, consentir, reclamar; critérios de quem é *school official* e o que é *legitimate educational interest* | política publicada pela organização (C.ORG) |
| §99.10 inspeção | atender "within a reasonable period of time, but not more than 45 days"; registros não podem ser destruídos com pedido pendente | exportação por aluno; bloqueio de exclusão (legal hold) |
| §99.20–22 emenda | pedido de correção; audiência com decisão escrita | trilha de correção com proveniência (C.PRV) |
| §99.30 consentimento | escrito, assinado e datado: registros, finalidade, destinatários; eletrônico válido se autenticar o signatário | C.CNS com escopo (registros, finalidade, destinatário) |
| §99.31(a)(1) school official | acesso com interesse educacional legítimo; terceirizado qualifica se (1) executa serviço que a instituição faria com funcionários, (2) está "under the direct control of the agency or institution with respect to the use and maintenance of education records", (3) sujeito às limitações de redivulgação de §99.33(a); métodos razoáveis para limitar acesso (a)(1)(ii) | base legal do VUOO como fornecedor; controle de acesso por papel + finalidade |
| §99.31 outras exceções | transferência para outra escola (a)(2); autoridades (a)(3); estudos com acordo escrito (a)(6); emergência de saúde ou segurança (a)(10); directory information (a)(11); dados desidentificados (b)(1) | C.CNS com `legal_basis` enumerada pelo adaptador |
| §99.32 registro de divulgações | registrar cada pedido e divulgação de PII, partes e interesse legítimo, mantido junto ao registro do aluno; isentos: pais/aluno, school officials, consentidos, directory information; emergência exige registro da "articulable and significant threat" | **entidade de registro de divulgação** (sem alvo no Core provisório) |
| §99.37 directory information | aviso público com tipos, direito de opt-out e prazo; opt-out vale para ex-alunos até revogado; opt-out não impede uso do nome/ID/e-mail institucional em sala | flag de opt-out por pessoa, persistente após desligamento |

## Situação regulatória

Nenhuma emenda ao 34 CFR 99 posterior a 2011 aparece na transcrição oficial [E27]. Fonte secundária relata que a agenda regulatória do ED de julho de 2026 previa *negotiated rulemaking* sobre FERPA para setembro de 2026 [E29]; não verificado em reginfo.gov. A FTC adiou a regra escolar da COPPA para evitar conflito com mudanças no FERPA (ver `psg.legal.gdpr-k-and-coppa`).
