---
titulo: Insumos do projeto VUOO e CIATec
escopo: projeto
status: congelado (IN-01 a IN-35); novos insumos a partir de IN-36
atualizado_em: 2026-10-29
---

# Insumos: o que os projetos já decidiram

> **Independência do produto (2026-11-05).** O produto VUOO é independente destes projetos e começa do zero. Os insumos abaixo são **contexto e inspiração**, não restrições: valem para o produto só quando uma decisão de produto (`D-nn`, `RN-nn`, `ADR-nn`) os adota explicitamente.

Este arquivo extrai dos dois documentos-fonte (`projeto/vuoo.md`, proposta PIPE-TC Fase 2; `projeto/ciatec.md`, proposta CCD/FAPESP) o que as propostas diziam sobre o produto. Cada item cita a fonte. Quando o item traz uma implicação tirada pelo estudo, e não dita pela fonte, ela vem marcada **[DERIVADO]**. As decisões que derivam destes insumos ficam em `produtos/`, sempre referenciando o código do insumo (ex.: `[IN-07]`).

> **Códigos.** Os códigos IN-01 a IN-35 estão congelados: nunca mudam de número nem de sentido. Correções entram como nota no próprio item; insumos novos entram no fim, a partir de IN-36, com a data.

## Como os dois projetos se conectam

| | CIATec (CCD, 5 anos) | VUOO (PIPE-TC, 24 meses) |
|---|---|---|
| Quem faz | USP/EACH + consórcio (SEDUC-SP, SEDPcD-SP, APAEs, Exeter…) | Wemoga, com CIATec como instituição cooperada |
| O que entrega | Plataforma aberta de jogos colaborativos adaptativos, 4 jogos iniciais, TEA como referência | Plataforma comercial: gêmeo digital + VUOO Bot + micro-atividades + interface do professor |
| Natureza | Ciência aberta, uso gratuito, interesse público | SaaS B2G/B2B, R$ 9,50/estudante/mês (a validar) |
| Ponte | Instrumentos cognitivo-motores validados pelo grupo | Migra esses instrumentos para formato gamificado na escola |

**Leitura:** o CIATec é a fonte de ciência e a chancela; o VUOO é o produto que chega à escola. A linguagem visual é do **VUOO**, com o CIATec/USP e a FAPESP como endosso.

## Insumos

### Público e posicionamento
- **[IN-01] Faixa etária e público:** 1º ao 5º ano, 6 a 12 anos, rede estadual de SP (ciatec §1). O VUOO fala em "anos iniciais", com entrada pela rede pública (B2G) e expansão para redes privadas (B2B) (vuoo §7).
- **[IN-02] Turma inteira, não só educação especial.** Perspectiva transdiagnóstica, DUA, "a plataforma atende a turma inteira". A educação especial é a porta de entrada legal, não o público exclusivo. (vuoo resumo, §7)
- **[IN-03] Neurodivergências contempladas:** TEA, TDAH e dificuldades específicas de aprendizagem (vuoo PP1); o CIATec usa o TEA como modelo de referência (ciatec §1).
- **[IN-04] Sem rótulo diagnóstico.** "sem rotular o aluno" (ciatec, justificativa); a base operacional "não armazena laudos nem rótulos diagnósticos"; padrões atípicos são comunicados "como sinais pedagógicos, **com orientação de encaminhamento** e sem rotulagem" (vuoo, ética). [DERIVADO] **Nenhuma superfície do produto pode diferenciar crianças neurodivergentes das demais; e todo sinal ao professor precisa vir com orientação de encaminhamento.**
- **[IN-05] Posicionamento educacional, não clínico.** "sem caráter clínico-terapêutico" (ciatec OE9); "posicionamento educacional e não clínico" preserva liberdade de operação (vuoo §5). [DERIVADO] **A linguagem não pode parecer de saúde, terapia ou diagnóstico.**

### Dispositivo e contexto de uso
- **[IN-06] Smartphone primeiro.** "Redesenho dos instrumentos para smartphone" (vuoo F1.2); "operar em qualquer escola com acesso a smartphones" (vuoo §4). CIATec prevê web + Android/iOS para smartphones e tablets (ciatec §2.1).
- **[IN-07] PWA/app, uso offline, WCAG.** (vuoo F3.1)
- **[IN-08] Uso em sala, em rotina diária**, também em casa e outros ambientes (ciatec §1: "escolas, residências, centros esportivos e culturais").
- **[IN-09] Aplicação sem mediação especializada.** O estudante precisa entender a atividade sem um especialista ao lado (vuoo resumo, OE1).

### VUOO Bot (companheiro)
- **[IN-10] Companheiro digital adaptativo** que entrega "micro-atividades calibradas ao perfil cognitivo-motor" (vuoo resumo).
- **[IN-11] Quatro comportamentos adaptativos já nomeados: espelhar, provocar, celebrar, recuar.** (vuoo F3.1) — a personalidade do Bot precisa acomodar os quatro.
- **[IN-12] "Mediação sem dependência de linguagem verbal."** (vuoo F3.1) — o Bot precisa se comunicar por expressão, gesto, som e pictograma, não só por texto/fala.
- **[IN-13] Animatrônica física.** A Wemoga **apoia** um projeto de animatrônica **do grupo CIATec**, com impressão 3D e "conexão direta ao companheiro digital proposto no PP3" (vuoo §9b, §9c). [DERIVADO] O Bot deve ser compatível com fabricação em 3D: formas simples, poucos graus de liberdade, expressão em tela/luz. A titularidade do personagem não está prevista no acordo de PI (F1.1).
- **[IN-14] O Duolingo é citado como referência de retenção e de "mascote como diferencial central de marca"**, e criticado por "engajamento sem substância cognitiva mensurável; sem inclusão; mediação superficial" (vuoo Tabela 3).

### Micro-atividades
- **[IN-15] Dupla camada:** curricular (BNCC) + cognitivo-motora (instrumentos do CIATec). (vuoo OE5, F3.2)
- **[IN-16] Construtos medidos:** funções executivas — planejamento, controle inibitório, flexibilidade cognitiva, memória de trabalho (vuoo §4); tempo de reação e lei de Fitts (OpenBubble, vuoo §6a); tempo de hesitação, sequência de decisões, padrões de erro (vuoo §4); variáveis atencionais por eye/head tracking (Wemoga Eye).
- **[IN-17] A gamificação não pode distorcer a medição.** O PP3 testa se "a adaptação do VUOO Bot aumenta o engajamento sem comprometer essa captura", com critério de preservação da correlação com o instrumento de referência nas duas variantes (vuoo PP3). O A/B do PP3 compara **Bot adaptativo × versão sem adaptação** (40 por variante). [DERIVADO] **Restrição de design mais importante deste estudo:** nada da linguagem pode alterar o estímulo ou a resposta medida. Os instrumentos são aplicados no PP1 em versão gamificada "por aplicador treinado", com "normalização das variáveis de captura" e "parecer de preservação dos construtos" (F1.2, E1.3).
- **[IN-18] CMS para gestão e expansão do repertório** (vuoo F3.2) — a linguagem precisa ser um sistema de componentes e templates, não peças únicas.
- **[IN-19] Jogos colaborativos.** O CIATec propõe "jogos colaborativos acessíveis" e cita evidência de que jogos colaborativos com mediador (professor ou IA) favorecem interação entre crianças com TEA e colegas (ciatec §1). O VUOO não menciona colaboração explicitamente — **ponto de tensão a resolver**.
- **[IN-20] Quatro Pilares (Delors): aprender a conhecer, a fazer, a conviver, a ser.** Organizam os temas dos jogos (ciatec Tabela 2).

### Professor, gestor e família
- **[IN-21] Interface do professor com saídas para o PEI**, relatórios, alertas de risco, consultas em linguagem natural com "caminho de evidência recuperável" (vuoo PP2, F4.2).
- **[IN-22] Letramento digital variável:** o estudo do PP4 estratifica por letramento digital e exige que as saídas sejam "compreensíveis e acionáveis independentemente do nível de letramento digital do professor" (vuoo §4).
- **[IN-23] Gestor e secretaria:** painel de rede, exportação para prestação de contas (vuoo F4.2).
- **[IN-24] Família:** "fortalecendo o vínculo entre dados escolares, familiares e comunitários" (ciatec resumo). Não há interface de família especificada.

### Pesquisa e variação
- **[IN-25] O CIATec prevê testes A/B/n com "cinco interfaces visuais distintas, dois tipos de feedback e dois sistemas de progressão"** (ciatec §3.2.5). [DERIVADO] A linguagem visual precisa ser parametrizável por tokens. O desenho do A/B/n é do CIATec; este estudo só pode propor.
- **[IN-26] O estudo de prova de conceito menciona "classificações"** e o de mundo real, "sistemas de classificação dinâmicos" (ciatec §3.2.4–5). **Tensão** com a recomendação de não usar rankings entre crianças: pergunta ao CIATec.
- **[IN-27] Métricas internas previstas:** taxa de acerto, tentativas, erro médio, abandono, interações por minuto (ciatec §3.2.3); conclusão, tempo em tarefa, retorno em sessões subsequentes (vuoo PP3).
- **[IN-28] Triagens de saúde mental:** o estudo transversal do CIATec aplica SDQ, RCADS e PANAS como triagens (ciatec §3.2.2), sem desenho pré/pós declarado. [DERIVADO] Recomenda-se usá-las como contra-indicador da gamificação.

### Institucional e legal
- **[IN-29] LGPD art. 14**, dados de crianças, pseudonimização, minimização (vuoo, ética).
- **[IN-30] Ciência aberta.** A plataforma do CIATec é aberta, de uso gratuito mediante aprovação do comitê gestor, e o uso comercial deve respeitar "as licenças e a governança do projeto" (ciatec, Aplicações comerciais). O VUOO é produto comercial. [DERIVADO] Os jogos do CIATec não podem ficar presos ao SaaS pago.
- **[IN-31] Missão do CIATec:** "inclusão com sentido, consciência e equidade"; "transformar as relações entre tecnologia, ser humano e sociedade".
- **[IN-32] Título do VUOO fala em "trajetórias educacionais".** A metáfora de trajetória já está no nome do projeto.
- **[IN-33] O CIATec quer identificar padrões associados ao TEA.** A proposta prevê "um modelo de IA capaz de identificar, ao longo das atividades, padrões específicos que podem ser associados ao TEA" e, no futuro, "apoio diagnóstico" (ciatec §1, Aplicações comerciais). Isso tensiona [IN-04] e [IN-05]. [DERIVADO] Inferência associada a condição fica restrita à base de pesquisa e nunca chega a nenhuma interface (criança, professor, gestor, família).
- **[IN-34] Gêmeo produz faixas por idade e o PP4 mede identificação de risco.** O gêmeo classifica "abaixo, dentro e acima do esperado para a idade" (vuoo PP2); o PP4 tem como critério "redução de 30% ou mais no tempo até a identificação do risco" e a acurácia dessa identificação. [DERIVADO] O painel precisa permitir dizer a faixa sem rotular.
- **[IN-35] Precisão dos alertas é métrica do PP5**, "medida pela proporção confirmada pelo professor responsável". [DERIVADO] Todo sinal precisa de um gesto de confirmação.

## Lacunas que estes documentos não resolvem

Estas entram como `[ASSUMIDO]` nos estudos de produto:

1. Se o VUOO e o CIATec vão compartilhar a mesma plataforma de jogos ou se o CIATec terá identidade própria nos seus 4 jogos.
2. Se haverá uso individual (cada criança no seu aparelho) ou compartilhado (um tablet por dupla/grupo) — muda tudo na colaboração.
3. Se a criança lê. No 1º ano, grande parte não lê com fluência; isso define o peso de áudio e pictograma.
4. Se haverá fone de ouvido em sala.
5. Se existe interface de família no escopo do PIPE.
