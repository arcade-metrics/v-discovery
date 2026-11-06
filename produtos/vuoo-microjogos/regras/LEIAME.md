# Regras de negócio

Uma regra por arquivo, com código estável `RN-nn`. Pasta criada em 05/11/2026; nenhuma regra escrita ainda.

## Formato

```yaml
---
id: RN-01
titulo:
status: proposta | aceita | substituída
origem: []          # seção do 02-prd.md, 03-mvp.md ou do guia-de-estilo.md
substitui:
atualizado_em: AAAA-MM-DD
---
```

Corpo: a regra em uma frase verificável; o que ela protege; como se testa; exceções; custo de voltar atrás.

## Candidatas

**Limites invioláveis do estilo** ([../guia-de-estilo.md](../guia-de-estilo.md) §12):

| # | Limite |
|---|---|
| L-01 | No máximo 3 flashes por segundo |
| L-02 | Texto ≥ 4,5:1 e componentes ≥ 3:1 em toda combinação |
| L-03 | Cor nunca é o único código |
| L-04 | Pausar, Ouvir e Ajustes sempre visíveis, na mesma posição |
| L-05 | Todo laço de mais de 5 s é pausável |
| L-06 | Erro nunca é punitivo: sem alarme, sem tremor, sem tristeza do personagem, sem sarcasmo |
| L-07 | Estímulos de avaliação não mudam por estilo, preset ou IA |
| L-08 | A IA nunca reduz acesso nem aumenta estímulo acima do teto do aluno ou do professor |
| L-09 | Toda mudança automática é anunciada e desfeita com um toque |
| L-10 | Alvos nunca abaixo de 44 px, espaçamento nunca abaixo de 8 px |

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
