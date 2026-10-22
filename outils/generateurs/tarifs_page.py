# Exécuté dans build_pages.py après fx_page.py : la page Tarifs sur le standard des pages annexes.
_fmt = lambda n: f'{n:,}'.replace(',', ' ')

def _receipt(i, kind, amount, on=False):
    fee = round(amount * .05)
    return f'''            <div class="fxh__card tsr{' is-on' if on else ''}" data-fxh-s="{i}">
              <p class="fxh__k">Une vente · {kind}</p>
              <dl class="tsr__rows">
                <div><dt>Payé par le client</dt><dd>{_fmt(amount)} XOF</dd></div>
                <div class="tsr__fee"><dt>Commission mepaye · 5 %</dt><dd>− {_fmt(fee)} XOF</dd></div>
                <div><dt>Abonnement</dt><dd>0 XOF</dd></div>
              </dl>
              <p class="tsr__net"><span>Pour vous</span><b>{_fmt(amount - fee)} <small>XOF</small></b></p>
            </div>'''

TS_ARCH = '''          <div class="fxh" data-fxh aria-hidden="true">
''' + _receipt(0, 'Ebook', 5000, True) + '\n' + _receipt(1, 'Formation', 25000) + '\n' + _receipt(2, 'Coaching', 15000) + '''
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Ebook</li><li>Formation</li><li>Coaching</li></ol>'''

ZEROS = [('Abonnement mensuel', '0 XOF'), ('Création de boutique', '0 XOF'), ('Frais fixes', '0 XOF'), ('Carte bancaire pour commencer', 'Non requise')]
TS_PACKS = [('decouverte', 'Découverte', 2500, 100, None, False), ('starter', 'Starter', 6500, 300, '+8 % de crédits offerts', False),
            ('pro', 'Pro', 15000, 800, '+15 % de crédits offerts', True), ('business', 'Business', 33000, 2000, '+25 % de crédits offerts', False),
            ('agence', 'Agence', 75000, 5000, '+33 % de crédits offerts', False)]

def _pack_opt(k, n, price, cr, bonus, pro):
    return f'''              <label class="tsp__opt">
                <input type="radio" name="pack" value="{k}" data-name="{n}" data-price="{price}" data-cr="{cr}" data-bonus="{bonus or ''}"{' checked' if pro else ''}>
                <span class="tsp__in">
                  <span class="tsp__n">{n}{'<em>Le plus choisi</em>' if pro else ''}</span>
                  <span class="tsp__m"><b>{_fmt(cr)}</b> crédits</span>
                  <span class="tsp__p">{_fmt(price)} XOF</span>
                </span>
              </label>'''

_pro = TS_PACKS[2]

_pl = lambda n, w: w + ('s' if n > 1 else '')
TG_DESC = {'decouverte': 'Pour tester l’IA sur un premier produit.', 'starter': 'Pour lancer vos premiers produits.', 'pro': 'Pour créer chaque semaine, sans compter.', 'business': 'Pour un catalogue qui grandit vite.', 'agence': 'Pour produire pour plusieurs marques.'}
def _tg_col(k, n, price, cr, bonus, pro):
    f = lambda ic, t: f'<li><svg aria-hidden="true"><use href="#i-{ic}"/></svg><span>{t}</span></li>'
    feats = [f('spark', f'<b data-tg-cr>{_fmt(cr)}</b> crédits IA'), f('book', f'Jusqu’à <b data-tg-eb>{cr // 50}</b> <span data-tg-ebw>{_pl(cr // 50, "ebook")}</span>'), f('play', f'ou <b data-tg-fo>{cr // 80}</b> <span data-tg-fow>{_pl(cr // 80, "formation")}</span>'),
             f('gift', bonus if bonus else 'Idéal pour tester'), f('check', 'Paiement unique')]
    usage = f'<div class="pkg__use"><p>Ce que vous pouvez créer</p><div><span><svg aria-hidden="true"><use href="#i-book"/></svg><b data-tg-eb>{cr // 50}</b> ebooks</span><span><svg aria-hidden="true"><use href="#i-play"/></svg><b data-tg-fo>{cr // 80}</b> formations</span></div></div>' if pro else ''
    if pro: feats = feats[:1] + feats[3:]
    return f"""          <article class="pkg__c{' pkg__c--pro' if pro else ''}" data-tg-col data-cr="{cr}">
            <p class="pkg__tag">{n}{'<em>Le plus choisi</em>' if pro else ''}</p>
            <p class="pkg__p">{_fmt(price)}<small>XOF</small></p>
            <p class="pkg__d">{TG_DESC[k]}</p>
            <a class="pkg__cta" href="inscription.html"><span>Choisir {n}</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
            {usage}
            <ul class="pkg__f">{''.join(feats)}</ul>
          </article>"""
TG_COLS = '\n'.join(_tg_col(*p) for p in TS_PACKS)
tarifs_body = FX_ICONS + '\n' + ax_hero('coins', 'Tarifs · Sans abonnement',
    'On se paie seulement<br> <em>quand vous vendez</em>.',
    '5 % par vente. Des crédits IA seulement si vous en avez besoin.',
    f'<a class="btn btn--lg" href="inscription.html">Commencer gratuitement {ARROW}</a><a class="link" href="#simulateur">Simuler mes gains {CHEV}</a>',
    TS_ARCH, 'Exemples : sur chaque vente, mepaye garde 5 %, sans abonnement.') + '\n' + ax_bar([
    ('commission', 'Commission'), ('simulateur', 'Simulateur'), ('credits', 'Crédits IA'), ('avantages', 'Avantages'), ('questions', 'Questions')]) + f'''
    <section class="ax-sec" id="commission" aria-labelledby="commission-t" data-ax-chap>
      <div class="wrap">
{ax_head('Commission · un seul tarif', 'Un seul tarif. Rien d’autre.', 'Prélevés à la vente. Rien à payer pour commencer.', 'commission-t')}
        <div class="tsc" data-reveal>
          <div class="tsc__big">
            <p class="tsc__k">Sur chaque vente</p>
            <p class="tsc__v">5<span>%</span></p>
            <p class="tsc__s">Sur le montant payé par le client.</p>
          </div>
          <div class="ax-plate tsc__zero">
            <div class="ax-plate__core">
              <p class="tsc__zk">Ce que vous ne payez pas</p>
              <ul>
{chr(10).join(f'                <li><span>{t}</span><b>{v}</b></li>' for t, v in ZEROS)}
              </ul>
              <p class="tsc__op"><svg aria-hidden="true"><use href="#i-help"/></svg>Frais de l’opérateur en plus, en général 1 à 2 %.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="ax-sec ax-sec--soft" id="simulateur" aria-labelledby="simulateur-t" data-ax-chap>
      <div class="wrap">
{ax_head('Simulateur', 'Combien vous gardez.', 'Deux curseurs, le calcul est immédiat.', 'simulateur-t')}
        <div class="ax-plate tss" data-tss data-reveal>
          <div class="ax-plate__core tss__core">
            <div class="tss__in">
              <label class="range"><span class="range__top"><span class="field__l">Prix de votre produit</span><output data-tss-o-price>14 900 XOF</output></span><input type="range" min="1000" max="100000" step="500" value="14900" data-tss-price aria-label="Prix de votre produit, en XOF"></label>
              <label class="range"><span class="range__top"><span class="field__l">Ventes par mois</span><output data-tss-o-qty>40</output></span><input type="range" min="1" max="300" step="1" value="40" data-tss-qty aria-label="Nombre de ventes par mois"></label>
              <div class="tss__split" aria-hidden="true"><span class="tss__keep" data-tss-bar></span><span class="tss__cut"></span></div>
              <p class="tss__legend" aria-hidden="true"><span><i class="tss__dot"></i>Pour vous · 95 %</span><span><i class="tss__dot tss__dot--n"></i>mepaye · 5 %</span></p>
            </div>
            <div class="tss__out" aria-live="polite">
              <dl class="tss__rows">
                <div><dt>Chiffre d’affaires</dt><dd data-tss-gross>596 000 XOF</dd></div>
                <div><dt>Commission mepaye (5 %)</dt><dd data-tss-fee>− 29 800 XOF</dd></div>
                <div><dt>Abonnement</dt><dd>0 XOF</dd></div>
              </dl>
              <div class="tss__net"><span>Vous recevez, chaque mois</span><b data-tss-net>566 200 XOF</b></div>
              <p class="tss__note">Avant frais de l’opérateur de paiement.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="ax-sec ax-sec--pale" id="credits" aria-labelledby="credits-t" data-ax-chap>
      <div class="wrap">
{ax_head('Crédits IA · à la demande', 'Un pack, autant de produits que vous voulez.', 'Paiement unique. Plus le pack est grand, plus il y a de crédits offerts.', 'credits-t')}
        <div class="tg-top" data-reveal>
          <p class="tsp__scale"><span>1 ebook <b>50 crédits</b></span><span>1 formation <b>80 crédits</b></span><span>1 description <b>5 crédits</b></span></p>
          <label class="tg-sw"><input type="checkbox" role="switch" data-tg-wallet><span class="tg-sw__t" aria-hidden="true"></span><span>Payer avec mon wallet</span><b>+10 %</b></label>
        </div>
        <div class="pkg" data-tg data-reveal>
{TG_COLS}
        </div>
        <p class="tg-note" data-tg-note>Crédits du pack, hors bonus du wallet.</p>
      </div>
    </section>

    <section class="ax-sec" id="avantages" aria-labelledby="avantages-t" data-ax-chap>
      <div class="wrap">
{ax_head('Avantages · inclus', 'Ce qui est inclus, sans supplément.', '', 'avantages-t')}
        <div class="tsa">
          <article class="tsa__c" data-reveal>
            <div class="ax-plate"><div class="ax-plate__core tsa__v">
              <div class="m-card tsa__w"><p class="m-wd__k">Solde du wallet</p><p class="m-wd__v">186 500 <small>XOF</small></p><span class="tsa__pay">Payer le pack avec mon wallet</span><span class="m-tag m-tag--ok">+10 % de crédits offerts</span></div>
            </div></div>
            <h3>Payez vos crédits avec vos ventes</h3>
            <p>10 % de crédits en plus.</p>
          </article>
          <article class="tsa__c" data-reveal>
            <div class="ax-plate"><div class="ax-plate__core tsa__v">
              <div class="m-card tsa__sw"><p class="tsa__swh"><b>Vos boutiques</b><span>3 / 5</span></p><ul>{''.join(f'<li class="{c}"><span class="tsa__av" style="--c:{col}">{l}</span><span><b>{n}</b><small>{d}</small></span>{ck}</li>' for c, col, l, n, d, ck in (('is-on', '#0866FF', 'S', 'Studio Aïcha', 'studio-aicha.mepaye.shop', '<svg aria-hidden="true"><use href="#i-check"/></svg>'), ('', '#0E8A6A', 'W', 'Wellness Pro', 'wellness.mepaye.shop', ''), ('', '#D9622B', 'D', 'Digital Habit', 'habit.mepaye.shop', '')))}</ul><p class="tsa__add"><span>+</span>Ajouter<em>Sans frais</em></p></div>
            </div></div>
            <h3>Jusqu’à 5 boutiques</h3>
            <p>Un seul compte.</p>
          </article>
          <article class="tsa__c" data-reveal>
            <div class="ax-plate"><div class="ax-plate__core tsa__v">
              <div class="m-card tsa__r"><div class="fxh__notif"><img src="assets/logos/orange.svg" alt=""><span><b>Retrait reçu</b><small>+120 000 XOF · Orange Money</small></span></div><p class="tsa__t"><svg aria-hidden="true"><use href="#i-clock"/></svg>Moins de 2 heures</p></div>
            </div></div>
            <h3>Retraits en moins de 2 heures</h3>
            <p>Sur votre Mobile Money. <a href="aide-demander-retrait-gains.html">Comment retirer</a></p>
          </article>
        </div>
      </div>
    </section>
''' + ax_faq([
    ('Faut-il payer pour ouvrir une boutique ?', 'Non. La création de boutique est gratuite, sans abonnement, et sans carte bancaire pour commencer.'),
    ('Sur quel montant les 5 % sont-ils calculés ?', 'Sur le montant payé par le client, dans la devise de la vente. Les frais de l’opérateur Mobile Money ou de la carte, en général 1 à 2 %, sont en plus. Tout est détaillé dans votre wallet. <a href="aide-commission-5-pourcent-comment-calculee.html">En savoir plus</a>.'),
    ('Et en cas de remboursement ?', 'Pour un remboursement intégral, la commission mepaye vous est rendue. Les frais de l’opérateur peuvent rester acquis.'),
    ('Puis-je payer mes crédits avec mes ventes ?', 'Oui. Payez votre pack depuis votre wallet mepaye : vous recevez 10 % de crédits en plus.'),
]) + '\n' + ax_end('Commencez gratuitement.', 'Ouvrir votre boutique ne coûte rien. Vous payez seulement quand vous vendez.', 'Commencer gratuitement', 'inscription.html')
