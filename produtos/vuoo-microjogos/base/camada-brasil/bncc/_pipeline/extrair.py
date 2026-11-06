"""Extração dos quadros da BNCC homologada (BNCC_20dez_site.pdf, 20/12/2017).

Lê a camada de texto com posições (PyMuPDF) e reconstrói as tabelas pela
geometria da página: colunas pela posição x dos cabeçalhos, linhas da tabela
pelos fios horizontais desenhados, faixas (campo de atuação, eixo) pelo texto
em caixa alta antes do primeiro conteúdo de tabela. Nada é digitado à mão.
"""
import json
import re
import sys
from collections import Counter

from pathlib import Path

import fitz  # PyMuPDF

PDF = str(Path(__file__).resolve().parent.parent / 'BNCC_20dez_site.pdf')
OFFSET = 2  # página impressa = página PDF - 2
# O "(" é opcional: em EF09GE01 (PDF 393) o documento imprime o código sem ele.
COD = re.compile(r'\(?(E[IF]\d{2}[A-Z]{2}\d{2})\)')
LIGADURAS = {'\ufb01': 'fi', '\ufb02': 'fl'}
SOBRESCRITO = str.maketrans('0123456789', '\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079')

# Confer\u00eancia visual da p\u00e1gina impressa (imagem renderizada), quando a camada
# de texto n\u00e3o basta. Cada entrada: o que a p\u00e1gina imprime e onde foi conferido.
HIFEN_CONFERIDO = {  # h\u00edfen de fim de linha que \u00e9 h\u00edfen da palavra
    'gr\u00e1fico-espacial': 'PDF 159, EF69LP48',
    'p\u00f3s-escrita': 'PDF 256, unidade tem\u00e1tica de L\u00edngua Inglesa 8\u00ba ano',
}
CORRECOES_VISUAIS = {  # c\u00f3digo: (camada de texto, p\u00e1gina impressa, p\u00e1gina PDF)
    'EF07MA33': ('o n\u00famero como', 'o n\u00famero \u03c0 como', 309),
}

COMPONENTES = {'LÍNGUA PORTUGUESA': 'LP', 'ARTE': 'AR', 'EDUCAÇÃO FÍSICA': 'EF', 'LÍNGUA INGLESA': 'LI',
               'MATEMÁTICA': 'MA', 'CIÊNCIAS': 'CI', 'GEOGRAFIA': 'GE', 'HISTÓRIA': 'HI',
               'ENSINO RELIGIOSO': 'ER'}

doc = fitz.open(PDF)


def linhas(pn):
    """Linhas de texto da página PDF `pn` (1-indexada): dicts com x0,y0,x1,texto,fonte,tamanho."""
    out = []
    for b in doc[pn - 1].get_text('dict')['blocks']:
        for l in b.get('lines', []):
            tam = max(s['size'] for s in l['spans'])
            # sobrescrito numérico (cm³, ax²): span bem menor que o resto da linha
            t = ''.join(s['text'].translate(SOBRESCRITO) if s['size'] < tam - 3 and s['text'].strip().isdigit()
                        else s['text'] for s in l['spans'])
            for k, v in LIGADURAS.items():
                t = t.replace(k, v)
            t = t.replace('\u2028', ' ')
            t = re.sub(r'[\x00-\x08\x0b-\x1f]', '', t)  # controle do InDesign (ex.: \x07 ap\u00f3s '\u2022')
            if not t.strip():
                continue
            sp = l['spans'][0]
            out.append({'x0': l['bbox'][0], 'y0': l['bbox'][1], 'x1': l['bbox'][2], 't': t.rstrip(),
                        'fonte': sp['font'], 'tam': round(sp['size'], 1), 'pag': pn})
    return sorted(out, key=lambda r: (round(r['y0'], 0), r['x0']))


def fios(pn):
    """Fios horizontais da página: (x0, y, x1)."""
    return [(r.x0, r.y0, r.x1) for r in (d['rect'] for d in doc[pn - 1].get_drawings())
            if abs(r.y1 - r.y0) < 1 and r.x1 - r.x0 > 20]


# ------------------------------------------------------------ hifenização
# Léxico do próprio documento: palavras com hífen interno e palavras inteiras
# que aparecem no meio de linha (onde não há quebra), para decidir se um
# hífen de fim de linha é quebra silábica ou hífen da palavra.
TEXTO_TODO = '\n'.join(p.get_text() for p in doc)
for k, v in LIGADURAS.items():
    TEXTO_TODO = TEXTO_TODO.replace(k, v)
PALAVRAS = Counter(re.findall(r'[\wÀ-ú]+(?:-[\wÀ-ú]+)*', TEXTO_TODO))
HIFENIZACAO = []  # registro de cada decisão


def juntar(partes, ctx):
    """Une linhas de uma mesma célula. Regras declaradas:
    - fim em '/' : une sem espaço (quebra após a barra);
    - fim em '-' : decide pelo léxico do documento; ambíguo vai para conferência;
    - demais     : une com um espaço."""
    txt = ''
    for p in partes:
        p = p.strip()
        if not txt:
            txt = p
            continue
        if txt.endswith('/'):
            txt += p
        elif txt.endswith('-') and not txt.endswith(' -'):
            antes = re.search(r'([\wÀ-ú-]+)-$', txt).group(1)
            depois = re.match(r'([\wÀ-ú-]+)', p)
            depois = depois.group(1) if depois else ''
            com, sem = f'{antes}-{depois}', f'{antes}{depois}'
            n_com, n_sem = PALAVRAS.get(com, 0), PALAVRAS.get(sem, 0)
            if com in HIFEN_CONFERIDO:
                txt += p; d = f'mantém hífen (conferência visual: {HIFEN_CONFERIDO[com]})'
            elif n_com and not n_sem:
                txt += p; d = 'mantém hífen'
            elif n_sem and not n_com:
                txt = txt[:-1] + p; d = 'quebra silábica'
            elif depois[:1].isupper():
                txt += p; d = 'mantém hífen (maiúscula)'
            else:
                # sem evidência: palavra portuguesa comum é quebra silábica
                txt = txt[:-1] + p
                d = 'quebra silábica (sem evidência; conferir)' if not (n_com or n_sem) else \
                    f'AMBÍGUO com={n_com} sem={n_sem}: tratado como quebra (conferir)'
            HIFENIZACAO.append({'ctx': ctx, 'com': com, 'sem': sem, 'decisao': d})
        else:
            txt += ' ' + p
    return re.sub(r' {2,}', ' ', txt).strip()


def paragrafos(ls, gap=15.5):
    """Agrupa linhas da mesma coluna em parágrafos pelo espaçamento vertical.
    Espaço maior que o entrelinha abre parágrafo novo, exceto quando a linha
    anterior termina em '/' ou '-' ou a seguinte começa em minúscula (a frase continua)."""
    grupos, ult = [], None
    for l in ls:
        t = l['t'].strip()
        continua = ult is not None and (ult['t'].rstrip().endswith(('/', '-')) or t[:1].islower())
        # item com marcador '•' abre parágrafo; voltar à margem depois de um item recuado também
        marcador = t.startswith('•') or (ult is not None and l['x0'] < ult['x0'] - 5)
        if ult is None or marcador or (l['y0'] - ult['y0'] > gap and not continua):
            grupos.append([])
        grupos[-1].append(l)
        ult = l
    return grupos


def corrigir(codigo, texto):
    if codigo in CORRECOES_VISUAIS:
        de, para, _ = CORRECOES_VISUAIS[codigo]
        assert de in texto, f'{codigo}: trecho a corrigir não encontrado'
        texto = texto.replace(de, para, 1)
    return texto


# ------------------------------------------------------------ Ensino Fundamental
def quadros_ef():
    """Pares (esquerda, direita) dos quadros do EF, com título do quadro."""
    pares = []
    for pn in range(56, doc.page_count + 1):
        ls = linhas(pn)
        tit = [l for l in ls if l['tam'] >= 16 and l['y0'] < 200]
        cab = [l for l in ls if l['t'].strip().startswith('OBJETOS DE CONHECIMENTO') and 'Medium' in l['fonte']]
        if tit and cab:
            pares.append((pn, ' '.join(t['t'].strip() for t in tit), cab[0]['x0']))
    return pares


def extrair_ef():
    habs, avisos = [], []
    estado = {}  # carrega faixa e coluna 1 entre páginas do mesmo quadro
    for pe, titulo, x_oc in quadros_ef():
        pd = pe + 1
        base = titulo.replace('(Continuação)', '').strip()
        comp_nome, anos_quadro = [s.strip() for s in base.split('–', 1)]
        comp = COMPONENTES[comp_nome]
        if base != estado.get('quadro'):
            estado = {'quadro': base, 'faixa': None, 'faixa_texto': None, 'col1': None, 'col1_nota': None}
        L = [l for l in linhas(pe) if 110 < l['y0'] < 790]
        R = [l for l in linhas(pd) if 110 < l['y0'] < 790]
        cab_y = next(l['y0'] for l in L if l['t'].strip().startswith('OBJETOS DE CONHECIMENTO'))
        L = [l for l in L if l['y0'] > cab_y + 5]
        R = [l for l in R if l['y0'] > cab_y + 5 and not re.fullmatch(r'\d+º ANO', l['t'].strip())]
        # faixas: texto em caixa alta na coluna 1, fonte regular (campo de atuação / eixo)
        faixa_ini = [l for l in L if l['x0'] < 80 and 'Book' in l['fonte'] and
                     re.match(r'(CAMPO|EIXO|TODOS OS CAMPOS|DIMENSÃO)', l['t'].strip())]
        conteudo = [l for l in L if (l['x0'] < 80 and 'Book' not in l['fonte']) or l['x0'] >= x_oc - 2] + \
                   [l for l in R if COD.match(l['t'].strip())]
        faixas = []
        for f in faixa_ini:
            fim = min([c['y0'] for c in conteudo if c['y0'] > f['y0'] + 1] + [790])
            faixas.append((f['y0'], fim))
        def na_faixa(l):
            return any(a - 1 <= l['y0'] < b - 1 for a, b in faixas)
        faixa_anterior = estado['faixa']  # vem da página anterior do mesmo quadro
        faixas_pag = []  # (y, nome) das faixas desta página
        for a, b in faixas:
            tl = [l for l in L if a - 1 <= l['y0'] < b - 1]
            tr = [l for l in R if a - 1 <= l['y0'] < b - 1]
            txt = juntar([l['t'] for l in tl] + [l['t'] for l in tr], f'faixa p{pe}')
            nome = re.split(r' – ', txt, 1)[0] if ' – ' in txt else txt
            faixas_pag.append((a, nome))
            FAIXAS.setdefault((base, nome), {'texto': txt, 'pagina_pdf': pe})
            estado['faixa'] = nome
        def faixa_de(y):
            acima = [n for a, n in faixas_pag if a < y]
            return acima[-1] if acima else faixa_anterior
        L = [l for l in L if not na_faixa(l)]
        R = [l for l in R if not na_faixa(l)]
        # separadores de linha da tabela: só os fios da coluna de objetos (página da esquerda)
        # e as faixas. Fios da página da direita que não existem à esquerda só subdividem
        # a coluna de habilidades dentro de uma mesma célula de objetos.
        seps = sorted({round(y) for x0, y, x1 in fios(pe) if x0 >= x_oc - 15 and x1 > 540} |
                      {round(b) for a, b in faixas} | {round(a) for a, b in faixas})
        linha_de = lambda y: sum(1 for s in seps if s <= y + 2)
        # coluna 1 (unidade temática / prática): fios próprios definem as células
        seps1 = sorted({round(y) for x0, y, x1 in fios(pe) if x0 < 70 and x1 < x_oc}
                       | {round(a) for a, b in faixas} | {round(b) for a, b in faixas})
        col1 = [l for l in L if l['x0'] < x_oc - 15]
        celulas1 = {}
        for l in col1:
            k = sum(1 for s in seps1 if s <= l['y0'] + 2)
            celulas1.setdefault(k, []).append(l)
        col1_por_celula = {}
        for k, ls in celulas1.items():
            # a nota de rodapé da célula começa em '*' e vai até o fim da célula
            ini = next((i for i, l in enumerate(ls) if l['t'].lstrip().startswith('*')), len(ls))
            nome, nota = ls[:ini], ls[ini:]
            col1_por_celula[k] = (juntar([l['t'] for l in nome], f'col1 p{pe}') if nome else None,
                                  juntar([l['t'] for l in nota], f'nota p{pe}') if nota else None,
                                  min(l['y0'] for l in ls))
        def col1_de(y):
            k = sum(1 for s in seps1 if s <= y + 2)
            if k in col1_por_celula and col1_por_celula[k][0]:
                return col1_por_celula[k]
            return None
        # objetos de conhecimento por linha da tabela
        oc = {}
        for g in paragrafos([l for l in L if l['x0'] >= x_oc - 2]):
            oc.setdefault(linha_de(g[0]['y0']), []).append(juntar([l['t'] for l in g], f'oc p{pe}'))
        # habilidades: início pelo código; continuação pela mesma coluna x
        abertas = []
        for l in R:
            m = COD.match(l['t'].strip())
            if m:
                abertas.append({'codigo': m.group(1), 'x0': l['x0'], 'y0': l['y0'], 'partes': [l['t'].strip()[m.end():].strip()]})
            else:
                cand = [h for h in abertas if abs(h['x0'] - l['x0']) < 4 and h['y0'] < l['y0']]
                if not cand:
                    avisos.append(f'p{pd}: linha sem habilidade: {l["t"][:60]}')
                    continue
                max(cand, key=lambda h: h['y0'])['partes'].append(l['t'])
        for h in abertas:
            ln = linha_de(h['y0'])
            c1 = col1_de(h['y0'])
            if c1:
                estado['col1'], estado['col1_nota'] = c1[0], c1[1]
            habs.append({
                'codigo': h['codigo'], 'componente': comp, 'quadro': base, 'anos_quadro': anos_quadro,
                'faixa': faixa_de(h['y0']), 'col1': estado['col1'], 'col1_nota': estado['col1_nota'],
                'objetos': oc.get(ln, []), 'texto': corrigir(h['codigo'], juntar(h['partes'], h['codigo'])),
                'pagina_pdf': pd, 'pagina': pd - OFFSET, 'linha_tabela': ln,
            })
    return habs, avisos


FAIXAS = {}  # (quadro, nome da faixa) -> texto completo da faixa


# ------------------------------------------------------------ Educação Infantil
CAMPOS_EI = {'EO': 'O eu, o outro e o nós', 'CG': 'Corpo, gestos e movimentos',
             'TS': 'Traços, sons, cores e formas', 'EF': 'Escuta, fala, pensamento e imaginação',
             'ET': 'Espaços, tempos, quantidades, relações e transformações'}


def extrair_ei():
    """Quadros 'CAMPO DE EXPERIÊNCIAS' (PDF 45 a 52): três colunas por grupo etário.
    A linha do quadro (mesma altura nas três colunas) é registrada como está na página."""
    objs, grupos_etarios, linha_global = [], {}, {}
    for pn in range(44, 54):
        ls = [l for l in linhas(pn) if 140 < l['y0'] < 790]
        cods = [l for l in ls if COD.match(l['t'].strip())]
        if not cods:
            continue
        # cabeçalhos dos grupos etários (só na primeira página de cada campo)
        for l in ls:
            if l['tam'] < 10 and 'Book' in l['fonte'] and l['y0'] < 215:
                grupos_etarios.setdefault((pn, round(l['x0'])), []).append(l['t'])
        colunas = sorted({round(c['x0']) for c in cods})
        abertas = []
        for l in ls:
            if l['tam'] < 10 or l['t'].strip().startswith('OBJETIVOS DE APRENDIZAGEM'):
                continue
            m = COD.match(l['t'].strip())
            if m:
                abertas.append({'codigo': m.group(1), 'x0': l['x0'], 'y0': l['y0'],
                                'partes': [l['t'].strip()[m.end():].strip()]})
            else:
                cand = [h for h in abertas if abs(h['x0'] - l['x0']) < 4 and h['y0'] < l['y0']]
                max(cand, key=lambda h: h['y0'])['partes'].append(l['t'])
        alturas = sorted({round(h['y0']) for h in abertas})
        for h in abertas:
            campo = h['codigo'][4:6]
            k = (campo, pn)
            objs.append({'codigo': h['codigo'], 'campo': campo, 'grupo': h['codigo'][2:4],
                         'texto': corrigir(h['codigo'], juntar(h['partes'], h['codigo'])),
                         'pagina_pdf': pn, 'pagina': pn - OFFSET,
                         'linha_pagina': alturas.index(round(h['y0'])) + 1, 'y': round(h['y0'])})
    # linha do quadro: posição da linha contada ao longo das páginas do mesmo campo
    for campo in CAMPOS_EI:
        seq = sorted({(o['pagina_pdf'], o['y']) for o in objs if o['campo'] == campo})
        for o in objs:
            if o['campo'] == campo:
                o['linha_quadro'] = seq.index((o['pagina_pdf'], o['y'])) + 1
    for o in objs:
        del o['y']
    # rótulos dos grupos etários: os da primeira página do quadro (PDF 45), da esquerda para a direita
    p0 = min(pn for pn, x in grupos_etarios)
    rotulos = [juntar(partes, 'grupo etário') for (pn, x), partes in sorted(grupos_etarios.items()) if pn == p0]
    return objs, rotulos


# ------------------------------------------------------------ listas oficiais
def lista_numerada(pn, titulo_inicio, esperado):
    """Itens '1.' a 'n.' sob um título, na página `pn` e, se preciso, na seguinte."""
    itens, titulo = [], None
    for p in (pn, pn + 1):
        ls = linhas(p)
        if p == pn:
            i0 = next(i for i, l in enumerate(ls) if l['t'].strip().startswith(titulo_inicio))
            tit = [ls[i0]]
            for l in ls[i0 + 1:]:
                if l['tam'] == ls[i0]['tam'] and abs(l['x0'] - ls[i0]['x0']) < 2:
                    tit.append(l)
                else:
                    break
            titulo = juntar([l['t'] for l in tit], 'título')
            ls = [l for l in ls if l['y0'] > tit[-1]['y0']]
        nums = [l for l in ls if re.match(r'\d+\.\s', l['t'].strip()) and 'Light' not in l['fonte']]
        if not nums:
            continue
        x_num = nums[0]['x0']
        cont = [l for l in ls if 'Light' in l['fonte'] and x_num + 10 < l['x0'] < x_num + 25]
        for l in sorted([l for l in nums if abs(l['x0'] - x_num) < 4] + cont, key=lambda l: l['y0']):
            m = re.match(r'(\d+)\.\s+', l['t'].strip())
            if m and abs(l['x0'] - x_num) < 4:
                if int(m.group(1)) != len(itens) + 1:
                    break
                itens.append({'numero': int(m.group(1)), 'partes': [l['t'].strip()[m.end():]], 'pagina_pdf': p})
            elif itens:
                itens[-1]['partes'].append(l['t'])
        if len(itens) >= esperado:
            break
    out = [{'numero': i['numero'], 'texto': juntar(i['partes'], f'{titulo_inicio} {i["numero"]}'),
            'pagina_pdf': i['pagina_pdf'], 'pagina': i['pagina_pdf'] - OFFSET} for i in itens]
    assert len(out) == esperado, f'{titulo}: {len(out)} itens, esperado {esperado}'
    return titulo, out


LISTAS = [  # (id, página PDF do título, início do título, itens esperados)
    ('competencias-gerais', 11, 'COMPETÊNCIAS GERAIS DA BASE', 10),
    ('linguagens', 65, 'COMPETÊNCIAS ESPECÍFICAS DE LINGUAGENS', 6),
    ('lingua-portuguesa', 87, 'COMPETÊNCIAS ESPECÍFICAS DE LÍNGUA PORTUGUESA', 10),
    ('arte', 198, 'COMPETÊNCIAS ESPECÍFICAS DE ARTE', 9),
    ('educacao-fisica', 223, 'COMPETÊNCIAS ESPECÍFICAS DE EDUCAÇÃO FÍSICA', 10),
    ('lingua-inglesa', 246, 'COMPETÊNCIAS ESPECÍFICAS DE LÍNGUA INGLESA', 6),
    ('matematica-area', 267, 'COMPETÊNCIAS ESPECÍFICAS DE MATEMÁTICA', 8),
    ('ciencias-da-natureza', 324, 'COMPETÊNCIAS ESPECÍFICAS DE CIÊNCIAS DA NATUREZA', 8),
    ('ciencias-humanas', 357, 'COMPETÊNCIAS ESPECÍFICAS DE CIÊNCIAS HUMANAS', 7),
    ('geografia', 366, 'COMPETÊNCIAS ESPECÍFICAS DE GEOGRAFIA', 7),
    ('historia', 402, 'COMPETÊNCIAS ESPECÍFICAS DE HISTÓRIA', 7),
    ('ensino-religioso', 437, 'COMPETÊNCIAS ESPECÍFICAS DE ENSINO RELIGIOSO', 6),
]


def direitos_ei():
    """Seis direitos de aprendizagem (PDF 38): itens com marcador '•'."""
    ls = [l for l in linhas(38) if l['y0'] > 150 and l['y0'] < 600]
    itens = []
    for l in ls:
        t = l['t'].strip()
        if t.startswith('•'):
            itens.append([t.lstrip('•').strip()])
        elif itens and l['x0'] > 115:
            itens[-1].append(t)
    out = []
    for i, partes in enumerate(itens, 1):
        txt = juntar(partes, f'direito {i}')
        out.append({'numero': i, 'direito': re.match(r'[\wÀ-ú-]+', txt).group(0), 'texto': txt,
                    'pagina_pdf': 38, 'pagina': 36})
    assert len(out) == 6
    return out


def sintese_ei():
    """Quadro 'SÍNTESE DAS APRENDIZAGENS' (PDF 54 e 55): campo × aprendizagens."""
    out = []
    campo = None
    for pn in (54, 55):
        ls = [l for l in linhas(pn) if 125 < l['y0'] < 790]
        col1 = [l for l in ls if l['x0'] < 190]
        col2 = [l for l in ls if l['x0'] >= 190]
        rotulos = []
        for g in paragrafos(col1):
            rotulos.append((g[0]['y0'], juntar([l['t'] for l in g], 'síntese campo')))
        for g in paragrafos(col2, gap=15):
            y = g[0]['y0']
            acima = [r for r in rotulos if r[0] <= y + 2]
            if acima:
                campo = acima[-1][1]
            out.append({'campo': campo, 'texto': juntar([l['t'] for l in g], 'síntese'),
                        'pagina_pdf': pn, 'pagina': pn - OFFSET})
    return out


if __name__ == '__main__':
    habs, avisos = extrair_ef()
    faixas = [{'quadro': q, 'nome': n, **v} for (q, n), v in FAIXAS.items()]
    ei, rotulos_grupo = extrair_ei()
    listas = {}
    for id_, pn, ini, n in LISTAS:
        titulo, itens = lista_numerada(pn, ini, n)
        listas[id_] = {'titulo': titulo, 'itens': itens}
    saida = {'documento': {'arquivo': 'BNCC_20dez_site.pdf', 'paginas': doc.page_count},
             'habilidades_ef': habs, 'faixas_ef': faixas, 'objetivos_ei': ei, 'grupos_etarios_ei': rotulos_grupo,
             'direitos_ei': direitos_ei(), 'sintese_ei': sintese_ei(), 'listas': listas,
             'hifenizacao': HIFENIZACAO, 'avisos': avisos}
    json.dump(saida, open(sys.argv[1] if len(sys.argv) > 1 else 'bncc2017.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(len(habs), 'habilidades EF;', len(ei), 'objetivos EI;', len(avisos), 'avisos;',
          Counter(h['componente'] for h in habs))
    print('listas:', {k: len(v['itens']) for k, v in listas.items()})
    print('síntese:', len(saida['sintese_ei']), 'grupos:', rotulos_grupo)
    for a in avisos[:20]:
        print(' ', a)
