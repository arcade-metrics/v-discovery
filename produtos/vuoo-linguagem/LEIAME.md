# VUOO · Linguagem de produto dos microjogos

Estudo de linguagem visual, verbal, sonora e de jogo para os microjogos do VUOO (PIPE-TC Fase 2, Wemoga), em cooperação com o CIATec (CCD/FAPESP, EACH/USP). Feito em 27/10/2026, com decisões delegadas pelo dono do produto, pesquisa em 4 frentes e 3 rodadas de revisão independente.

## Por onde começar

1. **`vuoo-linguagem.html`**: a página visual, para ver tudo aplicado.
2. **`02-gamificacao.md`**: como cada mecânica do Duolingo foi traduzida, e por quê.
3. **`05-decisoes.md`**: as 23 decisões, cada uma com opções, argumentos e o custo de voltar atrás.
4. **`99-pendencias.md`**: o que precisa de você, do CIATec, do jurídico e da consultoria.

## Arquivos

| Arquivo | O que tem |
|---|---|
| `00-insumos.md` | 35 restrições tiradas dos documentos do VUOO e do CIATec, com a fonte de cada uma |
| `01-brief.md` | Problema, personas, 6 hipóteses (onde cada uma roda, com braços seguros), riscos |
| `02-gamificacao.md` | Duolingo → VUOO, mecânica por mecânica; métrica-norte e guarda-corpos |
| `03-linguagem.md` | Marca, conceito, Bot, cor (3 modos), tipografia, pictogramas, ilustração, movimento, som, layout, tom de voz, painel do professor, DUA |
| `04-microjogos.md` | Regra de composição da dupla camada, anatomia em 9 fases, ficha-modelo, 7 conceitos |
| `05-decisoes.md` | Registro de decisões D-01 a D-23 |
| `06-especificacao-base.md` | **Fonte única** de fluxo, falas (com ID) e estados do Bot |
| `99-pendencias.md` | Pendências por responsável |
| `ferramentas/` | Script que valida contraste e daltonismo; paleta em JSON; resultado (40 pares, todos aprovados) |
| `pesquisa/` | Duolingo, neurodivergência, comparação com 16 produtos, restrições institucionais e legais |
| `revisao/` | As 3 rodadas de revisão e as discussões com o que foi aceito ou não |

## Para revalidar a paleta

```
python ferramentas/contraste.py ferramentas/paleta.json
```
