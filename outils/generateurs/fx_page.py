# Exécuté dans build_pages.py. Standard des pages annexes (ax-*) + page Fonctionnalités.
# Anatomie commune : ouverture en arche (texte à gauche, objet vivant dans l'arche),
# barre de chapitres collante, chapitres alternés, questions, appel final.

FX_ICONS = '''  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></symbol>
  </svg>'''

def ax_hero(kicker_ic, kicker, h1, lead, ctas, arch_inner, arch_label):
    return f'''    <section class="ax-hero">
      <div class="wrap ax-hero__in">
        <div class="ax-hero__t">
          <p class="ax-kick"><span class="ax-kick__ic" aria-hidden="true"><svg><use href="#i-{kicker_ic}"/></svg></span>{kicker}</p>
          <h1 class="ax-h1">{h1}</h1>
          <p class="ax-lead">{lead}</p>
          <div class="ax-ctas">{ctas}</div>
        </div>
        <figure class="ax-arch" aria-label="{arch_label}">
{arch_inner}
        </figure>
      </div>
    </section>'''

def ax_bar(items):
    links = ''.join(f'<a href="#{i}" data-ax-link>{t}</a>' for i, t in items)
    return f'''    <nav class="ax-bar" aria-label="Sur cette page" data-ax-bar>
      <div class="ax-bar__in"><span class="ax-bar__ind" aria-hidden="true" data-ax-ind></span>{links}</div>
    </nav>'''

def ax_head(kicker, h2, lead, hid, extra=''):
    return f'''        <header class="ax-head" data-reveal>
          <div><p class="ax-head__k">{kicker}</p><h2 class="ax-h2" id="{hid}">{h2}</h2></div>
          <p class="ax-head__p">{lead}{extra}</p>
        </header>'''

def ax_faq(qs, hid='questions'):
    items = '\n'.join(f'          <details class="ax-q"><summary>{q}</summary><div class="ax-q__a"><p>{a}</p></div></details>' for q, a in qs)
    return f'''    <section class="ax-sec" id="{hid}" aria-labelledby="{hid}-t" data-ax-chap>
      <div class="wrap ax-faq">
        <header class="ax-faq__h" data-reveal><p class="ax-head__k">Questions</p><h2 class="ax-h2" id="{hid}-t">Ce qu’on nous demande.</h2><p class="ax-head__p">Une autre question ? <a href="contact.html">Écrivez-nous</a>.</p></header>
        <div class="ax-faq__l" data-reveal>
{items}
        </div>
      </div>
    </section>'''

def ax_end(t, p, cta, href):
    return f'''    <section class="ax-end-wrap">
      <div class="wrap">
        <div class="ax-end" data-reveal>
          <span class="ax-end__arch" aria-hidden="true"><img src="assets/brand/symbole.svg" alt=""></span>
          <div><h2>{t}</h2><p>{p}</p></div>
          <a class="btn btn--lg ax-end__btn" href="{href}">{cta} {ARROW}</a>
        </div>
      </div>
    </section>'''

# ------------------------------------------------------------------ aperçus des modules (illustrations à plat)
L = lambda *xs: ''.join(f'<i style="--w:{x}%"></i>' for x in xs)
PV = {
 'ia': f'''<div class="m-card m-ia"><p class="m-ia__q"><svg><use href="#i-spark"/></svg>Un ebook sur la cuisine légère</p><div class="m-ia__doc"><b>Chapitre 1 · Pourquoi manger léger</b><span class="m-lines m-type">{L(96, 88, 92, 60)}</span><b>Chapitre 2 · Le placard idéal</b><span class="m-lines m-type m-type--2">{L(90, 70)}</span></div><span class="m-tag m-tag--ok"><span class="m-dot"></span>Rédaction en direct</span></div>''',
 'page': f'''<div class="m-card m-page"><span class="m-page__bar"><i></i><i></i><i></i></span><span class="m-page__hero"><b></b><span class="m-lines">{L(70, 50)}</span><u>Acheter</u></span><span class="m-page__blk"></span><span class="m-page__drag"><span class="m-lines">{L(80, 60)}</span><svg class="m-cursor" viewBox="0 0 24 24"><path d="M5 3l14 8-6 1.5L10 19z"/></svg></span></div>''',
 'cours': '''<div class="m-card m-cours"><p class="m-h">Formation · Vendre en ligne</p><ol><li class="is-done"><span></span>Module 1 · Trouver son idée</li><li class="is-done"><span></span>Module 2 · Créer l’offre</li><li class="is-on"><span></span>Quiz · 8 questions</li><li><span></span>Certificat</li></ol><span class="m-prog"><i style="--w:62%"></i></span></div>''',
 'boutique': '''<div class="m-card m-shop"><p class="m-url"><svg><use href="#i-lock"/></svg>votrenom.mepaye.shop</p><div class="m-shop__id"><span>A</span><b>Atelier Démo</b></div><div class="m-shop__g"><i></i><i></i><i></i></div><p class="m-shop__th"><span style="--c:#0866FF" class="is-on"></span><span style="--c:#10244A"></span><span style="--c:#0E8A6A"></span><span style="--c:#D9622B"></span><small>15+ thèmes</small></p></div>''',
 'paiement': '''<div class="m-card m-pay"><p class="m-h">Payer 14 900 XOF</p><ul><li class="is-on"><img src="assets/logos/wave.webp" alt="">Wave</li><li><img src="assets/logos/orange.svg" alt="">Orange Money</li><li><img src="assets/logos/mtn-momo.webp" alt="">MTN MoMo</li><li><span class="m-pay__card"><img src="assets/logos/visa.svg" alt=""></span>Carte</li><li><span class="m-pay__pp">P</span>PayPal</li></ul><span class="m-tag m-tag--ok">Payé en moins de 30 s</span></div>''',
 'affiliation': '''<div class="m-card m-aff"><p class="m-url"><svg><use href="#i-link"/></svg>mepaye.shop/r/aicha</p><p class="m-h">Une vente de 10 000 XOF</p><div class="m-aff__split"><span style="--w:75%"><b>Vous</b>7 500</span><span style="--w:25%"><b>Affilié</b>2 500</span></div><p class="m-aff__n"><span class="m-tag">25 % à vie</span><span class="m-tag">Cookie 30 jours</span></p></div>''',
 'communaute': '''<div class="m-card m-com"><div class="m-com__h"><span class="m-com__ic"><img src="assets/brand/symbole.svg" alt=""></span><span><b>Club des acheteurs</b><small>128 membres</small></span></div><p class="m-com__msg"><span>A</span>Nouveau module en ligne ce soir.</p><p class="m-com__msg m-com__msg--r">Merci, j’ai hâte !</p><span class="m-tag"><svg><use href="#i-lock"/></svg>Réservé aux acheteurs</span></div>''',
 'retraits': '''<div class="m-card m-wd"><p class="m-wd__k">Solde disponible</p><p class="m-wd__v">186 500 <small>XOF</small></p><ol class="m-steps"><li class="is-done"><b>Retrait demandé</b><small>10:02</small></li><li class="is-done"><b>Envoyé vers Orange Money</b><small>10:41</small></li><li class="is-on"><b>Reçu</b><small>11:14</small></li></ol></div>''',
 'securite': '''<div class="m-card m-sec"><span class="m-sec__shield"><svg><use href="#i-shield"/></svg></span><ul><li><svg><use href="#i-check"/></svg>Identité vérifiée (KYC)</li><li><svg><use href="#i-check"/></svg>Double authentification</li><li><svg><use href="#i-check"/></svg>Liens de téléchargement signés</li><li><svg><use href="#i-check"/></svg>Données conformes RGPD</li></ul></div>''',
 'acheteur': f'''<div class="m-card m-buy"><p class="m-h">Mes achats</p><ul><li><span class="m-th m-th--b"><svg><use href="#i-book"/></svg></span><span><b>Guide : lancer sa boutique</b><small>Ebook · Accès à vie</small></span></li><li><span class="m-th"><svg><use href="#i-play"/></svg></span><span><b>Formation : vendre en ligne</b><small>62 % terminé</small></span></li><li><span class="m-th m-th--c"><svg><use href="#i-doc"/></svg></span><span><b>Modèle de facture</b><small>Télécharger</small></span></li></ul></div>''',
 'emails': '''<div class="m-card m-auto"><div class="m-auto__h"><span class="m-auto__ic"><svg><use href="#i-mail"/></svg></span><b>Relance panier abandonné</b><span class="m-auto__st"><span class="m-dot"></span>Active</span></div><ol class="m-auto__rail"><span class="m-auto__fill" aria-hidden="true"></span><li class="m-auto__s m-auto__s--1"><span class="m-auto__n"><svg><use href="#i-cart"/></svg></span><span><small>Déclencheur</small><b>Panier abandonné</b></span></li><li class="m-auto__w"><svg><use href="#i-clock"/></svg>1 heure plus tard</li><li class="m-auto__s m-auto__s--2"><span class="m-auto__n"><svg><use href="#i-mail"/></svg></span><span><small>E-mail envoyé</small><span class="m-auto__mail"><b>Votre panier vous attend</b><span>Bonjour Awa, votre guide est toujours là.</span></span></span></li><li class="m-auto__w"><svg><use href="#i-clock"/></svg>1 jour plus tard</li><li class="m-auto__s m-auto__s--3"><span class="m-auto__n"><svg><use href="#i-gift"/></svg></span><span><small>Code promo</small><span class="m-auto__code"><code>MERCI10</code><span class="m-tag m-tag--ok">-10 %</span></span></span></li></ol></div>''',
 'analytics': '''<div class="m-card m-an"><p class="m-wd__k">Revenus · 7 derniers jours</p><p class="m-wd__v">312 500 <small>XOF</small></p><span class="m-an__bars"><i style="--h:38%"></i><i style="--h:52%"></i><i style="--h:45%"></i><i style="--h:70%"></i><i style="--h:58%"></i><i style="--h:84%"></i><i style="--h:96%"></i></span><p class="m-an__spot"><svg><use href="#i-star"/></svg>Spotlight : <b>Formation courte</b> mène la semaine</p></div>''',
 'pixels': '''<div class="m-card m-px"><p class="m-h">Tracking · 9 pixels</p><ul><li><b>Meta</b><span class="m-tg is-on"></span></li><li><b>TikTok</b><span class="m-tg is-on"></span></li><li><b>Google Analytics 4</b><span class="m-tg is-on"></span></li><li><b>Snapchat</b><span class="m-tg"></span></li></ul><p class="m-px__ev"><span class="m-dot"></span>Achat envoyé à 3 pixels</p></div>''',
}

CHAPS = [
    ('creer', 'Créer', 'De l’idée au produit prêt à vendre.', 'L’IA rédige, vous validez. Pages de vente et formations, sans une ligne de code.', [
        ('ia', 'spark', 'Création IA', 'Ebooks, formations, templates : l’IA rédige, vous validez.', ['Ebook', 'Formation', 'Template']),
        ('page', 'layout', 'Page de vente', 'Glissez, déposez, publiez. Sans code.', ['Glisser-déposer']),
        ('cours', 'play', 'Formations complètes', 'Modules, vidéos, quiz et certificats.', ['Quiz', 'Certificats']),
    ]),
    ('vendre', 'Vendre', 'Une vitrine à votre image.', 'Vos clients paient comme ils en ont l’habitude, et d’autres vendent pour vous.', [
        ('boutique', 'store', 'Boutique personnalisée', 'votrenom.mepaye.shop ou votre propre domaine. Plus de 15 thèmes.', ['Domaine personnalisé', '15+ thèmes']),
        ('paiement', 'wallet', 'Paiement multi-moyens', 'Mobile Money, carte, PayPal. Payé en moins de 30 secondes.', ['Mobile Money', 'Carte', 'PayPal']),
        ('affiliation', 'link', 'Affiliation double', 'Vos clients vendent pour vous. Gains partagés à chaque vente.', ['25 % à vie', 'Cookie 30 jours']),
        ('communaute', 'users', 'Communautés intégrées', 'Un espace privé, réservé à vos acheteurs.', ['Accès réservé']),
    ]),
    ('encaisser', 'Encaisser', 'Votre argent, vite et en sécurité.', 'Retirez vos gains sur Mobile Money, vos clients gardent leurs achats à vie.', [
        ('retraits', 'up', 'Retraits en moins de 2 h', 'Vos gains arrivent sur votre Mobile Money.', ['Moins de 2 h']),
        ('securite', 'shield', 'Confiance et sécurité', 'Identité vérifiée, liens signés, litiges gérés.', ['KYC', '2FA', 'RGPD']),
        ('acheteur', 'book', 'Espace acheteur', 'Vos clients retrouvent leurs achats à vie.', ['Accès à vie']),
    ]),
    ('grandir', 'Grandir', 'Automatiser, mesurer, vendre plus.', 'Les relances partent toutes seules, et vous voyez ce qui marche.', [
        ('emails', 'mail', 'Automatisations e-mail', 'Bienvenue, panier abandonné, relances : envoyés tout seuls.', ['Panier abandonné', 'Upsell']),
        ('analytics', 'trend', 'Analytics et Spotlight', 'Vos revenus et vos ventes, en temps réel.', ['Temps réel', 'UTM']),
        ('pixels', 'target', 'Tracking 9 pixels', 'Meta, TikTok, Google : mesurez vos publicités.', ['Meta', 'TikTok', 'GA4']),
    ]),
]

def fx_chapter(ci, cid, t, h2, lead, mods):
    tabs = '\n'.join(f'''              <button class="fxe__tab" role="tab" type="button" id="t-{m}" aria-controls="p-{cid}" aria-selected="{str(i == 0).lower()}"{'' if i == 0 else ' tabindex="-1"'} data-fxe-tab="{m}">
                <span class="fxe__ic" aria-hidden="true"><svg><use href="#i-{ic}"/></svg></span>
                <span class="fxe__tx"><b>{n}</b><span class="fxe__d">{d}</span><span class="fxe__chips">{''.join(f'<span>{x}</span>' for x in tags)}</span></span>
              </button>''' for i, (m, ic, n, d, tags) in enumerate(mods))
    pvs = '\n'.join(f'                <div class="fxe__pv{" is-on" if i == 0 else ""}" data-fxe-pv="{m}">{PV[m]}</div>' for i, (m, *_rest) in enumerate(mods))
    return f'''    <section class="ax-sec{' ax-sec--soft' if ci % 2 else ''}" id="{cid}" aria-labelledby="{cid}-t" data-ax-chap>
      <div class="wrap">
{ax_head(f'{t} · {len(mods)} modules', h2, lead, cid + '-t')}
        <div class="fxe{' fxe--flip' if ci % 2 else ''}" data-fxe data-reveal>
          <div class="fxe__list" role="tablist" aria-orientation="vertical" aria-label="Modules : {t}">
{tabs}
          </div>
          <div class="fxe__plate" id="p-{cid}" role="tabpanel" aria-labelledby="t-{mods[0][0]}" tabindex="0">
            <div class="fxe__core">
{pvs}
            </div>
          </div>
        </div>
      </div>
    </section>'''

HERO_ARCH = '''          <div class="fxh" data-fxh aria-hidden="true">
            <div class="fxh__card is-on" data-fxh-s="0"><p class="fxh__k">Créer</p><p class="m-ia__q"><svg><use href="#i-spark"/></svg>Un ebook sur la cuisine légère</p><div class="m-ia__doc"><b>Chapitre 1 · Pourquoi manger léger</b><span class="m-lines">''' + L(96, 84, 90, 58) + '''</span></div><span class="m-tag m-tag--ok">Ebook rédigé</span></div>
            <div class="fxh__card" data-fxh-s="1"><p class="fxh__k">Vendre</p><p class="m-url"><svg><use href="#i-lock"/></svg>atelier-demo.mepaye.shop</p><div class="fxh__prod"><span class="fxh__cover"><i></i></span><span><b>Cuisiner léger</b><small>Ebook</small></span></div><span class="fxh__buy">Acheter · 5 000 XOF</span></div>
            <div class="fxh__card" data-fxh-s="2"><p class="fxh__k">Encaisser</p><div class="fxh__notif"><img src="assets/logos/wave.webp" alt=""><span><b>Paiement reçu</b><small>+5 000 XOF · Wave</small></span></div><p class="m-wd__k">Solde disponible</p><p class="m-wd__v">186 500 <small>XOF</small></p></div>
            <div class="fxh__card" data-fxh-s="3"><p class="fxh__k">Grandir</p><p class="m-wd__k">Ventes · 7 jours</p><span class="m-an__bars">''' + ''.join(f'<i style="--h:{h}%"></i>' for h in (34, 48, 42, 66, 58, 80, 96)) + '''</span><span class="m-tag m-tag--ok">Mis à jour en temps réel</span></div>
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Créer</li><li>Vendre</li><li>Encaisser</li><li>Grandir</li></ol>'''

fx_body = FX_ICONS + '\n' + ax_hero('layout', 'Fonctionnalités · 13 modules',
    'Tout pour vendre,<br> <em>au même endroit</em>.',
    'Créez, vendez, encaissez et grandissez, sans jongler entre six outils.',
    f'<a class="btn btn--lg" href="inscription.html">Commencer gratuitement {ARROW}</a><a class="link" href="#creer">Voir les modules {CHEV}</a>',
    HERO_ARCH, 'Le parcours d’un produit sur mepaye : créé, vendu, encaissé, puis suivi.') + '\n' + ax_bar([(c[0], c[1]) for c in CHAPS] + [('questions', 'Questions')]) + '\n' + '\n'.join(fx_chapter(i, *c) for i, c in enumerate(CHAPS)) + '\n' + ax_faq([
    ('Faut-il payer un abonnement ?', 'Non. Les 13 modules sont inclus. mepaye prélève 5 % sur chaque vente, rien d’autre. <a href="tarifs.html">Voir les tarifs</a>.'),
    ('Puis-je utiliser mon propre nom de domaine ?', 'Oui. Votre boutique est en ligne sur votrenom.mepaye.shop, ou sur votre propre domaine.'),
    ('Comment mes clients peuvent-ils payer ?', 'En Mobile Money (Wave, Orange Money, MTN MoMo, Moov Money), par carte Visa ou Mastercard, ou avec PayPal.'),
    ('En combien de temps suis-je payé ?', 'Vos gains sont dans votre wallet dès la vente. Un retrait arrive sur votre Mobile Money en moins de 2 heures.'),
]) + '\n' + ax_end('Prêt à essayer ?', 'Compte créé en 30 secondes. Aucune carte bancaire requise.', 'Commencer gratuitement', 'inscription.html')
