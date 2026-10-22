"""Réécrit tous les liens internes du site en adresses propres : /tarifs au lieu de tarifs.html,
/ au lieu de index.html. Les ancres et les paramètres sont conservés."""
import re, sys, pathlib

SITE = pathlib.Path(sys.argv[1])
pages = {p.stem for p in SITE.glob('*.html')}

def clean(m):
    attr, q, path, rest = m.group(1), m.group(2), m.group(3), m.group(4) or ''
    name = path.lstrip('/')[:-5]
    if name not in pages:
        return m.group(0)
    url = '/' if name == 'index' else f'/{name}'
    return f'{attr}={q}{url}{rest}{q}'

pat = re.compile(r'\b(href|action)=(["\'])(/?[a-z0-9-]+\.html)([#?][^"\']*)?\2')
n = 0
for f in SITE.glob('*.html'):
    s = f.read_text()
    t, k = pat.subn(clean, s)
    if k:
        f.write_text(t); n += k
print('liens réécrits :', n)
