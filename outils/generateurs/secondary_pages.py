# Exécuté dans build_pages.py après more_pages.py : À propos et Contact sur le standard annexe.
def _fx(ic, t):
    return f'<li><svg aria-hidden="true"><use href="#i-{ic}"/></svg><span>{t}</span></li>'

# ================================================================== À propos
AB_ARCH = '''          <img class="abh__photo" src="assets/img/creatrice.webp" alt="" loading="eager" decoding="async">
          <div class="fxh abh" data-fxh aria-hidden="true">
            <div class="fxh__card is-on" data-fxh-s="0"><p class="fxh__k">Paiement</p><p class="abh__logos"><img src="assets/logos/pm/wave.webp" alt=""><img src="assets/logos/pm/orange-money.webp" alt=""><img src="assets/logos/pm/mtn-momo.webp" alt=""><img src="assets/logos/pm/moov-money.webp" alt=""><img src="assets/logos/pm/airtel-money.webp" alt=""><img src="assets/logos/pm/mixx-tg.webp" alt=""><img src="assets/logos/pm/flooz.webp" alt=""><img src="assets/logos/pm/mixx-sn.webp" alt=""><img src="assets/logos/pm/m-pesa.webp" alt=""><img src="assets/logos/pm/celtiis.webp" alt=""></p><b class="abh__t">Mobile Money intégré</b></div>
            <div class="fxh__card" data-fxh-s="1"><p class="fxh__k">Versement</p><p class="abh__big">2 h</p><b class="abh__t">Au plus, vers votre Mobile Money</b></div>
            <div class="fxh__card" data-fxh-s="2"><p class="fxh__k">Prix</p><p class="abh__big">5 %</p><b class="abh__t">Par vente, zéro abonnement</b></div>
          </div>'''

about_body2 = LOCAL_ICONS + '\n' + ax_hero('users', 'À propos · mepaye',
    'Pensé depuis<br> <em>l’Afrique francophone</em>.',
    'Pour que chaque créateur vende son savoir, sans obstacle.',
    f'<a class="btn btn--lg" href="inscription.html">Rejoindre mepaye {ARROW}</a><a class="link" href="#conviction">Notre conviction {CHEV}</a>',
    AB_ARCH, 'Une créatrice dans l’arche mepaye, et nos trois engagements.') + '\n' + ax_bar([
    ('constat', 'Le constat'), ('conviction', 'Conviction'), ('editeur', 'Éditeur')]) + f'''
    <section class="ax-sec ax-sec--pale" id="constat" aria-labelledby="constat-t" data-ax-chap>
      <div class="wrap">
{ax_head('Le constat', 'Le talent n’est pas le problème.', 'Les outils, si. Ils n’ont pas été pensés pour les créateurs africains.', 'constat-t')}
        <div class="pkg pkg--2 abc" data-reveal>
          <article class="pkg__c abc__old">
            <p class="pkg__tag">Les outils existants</p>
            <p class="pkg__p">Avant<small>des obstacles</small></p>
            <ul class="pkg__f">{_fx('x', 'Pas de Mobile Money')}{_fx('x', 'Versements en 72 h')}{_fx('x', 'Frais cachés')}{_fx('x', 'Support en anglais')}</ul>
          </article>
          <article class="pkg__c pkg__c--pro">
            <p class="pkg__tag">mepaye<em>Notre réponse</em></p>
            <p class="pkg__p">Avec mepaye<small>tout est inclus</small></p>
            <ul class="pkg__f">{_fx('check', 'Wave, Orange, MTN, Moov')}{_fx('check', 'Versement en moins de 2 h')}{_fx('check', '5 %, transparent')}{_fx('check', 'IA Claude intégrée')}</ul>
            <a class="pkg__cta" href="fonctionnalites.html"><span>Voir les fonctionnalités</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          </article>
        </div>
      </div>
    </section>

    <section class="ax-sec" id="conviction" aria-labelledby="conviction-t" data-ax-chap>
      <div class="wrap">
        <figure class="abq" data-reveal>
          <div class="abq__img"><img src="assets/img/usage-cotonou.webp" alt="" loading="lazy" decoding="async"></div>
          <div class="abq__t">
            <p class="ax-head__k" id="conviction-t">Notre conviction</p>
            <blockquote>Un créateur africain ne devrait jamais choisir entre la qualité des outils et l’adaptation locale.</blockquote>
            <p class="abq__a"><span class="abq__m"><img src="assets/brand/symbole.svg" alt=""></span>mepaye offre les deux.</p>
          </div>
        </figure>
        <p class="abs" data-reveal aria-label="Créez. Vendez. mepaye.">Créez. Vendez. <span>mepaye.</span></p>
        <figure class="abs__ph" data-reveal><img src="assets/img/communaute.webp" alt="Deux créateurs rient en comparant leurs téléphones, sous un ciel bleu" width="1536" height="1024" loading="lazy" decoding="async"></figure>
      </div>
    </section>

    <section class="ax-sec ax-sec--soft" id="editeur" aria-labelledby="editeur-t" data-ax-chap>
      <div class="wrap">
        <div class="abe2" data-reveal>
          <div class="abe2__in">
            <div class="abe2__id">
              <span class="abe2__seal" aria-hidden="true"><img src="assets/brand/symbole.svg" alt=""></span>
              <div>
                <p class="abe2__k" id="editeur-t">Éditeur</p>
                <p class="abe2__n">OPUXE L.L.C.</p>
                <p class="abe2__s">La société qui édite mepaye.</p>
              </div>
              <a class="abe2__go" href="mentions-legales.html">Mentions légales<span class="abe2__ar" aria-hidden="true"><svg><use href="#i-arrow"/></svg></span></a>
            </div>
            <dl class="abe2__facts">
              <div><dt>Forme</dt><dd>LLC, Nouveau-Mexique</dd></div>
              <div><dt>Dossier d’État</dt><dd>n° 3132213</dd></div>
              <div><dt>Constituée le</dt><dd>8 décembre 2025</dd></div>
              <div><dt>Siège</dt><dd>1209 Mountain Road Pl NE, Ste R<br>Albuquerque, NM 87110, États-Unis</dd></div>
            </dl>
          </div>
        </div>
      </div>
    </section>
''' + ax_end('Rejoignez mepaye.', 'Votre boutique est prête en quelques minutes.', 'Rejoindre mepaye', 'inscription.html')

# ================================================================== Contact
CT_ARCH = '''          <div class="fxh cth" data-fxh aria-hidden="true">
            <div class="fxh__card is-on" data-fxh-s="0"><p class="fxh__k">Votre message</p><p class="cth__in">Bonjour, comment retirer mes gains ?</p><span class="m-tag"><svg><use href="#i-clock"/></svg>Envoyé à 9:12</span></div>
            <div class="fxh__card" data-fxh-s="1"><p class="fxh__k">Notre réponse</p><p class="cth__in">Bonjour,</p><p class="cth__out"><span class="cth__av"><img src="assets/brand/symbole.svg" alt=""></span>Depuis votre wallet, touchez Retirer : l’argent arrive sur votre Mobile Money.</p><span class="m-tag m-tag--ok">Répondu le jour même</span></div>
            <div class="fxh__card" data-fxh-s="2"><p class="fxh__k">C’est réglé</p><div class="fxh__notif"><img src="assets/logos/orange.svg" alt=""><span><b>Retrait reçu</b><small>+120 000 XOF · Orange Money</small></span></div><span class="m-tag m-tag--ok"><svg><use href="#i-check"/></svg>Résolu</span></div>
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Question</li><li>Réponse</li><li>Résolu</li></ol>'''

_topics = ['Ma boutique', 'Un paiement', 'Un achat', 'Autre']
contact_body2 = LOCAL_ICONS + '\n' + ax_hero('mail', 'Contact · 24 h ouvrées',
    'Parlons de<br> <em>votre projet</em>.',
    'Une question, un souci, une idée : nous lisons chaque message.',
    f'<a class="btn btn--lg" href="#message">Écrire un message {ARROW}</a><a class="link" href="aide.html">Centre d’aide {CHEV}</a>',
    CT_ARCH, 'Exemple : une question, la réponse de l’équipe, le problème réglé.') + '\n' + ax_bar([
    ('message', 'Message'), ('canaux', 'Autres canaux'), ('questions', 'Questions')]) + f'''
    <section class="ax-sec ax-sec--pale" id="message" aria-labelledby="message-t" data-ax-chap>
      <div class="wrap">
{ax_head('Message', 'Écrivez-nous.', 'Votre messagerie s’ouvre avec le message prêt à envoyer.', 'message-t')}
        <div class="ax-plate ctf" data-reveal><div class="ax-plate__core">
          <form class="ct2" data-ct novalidate>
            <fieldset class="ct2__topics">
              <legend>Votre message concerne</legend>
              <div>{''.join(f'<label><input type="radio" name="sujet" value="{t}"{" checked" if i == 0 else ""}><span>{t}</span></label>' for i, t in enumerate(_topics))}</div>
            </fieldset>
            <div class="ct2__row">
              <label class="ct2__f"><span>Nom</span><input name="nom" type="text" autocomplete="name" placeholder="Awa Diop" required></label>
              <label class="ct2__f"><span>E-mail</span><input name="email" type="email" autocomplete="email" placeholder="vous@exemple.com" required></label>
            </div>
            <label class="ct2__f"><span>Message</span><textarea name="message" rows="5" placeholder="Votre question en quelques lignes." required></textarea></label>
            <p class="ct__err" data-ct-err role="alert" hidden></p>
            <div class="ct2__go"><button class="btn btn--lg" type="submit">Préparer l’e-mail {ARROW}</button><span class="ct2__hint"><svg aria-hidden="true"><use href="#i-clock"/></svg>Réponse sous 24 h ouvrées</span></div>
          </form>
        </div></div>
      </div>
    </section>

    <section class="ax-sec" id="canaux" aria-labelledby="canaux-t" data-ax-chap>
      <div class="wrap">
{ax_head('Autres canaux', 'Le bon chemin, tout de suite.', '', 'canaux-t')}
        <div class="pkg ctc" data-reveal>
          <article class="pkg__c pkg__c--pro">
            <p class="pkg__tag">E-mail<em>Le plus rapide</em></p>
            <p class="pkg__p ctc__mail">contact@mepaye.com</p>
            <p class="pkg__d">Pour toute question.</p>
            <button type="button" class="pkg__cta" data-copy-mail="contact@mepaye.com">Copier l’adresse</button>
          </article>
          <article class="pkg__c">
            <p class="pkg__tag">Centre d’aide</p>
            <p class="pkg__p">12<small>articles</small></p>
            <p class="pkg__d">Les réponses aux questions fréquentes.</p>
            <a class="pkg__cta" href="aide.html"><span>Ouvrir l’aide</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          </article>
          <article class="pkg__c">
            <p class="pkg__tag">Créateurs</p>
            <p class="pkg__p">Bientôt<small>chat</small></p>
            <p class="pkg__d">Un chat intégré à votre espace.</p>
            <a class="pkg__cta" href="connexion.html"><span>Mon espace</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          </article>
        </div>
      </div>
    </section>
''' + ax_faq([
    ('Sous quel délai répondez-vous ?', 'En moins de 24 heures ouvrées, par e-mail.'),
    ('Un problème avec un achat ?', 'Contactez d’abord le créateur depuis la page du produit. Sans réponse, écrivez-nous. <a href="aide-demander-remboursement.html">Demander un remboursement</a>.'),
    ('Comment supprimer mon compte ?', 'Depuis Paramètres, Compte. <a href="supprimer-mon-compte.html">Voir la marche à suivre</a>.'),
]) + '\n' + ax_end('Pas encore de compte ?', 'Votre boutique est gratuite, en ligne en quelques minutes.', 'Commencer gratuitement', 'inscription.html')

for _i, _pg in enumerate(MORE_PAGES):
    if _pg[0] == 'a-propos.html':
        MORE_PAGES[_i] = (_pg[0], _pg[1], _pg[2], about_body2, _pg[4])
    if _pg[0] == 'contact.html':
        MORE_PAGES[_i] = (_pg[0], _pg[1], _pg[2], contact_body2, _pg[4])

# ================================================================== Supprimer mon compte
DL_ARCH = '''          <div class="fxh dlh" data-fxh aria-hidden="true">
            <div class="fxh__card is-on" data-fxh-s="0"><p class="fxh__k">Jour 0</p><b class="dlh__t">Demande enregistrée</b><p class="dlh__p">Le compte est marqué pour suppression.</p><span class="dlh__bar"><i style="--p:4%"></i></span></div>
            <div class="fxh__card" data-fxh-s="1"><p class="fxh__k">Jours 1 à 30</p><b class="dlh__t">Vous pouvez annuler</b><p class="dlh__p">Reconnectez-vous, un écran le propose.</p><span class="dlh__bar"><i style="--p:55%"></i></span><span class="m-tag m-tag--ok">Annulation possible</span></div>
            <div class="fxh__card" data-fxh-s="2"><p class="fxh__k">Jour 30</p><b class="dlh__t">Effacement définitif</b><p class="dlh__p">Plus rien n’est récupérable.</p><span class="dlh__bar dlh__bar--end"><i style="--p:100%"></i></span></div>
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Jour 0</li><li>30 jours</li><li>Jour 30</li></ol>'''

del_body2 = LOCAL_ICONS + '\n' + ax_hero('trash', 'Compte · Suppression',
    'Partir,<br> <em>en toute clarté</em>.',
    'Supprimez votre compte à tout moment. Vous avez 30 jours pour changer d’avis.',
    f'<a class="btn btn--lg" href="connexion.html">Depuis mon espace {ARROW}</a><a class="link" href="mailto:support@mepaye.com?subject=Suppression%20de%20compte">Sans accès ? Écrire au support {CHEV}</a>',
    DL_ARCH, 'Les trente jours qui suivent une demande de suppression.') + '\n' + ax_bar([
    ('facons', 'Deux façons'), ('donnees', 'Vos données'), ('questions', 'Questions')]) + f'''
    <section class="ax-sec ax-sec--pale" id="facons" aria-labelledby="facons-t" data-ax-chap>
      <div class="wrap">
{ax_head('Deux façons', 'Avec ou sans accès à votre compte.', 'Dans les deux cas, 30 jours pour annuler.', 'facons-t')}
        <div class="pkg pkg--2" data-reveal>
          <article class="pkg__c pkg__c--pro">
            <p class="pkg__tag">Depuis votre espace<em>Le plus simple</em></p>
            <p class="pkg__p">En 4 gestes<small>immédiat</small></p>
            <ol class="dl2-path"><li>Connectez-vous</li><li>Paramètres</li><li>Compte</li><li>Supprimer mon compte</li></ol>
            <a class="pkg__cta" href="connexion.html"><span>Me connecter</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          </article>
          <article class="pkg__c">
            <p class="pkg__tag">Sans accès</p>
            <p class="pkg__p">Par e-mail<small>support</small></p>
            <p class="pkg__d">Écrivez depuis l’adresse de votre compte, objet « Suppression de compte ». Nous vérifions votre identité.</p>
            <a class="pkg__cta" href="mailto:support@mepaye.com?subject=Suppression%20de%20compte"><span>Écrire au support</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          </article>
        </div>
      </div>
    </section>

    <section class="ax-sec" id="donnees" aria-labelledby="donnees-t" data-ax-chap>
      <div class="wrap">
{ax_head('Vos données', 'Ce qui part, ce qui reste.', 'Vos acheteurs gardent toujours ce qu’ils ont payé.', 'donnees-t')}
        <div class="dl2" data-reveal>
          <article class="dl2__c">
            <p class="pkg__tag">Supprimé</p>
            <ul class="pkg__f">{_fx('x', 'Sessions et appareils connus')}{_fx('x', 'Notifications et brouillons')}{_fx('x', 'Exports et jetons d’accès')}{_fx('x', 'Nom, e-mail, téléphone, photo')}</ul>
          </article>
          <article class="dl2__c dl2__c--keep">
            <p class="pkg__tag">Conservé</p>
            <ul class="pkg__f">{_fx('check', 'Commandes, paiements, versements')}{_fx('check', 'Achats de vos clients, toujours accessibles')}{_fx('check', 'Boutique affichée « Créateur supprimé »')}</ul>
            <p class="dl2__why"><svg aria-hidden="true"><use href="#i-help"/></svg>Ce sont des pièces comptables, sur de l’argent réellement encaissé.</p>
          </article>
        </div>
      </div>
    </section>
''' + ax_faq([
    ('Puis-je annuler la suppression ?', 'Oui, pendant 30 jours. Reconnectez-vous : un écran vous propose d’annuler.'),
    ('Mes clients perdent-ils leurs achats ?', 'Non. Fichiers, formations, communautés et licences restent accessibles à ceux qui les ont payés.'),
    ('Puis-je encore vendre pendant 30 jours ?', 'Non. Aucune nouvelle vente n’est possible une fois la demande enregistrée.'),
]) + '\n' + ax_end('Une question avant de partir ?', 'Le support répond sous 24 h ouvrées.', 'Écrire au support', 'contact.html')

for _i, _pg in enumerate(MORE_PAGES):
    if _pg[0] == 'supprimer-mon-compte.html':
        MORE_PAGES[_i] = (_pg[0], _pg[1], _pg[2], del_body2, _pg[4])
