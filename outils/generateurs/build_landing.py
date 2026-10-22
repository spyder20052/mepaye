import re
"""Landing mepaye : la page actuelle de mepaye.com (mêmes sections, mêmes textes, mêmes polices),
rendue plus soignée, statique, avec les vraies captures de l'application."""
import sys, pathlib, re
SITE = pathlib.Path(sys.argv[1]); S = pathlib.Path(sys.argv[2])
sprite = (S / 'sprite.html').read_text()
old = (S / 'landing-v1' / 'index.html').read_text()
fa = old.index('<svg class="final__sign"'); fb = old.index('</svg>', old.index('class="final__shine"')) + 6
final_svg = old[fa:fb]
# le logo garde sa forme plate : plus de volume ni de reflet
final_svg = re.sub(r'\s*<!-- 2\. le logo prend du volume -->.*?</g>\s*<g class="final__shine".*?</g>', '', final_svg, flags=re.S)
final_svg = re.sub(r'<defs>.*?</defs>', '', final_svg, flags=re.S)

EXTRA = '''  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="l-code" viewBox="0 0 24 24"><path d="m8.5 8-4 4 4 4M15.5 8l4 4-4 4M13.5 5.5l-3 13"/></symbol>
    <symbol id="l-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.4 3.5 5.3 3.5 8.5s-1.1 6.1-3.5 8.5c-2.4-2.4-3.5-5.3-3.5-8.5S9.6 5.9 12 3.5z"/></symbol>
    <symbol id="l-phone" viewBox="0 0 24 24"><rect x="7" y="3" width="10" height="18" rx="2.5"/><path d="M11 18h2"/></symbol>
    <symbol id="l-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></symbol>
    <symbol id="l-store" viewBox="0 0 24 24"><path d="M4.5 9.5 6 4.5h12l1.5 5"/><path d="M4.5 9.5a2.5 2.5 0 0 0 5 0 2.5 2.5 0 0 0 5 0 2.5 2.5 0 0 0 5 0"/><path d="M5.5 12v7.5h13V12"/></symbol>
    <symbol id="l-coins" viewBox="0 0 24 24"><ellipse cx="12" cy="7" rx="6.5" ry="2.8"/><path d="M5.5 7v5c0 1.5 2.9 2.8 6.5 2.8s6.5-1.3 6.5-2.8V7M5.5 12v5c0 1.5 2.9 2.8 6.5 2.8s6.5-1.3 6.5-2.8v-5"/></symbol>
    <symbol id="l-list" viewBox="0 0 24 24"><path d="M9 7h10M9 12h10M9 17h10M5 7h.01M5 12h.01M5 17h.01"/></symbol>
    <symbol id="l-doc" viewBox="0 0 24 24"><path d="M7 3.5h7l4 4V20a.5.5 0 0 1-.5.5h-10.5A.5.5 0 0 1 6.5 20V4a.5.5 0 0 1 .5-.5z"/><path d="M14 3.5v4h4M9.5 12h5M9.5 15.5h5"/></symbol>
    <symbol id="l-cap" viewBox="0 0 24 24"><path d="m2.5 9.5 9.5-5 9.5 5-9.5 5z"/><path d="M6.5 11.6v4.2c1.6 1.5 3.4 2.2 5.5 2.2s3.9-.7 5.5-2.2v-4.2"/></symbol>
    <symbol id="l-pen" viewBox="0 0 24 24"><path d="M15.5 4.5 19.5 8.5 9 19H5v-4z"/><path d="m13.5 6.5 4 4"/></symbol>
    <symbol id="l-book" viewBox="0 0 24 24"><path d="M12 6.5c-2-1.5-4.5-2-7.5-2v13c3 0 5.5.5 7.5 2 2-1.5 4.5-2 7.5-2v-13c-3 0-5.5.5-7.5 2z"/><path d="M12 6.5v13"/></symbol>
    <symbol id="l-play" viewBox="0 0 24 24"><rect x="3.5" y="5" width="17" height="14" rx="3"/><path d="m10.5 9.5 4 2.5-4 2.5z"/></symbol>
    <symbol id="l-video" viewBox="0 0 24 24"><rect x="3" y="6.5" width="12" height="11" rx="2.5"/><path d="m15 10.5 5.5-3v9l-5.5-3"/></symbol>
    <symbol id="l-users" viewBox="0 0 24 24"><circle cx="9" cy="8.5" r="3.2"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0M15.5 5.6a3.2 3.2 0 0 1 0 5.8M17.5 14.2a5.5 5.5 0 0 1 3 4.8"/></symbol>
    <symbol id="l-brief" viewBox="0 0 24 24"><rect x="3.5" y="7" width="17" height="12" rx="2.5"/><path d="M9 7V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V7M3.5 12.5h17"/></symbol>
    <symbol id="l-box" viewBox="0 0 24 24"><path d="m12 3.5 8 4v9l-8 4-8-4v-9z"/><path d="m4 7.5 8 4 8-4M12 11.5v9"/></symbol>
    <symbol id="l-key" viewBox="0 0 24 24"><circle cx="8" cy="15" r="3.5"/><path d="m10.5 12.5 8-8M16 7l2.5 2.5M14 9l1.8 1.8"/></symbol>
    <symbol id="l-layout" viewBox="0 0 24 24"><rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="M3.5 9h17M9.5 9v10.5"/></symbol>
    <symbol id="l-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/></symbol>
    <symbol id="l-chart" viewBox="0 0 24 24"><path d="M4 19.5h16M7 16v-4M12 16V8M17 16v-6"/></symbol>
    <symbol id="l-cart" viewBox="0 0 24 24"><path d="M3.5 4.5h2l2 11h10l2-8H7"/><circle cx="9.5" cy="19" r="1.3"/><circle cx="16.5" cy="19" r="1.3"/></symbol>
    <symbol id="l-trend" viewBox="0 0 24 24"><path d="m3.5 16 5.5-5.5 4 4 7-7.5"/><path d="M15 7h5v5"/></symbol>
    <symbol id="l-percent" viewBox="0 0 24 24"><path d="M18.5 5.5 5.5 18.5"/><circle cx="7.5" cy="7.5" r="2.2"/><circle cx="16.5" cy="16.5" r="2.2"/></symbol>
    <symbol id="l-card" viewBox="0 0 24 24"><rect x="3.5" y="6" width="17" height="12" rx="2.5"/><path d="M3.5 10h17M7 14.5h3"/></symbol>
    <symbol id="l-arrow" viewBox="0 0 24 24"><path d="M5 12h13.5M13 6.5l5.5 5.5-5.5 5.5"/></symbol>
    <symbol id="l-menu" viewBox="0 0 24 24"><path d="M4.5 7.5h15M4.5 12h15M4.5 16.5h15"/></symbol>
  </svg>'''

def ic(n): return f'<svg aria-hidden="true"><use href="#l-{n}"/></svg>'
def chip(icon, color, text, pos): return f'<span class="chip chip--{pos}"><span class="chip__ic" style="--c:{color}">{ic(icon)}</span>{text}</span>'
def phone(img, alt, cls='', ext='webp'):
    # iPhone Pro : cadre titane, bord noir fin, Dynamic Island, boutons latéraux, barre d'état standard
    bar = ('<span class="ph__bar" aria-hidden="true"><b>9:41</b><span class="ph__sys">'
           '<svg><use href="#i-sig"/></svg><svg><use href="#i-wifi"/></svg><svg class="ph__bat"><use href="#i-bat"/></svg></span></span>')
    return (f'<figure class="ph {cls}"><span class="ph__glass"><span class="ph__screen">{bar}'
            f'<img src="assets/app/{img}.{ext}" alt="{alt}" width="770" height="1553" loading="lazy" decoding="async">'
            '<i class="ph__island" aria-hidden="true"></i><i class="ph__home" aria-hidden="true"></i></span></span>'
            '<i class="ph__k ph__k--act" aria-hidden="true"></i><i class="ph__k ph__k--up" aria-hidden="true"></i><i class="ph__k ph__k--dn" aria-hidden="true"></i>'
            '<i class="ph__k ph__k--pow" aria-hidden="true"></i><i class="ph__k ph__k--cam" aria-hidden="true"></i></figure>')
def scene(img, alt, mpos='50%', d='scenes', w=3344, h=1882):
    # photo de campagne : l'écran du téléphone est une vraie interface de l'app, incrustée
    return f'<img class="scene" src="assets/{d}/{img}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" style="--mpos:{mpos}">'
def focus(img, w, h, alt, caption, side):
    # l'encart net : un morceau de la vraie interface, lisible, posé à côté de la photo
    return (f'<figure class="focus focus--{side}"><span class="focus__in"><img src="assets/focus/{img}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></span>'
            f'<figcaption>{caption}</figcaption></figure>')
def mock(img, alt, mpos='50%', w=2508, h=1412):
    # mockup photo-réaliste : les écrans sont les vraies interfaces de l'app, incrustées en haute définition
    return f'<img class="scene scene--mock" src="assets/mockups/{img}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" style="--mpos:{mpos}">'
def chiprow(*chips): return '<div class="chiprow">' + ''.join(chips) + '</div>'
def head(eyebrow, title, lead='', tid=''):
    return (f'<header class="sh"><p class="sh__k">{eyebrow}</p><h2 class="sh__t" id="{tid}">{title}</h2>' + (f'<p class="sh__p">{lead}</p>' if lead else '') + '</header>')
def section(sid, eyebrow, title, lead, panel, tone='blue', extra=''):
    return f'''    <section class="sec" id="{sid}" aria-labelledby="{sid}-t">
      <div class="wrap">
        {head(eyebrow, title, lead, sid + '-t')}{extra}
        <div class="panel panel--{tone}">{panel}</div>
      </div>
    </section>
'''

PM = [('wave','Wave'),('orange-money','Orange Money'),('mtn-momo','MTN MoMo'),('moov-money','Moov Money'),('airtel-money','Airtel Money'),('mixx-tg','T-Money'),('flooz','Flooz'),('mixx-sn','Free Money'),('m-pesa','M-Pesa'),('celtiis','Celtiis Cash'),('visa','Visa'),('mastercard','Mastercard')]
KINDS = [('doc','#0866FF','Fichiers','PDF, ZIP, presets, codes.'),('book','#5B4FE0','Ebook','Livre numérique, lecteur intégré.'),('play','#FF6A2C','Formation','Cours vidéo multi-leçons.'),('video','#F5B000','Coaching','Sessions 1:1 ou en groupe.'),('users','#16A36A','Communauté','Groupe privé WhatsApp ou Telegram.'),('brief','#E0457B','Service','Prestation sur-mesure.'),('box','#0EA5B7','Bundle','Packs de plusieurs produits.'),('key','#7C5CE6','Licence',"Clés ou codes d'activation."),('layout','#10244A','Template','Modèles réutilisables.')]
QUOTES = [("Exactement la plateforme que j'attendais. Simple, claire, rapide.",'JK','Jean K.','#0866FF',4.5),("J'ai adoré dès la première utilisation. Tout est pensé pour aller vite.",'SM','Serge M.','#16A36A',5),("Enfin un outil fait pour nous. Je recommande sans hésiter.",'ID','Ibrahim D.','#7C5CE6',4.7),("Très bon. L'interface est belle et tout fonctionne.",'MB','Mamadou B.','#E0457B',4.8),("Bluffé par la qualité. On sent le soin dans chaque détail.",'AT','Alain T.','#F5B000',5),("La meilleure expérience que j'ai testée pour vendre en ligne.",'PN','Patrick N.','#0EA5B7',4.6),("Rapide, propre, efficace. J'adore.",'MS','Moussa S.','#FF6A2C',4.9),("Un vrai plaisir à utiliser. Hâte de lancer ma boutique.",'FO','Fabrice O.','#10244A',4.8)]
AVG = round(sum(q[4] for q in QUOTES) / len(QUOTES), 1)  # note moyenne affichée sous le titre des avis
STARS = ''.join(f'<svg class="star" width="16" height="13" aria-hidden="true"><use href="#i-star"/></svg>' for _ in range(5))
def stars(r):
    # note décimale : la 5ᵉ étoile se remplit à la fraction de la note, « 4,5 » « 4,7 » à côté
    n = f'{r:.1f}'.replace('.', ',').replace(',0', '')
    return (f'<span class="quote__stars"><span class="quote__stars-in"><span class="quote__stars-fill" aria-hidden="true" style="width:{r / 5 * 100:.0f}%">{STARS}</span>{STARS}</span>'
            f'<span class="quote__note">{n}</span></span>')
def avis_marquee(items, mod):
    # une rangée du carrousel : la liste est doublée pour la boucle infinie, l'aria-hidden porte le doublon
    def carte(q, i, n, c, r):
        # carte : la note en tête, la citation (le guillemet est un ornement), l'auteur sous un filet
        return (f'<li class="quote"><svg class="quote__mark" viewBox="0 0 48 40" aria-hidden="true"><path d="M20 4C10.5 6.6 3.5 14 3.5 24.5 3.5 31.4 7.8 36 13.6 36c5 0 8.6-3.6 8.6-8.4 0-4.6-3.3-8-7.8-8.2.9-4.4 4.4-8.3 9.2-10.2L20 4zm24 0c-9.5 2.6-16.5 10-16.5 20.5 0 6.9 4.3 11.5 10.1 11.5 5 0 8.6-3.6 8.6-8.4 0-4.6-3.3-8-7.8-8.2.9-4.4 4.4-8.3 9.2-10.2L44 4z"/></svg>{stars(r)}<blockquote>{q}</blockquote>'
                f'<p class="quote__who"><span class="quote__av" style="--c:{c}">{i}</span>{n}</p></li>')
    html = ''.join(carte(*x) for x in items)
    return (f'<div class="marquee marquee--{mod}"><ul class="quotes quotes--track">{html}</ul>'
            f'<ul class="quotes quotes--track" aria-hidden="true">{html}</ul></div>')
WHY = [('percent','#16A36A','5 % par vente, zéro abonnement','Vous ne payez que quand vous gagnez. Pas de frais fixe, pas de carte bancaire pour commencer.'),('card','#0866FF','Tous les paiements, un seul endroit','Mobile Money (Wave, Orange Money, MTN, Moov) et cartes Visa &amp; Mastercard. Vos clients paient comme ils veulent.'),('store','#7C5CE6','Jusqu’à 5 boutiques','Plusieurs marques, chacune son domaine et son style, depuis un seul compte.'),('pen','#F5B000',"L'IA qui rédige pour vous",'Transformez une idée en ebook ou en formation structurée, en quelques minutes.')]

body = f'''  <a class="skip" href="#contenu">Aller au contenu</a>
  <header class="top">
    <div class="wrap top__in">
      <a class="top__logo" href="/" aria-label="Mepaye, accueil"><img src="assets/brand/logo-bicolore.svg" alt="Mepaye" width="941" height="201"></a>
      <nav class="top__nav" aria-label="Navigation principale">
        <a href="/fonctionnalites">Produits</a>
        <a href="/tarifs">Tarifs</a>
        <a href="/connexion">Connexion</a>
        <a class="btn btn--sm" href="/inscription">Commencer →</a>
      </nav>
      <details class="top__menu">
        <summary aria-label="Ouvrir le menu">{ic('menu')}</summary>
        <div class="top__drop"><a href="/fonctionnalites">Produits</a><a href="/tarifs">Tarifs</a><a href="/connexion">Connexion</a><a class="btn" href="/inscription">Commencer →</a></div>
      </details>
    </div>
  </header>

  <main id="contenu">
    <section class="hero" aria-labelledby="hero-t">
      <div class="wrap hero__in">
        <h1 class="hero__t" id="hero-t">Créez. Vendez. Encaissez.</h1>
        <p class="hero__p">Tout pour créer, vendre et encaisser vos produits digitaux.</p>
        <div class="hero__ctas"><a class="btn" href="/inscription">Commencer</a><a class="btn btn--ghost" href="/connexion">Se connecter</a></div>
        <p class="hero__fine">Sans abonnement. 5 % par vente, c'est tout.</p>
      </div>
      <div class="hero__art" role="img" aria-label="Un acheteur paie depuis son téléphone, la créatrice reçoit aussitôt la notification Une vente ! Mepaye te paye">
        <div class="stage">
          <span class="stage__arch" aria-hidden="true"></span>
          <span class="stage__floor" aria-hidden="true"></span>
          <span class="stage__sh stage__sh--phone" aria-hidden="true"></span><span class="stage__sh stage__sh--buyer" aria-hidden="true"></span><span class="stage__sh stage__sh--shoes" aria-hidden="true"></span><span class="stage__sh stage__sh--seller" aria-hidden="true"></span>
          <img class="stage__phone" src="assets/people/hero-phone.webp" alt="" width="836" height="1883" decoding="async">
          <img class="stage__p stage__p--buyer" src="assets/people/hero-acheteur.webp" alt="" width="1009" height="964" decoding="async">
          <img class="stage__p stage__p--seller" src="assets/people/hero-creatrice.webp" alt="" width="450" height="1256" decoding="async">
          <ul class="notifs" aria-hidden="true"><li class="notif"><span class="notif__app"><img src="assets/brand/symbole.svg" alt="" width="24" height="24"></span><span class="notif__txt"><span class="notif__top"><b>Une vente ! Mepaye te paye 🎉</b><i>maintenant</i></span><span class="notif__msg">Tu viens de vendre pour 3 500 XOF</span></span></li></ul>
        </div>
        <p class="hero__fine hero__fine--m">Sans abonnement. 5 % par vente, c'est tout.</p>
      </div>
    </section>

{section('boutique', 'Votre boutique', 'Votre boutique, à votre image.', 'Un nom, vos couleurs, votre logo. Une vitrine à votre image, sur votre domaine, sans écrire une ligne de code.',
  mock('boutique', 'La boutique Studio Aïcha sur deux iPhone : la liste des produits et une page produit', '54%'), 'mock panel--mock-blue',
  extra=chiprow(chip('code', '#7C5CE6', 'Sans code', 'tr'), chip('globe', '#0866FF', '.mepaye.shop inclus', 'bl')))}
    <section class="sec" id="paiements" aria-labelledby="paiements-t">
      <div class="wrap">
        {head('Moyens de paiement', 'Le paiement, sous toutes ses formes.', '', 'paiements-t')}
        <div class="panel panel--mock panel--mock-blue panel--notif">{mock('notification', 'Une notification iOS de Mepaye : Une vente ! Mepaye te paye. Tu viens de vendre pour 3 500 XOF', '50%')}</div>
        <div class="panel panel--grey panel--logos panel--after"><ul class="logos" aria-label="Moyens de paiement acceptés">{''.join(f'<li><img src="assets/logos/pm/{f}.webp" alt="{n}" width="56" height="56" loading="lazy"></li>' for f, n in PM)}</ul></div>
      </div>
    </section>

    <section class="sec" id="marques" aria-labelledby="marques-t">
      <div class="wrap">
        {head('Pour aller plus loin', 'Une identité.<br>Plusieurs marques.', "Jusqu'à 5 boutiques, chacune avec son domaine, sa devise, son style. Invitez votre équipe. Connectez vos outils via l'API, les webhooks et les automatisations.", 'marques-t')}
        {chiprow(chip('store', '#0866FF', '5 boutiques', 'tr'), chip('globe', '#7C5CE6', 'Domaine custom', 'ml'), chip('coins', '#16A36A', 'Multi-devises', 'br'))}
        <ul class="brands" aria-label="Trois boutiques, un seul compte"><li class="brand brand--aicha"><figure class="brand__arch"><img src="assets/marques/aicha.webp" alt="Une créatrice tient son iPhone : sa boutique Studio Aïcha" width="900" height="1125" loading="lazy" decoding="async"></figure><div class="brand__card"><img src="assets/marques/carte-aicha.webp" alt="" width="560" height="392" loading="lazy" decoding="async"></div><p class="brand__n">Studio Aïcha</p><p class="brand__d">studio-aicha.mepaye.shop</p></li><li class="brand brand--wellness"><figure class="brand__arch"><img src="assets/marques/wellness.webp" alt="Un coach montre son iPhone : sa boutique Wellness Pro" width="900" height="1125" loading="lazy" decoding="async"></figure><div class="brand__card"><img src="assets/marques/carte-wellness.webp" alt="" width="560" height="392" loading="lazy" decoding="async"></div><p class="brand__n">Wellness Pro</p><p class="brand__d">wellness.mepaye.shop</p></li><li class="brand brand--habit"><figure class="brand__arch"><img src="assets/marques/habit.webp" alt="Une formatrice tend son iPhone : sa boutique Digital Habit" width="900" height="1125" loading="lazy" decoding="async"></figure><div class="brand__card"><img src="assets/marques/carte-habit.webp" alt="" width="560" height="392" loading="lazy" decoding="async"></div><p class="brand__n">Digital Habit</p><p class="brand__d">habit.mepaye.shop</p></li></ul>
      </div>
    </section>

{section('revenus', 'Vos revenus', 'Votre argent, sur votre Mobile Money.', 'Retirez vos gains directement sur Wave, Orange Money ou MTN.<br>Pas de banque tierce, pas de paperasse.',
  scene('revenus', 'Une créatrice montre fièrement son solde Mepaye sur son téléphone', '41%') + focus('solde', 640, 692, 'Solde disponible : 2 451 350 XOF, avec le bouton Retirer mes gains', 'Mobile Money · Dès validation · Devise locale', 'r'), 'photo panel--shift',
  extra='<p class="sh__strong">5 % par vente. Zéro abonnement. Zéro frais caché.</p><p class="sh__small">Vous ne payez que quand vous gagnez.</p>')}
{section('creation', 'Création', 'Décrivez votre idée.<br>Mepaye rédige.', 'Notre IA transforme une simple idée en ebook ou en formation structurée : plan, chapitres, leçons. Vous gardez la main, vous publiez quand vous voulez.',
  mock('creation', "Une main tient un iPhone qui affiche la génération d'un ebook par l'IA de Mepaye", '80%'), 'mock panel--mock-blue', extra=chiprow(chip('list', '#F5B000', 'Plan', 'tl'), chip('doc', '#5B4FE0', 'Chapitres', 'tr'), chip('cap', '#0866FF', 'Leçons', 'bl'), chip('pen', '#16A36A', 'Rédaction', 'br')))}
    <section class="sec" id="produits" aria-labelledby="produits-t">
      <div class="wrap">
        {head('Ce que vous vendez', 'Un seul endroit. Tous vos produits.', 'Quoi que vous créiez, Mepaye sait le vendre.', 'produits-t')}
        <ul class="kinds">{''.join(f'<li class="kind"><span class="kind__ic" style="--c:{c}">{ic(i)}</span><h3>{t}</h3><p>{d}</p></li>' for i, c, t, d in KINDS)}</ul>
      </div>
    </section>

{section('api', 'API Paiement', 'Gardez votre site.<br>Mepaye encaisse.', 'Branchez l’API Mepaye sur le site que vous avez déjà. Vos clients paient en Mobile Money ou par carte, l’argent arrive dans votre wallet.',
  scene('paiement', 'Un iPhone posé à plat affiche la page de paiement hébergée de Mepaye : Wave, Orange Money, MTN MoMo, Moov Money ou carte, pour 3 500 XOF', '22%', 'mockups', 4520, 2444) + focus('paiement', 640, 488, 'Moyens de paiement : Wave, Orange Money, MTN MoMo, Moov Money, Visa et Mastercard', 'Mobile Money · Carte · Paiement chiffré', 'r'), 'photo panel--photo-plat',
  extra=chiprow(chip('key', '#7C5CE6', 'Clé API', 'tr'), chip('code', '#0866FF', 'Mode test', 'bl')))}
{section('affiliation', 'Affiliation', 'Vos clients deviennent vos vendeurs.', "Ouvrez votre programme d'affiliation en un clic. Fixez la commission (jusqu'à 60 %). Mepaye suit les ventes et paie vos affiliés automatiquement.",
  scene('affiliation', "Deux amies regardent l'espace affiliation de Mepaye et ses commissions", '45%') + focus('affiliation', 640, 363, 'Niveau Argent, 47 500 XOF de commissions reçues', 'Lien unique · Jusqu’à 60 % · Suivi automatique', 'r'), 'photo panel--shift')}
{section('analytics', 'Analytics', 'Chaque décision, appuyée par vos chiffres.', 'Revenus, conversions, sources de trafic, comportement des acheteurs, ventes par pays. Tout dans un seul tableau de bord, sans outil externe.',
  scene('analytics', 'Un créateur suit la courbe de ses revenus dans le tableau de bord Mepaye', '61%') + focus('revenus', 640, 560, 'Évolution des revenus sur 30 jours, en hausse', 'Revenus · Ventes · Conversion · Trafic', 'l'), 'photo panel--photo-grey')}
    <section class="sec" id="avis" aria-labelledby="avis-t">
      <div class="wrap">
        <header class="sh"><h2 class="sh__t" id="avis-t">Ils l'utilisent. Ils l'adorent.</h2><p class="sh__p">Les premiers créateurs sur Mepaye en parlent mieux que nous.</p></header>
        <p class="avis__avg">{stars(AVG)}<span><b>{f"{AVG:.1f}".replace(".", ",")}</b>/5 de moyenne</span></p>
      </div>
      {avis_marquee(QUOTES, 'UNIQUE')}
    </section>

    <section class="sec" id="essentiel" aria-labelledby="essentiel-t">
      <div class="wrap">
        {head("L'essentiel", 'Pourquoi Mepaye.', "Tout ce qu'il faut pour vendre. Rien qui vous freine.", 'essentiel-t')}
        <ul class="why">{''.join(f'<li class="why__c"><span class="kind__ic" style="--c:{c}">{ic(i)}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, c, t, d in WHY)}</ul>
      </div>
    </section>

    <section class="final" data-final aria-labelledby="final-title">
      <div class="final__mark" aria-hidden="true">
        {final_svg}
      </div>
      <h2 class="final__t" id="final-title">Commencez aujourd'hui.</h2>
      <p class="final__p">Création gratuite. Pas de carte bancaire requise. Cinq minutes pour publier votre première offre.</p>
      <a class="btn btn--lg" href="/inscription">Commencer →</a>
    </section>
  </main>

  <footer class="foot">
    <div class="wrap foot__in">
      <a class="foot__logo" href="/" aria-label="Mepaye, accueil"><img src="assets/brand/logo-bicolore.svg" alt="Mepaye" width="941" height="201"></a>
      <nav class="foot__nav" aria-label="Liens du site"><a href="/tarifs">Tarifs</a><i>·</i><a href="/fonctionnalites">Fonctionnalités</a><i>·</i><a href="/affiliation">Affiliation</a><i>·</i><a href="/aide">Centre d'aide</a><i>·</i><a href="/blog">Blog</a></nav>
      <p class="foot__copy">© 2026 Mepaye, une marque d'OPUXE L.L.C.</p>
    </div>
    <nav class="wrap foot__legal" aria-label="Informations légales"><a href="/cgu">CGU</a><i>·</i><a href="/cgv">CGV</a><i>·</i><a href="/confidentialite">Confidentialité</a><i>·</i><a href="/mentions-legales">Mentions légales</a></nav>
  </footer>
'''

html = f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Mepaye · Créez. Vendez. Encaissez.</title>
  <meta name="description" content="Tout pour créer, vendre et encaisser vos produits digitaux. Sans abonnement. 5 % par vente, c'est tout.">
  <meta name="theme-color" content="#FFFFFF">
  <link rel="icon" href="assets/brand/favicon-32.png" sizes="32x32">
  <link rel="icon" href="assets/brand/symbole.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..500&family=Inter:wght@400..500&display=swap">
  <link rel="stylesheet" href="landing.css">
  <script>document.documentElement.classList.add('js')</script>
</head>
<body>
{sprite}
{EXTRA}
{body}  <script src="landing.js" defer></script>
</body>
</html>
'''
# Urbanist dessine la diagonale du « z » plus épaisse que ses autres traits : on l'allège dans les titres
def _lz(m):
    return m.group(1) + re.sub(r'(>[^<]*)', lambda t: t.group(1).replace('z', '<span class="lz">z</span>'), m.group(2)) + m.group(3)
html = re.sub(r'(<h[12] class="(?:hero__t|sh__t|final__t)"[^>]*)(>.*?)(</h[12]>)', _lz, html, flags=re.S)
(SITE / 'index.html').write_text(html)
print('landing écrite', len(html))
