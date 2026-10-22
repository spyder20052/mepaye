# Exécuté dans build_pages.py après la section Affiliation d'origine : la page sur le standard annexe.
_f = lambda n: f'{n:,}'.replace(',', ' ')

AF_ARCH = '''          <div class="fxh" data-fxh aria-hidden="true">
            <div class="fxh__card is-on" data-fxh-s="0"><p class="fxh__k">Le clic</p><p class="m-url"><svg><use href="#i-link"/></svg>mepaye.shop/r/aicha</p><p class="af-h__t">Un visiteur clique sur votre lien.</p><span class="m-tag"><svg><use href="#i-clock"/></svg>Suivi pendant 30 jours</span></div>
            <div class="fxh__card" data-fxh-s="1"><p class="fxh__k">La vente</p><div class="fxh__prod"><span class="fxh__cover fxh__cover--v"><i></i></span><span><b>Formation : vendre en ligne</b><small>25 000 XOF</small></span></div><span class="m-tag m-tag--ok">Vente attribuée à votre lien</span></div>
            <div class="fxh__card" data-fxh-s="2"><p class="fxh__k">La commission</p><div class="fxh__notif"><img src="assets/brand/symbole.svg" alt=""><span><b>+7 125 XOF</b><small>Commission de 30 % créditée</small></span></div><p class="m-wd__k">Solde du wallet</p><p class="m-wd__v">193 625 <small>XOF</small></p></div>
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Clic</li><li>Vente</li><li>Commission</li></ol>'''

def _feat(ic, t):
    return f'<li><svg aria-hidden="true"><use href="#i-{ic}"/></svg><span>{t}</span></li>'

AF_PROGS = f'''        <div class="pkg pkg--2" data-reveal>
          <article class="pkg__c">
            <p class="pkg__tag">Affiliation plateforme</p>
            <p class="pkg__p">25 %<small>à vie</small></p>
            <p class="pkg__d">Sur chaque achat de crédits de vos filleuls.</p>
            <a class="pkg__cta" href="inscription.html"><span>Obtenir mon lien</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
            <ul class="pkg__f">{_feat('link', 'Lien à votre pseudo')}{_feat('clock', 'Cookie 30 jours')}{_feat('doc', 'Kit WhatsApp fourni')}{_feat('wallet', 'Payé en Mobile Money')}</ul>
          </article>
          <article class="pkg__c pkg__c--pro">
            <p class="pkg__tag">Affiliation produits<em>Jusqu’à 60 %</em></p>
            <p class="pkg__p">20 à 60 %<small>par vente</small></p>
            <p class="pkg__d">Commission fixée par chaque créateur.</p>
            <a class="pkg__cta" href="inscription.html"><span>Voir le marketplace</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
            <div class="pkg__use"><p>Formation à 25 000 XOF, à 30 %</p><div><span><svg aria-hidden="true"><use href="#i-coins"/></svg><b>7 125</b> XOF pour vous</span><span><svg aria-hidden="true"><use href="#i-bolt"/></svg><b>Immédiat</b> à la vente</span></div></div>
            <ul class="pkg__f">{_feat('star', 'Classement mensuel')}{_feat('shield', '4 niveaux d’affilié')}</ul>
          </article>
        </div>'''


_MEDAL = {'bronze': ('#B97A3F', '#E2B07E'), 'silver': ('#97A3B8', '#D3DAE6'), 'gold': ('#D7A93C', '#F3D88F'), 'diamond': ('#3FA3DD', '#A6DBF6')}
def _medal(k, big=False):
    c1, c2 = _MEDAL[k]
    glyph = '<path d="M32 22l6 8-6 12-6-12z" fill="#fff"/>' if k == 'diamond' else '<path d="m32 21 3.2 6.6 7.2 1-5.2 5 1.3 7.2L32 37.4l-6.5 3.4 1.3-7.2-5.2-5 7.2-1z" fill="#fff"/>'
    return (f'<svg class="af-medal{" af-medal--big" if big else ""}" viewBox="0 0 64 80" aria-hidden="true">'
            f'<path d="M20 58h10v20l-5-4-5 4zM34 58h10v20l-5-4-5 4z" fill="{c1}"/>'
            f'<path d="M6 60V30a26 26 0 0 1 52 0v30z" fill="{c1}"/>'
            f'<path d="M13 56V31a19 19 0 0 1 38 0v25z" fill="{c2}"/>{glyph}</svg>')

AF_STEPS = [('target', 'Choisissez un produit', 'Dans le marketplace.'),
            ('link', 'Récupérez votre lien', 'Suivi 30 jours.'),
            ('users', 'Partagez-le', 'Kit WhatsApp fourni.'),
            ('wallet', 'Encaissez', 'Dès la vente confirmée.')]

TIERS = [('Bronze', '#C98A4B'), ('Silver', '#AEB9CC'), ('Gold', '#E3BE62'), ('Diamond', '#7FCBF0')]

aff_body = FX_ICONS + '''
  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13 3.5 5.5 13.5H12l-1 7 7.5-10H12z"/></symbol>
  </svg>
''' + ax_hero('link', 'Affiliation · Programme double',
    'Gagnez de l’argent<br> <em>en recommandant</em>.',
    '25 % à vie sur vos filleuls. Jusqu’à 60 % sur les produits d’autres créateurs.',
    f'<a class="btn btn--lg" href="inscription.html">Devenir affilié {ARROW}</a><a class="link" href="#simulateur">Simuler mes gains {CHEV}</a>',
    AF_ARCH, 'Exemple : un clic sur votre lien, une vente, votre commission créditée.') + '\n' + ax_bar([
    ('programmes', 'Deux programmes'), ('simulateur', 'Simulateur'), ('etapes', 'Comment ça marche'), ('niveaux', 'Niveaux'), ('createurs', 'Pour les créateurs'), ('questions', 'Questions')]) + f'''
    <section class="ax-sec ax-sec--pale" id="programmes" aria-labelledby="programmes-t" data-ax-chap>
      <div class="wrap">
{ax_head('Deux programmes · un compte', 'Recommandez la plateforme, ou ses produits.', 'Les deux se cumulent.', 'programmes-t')}
{AF_PROGS}
      </div>
    </section>

    <section class="ax-sec" id="simulateur" aria-labelledby="simulateur-t" data-ax-chap>
      <div class="wrap">
{ax_head('Simulateur', 'Combien pouvez-vous gagner ?', 'Trois curseurs, le calcul est immédiat.', 'simulateur-t')}
        <div class="ax-plate tss" data-afs data-reveal>
          <div class="ax-plate__core tss__core">
            <div class="tss__in">
              <label class="range"><span class="range__top"><span class="field__l">Prix du produit</span><output data-afs-o-price>15 000 XOF</output></span><input type="range" min="1000" max="100000" step="500" value="15000" data-afs-price aria-label="Prix du produit, en XOF"></label>
              <label class="range"><span class="range__top"><span class="field__l">Commission fixée par le créateur</span><output data-afs-o-rate>30 %</output></span><input type="range" min="20" max="60" step="5" value="30" data-afs-rate aria-label="Commission, de 20 à 60 %"></label>
              <label class="range"><span class="range__top"><span class="field__l">Ventes par mois</span><output data-afs-o-n>20</output></span><input type="range" min="1" max="200" step="1" value="20" data-afs-n aria-label="Ventes par mois"></label>
            </div>
            <div class="tss__out" aria-live="polite">
              <dl class="tss__rows">
                <div><dt>Par vente</dt><dd data-afs-one>4 275 XOF</dd></div>
                <div><dt>En crédits IA, avec le bonus de 10 %</dt><dd data-afs-cr>94 050 XOF</dd></div>
              </dl>
              <div class="tss__net"><span>Vous gagnez, chaque mois</span><b data-afs-total>85 500 XOF</b></div>
              <p class="tss__note">Estimation sur le prix après commission mepaye, avant frais de l’opérateur de paiement.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="ax-sec ax-sec--soft" id="etapes" aria-labelledby="etapes-t" data-ax-chap>
      <div class="wrap">
{ax_head('Comment ça marche · 4 étapes', 'Du lien à votre wallet.', 'Le suivi est automatique.', 'etapes-t')}
        <ol class="dv-flow af-flow" data-reveal>
          <span class="dv-flow__run" aria-hidden="true"><span class="dv-flow__tok">+7 125 XOF</span></span>
''' + '\n'.join(f'''          <li class="dv-node" style="--d:{i * 2}s">
            <span class="dv-node__ic" aria-hidden="true"><svg><use href="#i-{ic}"/></svg></span>
            <div><h3><span class="af-n">{i + 1}</span>{t}</h3><p>{p}</p></div>
          </li>''' for i, (ic, t, p) in enumerate(AF_STEPS)) + f'''
        </ol>
      </div>
    </section>

    <section class="ax-sec" id="niveaux" aria-labelledby="niveaux-t" data-ax-chap>
      <div class="wrap">
{ax_head('Niveaux et classement', 'Plus vous vendez, plus vous montez.', 'Quatre niveaux, un classement chaque mois.', 'niveaux-t')}
        <div class="af-lv2" data-reveal>
          <div class="ax-plate af-me"><div class="ax-plate__core">
            <p class="af-me__k">Votre niveau</p>
            <div class="af-me__top">
              {_medal('silver', True)}
              <div><p class="af-me__lv">Silver</p><p class="af-me__sub">Prochain niveau : Gold</p></div>
            </div>
            <div class="af-me__bar" aria-hidden="true"><i style="--p:72%"></i></div>
            <ol class="af-me__tiers">
{''.join(f'<li class="{st}">{_medal(k)}<span>{n}</span></li>' for k, n, st in (('bronze', 'Bronze', 'is-done'), ('silver', 'Silver', 'is-on'), ('gold', 'Gold', ''), ('diamond', 'Diamond', '')))}
            </ol>
          </div></div>
          <div class="ax-plate af-pod"><div class="ax-plate__core">
            <p class="af-board__h"><span>Classement du mois</span><span class="m-tag"><svg aria-hidden="true"><use href="#i-clock"/></svg>Remis à zéro le 1er</span></p>
            <div class="af-pod__s" aria-label="Exemple de podium">
              <div class="af-pod__p af-pod__p--2"><span class="af-av" style="--c:#7FCBF0">M</span><b>Mariam S.</b><span class="af-pod__b"><em>2</em><small>41 ventes</small></span></div>
              <div class="af-pod__p af-pod__p--1"><span class="af-pod__crown" aria-hidden="true"><svg><use href="#i-star"/></svg></span><span class="af-av" style="--c:#E3BE62">K</span><b>Kofi A.</b><span class="af-pod__b"><em>1</em><small>48 ventes</small></span></div>
              <div class="af-pod__p af-pod__p--3"><span class="af-av" style="--c:#0866FF">V</span><b>Vous</b><span class="af-pod__b"><em>3</em><small>37 ventes</small></span></div>
            </div>
            <p class="tss__note">Exemple d’affichage.</p>
          </div></div>
        </div>
      </div>
    </section>

    <section class="ax-sec ax-sec--soft" id="createurs" aria-labelledby="createurs-t" data-ax-chap>
      <div class="wrap">
{ax_head('Pour les créateurs', 'D’autres vendent pour vous.', 'Activez l’affiliation, mepaye gère le reste.', 'createurs-t', ' <a href="aide-lancer-programme-affiliation.html">Lire le guide</a>.')}
        <div class="af-cr" data-reveal>
          <div class="ax-plate"><div class="ax-plate__core af-cr__v">
            <div class="m-card af-set">
              <p class="m-h">Formation : vendre en ligne</p>
              <p class="af-set__row"><span><b>Affiliation</b><small>Visible dans le marketplace</small></span><span class="m-tg is-on"></span></p>
              <div class="af-set__rate"><span>Commission de l’affilié</span><b data-afc-o>30 %</b></div>
              <input type="range" min="10" max="60" step="5" value="30" data-afc aria-label="Commission accordée à l’affilié">
              <p class="af-set__ex"><span>Sur une vente à 25 000 XOF</span><span>Affilié <b data-afc-a>7 125</b> · Vous <b data-afc-y>16 625</b></span></p>
            </div>
          </div></div>
          <div class="af-cr__t">
            <ol class="af-how">
              <li><b>Ouvrez la fiche du produit</b></li>
              <li><b>Activez l’affiliation</b></li>
              <li><b>Fixez la commission</b><span>Le produit rejoint le marketplace.</span></li>
            </ol>
            <div class="tbl af-tbl"><table><thead><tr><th>Produit</th><th>Commission conseillée</th></tr></thead><tbody>
              <tr><td>Formation premium, accompagnement</td><td>25 à 40 %</td></tr>
              <tr><td>Formation courte, ebook complet</td><td>15 à 25 %</td></tr>
              <tr><td>Ebook court, template</td><td>10 à 20 %</td></tr>
            </tbody></table></div>
          </div>
        </div>
      </div>
    </section>
''' + ax_faq([
    ('Combien de temps dure le suivi de mon lien ?', 'Trente jours. Si le visiteur achète dans ce délai, la vente vous est attribuée.'),
    ('Quand suis-je payé ?', 'Votre commission est créditée sur votre wallet dès que la vente est confirmée. Vous la retirez en Mobile Money.'),
    ('Sur quel montant ma commission est-elle calculée ?', 'Sur le montant net de la vente, après la commission mepaye et les frais de l’opérateur de paiement.'),
    ('Puis-je transformer mes gains en crédits IA ?', 'Oui. Payez vos crédits avec vos gains d’affiliation : vous recevez 10 % de crédits en plus.'),
]) + '\n' + ax_end('Devenez affilié.', 'Votre lien est prêt dès la création de votre compte.', 'Devenir affilié', 'inscription.html')
