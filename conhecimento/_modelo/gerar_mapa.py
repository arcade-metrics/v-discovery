#!/usr/bin/env python3
"""Gera a secao automatica do mapa de conceitos de um dominio a partir do frontmatter.

Uso: python conhecimento/_modelo/gerar_mapa.py <dominio>

Imprime em stdout: tabela de documentos por pasta, tabela de relacoes tipadas e um
diagrama Mermaid com as relacoes estruturais (parte-de, depende-de, alternativa-a,
especificado-por, implementado-por). Cole a saida na secao "Gerado" de mapa-conceitos.md.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ESTRUTURAIS = {"parte-de", "depende-de", "alternativa-a", "especificado-por", "implementado-por"}


def frontmatter(texto):
    if not texto.startswith("---"):
        return None
    fim = texto.find("\n---", 3)
    return texto[3:fim] if fim > 0 else None


def main():
    dom = sys.argv[1]
    docs = {}
    rels = []
    for p in sorted((RAIZ / dom).rglob("*.md")):
        fm = frontmatter(p.read_text(encoding="utf-8"))
        if not fm:
            continue
        i = re.search(r"^id:\s*(\S+)", fm, re.M)
        t = re.search(r"^titulo:\s*(.+)$", fm, re.M)
        tipo = re.search(r"^tipo:\s*(\S+)", fm, re.M)
        if not i:
            continue
        rel = p.relative_to(RAIZ / dom).as_posix()
        docs[i.group(1)] = (rel, (t.group(1).strip().strip('"') if t else ""), tipo.group(1) if tipo else "")
        for m in re.finditer(r"tipo:\s*([\w\-]+),\s*alvo:\s*([\w.\-]+)", fm):
            rels.append((i.group(1), m.group(1), m.group(2)))

    # ids de todos os dominios, para distinguir alvo em outro dominio de alvo inexistente
    todos = set()
    for q in RAIZ.rglob("*.md"):
        fm = frontmatter(q.read_text(encoding="utf-8"))
        if fm:
            m = re.search(r"^id:\s*(\S+)", fm, re.M)
            if m:
                todos.add(m.group(1))

    print("### Documentos\n")
    print("| Id | Tipo | Arquivo | Título |")
    print("|---|---|---|---|")
    for i, (rel, t, tipo) in sorted(docs.items()):
        print(f"| `{i}` | {tipo} | [{rel}]({rel}) | {t} |")

    print("\n### Relações tipadas\n")
    cont = defaultdict(int)
    for _, t, _ in rels:
        cont[t] += 1
    print("| Tipo | Quantidade |")
    print("|---|---|")
    for t, n in sorted(cont.items(), key=lambda x: -x[1]):
        print(f"| `{t}` | {n} |")
    print()
    print("| Origem | Tipo | Alvo |")
    print("|---|---|---|")
    for o, t, a in sorted(rels):
        falta = "" if a in docs else (" (outro domínio)" if a in todos else " (inexistente)")
        print(f"| `{o}` | {t} | `{a}`{falta} |")

    print("\n### Diagrama (relações estruturais)\n")
    print("```mermaid")
    print("graph LR")
    vistos = set()
    for o, t, a in rels:
        if t not in ESTRUTURAIS or (o, t, a) in vistos:
            continue
        vistos.add((o, t, a))
        no = lambda x: x.replace(".", "_").replace("-", "_")
        seta = {"parte-de": "-->|parte de|", "depende-de": "-.->|depende|", "alternativa-a": "<-->|alt|",
                "especificado-por": "-->|spec|", "implementado-por": "-->|impl|"}[t]
        print(f"  {no(o)}[{o}] {seta} {no(a)}[{a}]")
    print("```")


if __name__ == "__main__":
    main()
