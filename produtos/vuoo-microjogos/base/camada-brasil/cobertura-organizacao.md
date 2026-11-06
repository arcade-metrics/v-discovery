# Cobertura por domínio: frente organização e dados (Brasil)

Escala do briefing §6.4: **Completa**, **Parcial**, **Indireta**, **Ausente**, **Não verificada**. Só as referências desta frente. Justificativas resumidas; fontes em [evidencias-organizacao.md](evidencias-organizacao.md). Acesso: 2026-11-05.

| Referência | D1 Organização | D2 Aprendizagem | D3 Estudante | D4 Currículo | D5 Avaliação | D6 Experiência | D7 Inclusão | D8 Interoperabilidade |
|---|---|---|---|---|---|---|---|---|
| Censo Escolar / Educacenso 2026 ([fichas/educacenso.md](fichas/educacenso.md)) | Completa | Ausente | Parcial | Indireta | Indireta | Ausente | Parcial | Parcial |
| Identificadores ([fichas/inep-identificadores.md](fichas/inep-identificadores.md)) | Indireta | Ausente | Parcial | Ausente | Ausente | Ausente | Ausente | Completa |
| LDB ([fichas/ldb.md](fichas/ldb.md)) | Completa | Ausente | Indireta | Parcial | Parcial | Ausente | Parcial | Ausente |
| EducaDados / LC 220 ([fichas/educadados.md](fichas/educadados.md)) | Indireta | Ausente | Indireta | Ausente | Indireta | Ausente | Ausente | Parcial |
| MEC Gestão Presente + API v2 ([fichas/mec-gestao-presente.md](fichas/mec-gestao-presente.md)) | Completa | Ausente | Parcial | Indireta | Parcial | Ausente | Parcial | Completa |
| CMDEB ([fichas/cmdeb.md](fichas/cmdeb.md)) | Completa | Ausente | Parcial | Indireta | Parcial | Ausente | Parcial | Parcial |
| SED-SP ([fichas/sed-sp.md](fichas/sed-sp.md)) | Não verificada | Ausente | Não verificada | Ausente | Não verificada | Ausente | Não verificada | Parcial |

## Justificativas

| Referência | Domínio | Por quê |
|---|---|---|
| Censo | D1 Completa | escola, mantenedora, vinculação, turma (tipo, mediação, horário, etapa, organização), vínculos de gestor, profissional e aluno; ano letivo |
| Censo | D3 Parcial | identidade, vínculos e situação anual; sem frequência, notas, histórico intra-ano |
| Censo | D4 Indireta | só marca componentes oferecidos por turma e por docente |
| Censo | D5 Indireta | rendimento anual (aprovado/reprovado) e recursos para o Saeb |
| Censo | D7 Parcial | deficiência/TEA/AH-SD, transtornos, recursos, AEE, classe especial, bilíngue, acessibilidade física (reg. 10) |
| Censo | D8 Parcial | leiaute, regras de validação, resolução de identidade; sem API, sem schema formal |
| Identificadores | D8 Completa | formatos, emissores, unicidade e regra de resolução documentados; publicidade só parcialmente |
| LDB | D1 Completa | níveis, etapas, formas de organização, carga, dias, frequência, sistemas |
| LDB | D4/D5 Parcial | base comum + parte diversificada; avaliação contínua, recuperação, frequência para aprovação |
| EducaDados | D8 Parcial | normas de princípio (Inue, conjuntos mínimos, padrão, plataforma), sem especificação técnica publicada |
| Gestão Presente | D1 Completa | turma com turno, vagas, datas, organização; instituição; profissional × rede × turma × componente |
| Gestão Presente | D3 Parcial | matrícula com datas e situação, frequência mensal, avaliação por componente; sem trajetória completa documentada |
| Gestão Presente | D5 Parcial | resultado por componente com 10 sistemas de avaliação |
| Gestão Presente | D8 Completa | OpenAPI 3.1 pública, autenticação, lotes, pré-validação |
| CMDEB | D8 Parcial | modelo de informação com tipos e categorias; sem serialização própria (a API a define) |
| SED-SP | D8 Parcial | só o RA e o processo de unificação foram verificados |

## Lacunas desta frente

- Leiaute da Situação do Aluno 2026: não publicado em 2026-11-05 (usado o de 2025).
- Dicionário dos microdados do Censo: não lido (ZIP não baixado).
- Texto integral da Portaria MEC 234/2025: não lido.
- Padrão Nacional de Interoperabilidade da Educação (Portaria 269 arts. 9–11): não publicado.
- Outros estados além de SP: não pesquisados.
