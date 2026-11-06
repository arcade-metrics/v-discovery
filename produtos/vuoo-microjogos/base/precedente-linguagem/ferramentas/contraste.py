"""Valida os pares de cor da paleta VUOO contra WCAG 2.2 (AA/AAA) e simula daltonismo.

Uso: python contraste.py paleta.json
O JSON tem {"tokens": {nome: "#rrggbb"}, "pares": [[texto, fundo, "uso"], ...]}.
Pares de texto normal exigem 4.5:1 (AA); texto grande e componentes de UI, 3:1.
"""
import json
import sys


def _lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def rgb(hexa):
    h = hexa.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminancia(hexa):
    r, g, b = (_lin(v) for v in rgb(hexa))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# Matrizes de Machado et al. (2009), severidade 1.0, aplicadas em RGB linear.
CVD = {
    "protanopia": ((0.152286, 1.052583, -0.204868), (0.114503, 0.786281, 0.099216), (-0.003882, -0.048116, 1.051998)),
    "deuteranopia": ((0.367322, 0.860646, -0.227968), (0.280085, 0.672501, 0.047413), (-0.011820, 0.042940, 0.968881)),
    "tritanopia": ((1.255528, -0.076749, -0.178779), (-0.078411, 0.930809, 0.147602), (0.004733, 0.691367, 0.303900)),
}


def simula(hexa, tipo):
    lin = [_lin(v) for v in rgb(hexa)]
    out = []
    for linha in CVD[tipo]:
        v = max(0.0, min(1.0, sum(m * c for m, c in zip(linha, lin))))
        s = 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
        out.append(round(s * 255))
    return "#%02x%02x%02x" % tuple(out)


def lab(hexa):
    r, g, b = (_lin(v) for v in rgb(hexa))
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def delta_e(a, b):
    """CIE76: abaixo de ~10 as cores se confundem num relance; acima de ~20, distintas."""
    return sum((p - q) ** 2 for p, q in zip(lab(a), lab(b))) ** 0.5


def main(caminho):
    dados = json.load(open(caminho, encoding="utf-8"))
    tok = dados["tokens"]
    falhas = 0
    print(f"{'texto':<18}{'fundo':<18}{'razão':>7}  {'meta':>5}  resultado  uso")
    for texto, fundo, uso, *meta in dados["pares"]:
        alvo = float(meta[0]) if meta else 4.5
        r = contraste(tok[texto], tok[fundo])
        ok = r >= alvo
        falhas += not ok
        nivel = "AAA" if r >= 7 else "AA" if r >= 4.5 else "AA-grande" if r >= 3 else "FALHA"
        print(f"{texto:<18}{fundo:<18}{r:7.2f}  {alvo:5.1f}  {'ok ' if ok else 'XX '}{nivel:<8} {uso}")
    for grupo in dados.get("distinguir", []):
        print(f"\nDistinção sob daltonismo: {', '.join(grupo)}")
        for tipo in ("visão típica", *CVD):
            sim = {n: tok[n] if tipo == "visão típica" else simula(tok[n], tipo) for n in grupo}
            pares = sorted(
                (delta_e(sim[a], sim[b]), a, b)
                for i, a in enumerate(grupo) for b in grupo[i + 1:]
            )
            pior = pares[0]
            aviso = "  << confundíveis" if pior[0] < 10 else ""
            print(f"  {tipo:<13} menor ΔE: {pior[0]:5.1f} ({pior[1]} x {pior[2]}){aviso}")
    print(f"\n{falhas} par(es) abaixo da meta")
    return falhas


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1]) else 0)
