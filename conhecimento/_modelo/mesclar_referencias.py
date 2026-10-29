#!/usr/bin/env python3
"""Mescla referencias/fragmentos/*.bib em bibliografia.bib e *-indice.md em indice-fontes.md.

Uso: python conhecimento/_modelo/mesclar_referencias.py

- Chave duplicada entre fragmentos: mantem a primeira ocorrencia (ordem alfabetica de arquivo)
  e avisa se o campo url divergir.
- Reescreve bibliografia.bib e indice-fontes.md inteiros, preservando o cabecalho de cada um.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REF = RAIZ / "referencias"
FRAG = REF / "fragmentos"
BIB = REF / "bibliografia.bib"
IDX = REF / "indice-fontes.md"

CABECALHO_BIB = """% Bibliografia central de conhecimento/
% Convenção de chave: <sobrenome-primeiro-autor><ano><palavra-do-titulo>, minúsculas, ASCII.
% Para RFC: rfc<numero>. Para W3C: w3c<ano><slug>. Para documentação de fornecedor: <produto><ano><slug>.
% Campos obrigatórios além dos do tipo: url, urldate (data de consulta). Quando houver: doi, version.
% Gerado por _modelo/mesclar_referencias.py a partir de fragmentos/. Edite os fragmentos, não este arquivo.

"""

CABECALHO_IDX = """# Índice de fontes

Uma linha por fonte. Chave igual à de `bibliografia.bib`. Tipos: normativo, fornecedor, academico, tecnico, secundario.
Gerado por `_modelo/mesclar_referencias.py` a partir de `fragmentos/`.

| Chave | Título | Tipo | Domínio | URL | Consultado em |
|---|---|---|---|---|---|
"""


def entradas_bib(texto):
    """Divide um .bib em entradas (chave, texto) contando chaves."""
    out = []
    i = 0
    while True:
        m = re.search(r"@\w+\s*\{\s*([^,\s]+)\s*,", texto[i:])
        if not m:
            break
        ini = i + m.start()
        j = i + m.end()
        prof = 1
        while j < len(texto) and prof:
            if texto[j] == "{":
                prof += 1
            elif texto[j] == "}":
                prof -= 1
            j += 1
        out.append((m.group(1), texto[ini:j].strip()))
        i = j
    return out


def url_de(entrada):
    m = re.search(r"url\s*=\s*[{\"]([^}\"]+)[}\"]", entrada)
    return m.group(1).strip() if m else None


def main():
    chaves = {}
    ordem = []
    for f in sorted(FRAG.glob("*.bib")):
        for k, e in entradas_bib(f.read_text(encoding="utf-8")):
            if k in chaves:
                u1, u2 = url_de(chaves[k][1]), url_de(e)
                if u1 != u2:
                    print(f"AVISO chave {k} duplicada com url diferente: {chaves[k][0]} vs {f.name}")
                continue
            chaves[k] = (f.name, e)
            ordem.append(k)
    BIB.write_text(CABECALHO_BIB + "\n\n".join(chaves[k][1] for k in sorted(ordem)) + "\n", encoding="utf-8")

    linhas = {}
    for f in sorted(FRAG.glob("*-indice.md")):
        for ln in f.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln.startswith("|") or ln.startswith("|---") or ln.lower().startswith("| chave"):
                continue
            k = ln.split("|")[1].strip().strip("`")
            if k and k not in linhas:
                linhas[k] = ln
    faltam_idx = [k for k in ordem if k not in linhas]
    faltam_bib = [k for k in linhas if k not in chaves]
    IDX.write_text(CABECALHO_IDX + "\n".join(linhas[k] for k in sorted(linhas)) + "\n", encoding="utf-8")
    print(f"bib: {len(chaves)} entradas; indice: {len(linhas)} linhas")
    for k in faltam_idx:
        print(f"AVISO {k} esta no .bib mas nao no indice")
    for k in faltam_bib:
        print(f"AVISO {k} esta no indice mas nao no .bib")


if __name__ == "__main__":
    main()
