"""Gera as tabelas .md de PRD/padroes/brasil/bncc/ a partir do JSON de extrair.py.

Uso: python gerar_md.py <saida-de-extrair.json> <pasta PRD/padroes/brasil/bncc>"""
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

m = json.load(open(sys.argv[1], encoding='utf-8'))
OUT = Path(sys.argv[2])
SHA = '7d0004aacde591d4d898cbdf950ab7ed28e875f837dab12bb88cb15567cdf180'
FONTE = (f'> **Fonte:** *Base Nacional Comum Curricular: Educação é a Base* (Educação Infantil e Ensino Fundamental), '
         f'MEC, versão homologada de 20/12/2017, arquivo `BNCC_20dez_site.pdf` (472 páginas PDF, SHA-256 `{SHA[:16]}…`). '
         f'Transcrição linha a linha em 2026-11-04. Página impressa = página PDF − 2.')
COMP = OrderedDict([('LP', 'Língua Portuguesa'), ('AR', 'Arte'), ('EF', 'Educação Física'), ('LI', 'Língua Inglesa'),
                    ('MA', 'Matemática'), ('CI', 'Ciências'), ('GE', 'Geografia'), ('HI', 'História'),
                    ('ER', 'Ensino Religioso')])
ARQ = {'LP': '21-lingua-portuguesa', 'AR': '22-arte', 'EF': '23-educacao-fisica', 'LI': '24-lingua-inglesa',
       'MA': '25-matematica', 'CI': '26-ciencias', 'GE': '27-geografia', 'HI': '28-historia',
       'ER': '29-ensino-religioso'}
CAMPOS = OrderedDict([('EO', 'O eu, o outro e o nós'), ('CG', 'Corpo, gestos e movimentos'),
                      ('TS', 'Traços, sons, cores e formas'), ('EF', 'Escuta, fala, pensamento e imaginação'),
                      ('ET', 'Espaços, tempos, quantidades, relações e transformações')])
GRUPOS = {'01': 'Bebês', '02': 'Crianças bem pequenas', '03': 'Crianças pequenas'}
DUPLICADOS = {c for c, n in Counter(h['codigo'] for h in m['habilidades_ef']).items() if n > 1}


def e(t):
    return (t or '').replace('|', '\\|')


def pag(r):
    return f"{r['pagina']} (PDF {r['pagina_pdf']})"


def escrever(nome, texto):
    (OUT / nome).write_text(texto.rstrip() + '\n', encoding='utf-8')


# ---------------------------------------------------------------- competências
L = m['listas']
s = f'# Competências gerais da BNCC\n\n{FONTE}\n\nLista "{L["competencias-gerais"]["titulo"]}", na ordem e numeração do documento.\n\n'
s += '| Nº | Competência geral | Página |\n|---|---|---|\n'
for it in L['competencias-gerais']['itens']:
    s += f"| {it['numero']} | {e(it['texto'])} | {pag(it)} |\n"
escrever('01-competencias-gerais.md', s)

s = f'# Competências específicas do Ensino Fundamental\n\n{FONTE}\n\nUma tabela por lista do documento, na ordem em que aparecem. O título de cada seção é o título impresso.\n\n'
for k, v in L.items():
    if k == 'competencias-gerais':
        continue
    s += f"## {v['titulo'].title().replace(' De ', ' de ').replace(' Para O ', ' para o ').replace(' Da ', ' da ')}\n\n"
    s += '| Nº | Competência específica | Página |\n|---|---|---|\n'
    for it in v['itens']:
        s += f"| {it['numero']} | {e(it['texto'])} | {pag(it)} |\n"
    s += '\n'
escrever('02-competencias-especificas.md', s)

# ---------------------------------------------------------------- Educação Infantil
s = f'# Educação Infantil\n\n{FONTE}\n\n'
s += '## Grupos etários\n\nRótulos do cabeçalho dos quadros de objetivos (PDF 45).\n\n| Código no objetivo | Grupo etário (como impresso) |\n|---|---|\n'
for cod, rot in zip(['01', '02', '03'], m['grupos_etarios_ei']):
    s += f'| EI{cod} | {e(rot)} |\n'
s += '\n## Direitos de aprendizagem e desenvolvimento\n\n| Nº | Direito | Texto | Página |\n|---|---|---|---|\n'
for d in m['direitos_ei']:
    s += f"| {d['numero']} | {d['direito']} | {e(d['texto'])} | {pag(d)} |\n"
s += '\n## Campos de experiências\n\n| Sigla no código | Campo de experiências |\n|---|---|\n'
for k, v in CAMPOS.items():
    s += f'| {k} | {v} |\n'
s += ('\n## Objetivos de aprendizagem e desenvolvimento\n\nCada quadro tem três colunas (grupos etários). '
      '"Linha" é a linha do quadro em que o objetivo está impressa: objetivos na mesma linha, no mesmo campo, '
      'estão lado a lado no documento.\n\n')
for k, v in CAMPOS.items():
    objs = [o for o in m['objetivos_ei'] if o['campo'] == k]
    s += f'### Campo de experiências "{v}"\n\n| Linha | Código | Grupo | Objetivo | Página |\n|---|---|---|---|---|\n'
    for o in sorted(objs, key=lambda o: (o['linha_quadro'], o['grupo'])):
        s += f"| {o['linha_quadro']} | {o['codigo']} | {GRUPOS[o['grupo']]} | {e(o['texto'])} | {pag(o)} |\n"
    s += '\n'
s += '## Síntese das aprendizagens\n\nQuadro "SÍNTESE DAS APRENDIZAGENS" (transição para o Ensino Fundamental).\n\n| Campo de experiências | Aprendizagem | Página |\n|---|---|---|\n'
for x in m['sintese_ei']:
    s += f"| {e(x['campo'])} | {e(x['texto'])} | {pag(x)} |\n"
escrever('10-educacao-infantil.md', s)

# ---------------------------------------------------------------- Ensino Fundamental
faixa_txt = {(f['quadro'], f['nome']): f['texto'] for f in m['faixas_ef']}
for comp, nome in COMP.items():
    habs = [h for h in m['habilidades_ef'] if h['componente'] == comp]
    col1 = 'Prática de linguagem' if comp == 'LP' else 'Unidade temática'
    s = f'# {nome}: habilidades do Ensino Fundamental\n\n{FONTE}\n\n'
    s += (f'{len(habs)} habilidades, na ordem dos quadros do documento. Cada linha da tabela é uma habilidade; '
          f'"{col1}" e "Objetos de conhecimento" são as células da mesma linha do quadro impresso '
          '(vários objetos na célula aparecem separados por `<br>`).')
    if comp in ('LP', 'LI'):
        s += (' As faixas do quadro (' + ('campos de atuação' if comp == 'LP' else 'eixos') +
              ') aparecem como subtítulos, com o texto impresso na faixa.')
    s += '\n\n'
    quadro = faixa = None
    for h in habs:
        if h['quadro'] != quadro:
            quadro, faixa = h['quadro'], None
            s += f"\n## {quadro}\n\n"
            abre = True
        if h['faixa'] != faixa:
            faixa = h['faixa']
            if faixa:
                txt = faixa_txt.get((quadro, faixa), faixa)
                s += f"\n### {faixa}\n\n" + (f"> {e(txt)}\n\n" if txt != faixa else '')
            abre = True
        if abre:
            s += f'| {col1} | Objetos de conhecimento | Código | Habilidade | Página |\n|---|---|---|---|---|\n'
            abre = False
        c1 = e(h['col1'])
        if h['col1_nota']:
            c1 += f"<br>_{e(h['col1_nota']).replace('*', chr(92) + '*')}_"
        cod = h['codigo'] + (' ⚠' if h['codigo'] in DUPLICADOS else '')
        s += f"| {c1} | {'<br>'.join(e(o) for o in h['objetos'])} | {cod} | {e(h['texto'])} | {pag(h)} |\n"
    if any(h['codigo'] in DUPLICADOS for h in habs):
        s += '\n⚠ Código impresso duas vezes no documento, com textos diferentes. Ver [98-decisoes.md](98-decisoes.md), decisão 2.\n'
    escrever(f'{ARQ[comp]}.md', s)

# ---------------------------------------------------------------- índice
s = f'# Índice de códigos\n\n{FONTE}\n\n'
s += f"{len(m['objetivos_ei']) + len(m['habilidades_ef'])} registros ({len(m['objetivos_ei'])} objetivos da EI e {len(m['habilidades_ef'])} habilidades do EF), na ordem do documento.\n\n"
s += '| Código | Etapa | Campo / componente | Quadro | Página | Arquivo |\n|---|---|---|---|---|---|\n'
for o in sorted(m['objetivos_ei'], key=lambda o: (o['pagina_pdf'], o['linha_quadro'], o['grupo'])):
    s += f"| {o['codigo']} | EI | {CAMPOS[o['campo']]} | {GRUPOS[o['grupo']]} | {pag(o)} | [10](10-educacao-infantil.md) |\n"
for h in m['habilidades_ef']:
    s += f"| {h['codigo']} | EF | {COMP[h['componente']]} | {h['quadro']} | {pag(h)} | [{ARQ[h['componente']][:2]}]({ARQ[h['componente']]}.md) |\n"
escrever('90-indice-codigos.md', s)

# contagens para o README
cont = Counter(h['componente'] for h in m['habilidades_ef'])
print({COMP[k]: cont[k] for k in COMP}, 'EI', len(m['objetivos_ei']), 'síntese', len(m['sintese_ei']))
