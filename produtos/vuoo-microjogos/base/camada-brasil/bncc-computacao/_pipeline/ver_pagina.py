"""Renderiza o trecho de uma página do PDF para conferência visual.

Uso: python ver_pagina.py <página PDF> "<texto a localizar>" <nome> [altura] [ocorrência]
Grava <nome>.png no diretório atual: a faixa da página que começa no texto.
"""
import sys
from pathlib import Path

import fitz  # PyMuPDF

d = fitz.open(str(Path(__file__).resolve().parent.parent / 'BNCCComputaoCompletodiagramado.pdf'))
pn, txt, nome = int(sys.argv[1]), sys.argv[2], sys.argv[3]
altura = float(sys.argv[4]) if len(sys.argv) > 4 else 80
k = int(sys.argv[5]) if len(sys.argv) > 5 else 0
p = d[pn - 1]
r = p.search_for(txt)[k]
p.get_pixmap(dpi=150, clip=fitz.Rect(0, r.y0 - 8, p.rect.x1, r.y0 + altura)).save(f'{nome}.png')
print('ok', nome)
