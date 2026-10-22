# Exécuté dans build_pages.py après la section Centre d'aide d'origine : l'aide sur le standard annexe, épurée.
HC = [
    ('acheteurs', 'cart', 'Acheteurs', 'Acheter, recevoir, se faire rembourser.', False, [
        ('Acheter et recevoir sa commande', 'Acheter un produit sur mepaye et recevoir sa commande', 'acheter-recevoir-produit-mepaye'),
        ('Demander un remboursement', 'Demander un remboursement après un achat', 'demander-remboursement')]),
    ('createurs', 'store', 'Créateurs', 'Lancer et faire grandir votre boutique.', True, [
        ('Créer son compte et sa boutique', 'Créer son compte mepaye et configurer sa première boutique', 'creer-compte-configurer-boutique'),
        ('Choisir son type de produit', 'Quel type de produit créer sur mepaye', 'choisir-type-produit'),
        ('Vendre en 7 jours', 'Vendre son premier produit digital en 7 jours', 'vendre-premier-produit-7-jours'),
        ('Créer un ebook avec l’IA', 'Utiliser l’IA mepaye pour créer un ebook', 'utiliser-ia-creer-ebook'),
        ('Lancer son affiliation', 'Lancer son programme d’affiliation pour multiplier ses ventes', 'lancer-programme-affiliation')]),
    ('paiements', 'wallet', 'Paiements', 'Encaisser, retirer, vérifier votre identité.', False, [
        ('Le paiement Mobile Money', 'Comment fonctionne le paiement Mobile Money sur mepaye', 'comment-fonctionne-mobile-money'),
        ('La commission de 5 %', 'La commission mepaye de 5 % : comment elle est calculée', 'commission-5-pourcent-comment-calculee'),
        ('Retirer ses gains', 'Demander un retrait de gains depuis votre wallet', 'demander-retrait-gains'),
        ('Vérifier son identité', 'Vérification d’identité (KYC) sur mepaye', 'verification-identite-kyc')]),
    ('support', 'help', 'Support', 'Une question hors des cases.', False, [
        ('Contacter le support', 'Contacter le support mepaye', 'contacter-support-mepaye')]),
]

def _hc_col(cid, ic, t, d, pro, items):
    n = len(items)
    links = ''.join(f'<li data-help-item><a href="aide-{s_}.html"><span>{short}</span><span class="sr-only"> : {full}</span><svg aria-hidden="true"><use href="#i-chev"/></svg></a></li>' for short, full, s_ in items)
    return f'''          <article class="pkg__c{' pkg__c--pro' if pro else ''}" id="{cid}" data-help-card>
            <p class="pkg__tag">{t}{'<em>Le plus lu</em>' if pro else ''}</p>
            <p class="pkg__p">{n}<small>article{'s' if n > 1 else ''}</small></p>
            <p class="pkg__d">{d}</p>
            <ul class="hc2__l">{links}</ul>
          </article>'''

HC_POP = [('wallet', 'Retirer ses gains', 'Vers Mobile Money, dès 1 000 XOF.', 'demander-retrait-gains'),
          ('coins', 'La commission de 5 %', 'Comment elle est calculée.', 'commission-5-pourcent-comment-calculee'),
          ('shield', 'Vérifier son identité', 'Obligatoire pour retirer.', 'verification-identite-kyc')]

HC_ARCH = '''          <div class="fxh hch" data-fxh aria-hidden="true">
            <div class="fxh__card is-on" data-fxh-s="0"><p class="hch__q"><svg><use href="#i-search"/></svg>Comment retirer mes gains ?</p><p class="hch__a">Depuis votre wallet, vers votre Mobile Money. Minimum 1 000 XOF.</p><span class="m-tag"><svg><use href="#i-wallet"/></svg>Paiements</span></div>
            <div class="fxh__card" data-fxh-s="1"><p class="hch__q"><svg><use href="#i-search"/></svg>Comment est calculée la commission ?</p><p class="hch__a">5 % du montant payé par le client. Frais de l’opérateur en plus.</p><span class="m-tag"><svg><use href="#i-wallet"/></svg>Paiements</span></div>
            <div class="fxh__card" data-fxh-s="2"><p class="hch__q"><svg><use href="#i-search"/></svg>Faut-il vérifier mon identité ?</p><p class="hch__a">Pour retirer vos gains, oui. Pour vendre, non.</p><span class="m-tag"><svg><use href="#i-shield"/></svg>Paiements</span></div>
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Retrait</li><li>Commission</li><li>Identité</li></ol>'''

_quick = ''.join(f'<button type="button" data-help-quick="{q}">{q}</button>' for q in ['Retrait', 'Commission', 'KYC', 'Remboursement', 'Mobile Money'])
HC_SEARCH = f'''<div class="hc2-s">
            <label class="hc2-s__f"><svg aria-hidden="true"><use href="#i-search"/></svg><span class="sr-only">Rechercher dans l’aide</span><input type="search" placeholder="Retrait, commission, ebook…" data-help-q autocomplete="off"></label>
            <div class="hc2-s__q" role="group" aria-label="Recherches fréquentes">{_quick}</div>
          </div>'''

aide_body = FX_ICONS + '\n' + ax_hero('help', 'Centre d’aide · 12 articles',
    'Une question ?<br> <em>La réponse est ici</em>.',
    'Des réponses courtes, pour vendre et acheter.',
    HC_SEARCH, HC_ARCH, 'Exemples de questions et leurs réponses.') + '\n' + ax_bar([
    ('rubriques', 'Rubriques'), ('populaires', 'Les plus lus'), ('contact', 'Contact')]) + f'''
    <section class="ax-sec ax-sec--pale" id="rubriques" aria-labelledby="rubriques-t" data-ax-chap>
      <div class="wrap">
{ax_head('Rubriques', 'Tous les articles.', 'Quatre rubriques, une réponse par article.', 'rubriques-t')}
        <div class="pkg hc2" data-reveal>
{chr(10).join(_hc_col(*c) for c in HC)}
        </div>
        <p class="hc2__none" data-help-none hidden>Aucun article ne correspond. Essayez un autre mot, ou <a href="contact.html">écrivez-nous</a>.</p>
      </div>
    </section>

    <section class="ax-sec" id="populaires" aria-labelledby="populaires-t" data-ax-chap>
      <div class="wrap">
{ax_head('Les plus lus', 'Ce que l’on cherche le plus.', 'Trois réponses, en une minute.', 'populaires-t')}
        <div class="hc2-pop">
{chr(10).join(f"""          <a class="hc2-pop__c" href="aide-{s_}.html" data-reveal>
            <span class="hc2-pop__ic" aria-hidden="true"><svg><use href="#i-{ic}"/></svg></span>
            <b>{t}</b>
            <span>{d}</span>
            <span class="hc2-pop__go">Lire <svg aria-hidden="true"><use href="#i-arrow"/></svg></span>
          </a>""" for ic, t, d, s_ in HC_POP)}
        </div>
      </div>
    </section>

    <div id="contact" data-ax-chap>
''' + ax_end('Pas de réponse ici ?', 'Le support répond sous 24 h ouvrées.', 'Écrire au support', 'contact.html') + '''
    </div>
'''
