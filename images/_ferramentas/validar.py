"""Valida os SVGs da biblioteca VUOO e gera o JSON de cada objeto e o catálogo.

Uso: python3 _ferramentas/validar.py [arquivo.svg ...]
Sem argumentos, valida todos os SVGs em <categoria>/<NN-item>/<NN-item>.svg.
Para cada SVG válido regrava <NN-item>.json ao lado dele; no fim regrava
catalogo.json na raiz de images/. As regras vêm de vocabulario.json.
Sai com código 1 se algum arquivo tiver erro.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)

FORMAS = {"path", "circle", "ellipse", "rect", "polygon", "polyline", "line", "use"}
PROIBIDOS = {"linearGradient", "radialGradient", "filter", "mask", "pattern", "image", "text", "style"}
NOME = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")
ARQUIVO = re.compile(r"^(\d{2,3})-([a-z][a-z0-9]*(?:-[a-z0-9]+)*)\.svg$")
REF = re.compile(r"url\(#([^)]+)\)")


def tag(el):
    return el.tag.split("}")[-1]


def vocabulario():
    return json.loads((RAIZ / "vocabulario.json").read_text(encoding="utf-8"))


def cores_da_paleta(voc):
    """{'#RRGGBB': (familia, tom)} a partir da paleta do vocabulário."""
    return {hexa.upper(): (familia, tom)
            for familia, tons in voc["paleta"].items() for tom, hexa in tons.items()}


def partes_do_nome(pid, item, voc):
    """'chaleira-tampa-puxador' -> (['tampa', 'puxador'], None); token desconhecido -> (tokens, token)."""
    tokens = []
    for t in pid[len(item) + 1:].split("-"):
        if t.isdigit() and tokens:
            tokens[-1] += "-" + t
        elif t in voc["partes"]:
            tokens.append(t)
        else:
            return tokens, t
    return tokens, None


def referencias(el):
    for nome, valor in el.attrib.items():
        yield from REF.findall(valor)
        if nome in ("href", f"{{{XLINK}}}href") and valor.startswith("#"):
            yield valor[1:]


def validar(caminho, voc):
    """Devolve (erros, avisos, ficha). A ficha é o JSON do objeto, ou None se houver erro."""
    erros, avisos = [], []
    m = ARQUIVO.match(caminho.name)
    if not m:
        return [f"nome de arquivo fora do padrão NN-item.svg: {caminho.name}"], avisos, None
    numero, item = int(m[1]), m[2]
    categoria = caminho.parent.parent.name
    if caminho.parent.name != caminho.stem:
        erros.append(f"o arquivo deve ficar na pasta <categoria>/{caminho.stem}/")
    if categoria not in voc["categorias"]:
        erros.append(f"categoria '{categoria}' não está no vocabulário")

    raiz = ET.parse(caminho).getroot()
    if raiz.get("viewBox") != voc["viewBox"]:
        erros.append(f"viewBox deve ser \"{voc['viewBox']}\" (encontrado: {raiz.get('viewBox')})")
    if raiz.get("role") != "img":
        erros.append('falta role="img" no <svg>')
    titulo = raiz.find(f"{{{SVG}}}title")
    nome = (titulo.text or "").strip() if titulo is not None else ""
    if not nome:
        erros.append("falta <title> com o nome do objeto")

    ids = {el.get("id") for el in raiz.iter() if el.get("id")}
    for el in raiz.iter():
        t = tag(el)
        if t in PROIBIDOS:
            erros.append(f"<{t}> não é permitido (sem gradiente, filtro, texto, imagem ou CSS embutido)")
        for a in ("opacity", "fill-opacity", "stroke-opacity"):
            if el.get(a) not in (None, "1"):
                erros.append(f"{a} não é permitido (sem transparência)")
        if el.get("style"):
            erros.append("use atributos (fill, stroke) em vez de style=")
        i = el.get("id")
        if i and not NOME.match(i):
            erros.append(f"id '{i}' deve ter minúsculas, sem acento, palavras separadas por hífen")
        elif i and i != item and not i.startswith(item + "-"):
            erros.append(f"id '{i}' deve começar com '{item}-'")
        for alvo in referencias(el):
            if alvo not in ids:
                erros.append(f"referência para #{alvo}, que não existe")

    conteudo = [el for el in raiz if tag(el) not in ("title", "desc", "defs", "metadata")]
    if len(conteudo) != 1 or tag(conteudo[0]) != "g" or conteudo[0].get("id") != item:
        erros.append(f'o conteúdo deve estar num único <g id="{item}">')
        return erros, avisos, None

    paleta = cores_da_paleta(voc)
    camada = {tom: i for i, grupo in enumerate(voc["camadas"]) for tom in grupo}
    partes = {}

    def percorrer(el, parte):
        for filho in el:
            t = tag(filho)
            pid = filho.get("id") if t == "g" else None
            if pid:
                tokens, ruim = partes_do_nome(pid, item, voc)
                if ruim:
                    erros.append(f"{pid}: '{ruim}' não está no vocabulário de partes")
                    continue
                pai = f"{item}-" + "-".join(tokens[:-1]) if len(tokens) > 1 else None
                if pai != parte:
                    erros.append(f"{pid} deve ficar dentro de {pai or item}")
                base = tokens[-1].split("-")[0]
                pivo = filho.get("data-pivo")
                if pivo:
                    try:
                        x, y = (float(v) for v in pivo.split(","))
                        pivo = [x, y]
                        if not (0 <= x <= voc["tamanho"] and 0 <= y <= voc["tamanho"]):
                            erros.append(f"{pid}: data-pivo fora da prancheta")
                    except ValueError:
                        erros.append(f"{pid}: data-pivo deve ser \"x,y\" (encontrado: {pivo})")
                        pivo = None
                elif voc["partes"][base]["pivo"]:
                    erros.append(f"{pid}: '{base}' gira, falta data-pivo (marcador {pid}-pivo)")
                partes[pid] = {"parte": base, "pai": pai, "move": voc["partes"][base]["move"],
                               "pivo": pivo, "tons": [], "cores": {}, "subpartes": 0}
                if pai in partes:
                    partes[pai]["subpartes"] += 1
                percorrer(filho, pid)
            elif t == "g":
                if parte is None:
                    erros.append(f"grupo sem nome fora de uma parte de {item}")
                percorrer(filho, parte)
            elif t in FORMAS:
                classe = (filho.get("class") or "").split()
                if parte is None:
                    erros.append(f"<{t}> solta em {item}: toda forma deve estar numa parte")
                elif len(classe) != 1 or classe[0] not in voc["tons"]:
                    erros.append(f"{parte}: <{t}> sem class de tom ({', '.join(voc['tons'])})")
                else:
                    tom = classe[0]
                    partes[parte]["tons"].append(tom)
                    cor = filho.get("fill")
                    if cor in (None, "none"):
                        cor = filho.get("stroke")
                    if cor and cor.startswith("#"):
                        partes[parte]["cores"].setdefault(tom, set()).add(cor.upper())

    percorrer(conteudo[0], None)

    ficha_partes = {}
    for pid, p in partes.items():
        indices = [camada[t] for t in p["tons"]]
        if indices != sorted(indices):
            ordem = " antes de ".join("/".join(g) for g in voc["camadas"])
            erros.append(f"{pid}: {ordem} (encontrado: {', '.join(p['tons'])})")
        if not p["tons"] and not p["subpartes"]:
            avisos.append(f"{pid}: parte vazia")
        familias = set()
        for tom, cores in p["cores"].items():
            for cor in cores:
                if cor in paleta:
                    familias.add(paleta[cor][0])
                else:
                    avisos.append(f"{pid}: cor {cor} ({tom}) fora da paleta do vocabulário")
        ficha_partes[pid] = {
            "parte": p["parte"],
            "pai": p["pai"],
            "move": p["move"],
            "pivo": p["pivo"],
            "tons": list(dict.fromkeys(p["tons"])),
            "cores": {tom: sorted(c) for tom, c in p["cores"].items()},
            "familias": sorted(familias),
        }

    if erros:
        return erros, avisos, None
    png = caminho.with_suffix(".png")
    ficha = {
        "item": item,
        "numero": numero,
        "categoria": categoria,
        "nome": nome,
        "svg": caminho.name,
        "png": png.name if png.exists() else None,
        "viewBox": voc["viewBox"],
        "partes": ficha_partes,
        "gerado_por": "_ferramentas/validar.py a partir do SVG; não edite à mão",
    }
    return erros, avisos, ficha


def todos_os_svgs():
    return sorted(p for p in RAIZ.glob("*/*/*.svg")
                  if not p.relative_to(RAIZ).parts[0].startswith(("_", ".")))


def gravar_catalogo():
    itens = []
    for svg in todos_os_svgs():
        ficha_json = svg.with_suffix(".json")
        if not ficha_json.exists():
            continue
        f = json.loads(ficha_json.read_text(encoding="utf-8"))
        pasta = svg.parent.relative_to(RAIZ).as_posix()
        itens.append({
            "item": f["item"], "numero": f["numero"], "categoria": f["categoria"], "nome": f["nome"],
            "svg": f"{pasta}/{f['svg']}", "json": f"{pasta}/{ficha_json.name}",
            "png": f"{pasta}/{f['png']}" if f["png"] else None,
            "partes": list(f["partes"]),
        })
    itens.sort(key=lambda i: (i["categoria"], i["numero"]))
    catalogo = {"gerado_por": "_ferramentas/validar.py; não edite à mão", "itens": itens}
    (RAIZ / "catalogo.json").write_text(json.dumps(catalogo, ensure_ascii=False, indent=2) + "\n",
                                        encoding="utf-8")
    return len(itens)


def processar(arquivos, voc):
    """Valida, grava o JSON de cada SVG válido e apaga o de cada inválido. Devolve o número de inválidos."""
    invalidos = 0
    for svg in arquivos:
        erros, avisos, ficha = validar(svg, voc)
        ficha_json = svg.with_suffix(".json")
        print(f"{'ERRO' if erros else 'OK  '} {svg.relative_to(RAIZ) if svg.is_relative_to(RAIZ) else svg}")
        for e in erros:
            print(f"     erro:  {e}")
        for a in avisos:
            print(f"     aviso: {a}")
        if ficha:
            ficha_json.write_text(json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        else:
            invalidos += 1
            if ficha_json.exists():
                ficha_json.unlink()
    return invalidos


def main(args):
    voc = vocabulario()
    arquivos = [Path(a).resolve() for a in args] or todos_os_svgs()
    invalidos = processar(arquivos, voc)
    print(f"\n{len(arquivos) - invalidos}/{len(arquivos)} válidos; catálogo com {gravar_catalogo()} itens")
    return 1 if invalidos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
