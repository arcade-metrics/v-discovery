#!/usr/bin/env python3
"""Valida a base de conhecimento em conhecimento/.

Uso: python conhecimento/_modelo/validar.py [dominio]

Verifica, por documento com frontmatter:
- id presente, unico, com prefixo do dominio;
- alvos de `relacoes` existem (ou sao listados como lacuna);
- chaves em `fontes` existem em referencias/bibliografia.bib;
- chaves [F: chave] no corpo existem na bibliografia;
- ausencia de mencoes a produtos consumidores.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
BIB = RAIZ / "referencias" / "bibliografia.bib"
PROIBIDOS = re.compile(r"\b(vuoo|ciatec|wemoga)\b", re.I)
PREFIXOS = {
    "realtime-multiplayer": "rtm",
    "aprendizagem-adaptativa": "adp",
    "grafo-conhecimento-educacional": "kg",
    "interoperabilidade": "iop",
    "lms-e-plataformas": "lms",
    "dados-pesquisa-e-eventos": "dat",
    "learning-analytics-e-avaliacao": "lae",
    "fundamentos-pedagogicos": "ped",
    "privacidade-seguranca-e-governanca": "psg",
    "gamificacao-e-jogos": "gam",
    "acessibilidade-educacao-especial-e-dua": "acs",
}


def frontmatter(texto):
    if not texto.startswith("---"):
        return None, texto
    fim = texto.find("\n---", 3)
    if fim < 0:
        return None, texto
    return texto[3:fim], texto[fim + 4:]


def campo_lista(fm, nome):
    m = re.search(rf"^{nome}:\s*\[(.*?)\]", fm, re.M | re.S)
    if m:
        return [x.strip().strip("'\"") for x in m.group(1).split(",") if x.strip()]
    return []


def campo(fm, nome):
    m = re.search(rf"^{nome}:\s*(.+)$", fm, re.M)
    return m.group(1).strip() if m else None


def relacoes(fm):
    alvos = []
    for m in re.finditer(r"alvo:\s*([\w.\-]+)", fm):
        alvos.append(m.group(1))
    return alvos


def chaves_bib():
    if not BIB.exists():
        return set()
    return set(re.findall(r"^@\w+\{([^,\s]+),", BIB.read_text(encoding="utf-8"), re.M))


def main():
    dominios = [sys.argv[1]] if len(sys.argv) > 1 else list(PREFIXOS)
    bib = chaves_bib()
    erros, avisos = [], []
    ids = {}
    docs = []
    for d in dominios:
        for p in (RAIZ / d).rglob("*.md"):
            texto = p.read_text(encoding="utf-8")
            fm, corpo = frontmatter(texto)
            rel = p.relative_to(RAIZ)
            if PROIBIDOS.search(texto):
                erros.append(f"{rel}: menciona produto consumidor")
            if fm is None:
                if p.name not in ("README.md",):
                    avisos.append(f"{rel}: sem frontmatter")
                continue
            i = campo(fm, "id")
            if not i:
                erros.append(f"{rel}: sem id")
                continue
            if i in ids:
                erros.append(f"{rel}: id duplicado {i} (tambem em {ids[i]})")
            ids[i] = rel
            if not i.startswith(PREFIXOS[d] + "."):
                erros.append(f"{rel}: id {i} nao usa prefixo {PREFIXOS[d]}")
            docs.append((rel, fm, corpo, i))
    for rel, fm, corpo, i in docs:
        for alvo in relacoes(fm):
            if alvo not in ids and not any(alvo.startswith(k.rstrip("*")) for k in ids if k.endswith("*")):
                avisos.append(f"{rel}: relacao para id inexistente {alvo}")
        for k in campo_lista(fm, "fontes"):
            if k not in bib:
                erros.append(f"{rel}: fonte {k} nao esta em bibliografia.bib")
        for k in set(re.findall(r"\[F:\s*([\w\-:]+)", corpo)):
            k = k.split(":")[0]
            if k not in bib:
                erros.append(f"{rel}: citacao [F: {k}] sem entrada em bibliografia.bib")
    print(f"documentos: {len(docs)}  ids: {len(ids)}  chaves bib: {len(bib)}")
    for a in avisos:
        print("AVISO", a)
    for e in erros:
        print("ERRO", e)
    print(f"avisos: {len(avisos)}  erros: {len(erros)}")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
