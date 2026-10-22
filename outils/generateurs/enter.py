"""Entrée des pages : le contenu du haut de page apparaît en fondu échelonné dès le premier affichage,
sauf quand on arrive par la transition entre pages (elle s'en charge déjà)."""
import sys, pathlib
SITE = pathlib.Path(sys.argv[1])
OLD = "<script>document.documentElement.classList.add('js')</script>"
NEW = ("<script>document.documentElement.classList.add('js','enter-on');"
       "addEventListener('pagereveal',function(e){if(e.viewTransition)document.documentElement.classList.remove('enter-on')});"
       "setTimeout(function(){document.documentElement.classList.add('entered')},1600)</script>")
import re
# les polices ne bloquent plus le premier affichage : la page se dessine dès que la feuille du site est là
FONT = re.compile(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/css2\?[^"]+)">')
def font(m):
    u = m.group(1)
    return (f'<link rel="preload" as="style" href="{u}">'
            f'<link rel="stylesheet" href="{u}" media="print" onload="this.media=\'all\'">'
            f'<noscript><link rel="stylesheet" href="{u}"></noscript>')
n = 0
for f in SITE.glob('*.html'):
    s = f.read_text(); t = s
    if OLD in t: t = t.replace(OLD, NEW)
    t = FONT.sub(font, t)
    if t != s: f.write_text(t); n += 1
print('entrée ajoutée :', n)
