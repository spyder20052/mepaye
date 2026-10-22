"""Accueil : chaque grande image reçoit des versions plus légères (srcset), le navigateur charge
la plus petite qui reste nette ; le visuel du hero est chargé en priorité."""
import re, sys, hashlib, pathlib
from PIL import Image
SITE = pathlib.Path(sys.argv[1]); OUT = SITE / 'assets' / 'r'; OUT.mkdir(exist_ok=True)
# dossier -> (largeurs, attribut sizes)
RULES = {
    'assets/scenes/':  ([800, 1200, 1700, 2400], '(max-width: 760px) 205vw, min(1200px, 92vw)'),
    'assets/mockups/': ([800, 1200, 1700, 2400], '(max-width: 760px) 196vw, min(1200px, 92vw)'),
    'assets/marques/': ([360, 560, 900],          '(max-width: 760px) 76vw, 340px'),
    'assets/people/':  ([360, 560, 840],          '(max-width: 640px) 42vw, 230px'),
}
def variants(src, widths):
    f = SITE / src; im = Image.open(f); W = im.width; out = []
    h = hashlib.sha1(f.read_bytes()).hexdigest()[:8]
    for w in widths + [W]:
        if w > W or any(w == x for x, _ in out): continue
        name = f'{f.stem}-{w}-{h}.webp'; t = OUT / name
        if not t.exists():
            v = im if w == W else im.resize((w, round(im.height * w / W)), Image.LANCZOS)
            kw = {'exact': True} if v.mode == 'RGBA' else {}
            v.save(t, 'WEBP', quality=80, method=6, **kw)
        out.append((w, f'assets/r/{name}'))
    return out
html = (SITE / 'index.html').read_text()
def sub(m):
    tag, src = m.group(0), m.group(1)
    for d, (widths, sizes) in RULES.items():
        if src.startswith(d) and 'carte-' not in src:
            vs = variants(src, widths)
            srcset = ', '.join(f'{u} {w}w' for w, u in vs)
            small = vs[min(1, len(vs) - 1)][1]
            return tag.replace(f'src="{src}"', f'src="{small}" srcset="{srcset}" sizes="{sizes}"')
    return tag
html = re.sub(r'<img [^>]*?src="(assets/[^"?]+\.webp)"[^>]*>', sub, html)
# le téléphone du hero est la première image vue : chargée tout de suite, en priorité
html = re.sub(r'(<img class="stage__phone"[^>]*?)( decoding="async">)', r'\1 fetchpriority="high"\2', html)
(SITE / 'index.html').write_text(html)
print('images réactives :', html.count('srcset='))
