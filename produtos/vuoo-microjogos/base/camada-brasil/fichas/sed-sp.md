# Ficha curta: Secretaria Escolar Digital (SED) – São Paulo, e o que varia por estado/município

```yaml
id: br.sp.sed
name: Secretaria Escolar Digital (SED) da Secretaria da Educação do Estado de São Paulo
acronym: SED / RA
jurisdiction: Brasil – São Paulo (estadual)
issuing_organization: Secretaria da Educação do Estado de São Paulo (SEDUC-SP)
reference_type: sistema de gestão escolar estadual (registro administrativo oficial da rede estadual)
domain: [D1, D3, D8]
official_url: not_found (portal sed.educacao.sp.gov.br não consultado; fontes são POPs e tutoriais da SEDUC-SP)
repository_url: not_found
version: "POP.URENT1.2005 (publicado em jun/2026)"
publication_date: 2026-06
last_updated: unknown
legal_status: "sistema oficial da rede estadual de SP; ato normativo que o institui: not_found"
mandatory_scope: "rede estadual de SP; uso por redes municipais e escolas privadas de SP: unknown"
education_levels: [ensino fundamental, ensino médio, EJA (rede estadual)]
geographic_scope: São Paulo
language: pt-BR
license: not_found
technical_formats: unknown
api_available: not_found
data_model_available: not_found
ontology_available: não
schemas_available: not_found
implementation_examples: not_found
related_standards: [br.inep.censo-escolar, br.identificadores-educacionais]
entities: [Aluno (RA), Matrícula, Classe, Escola, Ficha do aluno]
relationships: "aluno 1 RA (duplicidades tratadas por unificação: escolhe-se o RA principal, movem-se as matrículas e exclui-se o duplicado)"
vocabularies: not_found
core_relevance: baixa
regional_adapter_relevance: média (SP é prioridade; RA é o identificador que escolas estaduais de SP usam no dia a dia)
limitations: "fontes operacionais (POP de unidade regional, tutoriais), não normativas; sem documentação de API"
open_questions: [Q-13]
sources: [E40, E41]
access_date: 2026-11-05
research_status: parcial (ficha curta)
```

## Achados (E40)

- **RA (Registro do Aluno)**: "número único de identificação do estudante na rede estadual de ensino de São Paulo, utilizado para registro, controle e acompanhamento de sua vida escolar".
- O RA é informado com **dígito e UF** (ex.: na troca de RA, "inserir o número do RA, com dígito e UF").
- Duplicidade de RA é tratada por processo administrativo: conferência de nome, CPF e nascimento; escolha do "RA principal" (preferencialmente o com mais registros); troca das matrículas para o principal; exclusão do duplicado por perfil restrito.
- Recomendação do próprio POP: priorizar o CPF no cadastro; redobrar a conferência para estudantes sem CPF (estrangeiros, menores).
- Estrutura administrativa: escolas → Unidades Regionais de Ensino (URE) → SEDUC; a Tabela de Órgãos Regionais do INEP 2026 tem 108 linhas para SP (E04) [I: correspondência URE × órgão regional INEP não verificada].

## O que varia por estado/município (registro de alto nível) [I salvo indicação]

| Tema | Onde varia | Base |
|---|---|---|
| Calendário escolar (datas, dias letivos acima do mínimo) | por sistema/escola | LDB art. 23 §2 (E20) |
| Forma de organização (ciclos, séries) e regras de progressão/reclassificação | por sistema e regimento escolar | LDB arts. 23–24; Caderno 2ª etapa sobre dependência "estabelecida no regimento escolar e nas normas do respectivo sistema" (E10 §5.2) |
| Escala de avaliação | por rede (o CMDEB tem 10 sistemas de avaliação) | E31 |
| Órgãos regionais | por UF (Tabela de Órgãos Regionais) | E04 |
| Identificador local do aluno (RA em SP; outros estados: not_verified) | por rede | E40 |
| Sistema de gestão (próprio, GPE do MEC, fornecedor) e forma de envio ao Censo (migração por arquivo ou digitação) | por rede/escola | E05, E34 |
| Carga horária semipresencial | Conselhos estaduais/municipais | Caderno 2026 p. 46 (E06) |
| Currículo estadual/municipal | por sistema | frente de currículo |
