"""Assemble les pages publiques de mepaye à partir de l'en-tête, du pied de page
et du jeu d'icônes de l'accueil, puis relie l'accueil à ces pages."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from menu import menu_html

SITE = pathlib.Path(sys.argv[1])
idx = (SITE / 'index.html').read_text()

LINKS = {
    'https://mepaye.com/fonctionnalites': 'fonctionnalites.html',
    'https://mepaye.com/tarifs': 'tarifs.html',
    'https://mepaye.com/affiliation': 'affiliation.html',
    'https://mepaye.com/aide': 'aide.html',
    'https://mepaye.com/blog': 'blog.html',
    'https://mepaye.com/cgu': 'cgu.html',
    'https://mepaye.com/cgv': 'cgv.html',
    'https://mepaye.com/politique-confidentialite': 'confidentialite.html',
    'https://mepaye.com/mentions-legales': 'mentions-legales.html',
}
def relink(s):
    for a, b in LINKS.items():
        s = s.replace(f'href="{a}"', f'href="{b}"')
    return s

EXTRA_ICONS = '''      <symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8.5" r="3.2"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><path d="M15.5 5.6a3.2 3.2 0 0 1 0 5.8M17.5 14.2a5.5 5.5 0 0 1 3 4.8"/></symbol>
      <symbol id="i-mail" viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="13" rx="2.5"/><path d="m4.5 7 7.5 6 7.5-6"/></symbol>
      <symbol id="i-target" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".6"/></symbol>
      <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3.5 5 6.2v5.3c0 4.3 3 7.6 7 9 4-1.4 7-4.7 7-9V6.2z"/><path d="m9 12 2.2 2.2L15.5 10"/></symbol>
      <symbol id="i-gift" viewBox="0 0 24 24"><rect x="4" y="8.5" width="16" height="4" rx="1"/><path d="M5.5 12.5v7h13v-7M12 8.5v11M12 8.5S10.8 4.5 8.6 4.5a2 2 0 0 0 0 4H12zM12 8.5s1.2-4 3.4-4a2 2 0 0 1 0 4H12z"/></symbol>
      <symbol id="i-help" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.5a2.5 2.5 0 0 1 4.8 1c0 1.7-2.4 2-2.4 3.5"/><circle cx="12" cy="17" r=".6"/></symbol>
      <symbol id="i-coins" viewBox="0 0 24 24"><ellipse cx="10" cy="7.5" rx="5.5" ry="2.5"/><path d="M4.5 7.5v4c0 1.4 2.5 2.5 5.5 2.5s5.5-1.1 5.5-2.5v-4"/><path d="M9 16.4c.3 1.2 2.6 2.1 5.5 2.1 3 0 5.5-1.1 5.5-2.5v-4c0-1.2-1.8-2.2-4.3-2.4"/></symbol>
      <symbol id="i-layout" viewBox="0 0 24 24"><rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="M3.5 9h17M9.5 9v10.5"/></symbol>
      <symbol id="i-cart" viewBox="0 0 24 24"><path d="M3.5 4.5h2.2l2 10.5h10.3l1.8-7.5H6.6"/><circle cx="9" cy="19" r="1.2"/><circle cx="17" cy="19" r="1.2"/></symbol>
'''
sprite = idx[idx.index('  <svg width="0" height="0"'):idx.index('  </svg>') + len('  </svg>')]
if 'id="i-users"' not in sprite:
    sprite = sprite.replace('  </svg>', EXTRA_ICONS + '  </svg>')
    idx = idx.replace(idx[idx.index('  <svg width="0" height="0"'):idx.index('  </svg>') + len('  </svg>')], sprite)
footer = relink(idx[idx.index('  <footer class="foot">'):idx.index('  </footer>') + len('  </footer>')])
footer = footer.replace('href="#api"', 'href="developpeurs.html"')

NAV = [('fonctionnalites.html', 'Fonctionnalités'), ('tarifs.html', 'Tarifs'), ('affiliation.html', 'Affiliation'),
       ('developpeurs.html', 'Développeurs'), ('aide.html', 'Aide'), ('blog.html', 'Blog')]

def icon(name, cls='ic'):
    return f'<span class="{cls}" aria-hidden="true"><svg><use href="#i-{name}"/></svg></span>'

def page(slug, title, desc, body, current=None):
    links = '\n'.join(
        f'            <a href="{h}"' + (' aria-current="page"' if h == current else '') + f'>{t}</a>' for h, t in NAV)
    mlinks = '\n'.join(f'        <li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <script type="speculationrules">{{"prefetch":[{{"where":{{"href_matches":"/*"}},"eagerness":"moderate"}}]}}</script>
  <title>{title} · mepaye</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#FFFFFF">
  <meta property="og:title" content="{title} · mepaye">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://mepaye.com/{slug}">
  <link rel="icon" href="assets/brand/favicon-32.png" sizes="32x32">
  <link rel="icon" href="assets/brand/symbole.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400..600&family=Geist+Mono:wght@400..500&family=Parkinsans:wght@500..700&display=swap">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="pages.css">
  <link rel="stylesheet" href="annex.css">
  <script>document.documentElement.classList.add('js')</script>
</head>
<body class="page">
{sprite}

  <a class="skip" href="#contenu">Aller au contenu</a>

  <header class="nav" data-nav>
    <div class="nav__bar" data-nav-bar>
      <div class="nav__in">
        <a class="nav__logo" href="index.html" aria-label="mepaye, accueil"><img class="nav__word" src="assets/brand/logo.svg" alt="" width="94" height="20"><img class="nav__sym" src="assets/brand/symbole.svg" alt="" width="30" height="18"></a>
        <div class="nav__mid">
          <nav class="nav__set nav__set--site" aria-label="Navigation principale">
{links}
          </nav>
        </div>
        <div class="nav__act">
          <a class="nav__login" href="https://mepaye.com/auth/connexion">Connexion</a>
          <a class="pill pill--blue" href="https://mepaye.com/auth/inscription">Commencer</a>
          <button class="burger" type="button" aria-expanded="false" aria-controls="menu" data-burger><span class="sr-only">Ouvrir le menu</span><i></i><i></i></button>
        </div>
      </div>
    </div>
  </header>

{menu_html(current)}

  <main id="contenu">
{body}
  </main>

{footer}

  <script src="pages.js" defer></script>
  <script src="annex.js" defer></script>
</body>
</html>
'''

ARROW = '<span class="btn__ic" aria-hidden="true"><svg><use href="#i-arrow"/></svg></span>'
CHEV = '<svg aria-hidden="true"><use href="#i-chev"/></svg>'
CHECK = '<svg aria-hidden="true"><use href="#i-check"/></svg>'

def band(t, p, cta='Commencer gratuitement', href='https://mepaye.com/auth/inscription'):
    return f'''    <section class="pg-sec">
      <div class="wrap">
        <div class="band" data-reveal>
          <div><h2>{t}</h2><p>{p}</p></div>
          <a class="btn btn--lg" href="{href}">{cta} {ARROW}</a>
        </div>
      </div>
    </section>'''

def hero(kicker, h1, lead, extra='', plain=False):
    return f'''    <section class="pg-hero{' pg-hero--plain' if plain else ''}">
      <div class="wrap">
        <p class="kicker">{kicker}</p>
        <h1 class="pg-h1">{h1}</h1>
        <p class="lead">{lead}</p>
{extra}
      </div>
    </section>'''

PAY_CHIPS = '''        <div class="chips">
          <span class="chip"><img src="assets/logos/wave.webp" alt="">Wave</span>
          <span class="chip"><img src="assets/logos/orange.svg" alt="">Orange Money</span>
          <span class="chip"><img src="assets/logos/mtn-momo.webp" alt="">MTN MoMo</span>
          <span class="chip"><img src="assets/logos/moov-money.webp" alt="">Moov Money</span>
          <span class="chip"><img src="assets/logos/visa.svg" alt="">Visa</span>
          <span class="chip"><img src="assets/logos/mastercard.svg" alt="">Mastercard</span>
        </div>'''

# ------------------------------------------------------------------ Fonctionnalités
GROUPS = [
    ('01', 'Créer', 'De l’idée au produit prêt à vendre.', [
        ('spark', 'Création IA', 'Ebooks, formations, templates : l’IA rédige, vous validez.', ['Ebook', 'Formation', 'Template'], True),
        ('layout', 'Créateur de page de vente', 'Glissez, déposez, publiez. Sans code.', ['Glisser-déposer'], False),
        ('play', 'Formations complètes', 'Modules, vidéos, quiz et certificats.', ['Quiz', 'Certificats'], False),
    ]),
    ('02', 'Vendre', 'Une vitrine à votre image, payée comme vos clients le veulent.', [
        ('store', 'Boutique personnalisée', 'votrenom.mepaye.shop ou votre domaine. Plus de 15 thèmes.', ['Domaine personnalisé', '15+ thèmes'], False),
        ('wallet', 'Paiement multi-moyens', 'Mobile Money, carte, PayPal. Payé en moins de 30 secondes.', ['Mobile Money', 'Carte', 'PayPal'], False),
        ('link', 'Affiliation double', 'Vos clients vendent pour vous. Gains partagés à chaque vente.', ['25 % à vie', 'Cookie 30 j'], False),
        ('users', 'Communautés intégrées', 'Un espace privé, réservé à vos acheteurs.', ['Accès réservé'], False),
    ]),
    ('03', 'Encaisser', 'Votre argent, vite et en sécurité.', [
        ('up', 'Retraits en moins de 2 h', 'Vos gains arrivent sur votre Mobile Money.', ['Moins de 2 h'], True),
        ('shield', 'Confiance et sécurité', 'Identité vérifiée, liens signés, litiges gérés.', ['KYC', '2FA', 'RGPD'], False),
        ('book', 'Espace acheteur', 'Vos clients retrouvent leurs achats à vie.', ['Accès à vie'], False),
    ]),
    ('04', 'Grandir', 'Automatiser et mesurer pour vendre plus.', [
        ('mail', 'Automatisations e-mail', 'Bienvenue, panier abandonné, relances : envoyés tout seuls.', ['Panier abandonné', 'Upsell'], False),
        ('trend', 'Analytics et Spotlight', 'Vos revenus et vos ventes, en temps réel.', ['Temps réel', 'UTM'], False),
        ('target', 'Tracking 9 pixels', 'Meta, TikTok, Google : mesurez vos publicités.', ['Meta', 'TikTok', 'GA4'], False),
    ]),
]
def fx_card(ic, t, p, tags, feat):
    chips = ''.join(f'<span class="chip">{x}</span>' for x in tags)
    return f'''              <article class="fx{' fx--feat' if feat else ''}" data-reveal>
                {icon(ic)}
                <h3>{t}</h3>
                <p>{p}</p>
                <div class="chips">{chips}</div>
              </article>'''
fx_body = hero('13 modules · 1 plateforme', 'Tout ce qu’il faut <em>pour vendre</em>.',
    'Créer, vendre, livrer, analyser : un seul outil au lieu de six.',
    f'''        <div class="pg-ctas">
          <a class="btn btn--lg" href="https://mepaye.com/auth/inscription">Commencer gratuitement {ARROW}</a>
          <a class="link" href="tarifs.html">Voir les tarifs {CHEV}</a>
        </div>''')
fx_body += '\n    <section class="pg-sec pg-sec--tight">\n      <div class="wrap">\n'
for n, t, p, cards in GROUPS:
    fx_body += f'''        <div class="fx-group">
          <div class="fx-group__h" data-reveal><p class="fx-group__n">{n}</p><h2 class="fx-group__t">{t}</h2><p class="fx-group__p">{p}</p></div>
          <div class="fx-grid">
''' + '\n'.join(fx_card(*c) for c in cards) + '''
          </div>
        </div>
'''
fx_body += '      </div>\n    </section>\n' + band('Prêt à essayer ?', 'Compte créé en 30 secondes. Aucune carte bancaire requise.')

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/fx_page.py').read())

# ------------------------------------------------------------------ Tarifs
ph = idx[idx.index('        <div class="ph" data-reveal>'):idx.index('      </div>\n    </section>', idx.index('        <div class="ph" data-reveal>'))]
ph = relink(ph).replace('<p class="kicker">Tarifs</p>', '<p class="kicker">Commission</p>').replace('<h2 class="h2" id="price-title">Un seul tarif. Rien d’autre.</h2>', '<h2 class="h2">On se paie quand vous vendez.</h2>')
PACKS = [('Découverte', '2 500', '100', None, False), ('Starter', '6 500', '300', '+8 % de crédits offerts', False),
         ('Pro', '15 000', '800', '+15 % de crédits offerts', True), ('Business', '33 000', '2 000', '+25 % de crédits offerts', False),
         ('Agence', '75 000', '5 000', '+33 % de crédits offerts', False)]
packs = '\n'.join(f'''          <article class="pack{' pack--pro is-sel' if pro else ''}" data-pack data-reveal>
            {'<span class="pack__flag">Le plus choisi</span>' if pro else ''}
            <p class="pack__n">{n}</p>
            <p class="pack__p">{p} <small>XOF</small></p>
            <p class="pack__c"><b>{c}</b> crédits IA</p>
            <span class="pack__bonus{'' if b else ' pack__bonus--none'}">{b or 'Pour tester'}</span>
            <a class="pack__cta" href="https://mepaye.com/auth/inscription">Choisir {n}</a>
          </article>''' for n, p, c, b, pro in PACKS)
tarifs_body = hero('Sans abonnement · Sans frais cachés', 'Des tarifs simples, <em>transparents</em>.',
    '5 % par vente. Des crédits IA seulement si vous en avez besoin.', PAY_CHIPS) + f'''
    <section class="pg-sec pg-sec--tight pricing">
      <div class="wrap">
{ph}      </div>
    </section>

    <section class="pg-sec pg-sec--surf">
      <div class="wrap">
        <header class="pg-head pg-head--center" data-reveal>
          <p class="kicker">Crédits IA</p>
          <h2 class="h2">Un pack, autant de produits que vous voulez.</h2>
          <p class="lead">Plus le pack est grand, plus vous recevez de crédits offerts.</p>
        </header>
        <p class="scale" data-reveal><span>1 ebook = <b>50 crédits</b></span><span>1 formation = <b>80 crédits</b></span><span>Description IA = <b>5 crédits</b></span></p>
        <div class="packs">
{packs}
        </div>
      </div>
    </section>

    <section class="pg-sec">
      <div class="wrap">
        <div class="duo">
          <article class="card card--blue" data-reveal>
            {icon('coins', 'ic ic--white')}
            <h3>Payez vos crédits avec votre wallet mepaye</h3>
            <p>Payez avec le solde de vos ventes : +10 % de crédits offerts.</p>
            <a class="link" href="https://mepaye.com/aide/demander-retrait-gains">Comment retirer mes gains {CHEV}</a>
          </article>
          <article class="card" data-reveal>
            {icon('store', 'ic ic--white')}
            <h3>Jusqu’à 5 boutiques avec un seul compte</h3>
            <p>Une marque par boutique, sans frais en plus.</p>
            <a class="link" href="fonctionnalites.html">Voir les fonctionnalités {CHEV}</a>
          </article>
        </div>
      </div>
    </section>

    <section class="pg-sec pg-sec--tight">
      <div class="wrap">
        <header class="pg-head" data-reveal><p class="kicker">Comment ça marche</p><h2 class="h2">Trois étapes, aucune surprise.</h2></header>
        <ol class="hsteps">
          <li class="hstep" data-reveal><span class="hstep__n">1</span><h3>Choisissez un pack de crédits</h3><p>Dès 2 500 XOF pour tester.</p></li>
          <li class="hstep" data-reveal><span class="hstep__n">2</span><h3>Créez autant de produits que vous voulez</h3><p>Chaque création IA utilise quelques crédits.</p></li>
          <li class="hstep" data-reveal><span class="hstep__n">3</span><h3>Vendez et encaissez en 2 h</h3><p>5 % par vente, rien d’autre.</p></li>
        </ol>
      </div>
    </section>
''' + band('Commencez gratuitement.', 'Création de boutique gratuite. Vous ne payez que lorsque vous vendez.')

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/tarifs_page.py').read())

# ------------------------------------------------------------------ Affiliation
aff_body = hero('Programme double', 'Gagnez de l’argent en <em>recommandant</em> mepaye.',
    '25 % à vie sur vos filleuls. Jusqu’à 60 % sur les produits d’autres créateurs.',
    f'''        <div class="pg-ctas">
          <a class="btn btn--lg" href="https://mepaye.com/auth/inscription">Devenir affilié {ARROW}</a>
          <a class="link" href="https://mepaye.com/aide/lancer-programme-affiliation">Lancer mon propre programme {CHEV}</a>
        </div>''') + f'''
    <section class="pg-sec pg-sec--tight">
      <div class="wrap">
        <div class="prog">
          <article class="prog__c" data-reveal>
            <p class="kicker">Affiliation plateforme</p>
            <p class="prog__rate">25<small> % à vie</small></p>
            <h2>Recommandez mepaye à d’autres créateurs.</h2>
            <p>25 % à vie sur leurs achats de crédits.</p>
            <ul class="ticks">
              <li>{CHECK}Un lien unique à votre pseudo</li>
              <li>{CHECK}Cookie de 30 jours</li>
              <li>{CHECK}Bannières et scripts WhatsApp fournis</li>
              <li>{CHECK}Paiement en Mobile Money ou sur votre wallet</li>
            </ul>
            <p class="reflink"><span>mepaye.com/r/votre-pseudo</span><b>Copier</b></p>
          </article>
          <article class="prog__c prog__c--navy" data-reveal>
            <p class="kicker kicker--light">Affiliation produits</p>
            <p class="prog__rate">20–60<small> %</small></p>
            <h2>Faites connaître les produits d’autres créateurs.</h2>
            <p>Commission fixée par chaque créateur.</p>
            <ul class="ticks">
              <li>{CHECK}Partage instantané à chaque vente</li>
              <li>{CHECK}Classement mensuel des affiliés</li>
              <li>{CHECK}Suivi en temps réel</li>
            </ul>
            <div class="tiers" aria-label="Niveaux d’affilié">
              <span class="tier" style="--c:#C98A4B"><i></i>Bronze</span>
              <span class="tier" style="--c:#C9D3E3"><i></i>Silver</span>
              <span class="tier" style="--c:#E3BE62"><i></i>Gold</span>
              <span class="tier" style="--c:#8DD3F5"><i></i>Diamond</span>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="pg-sec pg-sec--surf">
      <div class="wrap">
        <header class="pg-head pg-head--center" data-reveal><p class="kicker">Simulateur</p><h2 class="h2">Combien pouvez-vous gagner ?</h2></header>
        <div class="sim" data-reveal>
          <div class="sim__in">
            <label class="range"><span class="range__top"><span class="field__l">Prix du produit</span><output data-aff-price-out>14 900 XOF</output></span><input type="range" min="1000" max="100000" step="500" value="14900" data-aff-price aria-label="Prix du produit en XOF"></label>
            <label class="range"><span class="range__top"><span class="field__l">Commission fixée par le créateur</span><output data-aff-rate-out>30 %</output></span><input type="range" min="20" max="60" step="5" value="30" data-aff-rate aria-label="Commission, de 20 à 60 %"></label>
            <label class="range"><span class="range__top"><span class="field__l">Ventes par mois</span><output data-aff-n-out>20</output></span><input type="range" min="1" max="200" step="1" value="20" data-aff-n aria-label="Ventes par mois"></label>
          </div>
          <div class="sim__out" aria-live="polite">
            <p>Vous gagnez, chaque mois</p>
            <b data-aff-total>89 400 XOF</b>
            <p class="sim__one"><span>Par vente</span><b data-aff-one>4 470 XOF</b></p>
          </div>
        </div>
      </div>
    </section>

    <section class="pg-sec">
      <div class="wrap">
        <article class="card card--blue" data-reveal>
          {icon('gift', 'ic ic--white')}
          <h3>Convertissez vos gains en crédits</h3>
          <p>+10 % de crédits IA offerts.</p>
        </article>
      </div>
    </section>
''' + band('Devenez affilié.', 'Votre lien est prêt dès la création de votre compte.', 'Devenir affilié')

# ------------------------------------------------------------------ Pages ajoutées (Développeurs, docs, ebook, à propos, contact, compte, 404)
exec(open(str(pathlib.Path(__file__).resolve().parent) + '/more_pages.py').read())

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/aff_page.py').read())

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/dev_page2.py').read())

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/ebook_page.py').read())

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/secondary_pages.py').read())

# ------------------------------------------------------------------ Centre d'aide
HELP = [
    ('cart', 'Pour les acheteurs', 'Acheter et recevoir vos produits', [
        ('Acheter un produit sur mepaye et recevoir sa commande', 'acheter-recevoir-produit-mepaye'),
        ('Demander un remboursement après un achat', 'demander-remboursement')]),
    ('store', 'Pour les créateurs', 'Lancer et développer votre boutique', [
        ('Créer son compte mepaye et configurer sa première boutique', 'creer-compte-configurer-boutique'),
        ('Quel type de produit créer sur mepaye', 'choisir-type-produit'),
        ('Vendre son premier produit digital en 7 jours', 'vendre-premier-produit-7-jours'),
        ('Utiliser l’IA mepaye pour créer un ebook', 'utiliser-ia-creer-ebook'),
        ('Lancer son programme d’affiliation pour multiplier ses ventes', 'lancer-programme-affiliation')]),
    ('wallet', 'Paiements et retraits', 'Encaisser, retirer, vérifier votre identité', [
        ('Comment fonctionne le paiement Mobile Money sur mepaye', 'comment-fonctionne-mobile-money'),
        ('La commission mepaye de 5 % : comment elle est calculée', 'commission-5-pourcent-comment-calculee'),
        ('Demander un retrait de gains depuis votre wallet', 'demander-retrait-gains'),
        ('Vérification d’identité (KYC) sur mepaye', 'verification-identite-kyc')]),
    ('help', 'FAQ générale', 'Une question qui ne rentre dans aucune case', [
        ('Contacter le support mepaye', 'contacter-support-mepaye')]),
]
HELP_IDS = ['acheteurs', 'createurs', 'paiements', 'support']
def hlink(a, s_):
    href = f'https://mepaye.com/aide/{s_}'
    return f'<li data-help-item><a href="{href}"><span>{a}</span><svg aria-hidden="true"><use href="#i-chev"/></svg></a></li>'
topics = '\n'.join(f"""          <a class="hc-topic" href="#{HELP_IDS[k]}" data-reveal>
            {icon(ic, 'ic')}
            <b>{t}</b>
            <span>{sub}</span>
            <small>{len(items)} article{'s' if len(items) > 1 else ''} <svg aria-hidden="true"><use href="#i-arrow"/></svg></small>
          </a>""" for k, (ic, t, sub, items) in enumerate(HELP))
POP = [('wallet', 'Paiements et retraits', 'Demander un retrait de gains depuis votre wallet', 'Transférez le solde de votre wallet vers votre compte Mobile Money, généralement en moins de 2 heures.', 'https://mepaye.com/aide/demander-retrait-gains'),
       ('coins', 'Paiements et retraits', 'La commission mepaye de 5 % : comment elle est calculée', '5 % prélevés uniquement sur les ventes encaissées, plus les frais de l’opérateur Mobile Money.', 'https://mepaye.com/aide/commission-5-pourcent-comment-calculee'),
       ('store', 'Pour les créateurs', 'Créer son compte mepaye et configurer sa première boutique', 'Inscription gratuite, sans carte bancaire : votre boutique est en ligne en quelques minutes.', 'https://mepaye.com/aide/creer-compte-configurer-boutique')]
popular = '\n'.join(f"""          <a class="hc-pop" href="{h}" data-reveal>
            {icon(ic, 'ic ic--white')}
            <span class="hc-pop__k">{k}</span>
            <b>{t}</b>
            <span class="hc-pop__p">{d}</span>
            <span class="hc-pop__more">Lire l’article <svg aria-hidden="true"><use href="#i-arrow"/></svg></span>
          </a>""" for ic, k, t, d, h in POP)
cats = '\n'.join(f"""        <section class="hc-cat" id="{HELP_IDS[k]}" data-help-card>
          <div class="hc-cat__h" data-reveal>{icon(ic, 'ic')}<h2>{t}</h2><p>{sub}</p></div>
          <ul class="hc-list" data-reveal>
""" + '\n'.join('            ' + hlink(a, s_) for a, s_ in items) + """
          </ul>
        </section>""" for k, (ic, t, sub, items) in enumerate(HELP))
QUICK = ['Retrait', 'Commission', 'KYC', 'Remboursement', 'Mobile Money']
quick = ''.join(f'<button type="button" data-help-quick="{q}">{q}</button>' for q in QUICK)
aide_body = f"""    <section class="hc-hero">
      <div class="wrap">
        <div class="hc-hero__in">
          <p class="kicker">Centre d’aide</p>
          <h1 class="pg-h1">Comment pouvons-nous <em>vous aider</em> ?</h1>
          <p class="lead">Des réponses rapides pour vendre et acheter sur mepaye.</p>
          <label class="hc-search"><svg aria-hidden="true"><use href="#i-search"/></svg><span class="sr-only">Rechercher dans l’aide</span><input type="search" placeholder="Rechercher un article : retrait, commission, ebook…" data-help-q autocomplete="off"></label>
          <div class="hc-quick" role="group" aria-label="Recherches fréquentes"><span>Recherches fréquentes</span>{quick}</div>
        </div>
      </div>
    </section>

    <section class="pg-sec pg-sec--tight hc-entry">
      <div class="wrap">
        <div class="hc-topics">
{topics}
        </div>
      </div>
    </section>

    <section class="pg-sec hc-popular">
      <div class="wrap">
        <header class="pg-head" data-reveal><p class="kicker">Les plus consultés</p><h2 class="h2">Articles populaires</h2></header>
        <div class="hc-pops">
{popular}
        </div>
      </div>
    </section>

    <section class="pg-sec pg-sec--tight">
      <div class="wrap">
        <header class="pg-head" data-reveal><p class="kicker">Par rubrique</p><h2 class="h2">Tous les articles</h2></header>
        <div class="hc-cats">
{cats}
        </div>
        <p class="help__none" data-help-none hidden>Aucun article ne correspond. Essayez un autre mot, ou écrivez-nous.</p>
      </div>
    </section>

    <section class="pg-sec pg-sec--tight">
      <div class="wrap">
        <div class="hc-support" data-reveal>
          <div class="hc-support__t">
            {icon('mail', 'ic')}
            <h2>Vous ne trouvez pas votre réponse ?</h2>
            <p>Réponse par e-mail sous 24 h ouvrées.</p>
            <a class="btn btn--lg" href="mailto:contact@mepaye.com">Écrire au support {ARROW}</a>
          </div>
          <dl class="hc-support__f">
            <div><dt>Adresse</dt><dd>contact@mepaye.com</dd></div>
            <div><dt>Délai de réponse</dt><dd>Sous 24 h ouvrées</dd></div>
            <div><dt>Litige avec un créateur</dt><dd>Ouvrez un ticket auprès du support, voir les <a href="cgv.html">CGV</a></dd></div>
          </dl>
        </div>
      </div>
    </section>
"""

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/hc_page.py').read())

# ------------------------------------------------------------------ Blog
POSTS = [
    ('guides', 'Guide', 'Comment créer un ebook qui se vend en Afrique francophone : guide 2026', 'Le guide complet pour transformer votre expertise en ebook rentable, de l’idée à la mise en vente sur le marché francophone africain.', 'creer-ebook-vendre-afrique-francophone', 'cover--blue', '<span class="cover__o cv-book"><span class="bk3"><span class="bk3__c"><i class="bk3__arch"></i><b></b><b></b><small></small></span><span class="bk3__p"></span></span></span>'),
    ('paiements', 'Paiements', 'Mobile Money pour créateurs : guide complet Wave, Orange Money et MTN MoMo', 'Tout ce qu’il faut savoir pour encaisser ses ventes via Mobile Money en 2026 : comment ça marche, quels frais, quel opérateur choisir selon votre pays.', 'mobile-money-creators-wave-orange-mtn', 'cover--navy', '<span class="cover__o cv-phone"><span class="ph3"><i class="ph3__isl"></i><span class="ph3__amt"><b></b><small></small></span><span class="ph3__row is-on"><img src="assets/logos/pm/wave.webp" alt=""><i></i><u></u></span><span class="ph3__row"><img src="assets/logos/pm/orange-money.webp" alt=""><i></i><u></u></span><span class="ph3__row"><img src="assets/logos/pm/mtn-momo.webp" alt=""><i></i><u></u></span><span class="ph3__btn"></span></span></span>'),
    ('guides', 'Guide', 'Lancer son premier produit digital en 7 jours : roadmap pour créateurs', 'Une roadmap concrète, jour par jour, pour passer de l’idée à la première vente d’un produit digital en une semaine.', 'lancer-premier-produit-digital-7-jours', '', '<span class="cover__o cv-week"><span class="wk3"><span class="wk3__h"><b></b><i></i></span><span class="wk3__d"><i></i><i></i><i></i><i></i><i></i><i></i><i class="is-go"></i></span><span class="wk3__bar"><i></i></span></span></span>'),
    ('formations', 'Formations', 'Vendre ses formations en ligne en Afrique : tarifs, plateforme et paiement', 'Comment structurer, tarifer et vendre une formation en ligne sur le marché africain francophone, sans complexité technique.', 'vendre-formation-en-ligne-afrique', 'cover--navy', '<span class="cover__o cv-video"><span class="vd3"><span class="vd3__scr"><i class="vd3__play"></i><span class="vd3__bar"><i></i></span></span><span class="vd3__meta"><b></b><i></i></span></span></span>'),
    ('affiliation', 'Affiliation', 'Affiliation et programmes partenaires : multiplier ses revenus de créateur', 'Comment ouvrir un programme d’affiliation et transformer vos meilleurs clients en partenaires qui vendent à votre place.', 'affiliation-multiplier-revenus-createur', 'cover--green', '<span class="cover__o cv-link"><span class="lk3__t">+25 %</span><span class="lk3"><span class="lk3__ic"></span><i></i><b></b></span><span class="lk3__cur"></span></span>'),
]
posts = '\n'.join(f'''          <article class="post{' post--feat' if i == 0 else ''}" data-cat="{cat}" data-reveal>
            <a class="post__a" href="https://mepaye.com/blog/{slug}">
              <span class="cover {cv}" aria-hidden="true">{art}</span>
              <span class="post__body">
                <span class="post__meta"><span class="tag">{tag}</span><time datetime="2026-05-08">8 mai 2026</time></span>
                <h2>{t}</h2>
                <p>{p}</p>
                <span class="post__more">Lire l’article</span>
              </span>
            </a>
          </article>''' for i, (cat, tag, t, p, slug, cv, art) in enumerate(POSTS))
blog_body = hero('Blog', 'Guides et stratégies pour <em>vendre votre savoir</em>.',
    'Des guides concrets pour vendre votre savoir en Afrique francophone.',
    '''        <div class="filters" role="group" aria-label="Filtrer par thème">
          <button type="button" aria-pressed="true" data-filter="all">Tout</button>
          <button type="button" aria-pressed="false" data-filter="guides">Guides</button>
          <button type="button" aria-pressed="false" data-filter="paiements">Paiements</button>
          <button type="button" aria-pressed="false" data-filter="formations">Formations</button>
          <button type="button" aria-pressed="false" data-filter="affiliation">Affiliation</button>
        </div>''', plain=True) + f'''
    <section class="pg-sec pg-sec--tight">
      <div class="wrap">
        <div class="posts">
{posts}
        </div>
      </div>
    </section>
''' + band('Prêt à vendre votre savoir ?', 'Créez votre boutique gratuitement et publiez votre premier produit aujourd’hui.')

exec(open(str(pathlib.Path(__file__).resolve().parent) + '/blog_page.py').read())

# ------------------------------------------------------------------ Pages légales (texte d'origine, inchangé)
LEGAL_NAV = [('cgu.html', 'CGU'), ('cgv.html', 'CGV'), ('confidentialite.html', 'Confidentialité'), ('mentions-legales.html', 'Mentions légales')]
def legal(slug, h1, updated, intro, sections):
    nav = ''.join(f'<a href="{h}"' + (' aria-current="page"' if h == slug else '') + f'>{t}</a>' for h, t in LEGAL_NAV)
    toc = '\n'.join(f'            <li><a href="#s{i+1}">{t}</a></li>' for i, (t, _) in enumerate(sections))
    secs = '\n'.join(f'''          <section id="s{i+1}">
            <h2>{'<span>' + str(i+1).zfill(2) + '</span>' if len(sections) > 3 else ''}{t}</h2>
{c}
          </section>''' for i, (t, c) in enumerate(sections))
    meta = f'<p class="doc__meta">{"<span><b>Dernière mise à jour :</b> " + updated + "</span>" if updated else ""}<span>{intro}</span></p>' if (updated or intro) else ''
    return hero('Informations légales', h1, '', f'        <nav class="legal-nav" aria-label="Documents légaux">{nav}</nav>', plain=True).replace('        <p class="lead"></p>\n', '') + f'''
    <section class="pg-sec pg-sec--tight">
      <div class="wrap legal">
        <nav class="toc" aria-label="Sommaire" data-toc>
          <p>Sommaire</p>
          <ol>
{toc}
          </ol>
        </nav>
        <article class="doc">
          {meta}
{secs}
        </article>
      </div>
    </section>
'''
P = lambda *xs: '\n'.join(f'            <p>{x}</p>' for x in xs)
UL = lambda *xs: '            <ul>\n' + '\n'.join(f'              <li>{x}</li>' for x in xs) + '\n            </ul>'
ADDR = 'OPUXE L.L.C., 1209 Mountain Road Pl NE, Ste R, Albuquerque, NM 87110 (États-Unis)'

cgu = legal('cgu.html', 'Conditions générales d’utilisation', '21 septembre 2026', f'Mepaye est un service édité par {ADDR}.', [
    ('Objet', P('Les présentes CGU régissent l’utilisation de la plateforme Mepaye accessible via mepaye.com et mepaye.shop. En créant un compte, tu acceptes sans réserve ces conditions.')),
    ('Inscription &amp; compte', P('L’inscription est gratuite. Tu dois fournir des informations exactes et à jour. Tu es responsable de la confidentialité de tes identifiants.')),
    ('Contenu des créateurs', P('Tu conserves la propriété de tes contenus. Tu nous accordes une licence non-exclusive limitée à l’hébergement et à la distribution à tes acheteurs via la plateforme.')),
    ('Commission plateforme', P('Mepaye prélève une commission de 5% sur chaque vente encaissée via la plateforme (taux appliqué depuis le 24 avril 2026 ; les ventes antérieures conservent leur taux de 10% tel qu’appliqué au moment de la transaction). Aucun autre frais caché.')),
    ('Contenus interdits', P('Sont interdits : contenus illégaux, violents, pornographiques, racistes, apologie du terrorisme, contrefaçon, arnaques, produits financiers non réglementés.')),
    ('Suspension &amp; résiliation', P('Mepaye se réserve le droit de suspendre ou supprimer tout compte en violation des présentes CGU, sans préavis ni remboursement des crédits en cas de fraude avérée.')),
    ('Suppression de compte et solde résiduel', P('Tu peux supprimer ton compte à tout moment depuis Réglages → Compte. Un retrait déjà engagé doit d’abord être finalisé, et un solde supérieur ou égal au minimum de retrait doit être retiré avant la suppression. Si ton solde est inférieur au minimum de retrait, il ne peut techniquement pas t’être versé : tu peux alors supprimer ton compte en renonçant expressément à ce reliquat, dont le montant t’est affiché avant confirmation. Ce solde est perdu définitivement et ne pourra plus être réclamé.')),
    ('Limitation de responsabilité', P('Mepaye fournit la plateforme "en l’état". Nous ne garantissons pas qu’elle sera exempte d’erreurs ou d’interruptions. Notre responsabilité est limitée au montant des frais payés les 12 derniers mois.')),
    ('Droit applicable', P('Les présentes CGU sont régies par le droit ivoirien. Tout litige sera soumis aux tribunaux compétents d’Abidjan.')),
])
cgv = legal('cgv.html', 'Conditions générales de vente', '21 avril 2026', f'Les présentes conditions sont celles de {ADDR.replace("OPUXE L.L.C.,", "OPUXE L.L.C., éditeur de Mepaye,")}.', [
    ('Vendeur', P('Les produits vendus sur Mepaye le sont par les créateurs inscrits sur la plateforme. Mepaye intervient en tant qu’intermédiaire technique et de paiement.')),
    ('Produits', P('Les produits sont des biens numériques : ebooks, formations, templates, licences, accès communautés. Les caractéristiques sont celles présentées sur la page produit.')),
    ('Prix', P('Les prix sont affichés dans la devise de la boutique. Ils sont fermes pour la durée de validité du lien de paiement.')),
    ('Paiement', P('Paiements acceptés : Wave, Orange Money, MTN Mobile Money, Moov Money, carte Visa/Mastercard, virement. Le paiement est traité de manière sécurisée par nos prestataires de paiement agréés.')),
    ('Livraison', P('La livraison est immédiate par email (lien de téléchargement signé) ou via l’espace acheteur.')),
    ('Droit de rétractation / remboursement', P('Chaque créateur fixe sa propre politique de remboursement (0, 7, 14 ou 30 jours). En cas de litige non résolu avec le créateur, tu peux ouvrir un ticket auprès du support Mepaye.')),
    ('Service client', P('Contact : <a href="mailto:contact@mepaye.com">contact@mepaye.com</a> : réponse sous 24h ouvrées.')),
])
COOK = '''            <div class="cookies">
              <div><code>next-auth.session-token</code><span>Session d’authentification (httpOnly, durée 30 jours).</span></div>
              <div><code>mepaye_consent</code><span>Ton choix de consentement cookies (180 jours).</span></div>
              <div><code>mp_seen_dashboard</code><span>Onboarding dashboard (cookie technique).</span></div>
              <div><code>mepaye_refp_*</code><span>Attribution affiliation last-click, posé uniquement quand tu cliques sur un lien d’affilié (30 jours).</span></div>
            </div>'''
conf = legal('confidentialite.html', 'Politique de confidentialité', '21 septembre 2026', f'Le responsable du traitement des données est {ADDR}.', [
    ('Données collectées', P('Email, prénom, pays, téléphone (optionnel), numéro Mobile Money pour payout, historique de commandes, logs de connexion. Selon les cas : pièce d’identité et selfie pour la vérification d’identité (section 6), et jeton d’appareil si tu actives les notifications (section 7).')),
    ('Finalités', P('Fournir le service, traiter les paiements, envoyer des communications essentielles (reçus, magic link), améliorer la plateforme, lutter contre la fraude.')),
    ('Partage des données', P('Uniquement avec nos prestataires techniques (voir section 10) sous contrat de confidentialité. Jamais de revente.')),
    ('Tes droits', P('Accès, rectification, suppression, portabilité. Envoie ta demande à <a href="mailto:contact@mepaye.com">contact@mepaye.com</a> : réponse sous 30 jours.')),
    ('Cookies utilisés', COOK + '\n' + P('Tous ces cookies sont strictement nécessaires au service. Les cookies de mesure d’audience et marketing ne sont activés qu’avec ton consentement explicite via la bannière.')),
    ('Vérification d’identité (KYC)', P('Pour lutter contre la fraude et le blanchiment, nous demandons à certains créateurs de vérifier leur identité avant de pouvoir retirer leurs revenus. Tu téléverses alors une pièce d’identité officielle (carte nationale ou passeport, recto et verso selon le document) et un selfie.') + '''
            <h3>Où ils sont stockés, et qui peut les lire</h3>
''' + P('Ces fichiers sont déposés dans un espace privé du serveur, en dehors de toute arborescence publiée : aucune URL directe n’y mène. Ils ne sont accessibles que par une route authentifiée, qui n’autorise que deux profils : toi, pour tes propres documents, et un administrateur Mepaye. Chaque consultation par un administrateur est horodatée et journalisée. Ils ne sont pas chiffrés au repos : la protection repose sur l’isolement du stockage et sur ce contrôle d’accès, pas sur un chiffrement des fichiers eux-mêmes.') + '''
            <h3>Finalité</h3>
''' + P('Vérifier que tu es bien la personne qui reçoit les fonds, et respecter nos obligations de vigilance. Ces documents ne servent à rien d’autre : ni marketing, ni partage avec un tiers en dehors de ce que la loi exige.') + '''
            <h3>Durée de conservation</h3>
''' + P('Tant que ton compte existe, les documents sont conservés. Après la suppression de ton compte, le dossier de vérification (statut, date, nom vérifié) et les fichiers eux-mêmes sont conservés cinq ans, puis supprimés définitivement : c’est le délai des obligations de vigilance en matière de lutte contre la fraude. Passé ce délai, il n’y a plus de raison de les garder.') + '''
            <h3>Tes droits</h3>
''' + P('Tu peux demander à consulter ton dossier à tout moment en écrivant à <a href="mailto:contact@mepaye.com">contact@mepaye.com</a>. La suppression anticipée des documents n’est pas possible tant que le délai ci-dessus court, mais tu peux supprimer ton compte, ce qui déclenche le compte à rebours.')),
    ('Notifications push', P('Si tu actives les notifications dans l’application mobile ou dans ton navigateur, ton appareil nous transmet un jeton d’identification technique. Ce jeton ne contient ni ton nom, ni ton numéro, ni ta position : c’est une adresse de livraison.',
        'Il est transmis à Firebase Cloud Messaging (Google) pour l’application mobile, ou au service de push de ton navigateur (Apple, Google ou Mozilla selon le cas), qui achemine le message jusqu’à ton appareil. Le contenu envoyé se limite au strict nécessaire : « Une vente ! Mepaye te paye », « Retrait exécuté », avec le montant concerné et un lien vers ton tableau de bord.') + '''
            <h3>Durée</h3>
''' + P('Le jeton vit tant que la notification est active. Tu le supprimes en désactivant les notifications dans les réglages de l’application, en la désinstallant, ou en supprimant ton compte, dans ce dernier cas, il est effacé immédiatement, sans attendre le délai de trente jours.')),
    ('Conservation', P('Données de compte : jusqu’à suppression. Documents d’identité : cinq ans après la suppression du compte (voir section 6). Jeton de notification push : effacé à la suppression du compte (voir section 7). Factures : 10 ans (obligation légale). Logs techniques : 12 mois. Logs de monitoring technique : 30 jours.')),
    ('Contact DPO', P('Pour toute question confidentialité : <a href="mailto:contact@mepaye.com">contact@mepaye.com</a>.')),
    ('Nos sous-traitants techniques', P('Pour fournir le service, Mepaye fait appel à des sous-traitants techniques, tenus par contrat à la confidentialité et à la sécurité de tes données. Nous ne transmettons tes données qu’aux catégories de destinataires ci-dessous, et jamais à des fins de revente.') + '''
            <h3>Notre prestataire de monitoring technique</h3>
''' + P('Pour détecter et corriger les erreurs techniques de la plateforme, notre prestataire de monitoring collecte :') + '\n' + UL('les messages d’erreur JavaScript anonymisés ;', 'l’URL de la page où l’erreur s’est produite ;', 'le navigateur et l’OS ;', 'une capture du DOM au moment de l’erreur, avec masquage automatique des champs de saisie (mots de passe, emails, téléphones).') + '\n' + P('Base légale : intérêt légitime (sécurité et stabilité du service). Conservation : 30 jours.') + '''
            <h3>Nos prestataires de paiement agréés</h3>
''' + P('Le traitement des paiements (Mobile Money et carte bancaire) est confié à des prestataires de paiement agréés. Selon le moyen de paiement choisi, ils reçoivent les données strictement nécessaires à l’exécution de la transaction (email, prénom, nom, téléphone, pays et, pour les paiements par carte, les informations de carte traitées selon la norme de sécurité PCI-DSS). Ces données ne servent qu’à exécuter le paiement. Base légale : exécution du contrat.') + '''
            <h3>Notre prestataire d’envoi d’emails</h3>
''' + P('L’envoi des emails transactionnels (reçus d’achat, magic link, notifications) est confié à notre prestataire d’envoi d’emails, qui reçoit uniquement ton email et ton prénom. Base légale : exécution du contrat.') + '''
            <h3>Les régies publicitaires configurées par le créateur</h3>
''' + P('Si la boutique du créateur a configuré ses propres pixels marketing, Mepaye envoie un évènement Purchase côté serveur uniquement si tu as accepté les cookies marketing dans la bannière de consentement. Sinon, aucune donnée n’est transmise à ces régies. Base légale : consentement.')),
    ('Transferts hors Union européenne', P('Certains de nos sous-traitants, ainsi que la société éditrice de Mepaye (établie aux États-Unis), peuvent traiter tes données en dehors de l’Union européenne. Ces transferts sont encadrés par des garanties appropriées, notamment les clauses contractuelles types adoptées par la Commission européenne.')),
])
ment = legal('mentions-legales.html', 'Mentions légales', '', '', [
    ('Éditeur', P('Mepaye est édité par :') + '''
            <address>OPUXE L.L.C.<br>1209 Mountain Road Pl NE, Ste R<br>Albuquerque, NM 87110<br>Société à responsabilité limitée de droit américain (New Mexico)<br>Dossier d’État n° 3132213, constituée le 8 décembre 2025<br>États-Unis</address>
''' + P('Contact : <a href="mailto:contact@mepaye.com">contact@mepaye.com</a>')),
    ('Hébergement', P('Le site est hébergé par un prestataire d’hébergement professionnel.')),
    ('Propriété intellectuelle', P('L’ensemble du site (design, logo, marque Mepaye, code source, textes) est protégé par le droit d’auteur. Toute reproduction non autorisée est interdite.')),
])


# ------------------------------------------------------------------ Gabarits de lecture (tous les articles, en local)
import re as _re, json as _json, unicodedata as _ud
ARTS = _json.load(open(str(pathlib.Path(__file__).resolve().parent) + '/articles.json'))
def localize(html):
    html = _re.sub(r'href="(?:https://mepaye\.com)?/aide/([a-z0-9-]+)"', r'href="aide-\1.html"', html)
    html = _re.sub(r'href="(?:https://mepaye\.com)?/blog/([a-z0-9-]+)"', r'href="article-\1.html"', html)
    for u, f in (('/politique-confidentialite', 'confidentialite.html'), ('/creerebook', 'creer-ebook.html'), ('/developpeur/docs/produits', 'docs-produits.html'), ('/developpeur/docs', 'docs-paiement.html'),
                 ('/cgu', 'cgu.html'), ('/cgv', 'cgv.html'), ('/mentions-legales', 'mentions-legales.html'), ('/fonctionnalites', 'fonctionnalites.html'), ('/tarifs', 'tarifs.html'),
                 ('/affiliation', 'affiliation.html'), ('/a-propos', 'a-propos.html'), ('/contact', 'contact.html'), ('/supprimer-mon-compte', 'supprimer-mon-compte.html'), ('/aide', 'aide.html'), ('/blog', 'blog.html')):
        html = html.replace(f'href="{u}"', f'href="{f}"').replace(f'href="https://mepaye.com{u}"', f'href="{f}"')
    for u, f in (('/auth/inscription', 'inscription.html'), ('/auth/connexion', 'connexion.html')):
        html = html.replace(f'href="{u}"', f'href="{f}"').replace(f'href="https://mepaye.com{u}"', f'href="{f}"')
    return html
def _slug(t):
    t = _ud.normalize('NFD', t).encode('ascii', 'ignore').decode().lower()
    return _re.sub(r'[^a-z0-9]+', '-', t).strip('-')[:48]
def with_ids(html):
    heads = []
    def rep(m):
        t = _re.sub('<[^>]+>', '', m.group(1)); i = _slug(t); heads.append((i, t))
        return f'<h2 id="{i}">{m.group(1)}</h2>'
    return _re.sub(r'<h2>(.*?)</h2>', rep, html), heads
def tables(html):
    return _re.sub(r'(<table>.*?</table>)', r'<div class="tbl">\1</div>', html, flags=_re.S)
def notes(html):
    return _re.sub(r'<blockquote>(.*?)</blockquote>', lambda m: f'<div class="note"><span class="ic" aria-hidden="true"><svg><use href="#i-spark"/></svg></span><p>{_re.sub("</?p>", "", m.group(1))}</p></div>', html, flags=_re.S)
MONTHS = {'01': 'janvier', '02': 'février', '03': 'mars', '04': 'avril', '05': 'mai', '06': 'juin', '07': 'juillet', '08': 'août', '09': 'septembre', '10': 'octobre', '11': 'novembre', '12': 'décembre'}

ART_PAGES = []
# --- blog
POST_BY_SLUG = {x[4]: x for x in POSTS}
for idx_p, (cat, tag, t, p_, sl, cv, art) in enumerate(POSTS):
    a = ARTS[f'blog/{sl}']
    prose, heads = with_ids(tables(notes(a['body'])))
    words = len(_re.sub('<[^>]+>', ' ', a['intro'] + a['body']).split())
    mins = max(1, round(words / 220))
    toc = '\n'.join(f'            <li><a href="#{i}">{h}</a></li>' for i, h in heads)
    others = [x for x in POSTS if x[4] != sl][:3]
    rel = '\n'.join(f"""          <article class="post" data-reveal>
            <a class="post__a" href="article-{o[4]}.html">
              <span class="cover {o[5]}" aria-hidden="true">{o[6]}</span>
              <span class="post__body">
                <span class="post__meta"><span class="tag">{o[1]}</span><time datetime="2026-05-08">8 mai 2026</time></span>
                <h2>{o[2]}</h2>
                <span class="post__more">Lire l’article</span>
              </span>
            </a>
          </article>""" for o in others)
    body = f"""    <header class="art-head">
      <div class="wrap">
        <nav class="crumbs" aria-label="Fil d’Ariane"><a href="blog.html">Blog</a>{CHEV}<span aria-current="page">{tag}</span></nav>
        <h1 class="art-h1">{a['h1']}</h1>
        <p class="art-meta"><span class="tag">{tag}</span><span><time datetime="2026-05-08">Publié le 8 mai 2026</time></span><span>{mins} min de lecture</span></p>
        <p class="art-intro">{a['intro']}</p>
      </div>
    </header>
    <div class="art-cover"><span class="cover {cv}" aria-hidden="true">{art}</span></div>
    <div class="wrap art">
      <article class="prose">
{prose}
      </article>
      <aside class="art-aside">
        <nav class="toc" aria-label="Dans cet article" data-toc>
          <p>Dans cet article</p>
          <ol>
{toc}
          </ol>
        </nav>
        <div class="art-cta">
          <b>Passez de l’idée à la vente.</b>
          <p>Création de compte gratuite, 5 % uniquement sur les ventes encaissées.</p>
          <a class="btn btn--sm" href="https://mepaye.com/auth/inscription">Créer ma boutique {ARROW}</a>
        </div>
      </aside>
    </div>
    <section class="related">
      <div class="wrap">
        <header class="pg-head" data-reveal><p class="kicker">À lire ensuite</p><h2 class="h2">Continuez votre lecture.</h2></header>
        <div class="posts">
{rel}
        </div>
      </div>
    </section>
""" + band('Prêt à vendre votre savoir ?', 'Créez votre boutique gratuitement et publiez votre premier produit aujourd’hui.')
    ART_PAGES.append((f'article-{sl}.html', _re.sub('<[^>]+>', '', a['h1']), _re.sub('<[^>]+>', '', p_), body, 'blog.html'))

# --- aide
for ic, cname, sub, items in HELP:
    for title, sl in items:
        a = ARTS[f'aide/{sl}']
        prose, heads = with_ids(tables(notes(a['body'])))
        toc = '\n'.join(f'            <li><a href="#{i}">{h}</a></li>' for i, h in heads)
        same = [x for x in items if x[1] != sl] or [x for c in HELP for x in c[3] if x[1] != sl][:3]
        more = '\n'.join(f'              <li><a href="aide-{s_}.html">{t_}<svg aria-hidden="true"><use href="#i-chev"/></svg></a></li>' for t_, s_ in same[:4])
        toc_block = f"""        <nav class="toc" aria-label="Sommaire" data-toc>
          <p>Sommaire</p>
          <ol>
{toc}
          </ol>
        </nav>""" if heads else ''
        body = f"""    <header class="art-head">
      <div class="wrap">
        <nav class="crumbs" aria-label="Fil d’Ariane"><a href="aide.html">Centre d’aide</a>{CHEV}<a href="aide.html#{HELP_IDS[[c[1] for c in HELP].index(cname)]}">{cname}</a></nav>
        <h1 class="art-h1">{a['h1']}</h1>
        <p class="art-intro">{a['intro']}</p>
      </div>
    </header>
    <div class="wrap art art--help">
      <aside class="art-aside">
{toc_block}
      </aside>
      <div>
        <article class="prose">
{prose}
        </article>
        <div class="feedback" data-feedback>
          <p>Cet article vous a-t-il aidé ?</p>
          <div class="feedback__b"><button type="button" aria-pressed="false" data-v="oui">Oui</button><button type="button" aria-pressed="false" data-v="non">Non</button></div>
          <p class="feedback__ok" data-feedback-ok role="status" hidden></p>
        </div>
        <section class="more-help">
          <h2 class="h4">Dans la même rubrique</h2>
          <ul class="help__l">
{more}
          </ul>
        </section>
        <div class="contact">
          {icon('mail', 'ic')}
          <div><h2>Besoin d’un coup de main ?</h2><p>Écrivez à contact@mepaye.com, nous répondons sous 24 h ouvrées.</p></div>
          <a class="btn" href="mailto:contact@mepaye.com">Écrire au support {ARROW}</a>
        </div>
      </div>
    </div>
"""
        ART_PAGES.append((f'aide-{sl}.html', _re.sub('<[^>]+>', '', a['h1']), _re.sub('<[^>]+>', '', a['intro'])[:155], body, 'aide.html'))

PAGES = [
    ('fonctionnalites.html', 'Fonctionnalités', '13 modules, une plateforme : créez, vendez, livrez, automatisez et analysez vos produits digitaux sur mepaye.', fx_body, 'fonctionnalites.html'),
    ('tarifs.html', 'Tarifs', 'Sans abonnement ni frais cachés : 5 % par vente et des crédits IA à la demande, payables en Mobile Money.', tarifs_body, 'tarifs.html'),
    ('affiliation.html', 'Affiliation', '25 % à vie sur vos filleuls et jusqu’à 60 % sur les produits d’autres créateurs : le programme d’affiliation double de mepaye.', aff_body, 'affiliation.html'),
    ('aide.html', 'Centre d’aide', 'Tout ce qu’il faut savoir pour vendre sur mepaye et acheter en toute confiance.', aide_body, 'aide.html'),
    ('blog.html', 'Blog', 'Des guides concrets pour vendre votre savoir en Afrique francophone.', blog_body, 'blog.html'),
    ('cgu.html', 'Conditions générales d’utilisation', 'Conditions générales d’utilisation de la plateforme mepaye.', cgu, None),
    ('cgv.html', 'Conditions générales de vente', 'Conditions générales de vente des produits vendus sur mepaye.', cgv, None),
    ('confidentialite.html', 'Politique de confidentialité', 'Comment mepaye collecte, utilise et protège vos données.', conf, None),
    ('mentions-legales.html', 'Mentions légales', 'Mentions légales du site mepaye.', ment, None),
]
PAGES += ART_PAGES + MORE_PAGES
for fname, title, desc, body, cur in PAGES:
    out = localize(page(fname.replace('.html', ''), title, desc, body, cur))
    if fname == '404.html':
        out = re.sub(r'(href|src)="(?!https?:|mailto:|#|/)', r'\1="/', out)
    (SITE / fname).write_text(out)
    print('écrit', fname)

# l'accueil pointe désormais vers ces pages
idx = localize(relink(idx))
(SITE / 'index.html').write_text(idx)
print('accueil relié')
