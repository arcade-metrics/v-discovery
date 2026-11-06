"""Converte um SVG exportado do Illustrator para o padrão da biblioteca VUOO.

Uso: python3 _ferramentas/normalizar.py _exportar/29-chaleira.svg --categoria cozinha [--nome "Chaleira"]

Lê os nomes de camada (que o Illustrator exporta como id ou data-name) e:
- transforma o bloco <style> e style= em atributos fill/stroke;
- limpa os nomes (_1_, _x5F_, acentos, maiúsculas, espaços);
- vira class a camada de tom (base, chaleira-tampa-base, ...);
- aninha as partes pelo nome (chaleira-tampa-puxador entra em chaleira-tampa);
- troca o marcador <parte>-pivo por data-pivo na parte e apaga o marcador;
- prefixa com o item os ids de <defs> (clippath-1 vira chaleira-recorte-1);
- escala para a prancheta padrão se o viewBox for outro quadrado.
Grava em <categoria>/<NN-item>/<NN-item>.svg e roda validar.py nele.
"""
import argparse
import copy
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

from validar import ARQUIVO, FORMAS, RAIZ, SVG, XLINK, cores_da_paleta, gravar_catalogo, processar, tag, vocabulario

DESCARTAR = {"id", "data-name", "class"}


def limpar_nome(el):
    bruto = el.get("data-name") or el.get("id") or ""
    bruto = re.sub(r"_x([0-9A-Fa-f]{2})_", lambda m: chr(int(m[1], 16)), bruto)
    bruto = re.sub(r"_\d+_$", "", bruto)
    bruto = unicodedata.normalize("NFKD", bruto).encode("ascii", "ignore").decode()
    bruto = re.sub(r"[\s_]+", "-", bruto.strip().lower())
    return re.sub(r"-+", "-", bruto).strip("-")


def cor(valor):
    v = valor.strip()
    if re.fullmatch(r"#[0-9a-fA-F]{3}", v):
        v = "#" + "".join(c * 2 for c in v[1:])
    return v.upper() if re.fullmatch(r"#[0-9a-fA-F]{6}", v) else v


def declaracoes(texto):
    return {k.strip(): v.strip() for k, v in
            (d.split(":", 1) for d in texto.split(";") if ":" in d)}


def aplicar_estilos(raiz):
    """Troca as classes cls-N do Illustrator e os style= por atributos de apresentação."""
    regras = {}
    for st in raiz.iter(f"{{{SVG}}}style"):
        for seletores, corpo in re.findall(r"([^{}]+)\{([^}]*)\}", st.text or ""):
            for s in seletores.split(","):
                s = s.strip()
                if s.startswith("."):
                    regras.setdefault(s[1:], {}).update(declaracoes(corpo))
    for el in raiz.iter():
        for c in (el.get("class") or "").split():
            for k, v in regras.get(c, {}).items():
                el.set(k, v)
        for k, v in declaracoes(el.attrib.pop("style", "")).items():
            el.set(k, v)
        el.attrib.pop("class", None)
        for a in ("fill", "stroke"):
            if el.get(a):
                el.set(a, cor(el.get(a)))


def classificar(nome, item, tons):
    """Devolve (tipo, parte_do_nome, tom) a partir do nome de camada limpo."""
    m = re.fullmatch(rf"(?:(.+)-)?({'|'.join(tons)})(?:-\d+)?", nome)
    if m:
        return "tom", m[1], m[2]
    m = re.fullmatch(r"(?:(.+)-)?pivo(?:-\d+)?", nome)
    if m:
        return "pivo", m[1], None
    if nome == item or not nome or nome.startswith(("camada", "layer")):
        return "grupo", None, None
    if nome.startswith(item + "-"):
        return "parte", nome, None
    return "desconhecido", None, None


def centro(el):
    t = tag(el)
    f = lambda a: float(el.get(a, 0))
    if t in ("circle", "ellipse"):
        return f("cx"), f("cy")
    if t == "rect":
        return f("x") + f("width") / 2, f("y") + f("height") / 2
    return None


class Normalizador:
    def __init__(self, item, voc):
        self.item, self.voc = item, voc
        self.tons = list(voc["tons"])
        self.paleta = cores_da_paleta(voc)
        self.partes = {}
        self.pivos = {}
        self.avisos = []

    def parte(self, pid):
        if pid not in self.partes:
            self.partes[pid] = ET.Element(f"{{{SVG}}}g", {"id": pid})
        return self.partes[pid]

    def completar(self, nome):
        """'tampa' ou 'chaleira-tampa' -> 'chaleira-tampa'."""
        return nome if nome.startswith(self.item + "-") else f"{self.item}-{nome}"

    def destino(self, parte_do_nome, parte, atual):
        if parte_do_nome and parte_do_nome != self.item:
            pid = self.completar(parte_do_nome)
            return pid, (atual if pid == parte else self.parte(pid))
        if parte:
            return parte, atual
        pid = f"{self.item}-corpo"
        self.avisos.append(f"forma fora de parte foi para {pid}")
        return pid, self.parte(pid)

    def tom_pela_cor(self, el):
        c = el.get("fill") if el.get("fill") not in (None, "none") else el.get("stroke")
        return self.paleta.get((c or "").upper(), (None, None))[1]

    def visitar(self, el, parte, atual, tom_forcado=None):
        for filho in el:
            t = tag(filho)
            if t in ("defs", "title", "desc", "metadata", "clipPath", "style"):
                continue
            tipo, parte_do_nome, tom = classificar(limpar_nome(filho), self.item, self.tons)
            if tipo == "desconhecido":
                self.avisos.append(f"nome de camada '{limpar_nome(filho)}' ignorado")
                tipo = "grupo"
            if tipo == "pivo":
                pid = self.completar(parte_do_nome) if parte_do_nome else parte
                alvo = filho if t != "g" else next((f for f in filho.iter() if tag(f) in FORMAS), None)
                ponto = centro(alvo) if alvo is not None else None
                if pid and ponto:
                    self.pivos[pid] = ponto
                else:
                    self.avisos.append("marcador de pivô ignorado: desenhe um círculo na camada <parte>-pivo")
                continue
            if t == "g" and tipo == "parte":
                g = self.parte(parte_do_nome)
                g.attrib.update({k: v for k, v in filho.attrib.items() if k not in DESCARTAR})
                self.visitar(filho, parte_do_nome, g)
            elif t == "g":
                if tipo == "tom":
                    parte_alvo, atual_alvo = self.destino(parte_do_nome, parte, atual)
                else:
                    parte_alvo, atual_alvo = parte, atual
                extras = {k: v for k, v in filho.attrib.items() if k not in DESCARTAR}
                if extras:
                    if parte_alvo is None:
                        parte_alvo, atual_alvo = self.destino(None, None, None)
                    atual_alvo = ET.SubElement(atual_alvo, f"{{{SVG}}}g", extras)
                self.visitar(filho, parte_alvo, atual_alvo, tom if tipo == "tom" else tom_forcado)
            elif t in FORMAS:
                pid, alvo = self.destino(parte_do_nome if tipo == "tom" else None, parte, atual)
                tom_final = tom if tipo == "tom" else tom_forcado
                if not tom_final:
                    tom_final = self.tom_pela_cor(filho)
                    if tom_final:
                        self.avisos.append(f"{pid}: tom '{tom_final}' deduzido pela cor de uma <{t}>")
                    else:
                        self.avisos.append(f"{pid}: <{t}> sem tom; nomeie a camada (base, sombra, marca, brilho)")
                forma = ET.SubElement(alvo, filho.tag, {k: v for k, v in filho.attrib.items() if k not in DESCARTAR})
                if tom_final:
                    forma.set("class", tom_final)

    def montar(self, escala):
        raiz = ET.Element(f"{{{SVG}}}g", {"id": self.item})
        if escala != 1:
            raiz.set("transform", f"scale({escala:g})")
        ordem = list(self.partes)
        for pid in ordem:
            pai = max((p for p in ordem if pid.startswith(p + "-")), key=len, default=None)
            if pai and ordem.index(pai) > ordem.index(pid):
                self.avisos.append(f"{pid} estava abaixo de {pai}; agora fica por cima dele")
            (self.partes[pai] if pai else raiz).append(self.partes[pid])
        for pid, (x, y) in self.pivos.items():
            if pid in self.partes:
                self.partes[pid].set("data-pivo", f"{round(x * escala, 1):g},{round(y * escala, 1):g}")
            else:
                self.avisos.append(f"pivô de {pid}, parte que não existe")
        return raiz


def renomear_defs(defs, conteudo, item):
    """Prefixa com o item os ids de <defs> e atualiza as referências."""
    novos, contagem = {}, {}
    for el in defs.iter():
        antigo = el.get("id")
        if not antigo:
            continue
        limpo = limpar_nome(el)
        if limpo.startswith(item + "-"):
            novo = limpo
        else:
            sufixo = "recorte" if tag(el) == "clipPath" else "forma"
            contagem[sufixo] = contagem.get(sufixo, 0) + 1
            novo = f"{item}-{sufixo}-{contagem[sufixo]}"
        novos[antigo] = novo
        el.set("id", novo)
        el.attrib.pop("data-name", None)
    for el in list(defs.iter()) + list(conteudo.iter()):
        for nome, valor in list(el.attrib.items()):
            valor = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{novos.get(m[1], m[1])})", valor)
            if nome in ("href", f"{{{XLINK}}}href"):
                del el.attrib[nome]
                nome = "href"
                if valor.startswith("#"):
                    valor = "#" + novos.get(valor[1:], valor[1:])
            el.set(nome, valor)


def normalizar(entrada, categoria, nome, voc):
    m = ARQUIVO.match(entrada.name)
    if not m:
        sys.exit(f"o arquivo deve se chamar NN-item.svg (ex.: 29-chaleira.svg), não {entrada.name}")
    item = m[2]
    fonte = ET.parse(entrada).getroot()
    aplicar_estilos(fonte)

    vb = [float(v) for v in (fonte.get("viewBox") or "").replace(",", " ").split()]
    if len(vb) != 4 or vb[0] or vb[1] or vb[2] != vb[3]:
        sys.exit(f"a prancheta deve ser quadrada e começar em 0,0 (viewBox: {fonte.get('viewBox')})")
    escala = voc["tamanho"] / vb[2]

    n = Normalizador(item, voc)
    if escala != 1:
        n.avisos.append(f"prancheta de {vb[2]:g} px escalada para {voc['tamanho']} px")
    n.visitar(fonte, None, None)
    conteudo = n.montar(escala)

    defs = ET.Element(f"{{{SVG}}}defs")
    for el in fonte.iter():
        if tag(el) == "defs":
            defs.extend(copy.deepcopy(f) for f in el if tag(f) != "style")
    for el in fonte:
        if tag(el) == "clipPath":
            defs.append(copy.deepcopy(el))
    renomear_defs(defs, conteudo, item)

    if not nome:
        titulo = fonte.find(f"{{{SVG}}}title")
        nome = (titulo.text or "").strip() if titulo is not None else fonte.get("aria-label")
    if not nome:
        nome = item.replace("-", " ").capitalize()
        n.avisos.append(f"sem --nome; usei '{nome}' (confira os acentos)")

    tamanho = str(voc["tamanho"])
    svg = ET.Element(f"{{{SVG}}}svg", {"viewBox": voc["viewBox"], "width": tamanho, "height": tamanho,
                                        "role": "img", "aria-labelledby": f"{item}-titulo"})
    ET.SubElement(svg, f"{{{SVG}}}title", {"id": f"{item}-titulo"}).text = nome
    if len(defs):
        svg.append(defs)
    svg.append(conteudo)
    ET.indent(svg)

    saida = RAIZ / categoria / entrada.stem / entrada.name
    saida.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(saida, encoding="UTF-8", xml_declaration=True)
    return saida, n.avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("entrada", type=Path)
    ap.add_argument("--categoria", required=True)
    ap.add_argument("--nome", help="nome exibido, com acentos (vira o <title>)")
    args = ap.parse_args()
    voc = vocabulario()
    if args.categoria not in voc["categorias"]:
        sys.exit(f"categoria '{args.categoria}' não está em vocabulario.json: {', '.join(voc['categorias'])}")

    saida, avisos = normalizar(args.entrada.resolve(), args.categoria, args.nome, voc)
    print(f"gravado {saida.relative_to(RAIZ)}")
    for a in avisos:
        print(f"     normalização: {a}")
    invalidos = processar([saida], voc)
    gravar_catalogo()
    return 1 if invalidos else 0


if __name__ == "__main__":
    sys.exit(main())
