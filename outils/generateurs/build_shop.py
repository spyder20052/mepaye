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

def cover(kind, v, big=False):
    """Couverture illustrée à plat, aux couleurs de la boutique."""
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

# ---- suite de build_shop_base.py : écrans premium de la boutique démo ----
SALES = sum(p[4] or 0 for p in P)
GO = '<span class="sx-go" aria-hidden="true"><svg><use href="#i-arrow"/></svg></span>'
import sys as _sys; _sys.path.insert(0, str(pathlib.Path(__file__).parent))
from pm_data import PM, src as pm_src
LOGOS = ''.join(f'<img src="{pm_src(fl)}" alt="{n}" width="28" height="28">' for k, fl, n, sh, t in PM)
FORMAT = {'Formation': 'Vidéo en ligne', 'Template': 'Fichier modifiable', 'Ebook': 'PDF'}

SHOP_HEAD = f'''  <a class="skip" href="#contenu">Aller au contenu</a>
  <p class="sh-pv" data-shop-preview hidden>Aperçu de votre boutique, avec des produits d’exemple. <a href="inscription.html">Revenir à l’inscription</a></p>
  <header class="sx-top">
    <div class="sh-wrap sx-top__in">
      <a class="sh-id" href="boutique.html"><span class="sh-av" data-shop-init>{SHOP['init']}</span><span data-shop-name>{SHOP['name']}</span></a>
      <div class="sx-top__r">
        <span class="sx-cur" title="Devise de la boutique">XOF</span>
        <a class="sx-buys" href="connexion.html"><svg aria-hidden="true"><use href="#s-bag"/></svg><span>Mes achats</span></a>
      </div>
    </div>
  </header>
'''
SHOP_FOOT = f'''  <footer class="sx-foot">
    <div class="sh-wrap">
      <div class="sx-foot__top">
        <a class="sh-id" href="boutique.html"><span class="sh-av" data-shop-init>{SHOP['init']}</span><span data-shop-name>{SHOP['name']}</span></a>
        <nav aria-label="Liens de la boutique"><a href="boutique.html#produits">Produits</a><a href="boutique.html#a-propos">À propos</a><a href="connexion.html">Mes achats</a></nav>
        <nav aria-label="Informations légales"><a href="mentions-legales.html">Mentions légales</a><a href="cgv.html">CGV</a><a href="confidentialite.html">Confidentialité</a></nav>
      </div>
      <div class="sx-foot__base">
        <p>© 2026 <span data-shop-name>{SHOP['name']}</span></p>
        <a class="sh-by" href="index.html">Propulsé par <img src="assets/brand/logo.svg" alt="mepaye" width="70" height="15"></a>
      </div>
    </div>
  </footer>
'''

def card(p, wide=False):
    slug, typ, name, price, sales, desc, v = p
    extra = f'<span class="sx-c__d">{desc}</span>' if wide else ''
    sold = f'<span class="sx-c__s">{sales} ventes</span>' if sales else ''
    return f'''          <li class="sx-c{(" sx-c--" + wide) if wide else ""}" data-type="{KIND[typ]}">
            <a href="produit-{slug}.html">
              <span class="sx-c__m">{cover(KIND[typ], v)}</span>
              <span class="sx-c__b">
                <span class="sx-c__k"><span class="sx-tag">{typ}</span>{sold}</span>
                <span class="sx-c__n">{name}</span>
                {extra}
                <span class="sx-c__f"><b>{fmt(price)}<small>XOF</small></b>{GO}</span>
              </span>
            </a>
          </li>'''

def trust(cls=''):
    items = [('s-bolt', 'Accès immédiat'), ('i-lock', 'Paiement sécurisé'), ('s-undo', 'Garantie 7 jours')]
    li = ''.join(f'<li><svg aria-hidden="true"><use href="#{ic}"/></svg>{t}</li>' for ic, t in items)
    return f'<div class="sx-trust {cls}"><ul>{li}</ul><span class="sx-logos" aria-label="Moyens de paiement acceptés">{LOGOS}</span></div>'

counts = {t: sum(1 for p in P if p[1] == t) for t in PLURAL}
chips = f'<button type="button" aria-pressed="true" data-f="all">Tout <span>{len(P)}</span></button>' + ''.join(
    f'<button type="button" aria-pressed="false" data-f="{KIND[t]}">{PLURAL[t]} <span>{counts[t]}</span></button>' for t in ('Formation', 'Template', 'Ebook'))

feat = P[0]
shop_page = head(f'{SHOP["name"]} · Boutique mepaye', 'Atelier Démo, la boutique de démonstration mepaye : formations, templates et ebooks.', 'shop.css', 'shop') + SHOP_HEAD + f'''
  <main id="contenu">
    <section class="sx-hero">
      <div class="sh-wrap sx-hero__in">
        <div class="sx-hero__t">
          <p class="sx-dom"><svg aria-hidden="true"><use href="#i-lock"/></svg>{SHOP['slug']}.mepaye.com</p>
          <h1>Bienvenue sur <span data-shop-name>{SHOP['name']}</span>.</h1>
          <p class="sx-lead">Mes meilleurs produits, directement accessibles.</p>
          <dl class="sx-facts">
            <div><dt>Produits</dt><dd>{len(P)}</dd></div>
            <div><dt>Ventes</dt><dd>{SALES}</dd></div>
            <div><dt>Livraison</dt><dd>Immédiate</dd></div>
          </dl>
          <div class="sx-ctas"><a class="sx-btn" href="#produits">Voir les produits {GO}</a><a class="sx-link" href="#a-propos">À propos</a></div>
        </div>
        <a class="sx-feat" href="produit-{feat[0]}.html" aria-label="À la une : {feat[2]}, {fmt(feat[3])} XOF">
          <span class="sx-feat__arch">
            <span class="sx-feat__k">À la une</span>
            {cover('formation', 1, big=True)}
          </span>
          <span class="sx-feat__card">
            <span><small>{feat[1]} · {feat[4]} ventes</small><b>{feat[2]}</b></span>
            <span class="sx-feat__p">{fmt(feat[3])}<small>XOF</small></span>
            {GO}
          </span>
        </a>
      </div>
    </section>

    <div class="sh-wrap">{trust()}</div>

    <section class="sx-sec" id="produits" aria-labelledby="prod-t">
      <div class="sh-wrap">
        <div class="sx-head">
          <div><p class="sx-k">Catalogue</p><h2 id="prod-t">Tous mes produits</h2></div>
          <div class="sx-chips" role="group" aria-label="Filtrer par type">{chips}</div>
        </div>
        <ul class="sx-grid" data-grid>
{chr(10).join(card(p, wide={0: 'w', 3: 'w2'}.get(i)) for i, p in enumerate(P))}
        </ul>
        <p class="sx-none" data-none hidden>Aucun produit de ce type pour le moment.</p>
      </div>
    </section>

    <section class="sx-sec" id="a-propos" aria-labelledby="ab-t">
      <div class="sh-wrap">
        <div class="sx-about">
          <span class="sx-about__av" aria-hidden="true"><span data-shop-init>{SHOP['init']}</span></span>
          <div class="sx-about__t">
            <p class="sx-k">À propos</p>
            <h2 id="ab-t" data-shop-name>{SHOP['name']}</h2>
            <p>La boutique de démonstration de mepaye : de vrais produits d’exemple, pour voir une boutique en conditions réelles.</p>
          </div>
          <a class="sx-btn sx-btn--ghost" href="#produits">Voir les produits {GO}</a>
        </div>
      </div>
    </section>
  </main>
''' + SHOP_FOOT + '''  <script src="shop.js" defer></script>
</body>
</html>
'''
(SITE / 'boutique.html').write_text(shop_page)
print('écrit boutique.html')

# ---------------------------------------------------------------- pages produit
def views(kind, v):
    """Trois vues de la galerie : couverture, aperçu, sommaire (illustrations, sans contenu inventé)."""
    if kind == 'formation':
        prev = '<span class="gv gv--video"><span class="gv__screen"><span class="cv__play"></span><span class="gv__track"><i></i></span></span></span>'
        n = 4 if v == 1 else 5
        toc_ic = 's-play'
    elif kind == 'template':
        prev = '<span class="gv gv--sheet"><span class="gv__sheet"><b></b><i></i><i></i><u></u><u></u><u></u><u></u><u></u><u></u></span></span>'
        n, toc_ic = 4, 's-image'
    else:
        prev = '<span class="gv gv--spread"><span class="gv__pg"><b></b><i></i><i></i><i></i><i></i></span><span class="gv__pg"><i></i><i></i><u></u><i></i></span></span>'
        n, toc_ic = 5, 's-list'
    rows = ''.join(f'<li><span>{i:02d}</span><i style="width:{[62,48,70,54,44][i-1]}%"></i><svg><use href="#{toc_ic}"/></svg></li>' for i in range(1, n + 1))
    toc = f'<span class="gv gv--toc"><ol>{rows}</ol></span>'
    return [('Couverture', cover(kind, v, big=True)), ('Aperçu', prev), ('Sommaire', toc)]

GAR = [('s-bolt', 'Accès immédiat', 'Livré dès le paiement'), ('i-lock', 'Paiement sécurisé', 'Mobile Money et carte'), ('s-undo', 'Garantie 7 jours', 'Satisfait ou remboursé'), ('i-shield', 'Données protégées', 'Confidentialité RGPD')]

for i, p in enumerate(P):
    slug, typ, name, price, sales, desc, v = p
    kind = KIND[typ]
    others = ([q for q in P if q != p and q[1] == typ][:1] + [q for q in P if q != p and q[1] != typ])[:3]
    buy = f'data-buy data-name="{name}" data-type="{typ}" data-price="{price}"'
    vw = views(kind, v)
    stage = ''.join(f'<div class="pg__v{"" if j == 0 else ""}" id="v-{slug}-{j}" role="tabpanel" aria-label="{t}"{"" if j == 0 else " hidden"}>{h}</div>' for j, (t, h) in enumerate(vw))
    thumbs = ''.join(f'<button type="button" role="tab" aria-selected="{"true" if j == 0 else "false"}" aria-controls="v-{slug}-{j}" tabindex="{0 if j == 0 else -1}"><span class="pg__th" aria-hidden="true">{h}</span><span>{t}</span></button>' for j, (t, h) in enumerate(vw))
    sold = f'<span class="pb__sales"><i aria-hidden="true"></i>{sales} ventes</span>' if sales else ''
    html = head(f'{name} · {SHOP["name"]}', desc, 'shop.css', 'shop') + SHOP_HEAD + f'''
  <main id="contenu">
    <div class="sh-wrap">
      <nav class="sx-crumbs" aria-label="Fil d’Ariane"><a href="boutique.html" data-shop-name>{SHOP['name']}</a>{CHEV}<a href="boutique.html#produits">{PLURAL[typ]}</a>{CHEV}<span aria-current="page">{name}</span></nav>
      <div class="pp2">
        <div class="pg" data-gallery>
          <div class="pg__stage">{stage}</div>
          <div class="pg__thumbs" role="tablist" aria-label="Vues du produit">{thumbs}</div>
        </div>
        <aside class="pb" aria-label="Acheter">
          <div class="pb__in">
            <p class="pb__k"><span class="sx-tag">{typ}</span>{sold}</p>
            <h1>{name}</h1>
            <p class="pb__d">{desc}</p>
            <p class="pb__p">{fmt(price)}<small>XOF</small></p>
            <a class="sx-btn sx-btn--xl" href="paiement.html" {buy}>Acheter maintenant {GO}</a>
            <ul class="pb__ticks">
              <li>{CHECK}Accès immédiat après paiement</li>
              <li>{CHECK}Re-téléchargement illimité</li>
              <li>{CHECK}Garantie 7 jours</li>
            </ul>
            <p class="pb__pay"><span class="sx-logos" aria-label="Moyens de paiement acceptés">{LOGOS}</span></p>
          </div>
        </aside>
      </div>
    </div>

    <section class="sx-sec sx-sec--soft" aria-labelledby="desc-t">
      <div class="sh-wrap pd">
        <div class="pd__t">
          <p class="sx-k">Description</p>
          <h2 id="desc-t">À propos de ce produit</h2>
          <p>{desc}</p>
        </div>
        <dl class="pd__facts">
          <div><dt>Type</dt><dd>{typ}</dd></div>
          <div><dt>Format</dt><dd>{FORMAT[typ]}</dd></div>
          <div><dt>Livraison</dt><dd>Immédiate, par e-mail</dd></div>
          <div><dt>Prix</dt><dd>{fmt(price)} XOF</dd></div>
        </dl>
      </div>
    </section>

    <div class="sh-wrap">
      <ul class="sx-gar" aria-label="Nos garanties">
{chr(10).join(f'        <li><svg aria-hidden="true"><use href="#{ic}"/></svg><b>{t}</b><small>{d}</small></li>' for ic, t, d in GAR)}
      </ul>
    </div>

    <section class="sx-sec" aria-labelledby="more-t">
      <div class="sh-wrap">
        <div class="sx-head"><div><p class="sx-k">Dans la boutique</p><h2 id="more-t">Vous aimerez aussi</h2></div><a class="sx-link" href="boutique.html#produits">Tous les produits {CHEV}</a></div>
        <ul class="sx-grid sx-grid--3">
{chr(10).join(card(q) for q in others)}
        </ul>
      </div>
    </section>
  </main>
  <div class="pp-bar" aria-hidden="true" data-pp-bar><span><b>{fmt(price)} XOF</b><small>{name}</small></span><a class="sx-btn" href="paiement.html" tabindex="-1" {buy}>Acheter {GO}</a></div>
''' + SHOP_FOOT + '''  <script src="shop.js" defer></script>
</body>
</html>
'''
    (SITE / f'produit-{slug}.html').write_text(html)
    print(f'écrit produit-{slug}.html')

# ---------------------------------------------------------------- pay.mepaye.com
COUNTRIES = [('BJ', 'Bénin', '+229'), ('BF', 'Burkina Faso', '+226'), ('CM', 'Cameroun', '+237'), ('CI', 'Côte d’Ivoire', '+225'), ('GN', 'Guinée', '+224'), ('ML', 'Mali', '+223'), ('NE', 'Niger', '+227'), ('SN', 'Sénégal', '+221'), ('TG', 'Togo', '+228')]
METHODS = [(k, sh, pm_src(fl), 'mm') for k, fl, n, sh, t in PM if t == 'mm'] + [('carte', 'Carte bancaire', None, 'card')]

def steps(test):
    names = ['Paiement', 'Confirmation', 'Reçu'] if test else ['Informations', 'Confirmation', 'Reçu']
    cur = ' aria-current="step"'
    li = ''.join(f'<li{cur if i == 0 else ""}><span>{i+1}</span>{n}</li>' for i, n in enumerate(names))
    return f'<ol class="ck2-steps" data-ck-steps aria-label="Étapes du paiement">{li}</ol>'

def pay_page(test):
    p = P[0]
    covers = ''.join(f'<span class="ck-cv" data-ck-cv="{k}"{"" if k == "formation" else " hidden"}>{cover(k, 1)}</span>' for k in ('formation', 'template', 'ebook'))
    summary = f'''      <aside class="ck2-sum" aria-label="Récapitulatif">
        <p class="ck2-shop"><span class="sh-av" data-ck-init>{SHOP['init']}</span><span data-ck-shop>{SHOP['name']}</span></p>
        <div class="ck2-item">{covers}<span><small data-ck-type>{p[1]}</small><b data-ck-name>{p[2]}</b></span></div>
        <dl class="ck2-tot">
          <div><dt>Sous-total</dt><dd><span data-ck-price>{fmt(p[3])}</span> XOF</dd></div>
          <div><dt>Frais</dt><dd>0 XOF</dd></div>
          <div class="ck2-tot__all"><dt>Total</dt><dd><b data-ck-price>{fmt(p[3])}</b> <small>XOF</small></dd></div>
        </dl>
        <ul class="ck2-trust"><li><svg aria-hidden="true"><use href="#s-bolt"/></svg>Accès immédiat</li><li><svg aria-hidden="true"><use href="#s-undo"/></svg>Garantie 7 jours</li></ul>
      </aside>'''
    receipt = f'''          <div class="ck2-state" data-ck-state="ok" hidden tabindex="-1">
            <span class="ck-done" aria-hidden="true"><svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="28"/><path d="m20 33 8 8 16-17"/></svg></span>
            <h2>Paiement reçu</h2>
            <p data-ck-okmsg>Votre accès vous attend. La confirmation part par e-mail.</p>
            <div class="ck2-rc">
              <p class="ck2-rc__h"><svg aria-hidden="true"><use href="#s-receipt"/></svg>Reçu<span data-rc-ref>MP-0000-0000</span></p>
              <dl>
                <div><dt>Produit</dt><dd data-ck-name>{p[2]}</dd></div>
                <div><dt>Date</dt><dd data-rc-date>…</dd></div>
                <div><dt>Moyen</dt><dd data-rc-m>{'Simulation' if test else 'Wave'}</dd></div>
                <div class="ck2-rc__t"><dt>Montant payé</dt><dd><span data-ck-price>{fmt(p[3])}</span> XOF</dd></div>
              </dl>
            </div>
            <div class="ck2-go"><a class="sx-btn sx-btn--xl" href="connexion.html">Accéder à mon achat {GO}</a><a class="sx-link" href="boutique.html">Retour à la boutique</a></div>
          </div>'''
    ko = '''          <div class="ck2-state" data-ck-state="ko" hidden tabindex="-1">
            <span class="ck-done ck-done--ko" aria-hidden="true"><svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="28"/><path d="m24 24 16 16M40 24 24 40"/></svg></span>
            <h2>Paiement échoué</h2>
            <p>Aucun montant n’a été prélevé. Vous pouvez réessayer.</p>
            <div class="ck2-go"><button class="sx-btn sx-btn--xl" type="button" data-ck-retry>Réessayer</button></div>
          </div>'''
    wait = f'''          <div class="ck2-state" data-ck-state="wait" hidden tabindex="-1">
            <div class="ck2-ph" aria-hidden="true">
              <span class="ck2-ph__notch"></span>
              <span class="ck2-push"><span class="ck2-push__h"><span class="sh-av" data-ck-init>{SHOP['init']}</span><b data-ck-shop>{SHOP['name']}</b><small>maintenant</small></span><span class="ck2-push__b">Demande de paiement de <b><span data-ck-price>{fmt(p[3])}</span> XOF</b></span><span class="ck2-push__a"><i>Refuser</i><i>Valider</i></span></span>
              <span class="ck2-ph__pin"><i></i><i></i><i></i><i></i></span>
            </div>
            <h2>Confirmez sur votre téléphone</h2>
            <p data-ck-wait>Une demande de paiement a été envoyée. Validez-la avec votre code secret.</p>
            <p class="ck2-timer" aria-hidden="true"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="8"/><circle class="ck2-timer__p" cx="10" cy="10" r="8"/></svg>En attente de validation</p>
          </div>'''
    if test:
        form = f'''          <div class="ck2-form" data-ck-form>
            <div class="ck2-test"><span class="ck2-test__ic"><svg aria-hidden="true"><use href="#s-flask"/></svg></span><p><b>Mode test</b>Paiement créé avec une clé <code>mp_test_</code>. Aucun argent réel ne circule.</p></div>
            <div class="ck2-sim">
              <button class="ck2-simb ck2-simb--ok" type="button" data-ck-sim="ok"><span class="ck2-simb__ic"><svg aria-hidden="true"><use href="#i-check"/></svg></span><span><b>Simuler un paiement réussi</b><code>payment.succeeded</code></span><svg class="ck2-simb__go" aria-hidden="true"><use href="#i-arrow"/></svg></button>
              <button class="ck2-simb ck2-simb--ko" type="button" data-ck-sim="ko"><span class="ck2-simb__ic"><svg aria-hidden="true"><use href="#s-x"/></svg></span><span><b>Simuler un échec</b><code>payment.failed</code></span><svg class="ck2-simb__go" aria-hidden="true"><use href="#i-arrow"/></svg></button>
            </div>
            <p class="ck2-legal">Le webhook part avec <code>test: true</code>.</p>
          </div>'''
    else:
        opts = ''.join(f'<option value="{c}" data-dial="{d}"{" selected" if c == "BJ" else ""}>{n}</option>' for c, n, d in COUNTRIES)
        meth = ''.join(
            f'<label class="ck2-m"><input type="radio" name="moyen" value="{k}" data-kind="{kind}" data-label="{n}"{" checked" if k == "wave" else ""}><span class="ck2-m__in">'
            + (f'<img src="{img}" alt="" width="40" height="40">' if img else '<span class="ck2-m__card"><svg aria-hidden="true"><use href="#s-card"/></svg></span>')
            + f'<span class="ck2-m__n">{n}</span><span class="ck2-m__dot" aria-hidden="true"></span></span></label>' for k, n, img, kind in METHODS)
        form = f'''          <form class="ck2-form" data-ck-form novalidate>
            <fieldset>
              <legend>Vos informations</legend>
              <label class="ck2-f"><span>Nom complet</span><input name="nom" autocomplete="name" placeholder="Awa Diop" required></label>
              <label class="ck2-f"><span>E-mail</span><input name="email" type="email" autocomplete="email" placeholder="vous@exemple.com" required><small>Votre achat arrive à cette adresse.</small></label>
              <div class="ck2-row">
                <label class="ck2-f"><span>Pays</span><span class="ck2-sel"><select name="pays" autocomplete="country">{opts}</select><svg aria-hidden="true"><use href="#i-chev"/></svg></span></label>
                <label class="ck2-f"><span>Téléphone</span><span class="ck2-tel"><b data-ck-dial>+229</b><input name="tel" type="tel" inputmode="tel" autocomplete="tel-national" placeholder="01 23 45 67 89" required></span><small data-ck-telhint>Le numéro de votre compte Mobile Money.</small></label>
              </div>
            </fieldset>
            <fieldset>
              <legend>Moyen de paiement</legend>
              <div class="ck2-ms">{meth}</div>
            </fieldset>
            <p class="ck2-err" data-ck-err role="alert" hidden></p>
            <button class="sx-btn sx-btn--xl ck2-pay" type="submit"><svg aria-hidden="true"><use href="#i-lock"/></svg>Payer <span data-ck-price>{fmt(p[3])}</span> XOF</button>
            <p class="ck2-legal">Paiement chiffré. En payant, vous acceptez les <a href="cgv.html">CGV</a>.</p>
          </form>'''
    return head(('Mode test · ' if test else '') + 'Paiement · mepaye', 'Paiement sécurisé mepaye : Mobile Money et carte.', 'shop.css', 'ck' + (' ck--test' if test else '')) + f'''  <header class="ck2-top">
    <div class="sh-wrap ck2-top__in">
      <a href="index.html" aria-label="mepaye"><img src="assets/brand/logo.svg" alt="mepaye" width="84" height="18"></a>
      {'<span class="ck2-badge">Mode test</span>' if test else ''}
      <span class="ck2-url"><svg aria-hidden="true"><use href="#i-lock"/></svg>pay.mepaye.com</span>
    </div>
  </header>
  <main id="contenu" class="sh-wrap ck2">
    {steps(test)}
    <div class="ck2-grid">
      <section class="ck2-main" aria-labelledby="ck-t">
        <div class="ck2-main__in">
          <h1 id="ck-t" class="ck2-h1">{'Paiement de test' if test else 'Paiement'}</h1>
{form}
{wait}
{receipt}
{ko}
        </div>
      </section>
{summary}
    </div>
  </main>
  <footer class="ck2-foot sh-wrap"><a class="sh-by" href="index.html">Propulsé par <img src="assets/brand/logo.svg" alt="mepaye" width="70" height="15"></a><nav><a href="cgv.html">CGV</a><a href="confidentialite.html">Confidentialité</a><a href="aide.html">Aide</a></nav></footer>
  <script src="shop.js" defer></script>
</body>
</html>
'''

(SITE / 'paiement.html').write_text(pay_page(False)); print('écrit paiement.html')
(SITE / 'paiement-test.html').write_text(pay_page(True)); print('écrit paiement-test.html')
