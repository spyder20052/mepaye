"""Ajoute à chaque feuille de style et script local un numéro de version tiré de son contenu
(styles.css?v=1a2b3c4d) : un navigateur ne peut plus garder une ancienne version en cache."""
import re, sys, hashlib, pathlib

SITE = pathlib.Path(sys.argv[1])
ver = {}
def v(name):
    if name not in ver:
        f = SITE / name
        ver[name] = hashlib.sha1(f.read_bytes()).hexdigest()[:8] if f.is_file() else None
    return ver[name]

pat = re.compile(r'\b(href|src)="(/?)([a-z0-9-]+\.(?:css|js)|assets/img/[a-z0-9-]+\.webp)(?:\?v=[0-9a-f]+)?"')
def sub(m):
    h = v(m.group(3))
    return m.group(0) if not h else f'{m.group(1)}="{m.group(2)}{m.group(3)}?v={h}"'

n = 0
for f in SITE.glob('*.html'):
    s = f.read_text()
    t, k = pat.subn(sub, s)
    if t != s:
        f.write_text(t)
    n += k
print('ressources versionnées :', n)
