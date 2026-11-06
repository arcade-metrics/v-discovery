# Ficha: Resolução SEDUC-SP 129/2025 (educação especial na rede estadual paulista)

> **Achado novo** em relação a `conhecimento/`, que só registrava a existência desta resolução (via PDL 30/2025 da ALESP) sem ter aberto o texto. Lida nesta sessão no PDF publicado no repositório de mídias da Seduc-SP (`midiasstoragesec.blob.core.windows.net/001/2025/11/resoluo-seduc-n-129.pdf`). Acesso: 2026-11-05.

```yaml
id: br.sp.resolucao-seduc-129-2025
name: "Resolução SEDUC nº 129, de 30 de setembro de 2025: regulamentação da Política de Educação Especial do Estado de São Paulo e do Plano Integrado para Pessoas com TEA"
acronym: Res. SEDUC 129/2025
jurisdiction: Estado de São Paulo (rede estadual)
issuing_organization: Secretaria da Educação do Estado de São Paulo
reference_type: regulamento (resolução de secretaria) com formulários anexos
domain: [D7, D3, D5, D4]
official_url: https://midiasstoragesec.blob.core.windows.net/001/2025/11/resoluo-seduc-n-129.pdf
repository_url: not_found
version: "30/09/2025; publicada no DOE em 03/10/2025 (data de publicação segundo acs.br.pneepei-and-aee/ALESP)"
publication_date: 2025-10-03
last_updated: unknown
legal_status: em vigor desde a publicação (art. 35); revoga a Res. SEDUC 21/2023 (art. 34); objeto do PDL 30/2025 na ALESP que pretende sustá-la (andamento não verificado)
mandatory_scope: escolas da rede estadual de SP e seus servidores (art. 33 prevê apuração de responsabilidade)
education_levels: [EF, EM (rede estadual); inclui Programa Ensino Integral]
geographic_scope: SP
language: pt-BR
license: unknown
technical_formats: [PDF; formulários em DOCX publicados como "documentos orientadores" (não abertos)]
api_available: false
data_model_available: parcial (formulários com campos: Anexos II a V)
ontology_available: false
schemas_available: false
implementation_examples: [Secretaria Escolar Digital (SED) como sistema de registro]
related_standards: [br.sp.decreto-67635, br.aee-pneepei, br.portaria-mec-421-2026, br.sp.curriculo-paulista, br.lei-12764-tea]
entities: [estudante elegível, Estudo de Caso (= API), nível de apoio (1, 2, 3), PAEE, PEI (por componente e bimestre), Relatório de Acolhimento, Orientação e Retorno bimestral aos Pais, professor especializado, professor do Projeto Ensino Colaborativo, profissional de apoio escolar, sala de recursos, modalidade itinerante]
relationships: [Estudo de Caso → PAEE (estudante); PAEE → PEI (por componente curricular × bimestre) → habilidades do Currículo Paulista; Relatório bimestral → PAEE]
vocabularies: [níveis de apoio 1–3 com descrição; categorias de elegibilidade; hipóteses de escrita (pré-silábico, silábico, silábico-alfabético, alfabético); tipos de apoio do profissional]
core_relevance: muito alta: único formulário oficial de PEI encontrado com campos concretos, e liga o plano ao currículo e ao bimestre
regional_adapter_relevance: muito alta (prioridade SP)
limitations: [anterior à Port. MEC 421/2026 (prazo de adequação até 2029); mantém laudo em alguns fluxos (ver abaixo); contestada politicamente]
open_questions: [Q-INC-02, Q-INC-03, Q-INC-07, Q-INC-08]
sources: [E-30]
access_date: 2026-11-05
research_status: verificado (texto integral lido)
```

## Regras que viram dado

| Regra | Dispositivo |
|---|---|
| API (Decreto 67.635) "está compreendida nesta Resolução como Estudo de Caso" | art. 14 |
| Estudo de Caso para todos os elegíveis, consolidado em relatório pedagógico que subsidia o PAEE | art. 14 §2 |
| Para todos os elegíveis, além do PAEE, um **PEI** com plano de acessibilização curricular e "medidas individualizadas de acesso ao currículo" | art. 14 §3 |
| PAEE pelo professor especializado; PEI pelo **professor regente ou de componente**, com apoio do especializado | art. 14 §4; art. 23, V, f |
| Documentação **atualizada bimestralmente** e apresentada aos pais | art. 14 §5 |
| Estudo de Caso e PAEE concluídos em **30 dias letivos** após o início da frequência, prorrogável com justificativa | art. 5 §2 |
| Estudo de Caso "de forma excepcional" para estudantes "em hipótese diagnóstica ou em processo de investigação" | art. 15, II |
| AEE para estudante sem laudo conclusivo: por professor especializado "sem direcionamento da especificidade"; após 1 ano, a escola convoca responsáveis para comprovar "continuidade do acompanhamento médico e a busca pelo laudo conclusivo" | art. 18, I e IV |
| Abertura de sala de recursos exige, entre outros, laudo médico "nos casos em que a qualificação do atendimento… deva ser indicada" | art. 9, I, h |
| Diretor zela pelos documentos na SED: "nível de apoio pedagógico, laudo, ou documento equivalente, hipótese diagnóstica, ata de reunião da família…, Estudo de Caso, PAEE" | art. 23, IV, c |
| Elegíveis identificados a partir da "indicação de deficiência já registrada na Secretaria Escolar Digital" | art. 5, I, c; II, a |

**Tensão normativa** [I]: a regra federal posterior (Port. MEC 421/2026 art. 7 §4; Dec. 12.686 art. 11 §7) veda condicionar matrícula, escolarização e AEE a laudo. A resolução paulista **oferece** AEE sem laudo (art. 18), mas condiciona a especialidade do professor ao laudo e exige comprovação de busca do laudo após um ano. O adaptador SP precisa representar `laudo` como documento opcional anexado, com efeitos administrativos locais, sem que o Core dependa dele. Registrado como Q-INC-07.

## Formulários (Anexos II a V): campos

**Anexo II – Estudo de Caso**: I. dados gerais (nome, nascimento, idade, escola, ano/série, turno, endereço, responsáveis, contato de emergência; elegibilidade em caixas: DI, DV, DF, DA, surdocegueira, deficiência múltipla, AH/SD, TEA, outros); II. **Nível de Apoio** 1, 2 ou 3 (descrições funcionais); III. informações do estudante (gosta da escola, amigos, atividades preferidas e desafiadoras, como expressa necessidades, satisfação com apoios); IV. informações da escola (participação, interesses, desempenho, potencialidades e desafios, envolvimento da turma, **barreiras** "comunicacionais, arquitetônicas, atitudinais ou outras"); V. informações da família (expectativas, autorregulação, particularidades, acompanhamento clínico/terapêutico com especialidade, profissional, contato e **autorização para a escola contatá-lo** SIM/NÃO); VI. observação do professor especializado (hipótese de escrita; Libras/Braille básico-intermediário-avançado; quatro operações; comportamentos repetitivos; hiperfoco; comunicação e CAA; motor fino/amplo; recursos de acessibilidade); VII. assinaturas (diretor, coordenador, professor especializado).

**Anexo III – PAEE**: identificação (inclui sexo), escolaridade, elegibilidade, nível de apoio; relato do estudo de caso; apoios, recursos e serviços (recursos pedagógicos/acessibilidade/TA; professor de Libras ou interlocutor; instrutor-mediador ou guia-intérprete; profissional de apoio com 7 funções: alimentação, higiene, locomoção, autocuidado, mediação das atividades, comunicação e interação, socialização); motivos; **habilidades a desenvolver no AEE**; estratégias; **planejamento por bimestre (1º a 4º)**; orientações ao regente, ao ensino colaborativo e à equipe; materiais e TA; itens a adquirir via PDDE-Paulista; **medidas para superar as barreiras**; assinaturas e ciência do responsável.

**Anexo IV – PEI**: estudante, professor regente, professor especializado, **componente curricular**, **bimestre**; "Quais conteúdos e habilidades do Currículo da Rede Estadual Paulista serão desenvolvidos no bimestre?"; estratégias, intervenções e recursos de acessibilidade; **instrumentos para acompanhar o aprendizado**; vídeos, livros, jogos e atividades indicados; assinaturas.

**Anexo V – Relatório de Acolhimento e Retorno bimestral**: acolhimento (apresentação do estudo de caso, apoios, "objetivos e Metas do PAEE", frequência do atendimento, orientações para casa); alinhamento bimestral (objetivos do período, metodologias, **progressos**, desafios, próximas intervenções); assinaturas incluindo o responsável.

### Leitura para o Core [I]

- O PEI paulista é **uma instância por (estudante, componente, bimestre)** e referencia habilidades do Currículo Paulista: `C.PLN` → `C.CMP` é relação de primeira classe, com período (`C.SES`) e oferta (`C.OFR`).
- "Nível de apoio" 1–3 é uma **intensidade de apoio** descrita em termos funcionais, sem diagnóstico; bom candidato para `C.SUP.intensidade` (vocabulário local SP, sem equivalência garantida com escalas como SIS-C, ver acs.asmt.barriers-and-support-needs).
- O formulário mistura dado pedagógico, dado de saúde (acompanhamento clínico, hipótese diagnóstica) e contatos de terceiros: classificação por campo é necessária (ver lgpd-educacao.md).
- A "autorização para a escola contatar profissionais" é um consentimento de compartilhamento registrado no próprio plano: `C.CNS` ligado a `C.PLN`.
