---
id: psg.ai.eu-ai-act-and-brazil
titulo: AI Act europeu (educação como alto risco) e PL 2338/2023 no Brasil
tipo: comparacao
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [eu2024aiact, eu2026omnibusai, pl23382023, camara2026pl2338tramitacao, brasil2018lgpd]
relacoes:
  - { tipo: complementa, alvo: psg.ai.ai-governance-frameworks }
  - { tipo: complementa, alvo: psg.ai.transparency-and-human-oversight }
  - { tipo: complementa, alvo: psg.ai.model-documentation }
  - { tipo: complementa, alvo: psg.audit.ripd-dpia }
  - { tipo: relacionado-a, alvo: psg.audit.audit-trails }
  - { tipo: relacionado-a, alvo: psg.legal.gdpr-k-and-coppa }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: lae.ind.dropout-and-risk-prediction }
termos: [AI Act, sistema de IA de alto risco, Anexo III, provider, deployer, instruções de uso, avaliação de impacto sobre direitos fundamentais, FRIA, Digital Omnibus, PL 2338/2023, avaliação de impacto algorítmico, avaliação preliminar]
---

# AI Act europeu e PL 2338/2023

## Definição e terminologia

O **Regulamento (UE) 2024/1689** (AI Act) classifica sistemas de IA por risco e impõe obrigações a quem os fornece (**provider**) e a quem os usa sob sua autoridade (**deployer**) [F: eu2024aiact, art. 3, via glossário do espelho]. O **PL 2338/2023** é o projeto brasileiro de marco legal da IA; usa os termos **desenvolvedor**, **distribuidor** e **aplicador** e **não é lei** em 30/10/2026 (situação abaixo). Este documento lê os dois textos a partir de uma pergunta: quando uma plataforma educacional que modela, recomenda ou sinaliza alunos cai no regime de alto risco, e o que isso exige.

Nota de fonte: o EUR-Lex não carregou nesta sessão; os artigos foram lidos no espelho AI Act Explorer, que exibe a redação consolidada com as alterações do Regulamento (UE) 2026/1744, o "Digital Omnibus on AI", adotado em 8/7/2026 e em vigor desde 27/7/2026 [F: eu2026omnibusai].

## Problema que resolve

Os frameworks voluntários (`psg.ai.ai-governance-frameworks`) não dizem quando a governança é obrigatória. A LGPD cobre o dado pessoal e a revisão de decisão automatizada (art. 20) [F: brasil2018lgpd, art. 20], mas não exige gestão de riscos do modelo, instruções de uso ao cliente escolar nem supervisão humana desenhada no sistema. O AI Act exige, e o PL 2338/2023 propõe exigências semelhantes [I].

## Fundamentos e funcionamento

### AI Act: quando a educação é alto risco

O art. 6(2) considera de alto risco os sistemas do Anexo III [F: eu2024aiact, art. 6(2)]. O ponto 3 do Anexo III, "Education and vocational training", lista: (a) sistemas para determinar acesso, admissão ou alocação em instituições; (b) sistemas "intended to be used to evaluate learning outcomes, including when those outcomes are used to steer the learning process of natural persons"; (c) avaliação do nível de educação adequado a que a pessoa terá acesso; (d) monitoramento e detecção de comportamento proibido em provas [F: eu2024aiact, Anexo III, 3]. [I] A alínea (b) alcança diretamente o modelo do aprendiz que avalia domínio e com isso dirige a sequência de atividades.

O art. 6(3) permite que um sistema do Anexo III não seja alto risco quando não representa risco significativo, por exemplo se executa "a narrow procedural task" ou "a preparatory task"; mas o sistema do Anexo III é "always" alto risco quando "performs profiling of natural persons" [F: eu2024aiact, art. 6(3)]. O provider que invoca a derrogação deve documentar a avaliação antes de colocar o sistema no mercado e registrá-lo [F: eu2024aiact, art. 6(4)]. [I] Como modelar o aprendiz para prever desempenho tende a configurar perfilamento no sentido do GDPR art. 4(4), ao qual o AI Act remete, a derrogação dificilmente se aplica a modelos adaptativos individualizados; a interpretação depende das diretrizes da Comissão previstas no art. 6(5).

### Obrigações principais

- **Gestão de riscos (art. 9)**: processo "continuous iterative" ao longo do ciclo de vida; o provider deve considerar se o sistema "is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups" [F: eu2024aiact, art. 9(2), 9(9)].
- **Transparência ao deployer (art. 13)**: instruções de uso com finalidade, acurácia e suas métricas, desempenho "regarding specific persons or groups of persons", capacidades "to provide information that is relevant to explain its output" e as medidas de supervisão do art. 14 [F: eu2024aiact, art. 13(3)]. Detalhado em `psg.ai.transparency-and-human-oversight` e `psg.ai.model-documentation`.
- **Supervisão humana (art. 14)**: o sistema deve poder ser "effectively overseen by natural persons" e permitir ao supervisor, entre outros, perceber o viés de automação e "disregard, override or reverse the output" [F: eu2024aiact, art. 14(1), 14(4)].
- **Deployer (art. 26)**: atribuir a supervisão a pessoas com "competence, training and authority"; monitorar o funcionamento; guardar os logs sob seu controle por período adequado, "of at least six months"; usar as informações do art. 13 na DPIA do art. 35 do GDPR; e, nos sistemas do Anexo III que decidem ou ajudam a decidir sobre pessoas, informá-las de que estão sujeitas ao sistema [F: eu2024aiact, art. 26(2), 26(5), 26(6), 26(9), 26(11)].
- **Avaliação de impacto sobre direitos fundamentais (art. 27)**: antes do primeiro uso, deployers que são "bodies governed by public law, or are private entities providing public services" avaliam processos, período e frequência de uso, categorias de pessoas afetadas, riscos específicos, implementação da supervisão humana e medidas de governança e reclamação; podem aproveitar a DPIA, e o AI Office deve oferecer um questionário-modelo [F: eu2024aiact, art. 27(1), 27(4), 27(5)]. [I] Redes públicas de ensino que usam sistemas do Anexo III 3 estão nesse grupo; o tema se liga a `psg.audit.ripd-dpia`.
- **Transparência ao usuário (art. 50)**: sistemas que interagem diretamente com pessoas devem informá-las de que interagem com IA [F: eu2024aiact, art. 50(1)].
- **Direito à explicação (art. 86)**: quem é afetado por decisão do deployer baseada em saída de sistema do Anexo III pode obter "clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken" [F: eu2024aiact, art. 86(1)].

### Calendário (art. 113, redação de 2026)

O regulamento entrou em vigor em 1/8/2024 e aplica-se em geral a partir de 2/8/2026; os capítulos I e II, desde 2/2/2025. Pela redação dada pelo Regulamento 2026/1744, as seções 1 a 3 do capítulo III aplicam-se a partir de **2/12/2027** para sistemas de alto risco do art. 6(2) e Anexo III e de 2/8/2028 para os do Anexo I [F: eu2024aiact, art. 113; eu2026omnibusai]. No espelho, os arts. 50 e 86 aparecem com aplicação desde 2/8/2026 [F: eu2024aiact, arts. 50 e 86].

### PL 2338/2023

**Situação** (consulta de 30/10/2026): aprovado pelo Plenário do Senado na sessão de 10/12/2024 e remetido à Câmara pelo Ofício SF nº 235, de 17/03/2025 [F: camara2026pl2338tramitacao]. Na Câmara, a Mesa criou em 04/04/2025 comissão especial por distribuição a mais de quatro comissões de mérito; o relator foi designado em 20/05/2025; o regime é de prioridade e a situação registrada na API de dados abertos é **"Aguardando Parecer"**, com última movimentação (apensações) em 27/10/2026 [F: camara2026pl2338tramitacao]. Não há parecer da comissão especial registrado.

**Conteúdo do texto do Senado** [F: pl23382023]:
- Alto risco por finalidade (art. 14), incluindo, no inciso II, sistemas usados "como fator determinante" na seleção de estudantes, "ou para avaliações determinantes no progresso acadêmico ou monitoramento de estudantes", ressalvado o monitoramento só para segurança; não é alto risco o uso como "tecnologia intermediária que não influencie ou determine resultado ou decisão" (art. 14, parágrafo único).
- Critérios para novas hipóteses incluem afetar grupo vulnerável e "impactar negativamente o desenvolvimento e a integridade física, psíquica ou moral de crianças e adolescentes" (art. 15, III e X).
- Direitos da pessoa afetada por IA de alto risco: explicação, contestação e "revisão humana das decisões" (art. 6), explicação gratuita em linguagem simples (art. 7), supervisão humana que permita "compreender, interpretar, decidir e intervir" (art. 8).
- Avaliação preliminar facultativa (art. 12) e avaliação de impacto algorítmico obrigatória para alto risco (art. 25); a Administração Pública deve registrar quem usou o sistema, para qual situação e finalidade (art. 23, I).
- Vigência de 730 dias após a publicação, com exceções (art. 80).

## Alternativas e comparações

| Critério | AI Act (UE) | PL 2338/2023 (texto do Senado) | LGPD (vigente) |
|---|---|---|---|
| Status | em vigor; alto risco do Anexo III a partir de 2/12/2027 | projeto na Câmara, aguardando parecer | em vigor |
| Gatilho educacional | avaliar resultados que dirigem a aprendizagem (Anexo III 3(b)) | avaliação "determinante" no progresso ou monitoramento (art. 14, II) | decisão unicamente automatizada que afete interesses (art. 20) |
| Supervisão humana | desenhada pelo provider, atribuída pelo deployer (arts. 14, 26) | direito e dever (arts. 6, III e 8) | revisão a pedido, sem exigir pessoa natural |
| Explicação | instruções ao deployer (art. 13) e explicação ao afetado (art. 86) | direito à explicação (arts. 6, I e 7) | critérios e procedimentos, ressalvado segredo (art. 20, §1) |
| Avaliação de impacto | gestão de riscos (art. 9) e FRIA para entes públicos (art. 27) | avaliação de impacto algorítmico (art. 25) | RIPD quando exigido |

[I] O PL é mais estreito no gatilho (exige caráter "determinante") e mais largo nos direitos individuais; o AI Act é mais detalhado nas obrigações técnicas do fornecedor.

## Exemplo técnico independente de domínio

Triagem regulatória de uma funcionalidade [I]:

```
para cada funcionalidade F:
  se F avalia resultado de aprendizagem e dirige a sequência -> candidato Anexo III 3(b)
  se F perfila o aluno (prevê desempenho, risco) -> derrogação do art. 6(3) indisponível
  se oferta na UE e alto risco -> art. 9, 13, 14 (provider); 26 e talvez 27 (escola)
  se F for "determinante" para progresso acadêmico -> alto risco no PL 2338 (se aprovado assim)
  sempre -> LGPD art. 20 se decisão unicamente automatizada afeta interesse do aluno
  registrar a triagem e sua data; revisar quando a lei ou a funcionalidade mudar
```

## Relações com outros conceitos

Complementa `psg.ai.ai-governance-frameworks` (os frameworks operacionalizam o que a lei exige), `psg.ai.transparency-and-human-oversight` (arts. 13, 14, 86 e LGPD art. 20) e `psg.ai.model-documentation` (instruções de uso). A FRIA dialoga com `psg.audit.ripd-dpia`; os logs do art. 26(6), com `psg.audit.audit-trails`. A comparação com o GDPR fica em `psg.legal.gdpr-k-and-coppa`. Alertas de evasão (`lae.ind.dropout-and-risk-prediction`) são o caso típico de perfilamento.

## Lacunas e questões abertas

- O texto oficial no EUR-Lex (AI Act e Regulamento 2026/1744) não carregou; a redação consolidada foi lida em espelho não oficial.
- Não foram consultadas as diretrizes da Comissão sobre o art. 6 nem os considerandos 56 e 61, que podem esclarecer o alcance de "steer the learning process".
- O texto que a Câmara vier a aprovar pode diferir do texto do Senado; os artigos citados podem mudar de número ou conteúdo.
- A relação entre a avaliação de impacto algorítmico do PL e o RIPD da LGPD não está definida no texto.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| eu2024aiact | normativo (espelho consolidado) | 2026-10-30 |
| eu2026omnibusai | normativo (espelho) | 2026-10-30 |
| pl23382023 | normativo (projeto de lei) | 2026-10-30 |
| camara2026pl2338tramitacao | tecnico | 2026-10-30 |
| brasil2018lgpd | normativo | 2026-10-30 |
