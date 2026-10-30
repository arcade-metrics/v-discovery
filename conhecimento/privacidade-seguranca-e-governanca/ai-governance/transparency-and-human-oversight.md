---
id: psg.ai.transparency-and-human-oversight
titulo: Transparência, explicabilidade e supervisão humana em decisões sobre aprendizes
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [brasil2018lgpd, eu2016gdpr, eu2024aiact, pl23382023, nist2023airmf, nist2024ai6001, unicef2021aichildren, khosravi2022explainable, conati2021personalized]
relacoes:
  - { tipo: depende-de, alvo: psg.audit.audit-trails }
  - { tipo: depende-de, alvo: psg.access.school-roles }
  - { tipo: complementa, alvo: psg.ai.model-documentation }
  - { tipo: complementa, alvo: psg.ai.eu-ai-act-and-brazil }
  - { tipo: complementa, alvo: adp.lm.open-learner-model }
  - { tipo: complementa, alvo: lae.ind.dashboards-and-olm }
  - { tipo: relacionado-a, alvo: lae.ind.dropout-and-risk-prediction }
  - { tipo: relacionado-a, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.legal.eca-and-digital-eca }
  - { tipo: parte-de, alvo: psg.ai.ai-governance-frameworks }
termos: [transparência, explicabilidade, interpretabilidade, explicação local, explicação contrafactual, decisão unicamente automatizada, revisão de decisão automatizada, supervisão humana, human-in-the-loop, viés de automação, override, segredo comercial]
---

# Transparência, explicabilidade e supervisão humana em decisões sobre aprendizes

## Definição e terminologia

O NIST distingue três características: **transparência** é o quanto a informação sobre o sistema e suas saídas está disponível a quem interage com ele; **explicabilidade** é "a representation of the mechanisms underlying AI systems' operation"; **interpretabilidade** é "the meaning of AI systems' output in the context of their designed functional purposes". Transparência responde "o que aconteceu", explicabilidade "como" e interpretabilidade "por que" e o que significa para o usuário [F: nist2023airmf, §3.4, §3.5]. **Supervisão humana** é a capacidade, desenhada no sistema e atribuída a pessoas, de entender, monitorar, desconsiderar, reverter ou interromper a saída [F: eu2024aiact, art. 14(4)].

Neste documento, **decisão sobre aprendiz** é qualquer saída do sistema que altere o que o aluno recebe ou como é visto: ajuste de dificuldade, sequência de atividades, alerta de risco ao professor, sugestão de encaminhamento [I]. Não é o modelo aberto do aprendiz como recurso pedagógico (`adp.lm.open-learner-model`), embora compartilhe técnicas.

## Problema que resolve

Pergunta do domínio: como explicar uma adaptação ou um alerta a professor e responsável sem expor o modelo inteiro, e que supervisão humana se aplica quando o sistema sugere algo sobre um aluno. A tensão é real: o NIST pede que medidas de transparência considerem "the need to safeguard proprietary information" [F: nist2023airmf, §3.4], e a LGPD ressalva "os segredos comercial e industrial" no dever de informar critérios [F: brasil2018lgpd, art. 20, §1].

## Fundamentos e funcionamento

### Obrigações e orientações

- **LGPD art. 20** (redação da Lei 13.853/2019): o titular pode "solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado" que afetem seus interesses, incluídas decisões sobre perfil e personalidade; o controlador fornece, quando solicitado, "informações claras e adequadas a respeito dos critérios" e procedimentos, observado o segredo; se recusar por segredo, "a autoridade nacional poderá realizar auditoria para verificação de aspectos discriminatórios" (§2) [F: brasil2018lgpd, art. 20]. A redação original exigia revisão "por pessoa natural"; a expressão foi retirada pela MP 869/2018 e mantida fora pela Lei 13.853/2019 [F: brasil2018lgpd, art. 20, notas de redação].
- **GDPR art. 22**, para comparação: direito de não se sujeitar a decisão "based solely on automated processing" com efeitos jurídicos ou similarmente significativos; nas exceções, garantia de "at least the right to obtain human intervention", de manifestar ponto de vista e contestar [F: eu2016gdpr, art. 22(1), 22(3)].
- **AI Act art. 13**: instruções de uso devem permitir ao deployer "interpret a system's output and use it appropriately", incluindo capacidades "to provide information that is relevant to explain its output", desempenho por grupos de pessoas e as medidas técnicas que facilitam a interpretação [F: eu2024aiact, art. 13(1), 13(3)(b), 13(3)(d)].
- **AI Act art. 14**: supervisão proporcional a risco, autonomia e contexto, embutida pelo provider ou implementada pelo deployer; o supervisor deve poder entender capacidades e limites, "remain aware of the possible tendency of automatically relying or over-relying on the output" (viés de automação), interpretar corretamente a saída, desconsiderá-la ou revertê-la e interromper o sistema [F: eu2024aiact, art. 14(3), 14(4)]. O deployer atribui a supervisão a pessoas com "competence, training and authority, as well as the necessary support" [F: eu2024aiact, art. 26(2)], e o afetado por decisão baseada em sistema do Anexo III pode obter explicação do papel do sistema e dos "main elements of the decision taken" [F: eu2024aiact, art. 86(1)].
- **PL 2338/2023** (texto do Senado, não aprovado pela Câmara): explicação "respeitado o segredo comercial e industrial", com informações "suficientes, adequadas e inteligíveis", gratuita e em linguagem simples; revisão humana; supervisão que permita "compreender, interpretar, decidir e intervir" [F: pl23382023, arts. 6 a 8].
- **UNICEF**: explicação em nível adequado à idade; a IA não deve ser o único insumo de decisões-chave sobre crianças sem "a human-in-the-loop to make the final decision", e crianças e cuidadores devem ser avisados quando a IA orientou tais decisões [F: unicef2021aichildren, req. 6].

### "Unicamente automatizada" em contexto escolar

[I] Uma adaptação aplicada sem revisão (o sistema troca a atividade seguinte) é decisão unicamente automatizada no sentido do art. 20; um alerta que o professor lê e decide é decisão assistida. A distinção só protege se a intervenção humana for efetiva: o NIST registra que, em certas tarefas, a parte de IA "can amplify human biases" [F: nist2023airmf, Apêndice C], e o perfil de IA generativa lista "automation bias, over-reliance" entre os riscos de configuração humano-IA [F: nist2024ai6001, §2]. Professor que aceita todo alerta sem condições de discordar não transforma a decisão em humana.

### Explicar sem expor o modelo

A literatura de XAI em educação oferece abordagens que dispensam revelar parâmetros: relevância de atributos (usada para mostrar o que pesou no "at-riskness" de um aluno), explicação por exemplos, **explicação local**, que explica uma instância "independent of what might be happening at the model level" e é usada em modelos abertos do aprendiz para informar progresso "without overwhelming the students about the entire model", comparação com casos semelhantes e **explicação contrafactual**, que mostra "the smallest change to the feature values that changes the prediction" [F: khosravi2022explainable, §3.2]. Para modelos pouco interpretáveis, uma via citada é treinar substitutos interpretáveis locais em torno de cada predição [F: khosravi2022explainable, §3.2]. Os mesmos autores alertam para três armadilhas: explicações imprecisas (uma interpretação "can only be as good as its underlying model"), explicações incompletas e comportamento disfuncional, quando quem conhece a regra passa a manipulá-la [F: khosravi2022explainable, §3.5]. Recomendam começar por modelos interpretáveis e aumentar a complexidade aos poucos, comparando acurácia e interpretabilidade [F: khosravi2022explainable, §3.5].

Evidência empírica: num tutor que dá dicas adaptativas, explicações sobre por que a dica foi dada aumentaram confiança, utilidade percebida e intenção de uso; o acesso às explicações e o ganho de aprendizagem variaram conforme características do usuário [F: conati2021personalized, resumo]. O estudo teve 72 participantes universitários [F: conati2021personalized, §5.1], e o efeito sobre aprendizagem dependeu da conscienciosidade: alunos com nível baixo se beneficiaram, os de nível alto não [F: khosravi2022explainable, §4.2.5]. O desenho usou explicações em camadas ("why" e "how"), acessíveis por níveis de detalhe para equilibrar completude e sobrecarga [F: khosravi2022explainable, §4.2.4]. [I] A transferência para crianças pequenas ou com deficiência intelectual não foi testada nessas fontes.

## Requisitos e pressupostos

- Trilha de decisão com entradas, versão do modelo e ações humanas, sem a qual revisão e explicação posterior são impossíveis (`psg.audit.audit-trails`) [I].
- Papéis definidos: quem supervisiona, quem só recebe explicação, quem pode desligar (`psg.access.school-roles`) [I].
- Documentação global do modelo (finalidade, limites, desempenho por grupo) mantida fora da explicação individual (`psg.ai.model-documentation`) [I].

## Vantagens e limitações

Explicação local e contrafactual atende ao art. 20, §1 da LGPD e ao art. 86 do AI Act sem entregar o modelo [I]. Limitações: explicações pós-hoc podem ser plausíveis e falsas [F: khosravi2022explainable, §3.5]; explicar para a criança e para o responsável exige versões distintas [F: unicef2021aichildren, req. 6]; supervisão formal sem tempo, treino e autoridade é decorativa [I].

## Alternativas e comparações

| Público | O que recebe | O que não recebe | Base |
|---|---|---|---|
| Professor (supervisor) | saída, 2 ou 3 fatores principais, confiança, limites conhecidos, botão de rejeitar com motivo | pesos, dados de outros alunos | AI Act art. 14(4); NIST MAP 2.2 |
| Responsável | o que mudou, por quê em linguagem simples, quem revisou, como pedir revisão | detalhes técnicos | LGPD art. 20; UNICEF req. 6 |
| Aluno | aviso de que há IA, explicação adequada à idade | escores de risco sobre si sem mediação | AI Act art. 50(1); UNICEF req. 6 |
| Auditor ou ANPD | documentação do modelo, trilha, testes por grupo | nada por segredo, se houver auditoria | LGPD art. 20, §2 |

## Exemplo técnico independente de domínio

```
ao gerar saida S para aluno A:
  explicacao = {fatores_principais(S, k=3), contrafactual_minimo(S),
                confianca(S), limites_conhecidos(modelo.versao)}
  se S.tipo em {alerta, encaminhamento}:        # decisao assistida
      enfileirar para professor P; S nao produz efeito ate P decidir
      registrar(P, decisao in {aceitar, rejeitar, modificar}, motivo, ts)
  se S.tipo == adaptacao:                       # unicamente automatizada
      aplicar; expor ao professor "o que mudou e por que"; permitir reverter
  canal_revisao(responsavel): pedido -> revisao humana com trilha -> resposta
  monitorar: taxa_de_aceite_por_professor; aceite ~100% => sinal de vies de automacao
```

## Relações com outros conceitos

Depende de `psg.audit.audit-trails` e `psg.access.school-roles`. Complementa `psg.ai.model-documentation` (explicação global) e `psg.ai.eu-ai-act-and-brazil` (fonte das obrigações). As técnicas de exibição a professor e aluno estão em `lae.ind.dashboards-and-olm` e `adp.lm.open-learner-model`; alertas de evasão, em `lae.ind.dropout-and-risk-prediction`. Base legal e ECA em `psg.legal.lgpd-children` e `psg.legal.eca-and-digital-eca`.

## Lacunas e questões abertas

- A ANPD não regulamentou o art. 20 nem definiu o grau de intervenção humana que afasta o "unicamente automatizada"; as orientações europeias sobre intervenção humana significativa não foram consultadas.
- Não foram encontrados estudos de explicação de decisões adaptativas para responsáveis nem para crianças com deficiência intelectual ou de comunicação.
- A taxa de aceite como indicador de viés de automação é proposta deste documento, sem validação empírica.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| brasil2018lgpd | normativo | 2026-10-30 |
| eu2016gdpr | normativo (espelho, art. 22) | 2026-10-30 |
| eu2024aiact | normativo (espelho consolidado) | 2026-10-30 |
| pl23382023 | normativo (projeto de lei) | 2026-10-30 |
| nist2023airmf | tecnico | 2026-10-30 |
| nist2024ai6001 | tecnico | 2026-10-30 |
| unicef2021aichildren | tecnico | 2026-10-30 |
| khosravi2022explainable | academico | 2026-10-30 |
| conati2021personalized | academico | 2026-10-30 |
