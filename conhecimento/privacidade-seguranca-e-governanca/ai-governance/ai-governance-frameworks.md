---
id: psg.ai.ai-governance-frameworks
titulo: Frameworks de governança de IA (NIST AI RMF, ISO/IEC 42001, UNICEF e UNESCO)
tipo: framework
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [nist2023airmf, nist2026airmfplaybook, nist2024ai6001, iso420012023, iso238942023, unicef2021aichildren, unesco2021ethicsai, unesco2023genaiguidance, unnews2023genaischools, eu2024aiact]
relacoes:
  - { tipo: complementa, alvo: psg.audit.privacy-risk-management }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: complementa, alvo: psg.ai.eu-ai-act-and-brazil }
  - { tipo: complementa, alvo: psg.ai.transparency-and-human-oversight }
  - { tipo: complementa, alvo: psg.ai.model-documentation }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: lae.psy.fairness-in-measurement }
  - { tipo: relacionado-a, alvo: adp.eval.evaluation-protocols }
termos: [governança de IA, AI RMF, GOVERN, MAP, MEASURE, MANAGE, perfil de uso, sistema de gestão de IA, AIMS, avaliação de impacto de sistema de IA, IA centrada na criança, human-AI configuration, confabulação]
---

# Frameworks de governança de IA

## Definição e terminologia

**Governança de IA** designa, neste documento, o conjunto de políticas, papéis, processos e evidências com que uma organização decide se, como e sob que controles um sistema de IA é desenvolvido, adquirido e usado, e como seus riscos são acompanhados ao longo do ciclo de vida [I]. Quatro referências organizam o tema e têm naturezas distintas: o **NIST AI RMF 1.0** é um framework técnico voluntário de gestão de riscos; a **ISO/IEC 42001:2023** é uma norma certificável de sistema de gestão; o guia do **UNICEF** e as duas publicações da **UNESCO** são orientações de política pública centradas em direitos, sem força vinculante [I]. Nenhuma delas é lei; as obrigações legais estão em `psg.ai.eu-ai-act-and-brazil` e, para dados pessoais, em `psg.legal.lgpd-children`.

O que este documento não cobre: a medição estatística de viés (fica em `lae.psy.fairness-in-measurement`), os protocolos de avaliação de modelos adaptativos (`adp.eval.evaluation-protocols`) e a gestão de riscos de privacidade (`psg.audit.privacy-risk-management`), à qual a governança de IA se acopla.

## Problema que resolve

Um sistema que modela o aprendiz, recomenda atividades ou sinaliza alunos em risco toma ou prepara decisões sobre crianças. Os riscos (erro, viés, opacidade, dependência excessiva do professor na saída, uso fora da finalidade) não são cobertos pela gestão de riscos de segurança nem pela de privacidade: o NIST observa que um sistema transparente "is not necessarily an accurate, privacy-enhanced, secure, or fair system" [F: nist2023airmf, §3.4]. Falta uma estrutura que distribua responsabilidades, defina o que medir e quando parar o sistema [I].

## Fundamentos e funcionamento

### NIST AI RMF 1.0 (NIST AI 100-1, jan. 2023)

O framework se declara "voluntary, rights-preserving, non-sector-specific, and use-case agnostic" [F: nist2023airmf, Executive Summary]. Define sete características de IA confiável: "valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed" [F: nist2023airmf, §3]. O núcleo tem quatro funções, GOVERN, MAP, MEASURE e MANAGE, divididas em categorias e subcategorias; GOVERN é transversal e as ações "do not constitute a checklist" [F: nist2023airmf, §5]. Subcategorias diretamente ligadas a este domínio:

- GOVERN 1.1: requisitos legais e regulatórios "are understood, managed, and documented" [F: nist2023airmf, Tabela 1].
- GOVERN 3.2: políticas que definem papéis "for human-AI configurations and oversight of AI systems" [F: nist2023airmf, Tabela 1].
- MAP 2.2: documentar os limites de conhecimento do sistema e "how system output may be utilized and overseen by humans" [F: nist2023airmf, Tabela 2].
- MAP 3.5: processos de supervisão humana "defined, assessed, and documented" [F: nist2023airmf, Tabela 2].
- MEASURE 2.9: o modelo "is explained, validated, and documented"; MEASURE 2.11: equidade e viés avaliados e documentados [F: nist2023airmf, Tabela 3].
- MANAGE 2.4: mecanismos e responsáveis para "supersede, disengage, or deactivate" sistemas com desempenho inconsistente com o uso pretendido [F: nist2023airmf, Tabela 4].

**Perfis de uso** são implementações das funções "for a specific setting or application" (o documento cita perfis de contratação e de moradia) [F: nist2023airmf, §6]; não há perfil educacional publicado pelo NIST entre os documentos consultados [I]. O **Playbook** traz ações sugeridas por subcategoria, é voluntário e "neither a checklist nor set of steps"; em 30/10/2026 a página informa que "The AI RMF 1.0 is being updated" e que o Playbook será revisto depois [F: nist2026airmfplaybook]. O **NIST AI 600-1** (jul. 2024) é um perfil transversal para IA generativa que lista doze riscos, entre eles confabulação ("confidently stated but erroneous or false content"), privacidade de dados e **human-AI configuration**, que inclui "automation bias, over-reliance, or emotional entanglement" [F: nist2024ai6001, §2].

### ISO/IEC 42001:2023 e ISO/IEC 23894:2023

A ISO/IEC 42001 "specifies the requirements and provides guidance for establishing, implementing, maintaining and continually improving an AI (artificial intelligence) management system" e se aplica a qualquer organização "that provides or uses products or services that utilize AI systems" [F: iso420012023, metadados, §1]. O sumário mostra uma avaliação de impacto de sistema de IA no planejamento (6.1.4) e na operação (8.4), um Anexo A normativo de objetivos de controle e controles e um Anexo B normativo de orientação de implementação [F: iso420012023, metadados]. A ISO/IEC 23894:2023 orienta organizações que "develop, produce, deploy or use" IA a gerir riscos específicos de IA [F: iso238942023, metadados]. O conteúdo dos controles não foi acessado.

### UNICEF, Policy Guidance on AI for Children 2.0 (nov. 2021)

O guia parte de uma fundação, "uphold children's rights", lida pelas lentes de proteção, provisão e participação, e propõe nove requisitos para IA centrada na criança, do apoio ao desenvolvimento e bem-estar até a criação de um ambiente propício [F: unicef2021aichildren, Executive summary]. O requisito 6, transparência, explicabilidade e responsabilização, pede linguagem adequada à idade e afirma que a IA não deve ser "the only input to determine key life decisions that impact children", citando expressamente "processing school applications", sem "a human-in-the-loop to make the final decision" [F: unicef2021aichildren, req. 6].

### UNESCO

A Recomendação sobre a Ética da IA foi adotada pelos 193 Estados-membros em novembro de 2021 e lista dez princípios, entre eles "Transparency and explainability" e "Human oversight and determination"; os sistemas não devem "displace ultimate human responsibility and accountability" [F: unesco2021ethicsai]. O guia de IA generativa na educação e pesquisa (set. 2023) propõe uma abordagem "human-agent and age-appropriate" para validação ética e desenho pedagógico [F: unesco2023genaiguidance]; segundo a cobertura da ONU, recomenda considerar "an age limit of 13" para uso em sala e que as instituições validem os sistemas antes do uso por estudantes [F: unnews2023genaischools].

## Vantagens e limitações

O AI RMF dá vocabulário e granularidade (subcategorias auditáveis) sem custo de licença; sua limitação é ser voluntário e genérico, exigindo um perfil próprio para educação [I]. A ISO/IEC 42001 permite certificação e integra-se a sistemas ISO de segurança e privacidade, mas o texto é pago e os controles não foram verificados aqui. UNICEF e UNESCO trazem o que os outros não têm, o foco em crianças e em sala de aula, mas não especificam evidências nem métricas [I]. Nenhuma das quatro substitui a avaliação jurídica: o AI Act, por exemplo, exige gestão de riscos que considere impacto sobre menores de 18 anos [F: eu2024aiact, art. 9(9)], requisito que um perfil NIST pode operacionalizar, mas não cria [I].

## Alternativas e comparações

| Critério | NIST AI RMF 1.0 | ISO/IEC 42001 | UNICEF 2.0 | UNESCO (2021, 2023) |
|---|---|---|---|---|
| Natureza | framework voluntário | norma certificável de sistema de gestão | orientação de política | recomendação e guia de política |
| Unidade de análise | sistema e ciclo de vida | organização (AIMS) | política pública e sistema | Estado e instituição de ensino |
| Foco em crianças | não específico | não verificado | central | presente (idade, validação) |
| Supervisão humana | GOVERN 3.2, MAP 3.5, MANAGE 2.4 | não verificado | human-in-the-loop em decisões-chave | "human oversight and determination" |
| Acesso | aberto | pago | aberto | aberto |

Uso combinado [I]: UNICEF e UNESCO definem o que proteger; o AI RMF, como mapear e medir; a ISO/IEC 42001, como manter isso como processo auditável.

## Exemplo técnico independente de domínio

Esboço de perfil de uso, no formato do AI RMF, para um sistema que recomenda atividades a menores [I]:

```
perfil: recomendador-educacional (alvo)
GOVERN 1.1  -> mapa legal: LGPD art. 14 e 20; AI Act Anexo III 3(b) se houver oferta na UE
GOVERN 3.2  -> papéis: professor supervisiona; coordenação aprova limiares; responsável recebe explicação
MAP 1.1     -> finalidade: sequenciar exercícios; fora de escopo: nota, retenção, laudo
MAP 3.5     -> supervisão: professor pode rejeitar qualquer recomendação; rejeições registradas
MEASURE 2.9 -> explicação local validada com professores; MEASURE 2.11 -> desempenho por subgrupo
MANAGE 2.4  -> gatilho de desligamento: queda de acurácia > limiar ou disparidade entre subgrupos
UNICEF req.6 -> explicação em linguagem para a idade; nenhuma decisão-chave sem humano
```

## Relações com outros conceitos

Complementa `psg.audit.privacy-risk-management` (estrutura análoga de funções) e `psg.audit.ripd-dpia` (a avaliação de impacto de IA e o RIPD compartilham insumos). Os requisitos legais estão em `psg.ai.eu-ai-act-and-brazil`; a supervisão humana e a explicação, em `psg.ai.transparency-and-human-oversight`; a evidência documental (MEASURE 2.9), em `psg.ai.model-documentation`. A medição exigida por MEASURE 2.11 fica em `lae.psy.fairness-in-measurement` e `adp.eval.evaluation-protocols`.

## Lacunas e questões abertas

- O texto da ISO/IEC 42001 (controles do Anexo A, método de 8.4) e o da ISO/IEC 23894 não foram acessados; a relação entre a avaliação de impacto de sistema de IA da 42001 e o RIPD da LGPD fica por verificar.
- A revisão anunciada do AI RMF 1.0 não tem data nem rascunho localizado em 30/10/2026.
- Os textos integrais das duas publicações da UNESCO não carregaram; o limite de 13 anos foi verificado apenas por notícia da ONU.
- Não foi localizado perfil AI RMF específico para educação ou para crianças.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| nist2023airmf | tecnico | 2026-10-30 |
| nist2026airmfplaybook | tecnico | 2026-10-30 |
| nist2024ai6001 | tecnico | 2026-10-30 |
| iso420012023 | normativo [metadados] | 2026-10-30 |
| iso238942023 | normativo [metadados] | 2026-10-30 |
| unicef2021aichildren | tecnico | 2026-10-30 |
| unesco2021ethicsai | normativo (página de resumo) | 2026-10-30 |
| unesco2023genaiguidance | tecnico (página de apresentação) | 2026-10-30 |
| unnews2023genaischools | secundario | 2026-10-30 |
| eu2024aiact | normativo (espelho) | 2026-10-30 |
