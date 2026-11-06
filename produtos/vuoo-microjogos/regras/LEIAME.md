# Regras de negócio

Uma regra por arquivo, com código estável `RN-nn`. Nenhuma regra escrita ainda.

## Formato

```yaml
---
id: RN-01
titulo:
status: proposta | aceita | substituída
origem: []          # seção do 02-prd.md, 03-mvp.md, decisoes.md ou base/parametrizacao-estilo.md
substitui:
atualizado_em: AAAA-MM-DD
---
```

Corpo: a regra em uma frase verificável; o que ela protege; como se testa; exceções; custo de voltar atrás.

## Candidatas

**Limites invioláveis do estilo:** L-01 a L-10, definidos em [../base/parametrizacao-estilo.md](../base/parametrizacao-estilo.md) §5 (dono único; resumo no [guia de estilo](../guia-de-estilo.md) §12). Cada limite vira uma `RN-nn` quando for escrito.

**Do PRD e do MVP:**

- Nenhum dado do aluno é coletado antes da autorização do responsável (PRD RF-01; MVP §7).
- O metadado de educação especial nunca alimenta a adaptação (PRD §3).
- A referência de laudo nunca guarda o arquivo (PRD RF-08).
- Sem vidas e sem ranking público (PRD §6).
- Nada se perde por ausência: a ofensiva pausa e nunca zera (PRD §6).
- Estilo só nas configurações do jogador; Moderado é sempre o padrão (PRD §8).

- Limites diários: até 2 sessões de trilha e alerta gentil aos 30 min de jogos livres (PRD §5).
- Casas de dias que faltam ficam neutras, sem evidenciar perda; dias passados podem ser feitos depois (PRD §6).
- Celebração descreve participação, nunca conta acertos (PRD §6).
- Nenhuma reação do mascote depende de acerto ou erro (PRD §6).
- Na tarefa de função executiva, o conteúdo da BNCC nunca decide a resposta (PRD §4).
- Quem jogou sem rede aparece como "aguardando sincronização", nunca "não jogou" (PRD §10).

**Do estudo anterior de linguagem** (`base/precedente-linguagem/`):

- Sem recompensa por sorteio; toda recompensa é anunciada antes.
- Sem notificação para o aluno.
- Sem chat entre alunos.
- "Parar" e "Continuar" sempre com o mesmo peso visual.
- Número nunca é falado em feedback ("12 de 20").
- Sinal de atenção ao professor só com confirmação humana, nunca como "risco". `[A CONFIRMAR]`
