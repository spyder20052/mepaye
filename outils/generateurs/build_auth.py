"""Écrans de compte mepaye : une carte centrée, sans défilement."""
import sys, pathlib

SITE = pathlib.Path(sys.argv[1])
idx = (SITE / 'index.html').read_text()
sprite = idx[idx.index('  <svg width="0" height="0"'):idx.index('  </svg>')]
sprite += '''      <symbol id="a-mail" viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="13" rx="2.5"/><path d="m4.5 7 7.5 6 7.5-6"/></symbol>
      <symbol id="a-lock" viewBox="0 0 24 24"><rect x="5" y="10.5" width="14" height="9.5" rx="2.5"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"/></symbol>
      <symbol id="a-user" viewBox="0 0 24 24"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 19.5a7 7 0 0 1 14 0"/></symbol>
      <symbol id="a-eye" viewBox="0 0 24 24"><path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/></symbol>
      <symbol id="a-eyeoff" viewBox="0 0 24 24"><path d="M3.5 3.5l17 17M10 6a9.6 9.6 0 0 1 2-.5c6 0 9.5 6.5 9.5 6.5a17 17 0 0 1-2.6 3.4M6.3 7.3C3.9 9 2.5 12 2.5 12S6 18.5 12 18.5a9 9 0 0 0 4.4-1.1"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/></symbol>
      <symbol id="a-in" viewBox="0 0 24 24"><path d="M14 4.5h3.5a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H14"/><path d="M4.5 12h10M11 8.5l3.5 3.5-3.5 3.5"/></symbol>
      <symbol id="a-key" viewBox="0 0 24 24"><circle cx="8" cy="15" r="3.5"/><path d="m10.5 12.5 8-8M16 7l2.5 2.5M14 9l1.8 1.8"/></symbol>
      <symbol id="a-shield" viewBox="0 0 24 24"><path d="M12 3.5 5 6.2v5.3c0 4.3 3 7.6 7 9 4-1.4 7-4.7 7-9V6.2z"/><path d="m9 12 2.2 2.2L15.5 10"/></symbol>
      <symbol id="a-store" viewBox="0 0 24 24"><path d="M4.5 9.5 6 4.5h12l1.5 5"/><path d="M4.5 9.5a2.5 2.5 0 0 0 5 0 2.5 2.5 0 0 0 5 0 2.5 2.5 0 0 0 5 0"/><path d="M5.5 12v7.5h13V12"/></symbol>
      <symbol id="a-brush" viewBox="0 0 24 24"><path d="M19.5 4.5c-4 1.5-8 5.5-9.5 8.5l2 2c3-1.5 7-5.5 8.5-9.5z"/><path d="M10 13c-2 0-3.5 1.5-3.5 3.5 0 1.2-.8 2.5-2 3 3 .5 6.5-.5 7.5-4.5z"/></symbol>
      <symbol id="a-check" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></symbol>
  </svg>'''

I = lambda n: f'<svg aria-hidden="true"><use href="#a-{n}"/></svg>'
EYE = f'<button class="eye" type="button" data-eye aria-controls="{{}}" aria-pressed="false" aria-label="Afficher le mot de passe"><svg class="on" aria-hidden="true"><use href="#a-eye"/></svg><svg class="off" aria-hidden="true"><use href="#a-eyeoff"/></svg></button>'


def field(fid, typ, ph, icon, ac, extra=''):
    eye = EYE.format(fid) if typ == 'password' else ''
    cls = ' class="pw"' if typ == 'password' else ''
    return (f'<div class="fi-a">{I(icon)}<label class="sr-only" for="{fid}">{ph}</label>'
            f'<input id="{fid}" type="{typ}"{cls} autocomplete="{ac}" placeholder="{ph}" required{extra}>{eye}</div>')


def btn(label, loading='', cls='b-a b-a--main'):
    d = f' data-loading="{loading}"' if loading else ''
    return f'<button class="{cls}" type="submit"{d}><span class="btn__t">{label}</span></button>'


def page(title, desc, card):
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <script type="speculationrules">{{"prefetch":[{{"where":{{"href_matches":"/*"}},"eagerness":"moderate"}}]}}</script>
  <title>{title} · mepaye</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#F4F7FD">
  <meta name="robots" content="noindex">
  <link rel="icon" href="assets/brand/favicon-32.png" sizes="32x32">
  <link rel="icon" href="assets/brand/symbole.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400..600&family=Geist+Mono:wght@400..500&family=Parkinsans:wght@500..700&display=swap">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="auth.css">
  <script>document.documentElement.classList.add('js')</script>
</head>
<body>
{sprite}

  <div class="authp">
    <div class="authp__bg" aria-hidden="true">
      <svg class="portal" preserveAspectRatio="none"></svg>
    </div>
    <header class="authp__top">
      <a class="authp__logo" href="index.html" aria-label="mepaye, accueil"><img src="assets/brand/logo.svg" alt="" width="941" height="201"></a>
      <a class="authp__back" href="index.html"><svg aria-hidden="true"><use href="#i-chev"/></svg>Retour au site</a>
    </header>
    <main id="contenu" class="card-a">
{card}
    </main>
    <p class="authp__legal"><a href="cgu.html">CGU</a><a href="confidentialite.html">Confidentialité</a><a href="aide.html">Aide</a></p>
  </div>
  <script src="auth.js" defer></script>
</body>
</html>
'''


# ---------- Connexion
conn = f'''      <span class="card-a__ic" aria-hidden="true">{I('in')}</span>
      <h1>Connexion</h1>
      <p class="card-a__sub">Vos ventes et vos achats, au même endroit.</p>
      <form data-form-login novalidate>
        <div class="fa">
          {field('email', 'email', 'Adresse e-mail', 'mail', 'email')}
          {field('mdp', 'password', 'Mot de passe', 'lock', 'current-password')}
        </div>
        <p class="row-a"><a href="mot-de-passe-oublie.html">Mot de passe oublié ?</a></p>
        <div class="go-a">
          {btn('Se connecter', 'Connexion…')}
          <p class="or-a">ou</p>
          <a class="b-a b-a--ghost" href="connexion-lien.html" data-to-link>{I('mail')}Recevoir un lien par e-mail</a>
        </div>
        <p class="notice" data-login-ok role="status" hidden>{I('check')}Connexion réussie.</p>
      </form>
      <p class="card-a__alt">Pas encore de compte ? <a href="inscription.html">Créer un compte</a></p>
      <div class="wel" data-welcome hidden>
        <span class="wel__mark" aria-hidden="true"><svg viewBox="0 0 64 72"><path class="wel__arch" d="M6 70V32a26 26 0 0 1 52 0v38z"/><path class="wel__tick" pathLength="1" d="m21 42 8 8 15-16"/></svg></span>
        <p class="wel__k">Connexion réussie</p>
        <h2 class="wel__t" tabindex="-1">Bon retour, <span data-wel-name>vous</span>.</h2>
        <p class="wel__s" aria-live="polite"><span data-wel-s>Ouverture de votre espace…</span></p>
      </div>'''

# ---------- Lien par e-mail / mot de passe oublié
def link_card(icon, h, sub, cta, sent, alt):
    return f'''      <section data-view="ask">
        <span class="card-a__ic" aria-hidden="true">{I(icon)}</span>
        <h1>{h}</h1>
        <p class="card-a__sub">{sub}</p>
        <form data-form-link novalidate>
          <div class="fa">{field('email', 'email', 'Adresse e-mail', 'mail', 'email')}</div>
          <div class="go-a">{btn(cta, 'Envoi…')}</div>
        </form>
        <p class="card-a__alt">{alt}</p>
      </section>
      <section data-view="sent" hidden>
        <span class="card-a__ic card-a__ic--ok" aria-hidden="true">{I('mail')}</span>
        <h1>Vérifiez vos e-mails</h1>
        <p class="card-a__sub">{sent} <b data-sent-to>votre adresse</b>.</p>
        <div class="go-a">
          <a class="b-a b-a--main" href="https://mail.google.com/" target="_blank" rel="noopener">Ouvrir Gmail</a>
          <a class="b-a b-a--ghost" href="https://outlook.live.com/" target="_blank" rel="noopener">Ouvrir Outlook</a>
        </div>
        <p class="resend">Rien reçu ? <button type="button" data-resend>Renvoyer</button></p>
        <p class="notice" data-resent role="status" hidden>{I('check')}E-mail renvoyé.</p>
        <p class="card-a__alt"><button type="button" data-change>Changer d’adresse</button></p>
      </section>'''

lien = link_card('mail', 'Connexion par e-mail', 'Recevez un lien pour vous connecter, sans mot de passe.', 'Recevoir le lien',
                 'Lien de connexion envoyé à', '<a href="connexion.html">Utiliser mon mot de passe</a>')
mdp = link_card('key', 'Mot de passe oublié', 'Recevez un lien pour en choisir un nouveau.', 'Envoyer le lien',
                'Lien de réinitialisation envoyé à', '<a href="connexion.html">Retour à la connexion</a>')

# ---------- Inscription, en quatre étapes
THEMES = [('#0866FF', 'Bleu mepaye'), ('#10244A', 'Marine'), ('#0E8A6A', 'Vert'), ('#D9622B', 'Terre cuite'), ('#7C3AED', 'Violet'), ('#E5484D', 'Corail')]
themes = ''.join(f'<label class="theme" style="--c:{c}"><input type="radio" name="theme" value="{c}"{" checked" if i == 0 else ""}><span class="sr-only">{n}</span></label>' for i, (c, n) in enumerate(THEMES))
code = ''.join(f'<input type="text" inputmode="numeric" autocomplete="{"one-time-code" if k == 0 else "off"}" maxlength="1" placeholder="·" aria-label="Chiffre {k + 1} sur 6">' for k in range(6))
MINI = '<div class="mini" data-shop aria-hidden="true"><span class="mini__av" data-shop-av>V</span><span><span class="mini__n" data-shop-name>Votre boutique</span><span class="mini__u"><span data-shop-url>votre-boutique</span>.mepaye.shop</span></span><span class="mini__b">Acheter</span></div>'
BACK = f'<button class="back-a" type="button" data-back aria-label="Étape précédente"><svg aria-hidden="true"><use href="#i-chev"/></svg></button>'
class _Prog:
    """Barre de progression propre à chaque étape : les segments déjà franchis et l'étape en cours sont bleus."""
    def format(self, n):
        segs = ''.join(f'<li class="{"is-on" if k == n else "is-done" if k < n else ""}"></li>' for k in range(1, 5))
        return f'<ol class="prog-a" aria-label="Étape {n} sur 4">{segs}</ol>'
PROG = _Prog()

insc = f'''      <div data-wizard>
        <section data-step>
          {PROG.format(n=1)}
          <h1>Créer un compte</h1>
          <p class="card-a__sub">Gratuit. Vous payez 5 % seulement quand vous vendez.</p>
          <form data-form-account novalidate>
            <div class="fa">
              <div class="fa fa--2"><div class="fa">{field('prenom', 'text', 'Prénom', 'user', 'given-name')}</div><div class="fa"><div class="fi-a"><label class="sr-only" for="nom">Nom</label><input id="nom" class="no-ic" type="text" autocomplete="family-name" placeholder="Nom" required></div></div></div>
              {field('email', 'email', 'Adresse e-mail', 'mail', 'email')}
              {field('mdp', 'password', 'Mot de passe', 'lock', 'new-password', ' data-pw aria-describedby="regles"')}
              <ul class="rules" id="regles" aria-label="Règles du mot de passe"><li data-rule="len">8 caractères</li><li data-rule="up">1 majuscule</li><li data-rule="num">1 chiffre</li></ul>
              {field('mdp2', 'password', 'Confirmer le mot de passe', 'lock', 'new-password')}
              <label class="check"><input id="cgu" type="checkbox" required><span>J’accepte les <a href="cgu.html">CGU</a> et la <a href="confidentialite.html">confidentialité</a>.</span></label>
            </div>
            <div class="go-a">{btn('Continuer', 'Création…')}</div>
          </form>
          <p class="card-a__alt">Déjà un compte ? <a href="connexion.html">Se connecter</a></p>
        </section>

        <section data-step hidden>
          {BACK}
          {PROG.format(n=2)}
          <span class="card-a__ic" aria-hidden="true">{I('shield')}</span>
          <h1>Vérifiez votre e-mail</h1>
          <p class="card-a__sub">Code envoyé à <b data-sent-to>votre adresse</b>.</p>
          <form data-form-code novalidate>
            <fieldset><legend class="sr-only">Code de vérification à 6 chiffres</legend><div class="code">{code}</div></fieldset>
            <p class="f__err" data-code-err role="alert" hidden style="margin-top:.5rem">Saisissez les 6 chiffres.</p>
            <p class="resend">Rien reçu ? <button type="button" data-resend>Renvoyer le code</button></p>
            <p class="notice" data-resent role="status" hidden>{I('check')}Nouveau code envoyé.</p>
            <div class="go-a">{btn('Vérifier', 'Vérification…')}</div>
          </form>
        </section>

        <section data-step hidden>
          {BACK}
          {PROG.format(n=3)}
          <h1>Votre boutique</h1>
          <p class="card-a__sub">Le nom que verront vos clients.</p>
          <form data-form-shop novalidate>
            {MINI}
            <div class="fa">
              {field('boutique', 'text', 'Nom de la boutique', 'store', 'organization')}
              <div class="fi-a"><label class="sr-only" for="adresse">Adresse de la boutique</label><input id="adresse" class="no-ic has-suffix" type="text" autocomplete="off" spellcheck="false" placeholder="votre-boutique" aria-describedby="dispo" required><span class="suffix">.mepaye.shop</span></div>
              <p class="hint-a" id="dispo" data-avail aria-live="polite">Lettres minuscules, chiffres et tirets.</p>
            </div>
            <div class="go-a">{btn('Continuer', 'Réservation…')}</div>
          </form>
        </section>

        <section data-step hidden>
          {BACK}
          {PROG.format(n=4)}
          <h1>Votre couleur</h1>
          <p class="card-a__sub">Modifiable à tout moment.</p>
          <form data-form-style novalidate>
            {MINI.replace(' data-shop ', ' data-shop-style ')}
            <fieldset><legend class="sr-only">Couleur principale</legend><div class="themes">{themes}</div></fieldset>
            <label class="toggle">Mode sombre<input id="sombre" type="checkbox" role="switch"></label>
            <div class="go-a">{btn('Créer ma boutique', 'Création…')}</div>
          </form>
        </section>

        <section data-step hidden>
          <span class="card-a__ic card-a__ic--ok" aria-hidden="true">{I('check')}</span>
          <h1>Votre boutique est prête</h1>
          <p class="card-a__sub">Ajoutez un produit, partagez votre lien, encaissez.</p>
          <p class="done__url"><span data-shop-url>votre-boutique</span>.mepaye.shop</p>
          <div class="go-a"><a class="b-a b-a--main" href="boutique.html">Voir ma boutique</a><a class="b-a b-a--ghost" href="aide-vendre-premier-produit-7-jours.html">Guide : première vente en 7 jours</a></div>
        </section>
      </div>'''

PAGES = [
    ('inscription.html', 'Créer un compte', 'Créez votre compte mepaye gratuitement et ouvrez votre boutique en quelques minutes.', insc),
    ('connexion.html', 'Connexion', 'Connectez-vous à votre compte mepaye.', conn),
    ('connexion-lien.html', 'Connexion par e-mail', 'Connectez-vous à mepaye sans mot de passe, grâce à un lien envoyé par e-mail.', lien),
    ('mot-de-passe-oublie.html', 'Mot de passe oublié', 'Recevez un lien pour choisir un nouveau mot de passe mepaye.', mdp),
]
for f, t, d, c in PAGES:
    (SITE / f).write_text(page(t, d, c))
    print('écrit', f)
