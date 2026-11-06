"""Compara a extração (saída de extrair.py) com uma linhagem independente: o
`computacao.json` do dataset bncc-dados (CC BY 4.0, bncc.dev, mantido pela Profy),
usado só para comparação. Nada dele é copiado para as tabelas.

Uso: python comparar.py <saida-de-extrair.json> <computacao.json do bncc-dados>
"""
import json
import sys
from collections import Counter

m = json.load(open(sys.argv[1], encoding='utf-8'))
co = json.load(open(sys.argv[2], encoding='utf-8'))

nos = {r['codigo']: r for r in m['aprendizagens']}
eles = {h['codigo']: h for k in ('objetivos_ei', 'habilidades_ef', 'habilidades_em') for h in co[k]}
eixos = {e['id']: e['nome'] for e in co['eixos']}
objetos = {o['id']: o for o in co['objetos_conhecimento']}
comp = {c['id']: c for c in co['competencias']}
ANOS = {'1º ANO': [1], '2º ANO': [2], '3º ANO': [3], '4º ANO': [4], '5º ANO': [5], '6º ANO': [6], '7º ANO': [7],
        '8º ANO': [8], '9º ANO': [9], '1º ao 5º ANO': [1, 2, 3, 4, 5], '6º ao 9º ANO': [6, 7, 8, 9]}


def anos(r):
    for k, v in sorted(ANOS.items(), key=lambda kv: -len(kv[0])):
        if r['quadro'].endswith(k):
            return v


def norm(t):
    return ' '.join((t or '').split()).casefold()


iguais, difs = Counter(), []


def conf(item, cod, a, b):
    if a == b:
        iguais[item] += 1
    else:
        difs.append((item, cod, a, b))


print(f'Códigos: extração {len(nos)}, linhagem {len(eles)}; só na extração {sorted(set(nos) - set(eles))}; '
      f'só na linhagem {sorted(set(eles) - set(nos))}')
for cod, r in nos.items():
    h = eles.get(cod)
    if not h:
        continue
    conf('texto', cod, r['texto'], h['texto'])
    conf('página PDF', cod, r['pagina_pdf'], int(h['fonte'].get('localizador_pdf', '0').split()[-1]))
    if 'eixo' in r:
        conf('eixo', cod, norm(r['eixo']), norm(eixos.get(h.get('eixo'))))
    if r['etapa'] == 'EF':
        conf('anos', cod, anos(r), h['anos'])
        ob = [objetos[i] for i in h['objetos_conhecimento']]
        if 'subobjeto' in r:
            conf('objeto (nível 1)', cod, norm(r['objeto']), norm(objetos[ob[0]['pai']]['nome'] if ob[0]['pai'] else ob[0]['nome']))
            conf('objeto (nível 2)', cod, norm(r['subobjeto']), norm(ob[0]['nome']))
        else:
            conf('objeto', cod, norm(r['objeto']), norm(' / '.join(o['nome'] for o in ob)))
    if r['etapa'] == 'EM':
        conf('competência (número)', cod, r['competencia'], comp[h['competencia']]['numero'])
    if r['etapa'] == 'EI':
        conf('grupo etário', cod, '03', h['grupo_etario'][-2:])

listas = [('competências EF', m['competencias_ef'], 'geral_computacao'),
          ('competências EM', m['competencias_em'], 'especifica_em_computacao')]
for nome, itens, tipo in listas:
    deles = {c['numero']: c['texto'] for c in co['competencias'] if c['tipo'] == tipo}
    for i in itens:
        conf(nome, i['numero'], i['texto'], deles.get(i['numero']))

print('\n| Item | Iguais | Diferentes |\n|---|---|---|')
for item in dict.fromkeys(list(iguais) + [d[0] for d in difs]):
    print(f'| {item} | {iguais[item]} | {sum(1 for d in difs if d[0] == item)} |')
print('\nDiferenças:')
for item, cod, a, b in difs:
    print(f'- {item} {cod}\n    extração: {a!r}\n    linhagem: {b!r}')
