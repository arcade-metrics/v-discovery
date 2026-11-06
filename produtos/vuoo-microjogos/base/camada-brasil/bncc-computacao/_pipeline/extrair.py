"""Extração dos quadros de *Computação na Educação Básica: Complemento à BNCC*
(BNCCComputaoCompletodiagramado.pdf, 13/04/2022, 75 páginas PDF).

Lê a camada de texto com posições (PyMuPDF) e reconstrói as tabelas pela
geometria da página: colunas pelos fios verticais (ou, na falta deles, pelo
meio entre os cabeçalhos), linhas da tabela pelos fios horizontais, e a página
dupla (habilidade à esquerda, explicação e exemplos à direita) pela altura de
cada linha. Nada é digitado à mão; as exceções estão nos mapas abaixo, cada uma
com a página conferida na imagem.

Uso: python extrair.py <saida.json>
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

import fitz  # PyMuPDF

PDF = str(Path(__file__).resolve().parent.parent / 'BNCCComputaoCompletodiagramado.pdf')
OFFSET = 4  # página impressa = página PDF - 4
COD = re.compile(r'^\((E[IFM]\d{2}CO\d{2,3})\)\s*')
LIGADURAS = {'ﬁ': 'fi', 'ﬂ': 'fl'}

# Conferência visual da página impressa (imagem renderizada), quando a camada
# de texto não basta. Cada entrada: o que a página imprime e onde foi conferido.
CODIGO_IMPRESSO = {  # código como impresso -> código reconhecido
    'EF05CO011': ('EF05CO11', 'PDF 36: impresso com três dígitos; a sequência do 5º ano vai de EF05CO01 a EF05CO11'),
}
HIFEN_CONFERIDO = {  # hífen de fim de linha que é hífen da palavra
    'vice-versa': 'PDF 33, EF05CO03 (grafia com hífen obrigatória)',
    'inglês-espanhol': 'PDF 63, EF69CO10 (mesma linha impressa traz "português-inglês")',
    'on-line': 'PDF 45, EF06CO09 (ambíguo: o documento usa "online" e "on-line"; mantém o hífen impresso)',
}

QUEBRA_SEM_HIFEN = {  # palavra partida no fim da linha sem hífen (coluna estreita)
    'responsabilidad e': ('responsabilidade', 'PDF 58, objeto de conhecimento de EF09CO06 a EF09CO09'),
}

EIXOS = {'PENSAMENTO COMPUTACIONAL': 'Pensamento Computacional', 'MUNDO DIGITAL': 'Mundo Digital',
         'CULTURA DIGITAL': 'Cultura Digital'}

ROTULOS = {'EIXO', 'OBJETO DE CONHECIMENTO', 'HABILIDADE', 'OBJETIVO DE APRENDIZAGEM', 'COMPETÊNCIA ESPECÍFICA',
           'EXPLICAÇÃO DA HABILIDADE', 'EXEMPLOS'}

doc = fitz.open(PDF)


def limpar(t):
    for k, v in LIGADURAS.items():
        t = t.replace(k, v)
    t = t.replace(' ', ' ').replace(' ', ' ')
    return re.sub(r'[\x00-\x08\x0b-\x1f]', '', t)


def palavras(pn):
    """Palavras horizontais da página PDF `pn` (1-indexada)."""
    out = []
    for x0, y0, x1, y1, t, *_ in doc[pn - 1].get_text('words'):
        t = limpar(t)
        if t.strip() and (x1 - x0) >= (y1 - y0) * 0.2:
            out.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 't': t})
    return out


def linhas_dict(pn):
    """Linhas do dicionário de texto, com a direção (para o texto rotacionado do eixo)."""
    out = []
    for b in doc[pn - 1].get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = limpar(''.join(s['text'] for s in l['spans'])).strip()
            if t:
                x0, y0, x1, y1 = l['bbox']
                out.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 't': t, 'dir': l['dir'],
                            'tam': round(max(s['size'] for s in l['spans']), 1)})
    return out


def agrupar_linhas(ws):
    """Agrupa palavras em linhas pela altura; cada linha: x0, x1, y0, texto, largura da 1ª palavra."""
    ws = sorted(ws, key=lambda w: (w['y0'], w['x0']))
    grupos = []
    for w in ws:
        if grupos and abs((w['y0'] + w['y1']) / 2 - grupos[-1]['ym']) < 3:
            grupos[-1]['ws'].append(w)
        else:
            grupos.append({'ym': (w['y0'] + w['y1']) / 2, 'ws': [w]})
    out = []
    for g in grupos:
        g['ws'].sort(key=lambda w: w['x0'])
        out.append({'x0': g['ws'][0]['x0'], 'x1': g['ws'][-1]['x1'], 'y0': min(w['y0'] for w in g['ws']),
                    't': ' '.join(w['t'] for w in g['ws']), 'w0': g['ws'][0]['x1'] - g['ws'][0]['x0']})
    return out


def dentro(ws, x0, x1, y0, y1):
    return [w for w in ws if x0 <= (w['x0'] + w['x1']) / 2 < x1 and y0 <= (w['y0'] + w['y1']) / 2 < y1]


# ------------------------------------------------------------ hifenização
TEXTO_TODO = limpar('\n'.join(p.get_text() for p in doc))
PALAVRAS = Counter(re.findall(r'[\wÀ-ú]+(?:-[\wÀ-ú]+)*', TEXTO_TODO))
HIFENIZACAO = []  # registro de cada decisão


def juntar(txt, p, ctx):
    """Une a linha `p` ao texto `txt` numa quebra de linha que não é parágrafo:
    - fim em '/' : une sem espaço;
    - fim em '-' dentro de endereço web: une sem espaço e mantém o hífen;
    - fim em '-' : decide pelo léxico do documento; ambíguo vai para conferência;
    - demais     : une com um espaço."""
    p = p.strip()
    if not txt:
        return p
    ultimo = txt.split()[-1] if txt.split() else ''
    if txt.endswith('/'):
        return txt + p
    if txt.endswith('-') and not txt.endswith(' -'):
        if '://' in ultimo or 'www.' in ultimo:
            HIFENIZACAO.append({'ctx': ctx, 'com': ultimo + p.split()[0], 'decisao': 'mantém hífen (endereço web)'})
            return txt + p
        antes = re.search(r'([\wÀ-ú-]+)-$', txt)
        antes = antes.group(1) if antes else ''
        depois = re.match(r'([\wÀ-ú-]+)', p)
        depois = depois.group(1) if depois else ''
        com, sem = f'{antes}-{depois}', f'{antes}{depois}'
        n_com, n_sem = PALAVRAS.get(com, 0), PALAVRAS.get(sem, 0)
        if com in HIFEN_CONFERIDO:
            r, d = txt + p, f'mantém hífen (conferência visual: {HIFEN_CONFERIDO[com]})'
        elif n_com and not n_sem:
            r, d = txt + p, 'mantém hífen'
        elif n_sem and not n_com:
            r, d = txt[:-1] + p, 'quebra silábica'
        elif depois[:1].isupper():
            r, d = txt + p, 'mantém hífen (maiúscula)'
        else:
            r = txt[:-1] + p
            d = 'quebra silábica (sem evidência; conferir)' if not (n_com or n_sem) else \
                f'AMBÍGUO com={n_com} sem={n_sem}: tratado como quebra (conferir)'
        HIFENIZACAO.append({'ctx': ctx, 'com': com, 'sem': sem, 'decisao': d})
        return r
    if ('://' in ultimo or ultimo.startswith('www.')) and not re.search(r'[)\].,;:]$', ultimo) \
            and re.match(r'[\w/#?=&.%-]', p) and not p[:1].isupper():
        # endereço partido sem hífen nem barra: a continuação não tem espaço
        HIFENIZACAO.append({'ctx': ctx, 'com': ultimo + p.split()[0], 'decisao': 'endereço web continuado'})
        return txt + p
    return txt + ' ' + p


def texto_corrido(ls, ctx):
    """Célula de parágrafo único (habilidade, objeto, competência): todas as linhas unidas."""
    txt = ''
    for l in ls:
        txt = juntar(txt, l['t'], ctx)
    for k, (v, onde) in QUEBRA_SEM_HIFEN.items():
        if k in txt:
            txt = txt.replace(k, v)
            HIFENIZACAO.append({'ctx': ctx, 'com': v, 'decisao': f'palavra partida sem hífen (conferência visual: {onde})'})
    return re.sub(r' {2,}', ' ', txt).strip()


MARCADOR = re.compile(r'(\d+\)|\((?:[ivx]+|[a-e])\)|•|- |Passo \(\d+\))')  # início de item de lista


def texto_estruturado(ls, ctx):
    """Célula com parágrafos e listas (explicação, exemplos). Regras declaradas:
    - espaço vertical maior que 1,5 entrelinha: parágrafo novo (linha em branco);
    - a 1ª palavra da linha seguinte caberia na linha anterior, ou a linha começa
      com marcador de lista: quebra de linha real;
    - demais: a frase continua (une como em `juntar`)."""
    if not ls:
        return ''
    gaps = [b['y0'] - a['y0'] for a, b in zip(ls, ls[1:]) if b['y0'] - a['y0'] > 5]
    entre = min(gaps) if gaps else 11.5
    larg = max(l['x1'] - l['x0'] for l in ls)
    esq = min(l['x0'] for l in ls)
    txt = ls[0]['t']
    for a, b in zip(ls, ls[1:]):
        if b['y0'] - a['y0'] > entre * 1.5:
            txt += '\n\n' + b['t']
        elif a['t'].endswith('-') and not a['t'].endswith(' -'):
            txt = juntar(txt, b['t'], ctx)
        elif (a['x1'] - esq) + 2.6 + b['w0'] < larg - 1 or MARCADOR.match(b['t']):
            txt += '\n' + b['t']
        else:
            txt = juntar(txt, b['t'], ctx)
    return re.sub(r' {2,}', ' ', txt).strip()


# ------------------------------------------------------------ geometria da tabela
def geometria(pn):
    """Topo e base da tabela, fios verticais e horizontais da página."""
    p = doc[pn - 1]
    vs, hs, fills = [], [], []
    for g in p.get_drawings():
        if g['type'] == 'f':
            fills.append(g['rect'])
        for it in g['items']:
            if it[0] != 'l':
                continue
            a, b = it[1], it[2]
            if abs(a.x - b.x) < 1 and abs(b.y - a.y) > 30:
                vs.append(round(a.x, 1))
            elif abs(a.y - b.y) < 1 and abs(b.x - a.x) > 20:
                hs.append((min(a.x, b.x), a.y, max(a.x, b.x)))
    # faixa de cabeçalho: o retângulo preenchido que contém os rótulos das colunas
    rot = [l for l in linhas_dict(pn) if l['t'] in ROTULOS]
    ym = (rot[0]['y0'] + rot[0]['y1']) / 2
    cab = [r for r in fills if r.y0 <= ym <= r.y1 and r.height < 32]
    cab = min(cab, key=lambda r: r.height)
    base = max(r.y1 for r in fills if r.y0 >= cab.y1 - 1)
    return cab.y1, base, sorted(set(vs)), hs


def colunas(pn, x_esq, x_dir, cabecalhos):
    """Limites das colunas: fios verticais; onde falta fio entre dois cabeçalhos, o meio entre eles."""
    _, _, vs, _ = geometria(pn)
    lim = sorted({x_esq, x_dir} | {x for x in vs if x_esq + 5 < x < x_dir - 5})
    ls = linhas_dict(pn)
    cab = sorted([l for l in ls if l['t'] in cabecalhos], key=lambda l: l['x0'])
    for a, b in zip(cab, cab[1:]):
        if not any(a['x1'] < x < b['x0'] for x in lim):
            lim = sorted(lim + [(a['x1'] + b['x0']) / 2])
    return list(zip(lim, lim[1:]))


def celulas(pn, col, topo, base):
    """Limites verticais das células de uma coluna: fios horizontais que a atravessam."""
    _, _, _, hs = geometria(pn)
    ys = sorted({round(y, 1) for x0, y, x1 in hs if x0 <= col[0] + 2 and x1 >= col[1] - 2 and topo + 2 < y < base - 2})
    ys = [topo] + ys + [base]
    return list(zip(ys, ys[1:]))


def celula_de(cels, y):
    for a, b in cels:
        if a <= y < b:
            return a, b
    raise ValueError(f'y={y} fora da tabela')


def titulo(pn):
    ts = [l for l in linhas_dict(pn) if l['tam'] >= 14 and l['t'].startswith('COMPUTAÇÃO')]
    return ts[0]['t'] if ts else None


def eixo_da_celula(pn, x0, x1, y0, y1):
    ls = [l for l in linhas_dict(pn) if x0 <= (l['x0'] + l['x1']) / 2 < x1 and y0 <= (l['y0'] + l['y1']) / 2 < y1]
    ls.sort(key=lambda l: (l['x0'], l['y0']) if l['dir'][1] else (l['y0'], l['x0']))
    t = re.sub(r'\s+', ' ', ' '.join(l['t'] for l in ls)).strip()
    return t


# ------------------------------------------------------------ quadros
CONFERENCIA = []  # alinhamento esquerda × direita e outras checagens


def quadros():
    pares = []
    for pn in range(1, doc.page_count):
        t = doc[pn - 1].get_text()
        if re.search(r'\(E[IFM]\d{2}CO\d+\)', t):
            pares.append((pn, pn + 1))
    return pares


def extrair():
    regs = []
    ant = {}
    for pe, pd in quadros():
        tit = titulo(pe)
        quadro = re.sub(r'\s*\(CONTINUAÇÃO\)$', '', tit)
        etapa = 'EI' if 'EDUCAÇÃO INFANTIL' in quadro else 'EM' if 'ENSINO MÉDIO' in quadro else 'EF'
        topo, base, _, _ = geometria(pe)
        cab_e = {'EI': ['EIXO', 'OBJETIVO DE APRENDIZAGEM'], 'EM': ['COMPETÊNCIA ESPECÍFICA', 'HABILIDADE'],
                 'EF': ['EIXO', 'OBJETO DE CONHECIMENTO', 'HABILIDADE']}[etapa]
        cols_e = colunas(pe, 57, 567, cab_e)
        topo_d, base_d, _, _ = geometria(pd)
        cols_d = colunas(pd, 28, 539, ['EXPLICAÇÃO DA HABILIDADE', 'EXEMPLOS'])
        ws_e, ws_d = palavras(pe), palavras(pd)
        col_h = cols_e[-1]
        cels_h = celulas(pe, col_h, topo, base)
        cels_d = celulas(pd, cols_d[0], topo_d, base_d)
        for a, b in cels_h:
            ls = agrupar_linhas(dentro(ws_e, *col_h, a, b))
            if not ls:
                continue
            txt = texto_corrido(ls, f'PDF {pe}')
            m = COD.match(txt)
            if not m:
                raise ValueError(f'PDF {pe}: célula sem código de abertura: {txt[:60]}')
            cod_imp = m.group(1)
            cod = CODIGO_IMPRESSO.get(cod_imp, (cod_imp,))[0]
            if len(COD.findall(txt)) > 1 or len(re.findall(r'\(E[IFM]\d{2}CO\d+\)', txt)) > 1:
                raise ValueError(f'PDF {pe}: mais de um código na célula')
            r = {'codigo': cod, 'etapa': etapa, 'quadro': quadro, 'texto': txt[m.end():].strip(),
                 'pagina': pe - OFFSET, 'pagina_pdf': pe, 'pagina_pdf_dir': pd}
            if cod_imp != cod:
                r['codigo_impresso'] = cod_imp
            # colunas da esquerda: a célula de cada uma que contém a linha da habilidade
            ym = (a + b) / 2
            outras = []
            for col in cols_e[:-1]:
                ca, cb = celula_de(celulas(pe, col, topo, base), ym)
                if col == cols_e[0] and etapa != 'EM':
                    outras.append(eixo_da_celula(pe, *col, ca, cb))
                else:
                    outras.append(texto_corrido(agrupar_linhas(dentro(ws_e, *col, ca, cb)), f'PDF {pe}'))
            if etapa == 'EI':
                r['eixo_impresso'] = outras[0]
            elif etapa == 'EM':
                r['competencia_texto'] = outras[0]
            elif len(outras) == 2:
                r['eixo_impresso'], r['objeto'] = outras
            elif len(outras) == 4:
                r['eixo_impresso'], r['objeto'], r['subobjeto'], r['enunciado_geral'] = outras
            else:
                raise ValueError(f'PDF {pe}: {len(cols_e)} colunas inesperadas')
            # célula vazia (continuação de página): herda a anterior do mesmo quadro, registrado
            for k in ('eixo_impresso', 'objeto', 'subobjeto', 'enunciado_geral', 'competencia_texto'):
                if k in r and not r[k]:
                    if ant.get('quadro') == quadro and ant.get(k):
                        r[k] = ant[k]
                        CONFERENCIA.append(f'{cod}: {k} vazio na PDF {pe}, herdado da linha anterior')
                    else:
                        raise ValueError(f'{cod}: {k} vazio')
            if 'eixo_impresso' in r:
                if r['eixo_impresso'] not in EIXOS:
                    raise ValueError(f'{cod}: eixo desconhecido {r["eixo_impresso"]!r}')
                r['eixo'] = EIXOS[r['eixo_impresso']]
            # página da direita: as linhas cuja altura cai dentro da célula da habilidade.
            # Em geral é uma; quando são várias, ficam em ordem como pares explicação/exemplos.
            linhas_d = [(da, db) for da, db in cels_d if a - 2 <= (da + db) / 2 < b + 2]
            for da, db in linhas_d:
                if da < a - 2 or db > b + 2:
                    raise ValueError(f'{cod}: célula da direita {da:.0f}-{db:.0f} ultrapassa a da esquerda {a:.0f}-{b:.0f}')
            if len(linhas_d) > 1:
                CONFERENCIA.append(f'{cod}: {len(linhas_d)} linhas de explicação/exemplos para uma habilidade (PDF {pd})')
            r['detalhes'] = []
            for da, db in linhas_d:
                det = {}
                if len(cols_d) == 2:
                    det['explicacao'] = texto_estruturado(agrupar_linhas(dentro(ws_d, *cols_d[0], da, db)), f'PDF {pd}')
                det['exemplos'] = texto_estruturado(agrupar_linhas(dentro(ws_d, *cols_d[-1], da, db)), f'PDF {pd}')
                r['detalhes'].append(det)
            regs.append(r)
            ant = r
    return regs


# ------------------------------------------------------------ listas numeradas
def lista_numerada(pn, esperado):
    """Itens '1.', '2.'... de uma página de texto, com a introdução (texto antes do 1º item)."""
    ls = agrupar_linhas([w for w in palavras(pn) if w['y1'] - w['y0'] < 14 and w['y0'] < 790])
    marcas = [l for l in ls if re.fullmatch(r'\d+\.', l['t'].split()[0]) and l['x0'] < 140]
    itens = []
    for i, m in enumerate(marcas):
        fim = marcas[i + 1]['y0'] - 2 if i + 1 < len(marcas) else 790
        corpo = [dict(l) for l in ls if m['y0'] - 2 <= l['y0'] < fim]
        corpo[0]['t'] = corpo[0]['t'][len(m['t'].split()[0]):].strip()
        corpo = [l for l in corpo if l['t'] and l['x0'] > 140 or l is corpo[0]]
        itens.append({'numero': int(m['t'].split()[0][:-1]), 'texto': texto_corrido(corpo, f'PDF {pn}'),
                      'pagina': pn - OFFSET, 'pagina_pdf': pn})
    if len(itens) != esperado:
        raise ValueError(f'PDF {pn}: {len(itens)} itens, esperados {esperado}')
    intro = [l for l in ls if l['x0'] > 125 and (not marcas or l['y0'] < marcas[0]['y0'] - 2) and l['y0'] > 360]
    return itens, texto_corrido(intro, f'PDF {pn}')


def main():
    regs = extrair()
    premissas, intro_ei = lista_numerada(5, 4)
    comp_ef, _ = lista_numerada(15, 7)
    comp_em, _ = lista_numerada(65, 7)
    # Competência do EM: a k-ésima célula distinta do quadro é a competência k da lista
    # (PDF 65). O texto da célula nem sempre é igual ao da lista; a diferença é registrada.
    ordem = []
    for r in regs:
        if r['etapa'] == 'EM' and r['competencia_texto'] not in ordem:
            ordem.append(r['competencia_texto'])
    if len(ordem) != len(comp_em):
        raise ValueError(f'{len(ordem)} competências no quadro do EM, {len(comp_em)} na lista')
    for k, t in enumerate(ordem, 1):
        lista = comp_em[k - 1]['texto']
        if t != lista:
            CONFERENCIA.append(f'competência {k} do EM: texto do quadro difere da lista da PDF 65')
    for r in regs:
        if r['etapa'] == 'EM':
            r['competencia'] = ordem.index(r['competencia_texto']) + 1
    out = {
        'fonte': {'arquivo': Path(PDF).name, 'paginas_pdf': doc.page_count, 'metadados': doc.metadata},
        'premissas_ei': {'introducao': intro_ei, 'itens': premissas},
        'competencias_ef': comp_ef,
        'competencias_em': comp_em,
        'aprendizagens': regs,
        'hifenizacao': HIFENIZACAO,
        'conferencia': CONFERENCIA,
    }
    Path(sys.argv[1]).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    c = Counter(r['etapa'] for r in regs)
    print(f"{len(regs)} aprendizagens {dict(c)}; premissas {len(premissas)}; competências EF {len(comp_ef)}, EM {len(comp_em)}")
    print(f"hifenização: {Counter(h['decisao'] for h in HIFENIZACAO)}")
    for x in CONFERENCIA:
        print('conferir:', x)


if __name__ == '__main__':
    main()
