"""Vitrine publique (boutique de démonstration « Atelier Démo »), pages produit,
et page de paiement hébergée pay.mepaye.com (normale et mode test)."""
import sys, pathlib

SITE = pathlib.Path(sys.argv[1])
idx = (SITE / 'index.html').read_text()
sprite = idx[idx.index('  <svg width="0" height="0"'):idx.index('  </svg>') + len('  </svg>')]
EXTRA = '''  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="s-bag" viewBox="0 0 24 24"><path d="M5.5 8.5h13l-1 11h-11z"/><path d="M9 8.5V7a3 3 0 0 1 6 0v1.5"/></symbol>
    <symbol id="s-bolt" viewBox="0 0 24 24"><path d="M13 3.5 5.5 13.5H12l-1 7 7.5-10H12z"/></symbol>
    <symbol id="s-reload" viewBox="0 0 24 24"><path d="M19 12a7 7 0 1 1-2.1-5"/><path d="M19.5 4.5v4h-4"/></symbol>
    <symbol id="s-undo" viewBox="0 0 24 24"><path d="M9 7.5 5 11.5l4 4"/><path d="M5.5 11.5H14a4.5 4.5 0 0 1 0 9h-2"/></symbol>
    <symbol id="s-phone" viewBox="0 0 24 24"><rect x="7" y="3.5" width="10" height="17" rx="2.5"/><path d="M11 17.5h2"/></symbol>
    <symbol id="s-card" viewBox="0 0 24 24"><rect x="3.5" y="6" width="17" height="12" rx="2.5"/><path d="M3.5 10h17M7 14.5h3"/></symbol>
    <symbol id="s-x" viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></symbol>
    <symbol id="s-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/></symbol>
    <symbol id="s-play" viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></symbol>
    <symbol id="s-list" viewBox="0 0 24 24"><path d="M9 7h11M9 12h11M9 17h11M4.5 7h.01M4.5 12h.01M4.5 17h.01"/></symbol>
    <symbol id="s-image" viewBox="0 0 24 24"><rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="m4 17 5-5 4 4 2.5-2.5L20 18"/><circle cx="15.5" cy="9" r="1.5"/></symbol>
    <symbol id="s-receipt" viewBox="0 0 24 24"><path d="M6 3.5h12v17l-2-1.4-2 1.4-2-1.4-2 1.4-2-1.4-2 1.4z"/><path d="M9 8h6M9 12h6"/></symbol>
    <symbol id="s-flask" viewBox="0 0 24 24"><path d="M9.5 4h5M10.5 4v5.5L5.6 17.6A1.6 1.6 0 0 0 7 20h10a1.6 1.6 0 0 0 1.4-2.4l-4.9-8.1V4"/><path d="M7.8 14.5h8.4"/></symbol>
  </svg>'''

SHOP = {'name': 'Atelier Démo', 'init': 'A', 'slug': 'atelier-demo'}
P = [
    # slug, type, nom, prix, ventes, description, variante de couverture
    ('formation-courte-vendre-en-ligne', 'Formation', 'Formation courte : vendre en ligne', 25000, 64, 'Quatre modules vidéo pour passer de l’idée à la première vente.', 1),
    ('modele-facture-freelance', 'Template', 'Modèle de facture pour freelance', 2000, None, 'Un modèle de facture prêt à remplir, pensé pour les freelances.', 1),
    ('guide-lancer-sa-boutique', 'Ebook', 'Guide : lancer sa boutique en ligne', 5000, 65, 'Un guide de 40 pages pour ouvrir sa boutique et encaisser ses premiers paiements.', 1),
    ('calendrier-editorial-90-jours', 'Template', 'Calendrier éditorial trimestriel', 4500, None, 'Trois mois de publications planifiées, semaine par semaine.', 2),
    ('formation-comptabilite-freelance', 'Formation', 'Formation : tenir sa comptabilité de freelance', 15000, None, 'Les bases pour suivre vos revenus et vos dépenses de freelance.', 2),
    ('modeles-publications-reseaux-sociaux', 'Template', 'Pack de 30 modèles de publications', 7500, None, 'Trente modèles prêts à personnaliser pour vos réseaux sociaux.', 3),
    ('photos-produit-au-smartphone', 'Ebook', 'Ebook : des photos produit nettes au smartphone', 3500, None, 'Des photos produit nettes, avec votre seul smartphone.', 2),
]
KIND = {'Formation': 'formation', 'Template': 'template', 'Ebook': 'ebook'}
PLURAL = {'Formation': 'Formations', 'Template': 'Templates', 'Ebook': 'Ebooks'}
fmt = lambda n: f'{n:,}'.replace(',', ' ')
ARROW = '<svg aria-hidden="true"><use href="#i-arrow"/></svg>'
CHEV = '<svg aria-hidden="true"><use href="#i-chev"/></svg>'
CHECK = '<svg aria-hidden="true"><use href="#i-check"/></svg>'

# miniatures photo des produits (assets/covers/<slug>.webp) ; les autres gardent la couverture illustrée
COVERS = {'formation-courte-vendre-en-ligne', 'modele-facture-freelance', 'guide-lancer-sa-boutique', 'calendrier-editorial-90-jours', 'formation-comptabilite-freelance', 'modeles-publications-reseaux-sociaux'}
def cover_src(slug): return f'assets/covers/{slug}.webp' if slug in COVERS else ''

def cover(kind, v, big=False, slug=None):
    """Couverture du produit : sa miniature photo si elle existe, sinon l'illustration à plat aux couleurs de la boutique."""
    if slug in COVERS:
        return f'<span class="cv cv--img{" cv--big" if big else ""}" aria-hidden="true"><img src="{cover_src(slug)}" alt="" width="900" height="900" loading="lazy" decoding="async"></span>'
    if kind == 'formation':
        art = '<span class="cv__screen"><span class="cv__play"></span><span class="cv__bar"><i></i></span></span><span class="cv__chip">4 modules</span>' if v == 1 else '<span class="cv__screen"><span class="cv__play"></span><span class="cv__bar"><i></i></span></span><span class="cv__chip">Leçon 1</span>'
    elif kind == 'template':
        art = '<span class="cv__page"><b></b><i></i><i></i><u></u><u></u><u></u><u></u></span>' if v != 2 else '<span class="cv__page cv__page--cal"><b></b>' + '<u></u>' * 12 + '</span>'
        if v == 3:
            art = '<span class="cv__posts"><i></i><i></i><i></i><i></i></span>'
    else:
        art = '<span class="cv__book"><i class="cv__arch"></i><b></b><small></small></span>'
    return f'<span class="cv cv--{kind} cv--v{v}{" cv--big" if big else ""}" aria-hidden="true">{art}</span>'

def head(title, desc, css, body_cls):
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <script type="speculationrules">{{"prefetch":[{{"where":{{"href_matches":"/*"}},"eagerness":"moderate"}}]}}</script>
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#FFFFFF">
  <link rel="icon" href="assets/brand/favicon-32.png" sizes="32x32">
  <link rel="icon" href="assets/brand/symbole.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400..600&family=Geist+Mono:wght@400..500&family=Parkinsans:wght@500..700&display=swap">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="{css}">
  <script>document.documentElement.classList.add('js')</script>
</head>
<body class="{body_cls}">
{sprite}
{EXTRA}
'''

