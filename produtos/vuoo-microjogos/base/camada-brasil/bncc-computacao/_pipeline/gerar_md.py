"""Gera as tabelas .md de PRD/padroes/brasil/bncc-computacao/ a partir do JSON de extrair.py.

Uso: python gerar_md.py <saida-de-extrair.json> <pasta PRD/padroes/brasil/bncc-computacao>"""
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

m = json.load(open(sys.argv[1], encoding='utf-8'))
OUT = Path(sys.argv[2])
SHA = '60aab0b192acf867bc582dc06678cd8f3bc597e8f1b65256fc7bf04190bb793d'
FONTE = (f'> **Fonte:** *Computação na Educação Básica: Complemento à BNCC*, arquivo `BNCCComputaoCompletodiagramado.pdf` '
         f'(75 páginas PDF, criado em 13/04/2022, SHA-256 `{SHA[:16]}…`). '
         f'Transcrição linha a linha em 2026-11-05. Página impressa = página PDF − 4.')
REGS = m['aprendizagens']


def e(t):
    """Escape para célula de tabela."""
    return (t or '').replace('|', '\\|').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')


def bloco(t):
    """Texto com parágrafos e quebras de linha, fora de tabela."""
    pars = []
    for p in (t or '').split('\n\n'):
        ls = []
        for l in p.split('\n'):
            l = l.replace('<', '&lt;').replace('>', '&gt;').replace('*', '\\*')
            l = re.sub(r'^([-+#]|\d+\.)', r'\\\1', l)
            ls.append(l)
        pars.append('<br>\n'.join(ls))
    return '\n\n'.join(pars)


def pag(r, chave='pagina_pdf'):
    return f"{r[chave] - 4} (PDF {r[chave]})"


def escrever(nome, texto):
    (OUT / nome).write_text(texto.rstrip() + '\n', encoding='utf-8')


def detalhes(r):
    out = [f"### {r['codigo']}", '', f"*{e(r['texto'])}* · página {pag(r, 'pagina_pdf_dir')}", '']
    n = len(r['detalhes'])
    for i, d in enumerate(r['detalhes'], 1):
        suf = f' ({i} de {n})' if n > 1 else ''
        if 'explicacao' in d:
            out += [f'**Explicação da habilidade{suf}**', '', bloco(d['explicacao']), '']
        out += [f'**Exemplos{suf}**', '', bloco(d['exemplos']), '']
    return out


def por_quadro(regs):
    q = OrderedDict()
    for r in regs:
        q.setdefault(r['quadro'], []).append(r)
    return q


# ---------------------------------------------------------------- premissas e competências
L = ['# Premissas e competências', '', FONTE, '',
     'As três listas numeradas do documento, como impressas. Nas competências do Ensino Médio, o texto da lista '
     'e o da coluna "Competência específica" do quadro diferem em três itens; ver [98-decisoes.md](98-decisoes.md), decisão 4.', '']
p = m['premissas_ei']
L += ['## Educação Infantil: premissas', '', f"> {p['introducao']}", '', '| Nº | Premissa | Página |', '|---|---|---|']
L += [f"| {i['numero']} | {e(i['texto'])} | {pag(i)} |" for i in p['itens']]
L += ['', '## Ensino Fundamental: competências', '', '| Nº | Competência | Página |', '|---|---|---|']
L += [f"| {i['numero']} | {e(i['texto'])} | {pag(i)} |" for i in m['competencias_ef']]
L += ['', '## Ensino Médio: competências', '', '| Nº | Competência | Página |', '|---|---|---|']
L += [f"| {i['numero']} | {e(i['texto'])} | {pag(i)} |" for i in m['competencias_em']]
escrever('01-premissas-e-competencias.md', '\n'.join(L))

# ---------------------------------------------------------------- Educação Infantil
ei = [r for r in REGS if r['etapa'] == 'EI']
L = ['# Educação Infantil: objetivos de aprendizagem', '', FONTE, '',
     f'{len(ei)} objetivos, todos do grupo etário 03 (crianças pequenas), na ordem do quadro. '
     'O quadro da EI não tem coluna de explicação: a página da direita traz só os exemplos.', '',
     '| Eixo | Código | Objetivo de aprendizagem | Página |', '|---|---|---|---|']
L += [f"| {r['eixo']} | {r['codigo']} | {e(r['texto'])} | {pag(r)} |" for r in ei]
L += ['', '## Exemplos', '']
for r in ei:
    L += detalhes(r)
escrever('10-educacao-infantil.md', '\n'.join(L))


# ---------------------------------------------------------------- Ensino Fundamental
def arquivo_ef(nome, titulo, regs, intro):
    L = [f'# {titulo}', '', FONTE, '', intro, '']
    for quadro, rs in por_quadro(regs).items():
        L += [f'## {quadro}', '']
        if 'subobjeto' in rs[0]:
            L += ['| Eixo | Objeto de conhecimento | Objeto (2º nível) | Enunciado geral (sem código) | Código | Habilidade | Página |',
                  '|---|---|---|---|---|---|---|']
            L += [f"| {r['eixo']} | {e(r['objeto'])} | {e(r['subobjeto'])} | {e(r['enunciado_geral'])} | "
                  f"{r['codigo']} | {e(r['texto'])} | {pag(r)} |" for r in rs]
        else:
            L += ['| Eixo | Objeto de conhecimento | Código | Habilidade | Página |', '|---|---|---|---|---|']
            L += [f"| {r['eixo']} | {e(r['objeto'])} | {r['codigo']} | {e(r['texto'])} | {pag(r)} |" for r in rs]
        L += ['']
    L += ['## Explicação e exemplos', '']
    for r in regs:
        L += detalhes(r)
    escrever(nome, '\n'.join(L))


ef = [r for r in REGS if r['etapa'] == 'EF']
ini = [r for r in ef if r['codigo'][2] == '0' and r['codigo'][3] in '12345' or r['codigo'][2:4] == '15']
fin = [r for r in ef if r not in ini]
arquivo_ef('20-ensino-fundamental-anos-iniciais.md', 'Ensino Fundamental, anos iniciais: habilidades', ini,
           f'{len(ini)} habilidades, na ordem dos quadros: um quadro por ano (1º ao 5º) e o quadro "por etapa" '
           '(códigos `EF15CO`). Cada linha é uma habilidade; eixo e objeto de conhecimento são as células da mesma '
           'linha do quadro impresso. A explicação e os exemplos (página da direita) vêm depois das tabelas.')
arquivo_ef('21-ensino-fundamental-anos-finais.md', 'Ensino Fundamental, anos finais: habilidades', fin,
           f'{len(fin)} habilidades, na ordem dos quadros: um quadro por ano (6º ao 9º) e o quadro "por etapa" '
           '(códigos `EF69CO`). Nos anos finais o quadro tem dois níveis de objeto de conhecimento e, sob o '
           'cabeçalho "HABILIDADE", uma coluna sem código com um enunciado que agrupa várias habilidades '
           '([98-decisoes.md](98-decisoes.md), decisão 3). A explicação e os exemplos vêm depois das tabelas.')

# ---------------------------------------------------------------- Ensino Médio
em = [r for r in REGS if r['etapa'] == 'EM']
L = ['# Ensino Médio: habilidades', '', FONTE, '',
     f'{len(em)} habilidades, agrupadas pela competência específica a que o quadro as liga. O título de cada grupo é '
     'o texto impresso na coluna "Competência específica" do quadro; o número é a posição na lista da página 61 '
     '(PDF 65). A explicação e os exemplos vêm depois das tabelas.', '']
grupos = OrderedDict()
for r in em:
    grupos.setdefault(r['competencia'], []).append(r)
for k, rs in grupos.items():
    L += [f'## Competência {k}', '', f"> {rs[0]['competencia_texto']}", '',
          '| Código | Habilidade | Página |', '|---|---|---|']
    L += [f"| {r['codigo']} | {e(r['texto'])} | {pag(r)} |" for r in rs]
    L += ['']
L += ['## Explicação e exemplos', '']
for r in em:
    L += detalhes(r)
escrever('30-ensino-medio.md', '\n'.join(L))

# ---------------------------------------------------------------- índice
ARQ = {'EI': '10', 'EM': '30'}
L = ['# Índice de códigos', '', FONTE, '',
     f'{len(REGS)} registros ({len(ei)} objetivos da EI, {len(ef)} habilidades do EF, {len(em)} do EM), na ordem do documento.', '',
     '| Código | Etapa | Eixo / competência | Quadro | Página | Arquivo |', '|---|---|---|---|---|---|']
for r in REGS:
    a = ARQ.get(r['etapa']) or ('20' if r in ini else '21')
    nome = {'10': '10-educacao-infantil', '20': '20-ensino-fundamental-anos-iniciais',
            '21': '21-ensino-fundamental-anos-finais', '30': '30-ensino-medio'}[a]
    ctx = r.get('eixo') or f"Competência {r['competencia']}"
    cod = r['codigo'] + (f" (impresso `{r['codigo_impresso']}`)" if 'codigo_impresso' in r else '')
    L.append(f"| {cod} | {r['etapa']} | {ctx} | {r['quadro'].replace('COMPUTAÇÃO - ', '').replace('COMPUTAÇÃO / ', '')} "
             f"| {pag(r)} | [{a}]({nome}.md#{r['codigo'].lower()}) |")
escrever('90-indice-codigos.md', '\n'.join(L))
print('ok')
