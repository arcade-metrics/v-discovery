# VUOO · Linguagem de produto dos microjogos

> **Estudo anterior, enquadrado no projeto de pesquisa.** Em 2026-11-05 ficou decidido que o produto VUOO é independente do projeto com o CIATec e começa do zero. Este estudo continua como **precedente**: as decisões D-01 a D-23, os insumos e as pendências daqui só valem para o produto quando forem decididos de novo em [`../vuoo-microjogos/`](../vuoo-microjogos/LEIAME.md). Referências a PP, fases, CIATec, base de pesquisa e CEP descrevem o projeto, não o produto.

Estudo de linguagem visual, verbal, sonora e de jogo para os microjogos do VUOO (PIPE-TC Fase 2, Wemoga), em cooperação com o CIATec (CCD/FAPESP, EACH/USP). Feito em 27/10/2026, com decisões delegadas pelo dono do produto, pesquisa em 4 frentes e 3 rodadas de revisão independente.

## Por onde começar

1. **`guia-pratico-design.md`**: guia prático de design, autocontido — quem vai desenhar, ilustrar, escrever ou implementar uma tela só precisa deste arquivo.
2. **`transformar-em-vuoo.md`**: receita para um agente transformar qualquer forma (papel, imagem, SVG, Illustrator) em ilustração VUOO, como SVG pronto para animar.
3. **`vuoo-linguagem.html`**: a página visual, para ver tudo aplicado.
4. **`02-gamificacao.md`**: como cada mecânica do Duolingo foi traduzida, e por quê.
5. **`05-decisoes.md`**: as 23 decisões, cada uma com opções, argumentos e o custo de voltar atrás.
6. **`99-pendencias.md`**: o que precisa de você, do CIATec, do jurídico e da consultoria.

## Arquivos

| Arquivo | O que tem |
|---|---|
| `guia-pratico-design.md` | **Guia prático de design, autocontido:** marca, Bot, cor, tipografia, pictogramas, ilustração, movimento, som, layout e componentes, anatomia de microjogo, tom de voz — condensado de `03`, `04` e `06`, sem citações de pesquisa nem referências cruzadas |
| `transformar-em-vuoo.md` | Receita passo a passo para o agente: ler a entrada, simplificar, reconstruir com formas básicas, pintar com as rampas de ilustração, montar o SVG, testes de aceite e relatório |
| `00-insumos.md` | 35 restrições tiradas dos documentos do VUOO e do CIATec, com a fonte de cada uma |
| `01-brief.md` | Problema, personas, 6 hipóteses (onde cada uma roda, com braços seguros), riscos |
| `02-gamificacao.md` | Duolingo → VUOO, mecânica por mecânica; métrica-norte e guarda-corpos |
| `03-linguagem.md` | Marca, conceito, Bot, cor (3 modos), tipografia, pictogramas, ilustração, movimento, som, layout, tom de voz, painel do professor, DUA |
| `04-microjogos.md` | Regra de composição da dupla camada, anatomia em 9 fases, ficha-modelo, 7 conceitos |
| `05-decisoes.md` | Registro de decisões D-01 a D-23 |
| `06-especificacao-base.md` | **Fonte única** de fluxo, falas (com ID) e estados do Bot |
| `99-pendencias.md` | Pendências por responsável |
| `ferramentas/` | Script que valida contraste e daltonismo; paleta em JSON; resultado (62 pares, todos aprovados, incluindo as rampas de ilustração `il-*`) |
| `pesquisa/` | Duolingo, neurodivergência, comparação com 16 produtos, restrições institucionais e legais |
| `revisao/` | As 3 rodadas de revisão e as discussões com o que foi aceito ou não |

## Para revalidar a paleta

```
python ferramentas/contraste.py ferramentas/paleta.json
```
