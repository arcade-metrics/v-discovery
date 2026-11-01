# Biblioteca de ilustrações VUOO

Cada ilustração é um objeto com três arquivos na mesma pasta:

```
cozinha/29-chaleira/
  29-chaleira.ai     ← fonte: só este é editado à mão
  29-chaleira.svg    ← gerado por ferramentas/normalizar.py
  29-chaleira.json   ← gerado por ferramentas/validar.py
  29-chaleira.png    ← render 1024 × 1024 para revisão
```

Na raiz ficam:

- `vocabulario.json`: as regras (partes, tons, categorias, paleta, prancheta). **É o único arquivo de regra.** Para criar uma parte ou categoria nova, acrescente-a aqui antes de usá-la.
- `catalogo.json`: lista de todos os objetos, gerada. O app procura por ela.
- `vuoo-guia-universal-linguagem-visual.md`: como desenhar. Este LEIAME trata de como nomear e entregar.
- `_originais/`: SVGs anteriores à biblioteca, sem nomes, guardados como referência. As ferramentas ignoram pastas que começam com `_`.

## Nomes

Tudo em minúsculas, sem acento, com hífen entre as palavras. Todo nome começa com o item, para não colidir quando vários SVGs estão na mesma tela: `chaleira-tampa`, e não `tampa`. No arquivo, o número de ordem vem antes (`29-chaleira.svg`). Nos ids, não, porque um id que começa com dígito atrapalha o CSS.

São três níveis:

1. **Item**, o grupo raiz: `chaleira`.
2. **Parte**, que pode ser animada sozinha: `chaleira-corpo`, `chaleira-tampa`. As palavras precisam estar em `partes` no vocabulário. Uma parte repetida ganha número (`fogao-botao-1`). Uma parte que se move junto com outra fica aninhada nela, e o nome mostra isso: `chaleira-tampa-puxador` fica dentro de `chaleira-tampa`.
3. **Tom**, as formas pintadas dentro da parte, que viram `class`. Os nomes são fixos: `sombra`, `base`, `marca`, `brilho`. Dentro de cada parte, sombra e base vêm antes de marca e brilho. Sombra e base podem vir em qualquer ordem entre si: no método do guia, a sombra é a forma inteira embaixo e a base é a cópia deslocada e recortada por cima; também vale base inteira com a sombra recortada por cima.

Frutas inteiras usam `corpo`. Frutas cortadas usam `casca`, `polpa` e `miolo`. Várias frutas no mesmo desenho viram `corpo-1`, `corpo-2` (cereja, uva, mirtilo). Sementes miúdas são `marca` da polpa ou do corpo; um caroço grande é a parte `semente`.

Tudo o que pode se mover sozinho vira parte: tampa, porta, ponteiro, botão, líquido, vapor, cabo. As partes que giram (`"pivo": true` no vocabulário) precisam de ponto de giro.

## No Illustrator

O nome da camada é a única informação que passa pelo Illustrator, pelo SVG e pelo After Effects. Por isso, toda a semântica fica nele.

- Prancheta de **1024 × 1024 px**.
- **Cada parte é uma camada de topo** (`chaleira-corpo`, `chaleira-tampa`, `chaleira-tampa-puxador`), porque o After Effects só transforma as camadas de topo em layers. Não aninhe as partes: o normalizador faz o aninhamento pelo nome. Ponha a camada filha acima da camada mãe.
- Dentro da parte, nomeie as formas ou subcamadas pelo tom: `sombra`, `base`, `marca`, `brilho`. Também vale o nome completo (`chaleira-tampa-base`). Nomes repetidos não são problema.
- **Ponto de giro:** desenhe um círculo pequeno, de qualquer cor, numa camada `chaleira-tampa-pivo` dentro da parte. O normalizador lê o centro, grava em `data-pivo` e apaga o círculo. No After Effects, coloque o anchor point sobre ele.
- Sem gradiente, transparência, efeito, texto ou imagem. O validador recusa qualquer um deles.

**Exportar** (Arquivo › Exportar › Exportar como › SVG), salvando em `_exportar/29-chaleira.svg`:

| Opção | Valor |
|---|---|
| Estilo | Atributos de apresentação |
| Fonte | SVG |
| Imagens | Preservar |
| IDs de objeto | Nomes de camada |
| Decimal | 2 |
| Minificar / Responsivo | desmarcados |

## Gerar e validar

Os comandos são rodados a partir de `images/` e só precisam de Python 3.9 ou mais recente, sem instalar nada:

```sh
# exportação do Illustrator → SVG no padrão + JSON + catálogo
python3 ferramentas/normalizar.py _exportar/29-chaleira.svg --categoria cozinha --nome "Chaleira"

# revalida tudo e regrava os JSON e o catálogo (rode depois de mexer no vocabulário)
python3 ferramentas/validar.py
```

O normalizador avisa tudo o que precisou deduzir ou corrigir: forma sem nome com o tom deduzido pela cor, forma fora de parte enviada para `<item>-corpo`, camada de nome desconhecido. Um **erro** impede gerar o JSON. Um **aviso** não impede, mas merece revisão. Cor fora da paleta é aviso.

O validador também aceita um SVG feito à mão, desde que já esteja no padrão.

## O SVG gerado

```xml
<svg viewBox="0 0 1024 1024" role="img" aria-labelledby="chaleira-titulo">
  <title id="chaleira-titulo">Chaleira</title>
  <defs>
    <clipPath id="chaleira-corpo-recorte">…</clipPath>
  </defs>
  <g id="chaleira">
    <g id="chaleira-corpo">
      <path class="sombra" fill="#8293B8" …/>
      <g clip-path="url(#chaleira-corpo-recorte)"><path class="base" fill="#AEBEDB" …/></g>
      <path class="brilho" fill="#DCE5F5" …/>
    </g>
    <g id="chaleira-tampa" data-pivo="380,300">
      …
      <g id="chaleira-tampa-puxador">…</g>
    </g>
  </g>
</svg>
```

- O `fill` fica no arquivo, para ele abrir sozinho em qualquer programa. No app, uma regra CSS sobrepõe o `fill` sem editar o SVG (por exemplo, `.vuoo-suave .base { fill: … }`).
- O `data-pivo` está nas coordenadas do `viewBox`. Para usá-lo como origem de giro: GSAP `svgOrigin: "380 300"`, ou CSS `transform-box: view-box; transform-origin: 380px 300px`.
- Um desenho feito em outra prancheta (por exemplo, 400 px) é escalado com `transform="scale(...)"` no grupo do item. O `data-pivo` já sai convertido.

## O JSON de cada objeto

Ele é gerado a partir do SVG e nunca editado à mão. Traz o nome com acentos, a categoria, o número e, para cada parte, o pai, se ela se move, o pivô, os tons e as cores, e a família da paleta. É o arquivo que o app e um script de After Effects leem para montar o parenting e os anchor points. Veja `cozinha/01-colher/01-colher.json`.
